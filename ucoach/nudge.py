"""ucoach nudge: avisos proactivos deterministas, sin LLM (research/03 y 04).

- Revisa el estado cada 30 min (lo lanza launchd, systemd o el Programador de tareas).
- Presupuesto: avisos_max_dia (por defecto 3, nunca más de 4), nunca dos en 60 min.
- Silencio: antes de despertar, desde 30 min antes de dormir, durante el foco y las reuniones,
  en días libres, con «hoy no» y con snooze. En modo sostener solo quedan luz y desconexión.
- Aleatorización simple (fija, sin aprendizaje) en los avisos de movimiento: cada decisión
  queda registrada, se envíe o no, para poder medir su efecto en la validación.
- Las plantillas son fijas: ni datos de salud ni títulos de reuniones ni texto del usuario.
"""

from __future__ import annotations

import json
import random
from datetime import date, datetime

from ucoach.core.coach import focal_habit, habit_phase, last_activity
from ucoach.core.planner import chains
from ucoach.core.util import to_hhmm, to_min

TEMPLATES = {
    "luz_matinal": "Buenos días. Sal 10-20 minutos a la luz exterior.",
    "abre_brief": "Tu brief de hoy te espera: abre tu IA y pide el brief de mañana.",
    "retomar": "¿Retomamos? Hoy basta con la versión de 2 minutos de tu hábito.",
    "habito_focal": "Momento de tu hábito focal.",
    "tras_reuniones": "Llevas un buen rato de reuniones: camina 5-10 minutos antes de seguir.",
    "bajon_tarde": "Bajón de la tarde: paseo corto con luz natural y una tarea fácil.",
    "moverse_tarde": "¿Un paseo de 10 minutos antes de cerrar el día?",
    "ultimo_cafe": "Último café de hoy: a partir de ahora, mejor sin cafeína.",
    "desconexion": "Empieza la desconexión: luz tenue, nada de trabajo y 20 minutos de lectura.",
}
RANDOMIZED = {"tras_reuniones", "bajon_tarde", "moverse_tarde"}
WORK_KINDS = {"abre_brief", "tras_reuniones", "bajon_tarde", "moverse_tarde"}
MAX_PER_DAY = 4
MIN_GAP = 60


def _blocks(db, iso: str) -> list[dict]:
    r = db.one("SELECT blocks FROM plans WHERE date=?", (iso,))
    return json.loads(r["blocks"]) if r else []


def _inside(t: int, start: str, end: str) -> bool:
    return to_min(start) <= t < to_min(end)


def candidates(db, now_dt: datetime) -> list[str]:
    p = db.profile()
    t = now_dt.hour * 60 + now_dt.minute
    today = now_dt.date()
    iso = today.isoformat()
    wake, bed = to_min(p["hora_despertar"]), to_min(p["hora_dormir"])
    if bed <= wake:
        bed += 24 * 60
    out = []
    if wake + 10 <= t < wake + 90 and not db.q(
            "SELECT 1 FROM habit_log l JOIN habits h ON h.id=l.habit_id WHERE l.date=? AND lower(h.name) LIKE '%luz%'",
            (iso,)):
        out.append("luz_matinal")
    if to_min("09:00") <= t < to_min("10:30") and not db.one("SELECT 1 FROM plans WHERE date=?", (iso,)):
        out.append("abre_brief")
    last = last_activity(db)
    if to_min("10:00") <= t < to_min("12:00") and last and (today - last).days >= 3:
        out.append("retomar")
    focal = focal_habit(db)
    if focal and focal["hour"] and to_min(focal["hour"]) <= t < to_min(focal["hour"]) + 60 and not db.one(
            "SELECT 1 FROM habit_log WHERE habit_id=? AND date=?", (focal["id"], iso)):
        phase = habit_phase(db, focal, today)
        if phase == "andamio" or (phase == "retirada" and today.toordinal() % 2 == 0):
            out.append("habito_focal")
    meetings = [(to_min(r["start"]), to_min(r["end"])) for r in db.q("SELECT * FROM meetings WHERE date=?", (iso,))]
    if any(e - s >= 120 and 0 <= t - e < 30 for s, e in chains(meetings)):
        out.append("tras_reuniones")
    if to_min("15:00") <= t < to_min("16:30"):
        out.append("bajon_tarde")
    steps = db.one("SELECT value FROM metrics WHERE date=? AND name='pasos'", (iso,))
    if to_min("17:00") <= t < to_min("18:00") and (steps is None or steps["value"] < 4000):
        out.append("moverse_tarde")
    coffee = bed - 9 * 60
    if coffee - 15 <= t < coffee + 15:
        out.append("ultimo_cafe")
    if bed - 60 <= t < bed - 30:
        out.append("desconexion")
    return out


def blocked_reason(db, now_dt: datetime) -> str | None:
    p = db.profile()
    t = now_dt.hour * 60 + now_dt.minute
    iso = now_dt.date().isoformat()
    wake, bed = to_min(p["hora_despertar"]), to_min(p["hora_dormir"])
    if p.get("avisos_canal") == "ninguno" or not p.get("avisos_max_dia"):
        return "avisos desactivados"
    if p.get("hoy_no") == iso:
        return "hoy no"
    if p.get("snooze_hasta") and now_dt < datetime.fromisoformat(p["snooze_hasta"]):
        return "snooze"
    if now_dt.weekday() in (p.get("dias_libres") or []):
        return "día libre"
    late = bed - 30 if bed > wake else bed - 30 + 24 * 60
    if t < wake or t >= late:
        return "horas de silencio"
    for b in _blocks(db, iso):
        if b["tipo"] in ("foco", "siesta") and _inside(t, b["inicio"], b["fin"]):
            return "bloque de " + b["tipo"]
    for m in db.q("SELECT * FROM meetings WHERE date=?", (iso,)):
        if _inside(t, m["start"], m["end"]):
            return "en una reunión"
    sent = db.q("SELECT ts FROM nudges WHERE date=? AND sent=1 ORDER BY ts", (iso,))
    if len(sent) >= min(int(p.get("avisos_max_dia") or 3), MAX_PER_DAY):
        return "presupuesto del día agotado"
    if sent and (now_dt - datetime.fromisoformat(sent[-1]["ts"])).total_seconds() < MIN_GAP * 60:
        return "menos de 60 min desde el último aviso"
    return None


def decide(db, now_dt: datetime, rng: random.Random | None = None) -> dict:
    rng = rng or random.Random()
    p = db.profile()
    iso = now_dt.date().isoformat()
    reason = blocked_reason(db, now_dt)
    if reason:
        return {"enviar": False, "motivo": reason}
    done = {r["kind"] for r in db.q("SELECT kind FROM nudges WHERE date=?", (iso,))}
    kinds = [k for k in candidates(db, now_dt) if k not in done]
    if p.get("modo") == "sostener":
        kinds = [k for k in kinds if k in ("luz_matinal", "desconexion")]
    if not kinds:
        return {"enviar": False, "motivo": "nada pendiente ahora"}
    kind = kinds[0]
    send = True
    if kind in RANDOMIZED:
        send = rng.random() < float(p.get("avisos_probabilidad", 0.7))
    return {"enviar": send, "tipo": kind, "texto": TEMPLATES[kind],
            "motivo": None if send else "aleatorización: esta vez no se envía (queda registrado)"}


def run(db, now_dt: datetime, dry_run: bool = False, sender=None) -> dict:
    d = decide(db, now_dt)
    if "tipo" not in d:
        return d
    channel = None
    if d["enviar"] and not dry_run:
        from ucoach.channels import send
        channel = (sender or send)(d["texto"], db.profile())
    if not dry_run:
        db.conn.execute("INSERT INTO nudges (ts, date, kind, sent, channel) VALUES (?,?,?,?,?)",
                        (now_dt.isoformat(timespec="seconds"), now_dt.date().isoformat(), d["tipo"],
                         int(d["enviar"]), channel))
        db.conn.commit()
    d["canal"] = channel
    return d


def snooze(db, hours: int, now_dt: datetime) -> str:
    from datetime import timedelta
    until = (now_dt + timedelta(hours=hours)).isoformat(timespec="minutes")
    db.set_profile({"snooze_hasta": until})
    return until


def today_no(db, day: date) -> None:
    db.set_profile({"hoy_no": day.isoformat()})


__all__ = ["run", "decide", "candidates", "TEMPLATES", "snooze", "today_no", "to_hhmm"]
