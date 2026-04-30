---
name: educa-edtech-bpmn-miro-process-mapping
description: "Mapea procesos operativos, automatizaciones y diagnósticos AS-IS/TO-BE de Educa Edtech a partir de documentación de Confluence, entrevistas, notas o ejemplos previos de Miro. Usa esta skill cuando Santi o Kevin pidan crear, revisar, ordenar o preparar mapas de procesos en Miro, BPMN, swimlanes, mapas de fricción, documentación de procesos, automatizaciones, diagnóstico operativo, rediseño TO-BE o tableros visuales derivados de Confluence."
---

# Educa Edtech · BPMN & Miro Process Mapping

## Cuándo usar esta skill

Usar esta skill cuando la tarea implique transformar documentación, entrevistas, notas, tickets, automatizaciones o páginas de Confluence de Educa Edtech en un mapa de proceso preparado para Miro.

Activadores frecuentes:

- "mapea este proceso en Miro"
- "crea el AS-IS y TO-BE"
- "pasa esta documentación a BPMN"
- "haz el mapa de diagnóstico"
- "extrae actores, tareas y decisiones"
- "convierte esta automatización en un flujo visual"
- "prepara el tablero para Kevin"
- "revisa si este proceso está bien mapeado"
- "documenta el flujo desde Confluence"
- "saca fricciones, riesgos y oportunidades"

Esta skill debe combinarse con:

1. `skills/educa-edtech-confluence/SKILL.md` cuando la fuente o destino sea Confluence OPERACIONES (`AA1`).
2. `skills/educa-edtech-jira/SKILL.md` cuando el proceso deba derivar tareas, Epics, subtareas o vínculos Jira.
3. `skills/n8n-workflow-engineering/SKILL.md` cuando el proceso esté implementado o vaya a implementarse como workflow n8n.
4. `skills/meeting-notes/SKILL.md` cuando la fuente sean entrevistas, reuniones o notas sin estructurar.

---

## Objetivo

Convertir información funcional u operativa en una especificación visual clara y accionable para Miro, separando:

- Proceso actual **AS-IS**.
- Proceso futuro **TO-BE**.
- Actores, equipos y sistemas.
- Eventos de inicio y cierre.
- Tareas manuales, automáticas y semi-automáticas.
- Decisiones, reglas funcionales y excepciones.
- Inputs, outputs y flujo de datos.
- Fricciones, riesgos, dependencias y oportunidades de mejora.
- Elementos preparados para documentación Confluence y seguimiento Jira.

La salida debe permitir que Kevin o el equipo puedan crear o revisar el tablero Miro sin tener que reinterpretar la documentación desde cero.

---

## Fuentes internas de referencia

Consultar cuando estén disponibles en el entorno corporativo:

| Tipo | Referencia | Uso |
|---|---|---|
| Metodología | Confluence `AA1`, página `1702330377`, `Metodología - Mapa de diagnóstico` | Método de diagnóstico por capas: antes, durante y después de entrevistas; mapa de fricción y consolidación por área |
| Ejemplo de proceso | Confluence `AA1`, página `1757184001`, `Documentación de Procesos — Triaje tickets soporte` | Ejemplo completo con AS-IS, TO-BE, reglas funcionales, inputs, outputs, KPIs y riesgos |
| Ejemplo de automatización | Confluence `AA1`, página `1789886475`, `Automatización facturación artículos` | Referencia de automatización/proceso a contrastar si el contenido está disponible |
| Estilo Miro | Tableros internos de Miro aportados por Santi/Kevin | Estilo visual, estructura AS-IS/TO-BE, swimlanes y convenciones del equipo |

No copiar información sensible en repositorios públicos. Si se trabaja desde Claude empresarial, usar los enlaces privados aportados por Santi/Kevin como contexto de sesión o archivos internos, no como contenido público reutilizable.

---

## Entradas necesarias

Antes de mapear, recopilar lo máximo posible:

| Entrada | Obligatoria | Descripción |
|---|---:|---|
| Nombre del proceso o automatización | Sí | Nombre claro y autónomo |
| Fuente documental | Sí | Página Confluence, notas, entrevista, acta, workflow o descripción funcional |
| Objetivo del mapa | Sí | Diagnóstico, documentación AS-IS, rediseño TO-BE, automatización, validación o presentación |
| Alcance | Sí | Dónde empieza y dónde termina el proceso |
| Actores | Si disponible | Personas, roles, áreas o equipos que intervienen |
| Sistemas | Si disponible | Jira, Confluence, n8n, email, CRM, ERP, SharePoint, Supabase, LibreChat, etc. |
| Reglas de negocio | Si disponible | Condiciones, criterios, validaciones, etiquetas, derivaciones o políticas |
| Inputs / outputs | Si disponible | Datos que entran y resultados esperados |
| Ejemplo Miro de referencia | Recomendado | Tablero o captura cuyo estilo debe imitarse |
| Nivel de detalle | Recomendado | Ejecutivo, operativo, técnico o mixto |

Si falta información crítica, no inventarla. Marcarla como `Pendiente de confirmar`.

---

## Procedimiento paso a paso

### 1. Entender el propósito del mapa

Determinar qué se quiere conseguir:

- Diagnosticar fricciones.
- Documentar el estado actual.
- Diseñar un proceso futuro.
- Preparar una automatización.
- Validar reglas con negocio o tecnología.
- Crear un tablero visual para una reunión.

Indicar explícitamente el tipo de salida:

```text
Tipo de mapa: AS-IS / TO-BE / AS-IS + TO-BE / Mapa de diagnóstico / Automatización / BPMN / Swimlane
Audiencia: negocio / técnica / mixta / dirección
Nivel de detalle: alto / medio / bajo
```

### 2. Leer y descomponer la fuente

Extraer de la documentación:

- Trigger o evento inicial.
- Resultado final.
- Pasos secuenciales.
- Responsables por paso.
- Herramientas usadas.
- Datos que se crean, consultan o modifican.
- Decisiones.
- Excepciones.
- Riesgos.
- Métricas.
- Puntos manuales.
- Posibles automatizaciones.

No empezar a diseñar Miro hasta tener una tabla base de proceso.

### 3. Separar AS-IS y TO-BE

El AS-IS describe cómo ocurre hoy.

El TO-BE describe cómo debería funcionar tras mejora, automatización o rediseño.

No mezclar ambos en el mismo flujo sin etiquetarlos claramente.

| Vista | Pregunta guía |
|---|---|
| AS-IS | ¿Qué ocurre hoy realmente? |
| Fricciones | ¿Dónde hay carga manual, espera, error, dependencia o duplicidad? |
| TO-BE | ¿Cómo debería ocurrir de forma mejorada? |
| Automatización | ¿Qué pasos puede ejecutar un sistema o agente? |
| Control humano | ¿Dónde debe validar una persona? |

### 4. Identificar elementos BPMN/Miro

Convertir la información en elementos visuales:

| Elemento | Uso |
|---|---|
| Evento inicial | Qué dispara el proceso |
| Evento final | Resultado final del proceso |
| Tarea manual | Acción humana |
| Tarea automática | Acción ejecutada por sistema |
| Tarea semi-automática | Sistema ayuda, persona valida |
| Gateway / decisión | Punto donde el flujo se bifurca |
| Swimlane | Actor, área o sistema responsable |
| Data object | Documento, ticket, email, registro o dato relevante |
| Anotación | Regla, riesgo, fricción o pendiente |
| Subproceso | Bloque que merece detalle propio |

### 5. Construir la tabla maestra del proceso

Antes de proponer el tablero, generar una tabla como esta:

| ID | Fase | Paso | Actor / lane | Sistema | Tipo | Entrada | Salida | Regla / condición | Fricción / riesgo |
|---|---|---|---|---|---|---|---|---|---|
| P01 | Inicio | | | | Manual / Auto / Semi-auto | | | | |

Reglas:

- Cada paso debe tener un responsable.
- Cada decisión debe tener salidas posibles.
- Cada automatización debe indicar sistema ejecutor.
- Cada punto ambiguo debe marcarse como pendiente.

### 6. Diseñar estructura del tablero Miro

Preparar una especificación de tablero, aunque no se cree directamente en Miro.

Estructura recomendada:

```text
Título del tablero
├── 1. Contexto y objetivo
├── 2. Leyenda visual
├── 3. AS-IS
│   ├── Swimlanes por actor/sistema
│   ├── Flujo principal
│   ├── Fricciones marcadas
│   └── Pendientes de confirmar
├── 4. TO-BE
│   ├── Swimlanes por actor/sistema
│   ├── Flujo automatizado/mejorado
│   ├── Controles humanos
│   └── Excepciones
├── 5. Reglas funcionales
├── 6. Inputs/outputs y sistemas
├── 7. Riesgos y KPIs
└── 8. Acciones derivadas Jira/Confluence
```

### 7. Definir estilo visual

Usar una leyenda consistente:

| Tipo de elemento | Convención recomendada |
|---|---|
| Actor / área | Swimlane horizontal o vertical |
| Sistema | Swimlane propia o bloque diferenciado |
| Paso manual | Caja de tarea manual |
| Paso automático | Caja de tarea automática |
| Decisión | Rombo / gateway |
| Fricción | Marcador de alerta o nota destacada |
| Riesgo | Nota lateral con severidad |
| Pendiente | Nota `Pendiente de confirmar` |
| KPI | Bloque específico de medición |
| Jira/Confluence | Bloque de acciones derivadas |

No depender exclusivamente del color para comunicar significado. Acompañar siempre con etiqueta textual.

### 8. Generar salida para Miro

Si hay conector/API/MCP de Miro disponible, preparar instrucciones de creación con nombres de frames, shapes, conectores y textos.

Si no hay conector, entregar una especificación lista para que una persona la replique.

### 9. Validar contra documentación Confluence

Comprobar que el mapa respeta la documentación operativa:

- Metadatos del proceso.
- Trigger y output.
- AS-IS documentado.
- TO-BE esperado.
- Reglas funcionales.
- Inputs/outputs.
- Sistemas.
- KPIs.
- Riesgos.
- Pendientes.

Si el mapa contradice la documentación, señalar la contradicción y pedir validación.

### 10. Proponer acciones derivadas

Al final, proponer si procede:

- Actualización de página Confluence.
- Nueva tarea Jira.
- Subtareas técnicas.
- Pendientes de validación con owner funcional o técnico.
- Revisión de Miro con Kevin.

No crear ni modificar Jira, Confluence o Miro sin confirmación explícita.

---

## Formato de salida esperado

Usar este formato por defecto:

```markdown
# Mapeo de proceso — [Nombre]

## 1. Resumen

## 2. Supuestos y fuentes utilizadas

## 3. Alcance

| Campo | Detalle |
|---|---|
| Trigger | |
| Output final | |
| Actores | |
| Sistemas | |
| Tipo de mapa | AS-IS / TO-BE / ambos |

## 4. Tabla maestra del proceso

| ID | Vista | Fase | Paso | Actor / lane | Sistema | Tipo | Entrada | Salida | Regla / condición | Fricción / riesgo |
|---|---|---|---|---|---|---|---|---|---|---|

## 5. Especificación del tablero Miro

### Frame 1 — Contexto
### Frame 2 — AS-IS
### Frame 3 — Fricciones
### Frame 4 — TO-BE
### Frame 5 — Reglas funcionales
### Frame 6 — Riesgos, KPIs y próximos pasos

## 6. Elementos BPMN/Miro

| ID | Elemento | Texto visible | Tipo | Lane | Conecta con | Notas |
|---|---|---|---|---|---|---|

## 7. Reglas funcionales y excepciones

## 8. Fricciones detectadas

| Fricción | Evidencia | Impacto | Posible mejora |
|---|---|---|---|

## 9. Pendientes de confirmar

## 10. Acciones recomendadas

### Candidatas a Jira
### Candidatas a Confluence
### Revisión requerida
```

---

## Criterios de calidad

Antes de entregar, comprobar:

- [ ] El mapa tiene objetivo claro.
- [ ] Se distingue AS-IS de TO-BE.
- [ ] El trigger y output están identificados.
- [ ] Cada paso tiene actor o sistema responsable.
- [ ] Las decisiones tienen condiciones y salidas.
- [ ] Los pasos manuales, automáticos y semi-automáticos están diferenciados.
- [ ] Las fricciones aparecen asociadas a pasos concretos.
- [ ] Los inputs y outputs principales están reflejados.
- [ ] Las reglas funcionales no se han inventado.
- [ ] Los pendientes están marcados explícitamente.
- [ ] La salida puede trasladarse a Miro sin reinterpretación pesada.
- [ ] Se respetan las reglas de Confluence/Jira de Educa si aplica.
- [ ] No se incluyen credenciales, emails, tokens ni información sensible innecesaria.

---

## Errores comunes a evitar

- Mezclar AS-IS y TO-BE sin separarlos.
- Dibujar pasos sin responsable.
- Convertir una decisión en una tarea lineal.
- Omitir casos de excepción o fallback.
- Inventar reglas funcionales no documentadas.
- Usar nombres personales cuando baste con roles funcionales.
- Hacer un mapa bonito pero no accionable.
- Crear demasiados detalles técnicos para una audiencia de negocio.
- Crear un TO-BE sin reflejar qué fricción resuelve.
- No marcar dudas o campos pendientes.
- Asumir que una skill permite editar Miro si no existe conector/API/MCP activo.

---

## Relación con Miro

Esta skill puede producir una especificación de tablero Miro.

Solo debe crear o modificar tableros reales si existe un conector/API/MCP de Miro disponible y el usuario confirma la acción.

Sin conector, entregar:

- Frames recomendados.
- Swimlanes.
- Tabla de elementos.
- Textos de cada nodo.
- Conexiones entre nodos.
- Leyenda visual.
- Pendientes.

Con conector, pedir confirmación antes de crear o modificar un tablero real.

---

## Plantillas relacionadas

- `templates/confluence-page-template.md`
- `templates/jira-issue-template.md`
- `templates/executive-summary-template.md`

---

## Conocimiento relacionado

- `skills/educa-edtech-confluence/SKILL.md`
- `skills/educa-edtech-jira/SKILL.md`
- `skills/n8n-workflow-engineering/SKILL.md`
- `knowledge/company-writing-style.md`
- `knowledge/quality-standards.md`
- `skills/educa-edtech-bpmn-miro-process-mapping/references/miro-mapping-guidelines.md`
