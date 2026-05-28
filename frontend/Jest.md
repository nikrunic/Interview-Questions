# Jest & React Testing Library Interview Questions

This document contains interview questions focused on testing JavaScript and React applications.

## Basic Questions

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

---

## Intermediate Questions

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

## Additional Depth (Architectural Focus)


---

## Expert Questions

---

## Intermediate Questions

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

---

## Practice Questions

---

### 1. Write a Jest unit test to mock a fetch callback helper.

**Example Solution:**
```javascript
const fetchProducts = async (fetcherFn) => {
  const data = await fetcherFn("/products");
  return data.map(p => p.name.toUpperCase());
};

// Jest Test
test('should fetch products and format names', async () => {
  const mockFetcher = jest.fn().mockResolvedValue([
    { name: "laptop" },
    { name: "phone" }
  ]);
  
  const result = await fetchProducts(mockFetcher);
  
  expect(mockFetcher).toHaveBeenCalledWith("/products");
  expect(result).toEqual(["LAPTOP", "PHONE"]);
});
```

---

## Expert Questions

### 2. Write a Jest test checking promise resolution and error rejections.

**Example Solution:**
```javascript
function loadUser(id) {
  if (id <= 0) return Promise.reject(new Error("Invalid ID"));
  return Promise.resolve({ id, name: "Nik" });
}

// Jest Tests
describe('loadUser API', () => {
  test('resolves data on valid ID', async () => {
    await expect(loadUser(1)).resolves.toEqual({ id: 1, name: "Nik" });
  });

  test('rejects with error on invalid ID', async () => {
    await expect(loadUser(-1)).rejects.toThrow("Invalid ID");
  });
});
```

---

## Practice Questions

### 1. Write a Jest unit test to mock a fetch callback helper.

**Example Solution:**
```javascript
const fetchProducts = async (fetcherFn) => {
  const data = await fetcherFn("/products");
  return data.map(p => p.name.toUpperCase());
};

// Jest Test
test('should fetch products and format names', async () => {
  const mockFetcher = jest.fn().mockResolvedValue([
    { name: "laptop" },
    { name: "phone" }
  ]);
  
  const result = await fetchProducts(mockFetcher);
  
  expect(mockFetcher).toHaveBeenCalledWith("/products");
  expect(result).toEqual(["LAPTOP", "PHONE"]);
});
```

### 2. Write a Jest test checking promise resolution and error rejections.

**Example Solution:**
```javascript
function loadUser(id) {
  if (id <= 0) return Promise.reject(new Error("Invalid ID"));
  return Promise.resolve({ id, name: "Nik" });
}

// Jest Tests
describe('loadUser API', () => {
  test('resolves data on valid ID', async () => {
    await expect(loadUser(1)).resolves.toEqual({ id: 1, name: "Nik" });
  });

  test('rejects with error on invalid ID', async () => {
    await expect(loadUser(-1)).rejects.toThrow("Invalid ID");
  });
});
```

### 3. Write a Jest test simulating and checking timers via `jest.useFakeTimers()`.

**Example Solution:**
```javascript
function delayCallback(callback) {
  setTimeout(() => callback("done"), 1000);
}

test('should call callback after timeout', () => {
  jest.useFakeTimers();
  const mockCb = jest.fn();
  delayCallback(mockCb);
  
  expect(mockCb).not.toBeCalled();
  jest.advanceTimersByTime(1000);
  expect(mockCb).toBeCalledWith("done");
});
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Unit Testing with Jest application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Unit Testing with Jest operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Unit Testing with Jest configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Unit Testing with Jest event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Unit Testing with Jest with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Unit Testing with Jest performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Unit Testing with Jest failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Unit Testing with Jest data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Unit Testing with Jest state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Unit Testing with Jest logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Unit Testing with Jest files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Unit Testing with Jest connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Unit Testing with Jest.

*(Challenge question for self-study and practical project implementation.)*

