---
kind: qa-report
target: documento-producto-v0.2.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 9.8
score_before_fix: 4.8
score_limited_by: hallazgos
coverage_claims: 140
coverage_verified: 134
independent: true
sources: 10
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA de fidelidad · `documento-producto-v0.2.md`

Verificador independiente: no escribí el documento ni la síntesis. Fuentes: la síntesis corregida (`research/ucoach-analysis.md`) y los nueve informes de `research/` (`01` a `09`). Cada regla, umbral, nivel, precio, plazo, métrica y afirmación legal se ha cotejado con la síntesis y, cuando hacía falta, con el informe de origen. No se ha buscado en la web.

## Nota: 4.8 / 10 · CORREGIR ANTES DE ENTREGAR

```
python3 nota.py --claims 140 --verificadas 134 --portantes 80 --portantes-ok 75 --criticas 0 --medias 3 --bajas 9 --bloqueos 0
Techo por cobertura 9.43 = 10 x (0.7 x 75/80 + 0.3 x 134/140)
Penalización 5.25 = 1.0 x 3 medias + 0.25 x 9 bajas
Nota 4.8
```

La nota la limitan los **hallazgos**; el techo de cobertura es 9,4. No hay críticas. Las tres medias se corrigen con una línea o una tabla corta cada una. Con todo corregido, la nota quedaría cerca del techo.

## Cobertura

| Concepto | Cifra |
|---|---|
| Afirmaciones verificables extraídas | 140 (el preflight contó 19; se usa el mayor) |
| Portantes | 80 (reglas, derivación, niveles, privacidad y ley, precios, plazos, métricas, arquitectura) |
| Portantes fieles sin reservas | 75 de 80 |
| De apoyo cotejadas | 54 de 60 |
| Total cotejadas | 134 de 140 |

Sin cotejar (6 de apoyo): frases de contexto del apartado «Problema» («los hábitos son lo primero que cae») y pasos operativos de «Próximos pasos» (recuperar el código de la v0.1), que no son afirmaciones del research.

**Hereda de la v0.1** (no es un fallo, no viene del research): el entreno de 45 min (l. 119), la preparación de 10 min antes de las reuniones clave (l. 117), las 12 herramientas de la v0.1 (l. 187), el ejemplo de las 5,2 h (l. 70) y el chequeo de ergonomía del `onboarding` (l. 179).

Los equivalentes de M1, M4, M5 y M6, la congelación de Garmin y el 112 están bien aplicados (l. 118, l. 3 y 9, l. 134, l. 111, l. 302 y l. 131).

## Veredicto

**CORREGIR ANTES DE ENTREGAR** (`NEEDS REVISION`). El documento es fiel a la síntesis en casi todo: cifras de cafeína, sueño, luz, foco, movimiento, niveles A-D, precios (49-99 €, 29-59 €/mes, 99-199 €/mes y 8-12 €/mes), umbrales de métricas, fechas de la hoja de ruta, finalidad prevista literal de `05` y arquitectura de `04`. No usa ninguna frase de la lista de palabras que hay que evitar, no tiene guiones largos y solo tiene una fecha relativa. Quedan tres medias: una afirmación legal más tajante que `05` sin pasar por el abogado, una derivación de espalda sin las señales de alarma que obligan a ir al médico y unas métricas sin criterios de pivote.

## Hallazgos por gravedad

### Críticas

Ninguna.

### Medias

**VM1 · OVERCLAIM legal · Ley de IA**
- **Dice el documento** (l. 241): «El motor de reglas, con aleatorización simple y sin aprendizaje, queda fuera de la definición de sistema de IA». En la fila del abogado (l. 245) no aparece la Ley de IA.
- **Dicen los informes**: `05-privacidad-regulacion.md`, l. 115: «la versión local **probablemente** queda fuera de la ley», `inferred` ⚖️; y l. 353 lo pone en la lista del abogado: «Ley de IA: si el motor queda fuera de la definición de sistema de IA». La síntesis (l. 345) sigue a `03`, que lo dice sin matiz, pero `05` es el informe legal.
- **Corrección**: l. 241: «El motor de reglas […] probablemente queda fuera de la definición de sistema de IA (a confirmar con un abogado)». l. 245: añadir «la Ley de IA (si el motor queda fuera de la definición y el art. 50 si hay chat propio)».

**VM2 · Omisión de seguridad · Derivación de espalda y cuello**
- **Dice el documento** (l. 137): «Dolor de espalda o cuello persistente | Fisioterapeuta».
- **Dice el informe**: `07-practicas-complementarias.md`, l. 524: «Señales de alarma que obligan a derivar al médico: pérdida de fuerza, hormigueo que baja por la pierna o el brazo, alteraciones de esfínteres, fiebre, pérdida de peso sin explicación, dolor nocturno que no cede, traumatismo». El fisioterapeuta es «si no mejora en 4-6 semanas» (l. 521). `02`, apartado 13a, dice lo mismo («más de 4-6 semanas o se irradia»).
- **Corrección**: partir la fila en dos: «Dolor de espalda o cuello que no mejora en 4-6 semanas | Fisioterapeuta» y «Pérdida de fuerza, hormigueo que baja por un brazo o una pierna, alteraciones de esfínteres, fiebre, dolor nocturno que no cede o traumatismo | Médico».

**VM3 · Omisión · Métricas sin criterios de decisión**
- **Dice el documento** (l. 264-278): solo objetivos. Faltan los umbrales de pivote, el cron activo en la semana 8 y la salvedad de Sean Ellis.
- **Dicen la síntesis y el informe**: síntesis, l. 323-333 (columna «Pivotar»: <20 % de semanas activas en la semana 4 → formato; <5 plazas → reformular; 0 coaches → aceleradoras; <25 % «muy decepcionado» en todos los segmentos; cron activo ≥70 % en la semana 8; Sean Ellis indicativo con menos de 40 respuestas). `06-negocio-gtm.md`, l. 146-152: son los «Criterios de decisión el 18 de febrero de 2027».
- **Corrección**: añadir a la tabla una columna «Pivotar» con los cuatro umbrales, la fila del cron (≥70 % en la semana 8) y, en Sean Ellis, «(indicativo con menos de 40 respuestas)».

### Bajas

**VB1 · l. 14 · TCC-I.** «dentro la TCC-I» choca con l. 134 («Ucoach no la aplica»). Corrección: «dentro la derivación a la TCC-I». (Es la misma contradicción que N2 en la síntesis.)

**VB2 · l. 17 · Versiones del protocolo.** «El servidor habla las dos versiones vigentes». Según `04`, l. 13, y la síntesis, l. 57, solo la 2026-07-28 es la vigente; la 2025-11-25 es *legacy*. Corrección: «El servidor habla las dos eras del protocolo: la vigente (2026-07-28) y la anterior (2025-11-25)».

**VB3 · l. 93 · Presupuesto de avisos.** «De 1 a 3 avisos al día como máximo». La síntesis (l. 201) y `03` dicen de 1 a 3, «como máximo 4», y nunca dos en 60 minutos. Corrección: «De 1 a 3 avisos al día, nunca más de 4 ni dos en la misma hora».

**VB4 · l. 135 · Regla de conducción sin fuente.** «Con menos de 5 h o mucha somnolencia, no conducir». Viene de `02`, l. 371, marcada `inferred`, y el propio informe (l. 517) dice que falta «buscar una fuente para la regla de conducción» (`QA-REPORT-02`, H-B23, no corregido). No está en la síntesis. Corrección: mantenerla como prudencia, pero marcarla «(pauta prudente sin fuente específica)» o quitar la cifra de 5 h.

**VB5 · l. 131-137 · Derivación incompleta.** Falta «fatiga persistente pese a dormir bien» (síntesis, l. 120; `02`, l. 364, que añade «pérdida de peso sin explicación»). Corrección: añadir la fila «Fatiga persistente pese a dormir bien, pérdida de peso sin explicación | Derivar al médico».

**VB6 · l. 109-123 · Falta la regla de alcohol.** La síntesis (l. 104) la mantiene: «Menos es mejor y cuanto antes, mejor» (`02`, regla 11). Corrección: añadir la fila «Alcohol | Cuanto menos y cuanto antes, mejor».

**VB7 · l. 201 · Herramienta `practica` sin respaldo como herramienta.** Ningún informe propone una herramienta con ese nombre: `07`, l. 631-632, propone un recurso (`practicas.md` o una tabla) que la IA consulta. Es una decisión de diseño razonable, no un hallazgo del research. Corrección: marcarla «(decisión de diseño sobre el recurso que propone `07`)» o dejar solo el recurso de l. 206.

**VB8 · l. 253 · Fecha relativa.** «Desde ya». Corrección: «Desde el 20-11-2026» o «Desde la fase 0».

**VB9 · l. 269 · Cohorte orgánica sin sitio en la hoja de ruta.** La métrica aparece, pero la fase 1 (l. 301) no incluye la cohorte orgánica, que la síntesis (l. 318) marca como opcional. Corrección: añadir «cohorte orgánica opcional tras el Show HN» a la fase 1, o marcar la métrica como opcional.

## Lista de palabras de `05`, escritura y fechas

- **Palabras que hay que evitar** (`05`, apartado 4): ninguna aparece como afirmación del producto. «Diagnosticar, tratar, curar…» solo sale en la finalidad prevista, que es literal de `05`, y en la fila que enumera las palabras prohibidas (l. 235). La promesa de privacidad (l. 233) es la alternativa segura de `05`.
- **Mensaje de rendimiento**: no usa «llega a la negociación de mañana con energía» ni «potencia tu rendimiento». «Coach de rendimiento» (l. 9) y «coach de alto rendimiento» (l. 68) no prometen efectos sobre el estado físico o mental; conviene que el abogado lo mire con el resto del RD 1907/1996, pero no lo cuento como hallazgo.
- **«Insomnio»** aparece en una regla interna (l. 115, «quejas de insomnio»), no en un texto al usuario; el texto que vea el usuario debe ser el de `05` («si te cuesta dormir de forma habitual»).
- **Guiones largos**: 0.
- **Fechas relativas**: una (VB8). «Ahora es un recordatorio opcional» (l. 125) se refiere a la v0.2 frente a la v0.1, no al calendario.
- **Castellano de España**: correcto.

## Sólido

- **Método**: sueño (7-9 h, media de 3 a 7 noches, nivel «largo», regla de la sensación subjetiva con deuda acumulada), despertar ±30-60 min, luz desde 3 h antes, cafeína ≥9 h y ≥13,5 h con 400 mg, siesta antes de las 15:00, foco de 60-120 min, micropausas con su población, 7.000-8.000 pasos, VFC con tendencia de 7 días y decisiones irreversibles con deuda: todo coincide con la síntesis, l. 94-107.
- **Derivación**: 024 y 112 si hay peligro inmediato; regla de dificultad para dormir con la TCC-I solo como derivación; umbrales internos y textos sin trastornos. Fiel a la síntesis, l. 111-120, y a `05`.
- **Niveles A-D**: los ejemplos de cada nivel coinciden con `07`; los usos por nivel, con la política de la síntesis (l. 127).
- **Rituales y herramientas**: `brief_manana` (6 líneas), `cierre_dia` (5 minutos), `retomar` (3 días), `preparar_reunion`, `auditar_agenda`, `registrar_estimacion` y los campos nuevos de `registrar_checkin` y `perfil` coinciden con `08`, apartado 14.
- **Arquitectura**: dual-era, 0700/0600 con WAL y SHM, `nudge` sin LLM y con plantillas fijas, launchd, systemd con `Persistent=true`, Programador de tareas, `.mcpb` privado sin directorio, plugin, brief como tarea local con respaldo a las 09:00, conectores P2 con Polar primero: fiel a `04` y a la síntesis.
- **Privacidad y ley**: promesa y finalidad literales de `05`; art. 9 para toda la base; promotor no responsable en local; consentimiento antes de medir; art. 50 desde el 2-08-2026; Ley 10/2025; Equipos sin datos de salud; EE. UU. aparcado.
- **Negocio y plazos**: precios, cohorte de 10-20 fundadores, aceleradoras con 10-40 fundadores en primavera de 2027, coaches a 175-350 $/mes, fases del 20-11 al 17-12-2026 y del 18-12-2026 al 18-02-2027: fiel a `06` y a la síntesis.

## Correcciones a aplicar

1. **l. 14**: «dentro la TCC-I» → «dentro la derivación a la TCC-I» (VB1).
2. **l. 17**: «El servidor habla las dos versiones vigentes» → «El servidor habla las dos eras del protocolo: la vigente (2026-07-28) y la anterior (2025-11-25)» (VB2).
3. **l. 93**: «De 1 a 3 avisos al día como máximo» → «De 1 a 3 avisos al día, nunca más de 4 ni dos en la misma hora» (VB3).
4. **l. 109-123**: añadir la fila «Alcohol | Cuanto menos y cuanto antes, mejor» (VB6).
5. **l. 135**: marcar «Con menos de 5 h o mucha somnolencia, no conducir» como pauta prudente sin fuente específica, o quitar la cifra (VB4).
6. **l. 137**: partir en «Dolor de espalda o cuello que no mejora en 4-6 semanas | Fisioterapeuta» y «Pérdida de fuerza, hormigueo que baja por un brazo o una pierna, alteraciones de esfínteres, fiebre, dolor nocturno que no cede o traumatismo | Médico» (VM2).
7. **Tras l. 136**: añadir «Fatiga persistente pese a dormir bien, pérdida de peso sin explicación | Derivar al médico» (VB5).
8. **l. 201**: marcar `practica` como decisión de diseño sobre el recurso de `07`, o quitar la herramienta y dejar el recurso de l. 206 (VB7).
9. **l. 241**: «queda fuera de la definición de sistema de IA» → «probablemente queda fuera de la definición de sistema de IA (a confirmar con un abogado)» (VM1).
10. **l. 245**: añadir a la fila del abogado «la Ley de IA (si el motor queda fuera de la definición y el art. 50 si hay chat propio)» (VM1).
11. **l. 253**: «Desde ya» → «Desde el 20-11-2026» (VB8).
12. **l. 264-278**: añadir la columna «Pivotar» (<20 % de semanas activas en la semana 4 → formato; <5 plazas → reformular oferta o público; 0 coaches → probar aceleradoras; <25 % «muy decepcionado» en todos los segmentos), la fila «Cron activo en la semana 8 | ≥70 %» y «(indicativo con menos de 40 respuestas)» en Sean Ellis (VM3).
13. **l. 269 o l. 301**: añadir la cohorte orgánica opcional a la fase 1, o marcar la métrica como opcional (VB9).

## Re-verificación (2026-11-19)

Las correcciones las aplicó el coordinador; yo no escribí el documento ni las correcciones. He cotejado cada línea nueva con la síntesis y con el informe de origen.

| Hallazgo | Estado | Línea nueva |
|---|---|---|
| VM1 · Ley de IA | corregido: «probablemente […] (a confirmar con un abogado)», como `05`, l. 115; la Ley de IA entra en la fila del abogado, como `05`, l. 353 | 244, 248 |
| VM2 · derivación de espalda | corregido: fisioterapeuta si no mejora en 4-6 semanas y médico ante las señales de alarma; fiel a `07`, l. 521 y 524 | 139, 140 |
| VM3 · métricas sin pivote | corregido: columnas «Seguir» y «Pivotar» con los cuatro umbrales, fila del cron ≥70 % y salvedad de Sean Ellis; coincide con la síntesis, l. 323-333, y con `06`, l. 146-152 | 269-284 |
| VB1 · TCC-I | corregido | 14 |
| VB2 · versiones del protocolo | corregido: fiel a `04`, l. 13 | 17 |
| VB3 · presupuesto de avisos | corregido: fiel a `03` y a la síntesis, l. 201-202 | 93 |
| VB4 · regla de conducción | corregido: sin la cifra de 5 h y marcada como pauta prudente sin fuente | 136 |
| VB5 · fatiga persistente | corregido: fiel a `02`, l. 364 | 137 |
| VB6 · alcohol | corregido: fiel a `02`, regla 11 | 121 |
| VB7 · herramienta `practica` | corregido: marcada como decisión de diseño | 204 |
| VB8 · «Desde ya» | corregido | 256 |
| VB9 · cohorte orgánica | corregido: opcional en la métrica y en la fase 1 | 274, 307 |

Las 13 correcciones están aplicadas y son fieles. La tabla de métricas es coherente con la síntesis, y las filas nuevas de derivación también, entre sí y con `07`.

**Hallazgo nuevo introducido por las correcciones** (baja):
- **VN1 · l. 136 frente a l. 115 · siesta y conducción.** La l. 136 propone «no conducir o hacer antes una siesta», pero la regla de la siesta (l. 115) dice «Nunca […] antes de conducir». `02` concilia las dos cosas: tras la siesta, no conducir en los 15-30 minutos siguientes (l. 157). Corrección: l. 136, «no conducir, o hacer una siesta y esperar 15-30 minutos antes de conducir»; l. 115, «ni justo antes de conducir (esperar 15-30 minutos)».

**Nota tras corregir** (solo lo abierto: 0 críticas, 0 medias, 1 baja):

```
python3 nota.py --claims 140 --verificadas 134 --portantes 80 --portantes-ok 80 --criticas 0 --medias 0 --bajas 1 --bloqueos 0
Nota QA: 9.8 / 10 · ENTREGABLE
Techo por cobertura 9.87 · Penalización 0.25
```

**Veredicto tras corregir: ENTREGABLE** (`PASS`). No quedan críticas ni medias, y las 80 portantes son fieles. Queda abierta una baja (VN1). Fuera de la nota siguen los puntos que el propio documento manda al abogado (Ley de IA, RD 1907/1996, validación) y lo heredado de la v0.1, que no viene del research.

## Cierre de la baja VN1 (sesión principal, 2026-11-19)

- VN1 (siesta y conducción) está corregida en las dos líneas. La regla de la siesta dice ahora «tras la siesta, esperar 15-30 min antes de conducir», y la fila de derivación dice «no conducir, o hacer antes una siesta y esperar 15-30 min». Las dos coinciden con `research/02`. No queda ningún hallazgo abierto. La nota (9,8) la limita la cobertura.
