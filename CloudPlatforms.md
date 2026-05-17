# Cloud Platforms (AWS, GCP, Azure) Interview Questions

This document contains interview questions focused on cloud computing, infrastructure as a service, and cloud platforms like AWS and GCP.

## Basic (Easy)

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
\n## Additional Depth (Architectural Focus)\n
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
