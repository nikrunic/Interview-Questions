# JavaScript Practical Questions & Answers

Verified outputs with step-by-step explanations for each snippet. **50 practical questions** (Q1–Q50). Run any example in Node.js or the browser console to confirm.

---

## Section A — `map` vs `forEach`

### 1. What is printed when you use `map` to return only even numbers without an `else` branch?

**Code:**

```javascript
const arriNumbers = [1, 2, 3, 4, 5, 6];
const r = arriNumbers.map((e) => {
  if (e % 2 == 0) {
    return e;
  }
});
console.log(arriNumbers);
console.log(r);
```

**Answer:**

```text
[1, 2, 3, 4, 5, 6]
[undefined, 2, undefined, 4, undefined, 6]
```

**How this answer is obtained:**

1. `map` always returns a **new array with the same length** as the original (6 elements).
2. For each element, if `e % 2 == 0` is true, the callback **returns** `e` (2, 4, 6).
3. For odd numbers (1, 3, 5), the `if` block is skipped and the function returns **`undefined`** implicitly.
4. `arriNumbers` is never mutated — only `r` is built from return values.

**Correct approach for only evens:** `arriNumbers.filter((e) => e % 2 === 0)` → `[2, 4, 6]`.

---

### 2. What does `forEach` return when you `return e` inside the callback?

**Code:**

```javascript
const arriNumbers1 = [1, 2, 3, 4, 5, 6];
const r1 = arriNumbers1.forEach((e) => {
  if (e % 2 == 0) {
    return e;
  }
});
console.log(r1);
```

**Answer:**

```text
undefined
```

**How this answer is obtained:**

1. `Array.prototype.forEach` **always returns `undefined`** — it is not designed to collect values.
2. `return e` inside the callback only skips the rest of **that iteration** (like `continue`); it does **not** return from the outer function or build an array.
3. Therefore `r1` is always `undefined`, regardless of what you return inside the callback.

---

### 3. How do you collect even numbers using `forEach` and an external array?

**Code:**

```javascript
const arriNumbers2 = [1, 2, 3, 4, 5, 6];
let r2 = [];
arriNumbers2.forEach((e) => {
  if (e % 2 == 0) {
    return r2.push(e);
  }
});
console.log(r2);
```

**Answer:**

```text
[2, 4, 6]
```

**How this answer is obtained:**

1. `r2` starts as `[]`.
2. For each even `e`, `r2.push(e)` adds the value to `r2` and returns the new length (ignored).
3. The `return` here does not affect `r2` — the **side effect** (`push`) is what builds the array.
4. Odd numbers skip the `if` block; nothing is pushed for them.

**Note:** In your original snippet you logged `r` instead of `r2`; the correct variable to log is `r2`.

**Preferred:** `const r2 = arriNumbers2.filter((e) => e % 2 === 0);`

---

## Section B — References (arrays & objects)

### 4. If `b1 = a1` and then `a1.push(5)`, what are `a1` and `b1`?

**Code:**

```javascript
const a1 = [1, 2, 3, 4];
const b1 = a1;
a1.push(5);
console.log(a1);
console.log(b1);
```

**Answer:**

```text
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

**How this answer is obtained:**

1. `b1 = a1` copies the **reference** (memory address), not a new array.
2. Both variables point to the **same array** in memory.
3. `a1.push(5)` mutates that shared array.
4. Reading `b1` shows the same mutated array.

**To copy without sharing:** `const b1 = [...a1];` or `const b1 = structuredClone(a1);`

---

### 5. Why does the first `console.log(a2)` differ from `console.log(b2)`?

**Code:**

```javascript
const a2 = [1, 2, 3, 4];
console.log(a2);
a2.push(5);
const b2 = a2;
console.log(b2);
```

**Answer:**

```text
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
```

**How this answer is obtained:**

1. **First log** runs **before** `push(5)` → still `[1, 2, 3, 4]`.
2. `a2.push(5)` mutates the array in place → `[1, 2, 3, 4, 5]`.
3. `b2 = a2` assigns the reference **after** the push, so `b2` already points to the array with `5`.
4. **Second log** shows `[1, 2, 3, 4, 5]`.

This is **timing of assignment**, not a separate copy.

---

### 6. What is `b3` after `b3 = a3` without `let` or `const`?

**Code:**

```javascript
const a3 = [1, 2, 3, 4];
b3 = a3;
console.log(b3);
```

**Answer:**

```text
[1, 2, 3, 4]
```

**How this answer is obtained:**

1. `b3 = a3` assigns the same array reference to `b3`.
2. Without `let`/`const`/`var`, `b3` becomes a property on the **global object** (`window` in browser, `global` in Node) in non-strict mode.
3. `console.log(b3)` prints the array contents `[1, 2, 3, 4]`.

**Best practice:** use `const b3 = a3;` (shared reference) or `const b3 = [...a3];` (shallow copy).

---

### 7. After shallow copy with spread, does changing `a4.name` affect `b4`?

**Code:**

```javascript
let a4 = { name: "john", age: 30 };
let b4 = { ...a4 };
a4.name = "jane";
console.log(a4);
console.log(b4);
```

**Answer:**

```text
{ name: 'jane', age: 30 }
{ name: 'john', age: 30 }
```

**How this answer is obtained:**

1. `{ ...a4 }` creates a **new object** and copies enumerable own properties (`name`, `age`) by value (primitives are copied).
2. `a4.name = "jane"` updates only the `a4` object.
3. `b4` is a separate object, so `b4.name` stays `"john"`.

**Note:** Your original code used `a.name = "jane"` (wrong variable). It must be `a4.name` to get this output.

**Shallow copy limit:** nested objects are still shared if you copy `{ user: { id: 1 } }` — use `structuredClone(a4)` for deep copy.

---

## Section C — `var` vs `let` (scope)

### 8. What are `b5` and `c5` after the `if` block?

**Code:**

```javascript
(() => {
  let c5;
  if (true) {
    var b5 = 20;
    c5 = 25;
  }
  console.log(b5);
  console.log(c5);
})();
```

**Answer:**

```text
20
25
```

**How this answer is obtained:**

1. `var b5` is **function-scoped** (hoisted to the IIFE scope), not block-scoped — it exists for the whole IIFE.
2. Inside `if`, `b5 = 20` assigns that binding → `b5` is `20` after the block.
3. `let c5` is declared in the outer block; `c5 = 25` inside `if` assigns the **outer** `c5` (no inner shadow) → `25`.

---

### 9. Why is outer `c6` `undefined` while `b6` is `20`?

**Code:**

```javascript
(() => {
  let c6;
  if (true) {
    var b6 = 20;
    let c6 = 25;
  }
  console.log(b6);
  console.log(c6);
})();
```

**Answer:**

```text
20
undefined
```

**How this answer is obtained:**

1. `var b6 = 20` → same as Q8: `b6` is `20` after the `if` block.
2. `let c6 = 25` **inside** `if` creates a **new block-scoped** variable that **shadows** the outer `let c6`.
3. The outer `c6` is **never assigned**, so it remains `undefined`.
4. The inner `c6 = 25` is destroyed when the `if` block ends.

---

## Section D — Event loop

### 10. In what order are `c`, `d`, `b`, and `a` logged?

**Code:**

```javascript
console.log("c");
setTimeout(() => console.log("a"), 0);
Promise.resolve().then(() => console.log("b"));
const promise = Promise.resolve();
console.log("d");
```

**Answer:**

```text
c
d
b
a
```

**How this answer is obtained:**

1. **Synchronous stack (first):** `console.log("c")` → `c`. `setTimeout` schedules a **macrotask**. `Promise.then` schedules a **microtask**. `Promise.resolve()` creates a promise but does not log yet. `console.log("d")` → `d`.
2. **Call stack empty:** run all **microtasks** → `.then` logs `b`.
3. **Then macrotasks:** `setTimeout` callback logs `a`.

Rule: sync code → microtasks (Promises) → macrotasks (`setTimeout`), even when delay is `0`.

---

## Section E — `reduce`

### 11. What is the sum of all numbers in `arr`?

**Code:**

```javascript
const arr = [2, 5, 8, 9, 6, 3, 1, 4, 7];
const sumOutput = arr.reduce((accumulater, current) => {
  accumulater = accumulater + current;
  return accumulater;
}, 0);
```

**Answer:**

```text
45
```

**How this answer is obtained:**

| Step | current | accumulater after |
|------|---------|-------------------|
| start | — | 0 |
| +2 | 2 | 2 |
| +5 | 5 | 7 |
| +8 | 8 | 15 |
| +9 | 9 | 24 |
| +6 | 6 | 30 |
| +3 | 3 | 33 |
| +1 | 1 | 34 |
| +4 | 4 | 38 |
| +7 | 7 | **45** |

Initial value `0` is the second argument to `reduce`. Each step must **return** the accumulator.

---

### 12. What is the maximum value in `arr` using `reduce` without an initial value?

**Code:**

```javascript
const arr = [2, 5, 8, 9, 6, 3, 1, 4, 7];
const maxOutput = arr.reduce((max, current) => {
  if (current > max) {
    max = current;
  }
  return max;
});
```

**Answer:**

```text
9
```

**How this answer is obtained:**

1. With **no initial value**, the first element (`2`) becomes the first `max`.
2. Each later element is compared; `max` is updated when `current` is larger.
3. The largest value in the array is **9**.

---

### 13. How many users exist for each age?

**Code:**

```javascript
const users = [
  { firstName: "knl", age: 30 },
  { firstName: "avi", age: 24 },
  { firstName: "dhey", age: 31 },
  { firstName: "dhol", age: 30 },
  { firstName: "abhy", age: 24 },
  { firstName: "akash", age: 30 },
  { firstName: "Rushik", age: 12 },
  { firstName: "uttam", age: 27 },
  { firstName: "devang", age: 18 },
  { firstName: "joy", age: 10 },
];

const ageArry = users.reduce((acc, curr) => {
  if (acc[curr.age]) {
    acc[curr.age] = ++acc[curr.age];
  } else {
    acc[curr.age] = 1;
  }
  return acc;
}, {});
```

**Answer:**

```javascript
{ 10: 1, 12: 1, 18: 1, 24: 2, 27: 1, 30: 3, 31: 1 }
```

**How this answer is obtained:**

1. Accumulator starts as `{}`.
2. For each user, use `age` as key. First time → set `1`. Already exists → increment with `++acc[curr.age]`.
3. Ages **24** (avi, abhy) → `2`. Ages **30** (knl, dhol, akash) → `3`. All others appear once.

---

### 14. Which first names have `age > 10`?

**Code:**

```javascript
const nameOutput = users.reduce((prevVal, currVal) => {
  if (currVal.age > 10) {
    prevVal.push(currVal.firstName);
  }
  return prevVal;
}, []);
```

**Answer:**

```javascript
["knl", "avi", "dhey", "dhol", "abhy", "akash", "Rushik", "uttam", "devang"]
```

**How this answer is obtained:**

1. Accumulator starts as `[]`.
2. **joy** has `age: 10` — condition is `> 10`, not `>= 10`, so **joy is excluded**.
3. All other 9 users have age 12 or higher → their `firstName` values are pushed.

Equivalent: `users.filter((u) => u.age > 10).map((u) => u.firstName)`.

---

## Section F — `map`

### 15. Which objects get `status: "inactive"` after `map`?

**Code:**

```javascript
const arr = [
  { name: "Jack", age: 24, status: "active" },
  { name: "Dan", age: 83, status: "active" },
  { name: "Garry", age: 61, status: "active" },
];

const newArr = arr.map((object) => {
  if (object.age >= 55) {
    return { ...object, status: "inactive" };
  }
  return object;
});
```

**Answer:**

```javascript
[
  { name: "Jack", age: 24, status: "active" },
  { name: "Dan", age: 83, status: "inactive" },
  { name: "Garry", age: 61, status: "inactive" },
]
```

**How this answer is obtained:**

1. Jack (24) → returns **same object reference** with `status: "active"`.
2. Dan (83) and Garry (61) → `age >= 55` → new object via spread with `status: "inactive"`.
3. Original `arr` is unchanged unless you assign `arr = newArr`.

---

### 16. What are `double`, `tripal`, and `binary` for `[3, 5, 8, 9, 12]`?

**Code:**

```javascript
const arr = [3, 5, 8, 9, 12];
const double = arr.map((x) => x * 2);
const tripal = arr.map((x) => x * 3);
const binary = arr.map((x) => x.toString(2));
```

**Answer:**

```javascript
double  → [6, 10, 16, 18, 24]
tripal  → [9, 15, 24, 27, 36]
binary  → ["11", "101", "1000", "1001", "1100"]
```

**How this answer is obtained:**

1. `map` applies the function to **each index**; length stays **5**.
2. `x * 2` and `x * 3` are numeric multiplication.
3. `x.toString(2)` converts each number to a **binary string** (base 2), e.g. `12` → `"1100"`.

---

## Section G — `filter`

### 17. What are `isOdd`, `isEven`, and `isGraterThen` for `[3, 5, 8, 9, 12]`?

**Code:**

```javascript
const arr = [3, 5, 8, 9, 12];

const isOdd = arr.filter((x) => x % 2);
const isEven = arr.filter((x) => x % 2 === 0);
const isGraterThen = arr.filter((x) => x > 6);
```

**Answer:**

```javascript
isOdd         → [3, 5, 9]
isEven        → [8, 12]
isGraterThen  → [8, 9, 12]
```

**How this answer is obtained:**

1. `filter` keeps elements where the callback returns **truthy**.
2. `x % 2` for odd `x` is `1` (truthy); for even `x` is `0` (falsy).
3. `x % 2 === 0` keeps only evens.
4. `x > 6` keeps 8, 9, 12.

---

### 18. What are `filterAge` and `filterName` for the `users` array?

**Code:**

```javascript
const filterAge = users.filter((x) => x.age > 20);
const filterName = users.filter((x) => x.age < 20).map((y) => y.firstName);
```

**Answer:**

```javascript
filterAge.length  → 7 users (ages 24, 27, 30, 31)
filterName        → ["Rushik", "devang", "joy"]
```

**How this answer is obtained:**

1. `age > 20` includes: knl(30), avi(24), dhey(31), dhol(30), abhy(24), akash(30), uttam(27) → **7 objects**.
2. `age < 20` includes: Rushik(12), devang(18), joy(10) → **3 names** after `.map`.

---

## Section H — Group by branch

### 19. What is `merged` when grouping `company` by branch with `reduce`?

**Code:**

```javascript
const company = [
  { name: "krunal", branch: "aa" },
  { name: "avanish", branch: "ab" },
  { name: "nisarga", branch: "ac" },
  { name: "utam", branch: "aa" },
  { name: "malinga", branch: "ab" },
  { name: "himani", branch: "ac" },
  { name: "manthan", branch: "aa" },
  { name: "Khimesh", branch: "ab" },
  { name: "krunal", branch: "ac" },
];

const merged = company.reduce((acc, cur) => {
  const found = acc.find((item) => item.branch === cur.branch);
  if (found) {
    found.names.push(cur.name);
  } else {
    acc.push({ branch: cur.branch, names: [cur.name] });
  }
  return acc;
}, []);
```

**Answer:**

```javascript
[
  { branch: "aa", names: ["krunal", "utam", "manthan"] },
  { branch: "ab", names: ["avanish", "malinga", "Khimesh"] },
  { branch: "ac", names: ["nisarga", "himani", "krunal"] },
]
```

**How this answer is obtained:**

1. Start with `acc = []`.
2. For each person, `find` checks if that `branch` already exists in `acc`.
3. If yes → push `name` into existing `names` array.
4. If no → add `{ branch, names: [name] }`.
5. Order of branches follows **first appearance**: aa, ab, ac.

---

### 20. What is `output` when grouping with `forEach` (note: property is `name`, not `names`)?

**Code:**

```javascript
const output = [];
company.forEach((element) => {
  let branchData = output.find((o) => o.branch === element.branch);
  if (branchData) {
    branchData.name.push(element.name);
  } else {
    output.push({
      name: [element.name],
      branch: element.branch,
    });
  }
});
```

**Answer:**

```javascript
[
  { name: ["krunal", "utam", "manthan"], branch: "aa" },
  { name: ["avanish", "malinga", "Khimesh"], branch: "ab" },
  { name: ["nisarga", "himani", "krunal"], branch: "ac" },
]
```

**How this answer is obtained:**

Same logic as Q19, but the list of names is stored under the key **`name`** (array) instead of **`names`**. The grouped data is identical; only the property name differs.

---

## Section I — Build & transform arrays

### 21. How do you convert `["a", "b", "c"]` into objects with `task_date`?

**Code:**

```javascript
const array1 = ["a", "b", "c"];
let lootArray = [];
array1.forEach((element) => lootArray.push({ task_date: element }));
```

**Answer:**

```javascript
[
  { task_date: "a" },
  { task_date: "b" },
  { task_date: "c" },
]
```

**How this answer is obtained:**

1. Each string becomes one object via `push` inside `forEach`.
2. **Declarative alternative:** `array1.map((element) => ({ task_date: element }))` — same result, returns the array directly.

---

## Section J — Unique values

### 22. What does `uniqueArraySet([1, 5, 2, 4, 1, 6])` return?

**Code:**

```javascript
function uniqueArraySet(array) {
  const newSet = new Set(array);
  return Array.from(newSet);
}
uniqueArraySet([1, 5, 2, 4, 1, 6]);
```

**Answer:**

```javascript
[1, 5, 2, 4, 6]
```

**How this answer is obtained:**

1. `Set` stores only **unique** values; duplicate `1` is ignored.
2. `Array.from` converts the Set back to an array.
3. Order is **insertion order** (first time each value appeared).

---

### 23. What does `uniqueArrayFilter` return?

**Code:**

```javascript
function uniqueArrayFilter(arr) {
  return arr.filter((elem, index, self) => index === self.indexOf(elem));
}
uniqueArrayFilter([1, 5, 2, 4, 1, 6]);
```

**Answer:**

```javascript
[1, 5, 2, 4, 6]
```

**How this answer is obtained:**

1. Keep element only at its **first index** (`indexOf` finds first position).
2. Second `1` has `index !== indexOf` → filtered out.
3. Same result as Set; worst-case time is O(n²) due to `indexOf` inside `filter`.

---

### 24. What does `uniqueArrayForEach` return and what is the caveat?

**Code:**

```javascript
function uniqueArrayForEach(arr) {
  const unique = [];
  arr.forEach(function (i) {
    if (!unique[i]) {
      unique[i] = true;
    }
  });
  return Object.keys(unique);
}
uniqueArrayForEach([6, 7, 1, 5, 2, 4, 1, 6]);
```

**Answer:**

```javascript
["1", "2", "4", "5", "6", "7"]
```

**How this answer is obtained:**

1. Uses array values as **indices** (`unique[6] = true`, etc.) — a sparse array trick.
2. `Object.keys` returns keys as **strings**, sorted numerically for numeric keys.
3. Duplicate `1` and `6` do not add new keys.

**Caveats:** Not a general-purpose dedupe (fails for non-integer values, `null`, objects). Prefer `[...new Set(arr)]`.

---

## Section K — Regular expressions

### 25. How do you swap first and last name in `"Akash Barsagadey"`?

**Code:**

```javascript
const name = "Akash Barsagadey";
const swapName = name.replace(/(\w+)\s(\w+)/, "$2 $1");
```

**Answer:**

```text
"Barsagadey Akash"
```

**How this answer is obtained:**

1. `(\w+)` — capture group 1: first word (`Akash`).
2. `\s` — space between words.
3. `(\w+)` — capture group 2: second word (`Barsagadey`).
4. Replacement `"$2 $1"` puts group 2 first, then group 1.

**Limitation:** Only the **first two** words are matched. For three or more words, use split/reverse/join or a different pattern.

---

## Section L — `find`, `some`, `every`, `includes`

### 26. What is the difference between `find` and `filter`?

**Code:**

```javascript
const nums = [3, 7, 12, 5, 9];
const firstBig = nums.find((x) => x > 6);
const allBig = nums.filter((x) => x > 6);
```

**Answer:**

```javascript
firstBig  → 7        // first match only
allBig    → [7, 12, 9]
```

**How this answer is obtained:**

1. `find` returns the **first element** that satisfies the test, or `undefined` if none.
2. `filter` returns a **new array** of **all** matching elements.
3. Both stop iterating after `find` finds one match (short-circuit for `find`).

---

### 27. What do `some` and `every` return?

**Code:**

```javascript
const nums = [1, 2, 3];
console.log(nums.some((x) => x > 2));
console.log(nums.every((x) => x > 0));
console.log(nums.every((x) => x > 2));
```

**Answer:**

```text
true
true
false
```

**How this answer is obtained:**

1. `some` → **true** if **at least one** element passes (3 > 2).
2. `every` → **true** only if **all** elements pass.
3. `every((x) => x > 2)` fails on 1 and 2 → **false**.

---

### 28. How do you check if an array includes a value?

**Code:**

```javascript
const fruits = ["apple", "banana", "mango"];
console.log(fruits.includes("banana"));
console.log(fruits.includes("grape"));
console.log(fruits.indexOf("mango"));
```

**Answer:**

```text
true
false
2
```

**How this answer is obtained:**

1. `includes` returns **boolean** — good for existence checks.
2. `indexOf` returns **index** (0-based) or **-1** if missing.
3. Prefer `includes` when you only need true/false (clearer with `NaN` edge cases).

---

## Section M — `sort`, `slice`, `splice`

### 29. Why does `[10, 2, 5].sort()` not sort numbers correctly?

**Code:**

```javascript
const wrong = [10, 2, 5].sort();
const right = [10, 2, 5].sort((a, b) => a - b);
console.log(wrong);
console.log(right);
```

**Answer:**

```javascript
wrong → [10, 2, 5]   // string sort: "10" before "2"
right → [2, 5, 10]
```

**How this answer is obtained:**

1. Default `sort()` converts elements to **strings** and compares Unicode order.
2. `"10"` starts with `"1"`, which is less than `"2"`, so `10` appears first.
3. Numeric sort: `(a, b) => a - b` ascending; `(a, b) => b - a` descending.

---

### 30. What is the difference between `slice` and `splice`?

**Code:**

```javascript
const original1 = [1, 2, 3, 4];
const sliced = original1.slice(1, 3);

const original2 = [1, 2, 3, 4];
const removed = original2.splice(1, 2, "x");
```

**Answer:**

```javascript
sliced    → [2, 3]           // original1 unchanged: [1, 2, 3, 4]
removed   → [2, 3]             // what was removed
original2 → [1, "x", 4]        // mutated in place
```

**How this answer is obtained:**

1. **`slice(start, end)`** — non-mutating; `end` is exclusive. Copies elements from index 1 up to (not including) 3.
2. **`splice(start, deleteCount, ...items)`** — **mutates** array; deletes 2 items at index 1, inserts `"x"`.
3. Memory trick: **s**lice = **s**afe copy · **s**plice = **s**urgery (changes original).

---

## Section N — `flat`, `flatMap`, spread

### 31. How do you flatten a nested array?

**Code:**

```javascript
const nested = [1, [2, [3, 4]], 5];
console.log(nested.flat());
console.log(nested.flat(2));
```

**Answer:**

```javascript
flat()   → [1, 2, [3, 4], 5]   // depth 1
flat(2)  → [1, 2, 3, 4, 5]     // depth 2
```

**How this answer is obtained:**

1. `flat()` default depth is **1** — one level of nesting removed.
2. `flat(2)` flattens two levels — inner `[3, 4]` merges into the main array.
3. `Infinity` flattens fully: `nested.flat(Infinity)`.

---

### 32. What does `flatMap` do?

**Code:**

```javascript
const nums = [1, 2, 3];
const result = nums.flatMap((x) => [x, x * 2]);
```

**Answer:**

```javascript
[1, 2, 2, 4, 3, 6]
```

**How this answer is obtained:**

1. `flatMap` = `map` then `flat(1)` in one step.
2. Each `x` becomes `[x, x*2]`; results are concatenated into one array.
3. Shorter than `nums.map(...).flat()` when each item maps to multiple values.

---

### 33. How do you merge arrays and clone with spread?

**Code:**

```javascript
const a = [1, 2];
const b = [3, 4];
const merged = [...a, ...b, 5];
const copy = [...a];

a.push(99);
console.log(merged);
console.log(copy);
console.log(a);
```

**Answer:**

```javascript
merged → [1, 2, 3, 4, 5]
copy   → [1, 2]        // shallow copy — not affected by later push on a
a      → [1, 2, 99]
```

**How this answer is obtained:**

1. Spread **`...`** expands iterables into individual elements.
2. `[...a]` creates a **new array** (shallow copy of top-level elements).
3. `merged` is independent; `copy` does not get `99` because `push` only mutates `a`.

---

## Section O — Destructuring & rest

### 34. How do array and object destructuring work?

**Code:**

```javascript
const [first, second, ...rest] = [10, 20, 30, 40];
const { name, age: userAge = 18 } = { name: "Knl", age: 30 };

console.log(first, second, rest);
console.log(name, userAge);
```

**Answer:**

```text
10 20 [30, 40]
Knl 30
```

**How this answer is obtained:**

1. Array destructuring assigns by **position**; `...rest` collects remaining elements.
2. Object destructuring uses **property names**; `age: userAge` renames; `= 18` is default if missing.
3. `userAge` is `30` because `age` exists — default applies only for `undefined`.

---

### 35. How do rest parameters work in functions?

**Code:**

```javascript
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
console.log(sum(1, 2, 3, 4));
```

**Answer:**

```text
10
```

**How this answer is obtained:**

1. `...numbers` collects all arguments into a **real array** `[1, 2, 3, 4]`.
2. Unlike `arguments`, rest works in arrow functions (if used in params) and is always an array.
3. `reduce` sums to **10**.

---

## Section P — Operators & truthiness

### 36. What is the difference between `==` and `===`?

**Code:**

```javascript
console.log(5 == "5");
console.log(5 === "5");
console.log(0 == false);
console.log(0 === false);
console.log(null == undefined);
console.log(null === undefined);
```

**Answer:**

```text
true
false
true
false
true
false
```

**How this answer is obtained:**

1. `==` performs **type coercion** before compare (string `"5"` becomes number `5`).
2. `===` compares **value and type** — no coercion.
3. Always prefer **`===`** unless you have a specific reason for `==`.

---

### 37. What is the difference between `||` and `??`?

**Code:**

```javascript
console.log(0 || "default");
console.log(0 ?? "default");
console.log("" || "default");
console.log("" ?? "default");
console.log(null ?? "default");
```

**Answer:**

```text
default
0
default
(empty string)
default
```

**How this answer is obtained:**

1. `||` returns right side if left is **any falsy** value (`0`, `""`, `null`, `undefined`, `false`, `NaN`).
2. `??` (nullish coalescing) returns right side only if left is **`null` or `undefined`**.
3. Use `??` when `0` or `""` are valid values you want to keep.

---

### 38. What is optional chaining (`?.`)?

**Code:**

```javascript
const user = { profile: { city: "Ahmedabad" } };
const missing = {};

console.log(user?.profile?.city);
console.log(missing?.profile?.city);
console.log(missing.profile.city);
```

**Answer:**

```text
Ahmedabad
undefined
// TypeError: Cannot read properties of undefined (reading 'city')
```

**How this answer is obtained:**

1. `?.` short-circuits to `undefined` if the part before it is `null` or `undefined`.
2. No error for `missing?.profile?.city`.
3. Without `?.`, `missing.profile` throws because `profile` is read on `undefined`.

---

## Section Q — Closures & `this`

### 39. How does a closure preserve counter state?

**Code:**

```javascript
function makeCounter() {
  let count = 0;
  return () => ++count;
}
const counter = makeCounter();
console.log(counter());
console.log(counter());
console.log(counter());
```

**Answer:**

```text
1
2
3
```

**How this answer is obtained:**

1. Inner function **closes over** `count` from the outer scope.
2. Each call to `counter()` increments the **same** `count` variable.
3. `count` is not global — it is private to the closure created by `makeCounter()`.

---

### 40. How does `this` differ in arrow functions vs regular functions?

**Code:**

```javascript
const obj = {
  name: "Knl",
  regular: function () {
    return this.name;
  },
  arrow: () => this.name,
};

console.log(obj.regular());
console.log(obj.arrow());
```

**Answer (in browser or Node REPL — `this` for arrow follows lexical scope):**

```text
"Knl"
undefined   // arrow uses outer `this` (global/window), not obj
```

**How this answer is obtained:**

1. **Regular function** called as `obj.regular()` — `this` is `obj`.
2. **Arrow function** has **no own `this`** — it inherits `this` from where it was **defined** (module/global), not from `obj`.
3. Use regular functions for object methods when you need `this`; arrows for callbacks when you want lexical `this`.

---

## Section R — Promises & `async/await`

### 41. In what order do Promise callbacks run?

**Code:**

```javascript
console.log("1");
Promise.resolve().then(() => console.log("2"));
Promise.resolve().then(() => console.log("3"));
console.log("4");
```

**Answer:**

```text
1
4
2
3
```

**How this answer is obtained:**

1. Sync: `1`, then promises scheduled, then `4`.
2. Stack empty → run **microtasks** in order: `2`, then `3`.
3. Same pattern as Q10 (event loop).

---

### 42. What does `async/await` print?

**Code:**

```javascript
async function demo() {
  console.log("A");
  await Promise.resolve();
  console.log("B");
}
console.log("C");
demo();
console.log("D");
```

**Answer:**

```text
C
A
D
B
```

**How this answer is obtained:**

1. `C` sync first.
2. `demo()` runs until first `await` → logs `A`, then pauses `demo` and returns a Promise.
3. `D` runs (still sync, before microtasks from awaited promise complete).
4. After microtask, `demo` resumes → logs `B`.

---

## Section S — Strings & common patterns

### 43. How do you check if a string is a palindrome?

**Code:**

```javascript
const isPalindrome = (str) =>
  str === str.split("").reverse().join("");

console.log(isPalindrome("madam"));
console.log(isPalindrome("hello"));
```

**Answer:**

```text
true
false
```

**How this answer is obtained:**

1. `split("")` → array of characters.
2. `reverse()` reverses array in place.
3. `join("")` builds string — compare to original.

**Case-insensitive:** `str.toLowerCase()` before compare.

---

### 44. How do you count word/letter frequency with `reduce`?

**Code:**

```javascript
const letters = ["a", "b", "a", "c", "a", "b"];
const count = letters.reduce((acc, letter) => {
  acc[letter] = (acc[letter] || 0) + 1;
  return acc;
}, {});
console.log(count);
```

**Answer:**

```javascript
{ a: 3, b: 2, c: 1 }
```

**How this answer is obtained:**

1. Start with `{}`.
2. For each letter, set `acc[letter]` to existing count + 1, or `0 + 1` if first time (`|| 0`).
3. Return updated `acc` each step.

---

### 45. How do you deep clone with `JSON` and what are the limits?

**Code:**

```javascript
const original = { a: 1, nested: { b: 2 } };
const clone = JSON.parse(JSON.stringify(original));
original.nested.b = 99;
console.log(clone.nested.b);
console.log(original.nested.b);
```

**Answer:**

```text
2
99
```

**How this answer is obtained:**

1. `JSON.stringify` → string; `JSON.parse` → new object tree.
2. `clone` is independent — changing `original` does not affect `clone`.
3. **Limits:** loses `undefined`, functions, `Date` (becomes string), `Map`, circular refs throw. Prefer `structuredClone(original)` in modern JS.

---

### 46. How do you chain `map`, `filter`, and `reduce` in one pipeline?

**Code:**

```javascript
const products = [
  { name: "Pen", price: 10, qty: 2 },
  { name: "Book", price: 50, qty: 1 },
  { name: "Bag", price: 200, qty: 3 },
];

const total = products
  .filter((p) => p.price < 100)
  .map((p) => ({ ...p, lineTotal: p.price * p.qty }))
  .reduce((sum, p) => sum + p.lineTotal, 0);

console.log(total);
```

**Answer:**

```text
70
```

**How this answer is obtained:**

1. `filter` — Pen (10) and Book (50) pass `price < 100`; Bag (200) is removed.
2. `map` — Pen `lineTotal: 10 × 2 = 20`, Book `lineTotal: 50 × 1 = 50`.
3. `reduce` — `20 + 50 = 70`.

---

### 47. How do you get intersection of two arrays with `Set`?

**Code:**

```javascript
const a = [1, 2, 3, 4];
const b = [3, 4, 5, 6];
const intersection = [...new Set(a)].filter((x) => new Set(b).has(x));
console.log(intersection);
```

**Answer:**

```javascript
[3, 4]
```

**How this answer is obtained:**

1. Convert `b` to `Set` for O(1) lookup with `.has(x)`.
2. Filter `a` (via Set dedupe of `a` if needed) for values that exist in both arrays.
3. Result: elements in **both** `a` and `b`.

---

### 48. How do you remove falsy values from an array?

**Code:**

```javascript
const mixed = [0, 1, false, 2, "", 3, null, undefined, NaN, 4];
const cleaned = mixed.filter(Boolean);
console.log(cleaned);
```

**Answer:**

```javascript
[1, 2, 3, 4]
```

**How this answer is obtained:**

1. `Boolean` as callback converts each value to true/false.
2. Falsy values (`0`, `false`, `""`, `null`, `undefined`, `NaN`) are removed.
3. To keep `0`, use explicit filter: `.filter((x) => x !== null && x !== undefined && !Number.isNaN(x))`.

---

### 49. What is the output of `typeof` and `Array.isArray`?

**Code:**

```javascript
console.log(typeof []);
console.log(typeof null);
console.log(Array.isArray([]));
console.log(Array.isArray({}));
```

**Answer:**

```text
object
object
true
false
```

**How this answer is obtained:**

1. Arrays are type **`object`** in JavaScript — `typeof []` is `"object"`.
2. Historical bug: `typeof null` is also `"object"`.
3. Use **`Array.isArray()`** to reliably detect arrays.

---

### 50. How do you safely access nested JSON API data?

**Code:**

```javascript
const apiResponse = {
  data: {
    users: [{ id: 1, name: "Knl" }],
  },
};

const name = apiResponse?.data?.users?.[0]?.name ?? "Guest";
const missing = apiResponse?.items?.[0]?.title ?? "N/A";

console.log(name);
console.log(missing);
```

**Answer:**

```text
Knl
N/A
```

**How this answer is obtained:**

1. `?.` avoids errors when a path is missing (`items` does not exist).
2. `?.[0]` safely accesses first array element.
3. `?? "Guest"` / `?? "N/A"` applies only when result is `null` or `undefined`.

---

## Quick reference

| Goal | Method |
|------|--------|
| Transform each item | `map` |
| Keep matching items | `filter` |
| Single accumulated value | `reduce` |
| Side effects only | `forEach` |
| Unique values | `[...new Set(arr)]` |
| Shallow copy array | `[...arr]` |
| Shallow copy object | `{ ...obj }` |
| Deep copy | `structuredClone(value)` |

**References:** [MDN Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) · [Event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)
