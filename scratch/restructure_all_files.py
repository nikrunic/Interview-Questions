import os
import re

# Custom practice/technical questions for each file path
# Each path maps to exactly 3 solved questions with full descriptions and code blocks.
# The remaining 27 challenges will be dynamically generated based on the topic.
custom_questions = {
    "backend/Authentication.md": {
        "topic": "Web Security & Authentication",
        "solved": [
            {
                "title": "Implement a JWT token generation function using `crypto` in Node.js.",
                "solution": """```javascript
const crypto = require("crypto");

function generateJWT(payload, secret, expiresInSeconds = 3600) {
  const header = { alg: "HS256", typ: "JWT" };
  const exp = Math.floor(Date.now() / 1000) + expiresInSeconds;
  const fullPayload = { ...payload, exp };

  const base64UrlEncode = (obj) => {
    return Buffer.from(JSON.stringify(obj))
      .toString("base64")
      .replace(/=/g, "")
      .replace(/\\+/g, "-")
      .replace(/\\//g, "_");
  };

  const encodedHeader = base64UrlEncode(header);
  const encodedPayload = base64UrlEncode(fullPayload);

  const signature = crypto
    .createHmac("sha256", secret)
    .update(`${encodedHeader}.${encodedPayload}`)
    .digest("base64url");

  return `${encodedHeader}.${encodedPayload}.${signature}`;
}
```"""
            },
            {
                "title": "Implement a rate-limiting middleware in Express using an in-memory sliding window.",
                "solution": """```javascript
const rateLimit = (limit = 100, windowMs = 60000) => {
  const ipRequests = new Map();

  return (req, res, next) => {
    const ip = req.ip;
    const now = Date.now();
    
    if (!ipRequests.has(ip)) {
      ipRequests.set(ip, []);
    }

    const timestamps = ipRequests.get(ip);
    const activeTimestamps = timestamps.filter(t => now - t < windowMs);
    
    if (activeTimestamps.length >= limit) {
      return res.status(429).json({ error: "Too many requests. Please try again later." });
    }

    activeTimestamps.push(now);
    ipRequests.set(ip, activeTimestamps);
    next();
  };
};
```"""
            },
            {
                "title": "Implement a PBKDF2 password hashing helper in Node.js.",
                "solution": """```javascript
const crypto = require("crypto");

function hashPassword(password) {
  const salt = crypto.randomBytes(16).toString("hex");
  const hash = crypto.pbkdf2Sync(password, salt, 1000, 64, "sha512").toString("hex");
  return { salt, hash };
}

function verifyPassword(password, salt, hash) {
  const checkHash = crypto.pbkdf2Sync(password, salt, 1000, 64, "sha512").toString("hex");
  return hash === checkHash;
}
```"""
            }
        ]
    },

    "backend/CSharp.md": {
        "topic": "C# Programming",
        "solved": [
            {
                "title": "Write an allocation-free query string parser using `ReadOnlySpan<char>`.",
                "solution": """```csharp
using System;

public class QueryParser
{
    public static void ParseQuery(string queryString)
    {
        ReadOnlySpan<char> span = queryString.AsSpan();
        if (span.StartsWith("?"))
        {
            span = span.Slice(1);
        }

        while (span.Length > 0)
        {
            int ampersandIdx = span.IndexOf('&');
            ReadOnlySpan<char> pair = ampersandIdx == -1 ? span : span.Slice(0, ampersandIdx);
            
            int eqIdx = pair.IndexOf('=');
            if (eqIdx != -1)
            {
                ReadOnlySpan<char> key = pair.Slice(0, eqIdx);
                ReadOnlySpan<char> value = pair.Slice(eqIdx + 1);
                Console.WriteLine($"Key: {key.ToString()}, Value: {value.ToString()}");
            }

            span = ampersandIdx == -1 ? ReadOnlySpan<char>.Empty : span.Slice(ampersandIdx + 1);
        }
    }
}
```"""
            },
            {
                "title": "Implement a generic Repository Pattern in C# using Entity Framework Core.",
                "solution": """```csharp
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IRepository<T> where T : class
{
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> GetByIdAsync(int id);
    Task AddAsync(T entity);
    void Update(T entity);
    void Delete(T entity);
}

public class Repository<T> : IRepository<T> where T : class
{
    protected readonly DbContext _context;
    
    public Repository(DbContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<T>> GetAllAsync() => await _context.Set<T>().ToListAsync();

    public async Task<T> GetByIdAsync(int id) => await _context.Set<T>().FindAsync(id);

    public async Task AddAsync(T entity) => await _context.Set<T>().AddAsync(entity);

    public void Update(T entity) => _context.Set<T>().Update(entity);

    public void Delete(T entity) => _context.Set<T>().Remove(entity);
}
```"""
            },
            {
                "title": "Write a Thread-Safe Singleton implementation using double-check locking in C#.",
                "solution": """```csharp
public sealed class DatabaseConnector
{
    private static DatabaseConnector _instance;
    private static readonly object _lock = new object();

    private DatabaseConnector() {}

    public static DatabaseConnector Instance
    {
        get
        {
            if (_instance == null)
            {
                lock (_lock)
                {
                    if (_instance == null)
                    {
                        _instance = new DatabaseConnector();
                    }
                }
            }
            return _instance;
        }
    }
}
```"""
            }
        ]
    },

    "backend/DotNet.md": {
        "topic": ".NET Runtime & API Development",
        "solved": [
            {
                "title": "Write an ASP.NET Core Middleware that monitors execution time and logs details.",
                "solution": """```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Threading.Tasks;

public class PerformanceLogMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<PerformanceLogMiddleware> _logger;

    public PerformanceLogMiddleware(RequestDelegate next, ILogger<PerformanceLogMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        var stopwatch = Stopwatch.StartNew();
        
        await _next(context);
        
        stopwatch.Stop();
        _logger.LogInformation(
            "Request {Method} {Path} responded {StatusCode} in {Elapsed}ms",
            context.Request.Method,
            context.Request.Path,
            context.Response.StatusCode,
            stopwatch.ElapsedMilliseconds
        );
    }
}
```"""
            },
            {
                "title": "Configure Service Lifetimes (Transient, Scoped, Singleton) in .NET 8.",
                "solution": """```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddTransient<IMyTransientService, MyTransientService>();
builder.Services.AddScoped<IMyScopedService, MyScopedService>();
builder.Services.AddSingleton<IMySingletonService, MySingletonService>();

var app = builder.Build();
app.MapGet("/", (
    IMyTransientService t1, IMyTransientService t2,
    IMyScopedService s1, IMyScopedService s2,
    IMySingletonService sig1, IMySingletonService sig2) => 
{
    return new {
        TransientMatched = t1.Guid == t2.Guid, // false
        ScopedMatched = s1.Guid == s2.Guid,   // true (same request scope)
        SingletonMatched = sig1.Guid == sig2.Guid // true (global application scope)
    };
});
app.Run();
```"""
            },
            {
                "title": "Implement a Custom Background Hosted Service in ASP.NET Core using `BackgroundService`.",
                "solution": """```csharp
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Threading;
using System.Threading.Tasks;

public class QueueProcessorService : BackgroundService
{
    private readonly ILogger<QueueProcessorService> _logger;

    public QueueProcessorService(ILogger<QueueProcessorService> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);
            await Task.Delay(5000, stoppingToken);
        }
    }
}
```"""
            }
        ]
    },

    "backend/DynamoDB.md": {
        "topic": "DynamoDB & NoSQL Modeling",
        "solved": [
            {
                "title": "Write a Node.js script to query DynamoDB using the AWS SDK v3.",
                "solution": """```javascript
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
```"""
            },
            {
                "title": "Implement Transactional Writes (TransactWriteItems) in DynamoDB.",
                "solution": """```javascript
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
```"""
            },
            {
                "title": "Write a conditional update script utilizing optimistic locking in DynamoDB.",
                "solution": """```javascript
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
```"""
            }
        ]
    },

    "backend/Hasura-GraphQL.md": {
        "topic": "GraphQL & Hasura Engines",
        "solved": [
            {
                "title": "Write a standard Hasura GraphQL query with dynamic filters and aggregate counts.",
                "solution": """```graphql
query GetProductsWithFilter($category: String!, $minPrice: numeric!) {
  products(where: {
    category: {_eq: $category},
    price: {_gte: $minPrice}
  }) {
    id
    name
    price
    category
  }
  products_aggregate(where: {
    category: {_eq: $category},
    price: {_gte: $minPrice}
  }) {
    aggregate {
      count
      avg {
        price
      }
    }
  }
}
```"""
            },
            {
                "title": "Write a custom database action payload for Hasura metadata.",
                "solution": """```yaml
- name: process_payment
  definition:
    kind: synchronous
    handler: https://payment-gateway.service/hasura-action
    forward_client_headers: true
  payload:
    arguments:
      - name: payment_method_id
        type: String!
      - name: amount
        type: Int!
    type: PaymentResponse
```"""
            },
            {
                "title": "Implement a GraphQL query combining parent-child relations with sorting.",
                "solution": """```graphql
query GetAuthorsWithRecentBooks {
  authors(order_by: { name: asc }) {
    id
    name
    books(limit: 5, order_by: { published_date: desc }) {
      id
      title
      published_date
    }
  }
}
```"""
            }
        ]
    },

    "backend/RestAPI.md": {
        "topic": "RESTful API Architecture",
        "solved": [
            {
                "title": "Implement a complete REST API controller in Node.js (Express) with standard status codes.",
                "solution": """```javascript
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
```"""
            },
            {
                "title": "Implement an API client with dynamic exponential backoff and jitter retry mechanism.",
                "solution": """```javascript
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
```"""
            },
            {
                "title": "Write a central Express error-handling middleware matching REST spec.",
                "solution": """```javascript
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
```"""
            }
        ]
    },

    "backend/MSSQL.md": {
        "topic": "Microsoft SQL Server & T-SQL",
        "solved": [
            {
                "title": "Write a T-SQL query using a Common Table Expression (CTE) and `DENSE_RANK()` to find the second highest salary.",
                "solution": """```sql
WITH SalaryCTE AS (
  SELECT Name, Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS Rank
  FROM Employees
)
SELECT Name, Salary 
FROM SalaryCTE 
WHERE Rank = 2;
```"""
            },
            {
                "title": "Write a T-SQL query demonstrating dynamic pagination using `OFFSET` and `FETCH NEXT`.",
                "solution": """```sql
SELECT EmployeeId, Name, Salary
FROM Employees
ORDER BY EmployeeId
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;
```"""
            },
            {
                "title": "Implement a TRY...CATCH transaction handler with error logging in MSSQL.",
                "solution": """```sql
BEGIN TRY
    BEGIN TRANSACTION;
        UPDATE Accounts SET Balance = Balance - 100 WHERE AccountId = 1;
        UPDATE Accounts SET Balance = Balance + 100 WHERE AccountId = 2;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;
    
    DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
    DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
    DECLARE @ErrorState INT = ERROR_STATE();
    
    RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
END CATCH;
```"""
            }
        ]
    },

    "backend/MongoDB.md": {
        "topic": "MongoDB Databases",
        "solved": [
            {
                "title": "Write a MongoDB Aggregation Pipeline query to group users by age and return the average score.",
                "solution": """```javascript
db.users.aggregate([
  { $group: { _id: "$age", avgScore: { $avg: "$score" } } },
  { $sort: { _id: 1 } }
]);
```"""
            },
            {
                "title": "Implement a robust transaction in Mongoose to transfer funds between two accounts.",
                "solution": """```javascript
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
```"""
            },
            {
                "title": "Create a Mongoose schema validation rule with custom validator and compound index.",
                "solution": """```javascript
const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    validate: {
      validator: (v) => /\\S+@\\S+\\.\\S+/.test(v),
      message: props => `\${props.value} is not a valid email!`
    }
  },
  tenantId: mongoose.Schema.Types.ObjectId
});

userSchema.index({ email: 1, tenantId: 1 }, { unique: true });
```"""
            }
        ]
    },

    "backend/MySQL.md": {
        "topic": "MySQL Database Administration",
        "solved": [
            {
                "title": "Write a SQL query to find all duplicate emails in a `Users` table.",
                "solution": """```sql
SELECT email, COUNT(email) 
FROM Users 
GROUP BY email 
HAVING COUNT(email) > 1;
```"""
            },
            {
                "title": "Write a SQL query using `INNER JOIN` to fetch the top 5 customers by total order spend.",
                "solution": """```sql
SELECT c.CustomerId, c.Name, SUM(o.TotalAmount) AS TotalSpend
FROM Customers c
INNER JOIN Orders o ON c.CustomerId = o.CustomerId
GROUP BY c.CustomerId, c.Name
ORDER BY TotalSpend DESC
LIMIT 5;
```"""
            },
            {
                "title": "Implement a MySQL transaction block using Row-Level Locking via `FOR UPDATE`.",
                "solution": """```sql
START TRANSACTION;
SELECT Balance FROM Accounts WHERE AccountId = 1 FOR UPDATE;
UPDATE Accounts SET Balance = Balance - 100 WHERE AccountId = 1;
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountId = 2;
COMMIT;
```"""
            }
        ]
    },

    "backend/NoSQL.md": {
        "topic": "NoSQL Architectures (DynamoDB & Redis)",
        "solved": [
            {
                "title": "Write a Node.js function using `@aws-sdk/client-dynamodb` to query orders within a date range.",
                "solution": """```javascript
const { QueryCommand } = require("@aws-sdk/lib-dynamodb");

async function queryOrders(ddbDocClient, userId, startDate, endDate) {
  return ddbDocClient.send(new QueryCommand({
    TableName: "Orders",
    KeyConditionExpression: "userId = :uid AND orderDate BETWEEN :start AND :end",
    ExpressionAttributeValues: {
      ":uid": userId,
      ":start": startDate,
      ":end": endDate
    }
  }));
}
```"""
            },
            {
                "title": "Implement an API sliding-window rate limiter in Node.js using Redis `INCR` and `EXPIRE`.",
                "solution": """```javascript
async function isRateLimited(redisClient, ipAddress) {
  const key = `rate:\${ipAddress}`;
  const count = await redisClient.incr(key);
  if (count === 1) {
    await redisClient.expire(key, 60);
  }
  return count > 100;
}
```"""
            },
            {
                "title": "Write a Redis client caching wrapper with TTL fallback validation.",
                "solution": """```javascript
async function getOrSetCache(redisClient, key, fetchFn, ttl = 300) {
  const cached = await redisClient.get(key);
  if (cached) return JSON.parse(cached);
  
  const freshData = await fetchFn();
  await redisClient.setEx(key, ttl, JSON.stringify(freshData));
  return freshData;
}
```"""
            }
        ]
    },

    "backend/NodeJs.md": {
        "topic": "Node.js & Express Applications",
        "solved": [
            {
                "title": "Build a basic HTTP server with the native `http` module that parses query parameters.",
                "solution": """```javascript
const http = require("http");
const url = require("url");

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ query: parsedUrl.query }));
});
server.listen(3000);
```"""
            },
            {
                "title": "Write an Express middleware that logs request execution times to the console.",
                "solution": """```javascript
const express = require("express");
const app = express();

app.use((req, res, next) => {
  const start = process.hrtime();
  res.on("finish", () => {
    const diff = process.hrtime(start);
    const ms = diff[0] * 1e3 + diff[1] * 1e-6;
    console.log(`\${req.method} \${req.url} - \${ms.toFixed(3)}ms`);
  });
  next();
});
```"""
            },
            {
                "title": "Write a Node.js clustering script using `cluster` module for multi-process scaling.",
                "solution": """```javascript
const cluster = require("cluster");
const http = require("http");
const numCPUs = require("os").cpus().length;

if (cluster.isMaster) {
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  cluster.on("exit", (worker) => {
    cluster.fork(); // Revive crashed worker
  });
} else {
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end("Hello World");
  }).listen(8000);
}
```"""
            }
        ]
    },

    "frontend/Accessibility.md": {
        "topic": "Web Accessibility (a11y)",
        "solved": [
            {
                "title": "Write an accessible Modal dialog with focus trap using Vanilla JavaScript.",
                "solution": """```javascript
function initModal(modalId, triggerId, closeId) {
  const modal = document.getElementById(modalId);
  const trigger = document.getElementById(triggerId);
  const close = document.getElementById(closeId);
  
  const focusables = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex="0"]');
  const firstFocusable = focusables[0];
  const lastFocusable = focusables[focusables.length - 1];

  trigger.addEventListener("click", () => {
    modal.setAttribute("aria-hidden", "false");
    modal.style.display = "block";
    firstFocusable.focus();
  });

  const closeModal = () => {
    modal.setAttribute("aria-hidden", "true");
    modal.style.display = "none";
    trigger.focus();
  };

  close.addEventListener("click", closeModal);

  modal.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
    if (e.key === "Tab") {
      if (e.shiftKey) {
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }
    }
  });
}
```"""
            },
            {
                "title": "Implement dynamic screen-reader announcer (aria-live) for custom status notifications.",
                "solution": """```html
<div id="announcer" class="sr-only" aria-live="polite" aria-atomic="true"></div>

<script>
  function announceStatus(message) {
    const announcer = document.getElementById("announcer");
    announcer.textContent = ""; 
    setTimeout(() => {
      announcer.textContent = message; 
    }, 100);
  }
</script>

<style>
  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }
</style>
```"""
            },
            {
                "title": "Create a accessible custom select component using ARIA roles and keyboard interaction.",
                "solution": """```html
<div class="custom-select" role="combobox" aria-expanded="false" aria-haspopup="listbox">
  <button id="select-btn" aria-controls="select-list">Select Option</button>
  <ul id="select-list" role="listbox" aria-label="Select Option" style="display: none;">
    <li role="option" tabindex="0" aria-selected="false">Option 1</li>
    <li role="option" tabindex="0" aria-selected="false">Option 2</li>
  </ul>
</div>
```"""
            }
        ]
    },

    "frontend/Angular.md": {
        "topic": "Angular Enterprise Applications",
        "solved": [
            {
                "title": "Build a custom Angular directive that highlights elements on hover with custom colors.",
                "solution": """```typescript
import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  @Input() appHighlight = 'yellow';
  @Input() defaultColor = 'transparent';

  constructor(private el: ElementRef) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.highlight(this.appHighlight);
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.highlight(this.defaultColor);
  }

  private highlight(color: string) {
    this.el.nativeElement.style.backgroundColor = color;
  }
}
```"""
            },
            {
                "title": "Implement an Angular custom reactive form validator for checking email domains.",
                "solution": """```typescript
import { AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';

export function allowedDomainsValidator(domains: string[]): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    if (!control.value) return null;
    
    const email = control.value as string;
    const domain = email.substring(email.lastIndexOf('@') + 1);
    
    return domains.includes(domain.toLowerCase()) 
      ? null 
      : { invalidDomain: { value: control.value } };
  };
}
```"""
            },
            {
                "title": "Create a reusable custom Angular Pipe implementing dynamic string truncation.",
                "solution": """```typescript
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'truncate',
  standalone: true
})
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 20, trail = '...'): string {
    if (!value) return '';
    return value.length > limit ? value.substring(0, limit) + trail : value;
  }
}
```"""
            }
        ]
    },

    "frontend/BrowserCompatibility.md": {
        "topic": "Cross-Browser Compatibility",
        "solved": [
            {
                "title": "Implement progressive enhancement feature detection for modern browser APIs.",
                "solution": """```javascript
function getFileSystemAccess() {
  if ('showOpenFilePicker' in window) {
    return window.showOpenFilePicker();
  } else {
    return new Promise((resolve) => {
      const input = document.createElement('input');
      input.type = 'file';
      input.onchange = () => resolve(input.files);
      input.click();
    });
  }
}
```"""
            },
            {
                "title": "Write CSS fallback rules using the `@supports` query block.",
                "solution": """```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

@supports not (display: grid) {
  .card-grid {
    display: flex;
    flex-wrap: wrap;
  }
  .card-grid > .card {
    flex: 1 1 250px;
    margin: 0.75rem;
  }
}
```"""
            },
            {
                "title": "Write a lightweight Promise-based polyfill for `Array.prototype.includes`.",
                "solution": """```javascript
if (!Array.prototype.includes) {
  Object.defineProperty(Array.prototype, 'includes', {
    value: function(searchElement, fromIndex) {
      if (this == null) throw new TypeError('"this" is null or not defined');
      const o = Object(this);
      const len = o.length >>> 0;
      if (len === 0) return false;
      const n = fromIndex | 0;
      let k = Math.max(n >= 0 ? n : len - Math.abs(n), 0);
      while (k < len) {
        if (o[k] === searchElement) return true;
        k++;
      }
      return false;
    }
  });
}
```"""
            }
        ]
    },

    "frontend/CSS3.md": {
        "topic": "CSS3 Grid, Flexbox, & Layouts",
        "solved": [
            {
                "title": "Build a modern, responsive 3-column Layout using CSS Grid and container queries.",
                "solution": """```css
.parent-container {
  display: grid;
  grid-template-columns: 240px 1fr 300px;
  min-height: 100vh;
  gap: 1rem;
}

@media (max-width: 1024px) {
  .parent-container {
    grid-template-columns: 1fr;
  }
}

.card-wrapper {
  container-type: inline-size;
}

@container (min-width: 500px) {
  .card {
    display: flex;
    align-items: center;
  }
}
```"""
            },
            {
                "title": "Create a premium glassmorphic UI card styled entirely in CSS3.",
                "solution": """```css
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.glass-card:hover {
  transform: translateY(-8px) scale(1.02);
}
```"""
            },
            {
                "title": "Create a CSS-only custom dynamic tooltip component with absolute anchoring.",
                "solution": """```css
.tooltip-trigger {
  position: relative;
  display: inline-block;
}

.tooltip-trigger::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 125%;
  left: 50%;
  transform: translateX(-50%) scale(0);
  background: #333;
  color: #fff;
  padding: 5px 10px;
  border-radius: 4px;
  white-space: nowrap;
  transition: transform 0.2s ease;
}

.tooltip-trigger:hover::after {
  transform: translateX(-50%) scale(1);
}
```"""
            }
        ]
    },

    "frontend/Cypress.md": {
        "topic": "E2E Testing with Cypress",
        "solved": [
            {
                "title": "Write a Cypress test asserting the user login and routing flow.",
                "solution": """```javascript
describe('User Login Flow', () => {
  it('should fill form and redirect to dashboard', () => {
    cy.visit('/login');
    cy.get('input[name="email"]').type('user@example.com');
    cy.get('input[name="password"]').type('secret123');
    cy.get('button[type="submit"]').click();
    
    cy.url().should('include', '/dashboard');
    cy.get('h1').should('contain', 'Welcome Back');
  });
});
```"""
            },
            {
                "title": "Write a Cypress test that mocks network requests using interception tools.",
                "solution": """```javascript
describe('Mock API Test', () => {
  it('should show mock products on dashboard', () => {
    cy.intercept('GET', '/api/v1/products', {
      statusCode: 200,
      body: [
        { id: 1, name: 'Mock Product A', price: 99.99 },
        { id: 2, name: 'Mock Product B', price: 49.99 }
      ]
    }).as('getProducts');

    cy.visit('/dashboard');
    cy.wait('@getProducts');

    cy.get('.product-card').should('have.length', 2);
    cy.get('.product-card').first().should('contain', 'Mock Product A');
  });
});
```"""
            },
            {
                "title": "Write a Cypress custom command helper to bypass login forms by stubbing JWT cookies.",
                "solution": """```javascript
Cypress.Commands.add('loginViaToken', (token) => {
  cy.setCookie('auth_token', token);
  cy.visit('/dashboard');
});

// Usage in test
it('should load dashboard instantly', () => {
  cy.loginViaToken('mock-jwt-token-123');
  cy.get('.profile').should('exist');
});
```"""
            }
        ]
    },

    "frontend/HTML.md": {
        "topic": "Semantic HTML5 & DOM",
        "solved": [
            {
                "title": "Design a fully semantic, SEO-friendly HTML5 article structure.",
                "solution": """```html
<article itemscope itemtype="https://schema.org/BlogPosting">
  <header>
    <h1 itemprop="headline">Deep Dive into CSS Container Queries</h1>
    <p>Published on <time itemprop="datePublished" datetime="2026-05-28">May 28, 2026</time></p>
  </header>
  
  <section itemprop="articleBody">
    <p>Container queries allow developers to style elements based on the size of their parent...</p>
    <aside>
      <h4>Tip</h4>
      <p>Always declare <code>container-type: inline-size</code> on the parent.</p>
    </aside>
  </section>
  
  <footer>
    <address>Written by <span itemprop="author">Nik Runic</span></address>
  </footer>
</article>
```"""
            },
            {
                "title": "Implement progressive enhancement video fallback elements in HTML5.",
                "solution": """```html
<video controls width="640" height="360" poster="/assets/hero-poster.jpg">
  <source src="/assets/intro.webm" type="video/webm">
  <source src="/assets/intro.mp4" type="video/mp4">
  <track src="/assets/captions_en.vtt" kind="captions" srclang="en" label="English">
  <p>Your browser does not support the video tag. 
     You can <a href="/assets/intro.mp4">download the video file</a> instead.</p>
</video>
```"""
            },
            {
                "title": "Design an accessible, responsive HTML5 data table with row and column scopes.",
                "solution": """```html
<table>
  <caption>Company Quarterly Sales (2026)</caption>
  <thead>
    <tr>
      <th scope="col">Quarter</th>
      <th scope="col">Sales</th>
      <th scope="col">Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Q1</th>
      <td>$12,000</td>
      <td>$10,000</td>
    </tr>
  </tbody>
</table>
```"""
            }
        ]
    },

    "frontend/Javascript.md": {
        "topic": "JavaScript Core Mechanics",
        "solved": [
            {
                "title": "Write a custom implementation of `Array.prototype.map()`.",
                "solution": """```javascript
Array.prototype.myMap = function(callback) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};
```"""
            },
            {
                "title": "Implement a debounce helper function in JavaScript.",
                "solution": """```javascript
function debounce(func, delay) {
  let timerId;
  return function(...args) {
    clearTimeout(timerId);
    timerId = setTimeout(() => func.apply(this, args), delay);
  };
}
```"""
            },
            {
                "title": "Write a function to check if a string is a palindrome.",
                "solution": """```javascript
function isPalindrome(str) {
  const clean = str.toLowerCase().replace(/[^a-z0-9]/g, "");
  return clean === clean.split("").reverse().join("");
}
```"""
            }
        ]
    },

    "frontend/Jest.md": {
        "topic": "Unit Testing with Jest",
        "solved": [
            {
                "title": "Write a Jest unit test to mock a fetch callback helper.",
                "solution": """```javascript
const fetchProducts = async (fetcherFn) => {
  const data = await fetcherFn("/products");
  return data.map(p => p.name.toUpperCase());
};

// Jest Test
test('should fetch products and format names', async () => {
  const mockFetcher = jest.fn().mockResolvedValue([
    { name: "laptop" },
    { name: "phone" }
  ]);
  
  const result = await fetchProducts(mockFetcher);
  
  expect(mockFetcher).toHaveBeenCalledWith("/products");
  expect(result).toEqual(["LAPTOP", "PHONE"]);
});
```"""
            },
            {
                "title": "Write a Jest test checking promise resolution and error rejections.",
                "solution": """```javascript
function loadUser(id) {
  if (id <= 0) return Promise.reject(new Error("Invalid ID"));
  return Promise.resolve({ id, name: "Nik" });
}

// Jest Tests
describe('loadUser API', () => {
  test('resolves data on valid ID', async () => {
    await expect(loadUser(1)).resolves.toEqual({ id: 1, name: "Nik" });
  });

  test('rejects with error on invalid ID', async () => {
    await expect(loadUser(-1)).rejects.toThrow("Invalid ID");
  });
});
```"""
            },
            {
                "title": "Write a Jest test simulating and checking timers via `jest.useFakeTimers()`.",
                "solution": """```javascript
function delayCallback(callback) {
  setTimeout(() => callback("done"), 1000);
}

test('should call callback after timeout', () => {
  jest.useFakeTimers();
  const mockCb = jest.fn();
  delayCallback(mockCb);
  
  expect(mockCb).not.toBeCalled();
  jest.advanceTimersByTime(1000);
  expect(mockCb).toBeCalledWith("done");
});
```"""
            }
        ]
    },

    "frontend/LESS.md": {
        "topic": "LESS CSS Preprocessing",
        "solved": [
            {
                "title": "Implement custom responsive grid mixins in LESS.",
                "solution": """```less
.make-grid(@cols; @gutter) {
  display: flex;
  flex-wrap: wrap;
  margin-left: -(@gutter / 2);
  margin-right: -(@gutter / 2);
  
  .col {
    flex: 0 0 (100% / @cols);
    max-width: (100% / @cols);
    padding-left: (@gutter / 2);
    padding-right: (@gutter / 2);
  }
}

// Usage
.gallery {
  .make-grid(4, 20px);
}
```"""
            },
            {
                "title": "Build a dark/light theme switching variables structure in LESS.",
                "solution": """```less
@theme-dark: {
  @bg: #121212;
  @text: #ffffff;
};
@theme-light: {
  @bg: #ffffff;
  @text: #121212;
};

.apply-theme(@theme) {
  @theme();
  background-color: @bg;
  color: @text;
}

body.dark {
  .apply-theme(@theme-dark);
}

body.light {
  .apply-theme(@theme-light);
}
```"""
            },
            {
                "title": "Write a LESS recursive loop to generate helper padding classes.",
                "solution": """```less
.generate-paddings(@index) when (@index > 0) {
  .generate-paddings((@index - 5)); // Decr index
  .p-@{index} {
    padding: ~"@{index}px";
  }
}
.generate-paddings(25); // Calls loop
```"""
            }
        ]
    },

    "frontend/Nextjs.md": {
        "topic": "Next.js Framework",
        "solved": [
            {
                "title": "Build an dynamic asynchronous App Router page in Next.js.",
                "solution": """```typescript
import { Suspense } from "react";

interface Product {
  id: number;
  name: string;
}

async function ProductList() {
  const res = await fetch("https://api.example.com/products", { cache: "no-store" });
  const products: Product[] = await res.json();
  
  return (
    <ul>
      {products.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
  );
}

export default function Page() {
  return (
    <main>
      <h1>Products</h1>
      <Suspense fallback={<p>Loading products...</p>}>
        <ProductList />
      </Suspense>
    </main>
  );
}
```"""
            },
            {
                "title": "Implement an App Router API handler utilizing dynamic parameters and route protection.",
                "solution": """```typescript
import { NextResponse } from "next/server";

export async function GET(request: Request, { params }: { params: { id: string } }) {
  const authHeader = request.headers.get("authorization");
  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const userId = params.id;
  return NextResponse.json({ id: userId, name: "John Doe" });
}
```"""
            },
            {
                "title": "Implement standard middleware in Next.js (App Router) managing redirect rewrites.",
                "solution": """```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}
```"""
            }
        ]
    },

    "frontend/ReactArchiteture.md": {
        "topic": "React Architecture & Optimization",
        "solved": [
            {
                "title": "Implement a performant, memoized context selector utility.",
                "solution": """```javascript
import React, { createContext, useContext, useState, useMemo } from "react";

const StateContext = createContext(null);

export function AppStateProvider({ children }) {
  const [user, setUser] = useState({ name: "Nik", role: "admin" });
  const [theme, setTheme] = useState("dark");

  const value = useMemo(() => ({ user, setUser, theme, setTheme }), [user, theme]);

  return <StateContext.Provider value={value}>{children}</StateContext.Provider>;
}

export function useUser() {
  const context = useContext(StateContext);
  if (!context) throw new Error("useUser must be used within AppStateProvider");
  return useMemo(() => [context.user, context.setUser], [context.user, context.setUser]);
}
```"""
            },
            {
                "title": "Implement a high-performance Dynamic Grid virtualization window.",
                "solution": """```javascript
import React, { useState } from "react";

export function VirtualizedList({ items, itemHeight, viewportHeight }) {
  const [scrollTop, setScrollTop] = useState(0);

  const startIndex = Math.floor(scrollTop / itemHeight);
  const endIndex = Math.min(items.length - 1, Math.floor((scrollTop + viewportHeight) / itemHeight));

  const visibleItems = items.slice(startIndex, endIndex + 1);
  const totalHeight = items.length * itemHeight;
  const offsetY = startIndex * itemHeight;

  return (
    <div 
      onScroll={(e) => setScrollTop(e.currentTarget.scrollTop)}
      style={{ height: viewportHeight, overflowY: "auto", position: "relative" }}
    >
      <div style={{ height: totalHeight, width: "100%", position: "absolute" }}>
        <div style={{ transform: `translateY(\${offsetY}px)`, position: "absolute", left: 0, right: 0 }}>
          {visibleItems.map((item, idx) => (
            <div key={startIndex + idx} style={{ height: itemHeight }}>
              {item}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```"""
            },
            {
                "title": "Implement an asynchronous module lazy loader using `React.lazy` and `Suspense` boundary error handling.",
                "solution": """```javascript
import React, { Suspense } from "react";

const HeavyComponent = React.lazy(() => import("./HeavyComponent"));

export function App() {
  return (
    <ErrorBoundary fallback={<div>Failed to load module.</div>}>
      <Suspense fallback={<div>Loading component...</div>}>
        <HeavyComponent />
      </Suspense>
    </ErrorBoundary>
  );
}
```"""
            }
        ]
    },

    "frontend/Reactjs.md": {
        "topic": "React.js State & Components",
        "solved": [
            {
                "title": "Write a custom React hook `useFetch` to handle API requests and caching.",
                "solution": """```javascript
import { useState, useEffect } from "react";

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let active = true;
    fetch(url)
      .then(res => res.json())
      .then(data => {
        if (active) {
          setData(data);
          setLoading(false);
        }
      });
    return () => { active = false; };
  }, [url]);

  return { data, loading };
}
```"""
            },
            {
                "title": "Implement a search component with debounced text input using standard state hook.",
                "solution": """```javascript
import React, { useState, useEffect } from "react";

function SearchBox({ onSearch }) {
  const [query, setQuery] = useState("");

  useEffect(() => {
    const handler = setTimeout(() => {
      onSearch(query);
    }, 300);
    return () => clearTimeout(handler);
  }, [query, onSearch]);

  return <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search..." />;
}
```"""
            },
            {
                "title": "Create a ThemeContext and ThemeProvider to toggle dark/light CSS variables.",
                "solution": """```javascript
import React, { createContext, useState, useEffect } from "react";

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
  }, [theme]);

  const toggleTheme = () => setTheme(prev => prev === "light" ? "dark" : "light");

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
```"""
            }
        ]
    },

    "frontend/Redux.md": {
        "topic": "Redux State Management",
        "solved": [
            {
                "title": "Implement a complete Redux Toolkit slice containing async Thunks.",
                "solution": """```typescript
import { createSlice, createAsyncThunk, PayloadAction } from "@reduxjs/toolkit";

export const fetchUser = createAsyncThunk("user/fetch", async (id: number) => {
  const res = await fetch(`/api/user/\${id}`);
  return (await res.json()) as { name: string; email: string };
});

interface UserState {
  name: string;
  loading: boolean;
  error: string | null;
}

const initialState: UserState = { name: "", loading: false, error: null };

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => { state.loading = true; })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.loading = false;
        state.name = action.payload.name;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || "Failed to fetch";
      });
  }
});

export default userSlice.reducer;
```"""
            },
            {
                "title": "Implement a Redux store middleware that catches and aggregates error payloads.",
                "solution": """```javascript
const errorLoggerMiddleware = store => next => action => {
  if (action.type.endsWith('/rejected')) {
    console.error(`Action \${action.type} failed:`, action.error || action.payload);
  }
  return next(action);
};
```"""
            },
            {
                "title": "Create a fully functional custom Redux store implementation from scratch.",
                "solution": """```javascript
function createStore(reducer, initialState) {
  let state = initialState;
  const listeners = [];

  const getState = () => state;

  const dispatch = (action) => {
    state = reducer(state, action);
    listeners.forEach(listener => listener());
  };

  const subscribe = (listener) => {
    listeners.push(listener);
    return () => {
      const idx = listeners.indexOf(listener);
      if (idx !== -1) listeners.splice(idx, 1);
    };
  };

  return { getState, dispatch, subscribe };
}
```"""
            }
        ]
    },

    "frontend/ResponsiveDesign.md": {
        "topic": "Responsive Web Design",
        "solved": [
            {
                "title": "Write fluid responsive font structures using the CSS `clamp` function.",
                "solution": """```css
:root {
  --font-body: clamp(1rem, 1.2vw + 0.75rem, 1.5rem);
  --font-header: clamp(2rem, 3vw + 1.5rem, 4rem);
}

body {
  font-size: var(--font-body);
}

h1 {
  font-size: var(--font-header);
}
```"""
            },
            {
                "title": "Design a dynamic layout component that switches from stack to row via CSS Container Queries.",
                "solution": """```css
.card-container {
  container-type: inline-size;
}

.product-card {
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

@container (min-width: 450px) {
  .product-card {
    flex-direction: row;
    align-items: center;
    gap: 1.5rem;
  }
}
```"""
            },
            {
                "title": "Implement an aspect-ratio-friendly responsive gallery item layout.",
                "solution": """```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 10px;
}

.gallery-item {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}
```"""
            }
        ]
    },

    "frontend/SCSS.md": {
        "topic": "Sass/SCSS Styling Systems",
        "solved": [
            {
                "title": "Design responsive media-query breakpoints using SCSS maps and `@mixin` structures.",
                "solution": """```scss
$breakpoints: (
  "sm": 576px,
  "md": 768px,
  "lg": 992px,
  "xl": 1200px
);

@mixin respond-to($size) {
  @if map-has-key($breakpoints, $size) {
    @media (min-width: map-get($breakpoints, $size)) {
      @content;
    }
  } @else {
    @warn "Breakpoint \${size} not found.";
  }
}

.sidebar {
  width: 100%;
  @include respond-to("md") {
    width: 250px;
  }
}
```"""
            },
            {
                "title": "Build color scheme maps utilizing `@each` loop directives to auto-generate utilities.",
                "solution": """```scss
$colors: (
  "primary": #3b82f6,
  "success": #10b981,
  "danger": #ef4444
);

@each $name, $value in $colors {
  .bg-#{$name} {
    background-color: $value;
  }
  .text-#{$name} {
    color: $value;
  }
}
```"""
            },
            {
                "title": "Create a modular dark/light dynamic theme mapping generator inside SCSS.",
                "solution": """```scss
$themes: (
  light: (
    bg: #ffffff,
    text: #333333
  ),
  dark: (
    bg: #121212,
    text: #ffffff
  )
);

@mixin theme-styles {
  @each $theme, $map in $themes {
    .theme-#{$theme} & {
      background: map-get($map, bg);
      color: map-get($map, text);
    }
  }
}
```"""
            }
        ]
    },

    "frontend/TailwindCSS.md": {
        "topic": "Tailwind CSS Layouts",
        "solved": [
            {
                "title": "Build a responsive card using Tailwind CSS utility classes.",
                "solution": """```html
<div class="max-w-md mx-auto bg-white dark:bg-slate-800 rounded-xl shadow-md overflow-hidden md:max-w-2xl transition duration-300 hover:scale-105">
  <div class="md:flex">
    <div class="md:shrink-0">
      <img class="h-48 w-full object-cover md:h-full md:w-48" src="/assets/card-hero.jpg" alt="Hero">
    </div>
    <div class="p-8">
      <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Tailwind V3</div>
      <h3 class="block mt-1 text-lg leading-tight font-medium text-black dark:text-white">Responsive Cards</h3>
      <p class="mt-2 text-slate-500 dark:text-slate-400">Learn utility-first responsive styling cleanly.</p>
    </div>
  </div>
</div>
```"""
            },
            {
                "title": "Configure a custom theme color scale in `tailwind.config.js`.",
                "solution": """```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f9ff',
          500: '#0ea5e9',
          900: '#0c4a6e',
        }
      }
    }
  }
}
```"""
            },
            {
                "title": "Build a grid system showing custom column widths using Tailwind's layout engines.",
                "solution": """```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 p-6">
  <div class="col-span-1 bg-blue-100 p-4">Sidebar</div>
  <div class="col-span-2 bg-green-100 p-4">Main Content Area</div>
</div>
```"""
            }
        ]
    },

    "frontend/Typscript.md": {
        "topic": "TypeScript Type Systems",
        "solved": [
            {
                "title": "Implement a custom `Omit<T, K>` utility type using mapped and conditional types.",
                "solution": """```typescript
type MyOmit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;

// Example
interface User {
  id: number;
  name: string;
  email: string;
}
type PublicUser = MyOmit<User, 'email'>;
```"""
            },
            {
                "title": "Create a type-safe API response wrapper using Generics.",
                "solution": """```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

async function apiCall<T>(url: string): Promise<ApiResponse<T>> {
  const res = await fetch(url);
  return res.json();
}
```"""
            },
            {
                "title": "Define a custom `DeepPartial<T>` helper mapping deep optional nodes.",
                "solution": """```typescript
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

// Example
interface Config {
  db: { host: string; port: number };
}
const myConfig: DeepPartial<Config> = { db: { port: 5432 } };
```"""
            }
        ]
    },

    "frontend/Vuejs.md": {
        "topic": "Vue.js Reactive Framework",
        "solved": [
            {
                "title": "Create a custom reusable Composition API helper hook `useLocalStorage` in Vue 3.",
                "solution": """```typescript
import { ref, watch, Ref } from "vue";

export function useLocalStorage<T>(key: string, defaultValue: T): Ref<T> {
  const storedValue = localStorage.getItem(key);
  const data = ref<T>(storedValue ? JSON.parse(storedValue) : defaultValue) as Ref<T>;

  watch(data, (newValue) => {
    localStorage.setItem(key, JSON.stringify(newValue));
  }, { deep: true });

  return data;
}
```"""
            },
            {
                "title": "Build a debounced search input component using `<script setup>` in Vue 3.",
                "solution": """```html
<script setup lang="ts">
import { ref, watch } from "vue";

const search = ref("");
const debouncedSearch = ref("");
let timeoutId: ReturnType<typeof setTimeout>;

watch(search, (newVal) => {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    debouncedSearch.value = newVal;
  }, 300);
});
</script>

<template>
  <div class="search-box">
    <input v-model="search" placeholder="Type to search..." class="border p-2 rounded" />
    <p>Searching for: {{ debouncedSearch }}</p>
  </div>
</template>
```"""
            },
            {
                "title": "Create a Vue 3 custom directive managing element auto-focus behaviors.",
                "solution": """```typescript
const vFocus = {
  mounted: (el: HTMLElement) => {
    el.focus();
  }
};
// Use as: <input v-focus />
```"""
            }
        ]
    },

    "frontend/WebPerformance.md": {
        "topic": "Web Performance Tuning",
        "solved": [
            {
                "title": "Write an image lazy-loading script utilizing the dynamic browser IntersectionObserver.",
                "solution": """```javascript
function lazyLoadImages() {
  const images = document.querySelectorAll("img[data-src]");
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute("data-src");
        obs.unobserve(img);
      }
    });
  });

  images.forEach(img => observer.observe(img));
}
```"""
            },
            {
                "title": "Dynamically import a heavy external library on user interaction to improve Largest Contentful Paint (LCP).",
                "solution": """```javascript
const button = document.getElementById("chart-btn");

button.addEventListener("click", async () => {
  const { default: Chart } = await import("chart.js/auto");
  
  const ctx = document.getElementById("myChart");
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue'],
      datasets: [{ data: [12, 19] }]
    }
  });
});
```"""
            },
            {
                "title": "Implement standard client resource prefetching for future dynamic navigations.",
                "solution": """```javascript
function prefetchUrl(url) {
  const link = document.createElement("link");
  link.rel = "prefetch";
  link.href = url;
  document.head.appendChild(link);
}
```"""
            }
        ]
    },

    "frontend/Webpack.md": {
        "topic": "Webpack & Build Tooling",
        "solved": [
            {
                "title": "Build a basic webpack.config.js handling TypeScript and CSS bundle extraction.",
                "solution": """```javascript
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: "./src/index.ts",
  module: {
    rules: [
      { test: /\\.tsx?$/, use: "ts-loader", exclude: /node_modules/ },
      { test: /\\.css$/, use: [MiniCssExtractPlugin.loader, "css-loader"] }
    ]
  },
  resolve: { extensions: [".tsx", ".ts", ".js"] },
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
    clean: true
  },
  plugins: [new MiniCssExtractPlugin()]
};
```"""
            },
            {
                "title": "Configure bundle code-splitting via standard `optimization.splitChunks` blocks.",
                "solution": """```javascript
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\\\/]node_modules[\\\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
      },
    },
  },
};
```"""
            },
            {
                "title": "Configure a Webpack compression compiler plugin for GZIP bundle assets.",
                "solution": """```javascript
const CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
  plugins: [
    new CompressionPlugin({
      algorithm: "gzip",
      test: /\\.js$|\\.css$|\\.html$/,
      threshold: 10240,
      minRatio: 0.8
    })
  ]
};
```"""
            }
        ]
    },

    "devops/CICD.md": {
        "topic": "CI/CD & DevOps Automation",
        "solved": [
            {
                "title": "Write a YAML workflow for GitHub Actions executing Jest unit testing on PR.",
                "solution": """```yaml
name: Node CI Pipeline

on:
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Run Jest Tests
        run: npm test
```"""
            },
            {
                "title": "Build a highly performant multi-stage Dockerfile for nesting Node.js environments.",
                "solution": """```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=builder /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```"""
            },
            {
                "title": "Write a multi-stage Dockerfile utilizing target build parameters.",
                "solution": """```dockerfile
FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./

FROM base AS dev
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]

FROM base AS prod
RUN npm ci --only=production
COPY . .
USER node
CMD ["node", "server.js"]
```"""
            }
        ]
    },

    "devops/CloudPlatforms.md": {
        "topic": "Cloud Platforms & Infrastructure",
        "solved": [
            {
                "title": "Build a basic Terraform file launching static hosting pools inside AWS S3 buckets.",
                "solution": """```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "static_site" {
  bucket = "my-awesome-interview-site-2026"
}

resource "aws_s3_bucket_website_configuration" "static_config" {
  bucket = aws_s3_bucket.static_site.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}
```"""
            },
            {
                "title": "Configure a modern, secure reverse-proxy redirect using Nginx config templates.",
                "solution": """```nginx
server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```"""
            },
            {
                "title": "Write an Ansible playbook managing package updates on Ubuntu platforms.",
                "solution": """```yaml
- name: Update system packages
  hosts: webservers
  become: yes
  tasks:
    - name: Update apt cache and upgrade packages
      apt:
        update_cache: yes
        upgrade: dist
```"""
            }
        ]
    },

    "devops/Git.md": {
        "topic": "Git & Version Control",
        "solved": [
            {
                "title": "Write the Git commands to resolve a merge conflict in a file step-by-step.",
                "solution": """```bash
# 1. Start the merge that creates a conflict
git merge feature-branch

# 2. Check which files are in conflict
git status

# 3. Open the conflicted file and resolve markers manually
# <<<<<<< HEAD
# const url = "production-url";
# =======
# const url = "staging-url";
# >>>>>>> feature-branch

# 4. Add the resolved file
git add resolved_file.js

# 5. Complete the merge commit
git commit -m "merge: resolve conflict on API endpoints"
```"""
            },
            {
                "title": "Write Git commands to squash the last 3 local commits before pushing.",
                "solution": """```bash
# Start an interactive rebase for the last 3 commits
git rebase -i HEAD~3

# In the interactive editor, keep the first commit as "pick" and change the next two to "squash" or "s":
# pick a1b2c3d Commit number 1
# squash e5f6g7h Commit number 2
# squash i9j0k1l Commit number 3

# Save the new squashed message and verify using:
git log --oneline
```"""
            },
            {
                "title": "Write Git commands to rollback a pushed commit without rewriting Git history.",
                "solution": """```bash
# Revert the specific commit using git revert (creates a new commit reverting changes)
git revert a1b2c3d4

# Push the revert commit to remote safely
git push origin main
```"""
            }
        ]
    }
}

# 27 generic but highly relevant, professional challenge templates that we fill with the topic
challenge_templates = [
    "Design a high-throughput, fault-tolerant system leveraging key principles of {topic}.",
    "Write a custom utility to validate input schemas and sanitize payloads in {topic}.",
    "Implement a comprehensive error-boundary and logging module for a {topic} application.",
    "Optimize memory consumption and execution hot-paths under high load in {topic}.",
    "Write an automated unit testing suite targeting complex race-conditions in {topic}.",
    "Create a localized internationalization (i18n) helper integrated with {topic}.",
    "Build a secure token-based authentication handshake flow within {topic}.",
    "Design a distributed caching and invalidation strategy for heavy {topic} operations.",
    "Create a CLI tool to automate scaffolding and deployment of {topic} configurations.",
    "Implement a real-time event-driven pub/sub handler using {topic} event structures.",
    "Draft an architectural decision record (ADR) comparing {topic} with its primary competitors.",
    "Create a mock framework to isolate and test external integrations in {topic}.",
    "Write a custom telemetry wrapper to output {topic} performance metrics to Prometheus/Grafana.",
    "Design a zero-downtime blue-green roll-out plan for a database or service utilizing {topic}.",
    "Implement a circuit-breaker pattern to gracefully degrade service during {topic} failures.",
    "Write an automated script to detect memory leaks and unhandled promise rejections in {topic}.",
    "Build a user-friendly audit log tracking all state mutations and access events in {topic}.",
    "Design an API gateway integration mapping REST inputs to {topic} data layers.",
    "Implement a rate-limiter with custom sliding-window configurations in {topic}.",
    "Create a backup and recovery automated script for preserving {topic} state repositories.",
    "Design a microservice boundary that encapsulates {topic} logic without tight coupling.",
    "Build a role-based access control (RBAC) middleware verifying permissions on {topic}.",
    "Write an optimized compiler or parser configuration to bundle {topic} files for web browsers.",
    "Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in {topic}.",
    "Create an automated health-check endpoint monitor checking {topic} connection integrity.",
    "Implement a secure CORS and CSP policy wrapper for endpoints exposing {topic}.",
    "Refactor a legacy monolithic module into modern, modular ES modules using {topic}."
]

def process_all_files():
    directories = ["frontend", "backend", "devops"]
    files_processed = 0

    for directory in directories:
        if not os.path.exists(directory):
            continue
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                if not filename.endswith(".md"):
                    continue
                
                filepath = os.path.join(root, filename)
                # Skip js-practical.md since it is a purely practical code file with a different purpose
                if filename == "js-practical.md":
                    continue
                    
                # Read file content
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    
                # Clean up all literal backslash-n sequences if they got written as text in previous turns
                content = content.replace("\\n", "\n")
                    
                # Find all Q&A patterns (e.g. ### [number].)
                questions = re.findall(r"^###\s+(\d+)\.", content, re.MULTILINE)
                if not questions:
                    # Skip reference sheets with no questions
                    continue
                    
                total_questions = len(questions)
                print(f"Restructuring Q&A in {filepath} ({total_questions} questions)...")
                
                # Find each question block in order.
                q_matches = list(re.finditer(r"^###\s+\d+\.", content, re.MULTILINE))
                
                if not q_matches:
                    continue
                    
                # Header text before the first question
                header_text = content[:q_matches[0].start()]
                
                # Clean up any existing H2 difficulty headings from header_text
                header_lines = header_text.splitlines()
                cleaned_header_lines = []
                for line in header_lines:
                    if line.strip().startswith("##"):
                        lower_line = line.lower()
                        if any(x in lower_line for x in ["basic", "medium", "hard", "easy", "intermediate", "expert", "depth", "additional", "practice", "technical"]):
                            continue
                    cleaned_header_lines.append(line)
                header_text = "\n".join(cleaned_header_lines) + "\n"
                
                # Collect all question bodies
                q_bodies = []
                for i in range(len(q_matches)):
                    start = q_matches[i].start()
                    end = q_matches[i+1].start() if i + 1 < len(q_matches) else len(content)
                    q_body = content[start:end]
                    
                    # Clean up any trailing horizontal rules, headings or whitespace within/after question body
                    if i == len(q_matches) - 1:
                        lines = q_body.splitlines()
                        cleaned_lines = []
                        for line in lines:
                            if line.strip().startswith("##"):
                                lower_line = line.lower()
                                if any(x in lower_line for x in ["basic", "medium", "hard", "easy", "intermediate", "expert", "depth", "additional", "practice", "technical"]):
                                    break
                            cleaned_lines.append(line)
                        q_body = "\n".join(cleaned_lines)
                    q_bodies.append(q_body.strip())
                
                # Determine question indices for partitioning
                if total_questions <= 3:
                    b_idx, i_idx = 1, 2
                elif total_questions <= 6:
                    b_idx, i_idx = 2, 4
                elif total_questions <= 25:
                    b_idx = total_questions // 3
                    i_idx = b_idx * 2
                elif total_questions <= 60:
                    b_idx = 15
                    i_idx = 35
                else:
                    b_idx = 20
                    i_idx = 50
                    
                # Build the new content using standard newlines
                new_content = header_text.strip() + "\n\n"
                
                # 1. Basic section
                new_content += "## Basic Questions\n\n"
                for qb in q_bodies[:b_idx]:
                    new_content += qb + "\n\n---\n\n"
                    
                # 2. Intermediate section
                new_content += "## Intermediate Questions\n\n"
                for qb in q_bodies[b_idx:i_idx]:
                    new_content += qb + "\n\n---\n\n"
                    
                # 3. Expert section
                new_content += "## Expert Questions\n\n"
                for qb in q_bodies[i_idx:]:
                    new_content += qb + "\n\n---\n\n"
                    
                # Retrieve customization for this file
                meta = custom_questions.get(filepath)
                if not meta:
                    # Fallback meta if not explicitly hardcoded
                    is_frontend = "frontend" in filepath
                    meta = {
                        "topic": os.path.basename(filepath).replace(".md", "") + " Concepts",
                        "solved": [
                            {
                                "title": "Explain how to debug a failing application in this technology.",
                                "solution": "**Answer:**\nCheck local logs, run stepping debuggers, and isolate network requests.\n\n**Example:**\n`npm run debug`"
                            },
                            {
                                "title": "What are the common performance optimization steps for this technology?",
                                "solution": "**Answer:**\nLeverage caching, optimize asset bundles, and minimize synchronous parsing blocking."
                            },
                            {
                                "title": "Design a secure deployment schema mapping to key production environments.",
                                "solution": "**Answer:**\nUse environment variables for credentials and enforce HTTPS/SSL headers."
                            }
                        ]
                    }
                
                topic = meta["topic"]
                is_frontend = "frontend" in filepath
                sec_title = "Practice Questions" if is_frontend else "Technical Questions"
                
                # Build the Practice/Technical Questions section at the end
                new_content += f"## {sec_title}\n\n"
                
                # 1. Append the 3 solved questions
                for idx, sq in enumerate(meta["solved"], 1):
                    new_content += f"### {idx}. {sq['title']}\n\n**Example Solution:**\n{sq['solution']}\n\n"
                
                # 2. Append the 27 dynamic challenges for self-practice to reach exactly 30 questions
                for idx, template in enumerate(challenge_templates, 4):
                    challenge = template.format(topic=topic)
                    new_content += f"### {idx}. [Self-Practice] {challenge}\n\n*(Challenge question for self-study and practical project implementation.)*\n\n"
                
                # Write back to file with native newlines
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                    
                files_processed += 1

    print(f"Successfully completed processing of {files_processed} files.")

if __name__ == "__main__":
    process_all_files()
