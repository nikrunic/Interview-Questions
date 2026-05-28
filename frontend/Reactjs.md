# React.js — Complete Interview Guide

This file combines two React resources into one place:

| Part | Content | Former file |
|------|---------|-------------|
| **1** | Interview preparation (concepts, links, tables) | `React-Interview-Prep.md` |
| **2** | 100 interview Q&A (Basic / Medium / Hard) | `Reactjs.md` |

**Related (kept separate):**

- [React Architecture](./ReactArchiteture.md) — patterns, scaling, structure (100 Q&A)
- [Redux & State Management](./Redux.md) — Redux-specific Q&A

---

## Table of contents

- [Part 1 — Interview preparation](#part-1--interview-preparation)
  - [Core React (1–26)](#core-react-topics)
  - [Redux (27–29)](#redux-topics)
  - [Extended topics (30–46)](#extended-topics)
- [Part 2 — Interview questions (100)](#part-2--interview-questions-100)
- [Part 3 — Core Concepts Cheatsheet (Concise Q&A)](#part-3--core-concepts-cheatsheet-concise-qa)

---

# Part 1 — Interview preparation

Core React, Redux, routing, performance, and related concepts for interviews. Component and API names use official spelling (`StrictMode`, `React.memo`, `useEffect`, `ErrorBoundary`).

---

## Core React topics

## 1. What is React?

**Answer:**

**React** is a JavaScript library for building user interfaces, maintained by Meta. It lets you compose UIs from reusable **components** and efficiently update the DOM when **state** changes.

**Why React:**

- Component-based architecture  
- Declarative UI (describe *what* UI should look like)  
- Virtual DOM for efficient updates  
- Large ecosystem (React Router, Redux, Next.js)

**Reference:** [What and why React (C# Corner)](https://www.c-sharpcorner.com/article/what-and-why-reactjs/)

---

## 2. What is the Virtual DOM?

**Answer:**

The **Virtual DOM** is a lightweight in-memory representation of the real DOM. When state or props change, React:

1. Builds a new virtual tree  
2. **Diffs** it with the previous tree (reconciliation)  
3. Applies only the **minimal changes** to the real DOM  

**The Core Concept:**

Avoids expensive full-page DOM rewrites; batches updates for better performance.

**Reference:**

- [What is Virtual DOM (Stack Overflow)](https://stackoverflow.com/questions/21965738/what-is-virtual-dom)  
- [InterviewBit — React DOM](https://www.interviewbit.com/react-interview-questions/#react-react-dom)

---

## 3. What is JSX?

**Answer:**

**JSX** (JavaScript XML) is syntax extension that lets you write HTML-like markup inside JavaScript. It is **not** understood by browsers directly — it is compiled to `React.createElement()` calls (via **Babel** or similar).

**Example:**

```jsx
const element = <h1 className="title">Hello</h1>;
// Compiles to:
// React.createElement("h1", { className: "title" }, "Hello");
```

**Rules:** `className` instead of `class`, `htmlFor` instead of `for`, single parent or fragments.

**Reference:** [InterviewBit — JSX](https://www.interviewbit.com/react-interview-questions/#react-jsx)

---

## 4. Class components vs functional components

**Answer:**

| | Class component | Functional component |
|---|-----------------|----------------------|
| Syntax | `class extends React.Component` | `function` or arrow + hooks |
| State | `this.state`, `this.setState` | `useState`, `useReducer` |
| Lifecycle | `componentDidMount`, etc. | `useEffect` |
| `this` | Required | Not used |

**Functional component outcomes (your notes):**

- Removes confusing **`this`** binding  
- Lifecycle replaced by **`useEffect`** (mount, update, unmount)  
- Cleaner, composable logic with custom hooks  

**Note:** Class components still work; new code should prefer functions + hooks.

**Reference:** [Choose functional components (Twilio)](https://www.twilio.com/blog/react-choose-functional-components)

---

## 5. Advantages of React

**Answer:**

- **Reusable components** — DRY UI building blocks  
- **Virtual DOM** — efficient updates  
- **One-way data flow** — predictable data direction  
- **Strong ecosystem** — tools, libraries, community  
- **React Native** — mobile with same patterns  
- **SEO options** — with Next.js / SSR  

**Reference:** [InterviewBit — React advantages](https://www.interviewbit.com/react-interview-questions/#react-advantage)

---

## 6. Controlled vs uncontrolled components

**Answer:**

| | Controlled | Uncontrolled |
|---|------------|--------------|
| Value source | **React state** | **DOM** |
| Changes | `onChange` → `setState` | DOM handles input; read via **ref** |
| Validation | Easy in React | Harder |

**Example — controlled:**

```jsx
const [email, setEmail] = useState("");
<input value={email} onChange={(e) => setEmail(e.target.value)} />
```

**Example — uncontrolled:**

```jsx
const inputRef = useRef();
<input ref={inputRef} defaultValue="test" />
// inputRef.current.value
```

**Reference:** [InterviewBit — controlled components](https://www.interviewbit.com/react-interview-questions/#react-controlled-components)

---

## 7. Lifecycle methods in React

**Answer:**

**Class lifecycle (main phases):**

| Phase | Methods |
|-------|---------|
| Mounting | `constructor`, `render`, `componentDidMount` |
| Updating | `render`, `componentDidUpdate` |
| Unmounting | `componentWillUnmount` |

**Deprecated (avoid):** `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` → use `getDerivedStateFromProps` / `getSnapshotBeforeUpdate` or hooks.

**Functional equivalent with `useEffect`:**

```jsx
useEffect(() => {
  // componentDidMount + componentDidUpdate (if deps set)
  return () => {
    // componentWillUnmount — cleanup
  };
}, [dependencies]);
```

**Reference:** [InterviewBit — lifecycle](https://www.interviewbit.com/react-interview-questions/#react-different-lifecycle)

---

## 8. Props vs state

**Answer:**

| | **Props** | **State** |
|---|-----------|-----------|
| Source | Parent → child | Internal to component |
| Mutable by child? | **No** (read-only) | **Yes** (`setState` / `useState`) |
| Purpose | Configuration, data down | UI that changes over time |

**Rule:** Props flow **down**; events/callbacks flow **up**.

**Reference:** [React state vs props (JavaTpoint)](https://www.javatpoint.com/react-state-vs-props)

---

## 9. What is `StrictMode` in React?

**Answer:**

**`<StrictMode>`** is a development-only wrapper that helps find problems early. It does **not** render visible UI.

**What it does:**

- Warns about **legacy APIs** (e.g. unsafe lifecycles)  
- Warns about **deprecated** `findDOMNode`, string refs  
- Detects unexpected **side effects** (double-invoking some functions in dev to surface bugs)  
- Warns about **legacy Context API**  

**Example:**

```jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

**Note:** Spelling is **`StrictMode`**, not “Strict mode component.”

**Reference:** [InterviewBit — Strict Mode](https://www.interviewbit.com/react-interview-questions/#react-strict-mode)

---

## 10. Avoiding unnecessary re-renders (class vs function)

**Answer:**

**Class components:**

- **`React.PureComponent`** — shallow compare props/state before re-render  
- **`shouldComponentUpdate(nextProps, nextState)`** — manual control  

**Function components:**

- **`React.memo(Component)`** — memoizes component; skips re-render if props are shallow-equal  
- **`useMemo`** — cache expensive computed values  
- **`useCallback`** — stable function references for child props  

**Example:**

```jsx
const Child = React.memo(function Child({ name }) {
  return <span>{name}</span>;
});
```

**Caution:** `React.memo` only helps when props are stable; inline objects/functions break memoization unless wrapped with `useCallback` / `useMemo`.

**References:**

- [Avoid unnecessary rendering (DEV)](https://dev.to/spukas/avoid-unnecessary-rendering-for-function-components-in-react-m63)  
- [use React.memo wisely](https://dmitripavlutin.com/use-react-memo-wisely/)

---

## 11. Techniques to optimize React app performance

**Answer:**

- **`React.memo`**, `useMemo`, `useCallback`  
- **Code splitting** — `React.lazy()` + dynamic `import()`  
- **Lazy loading** routes and heavy components  
- **Virtualization** for long lists (`react-window`)  
- **Avoid inline objects/functions** as props when children are memoized  
- **Production build** — minified bundles  
- **Keys** on lists — stable, unique keys  
- **State colocation** — keep state close to where it’s used  

**Reference:** [InterviewBit — React performance](https://www.interviewbit.com/react-interview-questions/#react-performance)

---

## 12. Lazy loading and `React.Suspense`

**Answer:**

**Lazy loading** loads a component **only when needed** (smaller initial bundle).

```jsx
const Dashboard = React.lazy(() => import("./Dashboard"));

function App() {
  return (
    <React.Suspense fallback={<div>Loading...</div>}>
      <Dashboard />
    </React.Suspense>
  );
}
```

**`React.Suspense`** shows **`fallback`** UI while the lazy component’s code is loading.

**References:**

- [Lazy loading in React (LoginRadius)](https://www.loginradius.com/blog/async/lazy-loading-in-react/)  
- [React.Suspense (React docs)](https://react.dev/reference/react/Suspense)

---

## 13. Passing data between React components

**Answer:**

| Direction | Mechanism |
|-----------|-----------|
| Parent → child | **Props** |
| Child → parent | **Callback props** (`onSave`, `onChange`) |
| Deep tree | **Context API**, state management (Redux), composition |
| Sibling | Lift state to **common parent** |

**Example — lifting state:**

```jsx
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <>
      <ChildA count={count} />
      <ChildB onIncrement={() => setCount((c) => c + 1)} />
    </>
  );
}
```

**Reference:** [InterviewBit — pass data](https://www.interviewbit.com/react-interview-questions/#react-pass-data)

---

## 14. Higher-Order Components (HOC)

**Answer:**

A **Higher-Order Component** is a function that takes a component and returns a **new enhanced component** (pattern: `withX(Component)`).

**Use cases:** auth guards, logging, injecting props, theme.

```jsx
function withAuth(WrappedComponent) {
  return function Authenticated(props) {
    if (!props.isLoggedIn) return <Login />;
    return <WrappedComponent {...props} />;
  };
}
```

**Modern alternative:** **custom hooks** (e.g. `useAuth()`) — preferred in new code.

**References:**

- [InterviewBit — HOC](https://www.interviewbit.com/react-interview-questions/#react-hoc)  
- [HOC (Smashing Magazine)](https://www.smashingmagazine.com/2020/06/higher-order-components-react/)

---

## 15. Prop drilling and Context API

**Answer:**

**Prop drilling** is passing props through many intermediate components that do not use them, only to reach a deep child.

**Solution:** **React Context** — provide value at top, consume anywhere below without passing through every level.

```jsx
const ThemeContext = React.createContext("light");

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button className={theme}>Click</button>;
}
```

**References:**

- [InterviewBit — prop drilling](https://www.interviewbit.com/react-interview-questions/#react-prop-drilling)  
- [Avoid prop drilling with Context](https://medium.com/swlh/avoid-prop-drilling-with-react-context-a00392ee3d8)

---

## 16. Error Boundaries in React

**Answer:**

An **Error Boundary** is a class component (or library wrapper) that catches **JavaScript errors in child tree**, logs them, and shows **fallback UI** instead of crashing the whole app.

**Before React 16:** One uncaught error could white-screen the entire app.

**After React 16+:** Error boundaries isolate failures.

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  componentDidCatch(error, info) {
    console.error(error, info);
  }
  render() {
    if (this.state.hasError) return <h1>Something went wrong.</h1>;
    return this.props.children;
  }
}
```

**Important:**

- Catches **render/lifecycle/constructor** errors in children — **runtime errors**  
- Does **not** catch event handlers, async code, or SSR errors (use `try/catch` there)  
- **Hooks** do not have `componentDidCatch` — use `react-error-boundary` package or class boundary  

**References:**

- [Error boundaries (DigitalOcean)](https://www.digitalocean.com/community/tutorials/react-error-boundaries)  
- [use react-error-boundary (Kent C. Dodds)](https://kentcdodds.com/blog/use-react-error-boundary-to-handle-errors-in-react)  
- [Error handling in React hooks](https://medium.com/technofunnel/error-handling-in-react-hooks-e42ab91c48f4)

---

## 17. Change default port 3000 (Create React App)

**Answer:**

**Option 1 — `.env` file (recommended):**

```env
PORT=4000
```

**Option 2 — cross-env (package.json script):**

```json
"start": "set PORT=4000 && react-scripts start"
```

(On Linux/Mac: `PORT=4000 react-scripts start`)

**Reference:** [Changing default port 3000](https://tech.amikelive.com/node-830/reactjs-changing-default-port-3000-in-create-react-app/)

---

## 18. What is Webpack?

**Answer:**

**Webpack** is a **module bundler**. It builds a **dependency graph** from your entry files and outputs optimized bundles for the browser.

**Key features:**

- **Bundling** — combine JS/CSS/assets  
- **Code splitting** — separate chunks loaded on demand  
- **Loaders** — transform files (Babel, CSS, images)  
- **Plugins** — minify, define env vars, etc.  

**In brief:** Webpack analyzes imports, produces minimal files (often `bundle.js`) so the app loads faster. Create React App hides Webpack config; **Vite** is a popular modern alternative.

**References:**

- [Intro to Webpack (freeCodeCamp)](https://www.freecodecamp.org/news/an-intro-to-webpack-what-it-is-and-how-to-use-it-8304ecdc3c60/)  
- [Webpack concepts](https://webpack.js.org/concepts/)

---

## 19. JavaScript vs JSX

**Answer:**

| | `.js` | `.jsx` |
|---|-------|--------|
| Content | Plain JavaScript | JavaScript + JSX markup |
| Browser | Runs after build | Must be **transpiled** first |

JSX is syntactic sugar for `React.createElement`.

**References:**

- [JS vs JSX (Joseph Khan)](https://josephkhan.me/difference-between-js-and-jsx-files-react/)  
- [Stack Overflow — JS vs JSX](https://stackoverflow.com/questions/46169472/reactjs-js-vs-jsx)

---

## 20. Can the browser understand JSX?

**Answer:**

**No.** Browsers execute **JavaScript**, not JSX.

JSX is transformed to JS by a **transpiler** (typically **Babel** with `@babel/preset-react`). The bundled `.js` file is what the browser runs.

---

## 21. React vs Angular

**Answer:**

| | **React** | **Angular** |
|---|-----------|-------------|
| Type | **Library** (UI) | **Full framework** |
| Language | JavaScript / optional TypeScript | TypeScript-first |
| Learning curve | Gentler entry | Steeper (modules, DI, RxJS) |
| Data binding | One-way (+ explicit two-way in forms) | Two-way by default |
| DOM | Virtual DOM | Real DOM + change detection |

**Interview line:** React gives flexibility; Angular gives more structure out of the box.

**References:**

- [Angular vs React (Cleveroad)](https://www.cleveroad.com/blog/angular-vs-react)  
- [Angular vs React (freeCodeCamp)](https://www.freecodecamp.org/news/angular-vs-react-what-to-choose-for-your-app-2/)

---

## 22. `Switch` vs `exact` (React Router v5)

**Answer:**

Used in **React Router v5** (v6 uses `<Routes>` instead of `<Switch>`).

| | **`exact`** | **`Switch>`** |
|---|-------------|----------------|
| Role | Path must match **exactly** (no partial match) | Renders **first** matching `<Route>` only |
| Order | N/A | **Order matters** — first match wins |

```jsx
<Switch>
  <Route exact path="/" component={Home} />
  <Route path="/users" component={Users} />
</Switch>
```

Without `exact` on `/`, `/users` might also match `/` prefix depending on config.

**Reference:** [React Router (GeeksforGeeks)](https://www.geeksforgeeks.org/reactjs-router/)

**Note:** React Router **v6** — use `<Routes>` and relative paths; `exact` is default behavior.

---

## 23. Does the browser understand JavaScript?

**Answer:**

**Yes.** All modern browsers include a **JavaScript engine** (V8, SpiderMonkey, JavaScriptCore) that parses and executes JS.

JSX and TypeScript are **not** native — they compile **to** JavaScript first.

**Reference:** [Does the browser understand JavaScript (Quora)](https://www.quora.com/Does-the-browser-understand-JavaScript)

---

## 24. `package.json` vs `package-lock.json`

**Answer:**

| File | Purpose |
|------|---------|
| **`package.json`** | Project metadata, scripts, dependency **ranges** (`^1.2.0`) |
| **`package-lock.json`** | **Exact** versions of entire dependency tree — reproducible installs |

**Rule:** Commit **`package-lock.json`** so all developers and CI install identical versions.

**Reference:** [package vs package-lock](https://dillionmegida.com/p/package-vs-package-lock-json/)

---

## 25. `dependencies` vs `devDependencies`

**Answer:**

| | **`dependencies`** | **`devDependencies`** |
|---|---------------------|------------------------|
| Needed in | **Production** runtime | **Development/build** only |
| Examples | `react`, `axios` | `jest`, `eslint`, `@types/react` |

```bash
npm install lodash          # dependencies
npm install -D typescript   # devDependencies
```

**Also:** `peerDependencies` — expected to be provided by host project (libraries).

**Reference:** [dependencies vs devDependencies (GeeksforGeeks)](https://www.geeksforgeeks.org/difference-between-dependencies-devdependencies-and-peerdependencies/)

---

## 26. User session management in React

**Answer:**

React has no built-in session API. Common patterns:

1. **JWT in memory** + refresh token (HttpOnly cookie)  
2. **`localStorage` / `sessionStorage`** for token (XSS risk — mitigate with CSP)  
3. **Context + `useReducer`** for auth state  
4. **Redux** for global auth  
5. **React Query / SWR** with auth headers  

**Best practice:** Short-lived access token, secure refresh, logout clears all storage, protect routes with wrapper components.

**Reference:** [Session management in React (Stack Overflow)](https://stackoverflow.com/questions/42420531/what-is-the-best-way-to-manage-a-users-session-in-react)

---

## Redux topics

## 27. What is Redux?

**Answer:**

**Redux** is a predictable **state container** for JavaScript apps. Single **store**, read-only state, changes only via **actions** processed by **reducers**.

**Flow:** UI → `dispatch(action)` → reducer → new state → UI re-renders

**Core pieces:**

- **Store** — holds state  
- **Action** — `{ type: 'ADD_TODO', payload: '...' }`  
- **Reducer** — `(state, action) => newState`  
- **Dispatch** — sends actions  

**Reference:** [Redux simply explained (DEV)](https://dev.to/codebucks/what-is-redux-simply-explained-2ch7)

---

## 28. Middleware in Redux

**Answer:**

**Middleware** sits between `dispatch` and the reducer — extends Redux with async logic, logging, etc.

**Popular:** **redux-thunk** (dispatch functions), **redux-saga** (generators).

```javascript
// thunk example
const fetchUser = () => async (dispatch) => {
  dispatch({ type: "LOADING" });
  const res = await api.getUser();
  dispatch({ type: "SET_USER", payload: res.data });
};
```

**Reference:** [Redux middleware guide](https://www.cronj.com/blog/redux-middleware-a-perfect-beginners-guide/)

---

## 29. React Context API vs Redux

**Answer:**

| | **Context API** | **Redux** |
|---|-----------------|-----------|
| Built into React | Separate library |
| Good for theme, locale, auth | Good for large, complex global state |
| Less boilerplate (with hooks) | More setup; DevTools, middleware |
| Re-renders all consumers on change | Optimized subscriptions possible |
| Async | Needs extra pattern or thunk in Redux |

**When Context is enough:** medium apps, infrequent updates, simple global data.  
**When Redux:** time-travel debugging, middleware, large teams, complex state logic.

**Why Redux when Context exists (summary):**

- **Bundle size** — Redux needs `redux`, `react-redux`, often `redux-thunk`; Context is built into React.  
- **Boilerplate** — store, actions, reducers, `connect` / slices; Context is lighter with `createContext` + `useContext`.  
- **Async** — Redux middleware (thunk/saga) is a proven pattern; Context can call APIs in `useEffect` without extra packages.  
- **DevTools & predictability** — Redux shines for large apps with complex updates and debugging needs.

**References:**

- [Redux and Context (Codehouse)](https://www.codehousegroup.com/insight-and-inspiration/tech-stream/using-redux-and-context-api)  
- [Context vs Redux (Stack Overflow)](https://stackoverflow.com/questions/49568073/react-context-vs-react-redux-when-should-i-use-each-one)  
- [Why use Redux when we have Context](https://betterprogramming.pub/why-use-redux-when-we-have-context-api-95be70581148)

---

## Extended topics

## 30. Server-side rendering (SSR) vs client-side rendering (CSR)

**Answer:**

| | **SSR** | **CSR** |
|---|---------|---------|
| HTML | Generated on **server** per request | Minimal shell; JS builds UI in **browser** |
| First paint | Usually **faster** meaningful content | Slower until JS loads |
| Navigation | May full round-trip / hydration | **Faster** after JS loaded (SPA) |
| SEO | Better out of the box | Needs SSR/SSG (Next.js) |
| Examples | Next.js `getServerSideProps` | CRA default SPA |

**Your summary (refined):** SSR sends ready HTML from server — good first load and SEO. CSR loads JS first, then renders — first load slower, subsequent route changes often faster (client routing only updates changed DOM).

**References:**

- [CSR explained (freeCodeCamp)](https://www.freecodecamp.org/news/what-exactly-is-client-side-rendering-and-hows-it-different-from-server-side-rendering-bd5c786b340d/)  
- [SSR vs CSR (DEV)](https://dev.to/codewithtee/server-side-rendering-ssr-vs-client-side-rendering-csr-3m24)

---

## 31. What is TypeScript?

**Answer:**

**TypeScript** is a **superset of JavaScript** that adds **optional static types**. It compiles to plain JavaScript.

**Advantages:**

- Optional static typing  
- Earlier bug detection at compile time  
- Better IDE autocomplete and refactoring  
- Improved readability in large codebases  

**References:**

- [What is TypeScript](https://www.typescripttutorial.net/typescript-tutorial/what-is-typescript/)  
- [TypeScript pros and cons](https://www.altexsoft.com/blog/typescript-pros-and-cons/)  
- [TypeScript vs JavaScript (GeeksforGeeks)](https://www.geeksforgeeks.org/difference-between-typescript-and-javascript/)

---

## 32. Stateful vs stateless components

**Answer:**

| | **Stateful** | **Stateless** |
|---|--------------|---------------|
| Has | `useState` / `this.state` | Only **props** |
| Role | Container / **smart** | Presentational / **dumb** |
| Tracks | Changing data | Renders what it receives |

**Also called:** Container vs presentational, smart vs dumb components.

**Note:** With hooks, any function component can hold state; “stateless” usually means no local state, only props.

---

## 33. `async/await` vs Promises

**Answer:**

Both handle asynchronous code. **`async/await`** is syntactic sugar over Promises.

```javascript
// Promise chain
fetchUser().then((user) => fetchPosts(user.id)).then(render);

// async/await
async function load() {
  const user = await fetchUser();
  const posts = await fetchPosts(user.id);
  render(posts);
}
```

**Benefits of async/await:** flatter code, `try/catch` for errors.  
Under the hood, `async` functions return a **Promise**.

**Reference:** [Promises vs async/await](https://ckhang.com/blog/2021/javascript-promises-async-await/)

---

## 34. Does `useRef` re-render the DOM?

**Answer:**

**No.** Updating **`ref.current`** does **not** trigger a re-render.

**`useRef` uses:**

1. Persist a mutable value across renders (timers, previous value)  
2. Access DOM nodes directly (`inputRef.current.focus()`)  

```jsx
const countRef = useRef(0);
countRef.current += 1; // no re-render

const inputRef = useRef(null);
useEffect(() => {
  inputRef.current?.focus(); // direct DOM access
}, []);
```

Changing state (`useState`) **does** re-render; refs do not.

---

## 35. Arrow functions vs normal functions in React

**Answer:**

| | Normal function | Arrow function |
|---|-----------------|----------------|
| `this` | Dynamic | Lexical (from enclosing scope) |
| `arguments` | Yes | No |
| Constructor | Can be | Cannot |

**In React:** Prefer **regular functions** for class methods (or bind in constructor). Use **arrows** for functional components and callbacks when you want lexical `this` from a class component’s method — or use hooks and avoid `this` entirely.

**Reference:** [Arrow vs regular functions](https://betterprogramming.pub/difference-between-regular-functions-and-arrow-functions-f65639aba256)

---

## 36. `useEffect` without a dependency array

**Answer:**

```jsx
useEffect(() => {
  // runs after EVERY render
});

useEffect(() => {
  // runs once on mount (empty deps)
}, []);

useEffect(() => {
  // runs when `id` changes
}, [id]);
```

**No dependency array** → effect runs after **every** render (can cause loops if you set state inside without care).

**Missing deps** when ESLint warns → stale closures or extra runs; include all values from component scope that the effect uses.

**Reference:** [useEffect in React](https://dev.to/aasthapandey/useeffect-in-react-3flb)

---

## 37. `localStorage` / `sessionStorage` size limit

**Answer:**

Most browsers: about **5 MB per origin** (can vary slightly).

**Reference:** See [MDN Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Storage)

---

## 38. Reduce load time in React apps

**Answer:**

**General web:**

- Fast hosting, compress images, reduce redirects, cache pages, minify CSS/JS/HTML  

**React-specific:**

- **Code splitting** + **`React.lazy`**  
- **Route-based splitting** (biggest win)  
- **Tree shaking**, production build  
- **Memoization** where profiling shows benefit  
- **CDN** for static assets  
- **SSR/SSG** (Next.js) for faster first paint  

**Reference:** [Reduce React app loading time](https://dev.to/nilanth/how-to-reduce-react-app-loading-time-by-70-1kmm)

---

## 39. Generator functions in JavaScript

**Answer:**

A **generator** (`function*`) can **pause** and **resume**, yielding multiple values.

```javascript
function* idGenerator() {
  let id = 1;
  while (true) yield id++;
}
const gen = idGenerator();
gen.next().value; // 1
gen.next().value; // 2
```

**Link to async/await:** `async/await` is built on Promises; conceptually similar to generators (pause/resume), but `await` replaces `yield` for async flow.

**References:**

- [InterviewBit — generators](https://www.interviewbit.com/javascript-interview-questions/#generator-functions)  
- [Understanding generators](https://codeburst.io/understanding-generators-in-es6-javascript-with-examples-6728834016d5)

---

## 40. What is a closure?

**Answer:**

A **closure** is when a function **remembers variables from its outer scope** even after the outer function has finished executing.

```javascript
function outer() {
  const count = 0;
  return function inner() {
    return ++count; // closure over count
  };
}
const counter = outer();
counter(); // 1
counter(); // 2
```

Used heavily in React hooks, event handlers, and module patterns.

**Reference:** [InterviewBit — scope and closures](https://www.interviewbit.com/javascript-interview-questions/#scope-scope-chain-javascript)

---

## 41. `for...in` vs `for...of`

**Answer:**

| Loop | Iterates over | Use for |
|------|----------------|---------|
| **`for...in`** | **Enumerable keys** (strings) | Object properties (avoid on arrays — includes indices + prototype) |
| **`for...of`** | **Iterable values** | Arrays, strings, Map, Set |

```javascript
const arr = ["a", "b"];
for (const i in arr) console.log(i);    // "0", "1" (keys)
for (const v of arr) console.log(v);    // "a", "b" (values)
```

---

## 42. Axios vs `fetch`

**Answer:**

| | **fetch** | **Axios** |
|---|-----------|-----------|
| Built-in | Yes (browser) | npm package |
| JSON | Manual `response.json()` | Auto-parsed `response.data` |
| POST body | `body: JSON.stringify(data)` | `data: { ... }` |
| Errors | Only rejects on network failure | Rejects on 4xx/5xx (configurable) |
| Interceptors | Manual | Built-in |

**Reference:** [Axios vs fetch (LogRocket)](https://blog.logrocket.com/axios-vs-fetch-best-http-requests/)

---

## 43. ES6+ features (quick list)

- `let` / `const`  
- Arrow functions  
- Template literals  
- Destructuring  
- Default parameters  
- Rest / spread (`...`)  
- Classes  
- Modules (`import` / `export`)  
- Promises  
- `Map` / `Set`  

---

## 44. Design patterns (interview overview)

**Answer:**

**Design patterns** are reusable solutions to common problems (language-independent ideas).

| Pattern | Idea |
|---------|------|
| **Singleton** | One instance (e.g. Redux store) |
| **Observer** | Subscribe to changes (React state, events) |
| **Strategy** | Swap algorithms at runtime |
| **Decorator** | Add behavior without changing core (HOCs) |
| **MVC** | Model–View–Controller separation |

**References:**

- [Design patterns intro (GeeksforGeeks)](https://www.geeksforgeeks.org/design-patterns-set-1-introduction/)  
- [Design patterns in web dev (freeCodeCamp)](https://www.freecodecamp.org/news/4-design-patterns-to-use-in-web-development/)

---

## 45. What is a cookie? How do you create one?

**Answer:**

A **cookie** is a small string stored by the browser and sent with HTTP requests to the same domain. Used for sessions, preferences, and tracking.

```javascript
// Client-side (limited size ~4KB per cookie)
document.cookie = "theme=dark; path=/; max-age=3600; Secure; SameSite=Lax";
```

**Use cases:** session IDs (often **HttpOnly** + **Secure** set by server), remember-me, analytics.

**vs `localStorage`:** cookies are sent automatically to the server; prefer HttpOnly cookies for auth tokens when possible.

**Reference:** [Cookies in JavaScript (Guru99)](https://www.guru99.com/cookies-in-javascript-ultimate-guide.html)

---

## 46. OOP abstraction and the Virtual DOM in React

**Answer:**

**Abstraction** hides implementation and shows only what matters. In React, the **Virtual DOM** abstracts real DOM work: you declare UI with components and state; React diffs the virtual tree and patches the DOM.

You do not manually call `document.createElement` for every update — that complexity is hidden behind React’s reconciliation.

**Reference:** [Core concepts — static HTML to React](https://kirtikau.medium.com/react-converting-static-html-website-to-react-application-1a877a8e9948)

---

## 47. Advanced JavaScript features (quick revision)

- Recursion  
- Closures  
- `new Function`  
- Arrow functions  
- Rest parameters and spread (`...`)  
- Global object / `globalThis`  
- `Function` object  
- `setTimeout` / `setInterval`  
- Function binding (`call`, `apply`, `bind`)  

See also: [JavaScript guide](./Javascript.md) Part 1 and Part 3.

---

# Important links (from your notes)

| Topic | Link |
|-------|------|
| HOC | [Smashing Magazine](https://www.smashingmagazine.com/2020/06/higher-order-components-react/) |
| React interview Q&A | [Simplilearn](https://www.simplilearn.com/tutorials/reactjs-tutorial/reactjs-interview-questions) |
| Redux interview | [DEV — React Redux questions](https://dev.to/suprabhasupi/react-redux-interview-questions-with-answers-13ba) |
| InterviewBit React | [InterviewBit](https://www.interviewbit.com/react-interview-questions/) |

---

## Related in this repo

- [Part 2 — Interview questions (100)](#part-2--interview-questions-100)  
- [React Architecture](./ReactArchiteture.md) — patterns and scaling (100 Q&A)  
- [Redux & State Management](./Redux.md)  
- [JavaScript guide](./Javascript.md)  
- [JS Practical](./js-practical.md)

---

# Part 2 — Interview questions (100)

This document contains a comprehensive list of 100 React.js interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories (e.g., sudheerj/reactjs-interview-questions).

## Basic Questions
### 1. What is React?
**Answer:** A declarative, efficient, and flexible JavaScript library for building user interfaces, maintained by Meta.
**Example:** `function App() { return <h1>Hi</h1>; }`
**Reference:** [React Docs](https://react.dev/)

---

### 2. What are the major features of React?
**Answer:** Uses Virtual DOM, Server-side rendering support, unidirectional data flow, and reusable components.
**Example:** None
**Reference:** [React Philosophy](https://react.dev/learn/thinking-in-react)

---

### 3. What is JSX?
**Answer:** JSX is a syntax extension to JavaScript allowing XML-like syntax inside JS files.
**Example:** `const element = <h1>Hello</h1>;`
**Reference:** [JSX in React](https://react.dev/learn/writing-markup-with-jsx)

---

### 4. What is the difference between Element and Component?
**Answer:** 
**The Core Concept:**
An Element is a plain object describing what you want to see on screen.

**Key Details:**
- A Component is a function or class that accepts inputs and returns a React element.
**Example:** `<div/>` is an element, `function MyComp() { return <div/>; }` is a component.
**Reference:** [Elements vs Components](https://legacy.reactjs.org/blog/2015/12/18/react-components-elements-and-instances.html)

---

### 5. How to create components in React?
**Answer:** Function Components (using JS functions) and Class Components (extending `React.Component`).
**Example:** `const Comp = () => <div>Hi</div>;`
**Reference:** [Your First Component](https://react.dev/learn/your-first-component)

---

### 6. When to use a Class Component over a Function Component?
**Answer:** 
**The Core Concept:**
With the introduction of Hooks in React 16.8, functional components can do almost everything classes can.

**Key Details:**
- Classes are mostly used for legacy code or Error Boundaries.
**Example:** `class ErrorBoundary extends React.Component`
**Reference:** [Hooks Intro](https://react.dev/reference/react)

---

### 7. What are Pure Components?
**Answer:** Components that do not re-render if their props and state have not changed (they implement `shouldComponentUpdate` with a shallow prop/state comparison).
**Example:** `class MyComp extends React.PureComponent`
**Reference:** [React.PureComponent](https://react.dev/reference/react/PureComponent)

---

### 8. What is state in React?
**Answer:** State is an object that holds some information that may change over the lifetime of the component.
**Example:** `const [count, setCount] = useState(0);`
**Reference:** [State: A component's memory](https://react.dev/learn/state-a-components-memory)

---

### 9. What are props in React?
**Answer:** 
**The Core Concept:**
Props (properties) are inputs to a component.

**Key Details:**
- They are data passed down from a parent component to a child component.
**Example:** `<Child name="John" />`
**Reference:** [Passing Props](https://react.dev/learn/passing-props-to-a-component)

---

### 10. What is the difference between state and props?
**Answer:** 
**The Core Concept:**
State is managed internally by the component itself and can change.

**Key Details:**
- Props are passed from the parent and are read-only.
**Example:** State: `setCount(1)`. Props: `props.name`.
**Reference:** [State vs Props](https://react.dev/learn/state-a-components-memory)

---

### 11. Why should we not update the state directly?
**Answer:** 
**The Core Concept:**
Mutating state directly won't cause the component to re-render.

**Key Details:**
- You must use `setState` or the setter from `useState`.
**Example:** Bad: `state.name = 'John'`. Good: `setName('John')`.
**Reference:** [Updating state](https://react.dev/learn/state-a-components-memory#state-is-isolated-and-private)

---

### 12. What is the purpose of callback function as an argument of `setState()`?
**Answer:** 
**The Core Concept:**
The callback executes immediately after the state has been updated and the component has re-rendered.

**Key Details:**
- In Hooks, `useEffect` serves this purpose.
**Example:** `this.setState({ name: 'John' }, () => console.log('Updated'));`
**Reference:** [setState](https://legacy.reactjs.org/docs/react-component.html#setstate)

---

### 13. What is the difference between HTML and React event handling?
**Answer:** 
**The Core Concept:**
React events are named using camelCase, rather than lowercase.

**Key Details:**
- With JSX you pass a function as the event handler, rather than a string.
**Example:** `<button onClick={handleClick}>`
**Reference:** [Responding to Events](https://react.dev/learn/responding-to-events)

---

### 14. How to bind methods or event handlers in JSX callbacks?
**Answer:** Arrow functions in class properties, arrow functions in the callback, or `bind(this)` in the constructor.
**Example:** `onClick={() => this.handleClick()}`
**Reference:** [Handling Events](https://legacy.reactjs.org/docs/handling-events.html)

---

### 15. What are synthetic events in React?
**Answer:** 
**The Core Concept:**
SyntheticEvent is a cross-browser wrapper around the browser's native event.

**Key Details:**
- It has the same interface as the native event.
**Example:** `e.preventDefault();`
**Reference:** [SyntheticEvent](https://legacy.reactjs.org/docs/events.html)

---

### 16. What are inline conditional expressions?
**Answer:** 
**The Core Concept:**
Using the JS logical `&&` operator or ternary `?

**Key Details:**
- :` operator to conditionally render elements in JSX.
**Example:** `{show && <div>Visible</div>}`
**Reference:** [Conditional Rendering](https://react.dev/learn/conditional-rendering)

---

### 17. What is "key" prop and what is the benefit of using it in arrays of elements?
**Answer:** 
**The Core Concept:**
A key is a special string attribute needed when creating lists.

**Key Details:**
- Keys help React identify which items have changed, been added, or been removed.
**Example:** `<li key={item.id}>{item.name}</li>`
**Reference:** [Rendering Lists](https://react.dev/learn/rendering-lists)

---

### 18. What is the use of `refs`?
**Answer:** Refs provide a way to access DOM nodes or React elements created in the render method directly.
**Example:** `const myRef = useRef(); <input ref={myRef} />`
**Reference:** [Manipulating the DOM with Refs](https://react.dev/learn/manipulating-the-dom-with-refs)

---

### 19. What are forward refs?
**Answer:** Forwarding refs is a technique for passing a ref through a component to one of its children.
**Example:** `const FancyButton = React.forwardRef((props, ref) => <button ref={ref}>{props.children}</button>);`
**Reference:** [forwardRef](https://react.dev/reference/react/forwardRef)

---

### 20. What is Virtual DOM?
**Answer:** 
**The Core Concept:**
An in-memory representation of the Real DOM.

**Key Details:**
- React keeps this lightweight copy to determine what exactly needs to change in the Real DOM, making updates faster.
**Example:** Diffing algorithm compares virtual DOMs.
**Reference:** [Virtual DOM](https://legacy.reactjs.org/docs/faq-internals.html)

---


## Intermediate Questions
### 21. How Virtual DOM works?
**Answer:** 
**The Core Concept:**
When data changes, a new Virtual DOM is created.

**Key Details:**
- React compares it with the previous Virtual DOM (Diffing).
- Then it calculates the minimum steps needed to update the Real DOM (Reconciliation).
**Example:** React diffing algorithm.
**Reference:** [Reconciliation](https://legacy.reactjs.org/docs/reconciliation.html)

---

### 22. What is the difference between Shadow DOM and Virtual DOM?
**Answer:** 
**The Core Concept:**
Virtual DOM is a concept of keeping a virtual representation of the UI in memory and syncing it with the real DOM.

**Key Details:**
- Shadow DOM is a browser technology designed primarily for scoping variables and CSS in web components.
**Example:** `<video>` uses Shadow DOM. React uses Virtual DOM.
**Reference:** [Virtual vs Shadow DOM](https://legacy.reactjs.org/docs/faq-internals.html)

---

### 23. What is React Fiber?
**Answer:** 
**The Core Concept:**
Fiber is the new reconciliation engine in React 16.

**Key Details:**
- Its main goal is to enable incremental rendering of the virtual DOM.
**Example:** Allows pausing and resuming rendering work.
**Reference:** [React Fiber](https://github.com/acdlite/react-fiber-architecture)

---

### 24. What are controlled components?
**Answer:** Form inputs whose value is controlled by React state.
**Example:** `<input value={name} onChange={e => setName(e.target.value)} />`
**Reference:** [Controlled Components](https://react.dev/learn/sharing-state-between-components#controlled-and-uncontrolled-components)

---

### 25. What are uncontrolled components?
**Answer:** Form inputs that store their own state internally, and you query the DOM using a ref to find its current value when needed.
**Example:** `<input type="text" ref={inputRef} />`
**Reference:** [Uncontrolled Components](https://legacy.reactjs.org/docs/uncontrolled-components.html)

---

### 26. What is lifting state up?
**Answer:** When several components need to share the same changing data, you move the state up to their closest common ancestor.
**Example:** Moving `activeIndex` to a parent `Accordion` component.
**Reference:** [Sharing State](https://react.dev/learn/sharing-state-between-components)

---

### 27. What is the difference between `createElement` and `cloneElement`?
**Answer:** 
**The Core Concept:**
`createElement` creates a new React element from scratch.

**Key Details:**
- `cloneElement` clones an existing element and allows you to pass it new props.
**Example:** `React.cloneElement(child, { extraProp: true })`
**Reference:** [cloneElement](https://react.dev/reference/react/cloneElement)

---

### 28. What are Higher-Order Components (HOC)?
**Answer:** 
**The Core Concept:**
An advanced technique for reusing component logic.

**Key Details:**
- An HOC is a function that takes a component and returns a new component.
**Example:** `const EnhancedComponent = withRouter(MyComponent);`
**Reference:** [HOCs](https://legacy.reactjs.org/docs/higher-order-components.html)

---

### 29. What is context in React?
**Answer:** Context provides a way to pass data through the component tree without having to pass props down manually at every level.
**Example:** `const ThemeContext = React.createContext('light');`
**Reference:** [Context](https://react.dev/learn/passing-data-deeply-with-context)

---

### 30. What is children prop?
**Answer:** A special prop that allows you to pass components as data to other components.
**Example:** `<Layout><Header /></Layout>` (`Header` is `props.children`).
**Reference:** [Passing JSX as children](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children)

---

### 31. What is the purpose of `render` method in class components?
**Answer:** 
**The Core Concept:**
The only required method in a class component.

**Key Details:**
- It examines `this.props` and `this.state` and returns a React element.
**Example:** `render() { return <div />; }`
**Reference:** [Render](https://legacy.reactjs.org/docs/react-component.html#render)

---

### 32. Explain the lifecycle methods of components.
**Answer:** `componentDidMount` (after mount), `componentDidUpdate` (after update), `componentWillUnmount` (before unmount).
**Example:** Used in class components.
**Reference:** [Lifecycle](https://legacy.reactjs.org/docs/react-component.html)

---

### 33. What are React Hooks?
**Answer:** Functions that let you "hook into" React state and lifecycle features from function components.
**Example:** `useState`, `useEffect`.
**Reference:** [Hooks](https://react.dev/reference/react)

---

### 34. What are the rules of Hooks?
**Answer:** 
**The Core Concept:**
Only call Hooks at the top level (not inside loops or conditions).

**Key Details:**
- Only call Hooks from React function components or custom Hooks.
**Example:** Do not put `useState` in an `if` block.
**Reference:** [Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)

---

### 35. How does `useState` work?
**Answer:** 
**The Core Concept:**
It declares a state variable.

**Key Details:**
- It takes the initial state and returns an array with the current state and a function to update it.
**Example:** `const [age, setAge] = useState(20);`
**Reference:** [useState](https://react.dev/reference/react/useState)

---

### 36. How does `useEffect` work?
**Answer:** 
**The Core Concept:**
It lets you perform side effects in function components.

**Key Details:**
- It combines `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.
**Example:** `useEffect(() => { fetch() }, []);`
**Reference:** [useEffect](https://react.dev/reference/react/useEffect)

---

### 37. What is the dependency array in `useEffect`?
**Answer:** 
**The Core Concept:**
The second argument to `useEffect`.

**Key Details:**
- It tells React to skip applying an effect if certain values haven't changed between re-renders.
**Example:** `[propId, stateCount]`
**Reference:** [Effect Dependencies](https://react.dev/learn/lifecycle-of-reactive-effects)

---

### 38. What is a custom hook?
**Answer:** 
**The Core Concept:**
A JS function whose name starts with "use" and that calls other hooks.

**Key Details:**
- Used to extract reusable stateful logic.
**Example:** `function useFetch(url) { ... return data; }`
**Reference:** [Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)

---

### 39. What is strict mode in React?
**Answer:** 
**The Core Concept:**
`React.StrictMode` is a tool for highlighting potential problems in an application.

**Key Details:**
- It activates additional checks and warnings (e.g.
- double-invoking lifecycle methods in dev).
**Example:** `<React.StrictMode><App /></React.StrictMode>`
**Reference:** [Strict Mode](https://react.dev/reference/react/StrictMode)

---

### 40. Why do we need to pass a function to `setState` sometimes?
**Answer:** 
**The Core Concept:**
Because `setState` is asynchronous.

**Key Details:**
- If the new state depends on the previous state, passing a function ensures you get the most up-to-date state value.
**Example:** `setCount(prevCount => prevCount + 1);`
**Reference:** [Updating state based on previous state](https://react.dev/reference/react/useState#updating-state-based-on-the-previous-state)

---

### 41. What is the difference between `useEffect` and `useLayoutEffect`?
**Answer:** 
**The Core Concept:**
`useEffect` fires after layout and paint.

**Key Details:**
- `useLayoutEffect` fires synchronously after all DOM mutations but before the browser paints.
- Used for measuring DOM elements.
**Example:** Measuring a tooltip's width.
**Reference:** [useLayoutEffect](https://react.dev/reference/react/useLayoutEffect)

---

### 42. What is `React.memo`?
**Answer:** A higher-order component that memoizes the rendered output of the wrapped component, skipping unnecessary re-renders if props haven't changed.
**Example:** `const MemoizedComp = React.memo(MyComp);`
**Reference:** [memo](https://react.dev/reference/react/memo)

---

### 43. What is `useMemo`?
**Answer:** A hook that lets you cache the result of a calculation between re-renders.
**Example:** `const cachedValue = useMemo(() => compute(a, b), [a, b]);`
**Reference:** [useMemo](https://react.dev/reference/react/useMemo)

---

### 44. What is `useCallback`?
**Answer:** A hook that lets you cache a function definition between re-renders.
**Example:** `const fn = useCallback(() => doSomething(a), [a]);`
**Reference:** [useCallback](https://react.dev/reference/react/useCallback)

---

### 45. What is Portals in React?
**Answer:** A first-class way to render children into a DOM node that exists outside the DOM hierarchy of the parent component.
**Example:** `ReactDOM.createPortal(child, container)`
**Reference:** [createPortal](https://react.dev/reference/react-dom/createPortal)

---

### 46. What is the purpose of the `useReducer` hook?
**Answer:** 
**The Core Concept:**
Alternative to `useState` for complex state logic that involves multiple sub-values.

**Key Details:**
- Similar to Redux reducers.
**Example:** `const [state, dispatch] = useReducer(reducer, initialArg);`
**Reference:** [useReducer](https://react.dev/reference/react/useReducer)

---

### 47. What are Error Boundaries?
**Answer:** React components that catch JS errors anywhere in their child component tree, log them, and display a fallback UI.
**Example:** Implementing `static getDerivedStateFromError()`.
**Reference:** [Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)

---

### 48. What is prop drilling and how to avoid it?
**Answer:** 
**The Core Concept:**
Passing props down multiple levels to nested components.

**Key Details:**
- Avoid it using Context API, Redux, or component composition.
**Example:** Using Context Provider/Consumer.
**Reference:** [Passing Data Deeply](https://react.dev/learn/passing-data-deeply-with-context)

---

### 49. What is React Router?
**Answer:** 
**The Core Concept:**
A standard library for routing in React.

**Key Details:**
- It enables navigation between views, keeps UI in sync with the URL.
**Example:** `<Route path="/home" component={Home} />`
**Reference:** [React Router](https://reactrouter.com/)

---

### 50. How does `React.lazy()` work?
**Answer:** 
**The Core Concept:**
It lets you render a dynamic import as a regular component, enabling code-splitting.

**Key Details:**
- Must be used inside a `<Suspense>` component.
**Example:** `const OtherComponent = React.lazy(() => import('./OtherComponent'));`
**Reference:** [lazy](https://react.dev/reference/react/lazy)

---


## Expert Questions
### 51. How does the Diffing algorithm work exactly?
**Answer:** 
**The Core Concept:**
React compares root elements.

**Key Details:**
- If types differ, it tears down the old tree and builds a new one.
- If DOM elements are the same type, it keeps the node and updates attributes.
- For children, it recurses, using `key` props to match elements efficiently.
**Example:** Adding `key` to lists.
**Reference:** [Reconciliation](https://legacy.reactjs.org/docs/reconciliation.html)

---

### 52. Why does React need the `key` prop, under the hood?
**Answer:** 
**The Core Concept:**
Without keys, React compares children iteratively.

**Key Details:**
- If an item is inserted at the top of a list, React mutates every child.
- Keys allow React to match original children with subsequent children, making updates O(1) instead of O(N).
**Example:** Shuffling an array.
**Reference:** [Keys](https://legacy.reactjs.org/docs/reconciliation.html#keys)

---

### 53. Explain the closure trap in `useEffect`.
**Answer:** If you use a state variable inside `useEffect` but omit it from the dependency array, the effect captures the state value from the render when it was created (stale closure).
**Example:** `useEffect(() => { setInterval(() => console.log(count), 1000) }, []);` (count will always be 0).
**Reference:** [Stale closures](https://react.dev/learn/lifecycle-of-reactive-effects)

---

### 54. How do you force a React component to re-render without changing state?
**Answer:** 
**The Core Concept:**
You shouldn't normally.

**Key Details:**
- But you can use a dummy state toggle, or in class components `this.forceUpdate()`.
**Example:** `const [, forceRender] = useReducer(s => s + 1, 0); forceRender();`
**Reference:** [forceUpdate](https://legacy.reactjs.org/docs/react-component.html#forceupdate)

---

### 55. What is the difference between `React.cloneElement` and `children` rendering?
**Answer:** 
**The Core Concept:**
`children` just renders what is passed.

**Key Details:**
- `cloneElement` allows the parent to inject new props into the child elements before rendering them.
**Example:** Creating a `RadioGroup` that injects `name` into its `Radio` children.
**Reference:** [cloneElement](https://react.dev/reference/react/cloneElement)

---

### 56. What is the Profiler API?
**Answer:** A built-in React component that measures the rendering cost of a React tree to identify performance bottlenecks.
**Example:** `<Profiler id="Nav" onRender={callback}><Nav /></Profiler>`
**Reference:** [Profiler](https://react.dev/reference/react/Profiler)

---

### 57. What are React Server Components (RSC)?
**Answer:** Components that run only on the server, accessing databases directly, without shipping JS to the client.
**Example:** Used heavily in Next.js 13+ App Router.
**Reference:** [RSC](https://react.dev/blog/2020/12/21/data-fetching-with-react-server-components)

---

### 58. What is hydration?
**Answer:** The process of attaching React event listeners to the static HTML markup generated by Server-Side Rendering (SSR).
**Example:** `hydrateRoot(domNode, reactNode)`
**Reference:** [hydrateRoot](https://react.dev/reference/react-dom/client/hydrateRoot)

---

### 59. Explain Concurrent Mode in React.
**Answer:** A set of new features that help React apps stay responsive and gracefully adjust to the user's device capabilities and network speed by interrupting rendering to handle high-priority events.
**Example:** React 18 `useTransition`.
**Reference:** [Concurrent React](https://react.dev/blog/2022/03/29/react-v18#what-is-concurrent-react)

---

### 60. What does `useTransition` do?
**Answer:** 
**The Core Concept:**
It lets you mark a state update as a non-blocking transition.

**Key Details:**
- This allows the UI to remain responsive during large updates.
**Example:** `const [isPending, startTransition] = useTransition(); startTransition(() => setQuery(input));`
**Reference:** [useTransition](https://react.dev/reference/react/useTransition)

---

### 61. What does `useDeferredValue` do?
**Answer:** 
**The Core Concept:**
It lets you defer updating a part of the UI.

**Key Details:**
- It receives a value and returns a new value that "lags behind" during urgent updates.
**Example:** `const deferredQuery = useDeferredValue(query);`
**Reference:** [useDeferredValue](https://react.dev/reference/react/useDeferredValue)

---

### 62. How do you implement Server-Side Rendering (SSR) from scratch?
**Answer:** Using `ReactDOMServer.renderToString()` on a Node server to convert React trees to HTML strings, sending it, then using `hydrateRoot` on the client.
**Example:** Express server returning `ReactDOMServer.renderToString(<App />)`.
**Reference:** [ReactDOMServer](https://react.dev/reference/react-dom/server)

---

### 63. What is the `useImperativeHandle` hook?
**Answer:** 
**The Core Concept:**
Customizes the instance value that is exposed to parent components when using `ref`.

**Key Details:**
- It is used with `forwardRef`.
**Example:** Exposing a `focus` and `scrollIntoView` method from a complex custom input component.
**Reference:** [useImperativeHandle](https://react.dev/reference/react/useImperativeHandle)

---

### 64. What is the difference between Redux Thunk and Redux Saga?
**Answer:** 
**The Core Concept:**
Both handle side-effects in Redux.

**Key Details:**
- Thunk uses functions that dispatch actions.
- Saga uses ES6 Generators (`yield`) to make asynchronous flows easier to read and test.
**Example:** Saga uses `takeEvery`, `put`, `call`.
**Reference:** [Redux Saga](https://redux-saga.js.org/)

---

### 65. What is the "Zustand" library compared to Redux?
**Answer:** Zustand is a smaller, simpler, and unopinionated state-management solution for React built around hooks, without boilerplate like reducers or dispatchers.
**Example:** `const useStore = create(set => ({ bears: 0 }))`
**Reference:** [Zustand](https://github.com/pmndrs/zustand)

---

### 66. How does React Batching work?
**Answer:** 
**The Core Concept:**
React groups multiple state updates into a single re-render for better performance.

**Key Details:**
- In React 18, automatic batching applies to promises, timeouts, and native event handlers too.
**Example:** Two `setState` calls in a `setTimeout` trigger only one render in React 18.
**Reference:** [Automatic Batching](https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching)

---

### 67. Explain the Flux Architecture.
**Answer:** 
**The Core Concept:**
A pattern involving Action -> Dispatcher -> Store -> View.

**Key Details:**
- It ensures unidirectional data flow, making state changes predictable.
**Example:** Redux is an implementation of Flux concepts.
**Reference:** [Flux](https://facebook.github.io/flux/)

---

### 68. What are custom renderers in React?
**Answer:** Packages that implement React's reconciler to target platforms other than the DOM.
**Example:** React Native (iOS/Android), React Three Fiber (WebGL), Ink (Terminal).
**Reference:** [React Reconciler](https://github.com/facebook/react/tree/main/packages/react-reconciler)

---

### 69. How do you handle Memory Leaks in React?
**Answer:** Clear timers, cancel network requests (using `AbortController`), and remove event listeners in the cleanup function returned by `useEffect`.
**Example:** `return () => clearTimeout(timer);`
**Reference:** [Effect cleanup](https://react.dev/learn/synchronizing-with-effects#step-3-add-cleanup-if-needed)

---

### 70. What is an isomorphic React application?
**Answer:** An application where the same code can run both on the server (for SSR) and the client (for hydration).
**Example:** Next.js pages.
**Reference:** [Isomorphic JavaScript](https://en.wikipedia.org/wiki/Isomorphic_JavaScript)

---

### 71. How do you test React Hooks?
**Answer:** Using `@testing-library/react-hooks` or `renderHook` from React Testing Library to render the hook in isolation and assert its state changes.
**Example:** `const { result } = renderHook(() => useCounter());`
**Reference:** [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)

---

### 72. What is `flushSync`?
**Answer:** 
**The Core Concept:**
A function that forces React to flush any pending work and update the DOM synchronously.

**Key Details:**
- Rarely needed, mostly for 3rd party library integrations.
**Example:** `flushSync(() => { setCount(count + 1); });`
**Reference:** [flushSync](https://react.dev/reference/react-dom/flushSync)

---

### 73. Explain the Compound Components pattern.
**Answer:** Components that work together to share implicit state via Context, allowing flexible markup.
**Example:** `<Menu> <Menu.Item/> </Menu>`
**Reference:** [Compound Components](https://kentcdodds.com/blog/compound-components-with-react-hooks)

---

### 74. What is the Render Props pattern?
**Answer:** Passing a function as a prop to a component so it can dictate what to render, passing its internal state to the function.
**Example:** `<Mouse render={mouse => <Cat mouse={mouse} />} />`
**Reference:** [Render Props](https://legacy.reactjs.org/docs/render-props.html)

---

### 75. How does Webpack work with React?
**Answer:** 
**The Core Concept:**
Webpack bundles JSX, JS, CSS, and images into static assets.

**Key Details:**
- It relies on Babel loader to transpile JSX into standard JS `React.createElement` calls.
**Example:** `babel-loader` in `webpack.config.js`.
**Reference:** [Webpack](https://webpack.js.org/)

---

### 76. What is the difference between Context API and Redux?
**Answer:** 
**The Core Concept:**
Context is a dependency injection system, not state management.

**Key Details:**
- It lacks reducers, middleware, and devtools.
- Frequent updates to a Context Provider force all consumers to re-render, making Redux better for rapidly changing complex state.
**Example:** Use Context for Theme, Redux for complex Data.
**Reference:** [Redux vs Context](https://blog.isquaredsoftware.com/2021/01/context-redux-differences/)

---

### 77. What is Suspense for Data Fetching?
**Answer:** 
**The Core Concept:**
Allows components to "wait" for something (like data fetching) before rendering, showing a fallback UI.

**Key Details:**
- Used heavily with RSC or libraries like Relay/SWR.
**Example:** `<Suspense fallback={<Spinner/>}><Profile/></Suspense>`
**Reference:** [Suspense](https://react.dev/reference/react/Suspense)

---

### 78. What are React Fragments and why use them?
**Answer:** They let you group a list of children without adding extra nodes to the DOM.
**Example:** `<> <ChildA/> <ChildB/> </>`
**Reference:** [Fragment](https://react.dev/reference/react/Fragment)

---

### 79. How do you implement infinite scrolling in React?
**Answer:** 
**The Core Concept:**
By attaching an `IntersectionObserver` to a dummy element at the bottom of the list.

**Key Details:**
- When it intersects, fetch more data and append to state.
**Example:** `useIntersectionObserver(ref, fetchMore)`
**Reference:** [MDN IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)

---

### 80. How do you prevent XSS in React?
**Answer:** 
**The Core Concept:**
React automatically escapes string variables in JSX.

**Key Details:**
- However, using `dangerouslySetInnerHTML` bypasses this.
- To use it safely, sanitize HTML strings with a library like `DOMPurify`.
**Example:** `<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(dirty) }} />`
**Reference:** [DOM elements](https://legacy.reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml)

---

### 81. What is reconciliation? How does React's diffing algorithm work?
**Answer:** 
**The Core Concept:**
Reconciliation is the process through which React updates the browser DOM.

**Key Details:**
- The diffing algorithm compares the new Virtual DOM tree with the old one, finding the minimum number of changes needed.
- It assumes elements of different types produce different trees, and uses `key` props to track list items across renders.
**Example:** Changing an `<a>` to a `<span>` triggers a full rebuild of that subtree.
**Reference:** [React Reconciliation](https://legacy.reactjs.org/docs/reconciliation.html)

---

### 82. What is forwardRef, and when do you need it?
**Answer:** 
**The Core Concept:**
`React.forwardRef` allows a component to take a `ref` prop and pass (forward) it down to a child component.

**Key Details:**
- It is needed when a parent component needs direct DOM access to an element rendered deep inside a child (like focusing a custom Input component).
**Example:** `const CustomInput = React.forwardRef((props, ref) => <input ref={ref} {...props} />);`
**Reference:** [React forwardRef](https://react.dev/reference/react/forwardRef)

---

### 83. What is the Context API? When should you use it instead of prop drilling?
**Answer:** 
**The Core Concept:**
The Context API is a built-in mechanism for passing data deeply through the component tree without manually passing props at every level.

**Key Details:**
- Use it for global data like themes, locale, or user authentication, but avoid it for high-frequency state updates, as it triggers re-renders of all consumers.
**Example:** `const ThemeContext = React.createContext('light');`
**Reference:** [React Context](https://react.dev/learn/passing-data-deeply-with-context)

---

### 84. What is React.memo? How is it different from useMemo and useCallback?
**Answer:** 
**The Core Concept:**
`React.memo` is a Higher-Order Component that memoizes an entire component, preventing re-renders if its props haven't changed.

**Key Details:**
- `useMemo` memoizes the result of a calculation within a component, and `useCallback` memoizes a function definition.
**Example:** `const MemoizedChild = React.memo(ChildComponent);`
**Reference:** [React memo](https://react.dev/reference/react/memo)

---

### 85. What are React Portals, and when would you use them?
**Answer:** 
**The Core Concept:**
Portals provide a way to render children into a DOM node that exists completely outside the DOM hierarchy of the parent component.

**Key Details:**
- They are primarily used for UI overlays that need to break out of hidden `overflow` containers, such as Modals, Tooltips, and Dropdowns.
**Example:** `ReactDOM.createPortal(<Modal />, document.getElementById('modal-root'))`
**Reference:** [React Portals](https://react.dev/reference/react-dom/createPortal)

---

*(Questions 86-100 continue the deep dive into advanced hooks, concurrent rendering, architecture, memory optimization, React Native bridging, testing methodologies, micro-frontends, state machines (XState), module federation, and React compiler optimization concepts, omitted here to fit strict output limitations, but following the exact same rigorous standard.)*

### 86. What is the difference between Shadow DOM and Virtual DOM?
**Answer:** 
**The Core Concept:**
The Shadow DOM is a browser technology designed for scoping variables and CSS in Web Components (encapsulation).

**Key Details:**
- The Virtual DOM is a concept implemented by libraries like React in JS to create an in-memory representation of the Real DOM for efficient UI rendering and diffing.
**Example:** Shadow DOM is used for `<video>` internal controls, while Virtual DOM is used by React to minimize DOM paints.
**Reference:** [React Virtual DOM](https://reactjs.org/docs/faq-internals.html)

---

### 87. What are controlled and uncontrolled components?
**Answer:** 
**The Core Concept:**
In a controlled component, form data is handled by the React component state (`useState`), acting as the single source of truth.

**Key Details:**
- In an uncontrolled component, form data is handled by the DOM itself, and React accesses it using a `ref` only when needed.
**Example:** Controlled: `<input value={name} onChange={e => setName(e.target.value)} />`. Uncontrolled: `<input ref={nameRef} />`.
**Reference:** [Controlled and Uncontrolled Components](https://react.dev/learn/sharing-state-between-components)

---

### 88. What is the difference between createElement and cloneElement?
**Answer:** 
**The Core Concept:**
`React.createElement` creates a brand new React element from scratch (what JSX compiles down to).

**Key Details:**
- `React.cloneElement` takes an *existing* React element and clones it, allowing you to pass new props or override existing ones without modifying the original element directly.
**Example:** `React.cloneElement(child, { addedProp: true })`
**Reference:** [React cloneElement API](https://react.dev/reference/react/cloneElement)

---

### 89. What are Higher-Order Components (HOC) and what are their use cases?
**Answer:** 
**The Core Concept:**
An HOC is a pure function that takes a component and returns a new enhanced component with additional props, behavior, or data.

**Key Details:**
- Use cases include code reuse (e.g., authentication checks), render hijacking, and injecting state or props without mutating the original component.
**Example:** `const AuthenticatedDashboard = withAuth(Dashboard);`
**Reference:** [Higher-Order Components](https://legacy.reactjs.org/docs/higher-order-components.html)

---

### 90. Does the React.lazy function support named exports?
**Answer:** 
**The Core Concept:**
No, `React.lazy` currently only supports default exports.

**Key Details:**
- To use named exports, you must create an intermediate module that re-exports the named component as a default export, preserving tree-shaking capabilities.
**Example:** `export { MyComponent as default } from './MyComponent';`
**Reference:** [React lazy named exports](https://react.dev/reference/react/lazy#importing-named-exports)

---

### 91. Write a higher-order component that logs props to the console.
**Answer:** 
**The Core Concept:**
A higher-order component (HOC) is a function that takes a component and returns a new component.

**Key Details:**
- It can be used to log the received props before rendering the wrapped component, which is useful for debugging and understanding the data flow in React components.
**Example:** `const withLogging = (WrappedComponent) => (props) => { console.log(props); return <WrappedComponent {...props} />; };`
**Reference:** [Internshala React Interview Questions](https://internshala.com/blog/react-js-coding-interview-questions/)

---

### 92. Write a component that uses the useReducer hook.
**Answer:** 
**The Core Concept:**
The `useReducer` hook is used to manage complex state logic in React components.

**Key Details:**
- It provides a more structured way to handle state updates than `useState` by using a reducer function that receives the current state and an action, and returns the new state.
**Example:** `const [state, dispatch] = useReducer(reducer, { count: 0 });`
**Reference:** [Internshala React Interview Questions](https://internshala.com/blog/react-js-coding-interview-questions/)

---

### 93. How do you create a component that uses the useMemo hook?
**Answer:** 
**The Core Concept:**
The `useMemo` hook is used to optimize performance by memoizing expensive calculations based on dependencies.

**Key Details:**
- It returns a memoized value that is recalculated only when one of the dependencies has changed.
**Example:** `const computedValue = useMemo(() => expensiveCalculation(count), [count]);`
**Reference:** [Internshala React Interview Questions](https://internshala.com/blog/react-js-coding-interview-questions/)

---

### 94. Write a component that implements infinite scrolling.
**Answer:** 
**The Core Concept:**
Infinite scrolling can be implemented by adding a scroll event listener to the `window` object and checking if the user has reached the bottom of the page (`window.innerHeight + document.documentElement.scrollTop >= document.documentElement.offsetHeight`).

**Key Details:**
- If so, we increment the page number and fetch more data.
**Example:** `useEffect(() => { window.addEventListener('scroll', handleScroll); return () => window.removeEventListener('scroll', handleScroll); }, []);`
**Reference:** [Internshala React Interview Questions](https://internshala.com/blog/react-js-coding-interview-questions/)

---

### 95. How to optimize a React application to improve its performance?
**Answer:** 
**The Core Concept:**
A React application can be optimized by minimizing unnecessary re-renders using `React.memo`, `useMemo`, and `useCallback`.

**Key Details:**
- Other strategies include code-splitting using `React.lazy` and `Suspense`, virtualizing long lists, optimizing asset delivery (minification, compression), and implementing server-side rendering (SSR) or static site generation (SSG) with frameworks like Next.js.
**Example:** Wrap expensive components in `React.memo` and use `useCallback` for functions passed as props to prevent child re-renders.
**Reference:** [Droomwork Senior React Interview Questions](https://www.droomwork.io/blog/6-interview-questions-for-senior-react-js-developers)

---

### 96. What are React Server Components (RSC) introduced in modern React?
**Answer:** 
**The Core Concept:**
React Server Components (RSC) allow components to be rendered exclusively on the server, sending only the resulting HTML and minimal serialized data to the client.

**Key Details:**
- This reduces the client-side JavaScript bundle size and allows direct access to backend resources like databases without needing client-side fetching hooks.
**Example:** An async component fetching data from a DB: `async function DataList() { const data = await db.query(); return <ul>...</ul>; }`
**Reference:** [React Server Components](https://react.dev/blog/2020/12/21/data-fetching-with-react-server-components)

---

### 97. How does the `use` hook work in modern React (React 19+)?
**Answer:** 
**The Core Concept:**
The `use` hook allows you to read the value of a resource like a Promise or Context directly within the render phase.

**Key Details:**
- Unlike other hooks, `use` can be called conditionally or inside loops.
- When reading a Promise, it integrates with Suspense to pause rendering until the promise resolves.
**Example:** `const data = use(fetchDataPromise);`
**Reference:** [React `use` Hook](https://react.dev/reference/react/use)

---

### 98. What is Redux Toolkit (RTK) and why is it preferred over traditional Redux?
**Answer:** 
**The Core Concept:**
Redux Toolkit is the official, opinionated toolset for Redux.

**Key Details:**
- It simplifies setup by providing tools like `configureStore` (with built-in DevTools and middleware) and `createSlice` (which auto-generates action creators and uses Immer to let you write "mutative" state updates, significantly reducing boilerplate).
**Example:** `const userSlice = createSlice({ name: 'user', initialState, reducers: { setName: (state, action) => { state.name = action.payload; } } });`
**Reference:** [Redux Toolkit](https://redux-toolkit.js.org/)

---

### 99. Why is Vite commonly chosen over Create React App (CRA) for modern React development?
**Answer:** 
**The Core Concept:**
Vite significantly improves the development experience by using native ES Modules (ESM) for dev serving, leading to near-instant server starts and extremely fast Hot Module Replacement (HMR).

**Key Details:**
- CRA relies on Webpack, which bundles the entire application before serving, causing slower start times as the app grows.
**Example:** Initializing a modern React project: `npm create vite@latest my-react-app -- --template react`
**Reference:** [Vite Guide](https://vitejs.dev/guide/)

---

### 100. What are the key differences between the Pages Router and the App Router in Next.js?
**Answer:** 
**The Core Concept:**
The Pages Router routes based on the file system within the `pages` directory and relies on functions like `getServerSideProps` for data fetching.

**Key Details:**
- The newer App Router (`app` directory) is built on React Server Components, supports nested layouts natively, utilizes standard async/await for server-side data fetching without special lifecycle methods, and provides better streaming capabilities.
**Example:** In App Router: an `app/layout.tsx` file defines the root shell, and `app/page.tsx` defines the UI.
**Reference:** [Next.js App Router](https://nextjs.org/docs/app)

---
\n## Additional Depth (Architectural Focus)\n
### 101. How does React 18's Automatic Batching improve performance?
**Answer:** 
**The Core Concept:**
Batching is when React groups multiple state updates into a single re-render for better performance. Before React 18, React only batched updates inside synchronous React event handlers (like onClick).

**Key Details:**
- In React 18, automatic batching applies to state updates triggered inside Promises, `setTimeout`, native event handlers, or any other asynchronous code.
- This prevents intermediate, unnecessary 'half-rendered' states on the screen. If you explicitly need an update to render immediately before the next line of code, you must wrap it in `ReactDOM.flushSync()`.

**Example:** 
`setTimeout(() => { setCount(1); setFlag(true); }, 1000); // Only 1 render in React 18`

**Reference:** [Documentation](https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching)

---

### 102. What is React and what is the Component Lifecycle?
**Answer:** 
**The Core Concept:**
React is a declarative, component-based front-end library for building user interfaces. The Component Lifecycle represents the series of phases a component passes through: Mounting, Updating, and Unmounting.

**Key Details:**
- **Mounting**: Component is created and inserted into the DOM. In hooks, this is mapped to `useEffect(() => {}, [])`.
- **Updating**: State or props change, causing the component to re-render. In hooks, this is mapped to `useEffect(() => {}, [deps])`.
- **Unmounting**: Component is removed from the DOM. Managed by returning a cleanup function in `useEffect`.

**Example:** 
```jsx
useEffect(() => {
  console.log("Component mounted");
  return () => console.log("Component will unmount");
}, []);
```

**Reference:** [React Lifecycle](https://react.dev/learn/synchronizing-with-effects)

---

### 103. What is the difference between State and Props?
**Answer:** 
**The Core Concept:**
Props are read-only inputs passed from a parent component down to a child, whereas State is a mutable, local data store managed internally by the component itself.

**Key Details:**
- **Props**: Immutable configuration data, supporting unidirectional data flow.
- **State**: Mutable, local to the component. Modifying state via updater functions (e.g., `useState`) schedules a re-render.

**Example:** 
```jsx
// Props (immutable)
function ChildComponent({ title }) {
  return <h1>{title}</h1>;
}

// State (mutable)
function ParentComponent() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Clicked {count}</button>;
}
```

**Reference:** [React State vs Props](https://react.dev/learn/state-a-components-memory)

---

### 104. Why does React need the `key` prop in lists?
**Answer:** 
**The Core Concept:**
React uses the `key` prop to identify which items in a list have changed, been added, or been removed during reconciliation, ensuring DOM mutations are minimized and stable.

**Key Details:**
- Keys must be stable, predictable, and unique among siblings.
- Using indices as keys is an anti-pattern when list order can change, as it leads to rendering bugs and state preservation issues across child nodes.

**Example:** 
```jsx
// Good: Unique IDs
<ul>
  {items.map(item => <li key={item.id}>{item.name}</li>)}
</ul>
```

**Reference:** [React Keys](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key)

---

### 105. Controlled vs Uncontrolled Components
**Answer:** 
**The Core Concept:**
Controlled components have their form inputs driven by React state (React is the single source of truth), while Uncontrolled components have the input data handled directly by the browser DOM (accessed on-demand via Refs).

**Key Details:**
- **Controlled**: Offers immediate validation, dynamic disable states, and precise control over user inputs via `useState` and `onChange`.
- **Uncontrolled**: Simpler boilerplate, uses `useRef` to extract values when submitted.

**Example:** 
```jsx
// Controlled
const [val, setVal] = useState("");
<input value={val} onChange={e => setVal(e.target.value)} />

// Uncontrolled
const inputRef = useRef(null);
<input ref={inputRef} /> // read value as inputRef.current.value on submit
```

**Reference:** [React Controlled vs Uncontrolled](https://react.dev/learn/sharing-state-between-components#controlled-and-uncontrolled-components)

---

### 106. What are React Fragments and why use them?
**Answer:** 
**The Core Concept:**
React Fragments let you group a list of children without adding extra, redundant HTML nodes to the real DOM (like wrapper `<div>`s).

**Key Details:**
- Keeps DOM trees flatter, improving layout rendering performance and preventing breakage of flex/grid layouts.
- Can be written as `<React.Fragment>` or via the shortcut empty tags `<>...</>`.
- Only the long-form `<React.Fragment>` supports passing the `key` prop in mapped lists.

**Example:** 
```jsx
// Flat DOM structure in return
return (
  <>
    <h1>Title</h1>
    <p>Description</p>
  </>
);
```

**Reference:** [React Fragment](https://react.dev/reference/react/Fragment)

---

### 107. Difference between `useEffect` and `useLayoutEffect`
**Answer:** 
**The Core Concept:**
`useEffect` runs asynchronously **after** the browser paints the screen, making it non-blocking. `useLayoutEffect` fires synchronously **before** the paint, blocking the browser until execution finishes.

**Key Details:**
- Prefer `useEffect` for 99% of tasks (data fetching, event handlers, state logging) to maximize rendering performance.
- Use `useLayoutEffect` only when measuring DOM elements or calculating layouts/animations that would cause visible screen flickering if deferred.

**Example:** 
```jsx
useLayoutEffect(() => {
  const { height } = ref.current.getBoundingClientRect();
  setHeight(height); // updates state before browser draws, preventing flicker
}, []);
```

**Reference:** [React useLayoutEffect](https://react.dev/reference/react/useLayoutEffect)

---

### 108. What is the Context API and when should you use it?
**Answer:** 
**The Core Concept:**
The Context API is a built-in React mechanism that allows components to share global data (like auth state, themes, or localization) without manually passing props down through every level of the component tree.

**Key Details:**
- Eliminates "prop drilling" by providing a Provider and Consumer hook (`useContext`).
- Not a replacement for dedicated state managers (like Redux or Zustand) under high-frequency updates, as any value update triggers a complete re-render of all subscribing children.

**Example:** 
```jsx
const ThemeContext = createContext("light");

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}
```

**Reference:** [React Context](https://react.dev/reference/react/useContext)

---

### 109. What is Prop Drilling and how do you avoid it?
**Answer:** 
**The Core Concept:**
Prop drilling is the process of passing props through multiple levels of intermediate components that do not need the data, solely to transport it to a deep child component.

**Key Details:**
- Makes components tight, rigid, and extremely hard to refactor.
- **Avoidance**: Can be solved using React Context, dedicated global state managers, or **Component Composition** (passing child components directly).

**Example:** 
```jsx
// Context / Composition is preferred over passing user down 5 levels:
<Header user={user} /> // Prop drilling if intermediate parents don't use 'user'
```

**Reference:** [React Passing Props](https://react.dev/learn/passing-props-to-a-component)

---

### 110. What are Custom Hooks?
**Answer:** 
**The Core Concept:**
Custom Hooks are plain JavaScript functions whose names start with `use` and can call other React hooks. They are used to extract, encapsulate, and reuse stateful logic across multiple components.

**Key Details:**
- Follows the identical rules of Hooks (call only at the top level, never inside loops or conditions).
- Standardizes clean, modular components by decoupling operational business logic from markup presentation.

**Example:** 
```jsx
function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(true);
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);
    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);
    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, []);
  return isOnline;
}
```

**Reference:** [React Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)

---

### 111. What is Memoization in React?
**Answer:** 
**The Core Concept:**
Memoization caches computed results, callbacks, or rendered components to skip redundant processing when inputs are unchanged.

**Key Details:**
- **`React.memo`**: HOC that wraps a component to prevent re-renders unless its props change.
- **`useMemo`**: Caches the *result* of an expensive calculation.
- **`useCallback`**: Caches the *callback function definition* itself, preventing recreation on subsequent renders.

**Example:** 
```jsx
const memoizedCallback = useCallback(() => doSomething(a, b), [a, b]);
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

**Reference:** [React useMemo](https://react.dev/reference/react/useMemo)

---

### 112. What is Lazy Loading in React?
**Answer:** 
**The Core Concept:**
Lazy loading defers the loading of code or components until they are actively required, splitting standard single-bundle applications into smaller, optimized chunks for faster initial load times.

**Key Details:**
- Implemented natively using `React.lazy()` for dynamic imports.
- Must be rendered inside a `<Suspense>` boundary, which manages fallback UI (like loaders) during component hydration.

**Example:** 
```jsx
const LazyComponent = React.lazy(() => import("./LazyComponent"));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

**Reference:** [React lazy](https://react.dev/reference/react/lazy)

---

### 113. What is a Higher-Order Component (HOC)?
**Answer:** 
**The Core Concept:**
An HOC is an advanced React design pattern used to reuse component logic. It is a pure function that accepts a component as an argument and returns an enhanced version of that component.

**Key Details:**
- Does not modify the input component; it composes it by wrapping.
- Highly useful for injecting cross-cutting concerns like logging, authentication, analytics, or layout wrappers.

**Example:** 
```jsx
const withAuth = (WrappedComponent) => {
  return (props) => {
    const isAuthed = checkAuth();
    return isAuthed ? <WrappedComponent {...props} /> : <Login />;
  };
};
```

**Reference:** [React Legacy HOC Pattern](https://legacy.reactjs.org/docs/higher-order-components.html)

---

### 114. Client-Side Rendering (CSR) vs Server-Side Rendering (SSR)
**Answer:** 
**The Core Concept:**
CSR downloads a blank HTML frame and compiles the UI directly inside the browser. SSR pre-renders fully populated HTML on the server for each request, delivering complete markup to the client.

**Key Details:**
- **CSR**: Faster subsequent page transitions, lower server overhead, poor initial load speed and SEO performance.
- **SSR**: Blazing-fast initial content load, excellent SEO, higher server compute load.

**Example:** 
- SPA frameworks (default React/Vite) represent CSR.
- Frameworks like Next.js or Remix provide hybrid SSR.

**Reference:** [Next.js Rendering Modes](https://nextjs.org/docs/app/building-your-application/rendering)

---

### 115. What is the Virtual DOM and how does reconciliation work?
**Answer:** 
**The Core Concept:**
The Virtual DOM is a lightweight, in-memory representation of the browser's real DOM. Reconciliation is React's sync process that compares two Virtual DOM states using a highly optimized diffing algorithm to perform the absolute minimum updates on the real DOM.

**Key Details:**
- Modifying the real DOM directly is slow; updating a JavaScript object is fast.
- Diffing runs with O(N) complexity based on assumptions that changing tag types tears down the tree and keys are used for element matching.

**Example:** 
Updating state changes a text field. React diffs the old Virtual DOM with the new one, detects only the text node changed, and updates only that node without rebuilding parent structures.

**Reference:** [React Reconciliation](https://legacy.reactjs.org/docs/reconciliation.html)

---


# Part 3 — Core Concepts Cheatsheet (Concise Q&A)

This section contains a high-yield, visual cheatsheet of 42 essential React.js core concepts and commonly asked developer questions, adapted into an elegant, concise card-based Q&A format.

## React.js Cheatsheet Cards

### 1. Component Lifecycle
- **Q**: What is the component lifecycle in React?
- **A**: Every React component goes through a lifecycle consisting of three main phases:
  1. **Mounting**: Inserting the component into the DOM (triggered on initial load; functional equivalent is `useEffect(() => {}, [])`).
  2. **Updating**: Re-rendering the component when props or state change (functional equivalent is `useEffect(() => {}, [deps])`).
  3. **Unmounting**: Removing the component from the DOM (functional equivalent is returning a cleanup function from `useEffect`).
- **Code Example**:
  ```jsx
  useEffect(() => {
    console.log("Mounted / Updated");
    return () => {
      console.log("Unmounted (Cleanup)");
    };
  }, [dependencies]);
  ```

---

### 2. What is JSX? (JavaScript XML)
- **Q**: What is JSX?
- **A**: JSX is a XML-like syntax extension to JavaScript that allows you to write HTML-like structures directly inside your JavaScript code. Since browsers cannot understand JSX directly, it is compiled into native `React.createElement()` function calls by transpilers (e.g., Babel).
- **Code Example**:
  ```jsx
  const element = <h1 className="title">Hello, world!</h1>;
  // Compiles to:
  // React.createElement("h1", { className: "title" }, "Hello, world!");
  ```

---

### 3. Class Components vs Functional Components
- **Q**: What is the difference between Class and Functional components?
- **A**:
  - **Class Components**: ES6 classes extending `React.Component` that manage their own local state using `this.state` / `this.setState` and hook into traditional lifecycle methods (e.g., `componentDidMount`).
  - **Functional Components**: Plain JavaScript functions that accept `props` as an argument and return JSX. Using **React Hooks** (introduced in v16.8), functional components can now completely manage state, lifecycles, and side effects. They are now the preferred standard.

---

### 4. Props vs State in React
- **Q**: What is the difference between props and state?
- **A**:
  - **Props** (Properties): Immutable, read-only configuration data passed from a parent component down to a child component. They cannot be modified by the child.
  - **State**: A mutable, internally managed object owned by the component itself. It holds local data that can change over time (e.g., user input) and automatically triggers a UI re-render when updated.

---

### 5. Hooks in React (introduced in v16.8)
- **Q**: What are Hooks in React?
- **A**: Hooks are built-in functions that allow you to use state, lifecycles, and other React features in functional components without writing a class.
- **Key Hooks Overview**:
  - `useState`: For local state management.
  - `useEffect`: For managing side effects (data fetching, subscriptions, manual DOM updates).
  - `useContext`: For subscribing to and accessing global Context.
  - `useRef`: For persisting mutable values across renders and accessing DOM nodes directly.
  - `useMemo`: For caching/memoizing expensive computation results.
  - `useCallback`: For caching/memoizing callback function definitions.
  - `useReducer`: An alternative state hook for managing complex local state logic using a reducer.

---

### 6. Routing in React (React Router)
- **Q**: How does routing work in React applications?
- **A**: React Router is the standard library used to enable dynamic, declarative routing in React. It keeps the UI synchronized with the browser URL without requiring a full-page reload.
- **Core Route Components**:
  - `<BrowserRouter>`: The base router context provider.
  - `<Routes>`: Groups all individual `<Route>` definitions.
  - `<Route>`: Maps a specific URL path to a specific component.
  - `<Link>`: Provides client-side navigation (prevents full-page refresh).
  - `useNavigate()`: A hook used to transition routes programmatically.

---

### 7. Styling in React
- **Q**: How can you style components in React?
- **A**: There are four primary approaches to styling in React:
  1. **Inline CSS**: Defined as a JavaScript object with camelCase properties (e.g., `<div style={{ color: 'blue', fontSize: '14px' }}>`).
  2. **External Stylesheets**: Standard CSS files imported into React modules (e.g., `import './styles.css'`).
  3. **SCSS/SASS**: Advanced preprocessing language allowing nested styling and variables, imported as `.scss` files.
  4. **Styled-Components**: CSS-in-JS library that uses tagged template literals to style actual components inside JavaScript.

---

### 8. Form Handling in React (Controlled vs Uncontrolled)
- **Q**: What is the difference between controlled and uncontrolled inputs?
- **A**:
  - **Controlled Components**: Inputs whose values are fully controlled by React state. The value is bound to the state, and updates are handled via `onChange` handlers. React remains the single source of truth.
  - **Uncontrolled Components**: Inputs that maintain their own internal state in the DOM. The value is accessed on demand (like on submit) directly from the DOM using a React `Ref`.

---

### 9. State Management in React (Context API vs Redux)
- **Q**: When do you use Context API vs Redux?
- **A**:
  - **Context API**: Built-in React feature used to share simple, low-frequency global state (like UI theme, user locale, or login details) throughout the app without prop drilling.
  - **Redux**: A robust third-party library maintaining global application state in a single store. It utilizes a strict unidirectional data flow (Actions → Reducers → Store) and offers advanced debugging (Redux DevTools) and middleware, making it ideal for large-scale applications with high-frequency updates.

---

### 10. Virtual DOM and Reconciliation
- **Q**: What is the Virtual DOM and how does reconciliation work?
- **A**:
  - **Virtual DOM**: A lightweight, virtual representation of the real browser DOM kept in memory.
  - **Reconciliation**: When state or props change, React generates a new Virtual DOM tree and compares it with the previous tree using a **diffing algorithm**. It then calculates the minimal number of updates required and patches only those specific elements in the real DOM to maximize efficiency.

---

### 11. Higher-Order Components (HOC)
- **Q**: What is a Higher-Order Component?
- **A**: An HOC is an advanced React pattern used for reusing component logic. It is a pure function that takes a component as an argument and returns a new, enhanced component with injected props or behaviors.
- **Code Example**:
  ```jsx
  const EnhancedComponent = withAuth(MyComponent);
  ```

---

### 12. Error Boundaries in React
- **Q**: What are Error Boundaries?
- **A**: Error Boundaries are class-based React components that catch uncaught JavaScript runtime errors anywhere in their child component tree, log the errors, and render a fallback UI instead of allowing the entire application to crash (white-screen).

---

### 13. Port Changes in React (Create React App)
- **Q**: How do you change the default port of a React development server?
- **A**: By default, Create React App uses port 3000. You can change it by setting the `PORT` environment variable:
  - In a root `.env` file: `PORT=4000`
  - In your `package.json` scripts: `"start": "PORT=4000 react-scripts start"`

---

### 14. Webpack & Bundling
- **Q**: What is Webpack and why is it used?
- **A**: Webpack is a static module bundler for modern JavaScript applications. It analyzes your application's dependency graph (including JS, CSS, images, and other assets) and compiles/bundles them into small, optimized bundles suited for fast browser loading.

---

### 15. package.json vs package-lock.json
- **Q**: What is the difference between package.json and package-lock.json?
- **A**:
  - **package.json**: Holds project metadata, dev scripts, and a list of dependencies with version ranges (e.g., `"react": "^18.2.0"`).
  - **package-lock.json**: Automatically generated on package installation. It records the exact version of every package and transitive dependency installed, securing absolute reproducibility of dependencies across all developer machines and CI environments.

---

### 16. dependencies vs devDependencies
- **Q**: What is the difference between dependencies and devDependencies?
- **A**:
  - **dependencies**: Essential packages required to run the application in a production environment (e.g., `react`, `react-dom`, `axios`).
  - **devDependencies**: Packages only used during local development and build processes, excluded from production bundles (e.g., `typescript`, `jest`, `eslint`, `webpack`).

---

### 17. User Session Management in React
- **Q**: How do you implement session management in React?
- **A**: Since React is client-side, sessions are typically managed by:
  1. Storing a **JWT (JSON Web Token)** inside browser storage (`localStorage` / `sessionStorage`) or in secure HttpOnly cookies.
  2. Sending the token in the authentication header of subsequent API requests.
  3. Storing global user authentication states in React Context or Redux.

---

### 18. Redux & State Management Architecture
- **Q**: What are the core components of Redux's state architecture?
- **A**: Redux operates on three primary core concepts:
  1. **Store**: A single, global state tree representing the application's entire truth.
  2. **Action**: A plain JavaScript object that informs the store of an event, carrying a mandatory `type` and optional `payload` (e.g., `{ type: 'INCREMENT' }`).
  3. **Reducer**: A pure function `(state, action) => newState` that computes the next state without mutating the previous state.

---

### 19. React Context API vs Redux Trade-offs
- **Q**: How do you choose between Context API and Redux?
- **A**:
  - **Context API**: Ideal for low-frequency state updates like themes, language translation, or basic authentication. It requires no setup overhead or extra packages.
  - **Redux**: Best for complex, high-frequency updates, large shared states, and large development teams. It provides robust middleware, predictable time-travel debugging, and highly optimized subscription management.

---

### 20. Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)
- **Q**: What is the difference between SSR and CSR?
- **A**:
  - **Client-Side Rendering (CSR)**: The browser downloads a minimal HTML frame and a large JavaScript bundle. The browser's engine then builds the UI dynamically. This is faster for page transitions but slow on initial load and poor for SEO.
  - **Server-Side Rendering (SSR)**: The server pre-renders the HTML for a page dynamically upon request and sends fully formed markup to the client. This offers faster initial loads and excellent SEO, at the cost of higher server resource utilization.

---

### 21. TypeScript in React
- **Q**: What are the main benefits of TypeScript in React applications?
- **A**: TypeScript adds optional static typing to JavaScript. In React, it checks for bugs at compile-time (e.g., invalid props passed to a component), provides powerful code autocomplete, facilitates self-documenting code, and increases refactoring safety in large teams.

---

### 22. Stateful vs Stateless Components
- **Q**: What are stateful and stateless components?
- **A**:
  - **Stateful Components** (Smart / Container): Manage their own internal mutable states (using `useState` or `this.state`) and lifecycle methods. They typically handle data fetching and coordinate state.
  - **Stateless Components** (Dumb / Presentational): Hold no local state. They simply receive data through `props` and render the UI. They are highly modular, pure, and simple to test.

---

### 23. async/await vs Promises
- **Q**: How do async/await and Promises compare?
- **A**: Promises are standard JavaScript objects representing the eventual outcome of asynchronous operations. `async/await` is syntactic sugar on top of Promises, enabling asynchronous code to be written sequentially in a clean, synchronous-like syntax, resolving callback nesting issues and allowing standard `try/catch` block error handling.

---

### 24. useRef & DOM Manipulation
- **Q**: What is useRef and when is it used?
- **A**: `useRef` is a built-in React hook that returns a mutable reference object whose `.current` property is initialized with a given value. It is most commonly used to store a direct reference to a DOM node in functional components to manage focus, trigger text selection, or measure dimensions.
- **Code Example**:
  ```jsx
  const inputRef = useRef(null);
  const handleFocus = () => inputRef.current.focus();
  ```

---

### 25. Does useRef re-render the DOM?
- **Q**: Does changing a Ref's value trigger a component re-render?
- **A**: **No.** Modifying the `.current` property of a ref is a direct assignment that does not trigger a React component re-render. It is highly useful for storing and persisting values (such as timer IDs or previous state values) that are needed across renders but do not affect the visual UI.

---

### 26. Code Splitting & Lazy Loading (React.lazy)
- **Q**: How do you implement lazy loading / code splitting in React?
- **A**: Use `React.lazy()` along with `Suspense` to load components dynamically. This splits your code into separate bundles that are only loaded when required, reducing the initial bundle size and improving initial load time.
- **Code Example**:
  ```jsx
  import React, { Suspense } from 'react';
  const LazyComponent = React.lazy(() => import('./LazyComponent'));

  function App() {
    return (
      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
    );
  }
  ```

---

### 27. Diffing Algorithm
- **Q**: How does React's diffing algorithm work?
- **A**: The diffing algorithm compares the new Virtual DOM with the previous one. It operates on $O(N)$ time complexity using two main heuristic assumptions:
  1. Two elements of different types will produce different trees, so React will tear down the old tree and build a new one.
  2. The developer can hint at stable elements across renders using the unique `key` prop.

---

### 28. Key Prop under the hood
- **Q**: Why does React need the `key` prop under the hood?
- **A**: React uses the `key` prop to identify which items in a list have changed, been added, or been removed. Without unique keys, React compares children index-by-index, resulting in unnecessary DOM mutations and state bugs during list modifications (like inserting at the beginning of a list). Unique keys allow for highly efficient $O(1)$ matching.

---

### 29. Closure Trap in useEffect
- **Q**: Explain the closure trap in `useEffect` and how to resolve it.
- **A**: The closure trap (stale closure) occurs when a callback inside `useEffect` references a state or prop value but is not declared in the dependency array. The hook captures the value from the render when it was created, and subsequent state changes are ignored by the hook's callback function.
- **Code Example**:
  ```jsx
  // Stale Closure (always prints 0):
  useEffect(() => {
    const id = setInterval(() => console.log(count), 1000);
    return () => clearInterval(id);
  }, []);

  // Correct (re-runs timer when count changes):
  useEffect(() => {
    const id = setInterval(() => console.log(count), 1000);
    return () => clearInterval(id);
  }, [count]);
  ```

---

### 30. RSC vs Client Components
- **Q**: What is the difference between React Server Components (RSC) and Client Components?
- **A**:
  - **Server Components**: Rendered exclusively on the server, they do not ship JavaScript to the client (yielding zero bundle size contribution). They can access backend databases or file systems directly.
  - **Client Components**: Defined using `"use client"`. They are sent to the client, hydrated, and allow client-side interactivity (event listeners, states, context, and standard browser APIs).

---

### 31. use hook in React 19
- **Q**: What is the new `use` hook in React 19?
- **A**: The `use` hook is a new API that lets you read the value of a resource (like a Promise or Context) directly within the render method. Unlike other hooks, `use` can be called conditionally, inside loops, or inside conditional blocks (e.g., `if` statements).
- **Code Example**:
  ```jsx
  import { use } from 'react';

  function DataViewer({ dataPromise }) {
    // Resolves Promise directly in render phase:
    const data = use(dataPromise);
    return <div>{data.message}</div>;
  }
  ```

---

### 32. Redux Toolkit
- **Q**: What is Redux Toolkit (RTK) and why is it preferred?
- **A**: Redux Toolkit is the official, opinionated toolset for efficient Redux development. It simplifies store configuration, reduces boilerplate code, and incorporates `Immer` under the hood, allowing developers to write intuitive "mutative" state updates that are safely compiled into immutable state updates.
- **Code Example**:
  ```javascript
  import { createSlice } from '@reduxjs/toolkit';

  const counterSlice = createSlice({
    name: 'counter',
    initialState: { value: 0 },
    reducers: {
      increment: (state) => { state.value += 1; } // Mutative syntax made safe
    }
  });
  ```

---

### 33. Vite vs CRA
- **Q**: Why is Vite commonly preferred over Create React App (CRA)?
- **A**:
  - **CRA**: Relies on Webpack, which bundles the entire application before starting the development server, leading to slower load and update speeds as the app scales.
  - **Vite**: Uses native ES modules (ESM) to serve files on demand directly to the browser, and utilizes `esbuild` for dependency pre-bundling. This results in near-instant startup times and blazing-fast, modular Hot Module Replacement (HMR).

---

### 34. Pages vs App Router in Next.js
- **Q**: What is the difference between the Pages Router and App Router in Next.js?
- **A**:
  - **Pages Router**: Routes are mapped to files in the `pages` directory. Employs special lifecycle functions (`getServerSideProps`, `getStaticProps`) for data fetching.
  - **App Router**: Routes are mapped to files in the `app` directory. Built natively on React Server Components, supports nested layouts, and uses standard `async/await` data fetching directly inside server components.

---

### 35. Automatic Batching
- **Q**: What is automatic batching in React 18?
- **A**: Batching is when React groups multiple state updates into a single re-render for performance. Before React 18, React only batched updates inside React event handlers. In React 18, **Automatic Batching** groups all updates, including those inside Promises, `setTimeout`, or native event handlers.
- **Code Example**:
  ```javascript
  // Triggers only 1 re-render in React 18:
  setTimeout(() => {
    setCount(c => c + 1);
    setFlag(f => !f);
  }, 1000);
  ```

---

### 36. createElement vs cloneElement
- **Q**: What is the difference between `React.createElement` and `React.cloneElement`?
- **A**:
  - `React.createElement`: Creates a brand new React element from scratch using a component type, optional props, and children (compiled from JSX).
  - `React.cloneElement`: Copies an existing React element and returns a clone, allowing you to merge new props or override children while keeping the original structure.
- **Code Example**:
  ```jsx
  // createElement:
  React.createElement('div', { className: 'alert' }, 'Warning!');

  // cloneElement:
  React.cloneElement(childElement, { theme: 'dark' });
  ```

---

### 37. Named exports in React.lazy
- **Q**: Does `React.lazy` support named exports?
- **A**: **No.** `React.lazy` only supports default exports. If you need to lazy-load a component that is exported as a named export, you must import the named export in an intermediate module and re-export it as the default export.
- **Code Example**:
  ```javascript
  // Dynamic import workaround:
  const MyComponent = React.lazy(() => 
    import('./components').then(module => ({ default: module.MyComponent }))
  );
  ```

---

### 38. Logging HOC
- **Q**: Write a Higher-Order Component (HOC) that logs props to the console.
- **A**: A Higher-Order Component is a pattern where a function takes a component and returns a new enhanced component, useful for injecting cross-cutting concerns like logging.
- **Code Example**:
  ```jsx
  import React from 'react';

  const withLogging = (WrappedComponent) => {
    return (props) => {
      console.log('Component rendered with props:', props);
      return <WrappedComponent {...props} />;
    };
  };
  ```

---

### 39. useReducer Counter
- **Q**: Write a component that uses the `useReducer` hook.
- **A**: `useReducer` is excellent for managing complex state objects or when the next state depends on the previous state.
- **Code Example**:
  ```jsx
  import React, { useReducer } from 'react';

  const reducer = (state, action) => {
    switch (action.type) {
      case 'increment': return { count: state.count + 1 };
      case 'decrement': return { count: state.count - 1 };
      default: return state;
    }
  };

  function Counter() {
    const [state, dispatch] = useReducer(reducer, { count: 0 });
    return (
      <div>
        <p>Count: {state.count}</p>
        <button onClick={() => dispatch({ type: 'increment' })}>+</button>
        <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      </div>
    );
  }
  ```

---

### 40. useMemo Example
- **Q**: Write a component that uses the `useMemo` hook.
- **A**: `useMemo` is used to cache the result of an expensive calculation to prevent it from re-running on every render unless its dependencies change.
- **Code Example**:
  ```jsx
  import React, { useState, useMemo } from 'react';

  function ExpensiveCalc({ items }) {
    const [filter, setFilter] = useState('');

    const heavySum = useMemo(() => {
      console.log('Calculating heavy sum...');
      return items.reduce((acc, curr) => acc + curr.value, 0);
    }, [items]); // Recalculates only when items array changes

    return <div>Sum: {heavySum}</div>;
  }
  ```

---

### 41. Infinite Scroll
- **Q**: Write a component that implements infinite scrolling.
- **A**: Infinite scroll can be implemented by adding scroll event listeners to monitor when the user is close to the bottom of the page, or by using the modern **Intersection Observer API** to observe a loader element at the bottom of the list.
- **Code Example**:
  ```jsx
  import React, { useEffect, useRef } from 'react';

  function InfiniteList({ onLoadMore }) {
    const sentinelRef = useRef(null);

    useEffect(() => {
      const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          onLoadMore();
        }
      }, { threshold: 1.0 });

      if (sentinelRef.current) observer.observe(sentinelRef.current);
      return () => observer.disconnect();
    }, [onLoadMore]);

    return <div ref={sentinelRef}>Loading more...</div>;
  }
  ```

---

### 42. React Performance Optimizations
- **Q**: How do you optimize a React application to improve performance?
- **A**: Performance in React is optimized by preventing unnecessary renders and keeping bundle sizes minimal:
  1. **React.memo**: Memoize functional components to prevent re-renders when props haven't changed.
  2. **useMemo & useCallback**: Cache expensive computations and callback references.
  3. **Code Splitting**: Dynamic imports using `React.lazy` and `Suspense`.
  4. **Windowing / Virtualization**: Use libraries like `react-window` to render only the visible viewport items in extremely long lists.

---

## Practice Questions

### 1. Write a custom React hook `useFetch` to handle API requests and caching.

**Example Solution:**
```javascript
import { useState, useEffect } from "react";

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, [url]);

  return { data, loading };
}
```

### 2. Implement a search component with debounced text input.

**Example Solution:**
```javascript
function debounce(func, delay) {
  let timerId;
  return function(...args) {
    clearTimeout(timerId);
    timerId = setTimeout(() => func.apply(this, args), delay);
  };
}
```

