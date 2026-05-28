# Accessibility (a11y) Interview Questions

This document contains interview questions focused on web accessibility standards, ARIA, and building inclusive user interfaces.

## Basic Questions

### 1. What is Web Accessibility (a11y)?
**Answer:** 
**The Core Concept:**
Web accessibility means designing and developing websites, tools, and technologies so that people with disabilities can use them.

**Key Details:**
- It ensures equal access and opportunity for people with auditory, cognitive, neurological, physical, speech, and visual disabilities.
- The numeronym "a11y" stands for "a", then 11 letters, then "y".

**Example:** Using semantic HTML and providing text alternatives for non-text content.

**Reference:** [W3C Accessibility Introduction](https://www.w3.org/WAI/fundamentals/accessibility-intro/)

---

---

---

### 2. What are WCAG guidelines?
**Answer:** 
**The Core Concept:**
The Web Content Accessibility Guidelines (WCAG) are a set of recommendations for making web content more accessible.

**Key Details:**
- They are organized around four core principles: Perceivable, Operable, Understandable, and Robust (POUR).
- Compliance is typically measured in three levels: A, AA, and AAA.

**Example:** Ensuring a contrast ratio of at least 4.5:1 for normal text meets WCAG AA standards.

**Reference:** [WCAG Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)

---

---

## Intermediate Questions

---

## Intermediate Questions

### 3. What is ARIA?
**Answer:** 
**The Core Concept:**
WAI-ARIA (Accessible Rich Internet Applications) is a specification that provides additional semantics to HTML.

**Key Details:**
- It is used to improve accessibility for dynamic content and advanced UI controls developed with JavaScript.
- You should only use ARIA when native HTML semantics are missing or fall short.

**Example:** `aria-expanded="true"` on a custom dropdown button to inform screen readers of its state.

**Reference:** [MDN ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)

---

## Additional Depth (Architectural Focus)


---

---

### 4. How do you handle focus management in Single Page Applications (SPAs)?
**Answer:** 
**The Core Concept:**
In SPAs, client-side routing does not trigger a full page reload, meaning screen readers are not inherently alerted to page changes. Focus management involves programmatically shifting the browser's focus to the new content or a relevant heading so that assistive technologies can read the updated context.

**Key Details:**
- You should manage focus using JavaScript's `.focus()` method on a `tabindex="-1"` element after a route change.
- Avoid trapping focus within a component unless it is a modal dialogue, ensuring keyboard navigation remains intuitive.

**Example:** 
`useEffect(() => { headingRef.current?.focus(); }, [pathname]);`

**Reference:** [Documentation](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

---

---

## Expert Questions

## Practice Questions

---

## Expert Questions

### 1. Write an accessible Modal dialog with focus trap using Vanilla JavaScript.

**Example Solution:**
```javascript
function initModal(modalId, triggerId, closeId) {
  const modal = document.getElementById(modalId);
  const trigger = document.getElementById(triggerId);
  const close = document.getElementById(closeId);
  
  const focusables = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex="0"]');
  const firstFocusable = focusables[0];
  const lastFocusable = focusables[focusables.length - 1];

  trigger.addEventListener("click", () => {
    modal.setAttribute("aria-hidden", "false");
    modal.style.display = "block";
    firstFocusable.focus();
  });

  const closeModal = () => {
    modal.setAttribute("aria-hidden", "true");
    modal.style.display = "none";
    trigger.focus();
  };

  close.addEventListener("click", closeModal);

  modal.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
    if (e.key === "Tab") {
      if (e.shiftKey) { // Shift + Tab
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else { // Tab
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }
    }
  });
}
```

---

### 2. Implement dynamic screen-reader announcer (aria-live) for custom status notifications.

**Example Solution:**
```html
<div id="announcer" class="sr-only" aria-live="polite" aria-atomic="true"></div>

<script>
  function announceStatus(message) {
    const announcer = document.getElementById("announcer");
    announcer.textContent = ""; // Clear existing
    setTimeout(() => {
      announcer.textContent = message; // Force redraw/read
    }, 100);
  }
</script>

<style>
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
</style>
```

---

## Practice Questions

### 1. Write an accessible Modal dialog with focus trap using Vanilla JavaScript.

**Example Solution:**
```javascript
function initModal(modalId, triggerId, closeId) {
  const modal = document.getElementById(modalId);
  const trigger = document.getElementById(triggerId);
  const close = document.getElementById(closeId);
  
  const focusables = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex="0"]');
  const firstFocusable = focusables[0];
  const lastFocusable = focusables[focusables.length - 1];

  trigger.addEventListener("click", () => {
    modal.setAttribute("aria-hidden", "false");
    modal.style.display = "block";
    firstFocusable.focus();
  });

  const closeModal = () => {
    modal.setAttribute("aria-hidden", "true");
    modal.style.display = "none";
    trigger.focus();
  };

  close.addEventListener("click", closeModal);

  modal.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
    if (e.key === "Tab") {
      if (e.shiftKey) {
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }
    }
  });
}
```

### 2. Implement dynamic screen-reader announcer (aria-live) for custom status notifications.

**Example Solution:**
```html
<div id="announcer" class="sr-only" aria-live="polite" aria-atomic="true"></div>

<script>
  function announceStatus(message) {
    const announcer = document.getElementById("announcer");
    announcer.textContent = ""; 
    setTimeout(() => {
      announcer.textContent = message; 
    }, 100);
  }
</script>

<style>
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
</style>
```

### 3. Create a accessible custom select component using ARIA roles and keyboard interaction.

**Example Solution:**
```html
<div class="custom-select" role="combobox" aria-expanded="false" aria-haspopup="listbox">
  <button id="select-btn" aria-controls="select-list">Select Option</button>
  <ul id="select-list" role="listbox" aria-label="Select Option" style="display: none;">
    <li role="option" tabindex="0" aria-selected="false">Option 1</li>
    <li role="option" tabindex="0" aria-selected="false">Option 2</li>
  </ul>
</div>
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Web Accessibility (a11y) application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Web Accessibility (a11y) operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Web Accessibility (a11y) configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Web Accessibility (a11y) event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Web Accessibility (a11y) with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Web Accessibility (a11y) performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Web Accessibility (a11y) failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Web Accessibility (a11y) data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Web Accessibility (a11y) state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Web Accessibility (a11y) logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Web Accessibility (a11y) files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Web Accessibility (a11y) connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Web Accessibility (a11y).

*(Challenge question for self-study and practical project implementation.)*

