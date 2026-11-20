"""planificar_dia: propone el día con las reglas corregidas por el research (02, 07 y 08).

No toca el calendario: devuelve bloques que la IA puede proponer crear con un sí del usuario.
"""

from __future__ import annotations

import re
import unicodedata
from datetime import date, datetime, timedelta

from ucoach.core import sleep as sleepmod
from ucoach.core.util import to_hhmm, to_min

KEY_WORDS = ["inversor", "pitch", "negociacion", "cliente", "entrevista", "board", "consejo",
             "ronda", "demo", "venta", "contratacion", "despido", "feedback"]
CHRONO_PEAK = {"alondra": "09:00", "intermedio": "10:00", "buho": "11:30"}
FOCUS_LEN = {sleepmod.DEUDA: 60, sleepmod.JUSTO: 90, sleepmod.BIEN: 120, sleepmod.LARGO: 90, None: 90}
CONTROL = re.compile(r"[\x00-\x1f\x7f]")


def _norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()
    return text


def sanitize_title(title: str | None) -> str:
    """El título de una reunión es entrada no fiable: se limpia y se trunca."""
    return CONTROL.sub(" ", title or "").strip()[:40]


class Day:
    """Ocupación del día en minutos."""

    def __init__(self, meetings: list[tuple[int, int]]):
        self.busy = sorted(meetings)

    def free(self, start: int, end: int) -> bool:
        return all(end <= s or start >= e for s, e in self.busy)

    def take(self, start: int, end: int) -> None:
        self.busy.append((start, end))
        self.busy.sort()

    def find(self, earliest: int, latest_end: int, length: int, prefer: int | None = None, step: int = 15):
        candidates = []
        t = earliest
        while t + length <= latest_end:
            candidates.append(t)
            t += step
        if prefer is not None:
            candidates.sort(key=lambda c: (c < prefer, abs(c - prefer)))
        for c in candidates:
            if self.free(c, c + length):
                return c
        return None


def learned_peak(db, day: date) -> str | None:
    """Franja de más energía según los check-ins de las 3 últimas semanas (si hay datos suficientes)."""
    since = (day - timedelta(days=21)).isoformat()
    rows = db.q("SELECT ts, energy FROM checkins WHERE energy IS NOT NULL AND ts >= ?", (since,))
    bands: dict[int, list[int]] = {}
    for r in rows:
        hour = datetime.fromisoformat(r["ts"]).hour
        if 8 <= hour < 18:
            bands.setdefault(hour // 2 * 2, []).append(r["energy"])
    good = {b: sum(v) / len(v) for b, v in bands.items() if len(v) >= 3}
    if len(good) < 2:
        return None
    best = max(good, key=good.get)
    return f"{best:02d}:00"


def is_key(meeting: dict, extra_words: list[str]) -> bool:
    if meeting.get("clave"):
        return True
    title = _norm(meeting.get("titulo", ""))
    return any(w in title for w in KEY_WORDS + [_norm(x) for x in extra_words])


def chains(meetings: list[tuple[int, int]], gap: int = 10) -> list[tuple[int, int]]:
    out: list[list[int]] = []
    for s, e in sorted(meetings):
        if out and s - out[-1][1] < gap:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [(s, e) for s, e in out]


def plan_day(db, day: date, meetings: list[dict], destacado: str | None = None, save: bool = True) -> dict:
    p = db.profile()
    wake, bed = to_min(p["hora_despertar"]), to_min(p["hora_dormir"])
    if bed <= wake:
        bed += 24 * 60
    work_start, work_end = to_min(p["hora_inicio_trabajo"]), to_min(p["hora_fin_trabajo"])
    st = sleepmod.sleep_state(db, day)
    state = st["estado"]
    sostener = p.get("modo") == "sostener"

    parsed = []
    for m in meetings:
        s, e = to_min(m["inicio"]), to_min(m["fin"])
        if e <= s:
            raise ValueError(f"la reunión {m.get('titulo', '')!r} termina antes de empezar")
        parsed.append({"s": s, "e": e, "titulo": sanitize_title(m.get("titulo")),
                       "clave": is_key(m, p.get("palabras_clave_momento_clave") or [])})
    d = Day([(m["s"], m["e"]) for m in parsed])
    blocks, alerts = [], []

    def add(start, length, kind, title, note="", exclusive=True):
        blocks.append({"inicio": to_hhmm(start), "fin": to_hhmm(start + length), "tipo": kind,
                       "titulo": title, "nota": note})
        if exclusive:
            d.take(start, start + length)

    # 1. Luz matinal (primera hora y media tras despertar).
    add(wake + 15, 15, "luz", "Luz exterior 10-20 min",
        "En la primera hora y media tras despertar. Si está nublado, algo más de tiempo.", exclusive=False)

    # 2. Preparación de reuniones clave (10 min antes).
    for m in [m for m in parsed if m["clave"]]:
        slot = d.find(m["s"] - 120, m["s"], 10, prefer=m["s"] - 10, step=5)
        if slot is not None:
            add(slot, 10, "preparacion", f"Preparar: {m['titulo'] or 'reunión clave'}",
                "Objetivo en una frase, objeciones que temes y tu límite. Ritual: preparar_momento_clave.")
        else:
            alerts.append("No hay hueco para preparar una reunión clave: prepárala la víspera.")
    if any(m["clave"] for m in parsed) and state == sleepmod.DEUDA:
        alerts.append("Hoy tienes una reunión clave con poco sueño: prepara la frase de apertura y un ejemplo concreto.")

    # 3. Bloque de foco en el pico de energía (60-120 min según el sueño).
    length = 60 if sostener else FOCUS_LEN[state]
    peak_src = "check-ins" if learned_peak(db, day) else "cronotipo"
    peak = to_min(learned_peak(db, day) or CHRONO_PEAK.get(p["cronotipo"], "10:00"))
    peak = max(peak, work_start)
    placed = None
    for ln in (length, 60, 45):
        placed = d.find(work_start, work_end, ln, prefer=peak)
        if placed is not None:
            length = ln
            break
    if placed is None:
        alerts.append("Hoy no queda ningún hueco de 45 min o más para trabajo profundo: elige qué reunión mover o acortar.")
    else:
        add(placed, length, "foco", f"Trabajo profundo {length} min",
            f"Tu destacado del día, con una meta clara. Sin avisos. Levántate 2-3 min cada ~30 min. Pico estimado por {peak_src}.")
        if placed > peak + 60:
            alerts.append("Las reuniones ocupan tu mejor franja de energía: valora mover alguna a la tarde.")

    # 4. Comida (preferible antes de las 15:00).
    lunch = d.find(to_min("12:30"), to_min("15:30"), 45, prefer=to_min("13:30"))
    if lunch is not None:
        add(lunch, 45, "comida", "Comida 45 min", "Sin pantalla si puedes. Evita una comida copiosa si después viene foco.")

    # 5. Siesta si se durmió poco (nunca con dificultad habitual para dormir).
    slept_little = state == sleepmod.DEUDA or st["ultima_noche_estado"] == sleepmod.DEUDA
    if slept_little and not p.get("dificultad_dormir"):
        nap = d.find(to_min("13:00"), to_min("15:00"), 20, prefer=to_min("14:00"))
        if nap is not None:
            add(nap, 20, "siesta", "Siesta 10-20 min",
                "Con alarma y antes de las 15:00. Tras la siesta, espera 15-30 min antes de conducir.")

    # 6. Entreno 45 min con la intensidad según el sueño.
    if p.get("hora_entreno"):
        train_pref = to_min(p["hora_entreno"])
    else:
        train_pref = work_end + 15
    train = d.find(min(train_pref, work_end), bed - 180, 45, prefer=train_pref)
    if train is not None:
        if state == sleepmod.DEUDA:
            intensity = "Mantén la sesión, sin esfuerzos máximos ni trabajo muy técnico"
            if train >= to_min("16:00"):
                intensity += "; si puedes, mejor por la mañana, que es cuando menos se nota el sueño corto"
        elif state == sleepmod.JUSTO:
            intensity = "Intensidad moderada"
        else:
            intensity = "La intensidad que tengas en el plan"
        add(train, 45, "entreno", "Entreno 45 min", intensity + ".")

    # 7. Pausas de 5-10 min cada 60-90 min durante la jornada.
    t = work_start + 90
    while t + 10 <= work_end:
        if d.free(t, t + 10):
            add(t, 10, "pausa", "Pausa 5-10 min", "De pie o caminando, mejor con luz natural.", exclusive=False)
        t += 90

    # 8. Desconexión y lectura.
    add(bed - 60, 60, "desconexion", "Desconexión",
        "Actividad tranquila, sin trabajo, correo ni redes. 20 min de lectura en papel o e-ink. Móvil fuera del dormitorio.",
        exclusive=False)

    # Alertas de agenda.
    for s, e in chains([(m["s"], m["e"]) for m in parsed]):
        if e - s >= 120:
            alerts.append(f"Reuniones seguidas de {to_hhmm(s)} a {to_hhmm(e)} sin pausa: mete 5-10 min entre ellas si puedes.")
    if any(m["s"] < work_start or m["e"] > work_end for m in parsed):
        alerts.append("Hay reuniones fuera de tu horario de trabajo.")
    if st["deuda_acumulada"] or state == sleepmod.DEUDA:
        alerts.append("Con poco sueño: aplaza o contrasta con otra persona las decisiones irreversibles.")
    if sostener:
        alerts.append("Modo sostener: hoy no hay metas nuevas, solo una acción de recuperación.")

    blocks.sort(key=lambda b: to_min(b["inicio"]))
    windows = {
        "ultimo_cafe": to_hhmm(bed - 9 * 60),
        "ultimo_preentreno_o_bebida_energetica": to_hhmm(bed - 13.5 * 60),
        "cafeina_max_dia_mg": 400,
        "luz_tenue_desde": to_hhmm(bed - 180),
        "cena_antes_de": to_hhmm(bed - 120),
        "dormir": to_hhmm(bed),
    }
    result = {
        "fecha": day.isoformat(),
        "sueno": st,
        "destacado": destacado,
        "pregunta_destacado": None if destacado else
            "Si hoy solo pudieras terminar una cosa, ¿cuál haría que el día valiera la pena?",
        "pregunta_obstaculo": "¿Qué es lo más probable que te saque de eso hoy? ¿Y qué harás si pasa?",
        "bloques": blocks,
        "ventanas": windows,
        "alertas": alerts,
        "nota": "Propuesta: no se ha tocado el calendario. Crea los bloques solo si el usuario dice que sí.",
    }
    if save:
        _save(db, day, parsed, blocks)
    return result


def _save(db, day: date, parsed: list[dict], blocks: list[dict]) -> None:
    import json
    iso = day.isoformat()
    db.conn.execute("DELETE FROM meetings WHERE date=?", (iso,))
    for m in parsed:
        db.conn.execute("INSERT OR REPLACE INTO meetings VALUES (?,?,?,?,?)",
                        (iso, to_hhmm(m["s"]), to_hhmm(m["e"]), int(m["clave"]), m["titulo"]))
    db.conn.execute("INSERT OR REPLACE INTO plans VALUES (?,?,?)",
                    (iso, json.dumps(blocks, ensure_ascii=False), datetime.now().isoformat(timespec="seconds")))
    db.conn.commit()


def summary_text(plan: dict) -> str:
    s = plan["sueno"]
    lines = [f"Plan del {plan['fecha']}"]
    if s["estado"]:
        lines.append(f"Sueño: {s['estado']}" + (" (deuda acumulada)" if s["deuda_acumulada"] else ""))
    for b in plan["bloques"]:
        lines.append(f"- {b['inicio']}-{b['fin']} {b['titulo']}")
    w = plan["ventanas"]
    lines.append(f"Último café: {w['ultimo_cafe']} · luz tenue desde {w['luz_tenue_desde']}")
    lines += [f"! {a}" for a in plan["alertas"]]
    return "\n".join(lines)
