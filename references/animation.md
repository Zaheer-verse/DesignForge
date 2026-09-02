# Animation and Motion Design

Motion is a powerful design tool when used purposefully. It communicates state, guides attention, and creates polish. Misused, it distracts and frustrates.

---

## Motion Philosophy

### Why Motion Matters

**Functional purposes:**
- **Feedback** — Confirms user actions
- **Orientation** — Shows spatial relationships
- **State change** — Communicates transitions
- **Attention** — Directs focus

**Emotional purposes:**
- **Brand personality** — Playful, serious, precise
- **Quality perception** — Polish and care
- **Delight** — Memorable moments

### Motion Principles

1. **Motion communicates** — Every animation sends a message
2. **Less is more** — Restraint creates impact
3. **Purpose over polish** — Function before decoration
4. **Performance matters** — Choppy animation is worse than none
5. **Accessibility first** — Respect reduced motion preferences

---

## Duration Scale

### Standard Durations

```css
:root {
  --duration-instant: 100ms;   /* Micro-interactions */
  --duration-fast: 150ms;      /* Hover, focus states */
  --duration-normal: 300ms;    /* Standard transitions */
  --duration-slow: 500ms;      /* Complex animations */
  --duration-slower: 750ms;    /* Page transitions */
  --duration-slowest: 1000ms;  /* Dramatic reveals */
}
```

### Duration Guidelines

| Element Type | Duration | Reason |
|--------------|----------|--------|
| Hover states | 100-150ms | Immediate feedback |
| Focus states | 100ms | Instant visibility |
| Button press | 100-150ms | Tactile response |
| Toggle | 200-300ms | State clarity |
| Card hover | 200-300ms | Subtle lift |
| Modal open | 200-400ms | Smooth appearance |
| Toast notification | 300-500ms | Attention without delay |
| Page transition | 400-600ms | Spatial orientation |
| Scroll reveal | 400-800ms | Narrative pacing |
| Hero entrance | 600-1000ms | Dramatic impact |

---

## Easing Functions

### Standard Easings

```css
:root {
  /* Enter: Start slow, end fast */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);

  /* Exit: Start fast, end slow */
  --ease-in: cubic-bezier(0.4, 0, 1, 1);

  /* Move: Start slow, middle fast, end slow */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);

  /* Spring: Bouncy, playful */
  --spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --spring-gentle: cubic-bezier(0.175, 0.885, 0.32, 1.275);

  /* Linear: Constant speed (rarely used) */
  --linear: linear;
}
```

### When to Use Each

**ease-out (default for entrances)**
```css
.modal-enter {
  animation: fadeSlideUp 300ms var(--ease-out);
}
```
- Elements appearing on screen
- Dropdowns opening
- Modals appearing
- Toast notifications

**ease-in (default for exits)**
```css
.modal-exit {
  animation: fadeSlideDown 200ms var(--ease-in);
}
```
- Elements leaving screen
- Dropdowns closing
- Modals disappearing

**ease-in-out (for movements)**
```css
.card:hover {
  transform: translateY(-4px);
  transition: transform 300ms var(--ease-in-out);
}
```
- Position changes
- Size changes
- Elements moving within container

**spring (for playful interactions)**
```css
.button:active {
  transform: scale(0.95);
  transition: transform 150ms var(--spring);
}
```
- Playful interactions
- Gaming interfaces
- Creative products
- Use sparingly

---

## Animation Types

### Entrance Animations

**Fade In**
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  animation: fadeIn 300ms var(--ease-out);
}
```

**Slide Up (from below)**
```css
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.slide-up {
  animation: slideUp 400ms var(--ease-out);
}
```

**Scale In**
```css
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.scale-in {
  animation: scaleIn 200ms var(--ease-out);
}
```

### Exit Animations

**Fade Out**
```css
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

.fade-out {
  animation: fadeOut 200ms var(--ease-in);
}
```

**Slide Down (exit down)**
```css
@keyframes slideDown {
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(20px);
  }
}
```

### Interaction Animations

**Button Hover**
```css
.button {
  transition: all 150ms var(--ease-out);
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.button:active {
  transform: translateY(0);
}
```

**Card Lift**
```css
.card {
  transition: all 300ms var(--ease-out);
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
}
```

**Input Focus**
```css
.input {
  transition: border-color 150ms var(--ease-out),
              box-shadow 150ms var(--ease-out);
}

.input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px var(--color-primary-alpha);
}
```

### Scroll Animations

**Scroll Reveal**
```css
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 600ms var(--ease-out),
              transform 600ms var(--ease-out);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

**Parallax**
```css
.parallax-layer {
  will-change: transform;
  transform: translateY(calc(var(--scroll) * 0.3));
}
```

---

## Stagger and Orchestration

### Staggering Principles

Don't animate everything at once. Create rhythm with staggered delays:

```css
.stagger-item {
  opacity: 0;
  transform: translateY(20px);
  animation: slideUp 400ms var(--ease-out) forwards;
}

.stagger-item:nth-child(1) { animation-delay: 0ms; }
.stagger-item:nth-child(2) { animation-delay: 100ms; }
.stagger-item:nth-child(3) { animation-delay: 200ms; }
.stagger-item:nth-child(4) { animation-delay: 300ms; }
```

### CSS Variables for Stagger

```css
.stagger-grid {
  --stagger-delay: 50ms;
}

.stagger-item {
  animation: slideUp 400ms var(--ease-out) forwards;
  animation-delay: calc(var(--index) * var(--stagger-delay));
}
```

---

## Reduced Motion

### Mandatory Support

Always support `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Thoughtful Reduced Motion

Some animations should persist:

```css
/* Remove decorative motion */
@media (prefers-reduced-motion: reduce) {
  .parallax { transform: none; }
  .floating { animation: none; }
}

/* Keep functional state changes */
@media (prefers-reduced-motion: reduce) {
  .collapse {
    transition: height 0.01ms; /* Instant but still functional */
  }
}
```

---

## Animation Libraries

### When to Use Libraries

**Use CSS for:**
- Simple hover/focus states
- Basic entrance/exit
- Performance-critical animations
- Simple transitions

**Use JavaScript libraries for:**
- Complex orchestrations
- Scroll-linked animations
- Drag interactions
- Physics-based motion
- Timeline control

### Library Selection

**Framer Motion / Motion One** (React)
```javascript
import { motion } from 'framer-motion';

<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
/>
```

**GSAP** (Framework-agnostic)
```javascript
import { gsap } from 'gsap';

gsap.to('.element', {
  opacity: 1,
  y: 0,
  duration: 0.4,
  ease: 'power2.out',
  stagger: 0.1
});
```

**React Spring** (Physics-based)
```javascript
import { useSpring, animated } from 'react-spring';

const props = useSpring({
  opacity: 1,
  transform: 'translateY(0px)',
  from: { opacity: 0, transform: 'translateY(20px)' },
  config: { tension: 280, friction: 60 }
});
```

---

## Performance Rules

### GPU Acceleration

Use properties that trigger GPU acceleration:

**Good (GPU accelerated):**
- `transform`
- `opacity`

**Avoid (trigger layout):**
- `width` / `height`
- `top` / `left` / `right` / `bottom`
- `margin` / `padding`

### will-change

Use sparingly for known animations:

```css
.will-animate {
  will-change: transform, opacity;
}

/* Remove after animation */
.animated {
  will-change: auto;
}
```

### Containment

```css
.animated-container {
  contain: layout style;
}
```

---

## Common Mistakes

❌ **Everything animates**
- Creates chaos
- Slows perceived performance
- Dilutes importance

❌ **Inconsistent durations**
- Feels amateur
- Breaks visual harmony

❌ **Ignoring reduced motion**
- Excludes users
- May cause discomfort

❌ **Animating layout properties**
- Causes jank
- Poor performance

❌ **Too slow**
- Feels sluggish
- Frustrates users

❌ **Too fast**
- Misses the purpose
- Creates jarring experience

---

## Quick Reference

```css
:root {
  /* Durations */
  --duration-fast: 150ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;

  /* Easings */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

Motion should feel inevitable, not added. Design animation as part of the system, not as decoration.
