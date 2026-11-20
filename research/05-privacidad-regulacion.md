# 05 · Privacidad y regulación

**Fecha:** 2026-11-19
**Línea:** 5 de 7 (privacidad y regulación) del deep research de Ucoach
**Base:** documento de producto v0.1 (Google Doc `1S6MFA-6j9KQh4pYVxCYngqUF8hHvjSIaFO7EjO2owyw`), sección "Privacidad, seguridad y regulación", y modelo de negocio (local MIT, Pro gestionado de 8 a 15 €/mes y plan Equipos)
**Aviso:** esto es investigación, no asesoría jurídica. Lo marcado con ⚖️ debe confirmarlo un abogado antes de lanzar la versión gestionada o el plan Equipos.

**Niveles de confianza**
- `verified`: comprobado en esta sesión contra el texto oficial o la página del organismo, o contra varias fuentes primarias coherentes entre sí.
- `reported`: lo publican despachos o prensa especializada, pero no lo he comprobado en la fuente oficial.
- `inferred`: es mi razonamiento a partir de las normas; no hay fuente que lo diga para un caso como Ucoach.

**Método y límites.** Hice unas 35 búsquedas y consulté más de 40 fuentes (con WebFetch de páginas oficiales o primarias cuando se pudo). El límite de búsquedas compartido se agotó antes de terminar, así que quedaron sin verificar estos puntos: el recurso de casación contra el Marco de Privacidad UE-EE. UU. (asunto Latombe), la sentencia EDPS/SRB (C-413/23 P), la transposición española de la Directiva 2023/2673 después de junio de 2026, el estado en 2026 de la ley de salud de Nueva York y del pleito contra Amazon por la ley de Washington, y los textos exactos de la guía MDCG 2019-11 rev.1. Van marcados como `reported` y aparecen en la lista de cosas que hay que confirmar. **Actualización del QA de 2026-11-19:** un verificador independiente comprobó contra el texto oficial (DOUE, BOE) Latombe, SRB, la transposición de la Directiva 2023/2673, Nueva York y la MDCG 2019-11 rev.1. Solo sigue sin verificar el estado procesal de Maxwell v. Amazon. Las etiquetas se han actualizado donde aparecen: `verified` solo cuando la fuente es el texto oficial o primario.

---

## 1. Resumen

1. **En la versión local, el promotor no es responsable del tratamiento, pero la promesa de privacidad del documento es falsa tal como está escrita.** Un desarrollador que distribuye software y nunca recibe datos no decide sobre ningún tratamiento real. El RGPD solo le "anima" a diseñar con privacidad (considerando 78; CEPD, directrices 4/2019). El usuario que registra sus propios datos para sí mismo está dentro de la excepción doméstica (art. 2.2.c). Pero la frase "sin que tus datos de salud salgan de tu máquina" no se sostiene: lo que devuelve Ucoach entra en la conversación con Claude o ChatGPT y lo procesa su proveedor, que en los planes de consumo puede usarlo para entrenar si el usuario no lo ha desactivado. Telegram es otra salida. `verified` en cuanto a las normas, `inferred` en cuanto a la aplicación a Ucoach.
2. **Casi todo lo que guarda Ucoach son datos de salud del art. 9.** Sueño, VFC, frecuencia cardiaca en reposo y peso lo son claramente. La energía y el ánimo autoevaluados, seguidos en el tiempo y cruzados con el sueño, también lo son con alta probabilidad: el Grupo del Artículo 29 dice que los datos de estilo de vida registrados en el tiempo o combinados pasan a ser datos de salud, y el TJUE interpreta de forma amplia los datos que revelan salud de forma indirecta (C-184/20, de 2022; C-21/23, de 2024). Conviene tratar la base entera como categoría especial. `verified` + `inferred`.
3. **En la versión gestionada, el promotor pasa a ser responsable del tratamiento de datos de salud.** Necesita consentimiento explícito (art. 9.2.a), que en salud sí basta en España porque el art. 9.1 de la LOPDGDD no la incluye entre las excepciones; una evaluación de impacto (cumple al menos cinco criterios de la lista de la AEPD de 2019, y con dos o más la AEPD la considera necesaria en la mayoría de los casos: hay que hacerla; corregido tras QA 2026-11-19); contratos de encargo con cada proveedor; alojamiento en la UE; avisos móviles sin datos de salud en el contenido; notificación de brechas en 72 horas, y probablemente un delegado de protección de datos cuando crezca. ⚖️
4. **Ley de IA: Ucoach queda en riesgo mínimo o fuera de la ley, salvo el plan Equipos.** El Reglamento 2026/1744 ("Digital Omnibus" sobre IA, DOUE del 24-07-2026, en vigor desde el 27-07-2026) retrasa el alto riesgo al 2-12-2027 (Anexo III) y al 2-08-2028 (Anexo I). No retrasa las prohibiciones ni el art. 50 (transparencia), que se aplica desde el 2-08-2026; del art. 50 solo sustituye el apartado 7, y da a los sistemas generativos ya comercializados antes del 2-08-2026 hasta el 2-12-2026 para cumplir el 50.2, en un nuevo art. 111.4 (corregido tras QA 2026-11-19, texto oficial: https://publications.europa.eu/resource/celex/32026R1744). Un motor de reglas escritas a mano, con aleatorización simple y sin aprendizaje, no es un "sistema de IA"; un motor que aprende solo cuándo y qué enviar (bandit o aprendizaje por refuerzo) probablemente sí lo es, y entonces Ucoach debe cumplir el art. 50 (ver la sección 3.3). Si el Pro añade su propio chat o agente con un modelo de terceros, Ucoach es proveedor de ese sistema y debe avisar al usuario de que habla con una IA. El riesgo serio está en el plan Equipos: inferir estrés o emociones de trabajadores está prohibido (art. 5.1.f) y monitorizar su comportamiento es alto riesgo (Anexo III, punto 4). `verified` + `inferred`.
5. **Producto sanitario: Ucoach queda fuera mientras su finalidad sea el bienestar.** Lo que decide la frontera son las palabras. El MDR excluye el software de estilo de vida y bienestar (considerando 19), pero hablar de "insomnio", "burnout", "detectar estrés" o "tratar" con umbrales de corte acerca a Ucoach a la regla 11 (clase IIa). La FDA revisó su guía de bienestar el 6-01-2026 con la misma lógica: no nombrar enfermedades ni umbrales diagnósticos. Hay una lista de palabras a evitar en la sección 4. `verified`.
6. **El Espacio Europeo de Datos Sanitarios (Reglamento 2025/327) no obliga a Ucoach** salvo que afirme ser interoperable con historias clínicas electrónicas. En ese caso necesitaría una etiqueta, y solo a partir del 26-03-2029 o el 26-03-2031 según la categoría de datos. `verified`.
7. **En EE. UU., mejor no vender al principio.** Si se vende allí, la versión gestionada entra en la Health Breach Notification Rule de la FTC (ampliada en vigor desde el 29-07-2024) y en la My Health My Data Act de Washington, que exige consentimiento separado, una política de privacidad específica y abre la vía a demandas privadas; también en las leyes de Nevada y Connecticut. Los casos GoodRx, BetterHelp, Premom y Flo castigaron compartir datos de salud con terceros a través de SDK publicitarios. `verified` (FTC, Washington y casos, con fuente primaria) / `reported` (Nevada y Connecticut) (corregido tras QA 2026-11-19).
8. **"Agregado y anónimo" no funciona con equipos de 2 a 5 personas.** Con tan pocos miembros, cualquier media permite deducir los datos de cada uno, y además está la presión jerárquica. Hay que rediseñar el plan Equipos para que no comparta datos de salud. En consumo, la Ley 10/2025 ya obliga a avisar 15 días antes de cada renovación, y la Directiva 2023/2673 obliga a los Estados a exigir un "botón de desistimiento" desde el 19-06-2026, aunque a 04-11-2026 España aún no la ha transpuesto (corregido tras QA 2026-11-19). Conviene implementarlo igualmente. La biblioteca de libros tiene un riesgo bajo si no copia frases propias de los autores. `verified` + `inferred`.

---

## 2. Tabla de normas

| Norma | ¿Aplica a la versión local (MIT, sin servidor)? | ¿Aplica a la versión gestionada (Pro / Equipos)? | Obligaciones clave | Plazo / fecha | Fuente |
|---|---|---|---|---|---|
| RGPD (UE 2016/679) + LOPDGDD (LO 3/2018) | Al usuario no (excepción doméstica). Al promotor no, mientras no reciba datos. **Sí** a cualquier dato que reciba (telemetría, soporte, lista de espera, la validación con 20 usuarios) | **Sí**: el promotor es responsable | Art. 9.2.a consentimiento explícito; art. 13 información; art. 25 privacidad desde el diseño; art. 28 encargados; art. 30 registro; art. 32 seguridad; art. 33-34 brechas; art. 35 EIPD; art. 37 DPO a escala; cap. V transferencias | Aplicable desde 25-05-2018 (art. 99.2) (corregido tras QA 2026-11-19). El Omnibus de datos que lo modificaría está en negociación y no es ley a 19-11-2026 | EUR-Lex; BOE; AEPD |
| Ley de IA (UE 2024/1689), modificada por el Reglamento 2026/1744 | Probablemente no: el motor de reglas no es un sistema de IA y el uso personal no profesional está excluido para quien despliega | Art. 50 si hay chat o agente propio; art. 4 (alfabetización, suavizado); art. 5 y Anexo III en Equipos | Avisar de que se interactúa con una IA; no manipular ni explotar vulnerabilidades; en Equipos, nada de reconocimiento de emociones en el trabajo | Prohibiciones: 2-02-2025. Modelos de uso general (GPAI): 2-08-2025. Art. 50: 2-08-2026. Alto riesgo Anexo III: **2-12-2027**. Anexo I: **2-08-2028** | EUR-Lex; Comisión; nicfab |
| MDR (UE 2017/745), regla 11, guía MDCG 2019-11 rev.1 | No, si la finalidad declarada es bienestar | No, con la misma condición | Controlar las afirmaciones en web, app, tiendas y prompts. Si se cruza la frontera: marcado CE, clase IIa y organismo notificado | MDCG 2019-11 rev.1: 17-06-2025 | Comisión (DG SANTE); Emergo |
| EHDS (UE 2025/327) | No | Solo si se afirma interoperabilidad con historia clínica electrónica | Etiqueta de app de bienestar (art. 47) con validez máxima de 3 años | En vigor 25-03-2025 (corregido tras QA 2026-11-19); aplicación general 26-03-2027; art. 47: 26-03-2029 o 26-03-2031 según la categoría | EUR-Lex (art. 105) |
| Directiva 2011/83 + Directiva 2023/2673 (botón de desistimiento) + TRLGDCU | No (es gratis) | **Sí** (suscripción) | 14 días de desistimiento; función de desistimiento en línea; consentimiento expreso si el servicio empieza antes de que acabe ese plazo | Botón: los Estados debían aplicarlo desde 19-06-2026. España no lo ha transpuesto a 04-11-2026 (TRLGDCU consolidado) y tiene abierto un procedimiento de infracción (corregido tras QA 2026-11-19) | EUR-Lex; BOE; OCU; El Derecho; iubenda |
| Ley 10/2025 de atención a la clientela (modifica el art. 97.1.p del TRLGDCU) | No | **Sí** | Avisar al menos 15 días antes de cada renovación automática, con sus consecuencias, y facilitar la baja | BOE 27-12-2025; en vigor desde 28-12-2025 | BOE; Ministerio de Consumo |
| FTC Health Breach Notification Rule (16 CFR 318) | Dudoso: sin servidor no hay "registro personal de salud" del proveedor | **Sí**, si hay usuarios en EE. UU. | Notificar brechas, que incluyen la cesión no autorizada; multas civiles | Regla ampliada en vigor desde 29-07-2024 | FTC; Federal Register |
| Washington My Health My Data Act | Riesgo bajo | **Sí**, si hay usuarios en Washington | Consentimiento separado para recoger y para compartir; autorización firmada para vender; política específica enlazada en la portada; demandas privadas | 31-03-2024 (pequeñas empresas: 30-06-2024) | Fiscal General de Washington |
| Nevada SB 370 / Connecticut SB 3 | No | Sí, si hay usuarios allí | Consentimiento; prohibición de vender sin autorización; geovallado | NV: 31-03-2024. CT: 1-07-2023 | Despachos |
| FDA, guía *General Wellness* | No (software de estilo de vida, excluido por la sección 520(o)(1)(B)) | No, con afirmaciones de bienestar | No mencionar enfermedades ni umbrales diagnósticos | Revisión del 6-01-2026 | Covington; King & Spalding |
| Ley de Propiedad Intelectual (RDL 1/1996), arts. 10, 21 y 32 | Sí (la biblioteca va en el código MIT) | Sí | Resumir ideas con palabras propias; citas breves solo con fines permitidos y con autor y fuente | Vigente | BOE |
| Otras a vigilar (sección 3.10): Cyber Resilience Act, Directiva de responsabilidad por productos 2024/2853, Data Act, RD 1907/1996, DSA, Ley Europea de Accesibilidad | CRA: no si el software es libre y no se monetiza | Probablemente sí (CRA, responsabilidad por productos, RD 1907/1996) | Ver sección 3.10 | CRA: notificaciones desde 11-09-2026 y todo desde 11-12-2027. Directiva 2024/2853: transposición hasta 9-12-2026 | `reported` |

---

## 3. Detalle por norma

### 3.1 RGPD y LOPDGDD

**a) ¿Son datos de salud?**
- El art. 4.15 del RGPD define los datos de salud como los relativos a la salud física o mental. El art. 9.1 prohíbe tratar datos "que revelen" categorías especiales, salvo las excepciones del art. 9.2. `verified`
- **C-184/20, OT** (TJUE, 1-08-2022): los datos que revelan una categoría especial *de forma indirecta*, por deducción o cruce, también entran en el art. 9. `verified` (con comentarios de varios despachos; párrafos 117-128).
- **C-21/23, Lindenapotheke** (TJUE, 4-10-2024): los datos de un pedido de medicamentos sin receta son datos de salud porque permiten deducir información sobre la salud. Esto confirma un umbral bajo. `verified` (nota de prensa del TJUE y comentarios).
- **Grupo del Artículo 29, anexo sobre datos de salud en apps y dispositivos** (5-02-2015): distingue tres tipos de datos de salud: (1) datos médicos; (2) datos brutos de sensores que, solos o combinados, permiten sacar conclusiones sobre la salud o el riesgo; (3) conclusiones sobre la salud, sean correctas o no. Los datos de estilo de vida "aparentemente inocuos" pasan a ser de salud si se registran en el tiempo o se combinan con otros. También dice que la base más probable para apps de salud es el consentimiento explícito. `verified` (texto oficial del anexo, https://ec.europa.eu/justice/article-29/documentation/other-document/files/2015/20150205_letter_art29wp_ec_health_data_after_plenary_annex_en.pdf; corregido tras QA 2026-11-19).
- **Cómo se aplica a Ucoach** `inferred`:
  - VFC, FC en reposo, peso y horas y calidad del sueño son datos de salud por sí mismos (tipo 2).
  - Los check-ins de energía, ánimo y foco cruzados con el sueño, y la revisión semanal ("tu energía es mayor cuando duermes 7 horas"), son conclusiones sobre el estado físico y mental (tipo 3).
  - La ergonomía (dolor, postura) es dudosa. Hábitos como la lectura no son de salud, pero conviven en la misma base.
  - Conclusión: hay que diseñar todo el producto como si tratara categorías especiales.
- **El CEPD no tiene directrices específicas sobre wearables.** Lo que hay son el anexo del Grupo del Artículo 29 de 2015, las directrices 03/2020 (salud e investigación, COVID) y su intervención en la compra de Fitbit por Google. `verified`

**b) Versión local: ¿quién es responsable?**
- **El usuario.** Su uso es "exclusivamente personal o doméstico" (art. 2.2.c y considerando 18). El RGPD no se le aplica cuando registra sus propios datos. Si mete datos de otras personas (por ejemplo, notas sobre un socio), sigue siendo uso doméstico mientras no los publique. `verified` (norma) / `inferred` (caso).
- **El promotor.** Responsable es quien determina los fines y medios de un tratamiento (art. 4.7). Quien publica software que se ejecuta en máquinas ajenas y no recibe nada no participa en ningún tratamiento concreto. El considerando 78 y las directrices 4/2019 del CEPD tratan a los "productores" de aplicaciones como actores a los que se *anima* a aplicar la privacidad desde el diseño, pero a los que el art. 25 no se dirige directamente. `verified`
- **Matiz de C-683/21** (TJUE, 5-12-2023): quien *encarga* una app y participa en sus fines y medios puede ser responsable aunque no trate datos con ella. Aquí no aplica, porque cada usuario decide sus fines, pero el diseño de Ucoach sí condiciona los medios. Es otra razón para aplicar la privacidad desde el diseño aunque la ley no lo exija. `verified` (sentencia) / `inferred` (aplicación).
- **Cuándo pasa el promotor a ser responsable, incluso con la versión local** `inferred`:
  1. Telemetría, informes de errores o comprobación de actualizaciones que envíen identificadores.
  2. Soporte en el que el usuario mande su `~/.ucoach` o registros.
  3. Lista de espera y analítica web.
  4. **La fase de validación con 20 emprendedores.** Si el promotor recoge "noches registradas", "energía media" o entrevistas sobre su sueño, trata datos de salud de terceros. Necesita consentimiento explícito, una hoja informativa, minimización y valorar una EIPD. El documento v0.1 no lo contempla.
- **Telegram.** El usuario configura su propio bot y token, así que el responsable del envío es el usuario y Telegram trata los datos. Ucoach debe advertir de que el texto de un aviso ("dormiste 5,2 h") pasa por los servidores de Telegram. `inferred`

**c) Versión gestionada (Pro)**
- **Responsable:** la sociedad promotora. **Encargados:** alojamiento, base de datos, correo, pasarela de pago y notificaciones push (APNs de Apple y FCM de Google), cada uno con un contrato del art. 28. `inferred`
- **Bases jurídicas.** Art. 6.1.b (ejecución del contrato) para la cuenta y la facturación, más **art. 9.2.a (consentimiento explícito)** para los datos de salud. El consentimiento debe ser separado, granular por fuente (Oura, Garmin, Apple Health, check-ins) y tan fácil de retirar como de dar. En España, el art. 9.1 de la LOPDGDD excluye el "solo consentimiento" para ideología, afiliación sindical, religión, orientación sexual, creencias u origen racial o étnico, pero **no para la salud**. `verified` (BOE, texto consolidado de la LOPDGDD, https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673; corregido tras QA 2026-11-19) ⚖️
- **Evaluación de impacto (art. 35).** La lista de la AEPD (mayo de 2019) dice que la EIPD es necesaria "en la mayoría de los casos" cuando se cumplen dos o más de sus 11 criterios, y que la certeza aumenta con más criterios. Ucoach Pro cumple al menos cinco: categorías especiales, perfilado o evaluación (el plan del día depende de su estado), observación sistemática con apps, combinación de fuentes (wearables más calendario) y uso de tecnologías nuevas (IA). Con ese encaje **hay que hacer la EIPD**, y la del plan Equipos con más razón. `verified` (lista de la AEPD, https://www.aepd.es/documento/listas-dpia-es-35-4.pdf) / `inferred` (encaje) (corregido tras QA 2026-11-19).
- **DPO (art. 37.1.c):** obligatorio si la actividad principal es tratar categorías especiales "a gran escala". Con pocos cientos de usuarios es discutible; con miles, probablemente sí. El art. 34 de la LOPDGDD no menciona expresamente las apps de bienestar. `inferred` ⚖️
- **Transferencias internacionales.** Lo más sencillo es alojar en la UE y limitar los subencargados en EE. UU. a empresas adheridas al Marco de Privacidad de Datos UE-EE. UU. (Decisión de Ejecución (UE) 2023/1795, de 10-07-2023). El Tribunal General desestimó el recurso Latombe (T-553/23) el 3-09-2025, y la casación C-703/25 P, interpuesta el 31-10-2025, sigue pendiente a 19-11-2026. `verified` (textos oficiales: https://publications.europa.eu/resource/celex/32023D1795, https://publications.europa.eu/resource/celex/62023TJ0553 y https://publications.europa.eu/resource/celex/62025CN0703; corregido tras QA 2026-11-19) ⚖️
- **Seguridad.** Cifrado en tránsito y en reposo. La "sincronización cifrada" debería ser de extremo a extremo si se quiere mantener la promesa de que el promotor no lee los datos; si el servidor puede descifrarlos, no hay que decir que no puede. Las notificaciones push deben ir **sin datos de salud** en el contenido. `inferred`
- **Brechas:** notificar a la AEPD en 72 horas (art. 33) y a los usuarios si el riesgo es alto (art. 34), cosa que con datos de salud es lo normal. `verified` (norma)
- **Anonimización y seudonimización.** El CEPD aprobó el 7-07-2026 el *borrador* de directrices 02/2026 sobre anonimización, con consulta pública hasta el 30-10-2026. Aplica tres criterios: que ningún registro se pueda aislar, que no se pueda enlazar con otros datos y que no se pueda inferir nada concreto de una persona. También insiste en que el anonimato depende de quién mira los datos, a raíz de la sentencia SRB (C-413/23 P, 4-09-2025: unos datos seudonimizados siguen siendo personales para quien tiene la información adicional, y pueden no serlo para un destinatario que no puede reidentificar). Ver la sección 3.8 sobre Equipos. `verified` (directrices, https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf; sentencia, https://publications.europa.eu/resource/celex/62023CJ0413; corregido tras QA 2026-11-19).

**d) Cambios de 2025-2026 en el RGPD.** La Comisión presentó el 19-11-2025 el "Digital Omnibus" de datos. Propone una definición relativa de dato personal, un nuevo art. 9.2.k para datos sensibles residuales en el desarrollo de IA y el interés legítimo para IA (art. 88c). El CEPD y el SEPD emitieron el dictamen conjunto 2/2026, y el Parlamento presentó unas 1.840 enmiendas en agosto de 2026. **A 19-11-2026 no es ley.** Ucoach debe diseñarse con el RGPD vigente. `reported`

### 3.2 Espacio Europeo de Datos Sanitarios (Reglamento 2025/327)
- Reglamento (UE) 2025/327, de 11-02-2025. Publicado en el DOUE el 5-03-2025 y en vigor desde el 25-03-2025, a los veinte días de su publicación. Aplicación general desde el 26-03-2027. `verified` (texto oficial, https://publications.europa.eu/resource/celex/32025R0327; corregido tras QA 2026-11-19)
- **Apps de bienestar (art. 47).** Solo tienen que llevar etiqueta si el fabricante **afirma que son interoperables con sistemas de historia clínica electrónica**. La etiqueta indica las categorías de datos, las especificaciones comunes que cumple y su validez (máximo 3 años). En software va dentro de la app. Los distribuidores deben mostrarla en el punto de venta. Su formato se fijará por acto de ejecución. `verified`
- **Fechas (art. 105):** los arts. 47 a 49 se aplican desde el **26-03-2029** para resúmenes de pacientes, recetas y dispensaciones electrónicas, y desde el **26-03-2031** para imágenes médicas, resultados de laboratorio e informes de alta. `verified`
- **Para Ucoach:** no aplica mientras no diga que es interoperable con historias clínicas. No conviene decirlo. A largo plazo, el EHDS permitirá que el usuario añada datos de apps de bienestar a su historia clínica, lo que podría ser una función futura, pero entonces habría que cumplir el art. 47. `inferred`

### 3.3 Ley de IA (Reglamento 2024/1689) y "Digital Omnibus" sobre IA

**Calendario actualizado** `verified`:

| Hito | Fecha |
|---|---|
| Publicación / entrada en vigor | 12-07-2024 / 1-08-2024 |
| Prohibiciones (art. 5) y alfabetización (art. 4) | 2-02-2025 |
| Modelos de uso general (GPAI), gobernanza y sanciones | 2-08-2025 |
| Aplicación general, incluido el **art. 50** (transparencia) | **2-08-2026** (no se retrasó) |
| Marcado de contenido generado (art. 50.2) para sistemas generativos comercializados antes del 2-08-2026 (régimen transitorio del nuevo art. 111.4; los sistemas nuevos, desde el 2-08-2026) (corregido tras QA 2026-11-19) | 2-12-2026 |
| Nuevas prohibiciones del Omnibus (imágenes íntimas sin consentimiento y material de abuso sexual infantil) | 2-12-2026 |
| Alto riesgo del **Anexo III** (antes 2-08-2026) | **2-12-2027** |
| Alto riesgo del **Anexo I** (productos regulados, antes 2-08-2027) | **2-08-2028** |

- **"Digital Omnibus" sobre IA = Reglamento (UE) 2026/1744**, de 8-07-2026. Acuerdo provisional del 7-05-2026, voto del Parlamento el 16-06-2026, aprobación del Consejo el 29-06-2026, **DOUE del 24-07-2026 y entrada en vigor el 27-07-2026**. Además del retraso:
  - Suaviza el art. 4: ya no hay que "garantizar" un nivel de alfabetización, sino tomar medidas para fomentarlo.
  - Añade el art. 4a (base para tratar categorías especiales con el fin de detectar sesgos).
  - Simplifica obligaciones para pymes y pequeñas empresas de mediana capitalización.
  - Del art. 50 solo sustituye el apartado 7 (códigos de buenas prácticas para detectar y etiquetar contenido). Los apartados 1 a 6 no cambian. El plazo transitorio del 50.2 no está en el art. 50, sino en el nuevo art. 111.4.
  - `verified` (texto oficial del Reglamento 2026/1744, https://publications.europa.eu/resource/celex/32026R1744; corregido tras QA 2026-11-19).
- **¿Es Ucoach un "sistema de IA"?** Las directrices de la Comisión sobre la definición (6-02-2025) excluyen los sistemas basados en reglas definidas solo por personas y el tratamiento básico de datos. El motor de `planificar_dia`, con sus reglas fijas, encaja en esa exclusión. La IA es el modelo del usuario (Claude o ChatGPT). Además, quien usa una IA a título personal y no profesional no es "responsable del despliegue" (art. 3.4). Por tanto, **la versión local probablemente queda fuera de la ley** salvo como componente. `verified` (directrices, versión formal C(2025) 5053 de 29-07-2025, https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-definition_en.pdf; corregido tras QA 2026-11-19) / `inferred` (encaje) ⚖️
- **Qué diseño de avisos mantiene a Ucoach fuera de la definición (corregido tras QA 2026-11-19; responde a la recomendación de micro-aleatorización del informe 03).** Según las directrices, la capacidad de inferir es "a key, indispensable condition". `inferred` ⚖️:
  - **Fuera:** reglas escritas por una persona, con aleatorización simple (probabilidad de envío fija) para medir qué tipo de aviso funciona, y una persona que revisa los resultados y retira los tipos sin efecto. El sistema no aprende ni infiere por sí mismo.
  - **Dentro:** un bandit o un aprendizaje por refuerzo que ajusta solo cuándo y qué enviar a cada usuario a partir de su respuesta, como el del ensayo de prevención de diabetes que cita el informe 03. Probablemente es un sistema de IA del que Ucoach es proveedor. Consecuencias: transparencia del art. 50 si interactúa con el usuario (aviso de que es una IA), alfabetización del art. 4 y prohibiciones del art. 5. Sigue siendo riesgo mínimo, no alto, mientras la finalidad sea el bienestar.
- **Si Ucoach "solo es una herramienta que usa un modelo de terceros"** `inferred`:
  - En la versión local, Ucoach es un servidor MCP que el usuario conecta a *su* asistente. El proveedor del sistema que conversa es Anthropic u OpenAI, que cumplen el art. 50.1 en su interfaz.
  - Si el Pro ofrece **su propia app o chat** con un modelo por API (por ejemplo, avisos móviles redactados por un LLM o un coach dentro de la app), **Ucoach es proveedor de un sistema de IA** que interactúa con personas. Debe avisar de que es una IA en el primer contacto, de forma específica y no escondida en los términos, con recordatorios en contextos sensibles (malestar emocional, consejos de salud) y siempre que se le pregunte (directrices sobre el art. 50, C(2026) 5054 de 20-07-2026, https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-07/guidelines_on_the_implementation_of_the_transparency_obligations_for_certain_ai_systems_under_article_50_of_the_ai_act_bzptwqhk0ikg1dtlddap41psfy_131215.pdf). `verified`. Las directrices definen al proveedor por el art. 3.3 (quien desarrolla o encarga el sistema y lo comercializa con su nombre); de ahí se deduce que construir sobre el modelo de otro no traslada la obligación, pero no lo dicen expresamente (`inferred`; corregido tras QA 2026-11-19).
  - Las obligaciones de los modelos de uso general son de Anthropic u OpenAI, no de Ucoach.
- **Clasificación:** el bienestar no está en el Anexo III, así que es **riesgo mínimo**, con transparencia del art. 50 si hay interacción directa. No es alto riesgo salvo que el producto pase a ser sanitario (Anexo I, MDR clase IIa o superior, que requiere organismo notificado → alto riesgo desde el 2-08-2028). `inferred`
- **Prácticas prohibidas relevantes (art. 5, desde el 2-02-2025)** `verified` (texto) / `inferred` (encaje):
  - **5.1.a, técnicas manipuladoras o engañosas** que alteren el comportamiento y causen un perjuicio importante. Riesgo bajo, pero hay que evitar el diseño adictivo (rachas punitivas, culpa) y los "avisos" que empujen a dormir menos o entrenar con fatiga.
  - **5.1.b, explotar vulnerabilidades** por edad, discapacidad o situación social o económica. Un emprendedor en crisis de agotamiento es vulnerable, así que el producto no debe aprovechar ese estado para vender Pro ni retener al usuario.
  - **5.1.f, reconocimiento de emociones en el trabajo y la educación.** Ver la sección 3.8. Las directrices de la Comisión sobre prácticas prohibidas (publicadas en febrero de 2025; versión formal C(2025) 5052 de 29-07-2025) dicen que "the general monitoring of stress levels at the workplace is not permitted" y que un sistema "to detect burnout or depression at the workplace" seguiría prohibido; la excepción médica se refiere a productos sanitarios con marcado CE y no cubre el bienestar general (ap. 257 y 263). `verified` (https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-prohibited_en.pdf; corregido tras QA 2026-11-19)
- **Reconocimiento de emociones fuera del trabajo.** El ánimo que el propio usuario escribe (1 a 5) no es reconocimiento de emociones, porque la ley lo define como inferencia a partir de datos biométricos. Si una versión futura **infiriera estados emocionales o "estrés" a partir de la VFC con un modelo**, podría ser un sistema de reconocimiento de emociones: alto riesgo del Anexo III, punto 1.c (desde el 2-12-2027), obligación de informar del art. 50.3 y prohibición en el trabajo. Conviene hablar de "recuperación" o "variabilidad cardiaca", no de "estrés emocional detectado". `inferred` ⚖️

### 3.4 Productos sanitarios (MDR 2017/745), regla 11 y FDA

- **La frontera.** El MDR define producto sanitario por su *finalidad prevista* (art. 2.1 y 2.12), que se deduce de la etiqueta, las instrucciones, la **publicidad** y las declaraciones del fabricante. El **considerando 19** excluye el software "destinado a fines de estilo de vida y bienestar". La guía **MDCG 2019-11 rev.1** (17-06-2025) mantiene la lógica, añade ejemplos (Anexo XVI, predicción y pronóstico, software modular) e introduce el concepto de IA sanitaria. `verified` (fecha y considerando) / `reported` (detalle de los ejemplos).
- **Regla 11:** el software que da información para decisiones con fines de diagnóstico o terapéuticos es **clase IIa** como mínimo (IIb o III si puede causar un deterioro grave o la muerte). El software que monitoriza procesos fisiológicos es IIa, o IIb si vigila parámetros vitales cuyas variaciones puedan suponer un peligro inmediato (corregido tras QA 2026-11-19). El resto es clase I. En la práctica, casi cualquier software sanitario necesita organismo notificado. `verified` (texto oficial del MDR, anexo VIII, https://publications.europa.eu/resource/celex/32017R0745)
- **¿Convierten estas palabras a Ucoach en producto sanitario?** `inferred` ⚖️

| Término | Riesgo | Por qué |
|---|---|---|
| "insomnio" | **Alto** si Ucoach lo detecta, puntúa o trata. **Bajo** si solo deriva ("si te cuesta dormir de forma persistente, consulta a un profesional") | Es un trastorno con criterios diagnósticos. Ofrecer TCC-I es terapia: las apps de TCC-I como Somryst o Sleepio están reguladas como productos sanitarios |
| "deuda de sueño" | **Bajo-medio** | Es un término divulgativo, no un diagnóstico. El riesgo sube si se presenta como medida clínica ("tu deuda indica riesgo de…") |
| "burnout" | **Medio-alto** | La OMS lo clasifica como fenómeno ocupacional (CIE-11 QD85), no como enfermedad, pero "detectar", "prevenir" o "tratar" el burnout suena a finalidad sanitaria y en el trabajo choca con el art. 5.1.f |
| "estrés" | **Bajo** en el sentido de bienestar ("gestionar el estrés", "relajarte"). **Alto** si es "detectamos estrés" a partir de biométricos o "reduce la ansiedad" | La propia FDA acepta el estrés como bienestar; "ansiedad" es una condición clínica |
| "VFC baja = enfermedad, arritmia, sobreentrenamiento clínico" | **Alto** | Interpretar biométricos para diagnosticar es la regla 11 |

- **FDA, *General Wellness: Policy for Low Risk Devices*, revisión del 6-01-2026** (sustituye a la de 2019):
  - El software para un estilo de vida saludable sin relación con enfermedades queda **excluido** de la definición de dispositivo (FDCA, sección 520(o)(1)(B)).
  - Los productos de bienestar **no pueden** mencionar "enfermedades concretas, condiciones clínicas ni umbrales diagnósticos".
  - Se permite un aviso del tipo "puede ser útil que lo evalúe un profesional" cuando un valor sale del rango de bienestar, siempre que no nombre enfermedades, no llame "anormal" al valor y no haya alertas continuas para gestionar una enfermedad.
  - La revisión se centra en wearables (presión arterial, VFC) y no menciona la IA. Permite mostrar valores, tendencias y líneas base de sueño, actividad, estrés y recuperación, y acepta la gestión del estrés como uso de bienestar.
  - La FDA incluyó la revisión de su política de software en la lista A del año fiscal 2026, pero no la publicó: sigue como borrador pendiente en la lista B del año fiscal 2027 (https://www.fda.gov/media/195054/download; corregido tras QA 2026-11-19).
  - `verified` (texto de la guía, https://www.fda.gov/media/90652/download; corregido tras QA 2026-11-19).

### 3.5 Estados Unidos (solo si se vende allí)

- **FTC Health Breach Notification Rule.**
  - Regla final aprobada el 26-04-2024, publicada en el Federal Register el 30-05-2024 y **en vigor desde el 29-07-2024**.
  - Cubre a los proveedores de "registros personales de salud" que reúnen datos de varias fuentes, como un wearable más una entrada manual, que es el caso de Ucoach Pro.
  - "Brecha" incluye **la cesión no autorizada**, no solo el hackeo, y la definición de dato identificable es amplia (incluye identificadores de dispositivo).
  - `verified` (Federal Register 2024-10855 vía despachos)
  - Versión local sin servidor: es dudoso que Ucoach sea "proveedor" de un registro, y no hay datos que puedan filtrarse desde el promotor. `inferred`
- **Casos de la FTC:**
  - **GoodRx** (02-2023): primera acción con la regla de brechas; multa civil de 1,5 M$ por compartir datos con Facebook y Google.
  - **BetterHelp** (03-2023): 7,8 M$ en devoluciones a consumidores (sección 5 de la FTC Act); compartía datos de salud mental para publicidad.
  - **Premom / Easy Healthcare** (17-05-2023): segunda acción con la regla de brechas; 100.000 $ más otros 100.000 $ para tres estados; SDK de terceros, incluidos dos chinos.
  - **Flo Health**: acuerdo con la FTC en 2021. Además, el 1-08-2025 un jurado de California declaró responsable a Meta en la demanda colectiva *Frasco v. Flo Health* (ley CIPA) por captar datos menstruales de Flo con su SDK; Google, Flo y Flurry habían llegado antes a acuerdos (https://lowey.com/cases/flo-health-class-action/; corregido tras QA 2026-11-19).
  - **Lección para Ucoach:** ningún SDK publicitario ni de analítica de terceros en la versión gestionada, y no afirmar privacidad que no se cumple (eso es engaño según la sección 5).
  - `verified` (FTC Premom; prensa sobre Flo) / `reported` (importes de GoodRx y BetterHelp, coherentes en varias fuentes)
- **Washington My Health My Data Act (RCW 19.373):**
  - "Datos de salud del consumidor" en sentido amplio: el Fiscal General pone de ejemplo una app que registra la digestión o la transpiración, y las inferencias cuentan.
  - Obligaciones: **consentimiento separado** para recoger y para compartir; **autorización firmada** para vender (guardarla 6 años); **política de privacidad de datos de salud propia, enlazada en la portada**.
  - La infracción lo es automáticamente de la ley de protección del consumidor de Washington, con **acción privada**.
  - Aplicable desde el 31-03-2024 (pequeñas empresas: 30-06-2024).
  - Primera demanda colectiva: Maxwell v. Amazon (W.D. Wash., 10-02-2025). Su estado procesal a noviembre de 2026 sigue sin verificar.
  - `verified` (Fiscal General) / `reported` (demanda)
- **Nevada SB 370** (en vigor el 31-03-2024): parecida pero más estrecha y sin acción privada; prohíbe el geovallado. **Connecticut SB 3** (Public Act 23-56; el texto marca 1-07-2023, algunos despachos dicen 1-10-2023 para las enmiendas de salud): añade los datos de salud del consumidor a los datos sensibles de su ley de privacidad (consentimiento) y prohíbe venderlos sin consentimiento. `reported` (Nevada, solo fuente secundaria) / `verified` (texto de la ley de Connecticut, https://www.cga.ct.gov/2023/ACT/PA/PDF/2023PA-00056-R00SB-00003-PA.pdf) (corregido tras QA 2026-11-19)
- **Nueva York (NYHIPA, S929):** **vetada** por la gobernadora el 19-12-2025. La versión revisada, S9269/A10357, la aprobaron el Senado (3-06-2026) y la Asamblea (4-06-2026); a 19-11-2026 no consta firma ni veto. `verified` (https://www.nysenate.gov/legislation/bills/2025/S9269; corregido tras QA 2026-11-19)
- **Recomendación:** lanzar solo en la UE y en el Espacio Económico Europeo. Si se abre EE. UU., poner a Washington como referencia de cumplimiento. `inferred`

### 3.6 Consumo y suscripciones (versión Pro)

- **Desistimiento de 14 días** (TRLGDCU, arts. 102 y siguientes; Directiva 2011/83). En servicios digitales, si el usuario pide que el servicio empiece antes de que acabe el plazo, hay que recabar su **consentimiento expreso** y, si desiste, cobrar solo la parte proporcional. `verified` (norma general, secundaria)
- **Botón de desistimiento (Directiva 2023/2673, nuevo art. 11 bis de la Directiva 2011/83):**
  - Función de desistimiento en línea visible y disponible durante todo el plazo, en contratos celebrados por interfaz en línea, **incluidas las suscripciones**.
  - **Los Estados debían aplicarla desde el 19-06-2026**, y el plazo para transponerla acabó el 19-12-2025. Una directiva necesita transposición: hasta que España la incorpore, la obligación no está en la ley española. A 04-11-2026, el TRLGDCU consolidado del BOE **no la recoge**. La Comisión envió carta de emplazamiento a España y a otros 20 Estados (enero de 2026), y el Gobierno aprobó en enero de 2026 un anteproyecto que la transpone en parte.
  - Hay que implementarla igualmente: llegará, y es buena práctica.
  - `verified` (directiva, https://publications.europa.eu/resource/celex/32023L2673; TRLGDCU, https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555) / `reported` (procedimiento de infracción y anteproyecto, https://elderecho.com/bruselas-expedienta-a-espana-por-no-transponer-la-directiva-sobre-servicios-financieros-a-distancia) (corregido tras QA 2026-11-19).
- **Ley 10/2025, de 26 de diciembre, de servicios de atención a la clientela** (BOE 27-12-2025): modifica el **art. 97.1.p del TRLGDCU**. Las empresas de suscripción deben avisar **al menos 15 días antes** de cada renovación automática, explicar qué pasa si no se cancela y facilitar una baja sencilla. `verified` (nota oficial del Ministerio de Consumo)
  - Nota: el encargo mencionaba la "Ley 4/2025". La norma que regula estas suscripciones es la **Ley 10/2025**. No encontré una "Ley 4/2025" relevante.
- **Contenidos y servicios digitales** (Directiva 2019/770, transpuesta en el TRLGDCU): conformidad, actualizaciones y no cambiar el servicio a peor sin aviso ni derecho a resolver. `reported`
- **Digital Fairness Act:** la Comisión presentó la propuesta el 11-11-2026. Cubre patrones oscuros, diseño adictivo (con opción de desactivarlo), cancelación fácil de suscripciones, fin de las renovaciones automáticas no deseadas y de las pruebas gratuitas trampa, influencers y personalización dirigida a menores. Es una propuesta, no una ley, pero afecta de lleno al Pro (suscripción) y al diseño de rachas y avisos. `verified` (https://commission.europa.eu/news-and-media/news/making-your-online-experience-fairer-2026-11-11_en) / número COM sin verificar (corregido tras QA 2026-11-19).

### 3.7 Proveedores de IA: retención y entrenamiento

- **Anthropic** (cambio anunciado el 28-08-2025) `verified`:
  - Afecta a los planes **Free, Pro y Max**, incluido Claude Code con esas cuentas. Los usuarios debían elegir antes del **8-10-2025** si permiten el uso de sus chats para entrenar.
  - Si lo permiten: **retención de 5 años** y uso para entrenamiento, aplicado a chats nuevos o retomados y también a las valoraciones de respuestas.
  - Si no lo permiten: 30 días.
  - Los chats borrados no se usan para entrenamientos futuros.
  - **No afecta** a Claude for Work (Team y Enterprise), Gov, Education, la API ni el acceso por Amazon Bedrock y Google Vertex AI.
- **OpenAI** `verified` (documentación de la API) / `reported` (consumo):
  - **API:** no entrena con los datos desde el 1-03-2023 salvo que el cliente lo active; guarda registros de abuso hasta 30 días; hay retención cero (ZDR) con aprobación previa. Los datos enviados a **servidores MCP de terceros** siguen las políticas de esos terceros.
  - **ChatGPT de consumo (Free, Plus, Pro):** usa el contenido para mejorar el modelo por defecto, salvo que se desactive "Mejorar el modelo para todos". Según análisis de terceros, eso incluye el contenido de apps y conectores.
  - **Business, Enterprise y Edu:** no entrenan por defecto.
  - OpenAI no revisa ni certifica las apps MCP personalizadas (*App Security Whitepaper*, junio de 2026).
- **Qué debe explicar Ucoach al usuario** `inferred`:
  1. Lo que devuelven las herramientas de Ucoach (sueño, VFC, ánimo) **entra en tu conversación** y lo procesa tu proveedor de IA con *sus* condiciones.
  2. En los planes de consumo, puede usarse para entrenar si no lo has desactivado (Claude: Ajustes → Privacidad; ChatGPT: Controles de datos), y la retención puede llegar a 5 años en Claude si lo has permitido.
  3. Con API, Team o Enterprise no se entrena por defecto.
  4. Ucoach no controla ni puede borrar lo que tu proveedor ya recibió: para borrarlo, borra el chat allí.
  5. Recomendación práctica: desactivar el entrenamiento, usar las herramientas con el mínimo de datos (resúmenes en lugar de series en bruto) y no pegar exportaciones completas.
- **Diseño que ayuda** `inferred`:
  - Que `contexto_del_dia` devuelva por defecto **resúmenes** ("sueño: justo; tendencia: estable") y no series en bruto.
  - Un modo "privado" que oculte las métricas biométricas.
  - Una herramienta `exportar_y_borrar`.
  - Avisar en el onboarding.

### 3.8 Plan Equipos

- **Si el cliente es una empresa** (equipo con empleados), la empresa es responsable y Ucoach encargado, o corresponsables si Ucoach define los informes.
  - El consentimiento del trabajador **casi nunca es libre** por el desequilibrio de poder (CEPD, directrices 05/2020).
  - La guía de la AEPD sobre relaciones laborales dice que **monitorizar la salud con pulseras o relojes está en general prohibido** salvo que lo prevea una ley, y que el empresario solo puede conocer la *aptitud* para el puesto, no el estado de salud.
  - El art. 88 del RGPD y los arts. 87 a 91 de la LOPDGDD (intimidad con dispositivos digitales, desconexión digital, videovigilancia, geolocalización y negociación colectiva) refuerzan el control.
  - La desconexión digital (art. 88 LOPDGDD) sí encaja con Ucoach si se plantea como política de reuniones y horarios, no como seguimiento de personas.
  - `verified` (guía de la AEPD actualizada en diciembre de 2025, https://www.aepd.es/documento/la-proteccion-de-datos-en-las-relaciones-laborales.pdf; directrices 05/2020, ap. 21-22, https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf; corregido tras QA 2026-11-19) ⚖️
- **Ley de IA:**
  - Inferir estrés, burnout o emociones de trabajadores a partir de biométricos está **prohibido** (art. 5.1.f, desde el 2-02-2025). La excepción médica no ampara el "bienestar general".
  - Usar IA para **monitorizar o evaluar el rendimiento y el comportamiento** de trabajadores es **alto riesgo** (Anexo III, punto 4.b; desde el 2-12-2027): gestión de riesgos, supervisión humana, registro e información a los representantes de los trabajadores.
  - `verified` (texto) / `reported` (directrices).
- **Socios fundadores sin relación laboral:** no se aplica la normativa laboral, pero la desigualdad de poder sigue existiendo (socio mayoritario, inversores) y los datos siguen siendo de salud. `inferred`
- **¿Es viable "agregado y anónimo" con 2 a 5 personas? No.** `inferred` (apoyado en el borrador 02/2026 del CEPD y el dictamen 05/2014 del Grupo del Artículo 29):
  - Con 2 personas, cada una deduce exactamente el dato de la otra a partir de la media y del suyo propio.
  - Con 3 a 5, basta comparar semana a semana (quién faltó, quién viajó) o contrastar con lo que se sabe del equipo ("la energía media bajó cuando Ana tuvo el pitch").
  - El borrador del CEPD pide que no se pueda **inferir** nada concreto de una persona, y reconoce que combinar estadísticas agregadas permite deducir datos individuales.
  - Ninguna fuente fija un umbral; la práctica estadística usa supresión de celdas con menos de 5 a 10 personas, y el ruido de la privacidad diferencial con n < 10 destruye la utilidad.
  - **Conclusión:** con equipos pequeños, los datos "agregados" siguen siendo personales y de salud.
- **Rediseño recomendado** `inferred`:
  1. El plan Equipos **no comparte datos de salud**: comparte **normas y calendario** (reuniones sin pausa, horas fuera de jornada, bloques de foco protegidos), que son datos de agenda, también personales pero no sensibles.
  2. Cada persona puede, si quiere, compartir **una señal elegida por ella** ("hoy voy justo de energía"), en el momento, sin histórico y revocable.
  3. Nunca informes por persona para quien manda; nunca métricas biométricas.
  4. Si algún día hay agregados, solo con 10 o más personas, con supresión y una EIPD propia.

### 3.9 Licencias: biblioteca de 103 libros

- **Ideas, no expresión.**
  - La LPI protege "creaciones originales… expresadas" (art. 10.1). Las ideas, métodos y conceptos no están protegidos (ADPIC, art. 9.2; Tratado de la OMPI sobre Derecho de Autor, art. 2).
  - Resumir una idea con palabras propias, en una o dos frases, no es "transformación" (art. 21) mientras no se copie la forma.
  - Hay precedente europeo: el Tribunal Supremo alemán, en *Perlentaucher* (I ZR 12/08, 1-12-2010), dijo que contar el contenido con palabras propias es en general lícito y que lo decisivo es **cuánto se copian formulaciones originales**, caso a caso.
  - `verified` (LPI en el BOE) / `reported` (Perlentaucher, solo resumen secundario: https://www.ra-plutte.de/kurzzusammenfassungen-von-buchrezensionen-abstracts-die-bgh-entscheidung-perlentaucher/) (corregido tras QA 2026-11-19)
- **Títulos.** El art. 10.2 de la LPI protege el título "cuando sea original, como parte de la obra". Usar el título para *identificar* el libro (con autor) es una referencia, no una explotación. Algunos títulos son además **marcas registradas** (por ejemplo, programas tipo "Miracle Morning"): se pueden usar de forma nominativa para referirse al libro, pero no para nombrar funciones de Ucoach ("Modo Miracle Morning"). `verified` (art. 10.2) / `inferred` (marcas; comprobar en EUIPO y USPTO).
- **Derecho de cita (art. 32.1).** Permite incluir fragmentos ajenos "a título de cita o para su análisis, comentario o juicio crítico", indicando autor y fuente, y la LPI española lo limita a fines docentes o de investigación. La biblioteca usa algunas frases entrecomilladas (por ejemplo, las preguntas de *The Coaching Habit*). Son muy breves y con atribución, así que el riesgo es bajo, pero no encajan con claridad en el art. 32. Mejor parafrasear o reducirlas al mínimo. `verified` (texto) / `inferred` (encaje)
- **Riesgo global: BAJO**, con estas condiciones:
  - Una o dos frases por libro, en palabras propias.
  - Sin listas ni estructuras copiadas a la letra (por ejemplo, las "cuatro leyes" de *Atomic Habits* se describen, no se traducen literalmente como lema).
  - Sin portadas ni extractos.
  - Sin enlaces a copias piratas.
  - Avisar de que el resumen no sustituye a la lectura (ya lo hace).
  - Si se monetiza un "plan de lectura" de pago muy centrado en libros concretos, el riesgo sube un poco. getAbstract, por ejemplo, licencia los resúmenes extensos con las editoriales; Ucoach no hace resúmenes extensos.
  - `inferred`
- **Licencia MIT:** el texto de la biblioteca forma parte del repositorio. Hay que asegurarse de que es contenido propio o licenciable (no generado copiando reseñas de terceros). Si alguna idea viene de una fuente con licencia restrictiva, sacarla. `inferred`

### 3.10 Otras normas a vigilar (no estaban en el encargo)

- **Cyber Resilience Act (Reglamento 2024/2847):**
  - En vigor desde el 10-12-2024; obligaciones de notificar vulnerabilidades desde el **11-09-2026** y todo lo demás desde el **11-12-2027**.
  - El software libre no monetizado queda fuera. Un modelo *open core* en el que la parte libre forma parte de una oferta comercial puede quedar dentro, igual que una app móvil de pago (considerandos 15 y 18).
  - ⚖️ `verified` (fechas y considerandos, https://publications.europa.eu/resource/celex/32024R2847) / `inferred` (encaje del *open core*) (corregido tras QA 2026-11-19)
- **Directiva (UE) 2024/2853 de responsabilidad por productos defectuosos:**
  - Incluye el software como producto, y entre los daños cuenta la destrucción de datos y los daños psicológicos médicamente reconocidos.
  - **Transposición hasta el 9-12-2026.** Excluye el software libre suministrado fuera de una actividad comercial.
  - Para el Pro: responsabilidad objetiva por defectos, incluidas las actualizaciones de seguridad.
  - `verified` (https://publications.europa.eu/resource/celex/32024L2853; corregido tras QA 2026-11-19)
- **Data Act (Reglamento 2023/2854), aplicable desde el 12-09-2025:**
  - El usuario de un wearable puede pedir que sus datos se compartan con un tercero (art. 5). Es una vía alternativa a las API comerciales de Oura, Garmin o Whoop.
  - Ucoach, como tercero, tendría límites: usar los datos solo para lo acordado con el usuario y no usarlos para desarrollar un producto competidor del fabricante.
  - `verified` (arts. 5 y 6, https://publications.europa.eu/resource/celex/32023R2854; corregido tras QA 2026-11-19) ⚖️
- **Real Decreto 1907/1996 (España), publicidad de productos y servicios "con pretendida finalidad sanitaria":** el art. 4 prohíbe en 16 supuestos la publicidad de productos o métodos con pretendida finalidad sanitaria. Entre ellos: presentarlos como útiles para prevenir o tratar el insomnio, atribuirles la capacidad de potenciar el rendimiento físico o psíquico, sugerir que sustituyen la consulta de profesionales sanitarios, asegurar alivio o curación, y usar testimonios de profesionales, famosos o pacientes. **No solo es relevante si se añaden prácticas como el grounding, suplementos u osteopatía** (posicionamiento aclarado en `00-scope.md`): también lo es para el mensaje de "rendimiento" que recomienda el informe 03 ("Llega a la negociación de mañana con energía") y para cualquier mención al insomnio. Hay que redactar el rendimiento como organización y hábitos, sin prometer efectos sobre el estado físico o mental. El Reglamento 1924/2006 regula las declaraciones nutricionales y de propiedades saludables de los **alimentos**. `verified` (texto del RD, https://www.boe.es/buscar/act.php?id=BOE-A-1996-18085; Reglamento, https://publications.europa.eu/resource/celex/32006R1924) / ⚖️ si un método de hábitos de sueño y energía entra en su ámbito (corregido tras QA 2026-11-19)
- **DSA (Reglamento 2022/2065):** la sincronización gestionada que almacena datos del usuario es un servicio de alojamiento de datos. Obliga a tener puntos de contacto, condiciones claras y un sistema de notificación de contenidos, aunque es poco relevante si no hay contenido público. `inferred`
- **Ley Europea de Accesibilidad (Directiva 2019/882, aplicable desde el 28-06-2025):** las microempresas que prestan servicios están exentas (art. 4.5). España la transpuso con la Ley 11/2023. `verified` (https://publications.europa.eu/resource/celex/32019L0882; corregido tras QA 2026-11-19)

---

## 4. Afirmaciones y palabras a evitar en los textos del producto

| Evitar | Por qué | Alternativa segura |
|---|---|---|
| "Tus datos de salud nunca salen de tu máquina" | Falso: pasan por el proveedor de IA (y por Telegram si se activa). Sería engañoso según la FTC y la normativa de consumo | "Ucoach guarda tus datos en tu ordenador. Cuando tu IA los consulta, los procesa tu proveedor de IA según sus condiciones." |
| "Privado" o "100 % privado" sin matiz | Igual que lo anterior | "Local por defecto. Sin servidores de Ucoach." |
| "Anónimo" (en Equipos) | No lo es con 2 a 5 personas | "Tu equipo solo ve lo que tú decides compartir." |
| "Diagnostica", "detecta", "trata", "cura", "previene [enfermedad]" | Finalidad sanitaria (MDR y FDA) | "Te ayuda a organizar", "propone", "sugiere hábitos" |
| "Insomnio" como algo que Ucoach mide o trata | Trastorno clínico | "Si te cuesta dormir de forma habitual, consulta a un profesional." Solo como derivación |
| "Combate o previene el burnout", "detecta el burnout" | Finalidad sanitaria y, en el trabajo, art. 5.1.f | "Ritmo sostenible", "proteger tu energía", "días de recuperación" |
| "Detectamos tu estrés con la VFC" | Posible reconocimiento de emociones o monitorización fisiológica | "Tu VFC de hoy está por debajo de tu media; puede ser buen día para algo suave." |
| "Reduce la ansiedad o la depresión" | Condiciones clínicas | "Ideas para relajarte", "pausas para desconectar" |
| "Tu VFC o FC es anormal o peligrosa" | Umbral diagnóstico (la FDA lo prohíbe explícitamente) | "Fuera de tu rango habitual. Si lo notas a menudo o te encuentras mal, consulta a un profesional." |
| "Deuda de sueño peligrosa", "riesgo de enfermedad" | Pronóstico clínico | "Has dormido menos de lo que te sienta bien; hoy, plan más ligero." |
| "Clínicamente probado", "basado en la ciencia" sin fuentes | Exige pruebas (consumo, RD 1907/1996, sección 5 de la FTC) | "Basado en recomendaciones de consenso (OMS…). Ver fuentes." |
| "Sustituye a tu médico, nutricionista o coach" | RD 1907/1996 | "No sustituye el consejo profesional." |
| "Potencia tu rendimiento físico y mental", "más energía garantizada" (añadido tras QA 2026-11-19) | RD 1907/1996, art. 4: prohíbe atribuir a un método con pretendida finalidad sanitaria la capacidad de potenciar el rendimiento físico o psíquico | "Organiza tu día para llegar con energía a lo importante", "planifica en función de cómo has dormido" |
| "Terapia", "tratamiento", "paciente", "síntomas" | Lenguaje clínico | "Hábito", "pauta", "usuario", "cómo te sientes" |
| "Interoperable con tu historia clínica" | Activaría la etiqueta del EHDS | No decirlo |
| "Coach" humano implícito | Art. 50 si hay chat propio | "Coach de IA" o "asistente" |

**Formulación de la finalidad prevista** (para la web, las tiendas de apps y los términos):
> "Ucoach es una herramienta de bienestar y organización personal para adultos sanos. Ofrece pautas generales de sueño, luz, actividad, alimentación y ergonomía. No está destinada a diagnosticar, tratar, curar, aliviar ni prevenir ninguna enfermedad, y no es un producto sanitario. Ante síntomas o dudas de salud, consulta a un profesional."

---

## 5. Correcciones a la sección "Privacidad, seguridad y regulación" de la v0.1

| Fila del documento | Veredicto | Corrección |
|---|---|---|
| **Datos:** "Todo en SQLite local… Sin servidores de Ucoach" | ✅ Bien | Añadir: cifrado opcional de la base (por ejemplo, SQLCipher o una clave del llavero del sistema), copia y borrado en un comando, y ninguna telemetría |
| **Red:** "Sin llamadas externas, salvo Telegram" | ✅ Bien, pero incompleto | Advertir de que el texto de los avisos pasa por Telegram y permitir avisos "neutros" sin cifras de salud |
| **Acciones:** solo escribe en local; las acciones externas las confirma el usuario | ✅ Bien | Es una buena defensa ante inyección de instrucciones. Mantener las herramientas de solo lectura y escritura local |
| **Proveedor de IA:** "Debe explicarse con claridad" | ⚠️ Correcto pero insuficiente | Concretar el texto (sección 3.7): planes de consumo frente a API o empresa, desactivar el entrenamiento, retención de 5 años o 30 días en Claude, y que Ucoach devuelva resúmenes por defecto |
| **Propuesta de valor:** "sin que tus datos de salud salgan de tu máquina" | ❌ **Incorrecto** | Contradice la fila anterior. Cambiar por "sin servidores de Ucoach: tus datos viven en tu ordenador y solo los ve la IA que tú eliges" |
| **Datos de salud:** art. 9; en local "el usuario controla"; la gestionada necesitará consentimiento explícito, cifrado y EIPD | ⚠️ Bien encaminado, incompleto | Añadir: (1) excepción doméstica y que el promotor no es responsable *mientras no reciba datos*; (2) **la fase de validación con 20 usuarios sí trata datos de salud**; (3) energía y ánimo también cuentan como salud; (4) en Pro: encargados, alojamiento en la UE, push sin datos, brechas en 72 h, DPO a escala; (5) **EE. UU. tiene reglas propias** (FTC, Washington) |
| **Ley de IA:** "fuera del alto riesgo; transparencia; confirmar con abogado" | ⚠️ Correcto en lo esencial | Matizar: (1) el motor de reglas probablemente no es un sistema de IA; (2) el art. 50 aplica desde el 2-08-2026 si hay chat o app propia; (3) el Omnibus (Reglamento 2026/1744) retrasó el alto riesgo pero no las prohibiciones; (4) **el plan Equipos sí roza el art. 5.1.f y el Anexo III, punto 4** |
| **Límite médico:** "Sin diagnósticos ni tratamientos; deriva" | ✅ Bien | Añadir la finalidad prevista por escrito y la lista de palabras de la sección 4. Revisar el texto de la biblioteca (hay una ficha con TCC para el insomnio y un libro titulado *Burnout*): está bien como lectura, pero Ucoach no debe "aplicar" TCC-I |
| **Pie:** "No es un dispositivo médico…" | ✅ Bien | Usar "producto sanitario", que es el término legal en España |
| **Modelo de negocio, Equipos:** "informes agregados y anónimos" | ❌ **No viable como está** | Rediseñar (sección 3.8) |
| **Falta** | ➕ | Consumo (desistimiento, botón, aviso de 15 días antes de renovar); edad mínima (18 años, o 14 como mínimo en España para consentir: art. 7 LOPDGDD); licencias de la biblioteca; seguridad del canal MCP (inyección de instrucciones desde otros conectores); CRA y responsabilidad por productos para el Pro |

---

## 6. Recomendaciones priorizadas

**P0: ahora, antes de la validación con 20 emprendedores**
1. Corregir la frase "sin que tus datos salgan de tu máquina" en el documento, el README y la web.
2. Escribir la finalidad prevista (sección 4) y repasar todos los textos de protocolos, prompts y biblioteca con la lista de palabras.
3. Hoja informativa y consentimiento explícito para la validación. Recoger solo lo mínimo: métricas agregadas que el usuario elige compartir; nada en bruto. Base: art. 9.2.a. Plazo de borrado. Registro de actividades (aunque sea sencillo).
4. Pantalla de onboarding "Tu IA y tus datos", con instrucciones para desactivar el entrenamiento en Claude y ChatGPT.
5. Que `contexto_del_dia` y `revision_semanal` devuelvan resúmenes por defecto, con una opción de detalle.
6. Ninguna telemetría. Si algún día la hay: que sea opcional, anónima de verdad y documentada.

**P1: antes de la versión gestionada (Pro)**
7. EIPD completa, registro de actividades, contratos con cada encargado, alojamiento en la UE, cifrado de extremo a extremo si se promete que el promotor no puede leer los datos, push sin datos de salud, procedimiento de brechas de 72 h y valorar un DPO externo.
8. Consentimiento explícito granular por fuente (wearable, calendario, check-ins), con un panel para retirarlo y borrar los datos.
9. Ningún SDK de publicidad ni de analítica de terceros en la app ni en la web con sesión iniciada (lección de GoodRx, BetterHelp, Premom y Flo).
10. Si hay chat o app con un LLM propio: aviso de "estás hablando con una IA" (art. 50), recordatorios en contexto de salud y medidas de alfabetización (art. 4).
11. Consumo: desistimiento con consentimiento expreso para empezar antes de que acabe el plazo, botón de desistimiento, aviso 15 días antes de cada renovación y baja en dos clics.
12. Revisar el CRA y la responsabilidad por productos (Directiva 2024/2853) para el Pro y la app móvil.

**P2: antes del plan Equipos y de EE. UU.**
13. Rediseñar Equipos con normas y calendario, sin datos de salud (sección 3.8). Nada de inferir estrés o emociones. EIPD propia.
14. EE. UU.: política de datos de salud según la ley de Washington, consentimiento separado y procedimiento para la regla de brechas de la FTC. O no vender allí.
15. Comprobar en la EUIPO y la USPTO las marcas de los títulos de la biblioteca que se usen como nombre de función.

**⚖️ Qué confirmar con un abogado**
- Que el promotor no es responsable en la versión local y que la fase de validación cumple (consentimiento y hoja informativa).
- Si el Pro con cifrado de extremo a extremo cambia el reparto de papeles; si hace falta DPO y a partir de qué volumen.
- Las bases jurídicas del Pro (art. 6.1.b más 9.2.a) y el texto del consentimiento.
- Que Ucoach queda fuera del MDR con la finalidad redactada, y revisión de los textos de sueño y de la ficha de TCC-I.
- Ley de IA: si el motor queda fuera de la definición de sistema de IA; las obligaciones del art. 50 si hay app propia; el diseño del plan Equipos frente al art. 5.1.f y el Anexo III, punto 4.
- Seguimiento de: la transposición española de la Directiva 2023/2673 (pendiente a 04-11-2026), la casación C-703/25 P contra el Marco de Privacidad, el Omnibus de datos (RGPD, en comisión en el Parlamento) y la propuesta de Digital Fairness Act del 11-11-2026 (corregido tras QA 2026-11-19).
- Normas no analizadas en este informe (añadido tras QA 2026-11-19): art. 22 del RGPD (perfilado, porque el plan del día depende del estado del usuario), LSSI-CE y cookies para la web y la lista de espera, políticas de Apple HealthKit y Google Health Connect para los datos importados, términos de las API de Oura, Garmin y WHOOP, y Reino Unido.
- Si el CRA se aplica al *open core* (MIT) cuando existe una versión de pago.
- RD 1907/1996: si el mensaje de rendimiento, energía y sueño entra en su ámbito, y si se añaden prácticas complementarias (grounding, suplementos, osteopatía) (corregido tras QA 2026-11-19).
- Uso de títulos y frases entrecomilladas de la biblioteca.

---

## 7. Índice de fuentes

Fecha de consulta: 19-11-2026, salvo que se indique otra cosa. La confianza va entre corchetes.

**UE: textos y organismos oficiales**
1. Reglamento (UE) 2026/1744 (Digital Omnibus sobre IA), EUR-Lex: https://eur-lex.europa.eu/eli/reg/2026/1744/oj [la ficha existe; contenido vía nicfab]
2. nicfab, "Digital Omnibus on AI: Regulation (EU) 2026/1744 is published in the Official Journal" (07-2026): https://www.nicfab.eu/en/posts/digital-omnibus-ai-official-journal/ [verified, coherente con 3 a 5]
3. Comisión Europea / Transition Pathways, "AI Act Digital Omnibus: high-risk deadlines postponed" (2026): https://transition-pathways.europa.eu/adv-man/legislation/ai-act-digital-omnibus-high-risk-deadlines-postponed-machinery-carved-out
4. Sidley, "EU Lawmakers Reach Provisional Agreement to Delay Key EU AI Act Obligations" (22-06-2026): https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/
5. Usercentrics, "EU AI Act Deal: Digital Omnibus Now in Force" (2026): https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/
6. DLA Piper, "The EU's new guidelines on AI transparency" (10-08-2026), sobre las directrices del art. 50 del 20-07-2026: https://www.dlapiper.com/en-es/insights/publications/2026/08/the-eus-new-guidelines-on-ai-transparency
7. Comisión Europea, directrices sobre la definición de sistema de IA (6-02-2025): https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application [reported, vía Covington y Bird & Bird]
8. Directrices de la Comisión sobre prácticas prohibidas, resumen de Bird & Bird, "AI & the Workplace" (2025): https://cm.twobirds.com/en/insights/2025/global/ai-and-the-workplace-navigating-prohibited-ai-practices-in-the-eu ; Wolters Kluwer (14-04-2025): https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/
9. Reglamento (UE) 2025/327 (EHDS), EUR-Lex: https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng ; art. 47: https://www.ringholm.com/ehds/article-47.htm ; art. 105: https://streamlex.eu/articles/ehds-en-art-105/ [verified]
10. Comisión Europea (DG SANTE), MDCG 2019-11 rev.1 (17-06-2025): https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en ; Emergo by UL, resumen de la rev.1: https://www.emergobyul.com/news/european-revision-primary-software-guidance-mdcg-2019-11-revision-1-small-changes-meaningful
11. MDR, considerando 19 y regla 11, vía Sano Labs / CMS / Taylor Wessing: https://www.sanolabs.eu/blog/wellness-app-vs-medical-device-eu-mdr/ [verified para el considerando, coherente en varias fuentes]
12. TJUE C-184/20, OT (1-08-2022), comentario de Covington: https://www.insideprivacy.com/eu-data-protection/special-category-data-by-inference-cjeu-significantly-expands-the-scope-of-article-9-gdpr/
13. TJUE C-21/23, Lindenapotheke (4-10-2024), nota de prensa: https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-10/cp240159en.pdf ; Bird & Bird: https://cm.twobirds.com/en/insights/2024/global/feeling-unwell-after-the-cjeus-lindenapotheke-decision
14. TJUE C-683/21 (5-12-2023), EUR-Lex: https://eur-lex.europa.eu/eli/C/2024/914/oj/eng ; IAPP: https://iapp.org/news/a/the-cjeu-rules-on-the-liability-of-controllers
15. Grupo del Artículo 29, anexo "Health data in apps and devices" (5-02-2015), resumen: https://www.insideprivacy.com/international/european-union/article-29-working-party-clarifies-scope-of-health-data-in-apps-and-devices/
16. CEPD, directrices 4/2019 sobre el art. 25 (v2.0, 2020): https://edpb.europa.eu/sites/default/files/consultation/edpb_guidelines_201904_dataprotection_by_design_and_by_default.pdf ; texto: https://gdpr-text.com/guidelines/pbd
17. CEPD, borrador de directrices 02/2026 sobre anonimización (7-07-2026; consulta hasta el 30-10-2026), Covington: https://www.covingtonblogs.com/2026/08/04/edpb-publishes-draft-guidelines-on-anonymisation/
18. Digital Omnibus de datos (RGPD), propuesta del 19-11-2025: Latham & Watkins: https://www.lw.com/en/insights/digital-omnibus-eu-commission-proposes-to-streamline-gdpr-and-eu-ai-act ; European Law Blog sobre el art. 9: https://europeanlawblog.eu/the-ai-exemption-that-isnt-how-the-digital-omnibus-weakens-article-9s-strongest-protections-under-the-guise-of-technical-necessity/ ; IAPP: https://iapp.org/news/a/eu-digital-omnibus-amendments-to-gdpr-to-facilitate-ai-training-miss-the-mark [reported]

**España**
19. AEPD, lista de tratamientos que requieren EIPD (6-05-2019): https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-publica-el-listado-de-tratamientos-en-los-que-es
20. AEPD, guía "La protección de datos en las relaciones laborales": https://www.aepd.es/guias/la-proteccion-de-datos-en-las-relaciones-laborales.pdf [reported, vía El Derecho e Iberley]
21. BOE, Ley 10/2025, de 26 de diciembre (servicios de atención a la clientela): https://www.boe.es/eli/es/l/2025/12/26/10
22. Ministerio de Consumo, nota sobre la nueva regulación de suscripciones (art. 97.1.p del TRLGDCU): https://www.dsca.gob.es/es/consumo/nota-informativa-nueva-regulacion-suscripciones-ley-servicios-atencion-clientela
23. OCU, botón de desistimiento (19-06-2026): https://www.ocu.org/organizacion/prensa/notas-de-prensa/2026/normabotondesistimiento190626 ; El Derecho: https://elderecho.com/contratar-en-un-clic-desistir-tambien-las-nuevas-reglas-del-derecho-de-desistimiento-online ; iubenda: https://www.iubenda.com/es/blog/la-nueva-funcion-de-desistimiento-online-que-significa-la-directiva-ue-2023-2673-para-tu-empresa/
24. BOE, Ley de Propiedad Intelectual (RDL 1/1996), texto consolidado: https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930
25. Tribunal Supremo alemán, *Perlentaucher* (I ZR 12/08, 1-12-2010), resumen: https://www.mth-partner.de/en/copyright-admissibility-of-so-called-abstracts-short-summaries/ ; getAbstract sobre licencias: https://support.getabstract.com/en/knowledge/summaries-copyright

**EE. UU.**
26. Covington, "FDA issues revised guidance on general wellness products" (8-01-2026): https://www.cov.com/en/news-and-insights/insights/2026/01/fda-issues-revised-guidance-on-general-wellness-products ; King & Spalding: https://www.kslaw.com/insights/articles/fda-updates-general-wellness-and-clinical-decision-support-guidance-documents
27. FTC, Premom (17-05-2023): https://www.ftc.gov/news-events/news/press-releases/2023/05/ovulation-tracking-app-premom-will-be-barred-sharing-health-data-advertising-under-proposed-ftc
28. Regla de brechas de salud de la FTC, regla final de 2024: Morrison Foerster: https://www.mofo.com/resources/insights/240514-ftc-issues-final-rule-to-expand ; Venable: https://www.venable.com/insights/publications/2024/07/final-changes-to-health-breach-notification
29. GoodRx y BetterHelp (importes): https://blog.promise.legal/ftc-health-breach-notification-rule-health-apps/ [reported]
30. Flo contra Meta, veredicto del jurado (08-2025): https://techcrunch.com/2025/08/05/jury-rules-meta-violated-california-privacy-laws-by-collecting-menstrual-health-data-from-flo
31. Fiscal General de Washington, My Health My Data Act: https://www.atg.wa.gov/protecting-washingtonians-personal-health-data-and-privacy
32. Orrick, primera demanda con la ley de Washington (Amazon, 02-2025): https://www.orrick.com/en/Insights/2025/02/First-Lawsuit-Filed-Under-Washingtons-My-Health-My-Data-Act
33. McDermott, Nevada y Connecticut: https://www.mcdermottlaw.com/insights/nevada-and-connecticut-pass-consumer-health-data-laws/ ; Bass Berry, Nevada en vigor el 31-03-2024: https://www.bassberry.com/news/nevada-consumer-health-data-law-takes-effect-on-march-31-2024/
34. Veto de la ley de Nueva York (19-12-2025): https://www.insideprivacy.com/health-privacy/new-york-governor-vetoes-restrictive-health-privacy-law/ ; MoFo, versión de 2026: https://www.mofo.com/resources/insights/260316-nyhipa-returns-in-2026-revised-bill

**Proveedores de IA**
35. Anthropic, "Updates to our consumer terms" (28-08-2025): https://www.anthropic.com/news/updates-to-our-consumer-terms [verified]
36. OpenAI, "Data controls in the OpenAI platform" (API): https://developers.openai.com/api/docs/guides/your-data [verified]
37. OpenAI, controles de datos de ChatGPT y *App Security Whitepaper* (06-2026): https://help.openai.com/articles/20001496 ; https://cdn.openai.com/business-guides-and-resources/app-security-whitepaper.pdf [reported; openai.com devolvió 403]

**Añadidas tras el QA del 2026-11-19** (textos oficiales consultados por el verificador independiente)
39. RGPD, texto oficial: https://publications.europa.eu/resource/celex/32016R0679 ; LOPDGDD: https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673
40. Reglamento (UE) 2026/1744, texto oficial: https://publications.europa.eu/resource/celex/32026R1744 ; Ley de IA: https://publications.europa.eu/resource/celex/32024R1689
41. Comisión Europea, directrices sobre la definición de sistema de IA, C(2025) 5053: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-definition_en.pdf ; sobre prácticas prohibidas, C(2025) 5052: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-prohibited_en.pdf ; sobre el art. 50, C(2026) 5054: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-07/guidelines_on_the_implementation_of_the_transparency_obligations_for_certain_ai_systems_under_article_50_of_the_ai_act_bzptwqhk0ikg1dtlddap41psfy_131215.pdf
42. Reglamento (UE) 2025/327 (EEDS): https://publications.europa.eu/resource/celex/32025R0327 ; MDR: https://publications.europa.eu/resource/celex/32017R0745
43. TJUE C-413/23 P (SRB): https://publications.europa.eu/resource/celex/62023CJ0413 ; T-553/23 (Latombe): https://publications.europa.eu/resource/celex/62023TJ0553 ; casación C-703/25 P: https://publications.europa.eu/resource/celex/62025CN0703 ; Decisión 2023/1795: https://publications.europa.eu/resource/celex/32023D1795
44. CEPD, directrices 05/2020 sobre el consentimiento: https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf ; directrices 02/2026 sobre anonimización: https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf ; dictamen conjunto 2/2026: https://www.edpb.europa.eu/system/files/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf ; Grupo del Artículo 29, dictamen 05/2014: https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf
45. AEPD, listas de tratamientos que requieren EIPD: https://www.aepd.es/documento/listas-dpia-es-35-4.pdf
46. Directiva 2023/2673: https://publications.europa.eu/resource/celex/32023L2673 ; TRLGDCU consolidado: https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555 ; Ley 10/2025: https://www.boe.es/buscar/act.php?id=BOE-A-2025-26698
47. Comisión Europea, propuesta de Digital Fairness Act (11-11-2026): https://commission.europa.eu/news-and-media/news/making-your-online-experience-fairer-2026-11-11_en
48. FDA, guía General Wellness (2026): https://www.fda.gov/media/90652/download ; prioridades de guías del año fiscal 2027: https://www.fda.gov/media/195054/download
49. Senado de Nueva York, S9269: https://www.nysenate.gov/legislation/bills/2025/S9269 ; Connecticut, Public Act 23-56: https://www.cga.ct.gov/2023/ACT/PA/PDF/2023PA-00056-R00SB-00003-PA.pdf ; Flo, demanda colectiva: https://lowey.com/cases/flo-health-class-action/
50. RD 1907/1996: https://www.boe.es/buscar/act.php?id=BOE-A-1996-18085 ; CRA: https://publications.europa.eu/resource/celex/32024R2847 ; Directiva 2024/2853: https://publications.europa.eu/resource/celex/32024L2853 ; Data Act: https://publications.europa.eu/resource/celex/32023R2854 ; Directiva 2019/882: https://publications.europa.eu/resource/celex/32019L0882

**Contexto adicional**
38. Directivas y reglamentos citados de memoria y no verificados en la sesión original (verificados después en el QA de 2026-11-19, ver 39 a 50): CRA 2024/2847, Directiva 2024/2853, Data Act 2023/2854, RD 1907/1996, Ley Europea de Accesibilidad 2019/882, decisión de adecuación UE-EE. UU. (10-07-2023) y asunto Latombe [reported, a confirmar].
