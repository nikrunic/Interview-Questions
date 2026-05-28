# Web Performance Optimization Interview Questions

This document contains interview questions focused on modern web performance optimization, Core Web Vitals, code splitting, and lazy loading.

## Basic Questions

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

---

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

---

## Intermediate Questions

---

## Intermediate Questions

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

## Additional Depth (Architectural Focus)


---

---

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

---

## Expert Questions

## Practice Questions

---

## Expert Questions

### 1. Write an image lazy-loading script utilizing the dynamic browser IntersectionObserver.

**Example Solution:**
```javascript
function lazyLoadImages() {
  const images = document.querySelectorAll("img[data-src]");
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute("data-src");
        obs.unobserve(img);
      }
    });
  });

  images.forEach(img => observer.observe(img));
}
```

---

### 2. Dynamically import a heavy external library on user interaction to improve Largest Contentful Paint (LCP).

**Example Solution:**
```javascript
const button = document.getElementById("chart-btn");

button.addEventListener("click", async () => {
  // Dynamically load library
  const { default: Chart } = await import("chart.js/auto");
  
  const ctx = document.getElementById("myChart");
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue'],
      datasets: [{ data: [12, 19] }]
    }
  });
});
```

---

## Practice Questions

### 1. Write an image lazy-loading script utilizing the dynamic browser IntersectionObserver.

**Example Solution:**
```javascript
function lazyLoadImages() {
  const images = document.querySelectorAll("img[data-src]");
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute("data-src");
        obs.unobserve(img);
      }
    });
  });

  images.forEach(img => observer.observe(img));
}
```

### 2. Dynamically import a heavy external library on user interaction to improve Largest Contentful Paint (LCP).

**Example Solution:**
```javascript
const button = document.getElementById("chart-btn");

button.addEventListener("click", async () => {
  const { default: Chart } = await import("chart.js/auto");
  
  const ctx = document.getElementById("myChart");
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue'],
      datasets: [{ data: [12, 19] }]
    }
  });
});
```

### 3. Implement standard client resource prefetching for future dynamic navigations.

**Example Solution:**
```javascript
function prefetchUrl(url) {
  const link = document.createElement("link");
  link.rel = "prefetch";
  link.href = url;
  document.head.appendChild(link);
}
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Web Performance Tuning application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Web Performance Tuning operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Web Performance Tuning configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Web Performance Tuning event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Web Performance Tuning with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Web Performance Tuning performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Web Performance Tuning failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Web Performance Tuning data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Web Performance Tuning state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Web Performance Tuning logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Web Performance Tuning files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Web Performance Tuning connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Web Performance Tuning.

*(Challenge question for self-study and practical project implementation.)*

