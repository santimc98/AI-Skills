# AI-Skills

Repositorio personal de skills, procedimientos, plantillas y conocimiento operativo para trabajar con asistentes de IA en tareas profesionales.

La finalidad de este repositorio es que las instrucciones de trabajo no dependan de una única plataforma. Las mismas skills pueden reutilizarse con Claude, ChatGPT, LibreChat, agentes con MCP, GitHub/GitLab o cualquier sistema que pueda leer archivos Markdown.

## Objetivo

Centralizar en un único lugar:

- Skills de trabajo para Excel, Jira, Confluence, SharePoint y reporting.
- Procedimientos paso a paso para tareas repetibles.
- Plantillas reutilizables para documentación corporativa.
- Reglas de estilo, tono, estructura y calidad.
- Conocimiento operativo que un asistente debe consultar antes de actuar.

## Cómo debe usar este repositorio un asistente de IA

Antes de ejecutar una tarea, el asistente debe:

1. Leer `index.md`.
2. Identificar qué skill corresponde a la tarea solicitada.
3. Leer el archivo `SKILL.md` de esa skill.
4. Consultar las plantillas o documentos de conocimiento relacionados.
5. Confirmar los supuestos relevantes si faltan datos críticos.
6. Ejecutar la tarea siguiendo el procedimiento definido.
7. Entregar un resultado claro, accionable y listo para usar.

## Estructura del repositorio

```text
AI-Skills/
├── README.md
├── index.md
├── skills/
│   ├── excel-analysis/
│   │   └── SKILL.md
│   ├── confluence-documentation/
│   │   └── SKILL.md
│   ├── jira-backlog-management/
│   │   └── SKILL.md
│   ├── sharepoint-document-management/
│   │   └── SKILL.md
│   ├── executive-reporting/
│   │   └── SKILL.md
│   ├── meeting-notes/
│   │   └── SKILL.md
│   ├── ai-research/
│   │   └── SKILL.md
│   └── prompt-engineering/
│       └── SKILL.md
├── templates/
│   ├── confluence-page-template.md
│   ├── jira-issue-template.md
│   ├── excel-analysis-report-template.md
│   ├── executive-summary-template.md
│   ├── meeting-notes-template.md
│   └── weekly-status-report-template.md
├── knowledge/
│   ├── company-writing-style.md
│   ├── glossary.md
│   ├── team-processes.md
│   └── quality-standards.md
└── examples/
    └── README.md
```

## Convención para cada skill

Cada skill debe mantener esta estructura mínima:

```markdown
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

## Reglas generales de uso

- No inventar información empresarial que no esté en los documentos proporcionados.
- Diferenciar claramente entre datos confirmados, inferencias y supuestos.
- Pedir aclaración solo cuando falte información crítica para no cometer errores.
- Priorizar entregables listos para copiar en Confluence, Jira, SharePoint, Excel o presentaciones.
- Mantener un tono profesional, claro y orientado a negocio.
- Cuando se trabaje con datos, explicar los pasos de forma comprensible y trazable.

## Flujo recomendado

```text
Solicitud del usuario
        ↓
Leer index.md
        ↓
Seleccionar skill adecuada
        ↓
Leer SKILL.md
        ↓
Consultar templates/ y knowledge/
        ↓
Ejecutar tarea
        ↓
Entregar resultado final
```

## Nota

Este repositorio está pensado como una base viva. Las skills pueden ir evolucionando conforme se detecten nuevos casos de uso, errores frecuentes o mejores formas de trabajar.
