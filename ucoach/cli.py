"""Línea de comandos de Ucoach."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ucoach import __version__

PKG_ROOT = Path(__file__).resolve().parent.parent


def _db():
    from ucoach.db import DB
    return DB()


def cmd_config(_args) -> int:
    snippet = {"mcpServers": {"ucoach": {"command": sys.executable, "args": ["-m", "ucoach", "serve"],
                                         "env": {"PYTHONPATH": str(PKG_ROOT)}}}}
    print("Claude Code:\n  claude mcp add ucoach -e PYTHONPATH=%s -- %s -m ucoach serve\n" % (PKG_ROOT, sys.executable))
    print("Claude Desktop u otro cliente MCP (añade al fichero de configuración):")
    print(json.dumps(snippet, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="ucoach", description="Coach de excelencia profesional dentro de tu IA.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("serve", help="Servidor MCP por stdio")
    sub.add_parser("config", help="Muestra cómo conectarlo a tu IA")
    n = sub.add_parser("nudge", help="Revisa si toca un aviso (lo lanza el planificador cada 30 min)")
    n.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("schedule", help="Instala o quita el planificador de avisos")
    s.add_argument("accion", choices=["install", "uninstall", "show"])
    s.add_argument("--load", action="store_true", help="Además de escribirlo, actívalo")
    z = sub.add_parser("snooze", help="Silencia los avisos unas horas")
    z.add_argument("horas", type=int, choices=[1, 2, 4, 8])
    sub.add_parser("hoy-no", help="Hoy sin avisos (no cuenta como fallo)")
    ia = sub.add_parser("import-apple", help="Importa export.xml de Apple Health")
    ia.add_argument("fichero")
    ia.add_argument("--allow-dtd", action="store_true")
    ic = sub.add_parser("import-csv", help="Importa un CSV de sueño y métricas")
    ic.add_argument("fichero")
    st = sub.add_parser("stats", help="Resumen anónimo para la validación")
    st.add_argument("--semanas", type=int, default=1)
    sub.add_parser("undo", help="Deshace la última escritura")
    lt = sub.add_parser("lint-textos", help="Busca frases que hay que evitar (research/05)")
    lt.add_argument("rutas", nargs="*")
    sub.add_parser("version")
    args = ap.parse_args(argv)

    if args.cmd == "serve":
        from ucoach.mcp.server import serve
        serve()
        return 0
    if args.cmd == "config":
        return cmd_config(args)
    if args.cmd == "version":
        print(__version__)
        return 0
    if args.cmd == "lint-textos":
        from ucoach.lint import lint_builtin, lint_paths
        found = lint_paths(args.rutas) if args.rutas else lint_builtin() + lint_paths([str(PKG_ROOT / "ucoach/content")])
        for f in found:
            print(f"{f['donde']}: «{f['texto']}» → evita «{f['evitar']}»; mejor: {f['alternativa']}")
        print(f"{len(found)} hallazgo(s)")
        return 1 if found else 0
    if args.cmd == "schedule":
        from ucoach import schedule
        if args.accion == "install":
            print(schedule.install(args.load))
        elif args.accion == "uninstall":
            print(schedule.uninstall())
        else:
            print(schedule.launchd_plist())
        return 0

    from ucoach.db import now
    db = _db()
    try:
        if args.cmd == "nudge":
            from ucoach import nudge
            print(json.dumps(nudge.run(db, now(), dry_run=args.dry_run), ensure_ascii=False))
        elif args.cmd == "snooze":
            from ucoach import nudge
            print("Avisos silenciados hasta", nudge.snooze(db, args.horas, now()))
        elif args.cmd == "hoy-no":
            from ucoach import nudge
            nudge.today_no(db, now().date())
            print("Hoy sin avisos. Mañana seguimos.")
        elif args.cmd == "import-apple":
            from ucoach.importers import apple_health
            print(json.dumps(apple_health.import_file(db, args.fichero, args.allow_dtd), ensure_ascii=False))
        elif args.cmd == "import-csv":
            from ucoach.importers import csv_import
            print(json.dumps(csv_import.import_file(db, args.fichero), ensure_ascii=False))
        elif args.cmd == "stats":
            from ucoach import stats
            print(stats.report(db, now().date(), args.semanas))
        elif args.cmd == "undo":
            r = db.undo()
            print("Nada que deshacer." if r is None else f"Deshecho: {r['accion']} ({r['tabla']})")
    finally:
        db.close()
    return 0
