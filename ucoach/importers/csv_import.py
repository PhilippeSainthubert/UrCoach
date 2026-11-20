"""Importador CSV genérico (Oura, Garmin, WHOOP u otros exportados a CSV).

Columna obligatoria: fecha (o date). Columnas reconocidas (opcionales):
horas_sueno / sleep_hours / hours, calidad / quality, pasos / steps, vfc / hrv,
fc_reposo / rhr / resting_hr, readiness, peso / weight.
"""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

SLEEP_COLS = ("horas_sueno", "sleep_hours", "hours")
METRIC_COLS = {"pasos": "pasos", "steps": "pasos", "vfc": "vfc", "hrv": "vfc", "fc_reposo": "fc_reposo",
               "rhr": "fc_reposo", "resting_hr": "fc_reposo", "readiness": "readiness", "peso": "peso", "weight": "peso"}


def import_file(db, path: str) -> dict:
    n_sleep = n_metrics = 0
    with Path(path).expanduser().open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            row = {k.strip().lower(): (v or "").strip() for k, v in row.items() if k}
            raw = row.get("fecha") or row.get("date")
            try:
                d = date.fromisoformat(raw[:10]).isoformat()
            except (TypeError, ValueError):
                continue
            hours = next((row[c] for c in SLEEP_COLS if row.get(c)), None)
            if hours:
                try:
                    h = float(hours.replace(",", "."))
                    q = row.get("calidad") or row.get("quality")
                    if 0 < h <= 16:
                        db.conn.execute("INSERT OR REPLACE INTO sleep (date, hours, quality, source) VALUES (?,?,?,?)",
                                        (d, h, int(q) if q and q.isdigit() and 1 <= int(q) <= 5 else None, "csv"))
                        n_sleep += 1
                except ValueError:
                    pass
            for col, name in METRIC_COLS.items():
                if row.get(col):
                    try:
                        db.conn.execute("INSERT OR REPLACE INTO metrics (date, name, value, source) VALUES (?,?,?,?)",
                                        (d, name, float(row[col].replace(",", ".")), "csv"))
                        n_metrics += 1
                    except ValueError:
                        pass
    db.conn.commit()
    return {"noches": n_sleep, "metricas": n_metrics}
