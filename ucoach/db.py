"""Base de datos local de Ucoach (SQLite en ~/.ucoach, solo para el usuario)."""

from __future__ import annotations

import json
import os
import sqlite3
import stat
from datetime import datetime
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE IF NOT EXISTS profile (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS sleep (
    date TEXT PRIMARY KEY,              -- fecha del despertar (YYYY-MM-DD)
    hours REAL NOT NULL,
    quality INTEGER,                    -- 1-5, opcional
    bedtime TEXT, waketime TEXT,        -- HH:MM, opcionales
    source TEXT NOT NULL DEFAULT 'manual'
);
CREATE TABLE IF NOT EXISTS metrics (
    date TEXT NOT NULL, name TEXT NOT NULL, value REAL NOT NULL,
    source TEXT NOT NULL DEFAULT 'manual',
    PRIMARY KEY (date, name)
);
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    anchor TEXT, mini TEXT, hour TEXT,
    weekly_target INTEGER NOT NULL DEFAULT 5,
    focal INTEGER NOT NULL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'activo',   -- activo | automatico | archivado
    created TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS habit_log (
    habit_id INTEGER NOT NULL, date TEXT NOT NULL,
    PRIMARY KEY (habit_id, date)
);
CREATE TABLE IF NOT EXISTS srbai (
    habit_id INTEGER NOT NULL, date TEXT NOT NULL, score REAL NOT NULL,
    PRIMARY KEY (habit_id, date)
);
CREATE TABLE IF NOT EXISTS checkins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL, moment TEXT,
    energy INTEGER, mood INTEGER, focus INTEGER,
    highlight TEXT,                      -- si | parcial | no
    focus_minutes INTEGER, worked_after_end INTEGER
);
CREATE TABLE IF NOT EXISTS meetings (
    date TEXT NOT NULL, start TEXT NOT NULL, end TEXT NOT NULL,
    key INTEGER NOT NULL DEFAULT 0, title TEXT,
    PRIMARY KEY (date, start, end)
);
CREATE TABLE IF NOT EXISTS plans (date TEXT PRIMARY KEY, blocks TEXT NOT NULL, created TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS reading (book_id TEXT PRIMARY KEY, status TEXT NOT NULL, updated TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS ergonomics (ts TEXT PRIMARY KEY, answers TEXT NOT NULL, score INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS nudges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL, date TEXT NOT NULL, kind TEXT NOT NULL,
    sent INTEGER NOT NULL, channel TEXT
);
CREATE TABLE IF NOT EXISTS experiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    variable TEXT NOT NULL, option_a TEXT NOT NULL, option_b TEXT NOT NULL,
    start TEXT NOT NULL, days INTEGER NOT NULL, schedule TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'activo'
);
CREATE TABLE IF NOT EXISTS estimates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL, task TEXT NOT NULL, estimated INTEGER NOT NULL, actual INTEGER
);
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL, action TEXT NOT NULL, tbl TEXT NOT NULL,
    keyjson TEXT NOT NULL, before TEXT, after TEXT, undone INTEGER NOT NULL DEFAULT 0
);
"""

# Claves primarias por tabla, para el registro de auditoría y para deshacer.
PRIMARY_KEYS = {
    "profile": ["key"], "sleep": ["date"], "metrics": ["date", "name"],
    "habits": ["id"], "habit_log": ["habit_id", "date"], "srbai": ["habit_id", "date"],
    "checkins": ["id"], "meetings": ["date", "start", "end"], "plans": ["date"],
    "reading": ["book_id"], "ergonomics": ["ts"], "experiments": ["id"], "estimates": ["id"],
}


def home() -> Path:
    return Path(os.environ.get("UCOACH_HOME", Path.home() / ".ucoach")).expanduser()


def now() -> datetime:
    """Hora actual; UCOACH_NOW (ISO) la fija en pruebas."""
    fixed = os.environ.get("UCOACH_NOW")
    return datetime.fromisoformat(fixed) if fixed else datetime.now()


def _secure_permissions(directory: Path) -> None:
    os.chmod(directory, stat.S_IRWXU)  # 0700
    for name in ("ucoach.db", "ucoach.db-wal", "ucoach.db-shm"):
        p = directory / name
        if p.exists():
            os.chmod(p, stat.S_IRUSR | stat.S_IWUSR)  # 0600


class DB:
    def __init__(self, path: Path | None = None):
        directory = home() if path is None else path
        directory.mkdir(parents=True, exist_ok=True)
        old_umask = os.umask(0o077)
        try:
            self.conn = sqlite3.connect(directory / "ucoach.db")
        finally:
            os.umask(old_umask)
        self.dir = directory
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.executescript(SCHEMA)
        self.conn.execute("INSERT OR IGNORE INTO meta VALUES ('schema_version', ?)", (str(SCHEMA_VERSION),))
        self.conn.commit()
        _secure_permissions(directory)

    # --- utilidades -----------------------------------------------------
    def q(self, sql: str, args: tuple = ()) -> list[sqlite3.Row]:
        return self.conn.execute(sql, args).fetchall()

    def one(self, sql: str, args: tuple = ()) -> sqlite3.Row | None:
        return self.conn.execute(sql, args).fetchone()

    def _row(self, tbl: str, key: dict) -> dict | None:
        where = " AND ".join(f"{k}=?" for k in key)
        r = self.one(f"SELECT * FROM {tbl} WHERE {where}", tuple(key.values()))
        return dict(r) if r else None

    def upsert(self, tbl: str, row: dict, action: str) -> None:
        """Inserta o sustituye una fila y lo deja en audit_log para poder deshacerlo."""
        key = {k: row[k] for k in PRIMARY_KEYS[tbl] if k in row}
        before = self._row(tbl, key) if len(key) == len(PRIMARY_KEYS[tbl]) else None
        cols = ", ".join(row)
        marks = ", ".join("?" for _ in row)
        cur = self.conn.execute(f"INSERT OR REPLACE INTO {tbl} ({cols}) VALUES ({marks})", tuple(row.values()))
        if len(key) < len(PRIMARY_KEYS[tbl]):  # clave autoincremental
            key = {PRIMARY_KEYS[tbl][0]: cur.lastrowid}
        after = self._row(tbl, key)
        self.conn.execute(
            "INSERT INTO audit_log (ts, action, tbl, keyjson, before, after) VALUES (?,?,?,?,?,?)",
            (now().isoformat(timespec="seconds"), action, tbl, json.dumps(key),
             json.dumps(before) if before else None, json.dumps(after) if after else None),
        )
        self.conn.commit()

    def undo(self) -> dict | None:
        """Deshace la última escritura registrada que no se haya deshecho ya."""
        r = self.one("SELECT * FROM audit_log WHERE undone=0 ORDER BY id DESC LIMIT 1")
        if not r:
            return None
        key = json.loads(r["keyjson"])
        where = " AND ".join(f"{k}=?" for k in key)
        if r["before"]:
            before = json.loads(r["before"])
            cols = ", ".join(before)
            self.conn.execute(f"INSERT OR REPLACE INTO {r['tbl']} ({cols}) VALUES ({', '.join('?' for _ in before)})",
                              tuple(before.values()))
        else:
            self.conn.execute(f"DELETE FROM {r['tbl']} WHERE {where}", tuple(key.values()))
        self.conn.execute("UPDATE audit_log SET undone=1 WHERE id=?", (r["id"],))
        self.conn.commit()
        return {"accion": r["action"], "tabla": r["tbl"], "clave": key}

    # --- perfil -----------------------------------------------------------
    def profile(self) -> dict[str, Any]:
        data = dict(DEFAULT_PROFILE)
        for r in self.q("SELECT key, value FROM profile"):
            data[r["key"]] = json.loads(r["value"])
        return data

    def set_profile(self, values: dict[str, Any]) -> dict[str, Any]:
        for k, v in values.items():
            self.upsert("profile", {"key": k, "value": json.dumps(v)}, "perfil")
        return self.profile()

    def close(self) -> None:
        self.conn.close()


DEFAULT_PROFILE: dict[str, Any] = {
    "nombre": None,
    "hora_despertar": "07:00",
    "hora_dormir": "23:00",
    "cronotipo": "intermedio",          # alondra | intermedio | buho
    "hora_inicio_trabajo": "09:00",
    "hora_fin_trabajo": "19:00",
    "hora_entreno": None,               # HH:MM o None
    "dificultad_dormir": False,         # si es True, nunca se propone siesta
    "conduce_hoy": False,
    "objetivos": [],
    "palabras_clave_momento_clave": [],
    "metricas_activas": ["destacados", "foco", "energia"],
    "rutina_previa": [],
    "dias_libres": [5, 6],              # 0 = lunes
    "avisos_max_dia": 3,
    "avisos_canal": "sistema",          # sistema | ntfy | telegram | ninguno
    "ntfy_url": None,
    "telegram_chat_id": None,
    "avisos_probabilidad": 0.7,         # aleatorización simple de los avisos aleatorizables
    "modo_sin_numeros": False,
    "modo": "normal",                   # normal | sostener
    "snooze_hasta": None,
    "hoy_no": None,                     # fecha YYYY-MM-DD en la que el usuario dijo «hoy no»
}
