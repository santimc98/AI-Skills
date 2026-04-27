---
name: educa-edtech-pptx
description: "Use this skill whenever you need to create a PowerPoint presentation (.pptx) for Educa Edtech Group or any of its brands (Atlax360, AI Tutor, EDUCA LXP, etc.). Trigger on these cues — user is Santi from Atlax360/Educa Edtech and mentions 'presentación', 'pptx', 'deck', 'slides', 'diapositivas', 'reunión interna', 'comité', 'project manager', 'stakeholders', or references internal Educa Edtech topics (cursos online, plataforma educativa, IA embebida, Order to Cash, seguro de crédito). Also use whenever the user asks to turn a dashboard, report, Excel analysis or internal meeting content into slides. Always prefer this skill over generic pptx creation when the deliverable is a corporate presentation for Educa Edtech — the corporate template, palette, fonts and layout rules are non-negotiable for internal audiences."
---

# Presentaciones corporativas · Educa Edtech Group

Este skill existe para que cualquier slide que produzcas para Educa Edtech salga ya **on-brand**, sin tener que corregir después fuentes, colores o maquetación. Parte siempre de la plantilla corporativa incluida en `assets/template.pptx`.

## Regla de oro

**No crees la presentación desde cero con `python-pptx` en blanco.** Abre siempre `assets/template.pptx`, borra las slides que no necesites y añade nuevas reutilizando los *slide_layouts* del master. Así heredas gratis: el logo "EDUCA EDTECH Group" rotado en el margen derecho, las tipografías, el tamaño 16:9 widescreen (26,67 × 15 in) y los placeholders de "Insert picture here".

Si alguna slide requiere una composición que ningún layout cubre, duplica la más parecida (`cp_and_append_slide`) y reemplaza su contenido.

## Identidad visual

### Paleta — úsala literal

Estos hex están sacados del theme y del uso real en la plantilla, en orden de importancia:

| Rol | Hex | Cuándo |
|---|---|---|
| **Carbón principal** | `#454546` | Títulos en fondo claro, fondos oscuros de secciones |
| **Blanco** | `#FFFFFF` | Fondo por defecto, texto sobre oscuro |
| **Negro profundo** | `#000000` | Barra vertical derecha con "EDUCA EDTECH Group", zonas de alto contraste muy puntuales |
| **Gris claro 1** | `#EBEBEB` | Cajas de contenido sobre blanco, filas zebra de tabla |
| **Gris claro 2** | `#D5D5D5` | Bandas decorativas, rayados |
| **Gris medio** | `#BABABA` | Texto secundario, separadores, números decorativos grandes |
| **Azul corporativo** | `#244A80` | Caja de "ÍNDICE" y acentos estructurales |
| Accent datos 1 | `#2E7ABE` | Series de gráficos (azul claro) |
| Accent datos 2 | `#60BFB8` | Series de gráficos (verde agua) |
| Accent datos 3 | `#E96A73` | Series de gráficos (coral, para alertas o contraste) |
| Accent datos 4 | `#963058` | Series de gráficos (burdeos) |

**No uses azules, verdes o rojos de fantasía fuera de esta lista.** Si necesitas un color para "positivo" o "alerta", usa `#60BFB8` y `#E96A73`.

### Tipografía

La plantilla usa estas cuatro fuentes. Respeta jerarquía aunque el equipo pida cambios menores:

| Uso | Fuente | Tamaño |
|---|---|---|
| Título de portada / cierre | **Rubik Medium** | 80 pt |
| Título de slide de contenido | **Rubik Medium** | 60 pt |
| Texto destacado / cita | **Rubik Medium** | 30 pt |
| Subtítulo / eyebrow | **Rubik Light** | 25–30 pt |
| Cuerpo de texto | **Lato** | 20 pt |
| Números decorativos gigantes (1, 2, 3…) | **Montserrat ExtraBold** | 200–400 pt en `#D5D5D5` / `#BABABA` |

Si la máquina donde va a abrirse la presentación no tiene Rubik/Lato, embébelas en el archivo o cae a Arial como fallback — pero intenta no hacerlo.

### Motivos visuales recurrentes

La plantilla tiene una personalidad clara. Reutiliza estos elementos para que el deck se sienta "de la casa":

1. **Barra vertical "EDUCA EDTECH Group"** (negro, rotada 90°) en el margen derecho de slides de contenido. Ya viene en los masters — no la quites.
2. **Franjas verticales de fotografía B/N** (cielo estrellado / planeta) en portada, slides de cita y cierre. El motivo es espacial.
3. **Cajas con esquinas muy redondeadas** (radio ~20–30 pt) para contenedores destacados — especialmente la caja azul del índice y las tarjetas de KPIs.
4. **Números decorativos gigantes** en gris claro detrás o sobre un texto pequeño (layout "Three number with texts").
5. **Píldoras** (shape rounded rectangle extremos semicirculares) blancas sobre fondo negro para títulos de categoría (ver slide 27 "KPIs clave").
6. **Mucho espacio en blanco.** La plantilla respira. No rellenes cada cm — margen mínimo 0,7 in por lado.

## Layouts clave a reutilizar

La plantilla incluye 36 slides de ejemplo. Identifica estos **6 patrones** y úsalos como punto de partida. Los números que aparecen entre paréntesis son las slides de referencia en `assets/template.pptx`.

1. **Portada corporativa** (slide 2) — blanco + franjas espaciales + logo central. Úsala tal cual, sólo cambia título opcional.
2. **Slide de cita / mensaje** (slide 3) — gran titular a la izquierda, franjas de imagen a la derecha. Ideal para el "mensaje clave" de apertura o un hito.
3. **Índice** (slide 4) — barra negra "ÍNDICE" + rayado gris + caja azul `#244A80` con items numerados (círculos grises + texto blanco).
4. **Sección divider con número** (slide 5) — "01" gigante en gris, título debajo. Un divisor entre capítulos del deck.
5. **Contenido denso oscuro 3 columnas** (slide 7) — fondo `#454546`, título grande blanco, 3 columnas Lato 14–18pt.
6. **KPIs / dashboard** (slide 27) — fondo negro, columna izquierda con "KPIs / clave" 60pt, luego dos o tres columnas de métricas agrupadas con píldoras blancas arriba (Alcance, Engagement) y una columna aislada a la derecha con fondo blanco y píldora gris (Plataforma). Éste es el layout por defecto para cualquier slide con métricas o categorías paralelas.
7. **Tres números con texto** (slide 29) — 1 / 2 / 3 en `#BABABA` gigantes + tarjetas gris claro debajo con texto de 14pt.
8. **Cierre** (slide 6) — mismo tratamiento que portada: franjas espaciales + "Muchas gracias." + URL `www.educaedtech.com` en gris.

## Flujo de trabajo recomendado

Cuando el usuario te pida una presentación para Educa Edtech:

1. **Lee el brief y mapea a layouts** antes de tocar código. Decide qué slide de la plantilla es el punto de partida para cada slide de la nueva presentación. Anótalo.
2. **Copia la plantilla** a tu working directory:
   ```python
   import shutil
   shutil.copy("<skill-path>/assets/template.pptx", "presentacion.pptx")
   ```
3. **Duplica los layouts que necesites** y borra el resto. Ver `scripts/deck_builder.py` para helpers probados (duplicar slide, borrar slides por índice, sustituir textos preservando formato).
4. **Rellena contenido reemplazando texto**, no recreando shapes. Los placeholders rotulados `INSERT PICTURE HERE` se sustituyen por imágenes vía `shape.insert_picture` o eliminando el shape y añadiendo `Picture`.
5. **Inserta gráficos como imagen PNG** generada con matplotlib, no como `pptx.chart.Chart`. Da mucho mejor acabado y permite respetar la paleta. Usa la paleta de arriba y `font.family = 'Arial'` o `'DejaVu Sans'` si Lato no está.
6. **Limpia metadatos** (título, autor) antes de entregar — no dejes "Plantilla ppt EDUCA EDTECH".
7. **Verifica visualmente** convirtiendo a PDF e inspeccionando con un subagente antes de decir "listo". Busca específicamente:
   - Texto que desborda su shape (muy común al reemplazar contenido)
   - Barra "EDUCA EDTECH Group" desaparecida o duplicada
   - Logos / imágenes espaciales que al copiar layouts se han estirado
   - Tipografías que han caído a Calibri (señal de que Rubik/Lato no se aplicaron)

## Cosas que no hacer

- **No impongas paletas ajenas** aunque el tema de la presentación lo sugiera (ej. aunque sea sobre "IA" no metas cian eléctrico). Siempre la paleta corporativa.
- **No uses bullets redondos clásicos (•).** La plantilla usa iconos y numeración; bullets planos rompen el estilo.
- **No centres el cuerpo de texto.** Left-aligned siempre; sólo los títulos y los números decorativos se centran.
- **No añadas líneas horizontales decorativas bajo los títulos.** La plantilla usa espacio en blanco y tamaño para la jerarquía.
- **No dejes placeholders "INSERT PICTURE HERE" ni "Lorem ipsum"** en el entregable final. `extract-text` y `grep -i "insert\|lorem\|xxx"` antes de entregar.
- **No uses el logo pequeño de Educa Edtech flotando en slides de contenido** — ya lo aporta la barra vertical derecha de los masters.

## Snippets útiles

Están en `scripts/`:

- `scripts/deck_builder.py` — helpers para cargar la plantilla, duplicar un layout, borrar slides, reemplazar texto preservando estilo, e insertar un PNG en el hueco de un placeholder.
- `scripts/palette.py` — constantes con los hex y fuentes de la marca, listas para importar.

Impórtalos así:

```python
import sys
sys.path.insert(0, "<skill-path>/scripts")
from palette import CARBON, BLANCO, AZUL_EDUCA, ACCENT_DATOS, FONT_TITLE, FONT_BODY
from deck_builder import open_template, duplicate_slide, replace_text, insert_png_into_placeholder
```

## Cuándo desviarte del estilo

Si el cliente final es externo (propuesta comercial a un colegio, a un cliente de Atlax360) y te pide explícitamente "no uses la plantilla interna", pasa a la skill genérica `pptx`. Todo lo demás — reuniones internas, comités, reportes a PM, roadmaps, decks de producto para AI TUTOR/EDUCA LXP/Atlax360 — usa este skill.
