"""Canales de aviso: notificación del sistema (por defecto), ntfy o Telegram.

Los secretos (token de Telegram o de ntfy) se leen del llavero del sistema, nunca de la base:
- macOS: security add-generic-password -a "$USER" -s ucoach-telegram -w
- Linux: secret-tool store --label=ucoach service ucoach-telegram
o, como alternativa, de las variables UCOACH_TELEGRAM_TOKEN / UCOACH_NTFY_TOKEN.
"""

from __future__ import annotations

import json
import os
import platform
import shutil
import ssl
import subprocess
import sys
import urllib.request


def secret(service: str) -> str | None:
    env = os.environ.get(service.upper().replace("-", "_"))
    if env:
        return env
    try:
        if platform.system() == "Darwin":
            out = subprocess.run(["security", "find-generic-password", "-s", service, "-w"],
                                 capture_output=True, text=True, timeout=10)
        elif shutil.which("secret-tool"):
            out = subprocess.run(["secret-tool", "lookup", "service", service], capture_output=True, text=True, timeout=10)
        else:
            return None
        return out.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def _ssl_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    if not ctx.get_ca_certs() and os.path.exists("/etc/ssl/cert.pem"):
        ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    return ctx


def _post(url: str, data: bytes, headers: dict) -> None:
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=15, context=_ssl_context()) as r:
        r.read()


def system_notification(text: str) -> bool:
    system = platform.system()
    try:
        if system == "Darwin":
            script = 'display notification %s with title "Ucoach"' % json.dumps(text)
            subprocess.run(["osascript", "-e", script], check=True, timeout=10, capture_output=True)
            return True
        if system == "Linux" and shutil.which("notify-send"):
            subprocess.run(["notify-send", "Ucoach", text], check=True, timeout=10)
            return True
    except (OSError, subprocess.SubprocessError):
        return False
    return False


def send(text: str, profile: dict) -> str:
    channel = profile.get("avisos_canal", "sistema")
    try:
        if channel == "telegram":
            token, chat = secret("ucoach-telegram"), profile.get("telegram_chat_id")
            if token and chat:
                body = json.dumps({"chat_id": chat, "text": text, "disable_notification": False}).encode()
                _post(f"https://api.telegram.org/bot{token}/sendMessage", body, {"Content-Type": "application/json"})
                return "telegram"
        elif channel == "ntfy" and profile.get("ntfy_url"):
            headers = {"Title": "Ucoach"}
            token = secret("ucoach-ntfy")
            if token:
                headers["Authorization"] = f"Bearer {token}"
            _post(profile["ntfy_url"], text.encode("utf-8"), headers)
            return "ntfy"
    except OSError as e:
        print(f"ucoach: no se pudo enviar por {channel}: {e.__class__.__name__}", file=sys.stderr)
    if system_notification(text):
        return "sistema"
    print(f"[Ucoach] {text}")
    return "consola"
