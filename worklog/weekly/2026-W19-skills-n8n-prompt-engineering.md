# Worklog — Skills n8n y Prompt Engineering

Fecha: 2026-05-14

## Objetivo

Mejorar el repositorio `AI-Skills` con referencias reutilizables para:

1. uso de IA/Claude/ChatGPT con n8n;
2. comparación de MCPs de n8n;
3. creación de system prompts y user prompts para agentes;
4. plantillas específicas para nodos AI Agent de n8n.

## Cambios realizados

### Prompt Engineering

Se amplió:

```text
skills/prompt-engineering/SKILL.md
```

Con:

- separación clara entre system prompt y user prompt;
- patrón para agentes con herramientas;
- patrón para n8n AI Agent;
- checklist de auditoría de prompts;
- formato de salida para crear o auditar prompts;
- referencias externas a revisar antes de reutilizar.

Se añadieron referencias:

```text
skills/prompt-engineering/references/README.md
skills/prompt-engineering/references/system-vs-user-prompt.md
skills/prompt-engineering/references/agent-prompt-template.md
skills/prompt-engineering/references/n8n-ai-agent-prompt-template.md
```

### n8n Workflow Engineering

Se añadieron referencias complementarias:

```text
skills/n8n-workflow-engineering/references/README.md
skills/n8n-workflow-engineering/references/external-n8n-skill-sources.md
skills/n8n-workflow-engineering/references/n8n-mcp-usage-and-comparison.md
```

## Fuentes externas registradas para revisión

```text
https://github.com/czlonkowski/n8n-skills
https://github.com/czlonkowski/n8n-mcp
https://github.com/haunchen/n8n-skills
https://github.com/RedcoatAsher/n8n-skills-redux
https://github.com/splinesreticulating/n8n-v2-workflow-skill
https://github.com/enescingoz/awesome-n8n-templates
https://github.com/ckelsoe/prompt-architect
https://github.com/NeoLabHQ/context-engineering-kit
https://github.com/nidhinjs/prompt-master
```

## Decisión tomada

No se copió una skill externa completa. Se reforzó la skill interna existente con referencias propias, plantillas y criterios de seguridad, manteniendo el repositorio como fuente operativa principal.

## Uso recomendado

- Para crear o auditar workflows n8n: `skills/n8n-workflow-engineering/SKILL.md`.
- Para comparar MCPs de n8n: `skills/n8n-workflow-engineering/references/n8n-mcp-usage-and-comparison.md`.
- Para crear system/user prompts de agentes: `skills/prompt-engineering/SKILL.md`.
- Para prompts de n8n AI Agent: `skills/prompt-engineering/references/n8n-ai-agent-prompt-template.md`.

## Pendiente recomendado

Pedir a Claude Code que compare el MCP público `czlonkowski/n8n-mcp` con el MCP interno de Operaciones usando el prompt incluido en:

```text
skills/n8n-workflow-engineering/references/n8n-mcp-usage-and-comparison.md
```
