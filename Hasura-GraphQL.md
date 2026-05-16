# Hasura & GraphQL Interview Questions

This document contains a comprehensive list of Hasura and GraphQL interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is GraphQL?
**Answer:** GraphQL is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data. It allows clients to request exactly the data they need.
**Example:** `query { user { id name } }`
**Reference:** [GraphQL Official Website](https://graphql.org/)

### 2. How is GraphQL different from REST?
**Answer:** REST relies on multiple endpoints returning fixed data structures (over-fetching/under-fetching). GraphQL uses a single endpoint and allows the client to dictate the exact shape and size of the response.
**Example:** REST: `GET /users/1` and `GET /users/1/posts`. GraphQL: Single query getting both user and posts.
**Reference:** [GraphQL - REST vs GraphQL](https://www.howtographql.com/basics/1-graphql-is-the-better-rest/)

### 3. What is a Query in GraphQL?
**Answer:** A Query is used to fetch data from the server. It is equivalent to a GET request in REST.
**Example:** `query { allUsers { name } }`
**Reference:** [GraphQL - Queries and Mutations](https://graphql.org/learn/queries/)

### 4. What is a Mutation in GraphQL?
**Answer:** A Mutation is used to modify data on the server (create, update, delete). It is equivalent to POST, PUT, or DELETE requests in REST.
**Example:** `mutation { addUser(name: "John") { id } }`
**Reference:** [GraphQL - Mutations](https://graphql.org/learn/queries/#mutations)

### 5. What is Hasura?
**Answer:** Hasura is an open-source engine that connects to your databases and microservices and instantly auto-generates a production-ready GraphQL API.
**Example:** Connecting Hasura to Postgres generates a CRUD API instantly.
**Reference:** [Hasura Official Docs](https://hasura.io/docs/latest/graphql/core/index/)


## Medium (30%)

### 6. What are Subscriptions in GraphQL?
**Answer:** Subscriptions are a GraphQL feature that allows a server to push data to its clients in real-time, usually implemented via WebSockets. They are used for live updates.
**Example:** `subscription { messageAdded { id text } }`
**Reference:** [GraphQL - Subscriptions](https://graphql.org/blog/subscriptions-in-graphql-and-relay/)

### 7. How does Hasura handle authorization and role-based access control?
**Answer:** Hasura uses an attribute-based access control (ABAC) system. You define permissions at the row and column level for different roles (e.g., `user`, `admin`), often relying on headers like `x-hasura-role` and `x-hasura-user-id` passed from your auth provider.
**Example:** Row check: `{"user_id": {"_eq": "X-Hasura-User-Id"}}`
**Reference:** [Hasura - Authorization](https://hasura.io/docs/latest/graphql/core/auth/authorization/)

### 8. What are Hasura Actions?
**Answer:** Actions are a way to extend Hasura's schema with custom business logic. You define a custom mutation or query in Hasura, and Hasura forwards the request to an external REST or GraphQL webhook you provide.
**Example:** Creating a `registerUser` action that triggers a Node.js webhook.
**Reference:** [Hasura - Actions](https://hasura.io/docs/latest/graphql/core/actions/index/)

### 9. What are Hasura Event Triggers?
**Answer:** Event Triggers reliably capture data events (Insert, Update, Delete) on specified database tables and invoke HTTP webhooks to carry out custom business logic.
**Example:** Sending a welcome email when a new user is inserted into the `users` table.
**Reference:** [Hasura - Event Triggers](https://hasura.io/docs/latest/graphql/core/event-triggers/index/)

### 10. Explain the N+1 problem in GraphQL.
**Answer:** The N+1 problem occurs when fetching a list of items and then making a separate database query to fetch related data for each item, leading to terrible performance. This is typically solved using DataLoaders (batching and caching). Hasura solves this automatically by compiling GraphQL directly into optimized SQL joins.
**Example:** Fetching 100 users and then fetching posts for each user individually (101 queries).
**Reference:** [GraphQL - N+1 Problem](https://www.howtographql.com/advanced/1-server/)


## Hard (50%)

### 11. What is Remote Schema in Hasura?
**Answer:** Remote schemas allow you to bring in custom GraphQL servers and stitch their schema directly into the Hasura GraphQL API. This gives you a unified GraphQL endpoint across databases and external services.
**Example:** Stitching a custom Stripe GraphQL API with your Hasura Postgres API.
**Reference:** [Hasura - Remote Schemas](https://hasura.io/docs/latest/graphql/core/remote-schemas/index/)

### 12. How does Hasura translate GraphQL to SQL?
**Answer:** Hasura's compiler parses the GraphQL AST, validates it against the schema, and generates a single, highly optimized SQL query (using `JSON_AGG` and Joins). It does not use GraphQL resolvers, bypassing the N+1 problem entirely.
**Example:** A deep nested GraphQL query becomes one `SELECT ... JSON_AGG` Postgres query.
**Reference:** [Hasura Architecture](https://hasura.io/blog/architecture-of-a-high-performance-graphql-to-sql-server/)

### 13. What is Schema Stitching vs Federation?
**Answer:** Both are methods to combine multiple GraphQL APIs. Schema Stitching (Hasura Remote Schemas) involves an API gateway merging schemas. Federation (Apollo) is a distributed architecture where individual services define their boundaries and a gateway composes them. Hasura uses data federation linking databases, actions, and remote schemas.
**Example:** Apollo Federation uses `@key` directives. Hasura uses Remote Joins.
**Reference:** [Apollo - Federation vs Stitching](https://www.apollographql.com/docs/federation/)

### 14. How do you implement custom JWT authentication with Hasura?
**Answer:** You configure Hasura with a JWT secret. Your authentication service generates a JWT containing specific custom claims (`https://hasura.io/jwt/claims`). Hasura verifies the JWT signature and uses the claims (`x-hasura-role`, `x-hasura-user-id`) to enforce permission rules.
**Example:** Payload: `"https://hasura.io/jwt/claims": { "x-hasura-allowed-roles": ["user"], "x-hasura-default-role": "user", "x-hasura-user-id": "123" }`
**Reference:** [Hasura - JWT Authentication](https://hasura.io/docs/latest/graphql/core/auth/authentication/jwt/)

### 15. What are Hasura Computed Fields?
**Answer:** Computed fields allow you to add custom fields to your GraphQL schema that execute a custom SQL function in Postgres. This is useful for deriving data without storing it, like a full name from first and last name, or complex aggregations.
**Example:** Function `search_users(search text)` attached as a field to `user`.
**Reference:** [Hasura - Computed Fields](https://hasura.io/docs/latest/graphql/core/schema/computed-fields/)

### 16. What are Remote Joins in Hasura?
**Answer:** Remote joins allow you to join data across different data sources. You can join your Postgres database with a Remote Schema, an Action, or even another database seamlessly in a single GraphQL query.
**Example:** Joining `user_id` from Postgres with payment history from a Stripe Remote Schema.
**Reference:** [Hasura - Remote Joins](https://hasura.io/docs/latest/graphql/core/remote-schemas/remote-relationships/)

### 17. How do you handle migrations and metadata in Hasura across environments?
**Answer:** Hasura uses the Hasura CLI to manage database schemas (Migrations) and Hasura configurations (Metadata) as files. These files are checked into version control (Git) and applied sequentially in CI/CD pipelines to keep staging and production environments in sync.
**Example:** `hasura migrate apply && hasura metadata apply`
**Reference:** [Hasura - Migrations & Metadata](https://hasura.io/docs/latest/graphql/core/migrations/index/)

### 18. Explain cursor-based pagination vs offset-based pagination in GraphQL.
**Answer:** Offset (limit/offset) is simple but can skip or duplicate items if data is added/deleted during pagination. Cursor-based pagination uses a unique identifier (cursor) for the last fetched item, fetching the next set "after" that cursor. Cursor pagination scales better and is consistent.
**Example:** Relay connections specification uses `first: 10, after: "cursor"`.
**Reference:** [GraphQL - Pagination](https://graphql.org/learn/pagination/)

### 19. What is a GraphQL Fragment and what problem does it solve?
**Answer:** A Fragment is a reusable chunk of a GraphQL query. It solves the problem of writing the same fields over and over across multiple queries or mutations, keeping queries DRY (Don't Repeat Yourself).
**Example:** `fragment UserDetails on User { id name email }`
**Reference:** [GraphQL - Fragments](https://graphql.org/learn/queries/#fragments)

### 20. How do you mitigate Denial of Service (DoS) attacks on a GraphQL/Hasura server?
**Answer:** By implementing Depth Limits (preventing infinitely deep queries), Query Complexity limits (assigning costs to fields), Rate Limiting, and using API Gateways. Hasura Cloud provides Allow-lists (only executing pre-approved queries) and automated rate limits based on roles.
**Example:** Blocking a query that is nested 10 levels deep.
**Reference:** [Hasura - Security](https://hasura.io/docs/latest/graphql/cloud/security/index/)
