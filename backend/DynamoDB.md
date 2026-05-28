# DynamoDB Interview Questions

This document contains a comprehensive list of essential Amazon DynamoDB interview questions, focusing on architectural patterns, key schema design, data querying techniques, and real-world NoSQL scaling.

---

## Core Concepts & Schema Design

## Basic Questions

### 1. What is Amazon DynamoDB?
**Answer:** Amazon DynamoDB is a fully managed, serverless, key-value and document NoSQL database service offered by AWS. It is designed to provide high-performance, single-digit millisecond latency at any scale.

**Key Details:**
- **Fully Managed & Serverless**: Auto-scales throughput capacity up and down to match workloads without requiring server provisioning, OS patching, or manual replication configuration.
- **Data Model**: Data is stored in tables containing items (rows), which are collections of attributes (columns). It is schema-flexible; items in the same table can have unique attributes.
- **High Availability**: Automatically replicates your data across three physical Availability Zones (AZs) in an AWS Region to ensure robust fault tolerance.

**Example:** 
Storing and retrieving session states or real-time user profiles with sub-second lookups.

**Reference:** [What is Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

---

---

---

### 2. What is a Partition Key vs. Sort Key (Composite Primary Key)?
**Answer:** 
**The Core Concept:**
A Partition Key (PK) is a single attribute that DynamoDB uses as input to an internal hash function to determine the physical partition where the item is stored. A Sort Key (SK) is a second attribute used to physically sort items with the same partition key within a partition.

**Key Details:**
- **Simple Primary Key**: Consists solely of a Partition Key. Every item in the table must have a unique PK.
- **Composite Primary Key**: Consists of both a Partition Key and a Sort Key. Items can share the same PK, but their combination of PK and SK must be globally unique.
- **Query Efficiency**: You can perform direct, ultra-fast $O(1)$ lookups on the PK, and range queries (e.g., `begins_with`, `between`, `>`, `<`) using the SK.

**Example:** 
In a messaging application, `userId` is the Partition Key, and `messageTimestamp` is the Sort Key. This allows storing multiple messages per user, sorted sequentially.

**Reference:** [DynamoDB Primary Key Spec](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey)

---

## Querying and Operations

---

## Intermediate Questions

---

## Intermediate Questions

### 3. What is the difference between a `Query` and a `Scan` operation?
**Answer:** 
**The Core Concept:**
`Query` finds items based on their primary key values, searching only the specific partition where the target data resides. `Scan` reads *every single item* in the entire table, partition-by-partition.

**Key Details:**
- **Performance**: `Query` is highly efficient ($O(1)$ partition lookup + $O(\log N)$ sort key search) and consumes minimal Read Capacity Units (RCUs). `Scan` is highly inefficient ($O(N)$ time complexity) and can easily consume all your table's provisioned RCUs, throttling your API.
- **Limits**: Both operations are capped at returning a maximum of 1 MB of data per request, requiring pagination (using `LastEvaluatedKey`).

**Comparison Table:**

| Feature | `Query` | `Scan` |
|:---|:---|:---|
| **Complexity** | ✅ $O(1)$ / $O(\log N)$ | ❌ $O(N)$ (sequential) |
| **Throughput (RCU)**| Minimal (targeted reads) | High (reads entire table) |
| **Best For** | Finding specific items or ranges | Auditing or small lookup tables |
| **Mandatory Input** | Partition Key (`KeyConditionExpression`) | None |

**Reference:** [Query vs Scan in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html)

---

---

---

### 4. What is the difference between a Filter Expression and a Scan?
**Answer:** 
**The Core Concept:**
Scanning reads every item from disk. A **Filter Expression** is applied *after* the raw data has been read from the physical partitions but *before* it is returned to the client.

**Key Details:**
- **No RCU Saving**: A Filter Expression does **not** reduce the throughput cost (RCUs) of a `Scan` or `Query` because the items are still physically read from the partitions first.
- **Bandwidth Saving**: It only reduces network payload size by filtering out unwanted data on the AWS server tier, returning only matching items to your application.
- **Pitfall**: A `Scan` with a Filter Expression can still return an empty page of results with a `LastEvaluatedKey` if the 1 MB block of scanned items did not contain any matching filters.

**Example:** 
```javascript
// Consumes RCUs for the ENTIRE table, but returns only active users over the network
const params = {
  TableName: "Users",
  FilterExpression: "status = :active",
  ExpressionAttributeValues: { ":active": "ACTIVE" }
};
await dynamoDb.scan(params).promise();
```

**Reference:** [Filter Expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#Query.FilterExpression)

---

---

## Expert Questions

---

## Expert Questions

### 5. What is a Key Condition Expression?
**Answer:** 
**The Core Concept:**
A Key Condition Expression is a query parameter that specifies the key values for the items to be read. Unlike Filter Expressions, it directly restricts the read operation to a single partition on disk, maximizing efficiency and saving RCUs.

**Key Details:**
- You **must** provide the partition key name and exact value as an equality condition (`PK = :value`).
- You can optionally provide comparison conditions for the sort key (e.g., `SK begins_with :prefix`, `SK > :date`).
- Cannot reference non-key attributes (non-key filters must go inside the `FilterExpression`).

**Example:** 
```javascript
const params = {
  TableName: "Orders",
  KeyConditionExpression: "userId = :uid AND orderDate > :date",
  ExpressionAttributeValues: {
    ":uid": "user_12345",
    ":date": "2026-01-01"
  }
};
await dynamoDb.query(params).promise();
```

**Reference:** [Query Key Condition Expression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#Query.KeyConditionExpression)

---

---

---

### 6. What are Batch Writes and Batch Reads (`BatchWriteItem` and `BatchGetItem`)?
**Answer:** 
**The Core Concept:**
Batch operations allow you to execute multiple write (put/delete) or read (get) actions across one or more tables in a single, parallelized network request, significantly reducing connection overhead.

**Key Details:**
- **Limits**:
  - **`BatchGetItem`**: Read up to 100 items or 16 MB of data.
  - **`BatchWriteItem`**: Put or delete up to 25 items or 16 MB of data.
- **Partial Failures**: If the table lacks sufficient throughput capacity, a batch operation can partially succeed. Failed items are returned in the `UnprocessedKeys` or `UnprocessedItems` properties, which the application **must** retry using an exponential backoff algorithm.
- **No Transactions**: Batch operations are not atomic. If item 5 fails, items 1-4 remain committed. For atomic transactions, use `TransactWriteItems` and `TransactGetItems`.

**Example:** 
```javascript
// Bulk writing up to 25 users in a single request
const params = {
  RequestItems: {
    "Users": [
      { PutRequest: { Item: { userId: "1", name: "Alice" } } },
      { PutRequest: { Item: { userId: "2", name: "Bob" } } }
    ]
  }
};
const res = await dynamoDb.batchWrite(params).promise();
// check res.UnprocessedItems for retries!
```

**Reference:** [DynamoDB Batch Operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices-many-items.html)

---

---

## Technical Questions

---

### 1. Write a Node.js script to query DynamoDB using the AWS SDK v3.

**Example Solution:**
```javascript
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, QueryCommand } = require("@aws-sdk/lib-dynamodb");

const client = new DynamoDBClient({ region: "us-east-1" });
const ddbDocClient = DynamoDBDocumentClient.from(client);

async function getOrdersByCustomer(customerId) {
  const command = new QueryCommand({
    TableName: "OrdersTable",
    KeyConditionExpression: "CustomerId = :customerId AND OrderDate >= :since",
    ExpressionAttributeValues: {
      ":customerId": customerId,
      ":since": "2026-01-01"
    }
  });

  const response = await ddbDocClient.send(command);
  return response.Items;
}
```

---

### 2. Implement Transactional Writes (TransactWriteItems) in DynamoDB.

**Example Solution:**
```javascript
const { TransactWriteCommand } = require("@aws-sdk/lib-dynamodb");

async function purchaseProduct(customerId, productId, price) {
  const command = new TransactWriteCommand({
    TransactItems: [
      {
        Update: {
          TableName: "UsersTable",
          Key: { CustomerId: customerId },
          UpdateExpression: "SET balance = balance - :price",
          ConditionExpression: "balance >= :price",
          ExpressionAttributeValues: { ":price": price }
        }
      },
      {
        Put: {
          TableName: "OrdersTable",
          Item: {
            OrderId: `ORD#\${Date.now()}`,
            CustomerId: customerId,
            ProductId: productId,
            Price: price,
            PurchaseDate: new Date().toISOString()
          }
        }
      }
    ]
  });

  await ddbDocClient.send(command);
}
```

---

## Technical Questions

### 1. Write a Node.js script to query DynamoDB using the AWS SDK v3.

**Example Solution:**
```javascript
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, QueryCommand } = require("@aws-sdk/lib-dynamodb");

const client = new DynamoDBClient({ region: "us-east-1" });
const ddbDocClient = DynamoDBDocumentClient.from(client);

async function getOrdersByCustomer(customerId) {
  const command = new QueryCommand({
    TableName: "OrdersTable",
    KeyConditionExpression: "CustomerId = :customerId AND OrderDate >= :since",
    ExpressionAttributeValues: {
      ":customerId": customerId,
      ":since": "2026-01-01"
    }
  });

  const response = await ddbDocClient.send(command);
  return response.Items;
}
```

### 2. Implement Transactional Writes (TransactWriteItems) in DynamoDB.

**Example Solution:**
```javascript
const { TransactWriteCommand } = require("@aws-sdk/lib-dynamodb");

async function purchaseProduct(customerId, productId, price) {
  const command = new TransactWriteCommand({
    TransactItems: [
      {
        Update: {
          TableName: "UsersTable",
          Key: { CustomerId: customerId },
          UpdateExpression: "SET balance = balance - :price",
          ConditionExpression: "balance >= :price",
          ExpressionAttributeValues: { ":price": price }
        }
      },
      {
        Put: {
          TableName: "OrdersTable",
          Item: {
            OrderId: `ORD#\${Date.now()}`,
            CustomerId: customerId,
            ProductId: productId,
            Price: price,
            PurchaseDate: new Date().toISOString()
          }
        }
      }
    ]
  });

  await ddbDocClient.send(command);
}
```

### 3. Write a conditional update script utilizing optimistic locking in DynamoDB.

**Example Solution:**
```javascript
const { UpdateCommand } = require("@aws-sdk/lib-dynamodb");

async function updateInventory(productId, quantity, expectedVersion) {
  const command = new UpdateCommand({
    TableName: "Inventory",
    Key: { ProductId: productId },
    UpdateExpression: "SET qty = qty - :qty, version = version + :one",
    ConditionExpression: "version = :expectedVersion AND qty >= :qty",
    ExpressionAttributeValues: {
      ":qty": quantity,
      ":expectedVersion": expectedVersion,
      ":one": 1
    }
  });
  await ddbDocClient.send(command);
}
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a DynamoDB & NoSQL Modeling application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy DynamoDB & NoSQL Modeling operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of DynamoDB & NoSQL Modeling configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using DynamoDB & NoSQL Modeling event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing DynamoDB & NoSQL Modeling with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output DynamoDB & NoSQL Modeling performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during DynamoDB & NoSQL Modeling failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to DynamoDB & NoSQL Modeling data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving DynamoDB & NoSQL Modeling state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates DynamoDB & NoSQL Modeling logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle DynamoDB & NoSQL Modeling files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking DynamoDB & NoSQL Modeling connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using DynamoDB & NoSQL Modeling.

*(Challenge question for self-study and practical project implementation.)*

