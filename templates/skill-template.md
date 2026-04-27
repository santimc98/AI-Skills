# Plantilla de Skill

Usa esta plantilla cuando crees una nueva skill para el repositorio `AI-Skills`.

```markdown
---
name: nombre-skill
description: Describe qué hace la skill y cuándo debe usarse. Incluye palabras clave, contextos y situaciones que deberían activarla.
---

# Nombre de la skill

## Cuándo usar esta skill

Usar esta skill cuando...

No usar esta skill cuando...

## Objetivo

El objetivo de esta skill es...

## Entradas necesarias

Antes de ejecutar la skill, recopilar:

1. ...
2. ...
3. ...

Si falta información crítica, preguntar al usuario.
Si falta información no crítica, avanzar con supuestos explícitos.

## Procedimiento paso a paso

### 1. Preparación

...

### 2. Ejecución

...

### 3. Validación

...

### 4. Entrega

...

## Criterios de calidad

La respuesta final debe cumplir:

- ...
- ...
- ...

## Formato de salida esperado

Entregar el resultado con esta estructura:

```text
...
```

## Errores comunes a evitar

- ...
- ...
- ...

## Plantillas relacionadas

- `templates/...`

## Conocimiento relacionado

- `knowledge/...`
```

## Checklist rápido

Antes de guardar la skill, comprobar:

- [ ] Tiene frontmatter con `name` y `description`.
- [ ] La descripción indica cuándo se debe activar.
- [ ] El objetivo es concreto.
- [ ] Las entradas necesarias están claras.
- [ ] El procedimiento es accionable.
- [ ] El formato de salida está definido.
- [ ] Los criterios de calidad son verificables.
- [ ] Incluye errores comunes.
- [ ] Indica plantillas y knowledge relacionados si existen.
- [ ] No duplica una skill existente.
