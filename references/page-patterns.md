# Page Patterns

Different pages require different design strategies. This guide covers common page types and their specific design considerations.

---

## Landing Page

### Purpose
Convert visitors by communicating value proposition clearly and compelling visitors to take action.

### Key Elements

**Hero Section**
- Clear, bold headline
- Supporting subheadline
- Primary CTA
- Supporting visual (product screenshot, illustration)

**Social Proof**
- Logos of trusted brands
- Testimonials
- User count or metrics

**Features Section**
- 3-5 key features
- Clear benefits, not just features
- Visual demonstrations

**Pricing** (if applicable)
- Clear pricing tiers
- Feature comparison
- CTA for each tier

**Final CTA**
- Reinforce value
- Clear action
- Reduce friction

### Design Approach

```css
.landing-hero {
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: var(--space-16) var(--space-4);
}

.landing-hero h1 {
  font-size: clamp(2.5rem, 8vw, 5rem);
  font-weight: 800;
  line-height: 1.1;
  max-width: 900px;
}

.landing-hero p {
  font-size: clamp(1.125rem, 2vw, 1.5rem);
  color: var(--color-text-muted);
  max-width: 600px;
  margin-top: var(--space-4);
}
```

---

## Dashboard

### Purpose
Enable users to monitor, analyze, and act on data efficiently.

### Key Elements

**Navigation**
- Sidebar or top navigation
- Clear hierarchy
- Quick access to common actions

**Header**
- Page title
- Primary actions
- Search
- User menu

**Content Area**
- KPI cards
- Charts and visualizations
- Data tables
- Filters

### Design Approach

```css
.dashboard-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  min-height: 100vh;
}

.dashboard-main {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
  padding: var(--space-6);
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-4);
}

@media (max-width: 1024px) {
  .dashboard-layout {
    grid-template-columns: 1fr;
  }
}
```

### Data Visualization

- Use appropriate chart types
- Provide context (comparisons, trends)
- Enable drill-down
- Support accessibility (data tables as alternative)

---

## Authentication Pages

### Purpose
Enable secure access while minimizing friction.

### Key Elements

**Sign In**
- Email/password fields
- Social login options
- Forgot password link
- Remember me option
- Sign up link

**Sign Up**
- Minimal required fields
- Password requirements
- Terms acceptance
- Sign in link

**Password Reset**
- Email field
- Success confirmation
- Resend option

### Design Approach

```css
.auth-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
}

.auth-form-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: var(--space-8);
  max-width: 400px;
  margin: 0 auto;
}

.auth-visual {
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 768px) {
  .auth-layout {
    grid-template-columns: 1fr;
  }

  .auth-visual {
    display: none;
  }
}
```

---

## Documentation

### Purpose
Enable users to find, understand, and apply information.

### Key Elements

**Navigation**
- Sidebar with table of contents
- Search
- Breadcrumbs
- Version selector

**Content**
- Clear headings
- Code examples
- Screenshots/diagrams
- Related links

**Interactivity**
- Copy code buttons
- Live examples
- Feedback buttons

### Design Approach

```css
.docs-layout {
  display: grid;
  grid-template-columns: 250px 1fr 200px;
  min-height: 100vh;
}

.docs-content {
  max-width: 800px;
  margin: 0 auto;
  padding: var(--space-8);
}

.docs-content pre {
  background: var(--color-bg-muted);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  overflow-x: auto;
}

@media (max-width: 1024px) {
  .docs-layout {
    grid-template-columns: 1fr;
  }
}
```

---

## E-commerce Product Page

### Purpose
Convert browsers to buyers by providing information and reducing purchase friction.

### Key Elements

**Product Images**
- High-quality hero image
- Thumbnail gallery
- Zoom capability
- 360° view (optional)

**Product Information**
- Title
- Price
- Rating/reviews
- Description
- Variants (size, color)

**Purchase Actions**
- Add to cart
- Buy now
- Wishlist
- Share

**Social Proof**
- Reviews
- Related products
- Recently viewed

### Design Approach

```css
.product-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-8);
  padding: var(--space-8);
}

.product-images {
  position: sticky;
  top: var(--space-8);
}

.product-gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-2);
  margin-top: var(--space-4);
}

@media (max-width: 768px) {
  .product-layout {
    grid-template-columns: 1fr;
  }

  .product-images {
    position: relative;
  }
}
```

---

## Settings Page

### Purpose
Allow users to customize their experience and manage their account.

### Key Elements

**Navigation**
- Settings categories
- Search settings
- Breadcrumbs

**Settings Sections**
- Profile
- Security
- Notifications
- Billing
- Integrations
- Preferences

### Design Approach

```css
.settings-layout {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: var(--space-8);
  padding: var(--space-8);
}

.settings-section {
  padding: var(--space-6);
  border-bottom: 1px solid var(--color-border);
}

.settings-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-4) 0;
}

@media (max-width: 768px) {
  .settings-layout {
    grid-template-columns: 1fr;
  }
}
```

---

## AI Chat Interface

### Purpose
Enable natural, efficient interaction with AI systems.

### Key Elements

**Chat Area**
- Message bubbles
- Timestamps
- Read receipts (optional)
- Typing indicators

**Input Area**
- Text input
- Attachment button
- Send button
- Voice input (optional)

**Sidebar**
- Conversation history
- New chat
- Settings

### Design Approach

```css
.chat-layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  height: 100vh;
}

.chat-messages {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding: var(--space-6);
  overflow-y: auto;
}

.chat-message {
  max-width: 70%;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-lg);
}

.chat-message.user {
  align-self: flex-end;
  background: var(--color-primary);
  color: white;
}

.chat-message.assistant {
  align-self: flex-start;
  background: var(--color-surface);
}

.chat-input-container {
  padding: var(--space-4);
  border-top: 1px solid var(--color-border);
}

@media (max-width: 768px) {
  .chat-layout {
    grid-template-columns: 1fr;
  }

  .chat-sidebar {
    position: fixed;
    transform: translateX(-100%);
  }
}
```

---

## Search Page

### Purpose
Help users find specific content quickly and efficiently.

### Key Elements

**Search Bar**
- Prominent input
- Autocomplete suggestions
- Search button

**Filters**
- Categories
- Date range
- Content type
- Advanced filters

**Results**
- Title
- Snippet
- Metadata
- Pagination

### Design Approach

```css
.search-layout {
  max-width: 800px;
  margin: 0 auto;
  padding: var(--space-8);
}

.search-bar {
  display: flex;
  gap: var(--space-2);
  margin-bottom: var(--space-6);
}

.search-input {
  flex: 1;
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-lg);
}

.search-filters {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
  margin-bottom: var(--space-6);
}

.search-results {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.search-result {
  padding: var(--space-4);
  border-radius: var(--radius-md);
}

.search-result:hover {
  background: var(--color-bg-muted);
}
```

---

## Common Patterns Across Pages

### Header/Navigation

```css
.header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  padding: var(--space-3) var(--space-4);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: var(--width-full);
  margin: 0 auto;
}
```

### Footer

```css
.footer {
  background: var(--color-bg-muted);
  padding: var(--space-12) var(--space-4);
  margin-top: auto;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-8);
  max-width: var(--width-full);
  margin: 0 auto;
}
```

---

## Page-Specific Checklist

### Landing Page
- [ ] Clear value proposition
- [ ] Strong visual hierarchy
- [ ] Obvious CTA
- [ ] Social proof
- [ ] Mobile optimized

### Dashboard
- [ ] Efficient navigation
- [ ] Key metrics visible
- [ ] Data visualization clear
- [ ] Actions accessible
- [ ] Responsive layout

### Authentication
- [ ] Minimal friction
- [ ] Clear error messages
- [ ] Social login options
- [ ] Remember me
- [ ] Password reset

### Documentation
- [ ] Search functional
- [ ] Navigation clear
- [ ] Code examples work
- [ ] Responsive
- [ ] Version selector

---

Different pages serve different purposes. Design for the specific context and user goals.
