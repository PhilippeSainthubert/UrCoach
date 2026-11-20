---
name: ucoach-evaluar-practica
description: Evalúa una práctica de bienestar o rendimiento (osteopatía, grounding, frío, un suplemento, un protocolo de moda) o un libro propuesto para la biblioteca, le asigna nivel de evidencia A/B/C/D con fuentes y prepara la entrada para ucoach/content/practicas.json o biblioteca.json. Úsala cuando alguien diga «¿esto funciona?», «añade esta práctica», «evalúa este libro» o «me han recomendado X».
---

# Evaluar una práctica o un libro

Lanza el agente `curador-evidencia` si está disponible. Si no, sigue estos pasos tú mismo.

## Niveles

| Nivel | Criterio | Cómo la usa Ucoach |
|---|---|---|
| **A · Recomendable** | Metaanálisis, Cochrane o guía clínica a favor, con riesgo bajo | Por defecto en el plan |
| **B · Opcional** | Evidencia moderada o mixta, riesgo bajo | Si hay contexto |
| **C · Experimental** | Estudios pequeños, preliminares o contradictorios | Solo si preguntan; experimento personal de 2 semanas si no hay riesgo |
| **D · No recomendar** | Sin evidencia, refutada, con riesgo o con conflicto de interés que invalida los estudios | Se explica por qué y se ofrece una alternativa |

## Proceso

1. **Fuentes.** Busca primero revisiones Cochrane, metaanálisis y guías (NICE, AASM, OMS). Abre cada fuente: lo que recuerdas no cuenta como verificado. Anota el año.
2. **Conflictos de interés.** Por ejemplo, los autores con acciones en la empresa que vende la práctica.
3. **Riesgos y contraindicaciones.** Con suplementos: estado regulatorio en España y la UE, sin dosis personalizadas ni marcas.
4. **La entrada.** Redacta la entrada con el esquema exacto del fichero (mira las entradas que ya existen) y `revisado_el` con la fecha de hoy. La `pauta` va tuteando, sin palabras de la lista de `ucoach/content/palabras_evitar.json`.
5. **Libros.** Idea clave con palabras propias, una acción concreta en Ucoach y un aviso si alguna tesis está discutida o si el autor tiene intereses comerciales en lo que recomienda.
6. **Comprobación.** Ejecuta `python3 -m unittest tests.test_content` y `python3 -m ucoach lint-textos`.
7. **Cierre.** Enseña la entrada y sus fuentes al usuario antes de darla por buena.
