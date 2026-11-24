---
id: 20261124-cp0-cloud-backend-basics
title: CP0 · Cloud backend basics
tags: [question-bank, cp0]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp0-git-github-flow, 20261124-cp0-github-copilot, 20261124-exam-blueprint]
summary: 15 CP0 questions on Cloud backend basics (6 easy, 7 medium, 2 hard) with answers and explanations.
---

# CP0 · Cloud backend basics

> Summary: 15 CP0 questions on Cloud backend basics (6 easy, 7 medium, 2 hard) with answers and explanations.

## Context
Part of the CP0 Onboarding & Go essentials bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP0).

## Questions

### CP0-Q051 · Easy
What does an API gateway do?

- A. Stores relational data
- B. Builds Docker images
- C. Encrypts data at rest on disk
- D. Routes client requests to backend services and enforces auth and rate limits

**Answer: D** — Kong is the gateway in this programme.

### CP0-Q052 · Easy ★
What is a microservice?

- A. A small, independently deployable service owning one business capability
- B. A tiny virtual machine
- C. A Go package inside main.go
- D. A database index

**Answer: A** — The Order Service is one microservice.

### CP0-Q053 · Easy
Which component stores the orders data in the capstone?

- A. Datadog
- B. Kong
- C. Amazon DynamoDB
- D. GitHub Actions

**Answer: C** — Orders go to DynamoDB; customers to RDS.

### CP0-Q054 · Easy
What is a message queue used for?

- A. Serving static web pages
- B. Decoupling producers and consumers so work can be processed asynchronously
- C. Encrypting passwords
- D. Building container images

**Answer: B** — SQS is the queue service used later.

### CP0-Q055 · Medium
What does "stateless service" mean?

- A. The service has no database
- B. The service cannot log
- C. The service keeps no client session in memory, so any instance can serve any request
- D. The service never restarts

**Answer: C** — Statelessness enables horizontal scaling.

### CP0-Q056 · Medium
Why do we use infrastructure as code?

- A. Infrastructure is versioned, reviewed and reproducible
- B. It makes services faster at runtime
- C. It replaces unit tests
- D. It removes the need for AWS accounts

**Answer: A** — CloudFormation is the IaC tool here.

### CP0-Q057 · Medium
What is the role of observability tools such as Datadog?

- A. Replace the API gateway
- B. Collect traces, logs and metrics to understand system behavior
- C. Store customer orders
- D. Compile Go code

**Answer: B** — You cannot fix what you cannot see.

### CP0-Q058 · Medium
What does "contract-first API" mean?

- A. Only GraphQL is allowed
- B. Code is written first and docs later
- C. Contracts are signed with the client
- D. The OpenAPI contract is written and agreed before implementation and code is generated from it

**Answer: D** — Module 1 follows contract-first.

### CP0-Q059 · Medium ★
Synchronous vs asynchronous call: which is asynchronous?

- A. A SQL SELECT inside a handler
- B. Calling GET /orders/{id} and waiting for 200
- C. Reading a file from disk
- D. Publishing OrderPlaced to SNS and returning 202

**Answer: D** — Async: the caller does not wait for downstream processing.

### CP0-Q060 · Hard ★
Why run services in private subnets?

- A. Private subnets have no IP addresses
- B. They are not directly reachable from the internet, reducing attack surface
- C. Private subnets are cheaper
- D. Public subnets cannot run containers

**Answer: B** — Traffic enters only via the gateway/load balancer.

### CP0-Q061 · Easy ★
What is CI?

- A. A Kubernetes plugin
- B. A database replica
- C. Continuously building and testing every change automatically
- D. Customer Integration

**Answer: C** — GitHub Actions runs lint/build/test on every PR.

### CP0-Q062 · Medium
What is the difference between authentication and authorization?

- A. They are the same
- B. Authentication proves who you are; authorization decides what you may do
- C. Authentication is only for admins
- D. Authorization happens before authentication

**Answer: B** — Cognito authenticates; IAM/policies authorize.

### CP0-Q063 · Hard
What is the main benefit of an event-driven design for the Order Service?

- A. Lower latency for every request
- B. No need for a database
- C. New consumers can react to OrderPlaced without changing the producer
- D. Simpler debugging than synchronous calls

**Answer: C** — Loose coupling and extensibility, at the cost of complexity.

### CP0-Q064 · Easy
LocalStack is used in the bootcamp to…

- A. Replace Datadog
- B. Run Kong in AWS
- C. Emulate AWS services locally for safe practice
- D. Host the production database

**Answer: C** — Practice first on LocalStack, then on the sandbox account.

### CP0-Q065 · Medium
What does horizontal scaling mean?

- A. Adding more CPU to one machine
- B. Adding more instances of a service
- C. Adding more columns to a table
- D. Making the API return more fields

**Answer: B** — ECS can run more tasks to scale out.

## Related
- [Git & GitHub flow](git-github-flow.md) — see-also: same checkpoint.
- [GitHub Copilot](github-copilot.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
