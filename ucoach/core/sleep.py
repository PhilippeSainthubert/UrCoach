"""Estado del sueño: media de varias noches, regularidad y jet lag social.

Reglas (research/02):
- La meta es de 7 a 9 h. El estado del día no sale de una sola noche, sino de la media
  de las últimas noches disponibles (3 como mínimo para hablar de tendencia, 7 como máximo).
- Estados: deuda (<6 h), justo (6-7 h), bien (7-9,5 h) y largo (>=9,5 h de forma habitual).
- Tras una sola noche, la sensación del usuario manda. Con deuda acumulada (media de 3 noches
  o más por debajo de 6 h), los avisos se mantienen aunque diga sentirse bien (research/08,
  Van Dongen 2003: el deterioro no se percibe).
"""

from __future__ import annotations

import statistics
from datetime import date

from ucoach.core.util import bed_minutes, days_back, to_min

DEUDA, JUSTO, BIEN, LARGO = "deuda", "justo", "bien", "largo"


def classify(hours: float | None) -> str | None:
    if hours is None:
        return None
    if hours < 6:
        return DEUDA
    if hours < 7:
        return JUSTO
    if hours < 9.5:
        return BIEN
    return LARGO


def sleep_state(db, day: date) -> dict:
    rows = {r["date"]: dict(r) for r in db.q(
        "SELECT * FROM sleep WHERE date IN (%s)" % ",".join("?" * 7), tuple(days_back(day, 7)))}
    last = rows.get(day.isoformat())
    recent = [rows[d]["hours"] for d in days_back(day, 3) if d in rows]
    week = [rows[d]["hours"] for d in days_back(day, 7) if d in rows]
    avg3 = round(sum(recent) / len(recent), 2) if recent else None
    avg7 = round(sum(week) / len(week), 2) if week else None

    # El estado del día usa la media de 3 noches si hay al menos 2; si no, la última noche.
    basis = avg3 if len(recent) >= 2 else (last["hours"] if last else None)
    state = classify(basis)
    accumulated_debt = len(recent) >= 3 and avg3 is not None and avg3 < 6

    return {
        "ultima_noche_h": last["hours"] if last else None,
        "ultima_noche_estado": classify(last["hours"]) if last else None,
        "media_3_noches_h": avg3,
        "media_7_noches_h": avg7,
        "noches_registradas_7d": len(week),
        "estado": state,
        "deuda_acumulada": accumulated_debt,
        "regularidad": regularity(rows.values()),
        "nota": _note(state, accumulated_debt, len(week)),
    }


def regularity(rows) -> dict | None:
    """Variabilidad de las horas de despertar y de dormir (desviación típica en minutos)."""
    wakes = [to_min(r["waketime"]) for r in rows if r.get("waketime")]
    beds = [bed_minutes(r["bedtime"], r["waketime"]) for r in rows if r.get("bedtime") and r.get("waketime")]
    if len(wakes) < 3:
        return None
    sd_wake = round(statistics.pstdev(wakes))
    out = {"despertar_desviacion_min": sd_wake}
    if len(beds) >= 3:
        out["dormir_desviacion_min"] = round(statistics.pstdev(beds))
    out["valoracion"] = "regular" if sd_wake <= 45 else "irregular"
    return out


def social_jetlag(db, day: date, days_off: list[int]) -> int | None:
    """Diferencia en minutos entre el punto medio del sueño de días libres y laborables (14 días)."""
    mids_work, mids_free = [], []
    for d in days_back(day, 14):
        r = db.one("SELECT bedtime, waketime FROM sleep WHERE date=?", (d,))
        if not r or not r["bedtime"] or not r["waketime"]:
            continue
        bed = bed_minutes(r["bedtime"], r["waketime"])
        wake = to_min(r["waketime"]) + 24 * 60
        mid = (bed + wake) / 2
        (mids_free if date.fromisoformat(d).weekday() in days_off else mids_work).append(mid)
    if len(mids_free) < 2 or len(mids_work) < 3:
        return None
    return round(abs(sum(mids_free) / len(mids_free) - sum(mids_work) / len(mids_work)))


def _note(state: str | None, accumulated: bool, nights: int) -> str:
    if state is None:
        return "Sin datos de sueño recientes: pregunta cuánto ha dormido y cómo se siente (1-5)."
    if accumulated:
        return ("Deuda de sueño acumulada: plan más ligero y decisiones irreversibles con una segunda mirada, "
                "aunque se sienta bien (con poco sueño acumulado el bajón no se nota).")
    if nights < 3:
        return "Pocas noches registradas: tras una sola noche, manda cómo se siente el usuario."
    if state == LARGO:
        return "Duerme más de lo habitual de forma sostenida: si va con cansancio persistente, sugiere comentarlo con un profesional."
    return ""
