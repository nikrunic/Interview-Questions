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


### 31. What is the difference between `IApplicationBuilder.Use` and `IApplicationBuilder.Run`?
**Answer:** 
**The Core Concept:**
They define how middleware operates in the request pipeline.

**Key Details:**
- `Run` is a terminal middleware. It processes the request and *never* calls the `next` delegate. The pipeline ends there.
- `Use` allows you to process the request and optionally call `await next()` to pass the request to the next middleware in the pipeline.
**Example:** `app.Use(async (context, next) => { ... await next(); });`
**Reference:** [Middleware pipeline](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/)

### 32. What is `appsettings.Development.json`?
**Answer:** 
**The Core Concept:**
Environment-specific configuration file.

**Key Details:**
- ASP.NET Core natively supports Multiple Environments (Development, Staging, Production). The host automatically merges `appsettings.json` with `appsettings.{Environment}.json`, allowing you to override database strings or API keys based on the server environment.
**Example:** Setting `ASPNETCORE_ENVIRONMENT=Development`.
**Reference:** [Multiple environments](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments)

### 33. How does Dependency Injection handle `IDisposable` objects?
**Answer:** 
**The Core Concept:**
The DI container automatically manages the lifecycle of the objects it creates.

**Key Details:**
- If the DI container creates a service that implements `IDisposable`, it will automatically call `Dispose()` on it when the service's lifetime ends (e.g., at the end of the HTTP request for Scoped services). You should *never* manually dispose of DI-resolved objects.
**Example:** `using` statements are not needed for injected EF Core contexts.
**Reference:** [DI Guidelines](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-guidelines)

### 34. What is the `[FromServices]` attribute?
**Answer:** 
**The Core Concept:**
Injects a dependency directly into a controller action method.

**Key Details:**
- Instead of injecting a service into the Controller's constructor (which instantiates it for every endpoint), `[FromServices]` injects it only into the specific action that needs it, optimizing memory if the controller is massive.
**Example:** `public IActionResult Get([FromServices] IMyService service)`
**Reference:** [Method Injection](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/dependency-injection#action-injection-with-fromservices)

### 35. What is the `IHttpClientFactory`?
**Answer:** 
**The Core Concept:**
The recommended way to create `HttpClient` instances in .NET Core.

**Key Details:**
- Instantiating `HttpClient` manually leads to socket exhaustion. Making it a static Singleton leads to DNS caching bugs.
- `IHttpClientFactory` manages an internal pool of HTTP message handlers, solving both socket exhaustion and DNS issues natively.
**Example:** `services.AddHttpClient("GitHub", c => c.BaseAddress = new Uri("https://api.github.com/"));`
**Reference:** [IHttpClientFactory](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/use-httpclientfactory-to-implement-resilient-http-requests)

### 36. Explain Cross-Origin Resource Sharing (CORS) in ASP.NET Core.
**Answer:** 
**The Core Concept:**
A browser security feature restricting web pages from making requests to a different domain.

**Key Details:**
- ASP.NET Core provides CORS middleware (`app.UseCors()`) to explicitly allow specific domains, HTTP methods, and headers to interact with the API, preventing browser blocking.
**Example:** `builder.Services.AddCors(options => { options.AddPolicy("AllowAll", ...); });`
**Reference:** [Enable CORS](https://learn.microsoft.com/en-us/aspnet/core/security/cors)

### 37. What is Data Protection in ASP.NET Core?
**Answer:** 
**The Core Concept:**
The cryptographic API used to protect data like cookies, anti-CSRF tokens, and passwords.

**Key Details:**
- In distributed environments (web farms), if Server A encrypts a cookie, Server B must be able to decrypt it. Data Protection requires configuring a shared key ring (e.g., storing keys in Redis or Azure Blob Storage).
**Example:** `services.AddDataProtection().PersistKeysToAzureBlobStorage(...)`
**Reference:** [Data Protection](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/introduction)

### 38. What is the API Gateway pattern?
**Answer:** 
**The Core Concept:**
A design pattern where a single entry point sits in front of multiple microservices.

**Key Details:**
- In the .NET ecosystem, libraries like Ocelot or YARP (Yet Another Reverse Proxy) act as the gateway, handling routing, rate limiting, and authentication before forwarding requests to internal APIs.
**Example:** Routing `/api/users` to the User Microservice and `/api/orders` to the Order Microservice.
**Reference:** [API Gateway](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/direct-client-to-microservice-communication-versus-the-api-gateway-pattern)

### 39. What is Health Checks in ASP.NET Core?
**Answer:** 
**The Core Concept:**
A built-in middleware mechanism to expose the status of the app to external monitoring tools.

**Key Details:**
- It allows load balancers (like Nginx) or orchestrators (like Kubernetes) to query an endpoint (`/health`). If it returns 503 Unhealthy (e.g., because the database is down), Kubernetes will kill the pod and spin up a new one.
**Example:** `services.AddHealthChecks().AddSqlServer(connectionString);`
**Reference:** [Health checks](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks)

### 40. What is Hosted Services (Background Tasks)?
**Answer:** 
**The Core Concept:**
A way to run background tasks completely independently of the HTTP request pipeline.

**Key Details:**
- Implementing the `IHostedService` interface (usually inheriting `BackgroundService`) allows you to run long-running tasks like processing message queues, polling a database, or cleaning up files in the background while the web server serves UI.
**Example:** `services.AddHostedService<MyQueueProcessor>();`
**Reference:** [Background tasks](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services)

### 41. How does Content Negotiation work in ASP.NET Core?
**Answer:** 
**The Core Concept:**
The process of selecting the best response format (JSON, XML) based on what the client requested.

**Key Details:**
- The client sends an `Accept` header (e.g., `Accept: application/xml`). If the API is configured with an XML formatter, ASP.NET automatically serializes the C# object to XML instead of JSON.
**Example:** `services.AddControllers().AddXmlSerializerFormatters();`
**Reference:** [Formatting response data](https://learn.microsoft.com/en-us/aspnet/core/web-api/advanced/formatting)

### 42. What is Response Caching?
**Answer:** 
**The Core Concept:**
Reduces server load by caching the output of a controller action.

**Key Details:**
- The `[ResponseCache]` attribute sets cache-related HTTP headers (like `Cache-Control`). It instructs the client browser or intermediate proxy servers to store the response, drastically speeding up subsequent identical requests.
**Example:** `[ResponseCache(Duration = 60)]`
**Reference:** [Response caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/response)

### 43. What is Distributed Caching?
**Answer:** 
**The Core Concept:**
A cache shared by multiple app servers, usually maintained as an external service (like Redis).

**Key Details:**
- If your app is load-balanced across 5 servers, using local memory caching (IMemoryCache) means users hitting Server A won't see cached data from Server B. Distributed Caching solves this, ensuring cache consistency.
**Example:** `services.AddStackExchangeRedisCache(...)`
**Reference:** [Distributed caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/distributed)

### 44. Explain the Repository Pattern in .NET.
**Answer:** 
**The Core Concept:**
An abstraction layer between the Data Access Layer (EF Core) and the Business Logic Layer.

**Key Details:**
- It encapsulates the logic required to access data sources. While highly debated (as EF Core `DbSet` is already a repository), it makes unit testing easier by allowing you to mock the `IUserRepository` instead of mocking the massive EF Core context.
**Example:** `public class UserRepository : IUserRepository { ... }`
**Reference:** [Repository Pattern](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design)

### 45. What is the Unit of Work pattern?
**Answer:** 
**The Core Concept:**
A pattern used to group multiple database operations into a single transaction.

**Key Details:**
- If an operation requires saving to the Users table and the Logs table, Unit of Work ensures both succeed or both fail. In .NET, the EF Core `DbContext` inherently implements the Unit of Work pattern via `SaveChanges()`.
**Example:** `await _context.SaveChangesAsync();`
**Reference:** [Unit of Work](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-implementation-entity-framework-core)

### 46. What is AutoMapper?
**Answer:** 
**The Core Concept:**
A popular 3rd-party library used for object-to-object mapping.

**Key Details:**
- It eliminates the tedious, error-prone boilerplate code required to map properties from a Database Entity class to a DTO class (`dto.Name = entity.Name`).
**Example:** `_mapper.Map<UserDto>(userEntity);`
**Reference:** [AutoMapper](https://automapper.org/)

### 47. What is Serilog?
**Answer:** 
**The Core Concept:**
A highly popular 3rd-party logging framework for .NET.

**Key Details:**
- Unlike traditional text loggers, Serilog is built for "Structured Logging". It logs data objects in a queryable format (like JSON), making it incredibly easy to search through logs in systems like Elasticsearch or Application Insights.
**Example:** `Log.Information("User {UserId} logged in", user.Id);`
**Reference:** [Serilog](https://serilog.net/)

### 48. What is Polly?
**Answer:** 
**The Core Concept:**
A resilience and transient-fault-handling library.

**Key Details:**
- If your API makes a request to a 3rd-party API and it fails due to a micro-network blip, Polly automatically retries the request a defined number of times. It supports Retry, Circuit Breaker, Timeout, and Fallback policies.
**Example:** `.AddTransientHttpErrorPolicy(policy => policy.WaitAndRetryAsync(3, ...))`
**Reference:** [Polly](https://github.com/App-vNext/Polly)

### 49. What is xUnit vs NUnit vs MSTest?
**Answer:** 
**The Core Concept:**
They are the three primary Unit Testing frameworks in the .NET ecosystem.

**Key Details:**
- **MSTest:** Built-in by Microsoft, oldest.
- **NUnit:** Historically the most popular port of JUnit.
- **xUnit:** The modern standard, created by the original NUnit authors. It runs tests in isolation, removes global state, and is used internally by the .NET core team itself.
**Example:** `[Fact]` in xUnit vs `[Test]` in NUnit.
**Reference:** [Unit testing](https://learn.microsoft.com/en-us/dotnet/core/testing/)

### 50. Explain the CQRS Pattern.
**Answer:** 
**The Core Concept:**
Command and Query Responsibility Segregation.

**Key Details:**
- It dictates that you should split your application architecture into two distinct parts: Commands (operations that mutate state, like INSERT/UPDATE) and Queries (operations that read state, like SELECT).
- Often implemented in .NET using the **MediatR** library to drastically decouple controllers from business logic.
**Example:** `mediator.Send(new CreateUserCommand(data))`
**Reference:** [CQRS](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)

### 51. What is MediatR?
**Answer:** 
**The Core Concept:**
A popular in-process messaging library that implements the Mediator pattern.

**Key Details:**
- It decouples objects by removing direct dependencies between them. Controllers no longer inject 10 different services; they inject `IMediator` and send request objects. MediatR automatically routes the request to the correct handler class.
**Example:** `public class CreateUserHandler : IRequestHandler<CreateUserCommand, User>`
**Reference:** [MediatR GitHub](https://github.com/jbogard/MediatR)

### 52. What is FluentValidation?
**Answer:** 
**The Core Concept:**
A 3rd-party library for building strongly-typed validation rules.

**Key Details:**
- It replaces C# Data Annotations (`[Required]`, `[MaxLength]`) on models, keeping the models clean. Validation logic is moved to dedicated Validator classes utilizing a fluent, chainable API.
**Example:** `RuleFor(x => x.Email).NotEmpty().EmailAddress();`
**Reference:** [FluentValidation](https://docs.fluentvalidation.net/)

### 53. How do you secure sensitive data (secrets) during development?
**Answer:** 
**The Core Concept:**
Never store API keys or connection strings in source code or `appsettings.json` uploaded to Git.

**Key Details:**
- During local development, use the **Secret Manager tool** (`dotnet user-secrets`), which stores secrets in a hidden folder on your local machine outside the repository.
- In production, use Environment Variables or Azure Key Vault.
**Example:** `dotnet user-secrets set "DbPassword" "123"`
**Reference:** [Safe storage of app secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets)

### 54. What is the `[ApiController]` attribute?
**Answer:** 
**The Core Concept:**
An attribute that applies highly opinionated, API-specific behaviors to controllers.

**Key Details:**
- It automatically handles Model State validation (returning 400 Bad Request if validation fails, removing the need for `if (!ModelState.IsValid)`).
- It requires Attribute Routing and implies that parameters are bound from the request body by default.
**Example:** `[ApiController] [Route("[controller]")] public class WeatherController`
**Reference:** [ApiController Attribute](https://learn.microsoft.com/en-us/aspnet/core/web-api/#apicontroller-attribute)

### 55. What is `IActionResult` vs `ActionResult<T>`?
**Answer:** 
**The Core Concept:**
Return types for API controller methods.

**Key Details:**
- `IActionResult` allows returning multiple HTTP status codes (`Ok()`, `NotFound()`), but hides the actual return type from Swagger/OpenAPI documentation.
- `ActionResult<T>` introduced in .NET Core 2.1, retains the flexibility of HTTP status returns but explicitly declares the return type, enabling automatic API documentation generation.
**Example:** `public ActionResult<User> GetUser() { return NotFound(); }`
**Reference:** [Controller action return types](https://learn.microsoft.com/en-us/aspnet/core/web-api/action-return-types)

### 56. Explain the difference between `AddTransient`, `AddScoped`, and `AddSingleton`.
**Answer:** 
**The Core Concept:**
They define the lifetime of a Dependency Injection service.

**Key Details:**
- **Transient:** Created fresh every single time it is asked for. Use for lightweight, stateless services.
- **Scoped:** Created once per client HTTP request. Use for database contexts (`DbContext`).
- **Singleton:** Created once upon app startup and shared across every request. Use for in-memory caches.
**Example:** `services.AddScoped<IUserRepository, UserRepository>();`
**Reference:** [Service lifetimes](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection#service-lifetimes)

### 57. What is Kestrel vs IIS?
**Answer:** 
**The Core Concept:**
Kestrel is the native cross-platform web server for .NET. IIS is the Windows web server.

**Key Details:**
- You do not use IIS to "run" ASP.NET Core apps. The app runs in Kestrel.
- IIS (or Nginx/Apache) is configured as a "Reverse Proxy" that sits in front of Kestrel. It handles security, load balancing, and port sharing (port 80/443), then forwards the raw traffic to Kestrel on an internal port.
**Example:** Hosting on Windows via IIS reverse proxy.
**Reference:** [Host and deploy](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/)

### 58. What is the Global Exception Handler in .NET 8?
**Answer:** 
**The Core Concept:**
A standardized way to handle exceptions globally without writing custom middleware.

**Key Details:**
- You implement the `IExceptionHandler` interface to process exceptions and register it via `builder.Services.AddExceptionHandler<MyHandler>()`. It cleanly separates exception processing from pipeline routing.
**Example:** Catching a `DbException` and returning a formatted JSON `ProblemDetails` response.
**Reference:** [IExceptionHandler](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling)

### 59. What is `ProblemDetails`?
**Answer:** 
**The Core Concept:**
A machine-readable format for specifying errors in HTTP API responses.

**Key Details:**
- It conforms to the RFC 7807 specification. ASP.NET Core natively returns this JSON format when returning 400 Bad Request or unhandled exceptions, ensuring APIs across different teams return standard error payloads.
**Example:** `{ "type": "...", "title": "Not Found", "status": 404 }`
**Reference:** [ProblemDetails](https://learn.microsoft.com/en-us/aspnet/core/web-api/handle-errors)

### 60. How does Swagger/OpenAPI integrate into .NET?
**Answer:** 
**The Core Concept:**
Swagger automatically generates interactive API documentation.

**Key Details:**
- Provided by the `Swashbuckle.AspNetCore` package (or natively in .NET 8/9). It inspects your controllers, routes, and `ActionResult<T>` signatures via Reflection to build a visual UI for testing the API.
**Example:** `app.UseSwaggerUI();`
**Reference:** [Swagger](https://learn.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger)

### 61. What are Action Results like `Ok()`, `BadRequest()`, and `NotFound()`?
**Answer:** 
**The Core Concept:**
Helper methods that return formatted HTTP status codes.

**Key Details:**
- They inherit from `ObjectResult` or `StatusCodeResult`. They abstract away the need to manually construct `HttpResponse` objects and set headers.
**Example:** `return BadRequest("Invalid ID");` (Returns HTTP 400).
**Reference:** [ControllerBase Methods](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.controllerbase)

### 62. Explain the concept of Shadow Properties in EF Core.
**Answer:** 
**The Core Concept:**
Properties that exist in the EF Core model but do not exist in the C# entity class.

**Key Details:**
- They are stored entirely inside the `DbContext` change tracker and the database schema. Highly useful for audit trails (like `LastModifiedDate`) where you don't want to clutter your Domain Models with infrastructure data.
**Example:** `modelBuilder.Entity<Blog>().Property<DateTime>("LastUpdated");`
**Reference:** [Shadow Properties](https://learn.microsoft.com/en-us/ef/core/modeling/shadow-properties)

### 63. What is Eager Loading vs Lazy Loading vs Explicit Loading?
**Answer:** 
**The Core Concept:**
Ways EF Core loads related database tables (navigation properties).

**Key Details:**
- **Eager Loading:** Uses `.Include()`. Pulls the parent and child data in a single SQL query.
- **Lazy Loading:** Automatically issues a new SQL query the moment the child property is accessed. (Dangerous, causes N+1 problems).
- **Explicit Loading:** Manually triggers the loading of a specific related entity at a later time using `.Entry().Collection().Load()`.
**Example:** Always default to Eager Loading for performance.
**Reference:** [Loading Related Data](https://learn.microsoft.com/en-us/ef/core/querying/related-data)

### 64. What is the `AsNoTracking()` method in EF Core?
**Answer:** 
**The Core Concept:**
A massive performance optimization for read-only queries.

**Key Details:**
- By default, EF Core tracks every object it retrieves from the database so it can detect changes if `SaveChanges()` is called.
- `AsNoTracking()` bypasses the change tracker completely, saving significant memory and CPU overhead. Use it exclusively for `GET` endpoints where no updates will occur.
**Example:** `context.Users.AsNoTracking().ToList();`
**Reference:** [Tracking vs. No-Tracking Queries](https://learn.microsoft.com/en-us/ef/core/querying/tracking)

### 65. What is Entity Framework Core Migrations?
**Answer:** 
**The Core Concept:**
A feature that applies schema changes from C# models to the database.

**Key Details:**
- Instead of writing raw `ALTER TABLE` SQL scripts, developers modify the C# classes. EF Core calculates the difference and generates a Migration file. This ensures version control over database schemas.
**Example:** `dotnet ef migrations add AddEmailColumn`
**Reference:** [Migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/)

### 66. How does .NET handle Cross-Site Request Forgery (CSRF)?
**Answer:** 
**The Core Concept:**
A security attack where a malicious site tricks a user's browser into making an unwanted request to a trusted site.

**Key Details:**
- .NET handles this using Anti-forgery tokens (Synchronizer Token Pattern). The server sends a unique hidden token in the HTML form and sets a matching cookie. When the form is submitted, the `[ValidateAntiForgeryToken]` attribute verifies both match.
**Example:** Using `@Html.AntiForgeryToken()` in MVC Razor views.
**Reference:** [Prevent CSRF](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery)

### 67. Explain Output Caching introduced in .NET 7.
**Answer:** 
**The Core Concept:**
A highly advanced, built-in caching middleware.

**Key Details:**
- Unlike traditional Response Caching (which relies on HTTP headers and the client's browser), Output Caching is entirely server-side. It intercepts the request pipeline, caches the raw output bytes, and serves them to all subsequent users globally. It supports tag-based invalidation.
**Example:** `app.UseOutputCache();`
**Reference:** [Output caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/output)

### 68. What are Endpoint Filters in Minimal APIs?
**Answer:** 
**The Core Concept:**
The Minimal API equivalent to MVC Action Filters.

**Key Details:**
- They allow running code before and after an endpoint executes. They are strictly functional and attached via the `.AddEndpointFilter()` extension method, enabling extreme performance validation or logging without heavy MVC class architecture.
**Example:** `app.MapGet("/").AddEndpointFilter<MyValidationFilter>();`
**Reference:** [Endpoint filters](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/responses)

### 69. What is Keyed Dependency Injection?
**Answer:** 
**The Core Concept:**
Introduced in .NET 8, it allows registering multiple implementations of the exact same interface.

**Key Details:**
- Previously, resolving multiple implementations required factory patterns. Now, you register them with a unique string/enum key. In the constructor, use the `[FromKeyedServices("key")]` attribute to specify exactly which implementation you want.
**Example:** `builder.Services.AddKeyedScoped<ICache, RedisCache>("redis");`
**Reference:** [Keyed services](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection#keyed-services)

### 70. What are Worker Services in .NET?
**Answer:** 
**The Core Concept:**
A specialized project template designed for creating long-running background processes (daemons or Windows Services).

**Key Details:**
- It uses the standard .NET Generic Host (`IHost`) to provide Dependency Injection, Logging, and Configuration, but strips out all the web server (Kestrel/HTTP) overhead. Perfect for message queue consumers.
**Example:** `dotnet new worker`
**Reference:** [Worker Services](https://learn.microsoft.com/en-us/dotnet/core/extensions/workers)

### 71. What is gRPC in .NET?
**Answer:** 
**The Core Concept:**
A modern, open-source, high-performance Remote Procedure Call (RPC) framework.

**Key Details:**
- It uses HTTP/2 for transport and Protocol Buffers (Protobuf) as the interface description language. It is incredibly fast and produces massive binary compression compared to JSON REST APIs.
- .NET provides first-class support for building gRPC services for microservice-to-microservice communication.
**Example:** Defining services in a `.proto` file.
**Reference:** [gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/)

### 72. Explain the concept of Channel in .NET.
**Answer:** 
**The Core Concept:**
A thread-safe data structure introduced for high-performance producer/consumer scenarios.

**Key Details:**
- Located in `System.Threading.Channels`, it acts like a queue but natively supports `async/await`.
- Producers write data asynchronously, and consumers read it asynchronously. It prevents thread blocking and memory exhaustion (via bounded channels).
**Example:** `var channel = Channel.CreateUnbounded<string>();`
**Reference:** [Channels](https://learn.microsoft.com/en-us/dotnet/core/extensions/channels)

### 73. What is `IAsyncDisposable`?
**Answer:** 
**The Core Concept:**
The asynchronous equivalent of `IDisposable`.

**Key Details:**
- It allows a class to release unmanaged resources asynchronously, preventing thread blocking during cleanup (like closing a database connection over the network).
- Used with `await using (...)`.
**Example:** `await using (var stream = new FileStream(...)) { }`
**Reference:** [IAsyncDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.iasyncdisposable)

### 74. What is the Generic Host (`IHostBuilder`)?
**Answer:** 
**The Core Concept:**
The core foundation of modern .NET apps that configures app startup, DI, logging, and configuration.

**Key Details:**
- Originally, ASP.NET Core had a `WebHostBuilder`. In .NET Core 3.0, it was refactored into the Generic Host so that non-web applications (like Worker Services or console apps) could use the exact same DI and logging architecture.
**Example:** `Host.CreateDefaultBuilder(args)`
**Reference:** [Generic Host](https://learn.microsoft.com/en-us/dotnet/core/extensions/generic-host)

### 75. Explain ASP.NET Core Rate Limiting.
**Answer:** 
**The Core Concept:**
A native middleware introduced in .NET 7 to control the rate of incoming requests.

**Key Details:**
- It protects servers from Denial of Service (DoS) attacks or brute force attacks. Supports algorithms like Fixed Window, Sliding Window, Token Bucket, and Concurrency limiting.
**Example:** `app.UseRateLimiter();`
**Reference:** [Rate limiting](https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit)

### 76. What is `IOptionsSnapshot<T>` vs `IOptionsMonitor<T>`?
**Answer:** 
**The Core Concept:**
They handle hot-reloading of configuration data (`appsettings.json`) without restarting the app.

**Key Details:**
- `IOptionsSnapshot` is scoped. It reads the latest config data at the start of an HTTP request and keeps it constant for the duration of that request.
- `IOptionsMonitor` is singleton. It continuously monitors for changes and can trigger an event handler the exact millisecond the JSON file is saved.
**Example:** Injecting `IOptionsSnapshot<MySettings>` into a controller.
**Reference:** [Options Pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options)

### 77. What is JWT Refresh Tokens architecture?
**Answer:** 
**The Core Concept:**
A mechanism to maintain secure, long-lived user sessions.

**Key Details:**
- JWTs should have a short lifespan (e.g., 15 mins) for security. When it expires, the client sends a separate, long-lived "Refresh Token" (stored securely in the DB) to a specific endpoint to receive a new JWT without forcing the user to log in again.
**Example:** If the Refresh Token is revoked in the DB, the user loses access after 15 mins.
**Reference:** [Refresh Tokens](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/)

### 78. What is Azure App Configuration?
**Answer:** 
**The Core Concept:**
A managed service that centrally manages application settings and feature flags.

**Key Details:**
- Instead of deploying `appsettings.json` files to 100 different microservices, they all pull their configuration securely from Azure on startup. Changing a value in the portal updates all microservices instantly.
**Example:** `builder.Configuration.AddAzureAppConfiguration(...)`
**Reference:** [Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview)

### 79. Explain EF Core Value Conversions.
**Answer:** 
**The Core Concept:**
Allows mapping a property type in the C# domain model to a different data type in the database.

**Key Details:**
- Example: Storing a C# `Enum` as a string (`VARCHAR`) in the database instead of an integer. Or storing a complex `List<string>` as a serialized JSON string in a single DB column.
**Example:** `builder.Property(e => e.Status).HasConversion<string>();`
**Reference:** [Value Conversions](https://learn.microsoft.com/en-us/ef/core/modeling/value-conversions)

### 80. What are Global Query Filters in EF Core?
**Answer:** 
**The Core Concept:**
LINQ query predicates automatically applied to entity queries.

**Key Details:**
- Highly useful for Multi-Tenant applications (always filtering by `TenantId`) or Soft Delete scenarios (always filtering by `IsDeleted == false`). It ensures developers never accidentally expose deleted or cross-tenant data.
**Example:** `modelBuilder.Entity<Post>().HasQueryFilter(p => !p.IsDeleted);`
**Reference:** [Global Query Filters](https://learn.microsoft.com/en-us/ef/core/querying/filters)

### 81. How does ASP.NET Core Handle File Uploads safely?
**Answer:** 
**The Core Concept:**
Handling `IFormFile` from multipart/form-data requests.

**Key Details:**
- Never trust the user's file name or extension. Always validate the magic numbers (file signatures) of the raw bytes to ensure an `.exe` isn't disguised as a `.png`. Buffer large files to disk/cloud storage immediately to prevent exhausting server RAM.
**Example:** Uploading a profile picture to Azure Blob Storage.
**Reference:** [File uploads](https://learn.microsoft.com/en-us/aspnet/core/mvc/models/file-uploads)

### 82. What is an `ActionFilterAttribute`?
**Answer:** 
**The Core Concept:**
A custom class that inherits from `ActionFilterAttribute` to create reusable pipeline logic.

**Key Details:**
- By overriding `OnActionExecuting` (before) and `OnActionExecuted` (after), you can create custom validation, logging, or header injection logic that can be applied to any controller via `[MyCustomFilter]`.
**Example:** Creating an `[AuditLog]` attribute.
**Reference:** [Filters](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/filters)

### 83. What is the purpose of `IDistributedCache` interface?
**Answer:** 
**The Core Concept:**
An abstraction over distributed caching implementations.

**Key Details:**
- By injecting `IDistributedCache`, your application doesn't care if it's using Redis, SQL Server, or NCache. You can switch caching providers in `Program.cs` without rewriting a single line of business logic.
**Example:** `await _cache.SetStringAsync(key, data);`
**Reference:** [IDistributedCache](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.caching.distributed.idistributedcache)

### 84. Explain the Circuit Breaker Pattern (via Polly).
**Answer:** 
**The Core Concept:**
Prevents an application from repeatedly trying to execute an operation that's likely to fail.

**Key Details:**
- If a 3rd-party API goes down, sending 1000 retries will overwhelm both systems. A circuit breaker "trips" (opens) after X failures, instantly rejecting all new requests for a cooldown period, giving the failing system time to recover.
**Example:** Polly `CircuitBreakerAsync(exceptionsAllowedBeforeBreaking: 3, durationOfBreak: TimeSpan.FromSeconds(30))`
**Reference:** [Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)

### 85. What is the Outbox Pattern?
**Answer:** 
**The Core Concept:**
A microservices pattern for reliable messaging.

**Key Details:**
- If your API saves to a database and publishes an event to RabbitMQ, what happens if the database succeeds but RabbitMQ is down? Data inconsistency.
- The Outbox pattern saves the message into an "Outbox" table in the *same database transaction*. A separate background worker reads the Outbox table and reliably publishes to RabbitMQ.
**Example:** Implementing reliable domain events.
**Reference:** [Outbox Pattern](https://microservices.io/patterns/data/transactional-outbox.html)

### 86. How do you implement Semantic Logging in .NET?
**Answer:** 
**The Core Concept:**
Using strongly-typed log events instead of string concatenation.

**Key Details:**
- Instead of `Logger.Log($"User {id} failed login")`, use `Logger.Log("User {UserId} failed login", id)`. The logging framework (like Serilog) captures `UserId` as a distinct searchable column in the database/Elasticsearch, rather than just raw text.
**Example:** High-performance logging using `LoggerMessage` delegates.
**Reference:** [High-performance logging](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logger-message)

### 87. What are C# 12 Primary Constructors?
**Answer:** 
**The Core Concept:**
A concise syntax to declare constructors directly on the class declaration.

**Key Details:**
- It drastically reduces boilerplate for Dependency Injection. Instead of declaring private read-only fields and writing a constructor to assign them, you simply put the parameters next to the class name.
**Example:** `public class UserService(IUserRepository repo) { ... }`
**Reference:** [Primary constructors](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-12#primary-constructors)

### 88. What is `Task.FromResult<T>`?
**Answer:** 
**The Core Concept:**
Creates a `Task` that has already completed successfully with the specified result.

**Key Details:**
- Useful when implementing an interface that requires returning a `Task`, but your specific implementation executes synchronously (e.g., retrieving data from an in-memory dictionary instead of a database).
**Example:** `public Task<string> GetName() { return Task.FromResult("John"); }`
**Reference:** [Task.FromResult](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromresult)

### 89. What is the `.NET GC Server vs Workstation` mode?
**Answer:** 
**The Core Concept:**
The CLR Garbage Collector has two distinct modes optimized for different workloads.

**Key Details:**
- **Workstation:** Optimized for desktop apps (UI responsiveness). Collections happen frequently but fast.
- **Server:** Optimized for high-throughput web servers (ASP.NET Core default). It creates a dedicated GC thread for every logical CPU core, pausing execution longer but clearing massive amounts of memory simultaneously.
**Example:** Configured via `<ServerGarbageCollection>true</ServerGarbageCollection>`.
**Reference:** [Workstation and server garbage collection](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/workstation-server-gc)

### 90. Explain `ValueTask<T>`.
**Answer:** 
**The Core Concept:**
A lightweight alternative to `Task<T>`.

**Key Details:**
- `Task` is a reference type (allocated on the heap). If a method frequently completes synchronously (e.g., hitting a cache 99% of the time), allocating a `Task` causes heavy GC pressure.
- `ValueTask` is a struct (stack-allocated). It avoids heap allocation entirely if the operation completes synchronously.
**Example:** `public async ValueTask<int> GetValueAsync()`
**Reference:** [ValueTask](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.valuetask-1)

### 91. What is the Options Validation feature in ASP.NET Core?
**Answer:** 
**The Core Concept:**
Ensuring that configuration data loaded from `appsettings.json` is valid before the app starts.

**Key Details:**
- You can use Data Annotations (`[Required]`, `[Range]`) on your settings classes. By appending `.ValidateDataAnnotations()` during DI registration, the app will refuse to boot up if critical configuration (like a connection string) is missing or malformed.
**Example:** `services.AddOptions<MyConfig>().BindConfiguration("Config").ValidateDataAnnotations();`
**Reference:** [Options validation](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options#options-validation)

### 92. What are .NET Runtime Diagnostics (dotnet-counters, dotnet-trace)?
**Answer:** 
**The Core Concept:**
A suite of CLI tools for monitoring .NET performance in production.

**Key Details:**
- `dotnet-counters`: Monitors real-time metrics (CPU, Memory, GC allocations).
- `dotnet-trace`: Captures deep execution traces (flame graphs) to find CPU bottlenecks.
- `dotnet-dump`: Captures and analyzes memory dumps to find memory leaks.
**Example:** Running `dotnet-counters monitor -p 1234` on a Linux server.
**Reference:** [Diagnostic tools](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/)

### 93. Explain the Out-of-Process vs In-Process hosting models.
**Answer:** 
**The Core Concept:**
How ASP.NET Core apps run when placed behind IIS.

**Key Details:**
- **In-Process (Default):** The app is hosted directly inside the IIS worker process (`w3wp.exe`). Massively faster because requests don't cross process boundaries.
- **Out-of-Process:** The app runs in its own `dotnet.exe` Kestrel process, and IIS acts purely as a network proxy. Slower, but isolates the app from IIS crashes.
**Example:** Configured via `<AspNetCoreHostingModel>InProcess</AspNetCoreHostingModel>`.
**Reference:** [In-process hosting](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/in-process-hosting)

### 94. What is the `.AddDbContextPool()` method?
**Answer:** 
**The Core Concept:**
A performance optimization for EF Core.

**Key Details:**
- Instead of creating and disposing of a `DbContext` instance for every single HTTP request, DbContext Pooling retains a pool of reusable context instances. This drastically reduces the CPU overhead of initializing EF Core under high load.
**Example:** `services.AddDbContextPool<MyContext>(options => ...);`
**Reference:** [DbContext pooling](https://learn.microsoft.com/en-us/ef/core/performance/advanced-performance-topics#dbcontext-pooling)

### 95. What are Resilient Connections in EF Core?
**Answer:** 
**The Core Concept:**
Handling transient database connection failures automatically.

**Key Details:**
- In cloud environments (like Azure SQL), connections are occasionally dropped for load balancing. EF Core provides an `EnableRetryOnFailure()` execution strategy that automatically catches connection exceptions and safely retries the query.
**Example:** `options.UseSqlServer(str, sql => sql.EnableRetryOnFailure());`
**Reference:** [Connection resiliency](https://learn.microsoft.com/en-us/ef/core/miscellaneous/connection-resiliency)

### 96. What is the `IHttpContextAccessor`?
**Answer:** 
**The Core Concept:**
A service used to access the current `HttpContext` from outside a controller.

**Key Details:**
- Controllers have native access to `HttpContext`. If a deep Business Logic service needs access to the user's claims or HTTP headers, it must inject `IHttpContextAccessor`.
- It has a slight performance overhead and must be registered explicitly in `Program.cs`.
**Example:** `services.AddHttpContextAccessor();`
**Reference:** [Access HttpContext](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-context)

### 97. What is API Versioning?
**Answer:** 
**The Core Concept:**
Managing breaking changes by supporting multiple versions of an API concurrently.

**Key Details:**
- .NET supports this via `Asp.Versioning.Mvc`. Versions can be passed via URL path (`/api/v1/users`), Query String (`?api-version=1.0`), or HTTP Headers (`x-api-version`).
**Example:** `[ApiVersion("1.0")] [Route("api/v{version:apiVersion}/[controller]")]`
**Reference:** [API Versioning](https://github.com/dotnet/aspnet-api-versioning)

### 98. How does `User.Claims` work for Authorization?
**Answer:** 
**The Core Concept:**
Claims-based authorization evaluates the specific properties (claims) attached to a user's identity.

**Key Details:**
- When a JWT is validated, its payload is parsed into `Claims`. Instead of checking `IsInRole("Admin")`, modern .NET uses Policies. You define a policy ("MustBeOver18") that checks if the "Age" claim is > 18.
**Example:** `[Authorize(Policy = "MustBeOver18")]`
**Reference:** [Claims-based authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/claims)

### 99. What are Endpoint Routing and `MapControllers()`?
**Answer:** 
**The Core Concept:**
The routing architecture introduced in ASP.NET Core 3.0.

**Key Details:**
- It separates the *decision* of which endpoint to execute from the *execution* of the endpoint. This allows middleware (like Authorization) to know which endpoint is about to be executed before it actually runs.
**Example:** `app.UseRouting(); app.UseAuthorization(); app.MapControllers();`
**Reference:** [Routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing)

### 100. Explain OpenTelemetry integration in .NET.
**Answer:** 
**The Core Concept:**
The modern standard for distributed tracing and observability.

**Key Details:**
- .NET 8 has massive native support for OpenTelemetry. It automatically instruments HTTP requests, EF Core queries, and gRPC calls, exporting the tracing data (spans and metrics) to tools like Jaeger, Prometheus, or Datadog, providing full visibility across microservices.
**Example:** `builder.Services.AddOpenTelemetry().WithTracing(...)`
**Reference:** [OpenTelemetry in .NET](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-opentelemetry)
