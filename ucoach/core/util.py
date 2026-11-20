"""Utilidades de tiempo y de contenido."""

from __future__ import annotations

import json
import re
from datetime import date, datetime, timedelta
from functools import lru_cache
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"
HHMM = re.compile(r"^([01]\d|2[0-3]):([0-5]\d)$")


def to_min(hhmm: str) -> int:
    m = HHMM.match(hhmm or "")
    if not m:
        raise ValueError(f"hora no válida (usa HH:MM): {hhmm!r}")
    return int(m.group(1)) * 60 + int(m.group(2))


def to_hhmm(minutes: int | float) -> str:
    minutes = int(round(minutes)) % (24 * 60)
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def parse_date(value: str | None, default: date) -> date:
    return date.fromisoformat(value) if value else default


def days_back(d: date, n: int) -> list[str]:
    """Las n fechas que terminan en d (incluida), de la más antigua a la más reciente."""
    return [(d - timedelta(days=i)).isoformat() for i in range(n - 1, -1, -1)]


def bed_minutes(bed: str, wake: str) -> int:
    """Minutos de hora de dormir; si es después de medianoche, se suma un día para ordenar."""
    b, w = to_min(bed), to_min(wake)
    return b + 24 * 60 if b < w else b


@lru_cache(maxsize=None)
def load_json(name: str):
    path = CONTENT / name
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=None)
def load_text(rel: str) -> str:
    path = CONTENT / rel
    return path.read_text(encoding="utf-8") if path.exists() else ""


def protocol_names() -> list[str]:
    folder = CONTENT / "protocolos"
    return sorted(p.stem for p in folder.glob("*.md")) if folder.exists() else []


def iso_now(dt: datetime) -> str:
    return dt.isoformat(timespec="minutes")
