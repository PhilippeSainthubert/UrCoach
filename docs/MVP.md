# Ucoach · Diseño del MVP (v0.2.0)

**Fecha:** 2026-11-19 · **Base:** `producto/documento-producto-v0.2.md` y `research/ucoach-analysis.md`

## Objetivo del MVP

Que Philippe y 20 fundadores puedan usar Ucoach a diario durante la validación (del 18-12-2026 al 18-02-2027). Para eso hacen falta tres cosas:
- el método corregido por el research;
- unos avisos que no dependan de la nube;
- la medición de las métricas de decisión sin telemetría.

## Dentro del MVP

| Pieza | Qué hace | Dónde |
|---|---|---|
| Servidor MCP | stdio y JSON-RPC sin dependencias. Protocolo 2024-11-05 a 2025-11-25; responde `-32601` al instante a los métodos desconocidos, incluido `server/discover`, para que los clientes de la era 2026-07-28 vuelvan a `initialize`. Herramientas con anotaciones, validación estricta y salida estructurada | `ucoach/mcp/` |
| Base local | SQLite en `~/.ucoach` (permisos 0700 y 0600, también WAL y SHM), `audit_log` y `undo` | `ucoach/db.py` |
| Motor del método | Estado de sueño por media de noches, plan del día, contexto, revisión semanal, ergonomía, experimentos n-de-1, auditoría de agenda y derivación fija | `ucoach/core/` |
| Contenido | Catálogo de prácticas A-D, protocolos, derivación, biblioteca, método y palabras que hay que evitar | `ucoach/content/` |
| Avisos | `ucoach nudge`: determinista y sin LLM, con presupuesto de 1 a 3 al día, separación mínima, horas de silencio, `snooze` y «hoy no», aleatorización simple registrada y plantillas sin datos de salud | `ucoach/nudge.py` |
| Planificador | `ucoach schedule install`: launchd, systemd `--user` con `Persistent=true` o la orden de `schtasks` | `ucoach/schedule.py` |
| Canales | Notificación del sistema (por defecto), ntfy o Telegram, con el token en el llavero | `ucoach/channels.py` |
| Importadores | Apple Health (en streaming, rechaza DTD con entidades) y CSV | `ucoach/importers/` |
| Medición | `ucoach stats`: resumen semanal anónimo que el usuario pega en un formulario | `ucoach/stats.py` |
| Lint de textos | `ucoach lint-textos`: busca en cualquier texto las frases de la lista del informe 05 | `ucoach/lint.py` |
| Plugin de Claude Code | MCP, skills de los rituales y agentes (coach, curador de evidencia y revisor de textos) | `.claude-plugin/`, `.mcp.json`, `skills/`, `agents/` |

## Fuera del MVP (y por qué)

| Pieza | Motivo | Cuándo |
|---|---|---|
| Era 2026-07-28 completa (`server/discover`, `resultType`, `ttlMs`…) | El research recomienda anunciarla solo cuando pasen las pruebas de conformidad con la especificación delante | v0.3 |
| Paquete `.mcpb` para el chat de Claude Desktop | Necesita un aviso de versión propio y firma | v0.3 |
| Conectores directos (Polar, Garmin) | Primero hay que validar; la IA ya pasa los datos de otros MCP | Tras la validación |
| MCP Apps y panel | No funcionan en Claude Code; antes va el informe HTML | v0.4 |
| Servidor remoto, sincronización y app móvil | Responsabilidad del tratamiento de datos de salud (art. 9) | Solo si la validación lo pide |
| Motor de avisos que aprende (bandit) | Lo convertiría en sistema de IA (art. 50) | No previsto |

## Criterios de aceptación

1. `python3 -m unittest` pasa sin dependencias externas.
2. Claude Code arranca el servidor con `claude mcp add ucoach -- python3 -m ucoach serve`, o como plugin, y lista las herramientas, los prompts y los recursos.
3. Con 5,2 h de sueño y una negociación a las 9:00, `planificar_dia` propone:
   - un bloque de foco de 60 min;
   - preparar la reunión clave;
   - una siesta antes de las 15:00;
   - entreno sin esfuerzos máximos;
   - el último café 9 h antes de dormir;
   - el aviso de las decisiones irreversibles.
4. `ucoach nudge` nunca envía más de lo que marca el presupuesto, nunca dos avisos en 60 min, nunca durante el foco ni en horas de silencio, y ningún aviso lleva cifras de salud ni títulos de reuniones.
5. `ucoach lint-textos` pasa sin hallazgos sobre `ucoach/content/` y sobre los textos de las herramientas y los prompts.
6. Cero guiones largos en el contenido.

## Decisiones de diseño

- **Nombre:** `ucoach` es el nombre en clave del paquete. Cambiarlo a Circalia cuando se confirme la marca es un renombrado mecánico.
- **Sin LLM en el servidor:** todas las reglas son deterministas. La conversación la pone la IA del usuario guiada por `metodo.md` y los prompts.
- **La IA aporta el calendario:** Ucoach no pide credenciales. Las reuniones que llegan a `planificar_dia` se guardan con su hora, su marca de clave y un título truncado que nunca sale por los canales de aviso.
- **Datos mínimos al exterior:** las herramientas devuelven resúmenes por defecto (`detalle: true` para ver más). No hay telemetría.
