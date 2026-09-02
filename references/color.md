# Color System

A professional color system creates consistency, enables accessibility, and expresses brand personality.

---

## Color System Architecture

### Semantic Tokens

Never use arbitrary hex values directly. Use semantic tokens:

```css
:root {
  /* Core */
  --color-primary: #3B82F6;
  --color-secondary: #64748B;
  --color-accent: #F59E0B;

  /* Background */
  --color-bg: #FFFFFF;
  --color-bg-muted: #F8FAFC;
  --color-bg-subtle: #F1F5F9;

  /* Surface */
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-surface-overlay: rgba(255, 255, 255, 0.95);

  /* Border */
  --color-border: #E2E8F0;
  --color-border-muted: #F1F5F9;
  --color-border-strong: #CBD5E1;

  /* Text */
  --color-text: #0F172A;
  --color-text-muted: #64748B;
  --color-text-subtle: #94A3B8;

  /* Semantic */
  --color-success: #22C55E;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  --color-info: #3B82F6;
}
```

### Dark Mode

```css
:root.dark {
  --color-bg: #0F172A;
  --color-bg-muted: #1E293B;
  --color-bg-subtle: #334155;

  --color-surface: #1E293B;
  --color-surface-elevated: #334155;
  --color-surface-overlay: rgba(15, 23, 42, 0.95);

  --color-border: #334155;
  --color-border-muted: #1E293B;
  --color-border-strong: #475569;

  --color-text: #F8FAFC;
  --color-text-muted: #94A3B8;
  --color-text-subtle: #64748B;
}
```

---

## Color Palette Construction

### Step 1: Choose Base Hue

Select primary brand color based on:

**Blue** — Trust, technology, calm
**Green** — Growth, nature, success
**Purple** — Creativity, luxury, mystery
**Orange** — Energy, enthusiasm, action
**Red** — Urgency, passion, importance
**Teal** — Balance, innovation, clarity

### Step 2: Generate Scale

Create 9 shades for flexibility:

```css
:root {
  /* Blue scale example */
  --blue-50: #EFF6FF;
  --blue-100: #DBEAFE;
  --blue-200: #BFDBFE;
  --blue-300: #93C5FD;
  --blue-400: #60A5FA;
  --blue-500: #3B82F6; /* Base */
  --blue-600: #2563EB;
  --blue-700: #1D4ED8;
  --blue-800: #1E40AF;
  --blue-900: #1E3A8A;
  --blue-950: #172554;
}
```

**Usage:**
- 50-100: Backgrounds, highlights
- 200-300: Borders, subtle accents
- 400-500: Interactive elements (hover, active)
- 600-700: Primary buttons, links
- 800-950: Text on light backgrounds

---

## Contrast and Accessibility

### WCAG Requirements

**Normal Text (< 18px or < 14px bold)**
- Minimum: 4.5:1
- Enhanced (AAA): 7:1

**Large Text (≥ 18px or ≥ 14px bold)**
- Minimum: 3:1
- Enhanced (AAA): 4.5:1

**UI Components and Graphics**
- Minimum: 3:1

### Testing Colors

```javascript
// Calculate relative luminance
function getLuminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

// Calculate contrast ratio
function getContrast(color1, color2) {
  const l1 = getLuminance(...color1);
  const l2 = getLuminance(...color2);
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}
```

### Automatic Contrast in CSS

```css
/* Ensure readable text on colored backgrounds */
.button-primary {
  background: var(--color-primary-600);
  color: white; /* Will pass contrast on 600+ */
}

.button-secondary {
  background: var(--color-primary-100);
  color: var(--color-primary-900); /* Dark text on light bg */
}
```

---

## Gradients

### Purpose-Driven Gradients

Gradients must have a reason:

**Brand Expression**
```css
.hero {
  background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
}
```

**Depth and Atmosphere**
```css
.card {
  background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.05) 100%);
}
```

**Focus and Attention**
```css
.cta-button {
  background: linear-gradient(90deg, #F59E0B 0%, #EF4444 100%);
}
```

**Lighting Effect**
```css
.glow {
  background: radial-gradient(circle at 50% 0%, rgba(255,255,255,0.15) 0%, transparent 50%);
}
```

### Avoid

❌ Random gradients on every section
❌ Purple/blue gradients everywhere (AI default)
❌ Heavy gradients that reduce text readability
❌ Generic 45° angle without reason

---

## Accent Colors

### Usage

Accent colors should be **intentional and sparse**:

```css
/* Good: Accent draws attention */
.price {
  color: var(--color-accent);
}

.cta-button {
  background: var(--color-accent);
}

.notification-badge {
  background: var(--color-accent);
}

/* Bad: Accent overused */
h1, h2, h3, a, li, span {
  color: var(--color-accent); /* Too much! */
}
```

### Secondary Accent

For products needing two brand colors:

```css
:root {
  --color-primary: #3B82F6; /* Trust, calm */
  --color-accent: #F59E0B; /* Energy, action */
}

/* Use strategically */
.cta-primary {
  background: var(--color-primary);
}

.cta-secondary {
  background: var(--color-accent);
}
```

---

## Semantic Colors

### Consistent Meaning

```css
:root {
  /* Success - Green */
  --color-success: #22C55E;
  --color-success-bg: #DCFCE7;
  --color-success-border: #BBF7D0;

  /* Warning - Amber */
  --color-warning: #F59E0B;
  --color-warning-bg: #FEF3C7;
  --color-warning-border: #FDE68A;

  /* Error - Red */
  --color-error: #EF4444;
  --color-error-bg: #FEE2E2;
  --color-error-border: #FECACA;

  /* Info - Blue */
  --color-info: #3B82F6;
  --color-info-bg: #DBEAFE;
  --color-info-border: #BFDBFE;
}
```

### Usage Patterns

```html
<!-- Success state -->
<div class="alert alert-success">
  <span class="alert-icon">✓</span>
  <span class="alert-message">Changes saved successfully</span>
</div>

<!-- Error state -->
<div class="alert alert-error">
  <span class="alert-icon">✕</span>
  <span class="alert-message">Failed to save changes</span>
</div>
```

---

## Dark Mode Design

### Principles

1. **Don't just invert** — Dark mode requires its own palette
2. **Reduce contrast** — Pure white on pure black causes eye strain
3. **Elevate surfaces** — Use lighter grays for elevated elements
4. **Desaturate colors** — Colors appear more vibrant on dark backgrounds

### Implementation

```css
:root {
  --color-bg: #FFFFFF;
  --color-surface: #F8FAFC;
  --color-text: #0F172A;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0F172A;
    --color-surface: #1E293B;
    --color-text: #E2E8F0;
  }
}

/* Manual toggle */
:root.dark {
  --color-bg: #0F172A;
  --color-surface: #1E293B;
  --color-text: #E2E8F0;
}
```

### Color Adjustments for Dark Mode

```css
/* Light mode */
--color-primary: #3B82F6;

/* Dark mode - slightly lighter, less saturated */
--color-primary: #60A5FA;
```

---

## Color Palette Examples

### Tech SaaS (Blue)

```css
:root {
  --color-primary: #2563EB;
  --color-accent: #0EA5E9;
  --color-bg: #FFFFFF;
  --color-text: #0F172A;
}
```

### Fintech (Green)

```css
:root {
  --color-primary: #059669;
  --color-accent: #10B981;
  --color-bg: #FFFFFF;
  --color-text: #064E3B;
}
```

### Creative Agency (Purple)

```css
:root {
  --color-primary: #7C3AED;
  --color-accent: #EC4899;
  --color-bg: #FAFAFA;
  --color-text: #1F2937;
}
```

### Developer Tool (Dark)

```css
:root {
  --color-primary: #818CF8;
  --color-accent: #34D399;
  --color-bg: #0F172A;
  --color-text: #E2E8F0;
}
```

---

## Common Mistakes

❌ **Too many colors**
- Limit to 1-2 brand colors + semantic colors
- Restraint creates sophistication

❌ **Poor contrast**
- Always test with contrast checker
- Don't sacrifice readability for aesthetics

❌ **Arbitrary hex values**
- Use design tokens
- Enables consistency and theming

❌ **Gradients everywhere**
- Gradients need purpose
- Reserve for key moments

❌ **Ignoring dark mode**
- Design dark palette intentionally
- Don't just invert

---

## Quick Reference

```css
:root {
  /* Brand */
  --color-primary: #3B82F6;
  --color-secondary: #64748B;
  --color-accent: #F59E0B;

  /* Background */
  --color-bg: #FFFFFF;
  --color-bg-muted: #F8FAFC;
  --color-bg-subtle: #F1F5F9;

  /* Surface */
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;

  /* Border */
  --color-border: #E2E8F0;
  --color-border-strong: #CBD5E1;

  /* Text */
  --color-text: #0F172A;
  --color-text-muted: #64748B;
  --color-text-subtle: #94A3B8;

  /* Semantic */
  --color-success: #22C55E;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  --color-info: #3B82F6;
}
```

---

Color is one of the most powerful tools in design. Use it with intention, consistency, and accessibility in mind.
