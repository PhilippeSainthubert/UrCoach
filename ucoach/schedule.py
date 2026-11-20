"""ucoach schedule install: lanza `ucoach nudge` cada 30 min sin perder avisos con el equipo dormido.

- macOS: launchd con StartCalendarInterval (a diferencia de cron, ejecuta al despertar lo que se perdió).
- Linux: systemd --user timer con Persistent=true.
- Windows: orden de schtasks (con «ejecutar lo antes posible si se perdió»).
"""

from __future__ import annotations

import os
import platform
import subprocess
import sys
from pathlib import Path

from ucoach.db import home

LABEL = "com.ucoach.nudge"
PKG_ROOT = Path(__file__).resolve().parent.parent


def _env() -> dict:
    env = {"PYTHONPATH": str(PKG_ROOT)}
    if os.environ.get("UCOACH_HOME"):
        env["UCOACH_HOME"] = os.environ["UCOACH_HOME"]
    return env


def launchd_plist() -> str:
    env = "".join(f"<key>{k}</key><string>{v}</string>" for k, v in _env().items())
    log = home() / "nudge.log"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>{LABEL}</string>
  <key>ProgramArguments</key><array><string>{sys.executable}</string><string>-m</string><string>ucoach</string><string>nudge</string></array>
  <key>EnvironmentVariables</key><dict>{env}</dict>
  <key>StartCalendarInterval</key><array><dict><key>Minute</key><integer>0</integer></dict><dict><key>Minute</key><integer>30</integer></dict></array>
  <key>StandardErrorPath</key><string>{log}</string>
  <key>StandardOutPath</key><string>{log}</string>
</dict></plist>
"""


def systemd_units() -> tuple[str, str]:
    env = " ".join(f'"{k}={v}"' for k, v in _env().items())
    service = f"""[Unit]
Description=Ucoach nudge

[Service]
Type=oneshot
Environment={env}
ExecStart={sys.executable} -m ucoach nudge
"""
    timer = """[Unit]
Description=Ucoach nudge cada 30 min

[Timer]
OnCalendar=*:00/30
Persistent=true

[Install]
WantedBy=timers.target
"""
    return service, timer


def install(load: bool = False) -> str:
    system = platform.system()
    if system == "Darwin":
        path = Path.home() / "Library/LaunchAgents" / f"{LABEL}.plist"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(launchd_plist(), encoding="utf-8")
        cmd = ["launchctl", "bootstrap", f"gui/{os.getuid()}", str(path)]
        if load:
            subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}", str(path)], capture_output=True)
            subprocess.run(cmd, check=True)
            return f"Instalado y activado: {path}"
        return f"Escrito {path}\nPara activarlo: {' '.join(cmd)}"
    if system == "Linux":
        folder = Path.home() / ".config/systemd/user"
        folder.mkdir(parents=True, exist_ok=True)
        service, timer = systemd_units()
        (folder / "ucoach-nudge.service").write_text(service, encoding="utf-8")
        (folder / "ucoach-nudge.timer").write_text(timer, encoding="utf-8")
        cmd = "systemctl --user daemon-reload && systemctl --user enable --now ucoach-nudge.timer"
        if load:
            subprocess.run(cmd, shell=True, check=True)
            return "Instalado y activado: ucoach-nudge.timer"
        return f"Escritas las unidades en {folder}\nPara activarlo: {cmd}"
    if system == "Windows":
        return (f'schtasks /Create /SC MINUTE /MO 30 /TN Ucoach-nudge /TR "\\"{sys.executable}\\" -m ucoach nudge" /F\n'
                "Después, en el Programador de tareas, activa «Ejecutar la tarea lo antes posible si se omitió un inicio programado».")
    return "Sistema no reconocido: ejecuta `python3 -m ucoach nudge` cada 30 minutos con tu planificador."


def uninstall() -> str:
    if platform.system() == "Darwin":
        path = Path.home() / "Library/LaunchAgents" / f"{LABEL}.plist"
        subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}", str(path)], capture_output=True)
        if path.exists():
            path.unlink()
        return "Desinstalado."
    if platform.system() == "Linux":
        subprocess.run("systemctl --user disable --now ucoach-nudge.timer", shell=True, capture_output=True)
        return "Desactivado ucoach-nudge.timer."
    return "En Windows: schtasks /Delete /TN Ucoach-nudge /F"
