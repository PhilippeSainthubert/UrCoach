# QA · Mapa de afirmaciones (informes 01 y 06)

**No compartir con el verificador.** Cada id corresponde a una pregunta de `A-preguntas.md`. Líneas según `cat -n` de los informes a 2026-11-19. Capa: **P** portante, **A** apoyo.

## Informe 01 · `01-mercado-competencia.md`

| id | capa | lo que dice el informe (cita breve) | línea | fuente que cita el informe |
|---|---|---|---|---|
| A01-01 | P | Lifestack planifica en Google Calendar u Outlook según energía estimada con Oura, WHOOP, Garmin, Apple Health (y Fitbit); 4,99–9,99 $/mes o 35–50 $/año; «AI Planner for ADHD»; 4,4★ (73 valoraciones); también Todoist y Trello | 15, 22, 42 | App Store, nov. 2026 (`verified`) |
| A01-02 | P | Rise: curva horaria de energía desde la deuda de sueño; exporta la curva al calendario; 69,99 $/año | 15, 22, 41 | risescience.com, «verificado el 18-8-2026» pero etiquetado `reported` |
| A01-03 | P | athletedata (HealthspanOS AG), «Anthropic verified», lee 39 fuentes (tabla: Garmin, WHOOP, Oura, Apple Health, Withings «y unas 29 más»), escribe entrenos en Google Calendar; añadido en sept. 2026; suscripción sin precio publicado | 15, 77 | claude.com/marketplace/connectors/athletedata (`verified`) |
| A01-04 | P | Claude lee Apple Health desde ene. 2026; Apple Health y Health Connect en beta; HealthEx y Function; solo EE. UU., Pro y Max; conversaciones de salud ni entrenan ni van a la memoria | 16, 17, 97, 175 | Fortune 11-1-2026; MacTrast (`reported`) |
| A01-05 | P | ChatGPT Health anunciado 7-1-2026, despliegue en EE. UU. 23-7-2026; Apple Health, historial médico, MyFitnessPal, Function; excluye EEE, Suiza y Reino Unido | 16, 17, 101 | 9to5Mac, MacRumors, trendingtopics.eu (`reported`) |
| A01-06 | P | «ChatGPT Health excluye el EEE por el riesgo de que se considere software sanitario de alto riesgo» | 174 | sin fuente concreta (`reported`); la línea 336 lo deja como duda abierta |
| A01-07 | P | ChatGPT Dots: agentes siempre activos con ordenador en la nube, +4.000 apps, investigación proactiva en solo lectura; Pro y Business Premium desde 29-9-2026 (DevDay) | 16, 20, 103 | SiliconANGLE, TechRadar (`reported`); openai.com/ro-RO/index/introducing-dots |
| A01-08 | P | Claude Duet: agente proactivo en VM en la nube, brief matinal de correo y calendario, pide permiso antes de enviar/pagar/borrar; lista de espera, EE. UU., Pro y Max, desde 21-10-2026, sin coste extra | 16, 20, 99 | 9to5Mac 21-10-2026; 9to5Google; «ayuda de Claude» (`reported`) |
| A01-09 | P | Tareas programadas de Cowork «se ejecutan en remoto, también con el ordenador apagado»; «Require this computer» solo para organizaciones con Computer access; todos los planes de pago | 20, 98 | support.claude.com, art. 13854387 (`verified`) |
| A01-10 | P | Un servidor stdio en el portátil «probablemente no es accesible» desde tareas remotas, Duet o Dots | 20, 179, 190 | `inferred`, remitido a la línea 4 |
| A01-11 | P | Claude y ChatGPT «tienen calendario, memoria y tareas programadas» | 16 | sin fuente explícita en la frase |
| A01-12 | P | Página de Virtue: VMR-18060, febrero de 2025, previsión 2025-2031, 4.250 $, no muestra la cifra | 21, 114 | virtuemarketresearch.com/report/ai-coaching-tools-market (`verified`) |
| A01-13 | P | Los 5.800 M$ «a finales de 2026» solo aparecen en un blog de certificación de coaches con enlaces de afiliado | 21, 114 | lifecoachtraining.pages.dev |
| A01-14 | P | «No he encontrado ninguno de código abierto que junte agenda, sueño, hábitos, ergonomía y un método explícito»; «Nadie lo ofrece de forma abierta, explícita y auditable» | 18, 166, 200 | búsqueda propia (negativo) |
| A01-15 | P | Linell/coach: MIT, 3★, sin actividad desde 6-2025; objetivos, tareas, notas, guía diaria | 18, 88 | API de GitHub (`verified`) |
| A01-16 | P | garmin_mcp: MIT, 1.525★, activo en oct. 2026 | 18, 80, 177 | API de GitHub (`verified`) |
| A01-17 | P | Open Wearables: MIT, 2.805★, activo el 19-11-2026; Oura, Garmin, WHOOP, Apple Health, Polar, Suunto, Samsung, Strava, Health Connect; MCP en beta | 18, 81, 177 | API de GitHub; openwearables.io (`verified`) |
| A01-18 | P | Delx Wellness: registro MIT local-first; WHOOP, Oura, Garmin, Strava, Fitbit, Withings, Apple Health, Polar; `daily_summary`, `weekly_summary`, `wellness_context` «handoff para motores de recomendación»; perfil para Hermes; 28★, activo nov. 2026 | 18, 79, 177, 242 | github.com/davidmosiah/delx-wellness (`verified`) |
| A01-19 | P | LifeWheel: MCP hospedado, 21 herramientas, ChatGPT (Apps SDK), Claude, Cursor; conector gratis, app freemium | 18, 86, 209 | lifewheel.us (`verified`) |
| A01-20 | P | Wellness Project: conector comunitario del directorio de Claude, 15 herramientas, Basic gratis, Pro 9,99 $ (4,99 en promoción); nota 2-10-2026 | 78, 194, 209 | wellnessproject.ai/press (`verified`) |
| A01-21 | P | Oura 5,99 $/mes o 69,99 $/año; Advisor incluido | 22, 35 | recurdash, hometechnologyreview (`reported`) |
| A01-22 | P | Garmin Connect+ 6,99 $/mes o 69,99 $/año; mensajes de IA; «las reseñas la consideran pobre» | 22, 38 | TechRadar mar. 2025; the5krunner 20-4-2026 (`reported`) |
| A01-23 | P | Google Health Coach, antes Fitbit AI Coach; vista previa desde oct. 2025; GA 19-5-2026; 9,99 $/mes o 99 $/año; gratis con Google AI Pro y Ultra | 22, 36, 117, 195 | TechCrunch 7-5-2026 (`reported`); blog de Google 12-10-2026 (`verified`) |
| A01-24 | P | WHOOP One 199 $, Peak 239 $, Life 359 $/año; coach incluido | 22, 34, 116 | trackervs (`reported`) |
| A01-25 | P | Rosebud Bloom 12,99 $/mes o 107,99 $/año; sin plan gratis desde 30-9-2026 «según un competidor» | 22, 65 | mylifenote (`reported`) |
| A01-26 | P | WHOOP: mayo de 2026, «My Memory» y check-ins proactivos; agenda «No nativa: el usuario cuenta sus eventos» | 34, 176, 191 | Business Wire 8-5-2026 (`reported`) |
| A01-27 | P | «Los wearables no ven el trabajo… Ninguno lee el calendario»; columna Agenda = No para Oura, Google, Garmin, Samsung, Ultrahuman, Apple | 34-40, 176 | tablas 2.1, sin fuente específica para la negativa |
| A01-28 | P | Altman lo anunció en X el 15-2-2026; Steinberger lo publicó el día antes; OpenAI no compró OpenClaw, pasa a fundación independiente con apoyo de OpenAI | 115, 219 | Fortune, Engadget, Gizmodo, steipete.me (`reported`) |
| A01-29 | P | Clockwise cerró el 27-3-2026 (anunciado el 19-3-2026); Reclaim recomendado como alternativa | 50, 120 | blog de Reclaim (`reported`, fuente interesada) |
| A01-30 | P | Reclaim.ai «(de Dropbox)»; conector MCP para Claude y Claude Code, Copilot y ChatGPT; no conoce sueño ni energía | 48, 119, 234 | reclaim.ai/pricing (`verified`) |
| A01-31 | P | Sunsama: MCP incluido en Pro; Akiflow: conector MCP alojado en Pro; Timing: MCP en plan Connect; Morgen sin mención de MCP en tabla pero incluido en la taxonomía «(con MCP)» | 51-55, 152, 163 | páginas de precios (`verified`) |
| A01-32 | P | «la API de salud de Garmin exige licencia de socio según Delx» | 221 | Delx (`reported`) |
| A01-33 | P | «Un emprendedor español no puede hoy pedir a su IA un plan con sus datos de sueño sin una pieza como Ucoach» | 17 | inferencia a partir de A01-04/05; no comprueba Google ni wearables en España |
| A01-34 | P | Personal Intelligence conecta Gemini con apps de Google (ene. 2026); «No he encontrado prueba de que Gemini cruce Calendar con datos de Google Health» | 104, 337 | blog de Google 14-1-2026 (`reported`) |
| A01-35 | P | ChatGPT Health y Claude «se quedan en explicar, resumir y preparar preguntas para el médico» | 174 | `reported`, sin fuente concreta |
| A01-36 | A | Health+ recortado en feb. 2026; beta de iOS 27.2 en sept. 2026 con Insights, Readiness 0-10, Personal Guidance, Health Age; análisis Quest 119 $ | 37 | Gigazine 6-2-2026; 9to5Mac 29-8-2026; MacRumors 16-9-2026 (`reported`) |
| A01-37 | A | Samsung: Energy Score, Vitals, Heart Health Score, Daily Cardio Load; Health Assistant beta desde 21-7-2026 «posiblemente con Gemini» | 39 | Samsung Mobile Press 4-6-2026 (`verified`); eWeek (`reported`) |
| A01-38 | A | Ultrahuman Jade «biointeligencia», modos Standard y Deep Research; sin suscripción obligatoria; Ring PRO 479 $ a 499 € | 40 | FutureFive/IT Brief (`reported`, contradictorio) |
| A01-39 | A | Oura Advisor a todos 31-3-2025; LLM de salud femenina abril 2026; derivación clínica con Counsel junio 2026 | 35, 118 | Business Wire 2025; the5krunner 24-2-2026 (`reported`) |
| A01-40 | A | Google: memoria mejorada (oct. 2026), «Fitbit Air»; fuentes Fitbit, Pixel Watch, Apple Health, MyFitnessPal, Function, Lingo | 36, 258 | blog de Google 12-10-2026 (`verified`) |
| A01-41 | A | WHOOP ofrece clínicos por vídeo en EE. UU. | 34 | Business Wire 8-5-2026 (`reported`) |
| A01-42 | A | Motion pasó a «AI Employees»; ronda de 60 M$ a 550 M$ de valoración (sept. 2025); Pro AI 19 $, Business AI 29 $ | 49, 120 | usemotion.com (`verified`); Business Wire 5-9-2025 |
| A01-43 | A | Reclaim: Lite gratis; Starter 10–12 $; Business 15–18 $; Enterprise 22 $ | 48 | reclaim.ai/pricing (`verified`) |
| A01-44 | A | Sunsama 17/22 $; Akiflow 19/34 $; Morgen 15/30 $; Timing Professional 10 $/mes, Connect 168 $/año | 51-55 | páginas de precios (`verified`) |
| A01-45 | A | Amie 8–20 $/mes (contradictorio); ~8,3 M$ captados | 54 | Toolradar, MakerStack (`reported`) |
| A01-46 | A | Valence/Nadia en Delta, Experian, Kraft Heinz; Serie B 50 M$ liderada por Bessemer (sept. 2025); ~75 M$ total | 61 | Built In 26-9-2025; nota de Valence (`reported`) |
| A01-47 | A | BetterUp AI Coaching lanzado el 21-1-2025; «indicios no confirmados de salida del B2C en 2026»; 3.000–5.000 $/usuario/año | 62 | nota de BetterUp (`verified` vía buscador); risely.me |
| A01-48 | A | AIMY febrero de 2025; AIMY 2.0 cinco meses después | 63 | coachhub.com (`reported`) |
| A01-49 | A | Rocky.ai 10–30 $/mes consumidor; 99–199 $/mes empresa; marca blanca | 64 | agregadores (`reported`) |
| A01-50 | A | Rosebud semilla 6 M$ (Bessemer, junio 2025); sin plan gratis desde 30-9-2026 | 65 | TechCrunch 4-6-2025; mylifenote |
| A01-51 | A | Mindsera ~14,99 $/mes o 129 $/año | 66 | mylifenote (`reported`) |
| A01-52 | A | Ama, «primer coach de IA proactivo para emprendedores», lanzado 10-12-2025; Founder Coach 12-2-2026 | 67, 69 | Product Hunt (`reported`) |
| A01-53 | A | apple-health-mcp-server 288★ (julio 2026); private-journal-mcp 474★ (nov. 2026) | 18, 82, 85 | API de GitHub (`verified`) |
| A01-54 | A | totem: API privada por ingeniería inversa, 55 herramientas, 144★, sept. 2026 | 83 | GitHub (`verified`) |
| A01-55 | A | ~26.500 servidores (sept. 2026), ~30.700 (oct. 2026); directorio de Claude >300 en junio de 2026; dev.to >40 MCP de fitness | 91 | Skillselion, eseospace, dev.to (`reported`) |
| A01-56 | A | Memoria de Claude abierta al plan gratuito en marzo o abril de 2026 | 100 | uravation (`reported`) |
| A01-57 | A | Pulse: Pro desde sept. 2025, Gmail y Calendar opcionales; llegada a Plus no confirmada | 102, 337 | Tom's Guide (`reported`) |
| A01-58 | A | OpenClaw MIT, 394.783★, fundación con apoyo de OpenAI | 105 | API de GitHub 19-11-2026 (`verified`) |
| A01-59 | A | Hermes Agent (Nous Research): MIT, 264.581★, desde feb. 2026, memoria en `~/.hermes`, Telegram, WhatsApp, Slack | 106 | API de GitHub (`verified`); vellum.ai |
| A01-60 | A | OpenClaw: 341–386 skills maliciosas en ClawHub, CVE-2026-25253 | 196 | eSecurity Planet, Adversa (índice de fuentes) |
| A01-61 | A | ICF 2025: 5.340 M$ de ingresos, 122.974 coaches, elaborado por PwC | 130 | coachingfederation.org |
| A01-62 | A | Stratistics: 1.500 M$ (2025) → 8.800 M$ (2032), TACC 27,9 % | 131 | marketresearch.com |
| A01-63 | A | Salud y bienestar 16.500–22.000 M$ (2025); carrera con IA 3.700 M$ (2026) | 132-133 | Precedence, Business Research Co., Fortune BI; Stratistics |
| A01-64 | A | GrowthMentor recomienda «ChatGPT o Claude con rol de coach y tu contexto real» | 193 | growthmentor.com |

## Informe 06 · `06-negocio-gtm.md`

| id | capa | lo que dice el informe (cita breve) | línea | fuente que cita el informe |
|---|---|---|---|---|
| A06-01 | P | «Más del 95 % de los servidores MCP no ingresan nada, y menos del 0,5 % pasa de 1.000 $/mes» (feb. 2026) | 13, 60, 214 | N. Fainstein, dev.to (`reported`, autor con interés comercial) |
| A06-02 | P | «No he encontrado ningún MCP de consumo con ingresos públicos» | 13, 60 | búsqueda propia (negativo) |
| A06-03 | P | «OpenAI solo aprueba el pago externo para bienes físicos»; checkout integrado en beta privada para marketplaces; en ene. 2026 sin compras ni suscripciones | 13, 54 | Apps SDK Monetization (`verified`); foro de OpenAI ene. 2026 (`reported`) |
| A06-04 | P | «Ninguna fuente describe listados de pago» en el directorio de Claude; «Los directorios de ChatGPT y Claude no permiten vender suscripciones digitales dentro del chat» | 13, 55 | `reported` |
| A06-05 | P | MCPize: «los editores se quedan el 80 %», +450 desarrolladores, 900–1.200 servidores; otros se quedan entre el 15 y el 18 %; Apify mayor caso comercial | 52 | mcpize.com (`verified` el 80 %); resto `reported` |
| A06-06 | P | Marketplaces sirven para servidores remotos con clave; uno local por stdio «no se puede medir ni cobrar por llamada» | 13, 52 | razonamiento propio |
| A06-07 | P | Oura 5,99 €/mes o 69,99 €/año (EE. UU. 5,99 $/69,99 $); +50 métricas; Advisor incluido; primer mes gratis | 14, 28 | ouraring.com/membership (`verified`) |
| A06-08 | P | Rise ~69,99 $/año (~5,8 $/mes); también plan mensual y pago único en promociones | 14, 31 | ayuda de Rise, App Store, Tom's Guide (`reported`) |
| A06-09 | P | Google Health Premium 9,99 $/mes o 99 $/año, incluido sin coste en Google AI Pro y Ultra (mayo 2026); 37 países | 14, 15, 30, 72, 190 | sensai.fit, Android Authority (`reported`) |
| A06-10 | P | Rosebud 12,99 $/mes o 107,99 $/año | 14, 35 | Life Note, App Store (`reported`) |
| A06-11 | P | Reclaim Starter 10 $ (anual) o 12 $ (mensual); Business 15/18; Enterprise 22 | 14, 32 | reclaim.ai/pricing (`verified`) |
| A06-12 | P | Claude: Apple Health y Health Connect, beta, Pro y Max, solo EE. UU., ene. 2026; «detecta patrones»; no entrena y excluye de la memoria | 15, 68 | anthropic.com/news/healthcare-life-sciences (`verified`) |
| A06-13 | P | ChatGPT Health 7-1-2026; el 23-7-2026 «Health in ChatGPT» para mayores de 18 en EE. UU. (web e iOS); 230 M de personas a la semana | 15, 70 | Fortune; Digital Trends (`verified`) |
| A06-14 | P | Pulse desde sept. 2025, Google Calendar opcional, empezó en Pro | 15, 71 | Tom's Guide (`reported`) |
| A06-15 | P | «Claude Pro incluye tareas programadas»; «Permite programar el brief de mañana sin cron» | 15, 36, 69, 190 | claude.com/pricing (`verified`); Planoly sept. 2026 |
| A06-16 | P | Integraciones de salud «siguen siendo solo para EE. UU.» (Claude y ChatGPT); ventana europea | 15, 75, 193 | `verified` para Claude y ChatGPT |
| A06-17 | P | «Lo que ninguna ha lanzado es un método que cruce el trabajo y el cuerpo»; «Qué no han hecho: cruzar la agenda de trabajo con el cuerpo» | 15, 75 | `inferred`; no menciona Duet ni Dots |
| A06-18 | P | ~175 $/mes por una sesión mensual, ~350 $/mes por 2-5; sesión suelta ~140 $; paquete ejecutivo 1.250 $; negocio 1.000 $; 23.000 ventas de 1.529 coaches; oct. 2026 | 16, 40, 191 | paperbell.com (`verified`) |
| A06-19 | P | Coachvox ~99 $/mes al coach; los creadores cobran 10–100 £/mes | 16, 37 | ayuda de Coachvox (`reported`) |
| A06-20 | P | Future 199 $/mes o 149 $ con pago anual; Trainwell 149 $/mes | 17, 38, 39 | sensai.fit, trainwell.net (`reported`) |
| A06-21 | P | Sean Ellis «pide unas 40 respuestas como mínimo»; Superhuman del 22 % al 58 % | 18, 142 | First Round 2018 (`verified`) |
| A06-22 | P | ucoach.com 2004 → Athletics Hub; ucoach.io sept. 2025 (vídeo para federaciones); ucoach.ai jun. 2024 «Launching Soon»; ucoach.app 17-9-2025, vence 17-9-2026; u-coach.com dic. 2025 | 19, 171-175 | whois, curl, RDAP (`verified`) |
| A06-23 | P | App iOS «U-Coach App» (Adrien Chouteau) para entrenadores personales | 19, 177 | App Store (`reported`) |
| A06-24 | P | «las apps de hábitos pierden a la mayoría de usuarios en semanas»; «retención baja de las apps de hábitos» | 90, 107, 192 | sin fuente (posible remisión a línea 3) |
| A06-25 | P | Sincronizar datos de salud convierte a Philippe en responsable de datos de categoría especial (art. 9): evaluación de impacto, cifrado, DPA | 88 | sin fuente (razonamiento legal) |
| A06-26 | P | Con cifrado de extremo a extremo «el peso del RGPD sea menor» | 99 | `inferred` |
| A06-27 | P | Lista → registro 25–85 %, media 50 % si se activa en menos de un mes, <20 % si se espera más de 3 meses; «no tener la lista esperando más de 4 semanas» | 129 | Lenny's Newsletter 2022 (`verified`) |
| A06-28 | P | Coach-in-the-loop «ataca el mayor riesgo del producto, la retención»; «el coach es el motor de retención» | 16, 108, 192 | sin fuente |
| A06-29 | P | EUIPO/OEPM no verificado; «su registro como marca sería débil» | 180, 182 | no verificado (TMview bloqueado) |
| A06-30 | A | WHOOP 199/239/359 $/año; Reino Unido 169/229/349 £; Peak añade Healthspan y estrés; Life ECG y tensión (beta) | 29 | Wareable, T3, trackervs (`reported`) |
| A06-31 | A | Sunsama 17 $ anual / 22 $ mensual; acceso por MCP y Zapier | 33, 57 | sunsama.com/pricing (`verified`) |
| A06-32 | A | Motion Pro AI 19 $, Business AI 29 $ | 34 | usemotion.com/pricing (`verified`) |
| A06-33 | A | Claude Pro 17 $ (anual) o 20 $; Max desde 100 $ | 36 | claude.com/pricing (`verified`) |
| A06-34 | A | ICF 2025: media mundial ~234 $/sesión; Norteamérica ~297 $; C-suite >500 $/h | 41 | nextlevel.coach, noomii (`reported`) |
| A06-35 | A | España: 120–300 € presencial (media 137–250 €), online 40–150 €; «profesión sin regular, de 40 a 500 € la sesión»; índice: «120-500 €/sesión» | 42, 161, 219 | Cronoshare, modelosdeplandenegocios (`reported`) |
| A06-36 | A | Freemium 9–19 $/mes: «0 $ de ingresos todavía», «conversión baja» | 53 | dev.to rumblingb (`reported`) |
| A06-37 | A | Patrocinios: 500–2.000 $/mes | 58 | sin fuente concreta (`reported`) |
| A06-38 | A | «la mayoría de los servidores públicos tienen pocos usuarios o ninguno» | 60 | Pragmatic Engineer 2025 (`reported`) |
| A06-39 | A | «Apify es el mayor caso comercial citado, pero es B2B (scraping)» | 52 | `reported` |
| A06-40 | A | Jasper perdió terreno cuando ChatGPT hizo gratis su función principal (2023) | 77 | conocimiento previo (`reported`, no reverificado) |
| A06-41 | A | Reclaim comprado por Dropbox (2024) | 77 | conocimiento previo (`reported`, no reverificado) |
| A06-42 | A | 2–10 % de visitas frías se apuntan | 129 | LaunchList, mean.ceo (`reported`) |
| A06-43 | A | mcp-use en portada de HN en ago. 2025, asociado a salto de descargas | 132 | Manufact (`reported`, fuente propia) |
| A06-44 | A | Registro oficial de MCP, Smithery, Glama, mcp.so, PulseMCP, awesome-mcp-servers | 132 | sin fuente |
| A06-45 | A | Lanzadera: más de 1.700 empresas aceleradas desde 2013 | 141 | lanzadera.es (`verified`) |
| A06-46 | A | Wayra, Demium o programa de escuela de negocio como piloto | 141, 235 | `inferred` |
| A06-47 | A | «en beneficios para empleados compite con Gympass, ifeel, etc.» | 110 | sin fuente |
| A06-48 | A | YouCoach (fútbol, YouCoach SRL, youcoach.com desde 2005); YourCoach (coaches de salud, Düsseldorf) | 178-179 | App Store (`reported`) |
| A06-49 | A | Buscar en TMview «clases 9, 41, 42 y 44» | 182 | sin fuente |
| A06-50 | A | «.es no tiene RDAP público» | 176 | sin fuente |
| A06-51 | A | Google Health Coach: sueño, actividad, nutrición; historial médico solo en EE. UU. | 30 | sensai.fit, Android Authority (`reported`) |

## Contradicciones, saltos lógicos y huecos

### Señales de posible alucinación (prioridad para cruzar con el verificador)

- **Productos de otoño de 2026 que sostienen tesis enteras:** «ChatGPT Dots» (29-9-2026) y «Claude Duet» (21-10-2026) aparecen solo en 01 y solo con prensa `reported`. Si no existen, caen el resumen 2, la amenaza 1 y parte de la 2. La URL citada para Dots es `openai.com/ro-RO/...` (versión en rumano), algo raro (A01-07, A01-08).
- **iOS 27.2 beta en septiembre de 2026** (01, l. 37 y 263): una beta «.2» suele llegar en octubre o noviembre, no el mismo mes del lanzamiento de la versión mayor. Fechas sospechosas (A01-36).
- **Recuentos de estrellas enormes:** OpenClaw 394.783★ y Hermes Agent 264.581★ «desde febrero de 2026» (A01-58, A01-59). Si Hermes tiene esas estrellas en 9 meses, sería uno de los repositorios de crecimiento más rápido de GitHub.
- **CVE-2026-25253 y «341–386 skills maliciosas»** (A01-60): cifra y CVE concretos, citados solo en el índice de fuentes con titulares que hablan de otra cosa («41 % de skills con vulnerabilidades»).
- **«Fitbit Air»** (l. 258) y la memoria de Google Health de oct. 2026 (A01-40): solo aparecen en el título de una fuente del índice, no en la tabla.
- **Fechas exactas apoyadas en fuentes secundarias o interesadas:** cierre de Clockwise 27-3-2026 (blog de Reclaim), Rosebud sin plan gratis desde 30-9-2026 («según un competidor»), Samsung Health Assistant 21-7-2026.
- **Etiqueta incoherente:** Rise lleva «precio verificado el 18-8-2026» pero etiqueta `reported`; Lifestack lleva `verified` (App Store) y es la pieza central del resumen 1.

### Contradicciones internas en 01

1. **athletedata: 39 frente a 34 fuentes.** El resumen (l. 15) dice que «lee 39 fuentes»; la tabla (l. 77) enumera cinco «y unas 29 fuentes más», es decir, unas 34.
2. **Lifestack:** el resumen (l. 15) lista Oura, WHOOP, Garmin y Apple Health; la tabla (l. 42) añade Fitbit, y Todoist y Trello aparecen como «calendarios». Detalle menor.
3. **«Europa es el hueco» frente a «la capa de datos es un bien común».** El resumen 3 (l. 17) dice que un emprendedor español «no puede hoy pedir a su IA un plan con sus datos de sueño sin una pieza como Ucoach». Pero el resumen 5 y la tabla 2.4 describen MCP de datos MIT (garmin_mcp, Open Wearables, Delx) que funcionan con Claude desde cualquier país, más conectores del directorio de Claude (athletedata, Wellness Project) cuyo alcance geográfico no se comprueba. Los coaches de Oura, WHOOP y, quizá, Google tampoco están limitados a EE. UU. La conclusión no se sigue de las premisas.
4. **Morgen «(con MCP)»** en la taxonomía (l. 152) frente a la tabla 2.2, que no le atribuye MCP (l. 53); la capa 2 (l. 163) tampoco lo incluye.
5. **Pro de 5–8 € (P2 10a, l. 239) frente a referencias de 5,99–12,99 $.** El resumen 8 dice que un Pro de 8–15 € «compite con coaches incluidos», pero el informe no razona por qué 5–8 € resolvería eso.
6. **Amenaza 1: «el 70 % de Ucoach»** (l. 189) es una cifra sin cálculo ni fuente.
7. **Etiquetas:** Claude Health va como `reported` en 01 (l. 97), mientras 06 la da como `verified` con la nota oficial de Anthropic.

### Contradicciones internas en 06

1. **«En esa franja» de 8–15 €** (l. 14): Oura (5,99 €) y Rise (~5,8 $) quedan por debajo de la franja que se dice defender.
2. **«Ninguna ha lanzado… una versión para la UE: las integraciones de salud son solo para EE. UU.»** (l. 15) frente a Google Health Coach en «37 países» (l. 30, 72). Si entre esos 37 hay países de la UE (España incluida), la «ventana europea» de la l. 193 se debilita. El propio informe deja «disponibilidad en la UE de Google Health Coach» como pendiente (l. 235), pero el resumen la da por cerrada.
3. **H2 frente a criterios de decisión.** H2 (l. 122) pide que pague «al menos el 25 % de los usuarios activos», unas 5 personas de 20. El criterio de «seguir» (l. 148) pide ≥10 plazas, y «pivotar» empieza por debajo de 5: cumplir H2 deja el resultado en zona gris.
4. **Lista de espera frente a su propia conclusión.** La l. 129 concluye «no tener la lista esperando más de 4 semanas», pero la landing se abre en las semanas 1–4 (20 nov.–17 dic.) y la cohorte de pago empieza el 2 de febrero: entre 7 y 10 semanas de espera. La landing promete además la «cohorte de enero» (l. 129) y la cohorte empieza el 2 de febrero (l. 139).
5. **Calendario frente a criterios:** la cohorte empieza el 2-2-2027 y dura 30 días, así que el 18-2-2027 no se puede medir su resultado. Solo se mide la venta. El piloto de coaches («un mes gratis» y luego renovar) solo da datos de renovación el 18-2 si arranca antes del 18 de enero.
6. **Precios de coaching en España:** 120–300 € (presencial) y 40–150 € (online) en la l. 42, «de 40 a 500 €» en la l. 161 y «120-500 €/sesión» en el índice (l. 219).
7. **Pago dentro de ChatGPT:** se presenta como hecho vigente y `verified` (l. 13), pero se apoya en documentación y un foro de enero de 2026, y el propio informe lo deja pendiente («si OpenAI ha abierto suscripciones digitales… después de enero de 2026», l. 235).
8. **ucoach.app:** «vence el 17 sept. 2026», pero la comprobación es del 19-11-2026, dos meses después. El dato o el comentario del periodo de gracia está desfasado.
9. **«El canal que más rinde… es el coach humano»** (l. 16): no hay ningún dato de rendimiento de canal. Solo hay precios de coaches.

### Contradicciones entre 01 y 06

1. **06 ignora Duet y Dots.** 01 (mismo día) sitúa a Claude Duet y ChatGPT Dots como agentes proactivos con brief matinal sobre el calendario. 06 dice que ninguna plataforma cruza agenda y cuerpo y no los menciona en su tabla de riesgo de plataforma (l. 66-73). Una de las dos visiones está incompleta.
2. **Tareas programadas y servidor local.** 06 (l. 69) dice que las tareas programadas de Claude Pro «permiten programar el brief de mañana sin cron». 01 (l. 20, 98, 179) dice que se ejecutan en remoto y probablemente no llegan a un servidor stdio local, lo que pone en riesgo ese brief. Son conclusiones opuestas sobre la misma función.
3. **¿Ha cruzado alguien agenda y cuerpo?** 01 dice que sí: Lifestack, Rise, athletedata. 06 propone como mensaje central «Ucoach junta las dos cosas» (l. 166) y como categoría «Planificador de energía» (l. 163), que es exactamente el posicionamiento de Lifestack («energy-first planning»). 06 no menciona Lifestack.
4. **Precio del Pro:** 01 propone 5–8 € (l. 239); 06 dice que 8–15 € «se puede defender» (l. 14) y recomienda 8–12 € (l. 99).
5. **Primer B2B2C:** 01 apunta a aceleradoras y fondos de capital riesgo (l. 241) apoyándose en Valence, BetterUp y CoachHub, que venden a grandes empresas, no a aceleradoras. 06 prioriza a los coaches y deja las aceleradoras para la escala.
6. **Monetización de MCP de consumo:** 06 dice que no hay MCP de consumo con ingresos públicos y que los directorios no permiten vender suscripciones. 01 muestra conectores del directorio de Claude con planes de pago fuera del chat (Wellness Project Pro 9,99 $; athletedata con suscripción). No es una contradicción estricta (no hay ingresos públicos), pero 06 debería contar con esos casos.
7. **Oura:** 01 da 5,99 $/mes; 06 da 5,99 €/mes. Compatibles si los precios coinciden en número, pero conviene confirmarlo.

### Conclusiones que no se siguen de sus premisas

- 01, resumen 3 y P0-5: «Abrir con Europa» descansa en que solo las plataformas de IA bloquean la UE. No comprueba la disponibilidad en la UE de Google Health Coach, Oura Advisor, WHOOP Coach, athletedata ni Lifestack.
- 01, «Las plataformas evitan el método por riesgo regulatorio» (l. 174): la causa regulatoria es `reported` sin fuente y la propia l. 336 la deja abierta.
- 06, resumen 5: «se paga 10 veces más cuando hay una persona» se extrapola desde entrenadores de fitness (Future, Trainwell) a coaching de rendimiento para fundadores.
- 06, plan Coach: que el coach pagará 29–59 €/mes se deduce de lo que cobra al cliente (175–350 $), no de ningún dato de disposición a pagar por herramientas. Lo valida H3, pero el resumen lo presenta como hallazgo.
- 06: «Reclaim acabó comprado por Dropbox (2024)» y Jasper vienen de «conocimiento previo, no reverificado».

### Lo que falta

- **Herramientas para coaches con datos del cliente** (competencia directa del plan Coach de 06): plataformas como Paperbell, Practice, CoachAccountable, Simply.Coach, Satori o Delenta, y en salud Healthie, Trainerize o TrueCoach, que ya integran wearables. Ninguno de los dos informes las analiza.
- **Disponibilidad por país** de cada competidor clave en España y la UE (base de la tesis europea).
- **Cálculo de abajo arriba** que 01 recomienda en lugar del TAM: ninguno de los dos lo hace (número de emprendedores hispanohablantes con IA de pago y wearable; número de coaches de fundadores en España).
- **Economía unitaria del plan Coach:** cuántos coaches a 29–59 € hacen falta para que tenga sentido, coste de adquisición de un coach y tiempo de Philippe en las cohortes.
- **Fuente de la retención de apps de hábitos**, que sostiene la tesis central de 06 (l. 90, 192).
- **Riesgo regulatorio de las recomendaciones** (producto sanitario, MDR, AI Act): ambos lo remiten a la línea 5, pero 01 lo usa como argumento de foso y 06 recomienda un plan con recomendaciones de sueño y energía sin matizarlo.
- **Comprobación de marca** (TMview/OEPM) no hecha, aunque 06 recomienda cambiar de nombre.
- **Pendientes declarados por 01:** Stoic, Reflectly, Ahead, Bunch, Tenor, Bevel, Welltory y Ultrahuman. Bevel, en concreto, es una app de salud con IA que podría cruzar datos.
