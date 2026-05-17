# Next.js Interview Questions

This document contains interview questions focused on Next.js, Server-Side Rendering (SSR), and React frameworks.

## Basic (Easy)

### 1. What is Next.js?
**Answer:** 
**The Core Concept:**
Next.js is a React framework that provides building blocks to create fast, scalable web applications.

**Key Details:**
- It handles tooling and configuration for React, offering features like SSR, Static Site Generation (SSG), and routing out of the box.
- Maintained by Vercel.

**Example:** `npx create-next-app@latest`

**Reference:** [Next.js Documentation](https://nextjs.org/docs)

---

### 2. What is Server-Side Rendering (SSR)?
**Answer:** 
**The Core Concept:**
SSR is the process of rendering web pages on the server and sending fully populated HTML to the client.

**Key Details:**
- It improves SEO and initial page load performance compared to Client-Side Rendering (CSR).
- In Next.js, this is achieved using `getServerSideProps` or Server Components.

**Example:** `export async function getServerSideProps() { ... }`

**Reference:** [Next.js SSR](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)

---

### 3. What is Static Site Generation (SSG)?
**Answer:** 
**The Core Concept:**
SSG is the process of generating HTML at build time instead of on each request.

**Key Details:**
- The pre-rendered HTML is then reused on each request, making it extremely fast and easily cacheable by CDNs.
- In Next.js, this is done using `getStaticProps`.

**Example:** `export async function getStaticProps() { ... }`

**Reference:** [Next.js SSG](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)

---
\n## Additional Depth (Architectural Focus)\n
### 4. What are React Server Components (RSC) in the Next.js App Router?
**Answer:** 
**The Core Concept:**
React Server Components allow you to write UI that is rendered and optionally cached exclusively on the server. They are the default component type in the Next.js 13+ App Router.

**Key Details:**
- RSCs significantly reduce the client-side JavaScript bundle size because their code is never shipped to the browser; only the resulting HTML/React-tree is sent.
- Unlike traditional Client Components, RSCs cannot use state (`useState`), effects (`useEffect`), or browser APIs, but they can securely access backend resources like databases and secret API keys directly.

**Example:** 
`export default async function Page() { const data = await db.query(); return <div>{data}</div>; }`

**Reference:** [Documentation](https://nextjs.org/docs/app/building-your-application/rendering/server-components)

---
