# Validation Strategy

DesignForge has two validation layers.

## Repository Validation

The repository validator checks the skill corpus itself:

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests
```

It verifies:

- Required project files exist
- `SKILL.md` has expected frontmatter
- Markdown links resolve
- Placeholder repository URLs are absent
- Secret-like files and high-risk secret patterns are absent
- README examples reference files that exist

## Skill Behavior Validation

AI skill behavior is partly qualitative. Use review scenarios instead of pretending that deterministic unit tests can prove visual design quality.

Recommended scenarios:

- Normal landing page creation
- Dashboard redesign with existing code constraints
- Malformed or incomplete product brief
- Conflicting visual and accessibility requirements
- Long content and localization expansion
- 3D request on a performance-sensitive page
- Accessibility bug fix
- Production readiness review

For each scenario, check whether the agent:

- Inspects the existing project before editing
- Explains design decisions in context
- Avoids fake claims and fake assets
- Preserves accessibility and responsive behavior
- Runs available project checks
- Marks unavailable checks as `NOT RUN`
