# 06 · Modelo de negocio y go-to-market

**Fecha:** 2026-11-19 · **Línea 6 del deep research de Ucoach** · **Base:** documento de producto v0.1 (Drive) y aclaración de posicionamiento del 2026-11-19 ("coach de vida centrado en la eficiencia y la excelencia profesional, con energía y sueño óptimos").

**Confianza:** `verified` = comprobado en la fuente original en esta sesión; `reported` = lo dicen fuentes secundarias, sin confirmar en la original; `inferred` = deducción propia a partir de los datos.

> Nota de método: 26 búsquedas web y 20 páginas abiertas o consultadas directamente. A mitad de la investigación se agotó el cupo de búsquedas web que comparten todos los agentes de esta sesión, así que algunos puntos sobre canales (Product Hunt, comunidades españolas que no son Lanzadera) se basan en criterio propio y van marcados como `inferred`. La comprobación de marca en EUIPO/TMview no fue posible de forma automática (el cortafuegos del registro bloquea las consultas).

---

## 1. Resumen

1. **Cobrar a usuarios finales por un MCP casi no da dinero hoy.** Más del 95 % de los servidores MCP no ingresan nada, y menos del 0,5 % pasa de 1.000 $/mes (estimación de feb. 2026, `reported`). No he encontrado ningún MCP de consumo con ingresos públicos. Los directorios de ChatGPT y Claude no cobran suscripciones digitales dentro del chat: OpenAI solo aprueba el pago externo para bienes físicos (2026, `verified`, developers.openai.com/apps-sdk/build/monetization). El directorio de Claude sí lista conectores cuyo servicio se paga fuera, como athletedata o Wellness Project (`verified`, support.claude.com/en/articles/13145358) (corregido tras QA 2026-11-19). Ucoach, además, se ejecuta en local por stdio, así que ningún marketplace que cobre por llamada puede facturarlo.
2. **Hay un precio de 8 a 15 €/mes que se puede defender, pero el contenido propuesto para Pro no lo justifica.** En esa franja están Google Health Premium (9,99 $/mes), Rosebud (12,99 $/mes) y Reclaim (10-12 $/mes); justo por debajo, Oura (5,99 €/mes) y Rise (~5,8 $/mes en plan anual) (corregido tras QA 2026-11-19). Nadie paga cada mes por "instalación en un clic" o "sincronización", y los conectores de salud ya los están regalando las plataformas.
3. **El riesgo de plataforma ya se ha materializado en EE. UU.** Claude (ene. 2026) y ChatGPT (ene. y jul. 2026) leen Apple Health, y Claude también Health Connect. Ambas tienen agenda y automatización proactiva: tareas programadas en Claude Pro y en ChatGPT (con hub propio desde el 17-6-2026, cuando se retiró ChatGPT Pulse), y agentes en la nube con brief matinal: ChatGPT dots (29-9-2026) y Claude Duet (21-10-2026, solo EE. UU.) (corregido tras QA 2026-11-19). Google incluye su coach de salud con Gemini dentro de Google AI Pro sin coste extra (mayo de 2026). Lo que ninguna ha lanzado es un **método** que cruce la agenda, el trabajo y el cuerpo. En la UE, ChatGPT y Claude no leen datos de salud, pero Google Health Coach (con Fitbit o Pixel Watch) y Oura Advisor sí funcionan en España (`verified`, support.google.com/googlehealth/answer/14237941) (corregido tras QA 2026-11-19).
4. **El comprador con más capacidad de pago es el coach humano, no el fundador; que también sea el mejor canal es la hipótesis H3 (corregido tras QA 2026-11-19).** Un coach cobra unos 175 $/mes por una sesión mensual y unos 350 $/mes por 2-5 sesiones (Paperbell, 23.000 ventas, 2026, `verified`). Coachvox AI cobra unos 99 $/mes al coach por su clon de IA; lo que el coach cobra después a sus clientes no se ha podido verificar (`reported`) (corregido tras QA 2026-11-19). Con el modelo "coach-in-the-loop", Ucoach se vende B2B, que es lo que Philippe sabe hacer, y además ataca el mayor riesgo del producto, la retención.
5. **Plan más caro: sí, pero solo híbrido.** Los productos con un humano detrás (Future, 149-199 $/mes; Trainwell, 149 $/mes; 2026, `reported`) muestran que, en fitness, se paga unas 10 veces más cuando hay una persona que te pide cuentas (corregido tras QA 2026-11-19). Un plan "Ucoach + coach" de 99 a 199 €/mes tiene sentido si lo da un coach socio, no Philippe.
6. **Validar el comportamiento antes que la intención.** Con 20 usuarios, la encuesta de Sean Ellis no es fiable (se suele citar un mínimo de unas 40 respuestas; `reported`, sin pasaje confirmado en First Round) (corregido tras QA 2026-11-19). Las métricas que mandan son las locales: briefs a la semana, noches registradas y la retención en la semana 4. Además, hay que pedir dinero pronto, con una preventa o un programa de pago de 30 días.
7. **El nombre "Ucoach" está muy ocupado.** Hay una app iOS "U-Coach" para entrenadores personales, ucoach.io (vídeo para federaciones deportivas, 2025), ucoach.ai ("uCoach launching soon", 2024), ucoach.com (redirige a Athletics Hub, Reino Unido), la app «UCOACH» de marca blanca de Trainerize en Google Play y, sobre todo, la marca **UCOACH registrada y viva en EE. UU.** (USPTO, reg. 3536981, clases 35, 41, 42 y 45; `reported`, markinton.com). ucoach.app caducó el 17-9-2026 y está en periodo de redención. Además "coach" es descriptivo. Sirve como nombre en clave interno, pero el repositorio público y el Show HN deben salir con un nombre propio: ver `09-nombre.md` (corregido tras QA 2026-11-19).
8. **Ruta recomendada:** open source como imán de confianza y de distribución en la comunidad técnica, más un **plan Coach** (B2B2C) como primer ingreso, más **Programas de 30 días por cohortes** como producto de entrada. El Pro gestionado para particulares queda en tercer lugar, y solo si la retención lo justifica.

---

## 2. Tabla de precios comparables

| Producto | Precio | Qué incluye | Fuente | Año | Confianza |
|---|---|---|---|---|---|
| **Oura Membership** | 5,99 €/mes o 69,99 €/año (EE. UU.: 5,99 $ / 69,99 $). Requiere el anillo | +50 métricas, Oura Advisor (IA) incluido, primer mes gratis | ouraring.com/membership | 2026 | verified |
| **WHOOP** One / Peak / Life | 199 / 239 / 359 $/año (Jersey: 169 / 229 / 349 £; la web del Reino Unido no muestra precios) (corregido tras QA 2026-11-19) | Pulsera incluida; Peak añade Healthspan y estrés; Life añade ECG y tensión (beta). WHOOP Coach (IA) incluido | Wareable, T3, trackervs (whoop.com bloquea el acceso automático) | 2025-2026 | reported |
| **Google Health Premium** (antes Fitbit Premium) | 9,99 $/mes o 99 $/año; **incluido sin coste en Google AI Pro y Ultra** | Google Health Coach (Gemini): sueño, actividad, nutrición; historial médico solo en EE. UU.; 37 países, España incluida; exige Fitbit o Pixel Watch | blog.google/products-and-platforms/products/google-health/google-health-coach; support.google.com/googlehealth/answer/14237941 (corregido tras QA 2026-11-19) | mayo 2026 | verified |
| **Rise Science** | ~69,99 $/año (~5,8 $/mes); solo suscripción anual, con ofertas a 59,99 y 35,99 $ (corregido tras QA 2026-11-19) | Deuda de sueño, curva de energía, hábitos | App Store (apps.apple.com/us/app/rise-sleep-tracker/id1453884781) (corregido tras QA 2026-11-19) | 2026 | verified |
| **Reclaim.ai** | Lite gratis; Starter 10 $ (anual) o 12 $ (mensual); Business 15/18 $; Enterprise 22 $ por usuario y mes | Bloques de foco, hábitos, reuniones inteligentes, agentes de IA | reclaim.ai/pricing | 2026 | verified |
| **Sunsama** | 17 $/mes (anual) o 22 $/mes (mensual) | Planificación diaria guiada, integraciones, **acceso por MCP** y Zapier | sunsama.com/pricing | 2026 | verified |
| **Motion** | Pro AI 19 $/usuario/mes; Business AI 29 $ | Planificación automática, IA, créditos | usemotion.com/pricing | 2026 | verified |
| **Rosebud** (diario con IA) | Bloom 12,99 $/mes o 107,99 $/año (~9 $/mes) | Diario con IA, memoria, objetivos | Reseña de Life Note y App Store | 2026 | reported |
| **Claude Pro / Max** (lo que el usuario ya paga) | Pro 17 $/mes (anual) o 20 $/mes; Max desde 100 $/mes; Ultra 200 $/mes (corregido tras QA 2026-11-19) | Conectores, **tareas programadas** ("hand off and schedule tasks") | claude.com/pricing | 2026 | verified |
| **Coachvox AI** (clon de IA para coaches) | ~99 $/mes al coach; lo que los coaches cobran a sus clientes no se ha podido verificar (corregido tras QA 2026-11-19) | Bot entrenado con el contenido del coach | Directorios y ayuda de Coachvox | 2026 | reported |
| **Future** (entrenador humano + app) | 199 $/mes o 149 $/mes con pago anual | Entrenador personal remoto (fitness) | Reseñas en sensai.fit y trainwell | 2026 | reported |
| **Trainwell** (entrenador humano) | 149 $/mes | Entrenador humano por app | trainwell.net | 2026 | reported |
| **Coach humano (EE. UU., mercado medio)** | Sesión suelta ~140 $; cuota mensual: 175 $ (1 sesión) o 350 $ (2-5 sesiones); paquetes: típico 736 $ (unas 6 sesiones), 485 $ con 2-5 sesiones y 1.275 $ con 6 o más (corregido tras QA 2026-11-19) | Datos de más de 23.000 ventas de 1.529 coaches, del 2-10-2025 al 2-10-2026 | Paperbell | oct. 2026 | verified |
| **Coach ejecutivo (EE. UU., gama alta)** | Media mundial ~234 $/sesión; Norteamérica ~297 $; nivel C-suite >500 $/h (sin fuente atribuida) (corregido tras QA 2026-11-19) | Estudio ICF 2025 citado por terceros | nextlevel.coach, noomii | 2025-2026 | reported |
| **Coach ejecutivo/empresarial (España)** | 120-300 € por sesión presencial de 60 min (media declarada de 137-250 €); online, 20-65 € (corregido tras QA 2026-11-19) | Sin regulación; varía mucho | Cronoshare, modelosdeplandenegocios | 2025 | reported |

**Lectura (`inferred`):** hay tres escalones de precio claros. **(a) Apps de datos o planificación: 5-20 $/mes.** **(b) Humano por app: 150-200 $/mes.** **(c) Coaching 1:1: 175-1.000 $/mes.** Con 8-15 €/mes, Ucoach compite en (a) contra productos con hardware o con una app pulida, y además se apoya en la IA del usuario (17-20 $/mes), que cada vez trae más de serie. El margen interesante está en llevar el escalón (c) hacia abajo o el (a) hacia arriba con un humano: el híbrido.

---

## 3. Monetizar un MCP o una herramienta de IA open source (2025-2026)

| Vía | Qué se sabe | Encaje con Ucoach | Confianza |
|---|---|---|---|
| **Marketplaces de MCP de pago** (MCPize, MCP Marketplace, Agent Bazaar, Apify) | MCPize: "los editores se quedan el 80 % de cada suscripción", más de 450 desarrolladores y de 900 a 1.200 servidores. No publica ingresos. Apify se queda el 20 %; de MCP Marketplace y Agent Bazaar no hay datos públicos (corregido tras QA 2026-11-19). Apify es el mayor caso comercial citado, pero es B2B (scraping) | **Malo.** Sirven para servidores **remotos** con clave de API. Un servidor local por stdio, con datos de salud en la máquina del usuario, no se puede medir ni cobrar por llamada | verified (MCPize, 80 %) / reported (resto) |
| **Freemium con clave Pro** | Casos de desarrolladores independientes con Pro de 9 a 19 $/mes: "0 $ de ingresos todavía", "conversión baja" (dev.to, 2026) | Débil sin un servicio alojado que aporte valor | reported |
| **Directorio de apps de ChatGPT** | El pago externo está aprobado solo para bienes físicos; la hoja de pago integrada está en beta privada para marketplaces. En enero de 2026, sin compras dentro de la app ni suscripciones | Sirve para captar usuarios, no para cobrar | verified (docs) / reported (foro) |
| **Directorio de conectores de Claude** | La política del directorio no regula los conectores de pago: el cobro va por fuera, en la cuenta del servicio. Hay conectores listados con planes de pago (athletedata, Wellness Project, Reclaim, Akiflow, Sunsama) (corregido tras QA 2026-11-19) | Visibilidad y canal de venta de un servicio que se cobra fuera, no cobro por uso (corregido tras QA 2026-11-19) | verified (support.claude.com/en/articles/13145358) |
| **Open core + versión alojada** (patrón clásico: Supabase, PostHog, n8n) | Funciona cuando la versión alojada ahorra algo difícil: operaciones, equipo, cumplimiento normativo | Posible para Equipos o Coaches (panel compartido); débil para un individuo | inferred |
| **Producto existente expuesto por MCP** | Es la vía más fiable según todas las guías: el MCP es un canal de un SaaS que ya cobra (Sunsama incluye MCP en su plan de 17-22 $) | Ucoach es el MCP en sí, no hay SaaS detrás. Es una señal: el valor de pago debe vivir **fuera** del MCP | verified (Sunsama) / inferred |
| **Patrocinios** (GitHub Sponsors) | Algunos proyectos sacan entre 500 y 2.000 $/mes | Ingreso marginal, aunque da credibilidad | reported |

**¿Gana alguien dinero con MCP de consumo?** No he encontrado ningún caso con ingresos públicos. Los ejemplos con ingresos son B2B o de desarrolladores: datos financieros, seguridad, bases de datos (`reported`, feb. 2026; estimaciones de un autor con interés comercial). Según The Pragmatic Engineer, la mayoría de los servidores públicos tienen pocos usuarios o ninguno (2025, `reported`). Conclusión (`inferred`): **Ucoach no debe plantearse como "un MCP de pago", sino como un método y un servicio que se distribuyen gratis a través de un MCP.**

---

## 4. Riesgo de plataforma

| Plataforma | Qué ha lanzado | Fecha | Qué hace de lo que hace Ucoach | Confianza |
|---|---|---|---|---|
| **Anthropic / Claude** | Integraciones con Apple Health y Android Health Connect (beta, Pro y Max, **solo EE. UU.**). Claude "detecta patrones en métricas de salud y forma física". No usa esos datos para entrenar y los excluye de la memoria | ene. 2026 | Lee el sueño y la actividad sin Ucoach | verified |
| **Anthropic / Claude** | Tareas programadas incluidas en Pro; desde el 6-10-2026 se ejecutan en remoto | 2026 | Permite programar un brief de la plataforma con sus conectores, sin cron. No llega a un Ucoach local por stdio salvo con la app de escritorio abierta y conectada (corregido tras QA 2026-11-19) | verified (claude.com/pricing; support.claude.com/en/articles/13854387 y 15811196) |
| **Anthropic / Claude Duet** | Agente proactivo en la nube: brief matinal de las apps conectadas, vigila y avisa; pide permiso antes de enviar, pagar o borrar. Solo usa datos de salud si el usuario lo pide. Solo EE. UU., Pro, Max y Ultra, con lista de espera | 21 oct. 2026 | Brief matinal con la agenda: el camino más corto hacia un plan del día con sueño y agenda (corregido tras QA 2026-11-19) | verified (claude.com/resources/articles/claude-duet) |
| **OpenAI / ChatGPT** | ChatGPT Health: Apple Health, MyFitnessPal, Function e historial médico (EE. UU.). En julio, "Health in ChatGPT" para mayores de 18 años en EE. UU. (web e iOS). 300 M de personas preguntan por salud cada semana (230 M en enero) (corregido tras QA 2026-11-19) | 7 ene. y 23 jul. 2026 | Lo mismo, con más alcance | verified |
| **OpenAI / ChatGPT** | Tareas programadas con hub propio (Go, Plus, Pro, Business y Enterprise), que sustituyen a Pulse, retirado ese mismo día (corregido tras QA 2026-11-19) | 17 jun. 2026 | Brief de mañana proactivo con la agenda | reported (engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks) |
| **OpenAI / ChatGPT dots** | Agentes siempre activos con ordenador propio en la nube y más de 4.000 apps; Pro y Business Premium; en Pro excluye el EEE, Suiza y el Reino Unido (corregido tras QA 2026-11-19) | 29 sept. 2026 | Trabajo proactivo sobre las apps del usuario, sin datos de salud en la UE | reported (digitaltrends.com) |
| **Google** | Google Health Coach (Gemini) en Google Health Premium, incluido en Google AI Pro y Ultra; 37 países, entre ellos España y casi toda la UE; exige Fitbit o Pixel Watch (corregido tras QA 2026-11-19) | mayo 2026 | Coach de sueño, actividad y nutrición. No consta que use la agenda | verified (support.google.com/googlehealth/answer/14237941) |
| **WHOOP / Oura** | Coach con IA incluido en la suscripción | 2025-2026 | Coach del dispositivo, sin contexto de trabajo | verified (Oura) / reported (WHOOP) |

**Qué no han hecho (todavía):** (1) **cruzar la agenda de trabajo con el cuerpo** en un único plan con opinión propia ("mueve la negociación, has dormido 5 h"); (2) un **método** explícito con fuentes y avisos sobre la evidencia; (3) **lanzar en la UE** las integraciones de salud de Claude y ChatGPT, que siguen siendo solo para EE. UU. (`verified`); Google sí lo ha hecho con Health Coach (corregido tras QA 2026-11-19); (4) **portabilidad entre IAs**: un mismo coach en Claude, ChatGPT y Gemini; (5) **un humano** que te pida cuentas.

**Cómo se han defendido otros** (`reported`, conocimiento previo, no reverificado en esta sesión): Jasper perdió terreno cuando ChatGPT hizo gratis su función principal: en 2023 recortó un 20 % su valoración interna e hizo despidos (`reported`, maginative.com) (corregido tras QA 2026-11-19). Los que aguantan tienen **flujo de trabajo propio y datos propios** (Granola frente a las notas de Zoom y Meet), **distribución B2B con un comprador distinto del usuario**, o **una comunidad o un método** que la plataforma no replica. Reclaim acabó comprado por Dropbox en agosto de 2024 (`reported`, siliconangle.com) (corregido tras QA 2026-11-19): una salida razonable para una herramienta que la plataforma podía absorber.

**Implicación (`inferred`):** en 12 a 24 meses es probable que Claude o ChatGPT ofrezcan "plan del día con sueño y agenda" de serie en EE. UU. Lo que defiende a Ucoach es el **método que cruza agenda, trabajo y cuerpo, independiente del wearable + el humano + el nicho de fundadores**, con la UE como ventaja temporal frente a Claude y ChatGPT (corregido tras QA 2026-11-19), no la fontanería: conectores, sincronización, avisos.

---

## 5. Evaluación del modelo propuesto

| Pieza | ¿Aguanta? | Por qué |
|---|---|---|
| **Open source MIT gratis** | **Sí, como canal.** | El público técnico solo instalará algo que lea datos de salud si puede auditarlo. Genera confianza, contribuciones y visibilidad (GitHub, HN, directorios de MCP). Riesgo: MIT permite que otro lo aloje; es aceptable si el valor de pago es el humano o el método. |
| **Pro gestionado 8-15 €/mes** (instalación en un clic, sincronización cifrada, conectores, panel, avisos móviles) | **El precio sí, el contenido no.** | (1) La instalación en un clic es un coste de adquisición, no algo por lo que se pague cada mes. (2) Los conectores de salud ya los dan Claude y ChatGPT en EE. UU. y Google también en España, y Oura y WHOOP tienen su propio coach (corregido tras QA 2026-11-19). (3) Sincronizar datos de salud en un servidor convierte a Philippe en responsable del tratamiento de datos de categoría especial (art. 9 del RGPD): base legal de consentimiento explícito (art. 9.2.a), evaluación de impacto (art. 35), contrato de encargo con los proveedores (art. 28), cifrado (art. 32) y notificación de brechas en 72 h (art. 33) (`reported`, legiscope.com y lista de la AEPD) (corregido tras QA 2026-11-19). Es mucho coste fijo para cobrar 10 €. (4) Exige app móvil, infraestructura y soporte: es un producto de consumo completo, que es justo lo que Philippe no tiene. |
| **Equipos por usuario/mes** | **Prematuro.** | Pocos equipos fundadores compran bienestar. Tiene más sentido como "programa para aceleradoras" (sección 6). |
| **Programas (retos de 30 días)** | **Sí, y debería ir primero.** | Tiene principio y fin, lo que encaja con la retención baja de las apps de hábitos (en salud y fitness, entre el 3 y el 8 % de los usuarios siguen activos el día 30: `reported`, getstream.io/blog/app-retention-guide) (corregido tras QA 2026-11-19). Se puede vender en cohortes con un componente humano, se valida sin construir infraestructura y el marketing de contenidos de Philippe lo empuja bien. |
| **Hoja de ruta: conectores en los meses 3-5 y versión gestionada en los meses 5-8** | **Al revés.** | La plataforma está comoditizando los conectores. Primero hay que demostrar retención y disposición a pagar con el método y el humano; construir infraestructura gestionada solo si los números lo piden. |
| **Métricas de validación** (WAU/instalaciones >40 % a 4 semanas, NPS >40) | **Bien, pero falta dinero.** | Hay que añadir una métrica de pago (preventa o programa de pago) y una de valor percibido: "¿cambiaste algo esta semana por Ucoach?". |

**Precio recomendado (`inferred`):**
- **Gratis:** el servidor open source completo.
- **Programa de 30 días por cohortes:** 49-99 € de pago único (cohorte de 10-20 fundadores, check-in semanal en grupo, revisión de datos). Es el producto de entrada y el experimento de disposición a pagar.
- **Plan Coach:** 29-59 €/mes por coach, hasta 10 clientes (más clientes, más precio), con un panel en el que el cliente comparte un **resumen** semanal, no los datos en bruto. Lo paga quien ya factura 175-350 $/mes por cliente.
- **Híbrido "Ucoach + coach":** 99-199 €/mes, prestado por coaches socios con reparto de ingresos. Ancla de precio y producto premium.
- **Pro individual:** 8-12 €/mes, **solo si** en la fase de validación aparece demanda clara de avisos móviles o de panel. Si llega, con un modelo local-first (sincronización cifrada de extremo a extremo para que Ucoach no pueda leer los datos) para que el peso del RGPD sea menor. Es una hipótesis (`inferred`): la doctrina no está cerrada (TJUE C-413/23 P frente a la postura abierta del CEPD) y Ucoach seguiría siendo, como mínimo, encargado del almacenamiento; lo revisa la línea 5 (corregido tras QA 2026-11-19).

---

## 6. Opciones de modelo de negocio

| Opción | Cómo cobra | Pros | Contras | Encaje con Philippe (agencia de growth B2B en España) |
|---|---|---|---|---|
| **A. Pro individual (B2C) gestionado** | 8-15 €/mes | Escala si funciona; mercado de fundadores amplio | Compite con lo que dan gratis Claude, ChatGPT, Google y Oura; CAC de consumo alto; retención de apps de hábitos baja; RGPD art. 9; app móvil necesaria | **Bajo.** Es marketing de consumo, no B2B |
| **B. Coach-in-the-loop (B2B2C)** | 29-59 €/mes por coach, o reparto del híbrido | El comprador ya cobra 175-350 $/mes por cliente; el coach aporta la responsabilidad (retención); cada coach trae a sus clientes (distribución); se vende B2B; diferencial que no van a copiar las plataformas | Mercado de coaches fragmentado y sensible al precio; hay que diseñar bien qué ve el coach (consentimiento) y la calidad de los coaches; compite con herramientas para coaches que ya existen (Trainerize con apps de marca blanca, Coachvox AI a unos 99 $/mes) y que este informe no ha analizado a fondo (corregido tras QA 2026-11-19) | **Alto.** Venta B2B, alianzas y contenido para un nicho: el oficio de Philippe |
| **C. Programas por cohortes** (30 días: sueño, foco, energía) | 49-99 € por cohorte | Valida pago en semanas; sin infraestructura; contenido reutilizable; producto con principio y fin | Hay que facilitarlo (tiempo de Philippe o de un coach); escala lineal | **Alto.** Lanzamientos, listas y LinkedIn |
| **D. Aceleradoras y beneficio para empleados** | Por cohorte o por startup (p. ej. 1.000-3.000 € por cohorte de aceleradora) | Un acuerdo trae entre 10 y 40 fundadores; el bienestar del fundador es un argumento para las aceleradoras; refuerza la marca | Ciclo de venta lento; el que paga no es quien lo usa; en beneficios para empleados compite con Wellhub (antes Gympass), ifeel, etc. (corregido tras QA 2026-11-19) | **Medio-alto.** Philippe tiene red en el ecosistema; es un buen piloto en el trimestre 2 |
| **E. Licencia a fabricantes de wearables** | Licencia o integración | n. a. | Los fabricantes ya tienen coach propio (Oura, WHOOP, Google); no hay tracción para negociar | **Bajo** a corto plazo |
| **F. Contenido como motor** (newsletter o curso "rendimiento sostenible del fundador") | Patrocinio, curso, embudo hacia B, C y D | Reutiliza la biblioteca de 103 libros y los protocolos; construye audiencia, que es lo que más falta hace; bajo coste | Por sí solo da poco dinero; consume tiempo | **Alto como motor**, no como modelo |

**Recomendación (`inferred`):** **F (motor) → C (primer ingreso) → B (negocio recurrente) → D (escala)**, con el open source como base de confianza y A aparcado hasta tener datos. Esta combinación evita alojar datos de salud al principio, monetiza el método y el humano (lo que las plataformas no replican) y se apoya en lo que Philippe sabe hacer.

---

## 7. Plan de go-to-market y validación para los próximos 90 días (20 nov. 2026 - 18 feb. 2027)

**Hipótesis que hay que tumbar o confirmar:**
- **H1 (valor):** un fundador técnico usa el brief de mañana 4 o más días a la semana durante 4 semanas.
- **H2 (pago):** al menos 10 personas pagan 49 € por el programa de 30 días, sumando usuarios activos y lista de espera, y al menos el 25 % de los usuarios activos está entre ellas (corregido tras QA 2026-11-19).
- **H3 (coach):** 3 de cada 10 coaches entrevistados pagarían 39 €/mes por ver el resumen semanal de sus clientes.

### Semanas 1-4 (20 nov. - 17 dic.): uso propio + entrevistas + base pública
- **Uso propio diario** (fase 0 de la hoja de ruta), con un **diario público**: 2 publicaciones a la semana en LinkedIn (en español) y X (en inglés) sobre "lo que mi agenda y mi sueño me dijeron esta semana". *Building in public* con datos propios: es el formato que mejor domina Philippe.
- **15 entrevistas Mom Test** (10 fundadores técnicos y 5 coaches de fundadores o ejecutivos). Preguntas sobre el pasado, no sobre la idea: "¿cuándo fue la última vez que una mala noche te arruinó una reunión importante? ¿Qué hiciste?", "¿qué usas hoy para planificar el día? ¿Cuánto pagas?", "¿has pagado alguna vez a un coach o un programa? ¿Por qué lo dejaste?". A los coaches: "¿cómo sabes qué ha hecho tu cliente entre sesiones?". Reclutamiento: red de Growth4U, contactos de LinkedIn con "founder" y "CTO", comunidades de Claude y MCP.
- **Repositorio público** en GitHub, ya con el nombre definitivo y no con «Ucoach» (ver sección 8 y `09-nombre.md`) (corregido tras QA 2026-11-19), con un README claro (qué datos lee, dónde se guardan, qué no hace), instalación en 3 comandos y un vídeo de 60 segundos con el ejemplo de 5,2 h de sueño y el pitch.
- **Landing de lista de espera** con un único campo (email). Hasta el 21 de diciembre, una sola llamada a la acción que no deja a nadie esperando: "Instálalo gratis (técnicos)". El 22 de diciembre se añade la segunda, "Únete a la cohorte del 19 de enero (49 €)", para que nadie espere más de 4 semanas (corregido tras QA 2026-11-19). Benchmark de referencia: con tráfico frío se apunta entre el 10 y el 20 % según LaunchList, proveedor de listas de espera, y entre el 2 y el 5 % según una fuente independiente (`reported`) (corregido tras QA 2026-11-19). De la lista a cliente de pago, entre el 5 y el 25 %: unos 20 % si se da acceso en menos de un mes y menos del 10 % si se espera más de 3 meses (Lenny, 2022, `reported`: artículo de pago, leído a través de resúmenes) (corregido tras QA 2026-11-19). **Conclusión: no tener la lista esperando más de 4 semanas.**

### Semanas 5-8 (18 dic. - 14 ene.): 20 usuarios + lanzamiento técnico
- **Show HN + directorios de MCP** (registro oficial de MCP, Smithery, Glama, mcp.so, PulseMCP, awesome-mcp-servers) la segunda semana de enero, no en Navidad, y ya con el nombre definitivo (corregido tras QA 2026-11-19). Título técnico y honesto: "Show HN: un servidor MCP local que cruza tu agenda con tu sueño (Python, sin dependencias)". Referencia: mcp-use llegó a portada de HN en agosto de 2025 y lo asocia a un salto en descargas (`reported`, fuente propia del proyecto). Product Hunt queda **para después**, con la versión que tenga panel o programa: el público de PH es menos técnico (`inferred`).
- **Reddit con valor, no con enlaces:** r/ClaudeAI y r/mcp (instalación), r/QuantifiedSelf (los datos propios: "mi energía tras dormir 7 h o más frente al resto"), r/startups o r/Entrepreneur solo con contenido (`inferred`).
- **20 usuarios activos** (12 de la comunidad técnica y 8 de la red de Philippe). Onboarding 1:1 de 20 minutos por videollamada (hace las veces de *concierge*) y grupo de WhatsApp o Telegram. El brief de mañana lo dispara el cron local y llega por Telegram: las tareas programadas de Claude se ejecutan en remoto y no llegan a un Ucoach local salvo con la app de escritorio abierta y conectada (`verified`, support.claude.com/en/articles/15811196). H1 se mide con ese canal (corregido tras QA 2026-11-19).
- **Medir sin interfaz propia:** añadir `ucoach stats`, que lee la SQLite local y genera un resumen anónimo (días con brief, noches registradas, hábitos, check-ins y una pregunta: "¿qué cambiaste esta semana por Ucoach?"). El usuario lo pega cada domingo en un formulario. No hace falta telemetría ni servidor. Activación = onboarding completo + 3 briefs en los primeros 7 días.
- **Concierge MVP de la revisión semanal:** Philippe (o un coach socio) revisa cada domingo el resumen de 5 usuarios y les manda por WhatsApp un único cambio para la semana siguiente. Así se averigua si lo que retiene es el humano.

### Semanas 9-13 (15 ene. - 18 feb.): pedir dinero
- **Cohorte 1 de pago: "30 días de energía para fundadores"**, 49 € (precio de lanzamiento, el normal sería 99 €), de 10 a 20 personas, que empieza el 19 de enero y termina el 17 de febrero, la víspera de la decisión. La venta se abre el 22 de diciembre (corregido tras QA 2026-11-19). Incluye Ucoach, una sesión en grupo a la semana y revisión semanal. Esto valida H2.
- **Piloto con 3 coaches** (H3), que empieza como tarde el 15 de enero para conocer las renovaciones el 15 de febrero (corregido tras QA 2026-11-19): un mes gratis con un resumen compartido por el cliente (exportación de `ucoach stats` + revisión semanal) a cambio de un compromiso de pagar 39 €/mes si renuevan.
- **Una conversación con una aceleradora** para un piloto en primavera (Lanzadera, Valencia: más de 1.800 empresas impulsadas desde 2013 según su convocatoria de septiembre de 2026, `reported`, elreferente.es (corregido tras QA 2026-11-19); también Wayra, Demium o el programa de una escuela de negocio, `inferred`). Oferta: el programa de 30 días para una cohorte, gratis a cambio de datos y un testimonio.
- **Encuesta de Sean Ellis** a todos los que hayan usado Ucoach al menos 2 veces en las últimas 2 semanas. Con menos de 40 respuestas, tomarla como **indicativa**; segmentar por perfil, como hizo Superhuman, que empezó en el 22 % (First Round, 2018, `reported`); la subida posterior al 58 % no se ha confirmado en la fuente (corregido tras QA 2026-11-19).

### Criterios de decisión el 18 de febrero de 2027
| Señal | Seguir | Pivotar |
|---|---|---|
| Retención en la semana 4 (usuarios con brief 4+ días/semana) | ≥ 40 % | < 20 % → el problema es el formato (MCP pasivo), no el precio |
| Pago en la cohorte | ≥ 10 plazas vendidas y ≥ 25 % de los usuarios activos entre ellas (H2) | < 5 plazas → reformular la oferta o el público; entre 5 y 9, repetir con otra oferta (corregido tras QA 2026-11-19) |
| Coaches | ≥ 2 de 3 renuevan pagando | 0 → abandonar B y probar D |
| "Muy decepcionado" (Sean Ellis) | ≥ 40 % en algún segmento | < 25 % en todos |

**Lo que no hay que hacer en estos 90 días:** conectores directos con Oura, Garmin o WHOOP, app móvil, sincronización en la nube, plan de Equipos.

---

## 8. Posicionamiento y comprobación del nombre

### Nombre de categoría
| Opción | A favor | En contra | Veredicto (`inferred`) |
|---|---|---|---|
| "Coach de vida" | Lo entiende todo el mundo; es como lo define Philippe | En España "coach" arrastra escepticismo (profesión sin regular, de 20 € online a 300 € presencial la sesión, sin un estándar claro) (corregido tras QA 2026-11-19); suena a blando para un público técnico | Usar en un segundo nivel |
| "Chief of staff de energía" | Habla el idioma del fundador; sugiere protección de agenda | Promete acciones (que haga cosas), y Ucoach solo sugiere | Bueno para el titular en inglés |
| "Planificador de energía" / "Energy planner" | Concreto, describe la función (el plan del día según el sueño) | Menos aspiracional; Lifestack ya se presenta así («energy-first planning») y Rise exporta su previsión de energía al calendario, así que no diferencia (corregido tras QA 2026-11-19) | **Válido como descripción funcional, no como diferencial** (corregido tras QA 2026-11-19) |
| "Coach de rendimiento sostenible para fundadores" | Recoge la aclaración de Philippe (eficiencia + excelencia + energía y sueño) y el principio "rendimiento sostenible, no obsesión" | Largo | **Recomendado como posicionamiento** |

**Mensaje propuesto:** *"Tu agenda sabe qué te espera hoy. Tu reloj sabe cómo has dormido. Ucoach lo cruza con tu trabajo, dentro de la IA que ya usas, y te dice cómo jugar el día con un método explícito. Tus datos no salen de tu ordenador."* Prueba: el ejemplo de 5,2 h de sueño con negociación y pitch. Contra las plataformas y los coaches de wearable: "funciona con Claude, ChatGPT y cualquier IA compatible con MCP, con cualquier wearable; en Europa, además, Claude y ChatGPT todavía no leen tus datos de salud". Lifestack y Rise ya cruzan agenda y sueño; lo propio de Ucoach es el contexto de trabajo y el método (corregido tras QA 2026-11-19).

### Comprobación del nombre "Ucoach" (2026-11-19)
| Elemento | Hallazgo | Confianza |
|---|---|---|
| ucoach.com | Registrado en 2004; redirige a Athletics Hub (atletismo, Reino Unido) | verified (whois + curl) |
| ucoach.io | Registrado en sept. 2025; "ucoach - Video Management System & Platform for Organising Bodies" (deporte) | verified |
| ucoach.ai | Registrado en junio de 2024; página "uCoach - Launching Soon" con formulario de email (© 2024) | verified |
| ucoach.app | Registrado el 17 sept. 2025; caducó el 17 sept. 2026 y está en periodo de redención (pending delete) (corregido tras QA 2026-11-19) | verified (RDAP, pubapi.registry.google/rdap/domain/ucoach.app) |
| u-coach.com | Registrado el 22 dic. 2025; vence el 22 dic. 2026 y está en venta en ExpiredDomains (corregido tras QA 2026-11-19) | verified (WHOIS) |
| ucoach.es, ucoach.co | Sin respuesta RDAP (no concluyente; .es no tiene RDAP público) | no verificado |
| App "U-Coach App" (iOS, Adrien Chouteau) | Plataforma para entrenadores personales y sus clientes: programas, progreso, cobros | verified (iTunes Lookup API, id 1665103508) (corregido tras QA 2026-11-19) |
| App "UCOACH" (Google Play, com.trainerize.ucoach) | App de marca blanca de Trainerize para un coach (corregido tras QA 2026-11-19) | verified (play.google.com) |
| Marca UCOACH (EE. UU.) | Registrada y viva: USPTO, serie 77453726, reg. 3536981, Strada Collaborative LLC, clases 35, 41, 42 y 45 (corregido tras QA 2026-11-19) | reported (markinton.com/trademark/ucoach-77453726) |
| YouCoach | App de planificación de fútbol (youcoach srl); youcoach.com registrado el 17-6-2005 | verified (WHOIS e iTunes Search API) (corregido tras QA 2026-11-19) |
| YourCoach | Plataforma para coaches de salud (YourCoach Health Inc, en la App Store desde 2018) | verified (iTunes Search API) (corregido tras QA 2026-11-19) |
| Marcas EUIPO / OEPM | **No verificado**: TMview bloquea las consultas automáticas; ninguna búsqueda devolvió registros en la UE o España (corregido tras QA 2026-11-19) | n. a. |

**Conclusión:** "Ucoach" choca en el mismo terreno (coaching y apps de entrenadores) con varios proyectos, tiene ocupados los dominios principales (ucoach.app está en redención y u-coach.com, en venta), en EE. UU. hay una marca UCOACH viva en las clases 35, 41, 42 y 45, y "coach" es descriptivo (corregido tras QA 2026-11-19). **Mantenerlo solo como nombre en clave interno** y sacar el repositorio público, la landing y el Show HN con un nombre propio y registrable. `09-nombre.md` propone «Circalia»; antes de usarlo, buscarlo a mano en TMview y en el localizador de la OEPM, clases 9, 41, 42 y 44 (y probablemente la 35, sin fuente) (corregido tras QA 2026-11-19).

---

## 9. El hallazgo no obvio

**El problema de Ucoach no es el precio de Pro, sino a quién se lo cobra. Las plataformas están regalando justo lo que el plan Pro pensaba cobrar, mientras la única pieza que no pueden copiar (alguien que te pida cuentas) ya tiene un mercado que paga diez veces más.**

- Google incluye su coach de salud con Gemini en Google AI Pro sin coste extra, también en España (2026). Claude y ChatGPT ya leen Apple Health en EE. UU., y Claude Pro incluye tareas programadas (2026) (corregido tras QA 2026-11-19). Los conectores y los avisos, el núcleo del "Pro gestionado", son una función de serie que va a estar en todas partes.
- Los coaches humanos cobran a cada cliente unos 175-350 $ al mes (Paperbell, 2026), y no saben qué hace el cliente entre sesiones. Ucoach les da justo eso, con datos que se quedan en el ordenador del cliente.
- El plan Coach convierte el mayor riesgo del producto (la retención, porque las apps de salud y fitness conservan solo entre el 3 y el 8 % de los usuarios el día 30, `reported`, getstream.io) (corregido tras QA 2026-11-19) en su argumento de venta: el coach es el motor de retención (el apoyo humano mejora la adherencia en apps de salud mental: `reported`, metaanálisis de JAMA Psychiatry 2025 vía hcplive.com) (corregido tras QA 2026-11-19) y, a la vez, el canal de distribución, porque cada coach trae a sus clientes.
- Hay además una **ventaja europea temporal**: las integraciones de salud de Claude y ChatGPT son, a noviembre de 2026, solo para EE. UU. No es que en Europa no haya nada: Google Health Coach (con Fitbit o Pixel Watch) y Oura Advisor funcionan en España, pero ninguno mira la agenda ni el trabajo. El hueco es un método que cruce agenda, trabajo y cuerpo, independiente del wearable. Un coach local-first, que no aloja datos de salud y vende a coaches y aceleradoras en España, juega ahí (corregido tras QA 2026-11-19), y lo vende Philippe, con un oficio de marketing B2B que no sirve para una app de consumo de 10 €.

---

## 10. Índice de fuentes

| # | Fuente | Dato | Año | Confianza |
|---|---|---|---|---|
| 1 | Ucoach: documento de producto v0.1 (Google Drive, id 1S6MFA-6j9KQh4pYVxCYngqUF8hHvjSIaFO7EjO2owyw) | Modelo, hoja de ruta, métricas | 2026 | verified |
| 2 | [Oura Membership](https://ouraring.com/membership) | 5,99 €/mes, 69,99 €/año, Advisor incluido | 2026 | verified |
| 3 | [Reclaim.ai pricing](https://reclaim.ai/pricing) | Planes de 0 a 22 $/usuario/mes | 2026 | verified |
| 4 | [Sunsama pricing](https://www.sunsama.com/pricing) | 17-22 $/mes, incluye MCP | 2026 | verified |
| 5 | [Motion pricing](https://www.usemotion.com/pricing) | 19-29 $/usuario/mes | 2026 | verified |
| 6 | [Claude pricing](https://claude.com/pricing) | Pro 17-20 $, Max 100 $, tareas programadas | 2026 | verified |
| 7 | [Anthropic: Advancing Claude in healthcare and the life sciences](https://www.anthropic.com/news/healthcare-life-sciences) | Apple Health y Health Connect en beta, EE. UU., Pro y Max | ene. 2026 | verified |
| 8 | [Fortune: OpenAI launches ChatGPT Health](https://fortune.com/2026/01/07/openai-launches-chatgpt-health-in-a-push-to-become-a-hub-for-personal-health-data/) | Lanzamiento, integraciones, 230 M de usuarios/semana en enero (300 M en julio, ver fila 37) (corregido tras QA 2026-11-19) | ene. 2026 | verified |
| 9 | [Digital Trends: ChatGPT connects to Apple Health](https://www.digitaltrends.com/computing/chatgpt-can-now-connect-to-your-apple-health-data-to-give-more-personalized-health-answers/) | Health in ChatGPT, EE. UU. | jul. 2026 | verified |
| 10 | [Tom's Guide: ChatGPT Pulse](https://www.tomsguide.com/ai/chatgpt-pulse-is-here-now-ai-starts-the-chat-and-curates-your-feed) | Resumen proactivo diario con agenda; Pulse se retiró el 17-6-2026 (ver fila 36) (corregido tras QA 2026-11-19) | sept. 2025 | reported |
| 11 | [sensai.fit: Google Health Premium 2026](https://www.sensai.fit/blog/google-health-premium-fitbit-ai-coach-2026) y [Android Authority](https://androidauthority.com/google-health-premium-price-inclusions-features-3664507/) | 9,99 $/mes, 99 $/año, incluido en Google AI Pro | mayo 2026 | reported |
| 12 | [OpenAI Apps SDK: Monetization](https://developers.openai.com/apps-sdk/build/monetization) | Pago externo solo para bienes físicos; hoja de pago en beta | 2026 | verified |
| 13 | [OpenAI Community: ChatGPT App Monetization](https://community.openai.com/t/chatgpt-app-monetization-apps-sdk/1372343) | Sin compras ni suscripciones dentro de la app | ene. 2026 | reported |
| 14 | [N. Fainstein: The state of MCP monetization in 2026](https://dev.to/nicolas_fainstein/the-state-of-mcp-monetization-in-2026-28i4) | >95 % sin ingresos; medianas por categoría | feb. 2026 | reported |
| 15 | [MCPize](https://mcpize.com/) | 80 % para el editor; 450+ desarrolladores | 2026 | verified |
| 16 | [dev.to: How I monetize MCP servers in 2026](https://dev.to/rumblingb/how-i-monetize-mcp-servers-in-2026-real-numbers-no-hustle-bros-4ekf) | Freemium 9-19 $, 0 $ de ingresos | 2026 | reported |
| 17 | [Paperbell: What coaches charge](https://paperbell.com/blog/what-coaches-charge/) | 23.000 ventas; cuotas de 175-350 $/mes | oct. 2026 | verified |
| 18 | [Next Level Coach: executive coaching cost](https://www.nextlevel.coach/blog/how-much-does-executive-coaching-cost) | ICF 2025: 234 $ de media, 297 $ en Norteamérica | 2025-2026 | reported |
| 19 | [Cronoshare: coaching empresarial](https://www.cronoshare.com/cuanto-cuesta/coaching-empresarial) y [modelosdeplandenegocios](https://modelosdeplandenegocios.com/blogs/news/analisis-mercado-coaching-espana) | España: presencial 120-300 €/sesión de 60 min; online 20-65 € (corregido tras QA 2026-11-19) | 2025 | reported |
| 20 | [Coachvox support: get paid for AI coaching](https://support.coachvox.ai/article/72-how-to-get-paid-for-ai-coaching) | Lo que los creadores cobran a sus clientes no se ha podido verificar; ~99 $/mes al coach (corregido tras QA 2026-11-19) | 2026 | reported |
| 21 | [Future review (sensai.fit)](https://www.sensai.fit/blog/future-app-review-2026), [Trainwell](https://www.trainwell.net/blog/trainwell-vs-fitbod-human-coach-or-ai-app) | Humano por app: 149-199 $/mes | 2026 | reported |
| 22 | [Wareable: WHOOP memberships](https://www.wareable.com/wearable-tech/which-whoop-membership-deal-2025-black-friday), [T3](https://www.t3.com/active/fitness-trackers/did-whoop-just-win-the-wearable-subscription-game) | 199/239/359 $/año | 2025 | reported |
| 23 | [Rise en la App Store](https://apps.apple.com/us/app/rise-sleep-tracker/id1453884781) (corregido tras QA 2026-11-19), [Tom's Guide](https://www.tomsguide.com/wellness/sleep-tech/i-didnt-trust-the-rise-app-when-it-told-me-to-wake-up-at-4-45am-but-now-i-fall-asleep-quickly-and-sleep-through-the-night) | ~69,99 $/año | 2025-2026 | reported |
| 24 | [Rosebud review (Life Note)](https://blog.mylifenote.ai/rosebud-review/) | 12,99 $/mes, 107,99 $/año | 2026 | reported |
| 25 | [First Round: How Superhuman built an engine to find PMF](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) | Test del 40 % y punto de partida del 22 %; las ~40 respuestas y el 58 % no se han confirmado en la fuente (corregido tras QA 2026-11-19) | 2018 | reported |
| 26 | [Lenny's Newsletter: What is good waitlist conversion](https://www.lennysnewsletter.com/p/what-is-good-waitlist-conversion) | Lista → cliente de pago: 5-25 %; ~20 % con acceso en menos de un mes; <10 % tras más de 3 meses (artículo de pago, leído en resúmenes) (corregido tras QA 2026-11-19) | 2022 | reported |
| 27 | [LaunchList: waitlist benchmark](https://app.getlaunchlist.com/tools/waitlist-benchmark), [mean.ceo](https://blog.mean.ceo/?p=11219) | Visita → lista: 10-20 % en frío según LaunchList; 2-5 % según una fuente independiente (corregido tras QA 2026-11-19) | 2026 | reported |
| 28 | [Manufact (mcp-use): 10.000 GitHub stars](https://manufact.com/blog/10000-github-stars) | Show HN en portada, ago. 2025 | 2025 | reported |
| 29 | [The Pragmatic Engineer: MCP deep dive](https://newsletter.pragmaticengineer.com/p/mcp-deepdive) | La mayoría de los MCP públicos tienen pocos usuarios o ninguno | 2025 | reported |
| 30 | [Lanzadera](https://lanzadera.es/) | +1.800 empresas desde 2013 (convocatoria de septiembre de 2026, vía elreferente.es) (corregido tras QA 2026-11-19) | 2026 | reported |
| 31 | [App Store: U-Coach App](https://apps.apple.com/tj/app/u-coach-app/id1665103508); [ucoach.io](https://ucoach.io); [ucoach.ai](https://ucoach.ai); whois/RDAP de ucoach.com, .io, .ai, .app y u-coach.com | Conflictos de nombre | 2026 | verified / reported |
| 32 | [App Store: YourCoach](https://apps.apple.com/us/app/id1359191114); [YouCoach Soccer Planner](https://apps.apple.com/us/app/-/id1579384518) | Nombres parecidos | 2026 | reported |
| 33 | [Planoly: Claude scheduled tasks](https://www.planoly.com/blog/claude-scheduled-tasks-social-media-reports) | Tareas programadas en las apps de consumo de Claude | sept. 2026 | reported |
| 34 | [Ayuda de Google Health: países y requisitos](https://support.google.com/googlehealth/answer/14237941?hl=en) y [blog de Google: Google Health Coach](https://blog.google/products-and-platforms/products/google-health/google-health-coach) | 37 países con España; incluido en Google AI Pro y Ultra; exige Fitbit o Pixel Watch (corregido tras QA 2026-11-19) | 2026 | verified |
| 35 | [Claude: política del directorio de software](https://support.claude.com/en/articles/13145358) | No regula conectores de pago; el cobro va fuera (corregido tras QA 2026-11-19) | 2026 | verified |
| 36 | [Engadget: hub de tareas programadas de ChatGPT](https://engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks) | Tareas programadas desde el 17-6-2026; retirada de Pulse (corregido tras QA 2026-11-19) | 2026 | reported |
| 37 | [TechCrunch: ChatGPT Health para todos en EE. UU.](https://techcrunch.com/2026/07/23/openai-makes-chatgpt-health-available-to-all-u-s.-users/) | Expansión del 23-7-2026; 300 M de personas a la semana (corregido tras QA 2026-11-19) | jul. 2026 | reported |
| 38 | [Claude Duet](https://www.claude.com/resources/articles/claude-duet) y [Digital Trends: ChatGPT dots](https://www.digitaltrends.com/computing/openais-dots-push-ai-beyond-chatbots-with-always-on-agents-that-can-investigate-build-and-act-across-4000-apps/) | Agentes proactivos en la nube; Duet solo EE. UU.; dots en Pro excluye el EEE (corregido tras QA 2026-11-19) | 2026 | verified (Duet) / reported (dots) |
| 39 | [Claude: tareas recurrentes en Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) y [ejecución remota](https://support.claude.com/en/articles/15811196-what-to-expect-with-remote-execution-in-claude-cowork) | Las tareas se ejecutan en remoto; los MCP locales necesitan la app de escritorio abierta (corregido tras QA 2026-11-19) | 2026 | verified |
| 40 | [RDAP de ucoach.app](https://pubapi.registry.google/rdap/domain/ucoach.app); [marca UCOACH en la USPTO (Markinton)](https://markinton.com/trademark/ucoach-77453726); [Google Play: ucoach](https://play.google.com/store/search?q=ucoach) | ucoach.app en redención; marca UCOACH viva en EE. UU.; app UCOACH de Trainerize (corregido tras QA 2026-11-19) | 2026 | verified / reported |
| 41 | [Getstream: retención de apps](https://getstream.io/blog/app-retention-guide) y [HCPLive: apps de salud mental](https://www.hcplive.com/view/mental-health-apps-gain-high-uptake-struggle-adherence-retention) | Retención al día 30 en salud y fitness; efecto del apoyo humano (corregido tras QA 2026-11-19) | 2025-2026 | reported |
| 42 | [Legiscope: categorías especiales](https://www.legiscope.com/blog/categorias-especiales-datos-rgpd.html) | Obligaciones del RGPD para datos de salud (corregido tras QA 2026-11-19) | 2026 | reported |
| 43 | [Apify: monetización](https://docs.apify.com/platform/actors/publishing/monetize); [SiliconANGLE: Dropbox compra Reclaim](https://siliconangle.com/2024/08/22/dropbox-acquires-ai-powered-calendar-app-reclaim-ai); [Maginative: Jasper](https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/); [Wellhub](https://wellhub.com/es-es/plans-pricing/); [WHOOP Jersey](https://www.whoop.com/je/en/membership) | Comisión del 20 %; adquisición en agosto de 2024; recorte de Jasper; Gympass ahora es Wellhub; precios en libras (corregido tras QA 2026-11-19) | 2024-2026 | reported |

**Pendiente de verificar:** búsqueda manual de marca en TMview y OEPM; benchmarks recientes de Product Hunt para herramientas de desarrollo; herramientas para coaches con datos del cliente (competencia del plan Coach); lo que cobran los coaches de Coachvox a sus clientes. Resuelto en el QA del 2026-11-19: OpenAI sigue sin admitir suscripciones digitales en las apps de ChatGPT; Google Health Coach está disponible en España; Wayra y Demium no tienen programas de bienestar para fundadores (corregido tras QA 2026-11-19).
