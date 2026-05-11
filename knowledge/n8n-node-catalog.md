# Catálogo de nodos n8n — Operaciones IA

> **Estado:** catálogo vivo inicial  
> **Última actualización:** 2026-05-11  
> **Uso principal:** apoyar la skill `skills/n8n-workflow-engineering/SKILL.md` para diseñar, auditar y mejorar workflows de n8n con criterio node-first.  
> **Importante:** este documento no pretende ser una copia completa de la documentación oficial de n8n. Su función es servir como inventario operativo interno, ampliable y verificable contra la instancia real.

---

## 1. Objetivo

Este catálogo existe para que el asistente pueda razonar sobre workflows de n8n con más contexto operativo y evitar diseñar soluciones limitadas por desconocimiento de nodos nativos.

La regla principal es:

```text
Antes de proponer Code o HTTP Request, comprobar si existe un nodo nativo, AI node, database node, integration node o patrón visual de n8n que resuelva la necesidad de forma más mantenible.
```

---

## 2. Niveles de verificación

Cada nodo o capacidad debe clasificarse con uno de estos estados:

| Estado | Significado | Uso permitido |
|---|---|---|
| `verified-instance` | Confirmado en la instancia real de n8n usada por Operaciones. | Se puede recomendar con alta confianza. |
| `verified-docs` | Confirmado contra documentación oficial de la versión correspondiente. | Se puede recomendar, indicando versión si aplica. |
| `known-general` | Conocimiento general del ecosistema n8n, pendiente de verificar en la instancia real. | Se puede considerar, pero no asumir disponibilidad. |
| `candidate` | Nodo o capacidad plausible que debe buscarse en la instancia antes de diseñar. | Usar como pista de búsqueda, no como hecho. |
| `deprecated-or-unknown` | Nodo dudoso, renombrado, desactualizado o no confirmado. | No usar salvo verificación explícita. |

---

## 3. Jerarquía de fuentes

Cuando haya conflicto entre fuentes, priorizar este orden:

1. Catálogo real exportado desde la instancia de n8n.
2. API/MCP de n8n que liste node types, credenciales, operaciones y schemas.
3. Workflows existentes ya validados en la instancia.
4. Documentación oficial de n8n para la versión instalada.
5. Este catálogo manual.
6. Memoria o conocimiento general del asistente.

---

## 4. Regla node-first

Antes de usar un nodo genérico:

| Necesidad | Revisar primero | Usar HTTP Request o Code solo si... |
|---|---|---|
| Llamar una API externa | Nodo nativo del servicio, AI node o database node | El endpoint/operación no está cubierto, se requieren headers especiales o autenticación no soportada. |
| Transformar campos simples | Edit Fields, Set, Rename Keys, Item Lists, Aggregate | La transformación requiere lógica compleja, hashes, parsing robusto o validaciones multi-campo. |
| Enrutar por condición | IF, Switch, Filter | La condición es demasiado compleja para expresiones visuales mantenibles. |
| Procesar muchos items | Split in Batches / Loop Over Items, Merge, Aggregate | Se necesita control determinista avanzado o estado intermedio complejo. |
| Guardar en base de datos | Nodo nativo de base de datos o servicio | El nodo no soporta upsert, RPC, vector search o headers necesarios. |
| Generar embeddings o usar LLM | AI nodes / OpenAI / proveedor correspondiente | El modelo o endpoint no está soportado por el nodo instalado. |
| RAG/vector search | Vector Store nodes, Supabase/Postgres/PGVector si están disponibles | La operación vectorial requiere SQL/RPC específico o control no cubierto. |

---

## 5. Familias de nodos relevantes

### 5.1 Triggers y entrada

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Manual Trigger | Ejecutar pruebas manuales. | `known-general` | Validación controlada antes de activar cron/webhook. |
| Schedule Trigger / Cron | Ejecución programada. | `known-general` | Sincronizaciones recurrentes, reports, ingestas periódicas. |
| Webhook | Recibir llamadas externas. | `known-general` | Integraciones entrantes, callbacks, APIs internas. |
| Chat Trigger | Entrada conversacional en workflows AI. | `candidate` | Prototipos de agentes/chatbots dentro de n8n. |
| Form Trigger | Captura de formularios internos. | `candidate` | Formularios simples sin frontend propio. |

### 5.2 Control de flujo

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| IF | Bifurcación booleana. | `known-general` | Condiciones simples: existe/no existe, status, flags. |
| Switch | Varias ramas según valor. | `known-general` | Clasificación por tipo, source_type, acción o categoría. |
| Merge | Combinar ramas o datasets. | `known-general` | Reunir outputs después de lecturas paralelas. |
| Split in Batches / Loop Over Items | Procesar colecciones por lotes. | `known-general` | Evitar límites de API, rate limits o memoria. |
| Wait | Pausas controladas. | `known-general` | Reintentos, ventanas temporales, procesos asíncronos. |
| Stop and Error | Fallar de forma explícita. | `known-general` | Evitar continuar con datos incompletos o peligrosos. |

### 5.3 Transformación de datos

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Edit Fields / Set | Crear, editar o seleccionar campos. | `known-general` | Normalizaciones simples y visibles. |
| Rename Keys | Renombrar claves. | `candidate` | Adaptar payloads entre sistemas. |
| Item Lists | Operaciones sobre listas/items. | `known-general` | Ordenar, dividir, filtrar o manipular colecciones simples. |
| Aggregate | Agrupar o consolidar items. | `known-general` | Convertir múltiples registros en resumen o array. |
| Filter | Filtrar items por condiciones. | `known-general` | Limpiar registros antes de llamadas externas. |
| Code | JavaScript determinista. | `known-general` | Chunking, hashing, deduplicación, parsing robusto o lógica no mantenible visualmente. |

### 5.4 HTTP, APIs y conectores genéricos

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| HTTP Request | Consumir APIs REST/RPC. | `known-general` | Cuando no haya nodo nativo o se necesite control completo del request. |
| GraphQL | Consultas GraphQL. | `candidate` | APIs GraphQL con schema claro y operaciones mantenibles. |
| Respond to Webhook | Responder a llamadas entrantes. | `known-general` | Workflows que actúan como endpoint o tool externa. |

### 5.5 Bases de datos y almacenamiento

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| PostgreSQL | Consultas SQL, inserts, updates, upserts si están soportados. | `known-general` | Supabase self-hosted, pgvector, operaciones SQL directas. |
| Supabase | Operaciones con Supabase. | `candidate` | Cuando el nodo instalado cubra tabla, insert, update, upsert o query necesaria. |
| Google Sheets | Lectura/escritura de hojas. | `known-general` | Prototipos, trackers y operaciones no críticas. |
| Airtable | Bases tabulares. | `known-general` | Operativa simple con tablas y vistas. |
| Redis | Cache, colas ligeras o estado temporal. | `candidate` | Evitar llamadas repetidas o controlar estado. |

### 5.6 IA, LLMs, embeddings y RAG

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| OpenAI | LLMs, embeddings o llamadas a OpenAI si el nodo lo permite. | `known-general` | Generación, clasificación, extracción o embeddings soportados por el nodo. |
| Embeddings OpenAI | Generar vectores semánticos. | `candidate` | Pipelines RAG cuando esté instalado y soporte el modelo requerido. |
| Vector Store | Búsqueda/almacenamiento vectorial. | `candidate` | RAG gestionado desde AI nodes. Verificar soporte real. |
| Supabase Vector Store | RAG sobre Supabase/pgvector. | `candidate` | Si existe en la instancia y soporta la tabla/función prevista. |
| AI Agent | Orquestación de agente con herramientas. | `candidate` | Agentes conversacionales o workflows tool-using dentro de n8n. |
| Structured Output Parser | Forzar salida JSON/estructura. | `candidate` | Evitar respuestas libres cuando se necesita schema. |

### 5.7 Repositorios y control de versiones

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| GitLab | Operaciones con GitLab. | `candidate` | Listar, leer o consultar repos si el nodo cubre la operación. |
| GitHub | Operaciones con GitHub. | `known-general` | Repos, issues, PRs, archivos o automatizaciones sobre GitHub. |
| GitLab Knowledge MCP vía HTTP/MCP | Lectura controlada de knowledge versionado. | `verified-design` | Cuando se quiera aplicar safelist, read-only, redacción de secretos o lógica propia. |

### 5.8 Comunicación y productividad

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Gmail / Email | Enviar o leer correos según credenciales. | `known-general` | Notificaciones, reporting, alertas. |
| Microsoft Outlook | Correo corporativo M365. | `candidate` | Si la instancia dispone de credenciales y scopes aprobados. |
| Microsoft Teams | Mensajes o notificaciones. | `candidate` | Alertas internas y reporting en canales. |
| Slack | Mensajería. | `known-general` | Notificaciones internas si aplica. |
| Twilio | SMS/WhatsApp según configuración. | `known-general` | Confirmaciones, avisos o canales conversacionales. |

### 5.9 Documentos, archivos y parsing

| Nodo/capacidad | Uso típico | Estado | Cuándo preferirlo |
|---|---|---:|---|
| Read/Write Files from Disk | Lectura/escritura local si runtime lo permite. | `candidate` | Workflows con volumen persistente o ficheros temporales. |
| Extract From File | Extraer contenido de binarios/archivos. | `candidate` | Procesar CSV, JSON, HTML u otros formatos soportados. |
| Spreadsheet File | Leer/escribir CSV/XLSX. | `known-general` | ETL tabular y reporting. |
| HTML Extract | Extraer datos de HTML. | `known-general` | Scraping ligero o parsing de páginas recibidas. |
| XML | Procesar XML. | `known-general` | APIs legacy, feeds o integraciones empresariales. |

---

## 6. Patrones recomendados para Operaciones IA

### 6.1 Pipeline GitLab Knowledge → n8n → Supabase pgvector

Patrón recomendado:

```plaintext
Manual/Schedule Trigger
↓
GitLab Knowledge MCP/API: listar archivos
↓
GitLab Knowledge MCP/API: leer archivos
↓
Filter/Switch: separar README, instructions, manifest, knowledge, faq
↓
Edit Fields: normalizar metadatos
↓
Code: chunking + hashing + deduplicación
↓
OpenAI / Embeddings node: generar embeddings
↓
Supabase/PostgreSQL/HTTP Request: upsert en tabla de chunks
↓
PostgreSQL/HTTP Request: validar búsqueda vectorial
```

Decisión node-first:

| Paso | Nodo preferente | Alternativa |
|---|---|---|
| Listar/leer GitLab Knowledge | GitLab node si cubre operación; si no, MCP vía HTTP Request | HTTP Request al MCP GitLab Knowledge |
| Normalizar campos | Edit Fields / Set | Code si la lógica es dinámica |
| Chunking | Code | No conviene resolverlo visualmente si hay solape, límites y hashes |
| Hashing | Code | Solo si hay función nativa verificada, que no se asume |
| Embeddings | OpenAI / Embeddings node | HTTP Request si el nodo no soporta endpoint/modelo |
| Upsert Supabase | Supabase node o PostgreSQL | HTTP Request si se usa REST/RPC específico |
| Vector search | Supabase Vector Store / PostgreSQL | HTTP Request RPC si se usa función `match_*` |

### 6.2 Reglas de seguridad para workflows RAG

- No indexar `raw-research/`, `meta/`, `prompts/` o `intents/` por defecto.
- No guardar API keys ni service role keys en notas o código.
- Redactar outputs de pruebas si contienen secretos.
- Procesar primero un subconjunto pequeño antes de una ingesta completa.
- Guardar metadatos de trazabilidad: `agent_id`, `source_path`, `source_ref`, `chunk_index`, `content_hash`, `last_synced_at`.
- Preferir upsert idempotente a insert simple.

---

## 7. Cómo ampliar este catálogo

Cuando se tenga acceso a la instancia real de n8n:

1. Exportar/listar node types instalados.
2. Registrar versión de n8n.
3. Marcar cada nodo como `verified-instance`.
4. Añadir operaciones soportadas por nodo.
5. Añadir credenciales requeridas.
6. Documentar limitaciones detectadas.
7. Actualizar también `knowledge/n8n-node-inventory.json`.

Formato recomendado para nuevas entradas:

```markdown
### Nombre del nodo

| Campo | Valor |
|---|---|
| Estado | verified-instance / verified-docs / known-general / candidate |
| Categoría | trigger / transform / database / ai / communication / devops / other |
| Uso recomendado | ... |
| Cuándo preferirlo | ... |
| Cuándo no basta | ... |
| Credenciales | ... |
| Versión n8n verificada | ... |
| Fecha de revisión | ... |
```

---

## 8. Pendientes

- [ ] Obtener versión real de la instancia de n8n de Operaciones.
- [ ] Listar nodos instalados desde API/MCP si está disponible.
- [ ] Confirmar si existen nodos nativos de Supabase, GitLab y embeddings en la instancia.
- [ ] Confirmar operaciones soportadas por el nodo Supabase frente a PostgreSQL/HTTP Request.
- [ ] Confirmar si hay AI nodes / LangChain nodes habilitados.
- [ ] Añadir ejemplos de workflows internos por patrón.
- [ ] Convertir entradas `candidate` en `verified-instance` o descartarlas.
