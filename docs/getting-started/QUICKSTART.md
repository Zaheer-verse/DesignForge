# Quickstart

DesignForge is ready when the skill directory contains `SKILL.md`, `references/`, `templates/`, and `examples/`.

## 1. Install

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R DesignForge "$CODEX_HOME/skills/designforge"
```

Use your AI tool's documented skills directory if it does not use `CODEX_HOME`.

## 2. Invoke

```text
Use DesignForge to create a responsive product landing page for a developer tool. Inspect the existing stack first, build within current conventions, and run available validation checks.
```

## 3. Confirm The Agent Follows The Gate

The final response should clearly identify:

- Design and UX decisions
- Files changed
- Checks run
- Checks not run
- Any warnings or limitations

## 4. Validate This Repository

```bash
python scripts/validate_repository.py
```
