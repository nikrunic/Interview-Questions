# MS SQL Server Interview Questions

This document contains a comprehensive list of Microsoft SQL Server (T-SQL) interview questions, categorized by difficulty.

## Basic (10 Questions)

### 1. What is MS SQL Server?
**Answer:** 
**The Core Concept:**
Microsoft SQL Server is a comprehensive, enterprise-level Relational Database Management System (RDBMS) developed by Microsoft.

**Key Details:**
- Its primary query language is T-SQL (Transact-SQL), an extension of standard SQL that adds procedural programming, local variables, and error handling.
**Example:** Used heavily in enterprise Windows/.NET environments.
**Reference:** [SQL Server Docs](https://learn.microsoft.com/en-us/sql/sql-server/)

### 2. What is T-SQL?
**Answer:** 
**The Core Concept:**
Transact-SQL is Microsoft's proprietary extension to standard SQL.

**Key Details:**
- While standard SQL is great for interacting with data, T-SQL adds programming constructs like `IF...ELSE`, `WHILE` loops, `TRY...CATCH` blocks, and local variables using the `@` symbol.
**Example:** `DECLARE @MyVar INT; SET @MyVar = 10;`
**Reference:** [T-SQL Reference](https://learn.microsoft.com/en-us/sql/t-sql/tutorial-writing-transact-sql-statements)

### 3. What is the difference between `VARCHAR` and `NVARCHAR`?
**Answer:** 
**The Core Concept:**
Both store variable-length string data, but they differ in character encoding.

**Key Details:**
- `VARCHAR` stores non-Unicode (ASCII) characters, taking 1 byte per character.
- `NVARCHAR` stores Unicode characters, allowing for international languages (like Japanese or Arabic), taking 2 bytes per character.
**Example:** Use `NVARCHAR` for names that may contain international characters.
**Reference:** [nchar and nvarchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql)

### 4. What is an Identity Column?
**Answer:** 
**The Core Concept:**
A column property that automatically generates unique numeric values for new rows.

**Key Details:**
- Commonly used for Primary Keys. You define a "seed" (starting value) and an "increment" (how much it grows).
- Equivalent to `AUTO_INCREMENT` in MySQL.
**Example:** `ID INT IDENTITY(1,1) PRIMARY KEY`
**Reference:** [IDENTITY property](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql-identity-property)

### 5. What are clustered and non-clustered indexes?
**Answer:** 
**The Core Concept:**
Indexes speed up data retrieval.

**Key Details:**
- **Clustered Index:** Physically sorts and stores the data rows in the table based on the index key. A table can only have *one* clustered index (usually the Primary Key).
- **Non-Clustered Index:** A separate structure from the data rows. It contains pointers back to the actual data rows. A table can have multiple non-clustered indexes.
**Example:** An index at the back of a book (Non-clustered) vs A dictionary sorted alphabetically (Clustered).
**Reference:** [Clustered and Nonclustered Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described)

### 6. What is the `COALESCE` function?
**Answer:** 
**The Core Concept:**
It evaluates the arguments in order and returns the first non-null value.

**Key Details:**
- It is an ANSI SQL standard function. If all arguments are NULL, it returns NULL.
**Example:** `SELECT COALESCE(PhoneNumber, MobileNumber, 'No Contact') FROM Users;`
**Reference:** [COALESCE](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/coalesce-transact-sql)

### 7. What is the `ISNULL` function?
**Answer:** 
**The Core Concept:**
Similar to `COALESCE`, but specific to SQL Server. It replaces NULL with a specified replacement value.

**Key Details:**
- Unlike `COALESCE` which takes many arguments, `ISNULL` only takes two arguments: `ISNULL(check_expression, replacement_value)`.
**Example:** `SELECT ISNULL(Salary, 0) FROM Employees;`
**Reference:** [ISNULL](https://learn.microsoft.com/en-us/sql/t-sql/functions/isnull-transact-sql)

### 8. What is the `@@IDENTITY` vs `SCOPE_IDENTITY()`?
**Answer:** 
**The Core Concept:**
Both retrieve the last generated identity value.

**Key Details:**
- `@@IDENTITY` returns the last identity value generated in *any* table in the current session. (Dangerous if triggers create records elsewhere).
- `SCOPE_IDENTITY()` returns the last identity value generated in the *current scope* (e.g., the current stored procedure), making it the safe and preferred choice.
**Example:** `SELECT SCOPE_IDENTITY();`
**Reference:** [SCOPE_IDENTITY](https://learn.microsoft.com/en-us/sql/t-sql/functions/scope-identity-transact-sql)

### 9. What is a CTE (Common Table Expression)?
**Answer:** 
**The Core Concept:**
A CTE provides a temporary result set that you can reference within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement.

**Key Details:**
- Defined using the `WITH` keyword. It drastically improves the readability of complex queries by breaking them down into logical blocks compared to heavily nested subqueries.
**Example:** `WITH SalesCTE AS (SELECT ... ) SELECT * FROM SalesCTE;`
**Reference:** [WITH common_table_expression](https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql)

### 10. Explain the `GO` command in SQL Server Management Studio (SSMS).
**Answer:** 
**The Core Concept:**
`GO` is not an actual T-SQL statement.

**Key Details:**
- It is a command recognized by MS tools (like SSMS or sqlcmd) to signal the end of a batch of T-SQL statements. Variables defined above a `GO` cannot be accessed below it.
**Example:** Separating multiple schema creation steps.
**Reference:** [GO (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/sql-server-utilities-statements-go)

## Medium (10 Questions)

### 11. What is a Window Function?
**Answer:** 
**The Core Concept:**
A window function performs a calculation across a set of table rows that are somehow related to the current row.

**Key Details:**
- Unlike aggregate functions (which collapse rows into a single group), window functions do not cause rows to become grouped into a single output row. The rows retain their separate identities.
**Example:** `SUM(Salary) OVER (PARTITION BY DepartmentId)`
**Reference:** [Window Functions](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql)

### 12. Explain `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`.
**Answer:** 
**The Core Concept:**
They are window functions used to assign an ordered number to rows within a partition.

**Key Details:**
- `ROW_NUMBER()`: Gives a unique sequential number (1, 2, 3, 4).
- `RANK()`: Gives the same number for ties, but skips subsequent numbers (1, 2, 2, 4).
- `DENSE_RANK()`: Gives the same number for ties, but does *not* skip numbers (1, 2, 2, 3).
**Example:** Finding the top 3 highest salaries per department.
**Reference:** [Ranking Functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/ranking-functions-transact-sql)

### 13. What is a Stored Procedure vs a User Defined Function (UDF)?
**Answer:** 
**The Core Concept:**
Both encapsulate reusable logic, but have different rules.

**Key Details:**
- **Function:** Must return a value (scalar or table). Cannot modify database state (`INSERT`/`UPDATE`/`DELETE`). Can be called from inside a `SELECT` statement.
- **Stored Procedure:** Can return zero or multiple values. Can modify database state. Cannot be called inside a `SELECT` query (must use `EXEC`).
**Example:** `EXEC MyProcedure` vs `SELECT dbo.MyFunction()`.
**Reference:** [UDFs](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions)

### 14. What are Triggers in SQL Server?
**Answer:** 
**The Core Concept:**
A special kind of stored procedure that executes automatically when an event occurs in the database server.

**Key Details:**
- DML Triggers: Fire on `INSERT`, `UPDATE`, `DELETE`.
- DDL Triggers: Fire on schema changes like `CREATE`, `ALTER`, `DROP`.
- Inside DML triggers, you have access to two special temporary tables: `inserted` and `deleted`.
**Example:** Automatically writing an audit log when a record is updated.
**Reference:** [DML Triggers](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/dml-triggers)

### 15. What are the `inserted` and `deleted` magic tables?
**Answer:** 
**The Core Concept:**
Temporary, memory-resident tables available only inside DML triggers.

**Key Details:**
- During an `INSERT`, the new rows are in the `inserted` table.
- During a `DELETE`, the old rows are in the `deleted` table.
- During an `UPDATE`, the original rows are in `deleted` and the new, updated rows are in `inserted`.
**Example:** Comparing `deleted.Salary` to `inserted.Salary` to calculate the raise amount.
**Reference:** [Use the inserted and deleted Tables](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/use-the-inserted-and-deleted-tables)

### 16. What is the difference between a Local Temporary Table and a Global Temporary Table?
**Answer:** 
**The Core Concept:**
They are tables stored in `tempdb` and automatically dropped when no longer needed.

**Key Details:**
- **Local (`#Table`):** Prefixed with a single hash. Only visible to the connection that created it. Dropped when the connection closes.
- **Global (`##Table`):** Prefixed with a double hash. Visible to all connections. Dropped when the last connection referencing it closes.
**Example:** `CREATE TABLE #TempData (id INT);`
**Reference:** [Temporary Tables](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql#temporary-tables)

### 17. What is a Table Variable?
**Answer:** 
**The Core Concept:**
A variable that allows you to store a set of rows temporarily, similar to a temp table.

**Key Details:**
- Declared using `DECLARE @MyTable TABLE`. It is scoped to the stored procedure or batch.
- Generally faster for very small amounts of data compared to `#TempTables` because they do not participate in transactions or locking overhead, but can cause severe performance issues with large datasets due to lack of statistics.
**Example:** `DECLARE @UserIds TABLE (Id INT);`
**Reference:** [Table Variables](https://learn.microsoft.com/en-us/sql/t-sql/data-types/table-transact-sql)

### 18. What is the `PIVOT` operator?
**Answer:** 
**The Core Concept:**
It transforms rows into columns.

**Key Details:**
- It aggregates data and rotates rows into columns to create cross-tabulation reports. (e.g., turning a column of "Months" into 12 individual columns for each month).
**Example:** Pivoting sales data to show monthly columns.
**Reference:** [PIVOT and UNPIVOT](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-using-pivot-and-unpivot)

### 19. What is a Cross Join?
**Answer:** 
**The Core Concept:**
A JOIN without any joining condition.

**Key Details:**
- It produces the Cartesian product of the two tables. If Table A has 10 rows and Table B has 10 rows, the result will have 100 rows.
- Usually an accident unless generating combinations (like sizes and colors).
**Example:** `SELECT * FROM Sizes CROSS JOIN Colors;`
**Reference:** [CROSS JOIN](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins)

### 20. How do you handle errors in T-SQL?
**Answer:** 
**The Core Concept:**
Using `TRY...CATCH` blocks.

**Key Details:**
- Similar to modern programming languages. If a statement inside the `TRY` block throws an error, control transfers to the `CATCH` block where the error can be logged or the transaction rolled back.
**Example:** `BEGIN TRY ... END TRY BEGIN CATCH ... ROLLBACK END CATCH`
**Reference:** [TRY...CATCH](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql)

## Hard (10 Questions)

### 21. What is an Execution Plan?
**Answer:** 
**The Core Concept:**
The visual or textual roadmap showing exactly how the SQL Server Query Optimizer intends to execute (or executed) a query.

**Key Details:**
- It shows the operations performed (Index Seek, Table Scan, Hash Match) and their estimated/actual cost. It is the single most important tool for database performance tuning.
**Example:** Viewing the Actual Execution Plan in SSMS.
**Reference:** [Execution Plans](https://learn.microsoft.com/en-us/sql/relational-databases/performance/execution-plans)

### 22. What is the difference between an Index Seek and an Index Scan?
**Answer:** 
**The Core Concept:**
Indicators in an execution plan showing how an index was used.

**Key Details:**
- **Index Seek:** The optimizer knows exactly where to go in the B-Tree index structure to find the data. Very fast.
- **Index Scan:** The optimizer has to read through the *entire* index from top to bottom to find the data. Slower, often indicating a missing index or non-sargable predicate.
**Example:** Seek = finding a word in the dictionary. Scan = reading every word in the dictionary to find words ending in 'z'.
**Reference:** [Execution Plan Operators](https://learn.microsoft.com/en-us/sql/relational-databases/showplan-logical-and-physical-operators-reference)

### 23. What does "SARGable" mean?
**Answer:** 
**The Core Concept:**
Search Argument Able. A condition that allows the query optimizer to use an Index Seek.

**Key Details:**
- Applying functions or calculations to a column in a `WHERE` clause makes it non-SARGable, forcing a slow Scan instead of a fast Seek.
- *Bad (Non-SARGable):* `WHERE YEAR(OrderDate) = 2023`
- *Good (SARGable):* `WHERE OrderDate >= '2023-01-01' AND OrderDate < '2024-01-01'`
**Example:** Avoiding `LIKE '%text'` (leading wildcards).
**Reference:** [SARGable Queries](https://en.wikipedia.org/wiki/Sargable)

### 24. What are Statistics in SQL Server?
**Answer:** 
**The Core Concept:**
Blobs of data that describe the distribution of values in one or more columns of a table.

**Key Details:**
- The Query Optimizer relies entirely on these statistics to estimate how many rows a query will return. This estimation dictates whether it chooses to do an Index Seek or a Table Scan. If statistics are outdated, the optimizer will make terrible execution choices.
**Example:** `UPDATE STATISTICS Users;`
**Reference:** [Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics)

### 25. Explain the concept of Fill Factor.
**Answer:** 
**The Core Concept:**
Fill Factor determines how much empty space is left on a data page when an index is created or rebuilt.

**Key Details:**
- By default, pages are filled 100%. If a new row is inserted out of order, the page is full and splits into two (Page Split), which destroys performance and causes fragmentation.
- Setting a Fill Factor of 80% leaves 20% room for future inserts, reducing fragmentation in highly volatile tables.
**Example:** Adjusting Fill Factor for a GUID Primary Key.
**Reference:** [Fill Factor](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/specify-fill-factor-for-an-index)

### 26. What is NOLOCK (Read Uncommitted)?
**Answer:** 
**The Core Concept:**
A table hint that allows a query to read data without issuing shared locks.

**Key Details:**
- It prevents the query from being blocked by other transactions, making it very fast.
- However, it can read "Dirty Data" (uncommitted data that might be rolled back a millisecond later), leading to phantom reads or duplicated rows.
**Example:** `SELECT * FROM Orders WITH (NOLOCK);`
**Reference:** [Table Hints](https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-table)

### 27. What is a CTE Recursion?
**Answer:** 
**The Core Concept:**
A Common Table Expression that references itself.

**Key Details:**
- Used heavily for querying hierarchical data, like an Employee Org Chart (Manager -> Employee -> Intern) or a Bill of Materials. It requires an anchor member and a recursive member joined by a `UNION ALL`.
**Example:** Generating a calendar table of dates recursively.
**Reference:** [Recursive CTEs](https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql#guidelines-for-defining-and-using-recursive-common-table-expressions)

### 28. What is the `MERGE` statement?
**Answer:** 
**The Core Concept:**
Also known as an "Upsert". It performs `INSERT`, `UPDATE`, or `DELETE` operations on a target table based on the results of a join with a source table.

**Key Details:**
- It synchronizes two tables in a single statement. If the record matches, `UPDATE`. If not matched by target, `INSERT`. If not matched by source, `DELETE`.
**Example:** Syncing a staging data warehouse table into the production table.
**Reference:** [MERGE](https://learn.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql)

### 29. What is a Bookmark Lookup (Key Lookup)?
**Answer:** 
**The Core Concept:**
An expensive operation shown in an execution plan.

**Key Details:**
- It occurs when the query optimizer uses a Non-Clustered Index to find rows, but the query `SELECT`s columns that are *not* included in that index. The optimizer is forced to jump back (lookup) to the Clustered Index to fetch the missing columns.
- Resolved by creating a Covering Index (using the `INCLUDE` clause).
**Example:** Adding `INCLUDE (Email)` to an index on `LastName` to prevent the lookup.
**Reference:** [Key Lookup Showplan Operator](https://learn.microsoft.com/en-us/sql/relational-databases/showplan-logical-and-physical-operators-reference)

### 30. How do you implement Pagination efficiently in SQL Server?
**Answer:** 
**The Core Concept:**
Retrieving a small chunk of rows (e.g., Page 3, 50 items per page).

**Key Details:**
- Historically done using `ROW_NUMBER()` in a CTE.
- Modern SQL Server (2012+) uses the highly optimized `OFFSET ... FETCH NEXT` clauses attached to the `ORDER BY` statement.
**Example:** `ORDER BY Id OFFSET 100 ROWS FETCH NEXT 50 ROWS ONLY;`
**Reference:** [OFFSET FETCH](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql#using-offset-and-fetch-to-limit-the-rows-returned)
