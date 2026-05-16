# REST API Interview Questions

This document contains a comprehensive list of REST API interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What does REST stand for?
**Answer:** REST stands for Representational State Transfer. It is an architectural style for designing networked applications.
**Example:** Designing a web service that uses HTTP protocols to get or send data.
**Reference:** [Wikipedia - Representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)

### 2. What is an API?
**Answer:** API stands for Application Programming Interface. It is a set of rules and protocols that allows one software application to communicate with another.
**Example:** Using the Google Maps API to embed a map on a website.
**Reference:** [MDN - APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

### 3. What are the common HTTP methods used in REST?
**Answer:** The most common HTTP methods are GET (retrieve data), POST (create new data), PUT/PATCH (update existing data), and DELETE (remove data).
**Example:** `GET /users` to fetch users, `POST /users` to create a user.
**Reference:** [MDN - HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

### 4. What is a URI vs a URL?
**Answer:** A URI (Uniform Resource Identifier) is a sequence of characters that identifies a resource. A URL (Uniform Resource Locator) is a type of URI that not only identifies a resource but also provides the means of locating it (e.g., via `https://`).
**Example:** URI: `urn:isbn:0451450523`. URL: `https://example.com/books/1`.
**Reference:** [Wikipedia - Uniform Resource Identifier](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)

### 5. What are HTTP Status Codes? Give examples.
**Answer:** Status codes are responses from the server indicating the outcome of a request. 2xx indicates success, 3xx redirection, 4xx client error, and 5xx server error.
**Example:** `200 OK`, `404 Not Found`, `500 Internal Server Error`.
**Reference:** [MDN - HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)


## Medium (30%)

### 6. What is the difference between PUT and PATCH?
**Answer:** PUT is used to replace an entire resource. If the resource doesn't exist, it can create it. PATCH is used to apply partial modifications to a resource.
**Example:** PUT replaces the whole user object. PATCH updates only the user's email address.
**Reference:** [MDN - PATCH method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)

### 7. What does "Statelessness" mean in REST?
**Answer:** Statelessness means that the server does not store any state about the client session on the server-side. Each request from the client must contain all the information necessary to understand the request, and cannot take advantage of any stored context on the server.
**Example:** A client must send a JWT token with every request to authenticate, because the server doesn't remember who is logged in.
**Reference:** [REST API Tutorial - What is REST](https://restfulapi.net/)

### 8. What are Idempotent methods?
**Answer:** An idempotent HTTP method is one where making multiple identical requests has the same effect on the server as making a single request. GET, PUT, DELETE, HEAD, and OPTIONS are idempotent. POST and PATCH are generally not.
**Example:** Calling `DELETE /users/1` multiple times results in the user still being deleted.
**Reference:** [MDN - Idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)

### 9. What is caching in REST APIs?
**Answer:** Caching is the ability to store responses temporarily so that subsequent requests for the same resource can be served faster without hitting the database or processing the request again. It uses headers like `Cache-Control` and `ETag`.
**Example:** `Cache-Control: max-age=3600` tells the client to cache the response for 1 hour.
**Reference:** [MDN - HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

### 10. How do you implement versioning in REST APIs?
**Answer:** Versioning can be implemented in the URI/URL path, as a query parameter, or in custom HTTP headers (like `Accept`).
**Example:** URI Versioning: `https://api.example.com/v1/users`
**Reference:** [REST API Tutorial - Versioning](https://restfulapi.net/versioning/)


## Hard (50%)

### 11. What is HATEOAS?
**Answer:** HATEOAS (Hypermedia As The Engine Of Application State) is a constraint of the REST application architecture. A HATEOAS-compliant API provides links to related resources in its responses, allowing the client to navigate the API dynamically without prior knowledge of its structure.
**Example:** A response for an account might include links to deposit, withdraw, or transfer funds.
**Reference:** [Wikipedia - HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

### 12. How do you secure a REST API?
**Answer:** Security is enforced via HTTPS (TLS/SSL) to encrypt data in transit, Authentication (OAuth2, JWT) to verify identity, Authorization (RBAC) to ensure access rights, input validation/sanitization to prevent SQL injection/XSS, and Rate Limiting to prevent DoS attacks.
**Example:** Enforcing an `Authorization: Bearer <token>` header.
**Reference:** [REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)

### 13. What is CORS and how does it apply to REST APIs?
**Answer:** Cross-Origin Resource Sharing (CORS) is a security feature implemented by browsers. It blocks web pages from making API requests to a different domain than the one that served the web page, unless the API explicitly allows it via CORS headers (like `Access-Control-Allow-Origin`).
**Example:** An API returning `Access-Control-Allow-Origin: *` to allow public access.
**Reference:** [MDN - CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

### 14. Explain Rate Limiting and Throttling.
**Answer:** Rate Limiting controls the number of requests a client can make to an API within a specific time window. Throttling is similar but often involves slowing down responses instead of outright rejecting them once a threshold is reached. This protects the server from being overwhelmed.
**Example:** Returning a `429 Too Many Requests` status code when a user exceeds 100 requests per minute.
**Reference:** [API Rate Limiting](https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/)

### 15. What are ETags and how do they work?
**Answer:** An ETag (Entity Tag) is an HTTP header used for web cache validation and conditional requests. The server generates an ETag based on the resource's content. On subsequent requests, the client sends `If-None-Match: <ETag>`. If the resource hasn't changed, the server returns `304 Not Modified`, saving bandwidth.
**Example:** `ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"`
**Reference:** [MDN - ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)

### 16. Describe pagination strategies for REST APIs.
**Answer:** 1. **Offset Pagination:** Uses `limit` and `offset` query parameters. Slow for large datasets. 2. **Keyset/Cursor Pagination:** Uses a pointer (`cursor`) to the last viewed item. Fast and robust for real-time data but harder to implement. 3. **Page-based Pagination:** Uses `page` and `size`.
**Example:** `GET /users?cursor=MjAxOS0wMS0xNFQxMzozMzo0Mlo`
**Reference:** [REST API Design - Pagination](https://restfulapi.net/pagination/)

### 17. How should you handle errors and format error responses?
**Answer:** APIs should use appropriate HTTP status codes (4xx/5xx) and return a standardized JSON payload detailing the error. The payload should include an error code, a human-readable message, and optionally a link to documentation.
**Example:** `{ "error": { "code": "VALIDATION_FAILED", "message": "Email is required" } }`
**Reference:** [REST Error Handling](https://restfulapi.net/http-status-codes/)

### 18. What is the Richardson Maturity Model?
**Answer:** It is a model that breaks down the principal elements of a REST approach into three steps (levels). Level 0 uses HTTP purely as a transport mechanism. Level 1 introduces resources (URIs). Level 2 introduces HTTP verbs (GET, POST). Level 3 introduces Hypermedia Controls (HATEOAS).
**Example:** True REST is considered Level 3.
**Reference:** [Martin Fowler - Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)

### 19. What is a Webhook and how does it relate to REST?
**Answer:** A webhook is a user-defined HTTP callback. While REST APIs require clients to poll for data (pull), webhooks allow the server to push data to the client's URL when an event occurs, reducing unnecessary network traffic.
**Example:** GitHub sending a POST request to your API when a repository is pushed to.
**Reference:** [Webhooks Guide](https://sendgrid.com/blog/whats-webhook/)

### 20. How do you manage long-running background tasks in a REST API?
**Answer:** Synchronous execution of long tasks causes timeouts. In REST, you should return a `202 Accepted` immediately with a `Location` header pointing to a status endpoint. The client polls the status endpoint until the background worker finishes the task and updates the status to "completed."
**Example:** Client uploads video -> Server returns 202 -> Client polls `/videos/1/status` -> Status eventually says "ready".
**Reference:** [Asynchronous Request-Reply Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply)
