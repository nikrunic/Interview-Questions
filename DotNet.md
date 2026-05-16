# .NET Interview Questions

This document contains a comprehensive list of .NET framework and .NET Core interview questions.

## Basic (10 Questions)

### 1. What is the .NET Framework / .NET Core?
**Answer:** 
**The Core Concept:**
.NET is a free, cross-platform, open-source developer platform created by Microsoft for building many different types of applications.

**Key Details:**
- Originally Windows-only (.NET Framework), it evolved into the modern, cross-platform .NET Core (now just called .NET).
- It supports multiple languages (C#, F#, VB.NET).
**Example:** Building ASP.NET web APIs or MAUI mobile apps.
**Reference:** [What is .NET?](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet)

### 2. What is the CLR (Common Language Runtime)?
**Answer:** 
**The Core Concept:**
The CLR is the virtual machine component of .NET that manages the execution of .NET programs.

**Key Details:**
- It provides services such as memory management (Garbage Collection), type safety, exception handling, and thread management.
- It executes Intermediate Language (IL) code via Just-In-Time (JIT) compilation.
**Example:** N/A (Internal architecture).
**Reference:** [CLR Overview](https://learn.microsoft.com/en-us/dotnet/standard/clr)

### 3. What is IL (Intermediate Language) and JIT (Just-In-Time) compilation?
**Answer:** 
**The Core Concept:**
IL is a CPU-independent instruction set. JIT compiles this IL into native machine code.

**Key Details:**
- When you compile C#, it turns into IL (stored in a .dll).
- When you run the app, the CLR's JIT compiler turns that IL into specific machine code optimized for the host architecture on the fly.
**Example:** `csc.exe` produces IL; the CLR runs the JIT.
**Reference:** [Managed Code](https://learn.microsoft.com/en-us/dotnet/standard/managed-code)

### 4. What is the BCL (Base Class Library)?
**Answer:** 
**The Core Concept:**
The BCL is a foundational set of assemblies that provide common functionality for all .NET applications.

**Key Details:**
- It includes classes for collections, IO operations, thread management, database access, and more.
**Example:** The `System` namespace containing `String`, `Int32`, `Console`.
**Reference:** [BCL](https://learn.microsoft.com/en-us/dotnet/standard/class-library)

### 5. What is the difference between .NET Framework, .NET Core, and .NET Standard?
**Answer:** 
**The Core Concept:**
They represent the evolution of the .NET ecosystem.

**Key Details:**
- **.NET Framework:** Older, Windows-only platform.
- **.NET Core (now .NET 5+):** Modern, cross-platform, highly performant open-source platform.
- **.NET Standard:** A specification of APIs that all .NET implementations must support, used for creating portable class libraries.
**Example:** Targeting `netstandard2.0` to share code between old Framework apps and new Core apps.
**Reference:** [.NET Standard](https://learn.microsoft.com/en-us/dotnet/standard/net-standard)

### 6. What is NuGet?
**Answer:** 
**The Core Concept:**
NuGet is the package manager for .NET.

**Key Details:**
- It allows developers to create, share, and consume useful libraries and tools within the .NET ecosystem, resolving dependencies automatically.
**Example:** Running `dotnet add package Newtonsoft.Json`.
**Reference:** [NuGet](https://learn.microsoft.com/en-us/nuget/what-is-nuget)

### 7. What is ASP.NET Core?
**Answer:** 
**The Core Concept:**
ASP.NET Core is the cross-platform, high-performance, open-source framework for building modern, cloud-enabled web applications.

**Key Details:**
- It features a unified story for building web UI and web APIs, built-in dependency injection, and a lightweight modular HTTP request pipeline.
**Example:** Creating a REST API using `ControllerBase`.
**Reference:** [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/)

### 8. Explain the `Program.cs` and `Startup.cs` files in ASP.NET Core.
**Answer:** 
**The Core Concept:**
They are the entry points of an application.

**Key Details:**
- In older .NET Core, `Program.cs` builds the web host, and `Startup.cs` configures services (DI) and the HTTP request pipeline (Middleware).
- In modern .NET (6+), these are unified into a single `Program.cs` using top-level statements.
**Example:** `var builder = WebApplication.CreateBuilder(args);`
**Reference:** [App Startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup)

### 9. What is Middleware in ASP.NET Core?
**Answer:** 
**The Core Concept:**
Middleware is software assembled into an app pipeline to handle requests and responses.

**Key Details:**
- Each component chooses whether to pass the request to the next component in the pipeline and can perform work before and after the next component.
**Example:** Authentication middleware, Routing middleware, Error Handling middleware.
**Reference:** [Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/)

### 10. What is Entity Framework Core (EF Core)?
**Answer:** 
**The Core Concept:**
EF Core is a lightweight, extensible, open-source Object-Relational Mapper (O/RM) for .NET.

**Key Details:**
- It enables developers to work with a database using .NET objects, eliminating the need for most of the data-access code that typically needs to be written.
**Example:** `context.Users.Add(newUser); context.SaveChanges();`
**Reference:** [EF Core](https://learn.microsoft.com/en-us/ef/core/)

## Medium (10 Questions)

### 11. Explain Dependency Injection lifetimes in .NET (Transient, Scoped, Singleton).
**Answer:** 
**The Core Concept:**
DI manages object lifespans in the built-in container.

**Key Details:**
- **Transient:** A new instance is created every time it is requested.
- **Scoped:** A new instance is created once per HTTP request.
- **Singleton:** A single instance is created and shared throughout the entire lifetime of the application.
**Example:** `builder.Services.AddScoped<IMyService, MyService>();`
**Reference:** [DI Lifetimes](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection#service-lifetimes)

### 12. What is Kestrel?
**Answer:** 
**The Core Concept:**
Kestrel is the cross-platform, default web server included by default in ASP.NET Core project templates.

**Key Details:**
- It is highly optimized and incredibly fast. It can be used alone as an edge server or placed behind a reverse proxy server (like IIS, Nginx, or Apache).
**Example:** Kestrel listening on `http://localhost:5000`.
**Reference:** [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel)

### 13. How does routing work in ASP.NET Core?
**Answer:** 
**The Core Concept:**
Routing is responsible for matching incoming HTTP requests and dispatching those requests to the app's executable endpoints (like Controllers).

**Key Details:**
- It supports Conventional routing (used mainly in MVC) and Attribute routing (used mainly in REST APIs).
**Example:** `[Route("api/[controller]")]`
**Reference:** [Routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing)

### 14. What are Action Filters in ASP.NET Core?
**Answer:** 
**The Core Concept:**
Filters allow code to run before or after specific stages in the request processing pipeline.

**Key Details:**
- Action filters specifically run immediately before and after an action method is executed. Useful for validation, caching, or logging.
**Example:** `[Authorize]`, `[ValidateModelState]`
**Reference:** [Filters](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/filters)

### 15. What is the `appsettings.json` file?
**Answer:** 
**The Core Concept:**
It is the standard configuration file in ASP.NET Core, storing application settings in JSON format.

**Key Details:**
- It replaces the old `web.config`. Settings can be strongly typed using the Options pattern (`IOptions<T>`) and overridden by environment variables.
**Example:** Storing Database Connection Strings.
**Reference:** [Configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/)

### 16. What is the difference between `AddMvc()`, `AddControllers()`, and `AddControllersWithViews()`?
**Answer:** 
**The Core Concept:**
They configure the necessary services for different architectural needs to optimize memory usage.

**Key Details:**
- `AddMvc()`: Adds everything (Views, Razor Pages, API features).
- `AddControllers()`: Adds only API features (no Views), minimizing overhead for REST APIs.
- `AddControllersWithViews()`: Adds API features and support for MVC Views.
**Example:** Use `AddControllers()` for a pure backend API.
**Reference:** [MVC Services](https://learn.microsoft.com/en-us/aspnet/core/mvc/overview)

### 17. How does JWT Authentication work in .NET Core?
**Answer:** 
**The Core Concept:**
JSON Web Tokens provide a stateless authentication mechanism.

**Key Details:**
- The server validates credentials and issues a signed JWT. The client sends this token in the `Authorization` header (`Bearer <token>`). The .NET middleware validates the signature to authorize the request without querying a database.
**Example:** `services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)`
**Reference:** [JWT in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/jwt-authn)

### 18. What is Code-First vs Database-First in EF Core?
**Answer:** 
**The Core Concept:**
Two approaches to mapping databases to objects.

**Key Details:**
- **Code-First:** You write C# classes (Entities), and EF generates the database schema via Migrations.
- **Database-First:** The database exists, and you run a scaffolding command to generate the C# classes from the database schema.
**Example:** `dotnet ef migrations add InitialCreate` (Code-First)
**Reference:** [EF Core Approaches](https://learn.microsoft.com/en-us/ef/core/managing-schemas/)

### 19. What are EF Core Migrations?
**Answer:** 
**The Core Concept:**
Migrations are a way to keep the database schema in sync with the EF Core model while preserving existing data.

**Key Details:**
- As you change your C# models, you generate migration files (up/down methods) that represent the SQL changes needed to update the DB.
**Example:** `Update-Database` in Package Manager Console.
**Reference:** [Migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/)

### 20. What is Blazor?
**Answer:** 
**The Core Concept:**
Blazor is a framework for building interactive client-side web UI with .NET/C# instead of JavaScript.

**Key Details:**
- It runs either on a server (Blazor Server via WebSockets/SignalR) or directly in the browser using WebAssembly (Blazor WebAssembly).
**Example:** Writing an `<input @onclick="HandleClick" />` component.
**Reference:** [Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/)

## Hard (10 Questions)

### 21. How do you implement asynchronous streams in .NET?
**Answer:** 
**The Core Concept:**
Using `IAsyncEnumerable<T>` introduced in C# 8, allowing you to consume a stream of data asynchronously.

**Key Details:**
- It is heavily used for streaming data from databases or APIs without holding everything in memory. It is iterated using `await foreach`.
**Example:** `await foreach (var item in GetDataAsync()) { ... }`
**Reference:** [Async Streams](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/generate-consume-asynchronous-stream)

### 22. Explain the Garbage Collection Large Object Heap (LOH).
**Answer:** 
**The Core Concept:**
The GC segregates objects by size. Objects larger than ~85,000 bytes go to the LOH.

**Key Details:**
- Because moving large memory blocks is expensive, the LOH is rarely compacted during GC collections. This can lead to memory fragmentation and `OutOfMemoryException`.
- Modern .NET allows manual compaction of the LOH.
**Example:** Large byte arrays or large strings.
**Reference:** [Large Object Heap](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/large-object-heap)

### 23. What is the Options pattern in ASP.NET Core?
**Answer:** 
**The Core Concept:**
It uses classes to provide strongly typed access to groups of related settings from `appsettings.json`.

**Key Details:**
- It promotes encapsulation and separation of concerns. It uses `IOptions<T>` (singleton), `IOptionsSnapshot<T>` (scoped, reloads on change), or `IOptionsMonitor<T>` (singleton, dynamic reloads).
**Example:** `public MyService(IOptions<MySettings> options)`
**Reference:** [Options Pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options)

### 24. How do you prevent thread starvation in ASP.NET Core?
**Answer:** 
**The Core Concept:**
Thread starvation occurs when the ThreadPool is exhausted, causing the app to freeze.

**Key Details:**
- Prevent it by strictly using `async/await` completely top-to-bottom ("async all the way down").
- Never use `.Result` or `.Wait()` on a Task within synchronous code, as this blocks a thread while waiting for an asynchronous operation.
**Example:** Avoid `var data = GetDataAsync().Result;`
**Reference:** [Async Guidance](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md)

### 25. Explain minimal APIs introduced in .NET 6.
**Answer:** 
**The Core Concept:**
Minimal APIs are designed to create HTTP APIs with minimal dependencies and boilerplate.

**Key Details:**
- They remove the need for Controllers, allowing you to define endpoints directly in `Program.cs` using simple lambdas. Highly performant for microservices.
**Example:** `app.MapGet("/hello", () => "Hello World!");`
**Reference:** [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)

### 26. What is the N+1 query problem in EF Core and how do you solve it?
**Answer:** 
**The Core Concept:**
It occurs when EF Core executes one query to get a list of parents, and then N additional queries to load the children of each parent lazily.

**Key Details:**
- This crushes database performance.
- Solve it using Eager Loading (`.Include()`) so EF translates the request into a single SQL `JOIN` query.
**Example:** `context.Authors.Include(a => a.Books).ToList();`
**Reference:** [Loading Related Data](https://learn.microsoft.com/en-us/ef/core/querying/related-data)

### 27. How does SignalR work under the hood?
**Answer:** 
**The Core Concept:**
SignalR simplifies adding real-time web functionality to apps.

**Key Details:**
- It automatically handles connection management. It attempts to use WebSockets for real-time bidirectional communication. If WebSockets aren't available, it gracefully falls back to Server-Sent Events or Long Polling seamlessly.
**Example:** Real-time chat applications or live dashboards.
**Reference:** [SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction)

### 28. What is AOT (Ahead-Of-Time) Compilation in modern .NET?
**Answer:** 
**The Core Concept:**
Native AOT compiles the .NET code directly into native machine code at build time, bypassing the CLR's JIT compiler.

**Key Details:**
- It drastically reduces startup time (cold starts) and memory usage, ideal for AWS Lambdas/Azure Functions or microservices. The tradeoff is it restricts dynamic capabilities like Reflection.
**Example:** Setting `<PublishAot>true</PublishAot>` in the `.csproj`.
**Reference:** [Native AOT](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/)

### 29. How do you implement global exception handling in ASP.NET Core?
**Answer:** 
**The Core Concept:**
Catching unhandled exceptions globally to prevent server crashes and return standard HTTP error responses.

**Key Details:**
- In older versions, using custom Exception Handling Middleware.
- In modern .NET (8+), using the `IExceptionHandler` interface and registering it with `UseExceptionHandler()`.
**Example:** `app.UseExceptionHandler("/error");`
**Reference:** [Error Handling](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling)

### 30. Explain concurrency control in EF Core.
**Answer:** 
**The Core Concept:**
Preventing data loss when multiple users attempt to update the same row simultaneously.

**Key Details:**
- EF Core supports Optimistic Concurrency. You configure a concurrency token (usually a `RowVersion` column). If User A and User B read the same row, and User A saves, User B's save will throw a `DbUpdateConcurrencyException` because the token in the DB no longer matches their local token.
**Example:** `[Timestamp] public byte[] RowVersion { get; set; }`
**Reference:** [Concurrency](https://learn.microsoft.com/en-us/ef/core/saving/concurrency)
