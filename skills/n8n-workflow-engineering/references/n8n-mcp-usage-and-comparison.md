# n8n MCP usage and comparison

## Objetivo

Esta referencia sirve para trabajar con MCPs de n8n desde Claude, ChatGPT, LibreChat u otros clientes, y para comparar un MCP público de n8n con un MCP interno corporativo de Operaciones.

## MCP público de referencia

Repositorio recomendado para comparar:

```text
https://github.com/czlonkowski/n8n-mcp
```

Uso principal esperado:

- consultar documentación de nodos n8n;
- buscar nodos y operaciones;
- validar configuración de nodos;
- inspeccionar plantillas;
- ayudar a construir workflows con mayor conocimiento del ecosistema n8n;
- servir como copiloto técnico para diseño y validación de workflows.

## MCP interno de Operaciones

Uso principal esperado:

- conectar con la instancia real o test de n8n de Operaciones;
- listar workflows existentes;
- leer estructura resumida de workflows;
- revisar ejecuciones o errores si la API lo permite;
- operar bajo autenticación y redacción de secretos;
- limitar acciones según política interna;
- exponer solo herramientas necesarias para el contexto corporativo.

## Diferencia conceptual

| Aspecto | MCP público n8n-mcp | MCP interno Operaciones |
|---|---|---|
| Finalidad | Knowledge técnico del ecosistema n8n y ayuda de construcción | Operación controlada sobre la instancia de n8n de la empresa |
| Fuente de verdad | Catálogo/documentación/templates de n8n | Instancia real/test de n8n y workflows internos |
| Riesgo | Bajo/medio si solo consulta documentación | Medio/alto si puede leer o modificar workflows reales |
| Mejor uso | Diseñar, validar nodos, descubrir alternativas node-first | Auditar workflows internos, depurar errores, exportar/importar o revisar estado real |
| Seguridad | Revisar permisos, instalación y alcance | Auth obligatoria, redacción de secretos, mínimos privilegios |
| Producción | No debe tocar producción si no está diseñado para ello | Debe separar claramente test, staging y producción |

## Cómo pedirle a Claude Code que compare ambos MCPs

Prompt recomendado:

```text
Quiero que compares este MCP público de n8n:
https://github.com/czlonkowski/n8n-mcp

con nuestro MCP interno de Operaciones para n8n ubicado en el repositorio corporativo.

Analiza:
1. Herramientas expuestas por cada MCP.
2. Diferencias de arquitectura.
3. Diferencias de seguridad y autenticación.
4. Diferencias de permisos reales sobre n8n.
5. Qué capacidades del MCP público nos conviene incorporar.
6. Qué capacidades no debemos incorporar por riesgo operativo.
7. Qué mejoras harías a nuestro MCP interno.
8. Qué endpoints/tools deberían quedar read-only.
9. Qué endpoints/tools requerirían confirmación humana.
10. Qué cambios propones en README, SECURITY y .env.example.

No implementes cambios todavía. Primero devuelve diagnóstico, tabla comparativa y plan de mejora priorizado.
```

## Checklist de seguridad antes de usar cualquier MCP de n8n

- Revisar código fuente antes de conectarlo a una instancia real.
- Confirmar si puede escribir, borrar, activar o ejecutar workflows.
- Confirmar si devuelve credenciales, variables de entorno o secretos.
- Activar autenticación si se expone por HTTP.
- No exponerlo públicamente sin HTTPS y Bearer token.
- Usar instancia test antes de producción.
- Redactar secretos en respuestas.
- Limitar herramientas de escritura por defecto.
- Registrar qué cliente lo consume: Claude Code, LibreChat, ChatGPT, etc.

## Reglas de adopción interna

1. El MCP público puede servir como referencia técnica, no como sustituto automático del MCP interno.
2. El MCP interno debe priorizar seguridad, trazabilidad y mínimos privilegios.
3. Las capacidades de escritura deben estar desactivadas o protegidas por confirmación explícita.
4. Las herramientas de consulta deben devolver resúmenes útiles, no JSON masivo con secretos.
5. Toda mejora copiada de un proyecto externo debe revisarse por licencia, seguridad y compatibilidad.
