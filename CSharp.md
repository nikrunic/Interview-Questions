# C# Interview Questions

This document contains a comprehensive list of C# interview questions, categorized by difficulty.

## Basic (10 Questions)

### 1. What is C#?
**Answer:** 
**The Core Concept:**
C# (pronounced "C-Sharp") is a modern, object-oriented, and type-safe programming language developed by Microsoft.

**Key Details:**
- It runs on the .NET framework and is widely used for building Windows desktop apps, web apps (ASP.NET), and games (Unity).
- It is heavily inspired by C++ and Java.
**Example:** `Console.WriteLine("Hello World");`
**Reference:** [C# Docs](https://learn.microsoft.com/en-us/dotnet/csharp/)

### 2. What is the difference between a class and a struct in C#?
**Answer:** 
**The Core Concept:**
A `class` is a reference type, while a `struct` is a value type.

**Key Details:**
- Classes are allocated on the heap and are garbage collected.
- Structs are allocated on the stack (usually) and are faster for small data structures.
- Classes support inheritance, whereas structs do not.
**Example:** `public class MyClass {}` vs `public struct MyStruct {}`
**Reference:** [Classes and Structs](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes)

### 3. What are Value Types and Reference Types?
**Answer:** 
**The Core Concept:**
Value types directly contain their data, while reference types store a reference (memory address) to their data.

**Key Details:**
- Value types (int, float, bool, struct) are stored on the stack.
- Reference types (string, class, array, delegate) are stored on the heap.
**Example:** `int a = 5;` (Value) vs `string b = "Hello";` (Reference)
**Reference:** [Value Types vs Reference Types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types)

### 4. What is the difference between `ref` and `out` keywords?
**Answer:** 
**The Core Concept:**
Both are used to pass arguments by reference rather than by value.

**Key Details:**
- `ref` requires the variable to be initialized *before* it is passed to the method.
- `out` does not require prior initialization but requires the method to assign a value before returning.
**Example:** `public void Calculate(out int result)`
**Reference:** [ref and out](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref)

### 5. What are Properties in C#?
**Answer:** 
**The Core Concept:**
Properties are members that provide a flexible mechanism to read, write, or compute the value of a private field.

**Key Details:**
- They encapsulate fields using `get` and `set` accessors, allowing data validation without exposing the internal representation.
**Example:** `public int Age { get; set; }`
**Reference:** [Properties](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties)

### 6. What is the purpose of the `using` statement?
**Answer:** 
**The Core Concept:**
It ensures that unmanaged resources are correctly and immediately disposed of when they are no longer needed.

**Key Details:**
- It is syntactic sugar for a `try-finally` block that calls the `Dispose()` method of objects implementing `IDisposable`.
**Example:** `using (var reader = new StreamReader("file.txt")) { ... }`
**Reference:** [using Statement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/using)

### 7. What is an Interface?
**Answer:** 
**The Core Concept:**
An interface contains only the signatures of methods, properties, events, or indexers.

**Key Details:**
- A class or struct that implements the interface must provide the implementation for all its members.
- C# does not support multiple inheritance for classes, but allows a class to implement multiple interfaces.
**Example:** `public interface IAnimal { void Speak(); }`
**Reference:** [Interfaces](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/interfaces)

### 8. What is Enum in C#?
**Answer:** 
**The Core Concept:**
An enumeration (`enum`) is a distinct value type consisting of a set of named constants.

**Key Details:**
- By default, the underlying type of enum elements is `int`, starting at 0.
- They make code more readable by replacing magic numbers with meaningful names.
**Example:** `public enum Days { Monday, Tuesday, Wednesday }`
**Reference:** [Enums](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum)

### 9. What is a Namespace?
**Answer:** 
**The Core Concept:**
A namespace is used to organize code and prevent naming conflicts.

**Key Details:**
- It acts as a logical container for classes, interfaces, enums, and other namespaces.
- Accessed using the `using` directive at the top of a file.
**Example:** `namespace MyApplication { class Program {} }`
**Reference:** [Namespaces](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/namespaces)

### 10. Explain the `static` keyword.
**Answer:** 
**The Core Concept:**
The `static` modifier declares a member that belongs to the type itself rather than to a specific object.

**Key Details:**
- You do not need to instantiate a class to call a static method or access a static field.
- A static class cannot be instantiated at all.
**Example:** `Math.Round(3.14);`
**Reference:** [Static Classes and Members](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members)

## Medium (10 Questions)

### 11. What is Boxing and Unboxing?
**Answer:** 
**The Core Concept:**
Boxing is the process of converting a value type to the `object` reference type. Unboxing is the reverse.

**Key Details:**
- Boxing allocates memory on the heap and copies the value.
- Unboxing extracts the value from the object. Both operations are computationally expensive and should be avoided in performance-critical code.
**Example:** `int i = 123; object o = i; // Boxing`
**Reference:** [Boxing and Unboxing](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/types/boxing-and-unboxing)

### 12. What are Delegates?
**Answer:** 
**The Core Concept:**
A delegate is a type that represents references to methods with a particular parameter list and return type.

**Key Details:**
- They are similar to function pointers in C++, but are type-safe and secure.
- Used extensively for defining callback methods and handling events.
**Example:** `public delegate void MyDelegate(string msg);`
**Reference:** [Delegates](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

### 13. What is the difference between `String` and `StringBuilder`?
**Answer:** 
**The Core Concept:**
`String` is immutable, while `StringBuilder` is mutable.

**Key Details:**
- Modifying a `String` (like concatenation) creates a brand new string object in memory, which is inefficient in loops.
- `StringBuilder` dynamically expands its memory buffer, making it much faster for repetitive string manipulations.
**Example:** `StringBuilder sb = new StringBuilder(); sb.Append("Hello");`
**Reference:** [StringBuilder Class](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder)

### 14. What are Generics in C#?
**Answer:** 
**The Core Concept:**
Generics allow you to design classes and methods that defer the specification of one or more types until the class or method is declared.

**Key Details:**
- They maximize code reuse, type safety, and performance by preventing boxing/unboxing operations for value types.
**Example:** `List<int> numbers = new List<int>();`
**Reference:** [Generics](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics)

### 15. What is LINQ?
**Answer:** 
**The Core Concept:**
Language Integrated Query (LINQ) provides a consistent querying syntax directly integrated into C#.

**Key Details:**
- It allows you to query various data sources (Collections, SQL databases, XML) using a SQL-like syntax or method chaining natively in code.
**Example:** `var adults = users.Where(u => u.Age >= 18);`
**Reference:** [LINQ](https://learn.microsoft.com/en-us/dotnet/csharp/linq/)

### 16. What is an Extension Method?
**Answer:** 
**The Core Concept:**
Extension methods allow you to "add" methods to existing types without creating a new derived type or modifying the original type.

**Key Details:**
- They are defined as static methods inside a static class, using the `this` keyword before the first parameter.
**Example:** `public static int WordCount(this string str) { ... }`
**Reference:** [Extension Methods](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/extension-methods)

### 17. What is the `virtual` keyword?
**Answer:** 
**The Core Concept:**
The `virtual` keyword is used to modify a method, property, or event declaration and allow for it to be overridden in a derived class.

**Key Details:**
- Unlike abstract methods, virtual methods must have a default implementation.
**Example:** `public virtual void Draw() { }`
**Reference:** [Virtual](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)

### 18. What is the difference between `abstract` class and `interface`?
**Answer:** 
**The Core Concept:**
An interface is an empty contract, while an abstract class can provide some base implementation.

**Key Details:**
- A class can inherit from only one abstract class, but can implement multiple interfaces.
- Abstract classes can have fields, constructors, and access modifiers. Interfaces (traditionally) cannot.
**Example:** `public abstract class Shape { }`
**Reference:** [Abstract vs Interface](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

### 19. What is Reflection in C#?
**Answer:** 
**The Core Concept:**
Reflection is the ability of managed code to read its own metadata to find assemblies, modules, and type information at runtime.

**Key Details:**
- It allows dynamic instantiation of types, invocation of methods, and accessing private fields.
- Used heavily by ORMs and dependency injection frameworks, though it has a performance cost.
**Example:** `Type t = typeof(MyClass);`
**Reference:** [Reflection](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection)

### 20. Explain `async` and `await`.
**Answer:** 
**The Core Concept:**
These keywords are used for asynchronous programming, allowing the main thread (like UI or web requests) to remain unblocked while waiting for a long-running task to complete.

**Key Details:**
- `async` marks a method as asynchronous, and `await` pauses the execution of that method until the awaited task finishes, returning control to the caller.
**Example:** `public async Task<string> GetDataAsync() { return await httpClient.GetStringAsync(url); }`
**Reference:** [Asynchronous Programming](https://learn.microsoft.com/en-us/dotnet/csharp/async)

## Hard (10 Questions)

### 21. How does Garbage Collection (GC) work in C#?
**Answer:** 
**The Core Concept:**
The GC manages the allocation and release of memory for an application automatically.

**Key Details:**
- It operates on a generational model (Generation 0, 1, and 2). Gen 0 contains short-lived objects. If an object survives a collection, it is promoted to the next generation.
- It helps prevent memory leaks but can cause application pauses during "Stop the World" collections.
**Example:** `GC.Collect(); // Forces collection (not recommended)`
**Reference:** [Garbage Collection](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/)

### 22. What is the difference between `Task` and `Thread`?
**Answer:** 
**The Core Concept:**
A `Thread` is a low-level OS construct, while a `Task` is a higher-level abstraction managed by the ThreadPool.

**Key Details:**
- Tasks represent asynchronous operations and return a value (`Task<T>`).
- Tasks are more efficient because they reuse threads from the ThreadPool rather than incurring the heavy cost of creating a new OS thread.
**Example:** `Task.Run(() => DoWork());`
**Reference:** [Task vs Thread](https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-parallel-library-tpl)

### 23. What is the `yield` keyword?
**Answer:** 
**The Core Concept:**
The `yield` keyword is used to perform custom, stateful iteration over a collection.

**Key Details:**
- `yield return` provides the next value in iteration and preserves the current location in the code. Execution is restarted from that location the next time the iterator is called.
- It enables lazy evaluation of collections, saving massive amounts of memory.
**Example:** `IEnumerable<int> GetNumbers() { yield return 1; yield return 2; }`
**Reference:** [yield](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/yield)

### 24. Explain Dependency Injection (DI) in C#.
**Answer:** 
**The Core Concept:**
DI is a design pattern used to implement Inversion of Control (IoC), allowing the creation of dependent objects outside of a class and passing them in.

**Key Details:**
- It promotes loose coupling, making code vastly easier to test and maintain.
- Standard in ASP.NET Core, configured via `IServiceCollection` (AddTransient, AddScoped, AddSingleton).
**Example:** `public MyController(ILogger logger) { _logger = logger; }`
**Reference:** [Dependency Injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection)

### 25. What is the difference between `IQueryable` and `IEnumerable`?
**Answer:** 
**The Core Concept:**
Both are interfaces for iterating collections, but `IQueryable` is specifically optimized for out-of-memory data sources like SQL databases.

**Key Details:**
- `IEnumerable` executes the query in memory (client-side), meaning it pulls all records from the DB before filtering.
- `IQueryable` builds an expression tree and executes the filter on the server-side (database), making it highly performant for database queries.
**Example:** Entity Framework `DbSet` implements `IQueryable`.
**Reference:** [IEnumerable vs IQueryable](https://learn.microsoft.com/en-us/dotnet/api/system.linq.iqueryable)

### 26. What are Expression Trees?
**Answer:** 
**The Core Concept:**
Expression trees represent code in a tree-like data structure, where each node is an expression (e.g., a method call or a binary operation).

**Key Details:**
- Instead of compiling code into executable IL immediately, it compiles it into a data structure that can be inspected, modified, or translated into another language (like SQL via Entity Framework) at runtime.
**Example:** `Expression<Func<int, bool>> expr = num => num < 5;`
**Reference:** [Expression Trees](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/expression-trees/)

### 27. How does the `lock` statement work?
**Answer:** 
**The Core Concept:**
The `lock` statement acquires the mutual-exclusion lock for a given object, executes a statement block, and then releases the lock.

**Key Details:**
- It prevents multiple threads from executing a critical section of code simultaneously, avoiding race conditions.
- It is syntactic sugar for `Monitor.Enter` and `Monitor.Exit`.
**Example:** `lock (_syncObject) { balance -= amount; }`
**Reference:** [lock statement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

### 28. What are covariance and contravariance in C#?
**Answer:** 
**The Core Concept:**
They define how generic type parameters handle inheritance hierarchies.

**Key Details:**
- Covariance (`out`) allows you to use a more derived type than originally specified (e.g., assigning `IEnumerable<Derived>` to `IEnumerable<Base>`).
- Contravariance (`in`) allows you to use a more generic (less derived) type (e.g., passing `Action<Base>` to `Action<Derived>`).
**Example:** `IEnumerable<out T>` vs `IComparer<in T>`.
**Reference:** [Covariance and Contravariance](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/covariance-contravariance/)

### 29. What is the difference between `Finalize` and `Dispose`?
**Answer:** 
**The Core Concept:**
Both are used to free unmanaged resources, but `Dispose` is deterministic while `Finalize` is non-deterministic.

**Key Details:**
- `Dispose` is explicitly called by the developer (via `IDisposable` and the `using` statement) to clean up immediately.
- `Finalize` (destructor `~MyClass()`) is called automatically by the Garbage Collector before the object is destroyed, acting as a safety net if `Dispose` wasn't called.
**Example:** Implementing the Dispose Pattern.
**Reference:** [Dispose Pattern](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose)

### 30. What is `volatile` keyword?
**Answer:** 
**The Core Concept:**
The `volatile` keyword indicates that a field might be modified by multiple threads executing at the same time.

**Key Details:**
- The compiler, runtime system, or hardware may perform optimizations that reorder memory reads/writes. `volatile` prevents these optimizations, ensuring the most up-to-date value is always read from main memory.
**Example:** `private volatile bool _shouldStop;`
**Reference:** [volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)
