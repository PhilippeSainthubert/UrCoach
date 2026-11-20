# UrCoach · Brand kit v1

La guía visual está en `../urcoach-brand-kit.html`.

## Qué hay aquí

| Carpeta | Contenido |
|---|---|
| `logo/` | Isologotipo horizontal y apilado, y el símbolo suelto. Cada uno en color, color sobre oscuro, negro, blanco e índigo. Todo en SVG. |
| `app/` | El favicon (SVG y PNG de 16, 32 y 48 px), `apple-touch-icon-180`, los iconos de 192 y 512 px, y los iconos de app claro y oscuro a 1024 px. |
| `social/` | La imagen para compartir (1200 × 630), el banner de LinkedIn (1584 × 396) y el avatar (400 px). |
| `tokens/` | `tokens.css` (variables `--uc-*`) y `tokens.json`. |
| `_generador/` | `build_kit.py` genera todos los archivos y `guide.py`, la guía. |

## Reglas rápidas

- **Logo:** el ensō va siempre con el degradado del día y el nombre, en una sola tinta. No se estira, no se gira, no lleva sombras y el ensō no se cierra.
- **Proporciones:** el ensō mide 1,5 veces la altura de las mayúsculas. La separación entre el ensō y el nombre es 0,36 veces su diámetro, y ese mismo espacio es el margen mínimo alrededor del logo.
- **Tamaño mínimo:** 88 px de ancho para el horizontal. Por debajo se usa el símbolo solo, hasta 16 px.
- **Color:**
  - papel `#FAF9FC`;
  - tinta `#121018`;
  - índigo foco `#4F46E5`, el único color de acción;
  - noche `#0B0A12`.
- **Degradado del día:** cielo `#1FB6F2` → azur `#4C7CF6` → índigo `#4F46E5` → violeta `#7C3AED` → lavanda `#9061F9`, interpolado en OKLab. Se usa en el ensō y en la segunda línea del titular de portada; nunca en botones ni en texto corrido.
- **Letra:**
  - Inter Tight 600 para titulares y el logo;
  - Inter para el texto;
  - Instrument Serif cursiva para la segunda línea de los titulares.

  Las tres tienen licencia OFL.

## Regenerar

```bash
cd _generador
python build_kit.py   # archivos
python guide.py       # guía HTML
```

Hace falta Python con `fonttools`, `uharfbuzz` y `resvg_py` para los PNG. Las fuentes están en `_generador/fonts/`, todas con licencia OFL.

## Pendiente

- **Nombre:** UrCoach es nombre de trabajo y falta comprobarlo en la EUIPO y la OEPM.
- **Ensō:** la versión final del trazo la debería pintar un calígrafo; ahora es una imitación geométrica.
