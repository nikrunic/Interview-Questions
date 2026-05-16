# Core JavaScript Interview Questions

This document contains a comprehensive list of advanced and Core JavaScript interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What does it mean that JavaScript is single-threaded?
**Answer:** Single-threaded means that JavaScript executes one command at a time. It has a single Call Stack and Memory Heap. It cannot execute multiple blocks of code concurrently.
**Example:** Code executes line by line from top to bottom.
**Reference:** [MDN - Concurrency model and the event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

### 2. What is strict mode?
**Answer:** Strict mode is a way to opt in to a restricted variant of JavaScript, eliminating some silent errors by changing them to throw errors and fixing mistakes that make it difficult for JavaScript engines to perform optimizations.
**Example:** `"use strict";` at the top of a file or function.
**Reference:** [MDN - Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)

### 3. What are falsy values in JavaScript?
**Answer:** A falsy value is a value that is considered false when encountered in a Boolean context. There are 6 falsy values: `false`, `0`, `""` (empty string), `null`, `undefined`, and `NaN`.
**Example:** `if (null) { // won't execute }`
**Reference:** [MDN - Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)

### 4. What is the DOM?
**Answer:** The Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content.
**Example:** `document.getElementById('demo').innerHTML = "Hello World!";`
**Reference:** [MDN - Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

### 5. What are template literals?
**Answer:** Template literals are string literals allowing embedded expressions. You can use multi-line strings and string interpolation features with them.
**Example:** `` `Current user: ${user.name}` ``
**Reference:** [MDN - Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)


## Medium (30%)

### 6. What is a Higher-Order Function?
**Answer:** A higher-order function is a function that either takes one or more functions as arguments, or returns a function as its result.
**Example:** `Array.prototype.map`, `Array.prototype.filter`, and `Array.prototype.reduce` are higher-order functions.
**Reference:** [MDN - First-class Function](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)

### 7. What is an IIFE (Immediately Invoked Function Expression)?
**Answer:** An IIFE is a JavaScript function that runs as soon as it is defined. It creates a private lexical scope to avoid polluting the global namespace.
**Example:** `(function() { var a = 1; })();`
**Reference:** [MDN - IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)

### 8. Explain the difference between mutable and immutable objects.
**Answer:** A mutable object can be changed after it is created. An immutable object's state cannot be changed after creation. In JS, objects and arrays are mutable; primitive values (strings, numbers) are immutable.
**Example:** Mutating an array: `arr.push(1)`. Primitive immutable: `let a = "str"; a[0] = "b"; // fails`
**Reference:** [MDN - Mutable](https://developer.mozilla.org/en-US/docs/Glossary/Mutable)

### 9. What is method chaining?
**Answer:** Method chaining is a pattern where multiple methods are called sequentially on the same object. This is possible because each method returns the object itself.
**Example:** `str.replace("a", "b").toUpperCase().trim();`
**Reference:** [Wikipedia - Method chaining](https://en.wikipedia.org/wiki/Method_chaining)

### 10. How does `JSON.stringify()` and `JSON.parse()` work?
**Answer:** `JSON.stringify()` converts a JavaScript object or value to a JSON string. `JSON.parse()` parses a JSON string, constructing the JavaScript value or object described by the string. This is commonly used for deep cloning simple objects.
**Example:** `const clone = JSON.parse(JSON.stringify(originalObj));`
**Reference:** [MDN - JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

### 11. What is the difference between `Object.freeze()` and `Object.seal()`?
**Answer:** `Object.freeze()` makes an object completely immutable (cannot add, delete, or modify properties). `Object.seal()` prevents adding or deleting properties, but existing properties can still be modified.
**Example:** `Object.freeze(obj); obj.newProp = 1; // Fails`
**Reference:** [MDN - Object.freeze()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)


## Hard (50%)

### 12. Explain the Prototype Chain deeply.
**Answer:** Every JS object has a hidden, internal property `[[Prototype]]` (accessible via `__proto__`). When a property is accessed, the engine checks the object. If missing, it checks the object's prototype, then that prototype's prototype, until it reaches `null` (the end of the chain, usually `Object.prototype.__proto__`).
**Example:** `myArray.toString()` looks up `myArray`, doesn't find it, looks in `Array.prototype`, doesn't find it, looks in `Object.prototype`, finds it.
**Reference:** [MDN - Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

### 13. What is the difference between `Lexical Scope` and `Dynamic Scope`?
**Answer:** Lexical scope means scope is defined at lexing time (when the code is written/parsed), meaning a function's scope is determined by where it was defined. Dynamic scope (not used in JS) determines scope based on where the function is called. JS uses lexical scope via closures.
**Example:** A closure remembers the environment where it was *created*, not invoked.
**Reference:** [MDN - Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

### 14. What are Web APIs and how do they relate to the Event Loop?
**Answer:** Web APIs (like `setTimeout`, `fetch`, DOM events) are provided by the browser environment, not the V8 engine. They run concurrently in C++ background threads. When they complete, they push their callbacks into the Task Queue, which the Event Loop then pushes onto the Call Stack when it is empty.
**Example:** `setTimeout(() => {}, 1000)` delegates the 1-second timer to the Browser API.
**Reference:** [MDN - EventLoop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

### 15. What are Microtasks and Macrotasks?
**Answer:** In the event loop, tasks are split into two queues. Macrotasks (Task Queue) include `setTimeout`, `setInterval`, I/O, UI rendering. Microtasks (Microtask Queue) include `Promises`, `MutationObserver`, `process.nextTick`. The Event Loop completely empties the Microtask Queue *before* processing the next Macrotask.
**Example:** A resolved Promise will execute before a 0ms `setTimeout`.
**Reference:** [MDN - Using microtasks](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide)

### 16. Implement a polyfill for `Array.prototype.map`.
**Answer:** A polyfill provides modern functionality on older browsers.
**Example:** 
```javascript
Array.prototype.myMap = function(callback) {
  const result = [];
  for(let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};
```
**Reference:** [MDN - Array map Polyfill](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map#polyfill)

### 17. How does the `new` keyword actually work under the hood?
**Answer:** The `new` keyword does 4 things: 1) Creates a new empty object. 2) Links this new object to the constructor function's prototype property. 3) Binds `this` to the newly created object and executes the constructor. 4) Returns the object (unless the constructor explicitly returns a non-primitive).
**Example:** `const obj = new Person('John');`
**Reference:** [MDN - new operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)

### 18. What is a Proxy object?
**Answer:** The `Proxy` object enables you to create a proxy for another object, which can intercept and redefine fundamental operations for that object, such as property lookup, assignment, enumeration, function invocation, etc.
**Example:** `const proxy = new Proxy(target, { get: (obj, prop) => prop in obj ? obj[prop] : 37 });`
**Reference:** [MDN - Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)

### 19. Explain Memory Leaks in JavaScript.
**Answer:** Memory leaks occur when objects are no longer needed by the application but are still referenced by variables, preventing the garbage collector from reclaiming the memory. Common causes include uncleared intervals/timers, unremoved event listeners, and global variables.
**Example:** Setting `window.myData = largeArray;` and never deleting it.
**Reference:** [MDN - Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

### 20. What is Tail Call Optimization (TCO)?
**Answer:** TCO is a feature in ES6 where if the last action of a function is to return the result of calling another function (a tail call), the engine can reuse the current stack frame instead of creating a new one. This prevents stack overflow in recursive functions. (Note: currently only fully supported in Safari).
**Example:** `function factorial(n, acc = 1) { return n <= 1 ? acc : factorial(n - 1, n * acc); }`
**Reference:** [ECMAScript - Tail Position Calls](https://tc39.es/ecma262/#sec-tail-position-calls)
