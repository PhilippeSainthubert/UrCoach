---
kind: qa-report
target: 05-privacidad-regulacion.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 9.8
score_before_fix: 0.0
score_limited_by: hallazgos
coverage_claims: 115
coverage_verified: 115
independent: true
sources: 84
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 05 · Privacidad y regulación

## Nota: 0.0 / 10 · REHACER (antes de corregir; tras las correcciones, 9.8 · CORREGIR ANTES DE ENTREGAR por regla de crítica resuelta, ver «Re-verificación»)

La nota la limitan los hallazgos; la cobertura es completa (techo 10). Penalización de 10 puntos: 1 crítica (3), 4 medias (4) y 12 bajas (3). La crítica es una fecha de entrada en vigor mal puesta, de un día; no cambia ninguna recomendación, pero las reglas del encargo la clasifican como crítica porque es una fecha de una norma y es falsa. Lo demás es muy sólido: el Reglamento 2026/1744 existe con el número, la fecha y el calendario que da el informe, y casi todas las afirmaciones sobre normas coinciden con el texto oficial.

```
python3 nota.py --claims 115 --verificadas 115 --portantes 96 --portantes-ok 96 --criticas 1 --medias 4 --bajas 12 --bloqueos 0
Nota QA: 0.0 / 10 · REHACER
Techo por cobertura 10.0 · Penalización 10.0 = 3 x 1 crítica + 4 medias + 0.25 x 12 bajas
```

**Modo**: Deep · **Tipo**: research regulatorio · **Fecha**: 2026-11-19
**Independencia**: verificador en contexto separado ✓. No vio el informe ni el mapa y contestó 115 preguntas neutras (101 ALTA, 14 MEDIA). Usó el texto oficial del DOUE en la Oficina de Publicaciones (`publications.europa.eu/resource/celex/…`) y el BOE consolidado.
**Método**: Chain of Verification (`qa/C-mapa.md`, `qa/C-preguntas.md`, `qa/C-respuestas.md`). `searches: 0` se refiere a esta fase de comparación.
**Rúbricas y voz**: no hay rúbrica ni guía de voz de Ucoach; solo las reglas absolutas.

## Cobertura

| | |
|---|---|
| Afirmaciones verificables estimadas en el documento | unas 200-210 |
| C = máx(25 del preflight, 115 extraídas) | 115 |
| Verificadas con fuente consultada (incluidas las refutadas) | 115 (100 %) |
| Portantes verificadas | 96 de 96 (85 con texto oficial o primario) |
| Apoyo verificadas | 19 de 19 |

| Clase | ids |
|---|---|
| VERIFIED | 01 (cifra), 02-13, 15-21, 23-41, 43-54, 56-60, 62-65, 67, 68, 70-73, 75-85, 87-115 |
| DISCREPANCY | 22 (entrada en vigor del EEDS), 51 (regla 11), 61 (fecha del veredicto Flo) |
| OVERCLAIM | 14 (EIPD "obligatoria"), 42 ("dicen expresamente"), 69 (botón "se aplica") |
| STALE | 55 (política de software de la FDA), 66 (Nueva York), 74 (Digital Fairness Act) |
| PROVENANCE | 86 (Perlentaucher, secundaria) y etiquetas `verified` con fuente secundaria |
| MISSING | RD 1907/1996 y el rendimiento; normas no analizadas |
| INTERNAL | art. 50 y art. 111.4; "motor de reglas" frente al motor que aprende del informe 03 |

## Veredicto

**REHACER** (`MAJOR ISSUES`) antes de corregir, porque hay una crítica sin resolver. Se resuelve cambiando una fecha en dos líneas. Las cuatro medias tampoco cambian las recomendaciones, pero sí su base: la EIPD no es "obligatoria" por la lista de la AEPD, la directiva del botón no "se aplica" en España sin transponer, la Digital Fairness Act ya está propuesta y el RD 1907/1996 puede alcanzar al mensaje de "rendimiento" que recomienda el informe 03.

Lo que yo esperaba que fallara aguanta: el Reglamento (UE) 2026/1744 existe, de 8-07-2026, publicado el 24-07-2026 y en vigor el 27-07-2026, con el art. 4 rebajado, el art. 4 bis, el régimen de pymes y pequeñas de mediana capitalización, el Anexo III al 2-12-2027 y el Anexo I al 2-08-2028. La Ley 10/2025 existe con la fecha, el BOE y el art. 97.1.p citados. La guía de la FDA de 6-01-2026 existe y dice lo que dice el informe.

## Bloqueos deterministas

Ninguno. Los dos enlaces de la AEPD que marcó el preflight (URLError) dan 200 con curl: falsos positivos. Los 403 y 429 (DLA Piper, Bird & Bird, MDCG, help.openai.com) son bloqueos de bot; el verificador abrió DLA Piper y el MDCG.

## Contrato de escritura y voz

- **Script de-slop**: no disponible; las pruebas contables no se han comprobado.
- **Guiones largos**: 0 (grep sobre U+2014 y U+2013).
- **Primera persona**: el informe usa "no he verificado" y "no encontré" (l. 168, 171, 183, 185). Es útil porque declara un límite; se deja.

## Hallazgos por gravedad

### Crítica

**H-C1 · DISCREPANCY · crítica · El Reglamento del EEDS entró en vigor el 25-03-2025, no el 26-03-2025**
- **Dice**: "En vigor 26-03-2025" (l. 37); "Publicado en el DOUE el 5-03-2025 y en vigor desde el 26-03-2025" (l. 89).
- **Verificación independiente** (C05-22, https://publications.europa.eu/resource/celex/32025R0327): Reglamento (UE) 2025/327, de 11-02-2025, publicado en el DOUE el 05-03-2025, en vigor a los veinte días, el **25-03-2025**. Aplicación general desde el 26-03-2027 (art. 105).
- **Por qué es crítica**: es una fecha de una norma y es falsa. No cambia ninguna decisión de Ucoach (las fechas que importan, 2027, 2029 y 2031, son correctas).
- **Corrección**: "25-03-2025" en las l. 37 y 89, con `verified` y la URL del texto oficial.

### Medias

**H-M1 · OVERCLAIM · media · La lista de la AEPD no hace la EIPD "obligatoria"**
- **Dice**: "una evaluación de impacto obligatoria (cumple dos o más criterios de la lista de la AEPD de 2019)" (l. 21); "La EIPD es obligatoria" (l. 79).
- **Verificación independiente** (C05-14, https://www.aepd.es/documento/listas-dpia-es-35-4.pdf): la EIPD es necesaria "en la mayoría de los casos" con dos o más de los 11 criterios, y la certeza aumenta con más criterios. Entre ellos está la observación sistemática, también con apps.
- **Corrección**: "Ucoach Pro cumple al menos cinco criterios de la lista de la AEPD (categorías especiales, perfilado, observación sistemática con apps, combinación de fuentes y tecnologías nuevas). Con dos o más, la AEPD considera necesaria la EIPD en la mayoría de los casos: hay que hacerla". La decisión no cambia.

**H-M2 · OVERCLAIM · media · La directiva del botón de desistimiento no "se aplica" en España sin transponer**
- **Dice**: "desde el 19-06-2026 se aplica la directiva que exige un 'botón de desistimiento'" (l. 26), `verified`; el estado de noviembre, sin verificar (l. 181).
- **Verificación independiente** (C05-68 y C05-69, https://publications.europa.eu/resource/celex/32023L2673 y https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555): la directiva añade el art. 11 bis a la Directiva 2011/83, con transposición hasta el 19-12-2025 y aplicación de las medidas nacionales desde el 19-06-2026. El TRLGDCU consolidado a 04-11-2026 no la recoge. Hay carta de emplazamiento a España y a otros 20 Estados (30-01-2026, secundaria, https://elderecho.com/bruselas-expedienta-a-espana-por-no-transponer-la-directiva-sobre-servicios-financieros-a-distancia).
- **Corrección**: "La Directiva 2023/2673 obliga a los Estados a exigir el botón desde el 19-06-2026, pero a 04-11-2026 España no la ha transpuesto (hay procedimiento de infracción). Conviene implementarlo igualmente: llegará, y es buena práctica".

**H-M3 · STALE · media · La Digital Fairness Act ya está propuesta**
- **Dice**: "La Comisión la anunció … No he verificado si ya hay propuesta" (l. 185); también en la lista para el abogado (l. 349).
- **Verificación independiente** (C05-74, https://commission.europa.eu/news-and-media/news/making-your-online-experience-fairer-2026-11-11_en): la Comisión la presentó el 11-11-2026. Cubre patrones oscuros, diseño adictivo con opción de desactivarlo, cancelación fácil de suscripciones, renovaciones automáticas no deseadas y pruebas gratuitas trampa. El número COM no está verificado.
- **Corrección**: actualizar la l. 185. Es una propuesta, no una ley, pero afecta de lleno al Pro (suscripción) y a las rachas y los avisos del informe 03.

**H-M4 · MISSING · media · El RD 1907/1996 alcanza a "rendimiento" e "insomnio", no solo a las prácticas complementarias**
- **Dice**: el RD 1907/1996 "es relevante si se añaden prácticas como el grounding, suplementos u osteopatía" (l. 271, 351).
- **Verificación independiente** (C05-92, https://www.boe.es/buscar/act.php?id=BOE-A-1996-18085): el art. 4 prohíbe en 16 supuestos la publicidad de productos o métodos con pretendida finalidad sanitaria. Entre ellos: los que se presentan como útiles para tratar el insomnio, los que dicen potenciar el rendimiento físico o psíquico y los que sugieren sustituir la consulta de profesionales sanitarios.
- **Por qué importa**: el informe 03 recomienda vender "rendimiento" ("Llega a la negociación de mañana con energía", l. 230 del 03) y menciona el insomnio.
- **Corrección**: ampliar la l. 271 con esos supuestos, añadir una fila a la tabla de la sección 4 y un punto ⚖️: confirmar si un método de hábitos de sueño y energía entra en el ámbito del RD.

### Bajas

| id | clase | Dice (línea) | Verificación independiente | Corrección |
|---|---|---|---|---|
| H-B1 | DISCREPANCY | RGPD "En vigor desde 25-05-2018" (l. 34) | "será aplicable a partir del 25 de mayo de 2018" (art. 99.2; C05-01, https://publications.europa.eu/resource/celex/32016R0679) | "Aplicable desde 25-05-2018" |
| H-B2 | INTERNAL | Omnibus: no retrasa el art. 50 (l. 22) y solo cambia el 50.7 (l. 113), pero el 50.2 tiene plazo hasta 2-12-2026 (l. 104) | Las dos cosas son ciertas: el art. 50 se aplica desde 2-08-2026 y el Omnibus solo sustituye el 50.7; el plazo transitorio del 50.2 está en el nuevo art. 111.4 (C05-28, 29, 39, https://publications.europa.eu/resource/celex/32026R1744) | Citar el art. 111.4 en l. 22, 104 y 113 |
| H-B3 | OVERCLAIM | "Las directrices dicen expresamente que construir sobre el modelo de otro no traslada la obligación" (l. 118) | Las directrices C(2026) 5054 definen proveedor por el art. 3.3 (quien desarrolla o encarga y comercializa con su nombre); lo de construir sobre otro modelo es inferencia (C05-42, https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-07/guidelines_on_the_implementation_of_the_transparency_obligations_for_certain_ai_systems_under_article_50_of_the_ai_act_bzptwqhk0ikg1dtlddap41psfy_131215.pdf) | "Según el art. 3.3 y las directrices, quien comercializa el sistema con su nombre es proveedor aunque use el modelo de otro" (`inferred` en ese punto) |
| H-B4 | DISCREPANCY | "El software que monitoriza procesos fisiológicos es IIa" (l. 130) | IIa, o IIb si vigila parámetros vitales cuyas variaciones supongan peligro inmediato (C05-51, https://publications.europa.eu/resource/celex/32017R0745) | Añadir el IIb |
| H-B5 | STALE | "La FDA anunció que revisará su política de software y apps móviles en el año fiscal 2026" (l. 145) | Estaba en la lista A del FY2026 pero no se publicó; sigue en la lista B del FY2027 como borrador (C05-55, https://www.fda.gov/media/195054/download) | Actualizar |
| H-B6 | DISCREPANCY | "el 4-08-2025 un jurado de California condenó a Meta" (l. 160) | Veredicto del 1-08-2025 en *Frasco v. Flo Health*; Google, Flo y Flurry llegaron a acuerdos antes (C05-61, https://lowey.com/cases/flo-health-class-action/) | "1-08-2025" |
| H-B7 | STALE | NYHIPA: "versión revisada en 2026 cuyo estado no he verificado" (l. 171) | S9269 aprobada por el Senado (3-06-2026) y la Asamblea (4-06-2026); a 19-11-2026 sin firma ni veto (C05-66, https://www.nysenate.gov/legislation/bills/2025/S9269) | Actualizar |
| H-B8 | PROVENANCE | Perlentaucher `verified` (l. 242-243) | Solo resumen secundario (C05-86, https://www.ra-plutte.de/kurzzusammenfassungen-von-buchrezensionen-abstracts-die-bgh-entscheidung-perlentaucher/) | `reported` para la sentencia; la LPI sigue `verified` |
| H-B9 | PROVENANCE | `verified` con fuente secundaria: Nevada y Connecticut en el resumen (l. 25 frente a l. 170), Grupo del Artículo 29 vía Covington (l. 57), art. 9.1 LOPDGDD "secundaria" (l. 78), directrices de definición "secundaria" (l. 115), prohibiciones `reported` (l. 124), FDA vía despachos (l. 146), guía laboral de la AEPD "secundaria" (l. 219) | El verificador abrió el texto oficial de casi todas (C05-09, 13, 40, 45, 52, 53, 81); Nevada y Connecticut, solo secundaria o con discrepancia de fechas (C05-64, 65) | Subir a `verified` con la URL oficial lo que el verificador abrió; dejar Nevada `reported` |
| H-B10 | PROVENANCE | Fuentes usadas que no están en el índice: directrices 05/2020, dictamen 05/2014, sentencia SRB, Latombe | C05-16, 19, 80, 83 con texto oficial | Añadirlas al índice; Latombe y SRB pasan a `verified` |
| H-B11 | INTERNAL (con el 03) | "Un motor de reglas escritas a mano probablemente no es un 'sistema de IA'" (l. 22, 115) | El informe 03 recomienda un motor de avisos que aprende (l. 110 y 192 del 03). Las directrices (C(2025) 5053) exigen capacidad de inferir (C05-40, https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-definition_en.pdf) | Añadir qué diseño queda fuera y qué cambia con un bandit |
| H-B12 | MISSING | Normas no analizadas | Art. 22 RGPD (perfilado: "el plan del día depende de su estado", l. 79); LSSI-CE y cookies para la web y la lista de espera; políticas de Apple HealthKit y Google Health Connect; términos de las API de Oura, Garmin y WHOOP; Reino Unido | Señalarlas como pendientes; no se pueden corregir sin fuente |

## Sólido

Verificado contra el texto oficial. Que nadie lo "arregle":
- **RGPD y LOPDGDD**: art. 2.2.c y considerando 18, considerando 78 y art. 25 (solo responsables), directrices 4/2019 v2.0, arts. 4.7, 4.15, 9.1, 9.2.a, 33, 34 y 37.1.c; art. 9.1 LOPDGDD sin la salud; art. 34 LOPDGDD sin apps de bienestar; art. 7 (14 años); arts. 87-91 (C05-02 a 06, 12, 13, 15, 17, 82, 95).
- **Jurisprudencia**: C-184/20 (1-08-2022), C-21/23 (4-10-2024, sin receta), C-683/21 (5-12-2023), C-413/23 P (4-09-2025), T-553/23 Latombe desestimado (3-09-2025) con casación C-703/25 P pendiente (C05-07, 08, 11, 16, 19).
- **CEPD y GT29**: anexo de 2015 con los tres tipos, borrador 02/2026 (7-07-2026, consulta hasta el 30-10-2026, tres criterios), dictamen conjunto 2/2026, directrices 05/2020 sobre empleados, dictamen 05/2014 (C05-09, 10, 18, 21, 80, 83).
- **Ley de IA y Omnibus**: todas las fechas del calendario (C05-25 a 32), el Reglamento 2026/1744 y su tramitación (C05-33 a 35), arts. 4, 4 bis, pymes y 50.7 (C05-36 a 39), directrices de definición y de prohibiciones (burnout en el trabajo, ap. 257), arts. 3.4, 3.39, 5.1.a, b y f, anexo III 1.c y 4.b, 50.3 (C05-40 a 47).
- **Productos sanitarios**: art. 2.12 y considerando 19 del MDR, MDCG 2019-11 rev.1 de 17-06-2025, guía de bienestar de la FDA de 6-01-2026 (sustituye a la de 2019), sección 520(o)(1)(B), Somryst y Sleepio con 510(k) (C05-48 a 50, 52 a 54, 97 a 99).
- **EE. UU.**: HBNR (26-04-2024, 30-05-2024, 29-07-2024) y su alcance; GoodRx (1,5 M$, primera), BetterHelp (7,8 M$), Premom (segunda, 100.000 $ + 100.000 $); My Health My Data Act completa; Nevada; veto de Nueva York del 19-12-2025 (C05-56 a 60, 62 a 64, 66).
- **Consumo**: 14 días y pago proporcional, art. 11 bis y sus fechas, Ley 10/2025 (26-12-2025, BOE 27-12-2025, vigor 28-12-2025, art. 97.1.p, 15 días), sin "Ley 4/2025" relevante, RDL 7/2021 (C05-67, 68, 70 a 73).
- **Proveedores de IA**: Anthropic (28-08-2025, Free, Pro y Max con Claude Code, 8-10-2025, 5 años o 30 días, exclusiones), OpenAI API (1-03-2023, 30 días, ZDR, MCP), ChatGPT de consumo y el App Security Whitepaper de junio de 2026 (C05-75 a 79).
- **Otras**: AEPD laboral (actualizada 12-2025), LPI arts. 10, 21 y 32, CRA, Directiva 2024/2853, Data Act, DSA, Ley Europea de Accesibilidad (C05-81, 84, 85, 87 a 91, 93, 94).

## No verificable

Ninguna afirmación entera. Subdatos sin confirmar: número COM de la Digital Fairness Act, marcado CE de Sleepio, estado procesal de Maxwell v. Amazon, marca "Miracle Morning" en la EUIPO y fecha exacta de las enmiendas al Omnibus del RGPD.

## Falta

- RD 1907/1996 aplicado al mensaje de rendimiento e insomnio (H-M4).
- Art. 22 RGPD, LSSI-CE y cookies, políticas de HealthKit y Health Connect, términos de las API de wearables, Reino Unido (H-B12).
- Plazo de 12 meses de la disposición transitoria de la Ley 10/2025 para adaptar los servicios de atención a la clientela (C05-70), útil para el plan Pro.

## Correcciones a aplicar (línea a línea)

1. **l. 21**: EIPD (H-M1).
2. **l. 22**: art. 111.4 (H-B2); diseño del motor (H-B11).
3. **l. 25**: Nevada y Connecticut `reported` (H-B9).
4. **l. 26**: botón de desistimiento (H-M2).
5. **l. 34**: "Aplicable desde" (H-B1).
6. **l. 37 y 89**: 25-03-2025 (H-C1).
7. **l. 38**: estado de la transposición a 04-11-2026 (H-M2).
8. **l. 57, 78, 115, 124, 146, 219**: etiquetas con la URL oficial (H-B9).
9. **l. 79**: EIPD (H-M1).
10. **l. 81, 84**: Latombe y SRB `verified` (H-B10).
11. **l. 104, 113**: art. 111.4 (H-B2).
12. **l. 115, 120**: qué diseño queda fuera de la definición de sistema de IA (H-B11).
13. **l. 118**: art. 3.3 (H-B3).
14. **l. 130**: regla 11 con IIb (H-B4).
15. **l. 145**: FDA FY2026-FY2027 (H-B5).
16. **l. 160**: Flo, 1-08-2025 (H-B6).
17. **l. 171**: S9269 (H-B7).
18. **l. 179-181**: transposición e infracción (H-M2).
19. **l. 185**: Digital Fairness Act (H-M3).
20. **l. 242-243**: Perlentaucher `reported` (H-B8).
21. **l. 271 y sección 4**: RD 1907/1996 (H-M4).
22. **l. 349-351**: lista para el abogado: quitar Latombe (resuelto), actualizar la DFA y añadir el RD 1907/1996 y las normas pendientes (H-M3, H-M4, H-B12).
23. **Índice de fuentes**: añadir las fuentes oficiales del QA.

## Re-verificación

Fecha: 2026-11-19. Las correcciones se aplicaron con Edit sobre `05-privacidad-regulacion.md`, cambiando solo las frases afectadas, citando la URL del verificador (`qa/C-respuestas.md`) y marcando cada cambio con «(corregido tras QA 2026-11-19)». Regla de etiquetas aplicada: `verified` solo si la fuente es el texto oficial o primario; lo que solo tiene fuente secundaria queda `reported`. El informe pasa de 406 a 426 líneas; las líneas nuevas son las del informe corregido.

| hallazgo | estado | línea nueva |
|---|---|---|
| H-C1 · entrada en vigor del EEDS | corregido: 25-03-2025, con el texto oficial | 37, 89 |
| H-M1 · EIPD "obligatoria" | corregido: "necesaria en la mayoría de los casos" con dos o más criterios; Ucoach Pro cumple cinco, así que hay que hacerla | 21, 79 |
| H-M2 · botón de desistimiento "se aplica" | corregido: obligación de los Estados desde 19-06-2026; sin transponer en España a 04-11-2026; procedimiento de infracción (`reported`) | 26, 38, 183-185 |
| H-M3 · Digital Fairness Act | corregido: propuesta del 11-11-2026 y su contenido | 189, 354 |
| H-M4 · RD 1907/1996 y "rendimiento" | corregido: supuestos del art. 4 (insomnio, rendimiento físico o psíquico); aplicación al mensaje del informe 03; fila nueva en la sección 4; punto ⚖️ | 275, 297, 357 |
| H-B1 · RGPD "en vigor" | corregido: "aplicable desde" (art. 99.2) | 34 |
| H-B2 · art. 50 y art. 111.4 | corregido con el texto oficial: solo se sustituye el 50.7; transitorio del 50.2 en el art. 111.4 | 22, 104, 113-114 |
| H-B3 · "dicen expresamente" | corregido: art. 3.3; la deducción queda `inferred` | 121 |
| H-B4 · regla 11 | corregido: IIb para parámetros vitales | 133 |
| H-B5 · política de software de la FDA | corregido: no publicada en el FY2026; pendiente en el FY2027 | 149 |
| H-B6 · fecha del veredicto Flo | corregido: 1-08-2025, *Frasco v. Flo Health* | 164 |
| H-B7 · Nueva York | corregido: S9269 aprobada por las dos cámaras en junio de 2026, sin firma ni veto | 175 |
| H-B8 · Perlentaucher | corregido: `reported` | 247 |
| H-B9 · etiquetas `verified` con fuente secundaria | corregido: Grupo del Artículo 29, LOPDGDD, directrices de definición, de prohibiciones y del art. 50, FDA, AEPD laboral, CRA, Directiva 2024/2853, Data Act y EAA pasan a `verified` con la URL oficial; Nevada queda `reported` | 25, 57, 78, 115, 127, 150, 174, 223, 265, 270, 274, 277 |
| H-B10 · fuentes fuera del índice | corregido: fuentes 39 a 50; Latombe y SRB `verified` | 81, 84, 411-423 |
| H-B11 · motor de reglas frente a motor que aprende | corregido: qué diseño queda fuera (reglas fijas con aleatorización simple) y qué cambia con un bandit (art. 50, art. 4, sin alto riesgo en bienestar) | 22, 116 |
| H-B12 · normas no analizadas | **no corregido**: se listan como pendientes (art. 22 RGPD, LSSI-CE y cookies, HealthKit y Health Connect, API de wearables, Reino Unido) pero no se analizan, porque no hay fuente verificada | 355 |

Otros cambios: la nota de método (l. 13) indica qué puntos se verificaron después del QA y que solo sigue sin verificar el estado procesal de Maxwell v. Amazon. Guiones largos: 0.

**Nota antes de corregir**: 0.0 / 10 (REHACER, `MAJOR ISSUES`). Penalización de 10: 1 crítica, 4 medias y 12 bajas.

**Nota tras corregir** (solo lo abierto: 0 críticas, 0 medias, 1 baja, 0 bloqueos):

```
python3 nota.py --claims 115 --verificadas 115 --portantes 96 --portantes-ok 96 --criticas 0 --medias 0 --bajas 1 --bloqueos 0
Nota QA: 9.8 / 10 · ENTREGABLE
Techo por cobertura 10.0 · Penalización 0.25
```

**Veredicto tras corregir: CORREGIR ANTES DE ENTREGAR** (`NEEDS REVISION`). La banda de nota.py es ENTREGABLE, pero la regla del encargo dice que una crítica resuelta deja el veredicto en CORREGIR ANTES DE ENTREGAR. La corrección es trivial (una fecha), pero el informe es regulatorio y lleva ⚖️: antes de entregarlo, alguien distinto de quien corrigió debería cotejar las líneas 37 y 89 con el texto oficial, y un abogado debería revisar los puntos ⚖️ (sobre todo el RD 1907/1996 aplicado al mensaje de rendimiento).

Lo que este 9.8 no cubre:
1. Las correcciones las ha comprobado el mismo agente que hizo la comparación, contra las respuestas del verificador. No ha habido una segunda verificación independiente del texto nuevo.
2. La cobertura es de las 115 afirmaciones extraídas, sobre unas 200-210 verificables.
3. Siguen abiertos fuera de la nota: el número COM de la Digital Fairness Act, el marcado CE de Sleepio, el estado de Maxwell v. Amazon, la marca "Miracle Morning" en la EUIPO y las normas que no se analizan (H-B12).


## Comprobación de la corrección por un tercero (sesión principal, 2026-11-19)

- La única crítica (fecha de entrada en vigor del Reglamento (UE) 2025/327) se cotejó desde la sesión principal, que no escribió el informe ni la corrección. Las líneas 37 y 89 dicen «en vigor 25-03-2025», y la respuesta C05-22 del verificador independiente da lo mismo con el texto oficial (https://publications.europa.eu/resource/celex/32025R0327): publicado en el DOUE el 05-03-2025, en vigor a los 20 días y aplicable con carácter general desde el 26-03-2027.
- Con la crítica resuelta y re-verificada por un tercero, y sin medias abiertas, el veredicto pasa a **ENTREGABLE (`PASS`)**. La nota (9.8) no cambia.
- Sigue en pie la recomendación de que un abogado revise los puntos marcados con ⚖️ antes de lanzar la versión gestionada. No es un hallazgo del QA: es el límite de un informe hecho sin asesoría jurídica.
