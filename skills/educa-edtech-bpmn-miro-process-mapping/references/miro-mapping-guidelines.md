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
| Automatización/proceso | Confluence AA1 · `Automatización facturación artículos` | Referencia a contrastar cuando el contenido esté disponible |
| Miro | Tableros internos de proceso compartidos por Santi/Kevin | Estilo visual y organización AS-IS / TO-BE |

No incluir enlaces privados de Miro, credenciales, tokens, emails o datos personales en este repositorio público.

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
├── Contexto
├── Alcance
├── AS-IS
├── Fricciones detectadas
├── TO-BE
├── Reglas funcionales
├── Inputs / Outputs / Sistemas
├── Riesgos y KPIs
└── Acciones derivadas
```

---

## Convenciones de modelado

### Actores y sistemas

Usar swimlanes cuando haya varios responsables.

Ejemplos de lanes:

- Área solicitante
- Operaciones
- Tecnología
- Sistema origen
- Sistema destino
- Automatización / agente
- Owner funcional
- Owner técnico

### Tipos de tareas

| Tipo | Criterio |
|---|---|
| Manual | Una persona ejecuta el paso completo |
| Semi-automática | El sistema asiste, pero una persona valida o decide |
| Automática | El sistema ejecuta sin intervención humana |
| Control humano | Paso de revisión, aprobación o validación |
| Notificación | Comunicación generada hacia persona/equipo/sistema |

### Decisiones

Toda decisión debe tener:

- Pregunta explícita.
- Al menos dos salidas.
- Condición para cada salida.
- Responsable de la decisión si no es automática.

Ejemplo:

```text
¿El ticket se puede clasificar con confianza?
├── Sí → asignar etiqueta automáticamente
└── No → aplicar fallback y enviar a revisión manual
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
```

---

## Entregable mínimo antes de dibujar

Antes de crear o proponer el mapa en Miro, debe existir una tabla maestra:

| ID | Vista | Fase | Paso | Actor | Sistema | Tipo | Entrada | Salida | Regla | Fricción |
|---|---|---|---|---|---|---|---|---|---|---|

Si esta tabla no puede completarse, el mapa debe marcar pendientes antes de asumir el flujo.

---

## Checklist de revisión visual

- [ ] Hay título claro.
- [ ] El alcance se entiende sin explicación oral.
- [ ] AS-IS y TO-BE están separados.
- [ ] Las lanes corresponden a actores o sistemas reales.
- [ ] Cada paso tiene responsable.
- [ ] Cada gateway tiene pregunta y salidas.
- [ ] Las fricciones están visibles.
- [ ] Las automatizaciones están diferenciadas de tareas humanas.
- [ ] Hay bloque de pendientes.
- [ ] Hay bloque de acciones derivadas.
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
