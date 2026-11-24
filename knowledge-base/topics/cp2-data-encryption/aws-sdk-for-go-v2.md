---
id: 20261124-cp2-aws-sdk-for-go-v2
title: CP2 · AWS SDK for Go v2
tags: [question-bank, cp2]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp2-aws-fundamentals-iam-basics, 20261124-cp2-s3, 20261124-exam-blueprint]
summary: 20 CP2 questions on AWS SDK for Go v2 (5 easy, 10 medium, 5 hard) with answers and explanations.
---

# CP2 · AWS SDK for Go v2

> Summary: 20 CP2 questions on AWS SDK for Go v2 (5 easy, 10 medium, 5 hard) with answers and explanations.

## Context
Part of the CP2 Data & Encryption bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP2).

## Questions

### CP2-Q021 · Easy
Which call loads configuration from env, shared config and roles?

- A. sdk.Init()
- B. config.FromKeys("AKIA...")
- C. aws.NewSession()
- D. config.LoadDefaultConfig(ctx)

**Answer: D** — The default credential chain is the DoD requirement.

### CP2-Q022 · Easy
How do you create a DynamoDB client from config?

- A. new(dynamodb.Client)
- B. dynamodb.New()
- C. dynamodb.Connect(url)
- D. dynamodb.NewFromConfig(cfg)

**Answer: D** — Each service package has NewFromConfig.

### CP2-Q023 · Easy ★
What is the first parameter of every SDK v2 operation?

- A. The access key
- B. The region
- C. The table name
- D. context.Context

**Answer: D** — Pass the request context.

### CP2-Q024 · Medium
How do you point the SDK at LocalStack in development?

- A. Set region to "local"
- B. Use a different SDK
- C. Edit /etc/hosts for amazonaws.com
- D. Set a custom BaseEndpoint (e.g. http://localhost:4566) via options or env config

**Answer: D** — Keep the endpoint configurable, not hardcoded.

### CP2-Q025 · Medium
What does the default credential chain check?

- A. Env vars, shared config/credentials files, then container/instance role credentials
- B. Only hardcoded keys
- C. Only ~/.aws/credentials
- D. A Kong plugin

**Answer: A** — On ECS the task role is used automatically.

### CP2-Q026 · Medium
How should you handle a DynamoDB ConditionalCheckFailedException in Go?

- A. Ignore it
- B. Use errors.As with *types.ConditionalCheckFailedException and map to a domain error
- C. Compare err.Error() strings
- D. Retry forever

**Answer: B** — Typed errors make handling reliable.

### CP2-Q027 · Medium ★
What are paginators in SDK v2 for?

- A. Iterating through multi-page results like Query or ListObjectsV2
- B. Splitting files
- C. Rate limiting
- D. Formatting output

**Answer: A** — e.g. dynamodb.NewQueryPaginator.

### CP2-Q028 · Medium
Does the SDK retry throttling errors by default?

- A. No, never
- B. Yes, with a standard retryer and backoff
- C. Only in LocalStack
- D. Only for S3

**Answer: B** — Configure max attempts if needed.

### CP2-Q029 · Medium
Where should SDK clients be created?

- A. In init() with hardcoded keys
- B. In every function call
- C. Once at startup and reused (they are safe for concurrent use)
- D. In every request handler

**Answer: C** — Reuse avoids overhead.

### CP2-Q030 · Hard
How do you make repository code testable without AWS?

- A. Use global clients
- B. Depend on a small interface of the methods you use (e.g. PutItem, GetItem) and mock it
- C. Skip tests for repositories
- D. Call AWS in every unit test

**Answer: B** — Plus LocalStack for integration tests.

### CP2-Q031 · Hard
What does attributevalue.MarshalMap do?

- A. Encrypts the struct
- B. Converts a Go struct into a DynamoDB item (map of AttributeValue)
- C. Converts JSON to YAML
- D. Generates a table

**Answer: B** — Use dynamodbav struct tags.

### CP2-Q032 · Easy ★
Which package provides pointer helpers like aws.String("x")?

- A. net/http
- B. strings
- C. fmt
- D. github.com/aws/aws-sdk-go-v2/aws

**Answer: D** — Many SDK fields are pointers.

### CP2-Q033 · Medium
Which struct tag controls DynamoDB attribute names?

- A. db:"orderId"
- B. json:"orderId" only
- C. dynamodbav:"orderId"
- D. ddb:"orderId"

**Answer: C** — attributevalue uses dynamodbav tags.

### CP2-Q034 · Hard
Why must region be configured explicitly or via env in containers?

- A. Without a region the SDK cannot build endpoints and calls fail
- B. It defaults to every region
- C. It is optional for all services
- D. Region only matters for S3

**Answer: A** — Set AWS_REGION in the task definition.

### CP2-Q035 · Medium
What should the code do if LoadDefaultConfig returns an error at startup?

- A. Retry forever silently
- B. Use hardcoded credentials
- C. Continue with nil config
- D. Fail fast: log and exit so the deployment is marked unhealthy

**Answer: D** — Misconfiguration should be visible.

### CP2-Q036 · Easy
Which SDK version does the bootcamp use?

- A. AWS SDK for Go v1
- B. boto3
- C. AWS SDK for Go v2
- D. aws-sdk-js

**Answer: C** — v1 is in maintenance; v2 is modular.

### CP2-Q037 · Hard ★
What is middleware in SDK v2 used for?

- A. Kong plugins
- B. Gin routing
- C. SQL migrations
- D. Customizing the request pipeline, e.g. adding headers or tracing

**Answer: D** — Datadog's tracer hooks into it.

### CP2-Q038 · Medium ★
How do you set a per-call timeout on an SDK call?

- A. Pass a context created with context.WithTimeout
- B. Use a goroutine and ignore it
- C. Set a global sleep
- D. Configure Kong

**Answer: A** — Contexts bound every external call.

### CP2-Q039 · Medium
Which is the correct way to read a secret at startup?

- A. Put it in the Docker image
- B. Hardcode it in main.go
- C. Call Secrets Manager with the task role, cache the value in memory
- D. Read it from the Git repo

**Answer: C** — Module 4 expands on secret scope.

### CP2-Q040 · Hard
Why avoid creating a new SDK config per request?

- A. It is a compile error
- B. It disables retries
- C. It re-resolves credentials and endpoints, adding latency and throttling risk
- D. It leaks memory always

**Answer: C** — Create once, share safely.

## Related
- [AWS fundamentals & IAM basics](aws-fundamentals-iam-basics.md) — see-also: same checkpoint.
- [S3](s3.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
