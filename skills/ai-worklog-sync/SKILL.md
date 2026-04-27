---
name: ai-worklog-sync
description: "Use this skill whenever Santi wants to synchronize work done across ChatGPT, Claude, LibreChat or other AI assistants. Triggers: 'actualiza el worklog', 'registra la sesión', 'resumen semanal', 'sincroniza con Claude', 'sincroniza con ChatGPT', 'qué hemos hecho esta semana', 'prepara tareas Jira desde el worklog', 'crea seguimiento de actividad', 'pendientes de IA', 'weekly report', 'registro semanal'. This skill defines the shared operational memory for AI-assisted work: session logs, weekly summaries, decisions, pending Jira actions and possible Confluence documentation."
---

# AI Worklog Sync Skill

Esta skill define cómo sincronizar el trabajo realizado con distintos asistentes de IA, especialmente **ChatGPT** y **Claude**, usando el repositorio `AI-Skills` como memoria operativa común.

La idea principal es simple:

```text
ChatGPT / Claude / otros asistentes
        ↓
Worklog semanal en GitHub
        ↓
Revisión semanal
        ↓
Acciones reales a Jira
        ↓
Conocimiento estable a Confluence
```

---

## 1. Objetivo

Mantener un registro compartido, ordenado y reutilizable de:

- Trabajo realizado con asistentes de IA.
- Decisiones tomadas.
- Documentos, Excels, páginas de Confluence o issues de Jira tocados.
- Pendientes abiertos.
- Posibles acciones Jira.
- Posibles páginas Confluence.
- Riesgos, bloqueos y dudas.
- Continuidad entre sesiones de ChatGPT y Claude.

Esta skill evita depender solo de la memoria interna de cada asistente.

---

## 2. Cuándo usar esta skill

Usar esta skill cuando el usuario pida:

- Actualizar el worklog semanal.
- Registrar una sesión de trabajo.
- Sincronizar trabajo entre ChatGPT y Claude.
- Preparar un resumen semanal.
- Identificar tareas que deberían pasar a Jira.
- Identificar documentación que debería pasar a Confluence.
- Revisar lo trabajado durante la semana.
- Preparar actividad semanal para el equipo.
- Crear trazabilidad de tareas hechas con IA.

Ejemplos de frases del usuario:

```text
Actualiza el worklog con lo que hemos hecho hoy.
Registra esta sesión.
Sincroniza esto para que Claude lo pueda leer.
Prepara el resumen semanal de trabajo con IA.
Dime qué tareas Jira salen de esta semana.
Lee el worklog y continúa desde ahí.
```

---

## 3. Estructura del worklog

La estructura oficial del repositorio para sincronización es:

```text
worklog/
├── README.md
├── current-week.md
├── weekly/
│   └── YYYY-Www.md
├── sessions/
│   └── YYYY-MM-DD--assistant--short-topic.md
├── tasks/
│   ├── pending-jira-actions.md
│   └── pending-confluence-pages.md
└── decisions/
    └── decisions-log.md
```

### Archivos principales

| Archivo | Uso |
|---|---|
| `worklog/README.md` | Explica cómo funciona el sistema |
| `worklog/current-week.md` | Archivo puente que indica cuál es la semana activa |
| `worklog/weekly/YYYY-Www.md` | Resumen semanal acumulado |
| `worklog/sessions/YYYY-MM-DD--assistant--topic.md` | Registro detallado de una sesión concreta |
| `worklog/tasks/pending-jira-actions.md` | Acciones candidatas a Jira, no creadas aún |
| `worklog/tasks/pending-confluence-pages.md` | Páginas candidatas a Confluence, no creadas aún |
| `worklog/decisions/decisions-log.md` | Registro acumulado de decisiones importantes |

---

## 4. Regla al iniciar una sesión

Al inicio de una sesión importante, el asistente debe:

1. Leer `index.md` del repo `AI-Skills`.
2. Leer esta skill: `skills/ai-worklog-sync/SKILL.md`.
3. Leer `worklog/current-week.md`.
4. Leer el archivo semanal activo en `worklog/weekly/`.
5. Leer `worklog/tasks/pending-jira-actions.md` si se va a trabajar con Jira.
6. Leer `worklog/tasks/pending-confluence-pages.md` si se va a trabajar con documentación.
7. Continuar desde el estado actual sin repetir trabajo ya registrado.

Prompt recomendado:

```text
Lee mi repo AI-Skills. Usa index.md para elegir skills.
Después lee worklog/current-week.md, el worklog semanal activo y los pendientes.
Continúa el trabajo teniendo en cuenta lo ya realizado.
```

---

## 5. Regla al cerrar una sesión

Al final de una sesión importante, el asistente debe proponer o ejecutar, si tiene permiso, una actualización de:

1. Registro de sesión en `worklog/sessions/`.
2. Resumen semanal en `worklog/weekly/YYYY-Www.md`.
3. Decisiones importantes en `worklog/decisions/decisions-log.md`.
4. Acciones candidatas a Jira en `worklog/tasks/pending-jira-actions.md`.
5. Páginas candidatas a Confluence en `worklog/tasks/pending-confluence-pages.md`.

Prompt recomendado:

```text
Actualiza el worklog semanal con:
1. Trabajo realizado.
2. Decisiones tomadas.
3. Archivos, páginas o issues tocados.
4. Pendientes.
5. Posibles acciones Jira.
6. Posibles páginas Confluence.
No crees tareas reales todavía; solo déjalas propuestas.
```

---

## 6. Qué registrar y qué no registrar

### Registrar

- Tareas significativas realizadas con IA.
- Cambios en GitHub, Confluence o Jira.
- Decisiones de arquitectura, proceso o metodología.
- Análisis de Excel o documentos empresariales.
- Recomendaciones aceptadas.
- Pendientes que puedan convertirse en tareas.
- Bloqueos o dudas relevantes.
- Enlaces a páginas, issues o archivos tocados.

### No registrar

- Conversaciones triviales.
- Pruebas sin impacto.
- Datos sensibles innecesarios.
- Credenciales, tokens, claves API o secretos.
- Información personal no necesaria.
- Copias completas de documentos confidenciales si basta con un resumen.

---

## 7. Formato de registro de sesión

Cada sesión debe registrarse con este formato:

```markdown
# Session Log — YYYY-MM-DD — [Assistant] — [Tema breve]

## Metadata

| Campo | Valor |
|---|---|
| Fecha | YYYY-MM-DD |
| Asistente | ChatGPT / Claude / Otro |
| Usuario | Santi |
| Contexto | Educa Edtech / Operaciones / Otro |
| Skills usadas | `skill-1`, `skill-2` |
| Sistemas tocados | GitHub / Jira / Confluence / SharePoint / Excel / Otro |

## Objetivo de la sesión

[Qué se quería conseguir.]

## Trabajo realizado

- 

## Decisiones tomadas

- 

## Archivos / páginas / issues tocados

| Tipo | Referencia | Acción |
|---|---|---|
| GitHub | `ruta/archivo.md` | Creado / Actualizado / Revisado |
| Jira | `AA-XXX` | Leído / Propuesto / Actualizado |
| Confluence | `[Título]` | Leído / Creado / Actualizado |

## Pendientes

- 

## Posibles acciones Jira

| Acción | Tipo sugerido | Epic sugerida | Prioridad | Estado |
|---|---|---|---|---|
|  |  |  |  | Propuesta |

## Posibles páginas Confluence

| Página | Ubicación sugerida | Motivo | Estado |
|---|---|---|---|
|  |  |  | Propuesta |

## Riesgos o bloqueos

- 

## Próximo prompt recomendado

```text
[Prompt para continuar el trabajo en otro asistente]
```
```

---

## 8. Formato de resumen semanal

Cada semana debe tener un archivo:

```text
worklog/weekly/YYYY-Www.md
```

Formato:

```markdown
# AI Worklog — YYYY-Www

## Resumen ejecutivo

[Resumen breve de la semana.]

## Trabajo realizado

| Fecha | Asistente | Tema | Resultado |
|---|---|---|---|
| YYYY-MM-DD | ChatGPT / Claude |  |  |

## Decisiones tomadas

| Fecha | Decisión | Motivo | Impacto |
|---|---|---|---|
|  |  |  |  |

## Sistemas tocados

| Sistema | Elemento | Acción |
|---|---|---|
| GitHub |  |  |
| Jira |  |  |
| Confluence |  |  |
| SharePoint |  |  |

## Pendientes abiertos

- 

## Candidatas a Jira

| Acción | Tipo sugerido | Epic sugerida | Prioridad | Estado |
|---|---|---|---|---|
|  |  |  |  | Propuesta |

## Candidatas a Confluence

| Página | Ubicación sugerida | Motivo | Estado |
|---|---|---|---|
|  |  |  | Propuesta |

## Riesgos / bloqueos

- 

## Próximos pasos recomendados

1. 
2. 
3. 
```

---

## 9. Criterios para pasar algo a Jira

Solo convertir a Jira si cumple alguna de estas condiciones:

- Requiere acción de una persona del equipo.
- Tiene entregable claro.
- Tiene fecha, prioridad o dependencia.
- Afecta a una iniciativa existente.
- Requiere seguimiento en el backlog.
- Debe aparecer en KPIs o reporting del equipo.

No convertir a Jira:

- Ideas vagas.
- Notas personales.
- Exploraciones sin decisión.
- Prompts experimentales sin impacto.

Cuando una acción sea candidata a Jira, registrarla primero en:

```text
worklog/tasks/pending-jira-actions.md
```

Y aplicar después:

```text
skills/educa-edtech-jira/SKILL.md
```

---

## 10. Criterios para pasar algo a Confluence

Convertir a Confluence si:

- Es conocimiento estable del equipo.
- Define un proceso, guía, plantilla o procedimiento.
- Sirve para onboarding.
- Evita repetir explicaciones.
- Formaliza una decisión o forma de trabajar.
- Debe quedar disponible para varias personas.

No convertir a Confluence:

- Borradores muy inmaduros.
- Notas personales temporales.
- Información sensible sin validación.
- Conversaciones exploratorias sin conclusión.

Cuando una página sea candidata, registrarla primero en:

```text
worklog/tasks/pending-confluence-pages.md
```

Y aplicar después:

```text
skills/educa-edtech-confluence/SKILL.md
```

---

## 11. Relación con otras skills

| Caso | Skill complementaria |
|---|---|
| Documentación de Educa Edtech en Confluence | `skills/educa-edtech-confluence/SKILL.md` |
| Gestión de Jira OPERATIONS | `skills/educa-edtech-jira/SKILL.md` |
| Presentaciones corporativas | `skills/educa-edtech-pptx/SKILL.md` |
| Análisis Excel | `skills/excel-analysis/SKILL.md` |
| Reuniones y actas | `skills/meeting-notes/SKILL.md` |
| Informes ejecutivos | `skills/executive-reporting/SKILL.md` |

---

## 12. Reglas de seguridad

- No registrar secretos, tokens, contraseñas ni claves API.
- No copiar documentos completos si contienen información sensible.
- No subir datos personales innecesarios.
- No crear tareas reales en Jira sin confirmación explícita.
- No crear o actualizar páginas reales de Confluence sin confirmación explícita.
- Si el repositorio es público, evitar información confidencial; usar resúmenes y referencias, no contenido sensible.
- Si hay duda, registrar como `pendiente de revisión`.

---

## 13. Convención de nombres

### Sesiones

```text
worklog/sessions/YYYY-MM-DD--assistant--short-topic.md
```

Ejemplos:

```text
worklog/sessions/2026-04-27--chatgpt--skills-jira-confluence.md
worklog/sessions/2026-04-28--claude--excel-cost-analysis.md
```

### Semanas

```text
worklog/weekly/YYYY-Www.md
```

Ejemplo:

```text
worklog/weekly/2026-W18.md
```

### Decisiones

Usar siempre:

```text
worklog/decisions/decisions-log.md
```

---

## 14. Plantilla de cierre rápido

Cuando el usuario pida cerrar una sesión, responder o registrar:

```markdown
## Cierre de sesión

### Trabajo realizado
- 

### Decisiones
- 

### Pendientes
- 

### Candidatas a Jira
- 

### Candidatas a Confluence
- 

### Próximo paso recomendado
- 
```

---

## 15. Regla final

El worklog no sustituye a Jira ni a Confluence:

```text
Worklog = memoria operativa entre asistentes.
Jira = tareas oficiales del equipo.
Confluence = conocimiento estable del equipo.
SharePoint = archivos fuente y documentación de trabajo.
```

El objetivo es que cualquier asistente pueda saber qué se ha trabajado, qué falta y qué debe formalizarse sin depender de una conversación concreta.
