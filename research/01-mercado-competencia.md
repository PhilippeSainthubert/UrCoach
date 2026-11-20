# Ucoach · Línea 1 · Mercado y competencia

**Fecha:** 2026-11-19 · **Base:** documento de producto v0.1 (Google Doc `1S6MFA-6j9KQh4pYVxCYngqUF8hHvjSIaFO7EjO2owyw`) y alcance aclarado en `00-scope.md` (coach centrado en eficiencia y excelencia profesional, con energía y sueño óptimos).

**Método:** unas 65 búsquedas y lecturas de página (inglés y español), más una consulta a la API de GitHub el 2026-11-19 para estrellas y actividad de los repositorios MCP. Más de 60 fuentes distintas. Algunas webs oficiales bloquean la lectura automática (WHOOP, OpenAI, Business Wire devolvieron 403); en esos casos el dato se apoya en prensa y va marcado como `reported`.

**Etiquetas:** `verified` = leído en la fuente oficial (web de producto, precios, nota de prensa, ayuda oficial, API de GitHub). `reported` = fuente secundaria (prensa, blogs, agregadores). `inferred` = deducción propia a partir de lo anterior.

**Límite de esta investigación:** se agotó el cupo de búsquedas web de la sesión antes de cubrir Stoic, Reflectly, Ahead, Bunch, Tenor, Bevel y el detalle de Ultrahuman. Quedan como pendientes en el apartado 8.

---

## 1. Resumen

1. **El hueco que describe el documento v0.1 ya no existe tal cual.** El doc dice que «ninguna [pieza] cruza la agenda real con el sueño, la energía y los hábitos». Es falso en 2026: Lifestack planifica las tareas en Google Calendar u Outlook según la energía que estima con Oura, WHOOP, Garmin, Fitbit o Apple Health (`verified`, App Store), por unos 7 $ al mes o 50 $ al año (`reported`, blog.saner.ai) (corregido tras QA 2026-11-19). Rise Science añade como eventos de Google Calendar o Apple Calendar su previsión de energía basada en el sueño (`verified`, App Store y ayuda de Rise) (corregido tras QA 2026-11-19). En el directorio de conectores de Claude, athletedata lee más de 30 fuentes de wearables y escribe entrenamientos en Google Calendar (`verified`, sept. 2026) (corregido tras QA 2026-11-19).
2. **Las plataformas de IA ya tienen todas las piezas de Ucoach menos el método.** Claude (enero de 2026) y ChatGPT (enero de 2026, despliegue ampliado en julio) leen Apple Health. Las dos tienen calendario, memoria y tareas programadas, y desde el otoño de 2026 tienen agentes proactivos en la nube: ChatGPT dots (29-09-2026; en Pro excluye el EEE, Suiza y el Reino Unido) y Claude Duet (21-10-2026; solo EE. UU.) (corregido tras QA 2026-11-19). Lo que no tienen es un método de coaching con reglas, niveles de evidencia y seguimiento longitudinal.
3. **En Europa faltan las plataformas generalistas, no los coaches de salud (corregido tras QA 2026-11-19).** ChatGPT Health excluye el EEE, Suiza y el Reino Unido (`reported`, notebookcheck.net). Las integraciones de salud de Claude están en beta solo en EE. UU. (`verified`, anthropic.com). Gemini Personal Intelligence tampoco ha llegado a Europa (`reported`, 9to5Google). Pero en España sí funcionan Google Health Coach, incluido en Google AI Pro y que exige Fitbit o Pixel Watch (`verified`, ayuda de Google Health), y Oura Advisor, también en español (`reported`, ayuda de Oura). Ninguno de los dos mira la agenda. El hueco de Ucoach no es que en Europa no haya nada, sino que nadie cruza agenda, trabajo y cuerpo con un método explícito e independiente del wearable. Lo europeo es solo un añadido temporal: ChatGPT y Claude todavía no leen datos de salud aquí.
4. **La competencia MCP directa existe pero está fragmentada.** Hay decenas de servidores MCP de datos (garmin_mcp con 1.525 estrellas, Open Wearables con 2.805, Apple Health MCP con 288, diario privado con 474), un registro local-first de conectores de bienestar (Delx Wellness) y servidores hospedados de hábitos y diario (LifeWheel, Litak). No he encontrado ninguno de código abierto que junte agenda, sueño, hábitos, ergonomía y un método explícito. El único «life coach» MCP abierto (Linell/coach) tiene 3 estrellas y lleva parado desde junio de 2025.
5. **La capa de datos se está volviendo un bien común.** Conectar Oura, Garmin o WHOOP ya lo resuelven proyectos MIT activos y conectores verificados del directorio de Claude. El plan Pro del doc, que cobra por «conectores directos con Oura, Garmin y Whoop», vende justo la parte que se está regalando.
6. **La proactividad de las plataformas se va a la nube, y eso choca con un MCP local.** Las tareas programadas de Claude Cowork se ejecutan en remoto aunque el ordenador esté apagado (`verified`), y Duet y dots trabajan en máquinas virtuales en la nube. Las sesiones remotas de Claude no llegan a un servidor MCP local por stdio salvo que la app de escritorio esté abierta y conectada, y ChatGPT solo admite MCP remotos o su «Secure MCP Tunnel» (`verified`, support.claude.com; `reported`, developers.openai.com) (corregido tras QA 2026-11-19). Así, el brief de mañana automático del doc corre riesgo.
7. **La cifra de mercado del doc es débil.** Los 5.800 M$ atribuidos a Virtue Market Research solo aparecen en un blog de certificación de coaches con enlaces de afiliado. La página del informe de Virtue (febrero de 2025, previsión 2025-2031, 4.250 $) no publica esa cifra (`verified`). Hay que sustituirla.
8. **Referencias de precio para el plan Pro:** Oura 5,99 $/mes, Garmin Connect+ 6,99 $/mes, Google Health Premium 9,99 $/mes (gratis con Google AI Pro), WHOOP de 199 a 359 $/año, Rise 69,99 $/año, Lifestack unos 7 $/mes (corregido tras QA 2026-11-19) y Rosebud 12,99 $/mes. Un Pro de 8 a 15 € compite con coaches que el usuario ya tiene incluidos en su wearable o en su IA.

---

## 2. Tabla de competidores

Columnas «Agenda» y «Sueño/energía»: si el producto integra de forma nativa el calendario del usuario y datos de sueño o energía. «Indirecto» = el usuario lo cuenta en el chat, o lo obtiene combinando conectores.

### 2.1 Coaches de IA de wearables y apps de salud

| Producto | Categoría | Qué hace | Precio | Agenda | Sueño/energía | Fuente · año · etiqueta |
|---|---|---|---|---|---|---|
| **WHOOP Coach** + My Memory + Proactive Check-Ins | Wearable | Coach con LLM sobre datos de WHOOP. En mayo de 2026 añade «My Memory» (contexto editable del usuario) y check-ins proactivos por notificación: «prioriza el sueño antes de un evento clave», ajustar el entreno en viajes, seguir el estrés laboral. También ofrece clínicos por vídeo en EE. UU. | One 199 $/año, Peak 239 $/año, Life 359 $/año; coach incluido (no confirmado por nivel: whoop.com da 403) (corregido tras QA 2026-11-19) | **No** nativa: el usuario cuenta sus eventos | Sí | Business Wire / WHOOP, 8-5-2026 (`reported`, la web oficial devuelve 403); precios trackervs, 2026 (`reported`) |
| **Oura Advisor** | Wearable | Asistente con IA sobre sueño, actividad, estrés y comidas; gráficos en el chat; planes para objetivos; LLM propio de salud femenina (febrero de 2026, en pruebas en Oura Labs); derivación clínica con Counsel Health en EE. UU. (8-6-2026; 159 $/año tras 30 días de prueba) (corregido tras QA 2026-11-19) | Membresía 5,99 $/mes o 69,99 $/año (5,99 €/mes o 69,99 €/año en la UE); Advisor incluido | No | Sí | Business Wire, 31-3-2025 (rollout a todos); the5krunner, 24-2-2026 (`reported`); ouraring.com/membership y ouraring.com/blog/counsel-integration-oura-app (`verified`) (corregido tras QA 2026-11-19) |
| **Google Health Coach** (antes Fitbit AI Coach) | Wearable / plataforma | Coach con Gemini: onboarding conversacional, planes semanales adaptativos, registro de comidas por voz o foto, historial médico solo en EE. UU. Exige Fitbit o Pixel Watch y ser mayor de 18; Apple HealthKit y Health Connect llegarán «later» y la integración con Lingo está prevista. Disponible en 37 países, entre ellos España (corregido tras QA 2026-11-19) | 9,99 $/mes o 99 $/año; **gratis con Google AI Pro y Ultra** | No (el horario se lo cuenta el usuario) | Sí | TechCrunch, 7-5-2026 (`reported`); blog.google/products-and-platforms/products/google-health/google-health-coach y support.google.com/googlehealth/answer/14237941 (`verified`); vista previa desde octubre de 2025, GA el 19-5-2026 (corregido tras QA 2026-11-19) |
| **Apple Health (rediseño, antes «Project Mulberry»)** | Plataforma | El coach independiente «Health+» se recortó en febrero de 2026 (Bloomberg, vía 9to5Mac). Según rumores, funciones como Insights con IA, Readiness o Health Age llegarán sueltas a la app Salud más adelante en el ciclo de iOS 27; no hay confirmación de que estén ya en una beta (corregido tras QA 2026-11-19) | Sin suscripción anunciada; análisis Quest por 119 $ (EE. UU.) | No | Sí | Gigazine, 6-2-2026; 9to5Mac, 29-8-2026; MacRumors, 16-9-2026 (`reported`, Apple no lo ha anunciado) |
| **Garmin Connect+** (Active Intelligence) | Wearable | Mensajes de IA al despertar, tras entrenar y por la noche (sueño, VFC, carga, estrés). Las reseñas la consideran pobre | 6,99 $/mes o 69,99 $/año | No | Sí | TechRadar, marzo de 2025; the5krunner, 20-4-2026 (`reported`) |
| **Samsung Health** | Wearable | Energy Score con IA, Vitals nocturnos, Heart Health Score, Daily Cardio Load. Health Assistant en beta en EE. UU. desde el 21-7-2026 (posiblemente con Gemini); Samsung anuncia respuestas «sensitive to a user's schedule» con su Personal Data Engine, que unas fuentes dan como actual y otras como futuro (corregido tras QA 2026-11-19) | Sin precio | No confirmado | Sí | Samsung Mobile Press, 4-6-2026 (`verified`); eWeek, julio de 2026 (`reported`) |
| **Ultrahuman Jade** | Wearable | «Biointeligencia» sobre todo el ecosistema Ultrahuman (anillo, CGM, análisis de sangre), con modos Standard y Deep Research | Sin suscripción obligatoria; Ring PRO de 479 $ a 499 € | No | Sí | FutureFive/IT Brief, principios de 2026 (`reported`, datos contradictorios) |
| **Rise Science** | App de sueño | Curva horaria de energía (picos, bajones, ventana de melatonina) a partir de la deuda de sueño; añade la previsión de energía como eventos de Google Calendar o Apple Calendar | 69,99 $/año (ofertas a 59,99 y 35,99 $) | **Sí** (exporta la previsión al calendario) | Sí | App Store (apps.apple.com/us/app/rise-sleep-tracker/id1453884781, `verified`); ayuda de Rise sobre el calendario (`reported`) (corregido tras QA 2026-11-19) |
| **Lifestack** | Planificador con energía | «Energy-first planning»: pasa las tareas al calendario según la energía estimada con Apple Health, Oura, WHOOP, Garmin y Fitbit; IA para planificar día y semana. En 2026 se presenta como «AI Planner for ADHD». 4,4★ (73 valoraciones) | Unos 7 $/mes, 50 $/año o 120 $ de por vida (`reported`, blog.saner.ai) (corregido tras QA 2026-11-19) | **Sí** (Google, Outlook; tareas en Todoist y Trello) | **Sí** | App Store, nov. 2026 (`verified` para funciones y valoración) |

### 2.2 Calendario y productividad con IA

| Producto | Categoría | Qué hace | Precio | Agenda | Sueño/energía | Fuente · año · etiqueta |
|---|---|---|---|---|---|---|
| **Reclaim.ai** (de Dropbox) | Calendario IA | Bloques de foco, hábitos, pausas y reuniones. **Conector MCP para Claude y Claude Code**, Copilot y ChatGPT | Lite gratis; Starter 10-12 $; Business 15-18 $; Enterprise 22 $ (por plaza y mes) | Sí | No | reclaim.ai/pricing, 2026 (`verified`) |
| **Motion** | Suite de trabajo con agentes | Pasó de calendario automático a «AI Employees» y suite de trabajo para pymes. Ronda de 60 M$ con valoración de 550 M$ (sept. 2025) | Pro AI 19 $; Business AI 29 $ (por plaza y mes) | Sí | No | usemotion.com/pricing (`verified`); Business Wire, 5-9-2025 (`reported`) |
| **Clockwise** | Calendario IA | **Cerró el 27-3-2026** (anunciado el 19-3-2026); el equipo se une a Salesforce; Reclaim fue la alternativa recomendada | n. a. | n. a. | n. a. | getclockwise.com (`verified`); blog de Reclaim, marzo de 2026 (corregido tras QA 2026-11-19) |
| **Sunsama** | Planificador diario | Planificación diaria guiada y límites de carga; **MCP incluido en Pro** | 17 $/mes (anual) o 22 $ (mensual) | Sí | No | sunsama.com/pricing (`verified`) |
| **Akiflow** | Bandeja y calendario | Asistente «Aki»; **conector MCP alojado** en Pro | 19 $/mes (anual) o 34 $ (mensual) | Sí | No | akiflow.com/pricing (`verified`) |
| **Morgen** | Calendario IA | Planificación diaria con IA; se ofrece como sustituto de Clockwise | 15 $/mes (anual) o 30 $ (mensual) | Sí | No | morgen.so/pricing (`verified`) |
| **Amie** | Calendario y notas | Calendario con asistente, notas de reunión locales sin bot | Pro y Business sin precio público; 20-25 $/mes según terceros; unos 7 M$ captados según VCBacked, más 1,3 M$ de presemilla en 2020 (corregido tras QA 2026-11-19) | Sí | No | amie.so/pricing (`verified`, sin precios); VCBacked y TechCrunch (`reported`) |
| **Timing** | Registro de tiempo (Mac) | Registro automático del tiempo; resúmenes con IA; **MCP en el plan Connect** | Professional 10 $/mes; Connect 168 $/año | No (registra uso) | No | timingapp.com/pricing (`verified`) |

### 2.3 Coaching con IA: ejecutivo, emprendedor y vida

| Producto | Categoría | Qué hace | Precio | Agenda | Sueño/energía | Fuente · año · etiqueta |
|---|---|---|---|---|---|---|
| **Valence · Nadia** | Coaching ejecutivo B2B | Coach de liderazgo en Fortune 500 (Delta, Experian, Kraft Heinz). Serie B de 50 M$ liderada por Bessemer (sept. 2025); unos 75 M$ en total | Empresa, sin precio público | Integraciones de trabajo (no verificado) | No | Built In, 26-9-2025; nota de Valence (`reported`) |
| **BetterUp AI Coaching / Grow** | Coaching B2B (+B2C) | Coach con IA junto a coaches humanos (lanzado el 21-1-2025, fecha sin confirmar). Según su ayuda oficial, «BetterUp for Individuals» se está cerrando y no admite altas: la oferta se centra en empresas (corregido tras QA 2026-11-19) | Sin precio público; se estiman 3.000-5.000 $ por usuario y año | No | No | support.betterup.com/hc/en-us/articles/5023276679835 (`reported`, extracto); risely.me (`reported`) (corregido tras QA 2026-11-19) |
| **CoachHub AIMY** | Coaching B2B | Coach conversacional 24/7 (anunciado el 11-2-2025); AIMY 2.0 el 4-11-2025 (corregido tras QA 2026-11-19) | Empresa | No | No | coachhub.com, 2025 (`reported`) |
| **Rocky.ai** | Coach personal y marca blanca | Coaching diario por chat; plataforma de coach en marca blanca para coaches | Consumidor: 19,99 $/mes o 99,99 $/año en la App Store (`reported`); empresas y coaches: de 49 a 399 $/mes según plazas (`verified`, help.rocky.ai) (corregido tras QA 2026-11-19) | No | No | help.rocky.ai/rocky-for-creators/business-pricing-packages; agregadores |
| **Rosebud** | Diario con IA | Diario interactivo. Semilla de 6 M$ (Bessemer, junio de 2025); sin plan gratis desde el 30-9-2026 (según un competidor) | Bloom 12,99 $/mes o 107,99 $/año | No | No | TechCrunch, 4-6-2025; mylifenote, 2026 (`reported`) |
| **Mindsera** | Diario con IA | Diario con análisis de emociones y patrones | Plan gratuito y «Genius» por unos 129 $/año; precio mensual sin confirmar (corregido tras QA 2026-11-19) | No | No | mylifenote, 2026 (`reported`) |
| **Ama** | Coach para emprendedores | Se presenta como «el primer coach de IA proactivo para emprendedores», que aprende de lo que te agota; lanzado en Product Hunt, fecha sin confirmar (corregido tras QA 2026-11-19) | No verificado | No verificado | No verificado | Product Hunt (`reported`) |
| **Whenever** | Coach para fundadores | Protocolo diario de estrés, salud y rendimiento con datos personales e investigación | No verificado | No verificado | Probable | chatgate.ai (`reported`, fuente original retirada: el enlace da 404) (corregido tras QA 2026-11-19) |
| **Founder Coach** | Coach para fundadores | Seguimiento de OKR con coach persistente (12-2-2026) | No verificado | No | No | Product Hunt (`reported`) |

### 2.4 Servidores y conectores MCP de salud, hábitos y coaching (competencia directa)

Estrellas y última actividad consultadas en la API de GitHub el 2026-11-19 (`verified`).

| Proyecto | Tipo | Qué hace | Precio | Agenda | Sueño/energía | Datos (2026) |
|---|---|---|---|---|---|---|
| **athletedata** (HealthspanOS AG) | Conector del directorio de Claude, «Anthropic verified» | Lee Garmin, WHOOP, Oura, Apple Health y otras 29 apps, más de 30 fuentes en total (corregido tras QA 2026-11-19). Envía entrenos al reloj, programa en TrainingPeaks, intervals.icu y Hevy y **añade entrenamientos a Google Calendar**; tiene notas de coaching | Suscripción (precio no publicado) | **Sí** (escribe entrenos) | Sí | claude.com, añadido en sept. 2026 (`verified`) |
| **Wellness Project** | Conector comunitario del directorio de Claude | Historial unificado de entrenos, comidas, sueño, recuperación, análisis y wearables; 15 herramientas con gráficos en el chat | Basic gratis; Pro 9,99 $/mes (la promoción a 4,99 $ terminó el 15-10-2026) (corregido tras QA 2026-11-19) | No | Sí | Nota de prensa, 2-10-2026 (`verified`) |
| **Delx Wellness** (davidmosiah) | Registro de MCP local-first (MIT) | 16 conectores locales de solo lectura (Google Health, Garmin, WHOOP, Oura, Strava, Fitbit, Withings, Polar, Apple Health, Samsung Health, Eight Sleep, CGM, nutrición y otros). El meta-MCP `delx-living-body` (`living_body_daily_brief`, `living_body_ask`) responde preguntas como «¿entreno fuerte hoy?» con reglas offline. Perfiles «Daily Operator» para los agentes Hermes y OpenClaw (corregido tras QA 2026-11-19) | Gratis | No | Sí | 28★ en el registro, activo en nov. 2026 (`verified`) |
| **garmin_mcp** (Taxuspt) | MCP de datos (MIT) | Acceso a Garmin Connect | Gratis | No | Sí | **1.525★**, activo en oct. 2026 (`verified`) |
| **Open Wearables** (The Momentum) | Plataforma autoalojada + MCP (MIT) | API unificada para Oura, Garmin, WHOOP, Apple Health, Polar, Suunto, Samsung, Strava y Health Connect; puntuaciones de sueño, recuperación y esfuerzo; MCP en beta | Gratis (autoalojado) | No | Sí | **2.805★**, activo el 19-11-2026 (`verified`) |
| **apple-health-mcp-server** (The Momentum) | MCP de datos (MIT) | Consultas en lenguaje natural sobre el export de Apple Health con DuckDB | Gratis | No | Sí | 288★, julio de 2026 (`verified`) |
| **totem** (thebriangao) | MCP de WHOOP (API privada por ingeniería inversa) | 55 herramientas: recuperación, sueño, esfuerzo, diario, Whoop Coach, alarma inteligente | Gratis | No | Sí | 144★, sept. 2026 (`verified`); riesgo de términos de uso |
| **oura-ring-mcp**, **whoop-mcp** y decenas más | MCP de datos | Lectura de un único wearable | Gratis | No | Sí | 13-37★ (`verified`) |
| **private-journal-mcp** (obra) | MCP de diario (MIT) | Diario privado con búsqueda semántica para Claude | Gratis | No | No | 474★, nov. 2026 (`verified`) |
| **LifeWheel** | MCP hospedado | 21 herramientas: rueda de la vida, hábitos, objetivos, diario, ánimo y revisión semanal; ChatGPT (Apps SDK), Claude, Cursor | Conector gratis; app freemium | No | No | lifewheel.us (`verified`) |
| **Litak** | MCP hospedado | Planificador de equilibrio vital en 12 áreas; hábitos (máximo 6 en el plan gratuito) | Freemium | No | No | mcpservers.org (`reported`) |
| **Linell/coach** | MCP «life coach» (MIT) | Objetivos, tareas, notas y guía diaria | Gratis | No | No | 3★, **sin actividad desde 6-2025** (`verified`) |
| **wellness_planner** (rwking) | MCP experimental | `propose_schedule`: horario diario según una puntuación de disposición | Gratis | Tareas, no calendario | Sí | 0★, febrero de 2026 (`verified`) |

Contexto: no hay un total oficial de servidores MCP. El registro oficial devolvía 52.042 entradas el 28-10-2026, con duplicados y obsoletos; los censos deduplicados dan 22.561 en junio de 2026 (`reported`, agentndx-web.pages.dev). El directorio de conectores de Claude tenía 369 en junio de 2026 y entre 934 y 986 en octubre (`reported`, dirjournal.com) (corregido tras QA 2026-11-19).

### 2.5 Agentes personales y funciones de las plataformas de IA

| Producto | Qué hace relevante para Ucoach | Disponibilidad y precio | Fuente · año · etiqueta |
|---|---|---|---|
| **Claude: integraciones de salud** | Apple Health y Android Health Connect en beta; conectores HealthEx y Function para historial y análisis. Las conversaciones de salud no entrenan modelos ni van a la memoria | EE. UU., Pro y Max, desde enero de 2026 | anthropic.com/news/healthcare-life-sciences, 11-1-2026 (`verified`); Fortune; MacTrast (corregido tras QA 2026-11-19) |
| **Claude Cowork: tareas programadas** | Un prompt recurrente (por ejemplo un brief diario) con conectores, skills y plugins. **Se ejecuta en remoto**, también con el ordenador apagado. «Require this computer» solo existe para organizaciones con Computer access | Todos los planes de pago | support.claude.com, 2026 (`verified`) |
| **Claude Duet** | Agente proactivo en una VM en la nube: brief matinal sobre correo y calendario, sigue trabajando sin el usuario y pide permiso antes de enviar, pagar o borrar. Hereda memoria, skills y conectores | Vista previa con lista de espera, solo EE. UU., Pro, Max y Ultra, desde el 21-10-2026; sin coste extra (consume los límites del plan) | claude.com/resources/articles/claude-duet (`verified`); 9to5Mac, 21-10-2026 (corregido tras QA 2026-11-19) |
| **Memoria de Claude** | Memoria abierta a todos los usuarios, incluido el plan gratuito | 2 de marzo de 2026 | 9to5Mac, 2-3-2026 (`reported`) (corregido tras QA 2026-11-19) |
| **ChatGPT Health** | Espacio de salud separado; Apple Health, historial médico (EE. UU.), MyFitnessPal y Function; datos excluidos del entrenamiento | Anunciado el 7-1-2026; despliegue en EE. UU. el 23-7-2026; **excluidos el EEE, Suiza y el Reino Unido** | 9to5Mac y MacRumors, enero de 2026; trendingtopics.eu (`reported`) |
| **ChatGPT: tareas programadas** (antes Pulse) | Pulse, el brief diario proactivo con Gmail y Calendar opcionales, se lanzó en Pro el 25-9-2025 y **se retiró el 17-6-2026**. Lo sustituyen las tareas programadas, con hub propio | Go, Plus, Pro, Business y Enterprise desde el 17-6-2026; conectores de Gmail y Calendar no disponibles en el EEE, Suiza y el Reino Unido | engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks (`reported`) (corregido tras QA 2026-11-19) |
| **ChatGPT dots** | Agentes siempre activos con ordenador y navegador propios en la nube, más de 4.000 apps e investigación proactiva | Pro y Business Premium desde el 29-9-2026 (DevDay); el despliegue en Pro excluye el EEE, Suiza y el Reino Unido (corregido tras QA 2026-11-19) | Digital Trends y BetaNews, sept. 2026 (`reported`; openai.com da 403) (corregido tras QA 2026-11-19) |
| **Gemini + Google Health** | Personal Intelligence conecta Gemini con las apps de Google (enero de 2026). El Health Coach está incluido en Google AI Pro y Ultra. No he encontrado prueba de que Gemini cruce Calendar con datos de Google Health | Personal Intelligence: EE. UU. desde el 14-1-2026 y fuera de EE. UU. desde el 14-4-2026, salvo Europa. Health Coach: 37 países, España incluida, desde el 19-5-2026 (corregido tras QA 2026-11-19) | Blog de Google, 14-1-2026; TechCrunch, 7-5-2026 (`reported`) |
| **OpenClaw** | Agente personal autoinstalable; mensajería, correo, calendario y skills (ClawHub) | MIT, **394.783★**; fundación con apoyo de OpenAI | GitHub API, 19-11-2026 (`verified`) |
| **Hermes Agent** (Nous Research) | Agente autoalojado con memoria local (`~/.hermes`), Telegram, WhatsApp y Slack; crea sus propias skills | MIT, **264.581★**, repositorio creado el 22-7-2025 (corregido tras QA 2026-11-19) | GitHub API (`verified`); vellum.ai (`reported`) |

---

## 3. Verificación de los datos del documento v0.1

| Afirmación del doc | Veredicto | Detalle |
|---|---|---|
| «Virtue Market Research: 5.800 M$ a finales de 2026» | **Débil, no usar** | Solo lo cita un blog de certificación de coaches con enlaces de afiliado (lifecoachtraining.pages.dev). La página del informe de Virtue (VMR-18060, publicado en febrero de 2025, previsión 2025-2031, 4.250 $) no muestra ninguna cifra (`verified`). La segunda ficha de Virtue sobre el tema («AI Life Coach Tools Market», VMR-18158) tampoco la publica (`verified`) (corregido tras QA 2026-11-19). Además, sería la estimación más alta de las encontradas. |
| «OpenAI confirmó el 15-2-2026 la incorporación de Peter Steinberger» | **Correcto, con un matiz** | Sam Altman lo anunció en X el 15-2-2026; Steinberger lo había publicado el día antes en steipete.me (`reported`: Fortune, Engadget, Gizmodo y otros). Matiz: OpenAI no compró OpenClaw. El proyecto pasa a una fundación independiente de código abierto con apoyo de OpenAI. El doc debería decirlo así. |
| WHOOP Coach «incluido en la suscripción de 199 a 359 $ al año» | Correcto | One 199 $, Peak 239 $ y Life 359 $ (`reported`, 2026); no se ha podido confirmar si el coach va incluido en todos los niveles (corregido tras QA 2026-11-19). Le falta lo nuevo: memoria y check-ins proactivos (mayo de 2026). |
| Fitbit AI Coach «en vista previa pública desde finales de 2025» | **Desactualizado** | Ahora se llama Google Health Coach y está disponible para todos desde el 19-5-2026, en la app Google Health, por 9,99 $/mes o 99 $/año, y gratis con Google AI Pro y Ultra. Funciona en 37 países, España incluida, y exige Fitbit o Pixel Watch (`reported` TechCrunch; `verified` blog de Google y support.google.com/googlehealth/answer/14237941) (corregido tras QA 2026-11-19). |
| Oura Advisor «ecosistema cerrado» | Correcto, pero incompleto | Ya integra comidas, hábitos y rutinas, tiene un LLM propio de salud femenina en pruebas y deriva a clínicos de pago en EE. UU. (2026). Está disponible en España y en español (corregido tras QA 2026-11-19). |
| Reclaim «no conoce el sueño ni la energía» | Correcto | Pero ahora es un **conector MCP para Claude**: socio potencial, no solo competidor. |
| «Motion y similares: productividad sin salud» | Correcto | Motion pivotó a una suite de agentes para pymes. Clockwise cerró en marzo de 2026. |
| «Ninguna [pieza] cruza la agenda real con el sueño, la energía y los hábitos» | **Falso** | Lifestack (energía + calendario + wearables), Rise (curva de energía en el calendario), athletedata (wearables + Google Calendar en Claude). Ninguno lo hace con la profundidad de Ucoach en contexto de trabajo, pero el cruce como tal no es único. |
| «Los grandes fabricantes de wearables ya han lanzado coaches basados en LLM» | Correcto | WHOOP, Oura, Google y Garmin lo tienen; Samsung y Ultrahuman en 2026; Apple lo retrasa. |

### Tamaño de mercado: alternativas

Las definiciones no son comparables. Conviene citar un rango con su fuente y no una cifra única.

| Estimación | Cifra | Fuente | Fiabilidad |
|---|---|---|---|
| Coaching profesional (todos los tipos, ingresos de coaches) | 5.340 M$ de ingresos globales; 122.974 coaches | ICF Global Coaching Study 2025, elaborado por PwC | **Alta** (encuesta primaria) |
| Coaches de salud con IA | 1.500 M$ (2025) → 8.800 M$ (2032), TACC del 27,9 % | Stratistics MRC, 2025 | Media-baja (consultora de pago) |
| Coaching de salud y bienestar (con y sin IA) | 16.500-20.100 M$ en 2025, según la consultora | Fortune BI (16.500 M$) y Precedence (20.100 M$); la cifra de The Business Research Company no se ha encontrado (corregido tras QA 2026-11-19) | Baja-media; el rango muestra que no hay consenso |
| Plataformas de coaching de carrera con IA | Sin cifra verificada: la ficha de Stratistics no se ha encontrado; Market.us estima 5.000 M$ en 2025 para «AI career coach» (`reported`) (corregido tras QA 2026-11-19) | Market.us | Baja |

**Recomendación:** quitar el TAM del documento y sustituirlo por un cálculo de abajo arriba: emprendedores hispanohablantes que pagan una IA con MCP y llevan un wearable, por tasa de conversión, por precio. Para una fase de 20 usuarios y un open core, el TAM no aporta nada y una cifra floja resta credibilidad (`inferred`).

---

## 4. Taxonomía del panorama y hallazgo no obvio

### Taxonomía (noviembre de 2026)

```
                      DATOS DEL CUERPO ──────────────────────────────►
                      ninguno            un wearable           multi-fuente
CONTEXTO   ninguno    Diarios IA         Coaches de wearable   Open Wearables, Delx,
DE TRABAJO            (Rosebud,          (WHOOP, Oura, Google, Wellness Project
   │                  Mindsera,          Garmin, Samsung,      (capa de datos,
   │                  LifeWheel)         Ultrahuman, Apple)    sin método)
   │       tareas y   Reclaim, Motion,                         Lifestack (consumo,
   │       calendario Sunsama, Akiflow,                        ADHD), Rise (sueño
   │                  Morgen                                   → curva en calendario),
   │                                                           athletedata (entrenos)
   ▼       trabajo    Valence, BetterUp,                       ◄── ¿Ucoach? Plataformas
           completo   CoachHub (B2B,                           (Claude Duet + Health,
                      liderazgo)                               ChatGPT dots + Health)
                                                               cuando junten piezas
```

Cinco capas, de abajo arriba (Morgen no tiene MCP oficial: corregido tras QA 2026-11-19):

1. **Datos:** wearables y sus API, más los MCP de datos. Ya es un bien común: es MIT, se puede autoalojar y hay conectores verificados.
2. **Conectores de trabajo:** calendario, correo y tareas. Las plataformas los dan de serie y Reclaim, Sunsama, Akiflow y Timing ya publican MCP.
3. **Motor de la IA:** Claude, ChatGPT o Gemini. Gratis para Ucoach porque lo paga el usuario.
4. **Proactividad:** tareas programadas de Claude y de ChatGPT (Pulse se retiró el 17-6-2026), dots, Duet, OpenClaw y Hermes. Las plataformas la están absorbiendo, en la nube (corregido tras QA 2026-11-19).
5. **Método:** reglas, protocolos, evidencia, seguimiento longitudinal y experimentos personales. Delx ya ofrece recomendaciones diarias abiertas con reglas offline («¿entreno fuerte hoy?»), pero sin contexto de trabajo. **Nadie ofrece de forma abierta un método que cruce agenda, trabajo y cuerpo con niveles de evidencia explícitos** (corregido tras QA 2026-11-19).

### El hallazgo no obvio

**El hueco de Ucoach no está en cruzar agenda y sueño, que ya hacen Lifestack, Rise y athletedata y que harán las plataformas en cuanto el usuario conecte dos conectores. Está en ser la capa de método y memoria longitudinal que cruza agenda, trabajo y cuerpo con reglas explícitas e independiente del wearable, algo que no hacen ni las plataformas ni los coaches de wearable.** En Europa hay además una ventaja temporal: ChatGPT y Claude no leen datos de salud aquí, aunque Google Health Coach (con Fitbit o Pixel Watch) y Oura Advisor sí funcionan en España (corregido tras QA 2026-11-19).

Cuatro pruebas lo sostienen:

- **Las plataformas evitan el método por riesgo regulatorio.** ChatGPT Health y las integraciones de salud de Claude se quedan en explicar, resumir y preparar preguntas para el médico, y ChatGPT Health excluye el EEE. OpenAI no ha explicado por qué; la prensa lo atribuye a la regulación de los datos de salud (RGPD art. 9, AI Act, posible producto sanitario) (`reported`, notebookcheck.net y doctors.net.uk) (corregido tras QA 2026-11-19). Que la causa sea el riesgo regulatorio es una hipótesis (`inferred`). Un protocolo opinado («hoy no entrenes fuerte, siesta de 20 minutos, último café a las 15:00») es justo lo que no van a publicar como producto propio en la UE a corto plazo (`inferred`).
- **Las plataformas no guardan una serie temporal estructurada del usuario.** La memoria de Claude o ChatGPT recuerda hechos, no 90 noches de sueño junto a check-ins de energía y carga de reuniones. Según la ayuda de Claude, la memoria está diseñada para no usar la información sensible de salud en conversaciones futuras (`reported`, extracto de support.claude.com) (corregido tras QA 2026-11-19). Un SQLite local con esa serie permite algo que el chat no hace bien: comparar «mis días tras dormir 7 horas o más contra el resto» con números propios.
- **Los wearables no ven el trabajo.** WHOOP ya hace check-ins proactivos «antes de un día importante», pero solo si el usuario se lo cuenta (`reported`). Ninguno lee el calendario de forma nativa; Samsung anuncia un Personal Data Engine que tendría en cuenta la agenda, sin confirmar si ya funciona (`reported`, mobileworldlive.com) (corregido tras QA 2026-11-19). Es una barrera débil: añadir un conector de calendario es trivial para WHOOP (`inferred`).
- **La capa de datos sobra como negocio.** Open Wearables (2.805★) y garmin_mcp (1.525★) son MIT y están activos, y Delx Wellness reúne 16 conectores de solo lectura. Delx ya añade un brief diario con reglas offline, así que Ucoach no compite por los datos ni por un consejo diario genérico, sino por el método con contexto de trabajo y niveles de evidencia (`verified`, API de GitHub y README de davidmosiah/delx-wellness) (corregido tras QA 2026-11-19).

**Matiz que debilita la tesis local-first:** donde las plataformas ponen la proactividad (tareas programadas remotas, Duet, dots) no se llega a un servidor stdio en el portátil, salvo con la app de escritorio de Claude abierta y conectada (`verified`, support.claude.com/en/articles/15811196) (corregido tras QA 2026-11-19). Si Ucoach es solo local, el brief de mañana dependerá del cron y Telegram propios, no de la IA, y perderá su argumento de que «vive dentro de tu IA». Es la tensión técnica principal que debe resolver la línea 4.

---

## 5. Amenazas concretas y diferenciales

### Amenazas (ordenadas por probabilidad × impacto)

| # | Amenaza | Probabilidad | Impacto | Señal a vigilar |
|---|---|---|---|---|
| 1 | **Las plataformas generalistas llegan a Europa** con salud, calendario y agente proactivo (Claude Duet + Health, ChatGPT Health + dots y tareas programadas). Google ya está: Health Coach funciona en España (corregido tras QA 2026-11-19) | Alta en 12-24 meses | Muy alto: el usuario tendría buena parte de Ucoach sin instalar nada (corregido tras QA 2026-11-19) | Fecha de salida de ChatGPT Health o de Claude Health en el EEE |
| 2 | **La proactividad en la nube deja fuera al MCP local** (tareas remotas, Duet y dots en VM) | Alta (ya es así) | Alto: rompe el ritual del brief automático | A noviembre de 2026 solo hay puente si la app de escritorio de Claude está abierta y conectada (corregido tras QA 2026-11-19); vigilar si Cowork o Duet admiten conectores locales sin ella |
| 3 | **Un wearable añade el calendario** (WHOOP es el candidato obvio: ya tiene memoria y check-ins proactivos; Samsung anuncia un Personal Data Engine que tendría en cuenta la agenda) (corregido tras QA 2026-11-19) | Media-alta | Alto en el segmento con wearable caro | Notas de producto de WHOOP, Oura y Samsung |
| 4 | **Lifestack u otro planificador con energía** se mueve hacia profesionales o publica un MCP | Media | Medio: ya cobra unos 7 $/mes y no exige instalar nada (corregido tras QA 2026-11-19) | Cambios en su App Store; integración con Claude |
| 5 | **Hazlo tú mismo:** el usuario técnico (el público de la fase 1) junta garmin_mcp, el calendario y un prompt o una skill de coaching | Alta en fase 1 | Medio: es justo el público inicial; GrowthMentor ya recomienda «ChatGPT o Claude con rol de coach y tu contexto real» | Plantillas de prompt y skills de «health coach» en directorios |
| 6 | **Conectores verificados en el directorio de Claude** (athletedata, Wellness Project) se quedan con la distribución sin instalación | Media | Medio | Nuevas fichas de salud y coaching en claude.com/connectors |
| 7 | **Google AI Pro incluye Health Coach** y regala el coach a quien ya paga Gemini y lleva Fitbit o Pixel Watch, también en España (corregido tras QA 2026-11-19) | Ya ocurre | Medio: fija el precio de referencia del coaching de salud en 0 € para ese usuario | n. a. |
| 8 | **Incidente de seguridad en agentes personales** (OpenClaw: más de 1.184 skills maliciosas confirmadas en ClawHub a 1-3-2026 y varias CVE, entre ellas CVE-2026-25253; corregido tras QA 2026-11-19) que contamina la percepción de «MCP que toca datos de salud» | Media | Medio | Prensa de seguridad sobre MCP de salud |

### Diferenciales que aguantan

1. **Método explícito y auditable con niveles de evidencia.** Ningún competidor encontrado publica sus reglas y su grado de evidencia. Encaja con el posicionamiento aclarado (buenas prácticas, cada una con su nivel de evidencia). Es copiable, pero solo con trabajo editorial sostenido.
2. **Contexto de trabajo profundo:** reuniones clave por palabras, cadenas de reuniones sin pausa, preparación de negociaciones y ventanas de foco según el cronotipo. Lifestack parte de tareas y TDAH, WHOOP de deporte y Valence de liderazgo. El cruce de la carga de reuniones con la energía medida es propio.
3. **Disponible en Europa y en español, con datos locales y con cualquier wearable.** En España ya hay coaches de salud con IA (Google Health Coach con Fitbit o Pixel Watch, Oura Advisor), pero ninguno mira la agenda, y ChatGPT y Claude todavía no leen datos de salud aquí. Es una ventana de tiempo, no un foso, pero sirve para ganar los primeros usuarios y aprender (corregido tras QA 2026-11-19).
4. **Independiente del dispositivo** (Apple Health, CSV, cualquier MCP de datos) e independiente del proveedor de IA.
5. **Seguridad por diseño:** solo librería estándar, sin red salvo Telegram, sin skills de terceros, solo lectura y sugerencia. Contrasta con OpenClaw y con los MCP que piden usuario y contraseña de WHOOP o usan API privadas.

### Diferenciales del doc que **no** aguantan

- «Contexto cruzado» como algo único: ya existe (apartado 3).
- «Vive dentro de tu IA»: también athletedata, Wellness Project, LifeWheel y Delx.
- «El coste del modelo lo cubre la suscripción del usuario»: es igual para cualquier MCP.
- «Biblioteca de 103 libros»: es fácil de replicar con un LLM y aporta poco por sí sola. Su valor está en conectarla con el hábito más flojo de la revisión semanal, no en el catálogo.

---

## 6. Mejoras propuestas para Ucoach

### P0: antes de enseñar el producto a los 20 emprendedores

1. **Corregir el documento:** quitar «ninguna cruza la agenda con el sueño» y la cifra de Virtue; actualizar Fitbit a Google Health Coach (mayo de 2026); matizar lo de OpenClaw (fundación, no compra); añadir Lifestack, Rise, athletedata, Delx y las plataformas (Health, Duet, dots, Google Health Coach en España) a la tabla de competencia (corregido tras QA 2026-11-19).
2. **Reposicionar a Ucoach como capa de método, no de datos.** Una frase posible: «El método de un coach de alto rendimiento, con tus datos y en tu IA. Tú conectas tu wearable; Ucoach decide qué hacer hoy y aprende de tus semanas». Encaja con el alcance aclarado (eficiencia y excelencia profesional).
3. **Aceptar datos de cualquier MCP de wearables a través de la IA**, igual que ya hace con las reuniones. Que `planificar_dia` y `registrar_sueno` reciban sueño, VFC o disponibilidad que la IA saca de garmin_mcp, Open Wearables, Delx u Oura MCP, y documentar las combinaciones probadas. Así se elimina la fase 2 de «conectores Oura, Garmin y Whoop por API oficial» y se ahorran meses (la API de salud de Garmin exige aprobación y acuerdo de licencia, y Garmin congeló las altas nuevas desde la primavera de 2026; en octubre seguía cerrada: `reported`, the5krunner.com/2026/09/14/garmin-developer-api-access-paused) (corregido tras QA 2026-11-19).
4. **Resolver la proactividad fuera del portátil.** Hay tres caminos, a validar en la línea 4 (`inferred`):
   a. Un modo remoto opcional con HTTP *streamable*, autoalojado (Raspberry o VPS), para que las tareas programadas de Cowork, Duet o dots puedan llamarlo.
   b. Mantener el `nudge` por cron y Telegram como canal principal y presentarlo así.
   c. Un brief que se genere localmente y se entregue por Telegram, sin la IA.
   d. Aprovechar los puentes que ya existen: la app de escritorio de Claude abierta y conectada da acceso a los MCP locales, y ChatGPT ofrece un «Secure MCP Tunnel» para servidores locales (`verified` para Claude; `reported` para ChatGPT) (corregido tras QA 2026-11-19).
   Mientras tanto, el doc no debería prometer «tareas programadas de la IA» sin esta salvedad.
5. **Abrir con Europa, pero vendiendo el método (corregido tras QA 2026-11-19).** Ofrecer Ucoach a emprendedores de la UE como el coach que cruza su agenda y su trabajo con su cuerpo, con cualquier wearable y dentro de la IA que ya usan. «Lo que ChatGPT Health y Claude Health todavía no te dan aquí» vale como argumento secundario. No vale «ninguna IA te da esto en Europa», porque Google Health Coach (con Fitbit o Pixel Watch) y Oura Advisor funcionan en España. Puerta de entrada: el importador de Apple Health, que cubre a quien no lleva Fitbit ni Pixel Watch. Revisar la carga regulatoria con la línea 5: si las plataformas evitan la UE por riesgo de software sanitario (hipótesis, no confirmada por OpenAI), Ucoach necesita una formulación de bienestar muy cuidada.

### P1: durante la validación (meses 2 y 3)

6. **Métricas de trabajo que ningún wearable tiene:** horas de reunión al día, porcentaje de foco protegido, reuniones fuera de horario, cadenas sin pausa, y energía del check-in por tipo de reunión. Añadirlas a `revision_semanal` como «tu coste energético por tipo de reunión». Es el diferencial más defendible frente a WHOOP y Lifestack.
7. **Experimentos personales (n-of-1) en la revisión semanal:** «esta semana, último café a las 14:00; comparamos tu sueño y tu energía con la semana anterior». Usa la serie temporal local, que las plataformas no guardan, y se apoya en el principio de un hábito cada vez.
8. **Nivel de evidencia visible en cada recomendación** (A/B/C/D según la línea 7 del alcance), devuelto por la herramienta para que la IA lo muestre. Hace tangible el diferencial de «método explícito».
9. **Interoperar con Reclaim, Sunsama y Akiflow por MCP.** Ucoach propone el bloque de foco y el usuario deja que Reclaim lo defienda. Es mejor socio que rival, y Reclaim ya está en el ecosistema de Claude.

### P2: antes del plan Pro

10. **Replantear el plan Pro.** Las referencias de precio indican que el coach de salud viene incluido (WHOOP, Oura, Google con AI Pro) y que los planificadores cobran entre 10 y 20 $. Hay tres opciones a probar:
    a. Pro sin conectores, con sincronización cifrada entre dispositivos, avisos móviles y programas de 30 días. El precio lo fija la línea 6, que propone 8-12 €/mes y solo si la validación muestra demanda (corregido tras QA 2026-11-19).
    b. Pago único por programas (sueño de fundador, temporada de ronda de inversión).
    c. **B2B2C con aceleradoras y equipos de plataforma de fondos de capital riesgo**, que pagan el bienestar de su cartera. Valence, BetterUp y CoachHub demuestran que la empresa paga y el consumidor no tanto, aunque venden a grandes empresas, no a aceleradoras; BetterUp está cerrando su plan para particulares (`inferred`). La línea 6 prioriza a los coaches humanos (plan Coach) y deja las aceleradoras para la fase de escala (corregido tras QA 2026-11-19).
11. **Distribución en registros:** registro oficial de MCP, Glama, Smithery, mcp.so y el registro Delx (es local-first y ya tiene un perfil de Hermes). Si se hace el modo remoto, estudiar la entrada en el directorio de conectores de Claude.
12. **Convertir la seguridad en argumento:** firmar las versiones, publicar un SBOM (trivial sin dependencias), una página de «qué datos salen y cuáles no» y una comparativa explícita con OpenClaw y con los MCP de API privadas.
13. **Empaquetar como plugin o skill de Claude, además de MCP**, para que los rituales (brief, cierre, revisión) vengan como instrucciones y no dependan de que el usuario abra el prompt. Comprobar la viabilidad en la línea 4.

---

## 7. Índice de fuentes

**Wearables y apps de salud**
- WHOOP: nota de prensa de mayo de 2026 (Business Wire): https://businesswire.com/news/home/20260508464188/en/WHOOP-Expands-Health-Platform-with-On-Demand-Clinician-Access-and-New-AI-Features
- WHOOP: novedades 2026: https://www.whoop.com/us/en/thelocker/2026-whats-new/ · guía de IA: https://www.whoop.com/us/en/thelocker/new-ai-guidance-from-whoop/
- WHOOP: precios 2026 (trackervs): https://trackervs.pages.dev/pricing/whoop-pricing/
- Oura Advisor para todos los miembros (Business Wire, 2025): https://www.businesswire.com/news/home/20250331565896/en/Oura-Advisor-an-AI-powered-Personal-Health-Companion-Now-Rolling-Out-to-All-Oura-Members
- Oura Advisor Labs (the5krunner, 2026): https://the5krunner.com/2026/02/24/oura-advisor-labs-update-best-womens-health-guidance-grounded-in-your-data-whats-new/ · Counsel (blog de Oura): https://ouraring.com/blog/counsel-integration-oura-app/ · disponibilidad en España: https://support.ouraring.com/hc/en-us/articles/41056787356307 (corregido tras QA 2026-11-19)
- Oura: membresía (recurdash): https://recurdash.com/subscription-pricing/oura
- Google Health Coach, 9,99 $ (TechCrunch, 7-5-2026): https://techcrunch.com/2026/05/07/googles-9-99-per-month-ai-health-coach-launches-may-19/
- Google: actualizaciones de Google Health y Fitbit Air: https://blog.google/products-and-platforms/products/google-health/fitbit-google-health-updates/ · Google Health Coach (blog oficial): https://blog.google/products-and-platforms/products/google-health/google-health-coach · países y requisitos: https://support.google.com/googlehealth/answer/14237941?hl=en · Fitbit Air y app Google Health (9to5Google, 7-5-2026): https://9to5google.com/2026/05/07/google-health-app-fitbit/ (corregido tras QA 2026-11-19)
- Google Store, Google Health Premium: https://store.google.com/us/product/fitbit_premium?hl=en-US
- Google Personal Intelligence (enero de 2026): https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence · expansión fuera de EE. UU. salvo Europa (9to5Google, 14-4-2026): https://9to5google.com/2026/04/14/gemini-personal-intelligence-global/ (corregido tras QA 2026-11-19)
- Apple recorta Mulberry (Gigazine, febrero de 2026): https://gigazine.net/gsc_news/en/20260206-apple-project-muberry-scaled-back
- Apple: rediseño de Salud (9to5Mac, 29-8-2026): https://9to5mac.com/2026/08/29/apple-health-revamp-ai-coach-new-apple-watch-next-month/
- Beta de iOS 27.2 con la app Salud (MacRumors, 16-9-2026): https://macrumors.com/2026/09/16/ios-27-2-beta-health-app (rumor no confirmado; los informes posteriores retrasan estas funciones en el ciclo de iOS 27: https://www.macworld.com/article/3055235/) (corregido tras QA 2026-11-19)
- Garmin Connect+ (the5krunner, abril de 2026): https://the5krunner.com/2026/04/20/garmin-connect-plus-review/ · TechRadar: https://www.techradar.com/health-fitness/garmin-adds-premium-garmin-connect-tier-with-ai-features-but-promises-your-free-experience-is-not-going-away · pausa del programa de desarrolladores (the5krunner, 14-9-2026): https://the5krunner.com/2026/09/14/garmin-developer-api-access-paused/ (corregido tras QA 2026-11-19)
- Samsung Health (nota oficial, 4-6-2026): https://samsungmobilepress.com/articles/galaxy-watch-ai-health-features
- Samsung Health Assistant beta (eWeek): https://www.eweek.com/news/samsung-health-assistant-beta/
- Ultrahuman Ring PRO y Jade (FutureFive): https://futurefive.co.nz/story/ultrahuman-unveils-ring-pro-jade-ai-health-coach
- Rise Science: https://www.risescience.com/blog/rise-app-review · precios (App Store): https://apps.apple.com/us/app/rise-sleep-tracker/id1453884781 · calendario: https://help.risescience.com/hc/en-us/articles/40610919159575-How-does-RISE-Calendar-Integration-work (corregido tras QA 2026-11-19)
- Lifestack (App Store): https://apps.apple.com/app/id6473464429 · precio (blog de Saner.ai): https://blog.saner.ai/lifestack-review/ (corregido tras QA 2026-11-19)

**Calendario y productividad**
- Precios de Reclaim.ai: https://reclaim.ai/pricing
- Cierre de Clockwise (blog de Reclaim, 2026): https://reclaim.ai/blog/clockwise-shutdown-news · aviso oficial: https://www.getclockwise.com/ (corregido tras QA 2026-11-19)
- Precios de Motion: https://www.usemotion.com/pricing · ronda de 60 M$ (Business Wire, 2025): https://www.businesswire.com/news/home/20250905188051/en/Motion-Raises-$60M-at-$550M-Valuation-to-Build-the-Agentic-Work-Suite-for-Businesses
- Precios de Sunsama: https://www.sunsama.com/pricing
- Precios de Akiflow: https://akiflow.com/pricing
- Precios de Morgen: https://www.morgen.so/pricing
- Amie (MakerStack, 2026): https://makerstack.co/reviews/amie-review/ · precios: https://amie.so/pricing (corregido tras QA 2026-11-19)
- Precios de Timing: https://timingapp.com/pricing

**Coaching con IA**
- Serie B de Valence (Built In, 2025): https://builtin.com/articles/valence-raises-series-b-20250926 · https://www.valence.co/blog/series-b-press-release
- BetterUp AI Coaching (2025): https://www.betterup.com/press/betterup-launches-ai-coaching · planes individuales: https://support.betterup.com/hc/en-us/articles/5023276679835
- CoachHub AIMY: https://www.coachhub.com/news-media/coachhub-unveils-ai-coach-aimy · AIMY 2.0: https://www.coachhub.com/news-media/coachhub-launches-ai-coach-aimy-2
- Rocky.ai, precios para empresas: https://help.rocky.ai/rocky-for-creators/business-pricing-packages
- Rosebud, semilla de 6 M$ (TechCrunch, 2025): https://techcrunch.com/2025/06/04/rosebud-lands-6m-to-scale-its-interactive-ai-journaling-app
- Reseña de Rosebud 2026: https://blog.mylifenote.ai/rosebud-review/ · reseña de Mindsera: https://blog.mylifenote.ai/mindsera-review/
- Ama: https://www.producthunt.com/products/ama-4/launches · Founder Coach: https://www.producthunt.com/products/founder-coach/launches · Whenever: fuente original retirada (chatgate.ai da 404) (corregido tras QA 2026-11-19)
- GrowthMentor sobre coaches de negocio con IA: https://www.growthmentor.com/blog/ai-business-coach

**MCP de salud, hábitos y coaching**
- athletedata en el directorio de Claude: https://claude.com/marketplace/connectors/athletedata
- Wellness Project en el directorio de Claude (2-10-2026): https://wellnessproject.ai/press/claude-directory
- Delx Wellness: https://github.com/davidmosiah/delx-wellness · Garmin MCP: https://glama.ai/mcp/servers/davidmosiah/garmin-mcp · API de GitHub: https://api.github.com/repos/davidmosiah/delx-wellness (corregido tras QA 2026-11-19)
- Open Wearables: https://github.com/the-momentum/open-wearables · documentación del MCP: https://openwearables.io/docs/mcp-server/index
- Apple Health MCP (Momentum): https://github.com/the-momentum/apple-health-mcp-server
- garmin_mcp: https://github.com/Taxuspt/garmin_mcp
- totem (WHOOP): https://github.com/thebriangao/totem
- oura-ring-mcp: https://github.com/mitchhankins01/oura-ring-mcp · whoop-mcp: https://github.com/JedPattersonn/whoop-mcp
- private-journal-mcp: https://github.com/obra/private-journal-mcp
- Linell/coach: https://github.com/Linell/coach
- wellness_planner: https://glama.ai/mcp/servers/rwking/wellness_planner/tools/propose_schedule
- Integraciones de LifeWheel: https://lifewheel.us/integrations/
- Litak: https://mcpservers.org/servers/litak-io
- Censo de MCP (Skillselion, agosto de 2026): https://skillselion.com/research/mcp-server-census-2026-08 · estadísticas de eseospace: https://eseospace.com/blog/mcp-statistics/
- Censo de MCP 2026 (agentndx): https://agentndx-web.pages.dev/blog/how-many-mcp-servers-exist-census-2026 · directorio de conectores de Claude (dirjournal): https://www.dirjournal.com/blogs/claude-connectors-list (corregido tras QA 2026-11-19)

**Plataformas de IA y agentes personales**
- Claude for Healthcare y Apple Health (Fortune, 11-1-2026): https://fortune.com/2026/01/11/anthropic-unveils-claude-for-healthcare-and-expands-life-science-features-partners-with-healthex-to-let-users-connect-medical-records/ · anuncio oficial de Anthropic: https://www.anthropic.com/news/healthcare-life-sciences (corregido tras QA 2026-11-19)
- Claude en iPhone con Apple Health (MacTrast, 2026): https://www.mactrast.com/2026/01/claude-ai-iphone-app-gains-apple-health-integration-in-the-us/
- Tareas programadas de Claude Cowork (ayuda oficial): https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork · ejecución remota y MCP locales: https://support.claude.com/en/articles/15811196-what-to-expect-with-remote-execution-in-claude-cowork (corregido tras QA 2026-11-19)
- Claude Duet (9to5Mac, 21-10-2026): https://9to5mac.com/2026/10/21/anthropic-takes-on-chatgpt-dots-and-meta-muse-with-claude-duet/ · 9to5Google: https://9to5google.com/2026/10/21/claude-duet-anthropic-ai-agent-waitlist · artículo oficial: https://www.claude.com/resources/articles/claude-duet (corregido tras QA 2026-11-19)
- Memoria de Claude en el plan gratuito (2026): https://uravation.com/media/claude-memory-free-projects-artifacts-2026/ · fecha (9to5Mac, 2-3-2026): https://9to5mac.com/2026/03/02/free-claude-users-can-now-use-memory-and-import-context-from-rivals/ (corregido tras QA 2026-11-19)
- ChatGPT Health y Apple Health (9to5Mac, 7-1-2026): https://9to5mac.com/2026/01/07/apple-health-integration-launches-in-new-chatgpt-health-feature · MacRumors: https://macrumors.com/2026/01/07/openai-chatgpt-health-apple-health-integration/
- ChatGPT Health excluye la UE (trendingtopics): https://www.trendingtopics.eu/chatgpt-will-gesundheitsdaten-von-apple-health-und-co-vorerst-nicht-in-der-eu/ · Notebookcheck: https://www.notebookcheck.net/ChatGPT-now-reads-health-data-just-not-in-Germany.1350736.0.html · doctors.net.uk: https://www.doctors.net.uk/news/chatgpt-health-regulatory-hurdles-delay-rollout-across-uk-and-europe (corregido tras QA 2026-11-19)
- ChatGPT Pulse (Tom's Guide, 2025): https://www.tomsguide.com/ai/chatgpt-pulse-is-here-now-ai-starts-the-chat-and-curates-your-feed · retirada de Pulse y hub de tareas programadas (Engadget, 2026): https://engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks (corregido tras QA 2026-11-19)
- ChatGPT dots (SiliconANGLE, 29-9-2026): https://siliconangle.com/2026/09/29/openai-launches-dots-always-on-ai-agents-in-chatgpt-with-their-own-cloud-computers/ · OpenAI: https://openai.com/index/introducing-dots/ · Digital Trends: https://www.digitaltrends.com/computing/openais-dots-push-ai-beyond-chatbots-with-always-on-agents-that-can-investigate-build-and-act-across-4000-apps/ (corregido tras QA 2026-11-19)
- Fichaje de Steinberger por OpenAI (Fortune, 15-2-2026): https://fortune.com/2026/02/15/openai-openclaw-ai-agent-developer-peter-steinberg-moltbot-clawdbot-moltbook/ · blog de Steinberger: https://steipete.me/posts/2026/openclaw · Engadget: https://www.engadget.com/ai/openai-has-hired-the-developer-behind-ai-agent-openclaw-092934041.html
- Seguridad de OpenClaw (eSecurity Planet, 2026): https://www.esecurityplanet.com/threats/over-41-of-popular-openclaw-skills-found-to-contain-security-vulnerabilities/ · Adversa: https://adversa.ai/blog/openclaw-security-101-vulnerabilities-hardening-2026/ · ClawHavoc y CVE (Bitdoze): https://www.bitdoze.com/openclaw-security-guide/ (corregido tras QA 2026-11-19)
- OpenClaw en GitHub: https://github.com/openclaw/openclaw · Hermes Agent: https://github.com/NousResearch/hermes-agent · https://www.vellum.ai/md/blog/official-hermes-agent-breakdown

**Tamaño de mercado**
- Cita de Virtue en un blog secundario: https://lifecoachtraining.pages.dev/blog/life-coaching-trends-2026/
- Página del informe de Virtue (sin cifra pública): https://virtuemarketresearch.com/report/ai-coaching-tools-market
- ICF Global Coaching Study 2025: https://coachingfederation.org/blog/coaching-industry-continues-global-growth-with-5-34-billion-usd-revenue-new-research-reveals/
- Stratistics, coaches de salud con IA: https://www.marketresearch.com/Stratistics-Market-Research-Consulting-v4058/AI-Health-Coaches-Forecasts-Global-42340076
- Precedence, coaching de salud y bienestar: https://precedenceresearch.com/health-and-wellness-coaching-market
- Stratistics, coaching de carrera con IA: https://marketpublishers.com/report/data-cloud-ai/artificial-intelligence-n-machine-learning/ai-career-coaching-platforms-market-strat.html

---

## 8. Pendiente y dudas abiertas

- **Sin verificar (se agotó el cupo de búsqueda):** Stoic, Reflectly, Ahead, Bunch, Tenor, Bevel, Welltory, y la oferta y suscripción actuales de Ultrahuman. Ninguno parece cruzar agenda y cuerpo, pero conviene confirmarlo.
- **Para la línea 4:** las tareas programadas y las sesiones remotas de Claude no llegan a un MCP local por stdio salvo con la app de escritorio abierta y conectada, y ChatGPT solo admite MCP remotos o su «Secure MCP Tunnel». Queda por decidir cuál de los caminos de P0-4 se adopta para el brief automático (corregido tras QA 2026-11-19).
- **Para la línea 5:** por qué ChatGPT Health excluye el EEE (¿MDR, AI Act, RGPD art. 9?) y si el mismo razonamiento afecta a Ucoach.
- **Por confirmar:** el precio real de athletedata; si el Personal Data Engine de Samsung ya usa la agenda. Gemini Personal Intelligence no conecta Google Health, y ChatGPT Pulse se retiró el 17-6-2026 (corregido tras QA 2026-11-19).
