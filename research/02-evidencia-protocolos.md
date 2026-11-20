# Ucoach · Línea 2 · Evidencia científica de las reglas y protocolos

**Fecha:** 2026-11-19
**Base:** documento de producto Ucoach v0.1 (secciones "Lógica de planificación del día", "Protocolos por área" y "Biblioteca").
**Método:** 49 búsquedas web y 9 lecturas directas de fuentes (WebFetch o PDF) para verificarlas. Se priorizan metaanálisis, revisiones sistemáticas y guías de consenso. Seis fuentes no se pudieron abrir en la primera versión porque se agotó el cupo de búsquedas o el servidor bloqueó la lectura (Liu 2022 NEJM, Garaulet 2013, EFSA 2015, Ciria 2023, Kredlow 2015 y Baron 2017); Liu, Garaulet y la EFSA no son de apoyo, sino portantes. Un verificador independiente las abrió todas en la QA y ahora van como `verified` con su enlace (corregido tras QA 2026-11-19; ver `QA-REPORT-02-evidencia-protocolos.md`).

**Marcas de confianza**
- `verified`: cifra o conclusión comprobada en la fuente primaria, su resumen oficial o la nota de prensa oficial.
- `reported`: la recogen fuentes secundarias fiables, o viene de mi conocimiento previo de la fuente, sin haberla abierto en esta sesión. Una cifra `reported` puede venir de memoria; las portantes se contrastaron en la QA independiente (corregido tras QA 2026-11-19).
- `inferred`: conclusión propia a partir de la evidencia citada.

**Veredictos:** sólido (guías de consenso o metaanálisis consistentes) · razonable (dirección correcta, cifra o encuadre mejorables) · débil (heurística sin base directa) · incorrecto o engañoso.

---

## Resumen

1. **El núcleo de sueño es sólido, pero los umbrales son demasiado rígidos y dependen de una sola noche.** La meta de 7 a 9 horas coincide con AASM/SRS (2015) y NSF (2015). Ucoach debería usar la media de 3 a 7 noches, avisar también si se duerme más de 9 o 10 horas y añadir la **regularidad** como métrica propia: según Windred 2024, predice la mortalidad mejor que la duración (`verified`).
2. **La regla del primer café a los 75 minutos no tiene base científica.** Viene del "retraso de 90 minutos" de Huberman y ningún ensayo la respalda. Hay que quitarla o dejarla como opción personal. La del **último café antes de dormir va bien encaminada, pero 8 horas se quedan cortas**: el metaanálisis de Gardiner (2023) da **al menos 8,8 h** para un café y **al menos 13,2 h** para un preentreno (`verified`, https://pubmed.ncbi.nlm.nih.gov/36870101/). Ucoach debe usar al menos 9 h para un café y al menos 13,5 h para dosis altas (corregido tras QA 2026-11-19).
3. **La desconexión de 60 minutos sin pantallas se apoya en un argumento flojo, la luz azul.** El consenso de la NSF (2024) no llegó a acuerdo sobre si la luz de las pantallas afecta al sueño de los adultos. Importan más el contenido estimulante, el tiempo de sueño que se pierde y la **luz ambiente**: Brown et al. (2022) piden 10 lux melanópicos como máximo **desde 3 horas antes** de acostarse, no desde 1 hora.
4. **El bloque de foco de 90 minutos es una buena práctica, pero el "ciclo ultradiano de 90 minutos" de Kleitman no está demostrado en vigilia.** Y el efecto de sincronía con el cronotipo es irregular: lo encuentra menos de la mitad de los estudios en adultos jóvenes (revisión de 2025). Ucoach tiene una ventaja: puede usar los check-ins de energía del propio usuario para situar su pico en lugar de una tabla teórica.
5. **Las pausas cada 90 minutos se quedan cortas.** Los metaanálisis sobre romper el sedentarismo (2022 y 2025) muestran beneficio metabólico con 2 a 5 minutos de caminata **cada 30 minutos** o menos, en adultos con sobrepeso u obesidad (corregido tras QA 2026-11-19). La regla 20-20-20 es una heurística con evidencia escasa y contradictoria (2022-2023).
6. **"Un hábito cada vez" es sensato, pero la cadencia semanal choca con la evidencia.** Un hábito tarda una mediana de unos 2 meses en automatizarse (Lally 2010; Singh 2024). Si cada revisión semanal propone un cambio nuevo, se abandonan hábitos antes de consolidarse. Conviene mantener el foco 8 a 10 semanas o hasta que el hábito sea automático.
7. **Faltan reglas con muy buena evidencia:** la TCC-I (terapia cognitivo-conductual del insomnio) como primera línea ante el insomnio, según la AASM (2021) y la guía europea (2023); señales de alarma que obligan a derivar (apnea, somnolencia al volante, ánimo bajo persistente, dolor torácico al hacer ejercicio); la luz diurna durante toda la jornada; la regularidad de horarios de comida; el límite diario de cafeína; y una advertencia contra la obsesión por los datos del wearable.
8. **La biblioteca tiene avisos correctos, aunque algunos son vagos, y le faltan otros importantes:** Atomic Habits (la regla del 1 %), Ikigai (los datos de longevidad de las zonas azules), The Circadian Code (el ayuno con horario restringido), The Power of Full Engagement (los ciclos de 90 minutos), Peak (la práctica deliberada), Spoon-Fed (las 30 plantas), Spark y The Upside of Stress.

---

## Tabla resumen

| # | Regla de Ucoach | Veredicto | Cambio propuesto | Fuente principal |
|---|---|---|---|---|
| 1a | Dormir de 7 a 9 h | Sólido | Mantener. Avisar también si se duerme más de 9 o 10 h de forma habitual | Watson 2015 (AASM/SRS); Hirshkowitz 2015 (NSF) |
| 1b | Umbrales <6 deuda / 6-7 justo / ≥7 bien | Razonable | Usar la media de 3 a 7 noches en lugar de una sola. Añadir un nivel "largo" (>9-10 h). Combinar con la sensación subjetiva | Watson 2015; Cappuccio 2010 |
| 1c | Hora de despertar fija como ancla | Sólido | Mantener con margen de ±30-60 min. Es la pieza central de la TCC-I | AASM 2021 (insomnio); Sletten 2023 (NSF) |
| 1d | Horarios regulares, también el fin de semana | Sólido | Añadir un índice de regularidad y el jet lag social, calculados con los registros propios. Admitir recuperar sueño el fin de semana si falta entre semana | Windred 2024; Sletten 2023 |
| 2a | 10-20 min de luz exterior en la primera hora y media | Razonable | Mantener como mínimo práctico. Añadir "y toda la luz natural posible durante el día" | Brown 2022; Burns 2023 |
| 2b | Luz cálida y tenue por la noche | Sólido en lo esencial; el plazo es corto | Bajar la luz **3 h antes** de acostarse, no solo en la última hora. Dormitorio a oscuras (≤1 lux) | Brown 2022 (PLOS Biology) |
| 3a | Primer café a unos 75 min de despertar | Débil | Quitar la regla o dejarla como preferencia opcional. No presentarla como ciencia | Sin ensayos; Lovallo 2005 |
| 3b | Último café 8 h antes de dormir | Sólido en la dirección; 8 h se quedan cortas | Pasar a al menos 9 h para un café y al menos 13,5 h para dosis altas (preentreno, bebidas energéticas), por encima de los mínimos de Gardiner (8,8 h y 13,2 h). Añadir el límite de 400 mg al día (corregido tras QA 2026-11-19) | Gardiner 2023; Drake 2013; EFSA 2015 |
| 4 | Siesta de 10-20 min si se durmió <6 h | Razonable | Antes de las 15:00, con alarma. **No proponerla si hay quejas de insomnio** ni antes de conducir | Brooks y Lack 2006; Dutheil 2021 |
| 5a | Bloque de foco de 90 min (60 con deuda) | Razonable | Bloque flexible de 60 a 120 min. No justificarlo con el ciclo ultradiano | Albulescu 2022; revisión del BRAC |
| 5b | Pico de foco según cronotipo | Razonable o débil | Determinar el cronotipo con el MCTQ o el MEQ y ajustar el pico con los check-ins propios a las 2-3 semanas | Chauhan 2025 (revisión sistemática) |
| 6a | Entreno suave si hay deuda de sueño | Razonable | Matizar: no cancelar. Evitar las sesiones máximas o muy técnicas por la tarde; las de por la mañana sufren menos | Craven 2022 (Sports Medicine) |
| 6b | VFC o readiness para decidir la intensidad (implícito) | Débil o razonable | Usarlas solo como señal secundaria, con una línea base de 7 días, nunca por un dato aislado | Manresa-Rocamora 2021; Granero-Gallegos 2020; Düking 2021 (corregido tras QA 2026-11-19) |
| 7a | Pausa activa de 5 min cada 60-90 min | Razonable pero insuficiente | Micropausas de 2-3 min de pie o caminando cada 30 min aproximadamente (evidencia en adultos con sobrepeso u obesidad), más una pausa de 5-10 min cada 60-90. Sin saturar de avisos | Buffey 2022; metaanálisis 2025 sobre romper el sedentarismo |
| 7b | Regla 20-20-20 | Débil (heurística) | Dejarla como recordatorio opcional: "mira lejos y parpadea a menudo". No decir que está probada | Talens-Estarelles 2023; Johnson 2023 (corregido tras QA 2026-11-19) |
| 8a | Alerta con 2 h o más de reuniones seguidas | Razonable | Mantener. Citar el estudio de Microsoft como exploratorio (n=14) | Microsoft Human Factors Lab 2021 |
| 8b | Reuniones de 25 o 50 min | Razonable (heurística) | Mantener como norma de agenda, sin atribuirle evidencia fisiológica | Albulescu 2022 (inferred) |
| 9a | Comida de 45 min entre 13:00 y 15:30 | Razonable | Recomendar comer antes de las 15:00 cuando se pueda y mantener horarios regulares | Garaulet 2013; St-Onge 2017 (AHA) |
| 9b | Cena 2-3 h antes de dormir | Razonable | 3 h o más si hay reflujo; 2-3 h en general | Fujiwara 2005 |
| 9c | Evitar comidas copiosas antes del foco | Razonable (poca evidencia directa) | Mantener como sugerencia | inferred |
| 9d | Ayuno con horario restringido (no está en Ucoach) | No recomendar por defecto | No añadirlo como regla. Si el usuario lo pide: es seguro, pero no supera a la restricción calórica. La asociación de 2024 con la mortalidad es observacional, también en el estudio completo de 2025 (corregido tras QA 2026-11-19) | Liu 2022 (NEJM); abstract de la AHA 2024 y sus críticas |
| 10 | Desconexión de 60 min sin pantallas | Razonable con justificación débil | Hablar de "actividad tranquila y no estimulante" y no de "luz azul". Nada de trabajo, correo ni redes. Móvil fuera del dormitorio | Hartstein 2024 (consenso NSF) |
| 11 | Nada de alcohol en las 3 h previas | Razonable pero insuficiente | "Menos es mejor y cuanto antes, mejor". Incluso dosis bajas alteran el sueño REM. La OMS no fija un nivel seguro (OMS Europa, 2023: https://www.who.int/europe/news/item/04-01-2023-no-level-of-alcohol-consumption-is-safe-for-our-health; corregido tras QA 2026-11-19) | Gardiner 2025 (metaanálisis) |
| 12a | OMS: 150-300 min moderado o 75-150 vigoroso, y fuerza 2 días o más | Sólido | Mantener. Añadir "reducir el tiempo sentado" | Bull 2020 (OMS) |
| 12b | 8.000 pasos (biblioteca) | Sólido o razonable | Objetivo por defecto de 7.000 a 8.000 pasos y subir de forma gradual desde la línea base | Paluch 2022; Ding 2025 |
| 13a | Altura y distancia de la pantalla, pies, codos, etc. | Razonable (consenso, evidencia de resultados débil) | Mantener. Codos "a 90-110°". Presentarlo como comodidad, no como prevención probada del dolor | INSST; Hoe 2018 (Cochrane) |
| 13b | Alternar sentado y de pie | Razonable | Mantener. La mesa elevable reduce el tiempo sentado, pero su beneficio para la salud no está probado | Shrestha 2018 (Cochrane) |
| 14 | 20 min de lectura dentro de la desconexión, en papel o e-ink | Razonable | Mantener. Matizar que Chang 2015 usó 4 h de lectura con brillo alto | Chang 2015 (PNAS) |
| 15 | Revisión semanal con "un hábito cada vez" | Razonable pero mal calibrado | Mantener el mismo hábito de foco 8 a 10 semanas o hasta que sea automático (índice SRBAI) | Lally 2010; Singh 2024; James 2016 |

---

## Detalle por regla

### 1. Sueño

#### 1a. Objetivo de 7 a 9 horas
- **Veredicto:** sólido.
- **Evidencia:** el consenso conjunto de la AASM y la Sleep Research Society (Watson et al., 2015) recomienda dormir 7 horas o más con regularidad a los adultos de 18 a 60 años. La National Sleep Foundation (Hirshkowitz et al., 2015) recomienda 7-9 h para los adultos de 26 a 64 años y considera "puede ser adecuado" el margen de 6 a 10 h. Su revisión a diez años (*Sleep Health* 2026;12(4):599-611, 133 metaanálisis) reafirmó esos rangos: https://pubmed.ncbi.nlm.nih.gov/42248743/ (corregido tras QA 2026-11-19). Dormir poco **y** dormir mucho se asocia a más mortalidad en estudios prospectivos (metaanálisis de Cappuccio, 2010, con 1,38 millones de participantes; riesgo relativo de 1,12 para el sueño corto). El sueño largo probablemente sea en parte un marcador de enfermedad, no una causa.
- **Fuentes:**
  - Watson NF et al. 2015, *J Clin Sleep Med / Sleep*, consenso AASM/SRS. https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf `verified`
  - Hirshkowitz M et al. 2015, *Sleep Health*, NSF. https://www.sciencedaily.com/releases/2015/02/150202123716.htm `verified` (nota de prensa)
  - Cappuccio FP et al. 2010, *Sleep*, metaanálisis. https://wrap.warwick.ac.uk/5980/ y https://pubmed.ncbi.nlm.nih.gov/20469800/ `verified` en la QA (corregido tras QA 2026-11-19)
- **Cambio en Ucoach:** mantener el rango. Añadir un estado "largo" cuando la media semanal pase de 9-10 h, con el mensaje "si duermes mucho y sigues cansado, coméntalo con tu médico".

#### 1b. Umbrales <6 "deuda", 6-7 "justo", ≥7 "bien"
- **Veredicto:** razonable.
- **Evidencia:** los cortes de 6 y 7 h encajan con los consensos: menos de 6 h es "no recomendado" para la NSF y 7 h es el mínimo de la AASM. Pero clasificar el día por **una sola noche** es frágil por tres motivos. Los wearables cometen errores apreciables y fallan más en las fases: en una validación de 11 dispositivos, la concordancia de fases con la polisomnografía fue de F1 0,26 a 0,69 (corregido tras QA 2026-11-19). La necesidad de sueño varía de una persona a otra. Y la deuda se acumula a lo largo de varias noches (`inferred`). Además, "≥7 = buen día para intensidad" ignora la calidad y la regularidad del sueño.
- **Fuentes:** Watson 2015 y Hirshkowitz 2015 (arriba). Validaciones de wearables frente a polisomnografía (Lee et al., JMIR mHealth 2023): https://mhealth.jmir.org/2023/1/e50983 y https://pubmed.ncbi.nlm.nih.gov/37917155/ `verified` en la QA
- **Cambio en Ucoach:**
  - Calcular el estado con una media ponderada de 3 noches (la última pesa más) y la media de 7 días.
  - Cruzarlo con el check-in de energía de la mañana: si el usuario dice 4-5/5 tras 6,3 h, no tratarlo como deuda.
  - Redactarlo así: "Sueño corto en los últimos días" en lugar de "Deuda" tras una sola mala noche.

#### 1c. La hora de despertar fija como ancla
- **Veredicto:** sólido.
- **Evidencia:** fijar la hora de levantarse es un componente central de la TCC-I (control de estímulos y restricción del sueño), que la AASM recomienda como tratamiento de primera línea (guía de 2021, recomendación fuerte). Esa evidencia es en insomnio crónico; para la población general, la base es el consenso de la NSF (corregido tras QA 2026-11-19). El consenso de la NSF sobre regularidad (Sletten et al., 2023, 63 publicaciones y Delphi en dos rondas) concluye que la regularidad de las horas de acostarse y de levantarse es importante para la salud, la seguridad y el rendimiento. La luz por la mañana, más fácil de conseguir con una hora fija, adelanta el reloj interno (Wright 2013, ver la regla 2).
- **Fuentes:**
  - Edinger JD et al. 2021, *J Clin Sleep Med*, guía AASM sobre tratamientos conductuales del insomnio. https://aasm.org/new-guideline-supports-behavioral-psychological-treatments-for-insomnia/ `verified`
  - Sletten TL et al. 2023, *Sleep Health*, consenso de la NSF sobre regularidad. https://pubmed.ncbi.nlm.nih.gov/37684151/ `verified` (resumen)
- **Cambio en Ucoach:** mantener. Concretar un margen de **±30 a 60 min**, también en fin de semana. Tras una noche corta, permitir como mucho 1 h más de cama por la mañana en lugar de un ancla absoluta.

#### 1d. Regularidad del sueño y jet lag social
- **Veredicto:** sólido (evidencia observacional fuerte y consenso de expertos).
- **Evidencia:** Windred et al. (2024, *Sleep*) calcularon el *Sleep Regularity Index* (SRI) con acelerómetros de 60.977 participantes del UK Biobank. Una regularidad mayor se asoció a entre un 20 % y un 48 % menos de mortalidad por cualquier causa, y la regularidad predijo la mortalidad **mejor que la duración**. Es un estudio observacional en una población poco diversa (de unos 63 años de media), así que no demuestra causalidad. Sobre el jet lag social, un metaanálisis de 2024 en *Obesity Reviews* (en línea en diciembre de 2023; corregido tras QA 2026-11-19) (Arab, Garaulet, Scheer y otros) encontró una asociación pequeña pero consistente con el IMC (r ≈ 0,12; OR ≈ 1,20 de sobrepeso u obesidad). La NSF (2023) matiza que recuperar sueño el fin de semana **puede ser beneficioso** si falta entre semana.
- **Fuentes:**
  - Windred DP et al. 2024, *Sleep* 47(1), doi:10.1093/sleep/zsad253. https://researchnow.flinders.edu.au/en/publications/sleep-regularity-is-a-stronger-predictor-of-mortality-risk-than-s/ `verified` (resumen)
  - Arab A et al. 2024, *Obesity Reviews* 25(3):e13664, jet lag social y obesidad. https://pubmed.ncbi.nlm.nih.gov/38072635 `verified` en la QA (corregido tras QA 2026-11-19)
  - Sletten 2023 (arriba).
- **Cambio en Ucoach:**
  - Añadir a la revisión semanal dos métricas sencillas: la desviación estándar de la hora de levantarse (objetivo: menos de 30-45 min) y el jet lag social (diferencia entre el punto medio del sueño en días libres y en días laborables; objetivo: menos de 1 h).
  - Con 7 o más noches registradas, mostrar un SRI aproximado.
  - Cambiar "también el fin de semana" por "también el fin de semana, aunque puedes dormir algo más si entre semana te ha faltado sueño".

### 2. Luz

#### 2a. 10 a 20 minutos de luz exterior en la primera hora y media
- **Veredicto:** razonable.
- **Evidencia:** el consenso de Brown et al. (2022, *PLOS Biology*) pide **al menos 250 lux melanópicos (mEDI) a la altura de los ojos durante todo el día**, no solo por la mañana. La luz exterior, incluso nublada, supera con mucho la de interior: las normas fijan una iluminancia interior al menos diez veces menor que la luz natural exterior (Brown 2022; corregido tras QA 2026-11-19). Tras una semana de camping solo con luz natural, el reloj circadiano se adelantó unas 2 horas (Wright et al., 2013). En 86.772 participantes del UK Biobank, más luz de día y menos de noche se asociaron a menos depresión, TEPT y autolesiones (Burns et al., 2023, *Nature Mental Health*; estudio transversal). La cifra de "10-20 min" es una heurística práctica que ningún ensayo ha fijado como dosis (`inferred`).
- **Fuentes:**
  - Brown TM et al. 2022, *PLOS Biology* 20(3):e3001571. https://pmc.ncbi.nlm.nih.gov/articles/PMC8929548 `verified`
  - Wright KP et al. 2013, *Current Biology* 23:1554-1558. https://www.sciencealert.com/how-a-week-of-camping-resets-the-body-clock `reported`
  - Burns AC et al. 2023, *Nature Mental Health*, doi:10.1038/s44220-023-00135-8. https://www.nationalelfservice.net/mental-health/depression/associations-between-daily-light-exposure-and-psychiatric-disorders/ `reported` (en la QA solo se confirmó que el artículo existe; sus resultados no se verificaron; corregido tras QA 2026-11-19)
- **Cambio en Ucoach:**
  - Mantener la regla de la mañana como mínimo práctico. Añadir "y sal a la luz natural siempre que puedas durante el día; trabaja cerca de una ventana".
  - Para los búhos y en invierno, darle más prioridad. No proponer luz muy temprana a los alondras extremos que se despiertan antes de lo que quieren (`inferred`).

#### 2b. Luz cálida y tenue por la noche
- **Veredicto:** sólido en lo esencial; el plazo es demasiado corto.
- **Evidencia:** Brown et al. (2022) recomiendan **como máximo 10 lux mEDI desde al menos 3 horas antes de acostarse** y como máximo 1 lux mEDI en el dormitorio durante el sueño (10 si hace falta ver algo). Lo que más pesa es la intensidad de la luz ambiente, no solo su color.
- **Fuentes:** Brown 2022 (arriba), `verified`.
- **Cambio en Ucoach:** adelantar el aviso de "bajar luces" a **3 horas antes** de la hora de acostarse, como pide Brown 2022 (corregido tras QA 2026-11-19) (lámparas bajas e indirectas en lugar de techo blanco) y añadir "dormitorio a oscuras: persianas o antifaz".

### 3. Cafeína

#### 3a. Primer café unos 75 minutos después de despertar
- **Veredicto:** débil (sin base empírica).
- **Evidencia:** el "retraso de 90 minutos" que popularizó Huberman se basa en dos mecanismos supuestos: que la adenosina sigue eliminándose después de despertar y que el café interfiere con el pico de cortisol del despertar. **No hay ningún ensayo publicado** que demuestre que retrasar el café mejora la energía o evita el bajón de la tarde. En consumidores habituales, 5 días con 300-600 mg al día **redujeron** la respuesta de cortisol: desapareció tras la dosis de las 9:00, pero volvió a aparecer tras la de las 13:00 («reduced, but not eliminated»; Lovallo et al., 2005, *Psychosomatic Medicine*). La tolerancia es parcial, y aun así debilita el argumento del cortisol matinal (corregido tras QA 2026-11-19).
- **Fuentes:**
  - Lovallo WR et al. 2005, *Psychosom Med*. https://www.researchgate.net/publication/7561673_Caffeine_Stimulation_of_Cortisol_Secretion_Across_the_Waking_Hours_in_Relation_to_Caffeine_Intake_Levels y https://pubmed.ncbi.nlm.nih.gov/16204431/ `verified` en la QA
  - Análisis divulgativo de la controversia (2024-2025): https://sleepopolis.com/news/controversy-over-wait-to-caffeinate-rule/ `reported`
- **Cambio en Ucoach:** **eliminar** el cálculo de la hora del primer café o convertirlo en preferencia del usuario ("si te sienta mejor esperar, configúralo"). En el brief, mostrar solo la hora límite.

#### 3b. Último café 8 horas antes de dormir
- **Veredicto:** sólido en la dirección; las 8 h se quedan por debajo del mínimo de la evidencia (corregido tras QA 2026-11-19).
- **Evidencia:** el metaanálisis de Gardiner et al. (2023, *Sleep Medicine Reviews*, ensayos cruzados controlados) concluye que, para no perder tiempo de sueño, un café (107 mg en 250 ml) debe tomarse **al menos 8,8 h antes** de acostarse y un preentreno estándar (217,5 mg), **al menos 13,2 h antes**. La cafeína redujo el sueño profundo unos 11 minutos. En consumidores habituales el efecto podría ser menor por tolerancia, pero la evidencia es escasa. Drake et al. (2013) vieron que 400 mg tomados 6 h antes de acostarse quitaban más de 1 h de sueño objetivo sin que los participantes lo notaran. La EFSA (2015) considera seguros hasta 400 mg al día y 200 mg por toma en adultos sanos, y señala que 100 mg cerca de la hora de dormir pueden afectar al sueño de algunas personas.
- **Fuentes:**
  - Gardiner C et al. 2023, *Sleep Med Rev* 69:101764. https://eprints.leedsbeckett.ac.uk/id/eprint/9625/ `verified` (PDF del manuscrito aceptado)
  - Drake C et al. 2013, *J Clin Sleep Med*. https://pmc.ncbi.nlm.nih.gov/articles/PMC3805807 `verified` (resumen)
  - EFSA NDA Panel 2015, *EFSA Journal* 13(5):4102. https://efsa.onlinelibrary.wiley.com/doi/10.2903/j.efsa.2015.4102 (la web bloqueó la lectura); cifras confirmadas en la QA con la presentación oficial de la EFSA: https://www.efsa.europa.eu/sites/default/files/event/documentset/150305-p02.pdf `verified` (corregido tras QA 2026-11-19)
- **Cambio en Ucoach:**
  - Ventana dependiente de la dosis: café o té, al menos 9 h antes de dormir (Gardiner: 8,8 h como mínimo); dosis altas (preentreno, bebidas energéticas, doble espresso grande), al menos 13,5 h (Gardiner: 13,2 h como mínimo) (corregido tras QA 2026-11-19).
  - Añadir un registro opcional de cafeína y un aviso si se pasa de unos 400 mg al día.
  - Si el usuario indica que es sensible, adelantar la hora límite.

### 4. Siesta de 10 a 20 minutos si se durmieron menos de 6 horas
- **Veredicto:** razonable.
- **Evidencia:** tras limitar el sueño a unas 5 horas, una siesta de **10 minutos** a las 15:00 fue la más eficaz. La de 30 minutos produjo inercia del sueño inmediata y solo mejoró el rendimiento más tarde (Brooks y Lack, 2006, *Sleep*, n=24). El metaanálisis de Dutheil et al. (2021; 11 estudios, 381 participantes, casi todos de laboratorio) encuentra una mejora cognitiva pequeña tras la siesta (ES 0,18), sobre todo en la alerta (0,29), que dura hasta unos 120 minutos; las siestas antes de las 13:00 rinden más. No es un metaanálisis de siestas cortas: la siesta media fue de 55 minutos (corregido tras QA 2026-11-19). Pide más estudios en condiciones reales de trabajo. En insomnio crónico, la TCC-I recomienda **evitar las siestas** para no reducir la presión de sueño de la noche (`inferred` a partir de AASM 2021 y de la guía europea de 2023).
- **Fuentes:**
  - Brooks A, Lack L. 2006, *Sleep* 29(6). https://pubmed.ncbi.nlm.nih.gov/16796222/ `verified` (resumen)
  - Dutheil F et al. 2021, *Int J Environ Res Public Health*. https://pubmed.ncbi.nlm.nih.gov/34639511/ `verified` (resumen)
- **Cambio en Ucoach:**
  - Proponer la siesta **antes de las 15:00** (o unas 7 h antes de acostarse), con alarma a los 20 minutos de cama como máximo.
  - **No proponerla** si el usuario ha dicho que le cuesta dormirse o mantener el sueño.
  - Avisar de no conducir en los 15-30 minutos posteriores.

### 5. Bloque de foco y cronotipo

#### 5a. Bloque de 90 minutos (60 con deuda) y el "ciclo ultradiano"
- **Veredicto:** razonable como práctica; débil como justificación biológica.
- **Evidencia:** el ciclo de unos 90 minutos de Kleitman está bien establecido **durante el sueño** (alternancia NREM-REM). La idea de un *basic rest-activity cycle* que siga en vigilia no se ha confirmado: hay trabajos en contra ya desde 1977 y periodos que van de 80 a 120 minutos según la persona. El metaanálisis de micropausas de Albulescu et al. (2022, *PLOS ONE*, 22 muestras, N=2.335) halló más vigor (d=0,36) y menos fatiga (d=0,35), pero **ningún efecto significativo sobre el rendimiento en tareas exigentes**. Proteger un bloque sin interrupciones tiene sentido por el coste de cambiar de tarea, pero los 90 minutos no son una cifra fisiológica (`inferred`).
- **Fuentes:**
  - Revisiones sobre la alternancia actividad-reposo en vigilia (episodios cada 1-2 h, irregulares, sin ciclo fijo de 90 min): https://pubmed.ncbi.nlm.nih.gov/30454601/ y https://pubmed.ncbi.nlm.nih.gov/28349079/ `verified` en la QA. El DOI 10.1007/978-1-4020-8352-5_13 que se citaba es un capítulo de LaJambe y Brown sobre ritmos cognitivos en privación de sueño, no una revisión del BRAC (corregido tras QA 2026-11-19)
  - Albulescu P et al. 2022, *PLOS ONE* 17(8):e0272460. https://doaj.org/article/c6f37b6ba159469296b2cb968b65505f `verified` (resumen)
- **Cambio en Ucoach:** convertirlo en un bloque **configurable de 60 a 120 minutos** (90 por defecto) y quitar cualquier mención al "ciclo ultradiano". Con sueño corto, mantener el bloque pero dedicarlo a tareas conocidas y no a decisiones irreversibles (`inferred`).

#### 5b. Pico según cronotipo (alondra, intermedio o búho)
- **Veredicto:** razonable o débil.
- **Evidencia:** la revisión sistemática de Chauhan et al. (2025, *Chronobiology International*) observa que en más del 80 % de los estudios el cronotipo por sí solo no afecta a la cognición. El "efecto de sincronía" (rendir mejor a tu hora óptima) aparece en un 45 % de los estudios con adultos jóvenes y en un 83 % de los estudios con mayores, sobre todo en atención, inhibición y memoria. Los cuestionarios validados son el MEQ (Horne y Östberg, 1976) y el MCTQ (Roenneberg). Los cuatro "animales" de Breus no lo están.
- **Fuentes:**
  - Chauhan S et al. 2025, *Chronobiol Int*, doi:10.1080/07420528.2025.2490495. https://researchinnovation.kingston.ac.uk/en/publications/chronotype-and-synchrony-effects-in-human-cognitive-performance-a/ `reported`
  - Sleep Foundation sobre el MEQ y el MCTQ: https://www.sleepfoundation.org/how-sleep-works/chronotypes `reported`
- **Cambio en Ucoach:**
  - Establecer el cronotipo con el punto medio del sueño en días libres (corregido por deuda, como en el MCTQ) a partir de los registros, o con un cuestionario breve validado.
  - Tras 2-3 semanas de check-ins de energía y foco, **situar el pico según los datos del propio usuario** y avisarle si su pico real no coincide con el teórico. Encaja con el principio "Datos propios antes que promedios".

### 6. Entreno ajustado al sueño

#### 6a. Bajar la intensidad con deuda de sueño
- **Veredicto:** razonable, con matices.
- **Evidencia:** el metaanálisis de Craven et al. (2022, *Sports Medicine*, 959 participantes, 89 % hombres) halló que la pérdida aguda de sueño reduce el rendimiento físico una media del **7,6 %**. El efecto es consistente en las sesiones de **tarde** y casi nulo en las de **mañana**, y es mayor cuando se recorta el final de la noche o se pasa la noche en vela. Las tareas de habilidad son las más afectadas. No hay pruebas de que un ejercicio intenso tras una sola noche corta sea peligroso para una persona sana. Sí hay asociaciones observacionales entre dormir poco de forma **crónica** y lesionarse más (Milewski 2014, adolescentes, OR ≈ 1,7 por debajo de 8 h; la revisión posterior de Gao no aclara el efecto de la falta aguda).
- **Fuentes:**
  - Craven J et al. 2022, *Sports Med* 52:2669-2690, doi:10.1007/s40279-022-01706-y. https://read.qxmd.com/read/35708888/ `verified` (resumen)
  - Milewski MD et al. 2014, *J Pediatr Orthop*. https://pubmed.ncbi.nlm.nih.gov/25028798/ `reported`
- **Cambio en Ucoach:**
  - Con sueño corto, **no cancelar** el ejercicio: el ejercicio regular ayuda al sueño. Proponer:
    - mantener la sesión si es por la mañana;
    - evitar los intentos de marca, los máximos y la técnica compleja por la tarde;
    - sustituir los intervalos por zona 2 o fuerza submáxima.
  - Si hay deuda **varias noches seguidas**, bajar el volumen semanal.

#### 6b. VFC o readiness para decidir la intensidad
- **Veredicto:** débil o razonable.
- **Evidencia:** en el metaanálisis de Manresa-Rocamora et al. (2021, IJERPH 18(19):10299), el entrenamiento guiado por VFC obtuvo efectos pequeños y **no significativos** frente al plan predefinido en VO2máx (SMD 0,20) y rendimiento de resistencia (SMD 0,20), y un efecto significativo en los índices vagales (SMD 0,50). Granero-Gallegos et al. (2020) solo analizan el VO2máx y encuentran una ventaja pequeña del grupo guiado por VFC (ES 0,19) (corregido tras QA 2026-11-19). Düking et al. (2021) encontraron efectos medianos en parámetros submáximos, pero no en rendimiento (g=0,08), aunque con menos "no respondedores". Los metaanálisis tienen poca potencia.
- **Fuentes:**
  - Manresa-Rocamora A et al. 2021, *IJERPH* 18(19):10299. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8507742/ (PMID 34639599) `verified` en la QA (corregido tras QA 2026-11-19: antes se atribuía este enlace a Granero-Gallegos)
  - Granero-Gallegos A et al. 2020, *IJERPH* 17(21):7999. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7663087/ `verified` en la QA
  - Düking P et al. 2021, *J Sci Med Sport*. https://pubmed.ncbi.nlm.nih.gov/34489178/ `verified` en la QA
- **Cambio en Ucoach:** usar la VFC solo como **señal secundaria**. Compararla con la media móvil de 7 días del usuario y actuar solo si está por debajo de su rango normal **y** el sueño o la sensación subjetiva también son malos. Nunca bajar la intensidad por un dato aislado.

### 7. Pausas activas, sedentarismo y vista

#### 7a. Pausa activa de 5 minutos cada 60-90 minutos
- **Veredicto:** razonable pero insuficiente.
- **Evidencia:** en los ensayos cruzados del metaanálisis de Buffey et al. (2022, *Sports Medicine*), caminar a intensidad ligera redujo la glucosa y la insulina después de comer frente a seguir sentado, y funcionó mejor que solo ponerse de pie. Buffey reúne participantes sobre todo con sobrepeso. Un metaanálisis de 2025 en adultos con obesidad (17 ensayos, 261 participantes) concluye que interrumpir el tiempo sentado **cada 30 minutos más o menos con 2 a 5 minutos** de caminata o ejercicios sencillos de fuerza baja la glucosa (SMD −0,49) y la insulina (SMD −0,26). Los subgrupos apuntan a efectos mayores con pausas cada 30 minutos o menos. La OMS (2020) recomienda reducir el sedentarismo, pero no fija un umbral numérico.
- **Fuentes:**
  - Buffey AJ et al. 2022, *Sports Med*. https://www.pubmed.gov/35147898/ `verified` en la QA
  - Metaanálisis de 2025, *Frontiers in Nutrition*, doi:10.3389/fnut.2025.1708301. https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2025.1708301/full y https://pubmed.ncbi.nlm.nih.gov/41356824/ `verified` en la QA
  - Bull FC et al. 2020, *Br J Sports Med* 54:1451-1462. https://digibug.ugr.es/handle/10481/66573 `verified` (resumen)
- **Cambio en Ucoach:**
  - **Micropausas** de 2-3 minutos de pie o caminando cada 30 minutos aproximadamente de estar sentado, que es lo que estudió la evidencia (adultos con sobrepeso u obesidad; corregido tras QA 2026-11-19) (aprovechar llamadas y cambios de tarea), más una pausa de 5-10 minutos cada 60-90.
  - Para no saturar, `nudge` puede avisar solo si detecta 60 minutos sin moverse, si hay datos de pasos.
  - Proponer un paseo de 10 minutos después de comer.

#### 7b. Regla 20-20-20
- **Veredicto:** débil (heurística).
- **Evidencia:** la American Academy of Ophthalmology la recomienda junto con parpadear y poner la pantalla a la distancia de un brazo, unos 63 cm (`reported`: aao.org no se pudo abrir en la QA), y **no recomienda** las gafas de filtro azul. El único ensayo que la probó con recordatorios (Talens-Estarelles et al., 2023, *Contact Lens and Anterior Eye*, n=29) redujo los síntomas mientras duraron los recordatorios, pero la mejora desapareció una semana después. Johnson y Rosenfield (2023, *Optom Vis Sci*, n=30) no hallaron efecto de las pausas de 20 segundos en síntomas ni en rendimiento lector.
- **Fuentes:**
  - Talens-Estarelles C et al. 2023, *Cont Lens Anterior Eye* 46(2):101744. https://research.aston.ac.uk/en/publications/the-effects-of-breaks-on-digital-eye-strain-dry-eye-and-binocular/ y https://pubmed.ncbi.nlm.nih.gov/35963776/ `verified` en la QA (corregido tras QA 2026-11-19)
  - Johnson S, Rosenfield M. 2023, *Optom Vis Sci* 100(1):52-56, "20-20-20 Rule: Are These Numbers Justified?". https://pubmed.ncbi.nlm.nih.gov/36473088/ `verified` en la QA (corregido tras QA 2026-11-19)
  - AAO, consejos sobre fatiga visual digital (2020): https://aao.org/newsroom/news-releases/detail/protect-your-eyes-in-home-office `reported` (la web bloqueó la lectura en la QA)
- **Cambio en Ucoach:** dejarla en la lista de ergonomía como **sugerencia opcional**, redactada como "cada rato, mira a lo lejos unos segundos y parpadea", sin decir que está probada. No usar `nudge` cada 20 minutos.

### 8. Reuniones

#### 8a. Alerta con 2 h o más de reuniones seguidas sin pausas
- **Veredicto:** razonable (evidencia débil, plausible).
- **Evidencia:** el Microsoft Human Factors Lab (marzo de 2021) midió con EEG a 14 personas en 4 videollamadas de 30 minutos seguidas o separadas por 10 minutos de pausa. Sin pausas, la actividad beta, asociada al estrés, subió de forma acumulativa y se disparó en las transiciones. Con pausas se mantuvo estable y la asimetría alfa frontal indicó más implicación. Es un estudio corporativo, sin revisión por pares y con muestra mínima, y durante las pausas los participantes meditaban con Headspace (un factor de confusión). El metaanálisis de micropausas (Albulescu 2022) apoya la misma dirección en fatiga y vigor.
- **Fuentes:**
  - Microsoft WorkLab 2021, "Research proves your brain needs breaks". https://www.microsoft.com/en-us/worklab/work-trend-index/brain-research `verified`
- **Cambio en Ucoach:** mantener la alerta y proponer una acción concreta: "Mete 5-10 minutos entre la 2.ª y la 3.ª reunión: levántate, bebe agua, mira por la ventana". En la explicación, citar el estudio como "exploratorio".

#### 8b. Reuniones de 25 o 50 minutos
- **Veredicto:** razonable (norma organizativa, no fisiológica).
- **Evidencia:** no hay ensayos que comparen reuniones de 25 y 30 minutos. Su base es la misma que la de las pausas (punto 8a) y la observación práctica de que, sin un margen, no hay transición (`inferred`).
- **Cambio en Ucoach:** mantener como sugerencia de agenda ("acorta por defecto a 25/50 en tu calendario"), sin atribuirle un efecto probado.

### 9. Comida

#### 9a. Comida de 45 minutos entre las 13:00 y las 15:30
- **Veredicto:** razonable.
- **Evidencia:** en una cohorte española de 420 personas en tratamiento para perder peso, quienes comían **después de las 15:00** perdieron menos peso que quienes comían antes (Garaulet et al., 2013, *Int J Obes*). La declaración científica de la AHA (St-Onge et al., 2017) concluye que comer tarde podría ser perjudicial y que la regularidad y el horario de las comidas merecen atención, aunque la evidencia es sobre todo observacional. Vujović et al. (2022, *Cell Metabolism*, ensayo cruzado, n=16) vieron que comer tarde aumentaba el hambre y reducía el gasto energético.
- **Fuentes:**
  - Garaulet M et al. 2013, *Int J Obes* 37:604-611. https://pubmed.ncbi.nlm.nih.gov/23357955/ `verified` en la QA (corregido tras QA 2026-11-19)
  - St-Onge MP et al. 2017, *Circulation*, doi:10.1161/CIR.0000000000000476. https://professional.heart.org/en/science-news/meal-timing-and-frequency-implications-for-cardiovascular-disease-prevention `reported`
  - Vujović N et al. 2022, *Cell Metab* 34(10):1486-1498. https://news.harvard.edu/gazette/story/2022/10/study-looks-at-why-late-night-eating-increases-obesity-risk `reported`
- **Cambio en Ucoach:** preferir **13:00-15:00** cuando la agenda lo permita y priorizar la **regularidad** (comer a horas parecidas cada día). Mantener el margen hasta las 15:30 por el horario español.

#### 9b. Cena 2 o 3 horas antes de dormir
- **Veredicto:** razonable.
- **Evidencia:** en un estudio de casos y controles, acostarse menos de 3 h después de cenar multiplicaba por 7,45 la probabilidad de reflujo frente a esperar 4 h o más (Fujiwara et al., 2005, *Am J Gastroenterol*). Sobre la calidad del sueño **no hay metaanálisis**: solo ensayos pequeños y estudios transversales que muestran algo más de latencia de sueño con cenas muy tardías.
- **Fuentes:**
  - Fujiwara Y et al. 2005, *Am J Gastroenterol*. https://pubmed.ncbi.nlm.nih.gov/16393212/ `verified` (resumen)
- **Cambio en Ucoach:** "Cena 2-3 h antes de acostarte; **3 h o más si tienes ardor o reflujo**". Añadir "cena ligera si vas tarde".

#### 9c. Evitar comidas copiosas antes de los bloques de foco
- **Veredicto:** razonable (la evidencia directa es escasa).
- **Evidencia:** el bajón de la tarde tiene un componente circadiano y otro de la comida. Las comidas grandes favorecen la somnolencia, pero no he encontrado un metaanálisis sobre su efecto en el rendimiento cognitivo de oficina (`inferred`).
- **Cambio en Ucoach:** mantener como consejo y combinarlo con un paseo corto después de comer (punto 7a).

#### 9d. Alimentación con horario restringido (no es regla de Ucoach, pero el usuario preguntará)
- **Veredicto:** no recomendar por defecto.
- **Evidencia:**
  - En pérdida de peso, el ayuno con horario restringido se parece a la restricción calórica clásica. En el ensayo de Liu et al. (2022, *NEJM*, 139 adultos, 12 meses), combinarlo con la restricción calórica no aportó una diferencia significativa frente a la restricción sola.
  - La revisión paraguas de 2025 en *Diabetes Obes Metab* (12 metaanálisis, AMSTAR-2 y GRADE) encuentra evidencia de calidad alta de que el horario restringido reduce el peso, la grasa, la insulina en ayunas y la HbA1c en adultos con sobrepeso, y pide estudios a largo plazo. No dice que supere a la restricción calórica, y Liu 2022 muestra que no lo hace (corregido tras QA 2026-11-19).
  - **La controversia de 2024:** un *abstract* presentado en un congreso de la AHA (Zhong et al., NHANES 2003-2018, más de 20.000 adultos) asoció comer en menos de 8 h con un **91 % más de mortalidad cardiovascular**. Su base son 2 recordatorios de 24 h y puede haber causalidad inversa (el dato de «un 60 % más de fumadores» en ese grupo no se verificó en la QA). La UIC informó de una carta crítica de 34 expertos. **El estudio completo sí se publicó** después: Chen et al., *Diabetes Metab Syndr* 2025;19(7):103278 (n=19.831, referencia de 12-14 h). Da un HR cardiovascular de 2,35 (1,39-3,98), pero la asociación con la mortalidad total no resiste los análisis de sensibilidad y los autores admiten posible confusión residual. Sigue siendo observacional (corregido tras QA 2026-11-19).
- **Fuentes:**
  - Liu D et al. 2022, *NEJM* 386:1495-1504, doi:10.1056/NEJMoa2114833. https://pubmed.ncbi.nlm.nih.gov/35443107/ `verified` en la QA (corregido tras QA 2026-11-19)
  - Comunicado de la AHA de 2024: https://newsroom.heart.org/news/8-hour-time-restricted-eating-linked-to-a-91-higher-risk-of-cardiovascular-death `verified` en la QA; cobertura: https://www.nbcnews.com/health/heart-health/intermittent-fasting-risk-cardiovascular-death-rcna143853 `reported`
  - Carta crítica de los 34 expertos (2024), nota de la UIC: https://ahs.uic.edu/inside-ahs/news/ `reported` (el PDF que se citaba antes ya no responde; corregido tras QA 2026-11-19)
  - Estudio completo: Chen M et al. 2025, *Diabetes Metab Syndr* 19(7):103278. https://pubmed.ncbi.nlm.nih.gov/40849219/ `verified` en la QA
  - Revisión paraguas de 2025, *Diabetes Obes Metab* 27(2):920-932: https://pubmed.ncbi.nlm.nih.gov/39618023/ `verified` en la QA
- **Cambio en Ucoach:** no proponerlo. Si el usuario lo practica, decirle que "es una opción razonable si te resulta cómoda, pero no mejor que reducir la cantidad. El titular de 2024 sobre mortalidad sale de un estudio observacional que no demuestra que el horario sea la causa" (corregido tras QA 2026-11-19). Y derivarle al dietista-nutricionista si tiene diabetes, toma medicación o tiene antecedentes de trastornos de la conducta alimentaria.

### 10. Desconexión de 60 minutos sin pantallas antes de dormir
- **Veredicto:** razonable como hábito, con una justificación ("luz azul") débil.
- **Evidencia:** el consenso de la NSF (Hartstein et al., 2024, *Sleep Health*, 16 expertos, 522 artículos empíricos) concluyó que las pantallas empeoran el sueño de **niños y adolescentes** y que el contenido importa. **No hubo consenso** sobre si la luz de las pantallas afecta al sueño de nadie, ni sobre si el tiempo de pantalla, la luz o el contenido afectan al de los **adultos**. Chang et al. (2015) sí hallaron supresión de melatonina, retraso circadiano y unos 10 minutos más de latencia, pero con **4 horas** de lectura en un iPad a brillo alto. Brown et al. (2022) ponen el foco en la luz **ambiente** en las 3 horas previas.
- **Fuentes:**
  - Hartstein LE et al. 2024, *Sleep Health* 10(4):373-384, doi:10.1016/j.sleh.2024.05.001. https://www.colorado.edu/today/2024/05/28/light-or-content-what-we-know-about-screens-and-sleep-disruption `verified` (nota de la universidad de la autora)
  - Chang AM et al. 2015, *PNAS* 112(4):1232-1237. https://pubmed.ncbi.nlm.nih.gov/25535358/ `verified` (resumen)
- **Cambio en Ucoach:**
  - Redactarlo así: "Última hora: actividades tranquilas. Nada de trabajo, correo, noticias ni redes. Si usas pantalla, que sea contenido relajado y con el brillo al mínimo; el modo noche por sí solo ayuda poco. Móvil cargando fuera del dormitorio" (corregido tras QA 2026-11-19; ver Nagare 2019 en el informe 07).
  - Quitar cualquier mención a que la luz azul de la pantalla es el problema principal.
  - Medir si el usuario se acuesta a su hora: retrasar el sueño por las pantallas pesa más que la luz.

### 11. Alcohol: nada en las 3 horas previas
- **Veredicto:** razonable pero insuficiente.
- **Evidencia:** el metaanálisis de Gardiner et al. (2025, *Sleep Medicine Reviews*, 27 estudios) muestra que incluso **dosis bajas** (≤0,5 g/kg, unas dos consumiciones) alteran el sueño REM, con un efecto que crece con la dosis. Solo las dosis altas acortan el tiempo para dormirse, y ese es el "falso beneficio" del alcohol. En la mayoría de los ensayos el alcohol se tomó en las 3 horas previas al sueño, así que la evidencia no demuestra que esperar 3 horas evite los efectos. La regla de las 3 horas es una heurística (`inferred`).
- **Fuentes:**
  - Gardiner C et al. 2025, *Sleep Med Rev* 80:102030, doi:10.1016/j.smrv.2024.102030. https://research.monash.edu/en/publications/the-effect-of-alcohol-on-subsequent-sleep-in-healthy-adults-a-sys/ `reported`
- **Cambio en Ucoach:** "Si bebes, cuanto menos y cuanto antes, mejor; lo ideal es nada en las 3-4 h previas. Incluso una o dos copas empeoran el sueño REM". Añadir a la revisión semanal la relación entre los días con alcohol registrado y el sueño o la energía del día siguiente, con datos propios.

### 12. Ejercicio y pasos

#### 12a. Guías de la OMS de 2020
- **Veredicto:** sólido.
- **Evidencia:** la OMS (Bull et al., 2020) recomienda 150-300 minutos semanales de actividad moderada o 75-150 de vigorosa, más fuerza 2 días o más, y reducir el sedentarismo. No fija un umbral numérico de tiempo sentado porque la evidencia no alcanza.
- **Fuentes:** Bull FC et al. 2020 (arriba), `verified`. Guías de la OMS: https://www.who.int/publications/i/item/9789240015128
- **Cambio en Ucoach:** mantener. Añadir la línea de sedentarismo y que "cualquier actividad cuenta y más es mejor".

#### 12b. 8.000 pasos al día (acción de *Built to Move*)
- **Veredicto:** sólido o razonable.
- **Evidencia:** según el metaanálisis de Paluch et al. (2022, *Lancet Public Health*, 15 cohortes, 47.471 adultos), la mortalidad baja hasta estabilizarse en torno a **6.000-8.000 pasos en mayores de 60 años** y 8.000-10.000 en menores de 60. El de Ding et al. (2025, *Lancet Public Health*, 57 estudios) muestra que **7.000 pasos** frente a 2.000 se asocian a un 47 % menos de mortalidad y un 38 % menos de demencia. Más allá de 7.000, las mejoras adicionales son modestas.
- **Fuentes:**
  - Paluch AE et al. 2022, *Lancet Public Health*. https://doaj.org/article/c3639c468b4348958202e52793ab979d `verified` (resumen)
  - Ding D et al. 2025, *Lancet Public Health*, doi:10.1016/S2468-2667(25)00164-1. https://www.sciencedaily.com/releases/2025/07/250726234359.htm `verified` (nota de prensa)
- **Cambio en Ucoach:** objetivo por defecto de **7.000-8.000 pasos**. Si la media actual es baja, subir 1.000-2.000 sobre la línea base antes de fijar el objetivo. Recordar que son estudios observacionales.

### 13. Ergonomía

#### 13a. Pantalla, pies, codos, espalda, luz y reflejos
- **Veredicto:** razonable (consenso normativo; la evidencia sobre resultados de salud es débil).
- **Evidencia:** los puntos de control coinciden con las guías técnicas del INSST. El RD 488/1997 solo pide que la pantalla sea orientable e inclinable, sin dar ángulo ni distancia (corregido tras QA 2026-11-19):
  - pantalla entre la línea horizontal de visión y 40° por debajo, con el borde superior a la altura de los ojos o algo por debajo (guía técnica del INSST de 2021);
  - distancia nunca menor de 30 cm y habitual entre 40 y 75 cm (guía técnica del INSST), 40 cm o más (NTP 251), o la de un brazo, unos 63 cm (AAO);
  - reposapiés si los pies no llegan;
  - ventana lateral.

  Pero la revisión Cochrane de Hoe et al. (2018, 15 ensayos, 2.165 trabajadores, 14 con alto riesgo de sesgo) **no encontró efecto** del ajuste del puesto ni de las mesas elevables sobre el dolor de miembro superior. Solo halló evidencia moderada a favor de los reposabrazos con ratón alternativo para el cuello y el hombro, y muy baja a favor de pausas adicionales.
- **Fuentes:**
  - INSST, preguntas frecuentes sobre trabajo con ordenadores, NTP 251 y guía técnica de pantallas de 2021. https://www.insst.es/materias/riesgos/riesgos-ergonomicos/trabajo-con-ordenadores/faq `reported`; RD 488/1997: https://www.boe.es/buscar/act.php?id=BOE-A-1997-8671 `verified` en la QA
  - Hoe VCW et al. 2018, *Cochrane* CD008570. https://www.cochrane.org/CD008570 y https://pubmed.ncbi.nlm.nih.gov/30350850/ `verified`
- **Cambio en Ucoach:**
  - Mantener la lista y corregir "codos a 90°" por **"codos a 90-110°, hombros relajados"**.
  - Con gafas progresivas, bajar más la pantalla.
  - Presentar el chequeo como **comodidad y prevención razonable**, no como tratamiento del dolor. Si el dolor dura más de 4-6 semanas o se irradia, derivar a un médico o fisioterapeuta.
  - Añadir la idea de que "la mejor postura es la siguiente": variar de postura importa más que encontrar una perfecta (`inferred`).

#### 13b. Alternar sentado y de pie
- **Veredicto:** razonable.
- **Evidencia:** la revisión Cochrane de Shrestha et al. (2018; 34 estudios, 3.397 participantes) encuentra evidencia de calidad baja de que las mesas elevables reducen el tiempo sentado unos 100 minutos al día a corto plazo (IC 84-116) y unos 57 minutos a medio plazo. **La revisión no evalúa los beneficios para la salud**, así que no están probados (corregido tras QA 2026-11-19).
- **Fuentes:** Shrestha N et al. 2018, *Cochrane* CD010912.pub5. https://doi.org/10.1002/14651858.CD010912.pub5 y https://pubmed.ncbi.nlm.nih.gov/30556590/ `verified` en la QA (corregido tras QA 2026-11-19)
- **Cambio en Ucoach:** mantener, pero dando prioridad a **moverse**: caminar en las llamadas o hacer micropausas antes que estar de pie quieto, porque caminar supera a estar de pie en glucosa (punto 7a).

### 14. Lectura de 20 minutos dentro de la desconexión, en papel o e-ink
- **Veredicto:** razonable.
- **Evidencia:** en el ensayo de Chang et al. (2015, *PNAS*, n=12), leer en un dispositivo retroiluminado durante **4 horas** antes de dormir suprimió la melatonina, retrasó el reloj unos 90 minutos, alargó la latencia en unos 10 minutos y redujo la alerta de la mañana siguiente frente al libro en papel. La dosis de luz era alta y el consenso de la NSF (2024) no logró acuerdo sobre la importancia de la luz en adultos. Leer en papel o en e-ink con luz frontal cálida y baja es una forma prudente de cumplir el límite de 10 lux de Brown 2022 (`inferred`). La afirmación popular de que "leer 6 minutos reduce el estrés un 68 %" viene de un estudio no publicado (Mindlab, 2009) y no debe citarse (`reported`).
- **Fuentes:** Chang 2015 y Brown 2022 (arriba).
- **Cambio en Ucoach:** mantener. Precisar "papel o e-ink con luz baja; si usas tableta o móvil, brillo mínimo" (el modo noche es solo un complemento; corregido tras QA 2026-11-19). Elegir lectura que no active, nada de trabajo.

### 15. Revisión semanal con "un hábito cada vez"
- **Veredicto:** razonable en el principio, mal calibrado en la cadencia.
- **Evidencia:**
  - **Tiempo de formación.** En Lally et al. (2010, *Eur J Soc Psychol*, 96 participantes, 84 días), alcanzar el 95 % de la automaticidad costó una mediana de 66 días, con un rango de 18 a 254 (el extremo superior es una proyección). Saltarse un día suelto no impidió formar el hábito, pero la inconsistencia sí. La revisión sistemática de Singh et al. (2024, *Healthcare*, 20 estudios) sitúa la mediana en **59-66 días** y el rango entre 4 y 335. Señala como determinantes la frecuencia, hacerlo siempre a la misma hora, que resulte agradable y planificarlo. Solo 4 estudios midieron el tiempo directamente.
  - **Un hábito o varios.** Los ensayos que comparan el cambio secuencial con el simultáneo son pocos. James et al. (2016, *Prev Med*, 6 ensayos) no encontraron un ganador claro. Meader et al. (2017, 69 ensayos) y Silva et al. (2024) ven mejoras modestas con intervenciones simultáneas. "Un hábito cada vez" es razonable por la carga cognitiva y la retención, pero no está demostrado que sea superior.
- **Fuentes:**
  - Lally P et al. 2010, *Eur J Soc Psychol*. https://www.ucl.ac.uk/news/2009/aug/how-long-does-it-take-form-habit `verified` (nota de la UCL)
  - Singh B et al. 2024, *Healthcare* 12(23):2488. https://www.eurekalert.org/news-releases/1071242 `verified` (nota de prensa)
  - James E et al. 2016, *Prev Med*. https://www.pubmed.gov/27311332/ `reported`
- **Cambio en Ucoach:**
  - La revisión semanal **no debe proponer un hábito nuevo cada semana**. Debe mantener un **hábito de foco** durante 8 a 10 semanas o hasta que el usuario puntúe alto en automaticidad (4 preguntas del SRBAI, Gardner 2012) y solo entonces sumar el siguiente.
  - Cada semana, la sugerencia debe ser **ajustar** el hábito en curso (hacerlo más fácil, cambiar la señal o la hora), no sustituirlo.
  - Añadir el mensaje "fallar un día no rompe nada; lo que cuenta es la constancia" (Lally 2010), coherente con "no falles dos días seguidos" de Atomic Habits.

---

## Reglas que faltan

| Regla nueva | Por qué (evidencia) | Propuesta para Ucoach | Fuente |
|---|---|---|---|
| **Insomnio: TCC-I antes que "higiene del sueño"** | La AASM (2021) recomienda con fuerza la TCC-I multicomponente. Admite como componentes sueltos la restricción del sueño, el control de estímulos y la relajación, y **desaconseja la higiene del sueño como tratamiento único**. La guía europea (Riemann 2023) recomienda la TCC-I presencial o digital como primera línea (grado A) | Si el usuario declara dificultad para dormir **3 noches por semana o más durante 3 meses o más**, no darle más consejos de higiene: recomendarle la TCC-I (profesional o programa digital validado) y la consulta médica. Incluir la regla de los 20 minutos (levantarse si no se duerme) **sin aplicar por su cuenta la restricción del tiempo en cama**, que debe supervisar un profesional | AASM 2021: https://aasm.org/new-guideline-supports-behavioral-psychological-treatments-for-insomnia/ `verified`; Riemann 2023, *J Sleep Res*: https://worldsleepsociety.org/takeaways-from-updated-european-insomnia-guideline/ y https://pubmed.ncbi.nlm.nih.gov/38016484/ `verified` en la QA |
| **Señales de alarma y derivación** | Ronquidos fuertes, apneas presenciadas, somnolencia diurna, hipertensión e IMC alto son los indicadores de apnea. Con un STOP-Bang de 5 o más el riesgo es alto (de 3 o más, alta sensibilidad para la apnea moderada o grave) | Una lista explícita que desactive el consejo normal y derive: (1) sospecha de apnea, con STOP-Bang opcional; (2) **somnolencia al conducir**; (3) insomnio crónico; (4) ánimo bajo 2 semanas o más, o cualquier ideación autolítica, con derivación inmediata y teléfono 024 en España; (5) dolor torácico, mareo o falta de aire desproporcionada al hacer ejercicio; (6) pérdida de peso sin explicación o fatiga persistente pese a dormir bien | STOP-Bang: Chung et al. 2016, *Chest*, https://pubmed.ncbi.nlm.nih.gov/26378880/ `verified` en la QA (PMC4008971, que se citaba antes, es la validación de Boynton 2013); línea 024, en funcionamiento desde el 10-5-2022: https://www.sanidad.gob.es/gabinete/notasPrensa.do?id=5739 `verified` en la QA; resto `inferred` a partir de la práctica clínica (corregido tras QA 2026-11-19) |
| **Luz durante todo el día** | ≥250 lux mEDI durante el día (Brown 2022). Más luz de día se asocia a mejor salud mental (Burns 2023) | "Sal a la luz en cada pausa larga; reuniones por teléfono, caminando y al aire libre" | Brown 2022 `verified`; Burns 2023 `reported` |
| **Dormitorio a oscuras (≤1 lux)** | Recomendación explícita de Brown 2022 | Pregunta del onboarding y consejo sobre persianas o antifaz | Brown 2022 `verified` |
| **Temperatura del dormitorio** | La evidencia en jóvenes es escasa. En mayores de 65, la eficiencia del sueño fue máxima entre 20 y 25 °C (Baniassadi 2023, 50 personas, unas 11.000 noches), y de forma general se aconseja un dormitorio fresco | "Dormitorio fresco y ventilado, ajustado a tu comodidad y a la ropa de cama". Ucoach no da una cifra: el único dato con fuente (20-25 °C) es de mayores de 65, y no hay un rango validado para adultos más jóvenes (corregido tras QA 2026-11-19: se quita el rango de 17-21 °C, que era `inferred`) | Baniassadi A et al. 2023, *Sci Total Environ* 899:165623: https://pubmed.ncbi.nlm.nih.gov/37474050/ `verified` en la QA |
| **Horarios de comida regulares y cena no tardía** | Declaración científica de la AHA (2017); Vujović 2022 | Registrar opcionalmente la hora de las comidas. En la revisión semanal, señalar las cenas tardías o muy irregulares | St-Onge 2017 `reported` |
| **Límite diario de cafeína** | La EFSA (2015) fija 400 mg al día y 200 mg por toma | Contador opcional y aviso | EFSA 2015 `verified` en la QA (presentación oficial de la EFSA) |
| **No obsesionarse con el wearable** | Los wearables estiman razonablemente el tiempo total de sueño, pero fallan en las fases y en la eficiencia. Está descrita la "ortosomnia", la ansiedad por optimizar la puntuación del sueño (Baron et al., 2017, *J Clin Sleep Med*) | No mostrar las fases de sueño como diagnóstico. Si el usuario dice sentirse bien, no contradecirle por la puntuación. Tener un modo "sin números" | Validaciones JMIR 2023 y Baron 2017 (https://pubmed.ncbi.nlm.nih.gov/27855740/), `verified` en la QA |
| **Sueño y conducción** | Inferido de la evidencia general sobre falta de sueño y accidentes | Con menos de 5 h o mucha somnolencia, aviso de no conducir o de hacer una siesta antes | `inferred` |
| **Pareja de ejercicio y sueño** | El ejercicio regular mejora la calidad del sueño (metaanálisis de Kredlow et al., 2015, *J Behav Med*) | Al proponer un hábito de sueño, ofrecer el ejercicio como palanca compatible. Es una excepción razonable a "un hábito cada vez" | Kredlow 2015 (https://pubmed.ncbi.nlm.nih.gov/25596964/) `verified` en la QA |

---

## Biblioteca: avisos que corregir o añadir

### Avisos actuales: comprobación

| Libro | Aviso actual | ¿Correcto? | Redacción propuesta |
|---|---|---|---|
| Mindset (Dweck) | "Algunos estudios de réplica muestran efectos más pequeños de lo popularizado" | Sí, pero se queda corto | "Los metaanálisis encuentran efectos medios muy pequeños de las intervenciones de mentalidad de crecimiento (Sisk 2018; Macnamara y Burgoyne 2023: d≈0,05, que deja de ser significativo tras corregir el sesgo de publicación; corregido tras QA 2026-11-19). Podrían ayudar algo a grupos de riesgo; el debate sigue abierto". Fuente: https://kqed.org/mindshift/60490/does-growth-mindset-matter-the-debate-heats-up-with-dueling-meta-analyses `reported` |
| The Miracle Morning | Levantarse muy temprano no conviene a todos | Sí | Mantener |
| Willpower | El "agotamiento del ego" ha fallado en réplicas | Sí, es exacto | Añadir datos: "Hagger 2016 (23 laboratorios, d=0,04) y Vohs 2021 (36 laboratorios, d=0,06)". https://pmc.ncbi.nlm.nih.gov/articles/PMC4987495 `reported` |
| Stolen Focus | "Algunas conclusiones del libro son discutidas" | Correcto, pero vago | "El propio autor admite que no hay datos a largo plazo de que la atención haya empeorado. La tesis central y algunos capítulos (alimentación, TDAH) se apoyan en anécdotas". https://unherd.com/2022/01/johann-haris-stolen-ideas/ `reported` |
| The Power of When | La clasificación en cuatro animales es divulgativa | Sí | Añadir: "El cuestionario de los animales no está validado; Ucoach usa tres cronotipos y tus propios datos" |
| Why We Sleep | Algunas afirmaciones y cifras han sido criticadas | Sí | Añadir la referencia: "Guzey (2019) documentó errores factuales". https://guzey.com/books/why-we-sleep/ `reported` |
| Say Good Night to Insomnia | Ante insomnio persistente, consulta | Sí | Añadir: "La TCC-I, que el libro explica, es el tratamiento de primera elección según la AASM (2021) y la guía europea (2023)". Es un libro **bien alineado** con la evidencia |
| Sleep Smarter | Divulgativo; contrasta | Sí | Mantener |
| Born to Run | Tesis sobre el calzado discutidas | Sí | Mantener |
| Lifespan (Sinclair) | Tesis y suplementos muy discutidos | Sí | Añadir: "La relación entre resveratrol y sirtuinas no se ha confirmado. No hay ensayos en humanos que muestren que el NMN o el NAD+ alarguen la vida". `reported` |
| Glucose Revolution | Debate sobre los picos en personas sanas | Sí | Mantener |
| How Not to Die | Perspectiva vegetariana | Correcto, pero mal enfocado | "Algunas afirmaciones extrapolan estudios observacionales o de laboratorio más allá de lo que demuestran" (`inferred`) |
| Thinking, Fast and Slow | Algunos estudios citados no se han replicado | Sí | Precisar: "sobre todo el capítulo de *priming*, que el propio Kahneman reconoció". `reported` |
| Breath (Nestor) | Algunas afirmaciones van más allá de la evidencia | Sí | Añadir: "Taparse la boca para dormir no tiene apoyo y conlleva riesgo de asfixia (revisión sistemática de PLOS ONE, 2025)". https://pmc.ncbi.nlm.nih.gov/articles/PMC12094774 `reported` |
| Grit | El poder predictivo frente a la responsabilidad es debatido | Sí | Añadir: "Credé 2017 (88 muestras, unas 67.000 personas): correlación con el rendimiento de r≈0,18 y gran solapamiento con la responsabilidad". https://news.iastate.edu/news/2016/05/18/grit-analysis `reported` |
| Starting Strength | Aprende la técnica con un profesional | Sí (es de seguridad, no de evidencia) | Mantener |

### Libros sin aviso que deberían llevarlo

| Libro | Problema | Aviso propuesto | Confianza |
|---|---|---|---|
| **Atomic Habits** | El "1 % mejor cada día = 37 veces mejor al año" es una cuenta (1,01^365), no un resultado empírico: supone una mejora constante y sin rendimientos decrecientes. El resto del libro (diseñar el entorno, encadenar hábitos) sí encaja con la investigación sobre hábitos | "La regla del 1 % es una metáfora. Formar un hábito tarda una mediana de unos 2 meses (Lally 2010; Singh 2024)" | `inferred` (cuenta) + `verified` (Lally, Singh) |
| **Ikigai** | (1) Los datos de longevidad de Okinawa y las "zonas azules" se discuten por errores de registro y fraude de pensiones (Newman, 2019 y preprint de 2024; los investigadores de las zonas azules lo rebaten). (2) El diagrama de los cuatro círculos es una adaptación occidental, no el concepto japonés original | "Los datos de longevidad de Okinawa están en discusión. El diagrama de los cuatro círculos es una adaptación occidental" | `reported` |
| **The Circadian Code** (Panda) | Las pruebas en humanos de que el ayuno con horario restringido aporte algo más allá de comer menos son modestas (Liu 2022). La alarma de 2024 sobre mortalidad no está demostrada | "En personas, el ayuno con horario restringido no supera a la restricción calórica. La pauta de cenar pronto y con regularidad es la parte más sólida" | `reported` |
| **The Power of Full Engagement** | Se apoya en ciclos ultradianos de 90-120 minutos en vigilia, que no están confirmados | "Los 'ciclos de 90 minutos' en vigilia no están demostrados; alternar esfuerzo y recuperación sí es buena práctica" | `reported` |
| **Peak** (Ericsson) | En el metaanálisis de Macnamara et al. (2014, 88 estudios), la práctica deliberada explica de media el 12 % de las diferencias de rendimiento: 26 % en juegos, 21 % en música, 18 % en deporte, 4 % en educación y menos del 1 % en profesiones | "La práctica deliberada importa, pero explica menos de lo que sugiere el libro, sobre todo en el trabajo profesional" | `verified` (nota de la APS y de Princeton) |
| **Spoon-Fed** (Spector) | La cifra de 30 plantas a la semana viene de una asociación observacional con la diversidad de la microbiota (American Gut Project, 2018), no de resultados de salud | "Las 30 plantas son una regla práctica basada en una asociación con la microbiota, no un umbral probado" | `reported` |
| **Spark** (Ratey) | Los efectos del ejercicio sobre la cognición en adultos sanos son pequeños y en parte se deben al sesgo de publicación (revisión paraguas de Ciria et al., 2023, *Nature Human Behaviour*) | "El ejercicio es bueno para el ánimo y la salud. Sus efectos sobre la cognición en adultos sanos son menores de lo que plantea el libro" | `reported` |
| **The Upside of Stress** (McGonigal) | Se apoya mucho en un estudio observacional (Keller 2012) y en intervenciones sobre la "mentalidad del estrés" con efectos pequeños | "Reinterpretar el estrés puede ayudar algo; el dato sobre mortalidad que cita es observacional" | `reported` |
| **When** (Pink) | Cita el estudio de los jueces israelíes (Danziger 2011), muy discutido por sus factores de confusión | "Algunos estudios citados, como el de los jueces y las pausas, están discutidos" | `reported` |
| **Outlive** (Attia) | El consenso sobre ejercicio y longevidad es sólido. Algunas recomendaciones (fármacos de "longevidad", monitorización continua de glucosa en personas sanas) van por delante de la evidencia | "Lo de ejercicio y fuerza es sólido; lo de fármacos y monitorización, especulativo" | `inferred` |
| **Start with Why** (Sinek) | La explicación biológica del "círculo dorado" (sistema límbico frente a neocórtex) simplifica la neurociencia | "La explicación neurológica es una simplificación; la idea de comunicar el propósito es útil" | `inferred` |
| **Deskbound** (Starrett) | La relación entre una postura concreta y el dolor es débil en la literatura; moverse sí ayuda | "Moverse a menudo es lo importante; no hay una postura 'correcta' demostrada" | `inferred` |
| **Burnout** (Nagoski) | "Completar el ciclo del estrés" es un marco divulgativo, no un constructo validado | "Es un marco útil, no un modelo científico; ante el agotamiento persistente, consulta" | `inferred` |

**Nota:** no hay ningún libro de Huberman en la biblioteca, pero la regla del primer café a los 75 minutos viene de su divulgación. Conviene quitarla (punto 3a), no solo avisar.

---

## Índice de fuentes

**Sueño, regularidad e insomnio**
1. Watson NF et al. 2015. Consenso AASM/SRS sobre la duración del sueño. https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf `verified`
2. Hirshkowitz M et al. 2015. Recomendaciones de duración de la NSF, *Sleep Health*. https://www.sciencedaily.com/releases/2015/02/150202123716.htm `verified`
3. Cappuccio FP et al. 2010. Duración del sueño y mortalidad, *Sleep*. https://wrap.warwick.ac.uk/5980/ `verified` en la QA
4. Windred DP et al. 2024. Regularidad del sueño y mortalidad, *Sleep*. https://researchnow.flinders.edu.au/en/publications/sleep-regularity-is-a-stronger-predictor-of-mortality-risk-than-s/ `verified`
5. Sletten TL et al. 2023. Consenso de la NSF sobre regularidad, *Sleep Health*. https://pubmed.ncbi.nlm.nih.gov/37684151/ `verified`
6. Arab A et al. 2024. Jet lag social y obesidad, *Obesity Reviews*. https://pubmed.ncbi.nlm.nih.gov/38072635 `verified` en la QA
7. Edinger JD et al. 2021. Guía AASM sobre tratamientos conductuales del insomnio. https://aasm.org/new-guideline-supports-behavioral-psychological-treatments-for-insomnia/ `verified`
8. Riemann D et al. 2023. Guía europea del insomnio, *J Sleep Res*. https://pubmed.ncbi.nlm.nih.gov/38016484/ `verified` en la QA
9. Brooks A, Lack L. 2006. Duración de la siesta, *Sleep*. https://pubmed.ncbi.nlm.nih.gov/16796222/ `verified`
10. Dutheil F et al. 2021. Metaanálisis sobre siestas (media de 55 min), *IJERPH*. https://pubmed.ncbi.nlm.nih.gov/34639511/ `verified`
11. Baniassadi A et al. 2023. Temperatura nocturna y sueño en mayores, *Sci Total Environ*. https://pubmed.ncbi.nlm.nih.gov/37474050/ `verified` en la QA
12. Chung F et al. 2016. STOP-Bang, *Chest*. https://pubmed.ncbi.nlm.nih.gov/26378880/ `verified` en la QA (corregido tras QA 2026-11-19: PMC4008971 es la validación de Boynton 2013)
13. Lee T et al. 2023. Validación de wearables de sueño, *JMIR mHealth*. https://pubmed.ncbi.nlm.nih.gov/37917155/ `verified` en la QA

**Luz y pantallas**
14. Brown TM et al. 2022. Recomendaciones de luz, *PLOS Biology*. https://pmc.ncbi.nlm.nih.gov/articles/PMC8929548 `verified`
15. Wright KP et al. 2013. Camping y reloj circadiano, *Current Biology*. https://www.sciencealert.com/how-a-week-of-camping-resets-the-body-clock `reported`
16. Burns AC et al. 2023. Luz y trastornos psiquiátricos, *Nature Mental Health*. https://www.nationalelfservice.net/mental-health/depression/associations-between-daily-light-exposure-and-psychiatric-disorders/ `reported`
17. Hartstein LE et al. 2024. Consenso de la NSF sobre pantallas y sueño, *Sleep Health*. https://www.colorado.edu/today/2024/05/28/light-or-content-what-we-know-about-screens-and-sleep-disruption `verified`
18. Chang AM et al. 2015. eReaders y sueño, *PNAS*. https://pubmed.ncbi.nlm.nih.gov/25535358/ `verified`

**Cafeína y alcohol**
19. Gardiner C et al. 2023. Cafeína y sueño, metaanálisis, *Sleep Med Rev*. https://eprints.leedsbeckett.ac.uk/id/eprint/9625/ `verified`
20. Drake C et al. 2013. Cafeína 0, 3 y 6 h antes de dormir, *J Clin Sleep Med*. https://pmc.ncbi.nlm.nih.gov/articles/PMC3805807 `verified`
21. Lovallo WR et al. 2005. Cafeína y cortisol en consumidores habituales, *Psychosom Med*. https://pubmed.ncbi.nlm.nih.gov/16204431/ `verified` en la QA
22. EFSA 2015. Dictamen sobre la seguridad de la cafeína. https://efsa.onlinelibrary.wiley.com/doi/10.2903/j.efsa.2015.4102 · presentación oficial: https://www.efsa.europa.eu/sites/default/files/event/documentset/150305-p02.pdf `verified` en la QA
23. Gardiner C et al. 2025. Alcohol y sueño, metaanálisis, *Sleep Med Rev*. https://pubmed.ncbi.nlm.nih.gov/39631226/ `verified` en la QA

**Foco, cronotipo, pausas y reuniones**
24. Chauhan S et al. 2025. Cronotipo y sincronía, revisión sistemática, *Chronobiol Int*. https://researchinnovation.kingston.ac.uk/en/publications/chronotype-and-synchrony-effects-in-human-cognitive-performance-a/ `reported`
25. Ritmos ultradianos en vigilia, revisiones. https://pubmed.ncbi.nlm.nih.gov/30454601/ y https://pubmed.ncbi.nlm.nih.gov/28349079/ `verified` en la QA (corregido tras QA 2026-11-19: el DOI 10.1007/978-1-4020-8352-5_13 es un capítulo de LaJambe y Brown sobre privación de sueño)
26. Albulescu P et al. 2022. Micropausas, metaanálisis, *PLOS ONE*. https://doaj.org/article/c6f37b6ba159469296b2cb968b65505f `verified`
27. Microsoft Human Factors Lab 2021. EEG y reuniones seguidas. https://www.microsoft.com/en-us/worklab/work-trend-index/brain-research `verified`
28. Buffey AJ et al. 2022. Romper el sedentarismo, *Sports Med*. https://www.pubmed.gov/35147898/ `verified` en la QA
29. Metaanálisis de 2025 sobre pausas activas en obesidad, *Front Nutr*. https://pubmed.ncbi.nlm.nih.gov/41356824/ `verified` en la QA
30. Talens-Estarelles C et al. 2023. Prueba de la regla 20-20-20, *Cont Lens Anterior Eye*. https://pubmed.ncbi.nlm.nih.gov/35963776/ `verified` en la QA
31. Johnson S, Rosenfield M. 2023. "20-20-20 Rule: Are These Numbers Justified?", *Optom Vis Sci*. https://pubmed.ncbi.nlm.nih.gov/36473088/ `verified` en la QA
32. American Academy of Ophthalmology (2020). Fatiga visual digital. https://aao.org/newsroom/news-releases/detail/protect-your-eyes-in-home-office `reported` (bloqueada en la QA)

**Ejercicio**
33. Bull FC et al. 2020. Directrices de la OMS, *BJSM*. https://digibug.ugr.es/handle/10481/66573 `verified`
34. Paluch AE et al. 2022. Pasos y mortalidad, *Lancet Public Health*. https://doaj.org/article/c3639c468b4348958202e52793ab979d `verified`
35. Ding D et al. 2025. Pasos y salud, *Lancet Public Health*. https://www.sciencedaily.com/releases/2025/07/250726234359.htm `verified`
36. Craven J et al. 2022. Falta de sueño y rendimiento físico, *Sports Med*. https://read.qxmd.com/read/35708888/ `verified`
37. Manresa-Rocamora A et al. 2021. Entrenamiento guiado por VFC, metaanálisis, *IJERPH*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8507742/ `verified` en la QA · Granero-Gallegos A et al. 2020, VO2máx, *IJERPH*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7663087/ `verified` en la QA (corregido tras QA 2026-11-19)
38. Düking P et al. 2021. VFC con wearables, *J Sci Med Sport*. https://pubmed.ncbi.nlm.nih.gov/34489178/ `verified` en la QA
39. Milewski MD et al. 2014. Sueño y lesiones, *J Pediatr Orthop*. https://pubmed.ncbi.nlm.nih.gov/25028798/ `reported`

**Alimentación**
40. Fujiwara Y et al. 2005. Intervalo entre la cena y la cama y reflujo, *Am J Gastroenterol*. https://pubmed.ncbi.nlm.nih.gov/16393212/ `verified`
41. St-Onge MP et al. 2017. Declaración de la AHA sobre horario de comidas, *Circulation*. https://professional.heart.org/en/science-news/meal-timing-and-frequency-implications-for-cardiovascular-disease-prevention `reported`
42. Vujović N et al. 2022. Comer tarde, *Cell Metab*. https://news.harvard.edu/gazette/story/2022/10/study-looks-at-why-late-night-eating-increases-obesity-risk `reported`
43. Abstract de la AHA 2024 sobre comer en menos de 8 h y mortalidad cardiovascular. https://newsroom.heart.org/news/8-hour-time-restricted-eating-linked-to-a-91-higher-risk-of-cardiovascular-death `verified` en la QA · estudio completo: Chen M et al. 2025, *Diabetes Metab Syndr*. https://pubmed.ncbi.nlm.nih.gov/40849219/ `verified` en la QA (corregido tras QA 2026-11-19)
44. Revisión paraguas de 2025 sobre ayuno con horario restringido, *Diabetes Obes Metab*. https://pubmed.ncbi.nlm.nih.gov/39618023/ `verified` en la QA
45. Liu D et al. 2022. Ayuno con horario restringido más restricción calórica, *NEJM*. https://pubmed.ncbi.nlm.nih.gov/35443107/ `verified` en la QA
46. Garaulet M et al. 2013. Horario de la comida y pérdida de peso, *Int J Obes*. https://pubmed.ncbi.nlm.nih.gov/23357955/ `verified` en la QA

**Ergonomía**
47. INSST. Preguntas frecuentes sobre trabajo con ordenadores. https://www.insst.es/materias/riesgos/riesgos-ergonomicos/trabajo-con-ordenadores/faq `reported`
48. Hoe VCW et al. 2018. Intervenciones ergonómicas, *Cochrane*. https://www.cochrane.org/CD008570 `verified`
49. Shrestha N et al. 2018. Reducir el tiempo sentado en el trabajo, *Cochrane*. https://doi.org/10.1002/14651858.CD010912.pub5 `verified` en la QA (corregido tras QA 2026-11-19: el enlace de cochranelibrary.com bloquea a los robots)

**Hábitos y cambio de conducta**
50. Lally P et al. 2010. Formación de hábitos, *Eur J Soc Psychol*. https://www.ucl.ac.uk/news/2009/aug/how-long-does-it-take-form-habit `verified`
51. Singh B et al. 2024. Tiempo para formar un hábito, *Healthcare*. https://www.eurekalert.org/news-releases/1071242 `verified`
52. James E et al. 2016. Cambio secuencial frente a simultáneo, *Prev Med*. https://www.pubmed.gov/27311332/ `reported`

**Biblioteca**
53. Credé M et al. 2017. Metaanálisis sobre el grit, *JPSP*. https://news.iastate.edu/news/2016/05/18/grit-analysis `reported`
54. Macnamara BN, Burgoyne AP. 2023. Mentalidad de crecimiento, *Psychol Bull*. https://kqed.org/mindshift/60490/does-growth-mindset-matter-the-debate-heats-up-with-dueling-meta-analyses `reported`
55. Hagger MS et al. 2016 y Vohs KD et al. 2021. Réplicas del agotamiento del ego. https://pmc.ncbi.nlm.nih.gov/articles/PMC4987495 `reported`
56. Macnamara BN et al. 2014. Práctica deliberada, *Psychol Sci*. https://www.psychologicalscience.org/news/releases/becoming-an-expert-takes-more-than-practice.html `verified`
57. Guzey A. 2019. Errores de *Why We Sleep*. https://guzey.com/books/why-we-sleep/ `reported`
58. Newman S y la polémica de las zonas azules (2024). https://fortune.com/europe/2024/12/14/are-blue-zones-myth-extreme-aging-pension-fraud-century-old-lies/ `reported`
59. Revisión sistemática sobre taparse la boca para dormir, *PLOS ONE* 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12094774 `reported`
60. Ritchie S. 2022. Crítica de *Stolen Focus*. https://unherd.com/2022/01/johann-haris-stolen-ideas/ `reported`
61. Críticas a Sinclair y a la hipótesis resveratrol-sirtuinas. https://nautil.us/the-longevity-skeptic-305806/ `reported`
62. Ciria LF et al. 2023. Revisión paraguas sobre ejercicio y cognición, *Nature Human Behaviour*. https://pubmed.ncbi.nlm.nih.gov/36973359/ `verified` en la QA
63. Kredlow MA et al. 2015. Ejercicio y sueño, metaanálisis, *J Behav Med*. https://pubmed.ncbi.nlm.nih.gov/25596964/ `verified` en la QA
64. Baron KG et al. 2017. Ortosomnia, *J Clin Sleep Med*. https://pubmed.ncbi.nlm.nih.gov/27855740/ `verified` en la QA

**Fuentes que se citaban sin entrada en el índice (añadidas tras la QA 2026-11-19)**
65. Sisk VF et al. 2018. Mentalidad de crecimiento, *Psychol Sci*. https://pubmed.ncbi.nlm.nih.gov/29505339/ `verified` en la QA
66. Macnamara BN, Burgoyne AP. 2023. Mentalidad de crecimiento, *Psychol Bull*. https://pubmed.ncbi.nlm.nih.gov/36326645/ `verified` en la QA
67. Meader N et al. 2017. Cambio de múltiples conductas, *Am J Prev Med*. https://pubmed.ncbi.nlm.nih.gov/28258777/ `verified` en la QA
68. Silva CC et al. 2024. Intervenciones de múltiples conductas en enfermedades crónicas, *Ann Behav Med*. https://pubmed.ncbi.nlm.nih.gov/38721982/ `verified` en la QA
69. Gardner B et al. 2012. SRBAI, *IJBNPA*. https://pubmed.ncbi.nlm.nih.gov/22935297/ `verified` en la QA
70. Keller A et al. 2012. Percepción del estrés y mortalidad, *Health Psychol*. https://pubmed.ncbi.nlm.nih.gov/22201278/ `verified` en la QA
71. Danziger S et al. 2011. Jueces israelíes, *PNAS*, y sus críticas. https://pubmed.ncbi.nlm.nih.gov/21482790/ · https://daniellakens.blogspot.com/2017/07/impossibly-hungry-judges.html `verified` en la QA
72. Newman SJ 2019. Preprint sobre supercentenarios y zonas azules. https://www.biorxiv.org/content/10.1101/704080v1 `verified` en la QA
73. Hagger 2016 y Vohs 2021, en PubMed: https://pubmed.ncbi.nlm.nih.gov/27474142/ · https://pubmed.ncbi.nlm.nih.gov/34520296/ `verified` en la QA
74. Credé M et al. 2017, en PubMed: https://pubmed.ncbi.nlm.nih.gov/27845531/ `verified` en la QA

**Limitaciones de este informe:** la primera versión no pudo abrir Liu 2022, Garaulet 2013, la EFSA 2015, Ciria 2023, Kredlow 2015 y Baron 2017. Un verificador independiente las comprobó todas en la QA de 2026-11-19, y las cifras coinciden (corregido tras QA 2026-11-19). Siguen sin abrirse la web de la AAO (bloqueada) y los resultados de Burns 2023. Falta revisar a qué poblaciones no se aplican estas reglas (embarazo, trabajo a turnos, mayores de 60) y buscar una fuente para la regla de conducción.
