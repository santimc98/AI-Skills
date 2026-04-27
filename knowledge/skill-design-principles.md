# Principios de diseño de skills

Este documento recoge principios generales para diseñar skills reutilizables dentro del repositorio `AI-Skills`.

## 1. Alcance concreto

Una skill debe resolver una familia concreta de tareas. No debe ser tan estrecha que solo sirva para un caso aislado, ni tan amplia que mezcle demasiados comportamientos.

Ejemplos de buen alcance:

- `educa-edtech-excel-analysis`: analizar y mejorar Excels corporativos de Educa Edtech.
- `jira-backlog-management`: crear, revisar y ordenar issues de Jira.
- `skill-creator`: crear y mantener skills.

## 2. Descripción activadora

La descripción debe decir:

1. Qué hace la skill.
2. Cuándo debe usarse.
3. Qué palabras, tareas o contextos deberían activarla.

Una descripción demasiado corta hace que el asistente no la use cuando debería.

## 3. Instrucciones ejecutables

Una skill útil no solo explica conceptos. Debe decirle al asistente qué hacer paso a paso.

Preferir pasos concretos como leer el archivo de entrada, identificar columnas clave, detectar errores, crear una copia versionada y documentar cambios.

Evitar instrucciones vagas como analizar de forma adecuada sin explicar cómo.

## 4. Separar skill, plantilla y conocimiento

Usar cada tipo de archivo para su función:

- `SKILL.md`: procedimiento de actuación.
- `templates/`: formatos reutilizables de salida.
- `knowledge/`: reglas, contexto, glosarios o políticas.
- `examples/`: ejemplos resueltos.
- `scripts/`: automatizaciones o validadores.
- `references/`: documentación extensa específica de una skill.

## 5. Portabilidad

Las skills deben poder usarse con ChatGPT, Claude, LibreChat, OpenClaw u otros agentes.

Evitar dependencias innecesarias de una plataforma concreta. Si una plataforma tiene una función específica, documentarla como una opción, no como requisito universal.

## 6. Confirmación para cambios reales

Cuando una skill pueda modificar sistemas reales, debe exigir confirmación explícita antes de actuar.

Aplica especialmente a Jira, Confluence, SharePoint, GitHub, GitLab, correo, calendario y archivos corporativos.

## 7. Supuestos explícitos

Si falta información crítica, preguntar.

Si falta información no crítica, avanzar con supuestos explícitos.

## 8. Criterios de calidad verificables

Una skill debe permitir revisar si el resultado está bien.

Ejemplos:

- El informe separa hechos, inferencias y recomendaciones.
- El Excel original no se sobrescribe.
- La tarea de Jira incluye descripción, criterios de aceptación y prioridad.
- La página de Confluence incluye metadatos, objetivo, alcance, procedimiento y próximos pasos.

## 9. Evitar duplicidades

Antes de crear una skill, revisar `index.md` y comprobar si ya existe una parecida.

Si existe, mejorar la skill existente en vez de crear otra.

## 10. Mantener el índice actualizado

Toda skill nueva debe aparecer en `index.md` con:

- Nombre.
- Ruta.
- Cuándo usarla.
- Plantillas relacionadas.
- Conocimiento relacionado.

Si una skill no está en el índice, es más difícil que un asistente la descubra y la use.
