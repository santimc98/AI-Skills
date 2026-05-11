# Catálogo documental de nodos n8n — docs-derived

> **Estado:** catálogo derivado de documentación pública de n8n, no verificado globalmente en la instancia corporativa.  
> **Última actualización:** 2026-05-11  
> **Uso:** complementar `knowledge/n8n-node-catalog.md` y `knowledge/n8n-node-inventory.json` para aplicar el principio node-first.  
> **Regla crítica:** un nodo listado aquí existe o aparece documentado en el ecosistema n8n, pero solo debe tratarse como instalado en Operaciones si aparece en `verified-instance` / `verified-used-in-workflow` o si la UI/MCP lo confirma.

---

## 1. Fuentes documentales base

Fuentes usadas como referencia documental:

- Documentación oficial de n8n — Built-in integrations / Node types: `https://docs.n8n.io/integrations/builtin/node-types/`
- Documentación oficial de n8n — Core nodes: `https://docs.n8n.io/integrations/builtin/core-nodes/`
- Documentación oficial de n8n — LangChain concepts in n8n: `https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/`
- Página de integraciones n8n: `https://docs.n8n.io/integrations/`
- Paquete npm `n8n-nodes-base`: `https://www.npmjs.com/package/n8n-nodes-base`

Sobre versión: la versión de instancia corporativa no está expuesta por el MCP actual. La referencia `2.13.4` debe tratarse como versión objetivo indicada por el usuario o por entorno, no como versión confirmada por la instancia.

---

## 2. Estados usados en este catálogo

| Estado | Significado |
|---|---|
| `verified-used-in-workflow` | Confirmado en workflows reales inspeccionados por MCP/API. |
| `verified-docs` | Confirmado en documentación pública/oficial de n8n o ecosistema n8n. |
| `docs-derived` | Derivado de documentación n8n; requiere confirmación en instancia antes de asumir disponibilidad. |
| `unknown-instance` | No confirmado en la instancia corporativa actual. |
| `candidate-for-ui-check` | Nodo que conviene buscar manualmente en la UI de n8n si se va a usar. |

---

## 3. Principio de uso correcto

Cuando se diseñe o revise un workflow:

```text
1. Revisar primero nodos verified-used-in-workflow.
2. Si no cubren la necesidad, revisar este catálogo docs-derived.
3. Si un nodo docs-derived parece adecuado, buscarlo en la UI de n8n o pedir confirmación antes de diseñar alrededor de él.
4. Si no está disponible o no cubre la operación, usar HTTP Request o Code justificándolo.
```

---

## 4. Core nodes y patrones visuales documentados

### 4.1 Triggers y entrada

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo preferirlo frente a genéricos |
|---|---|---|---|---|
| Manual Trigger | `verified-docs` | `verified-used-in-workflow` | Pruebas manuales y validación controlada. | Antes de activar Schedule/Webhook en fases de diseño. |
| Schedule Trigger | `verified-docs` | `unknown-instance` | Ejecuciones programadas. | Frente a cron externo si n8n puede gobernar la periodicidad. |
| Webhook | `verified-docs` | `verified-used-in-workflow` | Entrada HTTP/eventos externos. | Frente a polling cuando la fuente puede llamar a n8n. |
| Respond to Webhook | `verified-docs` | `unknown-instance` | Responder a peticiones HTTP entrantes. | Para workflows que actúan como endpoint o API interna. |
| Chat Trigger | `verified-docs` | `verified-used-in-workflow` | Testing conversacional de workflows IA. | Frente a Webhook para pruebas internas de agentes. |
| Form Trigger | `verified-docs` | `unknown-instance` | Formularios simples de entrada. | Frente a crear frontend externo para capturas básicas. |
| Execute Workflow Trigger | `verified-docs` | `unknown-instance` | Disparar workflows desde otros workflows. | Para modularizar flujos grandes. |

### 4.2 Control de flujo

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo preferirlo frente a Code |
|---|---|---|---|---|
| IF | `verified-docs` | `verified-used-in-workflow` | Bifurcación booleana. | Condiciones simples y auditables. |
| Switch | `verified-docs` | `unknown-instance` | Ruteo multi-rama. | Clasificación por tipo, estado, intención, source_type. |
| Merge | `verified-docs` | `unknown-instance` | Combinar ramas o datasets. | Reunir outputs de ramas paralelas sin código. |
| Loop Over Items / Split in Batches | `verified-docs` | `unknown-instance` | Procesamiento por lotes. | Evitar rate limits, timeouts o exceso de memoria. |
| Wait | `verified-docs` | `unknown-instance` | Pausas, esperas o reintentos controlados. | Procesos asíncronos o dependientes de ventana temporal. |
| Stop and Error | `verified-docs` | `unknown-instance` | Cortar el flujo con error explícito. | Fallar seguro ante datos incompletos. |
| Execute Workflow | `verified-docs` | `unknown-instance` | Llamar subworkflows reutilizables. | Modularizar lógica común y evitar duplicidad. |
| No Operation / NoOp | `verified-docs` | `unknown-instance` | Nodo puente o marcador visual. | Claridad de ramas y pruebas. |

### 4.3 Transformación de datos

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo preferirlo frente a Code |
|---|---|---|---|---|
| Edit Fields / Set | `verified-docs` | `verified-used-in-workflow` | Crear, mapear o limpiar campos. | Transformaciones simples visibles. |
| Filter | `verified-docs` | `unknown-instance` | Filtrar items por condiciones. | Limpieza de datos antes de API/DB. |
| Aggregate | `verified-docs` | `unknown-instance` | Agrupar items o consolidar arrays. | Resúmenes y agrupaciones simples. |
| Sort | `verified-docs` | `unknown-instance` | Ordenar items. | Ordenaciones simples sin lógica custom. |
| Remove Duplicates | `verified-docs` | `unknown-instance` | Quitar duplicados por campos. | Dedupe simple antes de upsert/API. |
| Limit | `verified-docs` | `unknown-instance` | Limitar número de items. | Pruebas seguras y reducción de carga. |
| Date & Time | `verified-docs` | `unknown-instance` | Normalizar fechas. | Evitar parsing manual en Code. |
| Rename Keys | `verified-docs` | `unknown-instance` | Renombrar campos. | Adaptar payloads entre sistemas. |
| Item Lists | `verified-docs` | `unknown-instance` | Operaciones sobre listas/items. | Manipulación simple de colecciones. |
| Code | `verified-docs` | `verified-used-in-workflow` | JavaScript determinista. | Chunking, hashing, parsing robusto, lógica compleja. |

### 4.4 HTTP, APIs y protocolos

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo usarlo |
|---|---|---|---|---|
| HTTP Request | `verified-docs` | `verified-used-in-workflow` | APIs REST/RPC/MCP. | Solo cuando no haya nodo nativo suficiente o se requiera control exacto. |
| GraphQL | `verified-docs` | `unknown-instance` | APIs GraphQL. | Cuando el servicio expone schema GraphQL y no hay nodo específico mejor. |
| Webhook + Respond to Webhook | `verified-docs` | parcial | Crear endpoint interno. | Tools internas, callbacks o APIs ligeras. |

### 4.5 Archivos y parsing

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo preferirlo frente a Code |
|---|---|---|---|---|
| Spreadsheet File | `verified-docs` | `unknown-instance` | Leer/escribir CSV/XLSX. | ETL tabular estándar. |
| Extract From File | `verified-docs` | `unknown-instance` | Extraer datos de binarios/archivos. | Cuando n8n soporta el formato sin código. |
| Read/Write Files from Disk | `verified-docs` | `unknown-instance` | Leer/escribir ficheros en runtime. | Solo si el entorno permite acceso a disco. |
| HTML Extract | `verified-docs` | `unknown-instance` | Extraer datos de HTML. | Scraping/parsing ligero. |
| XML | `verified-docs` | `unknown-instance` | Procesar XML. | APIs legacy, feeds, integraciones antiguas. |
| Compression | `verified-docs` | `unknown-instance` | Comprimir/descomprimir archivos. | Flujo documental o integraciones de archivos. |

---

## 5. Integraciones documentadas relevantes para Operaciones IA

### 5.1 Repositorios y desarrollo

| Nodo / integración | Estado documental | Estado instancia | Uso recomendado | Nota node-first |
|---|---|---|---|---|
| GitLab | `verified-docs` | `unknown-instance` | Repositorios, issues, archivos si operación soportada. | Buscar antes de usar HTTP directo para operaciones simples. |
| GitHub | `verified-docs` | `unknown-instance` | Repos, issues, PRs, archivos. | Preferir nativo si existe en instancia y cubre operación. |
| Jira Software | `verified-docs` | `unknown-instance` | Issues y proyectos Jira. | Para Educa, comparar con Atlassian Rovo/MCP antes de duplicar. |
| HTTP Request a GitLab Knowledge MCP | `verified-design` | `verified-used-in-workflow` | Lectura controlada read-only. | Preferible cuando se requiera redacción, safelist y gobierno propio. |

### 5.2 Bases de datos y almacenamiento

| Nodo / integración | Estado documental | Estado instancia | Uso recomendado | Nota node-first |
|---|---|---|---|---|
| PostgreSQL | `verified-docs` | `unknown-instance` | SQL directo, upsert, consultas. | Confirmar en UI; no confundir con Postgres Memory. |
| Supabase | `verified-docs` | `unknown-instance` | Operaciones Supabase si el nodo cubre tablas/API. | Confirmar en UI; Supabase Vector Store sí está observado. |
| MySQL | `verified-docs` | `unknown-instance` | SQL MySQL. | Solo si hay caso de uso real. |
| Redis | `verified-docs` | `unknown-instance` | Cache/estado temporal. | Útil para dedupe temporal o rate limits si está disponible. |
| MongoDB | `verified-docs` | `unknown-instance` | Document store. | Confirmar disponibilidad. |
| Google Sheets | `verified-docs` | `unknown-instance` | Trackers y hojas operativas. | Preferir para prototipos/reporting ligero. |
| Airtable | `verified-docs` | `unknown-instance` | Bases tabulares. | Solo si existe caso de negocio. |

### 5.3 Comunicación y productividad

| Nodo / integración | Estado documental | Estado instancia | Uso recomendado | Nota node-first |
|---|---|---|---|---|
| Microsoft Teams | `verified-docs` | `unknown-instance` | Notificaciones y alertas. | Confirmar scopes antes de diseñar. |
| Microsoft Outlook | `verified-docs` | `unknown-instance` | Correo corporativo. | Confirmar Graph/scopes y compliance. |
| Gmail | `verified-docs` | `unknown-instance` | Correo Google. | Solo si aplica a cuentas autorizadas. |
| Google Drive | `verified-docs` | `unknown-instance` | Archivos Drive. | Confirmar permisos. |
| Slack | `verified-docs` | `unknown-instance` | Mensajería. | Solo si es canal usado por la empresa. |
| Chatwoot vía HTTP Request | `verified-design` | `verified-used-in-workflow` | Entrada/salida canal conversación. | Existe patrón real; validar impacto externo. |

---

## 6. AI / LangChain nodes documentados relevantes

### 6.1 Agentes y cadenas

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo usarlo |
|---|---|---|---|---|
| AI Agent / Agent | `verified-docs` | `verified-used-in-workflow` | Agente con modelo, herramientas y memoria. | Workflows conversacionales o tool-using. |
| Basic LLM Chain | `verified-docs` | `unknown-instance` | Cadena LLM simple. | Generar, resumir, transformar texto sin agente completo. |
| Retrieval Q&A Chain | `verified-docs` | `unknown-instance` | Pregunta-respuesta con retrieval. | RAG simple sin agente tool-using. |
| Question and Answer Chain | `verified-docs` | `unknown-instance` | Q&A sobre contexto. | Respuestas sobre documentos/contenido. |
| Text Classifier | `verified-docs` | `unknown-instance` | Clasificar texto. | Triaje, routing, categorización. |
| Information Extractor | `verified-docs` | `unknown-instance` | Extraer campos estructurados. | Evitar prompts libres + Code para extracción JSON. |
| Sentiment Analysis | `verified-docs` | `unknown-instance` | Clasificar sentimiento. | Casos de soporte/NPS/feedback. |

### 6.2 Modelos y embeddings

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo usarlo |
|---|---|---|---|---|
| OpenAI Chat Model | `verified-docs` | `verified-used-in-workflow` | Modelo chat para agentes/cadenas. | Preferir frente a HTTP si cubre modelo/config. |
| Embeddings OpenAI | `verified-docs` | `verified-used-in-workflow` | Embeddings para RAG/vector search. | Preferir frente a HTTP si soporta modelo/dimensiones. |
| OpenAI generic node | `verified-docs` | `unknown-instance` | Operaciones OpenAI genéricas si está disponible. | Confirmar en UI. |
| Other Chat Models | `verified-docs` | `unknown-instance` | Anthropic, Google, Ollama u otros según docs/instancia. | Confirmar proveedor y credenciales. |

### 6.3 Vector stores y retrievers

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo usarlo |
|---|---|---|---|---|
| Supabase Vector Store | `verified-docs` | `verified-used-in-workflow` | RAG con Supabase/pgvector. | Confirmado como herramienta RAG. |
| PGVector Vector Store | `verified-docs` | `unknown-instance` | RAG directo sobre PostgreSQL/pgvector. | Alternativa si se quiere control PostgreSQL. |
| Simple Vector Store | `verified-docs` | `unknown-instance` | Prototipos o pruebas simples. | No usar para producción crítica salvo validación. |
| Qdrant Vector Store | `verified-docs` | `unknown-instance` | RAG con Qdrant. | Solo si existe Qdrant corporativo. |
| Pinecone Vector Store | `verified-docs` | `unknown-instance` | RAG con Pinecone. | Solo si existe proveedor/coste aprobado. |
| Vector Store Retriever | `verified-docs` | `unknown-instance` | Convertir vector store en retriever. | Separar retrieval de agente/cadena. |

### 6.4 Document loaders y text splitters

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo preferirlo frente a Code |
|---|---|---|---|---|
| Default Data Loader / Document Loader | `verified-docs` | `unknown-instance` | Cargar documentos para RAG. | Si cubre formato y metadata necesarios. |
| GitHub Document Loader | `verified-docs` | `unknown-instance` | Cargar documentos desde GitHub. | Útil para repos, si aplica. |
| Character Text Splitter | `verified-docs` | `unknown-instance` | Chunking simple por caracteres. | Si no se necesita lógica custom. |
| Recursive Character Text Splitter | `verified-docs` | `unknown-instance` | Chunking más robusto por separadores. | Preferible a Code si cubre solape/tamaño. |
| Token Splitter | `verified-docs` | `unknown-instance` | Chunking por tokens. | Útil para límites de modelo. |

### 6.5 Memoria y output parsers

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo usarlo |
|---|---|---|---|---|
| Postgres Chat Memory | `verified-docs` | `verified-used-in-workflow` | Memoria persistente. | Agentes con historial por conversación. |
| Buffer Window Memory / Simple Memory | `verified-docs` | `verified-used-in-workflow` | Memoria temporal. | Tests o contexto corto. |
| Structured Output Parser | `verified-docs` | `unknown-instance` | Forzar salida estructurada. | Evitar respuestas libres cuando se necesita JSON. |
| Auto-fixing Output Parser | `verified-docs` | `unknown-instance` | Reparar salida no válida. | Cuando el LLM falla formatos. |
| Item List Output Parser | `verified-docs` | `unknown-instance` | Salidas tipo listas. | Extracciones/listados. |

### 6.6 Tools para agentes

| Nodo / capacidad | Estado documental | Estado instancia | Uso recomendado | Cuándo usarlo |
|---|---|---|---|---|
| Code Tool | `verified-docs` | `unknown-instance` | Herramienta custom para agente. | Lógica interna controlada. |
| Workflow Tool | `verified-docs` | `unknown-instance` | Permitir que agente llame subworkflow. | Modularizar herramientas seguras. |
| HTTP Request Tool | `verified-docs` | `unknown-instance` | Tool HTTP para agente. | Solo con allowlist y controles. |

---

## 7. Mapa de decisión node-first

| Necesidad | Buscar primero | Si no basta |
|---|---|---|
| Entrada manual de prueba | Manual Trigger | Chat Trigger si es IA conversacional. |
| Ejecución programada | Schedule Trigger | Cron externo si n8n no gobierna bien la periodicidad. |
| Endpoint entrante | Webhook + Respond to Webhook | Servicio MCP/API propio si hay seguridad compleja. |
| Ruteo simple | IF | Switch si hay varias ramas. |
| Ruteo multi-categoría | Switch | Code si las reglas son dinámicas o calculadas. |
| Normalización simple | Edit Fields / Set | Code si la estructura es dinámica o anidada. |
| Filtrado de items | Filter | IF para bifurcación; Code para lógica compleja. |
| Agrupar items | Aggregate | Code para reducers complejos. |
| Dedupe simple | Remove Duplicates | DB upsert o Code si hay hash/reglas custom. |
| Ordenar/limitar | Sort / Limit | Code solo si la lógica es compleja. |
| Procesar muchos items | Loop Over Items / Split in Batches | Worker externo si hay volumen alto. |
| API externa común | Nodo nativo del servicio | HTTP Request si no cubre endpoint/headers. |
| GitLab/GitHub | Nodo nativo si está disponible | MCP/HTTP si se necesita read-only, safelist o redacción. |
| Embeddings | Embeddings OpenAI | HTTP Request si falta modelo/dimensiones. |
| RAG Supabase | Supabase Vector Store | Supabase REST/RPC o PostgreSQL/PGVector para schema custom. |
| Memoria agente | Postgres Chat Memory | Custom DB/API si se requiere gobierno avanzado. |
| Extraer campos con LLM | Information Extractor + Structured Output Parser | Prompt + Code si no está disponible. |
| Clasificar texto | Text Classifier | LLM Chain/Agent o Code + LLM. |
| Chunking RAG | Text Splitter documentado | Code si se requieren hashes, metadata compleja o reglas propias. |
| Documentación del canvas | Sticky Note | Confluence para documentación estable. |

---

## 8. Implicaciones para el pipeline GitLab Knowledge → n8n → Supabase

Diseño node-first recomendado tras combinar instancia + documentación:

| Fase | Opción preferente | Estado | Alternativa |
|---|---|---|---|
| Trigger | Manual Trigger durante pruebas; Schedule Trigger al estabilizar | Manual verificado; Schedule docs-derived | Mantener manual hasta credenciales reales. |
| Listar/leer GitLab Knowledge | GitLab Knowledge MCP vía HTTP Request | Verificado en workflow | GitLab nativo solo si UI lo confirma y cubre lectura segura. |
| Normalizar metadatos | Set/Edit Fields | Verificado | Code si la estructura varía. |
| Filtrar fuentes RAG | Filter/Switch si disponibles | docs-derived | Code/IF si no están disponibles. |
| Chunking | Text Splitter si disponible y suficiente | docs-derived | Code verificado para chunking custom. |
| Hashing/deduplicación | Remove Duplicates + DB upsert si aplica | docs-derived | Code verificado para hash custom. |
| Embeddings | Embeddings OpenAI | Verificado | HTTP Request a OpenAI si requiere modelo/dimensiones no soportadas. |
| Upsert Supabase | Supabase genérico/PostgreSQL si UI confirma | docs-derived/unknown-instance | HTTP Request a Supabase REST/RPC verificado. |
| Retrieval runtime | Supabase Vector Store | Verificado | PGVector Vector Store si se decide usar Postgres directo. |
| Agente consumidor | AI Agent + OpenAI Chat Model + memory | Verificado | RAG chain si se quiere menos autonomía que agente. |

---

## 9. Qué debe hacer el asistente cuando use este catálogo

Antes de proponer un workflow:

1. Convertir el objetivo funcional en operaciones: trigger, leer, transformar, filtrar, enriquecer, escribir, responder, validar.
2. Para cada operación, buscar nodo `verified-used-in-workflow` o `verified-instance`.
3. Si no existe, buscar candidato `verified-docs` en este catálogo.
4. Si el nodo está en `verified-docs` pero `unknown-instance`, indicar que debe buscarse en la UI antes de asumirlo.
5. Usar HTTP Request solo si el nodo nativo no existe, no está confirmado o no cubre la operación exacta.
6. Usar Code solo para lógica que no sea razonable con nodos visuales: chunking avanzado, hashing, parsing robusto, validaciones complejas o payloads dinámicos.
7. Separar claramente hecho, inferencia y recomendación.

---

## 10. Pendientes de verificación en instancia

- [ ] Buscar en la UI si existe nodo genérico PostgreSQL.
- [ ] Buscar en la UI si existe nodo genérico Supabase.
- [ ] Buscar en la UI si existen Schedule Trigger, Respond to Webhook, Switch, Merge, Loop Over Items, Filter, Aggregate, Remove Duplicates, Sort y Date & Time.
- [ ] Buscar en la UI si existen Structured Output Parser, Information Extractor, Text Classifier, Document Loaders y Text Splitters.
- [ ] Confirmar si existe GitLab nativo y qué operaciones permite.
- [ ] Confirmar si existe GitHub nativo y qué operaciones permite.
- [ ] Confirmar si existen Teams, Outlook, Google Sheets, Drive, Gmail o Slack según necesidades reales.
- [ ] Obtener versión real de n8n desde UI, contenedor o Tecnología.
- [ ] Si Tecnología lo permite, ampliar el MCP con una tool read-only de catálogo global de nodos.
