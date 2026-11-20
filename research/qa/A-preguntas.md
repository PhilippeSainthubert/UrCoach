# QA · Preguntas para el verificador (informes 01 y 06)

Instrucciones para quien verifica: contesta cada pregunta con fuentes propias, sin suponer nada. Para cada respuesta da la fuente (URL), su fecha y si es fuente primaria (web oficial, nota de prensa, ayuda oficial, API, registro) o secundaria (prensa, blog, agregador). Si no encuentras nada o la información se contradice, dilo así. Si un producto o una función por la que se pregunta no existe o no encuentras rastro de él, eso también es una respuesta válida e importante. Fecha de referencia: 2026-11-19.

Capas: **P** = portante (de ella depende una recomendación). **A** = apoyo.

## Informe 01 (mercado y competencia)

| id | capa | pregunta | pista de dónde buscar |
|---|---|---|---|
| A01-01 | P | ¿Qué hace la app Lifestack? ¿Con qué wearables o fuentes de salud y con qué calendarios o gestores de tareas se integra? ¿Cuánto cuesta (mensual y anual)? ¿Cómo se posiciona hoy y qué valoración y número de reseñas tiene en la App Store? | Ficha de la App Store; web oficial del producto |
| A01-02 | P | ¿Qué funciones relacionadas con la energía diaria ofrece Rise Science (app de sueño)? ¿Permite exportar o sincronizar algo con el calendario del usuario? ¿Qué planes y precios tiene? | Centro de ayuda oficial de Rise; web oficial; App Store |
| A01-03 | P | ¿Qué es «athletedata»? ¿Qué empresa lo desarrolla? ¿Está en el directorio de conectores de Claude y con qué distintivo? ¿Desde cuándo? ¿Cuántas y qué fuentes de datos lee? ¿Puede escribir en Google Calendar? ¿Cuánto cuesta? | Ficha en el directorio de conectores de claude.com; web del desarrollador |
| A01-04 | P | ¿Qué integraciones de salud tiene Claude (Anthropic)? ¿Desde cuándo, con qué fuentes (Apple Health, Android Health Connect, otras), en qué países, en qué planes y en qué estado (beta o general)? ¿Usa Anthropic esas conversaciones para entrenar o las guarda en la memoria de Claude? | Anuncio oficial de Anthropic; centro de ayuda de Claude; prensa tecnológica |
| A01-05 | P | ¿Qué es ChatGPT Health? ¿Cuándo se anunció y cuándo se desplegó? ¿Qué fuentes de datos conecta? ¿En qué países está disponible y cuáles quedan fuera? Detalla la situación en Europa. | Anuncio oficial de OpenAI; ayuda de OpenAI; prensa tecnológica y europea |
| A01-06 | P | Si ChatGPT Health o la integración de Apple Health en ChatGPT no están disponibles en algunas regiones, ¿qué motivo ha dado OpenAI o ha publicado la prensa? | Declaraciones de OpenAI; prensa europea especializada; análisis regulatorios |
| A01-07 | P | ¿Existe un producto o función de OpenAI llamado «ChatGPT Dots»? Si existe: qué hace, cuándo se anunció, en qué planes está disponible, si se ejecuta en un ordenador en la nube y a cuántas apps se conecta. | Blog y notas de producto de OpenAI; prensa tecnológica (SiliconANGLE, TechRadar, The Verge) |
| A01-08 | P | ¿Existe un producto o función de Anthropic llamado «Claude Duet»? Si existe: qué hace, cuándo se anunció, en qué países y planes, si tiene lista de espera, si se ejecuta en la nube y si tiene coste extra. | Anuncios de Anthropic; centro de ayuda de Claude; prensa tecnológica (9to5Mac, 9to5Google) |
| A01-09 | P | En Claude Cowork, ¿dónde se ejecutan las tareas programadas (en el ordenador del usuario o en remoto)? ¿Se ejecutan con el ordenador apagado? ¿Existe una opción para obligar a que se ejecuten en el ordenador del usuario y quién puede usarla? ¿En qué planes están? | Centro de ayuda oficial de Claude (artículo sobre tareas recurrentes en Cowork) |
| A01-10 | P | ¿Pueden las tareas programadas de Claude, los agentes en la nube de Claude o de ChatGPT, o ChatGPT Pulse, llamar a un servidor MCP local que se ejecuta por stdio en el ordenador del usuario? ¿O solo a conectores remotos? ¿Hay algún puente de escritorio para ello? | Documentación oficial de MCP en Claude y en ChatGPT; centro de ayuda; especificación de MCP |
| A01-11 | P | A noviembre de 2026, ¿tienen Claude y ChatGPT integración con calendario, memoria y tareas programadas o proactivas? ¿En qué planes? | Páginas de precios y de funciones de Claude y ChatGPT; ayuda oficial |
| A01-12 | P | ¿Qué publica la página del informe de Virtue Market Research sobre el mercado de herramientas de coaching con IA: código del informe, fecha de publicación, periodo de previsión, precio, y si muestra alguna cifra de tamaño de mercado? | Web de Virtue Market Research |
| A01-13 | P | ¿Qué cifra de tamaño del mercado de coaching con IA (o coaching de vida con IA) se atribuye a Virtue Market Research en otras webs, y qué webs la citan? | Búsqueda de la cifra atribuida a Virtue en blogs y notas de prensa |
| A01-14 | P | ¿Existen servidores MCP de código abierto que combinen calendario, datos de sueño o wearables, hábitos y un método de coaching explícito? Nombra los que encuentres, con estrellas y actividad. | GitHub; registros de MCP (registro oficial, Glama, Smithery, mcp.so, PulseMCP) |
| A01-15 | P | ¿Qué es el repositorio Linell/coach en GitHub? ¿Qué hace, con qué licencia, cuántas estrellas tiene y cuándo fue su último commit? | API o web de GitHub |
| A01-16 | P | ¿Cuántas estrellas tiene el repositorio Taxuspt/garmin_mcp, con qué licencia, y cuándo fue su última actividad? | API o web de GitHub |
| A01-17 | P | ¿Qué es Open Wearables (the-momentum)? ¿Con qué wearables y plataformas se integra, con qué licencia, tiene servidor MCP y en qué estado, cuántas estrellas tiene y cuándo fue su última actividad? | GitHub; documentación oficial del proyecto |
| A01-18 | P | ¿Qué es Delx Wellness (davidmosiah)? ¿Licencia, conectores, herramientas que expone (y para qué dice servir cada una), perfiles para agentes, estrellas y actividad? | GitHub; registro de MCP del proyecto |
| A01-19 | P | ¿Qué es LifeWheel como servidor MCP? ¿Cuántas herramientas expone, con qué clientes de IA funciona y qué precio tiene? | Web oficial (página de integraciones) |
| A01-20 | P | ¿Qué es «Wellness Project» en relación con Claude? ¿Está en el directorio de conectores, con qué estatus, desde cuándo, cuántas herramientas tiene y qué planes y precios ofrece? | Nota de prensa del desarrollador; directorio de conectores de Claude |
| A01-21 | P | ¿Cuánto cuesta la membresía de Oura (mensual y anual) y qué incluye respecto a Oura Advisor? | Web oficial de Oura (membresía) |
| A01-22 | P | ¿Qué es Garmin Connect+, qué funciones de IA trae, cuánto cuesta y cómo lo han valorado las reseñas? | Web oficial de Garmin; reseñas especializadas |
| A01-23 | P | ¿Qué es Google Health Coach? ¿Cómo se llamaba antes, cuándo entró en vista previa y cuándo pasó a disponibilidad general, cuánto cuesta y si va incluido en algún plan de Google AI? | Blog oficial de Google; Google Store; prensa tecnológica |
| A01-24 | P | ¿Qué niveles de membresía tiene WHOOP, qué cuesta cada uno y si el coach con IA está incluido? | Web oficial de WHOOP; prensa y comparadores |
| A01-25 | P | ¿Qué planes y precios tiene Rosebud (diario con IA)? ¿Tiene plan gratuito actualmente? | Web oficial; App Store; reseñas |
| A01-26 | P | ¿Qué funciones nuevas ha añadido WHOOP a su coach con IA durante 2026? ¿Lee WHOOP el calendario del usuario de forma nativa? | Notas de prensa de WHOOP; blog oficial; prensa tecnológica |
| A01-27 | P | ¿Leen el calendario del usuario de forma nativa los coaches de IA de Oura (Advisor), Google (Health Coach), Garmin (Connect+), Samsung Health y Ultrahuman? | Webs oficiales y notas de producto de cada fabricante |
| A01-28 | P | ¿Qué relación tiene Peter Steinberger (creador de OpenClaw) con OpenAI? ¿Hubo fichaje, compra u otro acuerdo, cuándo y quién lo anunció? ¿Qué pasó con la propiedad y el gobierno del proyecto OpenClaw? | Blog del propio Steinberger; publicaciones de Sam Altman; prensa (Fortune, Engadget) |
| A01-29 | P | ¿Cuál es el estado de Clockwise (calendario con IA)? ¿Sigue operativo? ¿Ha anunciado cierre, venta u otro cambio, y con qué fechas? | Web y blog de Clockwise; prensa; blogs de competidores |
| A01-30 | P | ¿Quién es el propietario de Reclaim.ai y desde cuándo? ¿Ofrece conector o servidor MCP y para qué clientes de IA? ¿Usa datos de sueño o energía? | Web oficial de Reclaim; nota de adquisición; prensa |
| A01-31 | P | ¿Ofrecen Sunsama, Akiflow, Timing y Morgen acceso por MCP? ¿En qué plan y si es alojado o local? | Páginas de precios y documentación oficial de cada producto |
| A01-32 | P | ¿Qué requisitos pone Garmin para acceder a los datos de salud por su API oficial (Health API): es abierta o exige acuerdo o licencia de socio? | Portal oficial de desarrolladores de Garmin |
| A01-33 | P | Para un usuario en España a noviembre de 2026, ¿cuáles de estas funciones están disponibles: integraciones de salud de Claude, ChatGPT Health, Google Health Coach, Oura Advisor, WHOOP Coach? ¿En qué países está disponible Google Health Coach? | Páginas de disponibilidad por país de cada producto; ayuda oficial |
| A01-34 | P | ¿Qué es «Personal Intelligence» de Gemini, cuándo se lanzó y qué apps de Google conecta? ¿Puede Gemini cruzar Google Calendar con datos de Google Health o Fitbit? | Blog oficial de Google; ayuda de Gemini |
| A01-35 | P | ¿Qué tipo de respuestas dan ChatGPT Health y las integraciones de salud de Claude según sus propios términos: explicar y resumir datos, o dar planes y recomendaciones prescriptivas? ¿Qué limitaciones declaran? | Anuncios y términos oficiales de OpenAI y Anthropic |
| A01-36 | A | ¿Qué ha pasado con «Project Mulberry» y el servicio de coach «Health+» de Apple? ¿Qué funciones de IA de salud trae la versión más reciente de iOS o su beta, y cuándo se esperan? | Prensa especializada en Apple (9to5Mac, MacRumors, Bloomberg) |
| A01-37 | A | ¿Qué funciones de IA de salud ha lanzado Samsung Health en 2026, con qué fechas, y tiene algún asistente conversacional (en qué estado y con qué modelo de IA)? | Sala de prensa oficial de Samsung; prensa tecnológica |
| A01-38 | A | ¿Qué es Ultrahuman Jade, qué hace, y cuánto cuesta el Ultrahuman Ring PRO? ¿Tiene suscripción obligatoria? | Web oficial de Ultrahuman; prensa tecnológica |
| A01-39 | A | ¿Qué novedades ha tenido Oura Advisor desde su lanzamiento: cuándo llegó a todos los miembros, si tiene un modelo propio de salud femenina, y si deriva a clínicos (con qué socio)? | Notas de prensa de Oura; blog oficial; prensa especializada |
| A01-40 | A | ¿Qué novedades ha anunciado Google durante 2026 sobre Google Health, Fitbit y su coach de salud (funciones, dispositivos nuevos, fuentes de datos admitidas)? | Blog oficial de Google |
| A01-41 | A | ¿Qué anunció WHOOP sobre acceso a clínicos por vídeo, en qué país y cuándo? | Nota de prensa de WHOOP (Business Wire) |
| A01-42 | A | ¿Cómo ha cambiado el producto de Motion (usemotion.com)? ¿Qué rondas de financiación ha cerrado, por cuánto y con qué valoración? ¿Qué precios tiene hoy? | Página de precios de Motion; nota de prensa de la ronda |
| A01-43 | A | ¿Qué planes y precios tiene Reclaim.ai hoy? | Página oficial de precios de Reclaim |
| A01-44 | A | ¿Qué precios tienen Sunsama, Akiflow, Morgen y Timing (mensual y anual, y planes con IA o MCP)? | Páginas oficiales de precios |
| A01-45 | A | ¿Qué es Amie (calendario y notas), cuánto cuesta y cuánta financiación ha captado? | Web oficial; prensa o bases de datos de financiación |
| A01-46 | A | ¿Qué es Valence (coach de IA «Nadia»)? ¿Qué clientes públicos tiene, qué rondas ha levantado (importe, inversor principal, fecha) y cuánto lleva captado en total? | Nota de prensa de Valence; prensa (Built In, TechCrunch) |
| A01-47 | A | ¿Cuándo lanzó BetterUp su coaching con IA? ¿Tiene precios públicos? ¿Hay noticias de cambios en su oferta para particulares en 2026? | Sala de prensa de BetterUp; centro de ayuda |
| A01-48 | A | ¿Cuándo lanzó CoachHub su coach de IA AIMY y cuándo AIMY 2.0? | Sala de prensa de CoachHub |
| A01-49 | A | ¿Qué ofrece Rocky.ai a consumidores y a empresas o coaches (marca blanca), y a qué precios? | Web y centro de ayuda de Rocky.ai |
| A01-50 | A | ¿Cuánta financiación ha levantado Rosebud, cuándo y con qué inversor principal? ¿Ha cambiado su oferta gratuita durante 2026? | Prensa (TechCrunch); web oficial de Rosebud |
| A01-51 | A | ¿Qué cuesta Mindsera (diario con IA) en plan mensual y anual? | Web oficial; App Store |
| A01-52 | A | ¿Qué es «Ama» (coach de IA para emprendedores) y cuándo se lanzó? ¿Y «Founder Coach»? | Product Hunt; webs de los productos |
| A01-53 | A | ¿Cuántas estrellas y qué actividad reciente tienen los repositorios the-momentum/apple-health-mcp-server y obra/private-journal-mcp? | API o web de GitHub |
| A01-54 | A | ¿Qué es el repositorio thebriangao/totem? ¿Qué API de WHOOP usa, cuántas herramientas expone y cuántas estrellas tiene? | GitHub |
| A01-55 | A | ¿Cuántos servidores MCP existen según los recuentos públicos más recientes de 2026? ¿Cuántos conectores tiene o ha tenido el directorio de Claude en 2026? | Censos de MCP de terceros; anuncios de Anthropic |
| A01-56 | A | ¿Cuándo pasó la memoria de Claude a estar disponible en el plan gratuito? | Anuncios de Anthropic; notas de versión; ayuda de Claude |
| A01-57 | A | ¿Qué es ChatGPT Pulse, cuándo se lanzó, en qué planes y con qué conexiones? ¿Ha llegado al plan Plus? | Blog oficial de OpenAI; notas de versión; prensa |
| A01-58 | A | ¿Cuántas estrellas tiene el repositorio openclaw/openclaw en GitHub, con qué licencia, y quién lo gobierna hoy? | API de GitHub; web del proyecto |
| A01-59 | A | ¿Qué es Hermes Agent de Nous Research? ¿Licencia, desde cuándo existe, cuántas estrellas tiene en GitHub y qué canales y funciones ofrece? | API de GitHub; web de Nous Research |
| A01-60 | A | ¿Qué incidentes o vulnerabilidades de seguridad se han documentado en 2026 en OpenClaw y en su catálogo de skills? Da cifras e identificadores CVE si los hay. | Prensa de seguridad; base de datos NVD/CVE |
| A01-61 | A | ¿Qué cifras de ingresos globales y número de coaches publica el ICF Global Coaching Study 2025 y quién lo elaboró? | Web oficial de la ICF (International Coaching Federation) |
| A01-62 | A | ¿Qué tamaño y crecimiento estima Stratistics MRC para el mercado de coaches de salud con IA? | Ficha del informe en distribuidores de estudios de mercado |
| A01-63 | A | ¿Qué tamaño estiman las consultoras para el mercado de coaching de salud y bienestar en 2025 (Precedence Research, The Business Research Company, Fortune Business Insights) y para plataformas de coaching de carrera con IA (Stratistics)? | Fichas públicas de los informes de cada consultora |
| A01-64 | A | ¿Qué recomienda GrowthMentor en su artículo sobre coaches de negocio con IA? | Blog de GrowthMentor |

## Informe 06 (negocio y go-to-market)

| id | capa | pregunta | pista de dónde buscar |
|---|---|---|---|
| A06-01 | P | ¿Qué porcentaje de servidores MCP genera ingresos y qué porcentaje supera un umbral de ingresos mensuales relevante, según las estimaciones publicadas en 2026? ¿Quién las publica y con qué metodología o interés? | Artículos sobre monetización de MCP (dev.to, blogs de marketplaces) |
| A06-02 | P | ¿Hay algún servidor MCP o app de consumo dentro de ChatGPT o Claude con ingresos públicos conocidos? | Artículos de monetización de MCP; entrevistas a desarrolladores; marketplaces |
| A06-03 | P | ¿Qué permite hoy el Apps SDK de OpenAI en cuanto a cobros: pago externo (para qué tipo de bienes), checkout integrado (en qué estado) y suscripciones digitales dentro de ChatGPT? ¿Ha cambiado durante 2026? | Documentación oficial del Apps SDK (monetización); foro de desarrolladores de OpenAI |
| A06-04 | P | ¿Permite el directorio de conectores de Claude listar conectores de pago o cobrar suscripciones a través de él? ¿Hay conectores listados que tengan planes de pago? | Directorio de conectores de claude.com; políticas de Anthropic para desarrolladores |
| A06-05 | P | ¿Qué es MCPize? ¿Qué porcentaje de cada suscripción se queda el editor, cuántos desarrolladores y servidores tiene? ¿Qué comisiones cobran otros marketplaces de MCP (MCP Marketplace, Agent Bazaar, Apify)? | Web oficial de MCPize y de cada marketplace |
| A06-06 | P | ¿Pueden los marketplaces de MCP de pago medir y cobrar el uso de un servidor MCP que se ejecuta en local por stdio en la máquina del usuario, o solo de servidores remotos? | Documentación de MCPize, Apify y otros marketplaces |
| A06-07 | P | ¿Cuánto cuesta la membresía de Oura en euros y en dólares (mensual y anual), qué incluye y si hay periodo gratuito? | Web oficial de Oura |
| A06-08 | P | ¿Qué planes y precios tiene Rise Science (anual, mensual, pago único o promociones)? | Centro de ayuda de Rise; App Store |
| A06-09 | P | ¿Cuánto cuesta Google Health Premium, qué incluye, si va incluido en algún plan de suscripción de Google AI y desde cuándo, y en cuántos y qué países está disponible? | Blog oficial de Google; Google Store; prensa tecnológica |
| A06-10 | P | ¿Qué planes y precios tiene Rosebud (mensual y anual)? | Web oficial; App Store |
| A06-11 | P | ¿Qué planes y precios tiene Reclaim.ai (anual y mensual, por plaza)? | Página oficial de precios |
| A06-12 | P | ¿Qué integraciones de salud ofrece Claude, desde cuándo, en qué países y planes, en qué estado, y cómo trata Anthropic esos datos (entrenamiento, memoria)? | Anuncio oficial de Anthropic sobre salud y ciencias de la vida; ayuda de Claude |
| A06-13 | P | ¿Qué lanzó OpenAI con ChatGPT Health y en qué fechas? ¿Qué cambió en la expansión posterior (público, plataformas, requisitos, países)? ¿Cuántas personas preguntan por salud en ChatGPT cada semana según OpenAI? | Anuncio oficial de OpenAI; prensa (Fortune, Digital Trends) |
| A06-14 | P | ¿Qué es ChatGPT Pulse, cuándo se lanzó, en qué planes y si conecta con Google Calendar? | Blog oficial de OpenAI; prensa |
| A06-15 | P | ¿Incluye el plan Pro de Claude tareas programadas? ¿Desde cuándo, en qué apps (escritorio, web, móvil, Cowork) y dónde se ejecutan? | Página de precios de Claude; ayuda oficial |
| A06-16 | P | A noviembre de 2026, ¿han lanzado Anthropic, OpenAI o Google sus integraciones de salud con IA (Apple Health, Health Connect, coach de salud) en la Unión Europea o en España? | Páginas de disponibilidad y ayuda oficial de cada plataforma; prensa europea |
| A06-17 | P | ¿Ha lanzado alguna gran plataforma de IA (Claude, ChatGPT, Gemini) una función o agente que combine la agenda de trabajo del usuario con sus datos de salud o sueño para proponer un plan del día? Incluye agentes proactivos lanzados en 2026. | Anuncios oficiales de Anthropic, OpenAI y Google; prensa tecnológica |
| A06-18 | P | Según los datos de Paperbell, ¿cuánto cobran los coaches por sesión suelta, por cuota mensual (según número de sesiones) y por paquetes? ¿De cuántas ventas y coaches salen los datos y de qué fecha son? | Blog de Paperbell sobre lo que cobran los coaches |
| A06-19 | P | ¿Qué es Coachvox AI, cuánto paga el coach por usarlo y cuánto cobran los coaches a sus clientes por su clon de IA? | Web y centro de ayuda de Coachvox |
| A06-20 | P | ¿Cuánto cuestan Future (entrenador personal remoto) y Trainwell, con pago mensual y anual? | Webs oficiales; reseñas |
| A06-21 | P | En la encuesta de product-market fit de Sean Ellis, ¿cuántas respuestas mínimas se recomiendan para que sea fiable y qué umbral se usa? ¿Qué puntuaciones obtuvo Superhuman al empezar y tras su proceso? | Artículo de First Round Review sobre Superhuman; textos de Sean Ellis |
| A06-22 | P | ¿Qué hay en los dominios ucoach.com, ucoach.io, ucoach.ai, ucoach.app y u-coach.com: cuándo se registraron, cuándo vencen y qué muestra cada uno? | WHOIS/RDAP; visita directa a cada dominio |
| A06-23 | P | ¿Hay apps en las tiendas con el nombre «U-Coach», «Ucoach» o similares? ¿Qué hacen y quién las publica? | App Store y Google Play |
| A06-24 | P | ¿Qué retención típica tienen las apps de hábitos, bienestar y salud a 1, 4 y 12 semanas, según datos publicados? | Benchmarks de retención (Adjust, AppsFlyer, Business of Apps); estudios académicos |
| A06-25 | P | Según el RGPD, ¿qué obligaciones tiene un servicio que almacena en sus servidores datos de salud de sus usuarios (base legal del art. 9, responsable del tratamiento, evaluación de impacto, contrato de encargo, cifrado)? | Texto del RGPD; guías de la AEPD y del CEPD |
| A06-26 | P | Según el RGPD y las autoridades de protección de datos, ¿siguen siendo datos personales, y con qué obligaciones, los datos de salud que un proveedor guarda cifrados de extremo a extremo sin poder leerlos? | Guías del CEPD sobre seudonimización y cifrado; AEPD; doctrina reciente |
| A06-27 | P | ¿Qué tasas de conversión de lista de espera a registro real se consideran buenas y cómo varían con el tiempo que pasa la lista esperando? | Lenny's Newsletter (artículo sobre conversión de listas de espera) |
| A06-28 | P | ¿Hay evidencia de que añadir un coach humano o un acompañamiento de responsabilidad mejore la retención en apps de salud, hábitos o bienestar digital? | Estudios académicos; casos publicados de apps (Noom, Omada, Future) |
| A06-29 | P | ¿Hay marcas registradas o solicitadas «Ucoach», «U-Coach» o similares en EUIPO, OEPM o WIPO, y en qué clases de Niza? | TMview; localizador de la OEPM; WIPO Global Brand Database |
| A06-30 | A | ¿Qué niveles de membresía tiene WHOOP, qué cuestan en EE. UU. y en el Reino Unido y qué funciones añade cada nivel? | Web oficial de WHOOP; prensa (Wareable, T3) |
| A06-31 | A | ¿Qué precio tienen Sunsama (mensual y anual) y qué incluye respecto a MCP? | Página oficial de precios de Sunsama |
| A06-32 | A | ¿Qué precios tiene Motion por usuario y mes? | Página oficial de precios de Motion |
| A06-33 | A | ¿Cuánto cuestan los planes Claude Pro (mensual y anual) y Claude Max? | Página oficial de precios de Claude |
| A06-34 | A | ¿Qué tarifa media por sesión de coaching recoge el ICF Global Coaching Study 2025 a nivel mundial y en Norteamérica? ¿Cuánto cobra un coach de nivel C-suite? | Web de la ICF; resúmenes del estudio |
| A06-35 | A | ¿Cuánto cuesta una sesión de coaching ejecutivo o empresarial en España, presencial y online? ¿Está regulada la profesión de coach en España? | Cronoshare y comparadores de precios; asociaciones de coaching en España |
| A06-36 | A | ¿Qué resultados de ingresos reportan desarrolladores independientes con modelos freemium de servidores MCP (precio del Pro e ingresos)? | Artículos de desarrolladores en dev.to y blogs |
| A06-37 | A | ¿Cuánto ingresan por GitHub Sponsors proyectos de código abierto de tamaño medio? | Perfiles públicos de GitHub Sponsors; artículos con datos |
| A06-38 | A | ¿Qué dice The Pragmatic Engineer sobre cuántos usuarios tienen la mayoría de servidores MCP públicos? | Newsletter The Pragmatic Engineer (análisis de MCP) |
| A06-39 | A | ¿Qué papel tiene Apify en la monetización de MCP y de qué tipo son sus servidores (B2B o consumo)? | Web de Apify; artículos sobre monetización de MCP |
| A06-40 | A | ¿Qué le pasó a Jasper (redactor con IA) tras la llegada de ChatGPT? | Prensa tecnológica y de negocio |
| A06-41 | A | ¿Ha sido adquirida Reclaim.ai por otra empresa? Si es así, por cuál y en qué año. | Nota de prensa de la adquisición; prensa |
| A06-42 | A | ¿Qué porcentaje de visitas en frío se apunta típicamente a una lista de espera, según los proveedores de listas de espera? | Benchmarks de LaunchList y similares |
| A06-43 | A | ¿Cuándo llegó mcp-use a la portada de Hacker News y qué efecto en descargas o estrellas atribuye el propio proyecto? | Blog de Manufact / mcp-use; Hacker News |
| A06-44 | A | ¿Qué directorios y registros de servidores MCP existen y siguen activos (registro oficial, Smithery, Glama, mcp.so, PulseMCP, awesome-mcp-servers)? | Webs de cada directorio; GitHub |
| A06-45 | A | ¿Cuántas empresas ha acelerado Lanzadera (Valencia) y desde qué año? | Web oficial de Lanzadera |
| A06-46 | A | ¿Tienen Wayra y Demium programas de aceleración activos en España y algún programa de bienestar para fundadores? | Webs oficiales de Wayra y Demium |
| A06-47 | A | ¿Qué son Gympass e ifeel? ¿Operan en España en beneficios de bienestar para empleados? | Webs oficiales; prensa de negocio |
| A06-48 | A | ¿Qué son YouCoach y YourCoach, quién los publica y desde cuándo existe youcoach.com? | App Store; webs oficiales; WHOIS |
| A06-49 | A | ¿Qué clases de Niza cubren habitualmente una app o software de coaching de bienestar con IA? | Clasificación de Niza (WIPO); guías de la OEPM o EUIPO |
| A06-50 | A | ¿Tiene el registro de dominios .es (Red.es) un servicio RDAP público? | Web de dominios.es / Red.es |
| A06-51 | A | ¿Qué funciones incluye Google Health Coach y cuáles están limitadas a EE. UU. (por ejemplo historial médico)? | Blog oficial de Google; ayuda de Google Health |
