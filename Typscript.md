# TypeScript Interview Questions

This document contains a comprehensive list of TypeScript interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is TypeScript?
**Answer:** TypeScript is an open-source programming language developed by Microsoft. It is a strict syntactical superset of JavaScript and adds optional static typing to the language.
**Example:** `let isDone: boolean = false;`
**Reference:** [TypeScript Official Docs](https://www.typescriptlang.org/docs/)

### 2. How is TypeScript different from JavaScript?
**Answer:** JavaScript is dynamically typed, while TypeScript is statically typed. TypeScript allows identifying type errors at compile time, whereas JS errors are usually caught at runtime. TypeScript must be compiled into JavaScript to run in a browser.
**Example:** `let x = 10; x = "hello"; // Valid in JS, Error in TS`
**Reference:** [TS Docs - TypeScript for New Programmers](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)

### 3. What is a Type Assertion?
**Answer:** Type assertion is a way to tell the compiler "trust me, I know what I'm doing." It is like type casting in other languages, but it performs no special checking or restructuring of data.
**Example:** `let strLength: number = (<string>someValue).length;` or `(someValue as string).length;`
**Reference:** [TS Docs - Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)

### 4. What is the `any` type?
**Answer:** The `any` type is a powerful way to work with existing JavaScript, allowing you to opt-out of type checking and let the values pass through compile-time checks.
**Example:** `let looselyTyped: any = 4; looselyTyped = "Now I am a string";`
**Reference:** [TS Docs - any](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#any)

### 5. What are Interfaces?
**Answer:** Interfaces are a core way in TypeScript to name object types and establish contracts within your code as well as contracts with code outside of your project.
**Example:** `interface User { name: string; age: number; }`
**Reference:** [TS Docs - Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)


## Medium (30%)

### 6. What is the difference between `interface` and `type` aliases?
**Answer:** Both can be used to describe the shape of an object or a function signature. However, interfaces are better for defining object shapes and can be merged (declaration merging). Type aliases can be used for primitives, unions, and tuples.
**Example:** `type ID = string | number;` (Cannot do this with an interface).
**Reference:** [TS Docs - Differences Between Type Aliases and Interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

### 7. What is an Enum?
**Answer:** Enums allow a developer to define a set of named constants. Using enums can make it easier to document intent, or create a set of distinct cases. TS provides both numeric and string-based enums.
**Example:** `enum Direction { Up = 1, Down, Left, Right }`
**Reference:** [TS Docs - Enums](https://www.typescriptlang.org/docs/handbook/enums.html)

### 8. What are Generics in TypeScript?
**Answer:** Generics provide a way to make components work over a variety of types rather than a single one. This allows users to consume these components and use their own types.
**Example:** `function identity<T>(arg: T): T { return arg; }`
**Reference:** [TS Docs - Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)

### 9. What is the `unknown` type?
**Answer:** The `unknown` type is the type-safe counterpart of `any`. Anything is assignable to `unknown`, but `unknown` isn't assignable to anything but itself and `any` without a type assertion or a control flow based narrowing.
**Example:** `let value: unknown; if (typeof value === "string") { console.log(value.toUpperCase()); }`
**Reference:** [TS Docs - unknown](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#new-unknown-top-type)

### 10. Explain Union and Intersection types.
**Answer:** A Union type (`|`) describes a value that can be one of several types. An Intersection type (`&`) combines multiple types into one, meaning a value of this type will have all properties of the intersected types.
**Example:** Union: `let id: number | string;` Intersection: `type AdminUser = User & Admin;`
**Reference:** [TS Docs - Unions and Intersections](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)


## Hard (50%)

### 11. What are Utility Types? Give some examples.
**Answer:** TS provides several global utility types to facilitate common type transformations. Examples: `Partial<T>` (makes all properties optional), `Readonly<T>`, `Record<K, T>`, `Pick<T, K>`, and `Omit<T, K>`.
**Example:** `type OptionalUser = Partial<User>;`
**Reference:** [TS Docs - Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)

### 12. How do Decorators work in TypeScript?
**Answer:** Decorators provide a way to add both annotations and a meta-programming syntax for class declarations and members. They are functions called at runtime with information about the decorated declaration.
**Example:** `@sealed class BugReport { ... }`
**Reference:** [TS Docs - Decorators](https://www.typescriptlang.org/docs/handbook/decorators.html)

### 13. What is Type Guarding / Type Narrowing?
**Answer:** Narrowing occurs when TS infers a more specific type than declared based on runtime checks (like `typeof`, `instanceof`, `in`, or custom type guard functions).
**Example:** `function isString(test: any): test is string { return typeof test === "string"; }`
**Reference:** [TS Docs - Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)

### 14. What are Mapped Types?
**Answer:** Mapped types allow you to create new types based on existing ones by iterating over keys.
**Example:** `type OptionsFlags<Type> = { [Property in keyof Type]: boolean; };`
**Reference:** [TS Docs - Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)

### 15. Explain Conditional Types.
**Answer:** Conditional types take a form that looks like a conditional expression (`condition ? trueExpression : falseExpression`). They allow types to be evaluated dynamically.
**Example:** `type NonNullable<T> = T extends null | undefined ? never : T;`
**Reference:** [TS Docs - Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)

### 16. What is the `never` type?
**Answer:** The `never` type represents the type of values that never occur. It is used as the return type for functions that always throw an exception or never return (infinite loops).
**Example:** `function error(message: string): never { throw new Error(message); }`
**Reference:** [TS Docs - never](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-never-type)

### 17. How does Declaration Merging work?
**Answer:** Declaration merging means the compiler merges two or more separate declarations declared with the same name into a single definition. This is most commonly used with `interface`.
**Example:** `interface Box { height: number; } interface Box { width: number; }` resulting in an object with both properties.
**Reference:** [TS Docs - Declaration Merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)

### 18. What is the `infer` keyword?
**Answer:** The `infer` keyword is used within conditional types to infer a type variable from the structure of another type.
**Example:** `type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;`
**Reference:** [TS Docs - Type inference in conditional types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types)

### 19. What is `tsconfig.json` and what is `strict` mode?
**Answer:** `tsconfig.json` specifies the root files and compiler options required to compile the project. The `strict` flag enables a wide range of type checking behavior that results in stronger guarantees of program correctness (e.g., `noImplicitAny`, `strictNullChecks`).
**Example:** `"compilerOptions": { "strict": true }`
**Reference:** [TS Docs - tsconfig](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)

### 20. What is a Tuple type?
**Answer:** Tuple types allow you to express an array with a fixed number of elements whose types are known, but need not be the same.
**Example:** `let x: [string, number]; x = ["hello", 10];`
**Reference:** [TS Docs - Tuple](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)
