# Layout Patterns

Layout determines how content is organized and how users navigate visual information. A strong layout creates clarity, hierarchy, and flow.

---

## Spacing System

### Base Unit

Use 4px as the base unit for all spacing:

```css
:root {
  --space-1: 4px;    /* Tight */
  --space-2: 8px;    /* Compact */
  --space-3: 12px;   /* Close */
  --space-4: 16px;   /* Standard */
  --space-5: 20px;   /* Comfortable */
  --space-6: 24px;   /* Relaxed */
  --space-8: 32px;   /* Generous */
  --space-10: 40px;  /* Spacious */
  --space-12: 48px;  /* Section */
  --space-16: 64px;  /* Large section */
  --space-20: 80px;  /* Major section */
  --space-24: 96px;  /* Hero section */
}
```

### Application

```css
/* Components */
.button {
  padding: var(--space-2) var(--space-4);
  gap: var(--space-2);
}

.card {
  padding: var(--space-6);
  border-radius: var(--space-3);
}

/* Sections */
.section {
  padding-block: var(--space-16);
  gap: var(--space-8);
}

/* Layouts */
.page {
  padding-inline: var(--space-4);
  max-width: 1280px;
  margin-inline: auto;
}
```

---

## Container System

### Width Constraints

```css
:root {
  /* Content widths */
  --width-prose: 65ch;          /* Optimal reading width */
  --width-narrow: 640px;        /* Forms, narrow content */
  --width-default: 768px;       /* Standard content */
  --width-wide: 1024px;         /* Wide content */
  --width-full: 1280px;         /* Full layouts */
  --width-max: 1440px;          /* Maximum width */
}
```

### Container Classes

```css
.container {
  width: 100%;
  max-width: var(--width-full);
  margin-inline: auto;
  padding-inline: var(--space-4);
}

.container-narrow {
  max-width: var(--width-narrow);
}

.container-prose {
  max-width: var(--width-prose);
}

.container-wide {
  max-width: var(--width-wide);
}
```

---

## Grid Systems

### CSS Grid Foundation

```css
.grid {
  display: grid;
  gap: var(--space-6);
}

.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid-cols-4 { grid-template-columns: repeat(4, 1fr); }

/* Responsive */
@media (min-width: 768px) {
  .md\:grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .lg\:grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
  .lg\:grid-cols-4 { grid-template-columns: repeat(4, 1fr); }
}
```

### Auto-fit Grid

```css
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-6);
}
```

---

## Advanced Layout Patterns

### Asymmetric Hero

```css
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-12);
  min-height: 80vh;
}

@media (max-width: 768px) {
  .hero {
    grid-template-columns: 1fr;
    min-height: auto;
  }
}
```

### Bento Grid

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(3, minmax(200px, auto));
  gap: var(--space-4);
}

.bento-item-large {
  grid-column: span 2;
  grid-row: span 2;
}

.bento-item-tall {
  grid-row: span 2;
}

.bento-item-wide {
  grid-column: span 2;
}
```

### Split Layout

```css
.split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
}

.split-fixed {
  position: sticky;
  top: 0;
  height: 100vh;
}

@media (max-width: 1024px) {
  .split {
    grid-template-columns: 1fr;
  }

  .split-fixed {
    position: relative;
    height: auto;
  }
}
```

### Overlapping Sections

```css
.overlap-container {
  position: relative;
}

.overlap-above {
  position: relative;
  z-index: 2;
  margin-bottom: -100px;
}

.overlap-below {
  position: relative;
  z-index: 1;
}
```

### Full-bleed Section

```css
.full-bleed {
  width: 100vw;
  margin-inline: calc(50% - 50vw);
  padding-inline: calc(50vw - 50%);
}

/* Or using container queries */
.full-bleed-modern {
  width: 100cqw;
  margin-inline: calc(50cqi - 50cqw);
}
```

---

## Navigation Layouts

### Header

```css
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-inline: var(--space-4);
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-nav {
  display: flex;
  align-items: center;
  gap: var(--space-6);
}

@media (max-width: 768px) {
  .header-nav {
    display: none; /* Replace with mobile menu */
  }
}
```

### Sidebar

```css
.layout-with-sidebar {
  display: grid;
  grid-template-columns: 240px 1fr;
  min-height: 100vh;
}

.sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
}

@media (max-width: 1024px) {
  .layout-with-sidebar {
    grid-template-columns: 1fr;
  }

  .sidebar {
    position: fixed;
    left: -240px; /* Hidden by default */
    transition: left 0.3s ease;
  }

  .sidebar.open {
    left: 0;
  }
}
```

---

## Section Spacing

### Vertical Rhythm

```css
:root {
  --section-gap: var(--space-16);
  --section-gap-lg: var(--space-24);
}

section + section {
  margin-block-start: var(--section-gap);
}

section:last-child {
  margin-block-end: var(--section-gap);
}

/* For major sections */
section.major {
  margin-block: var(--section-gap-lg);
}
```

### Content Spacing

```css
.section {
  display: flex;
  flex-direction: column;
  gap: var(--space-8);
}

.section-header {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.section-content {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}
```

---

## Common Layout Patterns

### Centered Content

```css
.centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  max-width: var(--width-prose);
  margin-inline: auto;
}
```

### Two-Column Feature

```css
.feature-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-12);
  align-items: center;
}

.feature-row:nth-child(even) .feature-image {
  order: -1;
}

@media (max-width: 768px) {
  .feature-row {
    grid-template-columns: 1fr;
  }

  .feature-row:nth-child(even) .feature-image {
    order: 0;
  }
}
```

### Three-Column Cards

```css
.cards-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

@media (max-width: 1024px) {
  .cards-3 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .cards-3 {
    grid-template-columns: 1fr;
  }
}
```

### Masonry

```css
.masonry {
  column-count: 3;
  column-gap: var(--space-6);
}

.masonry-item {
  break-inside: avoid;
  margin-bottom: var(--space-6);
}

@media (max-width: 1024px) {
  .masonry { column-count: 2; }
}

@media (max-width: 640px) {
  .masonry { column-count: 1; }
}
```

---

## Responsive Layout Strategy

### Breakpoints

```css
:root {
  --bp-sm: 640px;   /* Small tablets */
  --bp-md: 768px;   /* Tablets */
  --bp-lg: 1024px;  /* Laptops */
  --bp-xl: 1280px;  /* Desktops */
  --bp-2xl: 1536px; /* Large displays */
}
```

### Mobile-First Approach

```css
/* Base: Mobile styles */
.layout {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

/* Tablet and up */
@media (min-width: 768px) {
  .layout {
    flex-direction: row;
    gap: var(--space-6);
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .layout {
    gap: var(--space-8);
  }
}
```

### Content Reordering

```css
.mobile-order {
  display: flex;
  flex-direction: column;
}

.mobile-order-image {
  order: 1;
}

.mobile-order-content {
  order: 2;
}

@media (min-width: 768px) {
  .mobile-order-image {
    order: 2;
  }

  .mobile-order-content {
    order: 1;
  }
}
```

---

## Layout Anti-Patterns

❌ **Everything centered**
- Creates weak visual interest
- Lacks hierarchy

❌ **Equal spacing everywhere**
- No distinction between sections
- Lacks rhythm

❌ **Full-width text**
- Lines too long to read comfortably
- Use max-width: 65ch

❌ **No vertical rhythm**
- Inconsistent spacing
- Feels disjointed

❌ **Forgetting mobile**
- Desktop layouts compressed on mobile
- Not designed for mobile context

---

## Quick Reference

```css
:root {
  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;

  /* Container widths */
  --width-prose: 65ch;
  --width-narrow: 640px;
  --width-default: 768px;
  --width-wide: 1024px;
  --width-full: 1280px;

  /* Breakpoints */
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}
```

---

Layout creates the foundation for everything else. Get it right, and the rest becomes easier.
