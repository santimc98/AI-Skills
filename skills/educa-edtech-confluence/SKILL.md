---
name: educa-edtech-confluence
description: "Use this skill whenever Santi (Educa Edtech) asks to create, edit, update, audit, structure or publish pages in Confluence for the OPERACIONES space. Triggers: 'crea una página', 'actualiza en Confluence', 'documenta el proceso', 'plantilla de proceso', 'plantilla de automatización', 'APTs', 'descripción área', 'añade en el wiki', 'sube a Confluence', 'documentación del equipo', 'diagnóstico', 'rediseño', 'Knowledge Core', or any request to write documentation for Educa Edtech. Covers processes, automations, APTs, area descriptions, FAQs, KPIs, risks, reporting, project pages and operational documentation. Always search/read before creating or editing, use the correct template, respect metadata, taxonomy, page state and Jira linkage rules."
---

# Confluence · Educa Edtech — Cómo trabajar con el espacio OPERACIONES

Esta skill define cómo trabajar con la documentación del equipo de **Operaciones / Business Operations & AI** en Confluence. Está basada en la documentación interna del espacio **OPERACIONES** y debe usarse antes de crear, editar, reorganizar o revisar cualquier página del equipo.

---

## 1. Datos de conexión

| Campo | Valor |
|---|---|
| Sitio | `educaedtech.atlassian.net` |
| Cloud ID | `7ba28d00-0b5a-4689-81b8-d07ff3c1272e` |
| Espacio principal | **OPERACIONES** |
| Space key | `AA1` |
| Space ID | `1574699012` |
| Homepage ID | `1574699212` |

---

## 2. Principios del área de Operaciones

El área de Operaciones es transversal. No actúa como soporte reactivo ni como helpdesk. Su función es asegurar que la organización funcione con orden, coherencia y escalabilidad.

Pilares del área:

1. **Conexión entre estrategia, procesos y tecnología**  
   Alinear lo que se decide estratégicamente con cómo se ejecuta y con las herramientas que lo soportan.

2. **Estructura y orden del sistema empresarial**  
   Construir una fuente oficial de información que formalice procesos, decisiones y métricas clave, evitando dependencia de conocimiento implícito de personas concretas.

3. **Eficiencia operativa con mayor peso tecnológico**  
   Identificar fricciones, duplicidades y dependencias estructurales para transformarlas en procesos más simples, estandarizados y apoyados en tecnología.

---

## 3. Estructura real actual del espacio AA1

Antes de crear una página, identificar en qué carpeta real del árbol debe vivir.

| Carpeta real | Uso recomendado |
|---|---|
| **GENERAL** | Bienvenida, instrucciones, onboarding, metodología, accesos, playbook y documentación interna base |
| **AUTOMATIZACIONES** | Automatizaciones, agentes, quick wins automatizados, procesos ETL, bots y soluciones IA operativas |
| **DOCUMENTACIÓN** | Knowledge core, trackers documentales y documentación transversal embebida |
| **PROYECTOS** | Proyectos activos/cerrados, auditorías, CAPMAN, quick wins y organización de iniciativas |
| **DATA Y REPORTING INTERNO** | KPIs, dashboards, reporting, data trackers y medición interna |
| **IA** | Estrategia IA, agentes, licencias IA, LibreChat y documentación tecnológica relacionada con IA |
| **TECNOLOGÍA** | Documentación técnica, sistemas, infraestructura y coordinación tecnológica cuando aplique |

---

## 4. Estructura conceptual del método

La documentación interna también usa una arquitectura conceptual. Si hay conflicto entre el árbol real y la estructura conceptual, priorizar el árbol real para ubicar la página y la estructura conceptual para entender el propósito.

| Sección conceptual | Qué contiene |
|---|---|
| 01 · Playbook del Área | Todo lo que define cómo es y cómo funciona el área |
| 02 · Cómo Trabajamos | Metodología, Jira, accesos y normas operativas |
| 03 · Medición | KPIs, instrucciones de actualización y reportes mensuales |
| 04 · Documentación | Todas las plantillas disponibles para documentar |
| 05 · Proyectos | Fichas de proyectos activos y cerrados |
| 06 · Sección adicional | Contenido específico cuando aplique |

---

## 5. Páginas internas de referencia

Consultar estas páginas cuando la tarea lo requiera:

| Página | ID | Uso |
|---|---:|---|
| Instrucciones Confluence — Operaciones | `1684307979` | Reglas oficiales de creación, nomenclatura, metadatos, etiquetas y mantenimiento |
| Instrucciones de Jira — Operaciones | `1645772816` | Reglas de Epics, issues, estados, etiquetas y trazabilidad Jira-Confluence |
| Documentacion Interna | `1576271873` | Índice de plantillas y conocimiento interno |
| IDs de procesos y automatizaciones | `1692729373` | Control de IDs `PRO-XXX-ÁREA` y `AUT-XXX` |
| Plantilla documentacion procesos | `1637515274` | Plantilla oficial para procesos operativos |
| Plantilla automatización | `1638039573` | Plantilla oficial para automatizaciones |
| Plantilla APTs | `1638268929` | Plantilla oficial para puestos de trabajo |
| Plantilla descripción área y objetivos | `1637613737` | Plantilla oficial para descripción de áreas |
| Taxonomía y etiquetas | `1639645195` | Reglas de labels, dominios, seguridad, estado, nivel y anillos |

---

## 6. Regla de oro antes de crear o editar

Antes de crear o modificar una página:

1. Buscar si ya existe contenido similar en el espacio.
2. Leer la página existente si puede verse afectada.
3. Identificar la carpeta correcta del árbol real.
4. Identificar la plantilla oficial aplicable.
5. Verificar si debe existir tarea, Epic o vínculo en Jira.
6. No modificar información real sin confirmación explícita del usuario.

---

## 7. Reglas de nomenclatura de páginas

El nombre debe ser autónomo y descriptivo. Una persona debe entender qué contiene la página sin contexto adicional.

| Tipo de documento | Formato recomendado |
|---|---|
| Descripción y Objetivos | `[Área] — Descripción y Objetivos` |
| APTs | `[Área] — APTs` |
| Proceso | `Documentación de Procesos — [Nombre del proceso]` |
| Automatización | `Automatización — [Nombre]` |
| Herramienta | `Herramienta — [Nombre]` |
| Proyecto | `Proyecto — [Nombre del proyecto]` |
| Acta | `Acta — [Tema] — [AAAA-MM-DD]` |
| Reporte | `Reporte — [Período] — [Área]` |

Normas generales:

- Usar siempre el guión largo `—` como separador.
- No usar abreviaturas salvo las del Glosario Corporativo.
- No incluir número de versión en el título; la versión va en metadatos.
- No incluir fechas salvo en reportes y actas.
- Si hay conflicto entre una guía de nomenclatura y una plantilla oficial vigente, priorizar la plantilla oficial vigente.

---

## 8. Estructura obligatoria de una página

Toda página operativa debe seguir esta estructura mínima:

1. **Bloque de metadatos** al inicio.
2. **Párrafo introductorio autónomo**; en Confluence debe prepararse como panel o bloque destacado cuando sea posible.
3. Secciones con encabezados H2 y H3.
4. Contenido organizado con tablas cuando facilite la lectura.
5. Histórico de cambios al final, salvo páginas índice.

---

## 9. Bloque de metadatos obligatorio

Toda página debe empezar con un bloque de metadatos.

Formato general:

```markdown
> **Comisión:** [Nombre de la comisión]
> **Área:** [Nombre del área exacto según Glosario]
> **Owner:** [Nombre completo / Cargo]
> **Anillo de seguridad:** [Anillo 1 / 2 / 3 / 4]
> **Versión:** v1.0
> **Última actualización:** AAAA-MM-DD
```

Normas:

| Campo | Norma |
|---|---|
| Comisión | Usar nombre exacto, sin abreviaturas propias |
| Área | Usar nombre exacto según Glosario/Knowledge Core |
| Owner | Nombre completo y cargo cuando sea necesario en documentación interna; en repositorio público usar rol funcional si basta |
| Anillo | Definido por la política de accesos; si hay duda, consultar al owner responsable |
| Versión | `v1.0` inicial; cambio menor `v1.1`; reestructuración `v2.0` |
| Última actualización | Actualizar siempre que se modifique contenido |

---

## 10. Sistema de etiquetas y taxonomía

### 10.1 Etiquetas obligatorias para procesos y automatizaciones

| Tipo de documento | Etiqueta obligatoria |
|---|---|
| Ficha de proceso | `proceso` |
| Automatización completa | `automatizacion` |

Sin estas etiquetas, el documento no se contabiliza correctamente en los IDs de procesos y automatizaciones.

Reglas:

- Añadir la etiqueta en el momento de creación de la página.
- Mantenerla aunque el documento pase a archivado u obsoleto.
- Usar exactamente `proceso` o `automatizacion`, sin variantes.

### 10.2 Taxonomía oficial del Knowledge Core

Cuando aplique, usar etiquetas controladas con prefijo. No inventar variantes.

| Dimensión | Prefijo | Ejemplos |
|---|---|---|
| Dominio / Equipo | `dom-` | `dom-operaciones`, `dom-finance`, `dom-rrhh`, `dom-transversal` |
| Seguridad | `sec-` | `sec-publico`, `sec-interno`, `sec-restringido`, `sec-confidencial` |
| Bloque estructural | `block-` | `block-modelo-operativo`, `block-tecnologia-sistemas`, `block-datos-metricas` |
| Estado | `status-` | `status-borrador`, `status-en-revision`, `status-aprobado`, `status-obsoleto` |
| Nivel | `level-` | `level-estrategico`, `level-operativo`, `level-tecnico` |
| Anillo de seguridad | `ring-` | `ring-1`, `ring-2`, `ring-3`, `ring-4` |

Reglas generales de etiquetas:

- Minúsculas.
- Sin tildes.
- Con guiones.
- Vocabulario controlado.
- Una única etiqueta `ring-` por documento.
- La etiqueta `ring-` debe coincidir con las restricciones reales de la página.

---

## 11. Estados de documentación

Al crear o revisar una página:

- Mientras esté en construcción, tratarla como borrador o pendiente de revisión.
- Cuando esté completa y validada, marcarla como `estado-verificada` si el flujo de Confluence lo permite.
- Si el cambio es estructural, devolverla a borrador hasta validación del Owner.
- No marcar una página como verificada si faltan metadatos, etiquetas o histórico de cambios.

---

## 12. IDs de documentos

| Tipo | Formato de ID | Ejemplo |
|---|---|---|
| Proceso | `PRO-[NNN]-[ÁREA]` | `PRO-001-OPS` |
| Automatización | `AUT-[NNN]` | `AUT-001` |

Antes de asignar un nuevo ID:

1. Consultar la página `IDs de procesos y automatizaciones`.
2. Verificar que no existe ya una ficha equivalente.
3. Mantener numeración consecutiva.
4. No reutilizar IDs antiguos aunque una página esté obsoleta.

---

## 13. Definición de Owners

**Owner Funcional**  
Responsable del proceso desde el punto de vista del negocio. Sabe para qué sirve la automatización o proceso, qué resultado debe dar y cuándo algo no funciona bien operativamente.

- Es la persona o rol del área propietaria del proceso.
- No tiene por qué ser de Operaciones.
- Valida que el resultado responde a la necesidad de negocio.

**Owner Técnico**  
Responsable de que la automatización funcione técnicamente. Sabe cómo está construida, puede modificarla y resuelve fallos técnicos.

- Suele pertenecer a Tecnología u Operaciones.
- Mantiene el artefacto técnico.
- Responde ante fallos de ejecución, integración o infraestructura.

Regla práctica:

- Resultado incorrecto desde negocio → Owner Funcional.
- Fallo técnico o no ejecución → Owner Técnico.

---

## 14. Integración Jira-Confluence

El trabajo del equipo conecta documentación en Confluence con ejecución en Jira.

### 14.1 Reglas generales de Jira

- El proyecto de Operaciones se organiza por **Epics**.
- Cada Epic representa una iniciativa, proyecto o quick win.
- Existe un Epic especial **TRACKER DOCUMENTACION** para tareas documentales.
- Todo Epic debe tener etiqueta `tipo-proyecto` o `tipo-quickwin`.
- Las tareas específicas de proceso o documentación pueden usar `tipo-proceso` o `tipo-documento`.
- No agrupar varias iniciativas en una misma Epic.
- No eliminar Epics; si se cancela una iniciativa, moverla a backlog y dejar comentario.
- Enlazar siempre la página de Confluence en la tarea Jira correspondiente.

### 14.2 Estados relevantes

| Estado | Uso |
|---|---|
| `PENDIENTE` | Iniciativa o documento identificado pero no iniciado |
| `DIAGNOSTICO` | Se observa y documenta el proceso AS-IS; no se propone solución todavía |
| `REDISEÑO` | Se diseña TO-BE, flujo, reglas de negocio y viabilidad técnica; no se ejecuta todavía |
| `EN CURSO` | Iniciativa en ejecución |
| `BLOQUEADO` | Dependencia externa impide avanzar |
| `TESTEO` | Ejecutado y pendiente de pruebas |
| `COMPLETADO` | Finalizado, revisado y en producción/publicado |

### 14.3 Cuándo crear o vincular Jira

Si una página documenta un proceso, automatización, diagnóstico, rediseño, proyecto o trabajo accionable:

1. Comprobar si existe Epic o Task relacionada.
2. Enlazar la página de Confluence en la tarea.
3. Si no existe y el usuario pide gestionarlo, proponer Epic/Task con título, descripción y criterios de aceptación.
4. No crear ni modificar issues sin confirmación explícita.

### 14.4 Tecnología

Cuando una iniciativa pasa a Tecnología:

- La Epic suele asignarse al responsable de Tecnología designado por el equipo.
- Las tareas con documentos importantes para Tecnología deben enlazarse a la Epic.
- Documentos críticos para Tecnología: reglas de negocio, flujos, documentación técnica, requisitos y validación de viabilidad.

---

## 15. PLANTILLA: Documentación de Procesos

Usar para documentar procesos operativos (`PRO-XXX-ÁREA`).
Página de referencia en Confluence: `1637515274`.

```markdown
# Documentación de Procesos — [NOMBRE DEL PROCESO]

> **Comisión:** [Nombre de la comisión]
> **Área:** [Nombre del área]
> **ID del proceso:** PRO-[XXX]-[ÁREA]
> **Anillo de seguridad:** [Anillo 1 / 2 / 3 / 4]
> **Versión:** v1.0
> **Fecha de creación:** AAAA-MM-DD
> **Owner:** [Nombre y cargo, o rol funcional si se documenta en repositorio público]

---

[Panel introductorio autónomo: 2-4 frases que expliquen qué es este proceso, qué problema de negocio resuelve y qué valor aporta. Debe entenderse sin contexto previo.]

---

## 1. Descripción general

[2-4 frases: qué es, qué problema resuelve, qué valor aporta. Autónomo sin contexto.]

---

## 2. Ficha de Identificación del Proceso

| Campo | Detalle |
|---|---|
| Nombre del proceso | [Nombre descriptivo] |
| Propósito / Objetivo | [¿Para qué existe? ¿Qué problema resuelve?] |
| Dónde empieza (Trigger) | [Evento que dispara el proceso] |
| Dónde termina (Output) | [Resultado final] |
| Process Owner | [Cargo/rol responsable estratégico] |
| Ejecutor principal (AS IS) | [Cargo/rol del que lo ejecuta] |
| Frecuencia de ejecución | [Puntual / Diaria / Semanal / Mensual / Por evento] |
| Volumen estimado | [Nº veces por ejecución o período] |
| Impacto en el negocio | [Impacto de automatizarlo en tiempo, dinero o calidad] |

---

## 3. Mapa de Pasos Operativos (AS-IS)

| Descripción de la acción | Herramienta / Módulo | Responsable | Tipo de tarea | Observaciones |
|---|---|---|---|---|
| | | | Manual / Semi-auto / Auto | |

---

## 4. Lógica del proceso (TO BE)

### 4.1 Comportamiento esperado (happy path)
[Flujo completo cuando todo funciona: desde trigger hasta output.]

### 4.2 Diagrama de flujo
[Enlace y/o captura]

### 4.3 Reglas funcionales
- Regla 1
- Regla 2

### 4.4 Documentos asociados
[Links a otras páginas vinculadas]

---

## 5. Flujo de datos

### 5.1 Inputs
| Dato / Campo | Descripción | Sistema origen |
|---|---|---|

### 5.2 Outputs
| Dato / Resultado | Descripción | Sistema destino |
|---|---|---|

---

## 6. Sistemas y herramientas

| Sistema / Herramienta | Rol en la automatización | Tipo de conexión | Responsable del acceso |
|---|---|---|---|

---

## 7. Carga operativa

| Métrica | AS-IS | Fuente |
|---|---|---|
| Frecuencia de ejecución | | |
| Horas totales al mes | | |
| Nº personas involucradas | | |
| % tiempo manual vs auto | | |
| Coste estimado mensual | | |
| Ahorro estimado | | |

---

## 8. Métricas y KPIs

| KPI / Métrica | Descripción | Fórmula | Fuente |
|---|---|---|---|

---

## 9. Riesgos

### Riesgos cualitativos
| Riesgo | Descripción | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|

### Riesgos cuantitativos
| Riesgo | Descripción | Probabilidad | Impacto económico | Mitigación |
|---|---|---|---|---|

---

## 10. Aprobación del Proceso

Las partes negocio y tecnología confirman que han revisado y están de acuerdo con el contenido del documento, la propuesta TO-BE y el alcance acordado.

**Observaciones MONTEVIVE:**

---

## 11. Histórico de Cambios

| Versión | Fecha | Autor | Descripción |
|---|---|---|---|
| v1.0 | AAAA-MM-DD | [Nombre o rol] | Creación inicial |
```

---

## 16. PLANTILLA: Automatización

Usar para documentar automatizaciones (`AUT-XXX`).
Página de referencia en Confluence: `1638039573`.

```markdown
# Automatización — [NOMBRE DE LA AUTOMATIZACIÓN]

> **Comisión:** [Nombre de la comisión]
> **Área:** [Nombre del área]
> **ID de automatización:** AUT-[XXX]
> **Proceso vinculado:** PRO-[XXX]-[ÁREA]
> **Anillo de seguridad:** [Anillo 1 / 2 / 3 / 4]
> **Versión:** v1.0
> **Fecha creación:** AAAA-MM-DD
> **Owner técnico:** [Nombre / Cargo, o rol funcional si se documenta en repositorio público]
> **Owner funcional:** [Nombre / Cargo — responsable del proceso de negocio, o rol funcional si se documenta en repositorio público]
> **Estado:** [Activa / En desarrollo / Pausada / Deprecada]

---

[Panel introductorio autónomo: 2-4 frases que expliquen qué hace la automatización, qué problema resuelve y qué valor aporta.]

---

## 1. Descripción General

[2-4 frases autónomas: qué hace, qué problema resuelve, qué valor aporta.]

---

## 2. Ficha de Identificación del Proceso

| Campo | Detalle |
|---|---|
| Nombre del proceso | |
| Propósito / Objetivo | |
| Dónde empieza (Trigger) | |
| Dónde termina (Output) | |
| Process Owner | |
| Ejecutor principal | |
| Frecuencia de ejecución | |
| Volumen estimado | |

---

## 3. Flujo de Datos

| ID AUTOMATIZACIÓN | AUTO-XXX |
|---|---|

### 3.1 Inputs
| Dato / Campo | Descripción | Sistema origen |
|---|---|---|

### 3.2 Outputs
| Dato / Resultado | Descripción | Sistema destino |
|---|---|---|

---

## 4. Lógica del proceso

### 4.1 Comportamiento esperado (happy path)
[Flujo paso a paso cuando todo funciona.]

### 4.2 Diagrama de flujo
[Enlace y captura]

### 4.3 Reglas funcionales
- Regla 1
- Regla 2

---

## 5. Sistemas y herramientas

| Sistema / Herramienta | Rol en la automatización | Tipo de conexión | Responsable |
|---|---|---|---|

---

## 6. Métricas y KPIs

| KPI / Métrica | Descripción | Fórmula de cálculo | Fuente de datos |
|---|---|---|---|

---

## 7. Mantenimiento y Responsabilidades

| Campo | Detalle |
|---|---|
| Owner técnico | |
| Owner funcional | |
| Frecuencia de revisión | |
| Dependencias críticas | |
| Última revisión técnica | AAAA-MM-DD |
| Próxima revisión programada | AAAA-MM-DD |

---

## 8. Histórico de Cambios

| Versión | Fecha | Autor | Descripción del cambio |
|---|---|---|---|
| v1.0 | AAAA-MM-DD | [Nombre o rol] | Creación inicial |
```

---

## 17. PLANTILLA: APTs

Usar para documentar puestos de trabajo. Página de referencia: `1638268929`.

```markdown
# [NOMBRE DEL ÁREA] — APTs

> **Comisión:** [Nombre]
> **Área:** [Nombre]
> **Anillo de seguridad:** [Anillo]
> **Owner:** [Nombre / Cargo, o rol funcional si se documenta en repositorio público]
> **Versión:** v1.0
> **Última actualización:** AAAA-MM-DD

---

[Panel introductorio autónomo: explicar qué contiene la página y para qué sirve.]

---

## Puesto — [NOMBRE DEL PUESTO]

| Campo | Detalle |
|---|---|
| Nombre del puesto | [Nombre oficial] |
| Área | [Nombre del área] |
| Tipo de puesto | [Directivo / Manager / Técnico] |
| Dependencia jerárquica | [Puesto al que reporta] |
| Descripción | [Misión del puesto en 2-3 frases] |

### Responsabilidades principales
- 

### Competencias requeridas
- 

### Herramientas que usa
- 

---

## Histórico de Cambios

| Versión | Fecha | Autor | Descripción |
|---|---|---|---|
| v1.0 | AAAA-MM-DD | [Nombre o rol] | Creación inicial |
```

---

## 18. PLANTILLA: Descripción y Objetivos del Área

Página de referencia: `1637613737`.

```markdown
# [NOMBRE DEL ÁREA] — Descripción y Objetivos

> **Comisión:** [Nombre]
> **Área:** [Nombre]
> **Anillo de seguridad:** [Anillo]
> **Owner:** [Nombre / Cargo, o rol funcional si se documenta en repositorio público]
> **Versión:** v1.0
> **Última actualización:** AAAA-MM-DD

---

[Panel introductorio autónomo: explicar qué es el área, qué valor aporta y qué encontrará el lector en la página.]

---

## 1. Misión y visión del área
[Propósito fundamental: por qué existe, a quién sirve, qué valor aporta.]

## 2. Objetivos
[Objetivos estratégicos del área]

## 3. Estructura del equipo
[Organigrama o descripción de roles]

## 4. Procesos principales
[Lista de procesos clave]

## 5. Herramientas
[Herramientas principales del área]

---

## Histórico de Cambios

| Versión | Fecha | Autor | Descripción |
|---|---|---|---|
| v1.0 | AAAA-MM-DD | [Nombre o rol] | Creación inicial |
```

---

## 19. Flujo de trabajo al crear una página

1. Buscar si ya existe una página equivalente.
2. Leer la página o plantilla de referencia si existe.
3. Identificar carpeta real del árbol.
4. Elegir plantilla oficial.
5. Crear la página en la ubicación correcta.
6. Añadir metadatos antes de escribir el contenido.
7. Añadir panel introductorio autónomo.
8. Completar secciones H2/H3.
9. Añadir etiquetas obligatorias y taxonomía aplicable.
10. Añadir histórico de cambios.
11. Enlazar con Jira si corresponde.
12. Pedir confirmación antes de publicar o modificar información real.
13. Una vez validada, marcar como `estado-verificada` si aplica.

---

## 20. Flujo de trabajo al actualizar una página

1. Leer la versión actual.
2. Identificar el cambio solicitado.
3. Mantener estructura, metadatos y estilo existente salvo que el usuario pida reestructurar.
4. Actualizar `Última actualización` con la fecha de hoy.
5. Incrementar versión si el cambio es relevante.
6. Añadir línea en Histórico de Cambios.
7. Si cambia estructura, alcance, owner, anillo o contenido crítico, tratar como borrador hasta validación del Owner.
8. No eliminar contenido histórico sin confirmación explícita.

---

## 21. Herramientas disponibles

Usar Atlassian Rovo cuando esté disponible.

| Acción | Herramienta orientativa |
|---|---|
| Buscar páginas o contenido | Search Confluence with CQL / Rovo Search Jira and Confluence |
| Leer una página | Retrieve Confluence page / Fetch content with ARI |
| Crear página | Create Confluence page |
| Actualizar página | Update Confluence page |
| Buscar issues | Search with JQL |
| Leer issue | Get issue |
| Crear issue | Create issue |
| Actualizar issue | Update issue |
| Transicionar issue | Transition issue |

Regla de seguridad: para crear, actualizar, comentar o transicionar en sistemas reales, pedir confirmación explícita si la acción puede modificar información visible por el equipo.

---

## 22. Checklist de calidad antes de entregar

Antes de entregar una página o propuesta de actualización:

- [ ] ¿Está en la carpeta correcta?
- [ ] ¿Sigue la plantilla oficial?
- [ ] ¿Tiene metadatos completos?
- [ ] ¿Tiene panel introductorio autónomo?
- [ ] ¿Usa títulos H2/H3 claros?
- [ ] ¿Tiene labels obligatorias?
- [ ] ¿Respeta taxonomía `dom-`, `sec-`, `block-`, `status-`, `level-`, `ring-` cuando aplica?
- [ ] ¿Incluye histórico de cambios?
- [ ] ¿Enlaza con Jira si corresponde?
- [ ] ¿Distingue hechos, supuestos y recomendaciones?
- [ ] ¿Evita inventar owners, fechas, IDs o estados?
- [ ] ¿Evita almacenar emails corporativos y nombres personales innecesarios en repositorios públicos?
