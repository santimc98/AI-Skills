# Claude Connectors Configuration

Resumen de la configuración observada en Claude para trabajar con Educa Edtech.

## Atlassian Rovo

Conector conectado para Jira y Confluence.

### Herramientas interactivas principales

- Create issue
- Update issue
- Retrieve Confluence page
- Get issue
- Search Confluence with CQL
- Search with JQL
- Transition issue

### Herramientas de lectura principales

- Get current user info
- Fetch content with ARI (beta)
- List accessible resources
- Get comment replies
- List page descendants
- Get page comments
- List page inline comments
- Get spaces
- Get issue link types
- Get remote links
- Get field metadata
- Get issue types
- Get pages in space
- Get transitions
- Get projects
- Lookup users
- Rovo Search Jira and Confluence

### Herramientas de escritura/eliminación principales

Configuradas con aprobación requerida.

- Add comment
- Add or update worklog
- Create Confluence footer comment
- Create Confluence inline comment
- Create Confluence page
- Create issue link
- Update Confluence page

## Microsoft 365

Conector conectado para SharePoint, OneDrive, Outlook y Teams.

### Herramientas disponibles

- chat_message_search
- find_meeting_availability
- outlook_calendar_search
- outlook_email_search
- read_resource
- sharepoint_folder_search
- sharepoint_search

## Regla de seguridad

Cuando una acción pueda modificar Jira, Confluence, SharePoint, Outlook o cualquier sistema corporativo, debe requerir confirmación explícita del usuario antes de ejecutarse.

## Uso por skills

- `skills/educa-edtech-confluence/SKILL.md` debe usarse para documentación en Confluence del espacio OPERACIONES.
- `skills/jira-backlog-management/SKILL.md` debe usarse para issues, backlog y JQL.
- `skills/sharepoint-document-management/SKILL.md` debe usarse para documentos y carpetas de SharePoint.
- `skills/meeting-notes/SKILL.md` puede apoyarse en búsqueda de calendario, correo y mensajes si el usuario pide actas o seguimiento.
