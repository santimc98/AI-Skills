# Guía de mapeo BPMN / Miro para Operaciones Educa Edtech

## Propósito

Este documento complementa la skill `educa-edtech-bpmn-miro-process-mapping`.

Su objetivo es fijar una forma común de convertir documentación operativa en mapas visuales de proceso, especialmente para trabajo de diagnóstico, rediseño, automatizaciones y documentación AS-IS / TO-BE.

---

## Referencias internas usadas para diseñar la skill

La skill se diseñó tomando como referencia funcional:

| Tipo | Referencia interna | Uso |
|---|---|---|
| Metodología | Confluence AA1 · `Metodología - Mapa de diagnóstico` | Diagnóstico por capas: antes de reunión, durante reunión, consolidación por área y traslado al mapa |
| Proceso documentado | Confluence AA1 · `Documentación de Procesos — Triaje tickets soporte` | Ejemplo de estructura completa: descripción, ficha, AS-IS, TO-BE, reglas, inputs/outputs, KPIs y riesgos |
| Automatización/proceso | Confluence AA1 · `Automatización facturación artículos` | Referencia de automatización/proceso a contrastar cuando el contenido esté disponible |
| Miro | Capturas internas de AS-IS/TO-BE de triaje soporte y facturación artículos | Estilo visual, swimlanes, colores, leyenda implícita y organización BPMN usada por el equipo |

No incluir enlaces privados de Miro, credenciales, tokens, emails o datos personales en este repositorio público.

---

## Plantilla visual base observada en Miro

Los mapas de ejemplo siguen una plantilla de **Flujo de proceso BPMN** con estas características:

1. Un frame blanco grande por mapa.
2. Título visible en la parte superior izquierda, normalmente con formato:
   - `BPMN [Nombre proceso] (As - Is)`
   - `BPMN [Nombre proceso] (To - Be)`
3. Swimlanes horizontales con etiqueta vertical a la izquierda.
4. Flujo principal de izquierda a derecha.
5. Inicio con evento circular verde pequeño o blanco con borde verde.
6. Fin con evento circular verde grande, etiquetado como `Proceso Finalizado` o equivalente.
7. Tareas como rectángulos redondeados.
8. Decisiones como rombos amarillos.
9. Conectores con flechas negras o grises, siempre etiquetados con `Sí` / `No` cuando salen de una decisión.
10. Notas adhesivas para aclaraciones, fuentes, dudas o reglas.

---

## Convención visual observada

### Colores de tareas

| Color / tipo visual | Uso observado | Regla de uso recomendada |
|---|---|---|
| Azul claro | Paso automático, sistema, plataforma o acción digital normalizada | Usar para acciones ejecutadas por sistemas, formularios, Jira, N8N, APIs, notificaciones automáticas o pasos objetivo del TO-BE |
| Naranja | Paso manual humano, revisión, análisis, decisión operativa humana o tarea con fricción | Usar para carga manual, intervención de responsable, revisión humana o paso que se quiere reducir/automatizar |
| Amarillo claro | Nota, regla, fuente de información, aclaración, duda o comentario lateral | Usar como sticky note, no como tarea del flujo |
| Verde | Inicio/fin, estado final o marcador positivo de cierre | Usar solo para eventos BPMN de inicio/final o resultado completado |
| Azul oscuro / colores intensos en cabecera de lane | Etiqueta vertical de actor/sistema | Usar para identificar swimlanes, no para tareas del flujo |

### Swimlanes

Las lanes se usan para separar responsabilidades. En los ejemplos aparecen lanes como:

- Jira Customer Service.
- Product Strategy Manager.
- N8N.
- Manager.
- Usuario.
- Proveedor.
- Tecnología.

Reglas:

- Crear una lane por actor, área o sistema que ejecute pasos.
- Si un sistema ejecuta pasos automáticos relevantes, darle lane propia.
- Si una persona o rol revisa, decide o corrige, darle lane propia.
- No mezclar en la misma lane un sistema y una persona salvo que el proceso sea muy simple.

### Estilo AS-IS

El AS-IS debe reflejar el proceso actual, aunque sea imperfecto.

Patrón observado:

- Más presencia de tareas naranjas cuando hay trabajo manual.
- Lanes de personas o roles humanos cuando ejecutan clasificación, revisión o análisis.
- Notas adhesivas para remarcar límites, problemas, criterios no claros o dependencias.
- Fricciones visibles junto al paso afectado.

### Estilo TO-BE

El TO-BE debe mostrar la mejora o automatización futura.

Patrón observado:

- Más tareas azules para automatización y sistema.
- Lane específica para N8N, agente, workflow o sistema automatizador cuando aplica.
- Mantenimiento de controles humanos naranjas solo cuando hay incertidumbre, fallback, aprobación o excepción.
- Decisiones explícitas de clasificación, confianza o validación.
- Fallback manual claramente conectado al cierre o a revisión.

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
│   ├── Lanes por actor/sistema actual
│   ├── Flujo actual de izquierda a derecha
│   ├── Tareas manuales en naranja
│   ├── Tareas automáticas/sistema en azul
│   ├── Decisiones en rombo amarillo
│   └── Notas de fricción o aclaración
├── Frame TO-BE
│   ├── Lanes por actor/sistema futuro
│   ├── Automatización o sistema con lane propia
│   ├── Pasos automatizados en azul
│   ├── Controles/fallbacks humanos en naranja
│   ├── Decisiones con salidas Sí/No
│   └── Resultado final claro
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
- Jira Customer Service.
- Proveedor.
- Usuario.

### Tipos de tareas

| Tipo | Criterio | Color recomendado |
|---|---|---|
| Manual | Una persona ejecuta el paso completo | Naranja |
| Semi-automática | El sistema asiste, pero una persona valida o decide | Azul si domina sistema; naranja si domina revisión humana |
| Automática | El sistema ejecuta sin intervención humana | Azul claro |
| Control humano | Paso de revisión, aprobación o validación | Naranja |
| Notificación | Comunicación generada hacia persona/equipo/sistema | Azul si automática; naranja si manual |
| Nota / aclaración | Comentario, regla, duda o fuente | Amarillo claro |

### Decisiones

Toda decisión debe tener:

- Pregunta explícita dentro del rombo.
- Al menos dos salidas.
- Etiquetas `Sí` y `No` en conectores.
- Condición para cada salida.
- Responsable de la decisión si no es automática.

Ejemplo:

```text
¿Clasificación realizada?
├── Sí → añadir etiqueta correspondiente
└── No → revisión manual / fallback
```

### Fricciones

Cada fricción debe asociarse a un paso concreto.

Evitar fricciones genéricas como "proceso manual" sin explicar dónde ocurre y qué impacto tiene.

Formato recomendado:

```text
Fricción: lectura manual de tickets
Paso afectado: análisis del contenido
Impacto: carga operativa y retraso en resolución
Posible mejora: clasificación automática con fallback humano
Representación Miro: sticky note amarilla cerca del paso + tarea manual naranja
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

> Cuando el proceso actual depende de una persona para interpretar información, el análisis humano debe aparecer en naranja y en lane propia.

### Triaje soporte — TO-BE

Patrón:

- Mantiene el origen en Jira.
- Añade lane `N8N` para automatizar análisis, clasificación y etiquetado.
- Usa datos del ticket como input visible.
- Conserva tarea humana naranja solo como fallback cuando no hay clasificación fiable.
- El flujo automatizado llega al mismo cierre funcional que el AS-IS.

Regla reutilizable:

> El TO-BE no debe eliminar el control humano cuando hay incertidumbre; debe desplazarlo a fallback o excepción.

### Facturación artículos — AS-IS

Patrón:

- Varias lanes: usuario, proveedor, manager/operaciones o roles equivalentes.
- Flujo más largo y con más notas de contexto.
- Numerosas tareas manuales naranjas.
- Decisiones y documentos asociados al proceso.
- Notas adhesivas para reglas, problemas o información complementaria.

Regla reutilizable:

> En procesos administrativos largos, usar notas para documentar reglas y dependencias, pero mantener el flujo principal limpio.

### Facturación artículos — TO-BE

Patrón:

- Flujo más lineal.
- Más tareas azules, indicando sistema/automatización.
- Conserva algún control humano naranja para validación o intervención relevante.
- Menos pasos que el AS-IS.
- Cierre claro con evento verde.

Regla reutilizable:

> El TO-BE debe simplificar el flujo, reducir tareas manuales y mostrar qué sistema asume cada paso automatizado.

---

## Entregable mínimo antes de dibujar

Antes de crear o proponer el mapa en Miro, debe existir una tabla maestra:

| ID | Vista | Fase | Paso | Actor | Sistema | Tipo | Entrada | Salida | Regla | Fricción |
|---|---|---|---|---|---|---|---|---|---|---|

Si esta tabla no puede completarse, el mapa debe marcar pendientes antes de asumir el flujo.

---

## Salida específica para crear en Miro

Cuando Claude tenga conector/MCP de Miro, debe generar una lista de objetos con esta estructura:

| ID | Frame | Lane | Tipo Miro | Texto | Color/estilo | Posición relativa | Conecta con |
|---|---|---|---|---|---|---|---|
| E01 | AS-IS | Jira Customer Service | Evento inicio | Inicio | Círculo verde | izquierda | T01 |
| T01 | AS-IS | Jira Customer Service | Tarea | Recibir ticket | Rectángulo azul | derecha de E01 | D01 |
| D01 | AS-IS | Jira Customer Service | Decisión | ¿Proyecto MyLXP o TutorLXP? | Rombo amarillo | derecha de T01 | T02/T03 |

Reglas:

- Usar coordenadas o posiciones relativas si no se conocen coordenadas exactas.
- Mantener espaciado horizontal amplio.
- Alinear tareas dentro de cada lane.
- Evitar cruces de flechas cuando sea posible.
- Si una flecha cruza lane, que represente handoff real.

---

## Checklist de revisión visual

- [ ] Hay título claro con `AS-IS` o `TO-BE`.
- [ ] El alcance se entiende sin explicación oral.
- [ ] AS-IS y TO-BE están separados en frames distintos.
- [ ] Las lanes corresponden a actores o sistemas reales.
- [ ] Cada paso tiene responsable.
- [ ] Cada gateway tiene pregunta y salidas `Sí` / `No`.
- [ ] Las tareas manuales están diferenciadas de las automáticas.
- [ ] Las fricciones están visibles junto al paso afectado.
- [ ] Las automatizaciones están diferenciadas de tareas humanas.
- [ ] Hay notas para reglas o pendientes, pero no saturan el flujo.
- [ ] Hay evento de inicio y evento final.
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
