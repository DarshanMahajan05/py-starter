# PRD — Premium AI SaaS Landing Page
**Version:** 1.0.0  
**Status:** Approved for Development  
**Last Updated:** 2026-06-26  
**Owner:** Hackathon Team  
**Stack:** Next.js · React · TypeScript · Tailwind CSS

---

## Table of Contents

1. [Product Overview](#1-product-overview)
2. [Goals](#2-goals)
3. [Target Audience](#3-target-audience)
4. [User Journey](#4-user-journey)
5. [Information Architecture](#5-information-architecture)
6. [Complete Page Structure](#6-complete-page-structure)
7. [Component Hierarchy](#7-component-hierarchy)
8. [Folder Structure](#8-folder-structure)
9. [State Management Strategy](#9-state-management-strategy)
10. [Pricing Engine Architecture](#10-pricing-engine-architecture)
11. [Responsive Strategy](#11-responsive-strategy)
12. [Motion Specifications](#12-motion-specifications)
13. [Performance Strategy](#13-performance-strategy)
14. [SEO Checklist](#14-seo-checklist)
15. [Accessibility Checklist](#15-accessibility-checklist)
16. [Technical Constraints](#16-technical-constraints)
17. [Acceptance Criteria](#17-acceptance-criteria)
18. [Future Scalability Notes](#18-future-scalability-notes)

---

## 1. Product Overview

### 1.1 Summary

A premium, production-ready AI SaaS marketing landing page designed to convert visitors into paying customers. The page communicates product value through polished UI, contextual animations, and a transparent pricing model. The design language draws from best-in-class SaaS products — Vercel, Linear, Notion AI, and OpenAI — emphasising clarity, whitespace, and typographic precision.

### 1.2 Design Pillars

| Pillar | Description |
|---|---|
| **Premium Feel** | Design quality on par with Vercel / Linear. Every pixel is intentional. |
| **Performance First** | Minimal JS, fast TTI, no external animation libraries. |
| **Accessible by Default** | WCAG 2.1 AA compliance is non-negotiable, not an afterthought. |
| **Developer Ergonomics** | Clean component architecture, typed props, isolated state, zero prop-drilling. |
| **Internationalised Pricing** | Multi-currency, multi-cycle pricing with no hardcoded values. |

### 1.3 Brand Voice

Confident, precise, and human. Avoid superlatives. Lead with outcomes, not features.

### 1.4 Asset Inventory

| Asset | Format | Usage |
|---|---|---|
| Color palette | CSS custom properties | Global design tokens |
| SVG illustrations | Inline SVG / `<Image>` | Feature section, hero decoration |
| Inter | Google Fonts / local | Body, UI copy |
| JetBrains Mono | Google Fonts / local | Code snippets, pricing numbers |
| Demo video | `.mp4` / `.webm` | Hero or feature showcase |

---

## 2. Goals

### 2.1 Business Goals

- Drive sign-up / trial conversions from organic and paid traffic.
- Communicate pricing transparency to reduce sales friction.
- Establish brand authority through design quality.
- Support multi-region audiences (USD, INR, EUR).

### 2.2 Product Goals

- Ship a fully functional, production-ready page within hackathon deadline.
- Achieve Lighthouse score ≥ 95 across all four categories.
- Zero dependency on external UI or animation libraries.
- Full keyboard navigability and screen-reader compatibility.

### 2.3 Success Metrics

| Metric | Target |
|---|---|
| Lighthouse Performance | ≥ 95 |
| Lighthouse Accessibility | ≥ 95 |
| Lighthouse SEO | ≥ 95 |
| Lighthouse Best Practices | ≥ 95 |
| First Contentful Paint (FCP) | < 1.2 s |
| Time to Interactive (TTI) | < 2.5 s |
| Cumulative Layout Shift (CLS) | < 0.05 |
| Largest Contentful Paint (LCP) | < 2.0 s |

---

## 3. Target Audience

### 3.1 Primary Persona — Developer / Technical Founder

| Attribute | Detail |
|---|---|
| **Role** | Software engineer, indie hacker, startup CTO |
| **Goal** | Evaluate whether the AI product fits their workflow and team size |
| **Pain Point** | Hidden pricing, complex onboarding, unreliable uptime |
| **Behaviour** | Scrolls fast, reads feature copy, jumps to pricing immediately |
| **Device** | Desktop-first, occasionally mobile |

### 3.2 Secondary Persona — Product / Growth Manager

| Attribute | Detail |
|---|---|
| **Role** | Head of Product, Growth Lead |
| **Goal** | Assess ROI and share pricing with finance for approval |
| **Pain Point** | Ambiguous value props, no annual discount transparency |
| **Behaviour** | Reads testimonials, checks the pricing tier matrix carefully |
| **Device** | Split desktop / mobile |

### 3.3 Tertiary Persona — Enterprise Evaluator

| Attribute | Detail |
|---|---|
| **Role** | Procurement, VP Engineering |
| **Goal** | Understand enterprise-tier limits and compliance posture |
| **Pain Point** | No clear upgrade path, unclear data handling |
| **Behaviour** | Scans for security badges, looks for a "Contact Sales" CTA |
| **Device** | Desktop |

---

## 4. User Journey

```
[Enter via ad / organic / direct]
        │
        ▼
[Hero Section]
  - Reads headline + sub-headline
  - Watches demo video or hero animation
  - Clicks primary CTA → [Sign-up / Trial] (conversion event)
        │ (continues scrolling)
        ▼
[Feature Showcase — Bento Grid / Accordion]
  - Expands feature cards to understand capabilities
  - Desktop: clicks Bento card to open detail
  - Mobile: taps Accordion panel
        │
        ▼
[Pricing Section]
  - Toggles monthly ↔ annual (sees 20% discount badge)
  - Switches currency (INR / USD / EUR)
  - Selects plan → CTA triggers sign-up modal or route
        │
        ▼
[Testimonials / Social Proof]
  - Reads 3–6 customer quotes
  - Views company logos or avatars
        │
        ▼
[Final CTA Banner]
  - Reinforces headline value prop
  - Prominent primary button
        │
        ▼
[Footer]
  - Navigates to docs, blog, legal, social links
```

---

## 5. Information Architecture

```
Landing Page (/)
├── <Header>          — Logo · Nav links · Theme toggle · CTA button
├── <HeroSection>     — H1 · Subheading · CTAs · Demo video / animation
├── <FeatureSection>  — Bento Grid (desktop) / Accordion (mobile)
├── <PricingSection>  — Currency selector · Billing toggle · Plan cards
├── <Testimonials>    — Quote cards · Logos / avatars
├── <CTABanner>       — Final conversion push
└── <Footer>          — Links · Legal · Social · Theme
```

### 5.1 Navigation Links

| Label | Anchor |
|---|---|
| Features | `#features` |
| Pricing | `#pricing` |
| Testimonials | `#testimonials` |
| Docs | `/docs` (external) |
| Sign In | `/login` |
| Get Started | `/signup` (primary CTA) |

---

## 6. Complete Page Structure

### 6.1 Header / Navigation

- **Behaviour:** Sticky on scroll; applies backdrop-blur + subtle border after 80 px scroll threshold.
- **Logo:** SVG inline, links to `/`.
- **Nav:** Horizontal links (desktop); collapsible hamburger menu (mobile, CSS-only drawer via `<details>`/`<summary>` or checkbox hack — no JS required).
- **CTA:** `Get Started` button, filled, in brand accent colour.
- **Theme:** Optional light/dark toggle (persisted via `localStorage`, respects `prefers-color-scheme`).

---

### 6.2 Hero Section

| Element | Spec |
|---|---|
| **Eyebrow tag** | Small caps label (e.g., "Now in public beta") with animated gradient border |
| **H1 Headline** | 56–72 px, Inter ExtraBold, max 2 lines |
| **Sub-headline** | 18–20 px, Inter Regular, max 3 lines, muted colour |
| **Primary CTA** | Filled button — "Get Started Free" |
| **Secondary CTA** | Ghost/outline button — "View Demo" |
| **Demo video** | Autoplay, muted, loop, `preload="none"`, `<video>` element with `poster` attribute |
| **Background** | Subtle radial gradient + SVG noise texture via CSS |
| **Decoration** | SVG illustration(s) absolutely positioned; animate via CSS `@keyframes` |

**Implementation Note:** The H1 must be the only `<h1>` on the page. All other section headings use `<h2>`.

---

### 6.3 Feature Showcase (Bento Grid ↔ Accordion)

This is the most technically complex section. Full specs in [Section 11 (Responsive Strategy)](#11-responsive-strategy) and [Section 12 (Motion Specifications)](#12-motion-specifications).

| Element | Spec |
|---|---|
| **Desktop layout** | CSS Grid, `grid-template-areas`, asymmetric Bento layout |
| **Mobile layout** | Vertical Accordion, CSS `max-height` transition |
| **Active state sync** | Active Bento card index stored in `useFeatureState` custom hook; on viewport change, Accordion reads same index |
| **Cards** | 5–7 feature tiles; each has icon (inline SVG), title (`<h3>`), description, optional mini-demo |
| **No JS animations** | CSS `transition` and `@keyframes` only |

---

### 6.4 Pricing Section

Full engine specs in [Section 10 (Pricing Engine Architecture)](#10-pricing-engine-architecture).

| Element | Spec |
|---|---|
| **Section heading** | `<h2>` — "Simple, Transparent Pricing" |
| **Billing toggle** | Monthly / Annual switch (custom CSS toggle, `role="switch"`, `aria-checked`) |
| **Currency selector** | `<select>` or custom listbox — INR / USD / EUR |
| **Plan cards** | 3 tiers: Starter · Pro · Enterprise |
| **Annual badge** | "Save 20%" badge, appears only when annual billing is active |
| **Price display** | JetBrains Mono, large, animated number transition via CSS |
| **Feature list** | Per-tier feature checklist with checkmark SVG icons |
| **CTA per card** | "Get Started", "Start Pro Trial", "Contact Sales" |
| **Popular badge** | "Most Popular" label on Pro plan |

---

### 6.5 Testimonials / Social Proof

| Element | Spec |
|---|---|
| **Section heading** | `<h2>` — "Trusted by teams worldwide" |
| **Logo strip** | 6–8 company logos (SVGs), grayscale, hover reveals colour |
| **Quote cards** | 3–6 cards in a 3-column grid (desktop) / 1-column (mobile) |
| **Quote anatomy** | Avatar image · Name · Title/Company · Star rating (SVG) · Quote text |
| **Avatar images** | `<img>` with explicit `width`, `height`, `alt` (person's name) |

---

### 6.6 CTA Banner

| Element | Spec |
|---|---|
| **Background** | Brand gradient or dark panel |
| **Heading** | `<h2>` — reinforcing hero value prop |
| **Sub-copy** | 1–2 sentences |
| **Button** | "Get Started Free" — same style as hero primary CTA |
| **Trust signal** | "No credit card required · Cancel anytime" |

---

### 6.7 Footer

| Element | Spec |
|---|---|
| **Layout** | 4-column grid (desktop) · 2-column (tablet) · 1-column (mobile) |
| **Columns** | Product · Company · Legal · Social |
| **Logo** | SVG, links to `/` |
| **Copyright** | `<small>` tag, current year via `Date` |
| **Links** | `<nav aria-label="Footer navigation">` |
| **Social icons** | SVG icons, `aria-label` per link |

---

## 7. Component Hierarchy

```
<RootLayout>                        # app/layout.tsx — metadata, fonts, theme
│
├── <Header>
│   ├── <Logo>
│   ├── <NavLinks>
│   ├── <MobileMenuToggle>
│   └── <HeaderCTA>
│
├── <HeroSection>
│   ├── <EyebrowTag>
│   ├── <HeroHeadline>
│   ├── <HeroSubheadline>
│   ├── <HeroCTAs>
│   │   ├── <PrimaryButton>
│   │   └── <SecondaryButton>
│   ├── <DemoVideo>
│   └── <HeroDecoration>            # SVG illustrations, background
│
├── <FeatureSection>
│   ├── <SectionHeader>
│   ├── <BentoGrid>                 # rendered on desktop via CSS
│   │   └── <BentoCard> (×N)
│   └── <FeatureAccordion>          # rendered on mobile via CSS
│       └── <AccordionItem> (×N)
│
├── <PricingSection>
│   ├── <SectionHeader>
│   ├── <PricingControls>
│   │   ├── <BillingToggle>         # uses usePricingStore
│   │   └── <CurrencySelector>      # uses usePricingStore
│   └── <PricingGrid>
│       └── <PricingCard> (×3)
│           ├── <PlanName>
│           ├── <PlanPrice>         # reads from pricingMatrix
│           ├── <FeatureList>
│           └── <PlanCTA>
│
├── <TestimonialsSection>
│   ├── <SectionHeader>
│   ├── <LogoStrip>
│   └── <TestimonialGrid>
│       └── <TestimonialCard> (×N)
│
├── <CTABanner>
│
└── <Footer>
    ├── <FooterLogo>
    ├── <FooterColumns> (×4)
    └── <FooterMeta>
```

---

## 8. Folder Structure

```
/
├── app/
│   ├── layout.tsx                  # RootLayout: metadata, font variables, <html> attrs
│   ├── page.tsx                    # Home page — assembles all sections
│   ├── globals.css                 # CSS custom properties, reset, base styles
│   └── fonts/                      # Self-hosted Inter + JetBrains Mono (woff2)
│
├── components/
│   ├── layout/
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   └── MobileMenu.tsx
│   │
│   ├── sections/
│   │   ├── HeroSection.tsx
│   │   ├── FeatureSection.tsx
│   │   ├── PricingSection.tsx
│   │   ├── TestimonialsSection.tsx
│   │   └── CTABanner.tsx
│   │
│   ├── features/                   # Sub-components for FeatureSection
│   │   ├── BentoGrid.tsx
│   │   ├── BentoCard.tsx
│   │   ├── FeatureAccordion.tsx
│   │   └── AccordionItem.tsx
│   │
│   ├── pricing/                    # Sub-components for PricingSection
│   │   ├── BillingToggle.tsx
│   │   ├── CurrencySelector.tsx
│   │   ├── PricingCard.tsx
│   │   └── FeatureList.tsx
│   │
│   ├── testimonials/
│   │   ├── TestimonialCard.tsx
│   │   └── LogoStrip.tsx
│   │
│   └── ui/                         # Primitive UI components
│       ├── Button.tsx
│       ├── SectionHeader.tsx
│       ├── Badge.tsx
│       └── Icon.tsx
│
├── hooks/
│   ├── usePricingStore.ts          # Billing cycle + currency state (Context + useReducer)
│   ├── useFeatureState.ts          # Active Bento/Accordion index
│   ├── useMediaQuery.ts            # SSR-safe viewport detection
│   └── useScrolled.ts              # Header scroll threshold detection
│
├── lib/
│   ├── pricingMatrix.ts            # Multidimensional pricing data + formatPrice()
│   ├── features.ts                 # Feature card data
│   ├── testimonials.ts             # Testimonial copy + avatar paths
│   └── metadata.ts                 # SEO metadata constants
│
├── public/
│   ├── images/
│   │   ├── og-image.png            # 1200×630 Open Graph image
│   │   ├── avatars/                # Testimonial avatars
│   │   └── logos/                  # Company logos (SVG)
│   ├── videos/
│   │   ├── demo.mp4
│   │   └── demo.webm
│   └── svgs/                       # Decorative SVG illustrations
│
├── styles/
│   └── animations.css              # Named @keyframes, shared CSS animation classes
│
├── types/
│   ├── pricing.ts                  # PricingTier, Currency, BillingCycle types
│   └── features.ts                 # FeatureCard type
│
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

---

## 9. State Management Strategy

### 9.1 Principles

- **No Redux. No Zustand. No Jotai.** State is co-located or lifted minimally.
- **Context only where isolation is required** (Pricing, Feature active state).
- **Derived state** is computed at render from props/context — no redundant `useState` copies.
- **Server Components** wherever possible (Next.js App Router). Client components are marked `'use client'` and are leaf nodes.

### 9.2 State Map

| State | Owner | Scope | Strategy |
|---|---|---|---|
| `billingCycle` | `PricingContext` | Pricing section only | `useReducer` inside Context |
| `currency` | `PricingContext` | Pricing section only | `useReducer` inside Context |
| `activeFeatureIndex` | `FeatureContext` | Feature section only | `useState` inside Context |
| `isScrolled` | `Header` | Header only | `useState` + `useScrolled` hook |
| `isMobileMenuOpen` | `Header` | Header only | `useState` |
| Theme (`dark`/`light`) | `<html>` class | Global | `localStorage` + `prefers-color-scheme` via inline script in `<head>` (no flash) |

### 9.3 PricingContext — Isolation Guarantee

`PricingSection` wraps only its own subtree with `<PricingProvider>`. Changes to `billingCycle` or `currency` **do not** trigger re-renders in `HeroSection`, `FeatureSection`, `TestimonialsSection`, or `Footer`.

```tsx
// app/page.tsx
export default function Page() {
  return (
    <>
      <HeroSection />           {/* Server Component */}
      <FeatureSection />        {/* Client Component with own Context */}
      <PricingProvider>         {/* Context boundary — only wraps pricing */}
        <PricingSection />
      </PricingProvider>
      <TestimonialsSection />   {/* Server Component */}
      <CTABanner />             {/* Server Component */}
    </>
  );
}
```

### 9.4 FeatureContext — Viewport Sync

`activeFeatureIndex` is a single number. `BentoGrid` and `FeatureAccordion` both read from the same context. `useMediaQuery('(max-width: 768px)')` determines which component is rendered, but the index is preserved — so switching viewport keeps the correct panel open.

```tsx
// hooks/useFeatureState.ts
const FeatureContext = createContext<FeatureContextType>(null!);

export function FeatureProvider({ children }: { children: ReactNode }) {
  const [activeIndex, setActiveIndex] = useState(0);
  return (
    <FeatureContext.Provider value={{ activeIndex, setActiveIndex }}>
      {children}
    </FeatureContext.Provider>
  );
}
```

---

## 10. Pricing Engine Architecture

### 10.1 Pricing Matrix Structure

All prices are stored as a **read-only nested object** — no hardcoded values anywhere in components.

```ts
// lib/pricingMatrix.ts

export type Currency = 'USD' | 'INR' | 'EUR';
export type BillingCycle = 'monthly' | 'annual';
export type PlanId = 'starter' | 'pro' | 'enterprise';

/**
 * Base monthly price in USD cents (avoid floating point errors).
 * Annual = base * 12 * 0.80
 */
const BASE_PRICES_CENTS: Record<PlanId, number> = {
  starter: 900,    // $9.00/mo
  pro:     2900,   // $29.00/mo
  enterprise: 9900 // $99.00/mo
};

/**
 * Exchange rates relative to USD.
 * In production, fetch from an FX API and cache at build time (ISR).
 */
export const EXCHANGE_RATES: Record<Currency, number> = {
  USD: 1,
  INR: 83.5,
  EUR: 0.92,
};

export const CURRENCY_SYMBOLS: Record<Currency, string> = {
  USD: '$',
  INR: '₹',
  EUR: '€',
};

export const CURRENCY_LOCALES: Record<Currency, string> = {
  USD: 'en-US',
  INR: 'en-IN',
  EUR: 'de-DE',
};

/**
 * Primary pricing computation function.
 * Returns formatted price string using Intl.NumberFormat.
 */
export function getPrice(
  plan: PlanId,
  cycle: BillingCycle,
  currency: Currency
): string {
  const baseCents = BASE_PRICES_CENTS[plan];
  const annualMultiplier = cycle === 'annual' ? 0.8 : 1;
  const totalUsdCents = baseCents * annualMultiplier;
  const totalInCurrency = (totalUsdCents / 100) * EXCHANGE_RATES[currency];

  return new Intl.NumberFormat(CURRENCY_LOCALES[currency], {
    style: 'currency',
    currency,
    maximumFractionDigits: currency === 'INR' ? 0 : 2,
  }).format(totalInCurrency);
}
```

### 10.2 Pricing Matrix (Visual Reference)

Approximate rendered values for documentation purposes:

| Plan | USD Monthly | USD Annual/mo | INR Monthly | INR Annual/mo | EUR Monthly | EUR Annual/mo |
|---|---|---|---|---|---|---|
| Starter | $9 | $7.20 | ₹751 | ₹601 | €8.28 | €6.62 |
| Pro | $29 | $23.20 | ₹2,421 | ₹1,937 | €26.68 | €21.34 |
| Enterprise | $99 | $79.20 | ₹8,266 | ₹6,613 | €91.08 | €72.86 |

### 10.3 PricingContext Reducer

```ts
// hooks/usePricingStore.ts

type PricingState = {
  cycle: BillingCycle;
  currency: Currency;
};

type PricingAction =
  | { type: 'SET_CYCLE'; payload: BillingCycle }
  | { type: 'SET_CURRENCY'; payload: Currency };

function pricingReducer(state: PricingState, action: PricingAction): PricingState {
  switch (action.type) {
    case 'SET_CYCLE':    return { ...state, cycle: action.payload };
    case 'SET_CURRENCY': return { ...state, currency: action.payload };
    default: return state;
  }
}
```

### 10.4 PricingCard — Price Consumption

`PricingCard` is a **pure component** that receives `planId` as a prop and reads `{ cycle, currency }` from `PricingContext` using `usePricingStore()`. It calls `getPrice(planId, cycle, currency)` at render. No prop-drilling of prices.

### 10.5 Annual Discount Logic

- Discount = 20% off the monthly price × 12.
- The per-month price shown on annual cycle = `monthly_price * 0.80`.
- Total annual charge = `monthly_price * 0.80 * 12`.
- A "Save X%" badge is computed dynamically: `Math.round((1 - 0.8) * 100)` = `20`.

---

## 11. Responsive Strategy

### 11.1 Breakpoint System (Tailwind)

| Name | Min Width | Target Device |
|---|---|---|
| `sm` | 640 px | Large phone (landscape) |
| `md` | 768 px | Tablet portrait |
| `lg` | 1024 px | Laptop |
| `xl` | 1280 px | Desktop |
| `2xl` | 1536 px | Wide desktop |

### 11.2 Layout Behaviour Per Section

| Section | Mobile (<768 px) | Tablet (768–1023 px) | Desktop (≥1024 px) |
|---|---|---|---|
| Header | Logo + hamburger | Logo + nav (condensed) | Full nav + CTA |
| Hero | Stack vertical, video below text | Side-by-side | Side-by-side, larger type |
| Feature | Accordion (1 column) | Accordion or 2-col grid | Bento Grid |
| Pricing | 1 column stacked | 2-column | 3-column |
| Testimonials | 1 column | 2-column | 3-column |
| Footer | 1 column | 2-column | 4-column |

### 11.3 Bento Grid ↔ Accordion — State Sync Specification

**Problem:** User on desktop opens Bento card #3. They resize to mobile. Card #3's Accordion panel must be open.

**Solution:**

1. `FeatureProvider` wraps the entire `<FeatureSection>`.
2. `activeFeatureIndex` is stored in context.
3. `useMediaQuery('(max-width: 767px)')` is evaluated in `FeatureSection`.
4. If mobile → render `<FeatureAccordion>`, else render `<BentoGrid>`.
5. Both components read `activeFeatureIndex` from context.
6. On mount, `AccordionItem` with `index === activeFeatureIndex` initialises as open.

```tsx
// components/sections/FeatureSection.tsx
'use client';

export default function FeatureSection() {
  const isMobile = useMediaQuery('(max-width: 767px)');

  return (
    <FeatureProvider>
      <section id="features" aria-labelledby="features-heading">
        <SectionHeader id="features-heading" ... />
        {isMobile ? <FeatureAccordion /> : <BentoGrid />}
      </section>
    </FeatureProvider>
  );
}
```

**SSR Consideration:** `useMediaQuery` returns `false` on SSR (defaults to desktop). This is acceptable — the Bento Grid is the default, and hydration will correct to Accordion on mobile before meaningful user interaction.

### 11.4 Bento Grid Layout

```css
/* Mobile-first, overridden at lg breakpoint */
.bento-grid {
  display: grid;
  gap: var(--space-4);
  grid-template-columns: 1fr;
}

@media (min-width: 1024px) {
  .bento-grid {
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: auto;
    grid-template-areas:
      "card1 card1 card2 card2 card3 card3"
      "card4 card4 card4 card5 card5 card5"
      "card6 card6 card7 card7 card7 card7";
  }
}
```

### 11.5 Accordion Behaviour

- Each `AccordionItem` uses `max-height: 0` → `max-height: 600px` CSS transition.
- `overflow: hidden` prevents content bleed during transition.
- `aria-expanded` toggled on the trigger button.
- `aria-controls` links trigger to panel ID.
- Only one panel open at a time (single-expand model).

---

## 12. Motion Specifications

> **Constraint:** No external animation libraries. CSS transitions, CSS animations (`@keyframes`), and the Web Animations API only.

### 12.1 Animation Principles

- **Purpose over decoration.** Every animation communicates state change or guides attention.
- **Respect `prefers-reduced-motion`.** All animations are suppressed or minimised when the media query matches.
- **Duration budget:** Micro-interactions < 200 ms. Entrance animations < 500 ms. No looping animations > 3 s without user pause control.

### 12.2 Animation Inventory

| Component | Trigger | Property | Duration | Easing |
|---|---|---|---|---|
| Header | Scroll past 80 px | `background`, `box-shadow` | 200 ms | `ease-out` |
| Hero decoration SVG | Page load | `opacity`, `transform: translateY` | 600 ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| Eyebrow tag | Page load | `opacity`, `transform: scale` | 400 ms | `ease-out` |
| Bento card | Click / hover | `box-shadow`, `transform: scale` | 150 ms | `ease-out` |
| Bento card (expand) | Click | `max-height`, `opacity` | 300 ms | `ease-in-out` |
| Accordion panel | Toggle | `max-height`, `opacity` | 300 ms | `ease-in-out` |
| Pricing toggle | Click | `transform: translateX` (indicator) | 200 ms | `ease-out` |
| Price number | Cycle / currency change | `opacity` fade out → in | 200 ms | `ease-in-out` |
| Plan card (hover) | Hover | `transform: translateY(-4px)`, `box-shadow` | 200 ms | `ease-out` |
| Logo strip | Continuous | `transform: translateX` (marquee) | 30 s | `linear` (paused on `hover`) |
| Testimonial card | Scroll into view | `opacity`, `transform: translateY` | 400 ms | `ease-out` |
| CTA button | Hover | `transform: scale(1.02)`, glow `box-shadow` | 150 ms | `ease-out` |

### 12.3 Entrance Animations

Use `IntersectionObserver` to add a `.in-view` class when elements enter the viewport, then trigger CSS animations via that class. **No GSAP. No Framer Motion.**

```css
/* styles/animations.css */

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.animate-fadeInUp {
  opacity: 0;
  animation: fadeInUp 0.4s var(--ease-spring) forwards;
}

.animate-fadeInUp.in-view {
  animation-play-state: running;
}

@media (prefers-reduced-motion: reduce) {
  .animate-fadeInUp {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

### 12.4 Hero Background Animation

Subtle animated radial gradient using CSS `@keyframes` on a pseudo-element. GPU-composited (only `opacity` and `transform` are animated).

```css
@keyframes heroGlow {
  0%, 100% { transform: scale(1) translate(0, 0); opacity: 0.6; }
  50%       { transform: scale(1.1) translate(-2%, 2%); opacity: 0.8; }
}

.hero-glow {
  animation: heroGlow 8s ease-in-out infinite;
  will-change: transform, opacity;
}
```

### 12.5 Price Number Transition

When `cycle` or `currency` changes, the price fades out (`opacity: 0`) then fades in with the new value. Implemented via React state + a CSS class toggled with `requestAnimationFrame`.

```tsx
// Key technique: toggle 'updating' class → CSS handles the cross-fade
// 'updating' class sets opacity: 0 with transition
// After transition end, update value, remove 'updating' class
```

---

## 13. Performance Strategy

### 13.1 JavaScript Budget

| Category | Strategy |
|---|---|
| **Minimal client JS** | Prefer Server Components; `'use client'` only on interactive leaves |
| **No animation libraries** | CSS + Web Animations API only |
| **No UI component libraries** | All components hand-written |
| **Bundle splitting** | Dynamic `import()` for below-fold sections if needed |
| **No jQuery / lodash** | Zero utility library dependencies |

### 13.2 Image Optimisation

| Strategy | Implementation |
|---|---|
| Next.js `<Image>` | All `<img>` tags use `next/image` with explicit `width` + `height` |
| Formats | AVIF / WebP with JPEG fallback (Next.js handles automatically) |
| Lazy loading | Below-fold images use `loading="lazy"` (Next.js default) |
| LCP image | Hero image / video poster uses `priority` prop |
| Avatar images | Served from `/public/images/avatars/`, sized at 2× of display size |

### 13.3 Font Strategy

```tsx
// app/layout.tsx — using next/font for zero-CLS font loading
import { Inter, JetBrains_Mono } from 'next/font/google';

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-mono',
  display: 'swap',
});
```

Self-hosted fallback fonts defined with `size-adjust` to eliminate CLS.

### 13.4 CSS Strategy

- **CSS custom properties** for all design tokens (colours, spacing, radius, typography).
- **Tailwind CSS** for utility classes; purged at build — zero unused CSS in production.
- **Critical CSS** inlined by Next.js automatically via `app/` router conventions.
- **`will-change`** applied only to actively animating elements, removed after animation completes.

### 13.5 Video Optimisation

```html
<video
  autoplay
  muted
  loop
  playsinline
  preload="none"
  poster="/images/demo-poster.webp"
  aria-label="Product demonstration"
>
  <source src="/videos/demo.webm" type="video/webm" />
  <source src="/videos/demo.mp4" type="video/mp4" />
</video>
```

- `preload="none"` prevents blocking.
- `poster` avoids layout shift before video loads.
- Both WebM and MP4 sources provided.

### 13.6 Rendering Strategy

| Section | Rendering Mode | Reason |
|---|---|---|
| Hero | Server Component | Static copy, no interaction |
| Feature Bento/Accordion | Client Component | Interactive state required |
| Pricing | Client Component (leaf) | Dynamic prices, toggle interaction |
| Testimonials | Server Component | Static data |
| CTA Banner | Server Component | Static |
| Footer | Server Component | Static links |

---

## 14. SEO Checklist

### 14.1 Metadata (Next.js App Router)

```ts
// lib/metadata.ts
export const siteMetadata = {
  title: 'ProductName — AI-Powered [Value Prop]',
  description: 'Concise, keyword-rich description under 160 characters.',
  url: 'https://yourproduct.com',
  ogImage: '/images/og-image.png',   // 1200×630 px
  twitterHandle: '@yourhandle',
};

// app/layout.tsx
export const metadata: Metadata = {
  title: { default: siteMetadata.title, template: `%s | ProductName` },
  description: siteMetadata.description,
  metadataBase: new URL(siteMetadata.url),
  openGraph: {
    title: siteMetadata.title,
    description: siteMetadata.description,
    url: siteMetadata.url,
    siteName: 'ProductName',
    images: [{ url: siteMetadata.ogImage, width: 1200, height: 630, alt: '...' }],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: siteMetadata.title,
    description: siteMetadata.description,
    creator: siteMetadata.twitterHandle,
    images: [siteMetadata.ogImage],
  },
  robots: { index: true, follow: true },
  canonical: siteMetadata.url,
};
```

### 14.2 SEO Checklist

- [ ] Single `<h1>` per page (Hero headline only)
- [ ] Logical heading hierarchy: H1 → H2 (sections) → H3 (cards) → H4 (sub-items)
- [ ] All `<img>` elements have descriptive, non-empty `alt` attributes
- [ ] Decorative images use `alt=""` and `aria-hidden="true"`
- [ ] Meaningful anchor text — no "click here" or "read more" without context
- [ ] Canonical URL tag set via `metadata.alternates.canonical`
- [ ] `robots.txt` present at `/public/robots.txt`
- [ ] `sitemap.xml` generated (Next.js `app/sitemap.ts`)
- [ ] Open Graph image: 1200×630 px, under 1 MB, text legible at thumbnail size
- [ ] Twitter Card meta tags complete
- [ ] JSON-LD structured data (`WebPage`, `Organization`, `Product`) in `<head>`
- [ ] `<html lang="en">` set
- [ ] Page title under 60 characters
- [ ] Meta description 120–160 characters, includes primary keyword
- [ ] No duplicate content
- [ ] All links crawlable (no `javascript:void(0)` for navigational links)
- [ ] Section IDs match nav anchor links (`#features`, `#pricing`, etc.)

### 14.3 Image Alt Strategy

| Image Type | Alt Strategy |
|---|---|
| Hero illustration | Describe what it depicts, e.g., "Abstract visualisation of AI data flow" |
| Testimonial avatars | Person's full name, e.g., `alt="Sarah Chen, CTO at Acme Inc"` |
| Company logos | Company name + "logo", e.g., `alt="Stripe logo"` |
| Feature icons | Describe function, e.g., `alt="Lightning bolt icon representing fast processing"` |
| Decorative SVGs | `alt=""` + `aria-hidden="true"` |
| Demo video | Provide `aria-label` on `<video>` element; include a transcript link |

---

## 15. Accessibility Checklist

### 15.1 WCAG 2.1 AA Requirements

- [ ] Colour contrast ratio ≥ 4.5:1 for normal text, ≥ 3:1 for large text
- [ ] All interactive elements reachable via `Tab` key
- [ ] Logical focus order matches visual reading order
- [ ] Visible focus indicator on all interactive elements (`outline` never set to `none` without a visible alternative)
- [ ] No keyboard traps
- [ ] `aria-label` or `aria-labelledby` on all icon-only buttons
- [ ] `role="switch"` + `aria-checked` on billing toggle
- [ ] `aria-expanded` on Accordion triggers
- [ ] `aria-controls` linking Accordion trigger to its panel
- [ ] `<nav>` elements have unique `aria-label` values ("Main navigation", "Footer navigation")
- [ ] Skip-to-content link as first focusable element
- [ ] Video has `aria-label`; `muted` + `autoplay` compliant (muted autoplay is allowed)
- [ ] Motion respects `@media (prefers-reduced-motion: reduce)`
- [ ] No content conveyed by colour alone (use icon + colour for status)
- [ ] `<select>` or listbox for currency is keyboard operable
- [ ] Form inputs (if any) have associated `<label>` elements
- [ ] Error messages are programmatically associated with their inputs
- [ ] All SVG icons that convey meaning have `<title>` or `aria-label`; decorative SVGs have `aria-hidden="true"`
- [ ] Page is usable at 200% browser zoom without horizontal scroll
- [ ] Touch targets ≥ 44×44 px on mobile

### 15.2 Screen Reader Behaviour

| Component | Expected Behaviour |
|---|---|
| Billing Toggle | Reads as: "Billing cycle, switch, Monthly, not checked" → "Annual, checked" |
| Accordion trigger | "Feature Name, button, collapsed/expanded" |
| Pricing card | Reads plan name, price with currency and cycle, then feature list items |
| Logo strip (marquee) | `aria-hidden="true"` on the animation; static list provided for SR |
| Testimonial cards | Each card is a `<blockquote>` with `<cite>` for attribution |

---

## 16. Technical Constraints

### 16.1 Hard Constraints

| Constraint | Detail |
|---|---|
| **No external UI libraries** | No shadcn/ui, Radix, MUI, Chakra, Headless UI, etc. |
| **No animation libraries** | No GSAP, Framer Motion, AOS, Lottie |
| **TypeScript strict mode** | `"strict": true` in `tsconfig.json` |
| **No hardcoded prices** | All prices derived from `pricingMatrix.ts` via `getPrice()` |
| **No prop-drilling of pricing state** | Only `usePricingStore()` hook consumed in leaf components |

### 16.2 Approved Dependencies

| Package | Purpose |
|---|---|
| `next` | Framework |
| `react` / `react-dom` | UI library |
| `typescript` | Type safety |
| `tailwindcss` | Utility CSS |
| `autoprefixer` | PostCSS plugin |
| `postcss` | CSS processing |
| `next/font` | Zero-CLS font loading |
| `next/image` | Optimised images |

### 16.3 Browser Support

| Browser | Min Version |
|---|---|
| Chrome / Edge | Last 2 major versions |
| Firefox | Last 2 major versions |
| Safari | 15+ |
| Mobile Safari | iOS 15+ |
| Samsung Internet | Last 2 major versions |

### 16.4 Environment

- Node.js ≥ 20
- Next.js ≥ 14 (App Router)
- Deployed on Vercel (assumed)

---

## 17. Acceptance Criteria

### 17.1 Header

- [ ] Logo visible and links to `/`
- [ ] Nav links scroll smoothly to their anchor sections
- [ ] Header applies backdrop-blur + border after 80 px scroll
- [ ] Mobile hamburger menu opens/closes without JS errors
- [ ] Mobile menu closes when a nav link is tapped
- [ ] "Get Started" CTA is keyboard focusable and activatable
- [ ] Tab order is logical: Logo → Nav links → CTA

### 17.2 Hero Section

- [ ] H1 is the only `<h1>` on the page
- [ ] Primary and secondary CTAs render correctly
- [ ] Demo video autoplays muted, loops, does not block TTI
- [ ] Hero renders correctly on 320 px (smallest mobile) to 2560 px (ultrawide)
- [ ] Entrance animations fire on load; respect `prefers-reduced-motion`
- [ ] All SVG illustrations have `aria-hidden="true"`

### 17.3 Feature Section (Bento / Accordion)

- [ ] On desktop (≥ 1024 px): Bento Grid renders with asymmetric layout
- [ ] On mobile (< 768 px): Accordion renders with all panels closed except the first
- [ ] Clicking a Bento card sets the active index in context
- [ ] Resizing from desktop to mobile with card #3 open: Accordion panel #3 is open
- [ ] Resizing from mobile to desktop with panel #2 open: Bento card #2 is active
- [ ] Accordion panel opens/closes with CSS `max-height` transition — no JS height calc
- [ ] `aria-expanded` toggles correctly on Accordion triggers
- [ ] No animation library is used — verified via bundle analysis
- [ ] Feature cards display icon, title, and description

### 17.4 Pricing Section

- [ ] Billing toggle switches between Monthly and Annual correctly
- [ ] Annual prices are exactly 80% of monthly prices (≤ 0.01 rounding tolerance)
- [ ] "Save 20%" badge is visible only in Annual mode
- [ ] Currency selector changes all three plan prices simultaneously
- [ ] Prices are formatted per locale: USD uses `$`, INR uses `₹` with Indian number formatting, EUR uses `€`
- [ ] Changing currency or cycle does not re-render `<HeroSection>`  (verified via React DevTools Profiler)
- [ ] `BillingToggle` reads as a switch with correct `aria-checked` in screen reader
- [ ] All three plan CTAs are keyboard accessible
- [ ] Price transition animation fires on cycle/currency change and respects `prefers-reduced-motion`
- [ ] No price value is hardcoded in any TSX file

### 17.5 Testimonials

- [ ] Minimum 3 testimonial cards render
- [ ] Each card contains: avatar, name, title, company, quote, and star rating
- [ ] All avatar `<img>` elements have descriptive `alt` text
- [ ] Logo strip renders company logos; pauses marquee on hover/focus
- [ ] Logo strip is `aria-hidden="true"` (decorative)
- [ ] Cards enter viewport with fade animation; respects reduced motion

### 17.6 CTA Banner

- [ ] Heading is an `<h2>`
- [ ] "No credit card required" trust signal is present
- [ ] CTA button is keyboard accessible
- [ ] Section renders correctly in dark and light modes

### 17.7 Footer

- [ ] 4-column layout on desktop, 2-column on tablet, 1-column on mobile
- [ ] All links are crawlable `<a>` elements with meaningful text
- [ ] `<nav aria-label="Footer navigation">` wraps the link columns
- [ ] Social icons have `aria-label` matching the platform name
- [ ] Copyright year is dynamically set

### 17.8 Global / Cross-cutting

- [ ] Lighthouse Performance ≥ 95
- [ ] Lighthouse Accessibility ≥ 95
- [ ] Lighthouse SEO ≥ 95
- [ ] Lighthouse Best Practices ≥ 95
- [ ] Zero console errors in production build
- [ ] TypeScript compiles without errors (`tsc --noEmit`)
- [ ] ESLint passes with zero errors
- [ ] Page renders correctly at 320 px, 768 px, 1024 px, 1440 px, 1920 px
- [ ] Dark mode and light mode both render without colour contrast failures
- [ ] Skip-to-content link present and functional
- [ ] `prefers-reduced-motion` suppresses all CSS animations globally
- [ ] Open Graph image loads correctly when URL is shared on Twitter / LinkedIn / Slack

---

## 18. Future Scalability Notes

### 18.1 Pricing Engine

- **FX rates:** Replace static `EXCHANGE_RATES` with an ISR (Incremental Static Regeneration) fetch from an FX API (e.g., Open Exchange Rates). Cache at build time, revalidate every 6–24 hours.
- **New currencies:** Add entry to `EXCHANGE_RATES`, `CURRENCY_SYMBOLS`, and `CURRENCY_LOCALES` — zero component changes required.
- **New plans:** Add to `BASE_PRICES_CENTS` and the plan data array — zero pricing logic changes.
- **Discount tiers:** Extend `BillingCycle` type and add a `CYCLE_MULTIPLIERS` map to support quarterly billing or promotional discounts.
- **Usage-based pricing:** Extend `getPrice()` to accept a `usage` parameter; the matrix supports additional dimensions.

### 18.2 Feature Section

- **New feature cards:** Add to the `features.ts` data array; the Bento layout will need a `grid-template-areas` update for the new card count.
- **Localisation:** Feature copy is isolated in `lib/features.ts`. Swap the import for an i18n-aware data source (e.g., `next-intl`) with no component changes.

### 18.3 Internationalisation (i18n)

- The component architecture is i18n-ready: all copy is in data files or constants, not scattered across TSX.
- Add `next-intl` or `react-i18next` to the layout without touching section components.
- Pricing already uses `Intl.NumberFormat` — the currency formatting is locale-correct by design.

### 18.4 CMS Integration

- Static data files (`lib/features.ts`, `lib/testimonials.ts`) can be replaced with CMS fetches (Contentful, Sanity, Payload) using Next.js `fetch` in Server Components with no client-side changes.

### 18.5 A/B Testing

- Section components are isolated and stateless where possible. Replace section imports in `page.tsx` with experiment-wrapped variants using a lightweight flag client (e.g., Statsig Edge Config).

### 18.6 Analytics

- Add `window.gtag` or Vercel Analytics calls at CTA click events. Events are already co-located with interaction handlers in `PricingCard` and `HeroCTAs`.

### 18.7 Multi-page Expansion

- The `RootLayout` header/footer are already in `app/layout.tsx`. Adding `/pricing`, `/features`, or `/enterprise` pages requires only creating new route folders — the shell reuses automatically.

---

*End of PRD — v1.0.0*
