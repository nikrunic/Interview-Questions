# Node.js Interview Questions

This document contains a comprehensive list of Node.js interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is Node.js?
**Answer:** Node.js is an open-source, cross-platform JavaScript runtime environment that executes JavaScript code outside a web browser, typically used for server-side development. It is built on Chrome's V8 JavaScript engine.
**Example:** `node server.js`
**Reference:** [Node.js Official Documentation](https://nodejs.org/en/about/)

### 2. How is Node.js different from client-side JavaScript?
**Answer:** Client-side JS runs in the browser and interacts with the DOM. Node.js runs on the server and provides APIs for file system access, network requests, and database interactions, but lacks DOM and window objects.
**Example:** `document.getElementById()` works in browser, `fs.readFile()` works in Node.js.
**Reference:** [MDN - Server-side website programming](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction)

### 3. What is NPM?
**Answer:** NPM (Node Package Manager) is the default package manager for the Node.js JavaScript runtime environment. It consists of a command line client and an online database of public and private packages.
**Example:** `npm install express`
**Reference:** [NPM Documentation](https://docs.npmjs.com/about-npm)

### 4. What is the `package.json` file?
**Answer:** The `package.json` file is a manifest for the project. It holds metadata relevant to the project, such as dependencies, scripts, versions, and project descriptions.
**Example:** `{ "name": "my-app", "version": "1.0.0", "dependencies": { "express": "^4.17.1" } }`
**Reference:** [NPM - Creating a package.json file](https://docs.npmjs.com/creating-a-package-json-file)

### 5. How do you import a module in Node.js?
**Answer:** Traditionally, Node.js uses CommonJS modules with the `require()` function. In newer versions, it also supports ES modules using `import`.
**Example:** `const fs = require('fs');` or `import fs from 'fs';`
**Reference:** [Node.js - Modules: CommonJS](https://nodejs.org/api/modules.html)

### 6. What is the `fs` module?
**Answer:** The `fs` (File System) module provides an API for interacting with the file system in a manner closely modeled around standard POSIX functions.
**Example:** `const fs = require('fs'); fs.writeFileSync('test.txt', 'Hello');`
**Reference:** [Node.js - File System](https://nodejs.org/api/fs.html)

### 7. What is an Event Emitter?
**Answer:** The `EventEmitter` is a class in the `events` module that facilitates communication between objects in Node.js. Objects emit named events that cause previously registered listeners to be called.
**Example:** `const EventEmitter = require('events'); const myEmitter = new EventEmitter(); myEmitter.on('event', () => console.log('Fired!')); myEmitter.emit('event');`
**Reference:** [Node.js - Events](https://nodejs.org/api/events.html)

### 8. Explain how to create a basic web server in Node.js.
**Answer:** You can create a web server using the built-in `http` module.
**Example:** `const http = require('http'); const server = http.createServer((req, res) => { res.end('Hello'); }); server.listen(3000);`
**Reference:** [Node.js - HTTP](https://nodejs.org/api/http.html)


## Medium (30%)

### 9. What is Express.js?
**Answer:** Express.js is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications, specifically routing and middleware.
**Example:** `const express = require('express'); const app = express(); app.get('/', (req, res) => res.send('Hello'));`
**Reference:** [Express.js Official Site](https://expressjs.com/)

### 10. What is Middleware in Express.js?
**Answer:** Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the next middleware function in the application's request-response cycle. They can execute code, make changes, and end the request cycle.
**Example:** `app.use((req, res, next) => { console.log('Time:', Date.now()); next(); });`
**Reference:** [Express - Writing middleware](https://expressjs.com/en/guide/writing-middleware.html)

### 11. Explain the difference between synchronous and asynchronous functions in Node.js.
**Answer:** Synchronous functions block the execution thread until they finish (e.g., `readFileSync`). Asynchronous functions do not block the thread; they initiate an operation and use a callback, promise, or event to signal completion (e.g., `readFile`).
**Example:** `const data = fs.readFileSync('/file.md');` (Sync) vs `fs.readFile('/file.md', (err, data) => {});` (Async)
**Reference:** [Node.js - Overview of Blocking vs Non-Blocking](https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/)

### 12. What are Node.js Streams?
**Answer:** Streams are collections of data—just like arrays or strings. The difference is that streams might not be available all at once, and they don't have to fit in memory. This makes streams powerful when working with large amounts of data.
**Example:** `const readStream = fs.createReadStream('large_file.txt'); readStream.pipe(process.stdout);`
**Reference:** [Node.js - Stream](https://nodejs.org/api/stream.html)

### 13. What is the difference between `process.nextTick()` and `setImmediate()`?
**Answer:** `process.nextTick()` schedules a callback to execute *immediately* after the current operation completes, before the Event Loop continues to the next phase. `setImmediate()` schedules a callback to execute in the "check" phase of the Event Loop, after I/O events.
**Example:** `process.nextTick(() => console.log('nextTick')); setImmediate(() => console.log('setImmediate'));`
**Reference:** [Node.js - Event Loop, Timers, and nextTick](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

### 14. What is REPL in Node.js?
**Answer:** REPL stands for Read Eval Print Loop. It represents a computer environment like a Windows console or Unix/Linux shell where a command is entered and the system responds with an output. Node.js comes with a built-in REPL.
**Example:** Type `node` in the terminal to enter the REPL, then type `1 + 1`.
**Reference:** [Node.js - REPL](https://nodejs.org/api/repl.html)

### 15. How do you handle exceptions in Node.js?
**Answer:** Exceptions can be handled using `try...catch` blocks for synchronous code and `async/await`. For callback-based async code, errors are typically passed as the first argument to the callback (Error-First Callback pattern).
**Example:** `fs.readFile('file', (err, data) => { if (err) return console.error(err); });`
**Reference:** [Node.js - Error Handling](https://nodejs.org/api/errors.html)

### 16. What is CORS and how do you enable it in Node.js?
**Answer:** Cross-Origin Resource Sharing (CORS) is a mechanism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served. It is typically enabled using the `cors` middleware package in Express.
**Example:** `const cors = require('cors'); app.use(cors());`
**Reference:** [MDN - CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

### 17. What are the global objects in Node.js?
**Answer:** Global objects are available in all modules without needing to require them. Examples include `process`, `console`, `__dirname`, `__filename`, `setTimeout`, and `Buffer`.
**Example:** `console.log(__dirname);`
**Reference:** [Node.js - Global Objects](https://nodejs.org/api/globals.html)


## Hard (50%)

### 18. How does the Node.js Event Loop work?
**Answer:** The event loop allows Node.js to perform non-blocking I/O operations despite being single-threaded by offloading operations to the system kernel whenever possible. It executes in phases: timers, pending callbacks, idle/prepare, poll, check, and close callbacks.
**Example:** It checks `setTimeout` first, then I/O callbacks, then `setImmediate`.
**Reference:** [Node.js - Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

### 19. What is `libuv`?
**Answer:** `libuv` is a multi-platform C library that provides support for asynchronous I/O based on event loops. Node.js uses `libuv` to handle non-blocking I/O operations, the thread pool, and the event loop.
**Example:** When Node.js makes a DNS query or file system operation, `libuv` delegates it to the OS or its internal thread pool.
**Reference:** [libuv Documentation](https://libuv.org/)

### 20. What is Clustering in Node.js?
**Answer:** Node.js runs in a single thread. Clustering allows you to create child processes (workers) that run simultaneously and share the same server port to take advantage of multi-core systems and handle more load.
**Example:** `const cluster = require('cluster'); if (cluster.isMaster) { cluster.fork(); } else { app.listen(8000); }`
**Reference:** [Node.js - Cluster](https://nodejs.org/api/cluster.html)

### 21. What are Worker Threads?
**Answer:** While clustering forks an entire Node process, Worker Threads (`worker_threads` module) allow you to run multiple JavaScript execution threads in parallel within the *same* process, sharing memory using `SharedArrayBuffer`.
**Example:** `const { Worker } = require('worker_threads'); const worker = new Worker('./worker.js');`
**Reference:** [Node.js - Worker Threads](https://nodejs.org/api/worker_threads.html)

### 22. What is a Memory Leak in Node.js and how do you find one?
**Answer:** A memory leak occurs when an application retains memory that is no longer needed, preventing garbage collection. This usually happens due to global variables, unclosed closures, or lingering event listeners. You find them using tools like Chrome DevTools (heap snapshots) or Node.js inspect.
**Example:** `node --inspect index.js`
**Reference:** [Node.js - Memory Diagnostics](https://nodejs.org/en/docs/guides/diagnostics/memory/)

### 23. Explain the architecture of Node.js.
**Answer:** Node.js consists of a V8 engine (compiles JS to machine code), `libuv` (handles async I/O and the event loop), and core APIs (written in JS and C++). It operates on a single-threaded, event-driven, non-blocking I/O model.
**Example:** V8 parses JS -> Libuv executes I/O -> Event loop queues callbacks.
**Reference:** [Node.js Dependencies](https://nodejs.org/en/docs/meta/topics/dependencies/)

### 24. How do you scale a Node.js application?
**Answer:** 1. **Clustering** (Vertical scaling on multi-core). 2. **Load Balancing** (Horizontal scaling across multiple machines using NGINX or HAProxy). 3. **Microservices** (Decomposing app into smaller, independent services). 4. **Caching** (Using Redis).
**Example:** Running Node behind an NGINX reverse proxy.
**Reference:** [Node.js - Clustering and Load Balancing](https://nodejs.org/en/knowledge/getting-started/how-to-scale-node-js-applications/)

### 25. What is the difference between Buffer and Stream?
**Answer:** A `Buffer` is a temporary memory area used to store raw binary data entirely in memory before it is processed. A `Stream` processes data continuously in chunks without keeping the whole payload in memory. Streams often use Buffers internally.
**Example:** `Buffer.from('hello')`
**Reference:** [Node.js - Buffer](https://nodejs.org/api/buffer.html)

### 26. How do you implement authentication in a Node.js/Express app?
**Answer:** Authentication is typically implemented using JSON Web Tokens (JWT) for stateless authentication or session-based authentication using tools like `express-session` and `Passport.js`.
**Example:** `const token = jwt.sign({ id: user.id }, 'secret');`
**Reference:** [Passport.js Documentation](https://www.passportjs.org/)

### 27. Explain Event-Driven Programming in Node.js.
**Answer:** Event-Driven Programming is a paradigm where the flow of the program is determined by events such as user actions, sensor outputs, or messages from other programs. Node.js relies heavily on this, executing callback functions when specific events are triggered.
**Example:** `server.on('request', (req, res) => { ... });`
**Reference:** [Node.js - Events](https://nodejs.org/api/events.html)
