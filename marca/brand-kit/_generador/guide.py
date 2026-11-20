#!/usr/bin/env python3
"""Guía del brand kit de UrCoach -> /Users/philippesaint-hubert/Ucoach/marca/urcoach-brand-kit.html"""
import math
import re
import sys
import xml.etree.ElementTree as ET

import build_kit as K

K.build_assets()
B = "brand-kit/"


def enso_inline(paint="day", dark=False, spec=K.ENSO, cls="ens"):
    x0, y0, x1, y1 = K.enso_bbox(spec)
    s = max(x1 - x0, y1 - y0) + 8
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return (f'<svg class="{cls}" viewBox="{K.f(cx - s / 2)} {K.f(cy - s / 2)} {K.f(s)} {K.f(s)}" aria-hidden="true">'
            f'{K.enso_group(spec, paint, dark)}</svg>')


def lockup_inline(kind="h", word=K.INK, paint="day", dark=False, cls="lk", title=None):
    inner, vb = K.lockup(kind, word, paint, dark)
    t = f' role="img" aria-label="{title}"' if title else ' aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="{" ".join(K.f(v) for v in vb)}"{t}>{inner}</svg>'


def day_diagram():
    """El trazo es el día: ensō grande con marcas de momento."""
    spec = K.ENSO
    a0, sw = spec["a0"], spec["sweep"]
    marks = [(0.0, "07:00", "Brief de la mañana", "La cabeza del trazo: la energía del día entero."),
             (.30, "09:00", "Foco", "El tramo más ancho y estable."),
             (.62, "15:00", "Descanso y movimiento", "El trazo afloja, sin romperse."),
             (.86, "21:30", "Cierre", "Se apaga el día."),
             (1.0, "22:00", "Desconexión", "La cola se queda sin tinta. El hueco es la noche.")]
    labels = []
    for t, h, n, d in marks:
        a = math.radians(a0 + sw * t)
        r1, r2 = 50, 62
        x1, y1 = 60 + r1 * math.cos(a), 60 + r1 * math.sin(a)
        x2, y2 = 60 + r2 * math.cos(a), 60 + r2 * math.sin(a)
        col = K.color_at(t, K.DAY_LIGHT)
        labels.append(f'<line x1="{K.f(x1)}" y1="{K.f(y1)}" x2="{K.f(x2)}" y2="{K.f(y2)}" stroke="{col}" stroke-width=".6"/>'
                      f'<circle cx="{K.f(x2)}" cy="{K.f(y2)}" r="1.4" fill="{col}"/>')
    svg = (f'<svg class="dayd" viewBox="-12 -12 144 144" aria-hidden="true">{K.enso_group(spec)}{"".join(labels)}'
           f'<text x="60" y="58" text-anchor="middle" class="dd-n">24 h</text>'
           f'<text x="60" y="66" text-anchor="middle" class="dd-s">un trazo</text></svg>')
    lst = "".join(f'<li><i style="background:{K.color_at(t, K.DAY_LIGHT)}"></i><b>{h}</b><span><strong>{n}.</strong> {d}</span></li>'
                  for t, h, n, d in marks)
    return svg, lst


def sw(name, hexv, use, dark_text=False):
    r, g, b = (int(hexv[i:i + 2], 16) for i in (1, 3, 5))
    on = "#fff" if K.contrast(hexv, "#FFFFFF") > K.contrast(hexv, K.INK) else K.INK
    return (f'<div class="sw"><div class="chip" style="background:{hexv};color:{on}"><span>{name}</span></div>'
            f'<dl><dt>HEX</dt><dd>{hexv}</dd><dt>RGB</dt><dd>{r} {g} {b}</dd></dl><p>{use}</p></div>')


def blocks():
    out = []
    for k, n, bg, t in K.BLOCKS:
        c = K.contrast(t, bg)
        out.append(f'<div class="blk" style="background:{bg};color:{t}"><b>{n}</b><span>{bg} · {t}</span>'
                   f'<em>{c:.1f}:1</em></div>')
    return "".join(out)


def gradient_bar(stops):
    return "linear-gradient(90deg," + ",".join(f"{K.color_at(i / 20, stops)} {i * 5}%" for i in range(21)) + ")"


def build():
    dsvg, dlist = day_diagram()
    versions = [
        ("Principal", "urcoach-horizontal-color.svg", "v-l"), ("Sobre oscuro", "urcoach-horizontal-color-sobre-oscuro.svg", "v-d"),
        ("Una tinta · negro", "urcoach-horizontal-negro.svg", "v-l"), ("Una tinta · blanco", "urcoach-horizontal-blanco.svg", "v-i"),
        ("Una tinta · índigo", "urcoach-horizontal-indigo.svg", "v-m"), ("Apilado", "urcoach-apilado-color.svg", "v-l v-st"),
    ]
    vhtml = "".join(f'<figure class="ver {c}"><img src="{B}logo/{f}" alt="UrCoach, {n.lower()}"><figcaption>{n}</figcaption></figure>'
                    for n, f, c in versions)
    wrong = [
        ("No lo estires", "transform:scaleX(1.35)"), ("No lo gires", "transform:rotate(-12deg)"),
        ("Sin sombras ni brillos", "filter:drop-shadow(0 6px 6px rgba(0,0,0,.45))"),
        ("No cambies la letra", "WM"), ("No lo pongas sobre fondos que compiten", "BUSY"),
        ("No cierres el ensō", "RING"),
    ]
    wr = []
    for n, st in wrong:
        if st == "WM":
            art = f'<span class="fake">{enso_inline(cls="fk-e")}<span style="font-family:Georgia,serif;font-weight:700">UrCoach</span></span>'
        elif st == "BUSY":
            art = f'<div class="busy"><img src="{B}logo/urcoach-horizontal-color.svg" alt=""></div>'
        elif st == "RING":
            art = '<span class="fake"><span class="ring"></span><span>UrCoach</span></span>'
        else:
            art = f'<img src="{B}logo/urcoach-horizontal-color.svg" alt="" style="{st}">'
        wr.append(f'<figure class="no"><div class="no-art">{art}</div><figcaption><b>✕</b> {n}</figcaption></figure>')
    core = "".join(sw(n, c, u) for _, n, c, u in K.CORE)
    day = "".join(sw(n, c, u) for _, n, c, u in K.DAY)
    downloads = [
        ("Logo", [("Horizontal, color", "logo/urcoach-horizontal-color.svg"), ("Horizontal, sobre oscuro", "logo/urcoach-horizontal-color-sobre-oscuro.svg"),
                  ("Horizontal, negro", "logo/urcoach-horizontal-negro.svg"), ("Horizontal, blanco", "logo/urcoach-horizontal-blanco.svg"),
                  ("Horizontal, índigo", "logo/urcoach-horizontal-indigo.svg"), ("Apilado, color", "logo/urcoach-apilado-color.svg"),
                  ("Apilado, sobre oscuro", "logo/urcoach-apilado-color-sobre-oscuro.svg"), ("Apilado, negro", "logo/urcoach-apilado-negro.svg"), ("Apilado, blanco", "logo/urcoach-apilado-blanco.svg"), ("Apilado, índigo", "logo/urcoach-apilado-indigo.svg"), ("Símbolo, color", "logo/urcoach-simbolo-color.svg"), ("Símbolo, sobre oscuro", "logo/urcoach-simbolo-color-sobre-oscuro.svg"), ("Símbolo, índigo", "logo/urcoach-simbolo-indigo.svg"),
                  ("Símbolo, negro", "logo/urcoach-simbolo-negro.svg"), ("Símbolo, blanco", "logo/urcoach-simbolo-blanco.svg")]),
        ("App y web", [("Favicon SVG", "app/favicon.svg"), ("Favicon 32 px", "app/favicon-32.png"), ("Apple touch 180", "app/apple-touch-icon-180.png"),
                       ("Icono 512", "app/icon-512.png"), ("Icono app claro 1024", "app/app-icon-claro-1024.png"), ("Icono app oscuro 1024", "app/app-icon-oscuro-1024.png")]),
        ("Redes", [("Imagen para compartir 1200×630", "social/og-image-1200x630.png"), ("Banner LinkedIn 1584×396", "social/linkedin-banner-1584x396.png"),
                   ("Avatar 400", "social/avatar-400.png")]),
        ("Código", [("Variables CSS", "tokens/tokens.css"), ("Tokens JSON", "tokens/tokens.json")]),
    ]
    dl = "".join(f'<div class="dlg"><h3>{g}</h3><ul>' + "".join(f'<li><a href="{B}{p}" download>{n}<span>{p.split(".")[-1].upper()}</span></a></li>' for n, p in items) + "</ul></div>"
                 for g, items in downloads)
    nav_items = [("esencia", "Esencia"), ("logo", "Logo"), ("simbolo", "Símbolo"), ("color", "Color"), ("tipografia", "Tipografía"),
                 ("componentes", "Componentes"), ("voz", "Voz"), ("aplicaciones", "Aplicaciones"), ("descargas", "Descargas")]
    toc = "".join(f'<a href="#{i}"><span>{n:02d}</span>{t}</a>' for n, (i, t) in enumerate(nav_items, 1))
    css = open(K.KIT / "tokens" / "tokens.css").read()
    html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>UrCoach · Brand kit</title>
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{B}app/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600&family=Inter:opsz,wght@14..32,400..600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
{css}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth;scroll-padding-top:24px}}
body{{margin:0;background:var(--uc-paper);color:var(--uc-ink);font:400 16px/1.6 var(--uc-font-text);-webkit-font-smoothing:antialiased;font-feature-settings:"cv11","ss01"}}
.wrap{{width:min(1200px,100% - 32px);margin-inline:auto}}
h1,h2,h3{{font-family:var(--uc-font-display);font-weight:600;letter-spacing:-.035em;margin:0}}
em.s{{font-family:var(--uc-font-accent);font-style:italic;font-weight:400;letter-spacing:-.01em;color:var(--uc-indigo)}}
.cover{{position:relative;overflow:hidden;background:var(--uc-night);color:#fff;padding:28px 0 0}}
.cover:before{{content:"";position:absolute;inset:-20% -10% auto auto;width:70vw;height:70vw;max-width:900px;max-height:900px;background:radial-gradient(closest-side,rgba(31,182,242,.28),transparent),radial-gradient(closest-side at 70% 70%,rgba(124,58,237,.35),transparent);filter:blur(20px)}}
.ctop{{position:relative;display:flex;justify-content:space-between;align-items:center;font-size:13px;color:#b9b6c9}}
.ctop svg{{height:26px;width:auto}}
.chero{{position:relative;display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;padding:90px 0 110px}}
.chero h1{{font-size:clamp(48px,7.4vw,104px);line-height:.95;letter-spacing:-.035em}}
.chero h1 em{{color:#a5b4fc}}
.chero p{{color:#c9c6d8;font-size:19px;max-width:46ch;margin:26px 0 0}}
.chero .ens{{width:100%;max-width:440px;justify-self:end;filter:drop-shadow(0 30px 80px rgba(79,70,229,.45))}}
.toc{{position:relative;display:flex;gap:6px;flex-wrap:wrap;padding:0 0 28px}}
.toc a{{color:#d6d3e4;text-decoration:none;font-size:13.5px;padding:8px 12px;border-radius:999px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}}
.toc a span{{font-variant-numeric:tabular-nums;color:#8b88a0;margin-right:6px}}
.toc a:hover{{background:rgba(255,255,255,.12)}}
section.s{{padding:110px 0 30px}}
.sh{{display:grid;grid-template-columns:200px 1fr;gap:30px;margin-bottom:44px}}
.sh .n{{font:500 13px var(--uc-font-text);color:var(--uc-indigo);letter-spacing:.06em;text-transform:uppercase;padding-top:14px}}
.sh h2{{font-size:clamp(34px,4.4vw,58px);line-height:1;letter-spacing:-.03em}}
.sh p{{color:var(--uc-ink-2);font-size:18px;max-width:62ch;margin:18px 0 0}}
.card{{background:#fff;border-radius:24px;box-shadow:0 0 0 1px var(--uc-line),0 20px 40px -28px rgba(40,30,90,.25)}}
.grid{{display:grid;gap:16px}}
.g2{{grid-template-columns:1fr 1fr}}.g3{{grid-template-columns:repeat(3,1fr)}}.g4{{grid-template-columns:repeat(4,1fr)}}.g5{{grid-template-columns:repeat(5,1fr)}}
.ess .card{{padding:28px}}
.ess h3{{font-size:22px;margin-bottom:8px}}
.ess p{{margin:0;color:var(--uc-ink-2)}}
.ess .big{{grid-column:1/-1;padding:44px;display:flex;justify-content:space-between;gap:30px;align-items:center}}
.ess .big blockquote{{margin:0;font:600 clamp(28px,3.4vw,44px)/1.08 var(--uc-font-display);letter-spacing:-.04em;max-width:22ch}}
.ess .traits{{display:flex;flex-direction:column;gap:10px;min-width:260px}}
.ess .traits span{{display:flex;justify-content:space-between;gap:20px;border-top:1px solid var(--uc-line);padding-top:10px;font-size:15px}}
.ess .traits b{{font-weight:600}}
.ess .traits i{{font-style:normal;color:var(--uc-muted)}}
.hero-logo{{padding:90px 40px;display:flex;justify-content:center}}
.hero-logo svg{{width:min(100%,640px);height:auto}}
.ver{{margin:0;border-radius:20px;display:flex;align-items:center;justify-content:center;padding:44px 28px 54px;position:relative;min-height:190px}}
.ver img{{width:min(100%,300px);height:auto}}
.ver.v-st img{{width:auto;height:120px}}
.ver figcaption,.no figcaption{{position:absolute;left:18px;bottom:14px;font-size:12.5px;color:var(--uc-muted)}}
.v-l{{background:#fff;box-shadow:0 0 0 1px var(--uc-line)}}.v-d{{background:var(--uc-night)}}.v-d figcaption{{color:#8b88a0}}
.v-i{{background:var(--uc-indigo)}}.v-i figcaption{{color:#c7c9ff}}.v-m{{background:#eceaf8}}
.rules{{margin-top:16px;padding:36px;display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center}}
.cons{{position:relative;padding:40px}}
.cons svg{{width:100%;height:auto;overflow:visible}}
.rules ul{{margin:0;padding:0;list-style:none;display:grid;gap:14px}}
.rules li{{border-top:1px solid var(--uc-line);padding-top:12px}}
.rules li b{{display:block;font-family:var(--uc-font-display);font-size:17px;letter-spacing:-.02em}}
.rules li span{{color:var(--uc-ink-2);font-size:15px}}
.mins{{display:flex;gap:28px;align-items:flex-end;margin-top:6px}}
.mins div{{display:flex;flex-direction:column;gap:6px;font-size:12px;color:var(--uc-muted)}}
.no{{margin:0;position:relative;background:#fff;border-radius:20px;box-shadow:0 0 0 1px var(--uc-line);padding:34px 20px 50px;min-height:170px;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.no-art{{display:flex;align-items:center;justify-content:center;width:100%}}
.no img{{width:200px;height:auto}}
.no figcaption b{{color:#e11d48;margin-right:4px}}
.fake{{display:inline-flex;align-items:center;gap:10px;font:600 30px var(--uc-font-display);letter-spacing:-.02em}}
.fk-e{{width:40px;height:40px}}
.ring{{width:34px;height:34px;border-radius:50%;border:5px solid;border-color:#1FB6F2 #4F46E5 #7C3AED #4C7CF6}}
.busy{{width:100%;height:100%;min-height:110px;border-radius:12px;display:flex;align-items:center;justify-content:center;background:repeating-linear-gradient(45deg,#1FB6F2 0 14px,#ffb547 14px 28px,#7C3AED 28px 42px)}}
.busy img{{width:180px}}
.sym{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.sym .card{{padding:40px}}
.dayd{{width:100%;max-width:440px;display:block;margin:0 auto}}
.dd-n{{font:600 12px var(--uc-font-display);fill:var(--uc-ink);letter-spacing:-.02em}}
.dd-s{{font:400 5.5px var(--uc-font-text);fill:var(--uc-muted)}}
.daylist{{list-style:none;margin:0;padding:0;display:grid;gap:14px}}
.daylist li{{display:grid;grid-template-columns:14px 60px 1fr;gap:12px;align-items:baseline;border-top:1px solid var(--uc-line);padding-top:12px}}
.daylist i{{width:12px;height:12px;border-radius:50%;transform:translateY(1px)}}
.daylist b{{font-variant-numeric:tabular-nums;font-weight:600}}
.daylist span{{color:var(--uc-ink-2);font-size:15px}}
.sym h3{{font-size:26px;margin-bottom:10px}}
.sym p{{color:var(--uc-ink-2);margin:0 0 22px}}
.icons{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}}
.icons img{{border-radius:22%;box-shadow:0 18px 30px -18px rgba(40,30,90,.5)}}
.icons .fv{{display:flex;gap:12px;align-items:center;background:#fff;border-radius:12px;box-shadow:0 0 0 1px var(--uc-line);padding:10px 14px;font-size:13px;color:var(--uc-ink-2)}}
.icons .fv img{{box-shadow:none;border-radius:0}}
.sw{{background:#fff;border-radius:20px;box-shadow:0 0 0 1px var(--uc-line);overflow:hidden}}
.sw .chip{{height:132px;padding:16px;display:flex;align-items:flex-end;font:600 17px var(--uc-font-display);letter-spacing:-.02em}}
.sw dl{{display:grid;grid-template-columns:auto 1fr;gap:2px 12px;margin:14px 16px 6px;font-size:13px}}
.sw dt{{color:var(--uc-muted)}}.sw dd{{margin:0;font-variant-numeric:tabular-nums}}
.sw p{{margin:0 16px 16px;font-size:13.5px;color:var(--uc-ink-2)}}
.gbar{{height:86px;border-radius:20px;margin:16px 0 8px;position:relative}}
.gnote{{display:flex;justify-content:space-between;font-size:13px;color:var(--uc-muted)}}
.blks{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}}
.blk{{border-radius:14px;padding:14px 14px 12px;display:flex;flex-direction:column;gap:4px;border-left:4px solid currentColor}}
.blk b{{font:600 15px var(--uc-font-display);letter-spacing:-.01em}}
.blk span{{font-size:11.5px;opacity:.85;font-variant-numeric:tabular-nums}}
.blk em{{font-style:normal;font-size:11.5px;font-weight:600}}
.sub{{font:600 20px var(--uc-font-display);letter-spacing:-.025em;margin:44px 0 6px}}
.subp{{color:var(--uc-ink-2);margin:0 0 18px;max-width:70ch}}
.typo .card{{padding:36px}}
.spec-a{{font:600 120px/1 var(--uc-font-display);letter-spacing:-.035em}}
.spec-b{{font:400 120px/1 var(--uc-font-text)}}
.spec-c{{font:400 120px/1 var(--uc-font-accent);font-style:italic;color:var(--uc-indigo)}}
.typo h3{{font-size:20px;margin-top:22px}}
.typo p{{margin:6px 0 0;color:var(--uc-ink-2);font-size:15px}}
.scale{{margin-top:16px;padding:12px 36px}}
.scale div{{display:grid;grid-template-columns:180px 1fr;gap:20px;align-items:baseline;border-top:1px solid var(--uc-line);padding:18px 0}}
.scale div:first-child{{border-top:0}}
.scale small{{font-size:12.5px;color:var(--uc-muted);line-height:1.5}}
.t-d{{font:600 76px/1 var(--uc-font-display);letter-spacing:-.035em}}
.t-h2{{font:600 48px/1.02 var(--uc-font-display);letter-spacing:-.03em}}
.t-h3{{font:600 24px/1.2 var(--uc-font-display);letter-spacing:-.025em}}
.t-l{{font:400 20px/1.5 var(--uc-font-text);color:var(--uc-ink-2)}}
.t-b{{font:400 16px/1.6 var(--uc-font-text)}}
.t-e{{font:600 12px var(--uc-font-text);letter-spacing:.08em;text-transform:uppercase;color:var(--uc-indigo)}}
.cmp-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.cmp-row .card{{padding:28px;display:flex;flex-direction:column;gap:16px}}
.cmp-row h3{{font-size:13px;font-family:var(--uc-font-text);font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--uc-muted)}}
.btns{{display:flex;gap:10px;flex-wrap:wrap}}
.btn{{display:inline-flex;align-items:center;gap:8px;border:0;border-radius:999px;padding:13px 20px;font:600 15px var(--uc-font-text);cursor:pointer}}
.b1{{background:var(--uc-ink);color:#fff}}.b2{{background:var(--uc-indigo);color:#fff}}.b3{{background:#fff;color:var(--uc-ink);box-shadow:inset 0 0 0 1px var(--uc-line)}}
.calb{{border-radius:4px;padding:10px 12px;border-left:3px solid currentColor;font-size:13px}}
.calb b{{display:block;font-weight:600;font-size:14px}}
.calb small{{opacity:.8}}
.calb.pro{{background-image:repeating-linear-gradient(135deg,transparent 0 8px,rgba(255,255,255,.55) 8px 10px)}}
.sleep{{background:var(--uc-night);color:#fff;border-radius:18px;padding:20px;display:grid;gap:10px}}
.sleep small{{color:#a7a4ba;font-size:12px}}
.sleep strong{{font:600 40px/1 var(--uc-font-display);letter-spacing:-.04em}}
.sleep .bars{{display:flex;gap:6px;align-items:flex-end;height:46px}}
.sleep .bars i{{flex:1;border-radius:4px;background:linear-gradient(#a78bfa,#4f46e5)}}
.sleep .bars i.low{{background:linear-gradient(#fda4af,#be123c)}}
.ev{{display:flex;gap:8px;flex-wrap:wrap}}
.ev span{{display:inline-flex;gap:8px;align-items:center;border-radius:999px;padding:6px 12px 6px 6px;font-size:13px;box-shadow:inset 0 0 0 1px var(--uc-line);background:#fff}}
.ev b{{width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font:700 12px var(--uc-font-display);color:#fff}}
.note{{display:flex;gap:12px;align-items:flex-start;background:rgba(255,255,255,.85);backdrop-filter:blur(12px);border-radius:18px;padding:14px;box-shadow:0 0 0 1px var(--uc-line),0 16px 30px -18px rgba(40,30,90,.35)}}
.note img{{width:38px;height:38px;border-radius:9px}}
.note b{{font-size:14px}}.note p{{margin:2px 0 0;font-size:13.5px;color:var(--uc-ink-2)}}
.voice .card{{padding:30px}}
.voice h3{{font-size:20px;margin-bottom:12px}}
.voice ul{{margin:0;padding:0;list-style:none;display:grid;gap:10px}}
.voice li{{border-top:1px solid var(--uc-line);padding-top:10px;font-size:15px;color:var(--uc-ink-2)}}
.dodont{{margin-top:16px;padding:10px 30px}}
.dodont div{{display:grid;grid-template-columns:1fr 1fr;gap:30px;border-top:1px solid var(--uc-line);padding:16px 0}}
.dodont div:first-child{{border-top:0}}
.dodont span{{font-size:15px}}
.dodont .y:before{{content:"Sí · ";color:#15803d;font-weight:600}}
.dodont .x{{color:var(--uc-muted)}}.dodont .x:before{{content:"No · ";color:#e11d48;font-weight:600}}
.apps{{display:grid;grid-template-columns:1.25fr 1fr;gap:16px;align-items:start}}
.apps figure{{margin:0;border-radius:20px;overflow:hidden;box-shadow:0 0 0 1px var(--uc-line),0 24px 40px -30px rgba(40,30,90,.45);position:relative;background:#fff}}
.apps figure img{{display:block;width:100%;height:auto}}
.apps figcaption{{padding:12px 16px;font-size:13px;color:var(--uc-muted);background:#fff}}
.apps .stack{{display:grid;gap:16px}}
.sig{{padding:22px;display:flex;gap:16px;align-items:center;background:#fff}}
.apps .sig img{{width:52px;height:52px;border-radius:12px}}
.sig b{{display:block;font-size:15px}}.sig span{{display:block;font-size:13px;color:var(--uc-muted)}}
.dls{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}
.dlg{{background:#fff;border-radius:20px;box-shadow:0 0 0 1px var(--uc-line);padding:22px}}
.dlg h3{{font-size:18px;margin-bottom:10px}}
.dlg ul{{list-style:none;margin:0;padding:0}}
.dlg a{{display:flex;justify-content:space-between;gap:10px;padding:9px 0;border-top:1px solid var(--uc-line);color:var(--uc-ink);text-decoration:none;font-size:14px}}
.dlg a span{{font-size:11px;color:var(--uc-indigo);font-weight:600}}
.dlg a:hover{{color:var(--uc-indigo)}}
footer{{padding:80px 0 60px;color:var(--uc-muted);font-size:13px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}}
footer svg{{height:22px;width:auto}}
@media (max-width:980px){{.chero,.sh,.rules,.sym,.apps{{grid-template-columns:1fr}}.chero .ens{{justify-self:start;max-width:260px}}.g3,.g4,.g5,.cmp-row,.dls{{grid-template-columns:1fr 1fr}}.blks{{grid-template-columns:repeat(2,1fr)}}.ess .big{{flex-direction:column;align-items:flex-start}}.spec-a,.spec-b,.spec-c{{font-size:84px}}}}
@media (max-width:640px){{.ctop>span{{display:none}}.g2,.g3,.g4,.g5,.cmp-row,.dls{{grid-template-columns:1fr}}.scale div{{grid-template-columns:1fr;gap:6px}}.t-d{{font-size:52px}}.t-h2{{font-size:36px}}.dodont div{{grid-template-columns:1fr;gap:6px}}.hero-logo{{padding:50px 20px}}section.s{{padding-top:80px}}}}
</style>
</head>
<body>
<header class="cover">
  <div class="wrap">
    <div class="ctop">{lockup_inline("h", "#FFFFFF", "day", True, title="UrCoach")}<span>Brand kit · v1 · 20 de noviembre de 2026</span></div>
    <div class="chero">
      <div><h1>Un trazo.<br><em class="s">Un día entero.</em></h1>
      <p>La marca de UrCoach en una página: el logo y cómo usarlo, el color, la letra, la voz y las piezas listas para descargar.</p></div>
      {enso_inline("day", True)}
    </div>
    <nav class="toc" aria-label="Secciones">{toc}</nav>
  </div>
</header>
<main class="wrap">

<section class="s" id="esencia">
  <div class="sh"><div class="n">01 · Esencia</div><div><h2>Excelencia profesional, <em class="s">con energía de sobra.</em></h2>
  <p>UrCoach es un coach de IA para fundadores: cruza cómo has dormido con tu agenda y te propone un día que se sostiene. Todo lo que recomienda lleva su nivel de evidencia.</p></div></div>
  <div class="grid g3 ess">
    <div class="card big"><blockquote>Un día completo no es un día lleno.</blockquote>
      <div class="traits"><span><b>Sereno</b><i>no grita, propone</i></span><span><b>Preciso</b><i>datos tuyos, no ideales</i></span><span><b>Honesto</b><i>dice cuándo la evidencia no acompaña</i></span></div></div>
    <div class="card"><h3>Para quién</h3><p>Fundadores y equipos pequeños que ya usan IA para trabajar y viven con la agenda llena.</p></div>
    <div class="card"><h3>Qué promete</h3><p>Llegar a lo importante con la energía que tienes hoy, no con la que te gustaría tener.</p></div>
    <div class="card"><h3>Qué no es</h3><p>Ni un producto sanitario, ni un gurú de la productividad, ni una app de rachas y medallas.</p></div>
  </div>
</section>

<section class="s" id="logo">
  <div class="sh"><div class="n">02 · Logo</div><div><h2>Ensō y nombre, <em class="s">siempre juntos.</em></h2>
  <p>El isologotipo une el ensō con UrCoach en Inter Tight seminegrita. El ensō lleva el color; el nombre, siempre en una sola tinta.</p></div></div>
  <div class="card hero-logo">{lockup_inline(title="UrCoach")}</div>
  <div class="grid g3" style="margin-top:16px">{vhtml}</div>
  <div class="card rules">
    <div class="cons" id="cons"></div>
    <ul>
      <li><b>Altura</b><span>El ensō mide 1,5 veces la altura de las mayúsculas y se centra en ellas.</span></li>
      <li><b>Separación</b><span>Entre el ensō y el nombre, 0,36 veces el diámetro del ensō. Ese mismo espacio es el margen mínimo alrededor del logo.</span></li>
      <li><b>Tamaño mínimo</b><span>Horizontal, 88 px de ancho (22 mm en papel). Por debajo, solo el símbolo, hasta 16 px.</span>
        <div class="mins"><div><img src="{B}logo/urcoach-horizontal-color.svg" alt="" style="width:88px"><span>88 px</span></div><div><img src="{B}app/favicon.svg" alt="" style="width:16px"><span>16 px</span></div></div></li>
    </ul>
  </div>
  <h3 class="sub">Lo que no se hace</h3>
  <div class="grid g3">{"".join(wr)}</div>
</section>

<section class="s" id="simbolo">
  <div class="sh"><div class="n">03 · Símbolo</div><div><h2>El trazo <em class="s">es el día.</em></h2>
  <p>Un ensō es el círculo zen que se pinta de un solo gesto y no se corrige. En UrCoach recorre las 24 horas: empieza con fuerza por la mañana y se queda sin tinta por la noche. El hueco es el descanso que el plan protege.</p></div></div>
  <div class="sym">
    <div class="card">{dsvg}</div>
    <div class="card"><h3>Del cielo a la noche</h3><p>El color sigue al trazo: celeste por la mañana, índigo en el foco y violeta al cerrar el día. Los mismos colores que la mañana, el foco y el sueño en el calendario.</p>
      <ul class="daylist">{dlist}</ul>
      <h3 style="margin-top:34px">Como icono</h3><p>El icono de la app y el favicon usan una versión con más cuerpo para leerse a 16 px.</p>
      <div class="icons"><img src="{B}app/icon-192.png" alt="Icono claro" width="84" height="84"><img src="{B}app/app-icon-oscuro-1024.png" alt="Icono oscuro" width="84" height="84">
        <span class="fv"><img src="{B}app/favicon-32.png" alt="" width="32" height="32"><img src="{B}app/favicon-16.png" alt="" width="16" height="16">Favicon 32 y 16</span></div>
    </div>
  </div>
</section>

<section class="s" id="color">
  <div class="sh"><div class="n">04 · Color</div><div><h2>Mucha luz, <em class="s">un acento.</em></h2>
  <p>La base es clara: papel, tinta y un único color de acción, el índigo del foco. El degradado del día se reserva al ensō, a la segunda línea del titular de portada y a acentos finos (un borde, una línea de tiempo, un halo de luz difuso); nunca va en botones ni en texto corrido.</p></div></div>
  <div class="grid g5">{core}</div>
  <h3 class="sub">El degradado del día</h3>
  <p class="subp">Interpolado en OKLab para que no se ensucie al pasar de celeste a violeta. Hay una versión más clara para fondos oscuros.</p>
  <div class="gbar" style="background:{gradient_bar(K.DAY_LIGHT)}"></div>
  <div class="gbar" style="background:{gradient_bar(K.DAY_DARK)};height:54px;margin-top:0"></div>
  <div class="gnote"><span>07:00 · mañana</span><span>foco</span><span>22:00 · noche</span></div>
  <div class="grid g5" style="margin-top:16px">{day}</div>
  <h3 class="sub">El código de color del calendario</h3>
  <p class="subp">Cada tipo de bloque tiene su fondo y su texto. La cifra es el contraste del texto sobre su fondo (AA pide 4,5:1).</p>
  <div class="blks">{blocks()}</div>
</section>

<section class="s typo" id="tipografia">
  <div class="sh"><div class="n">05 · Tipografía</div><div><h2>Tres voces, <em class="s">una familia.</em></h2>
  <p>Inter Tight para titulares y el logo, Inter para leer y la Instrument Serif cursiva como firma: una sola expresión por titular, nunca en el texto corrido.</p></div></div>
  <div class="grid g3">
    <div class="card"><div class="spec-a">Aa</div><h3>Inter Tight</h3><p>Titulares, cifras grandes y el logo. Seminegrita 600, espaciado entre −2 y −3,5 %.</p></div>
    <div class="card"><div class="spec-b">Aa</div><h3>Inter</h3><p>Texto, interfaz y datos, con cifras tabulares. Regular 400 y medium 500.</p></div>
    <div class="card"><div class="spec-c">Aa</div><h3>Instrument Serif</h3><p>La segunda línea de un titular, en cursiva e índigo. El toque humano.</p></div>
  </div>
  <div class="card scale">
    <div><small>Portada<br>Inter Tight 600 · 76/1 · −3,5 %</small><span class="t-d">El mismo día.</span></div>
    <div><small>Titular de sección<br>Inter Tight 600 · 48/1,02 · −3 %</small><span class="t-h2">Un coach que sabe <em class="s">cuándo callarse.</em></span></div>
    <div><small>Subtítulo<br>Inter Tight 600 · 24/1,2</small><span class="t-h3">Tu sí antes de cada bloque</span></div>
    <div><small>Entradilla<br>Inter 400 · 20/1,5</small><span class="t-l">Cada mañana, UrCoach cruza tu noche con tu agenda y te propone el plan.</span></div>
    <div><small>Texto<br>Inter 400 · 16/1,6</small><span class="t-b">La intensidad del plan sale de la media de tus últimas 3 noches: una mala noche pesa un tercio, no decide sola.</span></div>
    <div><small>Etiqueta<br>Inter 600 · 12 · +8 %</small><span class="t-e">Cómo funciona</span></div>
  </div>
  <p class="subp" style="margin-top:16px">Las tres son de Google Fonts con licencia SIL Open Font License: libres para la web, la app y los documentos.</p>
</section>

<section class="s" id="componentes">
  <div class="sh"><div class="n">06 · Componentes</div><div><h2>Las piezas <em class="s">del producto.</em></h2>
  <p>Botones en píldora, bloques de calendario con su color, datos del cuerpo sobre noche y la evidencia siempre visible.</p></div></div>
  <div class="cmp-row">
    <div class="card"><h3>Botones</h3><div class="btns"><button class="btn b1">Quiero una plaza</button><button class="btn b2">Aceptar el plan</button><button class="btn b3">Ver cómo funciona</button></div></div>
    <div class="card"><h3>Bloques del calendario</h3>
      <div class="calb" style="background:var(--uc-foco);color:var(--uc-foco-t);border-left-color:#a5b4fc"><b>Foco · 60 min</b><small>12:30 a 13:30 · el único bloque en índigo sólido</small></div>
      <div class="calb pro" style="background:var(--uc-descanso);color:var(--uc-descanso-t)"><b>Descanso</b><small>Propuesto por UrCoach · 14:00</small></div>
      <div class="calb" style="background:var(--uc-reunion);color:var(--uc-reunion-t)"><b>Reunión con inversores</b><small>10:00 a 11:00</small></div></div>
    <div class="card"><h3>Datos del cuerpo</h3><div class="sleep"><small>Anoche · tu wearable</small><strong>6 h 05</strong><small>Tercera noche corta · media 5 h 40</small>
      <div class="bars"><i style="height:92%"></i><i style="height:98%"></i><i style="height:88%"></i><i style="height:90%"></i><i class="low" style="height:65%"></i><i class="low" style="height:69%"></i><i class="low" style="height:75%"></i></div></div></div>
    <div class="card"><h3>Nivel de evidencia</h3><div class="ev"><span><b style="background:#15803d">A</b>Recomendable</span><span><b style="background:#4f46e5">B</b>Opcional</span><span><b style="background:#b45309">C</b>Experimental</span><span><b style="background:#be123c">D</b>No la recomendamos</span></div></div>
    <div class="card"><h3>Aviso</h3><div class="note"><img src="{B}app/icon-192.png" alt=""><div><b>UrCoach</b><p>Empieza la desconexión: luz tenue, nada de trabajo y 20 minutos de lectura.</p></div></div></div>
    <div class="card"><h3>Radios y sombras</h3><p style="margin:0;color:var(--uc-ink-2);font-size:15px">Tarjetas 24 px, piezas internas 16 px, bloques del calendario 4 px, botones en píldora. Sombras largas y suaves teñidas de índigo, nunca negras.</p></div>
  </div>
</section>

<section class="s voice" id="voz">
  <div class="sh"><div class="n">07 · Voz</div><div><h2>Habla como un buen coach: <em class="s">poco y claro.</em></h2>
  <p>De tú, en frases cortas, con datos tuyos y sin prometer lo que la evidencia no respalda.</p></div></div>
  <div class="grid g3">
    <div class="card"><h3>Siempre</h3><ul><li>Tus datos frente a una meta clara, sin juicios.</li><li>Una acción concreta, con hora.</li><li>La fuente en una línea si la pides.</li><li>«Hoy no» es una respuesta válida.</li></ul></div>
    <div class="card"><h3>Nunca</h3><ul><li>Diagnósticos ni lenguaje médico.</li><li>Culpa, rachas ni medallas.</li><li>Cifras de salud en los avisos.</li><li>Promesas de rendimiento garantizado.</li></ul></div>
    <div class="card"><h3>Tono</h3><ul><li>Sereno, como quien ha dormido bien.</li><li>Directo: primero la acción, luego el porqué.</li><li>Cálido sin ser blando.</li><li>Una sola exclamación al mes, como mucho.</li></ul></div>
  </div>
  <div class="card dodont">
    <div><span class="y">Dormiste 6 h 05, tu tercera noche corta. Hoy, foco de 60 minutos y entreno suave.</span><span class="x">¡Vaya noche! Tu cuerpo está en modo supervivencia, hay que darlo todo.</span></div>
    <div><span class="y">La ducha caliente por la noche tiene buena evidencia (A). Los baños de hielo, poca (C).</span><span class="x">Los baños de hielo multiplican tu testosterona y tu foco.</span></div>
    <div><span class="y">¿Lo movemos a mañana a las 08:30?</span><span class="x">Has fallado tu bloque de foco. Racha perdida.</span></div>
  </div>
</section>

<section class="s" id="aplicaciones">
  <div class="sh"><div class="n">08 · Aplicaciones</div><div><h2>Listo para <em class="s">salir a la calle.</em></h2>
  <p>La imagen para compartir la web, el banner de LinkedIn, el avatar y la firma de correo.</p></div></div>
  <div class="apps">
    <figure><img src="{B}social/og-image-1200x630.png" alt="Imagen para compartir de UrCoach"><figcaption>Imagen para compartir · 1200 × 630</figcaption></figure>
    <div class="stack">
      <figure><img src="{B}social/linkedin-banner-1584x396.png" alt="Banner de LinkedIn de UrCoach"><figcaption>Banner de LinkedIn · 1584 × 396</figcaption></figure>
      <figure style="display:grid;grid-template-columns:auto 1fr;align-items:center"><img src="{B}social/avatar-400.png" alt="Avatar" style="width:120px;margin:16px;border-radius:24px"><figcaption>Avatar · 400 × 400. El icono oscuro funciona como foto de perfil en LinkedIn, X y GitHub.</figcaption></figure>
      <figure><div class="sig"><img src="{B}app/icon-192.png" alt=""><div><b>Nombre Apellido</b><span>Fundador · UrCoach</span><span>Coach de IA de energía y foco para fundadores</span></div></div><figcaption>Firma de correo</figcaption></figure>
    </div>
  </div>
</section>

<section class="s" id="descargas">
  <div class="sh"><div class="n">09 · Descargas</div><div><h2>Todo, <em class="s">en un sitio.</em></h2>
  <p>Los archivos están en marca/brand-kit/. Los SVG son la fuente; los PNG, para donde no se acepte SVG.</p></div></div>
  <div class="dls">{dl}</div>
</section>
</main>
<div class="wrap"><footer>{lockup_inline("h", K.INK, "day", False)}<span>UrCoach · Nombre de trabajo, pendiente de comprobar en EUIPO y OEPM · Brand kit v1</span></footer></div>
<script>
// Construcción: el logo con sus medidas, dibujado a partir del SVG principal
fetch("{B}logo/urcoach-horizontal-color.svg").then(r=>r.text()).then(t=>{{
  const box=document.getElementById("cons"); box.innerHTML=t; const s=box.querySelector("svg");
  const vb=s.viewBox.baseVal; const g=document.createElementNS("http://www.w3.org/2000/svg","g");
  const D=150, gap=.36*D, x0=vb.x, y0=vb.y, h=vb.height, w=vb.width;
  const L=(x1,y1,x2,y2,c="#e11d48",dash="")=>`<line x1="${{x1}}" y1="${{y1}}" x2="${{x2}}" y2="${{y2}}" stroke="${{c}}" stroke-width="1.6" ${{dash?'stroke-dasharray="6 5"':''}}/>`;
  const R=(x,y,ww,hh)=>`<rect x="${{x}}" y="${{y}}" width="${{ww}}" height="${{hh}}" fill="#4f46e5" fill-opacity=".08" stroke="#4f46e5" stroke-opacity=".5" stroke-dasharray="6 5" stroke-width="1.4"/>`;
  g.innerHTML = R(x0-gap,y0-gap,w+2*gap,h+2*gap) + L(x0-60,-100,x0+w+60,-100,"#4f46e5",1) + L(x0-60,0,x0+w+60,0,"#4f46e5",1)
    + L(x0+D,40,x0+D+gap,40) + L(x0+D,28,x0+D,52) + L(x0+D+gap,28,x0+D+gap,52) + `<text x="${{x0+D+gap/2}}" y="84" text-anchor="middle" font-size="30" fill="#e11d48" font-family="Inter">0,36 D</text>`
    + `<text x="${{x0+w+70}}" y="-40" font-size="30" fill="#4f46e5" font-family="Inter">mayúsculas</text>`;
  s.setAttribute("viewBox", `${{x0-gap-10}} ${{y0-gap-10}} ${{w+2*gap+240}} ${{h+2*gap+60}}`); s.removeAttribute("width"); s.removeAttribute("height"); s.appendChild(g);
}}).catch(()=>{{}});
</script>
</body>
</html>
'''
    return html


if __name__ == "__main__":
    html = build()
    for i, s in enumerate(re.findall(r"<svg\b.*?</svg>", html, flags=re.S)):
        ET.fromstring(s)
    assert "—" not in html, "guion largo"
    K.GUIDE.write_text(html, encoding="utf-8")
    print("Escrito", K.GUIDE, len(html) // 1024, "KB")
