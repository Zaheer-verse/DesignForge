# Architecture

DesignForge is organized as a skill corpus.

```mermaid
flowchart TD
    A[SKILL.md] --> B[Core behavior and QA gates]
    A --> C[references]
    A --> D[templates]
    A --> E[examples]
    C --> F[Design, layout, accessibility, responsive, motion, 3D]
    D --> G[Page specs and design reviews]
    E --> H[Representative usage scenarios]
    I[scripts/validate_repository.py] --> A
    I --> C
    I --> D
    I --> E
```

## Core File

`SKILL.md` defines the role, workflow, anti-patterns, validation gate, and final quality classification.

## Supporting References

The `references/` directory gives deeper guidance for specialized areas. These files are intentionally separate so the main skill stays readable.

## Templates

Templates support repeatable planning and QA:

- `templates/page-spec.md`
- `templates/design-review.md`

## Examples

Examples show realistic prompts and design breakdowns. They should stay honest: do not imply a UI was built or tested unless that happened.

## Validation

The local validator checks repository integrity. It is designed to run in CI without external dependencies.
