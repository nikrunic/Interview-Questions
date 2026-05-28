# REST API Interview Questions

This document contains a comprehensive list of 100 REST API interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories and API design handbooks.

## Basic Questions

### 1. What does REST stand for?
**Answer:** Representational State Transfer.
**Example:** N/A
**Reference:** [REST APIs](https://restfulapi.net/)

---

---

---

### 2. What is a REST API?
**Answer:** An architectural style for an application program interface (API) that uses HTTP requests to access and use data.
**Example:** Fetching user data via `GET /users/1`
**Reference:** [IBM REST API](https://www.ibm.com/topics/rest-apis)

---

---

---

### 3. Who introduced REST?
**Answer:** 
**The Core Concept:**
Roy Fielding, in his 2000 Ph.D.

**Key Details:**
- dissertation.
**Example:** N/A
**Reference:** [Roy Fielding Dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)

---

---

---

### 4. What are the six guiding constraints of REST?
**Answer:** Client-server architecture, Statelessness, Cacheability, Layered system, Code on demand (optional), and Uniform interface.
**Example:** N/A
**Reference:** [REST Constraints](https://restfulapi.net/rest-architectural-constraints/)

---

---

---

### 5. What does "Statelessness" mean in REST?
**Answer:** 
**The Core Concept:**
The server does not store any state about the client session on the server side.

**Key Details:**
- Every request from the client must contain all the information necessary to understand the request.
**Example:** Sending a JWT token with every single request.
**Reference:** [Statelessness](https://restfulapi.net/statelessness/)

---

---

---

### 6. What is a Resource in REST?
**Answer:** 
**The Core Concept:**
The fundamental concept in REST.

**Key Details:**
- A resource is an object with a type, associated data, relationships to other resources, and a set of methods that operate on it.
**Example:** A "User" or a "Document".
**Reference:** [REST Resource](https://restfulapi.net/resource-naming/)

---

---

---

### 7. What is a URI?
**Answer:** 
**The Core Concept:**
Uniform Resource Identifier.

**Key Details:**
- It is used to identify a resource in a REST API.
**Example:** `https://api.example.com/v1/users/123`
**Reference:** [URI Design](https://restfulapi.net/resource-naming/)

---

---

---

### 8. What are the common HTTP methods used in REST?
**Answer:** GET, POST, PUT, PATCH, DELETE.
**Example:** `POST /users` creates a user.
**Reference:** [HTTP Methods](https://restfulapi.net/http-methods/)

---

---

---

### 9. What does the GET method do?
**Answer:** 
**The Core Concept:**
Retrieves a representation of a resource.

**Key Details:**
- It should only retrieve data and have no other effect (it is safe and idempotent).
**Example:** `GET /posts`
**Reference:** [GET Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)

---

---

---

### 10. What does the POST method do?
**Answer:** Submits an entity to the specified resource, often causing a change in state or side effects on the server (creating a new resource).
**Example:** `POST /posts`
**Reference:** [POST Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)

---

---

---

### 11. What is the difference between PUT and PATCH?
**Answer:** 
**The Core Concept:**
PUT replaces the entire resource with the updated representation.

**Key Details:**
- PATCH applies partial modifications to a resource.
**Example:** PUT overrides everything; PATCH updates just the email.
**Reference:** [PUT vs PATCH](https://restfulapi.net/rest-put-vs-patch/)

---

---

---

### 12. What does the DELETE method do?
**Answer:** Deletes the specified resource.
**Example:** `DELETE /users/1`
**Reference:** [DELETE Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)

---

---

---

### 13. What are HTTP Status Codes?
**Answer:** Standard response codes given by web servers on the internet to indicate whether a specific HTTP request has been successfully completed.
**Example:** `200 OK`, `404 Not Found`.
**Reference:** [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

---

---

### 14. What does a 2xx status code indicate?
**Answer:** 
**The Core Concept:**
Success.

**Key Details:**
- The action requested by the client was received, understood, and accepted.
**Example:** `200 OK`, `201 Created`.
**Reference:** [2xx Success](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses)

---

---

---

### 15. What does a 4xx status code indicate?
**Answer:** 
**The Core Concept:**
Client Error.

**Key Details:**
- The request contains bad syntax or cannot be fulfilled.
**Example:** `400 Bad Request`, `401 Unauthorized`.
**Reference:** [4xx Client Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses)

---

---

---

### 16. What does a 5xx status code indicate?
**Answer:** 
**The Core Concept:**
Server Error.

**Key Details:**
- The server failed to fulfill a valid request.
**Example:** `500 Internal Server Error`.
**Reference:** [5xx Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses)

---

---

---

### 17. What is JSON?
**Answer:** 
**The Core Concept:**
JavaScript Object Notation.

**Key Details:**
- The most common data format used for sending and receiving data in REST APIs.
**Example:** `{"name": "John"}`
**Reference:** [JSON](https://www.json.org/)

---

---

---

### 18. What are HTTP Headers?
**Answer:** Key-value pairs sent in HTTP requests and responses that provide metadata about the message, such as content type and authorization.
**Example:** `Content-Type: application/json`
**Reference:** [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

---

---

---

### 19. What is a Payload?
**Answer:** The actual data pack that is sent with the GET/POST/PUT HTTP request.
**Example:** The JSON body in a POST request.
**Reference:** [Payload](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages#body)

---

---

---

### 20. What is CRUD?
**Answer:** 
**The Core Concept:**
Create, Read, Update, Delete.

**Key Details:**
- The four basic operations of persistent storage, which map directly to POST, GET, PUT/PATCH, and DELETE.
**Example:** POST=Create, GET=Read.
**Reference:** [CRUD](https://developer.mozilla.org/en-US/docs/Glossary/CRUD)

---


## Medium (30 Questions)

---

## Intermediate Questions

---

## Intermediate Questions

### 21. What is an Idempotent operation?
**Answer:** An operation that will produce the same results if executed once or multiple times.
**Example:** `GET`, `PUT`, `DELETE` are idempotent. `POST` is not.
**Reference:** [Idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)

---

---

---

### 22. Why is POST not idempotent?
**Answer:** Making multiple identical POST requests will typically create multiple identical resources on the server.
**Example:** Hitting a checkout endpoint twice charges the user twice.
**Reference:** [Idempotent REST APIs](https://restfulapi.net/idempotent-rest-apis/)

---

---

---

### 23. Explain the Richardson Maturity Model.
**Answer:** 
**The Core Concept:**
A model that grades APIs by their RESTful maturity.

**Key Details:**
- Level 0 (Swamp of POX), Level 1 (Resources), Level 2 (HTTP Verbs), Level 3 (Hypermedia Controls/HATEOAS).
**Example:** Level 3 is true REST.
**Reference:** [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)

---

---

---

### 24. What is HATEOAS?
**Answer:** 
**The Core Concept:**
Hypermedia As The Engine Of Application State.

**Key Details:**
- A constraint of REST where the client interacts with a network application dynamically via hypermedia (links) provided dynamically by the server.
**Example:** The response includes `links: [{ rel: "next", href: "/page=2" }]`.
**Reference:** [HATEOAS](https://restfulapi.net/hateoas/)

---

---

---

### 25. How do you handle API Versioning?
**Answer:** 
**The Core Concept:**
API versioning allows you to change the API without breaking existing clients.

**Key Details:**
- Methods include URI versioning, Query Parameter versioning, and Header/Media-Type versioning.
**Example:** `https://api.example.com/v1/users`
**Reference:** [API Versioning](https://restfulapi.net/versioning/)

---

---

---

### 26. What is Content Negotiation?
**Answer:** The mechanism used for serving different representations of a resource at the same URI, so the client can specify which format it prefers (e.g., JSON or XML).
**Example:** The client sends `Accept: application/json`.
**Reference:** [Content Negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation)

---

---

---

### 27. What is the difference between `401 Unauthorized` and `403 Forbidden`?
**Answer:** 
**The Core Concept:**
`401` means "you are not authenticated" (you need to log in).

**Key Details:**
- `403` means "you are authenticated, but you do not have permission to access this resource."
**Example:** A user trying to access admin settings gets a 403.
**Reference:** [401 vs 403](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses)

---

---

---

### 28. What does `201 Created` mean?
**Answer:** 
**The Core Concept:**
The request was successful, and a new resource was created as a result.

**Key Details:**
- Typically used after a POST.
**Example:** Returning 201 after creating a new user account.
**Reference:** [201 Created](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201)

---

---

---

### 29. What does `204 No Content` mean?
**Answer:** 
**The Core Concept:**
The server successfully processed the request, but is not returning any content.

**Key Details:**
- Commonly used after a DELETE.
**Example:** Deleting a user doesn't require returning data, so return 204.
**Reference:** [204 No Content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204)

---

---

---

### 30. How do you implement Pagination in a REST API?
**Answer:** Typically through Query Parameters, using `limit` and `offset` (or `page` and `size`), or using Cursor-based pagination for high performance.
**Example:** `/users?limit=10&offset=20`
**Reference:** [REST Pagination](https://restfulapi.net/pagination/)

---

---

---

### 31. How do you implement Filtering in a REST API?
**Answer:** Using query parameters to filter the collection.
**Example:** `/users?role=admin&active=true`
**Reference:** [Filtering](https://restfulapi.net/rest-api-design-tutorial-with-example/#filtering)

---

---

---

### 32. How do you implement Sorting in a REST API?
**Answer:** Using a `sort` or `order` query parameter.
**Example:** `/users?sort=-created_at` (descending order).
**Reference:** [Sorting](https://restfulapi.net/rest-api-design-tutorial-with-example/#sorting)

---

---

---

### 33. What is a Webhook?
**Answer:** 
**The Core Concept:**
A user-defined HTTP callback.

**Key Details:**
- A way for an app to provide other applications with real-time information.
- It delivers data as it happens, rather than clients polling for it.
**Example:** Stripe sending a POST request when a payment succeeds.
**Reference:** [Webhooks](https://en.wikipedia.org/wiki/Webhook)

---

---

---

### 34. What is the difference between an API and a Webhook?
**Answer:** 
**The Core Concept:**
An API is pull-based (client asks server for data).

**Key Details:**
- A Webhook is push-based (server sends data to client when an event occurs).
**Example:** API: `GET /status`. Webhook: Server POSTs to your URL on status change.
**Reference:** [API vs Webhook](https://zapier.com/blog/what-are-webhooks/)

---

---

---

### 35. What is the `Authorization` header?
**Answer:** The HTTP header used to contain the credentials to authenticate a user agent with a server.
**Example:** `Authorization: Bearer <token>`
**Reference:** [Authorization Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)

---

---

---

### 36. What is OAuth 2.0?
**Answer:** 
**The Core Concept:**
An industry-standard protocol for authorization.

**Key Details:**
- It allows third-party services to exchange resources without sharing passwords.
**Example:** "Log in with Google".
**Reference:** [OAuth 2.0](https://oauth.net/2/)

---

---

---

### 37. What is JWT (JSON Web Token)?
**Answer:** 
**The Core Concept:**
A compact, URL-safe means of representing claims to be transferred between two parties.

**Key Details:**
- Used for stateless authentication.
**Example:** Three parts: Header, Payload, Signature.
**Reference:** [JWT.io](https://jwt.io/)

---

---

---

### 38. Explain Rate Limiting.
**Answer:** 
**The Core Concept:**
A strategy for limiting network traffic.

**Key Details:**
- It puts a cap on how often someone can repeat an action within a certain timeframe to protect APIs from abuse/DDoS.
**Example:** `429 Too Many Requests` returned when limit exceeded.
**Reference:** [Rate Limiting](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)

---

---

---

### 39. What is the `Accept` header?
**Answer:** An HTTP request header that informs the server about the types of data that can be sent back.
**Example:** `Accept: application/json`
**Reference:** [Accept Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept)

---

---

---

### 40. How do you design REST URIs for hierarchical relationships?
**Answer:** By nesting the paths to show the relationship between resources.
**Example:** `/users/123/posts/456`
**Reference:** [REST Resource Naming](https://restfulapi.net/resource-naming/)

---


## Hard (50 Questions)

---

---

### 41. What is the difference between REST and SOAP?
**Answer:** 
**The Core Concept:**
REST is an architectural style utilizing HTTP, usually returning JSON.

**Key Details:**
- SOAP is a strict protocol utilizing XML, requiring an XML wrapper (envelope) and strict schema definitions (WSDL).
**Example:** REST is lightweight; SOAP is heavily standardized.
**Reference:** [REST vs SOAP](https://www.ibm.com/cloud/blog/rest-vs-soap)

---

---

---

### 42. Explain Cross-Origin Resource Sharing (CORS).
**Answer:** 
**The Core Concept:**
A security mechanism by browsers that restricts cross-origin HTTP requests.

**Key Details:**
- Servers must include specific headers (`Access-Control-Allow-Origin`) to allow the browser to process the response.
**Example:** Preflight `OPTIONS` request.
**Reference:** [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

---

---

### 43. What is an API Gateway?
**Answer:** 
**The Core Concept:**
A server that is the single entry point into the system.

**Key Details:**
- It handles request routing, composition, protocol translation, security, and rate limiting.
**Example:** AWS API Gateway, Kong.
**Reference:** [API Gateway Pattern](https://microservices.io/patterns/apigateway.html)

---

---

---

### 44. How does HTTP Caching work in REST?
**Answer:** 
**The Core Concept:**
Using headers like `ETag`, `Cache-Control`, `Expires`, and `Last-Modified`.

**Key Details:**
- The client can use these to cache responses and validate if they are still fresh via conditional requests.
**Example:** `Cache-Control: max-age=3600`
**Reference:** [HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

---

---

---

### 45. What is an ETag?
**Answer:** 
**The Core Concept:**
Entity Tag.

**Key Details:**
- An HTTP response header that is an identifier for a specific version of a resource.
- Allows caches to be more efficient and prevents simultaneous updates of a resource from overwriting each other.
**Example:** `ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"`
**Reference:** [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)

---

---

---

### 46. What is a Conditional Request?
**Answer:** A request that is only processed if specific headers (like `If-Match` or `If-None-Match` comparing ETags) evaluate to true.
**Example:** `If-None-Match: "33a64df..."` returns 304 Not Modified if unchanged.
**Reference:** [Conditional Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests)

---

---

---

### 47. How do you handle concurrent updates in a REST API?
**Answer:** 
**The Core Concept:**
Using Optimistic Concurrency Control via ETags.

**Key Details:**
- The client sends an `If-Match: ETag` header with a PUT/PATCH.
- If the resource changed, the ETag doesn't match, and the server returns `412 Precondition Failed`.
**Example:** Preventing lost updates.
**Reference:** [Optimistic Concurrency Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match)

---

---

---

### 48. What is GraphQL and how does it compare to REST?
**Answer:** 
**The Core Concept:**
GraphQL is a query language where the client dictates the data shape.

**Key Details:**
- It solves REST's over-fetching and under-fetching by using a single endpoint.
**Example:** REST: `/users`, `/posts`. GraphQL: `/graphql`.
**Reference:** [GraphQL vs REST](https://graphql.org/faq/#how-is-graphql-different-from-rest)

---

---

---

### 49. How do you manage long-running tasks in a REST API?
**Answer:** 
**The Core Concept:**
Do not block the request.

**Key Details:**
- Return a `202 Accepted` status immediately with a `Location` header pointing to a status/job tracking endpoint.
- The client polls that endpoint until the task is complete.
**Example:** Uploading a large video -> 202 -> Poll `/jobs/1`.
**Reference:** [Async Request-Reply Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply)

---

---

---

### 50. What is OpenAPI / Swagger?
**Answer:** A widely adopted specification for machine-readable interface files for describing, producing, consuming, and visualizing RESTful web services.
**Example:** `swagger.yaml` generating automated docs.
**Reference:** [OpenAPI Specification](https://swagger.io/specification/)

---

---

## Expert Questions

---

## Expert Questions

### 51. What is HATEOAS?
**Answer:** 
**The Core Concept:**
Hypermedia As The Engine Of Application State—responses include links to related actions/resources.

**Key Details:**
- Clients discover capabilities from links.
- Rare in practice but part of REST maturity model.

**Example:** 
`links: { self, next, create }`

**Reference:** [Documentation](https://restfulapi.net/hateoas/)

---

---

---

### 52. What is API versioning?
**Answer:** 
**The Core Concept:**
Strategy to evolve APIs without breaking clients (URI, header, query, content negotiation).

**Key Details:**
- Prefer explicit /v1/ in URI or Accept header.
- Deprecate old versions with sunset headers.

**Example:** 
`GET /v2/users`

**Reference:** [Documentation](https://restfulapi.net/versioning/)

---

---

---

### 53. What is content negotiation?
**Answer:** 
**The Core Concept:**
Client and server agree on representation format via Accept and Content-Type headers.

**Key Details:**
- Support JSON and optionally XML.
- Return 406 if format unsupported.

**Example:** 
`Accept: application/json`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation)

---

---

---

### 54. What is 201 Created?
**Answer:** 
**The Core Concept:**
Success status when a resource is created, often with Location header to new resource.

**Key Details:**
- Body may contain created representation.
- Pair with POST.

**Example:** 
`201 + Location: /users/42`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201)

---

---

---

### 55. What is 204 No Content?
**Answer:** 
**The Core Concept:**
Success with empty body—common for DELETE or PUT with nothing to return.

**Key Details:**
- Still success—do not treat as error.
- DELETE often returns 204.

**Example:** 
`DELETE /users/1 -> 204`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204)

---

---

---

### 56. What is 400 vs 422?
**Answer:** 
**The Core Concept:**
400 Bad Request for malformed syntax; 422 Unprocessable Entity for semantically invalid but parsed body.

**Key Details:**
- 422 popular in validation errors.
- Be consistent across API.

**Example:** 
`422 + validation errors array`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422)

---

---

---

### 57. What is Problem Details (RFC 7807)?
**Answer:** 
**The Core Concept:**
Standard JSON error format with type, title, status, detail, instance.

**Key Details:**
- Improves machine-readable errors.
- Use application/problem+json.

**Example:** 
`{"type":"...","title":"Not Found","status":404}`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc7807)

---

---

---

### 58. What is pagination in REST?
**Answer:** 
**The Core Concept:**
Splitting large collections into pages via offset/limit or cursor.

**Key Details:**
- Cursor pagination avoids offset drift on live data.
- Include total only if cheap to compute.

**Example:** 
`?cursor=abc&limit=20`

**Reference:** [Documentation](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/)

---

---

---

### 59. What is cursor-based pagination?
**Answer:** 
**The Core Concept:**
Using opaque cursor from previous response instead of page number.

**Key Details:**
- Stable for frequently changing datasets.
- Cannot jump to arbitrary page easily.

**Example:** 
`next_cursor in response meta`

**Reference:** [Documentation](https://slack.engineering/evolving-api-pagination-at-slack/)

---

---

---

### 60. What is filtering and sorting?
**Answer:** 
**The Core Concept:**
Query parameters to narrow and order collections.

**Key Details:**
- Document allowed fields.
- Validate to prevent SQL injection in backends.

**Example:** 
`?status=active&sort=-createdAt`

**Reference:** [Documentation](https://restfulapi.net/filtering/)

---

---

---

### 61. What is sparse fieldsets?
**Answer:** 
**The Core Concept:**
Client requests only specific fields to reduce payload.

**Key Details:**
- fields=id,name on users.
- Maps to GraphQL-like efficiency in REST.

**Example:** 
`?fields=id,email`

**Reference:** [Documentation](https://jsonapi.org/format/#fetching-sparse-fieldsets)

---

---

---

### 62. What is API rate limiting?
**Answer:** 
**The Core Concept:**
Restricting requests per client/time window to protect availability.

**Key Details:**
- Return 429 Too Many Requests.
- Headers: Retry-After, X-RateLimit-*.

**Example:** 
`429 + Retry-After: 60`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)

---

---

---

### 63. What is idempotency key?
**Answer:** 
**The Core Concept:**
Client-sent unique key so retried POSTs do not create duplicates.

**Key Details:**
- Server stores key -> response mapping.
- Essential for payments.

**Example:** 
`Idempotency-Key: uuid`

**Reference:** [Documentation](https://stripe.com/docs/api/idempotent_requests)

---

---

---

### 64. What is ETag?
**Answer:** 
**The Core Concept:**
Entity tag for cache validation and optimistic concurrency.

**Key Details:**
- If-Match on PUT prevents lost updates.
- If-None-Match for conditional GET.

**Example:** 
`ETag: "v1-abc"`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)

---

---

---

### 65. What is conditional GET?
**Answer:** 
**The Core Concept:**
Client sends If-None-Match/If-Modified-Since; server returns 304 if unchanged.

**Key Details:**
- Saves bandwidth.
- CDN and browser caching rely on this.

**Example:** 
`304 Not Modified`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests)

---

---

---

### 66. What is API Gateway pattern?
**Answer:** 
**The Core Concept:**
Single entry point for routing, auth, throttling, and aggregation to microservices.

**Key Details:**
- AWS API Gateway, Kong, Azure APIM.
- Offloads cross-cutting concerns.

**Example:** 
`Client -> Gateway -> services`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway)

---

---

---

### 67. What is BFF for REST?
**Answer:** 
**The Core Concept:**
Backend for Frontend shapes REST responses per UI needs.

**Key Details:**
- Reduces chatty calls from mobile.
- Not a generic public API.

**Example:** 
`Mobile BFF aggregates 3 services`

**Reference:** [Documentation](https://samnewman.io/patterns/architectural/bff/)

---

---

---

### 68. What is chattiness in REST?
**Answer:** 
**The Core Concept:**
Many round trips needed for one screen due to normalized resources.

**Key Details:**
- Mitigate with compound documents or BFF.
- GraphQL addresses this tradeoff.

**Example:** 
`10 GETs for dashboard`

**Reference:** [Documentation](https://graphql.org/learn/thinking-in-graphs/)

---

---

---

### 69. What is over-fetching?
**Answer:** 
**The Core Concept:**
API returns more data than client needs.

**Key Details:**
- Field filtering and specialized endpoints help.
- GraphQL targets this problem.

**Example:** 
`GET user returns 50 fields, UI needs 3`

**Reference:** [Documentation](https://graphql.org/faq/#how-is-graphql-different-from-rest)

---

---

---

### 70. What is under-fetching?
**Answer:** 
**The Core Concept:**
One endpoint insufficient; client must call more endpoints.

**Key Details:**
- HATEOAS or includes expand related data.
- N+1 client calls.

**Example:** 
`GET user then GET /users/1/posts`

**Reference:** [Documentation](https://graphql.org/faq/#how-is-graphql-different-from-rest)

---

---

---

### 71. What is webhook?
**Answer:** 
**The Core Concept:**
Server pushes event to client URL via HTTP POST when something happens.

**Key Details:**
- Verify signatures (HMAC).
- Retry with exponential backoff.

**Example:** 
`POST https://client.com/hooks payment.succeeded`

**Reference:** [Documentation](https://webhooks.fyi/)

---

---

---

### 72. What is webhook idempotency?
**Answer:** 
**The Core Concept:**
Same event delivered multiple times must not double-charge or duplicate side effects.

**Key Details:**
- Use event id deduplication store.
- Return 2xx after processing.

**Example:** 
`stripe event id evt_123 processed once`

**Reference:** [Documentation](https://stripe.com/docs/webhooks/best-practices)

---

---

---

### 73. What is long polling?
**Answer:** 
**The Core Concept:**
Client holds request open until server has data or timeout.

**Key Details:**
- Fallback before WebSockets.
- Higher server load than push.

**Example:** 
`GET /messages?wait=30s`

**Reference:** [Documentation](https://en.wikipedia.org/wiki/Push_technology#Long_polling)

---

---

---

### 74. What is Server-Sent Events (SSE)?
**Answer:** 
**The Core Concept:**
One-way server push over HTTP with text/event-stream.

**Key Details:**
- Simpler than WebSockets for notifications.
- Auto-reconnect built in.

**Example:** 
`EventSource('/stream')`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

---

---

---

### 75. What is gRPC vs REST?
**Answer:** 
**The Core Concept:**
gRPC uses HTTP/2 + Protocol Buffers for strongly typed RPC; REST uses HTTP + JSON typically.

**Key Details:**
- gRPC better for internal microservices.
- REST better for public browser APIs.

**Example:** 
`service GetUser(UserRequest)`

**Reference:** [Documentation](https://grpc.io/docs/what-is-grpc/introduction/)

---

---

---

### 76. What is JSON:API specification?
**Answer:** 
**The Core Concept:**
Convention for JSON structure, relationships, and errors in REST APIs.

**Key Details:**
- includes, relationships, compound documents.
- Adopt if team wants consistency.

**Example:** 
`{"data":{"type":"articles","id":"1"}}`

**Reference:** [Documentation](https://jsonapi.org/)

---

---

---

### 77. What is HAL?
**Answer:** 
**The Core Concept:**
Hypertext Application Language—JSON linking format for HATEOAS.

**Key Details:**
- _links object in resources.
- Less common than custom links.

**Example:** 
`_links: { self: { href } }`

**Reference:** [Documentation](https://stateless.group/hal_specification.html)

---

---

---

### 78. What is OData?
**Answer:** 
**The Core Concept:**
Open protocol for querying REST APIs with $filter, $select, $expand.

**Key Details:**
- Popular in Microsoft ecosystems.
- Powerful but complex.

**Example:** 
`GET /Products?$filter=Price gt 10`

**Reference:** [Documentation](https://www.odata.org/)

---

---

---

### 79. What is API-first design?
**Answer:** 
**The Core Concept:**
Design contract (OpenAPI) before implementation.

**Key Details:**
- Enables parallel client/server work.
- Contract tests validate compliance.

**Example:** 
`openapi.yaml reviewed in PR`

**Reference:** [Documentation](https://swagger.io/resources/articles/adopting-an-api-first-approach/)

---

---

---

### 80. What is consumer-driven contract testing?
**Answer:** 
**The Core Concept:**
Consumers define expected API contract; provider verifies.

**Key Details:**
- Pact is popular tool.
- Catches breaking changes early.

**Example:** 
`Pact between mobile app and API`

**Reference:** [Documentation](https://docs.pact.io/)

---

---

---

### 81. What is breaking vs non-breaking API change?
**Answer:** 
**The Core Concept:**
Breaking removes/changes behavior clients rely on; non-breaking is additive.

**Key Details:**
- Adding optional field is safe.
- Renaming field is breaking.

**Example:** 
`add optional query param vs rename field`

**Reference:** [Documentation](https://semver.org/)

---

---

---

### 82. What is semantic versioning for APIs?
**Answer:** 
**The Core Concept:**
MAJOR for breaking, MINOR for features, PATCH for fixes.

**Key Details:**
- URL version or header policy.
- Communicate deprecation timeline.

**Example:** 
`v2.1.0`

**Reference:** [Documentation](https://semver.org/)

---

---

---

### 83. What is sunset header?
**Answer:** 
**The Core Concept:**
HTTP Sunset header announces API/version retirement date.

**Key Details:**
- Pair with deprecation warnings in docs.
- Give clients migration time.

**Example:** 
`Sunset: Sat, 01 Jan 2027 00:00:00 GMT`

**Reference:** [Documentation](https://datatracker.ietf.org/doc/html/rfc8594)

---

---

---

### 84. What is CORS preflight?
**Answer:** 
**The Core Concept:**
OPTIONS request before actual request when using custom headers or methods.

**Key Details:**
- Server must respond with Access-Control-Allow-*.
- Fails if gateway strips headers.

**Example:** 
`OPTIONS /api/users`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

---

---

### 85. What is mTLS for APIs?
**Answer:** 
**The Core Concept:**
Mutual TLS authenticates client and server with certificates.

**Key Details:**
- Common service-to-service.
- Complements OAuth.

**Example:** 
`client cert required on /internal/*`

**Reference:** [Documentation](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/)

---

---

---

### 86. What is OAuth2 for REST APIs?
**Answer:** 
**The Core Concept:**
Delegated authorization using bearer access tokens.

**Key Details:**
- Resource server validates JWT or introspects.
- Scopes limit access.

**Example:** 
`Authorization: Bearer token`

**Reference:** [Documentation](https://oauth.net/2/)

---

---

---

### 87. What is API key vs OAuth?
**Answer:** 
**The Core Concept:**
API keys identify app; OAuth identifies user delegation.

**Key Details:**
- Keys simpler for partners.
- OAuth for user data access.

**Example:** 
`X-API-Key for server cron job`

**Reference:** [Documentation](https://cloud.google.com/docs/authentication/api-keys)

---

---

---

### 88. What is scope-based authorization?
**Answer:** 
**The Core Concept:**
Permissions encoded in token scopes enforced per endpoint.

**Key Details:**
- read:users vs write:users.
- Document scope matrix.

**Example:** 
`scope must include admin for DELETE`

**Reference:** [Documentation](https://oauth.net/2/scope/)

---

---

---

### 89. What is OWASP API Security Top 10?
**Answer:** 
**The Core Concept:**
Common API risks: BOLA, broken auth, excessive data exposure, etc.

**Key Details:**
- BOLA = Broken Object Level Authorization.
- Use in threat modeling.

**Example:** 
`API1:2023 Broken Object Level Authorization`

**Reference:** [Documentation](https://owasp.org/API-Security/)

---

---

---

### 90. What is input validation for APIs?
**Answer:** 
**The Core Concept:**
Validate types, lengths, enums at boundary before business logic.

**Key Details:**
- Return 400 with clear errors.
- Never trust client.

**Example:** 
`email must match RFC pattern`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

---

---

---

### 91. What is output encoding?
**Answer:** 
**The Core Concept:**
Encode data in responses to prevent injection in consumers.

**Key Details:**
- Set correct Content-Type.
- Sanitize error messages.

**Example:** 
`no stack traces in production 500`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

---

---

---

### 92. What is mass assignment vulnerability?
**Answer:** 
**The Core Concept:**
Client sends unexpected fields that update privileged attributes.

**Key Details:**
- Use DTOs with allow lists.
- Ignore unknown properties.

**Example:** 
`POST { role: admin }`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)

---

---

---

### 93. What is file upload REST design?
**Answer:** 
**The Core Concept:**
Use multipart/form-data, virus scan, size limits, store outside web root.

**Key Details:**
- Return 201 with file metadata.
- Generate random filenames.

**Example:** 
`POST /upload multipart`

**Reference:** [Documentation](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

---

---

---

### 94. What is bulk operations API?
**Answer:** 
**The Core Concept:**
Batch create/update/delete in one request with partial success reporting.

**Key Details:**
- 207 Multi-Status possible.
- Idempotency critical.

**Example:** 
`POST /users/bulk`

**Reference:** [Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/207)

---

---

---

### 95. What is health check endpoint?
**Answer:** 
**The Core Concept:**
GET /health or /ready for load balancers and orchestrators.

**Key Details:**
- Liveness vs readiness probes.
- Do not require auth; minimal info.

**Example:** 
`GET /health -> 200 OK`

**Reference:** [Documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

---

---

---

### 96. What is graceful shutdown?
**Answer:** 
**The Core Concept:**
Stop accepting new requests, finish in-flight, then exit.

**Key Details:**
- Kubernetes preStop hook.
- Release DB connections.

**Example:** 
`SIGTERM handler drains server`

**Reference:** [Documentation](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace)

---

---

---

### 97. What is request tracing?
**Answer:** 
**The Core Concept:**
Correlation ID (X-Request-ID) across microservices for debugging.

**Key Details:**
- Propagate in logs.
- OpenTelemetry standardizes.

**Example:** 
`X-Correlation-ID: uuid`

**Reference:** [Documentation](https://opentelemetry.io/)

---

---

---

### 98. What is structured logging for APIs?
**Answer:** 
**The Core Concept:**
JSON logs with method, path, status, duration, userId.

**Key Details:**
- Enable log aggregation.
- No PII in logs.

**Example:** 
`{"method":"GET","status":200,"ms":45}`

**Reference:** [Documentation](https://www.honeycomb.io/blog/structured-logging-and-your-team)

---

---

---

### 99. What is API mocking?
**Answer:** 
**The Core Concept:**
Simulate API during development (WireMock, Prism from OpenAPI).

**Key Details:**
- Frontend unblocked.
- Contract-based mocks stay accurate.

**Example:** 
`prism mock openapi.yaml`

**Reference:** [Documentation](https://stoplight.io/open-source/prism)

---

---

---

### 100. What is load testing REST?
**Answer:** 
**The Core Concept:**
Tools like k6, JMeter measure throughput and latency under stress.

**Key Details:**
- Test realistic payloads.
- Find breaking point before prod.

**Example:** 
`k6 run script.js`

**Reference:** [Documentation](https://k6.io/docs/)

---

---

## Technical Questions

---

### 1. Implement a complete REST API controller in Node.js (Express) with standard status codes.

**Example Solution:**
```javascript
const express = require("express");
const app = express();
app.use(express.json());

const users = [];

app.post("/api/v1/users", (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ error: "Missing required fields: name, email" });
  }
  const newUser = { id: users.length + 1, name, email };
  users.push(newUser);
  res.status(201).json(newUser);
});

app.get("/api/v1/users/:id", (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) {
    return res.status(404).json({ error: "User not found" });
  }
  res.status(200).json(user);
});
```

---

### 2. Implement an API client with dynamic exponential backoff and jitter retry mechanism.

**Example Solution:**
```javascript
async function fetchWithRetry(url, options = {}, retries = 3, delay = 1000) {
  try {
    const response = await fetch(url, options);
    if (!response.ok && retries > 0) {
      throw new Error(`Server error: \${response.status}`);
    }
    return await response.json();
  } catch (error) {
    if (retries === 0) throw error;
    // Add jitter
    const jitter = Math.random() * 200;
    const nextDelay = delay * 2 + jitter;
    console.warn(`Retry failed. Retrying in \${nextDelay.toFixed(0)}ms...`);
    await new Promise(res => setTimeout(res, nextDelay));
    return fetchWithRetry(url, options, retries - 1, delay * 2);
  }
}
```

---

## Technical Questions

### 1. Implement a complete REST API controller in Node.js (Express) with standard status codes.

**Example Solution:**
```javascript
const express = require("express");
const app = express();
app.use(express.json());

const users = [];

app.post("/api/v1/users", (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ error: "Missing required fields: name, email" });
  }
  const newUser = { id: users.length + 1, name, email };
  users.push(newUser);
  res.status(201).json(newUser);
});

app.get("/api/v1/users/:id", (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) {
    return res.status(404).json({ error: "User not found" });
  }
  res.status(200).json(user);
});
```

### 2. Implement an API client with dynamic exponential backoff and jitter retry mechanism.

**Example Solution:**
```javascript
async function fetchWithRetry(url, options = {}, retries = 3, delay = 1000) {
  try {
    const response = await fetch(url, options);
    if (!response.ok && retries > 0) {
      throw new Error(`Server error: \${response.status}`);
    }
    return await response.json();
  } catch (error) {
    if (retries === 0) throw error;
    const jitter = Math.random() * 200;
    const nextDelay = delay * 2 + jitter;
    console.warn(`Retry failed. Retrying in \${nextDelay.toFixed(0)}ms...`);
    await new Promise(res => setTimeout(res, nextDelay));
    return fetchWithRetry(url, options, retries - 1, delay * 2);
  }
}
```

### 3. Write a central Express error-handling middleware matching REST spec.

**Example Solution:**
```javascript
function restErrorHandler(err, req, res, next) {
  console.error(err.stack);
  const statusCode = err.statusCode || 500;
  res.status(statusCode).json({
    error: {
      message: err.message || "Internal Server Error",
      code: err.code || "INTERNAL_ERROR",
      timestamp: new Date().toISOString()
    }
  });
}
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a RESTful API Architecture application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy RESTful API Architecture operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of RESTful API Architecture configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using RESTful API Architecture event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing RESTful API Architecture with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output RESTful API Architecture performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during RESTful API Architecture failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to RESTful API Architecture data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving RESTful API Architecture state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates RESTful API Architecture logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle RESTful API Architecture files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking RESTful API Architecture connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using RESTful API Architecture.

*(Challenge question for self-study and practical project implementation.)*

