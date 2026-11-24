---
id: 20261124-cp1-openapi-3-0
title: CP1 · OpenAPI 3.0
tags: [question-bank, cp1]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp1-http-rest, 20261124-cp1-json-schema, 20261124-exam-blueprint]
summary: 25 CP1 questions on OpenAPI 3.0 (7 easy, 12 medium, 6 hard) with answers and explanations.
---

# CP1 · OpenAPI 3.0

> Summary: 25 CP1 questions on OpenAPI 3.0 (7 easy, 12 medium, 6 hard) with answers and explanations.

## Context
Part of the CP1 Contract & Core API bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP1).

## Questions

### CP1-Q021 · Easy ★
What is an OpenAPI document?

- A. A Go library
- B. A machine-readable description of an HTTP API: paths, operations, schemas and security
- C. A test report
- D. A Docker file

**Answer: B** — It is the contract from which code is generated.

### CP1-Q022 · Easy
Which top-level field declares the specification version?

- A. version: 3
- B. openapi: 3.0.3
- C. spec: openapi
- D. swagger: 2.0

**Answer: B** — OpenAPI 3.x uses the openapi field; swagger is 2.0.

### CP1-Q023 · Easy
Where are endpoints defined in an OpenAPI document?

- A. Under servers
- B. Under components
- C. Under paths
- D. Under info

**Answer: C** — Each path holds operations like get/post.

### CP1-Q024 · Easy
Where should reusable schemas like Order be defined?

- A. components/schemas
- B. paths/schemas
- C. info/schemas
- D. servers/schemas

**Answer: A** — Reference them with $ref.

### CP1-Q025 · Easy
How do you reference a reusable schema?

- A. $ref: '#/components/schemas/Order'
- B. import Order
- C. include: Order
- D. ref(Order)

**Answer: A** — JSON Reference syntax.

### CP1-Q026 · Easy ★
What does operationId do?

- A. Sets the HTTP status code
- B. Gives each operation a unique name, used by code generators for function names
- C. Defines the server URL
- D. Declares a security scheme

**Answer: B** — oapi-codegen turns operationId into handler method names.

### CP1-Q027 · Medium ★
How do you declare a path parameter orderId?

- A. In headers only
- B. As a query parameter with required: false
- C. In parameters with in: path, required: true, and a schema
- D. In requestBody

**Answer: C** — Path params must be required.

### CP1-Q028 · Medium
Where is the JSON body of POST /orders described?

- A. requestBody.content.application/json.schema
- B. parameters with in: body
- C. responses.200.body
- D. components/bodies only

**Answer: A** — OpenAPI 3 replaced in: body with requestBody.

### CP1-Q029 · Medium
How do you document that POST /orders returns 201 with an Order?

- A. returns: Order
- B. status: created
- C. output: 201
- D. responses: '201': content: application/json: schema: $ref Order

**Answer: D** — Each status code is a key under responses.

### CP1-Q030 · Medium ★
What is the `default` response used for?

- A. Describing the error shape for any status not listed explicitly
- B. The 200 response
- C. A default server
- D. Default parameter values

**Answer: A** — Useful for a shared Problem error body.

### CP1-Q031 · Medium
How do you declare bearer JWT authentication?

- A. servers.auth: bearer
- B. x-auth: jwt
- C. components.securitySchemes with type: http, scheme: bearer, bearerFormat: JWT, then a security requirement
- D. A header parameter named Authorization only

**Answer: C** — Security schemes plus security requirements.

### CP1-Q032 · Medium
What is the `servers` section for?

- A. Base URLs where the API is served, per environment
- B. Database connection strings
- C. Listing backend microservices
- D. Kong plugins

**Answer: A** — e.g. https://api.sandbox.example.com/v1.

### CP1-Q033 · Medium ★
What does `tags` on operations help with?

- A. Versioning the DB
- B. Grouping operations in docs and generated code
- C. Security
- D. Rate limiting

**Answer: B** — Tags organize the API reference.

### CP1-Q034 · Medium
How do you document a query parameter `limit` with default 20, max 100?

- A. headers: limit
- B. in: query, schema: {type: integer, default: 20, minimum: 1, maximum: 100}
- C. in: body, limit: 20
- D. in: path, max: 100

**Answer: B** — Constraints live in the parameter schema.

### CP1-Q035 · Medium
What does `required: [customerId, items]` in a schema mean?

- A. Those fields are read-only
- B. Those properties must be present in the object
- C. Those fields are deprecated
- D. Those fields are nullable

**Answer: B** — Missing required properties fail validation.

### CP1-Q036 · Hard
How do you represent a field that may be null in OpenAPI 3.0.x?

- A. x-null: yes
- B. type: [string, null]
- C. optional: true
- D. nullable: true

**Answer: D** — type arrays with null are OpenAPI 3.1 / JSON Schema 2020-12; 3.0 uses nullable.

### CP1-Q037 · Hard
What does `readOnly: true` on Order.id mean?

- A. It is hidden from responses
- B. It is returned in responses but should not be sent in requests
- C. It can never change in the database
- D. It is required in requests

**Answer: B** — readOnly/writeOnly shape request vs response.

### CP1-Q038 · Hard
Two operations share the same Problem error response. Best practice?

- A. Define it once in components/responses and $ref it
- B. Copy the YAML in every operation
- C. Skip documenting errors
- D. Return plain text errors

**Answer: A** — Reuse keeps the contract consistent.

### CP1-Q039 · Hard
How should a breaking change (removing a field) be handled?

- A. Just delete the field
- B. Introduce a new version (e.g. /v2) or deprecate first with a migration window
- C. Change the type but keep the name
- D. Rename the field silently

**Answer: B** — Contracts are promises to clients.

### CP1-Q040 · Easy
Which section holds title and version of the API?

- A. tags
- B. components
- C. paths
- D. info

**Answer: D** — info.title and info.version.

### CP1-Q041 · Medium
Which tool can lint an OpenAPI file in CI?

- A. Spectral (or redocly lint)
- B. Trivy
- C. golangci-lint
- D. cfn-lint

**Answer: A** — Lint the contract like code.

### CP1-Q042 · Medium
What does `deprecated: true` on an operation signal?

- A. It requires admin auth
- B. Clients should stop using it; it will be removed later
- C. It is disabled now
- D. It is a beta feature

**Answer: B** — Deprecation communicates future removal.

### CP1-Q043 · Hard
Why is "100% of APIs defined in OpenAPI" part of the DoD?

- A. Go requires it
- B. Kong cannot route undocumented paths
- C. Every endpoint is documented, validated and generated from one source of truth, so gateway, clients and tests stay in sync
- D. It makes the binary smaller

**Answer: C** — Undocumented endpoints drift and break consumers.

### CP1-Q044 · Medium
What does `additionalProperties: false` do?

- A. Makes all fields optional
- B. Allows any extra property
- C. Rejects properties not defined in the schema
- D. Removes the schema from docs

**Answer: C** — Strict objects catch typos from clients.

### CP1-Q045 · Hard ★
How do you model "items must contain at least one line"?

- A. required: items
- B. length > 0
- C. type: array, minItems: 1, items: $ref OrderItem
- D. items: nonEmpty

**Answer: C** — Array constraints come from JSON Schema.

## Related
- [HTTP & REST](http-rest.md) — see-also: same checkpoint.
- [JSON Schema](json-schema.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
