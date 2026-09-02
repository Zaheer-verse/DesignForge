# Typography Guide

Typography is the foundation of web design. 90% of the web is text, making typography the single most impactful design decision.

---

## Typography Hierarchy

### The Scale

Establish a systematic scale, not arbitrary sizes:

```
Display     : 72px → 128px   (Hero headlines, landing pages)
H1          : 48px → 64px    (Page titles)
H2          : 32px → 48px    (Section headings)
H3          : 24px → 32px    (Subsection headings)
Body Large  : 20px → 24px    (Lead paragraphs, intros)
Body        : 16px → 18px    (Main content)
Small       : 14px → 16px    (Secondary content)
Caption     : 12px → 14px    (Labels, metadata)
Label       : 11px → 13px    (Tags, badges, tiny text)
```

### Fluid Typography

Use `clamp()` for responsive scaling without breakpoints:

```css
:root {
  --text-display: clamp(3rem, 8vw + 1rem, 8rem);
  --text-h1: clamp(2.5rem, 5vw + 1rem, 4rem);
  --text-h2: clamp(1.75rem, 4vw + 0.5rem, 3rem);
  --text-h3: clamp(1.25rem, 2vw + 0.5rem, 2rem);
  --text-body-lg: clamp(1.125rem, 1.5vw + 0.5rem, 1.5rem);
  --text-body: clamp(1rem, 1vw + 0.5rem, 1.125rem);
  --text-sm: clamp(0.875rem, 0.5vw + 0.5rem, 1rem);
  --text-caption: clamp(0.75rem, 0.5vw + 0.25rem, 0.875rem);
}
```

---

## Font Pairing

### The Rules

1. **Maximum 2 font families** (plus monospace if needed)
   - 1 display/heading font
   - 1 body font
   - Optional: monospace for code

2. **Contrast, not conflict**
   - Pair a distinctive display font with a neutral body font
   - Avoid two decorative fonts
   - Avoid two very similar fonts

3. **Test real content**
   - Headings look different in isolation vs. context
   - Check readability at all sizes
   - Verify special characters

### Pairing Strategies

**Strategy 1: Display + Neutral**
```
Headings: Inter Tight, Poppins, DM Sans Display
Body: Inter, DM Sans, Source Sans Pro
```
Modern, clean, professional

**Strategy 2: Serif + Sans**
```
Headings: Playfair Display, Merriweather, Lora
Body: Inter, Open Sans, Lato
```
Editorial, sophisticated, literary

**Strategy 3: Mono + Sans**
```
Headings: Space Mono, JetBrains Mono, IBM Plex Mono
Body: Inter, IBM Plex Sans, DM Sans
```
Technical, developer-focused, precise

**Strategy 4: Geometric + Humanist**
```
Headings: Poppins, Montserrat, Raleway
Body: Source Sans Pro, Nunito, Open Sans
```
Friendly, modern, approachable

**Strategy 5: Single Font, Multiple Weights**
```
Headings: Inter 700-900
Body: Inter 400-500
Code: Inter 400 (monospace variant)
```
Clean, cohesive, minimal

---

## Line Height

Line height (leading) affects readability significantly.

### Guidelines

```
Display/Headings: 1.1 → 1.2  (tighter for impact)
Body Text:        1.5 → 1.7  (generous for readability)
Small Text:       1.4 → 1.5  (slightly tighter for labels)
```

### CSS

```css
:root {
  --leading-tight: 1.1;
  --leading-snug: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
}

h1, h2, h3 {
  line-height: var(--leading-tight);
}

p, li {
  line-height: var(--leading-relaxed);
}

small, caption {
  line-height: var(--leading-normal);
}
```

---

## Letter Spacing

Track letter spacing to improve legibility at different sizes.

### Guidelines

```
Display/Headings: -0.02em to -0.04em  (tighter)
Body Text:         0em (normal)
Small Text:        0.01em to 0.02em (looser for legibility)
All Caps:          0.05em to 0.1em (always track out)
```

### CSS

```css
:root {
  --tracking-tighter: -0.04em;
  --tracking-tight: -0.02em;
  --tracking-normal: 0em;
  --tracking-wide: 0.02em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;
}

.display {
  letter-spacing: var(--tracking-tighter);
}

.all-caps {
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider);
}
```

---

## Measure (Line Length)

The width of text blocks affects readability.

### Optimal Measures

```
Body text:   65 → 80 characters (45 → 75 ideal)
Headings:    Shorter is fine, readability less critical
Mobile:      Full width minus padding
```

### CSS

```css
/* Optimal reading width */
.prose {
  max-width: 65ch; /* ch = width of "0" character */
  margin-inline: auto;
}

/* Wider for lead paragraphs */
.prose-lead {
  max-width: 75ch;
}

/* Narrower for captions */
.prose-caption {
  max-width: 45ch;
}
```

---

## Responsive Typography

### Mobile Considerations

1. **Scale down headings 15-25%**
   ```css
   h1 { font-size: clamp(2rem, 5vw, 4rem); }
   ```

2. **Maintain hierarchy**
   - Don't let headings become body-sized
   - Keep clear distinction between levels

3. **Increase line height slightly**
   ```css
   @media (max-width: 640px) {
     p { line-height: 1.7; }
   }
   ```

4. **Ensure touch-friendly tap targets**
   - Links and buttons: minimum 44px height

### Breakpoint Strategy

```css
:root {
  /* Mobile-first base */
  --text-h1: clamp(2rem, 5vw + 1rem, 4rem);
}

/* Or with explicit breakpoints */
@media (min-width: 640px) {
  h1 { font-size: 3rem; }
}

@media (min-width: 1024px) {
  h1 { font-size: 4rem; }
}
```

---

## Font Loading

### Performance

1. **Subset fonts** to only needed characters
2. **Preload critical fonts**
   ```html
   <link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
   ```

3. **Use `font-display: swap`**
   ```css
   @font-face {
     font-family: 'Inter';
     src: url('/fonts/inter-var.woff2') format('woff2');
     font-display: swap; /* Show fallback immediately */
   }
   ```

4. **Variable fonts** (when available)
   - Single file for multiple weights
   - Smaller total size
   - Smooth weight transitions

### Font Stack Fallbacks

```css
:root {
  /* System font fallbacks */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-serif: 'Lora', Georgia, 'Times New Roman', serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
}
```

---

## Typography by Context

### Landing Pages

- **Headings:** Bold, impactful, tight tracking
- **Body:** Slightly larger than standard (18-20px)
- **Hierarchy:** Strong contrast between levels

### Dashboards

- **Headings:** Medium weight, functional
- **Body:** Standard size (14-16px)
- **Data:** Monospace for numbers, right-aligned

### Documentation

- **Headings:** Clear hierarchy, functional
- **Body:** Optimal reading width (65ch)
- **Code:** Monospace, syntax highlighted

### Mobile Apps

- **Headings:** Bold but not oversized
- **Body:** Never smaller than 16px
- **Touch:** All text elements reachable

---

## Common Mistakes

❌ **Huge headings everywhere**
- Reserve large type for actual importance
- Create contrast, not uniformity

❌ **Too many font sizes**
- Use a scale, not arbitrary values
- Less is more

❌ **Poor line height**
- Tight line height strains reading
- Generous spacing aids comprehension

❌ **No fallback fonts**
- Always define fallbacks
- Test without web fonts loaded

❌ **Unreadable contrast**
- Maintain 4.5:1 contrast ratio
- Test on various backgrounds

❌ **Centered body text**
- Left-align for readability
- Center only short headings

---

## Quick Reference

```css
:root {
  /* Fonts */
  --font-display: 'Inter Tight', var(--font-sans);
  --font-body: 'Inter', var(--font-sans);
  --font-mono: 'JetBrains Mono', monospace;

  /* Sizes (fluid) */
  --text-xs: clamp(0.75rem, 0.5vw + 0.5rem, 0.875rem);
  --text-sm: clamp(0.875rem, 0.5vw + 0.5rem, 1rem);
  --text-base: clamp(1rem, 1vw + 0.5rem, 1.125rem);
  --text-lg: clamp(1.125rem, 1.5vw + 0.5rem, 1.5rem);
  --text-xl: clamp(1.25rem, 2vw + 0.5rem, 2rem);
  --text-2xl: clamp(1.5rem, 3vw + 0.5rem, 2.5rem);
  --text-3xl: clamp(2rem, 4vw + 1rem, 3rem);
  --text-4xl: clamp(2.5rem, 5vw + 1rem, 4rem);
  --text-5xl: clamp(3rem, 8vw + 1rem, 6rem);

  /* Line heights */
  --leading-tight: 1.2;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;

  /* Letter spacing */
  --tracking-tight: -0.02em;
  --tracking-normal: 0em;
  --tracking-wide: 0.02em;
}
```

---

Typography is the foundation of great design. Get it right, and everything else becomes easier.
