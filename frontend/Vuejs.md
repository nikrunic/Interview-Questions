# Vue.js Interview Questions

This document contains interview questions focused on Vue.js, the progressive JavaScript framework.

## Basic Questions

### 1. What is Vue.js?
**Answer:** 
**The Core Concept:**
Vue.js is an open-source model–view–viewmodel (MVVM) front end JavaScript framework for building user interfaces and single-page applications.

**Key Details:**
- It is designed to be incrementally adoptable, meaning the core library is focused on the view layer only.
- Created by Evan You, it blends features of both Angular (directives) and React (virtual DOM).

**Example:** `const app = Vue.createApp({});`

**Reference:** [Vue.js Introduction](https://vuejs.org/guide/introduction.html)

---

---

---

### 2. What are Vue Directives?
**Answer:** 
**The Core Concept:**
Directives are special attributes with the `v-` prefix that apply reactive side effects to the DOM when their expression's value changes.

**Key Details:**
- They allow you to conditionally render elements, bind attributes, or iterate over lists easily in the template.
- Common directives include `v-if`, `v-for`, `v-bind`, and `v-model`.

**Example:** `<p v-if="isVisible">Now you see me</p>`

**Reference:** [Vue Directives](https://vuejs.org/api/built-in-directives.html)

---

---

---

### 3. What is the Vue instance lifecycle?
**Answer:** 
**The Core Concept:**
Every Vue component instance goes through a series of initialization steps when it's created, such as setting up data observation, compiling the template, mounting the instance to the DOM, and updating the DOM when data changes.

**Key Details:**
- You can run custom logic at specific stages using lifecycle hooks.
- Commonly used hooks are `mounted`, `created`, `updated`, and `unmounted`.

**Example:** `mounted() { console.log('Component is now mounted.') }`

**Reference:** [Vue Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html)

---

## Additional Depth (Architectural Focus)


---

---

### 4. What is the Composition API and how does it compare to the Options API?
**Answer:** 
**The Core Concept:**
The Composition API is a set of additive, function-based APIs introduced in Vue 3 that allow flexible composition of component logic. It is fundamentally an alternative to the traditional, object-based Options API.

**Key Details:**
- The Options API forces code organization by lifecycle hook or property type (data, methods, computed), which fragments features across a component and makes complex files difficult to read.
- The Composition API (using `setup()`) allows developers to group code logically by feature, making it highly readable and allowing for easy extraction of reusable logic into external composable functions.

**Example:** 
`import { ref, computed } from 'vue';`

**Reference:** [Documentation](https://vuejs.org/guide/extras/composition-api-faq.html)

---

---

---

### 5. How does Vue 3's reactivity system work under the hood?
**Answer:** 
**The Core Concept:**
Vue 3 overhauled its reactivity system by replacing Object.defineProperty with ES6 Proxies. This allows Vue to seamlessly intercept and track operations like property access, assignment, and deletion on reactive objects without needing to recursively walk the object on initialization.

**Key Details:**
- Proxies solve major caveats from Vue 2, such as the inability to detect property additions/deletions or array index mutations.
- Because Proxies are a native browser feature, the memory footprint is smaller and initialization is faster, though they do not support IE11.

**Example:** 
`const state = reactive({ count: 0 }); // Returns a Proxy object`

**Reference:** [Documentation](https://vuejs.org/guide/extras/reactivity-in-depth.html)

---

---

---

### 6. What is the difference between `v-if` and `v-show`?
**Answer:** 
**The Core Concept:**
Both directives conditionally display elements, but they do so fundamentally differently. `v-if` conditionally renders the element (destroying and recreating the DOM node), while `v-show` simply toggles the CSS `display` property.

**Key Details:**
- Use `v-if` when the condition rarely changes, as toggling it incurs higher rendering costs.
- Use `v-show` for elements that toggle frequently (like tabs or accordions), as the initial render cost is higher but subsequent toggles are extremely cheap.

**Example:** 
`<div v-if="isLoaded">Full DOM mount</div> <div v-show="isVisible">CSS display toggle</div>`

**Reference:** [Documentation](https://vuejs.org/guide/essentials/conditional.html#v-if-vs-v-show)

---

---

---

### 7. What is the difference between `computed` properties and `methods`?
**Answer:** 
**The Core Concept:**
Computed properties are cached based on their reactive dependencies, meaning they only re-evaluate when a dependency changes. Methods are invoked and executed every time a re-render occurs.

**Key Details:**
- If you have an expensive calculation (like filtering a large array), a computed property prevents unnecessary recalculations, saving CPU cycles.
- Computed properties cannot accept arguments, whereas methods can. For parameterized logic, you must use a method.

**Example:** 
`const doubleCount = computed(() => count.value * 2);`

**Reference:** [Documentation](https://vuejs.org/guide/essentials/computed.html)

---

---

---

### 8. How do `watch` and `watchEffect` differ in the Composition API?
**Answer:** 
**The Core Concept:**
`watch` allows you to observe specific reactive data sources and execute a callback when they change, providing access to both the old and new values. `watchEffect` automatically tracks every reactive property accessed synchronously within its callback and re-runs when any of them change.

**Key Details:**
- `watch` is explicit and lazy by default (it only runs when the watched source changes).
- `watchEffect` is implicit and runs immediately upon creation to collect its dependencies, making it ideal for fetching data when multiple parameters change.

**Example:** 
`watch(count, (newVal, oldVal) => { console.log(newVal); }); watchEffect(() => console.log(count.value));`

**Reference:** [Documentation](https://vuejs.org/guide/essentials/watchers.html)

---

---

## Intermediate Questions

---

### 9. How does Vue handle parent-to-child and child-to-parent communication?
**Answer:** 
**The Core Concept:**
Vue strictly enforces a one-way data flow. Parents pass data down to children using `props`. Children send messages back to parents by emitting custom events using `$emit`.

**Key Details:**
- Props are read-only in the child component. Attempting to mutate a prop directly will trigger a Vue warning in the console.
- When a child needs to update a parent's state, it emits an event, and the parent listens to that event using `v-on` (or `@`) to update its own state.

**Example:** 
`// Child: emit('update', newValue); // Parent: <Child @update="handleUpdate" />`

**Reference:** [Documentation](https://vuejs.org/guide/components/events.html)

---

---

---

### 10. What is Provide / Inject?
**Answer:** 
**The Core Concept:**
Provide and Inject solve the 'prop drilling' problem in Vue by allowing an ancestor component to serve as a dependency injector for all its descendants, regardless of how deep the component tree goes.

**Key Details:**
- The parent uses `provide()` to expose data, and any descendant can use `inject()` to grab that data without intermediate components needing to pass it down.
- To maintain reactivity, you should provide `ref` or `reactive` objects. However, mutations should ideally be kept within the provider to ensure predictable data flow.

**Example:** 
`provide('theme', themeRef); const theme = inject('theme');`

**Reference:** [Documentation](https://vuejs.org/guide/components/provide-inject.html)

---

---

---

### 11. What is Pinia and how does it differ from Vuex?
**Answer:** 
**The Core Concept:**
Pinia is the modern, official state management library for Vue, succeeding Vuex. It provides a simpler API, full TypeScript inference, and eliminates the need for mutations.

**Key Details:**
- In Pinia, actions can be synchronous or asynchronous, directly mutating the state, entirely bypassing the verbose `commit` and `mutation` pattern of Vuex.
- Pinia stores are modular by design and do not require a single global nested store tree, enabling better code-splitting and performance.

**Example:** 
`export const useCounterStore = defineStore('counter', { state: () => ({ count: 0 }) });`

**Reference:** [Documentation](https://pinia.vuejs.org/introduction.html)

---

---

---

### 12. How does Scoped CSS work in Vue Single-File Components (SFCs)?
**Answer:** 
**The Core Concept:**
When a `<style>` tag has the `scoped` attribute, its CSS applies exclusively to elements of the current component. Vue achieves this by appending a unique data attribute (like `data-v-f3f3eg9`) to the component's HTML elements and CSS selectors.

**Key Details:**
- This provides encapsulated styling without the overhead of CSS-in-JS or BEM naming conventions.
- If you need a scoped style to affect deep child components, you must use the `:deep()` pseudo-class to pierce the scope boundary.

**Example:** 
`<style scoped> .title { color: red; } :deep(.child-el) { color: blue; } </style>`

**Reference:** [Documentation](https://vuejs.org/api/sfc-css-features.html#scoped-css)

---

---

---

### 13. What are Slots and Scoped Slots?
**Answer:** 
**The Core Concept:**
Slots are a mechanism for component content distribution, allowing a parent to inject custom HTML into a child component's template. Scoped slots take this further by allowing the child component to pass data back up to the injected slot content.

**Key Details:**
- Named slots allow multiple insertion points within a single component using the `<template #name>` syntax.
- Scoped slots are essentially functions that the parent passes to the child; the child calls them with data, rendering the parent's custom UI with the child's internal state.

**Example:** 
`// Child: <slot :item="item"></slot> // Parent: <template #default="{ item }">{{ item.name }}</template>`

**Reference:** [Documentation](https://vuejs.org/guide/components/slots.html)

---

---

---

### 14. What is the `<Teleport>` component?
**Answer:** 
**The Core Concept:**
Teleport is a built-in Vue component that allows you to render a part of a component's template into a DOM node that exists outside the DOM hierarchy of that component.

**Key Details:**
- It is primarily used for Modals, Tooltips, and Dropdowns where CSS constraints (like `overflow: hidden` or `z-index` stacking contexts) in the parent would otherwise clip or hide the overlay element.
- Despite being rendered elsewhere in the DOM, the teleported element remains part of the Vue component tree, retaining reactivity and component context (like provide/inject).

**Example:** 
`<Teleport to="body"> <div class="modal">...</div> </Teleport>`

**Reference:** [Documentation](https://vuejs.org/guide/built-ins/teleport.html)

---

---

---

### 15. What is `<Suspense>` in Vue 3?
**Answer:** 
**The Core Concept:**
Suspense is a built-in component that orchestrates async dependencies in the component tree. It renders a fallback UI while waiting for nested asynchronous components (or components with a top-level `await` in `<script setup>`) to resolve.

**Key Details:**
- It handles multiple async dependencies concurrently, only replacing the fallback UI when the entire tree has resolved.
- While highly powerful for loading states and data fetching, Suspense is still officially marked as an experimental feature in Vue 3.

**Example:** 
`<Suspense> <template #default><AsyncComp /></template> <template #fallback><Spinner /></template> </Suspense>`

**Reference:** [Documentation](https://vuejs.org/guide/built-ins/suspense.html)

---

---

---

## Intermediate Questions

### 16. How does `v-model` work on custom components in Vue 3?
**Answer:** 
**The Core Concept:**
In Vue 3, `v-model` is syntactic sugar for passing a `modelValue` prop and listening to an `update:modelValue` event. This simplifies two-way data binding on custom inputs.

**Key Details:**
- Unlike Vue 2, which used `value` and `input`, Vue 3 allows multiple `v-model` bindings on a single component by passing an argument (e.g., `v-model:title="pageTitle"`).
- Modifiers can also be added, and the child component can access them via the `modelModifiers` prop.

**Example:** 
`<Child v-model="text" /> // equivalent to :modelValue="text" @update:modelValue="text = $event"`

**Reference:** [Documentation](https://vuejs.org/guide/components/v-model.html)

---

---

## Expert Questions

---

### 17. Why were Mixins deprecated in favor of Composables (Composition API)?
**Answer:** 
**The Core Concept:**
Mixins were the primary way to reuse logic in Vue 2, but they suffered from severe drawbacks: property name collisions, unclear sources of properties (implicit dependencies), and poor TypeScript support.

**Key Details:**
- Composables (using the Composition API) solve this by utilizing standard JavaScript functions that return explicit reactive state and methods.
- With Composables, IDEs can accurately trace variables, naming conflicts are resolved locally via destructuring, and logic composition becomes highly flexible.

**Example:** 
`const { x, y } = useMouse(); // Source of variables is explicitly clear`

**Reference:** [Documentation](https://vuejs.org/guide/reusability/composables.html#vs-mixins)

---

---

---

### 18. Why is the `key` attribute required in `v-for`?
**Answer:** 
**The Core Concept:**
The `key` attribute provides Vue's virtual DOM diffing algorithm with a unique identifier for each node in a list. This allows Vue to track elements precisely during updates, additions, and deletions.

**Key Details:**
- Without keys, Vue uses an 'in-place patch' strategy, trying to reuse existing DOM elements and updating their content. This causes critical bugs if list items contain complex nested state or temporary DOM state (like input focus).
- The key must be a unique, stable primitive (string or number), typically a database ID, and never the array index.

**Example:** 
`<li v-for="item in items" :key="item.id">{{ item.name }}</li>`

**Reference:** [Documentation](https://vuejs.org/guide/essentials/list.html#maintaining-state-with-key)

---

---

---

### 19. What does the `<keep-alive>` component do?
**Answer:** 
**The Core Concept:**
`<keep-alive>` is a built-in component that caches dynamically toggled components instead of destroying them. When a cached component is toggled back into view, its state and DOM are restored instantly.

**Key Details:**
- It introduces two special lifecycle hooks: `activated` and `deactivated`, as `mounted` and `unmounted` are not called during toggling.
- It accepts `include` and `exclude` props (using strings, regex, or arrays) to specifically target which components should be cached, preventing excessive memory usage.

**Example:** 
`<keep-alive include="TabA,TabB"> <component :is="currentTab" /> </keep-alive>`

**Reference:** [Documentation](https://vuejs.org/guide/built-ins/keep-alive.html)

---

---

---

### 20. What is `nextTick` in Vue?
**Answer:** 
**The Core Concept:**
`nextTick` is a utility function that delays the execution of a callback until after the next DOM update cycle. It returns a Promise that resolves when the DOM has been updated.

**Key Details:**
- Vue updates the DOM asynchronously. When you mutate reactive state, the DOM is not updated immediately. `nextTick` is required if you need to query the DOM immediately after changing data that affects the layout.
- It is heavily used in testing and complex UI interactions, such as focusing an input element the moment it becomes visible via `v-if`.

**Example:** 
`message.value = 'updated'; await nextTick(); console.log(document.getElementById('msg').textContent);`

**Reference:** [Documentation](https://vuejs.org/api/general.html#nexttick)

---

---

---

### 21. What are Vue Router Navigation Guards?
**Answer:** 
**The Core Concept:**
Navigation guards are hooks provided by Vue Router that allow you to intercept and control route transitions. They can be defined globally, per-route, or within components.

**Key Details:**
- They are primarily used to enforce authentication, preventing unauthenticated users from accessing protected routes, or fetching data before a view is rendered.
- A guard function receives `to`, `from`, and `next` arguments. Returning `false` aborts the navigation, while returning a route path redirects the user.

**Example:** 
`router.beforeEach((to, from) => { if (to.meta.requiresAuth && !auth) return '/login'; });`

**Reference:** [Documentation](https://router.vuejs.org/guide/advanced/navigation-guards.html)

---

---

---

### 22. How do Custom Directives work in Vue 3?
**Answer:** 
**The Core Concept:**
Custom directives allow developers to encapsulate low-level DOM access and manipulation into reusable attributes. They are defined using lifecycle hooks similar to components (e.g., `mounted`, `updated`).

**Key Details:**
- While components are for generating and managing the DOM tree, custom directives are strictly for direct, low-level DOM manipulations that are otherwise difficult to achieve declaratively.
- A classic use case is a `v-focus` directive that automatically calls `.focus()` on an input element when it is mounted.

**Example:** 
`const vFocus = { mounted: (el) => el.focus() };`

**Reference:** [Documentation](https://vuejs.org/guide/reusability/custom-directives.html)

---

---

---

### 23. What is the Virtual DOM and how does Vue optimize it?
**Answer:** 
**The Core Concept:**
The Virtual DOM is a lightweight JavaScript representation of the actual DOM. Vue renders components into the Virtual DOM, compares (diffs) the new tree against the old tree, and applies only the minimum necessary changes to the real DOM.

**Key Details:**
- Vue 3 significantly optimized this process through compiler-informed Virtual DOM. The compiler statically analyzes the template, identifying static elements that never change and hoisting them out of the render loop.
- It also provides patch flags to dynamic elements, telling the diffing algorithm exactly what changed (e.g., text, class, or props), skipping full node comparisons.

**Example:** 
`Static hoisting prevents unnecessary node creation on every re-render.`

**Reference:** [Documentation](https://vuejs.org/guide/extras/rendering-mechanism.html)

---

---

---

### 24. How do you handle global state without Pinia/Vuex?
**Answer:** 
**The Core Concept:**
In Vue 3, you can easily create lightweight global state management by exporting a reactive object from an external JavaScript/TypeScript module.

**Key Details:**
- Because `reactive()` and `ref()` are not tightly coupled to components, they retain reactivity anywhere in the application.
- While this is suitable for small applications, it lacks the developer tools integration, SSR safety, and structural guidelines (actions, getters) provided by dedicated libraries like Pinia.

**Example:** 
`export const store = reactive({ count: 0 }); // Use directly in any component`

**Reference:** [Documentation](https://vuejs.org/guide/scaling-up/state-management.html)

---

---

## Practice Questions

---

### 1. Create a custom reusable Composition API helper hook `useLocalStorage` in Vue 3.

**Example Solution:**
```typescript
import { ref, watch, Ref } from "vue";

export function useLocalStorage<T>(key: string, defaultValue: T): Ref<T> {
  const storedValue = localStorage.getItem(key);
  const data = ref<T>(storedValue ? JSON.parse(storedValue) : defaultValue) as Ref<T>;

  watch(data, (newValue) => {
    localStorage.setItem(key, JSON.stringify(newValue));
  }, { deep: true });

  return data;
}
```

---

### 2. Build a debounced search input component using `<script setup>` in Vue 3.

**Example Solution:**
```html
<script setup lang="ts">
import { ref, watch } from "vue";

const search = ref("");
const debouncedSearch = ref("");
let timeoutId: ReturnType<typeof setTimeout>;

watch(search, (newVal) => {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    debouncedSearch.value = newVal;
  }, 300);
});
</script>

<template>
  <div class="search-box">
    <input v-model="search" placeholder="Type to search..." class="border p-2 rounded" />
    <p>Searching for: {{ debouncedSearch }}</p>
  </div>
</template>
```

---

## Expert Questions

## Practice Questions

### 1. Create a custom reusable Composition API helper hook `useLocalStorage` in Vue 3.

**Example Solution:**
```typescript
import { ref, watch, Ref } from "vue";

export function useLocalStorage<T>(key: string, defaultValue: T): Ref<T> {
  const storedValue = localStorage.getItem(key);
  const data = ref<T>(storedValue ? JSON.parse(storedValue) : defaultValue) as Ref<T>;

  watch(data, (newValue) => {
    localStorage.setItem(key, JSON.stringify(newValue));
  }, { deep: true });

  return data;
}
```

### 2. Build a debounced search input component using `<script setup>` in Vue 3.

**Example Solution:**
```html
<script setup lang="ts">
import { ref, watch } from "vue";

const search = ref("");
const debouncedSearch = ref("");
let timeoutId: ReturnType<typeof setTimeout>;

watch(search, (newVal) => {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    debouncedSearch.value = newVal;
  }, 300);
});
</script>

<template>
  <div class="search-box">
    <input v-model="search" placeholder="Type to search..." class="border p-2 rounded" />
    <p>Searching for: {{ debouncedSearch }}</p>
  </div>
</template>
```

### 3. Create a Vue 3 custom directive managing element auto-focus behaviors.

**Example Solution:**
```typescript
const vFocus = {
  mounted: (el: HTMLElement) => {
    el.focus();
  }
};
// Use as: <input v-focus />
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Vue.js Reactive Framework application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Vue.js Reactive Framework operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Vue.js Reactive Framework configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Vue.js Reactive Framework event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Vue.js Reactive Framework with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Vue.js Reactive Framework performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Vue.js Reactive Framework failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Vue.js Reactive Framework data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Vue.js Reactive Framework state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Vue.js Reactive Framework logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Vue.js Reactive Framework files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Vue.js Reactive Framework connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Vue.js Reactive Framework.

*(Challenge question for self-study and practical project implementation.)*

