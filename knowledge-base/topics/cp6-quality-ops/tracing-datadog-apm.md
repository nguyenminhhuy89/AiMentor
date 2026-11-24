---
id: 20261124-cp6-tracing-datadog-apm
title: CP6 · Tracing & Datadog APM
tags: [question-bank, cp6]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp6-code-quality-in-ci, 20261124-cp6-logs-metrics-rum, 20261124-exam-blueprint]
summary: 25 CP6 questions on Tracing & Datadog APM (6 easy, 12 medium, 7 hard) with answers and explanations.
---

# CP6 · Tracing & Datadog APM

> Summary: 25 CP6 questions on Tracing & Datadog APM (6 easy, 12 medium, 7 hard) with answers and explanations.

## Context
Part of the CP6 Quality, Observability & Ops bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP6).

## Questions

### CP6-Q021 · Easy ★
What is distributed tracing?

- A. Tracing Git history
- B. Following a single request across services via spans that share a trace ID
- C. Counting requests
- D. Logging to a file

**Answer: B** — Datadog APM visualizes traces.

### CP6-Q022 · Easy
What is a span?

- A. A Docker layer
- B. One timed operation within a trace, e.g. an HTTP handler or a DynamoDB call
- C. A log level
- D. A metric type

**Answer: B** — Spans form a tree.

### CP6-Q023 · Easy
Which library instruments Go services for Datadog APM?

- A. golangci-lint
- B. aws-lambda-go
- C. dd-trace-go
- D. pgx

**Answer: C** — Has integrations for Gin and AWS SDK.

### CP6-Q024 · Medium ★
How is trace context propagated over HTTP?

- A. In the request body
- B. Via headers such as traceparent (W3C) or Datadog's x-datadog-* headers
- C. It is not propagated
- D. Via cookies only

**Answer: B** — Propagators inject/extract headers.

### CP6-Q025 · Medium ★
How does the trace continue through SQS?

- A. Put it in the queue name
- B. It cannot
- C. SQS propagates automatically in all cases
- D. Inject trace context into message attributes on send and extract it in the consumer

**Answer: D** — DoD: trace IDs end to end.

### CP6-Q026 · Medium
What does unified service tagging (env, service, version) enable?

- A. Rate limiting
- B. Cheaper storage
- C. Encryption
- D. Correlating traces, logs and metrics for the same service and deployment

**Answer: D** — Set DD_ENV, DD_SERVICE, DD_VERSION.

### CP6-Q027 · Medium
How do you correlate logs with traces in Datadog?

- A. Print the trace manually in Jira
- B. Use different services
- C. Use the same log file
- D. Inject dd.trace_id and dd.span_id into structured logs

**Answer: D** — Then click from a trace to its logs.

### CP6-Q028 · Medium
What does the Gin integration of dd-trace-go do?

- A. Adds rate limiting
- B. Generates OpenAPI
- C. Validates JWT
- D. Creates a span per HTTP request with route, status and latency

**Answer: D** — Use gintrace middleware.

### CP6-Q029 · Medium
Where does the tracer send spans in ECS?

- A. Directly to Kong
- B. To DynamoDB
- C. To the Datadog Agent (sidecar) over localhost, which forwards to Datadog
- D. To CloudTrail

**Answer: C** — Agent runs as a sidecar container.

### CP6-Q030 · Hard
A trace shows the API span but the consumer span is a separate trace. Likely cause?

- A. Datadog is down
- B. The consumer is written in Go
- C. Trace context was not injected into or extracted from the message attributes
- D. The queue is FIFO

**Answer: C** — Fix propagation on publish and consume.

### CP6-Q031 · Hard ★
What is trace sampling?

- A. Encrypting traces
- B. Keeping a subset of traces to control volume and cost while retaining errors and important traces
- C. Testing tracer code
- D. Deleting all traces

**Answer: B** — Configure ingestion rules.

### CP6-Q032 · Medium
What does APM "latency p95" mean?

- A. 95% of requests were faster than this value
- B. 95 requests per second
- C. The fastest request
- D. The average latency

**Answer: A** — Percentiles reveal tail latency.

### CP6-Q033 · Medium
Which tags should be added to spans for the Order Service?

- A. Credit card number
- B. Password
- C. orderId (non-PII) and customer tier, not emails or phone numbers
- D. Customer email

**Answer: C** — No PII in telemetry.

### CP6-Q034 · Hard
What does instrumenting the AWS SDK v2 client give you?

- A. Faster calls
- B. Encrypted calls
- C. Child spans for each AWS call (DynamoDB, SQS, KMS) with latency and errors
- D. Nothing

**Answer: C** — Pinpoints slow dependencies.

### CP6-Q035 · Easy
What should the API return to clients to help support correlate issues?

- A. The trace/request ID in a response header and in error bodies
- B. Nothing
- C. The database password
- D. The stack trace

**Answer: A** — Customers can quote it.

### CP6-Q036 · Medium ★
What is a service map in Datadog?

- A. A graph of services and their dependencies built from traces
- B. A Jira board
- C. A Route 53 map
- D. A VPC diagram drawn manually

**Answer: A** — Shows upstream/downstream calls.

### CP6-Q037 · Hard
Why propagate a correlation ID even when tracing exists?

- A. Datadog requires it
- B. It encrypts logs
- C. It replaces tracing
- D. It survives systems that don't support tracing and links logs, events and support tickets

**Answer: D** — Belt and braces.

### CP6-Q038 · Medium
What does "error tracking" in APM show?

- A. IAM policies
- B. CPU usage
- C. Grouped exceptions/errors with stack traces and affected services
- D. DNS records

**Answer: C** — Prioritize by frequency and impact.

### CP6-Q039 · Hard
How do you verify the DoD "trace ID end to end"?

- A. Read the code
- B. Make one request, then find a single trace containing API, publish, consumer and DynamoDB spans with matching IDs in logs
- C. Check CPU graph
- D. Restart services

**Answer: B** — Evidence-based verification.

### CP6-Q040 · Easy ★
What is Datadog?

- A. A load balancer
- B. A Git host
- C. A SaaS observability platform for metrics, traces, logs and RUM
- D. A database

**Answer: C** — Used together with CloudWatch.

### CP6-Q041 · Medium
What does DD_VERSION usually contain?

- A. The region
- B. The Go version
- C. The deployed version, e.g. the Git SHA or image tag
- D. The Datadog API key

**Answer: C** — Compare deploys in APM.

### CP6-Q042 · Hard
Where must the Datadog API key be stored?

- A. In the Dockerfile
- B. In the Git repo
- C. In Confluence
- D. In Secrets Manager and injected into the agent at runtime

**Answer: D** — It is a secret.

### CP6-Q043 · Medium
What is a "resource" in Datadog APM for an HTTP service?

- A. The route/endpoint, e.g. POST /v1/orders
- B. The Docker image
- C. The log file
- D. The AWS account

**Answer: A** — Group latency per endpoint.

### CP6-Q044 · Hard
After adding tracing, p99 latency rose. Reasonable first check?

- A. Increase rate limits
- B. Sampling and tracer config overhead, and whether spans are exported synchronously or batched
- C. Rotate keys
- D. Remove all tests

**Answer: B** — Tracing should be low overhead.

### CP6-Q045 · Easy
Which env var names the service in Datadog?

- A. DATADOG_APP
- B. SERVICE_NAME_ONLY
- C. DD_SERVICE
- D. GO_SERVICE

**Answer: C** — Part of unified tagging.

## Related
- [Code quality in CI](code-quality-in-ci.md) — see-also: same checkpoint.
- [Logs, metrics & RUM](logs-metrics-rum.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
