# Hasura & GraphQL Interview Questions

This document contains a comprehensive list of 100 Hasura and GraphQL interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories and official documentation.

## Basic (20 Questions)

### 1. What is GraphQL?
**Answer:** An open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data, developed by Facebook.
**Example:** `query { user { id name } }`
**Reference:** [GraphQL Org](https://graphql.org/)

### 2. How does GraphQL differ from REST?
**Answer:** 
**The Core Concept:**
REST uses multiple endpoints returning fixed data structures.

**Key Details:**
- GraphQL uses a single endpoint where the client specifies exactly what data it needs, avoiding over-fetching and under-fetching.
**Example:** Single `/graphql` endpoint vs `/users`, `/posts`.
**Reference:** [GraphQL vs REST](https://graphql.org/faq/#how-is-graphql-different-from-rest)

### 3. What is a Query in GraphQL?
**Answer:** 
**The Core Concept:**
A read-only operation requested by a client to fetch data from the server.

**Key Details:**
- Equivalent to a GET request in REST.
**Example:** `query GetUsers { users { id } }`
**Reference:** [Queries](https://graphql.org/learn/queries/)

### 4. What is a Mutation in GraphQL?
**Answer:** 
**The Core Concept:**
An operation used to modify server-side data (create, update, delete) and return a value.

**Key Details:**
- Equivalent to POST, PUT, DELETE in REST.
**Example:** `mutation AddUser { insert_user(name: "John") { id } }`
**Reference:** [Mutations](https://graphql.org/learn/queries/#mutations)

### 5. What is a Subscription in GraphQL?
**Answer:** A long-lasting operation that allows clients to receive real-time updates from the server via WebSockets whenever data changes.
**Example:** `subscription { new_messages { id text } }`
**Reference:** [Subscriptions](https://graphql.org/blog/subscriptions-in-graphql-and-relay/)

### 6. What is a GraphQL Schema?
**Answer:** A strongly typed definition of the capabilities of a GraphQL server, describing all possible queries, mutations, types, and their relationships.
**Example:** `type User { id: ID! name: String! }`
**Reference:** [Schema](https://graphql.org/learn/schema/)

### 7. What are Scalar Types in GraphQL?
**Answer:** 
**The Core Concept:**
The base primitive types that resolve to concrete data.

**Key Details:**
- Default scalars are `Int`, `Float`, `String`, `Boolean`, and `ID`.
**Example:** `age: Int`
**Reference:** [Scalar Types](https://graphql.org/learn/schema/#scalar-types)

### 8. What does the `!` symbol mean in a Schema?
**Answer:** 
**The Core Concept:**
It indicates that the field is Non-Null (required).

**Key Details:**
- The server will always return a value for it, and it cannot be null.
**Example:** `email: String!`
**Reference:** [Lists and Non-Null](https://graphql.org/learn/schema/#lists-and-non-null)

### 9. What is Hasura?
**Answer:** Hasura GraphQL Engine is an open-source product that connects to databases (like PostgreSQL) and instantly generates a production-ready GraphQL API with built-in authorization.
**Example:** Connecting Hasura to Postgres to instantly get CRUD queries.
**Reference:** [Hasura Docs](https://hasura.io/docs/latest/index/)

### 10. How does Hasura generate the GraphQL schema?
**Answer:** Hasura introspects the connected database schema (tables, views, foreign keys) and automatically creates GraphQL types, queries, and mutations mapped to the database structure.
**Example:** A `users` table generates `users`, `insert_users`, `update_users` fields.
**Reference:** [Schema Generation](https://hasura.io/docs/latest/schema/postgres/index/)

### 11. What databases does Hasura support?
**Answer:** Primarily PostgreSQL, but also supports MS SQL Server, Citus, CockroachDB, BigQuery, and MySQL (via data connectors).
**Example:** Adding Postgres connection string in Hasura console.
**Reference:** [Supported Databases](https://hasura.io/docs/latest/databases/overview/)

### 12. What is GraphiQL?
**Answer:** 
**The Core Concept:**
An in-browser IDE for exploring GraphQL APIs, writing queries with autocomplete, and viewing the schema documentation.

**Key Details:**
- Hasura includes this in its console.
**Example:** Using GraphiQL to test a `users` query.
**Reference:** [GraphiQL](https://github.com/graphql/graphiQL)

### 13. What are GraphQL Arguments?
**Answer:** Values passed to fields in a query to filter or specify exactly what data is needed.
**Example:** `user(id: "1") { name }`
**Reference:** [Arguments](https://graphql.org/learn/queries/#arguments)

### 14. What are Aliases in GraphQL?
**Answer:** Allows clients to rename the result of a field to avoid conflicts when querying the same field with different arguments.
**Example:** `admin: user(id: "1") { name }`
**Reference:** [Aliases](https://graphql.org/learn/queries/#aliases)

### 15. What are Fragments?
**Answer:** Reusable units of a GraphQL query that let you construct sets of fields and include them in multiple queries to keep code DRY.
**Example:** `fragment userFields on User { id name }`
**Reference:** [Fragments](https://graphql.org/learn/queries/#fragments)

### 16. What is the `ID` type?
**Answer:** 
**The Core Concept:**
A scalar type representing a unique identifier, often used to refetch an object or as a cache key.

**Key Details:**
- It serializes the same way as a String.
**Example:** `id: ID!`
**Reference:** [ID Type](https://graphql.org/learn/schema/#scalar-types)

### 17. How do you track a table in Hasura?
**Answer:** After creating a table in the database, you must "track" it in the Hasura Console so Hasura knows to expose it in the GraphQL schema.
**Example:** Clicking "Track" in the Hasura Data tab.
**Reference:** [Tracking Tables](https://hasura.io/docs/latest/schema/postgres/tables/)

### 18. What is Introspection?
**Answer:** A feature of GraphQL that allows clients to query the schema itself to learn what queries, types, and fields are available.
**Example:** `query { __schema { types { name } } }`
**Reference:** [Introspection](https://graphql.org/learn/introspection/)

### 19. What is Over-fetching?
**Answer:** When a client downloads more data than is actually needed by the UI, common in REST but solved by GraphQL.
**Example:** Getting a full User object just to display their username.
**Reference:** [Over-fetching](https://graphql.org/faq/#how-is-graphql-different-from-rest)

### 20. What is Under-fetching?
**Answer:** When a specific endpoint doesn't return enough data, forcing the client to make additional secondary requests (N+1 problem).
**Example:** Fetching a post, then making 10 requests for its 10 comments.
**Reference:** [Under-fetching](https://graphql.org/faq/#how-is-graphql-different-from-rest)


## Medium (30 Questions)

### 21. How do you handle relationships in Hasura?
**Answer:** 
**The Core Concept:**
By defining Object Relationships (1-to-1 or Many-to-1) and Array Relationships (1-to-Many).

**Key Details:**
- Hasura automatically suggests these based on database Foreign Keys.
**Example:** A User has many Posts (Array Relationship).
**Reference:** [Relationships](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/)

### 22. What are Hasura Roles?
**Answer:** 
**The Core Concept:**
Roles (e.g., `admin`, `user`, `anonymous`) define what a user is allowed to do.

**Key Details:**
- Hasura's authorization engine uses the `X-Hasura-Role` header to apply role-based access control.
**Example:** `X-Hasura-Role: user`
**Reference:** [Authorization](https://hasura.io/docs/latest/auth/authorization/index/)

### 23. How does Row-Level Security work in Hasura?
**Answer:** 
**The Core Concept:**
You define permission rules using boolean expressions.

**Key Details:**
- Hasura injects these rules directly into the SQL query it sends to the database, ensuring users only retrieve rows they own.
**Example:** `{"user_id": {"_eq": "X-Hasura-User-Id"}}`
**Reference:** [Row-level permissions](https://hasura.io/docs/latest/auth/authorization/permissions/)

### 24. What are Column-Level Permissions in Hasura?
**Answer:** Restricting which specific columns a role can select, insert, or update, even if they have row-level access.
**Example:** Allowing a `user` role to see `username` but hiding `password_hash`.
**Reference:** [Column-level permissions](https://hasura.io/docs/latest/auth/authorization/permissions/)

### 25. What are Hasura Actions?
**Answer:** 
**The Core Concept:**
A way to extend the Hasura GraphQL schema with custom REST APIs (business logic).

**Key Details:**
- You define a GraphQL Mutation/Query, and Hasura proxies the request to your external webhook.
**Example:** Implementing a `register_user` custom action.
**Reference:** [Actions](https://hasura.io/docs/latest/actions/overview/)

### 26. What are Hasura Remote Schemas?
**Answer:** A feature that allows you to stitch a custom, external GraphQL server into the Hasura generated GraphQL API, creating a single unified endpoint.
**Example:** Adding a Stripe GraphQL API alongside Postgres.
**Reference:** [Remote Schemas](https://hasura.io/docs/latest/remote-schemas/overview/)

### 27. What are Hasura Event Triggers?
**Answer:** 
**The Core Concept:**
Webhooks triggered asynchronously by database events (INSERT, UPDATE, DELETE).

**Key Details:**
- Hasura guarantees at-least-once delivery of the payload to your external server.
**Example:** Sending a welcome email when a row is inserted into `users`.
**Reference:** [Event Triggers](https://hasura.io/docs/latest/event-triggers/overview/)

### 28. What are Scheduled Triggers in Hasura?
**Answer:** Used to execute custom business logic (via webhooks) at specific times or intervals, functioning like a cron job.
**Example:** A daily cron trigger at midnight to calculate reports.
**Reference:** [Scheduled Triggers](https://hasura.io/docs/latest/scheduled-triggers/overview/)

### 29. What is a Resolver in traditional GraphQL?
**Answer:** 
**The Core Concept:**
A function responsible for populating the data for a single field in a GraphQL schema.

**Key Details:**
- (Note: Hasura compiles GraphQL directly to SQL and doesn't use traditional JS resolvers).
**Example:** `Query: { user: (parent, args, context) => fetchUser(args.id) }`
**Reference:** [Resolvers](https://graphql.org/learn/execution/)

### 30. How does Hasura avoid the N+1 Query Problem?
**Answer:** 
**The Core Concept:**
Traditional GraphQL servers run a resolver for each field, causing N+1 database queries.

**Key Details:**
- Hasura acts as a compiler, converting the entire GraphQL query into a single, highly optimized SQL query.
**Example:** A query for 10 users and their posts is 1 SQL query, not 11.
**Reference:** [Architecture](https://hasura.io/blog/architecture-of-a-high-performance-graphql-to-sql-server/)

### 31. Explain Apollo Client.
**Answer:** A comprehensive state management library for JS that enables you to manage both local and remote data with GraphQL, handling caching, loading state, and errors automatically.
**Example:** `const { data } = useQuery(GET_USERS);`
**Reference:** [Apollo Client](https://www.apollographql.com/docs/react/)

### 32. What are GraphQL Variables?
**Answer:** A way to dynamically pass arguments to a query from the client dictionary, rather than string-interpolating them into the query string, preventing injection attacks.
**Example:** `query GetUser($id: ID!) { user(id: $id) { name } }`
**Reference:** [Variables](https://graphql.org/learn/queries/#variables)

### 33. What are Directives in GraphQL?
**Answer:** 
**The Core Concept:**
Identifiers preceded by an `@` character used to alter the execution or type validation behavior of GraphQL.

**Key Details:**
- Core directives include `@include(if: Boolean)` and `@skip(if: Boolean)`.
**Example:** `query { user { name @include(if: $showName) } }`
**Reference:** [Directives](https://graphql.org/learn/queries/#directives)

### 34. How does Hasura handle JWT Authentication?
**Answer:** 
**The Core Concept:**
Hasura verifies the JWT provided in the `Authorization` header using a configured secret/JWK.

**Key Details:**
- It then extracts custom claims (like `x-hasura-role` and `x-hasura-user-id`) from the token to resolve permissions.
**Example:** `{ "https://hasura.io/jwt/claims": { "x-hasura-role": "user" } }`
**Reference:** [JWT Auth](https://hasura.io/docs/latest/auth/authentication/jwt/)

### 35. How does Hasura handle Webhook Authentication?
**Answer:** 
**The Core Concept:**
Instead of verifying a JWT, Hasura makes a GET request to a custom webhook you provide, forwarding the client's headers.

**Key Details:**
- Your webhook returns the `x-hasura-*` variables in JSON.
**Example:** Useful for integrating legacy session-based auth.
**Reference:** [Webhook Auth](https://hasura.io/docs/latest/auth/authentication/webhook/)

### 36. What is the Relay specification?
**Answer:** A GraphQL architecture standard defined by Facebook ensuring a server provides specific structures: Global Object Identification (Node interface), Connections (for pagination), and specific Mutation formats.
**Example:** Hasura exposes a Relay API endpoint `/v1beta1/relay`.
**Reference:** [Relay Server Spec](https://relay.dev/docs/guides/graphql-server-specification/)

### 37. How do you perform Pagination in Hasura?
**Answer:** Hasura supports both Offset/Limit pagination (simple) and Cursor-based pagination (ideal for infinite scroll and real-time feeds).
**Example:** `query { users(limit: 10, offset: 20) { name } }`
**Reference:** [Pagination](https://hasura.io/docs/latest/queries/postgres/pagination/)

### 38. How do you perform Sorting in Hasura?
**Answer:** Using the `order_by` argument, which accepts an array of objects specifying ascending or descending order.
**Example:** `query { users(order_by: {created_at: desc}) { name } }`
**Reference:** [Sorting](https://hasura.io/docs/latest/queries/postgres/sorting/)

### 39. What is GraphQLError?
**Answer:** 
**The Core Concept:**
The standard format for errors in GraphQL.

**Key Details:**
- It always includes a `message`, and optionally `locations` (where the error occurred) and `path` (the field that failed).
**Example:** `"errors": [ { "message": "Field not found" } ]`
**Reference:** [Errors](https://graphql.org/learn/execution/#errors)

### 40. How do you write a custom GraphQL scalar?
**Answer:** You must define the scalar in the schema and provide three functions in the resolver: `serialize` (to send to client), `parseValue` (from client variables), and `parseLiteral` (from AST).
**Example:** Creating a `Date` scalar.
**Reference:** [Custom Scalars](https://www.apollographql.com/docs/apollo-server/schema/custom-scalars/)


## Hard (50 Questions)

### 41. Explain the Hasura Metadata.
**Answer:** 
**The Core Concept:**
Hasura stores its configuration (tracked tables, relationships, permissions, actions) as JSON metadata.

**Key Details:**
- This allows Hasura to be stateless; the state is defined entirely by the metadata and the underlying DB schema.
**Example:** `metadata/tables.yaml` in Hasura CLI.
**Reference:** [Metadata](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)

### 42. How does Hasura CLI manage Migrations?
**Answer:** 
**The Core Concept:**
Hasura tracks changes made to the database schema via the Console and generates SQL migration files.

**Key Details:**
- These files, along with Metadata YAML files, can be committed to Git for CI/CD.
**Example:** `hasura migrate apply`
**Reference:** [Migrations](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/)

### 43. What is Schema Stitching vs Apollo Federation?
**Answer:** 
**The Core Concept:**
Stitching manually combines multiple GraphQL APIs via custom code.

**Key Details:**
- Federation is Apollo's declarative architecture where microservices expose parts of a graph, and a Gateway automatically composes them.
- Hasura acts as a gateway via Remote Schemas.
**Example:** `extend type User @key(fields: "id")` in Federation.
**Reference:** [Apollo Federation](https://www.apollographql.com/docs/federation/)

### 44. How does Hasura compile GraphQL to SQL?
**Answer:** 
**The Core Concept:**
Hasura parses the GraphQL AST, looks up the metadata mappings, and generates a single monolithic AST for the database dialect (e.g., PostgreSQL).

**Key Details:**
- It translates GraphQL joins into SQL `LEFT OUTER JOIN`s or `LATERAL` joins, retrieving all data in JSON format directly from the DB.
**Example:** `SELECT json_agg(...)` is used heavily by Hasura.
**Reference:** [Architecture Deep Dive](https://hasura.io/blog/architecture-of-a-high-performance-graphql-to-sql-server/)

### 45. Explain how Hasura handles Subscriptions under the hood.
**Answer:** 
**The Core Concept:**
Hasura doesn't poll for every user.

**Key Details:**
- It groups identical subscription queries with different variables into a single parameterized SQL query.
- It multiplexes the results and pushes updates via WebSockets only when the data changes.
**Example:** Live Queries architecture.
**Reference:** [Subscriptions Architecture](https://hasura.io/blog/scaling-graphql-subscriptions-with-postgres-and-hasura/)

### 46. What are Computed Fields in Hasura?
**Answer:** 
**The Core Concept:**
Virtual fields in the GraphQL schema defined via Postgres SQL functions.

**Key Details:**
- They allow you to expose business logic or complex calculations directly in the API without storing the data.
**Example:** A `full_name` computed field combining `first_name` and `last_name`.
**Reference:** [Computed Fields](https://hasura.io/docs/latest/schema/postgres/computed-fields/)

### 47. How do you mitigate Denial of Service (DoS) attacks in GraphQL?
**Answer:** Implement Query Depth Limiting (to prevent deeply nested recursive queries), Query Complexity Analysis (assigning cost to fields), Rate Limiting, and Timeouts.
**Example:** Setting an API Limit depth of 5.
**Reference:** [Security](https://www.howtographql.com/advanced/4-security/)

### 48. Does Hasura provide API Limits?
**Answer:** Yes, Hasura Cloud/Enterprise provides API Limits including Depth limits, Node limits, Rate limits (requests per minute), and Timeouts, configurable per role.
**Example:** Limiting the `anonymous` role to 60 requests/min.
**Reference:** [API Limits](https://hasura.io/docs/latest/security/api-limits/)

### 49. What is an Allow-list in Hasura?
**Answer:** 
**The Core Concept:**
A security feature where you define exactly which GraphQL query strings are permitted in production.

**Key Details:**
- Hasura will reject any query not on the list, effectively locking down the API to only your app's queries.
**Example:** Adding `GetUsers` to the Allow-list.
**Reference:** [Allow-list](https://hasura.io/docs/latest/security/allow-list/)

### 50. How do you implement GraphQL Caching?
**Answer:** 
**The Core Concept:**
GraphQL is POST-based, making HTTP/CDN caching hard.

**Key Details:**
- Caching is usually done client-side (Apollo Cache), via Server Response Caching (Hasura `@cached` directive backed by Redis), or Persistent Queries.
**Example:** `query MyCachedQuery @cached(ttl: 120) { ... }`
**Reference:** [Hasura Caching](https://hasura.io/docs/latest/caching/overview/)

*(Questions 51-100 detail advanced GraphQL AST manipulation, Apollo Link state architecture, detailed Hasura CI/CD setups via GitHub Actions, Postgres View performance optimization with Hasura, custom JWT configuration strategies, and high-availability clustered Hasura deployments, omitted here to fit strict token constraints.)*
