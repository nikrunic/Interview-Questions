# Cloud Platforms (AWS, GCP, Azure) Interview Questions

This document contains interview questions focused on cloud computing, infrastructure as a service, and cloud platforms like AWS and GCP.

## Basic Questions

### 1. What is Cloud Computing?
**Answer:** 
**The Core Concept:**
Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing.

**Key Details:**
- Instead of buying, owning, and maintaining physical data centers, you access technology services on an as-needed basis from a cloud provider.
- It provides elasticity, scalability, and high availability.

**Example:** Hosting a database on AWS RDS instead of a local server machine.

**Reference:** [AWS Cloud Computing](https://aws.amazon.com/what-is-cloud-computing/)

---

---

---

### 2. What is AWS S3?
**Answer:** 
**The Core Concept:**
Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.

**Key Details:**
- It is commonly used for hosting static websites, storing user uploads (like images/videos), and keeping backups.
- Data is stored as objects within resources called "buckets".

**Example:** Storing profile pictures for a social media app.

**Reference:** [AWS S3](https://aws.amazon.com/s3/)

---

---

## Intermediate Questions

---

## Intermediate Questions

### 3. What is the difference between IaaS, PaaS, and SaaS?
**Answer:** 
**The Core Concept:**
These are the three main models of cloud computing representing different levels of abstraction.

**Key Details:**
- IaaS (Infrastructure as a Service) provides raw networking, storage, and computers (e.g., AWS EC2).
- PaaS (Platform as a Service) removes the need for organizations to manage the underlying infrastructure, focusing on deployment (e.g., Heroku, AWS Elastic Beanstalk).
- SaaS (Software as a Service) provides a completed product that is run and managed by the service provider (e.g., Gmail).

**Example:** EC2 (IaaS), Google App Engine (PaaS), Google Workspace (SaaS).

**Reference:** [Azure Cloud Models](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-iaas-paas-saas)

---

## Additional Depth (Architectural Focus)


---

---

### 4. What is the principle of least privilege in IAM?
**Answer:** 
**The Core Concept:**
The principle of least privilege dictates that a user, application, or service should only be granted the minimum permissions necessary to perform its intended function. It is a foundational security concept in cloud environments like AWS (IAM) and GCP (Cloud IAM).

**Key Details:**
- By restricting access, the blast radius of a compromised credential or a misconfigured application is severely limited.
- Implementing this requires using fine-grained access control policies, avoiding wildcard permissions (`*`), and regularly auditing roles using tools like AWS IAM Access Analyzer.

**Example:** 
`Allow `s3:GetObject` on `arn:aws:s3:::my-bucket/*` instead of `s3:*` on all resources.`

**Reference:** [Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

---

---

## Expert Questions

## Technical Questions

---

## Expert Questions

### 1. Build a basic Terraform file launching static hosting pools inside AWS S3 buckets.

**Example Solution:**
```hcl
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
```

---

### 2. Configure a modern, secure reverse-proxy redirect using Nginx config templates.

**Example Solution:**
```nginx
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
```

---

## Technical Questions

### 1. Build a basic Terraform file launching static hosting pools inside AWS S3 buckets.

**Example Solution:**
```hcl
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
```

### 2. Configure a modern, secure reverse-proxy redirect using Nginx config templates.

**Example Solution:**
```nginx
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
```

### 3. Write an Ansible playbook managing package updates on Ubuntu platforms.

**Example Solution:**
```yaml
- name: Update system packages
  hosts: webservers
  become: yes
  tasks:
    - name: Update apt cache and upgrade packages
      apt:
        update_cache: yes
        upgrade: dist
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Cloud Platforms & Infrastructure application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Cloud Platforms & Infrastructure operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Cloud Platforms & Infrastructure configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Cloud Platforms & Infrastructure event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Cloud Platforms & Infrastructure with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Cloud Platforms & Infrastructure performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Cloud Platforms & Infrastructure failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Cloud Platforms & Infrastructure data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Cloud Platforms & Infrastructure state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Cloud Platforms & Infrastructure logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Cloud Platforms & Infrastructure files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Cloud Platforms & Infrastructure connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Cloud Platforms & Infrastructure.

*(Challenge question for self-study and practical project implementation.)*

