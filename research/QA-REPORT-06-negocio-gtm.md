---
kind: qa-report
target: 06-negocio-gtm.md
mode: deep
verdict: NEEDS REVISION
verdict_es: CORREGIR ANTES DE ENTREGAR
score: 8.3
score_before_fix: 0.0
score_limited_by: cobertura
coverage_claims: 60
coverage_verified: 45
independent: true
sources: 78
searches: 0
qa_at: '2026-11-19T00:00:00Z'
---

# QA · 06 · Modelo de negocio y go-to-market

## Nota: 8.3 / 10 · CORREGIR ANTES DE ENTREGAR (tras corregir)

**Nota antes de corregir: 0.0 / 10 · REHACER.** Tras las correcciones del 2026-11-19 queda abierta una media, M12: falta analizar las herramientas para coaches. La nota la limita la cobertura: 25 de 29 portantes y 45 de 60 afirmaciones verificadas. nota.py la sitúa en la banda «ENTREGABLE CON RESERVAS», pero con una media abierta la regla del veredicto es CORREGIR ANTES DE ENTREGAR. El detalle está en «Re-verificación», al final.

Lo que sigue es el informe original, antes de corregir.

La nota la bajan los hallazgos. Con lo verificado, el techo sería 8,28, pero las penalizaciones suman 22: 1 crítica (3), 2 bloqueos (4), 12 medias (12) y 12 bajas (3). Pesan sobre todo las medias. Muchas no son datos falsos, sino incoherencias del plan de 90 días y cosas del 01 que el 06 no tiene en cuenta.

**Modo**: Deep · **Tipo**: research de negocio y GTM · **Fecha**: 2026-11-19
**Independencia**: verificador en contexto separado ✓. No vio ni el informe ni el mapa, solo `qa/A-preguntas.md`. El cruce se hizo con `qa/A-mapa.md` y `qa/A-respuestas.md`.
**Rúbricas**: sin rúbrica de tipo cargada ⚠
**Voz**: no aplica (documento interno de research)

Cálculo: `nota.py --claims 60 --verificadas 45 --portantes 29 --portantes-ok 25 --criticas 1 --medias 12 --bajas 12 --bloqueos 2`

## Cobertura

| | |
|---|---|
| Afirmaciones en el documento | 60, que es el recuento del preflight. Se extrajeron 51 y las 9 restantes cuentan como no verificadas. |
| Verificadas con fuente consultada | 45 (75 %) |
| Portantes verificadas | 25 de 29 |
| No verificables | 6 filas: A06-19, A06-21, A06-26, A06-29, A06-46 y A06-49 |
| Fuentes distintas del verificador | 78 URL |

Las cuatro portantes que no se pudieron verificar son el clon de Coachvox (A06-19), el mínimo de respuestas de Sean Ellis (A06-21), el efecto del cifrado de extremo a extremo en el RGPD (A06-26) y las marcas en la EUIPO y la OEPM (A06-29).

## Veredicto

**Tras corregir: CORREGIR ANTES DE ENTREGAR** (`NEEDS REVISION`). Queda abierta M12. Ver «Re-verificación».

Antes de corregir: **REHACER** (`MAJOR ISSUES`). Hay una crítica sin resolver: la «ventana europea», que sostiene el hallazgo no obvio y el posicionamiento, afirma que ninguna plataforma ha llevado a la UE sus integraciones de salud. Google sí lo ha hecho, y el propio informe lo da a entender con los «37 países». Además hay dos enlaces muertos y un plan de 90 días con fechas y criterios que no encajan entre sí.

La parte de monetización (MCP, Apps SDK, marketplaces) y los precios de referencia aguantan bien. También aguanta la recomendación de fondo: open source, programa de pago y plan Coach. Hay que corregir el contexto de plataformas, el calendario y los criterios.

## Bloqueos deterministas (preflight)

| Línea | Enlace | Estado | Corrección |
|---|---|---|---|
| 219 | https://www.cronoshare.com/cuanto-cuesta/coaching-empresarial | Sin respuesta en el preflight | El verificador sí lo abrió (MEDIA), así que probablemente bloquea a los robots. Conviene mantenerlo y añadir https://www.cronoshare.com/cuanto-cuesta/servicio-coaching, que también usó el verificador. Sigue contando como bloqueo hasta que el preflight lo dé por bueno. |
| 223 | https://help.risescience.com/hc/en-us/articles/4405177615639-RISE-pricing-and-subscriptions | 404 | Sustituir por https://apps.apple.com/us/app/rise-sleep-tracker/id1453884781, que es la fuente con la que se verificó el precio. |

Los dos 403 (androidauthority.com y paperbell.com) no bloquean. Paperbell lo abrió el verificador sin problema.

Placeholders: 0. Fechas relativas: 0. Guiones largos: el preflight encontró 3 (l. 111, 173 y 180) y, tras la corrección, quedan **0**, comprobado con grep.

## Contrato de escritura y voz

⚠ **No se pudo comprobar.** de-slop no estaba disponible: el preflight no encontró `contar-pruebas.py` y `G4U_DESLOP_SCRIPT` no está definido. Las cuatro pruebas del contrato no se pasaron. Guiones largos: 0 tras la corrección. No hay hallazgos de VOZ porque es un documento interno.

## Hallazgos

### Crítica

**C1 · A06-16 · ERROR (e INTERNAL) · crítica**
- **Dice**:
  - l. 15: «Lo que ninguna ha lanzado es un **método** [...] ni una versión para la UE: las integraciones de salud son solo para EE. UU.». En ese mismo párrafo aparece Google.
  - l. 75: «(3) **lanzar en la UE** las integraciones de salud, que siguen siendo solo para EE. UU.».
  - l. 193: «Hay además una **ventana europea** [...] donde los grandes todavía no han entrado».
  - l. 166: «también en Europa».
  - Contradice las l. 30 y 72 («37 países»).
- **Verificación independiente**:
  - **Google Health Coach** está en 37 países, entre ellos España, Alemania, Francia, Italia y Países Bajos (https://support.google.com/googlehealth/answer/14237941?hl=en). Va incluido sin coste en Google AI Pro y Ultra desde el 19-05-2026 (https://blog.google/products-and-platforms/products/google-health/google-health-coach). Exige Fitbit o Pixel Watch y no usa la agenda.
  - **Claude**: solo EE. UU. (https://www.anthropic.com/news/healthcare-life-sciences).
  - **ChatGPT Health**: excluye el EEE, Suiza y el Reino Unido (https://www.notebookcheck.net/ChatGPT-now-reads-health-data-just-not-in-Germany.1350736.0.html).
- **Corrección**:
  - **Resumen y riesgo de plataforma:** «Claude y ChatGPT no han llevado a la UE sus integraciones de salud. Google sí: Google Health Coach está en España y en casi toda la UE, incluido en Google AI Pro, aunque exige Fitbit o Pixel Watch y no usa la agenda.»
  - **Ventana europea:** acotarla a «usuarios de Claude o ChatGPT, y a quien no lleva Fitbit ni Pixel Watch».
  - **«Qué no han hecho»:** limitar el punto 3 a Claude y ChatGPT.

### Medias

**M1 · A06-04 · DISCREPANCY · media**
- **Dice**: «Los directorios de ChatGPT y Claude no permiten vender suscripciones digitales dentro del chat» (l. 13). En la l. 55: «Ninguna fuente describe listados de pago (2026) | Visibilidad, no ingresos».
- **Verificación independiente**: según la política del directorio (https://support.claude.com/en/articles/13145358), no hay regla sobre conectores de pago y el cobro va por fuera, en la cuenta del servicio. Sí hay conectores listados con planes de pago: athletedata (suscripción, https://claude.com/marketplace/connectors/athletedata), Wellness Project (Pro de 4,99 a 9,99 $, https://wellnessproject.ai/press/claude-directory), Reclaim, Akiflow y Sunsama. El 01 lo recoge (l. 77-78).
- **Corrección**: «El directorio de Claude no cobra en nombre del desarrollador, pero lista conectores cuyo servicio se paga fuera, como athletedata o Wellness Project. Sirve como canal de venta de un servicio, no como cobro por uso». La conclusión de que «el valor de pago vive fuera del MCP» se mantiene y queda reforzada.

**M2 · A06-14 · STALE · media**
- **Dice**: «Ambas tienen agenda y resúmenes proactivos: ChatGPT Pulse desde sept. 2025» (l. 15), y la fila de Pulse (l. 71).
- **Verificación independiente**: OpenAI retiró Pulse el 17-06-2026 y lo sustituyó por tareas programadas con un hub propio (https://engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks).
- **Corrección**: «ChatGPT tiene tareas programadas desde el 17-06-2026, también en Plus; Pulse se retiró ese día».

**M3 · A06-17 · MISSING (INTERNAL con el 01) · media**
- **Dice**: la tabla de riesgo de plataforma (l. 66-73) y «Qué no han hecho» (l. 75) no mencionan ningún agente proactivo de 2026.
- **Verificación independiente**: ninguna plataforma tiene una función que cruce la agenda con la salud, así que esa afirmación aguanta. Pero Claude Duet (21-10-2026: brief matinal de las apps conectadas, en la nube y solo en EE. UU.; https://www.claude.com/resources/articles/claude-duet) y ChatGPT dots (29-09-2026, en la nube, Pro excluye el EEE) existen. El 01 los pone en el centro de su análisis.
- **Corrección**: añadir los dos a la tabla. Duet ya hace el brief matinal con la agenda y solo usa datos de salud si el usuario lo pide. Es el camino más corto para que la plataforma haga «plan del día con sueño y agenda».

**M4 · A06-15 · INTERNAL (con el 01) · media**
- **Dice**: «Tareas programadas incluidas en Pro | Permite programar el brief de mañana sin cron» (l. 69). El plan de 90 días mide el brief (H1, l. 121) sin decir cómo se dispara.
- **Verificación independiente**: desde el 6-10-2026, las tareas de Pro, Max y Ultra se ejecutan en remoto (https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork). Las sesiones remotas no llegan a un MCP local por stdio salvo que la app de escritorio esté abierta y conectada (https://support.claude.com/en/articles/15811196-what-to-expect-with-remote-execution-in-claude-cowork). El 01 (l. 20 y 179) llega a la misma conclusión.
- **Corrección**: precisar que la tarea programada sirve para un brief de la plataforma con sus conectores, no para llamar a Ucoach en local. En el plan, indicar que el brief de Ucoach lo disparan el cron y Telegram, o la app de escritorio abierta. H1 depende de ello.

**M5 · A06-22 · STALE · media**
- **Dice**:
  - l. 19: «ucoach.app (registrado en 2025)».
  - l. 174: «vence el 17 sept. 2026: puede estar en periodo de gracia; vigilar».
  - l. 182: «no tiene ningún dominio principal libre».
- **Verificación independiente**: según RDAP (https://pubapi.registry.google/rdap/domain/ucoach.app), ucoach.app caducó el 17-09-2026 y está en «redemption period» o «pending delete». u-coach.com está en venta. El resto de los dominios se confirma.
- **Corrección**: actualizar las l. 19, 174 y 182. La decisión de buscar otro nombre se mantiene por la marca (M11) y porque «coach» es descriptivo, no por los dominios.

**M6 · A06-27 · DISCREPANCY y PROVENANCE · media**
- **Dice** (l. 129): «De la lista al registro real, entre el 25 y el 85 %, con una media del 50 % si se activa en menos de un mes, y menos del 20 % si se espera más de 3 meses (Lenny, 2022, `verified`)».
- **Verificación independiente**: el artículo es de pago y el verificador lo leyó a través de resúmenes. Da de lista a cliente de pago entre el 5 y el 25 %, unos 20 % si el acceso llega en menos de un mes y menos del 10 % si se espera más de 3 meses. Fuentes: https://www.lennysnewsletter.com/p/what-is-good-waitlist-conversion y https://speedrun.substack.com/p/the-growth-meta-how-to-build-a-waitlist.
- **Corrección**: aclarar a qué métrica se refiere cada cifra (registro o pago) y bajar la etiqueta a `reported` si no se leyó el artículo entero. La conclusión de no hacer esperar a la lista se mantiene.

**M7 · INTERNAL · media**
- **Dice**: «H2: al menos el 25 % de los usuarios activos paga 49 €» (l. 122). Los criterios de la l. 148 dicen «≥ 10 plazas vendidas | < 5 → reformular». En la l. 134 se habla de 20 usuarios activos.
- **Verificación independiente**: es una contradicción interna. Con 20 usuarios activos, cumplir H2 son 5 pagos, que caen en la zona gris entre seguir y pivotar.
- **Corrección**: alinear los dos. Por ejemplo, el criterio «≥ 25 % de los activos o ≥ 10 plazas, contando la lista de espera», y la de pivotar «< 10 % de los activos y < 5 plazas».

**M8 · INTERNAL · media**
- **Dice**: «no tener la lista esperando más de 4 semanas» y «Únete a la cohorte de enero (49 €)» (l. 129). La landing se abre en las semanas 1-4, del 20-11 al 17-12 (l. 125), y la cohorte empieza «el 2 de febrero» (l. 139).
- **Verificación independiente**: es una contradicción interna. La lista esperaría entre 7 y 10 semanas, y la cohorte que se anuncia como «de enero» es de febrero.
- **Corrección**: abrir la landing en la semana 5 o 6, o adelantar la cohorte a mediados de enero. Cambiar «cohorte de enero» por la fecha real.

**M9 · OVERCLAIM · media**
- **Dice** (l. 16): «El canal que más rinde y el comprador que más paga es el coach humano».
- **Verificación independiente**: Paperbell confirma lo que cobran los coaches (175-350 $/mes; https://paperbell.com/blog/what-coaches-charge/), pero ninguna fuente habla del rendimiento del canal. Lo de Coachvox (que los coaches cobran de 10 a 100 £ por su clon) no se pudo verificar (A06-19).
- **Corrección**: «El comprador con más capacidad de pago es el coach humano. Que también sea el mejor canal es la hipótesis H3». Quitar Coachvox de la prueba o marcarlo como no verificado.

**M10 · INTERNAL (con el 01) · media**
- **Dice**: «"Planificador de energía" / "Energy planner" | Recomendado como categoría funcional» (l. 163). Y el mensaje: «Ucoach junta las dos cosas» (l. 166).
- **Verificación independiente**:
  - **Lifestack** se presenta como planificador por energía con Apple Health, Oura, WHOOP, Garmin y Fitbit sobre Google y Outlook (https://itunes.apple.com/lookup?id=6473464429&country=us).
  - **Rise** exporta su previsión de energía a Google y Apple Calendar (https://help.risescience.com/hc/en-us/articles/40610919159575-How-does-RISE-Calendar-Integration-work).
  - El 01 da por falso que ese cruce sea único (l. 121).
- **Corrección**: citar Lifestack y Rise. Apoyar la categoría y el mensaje en el contexto de trabajo y en el método, no en «juntar agenda y sueño».

**M11 · MISSING · media**
- **Dice** (l. 180-182): las marcas no se verificaron. El plan lanza en inglés con el nombre: X (l. 126) y Show HN (l. 132).
- **Verificación independiente**:
  - **USPTO:** la marca UCOACH (reg. 3536981, Strada Collaborative LLC, clases 35, 41, 42 y 45) consta como viva (https://markinton.com/trademark/ucoach-77453726, MEDIA).
  - **Google Play:** hay una app «UCOACH», de marca blanca de Trainerize (https://play.google.com/store/search?q=ucoach).
  - **EUIPO y OEPM:** siguen sin comprobar.
- **Corrección**: añadir la marca de EE. UU. y recomendar que el repositorio público y el Show HN de enero salgan ya con el nombre definitivo, o con uno en clave neutro, después de revisar USPTO, EUIPO y OEPM.

**M12 · MISSING · media**
- **Dice**: el plan Coach, opción B (l. 97 y 108), es la recomendación central de ingresos recurrentes, pero el informe no analiza ninguna herramienta que los coaches ya usen para seguir a sus clientes.
- **Verificación independiente**: no se preguntó directamente. El verificador sí encontró a Trainerize, que ofrece apps de marca blanca para coaches (A06-23), y a Coachvox AI, unos 99 $/mes al coach (A06-19).
- **Corrección**: añadir una tabla de herramientas para coaches con datos del cliente que diga si integran wearables y cuánto cuestan. Candidatas: Paperbell, Practice, CoachAccountable, Simply.Coach, Trainerize, Healthie y Coachvox. Sin esa tabla, el precio de 29-59 € por coach no tiene referencia.

### Bajas

**B1 · INTERNAL · baja**
- **Dice** (l. 14): «Hay un precio de 8 a 15 €/mes [...] En esa franja están Oura (5,99 €/mes), Rise (~5,8 $/mes en plan anual)...».
- **Verificación independiente**: los dos precios se confirman (https://ouraring.com/membership y la App Store de Rise), pero quedan por debajo de la franja de 8 a 15 €.
- **Corrección**: «Cerca de esa franja, por debajo, están Oura y Rise».

**B2 · A06-08 · DISCREPANCY · baja**
- **Dice** (l. 31): «también plan mensual y pago único en promociones».
- **Verificación independiente**: en la App Store (https://apps.apple.com/us/app/rise-sleep-tracker/id1453884781) solo hay suscripción anual con 7 días de prueba, en variantes de 69,99, 59,99 y 35,99 $, más «AI Expert Access» a 29,99 $. No se ve ningún pago único.
- **Corrección**: «solo suscripción anual; 69,99 $, con ofertas a 59,99 y 35,99 $».

**B3 · A06-05 · DISCREPANCY · baja**
- **Dice** (l. 52): «Otros se quedan entre el 15 y el 18 %».
- **Verificación independiente**: Apify cobra un 20 % de comisión (https://docs.apify.com/platform/actors/publishing/monetize). No hay datos de MCP Marketplace ni de Agent Bazaar.
- **Corrección**: «Apify se queda el 20 %; del resto no hay datos públicos».

**B4 · A06-13 · STALE · baja**
- **Dice** (l. 70): «230 M de personas preguntan por salud cada semana».
- **Verificación independiente**: la cifra era de enero. En julio OpenAI dio 300 millones (https://techcrunch.com/2026/07/23/openai-makes-chatgpt-health-available-to-all-u-s.-users/).
- **Corrección**: «300 M (julio de 2026)».

**B5 · A06-18 · DISCREPANCY · baja**
- **Dice** (l. 40): «paquete ejecutivo mediano 1.250 $ (~200 $/h); paquete de negocio 1.000 $ (~250 $/h)».
- **Verificación independiente**: según Paperbell (https://paperbell.com/blog/what-coaches-charge/), el paquete típico cuesta 736 $ (unas 6 sesiones), el de 2-5 sesiones 485 $ y el de 6 o más 1.275 $. Los datos van del 2-10-2025 al 2-10-2026. Las cuotas mensuales (175 y 350 $) y la sesión de 140 $ se confirman.
- **Corrección**: sustituir las cifras de los paquetes.

**B6 · A06-30 · DISCREPANCY · baja**
- **Dice** (l. 29): «Reino Unido: 169 / 229 / 349 £».
- **Verificación independiente**: esos son los precios de Jersey (https://www.whoop.com/je/en/membership). La página en-gb no muestra precios.
- **Corrección**: quitar el Reino Unido o poner «Jersey».

**B7 · A06-35 · DISCREPANCY (e INTERNAL) · baja**
- **Dice**: «online, 40-150 €» (l. 42), «de 40 a 500 € la sesión» (l. 161) y «120-500 €/sesión» (l. 219).
- **Verificación independiente**: según https://www.cronoshare.com/cuanto-cuesta/coaching-empresarial, la sesión presencial de 60 minutos cuesta entre 120 y 300 € y la online entre 20 y 65 €. Otra tabla da de 100 a 500 €.
- **Corrección**: unificar en «presencial 120-300 €; online 20-65 €» en las tres líneas.

**B8 · A06-42 · DISCREPANCY · baja**
- **Dice** (l. 129): «entre el 2 y el 10 % de las visitas frías se apuntan (`reported`, proveedores de listas de espera)».
- **Verificación independiente**: LaunchList da entre el 10 y el 20 % en frío y entre el 3 y el 10 % con anuncios (https://app.getlaunchlist.com/blog/why-is-my-waitlist-not-converting). Una fuente independiente da una media del 2 al 5 %.
- **Corrección**: citar los dos rangos con su fuente.

**B9 · A06-45 · STALE · baja**
- **Dice** (l. 141): «más de 1.700 empresas aceleradas desde 2013, `verified`».
- **Verificación independiente**: en septiembre de 2026 eran más de 1.800 (https://elreferente.es/actualidad/lanzadera-selecciona-a-120-empresas-y-supera-ya-las-1-000-startups-impulsadas/).
- **Corrección**: «más de 1.800».

**B10 · A06-47 · STALE · baja**
- **Dice** (l. 110): «compite con Gympass, ifeel».
- **Verificación independiente**: Gympass ahora se llama Wellhub (https://wellhub.com/es-es/plans-pricing/).
- **Corrección**: «Wellhub (antes Gympass)».

**B11 · INTERNAL · baja**
- **Dice**: la cohorte 1 «empieza el 2 de febrero» (l. 139) y los criterios se evalúan el 18-02-2027 (l. 144). El piloto de coaches es de «un mes gratis [...] si renuevan» (l. 140).
- **Verificación independiente**: es una contradicción interna. El 18 de febrero la cohorte va por la mitad. Las renovaciones de los coaches solo se conocen si el piloto empezó antes del 18 de enero.
- **Corrección**: fijar el inicio del piloto de coaches en la semana 9 como muy tarde, y decir que de la cohorte solo se evalúa la venta.

**B12 · OVERCLAIM · baja**
- **Dice** (l. 17): «se paga 10 veces más cuando hay una persona que te pide cuentas».
- **Verificación independiente**: los precios de Future y Trainwell se confirman (https://www.sensai.fit/blog/future-app-review-2026), pero son entrenadores de fitness.
- **Corrección**: «en fitness, se paga unas 10 veces más...». Apoyar la extrapolación a fundadores en Paperbell.

## Sólido

Está verificado y no hay que «arreglarlo»:

- **Monetización de MCP:**
  - Menos del 5 % genera ingresos y menos del 0,5 % pasa de 1.000 $/mes, según estimaciones de autores con interés comercial (A06-01).
  - No hay MCP de consumo con ingresos públicos (A06-02).
  - El Apps SDK solo aprueba pago externo para bienes físicos, el checkout integrado está en beta para marketplaces y no hay suscripciones digitales (A06-03, ALTA).
  - Los marketplaces solo miden servidores remotos (A06-06).
  - MCPize da el 80 % al editor y tiene más de 450 desarrolladores (A06-05).
- **Precios de referencia:** Oura (A06-07), Google Health Premium, con los 37 países y la inclusión en AI Pro (A06-09), Rosebud (A06-10), Reclaim (A06-11), Sunsama, Motion y Claude Pro y Max (A06-31 a A06-33), y Future y Trainwell (A06-20).
- **Plataformas:**
  - Claude Health (A06-12, ALTA) y ChatGPT Health, con sus fechas y su alcance (A06-13).
  - Claude Pro incluye tareas programadas (A06-15).
  - Ninguna plataforma cruza la agenda con la salud (A06-17).
- **Coaches:** los datos de Paperbell de cuotas mensuales y sesión suelta (A06-18), y la tarifa media de la ICF por sesión (A06-34).
- **Nombre:** ucoach.com, ucoach.io, ucoach.ai, la app U-Coach, YouCoach y YourCoach (A06-22, A06-23 y A06-48), y que .es no tiene RDAP (A06-50).
- **Retención y RGPD:**
  - Las apps de salud y fitness retienen entre un 3 y un 8 % el día 30 (A06-24). El informe no da fuente.
  - El apoyo humano mejora la adherencia en apps de salud mental (A06-28). El informe no da fuente.
  - Las obligaciones del RGPD que cita la l. 88 son correctas (A06-25): art. 9, responsable del tratamiento, EIPD, contrato de encargo y cifrado.
- **Otros:**
  - Freemium de MCP con 0 $ (A06-36), GitHub Sponsors (A06-37), Pragmatic Engineer (A06-38) y Apify como caso B2B (A06-39).
  - Jasper (A06-40) y Reclaim comprada por Dropbox en 2024 (A06-41).
  - mcp-use en HN el 8-08-2025 (A06-43), los directorios MCP activos (A06-44) y las funciones del coach de Google (A06-51).

## No verificable

| id | Qué | Qué hacer |
|---|---|---|
| A06-19 | Los creadores de Coachvox cobran de 10 a 100 £/mes por su clon (l. 16 y 37) | No hay dato público. Quitarlo del resumen 4 o buscarlo en la ayuda oficial de Coachvox. |
| A06-21 | «pide unas 40 respuestas como mínimo» y «llegó al 58 %» (l. 18 y 142), con la etiqueta `verified` | Citar el pasaje exacto de First Round o bajar la etiqueta a `reported`. El umbral del 40 % y el 22 % inicial sí se confirman (MEDIA). |
| A06-26 | El cifrado de extremo a extremo hace que «el peso del RGPD sea menor» (l. 99) | La doctrina es ambigua: TJUE C-413/23 P frente a la postura abierta del CEPD, y el proveedor sería, como mínimo, encargado. Marcarlo como `inferred` y remitirlo a la línea 5. |
| A06-29 | Marcas «Ucoach» en la EUIPO y la OEPM | Búsqueda manual en TMview y en el localizador de la OEPM, como ya propone el informe. Ver M11 para EE. UU. |
| A06-46 | Wayra y Demium como pilotos | Ninguna de las dos tiene programa de bienestar para fundadores. Dejarlas como candidatas sin más. |
| A06-49 | Clases de Niza 9, 41, 42 y 44 | Sin fuente. El verificador sugiere añadir también la 35. Comprobarlo en TMclass. |
| A06-34 (parte) | Coach de nivel C-suite «>500 $/h» | Sin atribución. Quitarlo o marcarlo como estimación. |

## Falta

- **Claude Duet y ChatGPT dots** en el riesgo de plataforma (M3), y las **tareas programadas de ChatGPT** en lugar de Pulse (M2).
- **Lifestack y Rise** como referencia del posicionamiento «planificador de energía» (M10).
- **Herramientas para coaches** como competencia del plan Coach (M12).
- **Cómo se dispara el brief** si las tareas de la plataforma no llegan al MCP local (M4).
- **Economía unitaria del plan Coach:** cuántos coaches a 29-59 € hacen falta, cuánto cuesta captarlos y cuánto tiempo de Philippe exige cada cohorte.
- **Fuentes de retención y de apoyo humano**, que sostienen el hallazgo no obvio y no tienen cita (l. 90 y 192). Usar las de A06-24 y A06-28.
- **RGPD:** la base legal (consentimiento explícito, art. 9.2.a) y la notificación de brechas en 72 h (art. 33), que la l. 88 no menciona.
- **Plan Ultra de Claude (200 $/mes)** en la tabla de precios (l. 36).
- **Las 9 afirmaciones** del recuento del preflight (60) que no entraron en la extracción (51), sobre todo cifras de la sección 7. Quedan sin verificar.

## Correcciones a aplicar en el informe

1. **l. 13**: «no permiten vender suscripciones digitales dentro del chat» se mantiene, pero hay que añadir que el directorio de Claude lista conectores con planes de pago fuera del chat.
2. **l. 14**: Oura y Rise quedan por debajo de la franja, no dentro.
3. **l. 15**: quitar Pulse y poner las tareas programadas de ChatGPT (17-06-2026). La frase «ni una versión para la UE» debe excluir a Google (C1).
4. **l. 16**: «El canal que más rinde» → hipótesis H3. Quitar o marcar Coachvox.
5. **l. 17**: «en fitness, se paga unas 10 veces más».
6. **l. 18 y 142**: citar el pasaje de First Round o bajar a `reported` el mínimo de 40 respuestas y el 58 %.
7. **l. 19, 174 y 182**: ucoach.app caducado y en redención, u-coach.com en venta. Cambiar «ningún dominio principal libre».
8. **l. 29**: los precios en libras son de Jersey, no del Reino Unido.
9. **l. 31**: Rise solo tiene suscripción anual, sin pago único.
10. **l. 36**: añadir Ultra (200 $/mes).
11. **l. 40**: paquetes de Paperbell de 736, 485 y 1.275 $. Periodo del 2-10-2025 al 2-10-2026.
12. **l. 42, 161 y 219**: unificar los precios de España: presencial 120-300 € y online 20-65 €.
13. **l. 52**: «Apify 20 %; resto sin datos».
14. **l. 55**: «Visibilidad y canal de venta de un servicio que se cobra fuera».
15. **l. 66-73**: añadir Claude Duet y ChatGPT dots. Sustituir Pulse.
16. **l. 69**: precisar que la tarea se ejecuta en remoto y no llega a un MCP local por stdio.
17. **l. 70**: «300 M a la semana (julio de 2026)».
18. **l. 72 y 75**: Google Health Coach está en España y en la UE, así que el punto 3 aplica solo a Claude y ChatGPT.
19. **l. 88**: añadir la base legal (art. 9.2.a) y el art. 33.
20. **l. 90 y 192**: citar la fuente de retención (A06-24) y la de apoyo humano (A06-28).
21. **l. 99**: marcar como `inferred` y remitir a la línea 5.
22. **l. 108**: añadir la competencia de herramientas para coaches.
23. **l. 110**: «Wellhub (antes Gympass)».
24. **l. 122 y 148**: alinear H2 con los criterios de decisión.
25. **l. 125, 129 y 139**: alinear la apertura de la landing con la cohorte. Cambiar «cohorte de enero».
26. **l. 129**: aclarar la métrica de Lenny y bajarla a `reported`. Cuota fría de LaunchList del 10-20 % frente al 2-5 % independiente.
27. **l. 140 y 144**: arrancar el piloto de coaches antes del 18-01. Del 18-02 solo se evalúa la venta de la cohorte.
28. **l. 141**: Lanzadera «más de 1.800».
29. **l. 163 y 166**: citar Lifestack y Rise, y apoyar el mensaje en el trabajo y el método.
30. **l. 180-182**: añadir la marca UCOACH viva en la USPTO y la app UCOACH de Trainerize. No lanzar en público con el nombre antes de revisar las marcas.
31. **l. 193**: acotar la ventana europea a Claude y ChatGPT, y a usuarios sin Fitbit ni Pixel Watch.
32. **l. 219**: añadir un enlace alternativo de Cronoshare.
33. **l. 223**: sustituir el enlace de Rise (404) por la App Store.

## Re-verificación (2026-11-19)

Correcciones aplicadas con Edit sobre `06-negocio-gtm.md`. Cada cambio lleva la marca «(corregido tras QA 2026-11-19)» y cita la URL que consultó el verificador (`qa/A-respuestas.md`). Las etiquetas se ajustaron a lo que se consultó de verdad. Bajaron a `reported` Lenny, First Round (las ~40 respuestas y el 58 %) y Lanzadera; subieron a `verified` Google Health Premium, Rise (App Store), U-Coach, YouCoach y YourCoach. El índice de fuentes suma las filas 34 a 43.

| hallazgo | estado | línea nueva |
|---|---|---|
| C1 · «ninguna versión para la UE» y ventana europea | corregido: Google Health Coach (con Fitbit o Pixel Watch) y Oura Advisor funcionan en España; lo que no ha llegado a la UE son las integraciones de salud de ChatGPT y Claude. El hueco es el método que cruza agenda, trabajo y cuerpo, independiente del wearable | 15, 30, 74, 77, 81, 90, 168, 194, 197 |
| M1 · directorio de Claude sin listados de pago | corregido | 13, 55 |
| M2 · ChatGPT Pulse vigente | corregido: tareas programadas desde el 17-6-2026 y retirada de Pulse | 15, 72; índice, filas 10 y 36 |
| M3 · faltaban Duet y dots | corregido: dos filas nuevas en el riesgo de plataforma | 15, 70, 73 |
| M4 · tareas programadas frente a Ucoach local | corregido: la tarea se ejecuta en remoto; el brief de Ucoach lo disparan el cron y Telegram | 69, 136 |
| M5 · dominios (ucoach.app, u-coach.com) | corregido | 19, 176, 177, 186 |
| M6 · cifras de Lenny con `verified` | corregido: métrica real y `reported` | 131; índice, fila 26 |
| M7 · H2 frente a los criterios de decisión | corregido: H2 = ≥ 10 plazas y ≥ 25 % de los activos; criterios alineados | 124, 150 |
| M8 · espera de la lista y «cohorte de enero» | corregido: la llamada a la cohorte se abre el 22-12 y la cohorte empieza el 19-1 (4 semanas de espera) | 131, 141 |
| M9 · «el canal que más rinde» | corregido: pasa a ser la hipótesis H3; Coachvox, sin verificar | 16, 37 |
| M10 · «Planificador de energía» frente a Lifestack y Rise | corregido | 165, 168 |
| M11 · marca UCOACH en la USPTO | corregido: añadida; el repositorio, la landing y el Show HN salen con el nombre nuevo (ver `09-nombre.md`) | 19, 130, 134, 181-186 |
| **M12 · falta analizar las herramientas para coaches** | **no corregido**: se menciona como contra y como pendiente, pero falta la tabla. El verificador no tiene datos de Paperbell, Practice, CoachAccountable, Simply.Coach, Trainerize ni Healthie como herramientas, y añadirla sin fuente sería inventar | 110, 249 (mención) |
| B1 · Oura y Rise «en esa franja» | corregido | 14 |
| B2 · planes de Rise | corregido | 31 |
| B3 · comisiones de otros marketplaces | corregido | 52 |
| B4 · 230 M a la semana | corregido: 300 M en julio | 71 |
| B5 · paquetes de Paperbell | corregido | 40 |
| B6 · precios de WHOOP en el Reino Unido | corregido: son los de Jersey | 29 |
| B7 · precios de coaching en España | corregido en las l. 42 y 163 y en la fila 19 del índice | 42, 163 |
| B8 · benchmark de lista en frío | corregido | 131 |
| B9 · Lanzadera | corregido | 143 |
| B10 · Gympass | corregido | 112 |
| B11 · calendario de la cohorte y del piloto de coaches | corregido: la cohorte termina el 17-2 y el piloto empieza como tarde el 15-1 | 141, 142 |
| B12 · «10 veces más» | corregido: «en fitness» | 17 |
| Bloqueo · help.risescience.com (403 por bloqueo de robots) | corregido: sustituido por la ficha de la App Store | 31, 227 |
| Bloqueo · cronoshare.com | no aplica: el coordinador comprobó que devuelve 200 (falso positivo); no se ha tocado | 219 |
| No verificables (Coachvox, Sean Ellis, cifrado E2E, C-suite) | corregido: marcados sin confirmar, como `reported` o como `inferred` | 16, 18, 37, 41, 101, 144 |

**Nota recalculada** contando solo lo que queda abierto: `nota.py --claims 60 --verificadas 45 --portantes 29 --portantes-ok 25 --medias 1`. Da **8.3**, limitada por la cobertura.

**Veredicto: CORREGIR ANTES DE ENTREGAR**, porque queda una media abierta (M12). Para cerrarla hay que investigar las herramientas para coaches con fuentes, o recortar el plan Coach a hipótesis hasta tener esa tabla. Para subir la cobertura habría que verificar las 9 afirmaciones que no entraron en la extracción y las 4 portantes no verificables: Coachvox, las ~40 respuestas de Sean Ellis, el cifrado E2E frente al RGPD y las marcas en la EUIPO y la OEPM.

**Avisos:**
- **Enlaces:** el preflight volvió a correr con `--links` desde este subagente, pero el sandbox no tiene red y todos los enlaces devolvieron «sin respuesta». Para el estado de los enlaces vale la comprobación con curl del coordinador.
- **Recuento del preflight:** ahora da 122 «cifras», inflado por las marcas de corrección y por las cifras nuevas con fuente.
- **Guiones largos, placeholders y fechas relativas:** 0.

