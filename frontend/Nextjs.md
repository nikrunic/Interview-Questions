# Next.js Interview Questions

This document contains interview questions focused on Next.js, Server-Side Rendering (SSR), and React frameworks.

## Basic Questions

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

---

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

---

## Intermediate Questions

---

## Intermediate Questions

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

## Additional Depth (Architectural Focus)


---

---

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

---

## Expert Questions

---

## Expert Questions

### 5. How would you troubleshoot and resolve a memory leak in a Next.js application deployed via a standalone Docker container?
**Answer:** 
**The Core Concept:**
When deploying Next.js in a long-running environment like a Docker container (using `output: 'standalone'`), features like built-in Image Optimization (`next/image`) can cause progressive memory inflation. Unlike serverless environments (e.g., Vercel) where memory is naturally flushed when the ephemeral instance shuts down, Docker containers persist memory usage over time, requiring explicit limits and architectural adjustments to avoid heap out-of-memory crashes.

**Key Details:**
- **Image Optimization Leaks:** The default Next.js image optimizer processes and caches images on the Node.js server. In certain environments (like Alpine Linux Docker images), garbage collection can fail to release this memory effectively, leading to OOM crashes.
- **Architectural Resolution:** The most robust architectural fix for high-traffic applications is to offload image optimization to a dedicated external CDN (like Cloudinary, AWS CloudFront, or Imgix) by configuring a custom loader, thus bypassing the Node.js server entirely.
- **Build-Time Memory:** Memory leaks can also occur during `npm run build` (e.g., when compiling thousands of MDX pages). This is resolved by explicitly configuring V8 garbage collection limits using `NODE_OPTIONS="--max-old-space-size=4096"` in the CI/CD pipeline or Dockerfile.

**Example:** 
```javascript
// next.config.js - Offloading optimization to avoid Node server memory leaks
module.exports = {
  output: 'standalone',
  images: {
    loader: 'custom',
    loaderFile: './my-custom-image-loader.js',
  },
}
```

**Reference:** [Next.js Custom Image Loader](https://nextjs.org/docs/app/api-reference/next-config-js/images#loader)

---

---

## Practice Questions

---

### 1. Build an dynamic asynchronous App Router page in Next.js.

**Example Solution:**
```typescript
import { Suspense } from "react";

interface Product {
  id: number;
  name: string;
}

async function ProductList() {
  const res = await fetch("https://api.example.com/products", { cache: "no-store" });
  const products: Product[] = await res.json();
  
  return (
    <ul>
      {products.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
  );
}

export default function Page() {
  return (
    <main>
      <h1>Products</h1>
      <Suspense fallback={<p>Loading products...</p>}>
        <ProductList />
      </Suspense>
    </main>
  );
}
```

---

### 2. Implement an App Router API handler utilizing dynamic parameters and route protection.

**Example Solution:**
```typescript
import { NextResponse } from "next/server";

export async function GET(request: Request, { params }: { params: { id: string } }) {
  const authHeader = request.headers.get("authorization");
  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const userId = params.id;
  // Fetch user data...
  return NextResponse.json({ id: userId, name: "John Doe" });
}
```

---

## Practice Questions

### 1. Build an dynamic asynchronous App Router page in Next.js.

**Example Solution:**
```typescript
import { Suspense } from "react";

interface Product {
  id: number;
  name: string;
}

async function ProductList() {
  const res = await fetch("https://api.example.com/products", { cache: "no-store" });
  const products: Product[] = await res.json();
  
  return (
    <ul>
      {products.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
  );
}

export default function Page() {
  return (
    <main>
      <h1>Products</h1>
      <Suspense fallback={<p>Loading products...</p>}>
        <ProductList />
      </Suspense>
    </main>
  );
}
```

### 2. Implement an App Router API handler utilizing dynamic parameters and route protection.

**Example Solution:**
```typescript
import { NextResponse } from "next/server";

export async function GET(request: Request, { params }: { params: { id: string } }) {
  const authHeader = request.headers.get("authorization");
  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const userId = params.id;
  return NextResponse.json({ id: userId, name: "John Doe" });
}
```

### 3. Implement standard middleware in Next.js (App Router) managing redirect rewrites.

**Example Solution:**
```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Next.js Framework application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Next.js Framework operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Next.js Framework configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Next.js Framework event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Next.js Framework with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Next.js Framework performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Next.js Framework failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Next.js Framework data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Next.js Framework state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Next.js Framework logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Next.js Framework files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Next.js Framework connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Next.js Framework.

*(Challenge question for self-study and practical project implementation.)*

