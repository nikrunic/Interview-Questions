# Accessibility (a11y) Interview Questions

This document contains interview questions focused on web accessibility standards, ARIA, and building inclusive user interfaces.

## Basic (Easy)

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
\n## Additional Depth (Architectural Focus)\n
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
