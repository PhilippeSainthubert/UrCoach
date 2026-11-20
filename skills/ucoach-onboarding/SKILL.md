---
name: ucoach-onboarding
description: Instala y configura Ucoach la primera vez. Conecta el servidor MCP, explica «Tu IA y tus datos», configura el perfil, el hábito focal y la ergonomía, e instala los avisos con launchd o systemd. Úsala cuando el usuario diga «instala Ucoach», «empezar con Ucoach» o «configura mi coach».
---

# Onboarding de Ucoach

## 1. Instalación (Claude Code)

- Como plugin: el repositorio ya trae `.claude-plugin/plugin.json` y `.mcp.json`.
- Sin plugin: ejecuta `python3 -m ucoach config` desde la carpeta del repositorio y sigue la orden `claude mcp add` que imprime.
- Requisito: Python 3.10 o superior. No hay dependencias.

## 2. Tu IA y tus datos

Lee el recurso `ucoach://privacidad` y explícalo en 3 líneas:
- los datos viven en `~/.ucoach`;
- lo que consulta la IA lo procesa su proveedor;
- cómo desactivar en su IA el uso de sus conversaciones para entrenar.

## 3. Perfil

Una pregunta por mensaje, con `perfil`:
- horas de despertar y de dormir;
- horario de trabajo;
- cronotipo (alondra, intermedio o búho);
- si entrena y cuándo;
- hasta 3 objetivos;
- si le cuesta dormir de forma habitual (`dificultad_dormir`: si es así, Ucoach no propondrá siestas);
- palabras que marcan sus reuniones clave;
- su rutina previa a un momento importante (3 pasos).

## 4. Hábito focal

Uno solo, con su ancla («después de...») y su versión de 2 minutos, mejor por la mañana. Defínelo con `definir_habito` y `focal: true`.

## 5. Ergonomía

Usa `chequeo_ergonomia`: primero las preguntas y después las respuestas. Una sola mejora para empezar.

## 6. Avisos

Explica cómo funcionan:
- de 1 a 3 al día;
- nunca durante el foco ni en las horas de silencio;
- se pueden parar con `ucoach hoy-no` y `ucoach snooze`;
- no llevan datos de salud.

Después:
- ejecuta `python3 -m ucoach schedule install` y, con su permiso, `--load`;
- canal: por defecto, la notificación del sistema;
- si prefiere Telegram, el token va al llavero (`security add-generic-password -a "$USER" -s ucoach-telegram -w`) y el `telegram_chat_id`, al perfil.

## 7. Brief automático (opcional)

En Claude Desktop, crea una tarea programada **local** (pestaña Code) a las 7:30 en días laborables, con el texto «Haz mi brief de mañana con Ucoach». Las tareas en la nube no llegan a Ucoach. Si el equipo está dormido, el aviso de las 9:00 recuerda abrir el brief.
