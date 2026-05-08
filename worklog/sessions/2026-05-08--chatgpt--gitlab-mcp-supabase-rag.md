# Session Log — 2026-05-08 — ChatGPT — GitLab MCP y Supabase RAG

## Metadata

| Campo | Valor |
|---|---|
| Fecha | 2026-05-08 |
| Asistente | ChatGPT |
| Usuario | Santi |
| Contexto | Educa Edtech / Operaciones / Business Operations & AI |
| Skills usadas | `n8n-workflow-engineering`, `educa-edtech-jira`, `educa-edtech-confluence`, `ai-worklog-sync` |
| Sistemas tocados | GitLab corporativo, n8n, Supabase, Coolify, Jira, GitHub |

## Objetivo de la sesión

Continuar la infraestructura de knowledge para agentes internos, validando el MCP de GitLab como fuente documental, preparando un flujo n8n de ingesta hacia Supabase y dejando trazabilidad en GitHub/Jira sin registrar credenciales ni secretos.

## Trabajo realizado

- Se validó el uso del GitLab Knowledge MCP desplegado en servidor/Coolify como fuente de archivos del repositorio corporativo de agentes.
- Se preparó el consumo desde n8n mediante endpoints HTTP/wrappers REST, para que el flujo pueda listar archivos, leer contenido y procesarlo sin depender directamente de un cliente MCP avanzado.
- Se confirmó que el flujo de n8n puede trabajar sobre la ruta del agente de ponencia en GitLab y recuperar el contenido documental.
- Se construyó la cadena funcional del workflow de ingesta:
  - configuración central con placeholders;
  - listado de archivos de knowledge vía GitLab MCP;
  - lectura de archivos;
  - normalización del contenido;
  - generación de chunks y hashes;
  - deduplicación por hash;
  - preparación de llamada de embeddings;
  - preparación de upsert hacia Supabase.
- Se configuró el nodo HTTP de embeddings con `Authorization: Bearer {{ ... }}` y body JSON usando el modelo configurado en `Config`.
- Se revisó Supabase self-hosted en Coolify y se comprobó que la parte de base de datos para knowledge vectorial está preparada a nivel de tabla/función, según la validación realizada en el SQL editor.
- Se identificaron las credenciales pendientes para que el flujo quede ejecutable de punta a punta.

## Decisiones tomadas

- El flujo queda preparado con placeholders y sin credenciales reales hasta que Chema/equipo confirme claves y modelo de embeddings.
- Supabase self-hosted se usará como vector store inicial para knowledge de agentes, con pgvector y una tabla específica de chunks.
- Antes de documentar formalmente el pipeline GitLab → Supabase en Confluence, se documentará primero la infraestructura y gobernanza de GitLab corporativo para agentes.
- La documentación de Confluence que se actualizará primero será la página de infraestructura de MCPs y/o documentación base de GitLab, según enlaces que facilite Santi.

## Archivos / páginas / issues tocados

| Tipo | Referencia | Acción |
|---|---|---|
| GitLab | Repo corporativo de agentes | Consultado mediante GitLab Knowledge MCP |
| n8n | Workflow de ingesta knowledge | Configurado hasta quedar pendiente de credenciales |
| Supabase | Tabla/función de knowledge vectorial | Revisada/preparada para upsert y búsqueda vectorial |
| Jira | `AA-312`, `AA-376`, `AA-378`, `AA-358` | Pendiente de comentarios de actualización |
| GitHub | `worklog/sessions/2026-05-08--chatgpt--gitlab-mcp-supabase-rag.md` | Creación de registro de sesión |

## Pendientes

- Sustituir placeholders de configuración por credenciales reales en n8n cuando el equipo las confirme.
- Confirmar API key/modelo de embeddings con Chema o responsable técnico.
- Confirmar `supabase_url`, tabla objetivo y key de servicio o credencial segura equivalente.
- Ejecutar prueba end-to-end del workflow: GitLab → chunks → embeddings → Supabase upsert.
- Probar búsqueda vectorial sobre Supabase con preguntas reales del agente de ponencia.
- Documentar en Confluence primero la infraestructura/gobernanza de GitLab para agentes.
- Después, documentar el pipeline GitLab → Supabase RAG cuando esté probado de punta a punta.

## Posibles acciones Jira

| Acción | Tipo sugerido | Epic sugerida | Prioridad | Estado |
|---|---|---|---|---|
| Completar credenciales y prueba end-to-end de ingesta RAG del agente de ponencia | Subtarea / Tarea técnica | `AA-329` / `AA-358` | Alta | Propuesta |
| Documentar infraestructura GitLab para agentes corporativos | Tarea documental | `AA-312` o `AA-250` | Media | Propuesta |
| Actualizar página de infraestructura MCP con estado real del GitLab Knowledge MCP desplegado | Tarea documental | `AA-312` / `AA-374` | Media | Propuesta |

## Posibles páginas Confluence

| Página | Ubicación sugerida | Motivo | Estado |
|---|---|---|---|
| GitLab corporativo para agentes IA — estructura y gobernanza | OPERACIONES / IA / Infraestructura | Documentar repositorio, taxonomía, rutas, ramas y reglas de uso | Propuesta |
| Infraestructura MCPs internos — actualización estado GitLab Knowledge MCP | OPERACIONES / IA / Infraestructura | Reflejar despliegue, endpoints, autenticación y estado real | Propuesta |

## Riesgos o bloqueos

- No registrar ni pegar claves API, service role keys ni tokens en GitHub, Jira o Confluence.
- El flujo no debe ejecutarse en producción hasta confirmar credenciales seguras y endpoint correcto de Supabase.
- La key de Supabase con permisos elevados debe vivir en credencial/entorno seguro, no en texto plano del workflow.
- La documentación del pipeline RAG debe esperar a una prueba end-to-end para no formalizar un diseño todavía no validado.

## Próximo prompt recomendado

```text
Continuamos desde el worklog de 2026-05-08. Primero actualiza Jira con comentarios de avance en AA-312, AA-376, AA-378 y AA-358. Después, cuando te pase los enlaces, documentamos en Confluence la infraestructura de MCPs y la base de GitLab corporativo para agentes. No documentes todavía el pipeline GitLab → Supabase hasta que esté probado end-to-end.
```
