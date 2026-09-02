# Anti-Patterns

Patterns and practices to avoid when designing modern web interfaces. These common mistakes make designs feel generic, amateur, or unusable.

---

## Visual Anti-Patterns

### ❌ Generic Hero Sections

**The Problem:**
Every AI-generated landing page has the same hero structure:
- Giant gradient text headline
- Generic subheadline
- Two CTA buttons (one filled, one outline)
- Random floating decorative elements

**Better Approach:**
- Create unique layout compositions
- Use distinctive typography treatments
- Design meaningful visuals that support the message
- Vary the structure based on content and brand

### ❌ Excessive Glassmorphism

**The Problem:**
Blur and transparency applied everywhere without purpose:
- Every card has backdrop-filter
- Multiple layers of glass effects
- Text unreadable against busy backgrounds

**Better Approach:**
- Use glassmorphism only when depth differentiation is needed
- Ensure text remains readable
- Apply to specific, purposeful elements
- Provide solid fallbacks for older browsers

### ❌ Random Gradient Overload

**The Problem:**
Purple-to-blue gradients on every element:
- Background gradients everywhere
- Gradient text for all headings
- Gradient borders on all cards

**Better Approach:**
- Use gradients with purpose (brand, depth, focus)
- Choose brand-appropriate colors
- Reserve gradients for key moments
- Consider solid colors for simplicity

### ❌ Floating Blobs and Shapes

**The Problem:**
Random decorative elements that add nothing:
- Amorphous gradient blobs
- Random geometric shapes
- Meaningless 3D objects

**Better Approach:**
- Every element should support the message
- Use decorative elements to guide attention
- Consider whitespace instead
- Connect visuals to brand identity

### ❌ Excessive Rounded Cards

**The Problem:**
Every container is a rounded card with shadow:
- Monotonous visual rhythm
- No distinction between elements
- Overused pattern

**Better Approach:**
- Viate container styles
- Use different shapes for hierarchy
- Consider sharp edges for some elements
- Mix card styles intentionally

---

## Layout Anti-Patterns

### ❌ Everything Centered

**The Problem:**
All content centered by default:
- Weak visual interest
- No asymmetric tension
- Missed opportunities for hierarchy

**Better Approach:**
- Use intentional alignment
- Create asymmetric compositions
- Left-align body text
- Center only key focal points

### ❌ Three-Column Feature Grids

**The Problem:**
Every features section uses the same 3-column grid:
- Icon + title + description
- No variation or hierarchy
- Boring, template look

**Better Approach:**
- Vary the layout structure
- Use different grid patterns
- Add visual interest with asymmetry
- Consider bento or editorial layouts

### ❌ Stock Template Layouts

**The Problem:**
Layouts that scream "template":
- Predictable section order
- Standard hero/feature/pricing/CTA flow
- No unique structure

**Better Approach:**
- Create custom layout compositions
- Break conventions intentionally
- Design for the specific content
- Consider unique section arrangements

---

## Typography Anti-Patterns

### ❌ Huge Headings Everywhere

**The Problem:**
Oversized headings for minor content:
- Diminishes importance
- No hierarchy
- Wastes space

**Better Approach:**
- Reserve large type for actual importance
- Create clear size hierarchy
- Use size purposefully
- Consider context

### ❌ Poor Line Length

**The Problem:**
Text spanning full width:
- Lines too long to read comfortably
- Eye strain
- Poor readability

**Better Approach:**
- Limit body text to 65-80 characters
- Use max-width: 65ch
- Create readable column widths
- Consider responsive measure

### ❌ Too Many Font Sizes

**The Problem:**
Arbitrary font sizes throughout:
- No system
- Inconsistent hierarchy
- Visual noise

**Better Approach:**
- Use a type scale
- Limit to 8-10 sizes
- Apply consistently
- Document the system

---

## Color Anti-Patterns

### ❌ Arbitrary Colors

**The Problem:**
Random hex values with no system:
- Inconsistency
- Hard to maintain
- No dark mode support

**Better Approach:**
- Use design tokens
- Create semantic color variables
- Support theming
- Document the system

### ❌ Insufficient Contrast

**The Problem:**
Text unreadable on backgrounds:
- Low contrast gray text
- Colored text on colored backgrounds
- Accessibility failures

**Better Approach:**
- Ensure 4.5:1 contrast ratio
- Test all color combinations
- Use contrast checker tools
- Consider all users

### ❌ Color-Only Indicators

**The Problem:**
State communicated only through color:
- Color blind users excluded
- Missed information
- Accessibility failure

**Better Approach:**
- Combine color with text/icons
- Use patterns or shapes
- Ensure multiple indicators
- Test with grayscale

---

## Interaction Anti-Patterns

### ❌ No Hover States

**The Problem:**
Interactive elements with no feedback:
- Users uncertain what's clickable
- Poor discoverability
- Missing affordance

**Better Approach:**
- Clear hover states for all interactive elements
- Visible focus states
- Tactile feedback
- Consistent interaction patterns

### ❌ Hidden Navigation

**The Problem:**
Navigation that's hard to find or use:
- Obscure hamburger icons
- Non-obvious menus
- Confusing structure

**Better Approach:**
- Clear navigation labels
- Visible primary navigation
- Logical structure
- Mobile-friendly patterns

### ❌ Autoplay Media

**The Problem:**
Audio/video playing without consent:
- Startles users
- Interrupts
- Accessibility failure

**Better Approach:**
- Never autoplay with sound
- Provide clear controls
- User-initiated playback
- Respect preferences

---

## Animation Anti-Patterns

### ❌ Animation Overload

**The Problem:**
Everything animates simultaneously:
- Distracting
- Slows perceived performance
- Reduces impact

**Better Approach:**
- Animate purposefully
- Stagger animations
- Reserve motion for key moments
- Support reduced motion

### ❌ Ignoring Reduced Motion

**The Problem:**
No support for prefers-reduced-motion:
- Excludes users
- May cause discomfort
- Accessibility failure

**Better Approach:**
- Always support reduced motion
- Remove decorative animation
- Keep functional state changes
- Test with the setting enabled

### ❌ Slow Animations

**The Problem:**
Animations that take too long:
- Frustrates users
- Slows tasks
- Feels sluggish

**Better Approach:**
- Hover: 100-150ms
- Transitions: 200-400ms
- Page transitions: 300-600ms
- Only go slower for dramatic effect

---

## 3D Anti-Patterns

### ❌ 3D for the Sake of 3D

**The Problem:**
3D elements that serve no purpose:
- Random rotating objects
- Unnecessary complexity
- Performance impact

**Better Approach:**
- Use 3D when it improves understanding
- Product visualization
- Spatial storytelling
- Brand expression

### ❌ Heavy 3D on Mobile

**The Problem:**
Complex 3D scenes on mobile:
- Poor performance
- Battery drain
- Bad experience

**Better Approach:**
- Simplify or disable on mobile
- Reduce polygon count
- Lower texture resolution
- Provide fallbacks

---

## Content Anti-Patterns

### ❌ Lorem Ipsum

**The Problem:**
Placeholder text in production:
- Looks unfinished
- No hierarchy demonstration
- Lazy

**Better Approach:**
- Write real content
- Or create realistic placeholder content
- Demonstrate actual hierarchy
- Show real use cases

### ❌ Generic Marketing Speak

**The Problem:**
Phrases like "Revolutionize your workflow":
- Meaningless
- Not believable
- Easy to ignore

**Better Approach:**
- Specific benefits
- Concrete claims
- Real examples
- Honest value propositions

---

## Accessibility Anti-Patterns

### ❌ Missing Alt Text

**The Problem:**
Images without alternative text:
- Screen reader users excluded
- SEO impact
- Accessibility failure

**Better Approach:**
- All images need alt text
- Describe meaningful content
- Empty alt for decorative images
- Consider context

### ❌ Tiny Touch Targets

**The Problem:**
Buttons/links too small for touch:
- Frustrating on mobile
- Missed taps
- Poor UX

**Better Approach:**
- Minimum 44x44px touch targets
- Adequate spacing between targets
- Touch-friendly design
- Mobile-first approach

### ❌ Keyboard Inaccessible

**The Problem:**
Can't navigate with keyboard:
- Excludes keyboard users
- Focus trap issues
- Missing focus states

**Better Approach:**
- All interactive elements focusable
- Visible focus indicators
- Logical tab order
- No keyboard traps

---

## Performance Anti-Patterns

### ❌ Unoptimized Images

**The Problem:**
Massive unoptimized images:
- Slow load times
- Bandwidth waste
- Poor mobile experience

**Better Approach:**
- Compress images
- Use modern formats (WebP, AVIF)
- Implement lazy loading
- Serve responsive sizes

### ❌ Excessive JavaScript

**The Problem:**
JS for everything:
- Slow initial load
- Poor performance
- Unnecessary complexity

**Better Approach:**
- Use CSS when possible
- Lazy load JavaScript
- Code splitting
- Minimize dependencies

---

## Quick Reference: Anti-Pattern Checklist

Avoid these at all costs:

- [ ] Generic hero structures
- [ ] Excessive glassmorphism
- [ ] Random gradient everywhere
- [ ] Floating blobs without purpose
- [ ] All centered layouts
- [ ] Three-column feature grids
- [ ] Huge headings everywhere
- [ ] Poor line length
- [ ] Arbitrary colors
- [ ] Insufficient contrast
- [ ] Color-only indicators
- [ ] No hover states
- [ ] Hidden navigation
- [ ] Autoplay media
- [ ] Animation overload
- [ ] Ignoring reduced motion
- [ ] 3D without purpose
- [ ] Lorem ipsum in production
- [ ] Generic marketing speak
- [ ] Missing alt text
- [ ] Tiny touch targets
- [ ] Keyboard inaccessible
- [ ] Unoptimized images
- [ ] Excessive JavaScript

---

Great design is as much about what you avoid as what you create. Recognize these patterns and eliminate them.
