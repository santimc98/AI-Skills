# System prompt vs User prompt

## Idea principal

Un agente robusto separa lo que debe permanecer estable de lo que cambia en cada ejecución.

- **System prompt**: define identidad operativa, límites, herramientas, seguridad, procedimiento y formato base.
- **User prompt**: define la tarea concreta, datos variables y resultado esperado para una ejecución.

## Qué debe ir en el system prompt

| Bloque | Contenido |
|---|---|
| Rol | Quién es el agente y desde qué perspectiva trabaja. |
| Misión | Resultado principal que debe conseguir. |
| Alcance | Qué tareas puede atender y cuáles debe rechazar o escalar. |
| Herramientas | Qué herramientas tiene, cuándo usarlas y cuándo no. |
| Procedimiento | Pasos estables que debe seguir. |
| Seguridad | Reglas para datos sensibles, acciones externas, escritura y confirmaciones. |
| Incertidumbre | Qué hacer si faltan datos o la evidencia no basta. |
| Formato | Estructura de salida por defecto. |
| Calidad | Criterios para validar la respuesta antes de entregarla. |

## Qué debe ir en el user prompt

| Bloque | Contenido |
|---|---|
| Petición | Tarea concreta que se quiere resolver. |
| Datos | Payload, documento, mensaje, consulta, ID, registros o contexto puntual. |
| Restricciones de ejecución | Límites concretos de esa petición. |
| Resultado esperado | Qué debe devolver exactamente en esta ejecución. |
| Variables | Campos dinámicos que vienen de un workflow o usuario. |

## Regla práctica

```text
Si una instrucción debe cumplirse siempre, va al system prompt.
Si una instrucción solo aplica a esta ejecución, va al user prompt.
Si una instrucción controla el formato exacto, debe estar reforzada con parser, validador o pruebas.
```

## Ejemplo simple

### System prompt

```text
Eres un agente de soporte interno. Respondes de forma clara, no inventas datos y usas herramientas solo cuando necesitas verificar información real. Si una acción modifica sistemas reales, pides confirmación explícita antes de ejecutarla.
```

### User prompt

```text
Revisa este ticket de Jira y propón una respuesta para el usuario. No cambies el estado del ticket. Datos del ticket: {{ticket_json}}
```

## Errores comunes

- Meter credenciales o secretos en prompts.
- Repetir todo el system prompt dentro del user prompt.
- Poner reglas críticas solo en el user prompt cuando deberían estar siempre activas.
- Pedir JSON perfecto sin usar parser o validador.
- No definir qué hacer si una herramienta falla.
- Permitir acciones externas sin criterios de confirmación.
