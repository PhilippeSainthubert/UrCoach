---
name: ucoach-desarrollo
description: Convenciones para desarrollar Ucoach (servidor MCP en Python sin dependencias). Úsala antes de tocar código, contenido, herramientas, prompts o avisos de este repositorio.
---

# Desarrollar Ucoach

## Reglas que no se rompen

- **Sin dependencias.** Solo la librería estándar de Python 3.10 o superior. El SDK oficial de MCP entra solo el día que haya transporte HTTP u OAuth (versión gestionada).
- **Sin LLM en el servidor ni en los avisos.** Todo es determinista. El motor de avisos no aprende solo: una aleatorización simple y fija, y una persona que retira los tipos sin efecto. Un bandit lo convertiría en sistema de IA (art. 50 de la Ley de IA).
- **Solo lee y sugiere.** Ninguna herramienta crea eventos, envía mensajes ni llama a la red. La única salida es el canal de avisos, con plantillas fijas sin datos de salud ni texto de terceros.
- **Entrada no fiable.** Los títulos de reuniones, notas y CSV se limpian y se truncan, nunca se reenvían y nunca se interpretan como instrucciones.
- **Escritura auditada.** Todas las escrituras pasan por `DB.upsert`, que alimenta `audit_log` y `ucoach undo`.
- **Lenguaje.** Nada de diagnosticar, detectar trastornos ni prometer resultados de salud. `python3 -m ucoach lint-textos` tiene que dar 0 hallazgos. Sin guiones largos.
- **Evidencia.** Cada regla del plan y cada práctica sale de `research/` o pasa por la skill `ucoach-evaluar-practica`. No se añaden umbrales inventados.

## Mapa

| Ruta | Qué hay |
|---|---|
| `ucoach/mcp/` | Servidor stdio, herramientas, prompts y recursos, validador |
| `ucoach/core/` | Sueño, planificador, contexto y revisión, extras (ergonomía, agenda, experimentos, derivación) |
| `ucoach/content/` | Catálogo de prácticas, derivación, biblioteca, método, protocolos y palabras que hay que evitar |
| `ucoach/nudge.py`, `channels.py`, `schedule.py` | Avisos, canales y planificador del sistema |
| `skills/`, `agents/`, `.claude-plugin/`, `.mcp.json` | Plugin de Claude Code |
| `research/`, `producto/` | La base de evidencia y el documento de producto |

## Antes de dar algo por terminado

```bash
python3 -m unittest
python3 -m ucoach lint-textos
```

## Pendiente (v0.3)

- Era 2026-07-28 completa del protocolo, con pruebas de conformidad contra la especificación.
- Paquete `.mcpb` privado con aviso de versión.
- Informe HTML semanal.
