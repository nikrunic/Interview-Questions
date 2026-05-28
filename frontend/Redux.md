# Redux and State Management Interview Questions

This document contains interview questions focused on Redux, Zustand, Recoil, and modern state management.

## Basic (Easy)

### 1. What is Redux?
**Answer:** 
**The Core Concept:**
Redux is a predictable state container for JavaScript apps.

**Key Details:**
- It helps you write applications that behave consistently, run in different environments, and are easy to test.
- It uses a single centralized store for the entire application state.

**Example:** `const store = configureStore({ reducer: rootReducer })`

**Reference:** [Redux Docs](https://redux.js.org/)

---

### 2. What are the core principles of Redux?
**Answer:** 
**The Core Concept:**
Redux is built on three fundamental principles.

**Key Details:**
- Single source of truth: The state of your whole application is stored in an object tree within a single store.
- State is read-only: The only way to change the state is to emit an action.
- Changes are made with pure functions: To specify how the state tree is transformed by actions, you write pure reducers.

**Example:** `function reducer(state, action) { switch(action.type) { ... } }`

**Reference:** [Redux Principles](https://redux.js.org/understanding/thinking-in-redux/three-principles)

---

### 3. What is Zustand?
**Answer:** 
**The Core Concept:**
Zustand is a small, fast, and scalable bearbones state-management solution using simplified flux principles.

**Key Details:**
- It uses hooks to access state and does not require wrapping your app in context providers.
- It is much less boilerplate-heavy compared to traditional Redux.

**Example:** `const useStore = create((set) => ({ bears: 0, increase: () => set((state) => ({ bears: state.bears + 1 })) }))`

**Reference:** [Zustand GitHub](https://github.com/pmndrs/zustand)

---
\n## Additional Depth (Architectural Focus)\n
### 4. What are Redux Thunks and why are they needed?
**Answer:** 
**The Core Concept:**
Redux Thunk is a middleware that allows you to write action creators that return a function instead of an action object. This function receives the store's `dispatch` and `getState` methods as arguments.

**Key Details:**
- Because pure Redux reducers must be synchronous and devoid of side effects, Thunks provide a centralized place to handle asynchronous logic, such as making API calls, before dispatching the final success or failure actions.
- While Redux Saga uses generator functions for complex async flows, Thunks are simpler and represent the standard approach for basic async data fetching in Redux applications.

**Example:** 
`const fetchUser = () => async (dispatch) => { const res = await api(); dispatch({ type: 'SUCCESS', payload: res }); }`

**Reference:** [Documentation](https://redux.js.org/usage/writing-logic-thunks)

---

### 5. What is a Redux Middleware and how does it work under the hood?
**Answer:** 
**The Core Concept:**
A Redux Middleware provides a third-party extension point between dispatching an action and the moment it reaches the reducer. It is used for side effects, logging, crash reporting, routing, or asynchronous API calls.

**Key Details:**
- Uses a functional curry pattern under the hood: `store => next => action => { ... }`.
- **`store`**: The middleware has access to `dispatch` and `getState`.
- **`next`**: A function that passes control of the action to the next middleware in the pipeline, or finally to the reducer.
- **`action`**: The current action object being processed.

**Example:** 
```javascript
// A simple custom logging middleware
const loggerMiddleware = (store) => (next) => (action) => {
  console.log("Dispatching:", action);
  const result = next(action); // pass action to next middleware/reducer
  console.log("Next State:", store.getState());
  return result; // return result of next(action)
};
```

**Reference:** [Redux Middleware Guide](https://redux.js.org/understanding/history-and-design/middleware)

---

