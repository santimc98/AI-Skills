# Catálogo de nodos n8n — Operaciones IA

> **Estado:** catálogo vivo con verificación parcial por workflows reales  
> **Última actualización:** 2026-05-11  
> **Uso principal:** apoyar la skill `skills/n8n-workflow-engineering/SKILL.md` para diseñar, auditar y mejorar workflows de n8n con criterio node-first.  
> **Importante:** este documento no es todavía un catálogo global completo de todos los nodos instalados en la instancia. La verificación real disponible procede de workflows inspeccionados mediante MCP/API, no de un endpoint global de node types.

---

## 1. Objetivo

Este catálogo existe para que el asistente pueda razonar sobre workflows de n8n con más contexto operativo y evitar diseñar soluciones limitadas por desconocimiento de nodos nativos.

La regla principal es:

```text
Antes de proponer Code o HTTP Request, comprobar si existe un nodo nativo, AI node, database node, integration node o patrón visual de n8n que resuelva la necesidad de forma más mantenible.
```

---

## 2. Estado de verificación actual

### 2.1 Qué se ha podido confirmar

El 2026-05-11 se inspeccionó la instancia mediante MCP/API con permisos de solo lectura.

Confirmado:

- el MCP/API responde;
- se pueden listar workflows;
- se pueden inspeccionar workflows;
- se pueden leer metadatos de ejecuciones recientes;
- se inspeccionaron 3 workflows, todos inactivos;
- se identificaron 14 tipos técnicos de nodos usados en workflows reales;
- no se ejecutó, activó, desactivó ni modificó ningún workflow;
- no se editaron credenciales.

Limitaciones:

- la versión de n8n no está expuesta por el MCP/API actual;
- no existe endpoint visible de catálogo global de nodos instalados;
- no existe endpoint visible de paquetes/community nodes instalados;
- el inventario confirmado es **por uso en workflows**, no por disponibilidad global;
- no observar un nodo en workflows no significa que no esté instalado.

### 2.2 Nodos verificados en workflows reales

| Nodo/capacidad | Type técnico | Paquete | Categoría | Estado | Observación |
|---|---|---|---|---|---|
| Webhook | `n8n-nodes-base.webhook` | core | Trigger / HTTP | `verified-instance` | Usado como entrada Chatwoot. |
| Edit Fields / Set | `n8n-nodes-base.set` | core | Transformación | `verified-instance` | Usado para extraer campos y definir configuración. |
| IF | `n8n-nodes-base.if` | core | Control de flujo | `verified-instance` | Usado para filtrar mensajes entrantes. |
| AI Agent | `@n8n/n8n-nodes-langchain.agent` | official | IA / agente | `verified-instance` | Usado en workflow RAG omnicanal. |
| OpenAI Chat Model | `@n8n/n8n-nodes-langchain.lmChatOpenAi` | official | IA / LLM | `verified-instance` | Conectado al agente IA. |
| Embeddings OpenAI | `@n8n/n8n-nodes-langchain.embeddingsOpenAi` | official | IA / embeddings | `verified-instance` | Conectado a Supabase Vector Store. |
| Supabase Vector Store | `@n8n/n8n-nodes-langchain.vectorStoreSupabase` | official | Vector Store / RAG | `verified-instance` | Confirmado como herramienta RAG. |
| Postgres Memory | `@n8n/n8n-nodes-langchain.memoryPostgresChat` | official | Memoria / PostgreSQL | `verified-instance` | Memoria conversacional persistente. |
| HTTP Request | `n8n-nodes-base.httpRequest` | core | HTTP/API | `verified-instance` | Usado para Chatwoot, GitLab MCP, OpenAI embeddings y Supabase REST. |
| Chat Trigger | `@n8n/n8n-nodes-langchain.chatTrigger` | official | Trigger / chat test | `verified-instance` | Usado como trigger de testing. |
| Simple Memory / Buffer Window Memory | `@n8n/n8n-nodes-langchain.memoryBufferWindow` | official | Memoria IA | `verified-instance` | Memoria temporal en workflow de agente. |
| Code | `n8n-nodes-base.code` | core | Transformación avanzada | `verified-instance` | Usado para normalización, chunking, hashing y deduplicación. |
| Manual Trigger | `n8n-nodes-base.manualTrigger` | core | Trigger manual | `verified-instance` | Presente en workflows draft/test. |
| Sticky Note | `n8n-nodes-base.stickyNote` | core | Documentación visual | `verified-instance` | Usado para documentar configuración y esquema. |

---

## 3. Niveles de verificación

Cada nodo o capacidad debe clasificarse con uno de estos estados:

| Estado | Significado | Uso permitido |
|---|---|---|
| `verified-instance` | Confirmado en workflows reales o catálogo real de la instancia de n8n usada por Operaciones. | Se puede recomendar con alta confianza dentro de las capacidades observadas. |
| `verified-docs` | Confirmado contra documentación oficial de la versión correspondiente. | Se puede recomendar, indicando versión si aplica. |
| `known-general` | Conocimiento general del ecosistema n8n, pendiente de verificar en la instancia real. | Se puede considerar, pero no asumir disponibilidad. |
| `candidate` | Nodo o capacidad plausible que debe buscarse en la instancia antes de diseñar. | Usar como pista de búsqueda, no como hecho. |
| `verified-design` | Capacidad o patrón validado por diseño interno, aunque no necesariamente como nodo nativo. | Se puede usar como patrón arquitectónico. |
| `deprecated-or-unknown` | Nodo dudoso, renombrado, desactualizado o no confirmado. | No usar salvo verificación explícita. |

---

## 4. Jerarquía de fuentes

Cuando haya conflicto entre fuentes, priorizar este orden:

1. Catálogo real exportado desde la instancia de n8n.
2. API/MCP de n8n que liste node types, credenciales, operaciones y schemas.
3. Workflows existentes ya validados en la instancia.
4. Documentación oficial de n8n para la versión instalada.
5. Este catálogo manual.
6. Memoria o conocimiento general del asistente.

Actualmente solo está disponible la fuente 3: workflows existentes inspeccionados.

---

## 5. Regla node-first

Antes de usar un nodo genérico:

| Necesidad | Revisar primero | Usar HTTP Request o Code solo si... |
|---|---|---|
| Llamar una API externa | Nodo nativo del servicio, AI node o database node | El endpoint/operación no está cubierto, se requieren headers especiales o autenticación no soportada. |
| Transformar campos simples | Edit Fields / Set, Filter, Aggregate | La transformación requiere lógica compleja, hashes, parsing robusto o validaciones multi-campo. |
| Enrutar por condición | IF, Switch, Filter | La condición es demasiado compleja para expresiones visuales mantenibles. |
| Procesar muchos items | Split in Batches / Loop Over Items, Merge, Aggregate | Se necesita control determinista avanzado o estado intermedio complejo. |
| Guardar en base de datos | Supabase Vector Store, Supabase, PostgreSQL o HTTP controlado según operación | El nodo no soporta upsert, RPC, vector search o headers necesarios. |
| Generar embeddings o usar LLM | OpenAI Chat Model, Embeddings OpenAI u otros AI nodes verificados | El modelo o endpoint no está soportado por el nodo instalado. |
| RAG/vector search | Supabase Vector Store, Vector Store nodes, PostgreSQL/pgvector o RPC | La operación vectorial requiere SQL/RPC específico o control no cubierto. |
| Memoria conversacional | Postgres Memory o Buffer Window Memory | Se requiere persistencia/control no cubierto por la memoria disponible. |

---

## 6. Familias de nodos relevantes

### 6.1 Triggers y entrada

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Manual Trigger | Ejecutar pruebas manuales. | `verified-instance` | Validación controlada antes de activar cron/webhook. |
| Webhook | Recibir llamadas externas. | `verified-instance` | Integraciones entrantes, callbacks, APIs internas. |
| Chat Trigger | Entrada conversacional de prueba. | `verified-instance` | Prototipos de agentes/chatbots dentro de n8n. |
| Schedule Trigger / Cron | Ejecución programada. | `known-general` | Sincronizaciones recurrentes, reports, ingestas periódicas. No observado todavía. |
| Respond to Webhook | Responder a llamadas entrantes. | `known-general` | Workflows que actúan como endpoint o tool externa. No observado todavía. |

### 6.2 Control de flujo

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| IF | Bifurcación booleana. | `verified-instance` | Condiciones simples: existe/no existe, status, flags. |
| Switch | Varias ramas según valor. | `known-general` | Clasificación por tipo, source_type, acción o categoría. No observado todavía. |
| Merge | Combinar ramas o datasets. | `known-general` | Reunir outputs después de lecturas paralelas. No observado todavía. |
| Split in Batches / Loop Over Items | Procesar colecciones por lotes. | `known-general` | Evitar límites de API, rate limits o memoria. No observado todavía. |

### 6.3 Transformación de datos

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Edit Fields / Set | Crear, editar o seleccionar campos. | `verified-instance` | Normalizaciones simples y visibles. |
| Code | JavaScript determinista. | `verified-instance` | Chunking, hashing, deduplicación, parsing robusto o lógica no mantenible visualmente. |
| Filter | Filtrar items por condiciones. | `known-general` | Limpiar registros antes de llamadas externas. No observado como nodo nativo. |
| Aggregate | Agrupar o consolidar items. | `known-general` | Convertir múltiples registros en resumen o array. No observado todavía. |

### 6.4 HTTP, APIs y conectores genéricos

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| HTTP Request | Consumir APIs REST/RPC. | `verified-instance` | Cuando no haya nodo nativo o se necesite control completo del request. |
| GitLab Knowledge MCP vía HTTP Request | Lectura controlada de knowledge versionado. | `verified-instance` | Confirmado en patrón de ingesta mediante MCP interno. |
| GraphQL | Consultas GraphQL. | `candidate` | APIs GraphQL con schema claro y operaciones mantenibles. No observado todavía. |

### 6.5 Bases de datos, memoria y almacenamiento

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Supabase Vector Store | Recuperación RAG sobre Supabase. | `verified-instance` | Cuando se necesite usar Supabase como herramienta de recuperación para agente IA. |
| Postgres Memory | Memoria conversacional persistente. | `verified-instance` | Cuando un agente necesite memoria persistente por sesión/conversación. |
| PostgreSQL genérico | SQL directo sobre PostgreSQL/Supabase. | `known-general` | No observado como nodo base; no asumir disponibilidad hasta verificar. |
| Supabase genérico | Operaciones tabla/API Supabase. | `candidate` | No observado como nodo genérico; sí hay Supabase Vector Store y HTTP Request a Supabase REST. |
| Google Sheets | Lectura/escritura de hojas. | `known-general` | No observado todavía. |
| Spreadsheet File | Leer/escribir CSV/XLSX. | `known-general` | No observado todavía. |

### 6.6 IA, LLMs, embeddings y RAG

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| AI Agent | Orquestación de agente con modelo, memoria y herramientas. | `verified-instance` | Agentes conversacionales o workflows tool-using dentro de n8n. |
| OpenAI Chat Model | Modelo chat OpenAI para agente. | `verified-instance` | Cuando el workflow use agente IA con modelo OpenAI. |
| Embeddings OpenAI | Generar vectores semánticos. | `verified-instance` | Pipelines RAG y consultas vectoriales con embeddings. |
| Supabase Vector Store | Búsqueda/recuperación vectorial en Supabase. | `verified-instance` | RAG conectado a Supabase/pgvector. |
| Buffer Window Memory | Memoria temporal de conversación. | `verified-instance` | Tests o agentes sin persistencia larga. |
| Postgres Memory | Memoria persistente de conversación. | `verified-instance` | Agentes con historial por sesión/conversación. |
| Structured Output Parser | Forzar salida JSON/estructura. | `candidate` | No observado todavía. Buscar antes de usar Code para parseos de LLM. |

### 6.7 Repositorios y control de versiones

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| GitLab nativo | Operaciones con GitLab. | `candidate` | No observado. Buscar antes de usar HTTP si se necesita operación simple. |
| GitHub nativo | Operaciones con GitHub. | `known-general` | No observado. Buscar antes de usar HTTP si se necesita GitHub. |
| GitLab Knowledge MCP vía HTTP Request | Lectura controlada de repos/knowledge. | `verified-instance` | Confirmado como patrón real para read-only, redacción y control interno. |

### 6.8 Comunicación y productividad

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Microsoft Teams | Mensajes o notificaciones. | `candidate` | No observado. Confirmar instalación/scopes antes de diseñar. |
| Microsoft Outlook | Correo corporativo M365. | `candidate` | No observado. Confirmar instalación/scopes antes de diseñar. |
| Gmail / Email | Enviar o leer correos. | `known-general` | No observado todavía. |
| Chatwoot vía HTTP Request | Enviar/responder mensajes por API Chatwoot. | `verified-instance` | Confirmado mediante HTTP Request. Cuidar impacto externo. |

### 6.9 Documentación visual

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Sticky Note | Documentar el canvas del workflow. | `verified-instance` | Explicar configuración, riesgos, credenciales requeridas y esquema esperado. |

---

## 7. Patrones confirmados en workflows reales

### 7.1 Agente RAG omnicanal con Chatwoot

Patrón observado:

```plaintext
Webhook Chatwoot
↓
Set / Edit Fields
↓
IF / Code
↓
AI Agent
├─ OpenAI Chat Model
├─ Supabase Vector Store
│  └─ Embeddings OpenAI
└─ Postgres Memory / Buffer Memory
↓
HTTP Request a API Chatwoot
```

Uso:

- recibir mensajes entrantes;
- filtrar mensajes válidos;
- responder con agente IA;
- recuperar conocimiento desde Supabase Vector Store;
- mantener memoria de conversación;
- enviar respuesta por API externa.

Riesgo:

- tiene impacto externo si se ejecuta;
- los workflows inspeccionados estaban inactivos;
- no ejecutar sin validaciones previas.

### 7.2 Pipeline GitLab Knowledge → n8n → Supabase pgvector

Patrón observado:

```plaintext
Manual Trigger
↓
Set / configuración
↓
HTTP Request a GitLab Knowledge MCP
↓
Code: normalización, chunking, hashing, deduplicación
↓
HTTP Request / OpenAI embeddings
↓
HTTP Request / Supabase REST pgvector upsert
```

Decisión node-first actualizada:

| Paso | Nodo/patrón verificado | Alternativa a revisar |
|---|---|---|
| Listar/leer GitLab Knowledge | HTTP Request a GitLab Knowledge MCP | GitLab nativo si se confirma instalado y seguro. |
| Normalizar campos | Set + Code | Edit Fields si la normalización es simple. |
| Chunking | Code | Mantener Code salvo que exista nodo específico verificado. |
| Hashing | Code | Mantener Code. |
| Deduplicación | Code | Revisar si puede simplificarse con DB/upsert. |
| Embeddings | HTTP Request observado; Embeddings OpenAI verificado en otro workflow | Preferir Embeddings OpenAI si soporta modelo/dimensiones requeridas. |
| Upsert Supabase | HTTP Request a Supabase REST observado | Revisar Supabase Vector Store/PostgreSQL/Supabase genérico según operación. |
| RAG runtime | Supabase Vector Store verificado | Usar cuando encaje con schema y recuperación como tool. |

---

## 8. Reglas de seguridad para workflows RAG

- No indexar `raw-research/`, `meta/`, `prompts/` o `intents/` por defecto.
- No guardar API keys, service role keys ni bearer tokens en Set, Sticky Notes, Code ni headers visibles.
- Migrar secretos a credenciales n8n o variables de entorno.
- Redactar outputs de pruebas si contienen secretos.
- Procesar primero un subconjunto pequeño antes de una ingesta completa.
- Guardar metadatos de trazabilidad: `agent_id`, `source_path`, `source_ref`, `chunk_index`, `content_hash`, `last_synced_at`.
- Preferir upsert idempotente a insert simple.
- No ejecutar workflows con HTTP Request externo sin validar destino, payload y credenciales.

---

## 9. Cómo ampliar este catálogo

Para convertir este documento en catálogo completo de instancia, hace falta una segunda extracción con alguna de estas vías:

1. Endpoint real de node types instalados si existe.
2. Export/listado desde la interfaz de n8n.
3. Acceso al filesystem/paquetes del contenedor si Tecnología lo permite.
4. Endpoint interno de n8n que devuelva node schemas, si el MCP lo expone en el futuro.
5. Export de workflows más amplio para inferir nodos usados, sabiendo que esto no prueba todos los instalados.

Formato recomendado para nuevas entradas:

```markdown
### Nombre del nodo

| Campo | Valor |
|---|---|
| Estado | verified-instance / verified-docs / known-general / candidate |
| Categoría | trigger / transform / database / ai / communication / devops / other |
| Type técnico | ... |
| Paquete | core / official / community / custom / unknown |
| Uso recomendado | ... |
| Cuándo preferirlo | ... |
| Cuándo no basta | ... |
| Credenciales | ... |
| Versión n8n verificada | ... |
| Fecha de revisión | ... |
```

---

## 10. Pendientes

- [ ] Obtener versión real de la instancia de n8n de Operaciones.
- [ ] Listar catálogo global de nodos instalados desde n8n o desde la UI.
- [ ] Confirmar si existen nodos nativos genéricos de Supabase, PostgreSQL, GitLab, GitHub, Teams, Outlook, Google Sheets y Spreadsheet File.
- [ ] Confirmar operaciones soportadas por Supabase Vector Store frente a Supabase REST/pgvector custom.
- [ ] Confirmar si hay Structured Output Parser, Document Loaders, Text Splitters u otros nodos LangChain útiles.
- [ ] Confirmar si hay community/custom nodes instalados globalmente.
- [ ] Eliminar secretos embebidos en parámetros de workflows y migrarlos a credenciales/variables de entorno.
- [ ] Añadir ejemplos internos de configuración segura por patrón.
