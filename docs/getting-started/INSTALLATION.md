# Installation

DesignForge is a skill repository, not an installable package.

## Codex

Copy the repository into the local skills directory:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R DesignForge "$CODEX_HOME/skills/designforge"
```

Then ask Codex to use the skill by name:

```text
Use DesignForge for this UI redesign.
```

## Other AI Agents

If your tool supports custom instructions or skills:

1. Register `SKILL.md` as the main instruction file.
2. Keep `references/`, `templates/`, and `examples/` attached or discoverable.
3. Tell the agent to inspect relevant reference files before acting on specialized UI tasks.

## Verify

Run:

```bash
python scripts/validate_repository.py
```

Successful validation means the repository structure and documentation links are intact. It does not prove that a downstream AI tool loaded the skill correctly.
