"""ucoach stats: resumen semanal anónimo para la validación (sin telemetría).

El usuario lo copia y lo pega en el formulario de la validación. Solo recuentos:
ni horas de sueño, ni ánimo, ni títulos.
"""

from __future__ import annotations

from datetime import date, timedelta

from ucoach.core.coach import focal_habit


def _week(db, end: date) -> dict:
    dates = [(end - timedelta(days=i)).isoformat() for i in range(6, -1, -1)]
    marks = ",".join("?" * 7)
    briefs = len(db.q(f"SELECT 1 FROM plans WHERE date IN ({marks})", tuple(dates)))
    cierres = len(db.q(f"SELECT DISTINCT substr(ts,1,10) FROM checkins WHERE moment='cierre' AND substr(ts,1,10) IN ({marks})",
                       tuple(dates)))
    noches = len(db.q(f"SELECT 1 FROM sleep WHERE date IN ({marks})", tuple(dates)))
    focal = focal_habit(db)
    focal_days = len(db.q(f"SELECT 1 FROM habit_log WHERE habit_id=? AND date IN ({marks})",
                          (focal["id"], *dates))) if focal else None
    destacados = db.q(f"SELECT highlight FROM checkins WHERE highlight IS NOT NULL AND substr(ts,1,10) IN ({marks})",
                      tuple(dates))
    nudges = db.q(f"SELECT sent FROM nudges WHERE date IN ({marks})", tuple(dates))
    return {"semana_hasta": end.isoformat(), "rituales": briefs + cierres, "semana_activa": briefs + cierres >= 3,
            "briefs": briefs, "cierres": cierres, "noches_con_dato": noches, "habito_focal_dias": focal_days,
            "destacados_cumplidos": sum(1 for r in destacados if r["highlight"] == "si"),
            "destacados_registrados": len(destacados),
            "avisos_enviados": sum(r["sent"] for r in nudges), "avisos_no_enviados_por_sorteo": sum(1 - r["sent"] for r in nudges)}


def returns(db, end: date, weeks: int = 8) -> dict:
    """Tasa de vuelta: tras 3 días o más sin actividad, ¿vuelve en los 7 días siguientes?"""
    start = end - timedelta(days=7 * weeks)
    active = set()
    for sql in ("SELECT date d FROM plans", "SELECT substr(ts,1,10) d FROM checkins", "SELECT date d FROM habit_log",
                "SELECT date d FROM sleep WHERE source='manual'"):
        active |= {r["d"] for r in db.q(sql)}
    gaps, back = 0, 0
    day, run = start, 0
    while day <= end:
        if day.isoformat() in active:
            run = 0
        else:
            run += 1
            if run == 3:
                gaps += 1
                if any((day + timedelta(days=i)).isoformat() in active for i in range(1, 8)):
                    back += 1
        day += timedelta(days=1)
    return {"pausas_de_3_dias": gaps, "vueltas_en_7_dias": back}


def report(db, end: date, weeks: int = 1) -> str:
    lines = ["Ucoach · resumen anónimo (pégalo en el formulario de la validación)"]
    for w in range(weeks):
        s = _week(db, end - timedelta(days=7 * w))
        lines.append(f"- Semana hasta {s['semana_hasta']}: rituales {s['rituales']} "
                     f"({'activa' if s['semana_activa'] else 'no activa'}), briefs {s['briefs']}, cierres {s['cierres']}, "
                     f"noches con dato {s['noches_con_dato']}, hábito focal {s['habito_focal_dias']} días, "
                     f"destacados {s['destacados_cumplidos']} de {s['destacados_registrados']}, "
                     f"avisos enviados {s['avisos_enviados']} (no enviados por sorteo {s['avisos_no_enviados_por_sorteo']})")
    r = returns(db, end)
    lines.append(f"- Pausas de 3 días o más en 8 semanas: {r['pausas_de_3_dias']}; vueltas en 7 días: {r['vueltas_en_7_dias']}")
    lines.append("- Pregunta: ¿qué cambiaste esta semana por Ucoach? (contesta en el formulario)")
    return "\n".join(lines)
