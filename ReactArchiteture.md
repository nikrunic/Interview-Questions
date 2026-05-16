# React Architecture Interview Questions

This document contains a comprehensive list of React Architecture interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What does it mean that React is a "library" and not a "framework"?
**Answer:** A framework dictates the architecture and flow of your application (like Angular). React is just a library focused on the View layer of MVC. Developers must choose their own routers, state management, and build tools to create a full architecture.
**Example:** Using React with React Router and Redux creates a custom framework.
**Reference:** [React - Library vs Framework](https://www.freecodecamp.org/news/is-react-a-library-or-a-framework/)

### 2. What is Container/Presentational Component pattern?
**Answer:** It is a pattern where components are split into two categories: Container components handle the logic, data fetching, and state management. Presentational components simply receive data via props and render UI.
**Example:** `UserListContainer` fetches data; `UserList` maps over props and renders `<li>` tags.
**Reference:** [Dan Abramov - Presentational and Container Components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)

### 3. What is Single-Page Application (SPA) architecture?
**Answer:** An SPA is a web application that interacts with the user by dynamically rewriting the current web page with new data from the web server, instead of the default method of the browser loading entire new pages. React is commonly used to build SPAs.
**Example:** React Router swapping components without a full page reload.
**Reference:** [MDN - SPA](https://developer.mozilla.org/en-US/docs/Glossary/SPA)

### 4. Why should you keep components small and focused?
**Answer:** Small, focused components adhere to the Single Responsibility Principle. They are easier to read, test, maintain, and reuse across the application.
**Example:** Instead of a massive `Page` component, break it into `Header`, `Sidebar`, `Content`, and `Footer`.
**Reference:** [React Docs - Thinking in React](https://react.dev/learn/thinking-in-react)


## Medium (30%)

### 5. What is the Flux architecture?
**Answer:** Flux is an architectural pattern introduced by Facebook for building client-side web applications. It relies on unidirectional data flow. The main components are Actions, Dispatcher, Store, and View.
**Example:** View triggers Action -> Dispatcher sends Action to Store -> Store updates -> View re-renders.
**Reference:** [Facebook - Flux](https://facebook.github.io/flux/)

### 6. How does Redux differ from traditional Flux?
**Answer:** Redux simplifies Flux by having a single centralized Store (Flux has multiple stores). Redux does not use a Dispatcher; instead, it relies on pure functions called Reducers to calculate the next state based on the current state and an Action.
**Example:** `reducer(state, action) => newState`
**Reference:** [Redux Documentation](https://redux.js.org/)

### 7. What is Atomic Design methodology?
**Answer:** Atomic Design is a methodology for creating design systems. It breaks UIs down into 5 distinct levels: Atoms (buttons, inputs), Molecules (search form), Organisms (header), Templates (page layouts without data), and Pages (instances of templates with real data).
**Example:** `<Button>` (Atom) -> `<SearchBar>` (Molecule) -> `<Navbar>` (Organism).
**Reference:** [Brad Frost - Atomic Design](https://bradfrost.com/blog/post/atomic-web-design/)

### 8. Explain Context API vs Redux for state management.
**Answer:** Context API is built-in and great for low-frequency updates like themes, language, or auth state. Redux is better for complex state logic, high-frequency updates, and when you need advanced debugging tools (Redux DevTools) or middleware (Thunk/Saga).
**Example:** Use Context for Dark Mode, use Redux for a complex shopping cart.
**Reference:** [React - Context](https://react.dev/learn/passing-data-deeply-with-context)

### 9. What is a Custom Hook architecture pattern?
**Answer:** This pattern extracts complex stateful logic out of components and into custom functions starting with `use`. It allows logic to be reused across multiple components without changing the component hierarchy (like HOCs do).
**Example:** `const { data, loading, error } = useFetch(url);`
**Reference:** [React - Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)


## Hard (50%)

### 10. Explain Server-Side Rendering (SSR) vs Client-Side Rendering (CSR) with React.
**Answer:** CSR sends an empty HTML shell and a JS bundle to the browser; React renders the UI on the client (poor SEO, slow initial load). SSR renders the React components on the server into an HTML string, sending a fully rendered page to the client. The client then "hydrates" the HTML to attach event listeners.
**Example:** Create React App uses CSR. Next.js uses SSR.
**Reference:** [Next.js Docs - Rendering](https://nextjs.org/docs/basic-features/pages)

### 11. What is Static Site Generation (SSG)?
**Answer:** SSG means generating the HTML for a page at build time rather than on every request (SSR). The pre-rendered HTML is then reused on each request and can be served from a global CDN, making it extremely fast.
**Example:** Next.js `getStaticProps` function.
**Reference:** [Next.js Docs - SSG](https://nextjs.org/docs/basic-features/data-fetching/get-static-props)

### 12. What are Micro-Frontends in React?
**Answer:** Micro-frontends extend the concept of microservices to the frontend world. The application is split into smaller, independent mini-apps (often built by different teams) that are composed together at runtime to appear as a single application.
**Example:** Using Webpack Module Federation to load a React component from one URL into an app hosted on another URL.
**Reference:** [Martin Fowler - Micro Frontends](https://martinfowler.com/articles/micro-frontends.html)

### 13. How do you implement Code Splitting and Lazy Loading?
**Answer:** Code splitting divides the bundle into smaller chunks that can be loaded on demand. This is achieved using `React.lazy()` and `Suspense` for components, and dynamic `import()` for standard JavaScript modules. It drastically improves initial load times.
**Example:** `const OtherComponent = React.lazy(() => import('./OtherComponent'));`
**Reference:** [React Docs - Code-Splitting](https://legacy.reactjs.org/docs/code-splitting.html)

### 14. What is React Server Components (RSC)?
**Answer:** RSCs are components that execute exclusively on the server and do not ship their JavaScript to the client. They allow direct access to backend resources (databases) and reduce the client bundle size, while keeping the interactive client components at the leaves of the tree.
**Example:** A `Dashboard` Server Component querying a database directly and passing data as props to a `Chart` Client Component.
**Reference:** [React Blog - Server Components](https://react.dev/blog/2020/12/21/data-fetching-with-react-server-components)

### 15. Describe the Error Boundary architecture.
**Answer:** To prevent a single component crash from breaking the entire SPA, you wrap major sections of your app (routes, sidebars) in Error Boundary components. They catch errors during rendering, lifecycle methods, and constructors, and render a fallback UI.
**Example:** `<ErrorBoundary><MyWidget /></ErrorBoundary>`
**Reference:** [React Docs - Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)

### 16. What is hydration in React?
**Answer:** Hydration is the process of attaching event listeners and React state to the static HTML markup generated by the server (SSR or SSG). React attempts to attach to the existing markup instead of destroying it and re-rendering.
**Example:** `hydrateRoot(document.getElementById('root'), <App />);`
**Reference:** [React Docs - hydrateRoot](https://react.dev/reference/react-dom/client/hydrateRoot)

### 17. How do you handle complex state machines in React?
**Answer:** While `useState` or `useReducer` work for simple states, complex state transitions (like authentication flows or multi-step wizards) are often better modeled using Finite State Machines (FSMs) and libraries like XState to strictly control what states can transition into what other states.
**Example:** Using `@xstate/react`'s `useMachine`.
**Reference:** [XState Documentation](https://xstate.js.org/docs/)

### 18. Explain the compound component pattern.
**Answer:** The compound component pattern allows multiple components to work together and share state behind the scenes, providing a highly flexible and expressive API. It uses React Context to implicitly pass state to child components.
**Example:** ` <Select> <Select.Option value="1">One</Select.Option> </Select> `
**Reference:** [Kent C. Dodds - Compound Components](https://kentcdodds.com/blog/compound-components-with-react-hooks)

### 19. What is the render props pattern?
**Answer:** The render props pattern refers to a technique for sharing code between React components using a prop whose value is a function that returns a React element. It was popular before Hooks for sharing stateful logic.
**Example:** `<DataProvider render={data => <h1>Hello {data.target}</h1>} />`
**Reference:** [React Legacy Docs - Render Props](https://legacy.reactjs.org/docs/render-props.html)

### 20. How do you architect a scalable folder structure in a large React project?
**Answer:** Instead of grouping by file type (e.g., all reducers in one folder, all components in another), group by "Feature" or "Domain". Inside a feature folder, you include its components, hooks, api calls, and state slices. Common utilities and shared UI components live in a global `src/shared` directory.
**Example:** `src/features/authentication/`, `src/features/shopping-cart/`.
**Reference:** [React Folder Structure Best Practices](https://www.taniarascia.com/react-architecture-directory-structure/)
