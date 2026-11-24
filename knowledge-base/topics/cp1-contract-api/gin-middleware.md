---
id: 20261124-cp1-gin-middleware
title: CP1 · Gin & middleware
tags: [question-bank, cp1]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp1-http-rest, 20261124-cp1-openapi-3-0, 20261124-exam-blueprint]
summary: 20 CP1 questions on Gin & middleware (6 easy, 10 medium, 4 hard) with answers and explanations.
---

# CP1 · Gin & middleware

> Summary: 20 CP1 questions on Gin & middleware (6 easy, 10 medium, 4 hard) with answers and explanations.

## Context
Part of the CP1 Contract & Core API bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP1).

## Questions

### CP1-Q086 · Easy ★
What is Gin?

- A. A load balancer
- B. A test framework
- C. A database
- D. A Go HTTP web framework with routing and middleware

**Answer: D** — Used for the Order Service.

### CP1-Q087 · Easy
What is middleware in Gin?

- A. A Kong plugin only
- B. A Docker layer
- C. A handler function that runs before/after route handlers for cross-cutting concerns
- D. A database driver

**Answer: C** — Logging, recovery, auth, request IDs.

### CP1-Q088 · Easy
What does the Recovery middleware do?

- A. Recovers secrets
- B. Restores deleted orders
- C. Catches panics, returns 500 and keeps the server running
- D. Retries failed requests

**Answer: C** — Never let a panic crash the process.

### CP1-Q089 · Easy ★
What does c.Next() do inside middleware?

- A. Returns 200
- B. Runs the remaining handlers in the chain
- C. Skips to the next request
- D. Stops the chain

**Answer: B** — Code after c.Next() runs after the handler.

### CP1-Q090 · Medium ★
What does c.Abort() do?

- A. Panics
- B. Closes the TCP connection immediately
- C. Stops calling the remaining handlers in the chain
- D. Kills the server

**Answer: C** — Used by auth middleware on failure.

### CP1-Q091 · Medium
Which middleware order is best?

- A. auth → logger → recovery → request ID
- B. handler → recovery → logger
- C. request ID → logger → recovery → auth → handler
- D. logger only

**Answer: C** — The ID must exist before logging; recovery should wrap auth and handlers.

### CP1-Q092 · Medium ★
What should the request-ID middleware do?

- A. Read X-Request-ID (or traceparent) or generate one, store it in context and echo it in the response header
- B. Set a cookie
- C. Log the request body
- D. Generate an order ID

**Answer: A** — Enables correlation across logs and services.

### CP1-Q093 · Medium
Why use structured logging (JSON) instead of fmt.Println?

- A. JSON logs are encrypted
- B. Logs become searchable fields (trace_id, status, latency) in Datadog
- C. It is shorter
- D. Println is not allowed in Go

**Answer: B** — Structured logs power observability.

### CP1-Q094 · Medium
What should NOT be logged by the logging middleware?

- A. Latency
- B. HTTP method and path
- C. Status code
- D. Request bodies containing PII or tokens

**Answer: D** — Mask or omit sensitive data.

### CP1-Q095 · Medium
How should a handler get request-scoped values like trace ID?

- A. From environment variables
- B. From the context set by middleware
- C. From global variables
- D. From the database

**Answer: B** — Global state breaks concurrency.

### CP1-Q096 · Medium
What does gin.New() vs gin.Default() differ in?

- A. gin.Default() adds the default Logger and Recovery middleware; gin.New() adds none
- B. gin.New() is deprecated
- C. gin.Default() disables routing
- D. No difference

**Answer: A** — Use gin.New() to control the middleware chain explicitly.

### CP1-Q097 · Hard ★
Why should graceful shutdown be implemented?

- A. To keep the server running forever
- B. To skip health checks
- C. To finish in-flight requests when ECS stops a task (SIGTERM) instead of dropping them
- D. To make startup faster

**Answer: C** — Use http.Server.Shutdown with a timeout.

### CP1-Q098 · Hard
A middleware writes the response then the handler writes again. Result?

- A. Headers already written warning and a corrupt or ignored second write
- B. Nothing happens
- C. The server panics always
- D. Two responses are sent

**Answer: A** — Abort after writing in middleware.

### CP1-Q099 · Hard
Where should a timeout for downstream calls be enforced?

- A. In Kong only
- B. Nowhere, AWS handles it
- C. With time.Sleep
- D. Via context deadlines (http.Server timeouts plus context.WithTimeout per call)

**Answer: D** — Bound every external call.

### CP1-Q100 · Easy
Which Gin method binds a JSON body into a struct?

- A. json.Print(req)
- B. c.Param(&req)
- C. c.Query(&req)
- D. c.ShouldBindJSON(&req)

**Answer: D** — With strict-server, the generated code binds for you.

### CP1-Q101 · Medium
What should a health check endpoint (/healthz) return?

- A. A 500 every minute
- B. The OpenAPI spec
- C. The full order list
- D. 200 quickly when the process is ready, without heavy dependencies

**Answer: D** — Used by ECS/ALB health checks.

### CP1-Q102 · Medium
How can middleware measure request latency?

- A. Use time.Sleep
- B. Ask the client
- C. Read DynamoDB metrics
- D. Record time before c.Next() and compute duration after it

**Answer: D** — Emit latency as a log field and metric.

### CP1-Q103 · Hard
How should auth middleware treat a missing Authorization header on a protected route?

- A. Return 200 with an empty body
- B. Abort with 401 and a problem+json body
- C. Allow the request
- D. Return 404

**Answer: B** — Fail closed.

### CP1-Q104 · Easy
What does c.JSON(201, order) do?

- A. Logs the order
- B. Serializes order as JSON with status 201
- C. Parses JSON into order
- D. Saves the order

**Answer: B** — Response writer helper.

### CP1-Q105 · Medium
Why should CORS be configured deliberately?

- A. Browsers block cross-origin calls unless the server allows specific origins
- B. CORS encrypts traffic
- C. CORS is needed for server-to-server calls
- D. It speeds up Go

**Answer: A** — Allow only known front-end origins.

## Related
- [HTTP & REST](http-rest.md) — see-also: same checkpoint.
- [OpenAPI 3.0](openapi-3-0.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
