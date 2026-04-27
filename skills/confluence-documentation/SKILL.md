# Confluence Documentation Skill

## Cuándo usar esta skill

Usar esta skill cuando la tarea implique crear, mejorar o estructurar documentación para Confluence o documentación interna equivalente.

## Objetivo

Transformar información técnica, funcional o desordenada en documentación clara, útil, mantenible y orientada a equipos de trabajo.

## Entradas necesarias

- Tema o proceso que se quiere documentar.
- Audiencia: técnica, negocio, dirección, producto u operaciones.
- Nivel de detalle esperado.
- Estado del contenido: borrador, notas, reunión, análisis, decisión o procedimiento.
- Enlaces o documentos relacionados, si existen.

## Procedimiento paso a paso

1. Entender el objetivo de la página.
2. Identificar la audiencia y adaptar el nivel de detalle.
3. Organizar el contenido en secciones claras.
4. Separar contexto, decisión, procedimiento, riesgos y próximos pasos.
5. Usar títulos descriptivos.
6. Incluir tablas cuando faciliten comprensión.
7. Añadir checklist, criterios o pasos accionables si procede.
8. Preparar el resultado en Markdown compatible con copia a Confluence.

## Criterios de calidad

- La página debe poder entenderse sin contexto oral adicional.
- Debe quedar claro qué es información confirmada y qué es propuesta.
- Debe tener estructura navegable.
- Debe evitar redacción excesivamente comercial si es documentación interna.
- Debe incluir próximos pasos cuando haya trabajo pendiente.

## Formato de salida esperado

Estructura recomendada:

```markdown
# Título

## Resumen

## Contexto

## Objetivo

## Desarrollo / Procedimiento

## Decisiones

## Riesgos o consideraciones

## Próximos pasos

## Referencias
```

## Errores comunes a evitar

- Crear páginas largas sin jerarquía.
- Mezclar decisiones con ideas pendientes.
- No dejar claro quién debe actuar.
- Usar lenguaje ambiguo.
- Omitir contexto necesario.

## Plantillas relacionadas

- `templates/confluence-page-template.md`
- `templates/executive-summary-template.md`

## Conocimiento relacionado

- `knowledge/company-writing-style.md`
- `knowledge/team-processes.md`
- `knowledge/quality-standards.md`
