# JavaScript Interview Questions

This document contains a comprehensive list of JavaScript interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What are the different data types in JavaScript?
**Answer:** The basic data types are string, number, boolean, undefined, null, symbol, and bigint. These are primitive types. Objects (including arrays and functions) are non-primitive.
**Example:** `let name = "John"; let age = 25; let isStudent = true;`
**Reference:** [MDN - JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)

### 2. What is the difference between `let`, `var`, and `const`?
**Answer:** `var` is function-scoped and hoisted with `undefined`. `let` and `const` are block-scoped and hoisted but not initialized (temporal dead zone). `const` creates a read-only reference to a value.
**Example:** `const a = 10; let b = 20; var c = 30;`
**Reference:** [MDN - let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

### 3. What is the difference between `==` and `===`?
**Answer:** `==` compares values after performing type coercion. `===` (strict equality) compares both value and type without coercion.
**Example:** `1 == '1' // true`, `1 === '1' // false`
**Reference:** [MDN - Equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)

### 4. What is NaN?
**Answer:** `NaN` stands for "Not-a-Number". It represents a value which is not a valid number. It is the result of operations like dividing zero by zero or multiplying a string by a number.
**Example:** `"apple" * 3 // returns NaN`
**Reference:** [MDN - NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)

### 5. Explain what an array is.
**Answer:** An array is a special variable that can hold more than one value at a time in an ordered list.
**Example:** `const fruits = ["Apple", "Banana", "Cherry"];`
**Reference:** [MDN - Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

### 6. What does the `typeof` operator do?
**Answer:** The `typeof` operator returns a string indicating the type of the unevaluated operand.
**Example:** `typeof "hello" // returns "string"`
**Reference:** [MDN - typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

### 7. How do you create an object in JavaScript?
**Answer:** The most common way is using object literal syntax `{}`.
**Example:** `const person = { name: "Alice", age: 30 };`
**Reference:** [MDN - Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)

### 8. What is a function in JavaScript?
**Answer:** A function is a reusable block of code designed to perform a particular task. It executes when "called" or "invoked".
**Example:** `function greet() { return "Hello"; }`
**Reference:** [MDN - Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)


## Medium (30%)

### 9. What are arrow functions?
**Answer:** Arrow functions introduced in ES6 provide a more concise syntax to write functions and they lexically bind the `this` value (they don't have their own `this`).
**Example:** `const add = (a, b) => a + b;`
**Reference:** [MDN - Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

### 10. What is a closure?
**Answer:** A closure is a function bundled together with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function's scope from an inner function.
**Example:** `function makeFunc() { var name = 'Mozilla'; function displayName() { alert(name); } return displayName; }`
**Reference:** [MDN - Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

### 11. What is Hoisting?
**Answer:** Hoisting is JavaScript's default behavior of moving all declarations to the top of the current scope (script or function). Only declarations are hoisted, not initializations.
**Example:** `console.log(x); var x = 5; // outputs undefined, not error`
**Reference:** [MDN - Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

### 12. Explain the concept of Promises.
**Answer:** A Promise is an object representing the eventual completion or failure of an asynchronous operation. It has three states: pending, fulfilled, or rejected.
**Example:** `const p = new Promise((resolve, reject) => { setTimeout(() => resolve("Done"), 1000); });`
**Reference:** [MDN - Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

### 13. What is Event Bubbling?
**Answer:** Event bubbling is a method of event propagation in the HTML DOM where the event triggers on the innermost target element and then successively triggers on the ancestors of the target element.
**Example:** Clicking a `<p>` inside a `<div>` will trigger the click event on the `<p>`, then the `<div>`.
**Reference:** [MDN - Event bubbling](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling)

### 14. What is the difference between `null` and `undefined`?
**Answer:** `undefined` means a variable has been declared but has not yet been assigned a value. `null` is an assignment value representing no value or no object.
**Example:** `let a; console.log(a); // undefined. let b = null; // null.`
**Reference:** [MDN - null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

### 15. What are template literals?
**Answer:** Template literals are string literals allowing embedded expressions. You can use multi-line strings and string interpolation features with them. They are enclosed by the backtick (\`).
**Example:** `` `Hello ${name}!` ``
**Reference:** [MDN - Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

### 16. What is destructuring assignment?
**Answer:** It is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.
**Example:** `const {name, age} = {name: 'John', age: 30};`
**Reference:** [MDN - Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

### 17. Explain `map()`, `filter()`, and `reduce()`.
**Answer:** These are array methods. `map` transforms an array into a new array. `filter` returns a new array with elements that pass a test. `reduce` reduces the array to a single value by applying a function.
**Example:** `[1,2,3].map(x => x * 2); // [2,4,6]`
**Reference:** [MDN - Array.prototype.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)


## Hard (50%)

### 18. What is the Event Loop?
**Answer:** The Event Loop is a mechanism that allows JavaScript to perform non-blocking I/O operations despite being single-threaded. It constantly checks the call stack and the task queue, pushing tasks to the stack when it's empty.
**Example:** `setTimeout(() => console.log('first'), 0); console.log('second');` logs "second" then "first".
**Reference:** [MDN - The event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

### 19. How does `this` keyword work in JavaScript?
**Answer:** `this` refers to the object it belongs to. However, its value is determined by how a function is called (execution context). In global scope it's `window` (or `global`). In an object method, it's the object. In an arrow function, it inherits from the enclosing lexical context.
**Example:** `const obj = { name: "A", log() { console.log(this.name); } }`
**Reference:** [MDN - this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

### 20. What is the difference between `call`, `apply`, and `bind`?
**Answer:** All three change the `this` context of a function. `call` passes arguments individually. `apply` passes arguments as an array. `bind` returns a new function with the bound `this` context instead of invoking it immediately.
**Example:** `fn.call(obj, arg1, arg2); fn.apply(obj, [arg1, arg2]); const newFn = fn.bind(obj);`
**Reference:** [MDN - Function.prototype.bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

### 21. What is Prototypal Inheritance?
**Answer:** All JavaScript objects inherit properties and methods from a prototype. The `__proto__` property points to the prototype object, creating a prototype chain up to `Object.prototype`.
**Example:** `Array.prototype` contains `push()`, which all array instances inherit.
**Reference:** [MDN - Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

### 22. What are Generators?
**Answer:** Generators are functions that can be exited and later re-entered. Their context (variable bindings) will be saved across re-entrances. They are declared using `function*` and use the `yield` keyword.
**Example:** `function* gen() { yield 1; yield 2; }`
**Reference:** [MDN - Generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)

### 23. What is a WeakMap and how is it different from a Map?
**Answer:** A `WeakMap` is a collection of key/value pairs where the keys must be objects and the values can be arbitrary values. The keys are weakly referenced, meaning they do not prevent garbage collection if there are no other references to the object. `WeakMap` is not iterable.
**Example:** `let wm = new WeakMap(); let obj = {}; wm.set(obj, "data");`
**Reference:** [MDN - WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

### 24. Explain Curry in JavaScript.
**Answer:** Currying is the process of taking a function with multiple arguments and turning it into a sequence of functions each with only a single argument.
**Example:** `const add = a => b => a + b; add(2)(3); // 5`
**Reference:** [JavaScript.info - Currying](https://javascript.info/currying-partials)

### 25. What is the Temporal Dead Zone (TDZ)?
**Answer:** The TDZ is a specific period in the execution context during which a block-scoped variable (`let` or `const`) exists but cannot be accessed until it is initialized. Accessing it throws a ReferenceError.
**Example:** `{ console.log(a); let a = 5; } // ReferenceError`
**Reference:** [MDN - let Temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)

### 26. How do `async`/`await` work under the hood?
**Answer:** `async`/`await` is syntactic sugar over Promises and Generators. An `async` function always returns a Promise. The `await` keyword pauses the execution of the async function until the Promise is settled, acting like a `yield` in a generator.
**Example:** `async function fetchUser() { const data = await fetch(url); return data.json(); }`
**Reference:** [MDN - async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

### 27. What are Web Workers?
**Answer:** Web Workers allow you to run scripts in background threads, meaning you can execute complex computations without blocking the main browser thread (UI thread).
**Example:** `const worker = new Worker('worker.js'); worker.postMessage('hello');`
**Reference:** [MDN - Web Workers API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

### 28. How does Garbage Collection work in JavaScript?
**Answer:** JavaScript uses automatic garbage collection. The main algorithm is "Mark and Sweep", which periodically marks objects that are reachable from the "roots" (global object) and sweeps (deletes) those that are unreachable.
**Example:** Setting an object reference to `null` allows the memory it occupied to be garbage collected.
**Reference:** [MDN - Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

### 29. What is Debouncing and Throttling?
**Answer:** Both limit the rate at which a function is executed. **Debounce** delays the execution until a certain amount of time has passed since the last trigger (e.g., waiting for the user to stop typing). **Throttle** ensures the function is called at most once in a specified time period (e.g., limiting scroll events).
**Example:** Using `setTimeout` to reset a timer on keypress (debounce).
**Reference:** [CSS Tricks - Debouncing and Throttling](https://css-tricks.com/debouncing-throttling-explained-examples/)
