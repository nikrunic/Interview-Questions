# MS SQL Server Interview Questions

This document contains a comprehensive list of Microsoft SQL Server (T-SQL) interview questions, categorized by difficulty.

## Basic Questions
### 1. What is MS SQL Server?
**Answer:** 
**The Core Concept:**
Microsoft SQL Server is a comprehensive, enterprise-level Relational Database Management System (RDBMS) developed by Microsoft.

**Key Details:**
- Its primary query language is T-SQL (Transact-SQL), an extension of standard SQL that adds procedural programming, local variables, and error handling.
**Example:** Used heavily in enterprise Windows/.NET environments.
**Reference:** [SQL Server Docs](https://learn.microsoft.com/en-us/sql/sql-server/)

---

### 2. What is T-SQL?
**Answer:** 
**The Core Concept:**
Transact-SQL is Microsoft's proprietary extension to standard SQL.

**Key Details:**
- While standard SQL is great for interacting with data, T-SQL adds programming constructs like `IF...ELSE`, `WHILE` loops, `TRY...CATCH` blocks, and local variables using the `@` symbol.
**Example:** `DECLARE @MyVar INT; SET @MyVar = 10;`
**Reference:** [T-SQL Reference](https://learn.microsoft.com/en-us/sql/t-sql/tutorial-writing-transact-sql-statements)

---

### 3. What is the difference between `VARCHAR` and `NVARCHAR`?
**Answer:** 
**The Core Concept:**
Both store variable-length string data, but they differ in character encoding.

**Key Details:**
- `VARCHAR` stores non-Unicode (ASCII) characters, taking 1 byte per character.
- `NVARCHAR` stores Unicode characters, allowing for international languages (like Japanese or Arabic), taking 2 bytes per character.
**Example:** Use `NVARCHAR` for names that may contain international characters.
**Reference:** [nchar and nvarchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql)

---

### 4. What is an Identity Column?
**Answer:** 
**The Core Concept:**
A column property that automatically generates unique numeric values for new rows.

**Key Details:**
- Commonly used for Primary Keys. You define a "seed" (starting value) and an "increment" (how much it grows).
- Equivalent to `AUTO_INCREMENT` in MySQL.
**Example:** `ID INT IDENTITY(1,1) PRIMARY KEY`
**Reference:** [IDENTITY property](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql-identity-property)

---

### 5. What are clustered and non-clustered indexes?
**Answer:** 
**The Core Concept:**
Indexes speed up data retrieval.

**Key Details:**
- **Clustered Index:** Physically sorts and stores the data rows in the table based on the index key. A table can only have *one* clustered index (usually the Primary Key).
- **Non-Clustered Index:** A separate structure from the data rows. It contains pointers back to the actual data rows. A table can have multiple non-clustered indexes.
**Example:** An index at the back of a book (Non-clustered) vs A dictionary sorted alphabetically (Clustered).
**Reference:** [Clustered and Nonclustered Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described)

---

### 6. What is the `COALESCE` function?
**Answer:** 
**The Core Concept:**
It evaluates the arguments in order and returns the first non-null value.

**Key Details:**
- It is an ANSI SQL standard function. If all arguments are NULL, it returns NULL.
**Example:** `SELECT COALESCE(PhoneNumber, MobileNumber, 'No Contact') FROM Users;`
**Reference:** [COALESCE](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/coalesce-transact-sql)

---

### 7. What is the `ISNULL` function?
**Answer:** 
**The Core Concept:**
Similar to `COALESCE`, but specific to SQL Server. It replaces NULL with a specified replacement value.

**Key Details:**
- Unlike `COALESCE` which takes many arguments, `ISNULL` only takes two arguments: `ISNULL(check_expression, replacement_value)`.
**Example:** `SELECT ISNULL(Salary, 0) FROM Employees;`
**Reference:** [ISNULL](https://learn.microsoft.com/en-us/sql/t-sql/functions/isnull-transact-sql)

---

### 8. What is the `@@IDENTITY` vs `SCOPE_IDENTITY()`?
**Answer:** 
**The Core Concept:**
Both retrieve the last generated identity value.

**Key Details:**
- `@@IDENTITY` returns the last identity value generated in *any* table in the current session. (Dangerous if triggers create records elsewhere).
- `SCOPE_IDENTITY()` returns the last identity value generated in the *current scope* (e.g., the current stored procedure), making it the safe and preferred choice.
**Example:** `SELECT SCOPE_IDENTITY();`
**Reference:** [SCOPE_IDENTITY](https://learn.microsoft.com/en-us/sql/t-sql/functions/scope-identity-transact-sql)

---

### 9. What is a CTE (Common Table Expression)?
**Answer:** 
**The Core Concept:**
A CTE provides a temporary result set that you can reference within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement.

**Key Details:**
- Defined using the `WITH` keyword. It drastically improves the readability of complex queries by breaking them down into logical blocks compared to heavily nested subqueries.
**Example:** `WITH SalesCTE AS (SELECT ... ) SELECT * FROM SalesCTE;`
**Reference:** [WITH common_table_expression](https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql)

---

### 10. Explain the `GO` command in SQL Server Management Studio (SSMS).
**Answer:** 
**The Core Concept:**
`GO` is not an actual T-SQL statement.

**Key Details:**
- It is a command recognized by MS tools (like SSMS or sqlcmd) to signal the end of a batch of T-SQL statements. Variables defined above a `GO` cannot be accessed below it.
**Example:** Separating multiple schema creation steps.
**Reference:** [GO (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/sql-server-utilities-statements-go)

---

## Intermediate Questions
### 11. What is a Window Function?
**Answer:** 
**The Core Concept:**
A window function performs a calculation across a set of table rows that are somehow related to the current row.

**Key Details:**
- Unlike aggregate functions (which collapse rows into a single group), window functions do not cause rows to become grouped into a single output row. The rows retain their separate identities.
**Example:** `SUM(Salary) OVER (PARTITION BY DepartmentId)`
**Reference:** [Window Functions](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql)

---

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

---

### 13. What is a Stored Procedure vs a User Defined Function (UDF)?
**Answer:** 
**The Core Concept:**
Both encapsulate reusable logic, but have different rules.

**Key Details:**
- **Function:** Must return a value (scalar or table). Cannot modify database state (`INSERT`/`UPDATE`/`DELETE`). Can be called from inside a `SELECT` statement.
- **Stored Procedure:** Can return zero or multiple values. Can modify database state. Cannot be called inside a `SELECT` query (must use `EXEC`).
**Example:** `EXEC MyProcedure` vs `SELECT dbo.MyFunction()`.
**Reference:** [UDFs](https://learn.microsoft.com/en-us/sql/relational-databases/user-defined-functions/user-defined-functions)

---

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

---

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

---

### 16. What is the difference between a Local Temporary Table and a Global Temporary Table?
**Answer:** 
**The Core Concept:**
They are tables stored in `tempdb` and automatically dropped when no longer needed.

**Key Details:**
- **Local (`#Table`):** Prefixed with a single hash. Only visible to the connection that created it. Dropped when the connection closes.
- **Global (`##Table`):** Prefixed with a double hash. Visible to all connections. Dropped when the last connection referencing it closes.
**Example:** `CREATE TABLE #TempData (id INT);`
**Reference:** [Temporary Tables](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql#temporary-tables)

---

### 17. What is a Table Variable?
**Answer:** 
**The Core Concept:**
A variable that allows you to store a set of rows temporarily, similar to a temp table.

**Key Details:**
- Declared using `DECLARE @MyTable TABLE`. It is scoped to the stored procedure or batch.
- Generally faster for very small amounts of data compared to `#TempTables` because they do not participate in transactions or locking overhead, but can cause severe performance issues with large datasets due to lack of statistics.
**Example:** `DECLARE @UserIds TABLE (Id INT);`
**Reference:** [Table Variables](https://learn.microsoft.com/en-us/sql/t-sql/data-types/table-transact-sql)

---

### 18. What is the `PIVOT` operator?
**Answer:** 
**The Core Concept:**
It transforms rows into columns.

**Key Details:**
- It aggregates data and rotates rows into columns to create cross-tabulation reports. (e.g., turning a column of "Months" into 12 individual columns for each month).
**Example:** Pivoting sales data to show monthly columns.
**Reference:** [PIVOT and UNPIVOT](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-using-pivot-and-unpivot)

---

### 19. What is a Cross Join?
**Answer:** 
**The Core Concept:**
A JOIN without any joining condition.

**Key Details:**
- It produces the Cartesian product of the two tables. If Table A has 10 rows and Table B has 10 rows, the result will have 100 rows.
- Usually an accident unless generating combinations (like sizes and colors).
**Example:** `SELECT * FROM Sizes CROSS JOIN Colors;`
**Reference:** [CROSS JOIN](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins)

---

### 20. How do you handle errors in T-SQL?
**Answer:** 
**The Core Concept:**
Using `TRY...CATCH` blocks.

**Key Details:**
- Similar to modern programming languages. If a statement inside the `TRY` block throws an error, control transfers to the `CATCH` block where the error can be logged or the transaction rolled back.
**Example:** `BEGIN TRY ... END TRY BEGIN CATCH ... ROLLBACK END CATCH`
**Reference:** [TRY...CATCH](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql)

---

## Expert Questions
### 21. What is an Execution Plan?
**Answer:** 
**The Core Concept:**
The visual or textual roadmap showing exactly how the SQL Server Query Optimizer intends to execute (or executed) a query.

**Key Details:**
- It shows the operations performed (Index Seek, Table Scan, Hash Match) and their estimated/actual cost. It is the single most important tool for database performance tuning.
**Example:** Viewing the Actual Execution Plan in SSMS.
**Reference:** [Execution Plans](https://learn.microsoft.com/en-us/sql/relational-databases/performance/execution-plans)

---

### 22. What is the difference between an Index Seek and an Index Scan?
**Answer:** 
**The Core Concept:**
Indicators in an execution plan showing how an index was used.

**Key Details:**
- **Index Seek:** The optimizer knows exactly where to go in the B-Tree index structure to find the data. Very fast.
- **Index Scan:** The optimizer has to read through the *entire* index from top to bottom to find the data. Slower, often indicating a missing index or non-sargable predicate.
**Example:** Seek = finding a word in the dictionary. Scan = reading every word in the dictionary to find words ending in 'z'.
**Reference:** [Execution Plan Operators](https://learn.microsoft.com/en-us/sql/relational-databases/showplan-logical-and-physical-operators-reference)

---

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

---

### 24. What are Statistics in SQL Server?
**Answer:** 
**The Core Concept:**
Blobs of data that describe the distribution of values in one or more columns of a table.

**Key Details:**
- The Query Optimizer relies entirely on these statistics to estimate how many rows a query will return. This estimation dictates whether it chooses to do an Index Seek or a Table Scan. If statistics are outdated, the optimizer will make terrible execution choices.
**Example:** `UPDATE STATISTICS Users;`
**Reference:** [Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics)

---

### 25. Explain the concept of Fill Factor.
**Answer:** 
**The Core Concept:**
Fill Factor determines how much empty space is left on a data page when an index is created or rebuilt.

**Key Details:**
- By default, pages are filled 100%. If a new row is inserted out of order, the page is full and splits into two (Page Split), which destroys performance and causes fragmentation.
- Setting a Fill Factor of 80% leaves 20% room for future inserts, reducing fragmentation in highly volatile tables.
**Example:** Adjusting Fill Factor for a GUID Primary Key.
**Reference:** [Fill Factor](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/specify-fill-factor-for-an-index)

---

### 26. What is NOLOCK (Read Uncommitted)?
**Answer:** 
**The Core Concept:**
A table hint that allows a query to read data without issuing shared locks.

**Key Details:**
- It prevents the query from being blocked by other transactions, making it very fast.
- However, it can read "Dirty Data" (uncommitted data that might be rolled back a millisecond later), leading to phantom reads or duplicated rows.
**Example:** `SELECT * FROM Orders WITH (NOLOCK);`
**Reference:** [Table Hints](https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-table)

---

### 27. What is a CTE Recursion?
**Answer:** 
**The Core Concept:**
A Common Table Expression that references itself.

**Key Details:**
- Used heavily for querying hierarchical data, like an Employee Org Chart (Manager -> Employee -> Intern) or a Bill of Materials. It requires an anchor member and a recursive member joined by a `UNION ALL`.
**Example:** Generating a calendar table of dates recursively.
**Reference:** [Recursive CTEs](https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql#guidelines-for-defining-and-using-recursive-common-table-expressions)

---

### 28. What is the `MERGE` statement?
**Answer:** 
**The Core Concept:**
Also known as an "Upsert". It performs `INSERT`, `UPDATE`, or `DELETE` operations on a target table based on the results of a join with a source table.

**Key Details:**
- It synchronizes two tables in a single statement. If the record matches, `UPDATE`. If not matched by target, `INSERT`. If not matched by source, `DELETE`.
**Example:** Syncing a staging data warehouse table into the production table.
**Reference:** [MERGE](https://learn.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql)

---

### 29. What is a Bookmark Lookup (Key Lookup)?
**Answer:** 
**The Core Concept:**
An expensive operation shown in an execution plan.

**Key Details:**
- It occurs when the query optimizer uses a Non-Clustered Index to find rows, but the query `SELECT`s columns that are *not* included in that index. The optimizer is forced to jump back (lookup) to the Clustered Index to fetch the missing columns.
- Resolved by creating a Covering Index (using the `INCLUDE` clause).
**Example:** Adding `INCLUDE (Email)` to an index on `LastName` to prevent the lookup.
**Reference:** [Key Lookup Showplan Operator](https://learn.microsoft.com/en-us/sql/relational-databases/showplan-logical-and-physical-operators-reference)

---

### 30. How do you implement Pagination efficiently in SQL Server?
**Answer:** 
**The Core Concept:**
Retrieving a small chunk of rows (e.g., Page 3, 50 items per page).

**Key Details:**
- Historically done using `ROW_NUMBER()` in a CTE.
- Modern SQL Server (2012+) uses the highly optimized `OFFSET ... FETCH NEXT` clauses attached to the `ORDER BY` statement.
**Example:** `ORDER BY Id OFFSET 100 ROWS FETCH NEXT 50 ROWS ONLY;`
**Reference:** [OFFSET FETCH](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql#using-offset-and-fetch-to-limit-the-rows-returned)

---


### 31. What is the `VARCHAR(MAX)` and `NVARCHAR(MAX)` data type?
**Answer:** 
**The Core Concept:**
Replacements for the deprecated `TEXT` and `NTEXT` data types.

**Key Details:**
- They can store up to 2 GB of string data. Unlike the old `TEXT` types, they can be used with all standard string functions and operators (like `LIKE` and `=`).
**Example:** Use for storing large JSON payloads or document bodies.
**Reference:** [char and varchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/char-and-varchar-transact-sql)

---

### 32. What is the difference between `DELETE` and `TRUNCATE`?
**Answer:** 
**The Core Concept:**
Commands for removing data from a table.

**Key Details:**
- `DELETE` removes rows one by one and logs each row deletion in the transaction log (slower, can be rolled back). It fires triggers.
- `TRUNCATE` deallocates the data pages storing the table data, logging only the page deallocations (extremely fast). It does not fire triggers and resets Identity columns to their seed value.
**Example:** Use `TRUNCATE TABLE Logs;` to clear logs quickly.
**Reference:** [TRUNCATE TABLE](https://learn.microsoft.com/en-us/sql/t-sql/statements/truncate-table-transact-sql)

---

### 33. What is the `@@ROWCOUNT` variable?
**Answer:** 
**The Core Concept:**
A system variable that returns the number of rows affected by the last statement.

**Key Details:**
- If you run an `UPDATE` and want to know how many rows were modified (e.g., to verify success before committing a transaction), you immediately check `@@ROWCOUNT`.
**Example:** `IF @@ROWCOUNT = 0 PRINT 'No rows updated';`
**Reference:** [@@ROWCOUNT](https://learn.microsoft.com/en-us/sql/t-sql/functions/rowcount-transact-sql)

---

### 34. What is an `UPDATE` trigger?
**Answer:** 
**The Core Concept:**
A DML trigger that executes automatically after an `UPDATE` statement.

**Key Details:**
- You can use the `UPDATE()` function inside the trigger to check if a specific column was modified, allowing you to run expensive audit logic *only* if critical columns (like Salary) were changed.
**Example:** `IF UPDATE(Salary) BEGIN ... END`
**Reference:** [UPDATE()](https://learn.microsoft.com/en-us/sql/t-sql/functions/update-trigger-functions-transact-sql)

---

### 35. What is the difference between `CAST` and `CONVERT`?
**Answer:** 
**The Core Concept:**
Functions used to convert an expression from one data type to another.

**Key Details:**
- `CAST` is the ANSI SQL standard format. It is simpler.
- `CONVERT` is specific to SQL Server. It allows an optional "style" parameter, which is essential for formatting Dates and Times into specific string formats (like MM/DD/YYYY vs YYYY-MM-DD).
**Example:** `CONVERT(VARCHAR(10), GETDATE(), 101)`
**Reference:** [CAST and CONVERT](https://learn.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql)

---

### 36. What is the `HAVING` clause?
**Answer:** 
**The Core Concept:**
Used to filter the results of a `GROUP BY` clause.

**Key Details:**
- The `WHERE` clause filters rows *before* they are grouped. The `HAVING` clause filters the aggregated results *after* they are grouped. You cannot use aggregate functions (`SUM()`, `COUNT()`) in a `WHERE` clause.
**Example:** `SELECT Department, SUM(Salary) FROM Employees GROUP BY Department HAVING SUM(Salary) > 100000;`
**Reference:** [HAVING](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-having-transact-sql)

---

### 37. What is a Schema in SQL Server?
**Answer:** 
**The Core Concept:**
A logical container for database objects.

**Key Details:**
- It acts like a namespace. Objects are referenced using `SchemaName.ObjectName` (e.g., `dbo.Users`). It helps organize large databases and provides a layer for security (granting permissions to an entire schema instead of individual tables).
**Example:** `sales.Orders` vs `hr.Employees`.
**Reference:** [Schemas](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-schema)

---

### 38. What is the `dbo` schema?
**Answer:** 
**The Core Concept:**
The default schema in MS SQL Server.

**Key Details:**
- If a user creates a table without specifying a schema, it defaults to `dbo` (Database Owner).
- Always explicitly stating `dbo.` in your queries (e.g., `SELECT * FROM dbo.Users`) slightly improves performance as SQL Server doesn't have to resolve the default schema.
**Example:** `dbo.MyTable`
**Reference:** [Default Schema](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-schema)

---

### 39. What is the `UNIQUEIDENTIFIER` data type?
**Answer:** 
**The Core Concept:**
A 16-byte GUID (Globally Unique Identifier).

**Key Details:**
- Used when absolute uniqueness across different databases or servers is required. Generated using the `NEWID()` or `NEWSEQUENTIALID()` functions.
- Highly problematic as a Clustered Index (Primary Key) because random GUIDs cause massive index fragmentation (Page Splits) upon insertion.
**Example:** `ID UNIQUEIDENTIFIER DEFAULT NEWID()`
**Reference:** [uniqueidentifier](https://learn.microsoft.com/en-us/sql/t-sql/data-types/uniqueidentifier-transact-sql)

---

### 40. What is the difference between `NEWID()` and `NEWSEQUENTIALID()`?
**Answer:** 
**The Core Concept:**
Methods for generating GUIDs.

**Key Details:**
- `NEWID()` generates a completely random GUID.
- `NEWSEQUENTIALID()` generates a GUID that is greater than any GUID previously generated on that server. This solves the fragmentation problem, making it safe to use as a Clustered Index.
**Example:** `DEFAULT NEWSEQUENTIALID()`
**Reference:** [NEWSEQUENTIALID](https://learn.microsoft.com/en-us/sql/t-sql/functions/newsequentialid-transact-sql)

---

### 41. What is the `OUTPUT` clause?
**Answer:** 
**The Core Concept:**
Returns information from rows affected by an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement.

**Key Details:**
- Highly useful for returning the generated Identity values after a bulk insert, or returning the old values deleted during a cleanup operation. It accesses the `inserted` and `deleted` virtual tables.
**Example:** `INSERT INTO Users (Name) OUTPUT inserted.Id VALUES ('John');`
**Reference:** [OUTPUT Clause](https://learn.microsoft.com/en-us/sql/t-sql/queries/output-clause-transact-sql)

---

### 42. Explain the `APPLY` operator (`CROSS APPLY` vs `OUTER APPLY`).
**Answer:** 
**The Core Concept:**
Used to invoke a table-valued function for each row returned by an outer table query.

**Key Details:**
- `CROSS APPLY` is like an `INNER JOIN`: if the function returns nothing for a row, the outer row is removed from the result set.
- `OUTER APPLY` is like a `LEFT JOIN`: if the function returns nothing, the outer row is still returned with NULLs for the function columns.
**Example:** Executing a string-splitting function on a comma-separated column.
**Reference:** [APPLY](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-using-pivot-and-unpivot)

---

### 43. What are Magic Tables in SQL Server?
**Answer:** 
**The Core Concept:**
The virtual tables `inserted` and `deleted` used in triggers.

**Key Details:**
- They reside in memory and hold the state of rows exactly as they were before and after an operation. They cannot be modified directly.
**Example:** Used to track old values vs new values for auditing.
**Reference:** [inserted and deleted](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/use-the-inserted-and-deleted-tables)

---

### 44. What is a Subquery vs a Correlated Subquery?
**Answer:** 
**The Core Concept:**
Different types of nested queries.

**Key Details:**
- A standard **Subquery** is self-contained. It executes once, and its result is handed to the outer query.
- A **Correlated Subquery** references a column from the outer query. This forces the subquery to execute repeatedly—once for *every single row* returned by the outer query—often causing terrible performance.
**Example:** `SELECT name FROM employees e WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept = e.dept)`
**Reference:** [Correlated Subqueries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries)

---

### 45. What is the `FOR XML` clause?
**Answer:** 
**The Core Concept:**
Formats the results of a query as XML data.

**Key Details:**
- Historically used extensively to pass large datasets to applications or merge strings before `STRING_AGG` was introduced.
**Example:** `SELECT Name FROM Users FOR XML PATH('')`
**Reference:** [FOR XML](https://learn.microsoft.com/en-us/sql/relational-databases/xml/for-xml-sql-server)

---

### 46. What is the `STRING_AGG` function?
**Answer:** 
**The Core Concept:**
Concatenates the values of string expressions and places separator values between them.

**Key Details:**
- Introduced in SQL Server 2017, it replaces the massive hack of using `FOR XML PATH` and `STUFF` to create comma-separated lists from grouped data. Equivalent to `GROUP_CONCAT` in MySQL.
**Example:** `SELECT STRING_AGG(RoleName, ', ') FROM Roles;`
**Reference:** [STRING_AGG](https://learn.microsoft.com/en-us/sql/t-sql/functions/string-agg-transact-sql)

---

### 47. Explain the `EXISTS` vs `IN` performance differences.
**Answer:** 
**The Core Concept:**
Operators for checking if values are contained in a subquery.

**Key Details:**
- `IN` compares values directly. If the subquery contains `NULL` values, it can lead to unexpected missing results.
- `EXISTS` is highly optimized. It returns a boolean and stops processing the subquery the instant it finds a single match, making it vastly faster than `IN` for large datasets.
**Example:** Always prefer `IF EXISTS (SELECT 1 FROM...)` over `IF @val IN (SELECT...)`.
**Reference:** [EXISTS](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/exists-transact-sql)

---

### 48. What is Dynamic SQL?
**Answer:** 
**The Core Concept:**
SQL code constructed as a string variable at runtime and then executed.

**Key Details:**
- Executed using `EXEC()` or the safer `sp_executesql`. Necessary when table names or column names must be parameterized (which standard SQL doesn't allow).
- Extremely dangerous if not handled correctly due to SQL Injection risks.
**Example:** `EXEC sp_executesql N'SELECT * FROM ' + @TableName;`
**Reference:** [sp_executesql](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-executesql-transact-sql)

---

### 49. How do you prevent SQL Injection in Stored Procedures?
**Answer:** 
**The Core Concept:**
Ensuring user inputs cannot execute malicious code.

**Key Details:**
- Stored procedures natively prevent injection because standard parameters (`@Name`) are treated purely as literal values, not executable code.
- If using Dynamic SQL inside a procedure, you must use `sp_executesql` with strong parameters, NEVER direct string concatenation (`EXEC('... WHERE id=' + @Id)`).
**Example:** Using parameterized inputs in `sp_executesql`.
**Reference:** [SQL Injection](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-security-best-practices)

---

### 50. What is the difference between an Error and an Exception in T-SQL?
**Answer:** 
**The Core Concept:**
Error handling mechanisms.

**Key Details:**
- T-SQL uses severity levels (0-25) to categorize errors.
- Severity 11-19 are exceptions that can be caught by a `TRY...CATCH` block. Severity 20+ are fatal system errors that terminate the connection immediately and cannot be caught.
**Example:** Using `RAISERROR` or `THROW` to generate exceptions.
**Reference:** [Database Engine Errors](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/database-engine-error-severities)

---

### 51. What is an Execution Plan?
**Answer:** 
**The Core Concept:**
The visual roadmap of how the Query Optimizer retrieved the data.

**Key Details:**
- It is the most important tool for performance tuning. It reveals Index Scans vs Seeks, Hash Matches vs Nested Loops, Key Lookups, and missing index warnings.
**Example:** Pressing `Ctrl + M` in SSMS before executing a query.
**Reference:** [Execution Plans](https://learn.microsoft.com/en-us/sql/relational-databases/performance/execution-plans)

---

### 52. What is an Index Seek vs an Index Scan?
**Answer:** 
**The Core Concept:**
How SQL Server navigates an index B-Tree.

**Key Details:**
- **Seek:** The optimizer uses the B-Tree structure to navigate directly to the specific rows it needs. Highly efficient.
- **Scan:** The optimizer reads every single row in the index from beginning to end to find the data. Very slow on large tables; usually indicates a missing index or non-SARGable `WHERE` clause.
**Example:** `WHERE LastName = 'Smith'` (Seek) vs `WHERE LastName LIKE '%Smith'` (Scan).
**Reference:** [Showplan Operators](https://learn.microsoft.com/en-us/sql/relational-databases/showplan-logical-and-physical-operators-reference)

---

### 53. What is a SARGable query?
**Answer:** 
**The Core Concept:**
Search ARGument ABLE. A query structured so the optimizer can use an Index Seek.

**Key Details:**
- Wrapping an indexed column in a function destroys SARGability because SQL must calculate the function for every row before checking the index, resulting in an Index Scan.
- **Bad:** `WHERE YEAR(OrderDate) = 2023`
- **Good:** `WHERE OrderDate >= '2023-01-01' AND OrderDate < '2024-01-01'`
**Example:** Never perform math on the left side of the `=`.
**Reference:** [SARGable](https://en.wikipedia.org/wiki/Sargable)

---

### 54. What are Statistics in SQL Server?
**Answer:** 
**The Core Concept:**
Histograms detailing the distribution of data values in a column.

**Key Details:**
- The Query Optimizer relies on these statistics to estimate how many rows will be returned. This estimate determines whether it chooses a Nested Loop Join or a Hash Join, and whether to Seek or Scan. If statistics are outdated, the optimizer will create disastrous execution plans.
**Example:** `UPDATE STATISTICS dbo.Users;`
**Reference:** [Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics)

---

### 55. What is Parameter Sniffing?
**Answer:** 
**The Core Concept:**
A performance issue related to Stored Procedure execution plans.

**Key Details:**
- The first time a procedure runs, SQL Server compiles an Execution Plan based on the specific parameter provided (e.g., Status = 'Active'). It caches this plan.
- If 'Active' returns 1 million rows, the plan uses Scans. If the next user passes 'Archived' (which returns 2 rows), it reuses the cached Scan plan instead of a fast Seek, causing terrible performance.
**Example:** Fixed using `OPTION (RECOMPILE)` or local variables.
**Reference:** [Parameter Sniffing](https://learn.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide#parameter-sniffing)

---

### 56. What is a Bookmark Lookup (Key Lookup)?
**Answer:** 
**The Core Concept:**
A costly operation shown in an execution plan.

**Key Details:**
- It happens when an index is used to find a row, but the query `SELECT`s a column that is not included in that index. The engine must jump (lookup) from the non-clustered index back to the clustered index to retrieve the missing column data.
**Example:** Avoided by creating a Covering Index using the `INCLUDE` clause.
**Reference:** [Key Lookup](https://learn.microsoft.com/en-us/sql/relational-databases/showplan-logical-and-physical-operators-reference)

---

### 57. What is a Covering Index?
**Answer:** 
**The Core Concept:**
A non-clustered index that includes all columns required by a specific query.

**Key Details:**
- Using the `INCLUDE` keyword, you can add non-key columns to the leaf level of the index. If the query is completely "covered" by the index, SQL Server never touches the actual data table, resulting in maximum performance.
**Example:** `CREATE INDEX idx ON Users (LastName) INCLUDE (FirstName, Email);`
**Reference:** [Indexes with Included Columns](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-indexes-with-included-columns)

---

### 58. Explain the concept of Fill Factor.
**Answer:** 
**The Core Concept:**
A setting that dictates how full data pages are when an index is created or rebuilt.

**Key Details:**
- A page holds 8KB. At 100% Fill Factor, the page is full. If a new row is inserted, the page must split into two (Page Split), causing heavy disk I/O and fragmentation.
- A Fill Factor of 80% leaves 20% empty space for future inserts. Crucial for non-sequential keys (like GUIDs).
**Example:** `CREATE INDEX idx ON Users (ID) WITH (FILLFACTOR = 80);`
**Reference:** [Fill Factor](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/specify-fill-factor-for-an-index)

---

### 59. What is Index Fragmentation?
**Answer:** 
**The Core Concept:**
When the logical ordering of index pages does not match the physical ordering on disk.

**Key Details:**
- Caused by Page Splits resulting from inserts, updates, or deletes. High fragmentation forces the disk to work harder to read data. Fixed by `ALTER INDEX REORGANIZE` (for < 30% fragmentation) or `REBUILD` (for > 30%).
**Example:** Maintaining indexes via SQL Server Agent jobs.
**Reference:** [Resolve index fragmentation](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes)

---

### 60. What is a Deadlock?
**Answer:** 
**The Core Concept:**
A situation where two transactions hold locks on resources the other needs, blocking both indefinitely.

**Key Details:**
- SQL Server detects this cycle and automatically kills one of the transactions (the "Deadlock Victim") so the other can complete.
- Prevented by accessing tables in the exact same order across all procedures, keeping transactions short, and ensuring proper indexing to minimize lock duration.
**Example:** Transaction A locks Table 1, needs Table 2. Transaction B locks Table 2, needs Table 1.
**Reference:** [Deadlocks](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide#deadlocks)

---

### 61. What is the `NOLOCK` table hint?
**Answer:** 
**The Core Concept:**
Instructs the query to read data without acquiring shared locks.

**Key Details:**
- It completely bypasses blocking issues, making queries incredibly fast.
- The severe danger is "Dirty Reads"—reading data from an uncommitted transaction that might be rolled back a millisecond later. Do not use it for financial or critical data.
**Example:** `SELECT * FROM Orders WITH (NOLOCK);`
**Reference:** [Table Hints](https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-table)

---

### 62. What is RCSI (Read Committed Snapshot Isolation)?
**Answer:** 
**The Core Concept:**
A database-level setting that solves blocking without the dangers of `NOLOCK`.

**Key Details:**
- It uses Row Versioning (stored in `tempdb`). When a transaction updates a row, the old version is kept. Readers will read the old, consistent version instead of being blocked by the writer or reading dirty data. It provides Oracle-like MVCC concurrency.
**Example:** `ALTER DATABASE MyDB SET READ_COMMITTED_SNAPSHOT ON;`
**Reference:** [Snapshot Isolation](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/snapshot-isolation-in-sql-server)

---

### 63. What are the different Transaction Isolation Levels?
**Answer:** 
**The Core Concept:**
They define how isolated a transaction is from data modified by other transactions.

**Key Details:**
1. **Read Uncommitted:** Allows Dirty Reads (same as `NOLOCK`).
2. **Read Committed (Default):** Prevents Dirty Reads but allows Non-Repeatable Reads.
3. **Repeatable Read:** Prevents Dirty and Non-Repeatable reads, but allows Phantom Reads.
4. **Serializable:** Locks data ranges, preventing Phantom Reads. Highest safety, lowest concurrency.
**Example:** `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`
**Reference:** [Isolation Levels](https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql)

---

### 64. What is a Phantom Read?
**Answer:** 
**The Core Concept:**
A concurrency phenomenon.

**Key Details:**
- Transaction A runs `SELECT COUNT(*) WHERE Age > 30` and gets 10. Transaction B inserts a new person aged 35. Transaction A runs the same query and gets 11. The new row is the "phantom".
- Prevented by the `SERIALIZABLE` isolation level via Range Locks.
**Example:** Concurrency anomalies.
**Reference:** [Concurrency Effects](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide)

---

### 65. What is the `MERGE` statement?
**Answer:** 
**The Core Concept:**
Combines `INSERT`, `UPDATE`, and `DELETE` into a single statement.

**Key Details:**
- It compares a source table with a target table. "WHEN MATCHED THEN UPDATE", "WHEN NOT MATCHED THEN INSERT". Extremely powerful for syncing data warehouse dimensions or ETL processes.
**Example:** Syncing an import file with the production table.
**Reference:** [MERGE](https://learn.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql)

---

### 66. How do you implement Pagination in SQL Server?
**Answer:** 
**The Core Concept:**
Retrieving rows in chunks (e.g., Page 2, 50 items per page).

**Key Details:**
- Before 2012, this required complex `ROW_NUMBER()` logic. Modern T-SQL uses the `OFFSET ... FETCH NEXT` clause natively attached to the `ORDER BY` statement.
**Example:** `ORDER BY Id OFFSET 50 ROWS FETCH NEXT 50 ROWS ONLY;`
**Reference:** [OFFSET FETCH](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql)

---

### 67. Explain Table Partitioning.
**Answer:** 
**The Core Concept:**
Splitting a massive table across multiple physical filegroups while it continues to look like a single logical table to the application.

**Key Details:**
- Heavily used for archiving. If you partition logs by year, dropping the 2010 partition takes milliseconds (metadata update), whereas running `DELETE FROM Logs WHERE Year = 2010` on a billion-row table would crash the transaction log.
**Example:** `CREATE PARTITION FUNCTION`
**Reference:** [Partitioned Tables](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes)

---

### 68. What is a Recursive CTE?
**Answer:** 
**The Core Concept:**
A CTE that references itself, used to traverse hierarchical data.

**Key Details:**
- It consists of an "Anchor Member" (the base query, like the CEO of a company) and a "Recursive Member" (which joins back to the CTE to find direct reports), combined with a `UNION ALL`.
**Example:** Querying an Employee-Manager organizational chart or category trees.
**Reference:** [Recursive CTEs](https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql)

---

### 69. What are Window Aggregate Functions?
**Answer:** 
**The Core Concept:**
Performing aggregates without losing row-level details.

**Key Details:**
- Normally, `SUM(Salary)` collapses all rows into one. Using `SUM(Salary) OVER (PARTITION BY Department)` calculates the department total and appends it as a column to *every individual row*, without collapsing them.
**Example:** Calculating an employee's salary as a percentage of their department's total budget.
**Reference:** [OVER Clause](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql)

---

### 70. What is an Indexed View?
**Answer:** 
**The Core Concept:**
A View that has a Unique Clustered Index applied to it.

**Key Details:**
- Normally, a View is just a saved query. When queried, it runs the underlying SQL. If you add an index to it, SQL Server actually executes the View and materializes the result set to disk. Massive performance boost for heavy aggregation Views, but slows down inserts to the underlying tables.
**Example:** Equivalent to "Materialized Views" in Oracle/Postgres.
**Reference:** [Indexed Views](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views)

---

### 71. What is TempDB and why is it a bottleneck?
**Answer:** 
**The Core Concept:**
A system database that holds temporary objects.

**Key Details:**
- It stores `#TempTables`, table variables, sorting operations that spill from RAM, and row versions for RCSI. Because every user database on the server shares the same `tempdb`, heavy usage can cause severe physical disk contention (PAGELATCH wait types).
**Example:** Best practice is to split `tempdb` into multiple data files equal to the number of CPU cores.
**Reference:** [tempdb Database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/tempdb-database)

---

### 72. What are Columnstore Indexes?
**Answer:** 
**The Core Concept:**
The standard for storing and querying large data warehousing fact tables.

**Key Details:**
- Traditional indexes store data row by row (Rowstore). Columnstore stores data column by column. This allows massive data compression (up to 10x) and blistering fast aggregation speeds for analytical queries (`SUM`, `AVG`), as it only reads the columns requested.
**Example:** `CREATE CLUSTERED COLUMNSTORE INDEX idx ON FactSales;`
**Reference:** [Columnstore Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview)

---

### 73. What is the Transaction Log?
**Answer:** 
**The Core Concept:**
The file (.ldf) that records all transactions and database modifications made by each transaction.

**Key Details:**
- It guarantees ACID properties. In the event of a crash, SQL Server uses the log to roll forward committed transactions and roll back uncommitted ones. If a database is in "Full Recovery Mode", the log will grow infinitely until a Log Backup is taken.
**Example:** Shrinking a bloated LDF file.
**Reference:** [Transaction Log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server)

---

### 74. Explain Full vs Simple Recovery Models.
**Answer:** 
**The Core Concept:**
Settings dictating how the Transaction Log is maintained.

**Key Details:**
- **Simple:** The log is truncated immediately after a transaction completes. Space is reused. Point-in-time recovery is impossible. (Good for Dev/Test).
- **Full:** The log is never truncated automatically. It keeps all history, allowing restoration to an exact minute (e.g., 2:04 PM). Requires regular Log Backups to prevent the disk from filling up.
**Example:** Setting production databases to Full Recovery.
**Reference:** [Recovery Models](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server)

---

### 75. What is the `@@TRANCOUNT` variable?
**Answer:** 
**The Core Concept:**
Returns the number of active `BEGIN TRANSACTION` statements that have occurred on the current connection.

**Key Details:**
- Highly important in nested stored procedures. `BEGIN TRAN` increments it, `COMMIT TRAN` decrements it. `ROLLBACK TRAN` forces it to 0 and cancels the entire transaction chain regardless of nesting.
**Example:** `IF @@TRANCOUNT > 0 COMMIT TRANSACTION;`
**Reference:** [@@TRANCOUNT](https://learn.microsoft.com/en-us/sql/t-sql/functions/trancount-transact-sql)

---

### 76. What is `sp_who2` and `sys.dm_exec_requests`?
**Answer:** 
**The Core Concept:**
Tools used to troubleshoot performance and blocking.

**Key Details:**
- `sp_who2` is a legacy stored procedure showing current users and processes.
- Dynamic Management Views (DMVs) like `sys.dm_exec_requests` and `sys.dm_exec_sessions` provide modern, incredibly deep diagnostic data about what queries are currently executing, CPU time, and wait stats.
**Example:** Finding the SPID of a blocking query.
**Reference:** [sys.dm_exec_requests](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-exec-requests-transact-sql)

---

### 77. What are Wait Statistics?
**Answer:** 
**The Core Concept:**
Metrics tracked by SQL Server detailing exactly why a query had to pause execution.

**Key Details:**
- Instead of guessing why a database is slow, you look at Wait Stats. `PAGEIOLATCH_SH` means queries are waiting on slow disk reads. `LCK_M_U` means queries are blocked waiting for locks. It is the definitive guide to bottleneck analysis.
**Example:** Querying `sys.dm_os_wait_stats`.
**Reference:** [Wait Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-wait-stats-transact-sql)

---

### 78. What is a Filtered Index?
**Answer:** 
**The Core Concept:**
A nonclustered index optimized for queries that select a well-defined subset of data.

**Key Details:**
- It uses a filter predicate to index a portion of rows. E.g., if you only ever search for "Active" users, a filtered index on `LastName WHERE IsActive = 1` takes up significantly less disk space and maintenance overhead than indexing the whole table.
**Example:** `CREATE INDEX idx ON Users(LastName) WHERE IsActive = 1;`
**Reference:** [Filtered Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/create-filtered-indexes)

---

### 79. Explain `CROSS JOIN` vs `INNER JOIN`.
**Answer:** 
**The Core Concept:**
Table combinations.

**Key Details:**
- `INNER JOIN` combines rows based on a specific logical condition (`ON A.id = B.id`).
- `CROSS JOIN` has no condition. It creates a Cartesian product. If you have 5 cars and 5 colors, a CROSS JOIN outputs all 25 possible combinations.
**Example:** Generating test permutations.
**Reference:** [Joins](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins)

---

### 80. What is Query Folding in Linked Servers?
**Answer:** 
**The Core Concept:**
How SQL Server executes queries directed at an external Linked Server (like an Oracle DB or another SQL Server).

**Key Details:**
- If folding works, SQL Server sends the entire query to the remote server, and only the small result set is returned over the network. If the remote server doesn't support the syntax, SQL Server pulls the *entire remote table* across the network and filters it locally, destroying performance.
**Example:** `SELECT * FROM [RemoteServer].[DB].[dbo].[Users] WHERE Id = 1`
**Reference:** [Linked Servers](https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine)

---

### 81. What is the `sp_executesql` procedure?
**Answer:** 
**The Core Concept:**
The recommended system stored procedure for executing Dynamic SQL.

**Key Details:**
- Unlike `EXEC()`, `sp_executesql` allows parameter substitution. This natively protects against SQL Injection and allows SQL Server to cache and reuse the Execution Plan, vastly improving performance for dynamic queries.
**Example:** `EXEC sp_executesql N'SELECT * FROM Users WHERE Age > @A', N'@A int', @A = 25;`
**Reference:** [sp_executesql](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-executesql-transact-sql)

---

### 82. What is `MAXDOP`?
**Answer:** 
**The Core Concept:**
Maximum Degree of Parallelism.

**Key Details:**
- It controls the number of CPU processors used to execute a single query. By default (0), a complex query can hijack all CPUs, starving other queries. DBAs typically restrict MAXDOP to prevent a single bad query from taking down the server.
**Example:** Query hint: `OPTION (MAXDOP 4)`
**Reference:** [MAXDOP](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option)

---

### 83. What are In-Memory OLTP Tables?
**Answer:** 
**The Core Concept:**
Tables that reside entirely in memory (RAM) rather than on disk.

**Key Details:**
- Introduced in 2014, they use lock-free data structures. Extremely fast for high-concurrency, high-throughput transaction scenarios (like session state or IoT data ingestion). They can be configured as durable (survive restarts) or non-durable.
**Example:** `CREATE TABLE ... WITH (MEMORY_OPTIMIZED = ON);`
**Reference:** [In-Memory OLTP](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/in-memory-oltp-in-memory-optimization)

---

### 84. What is the `CHECKSUM` and `HASHBYTES` functions?
**Answer:** 
**The Core Concept:**
Functions used to detect changes in a row or encrypt passwords.

**Key Details:**
- `CHECKSUM` calculates a hash value over a row. It's fast but prone to collisions.
- `HASHBYTES` uses standard cryptographic algorithms (like SHA2_256) to return a secure hash. Used extensively for storing password hashes.
**Example:** `SELECT HASHBYTES('SHA2_256', 'Password123');`
**Reference:** [HASHBYTES](https://learn.microsoft.com/en-us/sql/t-sql/functions/hashbytes-transact-sql)

---

### 85. What is Change Data Capture (CDC)?
**Answer:** 
**The Core Concept:**
A feature that records insert, update, and delete activity applied to tables.

**Key Details:**
- Instead of using triggers (which slow down transactions), CDC reads the Transaction Log asynchronously and writes the changes to specific tracking tables. Ideal for ETL pipelines syncing SQL Server to a Data Warehouse or Elasticsearch.
**Example:** Enabling CDC on the `Orders` table.
**Reference:** [Change Data Capture](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server)

---

### 86. Explain Temporal Tables (System-Versioned).
**Answer:** 
**The Core Concept:**
Tables that automatically keep a full history of data changes.

**Key Details:**
- Introduced in 2016, when an `UPDATE` or `DELETE` occurs, the engine automatically copies the old row into a hidden History table, stamped with the exact time. You can query the table using `FOR SYSTEM_TIME AS OF '2023-01-01'` to see exactly what the data looked like in the past.
**Example:** Ideal for strict auditing and compliance.
**Reference:** [Temporal Tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables)

---

### 87. What is an Aggregate Window Function?
**Answer:** 
**The Core Concept:**
Aggregates like `SUM()` applied over a window of rows.

**Key Details:**
- Using `ORDER BY` inside the `OVER()` clause creates a running total. `SUM(Sales) OVER (ORDER BY Date)` will sum the current row with all previous rows, creating a cumulative calculation instantly without subqueries.
**Example:** Calculating a running bank balance.
**Reference:** [OVER Clause](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql)

---

### 88. What is the `CHOOSE` function?
**Answer:** 
**The Core Concept:**
Returns the item at the specified index from a list of values.

**Key Details:**
- Acts like an array index lookup. Simpler than a `CASE` statement when mapping integers to strings.
**Example:** `SELECT CHOOSE(StatusId, 'Pending', 'Active', 'Closed');`
**Reference:** [CHOOSE](https://learn.microsoft.com/en-us/sql/t-sql/functions/choose-transact-sql)

---

### 89. What is the `IIF` function?
**Answer:** 
**The Core Concept:**
A shorthand for a simple `CASE` expression.

**Key Details:**
- Borrowed from Access/Excel syntax. It evaluates a boolean expression and returns one value if true, another if false.
**Example:** `SELECT IIF(Score > 50, 'Pass', 'Fail') FROM Exams;`
**Reference:** [IIF](https://learn.microsoft.com/en-us/sql/t-sql/functions/logical-functions-iif-transact-sql)

---

### 90. What is `TRY_CONVERT` vs `CONVERT`?
**Answer:** 
**The Core Concept:**
Safe data type conversions.

**Key Details:**
- If `CONVERT` fails (e.g., trying to cast 'ABC' to an `INT`), the entire query crashes with a fatal error.
- `TRY_CONVERT` returns `NULL` if the cast fails, allowing the query to complete successfully without exception handling.
**Example:** `SELECT TRY_CONVERT(INT, '123A'); -- Returns NULL`
**Reference:** [TRY_CONVERT](https://learn.microsoft.com/en-us/sql/t-sql/functions/try-convert-transact-sql)

---

### 91. Explain Always On Availability Groups.
**Answer:** 
**The Core Concept:**
The premier High Availability (HA) and Disaster Recovery (DR) solution in SQL Server.

**Key Details:**
- Replaces database mirroring. It replicates transactions from a Primary replica to up to 8 Secondary replicas. It allows automatic failover and allows the Secondary replicas to be queried for read-only workloads (offloading reporting from the master).
**Example:** Enterprise data redundancy.
**Reference:** [Always On](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/always-on-availability-groups-sql-server)

---

### 92. What are sequence objects?
**Answer:** 
**The Core Concept:**
A user-defined schema-bound object that generates a sequence of numeric values.

**Key Details:**
- Similar to an Identity column, but an Identity is bound to a specific table. A Sequence is an independent database object, meaning multiple tables can share the exact same sequence of numbers.
**Example:** `NEXT VALUE FOR SalesSequence;`
**Reference:** [Sequence Numbers](https://learn.microsoft.com/en-us/sql/relational-databases/sequence-numbers/sequence-numbers)

---

### 93. What is a Table-Valued Parameter (TVP)?
**Answer:** 
**The Core Concept:**
A way to pass multiple rows of data to a stored procedure.

**Key Details:**
- Instead of executing a stored procedure 1,000 times to insert 1,000 rows (slow network overhead) or passing a giant comma-separated string, you define a User-Defined Table Type and pass the entire C# DataTable as a single parameter to the procedure.
**Example:** `EXEC InsertUsers @UsersList = @MyDataTable;`
**Reference:** [Table-Valued Parameters](https://learn.microsoft.com/en-us/sql/relational-databases/tables/use-table-valued-parameters-database-engine)

---

### 94. What is the Query Store?
**Answer:** 
**The Core Concept:**
A built-in feature that captures a history of queries, execution plans, and runtime statistics.

**Key Details:**
- Before Query Store, if a query suddenly became slow, diagnosing it was almost impossible if the bad plan was already flushed from memory. Query Store persists this history, allowing DBAs to instantly see performance regressions and force SQL Server to use a known-good past execution plan with one click.
**Example:** Forcing a good plan over a regressed plan.
**Reference:** [Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store)

---

### 95. What are Dirty Pages and Checkpoints?
**Answer:** 
**The Core Concept:**
How SQL Server handles memory-to-disk writes.

**Key Details:**
- When data is updated, it is updated in RAM (Buffer Pool), making the page "dirty". It is not immediately written to the physical database `.mdf` file.
- A "Checkpoint" is an internal background process that periodically flushes all Dirty Pages from memory to the physical disk, ensuring data integrity while maintaining high write performance.
**Example:** Internal memory management.
**Reference:** [Database Checkpoints](https://learn.microsoft.com/en-us/sql/relational-databases/logs/database-checkpoints-sql-server)

---

### 96. What is the difference between `Varchar(Max)` and `NVARCHAR(Max)`?
**Answer:** 
**The Core Concept:**
Storage for massive text fields.

**Key Details:**
- `VARCHAR(MAX)` stores up to 2GB of ASCII text (1 byte per char).
- `NVARCHAR(MAX)` stores up to 2GB of Unicode text (2 bytes per char), cutting the maximum string length in half compared to VARCHAR, but supporting global languages.
**Example:** Use `NVARCHAR` for user input, `VARCHAR` for system logs.
**Reference:** [char and varchar](https://learn.microsoft.com/en-us/sql/t-sql/data-types/char-and-varchar-transact-sql)

---

### 97. What is `sp_configure`?
**Answer:** 
**The Core Concept:**
A system stored procedure used to view or change global SQL Server configuration settings.

**Key Details:**
- Used to enable advanced options, configure maximum memory limits, change MAXDOP, or enable CLR integration. Requires the `RECONFIGURE` statement to apply changes.
**Example:** `EXEC sp_configure 'show advanced options', 1; RECONFIGURE;`
**Reference:** [sp_configure](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-configure-transact-sql)

---

### 98. Explain Database Sharding vs Partitioning.
**Answer:** 
**The Core Concept:**
Strategies for handling massive data scale.

**Key Details:**
- **Partitioning:** Splitting a large table into smaller physical files within the *same* database server.
- **Sharding:** Distributing the data across entirely *different* databases on different physical servers. Much harder to query (requires application logic to route queries), but scales infinitely.
**Example:** Partition by year. Shard by customer region.
**Reference:** [Sharding](https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding)

---

### 99. What are Graph Tables in SQL Server?
**Answer:** 
**The Core Concept:**
Native capabilities for node and edge relationships.

**Key Details:**
- Introduced in 2017, they allow you to query complex many-to-many relationships (like social networks or recommendation engines) using the `MATCH()` function, which is vastly simpler and faster than writing deeply recursive CTEs or dozens of `JOIN`s.
**Example:** `SELECT * FROM Person1 MATCH (Person1-(FriendOf)->Person2);`
**Reference:** [SQL Graph](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-architecture)

---

### 100. What is `sys.dm_db_missing_index_details`?
**Answer:** 
**The Core Concept:**
A Dynamic Management View that suggests performance improvements.

**Key Details:**
- As the Query Optimizer creates execution plans, it notes when a query would have run significantly faster if a specific index existed. This DMV stores those recommendations, allowing DBAs to query SQL Server directly to ask, "What indexes should I build to speed up the current workload?"
**Example:** Querying the DMV to find high-impact missing indexes.
**Reference:** [Missing Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-missing-index-details-transact-sql)

---
\n## Additional Depth (Architectural Focus)\n
### 101. What is the difference between a Clustered and Non-Clustered Index?
**Answer:** 
**The Core Concept:**
A Clustered Index determines the physical order of data rows in a table, meaning a table can only have one clustered index. A Non-Clustered Index is a separate structure from the data rows, containing the index key values and pointers to the actual data rows.

**Key Details:**
- Because the clustered index defines the physical storage, retrieving data via a clustered index is inherently faster as it avoids a secondary lookup.
- Non-Clustered indexes are ideal for queries that search on columns not included in the clustered index, but they incur a performance penalty (a 'Key Lookup') when retrieving non-indexed columns.

**Example:** 
`CREATE CLUSTERED INDEX IX_EmpId ON Employees(EmpId);`

**Reference:** [Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described)

---

### 102. What is a Database Transaction and what are the ACID properties?
**Answer:** 
**The Core Concept:**
A database transaction is a sequence of one or more database operations executed as a single, logical unit of work. It is governed by **ACID** properties to guarantee absolute data integrity under concurrency and crashes.

**Key Details:**
- **Atomicity**: "All or nothing." If a single statement inside the transaction fails, the entire transaction is rolled back.
- **Consistency**: Guarantees that any transaction will transition the database from one valid state to another, preserving all schemas, constraints, and triggers.
- **Isolation**: Ensures that concurrent transactions execute independently without bleeding uncommitted data into one another (controlled by Isolation Levels).
- **Durability**: Guarantees that once a transaction is committed, its changes are permanently recorded in non-volatile storage and survive system crashes.

**Example:** 
```sql
BEGIN TRANSACTION;
  UPDATE Accounts SET Balance = Balance - 100 WHERE AccountId = 1;
  UPDATE Accounts SET Balance = Balance + 100 WHERE AccountId = 2;
COMMIT TRANSACTION;
```

**Reference:** [SQL Server Transactions](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/transactions-transact-sql)

---

### 103. What is Database Normalization?
**Answer:** 
**The Core Concept:**
Database Normalization is the structured process of organizing database tables to minimize data redundancy (duplication) and prevent transactional anomalies (insertion, update, and deletion bugs).

**Key Details:**
- **First Normal Form (1NF)**: Requires atomic values (no repeating groups/multi-valued fields) and a designated primary key.
- **Second Normal Form (2NF)**: Meets 1NF, and ensures all non-key columns are fully dependent on the *entire* primary key (eliminates partial dependencies on composite keys).
- **Third Normal Form (3NF)**: Meets 2NF, and ensures non-key columns do not depend transitively on other non-key columns (eliminates transitive dependencies).
- **Trade-off**: Higher normalization reduces redundancy but increases table count, requiring complex SQL joins that can impact read throughput.

**Example:** 
```
// 1NF/2NF Violating Table: [EmployeeId, DepartmentId, DepartmentName]
// 3NF Normalized into two tables:
// Table 1: [EmployeeId, DepartmentId]
// Table 2: [DepartmentId, DepartmentName] (eliminates transitive dependency)
```

**Reference:** [Database Normalization Guide](https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description)

---

### 104. What is Database Indexing?
**Answer:** 
**The Core Concept:**
Database indexing is an optimization technique that creates specialized auxiliary data structures (typically B-Trees) to drastically accelerate record retrieval speeds, bypassing expensive full-table scans.

**Key Details:**
- **How it works**: An index stores key values sorted in a tree structure alongside pointers to their corresponding physical row locations.
- **Cost**: Accelerates reads (`SELECT`) but introduces write overhead (`INSERT`, `UPDATE`, `DELETE`) as index pages must be dynamically updated on every write.
- **Indexes in SQL**: `CREATE INDEX IX_TableName_Column ON TableName(ColumnName);`

**Reference:** [SQL Server Index Architecture](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide)

---

### 105. What is a Deadlock and how does SQL Server handle it?
**Answer:** 
**The Core Concept:**
A deadlock is a high-concurrency conflict where two or more transactions hold exclusive locks on resources the other needs to proceed, creating an infinite block cycle.

**Key Details:**
- **Detection**: SQL Server runs a background thread called the **Lock Monitor** every 5 seconds to scan the lock trees for cyclic dependencies.
- **Resolution**: Once a cycle is detected, the engine terminates one transaction (the "Deadlock Victim", usually the one with the lowest rollback cost), rolls back its changes, and throws a 1205 error to the client, allowing the other transaction to finish.
- **Prevention**: Keep transactions short, access tables in the identical order across all procedures, and build appropriate indexes to minimize lock duration.

**Example:** 
```
Transaction A: Locks Table 1 ---> Needs Table 2 (Blocked)
Transaction B: Locks Table 2 ---> Needs Table 1 (Blocked)
```

**Reference:** [Deadlock Analysis](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide#deadlocks)

---

### 106. What is the difference between an `INNER JOIN` and a `LEFT JOIN`?
**Answer:** 
**The Core Concept:**
An `INNER JOIN` returns only the records that have matching keys in both participating tables. A `LEFT JOIN` (Left Outer Join) returns *all* records from the left table, along with matching rows from the right table, filling unmatched right fields with `NULL`s.

**Key Details:**
- **INNER JOIN**: Filters out orphans. If a child row doesn't match a parent key, it is excluded from the output.
- **LEFT JOIN**: Preserves the left side. Useful for reports where you want to list all records regardless of whether they have matching details on the other side.

**Example:** 
```sql
-- Inner: Only users with active profile details
SELECT * FROM Users u INNER JOIN Profiles p ON u.Id = p.UserId;

-- Left: All users, with profiles being NULL if missing
SELECT * FROM Users u LEFT JOIN Profiles p ON u.Id = p.UserId;
```

**Reference:** [SQL Joins](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins)

---

### 107. What is Database Replication?
**Answer:** 
**The Core Concept:**
Database Replication is the automatic process of copying and distributing data from one database server (primary/master) to one or more auxiliary servers (secondaries/replicas) to maximize availability, disaster recovery, and read throughput.

**Key Details:**
- **Primary-Secondary (Master-Slave)**: Writes occur on the primary, which streams modifications to secondaries. Great for scaling massive read traffic by offloading queries to secondaries.
- **Multi-Master (Active-Active)**: Writes can occur on any node, with conflict resolution algorithms syncing changes across the entire cluster.
- **Replication latency**: The sync delay between primary writes and secondary reads, which can lead to eventual consistency read-skew bugs.

**Reference:** [SQL Server Replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication)

---

### 108. How do you prevent duplicate users with the same email?
**Answer:** 
**The Core Concept:**
Preventing duplicate emails requires a defense-in-depth approach combining strict database-level unique constraints with application-level verification checks.

**Key Details:**
- **Database Level (Mandatory)**: Create a `UNIQUE` index or constraint on the email column. This acts as the final gatekeeper, raising a duplicate key exception at the storage layer if a duplicate write attempt slips through the application.
- **Application Level**: Perform a query validation check (`SELECT EXISTS`) in the database before attempting to insert.
- **Concurrency Guard**: Wrap checking and writing in a database transaction, or use native atomic upserts (like `INSERT ... ON CONFLICT` or `upsert: true` in NoSQL).

**Example:** 
```sql
-- SQL database unique index constraint
ALTER TABLE Users ADD CONSTRAINT UQ_Users_Email UNIQUE (Email);
```

**Reference:** [Unique Constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/unique-constraints-and-check-constraints)

---

## Technical Questions

### 1. Write a T-SQL query using a Common Table Expression (CTE) and `DENSE_RANK()` to find the second highest salary.

**Example Solution:**
```sql
WITH SalaryCTE AS (
  SELECT Name, Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS Rank
  FROM Employees
)
SELECT Name, Salary 
FROM SalaryCTE 
WHERE Rank = 2;
```

### 2. Write a T-SQL query demonstrating dynamic pagination using `OFFSET` and `FETCH NEXT`.

**Example Solution:**
```sql
SELECT EmployeeId, Name, Salary
FROM Employees
ORDER BY EmployeeId
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;
```

