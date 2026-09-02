# Skill Reference

## Purpose

DesignForge guides AI coding agents through professional web UI/UX design engineering. It is intended for creating, redesigning, reviewing, and production-checking web interfaces.

## Activation

Use the skill by name in a request:

```text
Use DesignForge to improve this checkout flow.
```

An AI tool may also invoke it automatically for frontend design tasks if it supports skill routing.

## Expected Context

DesignForge works best with:

- Product or page goal
- Target audience
- Existing codebase or framework
- Brand or visual constraints
- Assets, copy, or content hierarchy
- Required validation checks

## Inputs

Common inputs include:

- Natural-language UI requests
- Existing frontend code
- Screenshots or design references
- Accessibility or responsive defects
- Product requirements
- Page specifications

## Outputs

Depending on the request, the agent may produce:

- Implemented frontend changes
- Design system decisions
- Page specs
- Design reviews
- QA reports
- Troubleshooting recommendations

## Operating Principles

- Inspect before changing.
- Use the existing stack and project conventions.
- Make design choices for a reason.
- Treat accessibility, performance, and security as release criteria.
- Report validation honestly.
- Avoid generic AI visual patterns.

## Failure Handling

The skill should classify final status as:

- `PASS`
- `PASS WITH WARNINGS`
- `NEEDS FIXES`
- `BLOCKED`

If a check cannot be run, the agent should say `NOT RUN` and explain why.

## Best Practices

- Provide audience and product context.
- Ask for specific validation.
- Use examples and templates for repeatable work.
- Keep visual ambition proportional to the product and timeline.

## Anti-Patterns

- Installing libraries without checking the project first
- Claiming screenshots, tests, or audits that were not performed
- Using inaccessible custom controls
- Adding motion without reduced-motion support
- Creating fake metrics, badges, screenshots, or affiliations
