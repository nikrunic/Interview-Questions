# MySQL Interview Questions

This document contains a comprehensive list of MySQL interview questions, categorized by difficulty.

## Basic (10 Questions)

### 1. What is MySQL?
**Answer:** 
**The Core Concept:**
MySQL is a very popular, open-source Relational Database Management System (RDBMS).

**Key Details:**
- It uses Structured Query Language (SQL) to manage, store, and retrieve data using tables.
- It is owned by Oracle and forms the "M" in the popular LAMP stack (Linux, Apache, MySQL, PHP).
**Example:** Creating a database to store user records for a web application.
**Reference:** [MySQL Reference](https://dev.mysql.com/doc/)

### 2. What are the common Data Types in MySQL?
**Answer:** 
**The Core Concept:**
MySQL supports numeric, date/time, and string (character) types.

**Key Details:**
- **Numeric:** INT, FLOAT, DOUBLE, DECIMAL.
- **String:** CHAR, VARCHAR, TEXT, ENUM, BLOB.
- **Date/Time:** DATE, TIME, DATETIME, TIMESTAMP.
**Example:** `CREATE TABLE users (id INT, name VARCHAR(50));`
**Reference:** [Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

### 3. What is a Primary Key?
**Answer:** 
**The Core Concept:**
A Primary Key uniquely identifies each record in a database table.

**Key Details:**
- It must contain UNIQUE values and cannot contain NULL values.
- A table can have only one Primary Key, which may consist of single or multiple fields (composite key).
**Example:** `id INT AUTO_INCREMENT PRIMARY KEY`
**Reference:** [Primary Keys](https://dev.mysql.com/doc/refman/8.0/en/primary-key-optimization.html)

### 4. What is a Foreign Key?
**Answer:** 
**The Core Concept:**
A Foreign Key is a field (or collection of fields) in one table that refers to the Primary Key in another table.

**Key Details:**
- It is used to prevent actions that would destroy links between tables, enforcing referential integrity.
**Example:** `FOREIGN KEY (user_id) REFERENCES users(id)`
**Reference:** [Foreign Keys](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html)

### 5. What are JOINs in MySQL?
**Answer:** 
**The Core Concept:**
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

**Key Details:**
- **INNER JOIN:** Returns records that have matching values in both tables.
- **LEFT JOIN:** Returns all records from the left table, and the matched records from the right table.
- **RIGHT JOIN:** Returns all records from the right table, and the matched records from the left.
**Example:** `SELECT * FROM orders INNER JOIN users ON orders.user_id = users.id;`
**Reference:** [JOINs](https://dev.mysql.com/doc/refman/8.0/en/join.html)

### 6. What is the difference between CHAR and VARCHAR?
**Answer:** 
**The Core Concept:**
Both store string data, but they differ in how they allocate storage.

**Key Details:**
- `CHAR` has a fixed length. If the data is shorter than the defined length, it is padded with spaces.
- `VARCHAR` has a variable length. It only uses as much storage as the data requires (plus 1 or 2 bytes for length).
**Example:** Use `CHAR(2)` for US State Codes (NY, CA). Use `VARCHAR(255)` for Emails.
**Reference:** [CHAR and VARCHAR](https://dev.mysql.com/doc/refman/8.0/en/char.html)

### 7. What is an Index in MySQL?
**Answer:** 
**The Core Concept:**
An index is a data structure used to speed up the retrieval of records from a database table.

**Key Details:**
- It acts like the index of a book. Instead of scanning the entire table (Table Scan), the database engine uses the index to find the row instantly.
- While it speeds up reads (`SELECT`), it slows down writes (`INSERT`, `UPDATE`) because the index must be updated.
**Example:** `CREATE INDEX idx_lastname ON users (last_name);`
**Reference:** [Indexes](https://dev.mysql.com/doc/refman/8.0/en/mysql-indexes.html)

### 8. What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?
**Answer:** 
**The Core Concept:**
They all remove data, but with different scopes and performance impacts.

**Key Details:**
- `DELETE`: Removes specific rows based on a WHERE clause. It logs the deletion (can be rolled back) and is slower.
- `TRUNCATE`: Empties the entire table immediately without logging individual row deletions (faster, cannot be rolled back).
- `DROP`: Destroys the entire table (schema and data) from the database entirely.
**Example:** `TRUNCATE TABLE logs;`
**Reference:** [TRUNCATE](https://dev.mysql.com/doc/refman/8.0/en/truncate-table.html)

### 9. What is the `GROUP BY` statement?
**Answer:** 
**The Core Concept:**
`GROUP BY` groups rows that have the same values into summary rows.

**Key Details:**
- It is almost always used with aggregate functions (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) to perform a calculation on each group.
**Example:** `SELECT country, COUNT(id) FROM users GROUP BY country;`
**Reference:** [GROUP BY](https://dev.mysql.com/doc/refman/8.0/en/group-by-modifiers.html)

### 10. What is the `HAVING` clause?
**Answer:** 
**The Core Concept:**
The `HAVING` clause is used to filter records that work on summarized `GROUP BY` results.

**Key Details:**
- The `WHERE` keyword cannot be used with aggregate functions, so `HAVING` was introduced to solve this.
**Example:** `SELECT country, COUNT(id) FROM users GROUP BY country HAVING COUNT(id) > 5;`
**Reference:** [HAVING](https://dev.mysql.com/doc/refman/8.0/en/select.html)

## Medium (10 Questions)

### 11. What are ACID properties in a database?
**Answer:** 
**The Core Concept:**
ACID guarantees that database transactions are processed reliably.

**Key Details:**
- **Atomicity:** Entire transaction succeeds, or entire transaction rolls back (no partial data).
- **Consistency:** The database remains in a valid state before and after the transaction.
- **Isolation:** Concurrent transactions do not interfere with each other.
- **Durability:** Once a transaction is committed, it remains saved even in the event of a power loss.
**Example:** Transferring money between two bank accounts securely.
**Reference:** [ACID Model](https://dev.mysql.com/doc/refman/8.0/en/mysql-acid.html)

### 12. What is a View in MySQL?
**Answer:** 
**The Core Concept:**
A view is a virtual table based on the result-set of an SQL statement.

**Key Details:**
- It contains rows and columns just like a real table. The fields in a view are fields from one or more real tables in the database.
- It simplifies complex queries and adds a layer of security (restricting access to specific columns).
**Example:** `CREATE VIEW ActiveUsers AS SELECT name, email FROM users WHERE status = 'active';`
**Reference:** [Views](https://dev.mysql.com/doc/refman/8.0/en/views.html)

### 13. What is a Stored Procedure?
**Answer:** 
**The Core Concept:**
A prepared SQL code that you can save, so the code can be reused over and over again.

**Key Details:**
- It allows you to pass parameters and encapsulate complex business logic natively inside the database server, reducing network traffic between the app and the DB.
**Example:** `CALL GetUserOrders(123);`
**Reference:** [Stored Procedures](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)

### 14. What are Triggers in MySQL?
**Answer:** 
**The Core Concept:**
A trigger is a set of SQL statements that automatically "fire" off in the database server when a specific event occurs.

**Key Details:**
- They are attached to tables and are executed in response to `INSERT`, `UPDATE`, or `DELETE` events. Useful for automatic audit logging.
**Example:** Automatically logging a user's old email to an audit table before it gets updated.
**Reference:** [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)

### 15. What is the difference between `UNION` and `UNION ALL`?
**Answer:** 
**The Core Concept:**
Both operators are used to combine the result sets of two or more `SELECT` statements into a single column output.

**Key Details:**
- `UNION` removes duplicate rows from the combined result set. It requires an internal sorting pass, making it slower.
- `UNION ALL` does not remove duplicate rows. Because it skips the sorting pass, it is significantly faster.
**Example:** `SELECT name FROM clients UNION ALL SELECT name FROM suppliers;`
**Reference:** [UNION](https://dev.mysql.com/doc/refman/8.0/en/union.html)

### 16. What is Database Normalization?
**Answer:** 
**The Core Concept:**
Normalization is the process of structuring a database to reduce data redundancy and improve data integrity.

**Key Details:**
- It involves dividing larger tables into smaller ones and linking them using relationships.
- Common forms include 1NF (atomic columns), 2NF (remove partial dependencies), and 3NF (remove transitive dependencies).
**Example:** Moving a `department_name` out of the `employees` table into a separate `departments` table.
**Reference:** [Normalization](https://en.wikipedia.org/wiki/Database_normalization)

### 17. What is Denormalization?
**Answer:** 
**The Core Concept:**
The deliberate process of adding redundant data back to a normalized database to improve read performance.

**Key Details:**
- When a database is highly normalized, retrieving data requires expensive `JOIN` operations across many tables.
- Denormalization stores the joined data together in one table, trading storage space and slower writes for much faster read queries.
**Example:** Storing `total_order_amount` directly in the `users` table instead of calculating it dynamically from `orders` every time.
**Reference:** [Denormalization](https://en.wikipedia.org/wiki/Denormalization)

### 18. Explain the InnoDB vs MyISAM storage engines.
**Answer:** 
**The Core Concept:**
They are the two primary engines defining how data is stored and handled in MySQL.

**Key Details:**
- **InnoDB:** The modern default. Supports ACID transactions, row-level locking, and foreign key constraints. Highly reliable.
- **MyISAM:** Older engine. Only supports table-level locking and does not support transactions or foreign keys. Extremely fast for read-heavy workloads (like data warehousing) but unsafe for complex apps.
**Example:** You should almost always use `ENGINE=InnoDB`.
**Reference:** [Storage Engines](https://dev.mysql.com/doc/refman/8.0/en/storage-engines.html)

### 19. What is a Subquery?
**Answer:** 
**The Core Concept:**
A subquery (or inner query) is a query nested inside another SQL query (`SELECT`, `INSERT`, `UPDATE`, or `DELETE`).

**Key Details:**
- The subquery executes first, and its result is used by the outer query.
**Example:** `SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);`
**Reference:** [Subqueries](https://dev.mysql.com/doc/refman/8.0/en/subqueries.html)

### 20. How do you find the second highest salary in a table?
**Answer:** 
**The Core Concept:**
This is a classic interview query to test pagination and sorting knowledge.

**Key Details:**
- You order the salaries descending, skip the first one using `OFFSET`, and limit the result to 1.
- Alternatively, you can use a subquery with `MAX()`.
**Example:** `SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;`
**Reference:** [LIMIT](https://dev.mysql.com/doc/refman/8.0/en/limit-optimization.html)

## Hard (10 Questions)

### 21. What is an Execution Plan (EXPLAIN statement)?
**Answer:** 
**The Core Concept:**
The `EXPLAIN` statement provides insight into how the MySQL optimizer will execute a specific query.

**Key Details:**
- It shows whether the query will do a full table scan or use an index, what order tables are joined in, and how many rows are expected to be examined. It is the primary tool for diagnosing slow queries.
**Example:** `EXPLAIN SELECT * FROM users WHERE status = 'active';`
**Reference:** [EXPLAIN](https://dev.mysql.com/doc/refman/8.0/en/explain.html)

### 22. What is a Composite Index?
**Answer:** 
**The Core Concept:**
A composite index is an index on two or more columns of a table.

**Key Details:**
- It speeds up queries that filter on both columns. Crucially, it only works for "leftmost" queries. An index on `(last_name, first_name)` speeds up queries filtering by `last_name`, but NOT queries filtering *only* by `first_name`.
**Example:** `CREATE INDEX idx_name ON users (last_name, first_name);`
**Reference:** [Multiple-Column Indexes](https://dev.mysql.com/doc/refman/8.0/en/multiple-column-indexes.html)

### 23. What are Deadlocks in MySQL and how do you resolve them?
**Answer:** 
**The Core Concept:**
A deadlock occurs when two or more transactions hold locks on resources that the other transactions need, creating an infinite waiting cycle.

**Key Details:**
- InnoDB automatically detects deadlocks and rolls back the transaction that modified the least amount of data.
- To prevent them, applications should access tables and rows in a fixed, consistent order across all transactions.
**Example:** TxA locks Table1, needs Table2. TxB locks Table2, needs Table1.
**Reference:** [Deadlocks](https://dev.mysql.com/doc/refman/8.0/en/innodb-deadlocks.html)

### 24. What is Connection Pooling?
**Answer:** 
**The Core Concept:**
Establishing a physical TCP connection to the database is slow and resource-heavy. Connection pooling creates a cache of ready-to-use connections.

**Key Details:**
- Instead of opening and closing a connection for every single query, applications borrow a connection from the pool and return it when done. This massively improves scalability.
**Example:** Configured via application frameworks (like HikariCP or .NET connection strings).
**Reference:** [Connection Pooling](https://en.wikipedia.org/wiki/Connection_pool)

### 25. Explain the difference between Row-Level Locking and Table-Level Locking.
**Answer:** 
**The Core Concept:**
Locking restricts simultaneous access to data to prevent corruption.

**Key Details:**
- **Table-Level (MyISAM):** Locks the entire table. If User A is updating row 1, User B cannot read or write to row 10,000 until User A finishes. Bad for concurrency.
- **Row-Level (InnoDB):** Locks only the specific row being modified. Other users can freely update different rows in the exact same table simultaneously.
**Example:** Row-level locking makes InnoDB suitable for high-traffic web apps.
**Reference:** [Internal Locking Methods](https://dev.mysql.com/doc/refman/8.0/en/internal-locking.html)

### 26. What is the N+1 Query Problem?
**Answer:** 
**The Core Concept:**
A severe performance anti-pattern often caused by Object-Relational Mappers (ORMs).

**Key Details:**
- The application executes 1 query to fetch a list of N parent items (e.g., 50 Authors). Then, it loops through the parents and executes N individual queries to fetch their children (e.g., 50 separate queries for Books).
- This results in 51 database queries instead of 1 `JOIN` query, destroying network performance.
**Example:** Fixing it involves Eager Loading (`JOIN` or `IN` clauses).
**Reference:** [N+1 Problem](https://secure.phabricator.com/book/phabcontrib/article/n_plus_one/)

### 27. What are the different Transaction Isolation Levels?
**Answer:** 
**The Core Concept:**
Isolation levels define the degree to which transactions are isolated from the data modifications made by other concurrent transactions.

**Key Details:**
1. **Read Uncommitted:** Can see uncommitted changes (Dirty Reads).
2. **Read Committed:** Can only see committed changes (No Dirty Reads).
3. **Repeatable Read (InnoDB Default):** Reading the same row twice gives the exact same result, even if another transaction updated it in the meantime.
4. **Serializable:** Strictest. Locks entire ranges of data, forcing transactions to execute completely sequentially.
**Example:** `SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`
**Reference:** [Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html)

### 28. What is Database Replication?
**Answer:** 
**The Core Concept:**
Replication enables data from one MySQL database server (the master) to be copied automatically to one or more MySQL database servers (the slaves).

**Key Details:**
- Used heavily for High Availability (failover) and scaling read traffic.
- The master handles all `INSERT/UPDATE/DELETE` operations, while the slaves handle `SELECT` operations to distribute the load.
**Example:** Master-Slave replication architecture.
**Reference:** [Replication](https://dev.mysql.com/doc/refman/8.0/en/replication.html)

### 29. What is Database Sharding?
**Answer:** 
**The Core Concept:**
Sharding is a horizontal scaling architecture that breaks a massive database down into smaller, distinct chunks (shards) spread across multiple independent servers.

**Key Details:**
- Unlike replication where every server has a full copy of the data, sharding distributes the data. Users A-M might be on Database Server 1, and Users N-Z on Database Server 2.
- It is highly complex to manage but essential for hyper-scale applications.
**Example:** Sharding by region (US cluster vs EU cluster).
**Reference:** [Database Sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture))

### 30. How do you optimize a slow database?
**Answer:** 
**The Core Concept:**
Database optimization requires identifying the bottleneck (CPU, Memory, IO, or Network).

**Key Details:**
1. Use the `Slow Query Log` to identify problem queries.
2. Run `EXPLAIN` on those queries and add missing Indexes.
3. Rewrite queries to avoid `SELECT *` and avoid functions on indexed columns.
4. Denormalize data or implement Redis caching to reduce DB hits.
5. Upgrade hardware or implement read replicas.
**Example:** Adding an index to a column frequently used in `WHERE` clauses.
**Reference:** [Optimizing MySQL](https://dev.mysql.com/doc/refman/8.0/en/optimize-overview.html)
