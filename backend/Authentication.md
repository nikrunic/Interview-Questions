# Authentication & Authorization Interview Questions

This document contains 100 interview questions focused on web security, authentication patterns (JWT, OAuth2), and session management.

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

### 4. What is OpenID Connect (OIDC)?
**Answer:** 
**The Core Concept:**
OIDC is an identity layer on top of OAuth 2.0 that lets clients verify end-user identity and obtain basic profile claims.

**Key Details:**
- OAuth 2.0 alone is authorization-only; OIDC adds standardized ID tokens (JWT) and a UserInfo endpoint.
- Common flows: Authorization Code with PKCE for SPAs and native apps.

**Example:** 
`GET /.well-known/openid-configuration`

**Reference:** [Documentation](https://openid.net/connect/)

---
### 5. What is SAML?
**Answer:** 
**The Core Concept:**
Security Assertion Markup Language is an XML-based standard for exchanging authentication and authorization data between an IdP and a Service Provider.

**Key Details:**
- Common in enterprise SSO (Okta, Azure AD federation to legacy apps).
- Uses signed XML assertions rather than bearer tokens like JWT.

**Example:** 
`SP-initiated SSO POST to /saml/acs`

**Reference:** [Documentation](https://wiki.oasis-open.org/security/FrontPage)

---
### 6. What is Single Sign-On (SSO)?
**Answer:** 
**The Core Concept:**
SSO allows a user to authenticate once and access multiple applications without re-entering credentials.

**Key Details:**
- Implemented via shared session cookies, SAML, or OIDC federation.
- Central IdP issues tokens or assertions consumed by relying parties.

**Example:** 
`Login once at login.company.com; access Jira, Confluence, and internal APIs`

**Reference:** [Documentation](https://auth0.com/docs/authenticate/single-sign-on)

---
### 7. What are HttpOnly and Secure cookie flags?
**Answer:** 
**The Core Concept:**
HttpOnly prevents JavaScript from reading the cookie; Secure ensures the cookie is sent only over HTTPS.

**Key Details:**
- Together they reduce XSS token theft and downgrade attacks.
- Use SameSite (Lax/Strict) to mitigate CSRF on cookie-based sessions.

**Example:** 
`Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Lax`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

---
### 8. What is a server-side session?
**Answer:** 
**The Core Concept:**
The server stores session state (user id, roles) keyed by a session ID sent to the client, usually in a cookie.

**Key Details:**
- Stateful: requires session store (Redis, SQL) and sticky sessions or shared store in scale-out.
- Invalidating a session immediately logs the user out everywhere that session is used.

**Example:** 
`express-session with Redis store`

**Reference:** [Documentation](https://owasp.org/www-community/Session_Management_Cheat_Sheet)

---
### 9. What is password hashing and why not use MD5?
**Answer:** 
**The Core Concept:**
Password hashing is a one-way transform designed to be slow and salted so stolen hashes cannot be reversed quickly.

**Key Details:**
- Use adaptive algorithms: bcrypt, scrypt, or Argon2id—not MD5/SHA1.
- Each password gets a unique random salt stored with the hash.

**Example:** 
`bcrypt.hash(password, 12)`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---
### 10. What is bcrypt's cost factor?
**Answer:** 
**The Core Concept:**
The cost (work factor) controls how many iterations bcrypt runs, increasing CPU time for each hash attempt.

**Key Details:**
- Increase cost over years as hardware improves (e.g., 10–12 for web apps).
- Trade-off: higher cost improves security but slows login under load.

**Example:** 
`bcrypt.hashSync(pw, 12)`

**Reference:** [Documentation](https://en.wikipedia.org/wiki/Bcrypt)

---
### 11. What is Argon2?
**Answer:** 
**The Core Concept:**
Argon2 won the Password Hashing Competition and is memory-hard, resisting GPU/ASIC cracking better than bcrypt alone.

**Key Details:**
- Variants: Argon2d, Argon2i, Argon2id (recommended for passwords).
- Tune memory, iterations, and parallelism per OWASP guidance.

**Example:** 
`argon2.hash(password)`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---
### 12. What is Multi-Factor Authentication (MFA)?
**Answer:** 
**The Core Concept:**
MFA requires two or more factors: something you know, have, or are.

**Key Details:**
- TOTP apps, WebAuthn/FIDO2 keys, and SMS (weaker) are common second factors.
- Enforce MFA for admin and privileged accounts at minimum.

**Example:** 
`TOTP code after password at login`

**Reference:** [Documentation](https://www.nist.gov/itl/topic/cybersecurity/multi-factor-authentication)

---
### 13. What is TOTP?
**Answer:** 
**The Core Concept:**
Time-based One-Time Password generates 6-digit codes from a shared secret and current time window.

**Key Details:**
- Used by Google Authenticator, Authy; RFC 6238.
- Server and client must have reasonably synchronized clocks.

**Example:** 
`speakeasy.totp.verify({ secret, token })`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc6238)

---
### 14. What is WebAuthn / FIDO2?
**Answer:** 
**The Core Concept:**
WebAuthn is a W3C API for passwordless or second-factor authentication using public-key cryptography bound to origins.

**Key Details:**
- Private key stays on authenticator (security key, platform passkey); server stores public key only.
- Resistant to phishing because credentials are origin-scoped.

**Example:** 
`navigator.credentials.create({ publicKey: options })`

**Reference:** [Documentation](https://webauthn.guide/)

---
### 15. What is Cross-Site Scripting (XSS)?
**Answer:** 
**The Core Concept:**
XSS injects malicious scripts into pages viewed by other users, often stealing cookies or tokens accessible to JavaScript.

**Key Details:**
- Stored, reflected, and DOM-based XSS are common variants.
- Mitigate with output encoding, CSP, HttpOnly cookies, and input validation.

**Example:** 
`<script>fetch('/steal?c='+document.cookie)</script>`

**Reference:** [Documentation](https://owasp.org/www-community/attacks/xss/)

---
### 16. What is Cross-Site Request Forgery (CSRF)?
**Answer:** 
**The Core Concept:**
CSRF tricks a logged-in user's browser into submitting unwanted requests using their existing session cookies.

**Key Details:**
- Mitigate with anti-CSRF tokens, SameSite cookies, and verifying Origin/Referer.
- State-changing operations should never rely on GET alone.

**Example:** 
`Hidden form POST from evil.com while user is logged into bank.com`

**Reference:** [Documentation](https://owasp.org/www-community/attacks/csrf)

---
### 17. What is CORS?
**Answer:** 
**The Core Concept:**
Cross-Origin Resource Sharing is a browser mechanism allowing servers to declare which origins may read responses from XHR/fetch.

**Key Details:**
- Preflight OPTIONS for non-simple requests with custom headers.
- CORS is not a substitute for authentication; it only relaxes same-origin policy for browsers.

**Example:** 
`Access-Control-Allow-Origin: https://app.example.com`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---
### 18. What is the OAuth 2.0 Authorization Code flow?
**Answer:** 
**The Core Concept:**
The user authenticates at the IdP; the client exchanges a short-lived authorization code for tokens at the token endpoint.

**Key Details:**
- Use PKCE for public clients (SPAs, mobile) to prevent code interception.
- Never expose client secrets in browser or mobile apps.

**Example:** 
`code -> POST /token with code_verifier`

**Reference:** [Documentation](https://oauth.net/2/grant-types/authorization-code/)

---
### 19. What is PKCE?
**Answer:** 
**The Core Concept:**
Proof Key for Code Exchange adds a code_verifier/challenge pair so stolen authorization codes cannot be exchanged without the verifier.

**Key Details:**
- Required best practice for public OAuth clients.
- Uses S256 challenge method in modern implementations.

**Example:** 
`code_challenge = BASE64URL(SHA256(code_verifier))`

**Reference:** [Documentation](https://oauth.net/2/pkce/)

---
### 20. What is a refresh token?
**Answer:** 
**The Core Concept:**
A long-lived token used only at the token endpoint to obtain new access tokens without re-prompting the user.

**Key Details:**
- Store securely; rotate on use; revoke on logout or compromise.
- Some providers use refresh token rotation to detect theft.

**Example:** 
`POST /token grant_type=refresh_token`

**Reference:** [Documentation](https://oauth.net/2/refresh-tokens/)

---
### 21. What is an access token?
**Answer:** 
**The Core Concept:**
A credential representing authorization to access resources, usually short-lived and sent as Bearer in Authorization header.

**Key Details:**
- OAuth access tokens may be opaque or JWT format depending on provider.
- Validate audience, issuer, expiry, and scopes on every API call.

**Example:** 
`Authorization: Bearer eyJhbGciOi...`

**Reference:** [Documentation](https://oauth.net/2/access-tokens/)

---
### 22. What are JWT claims?
**Answer:** 
**The Core Concept:**
Claims are name/value pairs in the JWT payload (registered, public, or private) describing the subject and token metadata.

**Key Details:**
- Common registered claims: sub, iss, aud, exp, iat, nbf.
- Custom claims hold roles, permissions, or tenant id—keep payloads small.

**Example:** 
`{"sub":"user123","role":"admin","exp":1710000000}`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc7519#section-4)

---
### 23. How do you validate a JWT?
**Answer:** 
**The Core Concept:**
Verify signature with the correct key, then validate iss, aud, exp, and optionally custom claims before trusting it.

**Key Details:**
- Fetch signing keys from JWKS URI for asymmetric algorithms (RS256).
- Reject alg=none and unexpected algorithms (algorithm confusion attacks).

**Example:** 
`jwt.verify(token, publicKey, { algorithms: ['RS256'], audience, issuer })`

**Reference:** [Documentation](https://auth0.com/docs/secure/tokens/json-web-tokens/validate-json-web-tokens)

---
### 24. What is RBAC?
**Answer:** 
**The Core Concept:**
Role-Based Access Control assigns permissions to roles and roles to users.

**Key Details:**
- Check roles at API and UI layers.
- Prefer fine-grained permissions over god roles like superadmin.

**Example:** 
`role: editor -> can publish posts`

**Reference:** [Documentation](https://en.wikipedia.org/wiki/Role-based_access_control)

---
### 25. What is ABAC?
**Answer:** 
**The Core Concept:**
Attribute-Based Access Control decides access using attributes of user, resource, and environment.

**Key Details:**
- More flexible than RBAC for complex policies.
- Often implemented with policy engines (OPA, Cedar).

**Example:** 
`allow if user.department == resource.ownerDept`

**Reference:** [Documentation](https://en.wikipedia.org/wiki/Attribute-based_access_control)

---
### 26. What is the principle of least privilege?
**Answer:** 
**The Core Concept:**
Grant only the minimum permissions required to perform a task.

**Key Details:**
- Apply to users, service accounts, and API keys.
- Review and revoke unused access regularly.

**Example:** 
`read-only DB user for reporting service`

**Reference:** [Documentation](https://csrc.nist.gov/glossary/term/least_privilege)

---
### 27. What is an API key?
**Answer:** 
**The Core Concept:**
A static secret identifying a client application, often sent in headers or query strings.

**Key Details:**
- Rotate keys; never commit to repos; scope per environment.
- Weaker than OAuth for user delegation—use for server-to-server.

**Example:** 
`X-API-Key: sk_live_...`

**Reference:** [Documentation](https://cloud.google.com/docs/authentication/api-keys)

---
### 28. What is HMAC authentication?
**Answer:** 
**The Core Concept:**
Hash-based Message Authentication Code signs requests with a shared secret to prove integrity and origin.

**Key Details:**
- Include timestamp/nonce to prevent replay.
- Common in webhooks (Stripe-Signature).

**Example:** 
`HMAC-SHA256(secret, timestamp + body)`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc2104)

---
### 29. What is mutual TLS (mTLS)?
**Answer:** 
**The Core Concept:**
Both client and server present X.509 certificates during TLS handshake for mutual authentication.

**Key Details:**
- Used in service meshes and zero-trust internal APIs.
- Requires certificate lifecycle management.

**Example:** 
`Envoy upstream TLS with client cert`

**Reference:** [Documentation](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/)

---
### 30. What is a security token service (STS)?
**Answer:** 
**The Core Concept:**
A component that issues, validates, and exchanges security tokens (SAML, JWT).

**Key Details:**
- Azure AD, Okta, and Keycloak act as STS/IdP.
- Federation trusts between STS instances enable SSO.

**Example:** 
`AWS STS AssumeRole`

**Reference:** [Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

---
### 31. What is token revocation?
**Answer:** 
**The Core Concept:**
Invalidating tokens before natural expiry so compromised credentials stop working.

**Key Details:**
- Maintain a denylist/blocklist or use short-lived tokens + refresh rotation.
- JWTs are hard to revoke without server-side session or introspection.

**Example:** 
`POST /revoke with token`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc7009)

---
### 32. What is OAuth token introspection?
**Answer:** 
**The Core Concept:**
RFC 7662 endpoint where resource servers ask the authorization server if a token is active and get metadata.

**Key Details:**
- Useful for opaque tokens.
- Adds latency—cache introspection results briefly.

**Example:** 
`POST /introspect token=...`

**Reference:** [Documentation](https://oauth.net/2/token-introspection/)

---
### 33. What is the OAuth Client Credentials grant?
**Answer:** 
**The Core Concept:**
Machine-to-machine flow where the client authenticates with client_id/secret and receives an access token.

**Key Details:**
- No user context in token.
- Use for background jobs and microservice calls.

**Example:** 
`grant_type=client_credentials`

**Reference:** [Documentation](https://oauth.net/2/grant-types/client-credentials/)

---
### 34. What is the Resource Owner Password Credentials grant?
**Answer:** 
**The Core Concept:**
Legacy grant exchanging username/password for tokens directly at the token endpoint.

**Key Details:**
- Deprecated for most use cases; avoid in new apps.
- Cannot support MFA cleanly; high phishing risk.

**Example:** 
`grant_type=password (discouraged)`

**Reference:** [Documentation](https://oauth.net/2/grant-types/password/)

---
### 35. What is the Implicit grant?
**Answer:** 
**The Core Concept:**
Historically returned tokens in URL fragment from authorize endpoint without code exchange.

**Key Details:**
- Removed from OAuth 2.1; use Authorization Code + PKCE instead.
- Tokens exposed in browser history.

**Example:** 
`response_type=token (legacy)`

**Reference:** [Documentation](https://oauth.net/2/grant-types/implicit/)

---
### 36. What is OIDC UserInfo endpoint?
**Answer:** 
**The Core Concept:**
Returns claims about the authenticated end-user when called with a valid access token.

**Key Details:**
- Complements ID token for additional profile fields.
- Must validate token before returning PII.

**Example:** 
`GET /userinfo Authorization: Bearer ...`

**Reference:** [Documentation](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo)

---
### 37. What is an ID token vs access token?
**Answer:** 
**The Core Concept:**
ID token proves authentication (for the client); access token authorizes API access (for the resource server).

**Key Details:**
- ID token is always JWT in OIDC.
- Do not send ID tokens to APIs expecting access tokens.

**Example:** 
`id_token aud=client_id; access_token aud=api`

**Reference:** [Documentation](https://auth0.com/docs/secure/tokens/id-tokens)

---
### 38. What is audience (aud) claim?
**Answer:** 
**The Core Concept:**
Identifies the intended recipient of the token; APIs must reject tokens with wrong aud.

**Key Details:**
- Prevents token replay across different APIs.
- Configure per API resource identifier.

**Example:** 
`"aud": "https://api.myapp.com"`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3)

---
### 39. What is token binding?
**Answer:** 
**The Core Concept:**
Cryptographically binding tokens to a TLS connection or device key to reduce theft usefulness.

**Key Details:**
- Limited browser support historically.
- WebAuthn/passkeys achieve similar goals.

**Example:** 
`Bound access token + DPoP proof`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc9449)

---
### 40. What is DPoP?
**Answer:** 
**The Core Concept:**
Demonstrating Proof-of-Possession binds requests to a public key the client proves possession of.

**Key Details:**
- Mitigates bearer token replay if token is stolen.
- Send DPoP header with signed HTTP request.

**Example:** 
`DPoP: eyJhbGciOiES256...`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc9449)

---
### 41. What is a nonce in OIDC?
**Answer:** 
**The Core Concept:**
Random value in auth request bound to ID token to prevent replay attacks.

**Key Details:**
- Validate nonce in ID token matches auth request.
- Store nonce server-side during login.

**Example:** 
`nonce=random123 in authorize URL`

**Reference:** [Documentation](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest)

---
### 42. What is state parameter in OAuth?
**Answer:** 
**The Core Concept:**
Opaque value returned unchanged to prevent CSRF on the OAuth callback.

**Key Details:**
- Generate cryptographically random state per request.
- Validate state matches session before exchanging code.

**Example:** 
`state=xyz in authorize & callback`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.1)

---
### 43. What is scope in OAuth?
**Answer:** 
**The Core Concept:**
Space-delimited list of permissions the client requests (e.g., read:users).

**Key Details:**
- Request minimum scopes.
- Resource server enforces scopes on each endpoint.

**Example:** 
`scope=openid profile email`

**Reference:** [Documentation](https://oauth.net/2/scope/)

---
### 44. What is consent screen?
**Answer:** 
**The Core Concept:**
UI where users approve scopes requested by a third-party client.

**Key Details:**
- Required for third-party apps.
- Show clear app name and requested permissions.

**Example:** 
`Allow GitHub Actions to read your repos?`

**Reference:** [Documentation](https://oauth.net/2/)

---
### 45. What is a confidential vs public OAuth client?
**Answer:** 
**The Core Concept:**
Confidential clients can keep secrets (server apps); public clients cannot (SPAs, mobile).

**Key Details:**
- Public clients must use PKCE.
- Never embed client secrets in mobile/SPA.

**Example:** 
`native app = public client`

**Reference:** [Documentation](https://oauth.net/2/client-types/)

---
### 46. What is ASP.NET Core Identity?
**Answer:** 
**The Core Concept:**
Membership system adding login UI, user store, password hashing, and 2FA to ASP.NET apps.

**Key Details:**
- Integrates with EF Core for user tables.
- Extend with external providers (Google, Microsoft).

**Example:** 
`AddIdentity<ApplicationUser>()`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity)

---
### 47. What is [Authorize] attribute?
**Answer:** 
**The Core Concept:**
Declares that a controller/action requires authenticated user and optional roles/policies.

**Key Details:**
- Returns 401 if not authenticated, 403 if forbidden.
- Use policy-based authorization for complex rules.

**Example:** 
`[Authorize(Roles = "Admin")]`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/simple)

---
### 48. What is policy-based authorization in ASP.NET?
**Answer:** 
**The Core Concept:**
Authorization policies encapsulate requirements (claims, roles, custom handlers).

**Key Details:**
- Register policies in Program.cs.
- Prefer over hard-coded role checks in controllers.

**Example:** 
`options.AddPolicy("CanEdit", p => p.RequireClaim(...))`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/policies)

---
### 49. What is claims-based identity?
**Answer:** 
**The Core Concept:**
Identity represented as a set of claims (type/value pairs) about the user.

**Key Details:**
- Claims map to permissions better than flat roles.
- Issued by IdP in SAML/OIDC/JWT.

**Example:** 
`ClaimTypes.Role = Admin`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/dotnet/framework/security/claims-based-identity-model-for-windows)

---
### 50. What is Azure AD / Entra ID?
**Answer:** 
**The Core Concept:**
Microsoft cloud IdP providing SSO, MFA, conditional access, and app registrations.

**Key Details:**
- Issues JWT access tokens for Microsoft Graph and custom APIs.
- Integrate via MSAL libraries.

**Example:** 
`Microsoft.Identity.Web in ASP.NET`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/entra/identity/)

---
### 51. What is MSAL?
**Answer:** 
**The Core Concept:**
Microsoft Authentication Library acquires tokens from Entra ID and other Microsoft identity platforms.

**Key Details:**
- Handles token cache and silent refresh.
- Use correct authority and scopes.

**Example:** 
`AcquireTokenSilent(scopes)`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/entra/msal/)

---
### 52. What is AWS Cognito?
**Answer:** 
**The Core Concept:**
Managed user directory and OAuth/OIDC provider for web and mobile apps.

**Key Details:**
- User Pools for authentication; Identity Pools for AWS credentials.
- Triggers (Lambda) customize auth flows.

**Example:** 
`amazon-cognito-identity-js`

**Reference:** [Documentation](https://docs.aws.amazon.com/cognito/)

---
### 53. What is Keycloak?
**Answer:** 
**The Core Concept:**
Open-source IdP supporting OIDC, SAML, social login, and user federation.

**Key Details:**
- Self-hosted alternative to commercial IdPs.
- Realms isolate tenants.

**Example:** 
`docker run quay.io/keycloak/keycloak`

**Reference:** [Documentation](https://www.keycloak.org/)

---
### 54. What is Auth0 / Okta?
**Answer:** 
**The Core Concept:**
Commercial identity platforms providing hosted login, MFA, and social connections.

**Key Details:**
- Universal Login redirects to hosted pages.
- Rules/actions customize token claims.

**Example:** 
`auth0.loginWithRedirect()`

**Reference:** [Documentation](https://auth0.com/docs)

---
### 55. What is password salting?
**Answer:** 
**The Core Concept:**
Random data combined with password before hashing so identical passwords produce different hashes.

**Key Details:**
- Salt stored alongside hash.
- Prevents rainbow table attacks.

**Example:** 
`salt = randomBytes(16)`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---
### 56. What is pepper?
**Answer:** 
**The Core Concept:**
Secret added to passwords before hashing, stored separately from the database (e.g., HSM).

**Key Details:**
- Extra layer if DB is stolen.
- Rotation requires rehashing all passwords.

**Example:** 
`hash(password + pepper)`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---
### 57. What is account lockout?
**Answer:** 
**The Core Concept:**
Temporarily blocking login after repeated failed attempts.

**Key Details:**
- Balance security vs DoS on known usernames.
- Use exponential backoff and CAPTCHA.

**Example:** 
`lock after 5 failures for 15 min`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---
### 58. What is credential stuffing?
**Answer:** 
**The Core Concept:**
Attack using leaked username/password pairs from other breaches.

**Key Details:**
- Mitigate with MFA, breach password lists, rate limiting.
- Detect impossible travel and velocity.

**Example:** 
`1M login attempts with stolen combos`

**Reference:** [Documentation](https://owasp.org/www-community/attacks/Credential_stuffing)

---
### 59. What is brute force attack?
**Answer:** 
**The Core Concept:**
Systematically guessing passwords or tokens until success.

**Key Details:**
- Rate limit, CAPTCHA, lockout, long secrets for tokens.
- Monitor failed login metrics.

**Example:** 
`try all 6-digit TOTP codes`

**Reference:** [Documentation](https://owasp.org/www-community/attacks/Brute_force_attack)

---
### 60. What is passwordless authentication?
**Answer:** 
**The Core Concept:**
Login without user-chosen passwords using magic links, WebAuthn, or OTP.

**Key Details:**
- Reduces password reuse risk.
- Protect email/SMS channels used for magic links.

**Example:** 
`Send magic link to email`

**Reference:** [Documentation](https://auth0.com/blog/what-is-passwordless-authentication/)

---
### 61. What is a magic link?
**Answer:** 
**The Core Concept:**
One-time URL sent to email that establishes a session when clicked.

**Key Details:**
- Short expiry; single use; bind to device fingerprint optionally.
- Vulnerable if email account is compromised.

**Example:** 
`https://app.com/auth/verify?token=one-time`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)

---
### 62. What is OTP via SMS?
**Answer:** 
**The Core Concept:**
One-time password sent by text message as second factor or primary login.

**Key Details:**
- Susceptible to SIM swap attacks.
- NIST discourages SMS for high assurance.

**Example:** 
`Your code is 482910`

**Reference:** [Documentation](https://pages.nist.gov/800-63-3/sp800-63b.html)

---
### 63. What is CAPTCHA?
**Answer:** 
**The Core Concept:**
Challenge distinguishing humans from bots during login or registration.

**Key Details:**
- Use risk-based step-up instead of always-on CAPTCHA.
- reCAPTCHA v3 scores risk silently.

**Example:** 
`g-recaptcha-response token`

**Reference:** [Documentation](https://www.google.com/recaptcha/)

---
### 64. What is rate limiting for auth endpoints?
**Answer:** 
**The Core Concept:**
Throttling login, register, and password-reset to slow attacks.

**Key Details:**
- Per IP, per account, and global limits.
- Return generic errors to prevent user enumeration.

**Example:** 
`5 login attempts / minute / IP`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---
### 65. What is user enumeration?
**Answer:** 
**The Core Concept:**
Learning valid usernames via different error messages or timing.

**Key Details:**
- Use same response for bad user vs bad password.
- Constant-time comparisons where feasible.

**Example:** 
`Invalid username or password (always)`

**Reference:** [Documentation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account)

---
### 66. What is secure password reset flow?
**Answer:** 
**The Core Concept:**
Verify identity via email link or MFA, issue one-time token, force session invalidation.

**Key Details:**
- Do not reveal if email exists.
- Expire tokens quickly.

**Example:** 
`POST /reset with token + new password`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)

---
### 67. What is session fixation?
**Answer:** 
**The Core Concept:**
Attacker sets victim's session ID before login; after login victim uses attacker's session.

**Key Details:**
- Regenerate session ID on login.
- Do not accept session IDs from URL.

**Example:** 
`req.session.regenerate()`

**Reference:** [Documentation](https://owasp.org/www-community/attacks/Session_fixation)

---
### 68. What is session hijacking?
**Answer:** 
**The Core Concept:**
Stealing a valid session ID via XSS, network sniffing, or malware.

**Key Details:**
- Use HTTPS, HttpOnly, Secure cookies.
- Short session lifetime and idle timeout.

**Example:** 
`stolen session cookie replay`

**Reference:** [Documentation](https://owasp.org/www-community/attacks/Session_hijacking_attack)

---
### 69. What is idle vs absolute session timeout?
**Answer:** 
**The Core Concept:**
Idle timeout logs out after inactivity; absolute timeout ends session after fixed duration regardless of activity.

**Key Details:**
- Use both for sensitive apps.
- Refresh tokens have similar absolute/idle concepts.

**Example:** 
`idle 30 min, absolute 8 hours`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

---
### 70. What is Content Security Policy (CSP)?
**Answer:** 
**The Core Concept:**
HTTP header restricting script/style sources to reduce XSS impact.

**Key Details:**
- Start with report-only mode.
- Avoid inline scripts or use nonces.

**Example:** 
`Content-Security-Policy: default-src 'self'`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

---
### 71. What is Subresource Integrity (SRI)?
**Answer:** 
**The Core Concept:**
Hash attribute on script/link tags ensuring CDN files were not tampered with.

**Key Details:**
- Pair with trusted CDNs.
- Update hash when upgrading library versions.

**Example:** 
`integrity=sha384-...`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)

---
### 72. What is the SameSite cookie attribute?
**Answer:** 
**The Core Concept:**
Controls whether cookies are sent on cross-site requests (Strict, Lax, None).

**Key Details:**
- None requires Secure.
- Lax is default in modern browsers.

**Example:** 
`SameSite=Strict`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)

---
### 73. What is BFF (Backend for Frontend) pattern?
**Answer:** 
**The Core Concept:**
A server-side component handles OAuth and stores tokens; browser only gets session cookie.

**Key Details:**
- Avoids exposing tokens to SPA JavaScript.
- Simplifies PKCE and refresh handling.

**Example:** 
`Next.js route handlers exchange code for tokens`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)

---
### 74. What is zero trust for APIs?
**Answer:** 
**The Core Concept:**
Never trust network location; verify identity, device, and context on every request.

**Key Details:**
- mTLS, JWT validation, and continuous authorization.
- Micro-segmentation and least privilege.

**Example:** 
`service mesh with SPIFFE IDs`

**Reference:** [Documentation](https://www.nist.gov/publications/zero-trust-architecture)

---
### 75. What is SPIFFE/SPIRE?
**Answer:** 
**The Core Concept:**
Standards for workload identity (SVIDs) in distributed systems.

**Key Details:**
- Used with service meshes for mTLS identity.
- Alternative to shared secrets between services.

**Example:** 
`spiffe://trust.domain/workload`

**Reference:** [Documentation](https://spiffe.io/)

---
### 76. What is secrets management?
**Answer:** 
**The Core Concept:**
Storing API keys and passwords in vaults (Azure Key Vault, HashiCorp Vault) not in code.

**Key Details:**
- Inject at runtime via managed identity.
- Audit access and rotate automatically.

**Example:** 
`Azure Key Vault reference in App Service`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/azure/key-vault/)

---
### 77. What is OWASP ASVS?
**Answer:** 
**The Core Concept:**
Application Security Verification Standard checklist for secure auth/session design.

**Key Details:**
- Level 1/2/3 increasing rigor.
- Use in security reviews and RFPs.

**Example:** 
`V2 Authentication verification`

**Reference:** [Documentation](https://owasp.org/www-project-application-security-verification-standard/)

---
### 78. What is broken authentication?
**Answer:** 
**The Core Concept:**
OWASP Top 10 category covering weak credentials, session issues, and missing MFA.

**Key Details:**
- Includes insecure recovery and credential transport.
- Test with OWASP testing guide.

**Example:** 
`no lockout + weak session IDs`

**Reference:** [Documentation](https://owasp.org/Top10/)

---
### 79. What is broken access control?
**Answer:** 
**The Core Concept:**
Users acting outside their intended permissions (IDOR, privilege escalation).

**Key Details:**
- Enforce authorization server-side always.
- Do not rely on hidden URLs or UI-only checks.

**Example:** 
`change ?userId=2 to access others data`

**Reference:** [Documentation](https://owasp.org/Top10/)

---
### 80. What is IDOR?
**Answer:** 
**The Core Concept:**
Insecure Direct Object Reference: accessing objects by manipulating identifiers without authorization check.

**Key Details:**
- Use opaque IDs and server-side ownership checks.
- Test all CRUD endpoints.

**Example:** 
`GET /api/orders/999 not owned by user`

**Reference:** [Documentation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References)

---
### 81. What is privilege escalation?
**Answer:** 
**The Core Concept:**
Gaining higher permissions than assigned (horizontal or vertical).

**Key Details:**
- Validate role changes server-side.
- Separate admin interfaces and audit logs.

**Example:** 
`regular user calls admin API`

**Reference:** [Documentation](https://owasp.org/www-community/attacks/Privilege_escalation)

---
### 82. What is horizontal vs vertical access control?
**Answer:** 
**The Core Concept:**
Horizontal: same role, different user's data. Vertical: lower role accessing admin functions.

**Key Details:**
- Both require explicit checks.
- ABAC can model both.

**Example:** 
`user A reads user B profile`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

---
### 83. What is defense in depth for auth?
**Answer:** 
**The Core Concept:**
Multiple layers: MFA, WAF, rate limits, monitoring, short tokens, and secure cookies.

**Key Details:**
- No single control is sufficient.
- Assume breach and limit blast radius.

**Example:** 
`MFA + anomaly detection + short JWT`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---
### 84. What is security logging for auth?
**Answer:** 
**The Core Concept:**
Audit login success/failure, lockouts, password changes, and admin actions without logging secrets.

**Key Details:**
- Correlate with SIEM alerts.
- Never log passwords or full tokens.

**Example:** 
`log userId, ip, event=LoginFailed`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

---
### 85. What is anomaly detection for logins?
**Answer:** 
**The Core Concept:**
ML/rules detecting impossible travel, new device, or unusual time.

**Key Details:**
- Step-up MFA on risk.
- Reduce account takeover impact.

**Example:** 
`login from new country -> require 2FA`

**Reference:** [Documentation](https://auth0.com/docs/secure/tokens/token-best-practices)

---
### 86. What is device fingerprinting?
**Answer:** 
**The Core Concept:**
Collecting browser/device signals to recognize returning clients.

**Key Details:**
- Privacy implications—disclose in policy.
- Supplement, not replace, strong auth.

**Example:** 
`canvas + UA + timezone hash`

**Reference:** [Documentation](https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks)

---
### 87. What is step-up authentication?
**Answer:** 
**The Core Concept:**
Re-prompting for stronger auth before sensitive actions (wire transfer, change email).

**Key Details:**
- Even if session is valid.
- Use recent auth time claim (auth_time).

**Example:** 
`confirm password before disable MFA`

**Reference:** [Documentation](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest)

---
### 88. What is auth_time claim?
**Answer:** 
**The Core Concept:**
OIDC claim indicating when the user last actively authenticated.

**Key Details:**
- Policies can require auth_time within N minutes.
- Used for step-up and session freshness.

**Example:** 
`"auth_time": 1710000000`

**Reference:** [Documentation](https://openid.net/specs/openid-connect-core-1_0.html#IDToken)

---
### 89. What is max_age parameter?
**Answer:** 
**The Core Concept:**
OIDC authorize parameter requiring authentication not older than specified seconds.

**Key Details:**
- Forces re-login if session too old.
- Pairs with auth_time validation.

**Example:** 
`max_age=300`

**Reference:** [Documentation](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest)

---
### 90. What is logout in OIDC?
**Answer:** 
**The Core Concept:**
RP-initiated logout redirects to IdP end_session_endpoint to clear SSO session.

**Key Details:**
- Also clear local tokens and cookies.
- Front-channel/back-channel logout for multiple apps.

**Example:** 
`GET /connect/endsession?id_token_hint=...`

**Reference:** [Documentation](https://openid.net/specs/openid-connect-session-1_0.html)

---
### 91. What is token storage in mobile apps?
**Answer:** 
**The Core Concept:**
Use secure enclave/Keychain (iOS) and Keystore (Android); avoid SharedPreferences/plain files.

**Key Details:**
- Use short-lived access tokens.
- Certificate pinning for API calls.

**Example:** 
`Expo SecureStore`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Mobile_Application_Security_Cheat_Sheet.html)

---
### 92. What is certificate pinning?
**Answer:** 
**The Core Concept:**
App only trusts specific server certificate/public key, mitigating rogue CA MITM.

**Key Details:**
- Maintenance burden on cert rotation.
- Use sparingly with backup pins.

**Example:** 
`TrustKit pinned domains`

**Reference:** [Documentation](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)

---
### 93. What is OAuth for native apps?
**Answer:** 
**The Core Concept:**
Use system browser (ASWebAuthenticationSession) and PKCE; no embedded WebViews.

**Key Details:**
- Redirect to custom URI scheme or app links.
- Follow RFC 8252 best practices.

**Example:** 
`myapp://callback?code=...`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc8252)

---
### 94. What is rotating refresh tokens?
**Answer:** 
**The Core Concept:**
Issuing new refresh token on each refresh and invalidating old one to detect theft.

**Key Details:**
- Reuse detection revokes token family.
- Auth0 and Azure AD support rotation.

**Example:** 
`refresh returns new refresh_token`

**Reference:** [Documentation](https://auth0.com/docs/secure/tokens/refresh-tokens/refresh-token-rotation)

---
### 95. What is JWT algorithm confusion attack?
**Answer:** 
**The Core Concept:**
Server accepts HS256 with public key as HMAC secret if misconfigured.

**Key Details:**
- Explicitly allow only expected algorithms.
- Use asymmetric keys for multi-service.

**Example:** 
`alg: HS256 with RSA pub key as secret`

**Reference:** [Documentation](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/)

---
### 96. What is jti claim?
**Answer:** 
**The Core Concept:**
JWT ID—a unique identifier for the token useful for replay prevention and revocation lists.

**Key Details:**
- Store jti until exp for one-time tokens.
- Pair with short expiry.

**Example:** 
`"jti": "a1b2c3"`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.7)

---
### 97. What is sliding vs absolute JWT expiry?
**Answer:** 
**The Core Concept:**
Absolute: fixed exp. Sliding: extend session on activity (usually via refresh tokens).

**Key Details:**
- Pure JWTs are absolute unless paired with refresh.
- Balance UX and security.

**Example:** 
`exp = now + 15min`

**Reference:** [Documentation](https://auth0.com/docs/secure/tokens/access-tokens)

---
### 98. What is hybrid flow in OIDC?
**Answer:** 
**The Core Concept:**
Returns authorization code and tokens from authorize endpoint (legacy).

**Key Details:**
- Rarely used today.
- Prefer standard code + PKCE.

**Example:** 
`response_type=code id_token token`

**Reference:** [Documentation](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth)

---
### 99. What is federated identity?
**Answer:** 
**The Core Concept:**
Trusting external IdP for authentication instead of local password database.

**Key Details:**
- SAML/OIDC links corporate directory to SaaS.
- Provision users via SCIM.

**Example:** 
`Login with Microsoft work account`

**Reference:** [Documentation](https://en.wikipedia.org/wiki/Federated_identity)

---
### 100. What is SCIM?
**Answer:** 
**The Core Concept:**
System for Cross-domain Identity Management protocol for automating user provisioning.

**Key Details:**
- Create/update/disable users in SaaS from IdP.
- Reduces manual account lifecycle errors.

**Example:** 
`POST /Users to SaaS SCIM endpoint`

**Reference:** [Documentation](https://scim.cloud/)

---
### 101. What is Just-In-Time (JIT) provisioning?
**Answer:** 
**The Core Concept:**
Creating user account on first SSO login from IdP claims.

**Key Details:**
- Map groups to roles.
- Validate signed assertions.

**Example:** 
`first SAML login creates local user`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/how-to-connect-fed-managed-accounts)

---
### 102. What is LDAP / Active Directory auth?
**Answer:** 
**The Core Concept:**
Directory protocol for bind (authenticate) and search operations in enterprises.

**Key Details:**
- Often behind VPN or LDAPS.
- Prefer modern OIDC federation over direct LDAP from cloud apps.

**Example:** 
`ldap.bind(userDN, password)`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)

---
### 103. What is Kerberos?
**Answer:** 
**The Core Concept:**
Network authentication protocol using tickets in Windows domains.

**Key Details:**
- Not used directly in most web APIs.
- Understanding helps with Windows SSO.

**Example:** 
`TGT and service tickets`

**Reference:** [Documentation](https://web.mit.edu/kerberos/)

---
### 104. What is NTLM?
**Answer:** 
**The Core Concept:**
Legacy Microsoft challenge-response auth still seen in Windows integrations.

**Key Details:**
- Disable where possible.
- Use Kerberos or modern protocols instead.

**Example:** 
`NTLM over HTTP (legacy)`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/windows-server/security/kerberos/ntlm-overview)

---
### 105. What is Windows Integrated Auth?
**Answer:** 
**The Core Concept:**
IIS/ASP.NET using Kerberos/NTLM for intranet SSO without login form.

**Key Details:**
- Negotiate scheme in browser.
- Not suitable for public internet clients.

**Example:** 
`Negotiate authentication`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth)

---
### 106. What is social login security?
**Answer:** 
**The Core Concept:**
Using Google/GitHub OAuth; validate state, use official SDKs, map minimal profile.

**Key Details:**
- Link social account to existing email carefully.
- Verify email_verified claim.

**Example:** 
`Google Sign-In button`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---
### 107. What is email verification?
**Answer:** 
**The Core Concept:**
Confirming user owns email before granting full access or sending sensitive mail.

**Key Details:**
- Signed, expiring verification links.
- Prevent disposable email abuse if needed.

**Example:** 
`GET /verify?token=...`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---
### 108. What is terms of service / privacy consent?
**Answer:** 
**The Core Concept:**
Recording user consent for GDPR compliance at registration.

**Key Details:**
- Store consent version and timestamp.
- Separate from marketing opt-in.

**Example:** 
`accepted_tos_version: 3`

**Reference:** [Documentation](https://gdpr.eu/)

---
### 109. What is GDPR impact on auth?
**Answer:** 
**The Core Concept:**
Right to erasure, data minimization, and lawful basis for processing identity data.

**Key Details:**
- Delete user PII on request.
- Document retention for audit logs.

**Example:** 
`DELETE /user/me`

**Reference:** [Documentation](https://gdpr.eu/what-is-gdpr/)

---
### 110. What is secrets in JWT?
**Answer:** 
**The Core Concept:**
JWTs are signed not encrypted—anyone with token can read payload unless JWE used.

**Key Details:**
- Never put passwords in JWT.
- Use encryption (JWE) only when necessary.

**Example:** 
`Bearer token decoded in jwt.io`

**Reference:** [Documentation](https://jwt.io/introduction)

---
### 111. What is JWE?
**Answer:** 
**The Core Concept:**
JSON Web Encryption encrypts JWT content for confidentiality.

**Key Details:**
- Heavier than JWS.
- Use HTTPS instead for transport in most cases.

**Example:** 
`encrypted JWT`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc7516)

---
### 112. What is JWKS?
**Answer:** 
**The Core Concept:**
JSON Web Key Set publishes public keys at /.well-known/jwks.json for token verification.

**Key Details:**
- Rotate keys with kid header.
- Cache keys with max-age.

**Example:** 
`GET /.well-known/jwks.json`

**Reference:** [Documentation](https://auth0.com/docs/secure/tokens/json-web-tokens/json-web-key-sets)

---
### 113. What is kid header in JWT?
**Answer:** 
**The Core Concept:**
Key ID indicating which key from JWKS signed the token.

**Key Details:**
- Support multiple active keys during rotation.
- Reject unknown kid.

**Example:** 
`"kid": "abc123"`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc7515#section-4.1.4)

---
### 114. What is clock skew for JWT?
**Answer:** 
**The Core Concept:**
Small leeway (e.g., 60s) when validating exp/nbf across distributed servers.

**Key Details:**
- Sync NTP on servers.
- Too much skew widens replay window.

**Example:** 
`clockTolerance: 60`

**Reference:** [Documentation](https://github.com/auth0/node-jsonwebtoken#usage)

---
### 115. What is secure headers for auth APIs?
**Answer:** 
**The Core Concept:**
HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy on auth endpoints.

**Key Details:**
- Prevent clickjacking login forms.
- Force HTTPS everywhere.

**Example:** 
`Strict-Transport-Security: max-age=31536000`

**Reference:** [Documentation](https://owasp.org/www-project-secure-headers/)

---
### 116. What is penetration testing auth?
**Answer:** 
**The Core Concept:**
Structured testing of login, session, OAuth, and password flows by security experts.

**Key Details:**
- Include MFA bypass attempts and IDOR.
- Fix findings before production.

**Example:** 
`OWASP WSTG auth chapters`

**Reference:** [Documentation](https://owasp.org/www-project-web-security-testing-guide/)

---
