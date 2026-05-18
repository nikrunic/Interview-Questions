# Content Skills & Formatting Standards

This document outlines the strict formatting guidelines, markdown standards, and pedagogical requirements that all content in this repository must adhere to. AI Agents and contributors must follow these rules without exception.

## 1. The Pedagogical Template

Every single question and answer added to this repository MUST strictly follow this exact markdown template:

```markdown
## [add border to section and space them properly]

### [Question Number]. [Question Title] / [Similar Question Title]

**Answer:**
**The Core Concept:**
[ three or five simple, declarative sentences summarizing what the technology/concept is.]

**Key Details:**

- [Bullet point 1 detailing architectural specifics, memory management, or performance implications.]
- [Bullet point 2 explaining how it works under the hood or its primary tradeoffs.]

**Example:**
[A practical code snippet, configuration example, or real-world use case. Use inline code `like this` or short explanations.]

**Reference:** [Link Text](https://official-documentation-link.com)

---
```

## 2. Difficulty Categorization

When expanding a file to the 100-question threshold, adhere to this general distribution:

- **Basic:** Definitions, fundamental syntax, and core terminology.
- **Medium:** Implementation details, common design patterns, and intermediate problem-solving.
- **Hard:** Deep architecture, Garbage Collection, Execution Plans, Performance Optimization, Concurrency, and advanced paradigms.

## 3. Technology Focus Areas

When generating content, prioritize the following modern paradigms:

- **React:** Focus on Server-first architecture, React Server Components (RSC), Suspense, and the compiler.
- **JavaScript:** ESM, immutable array methods, Promises/Microtasks, and event loop architecture.
- **C# / .NET:** High-performance computing (`Span<T>`, `Memory<T>`), DI Lifetimes, Minimal APIs, and modern C# features (Records, Pattern Matching).
- **Databases (MySQL / MSSQL):** Execution plans, B-Tree index structures, transaction isolation levels, locks, and query optimization.
- **CSS / HTML:** Semantic HTML5, CSS Grid/Flexbox, Container Queries, and accessibility (a11y).

## 4. Markdown Integrity

- Ensure all links in the `Reference` section point to valid, official documentation (e.g., Microsoft Learn, MDN, React Docs).
- Use proper markdown formatting for bolding (`**text**`) and code blocks.
- Maintain continuous sequential numbering (1 through 1000) across the sections within a file.
