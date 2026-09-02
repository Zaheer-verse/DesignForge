# Contributing

Thanks for helping improve DesignForge. This project is a documentation-first AI skill, so quality depends on clear instructions, realistic examples, and honest validation.

## Development Setup

No package installation is required for the current repository.

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests
```

Use Python 3.9 or newer if possible. The validator uses only the standard library.

## Repository Map

- `SKILL.md`: primary skill behavior and quality gates
- `references/`: detailed guidance used by the skill
- `templates/`: reusable planning and review templates
- `examples/`: realistic skill usage examples
- `docs/`: user and maintainer documentation
- `scripts/`: repository validation tools
- `tests/`: automated checks for the repository validator

## Contribution Guidelines

- Keep claims accurate and verifiable.
- Do not add fake metrics, badges, screenshots, URLs, tests, or affiliations.
- Prefer concise examples with realistic constraints.
- Keep the core skill focused; move deep supporting material into `references/` or `docs/`.
- Update `CHANGELOG.md` for user-facing changes.
- Run the validation commands before opening a pull request.

## Pull Requests

A good pull request explains:

- What changed
- Why it improves the skill or repository
- What validation was run
- Whether docs, examples, or templates changed
- Any known limitations

Small, focused pull requests are easiest to review.

## Issues

When reporting a problem, include:

- The affected file or section
- What is unclear, incorrect, outdated, or missing
- A suggested correction if you have one
- Any relevant AI tool or skill-loading context

## Commit Expectations

Use clear commit messages that describe the user-visible change, such as:

```text
docs: clarify Codex installation path
tests: validate internal markdown links
examples: add dashboard redesign scenario
```
