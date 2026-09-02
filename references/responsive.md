# Responsive Design

Responsive design is not just about making things fit on mobile. It's about designing the right experience for each context.

---

## Mobile-First Philosophy

### Why Mobile-First

1. **Constraints breed creativity** — Start with limitations
2. **Performance** — Mobile networks are slower
3. **Prioritization** — Forces content decisions
4. **Progressive enhancement** — Add complexity, don't remove it

### Approach

```css
/* Mobile-first: Base styles for mobile */
.component {
  padding: 16px;
  font-size: 16px;
}

/* Enhance for larger screens */
@media (min-width: 768px) {
  .component {
    padding: 24px;
    font-size: 18px;
  }
}

@media (min-width: 1024px) {
  .component {
    padding: 32px;
    font-size: 20px;
  }
}
```

---

## Breakpoints

### Standard Breakpoints

```css
:root {
  --bp-sm: 640px;   /* Small tablets */
  --bp-md: 768px;   /* Tablets */
  --bp-lg: 1024px;  /* Laptops */
  --bp-xl: 1280px;  /* Desktops */
  --bp-2xl: 1536px; /* Large displays */
}
```

### Breakpoint Usage

```css
/* Small devices (phones, 0-639px) */
/* Base styles - no media query */

/* Medium devices (tablets, 640px+) */
@media (min-width: 640px) { }

/* Large devices (laptops, 768px+) */
@media (min-width: 768px) { }

/* Extra large devices (desktops, 1024px+) */
@media (min-width: 1024px) { }

/* 2XL devices (large displays, 1280px+) */
@media (min-width: 1280px) { }

/* 3XL devices (ultra-wide, 1536px+) */
@media (min-width: 1536px) { }
```

### Container Queries (Modern)

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}
```

---

## Layout Patterns

### Responsive Grid

```css
.grid {
  display: grid;
  gap: 16px;
  grid-template-columns: 1fr;
}

/* 2 columns on tablet+ */
@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 3 columns on laptop+ */
@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }
}

/* 4 columns on desktop+ */
@media (min-width: 1280px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

### Responsive Navigation

```css
/* Mobile: Hamburger menu */
.nav-mobile {
  display: flex;
}

.nav-desktop {
  display: none;
}

@media (min-width: 1024px) {
  .nav-mobile {
    display: none;
  }

  .nav-desktop {
    display: flex;
  }
}
```

### Responsive Typography

```css
:root {
  /* Fluid typography scales automatically */
  --text-h1: clamp(2rem, 5vw + 1rem, 4rem);
  --text-h2: clamp(1.5rem, 4vw + 0.5rem, 3rem);
  --text-body: clamp(1rem, 1vw + 0.5rem, 1.125rem);
}
```

---

## Mobile-Specific Considerations

### Touch Targets

```css
/* Minimum 44x44px touch targets */
button,
a,
input,
select,
textarea {
  min-height: 44px;
  min-width: 44px;
}

/* Spacing between targets */
.button-group {
  display: flex;
  gap: 8px;
}
```

### Safe Areas

```css
/* Account for notches and home indicators */
.app {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}
```

### Hover States on Touch

```css
/* Hover only on devices that support it */
@media (hover: hover) {
  .card:hover {
    transform: translateY(-4px);
  }
}

/* Active state for touch */
.card:active {
  transform: scale(0.98);
}
```

---

## Testing Checklist

- [ ] Content readable on 320px width
- [ ] Touch targets at least 44px
- [ ] No horizontal scroll
- [ ] Images load appropriately
- [ ] Navigation accessible
- [ ] Forms usable
- [ ] Text readable (no pinch zoom needed)
- [ ] No content cut off
- [ ] Proper safe area handling

---

## Quick Reference

```css
/* Breakpoints */
@media (min-width: 640px) { /* tablet */ }
@media (min-width: 768px) { /* laptop */ }
@media (min-width: 1024px) { /* desktop */ }
@media (min-width: 1280px) { /* large */ }

/* Touch targets */
button, a {
  min-height: 44px;
  min-width: 44px;
}

/* Hover only on supported devices */
@media (hover: hover) {
  .card:hover { transform: translateY(-4px); }
}
```

---

Design for context, not just screen size. Mobile users have different goals, environments, and constraints.
