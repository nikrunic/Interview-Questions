# CI/CD Pipelines Interview Questions

This document contains interview questions focused on Continuous Integration, Continuous Deployment, and modern DevOps practices.

## Basic Questions

### 1. What does CI/CD stand for?
**Answer:** 
**The Core Concept:**
CI/CD stands for Continuous Integration and Continuous Deployment (or Continuous Delivery).

**Key Details:**
- It is a method to frequently deliver apps to customers by introducing automation into the stages of app development.
- It bridges the gap between development and operation activities and teams.

**Example:** Using GitHub Actions to automatically run tests and deploy to production upon a merge to `main`.

**Reference:** [Atlassian CI/CD](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)

---

---

---

### 2. What is Continuous Integration (CI)?
**Answer:** 
**The Core Concept:**
Continuous Integration is a coding philosophy and set of practices that drive development teams to implement small changes and check in code to version control repositories frequently.

**Key Details:**
- The primary goal is to establish a consistent and automated way to build, package, and test applications.
- This ensures that broken code does not get merged.

**Example:** Running unit tests on a Pull Request automatically before it can be merged.

**Reference:** [AWS Continuous Integration](https://aws.amazon.com/devops/continuous-integration/)

---

---

## Intermediate Questions

---

## Intermediate Questions

### 3. What is Continuous Deployment (CD)?
**Answer:** 
**The Core Concept:**
Continuous Deployment automates the release of a validated codebase directly to the production environment without manual intervention.

**Key Details:**
- It is the final stage of a mature CI/CD pipeline.
- It requires highly reliable automated testing, as any code that passes tests is immediately deployed to users.

**Example:** Pushing a commit to `main` instantly updates the live website on Vercel or AWS.

**Reference:** [Atlassian Continuous Deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)

---

## Additional Depth (Architectural Focus)


---

---

### 4. What is a deployment strategy and how does Blue-Green deployment work?
**Answer:** 
**The Core Concept:**
A deployment strategy defines how a new version of an application is rolled out to users to minimize downtime and risk. In a Blue-Green deployment, two identical production environments (Blue and Green) are maintained, but only one serves live traffic at a time.

**Key Details:**
- The new version is deployed to the idle environment (e.g., Green) and tested thoroughly. Once validated, the router or load balancer immediately switches all traffic from Blue to Green.
- This approach allows for near-zero downtime and provides an instant rollback mechanism by simply switching the router back to the original environment if issues occur.

**Example:** 
`AWS Route53 weighted routing changing from 100% Blue to 100% Green.`

**Reference:** [Documentation](https://aws.amazon.com/quickstart/architecture/blue-green-deployment/)

---

---

## Expert Questions

## Technical Questions

---

## Expert Questions

### 1. Write a YAML workflow for GitHub Actions executing Jest unit testing on PR.

**Example Solution:**
```yaml
name: Node CI Pipeline

on:
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Run Jest Tests
        run: npm test
```

---

### 2. Build a highly performant multi-stage Dockerfile for nesting Node.js environments.

**Example Solution:**
```dockerfile
# Stage 1: Build dependencies
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Serve
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=builder /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

---

## Technical Questions

### 1. Write a YAML workflow for GitHub Actions executing Jest unit testing on PR.

**Example Solution:**
```yaml
name: Node CI Pipeline

on:
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Run Jest Tests
        run: npm test
```

### 2. Build a highly performant multi-stage Dockerfile for nesting Node.js environments.

**Example Solution:**
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=builder /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### 3. Write a multi-stage Dockerfile utilizing target build parameters.

**Example Solution:**
```dockerfile
FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./

FROM base AS dev
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]

FROM base AS prod
RUN npm ci --only=production
COPY . .
USER node
CMD ["node", "server.js"]
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a CI/CD & DevOps Automation application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy CI/CD & DevOps Automation operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of CI/CD & DevOps Automation configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using CI/CD & DevOps Automation event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing CI/CD & DevOps Automation with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output CI/CD & DevOps Automation performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during CI/CD & DevOps Automation failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to CI/CD & DevOps Automation data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving CI/CD & DevOps Automation state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates CI/CD & DevOps Automation logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle CI/CD & DevOps Automation files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking CI/CD & DevOps Automation connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using CI/CD & DevOps Automation.

*(Challenge question for self-study and practical project implementation.)*

