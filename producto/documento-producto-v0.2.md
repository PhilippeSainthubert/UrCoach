# Ucoach (propuesta de nombre: Circalia)

*Coach de excelencia profesional para fundadores, que cuida la energía y el sueño como base del trabajo. Vive dentro de la IA que ya usas. Documento de producto, versión 0.2, 19 de noviembre de 2026. Sustituye a la v0.1 del Google Doc «Ucoach: documento de producto». La base está en `research/ucoach-analysis.md` y en los ocho informes verificados de `research/`.*

---

## Resumen ejecutivo

**Ucoach es la capa de método que convierte la IA que un fundador ya usa en su coach de rendimiento.** Cruza su agenda y su trabajo con su sueño, su energía y sus hábitos, y le dice cómo jugar el día. Cada pauta lleva su nivel de evidencia.

Cruzar agenda y sueño ya no es nuevo: lo hacen Lifestack, Rise y athletedata. Además, Claude y ChatGPT leen datos de salud en EE. UU., y Google Health Coach funciona en España con Fitbit o Pixel Watch. Lo que nadie ofrece es un **método explícito y auditable, con memoria longitudinal propia, que cruce agenda, trabajo y cuerpo, independiente del wearable y de la IA**. Eso es Ucoach.

Cambios principales respecto a la v0.1:
- **Método corregido con la evidencia.** Fuera las reglas sin base; dentro la derivación a la TCC-I, la derivación fija y las prácticas con nivel A, B, C o D.
- **Diseño para la recaída.** Sin rachas, con un ritual de vuelta y avisos que se retiran.
- **Proactividad que no depende de la nube.** Los avisos los dispara el sistema operativo.
- **Protocolo MCP actualizado.** El servidor habla las dos eras del protocolo: la vigente (2026-07-28) y la anterior (2025-11-25).
- **Promesa de privacidad honesta.**
- **Modelo de negocio:** contenido, programas por cohortes y un plan para coaches humanos.

Los riesgos principales son tres:
- que ChatGPT o Claude lleven a Europa la salud y los agentes proactivos;
- la retención, porque las apps de salud conservan entre el 3 y el 7 % de los usuarios a 30 días;
- la frontera con el producto sanitario, que deciden las palabras.

El plan es usarlo a diario, validar con 20 emprendedores con consentimiento y pedir dinero antes del 18 de febrero de 2027.

---

## Problema

Un fundador toma decisiones de alto impacto con una agenda que no controla del todo. Los hábitos que sostienen su rendimiento son lo primero que cae cuando aprieta el trabajo: duerme menos, se mueve menos y encadena reuniones sin pausa. Y dormir poco empeora el juicio sin que quien lo sufre lo note: tras dos semanas durmiendo 6 horas o menos, el rendimiento cognitivo cae como tras hasta dos noches en vela, mientras la somnolencia percibida apenas sube (Van Dongen, 2003).

Tiene datos de sobra, pero ninguno le dice qué hacer hoy:
- **El calendario** sabe qué reuniones hay, pero no cómo ha dormido.
- **El wearable** sabe cómo ha dormido, pero no que mañana tiene una negociación.
- **Su IA** puede leer las dos cosas, pero no tiene método ni memoria estructurada de sus semanas.
- **Un coach humano** pide cuentas, pero no ve qué pasa entre sesiones.

---

## Público objetivo

| Segmento | Descripción | Fase |
|---|---|---|
| Fundador técnico | Cómodo con la terminal; usa Claude u otra IA con MCP | 1 |
| Coach de fundadores y directivos | Cobra 175-350 $/mes por cliente y no ve lo que pasa entre sesiones | 1 (piloto) y 2 (plan Coach) |
| Cohortes de aceleradoras | Programas de 10 a 40 fundadores | 2 |
| Fundador no técnico | Usa IA a diario y no quiere instalar nada | 3 (versión gestionada, solo si la validación lo justifica) |

---

## Competencia

| Categoría | Ejemplos | Qué les falta frente a Ucoach |
|---|---|---|
| Coaches de wearable | WHOOP Coach, Oura Advisor, Google Health Coach (incluido en Google AI Pro), Garmin Connect+ | No leen la agenda; solo funcionan con su dispositivo |
| Planificadores con energía | Lifestack, Rise (curva de energía en el calendario) | Sin método con evidencia; sin contexto de trabajo profundo |
| Plataformas de IA | Claude (salud en EE. UU., Duet), ChatGPT (Health fuera del EEE, dots), Gemini | Sin método ni serie temporal estructurada del usuario; la salud no ha llegado a la UE en Claude ni en ChatGPT |
| MCP de datos de salud | Open Wearables, garmin_mcp, Delx Wellness, athletedata | Capa de datos sin método con contexto de trabajo |
| Calendario con IA | Reclaim, Motion, Sunsama, Akiflow | No conocen el sueño ni la energía. Reclaim es un socio posible: Ucoach propone el bloque y Reclaim lo defiende |
| Coaching ejecutivo con IA | Valence, BetterUp, CoachHub | B2B de liderazgo, sin datos del cuerpo |

---

## Propuesta de valor

**El método de un coach de alto rendimiento, con tus datos y dentro de tu IA. Tú conectas tu wearable; Ucoach decide qué hacer hoy y aprende de tus semanas.**

Ejemplo: has dormido 5,2 horas (media de 3 noches por debajo de 6) y tienes reuniones de 9:00 a 12:30, entre ellas una negociación. Ucoach te propone:
- salir 10-20 minutos a la luz al despertar;
- el destacado del día, con su obstáculo y un plan si-entonces;
- preparar la negociación la víspera, con objeciones y contingencias;
- aplazar o contrastar con alguien cualquier decisión irreversible;
- una siesta de 10-20 minutos antes de las 15:00;
- entreno sin esfuerzos máximos;
- último café 9 horas antes de dormir.

Y te avisa de que las reuniones ocupan tu mejor franja.

| Diferencial | Por qué importa |
|---|---|
| Método explícito con nivel de evidencia | Ningún competidor publica sus reglas ni su grado de evidencia |
| Contexto de trabajo | Reuniones clave, cadenas sin pausa, auditoría de agenda, momentos clave |
| Memoria longitudinal local | «Tu energía tras dormir 7 h o más frente al resto», con tus números |
| Independiente del dispositivo y de la IA | Apple Health, CSV o los datos que tu IA saca de otros MCP |
| Local por defecto y seguro por diseño | Sin servidores de Ucoach ni dependencias; solo lee y sugiere |

---

## Principios de producto

1. **Pocas intervenciones, en el momento justo.** De 1 a 3 avisos al día, nunca más de 4 ni dos en la misma hora.
2. **Ajustar al estado real.** Con mal sueño, menos exigencia y ninguna decisión irreversible sin una segunda mirada.
3. **Un hábito cada vez, hasta que sea automático** (8 a 10 semanas como referencia).
4. **La vuelta importa más que la racha.** Nunca «has roto tu racha».
5. **Datos propios antes que promedios.** Con honestidad: sin causalidad y con un mínimo de días.
6. **Cada práctica con su nivel de evidencia.** Por defecto, solo las de nivel A.
7. **Preguntar antes que aconsejar, y desafiar con amabilidad.** Sin adular y sin sermones.
8. **Rendimiento sostenible, no obsesión.** El descanso forma parte del plan.
9. **No es medicina.** Ucoach no diagnostica, deriva con textos fijos y no es un producto sanitario.

---

## El método

### Reglas del plan del día

| Área | Regla |
|---|---|
| Sueño | Meta de 7 a 9 h. El estado del día sale de la media de 3 a 7 noches: deuda, justo, bien o largo (>9-10 h). Índice de regularidad y de jet lag social. Tras una noche, la sensación del usuario manda sobre la puntuación del wearable; con deuda acumulada, el aviso se mantiene aunque diga sentirse bien |
| Despertar | Hora fija, con un margen de ±30-60 min |
| Luz | 10-20 min de luz exterior en la primera hora y media, y luz natural durante el día. Luz tenue desde 3 h antes de dormir y dormitorio a oscuras |
| Cafeína | Último café al menos 9 h antes de dormir; preentreno o bebidas energéticas, al menos 13,5 h; máximo de 400 mg al día |
| Siesta | 10-20 min antes de las 15:00 si se durmió poco. Nunca si hay quejas de insomnio. Tras la siesta, esperar 15-30 min antes de conducir |
| Foco | Bloque de 60 a 120 min en el pico que marquen tus check-ins, con una meta clara. Sin avisos durante el bloque |
| Reuniones | Preparación de 10 min antes de las reuniones clave. Alerta con 2 h o más seguidas. Reuniones de 25 o 50 min como norma |
| Movimiento | Micropausas de 2-3 min cada ~30 min dentro del bloque (evidencia en adultos con sobrepeso u obesidad); una pausa de 5-10 min cada 60-90 min; 7.000-8.000 pasos, subiendo de forma gradual |
| Entreno | 45 min. Con poco sueño, sin esfuerzos máximos ni muy técnicos por la tarde. La VFC, solo como tendencia de 7 días |
| Comida | Antes de las 15:00 cuando se pueda, con horarios regulares. Cena 2-3 h antes de dormir |
| Alcohol | Cuanto menos y cuanto antes, mejor |
| Desconexión | Actividad tranquila, sin trabajo, correo ni redes, y móvil fuera del dormitorio. 20 min de lectura en papel o e-ink |
| Decisiones | Las importantes, en las horas buenas. Con deuda de sueño, aplazar o contrastar las irreversibles |
| Ergonomía | Variar la postura. Pantalla y silla como comodidad. Alternar sentado y de pie |

Se retiran de la v0.1: el primer café a los 75 minutos, el bloque de 90 minutos justificado por el ciclo ultradiano, la «luz azul» como motivo de la desconexión y la regla 20-20-20 como regla probada (ahora es un recordatorio opcional).

### Derivación (regla fija, no la decide el modelo)

| Señal | Respuesta |
|---|---|
| Ideas de suicidio o de hacerse daño | Texto fijo con el 024, y el 112 si hay peligro inmediato. Se detiene el coaching |
| Ánimo bajo casi a diario 2 semanas o más; agotamiento persistente con cinismo | Recomendar un profesional sanitario y pasar al modo «sostener» |
| Pánico; consumo problemático | Derivar |
| Dificultad para dormir 3 noches o más por semana durante 3 meses o más | Dejar los consejos de higiene del sueño y sugerir hablarlo con un profesional. La TCC-I (profesional o programa digital validado) se menciona solo como derivación: Ucoach no la aplica |
| Ronquidos con pausas, somnolencia al conducir | Derivar. Con muy poco sueño o mucha somnolencia, no conducir, o hacer antes una siesta y esperar 15-30 min (pauta prudente, `research/02`) |
| Fatiga persistente pese a dormir bien, pérdida de peso sin explicación | Derivar al médico |
| Dolor torácico, mareo o falta de aire desproporcionada al hacer ejercicio | Derivar |
| Dolor de espalda o cuello que no mejora en 4-6 semanas | Fisioterapeuta |
| Pérdida de fuerza, hormigueo que baja por un brazo o una pierna, alteraciones de esfínteres, fiebre, dolor nocturno que no cede o traumatismo | Médico |

Los umbrales son internos: disparan una sugerencia y no se muestran como medida clínica. Los textos no nombran trastornos.

### Prácticas complementarias por nivel

| Nivel | Uso en Ucoach | Ejemplos |
|---|---|---|
| A · Recomendable | Por defecto en el plan | Ejercicio para la espalda y el cuello, variar la postura, mindfulness, ducha caliente 1-2 h antes de dormir |
| B · Opcional | Si hay contexto o el usuario se interesa | Manipulación espinal solo con ejercicio, ducha fría, sauna, respiración lenta y *cyclic sighing*, NSDR, creatina, melatonina para el jet lag, paseos en la naturaleza, tapones, escala de grises, VFC como tendencia |
| C · Experimental | Solo si el usuario pregunta; experimento personal de 2 semanas si no hay riesgo | Gafas ámbar, inmersión en hielo, magnesio, L-teanina, luz roja, ruido rosa, binaurales, EFT, fases de sueño del wearable |
| D · No recomendar | Se explica por qué y se ofrece una alternativa | Osteopatía craneal y visceral, fajas, gafas de luz azul de día, grounding, *mouth taping*, ashwagandha, nootrópicos con receta |

Suplementos: Ucoach no receta. Da el nivel, la dosis estudiada o autorizada y el riesgo, y deriva al farmacéutico o al médico. El catálogo guarda la fuente, el año y la fecha de revisión de cada práctica y se revisa cada 6 meses.

### Cómo conversa

- Pregunta antes de aconsejar, y una pregunta por mensaje.
- Mensajes breves.
- Tus datos antes que los estudios.
- Una sola recomendación.
- Sin sermones.
- Resume lo que ha entendido antes de proponer.
- Desafía con amabilidad: busca al menos un riesgo o una alternativa a cada plan y no elogia lo trivial.
- Cierra con un compromiso: qué, cuándo y dónde.
- Calla durante el foco, tras el apagado, en los días libres, ante un «hoy no» y sobre datos aislados.

---

## Rituales

| Ritual | Para qué sirve |
|---|---|
| `brief_manana` | Estado de energía, el destacado con su obstáculo y su plan si-entonces, los bloques, la hora límite del café y las alertas. Máximo 6 líneas |
| `cierre_dia` | Destacado cumplido o no, avance, energía de 1 a 5 y apagado (qué queda abierto y cuándo se retoma). Máximo 5 minutos. Sirve de brief si mañana no lo hay |
| `revision_semanal` | GROW con tus 3 métricas, el mismo hábito focal hasta que sea automático, un solo ajuste y seguimiento de lo leído |
| `retomar` | Tras 3 días o más sin actividad: sin culpa, versión mínima del hábito, celebrar la vuelta |
| `preparar_reunion` | Objetivo en una frase, si hace falta reunirse, agenda como preguntas y límite |
| `preparar_momento_clave` | Pitch, negociación o conversación difícil: víspera, 10 minutos antes y repaso posterior |
| `pre_mortem` | Solo antes de hitos: lanzamiento, ronda, contratación |
| `auditoria_agenda` | Mensual: % de reuniones, foco protegido y una acción |
| `plan_lectura` | Recuperación activa y una acción con fecha |
| `onboarding` | Perfil, hábito focal con su ancla y su versión de 2 minutos, ergonomía y la pantalla «Tu IA y tus datos» |

Modo **«sostener»**: en semanas de máxima carga, sin metas nuevas y con una sola acción de recuperación.

---

## Herramientas MCP (v0.2)

Las 12 herramientas de la v0.1 se mantienen. Todas llevan anotaciones (`readOnlyHint` donde corresponde) y validación estricta de la entrada.

Cambios en las existentes:
- **`contexto_del_dia`, `planificar_dia` y `revision_semanal`:** salida estructurada y resúmenes por defecto.
- **`planificar_dia`:** guarda las horas de las reuniones (sin descripciones) para que `nudge` las conozca.
- **`registrar_checkin`:** añade `destacado_cumplido`, `minutos_foco` y `trabajo_tras_hora_fin`.
- **`perfil`:** añade `hora_fin_trabajo`, `rutina_previa`, `palabras_clave_momento_clave` y `metricas_activas`.
- **`registrar_sueno` y `registrar_metrica`:** aceptan los datos que la IA obtiene de otros MCP de wearables.

Nuevas:

| Herramienta | Descripción |
|---|---|
| `senal_de_alerta` | Devuelve el texto fijo de derivación y los teléfonos para cada tipo de señal |
| `practica` | Consulta el catálogo: nivel, evidencia, fuente, riesgos y alternativa. Decisión de diseño: expone como herramienta el catálogo que `research/07` propone como recurso |
| `experimento` | Diseña y resume un experimento personal de 2 a 4 semanas |
| `auditar_agenda` | Calcula en local el reparto de la agenda a partir de los eventos que pasa la IA |
| `registrar_estimacion` | Estimado frente a real, para corregir la falacia de planificación |

Recursos: `metodo.md` (principios, banco de preguntas y derivación), el catálogo de prácticas y los protocolos.

Protocolos nuevos: espalda y cuello, recuperación, bajón de la tarde, viajes y jet lag, pitch y negociación, invierno, higiene digital y modo «sostener».

---

## Arquitectura

| Componente | Función |
|---|---|
| Servidor MCP | Python estándar, stdio, sin dependencias. **Dual-era**: especificación 2025-11-25 y 2026-07-28 (`server/discover`), con pruebas de conformidad |
| Base de datos | SQLite en `~/.ucoach` (permisos 0700/0600, también WAL y SHM). Logs sin datos de salud |
| `ucoach nudge` | Determinista, sin LLM, con plantillas fijas sin texto libre. Presupuesto de 1 a 3 avisos al día, horas de silencio, `snooze`, aleatorización simple por tipo de aviso y retirada de avisos cuando el hábito se automatiza |
| Planificador | `ucoach schedule install`: launchd (`StartCalendarInterval`) en macOS, systemd `--user` con `Persistent=true` en Linux y Programador de tareas en Windows. Sustituye a cron, que pierde las ejecuciones con el equipo dormido |
| Canales | Notificación del sistema (por defecto), ntfy (servidor propio o tema aleatorio largo) o Telegram (token en el llavero). Ningún aviso lleva datos de salud |
| Brief | Tarea local de Claude Desktop, con la app abierta y el equipo despierto. Respaldo: `nudge` a las 09:00 |
| Importadores | Apple Health (`export.xml` en streaming, con el analizador XML endurecido) y CSV |
| Distribución | `.mcpb` privado tipo `uv` para el chat de Claude Desktop (con aviso de versión propio, porque el directorio ya no acepta MCPB). Plugin para Claude Code, la pestaña Code y Cowork en local. Web y móvil, solo con servidor remoto (fase gestionada) |

**Seguridad.** El título de una reunión, una nota o un CSV son entrada no fiable: se truncan, nunca se reenvían y nunca se ejecutan. Las versiones se publican firmadas, con checksums y *trusted publishing*. Se añaden `audit_log` y `ucoach undo`.

---

## Privacidad, seguridad y regulación

| Tema | Decisión |
|---|---|
| Promesa | «Sin servidores de Ucoach: tus datos viven en tu ordenador y solo los ve la IA que tú eliges. Cuando tu IA los consulta, los procesa tu proveedor de IA según sus condiciones.» |
| Finalidad prevista | «Herramienta de bienestar y organización personal para adultos sanos. Ofrece pautas generales de sueño, luz, actividad, alimentación y ergonomía. No está destinada a diagnosticar, tratar, curar, aliviar ni prevenir ninguna enfermedad, y no es un producto sanitario. Ante síntomas o dudas de salud, consulta a un profesional.» |
| Palabras | Sin «diagnostica», «detecta el burnout», «insomnio» como algo que se mide, «tu VFC es anormal», «clínicamente probado» ni «potencia tu rendimiento». Ver `research/05`, apartado 4 |
| Datos de salud | Todo lo que guarda Ucoach se trata como categoría especial (art. 9 RGPD), también la energía y el ánimo |
| Versión local | El promotor no recibe datos y no es responsable del tratamiento; el usuario queda en la excepción doméstica |
| Validación con 20 usuarios | Consentimiento explícito y hoja informativa antes de la primera medición. Solo métricas mínimas, seudonimizadas, con plazo de borrado y registro de actividades |
| Proveedor de IA | Pantalla «Tu IA y tus datos», con instrucciones para desactivar el entrenamiento en Claude y ChatGPT |
| Telemetría | Ninguna |
| Ley de IA | El motor de reglas, con aleatorización simple y sin aprendizaje, probablemente queda fuera de la definición de sistema de IA (a confirmar con un abogado). Si hay chat propio, aviso de IA (art. 50, aplicable desde el 2-08-2026) |
| Versión gestionada | EIPD, contratos de encargo, alojamiento en la UE, brechas en 72 h, aviso 15 días antes de cada renovación (Ley 10/2025) y botón de desistimiento |
| Equipos | Comparten normas y calendario, nunca datos de salud. Sin inferir estrés ni emociones |
| EE. UU. | No vender al principio |
| Abogado | Confirmar que el promotor no es responsable en la versión local. Revisar la Ley de IA (si el motor queda fuera de la definición y el art. 50 si hay chat propio), la validación, la frontera con el producto sanitario, el RD 1907/1996, el art. 22 RGPD, la LSSI y el CRA antes de cobrar |

---

## Modelo de negocio

| Plan | Contenido | Precio orientativo | Cuándo |
|---|---|---|---|
| Open source | Servidor MCP completo, licencia MIT | Gratis | Desde el 20-11-2026 |
| Programa de 30 días | Cohorte de 10-20 fundadores, sesión semanal en grupo y revisión semanal | 49 € (lanzamiento) a 99 € | Enero de 2027 |
| Plan Coach | El cliente comparte un **resumen** semanal con su coach, no los datos en bruto | 29-59 € al mes por coach | Piloto en enero de 2027 |
| Ucoach + coach | Prestado por coaches socios con reparto de ingresos | 99-199 € al mes | Tras el piloto |
| Aceleradoras | Programa para una cohorte | Por cohorte | Primavera de 2027 |
| Pro individual | Avisos móviles y panel, local-first | 8-12 € al mes | Solo si la validación lo pide |

El contenido es el motor: el diario público de uso propio y una newsletter o curso de «rendimiento sostenible del fundador».

---

## Métricas de éxito (validación)

Decisión el 18 de febrero de 2027:

| Métrica | Seguir | Pivotar |
|---|---|---|
| Semana activa (3 rituales o más) en la cohorte guiada | ≥60 % en la semana 4, ≥45 % en la 8 y ≥35 % en la 12 | <20 % en la semana 4 → el problema es el formato |
| Activos en la semana 4, cohorte orgánica (opcional) | ≥20 % | n. a. |
| Tasa de vuelta tras 3 días o más inactivo | ≥50 % en 7 días | n. a. |
| Automaticidad del hábito focal (SRBAI) | +1 punto en la semana 8 | n. a. |
| Destacados cumplidos | Subida entre la semana 1 y la 6 | n. a. |
| Alianza con el coach (escala breve) | Medida a las 2 y a las 6 semanas | n. a. |
| Plazas vendidas en la cohorte de pago | ≥10, con ≥25 % de los activos entre ellas | <5 → reformular la oferta o el público |
| Coaches que renuevan pagando | ≥2 de 3 | 0 → probar aceleradoras |
| «Muy decepcionado» (Sean Ellis) | ≥40 % en algún segmento (indicativo con menos de 40 respuestas) | <25 % en todos |
| Avisos silenciados | <20 % | n. a. |
| Cron activo en la semana 8 | ≥70 % de los usuarios | n. a. |
| Consentimientos firmados antes de medir | 100 % | n. a. |

---

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| ChatGPT o Claude llevan salud, calendario y agente proactivo a la UE | Método y coach humano; independencia de la IA |
| Un wearable añade el calendario | Contexto de trabajo profundo; independencia del dispositivo |
| Abandono tras la primera recaída | Ritual de vuelta, sin rachas, avisos que se retiran, coach humano |
| Complacencia del LLM; respuestas inadecuadas en crisis | Regla antiadulación; derivación con textos fijos |
| Inyección de instrucciones por el calendario; clones del paquete | Entrada saneada, plantillas sin texto libre, firma y checksums |
| Frontera con el producto sanitario o la publicidad sanitaria | Finalidad prevista, lista de palabras, revisión de un abogado |
| El público técnico se lo monta solo con un MCP y un prompt | El método y la memoria longitudinal no caben en un prompt; open source para ganar confianza |

---

## Hoja de ruta

| Fase | Plazo | Entregables |
|---|---|---|
| 0. Uso propio y v0.2 | 20-11 a 17-12-2026 | P0 técnico y legal, método corregido, uso diario con diario público, 15 entrevistas, nombre definitivo, repositorio y landing |
| 1. Validación | 18-12-2026 a 18-02-2027 | 20 usuarios con consentimiento, Show HN y directorios de MCP, cohorte orgánica opcional sin entrevistas, cohorte de pago, piloto con 3 coaches y una aceleradora |
| 2. Coach y conectores | Primavera de 2027 | Plan Coach. Conectores propios solo si se piden: Polar primero, Garmin Personal si la congelación de altas no la afecta y una carpeta de Health Auto Export. Informe HTML semanal |
| 3. Versión gestionada | Solo si la validación lo justifica | Servidor remoto con el SDK oficial, EIPD y app de avisos |

---

## Próximos pasos

1. Buscar la marca «Circalia» en TMview y en la OEPM (clases 9, 41, 42 y 44) y comprobar el precio de los dominios.
2. Recuperar el código de la v0.1 de la sesión del móvil y llevarlo a un repositorio.
3. Aplicar el P0: dual-era, endurecer los datos, sanear el calendario, anotaciones, método y textos corregidos, y la promesa de privacidad.
4. Preparar el consentimiento y la hoja informativa de la validación.
5. Analizar las herramientas que ya usan los coaches (Trainerize, Coachvox AI y otras) antes del piloto.
6. Empezar el uso propio diario y el diario público.

---

*Ucoach ofrece pautas generales de bienestar. No es un producto sanitario ni sustituye el consejo de profesionales de la salud.*
