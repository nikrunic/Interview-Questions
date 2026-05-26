# Hasura GraphQL: The Complete Beginner-to-Architect Masterclass

**Hasura** is an open-source engine that connects to your databases and microservices and instantly gives you a production-ready **GraphQL API** — with real-time subscriptions, fine-grained authorization, event-driven workflows, and multi-source federation — all without writing a single resolver.

This guide starts from GraphQL fundamentals (for developers coming from REST), then progressively builds through the full Hasura platform — from Console-driven rapid prototyping to enterprise-grade, multi-tenant, event-driven architectures. Every concept is explained in plain language with real-world analogies, production-ready code, and architectural diagrams.

---

## 🗺️ The Enterprise Architect Roadmap

```mermaid
graph TD
    A["Phase 1: Beginner Level<br/>(GraphQL Fundamentals)"]
    B["Phase 2: Intermediate Level<br/>(Hasura Instant APIs & Console)"]
    C["Phase 3: Advanced Level<br/>(Permissions, Auth & Real-Time)"]
    D["Phase 4: Expert Level<br/>(Actions, Event Triggers & Remote Schemas)"]
    E["Phase 5: Technical Architect Level<br/>(Federation, Performance & Enterprise)"]
    
    A --> B
    B --> C
    C --> D
    D --> E
```

| Phase | Target Role | Key Focus Area | Capstone Project |
| :--- | :--- | :--- | :--- |
| **Phase 1: Beginner** | Frontend Developer | GraphQL queries, mutations, subscriptions, schema, types. | Query a public GraphQL API from the browser |
| **Phase 2: Intermediate** | Fullstack Developer | Hasura Console, instant APIs, relationships, filtering, aggregations. | Task-management API (users, projects, tasks) |
| **Phase 3: Advanced** | Platform Engineer | Row-level permissions, JWT/Webhook auth, real-time subscriptions. | Multi-tenant project board with live updates |
| **Phase 4: Expert** | Backend Architect | Actions, Event Triggers, Remote Schemas, Hasura CLI migrations. | E-commerce backend with Stripe Actions & Event Triggers |
| **Phase 5: Architect** | Enterprise Architect | Federation, Remote Joins, query performance, caching, observability. | Multi-source data gateway federating Postgres + REST + GraphQL |

---

## 🚀 Phase 1: Beginner Level (GraphQL Fundamentals)

### 1. What is GraphQL?

#### 💡 The Waiter's Order Pad Analogy:
Imagine two restaurants:

**Restaurant REST** has a fixed combo menu. You order "Combo #5" and receive a burger, fries, a drink, coleslaw, and dessert — even if you only wanted the burger and drink. If you also want soup from Combo #3, you have to place a completely separate order and wait for a second tray. That's **over-fetching** (getting data you don't need) and **under-fetching** (needing multiple requests to get everything you want).

**Restaurant GraphQL** gives the waiter a blank order pad. You write exactly what you want: "One burger, one drink, and one soup." The waiter goes to the kitchen once and returns with precisely your order — nothing more, nothing less, all in one trip.

**GraphQL** is a query language for your API where the **client** decides the shape and depth of the response, not the server.

---

### 2. REST vs. GraphQL — Side by Side

| Feature | REST | GraphQL |
| :--- | :--- | :--- |
| **Endpoint structure** | Multiple endpoints (`/users`, `/users/1/posts`) | Single endpoint (`/graphql`) |
| **Data shape** | Server decides what fields to return | Client specifies exact fields needed |
| **Over-fetching** | Common — you get the entire resource | Eliminated — request only needed fields |
| **Under-fetching** | Common — multiple round-trips needed | Eliminated — nested data in one query |
| **Versioning** | `/api/v1/`, `/api/v2/` | No versions — evolve schema with deprecation |
| **Real-time** | Requires separate WebSocket implementation | Built-in via Subscriptions |
| **Typing** | Loosely typed (relies on docs) | Strongly typed schema (self-documenting) |

---

### 3. The Three Operations

GraphQL has exactly three operation types:

#### a) Query (READ data)
```graphql
# Fetch exactly the fields you need — nothing more
query GetUser {
  user(id: 42) {
    name
    email
    posts {
      title
      createdAt
    }
  }
}
```

**Response** (mirrors the query shape exactly):
```json
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com",
      "posts": [
        { "title": "GraphQL 101", "createdAt": "2025-01-15" },
        { "title": "Hasura Deep Dive", "createdAt": "2025-03-22" }
      ]
    }
  }
}
```

#### b) Mutation (WRITE / UPDATE / DELETE data)
```graphql
mutation CreatePost {
  insert_post(object: { title: "My New Post", user_id: 42 }) {
    id
    title
    created_at
  }
}
```

#### c) Subscription (REAL-TIME stream)
```graphql
# Opens a persistent WebSocket connection
# Server pushes updates whenever data changes
subscription LiveComments {
  comments(where: { post_id: { _eq: 99 } }, order_by: { created_at: desc }) {
    id
    text
    author {
      name
    }
  }
}
```

---

### 4. Schema, Types & Resolvers

Every GraphQL API is backed by a **schema** — a contract that defines every type, field, and operation available.

```graphql
# Schema Definition Language (SDL)
type User {
  id: ID!                  # Non-nullable unique identifier
  name: String!            # Non-nullable string
  email: String!
  age: Int                 # Nullable integer
  posts: [Post!]!          # Non-nullable array of non-nullable Posts
}

type Post {
  id: ID!
  title: String!
  content: String
  author: User!            # Relationship back to User
  createdAt: String!
}

type Query {
  user(id: ID!): User      # Entry point for reading a user
  posts: [Post!]!          # Entry point for reading all posts
}

type Mutation {
  createPost(title: String!, content: String, userId: ID!): Post!
}
```

**Key Type System Rules:**
| Symbol | Meaning | Example |
| :--- | :--- | :--- |
| `String` | Nullable string | Field can return `null` |
| `String!` | Non-nullable string | Field **must** return a value |
| `[Post]` | Nullable array of nullable Posts | Can be `null`, items can be `null` |
| `[Post!]!` | Non-nullable array of non-nullable Posts | Array always exists, every item exists |

---

### 5. Variables, Fragments & Aliases

#### Variables (parameterize queries for reuse):
```graphql
query GetUser($userId: ID!) {
  user(id: $userId) {
    name
    email
  }
}

# Variables JSON:
# { "userId": "42" }
```

#### Fragments (reusable field sets):
```graphql
fragment UserFields on User {
  id
  name
  email
}

query {
  user(id: 42) {
    ...UserFields
    posts { title }
  }
}
```

#### Aliases (rename fields to avoid collisions):
```graphql
query {
  admin: user(id: 1) {
    name
  }
  viewer: user(id: 42) {
    name
  }
}
# Returns: { "admin": { "name": "..." }, "viewer": { "name": "..." } }
```

---

## 🛠️ Phase 2: Intermediate Level (Hasura Instant APIs & Console)

### 1. What is Hasura?

#### 💡 The Universal Translator Analogy:
Imagine the United Nations General Assembly. Delegates speak dozens of different languages, and a team of **simultaneous translators** sits in a booth, listening to every speaker and instantly converting their words into every other language — in real-time, with perfect accuracy, and without anyone needing to write translation scripts in advance.

**Hasura** is that translator booth for your data. Your PostgreSQL database "speaks SQL." Your frontend application "speaks GraphQL." Hasura sits between them and **instantly translates** every table, column, and relationship into a fully-typed, real-time GraphQL API. You don't write resolvers. You don't define schemas manually. You connect a database, and the API exists.

```
┌──────────────┐      ┌───────────────────┐      ┌──────────────────┐
│   Frontend   │      │      HASURA       │      │   PostgreSQL     │
│   (React,    │─────▶│   GraphQL Engine   │─────▶│   Database       │
│   Next.js)   │◀─────│                   │◀─────│                  │
│              │  GQL │  • Auto-generates  │  SQL │  • users table   │
│              │      │    schema from DB  │      │  • posts table   │
│              │      │  • Permissions     │      │  • comments tbl  │
│              │      │  • Subscriptions   │      │  • foreign keys  │
└──────────────┘      └───────────────────┘      └──────────────────┘
```

---

### 2. Setting Up Hasura (Docker Compose)

The fastest way to run Hasura locally is via Docker:

```yaml
# docker-compose.yml
version: '3.6'
services:
  postgres:
    image: postgres:16
    restart: always
    environment:
      POSTGRES_PASSWORD: postgrespassword
    volumes:
      - db_data:/var/lib/postgresql/data

  hasura:
    image: hasura/graphql-engine:v2.40.0
    ports:
      - "8080:8080"
    restart: always
    environment:
      HASURA_GRAPHQL_DATABASE_URL: postgres://postgres:postgrespassword@postgres:5432/postgres
      HASURA_GRAPHQL_ENABLE_CONSOLE: "true"
      HASURA_GRAPHQL_ADMIN_SECRET: myadminsecret
      HASURA_GRAPHQL_DEV_MODE: "true"
    depends_on:
      - postgres

volumes:
  db_data:
```

```bash
# Start everything
docker-compose up -d

# Open Hasura Console at http://localhost:8080/console
```

---

### 3. Tracking Tables & Relationships

Once your database has tables, Hasura auto-detects them. You **track** a table to expose it via the GraphQL API.

#### Creating Tables (via Hasura Console → SQL tab):
```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  role TEXT DEFAULT 'viewer',
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Projects table
CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  owner_id INTEGER REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Tasks table
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  status TEXT DEFAULT 'todo',
  project_id INTEGER REFERENCES projects(id),
  assignee_id INTEGER REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT now()
);
```

After tracking these tables, Hasura automatically generates:

| Generated Operation | Example |
| :--- | :--- |
| `query { users { ... } }` | Fetch all users |
| `query { users_by_pk(id: 1) { ... } }` | Fetch single user by primary key |
| `mutation { insert_users_one(...) { ... } }` | Insert a single user |
| `mutation { insert_users(...) { ... } }` | Bulk insert users |
| `mutation { update_users_by_pk(...) { ... } }` | Update a user by PK |
| `mutation { delete_users_by_pk(...) { ... } }` | Delete a user by PK |
| `subscription { users { ... } }` | Real-time stream of user changes |

---

### 4. Relationships (Object & Array)

Foreign keys in your database become **relationships** in GraphQL, enabling nested queries.

| Relationship Type | DB Pattern | GraphQL Effect | Example |
| :--- | :--- | :--- | :--- |
| **Object Relationship** | `tasks.assignee_id → users.id` | Returns a single nested object | `task { assignee { name } }` |
| **Array Relationship** | `users.id ← tasks.assignee_id` | Returns an array of nested objects | `user { tasks { title status } }` |

#### Nested Query (joining 3 tables in one request):
```graphql
query GetProjectBoard {
  projects {
    id
    title
    owner {                    # Object relationship → users
      name
    }
    tasks {                    # Array relationship → tasks
      title
      status
      assignee {               # Object relationship → users
        name
        email
      }
    }
  }
}
```

> This single GraphQL query replaces what would require **3 separate REST endpoints** and manual client-side data stitching.

---

### 5. Filtering, Sorting & Pagination

Hasura generates powerful filtering operators for every column type:

```graphql
query FilteredTasks {
  tasks(
    where: {
      status: { _eq: "in_progress" },          # Exact match
      assignee: { name: { _ilike: "%alice%" } }, # Case-insensitive pattern
      created_at: { _gte: "2025-01-01" }        # Greater than or equal
    },
    order_by: { created_at: desc },              # Sort descending
    limit: 10,                                    # Page size
    offset: 20                                    # Skip first 20
  ) {
    id
    title
    status
    assignee { name }
  }
}
```

#### Comparison Operators Reference:
| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `_eq` | Equal | `{ status: { _eq: "done" } }` |
| `_neq` | Not equal | `{ role: { _neq: "admin" } }` |
| `_gt`, `_gte` | Greater than / or equal | `{ age: { _gte: 18 } }` |
| `_lt`, `_lte` | Less than / or equal | `{ price: { _lt: 100 } }` |
| `_in` | In a list | `{ status: { _in: ["todo", "in_progress"] } }` |
| `_like`, `_ilike` | Pattern match (case-sensitive / insensitive) | `{ name: { _ilike: "%search%" } }` |
| `_is_null` | Is null check | `{ deleted_at: { _is_null: true } }` |

---

### 6. Aggregation Queries

```graphql
query ProjectStats {
  tasks_aggregate(where: { project_id: { _eq: 5 } }) {
    aggregate {
      count                     # Total tasks in project
      avg { estimated_hours }   # Average estimated hours
      max { estimated_hours }
      min { estimated_hours }
    }
    nodes {                     # Return matching rows alongside aggregates
      title
      status
    }
  }
}
```

---

## ⚡ Phase 3: Advanced Level (Permissions, Auth & Real-Time)

### 1. Hasura's Permission System

#### 💡 The Building Security Card Analogy:
Imagine a large corporate office building. Every employee receives a **security access card**. But not all cards are equal:
- The **CEO's card** opens every floor, every room, every safe.
- A **Marketing Manager's card** opens the marketing floor, the shared kitchen, and the conference rooms — but not the server room or HR's filing cabinets.
- An **Intern's card** opens the front lobby and their own desk area — nothing else.

The building's security system doesn't ask you to write custom code for each door. You configure a **permission matrix**: *"Role X can access Room Y under Condition Z."*

Hasura works exactly this way. You define permissions per **role**, per **table**, per **operation** (select/insert/update/delete), with **row-level** and **column-level** granularity. The engine enforces them automatically on every request.

---

### 2. Permission Architecture

Permissions are defined as a matrix of **Role × Table × Operation → Rules**:

```
┌─────────────────────────────────────────────────────────┐
│                    PERMISSION MATRIX                     │
├──────────┬──────────┬────────┬────────────┬─────────────┤
│   Role   │  Table   │  Op    │ Row Filter │  Columns    │
├──────────┼──────────┼────────┼────────────┼─────────────┤
│  admin   │  tasks   │ select │  {}  (all) │  all        │
│  admin   │  tasks   │ insert │  {}  (all) │  all        │
│  admin   │  tasks   │ update │  {}  (all) │  all        │
│  admin   │  tasks   │ delete │  {}  (all) │  —          │
├──────────┼──────────┼────────┼────────────┼─────────────┤
│  user    │  tasks   │ select │ assignee_id│  id, title, │
│          │          │        │ = user_id  │  status     │
│  user    │  tasks   │ insert │ assignee_id│  title,     │
│          │          │        │ = user_id  │  project_id │
│  user    │  tasks   │ update │ assignee_id│  status     │
│          │          │        │ = user_id  │  only       │
│  user    │  tasks   │ delete │  ✗ denied  │  —          │
├──────────┼──────────┼────────┼────────────┼─────────────┤
│  viewer  │  tasks   │ select │ project is │  id, title, │
│          │          │        │ public     │  status     │
│  viewer  │  tasks   │ insert │  ✗ denied  │  —          │
│  viewer  │  tasks   │ update │  ✗ denied  │  —          │
│  viewer  │  tasks   │ delete │  ✗ denied  │  —          │
└──────────┴──────────┴────────┴────────────┴─────────────┘
```

#### Row-Level Permission (JSON rule):
```json
// "user" role can only SELECT tasks assigned to them
{
  "assignee_id": {
    "_eq": "X-Hasura-User-Id"    // Session variable injected from JWT
  }
}
```

#### Column-Level Permission:
Restrict which columns a role can see. For example, the `user` role can read `id`, `title`, `status` but **not** `internal_notes` or `cost_estimate`.

---

### 3. Authentication Modes

Hasura itself does **not** handle login/signup. It verifies identity through one of two modes:

| Mode | How it Works | Best For |
| :--- | :--- | :--- |
| **JWT Mode** | Frontend sends a JWT token. Hasura verifies the signature and extracts `x-hasura-role`, `x-hasura-user-id` from claims. | Most production apps (Firebase Auth, Auth0, Clerk) |
| **Webhook Mode** | Hasura forwards every request to your webhook endpoint. Your server validates the session and returns role/user-id. | Custom auth systems, legacy integrations |

#### JWT Claims Example:
```json
{
  "sub": "user-42",
  "iat": 1700000000,
  "https://hasura.io/jwt/claims": {
    "x-hasura-default-role": "user",
    "x-hasura-allowed-roles": ["user", "admin"],
    "x-hasura-user-id": "42",
    "x-hasura-org-id": "org-7"
  }
}
```

#### Hasura Environment Configuration:
```bash
# JWT Mode
HASURA_GRAPHQL_JWT_SECRET='{"type":"RS256","jwk_url":"https://your-auth-provider.com/.well-known/jwks.json"}'

# Webhook Mode
HASURA_GRAPHQL_AUTH_HOOK=https://your-server.com/api/hasura-auth
HASURA_GRAPHQL_AUTH_HOOK_MODE=GET
```

---

### 4. Real-Time Subscriptions

Hasura turns any query into a live subscription by replacing the `query` keyword with `subscription`. Under the hood, it uses **WebSockets** and polls the database efficiently.

```graphql
# Live-updating task board — pushes changes instantly to all connected clients
subscription LiveProjectBoard($projectId: Int!) {
  tasks(
    where: { project_id: { _eq: $projectId } },
    order_by: { updated_at: desc }
  ) {
    id
    title
    status
    assignee {
      name
      avatar_url
    }
    updated_at
  }
}
```

#### Frontend Integration (React + Apollo Client):
```tsx
import { useSubscription, gql } from '@apollo/client';

const LIVE_TASKS = gql`
  subscription LiveTasks($projectId: Int!) {
    tasks(where: { project_id: { _eq: $projectId } }, order_by: { updated_at: desc }) {
      id
      title
      status
      assignee { name }
    }
  }
`;

function TaskBoard({ projectId }: { projectId: number }) {
  const { data, loading, error } = useSubscription(LIVE_TASKS, {
    variables: { projectId }
  });

  if (loading) return <p>Connecting to live feed...</p>;
  if (error) return <p>Subscription error: {error.message}</p>;

  return (
    <ul>
      {data.tasks.map((task: any) => (
        <li key={task.id}>
          [{task.status}] {task.title} — {task.assignee?.name}
        </li>
      ))}
    </ul>
  );
}
```

---

## 🧬 Phase 4: Expert Level (Actions, Event Triggers & Remote Schemas)

### 1. Actions (Custom Business Logic)

**Actions** extend Hasura's auto-generated schema with custom queries or mutations backed by your own REST/serverless endpoints. Hasura sends a structured payload to your handler and returns the result as part of the GraphQL response.

```
┌────────────┐     GraphQL      ┌─────────────┐     HTTP POST     ┌──────────────────┐
│   Client   │ ───────────────▶ │    Hasura    │ ────────────────▶ │  Your Action     │
│            │ ◀─────────────── │   Engine     │ ◀──────────────── │  Handler         │
│            │     Response     │             │      JSON         │  (Node/Python/   │
│            │                  │             │                   │   Serverless)    │
└────────────┘                  └─────────────┘                   └──────────────────┘
```

#### Step 1: Define the Action (in Hasura Console → Actions):
```graphql
# Action Definition
type Mutation {
  processPayment(
    amount: Int!
    currency: String!
    customer_id: Int!
  ): PaymentResult!
}

# Custom Output Type
type PaymentResult {
  payment_id: String!
  status: String!
  receipt_url: String
}
```

#### Step 2: Write the Handler (Node.js/Express):
```typescript
// /api/process-payment.ts
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export default async function handler(req: any, res: any) {
  // Hasura sends the Action input and session variables
  const { input, session_variables } = req.body;
  const { amount, currency, customer_id } = input;

  // Session variable injected from JWT
  const userId = session_variables['x-hasura-user-id'];

  try {
    const paymentIntent = await stripe.paymentIntents.create({
      amount,
      currency,
      metadata: { customer_id: String(customer_id), user_id: userId }
    });

    // Return the shape matching the Action's output type
    res.json({
      payment_id: paymentIntent.id,
      status: paymentIntent.status,
      receipt_url: paymentIntent.charges?.data[0]?.receipt_url ?? null
    });
  } catch (error: any) {
    res.status(400).json({ message: error.message });
  }
}
```

---

### 2. Event Triggers

#### 💡 The Tripwire Analogy:
Imagine a museum exhibit room. Thin laser beams (tripwires) crisscross the floor invisibly. The moment someone **crosses a beam** (a database row is inserted, updated, or deleted), an alarm fires automatically — notifying security, locking doors, and activating cameras. The museum staff doesn't manually watch every exhibit 24/7; the tripwires **react to changes**.

**Event Triggers** work identically. You configure a trigger on a table for specific operations (INSERT/UPDATE/DELETE). When that event occurs in the database, Hasura automatically fires an HTTP webhook to your service — reliably, with at-least-once delivery and automatic retries.

```
┌──────────────┐  INSERT/UPDATE  ┌───────────────┐   HTTP POST    ┌─────────────────────┐
│  PostgreSQL  │ ──────────────▶ │    Hasura      │ ─────────────▶ │  Your Webhook       │
│  Database    │                 │  Event Trigger │                │  • Send email       │
│              │                 │  System        │                │  • Sync to Stripe   │
│  (row change │                 │                │                │  • Index in Elastic │
│   detected)  │                 │  Retries on    │                │  • Push notification│
└──────────────┘                 │  failure       │                └─────────────────────┘
                                 └───────────────┘
```

#### Event Trigger Configuration (via Console or Metadata):
```yaml
# metadata/databases/default/tables/public_orders.yaml
event_triggers:
  - name: order_confirmed
    definition:
      enable_manual: false
      insert:
        columns: '*'
      update:
        columns:
          - status
    retry_conf:
      num_retries: 5
      interval_sec: 30
      timeout_sec: 60
    webhook: https://your-api.com/webhooks/order-confirmed
    headers:
      - name: X-Webhook-Secret
        value_from_env: WEBHOOK_SECRET
```

#### Webhook Handler:
```typescript
// /api/webhooks/order-confirmed.ts
export default async function handler(req: any, res: any) {
  const { event, table, trigger } = req.body;
  const { op, data } = event;  // op = "INSERT" | "UPDATE" | "DELETE"

  const newRow = data.new;      // The new row state
  const oldRow = data.old;      // The previous row state (for UPDATE/DELETE)

  if (op === 'UPDATE' && newRow.status === 'confirmed') {
    // Send confirmation email
    await sendEmail({
      to: newRow.customer_email,
      subject: `Order #${newRow.id} Confirmed`,
      body: `Your order of $${newRow.total} has been confirmed.`
    });

    // Sync to Stripe for invoicing
    await createStripeInvoice(newRow);
  }

  res.json({ success: true });
}
```

---

### 3. Remote Schemas (GraphQL Federation)

**Remote Schemas** let you stitch an external GraphQL API into Hasura's unified schema. Your frontend queries Hasura's single endpoint, and Hasura routes specific fields to the remote service transparently.

```
┌──────────┐       ┌──────────────────────────────┐
│  Client   │──────▶│         HASURA               │
│           │◀──────│   Unified GraphQL Endpoint   │
└──────────┘       │                              │
                   │  ┌─────────────┐             │
                   │  │ PostgreSQL  │  (local)    │
                   │  │ users,tasks │             │
                   │  └─────────────┘             │
                   │                              │
                   │  ┌─────────────┐             │
                   │  │ Inventory   │  (remote)   │
                   │  │ GraphQL API │             │
                   │  └─────────────┘             │
                   │                              │
                   │  ┌─────────────┐             │
                   │  │ Analytics   │  (remote)   │
                   │  │ GraphQL API │             │
                   │  └─────────────┘             │
                   └──────────────────────────────┘
```

#### Adding a Remote Schema (Hasura Console):
```json
{
  "url": "https://inventory-service.internal/graphql",
  "headers": {
    "Authorization": "Bearer ${INVENTORY_SERVICE_TOKEN}"
  },
  "forward_client_headers": true,
  "timeout_seconds": 30
}
```

---

### 4. Hasura CLI & Migrations

For production workflows, never use the Console to make schema changes directly. Use the **Hasura CLI** to version-control migrations and metadata.

```bash
# Initialize Hasura project
hasura init my-project --endpoint http://localhost:8080 --admin-secret myadminsecret

# Create a migration from current database state
hasura migrate create "init" --from-server --database-name default

# Apply migrations
hasura migrate apply --database-name default

# Export metadata (permissions, relationships, event triggers, actions)
hasura metadata export

# Apply metadata
hasura metadata apply

# Open console through CLI (tracks changes as migration files)
hasura console
```

#### Project Directory Structure:
```
my-project/
├── config.yaml
├── metadata/
│   ├── actions.graphql
│   ├── actions.yaml
│   ├── remote_schemas.yaml
│   └── databases/
│       └── default/
│           └── tables/
│               ├── public_users.yaml       # Permissions, relationships
│               ├── public_projects.yaml
│               └── public_tasks.yaml
├── migrations/
│   └── default/
│       ├── 1700000000000_init/
│       │   ├── up.sql                      # Schema changes (forward)
│       │   └── down.sql                    # Rollback (reverse)
│       └── 1700000001000_add_status_column/
│           ├── up.sql
│           └── down.sql
└── seeds/
    └── default/
        └── seed_data.sql                    # Test data
```

---

## 🏛️ Phase 5: Technical Architect Level (Federation, Performance & Enterprise)

### 1. Deployment Targets

| Target | Best For | Trade-Offs |
| :--- | :--- | :--- |
| **Hasura Cloud** | Fastest setup, managed infrastructure, built-in monitoring, auto-scaling. | Usage-based pricing, less infra control. |
| **Docker (self-hosted)** | Full control, runs on any cloud (AWS ECS, GCP Cloud Run). | You manage scaling, upgrades, and HA. |
| **Kubernetes** | Enterprise-grade HA, horizontal scaling, GitOps deployments. | Operational complexity, K8s expertise required. |

#### Production Docker Compose:
```yaml
services:
  hasura:
    image: hasura/graphql-engine:v2.40.0
    ports:
      - "8080:8080"
    environment:
      HASURA_GRAPHQL_DATABASE_URL: "${DATABASE_URL}"
      HASURA_GRAPHQL_ADMIN_SECRET: "${ADMIN_SECRET}"
      HASURA_GRAPHQL_ENABLE_CONSOLE: "false"         # Disable in production
      HASURA_GRAPHQL_DEV_MODE: "false"                # Disable in production
      HASURA_GRAPHQL_ENABLED_LOG_TYPES: "startup, http-log, query-log"
      HASURA_GRAPHQL_JWT_SECRET: '{"type":"RS256","jwk_url":"${AUTH_JWKS_URL}"}'
      HASURA_GRAPHQL_UNAUTHORIZED_ROLE: "anonymous"   # Default role for unauthenticated requests
      HASURA_GRAPHQL_CORS_DOMAIN: "https://myapp.com"
    restart: always
```

---

### 2. Query Performance & Optimization

Hasura translates every GraphQL query into a **single SQL statement** (no N+1 queries). But complex queries on large tables still need database-level optimization.

#### Analyzing Generated SQL:
```graphql
# Use the "Analyze" button in Hasura Console API Explorer
# It shows the exact SQL Hasura generates:
query {
  tasks(where: { status: { _eq: "in_progress" } }) {
    title
    assignee { name }
  }
}
```

Generated SQL:
```sql
SELECT
  t.title,
  u.name AS assignee_name
FROM tasks t
LEFT JOIN users u ON t.assignee_id = u.id
WHERE t.status = 'in_progress';
```

#### Performance Checklist:
| Optimization | Action |
| :--- | :--- |
| **Indexes** | Add indexes on columns used in `where`, `order_by`, and foreign keys. |
| **Connection pooling** | Use PgBouncer between Hasura and Postgres for high-concurrency workloads. |
| **Query depth limiting** | Set `HASURA_GRAPHQL_MAX_DEPTH` to prevent deeply nested abuse queries. |
| **Allow-lists** | In production, restrict to only pre-approved queries (prevent arbitrary queries). |
| **Subscription polling** | Tune `HASURA_GRAPHQL_LIVE_QUERIES_MULTIPLEXED_REFETCH_INTERVAL` (default 1s). |

---

### 3. Caching (`@cached` Directive)

Hasura Cloud supports query-level caching with the `@cached` directive. Responses are served from a CDN edge cache.

```graphql
query CachedProducts @cached(ttl: 300) {   # Cache for 5 minutes
  products(order_by: { popularity: desc }, limit: 50) {
    id
    name
    price
    image_url
  }
}
```

| Feature | Detail |
| :--- | :--- |
| **TTL** | Time-to-live in seconds. Default: 60s. |
| **Cache key** | Computed from the query, variables, and role. |
| **Invalidation** | Automatic after TTL expires. Manual via admin API. |
| **Scope** | Per-role — `admin` and `user` get separate cached results. |

---

### 4. Remote Joins (Cross-Source Federation)

**Remote Joins** let you create relationships between your local database tables and remote data sources (REST APIs, other GraphQL services, other databases) — all queryable in a single GraphQL request.

```
┌──────────────────────────────────────────────────────────────────┐
│                    HASURA SUPERGRAPH                              │
│                                                                  │
│  ┌─────────────┐    Remote Join    ┌──────────────────────────┐  │
│  │ PostgreSQL  │ ─────────────────▶│ Stripe REST API          │  │
│  │ orders tbl  │                   │ GET /v1/charges/{id}     │  │
│  │ (local)     │                   │ (Action-backed)          │  │
│  └─────────────┘                   └──────────────────────────┘  │
│                                                                  │
│  ┌─────────────┐    Remote Join    ┌──────────────────────────┐  │
│  │ PostgreSQL  │ ─────────────────▶│ Inventory GraphQL API    │  │
│  │ products    │                   │ (Remote Schema)          │  │
│  │ (local)     │                   │                          │  │
│  └─────────────┘                   └──────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

#### Unified Query Across Sources:
```graphql
query OrderWithPaymentAndInventory {
  orders(where: { customer_id: { _eq: 42 } }) {
    id
    total
    created_at

    # Remote Join → Stripe REST API (via Action)
    payment_details {
      stripe_charge_id
      status
      receipt_url
    }

    # Remote Join → Inventory GraphQL (via Remote Schema)
    line_items {
      product {
        warehouse_stock     # Lives in a different service
        estimated_delivery
      }
    }
  }
}
```

---

### 5. Observability & Production Security

#### OpenTelemetry Integration:
```bash
# Enable tracing export
HASURA_GRAPHQL_ENABLED_APIS=metadata,graphql,config
HASURA_GRAPHQL_ENABLE_TELEMETRY=true

# Export to Jaeger / Datadog / New Relic
HASURA_GRAPHQL_OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
HASURA_GRAPHQL_OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```

#### Production Security Checklist:
| Security Measure | Configuration |
| :--- | :--- |
| **Disable Console** | `HASURA_GRAPHQL_ENABLE_CONSOLE: "false"` |
| **Disable Dev Mode** | `HASURA_GRAPHQL_DEV_MODE: "false"` |
| **Allow-List** | Only permit pre-approved queries (block introspection in prod). |
| **Rate Limiting** | Use an API gateway (e.g., Kong, Nginx) in front of Hasura. |
| **CORS** | Restrict to your domain: `HASURA_GRAPHQL_CORS_DOMAIN`. |
| **Admin Secret Rotation** | Rotate `HASURA_GRAPHQL_ADMIN_SECRET` periodically. |
| **Query Depth Limit** | Set `HASURA_GRAPHQL_MAX_DEPTH` to prevent abuse. |
| **Introspection** | Disable in production: `HASURA_GRAPHQL_ENABLE_INTROSPECTION: "false"`. |
