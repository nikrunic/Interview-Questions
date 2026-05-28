# MongoDB Interview Questions

This document contains a comprehensive list of 100 MongoDB interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories and enterprise real-world scenarios.

---

## Basic Questions

### 1. What is MongoDB?
**Answer:** A document-oriented, open-source NoSQL database program designed for high volume data storage, scaling, and schema flexibility.
**Example:** `mongosh` CLI allows interacting with MongoDB databases.
**Reference:** [What is MongoDB](https://www.mongodb.com/what-is-mongodb)

---

---

### 2. What are the key features of MongoDB?
**Answer:** 
**The Core Concept:**
Dynamic schema, indexing, replication, aggregation framework, and horizontal sharding.
**Key Details:**
- **Flexible Schema**: Documents in the same collection can have different fields.
- **Horizontal Scale**: Scale out across multiple commodity servers.
**Example:** Creating indexes on any fields to accelerate search.
**Reference:** [MongoDB Features](https://www.mongodb.com/docs/manual/introduction/)

---

---

### 3. What is NoSQL and what are the main types?
**Answer:** NoSQL (Not Only SQL) databases are non-relational database systems that store data in formats other than tabular relations.
**Key Details:**
- **Key-Value Stores**: Redis, DynamoDB.
- **Document Stores**: MongoDB, CouchDB.
- **Column Family**: Cassandra, Hbase.
- **Graph Databases**: Neo4j.
**Reference:** [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)

---

---

### 4. Explain JSON vs. BSON in MongoDB.
**Answer:** JSON is a text-based format representing key-value pairs; BSON is a binary-encoded serialization of JSON documents containing extra data types.
**Key Details:**
- BSON allows fast traversal and holds native types like `Date` and `BinData`.
- BSON files are stored directly on disk by WiredTiger.
**Example:** `{"date": "2026-05-26"}` (JSON) vs. `Date` object (BSON).
**Reference:** [BSON Specification](https://bsonspec.org/)

---

---

### 5. What is an ObjectId in MongoDB, and what does it consist of?
**Answer:** A unique 12-byte identifier automatically generated for the `_id` field of every new document.
**Key Details:**
- **4-byte timestamp**: Epoch seconds of document creation.
- **5-byte random value**: Generated per process/machine.
- **3-byte counter**: Auto-incrementing value.
**Example:** `ObjectId("60d5ec40f8e91b2c4c8b4567")`
**Reference:** [MongoDB ObjectIds](https://www.mongodb.com/docs/manual/reference/method/ObjectId/)

---

---

### 6. How do you create a database and a collection in MongoDB?
**Answer:** By utilizing the `use` command to switch database contexts, and calling `createCollection()` or inserting a document.
**Example:**
```javascript
use myNewDB;
db.createCollection("customers");
```
**Reference:** [Create Database Manual](https://www.mongodb.com/docs/manual/reference/command/create/)

---

---

### 7. What is the difference between `insertOne()` and `insertMany()`?
**Answer:** `insertOne()` adds a single document, while `insertMany()` inserts an array of documents within a single network operation.
**Example:**
```javascript
db.users.insertOne({ name: "Alice" });
db.users.insertMany([{ name: "Bob" }, { name: "Charlie" }]);
```
**Reference:** [Insert Operations Guide](https://www.mongodb.com/docs/manual/reference/method/db.collection.insertMany/)

---

---

### 8. How do you find/query documents in a collection?
**Answer:** Use the `db.collection.find(query, projection)` method with match filters.
**Example:**
```javascript
db.users.find({ age: { $gte: 18 } });
```
**Reference:** [Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/)

---

---

### 9. Explain the use of projection in MongoDB queries.
**Answer:** Projections limit the fields returned in the result set to reduce network bandwidth.
**Example:** Return only `name` and exclude `_id`:
```javascript
db.users.find({ status: "active" }, { name: 1, _id: 0 });
```
**Reference:** [Project Fields from Queries](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/)

---

---

### 10. What are basic comparison operators like `$eq`, `$ne`, `$gt`, `$lt`?
**Answer:** Standard operators to match values against fields: equal, not equal, greater than, less than.
**Example:**
```javascript
db.products.find({ price: { $gt: 100, $lt: 500 } });
```
**Reference:** [Comparison Operators](https://www.mongodb.com/docs/manual/reference/operator/query-comparison/)

---

---

### 11. What are logical query operators like `$or`, `$and`, `$not`, `$nor`?
**Answer:** Logical operators to join query clauses with boolean operations.
**Example:**
```javascript
db.users.find({ $or: [{ role: "admin" }, { status: "vip" }] });
```
**Reference:** [Logical Query Operators](https://www.mongodb.com/docs/manual/reference/operator/query-logical/)

---

---

### 12. How do you update a document in MongoDB? Explain `$set`.
**Answer:** Use `updateOne()` or `updateMany()` with the `$set` operator to modify specific field values without overwriting the whole document.
**Example:**
```javascript
db.users.updateOne({ name: "Alice" }, { $set: { age: 29 } });
```
**Reference:** [Update Documents](https://www.mongodb.com/docs/manual/reference/operator/update/set/)

---

---

### 13. What is the purpose of `$unset` in an update query?
**Answer:** A field update operator that deletes a specific field entirely from a document.
**Example:** Delete the `nickname` field:
```javascript
db.users.updateOne({ name: "Bob" }, { $unset: { nickname: "" } });
```
**Reference:** [$unset Operator](https://www.mongodb.com/docs/manual/reference/operator/update/unset/)

---

---

### 14. What are array update operators like `$push`, `$pull`, `$pop`?
**Answer:** Specialized operators to manipulate elements inside array fields.
**Key Details:**
- `$push`: Appends an item.
- `$pull`: Removes all items matching a filter.
- `$pop`: Removes the first (-1) or last (1) item.
**Example:**
```javascript
db.users.updateOne({ name: "Alice" }, { $push: { tags: "developer" } });
```
**Reference:** [Array Update Operators](https://www.mongodb.com/docs/manual/reference/operator/update-array/)

---

---

### 15. How do you delete documents in MongoDB?
**Answer:** By using the `deleteOne()` or `deleteMany()` methods with a query filter.
**Example:**
```javascript
db.users.deleteMany({ status: "inactive" });
```
**Reference:** [Delete Documents](https://www.mongodb.com/docs/manual/tutorial/remove-documents/)

---

---

### 16. What is the difference between `deleteOne()` and `deleteMany()`?
**Answer:** `deleteOne()` deletes the first document matching the query; `deleteMany()` deletes all matching documents in the collection.
**Example:**
```javascript
db.logs.deleteOne({ level: "error" }); // Removes only one log
```
**Reference:** [db.collection.deleteOne](https://www.mongodb.com/docs/manual/reference/method/db.collection.deleteOne/)

---

---

### 17. What is an "upsert" operation in MongoDB?
**Answer:** An update parameter which inserts a new document if no document matches the query, or updates the match if it exists.
**Example:**
```javascript
db.users.updateOne(
  { email: "new@example.com" }, 
  { $set: { active: true } }, 
  { upsert: true }
);
```
**Reference:** [Upsert Option](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/)

---

---

### 18. How do you sort query results in MongoDB?
**Answer:** Use the `.sort()` modifier on the query cursor, passing `1` for ascending and `-1` for descending order.
**Example:**
```javascript
db.products.find().sort({ price: 1, name: -1 });
```
**Reference:** [Sort Cursor Results](https://www.mongodb.com/docs/manual/reference/method/cursor.sort/)

---

---

### 19. How do you limit and skip query results (e.g., for pagination)?
**Answer:** Combine `.limit(n)` to cap result counts and `.skip(m)` to bypass previous pages.
**Example:** Skip first 10, return next 5 items:
```javascript
db.products.find().skip(10).limit(5);
```
**Reference:** [Limit and Skip Cursor Methods](https://www.mongodb.com/docs/manual/reference/method/cursor.skip/)

---

---

### 20. What is a schema-less database, and what are its trade-offs?
**Answer:** A database that does not require pre-defined tables or schemas, allowing documents in the same collection to have unique attributes.
**Key Details:**
- **Trade-off**: Extremely fast prototyping and integration, but increases structural checking overhead in the application logic.
**Reference:** [Schema-less Design](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/)

---

## Intermediate Questions

---

## Intermediate Questions

### 21. What is an index in MongoDB, and why is it used?
**Answer:** A data structure that stores a small portion of the collection's data in a traversable B-Tree to bypass full collection scans.
**Example:**
```javascript
db.users.createIndex({ email: 1 });
```
**Reference:** [Indexes Manual](https://www.mongodb.com/docs/manual/indexes/)

---

---

### 22. How do you create and list indexes on a collection?
**Answer:** Use `createIndex()` to define the index and `getIndexes()` to list all active indexes.
**Example:**
```javascript
db.users.createIndex({ username: 1 }, { unique: true });
db.users.getIndexes();
```
**Reference:** [Index Management](https://www.mongodb.com/docs/manual/reference/method/db.collection.getIndexes/)

---

---

### 23. What is a compound index?
**Answer:** An index constructed on multiple fields within a single collection, optimizing queries that filter or sort by these multiple fields.
**Example:**
```javascript
db.orders.createIndex({ customer_id: 1, created_at: -1 });
```
**Reference:** [Compound Indexes](https://www.mongodb.com/docs/manual/core/index-compound/)

---

---

### 24. What is the left-prefix rule in compound indexes?
**Answer:** MongoDB can only use a compound index if the query contains the leftmost fields in the exact order they are listed in the index.
**Example:** Index on `{ A: 1, B: 1, C: 1 }` matches queries for `{ A }` or `{ A, B }` but NOT `{ B }` or `{ B, C }`.
**Reference:** [Prefixes of Compound Indexes](https://www.mongodb.com/docs/manual/core/index-compound/#prefixes)

---

---

### 25. Explain the ESR (Equality, Sort, Range) rule for designing compound indexes.
**Answer:** The optimal ordering of fields in a compound index to support both filtering and sorting efficiently.
**Key Details:**
- **E**quality: Fields with exact values must be positioned first.
- **S**ort: Fields defining the sort order must follow.
- **R**ange: Fields filtering ranges (`$gt`, `$in`) must be placed last.
**Reference:** [ESR Rule Guide](https://www.mongodb.com/docs/manual/core/multikey-index-bounds/#equality-sort-range)

---

---

### 26. What is a multikey index, and when is it automatically created?
**Answer:** An index created on a field that contains an array, mapping individual index entries to every element inside that array.
**Example:** Indexing `skills` array on users automatically generates a multikey index.
```javascript
db.users.createIndex({ skills: 1 });
```
**Reference:** [Multikey Indexes](https://www.mongodb.com/docs/manual/core/index-multikey/)

---

---

### 27. What is a covered query, and how does it improve performance?
**Answer:** A query that is completely satisfied by scanning the index, without reading any actual documents from disk.
**Key Details:**
- All query criteria and projected fields must be included in the index.
- The `_id` field must be explicitly excluded if it is not indexed.
**Example:**
```javascript
db.users.find({ username: "alice" }, { username: 1, _id: 0 }); // if username is indexed
```
**Reference:** [Covered Queries](https://www.mongodb.com/docs/manual/core/query-optimization/#covered-queries)

---

---

### 28. What is the difference between embedding documents and referencing documents?
**Answer:** Embedding nests related data directly within the parent document (denormalized); referencing uses references (`ObjectId` pointers) to point to other collections (normalized).
**Key Details:**
- **Embedding**: Fast reads, but limited by 16MB document size.
- **Referencing**: Prevents document growth and redundancy, but requires additional queries/joins.
**Reference:** [Embedded vs Reference Data Modeling](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/#embedded-data-vs-references)

---

---

### 29. How do you implement 1-to-Many relationships in MongoDB?
**Answer:** 
- **Embedded**: Nest child documents if the count is small and bounded (e.g. up to 10 addresses).
- **Referenced**: Store child document references in an array, or store parent ID reference in the child document if count is unbounded (e.g. thousands of comments).
**Reference:** [Model One-to-Many Relationships](https://www.mongodb.com/docs/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/)

---

---

### 30. How do you implement Many-to-Many relationships in MongoDB?
**Answer:** By storing arrays of references inside both collections (bidirectional referencing).
**Example:**
```json
// User Document
{ "_id": 1, "name": "Alice", "group_ids": [10, 20] }
// Group Document
{ "_id": 10, "name": "Admin", "user_ids": [1, 2] }
```
**Reference:** [Model Relationships](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/)

---

---

### 31. What is the Aggregation Framework?
**Answer:** A framework that processes large volumes of documents through a multi-stage data transformation pipeline on the server.
**Example:**
```javascript
db.sales.aggregate([ { $match: { year: 2026 } } ]);
```
**Reference:** [Aggregation Pipelines](https://www.mongodb.com/docs/manual/aggregation/)

---

---

### 32. What does `$match` do in an aggregation pipeline?
**Answer:** Filters document streams, allowing only documents matching the criteria to pass to the next stage.
**Example:** Matches active sales:
```javascript
{ $match: { status: "active" } }
```
**Reference:** [$match Stage Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/)

---

---

### 33. What does `$group` do in an aggregation pipeline?
**Answer:** Groups incoming documents by a specified key expression and performs calculations like counts, sums, or averages.
**Example:** Group by category and sum prices:
```javascript
{ $group: { _id: "$category", total: { $sum: "$price" } } }
```
**Reference:** [$group Stage Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/)

---

---

### 34. What does `$project` do in an aggregation pipeline?
**Answer:** Reshapes documents by adding, renaming, calculating, or omitting fields in the output stream.
**Example:** Add a custom field name:
```javascript
{ $project: { userEmail: "$email", age: 1 } }
```
**Reference:** [$project Stage Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/)

---

---

### 35. What is the purpose of the `$unwind` stage?
**Answer:** Deconstructs an array field from the input documents to output a document for each element of the array.
**Example:**
```javascript
{ $unwind: "$skills" } // A document with 3 skills becomes 3 documents
```
**Reference:** [$unwind Stage Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unwind/)

---

---

### 36. How does `$lookup` perform a join operation in MongoDB?
**Answer:** It performs an outer join from another collection within the same database to import documents.
**Example:**
```javascript
{
  $lookup: {
    from: "orders",
    localField: "_id",
    foreignField: "customer_id",
    as: "customer_orders"
  }
}
```
**Reference:** [$lookup Stage Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/)

---

---

### 37. What is the `$addFields` stage in an aggregation pipeline?
**Answer:** Appends new fields or overrides existing fields in the output document without redefining the entire document.
**Example:**
```javascript
{ $addFields: { calculatedTax: { $multiply: ["$price", 0.15] } } }
```
**Reference:** [$addFields Stage Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/addFields/)

---

---

### 38. Explain how the aggregation pipeline optimizations work internally (e.g., stage coalescing).
**Answer:** MongoDB analyzes pipeline stages and attempts to reorder, coalesce, or merge them to reduce CPU and disk reads.
**Key Details:**
- `$match` is moved to the front whenever possible to leverage indexes.
- Adjacent `$sort` and `$limit` stages are coalesced to perform top-K sorts in memory.
**Reference:** [Pipeline Optimization](https://www.mongodb.com/docs/manual/core/aggregation-pipeline-optimization/)

---

---

### 39. Does MongoDB support ACID transactions? If so, how?
**Answer:** Yes. MongoDB supports multi-document transactions using Sessions.
**Key Details:**
- Supported across Replica Sets (v4.0+) and Sharded Clusters (v4.2+).
- Operates under snapshot isolation levels.
**Example:**
```javascript
const session = db.getMongo().startSession();
session.startTransaction();
// ... db operations ...
session.commitTransaction();
```
**Reference:** [Transactions Manual](https://www.mongodb.com/docs/manual/core/transactions/)

---

---

### 40. How do you create a validation schema for a collection using JSON Schema?
**Answer:** Define a `$jsonSchema` document structure inside the `validator` parameter when creating or altering collections.
**Example:**
```javascript
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string", pattern: "@" }
      }
    }
  }
});
```
**Reference:** [JSON Schema Validation](https://www.mongodb.com/docs/manual/core/schema-validation/json-schema/)

---

---

### 41. What is a TTL (Time-To-Live) index, and when should you use it?
**Answer:** A single-field index that automatically deletes documents from a collection after a specified amount of time.
**Example:** Deletes documents 1 hour (3600 seconds) after creation:
```javascript
db.sessions.createIndex({ created_at: 1 }, { expireAfterSeconds: 3600 });
```
**Reference:** [Expire Data via TTL Indexes](https://www.mongodb.com/docs/manual/core/index-ttl/)

---

---

### 42. What is a text index, and how do you perform text searches in MongoDB?
**Answer:** An index that supports string searches within string content using tokenization, stemming, and stop-words.
**Example:**
```javascript
db.posts.createIndex({ content: "text" });
db.posts.find({ $text: { $search: "mongodb database" } });
```
**Reference:** [Text Indexes](https://www.mongodb.com/docs/manual/core/index-text/)

---

---

### 43. What is a partial index, and how does it save disk space?
**Answer:** An index that only indexes documents matching a specified filter expression, saving disk space and memory.
**Example:** Index only active customers' emails:
```javascript
db.users.createIndex(
  { email: 1 },
  { partialFilterExpression: { status: "active" } }
);
```
**Reference:** [Partial Indexes](https://www.mongodb.com/docs/manual/core/index-partial/)

---

---

### 44. What is a sparse index?
**Answer:** An index that only includes entries for documents where the indexed field actually exists.
**Example:**
```javascript
db.users.createIndex({ tax_id: 1 }, { sparse: true });
```
**Reference:** [Sparse Indexes](https://www.mongodb.com/docs/manual/core/index-sparse/)

---

---

### 45. How do you perform a geospatial query in MongoDB?
**Answer:** By storing locations as GeoJSON structures, creating a `2dsphere` index, and using operators like `$near` or `$geoWithin`.
**Example:**
```javascript
db.stores.createIndex({ location: "2dsphere" });
db.stores.find({
  location: {
    $near: {
      $geometry: { type: "Point", coordinates: [-73.96, 40.78] },
      $maxDistance: 1000 // 1 km
    }
  }
});
```
**Reference:** [Geospatial Queries](https://www.mongodb.com/docs/manual/geospatial-queries/)

---

---

### 46. What is the purpose of `$facet` in aggregation?
**Answer:** Allows executing multiple parallel aggregation pipelines on the same set of input documents within a single stage.
**Example:**
```javascript
{
  $facet: {
    categorized: [{ $group: { _id: "$category", count: { $sum: 1 } } }],
    priced: [{ $bucket: { groupBy: "$price", boundaries: [0, 50, 100] } }]
  }
}
```
**Reference:** [$facet Aggregation Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/facet/)

---

---

### 47. What is the `$merge` stage in aggregation?
**Answer:** Writes the aggregation pipeline output directly into a specified collection, allowing updates, inserts, or replacements.
**Example:**
```javascript
{ $merge: { into: "monthly_reports", on: "_id", whenMatched: "replace" } }
```
**Reference:** [$merge Aggregation Reference](https://www.mongodb.com/docs/manual/reference/operator/aggregation/merge/)

---

---

### 48. What are Capped Collections, and what are their use cases?
**Answer:** Fixed-size collections that maintain insertion order. Once size limit is reached, it overwrites the oldest entries (circular buffers).
**Example:** Create a 10MB capped collection for system logs:
```javascript
db.createCollection("logs", { capped: true, size: 10485760 });
```
**Reference:** [Capped Collections](https://www.mongodb.com/docs/manual/core/capped-collections/)

---

---

### 49. How does MongoDB handle data concurrency under the hood?
**Answer:** MongoDB uses reader-writer locks, allowing multiple readers to access data concurrently, but granting exclusive access to a single writer.
**Key Details:**
- Implemented at the global, database, collection, and document level.
- WiredTiger uses ticket controls to manage read/write thread concurrency in memory.
**Reference:** [MongoDB Concurrency and Locks](https://www.mongodb.com/docs/manual/faq/concurrency/)

---

---

### 50. What is the difference between `save()` and `updateOne()` or `replaceOne()`?
**Answer:** `save()` (deprecated in modern shells in favor of explicit write APIs) inserts or replaces documents based on whether `_id` is defined; `updateOne()` edits fields, and `replaceOne()` replaces the entire body matching a query.
**Example:**
```javascript
db.users.replaceOne({ _id: 1 }, { name: "New Name" }); // Bypasses specific field set
```
**Reference:** [Replace Documents Method](https://www.mongodb.com/docs/manual/reference/method/db.collection.replaceOne/)

---

## Expert Questions

---

## Expert Questions

### 51. Explain the architecture of a MongoDB Replica Set in detail.
**Answer:** 
**The Core Concept:**
A cluster of `mongod` nodes maintaining the same dataset to provide redundancy and automatic failover.
**Key Details:**
- **Primary Node**: Single active node processing all write commands.
- **Secondary Nodes**: Replicate data from primary's oplog and can serve read queries.
- **Arbiters**: Do not store data; exist solely to provide a majority vote during primary elections.
**Reference:** [Replica Set Architecture](https://www.mongodb.com/docs/manual/replication/)

---

---

### 52. How does the leader election process work in a Replica Set when a primary fails?
**Answer:** Secondary nodes use a Raft-like consensus protocol to vote for a new primary.
**Key Details:**
- Election is triggered if heartbeats fail for 10 seconds.
- Secondary with the highest priority and most up-to-date `oplog` initiates election.
- Promotion requires a strict majority vote from all voting replica set members.
**Reference:** [Replica Set Elections](https://www.mongodb.com/docs/manual/core/replica-set-elections/)

---

---

### 53. What is the purpose of an Arbiter in a replica set?
**Answer:** An Arbiter is a lightweight process that does not store database files but maintains a vote in elections.
**Key Details:**
- Solves even-numbered tie conflicts without doubling hardware cost (e.g. 2 data nodes + 1 arbiter instead of 3 data nodes).
- Never gets promoted to Primary.
**Example:** `rs.addArb("arbiter.example.com:27017")`
**Reference:** [Replica Set Arbiter](https://www.mongodb.com/docs/manual/core/replica-set-members/#arbiters)

---

---

### 54. Explain what the `oplog` is, how it works, and why it is critical for replication.
**Answer:** The Operation Log is a capped collection in the local database that records all write statements that modify database data.
**Key Details:**
- Secondary nodes read the oplog of their sync source asynchronously to replay updates.
- If a secondary falls too far behind the size of the primary's oplog window, it must perform a full initial sync from scratch.
**Reference:** [Replica Set Oplog](https://www.mongodb.com/docs/manual/core/replica-set-oplog/)

---

---

### 55. What is a Write Concern in MongoDB, and what do `w: 1`, `w: "majority"`, and `j: true` represent?
**Answer:** Settings that dictate write verification guarantees before returning success.
**Key Details:**
- `w: 1`: Return success once written to Primary memory/journal.
- `w: "majority"`: Return success after written to a majority of replica data nodes.
- `j: true`: Enforce journal writing before returning success, ensuring durability.
**Reference:** [Write Concern Guide](https://www.mongodb.com/docs/manual/reference/write-concern/)

---

---

### 56. Explain the concept of Read Concern, detailing `local`, `majority`, and `linearizable`.
**Answer:** Configures consistency and isolation levels for read operations.
**Key Details:**
- `local`: Return most recent data on target node; susceptible to rollback.
- `majority`: Return data confirmed by a majority of nodes; prevents dirty reads.
- `linearizable`: Node pings other nodes to verify it is still the primary before returning, ensuring absolute consistency.
**Reference:** [Read Concern Reference](https://www.mongodb.com/docs/manual/reference/read-concern/)

---

---

### 57. What is Read Preference in MongoDB, and what are its different modes?
**Answer:** Instructs drivers how to route read commands across the replica set.
**Key Details:**
- `primary`: Route to primary only.
- `primaryPreferred`: Route to primary, fall back to secondary.
- `secondary`: Route to secondaries for query scaling.
- `secondaryPreferred`: Route to secondaries first, fall back to primary.
- `nearest`: Route to node with lowest network latency.
**Reference:** [Read Preference](https://www.mongodb.com/docs/manual/core/read-preference/)

---

---

### 58. What is a rollback in replica sets, and when does it occur?
**Answer:** Reverting writes executed on a former primary that crashed before syncing those writes to the secondaries.
**Key Details:**
- Occurs when the crashed primary rejoins as a secondary and discovers its oplog diverges from the new primary.
- Reverted documents are written to rollback files on disk for manual recovery.
**Reference:** [Rollbacks During Replica Set Failover](https://www.mongodb.com/docs/manual/core/replica-set-rollbacks/)

---

---

### 59. How does MongoDB scale write operations horizontally via Sharding?
**Answer:** By partitioning collections along shard keys and distributing partitions (chunks) across multiple physical replica sets (shards).
**Key Details:**
- Eliminates single-server RAM, IOPS, and disk capacity bottlenecks.
- Scales both storage capacity and transaction write throughput.
**Reference:** [Sharding Manual](https://www.mongodb.com/docs/manual/sharding/)

---

---

### 60. What are Config Servers in a sharded cluster, and what metadata do they store?
**Answer:** A dedicated replica set that maintains the configuration settings and mapping data for the entire sharded cluster.
**Key Details:**
- Stores mapping of routing keys to physical shard addresses.
- Active during chunk splits, migrations, and cluster rebalancing.
**Reference:** [Config Servers](https://www.mongodb.com/docs/manual/core/sharded-cluster-config-servers/)

---

---

### 61. What is the role of `mongos` in a sharded cluster?
**Answer:** A routing service that acts as the single interface point for client applications.
**Key Details:**
- Stateless routing proxy.
- Queries config servers to locate target shards and routes client queries.
- Aggregates multi-shard results (scatter-gather) back to the client.
**Reference:** [mongos Router](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/)

---

---

### 62. How do you select a good Shard Key? Compare Ranged vs. Hashed sharding keys.
**Answer:** 
**The Core Concept:**
Selecting a shard key that provides high cardinality, low frequency, and avoids hot-spotting.
**Key Details:**
- **Ranged Sharding**: Keeps data sorted by range. Excellent for range queries, but write bottlenecks occur on monotonically increasing keys (e.g. timestamps).
- **Hashed Sharding**: Hashes field value to disperse writes uniformly across shards. Excellent for uniform write load, but terrible for range scans.
**Reference:** [Shard Keys Selection](https://www.mongodb.com/docs/manual/core/sharding-shard-key/)

---

---

### 63. What is the jumbo chunk problem in MongoDB sharding, and how do you prevent or fix it?
**Answer:** A chunk that grows past the maximum configured chunk size (default 64MB) and cannot be split because all documents share the exact same shard key value.
**Key Details:**
- **Impact**: The balancer cannot migrate jumbo chunks, causing data distribution imbalance.
- **Prevention**: Use a composite shard key with higher cardinality (e.g. `{ zip: 1, _id: 1 }` instead of just `{ zip: 1 }`).
**Reference:** [Clear Jumbo Chunk Flag](https://www.mongodb.com/docs/manual/tutorial/clear-jumbo-flag/)

---

---

### 64. How does the MongoDB balancer work in a sharded cluster?
**Answer:** A background process running on the primary config server that monitors chunk distribution and migrates chunks from overloaded shards to underloaded shards.
**Key Details:**
- Migrations occur online without application downtime.
- Minimizes imbalances in disk space utilization.
**Reference:** [Sharded Cluster Balancer](https://www.mongodb.com/docs/manual/core/sharding-balancer-administration/)

---

---

### 65. Explain WiredTiger storage engine internals, specifically its lock-free architecture.
**Answer:** WiredTiger is the default storage engine which implements optimistic concurrency control (OCC) to achieve high write throughput.
**Key Details:**
- Uses thread-safe Hazard Pointers to track read/write cursors.
- Replaces coarse table/collection locks with row-level modifications.
- Implements Write-Ahead Logging (journaling) and checkpoints.
**Reference:** [WiredTiger Storage Engine](https://www.mongodb.com/docs/manual/core/wiredtiger/)

---

---

### 66. How does WiredTiger utilize memory caching, and how do you configure its cache size?
**Answer:** It uses the WiredTiger Cache to store uncompressed index pages and document structures in memory.
**Key Details:**
- Configured using `--wiredTigerCacheSizeGB`.
- Defaults to 50% of (total RAM minus 1 GB).
- Insufficient cache size triggers aggressive disk page evictions, driving up CPU and disk latency.
**Reference:** [WiredTiger Cache Sizing](https://www.mongodb.com/docs/manual/core/wiredtiger/#memory-use)

---

---

### 67. Explain the `.explain("executionStats")` output in MongoDB and what to look for.
**Answer:** A profiling method that returns detailed execution metrics for a specific database query.
**Key Details:**
- Look at `totalKeysExamined` vs `nReturned` (ideally equal).
- Avoid `COLLSCAN` (collection scan); ensure it performs `IXSCAN` (index scan).
- Watch for `stage: "SORT"` which signifies in-memory sorting due to lack of sort indexing.
**Reference:** [Explain Output Analysis](https://www.mongodb.com/docs/manual/reference/explain-results/)

---

---

### 68. What are index intersections, and when does MongoDB use them?
**Answer:** When a query filters by multiple fields, MongoDB can perform index scans on two separate indexes and intersect the matches in memory.
**Key Details:**
- Bypasses compound index creation in some dynamic query cases.
- Less performant than a dedicated compound index matching the exact query.
**Reference:** [Index Intersection](https://www.mongodb.com/docs/manual/core/index-intersection/)

---

---

### 69. What is a stage scan vs an index scan (`COLLSCAN` vs `IXSCAN`)?
**Answer:** `COLLSCAN` requires reading every document in a collection from disk; `IXSCAN` reads the B-Tree index pages first to target the exact document addresses.
**Example:**
- `COLLSCAN` matches O(N) complexity.
- `IXSCAN` matches O(log N) complexity.
**Reference:** [Query Optimization Concepts](https://www.mongodb.com/docs/manual/core/query-optimization/)

---

---

### 70. How do you find and kill a long-running query in MongoDB?
**Answer:** Query active operations via `db.currentOp()` and terminate using `db.killOp(opId)`.
**Example:**
```javascript
// Find long queries running longer than 10 seconds
db.currentOp({ "active": true, "secs_running": { $gt: 10 } });
// Kill the operation
db.killOp(45291);
```
**Reference:** [Terminate Active Operations](https://www.mongodb.com/docs/manual/reference/method/db.killOp/)

---

---

### 71. What are Change Streams, and how do they work under the hood?
**Answer:** A feature allowing applications to stream real-time data changes in collections, databases, or clusters.
**Key Details:**
- Leverages the `oplog` and acts as a publisher-subscriber model.
- Requires replica sets or sharded clusters.
**Example:**
```javascript
const changeStream = db.users.watch();
changeStream.on("change", next => console.log(next));
```
**Reference:** [Change Streams](https://www.mongodb.com/docs/manual/changeStreams/)

---

---

### 72. Explain GridFS, its architecture, and when it should be used instead of regular documents.
**Answer:** A specification for storing large files that exceed the 16MB BSON document limit.
**Key Details:**
- Splits file into two collections: `fs.files` (metadata) and `fs.chunks` (255KB binary chunks).
- Use for large media files (videos, heavy archives) where direct HTTP stream slicing is required.
**Reference:** [GridFS Specification](https://www.mongodb.com/docs/manual/core/gridfs/)

---

---

### 73. How does MongoDB handle document growth on disk?
**Answer:** WiredTiger handles dynamic allocations by allocating new pages on disk to fit updated, expanded documents, releasing empty space to the operating system or keeping it in its free-lists.
**Key Details:**
- Unlike older engines (MMAPv1) which padded documents, WiredTiger compresses documents using Snappy/Zlib.
- Frequent deep updates causing growth can cause fragmentation on disk files.
**Reference:** [WiredTiger Compression](https://www.mongodb.com/docs/manual/core/wiredtiger/#data-compression)

---

---

### 74. Explain the difference between replica set sync types: initial sync and replication sync.
**Answer:** 
- **Initial Sync**: A secondary copies the entire database snapshot from the primary or another member to seed its storage.
- **Replication Sync**: Continuous asynchronous replication process where the secondary fetches and applies oplog changes in real-time.
**Reference:** [Replica Set Syncing](https://www.mongodb.com/docs/manual/core/replica-set-sync/)

---

---

### 75. What is the split-brain scenario in MongoDB clusters, and how does consensus prevent it?
**Answer:** A partition failure splitting a cluster into two isolated networks where both might attempt to act as the primary database, leading to data divergence.
**Key Details:**
- Consensus prevents this by enforcing that a Primary can only be elected if it communicates with a strict majority (>50%) of all voting members.
- The isolated "minority" network automatically steps down its primary if it loses contact with the majority.
**Reference:** [Replica Set Elections Majority](https://www.mongodb.com/docs/manual/core/replica-set-elections/)

---

---

### 76. What are the key considerations when migrating a database from SQL (e.g. MySQL) to MongoDB?
**Answer:**
**The Core Concept:**
Moving from normalized tables to denormalized, access-pattern-driven document schemas.
**Key Details:**
- **Join Elimination**: Embed sub-tables where possible to make reads atomic.
- **No Foreign Key Constraints**: Referential integrity must be managed at the application level.
- **No Schema Enforcement by default**: Use JSON Schema Validator if strict typing is required.
**Reference:** [Migrate to MongoDB](https://www.mongodb.com/docs/manual/tutorial/migrate-to-mongodb/)

---

---

### 77. How do you configure Role-Based Access Control (RBAC) in MongoDB?
**Answer:** Create users using custom roles or built-in roles (`readWrite`, `dbAdmin`, `root`) within the target database.
**Example:**
```javascript
db.createUser({
  user: "reportsUser",
  pwd: "password123",
  roles: [ { role: "read", db: "e_commerce" } ]
});
```
**Reference:** [Enable Authorization](https://www.mongodb.com/docs/manual/tutorial/enable-authentication/)

---

---

### 78. How does MongoDB implement Encryption at Rest (WiredTiger encryption)?
**Answer:** WiredTiger secures database files by encrypting disk sectors using symmetric keys before writing to the file system.
**Key Details:**
- Supports AES-256 in CBC or GCM modes.
- Managed via KMIP (Key Management Interoperability Protocol) or Amazon KMS.
**Reference:** [Encryption at Rest](https://www.mongodb.com/docs/manual/core/security-encryption-at-rest/)

---

---

### 79. What is Client-Side Field Level Encryption (CSFLE) in MongoDB?
**Answer:** Enordering encryption on sensitive document fields *on the client side* before sending BSON documents over the network.
**Key Details:**
- Fields are encrypted using a Key Management Service (KMS) such as AWS KMS, Azure Key Vault, or GCP KMS.
- Even database administrators (root) cannot view plain text data stored on disk.
**Reference:** [CSFLE Manual](https://www.mongodb.com/docs/manual/core/security-client-side-encryption/)

---

---

### 80. How do you perform Point-In-Time Recovery (PITR) in MongoDB?
**Answer:** Restoring the database to a specific millisecond using filesystem snapshots or oplog archives.
**Key Details:**
- Apply the last full backup image.
- Replay subsequent oplog logs, stopping exactly before the time of the rogue event.
**Reference:** [Point-in-Time Recovery](https://www.mongodb.com/docs/atlas-app-services/backup/pitr/)

---

---

### 81. What is the performance impact of using the `$lookup` stage, and how do you optimize it?
**Answer:** `$lookup` behaves like an unindexed left outer join, which can lead to O(N*M) scans if the joined collection is large.
**Key Details:**
- **Optimization**: Ensure the foreign field in the target collection is indexed.
- Use `$lookup` pipelines with `$match` limits to reduce joined document counts.
**Reference:** [$lookup Performance Tuning](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#performance-considerations)

---

---

### 82. What is index profiling in MongoDB? How do you locate unused indexes?
**Answer:** Monitoring the usage count of active indexes to clean up redundant indexes that degrade write performance.
**Example:** List index usage statistics:
```javascript
db.users.aggregate([ { $indexStats: {} } ]);
```
**Reference:** [$indexStats aggregation](https://www.mongodb.com/docs/manual/reference/operator/aggregation/indexStats/)

---

---

### 83. What is a covered index query, and what are the exact criteria to achieve it?
**Answer:** An ultra-fast index query that returns values directly from index nodes without touching data pages.
**Key Details:**
- The index must contain all fields queried in `find` or `match`.
- The projection must explicitly return only indexed fields and exclude `_id`.
**Reference:** [Covered Index Queries](https://www.mongodb.com/docs/manual/core/query-optimization/#covered-queries)

---

---

### 84. How does MongoDB handle locking? Explain database-level, collection-level, and document-level locking.
**Answer:** MongoDB employs a multi-granularity locking hierarchy: Global (Intent), Database (Intent), Collection (Intent), and Document locks.
**Key Details:**
- **Intent Locks**: Signal that a thread holds a lock at a lower level of the tree.
- WiredTiger handles conflicts optimistically at the document level, escalating to collection locks only when structural schema mutations occur.
**Reference:** [Locks in MongoDB](https://www.mongodb.com/docs/manual/faq/concurrency/)

---

---

### 85. What are the limits on MongoDB document sizes and collection counts?
**Answer:** 
- **Document Size**: Exactly 16MB for a single BSON document.
- **Collection Count**: There is no hard limit, though system resources (file descriptors, WiredTiger catalog size) define practical performance limits.
**Reference:** [MongoDB Limits and Thresholds](https://www.mongodb.com/docs/manual/reference/limits/)

---

---

### 86. Explain the purpose and usage of the `$redact` aggregation stage.
**Answer:** Restricts access to sensitive content based on access credentials embedded within the documents.
**Example:** Filters elements within a single document based on clearance levels:
```javascript
{
  $redact: {
    $cond: {
      if: { $in: [ "manager", "$clearance" ] },
      then: "$$DESCEND",
      else: "$$PRUNE"
    }
  }
}
```
**Reference:** [$redact stage](https://www.mongodb.com/docs/manual/reference/operator/aggregation/redact/)

---

---

### 87. How does the aggregation stage `$bucket` work, and when is it preferred over manual `$group`?
**Answer:** Categorizes incoming documents into structured range groups (buckets) based on defined boundaries.
**Example:** Group items into age brackets:
```javascript
{
  $bucket: {
    groupBy: "$age",
    boundaries: [ 0, 18, 30, 50 ],
    default: "Other"
  }
}
```
**Reference:** [$bucket aggregation](https://www.mongodb.com/docs/manual/reference/operator/aggregation/bucket/)

---

---

### 88. What is the difference between Hashed Sharding and Ranged Sharding regarding query scatter-gather?
**Answer:** 
- **Ranged Sharding**: Allows `mongos` to direct ranged queries (`$gt`) to a single shard.
- **Hashed Sharding**: Scatters writes perfectly, but forces `mongos` to query every shard (scatter-gather) for ranged matches.
**Reference:** [Scatter-Gather Queries](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#scatter-gather-queries)

---

---

### 89. How do you monitor MongoDB performance? Name critical metrics to watch.
**Answer:** Using commands like `db.serverStatus()` or database tools to inspect active operations, memory metrics, and IO usage.
**Key Details:**
- **Queued Operations**: Shows thread execution blocks.
- **Cache Eviction Rates**: Identifies index/memory shortage.
- **Oplog window size**: Confirms replica recovery headroom.
**Reference:** [Monitor MongoDB Performance](https://www.mongodb.com/docs/manual/administration/monitoring/)

---

---

### 90. What is a write conflict in WiredTiger, and how does the engine handle it?
**Answer:** Occurs when two concurrent threads attempt to write to the exact same document simultaneously.
**Key Details:**
- WiredTiger detects conflict, aborts one thread transaction, and transparently retries the write operation without bubbling an error to the user application.
**Reference:** [WiredTiger Concurrency](https://www.mongodb.com/docs/manual/faq/concurrency/#how-does-wiredtiger-handle-concurrent-writes-)

---

---

### 91. What is natural sorting in MongoDB (`$natural`), and when should it be used?
**Answer:** A sort modifier returning documents in the physical order they are stored on disk.
**Example:** Retrieve oldest files quickly from capped collections:
```javascript
db.logs.find().sort({ $natural: 1 });
```
**Reference:** [$natural Sort](https://www.mongodb.com/docs/manual/reference/method/cursor.sort/#natural-order)

---

---

### 92. How does the `$expr` operator allow comparison of fields from the same document?
**Answer:** It enables using aggregation expressions within standard find queries to perform field-to-field comparisons.
**Example:** Find orders where shipping charge exceeds product cost:
```javascript
db.orders.find({ $expr: { $gt: ["$shipping", "$cost"] } });
```
**Reference:** [$expr Operator Reference](https://www.mongodb.com/docs/manual/reference/operator/query/expr/)

---

---

### 93. What is the impact of using `$regex` queries without anchors on index performance?
**Answer:** A regex query without prefix anchors (e.g. `.*word.*`) cannot use index bounds, triggering a full index scan or collection scan.
**Example:**
- Unanchored `/word/`: Slow full scan.
- Anchored `/^word/`: Fast index prefix lookup.
**Reference:** [$regex Index Limitations](https://www.mongodb.com/docs/manual/reference/operator/query/regex/#index-use)

---

---

### 94. How does MongoDB handle decimal precision? Detail `Decimal128`.
**Answer:** It uses the `Decimal128` data type to support up to 34 decimal digits of precision, avoiding float rounding errors.
**Example:** Perfect for monetary values:
```javascript
db.orders.insertOne({ price: NumberDecimal("199.99") });
```
**Reference:** [Decimal128 Data Type](https://www.mongodb.com/docs/manual/core/shell-types/#decimal128)

---

---

### 95. What are schema design anti-patterns in MongoDB? Give three examples.
**Answer:** 
**Key Details:**
- **Unbounded Arrays**: Nesting an infinite array of comments inside posts (reaches 16MB document limit).
- **Too Many Collections**: Designing 1 collection per day or per customer (saturates database catalog memory).
- **Blob Collections**: Treating MongoDB as a key-value blob store, missing out on query filters and indexing.
**Reference:** [Data Modeling Anti-patterns](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1)

---

---

### 96. How do you handle schema migrations or updates in a production MongoDB database?
**Answer:** Through schema evolution or background bulk migrations using cursor streams.
**Key Details:**
- **Evolution**: Let application logic handle legacy document forms dynamically (lazy migration).
- **Active Migration**: Run background update scripts batching changes via `$set` to prevent write locks.
**Reference:** [Schema Migration in MongoDB](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/)

---

---

### 97. Explain what a cold start is in MongoDB and how to warm up the WiredTiger cache.
**Answer:** A situation where a newly rebooted database server starts with an empty RAM cache, leading to disk-bound read times for initial operations.
**Key Details:**
- **Warm up**: Run bulk queries to read indexes and active tables into memory:
```javascript
db.users.find().count(); // forces index scan into cache
```
**Reference:** [MongoDB Performance Optimization](https://www.mongodb.com/docs/manual/administration/analyzing-mongodb-performance/)

---

---

### 98. What is the role of the journal file, and how does it relate to write durability?
**Answer:** The journal is a write-ahead log file that records all data changes before applying them to physical database data pages.
**Key Details:**
- Guarantees durability in crash scenarios.
- Written to disk every 100ms by default.
**Reference:** [Journaling in MongoDB](https://www.mongodb.com/docs/manual/core/journaling/)

---

---

### 99. How does the `$graphLookup` stage work, and what is its primary use case?
**Answer:** A stage that performs a recursive search on a collection to traverse graphs, tree structures, or hierarchies.
**Example:** Traverses organizational hierarchy charts:
```javascript
{
  $graphLookup: {
    from: "employees",
    startWith: "$reportsTo",
    connectFromField: "reportsTo",
    connectToField: "name",
    as: "reportingHierarchy"
  }
}
```
**Reference:** [$graphLookup aggregation](https://www.mongodb.com/docs/manual/reference/operator/aggregation/graphLookup/)

---

---

### 100. How do you perform security audits in a production MongoDB deployment?
**Answer:** By enabling database auditing to record security operations (authentication, role creations, authorization changes) to audit log files.
**Key Details:**
- Configured in `mongod.conf`.
- Outputs in JSON or Syslog format for ingestion into SIEM tools.
**Reference:** [Configure Database Auditing](https://www.mongodb.com/docs/manual/tutorial/configure-auditing/)

---

## Technical Questions

---

### 1. Write a MongoDB Aggregation Pipeline query to group users by age and return the average score.

**Example Solution:**
```javascript
db.users.aggregate([
  { $group: { _id: "$age", avgScore: { $avg: "$score" } } },
  { $sort: { _id: 1 } }
]);
```

---

### 2. Implement a robust transaction in Mongoose to transfer funds between two accounts.

**Example Solution:**
```javascript
const mongoose = require("mongoose");

async function transferFunds(fromId, toId, amount) {
  const session = await mongoose.startSession();
  session.startTransaction();
  try {
    await Account.updateOne({ userId: fromId }, { $inc: { balance: -amount } }, { session });
    await Account.updateOne({ userId: toId }, { $inc: { balance: amount } }, { session });
    await session.commitTransaction();
  } catch (error) {
    await session.abortTransaction();
    throw error;
  } finally {
    session.endSession();
  }
}
```

---

## Technical Questions

### 1. Write a MongoDB Aggregation Pipeline query to group users by age and return the average score.

**Example Solution:**
```javascript
db.users.aggregate([
  { $group: { _id: "$age", avgScore: { $avg: "$score" } } },
  { $sort: { _id: 1 } }
]);
```

### 2. Implement a robust transaction in Mongoose to transfer funds between two accounts.

**Example Solution:**
```javascript
const mongoose = require("mongoose");

async function transferFunds(fromId, toId, amount) {
  const session = await mongoose.startSession();
  session.startTransaction();
  try {
    await Account.updateOne({ userId: fromId }, { $inc: { balance: -amount } }, { session });
    await Account.updateOne({ userId: toId }, { $inc: { balance: amount } }, { session });
    await session.commitTransaction();
  } catch (error) {
    await session.abortTransaction();
    throw error;
  } finally {
    session.endSession();
  }
}
```

### 3. Create a Mongoose schema validation rule with custom validator and compound index.

**Example Solution:**
```javascript
const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    validate: {
      validator: (v) => /\S+@\S+\.\S+/.test(v),
      message: props => `\${props.value} is not a valid email!`
    }
  },
  tenantId: mongoose.Schema.Types.ObjectId
});

userSchema.index({ email: 1, tenantId: 1 }, { unique: true });
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a MongoDB Databases application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy MongoDB Databases operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of MongoDB Databases configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using MongoDB Databases event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing MongoDB Databases with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output MongoDB Databases performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during MongoDB Databases failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to MongoDB Databases data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving MongoDB Databases state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates MongoDB Databases logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle MongoDB Databases files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking MongoDB Databases connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using MongoDB Databases.

*(Challenge question for self-study and practical project implementation.)*

