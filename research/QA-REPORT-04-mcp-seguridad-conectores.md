---
kind: qa-report
target: 04-mcp-seguridad-conectores.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 10.0
score_limited_by: hallazgos
coverage_claims: 81
coverage_verified: 81
independent: true
sources: 111
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 04 · MCP, proactividad, distribución, seguridad y conectores de datos

## Nota: 0.0 / 10 · REHACER (antes de corregir; tras las correcciones, 10.0 · ENTREGABLE, ver «Re-verificación»)

La nota la limitan los hallazgos, no la cobertura. Se verificaron las 81 afirmaciones extraídas, las 51 portantes incluidas, y 46 de esas 51 aguantan. La penalización suma 15 puntos: 2 bloqueos de enlaces (4), una crítica (3), 5 medias (5) y 12 bajas (3). Casi todo se arregla editando una línea. Con los dos enlaces y la crítica corregidos, la nota recalculada sería 2.0, y para pasar de 7 habría que cerrar también las medias.

**Modo**: Deep · **Tipo**: research técnico · **Fecha**: 2026-11-19
**Independencia**: verificador en contexto separado ✓. No vio el informe ni el mapa, y contestó 81 preguntas neutras con fuente abierta en su sesión (69 ALTA, 12 MEDIA).
**Método**: Chain of Verification. Extractor (mapa `qa/D-mapa.md` y preguntas `qa/D-preguntas.md`), verificador (`qa/D-respuestas.md`) y comparación en este informe. `searches: 0` se refiere a esta fase de comparación; el verificador declaró unas 14 búsquedas web solo para localizar fuentes.
**Rúbricas**: ⚠ no se cargaron `_base` ni la rúbrica de research de g4u-brain en esta pasada. Ucoach no es cliente de G4U con overlay.
**Voz**: ⚠ solo las reglas absolutas (cero guiones largos, castellano de tú). No hay guía de voz de Ucoach.

## Cobertura

| | |
|---|---|
| Afirmaciones verificables estimadas en el documento | unas 170 (muchas celdas juntan 2-4 hechos) |
| Afirmaciones extraídas y preguntadas (C = máx(53 del preflight, 81)) | 81 |
| Verificadas con fuente consultada (incluidas las refutadas) | 81 (100 %) |
| Portantes verificadas | 51 de 51 (46 aguantan tal cual; 5 con hallazgo) |
| Apoyo verificadas | 30 de 30 (27 aguantan; 3 con hallazgo) |
| No verificables | 0 afirmaciones enteras; 1 subdato (WHOOP, 3600 s) |

Clasificación por id:

| Clase | ids |
|---|---|
| VERIFIED | 01-09, 11-21, 23-32, 34, 35, 37-48, 50-68, 70-77, 79-81 |
| STALE | 22 (directorio de MCPB) |
| OVERCLAIM | 10 (política de 12 meses) |
| DISCREPANCY | 33 (ntfy), 36 (fecha del clon de Oura), 49 (Terra 399 $), 69 (fecha del Filesystem MCP), 78 (tokens de Polar) |
| UNVERIFIABLE (subdato) | 74 (caducidad de 3600 s del token de WHOOP) |
| INTERNAL / MISSING | ver Hallazgos (P0 incompleto, Polar "sin OAuth", etiquetas de confianza, etc.) |

## Veredicto

**REHACER** (`MAJOR ISSUES`) antes de corregir; **ENTREGABLE** (`PASS`) tras aplicar las correcciones (ver «Re-verificación»). El veredicto inicial salía de dos reglas: quedan dos bloqueos deterministas sin resolver y una crítica abierta. Fuera de eso, el informe es mucho mejor de lo que dice la nota. Todo el bloque del protocolo 2026-07-28, el SDK, las tareas programadas, launchd, las CVE, el clon de Oura y las API de Oura, WHOOP, Garmin, Apple y Junction coinciden con la verificación independiente. Lo que hay que rehacer es la sección de distribución con MCPB y una lista corta de líneas.

## Bloqueos deterministas (preflight)

| # | Enlace | Línea | Estado en el preflight | Qué vio el verificador | Corrección |
|---|---|---|---|---|---|
| B1 | https://support.google.com/cloud/answer/7454865 | 312 (fuente 49) | 404 | La abrió y la usó en D04-76 (tope de 100 usuarios de las apps sin verificar). El 404 parece de idioma o de bot. | Sustituir por `https://support.google.com/cloud/answer/7454865?hl=en` y añadir la página hermana `https://support.google.com/cloud/answer/13464323` |
| B2 | https://support.google.com/calendar/answer/37648 | 319 (fuente 56) | 404 | La abrió con `?hl=en` (D04-51) | Sustituir por `https://support.google.com/calendar/answer/37648?hl=en` |

Aviso, no bloqueo: la fuente 32 (l. 293, `akamai.com/blog/claude-desktop-extensions-rce`) dio 403. El verificador confirmó el caso en The Register (ver H-B2).

## Contrato de escritura y voz

- **Script de-slop**: no disponible en esta máquina (no existe `~/PROJECTS/sanchocmo-openclaw/skills/de-slop/scripts/` y `G4U_DESLOP_SCRIPT` está vacío). Las cuatro pruebas contables (afirmaciones largas, párrafos de más de cuatro líneas, monotonía de ritmo, patrones fuera de presupuesto) **no se han comprobado**. No es que estén pasadas.
- **Guiones largos**: 0 tras la corrección del coordinador (comprobado con `grep` sobre la raya y el guion medio, U+2014 y U+2013).
- **Voz**: castellano de tú y sin narrativa de proceso en el cuerpo. La nota de método de la l. 7 ("el presupuesto de búsquedas web se agotó") es narrativa de proceso, pero es útil porque declara un límite. Se puede dejar.

## Hallazgos

### Crítica

**H-C1 · STALE · crítica · El directorio de Claude ya no acepta paquetes MCPB**
- **Dice**: "**Baja**: doble clic o directorio"; "Actualización automática si está en el directorio"; "Entrar en el directorio exige revisión de Anthropic"; "Solo Claude Desktop como host confirmado" (l. 82). El resumen (l. 17) y la P1 (l. 241) presentan el `.mcpb` como "distribución de un clic" para la fase 1.5.
- **Verificación independiente** (D04-22, D04-23): la documentación actual de Claude dice que "Desktop extension listings in the directory are deprecated, and the directory no longer accepts MCPB submissions", y que un servidor local se distribuye dentro de un **plugin** (https://claude.com/docs/connectors/building/mcpb.md, https://claude.com/docs/connectors/custom/add-unlisted.md). Pero un plugin con servidor local se **ignora** en el chat (claude.ai web, app de escritorio y móvil) y solo carga en Claude Code y en Cowork local (https://claude.com/docs/plugins/platform-support.md). Un artículo de ayuda más antiguo aún menciona un formulario de envío; el verificador lo marca como contradicción entre fuentes, y gana la documentación más reciente. Además, el blog de MCP del 20/21-11-2025 cita como hosts compatibles "the Claude desktop app, Claude Code, and MCP for Windows" (https://blog.modelcontextprotocol.io/posts/2025-11-20-adopting-mcpb/).
- **Por qué es crítica**: la recomendación de distribución para no técnicos se apoya en el directorio, por la instalación, por las actualizaciones automáticas y como canal de confianza frente a clones. Sin directorio, cada usuario instala un `.mcpb` privado y lo **actualiza a mano**. En un producto con datos de salud, eso significa que un parche de seguridad no llega solo. Y el canal que Anthropic propone ahora (plugin) no llega al chat de Claude Desktop, que es justo donde está el público de la fase 1.5.
- **Corrección**: reescribir la fila MCPB (l. 82), el punto 5 del resumen (l. 17) y la P1 (l. 241). Lo que debería decir:
  - el `.mcpb` sigue siendo la única vía de un clic para el chat de Claude Desktop, pero solo como **fichero privado** (sin directorio y sin actualización automática);
  - hay que montar un aviso de versión propio, por ejemplo que `ucoach` compruebe la última versión firmada y lo avise en el brief;
  - el plugin es la vía para Claude Code y Cowork;
  - hay que añadir Claude Code como host compatible de MCPB.

### Medias

**H-M1 · MISSING · media · La P0 del modo dual-era está incompleta para anunciar 2026-07-28**
- **Dice**: P0 "Modo dual-era: `server/discover`, aceptar `_meta.io.modelcontextprotocol/*` por petición, `resultType:"complete"`, error -32601 … y anunciar `2026-07-28` + `2025-11-25`", esfuerzo "S-M" (l. 234). El resumen dice "unas pocas funciones" (l. 18).
- **Verificación independiente** (D04-02, D04-03, D04-53, https://modelcontextprotocol.io/specification/2026-07-28/changelog.md): en 2026-07-28 también son **obligatorios** `ttlMs` y `cacheScope` en `tools/list`, `prompts/list`, `resources/list`, `resources/read` y `resources/templates/list`. El servidor devuelve `serverInfo` en el `_meta` de cada resultado, y el desajuste de versión se contesta con `UnsupportedProtocolVersionError` (-32022). Además, se eliminan `ping` y `logging/setLevel`, y "recurso no encontrado" pasa a -32602.
- **Corrección**: completar la lista de la P0 con `ttlMs`/`cacheScope` en los listados, `serverInfo` en `_meta`, el error -32022 ante versiones no soportadas y -32602 para recursos inexistentes. Revisar el esfuerzo (probablemente M) o recomendar que Ucoach siga anunciando solo `2025-11-25` hasta tener pruebas de conformidad.

**H-M2 · OVERCLAIM · media · La política de 12 meses no protege a los servidores legacy**
- **Dice**: "la política de desuso da un mínimo de 12 meses y la tendencia está clara" (l. 35), sin fuente.
- **Verificación independiente** (D04-10, https://modelcontextprotocol.io/community/feature-lifecycle.md): la Feature Lifecycle and Deprecation policy (SEP-2596) fija un mínimo de 12 meses para **funciones** deprecadas, más una vía urgente de 90 días por seguridad. "La política se aplica a funciones, no a revisiones enteras", y no hay plazos de soporte de revisiones antiguas (https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/). Roots, Sampling y Logging se pueden retirar como pronto en la primera revisión a partir del 2027-07-28 (D04-04).
- **Corrección**: "La política de desuso de MCP (SEP-2596) da al menos 12 meses a las funciones deprecadas (Roots, Sampling, Logging: retirada no antes de la primera revisión tras el 2027-07-28), pero no fija plazos de soporte para las revisiones antiguas ni para el saludo `initialize`". Citar feature-lifecycle.md.

**H-M3 · DISCREPANCY + INTERNAL · media · Polar sí usa OAuth y sus tokens caducan**
- **Dice**: "OAuth2. Los tokens **no caducan** salvo revocación" (l. 196). La lectura de la l. 202 pone Garmin Personal "(sin OAuth)" y Polar como la vía más barata, y la P2 (l. 244) dice "Conector Garmin Personal o Polar (sin OAuth complejo)".
- **Verificación independiente** (D04-46, D04-78, https://www.polar.com/accesslink-api/): cualquier usuario registrado de Polar Flow puede crear un cliente API, con OAuth2 (código de autorización que caduca en 10 min). El token lleva `expires_in`, y el ejemplo de la documentación (31535999 s) equivale a **un año**. Hay un segundo límite de peticiones: 5.000 + 100 × usuarios cada 24 h.
- **Corrección**: l. 196: "OAuth2; el token caduca (`expires_in`, unos 365 días en el ejemplo de la documentación) y hay que reautorizar". Añadir el límite de 24 h. En la l. 202 y la l. 244, separar Garmin Personal (clave personal, sin OAuth) de Polar (OAuth2 sencillo, con reautorización anual).

**H-M4 · DISCREPANCY · media · El precio de 399 $/mes de Terra no aparece**
- **Dice**: "**399 $/mes (anual) o 499 $/mes**, 100.000 créditos (unas 500 conexiones activas)" (l. 198); el resumen dice "Terra desde 399-499 $/mes" (l. 19).
- **Verificación independiente** (D04-49, https://tryterra.co/pricing): Quick Start "desde 499 $/mes" con 100.000 créditos de Unified API, y Enterprise a medida. No hay plan gratuito (solo garantía de devolución de 30 días). El verificador no encontró ni el precio anual de 399 $ ni la equivalencia "unas 500 conexiones activas".
- **Corrección**: "Terra: desde 499 $/mes (Quick Start, 100.000 créditos), sin plan gratuito". Quitar el 399 $ y "unas 500 conexiones" salvo que se cite dónde aparecen. La conclusión de la l. 202 sale reforzada.

**H-M5 · DISCREPANCY · media · ntfy.sh dice lo contrario sobre el nombre del tema**
- **Dice**: "En ntfy.sh **los temas son públicos** y el nombre no es una contraseña, así que hay que usar un servidor propio" (l. 136).
- **Verificación independiente** (D04-33, https://docs.ntfy.sh/publish/, https://docs.ntfy.sh/config/): la documentación dice "all topics on ntfy.sh are public" y, a la vez, que "the topic is essentially a password". Es decir, el modelo de seguridad de ntfy.sh es un nombre de tema imposible de adivinar. En servidor propio con autenticación, el acceso por defecto es `read-write`, y hay que poner `auth-default-access: deny-all` (esto sí es correcto). La caché de 12 h es correcta.
- **Corrección**: "En ntfy.sh los temas son públicos y su única protección es que el nombre sea imposible de adivinar (la documentación lo trata como una contraseña). Para un canal con datos de salud, mejor un servidor propio con `deny-all` y tokens". La decisión puede quedarse igual, pero el argumento tiene que reflejar la fuente. Y, como las plantillas no llevan texto libre (regla 3, l. 132), conviene valorar si ntfy.sh con un tema aleatorio largo basta para la fase 1.

### Bajas

**H-B1 · DISCREPANCY · baja · Fecha y atribución del clon de Oura**
- **Dice**: "falso Oura MCP con StealC (Straiker, 05-02-2026)" (l. 158). La fuente 35 es de The Hacker News y está marcada `reported` (l. 296), y Straiker no aparece en el índice.
- **Verificación independiente** (D04-36, https://securityaffairs.com/188135/ai/smartloader-hackers-clone-oura-mcp-project-to-spread-stealc-malware.html): Straiker STAR Labs, publicado el **17-02-2026**. El grupo SmartLoader troyanizó el MCP de Oura y lo envió a registros públicos de MCP; la carga final era StealC.
- **Corrección**: l. 158: "(Straiker STAR Labs, 17-02-2026; grupo SmartLoader)". Añadir al índice el informe de Straiker o el de Security Affairs, y subir la confianza a `verified`.

**H-B2 · DISCREPANCY · baja · Incidente LayerX: fuente bloqueada, vector y caso que falta**
- **Dice**: "un evento de Google Calendar llevó a ejecución de código en Claude Desktop (LayerX, 02-2026, CVSS 10)" (l. 16); "-> Desktop Commander ->" (l. 155); fuente "LayerX/Akamai" (l. 293).
- **Verificación independiente** (D04-35, https://www.theregister.com/2026/02/11/claude_desktop_extensions_prompt_injection/): LayerX (Roy Paz), 9 y 11-02-2026. Es un RCE zero-click en el que Claude encadena un conector con acceso a terminal. El CVSS 10 lo **asignó el propio investigador**, y Anthropic no lo corrigió ("falls outside our current threat model"). Hubo además otro caso, "PromptJacking" de Koi Security (CVSS 8.9, publicado en 11-2025), que Anthropic **sí** parcheó.
- **Corrección**: l. 16: "…llevó a ejecución de código en Claude Desktop al encadenar una extensión con acceso a terminal (LayerX, 02-2026, CVSS 10 autoasignado)". l. 293: sustituir la URL de Akamai (403) por la de The Register. Añadir PromptJacking a la lista de la l. 169-178.

**H-B3 · DISCREPANCY · baja · Fecha del Filesystem MCP**
- **Dice**: "Filesystem MCP de Anthropic (08-2025): escape del sandbox (`reported`)" (l. 173).
- **Verificación independiente** (D04-69, NVD CVE-2025-53109 y CVE-2025-53110): las dos se publicaron el **2025-07-02** (enlaces simbólicos y prefijo de ruta). Afectan a versiones anteriores a 0.6.4 / 2025.7.01, con CVSS 4.0 de 7.3.
- **Corrección**: "Filesystem MCP de Anthropic (07-2025): CVE-2025-53109 y CVE-2025-53110, escape del directorio permitido, CVSS 7.3", con confianza `verified`.

**H-B4 · UNVERIFIABLE · baja · Caducidad del token de WHOOP**
- **Dice**: "Expira en 3600 s" (l. 189).
- **Verificación independiente** (D04-74, https://developer.whoop.com/docs/developing/oauth): la documentación no fija la cifra ("only valid for a short time", según `expires_in`). Lo demás se confirma: refresh con `offline`, invalidación al refrescar, niveles 100/1.000/5.000/ilimitado y webhooks v1 retirados.
- **Corrección**: "Caduca según `expires_in` (corto; la documentación no fija la cifra)".

**H-B5 · INTERNAL · baja · Dos imprecisiones de redacción técnica**
- **Dice**: "más de 14 paquetes transitivos" (l. 159) frente a "14 directas" (l. 63); "desde v2.1.232/v2.1.274" (l. 35).
- **Verificación independiente**: son 14 dependencias **directas** (D04-18, https://pypi.org/pypi/mcp/json; `typing-*` = typing-extensions + typing-inspection, y `httpx2` existe). El runtime v2 es el de por defecto desde v2.1.232 si la sesión descarga flags y desde v2.1.274 si no (D04-08, https://code.claude.com/docs/en/mcp.md).
- **Corrección**: l. 159: "14 dependencias directas, más sus transitivas". l. 35: "(runtime v2 por defecto desde v2.1.232 con flags remotos, v2.1.274 sin ellos; `MCP_PROTOCOL_NEGOTIATION=legacy` lo desactiva)".

**H-B6 · PROVENANCE · baja · El resumen etiqueta más fuerte que el cuerpo**
- **Dice**: el punto 7 (l. 19) es todo `verified`, aunque Apple es `reported` (l. 192) y el precio de Health Auto Export y las fechas de Fitbit están "no verificados". El punto 4 (l. 16) da como `verified` el clon de Oura, cuya única fuente era `reported`. El punto 2 (l. 14) dice "verified (documentación de Claude)" e incluye ChatGPT, que es `reported` (l. 106).
- **Verificación independiente**: ahora casi todo está confirmado por fuente independiente (D04-30, D04-36, D04-47, D04-48), así que el contenido aguanta. El fallo es de procedencia: en el momento de escribir no estaba verificado.
- **Corrección**: alinear las etiquetas del resumen con las del cuerpo, o actualizarlas a `verified` citando las fuentes nuevas de este QA.

**H-B7 · OVERCLAIM · baja · "Solo las tareas locales de Claude Desktop llegan a Ucoach"**
- **Dice**: l. 14.
- **Verificación independiente** (D04-27, D04-23): Cowork tiene "Require this computer" (solo con Computer access en la organización), y un plugin con servidor local carga en Cowork cuando la sesión corre en el equipo (https://claude.com/docs/plugins/platform-support.md). `/loop` de Claude Code también llega (l. 105).
- **Corrección**: "Para un usuario individual, solo las tareas locales de Claude Desktop (y `/loop` con una sesión abierta) llegan a Ucoach. Las de Cowork solo si la organización activa Computer access". La arquitectura no cambia.

**H-B8 · STALE · baja · La Fitbit Web API ya está apagada**
- **Dice**: "**Fechas de cierre de la Fitbit Web API no verificadas**" (l. 191).
- **Verificación independiente** (D04-76, https://developers.google.com/health/migration): el soporte heredado terminó el 30-09-2026, y la API y los endpoints OAuth de Fitbit **se apagan el 02-11-2026**, antes de la fecha del informe. Lo demás se confirma: tope de 100 usuarios, modo personal y `ACCOUNT_NOT_LINKED` (HTTP 400 `FAILED_PRECONDITION`).
- **Corrección**: "Fitbit Web API apagada el 02-11-2026; la única vía es la Google Health API".

**H-B9 · MISSING · baja · Huecos de la tabla que ya se pueden llenar**
- **Dice**: "?" en elicitation para VS Code, Cursor y ChatGPT (l. 49), "?" en anotaciones para VS Code (l. 45), "Sí" sin matiz en MCP Apps para VS Code (l. 53), "precio no verificado" en Health Auto Export y "v10.0" (l. 193).
- **Verificación independiente**:
  - Elicitation: VS Code Copilot la soporta en formulario y URL; Cursor la marca "Supported"; ChatGPT la implica. Claude Code hacia conectores de claude.ai solo declara formulario. claude.ai y Desktop no la mencionan, y Claude dice no soportar "advanced or draft capabilities" (D04-15).
  - Anotaciones en VS Code: solo afectan a la confirmación en el harness Local (D04-13).
  - MCP Apps en VS Code: experimental (D04-16).
  - Health Auto Export: versión actual 10.0.6 (29-10-2026). Descarga gratis; Premium 1,99 $/mes, 6,99 $/año o 24,99 $ vitalicio (D04-48, https://www.healthyapps.dev/, App Store).
- **Corrección**: rellenar esas celdas. En la l. 49, cambiar el "?" de Claude Desktop y claude.ai por "No documentado; la documentación de Claude dice que no soporta funciones avanzadas o en borrador".

**H-B10 · OVERCLAIM · baja · Conclusiones de conectores sin cálculo**
- **Dice**: "Los agregadores solo tienen sentido … con más de 300 usuarios de pago" (l. 202) y Garmin Personal como "la vía más barata y con menos fricción" para la fase 2 (l. 202).
- **Verificación independiente**: los precios confirmados (Terra desde 499 $, Junction 300 $ para 1-500 usuarios; D04-49, D04-50) no producen por sí solos el umbral de 300. La vía Personal de Garmin exige que cada usuario saque su propia clave en Garmin Connect (D04-45), y no se mide esa fricción frente al público no técnico de la fase 2.
- **Corrección**: mostrar el cálculo del umbral (coste mensual entre el margen por usuario) o quitar la cifra, y añadir los pasos que tiene que dar el usuario en Garmin Personal.

**H-B11 · MISSING · baja · Detalles de las tareas locales de Claude Desktop que afectan al brief**
- **Dice**: l. 104 y el diagrama de las l. 121-122.
- **Verificación independiente** (D04-29, https://code.claude.com/docs/en/desktop-scheduled-tasks.md): las tareas locales son sesiones de la **pestaña Code**, con intervalo mínimo de una hora; las herramientas con `requiresUserInteraction` **bloquean** la ejecución; "Keep computer awake" no impide que se duerma al cerrar la tapa.
- **Corrección**: añadirlo a la l. 104 y aclarar en la §3.2 que Ucoach tiene que estar configurado donde lo lee la pestaña Code. Ninguna herramienta que use el brief debe pedir interacción, y eso choca con la P3 de elicitation si se aplica a herramientas del brief.

**H-B12 · MISSING · baja · No consta que Claude Desktop sea dual-era**
- **Dice**: "Hoy sigue funcionando porque los clientes nuevos prueban `server/discover`" (l. 13).
- **Verificación independiente** (D04-08, D04-09): es dual-era confirmado en Claude Code y en los SDK v2 de Python y TS. No se encontró ningún cliente importante solo moderno. Para Claude Desktop, el host de la fase 1.5, no hay dato.
- **Corrección**: "…porque Claude Code y los SDK v2 prueban `server/discover` y vuelven a `initialize`; en Claude Desktop no está documentado".

## Sólido

Verificado de forma independiente y correcto. Que nadie lo "arregle":

- **Protocolo**:
  - 2026-07-28 es la revisión vigente, publicada el 28-07-2026. Elimina `initialize` y las sesiones, pasa a `_meta` por petición con `server/discover` obligatorio, introduce MRTR con `resultType` obligatorio y depreca Roots, Sampling y Logging. Tasks pasa a extensión, y "recurso no encontrado" pasa de -32002 a -32602 (D04-01 a 05, 52).
  - El fallback dual-era funciona como dice la l. 35 (D04-07). Modern → Legacy falla (D04-09). La especificación cita como fallo habitual procesar peticiones sin `initialize` (D04-11).
  - Los cambios de 2025-11-25 son los que lista la l. 31 (D04-12).
  - Las anotaciones aparecieron en 2025-03-26; `outputSchema`/`structuredContent` y `resource_link`, en 2025-06-18 (D04-13, 14, 55).
  - MCP Apps es estable desde el 26-01-2026, no funciona en Claude Code, y en claude.ai necesita servidor remoto y listado Verified (D04-16, 62).
  - La hoja de ruta es del 22-08-2026 (D04-54). Los cambios de OAuth son los citados: CIMD, `iss`, DCR deprecado (D04-60).
- **SDK**: `mcp` 2.3.0 del 02-10-2026, Python ≥3.10, `FastMCP` pasa a `MCPServer`. Tiene exactamente 14 dependencias directas, `httpx2` incluida. Es dual-era desde el mismo servidor, y el proyecto recomendó fijar `<2` (D04-17, 18, 19, 61).
- **MCPB y plugins**: tipo `uv` con manifest 0.4, Python instalado por el host, campos `sensitive` en el Keychain o el Credential Manager, sin sandbox. Los plugins ignoran los MCP locales en el chat de claude.ai y se sincronizan de la cuenta a Claude Code (D04-20, 21, 23, 63).
- **Registro y ChatGPT**: el Registro sigue en preview y no escanea (D04-24). ChatGPT escritorio admite stdio, y los plugins con MCP local solo los publican socios aprobados (D04-26).
- **Proactividad**:
  - Cowork en la nube con "Require this computer" (D04-27).
  - Tareas en la nube de Claude Code (antes *routines*): sin los MCP de `claude mcp add`, intervalo mínimo de 1 h, 100 ejecuciones por hora, research preview (D04-28).
  - Tareas locales de Desktop desde la 1.1.5368, con una recuperación en 7 días (D04-29).
  - Las tareas de ChatGPT sustituyen a Pulse desde el 17-06-2026 (D04-30).
  - cron, launchd `StartCalendarInterval` y `StartInterval` se comportan como dice la l. 108, citado literalmente de `man launchd.plist` (D04-31). Los equivalentes de systemd y Windows también son correctos (D04-32).
  - Telegram no cifra de extremo a extremo los chats con bots (D04-34).
- **Seguridad**: postmark-mcp (09-2025), CVE-2025-49596 (CVSS 9.4), CVE-2025-6514 (crítica, 9.6), OX Security del 15-04-2026 con la respuesta de "expected behavior" de Anthropic, Expat ≥2.7.2, GitHub MCP (05-2025), Smithery con el token de Fly.io, OWASP MCP, Agentic y LLM Top 10, la trifecta letal del 16-06-2025, keyring 25.7.0 y SQLCipher AES-256 con extensión compilada (D04-37 a 41, 64 a 68, 70 a 72).
- **Conectores**:
  - Oura: solo OAuth2, tokens personales deprecados en 12-2025, 10 usuarios sin aprobación, flujo solo cliente, 403 con suscripción caducada, `User-Agent` obligatorio (D04-42, 43, 73).
  - WHOOP: sandbox de 10 miembros y 5 apps (D04-44).
  - Garmin: vía Personal solo *pull*, Starter solo *push* sin histórico, Enterprise (D04-45, 75).
  - Polar: abierto a cualquier usuario de Flow (D04-46). Apple: sin API web (D04-47).
  - Health Auto Export: v10.0 del 09-09-2026 con servidor MCP (D04-48). Junction: 300 $/mes hasta 500 usuarios, sin descuento para startups (D04-50).
  - Google Calendar: URL iCal secreta con Reset (D04-51). Graph: `Calendars.ReadBasic` sin cuerpo del evento (D04-79). Sin RRULE en la librería estándar (D04-80). Telegram Bot API 10.4 (D04-81).

## No verificable

- **WHOOP, 3600 s** (l. 189): la documentación no publica la cifra. Hay que quitarla o citar una respuesta real de la API.
- **Lo que el informe ya declaraba sin verificar** (l. 7): Ultrahuman, Rook, Thryve y Pushover siguen sin verificar, porque no entraron en las preguntas. Hay que verificarlos o sacarlos de la tabla.
- **"12 herramientas" (l. 237) y "seis rituales" (l. 91)** vienen del documento de producto y no se pueden comprobar desde este informe. Habría que contrastarlos con el código o con el Google Doc de la v0.1.
- **Respuesta de Anthropic a OX Security** (l. 67, 178): solo se conoce por la versión de OX (confianza MEDIA). Hay que mantener `reported` en la respuesta, aunque el hecho de la publicación sí está verificado.

## Falta

- Qué hace Claude Desktop (el host de MCPB) con un servidor *legacy*: no está documentado (H-B12).
- En qué configuración MCP lee la pestaña Code las tareas locales, y si un `.mcpb` instalado en Desktop es visible para ellas. El brief de mañana depende de esto (H-B11).
- Si el flujo "solo cliente" de Oura entrega refresh token. Si no lo hace, el usuario tendría que reautorizar a menudo, lo que afecta a la P3 "Oura OAuth (flujo sin secreto)" (l. 248).
- Las implicaciones de seguridad de usar a la vez el servidor MCP de Health Auto Export y Ucoach en la misma sesión: más superficie para la trifecta letal de la amenaza 2.
- El caso PromptJacking de Koi Security (11-2025, parcheado) en la lista de incidentes (H-B2).
- La próxima revisión de MCP, prevista para el 2027-03-30 según el post del 11-11-2026 (D04-54). Sirve para planificar la v0.3.
- La columna de Cursor en anotaciones (sin documentación según el verificador) y otros clientes (Gemini CLI, Windsurf, Zed).
- Una vía de llavero en Linux sin dependencias (hoy depende de `keyring` como extra).

## Correcciones a aplicar en el informe

1. **l. 13**: cambiar "porque los clientes nuevos prueban `server/discover`" por "porque Claude Code y los SDK v2 prueban `server/discover` y vuelven a `initialize` (en Claude Desktop no está documentado)".
2. **l. 14**: matizar "Solo las tareas locales de Claude Desktop llegan" con lo de Cowork "Require this computer" (con Computer access) y `/loop`.
3. **l. 16**: "(LayerX, 02-2026, CVSS 10 autoasignado, encadenando una extensión con acceso a terminal)".
4. **l. 17**: reescribir el punto 5. El `.mcpb` se distribuye como fichero privado (el directorio ya no acepta MCPB) y se actualiza a mano, así que hace falta un aviso de versión propio. El plugin es para Claude Code y Cowork; en el chat de Desktop se ignora.
5. **l. 18**: quitar "(unas pocas funciones)" o remitir a la lista completa de la P0.
6. **l. 19**: cambiar "Terra desde 399-499 $/mes" por "Terra desde 499 $/mes". Añadir "Fitbit Web API apagada el 02-11-2026". Alinear las etiquetas de confianza.
7. **l. 35**: explicar v2.1.232/v2.1.274 y sustituir "la política de desuso da un mínimo de 12 meses" por el texto de H-M2, citando `community/feature-lifecycle.md`.
8. **l. 45, 49, 53**: rellenar VS Code, Cursor y ChatGPT según H-B9. En la l. 49, Claude Desktop y claude.ai pasan a "No documentado".
9. **l. 82**: fila MCPB. Fricción "Baja: doble clic sobre un fichero descargado". Quitar "o directorio", "Actualización automática si está en el directorio" y "Entrar en el directorio exige revisión de Anthropic". Añadir "El directorio ya no acepta MCPB (listados deprecados)" y "hosts: Claude Desktop y Claude Code". Fuente: https://claude.com/docs/connectors/building/mcpb.md.
10. **l. 104**: añadir "sesión de la pestaña Code; intervalo mínimo de 1 h; las herramientas con `requiresUserInteraction` bloquean la ejecución".
11. **l. 136**: reescribir lo de ntfy.sh según H-M5 ("la documentación trata el nombre del tema como una contraseña").
12. **l. 158**: "(Straiker STAR Labs, 17-02-2026; grupo SmartLoader)".
13. **l. 159**: "14 dependencias directas, más sus transitivas".
14. **l. 169-178**: l. 173 pasa a "Filesystem MCP de Anthropic (07-2025): CVE-2025-53109 y CVE-2025-53110, CVSS 7.3". Añadir "PromptJacking, Koi Security (11-2025, CVSS 8.9, parcheado)". En la l. 176, añadir la fecha 17-02-2026.
15. **l. 189**: cambiar "Expira en 3600 s" por "Caduca según `expires_in` (corto; cifra no publicada)".
16. **l. 191**: cambiar "Fechas de cierre … no verificadas" por "Soporte heredado hasta el 30-09-2026; API y OAuth de Fitbit apagados el 02-11-2026".
17. **l. 193**: "v10.0 (09-09-2026), actual 10.0.6 (29-10-2026)"; precio "gratis + Premium 1,99 $/mes, 6,99 $/año o 24,99 $ vitalicio (EE. UU.)"; añadir Home Assistant y Google Drive a los destinos.
18. **l. 196**: "OAuth2; el token caduca (unos 365 días en el ejemplo de la documentación)"; añadir "5.000 + 100×usuarios cada 24 h".
19. **l. 198**: "Desde 499 $/mes (Quick Start), 100.000 créditos"; quitar 399 $ y "unas 500 conexiones activas" salvo que haya fuente.
20. **l. 202**: separar Garmin Personal (sin OAuth) de Polar (OAuth2 con reautorización anual). Justificar el umbral de "300 usuarios de pago" o quitarlo, y describir la fricción de la clave personal de Garmin.
21. **l. 234**: completar la P0 con `ttlMs`/`cacheScope` obligatorios, `serverInfo` en `_meta`, -32022 para versiones no soportadas y -32602 para recursos inexistentes. Revisar el esfuerzo a M.
22. **l. 241**: P1 "Paquete `.mcpb` privado (fuera del directorio) con aviso de versión propio + plugin para Claude Code y Cowork".
23. **l. 244**: cambiar "(sin OAuth complejo)" por "(Garmin sin OAuth; Polar con OAuth2 sencillo)".
24. **l. 293**: sustituir la URL de Akamai (403) por https://www.theregister.com/2026/02/11/claude_desktop_extensions_prompt_injection/.
25. **l. 296**: añadir o sustituir por https://securityaffairs.com/188135/ai/smartloader-hackers-clone-oura-mcp-project-to-spread-stealc-malware.html y el informe de Straiker.
26. **l. 312**: `https://support.google.com/cloud/answer/7454865?hl=en` (bloqueo B1).
27. **l. 319**: `https://support.google.com/calendar/answer/37648?hl=en` (bloqueo B2).
28. **Índice de fuentes**: añadir https://modelcontextprotocol.io/community/feature-lifecycle.md, https://claude.com/docs/connectors/building/mcpb.md, https://claude.com/docs/plugins/platform-support.md (ya está como 20; comprobar la ruta), https://developers.google.com/health/migration (ya está como 48) y las NVD de CVE-2025-49596 y CVE-2025-53109/53110.

## Re-verificación

Fecha: 2026-11-19. Las correcciones se aplicaron con Edit sobre `04-mcp-seguridad-conectores.md`, cambiando solo las frases afectadas. Cada una se apoya en la respuesta del verificador independiente (`qa/D-respuestas.md`) y cita su URL. Las líneas nuevas son las del informe corregido (346 líneas; se han desplazado porque la recomendación de distribución del resumen y del índice de fuentes creció). Las recomendaciones que cambiaron llevan la marca «(corregido tras QA 2026-11-19)».

| hallazgo | estado (corregido / no corregido) | línea nueva |
|---|---|---|
| B1 · enlace 404 de Google Cloud (fuente 49) | corregido: `?hl=en` + página hermana 13464323 | 318 |
| B2 · enlace 404 de Google Calendar (fuente 56) | corregido: `?hl=en` | 325 |
| H-C1 · directorio MCPB cerrado | corregido: resumen, fila MCPB, fila de plugin, fase 1.5, fase 3 y P1 rehechos (chat de Desktop: `.mcpb` privado con aviso de versión propio; Claude Code, pestaña Code y Cowork local: plugin; web y móvil: servidor remoto) | 17-22, 87, 88, 95-97, 247 |
| H-M1 · P0 dual-era incompleta | corregido: `ttlMs`/`cacheScope`, `serverInfo`, -32022, -32602; esfuerzo M; anunciar 2026-07-28 solo tras conformidad | 23, 78, 240 |
| H-M2 · política de 12 meses | corregido: 12 meses para funciones, no para revisiones (fuente 58) | 40 |
| H-M3 · Polar "sin OAuth" y tokens | corregido: OAuth2 con token de unos 365 días, límite de 24 h | 202, 208, 250 |
| H-M4 · Terra 399 $ | corregido: desde 499 $/mes | 24, 204 |
| H-M5 · ntfy "no es una contraseña" | corregido: "essentially a password" (fuente 68), servidor propio recomendado | 141 |
| H-B1 · fecha del clon de Oura | corregido: Straiker STAR Labs, 17-02-2026, SmartLoader | 16, 163, 182, 302 |
| H-B2 · LayerX, fuente bloqueada y PromptJacking | corregido: CVSS autoasignado, vector, The Register; PromptJacking añadido | 16, 160, 181, 299 |
| H-B3 · fecha del Filesystem MCP | corregido: 07-2025, CVE-2025-53109/53110, CVSS 7.3 | 177 |
| H-B4 · WHOOP 3600 s | corregido: según `expires_in`, cifra no publicada | 195 |
| H-B5 · "más de 14 transitivos" y v2.1.232/274 | corregido | 40, 164 |
| H-B6 · etiquetas de confianza del resumen | corregido: ChatGPT como `reported`; Apple, Android, Health Auto Export y Fitbit con fuente consultada y `verified`; incidentes con fuente nueva | 14, 24, 175-184, 198, 200 |
| H-B7 · "solo las tareas locales de Desktop" | corregido: matiz de `/loop` y Cowork con Computer access | 14 |
| H-B8 · Fitbit apagada | corregido: 30-09-2026 y 02-11-2026 | 24, 197 |
| H-B9 · huecos de tabla y Health Auto Export | corregido: anotaciones en Cursor y VS Code, elicitation por cliente, MCP Apps experimental en VS Code, precio y versión 10.0.6 | 50, 54, 58, 199 |
| H-B10 · umbral de 300 usuarios y fricción de Garmin | corregido: umbral sustituido por el criterio de coste fijo; pasos de la clave personal de Garmin descritos | 208 |
| H-B11 · tareas locales de Desktop | corregido: intervalo de 1 h, `requiresUserInteraction`, pestaña Code y plugin | 95, 109, 136 |
| H-B12 · Claude Desktop dual-era | corregido: "en Claude Desktop ese comportamiento no está documentado" | 13 |

Otros cambios de la misma pasada:
- Fuentes 32, 35 y 36 sustituidas o ampliadas (The Register, Security Affairs, OX Security).
- Fuentes 58 a 75 añadidas al índice como «Añadidas tras el QA del 2026-11-19».
- "Hoy sigue funcionando" (l. 13) pasa a "A 19-11-2026" para quitar la fecha relativa.
- Systemd y Windows (l. 114) pasan a `verified` con las fuentes 70 y 71.
- Guiones largos en el informe: 0.

**Nota antes de corregir**: 0.0 / 10 · REHACER (`MAJOR ISSUES`). Penalización de 15: 1 crítica, 5 medias, 12 bajas y 2 bloqueos.

**Nota tras corregir** (nota.py con solo los hallazgos abiertos: 0 críticas, 0 medias, 0 bajas, 0 bloqueos):

```
python3 nota.py --claims 81 --verificadas 81 --portantes 51 --portantes-ok 51 --criticas 0 --medias 0 --bajas 0 --bloqueos 0
Nota QA: 10.0 / 10 · ENTREGABLE
```

Lo que este 10 no cubre, para que se lea bien:
1. Las correcciones las ha comprobado el mismo agente que hizo la comparación, contra las respuestas del verificador. No ha habido una segunda verificación independiente sobre el texto nuevo.
2. La cobertura es de las 81 afirmaciones extraídas, sobre unas 170 verificables.
3. Siguen abiertos, sin contar como hallazgos, los puntos de «No verificable» y «Falta»: Ultrahuman, Rook, Thryve y Pushover sin verificar; si la pestaña Code ve las extensiones `.mcpb`; el refresh token del flujo solo cliente de Oura; y las cifras de 12 herramientas y seis rituales, que vienen del documento de producto.

## Comprobación de la corrección por un tercero (sesión principal, 2026-11-19)

- **Quién corrige no se puede dar el visto bueno a sí mismo.** Las correcciones las aplicó el mismo agente que comparó el mapa con las respuestas. Por eso, desde la sesión principal (que no escribió el informe ni las correcciones) se cotejaron tres de ellas con `qa/D-respuestas.md`: la distribución por MCPB (D04-20, D04-22, D04-23 y D04-25), el precio de Terra (D04-49) y el OAuth de Polar (D04-46 y D04-78). Las tres coinciden con lo que encontró el verificador. Las otras 17 no se han cotejado una a una.
- **Enlaces:** después de corregir, el preflight marca 3 enlaces de support.google.com como 404, pero con curl devuelven 200, tanto con agente de navegador como sin él. Es un falso positivo del cliente HTTP del script, así que no cuentan como bloqueo.
- **Hasta dónde llega el 10.** La nota está calculada sobre las 81 afirmaciones extraídas: todas las portantes y 30 de apoyo. Según el extractor, el informe tiene unas 170 afirmaciones verificables. Las de contexto y el resto de las de apoyo no se verificaron. Lo que la nota afirma es que **todas las portantes están verificadas y no queda ningún hallazgo abierto**, no que el informe entero esté comprobado.
- **Sin verificar, fuera de la nota:** Ultrahuman, Rook, Thryve, Pushover, si la pestaña Code ve los `.mcpb`, el refresh token del flujo solo cliente de Oura y las cifras de 12 herramientas y seis rituales de la v0.1.
