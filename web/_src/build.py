#!/usr/bin/env python3
"""Monta web/index.html a partir de web/_src/template.html y las piezas de marca.

Marcadores en la plantilla:
  {{LOGO}}        isologotipo en línea (color, nombre en currentColor)
  {{ENSO_HERO}}   ensō grande con degradado y máscara para pintarse al cargar
  {{ENSO_SMALL}}  ensō pequeño (para iconos dentro de la página)
  {{ENSO_DARK}}   ensō con el degradado para fondo oscuro, con máscara de trazo
  {{FAVICON}}     data URI del favicon SVG
Uso: python build.py  (con el venv que tiene fonttools y uharfbuzz)
"""
import math
import re
import sys
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
WEB = HERE.parent
sys.path.insert(0, str(WEB.parent / "marca" / "brand-kit" / "_generador"))
import build_kit as K  # noqa: E402


def centerline(spec):
    pts = []
    n = 120
    for i in range(n + 1):
        t = i / n
        a = math.radians(spec["a0"] + spec["sweep"] * t)
        rr = spec["r"] + 2.2 * math.sin(math.pi * t) - 3.2 * t ** 3
        pts.append((60 + rr * math.cos(a), 60 + rr * math.sin(a)))
    return "M" + "L".join(f"{K.f(x)} {K.f(y)}" for x, y in pts)


def enso_drawn(dark=False, cls="enso-hero", spec=K.ENSO):
    """Ensō con máscara de trazo: la clase .draw anima --p de 0 a 1."""
    mid = K.uid("em")
    x0, y0, x1, y1 = K.enso_bbox(spec)
    s = max(x1 - x0, y1 - y0) + 6
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = f"{K.f(cx - s / 2)} {K.f(cy - s / 2)} {K.f(s)} {K.f(s)}"
    mask = (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="140" height="140">'
            f'<path class="enso-line" d="{centerline(spec)}" pathLength="1" fill="none" stroke="#fff" '
            f'stroke-width="{spec["wh"] + 6}" stroke-linecap="round"/></mask>')
    return (f'<svg class="{cls}" viewBox="{vb}" aria-hidden="true" focusable="false"><defs>{mask}</defs>'
            f'<g mask="url(#{mid})">{K.enso_group(spec, "day", dark)}</g></svg>')


def logo_inline():
    inner, vb = K.lockup("h", "currentColor", "day", False)
    return (f'<svg class="logo-svg" viewBox="{" ".join(K.f(v) for v in vb)}" role="img" aria-label="UrCoach">'
            f'{inner}</svg>')


def logo_inline_dark():
    inner, vb = K.lockup("h", "currentColor", "day", True)
    return (f'<svg class="logo-svg" viewBox="{" ".join(K.f(v) for v in vb)}" role="img" aria-label="UrCoach">'
            f'{inner}</svg>')


def small(dark=False, cls="enso-sm"):
    x0, y0, x1, y1 = K.enso_bbox(K.ENSO)
    s = max(x1 - x0, y1 - y0) + 4
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return (f'<svg class="{cls}" viewBox="{K.f(cx - s / 2)} {K.f(cy - s / 2)} {K.f(s)} {K.f(s)}" aria-hidden="true" focusable="false">'
            f'{K.enso_group(K.ENSO, "day", dark)}</svg>')


def dedupe_enso(html):
    """Cada ensō de color se define una vez en un <svg> oculto y se reutiliza con <use>."""
    pat = re.compile(r'<clipPath id="(ec\d+)"><path d="([^"]+)"/></clipPath><g clip-path="url\(#\1\)">(.*?)</g>', re.S)
    defs, seen = [], {}

    def sub(m):
        key = (m.group(2), m.group(3))
        if key not in seen:
            gid = f"ed{len(seen) + 1}"
            seen[key] = gid
            defs.append(f'<g id="{gid}"><clipPath id="{gid}c"><path d="{m.group(2)}"/></clipPath>'
                        f'<g clip-path="url(#{gid}c)">{m.group(3)}</g></g>')
        return f'<use href="#{seen[key]}"/>'

    html = pat.sub(sub, html)
    hidden = ('<svg width="0" height="0" style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true" focusable="false">'
              f'<defs>{"".join(defs)}</defs></svg>')
    return html.replace('<a class="skip"', hidden + '\n<a class="skip"', 1)


def main():
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    fav = K.favicon_doc()
    rep = {
        "{{LOGO}}": logo_inline(),
        "{{LOGO_DARK}}": logo_inline_dark(),
        "{{ENSO_HERO}}": enso_drawn(False),
        "{{ENSO_DARK}}": enso_drawn(True, "enso-final"),
        "{{ENSO_SMALL}}": small(),
        "{{ENSO_SMALL_DARK}}": small(True),
        "{{FAVICON}}": "data:image/svg+xml," + urllib.parse.quote(fav),
    }
    out = tpl
    for k, v in rep.items():
        while k in out:
            # cada aparición con ids propios
            if k in ("{{ENSO_SMALL}}", "{{ENSO_SMALL_DARK}}", "{{LOGO}}", "{{LOGO_DARK}}"):
                v = {"{{ENSO_SMALL}}": small, "{{ENSO_SMALL_DARK}}": lambda: small(True),
                     "{{LOGO}}": logo_inline, "{{LOGO_DARK}}": logo_inline_dark}[k]()
            out = out.replace(k, v, 1)
    out = dedupe_enso(out)
    left = re.findall(r"\{\{[A-Z_]+\}\}", out)
    assert not left, left
    assert "—" not in out, "guion largo"
    ids = re.findall(r'\sid="([^"]+)"', out)
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, dup
    (WEB / "index.html").write_text(out, encoding="utf-8")
    print("index.html", len(out) // 1024, "KB")


if __name__ == "__main__":
    main()
