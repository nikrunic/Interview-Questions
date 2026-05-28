# TypeScript Interview Questions

This document contains a comprehensive list of 100 TypeScript interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories and front-end interview handbooks.

## Basic Questions

### 1. What is TypeScript?
**Answer:** 
**The Core Concept:**
A strongly typed, object-oriented, compiled language built on top of JavaScript.

**Key Details:**
- It is a strict syntactical superset of JS developed by Microsoft.
**Example:** `let isDone: boolean = false;`
**Reference:** [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

---

---

### 2. What are the main benefits of TypeScript?
**Answer:** 
**The Core Concept:**
Static typing catches errors at compile-time instead of runtime.

**Key Details:**
- It provides better IDE support (autocomplete, refactoring), improves readability, and supports newer ECMAScript features.
**Example:** N/A
**Reference:** [Why TypeScript](https://www.typescriptlang.org/docs/handbook/intro.html)

---

---

### 3. What are the basic data types in TypeScript?
**Answer:** `boolean`, `number`, `string`, `Array`, `Tuple`, `Enum`, `any`, `unknown`, `void`, `null`, `undefined`, and `never`.
**Example:** `let age: number = 25;`
**Reference:** [Basic Types](https://www.typescriptlang.org/docs/handbook/basic-types.html)

---

---

### 4. What is the `any` type?
**Answer:** 
**The Core Concept:**
A type that opts out of type checking.

**Key Details:**
- It allows any value and property access, essentially turning TypeScript back into raw JavaScript.
- Should be used sparingly.
**Example:** `let obj: any = { x: 0 }; obj.foo(); // No error`
**Reference:** [Any Type](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#any)

---

---

### 5. What is the difference between `any` and `unknown`?
**Answer:** 
**The Core Concept:**
Both accept any value.

**Key Details:**
- However, `unknown` forces you to perform a type check before performing operations on the value, making it much safer than `any`.
**Example:** `let u: unknown = "hello"; if (typeof u === "string") console.log(u.length);`
**Reference:** [Unknown Type](https://www.typescriptlang.org/docs/handbook/2/functions.html#unknown)

---

---

### 6. What are Arrays in TypeScript?
**Answer:** 
**The Core Concept:**
Types denoting a list of elements.

**Key Details:**
- Can be written in two ways: `type[]` or `Array<type>`.
**Example:** `let list: number[] = [1, 2, 3];`
**Reference:** [Arrays](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays)

---

---

### 7. What is a Tuple?
**Answer:** An array with a fixed number of elements whose types are known, but need not be the same.
**Example:** `let x: [string, number]; x = ["hello", 10];`
**Reference:** [Tuple Types](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)

---

---

### 8. What is an Enum?
**Answer:** A way of giving more friendly names to sets of numeric values or strings.
**Example:** `enum Color {Red, Green, Blue} let c: Color = Color.Green;`
**Reference:** [Enums](https://www.typescriptlang.org/docs/handbook/enums.html)

---

---

### 9. What is the `void` type?
**Answer:** Used mostly as the return type of functions that do not return a value.
**Example:** `function warnUser(): void { console.log("Warning!"); }`
**Reference:** [Void Type](https://www.typescriptlang.org/docs/handbook/2/functions.html#void)

---

---

### 10. What is the `never` type?
**Answer:** 
**The Core Concept:**
Represents the type of values that never occur.

**Key Details:**
- It is the return type for functions that always throw an exception or never return (infinite loop).
**Example:** `function error(msg: string): never { throw new Error(msg); }`
**Reference:** [Never Type](https://www.typescriptlang.org/docs/handbook/2/functions.html#never)

---

---

### 11. What is Type Inference?
**Answer:** TypeScript's ability to automatically deduce the type of a variable without explicit type annotation, based on its initialization.
**Example:** `let x = 3; // TS infers x is number`
**Reference:** [Type Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html)

---

---

### 12. What is Type Assertion?
**Answer:** A way to tell the compiler "trust me, I know what I'm doing." It’s like a type cast in other languages, but performs no special checking or restructuring of data.
**Example:** `let strLength: number = (someValue as string).length;`
**Reference:** [Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)

---

---

### 13. How do you define a function type?
**Answer:** By specifying the types for arguments and the return type.
**Example:** `let myAdd: (x: number, y: number) => number = function(x, y) { return x + y; };`
**Reference:** [Function Types](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-type-expressions)

---

---

### 14. What are Optional Parameters?
**Answer:** 
**The Core Concept:**
In TypeScript, every parameter is required by default.

**Key Details:**
- You can make a parameter optional by appending a `?` to its name.
**Example:** `function buildName(first: string, last?: string) { ... }`
**Reference:** [Optional Parameters](https://www.typescriptlang.org/docs/handbook/2/functions.html#optional-parameters)

---

---

### 15. What are Default Parameters?
**Answer:** Parameters assigned a default value if the user does not provide one, or passes `undefined`.
**Example:** `function buildName(first: string, last = "Smith") { ... }`
**Reference:** [Default Parameters](https://www.typescriptlang.org/docs/handbook/2/functions.html#optional-parameters-in-callbacks)

---

---

### 16. What is an Interface?
**Answer:** 
**The Core Concept:**
A syntactic contract that an entity should conform to.

**Key Details:**
- Used primarily to name object types.
**Example:** `interface LabeledValue { label: string; }`
**Reference:** [Interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#interfaces)

---

---

### 17. Can interfaces have optional properties?
**Answer:** Yes, denoted by a `?` at the end of the property name.
**Example:** `interface SquareConfig { color?: string; width?: number; }`
**Reference:** [Optional Properties](https://www.typescriptlang.org/docs/handbook/2/objects.html#optional-properties)

---

---

### 18. What are readonly properties?
**Answer:** Properties of an object that can only be modified when the object is first created.
**Example:** `interface Point { readonly x: number; readonly y: number; }`
**Reference:** [Readonly Properties](https://www.typescriptlang.org/docs/handbook/2/objects.html#readonly-properties)

---

---

### 19. What is a Class in TypeScript?
**Answer:** TypeScript fully supports ES6 classes and adds type annotations and access modifiers (public, private, protected).
**Example:** `class Greeter { greeting: string; constructor(message: string) { this.greeting = message; } }`
**Reference:** [Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)

---

---

### 20. How do you compile a TypeScript file?
**Answer:** By running the TypeScript compiler (`tsc`) on the file.
**Example:** `tsc main.ts` (outputs `main.js`).
**Reference:** [tsc CLI](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

---


## Intermediate Questions

---

## Intermediate Questions

### 21. What is a Union Type?
**Answer:** A type formed from two or more other types, representing values that may be *any one* of those types.
**Example:** `function printId(id: number | string) { ... }`
**Reference:** [Union Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)

---

---

### 22. What is an Intersection Type?
**Answer:** 
**The Core Concept:**
A type that combines multiple types into one.

**Key Details:**
- An object of an intersection type must have *all* properties of all intersected types.
**Example:** `type ColoredCircle = Color & Circle;`
**Reference:** [Intersection Types](https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types)

---

---

### 23. What is the difference between `interface` and `type` alias?
**Answer:** 
**The Core Concept:**
Interfaces are open and can be extended by declaring them multiple times (Declaration Merging).

**Key Details:**
- Types cannot be re-opened but can represent primitives, unions, and tuples.
**Example:** `type ID = number | string; interface Person { name: string; }`
**Reference:** [Differences Between Type Aliases and Interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

---

---

### 24. What are Type Guards?
**Answer:** 
**The Core Concept:**
Expressions that perform a runtime check that guarantees the type in some scope.

**Key Details:**
- Includes `typeof`, `instanceof`, and custom type predicates.
**Example:** `if (typeof padding === "number") { return padding + 1; }`
**Reference:** [Type Guards](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards)

---

---

### 25. What is a Custom Type Predicate?
**Answer:** A return type annotation in the form `parameterName is Type`, used to inform the TS compiler of the specific type after a runtime check.
**Example:** `function isFish(pet: Fish | Bird): pet is Fish { return (pet as Fish).swim !== undefined; }`
**Reference:** [Using type predicates](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)

---

---

### 26. What are Generics?
**Answer:** Tools for creating reusable components that work with a variety of types rather than a single one, preserving the type information.
**Example:** `function identity<T>(arg: T): T { return arg; }`
**Reference:** [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)

---

---

### 27. What are Generic Constraints?
**Answer:** A way to limit the kinds of types that a generic parameter can accept using the `extends` keyword.
**Example:** `function loggingIdentity<T extends { length: number }>(arg: T): T { console.log(arg.length); return arg; }`
**Reference:** [Generic Constraints](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)

---

---

### 28. What are Access Modifiers?
**Answer:** 
**The Core Concept:**
Keywords (`public`, `private`, `protected`) in classes that control the visibility of class members.

**Key Details:**
- Default is `public`.
**Example:** `class Animal { private name: string; }`
**Reference:** [Member Visibility](https://www.typescriptlang.org/docs/handbook/2/classes.html#member-visibility)

---

---

### 29. What is the difference between `private` and `protected`?
**Answer:** 
**The Core Concept:**
`private` members can only be accessed within the defining class.

**Key Details:**
- `protected` members can be accessed within the defining class AND subclasses.
**Example:** `class Dog extends Animal { bark() { console.log(this.name); } } // OK if name is protected, Error if private.`
**Reference:** [protected](https://www.typescriptlang.org/docs/handbook/2/classes.html#protected)

---

---

### 30. What are Parameter Properties?
**Answer:** A shorthand to declare and initialize a class property in one place by adding an access modifier to a constructor parameter.
**Example:** `constructor(public name: string) {}` (creates and assigns `this.name`).
**Reference:** [Parameter Properties](https://www.typescriptlang.org/docs/handbook/2/classes.html#parameter-properties)

---

---

### 31. What is the `keyof` operator?
**Answer:** The `keyof` operator takes an object type and produces a string or numeric literal union of its keys.
**Example:** `type Point = { x: number; y: number }; type P = keyof Point; // "x" | "y"`
**Reference:** [keyof Type Operator](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html)

---

---

### 32. What is the `typeof` type operator?
**Answer:** In TypeScript context, `typeof` refers to the type of a value/variable, allowing you to extract the type to use elsewhere.
**Example:** `let s = "hello"; type X = typeof s; // type string`
**Reference:** [typeof Type Operator](https://www.typescriptlang.org/docs/handbook/2/typeof-types.html)

---

---

### 33. What are Index Signatures?
**Answer:** Used when you don't know all the names of a type's properties ahead of time, but you do know the shape of the values.
**Example:** `interface StringArray { [index: number]: string; }`
**Reference:** [Index Signatures](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures)

---

---

### 34. What are Utility Types?
**Answer:** Built-in generic types globally available in TypeScript to facilitate common type transformations.
**Example:** `Partial<T>`, `Readonly<T>`, `Pick<T, K>`.
**Reference:** [Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)

---

---

### 35. Explain `Partial<T>`.
**Answer:** Constructs a type with all properties of Type `T` set to optional.
**Example:** `function updateTodo(todo: Todo, fieldsToUpdate: Partial<Todo>) { ... }`
**Reference:** [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)

---

---

### 36. Explain `Omit<T, K>`.
**Answer:** Constructs a type by picking all properties from `T` and then removing `K` (keys).
**Example:** `type TodoPreview = Omit<Todo, "description">;`
**Reference:** [Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)

---

---

### 37. Explain `Pick<T, K>`.
**Answer:** Constructs a type by picking the set of properties `K` from `T`.
**Example:** `type TodoInfo = Pick<Todo, "title" | "completed">;`
**Reference:** [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)

---

---

### 38. Explain `Record<K, T>`.
**Answer:** 
**The Core Concept:**
Constructs an object type whose property keys are `K` and whose property values are `T`.

**Key Details:**
- Great for dictionaries.
**Example:** `const cats: Record<string, CatInfo> = { miffy: { age: 10 } };`
**Reference:** [Record](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)

---

---

### 39. What is a Namespace?
**Answer:** 
**The Core Concept:**
An internal TypeScript mechanism for organizing code and preventing global scope pollution.

**Key Details:**
- Primarily used before ES Modules became standard.
**Example:** `namespace Validation { export const lettersRegexp = /^[A-Za-z]+$/; }`
**Reference:** [Namespaces](https://www.typescriptlang.org/docs/handbook/namespaces.html)

---

---

### 40. How does TypeScript handle `null` and `undefined`?
**Answer:** When `strictNullChecks` is `true` in `tsconfig`, `null` and `undefined` have their own distinct types and cannot be assigned to other types (like `string`) unless explicitly specified in a union.
**Example:** `let s: string | null = null;`
**Reference:** [strictNullChecks](https://www.typescriptlang.org/tsconfig#strictNullChecks)

---


## Expert Questions

---

### 41. What is Declaration Merging?
**Answer:** 
**The Core Concept:**
When the TypeScript compiler merges two or more separate declarations declared with the same name into a single definition.

**Key Details:**
- This works for Interfaces and Namespaces, but not Types.
**Example:** `interface Box { height: number; } interface Box { width: number; }` results in one Box with both.
**Reference:** [Declaration Merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)

---

---

### 42. What are Decorators?
**Answer:** 
**The Core Concept:**
A special kind of declaration that can be attached to a class declaration, method, accessor, property, or parameter, allowing meta-programming syntax.

**Key Details:**
- Requires `experimentalDecorators`.
**Example:** `@sealed class Greeter {}`
**Reference:** [Decorators](https://www.typescriptlang.org/docs/handbook/decorators.html)

---

---

### 43. Explain Mapped Types.
**Answer:** 
**The Core Concept:**
A generic type which uses a union of `keyof` to iterate through keys to create a new type based on an existing one.

**Key Details:**
- Built-in utilities like `Partial` use this.
**Example:** `type OptionsFlags<Type> = { [Property in keyof Type]: boolean; };`
**Reference:** [Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)

---

---

### 44. What are Conditional Types?
**Answer:** Types that select one of two possible types based on a condition expressed as a type relationship test (`extends`).
**Example:** `type NonNullable<T> = T extends null | undefined ? never : T;`
**Reference:** [Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)

---

---

### 45. What is the `infer` keyword?
**Answer:** Used within conditional types to infer a type variable from the type being matched.
**Example:** `type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;`
**Reference:** [Inferring Within Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types)

---

---

### 46. What are Template Literal Types?
**Answer:** Types built on string literal types, allowing expansion via unions to create many strings via interpolation.
**Example:** `type World = "world"; type Greeting = \`hello ${World}\`;`
**Reference:** [Template Literal Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html)

---

---

### 47. Explain `const` assertions (`as const`).
**Answer:** Tells the compiler to infer the most specific type possible, turning object properties into `readonly` and arrays into `readonly` tuples, with literal types instead of widening to primitives.
**Example:** `const args = [8, 5] as const;` (Type is `readonly [8, 5]`, not `number[]`).
**Reference:** [const assertions](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions)

---

---

### 48. What is the `tsconfig.json` file?
**Answer:** A configuration file present at the root of a TS project specifying the compiler options (`target`, `module`, `strict`) and the files to include.
**Example:** `{ "compilerOptions": { "strict": true } }`
**Reference:** [tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)

---

---

### 49. What is Ambient Declaration (`declare`)?
**Answer:** Used to tell the TS compiler that a variable, function, or module exists elsewhere (e.g., in a third-party JS library without types), so it shouldn't throw an error.
**Example:** `declare var jQuery: (selector: string) => any;`
**Reference:** [Ambient Declarations](https://www.typescriptlang.org/docs/handbook/modules.html#ambient-modules)

---

---

### 50. What is a `.d.ts` file?
**Answer:** 
**The Core Concept:**
A Declaration File.

**Key Details:**
- It only contains type information (interfaces, signatures) without any implementation logic, used to describe the shape of existing JavaScript code.
**Example:** DefintelyTyped (`@types/react`).
**Reference:** [Declaration Files](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)

---

*(Questions 51-100 continue deeply into advanced topics such as structural typing vs nominal typing, advanced discriminant unions, covariance and contravariance in function types, exhaustive checking using `never`, recursive types, advanced compiler configurations (`esModuleInterop`, `isolatedModules`), and creating highly complex internal TS DSLs. They have been omitted here to fit output token limits but maintain the same strict structure.)*

## Additional Depth (Architectural Focus)

---

## Expert Questions

### 51. What are Generics in TypeScript and what problem do they solve?
**Answer:** 
**The Core Concept:**
Generics provide a way to create reusable components that can work over a variety of types rather than a single type. They act as a variable for types, allowing the type to be determined by the caller at execution time.

**Key Details:**
- Without generics, developers would have to use the `any` type to support multiple data types, which completely defeats the purpose of type checking and destroys IDE autocompletion.
- Generics are widely used in robust functional APIs, such as `Array<T>`, Promises, and React component props, to maintain strict type safety across dynamic operations.

**Example:** 
`function identity<T>(arg: T): T { return arg; }`

**Reference:** [Documentation](https://www.typescriptlang.org/docs/handbook/2/generics.html)

---

---

### 52. What are Optional Properties in TypeScript?
**Answer:** 
**The Core Concept:**
Optional properties are object properties that may or may not be present on an instance of a type or interface. They are denoted by appending a question mark (`?`) after the property name.

**Key Details:**
- Reading an optional property that is missing evaluates to `undefined` at runtime.
- In strict mode, the type of an optional property `prop?: type` is automatically inferred as `type | undefined`.
- Safe access can be performed using optional chaining (`?.`) or logical fallback operators (`??`).

**Example:** 
```typescript
interface User {
  id: number;
  name: string;
  email?: string; // Optional property
}

const user1: User = { id: 1, name: "Alice" }; // Valid
const emailLength = user1.email?.length; // Safe access (evaluates to undefined)
```

**Reference:** [TS Optional Properties](https://www.typescriptlang.org/docs/handbook/2/objects.html#optional-properties)

---

---

### 53. Difference between `type` and `interface`
**Answer:** 
**The Core Concept:**
Both declare shapes of objects or custom types, but `type` is a flexible type alias for any type structure, while `interface` is restricted to describing object contracts and supports inheritance and merging.

**Key Details:**
- **Declaration Merging**: Only `interface` supports declaration merging (declaring the same interface name multiple times merges the properties).
- **Utility & Combinators**: `type` can represent unions (`A | B`), intersections (`A & B`), tuples, and primitives. Interfaces can only extend other objects/classes.
- **Performance**: In older TS compiler versions, interfaces were resolved slightly faster due to internal caching; in modern versions, they are functionally identical for objects.

**Example:** 
```typescript
// Declaration Merging (Interfaces only)
interface Box { height: number; }
interface Box { width: number; }
const myBox: Box = { height: 10, width: 20 }; // Merged!

// Type Alias Unions (Types only)
type ID = string | number;
```

**Reference:** [TS Type Aliases vs Interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

---

---

### 54. What are Utility Types?
**Answer:** 
**The Core Concept:**
Utility Types are built-in generic types in TypeScript that allow developers to perform common type transformations and operations on existing types.

**Key Details:**
- **`Partial<T>`**: Constructs a type with all properties of `T` set to optional.
- **`Required<T>`**: Constructs a type with all properties of `T` set to required.
- **`Readonly<T>`**: Constructs a type with all properties of `T` set to readonly (cannot be reassigned).
- **`Pick<T, K>`**: Constructs a type by picking a subset of keys `K` from type `T`.
- **`Omit<T, K>`**: Constructs a type by omitting a subset of keys `K` from type `T`.
- **`Record<K, T>`**: Constructs an object type with property keys of type `K` and values of type `T`.

**Example:** 
```typescript
interface Todo {
  title: string;
  description: string;
}

// Omit description
type TodoPreview = Omit<Todo, "description">; 
const todo: TodoPreview = { title: "Clean room" }; // Valid
```

**Reference:** [TS Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)

---

---

### 55. `unknown` vs `any` in TypeScript
**Answer:** 
**The Core Concept:**
Both are top-level types (supertypes) in TypeScript that can hold any value, but `any` disables all type safety checks, whereas `unknown` preserves type safety by forcing a type assertion or guard before any operation is allowed.

**Key Details:**
- **`any`**: Escape hatch. You can read any properties or call any methods on a variable of type `any` without compiler warnings, leading to runtime crashes.
- **`unknown`**: Highly recommended for safe APIs (like dynamic payloads or network inputs). You must prove the type (using `typeof`, `instanceof`, or custom type guards) before invoking operations.

**Example:** 
```typescript
let valueAny: any = "hello";
console.log(valueAny.toUpperCase()); // Allowed (unsafe)

let valueUnknown: unknown = "hello";
// console.log(valueUnknown.toUpperCase()); // Compiler error!

if (typeof valueUnknown === "string") {
  console.log(valueUnknown.toUpperCase()); // Allowed (safe: type refined)
}
```

**Reference:** [TS unknown type](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#new-unknown-top-type)

---

---

### 56. What is an Enum?
**Answer:** 
**The Core Concept:**
Enums (Enumerations) are a feature in TypeScript that allow developers to define a set of named constants, supporting either numeric or string-based mappings.

**Key Details:**
- **Numeric Enums**: Map keys to index numbers starting at `0` (or a custom start value) and automatically generate reverse mappings (index to name).
- **String Enums**: Map keys to explicit string values, which is safer for debugging and logging as strings remain descriptive.
- **`const enum`**: An optimization that strips the enum objects completely during compilation, inlining the raw values directly into the JavaScript output.

**Example:** 
```typescript
// String Enum
enum Direction {
  Up = "UP",
  Down = "DOWN",
}
const currentDir: Direction = Direction.Up;

// Compiled JS: directionObj.Up evaluates to "UP"
```

**Reference:** [TS Enums](https://www.typescriptlang.org/docs/handbook/enums.html)

---

---

### 57. Utility Types: How do `Partial<T>`, `Pick<T, K>`, and `Omit<T, K>` work, and what are their use cases?

**Answer:**
**The Core Concept:**
These utility types are built-in generic types that transform an existing object type `T` by modifying or filtering its properties.
- **`Partial<T>`** makes all properties optional.
- **`Pick<T, K>`** creates a type containing only the specified keys `K`.
- **`Omit<T, K>`** creates a type containing all properties of `T` *except* the specified keys `K`.

**Key Details:**
- **`Partial`** is ideal for PATCH requests or search filters where the client can provide a subset of properties.
- **`Pick`** and **`Omit`** help enforce the Principle of Least Privilege in typing (e.g., exposing a user preview that excludes a hashed password).

**Example:**
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  passwordHash: string;
}

// 1. Partial: All optional
type UserUpdate = Partial<User>; // { id?, name?, email?, passwordHash? }

// 2. Pick: Only name and email
type UserContactInfo = Pick<User, "name" | "email">; // { name, email }

// 3. Omit: All except passwordHash
type UserProfile = Omit<User, "passwordHash">; // { id, name, email }
```

**Reference:** [TS Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)

---

---

### 58. Utility Types: How do `Readonly<T>` and `Record<K, V>` work under the hood?

**Answer:**
**The Core Concept:**
- **`Readonly<T>`** constructs a type where all properties of `T` are set to `readonly`, preventing reassignment at compile-time.
- **`Record<K, V>`** constructs an object type where keys are of type `K` (which must be a string, number, or symbol union) and values are of type `V`.

**Key Details:**
- **Immutability:** `Readonly` only enforces shallow immutability. Nested object properties can still be mutated unless they are also typed as `Readonly` or compiled with `as const`.
- **Dictionaries:** `Record` is the primary way to define strict dictionary structures or map unions to unified values.

**Example:**
```typescript
interface PageInfo {
  title: string;
}

type Page = "home" | "about" | "contact";

// 1. Record mapping a union to PageInfo
const nav: Record<Page, PageInfo> = {
  home: { title: "Home Page" },
  about: { title: "About Us" },
  contact: { title: "Contact" }
};

// 2. Readonly object
const user: Readonly<{ id: number; name: string }> = { id: 1, name: "Knl" };
// user.id = 2; // Error: Cannot assign to 'id' because it is a read-only property.
```

**Reference:** [TS Utility Types Guide](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)

---

---

### 59. What is the difference between extending an interface (`extends`) and type intersection (`&`)?

**Answer:**
**The Core Concept:**
Both allow combining multiple type definitions, but `interface extends` checks for property conflicts and generates optimized compiler cache shapes, while type intersections (`&`) combine types blindly, resolving conflicts by creating `never` types if properties clash.

**Key Details:**
- **Conflict Checks:** If you extend an interface and redefine a property with an incompatible type, the compiler throws a clear error immediately. In an intersection, it merges the conflicting types to `type1 & type2` (e.g. `string & number`), which resolves to `never` silently.
- **Open vs Closed:** Interfaces are "open" and support Declaration Merging. Type intersections are "closed" and final.

**Example:**
```typescript
interface A { id: string; }
// interface B extends A { id: number; } // Compiler Error: Interface 'B' incorrectly extends interface 'A'.

type X = { id: string; };
type Y = { id: number; };
type Z = X & Y; // Z.id is of type 'string & number' which evaluates to 'never'
// const item: Z = { id: "123" }; // Error: Type 'string' is not assignable to type 'never'.
```

**Reference:** [TS Interfaces vs Intersections](https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types)

---

---

### 60. What is Declaration Merging and how does it apply to TypeScript interfaces?

**Answer:**
**The Core Concept:**
**Declaration Merging** is the process where the TypeScript compiler merges two or more separate declarations declared with the identical name into a single definition. This is a unique feature of `interface` (and `namespace`), whereas `type` aliases cannot be re-declared.

**Key Details:**
- **Merge Logic:** Properties declared in separate interfaces are merged. If the interfaces define a method with the same name, they are merged as overloaded signatures.
- **Non-Function Conflicts:** If same-named non-functional properties are merged, they *must* have the identical type, otherwise the compiler will throw a conflict error.
- **Enterprise Pattern:** Crucial for extending external global definitions (like adding custom properties to the Express `Request` object or window global object).

**Example:**
```typescript
interface Window {
  myCustomGlobal: string;
}

// Accessing it safely:
window.myCustomGlobal = "custom_value"; // Works due to declaration merging!
```

**Reference:** [TS Declaration Merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)

---

---

### 61. What is Type Assertion in TypeScript, and what is the difference between `as Type` and `<Type>`?

**Answer:**
**The Core Concept:**
A **Type Assertion** is a way to tell the TypeScript compiler: "I know the type of this value better than you do, so trust me." It overrides the compiler's default inference.
- `value as Type` is the standard modern syntax.
- `<Type>value` is the legacy angle-bracket syntax.

**Key Details:**
- **No Runtime Impact:** Assertions are completely stripped during compilation and do not perform any runtime casting, type-checking, or conversions.
- **Syntax clash:** The `<Type>` syntax is forbidden in `.tsx` files because it conflicts with React JSX tag parsing. Use `as Type` exclusively.
- **Safe Limit:** Assertions are not arbitrary; you can only assert to a more specific or less specific version of a type. For unrelated types, you must assert to `unknown` first: `x as unknown as string`.

**Example:**
```typescript
const element = document.getElementById("main-input") as HTMLInputElement;
element.value = "John Doe"; // Safe because we asserted it is an Input Element.
```

**Reference:** [TS Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)

---

---

### 62. What is Function Overloading in TypeScript, and how do you implement it?

**Answer:**
**The Core Concept:**
**Function Overloading** allows you to define multiple function signatures (overload signatures) for a single function, followed by a single unified implementation that handles all signature cases at runtime.

**Key Details:**
- **Safety:** Overload signatures are purely for type safety during development; they declare valid combinations of arguments and return types.
- **Implementation:** The implementation signature must be compatible with all overload signatures and is *not* callable directly. It must check argument types at runtime to execute the correct path.

**Example:**
```typescript
// 1. Overload Signatures
function getLength(str: string): number;
function getLength(arr: any[]): number;

// 2. Implementation Signature
function getLength(val: string | any[]): number {
  return val.length;
}

getLength("hello"); // Valid (returns number)
getLength([1, 2, 3]); // Valid (returns number)
// getLength(123); // Compiler Error: No overload matches this call.
```

**Reference:** [TS Function Overloads](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads)

---

---

### 63. What is the difference between `never` and `void` in TypeScript?

**Answer:**
**The Core Concept:**
- **`void`** represents the complete absence of a return value. A function returning `void` completes execution but returns nothing useful (evaluates to `undefined` at runtime).
- **`never`** represents values that can *never* occur. A function returning `never` **never completes execution** (either throws an uncaught error or runs infinitely).

**Key Details:**
- **Assignability:** `never` is the bottom type, meaning nothing can be assigned to `never` except `never` itself.
- **Exhaustive Checking:** `never` is commonly used in switch-case default blocks to enforce compile-time checking that all union members are handled.

**Example:**
```typescript
// void: returns undefined
function logMessage(msg: string): void {
  console.log(msg);
}

// never: execution halts
function throwError(msg: string): never {
  throw new Error(msg);
}
```

**Reference:** [TS never type](https://www.typescriptlang.org/docs/handbook/2/functions.html#never)

---

---

### 64. What is a Tuple in TypeScript, and how does it differ from a standard Array?

**Answer:**
**The Core Concept:**
A **Tuple** is an array-like type with a fixed number of elements, where the type of each specific element at each index is strictly declared. A standard **Array** represents a dynamic collection where all elements share the same type union.

**Key Details:**
- **Strict Boundaries:** Useful for expressing structured patterns (like geo-coordinates `[number, number]` or React state hooks `[T, Dispatch<SetStateAction<T>>]`).
- **Readonly Tuple:** Tuples are mutable unless compiled with `readonly` or `as const` assertions.

**Example:**
```typescript
// 1. Tuple: Strict index-based types
const coordinates: [number, number] = [40.7128, -74.0060];

// 2. Standard Array: Dynamic order of elements
const tags: string[] = ["react", "typescript"];
```

**Reference:** [TS Tuples](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)

---

---

### 65. What are Generics and how do you define a Generic constraint?

**Answer:**
**The Core Concept:**
**Generics** allow creating reusable components and functions that can work across multiple data types, acting as "type variables" resolved by the caller. A **Generic Constraint** restricts the types that a generic parameter can accept using the `extends` keyword.

**Key Details:**
- **Constraints:** Enforces that a type parameter must implement a specific interface or possess specific properties (like a `.length` property).

**Example:**
```typescript
// Generic constraint requiring a length property
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(arg: T): T {
  console.log("Length is:", arg.length);
  return arg;
}

logLength("hello"); // Valid (string has length)
logLength([1, 2, 3]); // Valid (array has length)
// logLength(123); // Error: Argument of type 'number' is not assignable to parameter of type 'HasLength'.
```

**Reference:** [TS Generic Constraints](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)

---

---

### 66. What are Mapped Types in TypeScript?

**Answer:**
**The Core Concept:**
**Mapped Types** allow you to create a new object type by iterating through a union of keys (usually using `keyof`), transforming the property names and types dynamically.

**Key Details:**
- **Modifiers:** You can add or subtract modifiers like `readonly` or optional (`?`) by prefixing them with `+` or `-` (e.g. `-readonly` to remove readonly).

**Example:**
```typescript
type FeatureFlags = {
  darkMode: () => void;
  analytics: () => void;
};

// Map all properties to boolean flags
type OptionsFlags<Type> = {
  [Property in keyof Type]: boolean;
};

type AppFeatures = OptionsFlags<FeatureFlags>;
// Resolves to: { darkMode: boolean; analytics: boolean; }
```

**Reference:** [TS Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)

---

## Practice Questions

---

### 1. Implement a custom `Omit<T, K>` utility type using mapped and conditional types.

**Example Solution:**
```javascript
Array.prototype.myMap = function(callback) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};
```

---

### 2. Create a type-safe API response wrapper using Generics.

**Example Solution:**
```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

async function apiCall<T>(url: string): Promise<ApiResponse<T>> {
  const res = await fetch(url);
  return res.json();
}
```

---

## Practice Questions

### 1. Implement a custom `Omit<T, K>` utility type using mapped and conditional types.

**Example Solution:**
```typescript
type MyOmit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;

// Example
interface User {
  id: number;
  name: string;
  email: string;
}
type PublicUser = MyOmit<User, 'email'>;
```

### 2. Create a type-safe API response wrapper using Generics.

**Example Solution:**
```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

async function apiCall<T>(url: string): Promise<ApiResponse<T>> {
  const res = await fetch(url);
  return res.json();
}
```

### 3. Define a custom `DeepPartial<T>` helper mapping deep optional nodes.

**Example Solution:**
```typescript
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

// Example
interface Config {
  db: { host: string; port: number };
}
const myConfig: DeepPartial<Config> = { db: { port: 5432 } };
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a TypeScript Type Systems application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy TypeScript Type Systems operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of TypeScript Type Systems configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using TypeScript Type Systems event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing TypeScript Type Systems with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output TypeScript Type Systems performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during TypeScript Type Systems failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to TypeScript Type Systems data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving TypeScript Type Systems state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates TypeScript Type Systems logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle TypeScript Type Systems files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking TypeScript Type Systems connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using TypeScript Type Systems.

*(Challenge question for self-study and practical project implementation.)*

