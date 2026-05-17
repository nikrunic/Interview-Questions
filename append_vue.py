import os

vue_qna = [
    ("How does Vue 3's reactivity system work under the hood?",
     "Vue 3 overhauled its reactivity system by replacing Object.defineProperty with ES6 Proxies. This allows Vue to seamlessly intercept and track operations like property access, assignment, and deletion on reactive objects without needing to recursively walk the object on initialization.",
     ["Proxies solve major caveats from Vue 2, such as the inability to detect property additions/deletions or array index mutations.", "Because Proxies are a native browser feature, the memory footprint is smaller and initialization is faster, though they do not support IE11."],
     "const state = reactive({ count: 0 }); // Returns a Proxy object",
     "https://vuejs.org/guide/extras/reactivity-in-depth.html"),
    
    ("What is the difference between `v-if` and `v-show`?",
     "Both directives conditionally display elements, but they do so fundamentally differently. `v-if` conditionally renders the element (destroying and recreating the DOM node), while `v-show` simply toggles the CSS `display` property.",
     ["Use `v-if` when the condition rarely changes, as toggling it incurs higher rendering costs.", "Use `v-show` for elements that toggle frequently (like tabs or accordions), as the initial render cost is higher but subsequent toggles are extremely cheap."],
     "<div v-if=\"isLoaded\">Full DOM mount</div> <div v-show=\"isVisible\">CSS display toggle</div>",
     "https://vuejs.org/guide/essentials/conditional.html#v-if-vs-v-show"),
     
    ("What is the difference between `computed` properties and `methods`?",
     "Computed properties are cached based on their reactive dependencies, meaning they only re-evaluate when a dependency changes. Methods are invoked and executed every time a re-render occurs.",
     ["If you have an expensive calculation (like filtering a large array), a computed property prevents unnecessary recalculations, saving CPU cycles.", "Computed properties cannot accept arguments, whereas methods can. For parameterized logic, you must use a method."],
     "const doubleCount = computed(() => count.value * 2);",
     "https://vuejs.org/guide/essentials/computed.html"),
     
    ("How do `watch` and `watchEffect` differ in the Composition API?",
     "`watch` allows you to observe specific reactive data sources and execute a callback when they change, providing access to both the old and new values. `watchEffect` automatically tracks every reactive property accessed synchronously within its callback and re-runs when any of them change.",
     ["`watch` is explicit and lazy by default (it only runs when the watched source changes).", "`watchEffect` is implicit and runs immediately upon creation to collect its dependencies, making it ideal for fetching data when multiple parameters change."],
     "watch(count, (newVal, oldVal) => { console.log(newVal); }); watchEffect(() => console.log(count.value));",
     "https://vuejs.org/guide/essentials/watchers.html"),
     
    ("How does Vue handle parent-to-child and child-to-parent communication?",
     "Vue strictly enforces a one-way data flow. Parents pass data down to children using `props`. Children send messages back to parents by emitting custom events using `$emit`.",
     ["Props are read-only in the child component. Attempting to mutate a prop directly will trigger a Vue warning in the console.", "When a child needs to update a parent's state, it emits an event, and the parent listens to that event using `v-on` (or `@`) to update its own state."],
     "// Child: emit('update', newValue); // Parent: <Child @update=\"handleUpdate\" />",
     "https://vuejs.org/guide/components/events.html"),
     
    ("What is Provide / Inject?",
     "Provide and Inject solve the 'prop drilling' problem in Vue by allowing an ancestor component to serve as a dependency injector for all its descendants, regardless of how deep the component tree goes.",
     ["The parent uses `provide()` to expose data, and any descendant can use `inject()` to grab that data without intermediate components needing to pass it down.", "To maintain reactivity, you should provide `ref` or `reactive` objects. However, mutations should ideally be kept within the provider to ensure predictable data flow."],
     "provide('theme', themeRef); const theme = inject('theme');",
     "https://vuejs.org/guide/components/provide-inject.html"),
     
    ("What is Pinia and how does it differ from Vuex?",
     "Pinia is the modern, official state management library for Vue, succeeding Vuex. It provides a simpler API, full TypeScript inference, and eliminates the need for mutations.",
     ["In Pinia, actions can be synchronous or asynchronous, directly mutating the state, entirely bypassing the verbose `commit` and `mutation` pattern of Vuex.", "Pinia stores are modular by design and do not require a single global nested store tree, enabling better code-splitting and performance."],
     "export const useCounterStore = defineStore('counter', { state: () => ({ count: 0 }) });",
     "https://pinia.vuejs.org/introduction.html"),
     
    ("How does Scoped CSS work in Vue Single-File Components (SFCs)?",
     "When a `<style>` tag has the `scoped` attribute, its CSS applies exclusively to elements of the current component. Vue achieves this by appending a unique data attribute (like `data-v-f3f3eg9`) to the component's HTML elements and CSS selectors.",
     ["This provides encapsulated styling without the overhead of CSS-in-JS or BEM naming conventions.", "If you need a scoped style to affect deep child components, you must use the `:deep()` pseudo-class to pierce the scope boundary."],
     "<style scoped> .title { color: red; } :deep(.child-el) { color: blue; } </style>",
     "https://vuejs.org/api/sfc-css-features.html#scoped-css"),
     
    ("What are Slots and Scoped Slots?",
     "Slots are a mechanism for component content distribution, allowing a parent to inject custom HTML into a child component's template. Scoped slots take this further by allowing the child component to pass data back up to the injected slot content.",
     ["Named slots allow multiple insertion points within a single component using the `<template #name>` syntax.", "Scoped slots are essentially functions that the parent passes to the child; the child calls them with data, rendering the parent's custom UI with the child's internal state."],
     "// Child: <slot :item=\"item\"></slot> // Parent: <template #default=\"{ item }\">{{ item.name }}</template>",
     "https://vuejs.org/guide/components/slots.html"),
     
    ("What is the `<Teleport>` component?",
     "Teleport is a built-in Vue component that allows you to render a part of a component's template into a DOM node that exists outside the DOM hierarchy of that component.",
     ["It is primarily used for Modals, Tooltips, and Dropdowns where CSS constraints (like `overflow: hidden` or `z-index` stacking contexts) in the parent would otherwise clip or hide the overlay element.", "Despite being rendered elsewhere in the DOM, the teleported element remains part of the Vue component tree, retaining reactivity and component context (like provide/inject)."],
     "<Teleport to=\"body\"> <div class=\"modal\">...</div> </Teleport>",
     "https://vuejs.org/guide/built-ins/teleport.html"),
     
    ("What is `<Suspense>` in Vue 3?",
     "Suspense is a built-in component that orchestrates async dependencies in the component tree. It renders a fallback UI while waiting for nested asynchronous components (or components with a top-level `await` in `<script setup>`) to resolve.",
     ["It handles multiple async dependencies concurrently, only replacing the fallback UI when the entire tree has resolved.", "While highly powerful for loading states and data fetching, Suspense is still officially marked as an experimental feature in Vue 3."],
     "<Suspense> <template #default><AsyncComp /></template> <template #fallback><Spinner /></template> </Suspense>",
     "https://vuejs.org/guide/built-ins/suspense.html"),
     
    ("How does `v-model` work on custom components in Vue 3?",
     "In Vue 3, `v-model` is syntactic sugar for passing a `modelValue` prop and listening to an `update:modelValue` event. This simplifies two-way data binding on custom inputs.",
     ["Unlike Vue 2, which used `value` and `input`, Vue 3 allows multiple `v-model` bindings on a single component by passing an argument (e.g., `v-model:title=\"pageTitle\"`).", "Modifiers can also be added, and the child component can access them via the `modelModifiers` prop."],
     "<Child v-model=\"text\" /> // equivalent to :modelValue=\"text\" @update:modelValue=\"text = $event\"",
     "https://vuejs.org/guide/components/v-model.html"),
     
    ("Why were Mixins deprecated in favor of Composables (Composition API)?",
     "Mixins were the primary way to reuse logic in Vue 2, but they suffered from severe drawbacks: property name collisions, unclear sources of properties (implicit dependencies), and poor TypeScript support.",
     ["Composables (using the Composition API) solve this by utilizing standard JavaScript functions that return explicit reactive state and methods.", "With Composables, IDEs can accurately trace variables, naming conflicts are resolved locally via destructuring, and logic composition becomes highly flexible."],
     "const { x, y } = useMouse(); // Source of variables is explicitly clear",
     "https://vuejs.org/guide/reusability/composables.html#vs-mixins"),
     
    ("Why is the `key` attribute required in `v-for`?",
     "The `key` attribute provides Vue's virtual DOM diffing algorithm with a unique identifier for each node in a list. This allows Vue to track elements precisely during updates, additions, and deletions.",
     ["Without keys, Vue uses an 'in-place patch' strategy, trying to reuse existing DOM elements and updating their content. This causes critical bugs if list items contain complex nested state or temporary DOM state (like input focus).", "The key must be a unique, stable primitive (string or number), typically a database ID, and never the array index."],
     "<li v-for=\"item in items\" :key=\"item.id\">{{ item.name }}</li>",
     "https://vuejs.org/guide/essentials/list.html#maintaining-state-with-key"),
     
    ("What does the `<keep-alive>` component do?",
     "`<keep-alive>` is a built-in component that caches dynamically toggled components instead of destroying them. When a cached component is toggled back into view, its state and DOM are restored instantly.",
     ["It introduces two special lifecycle hooks: `activated` and `deactivated`, as `mounted` and `unmounted` are not called during toggling.", "It accepts `include` and `exclude` props (using strings, regex, or arrays) to specifically target which components should be cached, preventing excessive memory usage."],
     "<keep-alive include=\"TabA,TabB\"> <component :is=\"currentTab\" /> </keep-alive>",
     "https://vuejs.org/guide/built-ins/keep-alive.html"),
     
    ("What is `nextTick` in Vue?",
     "`nextTick` is a utility function that delays the execution of a callback until after the next DOM update cycle. It returns a Promise that resolves when the DOM has been updated.",
     ["Vue updates the DOM asynchronously. When you mutate reactive state, the DOM is not updated immediately. `nextTick` is required if you need to query the DOM immediately after changing data that affects the layout.", "It is heavily used in testing and complex UI interactions, such as focusing an input element the moment it becomes visible via `v-if`."],
     "message.value = 'updated'; await nextTick(); console.log(document.getElementById('msg').textContent);",
     "https://vuejs.org/api/general.html#nexttick"),
     
    ("What are Vue Router Navigation Guards?",
     "Navigation guards are hooks provided by Vue Router that allow you to intercept and control route transitions. They can be defined globally, per-route, or within components.",
     ["They are primarily used to enforce authentication, preventing unauthenticated users from accessing protected routes, or fetching data before a view is rendered.", "A guard function receives `to`, `from`, and `next` arguments. Returning `false` aborts the navigation, while returning a route path redirects the user."],
     "router.beforeEach((to, from) => { if (to.meta.requiresAuth && !auth) return '/login'; });",
     "https://router.vuejs.org/guide/advanced/navigation-guards.html"),
     
    ("How do Custom Directives work in Vue 3?",
     "Custom directives allow developers to encapsulate low-level DOM access and manipulation into reusable attributes. They are defined using lifecycle hooks similar to components (e.g., `mounted`, `updated`).",
     ["While components are for generating and managing the DOM tree, custom directives are strictly for direct, low-level DOM manipulations that are otherwise difficult to achieve declaratively.", "A classic use case is a `v-focus` directive that automatically calls `.focus()` on an input element when it is mounted."],
     "const vFocus = { mounted: (el) => el.focus() };",
     "https://vuejs.org/guide/reusability/custom-directives.html"),
     
    ("What is the Virtual DOM and how does Vue optimize it?",
     "The Virtual DOM is a lightweight JavaScript representation of the actual DOM. Vue renders components into the Virtual DOM, compares (diffs) the new tree against the old tree, and applies only the minimum necessary changes to the real DOM.",
     ["Vue 3 significantly optimized this process through compiler-informed Virtual DOM. The compiler statically analyzes the template, identifying static elements that never change and hoisting them out of the render loop.", "It also provides patch flags to dynamic elements, telling the diffing algorithm exactly what changed (e.g., text, class, or props), skipping full node comparisons."],
     "Static hoisting prevents unnecessary node creation on every re-render.",
     "https://vuejs.org/guide/extras/rendering-mechanism.html"),
     
    ("How do you handle global state without Pinia/Vuex?",
     "In Vue 3, you can easily create lightweight global state management by exporting a reactive object from an external JavaScript/TypeScript module.",
     ["Because `reactive()` and `ref()` are not tightly coupled to components, they retain reactivity anywhere in the application.", "While this is suitable for small applications, it lacks the developer tools integration, SSR safety, and structural guidelines (actions, getters) provided by dedicated libraries like Pinia."],
     "export const store = reactive({ count: 0 }); // Use directly in any component",
     "https://vuejs.org/guide/scaling-up/state-management.html")
]

def append_to_vue():
    filename = "Vuejs.md"
    if not os.path.exists(filename):
        print(f"Skipping {filename} - not found.")
        return
        
    with open(filename, 'a', encoding='utf-8') as f:
        # We start from Q5 as Q4 was added by the previous script
        current_q = 5
        for title, concept, details, example, reference in vue_qna:
            new_qna = f'''
### {current_q}. {title}
**Answer:** 
**The Core Concept:**
{concept}

**Key Details:**
- {details[0]}
- {details[1]}

**Example:** 
`{example}`

**Reference:** [Documentation]({reference})
'''
            f.write(new_qna)
            current_q += 1

if __name__ == "__main__":
    append_to_vue()
    print("Added 20 questions to Vuejs.md")
