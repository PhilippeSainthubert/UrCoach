---
kind: qa-report
target: ucoach-analysis.md
mode: deep
verdict: PASS
verdict_es: ENTREGABLE
score: 9.8
score_before_fix: 0.0
score_limited_by: cobertura
coverage_claims: 128
coverage_verified: 121
independent: true
sources: 9
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA de fidelidad · `ucoach-analysis.md`

Verificador independiente: no escribí la síntesis ni los informes. Es un QA de fidelidad: cada afirmación de la síntesis se ha cotejado con el informe que cita (`01` a `09`) y, para el apartado 11, con el frontmatter y la «Re-verificación» de cada `QA-REPORT-0N-*.md`. No se ha buscado en la web.

## Nota: 0.0 / 10 · CORREGIR ANTES DE ENTREGAR

```
python3 nota.py --claims 128 --verificadas 121 --portantes 55 --portantes-ok 52 --criticas 0 --medias 6 --bajas 16 --bloqueos 0
Techo por cobertura 9.45 = 10 x (0.7 x 52/55 + 0.3 x 121/128)
Penalización 10.0 = 1.0 x 6 medias + 0.25 x 16 bajas
Nota 0.0
```

La nota la limitan los **hallazgos**, no la cobertura (el techo es 9,45). No hay ninguna crítica: ninguna decisión, cifra de uso ni afirmación legal es infiel al informe que cita. La nota cae a 0 por la suma de 6 medias y 16 bajas, casi todas de una línea. Corregidas las 6 medias y las bajas, la nota quedaría en el techo de cobertura (unos 9,5).

## Cobertura

| Concepto | Cifra |
|---|---|
| Afirmaciones verificables extraídas | 128 (el preflight contó 38; se usa el mayor) |
| Portantes | 55 |
| Portantes cotejadas con el informe | 55 de 55 |
| Portantes fieles sin reservas | 52 de 55 (las 3 restantes son M1, M2 y M3) |
| De apoyo cotejadas | 66 de 73 |
| Total cotejadas | 121 de 128 |
| Informes leídos | 9 (`01` a `09`) más los 8 QA-REPORT |

Sin cotejar (7 de apoyo, de contexto): el texto exacto de algunas filas de la tabla del apartado 1 que repiten datos ya verificados en otros apartados, y los detalles cosméticos del diagrama del apartado 5.

## Veredicto

**CORREGIR ANTES DE ENTREGAR** (`NEEDS REVISION`). No hay críticas, pero quedan 6 medias abiertas. La síntesis es muy fiel en lo esencial: las cifras de cafeína, los umbrales de métricas, las fechas regulatorias, los niveles A-D, los precios del modelo de negocio y el plan de 90 días coinciden con los informes corregidos. Los problemas son de tres tipos:
1. una salvedad corregida tras la QA que se ha perdido (micropausas);
2. tres tensiones entre informes que la síntesis no ve y que no están en la tabla del apartado 8 (Garmin, TCC-I frente a la frontera sanitaria, sensación subjetiva frente a deuda acumulada);
3. dos afirmaciones que van algo más allá del informe en lo legal o en el mensaje (energía y ánimo como datos de salud, frase de rendimiento que `05` señala bajo el RD 1907/1996).

## Hallazgos por gravedad

### Críticas

Ninguna.

### Medias

**M1 · STALE / OVERCLAIM · Micropausas cada ~30 min sin la población estudiada**
- **Dice la síntesis** (l. 50): «Las micropausas cada ~30 min tienen beneficio metabólico». También l. 101 (regla de movimiento) y l. 342 (apartado 8), sin ninguna salvedad.
- **Dice el informe** (`02-evidencia-protocolos.md`, l. 22, l. 46 y l. 213): el beneficio se ha visto «en adultos con sobrepeso u obesidad (corregido tras QA 2026-11-19)». La salvedad se añadió en la corrección de la QA y la síntesis usa la versión anterior.
- **Corrección**: l. 50: «Las micropausas cada ~30 min tienen beneficio metabólico en adultos con sobrepeso u obesidad». En l. 101, añadir «(evidencia en adultos con sobrepeso u obesidad)».

**M2 · Contradicción entre informes no resuelta · Garmin**
- **Dice la síntesis** (l. 247): P2, «Garmin Personal (clave propia) o Polar». Y en l. 265, dentro del apartado atribuido a `04`: «Garmin congeló las altas nuevas a su programa de desarrolladores en 2026».
- **Dice el informe**: la congelación sale de `01-mercado-competencia.md`, l. 221 («Garmin congeló las altas nuevas desde la primavera de 2026; en octubre seguía cerrada»), y `QA-REPORT-01`, l. 184, concluye que «hoy un conector oficial con Garmin no es viable». `04-mcp-seguridad-conectores.md` no menciona la congelación y recomienda Garmin Personal como la vía más barata (l. 208 y l. 250).
- **Corrección**: en l. 265 citar `01`, no `04`. Añadir una fila al apartado 8: «Garmin Personal en la P2 (`04`) frente a la congelación de altas de Garmin (`01`)», con una resolución: comprobar si la vía Personal está afectada por la congelación antes de la P2; mientras tanto, Polar como primera opción.

**M3 · OVERCLAIM legal · Energía y ánimo como datos de salud**
- **Dice la síntesis** (l. 277): «La energía y el ánimo seguidos en el tiempo también cuentan como datos de salud».
- **Dice el informe** (`05-privacidad-regulacion.md`, l. 20): «también lo son **con alta probabilidad** […] Conviene tratar la base entera como categoría especial» (`verified` + `inferred`).
- **Corrección**: «La energía y el ánimo seguidos en el tiempo y cruzados con el sueño son, con alta probabilidad, datos de salud: se trata toda la base como categoría especial». No cambia ninguna decisión; corrige el grado de certeza de una afirmación legal.

**M4 · Mensaje que `05` sitúa bajo el RD 1907/1996**
- **Dice la síntesis** (l. 77): «vender rendimiento («llega a la negociación de mañana con energía») sin prometer resultados de salud». La misma frase es el modelo del mensaje. En l. 11, «con energía y sueño en su mejor nivel».
- **Dice el informe** (`05-privacidad-regulacion.md`, l. 275): el RD 1907/1996 «también lo es para el mensaje de "rendimiento" que recomienda el informe 03 ("Llega a la negociación de mañana con energía") […] Hay que redactar el rendimiento como organización y hábitos, sin prometer efectos sobre el estado físico o mental». La alternativa segura está en l. 297. `QA-REPORT-05`, l. 205, pide que un abogado revise sobre todo este punto.
- **Corrección**: en l. 77 sustituir el ejemplo por la alternativa de `05`: «organiza tu día para llegar con energía a lo importante» o «planifica en función de cómo has dormido», y añadir «(la frase de `03` está pendiente de revisión jurídica)». En l. 11, «que cuida la energía y el sueño como base del trabajo».

**M5 · Omisión · La regla de insomnio choca con la frontera sanitaria de `05`**
- **Dice la síntesis** (l. 111): con dificultad para dormir «3 noches o más por semana durante 3 meses o más […] se recomienda la TCC-I […]. Se incluye la regla de levantarse si no se duerme en unos 20 minutos».
- **Dice el informe**: la regla es fiel a `02-evidencia-protocolos.md`, l. 363. Pero `05-privacidad-regulacion.md`, l. 318, dice que «Ucoach no debe "aplicar" TCC-I»; la l. 289 limita «insomnio» a una derivación («Si te cuesta dormir de forma habitual, consulta a un profesional») y la l. 352 pide revisión jurídica de «los textos de sueño y de la ficha de TCC-I». La regla de los 20 minutos es un componente de la TCC-I (control de estímulos), y el umbral de 3 noches y 3 meses es el criterio clínico. La fila 4 del apartado 8 resuelve el burnout y el insomnio en general, pero no esta regla.
- **Corrección**: en l. 111 aclarar que el umbral es interno y no se muestra; que el texto al usuario es el de `05` (sin nombrar el insomnio); que la TCC-I se menciona solo como derivación a un profesional; y marcar la regla de los 20 minutos como pendiente de revisión jurídica. Añadir la tensión `02` / `05` al apartado 8.

**M6 · Omisión · «La sensación subjetiva manda» frente a la deuda acumulada**
- **Dice la síntesis** (l. 94): «La sensación subjetiva manda sobre la puntuación del wearable». Y en l. 182, con deuda de sueño, el aviso de decisiones irreversibles.
- **Dice el informe**: `03-retencion-conducta.md`, l. 123, y `02-evidencia-protocolos.md`, l. 370, dan prioridad a lo que siente el usuario. Pero `08-rendimiento-coaching.md`, l. 35 (Van Dongen 2003, `sólido`), dice: «Con deuda acumulada, avisar aunque el usuario "se sienta bien"», porque quien acumula deuda no lo nota. La síntesis no recoge la tensión ni la resuelve, y la regla tal como está escrita apagaría el aviso justo en el caso que describe `08`.
- **Corrección**: en l. 94: «Tras una noche, la sensación subjetiva manda sobre la puntuación del wearable. Con deuda acumulada (media de 7 días por debajo de 6 h), el aviso se mantiene aunque el usuario diga sentirse bien (`08`)». Añadir la tensión `02`, `03` / `08` al apartado 8.

### Bajas

**B1 · STALE · Fila 20-20-20 del apartado 8**
- **Dice la síntesis** (l. 343): tensión «La regla 20-20-20 como "lo que mejor funciona" frente a una heurística débil | 07 / 02».
- **Dice el informe**: `07-practicas-complementarias.md`, l. 194, ya no lo dice: «No presenta la regla 20-20-20 como probada» (corregido tras QA, `QA-REPORT-07`, l. 94-95 y l. 315).
- **Corrección**: marcar la fila como «07 / 02 (antes de la QA)», igual que la de la ventana europea (l. 349).

**B2 · Contradicción interna · Pre-mortem**
- **Dice la síntesis**: l. 377, Veinott 2010 entre lo «sin verificar en la QA, y por tanto sin regla que se apoye en ellos»; l. 187, el ritual `pre_mortem` se apoya en Veinott.
- **Dice el informe**: `QA-REPORT-08`, l. 407: «El pre-mortem queda como ritual opcional con evidencia "débil-razonable"».
- **Corrección**: en l. 375, «Sin verificar en la QA (solo sostienen, como mucho, rituales opcionales)», o sacar a Veinott de esa lista y remitir a l. 187.

**B3 · OVERCLAIM · Proceso del QA**
- **Dice la síntesis** (l. 388): cada informe pasó por «el cotejo de las críticas corregidas desde la sesión principal».
- **Dice el informe**: `QA-REPORT-06-negocio-gtm.md` no tiene sección de cotejo por un tercero, aunque tuvo una crítica (l. 51). `QA-REPORT-03` no tuvo críticas. Los otros seis sí la tienen.
- **Corrección**: «… y, en seis de los ocho, el cotejo de las críticas corregidas desde la sesión principal (en `03` no hubo críticas; en `06` no consta)».

**B4 · Apartado 11 · «Ninguno abierto» en el informe 05**
- **Dice la síntesis** (l. 396): «Qué limita la nota: Ninguno abierto».
- **Dice el informe**: `QA-REPORT-05`, l. 198-203: queda 1 baja abierta (H-B12, normas no analizadas), con penalización de 0,25. El frontmatter dice `score_limited_by: hallazgos`.
- **Corrección**: «Una baja abierta (normas no analizadas)».

**B5 · Salvedad perdida · WOOP**
- **Dice la síntesis** (l. 182): «WOOP breve: g = 0,34, Wang 2021».
- **Dice el informe** (`08`, l. 20): «mayor cuando lo guía una persona. Que una IA consiga ese mismo efecto es una hipótesis que hay que medir (corregido tras QA 2026-11-19)».
- **Corrección**: añadir «efecto con guía humana; con IA está por medir».

**B6 · OVERCLAIM · «La única excepción»**
- **Dice la síntesis** (l. 123): el ejercicio «es la única excepción razonable a "un hábito cada vez"».
- **Dice el informe** (`02`, l. 372): «Es una excepción razonable».
- **Corrección**: «Es una excepción razonable».

**B7 · Matiz perdido · 112**
- **Dice la síntesis** (l. 113): «024 y 112».
- **Dice el informe** (`08`, l. 448): 024, «y **112** si hay peligro inmediato».
- **Corrección**: «024, y 112 si hay peligro inmediato».

**B8 · Lista incompleta presentada como completa · Campos del catálogo**
- **Dice la síntesis** (l. 142): «un recurso con los campos `practica`, `nivel`, `evidencia`, `fuente`, `anio_fuente`, `riesgos`, `pauta`, `disparador` y `revisado_el`».
- **Dice el informe** (`07`, l. 631): además `para_que`, `contraindicaciones` y `momento`.
- **Corrección**: añadir los tres campos o escribir «entre otros».

**B9 · DISCREPANCY menor · Pausa activa de la v0.1**
- **Dice la síntesis** (l. 50): «Pausa activa de 5 min cada 90 min».
- **Dice el informe** (`02`, l. 46): «Pausa activa de 5 min cada 60-90 min».
- **Corrección**: «cada 60-90 min».

**B10 · Escritura · Fechas relativas**
- **Dice la síntesis**: l. 44, «Ahora es Google Health Coach»; l. 73, «ChatGPT y Claude aún no leen datos de salud aquí».
- **Dice el informe**: `01` y `06` lo fechan (desde el 19-5-2026; «a noviembre de 2026»).
- **Corrección**: l. 44, «Desde el 19-5-2026 es Google Health Coach»; l. 73, «a noviembre de 2026, ChatGPT y Claude no leen datos de salud en Europa».

**B11 · Resolución que cambia el canal de H1 sin decirlo**
- **Dice la síntesis** (l. 347): «Tarea local de Claude Desktop con `nudge` de respaldo. […] H1 se mide con ese canal».
- **Dice el informe**: `06`, l. 136, medía H1 con el brief que «lo dispara el cron local y llega por Telegram». `04`, l. 109: la tarea local solo corre «con la app abierta y el equipo despierto».
- **Corrección**: añadir que H1 pasa a depender de que Claude Desktop esté abierto y que, para medirlo, cuentan también los briefs abiertos tras el aviso de las 09:00.

**B12 · Omisión · Lista del abogado**
- **Dice la síntesis** (l. 291-297): empieza por «que la validación cumple».
- **Dice el informe** (`05`, l. 349): «Que el promotor no es responsable en la versión local y que la fase de validación cumple».
- **Corrección**: añadir «que el promotor no es responsable del tratamiento en la versión local».

**B13 · Precisión · Gafas de luz azul**
- **Dice la síntesis** (l. 20): «las gafas de luz azul en D».
- **Dice el informe** (`07`, l. 190 y l. 197): D son las de luz azul **de día**; las ámbar nocturnas son C.
- **Corrección**: «las gafas de luz azul de día en D».

**B14 · DISCREPANCY de redacción · NICE NG59**
- **Dice la síntesis** (l. 379): «las cifras de NICE NG59 tras 2026».
- **Dice el informe** (`07`, l. 729): «NICE NG59 sigue sin poder abrirse: no se ha confirmado ninguna actualización de 2026».
- **Corrección**: «si NICE NG59 tiene alguna actualización posterior a 2020».

**B15 · Contradicción interna · Cohorte orgánica sin cohorte en el plan**
- **Dice la síntesis**: l. 325 fija «Cohorte orgánica sin entrevistas ≥20 % activos en la semana 4», pero el plan de 90 días (l. 316-318) solo tiene los 20 usuarios guiados y la cohorte de pago.
- **Dice el informe**: `03`, l. 228, propone una «Cohorte B de 10-20 usuarios orgánicos sin entrevistas semanales»; `06` no la incluye en su plan.
- **Corrección**: añadir la cohorte B al plan (semanas 5-8, tras el Show HN) y decir cómo se mide sin telemetría, o marcar la métrica como opcional.

**B16 · Omisión · Mensaje de `06` con la promesa que `05` prohíbe**
- **Dice la síntesis**: no avisa de que `06` propone un mensaje con la promesa falsa.
- **Dice el informe**: `06`, l. 168, «Mensaje propuesto: […] Tus datos no salen de tu ordenador», que `05`, l. 285, declara falso.
- **Corrección**: en el apartado 6, punto 1, añadir «y el mensaje propuesto en `06`, apartado 8».

## Contradicciones internas

1. **Pre-mortem**: ritual que se apoya en Veinott (l. 187) frente a «sin regla que se apoye en ellos» (l. 377). Ver B2.
2. **Garmin**: P2 con Garmin Personal (l. 247) frente a la congelación de altas (l. 265), atribuida además al informe equivocado. Ver M2.
3. **Sensación subjetiva frente a deuda**: «la sensación subjetiva manda» (l. 94) frente al aviso de decisiones irreversibles con deuda de sueño (l. 106 y l. 182), sin regla para cuando el usuario dice sentirse bien con deuda acumulada. Ver M6.
4. **Cohorte orgánica**: métrica de decisión (l. 325) sin cohorte en el plan (l. 316-318). Ver B15.
5. **Mensaje**: el ejemplo de l. 77 contradice la regla de la misma línea («sin prometer resultados de salud») según la lectura de `05`. Ver M4.

No he encontrado umbrales con dos valores distintos: la cafeína (9 h y 13,5 h, 400 mg), los avisos (1-3, máximo 4, 60 min), el hábito focal (8-10 semanas), los informes personales (14 días y 5 por grupo) y las métricas son coherentes en todo el documento.

## Revisión de la tabla del apartado 8

| Fila | ¿Coherente con los informes? |
|---|---|
| Micropausas frente a 1-3 avisos | Sí (`02`, l. 213; `03`, l. 193), salvo la población estudiada (M1) |
| 20-20-20 | La resolución es correcta, pero la tensión ya no existe tras la QA de `07` (B1) |
| Motor que aprende frente a sistema de IA | Sí (`03`, «Lectura para Ucoach»; `05`, apartado 3.3) |
| Detectar burnout o insomnio | Sí (`03`, recomendación 16; `05`, l. 289-291), pero no cubre la regla de TCC-I del apartado 3.2 (M5) |
| Experimentos con 20 usuarios | Sí (`03`, recomendación 3; `05`, P0-3) |
| Brief automático frente a nube | Coherente con `04`; cambia el canal de H1 de `06` sin decirlo (B11) |
| «Vive dentro de tu IA» frente a avisos sin IA | Sí (`04`, reglas de diseño 1 y 2) |
| Ventana europea | Sí, bien marcada como anterior a la QA |
| Retención ≥40 % frente a semana activa ≥60 % | Sí: adopta las definiciones de `03` y el pivote <20 % de `06` (l. 149 de `06`), y lo declara |
| Un hábito cada vez frente a ejercicio | Sí (`02`, l. 372), salvo el «única» de l. 123 (B6) |
| Conectores P2 frente a 90 días | Sí, pero falta la tensión de Garmin (M2) |
| **Faltan** | Garmin `01` / `04` (M2); TCC-I `02` / `05` (M5); sensación subjetiva `02`, `03` / `08` (M6) |

## Omisiones

- Las tres tensiones entre informes de M2, M5 y M6. Cada una cambia una regla de producto.
- `QA-REPORT-05`, l. 205, pide que un abogado revise «sobre todo el RD 1907/1996 aplicado al mensaje de rendimiento»; la síntesis lo incluye en la lista (l. 296), pero sigue usando la frase como modelo (M4).
- `QA-REPORT-06`, l. 344, da como alternativa para cerrar M12 «recortar el plan Coach a hipótesis hasta tener esa tabla». La síntesis lo trata bien en l. 310 y l. 373, pero el resumen ejecutivo (l. 25) presenta el plan Coach como «negocio recurrente» sin esa reserva. No lo cuento como hallazgo aparte; conviene añadir «(hipótesis H3)» en l. 25.
- `06`, l. 168: el mensaje propuesto con «Tus datos no salen de tu ordenador» (B16).

## Escritura

- Guiones largos (raya y semirraya): 0.
- Castellano de España: correcto en todo el documento.
- Fechas relativas: dos casos (B10).
- Promesas de salud del apartado 4 de `05`: no aparece ninguna de la lista literal. La frase de l. 77 es la que `05` señala en su apartado 3.10 (M4), y «en su mejor nivel» (l. 11) roza el «más energía garantizada».

## Sólido

- **Cifras del método**: cafeína (≥9 h, ≥13,5 h y 400 mg; `02`, l. 40), luz desde 3 h antes, media de 3-7 noches y nivel «largo», ±30-60 min, 60-120 min tras 2-3 semanas, Microsoft n=14, 7.000-8.000 pasos, 20-25 °C solo en mayores de 65 y TCC-I con 3 noches y 3 meses: todo coincide con `02` corregido.
- **Niveles A-D** (apartado 3.3): todas las prácticas listadas tienen el nivel de `07` tras la QA, incluidas las que cambiaron (EFT en C, tapones y paseos en B). La política para C y D coincide con `07`, l. 606.
- **Retención y avisos**: 1-3 avisos, máximo 4, nunca dos en 60 min, retirada tras umbral o 3 semanas, «5 de 7», 14 días y 5 por grupo, Milkman, Silverman y Barasch, y HeartSteps a unas 4 semanas: fiel a `03`.
- **Técnica**: dual-era 2025-11-25 y 2026-07-28, -32022 y -32601, `.mcpb` privado sin directorio, plugin, launchd frente a cron, LayerX, 0700/0600 con WAL y SHM, Terra desde 499 $/mes, `mcp` 2.3.0 con 14 dependencias, Oura sin tokens personales desde 12-2025, WHOOP con 10 miembros y Fitbit apagada el 2-11-2026: fiel a `04`.
- **Regulación**: Reglamento 2026/1744 (2-12-2027 y 2-08-2028; art. 50 desde 2-08-2026), Ley 10/2025 (15 días), Directiva 2023/2673 sin transponer a 04-11-2026, art. 5.1.f, art. 9.2.a, EIPD «que hay que hacer», RD 1907/1996 y FTC más Washington: fiel a `05` corregido.
- **Negocio**: ruta F, C, B y D; 49-99 €, 29-59 €/mes, 99-199 €/mes y 8-12 €/mes; Paperbell 175-350 $; plan del 20-11-2026 al 18-02-2027 con venta el 22-12, cohorte del 19-01 al 17-02 y piloto desde el 15-01; criterios de pago, coaches y Sean Ellis: fiel a `06` corregido.
- **Nombre**: USPTO 3536981 en clases 35, 41, 42 y 45; Circalia con .ai, .app, .coach y getcircalia.com libres; circalia.com de febrero de 2026; clases 9, 41, 42 y 44 para la búsqueda: fiel a `06` y `09`.
- **Apartado 11**: las notas antes y después, los veredictos y las coberturas de los ocho informes coinciden con el frontmatter de cada QA-REPORT. El «81 de 81 (unas 170)» de `04` y el «Dos portantes sin verificar» de `08` coinciden con el cuerpo de sus QA. El aviso de Hungría, Países Bajos y la TGA (l. 381) coincide con `QA-REPORT-07`, l. 367.

## Correcciones a aplicar

1. **l. 11**: «con energía y sueño en su mejor nivel» → «que cuida la energía y el sueño como base del trabajo» (M4).
2. **l. 20**: «las gafas de luz azul en D» → «las gafas de luz azul de día en D» (B13).
3. **l. 25**: añadir «(hipótesis H3, pendiente de analizar las herramientas para coaches)» tras «plan Coach» (omisión).
4. **l. 44**: «Ahora es Google Health Coach» → «Desde el 19-5-2026 es Google Health Coach» (B10).
5. **l. 50**: «cada 90 min» → «cada 60-90 min»; «tienen beneficio metabólico» → «tienen beneficio metabólico en adultos con sobrepeso u obesidad» (B9, M1).
6. **l. 73**: «aún no leen datos de salud aquí» → «a noviembre de 2026, no leen datos de salud en Europa» (B10).
7. **l. 77**: sustituir el ejemplo «llega a la negociación de mañana con energía» por «organiza tu día para llegar con energía a lo importante» y anotar que la frase de `03` está pendiente de revisión jurídica (M4).
8. **l. 94**: «La sensación subjetiva manda sobre la puntuación del wearable» → «Tras una noche, la sensación subjetiva manda sobre la puntuación del wearable; con deuda acumulada, el aviso se mantiene aunque el usuario diga sentirse bien (`08`)» (M6).
9. **l. 101**: añadir «(evidencia en adultos con sobrepeso u obesidad)» tras «cada ~30 min» (M1).
10. **l. 111**: añadir que el umbral es interno, que el texto al usuario no nombra el insomnio (`05`, l. 289), que la TCC-I solo se menciona como derivación y que la regla de los 20 minutos queda pendiente de revisión jurídica (M5).
11. **l. 113**: «024 y 112» → «024, y 112 si hay peligro inmediato» (B7).
12. **l. 123**: «Es la única excepción razonable» → «Es una excepción razonable» (B6).
13. **l. 142**: añadir `para_que`, `contraindicaciones` y `momento` a la lista de campos (B8).
14. **l. 182**: tras «g = 0,34, Wang 2021», añadir «con guía humana; con IA, por medir» (B5).
15. **l. 247 y l. 265**: en l. 265 citar `01` como fuente de la congelación de Garmin; en l. 247 poner Polar primero y «Garmin Personal, si la congelación no la afecta» (M2).
16. **l. 277**: «también cuentan como datos de salud» → «son, con alta probabilidad, datos de salud: se trata toda la base como categoría especial» (M3).
17. **l. 274**: añadir «y el mensaje propuesto en `06`, apartado 8» a lo que hay que corregir (B16).
18. **l. 291**: añadir a la lista del abogado «que el promotor no es responsable del tratamiento en la versión local» (B12).
19. **l. 316-318 o l. 325**: añadir la cohorte orgánica B al plan de las semanas 5-8 con su forma de medir, o marcar la métrica como opcional (B15).
20. **l. 343**: «07 / 02» → «07 / 02 (antes de la QA)» (B1).
21. **l. 347**: añadir que H1 depende de que Claude Desktop esté abierto y que cuentan los briefs abiertos tras el aviso de las 09:00 (B11).
22. **Apartado 8, tabla**: añadir tres filas: Garmin Personal (`04`) frente a la congelación (`01`); TCC-I y regla de 20 minutos (`02`) frente a «no aplicar TCC-I» (`05`); sensación subjetiva (`02`, `03`) frente a deuda acumulada (`08`) (M2, M5, M6).
23. **l. 375-377**: precisar que lo no verificado solo sostiene, como mucho, rituales opcionales (el `pre_mortem`) (B2).
24. **l. 379**: «las cifras de NICE NG59 tras 2026» → «si NICE NG59 tiene alguna actualización posterior a 2020» (B14).
25. **l. 388**: «el cotejo de las críticas corregidas desde la sesión principal» → «y, en seis de los ocho, el cotejo de las críticas corregidas desde la sesión principal» (B3).
26. **l. 396**: «Ninguno abierto» → «Una baja abierta (normas no analizadas)» (B4).

## Re-verificación (2026-11-19)

Las correcciones las aplicó el coordinador; yo no escribí ni la síntesis ni las correcciones. He cotejado cada línea nueva con el informe de origen, no solo con mi propuesta.

| Hallazgo | Estado | Línea nueva |
|---|---|---|
| M1 · micropausas sin población | corregido y fiel a `02`, l. 46 y 213 | 50, 101 |
| M2 · Garmin | corregido: la congelación cita `01`; Polar primero; fila nueva en el apartado 8, coherente con `01`, l. 221 y `04`, l. 208 | 247, 265, 354 |
| M3 · energía y ánimo como datos de salud | corregido: «con alta probabilidad», como `05`, l. 20 | 277 |
| M4 · mensaje de rendimiento | corregido: el modelo es la alternativa de `05`, l. 297, y la frase de `03` queda pendiente de revisión jurídica | 11, 77 |
| M5 · insomnio y TCC-I | corregido: umbral interno, sin nombrar el insomnio, TCC-I solo como derivación, regla de 20 min pendiente; fila nueva fiel a `02`, l. 363 y `05`, l. 289 y 318 | 111, 355 |
| M6 · sensación subjetiva frente a deuda | corregido: fiel a `02`, l. 370, `03`, l. 123 y `08`, l. 35; fila nueva | 94, 356 |
| B1 · 20-20-20 | corregido | 344 |
| B2 · pre-mortem | corregido | 379 |
| B3 · cotejo desde la sesión principal | corregido | 392 |
| B4 · «Ninguno abierto» en `05` | corregido | 400 |
| B5 · WOOP | corregido | 182 |
| B6 · «la única excepción» | corregido | 123 |
| B7 · 112 | corregido | 113 |
| B8 · campos del catálogo | corregido: coincide con `07`, l. 631 | 142 |
| B9 · pausa de la v0.1 | corregido | 50 |
| B10 · fechas relativas | corregido | 44, 73 |
| B11 · canal de H1 | corregido | 348 |
| B12 · lista del abogado | corregido | 292 |
| B13 · gafas de luz azul de día | corregido | 20 |
| B14 · NICE NG59 | corregido | 383 |
| B15 · cohorte orgánica | corregido: opcional, 10-20 usuarios como en `03`, l. 228 | 318 |
| B16 · mensaje de `06` | corregido | 274 |
| Omisión · plan Coach como hipótesis | corregido | 25 |

Las 26 correcciones de la lista están aplicadas. Las tres filas nuevas del apartado 8 son coherentes con los informes. La de la sensación subjetiva dice «media de varias noches» en lugar de un umbral; es fiel a `08`, que habla de deuda acumulada sin fijar la media, así que no lo cuento como hallazgo.

**Hallazgos nuevos introducidos por las correcciones** (bajas):
- **N1 · l. 77 · repetición.** La frase «organiza tu día para llegar con energía a lo importante» aparece dos veces en el mismo párrafo. Corrección: quitar la última frase («Hay que usar formulaciones como…») o cambiarla por la cita de `05`, apartado 4.
- **N2 · l. 19 · contradicción con l. 111.** «Se añaden la TCC-I» choca con la regla nueva («Ucoach no aplica la TCC-I»; solo se menciona como derivación). Corrección: «Se añaden la derivación a la TCC-I y una tabla fija de derivación».

**Nota tras corregir** (solo lo abierto: 0 críticas, 0 medias, 2 bajas):

```
python3 nota.py --claims 128 --verificadas 121 --portantes 55 --portantes-ok 55 --criticas 0 --medias 0 --bajas 2 --bloqueos 0
Nota QA: 9.5 / 10 · ENTREGABLE
Techo por cobertura 9.84 · Penalización 0.5
```

**Veredicto tras corregir: ENTREGABLE** (`PASS`). No quedan críticas ni medias y las 55 portantes son fieles. La nota la limitan las dos bajas nuevas (N1 y N2); corregidas, subiría al techo de cobertura (9,8). La cobertura no cambia: 121 de 128 afirmaciones cotejadas.

### Segunda re-verificación (2026-11-19)

| Hallazgo | Estado | Línea nueva |
|---|---|---|
| N1 · frase repetida | corregido: la frase de ejemplo sale una sola vez y el párrafo remite a `05`, apartado 4 | 77 |
| N2 · «Se añaden la TCC-I» | corregido: «la derivación a la TCC-I (Ucoach no la aplica)», coherente con l. 111 y l. 355 | 19 |

No hay contradicciones nuevas. Nota con lo que queda abierto (nada):

```
python3 nota.py --claims 128 --verificadas 121 --portantes 55 --portantes-ok 55 --criticas 0 --medias 0 --bajas 0 --bloqueos 0
Nota QA: 9.8 / 10 · ENTREGABLE
Techo por cobertura 9.84 · Penalización 0
```

**Veredicto final: ENTREGABLE** (`PASS`). No queda ningún hallazgo abierto. La nota la limita solo la cobertura: 121 de 128 afirmaciones cotejadas, con las 55 portantes incluidas.
