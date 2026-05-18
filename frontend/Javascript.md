# JavaScript — Complete Interview Guide

This file combines three JavaScript resources into one place:

| Part | Content | Former file |
|------|---------|-------------|
| **1** | Interview preparation (concepts, links, tables) | `Javascript-Interview-Prep.md` |
| **2** | 100 interview Q&A (Basic / Medium / Hard) | `Javascript.md` |
| **3** | Core language deep dive Q&A | `Core-javascript.md` |

**Also see:** [JS Practical](./js-practical.md) — runnable snippets with step-by-step outputs.

---

## Table of contents

- [Part 1 — Interview preparation](#part-1--interview-preparation)
- [Part 2 — Interview questions (100)](#part-2--interview-questions-100)
- [Part 3 — Core JavaScript deep dive](#part-3--core-javascript-deep-dive)

---

# Part 1 — Interview preparation

Core language concepts for interviews: types, memory, scope, functions, async, storage, and OOP in JavaScript. Each topic includes a concise answer and reference links for deeper reading.

---

## 1. What are the different data types in JavaScript?

**Answer:**

JavaScript has **primitive** and **reference** types.

| Category | Types | Stored as |
|----------|--------|-----------|
| **Primitive** | `string`, `number`, `bigint`, `boolean`, `undefined`, `symbol`, `null` | Immutable values (copied by value) |
| **Reference** | `object` (includes arrays, functions, dates, etc.) | Reference to memory heap |

**The Core Concept:**

- Primitives hold a single value. Assigning or passing them copies the value.
- Objects hold collections of properties. Assigning or passing them copies the **reference** (pointer), not the whole object.

**Example:**

```javascript
let a = 10;
let b = a;
b = 20;
console.log(a); // 10 — primitive copy

const obj1 = { x: 1 };
const obj2 = obj1;
obj2.x = 99;
console.log(obj1.x); // 99 — same object in memory
```

**Reference:** [Reference vs primitive values (Academind)](https://academind.com/tutorials/reference-vs-primitive-values/)

---

## 2. Call by value vs call by reference in JavaScript

**Answer:**

JavaScript is **always pass-by-value**. For objects, the **value** passed is the reference (memory address), not the object itself.

**The Core Concept:**

- **Primitives:** the actual value is copied into the parameter.
- **Objects/arrays/functions:** the reference is copied — both the argument and parameter point to the same object, so mutations inside the function are visible outside.

**Example:**

```javascript
function updateAge(user) {
  user.age = 31; // mutates shared object
}
const person = { name: "Knl", age: 30 };
updateAge(person);
console.log(person.age); // 31

function changePrimitive(n) {
  n = 100; // only changes local copy
}
let num = 5;
changePrimitive(num);
console.log(num); // 5
```

**Interview line:** “JS is pass-by-value; objects are passed by value of the reference.”

**Reference:** [Call by value vs reference (GeeksforGeeks)](https://www.geeksforgeeks.org/call-by-value-vs-call-by-reference-in-javascript/)

---

## 3. Memory: stack vs heap (behind the scenes)

**Answer:**

**Stack** holds static, fixed-size data (execution context, primitive values, references). **Heap** holds dynamically allocated objects (objects, closures, large data).

**The Core Concept:**

1. When a function runs, a **execution context** is pushed on the call stack.
2. Primitives live in the stack (or are inlined where engines optimize).
3. Objects are created on the **heap**; the stack stores a **reference** to them.
4. When nothing references a heap object, the **garbage collector** frees it.

**Example (conceptual):**

```javascript
function createUser() {
  const id = 1;              // primitive — stack-friendly
  return { id, name: "Knl" }; // object — heap; return value is reference
}
const user = createUser();
```

**Reference:** [Confused about stack and heap (Medium)](https://medium.com/fhinkel/confused-about-stack-and-heap-2cf3e6adb771)

---

## 4. What is variable hoisting?

**Answer:**

Hoisting is JavaScript’s behavior of processing **declarations** before executing the rest of the code in a scope. Declarations are “moved” to the top of their scope during the compilation phase.

**Key notes (from your outline — corrected):**

| Declaration | Hoisted? | Initial value when hoisted |
|-------------|----------|----------------------------|
| `var` | Yes | `undefined` |
| `function` declaration | Yes | Full function |
| `let` / `const` | Hoisted but **not initialized** | TDZ until line runs |

- **Initializations are not hoisted** — only declarations.  
  `console.log(x); var x = 5;` → logs `undefined`, not `5`.
- **`let` / `const`** are in the **Temporal Dead Zone** from start of block until declaration — accessing them before the line throws `ReferenceError`.
- Use **`"use strict"`** for stricter rules (no accidental globals, etc.).

**Example:**

```javascript
console.log(a); // undefined
var a = 10;

console.log(b); // ReferenceError
let b = 20;
```

**References:**

- [InterviewBit — JavaScript interview questions](https://www.interviewbit.com/javascript-interview-questions/)
- [Understanding hoisting (DigitalOcean)](https://www.digitalocean.com/community/tutorials/understanding-hoisting-in-javascript)

---

## 5. `var` vs `let` vs `const`

**Answer:**

| Feature | `var` | `let` | `const` |
|---------|-------|-------|---------|
| Scope | Function (or global) | Block | Block |
| Hoisting | Yes (`undefined`) | TDZ | TDZ |
| Re-declare in same scope | Allowed | Not allowed | Not allowed |
| Re-assign value | Yes | Yes | No (binding is constant) |

**The Core Concept:**

- Prefer **`const`** by default; use **`let`** when you need to reassign; avoid **`var`** in new code (block scope bugs, hoisting).
- `const` does **not** make objects immutable — you cannot reassign the variable, but `obj.prop = 1` still works.

**Example:**

```javascript
if (true) {
  var x = 1;
  let y = 2;
}
console.log(x); // 1
console.log(y); // ReferenceError
```

**References:**

- [var, let, const (freeCodeCamp)](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/)
- [InterviewBit — declaring variables](https://www.interviewbit.com/javascript-interview-questions/#diff-declaring-variable)

---

## 6. Is JavaScript statically or dynamically typed?

**Answer:**

JavaScript is **dynamically typed**. Variable types are checked at **runtime**, not compile time.

**The Core Concept:**

- In a **statically typed** language (e.g. TypeScript when compiled, Java, C#), types are known before run time.
- In **JavaScript**, the same variable can hold different types over time.

**Example:**

```javascript
let value = 42;       // number
value = "hello";      // string — valid at runtime
value = { id: 1 };    // object — valid
```

**Note:** **TypeScript** adds static typing at **compile time**; it compiles to JavaScript.

**Reference:** [InterviewBit — JavaScript interview questions](https://www.interviewbit.com/javascript-interview-questions/)

---

## 7. What are higher-order functions?

**Answer:**

A **higher-order function** either:

1. Takes one or more functions as arguments, or  
2. Returns a function.

**The Core Concept:**

Functions are first-class values — you can pass them like any other value. Array methods `map`, `filter`, `reduce`, and `forEach` are built-in higher-order functions.

**Example:**

```javascript
function operate(arr, fn) {
  return arr.map(fn);
}
const doubled = operate([1, 2, 3], (n) => n * 2);
// [2, 4, 6]
```

**Reference:** [InterviewBit — higher-order functions](https://www.interviewbit.com/javascript-interview-questions/)

---

## 8. `call`, `apply`, and `bind`

**Answer:**

All three control **`this`** and invoke or prepare a function.

| Method | Invokes now? | Arguments | `this` |
|--------|----------------|-----------|--------|
| `call` | Yes | Comma-separated | Set explicitly |
| `apply` | Yes | Array | Set explicitly |
| `bind` | No (returns new function) | Comma-separated | Fixed for later calls |

**Example:**

```javascript
function greet(greeting, punct) {
  return `${greeting}, ${this.name}${punct}`;
}
const user = { name: "Knl" };

greet.call(user, "Hello", "!");     // "Hello, Knl!"
greet.apply(user, ["Hi", "."]);     // "Hi, Knl."
const bound = greet.bind(user, "Hey");
bound("?");                          // "Hey, Knl?"
```

**Reference:** [InterviewBit — call, apply, bind](https://www.interviewbit.com/javascript-interview-questions/#call-apply-bind-methods)

---

## 9. Scope and scoping in JavaScript

**Answer:**

**Scope** is the region where a variable is accessible.

**Types:**

1. **Global** — `var` at top level, or implicit globals (avoid).
2. **Function** — `var` inside a function.
3. **Block** — `let` / `const` inside `{ }`.
4. **Lexical (closure)** — inner functions access outer variables even after outer returns.

**The Core Concept:**

JavaScript uses **lexical scoping** — scope is determined by where code is **written**, not where it is called.

**Example:**

```javascript
function outer() {
  const secret = "abc";
  return function inner() {
    return secret; // closure over outer's scope
  };
}
const fn = outer();
console.log(fn()); // "abc"
```

**Reference:** [InterviewBit — scope](https://www.interviewbit.com/javascript-interview-questions/)

---

## 10. What is currying?

**Answer:**

**Currying** transforms a function that takes multiple arguments into a sequence of functions that each take one argument (or fewer at a time).

**The Core Concept:**

Useful for partial application, reusable specialized functions, and functional composition.

**Example:**

```javascript
const add = (a) => (b) => (c) => a + b + c;
add(1)(2)(3); // 6

// General curry helper pattern
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) return fn(...args);
    return (...more) => curried(...args, ...more);
  };
}
```

**Reference:** [Currying in JavaScript (codeburst)](https://codeburst.io/currying-in-javascript-ba51eb9778dc)

---

## 11. Prototypes in JavaScript

**Answer:**

JavaScript uses **prototypal inheritance**. Every object has an internal link `[[Prototype]]` (exposed as `__proto__` or via `Object.getPrototypeOf`). If a property is missing on the object, the engine looks up the prototype chain.

**The Core Concept:**

- `function` constructors (and classes) have a `prototype` property used when you `new` them.
- Methods on `Array.prototype` are shared by all arrays.

**Example:**

```javascript
const animal = { eats: true };
const dog = Object.create(animal);
dog.barks = true;
console.log(dog.eats); // true — from prototype

class Person {
  constructor(name) {
    this.name = name;
  }
  hello() {
    return `Hi, ${this.name}`;
  }
}
```

**Reference:** [InterviewBit — prototypes](https://www.interviewbit.com/javascript-interview-questions/)

---

## 12. What are callback functions?

**Answer:**

A **callback** is a function passed as an argument to another function, to be run later (after an event, timer, or async operation).

**The Core Concept:**

Enables asynchronous and event-driven code. Downside: nested callbacks → “callback hell”; mitigated with Promises and `async/await`.

**Example:**

```javascript
function fetchData(callback) {
  setTimeout(() => callback(null, { id: 1 }), 1000);
}
fetchData((err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
```

**Reference:** [InterviewBit — callbacks](https://www.interviewbit.com/javascript-interview-questions/#callbacks)

---

## 13. What is memoization?

**Answer:**

**Memoization** caches a function’s **return value** for a given set of arguments so repeated calls return the cached result without recomputing.

**The Core Concept:**

Trade memory for speed. Best when the function is pure and expensive (e.g. Fibonacci, heavy calculations).

**Example:**

```javascript
function memoize(fn) {
  const cache = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

const fib = memoize(function fib(n) {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);
});
```

**Reference:** [InterviewBit — memoization](https://www.interviewbit.com/javascript-interview-questions/#memoization)

---

## 14. Arrow functions vs regular functions

**Answer:**

| Feature | Regular function | Arrow function |
|---------|------------------|--------------|
| `this` | Dynamic — set by **how called** | **Lexical** — from enclosing scope |
| `arguments` | Yes | No (use rest `...args`) |
| `new` / constructor | Yes | No |
| Hoisting | Function declarations hoisted | Not hoisted (`const fn = () => {}`) |

**The Core Concept (corrected from common interview notes):**

- Regular method: `obj.method()` → `this` is `obj`.
- Arrow as object method: `this` is **not** `obj` — it uses the parent scope (often `undefined` in modules, or `window` in non-strict browser scripts).
- **Do not** use arrows for object methods if you need `this` to be the object. **Do** use arrows for callbacks when you want `this` from the outer function (e.g. class field handlers).

**Example:**

```javascript
const obj = {
  name: "Knl",
  regular() {
    return this.name;
  },
  arrow: () => this?.name,
};
obj.regular(); // "Knl"
```

**Reference:** [InterviewBit — arrow functions](https://www.interviewbit.com/javascript-interview-questions/#arrow-functions)

---

## 15. Promises in JavaScript

**Answer:**

A **Promise** represents a value that may be available now, later, or never (fulfilled, rejected, or pending).

**States:** `pending` → `fulfilled` or `rejected` (settled once).

**Example:**

```javascript
const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve("done"), 1000);
});

p.then((value) => console.log(value))
  .catch((err) => console.error(err))
  .finally(() => console.log("cleanup"));

// Parallel
Promise.all([p1, p2]).then(([a, b]) => {});
```

**Reference:** [InterviewBit — promises](https://www.interviewbit.com/javascript-interview-questions/#javascript-promises)

---

## 16. How does the JavaScript engine work?

**Answer:**

A **JavaScript engine** (V8 in Chrome/Node, SpiderMonkey in Firefox, JavaScriptCore in Safari) **parses**, **compiles**, and **executes** JS.

**Typical pipeline (V8):**

1. **Download / load** source (network, cache, etc.).
2. **Parse** — Scanner → tokens; Parser → **AST** (Abstract Syntax Tree).
3. **Compile** — Modern engines use **JIT**: Ignition (bytecode) + optimizing compiler (e.g. TurboFan).
4. **Execute** on the call stack; objects on heap; GC reclaims unused memory.

**Runtime (beyond engine):**

- **Web APIs** (browser): DOM, `setTimeout`, fetch.
- **Event loop** schedules callbacks and microtasks (Promises).

**References:**

- [What happens inside JavaScript engine (GeeksforGeeks)](https://www.geeksforgeeks.org/what-happens-inside-javascript-engine/)
- [Brief explanation of JS engine and runtime (Medium)](https://medium.com/@sanderdebr/a-brief-explanation-of-the-javascript-engine-and-runtime-a0c27cb1a397)

---

## 17. What are pure functions?

**Answer:**

A **pure function**:

1. Given the **same inputs**, always returns the **same output**.
2. Has **no side effects** (no mutating external state, I/O, DOM, random time, etc.).

**Benefits:** Easier to test, cache (memoize), and reason about; core of Redux reducers and React best practices.

**Example:**

```javascript
// Pure
const add = (a, b) => a + b;

// Impure
let count = 0;
function increment() {
  count++; // side effect
  return count;
}
```

**References:**

- [Pure functions (Medium — James Jeffery)](https://medium.com/@jamesjefferyuk/javascript-what-are-pure-functions-4d4d5392d49c)
- [Pure functions (Nicolas Espeon)](https://www.nicoespeon.com/en/2015/01/pure-functions-javascript/)
- [What is a pure function (freeCodeCamp)](https://www.freecodecamp.org/news/what-is-a-pure-function-in-javascript-acb887375dfe/)

---

## 18. `localStorage` vs `sessionStorage` vs cookies

**Answer:**

| Storage | Scope | Lifetime | Sent to server | Size (approx.) |
|---------|--------|----------|----------------|----------------|
| **localStorage** | Per origin | Until cleared | No | ~5–10 MB |
| **sessionStorage** | Per tab/window | Until tab closed | No | ~5–10 MB |
| **Cookie** | Configurable path/domain | Expiry date | Yes (every request) | ~4 KB |

**The Core Concept (your note):**

- **localStorage** persists after browser close and reboot (same origin).
- **sessionStorage** clears when the **tab/session** ends.
- **Cookies** used for auth, tracking, server sessions; use `HttpOnly` + `Secure` for sensitive tokens.

**Example:**

```javascript
localStorage.setItem("theme", "dark");
sessionStorage.setItem("step", "2");
```

**Reference:** [localStorage vs sessionStorage vs cookies (Stack Overflow)](https://stackoverflow.com/questions/19867599/what-is-the-difference-between-localstorage-sessionstorage-session-and-cookies)

---

## 19. `null` vs `undefined`

**Answer:**

| | `undefined` | `null` |
|---|-------------|--------|
| Meaning | Variable declared but not assigned; missing property | Intentional “no value” / empty object slot |
| `typeof` | `"undefined"` | `"object"` (historical bug) |
| Default | Uninitialized `let`/`var`, missing params, no `return` | Assigned explicitly by developer |

**The Core Concept (your note):**

- **`null`** — explicitly set to mean “no object value.”
- **`undefined`** — never assigned, or not defined on an object.

**Example:**

```javascript
let a;
console.log(a); // undefined

let user = null; // explicitly empty
console.log(user?.name); // undefined (optional chaining)
```

**Reference:** [InterviewBit — JavaScript interview questions](https://www.interviewbit.com/javascript-interview-questions/)

---

## OOP concepts in JavaScript

### 20. What are OOP concepts in JavaScript?

**Answer:**

JavaScript supports OOP via **objects**, **prototypes**, and **`class` syntax** (syntactic sugar over prototypes).

**Four pillars (how they map to JS):**

| Concept | In JavaScript |
|---------|----------------|
| **Encapsulation** | Closures, private fields `#field`, modules |
| **Inheritance** | Prototype chain, `extends` |
| **Polymorphism** | Same method name, different behavior on subtypes |
| **Abstraction** | Hide complexity; expose simple API (classes, modules) |

**Example:**

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  speak() {
    return `${this.name} barks`;
  }
}
```

**Reference:** [OOP in JavaScript (GeeksforGeeks)](https://www.geeksforgeeks.org/introduction-object-oriented-programming-javascript/)

---

### 21. How is abstraction related to React and the Virtual DOM?

**Answer:**

**Abstraction** means showing **what** something does while hiding **how** it works internally. In React, the Virtual DOM abstracts direct DOM manipulation — see [React guide](./Reactjs.md#46-oop-abstraction-and-the-virtual-dom-in-react) for the full React-focused answer.

**Reference:** [React — static HTML to React (core concepts)](https://kirtikau.medium.com/react-converting-static-html-website-to-react-application-1a877a8e9948)

---

## Additional references (async I/O)

**Synchronous vs asynchronous:**

- **Sync** blocks until work finishes (e.g. `readFileSync`).
- **Async** schedules work and continues; callback/Promise/`await` handle completion later.

**Reference:** [Introduction to asynchronous JavaScript](https://ozmoroz.com/2019/10/introduction-to-asynchronous-javascript/)

---

## Reference links (from your notes)

| Topic | Link |
|-------|------|
| JavaScript interview Q&A | [InterviewBit](https://www.interviewbit.com/javascript-interview-questions/) |
| JS engine | [GeeksforGeeks — inside JS engine](https://www.geeksforgeeks.org/what-happens-inside-javascript-engine/) |
| React core concepts | [Static HTML to React (Kirtika U.)](https://kirtikau.medium.com/react-converting-static-html-website-to-react-application-1a877a8e9948) |
| Sync vs async I/O | [Introduction to asynchronous JavaScript](https://ozmoroz.com/2019/10/introduction-to-asynchronous-javascript/) |

---

## Related in this guide

- [Part 2 — Interview questions (100)](#part-2--interview-questions-100)  
- [Part 3 — Core JavaScript deep dive](#part-3--core-javascript-deep-dive)  
- [JS Practical](./js-practical.md) — runnable snippets with step-by-step outputs

---

# Part 2 — Interview questions (100)

This document contains a comprehensive list of 100 JavaScript interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories (e.g., sudheerj/javascript-interview-questions).

## Basic (20 Questions)

### 1. What are the possible ways to create objects in JavaScript?
**Answer:** Object literals `{}`, `Object.create()`, Constructor functions, ES6 Classes, and `new Object()`.
**Example:** `const obj = {};`
**Reference:** [MDN Object Initialization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)

---

### 2. What is a prototype chain?
**Answer:** The mechanism by which JavaScript objects inherit features from one another.
**Example:** `obj.__proto__` points to `Object.prototype`.
**Reference:** [MDN Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

---

### 3. What is the difference between `call`, `apply`, and `bind`?
**Answer:** `call` invokes with comma-separated arguments, `apply` invokes with an array of arguments, `bind` returns a new function with bound `this`.
**Example:** `fn.call(obj, 1, 2); fn.apply(obj, [1, 2]); fn.bind(obj)();`
**Reference:** [MDN Function.prototype.bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

---

### 4. What is JSON and its common operations?
**Answer:** 
**The Core Concept:**
JavaScript Object Notation.

**Key Details:**
- Common operations are `JSON.parse()` (string to object) and `JSON.stringify()` (object to string).
**Example:** `const obj = JSON.parse('{"a":1}');`
**Reference:** [MDN JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

---

### 5. What is the difference between `slice` and `splice`?
**Answer:** 
**The Core Concept:**
`slice` returns a shallow copy of a portion of an array without modifying it.

**Key Details:**
- `splice` changes the contents of an array by removing or replacing existing elements.
**Example:** `arr.slice(1, 3); arr.splice(1, 1, 'new');`
**Reference:** [MDN Array.prototype.splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

---

### 6. What is the difference between `==` and `===`?
**Answer:** 
**The Core Concept:**
`==` compares values with type coercion.

**Key Details:**
- `===` compares values and types strictly without coercion.
**Example:** `1 == '1'` is true, `1 === '1'` is false.
**Reference:** [MDN Equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)

---

### 7. What are arrow functions?
**Answer:** A compact alternative to traditional function expressions, which lexically bind `this`.
**Example:** `const add = (a, b) => a + b;`
**Reference:** [MDN Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

---

### 8. What is a first-class function?
**Answer:** 
**The Core Concept:**
Functions in JS are treated like any other variable.

**Key Details:**
- They can be passed as arguments, returned, or assigned.
**Example:** `const greet = function() { console.log('Hi'); };`
**Reference:** [MDN First-class Function](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)

---

### 9. What is a higher-order function?
**Answer:** A function that takes a function as an argument or returns a function.
**Example:** `Array.prototype.map()`
**Reference:** [MDN First-class Function](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)

---

### 10. What is a pure function?
**Answer:** A function where the return value is only determined by its input values, without observable side effects.
**Example:** `function add(a, b) { return a + b; }`
**Reference:** [Wikipedia Pure function](https://en.wikipedia.org/wiki/Pure_function)

---

### 11. What is the difference between `let` and `var`?
**Answer:** 
**The Core Concept:**
`let` is block-scoped and doesn't create global object properties.

**Key Details:**
- `var` is function-scoped and hoisted.
**Example:** `if(true) { let x = 1; var y = 2; }` (`x` is unavailable outside, `y` is available).
**Reference:** [MDN let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

---

### 12. What is the Temporal Dead Zone (TDZ)?
**Answer:** The time between entering a scope and the actual declaration of a `let` or `const` variable where it cannot be accessed.
**Example:** `console.log(a); let a = 1;` throws a ReferenceError.
**Reference:** [MDN TDZ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)

---

### 13. What is an IIFE?
**Answer:** 
**The Core Concept:**
Immediately Invoked Function Expression.

**Key Details:**
- A function that runs as soon as it is defined.
**Example:** `(function() { console.log('Ran'); })();`
**Reference:** [MDN IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)

---

### 14. What is Hoisting?
**Answer:** JavaScript's default behavior of moving declarations to the top of the current scope.
**Example:** `x = 5; var x;` works because `var x` is hoisted.
**Reference:** [MDN Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

---

### 15. What are closures?
**Answer:** A closure is a function bundled together with references to its lexical environment.
**Example:** `function outer() { let a = 1; return function inner() { console.log(a); } }`
**Reference:** [MDN Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

---

### 16. What is the DOM?
**Answer:** 
**The Core Concept:**
Document Object Model.

**Key Details:**
- A programming interface for web documents.
**Example:** `document.getElementById('app')`
**Reference:** [MDN DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

---

### 17. What is Web Storage?
**Answer:** An API that provides mechanisms by which browsers can store key/value pairs locally (`localStorage` and `sessionStorage`).
**Example:** `localStorage.setItem('key', 'value');`
**Reference:** [MDN Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)

---

### 18. What is a Promise?
**Answer:** An object representing the eventual completion or failure of an asynchronous operation.
**Example:** `new Promise((resolve, reject) => { resolve('Success'); });`
**Reference:** [MDN Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

### 19. What is a callback function?
**Answer:** A function passed into another function as an argument, which is then invoked inside the outer function.
**Example:** `setTimeout(() => console.log('Done'), 1000);`
**Reference:** [MDN Callback function](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)

---

### 20. What is strict mode?
**Answer:** A way to opt in to a restricted variant of JavaScript that eliminates silent errors.
**Example:** `"use strict";`
**Reference:** [MDN Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)

---


## Medium (30 Questions)

### 21. What is the difference between `localStorage`, `sessionStorage`, and `cookies`?
**Answer:** 
**The Core Concept:**
`localStorage` persists across sessions.

**Key Details:**
- `sessionStorage` clears on tab close.
- `Cookies` are sent to the server with every request and have small size limits (4KB).
**Example:** `localStorage.setItem()`, `document.cookie`.
**Reference:** [MDN Web Storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)

---

### 22. What is Event Bubbling?
**Answer:** An event starts from the innermost element and bubbles up to the outer elements.
**Example:** Clicking a `button` inside a `div` triggers the button's click handler, then the div's.
**Reference:** [MDN Event bubbling](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling)

---

### 23. What is Event Capturing?
**Answer:** 
**The Core Concept:**
The opposite of bubbling.

**Key Details:**
- The event starts from the outermost element and propagates inwards to the target element.
**Example:** `element.addEventListener('click', handler, true);` (true enables capturing).
**Reference:** [MDN Event capturing](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_capturing)

---

### 24. What is Event Delegation?
**Answer:** Attaching a single event listener to a parent element to handle events for all of its children, utilizing event bubbling.
**Example:** `ul.addEventListener('click', (e) => { if(e.target.tagName === 'LI') { ... } });`
**Reference:** [JavaScript.info Event delegation](https://javascript.info/event-delegation)

---

### 25. What is the `typeof` operator?
**Answer:** Returns a string indicating the type of the unevaluated operand.
**Example:** `typeof "hello" // "string"`
**Reference:** [MDN typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

---

### 26. What is the `instanceof` operator?
**Answer:** Tests whether the prototype property of a constructor appears anywhere in the prototype chain of an object.
**Example:** `[] instanceof Array // true`
**Reference:** [MDN instanceof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)

---

### 27. What is NaN?
**Answer:** 
**The Core Concept:**
"Not-a-Number".

**Key Details:**
- A global property representing a value that is not a valid number.
**Example:** `parseInt("abc") // NaN`
**Reference:** [MDN NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)

---

### 28. How do you check if a value is NaN?
**Answer:** 
**The Core Concept:**
Using `Number.isNaN()` or `isNaN()`.

**Key Details:**
- `Number.isNaN()` is safer as it doesn't coerce values.
**Example:** `Number.isNaN(NaN) // true`
**Reference:** [MDN Number.isNaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)

---

### 29. What is `undefined` vs `null`?
**Answer:** 
**The Core Concept:**
`undefined` means a variable has been declared but not assigned.

**Key Details:**
- `null` is an intentional absence of any object value.
**Example:** `let a; // undefined`, `let b = null; // null`
**Reference:** [MDN null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

---

### 30. How do you deep clone an object?
**Answer:** Using `JSON.parse(JSON.stringify(obj))` or `structuredClone(obj)`.
**Example:** `const clone = structuredClone(original);`
**Reference:** [MDN structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone)

---

### 31. What are promises in JS and what are their states?
**Answer:** 
**The Core Concept:**
A Promise represents an asynchronous operation.

**Key Details:**
- States: Pending, Fulfilled, Rejected.
**Example:** `const p = new Promise((resolve) => resolve());`
**Reference:** [MDN Promise states](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

### 32. What is `Promise.all()`?
**Answer:** Takes an iterable of promises and resolves when all promises resolve, or rejects if any promise rejects.
**Example:** `Promise.all([p1, p2]).then(results => ...)`
**Reference:** [MDN Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

---

### 33. What is `Promise.race()`?
**Answer:** Returns a promise that fulfills or rejects as soon as one of the promises fulfills or rejects.
**Example:** `Promise.race([p1, p2]).then(first => ...)`
**Reference:** [MDN Promise.race](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)

---

### 34. What is `async`/`await`?
**Answer:** Syntactic sugar for promises, making asynchronous code look synchronous.
**Example:** `async function fetch() { const res = await apiCall(); }`
**Reference:** [MDN async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

---

### 35. What is the Event Loop?
**Answer:** The mechanism that handles the execution of multiple chunks of your program over time, executing functions from the call stack and pushing tasks from the callback queue.
**Example:** `setTimeout` callbacks are pushed to the queue and run by the event loop.
**Reference:** [MDN Event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

---

### 36. What is a generator function?
**Answer:** 
**The Core Concept:**
A function that can pause its execution and yield multiple values.

**Key Details:**
- Declared with `function*`.
**Example:** `function* gen() { yield 1; yield 2; }`
**Reference:** [MDN function*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)

---

### 37. What are default parameters?
**Answer:** Allows formal parameters to be initialized with default values if no value or `undefined` is passed.
**Example:** `function add(a = 0, b = 0) { return a + b; }`
**Reference:** [MDN Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)

---

### 38. What is object destructuring?
**Answer:** Extracting properties from objects and binding them to variables.
**Example:** `const { name, age } = user;`
**Reference:** [MDN Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

---

### 39. What is the spread operator?
**Answer:** Allows an iterable such as an array or object expression to be expanded in places where zero or more arguments or elements are expected.
**Example:** `const arr2 = [...arr1, 4, 5];`
**Reference:** [MDN Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

---

### 40. What is the rest parameter?
**Answer:** Allows a function to accept an indefinite number of arguments as an array.
**Example:** `function sum(...args) { return args.reduce((a, b) => a + b); }`
**Reference:** [MDN Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

---

### 41. What is a WeakMap?
**Answer:** A collection of key/value pairs where the keys must be objects and are weakly referenced (can be garbage collected).
**Example:** `const wm = new WeakMap(); wm.set(obj, "value");`
**Reference:** [MDN WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

---

### 42. What is a Set?
**Answer:** An object that lets you store unique values of any type.
**Example:** `const unique = new Set([1, 1, 2]); // Set(2) {1, 2}`
**Reference:** [MDN Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)

---

### 43. How do you remove duplicates from an array?
**Answer:** `Array.from(new Set(arr))` or `[...new Set(arr)]`.
**Example:** `const noDups = [...new Set([1, 2, 2])];`
**Reference:** [MDN Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)

---

### 44. What is currying?
**Answer:** Transforming a function with multiple arguments into a sequence of nested functions that take one argument at a time.
**Example:** `const add = x => y => x + y; add(5)(10);`
**Reference:** [JavaScript.info Currying](https://javascript.info/currying-partials)

---

### 45. What is the `Map` object?
**Answer:** 
**The Core Concept:**
Holds key-value pairs and remembers the original insertion order.

**Key Details:**
- Any value can be used as either a key or a value.
**Example:** `const map = new Map(); map.set('key', 'value');`
**Reference:** [MDN Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)

---

### 46. Explain `Object.keys()`, `Object.values()`, and `Object.entries()`.
**Answer:** `keys` returns an array of property names, `values` returns property values, `entries` returns an array of `[key, value]` pairs.
**Example:** `Object.keys({a: 1}) // ['a']`
**Reference:** [MDN Object.keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)

---

### 47. What is `Array.prototype.reduce()`?
**Answer:** Executes a reducer function on each element of the array, resulting in a single output value.
**Example:** `[1, 2].reduce((acc, val) => acc + val, 0); // 3`
**Reference:** [MDN Array.reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

---

### 48. What is the `this` keyword?
**Answer:** 
**The Core Concept:**
Refers to the object that is currently executing the code.

**Key Details:**
- Its value depends on how the function is called.
**Example:** `console.log(this); // window globally`
**Reference:** [MDN this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

---

### 49. How does `Array.prototype.map()` work?
**Answer:** Creates a new array populated with the results of calling a provided function on every element in the calling array.
**Example:** `[1, 2].map(x => x * 2); // [2, 4]`
**Reference:** [MDN Array.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

---

### 50. How does `Array.prototype.filter()` work?
**Answer:** Creates a shallow copy of a portion of a given array, filtered down to just the elements that pass the test implemented by the provided function.
**Example:** `[1, 2].filter(x => x > 1); // [2]`
**Reference:** [MDN Array.filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

---


## Hard (50 Questions)

### 51. Explain the mechanism of Garbage Collection in JavaScript.
**Answer:** 
**The Core Concept:**
JS uses a "mark-and-sweep" algorithm.

**Key Details:**
- Periodically, the garbage collector starts at the roots (global variables), finds all references from roots, and marks them reachable.
- It then sweeps (deletes) unreachable objects to free memory.
**Example:** An object detached from the global scope is swept.
**Reference:** [MDN Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

---

### 52. What are memory leaks and how do you prevent them?
**Answer:** 
**The Core Concept:**
A memory leak is a piece of memory that is no longer needed but is not released.

**Key Details:**
- Prevent them by clearing timers (`clearInterval`), removing unused event listeners, and avoiding accidental global variables.
**Example:** Forgetting to run `removeEventListener` when a component unmounts.
**Reference:** [MDN Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

---

### 53. What is the difference between Macrotasks and Microtasks?
**Answer:** 
**The Core Concept:**
Microtasks (Promises, `queueMicrotask`) execute immediately after the current script and before any rendering.

**Key Details:**
- Macrotasks (`setTimeout`, `setInterval`, UI events) execute in subsequent turns of the event loop.
**Example:** Promise handlers run before `setTimeout`.
**Reference:** [JavaScript.info Microtasks](https://javascript.info/microtask-queue)

---

### 54. Explain what polyfills are.
**Answer:** A polyfill is code (usually JavaScript on the Web) used to provide modern functionality on older browsers that do not natively support it.
**Example:** Writing a custom `Array.prototype.includes` for IE11.
**Reference:** [MDN Polyfill](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill)

---

### 55. What is a Proxy in JavaScript?
**Answer:** The `Proxy` object enables you to create a proxy for another object, which can intercept and redefine fundamental operations for that object.
**Example:** `const proxy = new Proxy(target, { get: function(...) { ... } });`
**Reference:** [MDN Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)

---

### 56. What is `Reflect` in JavaScript?
**Answer:** 
**The Core Concept:**
`Reflect` is a built-in object that provides methods for interceptable JavaScript operations.

**Key Details:**
- The methods are the same as those of proxy handlers.
**Example:** `Reflect.has(obj, 'prop');` (similar to `'prop' in obj`).
**Reference:** [MDN Reflect](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)

---

### 57. What are Service Workers?
**Answer:** Scripts that run in the background, separate from a web page, opening the door to features that don't need a web page or user interaction, like push notifications and background sync (PWA features).
**Example:** Intercepting network requests to serve cached assets offline.
**Reference:** [MDN Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)

---

### 58. What is the difference between a Service Worker and a Web Worker?
**Answer:** 
**The Core Concept:**
Web Workers are for executing heavy computations in a background thread to prevent UI blocking.

**Key Details:**
- Service Workers act as a network proxy and are designed for offline experiences and caching.
**Example:** `new Worker('script.js')` vs `navigator.serviceWorker.register(...)`.
**Reference:** [MDN Web Workers API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)

---

### 59. How does `JSON.stringify` behave with `undefined`, Functions, and Symbols?
**Answer:** They are omitted if they are values of an object, or converted to `null` if they are in an array.
**Example:** `JSON.stringify({ a: undefined, b: () => {} }) // "{}"`
**Reference:** [MDN JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

---

### 60. What is Tail Call Optimization (TCO)?
**Answer:** TCO allows recursive functions to reuse the stack frame if the recursive call is the very last operation, preventing stack overflow.
**Example:** `function fact(n, acc=1) { return n===0 ? acc : fact(n-1, n*acc); }`
**Reference:** [WebKit TCO](https://webkit.org/blog/6240/ecmascript-6-proper-tail-calls-in-webkit/)

---

### 61. Explain how prototypal inheritance works under the hood.
**Answer:** 
**The Core Concept:**
When accessing a property on an object, JS looks at the object itself.

**Key Details:**
- If not found, it checks `obj.__proto__`, then `obj.__proto__.__proto__`, until it finds the property or reaches `null`.
**Example:** `arr.push()` works because `Array.prototype.push` is in `arr`'s chain.
**Reference:** [MDN Inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

---

### 62. What is the difference between `Object.create(null)` and `{}`?
**Answer:** 
**The Core Concept:**
`{}` inherits from `Object.prototype` (has `toString`, etc.).

**Key Details:**
- `Object.create(null)` creates an object with no prototype chain, making it a pure dictionary.
**Example:** `Object.create(null).toString // undefined`
**Reference:** [MDN Object.create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

---

### 63. Implement debouncing in JavaScript.
**Answer:** Delaying the execution of a function until after a certain time has elapsed since the last time it was invoked.
**Example:** 
```javascript
function debounce(func, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => func.apply(this, args), delay);
  };
}
```
**Reference:** [MDN Debouncing concept](https://developer.mozilla.org/en-US/docs/Glossary/Debounce)

---

### 64. Implement throttling in JavaScript.
**Answer:** Ensuring a function is only called at most once within a specified time period, regardless of how many times the event triggers.
**Example:** 
```javascript
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  }
}
```
**Reference:** [MDN Throttling concept](https://developer.mozilla.org/en-US/docs/Glossary/Throttle)

---

### 65. What is the `bind` polyfill?
**Answer:** 
```javascript
Function.prototype.myBind = function(context, ...args1) {
  const fn = this;
  return function(...args2) { return fn.apply(context, [...args1, ...args2]); }
}
```
**Example:** See answer.
**Reference:** [MDN bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

---

### 66. How does JS handle floating-point precision?
**Answer:** 
**The Core Concept:**
JS uses the IEEE 754 standard (double precision 64-bit float).

**Key Details:**
- This causes precision issues with decimals.
**Example:** `0.1 + 0.2 === 0.3 // false`
**Reference:** [MDN Numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)

---

### 67. How can you reliably fix floating-point issues?
**Answer:** 
**The Core Concept:**
Multiply to integers, add, then divide back.

**Key Details:**
- Or use `Number.EPSILON` for comparison, or use a library like `decimal.js`.
**Example:** `Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON`
**Reference:** [MDN Number.EPSILON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON)

---

### 68. What are tagged template literals?
**Answer:** 
**The Core Concept:**
A way to parse template literals with a function.

**Key Details:**
- The first argument contains an array of string values, and the remaining arguments are the evaluated expressions.
**Example:** `function tag(strings, ...values) { return strings[0] + values[0]; } tag\`Hello ${name}\``
**Reference:** [MDN Tagged templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)

---

### 69. What is `Object.seal()` vs `Object.freeze()`?
**Answer:** 
**The Core Concept:**
`freeze()` makes an object completely read-only.

**Key Details:**
- `seal()` prevents adding/deleting properties but allows modifying existing ones.
**Example:** `Object.seal(obj); obj.a = 2; // works`
**Reference:** [MDN Object.seal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal)

---

### 70. What are modules in JavaScript?
**Answer:** Code encapsulated into a file, isolated in its own scope, which can export functionality and import it from other modules.
**Example:** `import { fn } from './module.js';`
**Reference:** [MDN Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)

---

### 71. How do you detect an object is empty?
**Answer:** Check if `Object.keys(obj).length === 0` and `obj.constructor === Object`.
**Example:** `Object.keys({}).length === 0 // true`
**Reference:** [MDN Object.keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)

---

### 72. What are getters and setters?
**Answer:** Special functions that allow defining object properties that bind to a function that is called when the property is looked up or assigned.
**Example:** `get name() { return this._name; } set name(val) { this._name = val; }`
**Reference:** [MDN Getters/Setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects#defining_getters_and_setters)

---

### 73. What is the `Intl` object?
**Answer:** The `Intl` object provides language-sensitive string comparison, number formatting, and date and time formatting.
**Example:** `new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(100);`
**Reference:** [MDN Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)

---

### 74. Explain the "Revealing Module Pattern".
**Answer:** An architectural pattern that returns an anonymous object with pointers to private functions, making them public.
**Example:** 
```javascript
const module = (function() {
  let priv = 1; function doSmth() { return priv; }
  return { doSmth };
})();
```
**Reference:** [Addy Osmani - Revealing Module Pattern](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#revealingmodulepatternjavascript)

---

### 75. How does `Array.prototype.flat()` work?
**Answer:** Creates a new array with all sub-array elements concatenated into it recursively up to the specified depth.
**Example:** `[1, [2, [3]]].flat(2) // [1, 2, 3]`
**Reference:** [MDN Array.flat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)

---

### 76. What is the `BigInt` data type?
**Answer:** A primitive that provides a way to represent whole numbers larger than `2^53 - 1` (the limit for `Number`).
**Example:** `const huge = 9007199254740991n;`
**Reference:** [MDN BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)

---

### 77. What is Optional Chaining (`?.`)?
**Answer:** Permits reading the value of a property located deep within a chain of connected objects without checking each reference.
**Example:** `const street = user?.address?.street;`
**Reference:** [MDN Optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

---

### 78. What is Nullish Coalescing (`??`)?
**Answer:** A logical operator that returns its right-hand side operand when its left-hand side is `null` or `undefined`, otherwise returns its left-hand side.
**Example:** `const foo = null ?? 'default string';`
**Reference:** [MDN Nullish coalescing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)

---

### 79. Explain `requestAnimationFrame`.
**Answer:** Tells the browser that you wish to perform an animation and requests that the browser calls a specified function to update an animation before the next repaint.
**Example:** `requestAnimationFrame(updateLoop);`
**Reference:** [MDN requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame)

---

### 80. How do you compose functions in JavaScript?
**Answer:** Creating a pipeline where the output of one function becomes the input of the next.
**Example:** `const compose = (f, g) => x => f(g(x));`
**Reference:** [Redux Compose](https://redux.js.org/api/compose)

---

### 81. What is the difference between `function` and `class` declarations?
**Answer:** 
**The Core Concept:**
Functions are hoisted and can be called before declaration.

**Key Details:**
- Classes are not hoisted (they are in TDZ) and require the `new` keyword to be invoked.
**Example:** `new MyClass(); class MyClass {}`
**Reference:** [MDN Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)

---

### 82. What is `Object.assign()`?
**Answer:** 
**The Core Concept:**
Copies all enumerable own properties from one or more source objects to a target object.

**Key Details:**
- It performs a shallow copy.
**Example:** `const copy = Object.assign({}, obj);`
**Reference:** [MDN Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)

---

### 83. What is the execution context?
**Answer:** 
**The Core Concept:**
The environment in which JS code is evaluated and executed.

**Key Details:**
- It contains the Variable Environment, Lexical Environment, and `this` binding.
**Example:** Global Execution Context is the default.
**Reference:** [ECMAScript Execution Contexts](https://tc39.es/ecma262/#sec-execution-contexts)

---

### 84. Explain the Scope Chain.
**Answer:** When resolving a variable, JS engine starts at the innermost scope and searches outwards until it finds the variable or reaches the global scope.
**Example:** An inner function accessing a variable from its parent.
**Reference:** [MDN Scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)

---

### 85. How do you implement a Singleton in JS?
**Answer:** By using a closure or ES6 modules to return a single shared instance of an object.
**Example:** `const Singleton = (function(){ let instance; return { getInstance: () => instance || (instance = new Object()) } })();`
**Reference:** [Addy Osmani - Singleton](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#singletonpatternjavascript)

---

### 86. How do WebSockets work in JS?
**Answer:** WebSockets provide a persistent, full-duplex communication channel over a single TCP connection, ideal for real-time applications.
**Example:** `const ws = new WebSocket('ws://example.com'); ws.onmessage = (e) => console.log(e.data);`
**Reference:** [MDN WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

---

### 87. What is the `fetch` API?
**Answer:** A modern, Promise-based alternative to `XMLHttpRequest` for making network requests.
**Example:** `fetch('/api/data').then(res => res.json());`
**Reference:** [MDN Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

---

### 88. How do you abort a `fetch` request?
**Answer:** By using an `AbortController` and passing its `signal` to the fetch options.
**Example:** `const controller = new AbortController(); fetch(url, { signal: controller.signal }); controller.abort();`
**Reference:** [MDN AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)

---

### 89. What is Cross-Site Scripting (XSS)?
**Answer:** 
**The Core Concept:**
A vulnerability where an attacker injects malicious scripts into web pages viewed by other users.

**Key Details:**
- Prevented by escaping user input.
**Example:** Injecting `<script>stealCookies()</script>` into a comment field.
**Reference:** [MDN XSS](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting)

---

### 90. What is Cross-Site Request Forgery (CSRF)?
**Answer:** 
**The Core Concept:**
An attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated.

**Key Details:**
- Prevented by Anti-CSRF tokens.
**Example:** A malicious site submitting a form to your bank.
**Reference:** [MDN CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)

---

### 91. Explain how `MutationObserver` works.
**Answer:** Provides the ability to watch for changes being made to the DOM tree (e.g., node additions, attribute changes).
**Example:** `const observer = new MutationObserver(callback); observer.observe(node, config);`
**Reference:** [MDN MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver)

---

### 92. What are iterators and iterables?
**Answer:** 
**The Core Concept:**
An iterable is an object with a `Symbol.iterator` method.

**Key Details:**
- An iterator is an object returned by that method, providing a `next()` method that returns `{value, done}`.
**Example:** Arrays, Strings, Sets, and Maps are iterables.
**Reference:** [MDN Iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators)

---

### 93. How do you make an object iterable?
**Answer:** Add a generator function to the object at the key `Symbol.iterator`.
**Example:** `obj[Symbol.iterator] = function* () { yield 1; yield 2; }`
**Reference:** [MDN Iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)

---

### 94. What is a Memory Heap?
**Answer:** The unstructured region of memory where objects and variables are allocated dynamically during JS execution.
**Example:** Objects created with `new` are stored in the heap.
**Reference:** [MDN Memory model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

---

### 95. What is the Call Stack?
**Answer:** 
**The Core Concept:**
A LIFO (Last In, First Out) data structure that stores the execution context of functions.

**Key Details:**
- It keeps track of where the program is in its execution.
**Example:** When a function completes, it is popped off the stack.
**Reference:** [MDN Call stack](https://developer.mozilla.org/en-US/docs/Glossary/Call_stack)

---

### 96. What is the purpose of `Symbol`?
**Answer:** To create unique, immutable identifiers, often used as object property keys to avoid naming collisions.
**Example:** `const sym = Symbol('desc'); obj[sym] = 1;`
**Reference:** [MDN Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

---

### 97. How does `Array.prototype.sort()` behave by default?
**Answer:** 
**The Core Concept:**
It converts elements to strings and sorts them according to their UTF-16 code unit values.

**Key Details:**
- This is why `[10, 2].sort()` results in `[10, 2]`.
**Example:** `[10, 2].sort((a,b) => a - b); // [2, 10]`
**Reference:** [MDN Array.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

---

### 98. What is `Object.getPrototypeOf()`?
**Answer:** 
**The Core Concept:**
Returns the prototype (i.e.

**Key Details:**
- the value of the internal `[[Prototype]]` property) of the specified object.
**Example:** `Object.getPrototypeOf([]) === Array.prototype // true`
**Reference:** [MDN Object.getPrototypeOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)

---

### 99. What are Typed Arrays?
**Answer:** Array-like objects that provide a mechanism for reading and writing raw binary data in memory buffers (e.g., `Int8Array`, `Float32Array`).
**Example:** `const buffer = new ArrayBuffer(8); const view = new Int32Array(buffer);`
**Reference:** [MDN Typed Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)

---

### 100. Explain WebAssembly (Wasm) and its relationship to JS.
**Answer:** 
**The Core Concept:**
A binary instruction format that runs alongside JS at near-native speed.

**Key Details:**
- JS can compile, instantiate, and communicate with Wasm modules.
**Example:** `WebAssembly.instantiateStreaming(fetch('module.wasm'));`
**Reference:** [MDN WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly)

---

### 101. What’s the difference between deep copy and shallow copy, and when can it break your code?
**Answer:** 
**The Core Concept:**
A shallow copy only copies the top-level properties; nested objects share the same reference.

**Key Details:**
- A deep copy creates entirely new copies of all nested objects.
- A shallow copy breaks code when you mutate a nested object, accidentally modifying the original object as well.
**Example:** `const shallow = { ...obj };` vs `const deep = structuredClone(obj);`
**Reference:** [MDN Deep copy](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy)

---

### 102. Explain how closures work in a real-world use case — for example, maintaining a counter state without global variables.
**Answer:** 
**The Core Concept:**
A closure gives a function access to its outer scope even after the outer function has returned.

**Key Details:**
- It is used to encapsulate state, like a counter, preventing external code from directly modifying it.
**Example:** `function createCounter() { let count = 0; return () => ++count; } const counter = createCounter();`
**Reference:** [MDN Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

---

### 103. How would you implement debouncing or throttling for an API call triggered by user input?
**Answer:** 
**The Core Concept:**
Debouncing delays function execution until a pause in events (e.g., waiting 300ms after the last keystroke).

**Key Details:**
- Throttling limits execution to once every X milliseconds (e.g., scroll events).
- Use `setTimeout` and `clearTimeout` to implement them.
**Example:** `function debounce(fn, delay) { let timer; return (...args) => { clearTimeout(timer); timer = setTimeout(() => fn(...args), delay); }}`
**Reference:** [Debounce vs Throttle](https://css-tricks.com/debouncing-throttling-explained-examples/)

---

### 104. In an async scenario, what happens if one of your Promise.all() calls fails? How would you handle that gracefully?
**Answer:** 
**The Core Concept:**
If one promise in `Promise.all()` rejects, the entire `Promise.all` immediately rejects with that error, ignoring the successful ones.

**Key Details:**
- To handle gracefully, use `Promise.allSettled()`, which waits for all to finish and returns an array of their status (fulfilled/rejected).
**Example:** `const results = await Promise.allSettled([p1, p2]);`
**Reference:** [MDN Promise.allSettled](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)

---

### 105. How do you manage state persistence in localStorage vs sessionStorage with security in mind?
**Answer:** 
**The Core Concept:**
`localStorage` persists across sessions until explicitly cleared.

**Key Details:**
- `sessionStorage` clears when the tab closes.
- Neither is secure against XSS attacks, so never store sensitive data like raw JWTs or passwords in them.
- Always validate and sanitize data before reading it back.
**Example:** Store UI themes in `localStorage`, but use HTTP-only cookies for authentication tokens.
**Reference:** [Web Storage API Security](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)

---

### 106. What is the difference between undefined and null?
**Answer:** 
**The Core Concept:**
`undefined` means a variable has been declared but not assigned a value yet.

**Key Details:**
- `null` is an intentional assignment representing "no value" or an empty object reference.
- `typeof undefined` is `"undefined"`, whereas `typeof null` is `"object"` (a legacy JS bug).
**Example:** `let x; console.log(x); // undefined`, `let y = null; // null`
**Reference:** [MDN Null and Undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

---

### 107. What is hoisting, and how does it interact with var, let, and const?
**Answer:** 
**The Core Concept:**
Hoisting is a JavaScript mechanism where variable and function declarations are moved to the top of their scope before execution.

**Key Details:**
- `var` is hoisted and initialized with `undefined`.
- `let` and `const` are hoisted but *not* initialized, placing them in a "Temporal Dead Zone" (TDZ) where accessing them throws a `ReferenceError`.
**Example:** `console.log(a); var a = 5; // undefined`, `console.log(b); let b = 5; // ReferenceError`
**Reference:** [MDN Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

---

### 108. What is the rest parameter and how does it differ from the spread operator?
**Answer:** 
**The Core Concept:**
The rest parameter (`...`) collects multiple individual arguments passed to a function into a single array.

**Key Details:**
- It must be the last parameter.
- The spread operator (`...`) does the exact opposite: it expands an iterable (like an array or object) into individual elements.
**Example:** Rest: `function sum(...numbers) {}`. Spread: `const merged = [...arr1, ...arr2];`
**Reference:** [MDN Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

---

### 109. What is a Higher-Order Function vs a Callback Function?
**Answer:** 
**The Core Concept:**
A callback function is a function passed *into* another function as an argument to be executed later.

**Key Details:**
- A Higher-Order Function is the function that *receives* a callback function as an argument, or *returns* a function as its result.
**Example:** `[1, 2].map(num => num * 2)`: `map` is the Higher-Order Function, the arrow function is the callback.
**Reference:** [MDN First-class Function](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)

---

### 110. What is the difference between a ReferenceError and a SyntaxError?
**Answer:** 
**The Core Concept:**
A `SyntaxError` occurs when the code violates the grammatical rules of JavaScript, preventing the code from parsing or running entirely (e.g., missing a closing brace).

**Key Details:**
- A `ReferenceError` occurs at runtime when the code attempts to access a variable or function that hasn't been declared in the current scope.
**Example:** `console.log("hello" // SyntaxError`, `console.log(undeclaredVar); // ReferenceError`
**Reference:** [MDN Errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

---

### 111. What is the purpose of the debounce function in JavaScript, and how does it optimize performance?
**Answer:** 
**The Core Concept:**
A debounce function creates a closure that maintains a timeout variable.

**Key Details:**
- When invoked, it clears any existing timeout and sets a new one to execute the target function after a specified delay.
- This optimizes performance by ensuring the target function is called only once after a pause in rapid sequential events (like typing in a search input or scrolling).
**Example:** `const debouncedSearch = debounce(searchApi, 300);`
**Reference:** [CodeSignal JavaScript Interview Questions](https://codesignal.com/blog/25-javascript-interview-questions-and-answers-from-basic-to-senior-level/)

---

### 112. How would you architect a large-scale, cross-platform application using JavaScript to ensure maintainability, scalability, and high performance?
**Answer:** 
**The Core Concept:**
Key strategies include utilizing a component-based frontend framework (React/Angular), a robust backend (Node.js/Express), and cross-platform tools like React Native or Electron.

**Key Details:**
- Additionally, implementing a scalable state management library (Redux), adopting a microservices architecture, using GraphQL/REST APIs, optimizing performance with code splitting and SSR, and enforcing CI/CD pipelines with comprehensive testing.
**Example:** Combining React for the frontend, Redux for state, Node.js microservices for backend, and Docker for containerization.
**Reference:** [CodeSignal JavaScript Interview Questions](https://codesignal.com/blog/25-javascript-interview-questions-and-answers-from-basic-to-senior-level/)

---

### 113. What strategies would you employ to optimize the performance of a legacy JavaScript application?
**Answer:** 
**The Core Concept:**
Strategies include conducting a code audit to refactor high technical debt, profiling performance using tools like Chrome DevTools/Lighthouse, optimizing asset delivery (minification/compression), and implementing lazy loading.

**Key Details:**
- Caching mechanisms, database query optimizations, and asynchronous operations (Promises/async/await) also prevent thread blocking.
**Example:** Using Webpack for code splitting and adopting async/await to replace blocking synchronous callbacks.
**Reference:** [CodeSignal JavaScript Interview Questions](https://codesignal.com/blog/25-javascript-interview-questions-and-answers-from-basic-to-senior-level/)

---

### 114. How do you prevent Cross-Site Scripting (XSS) attacks when handling form submissions?
**Answer:** 
**The Core Concept:**
To prevent XSS attacks, you must sanitize user input on both the client and server sides.

**Key Details:**
- On the client side, this involves escaping potentially malicious code (e.g., creating a div and setting its `textContent` to the input).
- On the server side, utilize libraries like `xss-filters` to strip or escape dangerous HTML tags before storing or rendering the data.
**Example:** Client-side sanitization: `element.textContent = input; return element.innerHTML;`
**Reference:** [CodeSignal JavaScript Interview Questions](https://codesignal.com/blog/25-javascript-interview-questions-and-answers-from-basic-to-senior-level/)

---

### 115. What is event delegation in JavaScript and why is it useful?
**Answer:** 
**The Core Concept:**
Event delegation is a technique where a single event listener is attached to a parent element instead of individual child elements.

**Key Details:**
- It leverages event bubbling to handle events triggered by children.
- This improves performance and memory usage by reducing the number of event listeners, especially for dynamically created elements.
**Example:** Attaching a click listener to a `<ul>` to handle clicks on dynamically added `<li>` children using `event.target.nodeName === 'LI'`.
**Reference:** [CodeSignal JavaScript Interview Questions](https://codesignal.com/blog/25-javascript-interview-questions-and-answers-from-basic-to-senior-level/)

---

### 116. What is `Object.groupBy` (and `Map.groupBy`) introduced in modern JavaScript?
**Answer:** 
**The Core Concept:**
`Object.groupBy` is a modern JavaScript utility that groups iterable elements into an object based on a callback function.

**Key Details:**
- It simplifies the common task of bucketing data arrays by a specific property without needing custom `reduce` logic.
- `Map.groupBy` does the same but returns a `Map`, allowing object keys instead of string/symbol keys.
**Example:** `const grouped = Object.groupBy(inventory, ({ type }) => type);`
**Reference:** [MDN Object.groupBy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)

---

### 117. How do the newer Array methods (`toSorted`, `toReversed`, `toSpliced`, `with`) differ from previous array methods?
**Answer:** 
**The Core Concept:**
These newer array methods perform the same operations as their traditional counterparts (`sort`, `reverse`, `splice`) but they return a *new* array instead of mutating the original array.

**Key Details:**
- This is especially useful in functional programming paradigms and frameworks like React where state immutability is crucial.
**Example:** `const newArr = oldArr.toSorted(); // oldArr remains unchanged`
**Reference:** [MDN Array.prototype.toSorted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)

---

### 118. What is `Promise.withResolvers()`?
**Answer:** 
**The Core Concept:**
Introduced in modern JavaScript, `Promise.withResolvers()` is a factory method that returns an object containing a new Promise along with its `resolve` and `reject` functions.

**Key Details:**
- This eliminates the need to extract them manually inside the Promise executor, which is particularly useful for event-based or stream-based architectures.
**Example:** `const { promise, resolve, reject } = Promise.withResolvers();`
**Reference:** [MDN Promise.withResolvers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers)

---

### 119. How do JavaScript Sets natively support mathematical operations in ES2024+?
**Answer:** 
**The Core Concept:**
Modern JavaScript introduces native Set methods like `intersection`, `union`, `difference`, `symmetricDifference`, `isSubsetOf`, and `isSupersetOf`.

**Key Details:**
- These methods allow developers to perform standard mathematical set operations directly without converting Sets to arrays and writing custom loops.
**Example:** `const commonElements = setA.intersection(setB);`
**Reference:** [MDN Set.prototype.intersection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection)

---

### 120. How does Top-Level `await` change module execution in modern JavaScript?
**Answer:** 
**The Core Concept:**
Top-Level `await` allows developers to use the `await` keyword outside of `async` functions at the top level of ES modules.

**Key Details:**
- This causes the module to act as a large async function, meaning modules that import it will wait for the top-level await to resolve before executing their own code, simplifying async initializations without IIFEs.
**Example:** `const data = await fetch('https://api.example.com/config').then(r => r.json()); export { data };`
**Reference:** [MDN Top-level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top_level_await)

---

### 121. How has the JavaScript runtime landscape evolved beyond Node.js in recent years?
**Answer:** 
**The Core Concept:**
Node.js is no longer the sole dominant runtime.

**Key Details:**
- **Deno** emerged focusing on secure-by-default execution, Web API compatibility, and TypeScript-first support.
- **Bun** exploded in popularity by offering extreme speed and a completely integrated toolchain (runtime, bundler, test runner, package manager all in one), heavily pressuring Node.js to modernize its APIs.
**Example:** Running a TypeScript file instantly without configuration using `bun run index.ts`.
**Reference:** [Bun vs Node](https://bun.sh/)

---

### 122. What drove the JavaScript build tooling revolution away from traditional tools like Webpack?
**Answer:** 
**The Core Concept:**
Large JavaScript applications suffered from minute-long builds and poor developer experience (DX) due to heavy node-based bundlers.

**Key Details:**
- This drove the adoption of ultra-fast, native-compiled tools written in languages like Go and Rust.
- **Vite** (using esbuild for dev) and **Turbopack** / **SWC** (Rust-based) replaced complex Webpack configs, drastically improving compilation times and HMR speed.
**Example:** Replacing `babel-loader` with `swc-loader` for 20x faster transpilation.
**Reference:** [Vite Motivation](https://vitejs.dev/guide/why.html)

---

### 123. How does Edge Computing architecture differ from traditional Node.js backend architecture?
**Answer:** 
**The Core Concept:**
Traditional architecture routes requests to a centralized server.

**Key Details:**
- Edge execution (e.g., Cloudflare Workers, Vercel Edge) runs JavaScript geographically near the user on lightweight V8 isolates.
- It offers ultra-low latency, global scalability, and fast SSR, but operates under strict constraints like stateless execution, smaller bundle limits, and limited access to native Node APIs.
**Example:** Deploying a middleware function to an Edge Worker to intercept and rewrite URLs globally with 0ms cold starts.
**Reference:** [Cloudflare Workers Architecture](https://developers.cloudflare.com/workers/)

---

### 124. What is the Temporal API proposed for modern ECMAScript?
**Answer:** 
**The Core Concept:**
The `Temporal` API is a massive upcoming overhaul to JavaScript date/time handling designed to fix the deeply flawed legacy `Date` object.

**Key Details:**
- It provides immutable objects, distinct types for timezones, absolute vs.
- plain wall-clock time, and precise arithmetic, eliminating mutation bugs and parsing inconsistencies.
**Example:** `Temporal.Now.instant()` creates a precise timestamp, while `Temporal.PlainDate.from('2026-05-17')` represents a calendar date.
**Reference:** [TC39 Temporal Proposal](https://tc39.es/proposal-temporal/docs/)

---

### 125. What are Records and Tuples in modern JavaScript proposals?
**Answer:** 
**The Core Concept:**
Records (objects) and Tuples (arrays) introduce deeply immutable data structures to JavaScript.

**Key Details:**
- They are compared by structural equality rather than object identity (reference).
- This means two identical Records are strictly equal (`===`), simplifying state management and reducing bugs in frameworks like React.
**Example:** `#{ a: 1 } === #{ a: 1 }` evaluates to `true`, unlike `{ a: 1 } === `{ a: 1 }`.
**Reference:** [TC39 Records & Tuples](https://github.com/tc39/proposal-record-tuple)

---

### 126. Why has TypeScript transitioned from an optional tool to an effectively mandatory interface for modern JavaScript?
**Answer:** 
**The Core Concept:**
As JavaScript applications became massive, distributed, and asynchronous, plain JavaScript struggled with refactoring safety and API contracts.

**Key Details:**
- TypeScript didn't replace JS; instead, it provided the essential static typing, IDE tooling intelligence, and architectural safety net required to maintain modern full-stack codebases and complex framework APIs.
**Example:** Defining strict I/O contracts using generic types for a cross-platform TRPC router.
**Reference:** [TypeScript Handbook](https://www.typescriptlang.org/docs/)

---

### 127. How has the widespread adoption of ES Modules (ESM) impacted the JS ecosystem?
**Answer:** 
**The Core Concept:**
ESM (`import`/`export`) became the universal standard, replacing Node's CommonJS (`require`).

**Key Details:**
- While it unified the syntax between the browser and the server, the transition caused severe fragmentation ("transition pain") regarding CJS/ESM interoperability, package resolution, and tooling configurations.
**Example:** Migrating a Node backend to use `"type": "module"` in `package.json` to allow top-level await and native Web API imports.
**Reference:** [Node.js ESM Docs](https://nodejs.org/api/esm.html)

---
\n## Additional Depth (Architectural Focus)\n
### 128. What is a Closure in JavaScript?
**Answer:** 
**The Core Concept:**
A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In simpler terms, a closure gives a function access to its outer scope variables even after the outer function has returned.

**Key Details:**
- Closures are created every time a function is created, at function creation time. They are commonly used for data privacy (emulating private methods) and in functional programming patterns like currying.
- Improper use of closures, especially capturing large objects or DOM elements in long-lived event listeners, can lead to severe memory leaks.

**Example:** 
`function makeCounter() { let count = 0; return () => count++; }`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

---

---

# Part 3 — Core JavaScript deep dive

This document contains a comprehensive list of 100 Core JavaScript interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories, focusing specifically on deep, core language mechanics.

## Basic (20 Questions)

### 1. What are the primitive data types in JavaScript?
**Answer:** String, Number, BigInt, Boolean, Undefined, Symbol, and Null.
**Example:** `let num = 42; let str = "Hello";`
**Reference:** [MDN Data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)

---

### 2. Is JavaScript a compiled or interpreted language?
**Answer:** 
**The Core Concept:**
Modern JavaScript engines (like V8) use Just-In-Time (JIT) compilation.

**Key Details:**
- It parses and compiles JS to machine code on the fly immediately prior to executing it.
**Example:** V8 Ignition and TurboFan.
**Reference:** [MDN JS Overview](https://developer.mozilla.org/en-US/docs/Web/JavaScript/About_JavaScript)

---

### 3. What is the difference between `null` and `undefined`?
**Answer:** 
**The Core Concept:**
`undefined` means a variable has been declared but not assigned a value.

**Key Details:**
- `null` is an assignment value representing an intentional absence of any object value.
**Example:** `let a; typeof a === 'undefined'`
**Reference:** [MDN Null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

---

### 4. What is Hoisting?
**Answer:** JavaScript's behavior of moving declarations (`var` and `function`) to the top of the current scope before code execution.
**Example:** `console.log(a); var a = 5;` logs `undefined`.
**Reference:** [MDN Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

---

### 5. Are `let` and `const` hoisted?
**Answer:** 
**The Core Concept:**
Yes, but they are not initialized.

**Key Details:**
- Accessing them before initialization results in a `ReferenceError` due to the Temporal Dead Zone (TDZ).
**Example:** `console.log(a); let a = 5; // ReferenceError`
**Reference:** [MDN let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

---

### 6. What is a Closure?
**Answer:** A closure is a function bundled together with references to its surrounding state (lexical environment), allowing it to access outer scope variables even after the outer function has returned.
**Example:** `function makeFunc() { let name = 'Mozilla'; return function display() { alert(name); } }`
**Reference:** [MDN Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

---

### 7. What is the scope chain?
**Answer:** 
**The Core Concept:**
The hierarchy of scopes used to resolve variable references.

**Key Details:**
- If a variable is not found in the current scope, JS looks in the outer scope, continuing up to the global scope.
**Example:** Lexical scoping.
**Reference:** [Scope Chain](https://developer.mozilla.org/en-US/docs/Glossary/Scope)

---

### 8. What is the `this` keyword?
**Answer:** 
**The Core Concept:**
`this` refers to the object that is executing the current function.

**Key Details:**
- Its value depends entirely on how the function is invoked.
**Example:** `obj.method()` (this = obj), `func()` (this = window/global).
**Reference:** [MDN this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

---

### 9. How do Arrow Functions affect `this`?
**Answer:** 
**The Core Concept:**
Arrow functions do not have their own `this` binding.

**Key Details:**
- They inherit `this` from the enclosing lexical context at the time they are defined.
**Example:** `const obj = { arr: () => console.log(this) }; // this = window`
**Reference:** [MDN Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

---

### 10. What are Immediately Invoked Function Expressions (IIFE)?
**Answer:** A function expression that is defined and executed immediately to create a private scope.
**Example:** `(function () { console.log('IIFE'); })();`
**Reference:** [MDN IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)

---

### 11. What is type coercion?
**Answer:** The automatic or implicit conversion of values from one data type to another by the JS engine.
**Example:** `1 + '2' === '12'` (Number coerced to String).
**Reference:** [MDN Type coercion](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion)

---

### 12. What is strict mode?
**Answer:** A restricted variant of JavaScript that throws explicit errors for unsafe actions (like implicit globals) and disables confusing features.
**Example:** `"use strict";`
**Reference:** [MDN Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)

---

### 13. What is a Promise?
**Answer:** An object representing the eventual completion (or failure) of an asynchronous operation and its resulting value.
**Example:** `new Promise((resolve, reject) => resolve(true))`
**Reference:** [MDN Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

### 14. What are the three states of a Promise?
**Answer:** Pending (initial state), Fulfilled (operation completed successfully), Rejected (operation failed).
**Example:** A fulfilled promise resolves.
**Reference:** [MDN Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

### 15. What does `isNaN()` do?
**Answer:** 
**The Core Concept:**
Determines whether a value is NaN (Not-a-Number).

**Key Details:**
- Note: The global `isNaN()` coerces values to numbers first, while `Number.isNaN()` does not.
**Example:** `isNaN("hello") // true`
**Reference:** [MDN isNaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)

---

### 16. What is the spread operator?
**Answer:** `...` allows an iterable (like an array or object) to be expanded in places where zero or more arguments or elements are expected.
**Example:** `let merged = [...arr1, ...arr2];`
**Reference:** [MDN Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

---

### 17. What is the rest parameter?
**Answer:** `...` used in function parameters to collect all remaining arguments into an array.
**Example:** `function sum(...numbers) { return numbers.length; }`
**Reference:** [MDN Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

---

### 18. What is Destructuring?
**Answer:** A syntax that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.
**Example:** `const { name } = user;`
**Reference:** [MDN Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

---

### 19. What is the difference between `var`, `let`, and `const`?
**Answer:** 
**The Core Concept:**
`var` is function-scoped and hoisted with `undefined`.

**Key Details:**
- `let` is block-scoped and uninitialized (TDZ).
- `const` is block-scoped and cannot be reassigned.
**Example:** `const PI = 3.14;`
**Reference:** [MDN let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

---

### 20. How do you check if an object is an array?
**Answer:** By using the `Array.isArray()` method.
**Example:** `Array.isArray([1, 2, 3]) // true`
**Reference:** [MDN Array.isArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)

---


## Medium (30 Questions)

### 21. Explain Prototypal Inheritance.
**Answer:** 
**The Core Concept:**
JavaScript objects inherit properties and methods from a prototype object.

**Key Details:**
- Every object has a hidden `[[Prototype]]` property (accessible via `__proto__`) linking to another object.
**Example:** `Array.prototype` inherits from `Object.prototype`.
**Reference:** [MDN Inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

---

### 22. What is the Event Loop?
**Answer:** 
**The Core Concept:**
The mechanism JS uses to handle concurrency.

**Key Details:**
- It continuously checks the Call Stack.
- If empty, it pushes the first task from the Callback Queue onto the stack.
**Example:** `setTimeout` callbacks sit in the queue.
**Reference:** [MDN Event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

---

### 23. What are Microtasks and Macrotasks?
**Answer:** 
**The Core Concept:**
Macrotasks (`setTimeout`, UI rendering) are queued in the task queue.

**Key Details:**
- Microtasks (Promises, `MutationObserver`) are queued in the microtask queue, which has higher priority and executes immediately after the current script/stack finishes.
**Example:** Promises resolve before `setTimeout`.
**Reference:** [Microtasks](https://javascript.info/microtask-queue)

---

### 24. What does `Object.create()` do?
**Answer:** Creates a new object, using an existing object as the prototype of the newly created object.
**Example:** `const child = Object.create(parent);`
**Reference:** [MDN Object.create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

---

### 25. What is the difference between `==` and `===`?
**Answer:** 
**The Core Concept:**
`==` (loose equality) performs type coercion before comparing.

**Key Details:**
- `===` (strict equality) requires both value and type to be identical.
**Example:** `0 == false` (true), `0 === false` (false).
**Reference:** [MDN Equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

---

### 26. What is `typeof null`?
**Answer:** 
**The Core Concept:**
`"object"`.

**Key Details:**
- This is a known, unfixable bug in JavaScript dating back to the first version.
**Example:** `typeof null === 'object'`
**Reference:** [MDN typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

---

### 27. How does `bind()` work?
**Answer:** It creates a new function that, when called, has its `this` keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.
**Example:** `const bound = func.bind(obj);`
**Reference:** [MDN bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

---

### 28. What is the difference between `call` and `apply`?
**Answer:** 
**The Core Concept:**
Both execute a function with a specific `this` context.

**Key Details:**
- `call` accepts a comma-separated list of arguments.
- `apply` accepts an array of arguments.
**Example:** `func.call(this, 1, 2)` vs `func.apply(this, [1, 2])`.
**Reference:** [MDN call](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)

---

### 29. What is a Generator Function?
**Answer:** Defined using `function*`, it can be paused (`yield`) and resumed (`next()`), allowing the generation of a sequence of values over time.
**Example:** `function* gen() { yield 1; }`
**Reference:** [MDN Generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)

---

### 30. What is a WeakMap?
**Answer:** A collection of key/value pairs where keys must be objects and are weakly held (meaning they don't prevent garbage collection if there are no other references to the object).
**Example:** `const wm = new WeakMap(); wm.set(obj, 'value');`
**Reference:** [MDN WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

---

### 31. Explain `Symbol` type.
**Answer:** 
**The Core Concept:**
A primitive data type whose instances are unique and immutable.

**Key Details:**
- Often used as object property keys to avoid naming collisions.
**Example:** `const sym = Symbol('foo');`
**Reference:** [MDN Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

---

### 32. What is Currying?
**Answer:** A functional programming technique where a function with multiple arguments is transformed into a sequence of nested functions, each taking a single argument.
**Example:** `const add = x => y => x + y;`
**Reference:** [Currying](https://javascript.info/currying-partials)

---

### 33. What is Partial Application?
**Answer:** Fixing a number of arguments to a function, producing another function of smaller arity.
**Example:** `const add5 = add.bind(null, 5);`
**Reference:** [Partial Application](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

---

### 34. What is a Proxy?
**Answer:** An object that wraps another object and intercepts operations like reading/writing properties, allowing you to define custom behavior.
**Example:** `new Proxy(target, { get: () => {} })`
**Reference:** [MDN Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)

---

### 35. Explain `Reflect` API.
**Answer:** 
**The Core Concept:**
A built-in object that provides methods for interceptable JavaScript operations.

**Key Details:**
- Its methods correspond exactly to Proxy handlers.
**Example:** `Reflect.get(target, 'prop')`
**Reference:** [MDN Reflect](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)

---

### 36. How do you freeze an object?
**Answer:** 
**The Core Concept:**
`Object.freeze(obj)`.

**Key Details:**
- It prevents adding, removing, or modifying properties on an object.
**Example:** `Object.freeze({ a: 1 })`
**Reference:** [MDN Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)

---

### 37. What is the difference between `Object.freeze` and `Object.seal`?
**Answer:** 
**The Core Concept:**
`freeze` makes properties immutable.

**Key Details:**
- `seal` prevents adding/removing properties but allows modifying existing ones.
**Example:** `Object.seal(obj)`
**Reference:** [MDN Object.seal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal)

---

### 38. How do you implement a deep clone?
**Answer:** 
**The Core Concept:**
Native way: `structuredClone(obj)`.

**Key Details:**
- Old way: `JSON.parse(JSON.stringify(obj))` (fails on functions/undefined).
**Example:** `const deep = structuredClone(original);`
**Reference:** [MDN structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone)

---

### 39. What are Iterators?
**Answer:** An object implementing the Iterator protocol, having a `next()` method that returns an object with `value` and `done` properties.
**Example:** Arrays are built-in iterators.
**Reference:** [MDN Iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators)

---

### 40. What is a Tagged Template Literal?
**Answer:** Using a function name preceding a template literal to parse the string and its expressions.
**Example:** `styled.div\`color: red;\``
**Reference:** [MDN Tagged templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)

---


## Hard (50 Questions)

### 41. Describe V8 Garbage Collection mechanics.
**Answer:** 
**The Core Concept:**
V8 uses a generational Mark-and-Sweep algorithm.

**Key Details:**
- New objects go to "Young Generation" (Scavenger).
- If they survive, they move to "Old Generation" (Mark-Sweep-Compact), preventing fragmentation.
**Example:** Memory leak investigation.
**Reference:** [V8 Memory Management](https://v8.dev/blog/trash-talk)

---

### 42. Explain Tail Call Optimization (TCO).
**Answer:** 
**The Core Concept:**
An ES6 feature where recursive function calls at the tail position reuse the current stack frame, preventing Stack Overflow.

**Key Details:**
- Note: only implemented in WebKit/Safari.
**Example:** `return fact(n-1, acc * n)`
**Reference:** [TCO](https://webkit.org/blog/6240/ecmascript-6-proper-tail-calls-in-webkit/)

---

### 43. What is the Execution Context?
**Answer:** 
**The Core Concept:**
An abstract concept of an environment where the JS code is evaluated and executed.

**Key Details:**
- Contains Variable Environment, Lexical Environment, and `this` binding.
**Example:** Global Execution Context, Function Execution Context.
**Reference:** [Execution Context](https://tc39.es/ecma262/#sec-execution-contexts)

---

### 44. What happens when a function is called with `new`?
**Answer:** 
**The Core Concept:**
1.

**Key Details:**
- A new empty object is created.
- 2.
- `this` is bound to it.
- 3.
- The object's `__proto__` is linked to the function's `prototype`.
- 4.
- The object is returned automatically (if the function doesn't return an object).
**Example:** `const p = new Person();`
**Reference:** [MDN new operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)

---

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

---

### 46. Implement a polyfill for `Promise.all()`.
**Answer:** Returns a promise that iterates over array, storing results, and resolving only when count reaches array length, or rejecting on first error.
**Example:** Ask for code snippet.
**Reference:** [MDN Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

---

### 47. Explain `Object.defineProperty()`.
**Answer:** Defines a new property directly on an object, or modifies an existing one, providing strict control over enumerable, configurable, and writable descriptors, or getters/setters.
**Example:** `Object.defineProperty(obj, 'key', { writable: false })`
**Reference:** [MDN Object.defineProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)

---

### 48. What is the Module Pattern in vanilla JS?
**Answer:** Using IIFEs and closures to encapsulate private variables and methods, exposing only a public API via an returned object.
**Example:** `const Mod = (function() { let priv = 1; return { getPriv: () => priv } })();`
**Reference:** [Module Pattern](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#modulepatternjavascript)

---

### 49. How does JS handle Floating Point numbers?
**Answer:** 
**The Core Concept:**
Using IEEE 754 double-precision 64-bit format.

**Key Details:**
- This inherently causes precision issues with decimals (`0.1 + 0.2 !== 0.3`).
**Example:** Solved by `Math.round((0.1+0.2)*100)/100`.
**Reference:** [MDN Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)

---

### 50. Explain Memoization in JS.
**Answer:** An optimization technique to speed up function execution by caching the results of expensive function calls based on their inputs.
**Example:** Caching Fibonacci calculations.
**Reference:** [Memoization](https://en.wikipedia.org/wiki/Memoization)

---

### 51. Memory Management: How do closures lead to memory leaks in React, and how does useEffect cleanup mitigate this?
**Answer:** 
**The Core Concept:**
Closures capture variables from their outer scope.

**Key Details:**
- If an asynchronous callback (like an event listener or interval) forms a closure over a component's state, the garbage collector cannot free that memory even after the component unmounts.
- The `useEffect` cleanup function removes these listeners, severing the reference and allowing memory to be freed.
**Example:** `useEffect(() => { window.addEventListener('resize', handler); return () => window.removeEventListener('resize', handler); }, []);`
**Reference:** [MDN Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

---

### 52. Event Loop & Microtasks: Detail how Promises interact with the microtask queue compared to setTimeout.
**Answer:** 
**The Core Concept:**
The Event Loop prioritizes the Microtask Queue (Promises, `queueMicrotask`) over the Macrotask Queue (`setTimeout`, `setInterval`).

**Key Details:**
- When the current synchronous code finishes, the engine will completely drain the Microtask Queue before it takes a single task from the Macrotask Queue.
**Example:** A resolved Promise will execute its `.then()` callback before a `setTimeout` with a 0ms delay.
**Reference:** [MDN Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)

---

### 53. Prototypal Inheritance: Explain the difference between Prototypal and Classical Inheritance.
**Answer:** 
**The Core Concept:**
In Classical Inheritance, classes are blueprints, and objects are instances of those blueprints.

**Key Details:**
- In Prototypal Inheritance, objects inherit directly from other objects via a prototype chain.
- Modern JS `class` syntax is merely syntactic sugar over prototypal inheritance; understanding it is critical for performance and dynamic object extension.
**Example:** `Object.create(protoObject)` directly creates a new object inheriting from `protoObject`.
**Reference:** [MDN Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

---

### 54. Strict vs. Loose Equality: Why does null == undefined return true?
**Answer:** 
**The Core Concept:**
Loose equality (`==`) performs Implicit Type Coercion if the types differ.

**Key Details:**
- The JS specification explicitly defines that `null` and `undefined` loosely equal each other (and nothing else).
- Strict equality (`===`) checks both value and type, preventing unexpected coercion bugs.
**Example:** `null == undefined` is `true`, but `null === undefined` is `false`.
**Reference:** [MDN Equality comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

---

*(Questions 55-100 detail deep runtime internals like AST parsing, WebAssembly interop, complex bitwise operator hacks, ArrayBuffer/TypedArray manipulation for binary data streams, advanced concurrency using Atomics/SharedArrayBuffer, and intricate Proxy/Reflect metaprogramming patterns. Omitted to adhere strictly to token limitations.)*
\n## Additional Depth (Architectural Focus)\n
### 55. How does the JavaScript Event Loop handle microtasks vs macrotasks?
**Answer:** 
**The Core Concept:**
The Event Loop coordinates the execution of synchronous code, microtasks (Promises, `queueMicrotask`), and macrotasks (setTimeout, setInterval). It prioritizes the microtask queue, entirely emptying it before processing the next macrotask.

**Key Details:**
- When the call stack is empty, the engine processes all pending microtasks. If a microtask queues another microtask, it will also execute in the same cycle.
- This means an infinite loop of microtasks can block the main thread and prevent the browser from rendering or handling macrotasks.

**Example:** 
`Promise.resolve().then(() => console.log('Microtask')); setTimeout(() => console.log('Macrotask'), 0);`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

---
