"""Importador de Apple Health (export.xml) en streaming y endurecido.

- Rechaza el fichero si declara entidades XML (<!ENTITY): evita ataques de expansión.
- Avisa si la versión de Expat es antigua (research/04 recomienda Expat 2.7.2 o superior).
- Sueño: suma de los intervalos «asleep» por fecha de despertar. Pasos: suma diaria.
  VFC (SDNN), frecuencia cardiaca en reposo y peso: media diaria.
"""

from __future__ import annotations

import pyexpat
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime
from pathlib import Path

SLEEP = "HKCategoryTypeIdentifierSleepAnalysis"
QUANTITIES = {
    "HKQuantityTypeIdentifierStepCount": ("pasos", "sum"),
    "HKQuantityTypeIdentifierHeartRateVariabilitySDNN": ("vfc", "mean"),
    "HKQuantityTypeIdentifierRestingHeartRate": ("fc_reposo", "mean"),
    "HKQuantityTypeIdentifierBodyMass": ("peso", "mean"),
}


def _dt(s: str) -> datetime:
    return datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S")


def check_safe(path: Path, allow_dtd: bool = False) -> list[str]:
    warnings = []
    head = path.open("rb").read(1 << 16).decode("utf-8", "ignore")
    if "<!ENTITY" in head and not allow_dtd:
        raise ValueError("El fichero declara entidades XML (<!ENTITY): no se importa por seguridad.")
    version = tuple(int(x) for x in pyexpat.EXPAT_VERSION.split("_")[1].split("."))
    if version < (2, 7, 2):
        warnings.append(f"Expat {pyexpat.EXPAT_VERSION}: conviene actualizar Python (Expat 2.7.2 o superior).")
    return warnings


def import_file(db, path: str, allow_dtd: bool = False) -> dict:
    p = Path(path).expanduser()
    warnings = check_safe(p, allow_dtd)
    sleep = defaultdict(float)
    bounds: dict[str, list[datetime]] = {}
    qty = defaultdict(list)
    for _, el in ET.iterparse(p, events=("end",)):
        if el.tag == "Record":
            t = el.get("type")
            if t == SLEEP and "Asleep" in (el.get("value") or ""):
                s, e = _dt(el.get("startDate")), _dt(el.get("endDate"))
                key = e.date().isoformat()
                sleep[key] += (e - s).total_seconds() / 3600
                b = bounds.setdefault(key, [s, e])
                b[0], b[1] = min(b[0], s), max(b[1], e)
            elif t in QUANTITIES:
                try:
                    qty[(QUANTITIES[t][0], _dt(el.get("startDate")).date().isoformat())].append(float(el.get("value")))
                except (TypeError, ValueError):
                    pass
        el.clear()
    n_sleep = 0
    for d, h in sleep.items():
        if 0 < h <= 16:
            s, e = bounds[d]
            db.conn.execute("INSERT OR REPLACE INTO sleep (date, hours, bedtime, waketime, source) VALUES (?,?,?,?,?)",
                            (d, round(h, 2), s.strftime("%H:%M"), e.strftime("%H:%M"), "apple_health"))
            n_sleep += 1
    n_metrics = 0
    for (name, d), values in qty.items():
        how = next(m for n, m in QUANTITIES.values() if n == name)
        value = sum(values) if how == "sum" else sum(values) / len(values)
        db.conn.execute("INSERT OR REPLACE INTO metrics (date, name, value, source) VALUES (?,?,?,?)",
                        (d, name, round(value, 2), "apple_health"))
        n_metrics += 1
    db.conn.commit()
    return {"noches": n_sleep, "metricas_diarias": n_metrics, "avisos": warnings}
