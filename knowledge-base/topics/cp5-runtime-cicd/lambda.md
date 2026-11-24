---
id: 20261124-cp5-lambda
title: CP5 · Lambda
tags: [question-bank, cp5]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp5-docker, 20261124-cp5-ecs, 20261124-exam-blueprint]
summary: 15 CP5 questions on Lambda (4 easy, 8 medium, 3 hard) with answers and explanations.
---

# CP5 · Lambda

> Summary: 15 CP5 questions on Lambda (4 easy, 8 medium, 3 hard) with answers and explanations.

## Context
Part of the CP5 Runtime, IaC & CI/CD bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP5).

## Questions

### CP5-Q046 · Easy
What is AWS Lambda?

- A. A database
- B. Serverless functions that run code in response to events without managing servers
- C. A container registry
- D. A queue

**Answer: B** — Used for the scheduled cancel job.

### CP5-Q047 · Easy ★
Which runtime is used for Go Lambdas today?

- A. go1.x (current recommended)
- B. nodejs
- C. provided.al2023 (OS-only runtime) with a bootstrap binary
- D. python

**Answer: C** — go1.x is deprecated.

### CP5-Q048 · Easy
What is the maximum Lambda execution time?

- A. 5 seconds
- B. 1 hour
- C. Unlimited
- D. 15 minutes

**Answer: D** — Long jobs need ECS or Step Functions.

### CP5-Q049 · Medium
What is a cold start?

- A. A failed deploy
- B. A DLQ
- C. A frozen container
- D. Extra latency when Lambda initializes a new execution environment

**Answer: D** — Go cold starts are relatively small.

### CP5-Q050 · Medium ★
Where should SDK clients be created in a Go Lambda?

- A. In the event payload
- B. Inside the handler every time
- C. Never
- D. Outside the handler (init/main) so they are reused across invocations

**Answer: D** — Reuse across warm invocations.

### CP5-Q051 · Medium
Which Go package wires the handler?

- A. github.com/aws/aws-lambda-go/lambda with lambda.Start(handler)
- B. os.Exec
- C. gin.Run
- D. net/http only

**Answer: A** — Standard Lambda Go library.

### CP5-Q052 · Medium
How does a Lambda get permissions to update DynamoDB?

- A. Its execution role with least-privilege policies
- B. Access keys in environment variables
- C. The caller's credentials automatically
- D. Kong

**Answer: A** — Same IAM principles.

### CP5-Q053 · Medium
What is reserved concurrency?

- A. Timeout
- B. Memory size
- C. A cap and guarantee on concurrent executions for a function
- D. Number of layers

**Answer: C** — Protects downstream systems.

### CP5-Q054 · Hard
An SQS-triggered Lambda processes a batch and one message fails. With ReportBatchItemFailures, what happens?

- A. The Lambda stops
- B. Only failed message IDs are returned to the queue for retry
- C. All are deleted
- D. The whole batch is retried

**Answer: B** — Partial batch responses.

### CP5-Q055 · Hard
Why might Lambda be preferred over ECS for the nightly cancel job?

- A. Lambda supports Gin better
- B. ECS cannot run jobs
- C. Short, infrequent work: pay per invocation, no always-on tasks
- D. Lambda has no limits

**Answer: C** — Match runtime to workload.

### CP5-Q056 · Easy ★
Which service triggers the nightly Lambda in the capstone?

- A. GitHub
- B. RDS
- C. Kong
- D. EventBridge Scheduler

**Answer: D** — Schedules invoke targets.

### CP5-Q057 · Medium
What does increasing Lambda memory also increase?

- A. Timeout
- B. Disk only
- C. CPU allocated proportionally
- D. Concurrency limit

**Answer: C** — Memory and CPU scale together.

### CP5-Q058 · Medium
Where do Lambda logs go by default?

- A. Amazon CloudWatch Logs
- B. S3
- C. Kong
- D. Jira

**Answer: A** — Forward to Datadog via extension/forwarder.

### CP5-Q059 · Hard ★
A Lambda in a VPC needs to call DynamoDB with no NAT. What enables it?

- A. Kong
- B. A DynamoDB gateway VPC endpoint
- C. Route 53 alias
- D. Public IP on Lambda

**Answer: B** — Private subnet → endpoint.

### CP5-Q060 · Medium
What is the Lambda deployment package for Go?

- A. The source code only
- B. go.mod
- C. A Dockerfile only
- D. A zip containing the compiled bootstrap binary (or a container image)

**Answer: D** — Build for linux/arm64 or amd64.

## Related
- [Docker](docker.md) — see-also: same checkpoint.
- [ECS](ecs.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
