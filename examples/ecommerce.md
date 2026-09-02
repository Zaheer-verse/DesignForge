# E-commerce Example

Case study: Creating a modern e-commerce product page using DesignForge principles.

---

## Project Brief

**Product:** Lumina — Modern lighting and home decor store

**Target Audience:**
- Design-conscious homeowners
- Age: 28-50
- Higher disposable income
- Aesthetic-focused

**Business Goal:**
- Drive product purchases
- Increase average order value
- Reduce return rate through clear information

**Brand Personality:**
- Elegant and sophisticated
- Modern and minimal
- Premium and curated

---

## Design Discovery

### Page Purpose
Convince visitors to purchase by providing all necessary information, creating desire, and reducing purchase friction.

### Content Hierarchy
1. Product images (visual desire)
2. Product title and price (key info)
3. Add to cart (primary action)
4. Product details (informed decision)
5. Reviews (social proof)
6. Related products (discovery)

### Visual Direction
**Style:** Luxury minimal + Editorial

**Rationale:**
- Luxury minimal: Premium feel, product focus
- Editorial: Curated, design-forward, aspirational

---

## Design System

### Colors
```css
:root {
  /* Brand */
  --color-bg: #FAFAFA;
  --color-surface: #FFFFFF;
  --color-text: #1A1A1A;
  --color-text-muted: #666666;
  
  /* Accent */
  --color-accent: #C4A77D; /* Warm gold */
  
  /* UI */
  --color-border: #E5E5E5;
  --color-success: #22C55E;
  --color-error: #EF4444;
}
```

### Typography
```css
:root {
  --font-display: 'Playfair Display', serif;
  --font-body: 'Inter', sans-serif;
  
  --text-product-title: clamp(1.75rem, 4vw, 2.5rem);
  --text-price: clamp(1.5rem, 3vw, 2rem);
}
```

---

## Page Structure

### 1. Product Hero
```html
<section class="product-hero">
  <div class="product-gallery">
    <div class="gallery-main">
      <button class="gallery-nav prev">
        <ChevronLeftIcon />
      </button>
      <img 
        src="lamp-1.jpg" 
        alt="Arc Floor Lamp in brass finish, shown in modern living room"
        class="gallery-image active"
      />
      <button class="gallery-nav next">
        <ChevronRightIcon />
      </button>
    </div>
    
    <div class="gallery-thumbs">
      <button class="thumb active">
        <img src="lamp-1-thumb.jpg" alt="" />
      </button>
      <button class="thumb">
        <img src="lamp-2-thumb.jpg" alt="" />
      </button>
      <button class="thumb">
        <img src="lamp-3-thumb.jpg" alt="" />
      </button>
      <button class="thumb">
        <img src="lamp-4-thumb.jpg" alt="" />
      </button>
    </div>
    
    <div class="gallery-badges">
      <span class="badge badge-new">New Arrival</span>
      <span class="badge badge-award">
        <AwardIcon />
        Design Award 2026
      </span>
    </div>
  </div>
  
  <div class="product-info">
    <nav class="breadcrumb">
      <a href="#">Home</a>
      <span>/</span>
      <a href="#">Lighting</a>
      <span>/</span>
      <a href="#">Floor Lamps</a>
    </nav>
    
    <div class="product-header">
      <h1>Arc Floor Lamp</h1>
      <div class="product-meta">
        <span class="product-sku">SKU: LUM-ARC-001</span>
        <div class="product-rating">
          <div class="stars">
            <StarIcon filled />
            <StarIcon filled />
            <StarIcon filled />
            <StarIcon filled />
            <StarIcon half />
          </div>
          <span>4.5 (128 reviews)</span>
        </div>
      </div>
    </div>
    
    <div class="product-price">
      <span class="price-current">$489</span>
      <span class="price-original">$599</span>
      <span class="price-savings">Save $110</span>
    </div>
    
    <p class="product-description">
      A sculptural statement piece that combines form and function. 
      The Arc Floor Lamp features a gracefully curved brass arm and 
      handblown glass shade, creating ambient lighting that transforms 
      any space.
    </p>
    
    <div class="product-options">
      <div class="option-group">
        <label>Finish</label>
        <div class="option-buttons">
          <button class="option-btn active">
            <span class="swatch" style="background: #C4A77D"></span>
            Brass
          </button>
          <button class="option-btn">
            <span class="swatch" style="background: #2C2C2C"></span>
            Matte Black
          </button>
          <button class="option-btn">
            <span class="swatch" style="background: #E8E8E8"></span>
            Polished Nickel
          </button>
        </div>
      </div>
      
      <div class="option-group">
        <label>Shade Color</label>
        <div class="option-buttons">
          <button class="option-btn color-only active" title="White">
            <span class="swatch" style="background: #FFFFFF; border: 1px solid #E5E5E5"></span>
          </button>
          <button class="option-btn color-only" title="Smoke">
            <span class="swatch" style="background: #4A4A5A"></span>
          </button>
          <button class="option-btn color-only" title="Amber">
            <span class="swatch" style="background: #D4A76A"></span>
          </button>
        </div>
      </div>
    </div>
    
    <div class="product-actions">
      <div class="quantity-selector">
        <button class="qty-btn minus" aria-label="Decrease quantity">
          <MinusIcon />
        </button>
        <input type="number" value="1" min="1" max="10" aria-label="Quantity" />
        <button class="qty-btn plus" aria-label="Increase quantity">
          <PlusIcon />
        </button>
      </div>
      
      <button class="add-to-cart-btn">
        <ShoppingBagIcon />
        Add to Cart
      </button>
    </div>
    
    <div class="secondary-actions">
      <button class="secondary-btn">
        <HeartIcon />
        Save
      </button>
      <button class="secondary-btn">
        <ShareIcon />
        Share
      </button>
    </div>
    
    <div class="product-highlights">
      <div class="highlight">
        <TruckIcon />
        <span>Free shipping on orders over $200</span>
      </div>
      <div class="highlight">
        <RefreshIcon />
        <span>30-day returns</span>
      </div>
      <div class="highlight">
        <ShieldIcon />
        <span>2-year warranty</span>
      </div>
    </div>
    
    <div class="accordion">
      <details class="accordion-item">
        <summary>
          <span>Details & Dimensions</span>
          <ChevronDownIcon />
        </summary>
        <div class="accordion-content">
          <table class="specs-table">
            <tr>
              <td>Height</td>
              <td>72" (183 cm)</td>
            </tr>
            <tr>
              <td>Base Diameter</td>
              <td>18" (46 cm)</td>
            </tr>
            <tr>
              <td>Shade Diameter</td>
              <td>16" (41 cm)</td>
            </tr>
            <tr>
              <td>Cord Length</td>
              <td>8 ft (244 cm)</td>
            </tr>
            <tr>
              <td>Material</td>
              <td>Brass, Handblown Glass</td>
            </tr>
            <tr>
              <td>Light Source</td>
              <td>E26, Max 100W (not included)</td>
            </tr>
          </table>
        </div>
      </details>
      
      <details class="accordion-item">
        <summary>
          <span>Shipping & Returns</span>
          <ChevronDownIcon />
        </summary>
        <div class="accordion-content">
          <p><strong>Shipping:</strong> Free standard shipping on orders over $200. 
          Ships within 3-5 business days.</p>
          <p><strong>Returns:</strong> Free returns within 30 days of delivery. 
          Item must be in original condition.</p>
        </div>
      </details>
      
      <details class="accordion-item">
        <summary>
          <span>Care Instructions</span>
          <ChevronDownIcon />
        </summary>
        <div class="accordion-content">
          <p>Wipe brass components with a soft, dry cloth. 
          For glass shade, use glass cleaner and lint-free cloth. 
          Avoid abrasive cleaners.</p>
        </div>
      </details>
    </div>
  </div>
</section>
```

---

## Component Patterns

### Product Gallery
```css
.product-hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-8);
  padding: var(--space-8);
}

.gallery-main {
  position: relative;
  aspect-ratio: 1;
  background: var(--color-surface);
  border-radius: var(--radius-lg);
  overflow: hidden;
}

.gallery-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gallery-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: white;
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-md);
  cursor: pointer;
  opacity: 0;
  transition: opacity 200ms;
}

.gallery-main:hover .gallery-nav {
  opacity: 1;
}

.gallery-nav.prev { left: var(--space-4); }
.gallery-nav.next { right: var(--space-4); }

.gallery-thumbs {
  display: flex;
  gap: var(--space-3);
  margin-top: var(--space-4);
}

.thumb {
  width: 80px;
  height: 80px;
  border: 2px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  cursor: pointer;
  padding: 0;
  background: none;
  transition: border-color 200ms;
}

.thumb.active,
.thumb:hover {
  border-color: var(--color-text);
}

.thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 768px) {
  .product-hero {
    grid-template-columns: 1fr;
  }
}
```

### Product Info
```css
.product-info {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.product-header h1 {
  font-family: var(--font-display);
  font-size: var(--text-product-title);
  font-weight: 500;
  letter-spacing: -0.02em;
}

.product-price {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
}

.price-current {
  font-size: var(--text-price);
  font-weight: 600;
}

.price-original {
  font-size: var(--text-lg);
  color: var(--color-text-muted);
  text-decoration: line-through;
}

.price-savings {
  background: var(--color-accent);
  color: white;
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
  font-weight: 500;
}
```

### Add to Cart
```css
.product-actions {
  display: flex;
  gap: var(--space-4);
}

.quantity-selector {
  display: flex;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.qty-btn {
  background: none;
  border: none;
  padding: var(--space-3);
  cursor: pointer;
  transition: background 150ms;
}

.qty-btn:hover {
  background: var(--color-bg);
}

.quantity-selector input {
  width: 48px;
  text-align: center;
  border: none;
  border-left: 1px solid var(--color-border);
  border-right: 1px solid var(--color-border);
  font-size: var(--text-base);
}

.add-to-cart-btn {
  flex: 1;
  background: var(--color-text);
  color: white;
  border: none;
  border-radius: var(--radius-md);
  padding: var(--space-4) var(--space-6);
  font-size: var(--text-base);
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  transition: background 150ms, transform 100ms;
}

.add-to-cart-btn:hover {
  background: #333;
}

.add-to-cart-btn:active {
  transform: scale(0.98);
}
```

---

## Reviews Section

```html
<section class="product-reviews">
  <div class="reviews-header">
    <h2>Customer Reviews</h2>
    <div class="reviews-summary">
      <div class="overall-rating">
        <span class="rating-number">4.5</span>
        <div class="stars">
          <StarIcon filled />
          <StarIcon filled />
          <StarIcon filled />
          <StarIcon filled />
          <StarIcon half />
        </div>
        <span class="total-reviews">Based on 128 reviews</span>
      </div>
      
      <div class="rating-breakdown">
        <div class="rating-bar">
          <span>5</span>
          <div class="bar">
            <div class="bar-fill" style="width: 72%"></div>
          </div>
          <span>72%</span>
        </div>
        <div class="rating-bar">
          <span>4</span>
          <div class="bar">
            <div class="bar-fill" style="width: 18%"></div>
          </div>
          <span>18%</span>
        </div>
        <div class="rating-bar">
          <span>3</span>
          <div class="bar">
            <div class="bar-fill" style="width: 6%"></div>
          </div>
          <span>6%</span>
        </div>
        <div class="rating-bar">
          <span>2</span>
          <div class="bar">
            <div class="bar-fill" style="width: 3%"></div>
          </div>
          <span>3%</span>
        </div>
        <div class="rating-bar">
          <span>1</span>
          <div class="bar">
            <div class="bar-fill" style="width: 1%"></div>
          </div>
          <span>1%</span>
        </div>
      </div>
      
      <button class="write-review-btn">
        Write a Review
      </button>
    </div>
  </div>
  
  <div class="reviews-list">
    <div class="review">
      <div class="review-header">
        <div class="reviewer">
          <img src="avatar1.jpg" alt="" />
          <div>
            <span class="reviewer-name">Sarah M.</span>
            <span class="verified-badge">
              <CheckIcon />
              Verified Purchase
            </span>
          </div>
        </div>
        <div class="review-meta">
          <div class="stars">
            <StarIcon filled />
            <StarIcon filled />
            <StarIcon filled />
            <StarIcon filled />
            <StarIcon filled />
          </div>
          <span class="review-date">2 weeks ago</span>
        </div>
      </div>
      <h4 class="review-title">Stunning addition to our living room</h4>
      <p class="review-text">
        This lamp exceeded my expectations. The quality is exceptional, 
        and it's become a real conversation piece. The brass finish is 
        more beautiful in person—photos don't do it justice. Assembly 
        was straightforward, and the light it casts creates such a warm 
        ambiance.
      </p>
      <div class="review-images">
        <img src="review-img1.jpg" alt="Customer photo of lamp in living room" />
        <img src="review-img2.jpg" alt="Customer photo showing lamp detail" />
      </div>
      <div class="review-footer">
        <button class="helpful-btn">
          <ThumbsUpIcon />
          Helpful (12)
        </button>
      </div>
    </div>
    
    <!-- More reviews... -->
  </div>
  
  <button class="load-more-btn">
    Load More Reviews
  </button>
</section>
```

---

## Related Products

```html
<section class="related-products">
  <h2>You May Also Like</h2>
  
  <div class="products-grid">
    <a href="#" class="product-card">
      <div class="card-image">
        <img src="related-1.jpg" alt="Pendant Light" />
        <button class="quick-add">
          <PlusIcon />
        </button>
      </div>
      <div class="card-info">
        <h3>Pendant Light</h3>
        <span class="card-price">$289</span>
      </div>
    </a>
    
    <a href="#" class="product-card">
      <div class="card-image">
        <img src="related-2.jpg" alt="Table Lamp" />
        <button class="quick-add">
          <PlusIcon />
        </button>
      </div>
      <div class="card-info">
        <h3>Table Lamp</h3>
        <span class="card-price">$189</span>
      </div>
    </a>
    
    <a href="#" class="product-card">
      <div class="card-image">
        <img src="related-3.jpg" alt="Wall Sconce" />
        <button class="quick-add">
          <PlusIcon />
        </button>
      </div>
      <div class="card-info">
        <h3>Wall Sconce</h3>
        <span class="card-price">$149</span>
      </div>
    </a>
    
    <a href="#" class="product-card">
      <div class="card-image">
        <img src="related-4.jpg" alt="Chandelier" />
        <button class="quick-add">
          <PlusIcon />
        </button>
      </div>
      <div class="card-info">
        <h3>Chandelier</h3>
        <span class="card-price">$789</span>
      </div>
    </a>
  </div>
</section>
```

---

## Responsive Behavior

### Mobile (< 768px)
- Single column layout
- Gallery as slider
- Sticky add-to-cart bar at bottom
- Accordion for details
- Simplified reviews

### Tablet/Desktop
- Side-by-side layout
- Gallery with thumbnails
- Full details visible
- Complete reviews

---

## Accessibility

- All images have descriptive alt text
- Color swatches have labels
- Focus states visible
- Keyboard navigable gallery
- Screen reader announcements for cart updates
- Reduced motion respected

---

This e-commerce example demonstrates product-focused design with clear information hierarchy, trust signals, and friction-reducing patterns.
