---
id: 20261124-cp1-errors-service-layer-testing
title: CP1 · Errors, service layer & testing
tags: [question-bank, cp1]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp1-http-rest, 20261124-cp1-openapi-3-0, 20261124-exam-blueprint]
summary: 15 CP1 questions on Errors, service layer & testing (4 easy, 7 medium, 4 hard) with answers and explanations.
---

# CP1 · Errors, service layer & testing

> Summary: 15 CP1 questions on Errors, service layer & testing (4 easy, 7 medium, 4 hard) with answers and explanations.

## Context
Part of the CP1 Contract & Core API bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP1).

## Questions

### CP1-Q106 · Easy
What is the media type for RFC 7807 errors?

- A. application/problem+json
- B. application/error+json
- C. application/json-error
- D. text/error

**Answer: A** — Problem Details for HTTP APIs.

### CP1-Q107 · Easy ★
Which field in a problem body holds the HTTP status code?

- A. status
- B. httpStatus
- C. code
- D. error

**Answer: A** — type, title, status, detail, instance.

### CP1-Q108 · Medium
Why keep handlers thin and put logic in a service layer?

- A. Handlers cannot call functions
- B. It makes Docker images smaller
- C. Gin limits handler size
- D. Business rules can be unit-tested without HTTP and reused by other entry points

**Answer: D** — Layers: handler → service → repository.

### CP1-Q109 · Medium
How should the handler map a service error ErrOrderNotFound?

- A. errors.Is → return the generated 404 problem response
- B. Return 500 for every error
- C. Panic
- D. Return 200 with empty body

**Answer: A** — Map domain errors to documented responses.

### CP1-Q110 · Medium
What does httptest.NewRecorder help with?

- A. Testing Gin handlers in-process without starting a real server
- B. Mocking DynamoDB
- C. Recording production traffic
- D. Load testing

**Answer: A** — Fast, deterministic handler tests.

### CP1-Q111 · Medium
What should a handler test assert?

- A. The Go version
- B. The Docker tag
- C. Only that no panic happened
- D. Status code, response body shape and that the service was called correctly

**Answer: D** — Cover success and error paths.

### CP1-Q112 · Hard ★
A 500 error response should include…

- A. The AWS account ID
- B. A generic title, the trace ID, and no internal details
- C. The SQL query
- D. The stack trace

**Answer: B** — Clients use the trace ID to report issues.

### CP1-Q113 · Hard
Where should validation of business rules (e.g. cannot cancel a shipped order) live?

- A. In Kong
- B. In the Gin router
- C. In the service layer, returning a typed domain error
- D. In the OpenAPI schema only

**Answer: C** — Schema validates shape; services validate rules.

### CP1-Q114 · Medium
What is an in-memory repository used for in Week 1?

- A. Caching Kong routes
- B. Running the API end-to-end before AWS storage exists, and in tests
- C. Storing secrets
- D. Production storage

**Answer: B** — Swap it for DynamoDB in Week 2 via the interface.

### CP1-Q115 · Easy
What does `instance` mean in a problem body?

- A. The EC2 instance ID
- B. The Go version
- C. A URI identifying this specific occurrence, often the request path
- D. The number of retries

**Answer: C** — Helps correlate a single error.

### CP1-Q116 · Hard
What is the main benefit of the generated client in tests?

- A. It increases coverage of generated code
- B. Contract tests catch mismatches between implementation and spec
- C. It replaces unit tests
- D. It skips the server

**Answer: B** — Use it in integration tests against the running service.

### CP1-Q117 · Medium ★
What coverage target does the bootcamp set for business logic by Day 5?

- A. 10%
- B. No target
- C. 100% of all files including generated
- D. ≥ 70%

**Answer: D** — Rising to the team threshold (default 80%) by the final DoD.

### CP1-Q118 · Medium
Which test name style is clearest?

- A. TestOK
- B. TestStuff
- C. TestCreateOrder_ReturnsConflict_WhenAlreadyExists
- D. Test1

**Answer: C** — Names describe behavior and condition.

### CP1-Q119 · Hard
Why not return different error shapes from different handlers?

- A. JSON cannot have multiple shapes
- B. Clients and the gateway need one predictable error contract
- C. Gin forbids it
- D. It increases latency

**Answer: B** — Consistency is part of the DoD.

### CP1-Q120 · Easy ★
Which response code should a successful GET /orders/{id} return?

- A. 201 Created
- B. 204 No Content
- C. 202 Accepted
- D. 200 OK

**Answer: D** — 200 with the order body.

## Related
- [HTTP & REST](http-rest.md) — see-also: same checkpoint.
- [OpenAPI 3.0](openapi-3-0.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
