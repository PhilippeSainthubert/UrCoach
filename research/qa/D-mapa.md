# D · Mapa de afirmaciones del informe 04 (NO compartir con el verificador)

Informe: `research/04-mcp-seguridad-conectores.md` (321 líneas). Las fuentes se citan por su número en el índice del informe (sección 8, líneas 257-320). "—" = el informe no cita una fuente concreta para esa afirmación.

Recuento: **51 portantes** (D04-01 a D04-51) y **30 de apoyo** (D04-52 a D04-81). Estimación de afirmaciones verificables en todo el informe: unas 170 (muchas celdas de las tablas contienen 2-4 hechos cada una).

| id | capa | lo que dice el informe (cita breve) | línea | fuente que cita el informe |
|---|---|---|---|---|
| D04-01 | P | "La especificación vigente es la **2026-07-28** (publicada el 28-07-2026)" | 13, 32 | 1, 7 |
| D04-02 | P | "elimina el saludo `initialize`, las sesiones…"; "cada petición lleva versión y capacidades en `_meta`. `server/discover` obligatorio" | 13, 32 | 2, 4 |
| D04-03 | P | "**MRTR** (`resultType: \"input_required\"`) sustituye a las peticiones servidor→cliente (elicitation, sampling, roots). `resultType` obligatorio" | 32 | 2 |
| D04-04 | P | "**Roots, Sampling y Logging en desuso.**"; Sampling "En desuso desde 2026-07-28" | 32, 50, 51 | 2 |
| D04-05 | P | Tasks: "Experimental en 2025-11-25; extensión `io.modelcontextprotocol/tasks` en 2026-07-28" | 31, 32, 52 | 2, 3, 13 |
| D04-06 | P | 2024-11-05 a 2025-11-25 = "Final (*legacy*)"; 2026-07-28 = "Current" | 13, 30-32 | 1, 4 |
| D04-07 | P | "un cliente *dual-era* … prueba `server/discover` y, si recibe cualquier error que no sea uno moderno, o si no hay respuesta en un plazo razonable, vuelve a `initialize`" | 13, 35 | 4 |
| D04-08 | P | "Claude Code (runtime v2, desde v2.1.232/v2.1.274) ya hace exactamente eso con servidores stdio" | 35, 56 | 18 |
| D04-09 | P | "Un cliente solo moderno … **falla** con un servidor *legacy*. Todavía no hay ninguno de los grandes así" | 35 | 4 (inferred en parte) |
| D04-10 | P | "la política de desuso da un mínimo de 12 meses" | 35 | — (probablemente 1/4) |
| D04-11 | P | "algo que la especificación cita como fallo habitual … Hay que responder siempre con un error JSON-RPC -32601"; P0: "error -32601 inmediato ante métodos desconocidos antes de `initialize`" | 37, 234 | 4, 5 |
| D04-12 | P | 2025-11-25: "Iconos, elicitation en modo URL, *sampling* con herramientas, **tasks experimentales**, JSON Schema 2020-12 por defecto, errores de validación como `isError` …, stderr para cualquier log en stdio" | 31, 163 | 3 |
| D04-13 | P | Anotaciones desde 2025-03-26; Claude Desktop "Sí (permisos)", Claude Code "Sí", claude.ai "Sí", ChatGPT "Sí (confirmación de escrituras)", Cursor/VS Code "?" | 30, 45 | 10, 11, 18 |
| D04-14 | P | Salida estructurada "2025-06-18; schema libre en 2026-07-28"; "devolviendo **también** el JSON en texto (la especificación lo pide por compatibilidad)" | 30, 46 | 6 |
| D04-15 | P | Elicitation: Claude Desktop "? (en 03-2026 un usuario dijo que no…)"; Claude Code "**Sí**, formulario y URL"; resto "?" | 49 | 18 (`reported` el resto) |
| D04-16 | P | MCP Apps "Extensión estable, 26-01-2026"; Desktop "**Sí** (también con servidores locales)", Claude Code "**No**", claude.ai Sí (con servidor remoto para app tools/entry points/webs), ChatGPT, Cursor, VS Code "Sí" | 53, 224, 226 | 11, 12, 21 |
| D04-17 | P | "`mcp` 2.3.0, 02-10-2026"; "`FastMCP` pasa a llamarse `MCPServer`. Requiere Python ≥3.10" | 18, 62 | 16 |
| D04-18 | P | "14 directas: anyio, httpx2, jsonschema, mcp-types, opentelemetry-api, pydantic, pyjwt[crypto], python-multipart, sse-starlette, starlette, typing-*, uvicorn, pywin32 en Windows" | 18, 63 | 16 |
| D04-19 | P | SDK "Dual-era de serie: responde a `initialize` y a `server/discover` desde el mismo proceso" | 64 | 8 (implícita) |
| D04-20 | P | MCPB "(antes DXT)"; "Tipo `uv` (manifest 0.4): el host instala Python y las dependencias (\"no user Python installation required\")" | 17, 68, 82 | 17, 26 |
| D04-21 | P | "token de Telegram como campo `sensitive`, que Claude Desktop guarda en el llavero del sistema"; "Keychain o Credential Manager" | 17, 82, 161 | 17 |
| D04-22 | P | "Solo Claude Desktop como host confirmado. Los `.mcpb` privados se actualizan a mano. Entrar en el directorio exige revisión de Anthropic. Las extensiones corren **sin sandbox**" | 82 | 17, 25, 26 |
| D04-23 | P | Plugin: "Claude Code: todo. Cowork: servidor local si la sesión corre en tu equipo. **Chat de claude.ai: ignora los MCP locales**" | 83 | 19, 20 |
| D04-24 | P | Registro: "En **preview**, sin garantías ni escaneo propio (lo delega en PyPI y en los agregadores)"; espacio de nombres `io.github.usuario/ucoach`, `server.json` | 84, 89 | 15 |
| D04-25 | P | "La versión web y móvil (claude.ai, ChatGPT) exige un **servidor remoto**"; conector remoto "Es la única vía que llega al móvil y a las tareas programadas en la nube" | 17, 85 | 20, 25 |
| D04-26 | P | "ChatGPT escritorio con MCP stdio local … Solo la app de escritorio, en hilos locales"; "Los plugins con MCP local solo pueden publicarlos **socios aprobados**" | 86 | 27, 28 |
| D04-27 | P | Cowork/claude.ai: "En la nube por defecto (corren \"aunque el equipo duerma o Claude Desktop esté cerrado\")"; "**No.** Solo conectores de la cuenta…"; "\"Require this computer\" existe solo si la organización tiene acceso al equipo activado"; "Planes de pago" | 14, 102 | 24 |
| D04-28 | P | Claude Code en la nube "(antes *routines*)": "Infraestructura de Anthropic"; "los MCP añadidos con `claude mcp add` no aparecen. Mínimo 1 hora"; "Research preview. 100 ejecuciones por hora" | 14, 103 | 22 |
| D04-29 | P | Tareas locales Desktop: "Solo con la app abierta y el equipo despierto. … **una** ejecución de recuperación al despertar (máx. 7 días). Notifica … Desde Claude Desktop 1.1.5368"; acceso a "archivos de configuración MCP y conectores" | 14, 104 | 23 |
| D04-30 | P | ChatGPT: "sustituyen a Pulse desde el 17-06-2026"; "Nube de OpenAI"; "Como mucho una por hora"; notificación push | 14, 106 | 29 (`reported`) |
| D04-31 | P | cron "**Se salta** las ejecuciones mientras el equipo duerme"; launchd `StartCalendarInterval`: "launchd will start the job the next time the computer wakes up" y agrupa; "`StartInterval`, en cambio, **sí** se las salta" | 15, 107-108, 239 | 44 (`man launchd.plist`, macOS 26.6.2) |
| D04-32 | P | "systemd `--user` timer con `Persistent=true` / Programador de tareas (\"ejecutar lo antes posible si se perdió\") … Equivalentes a launchd" | 15, 109 | — (`reported`) |
| D04-33 | P | "En ntfy.sh **los temas son públicos** … servidor propio con `auth-default-access: deny-all` y un token `tk_…`. La caché por defecto dura 12 horas" | 136 | 43 |
| D04-34 | P | "los chats con bots son *cloud chats*, cifrados entre cliente y servidor pero **no de extremo a extremo**" | 137 | 41 |
| D04-35 | P | "un evento de Google Calendar llevó a ejecución de código en Claude Desktop (LayerX, 02-2026, CVSS 10)"; "evento de Calendar → Desktop Commander → ejecución de código (LayerX, 09-02-2026, CVSS 10; Anthropic no lo corrigió entonces)" | 16, 155, 177 | 32 (LayerX/Akamai; enlace bloqueado 403 en el pre-flight) |
| D04-36 | P | "un servidor MCP falso de **Oura** distribuyó el infostealer StealC (02-2026)"; "falso Oura MCP con StealC (Straiker, 05-02-2026)" | 16, 158, 176, 188 | 35 (The Hacker News, "SmartLoader", `reported`) |
| D04-37 | P | "`postmark-mcp` que copiaba emails en BCC (09-2025)" | 158, 174 | 33 (`reported`) |
| D04-38 | P | "Anthropic MCP Inspector (06-2025): CVE-2025-49596, CVSS 9.4" | 171 | 33 (no hay fuente primaria en el índice) |
| D04-39 | P | "mcp-remote (07-2025): CVE-2025-6514, crítica" | 172 | 34 (advisory 09-07-2025) |
| D04-40 | P | "En 04-2026, OX Security criticó cómo los SDK ejecutan el comando de configuración stdio, y Anthropic lo consideró comportamiento esperado"; "(15-04-2026)" | 67, 178 | 36 (`reported`, CSA 20/23-04-2026) |
| D04-41 | P | "`iterparse` con Expat ≥2.7.2 (comprobar `pyexpat.EXPAT_VERSION`)" | 162, 242 | 38 |
| D04-42 | P | "**Oura** eliminó los tokens personales en diciembre de 2025 y ahora exige OAuth"; "**Solo OAuth2.** Tokens personales **en desuso desde 12-2025**, ya no sirven" | 19, 188 | 45 |
| D04-43 | P | "10 usuarios por app sin aprobación de Oura"; "Flujo de servidor y \"client-side only\" (sin secreto)" | 19, 188, 202 | 45 |
| D04-44 | P | WHOOP "permite 10 miembros en sandbox"; "equipo + app en el panel (hasta 5 apps)" | 19, 189 | 46 |
| D04-45 | P | "**Garmin** abrió una vía *Personal* para leer tus propios datos con clave personal (solo *pull*)" | 19, 190, 202, 244 | 47 |
| D04-46 | P | "**Polar** está abierto a cualquier usuario de Flow"; "OAuth2" | 19, 196 | 53 |
| D04-47 | P | "**Apple** sigue sin API web"; "No hay API web. Solo en el dispositivo" | 19, 192 | — (`reported`) |
| D04-48 | P | Health Auto Export "**v10.0 (09-09-2026)**. Automatizaciones a API REST, MQTT, iCloud Drive o Dropbox. **Servidor MCP propio sobre HTTP** (07-2026)"; "Más de 150 métricas"; "Prueba de 7 días; precio no verificado" | 19, 193 | 51 |
| D04-49 | P | Terra "**399 $/mes (anual) o 499 $/mes**, 100.000 créditos (unas 500 conexiones activas)"; "Sin plan gratuito. BAA en Enterprise" | 19, 198 | 54 |
| D04-50 | P | Junction "**300 $/mes, hasta 500 usuarios**. Sandbox gratuito"; "Sin descuento para startups" | 19, 199 | 55 |
| D04-51 | P | Google: "dirección secreta en formato iCal"; "se puede regenerar con *Reset*"; Outlook: publicar calendario | 210 | 56 (enlace 404 en el pre-flight) |
| D04-52 | A | "El error de recurso no encontrado cambia de -32002 a -32602" | 32 | 2 |
| D04-53 | A | "Listas con `ttlMs`/`cacheScope` y orden determinista" | 32 | 2 |
| D04-54 | A | "Hoja de ruta del 22-08-2026": mensajería agéntica, transporte HTTP unificado, identidad de agentes, resultados con forma canónica, descubrimiento progresivo | 33 | 9 |
| D04-55 | A | `resource_link` desde 2025-06-18 | 30, 47 | 6 |
| D04-56 | A | Prompts en Claude Code "como `/ucoach:brief_manana (MCP)`" | 48 | 18 |
| D04-57 | A | Tasks: Desktop "No", Claude Code "**Sí** (beta pública, v2.1.304+)", claude.ai "Sí", ChatGPT/Cursor/VS Code "No" | 52 | 11, 13, 18 |
| D04-58 | A | "Un rastreador externo la sitúa en 13 de 24 clientes (10-2026)" | 49 | — (`reported`) |
| D04-59 | A | Matriz de extensiones "último cambio el 16-11-2026" | 41, 268 | 11 |
| D04-60 | A | "Autorización OAuth (CIMD, `iss`, DCR en desuso) 2025-03-26 → 2026-07-28" | 55 | 2, 14 |
| D04-61 | A | "La propia nota de MCP pidió fijar `mcp<2` para evitar sorpresas" | 67 | 8 (implícita) |
| D04-62 | A | `ui://ucoach/panel`, `text/html;profile=mcp-app`, "CSP declarada en `_meta.ui.csp`"; "Los *entry points* y las webs embebidas de MCP Apps exigen listado Verified" | 85, 224 | 12, 21 |
| D04-63 | A | "Un plugin instalado en la cuenta se sincroniza a Claude Code" | 83 | 20 |
| D04-64 | A | "**OWASP MCP Top 10** (MCP01-MCP10:2025), documento vivo" | 147 | 30 |
| D04-65 | A | "OWASP Top 10 for Agentic Applications (09-12-2025: ASI01 *Agent Goal Hijack*, ASI02 *Tool Misuse*…)" | 148 | 37 (`reported`, vía Cycode) |
| D04-66 | A | "OWASP LLM Top 10 2025 (LLM01 inyección de prompts, LLM02 revelación de información sensible, LLM06 agencia excesiva)" | 149 | — |
| D04-67 | A | "Trifecta letal de Simon Willison (16-06-2025): datos privados + contenido no confiable + comunicación externa" | 150 | 31 |
| D04-68 | A | "GitHub MCP (05-2025): issue pública → fuga de repositorios privados" | 170 | 33 |
| D04-69 | A | "Filesystem MCP de Anthropic (08-2025): escape del sandbox (`reported`)" | 173 | 33 |
| D04-70 | A | "Smithery (10-2025): *path traversal*, se filtró un token de Fly.io (`reported`)" | 175 | 33 |
| D04-71 | A | "`keyring` como extra opcional (25.7.0)"; "(16-11-2025)" | 161, 300 | 39 |
| D04-72 | A | "**SQLCipher** (AES-256) exige una extensión en C" | 160 | 40 |
| D04-73 | A | Oura: "Devuelve **403 si la suscripción Oura ha caducado**"; "Recomienda *webhooks*. Cabecera `User-Agent` obligatoria"; "OpenAPI 1.43"; tipos de datos (resiliencia, estrés, SpO2, VO2 máx…) | 188 | 45 |
| D04-74 | A | WHOOP: refresh token "**rota** en cada uso"; "Expira en 3600 s"; "Escalas: 100, 1.000, 5.000 e ilimitado, con revisión manual. *Webhooks* v1 retirados" | 189 | 46 |
| D04-75 | A | Garmin: "Business Starter = solo *push*, sin histórico y usuarios limitados. Enterprise = *pull*, más de 1 mes de histórico" | 190 | 47 |
| D04-76 | A | Fitbit → Google Health API; "Las apps sin verificar tienen tope de **100 usuarios**. El \"modo personal\"…"; "error `ACCOUNT_NOT_LINKED`"; fechas de cierre no verificadas | 191, 211 | 48, 49 (enlace 49 da 404) |
| D04-77 | A | "Google Fit soportado **hasta finales de 2026**"; "Lectura por defecto de ~30 días (`reported`)" | 194 | 50 |
| D04-78 | A | Polar: "Los tokens **no caducan** salvo revocación"; "Límite: 500 + 20×usuarios cada 15 min. *Changelog* hasta 13-01-2026" | 196 | 53 |
| D04-79 | A | Graph: "**`Calendars.ReadBasic`** basta (también con cuentas personales) y expande los recurrentes"; "ReadBasic no incluye el cuerpo del evento" | 212 | 57 |
| D04-80 | A | "Las RRULE (eventos recurrentes) no tienen soporte en la librería estándar" | 210 | — |
| D04-81 | A | "Telegram Bot API 10.4 (09-11-2026)" | 303 | 42 |

---

## Problemas internos del informe (sin verificar en la web)

### Contradicciones internas

1. **Etiquetas de confianza del resumen más fuertes que las del cuerpo.**
   - Punto 7 (l. 19) marca todos los conectores de salud como `verified`, pero Apple HealthKit es `reported` (l. 192), Android Health Connect es `verified / reported` (l. 194), el precio de Health Auto Export está "no verificado" (l. 193) y las fechas de Fitbit tampoco (l. 191).
   - Punto 4 (l. 16) da como `verified` el falso MCP de Oura, pero la única fuente del índice para ese hecho (35, The Hacker News) está marcada `reported`. Además, la fuente atribuida en el cuerpo, "Straiker, 05-02-2026" (l. 158), no aparece en el índice.
   - Punto 5 (l. 17) marca los formatos como `verified`, mientras la tabla (l. 82) baja la madurez de `uv` en el host a `reported`.
   - Punto 2 (l. 14) etiqueta el bloque como `verified (documentación de Claude)`, pero incluye las tareas de ChatGPT, que no salen de la documentación de Claude y en la tabla son `reported` (l. 106, fuente 29 de prensa).
2. **Atribución del incidente de Claude Desktop.** El cuerpo dice "LayerX" (l. 16, 155) y la fuente es un blog de Akamai titulado "LayerX/Akamai" (l. 293). Además, la l. 155 dice que el vector pasó por "Desktop Commander" (un MCP de terceros), mientras que la l. 177 lo resume como "Extensiones de Claude Desktop → ejecución de código", y el resumen (l. 16) como "ejecución de código en Claude Desktop". Hay que aclarar si el fallo es de Claude Desktop o de la combinación con una extensión de terceros. El enlace de la fuente dio 403 en el pre-flight.
3. **Malware del clon de Oura.** El informe dice StealC (l. 16, 158, 176) y la fuente se titula "SmartLoader troyaniza Oura MCP" (l. 296). Puede ser coherente (un cargador que instala StealC), pero el informe no lo explica.
4. **Polar "sin OAuth complejo".** P2 (l. 244) y la lectura de l. 202 agrupan Polar con Garmin Personal como vías "sin OAuth", pero la tabla dice que Polar usa OAuth2 (l. 196).
5. **"Más de 14 paquetes transitivos"** (l. 159) frente a "14 directas" (l. 63). La lista de l. 63 tiene 13 entradas, y una es un comodín (`typing-*`); `pywin32` es solo de Windows. El nombre `httpx2` es raro: conviene confirmarlo, porque el paquete habitual es `httpx`.
6. **Dos versiones de Claude Code** para el mismo hecho: "desde v2.1.232/v2.1.274" (l. 35). No se explica qué cambió en cada una.
7. **"Solo las tareas locales de Claude Desktop llegan a Ucoach"** (l. 14), cuando la tabla reconoce la opción "Require this computer" de Cowork (l. 102) y que Cowork usa el servidor local "si la sesión corre en tu equipo" (l. 83). La conclusión es más absoluta que sus premisas.

### Conclusiones que no se siguen del todo de sus premisas

1. **"Hoy sigue funcionando porque los clientes nuevos prueban `server/discover`"** (l. 13). Solo se verifica para Claude Code (l. 35). Para Claude Desktop, que es el host de la fase 1.5 (MCPB), no se aporta evidencia de comportamiento dual-era. En la l. 56, Claude Desktop aparece con "—".
2. **Transporte dual-era hecho a mano "en unas pocas funciones"** (l. 18) y esfuerzo "S-M" (l. 234). El P0 propone anunciar `2026-07-28`, lo que implica cumplir MRTR, `resultType` obligatorio, `_meta` por petición, `ttlMs`/`cacheScope` y los nuevos códigos de error (l. 32). La estimación no se apoya en ningún análisis. Además, el propio informe enumera cinco riesgos de la implementación propia (l. 71) y admite que no ha visto el código (l. 37).
3. **Argumento de las dependencias del SDK.** La l. 68 reconoce que con MCPB tipo `uv` el peso de las dependencias "deja de importar al usuario". La tesis se queda solo en la superficie de ataque, que no se cuantifica: no hay CVE de esas dependencias ni análisis del árbol transitivo.
4. **Umbral de "más de 300 usuarios de pago" para los agregadores** (l. 202). No sale de los precios citados (Terra unas 500 conexiones por 399-499 $; Junction hasta 500 usuarios por 300 $). Falta el cálculo.
5. **Garmin Personal como vía "más barata y con menos fricción" para la fase 2** (l. 202). La fase 2 es para no técnicos, y la vía Personal obliga a cada usuario a sacar su propia clave en Garmin Connect. No se evalúa esa fricción.
6. **El cron se marca `verified` con la página de manual de launchd** (l. 107), que describe cron solo por contraste. No se cita `man cron` ni `man crontab`.
7. **"La política de desuso da un mínimo de 12 meses"** (l. 35) se usa para dar urgencia al dual-era, pero no tiene fuente explícita.
8. **"Anotaciones en las 12 herramientas"** (l. 237) y **"los seis rituales"** (l. 91). Las cifras vienen del documento de producto, no de este informe, que solo nombra unas 11 herramientas sueltas.

### Lo que falta

- Los huecos que el propio informe declara (l. 7): Ultrahuman, Rook, Thryve, Pushover, fechas de cierre de la Fitbit Web API, precio de Health Auto Export y soporte de elicitation en Claude Desktop. Aviso de método: el presupuesto de búsquedas se agotó a mitad de la investigación, pero la mayoría de las filas siguen marcadas `verified`.
- Columnas "?" para Cursor y VS Code en casi todas las funciones (l. 45-56), y sin datos de otros clientes (Gemini CLI, Windsurf, Zed…).
- Cómo negocia Claude Desktop (el host de MCPB) la versión del protocolo con un servidor *legacy*.
- Si las tareas locales de Claude Desktop (pestaña Code) leen la configuración MCP de Claude Desktop (`claude_desktop_config.json`, extensiones MCPB) o solo la de Claude Code. La arquitectura del brief de mañana depende de ello (l. 121-122).
- Las implicaciones de seguridad de usar el servidor MCP propio de Health Auto Export junto a Ucoach: es otro servidor en la misma sesión, lo que agrava la trifecta letal de la amenaza 2.
- Si la API de Oura exige suscripción de pago activa para leer los datos propios. Se menciona el 403 (l. 188), pero no cómo afecta a la recomendación de la fase 2.
- El soporte de llavero en Linux sin dependencias. Se apoya en `keyring` como extra, lo que tensiona el principio de "sin dependencias".
- Las fuentes 49 (Google Cloud, apps sin verificar) y 56 (Google Calendar iCal) dieron 404 en el pre-flight (`qa/pf-04-...json`), y la 32 (Akamai) dio 403. Las afirmaciones D04-51, D04-76 y D04-35 dependen de ellas.
