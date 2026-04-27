# Meeting Notes Skill

## Cuándo usar esta skill

Usar esta skill cuando la tarea implique resumir reuniones, extraer decisiones, generar actas o convertir conversaciones en próximos pasos accionables.

## Objetivo

Convertir información hablada o notas desordenadas en un resumen claro, estructurado y útil para seguimiento.

## Entradas necesarias

- Transcripción, notas o resumen de la reunión.
- Participantes, si se conocen.
- Fecha, si aplica.
- Objetivo de la reunión.
- Destino del resultado: Confluence, Jira, correo, informe interno o seguimiento personal.

## Procedimiento paso a paso

1. Identificar tema principal y objetivo de la reunión.
2. Extraer decisiones confirmadas.
3. Separar acuerdos de ideas pendientes.
4. Identificar tareas, responsables y fechas si aparecen.
5. Señalar dudas abiertas o riesgos.
6. Preparar una salida clara para seguimiento.
7. Si procede, proponer issues de Jira derivados.

## Criterios de calidad

- Las decisiones deben quedar claramente separadas de las discusiones.
- Las tareas deben incluir responsable y fecha cuando existan.
- No inventar asistentes, fechas ni responsables.
- El resumen debe ser breve pero suficiente.

## Formato de salida esperado

```markdown
# Acta de reunión

## Resumen

## Temas tratados

## Decisiones

## Acciones pendientes

## Riesgos o bloqueos

## Próximos pasos
```

## Errores comunes a evitar

- Confundir propuestas con decisiones.
- Asignar responsables no mencionados.
- Perder tareas accionables.
- Redactar un acta demasiado larga sin utilidad práctica.

## Plantillas relacionadas

- `templates/meeting-notes-template.md`
- `templates/jira-issue-template.md`

## Conocimiento relacionado

- `knowledge/team-processes.md`
