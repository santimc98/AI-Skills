# Session Log — Agente SIM Ponencia IA — Ficha Confluence

**Fecha:** 2026-05-11  
**Semana:** 2026-W19  
**Área:** Operaciones / Business Operations & AI  
**Sistema principal:** Confluence OPERACIONES (`AA1`)  
**Página:** `Agente SIM Ponencia IA`  
**URL:** https://educaedtech.atlassian.net/wiki/spaces/AA1/pages/1865842713/Agente+SIM+Ponencia+IA

## Resumen ejecutivo

Se creó la primera ficha documental del **Agente SIM Ponencia IA** en Confluence, siguiendo la plantilla oficial de **Agente IA** del espacio OPERACIONES. La página estaba vacía y se actualizó como ficha v1.0 en estado **borrador / en diseño**, dejando visibles los campos pendientes para completar cuando se confirme el contexto funcional y técnico definitivo.

La ficha documenta el agente como un caso operativo de arquitectura RAG basada en **GitLab Knowledge → n8n → Supabase pgvector → cliente autorizado / LibreChat**, con foco en la ponencia de IA. Se registraron alcance, limitaciones, knowledge, conectores, seguridad, evaluación, mantenimiento, tareas Jira relacionadas y pendientes abiertos.

## Trabajo realizado

| Elemento | Resultado |
|---|---|
| Página Confluence revisada | `Agente SIM Ponencia IA`, ID `1865842713`, estaba vacía antes de la actualización. |
| Skill aplicada | `skills/educa-edtech-confluence/SKILL.md` del repo `santimc98/AI-Skills`. |
| Plantilla consultada | `Plantilla Agente IA`, página ID `1813905409`. |
| Contexto usado | Worklog semanal `worklog/weekly/2026-W19.md`, especialmente avances sobre GitLab Knowledge, n8n, Supabase y agente de ponencia. |
| Acción ejecutada | Actualización completa de la página Confluence con ficha documental v1.0. |
| Versión Confluence resultante | Versión 2. |
| Mensaje de versión | `Creación inicial de ficha documental del Agente SIM Ponencia IA`. |

## Contenido documentado en la ficha

La página se estructuró con estas secciones:

1. Metadatos del agente.
2. Descripción general.
3. Ficha de identificación del agente.
4. Alcance y limitaciones.
5. Modelo y configuración técnica.
6. Knowledge / base de conocimiento.
7. Herramientas y conectores.
8. System prompt y personalidad.
9. Flujo de interacción.
10. Sistemas integrados.
11. Seguridad, permisos y gobernanza.
12. Métricas y KPIs.
13. Evaluación y pruebas de calidad.
14. Mantenimiento y responsabilidades.
15. Proceso y automatización vinculada.
16. Estado actual y pendientes.
17. Histórico de cambios.

## Hechos documentados

- El agente se documenta como **Agente SIM Ponencia IA**.
- Se clasifica como agente operativo relacionado con IA y ponencia.
- La arquitectura prevista usa knowledge versionado en GitLab y recuperación RAG.
- El flujo técnico previsto es **GitLab Knowledge → n8n → Supabase pgvector → agente/cliente autorizado**.
- Supabase está preparado con pgvector y tabla/función de búsqueda para conocimiento vectorial.
- El workflow n8n de ingesta está planteado para listar, leer, normalizar, chunkear, hashear, deduplicar, generar embeddings y hacer upsert.
- Se mantiene como pendiente la prueba end-to-end y la validación de recuperación RAG.

## Campos dejados como pendientes

Se dejaron explícitamente como pendientes para evitar inventar información:

- Comisión exacta.
- Owner funcional.
- Owner técnico nominal.
- Modelo LLM final.
- Modelo de embeddings definitivo.
- Configuración final de temperatura, tokens y contexto.
- Usuarios autorizados.
- Identidad bajo la que actúa el agente.
- Ruta exacta final de system prompt si se confirma.
- Diagrama de flujo final.
- Banco de preguntas de evaluación RAG.
- Costes estimados.
- Enlaces definitivos a workflow n8n, tabla Supabase y recursos técnicos.

## Decisiones de documentación

| Decisión | Motivo |
|---|---|
| Crear ficha v1.0 como borrador / en diseño | La página estaba vacía y ya había suficiente contexto técnico para documentar el estado actual sin declarar producción. |
| Marcar campos pendientes en vez de inventar datos | Mantener trazabilidad y evitar información falsa en Confluence. |
| Documentar GitLab Knowledge, n8n y Supabase como arquitectura prevista/preparada | Es el estado real recogido en el worklog semanal. |
| No marcar el agente como productivo | Falta prueba end-to-end y validación funcional. |
| Relacionar la ficha con AA-358 | AA-358 figura como tarea principal de Prompt y Base de conocimiento Agente Ponencia. |

## Jira relacionada

| Issue | Relación |
|---|---|
| AA-358 | Tarea principal asociada a Prompt y Base de conocimiento Agente Ponencia. |
| AA-312 | Infraestructura general de MCPs/agentes. |
| AA-375 | Build/deploy Docker para MCPs en entorno corporativo. |
| AA-376 | Despliegue GitLab Knowledge MCP en Coolify. |
| AA-377 | Despliegue n8n Operations MCP en Coolify. |
| AA-378 | Validación de consumo MCP desde cliente autorizado. |
| AA-379 | Decisión técnica MCP propio vs conector oficial. |

## Pendientes derivados

- Completar la ficha cuando se confirmen owner funcional, owner técnico nominal, usuarios destinatarios y plataforma final de consumo.
- Añadir enlaces definitivos a repo GitLab, workflow n8n, tabla Supabase y función de búsqueda cuando estén estabilizados.
- Ejecutar prueba end-to-end GitLab → n8n → Supabase.
- Crear banco de 15-20 preguntas reales para validar recuperación RAG.
- Actualizar la página a v1.1 tras cerrar los datos pendientes.
- Valorar vincular formalmente la página de Confluence a AA-358 si no queda enlazada automáticamente.

## Riesgos / notas

- No debe tratarse como agente en producción hasta completar credenciales, prueba end-to-end y evaluación funcional.
- No debe indexarse `raw-research` completo sin curación, para evitar contaminación de respuestas.
- No deben registrarse secretos, service role keys ni API keys en Confluence, Jira, GitHub o exports de workflow.
- Cualquier cambio de knowledge estable debe pasar por revisión humana antes de indexarse.

## Resultado final

Página Confluence actualizada correctamente:

```text
Agente SIM Ponencia IA
https://educaedtech.atlassian.net/wiki/spaces/AA1/pages/1865842713/Agente+SIM+Ponencia+IA
Versión Confluence: 2
Estado documental: v1.0 borrador / en diseño
```
