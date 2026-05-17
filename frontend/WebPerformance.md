# Web Performance Optimization Interview Questions

This document contains interview questions focused on modern web performance optimization, Core Web Vitals, code splitting, and lazy loading.

## Basic (Easy)

### 1. What are Core Web Vitals?
**Answer:** 
**The Core Concept:**
Core Web Vitals are a set of specific factors that Google considers important in a webpage's overall user experience.

**Key Details:**
- They consist of three main metrics: Largest Contentful Paint (LCP), First Input Delay (FID) / Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS).
- These metrics measure loading performance, interactivity, and visual stability.

**Example:** Using Lighthouse or Google Search Console to measure a page's LCP score.

**Reference:** [Web Vitals](https://web.dev/articles/vitals)

---

### 2. What is Code Splitting?
**Answer:** 
**The Core Concept:**
Code splitting is the practice of splitting a large JavaScript bundle into smaller, more manageable chunks.

**Key Details:**
- It allows you to load only the code required for the initial render, deferring the rest until needed.
- This significantly improves the initial page load time.

**Example:** Using dynamic `import()` in Webpack or React's `React.lazy()`.

**Reference:** [MDN Code Splitting](https://developer.mozilla.org/en-US/docs/Glossary/Code_splitting)

---

### 3. What is Lazy Loading?
**Answer:** 
**The Core Concept:**
Lazy loading is a design pattern that delays the initialization of an object or asset until it's actually needed.

**Key Details:**
- Commonly used for images, videos, and React components to save bandwidth and improve performance.
- Modern browsers support native lazy loading via the `loading="lazy"` attribute on `<img>` tags.

**Example:** `<img src="image.jpg" loading="lazy" alt="..." />`

**Reference:** [Web.dev Lazy Loading](https://web.dev/articles/lazy-loading-images)

---
\n## Additional Depth (Architectural Focus)\n
### 4. What is the critical rendering path and how do you optimize it?
**Answer:** 
**The Core Concept:**
The critical rendering path is the sequence of steps the browser goes through to convert HTML, CSS, and JavaScript into pixels on the screen. Optimizing it is crucial for achieving a fast First Contentful Paint (FCP).

**Key Details:**
- The browser must parse HTML to build the DOM, parse CSS to build the CSSOM, combine them into the Render Tree, calculate layout, and finally paint.
- To optimize it, you must minimize or defer render-blocking resources. This includes loading non-critical CSS asynchronously, deferring JavaScript execution using the `defer` or `async` attributes, and preloading critical web fonts.

**Example:** 
`<script src="app.js" defer></script>`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path)

---
