"""Contexto del día, hábitos, check-ins y revisión semanal."""

from __future__ import annotations

import random
from datetime import date, datetime, timedelta

from ucoach.core import sleep as sleepmod
from ucoach.core.util import days_back, load_json
from ucoach.db import now

# Señales de bienestar con umbral interno: solo disparan una sugerencia de derivación
# (research/03 y 05). Nunca se muestran como medida clínica.
MOOD_LOW_DAYS = 7


# --- hábitos ---------------------------------------------------------------
def define_habit(db, name: str, anchor=None, mini=None, hour=None, weekly_target=None,
                 focal=None, status=None) -> dict:
    row = db.one("SELECT * FROM habits WHERE name=?", (name,))
    data = dict(row) if row else {"name": name, "weekly_target": 5, "focal": 0, "status": "activo",
                                  "created": now().date().isoformat()}
    for k, v in {"anchor": anchor, "mini": mini, "hour": hour, "weekly_target": weekly_target,
                 "status": status}.items():
        if v is not None:
            data[k] = v
    if focal is not None:
        data["focal"] = int(bool(focal))
        if focal:  # solo un hábito focal a la vez
            db.conn.execute("UPDATE habits SET focal=0 WHERE name<>?", (name,))
    db.upsert("habits", data, "definir_habito")
    return dict(db.one("SELECT * FROM habits WHERE name=?", (name,)))


def log_habit(db, name: str, day: date) -> dict:
    row = db.one("SELECT * FROM habits WHERE name=?", (name,))
    habit = dict(row) if row else define_habit(db, name)
    db.upsert("habit_log", {"habit_id": habit["id"], "date": day.isoformat()}, "registrar_habito")
    done = len(db.q("SELECT 1 FROM habit_log WHERE habit_id=? AND date IN (%s)" % ",".join("?" * 14),
                    (habit["id"], *days_back(day, 14))))
    return {"habito": name, "fecha": day.isoformat(), "ultimos_14_dias": f"{done} de 14"}


def habit_phase(db, habit: dict, day: date) -> str:
    """andamio: aviso diario; retirada: días alternos; sin_aviso: automatizado (research/03)."""
    if habit["status"] == "automatico":
        return "sin_aviso"
    latest = db.one("SELECT score FROM srbai WHERE habit_id=? ORDER BY date DESC LIMIT 1", (habit["id"],))
    if latest and latest["score"] >= 5.5:
        return "sin_aviso"
    done = len(db.q("SELECT 1 FROM habit_log WHERE habit_id=? AND date IN (%s)" % ",".join("?" * 21),
                    (habit["id"], *days_back(day, 21))))
    return "retirada" if done >= 18 else "andamio"


def focal_habit(db) -> dict | None:
    r = db.one("SELECT * FROM habits WHERE focal=1 AND status<>'archivado'")
    return dict(r) if r else None


def record_srbai(db, name: str, items: list[int], day: date) -> dict:
    """SRBAI: 4 ítems de acuerdo de 1 a 7 (Gardner et al. 2012)."""
    habit = db.one("SELECT * FROM habits WHERE name=?", (name,))
    if not habit:
        raise ValueError(f"no existe el hábito {name!r}")
    score = round(sum(items) / len(items), 2)
    db.upsert("srbai", {"habit_id": habit["id"], "date": day.isoformat(), "score": score}, "srbai")
    return {"habito": name, "automaticidad": score, "escala": "1-7"}


# --- check-ins -----------------------------------------------------------------
def checkin(db, **kw) -> dict:
    row = {"ts": now().isoformat(timespec="minutes"), "moment": kw.get("momento"),
           "energy": kw.get("energia"), "mood": kw.get("animo"), "focus": kw.get("foco"),
           "highlight": kw.get("destacado_cumplido"), "focus_minutes": kw.get("minutos_foco"),
           "worked_after_end": None if kw.get("trabajo_tras_hora_fin") is None else int(kw["trabajo_tras_hora_fin"])}
    db.upsert("checkins", row, "registrar_checkin")
    return {"registrado": True, "momento": row["moment"]}


# --- actividad y señales -----------------------------------------------------------
def last_activity(db) -> date | None:
    dates = []
    for sql in ("SELECT MAX(date) d FROM sleep WHERE source='manual'", "SELECT MAX(date) d FROM habit_log",
                "SELECT MAX(substr(ts,1,10)) d FROM checkins", "SELECT MAX(date) d FROM plans"):
        r = db.one(sql)
        if r and r["d"]:
            dates.append(date.fromisoformat(r["d"]))
    return max(dates) if dates else None


def wellbeing_signals(db, day: date) -> list[str]:
    """Tipos de derivación sugeridos por datos (umbral interno). La IA llama a senal_de_alerta."""
    out = []
    moods = db.q("SELECT substr(ts,1,10) d, MIN(mood) m FROM checkins WHERE mood IS NOT NULL "
                 "AND substr(ts,1,10) >= ? GROUP BY d", ((day - timedelta(days=MOOD_LOW_DAYS - 1)).isoformat(),))
    if len(moods) >= MOOD_LOW_DAYS and all(r["m"] <= 2 for r in moods):
        out.append("animo-bajo-persistente")
    energy = db.q("SELECT substr(ts,1,10) d, AVG(energy) e FROM checkins WHERE energy IS NOT NULL "
                  "AND substr(ts,1,10) >= ? GROUP BY d", ((day - timedelta(days=13)).isoformat(),))
    week = [r["hours"] for r in db.q("SELECT hours FROM sleep WHERE date IN (%s)" % ",".join("?" * 7),
                                     tuple(days_back(day, 7)))]
    if len(energy) >= 10 and all(r["e"] <= 2 for r in energy) and week and min(week) >= 7:
        out.append("fatiga-persistente")
    return out


def day_context(db, day: date, detail: bool = False) -> dict:
    st = sleepmod.sleep_state(db, day)
    p = db.profile()
    iso = day.isoformat()
    metrics = {r["name"]: r["value"] for r in db.q("SELECT name, value FROM metrics WHERE date=?", (iso,))}
    habits_today = [r["name"] for r in db.q(
        "SELECT h.name FROM habit_log l JOIN habits h ON h.id=l.habit_id WHERE l.date=?", (iso,))]
    checkins = [dict(r) for r in db.q("SELECT moment, energy, mood, focus, highlight FROM checkins "
                                      "WHERE substr(ts,1,10)=? ORDER BY ts", (iso,))]
    last = last_activity(db)
    inactive = (day - last).days if last else None
    focal = focal_habit(db)
    ctx = {
        "fecha": iso,
        "sueno": st,
        "habito_focal": None if not focal else {"nombre": focal["name"], "ancla": focal["anchor"],
                                                "version_minima": focal["mini"], "fase": habit_phase(db, focal, day)},
        "habitos_hoy": habits_today,
        "checkins_hoy": checkins,
        "dias_sin_actividad": inactive,
        "sugerir_ritual_retomar": inactive is not None and inactive >= 3,
        "senales_para_derivar": wellbeing_signals(db, day),
        "modo": p.get("modo"),
        "modo_sin_numeros": p.get("modo_sin_numeros"),
        "recordatorio": "Datos del usuario antes que estudios. Una pregunta por mensaje. Si hay señales para derivar, "
                        "usa senal_de_alerta y no improvises.",
    }
    if detail:
        ctx["metricas_hoy"] = metrics
        ctx["jet_lag_social_min"] = sleepmod.social_jetlag(db, day, p.get("dias_libres") or [5, 6])
    if p.get("modo_sin_numeros"):
        ctx["sueno"] = {"estado": st["estado"], "deuda_acumulada": st["deuda_acumulada"], "nota": st["nota"]}
    return ctx


# --- revisión semanal ------------------------------------------------------------------
def weekly_review(db, day: date) -> dict:
    p = db.profile()
    dates = days_back(day, 7)
    marks = ",".join("?" * 7)
    sleep_rows = db.q(f"SELECT date, hours FROM sleep WHERE date IN ({marks})", tuple(dates))
    hours = [r["hours"] for r in sleep_rows]
    ck = db.q(f"SELECT * FROM checkins WHERE substr(ts,1,10) IN ({marks})", tuple(dates))
    energies = [r["energy"] for r in ck if r["energy"] is not None]
    highlights = [r["highlight"] for r in ck if r["highlight"]]

    habits = []
    for h in db.q("SELECT * FROM habits WHERE status<>'archivado'"):
        done = len(db.q(f"SELECT 1 FROM habit_log WHERE habit_id=? AND date IN ({marks})", (h["id"], *dates)))
        weeks = max(1, (day - date.fromisoformat(h["created"])).days // 7 + 1)
        habits.append({"nombre": h["name"], "hechos": done, "objetivo": h["weekly_target"],
                       "focal": bool(h["focal"]), "semanas": weeks, "fase": habit_phase(db, dict(h), day)})

    metrics = {
        "sueno_media_h": round(sum(hours) / len(hours), 1) if hours else None,
        "noches_bajo_6h": sum(1 for h in hours if h < 6),
        "energia_media": round(sum(energies) / len(energies), 1) if energies else None,
        "destacados": f"{highlights.count('si')} de {len(highlights)}" if highlights else None,
    }
    comparison = sleep_energy_comparison(db, day)
    focal = next((h for h in habits if h["focal"]), None)
    suggestions = []
    if focal:
        if focal["hechos"] < focal["objetivo"]:
            suggestions.append(f"Mismo hábito focal ({focal['nombre']}), un solo ajuste: hazlo más pequeño, "
                               "cambia el ancla o la hora.")
        elif focal["semanas"] >= 8:
            suggestions.append("Mide la automaticidad del hábito focal (4 preguntas de 1 a 7) antes de cambiar de hábito.")
        else:
            suggestions.append(f"Mantén el hábito focal ({focal['nombre']}): lleva {focal['semanas']} de 8-10 semanas.")
    else:
        suggestions.append("Elige un hábito focal con su ancla («después de...») y su versión de 2 minutos.")
    if metrics["noches_bajo_6h"] >= 3:
        suggestions.append("Tres noches o más por debajo de 6 h: protege la hora de despertar y adelanta la desconexión.")
    weak = min((h for h in habits if not h["focal"]), key=lambda h: h["hechos"] / max(1, h["objetivo"]), default=None)
    return {
        "semana_hasta": day.isoformat(),
        "metricas": metrics,
        "metricas_activas": p.get("metricas_activas"),
        "habitos": habits,
        "energia_segun_sueno": comparison,
        "sugerencias": suggestions[:3],
        "libro": suggest_book(weak["nombre"] if weak else (focal["nombre"] if focal else "")),
        "estructura": "GROW: ¿qué quieres que sea distinto el viernes? · ¿dónde estás del 1 al 10? · "
                      "¿qué funcionó otra vez? · ¿qué harás exactamente, cuándo y dónde?",
    }


def sleep_energy_comparison(db, day: date) -> dict:
    """Energía tras dormir 7 h o más frente al resto. Mínimo 14 días y 5 por grupo; sin causalidad."""
    dates = days_back(day, 28)
    by_day = {}
    for r in db.q("SELECT substr(ts,1,10) d, AVG(energy) e FROM checkins WHERE energy IS NOT NULL "
                  "AND substr(ts,1,10) >= ? GROUP BY d", (dates[0],)):
        by_day[r["d"]] = r["e"]
    good, rest = [], []
    for r in db.q("SELECT date, hours FROM sleep WHERE date >= ?", (dates[0],)):
        if r["date"] in by_day:
            (good if r["hours"] >= 7 else rest).append(by_day[r["date"]])
    if len(good) + len(rest) < 14 or len(good) < 5 or len(rest) < 5:
        return {"disponible": False, "motivo": "Hacen falta 14 días con datos y 5 en cada grupo."}
    diff = round(sum(good) / len(good) - sum(rest) / len(rest), 1)
    return {"disponible": True, "diferencia_energia": diff, "dias_7h_o_mas": len(good), "dias_resto": len(rest),
            "lectura": "Es una asociación en tus datos, no una prueba de causa."}


AREA_HINTS = {"lectura": "aprendizaje", "luz": "sueno", "sueno": "sueno", "dormir": "sueno", "foco": "foco",
              "medit": "mente", "camin": "deporte", "fuerza": "deporte", "deporte": "deporte",
              "agua": "alimentacion", "comida": "alimentacion", "pausa": "postura"}


def suggest_book(habit_name: str) -> dict | None:
    books = load_json("biblioteca.json")
    if not books:
        return None
    area = next((a for k, a in AREA_HINTS.items() if k in (habit_name or "").lower()), "habitos")
    pool = [b for b in books if b.get("area") == area] or [b for b in books if b.get("area") == "habitos"]
    if not pool:
        return None
    b = random.Random(f"{habit_name}{datetime.now().isocalendar()[1]}").choice(pool)
    return {k: b.get(k) for k in ("titulo", "autor", "idea", "accion", "aviso")}
