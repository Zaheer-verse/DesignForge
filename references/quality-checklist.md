# Quality Checklist

Final verification checklist before marking any web design task complete.

---

## Visual Hierarchy

- [ ] Clear focal point on every page
- [ ] Most important element has highest visual weight
- [ ] Secondary content visually subordinate
- [ ] Scanning reveals content priority
- [ ] No competing elements of equal importance

---

## Typography

- [ ] Font sizes follow a systematic scale
- [ ] Line height appropriate for each size
- [ ] Line length under 80 characters for body text
- [ ] Letter spacing adjusted for headings and small text
- [ ] Font weights create hierarchy
- [ ] Consistent font pairing (max 2-3 families)

---

## Color

- [ ] Color system with semantic tokens
- [ ] All text meets 4.5:1 contrast ratio
- [ ] Large text meets 3:1 contrast ratio
- [ ] Color not used as only indicator
- [ ] Dark mode supported (if applicable)
- [ ] Brand colors used consistently

---

## Spacing

- [ ] Spacing follows a consistent scale
- [ ] Generous whitespace around important elements
- [ ] Consistent section spacing
- [ ] Adequate padding in components
- [ ] No cramped elements

---

## Layout

- [ ] Grid system established and followed
- [ ] Content width constrained for readability
- [ ] No horizontal scroll (unless intentional)
- [ ] Sections clearly delineated
- [ ] Visual rhythm maintained

---

## Responsive Design

- [ ] Works at 320px width
- [ ] Works at 768px width
- [ ] Works at 1024px width
- [ ] Works at 1440px+ width
- [ ] Touch targets minimum 44x44px on mobile
- [ ] No content cut off at any viewport
- [ ] Navigation accessible on all devices
- [ ] Images scale appropriately

---

## Interaction

### Hover States
- [ ] All interactive elements have hover states
- [ ] Hover feedback is immediate (100-150ms)
- [ ] Hover states are visible and clear

### Focus States
- [ ] All interactive elements focusable via keyboard
- [ ] Focus states are visible
- [ ] Focus order is logical
- [ ] No keyboard traps

### Active States
- [ ] Buttons have pressed states
- [ ] Active states provide feedback
- [ ] State changes are smooth

### Loading States
- [ ] Skeleton or loading indicator for async content
- [ ] Buttons show loading state during action
- [ ] User understands when waiting is required

### Error States
- [ ] Form errors clearly indicated
- [ ] Error messages are helpful
- [ ] User can recover from errors

### Empty States
- [ ] Empty states are designed
- [ ] Empty states guide user action
- [ ] Not just blank screens

### Success States
- [ ] Success actions confirmed
- [ ] Success feedback provided
- [ ] User knows what happened

---

## Animation

- [ ] Animations have purpose
- [ ] Duration feels appropriate (not too slow/fast)
- [ ] Easing is smooth
- [ ] Stagger used for multiple elements
- [ ] `prefers-reduced-motion` supported
- [ ] No animation overload
- [ ] Performance is smooth (60fps)

---

## Accessibility

### Keyboard
- [ ] All interactive elements reachable via Tab
- [ ] Skip link provided
- [ ] Modal traps focus appropriately
- [ ] Escape closes modals/dropdowns
- [ ] No keyboard traps

### Screen Reader
- [ ] Semantic HTML used throughout
- [ ] Images have appropriate alt text
- [ ] Form inputs have labels
- [ ] Headings follow logical hierarchy (H1→H2→H3)
- [ ] ARIA used only when necessary
- [ ] Live regions for dynamic content

### Visual
- [ ] Color contrast ratios met
- [ ] Text resizable to 200%
- [ ] Content visible at 400% zoom
- [ ] No seizure-inducing content

### Motion
- [ ] `prefers-reduced-motion` respected
- [ ] No auto-playing video with sound
- [ ] Animations can be paused

---

## Performance

- [ ] Images optimized and compressed
- [ ] Modern image formats used (WebP, AVIF)
- [ ] Lazy loading for below-fold content
- [ ] Fonts preloaded or use font-display: swap
- [ ] No render-blocking resources
- [ ] Initial page weight under 500KB (excluding images)
- [ ] Lighthouse performance score 80+

---

## Content

- [ ] Real content or realistic placeholder
- [ ] No lorem ipsum in production
- [ ] Headlines are clear and specific
- [ ] CTAs are action-oriented
- [ ] Error messages are helpful
- [ ] Content is scannable

---

## Browser Testing

- [ ] Chrome tested
- [ ] Firefox tested
- [ ] Safari tested
- [ ] Edge tested
- [ ] Mobile Safari tested
- [ ] Mobile Chrome tested

---

## Code Quality

- [ ] Semantic HTML
- [ ] CSS follows naming conventions
- [ ] No inline styles (unless necessary)
- [ ] Components are reusable
- [ ] No console errors
- [ ] No hardcoded values (use tokens)

---

## 3D/WebGL (if applicable)

- [ ] 3D serves a purpose
- [ ] Performance tested on mobile
- [ ] Fallback provided for non-WebGL
- [ ] Reduced motion removes 3D
- [ ] Assets optimized
- [ ] Frame rate acceptable (30+ fps)

---

## Final Verification

- [ ] Does the page immediately communicate what it is?
- [ ] Is the most important action obvious?
- [ ] Is the hierarchy clear?
- [ ] Does it look intentional?
- [ ] Does it have a recognizable visual identity?
- [ ] Does mobile feel designed, not compressed?
- [ ] Can users accomplish their goals?
- [ ] Does anything look generic or template-like?
- [ ] Can any element be removed?
- [ ] Does it feel professional and premium?

---

## Sign-Off

**Designer:** _________________

**Date:** _________________

**Notes:**
________________________________

---

Use this checklist for every project. Quality is in the details.
