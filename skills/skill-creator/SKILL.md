---
name: skill-creator
description: Crea, mejora, audita y evalúa skills para el repositorio AI-Skills de Santi. Usa esta skill siempre que el usuario pida convertir un prompt, procedimiento, documentación, flujo de trabajo, tarea repetitiva o estilo de trabajo en una skill reutilizable; también cuando pida optimizar una skill existente, crear plantillas, actualizar index.md, diseñar pruebas de calidad o adaptar skills de Claude/ChatGPT/LibreChat/OpenClaw a un formato portable basado en GitHub.
---

# Skill Creator para AI-Skills

## Propósito

Esta skill sirve para crear y mantener skills reutilizables en el repositorio `santimc98/AI-Skills`.

Su objetivo no es solo escribir un archivo `SKILL.md`, sino convertir una forma de trabajar en un procedimiento claro, portable, verificable y fácil de reutilizar por distintos asistentes de IA.

Debe usarse especialmente cuando Santi quiera:

- Crear una skill nueva desde un prompt, una conversación, una documentación o una tarea repetitiva.
- Adaptar una skill de otra plataforma a su repositorio de GitHub.
- Mejorar una skill existente para que sea más clara, más específica o más fácil de activar.
- Crear plantillas asociadas a una skill.
- Crear documentos de conocimiento relacionados.
- Diseñar pruebas para comprobar si una skill funciona bien.
- Actualizar `index.md` para que la nueva skill sea descubrible.
- Convertir procedimientos de trabajo de Educa Edtech, LATIAX o proyectos personales en skills reutilizables.

## Principio central

Una buena skill no debe depender de que el asistente recuerde toda la conversación.

La skill debe dejar por escrito:

1. Cuándo debe activarse.
2. Qué objetivo persigue.
3. Qué entradas necesita.
4. Qué pasos debe seguir el asistente.
5. Qué criterios de calidad debe cumplir.
6. Qué formato de salida debe producir.
7. Qué errores debe evitar.
8. Qué plantillas o documentos debe consultar.

## Flujo obligatorio antes de crear o modificar una skill

Antes de crear o modificar cualquier skill del repositorio, seguir este flujo:

```text
Solicitud de Santi
        ↓
Leer README.md e index.md si están disponibles
        ↓
Buscar si ya existe una skill relacionada
        ↓
Decidir: crear nueva, mejorar existente, crear plantilla o crear knowledge
        ↓
Diseñar la estructura de la skill
        ↓
Redactar SKILL.md
        ↓
Crear o proponer plantillas/knowledge si hacen falta
        ↓
Proponer actualización de index.md
        ↓
Validar con checklist
        ↓
Pedir confirmación antes de modificar archivos reales, salvo permiso explícito
```

## Captura de intención

Cuando Santi pida crear una skill, primero extraer la intención real.

Si la conversación ya contiene suficiente contexto, no hacer preguntas innecesarias. Usar lo ya dicho y avanzar con supuestos explícitos.

Si falta información crítica, preguntar solo lo imprescindible.

### Preguntas útiles

No siempre hay que hacerlas todas. Usarlas solo si aportan claridad:

1. ¿Qué tarea exacta debe permitir hacer la skill?
2. ¿En qué contexto se usará: trabajo, universidad, LATIAX, proyecto personal u otro?
3. ¿Qué frases o situaciones deberían activar la skill?
4. ¿Qué herramientas intervienen: GitHub, GitLab, Jira, Confluence, Excel, SharePoint, n8n, correo, calendario, Python, etc.?
5. ¿Qué entregable final espera Santi?
6. ¿Qué pasos suele seguir un humano para hacer esta tarea?
7. ¿Qué errores frecuentes hay que evitar?
8. ¿Hay reglas internas de empresa, tono, formato o seguridad?
9. ¿La skill necesita plantillas?
10. ¿La skill necesita documentos de conocimiento relacionados?
11. ¿Hay que probarla con ejemplos?

## Decidir el tipo de artefacto

No todo debe convertirse en una skill.

Usar esta decisión:

| Caso | Artefacto recomendado |
|---|---|
| Procedimiento reutilizable con pasos claros | `skills/nombre-skill/SKILL.md` |
| Formato repetible de entrega | `templates/nombre-template.md` |
| Reglas, glosario, contexto o política interna | `knowledge/nombre-documento.md` |
| Ejemplos de uso o casos resueltos | `examples/nombre-ejemplo.md` |
| Automatización determinista o validación | `skills/nombre-skill/scripts/` |
| Documentación extensa que no debe cargarse siempre | `skills/nombre-skill/references/` |

## Estructura recomendada de una skill

Cada skill debe tener esta estructura base:

```markdown
---
name: nombre-skill
description: Descripción clara y activadora. Debe indicar qué hace la skill y cuándo debe usarse.
---

# Nombre de la skill

## Cuándo usar esta skill

## Objetivo

## Entradas necesarias

## Procedimiento paso a paso

## Criterios de calidad

## Formato de salida esperado

## Errores comunes a evitar

## Plantillas relacionadas

## Conocimiento relacionado
```

La descripción del frontmatter es especialmente importante. Debe ser concreta y algo proactiva. No debe limitarse a describir la skill; debe indicar cuándo activarla.

Ejemplo débil:

```yaml
description: Skill para Excel.
```

Ejemplo mejor:

```yaml
description: Analiza, audita, mejora y documenta archivos Excel. Usa esta skill cuando el usuario pida revisar hojas, fórmulas, KPIs, dashboards, cálculos, tablas dinámicas, costes, simulaciones o preparar conclusiones a partir de un Excel.
```

## Reglas de escritura

Al redactar una skill:

- Usar instrucciones en modo imperativo.
- Ser específico y operativo.
- Evitar teoría innecesaria.
- Separar pasos obligatorios de recomendaciones.
- Indicar cuándo pedir confirmación.
- Indicar cuándo avanzar con supuestos.
- Indicar qué documentos consultar antes de actuar.
- Incluir criterios de calidad verificables.
- Incluir errores comunes a evitar.
- Mantener la skill razonablemente breve.
- Mover documentación larga a `references/`.
- Mover formatos repetibles a `templates/`.
- Mover reglas generales a `knowledge/`.

## Compatibilidad con ChatGPT y GitHub

Cuando se trabaje desde ChatGPT con el conector de GitHub:

1. Leer `index.md` antes de elegir una skill.
2. Leer el `SKILL.md` específico antes de ejecutar la tarea.
3. Si se va a crear o modificar una skill en GitHub, comprobar si el archivo ya existe.
4. Si el cambio afecta a varias rutas, listar claramente los archivos que se van a crear o modificar.
5. No modificar sistemas reales como Jira, Confluence, SharePoint, correo o calendario sin confirmación explícita.
6. Para cambios en el repositorio `AI-Skills`, se puede crear directamente el archivo si Santi ha dado permiso claro en el mensaje.
7. Si no hay permiso claro, entregar primero el contenido propuesto y pedir confirmación.
8. Después de crear una skill, actualizar o proponer la actualización de `index.md`.

## Organización recomendada de carpetas

Para una skill simple:

```text
skills/nombre-skill/
└── SKILL.md
```

Para una skill con recursos:

```text
skills/nombre-skill/
├── SKILL.md
├── references/
│   └── guia-detallada.md
├── scripts/
│   └── quick_validate.py
└── examples/
    └── ejemplo-uso.md
```

Para plantillas globales:

```text
templates/nombre-template.md
```

Para conocimiento compartido:

```text
knowledge/nombre-documento.md
```

## Evaluación de skills

Cuando una skill sea importante o se vaya a usar con frecuencia, crear pruebas simples.

Una evaluación no tiene por qué ser compleja. Puede consistir en una tabla con:

- Prompt de prueba.
- Skill esperada.
- Resultado esperado.
- Criterios de aprobación.
- Errores que invalidan la respuesta.

Usar `templates/skill-evaluation-template.md` como base.

### Tipos de evaluación

| Tipo de skill | Evaluación recomendada |
|---|---|
| Excel, datos, scripts, automatizaciones | Casos con salida verificable |
| Jira, Confluence, documentación | Checklist de estructura y calidad |
| Reporting ejecutivo | Evaluación de claridad, utilidad y trazabilidad |
| Investigación de IA | Evaluación de fuentes, actualidad y conclusiones prácticas |
| Estilo de escritura | Comparación cualitativa con ejemplos buenos/malos |
| Prompts o agentes | Pruebas de comportamiento con escenarios distintos |

## Checklist de calidad antes de entregar una skill

Antes de entregar o guardar una skill, comprobar:

- [ ] Tiene frontmatter con `name` y `description`.
- [ ] La descripción explica cuándo debe activarse.
- [ ] El objetivo es concreto.
- [ ] Las entradas necesarias están claras.
- [ ] El procedimiento está ordenado paso a paso.
- [ ] Define el formato de salida esperado.
- [ ] Incluye criterios de calidad verificables.
- [ ] Incluye errores comunes a evitar.
- [ ] Indica plantillas relacionadas si existen.
- [ ] Indica conocimiento relacionado si existe.
- [ ] No duplica una skill existente.
- [ ] No mezcla demasiadas tareas distintas.
- [ ] No depende de memoria implícita del chat.
- [ ] Es portable entre asistentes.
- [ ] Respeta las reglas globales del repositorio.
- [ ] Si modifica sistemas reales, exige confirmación explícita.

## Cómo mejorar una skill existente

Cuando Santi pida mejorar una skill:

1. Leer la skill actual.
2. Identificar su propósito.
3. Revisar si la descripción activa bien la skill.
4. Detectar ambigüedades, pasos incompletos o duplicidades.
5. Separar contenido largo en `references/`, `templates/` o `knowledge/` si conviene.
6. Añadir criterios de calidad y errores comunes si faltan.
7. Proponer una versión mejorada.
8. Explicar los cambios principales.
9. Actualizar el archivo solo con permiso explícito.

## Cómo adaptar una skill externa

Cuando Santi comparta una skill de Claude, ChatGPT, LibreChat, OpenClaw u otra plataforma:

1. Analizar su objetivo y estructura.
2. Extraer las buenas prácticas funcionales.
3. No copiar contenido innecesario ni dependiente de una plataforma.
4. Reescribir la skill con lenguaje propio y adaptado a `AI-Skills`.
5. Sustituir referencias específicas de una plataforma por reglas portables.
6. Añadir reglas concretas para GitHub, ChatGPT y el flujo de trabajo de Santi.
7. Añadir atribución o nota de adaptación si procede por licencia.
8. Validar que la nueva skill funciona sin depender de la herramienta original.

## Criterios de una buena descripción

La descripción debe responder a tres preguntas:

1. ¿Qué hace la skill?
2. ¿Cuándo debe usarse?
3. ¿Qué palabras o contextos deberían activarla?

Plantilla recomendada:

```yaml
description: [Verbo de acción] [tipo de tarea] para [contexto]. Usa esta skill cuando el usuario pida [situaciones concretas], mencione [palabras clave] o necesite [resultado esperado].
```

## Reglas de seguridad y prudencia

No crear skills que:

- Faciliten acceso no autorizado.
- Exfiltren datos.
- Oculten acciones al usuario.
- Automaticen cambios peligrosos sin revisión.
- Manipulen sistemas reales sin confirmación.
- Contengan secretos, tokens, contraseñas o credenciales.
- Promuevan instrucciones engañosas o maliciosas.

Para tareas de empresa, separar siempre:

- Datos confirmados.
- Supuestos.
- Recomendaciones.
- Acciones que requieren validación humana.

## Formato de salida cuando se crea una skill

Cuando se entregue una skill nueva, responder con:

```text
Ruta recomendada:
...

Archivos creados o propuestos:
...

Resumen de la skill:
...

Contenido de SKILL.md:
...

Cambios recomendados en index.md:
...

Plantillas/knowledge adicionales:
...

Checklist de validación:
...
```

Si se modifica directamente GitHub, responder con:

```text
He creado/actualizado estos archivos:
- ...
- ...

La skill queda disponible en:
...

Uso recomendado:
...
```

## Plantillas relacionadas

- `templates/skill-template.md`
- `templates/skill-evaluation-template.md`

## Conocimiento relacionado

- `README.md`
- `index.md`
- `knowledge/skill-design-principles.md`
- `knowledge/quality-standards.md`
- `knowledge/company-writing-style.md`

## Nota de adaptación

Esta skill está diseñada para el repositorio `AI-Skills` de Santi y para un flujo portable basado en GitHub. Toma como referencia funcional patrones habituales de sistemas de skills, pero está reescrita y adaptada para trabajar con ChatGPT, conectores, repositorios GitHub/GitLab y procedimientos personales/profesionales de Santi.
