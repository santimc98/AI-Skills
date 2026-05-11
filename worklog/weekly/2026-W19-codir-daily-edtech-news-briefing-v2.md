# Session Log — CODIR Daily EdTech News Briefing V2

**Fecha:** 2026-05-11  
**Semana:** 2026-W19  
**Área:** Operaciones / Business Operations & AI  
**Sistemas principales:** n8n, n8n Operations MCP, GitLab/Coolify, Jira OPERATIONS  
**Workflow:** `CODIR - Daily EdTech News Briefing`  
**Workflow ID:** `WJrcK6slpJlQnxpG`  
**Estado final:** V2 aplicada, workflow inactivo (`active=false`)

## Resumen ejecutivo

Se completó la evolución del workflow `CODIR - Daily EdTech News Briefing` hacia una **V2 node-first conservadora**. El objetivo del workflow es ser invocado desde LibreChat mediante webhook, consultar fuentes RSS/Google News de EdTech e IA educativa, seleccionar las noticias más relevantes para CODIR/Educa Edtech y devolver un briefing final en Markdown directo.

El cambio principal fue sustituir las llamadas HTTP directas a OpenAI por nodos nativos de n8n/LangChain:

- `AI Agent - Ranking IA` + `OpenAI Chat Model - Ranking`.
- `AI Agent - Resumen IA` + `OpenAI Chat Model - Resumen`.

El workflow quedó actualizado correctamente con 22 nodos, manteniendo `active=false`, sin ejecutar llamadas externas, sin tocar credenciales y sin activar producción.

## Contexto previo

Durante la sesión se detectó que el MCP de n8n necesitaba varios ajustes para poder operar de forma segura y útil desde ChatGPT:

1. ChatGPT inicialmente seguía viendo el catálogo antiguo de tools.
2. El schema de `create_draft_workflow` era rechazado por ChatGPT porque `tags` se exponía como array sin `items`.
3. `update_inactive_workflow` estaba deshabilitado por variable de entorno.
4. `update_inactive_workflow` enviaba campos read-only a n8n (`id`, `active` y metadata), provocando errores 400.
5. El fallback `workflow-observed` del catálogo de nodos usaba el nombre visual del nodo en vez del type técnico, impidiendo validar nodos existentes.

Se corrigieron estos puntos mediante cambios en el MCP, merge a `main`, pull/redeploy en Coolify y actualización de la aplicación ChatGPT.

## Trabajo realizado sobre el MCP n8n Operations

| Punto | Resultado |
|---|---|
| Nuevas tools MCP | ChatGPT ya ve `get_mcp_capabilities`, `list_node_types`, `search_node_types`, `get_node_type_schema` y `validate_workflow_node_types`. |
| `create_draft_workflow` schema | Corregido `tags` para exponer `items: { type: string }`. |
| `ALLOW_UPDATE_INACTIVE_WORKFLOWS` | Activado en Docker Compose/Coolify (`true`). |
| `ALLOW_ACTIVE_WORKFLOW_UPDATE` | Se mantiene en `false`. |
| `update_inactive_workflow` | Corregido para enviar a n8n un body allowlist: `name`, `nodes`, `connections`, `settings`, `tags` si aplica. |
| Payload update | `id` ya no se envía en el body; solo en la URL del endpoint. |
| Catálogo `workflow-observed` | Corregido para usar `name = node.type` y `displayName = node.name`. |
| Diagnóstico catálogo global | Ahora muestra por qué fallan `/rest/node-types` y `/api/v1/node-types`. |

## Validación MCP posterior al fix

`get_mcp_capabilities` confirmó:

- `can_update_inactive_workflow = true`.
- `can_validate_workflow_node_types = true`.
- `allowActiveWorkflowUpdate = false`.
- `can_read_credential_secrets` aparece redactado y debe tratarse como `false`.

`validate_workflow_node_types` validó correctamente nodos ya observados:

- `n8n-nodes-base.webhook`.
- `n8n-nodes-base.set`.
- `n8n-nodes-base.code`.
- `n8n-nodes-base.if`.
- `n8n-nodes-base.httpRequest`.
- `n8n-nodes-base.respondToWebhook`.
- `n8n-nodes-base.stickyNote`.

El catálogo global sigue parcial:

```text
source: workflow-observed
catalog_global: false
/rest/node-types failed: n8n internal REST 404: <!DOCTYPE html>
/api/v1/node-types failed: n8n API error 404: {"message":"not found"}
```

## Cambio aplicado en el workflow

Workflow actualizado:

```text
Nombre: CODIR - Daily EdTech News Briefing
ID: WJrcK6slpJlQnxpG
Estado: active=false
Nodos finales: 22
```

### Sustituciones aplicadas

| Antes | Después |
|---|---|
| `OpenAI - Ranking IA` con `n8n-nodes-base.httpRequest` | `AI Agent - Ranking IA` + `OpenAI Chat Model - Ranking` |
| `OpenAI - Resumen IA` con `n8n-nodes-base.httpRequest` | `AI Agent - Resumen IA` + `OpenAI Chat Model - Resumen` |
| `Prepare Ranking Request` | `Prepare Ranking Input` |
| `Prepare Summary Request` | `Prepare Summary Input` |

### Nodo no sustituido

| Nodo | Motivo |
|---|---|
| `Fetch RSS Feed` con `n8n-nodes-base.httpRequest` | `RSS Read` no aparece en el catálogo observado y el catálogo global de nodos no está disponible. Se mantiene fallback seguro con HTTP Request. |

## Nodos nativos usados en V2

- `Webhook` — `n8n-nodes-base.webhook`.
- `Set / Edit Fields` — `n8n-nodes-base.set`.
- `IF` — `n8n-nodes-base.if`.
- `AI Agent` — `@n8n/n8n-nodes-langchain.agent`.
- `OpenAI Chat Model` — `@n8n/n8n-nodes-langchain.lmChatOpenAi`.
- `Respond to Webhook` — `n8n-nodes-base.respondToWebhook`.
- `Sticky Note` — `n8n-nodes-base.stickyNote`.
- `Code` — `n8n-nodes-base.code`.
- `HTTP Request` — `n8n-nodes-base.httpRequest`, solo para RSS.

## Nodos Code / HTTP Request mantenidos

| Nodo | Tipo | Motivo |
|---|---|---|
| `Build Feed URL Items` | Code | Construcción dinámica de URLs RSS y Google News. |
| `Fetch RSS Feed` | HTTP Request | Fallback por no poder confirmar `RSS Read`. |
| `Parse, Normalize, Filter 24h/48h` | Code | Normalización RSS, parseo de fechas, scoring preliminar, fallback 24h/48h y deduplicación avanzada. |
| `Build Empty Response Markdown` | Code | Respuesta controlada si no hay noticias suficientes. |
| `Prepare Ranking Input` | Code | Compactar candidatos para el nodo IA. |
| `Parse Ranking JSON` | Code | Parsing defensivo del JSON devuelto por IA. |
| `Prepare Summary Input` | Code | Preparar entrada compacta del resumen. |
| `Extract Final Markdown` | Code | Garantizar salida final Markdown. |

## Confirmaciones de seguridad

- No se ejecutó el workflow.
- No se hicieron llamadas externas reales durante la actualización.
- No se activó el workflow.
- No se tocaron credenciales.
- No se borró nada.
- El workflow quedó `active=false`.
- `settings.availableInMCP=false`.
- No se introdujeron secretos en nodos ni Sticky Notes.
- El nodo final sigue devolviendo texto/Markdown directo mediante `Respond to Webhook`.

## Estado final del workflow

| Campo | Valor |
|---|---|
| Nombre | `CODIR - Daily EdTech News Briefing` |
| ID | `WJrcK6slpJlQnxpG` |
| Estado | Inactivo (`active=false`) |
| Nodos | 22 |
| Salida final | Markdown/texto directo para LibreChat |
| Activación producción | Pendiente |
| Credenciales OpenAI | Pendientes de seleccionar/configurar desde UI n8n |
| Fuentes RSS | Pendientes de validación manual |

## Pendientes derivados

1. Configurar/seleccionar credenciales OpenAI reales en:
   - `OpenAI Chat Model - Ranking`.
   - `OpenAI Chat Model - Resumen`.
2. Validar una por una las URLs RSS y Google News del nodo `Config - RSS, criterios y prompts`.
3. Probar el webhook en modo test:

```http
POST /webhook-test/codir-edtech-news-briefing
Content-Type: application/json

{}
```

4. Revisar primeras ejecuciones en n8n, especialmente:
   - `Fetch RSS Feed`.
   - `Parse, Normalize, Filter 24h/48h`.
   - `AI Agent - Ranking IA`.
   - `Parse Ranking JSON`.
   - `AI Agent - Resumen IA`.
   - `Extract Final Markdown`.
   - `Respond Markdown to LibreChat`.
5. No activar producción hasta validar credenciales, fuentes RSS y respuesta Markdown.
6. Valorar una mejora posterior del MCP para resolver catálogo global real de node types si n8n ofrece endpoint compatible.

## Jira relacionada

| Issue | Relación |
|---|---|
| AA-276 | Agentes CODIR. Contexto principal del agente/flujo CODIR. |
| AA-302 | Subtarea de MCPs específicos del agente Ángel, incluyendo n8n News. |
| AA-310 | Epic WORKFLOWS N8N. Capa de workflows programados o invocados por agentes. |

## Decisiones tomadas

| Decisión | Motivo |
|---|---|
| Mantener `Fetch RSS Feed` con HTTP Request | `RSS Read` no está confirmado en el catálogo observado y el catálogo global no está disponible. |
| Sustituir OpenAI HTTP por nodos AI nativos | Alineación con principio node-first y mejor mantenibilidad en n8n. |
| Mantener `Code` en lógica determinista | Es más seguro para normalización, fallback, deduplicación y protección del Markdown final. |
| Mantener workflow inactivo | Evitar ejecución productiva sin credenciales y validación de RSS. |
| No introducir secretos en workflow | Seguridad y buenas prácticas de operación. |

## Resultado final

La V2 node-first queda aplicada correctamente. El workflow está listo para configurar credenciales OpenAI y ejecutar una primera prueba controlada en modo test, sin activación productiva.
