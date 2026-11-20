---
kind: qa-report
target: 03-retencion-conducta.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 9.1
score_before_fix: 0.0
score_limited_by: cobertura
coverage_claims: 97
coverage_verified: 74
independent: true
sources: 80
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 03 · Retención, cambio de conducta y eficacia del coaching con IA

## Nota: 0.0 / 10 · CORREGIR ANTES DE ENTREGAR (antes de corregir; tras las correcciones, 9.1 · ENTREGABLE, ver «Re-verificación»)

La nota la limitan los hallazgos, no la cobertura (el techo por cobertura es 9.14). No hay ninguna crítica. Pesan 12 medias y 22 bajas: penalización de 17,5 puntos. Casi todas se corrigen en una frase. El núcleo del informe aguanta: Baumel, Meyerowitz-Katz, Torous, JAMA 2025, Bloom, HeartSteps, Bidargaddi, Eisele, Wrzus, Singh 2024, Milkman 2021, Silverman y Barasch, Ferguson, Baron, Singh 2023 y Stanford 2025 coinciden con la fuente primaria, en la mayoría de los casos hasta el decimal.

```
python3 nota.py --claims 97 --verificadas 74 --portantes 47 --portantes-ok 46 --criticas 0 --medias 12 --bajas 22 --bloqueos 0
Nota QA: 0.0 / 10 · REHACER (banda de nota.py)
Techo por cobertura 9.14 = 10 x (0.7 x 46/47 + 0.3 x 74/97) · Penalización 17.5 = 12 medias + 0.25 x 22 bajas
```

La banda que imprime nota.py es REHACER porque la nota es 0, pero el veredicto lo fijan las reglas del encargo: sin críticas y con medias abiertas el veredicto es CORREGIR ANTES DE ENTREGAR.

**Modo**: Deep · **Tipo**: research de evidencia y producto · **Fecha**: 2026-11-19
**Independencia**: verificador en contexto separado ✓. No vio el informe ni el mapa y contestó 77 preguntas neutras (60 ALTA, 14 MEDIA, 3 BAJA).
**Método**: Chain of Verification. Extractor (`qa/C-mapa.md`, `qa/C-preguntas.md`), verificador (`qa/C-respuestas.md`) y comparación en este informe. `searches: 0` se refiere a esta fase de comparación.
**Rúbricas y voz**: no hay rúbrica ni guía de voz de Ucoach; solo se aplican las reglas absolutas (castellano de España, sin guiones largos, sin fechas relativas).

## Cobertura

| | |
|---|---|
| Afirmaciones verificables estimadas en el documento | unas 170-180 |
| C = máx(97 del preflight, 77 extraídas) | 97 |
| Verificadas con fuente consultada (incluidas las refutadas) | 74 (76 %) |
| Portantes verificadas | 46 de 47 (C03-05 sin fuente abierta) |
| Apoyo verificadas | 28 de 30 (C03-65 y C03-72 sin fuente abierta) |

| Clase | ids |
|---|---|
| VERIFIED | 01, 02, 08-14, 16-19, 21, 24-26, 28 (cifras), 30-42, 44, 46-49, 51-53, 55-63, 68, 69, 71, 74-76 |
| DISCREPANCY | 03 (año), 04, 07, 11 (URL), 15, 20, 23, 27, 29, 50, 64, 67, 73 |
| ERROR | 22, 66 |
| STALE | 70, 77 |
| PROVENANCE | 43, 45 (sin estudio identificable) |
| OVERCLAIM | 06 (metodología), micro-aleatorización (rec. 3) |
| UNVERIFIABLE | 05, 54, 65, 72 |
| INTERNAL / MISSING | ver Hallazgos (media frente a mediana, Freeman 30-49 %, cruces con el informe 05) |

## Veredicto

**CORREGIR ANTES DE ENTREGAR** (`NEEDS REVISION`). No hay ninguna crítica: ningún dato falso cambia una recomendación. Pero hay doce medias abiertas. Las más importantes son de coherencia con el informe 05: el motor de avisos que aprende, los umbrales para "detectar" burnout o insomnio y los experimentos con los 20 usuarios sin consentimiento. Hay además dos errores de hecho (la probabilidad de envío en los micro-ensayos y Slip Buddy, que no es un chatbot) y una cifra sin estudio identificable (registro de calorías).

## Bloqueos deterministas

Ninguno. El preflight marcó 4 enlaces con 403 (Business of Apps, GlobeNewswire, JAMA y Fast Company); son bloqueos de bot, no enlaces muertos. Para GlobeNewswire el verificador usó otra URL de la misma nota (H-B22).

## Contrato de escritura y voz

- **Script de-slop**: no disponible en esta máquina; las pruebas contables no se han comprobado.
- **Guiones largos**: 0 (comprobado con grep sobre U+2014 y U+2013).
- **Fechas relativas**: "hoy" en la l. 160 ("no tiene, hoy, ventaja demostrada"). Se cambia al corregir.

## Hallazgos por gravedad

### Críticas

Ninguna.

### Medias

**H-M1 · INTERNAL · media · "Una media de unos dos meses" es la mediana**
- **Dice**: "Un hábito necesita una media de unos dos meses, no una semana. La mediana para automatizar un hábito es de 59 a 66 días y la media de 106 a 154 días" (l. 20).
- **Verificación independiente** (C03-28, https://pubmed.ncbi.nlm.nih.gov/39685110/): 20 estudios y 2.601 participantes; medianas de 59-66 días, medias de 106-154 días, rango de 4-335.
- **Corrección**: "Un hábito tarda una mediana de unos dos meses (la media es de tres a cinco), no una semana". Añadir que, con 8-10 semanas, la mitad de los usuarios aún no habrá automatizado el hábito, y por eso hay que medir la automaticidad antes de cambiarlo.

**H-M2 · DISCREPANCY · media · Las cifras de Adjust no son las de salud y forma física**
- **Dice**: "Salud y forma física (Adjust) | ~27 % | ~13 % | ~8 %" (l. 39); "un 8 % según Adjust" (l. 65); "D30 del 3-8 %" (l. 16, 54).
- **Verificación independiente** (C03-04, https://www.adjust.com/blog/get-the-mobile-app-retention-benchmarks-for-2023/ y https://www.adjust.com/blog/what-makes-a-good-retention-rate/): con datos de 2022, salud y forma física D1 24 %, D14 9 %, D30 7 %; en 2024, D1 27 %. El 13 % de D7 es la media de todas las categorías y no hay D7 de la categoría.
- **Corrección**: fila de Adjust: "D1 24 % (2022) o 27 % (2024); D7 no publicado; D30 7 % (2022)", `verified`. l. 65: "un 7 % según Adjust". l. 16 y 54: "3-7 %".

**H-M3 · DISCREPANCY · media · El efecto de HeartSteps desaparece hacia la semana 4, no "durante las 6 semanas"**
- **Dice**: "el efecto fue cayendo durante las 6 semanas" (l. 17); "Los efectos de los avisos se apagan entre la semana 4 y la 6" (l. 56).
- **Verificación independiente** (C03-20, https://pmc.ncbi.nlm.nih.gov/articles/PMC6401341/): cualquier sugerencia, +66 % el día 1 con una caída del 2 % diario, indistinguible de cero hacia el día 28; sugerencias de caminar, +107 % con una caída del 3 % diario, indetectables hacia el día 29. Los participantes decían que se aburrían a las 2-4 semanas.
- **Corrección**: l. 17: "y el efecto cayó cada día hasta dejar de detectarse hacia el día 28-29". l. 56: "se apagan hacia la semana 4". La conclusión (validación corta) sale reforzada.

**H-M4 · ERROR · media · Los micro-ensayos no envían "menos de la mitad de las veces"**
- **Dice**: "Las pruebas con efecto usan entre 1 y 5 puntos de decisión al día y envían de media menos de la mitad de las veces" (l. 90).
- **Verificación independiente** (C03-22, https://pmc.ncbi.nlm.nih.gov/articles/PMC6401341/ y https://pubmed.ncbi.nlm.nih.gov/30497999/): HeartSteps enviaba con probabilidad 0,6 en cada punto disponible; Bidargaddi, 0,5.
- **Corrección**: "…y en cada uno envían con una probabilidad de 0,5 a 0,6. En HeartSteps eso da como mucho unas 3 sugerencias al día". El presupuesto de 1-3 avisos sigue en pie y queda mejor justificado.

**H-M5 · PROVENANCE · media · La encuesta de Sifted citada no es la que se pudo comprobar**
- **Dice**: "más de la mitad de los fundadores dicen haber sufrido burnout en el último año (Sifted, 2025)" (l. 23); "54 % (n≈138); 75 % ansiedad; 46 %…; 49 % se planteó dejar su startup" (l. 146).
- **Verificación independiente** (C03-43, https://thefinanser.com/2024/03/half-of-start-up-founders-are-ready-to-quit, secundaria; Sifted bloqueada): la encuesta de 2024 (n=156) da 53 % de burnout, 75 % de ansiedad, 45 % de salud mental mala o muy mala, 61 % ha pensado en dejar su empresa y 49 % lo considera para el año siguiente. Las cifras de 2025 solo aparecen en agregadores, con muestras contradictorias.
- **Corrección**: citar la encuesta de 2024 con sus cifras, `reported` (fuente secundaria), y marcar la de 2025 como no verificada. "Más de la mitad" se mantiene.

**H-M6 · PROVENANCE · media · La caída del registro de calorías del 68 % al 21 % no tiene estudio identificable**
- **Dice**: "68 % registra de forma constante en la semana 1 | 21 % en la semana 12" (l. 48); "El registro constante de calorías cae del 68 % en la semana 1 al 21 % en la 12" (l. 158). Sostiene la recomendación 10 (sueño pasivo).
- **Verificación independiente** (C03-45, https://pubmed.ncbi.nlm.nih.gov/22545978/ y https://doi.org/10.2196/64139): no aparece esa serie. Krukowski et al. (2013): programa web de 6 meses, 161 participantes; de media se registró el 28 % de los días laborables y el 17 % de los fines de semana, con la mayoría de registros al principio. Una revisión de JMIR mHealth (2026) recoge que con MyFitnessPal el autorregistro baja de 5,4 a 1,4 días por semana entre las semanas 4 y 12.
- **Corrección**: sustituir el 68 %→21 % por esas dos cifras, con sus fuentes. La recomendación se mantiene.

**H-M7 · ERROR · media · Slip Buddy no es un chatbot**
- **Dice**: "En el piloto Slip Buddy, una app de estilo chatbot y una app de calorías se usaron en una proporción de días parecida" (l. 160).
- **Verificación independiente** (C03-66, https://pubmed.ncbi.nlm.nih.gov/33792547/): Slip Buddy es una app para registrar deslices dietéticos y su contexto, no un chatbot (Pagoto et al., JMIR mHealth 2021, n=64). Uso del 53,8 % frente al 57,5 % de los días, sin diferencia.
- **Corrección**: quitar Slip Buddy como evidencia sobre el registro conversacional. La frase "No se encontró ningún ensayo que compare registrar en un chat con hacerlo en un formulario" queda sola, y la conclusión ("debe medirse") no cambia.

**H-M8 · STALE · media · Sí hay datos públicos de retención de Oura**
- **Dice**: "Wearables de pago (Oura, WHOOP) | No hay datos públicos de cohortes" (l. 50); también l. 68 y 237.
- **Verificación independiente** (C03-77, https://www.sec.gov/Archives/edgar/data/2133022/000119312526396051/d119865ds1a.htm): el S-1/A de Oura (21-09-2026) da una retención media ponderada de miembros de pago a 12 meses de aproximadamente el 85 % a 30-06-2026 (cohortes mensuales, con reactivaciones) y una ratio DAU/MAU del 65 %. De WHOOP no hay datos.
- **Corrección**: rellenar la fila de Oura con esas cifras y la advertencia de que son suscriptores de pago con hardware, no comparables con instalaciones gratuitas.

**H-M9 · INTERNAL (con el informe 05) · media · El "motor de avisos que aprende" cambia la clasificación de la Ley de IA**
- **Dice**: "un motor de avisos que aprende (como el aprendizaje por refuerzo del programa de diabetes)" (l. 110); micro-aleatorización que retira los tipos de aviso sin efecto (l. 192).
- **Verificación independiente** (C05-40, https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-definition_en.pdf): las directrices de la Comisión excluyen los sistemas basados en reglas definidas solo por personas; la capacidad de inferir es "a key, indispensable condition". El informe 05 concluye que Ucoach queda fuera porque su motor es de reglas fijas.
- **Corrección**: distinguir dos diseños. Reglas fijas más aleatorización simple con probabilidad constante, revisadas por una persona: no infiere y queda fuera de la definición. Un bandit o aprendizaje por refuerzo que ajusta solo los envíos: probablemente es un sistema de IA; en ese caso aplica la transparencia del art. 50 si interactúa con el usuario, sin riesgo alto mientras la finalidad sea el bienestar.

**H-M10 · INTERNAL (con el informe 05) · media · Umbrales para "detectar" burnout clínico o insomnio**
- **Dice**: "Derivación explícita ante señales de burnout clínico, ánimo bajo persistente (por ejemplo, ánimo de 2 o menos durante 7 días o más) o insomnio persistente" (l. 231); "derivar a terapia cognitivo-conductual para el insomnio" (l. 124, 207).
- **Verificación independiente**: la guía de bienestar de la FDA excluye las "references to specific diseases, clinical conditions, or diagnostic thresholds" (C05-53, https://www.fda.gov/media/90652/download); el MDR define la finalidad por el etiquetado y las declaraciones (C05-48, https://publications.europa.eu/resource/celex/32017R0745); el RD 1907/1996 prohíbe publicidad sobre el insomnio con pretendida finalidad sanitaria (C05-92, https://www.boe.es/buscar/act.php?id=BOE-A-1996-18085). El informe 05 pone "detecta el burnout" e "insomnio como algo que Ucoach mide" en la lista de palabras a evitar.
- **Corrección**: reformular como señales de bienestar que derivan a un profesional, sin nombrar trastornos ni presentar el umbral como diagnóstico: "si tu ánimo lleva una semana bajo o te cuesta dormir de forma habitual, puede ser útil hablarlo con un profesional".

**H-M11 · MISSING (con el informe 05) · media · Los experimentos con los 20 usuarios no prevén consentimiento**
- **Dice**: micro-aleatorización con 20 usuarios y 8 semanas (l. 192), experimentos n-de-1 (l. 212), métricas de validación por persona (l. 216-226). No se menciona el consentimiento.
- **Verificación independiente** (C05-12 y C05-13, https://publications.europa.eu/resource/celex/32016R0679 y https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673): los datos de sueño y ánimo son de salud; el art. 9.2.a exige consentimiento explícito para fines especificados, y en España basta para la salud.
- **Corrección**: añadir a la P1 y a la P5: consentimiento explícito por escrito, hoja informativa, recoger solo lo mínimo (lo que el usuario elige compartir), plazo de borrado y registro de actividades, como pide la P0 del informe 05.

**H-M12 · OVERCLAIM · media · Veinte usuarios no bastan para "saber qué tipos de aviso funcionan"**
- **Dice**: "Con 20 usuarios y 8 semanas habrá miles de decisiones, suficientes para saber qué tipos de aviso funcionan" (l. 192).
- **Verificación independiente** (C03-19, https://pubmed.ncbi.nlm.nih.gov/30192907/): HeartSteps, con 44 inscritos (37 analizados) y 6 semanas, no alcanzó significación para el efecto global (p=0,06); solo las sugerencias de caminar (p=0,02).
- **Corrección**: "…suficientes para detectar efectos grandes y descartar tipos claramente inútiles, no para medir efectos pequeños".

### Bajas

| id | clase | Dice (línea) | Verificación independiente | Corrección |
|---|---|---|---|---|
| H-B1 | DISCREPANCY | Braze: "Año del dato 2026" (l. 38) | 2026 es la fecha de la compilación; el año de los datos no se indica (C03-03, https://www.braze.com/resources/articles/mobile-app-retention) | "2026 (compilación; año de los datos no indicado)" |
| H-B2 | OVERCLAIM | "La retención digital empeoró en 2023" (l. 66) | Mixpanel amplió el alcance del informe de 2024; no se puede descartar un efecto de muestra (C03-06, https://mixpanel.com/wp-content/uploads/2024/01/2024_Benchmarks_Report.pdf) | Añadir esa advertencia |
| H-B3 | DISCREPANCY | Semana 8: "6-20 % … (dato antiguo)", fuente Mixpanel 2024 (l. 41) | El 6-20 % es del informe de 2017; el de 2019 dice "below 20 percent" (C03-07, https://mixpanel.com/blog/whats-a-good-retention-rate/) | Atribuir a Mixpanel 2017 y 2019 |
| H-B4 | DISCREPANCY | Therabot "N=210, 8 semanas"; −51 %, −31 %, −19 % `verified` (l. 46, 103) | Intervención de 4 semanas con seguimiento a las 8; el resumen da tamaños de efecto (d=0,85-0,90 en depresión), no esos porcentajes, que salen del comunicado (C03-15, https://pubmed.ncbi.nlm.nih.gov/42932588/) | "4 semanas de uso y seguimiento a 8"; porcentajes `reported` (comunicado) y d del artículo |
| H-B5 | DISCREPANCY | Bidargaddi: "Efecto algo menguante, sin significación" (l. 80) | El efecto sí fue significativo (RR 1,039, IC 1,01-1,08); lo no significativo fue la atenuación (P=0,84) (C03-23, https://pubmed.ncbi.nlm.nih.gov/30497999/) | Reescribir con esa distinción |
| H-B6 | DISCREPANCY | JITAI "se define por cinco elementos" (l. 72) | Cuatro componentes clave (puntos de decisión, opciones, variables de ajuste, reglas) y seis elementos con los resultados proximal y distal (C03-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5364076/) | Corregir y subir a `verified` |
| H-B7 | DISCREPANCY | "solo el 23 % llegó al umbral en el estudio principal" (l. 133) | El 23 % es de Keller et al. (alimentación sana); la revisión no habla de "estudio principal" (C03-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC11641623/) | "en el estudio de Keller et al." |
| H-B8 | DISCREPANCY | HeartSteps: "silenciar 1, 2, 4 u 8 horas" (l. 79) | "apagar la intervención hasta 12 horas" (C03-50, https://arxiv.org/html/1812.10800) | Corregir; el `snooze` de Ucoach (l. 190) es decisión de producto y puede quedarse |
| H-B9 | UNVERIFIABLE | "el 46,5 % del grupo IA habría preferido un coach humano" (l. 102) | No se encontró; el análisis secundario no lo dice (C03-54, https://api.crossref.org/works/10.2196/92981) | Quitar la cifra |
| H-B10 | INTERNAL | "30-49 % de fundadores con algún trastorno" (l. 111); "72 %" (l. 145) | 49 % frente a 32 % de controles; el 30 % es la depresión. El 72 % suma 49 % de antecedentes propios y 23 % de familiares, en controles el 48 %, y los autores lo llaman "highly preliminary" (C03-44 y C03-61, https://ideas.repec.org/a/kap/sbusec/v53y2019i2d10.1007_s11187-018-0059-8.html y https://www.michaelafreemanmd.com/documents/are-entrepreneurs-touched-with-fire-pre-pub-n-4-17-15.pdf) | Corregir las dos líneas y subir Freeman a `verified` |
| H-B11 | DISCREPANCY | Bertelsmann: "41 % duerme 6 horas o menos y 71 % sufre burnout" (l. 149) | "5-6 h o menos"; burnout "al menos varias veces al año"; n=50 no representativa (C03-64, https://www.indianpharmapost.com/healthcare/bii-spotlights-founder-wellness-in-startup-ecosystem-at-its-8th-badminton-championship-21056) | Corregir |
| H-B12 | DISCREPANCY | "SleepCoacher (Daskalova et al., 2016) y Self-E (2020) … autoexperimentos guiados de sueño" (l. 166) | Self-E es de CHI 2021 y no es específico de sueño (C03-67, https://jeffhuang.com/papers/SleepCoacher_UIST16.pdf) | Corregir |
| H-B13 | STALE | "No se pudo verificar … el cierre de la app de consumo de Woebot en 2025" (l. 241) | Cerró el 30-06-2025; el motivo no está verificado (C03-70, https://hlth.com/insights/news/woebot-health-is-shutting-down-its-app-2025-04-28) | Dar la fecha; el motivo, sin verificar |
| H-B14 | DISCREPANCY | "Mixpanel recomienda medir la retención semanal o mensual en B2B" (l. 49) | Usa retención a una semana y semanal, sin recomendar formalmente; no hay benchmarks por categoría de productividad (C03-73, https://mixpanel.com/blog/b2b-benchmarks-2026/) | Corregir |
| H-B15 | INTERNAL | "En ensayos, el abandono es del 40-48 %" (l. 67) frente a "26-48 %" (l. 16, 55) | Torous: 26,2 % bruto y 47,8 % corregido; Meyerowitz-Katz: 40 % en ensayos (C03-08, C03-09) | Unificar en "26-48 %" |
| H-B16 | PROVENANCE | "El plazo es corto (`verified`)" (l. 56), una inferencia; Startup Snapshot parte 2 `verified` vía blog (l. 148) | | `inferred` en l. 56; "verified (vía blog de Brad Feld)" en l. 148 |
| H-B17 | OVERCLAIM | "un 40 % a las 4 semanas multiplicaría por cinco o por diez el benchmark" (l. 54) | 40/3 ≈ 13, y D30 y activo semanal no son la misma métrica (l. 29) | "lo multiplicaría varias veces, aunque las métricas no son equivalentes" |
| H-B18 | PROVENANCE | SRBAI, ±30 del NPS y prueba de Sean Ellis sin fuente (l. 222, 224) | SRBAI: Gardner et al. 2012, 4 ítems, escala 1-7 (https://pubmed.ncbi.nlm.nih.gov/22935297/); NPS con n=20: ±28-44 (https://www.tlfresearch.com/news-opinion/what-is-your-nps-margin-of-error/); Ellis: ≥40 % "muy decepcionado" (https://learningloop.io/plays/product-market-fit-survey) | Citar las tres; NPS "±30-40 puntos" |
| H-B19 | INTERNAL | "inicio: 93,4 %" en la columna D1 (l. 45) | Es la tasa de inicio del programa | Moverlo a la última columna |
| H-B20 | MISSING | Avisos y "hoy no" por Telegram (l. 190) sin tener en cuenta el contenido | El informe 05 pide avisos sin cifras de salud (l. 74, 307) | Añadir "sin datos de salud en el texto" |
| H-B21 | MISSING | Todos los benchmarks son de apps de tienda o de ensayos | No hay benchmark de herramientas que viven dentro de un asistente de IA (MCP o CLI) | Señalarlo en huecos; no se puede corregir con fuente |
| H-B22 | PROVENANCE | Fuente 7, nota de Endeavour del 19-08-2014 (l. 255), 403 en el preflight | La nota consultada es del 15-08-2014 (C03-11, https://rss.globenewswire.com/news-release/2014/08/15/1060135/0/en/Endeavour-Partners-Consumer-Behavior-Study-Points-to-Uncertain-Future-of-Wearable-Devices.html) | Sustituir la URL y subir a `verified` |

## Sólido

Verificado de forma independiente y correcto. Que nadie lo "arregle":
- **Retención**: Baumel 2019, D15 3,9 % y D30 3,3 % (medianas), 93 apps, DAU 4,0 % y subtipos (C03-01, 02, 48, 49). Braze 3,9 % iOS y 3,4 % Android (C03-03). Mixpanel semana 1 del 50 % al 28 % (C03-06). Meyerowitz-Katz 43/49/40 % (C03-08). Torous 26,2 % y 47,8 %, con menos abandono con feedback humano y registro del ánimo (C03-09, 10). Endeavour, un tercio en 6 meses (C03-11).
- **Coaching con IA**: JAMA 2025 completo: N=368, 31,7 % frente a 31,9 %, inicio 93,4 % frente a 82,7 %, finalización 63,9 % frente a 50,3 %, aprendizaje por refuerzo sin LLM, publicado el 27-10-2025 (C03-12 a 14, 74). Bloom: N=54, 4 semanas, sin ventaja del LLM en actividad y mejoras en creencias, disfrute y autocompasión (C03-17, 18). Therabot: supervisión humana y "no generative AI agent is ready to operate fully autonomously" (C03-16). Singh 2023, todos los SMD (C03-37, 57). PH-LLM (C03-56). Revisión JMIR 2026, 14 de 43 (C03-53). Metaanálisis de Digital Health 2025, SMD 0,20 (C03-52).
- **Avisos**: HeartSteps, +14 % (p=0,06), +66 %, +107 % y sin efecto contra el sedentarismo (C03-19 a 21). Bidargaddi, 1.255 usuarios, RR 1,039 (C03-23, 60). Eisele y Wrzus (C03-24, 25, 59). Stawarz: los recordatorios frenan la automaticidad y las señales por eventos la favorecen (C03-26).
- **Hábitos y técnicas**: Singh 2024, medianas y medias (C03-28). Judah 2013 (C03-30). Milkman 2021: 61.293 personas, 54 intervenciones, 45 % eficaces, la mejor premiaba volver tras faltar, 8 % con efecto después y expertos sin capacidad de predicción (C03-31 a 33). Silverman y Barasch (C03-34). Michie 2009 (C03-38). Gollwitzer y Sheeran d=0,65 (C03-39). Sheeran 2024, 642 pruebas, d=0,27 y 0,15 con RoBMA (C03-40). Fresh start y el ensayo de 2017 sin efecto (C03-41). Temptation bundling (C03-68, 69).
- **Autoseguimiento**: Ferguson 2022 (C03-35, 58). Baron 2017, serie de 3 casos (C03-36). Precisión de wearables de sueño (C03-76).
- **Fundadores**: Stanford y Miles 2025, 58 % y n=90 (C03-42). Startup Snapshot 2023 y 2025 (C03-62, 63).

## No verificable

- **C03-05**: AppsFlyer 3 % a 30 días (2023) vía Business of Apps, que bloquea el acceso. Es redundante con Braze (verificado), así que se marca "no verificado".
- **C03-65**: Fast Company, CEO con coach por fase (403).
- **C03-72**: razones de abandono de Endeavour; no aparecen en lo que se pudo abrir.
- **Subdatos**: año de los datos de Braze, encuesta de Sifted 2025, motivo del cierre de Woebot y el 46,5 % de preferencia por el coach humano (H-B9).

## Falta

- Benchmarks de retención de herramientas dentro de un asistente de IA (MCP, CLI), el comparador más cercano a Ucoach (H-B21).
- Una estimación del efecto de observación de la cohorte guiada (Hawthorne).
- Evidencia sobre el canal de los avisos (Telegram frente a push nativo).
- Compromiso social, Epstein, Mehrotra y Künzler, que el propio informe declara sin revisar.

## Correcciones a aplicar (línea a línea)

1. **l. 16**: "3 % y 8 %" → "3 % y 7 %"; ajustar la cita de Sifted.
2. **l. 17**: decaimiento hasta el día 28-29 (H-M3).
3. **l. 20**: media → mediana (H-M1).
4. **l. 23**: Sifted 2024, `reported` (H-M5).
5. **l. 38-41**: Braze (H-B1), Adjust (H-M2), AppsFlyer "no verificado" (C03-05), Mixpanel semana 8 (H-B3).
6. **l. 45, 46**: mover "inicio" (H-B19); Therabot 4+8 semanas (H-B4).
7. **l. 48**: registro de calorías (H-M6).
8. **l. 49, 50**: Mixpanel B2B (H-B14); Oura (H-M8).
9. **l. 54, 56**: comparación de métricas (H-B17); semana 4 e `inferred` (H-M3, H-B16).
10. **l. 66, 67, 68**: advertencia de Mixpanel (H-B2); 26-48 % (H-B15); Oura (H-M8).
11. **l. 72, 79, 80**: JITAI (H-B6); silenciar 12 h (H-B8); Bidargaddi (H-B5).
12. **l. 90**: probabilidad de envío (H-M4).
13. **l. 102, 103**: quitar el 46,5 % (H-B9); Therabot (H-B4).
14. **l. 110, 111**: motor de avisos (H-M9); Freeman (H-B10).
15. **l. 124**: ortosomnia sin diagnosticar (H-M10).
16. **l. 133, 144-146, 148, 149**: Keller (H-B7); Freeman (H-B10); Sifted (H-M5); etiqueta (H-B16); Bertelsmann (H-B11).
17. **l. 158, 160, 166**: calorías (H-M6); Slip Buddy y "hoy" (H-M7); Self-E (H-B12).
18. **l. 190, 192**: Telegram (H-B20); diseño fijo o bandit, potencia y consentimiento (H-M9, H-M11, H-M12).
19. **l. 207, 212**: señales de bienestar (H-M10); consentimiento en `experimento` (H-M11).
20. **l. 222, 224**: fuentes de SRBAI, NPS y Ellis (H-B18); añadir una fila de consentimiento a la tabla de métricas (H-M11).
21. **l. 231**: derivación sin umbral diagnóstico (H-M10).
22. **l. 237-241**: Oura, B2B sin benchmark de asistentes (H-B21), Freeman verificado, Woebot (H-B13).
23. **l. 255**: URL de Endeavour (H-B22). Índice: añadir las fuentes nuevas del QA.
24. **Etiquetas**: subir a `verified`, con la URL del verificador, Stawarz, Nahum-Shani, Michie, Gollwitzer y Sheeran, Sheeran 2024, Dai 2014, Milkman 2014, Kirgios 2020 y Freeman.

## Re-verificación

Fecha: 2026-11-19. Las correcciones se aplicaron con Edit sobre `03-retencion-conducta.md`, cambiando solo las frases afectadas, citando la URL del verificador (`qa/C-respuestas.md`) y marcando cada cambio con «(corregido tras QA 2026-11-19)». El informe pasa de 306 a 324 líneas; las líneas nuevas son las del informe corregido.

| hallazgo | estado | línea nueva |
|---|---|---|
| H-M1 · media frente a mediana | corregido: "mediana de unos dos meses (y una media de tres a cinco)"; aviso de que a las 8-10 semanas cerca de la mitad aún no ha automatizado | 20 |
| H-M2 · Adjust | corregido: D1 24 %/27 %, D7 sin dato de categoría, D30 7 %; rango "3-7 %" | 16, 39, 55, 66 |
| H-M3 · decaimiento de HeartSteps | corregido: indetectable hacia el día 28-29 | 17, 57, 79 |
| H-M4 · "menos de la mitad" | corregido: probabilidad de envío 0,5-0,6; como mucho unas 3 sugerencias al día | 91 |
| H-M5 · Sifted | corregido: encuesta de 2024 (n=156, secundaria); 2025 sin verificar | 23, 148 |
| H-M6 · registro de calorías | corregido: Krukowski 2013 y revisión JMIR mHealth 2026 en lugar del 68 %→21 % | 48, 160 |
| H-M7 · Slip Buddy | corregido: retirado como evidencia de registro conversacional | 162, 309 |
| H-M8 · Oura | corregido: retención a 12 meses (~85 %) y DAU/MAU del S-1/A, con advertencia de comparabilidad | 50, 69, 240 |
| H-M9 · motor que aprende frente a Ley de IA | corregido: reglas fijas con aleatorización simple (fuera) frente a bandit (art. 50, sin alto riesgo en bienestar); la rec. 3 adopta el diseño fijo | 112, 194 |
| H-M10 · umbrales de burnout e insomnio | corregido: señales de bienestar que derivan a un profesional, sin nombrar trastornos ni diagnosticar | 126, 209, 234 |
| H-M11 · consentimiento de los 20 usuarios | corregido: consentimiento explícito, hoja informativa, minimización, borrado; nueva fila de métricas | 194, 214, 229 |
| H-M12 · potencia de la micro-aleatorización | corregido: "detectar efectos grandes y descartar tipos claramente inútiles" | 194 |
| H-B1 · año de Braze | corregido | 38 |
| H-B2 · metodología de Mixpanel | corregido | 67 |
| H-B3 · semana 8 de Mixpanel | corregido: informes de 2017 y 2019 | 41 |
| H-B4 · Therabot | corregido: 4 semanas + seguimiento a 8; tamaños de efecto y porcentajes del comunicado | 19, 46, 104 |
| H-B5 · Bidargaddi | corregido | 81 |
| H-B6 · JITAI | corregido: cuatro componentes clave y seis elementos | 73 |
| H-B7 · 23 % de Keller | corregido | 135 |
| H-B8 · silenciar hasta 12 h | corregido | 80 |
| H-B9 · 46,5 % | corregido: retirado | 103, 274 |
| H-B10 · Freeman 30-49 % y 72 % | corregido: 49 % frente a 32 %; 72 % preliminar, con antecedentes familiares y 48 % en controles | 113, 146, 147 |
| H-B11 · Bertelsmann | corregido | 151 |
| H-B12 · Self-E | corregido | 168 |
| H-B13 · Woebot | corregido: cierre el 30-06-2025, motivo sin verificar | 244 |
| H-B14 · Mixpanel B2B | corregido | 49 |
| H-B15 · 26-48 % frente a 40-48 % | corregido | 68 |
| H-B16 · etiquetas | corregido: `inferred` en el plazo; Startup Snapshot "vía el blog de Brad Feld" | 57, 150 |
| H-B17 · comparación D30 frente a semana activa | corregido | 55 |
| H-B18 · SRBAI, NPS y Ellis sin fuente | corregido: Gardner 2012, TLF Research, learningloop | 224, 226 |
| H-B19 · "inicio" en la columna D1 | corregido | 45 |
| H-B20 · Telegram | corregido: avisos sin datos de salud | 192 |
| H-B21 · benchmark de herramientas dentro de un asistente | **no corregido**: no hay fuente; se señala como hueco | 241 |
| H-B22 · URL de Endeavour | corregido | 44, 258 |

Otros cambios de la misma pasada:
- Subidas a `verified` con la URL del verificador: Stawarz (88, 269), Nahum-Shani (266), Michie (132, 166, 296), Gollwitzer y Sheeran (133, 292, 293), Dai y el ensayo de 2017 (138, 294), Milkman 2014 y Kirgios (139, 295), Freeman (146, 300), Digital Health 2025 y JMIR 2026 (101, 102, 278).
- C03-05 (AppsFlyer 3 %, Business of Apps) queda marcado "no verificado" (l. 40); el rango se apoya en Braze y Adjust, verificados.
- Índice: fuentes 41 a 52 añadidas como «Añadidas tras el QA del 2026-11-19».
- Guiones largos: 0. "hoy" en la l. 162 cambiado por "a noviembre de 2026".

**Nota antes de corregir**: 0.0 / 10 (CORREGIR ANTES DE ENTREGAR). Penalización de 17,5: 12 medias y 22 bajas.

**Nota tras corregir** (solo lo abierto: 0 críticas, 0 medias, 1 baja, 0 bloqueos):

```
python3 nota.py --claims 97 --verificadas 74 --portantes 47 --portantes-ok 46 --criticas 0 --medias 0 --bajas 1 --bloqueos 0
Nota QA: 9.1 / 10 · ENTREGABLE
Techo por cobertura 9.14 = 10 x (0.7 x 46/47 + 0.3 x 74/97) · Penalización 0.25
```

**Veredicto tras corregir: ENTREGABLE** (`PASS`). No hay críticas ni medias abiertas. La única portante sin fuente abierta (C03-05) se ha marcado "no verificado" y ya no sostiene nada. La nota la limita la cobertura, no los hallazgos: C son las 97 afirmaciones del preflight y se verificaron 74.

Lo que este 9.1 no cubre:
1. Las correcciones las ha comprobado el mismo agente que hizo la comparación, contra las respuestas del verificador. No ha habido una segunda verificación independiente del texto nuevo.
2. La cobertura es de 74 de 97 afirmaciones según el preflight, y de unas 170-180 verificables según la estimación del extractor.
3. Siguen abiertos fuera de la nota: Fast Company, las razones de abandono de Endeavour, la encuesta de Sifted de 2025 y el benchmark de herramientas dentro de un asistente de IA.
