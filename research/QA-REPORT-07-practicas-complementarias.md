---
kind: qa-report
target: 07-practicas-complementarias.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 8.6
score_limited_by: cobertura
score_before_fix: 0.0
coverage_claims: 157
coverage_verified: 83
independent: true
sources: 93
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 07 · Prácticas complementarias, de biohacking y de bienestar

## Nota: 0.0 / 10 · REHACER antes de corregir; tras las correcciones, 8.6 · ENTREGABLE (ver «Re-verificación»)

La nota la limitan los hallazgos; el techo por cobertura es 7,23. La penalización suma 39,25 puntos:
- un bloqueo de enlace: 2 puntos;
- seis críticas: 18 puntos;
- doce medias: 12 puntos;
- veintinueve bajas: 7,25 puntos.

Las críticas caen en tres zonas:
- **Afirmaciones regulatorias**: el umbral de la melatonina en España, el procedimiento europeo de la melatonina y la situación de la ashwagandha en otros países.
- **Fuentes que no dicen lo que el informe les atribuye**: el estudio de Basner en *Sleep* 2026, que sostiene el nivel A de los tapones, y Church 2018, que sostiene el nivel D del *tapping*.
- **Un mensaje al usuario**: presenta como probada la regla 20-20-20.

La mayor parte del catálogo, en cambio, aguanta: 54 de las 67 portantes coinciden con la verificación independiente.

Cálculo: `nota.py --claims 157 --verificadas 83 --portantes 67 --portantes-ok 54 --criticas 6 --medias 12 --bajas 29 --bloqueos 1` → 0.0, REHACER.

**Modo**: Deep · **Tipo**: research de evidencia y regulación · **Fecha**: 2026-11-19
**Independencia**: el verificador trabajó en un contexto separado ✓. No vio el informe ni el mapa, y contestó 87 preguntas neutras con fuentes que abrió en su sesión: PubMed, PMC, Crossref, BOE, AEMPS, CIMA, EMA, ClinicalTrials.gov, Fødevarestyrelsen y ANSES.
**Método**: Chain of Verification (`qa/B-mapa.md`, `qa/B-preguntas.md`, `qa/B-respuestas.md`). `searches: 0` se refiere a esta fase de comparación.
**Rúbricas**: ⚠ en esta pasada no se cargaron `_base` ni la rúbrica de research.

## Cobertura

| | |
|---|---|
| Afirmaciones verificables estimadas | entre 250 y 280 |
| Afirmaciones contadas (C = máx(157 del preflight, 87 extraídas)) | 157 |
| Extraídas y preguntadas | 87 (67 portantes y 20 de apoyo) |
| Verificadas con fuente consultada, incluidas las refutadas | 83 |
| Sin fuente abierta | B07-02 y B07-03 (nice.org.uk bloqueado), B07-57 (sin fuente) y B07-60 (tga.gov.au no respondió) |
| Portantes que aguantan | 54 de 67 |

La cobertura global (83 de 157, un 53 %) es baja porque el preflight contó 157 afirmaciones y solo se extrajeron 87 para preguntar. Las 70 que quedan son sobre todo cifras secundarias de las fichas.

Clasificación por id:

| Clase | ids |
|---|---|
| VERIFIED | 01, 03, 04, 05, 06, 08, 09, 11, 12, 13, 14, 16, 19, 21, 22, 25, 27, 29, 30, 31, 32, 33, 35, 36, 40, 41, 44, 45, 48, 50, 51, 53, 54, 55, 58, 59, 60, 61, 63, 65, 66, 69, 70, 73, 75, 76, 77, 79, 82, 84, 86 |
| VERIFIED con hallazgo de procedencia o de año (baja) | 07, 10, 24, 28, 81, 85 |
| ERROR | 49 (el artículo 8 no está abierto), 67 (no existe un Basner en *Sleep* 2026), 87 (Church 2018 concluye lo contrario) |
| STALE | 62 (ashwagandha en otros países) |
| DISCREPANCY | 17, 18, 34, 37, 42, 43, 46, 47, 64, 72, 78, 80 |
| UNVERIFIABLE | 02 (actualización de NICE de 2026), 15 (quién la encargó), 20 (619 personas; 10-25 %), 23 (porcentajes), 26 (distancia), 38 (WHOOP donó), 39 (riesgo de sesgo; muertes en el agua), 52 (financiación), 56 (pico a las 4 h), 57, 68 (REM con ruido rosa), 71 (metaanálisis de 2022), 74, 83 (71 estudios; hora del día) |
| INTERNAL | C07-01 a C07-12 y X-02, X-05 y X-06 del mapa |
| MISSING | suplementos frecuentes sin evaluar; correspondencia de escalas |

## Veredicto

**Tras corregir: ENTREGABLE** (`PASS`, 8.6, limitada por la cobertura), ver «Re-verificación». Antes de corregir era **REHACER** (`MAJOR ISSUES`): había seis críticas y un enlace roto. Todas se corrigen en líneas concretas, sin rehacer secciones:
- la melatonina: l. 31, 309, 312, 542, 618 y 714;
- la ashwagandha: l. 337 y 338;
- los tapones y el ruido rosa: l. 82, 83, 368, 375, 378 y 690;
- el *tapping*: l. 28, 95 y 476-481;
- la 20-20-20: l. 190.

## Bloqueos deterministas (preflight)

| # | Enlace | Línea | Estado | Qué vio el verificador | Corrección |
|---|---|---|---|---|---|
| B1 | https://fvst.dk/Media/638245843133059907/Withania%20somnifera%20%20risikovurdering%2015%20maj%202020.pdf | 338, 683 | 404 (roto) | También le dio 404. Abrió la página oficial de Fødevarestyrelsen sobre la ashwagandha (B07-61) | Sustituir por https://foedevarestyrelsen.dk/kost-og-foedevarer/alt-om-mad/kemi-i-maden/mad-med-uoensket-kemi/ashwagandha y mantener la referencia a la evaluación de la DTU de 2020 como texto, marcada «PDF no disponible» |
| (no bloqueo) | moodle2.units.it, PDF de Shechter | 195 | 200 | n. a. | Se mantiene |

## Contrato de escritura y voz

- **Script de-slop**: no disponible. Las pruebas contables **no se han comprobado**.
- **Guiones largos**: 0 tras la limpieza del coordinador (la celda «—» pasó a «sin fuente»).
- **Voz**: castellano de España, de tú en los mensajes de Ucoach.

## Hallazgos por gravedad

### Críticas

**H-C1 · INTERNAL (X-02) · crítica · Ucoach presenta la regla 20-20-20 como probada**
- **Dice**: l. 190: «Para los ojos funciona mejor la regla 20-20-20, parpadear y ajustar el brillo y la distancia de la pantalla».
- **Verificación independiente**:
  - Talens-Estarelles 2023: con recordatorios bajan los síntomas, pero el efecto no se mantiene una semana después (https://pubmed.ncbi.nlm.nih.gov/35963776/).
  - Johnson y Rosenfield 2023: las pausas de 20 s no tienen efecto en síntomas ni en lectura (https://pubmed.ncbi.nlm.nih.gov/36473088/).
  - El informe 02 la califica de débil.
- **Corrección**: «Para los ojos, lo razonable es parpadear, mirar a lo lejos de vez en cuando y ajustar el brillo y la distancia de la pantalla, aunque ninguna de estas medidas tiene evidencia fuerte».

**H-C2 · INTERNAL + DISCREPANCY (C07-01, B07-46) · crítica · Umbral de la melatonina en España, con tres formulaciones y sin texto oficial**
- **Dice**:
  - l. 31: «En España, a partir de 2 mg al día se considera medicamento».
  - l. 309: «la AEMPS considera medicamento la melatonina en cantidades superiores a 2 mg al día y ha retirado complementos de 3 mg (2020, 2021 y 2024)».
  - l. 312 y 542: «los complementos llevan menos de 2 mg».
- **Verificación independiente** (B07-46, B07-47):
  - **No hay un texto vigente de la AEMPS o la AESAN con el umbral explícito.** El único texto literal (Gobierno Vasco, 2013) atribuye a la AEMPS «cantidades superiores a 2 mg diarios» y en el mismo documento habla de la cantidad «a partir de la cual se considera medicamento». Es decir, el propio documento es ambiguo. Las retiradas comparan con el medicamento autorizado de 2 mg.
  - Retiradas: 2-4-2020 (3 mg), 2-7-2021 (3 mg) y 10-4-2024 (**5 mg**, no 3 mg) (https://www.aemps.gob.es/?p=14039 , https://www.aemps.gob.es/?p=19171 , https://www.aemps.gob.es/?p=33570). La AESAN informó de otra en septiembre de 2026 (5 mg; solo verificada en prensa).
- **Corrección**: una sola formulación en las cuatro líneas: «En España no hay un texto oficial vigente que fije el umbral con "a partir de" o "más de". La referencia es el medicamento autorizado de 2 mg, y la pauta prudente es que el complemento lleve menos de 2 mg». Corregir el año y la dosis de las retiradas.

**H-C3 · ERROR (B07-49) · crítica · El procedimiento del artículo 8 sobre la melatonina no está abierto, y falta la prohibición de Hungría**
- **Dice**: l. 309: «En 2026 está abierto un posible procedimiento del artículo 8 a escala europea». l. 618 y 714 repiten «procedimiento del artículo 8 de la UE» y «procedimiento europeo del artículo 8 en marcha».
- **Verificación independiente** (B07-49; NutraIngredients, cronología de la melatonina, 4-11-2026): **no hay ningún procedimiento formal del artículo 8 abierto**. Los jefes de agencias de la UE la señalaron en 2024, pero la evaluación está «on hold». **Hungría prohibió la melatonina en complementos en agosto de 2026.**
- **Corrección**: «No hay ningún procedimiento formal del artículo 8 abierto; la UE lo dejó en suspenso. Hungría prohibió la melatonina en complementos en agosto de 2026 (`reported`, NutraIngredients)».

**H-C4 · ERROR (B07-67, C07-03) · crítica · El nivel A de los tapones se apoya en un estudio en *Sleep* 2026 que no se localiza**
- **Dice**: l. 82: «Anulan el efecto del ruido en el sueño profundo y en el REM | Basner et al., 2026». l. 368: «Basner et al. (*Sleep*, febrero de 2026; 25 adultos durante 7 noches) encontraron que el ruido de aviones redujo el sueño profundo unos 23 minutos por noche, y que los tapones eliminaron ese efecto».
- **Verificación independiente** (B07-67, B07-68, https://pubmed.ncbi.nlm.nih.gov/42120238/): **no hay un estudio de Basner en *Sleep* de 2026**. Lo que existe es Basner et al., *Sleep Health* 2026;12(4):702-6:
  - polisomnografía en laboratorio con n=25 y 93 eventos de ruido;
  - el ruido rosa reduce los microdespertares, pero **los tapones funcionan mejor**.
  
  El efecto sobre el sueño profundo (23 min) y sobre el REM no aparece en el abstract.
- **Por qué es crítica**: es la única fuente de una práctica de nivel A («evidencia sólida»), y la propone por defecto en tres protocolos.
- **Corrección**: citar el estudio real, bajar los tapones a **B** («un ensayo de laboratorio con 25 personas; riesgo muy bajo») y marcar como no verificados los 23 min de sueño profundo.

**H-C5 · STALE (B07-62) · crítica · La situación de la ashwagandha en otros países está desfasada**
- **Dice**: l. 337: «Francia la ha restringido y Países Bajos y Suecia lo están valorando. Sigue sin haber una prohibición en toda la UE».
- **Verificación independiente** (B07-62; supplysidesj.com, 21-10-2026; nutraingredients.com, julio de 2026):
  - no hay prohibición en toda la UE ni procedimiento del artículo 8;
  - **Países Bajos** notificó en septiembre de 2026 un borrador para prohibirla salvo la raíz, con periodo de espera hasta el 7-12-2026;
  - **Polonia** tiene límites desde 2020;
  - **Hungría** la limita a 250 mg de raíz;
  - **Francia y Alemania** solo emiten advertencias;
  - **Suecia y Finlandia** la están evaluando.
- **Corrección**: sustituir la frase por esta lista, con fecha y fuentes.

**H-C6 · DISCREPANCY (B07-87) · crítica · Church 2018 concluye lo contrario de lo que dice el informe, y el nivel D del *tapping* pierde su base**
- **Dice**: l. 95: «El tapping no aporta nada más allá de los componentes de terapia que comparte con otras». l. 477: «el análisis de componentes de Church et al. (2018) admite que el efecto puede deberse a elementos que comparte con otras terapias». l. 479: «muchos de los autores favorables forman a terapeutas de EFT».
- **Verificación independiente**:
  - B07-87 (https://pubmed.ncbi.nlm.nih.gov/30273275/): Church et al. (2018), con 6 estudios (n=403) y 3 comparables (n=102), encuentran acupresión frente a control **d=−0,47** (IC −0,94 a 0,0, en el límite). **Concluyen que es un «active ingredient».** El conflicto de interés del coautor no se verificó. La crítica de Ernst (2018) apunta a la mala calidad de los estudios primarios, pero solo se conoce por fragmentos.
  - B07-86: Clond (2016), con 14 estudios, da d=1,23 antes y después (https://pubmed.ncbi.nlm.nih.gov/26894319/).
- **Por qué es crítica**: el nivel D se define como «sin evidencia, refutada o con riesgo». Hay evidencia, aunque sea de baja calidad, y no está refutada.
- **Corrección**: pasar el *tapping* a **C** (evidencia débil, de baja calidad y con autores vinculados a la técnica, `reported`). Reescribir la ficha 50 y la fila 52, y quitarlo de la lista de D del resumen (l. 28).

### Medias

**H-M1 · OVERCLAIM (C07-03) · media · Paseos en la naturaleza en nivel A con un solo estudio transversal**
- **Dice**: l. 80 y 384: nivel A, apoyado en White 2019.
- **Verificación independiente** (B07-70, https://pubmed.ncbi.nlm.nih.gov/31197192/): n=19.806, diseño transversal, OR 1,59 y 1,23. El dato es correcto, pero el diseño no da «evidencia sólida».
- **Corrección**: bajar a **B** en la tabla, la ficha y los protocolos.

**H-M2 · OVERCLAIM (C07-03) · media · Hidratación en nivel A, aunque la práctica en la oficina es una inferencia**
- **Dice**: l. 84 y 398: nivel A; «por debajo de ese umbral, el efecto no se distingue de cero».
- **Verificación independiente** (B07-72, https://pubmed.ncbi.nlm.nih.gov/29933347/): 33 estudios; ES −0,21; atención −0,52. Con una pérdida de peso de más del 2 %, el efecto es −0,28 frente a −0,14 con menos. Es menor, pero no es cero.
- **Corrección**: bajar a **B** y corregir la frase del umbral.

**H-M3 · INTERNAL (C07-02) · media · «Solo prácticas A y B» en los protocolos no se cumple**
- **Dice**: l. 33 y 492. En cambio:
  - el 4.7 incluye el modo noche (C), en la l. 583;
  - el 4.5 incluye una fila sin nivel (l. 558) y otra «A (`inferred`)» (l. 555);
  - el 4.6 incluye vitamina D, «Derivar».
- **Corrección**: decir qué excepciones hay y por qué. Son complementos opcionales que solo se ofrecen si el usuario ya hace esa práctica o pregunta por ella, o son derivaciones.

**H-M4 · UNVERIFIABLE (B07-02, C07-11) · media · La «actualización de julio de 2026» de NICE NG59 no se puede comprobar, y los fragmentos la contradicen**
- **Dice**: l. 134: «La actualización de julio de 2026 quitó de esa recomendación la mención a la terapia psicológica». También en l. 106, 618, 628 y 713.
- **Verificación independiente** (B07-02, sin URL abierta porque nice.org.uk devuelve 403): los fragmentos de NICE siguen diciendo «only as part of a treatment package including exercise, with or without psychological therapy». La única actualización conocida es de 2020 (fármacos en la ciática).
- **Corrección**: quitar la afirmación sobre julio de 2026, citar la frase que sí aparece y marcar la fecha como «no verificada».

**H-M5 · DISCREPANCY (B07-78) · media · Robbins 2024: los kappa no se verifican y el sesgo del Apple Watch va al revés**
- **Dice**: l. 32 y 90: «kappa entre 0,55 y 0,65». l. 437: «El Apple Watch sobrestimó el sueño profundo unos 43 minutos».
- **Verificación independiente** (https://pubmed.ncbi.nlm.nih.gov/39460013/ , PMC11511193): precisión por fases del 76-79,5 % en Oura, del 61,7-78 % en Fitbit y del 50,5-86,1 % en Apple. Sueño profundo: Oura sin diferencias, Fitbit −15 min y **Apple −43 min, es decir, lo infraestima**. Lo financió Oura.
- **Corrección**: cambiar los kappa por los porcentajes de precisión y poner «infraestimó».

**H-M6 · UNVERIFIABLE (B07-68) · media · La pérdida de REM con ruido rosa sostiene un mensaje al usuario y no se verifica**
- **Dice**: l. 83, 375 y 378: «el ruido rosa a 50 dB redujo el REM casi 19 minutos»; «los tapones [...] no te quitan sueño REM».
- **Verificación independiente**: no está en el abstract de *Sleep Health* 2026 (PubMed 42120238).
- **Corrección**: marcarlo como «no verificado» y quitarlo del mensaje al usuario.

**H-M7 · DISCREPANCY (B07-18) · media · Cinta bajo la mesa: velocidad y productividad sin base**
- **Dice**: l. 171: «Andando a unos 2,25 km/h [...] la velocidad de escritura se iguala»; «En un ensayo de la BYU [...] bajó un 9 %»; «Los pocos estudios de 12 a 52 semanas no encuentran efecto en la productividad». La pauta de la l. 174 y la del 4.1 dicen «a unos 2 km/h».
- **Verificación independiente** (https://pubmed.ncbi.nlm.nih.gov/32116273/): 18 estudios. Se escribe más lento, y **no hay datos de productividad a largo plazo**.
- **Corrección**: quitar la velocidad de la pauta («a ritmo lento») y corregir la frase de la productividad.

**H-M8 · UNVERIFIABLE (B07-39) · media · Wim Hof: riesgo de sesgo y muertes sin verificar**
- **Dice**: l. 63 y 284: «todos los estudios tienen alto riesgo de sesgo»; «Hay muertes documentadas».
- **Verificación independiente** (https://pubmed.ncbi.nlm.nih.gov/38478473/): 9 artículos (8 ensayos), con la conclusión de que es «promising». El riesgo de sesgo concreto no está en el abstract, y las muertes no se verificaron.
- **Corrección**: describir la revisión real y marcar las muertes como «no verificado». El aviso de seguridad (nunca en el agua) se mantiene como precaución.

**H-M9 · OVERCLAIM (C07-08, B07-26) · media · Lámpara de 10.000 lux en nivel B para el «bajón de invierno» y pauta de 20-30 min**
- **Dice**: l. 76, 208 y 211; protocolos 4.3 (l. 533) y 4.6 (l. 567); «20-30 min».
- **Verificación independiente**: la evidencia es en depresión no estacional (B07-24, https://pubmed.ncbi.nlm.nih.gov/39356500/) y en el TAE con calidad baja (B07-25). CANMAT 2016 dice **30 min** a primera hora (https://pmc.ncbi.nlm.nih.gov/articles/PMC4994794/).
- **Corrección**: nivel B con TAE y profesional, C para el bajón sin trastorno; 30 min; distancia «según el fabricante».

**H-M10 · INTERNAL (C07-05) · media · Melatonina «solo hacia el este»**
- **Dice**: l. 542: «Solo hacia el este y con 5 husos o más».
- **Verificación independiente** (B07-43, https://pubmed.ncbi.nlm.nih.gov/12076414/): 5 husos o más, **sobre todo** hacia el este.
- **Corrección**: «sobre todo hacia el este».

**H-M11 · INTERNAL (C07-12) · media · Protocolos de 5 a 7 prácticas a la vez frente a «un hábito cada vez»**
- **Dice**: l. 492: «respetan el principio de un hábito cada vez».
- **Corrección**: precisar que el protocolo es un menú, que Ucoach activa como mucho una práctica nueva a la vez y que mantiene las que el usuario ya hace.

**H-M12 · MISSING (X-05) · media · No hay correspondencia entre la escala A-D y la del informe 02**
- **Corrección**: añadir debajo de la tabla de niveles una equivalencia orientativa (`inferred`): sólido ≈ A, razonable ≈ B, débil ≈ C, incorrecto ≈ D.

### Bajas

| id | Clase | Dice (línea) | Verificación independiente | Corrección |
|---|---|---|---|---|
| H-B1 | DISCREPANCY | Índice: «Workplace-based interventions / strengthening» (l. 632) | Ejercicio en oficinistas con cervicalgia; 8 ECA; certeza baja (https://pubmed.ncbi.nlm.nih.gov/38219373/) | Corregir el título |
| H-B2 | UNVERIFIABLE | «el encargo vino del consejo profesional de fisioterapeutas» (l. 152) | No figura en el abstract (https://pubmed.ncbi.nlm.nih.gov/29452579/) | Marcar «no verificado» |
| H-B3 | DISCREPANCY | «Una revisión de 2022 (14 estudios, evidencia muy baja o baja)» (l. 164) | Rizzato et al. 2022 es una revisión narrativa | Corregir |
| H-B4 | UNVERIFIABLE | «619 personas»; «filtran solo entre un 10 % y un 25 %» (l. 187) | El abstract no da el total ni el porcentaje; la salud macular no se evaluó (https://pubmed.ncbi.nlm.nih.gov/37593770/) | Quitar las dos cifras |
| H-B5 | UNVERIFIABLE | Porcentajes de Nagare 17, 10 y 41 %, marcados `verified` (l. 201, 205) | El verificador no los encontró (https://pubmed.ncbi.nlm.nih.gov/31191118/) | Pasar a `reported` |
| H-B6 | DISCREPANCY | Menegaz de Almeida «2024» (l. 76, 208, 648) | *JAMA Psychiatry* 2025;82(1):38-46, en línea en 2024 | Indicar el año del número |
| H-B7 | DISCREPANCY | Muestras «de 1 a 84 personas» (l. 225) | De 12 a 84 (PMC3265077) | Corregir |
| H-B8 | DISCREPANCY | NCT06125639 «terminado en 2024» (l. 248) | Estado «Unknown»; final estimado en mayo de 2024 (https://clinicaltrials.gov/api/v2/studies/NCT06125639) | Corregir |
| H-B9 | UNVERIFIABLE | Balban: grupo de suspiros de 30 personas; «WHOOP donó las pulseras» (l. 276, 278) | Lo verificado es que Huberman era asesor de WHOOP y que se usaron sus pulseras; la donación no (PMC9873947) | Marcar «no verificado» |
| H-B10 | DISCREPANCY | Yoga nidra: «Para el sueño, la certeza es muy baja» (l. 298) | El abstract no da resultados de sueño; *Ann N Y Acad Sci* 2026;1556(1) (https://pubmed.ncbi.nlm.nih.gov/41327816/) | Corregir |
| H-B11 | DISCREPANCY | «8 de 10 ensayos»; «revisada en 2010» (l. 309, 673) | 9 de 10; versión de 2002, sin actualización localizada (https://pubmed.ncbi.nlm.nih.gov/12076414/) | Corregir |
| H-B12 | DISCREPANCY | Retirada de 3 mg en 2024 (l. 309, 675) | La de 2024 era de 5 mg | Corregir (lo cubre H-C2) |
| H-B13 | UNVERIFIABLE | Magtein «financiados por el fabricante» (l. 316) | No consta (https://pubmed.ncbi.nlm.nih.gov/39252819/) | Marcar «no verificado» |
| H-B14 | UNVERIFIABLE | Creatina: «pico a las 4 h» (l. 330) | Mediciones a las 3, 5,5 y 7,5 h (https://pubmed.ncbi.nlm.nih.gov/38418482/) | Quitar «a las 4 h» |
| H-B15 | UNVERIFIABLE | La creatina sube la creatinina sin daño renal (l. 332) | Sin fuente (B07-57) | Marcar «no verificado» y mantener el aviso de consultar al médico |
| H-B16 | DISCREPANCY | «Un metaanálisis de 2021 no encontró mejora en la calidad del sueño» (l. 345) | PMID 33382879: lactantes y niños (https://pubmed.ncbi.nlm.nih.gov/33382879/) | Precisar la población |
| H-B17 | UNVERIFIABLE | «un metaanálisis de ECA de 2022 no encuentra efecto en la tensión» (l. 391) | No localizado | Quitar |
| H-B18 | UNVERIFIABLE | «el grupo de control también redujo su uso» (l. 407) | En el ensayo localizado, el control solo automonitorizaba (https://pubmed.ncbi.nlm.nih.gov/36577008/) | Quitar |
| H-B19 | DISCREPANCY | Vasilev 2018 con «36 estudios» (l. 447) | 65 estudios, *Perspect Psychol Sci* (https://pubmed.ncbi.nlm.nih.gov/29958067/) | Corregir |
| H-B20 | DISCREPANCY | Basu y Banerjee «2023» (l. 454) | En línea en 2022 (https://pubmed.ncbi.nlm.nih.gov/35842538/) | Corregir |
| H-B21 | UNVERIFIABLE | Ayuno: «71 estudios»; «empeora a última hora del día» (l. 463) | 222 efectos y 3.484 participantes; peor con ayunos más largos y en jóvenes (https://pubmed.ncbi.nlm.nih.gov/41182703/) | Corregir |
| H-B22 | DISCREPANCY | Modafinilo: «la EMA limitó en 2010 [...]» (`inferred`) (l. 470) | Dictamen del CHMP de 18-11-2010 y decisión de la Comisión de 27-1-2011; en España, con receta (https://www.ema.europa.eu/en/medicines/human/referrals/modafinil) | Precisar las fechas y pasar a `verified` |
| H-B23 | PROVENANCE | Disección arterial sin fuente (l. 136) | Asociación sin causalidad demostrada, según AHA/ASA 2014 (https://pubmed.ncbi.nlm.nih.gov/25104849/) | Añadir la cita |
| H-B24 | PROVENANCE | Prohibición danesa con el PDF de la DTU (l. 338, 342) | Página oficial de Fødevarestyrelsen | Lo cubre B1 |
| H-B25 | INTERNAL (C07-04) | La numeración de la tabla maestra no coincide con la de las fichas | n. a. | Nota bajo la tabla |
| H-B26 | INTERNAL (C07-06, C07-07) | `verified` indirecto en Buijze y de Zoete | Los dos se verificaron ahora en PubMed (27631616, 41494147) | Actualizar las etiquetas |
| H-B27 | INTERNAL (C07-09) | VFC en B con efecto nulo en el rendimiento (l. 89) | Mejora los índices vagales (0,50) y no el rendimiento (https://pubmed.ncbi.nlm.nih.gov/34639599/) | Describirla como evidencia «mixta» |
| H-B28 | INTERNAL (X-06) | «Paseo de 10 min tras la comida (ya está en la base)» (l. 502, 529) | Es una propuesta del informe 02 (7a) | Corregir |
| H-B29 | MISSING | Faltan valeriana, glicina, CBD, monitorización de glucosa en sanos y TCC-I digital | n. a. | Pendiente de una nueva búsqueda |


## Sólido

Coinciden con la verificación independiente:
- **Lumbalgia y cuello**: Hayden 2021, ACP 2017, Gross 2015, de Zoete 2026 (existe: 76 ECA, 11.866 participantes, −7,01 frente a placebo con certeza muy baja), Slater 2019, Guillaud 2016 y 2018, van Duijvenbode 2008, Speed 2018.
- **Regulación española de la fisioterapia**: la Ley 44/2003, las 139 técnicas del plan de pseudoterapias y la consulta pública del 16-3-2026.
- **Luz y gafas**: Singh 2023 (fatiga visual), Luna-Rangel 2025 (todas las cifras), Shechter 2018.
- **Frío, calor y sauna**: Buijze 2016 (3.018 personas, −29 %), Cain 2025, Piñero 2024, Laukkanen 2015, Haghayegh 2019.
- **Respiración y meditación**: Fincham 2023, Balban 2023 (registro retrospectivo y asesoría de WHOOP), Goyal 2014, Bartlett 2019.
- **Melatonina**: Ferracioli-Oda 2013 y el Reglamento 432/2012.
- **Otros suplementos**: Mah y Pitre, *Proc Nutr Soc* 2024, Xu 2024 (con su corrección de 2025), Gordji-Nejad.
- **Ashwagandha**: Björnsson 2020, Explore 2024 y la prohibición danesa.
- **Sueño y vitaminas**: Shimizu 2024, Abboud 2022, Rotenberg 2025, Capezuti 2022.
- **Naturaleza, pantallas y wearables**: White 2019, Olson 2022, Böttger 2023, la réplica de Ward, Manresa-Rocamora 2021.
- **Foco y cognición**: Ingendoh 2023, Bamberg y Moreau 2025, Battleday y Brem 2015.
- **Grounding**: la declaración de intereses de Chevalier.

## No verificable

- **NICE NG59**: la web devolvió 403. El texto de la recomendación se conoce por fragmentos, y la fecha de la última actualización no se pudo confirmar.
- **TGA 2026** (11 notificaciones): solo por resumen de búsqueda.
- **Creatina y creatinina**: sin fuente.
- **Muertes con Wim Hof en el agua**: no se verificaron.
- **Ruido rosa y REM**: no se verificó.
- **Subdatos**:
  - el porcentaje de luz azul que filtran las lentes;
  - los porcentajes de Nagare;
  - el pico de la creatina;
  - la financiación de Magtein;
  - quién encargó Guillaud 2018;
  - la donación de WHOOP;
  - el metaanálisis de 2022 sobre baños de bosque.

## Falta

- Suplementos y prácticas que un usuario preguntaría: valeriana, glicina, CBD, kava, el *journaling* y la monitorización continua de glucosa en sanos.
- La TCC-I digital como práctica del catálogo.
- La correspondencia de escalas con el informe 02 (H-M12).

## Correcciones a aplicar (línea a línea)

1. **Debajo de la tabla de niveles (l. 20)**: equivalencia de escalas (H-M12).
2. **l. 28**: quitar el *tapping* de la lista de D (H-C6).
3. **l. 31**: melatonina (H-C2).
4. **l. 32, 90, 437**: Robbins (H-M5).
5. **l. 33, 492**: excepciones de nivel en los protocolos y un hábito cada vez (H-M3, H-M11).
6. **l. 51, 171, 174, 503**: cinta (H-M7).
7. **l. 63, 284**: Wim Hof (H-M8).
8. **l. 76, 208, 211, 533, 567**: lámpara (H-M9, H-B6).
9. **l. 80, 384, 568**: paseos en B (H-M1).
10. **l. 82, 83, 368, 375, 378, 520, 543, 553, 690**: tapones y ruido rosa (H-C4, H-M6).
11. **l. 84, 398, 401, 531, 544**: hidratación en B (H-M2).
12. **l. 89, 430**: VFC mixta (H-B27).
13. **l. 95, 476-481**: *tapping* en C (H-C6).
14. **l. 106, 134, 139, 618, 628, 713**: NICE y de Zoete (H-M4, H-B26).
15. **l. 136**: disección (H-B23).
16. **l. 152, 164, 187, 201, 205, 225, 238, 248**: H-B2 a H-B9 y H-B26.
17. **l. 190**: 20-20-20 (H-C1).
18. **l. 276, 278, 298, 309, 312, 313, 316, 330, 332**: H-B9 a H-B15 y H-C2, H-C3.
19. **l. 337, 338, 342**: ashwagandha (H-C5, B1).
20. **l. 345, 391, 398, 407, 447, 454, 463, 470**: H-B16 a H-B22.
21. **l. 502, 529**: paseo tras la comida (H-B28).
22. **l. 542**: «sobre todo hacia el este» (H-M10).
23. **l. 555, 558, 583**: excepciones (H-M3).
24. **l. 618, 714**: artículo 8 y Hungría (H-C3).
25. **l. 632, 648, 673, 675, 677, 683, 690, 698, 702**: índice de fuentes.

## Re-verificación

Fecha: 2026-11-19. Las correcciones se hicieron con Edit sobre `07-practicas-complementarias.md`, cambiando solo las frases, filas y entradas del índice afectadas. Cada una cita la URL de `qa/B-respuestas.md` y lleva la marca «(corregido tras QA 2026-11-19)». El informe pasa de 715 a 732 líneas, así que las líneas nuevas no coinciden con las antiguas. Tras la corrección hay 0 guiones largos.

| hallazgo | estado | línea nueva |
|---|---|---|
| B1 · PDF de fvst.dk con 404 | corregido: página oficial de Fødevarestyrelsen | 349, 699 |
| H-C1 · 20-20-20 presentada como probada | corregido: el mensaje ya no la presenta como probada y remite al informe 02 | 194 |
| H-C2 · umbral de la melatonina en España | corregido: una sola formulación («no hay texto oficial vigente con "a partir de" o "más de"; pauta, menos de 2 mg») | 35, 313, 316, 317, 558, 730 |
| H-C3 · artículo 8 y Hungría | corregido: no hay procedimiento formal; prohibición de Hungría de agosto de 2026 | 35, 313, 634, 693, 730 |
| H-C4 · Basner en *Sleep* 2026 y tapones en A | corregido: *Sleep Health* 2026 (n=25); tapones en B; 23 min sin verificar | 86, 378-382, 536, 559, 569, 706 |
| H-C5 · ashwagandha en otros países | corregido: Países Bajos, Polonia, Hungría, Francia, Alemania, Suecia y Finlandia, con fecha | 341-348, 353, 634 |
| H-C6 · Church 2018 y *tapping* en D | corregido: Church concluye «active ingredient»; el *tapping* pasa a C con un mensaje de plantilla C | 32, 99, 487-492, 724 |
| H-M1 · paseos en la naturaleza en A | corregido: B | 84, 232, 394, 534, 584 |
| H-M2 · hidratación en A | corregido: B; umbral del 2 % reescrito | 88, 408, 409, 547, 560 |
| H-M3 · «solo prácticas A y B» | corregido: excepciones declaradas y marcadas en las tablas | 37, 503-508, 549, 571, 583, 599 |
| H-M4 · NICE en julio de 2026 | corregido: se quita la afirmación, se cita la frase de NICE y la fecha queda «no verificada» | 110, 138, 634, 644, 729 |
| H-M5 · Robbins: kappa y Apple | corregido: precisión por fases; Apple infraestima | 36, 94, 448, 717 |
| H-M6 · REM con ruido rosa | corregido: no verificado y quitado del mensaje al usuario | 87, 386-389 |
| H-M7 · cinta bajo la mesa | corregido: sin datos de productividad a largo plazo; «a ritmo lento» | 55, 175, 178, 519 |
| H-M8 · Wim Hof | corregido: revisión descrita según el resumen; muertes «no verificadas»; el aviso se mantiene | 67, 288 |
| H-M9 · lámpara para el bajón | corregido: B con TAE y profesional, C para el bajón; 30 min (CANMAT) | 80, 211-215, 549, 583, 664 |
| H-M10 · «solo hacia el este» | corregido: «sobre todo hacia el este» | 558 |
| H-M11 · un hábito cada vez | corregido: el protocolo es un menú con como mucho una práctica nueva a la vez | 508 |
| H-M12 · escalas | corregido: equivalencia orientativa | 22 |
| H-B1 · título de *Applied Ergonomics* | corregido | 648 |
| H-B2 · encargo de Guillaud 2018 | corregido: no verificado | 156 |
| H-B3 · revisión de 2022 sobre fitball | corregido: narrativa | 168 |
| H-B4 · 619 personas; 10-25 % | corregido: quitados | 191 |
| H-B5 · porcentajes de Nagare | corregido: `reported` | 205, 209 |
| H-B6 · Menegaz de Almeida 2025 | corregido | 80, 212, 664 |
| H-B7 · muestras de 12 a 84 | corregido | 229 |
| H-B8 · NCT06125639 | corregido: «Unknown» | 252 |
| H-B9 · Balban y WHOOP | corregido | 280, 282 |
| H-B10 · yoga nidra | corregido: sin datos de sueño; 2026 | 69, 302, 686 |
| H-B11 · Herxheimer: 9 de 10; sin actualización en 2010 | corregido | 313, 689 |
| H-B12 · retirada de 2024 de 5 mg | corregido | 313, 691 |
| H-B13 · Magtein | corregido: financiación no verificada | 320 |
| H-B14 · pico de la creatina | corregido: 3, 5,5 y 7,5 h | 334 |
| H-B15 · creatinina | corregido: no verificado; el aviso al médico se mantiene | 336 |
| H-B16 · omega-3 2021 | corregido: población infantil | 356 |
| H-B17 · baños de bosque 2022 | corregido: quitado | 402 |
| H-B18 · grupo control de la escala de grises | corregido: experimento de n=112 | 418 |
| H-B19 · Vasilev | corregido: 65 estudios, *Perspect Psychol Sci* | 458, 718 |
| H-B20 · Basu y Banerjee | corregido: 2022 | 465 |
| H-B21 · Bamberg y Moreau | corregido: 222 efectos; 71 estudios y hora del día sin verificar | 474 |
| H-B22 · modafinilo y EMA | corregido: 2010-2011, `verified` | 481 |
| H-B23 · disección arterial | corregido: AHA/ASA 2014 | 140 |
| H-B24 · fuente de la prohibición danesa | corregido (cubierto por B1) | 349, 353 |
| H-B25 · numeración de la tabla y las fichas | corregido: nota | 24 |
| H-B26 · `verified` indirecto en Buijze y de Zoete | corregido: PubMed 27631616 y 41494147 | 143, 242, 643, 673 |
| H-B27 · VFC en B con resultado nulo | corregido: «evidencia mixta» | 93, 440 |
| H-B28 · paseo tras la comida «en la base» | corregido: propuesta del informe 02 (7a) | 518, 545 |
| H-B29 · prácticas que faltan (valeriana, glicina, CBD, etc.) | no corregido: hace falta una nueva búsqueda; se anota en los límites | 731 |

**Nota recalculada** con solo lo que queda abierto (1 baja): `nota.py --claims 157 --verificadas 83 --portantes 67 --portantes-ok 67 --criticas 0 --medias 0 --bajas 1 --bloqueos 0` → **8.6 / 10**. El script la sitúa en la banda «ENTREGABLE CON RESERVAS».

Las 67 portantes coinciden ahora con la verificación. B07-02 y B07-03 (NICE) se dan por buenas porque el texto corregido coincide con la respuesta MEDIA del verificador. La nota la limita la **cobertura**, no los hallazgos: se verificaron 83 de las 157 afirmaciones que contó el preflight. Para pasar de 9 habría que verificar unas 50 cifras secundarias más de las fichas.

**Veredicto tras corregir:** ENTREGABLE (`PASS`). No quedan críticas ni medias, las portantes están verificadas y queda abierta una baja. Antes de publicar el catálogo conviene confirmar por canales oficiales tres datos `reported` con fecha de 2026: la prohibición de la melatonina en Hungría, el borrador de los Países Bajos sobre la ashwagandha y el aviso de la TGA de julio de 2026.


## Comprobación de la corrección por un tercero (sesión principal, 2026-11-19)

- Desde la sesión principal se cotejaron dos críticas con qa/B-respuestas.md. Tapones: B07-67 y B07-68 confirman que el estudio es de Basner et al., Sleep Health 2026, con n=25, y la línea 86 lo recoge con nivel B. Melatonina: B07-46 y B07-49 confirman la ambigüedad del umbral de 2 mg, el procedimiento del art. 8 en suspenso y la prohibición de Hungría, y el resumen 6 lo recoge. Las dos coinciden. Las demás correcciones no se han cotejado una a una.
- Antes de publicar el catálogo de prácticas a usuarios, hay que confirmar en canales oficiales tres datos de 2026 que solo constan en prensa: Hungría, el borrador de los Países Bajos y la TGA.
