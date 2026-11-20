# Ucoach

*Nombre en clave. Propuesta de nombre definitivo: Circalia (pendiente de comprobar la marca).*

Coach de excelencia profesional para fundadores, que cuida la energía y el sueño como base del trabajo. Vive dentro de la IA que ya usas: es un servidor MCP local, en Python estándar y sin dependencias. Cruza tu agenda y tu trabajo con tu sueño, tu energía y tus hábitos, y te dice cómo jugar el día. Cada pauta lleva su nivel de evidencia (A recomendable, B opcional, C experimental, D no recomendar).

> Ucoach es una herramienta de bienestar y organización personal para adultos sanos. No está destinada a diagnosticar, tratar, curar, aliviar ni prevenir ninguna enfermedad, y no es un producto sanitario. Ante síntomas o dudas de salud, consulta a un profesional.

## Instalación

Requisito: Python 3.10 o superior.

```bash
git clone <repo> ~/Ucoach && cd ~/Ucoach
python3 -m ucoach config        # imprime la orden para Claude Code y el bloque para otros clientes MCP
```

**Claude Code como plugin:** el repositorio es un plugin. Incluye `.claude-plugin/plugin.json`, `.mcp.json`, las skills de los rituales y tres agentes (coach, curador de evidencia y revisor de textos).

**Claude Code sin plugin:**

```bash
claude mcp add ucoach -e PYTHONPATH=$HOME/Ucoach -- python3 -m ucoach serve
```

Después, abre tu IA y pide: «configura Ucoach» (skill `ucoach-onboarding` o prompt `onboarding`).

## Uso diario

| Momento | Qué hacer |
|---|---|
| Mañana | «Haz mi brief». Revisa el sueño y la agenda, pregunta tu destacado y su obstáculo, y propone el día |
| Antes de un momento clave | «Prepárame la negociación de mañana» |
| Noche | «Cierre del día». En 5 minutos: destacado, avance, energía y apagado del trabajo |
| Domingo | «Revisión semanal». GROW con tus datos y un solo ajuste del hábito focal |
| Tras unos días sin usarlo | El ritual `retomar`: vuelta sin culpa, sin rachas |

## Avisos proactivos (sin nube)

```bash
python3 -m ucoach schedule install --load   # launchd en macOS, systemd en Linux
python3 -m ucoach nudge --dry-run           # qué enviaría ahora y por qué
python3 -m ucoach hoy-no                    # hoy sin avisos (no cuenta como fallo)
python3 -m ucoach snooze 2                  # silencio 2 horas
```

Así funcionan:
- de 1 a 3 avisos al día, nunca más de 4 ni dos en la misma hora;
- nunca durante el foco, las reuniones, las horas de silencio o los días libres;
- las plantillas son fijas: no llevan datos de salud ni títulos de reuniones;
- el canal por defecto es la notificación del sistema. Opcionalmente, ntfy o Telegram, con el token en el llavero:

```bash
security add-generic-password -a "$USER" -s ucoach-telegram -w   # macOS; después: perfil telegram_chat_id
```

## Datos

- **Importar:**
  - `python3 -m ucoach import-apple export.xml`: Apple Health, en streaming; rechaza ficheros con entidades XML.
  - `python3 -m ucoach import-csv datos.csv`: Oura, Garmin, WHOOP o cualquier otro exportado a CSV.
- **Dónde viven:** en `~/.ucoach`, con permisos solo para tu usuario. No hay servidores de Ucoach ni telemetría.
- **Quién los ve:** lo que consulta tu IA lo procesa tu proveedor de IA según sus condiciones.
- **Deshacer:** `python3 -m ucoach undo` deshace la última escritura.
- **Validación:** `python3 -m ucoach stats` genera el resumen anónimo semanal.

## Desarrollo

```bash
python3 -m unittest                 # pruebas
python3 -m ucoach lint-textos       # frases que hay que evitar (frontera de producto sanitario y publicidad sanitaria)
```

Las convenciones están en `skills/ucoach-desarrollo/SKILL.md`, el diseño del MVP en `docs/MVP.md`, el producto en `producto/documento-producto-v0.2.md` y la evidencia en `research/`.

## Estructura

```
ucoach/
  mcp/        servidor stdio, herramientas (17), prompts (10), recursos
  core/       sueño, planificador, contexto, revisión, ergonomía, agenda, experimentos, derivación
  content/    prácticas A-D, derivación, biblioteca, método, protocolos, palabras que hay que evitar
  nudge.py    avisos deterministas · channels.py · schedule.py · stats.py · lint.py
  importers/  Apple Health y CSV
skills/       rituales y desarrollo (plugin de Claude Code)
agents/       coach, curador-evidencia, revisor-textos
tests/        unittest, sin dependencias
```
