# NoSQL: DynamoDB & Redis — Complete Interview Guide

This guide compiles 20 essential NoSQL, Amazon DynamoDB, and Redis interview questions and answers, formatted according to the repository's strict formatting standards.

---



---

## Table of Contents

- [Basic Questions](#basic-questions)
- [Intermediate Questions](#intermediate-questions)
- [Expert Questions](#expert-questions)
- [Technical Questions](#technical-questions)

---

## Basic Questions

### 1. Difference between Query and Scan / When to use which?

**Answer:**
**The Core Concept:**
A **Query** searches a DynamoDB table based on the Partition Key (and optionally the Sort Key), fetching only matching items. A **Scan** reads every single item in the entire table or index, evaluating every record against filter criteria.

**Key Details:**
- **Performance:** Query is extremely fast ($O(1)$ or $O(\log n)$) because it directly hits the partition; Scan is slow ($O(n)$) and heavily consumes read capacity units (RCUs).
- **Pricing:** Query is cheap as it only bills for matching records; Scan bills for the entire table size regardless of how many records are returned after filtering.
- **Rule of Thumb:** Always use Query for standard operations; reserve Scan for sparse background administrative tasks (like data exports).

**Example:**
```javascript
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, QueryCommand, ScanCommand } = require("@aws-sdk/lib-dynamodb");

const client = new DynamoDBClient({ region: "us-east-1" });
const ddbDocClient = DynamoDBDocumentClient.from(client);

// 1. Efficient Query
const queryRes = await ddbDocClient.send(new QueryCommand({
  TableName: "Users",
  KeyConditionExpression: "userId = :uid",
  ExpressionAttributeValues: { ":uid": "user_123" }
}));

// 2. Inefficient Scan
const scanRes = await ddbDocClient.send(new ScanCommand({
  TableName: "Users",
  FilterExpression: "age > :minAge",
  ExpressionAttributeValues: { ":minAge": 18 }
}));
```

**Reference:** [AWS Query vs Scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryandScan.html)

---

---

### 2. What is a Partition Key (PK) in DynamoDB?

**Answer:**
**The Core Concept:**
The **Partition Key** (also known as Hashing Key) is the primary attribute used by DynamoDB to determine the physical partition where the item is stored. It is passed into an internal hash function to distribute data evenly across physical storage nodes.

**Key Details:**
- **Uniqueness:** If a table uses *only* a Partition Key as its primary key, the Partition Key must be globally unique across all items.
- **Lookups:** Enables ultra-fast $O(1)$ lookups because the hash directly routes the request to the exact physical machine holding the data.
- **Design Rule:** Choose a high-cardinality attribute (like `userId` or `transactionId`) to avoid hot partitions (overloading a single storage node).

**Example:**
```javascript
// Schema Definition (Conceptual)
// Table: Users
// Primary Key: userId (Partition Key)
const putCommand = {
  TableName: "Users",
  Item: {
    userId: "user_999", // Uniquely identifies this record
    email: "test@gmail.com"
  }
};
```

**Reference:** [AWS Partition Keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html)

---

---

### 3. What is a Sort Key (SK) in DynamoDB?

**Answer:**
**The Core Concept:**
The **Sort Key** (also known as Range Key) is an optional second key that, when combined with the Partition Key, forms a composite primary key. It determines the physical order of items stored on the same partition.

**Key Details:**
- **Uniqueness:** With a composite key, multiple items can share the same Partition Key, but their Sort Keys must be unique (e.g., `userId` (PK) + `orderDate` (SK)).
- **Queries:** Allows query range expressions using operators like `begins_with`, `between`, `>`, and `<` on the Sort Key.
- **Relational Mapping:** Critical for implementing one-to-many relationships (e.g., a customer partition holding multiple order records).

**Example:**
```javascript
// Querying a user's orders made in a specific date range
const queryOrders = {
  TableName: "Orders",
  KeyConditionExpression: "userId = :uid AND orderDate BETWEEN :start AND :end",
  ExpressionAttributeValues: {
    ":uid": "user_123",
    ":start": "2026-01-01",
    ":end": "2026-05-28"
  }
};
```

**Reference:** [AWS Primary Keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.PrimaryKey)

---

---

### 11. What is Redis?

**Answer:**
**The Core Concept:**
**Redis** (Remote Dictionary Server) is an open-source, in-memory key-value data structure store used primarily as a database, cache, message broker, and queue.

**Key Details:**
- **Speed:** All data resides in RAM, enabling extremely fast sub-millisecond read and write operations.
- **Data Structures:** Unlike simple string key-value caches (like Memcached), Redis natively supports structured types such as Lists, Sets, Sorted Sets, Hashes, HyperLogLogs, and Geospatial indexes.
- **Single-Threaded Core:** Its core execution loop is single-threaded, avoiding race conditions and thread synchronization overhead, while utilizing I/O multiplexing for high concurrency.

**Example:**
```javascript
const { createClient } = require("redis");
const client = createClient();
await client.connect();

// Storing a simple string
await client.set("session:user_123", "logged_in");

// Storing structured data (Hash)
await client.hSet("user:123", {
  name: "Knl",
  role: "admin"
});
```

**Reference:** [Redis Intro](https://redis.io/docs/latest/develop/get-started/)

---

---

### 12. Redis vs. Traditional Database (SQL/NoSQL)

**Answer:**
**The Core Concept:**
The key difference is storage medium and durability. Traditional databases (like MySQL or MongoDB) write data directly to persistent disk storage (SSD/HDD) by default, while Redis keeps all active dataset records in volatile computer memory (RAM).

**Key Details:**
- **Performance:** Redis easily delivers 100,000+ operations/sec per node due to RAM access; disk-bound databases are bottlenecks in comparison.
- **Cost:** Volatile RAM storage is significantly more expensive than SSD disk capacity, meaning Redis is typically reserved for active hot data rather than large historical records.
- **Query Flexibility:** SQL databases offer dynamic joins and complex queries; Redis is key-value based, meaning records are retrieved only via explicit keys.

**Reference:** [Redis vs SQL](https://aws.amazon.com/nosql/key-value/)

---

---

### 13. What is Caching? / Caching Strategies?

**Answer:**
**The Core Concept:**
**Caching** is the practice of storing active, frequently requested data in a fast temporary storage layer (like Redis) so that subsequent reads are served instantly without querying the slower database layer.

**Key Details:**
- **Cache-Aside (Lazy Loading):** The application checks the cache first. If it's a *cache miss*, it queries the database, writes the result to the cache, and returns it. (Most common pattern).
- **Write-Through:** The application writes directly to both the cache and the database in a single transaction, ensuring data is never stale.
- **Cache Hit vs Miss:** A high cache hit ratio is the goal, indicating that most read operations are successfully offloaded from the disk database.

**Example (Cache-Aside pattern):**
```javascript
async function getUserData(userId) {
  const cacheKey = `user:${userId}`;
  
  // 1. Try Cache
  const cachedData = await redisClient.get(cacheKey);
  if (cachedData) {
    return JSON.parse(cachedData); // Cache Hit
  }

  // 2. Cache Miss -> Query DB
  const dbData = await db.queryUser(userId);
  
  // 3. Write to Cache for next time (expires in 1 hour)
  await redisClient.set(cacheKey, JSON.stringify(dbData), { EX: 3600 });
  
  return dbData;
}
```

**Reference:** [AWS Caching Strategies](https://aws.amazon.com/caching/)

---

---

## Intermediate Questions

### 4. What is a KeyConditionExpression in DynamoDB?

**Answer:**
**The Core Concept:**
A **KeyConditionExpression** is a query parameter string that specifies the key values for the items to be read. It specifies the partition key match and optional sort key range limits.

**Key Details:**
- **Validation:** You *must* specify the partition key name and exact value in this expression using equality (`=`).
- **Sort Key Operators:** You can optionally include the sort key and operators like `>` or `begins_with()` to narrow the subset of items.
- **Efficiency:** The KeyConditionExpression is processed *before* capacity consumption is calculated, making it highly efficient.

**Example:**
```javascript
const params = {
  TableName: "ForumPosts",
  // userId is PK, category#date is SK
  KeyConditionExpression: "userId = :uid AND begins_with(categoryDate, :category)",
  ExpressionAttributeValues: {
    ":uid": "user_456",
    ":category": "TECH"
  }
};
```

**Reference:** [KeyConditionExpression Syntax](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#Query.KeyConditionExpression)

---

---

### 5. Difference between FilterExpression and Scan?

**Answer:**
**The Core Concept:**
A **FilterExpression** is applied to a Query or Scan *after* the initial data is read from the physical partition but *before* results are returned to the client. A **Scan** is the operation that reads the entire table.

**Key Details:**
- **Capacity Billing:** A FilterExpression does **not** save money or capacity units (RCUs); billing is based on the data size read *prior* to filtering.
- **Client Bandwidth:** It only saves network bandwidth by sending a smaller filtered array to the client instead of the full payload.
- **Limitation:** If a Scan with a filter hits the 1MB evaluation limit, you must paginate even if zero filtered items are returned.

**Example:**
```javascript
// Consumes capacity for ALL user_123 items, but only returns active ones to the client
const queryWithFilter = {
  TableName: "Users",
  KeyConditionExpression: "userId = :uid",
  FilterExpression: "accountStatus = :status",
  ExpressionAttributeValues: {
    ":uid": "user_123",
    ":status": "ACTIVE"
  }
};
```

**Reference:** [AWS Query Filter Expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#Query.FilterExpression)

---

---

### 6. What is BatchWriteItem and BatchGetItem in DynamoDB?

**Answer:**
**The Core Concept:**
**BatchGetItem** reads up to 100 items across multiple tables in a single API call. **BatchWriteItem** puts or deletes up to 25 items in a single call.

**Key Details:**
- **Network Efficiency:** Dramatically reduces network round-trip overhead compared to making individual `GetItem` or `PutItem` calls.
- **Transaction Difference:** Unlike transactions, batches do **not** succeed or fail as a single unit. If some items fail, they are returned in an `UnprocessedKeys` array for you to retry.
- **Limits:** BatchGetItem is capped at 16MB of data; BatchWriteItem is capped at 16MB and cannot perform conditional updates.

**Example:**
```javascript
const { BatchGetCommand } = require("@aws-sdk/lib-dynamodb");

const batchRes = await ddbDocClient.send(new BatchGetCommand({
  RequestItems: {
    "Users": {
      Keys: [
        { userId: "user_1" },
        { userId: "user_2" }
      ]
    }
  }
}));
```

**Reference:** [AWS Batch Operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/batchops.html)

---

---

### 14. What is Redis Persistence? (RDB vs AOF)

**Answer:**
**The Core Concept:**
Since RAM is volatile, Redis provides two optional persistence mechanisms to recover dataset state in the event of an unexpected server crash: **RDB (Redis Database)** and **AOF (Append Only File)**.

**Key Details:**
- **RDB (Snapshotting):** Creates a compact, point-in-time binary snapshot of the entire dataset at specified intervals (e.g., every 5 minutes). Fast restarts, but risk losing data since the last snapshot.
- **AOF (Append-Only Log):** Logs every incoming write operation command to disk in real time. Maximizes data durability, but files grow large and slow down startup recovery.
- **Production Best Practice:** Run both simultaneously; use AOF for high durability and RDB for quick backups and recovery.

**Reference:** [Redis Persistence Guide](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)

---

---

### 15. What is Redis Pub/Sub?

**Answer:**
**The Core Concept:**
**Redis Pub/Sub** is a lightweight real-time messaging paradigm where publishers push messages onto named channels without knowing who the subscribers are, and subscribers listen to specific channels.

**Key Details:**
- **At-Most-Once Delivery:** Messages are fire-and-forget. If a subscriber is disconnected or offline when a message is published, the message is lost forever.
- **Real-Time Scaling:** Used for chat rooms, instant notifications, or triggering microservice tasks.
- **Alternative (Redis Streams):** For persistent queues (guaranteeing at-least-once delivery with history), modern Redis provides **Streams** instead of Pub/Sub.

**Example:**
```javascript
// Subscriber Client
const subClient = redisClient.duplicate();
await subClient.connect();
await subClient.subscribe("chat_channel", (message) => {
  console.log("New Message:", message);
});

// Publisher Client
const pubClient = redisClient.duplicate();
await pubClient.connect();
await pubClient.publish("chat_channel", "Hello World!");
```

**Reference:** [Redis Pub/Sub](https://redis.io/docs/latest/develop/interact/pubsub/)

---

---

### 16. What is TTL (Time-To-Live) in Redis?

**Answer:**
**The Core Concept:**
**TTL** is a mechanism that associates an expiration timeout with a specific key. Once the timeout expires, Redis automatically deletes the key from memory.

**Key Details:**
- **Memory Management:** Crucial for preventing memory saturation by ensuring transient data (like user sessions or temporary tokens) is self-cleaning.
- **Units:** Can be defined in seconds (`EXPIRE`) or milliseconds (`PEXPIRE`).
- **Passive vs Active Deletion:** Redis evicts keys both passively (when a client attempts to read an expired key) and actively (a background task randomly samples and sweeps expired keys).

**Example:**
```javascript
// Set key with a TTL of 30 seconds
await redisClient.set("tempToken", "xyz123", { EX: 30 });

// Check remaining TTL (returns seconds remaining, -2 if expired/missing)
const ttl = await redisClient.ttl("tempToken"); 
console.log(ttl); // e.g., 29
```

**Reference:** [Redis Expire Command](https://redis.io/docs/latest/commands/expire/)

---

---

### 17. What is Cache Invalidation?

**Answer:**
**The Core Concept:**
**Cache Invalidation** is the process of declaring cached data obsolete or deleting it immediately when underlying database records are modified, preventing the application from reading stale data.

**Key Details:**
- **The Hardest Problem:** As the famous computer science quote states: *"There are only two hard things in Computer Science: cache invalidation and naming things."*
- **Active Eviction:** When updating a record in the database, the application must immediately delete the corresponding key in Redis: `await redisClient.del(cacheKey)`.
- **TTL Fallback:** Always set a conservative TTL (e.g. 1 day) on all cache keys as a fail-safe backstop in case active invalidation logic fails.

**Reference:** [Caching Best Practices](https://aws.amazon.com/caching/best-practices/)

---

---

## Expert Questions

### 7. What is the difference between a Global Secondary Index (GSI) and a Local Secondary Index (LSI)?

**Answer:**
**The Core Concept:**
Secondary indexes allow querying data using attributes other than the main primary keys. An **LSI** shares the same Partition Key as the main table but has a different Sort Key. A **GSI** can have an entirely different Partition Key and Sort Key.

**Key Details:**
- **Creation Time:** LSIs must be created during table creation and cannot be deleted later. GSIs can be created or deleted at any time.
- **Throughput:** LSIs share the capacity units (RCUs/WCUs) of the main table. GSIs have their own provisioned throughput capacity.
- **Consistency:** LSIs support both strong and eventual consistency. GSIs only support eventual consistency.

**Comparison Table:**
| Feature | Local Secondary Index (LSI) | Global Secondary Index (GSI) |
|---------|-----------------------------|------------------------------|
| **Partition Key** | Must be same as main table | Can be entirely different |
| **Capacity Units**| Shared with main table | Separate and dedicated |
| **Consistency** | Strongly or Eventually Consistent | Eventually Consistent only |

**Reference:** [AWS Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)

---

---

### 8. What is a DynamoDB Stream?

**Answer:**
**The Core Concept:**
A **DynamoDB Stream** is a time-ordered log that captures item-level mutations (inserts, updates, deletes) in a DynamoDB table in real time, persisting them for up to 24 hours.

**Key Details:**
- **Trigger Lambda:** Commonly integrated with AWS Lambda to trigger serverless workflows (event-driven architecture) on record mutations.
- **View Types:** Can capture just the modified keys, the new image (after update), the old image (before update), or both.
- **Use Cases:** Ideal for replication, sending real-time emails upon user creation, or auditing user changes.

**Example:**
```json
// Conceptual Stream Record representing an INSERT
{
  "eventName": "INSERT",
  "dynamodb": {
    "Keys": { "userId": { "S": "user_123" } },
    "NewImage": {
      "userId": { "S": "user_123" },
      "email": { "S": "alex@gmail.com" }
    }
  }
}
```

**Reference:** [AWS DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html)

---

---

### 9. What is Eventual Consistency vs Strong Consistency in DynamoDB?

**Answer:**
**The Core Concept:**
By default, DynamoDB reads are **Eventually Consistent**, meaning a read request immediately following a write might return stale data because updates take time to replicate across all database nodes. **Strongly Consistent** reads guarantee that the most up-to-date write is returned.

**Key Details:**
- **Replication Lag:** DynamoDB replicates data across 3 Availability Zones. Eventually Consistent reads query any random node; Strongly Consistent reads query at least two nodes to return the absolute latest consensus.
- **Cost:** Strongly Consistent reads consume **double** the capacity units (RCUs) of Eventually Consistent reads.
- **Index Limit:** Secondary indexes (GSIs) do not support Strongly Consistent reads.

**Example:**
```javascript
// Strongly Consistent Read
const stronglyRes = await ddbDocClient.send(new GetCommand({
  TableName: "Users",
  Key: { userId: "user_123" },
  ConsistentRead: true // Consumes double RCUs!
}));
```

**Reference:** [AWS Read Consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)

---

---

### 10. How does DynamoDB scaling work?

**Answer:**
**The Core Concept:**
DynamoDB scales seamlessly by dividing table data across multiple physical partitions. As data size (exceeding 10GB per partition) or throughput demands (exceeding 1000 WCUs or 3000 RCUs) increase, DynamoDB automatically splits partitions.

**Key Details:**
- **Billing Modes:** Offers two capacity modes: **Provisioned** (you specify RCUs and WCUs, with auto-scaling boundaries) and **On-Demand** (scales instantly to match traffic, billed per request).
- **Hot Partition Issue:** If queries are concentrated on a single Partition Key value, that specific partition will throttle even if the table has overall high provisioned capacity.
- **Mitigation:** Use synthetic partition keys (e.g. adding a random suffix `_1` to `_9` to the PK) to spread hot keys across physical hardware.

**Reference:** [AWS Scaling and Partitioning](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html)

---

---

### 18. What is Distributed Caching?

**Answer:**
**The Core Concept:**
A **Distributed Cache** is a caching deployment where the cached data is spread across a cluster of multiple physical server nodes, functioning conceptually as a single, massive cache space.

**Key Details:**
- **Scaling Limit:** A single Redis server is capped by its host's RAM size. Distributed caching overcomes this limit by pooling RAM across instances.
- **Consistent Hashing:** Redis Cluster uses **Hash Slots** (16,384 slots) to allocate keys across nodes. Keys are hashed, determining which cluster node holds that data.
- **High Availability:** Supports master-replica replication to ensure the cache stays online if a single node fails.

**Reference:** [Redis Cluster Specs](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)

---

---

### 19. Redis vs. Memcached

**Answer:**
**The Core Concept:**
While both are highly performant in-memory caches, **Memcached** is a simple, multi-threaded key-value sub-cache optimized purely for flat strings, whereas **Redis** is a rich, feature-packed data structure store with persistence and clustering natively supported.

**Key Details:**
- **Data Types:** Memcached only supports flat strings. Redis supports rich types (Hashes, Lists, Sets).
- **Architecture:** Memcached is multi-threaded (scales vertically easily); Redis is single-threaded (scales horizontally via clustering).
- **Persistence:** Memcached loses all data on reboot; Redis optionally saves datasets to disk.

**Comparison Table:**
| Feature | Memcached | Redis |
|---------|-----------|-------|
| **Data structures** | Flat Strings only | Rich types (Sets, Hashes, Lists) |
| **Threading** | Multi-threaded | Single-threaded core |
| **Persistence** | None (purely volatile) | Optional (RDB & AOF) |

**Reference:** [AWS Redis vs Memcached](https://aws.amazon.com/elasticache/redis-vs-memcached/)

---

---

### 20. Enterprise Use Cases of Redis

**Answer:**
**The Core Concept:**
Beyond basic database caching, Redis's speed and rich structured datatypes enable several standard enterprise application patterns.

**Key Details:**
- **Session Store:** Storing user session tokens with TTLs, ensuring fast authentication lookups on every request.
- **API Rate Limiter:** Using the `INCR` command and sliding window algorithms to block brute-force traffic.
- **Sorted Leaderboards:** Utilizing the Sorted Set (`ZSET`) data structure to instantly rank millions of users in real time.
- **Distributed Lock (Redlock):** Ensuring that a highly concurrent distributed system processes a specific action (like inventory reservation) only once.

**Example (Rate Limiting pattern):**
```javascript
async function isRateLimited(ipAddress) {
  const limitKey = `rate:${ipAddress}`;
  const requests = await redisClient.incr(limitKey);
  
  if (requests === 1) {
    await redisClient.expire(limitKey, 60); // Reset count every 60 seconds
  }
  
  return requests > 100; // Limit to 100 requests per minute
}
```

**Reference:** [Redis Enterprise Use Cases](https://redis.io/solutions/)

---

## Technical Questions

### 1. Write a Node.js function using `@aws-sdk/client-dynamodb` to query orders within a date range.

**Example Solution:**
### 2. Implement an API sliding-window rate limiter in Node.js using Redis `INCR` and `EXPIRE`.

**Example Solution:**
```javascript
async function isRateLimited(redisClient, ipAddress) {
  const key = `rate:${ipAddress}`;
  const count = await redisClient.incr(key);
  if (count === 1) {
    await redisClient.expire(key, 60);
  }
  return count > 100; // limit to 100 requests per minute
}
```

