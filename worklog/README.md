# AI Worklog

Este directorio funciona como memoria operativa compartida entre asistentes de IA como ChatGPT, Claude, LibreChat u otros agentes.

No sustituye a Jira ni a Confluence.

```text
Worklog = memoria operativa entre asistentes
Jira = tareas oficiales del equipo
Confluence = conocimiento estable del equipo
SharePoint = archivos fuente y documentación de trabajo
```

## Cómo usarlo

### Al iniciar una sesión

1. Leer `index.md`.
2. Leer `skills/ai-worklog-sync/SKILL.md`.
3. Leer `worklog/current-week.md`.
4. Leer el worklog semanal activo.
5. Leer pendientes de Jira o Confluence si aplica.

### Al cerrar una sesión

Actualizar:

- `worklog/sessions/` con el registro detallado de la sesión.
- `worklog/weekly/YYYY-Www.md` con resumen acumulado.
- `worklog/tasks/pending-jira-actions.md` si hay acciones candidatas a Jira.
- `worklog/tasks/pending-confluence-pages.md` si hay páginas candidatas a Confluence.
- `worklog/decisions/decisions-log.md` si se tomó alguna decisión importante.

## Reglas de seguridad

- No registrar contraseñas, tokens, claves API ni secretos.
- No copiar documentos completos si contienen información sensible.
- No subir información confidencial si no es necesario.
- Usar resúmenes y referencias cuando sea suficiente.
- No crear tareas reales en Jira ni páginas reales en Confluence sin confirmación explícita.
