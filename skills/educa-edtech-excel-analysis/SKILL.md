---
name: educa-edtech-excel-analysis
description: "Use this skill whenever Santi asks to analyze, audit, improve, edit, rebuild or create Excel files for Educa Edtech / Operaciones. Triggers: 'revisa este Excel', 'mejora este Excel', 'audita fórmulas', 'sistema de scoring', 'dashboard', 'KPIs', 'calculadora', 'modelo en Excel', 'SharePoint Excel', 'actualiza el workbook', 'no rompas fórmulas', 'prepara versión v2'. This skill is mandatory before modifying corporate spreadsheets, especially files linked to Jira, Confluence, SharePoint, scoring systems, KPIs, dashboards or operational audits."
---

# Excel · Educa Edtech — Análisis, auditoría y edición segura de workbooks

Esta skill define cómo trabajar con archivos Excel corporativos de Educa Edtech, especialmente cuando el archivo forma parte de procesos de **Operaciones**, **auditoría**, **KPIs**, **scoring**, **automatización**, **reporting**, **Jira**, **Confluence** o **SharePoint**.

La regla principal es:

```text
Nunca modificar directamente el archivo original.
Trabajar siempre sobre una copia versionada y auditable.
```

---

## 1. Objetivo

Garantizar que cualquier análisis o modificación de Excel sea:

- Trazable.
- Reversible.
- Comprensible para negocio.
- Robusto ante nuevas filas o entrevistas.
- Respetuoso con fórmulas existentes.
- Compatible con documentación en Confluence.
- Preparado para seguimiento en Jira si requiere acción del equipo.

---

## 2. Cuándo usar esta skill

Usar esta skill cuando la tarea implique:

- Revisar o auditar un Excel corporativo.
- Modificar fórmulas, hojas, tablas, validaciones o dashboards.
- Crear una versión mejorada de un workbook existente.
- Analizar un sistema de scoring, KPIs o reporting.
- Limpiar o transformar datos tabulares para negocio.
- Preparar información para Confluence o Jira.
- Trabajar con archivos procedentes de SharePoint.
- Crear una calculadora operativa o modelo de priorización.

Ejemplos:

```text
Mejora este Excel sin romper fórmulas.
Audita el sistema de scoring IMO.
Crea una versión v2 de la calculadora.
Añade validaciones y changelog.
Revisa si las fórmulas están bien planteadas.
Prepara el Excel para que mi jefa lo revise.
```

---

## 3. Principios obligatorios

### 3.1 No sobrescribir originales

Nunca guardar cambios sobre el archivo original.

Usar siempre una copia versionada:

```text
Nombre original.xlsx
        ↓
Nombre original_v2_revision.xlsx
```

Si se hacen iteraciones:

```text
Nombre original_v2_revision.xlsx
Nombre original_v3_validada.xlsx
```

### 3.2 Separar análisis de modificación

Antes de modificar:

1. Leer estructura del workbook.
2. Identificar hojas, fórmulas y rangos críticos.
3. Detectar riesgos.
4. Proponer cambios.
5. Ejecutar solo los cambios autorizados.

### 3.3 No mezclar metodología con formato

Distinguir siempre entre:

| Tipo de cambio | Ejemplo | Riesgo |
|---|---|---|
| Formato | Colores, anchos, bordes, títulos | Bajo |
| Técnico | Fórmulas, validaciones, tablas dinámicas | Medio |
| Metodológico | Cambiar ponderaciones o definición de métrica | Alto |
| Estructural | Añadir/eliminar hojas, cambiar modelo de datos | Alto |
| Documental | Actualizar instrucciones o changelog | Bajo/medio |

Todo cambio metodológico debe explicarse y justificarse.

### 3.4 Mantener trazabilidad

Toda versión modificada debe incluir o actualizar una hoja:

```text
CHANGELOG
```

Con columnas:

| Fecha | Versión | Autor/Asistente | Tipo de cambio | Hoja afectada | Descripción | Motivo | Impacto |
|---|---|---|---|---|---|---|---|

### 3.5 Preservar fórmulas existentes salvo motivo justificado

Antes de tocar una fórmula:

- Identificar qué calcula.
- Comprobar dependencias.
- Revisar si está replicada en otras filas/columnas.
- Cambiarla solo si hay un error, fragilidad o mejora aprobada.
- Validar valores antes/después.

---

## 4. Flujo de trabajo obligatorio

```text
1. Importar archivo original
2. Crear diagnóstico estructural
3. Identificar fórmulas/rangos críticos
4. Detectar problemas y riesgos
5. Proponer plan de cambios
6. Crear copia versionada
7. Aplicar cambios
8. Verificar fórmulas y valores clave
9. Crear/actualizar CHANGELOG
10. Exportar archivo final
11. Resumir cambios y recomendaciones
```

---

## 5. Auditoría inicial del workbook

Antes de editar, revisar:

| Revisión | Pregunta |
|---|---|
| Hojas | ¿Qué hojas existen y para qué sirven? |
| Datos brutos | ¿Qué hojas contienen inputs manuales? |
| Fórmulas | ¿Qué hojas calculan automáticamente? |
| Dashboards | ¿Qué hojas presentan resultados? |
| Parámetros | ¿Hay ponderaciones editables? |
| Validaciones | ¿Hay listas desplegables o controles de entrada? |
| Fórmulas frágiles | ¿Dependen de orden de filas o rangos fijos? |
| Valores manuales | ¿Hay outputs hardcodeados donde deberían ser fórmulas? |
| Errores | ¿Hay `#REF!`, `#VALUE!`, `#DIV/0!`, `#N/A`? |
| Trazabilidad | ¿Existe hoja de instrucciones y changelog? |

---

## 6. Clasificación de hojas

Clasificar cada hoja en una de estas categorías:

| Tipo | Descripción | Regla de edición |
|---|---|---|
| Input manual | Datos introducidos por usuario | Tocar solo para añadir validaciones, comentarios o estructura |
| Catálogo / maestro | IDs, personas, áreas, comisiones, links | Mantener como fuente de verdad |
| Cálculo | Fórmulas e indicadores | Editar con máxima cautela |
| Parámetros | Pesos, escalas y reglas | Debe ser visible y editable con control |
| Output | Rankings, agregados, dashboards | Puede mejorarse, pero no hardcodear resultados |
| Documentación | Instrucciones, changelog | Actualizar siempre que cambie lógica |

---

## 7. Reglas para modelos de scoring y KPIs

Cuando el Excel calcule un scoring, índice o KPI:

### 7.1 Separar conceptos

No mezclar en un único indicador conceptos distintos si pueden llevar a decisiones diferentes.

Ejemplo recomendado:

```text
Madurez operativa ≠ Riesgo de pérdida de información ≠ Oportunidad de automatización
```

### 7.2 Nombrar bien cada indicador

El nombre del indicador debe reflejar qué mide realmente.

Mal ejemplo:

```text
% procesos automatizables = madurez
```

Mejor:

```text
% procesos automatizables = oportunidad de automatización
% procesos automatizados/estandarizados = madurez
```

### 7.3 Evitar que una métrica positiva mida algo negativo

Si una variable representa una debilidad, no debe sumar como madurez sin invertirla o justificarla.

Ejemplo:

```text
Más dependencia de persona = más riesgo, no más madurez.
Más automatizable = más oportunidad, no necesariamente más madurez.
Más manualidad = menos madurez.
```

### 7.4 Documentar ponderaciones

Toda ponderación debe tener:

- Celda editable.
- Nombre claro.
- Explicación en instrucciones.
- Justificación de negocio.
- Nota de que puede revisarse tras uso real.

### 7.5 Proteger contra divisiones por cero

Usar lógica equivalente a:

```text
Si denominador = 0 → devolver vacío, 0 controlado o NA documentado.
```

Nunca dejar errores visibles como `#DIV/0!`.

---

## 8. Reglas para datos manuales

### 8.1 Validaciones obligatorias

Añadir listas desplegables cuando existan categorías cerradas:

| Campo | Valores recomendados |
|---|---|
| Sí/No | `Sí`, `No` |
| Estado entrevista | `Pendiente de entrevista`, `Tabulada`, `Pendiente de revisión`, `Validada` |
| Criticidad | `Crítico`, `Operativo`, `Otro` |
| Frecuencia | `Diario`, `Semanal`, `Mensual`, `Puntual` |
| Impacto | `1`, `2`, `3` o `Bajo`, `Medio`, `Alto` |
| Esfuerzo | `1`, `2`, `3` o `Bajo`, `Medio`, `Alto` |
| Dependencia persona | `Baja`, `Media`, `Alta` |

### 8.2 Vacíos

No asumir que vacío siempre significa `No` salvo que esté explícitamente documentado.

Si se decide usar:

```text
vacío = No
```

Debe quedar indicado en:

- hoja `Instrucciones`;
- documentación Confluence;
- comentarios o validación de datos si aplica.

### 8.3 Campos de estado

Evitar estados ambiguos como:

```text
Pendiente
```

Preferir:

```text
Pendiente de entrevista
Tabulada
Pendiente de revisión
Validada
Descartada
```

---

## 9. Reglas para fórmulas

### 9.1 Preferir fórmulas robustas

Evitar fórmulas que dependan de que dos hojas tengan filas perfectamente alineadas.

Frágil:

```text
SUMPRODUCT(Maestro!A2:A10 = Comisión, Scoring!B2:B10)
```

Mejor:

```text
Añadir Comisión a la hoja de scoring con búsqueda por ID
y después usar AVERAGEIF/AVERAGEIFS sobre esa columna.
```

### 9.2 Usar IDs como claves

Si varias hojas comparten entrevistas, procesos o documentos, usar siempre un ID común:

```text
ID Entrevista
ID Proceso
ID Automatización
```

### 9.3 No hardcodear resultados

Si una tabla de salida depende de datos, debe calcularse con fórmulas siempre que sea razonable.

Permitido hardcodear solo:

- etiquetas;
- textos descriptivos;
- snapshots manuales claramente marcados;
- comentarios históricos.

### 9.4 Fórmulas legibles

Cuando una fórmula sea compleja, añadir explicación en la hoja `Instrucciones` o en un comentario.

---

## 10. Reglas de diseño y formato

### 10.1 Estructura visual

Cada hoja debe tener:

- Título claro.
- Breve descripción si la hoja no es obvia.
- Encabezados visibles.
- Columnas con anchura adecuada.
- Congelación de paneles si hay muchas filas.
- Formatos numéricos coherentes.
- Colores moderados y profesionales.

### 10.2 Códigos de color recomendados

| Color | Uso |
|---|---|
| Amarillo suave | Parámetros editables |
| Azul/gris | Encabezados y estructura |
| Verde suave | Métricas buenas / bajo riesgo |
| Rojo suave | Riesgo alto / atención |
| Gris claro | Campos calculados o no editables |

No abusar de colores. Priorizar legibilidad.

### 10.3 Dashboards

Un dashboard debe mostrar:

- KPIs principales.
- Ranking o top prioridades.
- Segmentación por área/comisión.
- Alertas o riesgos.
- Fecha del snapshot.
- Nota de interpretación.

---

## 11. Reglas de verificación antes de entregar

Antes de entregar un Excel modificado, comprobar:

- [ ] El archivo original no ha sido sobrescrito.
- [ ] Existe copia versionada.
- [ ] No hay errores evidentes de fórmula.
- [ ] Las fórmulas principales devuelven valores esperados.
- [ ] Los resultados clave coinciden o cambian con explicación.
- [ ] Las hojas input no fueron alteradas indebidamente.
- [ ] Las nuevas fórmulas no dependen de filas alineadas sin clave.
- [ ] Hay hoja `CHANGELOG`.
- [ ] Las instrucciones reflejan cambios metodológicos.
- [ ] El archivo se abre como `.xlsx` válido.
- [ ] El resumen final explica cambios, riesgos y próximos pasos.

---

## 12. Cómo trabajar con Confluence y Jira

### 12.1 Confluence

Si el Excel alimenta documentación de Confluence:

1. No actualizar Confluence hasta validar el Excel.
2. Preparar primero una propuesta de cambios en texto.
3. Aplicar `skills/educa-edtech-confluence/SKILL.md`.
4. Actualizar metodología, fórmulas, limitaciones y snapshot si cambian.

### 12.2 Jira

Crear o proponer tareas Jira si:

- Hay cambios metodológicos pendientes de validar.
- Hay errores que requieren revisión del equipo.
- Hay documentación pendiente.
- Hay dependencia de IT/SharePoint/propietarios del proceso.

Aplicar:

```text
skills/educa-edtech-jira/SKILL.md
```

---

## 13. Formato de salida recomendado

Al terminar una auditoría o mejora de Excel, entregar:

```markdown
## Resultado

Archivo generado: `[nombre_archivo_vX.xlsx]`

## Cambios realizados

| Tipo | Hoja | Cambio | Motivo | Impacto |
|---|---|---|---|---|

## Validaciones realizadas

- 

## Cambios metodológicos

- 

## Riesgos o limitaciones

- 

## Recomendaciones para Confluence

- 

## Recomendaciones para Jira

- 
```

---

## 14. Reglas específicas para sistemas de scoring operativo

Cuando el archivo sea un sistema de scoring como IMO/IRPI/automatización:

1. Separar claramente:
   - madurez;
   - riesgo;
   - oportunidad de automatización;
   - viabilidad técnica.
2. No usar el mismo indicador para tomar decisiones diferentes.
3. Añadir hoja de parámetros si no existe.
4. Añadir hoja de limitaciones metodológicas si el sistema se usará con dirección.
5. Hacer que las ponderaciones sean visibles y editables.
6. Evitar que estados ambiguos entren en cálculos sin control.
7. Indicar si un snapshot es manual o calculado automáticamente.
8. Añadir explicación para lectura ejecutiva.

---

## 15. Regla final

Un Excel corporativo no debe ser solo un archivo que calcula.

Debe poder responder:

```text
Qué mide,
por qué lo mide,
de dónde salen los datos,
qué fórmulas usa,
qué supuestos aplica,
qué limitaciones tiene,
qué cambió entre versiones,
y qué decisiones permite tomar.
```

Si no responde a esas preguntas, todavía no está listo para usarse como fuente de decisión.
