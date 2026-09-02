# Usage Guide

DesignForge works best when the request includes product context and clear constraints.

## Strong Prompt Shape

```text
Use DesignForge to [create/redesign/review] [page or feature].
Audience: [who this is for].
Goal: [what users need to accomplish].
Constraints: [framework, libraries, brand, timeline, assets].
Validation: [build, lint, test, responsive, accessibility, screenshots].
```

## Simple Example

```text
Use DesignForge to create a mobile-first landing page for a small invoicing app. Keep it calm, trustworthy, and fast. Use semantic HTML and validate responsive behavior.
```

## Advanced Example

```text
Use DesignForge to redesign the analytics dashboard. Preserve the existing Next.js routes and Tailwind setup. Improve density, scanning, empty states, focus states, and chart accessibility. Run the existing lint, test, and build commands and report anything not run.
```

## Expected Output

A good DesignForge-guided agent should provide:

- A brief discovery summary
- Implementation aligned with the existing stack
- Responsive and accessibility considerations
- Validation commands and results
- Honest warnings for checks that could not be run

## Anti-Patterns

Avoid asking for vague spectacle:

```text
Make it look amazing with lots of animations.
```

Prefer clear intent:

```text
Make the onboarding page feel premium and calm. Use motion only for orientation and feedback, support reduced motion, and prioritize completion of the first setup step.
```
