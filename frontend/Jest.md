# Jest & React Testing Library Interview Questions

This document contains interview questions focused on testing JavaScript and React applications.

## Basic (Easy)

### 1. What is Jest?
**Answer:** 
**The Core Concept:**
Jest is a delightful JavaScript Testing Framework with a focus on simplicity.

**Key Details:**
- It works out of the box for most JavaScript projects without configuration.
- It provides built-in matchers, mocking capabilities, and a test runner.

**Example:** `test('adds 1 + 2 to equal 3', () => { expect(sum(1, 2)).toBe(3); });`

**Reference:** [Jest Documentation](https://jestjs.io/)

---

### 2. What is React Testing Library (RTL)?
**Answer:** 
**The Core Concept:**
RTL is a testing utility for React that encourages testing components the way users interact with them.

**Key Details:**
- It focuses on querying the DOM for nodes rather than testing internal component state or implementation details.
- Promotes accessibility best practices by providing queries like `getByRole`.

**Example:** `render(<MyComponent />); expect(screen.getByText('Hello')).toBeInTheDocument();`

**Reference:** [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)

---
\n## Additional Depth (Architectural Focus)\n
### 3. How does Jest's module mocking (`jest.mock()`) work?
**Answer:** 
**The Core Concept:**
Jest intercepts the `require` or `import` calls during the test execution phase. When you call `jest.mock('module-name')`, Jest replaces the actual module with an auto-generated mock object, allowing you to control its behavior and track its usage.

**Key Details:**
- Because ES6 imports are hoisted to the top of the file by Babel, Jest uses a babel-plugin to ensure `jest.mock()` calls are hoisted above all `import` statements.
- You can provide a factory function to `jest.mock()` to define exactly how the mocked module should behave, which is critical for isolating the unit under test from external dependencies like database clients.

**Example:** 
`jest.mock('axios'); axios.get.mockResolvedValue({ data: {} });`

**Reference:** [Documentation](https://jestjs.io/docs/mock-functions)

---
