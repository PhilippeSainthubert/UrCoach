"""ucoach lint-textos: busca frases que hay que evitar (research/05, apartado 4) en textos de producto.

Una coincidencia precedida de una negación cercana («no», «ni», «sin») no cuenta, para no marcar
la declaración de finalidad («no está destinada a diagnosticar…»). Las secciones de markdown cuyo
título habla de lo que no se dice, del lenguaje o de lo que se evita se saltan. Una línea con
«lint:ignore» también se salta.
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from ucoach.core.util import load_json

SKIP_HEADINGS = ("no se dice", "lenguaje", "evitar", "palabras")
NEGATION = re.compile(r"\b(no|ni|sin|nunca|nada de)\b[^.;:]{0,60}$")
# Campos de los JSON en los que habla Ucoach con su propia voz. El resto (títulos e ideas de libros,
# evidencia, riesgos, fuentes) describe hechos o la tesis de un autor y no se revisa (research/05).
VOICE_FIELDS = ("pauta", "texto", "accion")
# La declaración oficial de finalidad prevista (research/05) se permite tal cual.
ALLOWED_LINES = ("no es un producto sanitario",)


def _norm(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()


def patterns() -> list[tuple[re.Pattern, dict]]:
    out = []
    for item in load_json("palabras_evitar.json"):
        try:
            out.append((re.compile(_norm(item["patron"])), item))
        except re.error:
            continue
    return out


def lint_text(text: str, where: str = "") -> list[dict]:
    findings, skip = [], False
    pats = patterns()
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("#"):
            skip = any(h in _norm(line) for h in SKIP_HEADINGS)
            continue
        if skip or "lint:ignore" in line:
            continue
        low = _norm(line)
        if any(a in low for a in ALLOWED_LINES):
            continue
        for rx, item in pats:
            for m in rx.finditer(low):
                if NEGATION.search(low[:m.start()]):
                    continue
                findings.append({"donde": f"{where}:{n}", "texto": line.strip()[:160], "evitar": item.get("ejemplo"),
                                 "alternativa": item.get("alternativa")})
                break
    return findings


def lint_paths(paths: list[str]) -> list[dict]:
    out = []
    for p in paths:
        path = Path(p)
        files = [f for f in path.rglob("*") if f.suffix in (".md", ".json", ".txt")] if path.is_dir() else [path]
        for f in files:
            if f.name == "palabras_evitar.json":
                continue
            if f.suffix == ".json":
                out += lint_json(f)
            else:
                out += lint_text(f.read_text(encoding="utf-8"), str(f))
    return out


def lint_json(path: Path) -> list[dict]:
    import json
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for item in data if isinstance(data, list) else []:
        for field in VOICE_FIELDS:
            if isinstance(item, dict) and isinstance(item.get(field), str):
                out += lint_text(item[field], f"{path}:{item.get('id') or item.get('tipo')}.{field}")
    return out


def lint_builtin() -> list[dict]:
    """Textos que el servidor manda a la IA o al usuario: herramientas, prompts, privacidad y avisos."""
    from ucoach.mcp import prompts
    from ucoach.mcp.tools import TOOLS
    from ucoach.nudge import TEMPLATES
    out = []
    for t in TOOLS:
        out += lint_text(t.description, f"herramienta:{t.name}")
    for name, p in prompts.PROMPTS.items():
        out += lint_text(p["text"], f"prompt:{name}")
    out += lint_text(prompts.PRIVACIDAD, "recurso:privacidad")
    for k, v in TEMPLATES.items():
        out += lint_text(v, f"aviso:{k}")
    return out
