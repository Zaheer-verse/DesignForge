# Troubleshooting

## The Skill Does Not Load

Check that:

- The directory name is discoverable by your AI tool.
- `SKILL.md` is at the skill root.
- The frontmatter contains `name: designforge`.
- Supporting folders were copied with the skill.

## The Agent Produces Generic UI

Add more context:

- Audience
- Product category
- Desired maturity level
- Existing brand constraints
- Content hierarchy
- Examples of what to avoid

Ask the agent to run the DesignForge discovery phase before implementation.

## The Agent Wants To Install New Libraries

DesignForge should inspect the existing stack first. Ask the agent to justify any new dependency and prefer existing project tools when practical.

## Accessibility Is Weak

Require explicit checks for:

- Semantic HTML
- Keyboard navigation
- Visible focus states
- Contrast
- Form labels
- Reduced motion

Use `references/accessibility.md` as the review source.

## Validation Script Fails

Read the reported file and message. Common causes:

- A Markdown link points to a missing file
- README mentions an example that does not exist
- Placeholder URLs were added
- A secret-like file was committed
- `SKILL.md` frontmatter was changed incorrectly
