# External n8n skill sources

## Objetivo

Mantener una lista curada de recursos externos útiles para mejorar la skill interna de n8n sin copiar contenido a ciegas.

## Recursos principales

### czlonkowski/n8n-skills

```text
https://github.com/czlonkowski/n8n-skills
```

Uso recomendado:

- inspiración para dividir la capacidad n8n en subskills;
- expresiones n8n;
- configuración de nodos;
- validación de workflows;
- patrones de construcción con Claude Code;
- uso conjunto con `n8n-mcp`.

### czlonkowski/n8n-mcp

```text
https://github.com/czlonkowski/n8n-mcp
```

Uso recomendado:

- referencia de MCP público maduro para n8n;
- comparación con MCP interno de Operaciones;
- consulta de nodos, plantillas y validaciones;
- inspiración para herramientas read-only o de validación.

### haunchen/n8n-skills

```text
https://github.com/haunchen/n8n-skills
```

Uso recomendado:

- documentación y análisis de estructura;
- búsqueda de nodos;
- validación de workflows;
- apoyo para catálogo de nodos.

### n8n-skills-redux

```text
https://github.com/RedcoatAsher/n8n-skills-redux
```

Uso recomendado:

- hardening;
- evitar sobreingeniería;
- patrones para producción;
- control de errores comunes.

### n8n-v2-workflow-skill

```text
https://github.com/splinesreticulating/n8n-v2-workflow-skill
```

Uso recomendado:

- revisar cambios de n8n 2.0;
- validar compatibilidad futura;
- aprender patrones actualizados.

### awesome-n8n-templates

```text
https://github.com/enescingoz/awesome-n8n-templates
```

Uso recomendado:

- ejemplos reales de workflows;
- patrones de automatización;
- inspiración para arquitecturas;
- no usar como producción sin auditoría.

## Reglas antes de reutilizar

1. Revisar licencia.
2. Revisar código y scripts.
3. Revisar si hay instrucciones peligrosas para agentes.
4. No instalar en entorno corporativo sin auditoría.
5. No copiar secretos, ejemplos inseguros ni comandos destructivos.
6. Adaptar siempre a la política interna: test first, no credenciales reales, redacción de secretos y mínimos privilegios.
7. Citar la fuente en documentación interna si se reutiliza una idea concreta.

## Cómo usarlos en nuestro repo

- Mantener nuestra skill como fuente principal.
- Añadir referencias internas resumidas y auditadas.
- No depender de repos externos durante la ejecución normal de un agente.
- Usar repos externos como benchmark de calidad y comparación funcional.
