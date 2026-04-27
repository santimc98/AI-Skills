# AI-Skills Index

Este archivo es el mapa principal del repositorio. Cualquier asistente de IA debe leerlo antes de elegir una skill.

## Regla principal

Cuando el usuario pida una tarea profesional, elegir la skill más específica disponible. Si la tarea toca varias áreas, combinar skills en este orden:

1. Skill principal de la tarea.
2. Skill secundaria si afecta al formato o destino final.
3. Plantilla relacionada.
4. Documentos de conocimiento aplicables.

Ejemplo:

```text
Analizar un Excel y preparar una página para Confluence
        ↓
1. skills/excel-analysis/SKILL.md
2. skills/educa-edtech-confluence/SKILL.md si es documentación del espacio OPERACIONES de Educa Edtech
3. templates/excel-analysis-report-template.md
4. knowledge/company-writing-style.md
```

---

## Skills específicas de Educa Edtech

### Educa Edtech Confluence

**Ruta:** `skills/educa-edtech-confluence/SKILL.md`

Usar cuando Santi pida crear, editar, actualizar o estructurar documentación en Confluence para Educa Edtech, especialmente en el espacio **OPERACIONES** (`AA1`).

Incluye:

- Reglas de nomenclatura de páginas.
- Bloque obligatorio de metadatos.
- Estructura del espacio OPERACIONES.
- Plantillas de procesos, automatizaciones, APTs y descripción de área.
- Reglas de owners funcionales/técnicos.
- Uso esperado de Atlassian Rovo para buscar, leer, crear o actualizar páginas.

**Conocimiento relacionado:**

- `knowledge/claude-connectors-configuration.md`
- `knowledge/company-writing-style.md`
- `knowledge/quality-standards.md`

---

### Educa Edtech PPTX

**Ruta:** `skills/educa-edtech-pptx/SKILL.md`

Usar cuando Santi pida una presentación corporativa, deck, pptx, slides o diapositivas para Educa Edtech Group, Atlax360, AI Tutor, EDUCA LXP u otros contextos internos de la empresa.

Incluye:

- Paleta corporativa.
- Reglas tipográficas.
- Motivos visuales recurrentes.
- Layouts clave de la plantilla.
- Flujo de trabajo para crear decks on-brand.
- Scripts auxiliares en `skills/educa-edtech-pptx/scripts/`.

**Importante:** la skill original incluye una plantilla binaria `assets/template.pptx`. La carpeta está preparada en `skills/educa-edtech-pptx/assets/`, pero el archivo `template.pptx` debe subirse manualmente si el conector no permite subir binarios.

**Conocimiento relacionado:**

- `knowledge/company-writing-style.md`
- `knowledge/quality-standards.md`

---

## Skills generales

### Excel Analysis

**Ruta:** `skills/excel-analysis/SKILL.md`

Usar cuando la tarea implique analizar archivos Excel, revisar hojas, fórmulas, columnas o métricas, crear tablas resumen, preparar dashboards, limpiar datos tabulares o calcular costes, consumos, KPIs y comparativas.

**Plantillas relacionadas:**

- `templates/excel-analysis-report-template.md`
- `templates/executive-summary-template.md`

---

### Confluence Documentation

**Ruta:** `skills/confluence-documentation/SKILL.md`

Usar para documentación genérica en Confluence cuando no aplique la skill específica de Educa Edtech. Si el trabajo es del espacio OPERACIONES de Educa Edtech, priorizar `skills/educa-edtech-confluence/SKILL.md`.

**Plantillas relacionadas:**

- `templates/confluence-page-template.md`
- `templates/executive-summary-template.md`

---

### Jira Backlog Management

**Ruta:** `skills/jira-backlog-management/SKILL.md`

Usar cuando la tarea implique crear, ordenar o mejorar issues de Jira, redactar épicas, historias, tareas, subtareas, criterios de aceptación, JQL o seguimiento del backlog.

**Plantillas relacionadas:**

- `templates/jira-issue-template.md`
- `templates/weekly-status-report-template.md`

---

### SharePoint Document Management

**Ruta:** `skills/sharepoint-document-management/SKILL.md`

Usar cuando la tarea implique organizar documentación en SharePoint, preparar documentos, proponer estructuras de carpetas, clasificar archivos o resumir documentación corporativa.

**Conocimiento relacionado:**

- `knowledge/claude-connectors-configuration.md`
- `knowledge/company-writing-style.md`

---

### Executive Reporting

**Ruta:** `skills/executive-reporting/SKILL.md`

Usar para informes ejecutivos, comparativas, recomendaciones para dirección, conclusiones y próximos pasos con enfoque de negocio.

---

### Meeting Notes

**Ruta:** `skills/meeting-notes/SKILL.md`

Usar para convertir reuniones en actas, extraer decisiones, riesgos, acuerdos, próximos pasos y tareas derivadas.

---

### AI Research

**Ruta:** `skills/ai-research/SKILL.md`

Usar para investigar modelos de IA, comparar benchmarks, analizar herramientas como ChatGPT, Claude, Gemini, OpenRouter, n8n, MCP o agentes, y traducir investigación técnica a decisiones prácticas.

---

### Prompt Engineering

**Ruta:** `skills/prompt-engineering/SKILL.md`

Usar para diseñar prompts, mejorar instrucciones de sistema, crear prompts para Claude, ChatGPT, LibreChat, OpenClaw, n8n o agentes propios, y auditar instrucciones reutilizables.

---

## Selección rápida por intención

| Si el usuario pide... | Usar principalmente |
|---|---|
| Crear/actualizar documentación de Educa Edtech en Confluence | `skills/educa-edtech-confluence/SKILL.md` |
| Crear una presentación corporativa Educa/Atlax360/AI Tutor | `skills/educa-edtech-pptx/SKILL.md` |
| Analizar un Excel | `skills/excel-analysis/SKILL.md` |
| Preparar una página de Confluence genérica | `skills/confluence-documentation/SKILL.md` |
| Crear tareas o historias de usuario | `skills/jira-backlog-management/SKILL.md` |
| Organizar documentos empresariales | `skills/sharepoint-document-management/SKILL.md` |
| Preparar informe para dirección | `skills/executive-reporting/SKILL.md` |
| Resumir una reunión | `skills/meeting-notes/SKILL.md` |
| Investigar herramientas o modelos de IA | `skills/ai-research/SKILL.md` |
| Crear o mejorar prompts | `skills/prompt-engineering/SKILL.md` |

---

## Reglas globales para todas las skills

1. No inventar datos.
2. Separar hechos, inferencias y recomendaciones.
3. Usar un tono profesional, claro y orientado a utilidad real.
4. Priorizar entregables listos para usar.
5. Explicar los pasos cuando la tarea sea técnica, matemática, analítica o de programación.
6. Mantener trazabilidad: indicar de dónde salen los datos, decisiones o conclusiones.
7. Si falta información crítica, pedirla; si no es crítica, avanzar con supuestos explícitos.
8. No sobrescribir documentación o tareas sin validación previa del usuario cuando pueda afectar a sistemas reales.
9. Para acciones en Jira, Confluence, SharePoint, Outlook o Teams, solicitar confirmación explícita cuando se vaya a modificar información real.

---

## Convención de actualización

Cuando se añada una nueva skill:

1. Crear carpeta en `skills/nombre-skill/`.
2. Añadir `SKILL.md`.
3. Actualizar este `index.md`.
4. Añadir plantillas si la skill produce entregables repetibles.
5. Añadir conocimiento relacionado si la skill depende de reglas internas.
