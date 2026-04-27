---
name: educa-edtech-confluence
description: "Use this skill whenever Santi (Educa Edtech) asks to create, edit, update or structure pages in Confluence. Triggers: 'crea una página', 'actualiza en Confluence', 'documenta el proceso', 'plantilla de proceso/automatización/APTs/descripción área', 'añade en el wiki', 'sube a Confluence', any request to write documentation for Educa Edtech. Covers all document types in the OPERACIONES space (AA1): processes, automations, APTs, area descriptions, weekly reports. Always follow the naming rules, metadata structure, and templates defined here before creating or editing anything."
---

# Confluence · Educa Edtech — Cómo trabajar con el espacio

## Datos de conexión

| Campo | Valor |
|---|---|
| Sitio | `educaedtech.atlassian.net` |
| Cloud ID | `7ba28d00-0b5a-4689-81b8-d07ff3c1272e` |
| Espacio principal | **OPERACIONES** — key `AA1`, spaceId `1574699012` |

---

## Estructura del espacio AA1

El espacio está organizado en 6 secciones fijas. Antes de crear una página, identifica en qué sección debe vivir:

| Sección | Contenido |
|---|---|
| 01 · Playbook del Área | Todo lo que define cómo es y cómo funciona el área |
| 02 · Cómo Trabajamos | Metodología, Jira, accesos y normas operativas |
| 03 · Medición | KPIs, instrucciones de actualización y reportes mensuales |
| 04 · Documentación | Todas las plantillas disponibles para documentar |
| 05 · Proyectos | Fichas de proyectos activos y cerrados |
| 06 · [Sección adicional] | Si aplica |

---

## Reglas de nomenclatura de páginas

El nombre debe ser autónomo y descriptivo. Formato por tipo:

| Tipo de documento | Formato del título |
|---|---|
| Descripción y Objetivos | `[Área] — Descripción y Objetivos` |
| APTs | `[Área] — APTs` |
| Proceso | `Documentación de Procesos — [Nombre del proceso]` |
| Automatización | `Automatización — [Nombre]` |
| Herramienta | `Herramienta — [Nombre]` |
| Proyecto | `Proyecto — [Nombre del proyecto]` |
| Acta | `Acta — [Tema] — [AAAA-MM-DD]` |
| Reporte | `Reporte — [Período] — [Área]` |

**Normas generales:**
- Usar siempre el guión largo `—` como separador (no `-`)
- Sin abreviaturas salvo el Glosario Corporativo
- Sin números de versión en el nombre
- Sin fechas salvo en reportes y actas

---

## Bloque de metadatos obligatorio

**Toda página debe empezar con este bloque:**

```
> **Comisión:** [Nombre de la comisión]
> **Área:** [Nombre del área exacto]
> **Owner:** [Nombre completo / Cargo]
> **Anillo de seguridad:** [Anillo 1 / 2 / 3 / 4]
> **Versión:** v1.0
> **Última actualización:** AAAA-MM-DD
```

**Versiones:** menor (v1.1) para cambios de contenido, mayor (v2.0) para reestructuraciones.

---

## Sistema de etiquetas (labels)

| Tipo de documento | Etiqueta obligatoria |
|---|---|
| Ficha de proceso | `proceso` |
| Automatización completa | `automatizacion` |

Sin esta etiqueta el documento no se contabiliza en los IDs. Añadir siempre al crear la página.

---

## IDs de documentos

| Tipo | Formato de ID |
|---|---|
| Proceso | `PRO-[NNN]-[ÁREA]` ej: `PRO-001-OPS` |
| Automatización | `AUT-[NNN]` ej: `AUT-001` |

---

## Definición de Owners

**Owner Funcional** — Responsable del proceso desde el negocio. Valida que el resultado es correcto. Es la persona del área propietaria del proceso, no de Operaciones.

**Owner Técnico** — Responsable técnico de que la automatización funcione. La mantiene y la arregla si falla. Es de Tecnología u Operaciones.

Regla práctica:
- ¿Resultado incorrecto? → Owner Funcional
- ¿Fallo técnico? → Owner Técnico

---

## PLANTILLA: Documentación de Procesos

Usar para documentar procesos operativos (ficheros tipo `PRO-XXX-ÁREA`).
**Página de referencia en Confluence:** ID `1637515274`

```markdown
# Documentación de Procesos — [NOMBRE DEL PROCESO]

> **Comisión:** [Nombre de la comisión]
> **Área:** [Nombre del área]
> **ID del proceso:** PRO-[XXX]-[ÁREA]
> **Anillo de seguridad:** [Anillo 1 / 2 / 3 / 4]
> **Versión:** v1.0
> **Fecha de creación:** AAAA-MM-DD
> **Owner:** [Nombre y cargo]

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
| Process Owner | [Cargo/nombre responsable estratégico] |
| Ejecutor principal (AS IS) | [Cargo/nombre del que lo ejecuta] |
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

### Cualitativos
| Riesgo | Descripción | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|

### Cuantitativos
| Riesgo | Descripción | Probabilidad | Impacto económico | Mitigación |
|---|---|---|---|---|

---

## 10. Aprobación del Proceso
Observaciones MONTEVIVE: [dejar en blanco hasta revisión]
```

---

## PLANTILLA: Automatización

Usar para documentar automatizaciones (ficheros tipo `AUT-XXX`).
**Página de referencia en Confluence:** ID `1638039573`

```markdown
# Automatización — [NOMBRE DE LA AUTOMATIZACIÓN]

> **Comisión:** [Nombre de la comisión]
> **Área:** [Nombre del área]
> **ID de automatización:** AUT-[XXX]
> **Proceso vinculado:** PRO-[XXX]-[ÁREA]
> **Anillo de seguridad:** [Anillo 1 / 2 / 3 / 4]
> **Versión:** v1.0
> **Fecha creación:** AAAA-MM-DD
> **Owner técnico:** [Nombre / Cargo]
> **Owner funcional:** [Nombre / Cargo]
> **Estado:** [Activa / En desarrollo / Pausada / Deprecada]

---

## 1. Descripción General
[2-4 frases autónomas: qué hace, qué problema resuelve, qué valor aporta.]

---

## 2. Ficha de Identificación

| Campo | Detalle |
|---|---|
| Nombre del proceso | |
| Propósito / Objetivo | |
| Trigger | |
| Output | |
| Process Owner | |
| Ejecutor principal | |
| Frecuencia | |
| Volumen estimado | |

---

## 3. Flujo de Datos

ID AUTOMATIZACIÓN: `AUTO-XXX`

### Inputs
| Dato / Campo | Descripción | Sistema origen |
|---|---|---|

### Outputs
| Dato / Resultado | Descripción | Sistema destino |
|---|---|---|

---

## 4. Lógica del proceso

### 4.1 Happy path
[Flujo paso a paso cuando todo funciona.]

### 4.2 Diagrama de flujo
[Enlace]

### 4.3 Reglas funcionales
- Regla 1

---

## 5. Sistemas y herramientas

| Sistema | Rol | Tipo de conexión | Responsable |
|---|---|---|---|

---

## 6. Métricas y KPIs

| KPI | Descripción | Fórmula | Fuente |
|---|---|---|---|

---

## 7. Mantenimiento y Responsabilidades

| Campo | Detalle |
|---|---|
| Owner técnico | |
| Owner funcional | |
| Frecuencia de revisión | |
| Dependencias críticas | |
| Última revisión técnica | |
| Próxima revisión programada | |

---

## 8. Histórico de Cambios

| Versión | Fecha | Autor | Descripción |
|---|---|---|---|
| v1.0 | AAAA-MM-DD | [Nombre] | Creación inicial |
```

---

## PLANTILLA: APTs

Usar para documentar puestos de trabajo. **Página de referencia:** ID `1638268929`

```markdown
# [NOMBRE DEL ÁREA] — APTs

> **Comisión:** [Nombre]
> **Área:** [Nombre]
> **Anillo de seguridad:** [Anillo]
> **Owner:** [Nombre / Cargo]
> **Versión:** 1.0
> **Última actualización:** AAAA-MM-DD

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
- 

### Competencias requeridas
- 

### Herramientas que usa
- 
```

---

## PLANTILLA: Descripción y Objetivos del Área

**Página de referencia:** ID `1637613737`

```markdown
# [NOMBRE DEL ÁREA] — Descripción y Objetivos

> **Comisión:** [Nombre]
> **Área:** [Nombre]
> **Anillo de seguridad:** [Anillo]
> **Owner:** [Nombre / Cargo]
> **Versión:** 1.0
> **Última actualización:** AAAA-MM-DD

---

## 1. Misión y visión del área
[Propósito fundamental: por qué existe, a quién sirve, qué valor aporta.]

## 2. Objetivos
[Objetivos estratégicos del área]

## 3. Estructura del equipo
[Organigrama o descripción de roles]

## 4. Procesos principales
[Lista de los procesos clave]

## 5. Herramientas
[Herramientas principales del área]
```

---

## Flujo de trabajo al crear una página

1. Comprobar que no existe ya una página con ese contenido (buscar primero)
2. Identificar la sección del espacio donde debe vivir
3. Usar la plantilla correspondiente de este skill
4. Rellenar el bloque de metadatos **antes** de escribir nada más
5. Añadir las etiquetas obligatorias (`proceso` o `automatizacion` si aplica)
6. Publicar con estado `current`

---

## Flujo de trabajo al actualizar una página

1. Editar el contenido
2. Actualizar `Última actualización` con la fecha de hoy
3. Incrementar versión si el cambio es relevante
4. Añadir línea al Histórico de Cambios describiendo qué cambió

---

## Herramienta Atlassian disponible

Para buscar contenido existente usar: `Atlassian Rovo:search`  
Para leer una página: `Atlassian Rovo:fetch` con su ARI  
Para crear: `Atlassian Rovo:createConfluencePage` con `cloudId: 7ba28d00-0b5a-4689-81b8-d07ff3c1272e` y `spaceId: 1574699012`  
Para editar: `Atlassian Rovo:updateConfluencePage`
