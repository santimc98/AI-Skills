---
name: educa-edtech-jira
description: "Use this skill whenever Santi (Educa Edtech) asks to create, review, update, organize, audit, summarize or plan work in Jira for the OPERATIONS project (AA). Triggers: 'crea una tarea en Jira', 'actualiza Jira', 'mueve la tarea', 'organiza el backlog', 'crea una Epic', 'crea subtareas', 'prepara el ticket', 'revisa el board', 'tracker documentación', 'tipo-proyecto', 'tipo-quickwin', 'diagnóstico', 'rediseño', 'bloqueado', 'testeo', 'link Confluence', or any request involving Jira/Confluence operational tracking for Educa Edtech. Always search/read before changing, respect Epics, labels, states, Confluence linkage and confirmation rules."
---

# Jira · Educa Edtech — Gestión del proyecto OPERATIONS (AA)

Esta skill define cómo trabajar con Jira en el proyecto **OPERATIONS** de Educa Edtech. Debe usarse antes de crear, editar, mover, comentar, ordenar o auditar issues del proyecto **AA**.

La regla principal es sencilla: **Jira refleja la ejecución del trabajo; Confluence refleja la documentación y el conocimiento estable**. Ambos deben mantenerse conectados.

---

## 1. Datos de conexión

| Campo | Valor |
|---|---|
| Sitio | `educaedtech.atlassian.net` |
| Cloud ID | `7ba28d00-0b5a-4689-81b8-d07ff3c1272e` |
| Proyecto Jira | **OPERATIONS** |
| Project key | `AA` |
| Project ID | `11724` |
| Tipo de proyecto | Software / Team-managed / Next-gen |
| Categoría | `AI PROJECTS` |
| Board backlog | `boards/1449/backlog` |
| Espacio Confluence relacionado | **OPERACIONES** (`AA1`) |

---

## 2. Cuándo usar esta skill

Usar esta skill cuando el usuario pida:

- Crear una Epic, tarea, subtarea, petición o error en Jira.
- Organizar el backlog del proyecto `AA`.
- Revisar si una tarea está bien redactada.
- Convertir una conversación, reunión o decisión en issues accionables.
- Dividir una iniciativa en tareas y subtareas.
- Preparar descripciones, criterios de aceptación o comentarios para Jira.
- Auditar estados, owners, etiquetas o trazabilidad del board.
- Conectar tareas de Jira con documentación de Confluence.
- Decidir si algo debe ser `tipo-proyecto`, `tipo-quickwin`, `tipo-proceso` o `tipo-documento`.
- Gestionar trabajo documental dentro de `TRACKER DOCUMENTACIÓN`.

Si la tarea implica crear o actualizar una página de Confluence, combinar con:

```text
skills/educa-edtech-confluence/SKILL.md
```

---

## 3. Principio operativo

El proyecto de Operaciones se organiza en torno a **Epics**.

Cada Epic representa una iniciativa:

- Proyecto estructural.
- Quick win.
- Automatización.
- Agente de IA.
- Rediseño operativo.
- Trabajo transversal relevante.

Dentro de cada Epic viven las tareas de ejecución.

Existe una Epic especial:

```text
AA-86 — TRACKER DOCUMENTACIÓN
```

Esta Epic agrupa las tareas documentales del área. No representa una iniciativa de mejora, sino un contenedor de documentación formalizada.

---

## 4. Estructura oficial del proyecto

```text
Proyecto AA — OPERATIONS
│
├── Epic — [Nombre de la iniciativa]
│   ├── Tarea — Diagnóstico del proceso
│   ├── Tarea — Rediseño del proceso
│   ├── Tarea — Ejecución técnica
│   └── Subtareas concretas
│
├── Epic — AA-86 TRACKER DOCUMENTACIÓN
│   ├── Tarea — Documento de proceso
│   ├── Tarea — Ficha de automatización
│   └── Tarea — Actualización de Confluence
│
└── Epic — AA-94 BACKLOG PETICIONES
    └── Peticiones o iniciativas pendientes de activar
```

---

## 5. Tipos de issue disponibles

| Tipo | Uso correcto |
|---|---|
| **Epic** | Iniciativa completa, proyecto, quick win o contenedor especial |
| **Tarea** | Trabajo independiente dentro de una Epic |
| **Subtarea** | Paso pequeño que forma parte de una tarea mayor |
| **Petición** | Solicitud funcional o necesidad expresada como petición |
| **Error** | Problema, fallo o comportamiento incorrecto |

Regla práctica:

- Si agrupa varias tareas y tiene entidad propia → **Epic**.
- Si es una unidad de trabajo ejecutable → **Tarea**.
- Si depende claramente de una tarea madre → **Subtarea**.
- Si es una solicitud aún poco definida → **Petición**.
- Si describe un fallo → **Error**.

---

## 6. Glosario operativo

| Término | Definición | Dónde vive |
|---|---|---|
| **Iniciativa** | Cualquier Epic con etiqueta `tipo-proyecto` o `tipo-quickwin` | Epic |
| **Proyecto** | Iniciativa estructural, planificada y con varias fases | Epic con `tipo-proyecto` |
| **Quick Win** | Iniciativa de bajo esfuerzo, resultado rápido y ejecución corta | Epic con `tipo-quickwin` |
| **Proceso** | Trabajo de diagnóstico o rediseño de un proceso | Tarea dentro de una Epic |
| **Documento** | Trabajo documental vinculado a una iniciativa | Tarea dentro de `AA-86 TRACKER DOCUMENTACIÓN` |
| **Backlog** | Iniciativas identificadas pero pendientes de activar | `AA-94 BACKLOG PETICIONES` o Epic en `PENDIENTE` |

---

## 7. Sistema de etiquetas

### 7.1 Etiquetas principales

Todo Epic debe tener una de estas dos etiquetas:

| Etiqueta | Se aplica a | Cuándo usarla |
|---|---|---|
| `tipo-proyecto` | Epic | Iniciativa estructural, con planificación o impacto relevante |
| `tipo-quickwin` | Epic | Iniciativa de bajo esfuerzo, resultado rápido y alcance acotado |

Un Epic sin etiqueta puede quedar fuera de KPIs, seguimiento y reporting.

### 7.2 Etiquetas de tareas específicas

| Etiqueta | Se aplica a | Cuándo usarla |
|---|---|---|
| `tipo-proceso` | Tarea | Diagnóstico o rediseño de proceso |
| `tipo-documento` | Tarea | Documentación formal en Confluence |

Reglas:

- No inventar nuevas etiquetas sin indicación explícita del equipo.
- No mezclar `tipo-proyecto` y `tipo-quickwin` en la misma Epic.
- No usar `tipo-proceso` para una Epic; se usa para tareas específicas.
- No usar `tipo-documento` para una Epic; se usa para tareas documentales.

---

## 8. Estados oficiales y significado

| Estado | Significado | Uso típico |
|---|---|---|
| `PENDIENTE` | Identificado, priorizado o creado, pero no iniciado | Epic, tarea o subtarea |
| `DIAGNOSTICO` | Se observa y documenta el proceso AS-IS; no se proponen soluciones todavía | Tarea de proceso |
| `REDISEÑO` | Se diseña el TO-BE, reglas, flujo y viabilidad; no se ejecuta todavía | Tarea de proceso |
| `EN CURSO` | Trabajo activo | Epic, tarea o subtarea |
| `BLOQUEADO` | No puede avanzar por dependencia externa | Epic, tarea o subtarea |
| `TESTEO` | Ejecutado y pendiente de pruebas | Iniciativas o tareas técnicas |
| `COMPLETADO` / `Completado` | Finalizado, revisado y en producción/publicado | Cierre de trabajo |

Diferencia clave:

```text
DIAGNOSTICO = observar y documentar lo que existe.
REDISEÑO = diseñar lo que debería existir.
EN CURSO = ejecutar o construir.
```

No se debe saltar directamente de diagnóstico a ejecución si falta rediseño, reglas de negocio o validación técnica.

---

## 9. Reglas por tipo de trabajo

### 9.1 Epic de proyecto

Usar `tipo-proyecto` cuando:

- Tiene alcance estructural.
- Requiere varias fases.
- Necesita diagnóstico, rediseño, validación o coordinación técnica.
- Tiene impacto operativo relevante.
- Puede durar más de dos semanas.

Ejemplos:

```text
Automatizacion flujos CAPMAN
Ia correctiva - Hawkings
IA resolutiva Callbell
N8n- seguimiento y bienvenida
```

### 9.2 Epic de quick win

Usar `tipo-quickwin` cuando:

- Tiene alcance acotado.
- Se puede ejecutar rápido.
- No requiere rediseño profundo.
- El resultado esperado es claro.
- El esfuerzo es bajo o medio.

Ejemplos:

```text
Agente ventas UDAVINCI
Triaje Tickets soporte
Scraping empresas - Empleo
Automatización reseñas
```

### 9.3 Tarea documental

Las tareas documentales deben vivir, como norma, dentro de:

```text
AA-86 — TRACKER DOCUMENTACIÓN
```

Ejemplos:

```text
Ficha automatización - PRO-007-STUDENTSUCCESS
Ficha automatización agente Angel
Documento proceso del agente
Plantilla automatización scrapeo
```

Si una tarea documental se crea temporalmente dentro de la Epic de la iniciativa para mantener contexto, debe indicarse claramente si después hay que moverla al `TRACKER DOCUMENTACIÓN`.

---

## 10. Relación obligatoria con Confluence

Toda tarea que genere, modifique o dependa de documentación debe enlazar la página de Confluence correspondiente.

Aplicar especialmente a:

- Documento de proceso.
- Ficha de automatización.
- Reglas de negocio.
- Diagramas de flujo.
- Documentación técnica.
- Diagnóstico AS-IS.
- Rediseño TO-BE.
- Requisitos técnicos.
- Plantillas o protocolos.

Reglas:

1. Buscar primero si la página ya existe en Confluence.
2. Si existe, enlazarla en la descripción o comentario de Jira.
3. Si no existe, crear propuesta de página siguiendo `educa-edtech-confluence`.
4. No marcar una tarea documental como completada si el documento no está publicado/revisado en Confluence.
5. Cuando se actualice Confluence por una tarea Jira, dejar comentario en Jira con el enlace y resumen del cambio.

---

## 11. Relación con Tecnología

Una iniciativa pasa a Tecnología cuando la Epic queda asignada a:

```text
Cristina Bullejos
```

Antes de pasar trabajo a Tecnología, verificar que están enlazados o descritos:

- Reglas de negocio.
- Flujos o diagramas.
- Requisitos técnicos.
- Entradas y salidas esperadas.
- Criterios de validación.
- Dependencias y accesos.
- Página de Confluence correspondiente.

Si falta algo crítico, crear tarea o subtarea antes de transferir.

---

## 12. Flujo recomendado para iniciativas de proceso

```text
1. Crear o identificar Epic de iniciativa
2. Etiquetar Epic como tipo-proyecto o tipo-quickwin
3. Crear tarea: Diagnóstico del proceso
4. Documentar AS-IS en Confluence
5. Crear tarea: Rediseño del proceso
6. Diseñar TO-BE, reglas y flujo
7. Validar viabilidad técnica si aplica
8. Pasar Epic a EN CURSO para ejecución
9. Pasar a TESTEO cuando esté implementado
10. Completar cuando esté probado y documentado
```

Estructura recomendada:

```text
Epic — [Nombre de la iniciativa]
├── Tarea — Diagnóstico del proceso
│   ├── Subtarea — Recopilar información actual
│   ├── Subtarea — Documentar AS-IS en Confluence
│   └── Subtarea — Validar diagnóstico con owner funcional
│
├── Tarea — Rediseño del proceso
│   ├── Subtarea — Definir TO-BE
│   ├── Subtarea — Crear diagrama de flujo
│   ├── Subtarea — Definir reglas de negocio y excepciones
│   └── Subtarea — Validar viabilidad con Tecnología
│
└── Tarea — Ejecución / implementación
    ├── Subtarea — Implementar solución
    ├── Subtarea — Testear funcionamiento
    └── Subtarea — Actualizar documentación final
```

---

## 13. Cómo redactar issues correctamente

Toda tarea debe ser entendible sin contexto externo.

### 13.1 Estructura mínima de una descripción

```markdown
## Objetivo
[Qué se quiere conseguir y por qué importa.]

## Contexto
[De dónde viene la petición, reunión, proceso o decisión.]

## Alcance
[Qué entra y qué no entra en esta tarea.]

## Entregables
- [Entregable 1]
- [Entregable 2]

## Criterios de aceptación
- [Condición verificable 1]
- [Condición verificable 2]

## Enlaces relacionados
- Confluence: [URL]
- SharePoint/Miro/Word: [URL]
- Epic relacionada: [AA-XXX]
```

### 13.2 Reglas de redacción

- Usar títulos claros y accionables.
- Evitar títulos genéricos como `hacer documento` o `revisar cosas`.
- Indicar entregables concretos.
- Diferenciar objetivo, contexto y tareas.
- Si se menciona un Word, Excel, Miro o Confluence, añadir enlace.
- Si hay dudas, escribirlas en comentarios mencionando a la persona correspondiente.

---

## 14. Plantillas rápidas

### 14.1 Epic de iniciativa

```markdown
## Objetivo
[Qué iniciativa se quiere desarrollar y qué problema resuelve.]

## Contexto
[Origen de la necesidad: reunión, área, proceso, stakeholder, documento previo.]

## Alcance
Incluye:
- 

No incluye:
- 

## Tipo de iniciativa
Etiqueta: `tipo-proyecto` / `tipo-quickwin`

## Entregables esperados
- 

## Documentación relacionada
- Confluence:
- SharePoint/Miro:

## Criterios de cierre
- La solución está ejecutada o entregada.
- La documentación vinculada está actualizada en Confluence.
- Los stakeholders han validado el resultado.
```

### 14.2 Tarea de diagnóstico

```markdown
## Objetivo
Documentar el proceso actual AS-IS sin proponer todavía una solución.

## Contexto
[Proceso, área, owner funcional y motivo del diagnóstico.]

## Actividades
- Recopilar información del proceso actual.
- Identificar entradas, salidas, herramientas y responsables.
- Documentar pasos operativos AS-IS.
- Detectar fricciones, riesgos y dependencias.
- Crear o actualizar la página de Confluence correspondiente.

## Entregables
- Documento de proceso AS-IS en Confluence.
- Lista de riesgos/fricciones detectadas.
- Enlaces a evidencias o documentos fuente.

## Criterios de aceptación
- El proceso está documentado en Confluence.
- La página contiene owner, área, alcance, pasos y herramientas.
- El owner funcional ha podido revisar o validar el diagnóstico.
```

### 14.3 Tarea de rediseño

```markdown
## Objetivo
Diseñar el proceso TO-BE y dejarlo preparado para ejecución o validación técnica.

## Contexto
[Diagnóstico previo, problema detectado y objetivo del rediseño.]

## Actividades
- Definir flujo TO-BE.
- Crear diagrama de flujo o enlazar Miro.
- Definir reglas de negocio y excepciones.
- Identificar requisitos técnicos.
- Validar viabilidad con Tecnología si aplica.
- Actualizar la documentación en Confluence.

## Entregables
- Flujo TO-BE documentado.
- Diagrama o enlace a Miro.
- Reglas de negocio.
- Requisitos técnicos.
- Página de Confluence actualizada.

## Criterios de aceptación
- El rediseño está descrito de forma ejecutable.
- Las reglas de negocio están claras.
- Las dependencias técnicas están identificadas.
- La documentación está enlazada en Jira.
```

### 14.4 Tarea documental para TRACKER DOCUMENTACIÓN

```markdown
## Objetivo
Formalizar la documentación de [proceso/automatización/agente] en Confluence.

## Contexto
[Iniciativa de origen, Epic relacionada y motivo de la documentación.]

## Actividades
- Revisar documentación fuente.
- Consultar IDs de procesos y automatizaciones si aplica.
- Usar la plantilla oficial de Confluence.
- Completar metadatos, owner, área, anillo y estado.
- Añadir etiquetas correspondientes.
- Enlazar la página resultante en esta tarea.

## Entregables
- Página de Confluence publicada o actualizada.
- Enlace a la Epic/iniciativa relacionada.
- Comentario final indicando qué se ha documentado.

## Criterios de aceptación
- La página está en la ubicación correcta.
- La documentación sigue la plantilla oficial.
- La tarea contiene enlace a Confluence.
- El documento está revisado antes de marcar como completado.
```

### 14.5 Subtarea

```markdown
## Qué hay que hacer
[Acción concreta.]

## Resultado esperado
[Resultado verificable.]

## Dependencias
[Persona, documento, acceso o decisión necesaria.]
```

### 14.6 Comentario de avance

```markdown
Actualización:

- Hecho:
  - 
- Pendiente:
  - 
- Bloqueos o dudas:
  - 
- Enlaces:
  - Confluence:
  - Documento/Miro/SharePoint:
```

### 14.7 Comentario de cierre

```markdown
Trabajo completado.

Resultado:
- 

Documentación actualizada:
- Confluence: [URL]

Validaciones:
- 

Observaciones:
- 
```

---

## 15. Checklist antes de crear una Epic

Antes de crear una Epic:

- [ ] ¿Representa una única iniciativa?
- [ ] ¿No existe ya una Epic equivalente?
- [ ] ¿Está claro si es `tipo-proyecto` o `tipo-quickwin`?
- [ ] ¿El título es permanente y suficientemente descriptivo?
- [ ] ¿Tiene owner o responsable inicial?
- [ ] ¿La descripción contiene objetivo, contexto, alcance y entregables?
- [ ] ¿Tiene relación con Confluence o documentación existente?
- [ ] ¿No está duplicando `BACKLOG PETICIONES`?

---

## 16. Checklist antes de crear una tarea

Antes de crear una tarea:

- [ ] ¿Debe vivir dentro de una Epic existente?
- [ ] ¿Es una tarea de ejecución, diagnóstico, rediseño o documentación?
- [ ] ¿Debe ir al `TRACKER DOCUMENTACIÓN`?
- [ ] ¿Necesita etiqueta `tipo-proceso` o `tipo-documento`?
- [ ] ¿Tiene entregables claros?
- [ ] ¿Tiene criterios de aceptación verificables?
- [ ] ¿Debe enlazar una página de Confluence?
- [ ] ¿Debe asignarse a una persona concreta?

---

## 17. Checklist antes de completar una tarea

Antes de mover una tarea a completado:

- [ ] ¿El entregable existe?
- [ ] ¿La documentación está enlazada?
- [ ] ¿Confluence está actualizado si aplica?
- [ ] ¿Se ha añadido comentario final de cierre?
- [ ] ¿No quedan subtareas abiertas críticas?
- [ ] ¿El owner o stakeholder relevante ha validado o puede revisar el resultado?

---

## 18. Consultas JQL útiles

### Todas las issues recientes del proyecto

```jql
project = AA ORDER BY updated DESC
```

### Epics del proyecto

```jql
project = AA AND issuetype = Epic ORDER BY updated DESC
```

### Epics pendientes

```jql
project = AA AND issuetype = Epic AND status = PENDIENTE ORDER BY updated DESC
```

### Iniciativas activas

```jql
project = AA AND issuetype = Epic AND status = "EN CURSO" ORDER BY updated DESC
```

### Tareas documentales

```jql
project = AA AND parent = AA-86 ORDER BY updated DESC
```

### Trabajo asignado a Santi

```jql
project = AA AND assignee = currentUser() ORDER BY updated DESC
```

### Issues sin etiqueta

```jql
project = AA AND labels is EMPTY ORDER BY updated DESC
```

### Issues bloqueadas

```jql
project = AA AND status = BLOQUEADO ORDER BY updated DESC
```

---

## 19. Reglas de seguridad al usar herramientas

Antes de modificar Jira real:

1. Leer el issue actual si existe.
2. Comprobar estado, parent, assignee, labels y descripción.
3. Preparar propuesta de cambio.
4. Pedir confirmación explícita si la acción modifica información real.

Acciones que requieren confirmación explícita:

- Crear issues.
- Editar títulos o descripciones.
- Cambiar estado.
- Cambiar parent/Epic.
- Cambiar assignee.
- Añadir comentarios visibles al equipo.
- Crear enlaces entre issues.
- Cerrar o reabrir trabajo.

Se puede consultar, resumir y proponer sin confirmación adicional.

---

## 20. Flujo de trabajo con Atlassian Rovo

| Acción | Herramienta orientativa |
|---|---|
| Buscar issues | `searchJiraIssuesUsingJql` o Rovo Search |
| Leer issue | `getJiraIssue` |
| Crear issue | `createJiraIssue` |
| Ver transiciones | `getTransitionsForJiraIssue` |
| Cambiar estado | `transitionJiraIssue` |
| Comentar issue | `addCommentToJiraIssue` |
| Ver enlaces remotos | `getJiraIssueRemoteIssueLinks` |
| Crear enlaces entre issues | `createIssueLink` |
| Buscar documentación | `searchConfluenceUsingCql` o Rovo Search |
| Leer página Confluence | `getConfluencePage` |

Regla: si el usuario da un enlace concreto de Jira o Confluence, leerlo antes de actuar.

---

## 21. Patrones observados en el proyecto AA

Epics relevantes detectadas:

```text
AA-86  — TRACKER DOCUMENTACIÓN
AA-94  — BACKLOG PETICIONES
AA-243 — AGENTES IA
AA-268 — Facturación artículosd
AA-222 — Business Operations Agent
AA-258 — Agente ventas UDAVINCI
AA-225 — Triaje Tickets soporte
AA-19  — Elevenlabs
AA-83  — Scraping empresas - Empleo
AA-193 — Automatizacion flujos CAPMAN
AA-43  — Ia correctiva - Hawkings
AA-147 — Automatización correos Google
AA-135 — Automatización registro correos
AA-20  — N8n- seguimiento y bienvenida
AA-100 — Automatización reseñas
AA-161 — Agente reuniones
AA-21  — IA resolutiva Callbell
```

Patrones reales:

- Muchas iniciativas de automatización nacen como Epics.
- Las fichas de automatización suelen acabar en `AA-86 TRACKER DOCUMENTACIÓN`.
- Algunas tareas se dejan temporalmente en la Epic de origen para preservar contexto y luego se mueven al tracker documental.
- Cuando una tarea depende de Word, SharePoint o Miro, debe enlazar la fuente.
- Cuando una tarea pide pasar información a Confluence, debe aplicarse la skill de Confluence.

---

## 22. Errores comunes a evitar

- Crear varias iniciativas dentro de una misma Epic.
- Crear una Epic sin `tipo-proyecto` o `tipo-quickwin`.
- Marcar como completada una tarea documental sin enlace a Confluence.
- Usar `DIAGNOSTICO` para proponer soluciones.
- Usar `REDISEÑO` para ejecutar soluciones.
- Pasar a Tecnología sin reglas de negocio o flujo mínimo.
- Renombrar una Epic cuando cambia el alcance; mejor dejar comentario.
- Eliminar Epics canceladas; mover a backlog y explicar en comentario.
- Crear tareas genéricas sin entregables ni criterios de aceptación.
- Inventar owners, fechas, enlaces o estados.

---

## 23. Formato de salida recomendado

Cuando el usuario pida preparar una tarea o Epic, responder con:

```markdown
## Propuesta para Jira

**Tipo de issue:** Epic / Tarea / Subtarea / Petición / Error  
**Proyecto:** AA — OPERATIONS  
**Parent/Epic:** AA-XXX — [Nombre]  
**Etiqueta recomendada:** `tipo-proyecto` / `tipo-quickwin` / `tipo-proceso` / `tipo-documento`  
**Estado inicial:** PENDIENTE

### Título
[Resumen claro]

### Descripción
[Texto listo para copiar en Jira]

### Criterios de aceptación
- 

### Enlaces necesarios
- Confluence:
- SharePoint/Miro/Word:

### Comentarios o dudas
- 
```

Cuando el usuario pida auditar el board, responder con:

```markdown
## Revisión Jira — Proyecto AA

### Hallazgos principales
- 

### Riesgos de seguimiento/KPI
- 

### Issues que conviene corregir
| Issue | Problema | Acción recomendada |
|---|---|---|

### Próximos pasos recomendados
1. 
2. 
3. 
```

---

## 24. Regla final

Jira no debe usarse solo como lista de tareas. En el proyecto OPERATIONS, Jira debe permitir responder:

```text
Qué iniciativa existe,
por qué existe,
en qué estado está,
quién la tiene,
qué documentación la soporta,
qué falta para avanzar,
y cuándo puede considerarse terminada.
```

Si un issue no responde a esas preguntas mínimas, debe mejorarse antes de considerarse bien configurado.
