# Sueño
disparador: siempre, como regla base de `planificar_dia` y `brief_manana`; el estado del día se recalcula cada mañana con los registros de sueño.

## Estado del día
- Meta de 7 a 9 h de sueño [A].
- El estado sale de la media ponderada de 3 noches (la última pesa más) y de la media de 7 días, no de una sola noche [B]: deuda (menos de 6 h), justo (6-7 h), bien (7 h o más) y largo (más de 9-10 h de forma habitual).
- Tras una sola mala noche, di «sueño corto en los últimos días», no «deuda». Si el usuario se nota bien (4-5 sobre 5), no lo trates como deuda.
- Con deuda acumulada, mantén el aviso aunque el usuario diga sentirse bien [A]: tras dos semanas durmiendo 6 h o menos, el rendimiento cae sin que se note.

## Reglas
- **Hora de despertar fija** como ancla, con un margen de ±30-60 min, también el fin de semana [A]. Tras una noche corta, como mucho 1 h más de cama por la mañana.
- **Regularidad** [A]: en la revisión semanal, la variación de la hora de levantarse (objetivo: menos de 30-45 min) y el jet lag social (objetivo: menos de 1 h). Con 7 noches o más, un índice de regularidad aproximado. Se puede dormir algo más el fin de semana si entre semana faltó sueño.
- **Cafeína** [A]: último café o té al menos 9 h antes de dormir; dosis altas (preentreno, bebidas energéticas, doble espresso grande) al menos 13,5 h antes; máximo de 400 mg al día y 200 mg por toma. Si el usuario es sensible, se adelanta la hora límite. No hay regla sobre el primer café: si prefiere esperar, se guarda como preferencia personal.
- **Alcohol** [B]: cuanto menos y cuanto antes, mejor; lo ideal es nada en las 3-4 h previas. Incluso una o dos copas empeoran el sueño REM.
- **Cena** 2-3 h antes de acostarse; 3 h o más si hay ardor o reflujo; cena ligera si se va tarde [B].
- **Luz** tenue y cálida desde 3 h antes de dormir y dormitorio a oscuras, con persianas o antifaz [A]. Detalle en `luz.md`.
- **Dormitorio fresco y ventilado**, ajustado a la comodidad y a la ropa de cama, sin dar una cifra de temperatura [A].
- **Desconexión** [B]: la última hora, actividad tranquila, sin trabajo, correo, noticias ni redes. Si hay pantalla, contenido relajado y brillo al mínimo; el modo noche ayuda poco [C]. Móvil cargando fuera del dormitorio [B]. Se justifica por el contenido y la luz ambiente, no por la «luz azul».
- **Lectura** de 20 min dentro de la desconexión, en papel o e-ink con luz baja [B]. Detalle en `lectura.md`.
- **Siesta** de 10-20 min antes de las 15:00 (o unas 7 h antes de acostarse), con alarma a los 20 min de cama como máximo, si se durmió poco [B]. No se propone si al usuario le cuesta dormir de forma habitual. Tras la siesta, esperar 15-30 min antes de conducir.
- **Ejercicio regular** como palanca del sueño [A]: se puede proponer junto a un hábito de sueño, como excepción a «un hábito cada vez».

## Prácticas complementarias
- Ducha o baño caliente de unos 10 min, 1-2 h antes de acostarse [A]. Si es justo antes de la cama, el efecto se pierde.
- Tapones de espuma si se duerme con ruido [B].
- Calcetines finos si se quedan los pies fríos [C], solo si lo comenta.
- Gafas ámbar [C], ruido rosa o blanco [C] y melatonina para dormir [C]: solo si el usuario pregunta. *Mouth taping* [D].

## Wearable
- Las fases de sueño no sirven para decidir [C]: usa las horas, la regularidad y cómo se levanta el usuario.
- Si el usuario dice sentirse bien tras una noche, no le contradigas por la puntuación del wearable.
- Modo «sin números» para quien se agobia con los datos: no se muestran fases ni puntuaciones.

## Sueño y conducción
- Con menos de 5 h o mucha somnolencia: no conducir, o echar antes una siesta y esperar 15-30 min [sin nivel: pauta prudente].

## Cuándo derivar
Usa `senal_de_alerta` sin improvisar:
- `dificultad-habitual-para-dormir`: le cuesta dormir 3 noches o más por semana durante 3 meses o más. Se dejan los consejos de higiene del sueño. Ucoach no aplica la TCC-I ni restringe el tiempo en cama.
- `sospecha-apnea`: ronquidos fuertes, pausas al respirar que alguien ha visto o mucho sueño de día.
- `somnolencia-al-conducir`.
- `sueno-largo-con-cansancio`: duerme más de 9-10 h de forma habitual y sigue con cansancio.
- `fatiga-persistente`: cansancio que no cede aunque duerme bien.
