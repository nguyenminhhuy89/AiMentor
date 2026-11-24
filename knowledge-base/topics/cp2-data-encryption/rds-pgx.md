---
id: 20261124-cp2-rds-pgx
title: CP2 · RDS & pgx
tags: [question-bank, cp2]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp2-aws-fundamentals-iam-basics, 20261124-cp2-aws-sdk-for-go-v2, 20261124-exam-blueprint]
summary: 15 CP2 questions on RDS & pgx (4 easy, 7 medium, 4 hard) with answers and explanations.
---

# CP2 · RDS & pgx

> Summary: 15 CP2 questions on RDS & pgx (4 easy, 7 medium, 4 hard) with answers and explanations.

## Context
Part of the CP2 Data & Encryption bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP2).

## Questions

### CP2-Q086 · Easy
What is Amazon RDS?

- A. A queue
- B. A managed relational database service (e.g. PostgreSQL)
- C. A NoSQL database
- D. A file store

**Answer: B** — Customers live in RDS Postgres.

### CP2-Q087 · Easy ★
What is pgx?

- A. A DynamoDB client
- B. A PostgreSQL driver and toolkit for Go
- C. A linter
- D. A Kong plugin

**Answer: B** — pgxpool manages connections.

### CP2-Q088 · Easy ★
What are database migrations?

- A. Moving data between regions
- B. Index rebuilds
- C. Versioned scripts that evolve the schema over time
- D. Backups

**Answer: C** — Tools: golang-migrate, goose.

### CP2-Q089 · Medium
Why use parameterized queries ($1, $2) with pgx?

- A. To make queries faster to type
- B. To enable caching only
- C. To prevent SQL injection
- D. Because Postgres requires it

**Answer: C** — Never concatenate user input into SQL.

### CP2-Q090 · Medium
Why use a connection pool (pgxpool)?

- A. To avoid using context
- B. To encrypt queries
- C. To run migrations
- D. Reuse connections efficiently under concurrent requests

**Answer: D** — Opening a connection per request is slow.

### CP2-Q091 · Medium ★
When is SQL (RDS) a better fit than DynamoDB?

- A. Unlimited scale key lookups
- B. Message delivery
- C. Storing large files
- D. Relational data with joins, ad-hoc queries and strong constraints

**Answer: D** — Choose by access patterns.

### CP2-Q092 · Medium
Where should the RDS password come from?

- A. A Jira ticket
- B. The README
- C. The Docker image
- D. AWS Secrets Manager (or IAM database auth), never code

**Answer: D** — Rotation is supported by Secrets Manager.

### CP2-Q093 · Hard
What does a transaction (BEGIN … COMMIT) guarantee?

- A. Atomicity: all statements succeed or none apply
- B. Cross-database joins
- C. Automatic retries
- D. Faster writes

**Answer: A** — Use tx.Rollback on error.

### CP2-Q094 · Hard
Why should RDS be in private subnets?

- A. It is cheaper
- B. So it is not reachable from the internet, only from the service's security group
- C. Postgres requires it
- D. For faster backups

**Answer: B** — Network isolation for data stores.

### CP2-Q095 · Medium
What does pgx.ErrNoRows indicate?

- A. The connection failed
- B. Duplicate key
- C. The query returned no rows
- D. A syntax error

**Answer: C** — Map to a domain NotFound error.

### CP2-Q096 · Medium
Which Postgres error code indicates unique violation?

- A. 42P01
- B. 23505
- C. 08006
- D. 40001

**Answer: B** — Map duplicate keys to 409.

### CP2-Q097 · Hard
What is the risk of running migrations automatically at every app start on many tasks?

- A. They will be skipped
- B. It speeds deployment
- C. None
- D. Concurrent migrations can conflict; run them as a separate controlled step

**Answer: D** — Use a migration job in the pipeline.

### CP2-Q098 · Easy
Which RDS feature gives a standby in another AZ for failover?

- A. Read replica in the same AZ
- B. Snapshots
- C. Multi-AZ deployment
- D. Parameter groups

**Answer: C** — Awareness for freshers.

### CP2-Q099 · Hard ★
How should customer PII in RDS be protected beyond encryption at rest?

- A. Hash phone numbers so they can be decrypted later
- B. Store it in plaintext with a strong password
- C. Encrypt sensitive columns with KMS envelope encryption and restrict access by IAM/security groups
- D. Rely on backups

**Answer: C** — Hashing is not reversible; use encryption when you must read it back.

### CP2-Q100 · Medium
What does a repository interface give you when switching storage?

- A. Faster SQL
- B. The service code does not change when moving from memory to RDS/DynamoDB
- C. Automatic migrations
- D. Free hosting

**Answer: B** — Dependency inversion in practice.

## Related
- [AWS fundamentals & IAM basics](aws-fundamentals-iam-basics.md) — see-also: same checkpoint.
- [AWS SDK for Go v2](aws-sdk-for-go-v2.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
