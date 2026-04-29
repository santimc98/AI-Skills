# n8n Workflow Engineering

## Cuándo usar esta skill

Usar esta skill cuando Santi pida auditar, revisar, depurar, editar, documentar o crear workflows de n8n, especialmente si la tarea implica nodos, conexiones, credenciales, expresiones, código, ejecuciones, errores, MCP, agentes IA o automatizaciones en producción.

También debe usarse cuando una tarea toque workflows que publican contenido externo, envían mensajes, crean registros, escriben en memoria o ejecutan acciones con impacto fuera de n8n.

## Objetivo

Trabajar con n8n con mentalidad de producción:

- robustez,
- trazabilidad,
- seguridad,
- facilidad de depuración,
- cambios mínimos,
- validación posterior,
- prevención de publicaciones o acciones incorrectas.

El objetivo no es solo que el workflow funcione una vez, sino que sea mantenible, observable y seguro ante fallos parciales.

## Entradas necesarias

Antes de actuar, recopilar o confirmar solo la información crítica:

- Nombre exacto del workflow.
- Objetivo funcional del workflow.
- Ejecución afectada, si existe un fallo concreto.
- Nodo donde aparece el error, si el usuario lo conoce.
- Resultado esperado.
- Riesgo externo: publicación, email, webhook, escritura en base de datos, CRM, memoria o API externa.
- Restricciones explícitas del usuario: no publicar, no tocar credenciales, no activar workflow, no borrar datos, etc.

Si hay acceso MCP a n8n y la tarea requiere tocar n8n, hacer primero un health check.

## Procedimiento paso a paso

### 1. Health check inicial

Si la tarea requiere interactuar con n8n mediante MCP, empezar comprobando que la instancia responde correctamente.

Verificar, según las herramientas disponibles:

1. Conectividad con n8n.
2. Acceso a workflows.
3. Acceso a ejecuciones.
4. Permisos suficientes para leer antes de escribir.
5. Si el workflow está activo o desactivado.

No modificar nada durante el health check.

### 2. Diagnosticar antes de editar

Antes de aplicar cambios:

1. Leer la estructura del workflow.
2. Identificar nodos relevantes.
3. Revisar conexiones.
4. Revisar expresiones críticas.
5. Revisar código en nodos Code/Function.
6. Revisar ejecuciones recientes si el problema viene de una ejecución.
7. Separar hechos confirmados de hipótesis.

No editar por intuición sin haber localizado la causa probable.

### 3. Revisión de ejecuciones fallidas

Para cada bug o ejecución fallida, identificar de forma explícita:

- Ejecución afectada.
- Nodo exacto que falla.
- Error exacto reportado por n8n.
- Entrada recibida por el nodo.
- Salida esperada.
- Causa raíz.
- Solución mínima segura.

Si hay varios errores encadenados, resolver primero el error más cercano a la causa raíz, no solo el último síntoma.

### 4. Política de cambios

Aplicar siempre cambios mínimos y seguros.

Reglas obligatorias:

- No borrar workflows salvo instrucción explícita de Santi.
- No modificar credenciales salvo instrucción explícita de Santi.
- No publicar, activar, desactivar o ejecutar acciones externas si no es necesario para validar.
- No sobrescribir lógica compleja si basta con corregir una expresión, conexión o validación.
- No eliminar validaciones de seguridad para que el workflow “pase”.
- No ocultar errores críticos con valores por defecto peligrosos.

Antes de cambios peligrosos, explicar brevemente qué se va a tocar y por qué.

### 5. Validar después de modificar

Después de cualquier cambio:

1. Validar que el workflow conserva su estructura esperada.
2. Revisar que las conexiones siguen siendo correctas.
3. Revisar expresiones modificadas.
4. Revisar nodos afectados por el cambio.
5. Ejecutar o revisar una ejecución de prueba cuando sea seguro.
6. Confirmar que no aparecen errores nuevos aguas abajo.
7. Si hay publicación externa, verificar los controles previos antes de permitir salida.

### 6. Workflows con publicación o impacto externo

Para workflows que publican en LinkedIn, envían emails, llaman APIs externas, escriben en memoria o hacen acciones públicas:

- Preferir fallar antes que publicar contenido truncado, vacío o incorrecto.
- Validar longitud mínima y máxima del contenido.
- Validar que no falten título, cuerpo, enlaces, hashtags o imagen si son obligatorios.
- Validar que no se publique contenido de prueba.
- Validar que el texto final sea el texto completo esperado, no una versión resumida accidental.
- Validar que las variables usadas por el nodo final existen realmente.
- Validar que los nodos referenciados en expresiones existen y mantienen el nombre esperado.

## Criterios de calidad

Un diagnóstico o cambio en n8n se considera correcto si:

- La causa raíz está identificada, no solo el síntoma.
- El nodo exacto afectado queda claro.
- La solución es mínima y reversible.
- El workflow queda más seguro que antes.
- Se evita introducir dependencias ocultas.
- Se mantiene trazabilidad de entradas, salidas y nodos afectados.
- La validación posterior confirma el resultado.
- La explicación permite a Santi entender qué pasó y cómo evitarlo.

## Formato de salida esperado

Responder siempre separando estas secciones cuando se haya diagnosticado o modificado algo:

```markdown
## Diagnóstico

## Cambio aplicado

## Resultado

## Siguiente acción recomendada
```

Si solo se está proponiendo una arquitectura o creando un workflow nuevo, usar:

```markdown
## Objetivo

## Diseño propuesto

## Workflow paso a paso

## Validaciones de seguridad

## Siguiente acción recomendada
```

## Errores comunes a evitar

- Editar antes de diagnosticar.
- Cambiar varios nodos a la vez sin necesidad.
- Borrar workflows, ejecuciones o credenciales sin instrucción explícita.
- Cambiar credenciales para probar hipótesis.
- Referenciar nodos por nombres que ya no existen.
- Usar datos de un nodo recortado cuando se necesita el texto completo.
- Publicar contenido externo sin validar longitud, estructura y campos obligatorios.
- Confundir el error final con la causa raíz.
- No revisar nodos aguas abajo después de corregir un nodo anterior.
- No explicar claramente qué se cambió.

## Plantillas relacionadas

No hay plantillas obligatorias todavía.

Cuando se creen plantillas para auditoría o documentación de workflows, ubicarlas preferentemente en `templates/`.

## Conocimiento relacionado

- `skills/linkedin-ai-news-workflow/SKILL.md` para el workflow principal de noticias de IA hacia LinkedIn.
- `skills/ai-research/SKILL.md` cuando la tarea incluya investigación o selección de noticias/modelos/herramientas de IA.
- `skills/prompt-engineering/SKILL.md` cuando la tarea incluya prompts para agentes, AI Writer o nodos LLM.
