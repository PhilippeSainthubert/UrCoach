---
kind: qa-report
target: 08-rendimiento-coaching.md
mode: deep
verdict: NEEDS REVISION
verdict_es: CORREGIR ANTES DE ENTREGAR
score: 8.6
score_before_fix: 0.0
score_limited_by: cobertura
coverage_claims: 136
coverage_verified: 84
independent: true
sources: 86
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 08 · Ciencia del rendimiento profesional y método de coaching

## Nota: 8.6 / 10 · CORREGIR ANTES DE ENTREGAR (tras corregir)

**Nota antes de corregir: 0.0 / 10 · REHACER.** El 2026-11-19 se corrigieron con Edit los 40 hallazgos (1 crítica, 17 medias y 22 bajas) y los 3 bloqueos. No queda ningún hallazgo abierto. La nota ahora la limita la cobertura: 64 de 66 portantes y 84 de 136 afirmaciones verificadas. nota.py la sitúa en «ENTREGABLE CON RESERVAS», pero la regla del veredicto manda CORREGIR ANTES DE ENTREGAR porque hubo una crítica (ya resuelta) y no todas las portantes están verificadas. Lo que falta es verificar, no corregir. El detalle está en «Re-verificación», al final.

Lo que sigue es el informe original, antes de corregir.

La nota la bajan los hallazgos, no la cobertura. Con lo verificado, el techo sería 8,64: 64 de 66 portantes y 84 de 136 afirmaciones. Las penalizaciones suman 31,5: 1 crítica (3), 3 bloqueos (6), 17 medias (17) y 22 bajas (5,5).

Casi todo lo que pesa tiene arreglo. Las citas existen, incluidas las que más riesgo tenían de ser inventadas (de Haan 2026, Cheng 2026 en *Science*, Sheeran 2024, Rogelberg 2026 y Poynter 2025), y casi todas las cifras de los metaanálisis coinciden. Fallan tres cosas:
- una afirmación que Ucoach diría al usuario y que el estudio no mide (C1);
- una docena de cifras o matices mal trasladados;
- el «método Ucoach», que se contradice en cinco reglas.

**Modo**: Deep · **Tipo**: research científico aplicado a producto · **Fecha**: 2026-11-19
**Independencia**: verificador en contexto separado ✓. No vio ni el informe ni el mapa, solo `qa/E-preguntas.md`. El cruce se hizo con `qa/E-mapa.md` y `qa/E-respuestas.md`.
**Rúbricas**: sin rúbrica de tipo cargada ⚠
**Voz**: no aplica (documento interno de research)

Cálculo: `nota.py --claims 136 --verificadas 84 --portantes 66 --portantes-ok 64 --criticas 1 --medias 17 --bajas 22 --bloqueos 3`

## Cobertura

| | |
|---|---|
| Afirmaciones en el documento | 136, que es el recuento del preflight. Se extrajeron 89 (66 portantes y 23 de apoyo); las demás cuentan como no verificadas. |
| Verificadas con fuente consultada | 84 (62 % de 136; 94 % de las extraídas). Unas 55 con confianza ALTA y 29 MEDIA |
| Portantes verificadas | 64 de 66 |
| No verificables | E08-29 (pre-mortem, BAJA), E08-16 en su parte de autointerrupciones (BAJA), E08-68 (28 % a solas), E08-71 (contenido de Bryan y Locke) y E08-73 (Rogelberg, «la mitad del tiempo de reunión») |
| Fuentes distintas del verificador | 86 URL |

Las dos portantes sin verificar son el estudio del pre-mortem de Veinott et al. (2010), que solo se encontró en fuentes secundarias porque el PDF de ISCRAM no se pudo abrir, y la proporción de autointerrupciones de Gloria Mark, que solo está en entrevistas.

## Veredicto

**Tras corregir: CORREGIR ANTES DE ENTREGAR** (`NEEDS REVISION`). No queda ningún hallazgo abierto. Quedan sin verificar dos portantes (el pre-mortem de Veinott y la proporción de autointerrupciones de Mark) y las 47 afirmaciones del recuento del preflight que no se extrajeron. Ver «Re-verificación».

Antes de corregir: **REHACER** (`MAJOR ISSUES`). Hay una crítica sin resolver y tres bloqueos deterministas. La crítica es que el informe pone en boca de Ucoach, y en dos tablas, que el líder privado de sueño «no lo nota». Barnes et al. (2016) no miden cómo se ve el líder a sí mismo.

Lo de fondo aguanta: el coaching funciona con un efecto moderado y sesgo de publicación, la alianza es el ingrediente con más peso, la complacencia de los LLM es un riesgo documentado y hace falta una derivación fija. También se sostienen los mitos refutados del agotamiento del ego, los jueces israelíes, el móvil cerca y el power posing hormonal. Para entregar hay que hacer tres cosas:
- corregir las cifras mal trasladadas;
- quitar lo que el estudio no dice;
- hacer coherente el método (métricas, duración del cierre, una pregunta cada vez, remisiones).

## Bloqueos deterministas (preflight)

| Línea | Enlace | Estado | Corrección |
|---|---|---|---|
| 528 | `https://doi.org/10.1016/0030-5073(67)90021-9` | 404: el enlace se corta en el paréntesis | Codificarlo: `https://doi.org/10.1016/0030-5073%2867%2990021-9`, que da 200 |
| 512 | `https://dlab.sauder.ubc.ca/sjdm/journal/16/16823/jdm16823.html` | Sin respuesta | Sustituir por `https://journal.sjdm.org/16/16823/jdm16823.html`, que da 200 |
| 543 | `https://researchr.org/publication/VeinottKW10` | Sin respuesta | E-respuestas no tiene otra URL del estudio. El verificador solo encontró psychologytoday.com y scienceblog.com en resultados de búsqueda, sin URL concreta. Se quita el enlace y se marca «fuente no accesible» |

Los demás enlaces que marcó el preflight dan 200 con curl desde la sesión principal y no cuentan.

Placeholders: 0. Fechas relativas: 0. Guiones largos: 0, comprobado con grep.

## Contrato de escritura y voz

⚠ **No se pudo comprobar.** de-slop no estaba disponible, así que no se pasaron las cuatro pruebas del contrato. Guiones largos: 0. No hay hallazgos de VOZ porque es un documento interno.

## Hallazgos por gravedad

### Crítica

**C1 · E08-06 · ERROR · crítica**
- **Dice**:
  - l. 37: «Un líder privado de sueño inspira menos, aunque él no lo note».
  - l. 115: «Los observadores ven a los líderes privados de sueño como menos carismáticos, pero estos no se ven peor a sí mismos».
  - l. 128, texto que Ucoach diría al usuario: «Hoy tu energía transmite menos aunque tú no lo notes».
- **Verificación independiente**:
  - Estudio 1: tres observadores puntúan menos carismático al líder privado de sueño, y lo explica la menor actuación profunda (deep acting).
  - Estudio 2: los seguidores privados de sueño también atribuyen menos carisma.
  - «El artículo no mide cómo se evalúa el líder a sí mismo en carisma» (https://www.bauer.uh.edu/workingfamilies/research/JAP-Barmes-Guarana,-Nauman-Kong-2016.pdf ; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Too%20tired%20to%20inspire%22). ALTA.
- **Por qué es crítica**: sostiene un mensaje del brief que Ucoach diría al usuario como hecho científico, y esa parte es falsa.
- **Corrección**:
  - l. 37: «Los observadores ven menos carismático a un líder privado de sueño (el estudio no mide cómo se ve él)».
  - l. 115: sustituir «pero estos no se ven peor a sí mismos» por el mecanismo verificado (menor actuación profunda) y la advertencia de que no se mide la autoevaluación.
  - l. 128: «Tras una mala noche, los demás tienden a verte menos carismático».

### Medias

**M1 · E08-04 · DISCREPANCY (e INTERNAL) · media**
- **Dice**: resumen, «Tras dos semanas a 6 horas, el rendimiento cognitivo cae como tras una o dos noches en vela» (l. 18). Tabla 2.1: «1-2 noches» (l. 35). § 4: «A 6 horas, el déficit equivalía a hasta 2 noches» (l. 113), con la etiqueta `reported`, aunque la tabla dice «sólido».
- **Verificación independiente**: «chronic restriction of sleep to 6 h or less per night produced cognitive performance deficits equivalent to up to 2 nights». Junta las condiciones de 4 y 6 horas y no da una cifra solo para 6 horas. La somnolencia apenas aumentaba tras los primeros días y «subjects were largely unaware». N = 48 (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22cumulative%20cost%20of%20additional%20wakefulness%22). ALTA.
- **Corrección**: «6 horas o menos (4 y 6 horas juntas)… hasta 2 noches» en las l. 18, 35 y 113. Subir la etiqueta a `verified`. La regla «avisar aunque el usuario se sienta bien» se mantiene.

**M2 · E08-09 · ERROR · media**
- **Dice**: «La privación de sueño afecta más a la cognición que depende de la emoción y a la función prefrontal: juicio, riesgo y decisiones complejas» (l. 117). Se cita como fuente de la regla del estado «Deuda» (l. 126).
- **Verificación independiente**: la privación ralentiza la atención y la vigilancia simples y empeora lo creativo, lo divergente y lo que depende de información emocional. Muchas tareas convergentes, de razonamiento y de decisión con reglas se ven relativamente poco afectadas. No menciona el riesgo (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Effects%20of%20sleep%20deprivation%20on%20cognition%22). ALTA (resumen).
- **Corrección**: reescribir la l. 117 con lo verificado y quitar a Killgore como fuente de la regla de la l. 126. La regla se sostiene con Gish 2019 y Van Dongen 2003.

**M3 · E08-12 · DISCREPANCY · media**
- **Dice**: «Los médicos recetan un 26 % más de antibióticos innecesarios en la 4.ª hora que en la 1.ª […] puede ser cansancio o puede ser ceder ante la insistencia del paciente» (l. 121). Tabla: «+26 % en la 4.ª hora» (l. 41). El resumen 3 dice «Lo que sí se sostiene es que el juicio empeora con […] la hora» (l. 19).
- **Verificación independiente**: odds ratio ajustada de recetar antibiótico de 1,26 en la 4.ª hora frente a la 1.ª, en 21.867 visitas por infección respiratoria aguda. Es una odds ratio, no un aumento del 26 %, y el estudio no clasifica las recetas como innecesarias. Los autores proponen la fatiga de decisión y citan como alternativas «glucose depletion or general fatigue» (https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4648561). ALTA.
- **Corrección**: «odds ratio 1,26» en las l. 41 y 121, sin «innecesarios», con los mecanismos verificados. En la l. 19, «según datos observacionales».

**M4 · E08-20 · DISCREPANCY · media**
- **Dice**: «Los planes de franja horaria se rompen con las interrupciones» (l. 20). También «planificar por franjas horarias mejoraba […] solo si había pocas interrupciones» (l. 142) y «el bloque fijo se rompe con las interrupciones» (l. 146). Tabla 3.5 (l. 46).
- **Verificación independiente**: Parke et al. comparan la «planificación de gestión del tiempo» (listas, prioridades, cuándo y cómo) con la planificación contingente. La primera mejora el compromiso y el rendimiento, «pero su efecto se debilita con muchas interrupciones»; la contingente no depende del nivel de interrupciones (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:%22Parke%20MR%22). ALTA.
- **Corrección**: cambiar «franjas horarias» por «planificación clásica de gestión del tiempo» y «solo si» por «su efecto se debilita» en las l. 20, 46, 142 y 146. El «cambio clave» (plan si-entonces en el brief) se mantiene.

**M5 · E08-35 · DISCREPANCY · media**
- **Dice**: el efecto es mayor «sobre todo en quienes desconectan mal» (l. 227), y en la tabla 6.2, «sobre todo en quien desconecta mal» (l. 59).
- **Verificación independiente**: 103 empleados y 1.127 metas. El efecto aparece **solo en personas con alta implicación con el trabajo (job involvement)** (https://api.crossref.org/works?query.bibliographic=Smit%20leaving%20work%20at%20work y resultados de BPS Research Digest y ScienceDaily). MEDIA.
- **Corrección**: «sobre todo en quien está muy implicado en su trabajo». Encaja mejor con el perfil de fundador, y el paso «aparca lo pendiente» se mantiene.

**M6 · E08-44 · DISCREPANCY (OVERCLAIM) · media**
- **Dice**:
  - l. 261: Körner 2022 «no encontró efectos sobre testosterona, cortisol ni indicadores fisiológicos, solo sobre sentirse más poderoso».
  - Tabla 7.3: «sin efecto en hormonas ni conducta […] refutado (en lo hormonal y conductual)» (l. 66).
  - Tabla de mitos: «no cambia hormonas ni conducta (Körner, 2022)» (l. 378).
  - Texto de Ucoach: «no cambia tus hormonas ni cómo te ven» (l. 281).
  - Índice: el título está mal formado (l. 569).
- **Verificación independiente**: Körner et al. encuentran efectos en el autoinforme **y en la conducta** (g = 0,35 en conjunto), pero no en los indicadores fisiológicos ni hormonales. Los efectos en conducta podrían deberse a sesgo de publicación o a valores atípicos. Título exacto: «Dominance and prestige: Meta-analytic review of experimentally induced body position effects on behavioral, self-report, and physiological dependent variables», *Psychol Bull* 148(1-2):67-85 (https://api.crossref.org/works?query.bibliographic=K%C3%B6rner%20power%20posing ; https://www.eurekalert.org/news-releases/952692). ALTA en el título y MEDIA en las cifras. Ranehill (N = 200) y el número especial de CRSP de 2017 no encuentran efecto en conducta.
- **Corrección**: «refutado en lo hormonal; dudoso en lo conductual». Texto de Ucoach: «no cambia tus hormonas, y su efecto en lo que haces es dudoso». Corregir también el título. La decisión de no recomendarlo se mantiene.

**M7 · E08-50 · DISCREPANCY · media**
- **Dice**: «Entrevista motivacional (Lundahl et al., 2010): 119 estudios, efecto medio pequeño (g ≈ 0,22)» (l. 298).
- **Verificación independiente**: g = 0,28 frente a comparadores débiles y g = 0,09, no significativo, frente a tratamientos específicos (https://api.crossref.org/works?query.bibliographic=Lundahl%20motivational%20interviewing). ALTA.
- **Corrección**: dar las dos cifras. Los principios 1 y 7 se mantienen.

**M8 · E08-57 · DISCREPANCY · media**
- **Dice**: «Los terapeutas responden bien el 93 % de las veces y los bots, menos del 60 %» (l. 310).
- **Verificación independiente**: terapeutas, 93 %. gpt-4o y llama3.1-405b dan menos del 80 % de respuestas adecuadas en conjunto, alrededor del 80 % ante ideación suicida y alrededor del 45 % ante delirios. Los bots comerciales de terapia rondan el 50 % (Noni, alrededor del 40 %). Estigma: 38 % en gpt-4o y 75 % en llama3.1-405b (https://arxiv.org/pdf/2504.18412). ALTA.
- **Corrección**: desglosar las cifras. La regla de derivación fija sale reforzada (delirios ≈45 %).

**M9 · E08-72 · ERROR · media**
- **Dice**: «Los primeros estudios de Rogelberg y colegas (2006) encontraron que la frecuencia de reuniones se asocia a más fatiga y carga percibida» (l. 165). No está en el índice.
- **Verificación independiente**: en Rogelberg et al. 2006 (JAP 91(1)), «ni el tiempo ni el número de reuniones se relacionaron de forma consistente con las actitudes y el bienestar laborales»; ese estudio no midió fatiga. La relación con la fatiga y la carga es de Luong y Rogelberg 2005 (*Group Dynamics* 9(1)), un estudio de diario (https://www.interruptions.net/literature/Rogelberg-JAP06-2006-00819-008.pdf ; https://api.openalex.org/works/doi:10.1037/1089-2699.9.1.58). ALTA.
- **Corrección**: atribuir la fatiga a Luong y Rogelberg 2005, decir lo que encontró el estudio de 2006 (pesa la eficacia percibida de la reunión) y añadir las dos al índice.

**M10 · E08-02 · PROVENANCE (y UNVERIFIABLE) · media**
- **Dice**: «En empresas de todos los tamaños, la mediana supera el 50 %» (l. 17). También «las reuniones suponen más del 50 % del tiempo en la mediana y alrededor del 80 % del tiempo está planificado», con la etiqueta `verified` (l. 90).
- **Verificación independiente**: el WP de NBER (2017) no da la cifra del CEO mediano. Las reuniones son «just over 40 %» en el cuartil inferior y el 65 % en el superior, y el tiempo planificado es 0,764 (bruto) y 0,782 (estimado) en la tabla B.3 (https://conference.nber.org/conf_papers/f93027/f93027.pdf). La JPE no se abrió. La muestra no es «de todos los tamaños». MEDIA.
- **Corrección**: dar el rango por cuartiles y el 76-78 % de tiempo planificado, quitar «de todos los tamaños» y anotar que la mediana no se ha confirmado.

**M11 · E08-52 · OVERCLAIM (e INTERNAL) · media**
- **Dice**:
  - l. 22: «en 2026 un ensayo de tres brazos con directivos no encontró ventaja de la IA frente al control […]. La IA rinde en la parte estructurada (metas, seguimiento y constancia) y flojea en la relación».
  - l. 304: «la alianza fue mayor con el humano».
  - Índice (l. 583): el título aparece como un marcador entre corchetes.
- **Verificación independiente**:
  - Existe y el DOI resuelve: «A randomised controlled comparison of the effectiveness of human and AI chatbot coaching with goal attainment, wellbeing and self-efficacy», *HRDI* 29(4):754-783, en línea el 28-02-2026, con N = 114. La efectividad es sustancial «but only for human coaching».
  - Que haya tres brazos y que sean altos directivos solo lo dice una fuente secundaria (BAJA). **La alianza no aparece en el resumen** (https://api.crossref.org/works/10.1080/13678868.2026.2633990).
- **Corrección**: dejar «solo el coaching humano fue eficaz» y marcar la alianza y los tres brazos como no verificados. En el resumen 6: con estudiantes, la IA rinde en metas y seguimiento; con directivos, en el único ensayo, no fue eficaz. Que flojee precisamente en la relación es una hipótesis. Corregir el título en el índice.

**M12 · INTERNAL · media**
- **Dice**: el resumen 8 incluye entre los mitos «“72 % más productividad” con días sin reuniones» (l. 24).
- **Verificación independiente**: el estudio da +71 % con 2 días, +73 % con 3 y +74 % con 4. Ninguna fila da 72 % (https://sloanreview.mit.edu/article/the-surprising-impact-of-meeting-free-days/). La tabla de mitos dice «71 %» (l. 383). Es probable que el 72 % venga del porcentaje de reuniones de Porter y Nohria.
- **Corrección**: «71 %», como en la tabla de mitos.

**M13 · INTERNAL · media**
- **Dice**: «Nunca más de 3 métricas en la vista semanal» (l. 367). En cambio, la `revision_semanal` usa «GROW con datos (destacados, foco, % de reuniones, desconexión y energía)» (l. 466), que son 5.
- **Verificación independiente**: no aplica (coherencia interna).
- **Corrección**: la revisión semanal usa las 3 métricas activas del usuario, elegidas entre esas cinco.

**M14 · INTERNAL · media**
- **Dice**: el apagado solo dura «3 minutos» (l. 240) y la pregunta de aprendizaje «1 minuto» (l. 336), pero el `cierre_dia`, que los incluye a los dos junto con otros tres pasos, tiene «Máximo 3 minutos» (l. 463).
- **Corrección**: apagado de 2 minutos; `cierre_dia` de 5 minutos como máximo con todos los pasos.

**M15 · INTERNAL · media**
- **Dice**: principio 2, «Una pregunta cada vez. No encadenar tres preguntas en un mensaje» (l. 402). El banco de preguntas y las plantillas encadenan dos o más: l. 153, 208, 245, 428, 430 y 431.
- **Corrección**: redefinir el principio: cada mensaje termina con una sola pregunta, y las preguntas encadenadas del banco, del WOOP del brief y del detector de desconexión se hacen de una en una, en mensajes sucesivos.

**M16 · INTERNAL (conclusión que no se sigue) · media**
- **Dice**: «El efecto es mayor cuando lo guía una persona, y aquí la IA ocupa ese papel (`inferred`)» (l. 207). Sostiene el «cambio clave» del resumen 4 (l. 20).
- **Verificación independiente**: Wang et al. 2021 comparan la interacción con un experimentador humano (g = 0,465) con un documento (g = 0,277). No hay brazo con IA (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8149892/fullTextXML).
- **Corrección**: presentarlo como hipótesis que hay que medir en la validación, no como fundamento.

**M17 · INTERNAL (atribución) · media**
- **Dice**: estado «Deuda» con «menos de 6 horas o media de 7 días por debajo de 6,5» y «Fuente: Gish 2019 y Killgore 2010» (l. 126).
- **Verificación independiente**: Gish 2019 habla de dormir al menos 7 horas cada noche (https://sciencedaily.com/releases/2019/08/190805112208.htm), y Killgore no da umbrales (M2).
- **Corrección**: los umbrales son una decisión de diseño (`inferred`). Citar Gish (≥ 7 h) y Van Dongen (≤ 6 h).

### Bajas

| id | clase | Dice (línea) | Verificación independiente | Corrección |
|---|---|---|---|---|
| B1 · E08-01/67 | PROVENANCE | Porter y Nohria con `verified` a partir de MGMA y McKinsey (l. 89, 499) | Las cifras cuadran (MEDIA), pero vienen de MGMA y de extractos en bobmorris.biz; HBR está tras un muro de pago (https://www.mgma.com/articles/test-of-time-harvard-study-reveals-how-ceos-spend-their-days-on-and-off-work ; https://bobmorris.biz/?p=55369) | Bajar a `reported` y añadir la fuente |
| B2 · E08-04/22/23/52/55 | INTERNAL | Solidez alta con confianza `reported`: Van Dongen, Sheeran 2024, Rogelberg 2026, de Haan 2026 y Cheng 2026 (l. 113, 143, 164, 304, 309) | Las cinco se verificaron en origen o en su resumen oficial (Europe PMC; https://kops.uni-konstanz.de/bitstreams/d703c468-46e9-47fc-8900-d32d7d19c8d9/download ; https://www.annualreviews.org/deliver/fulltext/orgpsych/13/1/annurev-orgpsych-031925-091223.pdf ; https://api.crossref.org/works/10.1126/science.aec8352) | Subir a `verified` y completar la referencia: Sheeran, ERSP 36(1), 2025; Cheng, DOI 10.1126/science.aec8352, 26-03-2026; Rogelberg, 13:415-442 |
| B3 | INTERNAL | Remisiones a «§ 12» (l. 69, 314) y a «§ 12.4» (l. 249) | No aplica | § 14.1, § 14 y § 14.4 |
| B4 | INTERNAL | «14 lecturas directas» (l. 7), con solo 9 fuentes `verified` en el índice | No aplica | Anotar el recuento real y remitir a este QA |
| B5 | INTERNAL | Bloque de foco de ≥ 25 min (l. 360), ≥ 60 min (l. 32, 99) y 90 min (l. 100) | No aplica | Minutos de foco en bloques de ≥ 60 min, como en `auditar_agenda` |
| B6 | INTERNAL | WOOP «razonable-sólido» (l. 53) frente a «razonable» (l. 204) | No aplica | «razonable» |
| B7 | INTERNAL | Tendencias «a partir de 3 días» (l. 441) frente a «al menos 3 semanas» (l. 368) | No aplica | Distinguir la tendencia de un indicador de la relación entre indicadores |
| B8 · E08-41 | DISCREPANCY | «Poynter, Pasqualini y Smith» (l. 256, 566) | Crossref da 2 autores: M. Poynter y M. Smith Pasqualini, DOI 10.58734/plc-2025-0011 (https://api.crossref.org/works?query.bibliographic=Poynter%20Pasqualini%20Smith%20replication%20Brooks) | «Poynter y Smith Pasqualini» |
| B9 · E08-51 | ERROR | «Escala de consecución de metas (GAS) […] como en Terblanche 2022» (l. 489) | El instrumento está adaptado de Grant et al. (2009), con % de éxito de 0 a 100; «no es un GAS» (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0270255) | Corregir el nombre del instrumento |
| B10 · E08-70 | DISCREPANCY | «un 40 % de usuarios que mira el correo antes de las 6:00» (l. 92) | Es el 40 % de quienes están conectados a las 6:00 (https://www.microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday) | Precisar el denominador y citar WorkLab |
| B11 · E08-60 | DISCREPANCY | «El mecanismo propuesto es la autoeficacia» (l. 323) | Hay dos mecanismos: el cognitivo (mejor comprensión de la tarea) y el emocional (autoeficacia). La mejora es del 23 % (https://api.crossref.org/works?query.bibliographic=Di%20Stefano%20Gino%20Pisano%20Staats) | Añadir el mecanismo cognitivo |
| B12 · E08-61 | UNVERIFIABLE | «Un análisis posterior sugiere que el efecto aparece sobre todo frente a no leer nada» (l. 324) | El resumen agrupa los dos comparadores (g = 0,15-0,16) y no informa de que dependa del comparador (https://api.crossref.org/works?query.bibliographic=Dodell-Feder%20Tamir) | Quitarlo y dar la cifra frente a ambos comparadores |
| B13 · E08-46 | UNVERIFIABLE | «el enfoque integrador obtuvo g = 0,71» (l. 291); tabla 8.3: «el integrador rinde bien» (l. 70) | 20 estudios y 957 participantes. Ningún enfoque es significativamente superior, tampoco el integrador. No se obtuvo el g por enfoque (https://scienceforwork.com/blog/not-all-coaching-is-created-equal-is-it) | Quitar el 0,71 o marcarlo como no verificado |
| B14 · E08-62 | UNVERIFIABLE | «La mayoría de los estudios son de salud» (l. 344) | No figura en el resumen (Europe PMC, PMID 26479070) | Marcarlo como no verificado |
| B15 · E08-42 | PROVENANCE | «Reúne 35 estudios y 5.638 personas», con `verified` (l. 257) | El verificador extrajo 44 tamaños de efecto de ECA, pero no el número de estudios ni de participantes (https://www.nature.com/articles/s41598-024-58408-w.pdf) | Dar los 44 tamaños de efecto y marcar el N como no comprobado |
| B16 · E08-19 | DISCREPANCY | «La formación en gestión del tiempo tiene un efecto pequeño» (l. 141) | «time management training makes people feel more in control of their time» (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7799745/fullTextXML) | Usar la frase verificada |
| B17 · E08-21/22 | INTERNAL | «d = 0,65 en 2006 frente a 0,27 en conducta en 2024» (l. 47) | Compara un efecto global con uno solo de conducta. Los globales son 0,65 y 0,36; con RoBMA, 0,15 (KOPS, arriba) | Comparar global con global y dar el RoBMA |
| B18 | OVERCLAIM | «Desconectar es la palanca de recuperación más sólida» (l. 21) | Wendsche 2017 es correlacional (https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.02072/full) | «el factor de recuperación con la asociación más sólida (datos correlacionales)» |
| B19 | INTERNAL | El mito «Más horas, más resultados» se refuta con datos de sueño (l. 385) | No aplica | Añadir que trabajar fuera de horario dificulta la desconexión (Wendsche) y reconocer que no hay estudio directo |
| B20 | INTERNAL | Resumen 1: «proteger un bloque de trabajo a solas, no solo sugerirlo» (l. 17), frente al principio de autonomía (l. 416) y a datos solo de grandes empresas (l. 94) | No aplica | «proponerlo y protegerlo si el usuario acepta»; indicar que los datos son de grandes empresas |
| B21 · E08-65/66/88 | MISSING | Sin fuente: el 024 y el 112 (l. 449), la ortosomnia (l. 351) y «releer es la estrategia que peor retiene» (l. 326). Faltan en el índice Luong y Rogelberg 2005, Rogelberg 2006, Weinshall-Margel y Shapard, CRSP 2017 y Carney, Bluedorn 1999, Driskell 1994 y Mark (Gallup 2006) | Todo verificado: https://www.sanidad.gob.es/linea024/home.htm ; Baron et al., J Clin Sleep Med 2017 (PubMed 27855740) ; Dunlosky 2013 y Roediger y Karpicke 2006 (Europe PMC, PMID 26173288 y 16507066) ; https://news.gallup.com/businessjournal/23146/too-many-interruptions-work.aspx ; https://faculty.haas.berkeley.edu/dana_carney/pdf_my%20position%20on%20power%20poses.pdf ; https://api.openalex.org/works/doi:10.1037/0021-9010.79.4.481 | Citar en el texto y añadirlas al índice |
| B22 | STALE | La lista «Pendiente de verificar» (l. 600-605) no recoge lo resuelto en este QA (Sheeran, de Haan, Bluedorn y Driskell) ni lo que sigue abierto | Ver «No verificable» | Actualizar la lista |

## Sólido

Verificado y sin cambios de fondo:
- **Uso del tiempo:**
  - Porter y Nohria: 72 % de reuniones, 37 a la semana, 36 % reactivo, 62,5 h semanales, 27 CEO durante 13 semanas y las cifras de apoyo de E08-67 (MEDIA).
  - Bandiera: N, países, perfiles, +7 % de ventas con efecto diferido y 17 % de desajuste (E08-03, ALTA).
  - Microsoft WTI 2025: una interrupción cada 2 minutos y 275 al día.
- **Sueño y juicio:** Gish 2019, incluido el umbral de 7 horas (E08-05 y E08-89); Barnes 2011 (E08-07); Christian y Ellis 2011, en lo esencial (E08-08).
- **Mitos refutados:**
  - Agotamiento del ego: 36 laboratorios, N = 3.531, d = 0,06 (E08-10).
  - Jueces israelíes y sus críticas (E08-11).
  - Origen y significado de los «23 minutos» (E08-15).
  - Réplica fallida del «brain drain» (E08-17).
  - Multitarea mediática: d = 0,17, que se anula al corregir (E08-18).
  - Power posing hormonal: Ranehill, CRSP y Carney (E08-43 y E08-82).
  - OKR: casi sin evidencia; Sears solo en un blog de consultor (E08-31 y E08-76).
- **Atención y planificación:**
  - Leroy (E08-13) y Mark 2008 (E08-14).
  - Aeon 2021 en todas sus correlaciones (E08-19).
  - Gollwitzer y Sheeran 2006 (E08-21) y Sheeran 2024-2025 (E08-22).
  - Locke y Latham (E08-26), Wang 2021 con todas sus cifras (E08-27), Buehler (E08-28), Sitkin (E08-30) y Dai (E08-32).
- **Reuniones:** Rogelberg 2026 existe y destaca la preparación (E08-23); los datos de Laker 2022 y sus limitaciones (E08-24); Oppezzo y Schwartz (E08-25); Bluedorn 1999 (E08-74).
- **Recuperación:**
  - Wendsche 2017, con todas las correlaciones (E08-33), Masicampo y Baumeister (E08-34) y Albulescu 2022 (E08-36).
  - De Bloom 2009 (E08-37) y Fritz y Sonnentag 2006 (E08-78).
  - Sonnentag 2018 y 2022 (E08-38 y E08-77).
  - Weinberger 2018 (E08-39), Stephan 2018 (E08-80) y Williamson et al. 2021 (E08-81).
- **Presión:** Brooks 2014 (E08-40), la réplica de 2025 (E08-41), Bosshard y Gomez en sus efectos (E08-42), Rupprecht 2021 (E08-45) y Driskell 1994 (E08-83).
- **Coaching:**
  - Theeboom (E08-84), Jones (E08-85), Grant 2009 (E08-86) y Grant 2012 (E08-49).
  - De Haan y Nilsson 2023: 37 ECA, g = 0,59, con sesgo (E08-47).
  - Graßmann 2020: r = 0,41 y −0,29 (E08-48).
- **IA:**
  - Terblanche 2022 (E08-51): ηp² de 0,269 frente a 0,265.
  - Wysa (E08-53) y Therabot, con la cita de autonomía (E08-54).
  - **Cheng et al., *Science* 2026, existe**: 391(6792), 11 modelos, 49 %, 3 experimentos y N = 2.405 (E08-55 y E08-56). El título dice literalmente «promotes dependence», así que la objeción del mapa sobre «aumenta la dependencia» queda descartada.
  - OpenAI y GPT-4o en abril de 2025 (E08-87).
- **Aprendizaje y métricas:** Adesope (E08-58), Pan y Rickard (E08-59), Di Stefano en su cifra (E08-60), Harkin (E08-62), Heidemeier y Moser (E08-63) y Amabile y Kramer (E08-64).
- **Derivación:** 024, gratuita, 24 h, desde el 10-05-2022, y 112 (E08-65).

## No verificable

| id | Qué | Qué hacer |
|---|---|---|
| E08-68 | 28 % del tiempo a solas de Porter y Nohria (l. 89) | Solo aparece en resúmenes de prensa, y HBR está tras un muro de pago. Se mantiene como «no verificado». No sostiene ninguna regla. |
| E08-29 | Veinott et al. 2010, pre-mortem con 178 participantes (l. 55, 198) | Solo fuentes secundarias, todas coincidentes, y el PDF no es accesible. Se mantiene «débil-razonable». El ritual `pre_mortem` es puntual y se puede conservar con esa etiqueta. |
| E08-16 (parte) | «Cerca de la mitad de las interrupciones son autointerrupciones» (l. 44, 138) | Solo aparece en entrevistas. Marcarlo. |
| E08-71 | Contenido de Bryan y Locke 1967 (l. 144) | Solo se encontró la ficha bibliográfica. Ya estaba marcado como «solo el abstract». |
| E08-73 | «Solo la mitad del tiempo de reunión se aprovecha» (l. 165) | Solo aparece en resúmenes de charlas. Marcarlo como no verificado. |
| E08-08 (parte) | «En 171 enfermeras, dormir menos de 6 horas» (l. 116) | El N viene de fuentes secundarias y el umbral de 6 horas no se verificó. Reformular sin el umbral. |
| E08-02 (parte) | Mediana de reuniones de los CEO (Bandiera) | Ver M10. |
| E08-52 (parte) | Tres brazos con altos directivos y alianza mayor con el humano | Ver M11. |

## Falta

- **Población:** casi toda la evidencia es de CEO de grandes empresas, estudiantes, enfermeras, médicos o deportistas. Solo Gish 2019 y Weinberger 2018 estudian emprendedores. Conviene decirlo en el resumen y no solo en el § 3.
- **IA:** no hay evidencia de que la regla antiadulación, la regla fija de derivación o un WOOP conducido por IA funcionen en un LLM. La fase de validación (§ 14.7) debería medirlo explícitamente.
- **Efectos adversos del coaching y dependencia del propio Ucoach:** solo se tocan de pasada.
- **Fuentes del índice:** faltan las que enumera B21.
- **Las 47 afirmaciones** del recuento del preflight (136) que no entraron en la extracción (89) siguen sin verificar.

## Correcciones a aplicar (línea a línea)

1. **l. 7:** anotar el recuento real de fuentes `verified` y remitir a este QA (B4).
2. **l. 17:** Bandiera por cuartiles, sin «de todos los tamaños», y «proponer y proteger si el usuario acepta» (M10, B20).
3. **l. 18:** Van Dongen, «6 horas o menos… hasta dos noches» (M1).
4. **l. 19:** «la hora y la carga continuada», según datos observacionales (M3).
5. **l. 20:** planificación clásica en lugar de franjas, y WOOP con IA como hipótesis (M4, M16).
6. **l. 21:** «asociación más sólida (datos correlacionales)» (B18).
7. **l. 22:** de Haan 2026 verificado; «flojea en la relación» pasa a ser hipótesis (M11).
8. **l. 24:** 72 % → 71 % (M12).
9. **l. 35, 37 y 41:** tabla de sueño (M1, C1, M3).
10. **l. 46, 47, 53 y 59:** tabla de atención, metas y recuperación (M4, B17, B6, M5).
11. **l. 66, 69, 70 y 73:** tabla de presión y coaching (M6, B3, B13, M11).
12. **l. 89:** Porter y Nohria a `reported`, con fuente añadida (B1).
13. **l. 90:** Bandiera por cuartiles y 76-78 % de tiempo planificado (M10).
14. **l. 92:** WTI, 40 % de quienes están conectados (B10).
15. **l. 113, 115, 116 y 117:** Van Dongen, Barnes 2016, Christian y Ellis, y Killgore (M1, C1, E08-08, M2).
16. **l. 121:** Linder, con la odds ratio y los mecanismos verificados (M3).
17. **l. 126 y 128:** estado «Deuda» y texto del brief (M17, C1).
18. **l. 138, 141, 142, 143 y 146:** autointerrupciones, Aeon, Parke, Sheeran y timeboxing (E08-16, B16, M4, B2, M4).
19. **l. 164 y 165:** Rogelberg 2026 a `verified`; Rogelberg 2006 y Luong y Rogelberg 2005 (B2, M9, E08-73).
20. **l. 207:** WOOP con IA como hipótesis (M16).
21. **l. 227 y 240:** Smit y duración del apagado (M5, M14).
22. **l. 249:** § 14.4 (B3).
23. **l. 256, 257, 261 y 266:** Poynter, Bosshard, Körner y la solidez del power posing (B8, B15, M6).
24. **l. 281:** texto de Ucoach sobre el power posing (M6).
25. **l. 291, 298, 304, 309, 310 y 314:** Wang 2022, Lundahl, de Haan 2026, Cheng a `verified`, Moore y § 14 (B13, M7, M11, B2, M8, B3).
26. **l. 323, 324 y 326:** Di Stefano, Dodell-Feder y fuente de releer (B11, B12, B21).
27. **l. 344 y 351:** Harkin y ortosomnia (B14, B21).
28. **l. 360 y 441:** bloque de foco y tendencias (B5, B7).
29. **l. 378, 385 y 391:** tabla de mitos (M6, B19, M11).
30. **l. 402:** principio «una pregunta cada vez» (M15).
31. **l. 449:** fuente del 024 (B21).
32. **l. 463, 466 y 489:** `cierre_dia`, `revision_semanal` y el instrumento de Terblanche (M14, M13, B9).
33. **Índice:**
    - l. 499: Porter (B1).
    - l. 505: Van Dongen a V (B2).
    - l. 512: enlace de Glöckner (bloqueo).
    - l. 527: Sheeran (B2).
    - l. 528: DOI de Bryan y Locke (bloqueo).
    - l. 532: Rogelberg 2026 (B2).
    - l. 543: Veinott, «fuente no accesible» (bloqueo).
    - l. 566: Poynter (B8).
    - l. 569: Körner (M6).
    - l. 583: de Haan 2026 (M11).
    - l. 587: Cheng (B2).
    - Fuentes nuevas (B21).
    - Lista de pendientes (B22).

## Re-verificación (2026-11-19)

Las correcciones se aplicaron con Edit sobre `08-rendimiento-coaching.md`, sin reescribir secciones enteras. Cada cambio lleva la marca «(corregido tras QA 2026-11-19)», que aparece 78 veces en el informe, y cita la URL que consultó el verificador (`qa/E-respuestas.md`).

Las etiquetas se ajustaron a lo que se consultó de verdad:
- **Bajó a `reported`:** Porter y Nohria.
- **Subieron a `verified`:** Van Dongen, Barnes 2016, Killgore, Linder, Parke, Sheeran, Rogelberg 2026, Lundahl, de Haan 2026 (solo el resumen), Cheng 2026, Moore y Dodell-Feder.

El índice añade las fuentes 77 a 89.

Comprobado con grep en el informe:
- Guiones largos: 0.
- Ya no aparece ninguno de los textos erróneos: «72 % más productividad», «no se ven peor», «aunque tú no lo notes», «franjas horarias», «§ 12.4», «menos del 60», «(GAS)», «Máximo 3 minutos», «hormonas ni conducta», «todos los tamaños», los enlaces muertos.
- La única remisión a «§ 12)» que queda (l. 202, Harkin) es correcta, porque las métricas están en el § 12.

| hallazgo | estado | línea nueva |
|---|---|---|
| C1 · Barnes 2016: «él no lo nota» | corregido: los observadores ven menos carisma; el estudio no mide la autoevaluación. Texto del brief cambiado | 37, 115, 128 |
| M1 · Van Dongen, 6 h | corregido: «6 horas o menos (4 y 6 h juntas)… hasta 2 noches»; `verified` | 18, 35, 113, 126 |
| M2 · Killgore | corregido con el resumen verificado; ya no es fuente de la regla «Deuda» | 117, 126 |
| M3 · Linder +26 % | corregido: odds ratio 1,26, sin «innecesarios», mecanismos verificados; resumen 3 matizado | 19, 41, 121 |
| M4 · Parke, «franjas horarias» | corregido: planificación clásica de gestión del tiempo cuyo efecto se debilita | 20, 46, 142, 146 |
| M5 · Smit, «desconectan mal» | corregido: alta implicación con el trabajo | 59, 227 |
| M6 · Körner, «ni conducta» | corregido: efecto en conducta dudoso, título exacto y texto de Ucoach | 66, 260, 265, 280, 377, 568 |
| M7 · Lundahl g ≈ 0,22 | corregido: 0,28 frente a comparadores débiles y 0,09 n. s. frente a tratamientos | 297 |
| M8 · Moore, «menos del 60 %» | corregido: desglose por modelo y por síntoma | 309 |
| M9 · Rogelberg 2006 y fatiga | corregido: Luong y Rogelberg 2005; lo que dice 2006 | 165, 603, 604 |
| M10 · Bandiera, mediana | corregido: cuartiles y 76-78 % planificado; mediana marcada como no confirmada | 17, 90 |
| M11 · de Haan 2026 e «IA flojea en la relación» | corregido: «solo el coaching humano fue eficaz»; brazos y alianza no verificados; la relación queda como hipótesis | 22, 73, 303, 390, 582 |
| M12 · «72 %» | corregido: 71 % | 24 |
| M13 · 3 métricas frente a 5 | corregido: la revisión usa las 3 métricas activas | 366, 465 |
| M14 · `cierre_dia` de 3 minutos | corregido: apagado de 2 minutos y cierre de 5 como máximo | 239, 462 |
| M15 · «una pregunta cada vez» | corregido: una pregunta por mensaje; las encadenadas, en mensajes sucesivos | 401 |
| M16 · WOOP guiado por IA | corregido: pasa a ser una hipótesis que hay que medir | 20, 207 |
| M17 · umbrales del estado «Deuda» | corregido: decisión de diseño (`inferred`), con Gish (≥ 7 h) y Van Dongen | 126 |
| B1 · Porter `verified` | corregido: `reported`, más bobmorris | 89, 498 |
| B2 · etiquetas de confianza | corregido: Sheeran, Rogelberg, de Haan y Cheng con referencia completa y V | 143, 164, 303, 308, 526, 531, 582, 586 |
| B3 · remisiones a § 12 | corregido: § 14.1, § 14.4 y § 14 | 69, 248, 313 |
| B4 · recuento de fuentes | corregido | 7 |
| B5 · bloque de foco | corregido: ≥ 60 min | 359 |
| B6 · solidez del WOOP | corregido: «razonable» | 53 |
| B7 · 3 días frente a 3 semanas | corregido | 440 |
| B8 · autores de la réplica de 2025 | corregido | 255, 565 |
| B9 · GAS en Terblanche | corregido | 488 |
| B10 · WTI 40 % | corregido | 92 |
| B11 · mecanismo de Di Stefano | corregido | 322 |
| B12 · Dodell-Feder | corregido | 323 |
| B13 · Wang 2022 g = 0,71 | corregido: marcado como no verificado; el integrador no es superior | 70, 290 |
| B14 · Harkin y salud | corregido: no verificado | 343 |
| B15 · Bosshard, N | corregido: 44 tamaños de efecto; N sin comprobar | 256 |
| B16 · formación en gestión del tiempo | corregido | 141 |
| B17 · Gollwitzer frente a Sheeran | corregido: global frente a global, y RoBMA | 47 |
| B18 · «palanca» de desconexión | corregido | 21 |
| B19 · mito «más horas» | corregido | 384 |
| B20 · proteger frente a autonomía | corregido | 17 |
| B21 · fuentes que faltaban | corregido: 024, ortosomnia, Dunlosky y Roediger, y fuentes 77 a 89 en el índice | 325, 350, 448, 599-613 |
| B22 · lista de pendientes | corregido | 615-623 |
| Bloqueo · DOI de Bryan y Locke | corregido: codificado | 527 |
| Bloqueo · enlace de Glöckner | corregido: journal.sjdm.org | 511 |
| Bloqueo · Veinott en researchr.org | corregido: sin enlace, marcado «fuente no accesible» | 542 |
| E08-08 · umbral de 6 h en enfermeras | corregido: se quita el umbral no verificado | 116 |
| E08-16 · autointerrupciones | marcado como no verificado (sigue sin verificar) | 44, 138 |
| E08-68 · 28 % a solas | marcado como no verificado (sigue sin verificar; no sostiene ninguna regla) | 89 |
| E08-73 · «la mitad del tiempo de reunión» | marcado como no verificado | 165 |

**Nota recalculada** contando solo lo que queda abierto, que son 0 hallazgos y 0 bloqueos:

`nota.py --claims 136 --verificadas 84 --portantes 66 --portantes-ok 64 --criticas 0 --medias 0 --bajas 0 --bloqueos 0` → **8.6 / 10**, limitada por la cobertura (techo de 8,64).

Para subirla hay que verificar más, no corregir más:
- el PDF de Veinott (ISCRAM 2010);
- el libro de Mark (2023);
- las 47 afirmaciones del recuento del preflight que no entraron en la extracción.

## Comprobación de la corrección por un tercero (sesión principal, 2026-11-19)

- Desde la sesión principal, que no escribió el informe ni sus correcciones, se cotejó la crítica C1 (Barnes et al., 2016) con la respuesta E08-06 del verificador independiente. Las líneas 37, 115 y 128 ya no dicen que el líder «no se ve peor»: dicen que son los observadores quienes le atribuyen menos carisma. Coincide con la fuente.
- El veredicto sigue en **CORREGIR ANTES DE ENTREGAR**, porque dos portantes siguen sin verificar: el pre-mortem de Veinott 2010 y la proporción de autointerrupciones de Gloria Mark. La síntesis las usará como «no verificado». El pre-mortem queda como ritual opcional con evidencia «débil-razonable» y no se apoya ninguna regla en la cifra de autointerrupciones.
