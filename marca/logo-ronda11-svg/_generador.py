#!/usr/bin/env python3
"""Ronda 11 de UrCoach: isologotipo = ensō (Trazo, elegido en la ronda 10) + nombre.

Diez tipografías OFL convertidas en contornos con HarfBuzz (kerning real) y fontTools.
En cada propuesta:
- el ensō se alinea al centro óptico de la altura de mayúsculas (o de la x en minúsculas);
- el grosor del cuerpo del trazo acompaña al asta de la letra (medida en la «I»);
- el espacio entre símbolo y nombre se mide de tinta a tinta.

Salida: /Users/philippesaint-hubert/Ucoach/marca/urcoach-logo-ronda11.html
y los SVG de cada isologotipo en logos-r11/svg/.
"""
import io
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
sys.path.insert(0, str(HERE.parent / "logos-r10"))
from build import enso, stroke_outline  # noqa: E402  (ronda 10: geometría del ensō)

OUT = Path("/Users/philippesaint-hubert/Ucoach/marca/urcoach-logo-ronda11.html")
SVGDIR = HERE / "svg"
FONTDIR = HERE / "fonts"
INK = "#121018"
INDIGO = "#4f46e5"


def f(x):
    s = f"{x:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


# --------------------------------------------------------------------------- fuentes
class Face:
    _cache = {}

    def __init__(self, file, axes):
        tt = TTFont(FONTDIR / file)
        if "fvar" in tt:
            tt = instancer.instantiateVariableFont(tt, axes)
        buf = io.BytesIO()
        tt.save(buf)
        data = buf.getvalue()
        self.tt = TTFont(io.BytesIO(data))
        self.gs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.upem = self.tt["head"].unitsPerEm
        os2 = self.tt["OS/2"]
        self.cap = self._ink_h("H") or os2.sCapHeight
        self.xh = self._ink_h("x") or os2.sxHeight
        self.hbfont = hb.Font(hb.Face(data))

    @classmethod
    def get(cls, file, **axes):
        k = (file, tuple(sorted(axes.items())))
        if k not in cls._cache:
            cls._cache[k] = Face(file, axes)
        return cls._cache[k]

    def _ink_h(self, ch):
        name = self.tt.getBestCmap().get(ord(ch))
        if not name:
            return None
        bp = BoundsPen(self.gs)
        self.gs[name].draw(bp)
        return bp.bounds[3] if bp.bounds else None

    def stem(self, ch):
        name = self.tt.getBestCmap()[ord(ch)]
        bp = BoundsPen(self.gs)
        self.gs[name].draw(bp)
        return bp.bounds[2] - bp.bounds[0]


def shape(face, text, sc, x, track, kern):
    """Devuelve (paths, bounds, x_final, glifos). sc: unidades de fuente -> unidades del logo."""
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(face.hbfont, buf, {"kern": True, "liga": False})
    paths, glyphs = [], []
    bx0 = by0 = 1e9
    bx1 = by1 = -1e9
    n = len(buf.glyph_infos)
    for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        name = face.order[info.codepoint]
        ch = text[info.cluster]
        gx = x + pos.x_offset * sc
        tr = (sc, 0, 0, -sc, gx, -pos.y_offset * sc)
        pen = SVGPathPen(face.gs)
        face.gs[name].draw(TransformPen(pen, tr))
        bp = BoundsPen(face.gs)
        face.gs[name].draw(TransformPen(bp, tr))
        d = pen.getCommands()
        if bp.bounds:
            b = bp.bounds
            bx0, by0, bx1, by1 = min(bx0, b[0]), min(by0, b[1]), max(bx1, b[2]), max(by1, b[3])
        glyphs.append(dict(ch=ch, d=d, bounds=bp.bounds, x=gx, adv=pos.x_advance * sc))
        x += pos.x_advance * sc
        if i < n - 1:
            x += track * 100
            nxt = text[buf.glyph_infos[i + 1].cluster]
            x += kern.get(ch + nxt, 0) * 100
    return glyphs, (bx0, by0, bx1, by1), x


# --------------------------------------------------------------------------- ensō
def enso_poly(D, body, cx, cy, hi=.11, hr=1.85):
    """Ensō de diámetro de tinta D con cuerpo de grosor `body` (unidades del logo), centrado en (cx, cy).
    El cuerpo se limita a 0,075-0,11 D para no deformar el símbolo elegido en la ronda 10 (0,089 D)."""
    body = min(max(body, .075 * D), hi * D)
    s = 1.0
    wb = 8.5
    for _ in range(4):
        wbs = body / s
        C, W = enso(wh=wbs * hr, wb=wbs, wt=max(.9, wbs * .14))
        P = stroke_outline(C, W, cap1=False)
        xs = [p[0] for p in P]
        ys = [p[1] for p in P]
        size = max(max(xs) - min(xs), max(ys) - min(ys))
        s = D / size
    mx = (max(xs) + min(xs)) / 2
    my = (max(ys) + min(ys)) / 2
    pts = [(cx + (px - mx) * s, cy + (py - my) * s) for px, py in P]
    return "M" + "L".join(f"{f(a)} {f(b)}" for a, b in pts) + "Z", (min(p[0] for p in pts), min(p[1] for p in pts),
                                                                    max(p[0] for p in pts), max(p[1] for p in pts))


# --------------------------------------------------------------------------- propuestas
P = [
    dict(n="01", name="Inter Tight", reg="Neutral y precisa", refs="Apple",
         segs=[("InterTight[wght].ttf", dict(wght=600), "UrCoach")], track=-.022, kern={"rC": -.01},
         ref="cap", D=1.5, gap=.36, stem="I", k=1.05,
         css="font-family:'Inter Tight';font-weight:600;letter-spacing:-.022em",
         why="Inter se dibujó para pantallas y es la libre que más se parece a la San Francisco de Apple. La versión Tight trae el espaciado apretado de titular. Es la opción que menos opina: deja todo el carácter al ensō.",
         tune="Seminegrita 600 con espaciado −2,2 %. La «r» se acerca 1 punto a la «C», que deja un hueco grande. El ensō mide 1,5 veces la altura de mayúsculas.",
         weak="Inter está en miles de productos: el nombre solo no es reconocible y depende del símbolo para ser propio."),
    dict(n="02", name="Geist", reg="Herramienta de desarrollo", refs="Vercel y Linear",
         segs=[("Geist[wght].ttf", dict(wght=500), "urcoach")], track=-.03, kern={},
         ref="x", D=2.05, gap=.42, stem="I", k=1.0,
         css="font-family:'Geist';font-weight:500;letter-spacing:-.03em",
         why="La hizo Vercel inspirada en la tipografía suiza, y es la que se ve en las herramientas de desarrollo. UrCoach vive dentro de Claude Code: en minúsculas suena a comando, a algo que se escribe.",
         tune="Medium 500, todo en minúsculas y espaciado −3 %. Sin la «C» mayúscula, el ensō se alinea a la altura de la x y mide el doble que ella.",
         weak="En minúsculas se pierde la lectura «Ur + Coach»; se puede leer «urco-ach». Muy de desarrolladores: menos cálida para un fundador que no programa."),
    dict(n="03", name="Instrument Sans", reg="Hermana de la serif de la landing", refs="la landing actual",
         segs=[("InstrumentSans[wdth,wght].ttf", dict(wght=600, wdth=88), "UrCoach")], track=-.012, kern={},
         ref="cap", D=1.52, gap=.36, stem="I", k=1.05,
         css="font-family:'Instrument Sans';font-weight:600;font-stretch:88%;letter-spacing:-.012em",
         why="Es la versión de palo seco de la Instrument Serif que ya firma los titulares de la landing en cursiva. Marca y web hablan con la misma familia, sin una tercera tipografía.",
         tune="Seminegrita 600, anchura al 88 % para que el nombre sea compacto, espaciado −1,2 %.",
         weak="Al estrecharla gana elegancia pero pierde presencia a tamaños pequeños; a 16 px conviene la anchura normal."),
    dict(n="04", name="Sora", reg="Geométrica tecnológica", refs="las fintech",
         segs=[("Sora[wght].ttf", dict(wght=600), "UrCoach")], track=-.03, kern={},
         ref="cap", D=1.48, gap=.34, stem="I", k=1.0,
         css="font-family:'Sora';font-weight:600;letter-spacing:-.03em",
         why="Formas geométricas y aberturas amplias: la «o» y la «C» casi son círculos, y responden al ensō. Suena a producto financiero o tecnológico serio.",
         tune="Seminegrita 600, espaciado −3 % porque de serie es muy abierta.",
         weak="Muy popular en cripto y web3 entre 2021 y 2023; puede envejecer con esa ola."),
    dict(n="05", name="Outfit", reg="Fina y luminosa", refs="Oura y el Apple Watch",
         segs=[("Outfit[wght].ttf", dict(wght=300), "UrCoach")], track=.0, kern={},
         ref="cap", D=1.5, gap=.38, stem="I", k=1.25,
         css="font-family:'Outfit';font-weight:300;letter-spacing:0",
         why="Geométrica en peso ligero: el nombre susurra y el ensō, también más fino, hace de protagonista. Es el registro de la salud y el sueño premium, con mucho aire.",
         tune="Ligera 300 sin cambiar el espaciado. El ensō se aligera para acompañar el asta fina.",
         weak="Por debajo de 20 px el peso 300 se rompe sobre fondos oscuros: necesita una versión 400 para tamaños pequeños."),
    dict(n="06", name="Michroma", reg="Ancha en mayúsculas", refs="Tesla y SpaceX",
         segs=[("Michroma-Regular.ttf", {}, "URCOACH")], track=.14, kern={},
         ref="cap", D=1.95, gap=.48, stem="I", k=.95,
         css="font-family:'Michroma';font-weight:400;letter-spacing:.14em;text-transform:uppercase",
         why="Mayúsculas extendidas y espaciadas, el registro de automoción y aeroespacial. Evoca la Microgramma y el futuro de los años 60. Es la más «máquina» de las diez.",
         tune="Mayúsculas con espaciado +14 %. El ensō crece a casi 2 veces la altura de mayúsculas porque las letras son bajas y anchas.",
         weak="El nombre se vuelve largo: en la barra de la landing ocupa el doble. En mayúsculas se pierde «Ur + Coach» y se lee «URCO-ACH»."),
    dict(n="07", name="Space Grotesk", reg="Ingeniería con carácter", refs="un laboratorio de I+D",
         segs=[("SpaceGrotesk[wght].ttf", dict(wght=500), "UrCoach")], track=-.025, kern={},
         ref="cap", D=1.5, gap=.36, stem="I", k=1.05,
         css="font-family:'Space Grotesk';font-weight:500;letter-spacing:-.025em",
         why="Nace de una monoespaciada y conserva detalles de máquina de escribir en la «a» y la «r». Técnica pero con personalidad, como un instrumento de laboratorio.",
         tune="Medium 500, espaciado −2,5 %.",
         weak="Sus rarezas compiten con el ensō: dos elementos con carácter en el mismo logo."),
    dict(n="08", name="Hanken Grotesk", reg="Suiza y sobria", refs="Stripe y Revolut",
         segs=[("HankenGrotesk[wght].ttf", dict(wght=600), "UrCoach")], track=-.03, kern={},
         ref="cap", D=1.5, gap=.36, stem="I", k=1.05,
         css="font-family:'Hanken Grotesk';font-weight:600;letter-spacing:-.03em",
         why="Grotesca de corte suizo, la familia de letras que usan las fintech premium. Más cálida que Inter, con la «a» y la «C» algo más redondas.",
         tune="Seminegrita 600 y espaciado −3 %.",
         weak="Discreta hasta el punto de ser intercambiable con otras grotescas; el valor está en el ajuste, no en la letra."),
    dict(n="09", name="Instrument Serif", reg="Editorial premium", refs="las revistas y el lujo",
         segs=[("InstrumentSerif-Regular.ttf", {}, "UrCoach")], track=-.01, kern={},
         ref="cap", D=1.42, gap=.34, stem=None, k=1.0, stem_fixed=11.5,
         css="font-family:'Instrument Serif';font-weight:400;letter-spacing:-.01em",
         why="Una serif de contraste alto, la misma que ya firma la segunda línea de los titulares de la landing. Con el ensō de pincel, el logo pasa de herramienta a oficio: un coach con criterio.",
         tune="Regular, espaciado −1 %. El grosor del ensō sigue los trazos gruesos de la serif, no los finos.",
         weak="Es la que menos dice «tecnología». A 16 px los trazos finos desaparecen."),
    dict(n="10", name="Figtree, dos pesos", reg="La letra de la landing, en dos voces", refs="Headspace y Calm",
         segs=[("Figtree[wght].ttf", dict(wght=400), "Ur"), ("Figtree[wght].ttf", dict(wght=700), "Coach")],
         track=-.02, kern={}, ref="cap", D=1.5, gap=.36, stem="I", k=1.0, stem_seg=1,
         css="font-family:'Figtree';letter-spacing:-.02em",
         why="Es la letra que ya usa toda la landing, con «Ur» en regular y «Coach» en negrita: se lee «tu coach» sin espacio. No hay que añadir ninguna tipografía.",
         tune="Regular 400 y negrita 700, espaciado −2 %. El ensō sigue el asta de la negrita.",
         weak="Dos pesos en una palabra es un recurso conocido; si no se cuida, parece un subrayado del nombre más que un logo."),
]


def wordmark(p, enso_o=False, o_body=None):
    """Compone el nombre a altura de mayúsculas 100. Devuelve dict con paths, bounds y la cara de referencia."""
    face0 = Face.get(p["segs"][0][0], **p["segs"][0][1])
    sc0 = 100 / face0.cap
    x = 0.0
    glyphs = []
    for file, axes, text in p["segs"]:
        face = Face.get(file, **axes)
        sc = 100 / face.cap
        g, _, x = shape(face, text, sc, x, p["track"], p["kern"])
        glyphs += g
        x += p["track"] * 100
    seg = p["segs"][p.get("stem_seg", 0)]
    sface = Face.get(seg[0], **seg[1])
    if p.get("stem"):
        stem = sface.stem(p["stem"]) * 100 / sface.cap
    else:
        stem = p["stem_fixed"]
    paths = []
    for g in glyphs:
        if enso_o and g["ch"] == "o" and g["bounds"]:
            b = g["bounds"]
            D = (b[3] - b[1]) * 1.06
            cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
            d, _ = enso_poly(D, (o_body or stem) * .95, cx, cy, hi=.24, hr=1.3)
            paths.append(("enso", d))
        else:
            paths.append(("g", g["d"]))
    bs = [g["bounds"] for g in glyphs if g["bounds"]]
    x0, x1 = min(b[0] for b in bs), max(b[2] for b in bs)
    ytop, ybot = min(b[1] for b in bs), max(b[3] for b in bs)
    xh = face0.xh * sc0
    return dict(paths=paths, x0=x0, x1=x1, ytop=ytop, ybot=ybot, stem=stem, xh=xh)


def lockup(p, kind="h", accent=None):
    """kind: h (horizontal), v (apilado). Devuelve (svg_inner, viewbox)."""
    w = wordmark(p)
    refh = 100 if p["ref"] == "cap" else w["xh"]
    body = w["stem"] * p["k"]
    if kind == "h":
        D = p["D"] * refh
        cx = w["x0"] - p["gap"] * D - D / 2
        cy = -refh / 2
        d, eb = enso_poly(D, body, cx, cy)
    else:
        D = 2.7 * 100 if p["ref"] == "cap" else 2.7 * 100
        cx = (w["x0"] + w["x1"]) / 2
        cy = w["ytop"] - .5 * 100 - D / 2
        d, eb = enso_poly(D, body * 1.6, cx, cy)
    ecol = f' fill="{accent}"' if accent else ""
    inner = f'<path{ecol} d="{d}"/>' + "".join(f'<path d="{gd}"/>' for _, gd in w["paths"])
    X0, Y0 = min(eb[0], w["x0"]), min(eb[1], w["ytop"])
    X1, Y1 = max(eb[2], w["x1"]), max(eb[3], w["ybot"], 0)
    return inner, (X0, Y0, X1 - X0, Y1 - Y0)


def svg(inner, vb, cls, pad=0.0, title=None):
    x, y, w, h = vb
    pw = pad * h
    t = f"<title>{title}</title>" if title else ""
    aria = ' role="img"' if title else ' aria-hidden="true"'
    return (f'<svg class="{cls}" viewBox="{f(x - pw)} {f(y - pw)} {f(w + 2 * pw)} {f(h + 2 * pw)}" '
            f'xmlns="http://www.w3.org/2000/svg"{aria} fill="currentColor">{t}{inner}</svg>')


def enso_o_mark(p):
    w = wordmark(p, enso_o=True)
    inner = "".join(f'<path d="{d}"/>' for _, d in w["paths"])
    return inner, (w["x0"], w["ytop"], w["x1"] - w["x0"], w["ybot"] - w["ytop"])


# --------------------------------------------------------------------------- página
def nav(svgh, dark):
    return (f'<div class="nav {"nav-d" if dark else "nav-l"}"><span class="nl">{svgh}</span>'
            f'<span class="links"><span>Método</span><span>Preguntas</span></span>'
            f'<span class="cta">Quiero una plaza</span></div>')


def card(p):
    ih, vbh = lockup(p, "h")
    ia, _ = lockup(p, "h", accent=INDIGO)
    iv, vbv = lockup(p, "v")
    (SVGDIR / f"r11-{p['n']}-horizontal.svg").write_text(
        svg(ih, vbh, "x", .12).replace('class="x" ', '').replace('fill="currentColor"', f'fill="{INK}"'))
    (SVGDIR / f"r11-{p['n']}-apilado.svg").write_text(
        svg(iv, vbv, "x", .12).replace('class="x" ', '').replace('fill="currentColor"', f'fill="{INK}"'))
    spec = " · ".join(
        f"{t} {a.get('wght', 400)}" + (f" ancho {a['wdth']} %" if "wdth" in a else "") for _, a, t in p["segs"])
    return f'''
<section class="card" id="p{p["n"]}">
  <header class="ch">
    <div class="cnum">{p["n"]}</div>
    <div class="ctit"><h2>{p["name"]}</h2><p>{p["reg"]} · en la línea de {p["refs"]}</p></div>
    <div class="cfont"><span>Ajuste</span><b>{spec}</b></div>
  </header>
  <div class="row q1">
    <figure class="pane big w">{svg(ih, vbh, "lu", .02, "UrCoach")}<figcaption>Isologotipo · negro</figcaption></figure>
    <figure class="pane big k">{svg(ih, vbh, "lu", .02)}<figcaption>Sobre negro</figcaption></figure>
  </div>
  <div class="row q2">
    <figure class="pane st w">{svg(iv, vbv, "lv", .02)}<figcaption>Apilado</figcaption></figure>
    <figure class="pane mid w">{svg(ia, vbh, "lm", .02)}<figcaption>Ensō en índigo</figcaption></figure>
    <figure class="pane mid i">{svg(ih, vbh, "lm", .02)}<figcaption>Sobre índigo</figcaption></figure>
    <figure class="pane mid sz w"><div class="sizes">{svg(ih, vbh, "s28")}{svg(ih, vbh, "s20")}{svg(ih, vbh, "s14")}</div><figcaption>28, 20 y 14 px de alto</figcaption></figure>
  </div>
  <div class="row r2">{nav(svg(ih, vbh, "ln"), False)}{nav(svg(ih, vbh, "ln"), True)}</div>
  <div class="row q4">
    <div class="txt"><h3>Por qué esta letra</h3><p>{p["why"]}</p></div>
    <div class="txt"><h3>Cómo está ajustada</h3><p>{p["tune"]}</p></div>
    <div class="txt weak"><h3>Punto débil</h3><p>{p["weak"]}</p></div>
    <div class="txt spec"><h3>En uso, texto real</h3><p class="sp" style="{p["css"]}">Duerme bien. Rinde mejor.</p><p class="sp2" style="{p["css"]};font-weight:inherit">Tu día, planificado con tu noche · 7 h 42 min</p></div>
  </div>
</section>'''


FONTS = ("https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500"
         "&family=Inter+Tight:wght@600&family=Instrument+Sans:wdth,wght@75..100,600&family=Sora:wght@600"
         "&family=Outfit:wght@300&family=Michroma&family=Space+Grotesk:wght@500&family=Hanken+Grotesk:wght@600"
         "&family=Instrument+Serif&family=Figtree:wght@400;700&display=swap")

CSS = r"""
.q1{grid-template-columns:1fr 1fr}
.q2{grid-template-columns:.9fr 1fr 1fr 1fr}
.q4{grid-template-columns:1fr 1fr;gap:22px 34px;margin-top:22px}
.pane.big{min-height:220px;padding:36px 28px 44px}
.pane.w{background:#fff}
.pane.k{background:radial-gradient(120% 140% at 20% 0%,#2a2733 0,#0b0a0f 60%);color:#fff}
.pane.k figcaption{color:#77748a}
.pane.i{background:var(--indigo);color:#fff}
.pane.i figcaption{color:rgba(255,255,255,.72)}
.pane.w{color:#000}
svg.lu{width:min(100%,430px);height:auto;max-height:96px}
svg.lv{height:132px;width:auto;max-width:100%}
svg.lm{width:min(100%,250px);height:auto;max-height:56px}
.sizes{display:flex;flex-direction:column;align-items:flex-start;gap:14px}
svg.s28{height:28px;width:auto}svg.s20{height:20px;width:auto}svg.s14{height:14px;width:auto}
.nav .nl{display:flex;align-items:center;min-width:0;flex-shrink:1}
.r2>*,.q1>*,.q2>*{min-width:0}
.nav{overflow:hidden}
.nav .links{min-width:0;overflow:hidden}
@media (max-width:1240px){.nav .links span:nth-child(n+2){display:none}}
svg.ln{height:24px;width:auto;max-width:100%}
.nav-d svg.ln{color:#fff}
.txt.spec .sp{font-size:30px;line-height:1.1;color:var(--ink);margin:2px 0 8px}
.txt.spec .sp2{font-size:15px;color:var(--ink2)}
.txt.spec .sp2[style*="Michroma"]{font-size:11.5px}
.txt.spec .sp[style*="Michroma"]{font-size:20px}
.weak h3{color:#be123c}
.cmp{display:grid;gap:0}
.cmp a{display:grid;grid-template-columns:44px 1fr 210px;align-items:center;gap:18px;padding:18px 4px;border-top:1px solid var(--line);text-decoration:none;color:#000}
.cmp a:hover{background:#faf9fc}
.cmp .cn{font:500 12px "Geist Mono",monospace;color:var(--indigo)}
.cmp svg{height:46px;width:auto;max-width:100%}
.cmp .cl{font-size:13px;color:var(--muted);text-align:right}
.cmp .cl b{display:block;color:var(--ink);font-weight:600;font-size:14px}
.comp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.comp .pane{min-height:200px}
.comp svg{width:min(100%,300px);height:auto;max-height:100px}
.comp svg.lv{height:130px;width:auto}
.comp .note{font-size:13.5px;color:var(--ink2);margin-top:10px}
.chosen{display:flex;align-items:center;gap:22px;margin-top:26px}
.chosen svg{width:84px;height:84px;color:var(--ink)}
.chosen p{margin:0;color:var(--ink2);max-width:62ch}
.rules{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px 30px}
.rules div{border-top:1px solid var(--line);padding-top:12px}
.rules h3{margin:0 0 4px;font-size:15px;font-weight:600}
.rules p{margin:0;color:var(--ink2);font-size:14px}
@media (max-width:980px){.q2{grid-template-columns:1fr 1fr}.q4,.comp,.rules{grid-template-columns:1fr}.cmp a{grid-template-columns:34px 1fr}.cmp .cl{display:none}}
@media (max-width:600px){.q1,.q2{grid-template-columns:1fr}}
"""


def build():
    SVGDIR.mkdir(exist_ok=True)
    css = (HERE / "css_r9.css").read_text() + CSS
    cards = "".join(card(p) for p in P)
    cmp = []
    for p in P:
        ih, vb = lockup(p, "h")
        cmp.append(f'<a href="#p{p["n"]}"><span class="cn">{p["n"]}</span>{svg(ih, vb, "c", .04)}'
                   f'<span class="cl"><b>{p["name"]}</b>{p["reg"]}</span></a>')
    # Composiciones de ejemplo (con la 01)
    p1 = P[0]
    ih, vbh = lockup(p1, "h")
    iv, vbv = lockup(p1, "v")
    io_, vbo = enso_o_mark(p1)
    (SVGDIR / "r11-composicion-enso-como-o.svg").write_text(
        svg(io_, vbo, "x", .12).replace('class="x" ', '').replace('fill="currentColor"', f'fill="{INK}"'))
    C, W = enso()
    ens = "M" + "L".join(f"{f(a)} {f(b)}" for a, b in stroke_outline(C, W, cap1=False)) + "Z"
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>UrCoach · Isologotipo, ronda 11</title>
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<div class="wrap">
  <header class="hero-top">
    <div class="eyebrow">UrCoach · Marca · Ronda 11</div>
    <h1>El ensō ya está. <span>Ahora, la letra.</span></h1>
    <p class="lead">Diez tipografías para el isologotipo, todas junto al Trazo de la ronda 10. Cada nombre está convertido en contornos con su kerning real, y en cada una el ensō se ajusta a la letra: misma altura óptica, el grosor del trazo acompaña al de la letra y la separación medida de tinta a tinta.</p>
    <div class="chosen"><svg viewBox="0 0 120 120" aria-hidden="true" fill="currentColor"><path d="{ens}"/></svg>
      <p><b>Símbolo elegido: 01 Trazo.</b> Un círculo de un solo gesto que queda abierto: el día completo no es el día lleno. Lo que cambia en esta ronda es solo el nombre y cómo se junta con el símbolo.</p></div>
  </header>

  <section class="panel">
    <h2>Las diez, una debajo de otra</h2>
    <p class="sub">A la misma altura de mayúsculas, para comparar de un vistazo. Pulsa cualquiera para ver su ficha.</p>
    <div class="cmp">{"".join(cmp)}</div>
  </section>

  <section class="panel">
    <h2>Reglas comunes a las diez</h2>
    <p class="sub">Lo que no cambia de una propuesta a otra, para que compares solo la letra.</p>
    <div class="rules">
      <div><h3>Altura</h3><p>El ensō mide 1,5 veces la altura de mayúsculas, centrado en ella. En la 02, en minúsculas, se mide sobre la altura de la x; en la 06, de mayúsculas anchas, crece a 1,95.</p></div>
      <div><h3>Grosor</h3><p>El cuerpo del trazo se acerca al asta de la «I»: si la letra es fina, el ensō es más fino; si es negrita, pesa más. Siempre dentro de un margen para que siga siendo el ensō elegido.</p></div>
      <div><h3>Separación</h3><p>Entre un tercio y la mitad del diámetro del ensō, medida de tinta a tinta. Es también el margen mínimo alrededor del logo.</p></div>
    </div>
  </section>

  {cards}

  <section class="panel">
    <h2>Tres formas de juntarlos</h2>
    <p class="sub">Composiciones de ejemplo con la 01. Cualquiera se aplica a la letra que elijas.</p>
    <div class="comp">
      <div><figure class="pane w">{svg(ih, vbh, "c", .04)}<figcaption>Horizontal</figcaption></figure><p class="note">La principal: barra de la web, firma de email, documentos.</p></div>
      <div><figure class="pane w">{svg(iv, vbv, "lv", .04)}<figcaption>Apilado</figcaption></figure><p class="note">Para avatares, portadas y la pantalla de inicio de la app.</p></div>
      <div><figure class="pane w">{svg(io_, vbo, "c", .04)}<figcaption>El ensō como «o»</figcaption></figure><p class="note">El símbolo vive dentro del nombre. Es más memorable, pero se lee peor pequeño y obliga a tener además el ensō suelto.</p></div>
    </div>
  </section>

  <footer class="foot">UrCoach · Ronda 11 de isologotipo · 20 de noviembre de 2026 · Nombre de trabajo. Las diez tipografías son de Google Fonts con licencia SIL Open Font License: se pueden usar en la marca y en la app sin pagar. Los nombres están convertidos en contornos con HarfBuzz; los SVG de cada isologotipo están exportados.</footer>
</div>
</body>
</html>
'''


def validate(html):
    errors = 0
    for i, s in enumerate(re.findall(r"<svg\b.*?</svg>", html, flags=re.S)):
        try:
            ET.fromstring(s)
        except ET.ParseError as e:
            errors += 1
            print(f"SVG {i} mal formado: {e}", file=sys.stderr)
    if "—" in html:
        print("Hay guiones largos", file=sys.stderr)
        errors += 1
    ids = re.findall(r'\sid="([^"]+)"', html)
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        print("IDs duplicados:", sorted(dup)[:10], file=sys.stderr)
        errors += 1
    return errors


if __name__ == "__main__":
    html = build()
    err = validate(html)
    OUT.write_text(html, encoding="utf-8")
    print(f"Escrito {OUT} ({len(html) // 1024} KB), errores: {err}")
    for p in P:
        w = wordmark(p)
        print(p["n"], p["name"], "stem", f(w["stem"]), "ancho", f(w["x1"] - w["x0"]))
    sys.exit(1 if err else 0)
