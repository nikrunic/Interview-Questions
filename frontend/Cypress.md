# Cypress & E2E Testing Interview Questions

This document contains interview questions focused on Cypress, End-to-End (E2E) testing, and integration testing frameworks.

## Basic (Easy)

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
\n## Additional Depth (Architectural Focus)\n
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
