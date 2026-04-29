# LinkedIn AI News Workflow

## Cuándo usar esta skill

Usar esta skill cuando Santi pida revisar, auditar, depurar, mejorar, documentar o extender el workflow de n8n:

`AI News → LinkedIn (daily, o3-deep-research)`

Este workflow publica automáticamente noticias de inteligencia artificial en LinkedIn para posicionar a Santi como divulgador de IA, automatización y agentes.

Esta skill debe combinarse con `skills/n8n-workflow-engineering/SKILL.md` para cualquier acción técnica sobre n8n.

## Objetivo del workflow

Publicar diariamente en LinkedIn un post completo, claro y seguro sobre noticias relevantes de inteligencia artificial.

El resultado editorial esperado es:

- Post completo.
- Título claro.
- Título en negrita compatible con LinkedIn.
- Hashtags generados por el AI Writer.
- Imagen generada.
- Link o referencia cuando aplique.
- Publicación segura, sin truncados, sin texto vacío y sin contenido incorrecto.

## Ruta principal de nodos

La ruta principal puede evolucionar, pero la lógica funcional esperada es:

```text
Disparador diario
  ↓
Búsqueda/investigación de noticias de IA
  ↓
Selección y filtrado editorial
  ↓
AI Writer
  ↓
Consolidar Post + Hashtags
  ↓
Generación de imagen
  ↓
base64 → binario n8n
  ↓
Adjuntar texto + link
  ↓
Publicación en LinkedIn
  ↓
ai_linkedin_memory
```

Al auditar el workflow, confirmar siempre la ruta real en n8n, porque los nombres exactos de nodos pueden cambiar.

## Reglas para construir el post final

El texto final que llega al nodo de publicación debe construirse desde el contenido completo generado por el AI Writer, no desde una versión recortada, resumen, preview o variable intermedia truncada.

Estructura recomendada:

```markdown
**Título claro del post**

Cuerpo completo del post.

Hashtags generados por el AI Writer.
```

Reglas obligatorias:

1. El título debe ir al inicio.
2. El título debe estar en formato `**Título**`, compatible visualmente con LinkedIn.
3. El cuerpo debe ser el texto completo preparado para publicar.
4. Los hashtags deben ir al final.
5. Los hashtags deben proceder del AI Writer cuando el workflow esté diseñado así.
6. No duplicar hashtags si ya vienen incluidos correctamente.
7. No publicar si falta el cuerpo principal.
8. No publicar si el texto final es sospechosamente corto.
9. No publicar si el texto final excede el límite de seguridad configurado.
10. No sustituir contenido completo por campos de preview, resumen o snippets.

## Control de título

El título debe ser:

- claro,
- específico,
- alineado con el contenido,
- no clickbait,
- breve pero informativo,
- colocado en la primera línea,
- envuelto como `**Título**`.

Antes de publicar, validar:

- que existe título,
- que no está vacío,
- que no contiene placeholders,
- que corresponde a la noticia elegida,
- que no se ha perdido al pasar entre nodos.

## Control de hashtags

Los hashtags deben ser generados o definidos por el AI Writer según la lógica editorial del workflow.

Criterios:

- Deben estar relacionados con IA, automatización, agentes, tecnología o el tema concreto del post.
- Deben aparecer al final del post.
- No deben reemplazar el cuerpo.
- No deben aparecer como `undefined`, `null`, array sin procesar o JSON crudo.
- No deben duplicarse si el AI Writer ya los incluyó.

Ejemplos de familias de hashtags aceptables:

- `#InteligenciaArtificial`
- `#IA`
- `#Automatización`
- `#AgentesIA`
- `#n8n`
- `#Productividad`
- `#Tecnología`

## Control de imagen

El workflow debe generar una imagen y convertirla correctamente a binario n8n antes de adjuntarla o publicarla.

Validar:

- que existe imagen generada,
- que la imagen no está vacía,
- que el base64 se convierte a binario correctamente,
- que el nodo final toma la imagen desde `base64 → binario n8n` o desde el nodo real equivalente,
- que el campo binario esperado por LinkedIn existe,
- que no se intenta publicar una imagen rota o inexistente.

Si la imagen es obligatoria para la publicación, preferir fallar antes que publicar sin imagen.

## Reglas para `ai_linkedin_memory`

La memoria `ai_linkedin_memory` debe usarse para evitar duplicados y mantener trazabilidad editorial.

Reglas:

1. Registrar solo publicaciones correctas o estados claramente controlados.
2. No registrar como publicada una ejecución que falló antes de publicar.
3. No conservar entradas defectuosas que puedan bloquear o contaminar futuras selecciones.
4. Si se elimina una fila defectuosa, documentar por qué se eliminó.
5. No borrar memoria válida salvo instrucción explícita de Santi.
6. Antes de tocar memoria, identificar qué fila se va a tocar y qué impacto tiene.
7. Mantener campos suficientes para reconocer noticia, fecha, título, enlace y estado si existen.

## Errores conocidos ya corregidos

### Referencia a nodo inexistente

En la ejecución del 29/04, el nodo `Adjuntar texto + link` falló porque referenciaba un nodo inexistente llamado `Alt text (accesibilidad)`.

Corrección aplicada:

- `Adjuntar texto + link` pasó a tomar el texto desde `Consolidar Post + Hashtags`.
- La imagen pasó a tomarse desde `base64 → binario n8n`.

Prevención:

- Validar que todo nodo referenciado en expresiones existe.
- Evitar dependencias a nombres de nodos eliminados o renombrados.

### Publicación truncada

Después de corregir el error anterior, hubo una publicación truncada porque se estaba usando una versión recortada del texto.

Corrección aplicada:

- `Consolidar Post + Hashtags` pasó a usar el texto completo del AI Writer.
- Se añadió el título arriba como `**Título**`.
- Se añadieron hashtags al final.
- Se añadieron validaciones para fallar antes de publicar si el texto era demasiado corto o demasiado largo.
- Se eliminó de `ai_linkedin_memory` la fila de la publicación defectuosa.
- La publicación final se relanzó correctamente.

Prevención:

- No usar campos de preview, resumen o texto truncado para publicar.
- Añadir controles de longitud y completitud antes del nodo de LinkedIn.

## Criterios de seguridad antes de publicar

Antes de permitir la publicación en LinkedIn, validar:

- Existe texto final.
- El texto final no está vacío.
- El texto final no es demasiado corto.
- El texto final no supera el límite de seguridad configurado.
- El título existe y está al inicio.
- El título usa formato `**Título**`.
- El cuerpo completo está presente.
- Los hashtags están presentes y al final si son obligatorios.
- La imagen existe si es obligatoria.
- El binario de imagen existe y es legible.
- No hay placeholders como `undefined`, `null`, `N/A`, `TODO`, `lorem ipsum` o JSON crudo.
- El link existe si el diseño editorial lo requiere.
- La noticia no está duplicada según `ai_linkedin_memory`.
- El nodo final no referencia nodos inexistentes.
- No se está publicando una ejecución de prueba por error.

Regla principal: si hay duda razonable, fallar antes de publicar.

## Procedimiento de auditoría del workflow

1. Hacer health check de n8n si se va a tocar la instancia.
2. Revisar la estructura actual del workflow.
3. Confirmar la ruta real de nodos.
4. Revisar últimas ejecuciones.
5. Identificar errores por ejecución, nodo, mensaje y causa raíz.
6. Revisar `Consolidar Post + Hashtags`.
7. Revisar `Adjuntar texto + link`.
8. Revisar generación y conversión de imagen.
9. Revisar nodo de publicación en LinkedIn.
10. Revisar escritura en `ai_linkedin_memory`.
11. Aplicar cambios mínimos.
12. Validar una ejecución segura.
13. Separar diagnóstico, cambio aplicado, resultado y siguiente acción recomendada.

## Formato de salida esperado

Cuando se revise este workflow, responder con:

```markdown
## Diagnóstico

## Cambio aplicado

## Resultado

## Siguiente acción recomendada
```

Si solo se propone una mejora editorial o técnica, responder con:

```markdown
## Objetivo

## Propuesta

## Riesgos que reduce

## Cómo validarlo

## Siguiente acción recomendada
```

## Errores comunes a evitar

- Publicar desde una variable truncada.
- Usar un nodo inexistente en una expresión.
- Generar hashtags fuera del AI Writer si el workflow espera que los genere él.
- Publicar sin imagen cuando la imagen es parte obligatoria del diseño.
- Escribir en memoria antes de confirmar publicación correcta.
- Borrar filas válidas de memoria.
- Cambiar credenciales de LinkedIn para resolver errores de contenido.
- Quitar validaciones de seguridad para desbloquear una ejecución.
- Relanzar una ejecución sin comprobar qué contenido final va a publicar.

## Plantillas relacionadas

No hay plantillas obligatorias todavía.

Puede añadirse más adelante una plantilla de auditoría para publicaciones LinkedIn en `templates/`.

## Conocimiento relacionado

- `skills/n8n-workflow-engineering/SKILL.md`
- `skills/ai-research/SKILL.md`
- `skills/prompt-engineering/SKILL.md`
