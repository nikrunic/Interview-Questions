# Node.js Interview Questions

This document contains a comprehensive list of 100 Node.js interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories.

## Basic Questions

### 1. What is Node.js?
**Answer:** An open-source, cross-platform, back-end JavaScript runtime environment built on Chrome's V8 engine that executes JS code outside a web browser.
**Example:** `node app.js`
**Reference:** [Node.js About](https://nodejs.org/en/about/)

---

---

### 2. Is Node.js single-threaded or multi-threaded?
**Answer:** Node.js operates on a single-threaded event loop, but it uses multiple threads under the hood via the libuv library for asynchronous I/O tasks.
**Example:** The Event Loop.
**Reference:** [Event Loop Timers and NextTick](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

---

---

### 3. What is NPM?
**Answer:** 
**The Core Concept:**
Node Package Manager.

**Key Details:**
- It is both a CLI tool for installing packages and an online repository of open-source JS projects.
**Example:** `npm install express`
**Reference:** [NPM Docs](https://docs.npmjs.com/)

---

---

### 4. What is the `package.json` file?
**Answer:** A manifest file for Node.js projects that includes metadata, dependencies, scripts, and versioning info.
**Example:** `{ "name": "app", "version": "1.0.0" }`
**Reference:** [package.json](https://docs.npmjs.com/cli/v9/configuring-npm/package-json)

---

---

### 5. What are modules in Node.js?
**Answer:** 
**The Core Concept:**
Reusable blocks of code.

**Key Details:**
- Node supports CommonJS (`require()`) and ES Modules (`import()`).
**Example:** `const fs = require('fs');`
**Reference:** [Node Modules](https://nodejs.org/api/modules.html)

---

---

### 6. What is the difference between `require()` and `import()`?
**Answer:** 
**The Core Concept:**
`require` is synchronous and part of CommonJS.

**Key Details:**
- `import` is asynchronous, statically analyzed, and part of the ES6 standard.
**Example:** `require('http')` vs `import http from 'http'`.
**Reference:** [ES Modules](https://nodejs.org/api/esm.html)

---

---

### 7. What is an Event Emitter?
**Answer:** A core module in Node.js that allows you to create, listen to, and emit custom events.
**Example:** `const ee = new EventEmitter(); ee.on('event', () => {}); ee.emit('event');`
**Reference:** [Events](https://nodejs.org/api/events.html)

---

---

### 8. What is REPL?
**Answer:** 
**The Core Concept:**
Read, Eval, Print, Loop.

**Key Details:**
- It's a virtual environment like a console/terminal where you can run Node.js code instantly.
**Example:** Typing `node` in the terminal starts the REPL.
**Reference:** [REPL](https://nodejs.org/api/repl.html)

---

---

### 9. What is a callback function in Node.js?
**Answer:** A function passed as an argument to another asynchronous function to be executed when the asynchronous operation completes.
**Example:** `fs.readFile('file.txt', (err, data) => { ... });`
**Reference:** [Callback Functions](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)

---

---

### 10. What is Callback Hell?
**Answer:** Heavily nested callbacks that make the code difficult to read and maintain (also known as the Pyramid of Doom).
**Example:** `a(b(c(d())))` nested logic.
**Reference:** [Callback Hell](http://callbackhell.com/)

---

---

### 11. How do you prevent Callback Hell?
**Answer:** By using Promises, `async/await`, or modularizing code into smaller named functions.
**Example:** `await fs.promises.readFile('file.txt');`
**Reference:** [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)

---

---

### 12. What is the `fs` module?
**Answer:** The File System module provides an API for interacting with the file system (reading/writing files).
**Example:** `const fs = require('fs'); fs.writeFileSync('test.txt', 'Hello');`
**Reference:** [File System](https://nodejs.org/api/fs.html)

---

---

### 13. What is the `http` module?
**Answer:** A core module that allows Node.js to transfer data over the Hyper Text Transfer Protocol (HTTP), allowing you to create a web server.
**Example:** `http.createServer((req, res) => { ... });`
**Reference:** [HTTP](https://nodejs.org/api/http.html)

---

---

### 14. What is `global` in Node.js?
**Answer:** 
**The Core Concept:**
An object that provides variables and functions available everywhere.

**Key Details:**
- It is the Node.js equivalent of the `window` object in browsers.
**Example:** `global.setTimeout`, `global.console`.
**Reference:** [Globals](https://nodejs.org/api/globals.html)

---

---

### 15. What are `__dirname` and `__filename`?
**Answer:** 
**The Core Concept:**
`__dirname` is the absolute path to the directory of the current module.

**Key Details:**
- `__filename` is the absolute path to the current module file itself.
**Example:** `console.log(__dirname);`
**Reference:** [Modules Globals](https://nodejs.org/api/modules.html#modules_dirname)

---

---

### 16. What is `process.env`?
**Answer:** 
**The Core Concept:**
An object containing the user environment variables.

**Key Details:**
- Often used to store sensitive configuration like API keys or ports.
**Example:** `const port = process.env.PORT || 3000;`
**Reference:** [process.env](https://nodejs.org/api/process.html#process_process_env)

---

---

### 17. How do you exit a Node.js process?
**Answer:** 
**The Core Concept:**
By calling `process.exit(code)`.

**Key Details:**
- 0 means success, any non-zero number means failure.
**Example:** `process.exit(1);`
**Reference:** [process.exit](https://nodejs.org/api/process.html#process_process_exit_code)

---

---

### 18. What is Express.js?
**Answer:** A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.
**Example:** `const app = express(); app.get('/', (req, res) => res.send('Hi'));`
**Reference:** [Express API](https://expressjs.com/)

---

---

### 19. What is Middleware in Express.js?
**Answer:** Functions that have access to the request object, response object, and the `next` function in the application's request-response cycle.
**Example:** `app.use((req, res, next) => { console.log('Logged'); next(); });`
**Reference:** [Express Middleware](https://expressjs.com/en/guide/using-middleware.html)

---

---

### 20. What is `package-lock.json`?
**Answer:** 
**The Core Concept:**
A file that is automatically generated when `package.json` changes.

**Key Details:**
- It locks the versions of installed dependencies to ensure consistent installs across machines.
**Example:** Always commit `package-lock.json` to source control.
**Reference:** [package-lock.json](https://docs.npmjs.com/cli/v9/configuring-npm/package-lock-json)

---


## Intermediate Questions

---

## Intermediate Questions

### 21. How does the Event Loop work in Node.js?
**Answer:** The Event Loop is what allows Node.js to perform non-blocking I/O operations despite being single-threaded, by offloading operations to the system kernel (libuv) whenever possible.
**Example:** Timers phase -> Pending Callbacks -> Idle/Prepare -> Poll -> Check -> Close Callbacks.
**Reference:** [Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

---

---

### 22. What is `setImmediate()` vs `setTimeout()`?
**Answer:** 
**The Core Concept:**
`setTimeout(cb, 0)` schedules execution after a minimum delay.

**Key Details:**
- `setImmediate(cb)` schedules execution to occur on the *Check* phase of the event loop, immediately after the Poll phase.
**Example:** Inside an I/O cycle, `setImmediate` always fires before `setTimeout`.
**Reference:** [setImmediate vs setTimeout](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#setimmediate-vs-settimeout)

---

---

### 23. What is `process.nextTick()`?
**Answer:** It schedules a callback to be invoked in the same phase of the event loop, immediately after the current operation completes, before moving to the next phase of the event loop.
**Example:** `process.nextTick(() => console.log('first'));`
**Reference:** [process.nextTick](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#process-nexttick)

---

---

### 24. What are Streams in Node.js?
**Answer:** Objects that let you read data from a source or write data to a destination in a continuous fashion (chunks), reducing memory usage for large files.
**Example:** `fs.createReadStream('huge.mp4')`
**Reference:** [Streams](https://nodejs.org/api/stream.html)

---

---

### 25. What are the types of Streams?
**Answer:** Readable (read data), Writable (write data), Duplex (both read/write), Transform (duplex that modifies data as it's written/read).
**Example:** `zlib.createGzip()` is a Transform stream.
**Reference:** [Stream Types](https://nodejs.org/api/stream.html#stream_types_of_streams)

---

---

### 26. What is piping in Node.js?
**Answer:** A mechanism to connect the output of a readable stream directly to the input of a writable stream.
**Example:** `readStream.pipe(writeStream);`
**Reference:** [stream.pipe](https://nodejs.org/api/stream.html#stream_readable_pipe_destination_options)

---

---

### 27. What is a Buffer in Node.js?
**Answer:** A temporary memory spot used to store raw binary data outside the V8 engine, particularly useful when reading from streams or interacting with TCP streams.
**Example:** `const buf = Buffer.from('Hello');`
**Reference:** [Buffer](https://nodejs.org/api/buffer.html)

---

---

### 28. How does Node.js handle child processes?
**Answer:** The `child_process` module provides the ability to spawn new processes to utilize multiple cores or run external OS commands.
**Example:** `const { exec } = require('child_process'); exec('ls', (err, out) => ...);`
**Reference:** [Child Process](https://nodejs.org/api/child_process.html)

---

---

### 29. What is the difference between `spawn()` and `exec()`?
**Answer:** 
**The Core Concept:**
`exec` buffers the command's output entirely into memory and returns it at the end.

**Key Details:**
- `spawn` streams the output as it happens, making it better for large data returns.
**Example:** Use `spawn` for long-running scripts, `exec` for quick bash commands.
**Reference:** [spawn vs exec](https://nodejs.org/api/child_process.html)

---

---

### 30. What is the `cluster` module?
**Answer:** A core module that allows you to easily create child processes (workers) that share the same server ports, enabling load balancing across multiple CPU cores.
**Example:** `if (cluster.isPrimary) { cluster.fork(); }`
**Reference:** [Cluster](https://nodejs.org/api/cluster.html)

---

---

### 31. Explain CORS.
**Answer:** 
**The Core Concept:**
Cross-Origin Resource Sharing.

**Key Details:**
- A mechanism that uses HTTP headers to tell browsers to give a web application running at one origin access to selected resources from a different origin.
**Example:** `app.use(cors())` in Express.
**Reference:** [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

---

### 32. How do you handle routing in Express.js?
**Answer:** 
**The Core Concept:**
By using the `app.get()`, `app.post()`, etc.

**Key Details:**
- methods, or by using the `express.Router` class to create modular, mountable route handlers.
**Example:** `const router = express.Router(); router.get('/', ...); app.use('/users', router);`
**Reference:** [Express Routing](https://expressjs.com/en/guide/routing.html)

---

---

### 33. What is the purpose of `module.exports`?
**Answer:** 
**The Core Concept:**
It is the object that is actually returned as the result of a `require` call.

**Key Details:**
- It allows you to expose functions, objects, or values from a module.
**Example:** `module.exports = { myFunction };`
**Reference:** [Modules](https://nodejs.org/api/modules.html)

---

---

### 34. Explain JSON Web Tokens (JWT).
**Answer:** An open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object, heavily used for stateless authentication.
**Example:** `jwt.sign({ userId: 123 }, 'secret');`
**Reference:** [JWT](https://jwt.io/introduction)

---

---

### 35. How do you hash passwords in Node.js?
**Answer:** 
**The Core Concept:**
Do not store plain text.

**Key Details:**
- Use a library like `bcrypt` or `argon2` to hash and salt the passwords before saving them to the database.
**Example:** `bcrypt.hash(password, 10);`
**Reference:** [Bcrypt on NPM](https://www.npmjs.com/package/bcrypt)

---

---

### 36. What is the `path` module?
**Answer:** A core module providing utilities for working with file and directory paths across different operating systems cleanly.
**Example:** `path.join(__dirname, 'public', 'index.html');`
**Reference:** [Path](https://nodejs.org/api/path.html)

---

---

### 37. What is PM2?
**Answer:** 
**The Core Concept:**
A production process manager for Node.js applications with a built-in load balancer.

**Key Details:**
- It keeps applications alive forever, reloads them without downtime, and manages logs.
**Example:** `pm2 start app.js`
**Reference:** [PM2](https://pm2.keymetrics.io/)

---

---

### 38. What are environmental variables in Node.js?
**Answer:** 
**The Core Concept:**
Key-value pairs stored in the OS environment, accessible via `process.env`.

**Key Details:**
- The `dotenv` package is commonly used to load them from a `.env` file during development.
**Example:** `require('dotenv').config();`
**Reference:** [Dotenv](https://www.npmjs.com/package/dotenv)

---

---

### 39. What is a RESTful API?
**Answer:** 
**The Core Concept:**
Representational State Transfer.

**Key Details:**
- An architectural style for designing networked applications using standard HTTP methods (GET, POST, PUT, DELETE) and stateless communication.
**Example:** `GET /users`, `POST /users`.
**Reference:** [REST APIs](https://restfulapi.net/)

---

---

### 40. How do you handle errors in Express asynchronous routes?
**Answer:** By passing the error to the `next()` function, or by using a wrapper library like `express-async-errors` to automatically catch rejected promises.
**Example:** `try { ... } catch (err) { next(err); }`
**Reference:** [Express Error Handling](https://expressjs.com/en/guide/error-handling.html)

---


## Expert Questions

---

### 41. Explain Libuv in detail.
**Answer:** 
**The Core Concept:**
A multi-platform C library that provides support for asynchronous I/O based on event loops.

**Key Details:**
- It handles the Thread Pool (for file system/DNS operations) and the Event Loop architecture for Node.js.
**Example:** fs operations use libuv's thread pool.
**Reference:** [Libuv Design](http://docs.libuv.org/en/v1.x/design.html)

---

---

### 42. How does Node.js resolve modules?
**Answer:** 
**The Core Concept:**
1.

**Key Details:**
- Core modules.
- 2.
- File modules (relative/absolute paths).
- 3.
- `node_modules` (traverses up the directory tree looking for `node_modules`).
**Example:** `require('express')` checks `node_modules`.
**Reference:** [Module Resolution](https://nodejs.org/api/modules.html#modules_all_together)

---

---

### 43. Explain the architecture of the V8 Engine.
**Answer:** 
**The Core Concept:**
Google's open-source high-performance JS and WebAssembly engine, written in C++.

**Key Details:**
- It compiles JS directly to native machine code before executing it, using JIT (Just-In-Time) compilation (Ignition interpreter and TurboFan compiler).
**Example:** V8 powers Chrome and Node.js.
**Reference:** [V8 Docs](https://v8.dev/)

---

---

### 44. What are Worker Threads?
**Answer:** 
**The Core Concept:**
A module (`worker_threads`) that allows you to use threads to execute JS in parallel.

**Key Details:**
- Useful for CPU-intensive JavaScript operations, solving the single-threaded CPU bottleneck.
**Example:** `const { Worker } = require('worker_threads');`
**Reference:** [Worker Threads](https://nodejs.org/api/worker_threads.html)

---

---

### 45. What is the difference between Cluster and Worker Threads?
**Answer:** 
**The Core Concept:**
Cluster spins up entire new Node.js processes (heavy memory usage) that can share ports.

**Key Details:**
- Worker threads run inside a single process, share memory via `SharedArrayBuffer`, and are lighter, but cannot share server ports directly.
**Example:** Cluster for web servers, Workers for math computations.
**Reference:** [Workers vs Cluster](https://nodejs.org/api/worker_threads.html)

---

---

### 46. What is Memory Leak in Node.js and how do you profile it?
**Answer:** 
**The Core Concept:**
Occurs when objects are no longer needed but are still referenced by the root, preventing garbage collection.

**Key Details:**
- Profiled using tools like Chrome DevTools (via `node --inspect`), heap snapshots, and analyzing memory increases over time.
**Example:** Global variables caching data infinitely.
**Reference:** [Debugging Memory Leaks](https://nodejs.org/en/docs/guides/diagnostics/memory/)

---

---

### 47. Explain Garbage Collection in V8.
**Answer:** 
**The Core Concept:**
V8 uses a generational garbage collector (Scavenger for new space/young generation, Mark-Sweep/Mark-Compact for old space).

**Key Details:**
- It periodically frees memory occupied by objects that are no longer reachable from the root.
**Example:** `--max-old-space-size=4096` alters GC behavior.
**Reference:** [V8 Garbage Collection](https://v8.dev/blog/trash-talk)

---

---

### 48. How do you implement WebSockets in Node.js?
**Answer:** 
**The Core Concept:**
Using libraries like `ws` or `socket.io`.

**Key Details:**
- WebSockets provide full-duplex, persistent communication over a single TCP connection, bypassing the HTTP request/response overhead for real-time apps.
**Example:** `const io = require('socket.io')(server);`
**Reference:** [Socket.io](https://socket.io/)

---

---

### 49. What is Backpressure in Node.js Streams?
**Answer:** 
**The Core Concept:**
When data is being read from a readable stream faster than it can be written to the writable stream, backpressure builds up.

**Key Details:**
- `stream.pipe()` automatically handles this by pausing the readable stream until the writable stream drains.
**Example:** Writing a massive file to a slow network connection.
**Reference:** [Backpressure Guide](https://nodejs.org/en/docs/guides/backpressuring-in-streams/)

---

---

### 50. How does Node.js handle unhandled promise rejections?
**Answer:** 
**The Core Concept:**
In newer versions, it crashes the Node.js process with a non-zero exit code.

**Key Details:**
- You should handle them using `.catch()` or the `process.on('unhandledRejection')` event to log and gracefully shut down.
**Example:** `process.on('unhandledRejection', (reason) => { ... });`
**Reference:** [unhandledRejection](https://nodejs.org/api/process.html#process_event_unhandledrejection)

---

---

## Expert Questions

### 51. What is the Node.js event loop order?
**Answer:** 
**The Core Concept:**
Phases: timers, pending callbacks, idle/prepare, poll, check, close callbacks; process.nextTick and microtasks run between.

**Key Details:**
- Understanding order explains setTimeout vs setImmediate.
- Microtasks (Promises) run before next macrotask.

**Example:** 
`setTimeout 0 vs setImmediate`

**Reference:** [Documentation](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

---

---

### 52. What is process.nextTick?
**Answer:** 
**The Core Concept:**
Queues callback before event loop continues—higher priority than Promise microtasks in Node.

**Key Details:**
- Can starve I/O if used recursively.
- Use for deferring after sync code.

**Example:** 
`process.nextTick(() => {})`

**Reference:** [Documentation](https://nodejs.org/api/process.html#processnexttickcallback-args)

---

---

### 53. What is setImmediate?
**Answer:** 
**The Core Concept:**
Schedules callback in check phase after poll phase I/O.

**Key Details:**
- Differs from setTimeout(0) on timing.
- Use for deferring after I/O.

**Example:** 
`setImmediate(() => console.log('check'))`

**Reference:** [Documentation](https://nodejs.org/api/timers.html#setimmediatecallback-args)

---

---

### 54. What is cluster module?
**Answer:** 
**The Core Concept:**
Spawns worker processes sharing server ports for multi-core utilization.

**Key Details:**
- Master distributes connections.
- PM2 uses similar concepts.

**Example:** 
`cluster.fork()`

**Reference:** [Documentation](https://nodejs.org/api/cluster.html)

---

---

### 55. What is worker_threads?
**Answer:** 
**The Core Concept:**
True parallel threads in Node for CPU-bound work without separate processes.

**Key Details:**
- Share memory via SharedArrayBuffer.
- Not for I/O—use async I/O instead.

**Example:** 
`new Worker('./cpu.js')`

**Reference:** [Documentation](https://nodejs.org/api/worker_threads.html)

---

---

### 56. What is child_process?
**Answer:** 
**The Core Concept:**
Spawns subprocesses (exec, spawn, fork) for shell commands or other Node scripts.

**Key Details:**
- fork() has IPC channel.
- Avoid shell injection—use spawn with args array.

**Example:** 
`spawn('ls', ['-la'])`

**Reference:** [Documentation](https://nodejs.org/api/child_process.html)

---

---

### 57. What is PM2?
**Answer:** 
**The Core Concept:**
Production process manager for Node with clustering, reload, and monitoring.

**Key Details:**
- Zero-downtime reload.
- Logs and startup scripts.

**Example:** 
`pm2 start app.js -i max`

**Reference:** [Documentation](https://pm2.keymetrics.io/)

---

---

### 58. What is Express middleware?
**Answer:** 
**The Core Concept:**
Functions (req, res, next) in pipeline for logging, auth, parsing.

**Key Details:**
- Order matters.
- Error middleware has 4 args.

**Example:** 
`app.use(express.json())`

**Reference:** [Documentation](https://expressjs.com/en/guide/using-middleware.html)

---

---

### 59. What is error-handling middleware?
**Answer:** 
**The Core Concept:**
Express middleware with (err, req, res, next) catching errors from prior middleware/routes.

**Key Details:**
- Call next(err) to forward.
- Centralize error formatting.

**Example:** 
`app.use((err, req, res, next) => ...)`

**Reference:** [Documentation](https://expressjs.com/en/guide/error-handling.html)

---

---

### 60. What is Helmet?
**Answer:** 
**The Core Concept:**
Express middleware setting security HTTP headers.

**Key Details:**
- HSTS, X-Frame-Options, etc.
- Default for production APIs.

**Example:** 
`app.use(helmet())`

**Reference:** [Documentation](https://helmetjs.github.io/)

---

---

### 61. What is express-rate-limit?
**Answer:** 
**The Core Concept:**
Middleware limiting repeated requests per IP/window.

**Key Details:**
- Mitigate brute force.
- Return 429 when exceeded.

**Example:** 
`rateLimit({ windowMs: 60000, max: 100 })`

**Reference:** [Documentation](https://github.com/express-rate-limit/express-rate-limit)

---

---

### 62. What is CORS in Express?
**Answer:** 
**The Core Concept:**
cors package sets Access-Control-Allow-* for browser clients.

**Key Details:**
- Configure allowed origins explicitly.
- Credentials need specific origin not *.

**Example:** 
`cors({ origin: 'https://app.com' })`

**Reference:** [Documentation](https://github.com/expressjs/cors)

---

---

### 63. What is body-parser / express.json?
**Answer:** 
**The Core Concept:**
Parses incoming JSON/urlencoded bodies onto req.body.

**Key Details:**
- Size limits prevent DoS.
- Validate parsed data.

**Example:** 
`express.json({ limit: '1mb' })`

**Reference:** [Documentation](https://expressjs.com/en/api.html#express.json)

---

---

### 64. What is Morgan?
**Answer:** 
**The Core Concept:**
HTTP request logger middleware for Express.

**Key Details:**
- dev vs combined formats.
- Pipe to Winston for production.

**Example:** 
`app.use(morgan('combined'))`

**Reference:** [Documentation](https://github.com/expressjs/morgan)

---

---

### 65. What is Winston logging?
**Answer:** 
**The Core Concept:**
Flexible logging library with transports (file, console, cloud).

**Key Details:**
- Log levels: error, warn, info.
- Structured JSON logs.

**Example:** 
`winston.createLogger({ transports: [...] })`

**Reference:** [Documentation](https://github.com/winstonjs/winston)

---

---

### 66. What is dotenv?
**Answer:** 
**The Core Concept:**
Loads environment variables from .env file into process.env.

**Key Details:**
- Never commit .env secrets.
- Use platform env in production.

**Example:** 
`require('dotenv').config()`

**Reference:** [Documentation](https://github.com/motdotla/dotenv)

---

---

### 67. What is NODE_ENV?
**Answer:** 
**The Core Concept:**
Convention: development, production, test—frameworks optimize based on value.

**Key Details:**
- Enables caching in Express views.
- Set in deployment platform.

**Example:** 
`NODE_ENV=production`

**Reference:** [Documentation](https://nodejs.org/en/learn/getting-started/nodejs-the-difference-between-development-and-production)

---

---

### 68. What is dependency injection in Node?
**Answer:** 
**The Core Concept:**
Passing dependencies (DB, services) into modules/classes for testability.

**Key Details:**
- Avoid global singletons.
- Use factories or DI containers.

**Example:** 
`constructor(db) injection`

**Reference:** [Documentation](https://en.wikipedia.org/wiki/Dependency_injection)

---

---

### 69. What is Sequelize?
**Answer:** 
**The Core Concept:**
ORM for SQL databases in Node with migrations and models.

**Key Details:**
- Supports Postgres, MySQL, SQLite.
- N+1 query risk with includes.

**Example:** 
`User.findAll({ include: Post })`

**Reference:** [Documentation](https://sequelize.org/)

---

---

### 70. What is Prisma?
**Answer:** 
**The Core Concept:**
Next-gen ORM with schema file, type-safe client, and migrations.

**Key Details:**
- Prisma Client generated from schema.
- Popular with TypeScript.

**Example:** 
`prisma.user.findMany()`

**Reference:** [Documentation](https://www.prisma.io/docs)

---

---

### 71. What is Mongoose?
**Answer:** 
**The Core Concept:**
MongoDB ODM with schemas, validation, and middleware.

**Key Details:**
- ObjectId references.
- Indexes defined in schema.

**Example:** 
`new Schema({ name: String })`

**Reference:** [Documentation](https://mongoosejs.com/)

---

---

### 72. What is connection pooling?
**Answer:** 
**The Core Concept:**
Reusing DB connections instead of opening per request.

**Key Details:**
- Configure pool size per workload.
- Release connections on errors.

**Example:** 
`pg Pool max: 20`

**Reference:** [Documentation](https://node-postgres.com/features/pooling)

---

---

### 73. What is Redis with Node?
**Answer:** 
**The Core Concept:**
In-memory store for cache, sessions, pub/sub via ioredis/node-redis.

**Key Details:**
- Set TTL on cache keys.
- Handle connection failures gracefully.

**Example:** 
`redis.setex('key', 3600, val)`

**Reference:** [Documentation](https://redis.io/docs/clients/nodejs/)

---

---

### 74. What is JWT in Express?
**Answer:** 
**The Core Concept:**
jsonwebtoken signs/verifies tokens; middleware checks Authorization header.

**Key Details:**
- Use strong secret or RS256.
- Validate exp and aud.

**Example:** 
`jwt.sign(payload, secret, { expiresIn: '1h' })`

**Reference:** [Documentation](https://github.com/auth0/node-jsonwebtoken)

---

---

### 75. What is Passport.js?
**Answer:** 
**The Core Concept:**
Authentication middleware with strategies (local, OAuth, JWT).

**Key Details:**
- Pluggable strategies.
- Serialize user to session.

**Example:** 
`passport.use(new JwtStrategy(...))`

**Reference:** [Documentation](https://www.passportjs.org/)

---

---

### 76. What is bcrypt in Node?
**Answer:** 
**The Core Concept:**
Password hashing with bcryptjs/bcrypt native addon.

**Key Details:**
- Async hash to avoid blocking.
- Cost factor 10-12 typical.

**Example:** 
`await bcrypt.hash(password, 12)`

**Reference:** [Documentation](https://github.com/kelektiv/node.bcrypt.js)

---

---

### 77. What is input validation with Joi/Zod?
**Answer:** 
**The Core Concept:**
Schema validation for req.body/query before processing.

**Key Details:**
- Return 400 with details.
- Zod infers TypeScript types.

**Example:** 
`schema.parse(req.body)`

**Reference:** [Documentation](https://zod.dev/)

---

---

### 78. What is async error handling in Express 5?
**Answer:** 
**The Core Concept:**
Rejected promises from async route handlers propagate to error middleware automatically.

**Key Details:**
- Express 4 needs wrap or catch.
- Avoid unhandled rejections.

**Example:** 
`app.get('/', async (req, res) => { await db(); })`

**Reference:** [Documentation](https://expressjs.com/en/guide/error-handling.html)

---

---

### 79. What is graceful shutdown in Node?
**Answer:** 
**The Core Concept:**
On SIGTERM close server, drain connections, close DB pools.

**Key Details:**
- Kubernetes sends SIGTERM.
- Set timeout for forced exit.

**Example:** 
`server.close(() => process.exit(0))`

**Reference:** [Documentation](https://nodejs.org/api/process.html#signal-events)

---

---

### 80. What is uncaughtException?
**Answer:** 
**The Core Concept:**
Event when sync error not caught—log and exit; do not rely on continuing.

**Key Details:**
- Fix code instead of running after.
- Use domain patterns sparingly.

**Example:** 
`process.on('uncaughtException', ...)`

**Reference:** [Documentation](https://nodejs.org/api/process.html#event-uncaughtexception)

---

---

### 81. What is REPL?
**Answer:** 
**The Core Concept:**
Read-Eval-Print Loop for interactive Node experimentation.

**Key Details:**
- node without script starts REPL.
- Useful for quick tests.

**Example:** 
`node -> > 1+1`

**Reference:** [Documentation](https://nodejs.org/api/repl.html)

---

---

### 82. What is V8 isolate?
**Answer:** 
**The Core Concept:**
Each Node process runs one V8 isolate; workers have separate isolates.

**Key Details:**
- Memory not shared except SharedArrayBuffer.
- Explains worker isolation.

**Example:** 
`worker_threads separate isolate`

**Reference:** [Documentation](https://v8.dev/docs)

---

---

### 83. What is libuv thread pool size?
**Answer:** 
**The Core Concept:**
Default 4 threads for fs, crypto, dns; set UV_THREADPOOL_SIZE.

**Key Details:**
- CPU-bound crypto blocks pool.
- Do not set excessively high.

**Example:** 
`UV_THREADPOOL_SIZE=128`

**Reference:** [Documentation](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

---

---

### 84. What is dns.lookup vs dns.resolve?
**Answer:** 
**The Core Concept:**
lookup uses OS resolver (sync thread pool); resolve uses DNS servers directly.

**Key Details:**
- Blocking lookup can stall event loop under load.
- Prefer resolve for async.

**Example:** 
`dns.promises.resolve4('nodejs.org')`

**Reference:** [Documentation](https://nodejs.org/api/dns.html)

---

---

### 85. What is stream.pipeline?
**Answer:** 
**The Core Concept:**
Safely pipes streams with error propagation and cleanup.

**Key Details:**
- Preferred over manual pipe.
- Node 10+.

**Example:** 
`pipeline(read, transform, write, cb)`

**Reference:** [Documentation](https://nodejs.org/api/stream.html#streampipelinesource-transforms-destination-callback)

---

---

### 86. What is readable stream modes?
**Answer:** 
**The Core Concept:**
Flowing vs paused—data emits automatically or on read().

**Key Details:**
- pipe() switches to flowing.
- Use pause/resume for control.

**Example:** 
`rs.pause(); rs.on('data')`

**Reference:** [Documentation](https://nodejs.org/api/stream.html#readable-streams)

---

---

### 87. What is writable stream cork/uncork?
**Answer:** 
**The Core Concept:**
Buffers multiple writes then flushes on uncork for efficiency.

**Key Details:**
- Batch small writes.
- Advanced optimization.

**Example:** 
`ws.cork(); ws.write(); ws.uncork()`

**Reference:** [Documentation](https://nodejs.org/api/stream.html#writablecork)

---

---

### 88. What is transform stream?
**Answer:** 
**The Core Concept:**
Duplex stream that modifies data passing through (zlib, crypto).

**Key Details:**
- Implement _transform.
- Used in compression pipelines.

**Example:** 
`zlib.createGzip()`

**Reference:** [Documentation](https://nodejs.org/api/stream.html#class-streamtransform)

---

---

### 89. What is object mode streams?
**Answer:** 
**The Core Concept:**
Streams carrying JavaScript objects instead of Buffers/strings.

**Key Details:**
- objectMode: true option.
- Useful for object pipelines.

**Example:** 
`new Transform({ objectMode: true })`

**Reference:** [Documentation](https://nodejs.org/api/stream.html#object-mode)

---

---

### 90. What is fs.promises?
**Answer:** 
**The Core Concept:**
Promise-based filesystem API avoiding callback hell.

**Key Details:**
- async/await friendly.
- Still uses thread pool for many ops.

**Example:** 
`await fs.promises.readFile('a.txt')`

**Reference:** [Documentation](https://nodejs.org/api/fs.html#promises-api)

---

---

### 91. What is path module?
**Answer:** 
**The Core Concept:**
Cross-platform path joining and resolution without string hacks.

**Key Details:**
- path.join, path.resolve.
- Never hardcode backslashes.

**Example:** 
`path.join(__dirname, 'data', 'file.json')`

**Reference:** [Documentation](https://nodejs.org/api/path.html)

---

---

### 92. What is os module?
**Answer:** 
**The Core Concept:**
System info: CPUs, memory, homedir, platform.

**Key Details:**
- Use for health metrics.
- cpus().length for cluster sizing.

**Example:** 
`os.freemem()`

**Reference:** [Documentation](https://nodejs.org/api/os.html)

---

---

### 93. What is crypto module?
**Answer:** 
**The Core Concept:**
Hashing, HMAC, ciphers, random bytes built-in.

**Key Details:**
- Use crypto.randomBytes for tokens.
- Prefer built-in over deprecated packages.

**Example:** 
`crypto.createHash('sha256')`

**Reference:** [Documentation](https://nodejs.org/api/crypto.html)

---

---

### 94. What is N-API?
**Answer:** 
**The Core Concept:**
Stable C API for native addons across Node versions.

**Key Details:**
- Replace legacy nan.
- Build with node-gyp.

**Example:** 
`napi_create_function`

**Reference:** [Documentation](https://nodejs.org/api/n-api.html)

---

---

### 95. What is Dockerizing Node apps?
**Answer:** 
**The Core Concept:**
Multi-stage builds, non-root user, NODE_ENV=production, .dockerignore node_modules.

**Key Details:**
- Run node dist/main.js.
- Healthcheck endpoint.

**Example:** 
`FROM node:20-alpine`

**Reference:** [Documentation](https://nodejs.org/en/docs/guides/nodejs-docker-webapp)

---

---

### 96. What is Kubernetes probes for Node?
**Answer:** 
**The Core Concept:**
Liveness/readiness HTTP checks on /health.

**Key Details:**
- Readiness waits for DB.
- Liveness restarts stuck pods.

**Example:** 
`readinessProbe httpGet /health`

**Reference:** [Documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

---

---

### 97. What is OpenTelemetry Node?
**Answer:** 
**The Core Concept:**
Distributed tracing and metrics SDK.

**Key Details:**
- Auto-instrument Express.
- Export to Jaeger/Datadog.

**Example:** 
`@opentelemetry/auto-instrumentations-node`

**Reference:** [Documentation](https://opentelemetry.io/docs/languages/js/)

---

---

### 98. What is GraphQL with Node?
**Answer:** 
**The Core Concept:**
Apollo Server or Yoga serves schema with resolvers.

**Key Details:**
- N+1 solved with DataLoader.
- Separate from REST routes.

**Example:** 
`new ApolloServer({ typeDefs, resolvers })`

**Reference:** [Documentation](https://www.apollographql.com/docs/apollo-server/)

---

---

### 99. What is tRPC?
**Answer:** 
**The Core Concept:**
End-to-end typesafe APIs without codegen between TS client/server.

**Key Details:**
- Popular in full-stack TS monorepos.
- Not REST but alternative.

**Example:** 
`appRouter with zod input`

**Reference:** [Documentation](https://trpc.io/)

---

---

### 100. What is Fastify vs Express?
**Answer:** 
**The Core Concept:**
Fastify focuses on performance and schema-based validation.

**Key Details:**
- Lower overhead per request.
- Plugin architecture.

**Example:** 
`fastify.get('/', schema, handler)`

**Reference:** [Documentation](https://fastify.dev/)

---

## Additional Depth (Architectural Focus)

---

### 101. What is Node.js and explain its Event-Driven architecture?
**Answer:** 
**The Core Concept:**
Node.js is an open-source, cross-platform JavaScript runtime built on Chrome's V8 engine. Its Event-Driven architecture means that every action (like database queries, network requests, or file systems) triggers an asynchronous event, processing events sequentially via callbacks.

**Key Details:**
- Decouples processing from thread counts, enabling highly scalable operations without generating separate system threads per request.
- Leverages the V8 engine for execution, compiling JavaScript directly to machine code.
- Relies on event emitters to publish events that are subscribed to by handlers throughout the application.

**Example:** 
```javascript
const EventEmitter = require("events");
const chatRoom = new EventEmitter();

chatRoom.on("message", (msg) => console.log("Received:", msg));
chatRoom.emit("message", "Hello, World!");
```

**Reference:** [Node.js Architecture](https://nodejs.org/en/about/)

---

---

### 102. How does the Event Loop work under the hood?
**Answer:** 
**The Core Concept:**
The Event Loop is the heart of Node.js, coordinating asynchronous, non-blocking I/O. It continuously checks the call stack and, if it is empty, schedules callbacks from queues in a strict cycle of phases.

**Key Details:**
- **Event Loop Phases**:
  1. **Timers**: Executes callbacks scheduled by `setTimeout()` and `setInterval()`.
  2. **Pending Callbacks**: Executes I/O callbacks deferred from previous cycles.
  3. **Idle, Prepare**: Used only internally by the system.
  4. **Poll**: Retrieves new I/O events; executes I/O callbacks.
  5. **Check**: Executes callbacks scheduled by `setImmediate()`.
  6. **Close Callbacks**: Processes socket close events (e.g., `socket.on('close')`).
- **Intermediate Queues**: Between phases, the Microtask Queue (including `process.nextTick()` and Promise callbacks) is fully drained.

**Example:** 
```javascript
setTimeout(() => console.log("Timer"), 0);
setImmediate(() => console.log("Immediate"));
process.nextTick(() => console.log("nextTick"));

// Order: nextTick -> Timer -> Immediate (depending on poll context)
```

**Reference:** [Node.js Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

---

---

### 103. Difference between `dependencies` and `devDependencies`
**Answer:** 
**The Core Concept:**
In `package.json`, `dependencies` are packages required to run the application in a production environment, while `devDependencies` are only used for local development, building, and testing.

**Key Details:**
- **dependencies**: Dynamic libraries, routers, utility wrappers, databases (e.g., `express`, `pg`, `zod`, `dotenv`).
- **devDependencies**: Compilers, linters, testing suites, bundlers, and typings (e.g., `typescript`, `jest`, `eslint`, `@types/node`).
- Production bundles ignore `devDependencies` when installed via `npm install --omit=dev` or `npm ci --only=production`, drastically reducing bundle size and attack surface.

**Example:** 
```json
{
  "dependencies": {
    "express": "^4.19.2"
  },
  "devDependencies": {
    "typescript": "^5.4.5"
  }
}
```

**Reference:** [NPM package.json Spec](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file)

---

---

### 104. Difference between a Buffer and a Stream
**Answer:** 
**The Core Concept:**
A Buffer is a fixed-size chunk of physical raw memory allocated outside the V8 heap. A Stream is a sequential sequence of data chunks transferred over time, allowing processing of data as it arrives without keeping it entirely in memory.

**Key Details:**
- **Buffer**: Best for binary manipulations of small, complete files. It loads the entire dataset into RAM, which causes server crashes when reading multi-gigabyte files.
- **Stream**: Processes data piece-by-piece. Uses standard events (`data`, `end`, `error`) or `.pipe()` to process massive files with steady, low memory footprints.

**Example:** 
```javascript
const fs = require("fs");

// Streams - Memory Efficient
const readStream = fs.createReadStream("massive_movie.mp4");
const writeStream = fs.createWriteStream("copy.mp4");
readStream.pipe(writeStream); // Handles backpressure automatically
```

**Reference:** [Node.js Streams](https://nodejs.org/api/stream.html)

---

---

### 105. What is Clustering and how does the `cluster` module work?
**Answer:** 
**The Core Concept:**
Clustering scales a Node.js API by spinning up multiple instances (workers) of the same process that share the same server port. This allows the application to utilize multi-core CPU architectures.

**Key Details:**
- The primary process spawns worker processes using `child_process.fork()`.
- The primary handles network traffic and distributes incoming TCP connections using a Round-Robin load-balancing algorithm.
- Workers run in separate V8 instances with independent memory heaps, preventing errors in one worker from taking down the entire cluster.

**Example:** 
```javascript
const cluster = require("cluster");
const os = require("os");

if (cluster.isPrimary) {
  const numCPUs = os.cpus().length;
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork(); // Spawn worker
  }
} else {
  // Workers share the same TCP port
  require("./server.js");
}
```

**Reference:** [Node.js Cluster](https://nodejs.org/api/cluster.html)

---

---

### 106. What are Built-in Middlewares in Express?
**Answer:** 
**The Core Concept:**
Built-in middlewares are functions packaged natively inside the Express framework to parse requests, parse cookies, or serve static assets, removing the need for legacy third-party dependencies (like body-parser).

**Key Details:**
- **`express.json()`**: Parses incoming requests containing JSON payloads.
- **`express.urlencoded()`**: Parses URL-encoded payloads (e.g., standard HTML forms).
- **`express.static()`**: Serves static files directly from a directory (e.g., images, compiled client assets).

**Example:** 
```javascript
const express = require("express");
const app = express();

app.use(express.json()); // Built-in parsing middleware
app.use(express.static("public")); // Built-in file serving middleware
```

**Reference:** [Express Built-in Middleware](https://expressjs.com/en/guide/using-middleware.html#middleware.built-in)

---

---

### 107. What is the MVC (Model-View-Controller) pattern?
**Answer:** 
**The Core Concept:**
MVC is an architectural software design pattern that divides an application into three interconnected components, separating data representation, user interfaces, and control flow logic.

**Key Details:**
- **Model**: Represents database schemas, validation logic, and business entities (data tier).
- **View**: The layout structure rendered to the user (HTML, template engines, or API JSON representation).
- **Controller**: Processes incoming HTTP requests, coordinates with Models, and selects which Views/JSON payloads to output.

**Example:** 
```
  [HTTP Request] ---> [Controller] <---> [Model] (DB Access)
                           |
                           v
                   [View / JSON Response]
```

**Reference:** [MDN MVC Architecture](https://developer.mozilla.org/en-US/docs/Glossary/MVC)

---

---

### 108. What is Redis and how is it used in caching?
**Answer:** 
**The Core Concept:**
Redis is a high-performance, in-memory, key-value database. It is widely used in Node.js as a caching tier to store frequently accessed data in RAM, reducing heavy query load on slower primary databases (like SQL or MongoDB).

**Key Details:**
- Operates in-memory to deliver sub-millisecond response latencies.
- **TTL (Time-To-Live)**: Keys are configured to auto-expire after a set duration, ensuring cached data does not remain indefinitely stale.
- **Cache-Aside Pattern**: Check Redis first. If a cache miss occurs, query the primary database, save the result in Redis, and return.

**Example:** 
```javascript
const Redis = require("ioredis");
const redis = new Redis();

async function getCachedUser(id) {
  const cacheKey = `user:${id}`;
  const cached = await redis.get(cacheKey);
  if (cached) return JSON.parse(cached); // Cache Hit

  const user = await db.users.findById(id); // Cache Miss
  await redis.setex(cacheKey, 3600, JSON.stringify(user)); // Cache for 1 hour
  return user;
}
```

**Reference:** [Redis Docs](https://redis.io/docs/clients/nodejs/)

---

---

### 109. What is the difference between `process.nextTick()` and `setImmediate()`?
**Answer:** 
**The Core Concept:**
`process.nextTick()` runs immediately after the current operation finishes, bypassing any Event Loop phases. `setImmediate()` executes during the *Check* phase of the Event Loop, immediately after the Poll phase.

**Key Details:**
- **`process.nextTick()`**: Technically not part of the event loop. Invocations drain the microtask queue, meaning recursive `nextTick` calls will completely block the event loop and freeze I/O.
- **`setImmediate()`**: Yields execution to the event loop, ensuring I/O events, timers, and other phases remain unblocked.

**Example:** 
```javascript
setImmediate(() => console.log("Immediate"));
process.nextTick(() => console.log("nextTick"));

// Output:
// nextTick (runs instantly before the event loop advances)
// Immediate (runs during the Check phase)
```

**Reference:** [Event Loop setImmediate vs nextTick](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#processnexttick-vs-setimmediate)

---

---

### 110. What are the best practices for security in a Node.js API?
**Answer:** 
**The Core Concept:**
Security in Node.js requires a defense-in-depth approach covering request parsing, dependency auditing, header configuration, and secure execution runtime rules.

**Key Details:**
- **Helmet**: Set HTTP security headers (HSTS, CSP, X-Frame-Options) to mitigate common browser vectors.
- **Rate Limiting**: Limit API request volume per IP window to prevent DDoS and brute-force attacks.
- **Data Sanitization**: Never trust client inputs; use tools like Zod to strictly validate payloads and prevent SQL/NoSQL Injection.
- **Dependency Audit**: Run `npm audit` frequently to check for vulnerabilities in third-party scripts.
- **Environment Rules**: Avoid running Node as the root user in Docker containers, and store sensitive secrets securely in environmental variables.

**Example:** 
```javascript
const express = require("express");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const app = express();

app.use(helmet()); // Set secure HTTP headers
app.use(rateLimit({ windowMs: 15 * 60 * 1000, max: 100 })); // Rate limiting
```

**Reference:** [Node.js Security Best Practices](https://nodejs.org/en/docs/guides/security-best-practices/)

---

## Technical Questions

---

### 1. Build a basic HTTP server with the native `http` module that parses query parameters.

**Example Solution:**
```javascript
const http = require("http");
const url = require("url");

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ query: parsedUrl.query }));
});
server.listen(3000);
```

---

### 2. Write an Express middleware that logs request execution times to the console.

**Example Solution:**
```javascript
const express = require("express");
const app = express();

app.use((req, res, next) => {
  const start = process.hrtime();
  res.on("finish", () => {
    const diff = process.hrtime(start);
    const ms = diff[0] * 1e3 + diff[1] * 1e-6;
    console.log(`${req.method} ${req.url} - ${ms.toFixed(3)}ms`);
  });
  next();
});
```

---

## Technical Questions

### 1. Build a basic HTTP server with the native `http` module that parses query parameters.

**Example Solution:**
```javascript
const http = require("http");
const url = require("url");

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ query: parsedUrl.query }));
});
server.listen(3000);
```

### 2. Write an Express middleware that logs request execution times to the console.

**Example Solution:**
```javascript
const express = require("express");
const app = express();

app.use((req, res, next) => {
  const start = process.hrtime();
  res.on("finish", () => {
    const diff = process.hrtime(start);
    const ms = diff[0] * 1e3 + diff[1] * 1e-6;
    console.log(`\${req.method} \${req.url} - \${ms.toFixed(3)}ms`);
  });
  next();
});
```

### 3. Write a Node.js clustering script using `cluster` module for multi-process scaling.

**Example Solution:**
```javascript
const cluster = require("cluster");
const http = require("http");
const numCPUs = require("os").cpus().length;

if (cluster.isMaster) {
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  cluster.on("exit", (worker) => {
    cluster.fork(); // Revive crashed worker
  });
} else {
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end("Hello World");
  }).listen(8000);
}
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Node.js & Express Applications application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Node.js & Express Applications operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Node.js & Express Applications configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Node.js & Express Applications event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Node.js & Express Applications with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Node.js & Express Applications performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Node.js & Express Applications failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Node.js & Express Applications data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Node.js & Express Applications state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Node.js & Express Applications logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Node.js & Express Applications files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Node.js & Express Applications connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Node.js & Express Applications.

*(Challenge question for self-study and practical project implementation.)*

