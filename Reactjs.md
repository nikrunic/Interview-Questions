# React.js Interview Questions

This document contains a comprehensive list of React.js interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is React.js?
**Answer:** React is an open-source, declarative, efficient, and flexible JavaScript library for building user interfaces. It is maintained by Meta (Facebook).
**Example:** `function App() { return <h1>Hello, React!</h1>; }`
**Reference:** [React Official Docs - Describing the UI](https://react.dev/learn/describing-the-ui)

### 2. What is JSX?
**Answer:** JSX is a syntax extension for JavaScript. It allows developers to write HTML-like structures in the same file as JavaScript code, making it easier to write and understand React components.
**Example:** `const element = <h1>Hello, world!</h1>;`
**Reference:** [React Docs - Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx)

### 3. What are Components in React?
**Answer:** Components are the building blocks of any React application. A component is a JavaScript class or function that optionally accepts inputs (props) and returns a React element that describes how a section of the UI should appear.
**Example:** `function Welcome(props) { return <h1>Hello, {props.name}</h1>; }`
**Reference:** [React Docs - Your First Component](https://react.dev/learn/your-first-component)

### 4. What are Props?
**Answer:** Props (short for "properties") are read-only inputs passed from a parent component to a child component. They allow components to be dynamic and reusable.
**Example:** `<Welcome name="Sara" />`
**Reference:** [React Docs - Passing Props to a Component](https://react.dev/learn/passing-props-to-a-component)

### 5. What is State in React?
**Answer:** State is an object that holds data that may change over the lifetime of a component. When state changes, React re-renders the component to reflect the new state.
**Example:** `const [count, setCount] = useState(0);`
**Reference:** [React Docs - State: A Component's Memory](https://react.dev/learn/state-a-components-memory)

### 6. What is the Virtual DOM?
**Answer:** The Virtual DOM is an in-memory representation of the real DOM. React uses it to calculate the most efficient way to update the browser's DOM by comparing the virtual DOM with a snapshot of the previous virtual DOM (Diffing).
**Example:** N/A (Internal concept).
**Reference:** [React Legacy Docs - Virtual DOM and Internals](https://legacy.reactjs.org/docs/faq-internals.html)

### 7. What is a Hook in React?
**Answer:** Hooks are functions that let you "hook into" React state and lifecycle features from functional components. They were introduced in React 16.8.
**Example:** `useState`, `useEffect`, `useContext`.
**Reference:** [React Docs - Built-in React Hooks](https://react.dev/reference/react)


## Medium (30%)

### 8. What is the difference between State and Props?
**Answer:** Props are passed *to* the component by its parent and are immutable (read-only). State is managed *within* the component and can be updated using a setter function (like `setCount`), triggering a re-render.
**Example:** Props are function arguments, State is local variables.
**Reference:** [React Docs - State vs Props](https://react.dev/learn/state-a-components-memory#state-is-isolated-and-private)

### 9. Explain `useEffect` hook.
**Answer:** `useEffect` lets you perform side effects in functional components. It serves the same purpose as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` in React class components.
**Example:** `useEffect(() => { document.title = \`Count: \${count}\`; }, [count]);`
**Reference:** [React Docs - Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects)

### 10. What are the rules of Hooks?
**Answer:** 1. Only call Hooks at the top level of a component (don't call them inside loops, conditions, or nested functions). 2. Only call Hooks from React function components or custom Hooks.
**Example:** Correct: `function MyComp() { const [a, setA] = useState(0); ... }`
**Reference:** [React Docs - Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)

### 11. What is Context API?
**Answer:** The Context API provides a way to pass data through the component tree without having to pass props down manually at every level (prop drilling).
**Example:** `const ThemeContext = createContext('light'); ... <ThemeContext.Provider value="dark">`
**Reference:** [React Docs - Passing Data Deeply with Context](https://react.dev/learn/passing-data-deeply-with-context)

### 12. What is Prop Drilling?
**Answer:** Prop drilling is the process of passing data from a higher-level component down to a deeply nested child component through multiple intermediate components that do not need the data themselves.
**Example:** App -> Navbar -> UserMenu -> Avatar (Avatar needs the data, but Navbar and UserMenu have to pass it).
**Reference:** [React Docs - Passing Data Deeply](https://react.dev/learn/passing-data-deeply-with-context#the-problem-with-passing-props)

### 13. What are Controlled vs Uncontrolled Components?
**Answer:** A controlled component's form data is handled by the React component's state. An uncontrolled component's form data is handled by the DOM itself using refs.
**Example:** Controlled: `<input value={stateValue} onChange={handleChange} />`
**Reference:** [React Docs - Controlled and uncontrolled components](https://react.dev/learn/sharing-state-between-components#controlled-and-uncontrolled-components)

### 14. What are Refs in React?
**Answer:** Refs (`useRef`) provide a way to access DOM nodes or React elements created in the render method directly. They can also be used to store a mutable value that does not cause a re-render when updated.
**Example:** `const inputRef = useRef(null); inputRef.current.focus();`
**Reference:** [React Docs - Referencing Values with Refs](https://react.dev/learn/referencing-values-with-refs)


## Hard (50%)

### 15. How does React's Reconciliation algorithm work?
**Answer:** React uses a heuristic O(n) algorithm called Diffing. It assumes: 1) Two elements of different types will produce different trees. 2) The developer can hint at which child elements may be stable across different renders with a `key` prop.
**Example:** When an `<li>` element is added to a list, React uses the `key` to identify if items have moved, preventing unnecessary re-renders of the entire list.
**Reference:** [React Legacy Docs - Reconciliation](https://legacy.reactjs.org/docs/reconciliation.html)

### 16. What is `useMemo` and when should you use it?
**Answer:** `useMemo` is a React Hook that lets you cache the result of a calculation between re-renders. You should use it to optimize expensive calculations that do not need to run on every render unless their dependencies change.
**Example:** `const cachedValue = useMemo(() => calculateExpensiveValue(a, b), [a, b]);`
**Reference:** [React Docs - useMemo](https://react.dev/reference/react/useMemo)

### 17. What is `useCallback` and how is it different from `useMemo`?
**Answer:** `useCallback` is a React Hook that lets you cache a function definition between re-renders. `useMemo` caches a *value*, while `useCallback` caches a *function*.
**Example:** `const handleSubmit = useCallback(() => { post(url, data); }, [url, data]);`
**Reference:** [React Docs - useCallback](https://react.dev/reference/react/useCallback)

### 18. What are Higher-Order Components (HOC)?
**Answer:** An HOC is an advanced technique for reusing component logic. It is a function that takes a component and returns a new component, injecting additional props or functionality.
**Example:** `const EnhancedComponent = withRouter(MyComponent);`
**Reference:** [React Legacy Docs - Higher-Order Components](https://legacy.reactjs.org/docs/higher-order-components.html)

### 19. What is React Fiber?
**Answer:** Fiber is the new reconciliation engine in React 16. Its main goal is to enable incremental rendering of the virtual DOM. It allows React to pause, abort, or reuse work as new updates come in, prioritizing layout/animations over less important data fetches.
**Example:** N/A (Internal architecture).
**Reference:** [GitHub - React Fiber Architecture](https://github.com/acdlite/react-fiber-architecture)

### 20. How do you handle errors in React? (Error Boundaries)
**Answer:** Error boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI instead of the component tree that crashed. They are currently only available as Class Components.
**Example:** `class ErrorBoundary extends React.Component { componentDidCatch(error, info) { ... } }`
**Reference:** [React Docs - Catching Rendering Errors](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)

### 21. What is the use of `React.memo`?
**Answer:** `React.memo` is a higher-order component. If your component renders the same result given the same props, you can wrap it in a call to `React.memo` for a performance boost by memoizing the result. React skips rendering the component and reuses the last rendered result.
**Example:** `const MyComponent = React.memo(function MyComponent(props) { ... });`
**Reference:** [React Docs - memo](https://react.dev/reference/react/memo)

### 22. Explain `useReducer` and when it is preferable to `useState`.
**Answer:** `useReducer` is an alternative to `useState` for complex state logic that involves multiple sub-values or when the next state depends on the previous one. It takes a reducer function and an initial state, returning the current state and a `dispatch` function.
**Example:** `const [state, dispatch] = useReducer(reducer, initialState);`
**Reference:** [React Docs - Extracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer)

### 23. What are Custom Hooks?
**Answer:** Custom Hooks are JavaScript functions whose names start with "use" and that may call other Hooks. They allow you to extract component logic into reusable functions.
**Example:** `function useWindowWidth() { const [width, setWidth] = useState(window.innerWidth); ... return width; }`
**Reference:** [React Docs - Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)

### 24. How do you prevent a component from rendering?
**Answer:** In functional components, you can return `null` from the render function. To prevent re-renders when props haven't changed, wrap the component in `React.memo`.
**Example:** `if (!isVisible) return null;`
**Reference:** [React Docs - Conditional Rendering](https://react.dev/learn/conditional-rendering)

### 25. What is Portals in React?
**Answer:** Portals provide a first-class way to render children into a DOM node that exists outside the DOM hierarchy of the parent component. Useful for modals, tooltips, and popovers.
**Example:** `ReactDOM.createPortal(child, container)`
**Reference:** [React Docs - createPortal](https://react.dev/reference/react-dom/createPortal)
