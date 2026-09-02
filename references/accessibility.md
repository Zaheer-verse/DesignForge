# Accessibility Guide

Accessibility is not optional. 1 in 5 users has a disability. Inaccessible design excludes real people from using your product.

---

## WCAG Principles

### Four Principles (POUR)

**Perceivable**
- Users can perceive the content
- Text alternatives for images
- Captions for video
- Sufficient color contrast

**Operable**
- Users can operate the interface
- Keyboard accessible
- Enough time to read
- No seizure triggers

**Understandable**
- Users can understand the content
- Readable text
- Predictable behavior
- Help with errors

**Robust**
- Works with assistive technologies
- Valid HTML
- Compatible with current and future tools

---

## Semantic HTML

### Use Proper Elements

```html
<!-- Bad -->
<div class="button" onclick="submit()">Submit</div>

<!-- Good -->
<button type="submit">Submit</button>
```

### Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Page Title</title>
</head>
<body>
  <header>
    <nav aria-label="Main navigation">
      <!-- Navigation -->
    </nav>
  </header>

  <main>
    <article>
      <h1>Main Heading</h1>
      <h2>Section Heading</h2>
      <h3>Subsection Heading</h3>
    </article>
  </main>

  <aside>
    <!-- Sidebar -->
  </aside>

  <footer>
    <!-- Footer -->
  </footer>
</body>
</html>
```

### Heading Hierarchy

```
H1 (1 per page)
├─ H2
│  ├─ H3
│  └─ H3
├─ H2
│  └─ H3
└─ H2
```

Never skip levels: H1 → H2 → H3 (not H1 → H3)

---

## Keyboard Navigation

### Focus Management

All interactive elements must be keyboard accessible:

```css
/* Visible focus state */
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Remove outline only if :focus-visible is supported */
:focus:not(:focus-visible) {
  outline: none;
}
```

### Focus Order

Logical tab order follows DOM order:

```html
<!-- Bad: Visual order differs from DOM order -->
<div style="display: flex; flex-direction: row-reverse;">
  <button>First</button>
  <button>Second</button>
</div>

<!-- Good: Match visual and DOM order -->
<div style="display: flex;">
  <button>Second</button>
  <button>First</button>
</div>
```

### Skip Links

```html
<a href="#main-content" class="skip-link">
  Skip to main content
</a>

<main id="main-content">
  <!-- Content -->
</main>
```

```css
.skip-link {
  position: absolute;
  top: -100px;
  left: 0;
  padding: 8px 16px;
  background: var(--color-primary);
  color: white;
  z-index: 1000;
}

.skip-link:focus {
  top: 0;
}
```

### Keyboard Traps

Never trap keyboard focus:

```javascript
// Bad: Focus trapped in modal
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    e.preventDefault(); // Traps focus!
  }
});

// Good: Cycle focus within modal
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    const focusable = modal.querySelectorAll('button, [href], input, select, textarea');
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }
});
```

---

## Color and Contrast

### Minimum Contrast Ratios

| Text Size | WCAG AA | WCAG AAA |
|-----------|---------|----------|
| Normal text (< 18px) | 4.5:1 | 7:1 |
| Large text (≥ 18px or 14px bold) | 3:1 | 4.5:1 |
| UI components | 3:1 | — |

### Don't Rely on Color Alone

```html
<!-- Bad: Only color indicates error -->
<input class="error" />

<!-- Good: Color + text + icon -->
<input class="error" aria-describedby="error-message" />
<span id="error-message" class="error-text">
  <svg aria-hidden="true">...</svg>
  Please enter a valid email
</span>
```

### Focus Visibility

```css
/* Never remove outline without replacement */
:focus {
  outline: none; /* BAD */
}

/* Provide alternative */
:focus {
  outline: none;
  box-shadow: 0 0 0 3px var(--color-focus-ring);
}
```

---

## Images and Media

### Alt Text

```html
<!-- Informative images -->
<img src="chart.png" alt="Sales increased 25% in Q4 2024">

<!-- Decorative images -->
<img src="decoration.png" alt="">

<!-- Complex images -->
<img src="organizational-chart.png" alt="Company organizational chart"
     aria-describedby="chart-description">
<p id="chart-description">
  The CEO oversees three divisions: Engineering, Marketing, and Sales...
</p>
```

### Video

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions.vtt" srclang="en" label="English">
</video>
```

---

## Forms

### Labels

```html
<!-- Explicit label -->
<label for="email">Email address</label>
<input id="email" type="email">

<!-- Implicit label -->
<label>
  Email address
  <input type="email">
</label>

<!-- aria-label (when visible label not possible) -->
<input type="search" aria-label="Search">
```

### Error Messages

```html
<input
  id="email"
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
>
<span id="email-error" role="alert">
  Please enter a valid email address
</span>
```

### Required Fields

```html
<label for="name">
  Name
  <span aria-hidden="true">*</span>
  <span class="sr-only">(required)</span>
</label>
<input id="name" required>
```

---

## ARIA Usage

### When to Use ARIA

**Use ARIA when:**
- Semantic HTML doesn't exist for your pattern
- Enhancing existing semantics
- Creating custom widgets

**Don't use ARIA when:**
- A native HTML element exists
- You can modify HTML instead

### Common ARIA Attributes

```html
<!-- Live regions for dynamic content -->
<div aria-live="polite">Message sent successfully</div>
<div aria-live="assertive">Error: Form submission failed</div>

<!-- Expanded/collapsed state -->
<button aria-expanded="false" aria-controls="menu">
  Menu
</button>

<!-- Current page in navigation -->
<nav aria-label="Main">
  <a href="/">Home</a>
  <a href="/about" aria-current="page">About</a>
</nav>

<!-- Hidden from screen readers -->
<span aria-hidden="true">★</span>

<!-- Described by -->
<button aria-describedby="tooltip">Help</button>
<div id="tooltip" role="tooltip">Click for more information</div>
```

### Screen Reader Only Content

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

---

## Motion and Animation

### Reduced Motion

Always support `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  /* Remove parallax */
  .parallax {
    transform: none !important;
  }

  /* Remove auto-play */
  .carousel {
    scroll-behavior: auto;
  }
}
```

### Seizure Prevention

Avoid rapid flashing:
- No more than 3 flashes per second
- Avoid red flashing
- Provide pause controls for animations

---

## Touch Targets

### Minimum Size

```css
/* Minimum 44x44px touch target */
.button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px;
}

/* Increase spacing between targets */
.nav-item {
  padding: 12px 16px;
}
```

### Touch Target Spacing

```css
/* At least 8px between touch targets */
.button-group {
  display: flex;
  gap: 8px;
}
```

---

## Testing

### Automated Testing

```bash
# axe-core CLI
axe-cli https://example.com

# pa11y
pa11y https://example.com

# Lighthouse
lighthouse https://example.com --only-categories=accessibility
```

### Manual Testing Checklist

- [ ] Tab through entire page
- [ ] All interactive elements focusable
- [ ] Focus visible on all elements
- [ ] No keyboard traps
- [ ] Screen reader navigation
- [ ] Heading structure correct
- [ ] Alt text for images
- [ ] Form labels present
- [ ] Error messages announced
- [ ] Color contrast sufficient
- [ ] Touch targets large enough
- [ ] Reduced motion respected

### Screen Reader Testing

**NVDA (Windows, free)**
- Download: nvaccess.org
- Shortcut: Insert + Q

**VoiceOver (macOS, built-in)**
- Enable: System Preferences → Accessibility
- Shortcut: Cmd + F5

**JAWS (Windows, paid)**
- Industry standard for enterprise

---

## Common Mistakes

❌ **Missing alt text**
- All images need alt (even if empty)

❌ **Poor color contrast**
- Test all text/background combinations

❌ **No keyboard support**
- Test tab navigation

❌ **Missing form labels**
- Every input needs a label

❌ **Autoplay media**
- Never autoplay audio/video

❌ **Tiny touch targets**
- Minimum 44x44px

❌ **Ignoring reduced motion**
- Support `prefers-reduced-motion`

❌ **Using only color**
- Add text/icons for state

---

## Quick Reference

```css
/* Focus visible */
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Screen reader only */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

/* Touch targets */
button, a {
  min-height: 44px;
  min-width: 44px;
}
```

---

Accessibility is not a feature—it's a requirement. Build it in from the start.
