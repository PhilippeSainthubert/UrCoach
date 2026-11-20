---
name: ucoach-revision-semanal
description: Revisión semanal de Ucoach con GROW y datos propios. Mantiene el mismo hábito focal hasta que sea automático (8-10 semanas como referencia) y propone un solo ajuste. Úsala los domingos o cuando el usuario diga «revisión semanal», «cómo fue la semana» o «qué cambio para la semana que viene».
---

# Revisión semanal

1. Llama a `revision_semanal`. Usa solo las métricas activas del usuario (3 como máximo).
2. Sigue GROW, una pregunta por mensaje:
   - **Goal:** «¿Qué quieres que sea distinto el viernes que viene?»
   - **Reality:** «Del 1 al 10, ¿dónde estás? ¿Qué hace que sea un X y no dos puntos menos?»
   - **Options:** «¿Qué funcionó la última vez que te pasó algo parecido?»
   - **Will:** «¿Qué vas a hacer exactamente, cuándo y dónde?» y «Del 1 al 10, ¿cuánta confianza tienes?»
3. **Hábito focal.** No cambies de hábito cada semana. Propón un solo ajuste: hacerlo más pequeño, mover el ancla o cambiar la hora. A partir de la semana 8, mide la automaticidad con `definir_habito` (`srbai`: 4 respuestas de 1 a 7). Solo con el hábito automatizado se elige uno nuevo, a ser posible en lunes o a principio de mes.
4. **Datos.**
   - Habla de «5 de 7», nunca de rachas rotas.
   - Muestra la energía según el sueño solo si la herramienta dice que hay datos suficientes, y como asociación, nunca como causa.
5. **Libro.** Si el libro sugerido encaja, ofrécelo con su acción y su aviso, si lo tiene.

Una vez al mes, añade la auditoría de agenda (prompt `auditoria_agenda`).
