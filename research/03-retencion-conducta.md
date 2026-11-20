# Ucoach · Línea 3 · Retención, cambio de conducta y eficacia del coaching con IA

**Fecha:** 19 de noviembre de 2026
**Base:** documento de producto Ucoach v0.1 (Google Doc `1S6MFA-6j9KQh4pYVxCYngqUF8hHvjSIaFO7EjO2owyw`) y alcance en `research/00-scope.md` (posicionamiento: eficiencia y excelencia profesional con energía y sueño óptimos).
**Método:** 29 búsquedas web, consulta directa de resúmenes en Europe PMC por DOI o PMID, y verificación con WebFetch de las fuentes clave. Se agotó el cupo de búsquedas web de la sesión antes de cubrir del todo cuatro puntos: retención de Oura y WHOOP, abandono del autoseguimiento (Epstein), receptividad a notificaciones (Mehrotra, Künzler) y el texto completo de Sifted 2025. Esos huecos se señalan donde aparecen.

**Etiquetas de confianza**
- `verified`: cifra comprobada en el resumen o en la página original durante esta sesión.
- `reported`: procede de fuentes secundarias o de memoria bibliográfica sin comprobar aquí.
- `inferred`: conclusión propia a partir de los datos.

---

## Resumen

1. **El objetivo de más del 40 % de usuarios activos semanales a las 4 semanas es bajo para la cohorte de validación y alto para las instalaciones orgánicas.** Las apps de salud y bienestar retienen entre el 3 % y el 7 % de los usuarios a los 30 días (corregido tras QA 2026-11-19). Las apps de salud mental retienen un 3,3 % (Baumel, 2019). En cambio, 20 emprendedores reclutados a mano y entrevistados cada semana se comportan como participantes de un ensayo, donde el abandono ronda el 26-48 %. Hay que medir las dos cohortes por separado y alargar la validación a 8-12 semanas.
2. **El efecto de un aviso se gasta.** En HeartSteps (2019), una sugerencia para caminar al principio aumentaba un 107 % los pasos de los 30 minutos siguientes, y el efecto cayó un 3 % cada día hasta dejar de detectarse hacia el día 29, es decir, en unas 4 semanas (corregido tras QA 2026-11-19; https://pmc.ncbi.nlm.nih.gov/articles/PMC6401341/). Las sugerencias contra el sedentarismo, el equivalente a la "pausa activa cada hora" de Ucoach, no tuvieron efecto detectable.
3. **La frecuencia de los avisos importa menos que su coste y su pertinencia.** En los estudios de muestreo de experiencias, hacer más preguntas al día no reduce el cumplimiento, pero hacer cuestionarios más largos sí (Eisele, 2022; Wrzus y Neubauer, 2023). Que el cron revise el estado cada 30 minutos está bien. El problema sería enviar algo cada 30 minutos: conviene fijar un presupuesto de 1 a 3 avisos al día.
4. **Hay evidencia de que el coaching automatizado funciona, pero aún no hay ensayos de coaches con LLM para este caso de uso.** Un programa de prevención de diabetes guiado por IA no fue inferior al humano y tuvo más finalización (63,9 % frente a 50,3 %; JAMA, 2025), aunque usaba aprendizaje por refuerzo, no un LLM. Therabot (NEJM AI, 2025) redujo los síntomas de depresión frente a la lista de espera con un efecto grande (d≈0,85-0,90; un 51 % según el comunicado de Dartmouth) (corregido tras QA 2026-11-19). En el único ensayo con un LLM centrado en actividad física (Bloom, 2025, N=54), el LLM cambió la mentalidad de los usuarios pero no aumentó la actividad más que el control.
5. **Un hábito tarda una mediana de unos dos meses (y una media de tres a cinco), no una semana (corregido tras QA 2026-11-19).** La mediana para automatizar un hábito es de 59 a 66 días y la media de 106 a 154 días (Singh, 2024). Una revisión semanal que cambia de hábito cada semana va contra esta evidencia. Hay que mantener el mismo hábito entre 8 y 10 semanas como mínimo y medir su automaticidad antes de cambiarlo: a las 8-10 semanas, cerca de la mitad de los usuarios aún no lo habrá automatizado.
6. **Las rachas rotas restan motivación.** Destacar una racha rota reduce la conducta siguiente, y el efecto se suaviza si la racha puede "repararse" (Silverman y Barasch, 2023). En el megaestudio de Milkman (Nature, 2021), la mejor de 54 intervenciones premiaba volver al gimnasio tras faltar.
7. **El autoseguimiento ayuda con la actividad física, pero en el sueño puede generar ansiedad.** Los wearables añaden unos 1.800 pasos al día (Ferguson, 2022). Por otro lado, la ortosomnia, la obsesión por la puntuación de sueño que da el dispositivo, aparece con datos de fiabilidad dudosa (Baron, 2017). Ucoach debe mostrar el sueño como tendencia semanal y dar prioridad a cómo se siente el usuario.
8. **Los fundadores sí pagan por coaching, pero de liderazgo y rendimiento.** El 58 % de los CEO ha recibido coaching pagado (Stanford, 2025). En cambio, más de la mitad de los fundadores dicen haber sufrido burnout en el último año (encuesta de Sifted de 2024, n=156, vía fuente secundaria; la de 2025 no se pudo verificar) (corregido tras QA 2026-11-19). Por eso conviene vender rendimiento y entregar dentro de él la salud y el descanso, que es justo el posicionamiento que fijó Philippe.

---

## Benchmarks de retención

"Retención Dn" es el porcentaje de quienes instalan que vuelven a abrir la app el día n. No son cifras comparables entre sí: cada fuente usa muestras y definiciones distintas.

| Categoría | D1 | D7 | D30 | D90 / largo plazo | Fuente | Año del dato | Confianza |
|---|---|---|---|---|---|---|---|
| Apps de salud mental (93 apps Android con 10.000 instalaciones o más) | n. d. | n. d. (D15: 3,9 %) | **3,3 %** (mediana) | n. d. | Baumel et al., JMIR | 2019 | verified |
| · subtipo "trackers" (ánimo y síntomas) | | | 6,1 % | | Baumel et al. | 2019 | verified |
| · subtipo mindfulness | | | 4,7 % | | Baumel et al. | 2019 | verified |
| · subtipo apoyo entre pares | | | 8,9 % (n=2) | | Baumel et al. | 2019 | verified |
| · uso diario (usuarios activos diarios / instalaciones) | | | | 4,0 % de mediana | Baumel et al. | 2019 | verified |
| Salud y forma física (AppsFlyer) | n. d. | n. d. | **3,9 % iOS / 3,4 % Android** | n. d. | Braze con datos de AppsFlyer vía Business of Apps | 2026 (fecha de la compilación; Braze no indica el año de los datos de origen) | verified |
| Salud y forma física (Adjust) (corregido tras QA 2026-11-19) | 24 % (2022) / 27 % (2024) | n. d. para la categoría (13 % es la media de todas las categorías) | 7 % (2022) | D14: 9 % (2022) | Adjust, https://www.adjust.com/blog/get-the-mobile-app-retention-benchmarks-for-2023/ y https://www.adjust.com/blog/what-makes-a-good-retention-rate/ | 2022 y 2024 | verified |
| Salud y forma física (AppsFlyer) | n. d. | n. d. | 3 % | n. d. | Business of Apps | 2023 | no verificado (fuente bloqueada en el QA de 2026-11-19) |
| Media de todas las industrias (web y app, Mixpanel) | | **28 %** en la semana 1 (50 % en 2022) | | 6-20 % en la semana 8 (Mixpanel 2017); "below 20 percent" en la mayoría de industrias (Mixpanel 2019) | Mixpanel Benchmarks; https://mixpanel.com/blog/whats-a-good-retention-rate/ | 2024 (datos de 2023); semana 8: 2017 y 2019 (corregido tras QA 2026-11-19) | verified |
| Apps para enfermedades crónicas (ensayos y estudios observacionales) | | | | Abandono agregado del **43 %** (49 % en estudios observacionales, 40 % en ensayos) | Meyerowitz-Katz et al., JMIR | 2020 | verified |
| Apps para depresión (ensayos) | | | | Abandono del 26,2 %, **47,8 %** tras corregir el sesgo de publicación | Torous et al., J Affect Disord | 2020 | verified |
| Wearables de actividad | | | | **1 de cada 3** deja de usarlo antes de 6 meses | Endeavour Partners (nota del 15-08-2014) | 2013-2014 | verified (corregido tras QA 2026-11-19) |
| Programa de prevención de diabetes guiado por IA (app, sin LLM) | | | | Inicio del programa: 93,4 % (82,7 % con coach humano). Finalización a 12 meses: **63,9 %** (50,3 % con coach humano) (corregido tras QA 2026-11-19) | Mathioudakis et al., JAMA | 2025 | verified |
| Therabot (LLM, ensayo de 4 semanas con seguimiento a las 8) (corregido tras QA 2026-11-19) | | | | Uso medio de más de 6 h | Heinz et al., NEJM AI, https://pubmed.ncbi.nlm.nih.gov/42932588/ | 2025 | verified |
| Estudios de muestreo de experiencias (EMA): 6 preguntas al día durante 7 días | | cumplimiento del 79 % | | | Wrzus y Neubauer, Assessment | 2023 | verified |
| Registro de calorías (programa web de 6 meses, n=161) (corregido tras QA 2026-11-19) | | | | Registro medio en el 28 % de los días laborables y el 17 % de los fines de semana, concentrado al principio. Con MyFitnessPal, de 5,4 a 1,4 días por semana entre las semanas 4 y 12 | Krukowski et al., Health Psychol 2013, https://pubmed.ncbi.nlm.nih.gov/22545978/ ; revisión JMIR mHealth 2026, https://doi.org/10.2196/64139 | 2013 y 2026 | verified |
| Productividad B2B | No se encontró un benchmark público fiable por categoría. Mixpanel publica la retención a una semana y semanal en B2B, por región, sin desglose por categoría (corregido tras QA 2026-11-19) | | | | Mixpanel, https://mixpanel.com/blog/b2b-benchmarks-2026/ | 2026 | verified |
| Wearables de pago: Oura (corregido tras QA 2026-11-19) | | | | Retención media ponderada de miembros de pago a 12 meses: ~85 % a 30-06-2026 (cohortes mensuales, con reactivaciones). DAU/MAU: 65 %. Son suscriptores de pago con hardware: no comparable con instalaciones gratuitas | S-1/A de Oura en la SEC, https://www.sec.gov/Archives/edgar/data/2133022/000119312526396051/d119865ds1a.htm | 2026 | verified |
| Wearables de pago: WHOOP | No hay datos públicos de cohortes | | | | | | n. d. |

### ¿Es realista el objetivo de más del 40 % de activos semanales a las 4 semanas?

- **Para instalaciones orgánicas del código abierto, no** (`inferred`). Si se parte de las tiendas de apps (D30 del 3-7 %), un 40 % a las 4 semanas multiplicaría varias veces el benchmark de salud y forma física, aunque D30 (volver justo el día 30) y activo semanal en la semana 4 no son la misma métrica (corregido tras QA 2026-11-19). Juega a favor que instalar un servidor MCP con `pipx` filtra a usuarios con mucha intención y que el ritual vive dentro de una IA que el usuario ya abre a diario. Aun así, un 15-25 % de activos semanales en la semana 4 ya sería un buen resultado para una herramienta orgánica.
- **Para los 20 emprendedores de la validación, es demasiado bajo** (`inferred`). Con contacto semanal se parecen más a los participantes de un ensayo (abandono del 26-48 %, Torous 2020; finalización del 64 % en el programa de IA, JAMA 2025) que a un usuario de tienda. Que solo 8 de 20 sigan activos en la semana 4 sería una mala señal. Por otro lado, el efecto de estar observado infla el resultado, así que 4 semanas no demuestran nada.
- **El plazo es corto** (`inferred` a partir de tres estudios verificados; corregido tras QA 2026-11-19). Los efectos de los avisos se apagan hacia la semana 4 (HeartSteps 2019). Solo el 8 % de las 54 intervenciones del megaestudio dejó un efecto medible después de sus 4 semanas (Milkman 2021). Y un hábito tarda una mediana de 59-66 días (Singh 2024). La validación debería medir las semanas 4, 8 y 12.

---

## Hallazgos por tema

### 1. Benchmarks de retención

- **La salud mental es la peor categoría** (`verified`, Baumel 2019). La retención a 30 días es del 3,3 % y la apertura diaria del 4 %. Los trackers retienen el doble que la media (6,1 %) y los ejercicios de respiración, nada (0 %). El uso tiene un pico por la tarde y la noche, salvo el mindfulness, que tiene dos picos (mañana y noche). Este patrón encaja con los dos rituales de Ucoach, el brief de mañana y el cierre del día.
- **Salud y forma física retiene un 3-4 % a los 30 días según AppsFlyer** (`verified`, Braze 2026) y un 7 % según Adjust (datos de 2022, `verified`; corregido tras QA 2026-11-19). La diferencia se debe a cómo mide cada fuente.
- **La retención digital empeoró en 2023**: la semana 1 cayó del 50 % al 28 % de media entre industrias (`verified`, Mixpanel 2024). Mixpanel amplió el alcance del informe de 2024, así que no se puede descartar que parte de la caída se deba a la nueva muestra (corregido tras QA 2026-11-19).
- **En ensayos, el abandono es del 26-48 %** (`verified`, Meyerowitz-Katz 2020: 40 % en ensayos; Torous 2020: 26,2 % bruto y 47,8 % corregido) (corregido tras QA 2026-11-19). Torous encontró menos abandono cuando había **feedback humano** y **registro del ánimo dentro de la app**, dos funciones que Ucoach ya tiene o puede imitar: el feedback lo da la IA y el check-in de ánimo ya existe.
- **Wearables:** un tercio abandona el dispositivo antes de 6 meses (`reported`, Endeavour 2014). Son datos antiguos. Oura publicó en su S-1/A (21-09-2026) una retención de miembros de pago a 12 meses de alrededor del 85 %, pero son suscriptores con hardware, no comparables con una herramienta gratuita. De WHOOP no hay cifras públicas (corregido tras QA 2026-11-19).

### 2. Fatiga de notificaciones y diseño de avisos

**Marco: JITAI (*just-in-time adaptive interventions*, Nahum-Shani et al., 2018,** `verified`**, https://pmc.ncbi.nlm.nih.gov/articles/PMC5364076/).** Una intervención adaptativa en el momento justo tiene cuatro componentes clave: puntos de decisión (cuándo se evalúa), opciones de intervención (mandar algo o no mandar nada), variables de ajuste (estado y contexto) y reglas de decisión. Con los resultados proximal (inmediato) y distal, el artículo habla de seis elementos (corregido tras QA 2026-11-19). Se interviene en momentos de *vulnerabilidad* u *oportunidad* y solo si la persona es *receptiva*. El cron cada 30 minutos de Ucoach es un **punto de decisión**, no un aviso. La pregunta correcta no es cada cuánto se revisa, sino cuántas veces la regla decide enviar algo.

**Evidencia de los micro-ensayos aleatorizados (MRT):**

| Estudio | Diseño | Resultado | Confianza |
|---|---|---|---|
| HeartSteps, Klasnja et al., Ann Behav Med 2019 | 44 adultos, 6 semanas, hasta 5 puntos de decisión al día a horas elegidas por el usuario; en cada uno se sorteaba si enviar sugerencia | Cualquier sugerencia: +14 % de pasos en 30 min de media (p=0,06). Al principio +66 % (167 pasos), **con un efecto que cae un 2 % cada día y deja de distinguirse de cero hacia el día 28**. Sugerencia de caminar: +107 % al inicio, con una caída del 3 % diario, indetectable hacia el día 29 (corregido tras QA 2026-11-19). **Sugerencias contra el sedentarismo: sin efecto detectable** | verified |
| HeartSteps, diseño | El usuario podía apagar la intervención hasta 12 horas desde la notificación (corregido tras QA 2026-11-19) | Control del usuario sobre la carga | verified (https://arxiv.org/html/1812.10800) |
| Bidargaddi et al., JMIR mHealth 2018 | 1.255 usuarios de una app de bienestar laboral, 89 días; 1 hora al día elegida al azar entre 6, y sorteo de enviar o no | Enviar el aviso aumenta un **3,9 %** la probabilidad de autorregistro en 24 h (RR 1,039, IC 95 % 1,01-1,08, P<0,05). El efecto se atenúa a lo largo del estudio, pero esa atenuación no es significativa (P=0,84) (corregido tras QA 2026-11-19). Mayor a mediodía en fin de semana (+11,8 %, exploratorio) | verified |
| HeartSteps II, De La Torre et al., 2024-2025 | MRT de un año, modelos individuales (n=10-11) | Cada mensaje recibido se asocia con más visitas a la app ese día | verified (resumen) |

**Carga de preguntar** (relevante para los check-ins):
- Eisele et al. (Assessment, 2022), con 163 estudiantes durante 14 días, encontró que pasar de **3 a 6 o 9 preguntas al día no** empeoró el cumplimiento ni la calidad. En cambio, **cuestionarios de 60 ítems frente a 30 sí** aumentaron la carga y empeoraron la calidad (`verified`).
- Wrzus y Neubauer (2023) revisaron 477 artículos y 677.536 participantes: los estudios hacen de media 6 preguntas al día durante 7 días, con un cumplimiento del 79 %, y el número de preguntas no predice el cumplimiento. Los incentivos económicos sí lo suben (`verified`). **Matiz:** son participantes de estudios, a menudo pagados, durante una o dos semanas. Un producto voluntario que dura meses no puede asumir esa tolerancia (`inferred`).

**Recordatorios frente a hábito:** Stawarz et al. (CHI, 2015) observaron que los recordatorios aumentan la repetición, pero pueden **frenar la automatización** porque el usuario se apoya en el aviso en lugar de en la señal del contexto. Las señales basadas en eventos ("después de X, hago Y") apoyaban mejor el hábito (`verified`, https://research-information.bris.ac.uk/en/publications/beyond-self-tracking-and-reminders-designing-smartphone-apps-that/; corregido tras QA 2026-11-19).

**Conclusiones para Ucoach:**
- **Revisar cada 30 minutos: sí. Enviar cada 30 minutos: no** (`inferred`). Las pruebas con efecto usan entre 1 y 5 puntos de decisión al día y en cada uno envían con una probabilidad de 0,5 (Bidargaddi) a 0,6 (HeartSteps). En HeartSteps eso da como mucho unas 3 sugerencias al día (corregido tras QA 2026-11-19). Ningún estudio revisado apoya más de 5 avisos al día.
- **Presupuesto recomendado:** 1 a 3 avisos proactivos al día, con un máximo de 4 y nunca dos en la misma hora. Además: horas de silencio, botón para silenciar 1 a 8 horas, y cada aviso con una sola acción concreta (`inferred` a partir de HeartSteps y Bidargaddi).
- **"Pausa activa cada hora" es el tipo de aviso con peor evidencia** (sin efecto en HeartSteps, `verified`). Hay que sustituirlo por un aviso de caminar ligado a un contexto (después de un bloque de reuniones, en el bajón de la tarde) y limitarlo a uno o dos al día.
- **Los avisos deben ser un andamio que se retira** (`inferred` a partir de Stawarz y Singh). A medida que sube la automaticidad del hábito, Ucoach manda menos.

### 3. Eficacia del coaching con IA y de los chatbots de salud

| Evidencia | Qué muestra | Límite | Confianza |
|---|---|---|---|
| Metaanálisis de Singh B. et al., npj Digital Medicine 2023 (19 ensayos, búsqueda hasta septiembre de 2022) | Chatbots: actividad total SMD 0,28; pasos 0,28; actividad moderada o vigorosa 0,53; fruta y verdura 0,59; **duración del sueño 0,44; calidad del sueño 0,50**. En el sueño funcionan mejor los programas con varios componentes que el chatbot solo | 74 % de ensayos de baja calidad; casi todos anteriores a los LLM | verified |
| Metaanálisis solo de ensayos aleatorizados de chatbots de ejercicio, Digital Health 2025 | Actividad física SMD 0,20 (IC 0,04-0,37) | Efecto pequeño y heterogéneo | verified (https://pubmed.ncbi.nlm.nih.gov/40656859/; corregido tras QA 2026-11-19) |
| Revisión de alcance, JMIR 2026 | Solo 14 de 43 estudios de chatbots de IA para cambio de conducta son ensayos aleatorizados; evidencia "exploratoria pero prometedora"; el sueño, poco estudiado | | verified (https://api.crossref.org/works/10.2196/79677; corregido tras QA 2026-11-19) |
| **Programa de prevención de diabetes con IA frente a humano**, Mathioudakis et al., JAMA 2025 (N=368, 12 meses) | Objetivo compuesto: 31,7 % con IA frente a 31,9 % con humano (no inferior). **Inicio: 93,4 % frente a 82,7 %. Finalización: 63,9 % frente a 50,3 %** | App con báscula y **aprendizaje por refuerzo para personalizar notificaciones, no un LLM**. Voluntarios motivados. (Se retira el dato de que el 46,5 % habría preferido un coach humano: no se encontró en las publicaciones del ensayo; corregido tras QA 2026-11-19) | verified |
| **Therabot**, Heinz et al., NEJM AI 2025 (N=210; 4 semanas de uso y seguimiento a las 8) | Síntomas frente a lista de espera: efecto grande en depresión (d≈0,85-0,90), ansiedad (d≈0,79-0,84) y riesgo de trastorno alimentario (d≈0,63-0,82). El comunicado de Dartmouth lo resume como −51 %, −31 % y −19 % (corregido tras QA 2026-11-19). Alianza terapéutica comparable a la de un terapeuta. Los usuarios iniciaban conversaciones a menudo, también de noche | Personal clínico supervisando. Los propios autores dicen que no está listo para funcionar de forma autónoma | verified (comunicado de Dartmouth) |
| **Bloom**, Jörke et al. (Stanford), arXiv 2025 (N=54, 4 semanas, LLM frente a control sin LLM) | Las dos ramas duplicaron la proporción de personas que cumplen las recomendaciones de actividad. **Sin ventaja del LLM en actividad.** El LLM sí mejoró la creencia en el beneficio, el disfrute y la autocompasión | Pequeño y corto | verified |
| Google PH-LLM, Nature Medicine 2025 | 79 % en examen de medicina del sueño (expertos: 76 %) y 88 % en forma física (expertos: 71 %); 857 casos | **Sin ensayo de resultados en el comportamiento de usuarios** | verified |
| WHOOP Coach, Oura Advisor, coach de Fitbit con Gemini | No se encontraron ensayos de resultados publicados | | inferred (búsqueda limitada) |

**Lectura para Ucoach** (`inferred`):
- La personalización automatizada **sostiene más el uso que un coach humano** (JAMA 2025), y un LLM **mejora la relación y la mentalidad** (Bloom, Therabot). Lo que aún no está demostrado es que un LLM cambie la conducta más que un buen sistema de reglas con avisos.
- La ventaja diferencial de Ucoach no debe ser "un LLM habla contigo". Debe ser el **contexto cruzado** (agenda, sueño y hábitos) combinado con un **motor de avisos que se ajusta con datos** y con la **conversación para los momentos difíciles**: volver tras fallar y replantear el plan.
- **Qué motor de avisos, y qué implica para la Ley de IA (corregido tras QA 2026-11-19).** Hay dos diseños posibles. (a) **Reglas fijas con aleatorización simple**: la regla la escribe una persona, la probabilidad de envío es constante y los tipos de aviso sin efecto los retira una persona al revisar los datos. No infiere nada por sí mismo, así que queda fuera de la definición de "sistema de IA" según las directrices de la Comisión, que exigen capacidad de inferir y excluyen los sistemas basados en reglas definidas solo por personas (https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-definition_en.pdf). Es el diseño recomendado para la validación. (b) **Bandit o aprendizaje por refuerzo** que decide solo cuándo y qué enviar, como el del programa de diabetes: probablemente es un sistema de IA. Si se adopta, Ucoach pasa a ser proveedor y debe cumplir la transparencia del art. 50 cuando el sistema interactúe con el usuario. No sería de alto riesgo mientras la finalidad declarada sea el bienestar (ver el informe 05, sección 3.3).
- Ucoach no es terapia. Con cerca de la mitad de los fundadores declarando alguna condición de salud mental a lo largo de la vida (49 % frente al 32 % de los controles, ver el punto 6; corregido tras QA 2026-11-19), el protocolo de derivación debe ser explícito.

### 4. Autoseguimiento: ¿mejora resultados o genera ansiedad?

- **Mejora la actividad física.** La revisión paraguas de Ferguson et al. (Lancet Digital Health, 2022), con 39 revisiones y 163.992 participantes, encontró en la actividad física un SMD de 0,3-0,6, unos **1.800 pasos más al día** y cerca de 1 kg menos. El beneficio "se mantiene en el tiempo". Los efectos sobre calidad de vida o dolor son pequeños (`verified`).
- **El autorregistro del ánimo dentro de la app** se asocia con menos abandono en los ensayos de depresión (`verified`, Torous 2020).
- **Ortosomnia** (Baron et al., JCSM, 2017): pacientes que buscan tratamiento por insomnio "detectado" por su wearable y entran en una "búsqueda perfeccionista del sueño ideal". Algunos alargan el tiempo en la cama para mejorar la puntuación, lo que empeora el insomnio. Los wearables de consumo distinguen mal las fases del sueño y los despertares. Es una **serie de casos, no una prevalencia** (`verified` el resumen; detalles `reported`).
- **Abandono de wearables:** se dejan por aburrimiento, por falta de utilidad práctica o porque los datos no llevan a ninguna acción (`reported`, Endeavour 2014). No se pudo revisar el modelo de *lapsing* de Epstein (2015) por falta de cupo de búsquedas.

**Implicaciones para cómo muestra los datos Ucoach** (`inferred`):
- El sueño se muestra **como media de 7 días y regularidad**, no como nota de cada noche. Nunca "has dormido mal" si el usuario dice sentirse bien: **lo que siente el usuario manda sobre el dispositivo**.
- No hay que inventar puntuaciones de sueño o de preparación propias. Basta con las horas y una pregunta subjetiva de 1 a 5.
- La tabla de deuda de sueño (menos de 6 h, de 6 a 7, 7 o más) está bien como regla interna, pero el texto al usuario debe ser de ajuste ("hoy, menos intensidad") y no de alarma.
- Hay que vigilar señales de bienestar que apunten a una relación ansiosa con el dato: muchas consultas sobre el sueño, preocupación declarada o más tiempo en la cama sin dormir más. En ese caso, Ucoach propone **menos seguimiento** (por ejemplo, una semana sin mirar el dato) y, si persiste, sugiere hablarlo con un profesional ("si te cuesta dormir de forma habitual, consulta a un profesional"). Ucoach no nombra trastornos, no diagnostica y no aplica terapia: la guía de bienestar de la FDA excluye las referencias a condiciones clínicas o umbrales diagnósticos (https://www.fda.gov/media/90652/download), y el informe 05 incluye "insomnio" en las palabras a evitar (corregido tras QA 2026-11-19).

### 5. Técnicas de cambio de conducta con mejor evidencia

| Técnica | Evidencia | Confianza | Uso en Ucoach |
|---|---|---|---|
| **Autorregistro combinado con otra técnica de autorregulación** (metas, feedback, revisión de metas) | En la metarregresión de Michie et al. (2009), las intervenciones de actividad y dieta que combinan autorregistro con al menos otra técnica de la teoría del control son más eficaces (0,42 frente a 0,26) | verified (https://pubmed.ncbi.nlm.nih.gov/19916637/; corregido tras QA 2026-11-19) | Check-in, revisión semanal y una sola meta: ya está en el diseño |
| **Intenciones de implementación** ("si X, entonces Y") | Gollwitzer y Sheeran 2006: d=0,65 en 94 pruebas. Sheeran, Listrom y Gollwitzer (Eur Rev Soc Psychol, en línea en 2024): 642 pruebas, d=0,27 en conducta y **d=0,15 tras corregir el sesgo con RoBMA** (0,35 con trim-and-fill) | verified (https://api.crossref.org/works/10.1080/10463283.2024.2334563; corregido tras QA 2026-11-19) | Que cada hábito tenga un "si-entonces" escrito por el usuario. Esperar un efecto modesto |
| **Apilar hábitos** (anclar a una rutina existente) | Judah et al. 2013 (N=50): usar el hilo dental *después* de cepillarse dio hábitos más fuertes a los 8 meses que hacerlo *antes*. Singh 2024: los hábitos **matutinos** y **elegidos por uno mismo** son más fuertes | verified | El hábito lo elige el usuario y se ancla a algo que ya hace, mejor por la mañana |
| **Tiempo de formación del hábito** | Mediana de 59-66 días, media de 106-154, rango de 4 a 335 (Singh et al. 2024); en uno de los estudios revisados (Keller et al., alimentación sana) solo el 23 % llegó al umbral (corregido tras QA 2026-11-19) | verified (https://pmc.ncbi.nlm.nih.gov/articles/PMC11641623/) | **Un hábito durante 8-10 semanas como mínimo**, no uno nuevo cada semana. Los "retos de 30 días" del modelo de negocio no bastan para formar un hábito |
| **Recompensa por volver** | Megaestudio de Milkman (Nature 2021; 61.293 personas, 54 intervenciones): el 45 % de las intervenciones subió las visitas al gimnasio entre un 9 y un 27 %; la **mejor premiaba volver tras faltar**; **solo el 8 % dejó un efecto después de las 4 semanas**; los expertos no supieron predecir cuáles funcionarían | verified | Celebrar la vuelta, no la perfección |
| **Rachas** | Destacar una racha intacta aumenta la conducta siguiente frente a una rota; el daño de la racha rota es mayor si uno se culpa y menor si puede repararla (Silverman y Barasch, JCR 2023, 7 estudios) | verified | Nada de "has roto tu racha". Usar ventanas flexibles ("5 de 7"), reparación y el lenguaje de "no fallar dos veces" |
| **Efecto de "empezar de cero"** | Las búsquedas, las visitas al gimnasio y los compromisos suben tras hitos temporales (lunes, inicio de mes, cumpleaños) (Dai, Milkman y Riis, 2014). No se transfiere de forma automática: un ensayo de recordatorios de medicación ligados a fechas de nuevo comienzo (Dai et al., JAMA Cardiol 2017, N=13.323) no mejoró la adherencia | verified (https://pubmed.ncbi.nlm.nih.gov/28196212/; corregido tras QA 2026-11-19) | Proponer el cambio de hábito en lunes o a principio de mes, y relanzar tras un parón |
| **Unir tentación y obligación** (*temptation bundling*) | Milkman et al. 2014: escuchar audiolibros solo en el gimnasio subió las visitas al principio, y el efecto decayó tras Acción de Gracias. Kirgios et al. 2020: enseñar la técnica añade un efecto modesto | verified (https://pubmed.ncbi.nlm.nih.gov/25843979/ y https://econpapers.repec.org/RePEc:eee:jobhdp:v:161:y:2020:i:s:p:20-35; corregido tras QA 2026-11-19) | Sugerencia opcional ("podcast solo al caminar"), no una pieza central |
| **Compromiso social** | No se revisaron estudios en esta sesión | n. d. | Fase 3 (equipos fundadores) |

### 6. Emprendedores: qué les duele y si pagan

| Dato | Cifra | Fuente | Año | Confianza |
|---|---|---|---|---|
| Fundadores con algún problema de salud mental a lo largo de la vida | ~49 % frente al 32 % de los controles; el 32 % tiene dos o más trastornos y el 18 %, tres o más. Muestra: 242 emprendedores y 93 controles, encuesta anónima autoinformada. El 49 % frente al 32 % procede del manuscrito de 2015 con la misma muestra | Freeman et al., Small Business Economics, https://ideas.repec.org/a/kap/sbusec/v53y2019i2d10.1007_s11187-018-0059-8.html | 2019 (piloto de 2015) | verified (corregido tras QA 2026-11-19) |
| Cifra popular del "72 %" | Es preliminar y no mide "tener problemas de salud mental": suma un 49 % con antecedentes personales y un 23 % sin síntomas pero con antecedentes familiares. En controles, la cifra equivalente es del 48 %. Los propios autores lo califican de "highly preliminary" (autoinforme, posible sesgo de selección, diseño transversal). Mal citada con frecuencia (corregido tras QA 2026-11-19) | Freeman et al. 2015, https://www.michaelafreemanmd.com/documents/are-entrepreneurs-touched-with-fire-pre-pub-n-4-17-15.pdf | 2015 | verified |
| Burnout en el último año (corregido tras QA 2026-11-19) | Encuesta de 2024 (n=156): 53 % burnout; 75 % ansiedad; 45 % salud mental mala o muy mala; 61 % ha pensado en dejar su empresa y 49 % lo considera para el año siguiente. La de 2025 (54 %, n≈138) solo aparece en agregadores, con muestras contradictorias: no verificada | Sifted, vía https://thefinanser.com/2024/03/half-of-start-up-founders-are-ready-to-quit | 2024 | reported (fuente secundaria; Sifted bloquea el acceso) |
| Impacto en la salud mental | 72 %; ansiedad 37 %; burnout 36 % | Startup Snapshot "The Untold Toll" | 2023 | reported |
| Efecto del estrés del fundador en el equipo | Los equipos con fundadores muy estresados tienen un 16 % menos de bienestar laboral, un 14 % más de burnout y un 16 % menos de seguridad psicológica. Solo el 10 % de los fundadores comparte sus dificultades con el equipo | Startup Snapshot, parte 2 (vía Brad Feld) | 2025 | verified (vía el blog de Brad Feld; corregido tras QA 2026-11-19) |
| Sueño | 41 % duerme 5-6 horas o menos y 71 % sufre burnout al menos varias veces al año (encuesta india, n=50, no representativa) (corregido tras QA 2026-11-19) | Bertelsmann India Investments, vía https://www.indianpharmapost.com/healthcare/bii-spotlights-founder-wellness-in-startup-ecosystem-at-its-8th-badminton-championship-21056 | 2026 | reported |
| **Pago por coaching** | **58 % de los CEO ha recibido coaching pagado**; el 69 % de ellos, muy satisfecho. Temas: desarrollo personal, liderazgo y organización | Stanford y Miles Group (n=90) | 2025 | verified |
| Coaching en startups con capital riesgo | 39 % de los CEO usó coach en el último año: 32 % en fase semilla y 60 % en crecimiento (n=56) | Fast Company | Fecha sin confirmar (~2016) | reported |

**Lectura** (`inferred`): lo que duele es el estrés sostenido, la soledad ("solo el 10 % lo comparte"), el burnout y el sueño sacrificado. Lo que pagan es coaching de **rendimiento y liderazgo**, y más cuanto más crece la empresa. Esto respalda el posicionamiento de Philippe: **vender eficiencia y excelencia profesional, y meter dentro la energía y el sueño**. El mensaje "cuida tu salud" vende poco a este público; "decide mejor en la negociación de mañana" vende más. El coste de un coach humano (cientos o miles de euros al mes, `reported`) deja mucho margen para un Pro de 8-15 €.

### 7. Fricción de registro

- **La longitud cuenta más que la frecuencia** (`verified`, Eisele 2022). Tres ítems de 1 a 5 (energía, ánimo, foco) están dentro de lo tolerable. Añadir más preguntas por check-in es lo que hay que evitar.
- **El registro manual decae.** En un programa web de 6 meses, los participantes registraron de media el 28 % de los días laborables y el 17 % de los fines de semana, con la mayoría de registros al principio (Krukowski et al. 2013, https://pubmed.ncbi.nlm.nih.gov/22545978/); con MyFitnessPal, el registro baja de 5,4 a 1,4 días por semana entre las semanas 4 y 12 (https://doi.org/10.2196/64139) (`verified`; corregido tras QA 2026-11-19). Pedir "5 noches registradas a mano" es pedir esfuerzo diario indefinido.
- **El registro pasivo elimina la fricción, pero no la desconfianza.** La importación de Apple Health convierte el sueño en dato pasivo, aunque con las limitaciones de precisión del punto 4.
- **El registro conversacional no tiene, a noviembre de 2026, ventaja demostrada.** No se encontró ningún ensayo que compare registrar en un chat con hacerlo en un formulario. (Se retira la cita de Slip Buddy: no es un chatbot, sino una app para registrar deslices dietéticos; Pagoto et al., JMIR mHealth 2021, https://pubmed.ncbi.nlm.nih.gov/33792547/; corregido tras QA 2026-11-19.) La ventaja de Ucoach es estructural: **el registro va dentro de un ritual que ya ocurre**, el brief o el cierre, sin abrir otra app. El usuario puede escribir "dormí fatal, unas 5 h" en lenguaje natural y la IA lo convierte en datos (`inferred`). Esto debe medirse, no suponerse.

### 8. Patrones de producto que retienen

- **Revisión semanal:** encaja con el autorregistro más la revisión de metas (Michie 2009, `verified`) y con el "empezar de cero" de cada lunes (Dai 2014, `verified`; corregido tras QA 2026-11-19). Debe ser corta, con un solo foco y **el mismo hábito durante semanas** (Singh 2024).
- **Informes personalizados** ("tu energía es 0,8 puntos mayor tras dormir 7 h"): son potentes porque usan los datos del propio usuario, pero **con 7 días de datos casi cualquier diferencia es ruido** (`inferred`). Conviene mostrarlos solo con un mínimo de datos (por ejemplo, 14 días o más y 5 o más días en cada grupo), con lenguaje de incertidumbre ("parece que", "de momento") y sin presentar la correlación como causa.
- **Experimentos n-de-1:** SleepCoacher (Daskalova et al., UIST 2016) mostró que los usuarios pueden hacer autoexperimentos guiados de sueño, y que el sueño mejora con la adherencia; Self-E (CHI 2021) extendió la idea a autoexperimentos personalizables, no solo de sueño (`verified`, https://jeffhuang.com/papers/SleepCoacher_UIST16.pdf; corregido tras QA 2026-11-19). Para Ucoach: "2 semanas alternando el último café a las 14:00 y a las 16:00, y mira tu energía de la mañana". Esto convierte el principio "datos propios antes que promedios" en método, no solo en gráfica.
- **Reflexión guiada:** el LLM aporta sobre todo cambio de mentalidad, autocompasión y alianza (Bloom 2025, Therabot 2025, `verified`). Las preguntas de los libros (GROW, "¿qué dependía de mí hoy?") son el uso natural de la IA en el cierre.
- **Feedback humano:** reduce el abandono en ensayos (Torous 2020, `verified`). En la validación, las entrevistas semanales hacen ese papel, y conviene no confundir su efecto con el del producto.

---

## El hallazgo no obvio

**El momento que decide la retención de Ucoach no es el primer día, sino el día después de fallar. Y el mejor aviso es el que deja de hacer falta.**

Las piezas de evidencia apuntan en la misma dirección:
- La intervención ganadora entre 54 del megaestudio de Nature (2021) **no premiaba ir al gimnasio, sino volver tras faltar**.
- Destacar una racha rota reduce la conducta siguiente, sobre todo si el usuario se culpa, y el efecto se suaviza si puede reparar la racha (JCR 2023).
- El efecto de los avisos se apaga en semanas (HeartSteps 2019). Los recordatorios pueden sustituir a la señal del contexto e impedir que el hábito se automatice (Stawarz 2015). Y el hábito tarda una mediana de dos meses (Singh 2024).
- Donde un LLM supera a un sistema de reglas no es en la cantidad de conducta, sino en **mentalidad, autocompasión y alianza** (Bloom 2025, Therabot 2025).

**Consecuencia** (`inferred`): las apps de hábitos optimizan las rachas y el número de avisos, y por eso pierden a la gente en la primera recaída. Ucoach tiene justo la pieza que les falta: una conversación sin culpa que replantea el plan, de modo que **la recaída se convierte en el ritual central** ("llevas 4 días sin cierre; ¿qué ha pasado y cuál es la versión de 2 minutos para hoy?"). Además, su motor de avisos debe **retirarse** a medida que el hábito se automatiza. La métrica que lo captura no es "activos semanales", sino la **tasa de vuelta**: el porcentaje de usuarios que, tras 3 días o más sin actividad, vuelven en los 7 días siguientes.

---

## Recomendaciones para el diseño de Ucoach (priorizadas)

### Prioridad 1: avisos (antes de reclutar a los 20)

1. **Separar la evaluación del envío.** El cron revisa cada 30 minutos, pero con un **presupuesto de envío**: 1 a 3 avisos al día por defecto, como máximo 4, nunca dos en 60 minutos, y horas de silencio que empiecen en la desconexión nocturna. Hay que añadir `ucoach snooze 1h|2h|4h|8h` y un "hoy no" por Telegram. El texto de los avisos que pasan por Telegram no lleva datos de salud (ni horas de sueño ni ánimo), porque pasa por los servidores de Telegram (ver el informe 05) (corregido tras QA 2026-11-19).
2. **Quitar "pausa activa cada hora"** como aviso por defecto. Sustituirlo por **una o dos sugerencias de caminar ligadas a un contexto**: después de 2 horas o más de reuniones seguidas (Ucoach ya lo detecta), en el bajón de la tarde o si a las 17:00 no se ha movido.
3. **Micro-aleatorización integrada.** En cada decisión de enviar, sortear (por ejemplo, 70/30) si el aviso se manda o no, y guardar la respuesta inmediata: si se hizo la acción, si se abrió el brief, si se registró algo. Con 20 usuarios y 8 semanas habrá miles de decisiones, suficientes para detectar efectos grandes y descartar *tipos* de aviso claramente inútiles, no para medir efectos pequeños: HeartSteps, con 44 inscritos, no alcanzó significación para el efecto global (p=0,06) (`inferred`; es el diseño de HeartSteps y Bidargaddi). Los tipos sin efecto los retira una persona al revisar los datos: la regla y la probabilidad de envío son fijas, para no convertir el motor en un sistema de IA (ver "Lectura para Ucoach" en el punto 3). **Antes de empezar**, cada participante firma un consentimiento explícito (art. 9.2.a RGPD) con hoja informativa: qué se registra, para qué, quién lo ve y cuándo se borra. Se recoge solo lo mínimo para estas métricas, seudonimizado, y se lleva un registro de actividades (ver la P0 del informe 05) (corregido tras QA 2026-11-19).
4. **Avisos que se retiran.** Cada hábito tiene una fase de andamio (aviso diario ligado a su ancla) y una de retirada: cuando la automaticidad pasa de un umbral o tras 3 semanas cumplidas, el aviso pasa a días alternos y después desaparece.

### Prioridad 2: rituales y hábitos

5. **La revisión semanal no cambia de hábito cada semana.** Debe evaluar el **mismo hábito focal** hasta que se automatice (8-10 semanas como referencia) y proponer solo un ajuste: hacerlo más pequeño, mover el ancla o cambiar la hora. Solo con el hábito automatizado propone uno nuevo, a ser posible en lunes o a principio de mes.
6. **Cada hábito nace con tres campos:** elegido por el usuario, un ancla ("después de...") y su versión de 2 minutos. Mejor por la mañana cuando sea posible (Singh 2024; Judah 2013).
7. **Sin rachas punitivas.** Mostrar "5 de 7" o "12 de los últimos 14 días", nunca un contador a cero. Permitir reparar la racha. Prohibir en los textos el "has roto tu racha".
8. **Un ritual de vuelta:** un prompt `retomar` que se activa tras 3 días o más sin actividad. Pregunta qué ha pasado sin culpa, propone la versión mínima del hábito, celebra explícitamente la vuelta (Milkman 2021) y, si hay un hito cerca, lo usa ("el lunes empezamos limpio").
9. **El brief de mañana no debe exigir un ritual diario.** Si el usuario se lo salta, el cierre del día puede hacer de brief del día siguiente. Hay que medir los rituales completados, no los briefs a secas.

### Prioridad 3: registro y presentación de datos

10. **Por defecto, sueño pasivo** (importación automática de Apple Health o CSV). Si no hay wearable, una sola pregunta conversacional en el brief: "¿Cuánto has dormido y cómo te sientes (1-5)?".
11. **Check-in de 3 ítems como máximo**, integrado en el cierre, sin pedirlo aparte. Un check-in extra a mediodía solo si el usuario lo activa.
12. **El sueño, como tendencia semanal y regularidad.** El dato subjetivo prevalece. Si aparecen señales de una relación ansiosa con el dato, proponer una semana sin mirar los datos, sin hablar de trastornos (corregido tras QA 2026-11-19).
13. **Informes personalizados con umbral y honestidad:** como mínimo 14 días y 5 días en cada grupo, lenguaje de incertidumbre y nunca causalidad.

### Prioridad 4: experimentos n-de-1

14. **Herramienta `experimento`:** el usuario elige una variable (hora del último café, luz matinal, siesta, bloque de foco de 60 o 90 minutos) y Ucoach propone alternarla durante 2 a 4 semanas con un orden aleatorio por días. Mide energía y foco en el check-in y lo resume en la revisión semanal con su incertidumbre. Es la forma más creíble de cumplir "datos propios antes que promedios" y además retiene, porque crea curiosidad por el resultado (`inferred`). En la versión local los datos se quedan en el equipo del usuario; si en la validación se comparten resultados de experimentos con el equipo de Ucoach, rige el mismo consentimiento explícito y la misma minimización que en la recomendación 3 (corregido tras QA 2026-11-19).

### Prioridad 5: métricas de validación revisadas

| Métrica v0.1 | Problema | Métrica propuesta | Objetivo (cohorte de 20, `inferred`) |
|---|---|---|---|
| Activos semanales / instalaciones >40 % a 4 semanas | Bajo para una cohorte guiada, plazo corto y "activo" sin definir | **Semana activa = 3 rituales o más completados** (brief, cierre o revisión). Medir las semanas 4, 8 y 12 | ≥60 % en la semana 4, ≥45 % en la 8 y ≥35 % en la 12 |
| n. a. | No mide la recaída | **Tasa de vuelta:** % que vuelve en 7 días tras 3 días o más inactivo | ≥50 % |
| 4 briefs o más por semana | Penaliza a quien usa el cierre como planificación | Mediana de rituales por usuario activo y semana | ≥4 |
| 5 noches registradas o más por semana | Mide la fricción, no el valor | **Noches con dato** (pasivo o conversacional) | ≥5 en usuarios con wearable y ≥4 sin él |
| Cumplimiento de hábitos frente a la semana 1 | Regresión a la media; el hábito cambia | **Automaticidad del hábito focal** (SRBAI, 4 ítems de acuerdo de 1 a 7; Gardner et al. 2012, https://pubmed.ncbi.nlm.nih.gov/22935297/) en las semanas 1, 4 y 8 | Subida de 1 punto o más en la escala de 7 en la semana 8 |
| Energía frente a la semana 1 | Regresión a la media y efecto de la observación | Diferencia de energía dentro de cada persona en condiciones de experimento n-de-1 | Descriptivo, sin umbral |
| NPS >40 | Con n=20, el margen de error al 95 % es de unos ±30-40 puntos (https://www.tlfresearch.com/news-opinion/what-is-your-nps-margin-of-error/) | Pregunta de Sean Ellis: "¿cómo te sentirías si no pudieras usar Ucoach?" | ≥40 % "muy decepcionado", el umbral de Ellis (https://learningloop.io/plays/product-market-fit-survey) + entrevistas (corregido tras QA 2026-11-19) |
| n. a. | Fatiga de avisos | % de avisos silenciados, desactivaciones del cron y efecto de cada tipo de aviso (micro-aleatorización) | Silenciados <20 %; cron activo ≥70 % en la semana 8 |
| n. a. | Separar el producto del contacto humano | Cohorte B de 10-20 usuarios orgánicos sin entrevistas semanales | Activos en la semana 4 ≥20 % |
| n. a. | Datos de salud de terceros en la validación (corregido tras QA 2026-11-19) | Consentimientos explícitos firmados antes de la primera medición; datos recogidos solo los de esta tabla | 100 % de participantes con consentimiento; borrado al cerrar la validación |

### Prioridad 6: mensaje y seguridad

15. **Vender rendimiento, entregar salud:** "Llega a la negociación de mañana con energía" mejor que "duerme mejor". Encaja con el posicionamiento de Philippe y con lo que pagan los CEO (Stanford 2025). Sin prometer resultados de salud ni "potenciar el rendimiento físico o psíquico" como efecto garantizado: el RD 1907/1996 lo restringe en la publicidad con pretendida finalidad sanitaria (ver el informe 05) (corregido tras QA 2026-11-19).
16. **Derivación explícita** ante señales de bienestar persistentes, por ejemplo un ánimo de 2 o menos durante 7 días o más, cansancio sostenido o dificultad habitual para dormir, con un texto que no nombra trastornos ni diagnostica: "si llevas una semana con el ánimo bajo o te cuesta dormir de forma habitual, puede ser útil hablarlo con un profesional", más los recursos definidos. El umbral es interno y sirve para disparar la sugerencia, no se muestra como medida clínica. Que cerca de la mitad de los fundadores declare alguna condición de salud mental (Freeman 2019) hace este protocolo imprescindible (corregido tras QA 2026-11-19).

---

## Huecos y límites de esta investigación

- No hay cifras públicas de retención de WHOOP ni del coach de Fitbit, ni ensayos de resultados de los coaches con IA de WHOOP, Oura o Fitbit. De Oura sí hay retención de miembros de pago en su S-1/A de 2026 (corregido tras QA 2026-11-19).
- No hay benchmarks fiables de retención para herramientas de productividad B2B por categoría, ni para herramientas que viven dentro de un asistente de IA (servidores MCP o CLI), que serían el comparador más cercano a Ucoach (añadido tras QA 2026-11-19).
- No se pudo acceder al original de Sifted: sus cifras son `reported` y la encuesta de 2025 queda sin verificar. Freeman 2019 se verificó con el resumen y el manuscrito de 2015 (corregido tras QA 2026-11-19).
- Verificados en el QA del 2026-11-19 con fuente primaria: Sheeran et al. 2024, Stawarz 2015, Dai 2014, Kirgios 2020, Michie 2009 y Daskalova 2016. Siguen sin verificar el dato de AppsFlyer de 2023 (Business of Apps bloquea el acceso), el artículo de Fast Company y las razones de abandono de Endeavour.
- La app de consumo de Woebot cerró el 30-06-2025 (https://hlth.com/insights/news/woebot-health-is-shutting-down-its-app-2025-04-28); el motivo no está verificado. No se usa como argumento (corregido tras QA 2026-11-19).
- Faltaron búsquedas sobre la receptividad según el contexto (Mehrotra 2016, Künzler 2019) porque se agotó el cupo.

---

## Índice de fuentes

**Retención y abandono**
1. Baumel A, Muench F, Edan S, Kane JM. *Objective User Engagement With Mental Health Apps*. JMIR 2019;21(9):e14567. https://www.jmir.org/2019/9/e14567/ (verified, resumen en Europe PMC)
2. Braze. *Mobile app retention* (tabla D30 con datos de AppsFlyer vía Business of Apps, 2026). https://www.braze.com/resources/articles/mobile-app-retention (verified)
3. Business of Apps. *Health & Fitness App Benchmarks* (AppsFlyer 2023; Adjust). https://www.businessofapps.com/data/health-fitness-app-benchmarks/ (reported; error 403)
4. Mixpanel. *2024 Benchmarks Report*. https://mixpanel.com/blog/2024-mixpanel-benchmarks-report (verified)
5. Meyerowitz-Katz G et al. *Rates of Attrition and Dropout in App-Based Interventions for Chronic Disease*. JMIR 2020;22(9):e20283. doi:10.2196/20283 (verified)
6. Torous J, Lipschitz J, Ng M, Firth J. *Dropout rates in clinical trials of smartphone apps for depressive symptoms*. J Affect Disord 2020;263:413-419. doi:10.1016/j.jad.2019.11.167 (verified)
7. Endeavour Partners. Estudio de consumo de wearables (nota del 15-08-2014). https://rss.globenewswire.com/news-release/2014/08/15/1060135/0/en/Endeavour-Partners-Consumer-Behavior-Study-Points-to-Uncertain-Future-of-Wearable-Devices.html (verified; corregido tras QA 2026-11-19: la URL anterior daba 403)
8. Sensor Tower. *State of Mobile Health and Fitness in 2025*. https://sensortower.com/blog/state-of-mobile-health-and-fitness-in-2025 (reported; sin datos de retención)

**Avisos y JITAI**

9. Klasnja P et al. *Efficacy of Contextually Tailored Suggestions for Physical Activity: A Micro-randomized Optimization Trial of HeartSteps*. Ann Behav Med 2019;53(6):573-582. doi:10.1093/abm/kay067 (verified)
10. Bidargaddi N et al. *To Prompt or Not to Prompt? A Microrandomized Trial of Time-Varying Push Notifications*. JMIR mHealth uHealth 2018;6(11):e10123. doi:10.2196/10123 (verified)
11. Spruijt-Metz D et al. *HeartSteps II Protocol*. IJERPH 2022. doi:10.3390/ijerph19042267; De La Torre SA et al., J Biomed Inform 2024, doi:10.1016/j.jbi.2024.104721 (verified)
12. Nahum-Shani I et al. *Just-in-Time Adaptive Interventions (JITAIs) in Mobile Health*. Ann Behav Med 2018;52(6):446-462. https://pmc.ncbi.nlm.nih.gov/articles/PMC5364076/ (verified tras QA 2026-11-19)
13. Eisele G et al. *The Effects of Sampling Frequency and Questionnaire Length on Perceived Burden, Compliance, and Careless Responding*. Assessment 2022. doi:10.1177/1073191120957102 (verified)
14. Wrzus C, Neubauer AB. *Ecological Momentary Assessment: A Meta-Analysis on Designs, Samples, and Compliance*. Assessment 2023. doi:10.1177/10731911211067538 (verified)
15. Stawarz K, Cox AL, Blandford A. *Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation*. CHI 2015, pp. 2653-2662. https://research-information.bris.ac.uk/en/publications/beyond-self-tracking-and-reminders-designing-smartphone-apps-that/ (verified tras QA 2026-11-19)

**Coaching con IA y chatbots**

16. Singh B et al. *Systematic review and meta-analysis of the effectiveness of chatbots on lifestyle behaviours*. npj Digit Med 2023;6:118. doi:10.1038/s41746-023-00856-1 (verified)
17. Mathioudakis N et al. Ensayo de prevención de diabetes con IA frente a humano. JAMA, 27 de octubre de 2025. https://jamanetwork.com/journals/jama/fullarticle/2840703 ; texto completo https://pmc.ncbi.nlm.nih.gov/articles/PMC12560030/ (verified). El dato de preferencia por el coach humano se retiró tras el QA de 2026-11-19 por no encontrarse
18. Heinz MV et al. *Randomized Trial of a Generative AI Chatbot for Mental Health Treatment*. NEJM AI 2025. doi:10.1056/AIoa2400802. Comunicado de Dartmouth: https://tto.dartmouth.edu/news/2025/03/first-therapy-chatbot-trial-yields-mental-health-benefits ; resumen https://pubmed.ncbi.nlm.nih.gov/42932588/ (verified; los porcentajes de mejora salen del comunicado, el artículo da tamaños de efecto)
19. Jörke M et al. *Bloom: Designing for LLM-Augmented Behavior Change Interactions*. arXiv:2510.05449, 2025. https://arxiv.org/abs/2510.05449 (verified)
20. Google Research. *A personal health large language model for sleep and fitness coaching*. Nature Medicine 2025. https://research.google/pubs/a-personal-health-large-language-model-for-sleep-and-fitness-coaching/ (verified)
21. Metaanálisis de ensayos de chatbots de ejercicio, Digital Health 2025, y revisión de alcance JMIR 2026 (e79677). https://www.jmir.org/2026/1/e79677 ; Wang et al., Digital Health 2025, https://pubmed.ncbi.nlm.nih.gov/40656859/ (verified tras QA 2026-11-19)

**Autoseguimiento**

22. Ferguson T et al. *Effectiveness of wearable activity trackers to increase physical activity and improve health: umbrella review*. Lancet Digit Health 2022;4:e615-26. doi:10.1016/S2589-7500(22)00111-X (verified)
23. Baron KG et al. *Orthosomnia: Are Some Patients Taking the Quantified Self Too Far?* J Clin Sleep Med 2017;13(2):351-354. doi:10.5664/jcsm.6472 (verified)
24. Sleep Foundation. *Orthosomnia*. https://www.sleepfoundation.org/sleep-tracking/orthosomnia (reported)

**Técnicas de cambio de conducta**

25. Milkman KL et al. *Megastudies improve the impact of applied behavioural science*. Nature 2021;600:478-483. doi:10.1038/s41586-021-04128-4 (verified)
26. Silverman J, Barasch A. *On or Off Track: How (Broken) Streaks Affect Consumer Decisions*. J Consumer Research 2023;49(6):1095-1117. https://www.colorado.edu/business/faculty-research/2023/04/19/or-track-how-broken-streaks-affect-consumer-decisions (verified)
27. Singh B, Murphy A, Maher C, Smith AE. *Time to Form a Habit*. Healthcare 2024;12(23):2488. doi:10.3390/healthcare12232488 (verified)
28. Judah G, Gardner B, Aunger R. *Forming a flossing habit*. Br J Health Psychol 2013. doi:10.1111/j.2044-8287.2012.02086.x (verified)
29. Gollwitzer PM, Sheeran P. *Implementation intentions and goal achievement: a meta-analysis*. Adv Exp Soc Psychol 2006;38:69-119. doi:10.1016/S0065-2601(06)38002-1 (verified tras QA 2026-11-19)
30. Sheeran P, Listrom O, Gollwitzer PM. *The when and how of planning: meta-analysis of implementation intentions (642 tests)*. Eur Rev Soc Psychol 36(1):162-194, en línea el 27-03-2024. https://api.crossref.org/works/10.1080/10463283.2024.2334563 (verified tras QA 2026-11-19)
31. Dai H, Milkman KL, Riis J. *The Fresh Start Effect*. Management Science 2014;60(10):2563-2582. https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf ; ensayo de recordatorios de medicación, Dai et al., JAMA Cardiol 2017, https://pubmed.ncbi.nlm.nih.gov/28196212/ (verified tras QA 2026-11-19)
32. Milkman KL, Minson JA, Volpp KG. *Holding the Hunger Games Hostage at the Gym*. Management Science 2014, https://pubmed.ncbi.nlm.nih.gov/25843979/ ; Kirgios EL et al., OBHDP 2020;161:20-35, https://econpapers.repec.org/RePEc:eee:jobhdp:v:161:y:2020:i:s:p:20-35 (verified tras QA 2026-11-19)
33. Michie S et al. *Effective techniques in healthy eating and physical activity interventions: a meta-regression*. Health Psychol 2009;28(6):690-701. https://pubmed.ncbi.nlm.nih.gov/19916637/ (verified tras QA 2026-11-19)

**Emprendedores**

34. Freeman MA et al. *The prevalence and co-occurrence of psychiatric conditions among entrepreneurs and their families*. Small Bus Econ 2019;53(2):323-342. https://ideas.repec.org/a/kap/sbusec/v53y2019i2d10.1007_s11187-018-0059-8.html ; manuscrito de 2015 (origen del 72 %): https://www.michaelafreemanmd.com/documents/are-entrepreneurs-touched-with-fire-pre-pub-n-4-17-15.pdf (verified tras QA 2026-11-19)
35. Sifted. *Founder mental health* (encuestas de 2024 y 2025). https://sifted.eu/articles/founder-mental-health (reported; error 403)
36. Startup Snapshot vía Brad Feld, *The toll of stress on startup teams*, 10 de diciembre de 2025. https://feld.com/archives/2025/12/the-toll-of-stress-on-startup-teams-and-its-link-to-founder-well-being/ (verified)
37. Stanford CGRI y Miles Group. *2025 CEO Coaching and Kitchen Cabinet Survey*. https://www.hoover.org/news/ceos-increasingly-using-informal-networks-advisors-professional-coaches-stanford-survey (verified)
38. Fast Company. *Dismantling the myth of the self-reliant CEO*. https://www.fastcompany.com/3060235/dismantling-the-myth-of-the-self-reliant-ceo (reported)
39. Encuesta de bienestar de fundadores de Bertelsmann India Investments, julio de 2026, vía YourStory (reported; error 403)

**Registro**

40. Krukowski RA et al. Patrones de autorregistro dietético en un programa web. Health Psychol 2013;32:164-70, https://pubmed.ncbi.nlm.nih.gov/22545978/ ; revisión JMIR mHealth 2026 (e64139), https://doi.org/10.2196/64139 ; SnappyMeal (arXiv:2511.03907) (reported). Pagoto et al., Slip Buddy, JMIR mHealth 2021, https://pubmed.ncbi.nlm.nih.gov/33792547/ (no es un chatbot; se retiró como evidencia). (Corregido tras QA 2026-11-19.)

**Añadidas tras el QA del 2026-11-19**

41. Adjust, benchmarks de retención 2023 y 2024: https://www.adjust.com/blog/get-the-mobile-app-retention-benchmarks-for-2023/ ; https://www.adjust.com/blog/what-makes-a-good-retention-rate/
42. Mixpanel, semana 8 (informes de 2017 y 2019): https://mixpanel.com/blog/whats-a-good-retention-rate/ ; benchmarks B2B 2026: https://mixpanel.com/blog/b2b-benchmarks-2026/
43. Oura, S-1/A ante la SEC (21-09-2026): https://www.sec.gov/Archives/edgar/data/2133022/000119312526396051/d119865ds1a.htm
44. HeartSteps, texto completo y diseño: https://pmc.ncbi.nlm.nih.gov/articles/PMC6401341/ ; https://arxiv.org/html/1812.10800
45. Gardner B et al., SRBAI, Int J Behav Nutr Phys Act 2012;9:102: https://pubmed.ncbi.nlm.nih.gov/22935297/
46. Margen de error del NPS: https://www.tlfresearch.com/news-opinion/what-is-your-nps-margin-of-error/ ; prueba de Sean Ellis: https://learningloop.io/plays/product-market-fit-survey
47. Singh 2024, texto completo: https://pmc.ncbi.nlm.nih.gov/articles/PMC11641623/
48. Sifted 2024 vía The Finanser: https://thefinanser.com/2024/03/half-of-start-up-founders-are-ready-to-quit
49. Bertelsmann India, encuesta de julio de 2026: https://www.indianpharmapost.com/healthcare/bii-spotlights-founder-wellness-in-startup-ecosystem-at-its-8th-badminton-championship-21056
50. Daskalova N et al., SleepCoacher, UIST 2016: https://jeffhuang.com/papers/SleepCoacher_UIST16.pdf
51. Cierre de Woebot: https://hlth.com/insights/news/woebot-health-is-shutting-down-its-app-2025-04-28
52. Comisión Europea, directrices sobre la definición de sistema de IA: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-definition_en.pdf ; FDA, General Wellness (2026): https://www.fda.gov/media/90652/download
