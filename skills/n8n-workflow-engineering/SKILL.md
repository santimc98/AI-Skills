# n8n Workflow Engineering

## Cuándo usar esta skill

Usar esta skill cuando Santi pida auditar, revisar, depurar, editar, documentar o crear workflows de n8n, especialmente si la tarea implica nodos, conexiones, credenciales, expresiones, código, ejecuciones, errores, MCP, agentes IA o automatizaciones en producción.

También debe usarse cuando una tarea toque workflows que publican contenido externo, envían mensajes, crean registros, escriben en memoria o ejecutan acciones con impacto fuera de n8n.

## Objetivo

Trabajar con n8n con mentalidad de producción:

- robustez,
- trazabilidad,
- seguridad,
- facilidad de depuración,
- cambios mínimos,
- validación posterior,
- prevención de publicaciones o acciones incorrectas,
- uso preferente de nodos nativos antes que soluciones genéricas con Code o HTTP Request.

El objetivo no es solo que el workflow funcione una vez, sino que sea mantenible, observable y seguro ante fallos parciales.

## Entradas necesarias

Antes de actuar, recopilar o confirmar solo la información crítica:

- Nombre exacto del workflow.
- Objetivo funcional del workflow.
- Ejecución afectada, si existe un fallo concreto.
- Nodo donde aparece el error, si el usuario lo conoce.
- Resultado esperado.
- Riesgo externo: publicación, email, webhook, escritura en base de datos, CRM, memoria o API externa.
- Restricciones explícitas del usuario: no publicar, no tocar credenciales, no activar workflow, no borrar datos, etc.

Si hay acceso MCP a n8n y la tarea requiere tocar n8n, hacer primero un health check.

## Principio node-first

Antes de proponer un nodo Code o HTTP Request, comprobar si existe un nodo nativo de n8n que cubra la necesidad.

Regla práctica:

1. Preferir nodo nativo oficial, AI/LangChain node, core node o community node ya instalado.
2. Distinguir siempre entre nodos verificados en la instancia y nodos solo documentados.
3. Si el nodo nativo existe y cubre la operación, usarlo salvo que haya una limitación conocida o el caso requiera control HTTP específico.
4. Si se propone HTTP Request o Code, explicar brevemente por qué no se usa un nodo nativo.
5. No asumir que un nodo no existe solo porque no esté en memoria: verificar en los catálogos, en la instancia de n8n, en el MCP disponible o pedir a Santi una captura/búsqueda si es necesario.

Estados de confianza recomendados:

| Estado | Uso |
|---|---|
| `verified-used-in-workflow` / `verified-instance` | Confirmado en workflows reales o catálogo real de la instancia. Puede recomendarse con alta confianza. |
| `verified-docs` / `docs-derived` | Confirmado por documentación n8n. Puede proponerse como candidato, pero debe verificarse en la UI/instancia antes de depender de él. |
| `unknown-instance` | No confirmado en la instancia. No diseñar alrededor de él sin validación. |

Ejemplos de preferencia:

- Supabase/RAG: preferir Supabase Vector Store, PGVector Vector Store, Embeddings OpenAI o PostgreSQL cuando cubran la operación; usar HTTP Request solo para REST/RPC, upserts especiales, funciones `match_*`, headers personalizados o funcionalidades no expuestas por el nodo.
- GitLab/GitHub: preferir nodos nativos cuando estén instalados y la operación esté cubierta; usar HTTP/MCP cuando se necesite un wrapper interno, lectura restringida, endpoints no soportados o lógica de seguridad propia.
- OpenAI/embeddings/LLM: preferir OpenAI Chat Model, Embeddings OpenAI, AI Agent, LLM Chain, Information Extractor, Text Classifier o Structured Output Parser cuando estén disponibles; usar HTTP Request si el modelo, endpoint, payload o proveedor no está soportado por el nodo instalado.
- Transformaciones simples: preferir Edit Fields/Set, IF, Switch, Merge, Loop Over Items, Filter, Aggregate, Remove Duplicates, Sort, Date & Time o nodos equivalentes antes que Code.
- Transformaciones complejas: usar Code solo para lógica determinista que no pueda mantenerse razonablemente con nodos visuales, como chunking avanzado, hashing, deduplicación custom, parsing robusto o payloads dinámicos.

## Catálogo actualizado de nodos n8n

Para evitar diseñar workflows con información desactualizada, mantener una fuente de conocimiento viva sobre los nodos disponibles en la instancia real de n8n y los nodos documentados por n8n.

Prioridad de fuentes, de más fiable a menos fiable:

1. Catálogo real exportado desde la instancia de n8n y versión instalada.
2. Herramientas MCP/API de n8n que permitan listar node types, credenciales, operaciones o schemas.
3. Workflows existentes ya validados en la instancia.
4. `knowledge/n8n-node-inventory.json` con nodos observados y patrones reales.
5. `knowledge/n8n-node-catalog.md` como catálogo operativo humano.
6. `knowledge/n8n-node-docs-derived-catalog.md` como catálogo documental de nodos n8n, útil para buscar alternativas node-first pero no suficiente para asumir instalación.
7. Documentación oficial de n8n correspondiente a la versión instalada.
8. Memoria o conocimiento general del asistente, solo como apoyo.

Regla crítica:

```text
Un nodo docs-derived no debe tratarse como instalado. Debe verificarse en UI, MCP, workflow existente o catálogo real antes de diseñar un workflow que dependa de él.
```

Archivos de conocimiento relacionados:

```text
knowledge/n8n-node-catalog.md
knowledge/n8n-node-inventory.json
knowledge/n8n-node-docs-derived-catalog.md
```

Contenido mínimo recomendado para cada nodo relevante:

```text
- Nombre visible del nodo.
- Nombre técnico/type si se conoce.
- Paquete: core, official, community o custom.
- Categoría: base de datos, IA, comunicación, transformación, trigger, devops, etc.
- Estado: verified-instance, verified-used-in-workflow, verified-docs, docs-derived, unknown-instance.
- Operaciones principales.
- Credenciales necesarias.
- Casos de uso recomendados.
- Cuándo preferir este nodo frente a HTTP Request.
- Cuándo no basta y conviene usar HTTP Request o Code.
- Versión de n8n donde se ha verificado.
- Fecha de revisión.
```

Actualizar este catálogo cuando:

- se actualice la versión de n8n;
- se instale o elimine un community node;
- se detecte que existe un nodo nativo que antes no se estaba usando;
- se cree un workflow con integración nueva;
- un nodo cambie de operaciones, credenciales o comportamiento;
- se confirme en UI un nodo que antes solo estaba como docs-derived.

## Procedimiento paso a paso

### 1. Health check inicial

Si la tarea requiere interactuar con n8n mediante MCP, empezar comprobando que la instancia responde correctamente.

Verificar, según las herramientas disponibles:

1. Conectividad con n8n.
2. Acceso a workflows.
3. Acceso a ejecuciones.
4. Permisos suficientes para leer antes de escribir.
5. Si el workflow está activo o desactivado.
6. Versión de n8n, si está disponible.
7. Nodos instalados o catálogo de nodos, si el MCP/API lo permite.
8. Si el MCP no expone catálogo global, usar `n8n-node-inventory.json` como evidencia de workflows y `n8n-node-docs-derived-catalog.md` solo como mapa de candidatos.

No modificar nada durante el health check.

### 2. Diagnosticar antes de editar

Antes de aplicar cambios:

1. Leer la estructura del workflow.
2. Identificar nodos relevantes.
3. Revisar conexiones.
4. Revisar expresiones críticas.
5. Revisar código en nodos Code/Function.
6. Revisar ejecuciones recientes si el problema viene de una ejecución.
7. Separar hechos confirmados de hipótesis.
8. Identificar si un nodo Code o HTTP Request podría sustituirse por un nodo nativo más mantenible.
9. Si el sustituto solo aparece como docs-derived, pedir confirmación en UI antes de recomendar el cambio como definitivo.

No editar por intuición sin haber localizado la causa probable.

### 3. Selección de nodos antes de diseñar o modificar

Antes de proponer una arquitectura nueva o modificar un flujo existente:

1. Listar las operaciones necesarias: leer, escribir, buscar, transformar, validar, enviar, esperar, disparar, responder, etc.
2. Mapear cada operación al nodo nativo más específico disponible.
3. Priorizar nodos `verified-used-in-workflow` si cubren la necesidad.
4. Considerar nodos `verified-docs` como candidatos a verificar en la UI.
5. Reservar HTTP Request para APIs o endpoints no cubiertos por nodos nativos confirmados.
6. Reservar Code para lógica de transformación, validación, hashing, chunking, deduplicación o parsing que no pueda mantenerse bien con nodos visuales.
7. Documentar la razón si se elige una opción genérica.

Plantilla rápida de decisión:

```text
Necesidad:
Nodo nativo considerado:
Estado del nodo: verified-used-in-workflow / verified-instance / verified-docs / unknown-instance
Motivo para usarlo / descartarlo:
Alternativa elegida:
Riesgo o limitación:
```

### 4. Revisión de ejecuciones fallidas

Para cada bug o ejecución fallida, identificar de forma explícita:

- Ejecución afectada.
- Nodo exacto que falla.
- Error exacto reportado por n8n.
- Entrada recibida por el nodo.
- Salida esperada.
- Causa raíz.
- Solución mínima segura.

Si hay varios errores encadenados, resolver primero el error más cercano a la causa raíz, no solo el último síntoma.

### 5. Política de cambios

Aplicar siempre cambios mínimos y seguros.

Reglas obligatorias:

- No borrar workflows salvo instrucción explícita de Santi.
- No modificar credenciales salvo instrucción explícita de Santi.
- No publicar, activar, desactivar o ejecutar acciones externas si no es necesario para validar.
- No sobrescribir lógica compleja si basta con corregir una expresión, conexión o validación.
- No eliminar validaciones de seguridad para que el workflow “pase”.
- No ocultar errores críticos con valores por defecto peligrosos.
- No sustituir un nodo nativo por HTTP Request o Code sin una razón técnica clara.
- No sustituir por un nodo solo `docs-derived` sin comprobar que existe en la instancia.

Antes de cambios peligrosos, explicar brevemente qué se va a tocar y por qué.

### 6. Validar después de modificar

Después de cualquier cambio:

1. Validar que el workflow conserva su estructura esperada.
2. Revisar que las conexiones siguen siendo correctas.
3. Revisar expresiones modificadas.
4. Revisar nodos afectados por el cambio.
5. Ejecutar o revisar una ejecución de prueba cuando sea seguro.
6. Confirmar que no aparecen errores nuevos aguas abajo.
7. Si hay publicación externa, verificar los controles previos antes de permitir salida.
8. Verificar que las notas visuales del workflow siguen reflejando la arquitectura real.

### 7. Workflows con publicación o impacto externo

Para workflows que publican en LinkedIn, envían emails, llaman APIs externas, escriben en memoria o hacen acciones públicas:

- Preferir fallar antes que publicar contenido truncado, vacío o incorrecto.
- Validar longitud mínima y máxima del contenido.
- Validar que no falten título, cuerpo, enlaces, hashtags o imagen si son obligatorios.
- Validar que no se publique contenido de prueba.
- Validar que el texto final sea el texto completo esperado, no una versión resumida accidental.
- Validar que las variables usadas por el nodo final existen realmente.
- Validar que los nodos referenciados en expresiones existen y mantienen el nombre esperado.

## Uso de HTTP Request

HTTP Request es válido cuando aporta control real, no como solución por defecto.

Usarlo preferentemente cuando:

- no existe nodo nativo para el servicio o endpoint;
- el nodo nativo existe pero no soporta la operación concreta;
- se requiere un endpoint REST/RPC específico;
- se necesitan headers, parámetros, paginación, upsert o autenticación personalizada;
- se llama a un MCP propio, proxy interno o servicio corporativo;
- se está prototipando una integración que luego podría migrarse a nodo nativo.

Antes de usarlo, comprobar:

- método HTTP;
- URL final;
- headers;
- body;
- autenticación;
- respuesta esperada;
- comportamiento ante error;
- si se debe activar `Never Error` o no;
- si se debe incluir o no response headers.

## Uso de Code

Code debe usarse para lógica que sea más segura, clara o mantenible en código que en nodos visuales.

Casos razonables:

- chunking de documentos;
- hashing o deduplicación;
- normalización compleja;
- parsing robusto de JSON/CSV/texto;
- validaciones multi-campo;
- construcción de payloads complejos;
- control de errores determinista;
- limpieza de datos con reglas explícitas.

Buenas prácticas:

- evitar dependencias externas salvo que estén permitidas en la instancia;
- no asumir que módulos como `crypto` están permitidos;
- preferir funciones internas sencillas cuando el task runner bloquee módulos;
- devolver siempre items con estructura consistente;
- añadir comentarios cortos solo donde aclaren lógica no evidente;
- no usar Code para operaciones que ya resuelven nodos nativos confirmados de forma clara.

## Documentación visual del workflow

Cuando se cree o documente un workflow complejo en n8n, añadir sticky notes en español para que cualquier persona pueda entenderlo al abrirlo.

Cada workflow debería incluir, cuando aplique:

- Objetivo funcional del workflow.
- Estado actual: borrador, pruebas, producción, inactivo, pendiente de credenciales, etc.
- Flujo principal resumido por fases.
- Sistemas conectados: APIs, bases de datos, MCPs, webhooks o servicios externos.
- Credenciales o variables necesarias, sin exponer valores sensibles.
- Tablas, endpoints o recursos destino.
- Reglas de deduplicación, claves únicas o criterios de upsert.
- Advertencias de seguridad antes de ejecutar acciones externas.

Las notas deben ser operativas, breves y en español. No deben contener tokens, contraseñas, claves API ni secretos reales.

## Criterios de calidad

Un diagnóstico o cambio en n8n se considera correcto si:

- La causa raíz está identificada, no solo el síntoma.
- El nodo exacto afectado queda claro.
- La solución es mínima y reversible.
- El workflow queda más seguro que antes.
- Se evita introducir dependencias ocultas.
- Se mantiene trazabilidad de entradas, salidas y nodos afectados.
- La validación posterior confirma el resultado.
- La explicación permite a Santi entender qué pasó y cómo evitarlo.
- La elección de nodos prioriza componentes nativos antes que HTTP Request o Code cuando sea razonable.
- Si se usa HTTP Request o Code, queda justificado por limitación funcional, seguridad, control o mantenibilidad.
- Si se propone un nodo documentado pero no verificado en instancia, queda indicado como pendiente de comprobación.
- El workflow queda documentado visualmente con notas en español cuando su complejidad lo justifique.

## Formato de salida esperado

Responder siempre separando estas secciones cuando se haya diagnosticado o modificado algo:

```markdown
## Diagnóstico

## Cambio aplicado

## Resultado

## Siguiente acción recomendada
```

Si solo se está proponiendo una arquitectura o creando un workflow nuevo, usar:

```markdown
## Objetivo

## Diseño propuesto

## Workflow paso a paso

## Validaciones de seguridad

## Siguiente acción recomendada
```

Cuando se proponga la elección de nodos, añadir si aporta valor:

```markdown
## Selección de nodos

| Necesidad | Nodo recomendado | Estado del nodo | Motivo | Alternativa si falla |
|---|---|---|---|---|
```

## Errores comunes a evitar

- Editar antes de diagnosticar.
- Cambiar varios nodos a la vez sin necesidad.
- Borrar workflows, ejecuciones o credenciales sin instrucción explícita.
- Cambiar credenciales para probar hipótesis.
- Referenciar nodos por nombres que ya no existen.
- Usar datos de un nodo recortado cuando se necesita el texto completo.
- Publicar contenido externo sin validar longitud, estructura y campos obligatorios.
- Confundir el error final con la causa raíz.
- No revisar nodos aguas abajo después de corregir un nodo anterior.
- No explicar claramente qué se cambió.
- Usar HTTP Request por desconocimiento de nodos nativos existentes.
- Usar Code para transformaciones simples que se pueden resolver con nodos visuales.
- Asumir que un nodo `docs-derived` está instalado sin comprobarlo en la instancia.
- No consultar la versión real de n8n ni los nodos instalados cuando el diseño depende de ello.
- Dejar sticky notes en inglés o con información genérica poco útil para el equipo.

## Plantillas relacionadas

No hay plantillas obligatorias todavía.

Cuando se creen plantillas para auditoría o documentación de workflows, ubicarlas preferentemente en `templates/`.

## Conocimiento relacionado

- `knowledge/n8n-node-catalog.md` para el catálogo humano de nodos y patrones confirmados/parciales.
- `knowledge/n8n-node-inventory.json` para inventario estructurado de nodos observados y patrones reales.
- `knowledge/n8n-node-docs-derived-catalog.md` para nodos documentados por n8n que deben verificarse en instancia antes de usarse.
- `skills/linkedin-ai-news-workflow/SKILL.md` para el workflow principal de noticias de IA hacia LinkedIn.
- `skills/ai-research/SKILL.md` cuando la tarea incluya investigación o selección de noticias/modelos/herramientas de IA.
- `skills/prompt-engineering/SKILL.md` cuando la tarea incluya prompts para agentes, AI Writer o nodos LLM.
