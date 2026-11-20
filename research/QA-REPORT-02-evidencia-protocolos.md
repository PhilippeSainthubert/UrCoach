---
kind: qa-report
target: 02-evidencia-protocolos.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 9.3
score_limited_by: cobertura
score_before_fix: 0.0
coverage_claims: 95
coverage_verified: 73
independent: true
sources: 97
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 02 · Evidencia científica de las reglas y protocolos

## Nota: 0.0 / 10 · REHACER antes de corregir; tras las correcciones, 9.3 · ENTREGABLE (ver «Re-verificación»)

La nota la limitan los hallazgos, no la cobertura: el techo por cobertura es 8,26. La penalización suma 20,75 puntos:
- un bloqueo de enlace: 2 puntos;
- dos críticas: 6 puntos;
- siete medias: 7 puntos;
- veintitrés bajas: 5,75 puntos.

Las dos críticas son pautas que Ucoach daría al usuario y que contradicen la fuente que el propio informe cita y da por verificada: la hora límite del café y el plazo para bajar la luz por la noche. Las dos se arreglan cambiando una cifra en tres o cuatro líneas. El fondo científico del informe aguanta bien: 40 de las 47 afirmaciones portantes coinciden con la verificación independiente.

Cálculo: `nota.py --claims 95 --verificadas 73 --portantes 47 --portantes-ok 40 --criticas 2 --medias 7 --bajas 23 --bloqueos 1` → 0.0, REHACER.

**Modo**: Deep · **Tipo**: research de evidencia científica · **Fecha**: 2026-11-19
**Independencia**: el verificador trabajó en un contexto separado ✓. No vio el informe ni el mapa, y contestó 76 preguntas neutras (`qa/B-preguntas.md`) con fuentes que abrió en su sesión: PubMed y PMC a través de las E-utilities, Crossref, BOE, OMS y otras.
**Método**: Chain of Verification. Extractor (`qa/B-mapa.md`), verificador (`qa/B-respuestas.md`) y comparación en este informe. `searches: 0` se refiere a esta fase de comparación.
**Rúbricas**: ⚠ en esta pasada no se cargaron `_base` ni la rúbrica de research de g4u-brain. Ucoach no tiene una rúbrica propia de cliente.

## Cobertura

| | |
|---|---|
| Afirmaciones verificables estimadas en el documento | entre 180 y 200 |
| Afirmaciones contadas (C = máx(95 del preflight, 76 extraídas)) | 95 |
| Extraídas y preguntadas | 76 (47 portantes y 29 de apoyo) |
| Verificadas con fuente consultada, incluidas las refutadas | 73 |
| Sin fuente útil | B02-24 (no localizado), B02-34 (aao.org bloqueado) y B02-55 (solo fuentes secundarias) |
| Portantes que aguantan | 40 de 47 |

Clasificación por id:

| Clase | ids |
|---|---|
| VERIFIED | 01, 03, 05, 06, 07, 09, 10, 12, 14, 16, 17, 18, 19, 22, 23, 25, 26, 27, 30, 31, 32, 33, 37, 38, 39, 40, 41, 42, 46, 47, 48, 50, 51, 52, 55, 56, 57, 58, 59, 60, 61, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75, 76 |
| VERIFIED con hallazgo de procedencia o de año (baja) | 02, 08, 35, 36, 49, 62, 63 |
| ERROR | 28, 29 (PMC8507742 atribuido a otro artículo) |
| STALE | 45 (el estudio completo de la AHA ya está publicado) |
| OVERCLAIM | 15 (Lovallo: «eliminaron») |
| DISCREPANCY | 20 (Dutheil), 43 (revisión paraguas), 53 (RD 488/1997), 54 (Shrestha), 67 (Macnamara y Burgoyne) |
| UNVERIFIABLE | 04 (el error del TST), 11 (el «1 %»), 13 (resultados de Burns), 24 («otro metaanálisis»), 34 (AAO, 46-64 cm), 44 (el «60 % más de fumadores») |
| INTERNAL | C02-01 a C02-11 y X-01, X-03 y X-05 del mapa (ver Hallazgos) |
| MISSING | poblaciones especiales y la fuente de la regla de conducción |

## Veredicto

**Tras corregir: ENTREGABLE** (`PASS`, 9.3), ver «Re-verificación». Antes de corregir era **REHACER** (`MAJOR ISSUES`), por dos críticas abiertas y un enlace roto. No hay que rehacer el informe, sino cuatro grupos de líneas:
- la regla de la cafeína: l. 19, 40 y 144;
- el plazo de la luz nocturna: l. 124;
- la atribución de PMC8507742: l. 45, 196, 198 y 466;
- el abstract de la AHA de 2024: l. 53, 267 y 271.

Con eso y las medias corregidas, el informe es entregable.

## Bloqueos deterministas (preflight)

| # | Enlace | Línea | Estado | Qué vio el verificador | Corrección |
|---|---|---|---|---|---|
| B1 | https://cms.ahs.uic.edu/inside-ahs/wp-content/uploads/sites/12/2024/04/Collective-Reponse-to-AHA-press-release-on-TRE.pdf | 271 | sin respuesta (roto) | Encontró la nota de la UIC sobre los 34 expertos (B02-45) | Sustituir por https://ahs.uic.edu/inside-ahs/news/ y añadir el estudio completo, https://pubmed.ncbi.nlm.nih.gov/40849219/ |
| (no bloqueo) | cochranelibrary.com, CD010912.pub5 | 332, 482 | 412 (bloqueo a robots) | Lo abrió en PubMed 30556590 | Sustituir por https://doi.org/10.1002/14651858.CD010912.pub5 |
| (no bloqueo) | ucl.ac.uk/news/2009/aug/... | 347, 485 | 403 (bloqueo a robots) | Crossref, 10.1002/ejsp.674 | Se mantiene |

## Contrato de escritura y voz

- **Script de-slop**: no disponible en esta máquina. Las pruebas contables (frases largas, párrafos de más de cuatro líneas, ritmo, patrones) **no se han comprobado**; eso no significa que las pase.
- **Guiones largos**: 0 (comprobado con `grep` de U+2014 y U+2013 tras la limpieza del coordinador).
- **Voz**: castellano de España, de tú en las pautas al usuario. La narrativa de proceso de la l. 5 («se agotó el cupo») declara un límite y es útil.

## Hallazgos por gravedad

### Críticas

**H-C1 · INTERNAL · crítica · La regla del café queda por debajo del umbral de Gardiner**
- **Dice**:
  - l. 19: «La del último café 8 horas antes de dormir sí está bien fundada: el metaanálisis de Gardiner (2023) da 8,8 h para un café y 13,2 h para un preentreno».
  - l. 40: veredicto «Sólido», cambio «Pasar a 8-9 h para un café y 12-13 h para dosis altas».
  - l. 144: «café o té, de 8 a 9 h antes de dormir; dosis altas [...] de 12 a 13 h».
- **Verificación independiente** (B02-16, https://pubmed.ncbi.nlm.nih.gov/36870101/): Gardiner et al. (2023), con 24 estudios, dan como mínimo **8,8 h** para un café (107 mg) y **13,2 h** para un preentreno (217,5 mg). La cafeína quita 45 min de sueño total y 11,4 min de sueño profundo.
- **Por qué es crítica**: es la hora límite que Ucoach calcula cada día. Las 8 h y las 12-13 h quedan por debajo de los mínimos que el informe da por verificados.
- **Corrección**: al menos 9 h para un café o té y al menos 13,5 h para dosis altas, citando las cifras de Gardiner (8,8 h y 13,2 h). Veredicto 3b: «Sólido en la dirección; 8 h se queda corta».

**H-C2 · INTERNAL · crítica · La luz de la noche se baja 2 h antes, y la fuente pide 3 h**
- **Dice**: l. 124: «adelantar el aviso de "bajar luces" a **2 o 3 horas antes**». Choca con el resumen (l. 20), la tabla (l. 38) y la evidencia (l. 122), que dicen 3 h.
- **Verificación independiente** (B02-10, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8929548/): Brown et al. (2022) piden un máximo de 10 lux mEDI «starting at least 3 hours before bedtime».
- **Corrección**: l. 124, «a **3 horas antes**».

### Medias

**H-M1 · ERROR · media · PMC8507742 no es Granero-Gallegos 2020 (X-01)**
- **Dice**: l. 196: «en el metaanálisis de Granero-Gallegos et al. (2020), el entrenamiento guiado por VFC obtuvo efectos [...] no significativos [...] en VO2máx (SMD 0,20) y rendimiento (SMD 0,20), y un efecto mayor en los propios índices vagales». Fuente en la l. 198 y en el índice (l. 466): PMC8507742.
- **Verificación independiente**:
  - B02-29: PMC8507742 corresponde a **Manresa-Rocamora et al. (2021)**, IJERPH 18(19):10299, PMID 34639599 (https://pubmed.ncbi.nlm.nih.gov/34639599/). Esas cifras son suyas: índices vagales 0,50; VO2máx y rendimiento 0,20, no significativos.
  - B02-28: Granero-Gallegos et al. (2020), IJERPH 17(21):7999, PMC7663087, solo analiza el VO2máx y encuentra una ventaja pequeña del grupo guiado por VFC (ES 0,187). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7663087/
- **Por qué es media**: el veredicto 6b (débil o razonable) aguanta con la fuente correcta, pero la cita es falsa.
- **Corrección**: atribuir las cifras a Manresa-Rocamora 2021 en las l. 45, 196, 198 y 466, y añadir Granero-Gallegos 2020 con su PMCID real.

**H-M2 · STALE · media · El estudio de la AHA sobre ventanas de comida cortas ya está publicado**
- **Dice**: l. 267: «en esta búsqueda no apareció ninguna publicación completa revisada por pares»; l. 53: «El dato de 2024 sobre mortalidad no es fiable».
- **Verificación independiente** (B02-45): Chen M, ..., Zhong VW, *Diabetes Metab Syndr* 2025;19(7):103278 (https://pubmed.ncbi.nlm.nih.gov/40849219/). Con n=19.831 y referencia de 12-14 h, el **HR cardiovascular es 2,35** (1,39-3,98). La asociación con la mortalidad total no resiste los análisis de sensibilidad, y los autores admiten posible confusión residual.
- **Corrección**: decir que el estudio completo existe, es observacional y admite confusión residual. El consejo («no recomendar por defecto») se mantiene.

**H-M3 · OVERCLAIM · media · Lovallo: la respuesta del cortisol se reduce, pero no desaparece**
- **Dice**: l. 130: «5 días con 300-600 mg al día **eliminaron** la respuesta de cortisol a la dosis de las 9:00».
- **Verificación independiente** (B02-15, https://pubmed.ncbi.nlm.nih.gov/16204431/): la respuesta desaparece tras la dosis de las 9:00, pero el cortisol vuelve a subir tras la de las 13:00 («reduced, but not eliminated»).
- **Corrección**: añadir que la tolerancia es parcial.

**H-M4 · DISCREPANCY · media · Dutheil 2021 no trata de siestas cortas**
- **Dice**: l. 150: «encuentra mejoras cognitivas tras siestas cortas, sobre todo en el estado de alerta, que duran unas 2 horas».
- **Verificación independiente** (B02-20, https://pubmed.ncbi.nlm.nih.gov/34639511/): 11 estudios con 381 participantes; **siesta media de 55 min**; ES global 0,18, alerta 0,29; efecto hasta unos 120 min. Las siestas antes de las 13:00 rinden más.
- **Corrección**: describir la muestra real. La base de la siesta corta es Brooks y Lack.

**H-M5 · DISCREPANCY · media · La revisión paraguas de 2025 no dice que la mayoría de las revisiones sean de calidad baja**
- **Dice**: l. 266: «la mayoría de las revisiones que reúnen son de calidad baja o críticamente baja».
- **Verificación independiente** (B02-43, https://pubmed.ncbi.nlm.nih.gov/39618023/): 12 metaanálisis evaluados con AMSTAR-2 y GRADE; evidencia de **calidad alta** de que el horario restringido reduce peso, grasa, insulina en ayunas y HbA1c en adultos con sobrepeso. Pide estudios a largo plazo. El abstract no da el reparto de calidad.
- **Corrección**: reescribir la viñeta. La conclusión (no supera a la restricción calórica, según Liu 2022) se mantiene.

**H-M6 · INTERNAL · media · Las pausas «cada 30-45 min» no siguen a la evidencia, que es de adultos con obesidad**
- **Dice**: l. 22 y 206 hablan de cada 30 min o menos; la tabla (l. 46) y el cambio (l. 212) proponen «cada 30-45 minutos».
- **Verificación independiente** (B02-32, https://pubmed.ncbi.nlm.nih.gov/41356824/): población **con obesidad**, 17 ensayos; pausas «about every ≤30 min with 2-5 min». Buffey 2022: participantes sobre todo con sobrepeso (https://pubmed.ncbi.nlm.nih.gov/35147898/).
- **Corrección**: «cada 30 min aproximadamente», indicando la población.

**H-M7 · INTERNAL · media · La temperatura del dormitorio no cuadra con su única fuente**
- **Dice**: l. 365: «en torno a 17-21 °C» (`inferred`), con Baniassadi 2023 como evidencia.
- **Verificación independiente** (B02-64, https://pubmed.ncbi.nlm.nih.gov/37474050/): 50 mayores en sus casas, 10.903 noches; la mejor eficiencia está entre 20 y 25 °C.
- **Corrección**: quitar la cifra de 17-21 °C de la pauta y dejar «fresco, ajustado a tu comodidad». Mantener el dato de Baniassadi como lo que es: un dato de mayores.

### Bajas

| id | Clase | Dice (línea) | Verificación independiente | Corrección |
|---|---|---|---|---|
| H-B1 | PROVENANCE | «Su revisión a diez años reafirmó esos rangos» sin fuente (l. 71) | NSF, *Sleep Health* 2026;12(4):599-611: 133 metaanálisis, «re-certifies» las recomendaciones (https://pubmed.ncbi.nlm.nih.gov/42248743/) | Añadir la cita |
| H-B2 | UNVERIFIABLE | «errores de decenas de minutos en el tiempo total de sueño» (l. 80) | Lee et al., JMIR 2023: 11 dispositivos; F1 de las fases entre 0,26 y 0,69; el abstract no da el error del tiempo total (https://pubmed.ncbi.nlm.nih.gov/37917155/) | Usar la cifra de las fases |
| H-B3 | DISCREPANCY | Arab et al. «2023» (l. 97) | *Obes Rev* 2024;25(3):e13664, en línea en diciembre de 2023 (https://pubmed.ncbi.nlm.nih.gov/38072635/) | 2024 |
| H-B4 | UNVERIFIABLE | «la de una oficina es menos del 1 % de la de un día de verano» (l. 111) | Brown 2022 solo dice «at least 1 order of magnitude below» (PMC8929548) | «al menos diez veces menor» |
| H-B5 | UNVERIFIABLE | Resultados de Burns 2023 (l. 111) | Solo se confirma que el artículo existe (https://api.crossref.org/works/10.1038/s44220-023-00135-8) | Marcar «resultados no verificados» |
| H-B6 | PROVENANCE | BRAC: Wikipedia y el DOI 10.1007/978-1-4020-8352-5_13 (l. 165, 452) | Ese DOI es LaJambe y Brown 2008, ritmos cognitivos en privación de sueño. Lo confirman PubMed 30454601 y 28349079 | Cambiar las fuentes |
| H-B7 | UNVERIFIABLE | «Otro metaanálisis detectó sesgo de publicación» (l. 171) | No localizado (B02-24) | Quitar |
| H-B8 | UNVERIFIABLE | AAO: «sentarse a 46-64 cm» (l. 218, 315) | La AAO dice «at arm's length, about 25 inches», unos 63 cm; aao.org no se pudo abrir (B02-34) | «a un brazo, unos 63 cm» (`reported`) |
| H-B9 | DISCREPANCY | Talens-Estarelles «2022», Johnson y Rosenfield «2022» (l. 47, 218, 220, 221, 457, 458) | *Cont Lens Anterior Eye* 2023;46(2):101744 (https://pubmed.ncbi.nlm.nih.gov/35963776/); *Optom Vis Sci* 2023;100(1):52-56 (https://pubmed.ncbi.nlm.nih.gov/36473088/) | 2023 |
| H-B10 | UNVERIFIABLE | «el grupo de menos de 8 h tenía un 60 % más de fumadores» (l. 267) | No consta en lo que se abrió (B02-44) | Marcar «no verificado» |
| H-B11 | PROVENANCE | «La OMS no fija un nivel seguro» sin fuente (l. 55) | https://www.who.int/europe/news/item/04-01-2023-no-level-of-alcohol-consumption-is-safe-for-our-health | Añadir |
| H-B12 | DISCREPANCY | Atribuye la colocación de la pantalla al «RD 488/1997 y notas técnicas del INSST»; «40 cm o más (INSST)» (l. 313-315) | El RD no da ángulo ni distancia. La guía técnica del INSST de 2021 dice 0-40° bajo la horizontal y nunca a menos de 300 mm (habitual, 400-750 mm); la NTP 251, al menos 40 cm (https://www.boe.es/buscar/act.php?id=BOE-A-1997-8671) | Precisar la fuente |
| H-B13 | DISCREPANCY | Shrestha: «calidad muy baja», «entre 84 y 116 min» (l. 331) | Unos 100 min al día a corto plazo (IC 84-116), con **calidad baja**; unos 57 min a medio plazo; la revisión **no evalúa** beneficios para la salud (https://pubmed.ncbi.nlm.nih.gov/30556590/) | Corregir |
| H-B14 | PROVENANCE | «Revisión STOP-Bang» = PMC4008971 (l. 362, 433) | PMC4008971 es la validación de Boynton 2013. Los umbrales están en Chung 2016, *Chest* (https://pubmed.ncbi.nlm.nih.gov/26378880/) | Cambiar la fuente |
| H-B15 | PROVENANCE | 024 sin fuente (l. 362) | Funciona desde el 10-5-2022 (https://www.sanidad.gob.es/gabinete/notasPrensa.do?id=5739) | Añadir |
| H-B16 | DISCREPANCY | «d≈0,05 tras corregir el sesgo» (l. 380) | d=0,05 sin corregir; tras la corrección, no significativo (https://pubmed.ncbi.nlm.nih.gov/36326645/) | Corregir |
| H-B17 | INTERNAL (C02-01) | l. 5: «Tres fuentes de apoyo» sin abrir. La l. 503 cuenta cuatro, y Liu, Garaulet y la EFSA son portantes | El verificador abrió Liu, Garaulet, la EFSA, Ciria, Kredlow y Baron | Actualizar la nota de método y las etiquetas |
| H-B18 | INTERNAL (C02-02) | `reported` incluye «mi conocimiento previo» (l. 9) | n. a. | Aclararlo en la definición |
| H-B19 | INTERNAL (C02-07) | Hora fija «Sólido» por la TCC-I (l. 35, 89) | La guía AASM es para insomnio crónico (B02-05) | Matizar la población |
| H-B20 | INTERNAL (C02-09) | Sin entrada en el índice: Sisk 2018, Meader 2017, Silva 2024, Gardner 2012, Keller 2012, Danziger 2011, Newman 2019 | El verificador las localizó (B02-59, 60, 67, 72, 76) | Añadirlas al índice |
| H-B21 | INTERNAL (C02-10) | Mantiene el margen hasta las 15:30 aunque Garaulet corta a las 15:00 (l. 248) | Garaulet verificado: corte a las 15:00 (https://pubmed.ncbi.nlm.nih.gov/23357955/) | Decisión de producto explícita: se acepta y no se cambia |
| H-B22 | INTERNAL (X-03) | Recomienda «brillo bajo y modo noche» (l. 282, 339) | El informe 07 deja el modo noche en C; Nagare 2019: cambiar el tono sin bajar el brillo «may be insufficient» (https://pubmed.ncbi.nlm.nih.gov/31191118/) | Poner el brillo en primer lugar y el modo noche como complemento |
| H-B23 | MISSING | No hay poblaciones especiales (embarazo, turnos, mayores de 60) y la regla de conducción no tiene fuente (l. 369) | n. a. | Pendiente de una nueva búsqueda |

## Sólido

El núcleo del informe coincide con la verificación independiente:
- Sueño: Watson, Cappuccio, Edinger 2021, Sletten 2023, Windred 2024, Riemann 2023.
- Luz: Brown 2022 (los dos umbrales), Wright 2013.
- Cafeína: Gardiner 2023, Drake, EFSA 2015; la ausencia de ensayos sobre retrasar el café.
- Siesta, foco y cronotipo: Brooks y Lack, Albulescu 2022, Chauhan 2025, Craven 2022.
- Pausas y actividad: Buffey 2022, el metaanálisis de 2025 en *Front Nutr*, las guías de la OMS 2020, Paluch 2022, Ding 2025.
- Ojos y reuniones: Talens-Estarelles, Johnson y Rosenfield, Microsoft 2021.
- Comida: Garaulet, St-Onge, Fujiwara, Liu.
- Pantallas y alcohol: Hartstein 2024, Chang 2015, Gardiner 2025 (alcohol).
- Ergonomía: Hoe 2018.
- Hábitos: Lally, Singh 2024, James 2016.
- STOP-Bang (umbrales), 024.
- Avisos de la biblioteca: Credé, Hagger y Vohs, Macnamara 2014, Ciria 2023, Guzey, Hari, Kahneman, Danziger, Keller, Newman.

Las cifras exactas de mayor riesgo también coinciden: 60.977 y 20-48 %; 8,8 y 13,2 h; 7,56 %; 45 y 83 %; 47.471; 7.000 pasos con −47 % y −38 %; 66 días; 59-66 días.

## No verificable

- **B02-24**: no se localizó ningún metaanálisis del efecto de sincronía con sesgo de publicación, así que se quita.
- **B02-34**: la web de la AAO bloqueó la lectura; la distancia se da por fragmentos de sus notas.
- **B02-55**: la cifra de Mindlab solo aparece en fuentes secundarias. El informe ya dice que no debe citarse.
- **Subdatos**:
  - Burns 2023 (resultados);
  - Chang 2015 (n=12 y las 4 h, de memoria y coincidentes);
  - la mediana de 66 días de Lally (de memoria y coincidente);
  - el 12 % global de Macnamara 2014;
  - el «60 % más de fumadores».

## Falta

- Poblaciones a las que no aplican las reglas: embarazo, trabajo a turnos y mayores de 60, que quedan fuera del rango de 18 a 60 años de Watson.
- Una fuente para la regla de no conducir con poco sueño.
- La correspondencia entre la escala de este informe (sólido, razonable, débil) y la de A-D del informe 07. Se recoge en el QA-REPORT del 07, H-M12.

## Correcciones a aplicar (línea a línea)

1. **l. 5 y l. 503**: decir que la QA de 2026-11-19 verificó Liu, Garaulet, la EFSA, Ciria, Kredlow y Baron (H-B17).
2. **l. 9**: aclarar que las `reported` sin abrir pueden venir de memoria y que se contrastaron en la QA (H-B18).
3. **l. 19, 40, 144**: café a al menos 9 h y dosis altas a al menos 13,5 h, con las cifras de Gardiner (H-C1).
4. **l. 22, 46, 212**: pausas cada 30 min aproximadamente, indicando la población con sobrepeso u obesidad (H-M6).
5. **l. 45, 196, 198, 466**: Manresa-Rocamora 2021 (PMC8507742) y Granero-Gallegos 2020 (PMC7663087) (H-M1).
6. **l. 47, 218, 220, 221, 457, 458**: años de 2023 (H-B9).
7. **l. 53, 266, 267, 271, 273**: revisión paraguas, estudio completo de 2025, fumadores sin verificar y enlace de la UIC (H-M2, H-M5, H-B10, B1).
8. **l. 55**: fuente de la OMS (H-B11).
9. **l. 71**: revisión de la NSF de 2026 (H-B1).
10. **l. 80**: wearables (H-B2).
11. **l. 89**: población de la TCC-I (H-B19).
12. **l. 97**: Arab 2024 (H-B3).
13. **l. 111, 115**: «al menos diez veces menor»; Burns sin verificar (H-B4, H-B5).
14. **l. 124**: 3 h (H-C2).
15. **l. 130**: Lovallo (H-M3).
16. **l. 150**: Dutheil (H-M4).
17. **l. 165, 452**: fuentes del BRAC (H-B6).
18. **l. 171**: quitar «Otro metaanálisis» (H-B7).
19. **l. 218, 315**: AAO, unos 63 cm (H-B8).
20. **l. 282, 339**: brillo antes que el modo noche (H-B22).
21. **l. 313-315**: INSST y RD 488/1997 (H-B12).
22. **l. 331, 332, 482**: Shrestha y su DOI (H-B13).
23. **l. 362, 433**: STOP-Bang de Chung 2016 y fuente del 024 (H-B14, H-B15).
24. **l. 365**: temperatura (H-M7).
25. **l. 380**: Macnamara y Burgoyne (H-B16).
26. **Índice**: añadir las fuentes que faltan (H-B20) y actualizar las etiquetas de Liu, Garaulet, EFSA, Riemann, Ciria, Kredlow y Baron.

## Re-verificación

Fecha: 2026-11-19. Las correcciones se hicieron con Edit sobre `02-evidencia-protocolos.md`, cambiando solo las frases afectadas. Cada una cita la URL de `qa/B-respuestas.md` y lleva la marca «(corregido tras QA 2026-11-19)». El informe pasa de 503 a 517 líneas porque se añadieron fuentes al índice, así que las líneas nuevas no coinciden con las antiguas. Tras la corrección hay 0 guiones largos.

| hallazgo | estado | línea nueva |
|---|---|---|
| B1 · enlace roto de la UIC | corregido: sustituido por la nota de la UIC, más el estudio completo en PubMed | 272, 273 |
| (no bloqueo) · Cochrane CD010912 | corregido: DOI | 334, 484 |
| H-C1 · café a 8 h, por debajo de Gardiner | corregido: al menos 9 h para un café y al menos 13,5 h para dosis altas, con las cifras de 8,8 h y 13,2 h | 19, 40, 137, 144 |
| H-C2 · luz nocturna 2-3 h | corregido: 3 h | 124 |
| H-M1 · PMC8507742 | corregido: Manresa-Rocamora 2021 (PMC8507742) y Granero-Gallegos 2020 (PMC7663087) | 45, 196, 198-200, 468 |
| H-M2 · estudio de la AHA ya publicado | corregido: Chen et al. 2025, HR 2,35, observacional | 53, 268, 273, 275, 476 |
| H-M3 · Lovallo | corregido: «reduced, but not eliminated» | 130, 132 |
| H-M4 · Dutheil | corregido: 11 estudios, siesta media de 55 min | 150, 433 |
| H-M5 · revisión paraguas | corregido: evidencia de calidad alta en peso; no supera a la restricción calórica | 267, 477 |
| H-M6 · pausas cada 30-45 min | corregido: cada 30 min aproximadamente, indicando la población | 22, 46, 206, 213 |
| H-M7 · temperatura 17-21 °C | corregido: se quita la cifra; Baniassadi como dato de mayores | 367, 434 |
| H-B1 · revisión de la NSF de 2026 | corregido | 71 |
| H-B2 · error del tiempo total en wearables | corregido: F1 de 0,26 a 0,69 | 80, 81 |
| H-B3 · Arab 2024 | corregido | 97, 100, 429 |
| H-B4 · «1 %» | corregido: «al menos diez veces menor» | 111 |
| H-B5 · resultados de Burns | corregido: marcados como no verificados | 115 |
| H-B6 · fuentes del BRAC | corregido | 165, 454 |
| H-B7 · «otro metaanálisis» | corregido: quitado | 171 |
| H-B8 · AAO 46-64 cm | corregido: unos 63 cm (`reported`) | 218, 223, 317, 461 |
| H-B9 · años de Talens y Johnson | corregido: 2023 | 47, 218, 221, 222, 459, 460 |
| H-B10 · fumadores | corregido: «no verificado» | 268 |
| H-B11 · OMS y alcohol | corregido | 55 |
| H-B12 · RD 488/1997 e INSST | corregido | 315-317, 323 |
| H-B13 · Shrestha | corregido: calidad baja; unos 100 min; no evalúa la salud | 333 |
| H-B14 · STOP-Bang | corregido: Chung 2016 | 364, 435 |
| H-B15 · 024 | corregido: fuente del Ministerio | 364 |
| H-B16 · Macnamara y Burgoyne | corregido | 382 |
| H-B17 · recuento de fuentes no abiertas | corregido | 5, 517 |
| H-B18 · `reported` y memoria | corregido | 9 |
| H-B19 · población de la TCC-I | corregido | 89 |
| H-B20 · fuentes sin entrada en el índice | corregido: entradas 65-74 | 505-515 |
| H-B21 · margen hasta las 15:30 | no corregido: decisión de producto explícita | 249 |
| H-B22 · modo noche | corregido: el brillo va primero | 284, 341 |
| H-B23 · poblaciones especiales y regla de conducción | no corregido: falta una nueva búsqueda; se anota en las limitaciones | 517 |

**Nota recalculada** con solo lo que queda abierto (2 bajas): `nota.py --claims 95 --verificadas 73 --portantes 47 --portantes-ok 47 --criticas 0 --medias 0 --bajas 2 --bloqueos 0` → **9.3 / 10, ENTREGABLE**.

Las 47 portantes coinciden ahora con la verificación. B02-34 se da por buena porque la cifra corregida coincide con la respuesta MEDIA del verificador. La nota la limita la cobertura: se verificaron 73 de las 95 afirmaciones que contó el preflight.

**Veredicto tras corregir:** ENTREGABLE (`PASS`). No quedan críticas ni medias, y quedan abiertas dos bajas.


## Comprobación de la corrección por un tercero (sesión principal, 2026-11-19)

- Desde la sesión principal se cotejó la crítica de la cafeína: la tabla resumen (fila 3b) dice ahora al menos 9 h y al menos 13,5 h, por encima de los mínimos de Gardiner 2023 (8,8 h y 13,2 h) que da el verificador. Coincide. Las demás correcciones no se han cotejado una a una.
