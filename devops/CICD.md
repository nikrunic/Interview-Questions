# CI/CD Pipelines Interview Questions

This document contains interview questions focused on Continuous Integration, Continuous Deployment, and modern DevOps practices.

## Basic (Easy)

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
\n## Additional Depth (Architectural Focus)\n
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
