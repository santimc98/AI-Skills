# Prompt Engineering Skill

## Cuándo usar esta skill

Usar esta skill cuando la tarea implique crear, auditar, mejorar o estructurar prompts e instrucciones para asistentes, agentes, automatizaciones o modelos de IA.

Usarla especialmente cuando haya que diseñar:

- system prompts para agentes;
- user prompts reutilizables;
- prompts para nodos AI Agent de n8n;
- prompts para Claude, ChatGPT, LibreChat, OpenClaw, Codex o asistentes internos;
- instrucciones con herramientas, MCPs, conectores o workflows;
- salidas estructuradas en JSON, Markdown, tablas o contratos operativos;
- prompts que deban ser reutilizables por un equipo.

## Objetivo

Convertir necesidades de trabajo en instrucciones claras, robustas y reutilizables para sistemas de IA.

La prioridad no es escribir un prompt bonito, sino construir una instrucción operativa que:

- reduzca ambigüedad;
- separe comportamiento estable de datos variables;
- controle el uso de herramientas;
- evite invenciones;
- defina formato de salida;
- permita evaluación y mejora iterativa;
- sea mantenible por otras personas.

## Entradas necesarias

Antes de diseñar el prompt, recopilar o inferir con supuestos explícitos:

- Objetivo real del agente o prompt.
- Contexto de uso: chat, n8n, Claude Code, LibreChat, MCP, API, workflow, documentación, etc.
- Usuario final del agente.
- Herramientas disponibles y límites de cada una.
- Datos de entrada esperados.
- Acciones permitidas y prohibidas.
- Riesgos: escritura en sistemas reales, publicación externa, datos sensibles, credenciales, operaciones irreversibles.
- Formato de salida deseado.
- Ejemplos de buenas y malas respuestas, si existen.
- Criterios para saber si la respuesta es correcta.

## Principio system prompt vs user prompt

Separar siempre lo estable de lo variable.

### System prompt

El system prompt debe contener el comportamiento estable del agente:

- rol;
- misión;
- alcance;
- herramientas disponibles;
- cuándo usar cada herramienta;
- restricciones de seguridad;
- política ante incertidumbre;
- formato de salida por defecto;
- criterios de calidad;
- criterios de escalado o parada;
- tono y estilo profesional.

No debe contener datos concretos de una ejecución salvo que sean reglas permanentes.

### User prompt

El user prompt debe contener la tarea concreta de esa ejecución:

- petición específica;
- datos variables;
- contexto recuperado de otros nodos;
- archivos, campos, mensajes o payloads concretos;
- objetivo inmediato;
- formato esperado para esa respuesta concreta;
- límites temporales o de alcance.

No debe repetir todas las reglas del sistema si ya están en el system prompt.

## Patrón recomendado para agentes con herramientas

Cuando el agente tenga herramientas, MCPs, APIs o conectores, diseñar el prompt con esta estructura:

```markdown
# Rol

Eres [rol del agente].

# Misión

Tu objetivo es [resultado principal].

# Alcance

Puedes ayudar con:
- ...

No debes:
- ...

# Herramientas

Tienes estas herramientas:

| Herramienta | Cuándo usarla | Cuándo no usarla | Riesgo |
|---|---|---|---|
| ... | ... | ... | ... |

# Procedimiento

1. Entiende la petición.
2. Comprueba si necesitas datos reales.
3. Usa herramientas solo cuando aporten evidencia o ejecuten una acción necesaria.
4. Separa hechos, inferencias y recomendaciones.
5. Valida la salida antes de responder.

# Reglas de seguridad

- No inventes datos.
- No ejecutes acciones destructivas sin confirmación explícita.
- No expongas secretos.
- No escribas en sistemas reales si la tarea solo pide análisis.

# Formato de respuesta

...

# Criterios de calidad

La respuesta es correcta si:
- ...
```

## Patrón recomendado para n8n AI Agent

En n8n, distinguir entre:

- **System Message**: reglas permanentes del agente.
- **Prompt/User Message**: input dinámico procedente del chat, webhook o nodos anteriores.
- **Output Parser**: contrato de salida cuando sea necesario JSON estricto.

Regla práctica:

```text
Si el workflow necesita herramientas, decisión autónoma y conversación flexible → usar AI Agent.
Si el workflow necesita obediencia estricta de formato, compliance o JSON cerrado → usar modelo básico + mensajes estructurados + parser/validador.
```

Para n8n, el user prompt debe evitar mezclar demasiada lógica. Lo ideal es pasar al modelo un payload claro:

```json
{
  "objetivo": "...",
  "entrada_usuario": "...",
  "contexto": { },
  "restricciones": [ ],
  "salida_esperada": "..."
}
```

## Procedimiento paso a paso

1. Identificar la tarea real que debe resolver el modelo.
2. Separar comportamiento estable, datos variables y formato de salida.
3. Definir si el prompt es para chat, agente con herramientas, workflow n8n, API o documentación.
4. Separar system prompt y user prompt.
5. Añadir reglas de decisión cuando haya varios caminos posibles.
6. Añadir criterios de uso de herramientas.
7. Añadir criterios de seguridad y escalado.
8. Añadir formato de salida.
9. Añadir ejemplos si reducen errores.
10. Revisar contradicciones.
11. Revisar si el prompt puede producir invenciones, acciones peligrosas o salidas ambiguas.
12. Preparar versión final lista para usar.

## Checklist de auditoría de prompts

Antes de dar el prompt como final, comprobar:

- ¿Está claro qué debe hacer el agente?
- ¿Está claro qué no debe hacer?
- ¿El system prompt contiene reglas estables y no datos efímeros?
- ¿El user prompt contiene datos variables y no repite reglas innecesarias?
- ¿Las herramientas tienen criterios de uso concretos?
- ¿Hay política ante falta de información?
- ¿Hay política ante errores de herramientas?
- ¿La salida esperada está definida?
- ¿Hay riesgo de inventar datos?
- ¿Hay riesgo de escribir, publicar, enviar o borrar algo sin confirmación?
- ¿Hay instrucciones contradictorias?
- ¿Se puede probar con ejemplos reales?

## Criterios de calidad

- El prompt debe ser claro y accionable.
- Debe indicar qué hacer cuando falta información.
- Debe definir formato de salida.
- Debe evitar instrucciones contradictorias.
- Debe ser mantenible y fácil de editar.
- Debe separar system prompt y user prompt cuando se use en agentes.
- Debe incluir reglas de uso de herramientas si el agente puede llamar MCPs, APIs o conectores.
- Debe incluir criterios de evaluación o validación.
- Debe proteger credenciales, datos sensibles y acciones con impacto externo.

## Formato de salida esperado

Cuando el usuario pida crear un prompt completo para un agente, responder con:

```markdown
# System prompt

...

# User prompt template

...

# Variables esperadas

| Variable | Descripción | Obligatoria | Ejemplo |
|---|---|---|---|

# Criterios de validación

...

# Casos de prueba recomendados

...
```

Cuando el usuario pida auditar un prompt existente, responder con:

```markdown
## Diagnóstico

## Problemas detectados

## Versión corregida

## Por qué mejora

## Pruebas recomendadas
```

## Errores comunes a evitar

- Crear prompts demasiado largos sin estructura.
- Mezclar instrucciones obligatorias con preferencias.
- Mezclar system prompt y datos variables de ejecución.
- No definir salida esperada.
- No indicar cómo actuar ante incertidumbre.
- No contemplar errores de herramientas.
- Permitir acciones externas sin confirmación.
- Pedir JSON estricto sin parser o validación posterior.
- Meter credenciales, tokens o secretos dentro del prompt.
- Diseñar un agente autónomo sin límites claros de herramientas.

## Referencias internas

- `skills/prompt-engineering/references/system-vs-user-prompt.md`
- `skills/prompt-engineering/references/agent-prompt-template.md`
- `skills/prompt-engineering/references/n8n-ai-agent-prompt-template.md`
- `knowledge/quality-standards.md`

## Referencias externas a revisar antes de copiar patrones

Estas fuentes son referencias de inspiración, no contenido para copiar literalmente sin auditoría:

- `ckelsoe/prompt-architect` — frameworks de diseño de prompts y prompts para múltiples asistentes.
- `NeoLabHQ/context-engineering-kit` — patrones de prompt engineering, jerarquía de instrucciones, evaluación y versionado.
- `nidhinjs/prompt-master` — generación práctica de prompts listos para herramientas.

Antes de reutilizar contenido externo, revisar licencia, seguridad, instrucciones ocultas y compatibilidad con el contexto corporativo.
