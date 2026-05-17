# Authentication & Authorization Interview Questions

This document contains interview questions focused on web security, authentication patterns (JWT, OAuth2), and session management.

## Basic (Easy)

### 1. What is the difference between Authentication and Authorization?
**Answer:** 
**The Core Concept:**
Authentication verifies who a user is, while Authorization verifies what they have access to.

**Key Details:**
- Authentication involves logging in with credentials (passwords, biometrics).
- Authorization checks permissions or roles to grant or deny access to resources.

**Example:** Logging in is Authentication; being allowed to view an admin dashboard is Authorization.

**Reference:** [Auth0: Authentication vs Authorization](https://auth0.com/docs/get-started/identity-fundamentals/authentication-and-authorization)

---

### 2. What is a JSON Web Token (JWT)?
**Answer:** 
**The Core Concept:**
JWT is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.

**Key Details:**
- It is commonly used for stateless authentication.
- A JWT consists of three parts: Header, Payload, and Signature, separated by dots (`.`).

**Example:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

**Reference:** [JWT Introduction](https://jwt.io/introduction)

---

### 3. What is OAuth2?
**Answer:** 
**The Core Concept:**
OAuth2 is an industry-standard protocol for authorization.

**Key Details:**
- It allows third-party applications to grant limited access to an HTTP service without sharing user credentials.
- It relies on access tokens and refresh tokens.

**Example:** "Log in with Google" or "Log in with GitHub" buttons use OAuth2.

**Reference:** [OAuth 2.0](https://oauth.net/2/)

---
\n## Additional Depth (Architectural Focus)\n
### 4. What are the security implications of storing JWTs in localStorage versus HttpOnly cookies?
**Answer:** 
**The Core Concept:**
Storing JWTs in localStorage makes them accessible via JavaScript, leaving the application vulnerable to Cross-Site Scripting (XSS) attacks where malicious scripts can steal the token. HttpOnly cookies prevent JavaScript access, mitigating XSS risks but introducing Cross-Site Request Forgery (CSRF) vulnerabilities.

**Key Details:**
- To secure HttpOnly cookies against CSRF, you must implement Anti-CSRF tokens or use the `SameSite=Strict` cookie attribute.
- localStorage is often used for convenience in SPAs, but requires rigorous sanitization of all user inputs to prevent XSS.

**Example:** 
`Set-Cookie: token=jwt_here; HttpOnly; Secure; SameSite=Strict`

**Reference:** [Documentation](https://owasp.org/www-community/vulnerabilities/Cross-Site_Request_Forgery)

---
