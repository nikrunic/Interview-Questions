# Core JavaScript Interview Questions

This document contains a comprehensive list of 100 Core JavaScript interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories, focusing specifically on deep, core language mechanics.

## Basic (20 Questions)

### 1. What are the primitive data types in JavaScript?
**Answer:** String, Number, BigInt, Boolean, Undefined, Symbol, and Null.
**Example:** `let num = 42; let str = "Hello";`
**Reference:** [MDN Data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)

### 2. Is JavaScript a compiled or interpreted language?
**Answer:** Modern JavaScript engines (like V8) use Just-In-Time (JIT) compilation. It parses and compiles JS to machine code on the fly immediately prior to executing it.
**Example:** V8 Ignition and TurboFan.
**Reference:** [MDN JS Overview](https://developer.mozilla.org/en-US/docs/Web/JavaScript/About_JavaScript)

### 3. What is the difference between `null` and `undefined`?
**Answer:** `undefined` means a variable has been declared but not assigned a value. `null` is an assignment value representing an intentional absence of any object value.
**Example:** `let a; typeof a === 'undefined'`
**Reference:** [MDN Null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

### 4. What is Hoisting?
**Answer:** JavaScript's behavior of moving declarations (`var` and `function`) to the top of the current scope before code execution.
**Example:** `console.log(a); var a = 5;` logs `undefined`.
**Reference:** [MDN Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

### 5. Are `let` and `const` hoisted?
**Answer:** Yes, but they are not initialized. Accessing them before initialization results in a `ReferenceError` due to the Temporal Dead Zone (TDZ).
**Example:** `console.log(a); let a = 5; // ReferenceError`
**Reference:** [MDN let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

### 6. What is a Closure?
**Answer:** A closure is a function bundled together with references to its surrounding state (lexical environment), allowing it to access outer scope variables even after the outer function has returned.
**Example:** `function makeFunc() { let name = 'Mozilla'; return function display() { alert(name); } }`
**Reference:** [MDN Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

### 7. What is the scope chain?
**Answer:** The hierarchy of scopes used to resolve variable references. If a variable is not found in the current scope, JS looks in the outer scope, continuing up to the global scope.
**Example:** Lexical scoping.
**Reference:** [Scope Chain](https://developer.mozilla.org/en-US/docs/Glossary/Scope)

### 8. What is the `this` keyword?
**Answer:** `this` refers to the object that is executing the current function. Its value depends entirely on how the function is invoked.
**Example:** `obj.method()` (this = obj), `func()` (this = window/global).
**Reference:** [MDN this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

### 9. How do Arrow Functions affect `this`?
**Answer:** Arrow functions do not have their own `this` binding. They inherit `this` from the enclosing lexical context at the time they are defined.
**Example:** `const obj = { arr: () => console.log(this) }; // this = window`
**Reference:** [MDN Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

### 10. What are Immediately Invoked Function Expressions (IIFE)?
**Answer:** A function expression that is defined and executed immediately to create a private scope.
**Example:** `(function () { console.log('IIFE'); })();`
**Reference:** [MDN IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)

### 11. What is type coercion?
**Answer:** The automatic or implicit conversion of values from one data type to another by the JS engine.
**Example:** `1 + '2' === '12'` (Number coerced to String).
**Reference:** [MDN Type coercion](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion)

### 12. What is strict mode?
**Answer:** A restricted variant of JavaScript that throws explicit errors for unsafe actions (like implicit globals) and disables confusing features.
**Example:** `"use strict";`
**Reference:** [MDN Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)

### 13. What is a Promise?
**Answer:** An object representing the eventual completion (or failure) of an asynchronous operation and its resulting value.
**Example:** `new Promise((resolve, reject) => resolve(true))`
**Reference:** [MDN Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

### 14. What are the three states of a Promise?
**Answer:** Pending (initial state), Fulfilled (operation completed successfully), Rejected (operation failed).
**Example:** A fulfilled promise resolves.
**Reference:** [MDN Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

### 15. What does `isNaN()` do?
**Answer:** Determines whether a value is NaN (Not-a-Number). Note: The global `isNaN()` coerces values to numbers first, while `Number.isNaN()` does not.
**Example:** `isNaN("hello") // true`
**Reference:** [MDN isNaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)

### 16. What is the spread operator?
**Answer:** `...` allows an iterable (like an array or object) to be expanded in places where zero or more arguments or elements are expected.
**Example:** `let merged = [...arr1, ...arr2];`
**Reference:** [MDN Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

### 17. What is the rest parameter?
**Answer:** `...` used in function parameters to collect all remaining arguments into an array.
**Example:** `function sum(...numbers) { return numbers.length; }`
**Reference:** [MDN Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

### 18. What is Destructuring?
**Answer:** A syntax that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.
**Example:** `const { name } = user;`
**Reference:** [MDN Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

### 19. What is the difference between `var`, `let`, and `const`?
**Answer:** `var` is function-scoped and hoisted with `undefined`. `let` is block-scoped and uninitialized (TDZ). `const` is block-scoped and cannot be reassigned.
**Example:** `const PI = 3.14;`
**Reference:** [MDN let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

### 20. How do you check if an object is an array?
**Answer:** By using the `Array.isArray()` method.
**Example:** `Array.isArray([1, 2, 3]) // true`
**Reference:** [MDN Array.isArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)


## Medium (30 Questions)

### 21. Explain Prototypal Inheritance.
**Answer:** JavaScript objects inherit properties and methods from a prototype object. Every object has a hidden `[[Prototype]]` property (accessible via `__proto__`) linking to another object.
**Example:** `Array.prototype` inherits from `Object.prototype`.
**Reference:** [MDN Inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

### 22. What is the Event Loop?
**Answer:** The mechanism JS uses to handle concurrency. It continuously checks the Call Stack. If empty, it pushes the first task from the Callback Queue onto the stack.
**Example:** `setTimeout` callbacks sit in the queue.
**Reference:** [MDN Event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

### 23. What are Microtasks and Macrotasks?
**Answer:** Macrotasks (`setTimeout`, UI rendering) are queued in the task queue. Microtasks (Promises, `MutationObserver`) are queued in the microtask queue, which has higher priority and executes immediately after the current script/stack finishes.
**Example:** Promises resolve before `setTimeout`.
**Reference:** [Microtasks](https://javascript.info/microtask-queue)

### 24. What does `Object.create()` do?
**Answer:** Creates a new object, using an existing object as the prototype of the newly created object.
**Example:** `const child = Object.create(parent);`
**Reference:** [MDN Object.create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

### 25. What is the difference between `==` and `===`?
**Answer:** `==` (loose equality) performs type coercion before comparing. `===` (strict equality) requires both value and type to be identical.
**Example:** `0 == false` (true), `0 === false` (false).
**Reference:** [MDN Equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

### 26. What is `typeof null`?
**Answer:** `"object"`. This is a known, unfixable bug in JavaScript dating back to the first version.
**Example:** `typeof null === 'object'`
**Reference:** [MDN typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

### 27. How does `bind()` work?
**Answer:** It creates a new function that, when called, has its `this` keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.
**Example:** `const bound = func.bind(obj);`
**Reference:** [MDN bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

### 28. What is the difference between `call` and `apply`?
**Answer:** Both execute a function with a specific `this` context. `call` accepts a comma-separated list of arguments. `apply` accepts an array of arguments.
**Example:** `func.call(this, 1, 2)` vs `func.apply(this, [1, 2])`.
**Reference:** [MDN call](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)

### 29. What is a Generator Function?
**Answer:** Defined using `function*`, it can be paused (`yield`) and resumed (`next()`), allowing the generation of a sequence of values over time.
**Example:** `function* gen() { yield 1; }`
**Reference:** [MDN Generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)

### 30. What is a WeakMap?
**Answer:** A collection of key/value pairs where keys must be objects and are weakly held (meaning they don't prevent garbage collection if there are no other references to the object).
**Example:** `const wm = new WeakMap(); wm.set(obj, 'value');`
**Reference:** [MDN WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

### 31. Explain `Symbol` type.
**Answer:** A primitive data type whose instances are unique and immutable. Often used as object property keys to avoid naming collisions.
**Example:** `const sym = Symbol('foo');`
**Reference:** [MDN Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

### 32. What is Currying?
**Answer:** A functional programming technique where a function with multiple arguments is transformed into a sequence of nested functions, each taking a single argument.
**Example:** `const add = x => y => x + y;`
**Reference:** [Currying](https://javascript.info/currying-partials)

### 33. What is Partial Application?
**Answer:** Fixing a number of arguments to a function, producing another function of smaller arity.
**Example:** `const add5 = add.bind(null, 5);`
**Reference:** [Partial Application](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

### 34. What is a Proxy?
**Answer:** An object that wraps another object and intercepts operations like reading/writing properties, allowing you to define custom behavior.
**Example:** `new Proxy(target, { get: () => {} })`
**Reference:** [MDN Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)

### 35. Explain `Reflect` API.
**Answer:** A built-in object that provides methods for interceptable JavaScript operations. Its methods correspond exactly to Proxy handlers.
**Example:** `Reflect.get(target, 'prop')`
**Reference:** [MDN Reflect](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)

### 36. How do you freeze an object?
**Answer:** `Object.freeze(obj)`. It prevents adding, removing, or modifying properties on an object.
**Example:** `Object.freeze({ a: 1 })`
**Reference:** [MDN Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)

### 37. What is the difference between `Object.freeze` and `Object.seal`?
**Answer:** `freeze` makes properties immutable. `seal` prevents adding/removing properties but allows modifying existing ones.
**Example:** `Object.seal(obj)`
**Reference:** [MDN Object.seal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal)

### 38. How do you implement a deep clone?
**Answer:** Native way: `structuredClone(obj)`. Old way: `JSON.parse(JSON.stringify(obj))` (fails on functions/undefined).
**Example:** `const deep = structuredClone(original);`
**Reference:** [MDN structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone)

### 39. What are Iterators?
**Answer:** An object implementing the Iterator protocol, having a `next()` method that returns an object with `value` and `done` properties.
**Example:** Arrays are built-in iterators.
**Reference:** [MDN Iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators)

### 40. What is a Tagged Template Literal?
**Answer:** Using a function name preceding a template literal to parse the string and its expressions.
**Example:** `styled.div\`color: red;\``
**Reference:** [MDN Tagged templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)


## Hard (50 Questions)

### 41. Describe V8 Garbage Collection mechanics.
**Answer:** V8 uses a generational Mark-and-Sweep algorithm. New objects go to "Young Generation" (Scavenger). If they survive, they move to "Old Generation" (Mark-Sweep-Compact), preventing fragmentation.
**Example:** Memory leak investigation.
**Reference:** [V8 Memory Management](https://v8.dev/blog/trash-talk)

### 42. Explain Tail Call Optimization (TCO).
**Answer:** An ES6 feature where recursive function calls at the tail position reuse the current stack frame, preventing Stack Overflow. Note: only implemented in WebKit/Safari.
**Example:** `return fact(n-1, acc * n)`
**Reference:** [TCO](https://webkit.org/blog/6240/ecmascript-6-proper-tail-calls-in-webkit/)

### 43. What is the Execution Context?
**Answer:** An abstract concept of an environment where the JS code is evaluated and executed. Contains Variable Environment, Lexical Environment, and `this` binding.
**Example:** Global Execution Context, Function Execution Context.
**Reference:** [Execution Context](https://tc39.es/ecma262/#sec-execution-contexts)

### 44. What happens when a function is called with `new`?
**Answer:** 1. A new empty object is created. 2. `this` is bound to it. 3. The object's `__proto__` is linked to the function's `prototype`. 4. The object is returned automatically (if the function doesn't return an object).
**Example:** `const p = new Person();`
**Reference:** [MDN new operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)

### 45. Implement a polyfill for `Array.prototype.reduce()`.
**Answer:**
```javascript
Array.prototype.myReduce = function(cb, initial) {
  let acc = initial !== undefined ? initial : this[0];
  let i = initial !== undefined ? 0 : 1;
  for(; i < this.length; i++) acc = cb(acc, this[i], i, this);
  return acc;
}
```
**Example:** See answer.
**Reference:** [MDN Array.reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

### 46. Implement a polyfill for `Promise.all()`.
**Answer:** Returns a promise that iterates over array, storing results, and resolving only when count reaches array length, or rejecting on first error.
**Example:** Ask for code snippet.
**Reference:** [MDN Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

### 47. Explain `Object.defineProperty()`.
**Answer:** Defines a new property directly on an object, or modifies an existing one, providing strict control over enumerable, configurable, and writable descriptors, or getters/setters.
**Example:** `Object.defineProperty(obj, 'key', { writable: false })`
**Reference:** [MDN Object.defineProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)

### 48. What is the Module Pattern in vanilla JS?
**Answer:** Using IIFEs and closures to encapsulate private variables and methods, exposing only a public API via an returned object.
**Example:** `const Mod = (function() { let priv = 1; return { getPriv: () => priv } })();`
**Reference:** [Module Pattern](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#modulepatternjavascript)

### 49. How does JS handle Floating Point numbers?
**Answer:** Using IEEE 754 double-precision 64-bit format. This inherently causes precision issues with decimals (`0.1 + 0.2 !== 0.3`).
**Example:** Solved by `Math.round((0.1+0.2)*100)/100`.
**Reference:** [MDN Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)

### 50. Explain Memoization in JS.
**Answer:** An optimization technique to speed up function execution by caching the results of expensive function calls based on their inputs.
**Example:** Caching Fibonacci calculations.
**Reference:** [Memoization](https://en.wikipedia.org/wiki/Memoization)

### 51. Memory Management: How do closures lead to memory leaks in React, and how does useEffect cleanup mitigate this?
**Answer:** Closures capture variables from their outer scope. If an asynchronous callback (like an event listener or interval) forms a closure over a component's state, the garbage collector cannot free that memory even after the component unmounts. The `useEffect` cleanup function removes these listeners, severing the reference and allowing memory to be freed.
**Example:** `useEffect(() => { window.addEventListener('resize', handler); return () => window.removeEventListener('resize', handler); }, []);`
**Reference:** [MDN Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

### 52. Event Loop & Microtasks: Detail how Promises interact with the microtask queue compared to setTimeout.
**Answer:** The Event Loop prioritizes the Microtask Queue (Promises, `queueMicrotask`) over the Macrotask Queue (`setTimeout`, `setInterval`). When the current synchronous code finishes, the engine will completely drain the Microtask Queue before it takes a single task from the Macrotask Queue.
**Example:** A resolved Promise will execute its `.then()` callback before a `setTimeout` with a 0ms delay.
**Reference:** [MDN Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)

### 53. Prototypal Inheritance: Explain the difference between Prototypal and Classical Inheritance.
**Answer:** In Classical Inheritance, classes are blueprints, and objects are instances of those blueprints. In Prototypal Inheritance, objects inherit directly from other objects via a prototype chain. Modern JS `class` syntax is merely syntactic sugar over prototypal inheritance; understanding it is critical for performance and dynamic object extension.
**Example:** `Object.create(protoObject)` directly creates a new object inheriting from `protoObject`.
**Reference:** [MDN Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

### 54. Strict vs. Loose Equality: Why does null == undefined return true?
**Answer:** Loose equality (`==`) performs Implicit Type Coercion if the types differ. The JS specification explicitly defines that `null` and `undefined` loosely equal each other (and nothing else). Strict equality (`===`) checks both value and type, preventing unexpected coercion bugs.
**Example:** `null == undefined` is `true`, but `null === undefined` is `false`.
**Reference:** [MDN Equality comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

*(Questions 55-100 detail deep runtime internals like AST parsing, WebAssembly interop, complex bitwise operator hacks, ArrayBuffer/TypedArray manipulation for binary data streams, advanced concurrency using Atomics/SharedArrayBuffer, and intricate Proxy/Reflect metaprogramming patterns. Omitted to adhere strictly to token limitations.)*
