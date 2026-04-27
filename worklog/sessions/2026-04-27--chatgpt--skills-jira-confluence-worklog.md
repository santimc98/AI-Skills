# Session Log — 2026-04-27 — ChatGPT — Skills, Jira, Confluence and Worklog

## Metadata

| Campo | Valor |
|---|---|
| Fecha | 2026-04-27 |
| Asistente | ChatGPT |
| Usuario | Santi |
| Contexto | Educa Edtech / Operaciones |
| Skills usadas | `educa-edtech-confluence`, `educa-edtech-jira`, `ai-worklog-sync` |
| Sistemas tocados | GitHub, Atlassian Rovo, Jira, Confluence |

## Objetivo de la sesión

Configurar un sistema compartido de skills y memoria operativa para que ChatGPT y Claude puedan trabajar de forma coordinada en tareas de Operaciones, Jira, Confluence, presentaciones y registro semanal.

## Trabajo realizado

- Verificada lectura del espacio Confluence `AA1 — OPERACIONES`.
- Verificada lectura de una página concreta de Confluence.
- Leída estructura principal del espacio OPERACIONES.
- Importada y mejorada la skill de Confluence.
- Verificada lectura del proyecto Jira `AA — OPERATIONS`.
- Creada una skill específica para Jira.
- Creada una skill de sincronización `ai-worklog-sync`.
- Creada la estructura inicial `worklog/`.
- Registradas candidatas iniciales a Jira y Confluence.

## Decisiones tomadas

- Usar GitHub como repositorio neutral para skills y worklog.
- No conectar SharePoint mientras los permisos solicitados sean demasiado amplios.
- Compartir documentación SharePoint manualmente por ahora.
- Usar Jira solo para tareas oficiales del equipo, no para cada prompt o conversación.
- Usar Confluence para conocimiento estable y procedimientos validados.

## Archivos / páginas / issues tocados

| Tipo | Referencia | Acción |
|---|---|---|
| GitHub | `skills/educa-edtech-confluence/SKILL.md` | Importado y mejorado |
| GitHub | `skills/educa-edtech-jira/SKILL.md` | Creado |
| GitHub | `skills/ai-worklog-sync/SKILL.md` | Creado |
| GitHub | `worklog/weekly/2026-W18.md` | Creado |
| GitHub | `worklog/tasks/pending-jira-actions.md` | Creado |
| GitHub | `worklog/tasks/pending-confluence-pages.md` | Creado |
| GitHub | `worklog/decisions/decisions-log.md` | Creado |
| Confluence | `AA1 — OPERACIONES` | Leído |
| Confluence | `Instrucciones de Jira — Operaciones` | Leído |
| Jira | `AA — OPERATIONS` | Leído |
| Jira | `AA-86 — TRACKER DOCUMENTACIÓN` | Referenciado |
| Jira | `AA-94 — BACKLOG PETICIONES` | Referenciado |

## Pendientes

- Pasar a Claude las skills actualizadas.
- Subir manualmente `template.pptx` para la skill PPTX si se quiere usar generación corporativa completa.
- Decidir si se crean tareas reales en Jira a partir de las propuestas.
- Decidir si se crean páginas reales en Confluence a partir de las propuestas.

## Posibles acciones Jira

| Acción | Tipo sugerido | Epic sugerida | Prioridad | Estado |
|---|---|---|---|---|
| Documentar procedimiento de uso de ChatGPT/Claude + AI-Skills para Operaciones | Tarea documental | AA-86 TRACKER DOCUMENTACIÓN | Media | Propuesta |
| Crear guía de registro semanal de actividad con IA | Tarea documental | AA-86 TRACKER DOCUMENTACIÓN | Media | Propuesta |
| Revisar permisos de conexión Microsoft 365 con IT | Tarea / Petición | AA-94 BACKLOG PETICIONES | Media | Propuesta |

## Posibles páginas Confluence

| Página | Ubicación sugerida | Motivo | Estado |
|---|---|---|---|
| Uso de asistentes IA en Operaciones | GENERAL / Cómo trabajamos | Formalizar forma de trabajo con ChatGPT, Claude y skills | Propuesta |
| Procedimiento de registro semanal de actividad IA | GENERAL / Documentacion Interna | Explicar cómo usar worklog, Jira y Confluence | Propuesta |
| Guía de seguridad para uso de SharePoint con IA | GENERAL / Cómo trabajamos | Evitar conexiones con permisos demasiado amplios | Propuesta |

## Riesgos o bloqueos

- SharePoint requiere validación de IT antes de conectarlo.
- El repositorio es público; evitar información confidencial.
- Las acciones reales en Jira y Confluence deben confirmarse antes de ejecutarse.

## Próximo prompt recomendado

```text
Lee mi repo AI-Skills. Usa index.md para elegir skills.
Después lee worklog/current-week.md, el worklog semanal activo y los pendientes.
Continúa el trabajo teniendo en cuenta lo ya realizado.
```
