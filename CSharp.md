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


### 31. What is the `readonly` keyword?
**Answer:** 
**The Core Concept:**
A modifier that prevents a field from being modified after it is initialized.

**Key Details:**
- A `readonly` field can only be assigned a value at the time of declaration or within the constructor of the same class.
- Unlike `const`, it can be initialized dynamically at runtime.
**Example:** `public readonly int MaxUsers;`
**Reference:** [readonly](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/readonly)

### 32. What is the `const` keyword?
**Answer:** 
**The Core Concept:**
A modifier that declares a field or local variable as a compile-time constant.

**Key Details:**
- The value must be known at compile time and cannot be changed.
- Constants are implicitly static; you access them via the type name, not the instance.
**Example:** `public const double Pi = 3.14159;`
**Reference:** [const](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/const)

### 33. What is the difference between `throw` and `throw ex`?
**Answer:** 
**The Core Concept:**
They dictate how exceptions are propagated up the call stack.

**Key Details:**
- `throw` re-throws the original exception, preserving the entire original stack trace (best practice).
- `throw ex` resets the stack trace to the line where `throw ex` is executed, hiding the true origin of the error (anti-pattern).
**Example:** `catch (Exception ex) { throw; }`
**Reference:** [Exception Handling](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/exception-handling)

### 34. What is a Tuple in C#?
**Answer:** 
**The Core Concept:**
A lightweight data structure that contains a specific number and sequence of elements.

**Key Details:**
- Introduced in C# 7, modern tuples use `ValueTuple` under the hood, making them value types that are great for returning multiple values from a method without creating `out` parameters or dedicated DTO classes.
**Example:** `public (int sum, int count) GetStats() { return (10, 2); }`
**Reference:** [Tuple types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-tuples)

### 35. What is the `dynamic` type?
**Answer:** 
**The Core Concept:**
A type that bypasses compile-time type checking.

**Key Details:**
- The compiler assumes that the `dynamic` object supports any operation. Type resolution happens entirely at runtime via the Dynamic Language Runtime (DLR).
- Useful when interacting with COM APIs (like Office Automation) or dynamic languages like Python.
**Example:** `dynamic obj = GetDynamicObject(); obj.DoSomething();`
**Reference:** [Using type dynamic](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/interop/using-type-dynamic)

### 36. What is the `var` keyword?
**Answer:** 
**The Core Concept:**
Implicitly types a local variable.

**Key Details:**
- The compiler determines the type at compile time based on the assigned value. It is strictly typed; once the type is inferred, it cannot be changed.
- It cannot be used for fields at the class level or for method return types.
**Example:** `var list = new List<string>();`
**Reference:** [Implicitly typed local variables](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/implicitly-typed-local-variables)

### 37. What are Attributes in C#?
**Answer:** 
**The Core Concept:**
Attributes are declarative tags used to convey metadata about types, methods, properties, or other program elements.

**Key Details:**
- The metadata can be inspected at runtime using Reflection.
- Heavily used in frameworks (like `[Obsolete]`, `[Serializable]`, `[Route]`, `[Authorize]`).
**Example:** `[Obsolete("Use NewMethod instead")] public void OldMethod() { }`
**Reference:** [Attributes](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/reflection-and-attributes/)

### 38. What is the difference between Array and ArrayList?
**Answer:** 
**The Core Concept:**
`Array` is strongly typed and fixed-size, whereas `ArrayList` is weakly typed and dynamic.

**Key Details:**
- `Array` can store primitives and objects without boxing, providing better performance.
- `ArrayList` stores everything as `object`, requiring boxing/unboxing. It is considered legacy and replaced by `List<T>`.
**Example:** `int[] arr = new int[5];` vs `ArrayList al = new ArrayList();`
**Reference:** [ArrayList Class](https://learn.microsoft.com/en-us/dotnet/api/system.collections.arraylist)

### 39. What is `IEnumerable`?
**Answer:** 
**The Core Concept:**
The foundational interface for all non-generic collections that can be enumerated (iterated over).

**Key Details:**
- It exposes a single method, `GetEnumerator()`, which allows a `foreach` loop to iterate through the collection. `IEnumerable<T>` is the strongly-typed generic version.
**Example:** `public IEnumerable<int> GetNumbers() { ... }`
**Reference:** [IEnumerable Interface](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable)

### 40. What is an Indexer?
**Answer:** 
**The Core Concept:**
Indexers allow instances of a class or struct to be indexed just like arrays.

**Key Details:**
- They are defined using the `this` keyword. They are essentially properties that take parameters (usually an `int` or `string`).
**Example:** `public string this[int index] { get { return arr[index]; } set { arr[index] = value; } }`
**Reference:** [Indexers](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/indexers/)

### 41. What is the difference between `==` and `.Equals()`?
**Answer:** 
**The Core Concept:**
Both check for equality, but they operate differently under the hood for reference types.

**Key Details:**
- For reference types, `==` typically checks for reference equality (do they point to the exact same object in memory).
- `.Equals()` can be overridden by the class to check for *value equality* (do the objects contain the same data). Strings natively override both to check for value equality.
**Example:** `objA.Equals(objB)`
**Reference:** [Equality comparisons](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/statements-expressions-operators/how-to-define-value-equality-for-a-type)

### 42. Explain the Null-conditional Operator (`?.`).
**Answer:** 
**The Core Concept:**
It provides a safe way to access members of an object that might be null.

**Key Details:**
- If the object is null, the expression evaluates to null rather than throwing a `NullReferenceException`.
- It drastically reduces the need for nested `if (obj != null)` checks.
**Example:** `int? length = user?.Name?.Length;`
**Reference:** [Null-conditional operators](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/member-access-operators#null-conditional-operators--and-)

### 43. What is the Null-coalescing Operator (`??`)?
**Answer:** 
**The Core Concept:**
It returns the left-hand operand if it isn't null; otherwise, it evaluates and returns the right-hand operand.

**Key Details:**
- Commonly used to provide default values.
- C# 8 introduced the null-coalescing assignment operator `??=`.
**Example:** `string name = inputName ?? "Default Name";`
**Reference:** [?? operator](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/null-coalescing-operator)

### 44. What is a Destructor (Finalizer)?
**Answer:** 
**The Core Concept:**
A special method invoked by the Garbage Collector before an object is destroyed from memory.

**Key Details:**
- Identified by a tilde (`~`) followed by the class name. It cannot be called manually.
- It is generally used as a fallback to release unmanaged resources if `Dispose()` was not called.
**Example:** `~MyClass() { // cleanup code }`
**Reference:** [Finalizers](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/destructors)

### 45. What are Partial Classes?
**Answer:** 
**The Core Concept:**
The `partial` keyword allows a class, struct, or interface to be split across multiple `.cs` files.

**Key Details:**
- During compilation, all the parts are combined into a single type.
- Heavily used in code-generation scenarios (like WinForms or EF Core designers) so that developer code and auto-generated code can live in separate files without overwriting each other.
**Example:** `public partial class Employee {}`
**Reference:** [Partial Classes and Methods](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/partial-classes-and-methods)

### 46. What is the difference between `break` and `continue`?
**Answer:** 
**The Core Concept:**
Both are jump statements used inside loops.

**Key Details:**
- `break` exits the nearest enclosing loop entirely.
- `continue` skips the remaining code in the current iteration and jumps to the next iteration of the loop.
**Example:** `if (skip) continue;`
**Reference:** [Jump Statements](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/jump-statements)

### 47. Explain the `params` keyword.
**Answer:** 
**The Core Concept:**
It allows a method to accept a variable number of arguments.

**Key Details:**
- It must be a single-dimensional array and must be the *last* parameter in the method signature.
- Callers can pass a comma-separated list of arguments, or an array, or nothing at all.
**Example:** `public void Log(params string[] messages) {}`
**Reference:** [params](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/params)

### 48. What is Method Overloading?
**Answer:** 
**The Core Concept:**
A type of static (compile-time) polymorphism where multiple methods can share the same name in a class.

**Key Details:**
- They must have different signatures (different number of parameters, different types of parameters, or different parameter order). The return type alone cannot be the differentiator.
**Example:** `public void Print(int i)` and `public void Print(string s)`
**Reference:** [Method Overloading](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods)

### 49. What is Method Overriding?
**Answer:** 
**The Core Concept:**
A type of dynamic (runtime) polymorphism where a derived class provides a specific implementation for a method defined in its base class.

**Key Details:**
- The base method must be marked as `virtual`, `abstract`, or `override`.
- The derived method uses the `override` keyword.
**Example:** `public override void Draw() { ... }`
**Reference:** [Knowing When to Use Override and New Keywords](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/knowing-when-to-use-override-and-new-keywords)

### 50. Explain the `new` keyword in method hiding.
**Answer:** 
**The Core Concept:**
The `new` modifier hides a member inherited from a base class.

**Key Details:**
- Unlike `override`, method hiding breaks polymorphism. If a derived object is accessed via a base class reference, the base class's version of the method is executed, not the derived version.
**Example:** `public new void Draw() { ... }`
**Reference:** [new modifier](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/new-modifier)

### 51. What is an Event in C#?
**Answer:** 
**The Core Concept:**
Events are a mechanism for a class to notify other classes when something of interest happens.

**Key Details:**
- They are built on top of delegates. The publisher raises the event, and subscribers handle it. The `event` keyword adds a layer of protection preventing outside classes from clearing the invocation list.
**Example:** `public event EventHandler ProcessCompleted;`
**Reference:** [Events](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/events/)

### 52. What is `Action` and `Func`?
**Answer:** 
**The Core Concept:**
They are built-in generic delegate types provided by the .NET BCL.

**Key Details:**
- `Action` represents a method that does *not* return a value (`void`). It can take up to 16 parameters.
- `Func` represents a method that *does* return a value. The last generic type parameter specifies the return type.
**Example:** `Func<int, int, bool> isGreater = (a, b) => a > b;`
**Reference:** [Func Delegate](https://learn.microsoft.com/en-us/dotnet/api/system.func-1)

### 53. What is a Predicate?
**Answer:** 
**The Core Concept:**
A built-in delegate that represents a method that defines a set of criteria and determines whether the specified object meets those criteria.

**Key Details:**
- It is functionally equivalent to `Func<T, bool>`, but often used in older BCL methods like `List<T>.FindAll()`.
**Example:** `Predicate<int> isEven = x => x % 2 == 0;`
**Reference:** [Predicate Delegate](https://learn.microsoft.com/en-us/dotnet/api/system.predicate-1)

### 54. What are Lambda Expressions?
**Answer:** 
**The Core Concept:**
An anonymous function used to create delegates or expression tree types inline.

**Key Details:**
- Introduced in C# 3.0, they use the `=>` operator (goes to). They are heavily used in LINQ for writing concise, functional-style code.
**Example:** `users.Where(u => u.Age > 18);`
**Reference:** [Lambda expressions](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions)

### 55. What is the difference between `Any()` and `Count()` in LINQ?
**Answer:** 
**The Core Concept:**
Both evaluate collections, but with vast performance differences when checking for existence.

**Key Details:**
- `Any()` returns `true` immediately upon finding the *first* matching element.
- `Count()` iterates through the *entire* collection to calculate the total number of items, which is incredibly wasteful if you only want to know if the collection is empty.
**Example:** Avoid `if (list.Count() > 0)`. Use `if (list.Any())`.
**Reference:** [Enumerable.Any](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.any)

### 56. What is Deferred Execution in LINQ?
**Answer:** 
**The Core Concept:**
The evaluation of a LINQ query is delayed until its realized value is actually required.

**Key Details:**
- Defining a query using `Where` or `Select` does not execute it. It is executed only when iterated over in a `foreach` loop or when a method like `ToList()`, `ToArray()`, or `Count()` is called.
**Example:** Query parameters can be changed before calling `ToList()`.
**Reference:** [Deferred Execution](https://learn.microsoft.com/en-us/dotnet/standard/linq/deferred-execution)

### 57. What is `IQueryable` vs `IList`?
**Answer:** 
**The Core Concept:**
`IList` holds data in memory, while `IQueryable` builds queries to be executed on a server.

**Key Details:**
- If you use `Where()` on an `IList` connected to EF, EF pulls the entire table into memory and filters locally.
- If you use `Where()` on an `IQueryable`, EF translates the filter into a SQL `WHERE` clause, executing the filter efficiently on the database server.
**Example:** `IQueryable<User> users = context.Users;`
**Reference:** [IQueryable](https://learn.microsoft.com/en-us/dotnet/api/system.linq.iqueryable)

### 58. Explain the `lock` statement vs `Mutex`.
**Answer:** 
**The Core Concept:**
Both are used for thread synchronization to prevent race conditions.

**Key Details:**
- `lock` is a lightweight construct that only synchronizes threads within the same application process.
- `Mutex` (Mutual Exclusion) is an OS-level construct that can synchronize threads *across different processes* (e.g., preventing an application from opening twice).
**Example:** `bool isNew; using(var mutex = new Mutex(true, "AppMutex", out isNew))`
**Reference:** [Mutexes](https://learn.microsoft.com/en-us/dotnet/standard/threading/mutexes)

### 59. What is the `ThreadLocal<T>` class?
**Answer:** 
**The Core Concept:**
It provides thread-local storage of data.

**Key Details:**
- It ensures that every thread accessing the variable has its own independent copy of the data, completely eliminating the need for `lock` statements for thread safety.
**Example:** `ThreadLocal<int> _threadCounter = new ThreadLocal<int>(() => 0);`
**Reference:** [ThreadLocal](https://learn.microsoft.com/en-us/dotnet/api/system.threading.threadlocal-1)

### 60. What is `Task.WhenAll` vs `Task.WaitAll`?
**Answer:** 
**The Core Concept:**
Both wait for multiple Tasks to complete.

**Key Details:**
- `Task.WhenAll` is non-blocking (asynchronous). It returns a new Task that completes when all passed tasks complete, allowing the calling thread to await it and remain responsive.
- `Task.WaitAll` is blocking (synchronous). It halts the executing thread completely until the tasks finish, potentially causing deadlocks in UI or ASP.NET applications.
**Example:** `await Task.WhenAll(task1, task2);`
**Reference:** [Task.WhenAll](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)

### 61. How does `ConfigureAwait(false)` work?
**Answer:** 
**The Core Concept:**
It configures an awaiter used to await a Task.

**Key Details:**
- By default (`true`), `await` captures the current SynchronizationContext (like the UI thread) and forces the continuation of the method back onto that thread.
- Passing `false` tells the runtime that the continuation does not need to resume on the original context, allowing it to run on any ThreadPool thread, preventing deadlocks and improving performance in class libraries.
**Example:** `await httpClient.GetAsync(url).ConfigureAwait(false);`
**Reference:** [ConfigureAwait](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.configureawait)

### 62. What is an Extension Method resolution order?
**Answer:** 
**The Core Concept:**
How the compiler decides between an instance method and an extension method.

**Key Details:**
- If a class has an instance method with the same name and signature as an extension method, the instance method ALWAYS takes precedence. The extension method is completely ignored.
**Example:** N/A
**Reference:** [Extension Methods](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/extension-methods)

### 63. What is Reflection Emit?
**Answer:** 
**The Core Concept:**
An advanced feature of the `System.Reflection.Emit` namespace.

**Key Details:**
- While Reflection allows you to *inspect* types at runtime, Reflection Emit allows you to *generate* IL code dynamically at runtime, creating entirely new types, assemblies, and methods on the fly. Heavy used by ORMs (like EF Core) and mocking frameworks (like Moq).
**Example:** Using `ILGenerator` to emit Opcodes.
**Reference:** [Emitting Dynamic Methods](https://learn.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/emitting-dynamic-methods-and-assemblies)

### 64. What is a Record in C# 9+?
**Answer:** 
**The Core Concept:**
A `record` is a reference type that provides built-in functionality for encapsulating data with value-based equality.

**Key Details:**
- Unlike classes (which use reference equality), two records are equal if their *properties* have the same values. They are inherently immutable and support non-destructive mutation via the `with` expression.
**Example:** `public record Person(string FirstName, string LastName);`
**Reference:** [Records](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/records)

### 65. What is the `with` expression?
**Answer:** 
**The Core Concept:**
Used primarily with `record` types for non-destructive mutation.

**Key Details:**
- Because records are immutable, you cannot change their properties. The `with` expression creates a clone of the record, copying all properties and modifying only the specific properties you provide.
**Example:** `var olderPerson = person with { Age = person.Age + 1 };`
**Reference:** [with expression](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/with-expression)

### 66. Explain Pattern Matching in C#.
**Answer:** 
**The Core Concept:**
A feature that tests whether an expression has a certain characteristic and, if so, extracts data into local variables.

**Key Details:**
- Modern C# allows incredibly expressive `switch` statements, type testing (`is Type t`), and relational patterns (`> 10 => "High"`), removing the need for sprawling `if-else` chains.
**Example:** `if (obj is string s) { Console.WriteLine(s.Length); }`
**Reference:** [Pattern matching](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/functional/pattern-matching)

### 67. What are Local Functions?
**Answer:** 
**The Core Concept:**
Private methods of a type that are nested in another member.

**Key Details:**
- They can only be called from their containing member. They are more efficient than lambdas/delegates because they do not require instantiation of a delegate object on the heap, reducing GC pressure.
**Example:** `int Add(int a, int b) { return a + b; }` defined inside another method.
**Reference:** [Local functions](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/local-functions)

### 68. What is the difference between `String.Empty` and `""`?
**Answer:** 
**The Core Concept:**
They are functionally identical.

**Key Details:**
- In the past (CLR 1.0), `""` created a new object while `String.Empty` did not. Today, string interning ensures both point to the exact same memory location. `String.Empty` is preferred purely for readability.
**Example:** `if (str == string.Empty)`
**Reference:** [String.Empty](https://learn.microsoft.com/en-us/dotnet/api/system.string.empty)

### 69. What is String Interning?
**Answer:** 
**The Core Concept:**
A mechanism the CLR uses to optimize string memory usage.

**Key Details:**
- Because strings are immutable, the CLR maintains an "intern pool". If you create multiple string variables with the literal value "Hello", the CLR does not allocate separate memory blocks. They all point to the single "Hello" reference in the pool.
**Example:** `object.ReferenceEquals("A", "A") // Returns true`
**Reference:** [String.Intern](https://learn.microsoft.com/en-us/dotnet/api/system.string.intern)

### 70. What is `IComparable` vs `IComparer`?
**Answer:** 
**The Core Concept:**
Interfaces used for sorting objects.

**Key Details:**
- `IComparable` is implemented *on* the class being sorted (e.g., `User` implements it). It defines the *default* sort order via `CompareTo()`.
- `IComparer` is implemented on a *separate* class to define custom, secondary sorting logic (e.g., `SortByAgeComparer`) via `Compare()`.
**Example:** `Array.Sort(users, new SortByAgeComparer());`
**Reference:** [IComparable Interface](https://learn.microsoft.com/en-us/dotnet/api/system.icomparable)

### 71. What is the `volatile` modifier in threading?
**Answer:** 
**The Core Concept:**
The `volatile` keyword indicates that a field might be modified by multiple threads executing simultaneously.

**Key Details:**
- It prevents the compiler/JIT from optimizing read/write access to that field (such as caching the value in a CPU register), forcing every read to fetch the latest value directly from main memory.
**Example:** `private volatile bool _shouldStop;`
**Reference:** [volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)

### 72. What are Covariance and Contravariance?
**Answer:** 
**The Core Concept:**
They describe how generic type parameters allow implicit reference conversion of collections.

**Key Details:**
- **Covariance (`out`):** Preserves assignment compatibility. You can assign `IEnumerable<Derived>` to `IEnumerable<Base>`. (Think "returning data").
- **Contravariance (`in`):** Reverses assignment compatibility. You can assign `Action<Base>` to `Action<Derived>`. (Think "consuming data").
**Example:** `IEnumerable<out T>`
**Reference:** [Covariance and Contravariance](https://learn.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance)

### 73. What is the difference between late binding and early binding?
**Answer:** 
**The Core Concept:**
Relates to when the compiler resolves method calls.

**Key Details:**
- **Early Binding (Compile-time):** The compiler knows the exact type and methods at compile time. Better performance, type safety, and IDE support.
- **Late Binding (Runtime):** Using Reflection or `dynamic`, the method call is resolved at runtime. Slower, but allows interacting with unknown types or COM objects.
**Example:** `obj.DoWork()` (Early) vs `type.GetMethod("DoWork").Invoke(obj)` (Late).
**Reference:** [Early and Late Binding](https://learn.microsoft.com/en-us/dotnet/visual-basic/programming-guide/language-features/early-late-binding/)

### 74. What is an Anonymous Type?
**Answer:** 
**The Core Concept:**
A convenient way to encapsulate a set of read-only properties into a single object without explicitly defining a type first.

**Key Details:**
- The type name is generated by the compiler and cannot be referenced in source code. Used extensively in LINQ projections (`Select`).
**Example:** `var person = new { Name = "John", Age = 30 };`
**Reference:** [Anonymous Types](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

### 75. Explain the `IDisposable` pattern.
**Answer:** 
**The Core Concept:**
The standard way to release unmanaged resources deterministically.

**Key Details:**
- Implements the `Dispose()` method. A proper pattern suppresses finalization (`GC.SuppressFinalize(this)`) to prevent the garbage collector from wasting time finalizing an object that has already been cleaned up.
**Example:** `public void Dispose() { Dispose(true); GC.SuppressFinalize(this); }`
**Reference:** [Dispose Pattern](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose)

### 76. What is the difference between `Array.CopyTo()` and `Array.Clone()`?
**Answer:** 
**The Core Concept:**
Both copy array data, but handle instantiation differently.

**Key Details:**
- `Clone()` creates a brand new array object containing a shallow copy of the elements. It returns an `object` that must be cast.
- `CopyTo()` requires an already existing, pre-allocated destination array and copies the elements into it starting at a specific index.
**Example:** `int[] arr2 = (int[])arr1.Clone();`
**Reference:** [Array.Clone Method](https://learn.microsoft.com/en-us/dotnet/api/system.array.clone)

### 77. What is `SemaphoreSlim`?
**Answer:** 
**The Core Concept:**
A lightweight synchronization primitive that limits the number of threads that can access a resource concurrently.

**Key Details:**
- Unlike `lock` which allows 1 thread, a Semaphore allows N threads. `SemaphoreSlim` is optimized for execution within a single app, and uniquely supports `async/await` (`WaitAsync()`).
**Example:** `await _semaphore.WaitAsync(); try { ... } finally { _semaphore.Release(); }`
**Reference:** [SemaphoreSlim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)

### 78. What is a Deadlock and how do you prevent it in C#?
**Answer:** 
**The Core Concept:**
A situation where two or more threads are blocked forever, waiting for each other to release a lock.

**Key Details:**
- Prevention strategies include: avoiding nested locks, always acquiring locks in a consistent order, using timeout mechanisms (`Monitor.TryEnter`), and avoiding `.Result` or `.Wait()` on Tasks on the UI thread.
**Example:** Thread 1 locks A, waits for B. Thread 2 locks B, waits for A.
**Reference:** [Deadlocks](https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives)

### 79. What is a Memory Leak in C#?
**Answer:** 
**The Core Concept:**
When memory is allocated but never released, despite the application no longer needing it.

**Key Details:**
- Since C# has a GC, true memory leaks are rare. "Logical leaks" happen when developers keep objects alive via static references, event handler subscriptions (forgetting to unsubscribe `-=`), or unclosed unmanaged resources (forgetting `Dispose()`).
**Example:** Subscribing to a static event and destroying the local object.
**Reference:** [Memory Leaks](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-memory-leak)

### 80. How do you find a Memory Leak in a .NET Application?
**Answer:** 
**The Core Concept:**
Using diagnostics tools to analyze the managed heap.

**Key Details:**
- Use tools like Visual Studio Diagnostic Tools, dotMemory, or `dotnet-dump`. Take a snapshot of memory, run the application, take another snapshot, and compare them to see which objects are surviving GC collections and who holds their "GC Root" reference.
**Example:** Analyzing GC Roots to find an un-detached event handler.
**Reference:** [Debug memory leaks](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-memory-leak)

### 81. Explain what `Span<T>` and `Memory<T>` are.
**Answer:** 
**The Core Concept:**
Modern C# types introduced for high-performance memory manipulation without allocations.

**Key Details:**
- They provide a type-safe window into a contiguous region of memory (like an array or unmanaged memory). By slicing a `Span`, you avoid allocating new array copies on the heap, massively reducing GC pressure.
**Example:** `ReadOnlySpan<char> slice = myString.AsSpan().Slice(0, 5);`
**Reference:** [Span<T> Struct](https://learn.microsoft.com/en-us/dotnet/api/system.span-1)

### 82. What is `stackalloc`?
**Answer:** 
**The Core Concept:**
A keyword used in an unsafe context to allocate memory on the stack rather than the heap.

**Key Details:**
- Allocating on the stack is almost instantaneous and avoids Garbage Collection entirely. Modern C# allows using `stackalloc` safely with `Span<T>` without the `unsafe` keyword.
**Example:** `Span<byte> buffer = stackalloc byte[100];`
**Reference:** [stackalloc](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/stackalloc)

### 83. What is the difference between `Task.Run` and `Task.Factory.StartNew`?
**Answer:** 
**The Core Concept:**
Methods to queue work to the ThreadPool.

**Key Details:**
- `Task.Run` was introduced in .NET 4.5 as a safer, simpler wrapper around `Task.Factory.StartNew`.
- `StartNew` has dangerous default behaviors regarding how it handles async delegates (it returns a `Task<Task>` requiring `.Unwrap()`). You should exclusively use `Task.Run`.
**Example:** `Task.Run(() => DoWork());`
**Reference:** [Task.Run vs Task.Factory.StartNew](https://devblogs.microsoft.com/pfxteam/task-run-vs-task-factory-startnew/)

### 84. Explain the difference between `AsEnumerable()` and `AsQueryable()`.
**Answer:** 
**The Core Concept:**
Both transition the execution model of a LINQ query.

**Key Details:**
- `AsEnumerable()` forces the rest of the query to execute in-memory via LINQ to Objects. Useful to switch from DB-execution to memory-execution when using a C# method EF doesn't understand.
- `AsQueryable()` converts an in-memory collection into an `IQueryable`. Useful for mocking database contexts in unit tests.
**Example:** `query.AsEnumerable().Select(x => MyCustomCsharpFunction(x))`
**Reference:** [AsEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.asenumerable)

### 85. What are Default Interface Methods?
**Answer:** 
**The Core Concept:**
Introduced in C# 8, interfaces can now provide a default implementation for a method.

**Key Details:**
- This was added primarily to allow API authors to add new methods to an existing interface without breaking all the classes that currently implement that interface.
**Example:** `public interface ILogger { void LogError(string e) { Console.WriteLine(e); } }`
**Reference:** [Default interface methods](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-8.0/default-interface-methods)

### 86. What is the `in` parameter modifier?
**Answer:** 
**The Core Concept:**
It passes an argument by reference, but guarantees it is read-only.

**Key Details:**
- Used heavily in high-performance computing. Passing large structs by value copies massive amounts of memory. Passing them via `in` passes a tiny memory pointer, but unlike `ref`, the compiler prevents the method from mutating the struct.
**Example:** `public void Process(in LargeStruct data)`
**Reference:** [in parameter modifier](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/in-parameter-modifier)

### 87. What are Source Generators?
**Answer:** 
**The Core Concept:**
A compiler feature introduced in C# 9 that lets developers write code that generates more C# code during compilation.

**Key Details:**
- Unlike Reflection (which is slow and happens at runtime), Source Generators inspect the code during the build step and emit highly optimized code files dynamically. Used heavily in modern .NET for JSON serialization and DI without Reflection overhead.
**Example:** The `System.Text.Json` source generator.
**Reference:** [Source Generators](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview)

### 88. Explain string interpolation vs `String.Format`.
**Answer:** 
**The Core Concept:**
Both construct dynamic strings.

**Key Details:**
- `String.Format` relies on positional arguments (`{0}`, `{1}`).
- String Interpolation (the `$` symbol) embeds variables directly (`{name}`). At compile time, interpolation is literally converted into `String.Format` or `String.Concat` calls, making them identical in performance but interpolation vastly superior in readability.
**Example:** `$"Hello {userName}"`
**Reference:** [String interpolation](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated)

### 89. What is a DTO (Data Transfer Object)?
**Answer:** 
**The Core Concept:**
An object used to carry data between processes to reduce the number of method calls.

**Key Details:**
- In ASP.NET, you never return your raw Database Entity classes directly to the client via an API. You map the Entity to a DTO containing only the properties the client needs. This prevents over-posting attacks and circular reference JSON errors.
**Example:** Mapping `User` to `UserDto` using AutoMapper.
**Reference:** [DTO Pattern](https://learn.microsoft.com/en-us/aspnet/web-api/overview/data/using-web-api-with-entity-framework/part-5)

### 90. Explain Boxing/Unboxing performance implications.
**Answer:** 
**The Core Concept:**
Converting a value type to a reference type (and back).

**Key Details:**
- When boxing occurs, the CLR must allocate a new object on the heap, copy the value from the stack to the heap, and create a reference. This creates massive memory allocations and GC pressure if done inside loops. Always use Generics (`List<int>`) to avoid it.
**Example:** `ArrayList` boxes integers, `List<int>` does not.
**Reference:** [Boxing/Unboxing Performance](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/types/boxing-and-unboxing)

### 91. What is the difference between `System.DateTime` and `System.DateTimeOffset`?
**Answer:** 
**The Core Concept:**
Both store dates and times, but handle time zones differently.

**Key Details:**
- `DateTime` only stores the date and time. It doesn't know *where* in the world it is, leading to daylight saving time bugs.
- `DateTimeOffset` stores the date, time, AND the offset from UTC. This is the Microsoft recommended standard for almost all database and API interactions.
**Example:** `DateTimeOffset.UtcNow`
**Reference:** [DateTime vs DateTimeOffset](https://learn.microsoft.com/en-us/dotnet/standard/datetime/choosing-between-datetime)

### 92. What is the `TaskCompletionSource<T>` class?
**Answer:** 
**The Core Concept:**
It allows you to create a `Task<T>` manually and control its state (Completed, Faulted, Canceled).

**Key Details:**
- Used heavily when wrapping legacy event-based asynchronous patterns (EAP) or old callback APIs into modern `async/await` compatible tasks.
**Example:** Setting `tcs.SetResult(true)` inside an event handler.
**Reference:** [TaskCompletionSource](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcompletionsource-1)

### 93. What is the `volatile` modifier vs `Interlocked` operations?
**Answer:** 
**The Core Concept:**
Both handle thread safety without locks.

**Key Details:**
- `volatile` only ensures the most up-to-date value is read from memory. It does NOT make operations atomic. (e.g., `counter++` is still thread-unsafe).
- `Interlocked` provides atomic operations (read, add, write in a single CPU instruction) ensuring absolute thread-safety for integer operations without locks.
**Example:** `Interlocked.Increment(ref _counter);`
**Reference:** [Interlocked Class](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)

### 94. What is a Closure in C#?
**Answer:** 
**The Core Concept:**
A closure occurs when a lambda expression or anonymous method references a variable defined outside its scope.

**Key Details:**
- The compiler creates a hidden class to hold the captured variable, meaning its lifetime is extended until the lambda is garbage collected. Capturing loop variables incorrectly in old C# versions led to the infamous "modified closure" bug.
**Example:** `int x = 5; Action a = () => Console.Write(x);`
**Reference:** [Closures](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions#capture-of-outer-variables-and-variable-scope-in-lambda-expressions)

### 95. Explain the `IDisposable` pattern with a Finalizer.
**Answer:** 
**The Core Concept:**
The full pattern used to clean up unmanaged resources (file handles, network sockets).

**Key Details:**
- The `Dispose(bool disposing)` method contains the logic.
- If called from `Dispose()` (disposing = true), it cleans up both managed and unmanaged resources.
- If called from the Finalizer (disposing = false), it cleans up ONLY unmanaged resources (because managed objects might have already been garbage collected).
**Example:** The official MS Dispose Pattern implementation.
**Reference:** [Dispose Pattern](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose)

### 96. What is the difference between `System.Array` and `System.Collections.Generic.List<T>`?
**Answer:** 
**The Core Concept:**
Array is a fixed-size contiguous block of memory. List is a dynamic wrapper around an Array.

**Key Details:**
- When a `List<T>` reaches its capacity, it allocates a new, larger internal array on the heap, copies the old elements over, and discards the old array.
- Pre-sizing a List (`new List<int>(1000)`) avoids this expensive reallocation overhead.
**Example:** `List.Capacity` vs `List.Count`.
**Reference:** [List Class](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1)

### 97. What is `lock(this)` or `lock(typeof(MyClass))` and why is it bad?
**Answer:** 
**The Core Concept:**
Locking on publicly accessible objects.

**Key Details:**
- If you lock on `this`, any external code that has a reference to your object could also lock on it, causing a massive, impossible-to-debug deadlock.
- The absolute rule of thread safety is to lock on a private, dedicated `object`.
**Example:** `private readonly object _syncRoot = new object();`
**Reference:** [lock statement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

### 98. What is `Task.Yield()`?
**Answer:** 
**The Core Concept:**
An asynchronous method that forces the current method to yield execution back to the caller immediately.

**Key Details:**
- It is used to force a method to complete asynchronously, even if it could run synchronously. Often used in UI applications to keep the UI thread responsive when entering a massive calculation loop.
**Example:** `await Task.Yield();`
**Reference:** [Task.Yield](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.yield)

### 99. What are Records and Positional Syntax?
**Answer:** 
**The Core Concept:**
A concise way to declare a record and its properties in one line.

**Key Details:**
- Using `public record Person(string Name, int Age);` automatically generates the constructor, read-only init properties, and a deconstructor behind the scenes.
**Example:** `var (name, age) = person;` (Deconstructing)
**Reference:** [Positional syntax for property definition](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/records#positional-syntax-for-property-definition)

### 100. What is the `ConfigureAwait` analyzer (CA2007) and why is it important for libraries?
**Answer:** 
**The Core Concept:**
A Roslyn analyzer rule enforcing the use of `ConfigureAwait(false)` in class libraries.

**Key Details:**
- If an open-source NuGet package awaits tasks without it, and a consumer uses that package in a WinForms/WPF app with blocking code, the entire app will deadlock. Library authors must use it; application authors (ASP.NET Core) generally don't need it.
**Example:** `await File.ReadAllTextAsync().ConfigureAwait(false);`
**Reference:** [CA2007](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2007)
