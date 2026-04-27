# Prompt Engineering Skill

## Cuándo usar esta skill

Usar esta skill cuando la tarea implique crear, auditar, mejorar o estructurar prompts e instrucciones para asistentes, agentes, automatizaciones o modelos de IA.

## Objetivo

Convertir necesidades de trabajo en instrucciones claras, robustas y reutilizables para sistemas de IA.

## Entradas necesarias

- Objetivo del prompt o agente.
- Contexto de uso.
- Herramientas disponibles.
- Restricciones o políticas.
- Formato de salida deseado.
- Ejemplos de buenas y malas respuestas, si existen.

## Procedimiento paso a paso

1. Identificar la tarea real que debe resolver el modelo.
2. Separar rol, contexto, instrucciones, restricciones y formato de salida.
3. Eliminar ambigüedades.
4. Añadir reglas de decisión cuando haya varios caminos posibles.
5. Añadir criterios de calidad.
6. Añadir ejemplos si ayudan a reducir errores.
7. Revisar que el prompt no incentive invención ni acciones peligrosas.
8. Preparar versión final lista para usar.

## Criterios de calidad

- El prompt debe ser claro y accionable.
- Debe indicar qué hacer cuando falta información.
- Debe definir formato de salida.
- Debe evitar instrucciones contradictorias.
- Debe ser mantenible y fácil de editar.

## Formato de salida esperado

```markdown
# Prompt / Instrucciones

## Rol

## Contexto

## Objetivo

## Herramientas disponibles

## Procedimiento

## Restricciones

## Formato de salida

## Criterios de calidad
```

## Errores comunes a evitar

- Crear prompts demasiado largos sin estructura.
- Mezclar instrucciones obligatorias con preferencias.
- No definir salida esperada.
- No indicar cómo actuar ante incertidumbre.
- No contemplar errores habituales.

## Plantillas relacionadas

- `templates/confluence-page-template.md`

## Conocimiento relacionado

- `knowledge/quality-standards.md`
