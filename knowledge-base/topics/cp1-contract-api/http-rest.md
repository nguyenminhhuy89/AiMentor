---
id: 20261124-cp1-http-rest
title: CP1 · HTTP & REST
tags: [question-bank, cp1]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp1-openapi-3-0, 20261124-cp1-json-schema, 20261124-exam-blueprint]
summary: 20 CP1 questions on HTTP & REST (9 easy, 8 medium, 3 hard) with answers and explanations.
---

# CP1 · HTTP & REST

> Summary: 20 CP1 questions on HTTP & REST (9 easy, 8 medium, 3 hard) with answers and explanations.

## Context
Part of the CP1 Contract & Core API bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP1).

## Questions

### CP1-Q001 · Easy
Which HTTP method should create a new order resource?

- A. HEAD /orders
- B. GET /orders
- C. POST /orders
- D. DELETE /orders

**Answer: C** — POST creates a subordinate resource in a collection.

### CP1-Q002 · Easy
Which status code means a resource was created successfully?

- A. 201 Created
- B. 204 No Content
- C. 302 Found
- D. 200 OK

**Answer: A** — Return 201, often with a Location header.

### CP1-Q003 · Easy
Which status code fits "order not found"?

- A. 500 Internal Server Error
- B. 401 Unauthorized
- C. 404 Not Found
- D. 400 Bad Request

**Answer: C** — 404 means the target resource does not exist.

### CP1-Q004 · Easy ★
Which status code fits a request body that fails schema validation?

- A. 503 Service Unavailable
- B. 201 Created
- C. 404 Not Found
- D. 400 Bad Request

**Answer: D** — Client errors in the request are 4xx; 422 is also used by some APIs.

### CP1-Q005 · Easy
Which HTTP method is safe (does not change server state)?

- A. DELETE
- B. PATCH
- C. POST
- D. GET

**Answer: D** — Safe methods: GET, HEAD, OPTIONS.

### CP1-Q006 · Easy
What does 401 Unauthorized mean?

- A. The resource moved
- B. The server crashed
- C. The user is authenticated but not allowed
- D. Authentication is missing or invalid

**Answer: D** — 403 is for authenticated-but-forbidden.

### CP1-Q007 · Easy
What does 403 Forbidden mean?

- A. The token is missing
- B. The caller is authenticated but lacks permission
- C. Rate limit exceeded
- D. The resource does not exist

**Answer: B** — Authorization failure → 403.

### CP1-Q008 · Easy
What status code signals too many requests from a rate limiter?

- A. 418 I'm a teapot
- B. 429 Too Many Requests
- C. 413 Payload Too Large
- D. 409 Conflict

**Answer: B** — Kong returns 429 when the limit is hit.

### CP1-Q009 · Medium
Which methods are idempotent by definition?

- A. POST and PATCH
- B. Only POST
- C. GET, PUT, DELETE
- D. Only GET

**Answer: C** — Repeating them has the same effect as one call.

### CP1-Q010 · Medium
Cancel an order with REST resource style. Which design is cleanest?

- A. PUT /orders/cancel
- B. DELETE /orders to remove all orders
- C. POST /orders/{id}:cancel or POST /orders/{id}/cancel as an action endpoint
- D. GET /cancelOrder?id=1

**Answer: C** — Explicit action endpoints model state transitions clearly; GET must never change state.

### CP1-Q011 · Medium
What status code fits "order already cancelled, cannot cancel again"?

- A. 409 Conflict
- B. 500 Internal Server Error
- C. 200 OK with error text
- D. 404 Not Found

**Answer: A** — 409 signals a conflict with the resource's current state.

### CP1-Q012 · Medium
What is the purpose of the Location header after POST /orders?

- A. To redirect the browser to login
- B. To set a cookie
- C. To show the server's region
- D. To give the URL of the newly created order

**Answer: D** — e.g. Location: /orders/ord_123.

### CP1-Q013 · Medium
Which is a good resource path naming style?

- A. /Orders_Items
- B. /order-item-list.php
- C. /orders/{orderId}/items
- D. /getOrderItems

**Answer: C** — Nouns, plural, hierarchical.

### CP1-Q014 · Medium ★
How should list endpoints handle large result sets?

- A. Use a GET body
- B. Return everything always
- C. Pagination with limit and cursor/next token
- D. Return only the first item

**Answer: C** — DynamoDB naturally uses LastEvaluatedKey cursors.

### CP1-Q015 · Medium ★
What does the Content-Type: application/json header on a request indicate?

- A. The request is authenticated
- B. The client accepts only JSON
- C. The body is compressed
- D. The body is JSON

**Answer: D** — Accept is for the response format.

### CP1-Q016 · Medium
A PATCH /orders/{id} request should…

- A. Create a new order
- B. Replace the full order
- C. Delete the order
- D. Partially update the order fields provided

**Answer: D** — PUT replaces; PATCH partially modifies.

### CP1-Q017 · Hard ★
A client retries POST /orders after a timeout and two orders are created. What is the standard fix?

- A. Accept an Idempotency-Key header and return the first result for repeated keys
- B. Switch POST to GET
- C. Increase the timeout to 10 minutes
- D. Return 500 on all retries

**Answer: A** — Idempotency keys make POST safe to retry.

### CP1-Q018 · Hard
Which status is best when a downstream dependency (DynamoDB) is temporarily unavailable?

- A. 201 Created
- B. 404 Not Found
- C. 503 Service Unavailable (optionally with Retry-After)
- D. 400 Bad Request

**Answer: C** — 5xx indicates server-side or dependency failure.

### CP1-Q019 · Easy ★
What does 204 No Content mean?

- A. The request had no body
- B. Success with no response body
- C. The resource was not found
- D. The server is busy

**Answer: B** — Common for DELETE.

### CP1-Q020 · Hard
What is HATEOAS-free but practical REST guidance for this bootcamp?

- A. Stable resource URLs, correct methods/status codes, consistent error bodies, and a versioned contract
- B. Every response must embed all links
- C. Use only POST for everything
- D. Use query strings for all data

**Answer: A** — Pragmatic REST focuses on consistency and contracts.

## Related
- [OpenAPI 3.0](openapi-3-0.md) — see-also: same checkpoint.
- [JSON Schema](json-schema.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
