#!/usr/bin/env python3
"""Brand kit de UrCoach (v1, 2026-11-20).

Isologotipo: ensō (Trazo, ronda 10) + UrCoach en Inter Tight 600 (ronda 11, opción 01).
Color del ensō: el trazo es el día. Cielo (mañana) -> índigo (foco) -> violeta (noche), interpolado en OKLab.

Genera en ../ (marca/brand-kit/):
  logo/*.svg, app/*.svg|png, social/*.svg|png, tokens/tokens.css|json
y la guía: /Users/philippesaint-hubert/Ucoach/marca/urcoach-brand-kit.html

Requiere: fonttools, uharfbuzz; resvg_py opcional para los PNG.
"""
import io
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = Path(__file__).resolve().parent
KIT = HERE.parent
FONTS = HERE / "fonts"
GUIDE = KIT.parent / "urcoach-brand-kit.html"

# --------------------------------------------------------------------------- color
INK = "#121018"
PAPER = "#FAF9FC"
INDIGO = "#4F46E5"
NIGHT = "#0B0A12"

# El día en el trazo. t = 0 cabeza (mañana), t = 1 cola (noche).
DAY_LIGHT = [(0.00, "#1FB6F2"), (0.30, "#4C7CF6"), (0.58, "#4F46E5"), (0.86, "#7C3AED"), (1.00, "#9061F9")]
DAY_DARK = [(0.00, "#5ED3FF"), (0.30, "#7C9DFF"), (0.58, "#8B8CFB"), (0.86, "#A684FA"), (1.00, "#C4B5FD")]


def _hex(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def _lin(c):
    return c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4


def _gam(c):
    c = max(0, min(1, c))
    return 12.92 * c if c <= .0031308 else 1.055 * c ** (1 / 2.4) - .055


def to_oklab(h):
    r, g, b = (_lin(c) for c in _hex(h))
    l = (.4122214708 * r + .5363325363 * g + .0514459929 * b) ** (1 / 3)
    m = (.2119034982 * r + .6806995451 * g + .1073969566 * b) ** (1 / 3)
    s = (.0883024619 * r + .2817188376 * g + .6299787005 * b) ** (1 / 3)
    return (.2104542553 * l + .7936177850 * m - .0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + .4505937099 * s,
            .0259040371 * l + .7827717662 * m - .8086757660 * s)


def from_oklab(L, a, b):
    l = (L + .3963377774 * a + .2158037573 * b) ** 3
    m = (L - .1055613458 * a - .0638541728 * b) ** 3
    s = (L - .0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + .2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - .3413193965 * s
    bb = -.0041960863 * l - .7034186147 * m + 1.7076147010 * s
    return "#" + "".join(f"{round(_gam(c) * 255):02X}" for c in (r, g, bb))


def color_at(t, stops):
    t = max(0, min(1, t))
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t <= t1:
            k = (t - t0) / (t1 - t0) if t1 > t0 else 0
            A, B = to_oklab(c0), to_oklab(c1)
            return from_oklab(*(A[i] + (B[i] - A[i]) * k for i in range(3)))
    return stops[-1][1]


def rel_lum(h):
    r, g, b = (_lin(c) for c in _hex(h))
    return .2126 * r + .7152 * g + .0722 * b


def contrast(a, b):
    la, lb = sorted((rel_lum(a), rel_lum(b)), reverse=True)
    return (la + .05) / (lb + .05)


# --------------------------------------------------------------------------- ensō
def f(x):
    s = f"{x:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _unit(dx, dy):
    d = math.hypot(dx, dy) or 1
    return dx / d, dy / d


def _cap(p, q, w):
    ang = math.atan2(p[1] - q[1], p[0] - q[0])
    return [(p[0] + w / 2 * math.cos(ang + math.pi / 2 - math.pi * k / 36),
             p[1] + w / 2 * math.sin(ang + math.pi / 2 - math.pi * k / 36)) for k in range(1, 36)]


def stroke_outline(C, W, cap0=True, cap1=True):
    c2, w2 = [C[0]], [W[0]]
    for p, w in zip(C[1:], W[1:]):
        if math.dist(p, c2[-1]) > 1e-3:
            c2.append(p)
            w2.append(w)
    C, W = c2, w2
    n = len(C)
    L, R = [], []
    for i in range(n):
        if i in (0, n - 1):
            a, b = (C[0], C[1]) if i == 0 else (C[-2], C[-1])
            t = _unit(b[0] - a[0], b[1] - a[1])
            m, k = (-t[1], t[0]), 1
        else:
            t1 = _unit(C[i][0] - C[i - 1][0], C[i][1] - C[i - 1][1])
            t2 = _unit(C[i + 1][0] - C[i][0], C[i + 1][1] - C[i][1])
            n1, n2 = (-t1[1], t1[0]), (-t2[1], t2[0])
            m = _unit(n1[0] + n2[0], n1[1] + n2[1])
            k = 1 / max(.35, m[0] * n1[0] + m[1] * n1[1])
        h = W[i] / 2 * k
        L.append((C[i][0] + m[0] * h, C[i][1] + m[1] * h))
        R.append((C[i][0] - m[0] * h, C[i][1] - m[1] * h))
    pts = L[:]
    if cap1:
        pts += _cap(C[-1], C[-2], W[-1])
    pts += R[::-1]
    if cap0:
        pts += _cap(C[0], C[1], W[0])
    return pts


ENSO = dict(r=40, a0=-56, sweep=318, wh=16.5, wb=8.5, wt=1.2)          # ronda 10, tal cual se eligió
ENSO_FAV = dict(r=39, a0=-54, sweep=304, wh=22, wb=15, wt=6)           # versión óptica para 16-48 px
ENSO_LOCK = dict(r=40, a0=-56, sweep=318, wh=19.6, wb=10.6, wt=1.5)    # dentro del isologotipo (ronda 11)


def _ss(a, b, x):
    x = max(0.0, min(1.0, (x - a) / (b - a)))
    return x * x * (3 - 2 * x)


def enso_pts(r, a0, sweep, wh, wb, wt, n=420):
    C, W = [], []
    for i in range(n + 1):
        t = i / n
        a = math.radians(a0 + sweep * t)
        rr = r + 2.2 * math.sin(math.pi * t) - 3.2 * t ** 3
        C.append((60 + rr * math.cos(a), 60 + rr * math.sin(a)))
        # grosor sin quiebros: cada tramo entra y sale con pendiente cero (smoothstep)
        w = wb + (wh - wb) * (1 - _ss(.03, .8, t)) ** 1.1
        w = w + (wt - w) * _ss(.74, 1, t) ** 1.2
        w *= .86 + .14 * _ss(0, .07, t)
        W.append(w)
    return stroke_outline(C, W, cap1=False)


def poly(P):
    return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in P) + "Z"


UID = [0]


def uid(p):
    UID[0] += 1
    return f"{p}{UID[0]}"


def enso_group(spec=ENSO, paint="day", dark=False):
    """<g> del ensō en su caja de 120. paint: 'day' (degradado), o un color sólido."""
    P = enso_pts(**spec)
    d = poly(P)
    if paint != "day":
        return f'<path fill="{paint}" d="{d}"/>'
    stops = DAY_DARK if dark else DAY_LIGHT
    cid = uid("ec")
    a0, sw = spec["a0"], spec["sweep"]
    step, ov = 2.0, .9
    wedges = []
    ang = a0 - 24
    while ang < a0 + sw + 24:
        t = (ang + step / 2 - a0) / sw
        c = color_at(t, stops)
        A, B = math.radians(ang - ov / 2), math.radians(ang + step + ov / 2)
        R = 75
        wedges.append(f'<path fill="{c}" d="M60 60L{f(60 + R * math.cos(A))} {f(60 + R * math.sin(A))}'
                      f'L{f(60 + R * math.cos(B))} {f(60 + R * math.sin(B))}Z"/>')
        ang += step
    return (f'<clipPath id="{cid}"><path d="{d}"/></clipPath>'
            f'<g clip-path="url(#{cid})">{"".join(wedges)}</g>')


def enso_bbox(spec=ENSO):
    P = enso_pts(**spec)
    xs, ys = [p[0] for p in P], [p[1] for p in P]
    return min(xs), min(ys), max(xs), max(ys)


# --------------------------------------------------------------------------- texto en contornos
class Face:
    _c = {}

    def __init__(self, file, axes):
        tt = TTFont(FONTS / file)
        if "fvar" in tt:
            tt = instancer.instantiateVariableFont(tt, axes)
        buf = io.BytesIO()
        tt.save(buf)
        data = buf.getvalue()
        self.tt = TTFont(io.BytesIO(data))
        self.gs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.upem = self.tt["head"].unitsPerEm
        self.hb = hb.Font(hb.Face(data))
        cm = self.tt.getBestCmap()
        bp = BoundsPen(self.gs)
        self.gs[cm[ord("H")]].draw(bp)
        self.cap = bp.bounds[3]

    @classmethod
    def get(cls, file, **axes):
        k = (file, tuple(sorted(axes.items())))
        if k not in cls._c:
            cls._c[k] = Face(file, axes)
        return cls._c[k]


def text_path(face, text, size, track=0.0, kern=None, features=None):
    """Contornos de `text` a `size` px de cuerpo, línea base en y=0. Devuelve (d, x0, x1, top, bottom, avance)."""
    kern = kern or {}
    sc = size / face.upem
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(face.hb, buf, features or {"kern": True})
    x, ds = 0.0, []
    b0 = [1e9, 1e9, -1e9, -1e9]
    infos = buf.glyph_infos
    for i, (info, pos) in enumerate(zip(infos, buf.glyph_positions)):
        name = face.order[info.codepoint]
        tr = (sc, 0, 0, -sc, x + pos.x_offset * sc, -pos.y_offset * sc)
        pen = SVGPathPen(face.gs)
        face.gs[name].draw(TransformPen(pen, tr))
        bp = BoundsPen(face.gs)
        face.gs[name].draw(TransformPen(bp, tr))
        if bp.bounds:
            b = bp.bounds
            b0 = [min(b0[0], b[0]), min(b0[1], b[1]), max(b0[2], b[2]), max(b0[3], b[3])]
        ds.append(pen.getCommands())
        x += pos.x_advance * sc
        if i < len(infos) - 1:
            x += track * size
            pair = text[info.cluster] + text[infos[i + 1].cluster]
            x += kern.get(pair, 0) * size
    return "".join(ds), b0[0], b0[2], b0[1], b0[3], x


WM_FONT = ("InterTight[wght].ttf", dict(wght=600))
WM_TRACK = -.022
WM_KERN = {"rC": -.01}


def wordmark(cap=100):
    face = Face.get(WM_FONT[0], **WM_FONT[1])
    size = cap * face.upem / face.cap
    d, x0, x1, top, bot, _ = text_path(face, "UrCoach", size, WM_TRACK, WM_KERN)
    return d, x0, x1, top, bot


# --------------------------------------------------------------------------- isologotipo
def lockup(kind="h", word=INK, paint="day", dark=False, pad=0.0):
    """Devuelve (svg_inner, (x, y, w, h)). Altura de mayúsculas = 100."""
    d, x0, x1, top, bot = wordmark()
    ex0, ey0, ex1, ey1 = enso_bbox(ENSO_LOCK)
    esz = max(ex1 - ex0, ey1 - ey0)
    if kind == "h":
        D = 150
        s = D / esz
        gap = .36 * D
        ox = x0 - gap - (ex1 - ex0) * s - ex0 * s
        oy = -50 - (ey0 + ey1) / 2 * s
    else:
        D = 270
        s = D / esz
        ox = (x0 + x1) / 2 - (ex0 + ex1) / 2 * s
        oy = top - 72 - ey1 * s
    g = f'<g transform="translate({f(ox)} {f(oy)}) scale({f(s)})">{enso_group(ENSO_LOCK, paint, dark)}</g>'
    inner = g + f'<path fill="{word}" d="{d}"/>'
    bx0 = min(ox + ex0 * s, x0)
    by0 = min(oy + ey0 * s, top)
    bx1 = max(ox + ex1 * s, x1)
    by1 = max(oy + ey1 * s, bot)
    w, h = bx1 - bx0, by1 - by0
    p = pad * h
    return inner, (bx0 - p, by0 - p, w + 2 * p, h + 2 * p)


def svg_doc(inner, vb, w=None, h=None, title="UrCoach", extra=""):
    x, y, ww, hh = vb
    if not w:
        w, h = ww, hh
    size = f' width="{f(w)}" height="{f(h)}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{f(x)} {f(y)} {f(ww)} {f(hh)}"{size} role="img"{extra}>'
            f'<title>{title}</title>{inner}</svg>')


def symbol_doc(paint="day", dark=False, spec=ENSO, pad=6):
    x0, y0, x1, y1 = enso_bbox(spec)
    s = max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = (cx - s / 2 - pad, cy - s / 2 - pad, s + 2 * pad, s + 2 * pad)
    return svg_doc(enso_group(spec, paint, dark), vb, title="UrCoach")


SQ = "M27 0H93C108 0 120 12 120 27V93C120 108 108 120 93 120H27C12 120 0 108 0 93V27C0 12 12 0 27 0Z"


def app_icon(dark=False, size=None, fav=False):
    spec = ENSO_FAV if fav else ENSO
    gid, bid, glo = uid("bg"), uid("blur"), uid("glow")
    if dark:
        bg = (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1B1730"/>'
              f'<stop offset="1" stop-color="{NIGHT}"/></linearGradient>')
    else:
        bg = (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/>'
              f'<stop offset="1" stop-color="#EEEDF6"/></linearGradient>')
    x0, y0, x1, y1 = enso_bbox(spec)
    s = 70 / max(x1 - x0, y1 - y0)
    ox, oy = 60 - (x0 + x1) / 2 * s, 60 - (y0 + y1) / 2 * s
    glow = ""
    if dark:
        glow = (f'<filter id="{bid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9"/></filter>'
                f'<g filter="url(#{bid})" opacity=".55" transform="translate({f(ox)} {f(oy)}) scale({f(s)})">{enso_group(spec, "day", True)}</g>')
    inner = (f'<defs>{bg}</defs><path d="{SQ}" fill="url(#{gid})"/>{glow}'
             f'<g transform="translate({f(ox)} {f(oy)}) scale({f(s)})">{enso_group(spec, "day", dark)}</g>')
    if not dark:
        inner += f'<path d="{SQ}" fill="none" stroke="#121018" stroke-opacity=".06"/>'
    return svg_doc(inner, (0, 0, 120, 120), size, size, "UrCoach")


def favicon_doc():
    return symbol_doc("day", False, ENSO_FAV, pad=3)


# --------------------------------------------------------------------------- piezas sociales
def headline(lines, x, y, size, lead, fill=INK, serif_fill=INDIGO):
    """lines: [(texto, 'sans'|'serif'), ...]. Devuelve paths."""
    out = []
    for i, (t, kind) in enumerate(lines):
        if kind == "sans":
            face = Face.get("InterTight[wght].ttf", wght=600)
            d, *_ = text_path(face, t, size, -.04)
            col = fill
        else:
            face = Face.get("InstrumentSerif-Italic.ttf")
            d, *_ = text_path(face, t, size * 1.06, -.01)
            col = serif_fill
        out.append(f'<g transform="translate({f(x)} {f(y + i * lead)})"><path fill="{col}" d="{d}"/></g>')
    return "".join(out)


def small_text(t, x, y, size, fill, w=500, track=0.0, font="Inter.ttf"):
    face = Face.get(font, wght=w, opsz=14) if font == "Inter.ttf" else Face.get(font, wght=w)
    d, x0, x1, *_ = text_path(face, t, size, track)
    return f'<g transform="translate({f(x)} {f(y)})"><path fill="{fill}" d="{d}"/></g>', x1


def aurora(w, h, dark=False, spots=None):
    bid = uid("au")
    spots = spots or [(.82, .1, .42, "#1FB6F2", .35), (.98, .5, .38, "#4F46E5", .3), (.7, .95, .35, "#9061F9", .25)]
    circles = "".join(f'<circle cx="{f(cx * w)}" cy="{f(cy * h)}" r="{f(r * w)}" fill="{c}" opacity="{o * (1.5 if dark else 1)}"/>'
                      for cx, cy, r, c, o in spots)
    return (f'<defs><filter id="{bid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{f(w * .06)}"/></filter></defs>'
            f'<g filter="url(#{bid})">{circles}</g>')


def og_image():
    W, H = 1200, 630
    inner = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>', aurora(W, H)]
    li, vb = lockup("h")
    s = 34 / 100
    inner.append(f'<g transform="translate({f(72 - vb[0] * s)} {f(78 - vb[1] * s)}) scale({f(s)})">{li}</g>')
    inner.append(headline([("El mismo día.", "sans"), ("Otra energía.", "serif")], 72, 300, 104, 112))
    t, _ = small_text("Coach de IA de energía y foco para fundadores", 74, 520, 26, "#3D3A48", 500)
    inner.append(t)
    t, _ = small_text("Beta · 20 plazas · desde el 18 de diciembre", 74, 562, 22, INDIGO, 600)
    inner.append(t)
    x0, y0, x1, y1 = enso_bbox(ENSO)
    s2 = 430 / (x1 - x0)
    inner.append(f'<g transform="translate({f(1150 - x1 * s2)} {f(315 - (y0 + y1) / 2 * s2)}) scale({f(s2)})" opacity=".96">{enso_group(ENSO)}</g>')
    return svg_doc("".join(inner), (0, 0, W, H), W, H, "UrCoach: el mismo día, otra energía")


def linkedin_banner():
    W, H = 1584, 396
    gid = uid("nb")
    inner = [f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#15122A"/>'
             f'<stop offset="1" stop-color="{NIGHT}"/></linearGradient></defs>',
             f'<rect width="{W}" height="{H}" fill="url(#{gid})"/>',
             aurora(W, H, True, [(.86, .2, .2, "#1FB6F2", .3), (.95, .8, .22, "#4F46E5", .35), (.7, 1, .18, "#9061F9", .3)])]
    x0, y0, x1, y1 = enso_bbox(ENSO)
    s2 = 300 / (x1 - x0)
    inner.append(f'<g transform="translate({f(1480 - x1 * s2)} {f(198 - (y0 + y1) / 2 * s2)}) scale({f(s2)})">{enso_group(ENSO, "day", True)}</g>')
    inner.append(headline([("El mismo día.", "sans"), ("Otra energía.", "serif")], 470, 170, 72, 80, "#FFFFFF", "#A5B4FC"))
    t, _ = small_text("Coach de IA de energía y foco para fundadores", 472, 300, 22, "#B9B6C9", 500)
    inner.append(t)
    return svg_doc("".join(inner), (0, 0, W, H), W, H, "UrCoach")


# --------------------------------------------------------------------------- tokens
BLOCKS = [
    ("sueno", "Sueño", "#ECE9FE", "#4C3FB8"), ("luz", "Luz", "#FFF2D6", "#8A5300"),
    ("medita", "Meditación", "#D5F5EF", "#0B6B60"), ("foco", "Foco", "#4F46E5", "#FFFFFF"),
    ("reunion", "Reuniones", "#EEF1F5", "#475569"), ("comida", "Comida", "#FFE8D6", "#9A3412"),
    ("descanso", "Descanso", "#DCF3FD", "#075985"), ("entreno", "Entreno", "#DCFCE7", "#166534"),
    ("lectura", "Lectura", "#FFE0E6", "#9F1239"), ("descon", "Desconexión", "#DBE4FF", "#1E3A8A"),
]

CORE = [
    ("tinta", "Tinta", INK, "Texto, wordmark y fondos de noche."),
    ("papel", "Papel", PAPER, "Fondo de la web y de los documentos."),
    ("niebla", "Niebla", "#F2F1F7", "Superficies suaves, tarjetas secundarias."),
    ("indigo", "Índigo foco", INDIGO, "El foco, los enlaces y las acciones dentro del producto. La acción principal de la web va en tinta."),
    ("noche", "Noche", NIGHT, "Secciones oscuras y fondo del icono de la app."),
]
DAY = [("cielo", "Cielo", "#1FB6F2", "La mañana"), ("azur", "Azur", "#4C7CF6", "El arranque"),
       ("indigo", "Índigo", "#4F46E5", "El foco"), ("violeta", "Violeta", "#7C3AED", "La tarde"),
       ("lavanda", "Lavanda", "#9061F9", "La noche")]


def tokens():
    css = [":root{", f"  --uc-ink:{INK}; --uc-paper:{PAPER}; --uc-mist:#F2F1F7; --uc-indigo:{INDIGO}; --uc-night:{NIGHT};",
           "  --uc-ink-2:#3D3A48; --uc-muted:#5B5869; --uc-line:#E9E7F0;",
           "  --uc-day:linear-gradient(100deg," + ",".join(f"{c} {int(t * 100)}%" for t, c in DAY_LIGHT) + ");",
           "  --uc-day-dark:linear-gradient(100deg," + ",".join(f"{c} {int(t * 100)}%" for t, c in DAY_DARK) + ");",
           "  --uc-font-display:\"Inter Tight\",\"Inter\",system-ui,sans-serif;",
           "  --uc-font-text:\"Inter\",system-ui,sans-serif;",
           "  --uc-font-accent:\"Instrument Serif\",Georgia,serif;"]
    for k, n, bg, t in BLOCKS:
        css.append(f"  --uc-{k}:{bg}; --uc-{k}-t:{t};")
    css.append("}")
    data = dict(color=dict(core={k: c for k, _, c, _ in CORE}, day_light=DAY_LIGHT, day_dark=DAY_DARK,
                           blocks={k: dict(bg=bg, text=t) for k, _, bg, t in BLOCKS}),
                font=dict(display="Inter Tight 600", text="Inter 400/500", accent="Instrument Serif italic"))
    return "\n".join(css) + "\n", json.dumps(data, ensure_ascii=False, indent=2)


# --------------------------------------------------------------------------- escritura
def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    ET.fromstring(text) if path.suffix == ".svg" else None
    return path


def rasterize(svg_path, png_path, w, h=None):
    try:
        import resvg_py
    except ImportError:
        return False
    data = resvg_py.svg_to_bytes(svg_string=svg_path.read_text(), width=w, height=h or w)
    png_path.write_bytes(bytes(data))
    return True


def build_assets():
    out = {}
    L = KIT / "logo"
    for kind, kn in (("h", "horizontal"), ("v", "apilado")):
        for name, word, paint, dark in (("color", INK, "day", False), ("color-sobre-oscuro", "#FFFFFF", "day", True),
                                        ("negro", INK, INK, False), ("blanco", "#FFFFFF", "#FFFFFF", True),
                                        ("indigo", INDIGO, INDIGO, False)):
            inner, vb = lockup(kind, word, paint, dark, pad=.0)
            out[f"{kn}-{name}"] = write(L / f"urcoach-{kn}-{name}.svg", svg_doc(inner, vb))
    for name, paint, dark in (("color", "day", False), ("color-sobre-oscuro", "day", True), ("negro", INK, False),
                              ("blanco", "#FFFFFF", True), ("indigo", INDIGO, False)):
        out[f"simbolo-{name}"] = write(L / f"urcoach-simbolo-{name}.svg", symbol_doc(paint, dark))
    A = KIT / "app"
    out["app-claro"] = write(A / "app-icon-claro.svg", app_icon(False))
    out["app-oscuro"] = write(A / "app-icon-oscuro.svg", app_icon(True))
    out["favicon"] = write(A / "favicon.svg", favicon_doc())
    out["fav-icon-claro"] = write(A / "_favicon-claro.svg", app_icon(False, fav=True))
    S = KIT / "social"
    out["og"] = write(S / "og-image-1200x630.svg", og_image())
    out["li"] = write(S / "linkedin-banner-1584x396.svg", linkedin_banner())
    css, js = tokens()
    write(KIT / "tokens" / "tokens.css", css)
    write(KIT / "tokens" / "tokens.json", js)
    pngs = [(out["favicon"], A / "favicon-16.png", 16), (out["favicon"], A / "favicon-32.png", 32),
            (out["favicon"], A / "favicon-48.png", 48), (out["app-claro"], A / "apple-touch-icon-180.png", 180),
            (out["app-claro"], A / "icon-192.png", 192), (out["app-claro"], A / "icon-512.png", 512),
            (out["app-oscuro"], A / "app-icon-oscuro-1024.png", 1024), (out["app-claro"], A / "app-icon-claro-1024.png", 1024),
            (out["app-oscuro"], S / "avatar-400.png", 400)]
    ok = all(rasterize(s, p, w) for s, p, w in pngs)
    ok = ok and rasterize(out["og"], S / "og-image-1200x630.png", 1200, 630)
    ok = ok and rasterize(out["li"], S / "linkedin-banner-1584x396.png", 1584, 396)
    (A / "_favicon-claro.svg").unlink(missing_ok=True)
    return out, ok


if __name__ == "__main__":
    out, ok = build_assets()
    print(f"{len(out)} SVG escritos en {KIT}; PNG: {'sí' if ok else 'pendiente (falta resvg_py)'}")
    for t, c in DAY_LIGHT:
        print(t, c, f"contraste sobre papel {contrast(c, PAPER):.2f}")
