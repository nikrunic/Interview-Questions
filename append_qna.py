import os
import re

qna_data = {
    "Accessibility.md": ("How do you handle focus management in Single Page Applications (SPAs)?",
        "In SPAs, client-side routing does not trigger a full page reload, meaning screen readers are not inherently alerted to page changes. Focus management involves programmatically shifting the browser's focus to the new content or a relevant heading so that assistive technologies can read the updated context.",
        ["You should manage focus using JavaScript's `.focus()` method on a `tabindex=\"-1\"` element after a route change.", "Avoid trapping focus within a component unless it is a modal dialogue, ensuring keyboard navigation remains intuitive."],
        "useEffect(() => { headingRef.current?.focus(); }, [pathname]);",
        "https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/"),

    "AgenticAI.md": ("What is the ReAct (Reasoning and Acting) prompting framework?",
        "ReAct is a paradigm that interleaves reasoning traces with action generation in Large Language Models. It enables the agent to dynamically plan, execute tools, and adjust its plan based on the observations received from the environment.",
        ["By forcing the model to articulate its thought process ('Thought: ...') before taking an action ('Action: ...'), it reduces hallucinations and improves problem-solving accuracy.", "The primary tradeoff is increased token consumption and latency due to the verbose reasoning steps."],
        "Thought: I need to find the user's IP. Action: tool_get_ip. Observation: 192.168.1.1",
        "https://arxiv.org/abs/2210.03629"),

    "Agile.md": ("What is the difference between Story Points and hours when estimating work?",
        "Story points represent a relative measure of complexity, effort, and risk, rather than an absolute time duration like hours. This abstraction helps teams account for varying skill levels, as a complex task takes the same 'points' regardless of whether a senior or junior developer executes it.",
        ["Story pointing often uses the Fibonacci sequence (1, 2, 3, 5, 8, 13) to reflect the inherent uncertainty in larger tasks.", "It prevents stakeholders from equating estimates directly to rigid deadlines, fostering a focus on velocity and continuous improvement."],
        "A simple UI text change is a 1; migrating a database table with downtime risk is an 8.",
        "https://www.atlassian.com/agile/project-management/estimation"),

    "Angular.md": ("How does Angular's Change Detection mechanism work under the hood?",
        "Angular uses a library called Zone.js to monkey-patch asynchronous operations (like setTimeout, Promises, and DOM events). Whenever an asynchronous event completes, Zone.js notifies Angular, which then runs change detection from the root component down through the component tree.",
        ["The default change detection strategy checks every component in the tree, which can be computationally expensive for large applications.", "Using `ChangeDetectionStrategy.OnPush` optimizes this by only checking a component when its `@Input()` references change or an event originates from within it."],
        "@Component({ changeDetection: ChangeDetectionStrategy.OnPush })",
        "https://angular.io/guide/change-detection"),

    "Authentication.md": ("What are the security implications of storing JWTs in localStorage versus HttpOnly cookies?",
        "Storing JWTs in localStorage makes them accessible via JavaScript, leaving the application vulnerable to Cross-Site Scripting (XSS) attacks where malicious scripts can steal the token. HttpOnly cookies prevent JavaScript access, mitigating XSS risks but introducing Cross-Site Request Forgery (CSRF) vulnerabilities.",
        ["To secure HttpOnly cookies against CSRF, you must implement Anti-CSRF tokens or use the `SameSite=Strict` cookie attribute.", "localStorage is often used for convenience in SPAs, but requires rigorous sanitization of all user inputs to prevent XSS."],
        "Set-Cookie: token=jwt_here; HttpOnly; Secure; SameSite=Strict",
        "https://owasp.org/www-community/vulnerabilities/Cross-Site_Request_Forgery"),

    "BrowserCompatibility.md": ("How does Babel facilitate cross-browser compatibility?",
        "Babel is a JavaScript compiler that transforms modern ECMAScript 2015+ syntax into backwards-compatible JavaScript code that older rendering engines can understand. It acts as a transpiler, ensuring developers can use modern language features without alienating users on legacy browsers.",
        ["Babel uses plugins to transform specific syntax (like arrow functions or optional chaining) and presets (like `@babel/preset-env`) to manage collections of plugins based on target browser environments.", "It works in tandem with polyfills (like core-js) to replicate missing global objects and instance methods, as transpilation alone only fixes syntax."],
        "// Babel transforms `const x = () => {}` to `var x = function() {}`",
        "https://babeljs.io/docs/en/"),

    "Webpack.md": ("What is Tree Shaking and how does Webpack implement it?",
        "Tree shaking is a dead-code elimination technique used to optimize the final JavaScript bundle size. It relies on the static structure of ES2015 module syntax (import and export) to determine which exports are actually used in the application.",
        ["Webpack marks unused exports during the build process, and a minifier (like Terser) physically removes the dead code from the output.", "For tree shaking to work efficiently, you must ensure that your codebase uses ES modules and that Babel is not compiling them down to CommonJS before Webpack analyzes them."],
        "In package.json: `\"sideEffects\": false` tells Webpack the package has no side effects and is safe to tree-shake.",
        "https://webpack.js.org/guides/tree-shaking/"),

    "Cypress.md": ("How do you intercept and mock network requests in Cypress?",
        "Cypress provides the `cy.intercept()` command to route, modify, and stub network requests at the browser network layer. This allows you to simulate various backend states (like 500 errors or specific JSON payloads) without relying on a live server environment.",
        ["Unlike traditional mocking that replaces the `fetch` or `XHR` objects in the window, `cy.intercept()` works at the network level, capturing all requests regardless of how they are initiated.", "You can alias intercepts using `.as('name')` and use `cy.wait('@name')` to ensure the application has completed the network call before asserting on the UI."],
        "cy.intercept('GET', '/api/users', { fixture: 'users.json' }).as('getUsers');",
        "https://docs.cypress.io/api/commands/intercept"),

    "CSharp.md": ("What is the difference between `IEnumerable<T>` and `IQueryable<T>`?",
        "`IEnumerable<T>` is best suited for querying data in-memory, whereas `IQueryable<T>` is designed for querying data out-of-memory, such as from a SQL database. While both facilitate LINQ queries, they compile and execute those queries differently.",
        ["`IEnumerable<T>` loads all records into application memory and then filters them using delegates, which can cause severe performance bottlenecks on large datasets.", "`IQueryable<T>` builds an expression tree that is translated into a domain-specific query (like a SQL `WHERE` clause) by the provider (e.g., Entity Framework), executing the filter on the database server."],
        "Use `IQueryable` for EF Core `DbSet` queries; use `IEnumerable` for local Lists.",
        "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/"),

    "CICD.md": ("What is a deployment strategy and how does Blue-Green deployment work?",
        "A deployment strategy defines how a new version of an application is rolled out to users to minimize downtime and risk. In a Blue-Green deployment, two identical production environments (Blue and Green) are maintained, but only one serves live traffic at a time.",
        ["The new version is deployed to the idle environment (e.g., Green) and tested thoroughly. Once validated, the router or load balancer immediately switches all traffic from Blue to Green.", "This approach allows for near-zero downtime and provides an instant rollback mechanism by simply switching the router back to the original environment if issues occur."],
        "AWS Route53 weighted routing changing from 100% Blue to 100% Green.",
        "https://aws.amazon.com/quickstart/architecture/blue-green-deployment/"),

    "CloudPlatforms.md": ("What is the principle of least privilege in IAM?",
        "The principle of least privilege dictates that a user, application, or service should only be granted the minimum permissions necessary to perform its intended function. It is a foundational security concept in cloud environments like AWS (IAM) and GCP (Cloud IAM).",
        ["By restricting access, the blast radius of a compromised credential or a misconfigured application is severely limited.", "Implementing this requires using fine-grained access control policies, avoiding wildcard permissions (`*`), and regularly auditing roles using tools like AWS IAM Access Analyzer."],
        "Allow `s3:GetObject` on `arn:aws:s3:::my-bucket/*` instead of `s3:*` on all resources.",
        "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"),

    "Core-javascript.md": ("How does the JavaScript Event Loop handle microtasks vs macrotasks?",
        "The Event Loop coordinates the execution of synchronous code, microtasks (Promises, `queueMicrotask`), and macrotasks (setTimeout, setInterval). It prioritizes the microtask queue, entirely emptying it before processing the next macrotask.",
        ["When the call stack is empty, the engine processes all pending microtasks. If a microtask queues another microtask, it will also execute in the same cycle.", "This means an infinite loop of microtasks can block the main thread and prevent the browser from rendering or handling macrotasks."],
        "Promise.resolve().then(() => console.log('Microtask')); setTimeout(() => console.log('Macrotask'), 0);",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop"),

    "CSS3.md": ("What is the Stacking Context in CSS and how is it formed?",
        "A stacking context is a three-dimensional conceptualization of HTML elements along an imaginary z-axis relative to the user. Elements within a stacking context are rendered in order based on their `z-index`, but they cannot interleave with elements in a different stacking context.",
        ["An element forms a new stacking context if it has an `opacity` less than 1, a `transform` or `filter` property other than none, or a `position` of absolute/relative with a `z-index` other than auto.", "Understanding stacking contexts resolves issues where an element with a `z-index` of 999 is inexplicably hidden behind an element with a `z-index` of 1, because the former is trapped inside a lower-level stacking context parent."],
        ".parent { position: relative; z-index: 1; } /* Traps children */",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context"),

    "DotNet.md": ("What are Minimal APIs in .NET?",
        "Minimal APIs were introduced in .NET 6 to create HTTP APIs with significantly less boilerplate code than traditional MVC controllers. They allow developers to configure routes and endpoints directly in the `Program.cs` file using concise lambda expressions.",
        ["They use the same underlying ASP.NET Core primitives (routing, model binding, dependency injection) but eliminate the need for class-based controllers and attributes.", "They are highly optimized for microservices and cloud-native applications, offering lower memory allocation and faster startup times."],
        "app.MapGet(\"/hello\", () => \"Hello World!\");",
        "https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis"),

    "Git.md": ("What is a Git rebase and how does it differ from merge?",
        "Git rebase integrates changes from one branch into another by moving or combining a sequence of commits to a new base commit. Unlike `git merge`, which creates a new merge commit and preserves the exact history of both branches, rebasing rewrites the project history to create a perfectly linear timeline.",
        ["Rebasing results in a cleaner, more readable commit history, but it alters commit hashes. Therefore, you should never rebase commits that have already been pushed to a public, shared repository.", "Interactive rebasing (`-i`) is a powerful tool to squash, edit, or reorder commits before merging a feature branch."],
        "git rebase main",
        "https://git-scm.com/book/en/v2/Git-Branching-Rebasing"),

    "Hasura-GraphQL.md": ("How does Hasura resolve GraphQL queries to Postgres databases efficiently?",
        "Hasura acts as a GraphQL-to-SQL compiler rather than a traditional GraphQL server with resolver functions. When it receives a GraphQL query, it compiles the entire query (including nested relations) into a single, optimized SQL query.",
        ["This architecture completely eliminates the infamous N+1 query problem, where traditional GraphQL resolvers make multiple round-trips to the database for nested fields.", "Hasura utilizes Postgres JSON aggregation functions (like `json_agg`) to format the SQL result exactly to the shape of the requested GraphQL response, minimizing application-level processing."],
        "A complex GraphQL query becomes `SELECT json_build_object(...) FROM ...`",
        "https://hasura.io/docs/latest/graphql/core/index/"),

    "HTML.md": ("What is the significance of semantic HTML5 elements like `<article>` and `<section>`?",
        "Semantic HTML introduces meaning to the web page structure rather than just defining its presentation. Tags like `<article>`, `<section>`, `<nav>`, and `<aside>` clearly describe their contents to both the browser and the developer.",
        ["Semantic markup drastically improves Accessibility (a11y) because screen readers use these tags to effectively navigate and outline the document for visually impaired users.", "It also improves Search Engine Optimization (SEO) as crawlers can accurately parse and weight the importance of the content based on its enclosing tag."],
        "<article> <h2>Blog Title</h2> <p>Content</p> </article>",
        "https://developer.mozilla.org/en-US/docs/Glossary/Semantics"),

    "Javascript.md": ("What is a Closure in JavaScript?",
        "A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In simpler terms, a closure gives a function access to its outer scope variables even after the outer function has returned.",
        ["Closures are created every time a function is created, at function creation time. They are commonly used for data privacy (emulating private methods) and in functional programming patterns like currying.", "Improper use of closures, especially capturing large objects or DOM elements in long-lived event listeners, can lead to severe memory leaks."],
        "function makeCounter() { let count = 0; return () => count++; }",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures"),

    "Jest.md": ("How does Jest's module mocking (`jest.mock()`) work?",
        "Jest intercepts the `require` or `import` calls during the test execution phase. When you call `jest.mock('module-name')`, Jest replaces the actual module with an auto-generated mock object, allowing you to control its behavior and track its usage.",
        ["Because ES6 imports are hoisted to the top of the file by Babel, Jest uses a babel-plugin to ensure `jest.mock()` calls are hoisted above all `import` statements.", "You can provide a factory function to `jest.mock()` to define exactly how the mocked module should behave, which is critical for isolating the unit under test from external dependencies like database clients."],
        "jest.mock('axios'); axios.get.mockResolvedValue({ data: {} });",
        "https://jestjs.io/docs/mock-functions"),

    "LESS.md": ("What are Mixins in LESS and how do they differ from normal CSS classes?",
        "Mixins in LESS allow you to embed all the properties of a class into another class by simply including the class name as one of its properties. They act like functions in traditional programming, enabling extensive code reuse.",
        ["Unlike a standard CSS class which is applied directly to HTML elements, a mixin can accept arguments, allowing you to pass variables (like colors or sizes) to dynamically generate CSS rules.", "Mixins without arguments are output into the compiled CSS by default, but appending parentheses to the mixin definition prevents it from being output, acting purely as a utility function."],
        ".border-radius(@radius: 5px) { border-radius: @radius; } .box { .border-radius(10px); }",
        "https://lesscss.org/features/#mixins-feature"),

    "MSSQL.md": ("What is the difference between a Clustered and Non-Clustered Index?",
        "A Clustered Index determines the physical order of data rows in a table, meaning a table can only have one clustered index. A Non-Clustered Index is a separate structure from the data rows, containing the index key values and pointers to the actual data rows.",
        ["Because the clustered index defines the physical storage, retrieving data via a clustered index is inherently faster as it avoids a secondary lookup.", "Non-Clustered indexes are ideal for queries that search on columns not included in the clustered index, but they incur a performance penalty (a 'Key Lookup') when retrieving non-indexed columns."],
        "CREATE CLUSTERED INDEX IX_EmpId ON Employees(EmpId);",
        "https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described"),

    "MySQL.md": ("How does the InnoDB storage engine handle transaction isolation?",
        "InnoDB uses Multi-Version Concurrency Control (MVCC) to provide high concurrency and strict transaction isolation. Instead of placing locks on every read, InnoDB presents each transaction with a snapshot of the database at the time the transaction started.",
        ["This allows readers and writers to access the same tables simultaneously without blocking each other, dramatically improving performance in read-heavy workloads.", "The default isolation level in InnoDB is REPEATABLE READ, which ensures that subsequent reads within the same transaction return the same data, preventing non-repeatable reads."],
        "SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;",
        "https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html"),

    "Nextjs.md": ("What are React Server Components (RSC) in the Next.js App Router?",
        "React Server Components allow you to write UI that is rendered and optionally cached exclusively on the server. They are the default component type in the Next.js 13+ App Router.",
        ["RSCs significantly reduce the client-side JavaScript bundle size because their code is never shipped to the browser; only the resulting HTML/React-tree is sent.", "Unlike traditional Client Components, RSCs cannot use state (`useState`), effects (`useEffect`), or browser APIs, but they can securely access backend resources like databases and secret API keys directly."],
        "export default async function Page() { const data = await db.query(); return <div>{data}</div>; }",
        "https://nextjs.org/docs/app/building-your-application/rendering/server-components"),

    "NodeJs.md": ("What is the role of libuv in Node.js architecture?",
        "libuv is a multi-platform C library that provides support for asynchronous I/O based on event loops. It abstracts the underlying operating system's asynchronous interfaces (like epoll on Linux or IOCP on Windows) and provides a unified API to Node.js.",
        ["It implements the Node.js Event Loop and maintains a thread pool (default size of 4) to handle heavy, blocking tasks that cannot be executed asynchronously by the OS, such as file system operations and crypto functions.", "When V8 encounters an asynchronous operation, it delegates it to libuv, which notifies the event loop via callbacks once the operation completes."],
        "The environment variable `UV_THREADPOOL_SIZE` can be used to increase the thread pool size.",
        "https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/"),

    "ReactArchiteture.md": ("What is the Flux Architecture pattern?",
        "Flux is a strict unidirectional data flow architecture devised by Meta (Facebook) for building client-side web applications. It eschews the complex two-way data binding of MVC frameworks in favor of a predictable, circular flow of data.",
        ["The flow goes: Action -> Dispatcher -> Store -> View. Views trigger Actions, which are broadcasted by a centralized Dispatcher to all Stores, which then update their state and emit a change event, prompting Views to re-render.", "Redux is the most famous implementation of Flux concepts, though it simplifies the architecture by condensing multiple stores into a single global state tree and dropping the Dispatcher entirely."],
        "View clicks button -> Action dispatched -> Store updates -> View renders.",
        "https://facebook.github.io/flux/"),

    "Reactjs.md": ("How does React 18's Automatic Batching improve performance?",
        "Batching is when React groups multiple state updates into a single re-render for better performance. Before React 18, React only batched updates inside synchronous React event handlers (like onClick).",
        ["In React 18, automatic batching applies to state updates triggered inside Promises, `setTimeout`, native event handlers, or any other asynchronous code.", "This prevents intermediate, unnecessary 'half-rendered' states on the screen. If you explicitly need an update to render immediately before the next line of code, you must wrap it in `ReactDOM.flushSync()`."],
        "setTimeout(() => { setCount(1); setFlag(true); }, 1000); // Only 1 render in React 18",
        "https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching"),

    "Redux.md": ("What are Redux Thunks and why are they needed?",
        "Redux Thunk is a middleware that allows you to write action creators that return a function instead of an action object. This function receives the store's `dispatch` and `getState` methods as arguments.",
        ["Because pure Redux reducers must be synchronous and devoid of side effects, Thunks provide a centralized place to handle asynchronous logic, such as making API calls, before dispatching the final success or failure actions.", "While Redux Saga uses generator functions for complex async flows, Thunks are simpler and represent the standard approach for basic async data fetching in Redux applications."],
        "const fetchUser = () => async (dispatch) => { const res = await api(); dispatch({ type: 'SUCCESS', payload: res }); }",
        "https://redux.js.org/usage/writing-logic-thunks"),

    "ResponsiveDesign.md": ("What is the CSS `clamp()` function and how does it aid fluid typography?",
        "The `clamp()` CSS function takes three comma-separated expressions: a minimum value, a preferred value, and a maximum allowed value. It restricts a CSS property to a range between the defined minimum and maximum bounds.",
        ["It is extremely powerful for responsive design, particularly fluid typography, as it allows font sizes to scale smoothly with the viewport width (using `vw`) without shrinking too small on mobile or growing excessively large on ultrawide monitors.", "It eliminates the need for numerous media queries just to adjust font sizes at discrete breakpoints."],
        "font-size: clamp(1rem, 2.5vw, 2rem);",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/clamp"),

    "RestAPI.md": ("What is the difference between PUT and PATCH HTTP methods?",
        "Both methods are used to update existing resources, but they define different update semantics. `PUT` is used for complete replacement of a resource, while `PATCH` is used for partial modifications.",
        ["When using `PUT`, the client must send the entire representation of the resource. If fields are omitted, the server should theoretically set them to null. `PUT` must be idempotent.", "`PATCH` requires sending only the fields that need to be updated. While commonly used, `PATCH` is not strictly required to be idempotent, though well-designed APIs usually implement it as such."],
        "PUT /users/1 {name: 'John', age: 30}. PATCH /users/1 {age: 31}.",
        "https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH"),

    "SCSS.md": ("How does SCSS `@extend` differ from `@include` (Mixins)?",
        "`@extend` lets you share a set of CSS properties from one selector to another without duplicating the CSS rules in the compiled output. `@include` injects the entire contents of a Mixin directly into the current selector.",
        ["`@extend` groups selectors together in the compiled CSS (e.g., `.error, .fatal-error { color: red; }`), which keeps the CSS file size small but can create complex, hard-to-track dependency graphs and specificity issues.", "Mixins (`@include`) duplicate the rules in the compiled CSS, increasing file size but providing better encapsulation and allowing you to pass dynamic arguments."],
        ".btn-primary { @extend .btn; background: blue; }",
        "https://sass-lang.com/documentation/at-rules/extend"),

    "TailwindCSS.md": ("What is the JIT (Just-In-Time) compiler in Tailwind CSS?",
        "The JIT compiler generates your CSS on-demand as you author your templates, rather than generating a massive CSS file containing all possible utility combinations upfront and purging the unused ones later.",
        ["Introduced as default in Tailwind v3, JIT enables instantaneous build times in development and unlocks the ability to use arbitrary values in utility classes (e.g., `top-[117px]`).", "It also ensures that the development CSS perfectly matches the production CSS, eliminating discrepancies caused by the older PurgeCSS pipeline."],
        "Using arbitrary values: `<div class=\"bg-[#1da1f2] p-[1.5rem]\">`",
        "https://tailwindcss.com/blog/just-in-time-the-next-generation-of-tailwind-css"),

    "Typscript.md": ("What are Generics in TypeScript and what problem do they solve?",
        "Generics provide a way to create reusable components that can work over a variety of types rather than a single type. They act as a variable for types, allowing the type to be determined by the caller at execution time.",
        ["Without generics, developers would have to use the `any` type to support multiple data types, which completely defeats the purpose of type checking and destroys IDE autocompletion.", "Generics are widely used in robust functional APIs, such as `Array<T>`, Promises, and React component props, to maintain strict type safety across dynamic operations."],
        "function identity<T>(arg: T): T { return arg; }",
        "https://www.typescriptlang.org/docs/handbook/2/generics.html"),

    "Vuejs.md": ("What is the Composition API and how does it compare to the Options API?",
        "The Composition API is a set of additive, function-based APIs introduced in Vue 3 that allow flexible composition of component logic. It is fundamentally an alternative to the traditional, object-based Options API.",
        ["The Options API forces code organization by lifecycle hook or property type (data, methods, computed), which fragments features across a component and makes complex files difficult to read.", "The Composition API (using `setup()`) allows developers to group code logically by feature, making it highly readable and allowing for easy extraction of reusable logic into external composable functions."],
        "import { ref, computed } from 'vue';",
        "https://vuejs.org/guide/extras/composition-api-faq.html"),

    "WebPerformance.md": ("What is the critical rendering path and how do you optimize it?",
        "The critical rendering path is the sequence of steps the browser goes through to convert HTML, CSS, and JavaScript into pixels on the screen. Optimizing it is crucial for achieving a fast First Contentful Paint (FCP).",
        ["The browser must parse HTML to build the DOM, parse CSS to build the CSSOM, combine them into the Render Tree, calculate layout, and finally paint.", "To optimize it, you must minimize or defer render-blocking resources. This includes loading non-critical CSS asynchronously, deferring JavaScript execution using the `defer` or `async` attributes, and preloading critical web fonts."],
        "<script src=\"app.js\" defer></script>",
        "https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path")
}

def append_to_file():
    for filename, data in qna_data.items():
        if not os.path.exists(filename):
            print(f"Skipping {filename} - not found.")
            continue
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find highest question number
        matches = re.findall(r'### (\d+)\.', content)
        if matches:
            next_num = max(int(m) for m in matches) + 1
        else:
            next_num = 1
            
        title, concept, details, example, reference = data
        new_qna = f'''
### {next_num}. {title}
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
        with open(filename, 'a', encoding='utf-8') as f:
            f.write('\\n## Additional Depth (Architectural Focus)\\n' + new_qna)
            
        print(f"Added Q{next_num} to {filename}")

if __name__ == "__main__":
    append_to_file()
