"""Ergonomía, auditoría de agenda, experimentos n-de-1, estimaciones, derivación, biblioteca y prácticas."""

from __future__ import annotations

import json
import random
import statistics
import unicodedata
from datetime import date, timedelta

from ucoach.core.planner import chains
from ucoach.core.util import load_json, to_min
from ucoach.db import now

# --- ergonomía (comodidad, no prevención probada: research/02 y 07) -----------------------
ERGONOMIA = [
    ("varias_posturas", "¿Cambias de postura a menudo (sentado, de pie, caminando en llamadas)?",
     "La mejor postura es la siguiente: cambia de posición en cada llamada."),
    ("pantalla_altura_ojos", "¿El borde superior de la pantalla está a la altura de los ojos o un poco por debajo?",
     "Sube la pantalla hasta que el borde superior quede a la altura de los ojos o algo por debajo."),
    ("pantalla_distancia_brazo", "¿La pantalla está a un brazo de distancia (50-75 cm)?",
     "Aleja la pantalla a un brazo de distancia."),
    ("pies_apoyados", "¿Apoyas los pies planos en el suelo o en un reposapiés?",
     "Apoya los pies en el suelo o en un reposapiés."),
    ("codos_90_110", "¿Los codos quedan a unos 90-110° con los hombros relajados?",
     "Ajusta silla o mesa para que los codos queden a 90-110° y los hombros sueltos."),
    ("espalda_apoyada", "¿Usas el respaldo, con apoyo en la zona lumbar?",
     "Usa el respaldo; un cojín pequeño ayuda si no tiene apoyo lumbar."),
    ("luz_natural_lateral", "¿La ventana te queda a un lado, no detrás ni delante de la pantalla?",
     "Coloca la mesa con la ventana a un lado."),
    ("sin_reflejos", "¿La pantalla está libre de reflejos?",
     "Inclina la pantalla o cambia la fuente de luz para quitar reflejos."),
    ("teclado_raton_cerca", "¿Teclado y ratón están cerca, sin estirar los brazos?",
     "Acerca teclado y ratón."),
    ("portatil_elevado", "Si usas portátil, ¿lo elevas y usas teclado y ratón externos?",
     "Eleva el portátil y usa teclado y ratón externos."),
    ("alterna_de_pie", "¿Alternas sentado y de pie, o al menos te levantas en cada llamada?",
     "Alterna sentado y de pie; la mesa elevable reduce el tiempo sentado, aunque su beneficio para la salud no está probado."),
]


def ergonomics(db, answers: dict | None) -> dict:
    if not answers:
        return {"preguntas": [{"clave": k, "pregunta": q} for k, q, _ in ERGONOMIA],
                "nota": "Responde con true o false. Es una guía de comodidad, no una prevención probada del dolor."}
    known = {k for k, _, _ in ERGONOMIA}
    unknown = set(answers) - known
    if unknown:
        raise ValueError(f"claves desconocidas: {sorted(unknown)}")
    fails = [fix for k, _, fix in ERGONOMIA if k in answers and answers[k] is False]
    score = round(100 * sum(1 for k in answers if answers[k]) / len(answers))
    db.upsert("ergonomics", {"ts": now().isoformat(timespec="seconds"), "answers": json.dumps(answers),
                             "score": score}, "chequeo_ergonomia")
    return {"puntuacion": score, "mejoras": fails[:3], "resto": fails[3:],
            "nota": "Empieza por una sola mejora. Si hay dolor de espalda o cuello que no mejora en 4-6 semanas, "
                    "usa senal_de_alerta (dolor-espalda-persistente)."}


# --- auditoría de agenda -------------------------------------------------------------------
def audit_agenda(db, events: list[dict], days: int = 5) -> dict:
    p = db.profile()
    ws, we = to_min(p["hora_inicio_trabajo"]), to_min(p["hora_fin_trabajo"])
    by_day: dict[str, list[tuple[int, int]]] = {}
    outside = 0
    for e in events:
        s, f = to_min(e["inicio"]), to_min(e["fin"])
        by_day.setdefault(e.get("fecha", "dia"), []).append((s, f))
        if s < ws or f > we:
            outside += 1
    total_work = (we - ws) * max(days, len(by_day))
    meeting_min = sum(f - s for v in by_day.values() for s, f in v)
    focus_blocks, long_chains = 0, 0
    for v in by_day.values():
        cursor = ws
        for s, f in sorted(v):
            if s - cursor >= 60:
                focus_blocks += 1
            cursor = max(cursor, f)
        if we - cursor >= 60:
            focus_blocks += 1
        long_chains += sum(1 for s, f in chains(v) if f - s >= 120)
    return {"porcentaje_reuniones": round(100 * meeting_min / total_work) if total_work else None,
            "huecos_de_foco_60min": focus_blocks, "cadenas_de_2h_o_mas": long_chains,
            "reuniones_fuera_de_horario": outside,
            "accion": "Elige una sola acción: proteger un bloque fijo, acortar recurrentes a 25 o 50 min, o probar una "
                      "mañana sin reuniones durante 4 semanas y mirar tus datos.",
            "nota": "Los datos de reparto de agenda de grandes CEO no son de fundadores; compárate contigo mismo."}


# --- experimentos n-de-1 --------------------------------------------------------------------
def experiment(db, accion: str, variable=None, opcion_a=None, opcion_b=None, dias: int = 14) -> dict:
    if accion == "crear":
        if not (variable and opcion_a and opcion_b):
            raise ValueError("para crear hacen falta variable, opcion_a y opcion_b")
        if not 14 <= dias <= 28:
            raise ValueError("un experimento dura entre 14 y 28 días")
        start = now().date()
        rng = random.Random()
        schedule = {}
        for week in range(0, dias, 7):  # aleatorización por días, equilibrada en cada semana
            arms = ["A"] * 4 + ["B"] * 3 if rng.random() < 0.5 else ["A"] * 3 + ["B"] * 4
            rng.shuffle(arms)
            for i, arm in enumerate(arms):
                if week + i < dias:
                    schedule[(start + timedelta(days=week + i)).isoformat()] = arm
        db.conn.execute("UPDATE experiments SET status='cerrado' WHERE status='activo'")
        db.upsert("experiments", {"variable": variable, "option_a": opcion_a, "option_b": opcion_b,
                                  "start": start.isoformat(), "days": dias, "schedule": json.dumps(schedule),
                                  "status": "activo"}, "experimento")
        return {"creado": True, "variable": variable, "A": opcion_a, "B": opcion_b, "dias": dias,
                "hoy": schedule[start.isoformat()]}
    exp = db.one("SELECT * FROM experiments WHERE status='activo' ORDER BY id DESC LIMIT 1")
    if not exp:
        return {"activo": False}
    schedule = json.loads(exp["schedule"])
    today = now().date().isoformat()
    if accion == "hoy":
        arm = schedule.get(today)
        return {"variable": exp["variable"], "hoy": arm,
                "opcion": exp["option_a"] if arm == "A" else exp["option_b"] if arm == "B" else None}
    if accion == "resumen":
        res = {"A": [], "B": []}
        for d, arm in schedule.items():
            r = db.one("SELECT AVG(energy) e FROM checkins WHERE substr(ts,1,10)=? AND energy IS NOT NULL", (d,))
            if r and r["e"] is not None:
                res[arm].append(r["e"])
        out = {"variable": exp["variable"], "A": exp["option_a"], "B": exp["option_b"],
               "dias_con_dato": {k: len(v) for k, v in res.items()}}
        if min(len(res["A"]), len(res["B"])) < 5:
            out["lectura"] = "Aún no hay datos suficientes (5 días con check-in en cada opción)."
            return out
        ma, mb = statistics.mean(res["A"]), statistics.mean(res["B"])
        se = (statistics.pvariance(res["A"]) / len(res["A"]) + statistics.pvariance(res["B"]) / len(res["B"])) ** 0.5
        out.update({"energia_media_A": round(ma, 2), "energia_media_B": round(mb, 2),
                    "diferencia": round(ma - mb, 2), "margen_aprox": round(2 * se, 2),
                    "lectura": "Si la diferencia es menor que el margen, no hay una diferencia clara. "
                               "Es tu dato personal, con incertidumbre, no una prueba general."})
        if accion == "resumen" and len(schedule) and today > max(schedule):
            db.conn.execute("UPDATE experiments SET status='cerrado' WHERE id=?", (exp["id"],))
            db.conn.commit()
        return out
    raise ValueError("accion debe ser crear, hoy o resumen")


def estimate(db, tarea: str, estimado: int, real: int | None) -> dict:
    db.upsert("estimates", {"ts": now().isoformat(timespec="minutes"), "task": tarea[:80],
                            "estimated": estimado, "actual": real}, "registrar_estimacion")
    rows = db.q("SELECT estimated, actual FROM estimates WHERE actual IS NOT NULL ORDER BY id DESC LIMIT 20")
    ratio = round(sum(r["actual"] for r in rows) / sum(r["estimated"] for r in rows), 2) if len(rows) >= 5 else None
    return {"registrado": True, "factor_corrector": ratio,
            "nota": None if ratio is None else f"Tus tareas suelen llevar {ratio} veces lo estimado."}


# --- derivación fija ---------------------------------------------------------------------
def alert(tipo: str) -> dict:
    table = {d["tipo"]: d for d in load_json("derivacion.json")}
    if tipo not in table:
        return {"error": f"tipo desconocido; usa uno de: {sorted(table)}"}
    d = table[tipo]
    return {"tipo": tipo, "texto": d["texto"], "recursos": d.get("recursos", []),
            "detiene_coaching": d.get("detiene_coaching", False), "modo": d.get("modo"),
            "instruccion": "Muestra el texto tal cual, sin añadir diagnósticos ni consejos médicos."}


def alert_types() -> list[str]:
    return [d["tipo"] for d in load_json("derivacion.json")]


# --- biblioteca y prácticas ----------------------------------------------------------------
def _n(s: str) -> str:
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def library(db, area=None, texto=None, limite: int = 5) -> dict:
    books = load_json("biblioteca.json")
    status = {r["book_id"]: r["status"] for r in db.q("SELECT * FROM reading")}
    out = []
    for b in books:
        if area and b.get("area") != area:
            continue
        if texto and _n(texto) not in _n(" ".join(str(b.get(k, "")) for k in ("titulo", "autor", "idea", "accion"))):
            continue
        out.append({**{k: b.get(k) for k in ("id", "titulo", "autor", "area", "idea", "accion", "aviso")},
                    "estado": status.get(b["id"])})
    return {"libros": out[:limite], "total": len(out),
            "nota": "Ideas resumidas con palabras propias: no cites ni reproduzcas el texto de los libros."}


def mark_book(db, book_id: str, estado: str) -> dict:
    ids = {b["id"] for b in load_json("biblioteca.json")}
    if book_id not in ids:
        raise ValueError(f"no existe el libro {book_id!r}; búscalo con biblioteca")
    db.upsert("reading", {"book_id": book_id, "status": estado, "updated": now().date().isoformat()}, "marcar_libro")
    nota = "Al terminar: escribe de memoria 3 ideas y una acción con fecha." if estado == "leido" else None
    return {"libro": book_id, "estado": estado, "nota": nota}


def practice(texto=None, nivel=None, area=None) -> dict:
    items = load_json("practicas.json")
    out = []
    for p in items:
        if nivel and p.get("nivel") != nivel:
            continue
        if area and area not in (p.get("areas") or []):
            continue
        if texto and _n(texto) not in _n(p.get("practica", "") + " " + p.get("id", "")):
            continue
        out.append(p)
    return {"practicas": out[:8], "total": len(out),
            "regla": "Por defecto, solo prácticas A. Las B si hay contexto. Las C y D solo si el usuario pregunta: "
                     "lo que se sabe, lo que no, el riesgo y la mejor alternativa. Nunca dosis personalizadas ni marcas."}
