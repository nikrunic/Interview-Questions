# Cypress & E2E Testing Interview Questions

This document contains interview questions focused on Cypress, End-to-End (E2E) testing, and integration testing frameworks.

## Basic Questions

### 1. What is Cypress?
**Answer:** 
**The Core Concept:**
Cypress is a next-generation frontend testing tool built for the modern web.

**Key Details:**
- It is primarily used for End-to-End (E2E) testing and integration testing.
- Unlike Selenium, Cypress executes in the same run loop as your application, providing native access to everything in the DOM.

**Example:** `cy.visit('/login'); cy.get('input[name=username]').type('user');`

**Reference:** [Cypress Overview](https://docs.cypress.io/guides/overview/why-cypress)

---

---

---

### 2. How is Cypress different from Selenium?
**Answer:** 
**The Core Concept:**
Cypress runs directly in the browser alongside your application, whereas Selenium operates outside the browser and sends remote commands across the network.

**Key Details:**
- Cypress provides automatic waiting, eliminating the need for arbitrary sleep or wait statements.
- Cypress is mostly limited to JavaScript and supports fewer browsers out-of-the-box compared to Selenium's vast ecosystem.

**Example:** Cypress automatically waits for elements to become visible before interacting with them.

**Reference:** [Cypress vs Selenium](https://docs.cypress.io/guides/overview/why-cypress#Cypress-is-unlike-and-better-than-other-testing-tools)

---

---

## Intermediate Questions

---

## Intermediate Questions

### 3. What is Time Travel in Cypress?
**Answer:** 
**The Core Concept:**
Time Travel is a feature that allows developers to see exactly what happened at each step of a test.

**Key Details:**
- Cypress takes snapshots of your application as tests run.
- You can hover over commands in the Command Log to see the state of the DOM at that specific point in time.

**Example:** Using the Cypress Test Runner UI to visually inspect a failed assertion step.

**Reference:** [Cypress Time Travel](https://docs.cypress.io/guides/core-concepts/cypress-app#Time-travel)

---

## Additional Depth (Architectural Focus)


---

---

### 4. How do you intercept and mock network requests in Cypress?
**Answer:** 
**The Core Concept:**
Cypress provides the `cy.intercept()` command to route, modify, and stub network requests at the browser network layer. This allows you to simulate various backend states (like 500 errors or specific JSON payloads) without relying on a live server environment.

**Key Details:**
- Unlike traditional mocking that replaces the `fetch` or `XHR` objects in the window, `cy.intercept()` works at the network level, capturing all requests regardless of how they are initiated.
- You can alias intercepts using `.as('name')` and use `cy.wait('@name')` to ensure the application has completed the network call before asserting on the UI.

**Example:** 
`cy.intercept('GET', '/api/users', { fixture: 'users.json' }).as('getUsers');`

**Reference:** [Documentation](https://docs.cypress.io/api/commands/intercept)

---

---

## Expert Questions

## Practice Questions

---

## Expert Questions

### 1. Write a Cypress test asserting the user login and routing flow.

**Example Solution:**
```javascript
describe('User Login Flow', () => {
  it('should fill form and redirect to dashboard', () => {
    cy.visit('/login');
    cy.get('input[name="email"]').type('user@example.com');
    cy.get('input[name="password"]').type('secret123');
    cy.get('button[type="submit"]').click();
    
    // Check path redirection
    cy.url().should('include', '/dashboard');
    cy.get('h1').should('contain', 'Welcome Back');
  });
});
```

---

### 2. Write a Cypress test that mocks network requests using interception tools.

**Example Solution:**
```javascript
describe('Mock API Test', () => {
  it('should show mock products on dashboard', () => {
    // Intercept GET request
    cy.intercept('GET', '/api/v1/products', {
      statusCode: 200,
      body: [
        { id: 1, name: 'Mock Product A', price: 99.99 },
        { id: 2, name: 'Mock Product B', price: 49.99 }
      ]
    }).as('getProducts');

    cy.visit('/dashboard');
    cy.wait('@getProducts');

    cy.get('.product-card').should('have.length', 2);
    cy.get('.product-card').first().should('contain', 'Mock Product A');
  });
});
```

---

## Practice Questions

### 1. Write a Cypress test asserting the user login and routing flow.

**Example Solution:**
```javascript
describe('User Login Flow', () => {
  it('should fill form and redirect to dashboard', () => {
    cy.visit('/login');
    cy.get('input[name="email"]').type('user@example.com');
    cy.get('input[name="password"]').type('secret123');
    cy.get('button[type="submit"]').click();
    
    cy.url().should('include', '/dashboard');
    cy.get('h1').should('contain', 'Welcome Back');
  });
});
```

### 2. Write a Cypress test that mocks network requests using interception tools.

**Example Solution:**
```javascript
describe('Mock API Test', () => {
  it('should show mock products on dashboard', () => {
    cy.intercept('GET', '/api/v1/products', {
      statusCode: 200,
      body: [
        { id: 1, name: 'Mock Product A', price: 99.99 },
        { id: 2, name: 'Mock Product B', price: 49.99 }
      ]
    }).as('getProducts');

    cy.visit('/dashboard');
    cy.wait('@getProducts');

    cy.get('.product-card').should('have.length', 2);
    cy.get('.product-card').first().should('contain', 'Mock Product A');
  });
});
```

### 3. Write a Cypress custom command helper to bypass login forms by stubbing JWT cookies.

**Example Solution:**
```javascript
Cypress.Commands.add('loginViaToken', (token) => {
  cy.setCookie('auth_token', token);
  cy.visit('/dashboard');
});

// Usage in test
it('should load dashboard instantly', () => {
  cy.loginViaToken('mock-jwt-token-123');
  cy.get('.profile').should('exist');
});
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a E2E Testing with Cypress application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy E2E Testing with Cypress operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of E2E Testing with Cypress configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using E2E Testing with Cypress event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing E2E Testing with Cypress with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output E2E Testing with Cypress performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during E2E Testing with Cypress failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to E2E Testing with Cypress data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving E2E Testing with Cypress state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates E2E Testing with Cypress logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle E2E Testing with Cypress files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking E2E Testing with Cypress connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using E2E Testing with Cypress.

*(Challenge question for self-study and practical project implementation.)*

