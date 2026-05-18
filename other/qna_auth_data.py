# (title, concept, [details], example, url) — Authentication Q5+
AUTH_EXTRA = [
    (
        "What is OpenID Connect (OIDC)?",
        "OIDC is an identity layer on top of OAuth 2.0 that lets clients verify end-user identity and obtain basic profile claims.",
        [
            "OAuth 2.0 alone is authorization-only; OIDC adds standardized ID tokens (JWT) and a UserInfo endpoint.",
            "Common flows: Authorization Code with PKCE for SPAs and native apps.",
        ],
        "GET /.well-known/openid-configuration",
        "https://openid.net/connect/",
    ),
    (
        "What is SAML?",
        "Security Assertion Markup Language is an XML-based standard for exchanging authentication and authorization data between an IdP and a Service Provider.",
        [
            "Common in enterprise SSO (Okta, Azure AD federation to legacy apps).",
            "Uses signed XML assertions rather than bearer tokens like JWT.",
        ],
        "SP-initiated SSO POST to /saml/acs",
        "https://wiki.oasis-open.org/security/FrontPage",
    ),
    (
        "What is Single Sign-On (SSO)?",
        "SSO allows a user to authenticate once and access multiple applications without re-entering credentials.",
        [
            "Implemented via shared session cookies, SAML, or OIDC federation.",
            "Central IdP issues tokens or assertions consumed by relying parties.",
        ],
        "Login once at login.company.com; access Jira, Confluence, and internal APIs",
        "https://auth0.com/docs/authenticate/single-sign-on",
    ),
    (
        "What are HttpOnly and Secure cookie flags?",
        "HttpOnly prevents JavaScript from reading the cookie; Secure ensures the cookie is sent only over HTTPS.",
        [
            "Together they reduce XSS token theft and downgrade attacks.",
            "Use SameSite (Lax/Strict) to mitigate CSRF on cookie-based sessions.",
        ],
        "Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Lax",
        "https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies",
    ),
    (
        "What is a server-side session?",
        "The server stores session state (user id, roles) keyed by a session ID sent to the client, usually in a cookie.",
        [
            "Stateful: requires session store (Redis, SQL) and sticky sessions or shared store in scale-out.",
            "Invalidating a session immediately logs the user out everywhere that session is used.",
        ],
        "express-session with Redis store",
        "https://owasp.org/www-community/Session_Management_Cheat_Sheet",
    ),
    (
        "What is password hashing and why not use MD5?",
        "Password hashing is a one-way transform designed to be slow and salted so stolen hashes cannot be reversed quickly.",
        [
            "Use adaptive algorithms: bcrypt, scrypt, or Argon2id—not MD5/SHA1.",
            "Each password gets a unique random salt stored with the hash.",
        ],
        "bcrypt.hash(password, 12)",
        "https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html",
    ),
    (
        "What is bcrypt's cost factor?",
        "The cost (work factor) controls how many iterations bcrypt runs, increasing CPU time for each hash attempt.",
        [
            "Increase cost over years as hardware improves (e.g., 10–12 for web apps).",
            "Trade-off: higher cost improves security but slows login under load.",
        ],
        "bcrypt.hashSync(pw, 12)",
        "https://en.wikipedia.org/wiki/Bcrypt",
    ),
    (
        "What is Argon2?",
        "Argon2 won the Password Hashing Competition and is memory-hard, resisting GPU/ASIC cracking better than bcrypt alone.",
        [
            "Variants: Argon2d, Argon2i, Argon2id (recommended for passwords).",
            "Tune memory, iterations, and parallelism per OWASP guidance.",
        ],
        "argon2.hash(password)",
        "https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html",
    ),
    (
        "What is Multi-Factor Authentication (MFA)?",
        "MFA requires two or more factors: something you know, have, or are.",
        [
            "TOTP apps, WebAuthn/FIDO2 keys, and SMS (weaker) are common second factors.",
            "Enforce MFA for admin and privileged accounts at minimum.",
        ],
        "TOTP code after password at login",
        "https://www.nist.gov/itl/topic/cybersecurity/multi-factor-authentication",
    ),
    (
        "What is TOTP?",
        "Time-based One-Time Password generates 6-digit codes from a shared secret and current time window.",
        [
            "Used by Google Authenticator, Authy; RFC 6238.",
            "Server and client must have reasonably synchronized clocks.",
        ],
        "speakeasy.totp.verify({ secret, token })",
        "https://datatracker.ietf.org/doc/html/rfc6238",
    ),
    (
        "What is WebAuthn / FIDO2?",
        "WebAuthn is a W3C API for passwordless or second-factor authentication using public-key cryptography bound to origins.",
        [
            "Private key stays on authenticator (security key, platform passkey); server stores public key only.",
            "Resistant to phishing because credentials are origin-scoped.",
        ],
        "navigator.credentials.create({ publicKey: options })",
        "https://webauthn.guide/",
    ),
    (
        "What is Cross-Site Scripting (XSS)?",
        "XSS injects malicious scripts into pages viewed by other users, often stealing cookies or tokens accessible to JavaScript.",
        [
            "Stored, reflected, and DOM-based XSS are common variants.",
            "Mitigate with output encoding, CSP, HttpOnly cookies, and input validation.",
        ],
        "<script>fetch('/steal?c='+document.cookie)</script>",
        "https://owasp.org/www-community/attacks/xss/",
    ),
    (
        "What is Cross-Site Request Forgery (CSRF)?",
        "CSRF tricks a logged-in user's browser into submitting unwanted requests using their existing session cookies.",
        [
            "Mitigate with anti-CSRF tokens, SameSite cookies, and verifying Origin/Referer.",
            "State-changing operations should never rely on GET alone.",
        ],
        "Hidden form POST from evil.com while user is logged into bank.com",
        "https://owasp.org/www-community/attacks/csrf",
    ),
    (
        "What is CORS?",
        "Cross-Origin Resource Sharing is a browser mechanism allowing servers to declare which origins may read responses from XHR/fetch.",
        [
            "Preflight OPTIONS for non-simple requests with custom headers.",
            "CORS is not a substitute for authentication; it only relaxes same-origin policy for browsers.",
        ],
        "Access-Control-Allow-Origin: https://app.example.com",
        "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS",
    ),
    (
        "What is the OAuth 2.0 Authorization Code flow?",
        "The user authenticates at the IdP; the client exchanges a short-lived authorization code for tokens at the token endpoint.",
        [
            "Use PKCE for public clients (SPAs, mobile) to prevent code interception.",
            "Never expose client secrets in browser or mobile apps.",
        ],
        "code -> POST /token with code_verifier",
        "https://oauth.net/2/grant-types/authorization-code/",
    ),
    (
        "What is PKCE?",
        "Proof Key for Code Exchange adds a code_verifier/challenge pair so stolen authorization codes cannot be exchanged without the verifier.",
        [
            "Required best practice for public OAuth clients.",
            "Uses S256 challenge method in modern implementations.",
        ],
        "code_challenge = BASE64URL(SHA256(code_verifier))",
        "https://oauth.net/2/pkce/",
    ),
    (
        "What is a refresh token?",
        "A long-lived token used only at the token endpoint to obtain new access tokens without re-prompting the user.",
        [
            "Store securely; rotate on use; revoke on logout or compromise.",
            "Some providers use refresh token rotation to detect theft.",
        ],
        "POST /token grant_type=refresh_token",
        "https://oauth.net/2/refresh-tokens/",
    ),
    (
        "What is an access token?",
        "A credential representing authorization to access resources, usually short-lived and sent as Bearer in Authorization header.",
        [
            "OAuth access tokens may be opaque or JWT format depending on provider.",
            "Validate audience, issuer, expiry, and scopes on every API call.",
        ],
        "Authorization: Bearer eyJhbGciOi...",
        "https://oauth.net/2/access-tokens/",
    ),
    (
        "What are JWT claims?",
        "Claims are name/value pairs in the JWT payload (registered, public, or private) describing the subject and token metadata.",
        [
            "Common registered claims: sub, iss, aud, exp, iat, nbf.",
            "Custom claims hold roles, permissions, or tenant id—keep payloads small.",
        ],
        '{"sub":"user123","role":"admin","exp":1710000000}',
        "https://datatracker.ietf.org/doc/html/rfc7519#section-4",
    ),
    (
        "How do you validate a JWT?",
        "Verify signature with the correct key, then validate iss, aud, exp, and optionally custom claims before trusting it.",
        [
            "Fetch signing keys from JWKS URI for asymmetric algorithms (RS256).",
            "Reject alg=none and unexpected algorithms (algorithm confusion attacks).",
        ],
        "jwt.verify(token, publicKey, { algorithms: ['RS256'], audience, issuer })",
        "https://auth0.com/docs/secure/tokens/json-web-tokens/validate-json-web-tokens",
    ),
]
