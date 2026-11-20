---
name: ucoach-cierre
description: Cierre del día de Ucoach en 5 minutos como máximo. Registra si se cumplió el destacado, en qué se avanzó y la energía, y hace el apagado del trabajo (qué queda abierto y cuándo se retoma). Úsala cuando el usuario diga «cierre», «cerrar el día», «fin de jornada» o cuando la lance una tarea local por la tarde.
---

# Cierre del día

Una pregunta por mensaje, con la herramienta del servidor `ucoach`:

1. «¿Cumpliste el destacado de hoy?» (sí, parcial o no). Sin juicio.
2. «¿En qué avanzaste hoy, aunque sea poco?»
3. «Energía de 1 a 5.» Llama a `registrar_checkin` con `momento: "cierre"`, `destacado_cumplido` y `energia`. Si lo cuenta, añade `minutos_foco` y `trabajo_tras_hora_fin`.
4. **Apagado:** «¿Qué queda abierto y cuándo lo retomas?» Que lo apunte donde suele hacerlo. Así se reduce la rumiación por la noche.
5. Si hizo el hábito focal, llama a `registrar_habito`.

**Qué no hacer en el cierre:**
- No propongas mejoras ni hábitos nuevos.
- Si fue un mal día, pregunta solo qué necesita para descansar.
- Si mañana no hay brief, lo que quede abierto en el apagado sirve como destacado de mañana.
