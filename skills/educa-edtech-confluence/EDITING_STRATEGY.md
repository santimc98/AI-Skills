# Confluence Editing Strategy — Educa Edtech

Este documento complementa `SKILL.md` y define cuál es la forma más segura de editar páginas de Confluence con asistentes de IA.

## Conclusión operativa

Para un humano suele ser más natural editar directamente secciones concretas dentro de la página. Para un LLM con herramientas, la forma más segura depende del tamaño y criticidad del cambio.

Regla general:

```text
Cambios pequeños y localizados → edición por bloques/secciones.
Cambios grandes o reestructuración → crear borrador V2 completo y reemplazar solo tras validación.
```

---

## 1. Por qué no conviene reemplazar siempre la página completa

Actualizar una página completa en una sola llamada puede tener riesgos:

- Puede activar bloqueos de seguridad del conector si el contenido es largo, contiene enlaces, tablas o fórmulas.
- Puede perder matices del formato original de Confluence.
- Puede sobrescribir cambios recientes hechos por otra persona.
- Puede eliminar comentarios contextuales, macros o elementos que no se representen bien en Markdown.
- Puede introducir demasiados cambios de golpe, dificultando la revisión.

Por tanto, no es recomendable reemplazar una página completa salvo que el usuario haya aprobado una versión final o se trate de una página nueva/borrador.

---

## 2. Por qué tampoco conviene editar “como humano” sin plan

Editar pequeñas partes sin una estrategia también tiene riesgos:

- El LLM puede no localizar exactamente la sección correcta.
- Puede dejar inconsistencias entre secciones.
- Puede actualizar una fórmula o explicación en un sitio y olvidarla en otro.
- Puede no actualizar metadatos, versión o histórico de cambios.

Por tanto, la edición por partes debe hacerse con mapa de cambios previo.

---

## 3. Estrategias disponibles

### Estrategia A — Comentario de revisión

Usar cuando:

- Todavía no hay aprobación del owner.
- Solo se quiere dejar feedback.
- La página es sensible o está en revisión.
- El usuario quiere evitar modificar contenido oficial.

Acción:

```text
Crear comentario footer con hallazgos, recomendaciones y próximos pasos.
```

Ventaja: muy seguro.  
Desventaja: no actualiza el contenido principal.

---

### Estrategia B — Edición puntual por sección

Usar cuando:

- El cambio afecta a una sección concreta.
- El usuario ya ha aprobado qué sección tocar.
- La página no tiene macros complejas en esa zona.
- El cambio es pequeño o medio.

Flujo:

```text
1. Leer página actual.
2. Identificar sección exacta.
3. Proponer texto nuevo de esa sección.
4. Confirmar con usuario.
5. Actualizar página manteniendo el resto intacto.
6. Actualizar metadatos/histórico si procede.
```

Ejemplos:

- Añadir una sección de limitaciones.
- Corregir una fórmula.
- Actualizar próximos pasos.
- Añadir un apartado de riesgos.

Ventaja: menos invasivo.  
Desventaja: requiere precisión y puede ser frágil si la página es larga.

---

### Estrategia C — Borrador V2 en página nueva

Usar cuando:

- El cambio afecta a muchas secciones.
- Hay rediseño metodológico.
- La página actual está pendiente de revisión por owner.
- Se quiere comparar v1 vs v2.
- No se debe tocar la página oficial todavía.

Flujo:

```text
1. Leer página original.
2. Crear página hija o borrador con título: [Original] — Propuesta v2.
3. Escribir versión completa revisada.
4. Enlazar la página original y el borrador entre sí.
5. Pedir revisión del owner.
6. Si se aprueba, reemplazar o fusionar en la página oficial.
```

Ventaja: muy segura para cambios grandes.  
Desventaja: genera una página adicional que luego hay que archivar, fusionar o eliminar manualmente.

---

### Estrategia D — Reemplazo completo de página oficial

Usar solo cuando:

- El usuario confirma explícitamente que quiere reemplazar la página oficial.
- La versión nueva ya ha sido validada.
- No hay cambios recientes de terceros pendientes.
- La página no contiene macros o elementos complejos que puedan perderse.
- El cuerpo no es tan largo como para activar bloqueos del conector.

Flujo:

```text
1. Leer la página oficial.
2. Crear backup textual o borrador V2.
3. Confirmar reemplazo con el usuario.
4. Actualizar página completa.
5. Revisar resultado leyendo la página publicada.
6. Corregir si algo se ha perdido.
```

Ventaja: deja la página limpia y coherente.  
Desventaja: es la opción con más riesgo operativo.

---

## 4. Matriz de decisión

| Situación | Estrategia recomendada |
|---|---|
| Solo feedback o revisión pendiente | A — Comentario |
| Cambio pequeño aprobado | B — Edición puntual |
| Cambio medio en 1–2 secciones | B — Edición puntual |
| Cambio metodológico importante | C — Borrador V2 |
| Reestructuración completa | C — Borrador V2 |
| Página oficial ya aprobada para sustituir | D — Reemplazo completo |
| Página con macros, enlaces o tablas complejas | A o C, evitar D |
| Página sensible o visible por dirección | A primero, C después |

---

## 5. Regla para páginas pendientes de revisión por owner

Si una página está pendiente de revisión por Lorena u otro owner:

```text
No modificar la página oficial salvo instrucción explícita.
```

Trabajar así:

1. Crear comentario de revisión, o
2. Crear página propuesta v2, o
3. Preparar texto listo para pegar manualmente.

---

## 6. Regla para actualización por secciones

Cuando se edite por secciones, antes de ejecutar hay que producir este plan:

```markdown
## Plan de edición Confluence

Página: [Título]
Page ID: [ID]
Estrategia: Edición puntual / Borrador V2 / Reemplazo completo

### Secciones que se tocarán
| Sección actual | Acción | Motivo |
|---|---|---|

### Secciones que NO se tocarán
- 

### Cambios de metadatos
- Versión:
- Última actualización:
- Histórico de cambios:

### Riesgos
- 
```

No ejecutar la edición hasta que el usuario confirme si la página es relevante o visible para el equipo.

---

## 7. Preferencia para el sistema IMO / scoring

Para la página del sistema de scoring IMO:

```text
Estrategia recomendada actual: C — Borrador V2 o comentario de revisión.
```

Motivo:

- Está pendiente de revisión por Lorena.
- Hay cambios metodológicos relevantes.
- La versión oficial no debería modificarse hasta validación.
- Es mejor dejar propuesta revisable antes de sustituir.

Cuando Lorena dé visto bueno:

```text
1. Preparar plan de edición por secciones.
2. Actualizar primero secciones metodológicas.
3. Actualizar después resultados/snapshot si procede.
4. Actualizar histórico de cambios.
5. Leer la página publicada para verificar.
```

---

## 8. Regla final

La opción más segura para un LLM no es siempre la más cómoda para un humano.

```text
Humano: suele preferir editar directamente.
LLM con herramientas: debe preferir planificar, proponer, crear borrador V2 si el cambio es grande, y editar por secciones solo cuando el cambio esté claramente delimitado.
```

Nunca hacer reemplazo completo de una página importante sin backup, validación y confirmación explícita.
