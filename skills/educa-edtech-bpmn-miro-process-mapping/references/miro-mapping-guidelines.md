# Guía de mapeo BPMN / Miro para Operaciones Educa Edtech

## Propósito

Este documento complementa la skill `educa-edtech-bpmn-miro-process-mapping`.

Su objetivo es fijar una forma común de convertir documentación operativa en mapas visuales de proceso, especialmente para trabajo de diagnóstico, rediseño, automatizaciones y documentación AS-IS / TO-BE.

---

## Jerarquía de criterios

Cuando haya conflicto entre fuentes, aplicar este orden:

1. **Página oficial `Metodología BPMN` de Confluence AA1**.
2. Ejemplos reales de Miro compartidos por Santi/Kevin.
3. Buenas prácticas BPMN generales.
4. Criterio visual propuesto por el asistente.

La página `Metodología BPMN` manda sobre cualquier convención inferida desde capturas.

---

## Referencias internas usadas para diseñar la skill

| Tipo | Referencia interna | Uso |
|---|---|---|
| Metodología oficial BPMN | Confluence AA1 · página `1812529177` · `Metodología BPMN` | Reglas obligatorias BPMN, elementos, pools, lanes, tipos de actividad y convención de colores |
| Metodología de diagnóstico | Confluence AA1 · `Metodología - Mapa de diagnóstico` | Diagnóstico por capas: antes de reunión, durante reunión, consolidación por área y traslado al mapa |
| Proceso documentado | Confluence AA1 · `Documentación de Procesos — Triaje tickets soporte` | Ejemplo de estructura completa: descripción, ficha, AS-IS, TO-BE, reglas, inputs/outputs, KPIs y riesgos |
| Automatización/proceso | Confluence AA1 · `Automatización facturación artículos` | Referencia de automatización/proceso a contrastar cuando el contenido esté disponible |
| Miro | Capturas internas de AS-IS/TO-BE de triaje soporte y facturación artículos | Estilo visual, swimlanes, colores, leyenda implícita y organización BPMN usada por el equipo |

No incluir enlaces privados de Miro, credenciales, tokens, emails o datos personales en este repositorio público.

---

## Elementos BPMN oficiales

### Elementos de flujo de trabajo

| Elemento | Uso |
|---|---|
| Events / Eventos | Iniciar o finalizar un proceso y gestionar acciones específicas dentro del flujo |
| Gateways / Compuertas | Separar o unir flujos del proceso; representan decisiones o validaciones |
| Activities / Actividades | Tareas ejecutadas por personas, sistemas o subprocesos |
| Sequence flow / Flujo de secuencia | Mostrar el movimiento del flujo de trabajo dentro de un mismo pool |

### Elementos organizativos

| Elemento | Uso |
|---|---|
| Pool | Contiene un proceso completo asociado a un mismo departamento/comisión y sus sistemas |
| Swimlane / Senda | Organiza el proceso según quién o qué ejecuta cada actividad |
| Group / Grupo | Encierra elementos gráficos sin afectar al flujo de secuencia |

### Elementos de comportamiento especial

| Elemento | Uso |
|---|---|
| Messages / Message flow | Transferir acciones o datos entre pools/procesos distintos |

---

## Tipos de actividad oficiales

| Tipo | Definición | Representación recomendada |
|---|---|---|
| Human activity | Paso realizado por una persona | Actividad de usuario, color anaranjado |
| Service activity | Paso realizado por un sistema | Actividad de servicio, color turquesa |
| Call activity | Subproceso reutilizable o bloque de proceso llamado desde el flujo | Call activity / subproceso |

Regla importante: no llamar “automático” a una tarea si realmente hay revisión, decisión o carga humana. En ese caso usar actividad humana o semi-automática y explicarlo.

---

## Reglas BPMN obligatorias antes de exportar a Miro

1. Un **Pool** representa a un mismo departamento o comisión y sus sistemas.
2. El **Pool** se representa de manera vertical.
3. Un Pool puede dividirse en varios **Lanes** horizontales.
4. Debe existir un solo evento de inicio por diagrama.
5. Todos los eventos de fin deben tener nombre descriptivo; no usar solo `Fin`.
6. Todas las salidas de compuertas deben tener etiqueta `SÍ` / `NO` o equivalente explícito.
7. Todas las compuertas representan puntos de decisión o validación.
8. Todas las compuertas deben formularse como pregunta, por ejemplo: `¿Documento completo?`.
9. Cada compuerta debe tener al menos un camino de error o rama `NO`.
10. Todas las tareas deben nombrarse como **VERBO + OBJETO**.
11. No incluir el nombre del sistema dentro de la tarea si ese sistema ya aparece en el lane.
12. Las personas, si son necesarias, deben representarse en su propio lane.
13. Los sistemas automáticos deben ir en su propio lane.
14. Máximo 15 elementos por diagrama; si hay más, dividir en varios diagramas o subprocesos.
15. El flujo debe leerse preferiblemente de izquierda a derecha o de arriba hacia abajo.
16. Evitar flujos que retroceden visualmente de forma caótica.
17. Una tarea debe ser una unidad mínima de trabajo.
18. Si una tarea contiene `y`, revisar si realmente son dos tareas separadas.
19. El flujo debe terminar en un evento de fin; no puede quedar abierto en una tarea.
20. No pueden existir elementos sueltos o huérfanos.
21. Todo elemento, excepto el evento de inicio y fin, debe tener al menos un flujo de entrada y uno de salida.
22. El flujo de secuencia, línea continua, nunca debe cruzar fronteras de Pool.
23. Para comunicar Pools distintos, usar solo flujos de mensaje, línea punteada.

---

## Regla de modelado de personas y sistemas

El objetivo es modelar el **flujo de información**, no describir cada click de una persona cambiando de herramienta.

Evitar:

```text
Persona entra a sistema 1 → Persona cambia a sistema 2 → Persona actualiza sistema 3
```

Preferir:

```text
Identificar ID          (Lane Sistema 1)
Validar información    (Lane Sistema 2)
Actualizar registro    (Lane Sistema 3)
Revisar excepción      (Lane Persona)
```

---

## Convención oficial de colores

### Colores de lanes por sistema/actor

| Lane | Color oficial |
|---|---|
| Excel | Verde |
| Innotutor | Turquesa |
| Educapay | Amarillo claro |
| Adyen / Otros | Azul |
| Zoho | Amarillo oscuro |
| Jira | Azul oscuro |
| N8N | Anaranjado claro |
| Persona | Blanco |
| CallBell | Amarillo |
| Campus | Violeta claro |
| Correo | Gris |
| 3CX | Violeta |
| LLM | Anaranjado oscuro |

Si aparece un sistema no listado, elegir un color consistente, documentarlo en la leyenda y no reutilizarlo para otro sistema dentro del mismo mapa.

### Colores de elementos de flujo de trabajo

| Elemento | Color oficial |
|---|---|
| Evento de inicio | Relleno gris claro + borde verde oscuro |
| Evento de fin de proceso completado | Relleno verde + borde negro |
| Gateway / Compuerta | Relleno amarillo claro + borde negro |
| Actividad tipo usuario | Relleno anaranjado |
| Actividad tipo servicio | Relleno turquesa |

La convención oficial anterior tiene prioridad sobre la convención visual inferida de capturas.

---

## Plantilla visual base observada en Miro

Los mapas de ejemplo siguen una plantilla de **Flujo de proceso BPMN** con estas características:

1. Un frame blanco grande por mapa.
2. Título visible en la parte superior izquierda, normalmente con formato:
   - `BPMN [Nombre proceso] (As - Is)`
   - `BPMN [Nombre proceso] (To - Be)`
3. Pool vertical con lanes horizontales.
4. Flujo principal de izquierda a derecha.
5. Inicio con evento circular de inicio.
6. Fin con evento circular verde, etiquetado con nombre descriptivo.
7. Tareas como rectángulos redondeados.
8. Decisiones como rombos amarillos.
9. Conectores con flechas, siempre etiquetados con `Sí` / `No` cuando salen de una decisión.
10. Notas adhesivas para aclaraciones, fuentes, dudas o reglas.

---

## Uso de colores en AS-IS y TO-BE

### Estilo AS-IS

El AS-IS debe reflejar el proceso actual, aunque sea imperfecto.

Patrón esperado:

- Más presencia de actividades humanas anaranjadas cuando hay trabajo manual.
- Lanes de personas o roles humanos cuando ejecutan clasificación, revisión o análisis.
- Lanes de sistemas reales cuando el flujo de información pasa por herramientas.
- Notas adhesivas para límites, problemas, criterios no claros o dependencias.
- Fricciones visibles junto al paso afectado.

### Estilo TO-BE

El TO-BE debe mostrar la mejora o automatización futura.

Patrón esperado:

- Más actividades de servicio turquesa cuando el sistema automatiza pasos.
- Lane específica para N8N, LLM, agente, workflow o sistema automatizador cuando aplica.
- Actividades humanas anaranjadas solo para incertidumbre, fallback, aprobación o excepción.
- Decisiones explícitas de clasificación, confianza o validación.
- Fallback manual claramente conectado a revisión o cierre.

---

## Metodología de diagnóstico que debe respetar la skill

### 1. Antes de la reunión

- Leer cuestionarios o documentación previa.
- Identificar el perfil entrevistado.
- No repetir preguntas ya respondidas.
- Preparar temas de profundización.

### 2. Durante la reunión

Clasificar notas según dimensiones de fricción:

| Dimensión | Qué recoge |
|---|---|
| Procesos | Pasos, responsables, secuencia, duplicidades, cuellos de botella |
| Herramientas | Sistemas usados, integraciones, limitaciones, datos duplicados |
| Documentación | Guías, páginas, instrucciones, ausencia de conocimiento formal |
| Data / KPIs | Métricas, reporting, trazabilidad, datos de control |
| Área / estructura | Dependencias, riesgos, owners, handoffs y coordinación |

### 3. Después de las reuniones

- Consolidar por área.
- Unificar visión de directores, managers y técnicos.
- Extraer fricciones principales.
- Extraer oportunidades de mejora.
- Preparar texto listo para nodos del mapa.

### 4. Traslado a Miro

El mapa debe ser output de la consolidación, no un trabajo interpretativo adicional.

---

## Estructura recomendada de mapa

```text
Mapa — [Nombre del proceso]
├── Frame AS-IS
│   ├── Pool del departamento/comisión
│   ├── Lanes horizontales por actor/sistema actual
│   ├── Flujo actual de izquierda a derecha
│   ├── Actividades humanas en anaranjado
│   ├── Actividades de servicio en turquesa
│   ├── Gateways en amarillo claro
│   └── Notas de fricción o aclaración
├── Frame TO-BE
│   ├── Pool del departamento/comisión
│   ├── Lanes horizontales por actor/sistema futuro
│   ├── Automatización o sistema con lane propia
│   ├── Actividades de servicio en turquesa
│   ├── Controles/fallbacks humanos en anaranjado
│   ├── Gateways con salidas Sí/No
│   └── Evento final descriptivo
└── Bloques auxiliares
    ├── Reglas funcionales
    ├── Inputs / outputs
    ├── Riesgos / KPIs
    └── Pendientes
```

---

## Convenciones de modelado

### Actores y sistemas

Usar swimlanes cuando haya varios responsables.

Ejemplos de lanes:

- Área solicitante.
- Operaciones.
- Tecnología.
- Sistema origen.
- Sistema destino.
- Automatización / agente.
- Owner funcional.
- Owner técnico.
- N8N.
- LLM.
- Jira Customer Service.
- Proveedor.
- Usuario.
- Correo.

### Decisiones

Toda decisión debe tener:

- Pregunta explícita dentro del rombo.
- Al menos dos salidas.
- Etiquetas `Sí` y `No` en conectores.
- Condición para cada salida.
- Al menos una rama de error o `NO`.
- Responsable de la decisión si no es automática.

Ejemplo:

```text
¿Clasificación realizada?
├── Sí → Añadir etiqueta correspondiente
└── No → Enviar a revisión manual
```

### Fricciones

Cada fricción debe asociarse a un paso concreto.

Evitar fricciones genéricas como `proceso manual` sin explicar dónde ocurre y qué impacto tiene.

Formato recomendado:

```text
Fricción: lectura manual de tickets
Paso afectado: analizar contenido
Impacto: carga operativa y retraso en resolución
Posible mejora: clasificación automática con fallback humano
Representación Miro: nota amarilla cerca del paso + actividad humana anaranjada
```

---

## Patrones observados en los ejemplos

### Triaje soporte — AS-IS

Patrón:

- Lane de sistema `Jira Customer Service` para recepción y asignación inicial.
- Lane humana `Product Strategy Manager` para análisis, determinación de etiqueta y asignación manual.
- Decisión temprana sobre si el proyecto es MyLXP o TutorLXP.
- Decisión final sobre si la etiqueta requiere notificación técnica.
- Cierre con evento verde.

Regla reutilizable:

> Cuando el proceso actual depende de una persona para interpretar información, el análisis humano debe aparecer como actividad humana en anaranjado y en lane propia.

### Triaje soporte — TO-BE

Patrón:

- Mantiene el origen en Jira.
- Añade lane `N8N` para automatizar análisis, clasificación y etiquetado.
- Usa datos del ticket como input visible.
- Conserva actividad humana solo como fallback cuando no hay clasificación fiable.
- El flujo automatizado llega al mismo cierre funcional que el AS-IS.

Regla reutilizable:

> El TO-BE no debe eliminar el control humano cuando hay incertidumbre; debe desplazarlo a fallback o excepción.

### Facturación artículos — AS-IS

Patrón:

- Varias lanes: usuario, proveedor, manager/operaciones o roles equivalentes.
- Flujo más largo y con más notas de contexto.
- Numerosas actividades humanas.
- Decisiones y documentos asociados al proceso.
- Notas adhesivas para reglas, problemas o información complementaria.

Regla reutilizable:

> En procesos administrativos largos, usar notas para documentar reglas y dependencias, pero mantener el flujo principal limpio.

### Facturación artículos — TO-BE

Patrón:

- Flujo más lineal.
- Más actividades de servicio, indicando sistema/automatización.
- Conserva algún control humano para validación o intervención relevante.
- Menos pasos que el AS-IS.
- Cierre claro con evento verde.

Regla reutilizable:

> El TO-BE debe simplificar el flujo, reducir tareas manuales y mostrar qué sistema asume cada paso automatizado.

---

## Entregable mínimo antes de dibujar

Antes de crear o proponer el mapa en Miro, debe existir una tabla maestra:

| ID | Vista | Fase | Paso | Actor | Sistema | Tipo BPMN | Entrada | Salida | Regla | Fricción |
|---|---|---|---|---|---|---|---|---|---|---|

Si esta tabla no puede completarse, el mapa debe marcar pendientes antes de asumir el flujo.

---

## Salida específica para crear en Miro

Cuando Claude tenga conector/MCP de Miro, debe generar una lista de objetos con esta estructura:

| ID | Frame | Pool | Lane | Tipo Miro/BPMN | Texto | Color/estilo | Posición relativa | Conecta con |
|---|---|---|---|---|---|---|---|---|
| E01 | AS-IS | Operaciones | Jira | Evento inicio | Inicio | Relleno gris claro + borde verde oscuro | izquierda | T01 |
| T01 | AS-IS | Operaciones | Jira | Service activity | Recibir ticket | Turquesa | derecha de E01 | D01 |
| D01 | AS-IS | Operaciones | Jira | Gateway | ¿Proyecto MyLXP o TutorLXP? | Amarillo claro + borde negro | derecha de T01 | T02/T03 |

Reglas:

- Usar coordenadas o posiciones relativas si no se conocen coordenadas exactas.
- Mantener espaciado horizontal amplio.
- Alinear tareas dentro de cada lane.
- Evitar cruces de flechas cuando sea posible.
- Si una flecha cruza lane dentro del mismo pool, debe representar handoff real.
- Si el flujo cruza pools, usar flujo de mensaje punteado.

---

## Checklist de revisión visual y BPMN

- [ ] Hay título claro con `AS-IS` o `TO-BE`.
- [ ] El alcance se entiende sin explicación oral.
- [ ] AS-IS y TO-BE están separados en frames distintos.
- [ ] Existe un solo evento de inicio por diagrama.
- [ ] Todos los eventos de fin tienen nombre descriptivo.
- [ ] Las lanes corresponden a actores o sistemas reales.
- [ ] Cada paso tiene responsable.
- [ ] Cada tarea se nombra como VERBO + OBJETO.
- [ ] No se mete el sistema en el texto de la tarea si ya está en el lane.
- [ ] Cada gateway está formulado como pregunta.
- [ ] Cada gateway tiene salidas `Sí` / `No`.
- [ ] Cada gateway tiene al menos una rama `NO` o camino de error.
- [ ] Las actividades humanas están diferenciadas de las actividades de servicio.
- [ ] Las fricciones están visibles junto al paso afectado.
- [ ] Las automatizaciones están en lane propia cuando corresponde.
- [ ] Hay notas para reglas o pendientes, pero no saturan el flujo.
- [ ] No hay elementos huérfanos.
- [ ] El flujo termina en evento de fin.
- [ ] El diagrama no supera 15 elementos; si los supera, se divide.
- [ ] El mapa puede enlazarse desde Confluence.

---

## Seguridad y privacidad

- No incluir credenciales.
- No incluir tokens.
- No incluir contraseñas.
- No incluir emails personales si no son necesarios.
- En repositorios públicos usar roles funcionales cuando baste.
- En Confluence corporativo usar owners reales cuando el documento lo requiera y esté autorizado.
- No modificar tableros reales sin confirmación explícita.
