# Ucoach · Síntesis del research

**Fecha:** 2026-11-19
**Para:** Philippe, fundador de Ucoach (nombre en clave; propuesta de nombre: Circalia)
**Base:** ocho informes de investigación (`01` a `08`), cada uno verificado por un QA independiente y corregido después (ver el apartado 11), más la búsqueda de nombre (`09-nombre.md`). Cada dato de esta síntesis sale de esos informes; la fuente primaria está en el índice del informe que se cita entre paréntesis.

---

## Resumen ejecutivo

**Ucoach tiene sitio, pero no donde lo situaba la v0.1.** Cruzar la agenda con el sueño ya lo hacen otros: Lifestack, Rise y athletedata. Además, Claude y ChatGPT leen Apple Health en EE. UU. y Google Health Coach funciona en España con Fitbit o Pixel Watch (`01`). Lo que nadie ofrece es un **método explícito, con niveles de evidencia y memoria longitudinal, que cruce agenda, trabajo y cuerpo, independiente del wearable y de la IA**. Ese es el producto: un coach de excelencia profesional que cuida la energía y el sueño como base del trabajo, no un conector de datos.

Las ocho decisiones que salen del research:

1. **Posicionamiento:** capa de método, no de datos. «Vender rendimiento, entregar salud» (`03`, `08`). Los conectores de wearables se están volviendo un bien común (`01`, `06`).
2. **El método cambia en serio** (`02`, `07`, `08`):
   - **Se quitan** las reglas sin base: el primer café a los 75 minutos y el bloque de 90 minutos justificado por el ciclo ultradiano.
   - **Se corrigen** otras: último café al menos 9 h antes de dormir; luz tenue desde 3 h antes; clasificar el sueño por la media de 3 a 7 noches; mantener un mismo hábito 8 a 10 semanas.
   - **Se añaden** la derivación a la TCC-I (Ucoach no la aplica) y una tabla fija de derivación, el brief con obstáculo y plan si-entonces, el ritual de apagado, la preparación de momentos clave y una regla contra la complacencia.
   - **Cada práctica lleva nivel A, B, C o D.** La osteopatía estructural queda en B (solo con ejercicio), la craneal y la visceral en D, el grounding en D y las gafas de luz azul de día en D.
3. **La retención se decide el día después de fallar** (`03`). Por eso: sin rachas que se ponen a cero, con un ritual de vuelta sin culpa, con avisos que se retiran cuando el hábito se automatiza y con un presupuesto de 1 a 3 avisos al día.
4. **La proactividad no puede depender de la IA** (`04`). Las tareas programadas en la nube de Claude y ChatGPT no llegan a un servidor local. Los avisos los dispara el sistema operativo (launchd y equivalentes) con plantillas fijas, y el brief va como tarea local de Claude Desktop.
5. **Técnica v0.2** (`04`): un núcleo sin dependencias compatible con las dos eras del protocolo MCP (2025-11-25 y 2026-07-28). La entrada del calendario se trata como no fiable. Se distribuye como `.mcpb` privado para el chat de Claude Desktop y como plugin para Claude Code y Cowork en local.
6. **Hay que reescribir la promesa de privacidad** (`05`). «Tus datos de salud no salen de tu máquina» es falso, porque pasan por el proveedor de IA y por Telegram. La validación con 20 personas ya trata datos de salud y necesita consentimiento explícito. Hay una lista de palabras que evitar para no entrar en el terreno del producto sanitario. El plan Equipos, tal como está, no es viable.
7. **Negocio** (`06`): el contenido como motor, un programa de 30 días por cohortes como primer ingreso y un plan Coach para coaches humanos como negocio recurrente (hipótesis H3, pendiente de analizar las herramientas que ya usan los coaches). Las aceleradoras sirven para escalar. El Pro individual queda aparcado hasta tener datos de retención.
8. **Nombre:** «Ucoach» solo sirve como nombre en clave. Existe la marca UCOACH registrada en EE. UU. en clases 35, 41, 42 y 45, y los dominios principales están ocupados. La propuesta es **Circalia**: .ai, .app, .coach y getcircalia.com están libres, y no hay ninguna app con ese nombre (`09`). Falta buscar la marca a mano en EUIPO y OEPM.

**El hallazgo no obvio.** Los tres informes que miraron el problema desde lugares distintos llegan a la misma conclusión: **lo valioso de Ucoach es lo que no se puede automatizar en un conector**.
- El método con evidencia graduada (`01`).
- La conversación sin culpa tras una recaída (`03`).
- La persona que pide cuentas, que en el negocio se traduce en coaches humanos dispuestos a pagar por ver el progreso de sus clientes entre sesiones (`06`).

Las plataformas regalan los datos y los avisos. Ucoach tiene que cobrar por el criterio.

---

## 1. Qué cambia respecto a la v0.1

| La v0.1 dice | Lo que encontró el research | Decisión para la v0.2 | Informe |
|---|---|---|---|
| «Ninguna pieza cruza la agenda real con el sueño, la energía y los hábitos» | Falso: Lifestack, Rise y athletedata ya lo hacen | Diferenciarse por el método con evidencia graduada y el contexto de trabajo | 01 |
| Mercado de 5.800 M$ (Virtue Market Research) | La ficha de Virtue no publica esa cifra; solo la cita un blog con enlaces de afiliado | Quitar la cifra. Usar los 5.340 M$ de ingresos del coaching (ICF 2025) como contexto o hacer un cálculo de abajo arriba | 01 |
| «OpenAI confirmó la incorporación del creador de OpenClaw» | Cierto, con matiz: el proyecto pasa a una fundación, OpenAI no lo compra | Matizar | 01 |
| «Fitbit AI Coach, en vista previa» | Desde el 19-5-2026 es Google Health Coach, disponible para todos e incluido en Google AI Pro | Actualizar | 01 |
| «Sin que tus datos de salud salgan de tu máquina» | Falso: pasan por el proveedor de IA y por Telegram | «Sin servidores de Ucoach: tus datos viven en tu ordenador y solo los ve la IA que tú eliges» | 05 |
| Primer café ~75 min después de despertar | Sin ensayos que lo respalden | Quitar | 02 |
| Último café 8 h antes de dormir | Gardiner 2023: al menos 8,8 h para un café y 13,2 h para un preentreno | Al menos 9 h y al menos 13,5 h para dosis altas, con un límite de 400 mg al día | 02 |
| Estado del día según la última noche (<6 / 6-7 / ≥7 h) | Una sola noche es frágil; la regularidad predice mejor que la duración (observacional) | Media de 3 a 7 noches, un nivel «largo» (>9-10 h) e índice de regularidad | 02 |
| Bloque de foco de 90 min por el cronotipo | El ciclo ultradiano de 90 min no está demostrado en vigilia; la sincronía con el cronotipo es irregular | Bloque de 60 a 120 min, situado con los check-ins del propio usuario | 02 |
| Pausa activa de 5 min cada 60-90 min, como aviso | Las micropausas cada ~30 min tienen beneficio metabólico en adultos con sobrepeso u obesidad; los avisos de «levántate» no tuvieron efecto detectable | Micropausas dentro del plan y del bloque, sin aviso. Avisos de movimiento solo ligados a un contexto (ver el apartado 8) | 02, 03 |
| Regla 20-20-20 | Heurística con evidencia escasa y contradictoria | Recordatorio opcional, sin decir que está probada | 02, 07 |
| Desconexión de 60 min «por la luz azul» | El consenso NSF 2024 no se pone de acuerdo sobre la luz de las pantallas en adultos | Justificarla por el contenido y la luz ambiente: bajar la luz desde 3 h antes y dormitorio a oscuras | 02 |
| Revisión semanal: un cambio nuevo cada semana | La automatización de un hábito tiene una mediana de unos 2 meses | El mismo hábito focal durante 8 a 10 semanas o hasta que sea automático (SRBAI) | 02, 03 |
| Avisos proactivos cada 30 min | Revisar cada 30 min está bien; enviar cada 30 min, no. El efecto de un aviso se gasta en unas 4 semanas | Presupuesto de 1 a 3 avisos al día, avisos que se retiran y opción de «hoy no» | 03 |
| Cron cada 30 min | cron pierde las ejecuciones con el equipo dormido | launchd (`StartCalendarInterval`), systemd con `Persistent=true` o el Programador de tareas | 04 |
| «Tareas programadas de la IA» para el brief | Las de la nube no llegan a un servidor stdio local | Tarea local de Claude Desktop, con `nudge` de respaldo | 04 |
| Compatible con MCP de 2024-11-05 a 2025-11-25 | La especificación vigente es la 2026-07-28 (sin `initialize`); Ucoach es *legacy* | Servidor dual-era con pruebas de conformidad | 04 |
| Pro: conectores Oura, Garmin y Whoop | Hay proyectos MIT activos y conectores verificados en el directorio de Claude; Garmin congeló las altas nuevas en 2026 y Oura eliminó los tokens personales | Aceptar datos de cualquier MCP de wearables a través de la IA; conectores propios solo después de validar | 01, 04, 06 |
| Equipos: «informes agregados y anónimos» | Con 2 a 5 personas no hay anonimato; inferir el estrés de trabajadores está prohibido (Ley de IA, art. 5.1.f) | Compartir normas y calendario, nunca datos de salud | 05 |
| Métricas: >40 % de activos a 4 semanas, NPS >40 | Bajo para una cohorte guiada, alto para instalaciones orgánicas; con 20 personas el NPS apenas significa nada | Ver las métricas del apartado 7 | 03 |

---

## 2. Posicionamiento y nombre

**Qué es:** un coach de excelencia profesional para fundadores y directivos, que cuida la energía y el sueño como medio para trabajar mejor. Vive dentro de la IA que el usuario ya usa y trabaja con cualquier wearable.

**Con qué se diferencia** (`01`, apartado 5):
1. Un método explícito y auditable, con el nivel de evidencia de cada práctica. Ningún competidor encontrado publica sus reglas ni su grado de evidencia.
2. Contexto de trabajo profundo: reuniones clave, cadenas de reuniones sin pausa, preparación de momentos clave y auditoría de la agenda. Ningún wearable lee el calendario de forma nativa.
3. Independiente del dispositivo y del proveedor de IA.
4. Local por defecto, sin servidores propios ni dependencias, y con seguridad por diseño.
5. En Europa y en español. Es una ventaja temporal, no un foso: Google Health Coach y Oura Advisor funcionan en España, aunque ninguno mira la agenda, y, a noviembre de 2026, ChatGPT y Claude no leen datos de salud en Europa.

**Lo que no diferencia** (`01`): «contexto cruzado» como algo único, «vive dentro de tu IA» (otros conectores también) y la biblioteca de 103 libros como catálogo. La biblioteca vale cuando se conecta con el hábito más flojo de la revisión semanal.

**Mensaje** (`03`, `05`, `06`): vender rendimiento («organiza tu día para llegar con energía a lo importante») sin prometer resultados de salud. La frase de ejemplo de `03` («llega a la negociación de mañana con energía») queda pendiente de revisión jurídica. El RD 1907/1996 prohíbe atribuir a un método con pretendida finalidad sanitaria la capacidad de «potenciar el rendimiento físico o psíquico». Ver la lista de alternativas seguras en `05`, apartado 4.

**Nombre** (`09`, `06`): «Ucoach» choca con la marca UCOACH registrada en EE. UU. (USPTO 3536981, clases 35, 41, 42 y 45; `reported`, markinton.com), con apps «U-Coach» y «UCOACH» y con ucoach.com, ucoach.io y ucoach.ai. **Circalia** viene de «circadiano», se pronuncia bien en varios idiomas y tiene .ai, .app, .coach y getcircalia.com libres a 2026-11-19. circalia.com está registrado desde febrero de 2026 sin web.

Antes de decidir:
1. Buscar la marca a mano en TMview y en la OEPM (clases 9, 41, 42 y 44).
2. Comprobar el precio real de los dominios.
3. Probar si 5 personas del público lo recuerdan al día siguiente.

---

## 3. El método

### 3.1 Reglas del plan del día (corregidas)

| Regla | v0.2 | Nivel | Informe |
|---|---|---|---|
| Sueño | Meta de 7 a 9 h. Estado según la media de 3 a 7 noches, con nivel «largo». Regularidad y jet lag social calculados con los registros propios. Tras una noche, la sensación subjetiva manda sobre la puntuación del wearable; con deuda acumulada, el aviso se mantiene aunque el usuario diga sentirse bien | Sólido | 02, 08 |
| Hora de despertar | Fija, con un margen de ±30-60 min. Es el ancla del día | Sólido | 02 |
| Luz | 10-20 min de luz exterior en la primera hora y media, y toda la luz natural posible durante el día. Luz tenue desde 3 h antes de dormir y dormitorio a oscuras | Sólido o razonable | 02 |
| Cafeína | Último café al menos 9 h antes de dormir; dosis altas, al menos 13,5 h; máximo de 400 mg al día. Sin regla sobre el primer café | Sólido | 02 |
| Siesta | 10-20 min antes de las 15:00 si se durmió poco. Nunca si hay quejas de insomnio ni antes de conducir | Razonable | 02 |
| Bloque de foco | De 60 a 120 min en el pico que marquen los check-ins del propio usuario tras 2-3 semanas. Una meta clara por bloque y ningún aviso durante el bloque | Razonable | 02, 08 |
| Reuniones | Alerta con 2 h o más seguidas (el estudio de Microsoft es exploratorio, n=14). Reuniones de 25 o 50 min como norma de agenda | Razonable | 02 |
| Movimiento | Micropausas de 2-3 min cada ~30 min dentro del plan (evidencia en adultos con sobrepeso u obesidad), una pausa de 5-10 min cada 60-90 min y un objetivo de 7.000-8.000 pasos que sube poco a poco | Sólido o razonable | 02 |
| Entreno con poco sueño | No cancelar. Evitar los esfuerzos máximos o muy técnicos por la tarde. La VFC solo como señal secundaria, con una línea base de 7 días | Razonable | 02, 07 |
| Comida | Comer antes de las 15:00 cuando se pueda, con horarios regulares. Cenar 2-3 h antes de dormir (3 h si hay reflujo). Ayuno con horario restringido no por defecto | Razonable | 02 |
| Alcohol | «Menos es mejor y cuanto antes, mejor» | Razonable | 02 |
| Desconexión | Actividad tranquila y no estimulante: sin trabajo, correo ni redes. Móvil fuera del dormitorio. 20 min de lectura en papel o e-ink | Razonable | 02 |
| Decisiones | Con deuda de sueño, aplazar las decisiones irreversibles o contrastarlas con otra persona. Las decisiones importantes, en las horas buenas | Razonable | 08 |
| Ergonomía | Variar la postura: «la mejor postura es la siguiente». Altura y distancia de la pantalla como comodidad, no como prevención probada. La mesa elevable reduce el tiempo sentado, pero su beneficio para la salud no está probado | Razonable | 02, 07 |

### 3.2 Reglas nuevas (`02`, `08`)

- **Dificultad habitual para dormir:** si cuesta dormir 3 noches o más por semana durante 3 meses o más, se deja de dar consejos de higiene del sueño y se sugiere hablarlo con un profesional, mencionando la TCC-I (con un profesional o un programa digital validado) solo como derivación. El umbral es interno y el texto al usuario no nombra el insomnio (`05`). Ucoach no aplica la TCC-I ni la restricción del tiempo en cama. La regla de levantarse si no se duerme en unos 20 minutos queda pendiente de revisión jurídica.
- **Tabla fija de derivación** (una herramienta `senal_de_alerta`, con textos fijos que no improvisa el modelo):
  - ideas de suicidio o de hacerse daño: 024, y 112 si hay peligro inmediato, y se detiene el coaching;
  - ánimo bajo casi a diario durante 2 semanas o más;
  - agotamiento persistente con cinismo;
  - pánico o consumo problemático;
  - sospecha de apnea;
  - somnolencia al volante;
  - dolor torácico o falta de aire desproporcionada al hacer ejercicio;
  - fatiga persistente pese a dormir bien.
- **Dormitorio fresco y ventilado, sin cifra.** El único rango con fuente, 20-25 °C, es de mayores de 65 años.
- **Modo «sin números».** Para quien se agobia con los datos (ortosomnia): no se muestran las fases de sueño como diagnóstico.
- **Ejercicio como palanca del sueño.** Es una excepción razonable a «un hábito cada vez».

### 3.3 Prácticas complementarias por nivel (`07`)

Política: Ucoach propone por defecto solo prácticas **A**, ofrece las **B** cuando hay contexto, y las **C** y **D** solo si el usuario pregunta o si ya las practica con un riesgo concreto.

| Nivel | Prácticas (selección) |
|---|---|
| **A · Recomendable** | Ejercicio terapéutico para la lumbalgia; fortalecimiento de cuello y escápulas; variar la postura; mindfulness; ducha o baño caliente 1-2 h antes de dormir |
| **B · Opcional** | Manipulación espinal (osteopatía o quiropráctica) solo con ejercicio; ducha fría; sauna; respiración lenta, *cyclic sighing* y NSDR; creatina; melatonina para el jet lag; paseos en la naturaleza; tapones si hay ruido; escala de grises y bloqueadores de apps; móvil fuera de la vista; VFC como tendencia; música sin letra; cinta de andar bajo la mesa; alfombrilla antifatiga |
| **C · Experimental** | Gafas ámbar nocturnas; modo nocturno; inmersión en hielo; Wim Hof (fuera del agua); melatonina para el insomnio; magnesio; L-teanina; omega-3; vitamina D sin déficit; luz roja; ruido rosa; binaurales; ayuno «para la claridad mental»; EFT o tapping; fases de sueño del wearable |
| **D · No recomendar** | Osteopatía craneal y visceral; fajas y correctores; fitball como silla; gafas de luz azul de día; grounding; agua fría justo después de la fuerza si se busca músculo; Wim Hof en el agua; ashwagandha; *mouth taping*; nootrópicos con receta; electrolitos en la oficina |

**Derivación en espalda y cuello:** al fisioterapeuta, que es profesión sanitaria regulada en España, antes que al osteópata, que no lo es (`07`).

**Suplementos:** Ucoach no receta. Informa del nivel, la dosis estudiada o autorizada y el riesgo, y deriva al farmacéutico o al médico. La melatonina en España no tiene un umbral oficial inequívoco («a partir de» o «más de» 2 mg); la pauta prudente es un complemento de menos de 2 mg. Hungría la prohibió en complementos en agosto de 2026 (`07`; pendiente de confirmar por canal oficial antes de publicar).

**Cómo hablar de C y D** (`07`, apartado 5): la estructura fija es lo que se sabe, lo que no, el riesgo y la mejor alternativa. Se declaran los conflictos de interés (por ejemplo, el grounding). Para las C sin riesgo se ofrece un experimento personal de 2 semanas; nunca para las D con riesgo.

**Catálogo:** un recurso con los campos `practica`, `nivel`, `para_que`, `evidencia`, `fuente`, `anio_fuente`, `riesgos`, `contraindicaciones`, `pauta`, `momento`, `disparador` y `revisado_el`, revisado cada 6 meses.

### 3.4 Protocolos nuevos o ampliados (`07`, `08`)

Siete protocolos con prácticas A y B (las excepciones están marcadas en `07`, apartado 4):
1. espalda y cuello;
2. recuperación tras un mal día;
3. bajón de la tarde;
4. viajes y jet lag;
5. pitch o negociación;
6. invierno;
7. higiene digital.

Además, el modo «sostener» para las semanas de máxima carga: sin metas nuevas y con una sola acción de recuperación.

### 3.5 Cómo conversa el coach (`08`, apartado 14)

- **Preguntar antes de aconsejar, una pregunta por mensaje.** Las preguntas encadenadas van en mensajes sucesivos.
- **Breve.** De 3 a 6 líneas en el brief.
- **Datos del usuario antes que estudios.** Un estudio solo se cita si el usuario pregunta por qué.
- **Una sola recomendación.**
- **Sin sermones.** No se repite un consejo que el usuario ya ha rechazado.
- **Desafío amable contra la complacencia.** Los LLM validan las acciones del usuario un ~49 % más que las personas (Cheng et al., *Science*, 2026). Por eso:
  - buscar al menos un riesgo o una alternativa a cada plan;
  - preguntar «¿qué parte depende de ti?»;
  - señalar con cifras un plan irreal;
  - no elogiar lo trivial.
- **Cerrar con compromiso.** Qué, cuándo y dónde, o «hoy no hace falta nada».
- **Cuándo callar:**
  - durante el foco;
  - tras el apagado;
  - en días libres;
  - ante un «hoy no»;
  - en un mal día, en el que solo pregunta «¿qué necesitas para pasar el día?»;
  - sobre datos aislados: las tendencias, desde 3 días; las relaciones entre indicadores, desde 3 semanas.

### 3.6 Rituales (`03`, `08`)

| Ritual | v0.2 |
|---|---|
| `brief_manana` | Destacado, cuándo y dónde, y un obstáculo con plan si-entonces (WOOP breve: g = 0,34, Wang 2021, con guía humana; con IA, está por medir). Con deuda de sueño, el aviso de decisiones irreversibles. Máximo 6 líneas. Si se lo salta, el cierre de la víspera hace de brief |
| `cierre_dia` | Destacado sí, parcial o no; «¿en qué avanzaste?»; energía de 1 a 5; **apagado** (lo abierto y cuándo retomarlo); aprendizaje opcional. Máximo 5 minutos |
| `revision_semanal` | GROW con las 3 métricas activas del usuario; un solo ajuste del mismo hábito focal; seguimiento de lo leído |
| `retomar` (nuevo) | Tras 3 días o más sin actividad: qué ha pasado, sin culpa; versión mínima del hábito; celebrar la vuelta |
| `preparar_momento_clave` (nuevo) | Víspera: objeciones, contingencias y ensayo. Antes: 10 min de reevaluación («esa activación es energía»). Después: repaso de 2 min. Sin power posing |
| `pre_mortem` (puntual) | Solo antes de hitos. Evidencia débil-razonable: Veinott 2010 no se pudo verificar en la QA |
| `auditoria_agenda` (mensual) | Porcentaje de reuniones, bloques de foco, recurrentes sin objetivo y una acción |
| `plan_lectura` | Recuperación activa (3 ideas de memoria) y una acción con fecha. Los resúmenes, como mapa para elegir |
| `experimento` (nuevo) | Experimento n-de-1 de 2 a 4 semanas con orden aleatorio por días (por ejemplo, hora del último café o bloque de 60 o 90 min), resumido con su incertidumbre |

**Mitos que Ucoach no repite** (`08`, apartado 13): el power posing hormonal; la fuerza de voluntad como depósito (d = 0,06 en la réplica de 36 laboratorios); los jueces que deciden peor antes de comer; los «23 minutos» para recuperar el foco; el «+71 %» de los días sin reuniones como causal; los OKR como ciencia; los resúmenes de libros como aprendizaje.

---

## 4. Retención y avisos

**El objetivo es la vuelta, no la racha** (`03`). La mejor de 54 intervenciones del megaestudio de Milkman (Nature, 2021) premiaba volver al gimnasio tras faltar. Destacar una racha rota reduce la conducta siguiente (Silverman y Barasch, 2023).

- **Presupuesto de envío:**
  - de 1 a 3 avisos al día, como máximo 4;
  - nunca dos en 60 minutos;
  - horas de silencio desde la desconexión;
  - `snooze` y un «hoy no» que no cuenta como fallo.
- **Avisos que se retiran.** Cada hábito tiene una fase de andamio, con un aviso diario ligado a su ancla. Cuando la automaticidad supera el umbral, o tras 3 semanas cumplidas, el aviso pasa a días alternos y después desaparece.
- **Sin rachas punitivas.** Se muestra «5 de 7» o «12 de los últimos 14», con racha reparable. Queda prohibido el texto «has roto tu racha».
- **Registro con poca fricción.** El sueño entra de forma pasiva (Apple Health o CSV) o con una sola pregunta en el brief. El check-in tiene 3 ítems como máximo, dentro del cierre.
- **Datos honestos.** El sueño se muestra como tendencia semanal y regularidad. Los informes personales piden al menos 14 días y 5 días por grupo, usan lenguaje de incertidumbre y nunca hablan de causalidad.

---

## 5. Arquitectura técnica v0.2 (`04`)

```
equipo del usuario
├─ servidor MCP (Python estándar, stdio, dual-era 2025-11-25 / 2026-07-28)
│   ├─ herramientas con anotaciones (readOnlyHint…) y salida estructurada
│   ├─ catálogo de prácticas con nivel A-D y método (recurso)
│   └─ SQLite en ~/.ucoach (0700/0600, también WAL y SHM)
├─ ucoach nudge: determinista, sin LLM, plantillas fijas sin texto libre
│   └─ lanzado por launchd / systemd --user / Programador de tareas
│       (ucoach schedule install)
├─ canales: notificación del sistema · ntfy (servidor propio o tema aleatorio) · Telegram
└─ Claude Desktop: tarea local «brief de mañana» (con la app abierta y el equipo despierto)
    respaldo: nudge a las 09:00 «abre tu brief»
```

**P0 (antes de los 20 usuarios):**
- **Dual-era completo:**
  - `server/discover`, `resultType`, `ttlMs` y `cacheScope`, `serverInfo` en `_meta`;
  - error -32022 ante versiones no soportadas y -32601 inmediato ante métodos desconocidos;
  - anunciar 2026-07-28 solo cuando pasen las pruebas de conformidad.
- **Endurecer los datos:** permisos comprobados al arrancar, token de Telegram en el llavero y logs sin datos de salud.
- **Sanear el calendario:** guardar solo horas, `clave` y un título truncado; las plantillas no llevan texto libre. El caso real de un evento de Google Calendar que acabó ejecutando código en Claude Desktop (LayerX, 2026) muestra que el título de una reunión es entrada no fiable.
- **Anotaciones en todas las herramientas** y validación estricta de la entrada.

**P1:**
- reuniones cacheadas para `nudge` (solo horas);
- `ucoach schedule install`;
- salida estructurada en `contexto_del_dia`, `planificar_dia` y `revision_semanal`;
- `.mcpb` privado tipo `uv`, con aviso de versión propio porque el directorio de Claude ya no acepta MCPB;
- plugin para Claude Code, la pestaña Code de Claude Desktop y Cowork en local;
- importador de Apple Health endurecido;
- `audit_log` y `ucoach undo`.

**P2 y siguientes:**
- **Conectores:** Polar (OAuth2 con reautorización anual), Garmin Personal (clave propia) si la congelación de altas no la afecta, y una carpeta vigilada para Health Auto Export.
- **Panel:** informe HTML semanal.
- **Publicación con garantías:** firma, checksums y *trusted publishing*.
- **Más adelante:** MCP Apps (no funciona en Claude Code), Oura OAuth y lectura de .ics.

**No hacer:**
- Sampling, Roots ni Logging del protocolo (en desuso).
- SQLCipher por defecto.
- Agregadores de pago (Terra desde 499 $/mes).
- Servidor remoto antes de la fase gestionada.

**SDK oficial:** solo cuando haya HTTP u OAuth. `mcp` 2.3.0 trae 14 dependencias directas.

**Conectores en 2026:**
- **Oura** exige OAuth desde que eliminó los tokens personales en diciembre de 2025.
- **WHOOP** tiene un sandbox de 10 miembros.
- **Polar** está abierto a cualquier usuario.
- **Fitbit:** su API web se apagó el 2-11-2026.
- **Garmin** congeló las altas nuevas a su programa de desarrolladores en 2026 (`01`).

La vía rápida es aceptar los datos que la IA ya obtiene de otros MCP de wearables (`01`, P0-3).

---

## 6. Privacidad y regulación (`05`)

**P0, antes de la validación:**
1. Corregir la promesa de privacidad en el documento, el README y la web, y también el mensaje propuesto en `06`, apartado 8.
2. Escribir la **finalidad prevista**: «herramienta de bienestar y organización personal para adultos sanos… no destinada a diagnosticar, tratar, curar, aliviar ni prevenir ninguna enfermedad; no es un producto sanitario».
3. Revisar todos los textos con la lista de palabras que hay que evitar (`05`, apartado 4). Ni «insomnio» como algo que se mide, ni «detectar burnout», ni «tu VFC es anormal», ni «clínicamente probado» sin fuentes, ni «potencia tu rendimiento».
4. **Consentimiento explícito** (art. 9.2.a RGPD) y hoja informativa para los 20 usuarios. Solo se recoge lo mínimo, seudonimizado y con plazo de borrado, y se lleva un registro de actividades. La energía y el ánimo seguidos en el tiempo son, con alta probabilidad, datos de salud: se trata toda la base como categoría especial.
5. Pantalla «Tu IA y tus datos», con instrucciones para desactivar el entrenamiento en Claude y ChatGPT, y resúmenes por defecto en `contexto_del_dia` y `revision_semanal`.
6. Ninguna telemetría. Los avisos que pasan por Telegram no llevan datos de salud.

**Marco:**
- **Versión local:** el promotor no es responsable del tratamiento mientras no reciba datos, y el usuario queda en la excepción doméstica.
- **Versión gestionada:**
  - consentimiento explícito y evaluación de impacto (EIPD) que hay que hacer;
  - contratos de encargo, alojamiento en la UE y notificación de brechas en 72 h;
  - el aviso de IA del art. 50 si hay chat propio;
  - consumo: Ley 10/2025, con aviso 15 días antes de cada renovación, y botón de desistimiento, aunque España no ha transpuesto la Directiva 2023/2673 a 04-11-2026.
- **Ley de IA:** el Reglamento (UE) 2026/1744 retrasa el alto riesgo al 2-12-2027 y al 2-08-2028, pero no las prohibiciones ni el art. 50, que se aplica desde el 2-08-2026.
- **EE. UU.:** mejor no vender al principio (FTC Health Breach Notification Rule y My Health My Data Act de Washington).

**Para un abogado** (`05`, apartado 6):
- que el promotor no es responsable del tratamiento en la versión local;
- que la validación cumple;
- la delimitación frente al producto sanitario con la finalidad redactada;
- el art. 22 del RGPD (perfilado);
- la LSSI y las cookies de la web;
- el RD 1907/1996 frente al mensaje de rendimiento y las prácticas complementarias;
- el CRA para el *open core*.

---

## 7. Negocio y validación (`06`, `03`)

**Ruta:** contenido como motor (F), programa de 30 días por cohortes de 49 a 99 € (C), plan Coach de 29 a 59 €/mes por coach (B) y aceleradoras (D). El open source es la base de confianza. Un híbrido «Ucoach + coach» de 99 a 199 €/mes lo prestarían coaches socios. El Pro individual de 8 a 12 €/mes, solo si aparece demanda.

**Por qué el coach humano:**
- Cobra unos 175-350 $/mes por cliente (Paperbell, 2026) y no ve qué hace el cliente entre sesiones.
- Aporta la responsabilidad que retiene: el apoyo humano mejora la adherencia, y el único ensayo de 2026 con directivos encontró efectos solo con coaching humano (de Haan, Terblanche y Nowack, 2026; `08`).
- Es un canal: cada coach trae a sus clientes.

Que sea el mejor canal es una hipótesis (H3), no un hecho. Las herramientas para coaches que ya existen (Trainerize, Coachvox AI) no se han analizado a fondo: ver el apartado 10.

**Plan de 90 días (20-11-2026 a 18-02-2027):**

| Semanas | Qué |
|---|---|
| 1-4 | Uso propio diario con diario público en LinkedIn y X. 15 entrevistas Mom Test (10 fundadores y 5 coaches). Repositorio público **con el nombre definitivo**. Landing de lista de espera |
| 5-8 | 20 usuarios con onboarding de 20 minutos, consentimiento firmado y `ucoach stats` local. Show HN y directorios de MCP la segunda semana de enero. Revisión semanal *concierge* a 5 usuarios. Opcional: una cohorte orgánica de 10 a 20 usuarios que llegan por el Show HN, sin entrevistas, medida con el mismo `ucoach stats` |
| 9-13 | Cohorte de pago (49 €) del 19-01 al 17-02, con la venta abierta el 22-12. Piloto con 3 coaches desde el 15-01 como tarde. Una conversación con una aceleradora |

**Métricas de validación** (definiciones de `03`, umbrales de decisión de `06` reconciliados, ver el apartado 8):

| Señal | Seguir | Pivotar |
|---|---|---|
| Semana activa (3 rituales o más) en la cohorte guiada | ≥60 % en la semana 4, ≥45 % en la 8 y ≥35 % en la 12 | <20 % en la semana 4 → el problema es el formato |
| Cohorte orgánica sin entrevistas | ≥20 % activos en la semana 4 | n. a. |
| Tasa de vuelta (vuelven en 7 días tras 3 días o más inactivos) | ≥50 % | n. a. |
| Automaticidad del hábito focal (SRBAI) | +1 punto en la semana 8 | n. a. |
| Pago en la cohorte | ≥10 plazas y ≥25 % de los activos entre ellas | <5 plazas → reformular oferta o público |
| Coaches | ≥2 de 3 renuevan pagando | 0 → abandonar el plan Coach y probar aceleradoras |
| Sean Ellis «muy decepcionado» | ≥40 % en algún segmento (indicativo con menos de 40 respuestas) | <25 % en todos |
| Avisos | Silenciados <20 % y el cron sigue activo en ≥70 % de usuarios en la semana 8 | n. a. |
| Consentimiento | 100 % antes de la primera medición | n. a. |

**No hacer en 90 días:** conectores directos, app móvil, sincronización en la nube ni plan Equipos.

---

## 8. Contradicciones entre informes y cómo se resuelven

| Tensión | Informes | Resolución |
|---|---|---|
| Micropausas cada ~30 min frente a 1-3 avisos al día y avisos de «levántate» sin efecto | 02 / 03 | Las micropausas forman parte del plan y del bloque de foco (texto del plan, sin aviso). Los avisos de movimiento solo se envían ligados a un contexto (tras 2 h de reuniones, en el bajón de la tarde o si a las 17:00 no se ha movido) y cuentan dentro del presupuesto diario |
| La regla 20-20-20 como «lo que mejor funciona» frente a una heurística débil | 07 (antes de la QA) / 02 | Recordatorio opcional («mira lejos y parpadea a menudo»), sin decir que está probado |
| Un motor de avisos que aprende frente a «Ucoach no es un sistema de IA» | 03 / 05 | Reglas fijas con aleatorización simple (70/30) y una persona que retira los tipos de aviso sin efecto: queda fuera de la definición. Un bandit o un aprendizaje por refuerzo convertiría el motor en sistema de IA: aplicaría el art. 50, sin riesgo alto mientras la finalidad sea el bienestar |
| Detectar burnout o insomnio frente a la frontera del producto sanitario | 03, 08 / 05 | Señales de bienestar con umbrales internos que solo disparan una sugerencia de hablar con un profesional, con textos fijos que no nombran trastornos ni diagnostican |
| Experimentos con 20 usuarios frente a datos de salud | 03 / 05 | Consentimiento explícito firmado, hoja informativa, minimización y borrado al cerrar |
| Brief automático frente a proactividad en la nube | 01, 06 / 04 | Tarea local de Claude Desktop con `nudge` de respaldo. El cierre de la víspera puede hacer de brief. H1 se mide con ese canal: depende de que Claude Desktop esté abierto, y cuentan también los briefs abiertos tras el aviso de las 09:00 |
| «Vive dentro de tu IA» frente a avisos sin IA | 01 / 04 | La IA para los rituales con valor (brief, cierre, revisión) y el sistema operativo para lo proactivo. Se presenta así, sin prometer tareas programadas de la IA |
| «Ventana europea» como foso frente a Google Health Coach en España | 01, 06 (antes de la QA) | Corregido: la ventaja europea es temporal y solo frente a ChatGPT y Claude; el hueco es el método con contexto de trabajo |
| Retención ≥40 % a 4 semanas como criterio de decisión frente a semana activa ≥60 % en la cohorte guiada | 06 / 03 | Se adoptan las definiciones de `03` (semana activa = 3 rituales o más, cohortes separadas) y se mantiene el umbral de pivote de `06` (<20 %) |
| Un hábito cada vez frente a ejercicio como palanca del sueño | 02 | Excepción declarada: proponer ejercicio junto a un hábito de sueño es compatible |
| Conectores propios en la P2 técnica frente a ningún conector en 90 días | 04 / 06 | Sin contradicción: los conectores van después de la validación y solo si los usuarios los piden |
| Garmin Personal como conector barato frente a la congelación de altas de Garmin | 04 / 01 | Polar va primero. Garmin Personal, solo si se confirma que la congelación no afecta a la clave personal |
| TCC-I y regla de los 20 minutos frente a «Ucoach no debe aplicar TCC-I» | 02 / 05 | La TCC-I solo se menciona como derivación, con un umbral interno y un texto que no nombra el insomnio. Ucoach no la aplica. La regla de los 20 minutos queda pendiente de revisión jurídica |
| La sensación subjetiva manda frente a «con poco sueño no notas el deterioro» | 02, 03 / 08 | Tras una noche, manda la sensación. Con deuda acumulada (media de varias noches), el aviso de decisiones irreversibles y de menos exigencia se mantiene aunque el usuario diga sentirse bien |

---

## 9. Riesgos principales

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| ChatGPT o Claude llevan a la UE salud, calendario y agente proactivo | Alta en 12-24 meses (`01`) | Diferenciarse por el método y el coach humano; independencia de la IA |
| Un wearable (WHOOP, Samsung) añade el calendario | Media-alta (`01`) | Contexto de trabajo profundo e independencia del dispositivo |
| Abandono tras la primera recaída | Alta en apps de salud: 3-7 % a 30 días (`03`) | Ritual de vuelta, sin rachas, avisos que se retiran y coach humano |
| Complacencia del LLM y consejos inadecuados en crisis | Documentado (`08`) | Regla antiadulación y tabla fija de derivación |
| Inyección de instrucciones por el calendario o un clon del paquete | Casos reales en 2026 (`04`) | Entrada saneada, plantillas sin texto libre, firma y checksums |
| Frontera con el producto sanitario o la publicidad sanitaria | Depende de las palabras (`05`) | Finalidad prevista, lista de palabras y revisión de un abogado |
| Hazlo tú mismo: el público técnico junta un MCP de Garmin, el calendario y un prompt | Alta en la fase 1 (`01`) | El método y la memoria longitudinal no caben en un prompt; open source para ganar su confianza |

---

## 10. Lo que no sabemos todavía

- **Marca:** búsqueda de «Circalia» (y alternativas) en EUIPO y OEPM, y precio real de los dominios.
- **Herramientas para coaches** (Trainerize, Coachvox AI y otras): no se han analizado a fondo; es lo único que quedó abierto en el QA del informe 06. Hay que hacerlo antes de diseñar el plan Coach.
- **Eficacia de un coach con LLM para este caso de uso:** no hay ensayos. El único ensayo de 2026 con directivos encontró efecto solo con coaching humano, y en el único ensayo con un LLM centrado en actividad física la actividad no subió más que en el control. Ucoach tiene que medirlo él mismo.
- **Sin verificar en la QA, y por tanto sin regla que se apoye en ellos (como mucho sostienen un ritual opcional, el `pre_mortem`):**
  - el 28 % de tiempo a solas de los CEO (Porter y Nohria);
  - el estudio del pre-mortem (Veinott 2010);
  - la proporción de autointerrupciones (Gloria Mark);
  - si NICE NG59 tiene alguna actualización posterior a 2020;
  - Ultrahuman, Rook y Thryve.
- **Pendiente de confirmar por canal oficial antes de publicar el catálogo:** la prohibición de la melatonina en complementos en Hungría, el borrador de los Países Bajos sobre la ashwagandha y la TGA.
- **Comportamiento dual-era de Claude Desktop:** no está documentado; hay que probarlo.

---

## 11. Estado del QA

Cada informe pasó por un extractor de afirmaciones, un verificador en contexto independiente (que no vio el informe), la comparación y las correcciones. En seis de los ocho informes, además, las críticas corregidas se cotejaron desde la sesión principal. La nota la calcula `nota.py` sobre las afirmaciones extraídas (todas las portantes más una muestra de apoyo) y tiene un techo por cobertura.

| Informe | Nota antes de corregir | Nota después | Veredicto | Afirmaciones verificadas | Qué limita la nota |
|---|---|---|---|---|---|
| 01 · Mercado y competencia | 0,0 | 9,7 | Entregable | 62 de 64 | Cobertura |
| 02 · Evidencia de las reglas | 0,0 | 9,3 | Entregable | 73 de 95 | Cobertura |
| 03 · Retención y conducta | 0,0 | 9,1 | Entregable | 74 de 97 | Cobertura |
| 04 · MCP, seguridad y conectores | 0,0 | 10,0 | Entregable | 81 de 81 extraídas (el informe tiene unas 170) | Ninguno abierto |
| 05 · Privacidad y regulación | 0,0 | 9,8 | Entregable | 115 de 115 | Una baja abierta (normas no analizadas) |
| 06 · Negocio y go-to-market | 0,0 | 8,3 | Corregir antes de entregar | 45 de 60 | Herramientas para coaches sin analizar |
| 07 · Prácticas complementarias | 0,0 | 8,6 | Entregable | 83 de 157 | Cobertura |
| 08 · Rendimiento y método | 0,0 | 8,6 | Corregir antes de entregar | 84 de 136 | Dos portantes sin verificar |

**Límites del QA:**
- No se pudo ejecutar el contrato de escritura de `de-slop` porque el script no existe en esta máquina. Los guiones largos están a 0 en los ocho informes.
- La re-verificación del texto corregido se hizo cotejando una muestra de las correcciones críticas, no todas una a una.
- Varias fuentes bloquean a los robots (403): no están rotas, pero no se pudieron abrir automáticamente.
