---
kind: qa-report
target: 01-mercado-competencia.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 9.7
score_before_fix: 0.0
score_limited_by: cobertura
coverage_claims: 64
coverage_verified: 62
independent: true
sources: 104
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 01 · Mercado y competencia

## Nota: 9.7 / 10 · ENTREGABLE (tras corregir)

**Nota antes de corregir: 0.0 / 10 · REHACER.** Tras aplicar las correcciones el 2026-11-19 no queda ningún hallazgo abierto, y la nota la limita solo la cobertura: 34 de 35 portantes y 62 de 64 afirmaciones verificadas. El detalle está en «Re-verificación», al final.

Lo que sigue es el informe original, antes de corregir.

La nota la bajan los hallazgos, no la cobertura. Con lo verificado, el techo sería 9,71, pero las penalizaciones suman 16: 1 crítica (3), 2 bloqueos (4), 4 medias (4) y 20 bajas (5). Solo la crítica y los dos enlaces muertos ya restan 7 puntos.

**Modo**: Deep · **Tipo**: research de mercado · **Fecha**: 2026-11-19
**Independencia**: verificador en contexto separado ✓. No vio ni el informe ni el mapa, solo `qa/A-preguntas.md`. El cruce se hizo con `qa/A-mapa.md` y `qa/A-respuestas.md`.
**Rúbricas**: sin rúbrica de tipo cargada ⚠
**Voz**: no aplica (documento interno de research)

Cálculo: `nota.py --claims 64 --verificadas 62 --portantes 35 --portantes-ok 34 --criticas 1 --medias 4 --bajas 20 --bloqueos 2`

## Cobertura

| | |
|---|---|
| Afirmaciones en el documento | 64 (el preflight contó 63; se usa la extracción, que es mayor) |
| Verificadas con fuente consultada | 62 (97 %) |
| Portantes verificadas | 34 de 35 |
| No verificables | 2 filas completas (A01-13, A01-51) y 8 partes de otras filas |
| Fuentes distintas del verificador | 104 URL |

El verificador no tuvo acceso a openai.com, help.openai.com, whoop.com, businesswire.com (403) ni a news.samsung.com (timeout). En esos casos se apoyó en prensa, y la confianza quedó en MEDIA.

## Veredicto

**Tras corregir: ENTREGABLE** (`PASS`). Ver «Re-verificación».

Antes de corregir: **REHACER** (`MAJOR ISSUES`). Hay una crítica sin resolver: la tesis «Europa es el hueco» se apoya en una afirmación falsa sobre lo que un usuario español puede hacer hoy. Además hay dos enlaces muertos. El resto del informe aguanta muy bien. Casi todas las afirmaciones sobre productos de 2026 que parecían más arriesgadas (Claude Duet, ChatGPT dots, cierre de Clockwise, estrellas de OpenClaw y Hermes, CVE-2026-25253) se confirmaron. La corrección es acotada: reescribir el resumen 3, el hallazgo no obvio y P0-5, cerrar las 4 medias y sustituir los dos enlaces.

## Bloqueos deterministas (preflight)

| Línea | Enlace | Estado | Corrección |
|---|---|---|---|
| 288 | https://chatgate.ai/post/whenever | 404 | El verificador no tiene un sustituto. Hay que buscar la web oficial de Whenever o quitar la fila de la l. 68, que ya se apoya en una «fuente débil». |
| 306 | https://dev.to/grove_chatforest/fitness-wearables-mcp-servers-strava-garmin-whoop-apple-health-oura-ring-fitbit-and-more-a3k | 404 | Quitar «Una reseña de dev.to contaba más de 40 MCP de fitness y wearables» (l. 91), o sustituir la cifra de contexto por el censo https://agentndx-web.pages.dev/blog/how-many-mcp-servers-exist-census-2026, que usó el verificador. |

Aviso fuera de la cuenta: https://help.risescience.com/hc/en-us/articles/4405177615639-RISE-pricing-and-subscriptions (l. 268) dio 404 en el preflight del 06. En el del 01 pasó. Conviene sustituirlo por https://apps.apple.com/us/app/rise-sleep-tracker/id1453884781 (precios) y https://help.risescience.com/hc/en-us/articles/40610919159575-How-does-RISE-Calendar-Integration-work (calendario).

Los ocho enlaces con 403 (Business Wire, whoop.com, openai.com y coachingfederation.org) no bloquean: la fuente existe y la web rechaza a los robots. El de la ICF lo abrió el verificador sin problema.

Placeholders: 0. Fechas relativas: 0. Guiones largos: el preflight encontró 17 y, tras la corrección, quedan **0**, comprobado con grep.

## Contrato de escritura y voz

⚠ **No se pudo comprobar.** de-slop no estaba disponible: el preflight no encontró `contar-pruebas.py` y `G4U_DESLOP_SCRIPT` no está definido. Las cuatro pruebas del contrato no se pasaron. Guiones largos: 0 tras la corrección. No hay hallazgos de VOZ porque es un documento interno sin guía de marca aplicable.

## Hallazgos

### Crítica

**C1 · A01-33 · ERROR · crítica**
- **Dice** (l. 17): «Un emprendedor español no puede hoy pedir a su IA un plan con sus datos de sueño sin una pieza como Ucoach. Es una ventana, no un foso.» Lo mismo sostienen la l. 170 («para usuarios a los que las plataformas no pueden servir con datos de salud: en Europa»), el diferencial 3 (l. 202) y P0-5 (l. 227).
- **Verificación independiente**:
  - **Google Health Coach**, el coach con Gemini, está disponible en España, que es uno de los 37 países de la lista oficial (https://support.google.com/googlehealth/answer/14237941?hl=en). Va incluido sin coste en Google AI Pro y Ultra desde el 19-05-2026 (https://blog.google/products-and-platforms/products/google-health/google-health-coach). Exige Fitbit o Pixel Watch, ser mayor de 18 años y no usa la agenda.
  - **Oura Advisor** funciona en España y en español (https://support.ouraring.com/hc/en-us/articles/41056787356307).
  - **Lo que sí se mantiene:** las integraciones de salud de Claude son solo para EE. UU. (https://www.anthropic.com/news/healthcare-life-sciences). ChatGPT Health excluye el EEE, Suiza y el Reino Unido (https://www.notebookcheck.net/ChatGPT-now-reads-health-data-just-not-in-Germany.1350736.0.html). Gemini Personal Intelligence excluye Europa y no conecta Google Health (https://9to5google.com/2026/04/14/gemini-personal-intelligence-global/).
- **Corrección**:
  - **Resumen 3:** «En España, Claude y ChatGPT no leen datos de salud y Gemini Personal Intelligence no está disponible. El único coach de plataforma con datos de sueño es Google Health Coach, que exige Fitbit o Pixel Watch y no mira la agenda. Para quien lleva Apple Watch, Oura, Garmin o WHOOP, el hueco existe, pero lo cubre a medias el coach de su propio wearable.»
  - **Hallazgo no obvio (l. 170):** cambiar «en Europa» por «usuarios de Claude o ChatGPT en Europa».
  - **Amenazas:** añadir Google Health Coach en España como amenaza que «ya ocurre».
  - **P0-5:** mantener el mensaje «lo que ChatGPT Health y Claude Health todavía no te dan aquí», que es cierto, sin generalizarlo a «las plataformas».

### Medias

**M1 · A01-18 · DISCREPANCY (con PROVENANCE parcial) · media**
- **Dice** (l. 79): Delx expone «`daily_summary`, `weekly_summary` con "next-week plan" y `wellness_context` como "handoff para motores de recomendación"» (`verified`). La l. 177 dice: «Ucoach puede ser ese motor y dejar los datos a otros». La l. 166 dice del método: «Nadie lo ofrece de forma abierta, explícita y auditable».
- **Verificación independiente**: https://api.github.com/repos/davidmosiah/delx-wellness y su README.
  - **Conectores:** 16, incluidos Google Health, Eight Sleep y CGM.
  - **Recomendaciones:** un meta-MCP, `delx-living-body`, con `living_body_daily_brief` y `living_body_ask`, contesta preguntas como «¿entreno fuerte hoy?» con reglas offline.
  - **Perfiles de agente:** `delx-wellness-hermes` y `delx-wellness-openclaw` («Daily Operator»).
  - **`wellness_context`:** no aparece.
- **Corrección**:
  - **Herramientas:** actualizar la lista y quitar `wellness_context` o citar el fichero donde aparece.
  - **Tesis:** reconocer que ya existe una capa abierta de recomendación diaria basada en reglas. Rebajar «Nadie lo ofrece» a lo que de verdad falta. Hay que comprobar si las reglas de Delx citan evidencia y tienen en cuenta el trabajo. Si no lo hacen, la diferencia está ahí.

**M2 · A01-06 · OVERCLAIM · media**
- **Dice** (l. 174): «ChatGPT Health excluye el EEE por el riesgo de que se considere software sanitario de alto riesgo (`reported`)».
- **Verificación independiente**: OpenAI no ha dado ni motivo ni calendario. La prensa lo atribuye en general a la regulación de los datos de salud: art. 9 del RGPD, AI Act y una posible clasificación como producto sanitario en el Reino Unido. Fuentes: https://www.notebookcheck.net/ChatGPT-now-reads-health-data-just-not-in-Germany.1350736.0.html y https://www.doctors.net.uk/news/chatgpt-health-regulatory-hurdles-delay-rollout-across-uk-and-europe.
- **Corrección**: «OpenAI no ha explicado la exclusión. La prensa la atribuye a la regulación de datos de salud (RGPD art. 9, AI Act, producto sanitario).» La prueba «las plataformas evitan el método por riesgo regulatorio» debe ir como `inferred`.

**M3 · A01-57 · STALE · media**
- **Dice** (l. 102): «ChatGPT Pulse | Brief diario proactivo con Gmail y Calendar opcionales | Pro desde septiembre de 2025; llegada a Plus no confirmada en 2026». Pulse aparece también en la capa 4 (l. 165), en la amenaza 1 (l. 189) y en las dudas abiertas (l. 337).
- **Verificación independiente**: OpenAI retiró Pulse el 17-06-2026 y lo sustituyó por tareas programadas con un hub propio, disponible en Go, Plus, Pro, Business y Enterprise (https://engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks).
- **Corrección**: en la tabla 2.5 y en las l. 165 y 189, cambiar Pulse por «tareas programadas de ChatGPT (desde el 17-06-2026, también en Plus)». Quitar la duda de la l. 337.

**M4 · INTERNAL (01 frente a 06) · media**
- **Dice** (l. 239): «Pro sin conectores, con sincronización cifrada [...] a 5-8 €/mes». El 06 dice «Hay un precio de 8 a 15 €/mes que se puede defender» (06, l. 14) y recomienda «Pro individual: 8-12 €/mes» (06, l. 99).
- **Verificación independiente**: es una contradicción entre los dos informes. Las referencias de precio sí se verificaron: Oura 5,99 €, Google Health Premium 9,99 $, Rosebud 12,99 $ y Lifestack unos 7 $ al mes.
- **Corrección**: el 01 debería remitir el precio a la línea 6 y adoptar su rango, o justificar por qué baja a 5-8 €.

### Bajas

**B1 · A01-03 · ERROR (e INTERNAL) · baja**
- **Dice**: «athletedata lee 39 fuentes de wearables» (l. 15), y en la tabla «Garmin, WHOOP, Oura, Apple Health, Withings y unas 29 fuentes más» (l. 77), que suman unas 34.
- **Verificación independiente**: la ficha (https://claude.com/marketplace/connectors/athletedata) da Garmin, WHOOP, Oura, Apple Health y otras 29, unas 33. La documentación dice «28 more».
- **Corrección**: «más de 30 fuentes» en las dos líneas.

**B2 · A01-01 · DISCREPANCY y PROVENANCE · baja**
- **Dice**: «por 5 a 10 $ al mes (`verified`, App Store)» (l. 15) y «4,99-9,99 $/mes o 35-50 $/año» (l. 42; también l. 22 y 192).
- **Verificación independiente**: la App Store (https://itunes.apple.com/lookup?id=6473464429&country=us) confirma la app, las integraciones y 4,4★ con 73 valoraciones, pero no da precios. Según https://blog.saner.ai/lifestack-review/, cuesta 7 $/mes, 50 $/año o 120 $ de por vida.
- **Corrección**: «unos 7 $/mes o 50 $/año (`reported`)». El precio no puede llevar la etiqueta `verified`.

**B3 · A01-31 · ERROR · baja**
- **Dice** (l. 152): «Morgen (con MCP)».
- **Verificación independiente**: https://www.morgen.so/pricing no menciona MCP. Solo hay servidores de la comunidad.
- **Corrección**: quitar «(con MCP)».

**B4 · A01-59 · ERROR con etiqueta `verified` · baja**
- **Dice** (l. 106): «MIT, 264.581★, desde febrero de 2026 | GitHub API (`verified`)».
- **Verificación independiente**: https://api.github.com/repos/NousResearch/hermes-agent indica que el repositorio se creó el 22-07-2025 y tiene 264.590★.
- **Corrección**: «desde julio de 2025».

**B5 · A01-48 · ERROR · baja**
- **Dice** (l. 63): «AIMY 2.0 cinco meses después».
- **Verificación independiente**: AIMY se anunció el 11-02-2025 y AIMY 2.0 el 4-11-2025, nueve meses después (https://www.coachhub.com/news-media/coachhub-launches-ai-coach-aimy-2).
- **Corrección**: «AIMY 2.0 en noviembre de 2025».

**B6 · A01-39 · DISCREPANCY · baja**
- **Dice** (l. 35): «LLM propio de salud femenina (abril de 2026)».
- **Verificación independiente**: se lanzó en febrero de 2026 dentro de Oura Labs y no tiene despliegue general (https://the5krunner.com/2026/02/24/oura-advisor-labs-update-best-womens-health-guidance-grounded-in-your-data-whats-new/). La derivación a Counsel se anunció el 8-06-2026, cuesta 159 $ al año tras la prueba y solo funciona en EE. UU. (https://ouraring.com/blog/counsel-integration-oura-app/).
- **Corrección**: «(febrero de 2026, en Oura Labs)». Añadir que Counsel es de pago.

**B7 · A01-40 · DISCREPANCY · baja**
- **Dice**: «memoria mejorada (octubre de 2026). Fuentes: Fitbit, Pixel Watch, Apple Health, MyFitnessPal, Function, Lingo» (l. 36), y en el índice «Fitbit Air (12-10-2026)» (l. 258).
- **Verificación independiente**: Fitbit Air se anunció el 7-05-2026. Google dice que el coach usará Apple HealthKit y Health Connect «later», y la integración con Lingo está «prevista». El coach exige Fitbit o Pixel Watch. Fuentes: https://9to5google.com/2026/05/07/google-health-app-fitbit/ y https://support.google.com/googlehealth/answer/14237941?hl=en. La mejora de memoria de octubre no se encontró.
- **Corrección**: quitar Apple Health y Lingo como fuentes actuales, añadir «exige Fitbit o Pixel Watch» y revisar la fecha y el título de la fuente de la l. 258.

**B8 · A01-36 · OVERCLAIM · baja**
- **Dice** (l. 37): «La beta de iOS 27.2 (septiembre de 2026) trae Insights con IA, Readiness 0-10, Personal Guidance, Health Age».
- **Verificación independiente**: el recorte de Mulberry y Health+ está confirmado (https://9to5mac.com/2026/02/05/apple-reportedly-scales-back-plans-for-ai-powered-health-coach/). No hay confirmación de que esas funciones ya estén en una beta, y los informes posteriores las retrasan dentro del ciclo de iOS 27 (https://www.macworld.com/article/3055235/).
- **Corrección**: «Apple las tiene previstas, según rumores, para más adelante en el ciclo de iOS 27 (`reported`)».

**B9 · A01-47 · STALE · baja**
- **Dice** (l. 62): «Hay indicios no confirmados de salida del B2C en 2026».
- **Verificación independiente**: la ayuda oficial dice que «BetterUp for Individuals» se está cerrando y ya no admite altas (https://support.betterup.com/hc/en-us/articles/5023276679835).
- **Corrección**: «BetterUp está cerrando su plan para particulares (ayuda oficial)». El dato refuerza P2 10c.

**B10 · A01-56 · DISCREPANCY · baja**
- **Dice** (l. 100): «Marzo o abril de 2026 (fechas contradictorias)».
- **Verificación independiente**: fue el 2-03-2026 (https://9to5mac.com/2026/03/02/free-claude-users-can-now-use-memory-and-import-context-from-rivals/).
- **Corrección**: «2 de marzo de 2026».

**B11 · A01-55 · STALE · baja**
- **Dice** (l. 91): «unos 26.500 servidores (septiembre de 2026) y unos 30.700 (octubre de 2026) [...] El directorio de conectores de Claude superaba los 300 en junio de 2026».
- **Verificación independiente**: el registro oficial tenía 52.042 entradas el 28-10-2026, con duplicados. Los censos deduplicados dan 22.561 en junio. El directorio de Claude tenía 369 conectores en junio y entre 934 y 986 en octubre. Fuentes: https://agentndx-web.pages.dev/blog/how-many-mcp-servers-exist-census-2026 y https://www.dirjournal.com/blogs/claude-connectors-list.
- **Corrección**: dar un rango con fecha y fuente, y actualizar el directorio a «cerca de 1.000 en octubre de 2026».

**B12 · A01-60 · STALE · baja**
- **Dice** (l. 196): «341-386 skills maliciosas en ClawHub, CVE-2026-25253».
- **Verificación independiente**: la campaña ClawHavoc tenía 341 skills el 13-02-2026, y el 1-03-2026 ya había más de 1.184 confirmadas. Además de CVE-2026-25253 hay CVE-2026-24763, CVE-2026-25157 y CVE-2026-27487. Fuentes: https://www.bitdoze.com/openclaw-security-guide/ y https://adversa.ai/blog/openclaw-security-101-vulnerabilities-hardening-2026/.
- **Corrección**: «más de 1.100 skills maliciosas confirmadas (marzo de 2026) y varias CVE, entre ellas CVE-2026-25253».

**B13 · A01-45 · DISCREPANCY · baja**
- **Dice** (l. 54): «8-20 $/mes (fuentes contradictorias); unos 8,3 M$ captados».
- **Verificación independiente**: la página de precios (https://amie.so/pricing) no los muestra, y terceros dan entre 20 y 25 $ al mes. La financiación son unos 7 M$ según VCBacked, más una presemilla de 1,3 M$.
- **Corrección**: «20-25 $/mes según terceros».

**B14 · A01-32 · MISSING · baja (refuerza la recomendación)**
- **Dice** (l. 221): «la API de salud de Garmin, por ejemplo, exige licencia de socio según Delx: `reported`».
- **Verificación independiente**: la API solo está abierta a desarrolladores aprobados y con acuerdo de licencia. Además, Garmin congeló las altas nuevas en la primavera de 2026 y en octubre seguía cerrada (https://the5krunner.com/2026/09/14/garmin-developer-api-access-paused/).
- **Corrección**: añadir la congelación. Hoy un conector oficial con Garmin no es viable, y eso cierra P0-3.

**B15 · A01-07 · MISSING · baja**
- **Dice** (l. 103): la fila de dots no indica la disponibilidad por regiones.
- **Verificación independiente**: el despliegue en Pro excluye el EEE, Suiza y el Reino Unido (https://www.digitaltrends.com/computing/openais-dots-push-ai-beyond-chatbots-with-always-on-agents-that-can-investigate-build-and-act-across-4000-apps/ y https://betanews.com/article/openai-dots-agents-chatgpt/).
- **Corrección**: añadirlo, porque refuerza la tesis europea frente a las plataformas.

**B16 · PROVENANCE (fuente más débil que la disponible) · baja**
- **Dice**: varias filas van como `reported`, aunque tienen fuente oficial. Son Claude Health (l. 97), Claude Duet (l. 99) y Clockwise (l. 50, «fuente interesada»). La URL de dots de la l. 317 es la versión rumana de openai.com y da 403.
- **Verificación independiente**: las fuentes oficiales son https://www.anthropic.com/news/healthcare-life-sciences, https://www.claude.com/resources/articles/claude-duet (que además incluye el plan Ultra) y https://www.getclockwise.com/ (el equipo se une a Salesforce).
- **Corrección**: citar esas fuentes, subir la etiqueta a `verified`, añadir Ultra a Duet y usar https://openai.com/index/introducing-dots/ como URL de dots.

**B17 · A01-27 · MISSING · baja**
- **Dice** (l. 176): «Ninguno lee el calendario». La amenaza 3 (l. 191) solo considera a WHOOP como candidato.
- **Verificación independiente**: Samsung Health Assistant, en beta en EE. UU. desde el 21-07-2026, anuncia respuestas «sensitive to a user's schedule» a través de su Personal Data Engine. Unos lo presentan como futuro y otros como actual (https://www.mobileworldlive.com/samsung/samsung-unveils-ai-powered-health-assistant/).
- **Corrección**: añadir Samsung como candidato en la amenaza 3.

**B18 · OVERCLAIM · baja**
- **Dice** (l. 189): «el usuario tendría el 70 % de Ucoach sin instalar nada».
- **Verificación independiente**: no hay cálculo ni fuente.
- **Corrección**: quitar la cifra o explicar de dónde sale.

**B19 · INTERNAL (01 frente a 06) · baja**
- **Dice** (l. 241): «B2B2C con aceleradoras y equipos de plataforma de fondos», con Valence, BetterUp y CoachHub como prueba.
- **Verificación independiente**: esas tres venden a grandes empresas, no a aceleradoras (A01-46 a A01-48). El 06 prioriza a los coaches y deja las aceleradoras para la fase de escala.
- **Corrección**: remitir a la recomendación del 06.

**B20 · A01-20 · STALE · baja**
- **Dice** (l. 78): «Pro 9,99 $/mes (4,99 $ en promoción)».
- **Verificación independiente**: la promoción Founder Pro a 4,99 $ terminó el 15-10-2026 (https://wellnessproject.ai/press/claude-directory).
- **Corrección**: «Pro 9,99 $/mes».

## Sólido

Está verificado y no hay que «arreglarlo»:

- **Lifestack** (A01-01): planificación por energía con Apple Health, Oura, WHOOP, Garmin y Fitbit, más Google Calendar, Outlook, Todoist y Trello. Se presenta como «AI Planner for ADHD» y tiene 4,4★ con 73 valoraciones.
- **Rise** (A01-02): exporta la previsión de energía a Google o Apple Calendar y cuesta 69,99 $ al año.
- **athletedata** (A01-03): HealthspanOS AG, distintivo «Anthropic verified», en el directorio desde septiembre de 2026 y escribe en Google Calendar.
- **Plataformas:**
  - Claude Health (A01-04): enero de 2026, solo EE. UU., Pro y Max, beta, sin entrenamiento.
  - ChatGPT Health (A01-05): 7-01-2026 y 23-07-2026, excluye el EEE, Suiza y el Reino Unido.
  - **ChatGPT dots** (A01-07) y **Claude Duet** (A01-08) existen, con las fechas, la ejecución en la nube y las condiciones que da el informe.
- **Tareas en la nube y MCP local:**
  - Las tareas de Cowork se ejecutan en remoto, y «Require this computer» es solo para organizaciones (A01-09, ALTA).
  - La inferencia de A01-10 se confirma: las sesiones en la nube no llegan a un MCP por stdio salvo que la app de escritorio esté abierta y conectada (https://support.claude.com/en/articles/15811196-what-to-expect-with-remote-execution-in-claude-cowork). ChatGPT solo admite MCP remotos, aunque tiene un «Secure MCP Tunnel» para servidores locales, que es útil para P0-4.
- **Virtue** (A01-12): sin cifra pública. Hay una segunda ficha, VMR-18158 «AI Life Coach Tools Market», que tampoco la publica.
- **Competencia MCP abierta** (A01-14): ningún MCP abierto con tracción combina agenda, sueño, hábitos y método. Hay intentos con 0-1★: enzojunq/Olav, mrcltk/ai-athlete-assistant-mcp-macos y tsutera09/tempo-mcp.
- **Datos de GitHub y directorios:** Linell/coach, garmin_mcp, Open Wearables, apple-health-mcp-server, private-journal-mcp, totem y OpenClaw (A01-15 a A01-17, A01-53, A01-54 y A01-58). LifeWheel (A01-19) y Wellness Project (A01-20, salvo B20).
- **Precios y funciones de wearables:** Oura, Garmin Connect+, Google Health Coach, WHOOP y Rosebud (A01-21 a A01-26). Ninguno lee el calendario de forma nativa (A01-27, con el matiz de Samsung de B17).
- **Otras afirmaciones:**
  - Steinberger ficha por OpenAI y OpenClaw pasa a una fundación (A01-28).
  - Clockwise cerró el 27-03-2026 (A01-29).
  - Reclaim es de Dropbox desde 2024 y tiene MCP para Claude (A01-30).
  - Sunsama, Akiflow y Timing tienen MCP (A01-31).
  - Gemini Personal Intelligence no cruza datos de salud (A01-34).
  - Las plataformas se limitan a explicar y resumir (A01-35).
- **Apoyo:**
  - Samsung (A01-37) y Ultrahuman (A01-38).
  - Clínicos de WHOOP (A01-41).
  - Motion (A01-42) y precios de Reclaim y de los planificadores (A01-43 y A01-44).
  - Valence (A01-46), Rosebud (A01-50) y Founder Coach (A01-52).
  - ICF 2025 (A01-61), Stratistics de coaches de salud (A01-62) y el rango de 16.500 a 22.000 M$ de salud y bienestar (A01-63).
  - GrowthMentor (A01-64).

## No verificable

| id | Qué | Qué hacer |
|---|---|---|
| A01-13 | Los 5.800 M$ atribuidos a Virtue (l. 21, 114). El verificador solo los encuentra en el mismo blog, lo que coincide con el informe. | Mantener la recomendación de quitar la cifra. No hay dato público. |
| A01-51 | Mindsera «~14,99 $/mes» (l. 66) | Quitar el precio mensual o marcarlo como no confirmado. El anual (~129 $) es MEDIA-BAJA. |
| A01-52 (parte) | Fecha de lanzamiento de Ama, 10-12-2025 (l. 67) | Quitar la fecha o citar la página de lanzamiento de Product Hunt. |
| A01-47 (parte) | Fecha de lanzamiento de BetterUp AI Coaching, 21-1-2025 (l. 62) | Citar la nota de prensa o quitar la fecha. |
| A01-24 (parte) | WHOOP Coach incluido en todos los niveles (l. 34, 116). whoop.com da 403. | Marcar como no confirmado por nivel. |
| A01-03 (parte) | Precio de athletedata | Ya figura como «no publicado». Dejarlo así. |
| A01-63 (parte) | Stratistics, coaching de carrera con IA, 3.700 M$ (l. 133), y la cifra de The Business Research Company | Quitar o sustituir. Market.us da 5.000 M$ en 2025. |
| A01-59 (parte) | Canales de Hermes Agent (Telegram, WhatsApp, Slack) | Citar el README o quitarlo. |

## Falta

- **Google Health Coach en España**, con sus requisitos (Fitbit o Pixel Watch, AI Pro), en la tabla 2.1, en el resumen 3 y en las amenazas (ver C1).
- **Tareas programadas de ChatGPT** (17-06-2026), que sustituyen a Pulse y llegan a Plus y Go.
- **Exclusión regional de dots** (B15) y **congelación de la API de Garmin** (B14).
- **Puentes locales para P0-4**: la app de escritorio de Claude abierta y el «Secure MCP Tunnel» de ChatGPT.
- **Intentos abiertos con 0-1★** que ya combinan sueño y calendario (A01-14). No amenazan hoy, pero el informe debería decir que existen.
- **El cálculo de abajo arriba** que el propio informe recomienda en lugar del TAM (l. 135).
- **Competidores pendientes** (l. 334): Stoic, Reflectly, Ahead, Bunch, Tenor, Bevel, Welltory y Ultrahuman. Siguen sin cubrir.

## Correcciones a aplicar en el informe

1. **l. 15**: «39 fuentes» → «más de 30 fuentes». «por 5 a 10 $ al mes (`verified`, App Store)» → «por unos 7 $/mes o 50 $/año (`reported`)».
2. **l. 16**: mantener Duet y dots. Añadir que dots en Pro excluye el EEE, Suiza y el Reino Unido, y que Duet es solo para EE. UU.
3. **l. 17**: reescribir según C1, con Google Health Coach disponible en España con Fitbit o Pixel Watch y la salud de Claude y ChatGPT bloqueada en la UE.
4. **l. 22**: Lifestack «unos 7 $/mes o 50 $/año».
5. **l. 34 y 116**: indicar que no está confirmado que el coach vaya incluido en todos los niveles.
6. **l. 35 y 118**: LLM de salud femenina «febrero de 2026, en Oura Labs». Counsel cuesta 159 $ al año tras la prueba.
7. **l. 36**: quitar Apple Health y Lingo como fuentes actuales («later»). Añadir «exige Fitbit o Pixel Watch» y quitar «memoria mejorada (octubre de 2026)» si no se cita la fuente.
8. **l. 37**: rebajar lo de la beta de iOS 27.2 a un rumor para más adelante en el ciclo de iOS 27.
9. **l. 42**: precio de Lifestack «~7 $/mes, 50 $/año, 120 $ de por vida (`reported`)». Mantener el resto como `verified`.
10. **l. 50**: citar https://www.getclockwise.com/ (`verified`) y añadir que el equipo se une a Salesforce.
11. **l. 54**: Amie «20-25 $/mes (terceros)».
12. **l. 62**: «BetterUp está cerrando su plan para particulares (ayuda oficial)».
13. **l. 63**: «AIMY 2.0 en noviembre de 2025».
14. **l. 66 y 67**: quitar el precio mensual de Mindsera y la fecha de Ama, o citar la fuente.
15. **l. 68 y 288**: sustituir o quitar Whenever (enlace muerto).
16. **l. 77**: «y unas 29 fuentes más» se mantiene. Cuadrar el total con la l. 15.
17. **l. 78**: «Pro 9,99 $/mes» (la promoción terminó el 15-10-2026).
18. **l. 79 y 177**: actualizar las herramientas de Delx (`delx-living-body`, perfiles «Daily Operator») y quitar `wellness_context`, que no está confirmada. Matizar «Ucoach puede ser ese motor».
19. **l. 91 y 306**: quitar la reseña de dev.to (enlace muerto) y actualizar los recuentos de MCP y del directorio de Claude, con fecha.
20. **l. 97 y 309**: citar https://www.anthropic.com/news/healthcare-life-sciences y subir la etiqueta a `verified`.
21. **l. 99**: citar https://www.claude.com/resources/articles/claude-duet, subir la etiqueta a `verified` y poner «Pro, Max y Ultra».
22. **l. 100**: «2 de marzo de 2026».
23. **l. 102, 165, 189, 316 y 337**: sustituir Pulse por las tareas programadas de ChatGPT (17-06-2026) e indicar que Pulse se retiró.
24. **l. 103 y 317**: URL de dots https://openai.com/index/introducing-dots/ y exclusión del EEE en Pro.
25. **l. 106**: Hermes Agent «desde julio de 2025».
26. **l. 152**: quitar «(con MCP)» de Morgen.
27. **l. 166 y 200**: rebajar «Nadie lo ofrece de forma abierta» a lo que de verdad falta (niveles de evidencia y contexto de trabajo), después de revisar Delx.
28. **l. 170**: «en Europa» → «usuarios de Claude o ChatGPT en Europa».
29. **l. 174**: el motivo de la exclusión del EEE lo atribuye la prensa, no OpenAI. Marcar el argumento como `inferred`.
30. **l. 189**: quitar el «70 %».
31. **l. 191**: añadir Samsung (Personal Data Engine) como candidato a leer la agenda.
32. **l. 195**: la amenaza 7 aplica también en España: Google Health Coach con AI Pro ya está aquí.
33. **l. 196**: «más de 1.100 skills maliciosas (marzo de 2026)» y varias CVE.
34. **l. 221**: añadir que Garmin congeló las altas de su programa de desarrolladores desde la primavera de 2026.
35. **l. 223 y 224**: añadir los puentes que existen hoy (app de escritorio de Claude abierta y «Secure MCP Tunnel» de ChatGPT).
36. **l. 227**: el mensaje de P0-5 se mantiene, pero añadir que Google Health Coach sí está en España.
37. **l. 239 y 241**: remitir el precio (5-8 €) y el comprador B2B2C a lo que decida el 06.
38. **l. 258**: revisar la fecha y el título de la fuente de Google (Fitbit Air es del 7-05-2026).
39. **l. 268**: sustituir el enlace de precios de Rise (404 en el preflight del 06) por la App Store.
40. **l. 337**: quitar la duda sobre Pulse en Plus.

## Re-verificación (2026-11-19)

Correcciones aplicadas con Edit sobre `01-mercado-competencia.md`. Cada cambio lleva la marca «(corregido tras QA 2026-11-19)» y cita la URL que consultó el verificador (`qa/A-respuestas.md`). Las etiquetas se ajustaron a lo que se consultó de verdad: subieron a `verified` Claude Health, Duet y Clockwise, y bajaron a `reported` el precio de Lifestack y la ayuda de BetterUp.

| hallazgo | estado | línea nueva |
|---|---|---|
| C1 · un usuario español sin alternativa (ventana europea) | corregido: resumen 3, hallazgo no obvio, diferencial 3 y P0-5 reformulados. Google Health Coach (con Fitbit o Pixel Watch) y Oura Advisor funcionan en España; el hueco es el método que cruza agenda, trabajo y cuerpo | 17, 170, 202, 228; también 36, 104, 117, 118, 189 y 195 |
| M1 · Delx (`wellness_context`) | corregido: herramientas reales y tesis rebajada | 79, 166, 177 |
| M2 · motivo de la exclusión del EEE | corregido: lo atribuye la prensa; la causa regulatoria pasa a `inferred` | 174 |
| M3 · ChatGPT Pulse vigente | corregido: tareas programadas de ChatGPT (17-6-2026) | 102, 165, 189, 317, 338 |
| M4 · Pro a 5-8 € frente al 06 | corregido: remite al precio del 06 | 240 |
| B1 · athletedata, 39 fuentes | corregido: más de 30 | 15, 77 |
| B2 · precio de Lifestack con `verified` | corregido: unos 7 $/mes, `reported` | 15, 22, 42, 192 |
| B3 · Morgen con MCP | corregido | 152, 160 |
| B4 · fecha de Hermes Agent | corregido | 106 |
| B5 · AIMY 2.0 | corregido | 63 |
| B6 · LLM de Oura y Counsel | corregido | 35, 118 |
| B7 · fuentes de Google Health Coach y Fitbit Air | corregido | 36, 259 |
| B8 · beta de iOS 27.2 | corregido: rumor | 37, 264 |
| B9 · BetterUp B2C | corregido | 62 |
| B10 · fecha de la memoria de Claude | corregido | 100 |
| B11 · recuentos de MCP y del directorio | corregido | 91 |
| B12 · skills maliciosas de ClawHub | corregido | 196 |
| B13 · precio de Amie | corregido | 54 |
| B14 · congelación de la API de Garmin | corregido | 221 |
| B15 · dots excluye el EEE | corregido | 16, 103 |
| B16 · etiquetas y fuentes oficiales | corregido | 50, 97, 99, 318 y el índice |
| B17 · Personal Data Engine de Samsung | corregido | 39, 176, 191 |
| B18 · el «70 %» | corregido: retirado | 189 |
| B19 · B2B2C frente al 06 | corregido | 242 |
| B20 · promoción de Wellness Project | corregido | 78 |
| Bloqueo · chatgate.ai (404) | corregido: enlace retirado; la fila de Whenever queda `reported` con «fuente original retirada» | 68, 289 |
| Bloqueo · dev.to (404) | corregido: dato retirado y sustituido por el censo de agentndx | 91, 307 |
| No verificables (Mindsera, Ama, WHOOP por nivel, Stratistics de carrera) | corregido: se quitan las cifras o se marcan sin confirmar | 34, 66, 67, 116, 133 |

**Nota recalculada** contando solo lo que queda abierto: `nota.py --claims 64 --verificadas 62 --portantes 35 --portantes-ok 34`. Da **9.7**, banda ENTREGABLE, limitada por la cobertura. La única portante sin verificar es A01-13: la cifra de Virtue solo aparece en un blog, que es justo lo que dice el informe, y la recomendación es quitarla.

**Avisos:**
- **Enlaces:** el preflight volvió a correr con `--links` desde este subagente, pero el sandbox no tiene red y todos los enlaces devolvieron «sin respuesta». Para el estado de los enlaces vale la comprobación con curl del coordinador: los dos 404 ya no están en el documento.
- **Recuento del preflight:** ahora da 121 «cifras» porque cuenta las marcas «2026-11-19» y las cifras nuevas con fuente. La cobertura se mantiene sobre las 64 afirmaciones extraídas.
- **Guiones largos, placeholders y fechas relativas:** 0.



## Comprobación de la corrección por un tercero (sesión principal, 2026-11-19)

- Desde la sesión principal, que no escribió el informe ni las correcciones, se cotejó la crítica de la «ventana europea» con las respuestas del verificador independiente (Google Health Coach en España con Google AI Pro; Oura Advisor en español). El resumen 3 y el hallazgo no obvio ya lo recogen. Las otras correcciones no se han cotejado una a una.
- Enlaces: los que el preflight marca con 403 o sin respuesta (Business Wire, openai.com, whoop.com, the5krunner y Product Hunt) bloquean a los robots. No están rotos y no cuentan como bloqueo.
