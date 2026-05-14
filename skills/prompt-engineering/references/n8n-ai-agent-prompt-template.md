# n8n AI Agent prompt template

Usar esta referencia cuando se diseñen prompts para nodos AI Agent, LLM Chain, Basic LLM Chain, Information Extractor, Text Classifier o workflows con agentes en n8n.

## Decisión rápida

```text
AI Agent node = cuando hacen falta herramientas, memoria, decisión autónoma o conversación flexible.
Modelo básico + mensajes estructurados + parser = cuando hace falta salida estricta, JSON cerrado o compliance fuerte.
```

## System Message recomendado

```text
Eres un agente dentro de un workflow de n8n.

Tu tarea es [OBJETIVO DEL AGENTE] usando únicamente la información recibida en el input y las herramientas disponibles.

Reglas obligatorias:
1. No inventes datos que no estén en el input o no puedas verificar con herramientas.
2. Si falta un dato crítico, devuelve una respuesta controlada indicando el dato faltante.
3. Usa herramientas solo cuando sean necesarias para completar la tarea.
4. No ejecutes acciones externas si la instrucción no lo requiere claramente.
5. Si una herramienta devuelve error, no lo ocultes: devuelve una respuesta de error útil para el workflow.
6. Respeta exactamente el formato de salida solicitado.
7. No incluyas razonamiento interno ni pasos ocultos en la respuesta final.

Formato de salida:
[DESCRIBIR FORMATO: JSON / TEXTO / CAMPOS]
```

## User Message recomendado

Pasar el input como objeto estructurado, no como texto largo desordenado.

```text
Tarea concreta:
{{ $json.task }}

Input del usuario:
{{ $json.user_input }}

Contexto del workflow:
{{ JSON.stringify($json.context) }}

Restricciones de esta ejecución:
{{ JSON.stringify($json.constraints) }}

Salida esperada:
{{ $json.expected_output }}
```

## JSON output recomendado

Cuando el workflow dependa de campos concretos, pedir JSON y validar después.

```json
{
  "status": "ok | needs_more_info | error",
  "answer": "respuesta para usuario o siguiente nodo",
  "missing_fields": [],
  "confidence": "high | medium | low",
  "actions_taken": [],
  "next_step": "continue | ask_user | stop | escalate"
}
```

## Campos mínimos para agentes de reserva, soporte o operaciones

```json
{
  "intent": "",
  "required_action": "",
  "entities": {},
  "missing_fields": [],
  "response_to_user": "",
  "should_call_tool": false,
  "tool_name": null,
  "tool_input": {},
  "risk_level": "low | medium | high"
}
```

## Validaciones posteriores en n8n

Después del nodo IA, añadir validaciones con IF, Code o Structured Output Parser:

- `status` existe.
- `status` pertenece a valores permitidos.
- Si `status = ok`, existen los campos necesarios.
- Si `status = needs_more_info`, existe `missing_fields`.
- Si hay acción externa, `risk_level` no debe ser `high` sin confirmación.
- Si se publica/envía contenido, validar longitud, campos obligatorios y ausencia de placeholders.

## Errores frecuentes en n8n

- Meter toda la lógica en el prompt y no validar después.
- Pedir JSON estricto sin parser ni nodo de validación.
- Pasar input desordenado procedente de muchos nodos.
- Referenciar nodos por nombre y luego renombrarlos.
- Usar AI Agent cuando bastaba un modelo simple con salida estructurada.
- Usar modelo simple cuando el flujo necesita herramientas y decisión iterativa.
- No controlar errores de herramientas.
- No diferenciar entre respuesta al usuario y datos para el siguiente nodo.

## Plantilla de decisión para usar en documentación

```text
Objetivo del nodo IA:
Tipo de nodo elegido: AI Agent / Basic LLM Chain / Information Extractor / Text Classifier / otro
Motivo:
Herramientas disponibles:
Formato de salida:
Validador posterior:
Riesgos:
```
