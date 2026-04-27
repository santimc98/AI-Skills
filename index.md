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
2. skills/confluence-documentation/SKILL.md
3. templates/excel-analysis-report-template.md
4. templates/confluence-page-template.md
5. knowledge/company-writing-style.md
```

---

## Índice de skills

### 1. Excel Analysis

**Ruta:** `skills/excel-analysis/SKILL.md`

Usar cuando la tarea implique:

- Analizar archivos Excel.
- Revisar hojas, tablas, fórmulas, columnas o métricas.
- Crear tablas resumen.
- Preparar dashboards o datos para reporting.
- Limpiar, transformar o explicar datos tabulares.
- Calcular costes, consumos, uso de tokens, KPIs o comparativas.

**Plantillas relacionadas:**

- `templates/excel-analysis-report-template.md`
- `templates/executive-summary-template.md`

**Conocimiento relacionado:**

- `knowledge/quality-standards.md`
- `knowledge/glossary.md`

---

### 2. Confluence Documentation

**Ruta:** `skills/confluence-documentation/SKILL.md`

Usar cuando la tarea implique:

- Crear documentación para Confluence.
- Redactar páginas técnicas o funcionales.
- Mejorar estructura, claridad o tono de una página.
- Convertir notas desordenadas en documentación empresarial.
- Crear manuales, guías, procedimientos o páginas de decisión.

**Plantillas relacionadas:**

- `templates/confluence-page-template.md`
- `templates/executive-summary-template.md`

**Conocimiento relacionado:**

- `knowledge/company-writing-style.md`
- `knowledge/team-processes.md`
- `knowledge/quality-standards.md`

---

### 3. Jira Backlog Management

**Ruta:** `skills/jira-backlog-management/SKILL.md`

Usar cuando la tarea implique:

- Crear, ordenar o mejorar issues de Jira.
- Redactar épicas, historias de usuario, tareas o subtareas.
- Definir criterios de aceptación.
- Relacionar documentación de Confluence con trabajo en Jira.
- Convertir decisiones o reuniones en tareas accionables.
- Mantener backlog, roadmap o seguimiento de trabajo.

**Plantillas relacionadas:**

- `templates/jira-issue-template.md`
- `templates/weekly-status-report-template.md`

**Conocimiento relacionado:**

- `knowledge/team-processes.md`
- `knowledge/quality-standards.md`

---

### 4. SharePoint Document Management

**Ruta:** `skills/sharepoint-document-management/SKILL.md`

Usar cuando la tarea implique:

- Organizar documentación en SharePoint.
- Preparar documentos para guardar o compartir.
- Proponer estructuras de carpetas.
- Clasificar archivos empresariales.
- Resumir o transformar documentos para equipos.
- Crear documentación reutilizable a partir de archivos corporativos.

**Plantillas relacionadas:**

- `templates/confluence-page-template.md`
- `templates/executive-summary-template.md`

**Conocimiento relacionado:**

- `knowledge/company-writing-style.md`
- `knowledge/team-processes.md`

---

### 5. Executive Reporting

**Ruta:** `skills/executive-reporting/SKILL.md`

Usar cuando la tarea implique:

- Crear informes ejecutivos.
- Resumir información para dirección o responsables de área.
- Preparar comparativas de modelos, costes, proveedores o herramientas.
- Explicar resultados técnicos con enfoque de negocio.
- Crear conclusiones, recomendaciones y próximos pasos.

**Plantillas relacionadas:**

- `templates/executive-summary-template.md`
- `templates/weekly-status-report-template.md`

**Conocimiento relacionado:**

- `knowledge/company-writing-style.md`
- `knowledge/quality-standards.md`

---

### 6. Meeting Notes

**Ruta:** `skills/meeting-notes/SKILL.md`

Usar cuando la tarea implique:

- Convertir una reunión en acta.
- Extraer decisiones, riesgos, acuerdos y próximos pasos.
- Crear tareas desde notas de reunión.
- Preparar resumen para Confluence, Jira o correo.

**Plantillas relacionadas:**

- `templates/meeting-notes-template.md`
- `templates/jira-issue-template.md`

**Conocimiento relacionado:**

- `knowledge/team-processes.md`

---

### 7. AI Research

**Ruta:** `skills/ai-research/SKILL.md`

Usar cuando la tarea implique:

- Investigar modelos de IA.
- Comparar benchmarks.
- Analizar herramientas como ChatGPT, Claude, Gemini, OpenRouter, n8n, MCP o agentes.
- Preparar documentación o recomendaciones sobre IA para empresa.
- Traducir investigación técnica a decisiones prácticas.

**Plantillas relacionadas:**

- `templates/executive-summary-template.md`
- `templates/confluence-page-template.md`

**Conocimiento relacionado:**

- `knowledge/glossary.md`
- `knowledge/quality-standards.md`

---

### 8. Prompt Engineering

**Ruta:** `skills/prompt-engineering/SKILL.md`

Usar cuando la tarea implique:

- Diseñar prompts para agentes.
- Mejorar instrucciones de sistema.
- Crear prompts para Claude, ChatGPT, LibreChat, OpenClaw, n8n o agentes propios.
- Convertir procesos de trabajo en instrucciones reutilizables.
- Auditar prompts para evitar ambigüedades.

**Plantillas relacionadas:**

- `templates/confluence-page-template.md`

**Conocimiento relacionado:**

- `knowledge/quality-standards.md`

---

## Selección rápida por intención

| Si el usuario pide... | Usar principalmente |
|---|---|
| Analizar un Excel | `skills/excel-analysis/SKILL.md` |
| Preparar una página para Confluence | `skills/confluence-documentation/SKILL.md` |
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

---

## Convención de actualización

Cuando se añada una nueva skill:

1. Crear carpeta en `skills/nombre-skill/`.
2. Añadir `SKILL.md`.
3. Actualizar este `index.md`.
4. Añadir plantillas si la skill produce entregables repetibles.
5. Añadir conocimiento relacionado si la skill depende de reglas internas.
