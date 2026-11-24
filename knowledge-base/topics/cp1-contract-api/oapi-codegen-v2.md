---
id: 20261124-cp1-oapi-codegen-v2
title: CP1 · oapi-codegen v2
tags: [question-bank, cp1]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp1-http-rest, 20261124-cp1-openapi-3-0, 20261124-exam-blueprint]
summary: 20 CP1 questions on oapi-codegen v2 (5 easy, 10 medium, 5 hard) with answers and explanations.
---

# CP1 · oapi-codegen v2

> Summary: 20 CP1 questions on oapi-codegen v2 (5 easy, 10 medium, 5 hard) with answers and explanations.

## Context
Part of the CP1 Contract & Core API bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP1).

## Questions

### CP1-Q066 · Easy ★
What does oapi-codegen do?

- A. Lints Go code
- B. Generates Go types, server interfaces and clients from an OpenAPI document
- C. Builds Docker images
- D. Generates OpenAPI from Go code

**Answer: B** — Contract-first code generation.

### CP1-Q067 · Easy
What is the rule for generated files in this bootcamp?

- A. Never edit them by hand; change the contract and regenerate
- B. Delete them after build
- C. Edit them to fix bugs quickly
- D. Copy them into handlers

**Answer: A** — Zero manual edits is a DoD gate.

### CP1-Q068 · Easy
How is generation usually triggered in the repo?

- A. go build automatically
- B. go mod tidy
- C. docker build
- D. A //go:generate directive run with go generate ./...

**Answer: D** — go generate runs the codegen command.

### CP1-Q069 · Medium ★
Which generate options give Gin server code plus request/response types?

- A. spec only
- B. client only
- C. chi-server only
- D. gin-server, strict-server and models

**Answer: D** — Configured in the oapi-codegen config YAML.

### CP1-Q070 · Medium
What is the advantage of the strict server interface?

- A. Handlers receive typed request objects and return typed response objects per status code
- B. It runs faster at compile time
- C. It disables validation
- D. It removes the need for Gin

**Answer: A** — Strict mode makes status/response pairs type-safe.

### CP1-Q071 · Medium
How do you register generated handlers with a Gin engine?

- A. Add routes manually for each path
- B. Import the YAML at runtime
- C. Call the generated RegisterHandlers(router, NewStrictHandler(impl, middlewares))
- D. Use gin.Default().Load(openapi)

**Answer: C** — The generated helper wires all routes.

### CP1-Q072 · Medium
How does CI prove generated code has zero manual edits?

- A. Count lines in the file
- B. Check file timestamps
- C. Run go generate ./... then git diff --exit-code
- D. Run go vet

**Answer: C** — Any diff fails the build.

### CP1-Q073 · Medium
Where should the oapi-codegen config live?

- A. In Confluence
- B. A versioned YAML file (e.g. api/cfg.yaml) next to openapi.yaml
- C. Hardcoded in main.go
- D. In environment variables only

**Answer: B** — Reproducible generation.

### CP1-Q074 · Medium ★
An operationId is createOrder. What does strict-server generate?

- A. A createorder.go file only
- B. A Kong route
- C. A CreateOrder method with CreateOrderRequestObject and CreateOrderResponseObject types
- D. A DynamoDB table

**Answer: C** — Names derive from operationId.

### CP1-Q075 · Medium
How should the generated client be used?

- A. Inside the same handler to call itself
- B. In integration tests and by other Go services calling the Order API
- C. Never
- D. Only in production

**Answer: B** — The client is type-safe and stays in sync with the contract.

### CP1-Q076 · Hard
You need a custom Go type for a field (e.g. decimal). How with zero manual edits?

- A. Add a sed script after generation
- B. Edit the generated struct
- C. Use x-go-type / x-go-type-import extensions in the OpenAPI schema
- D. Change go.mod

**Answer: C** — Extensions customize generation from the contract.

### CP1-Q077 · Hard ★
Where should business logic live relative to generated code?

- A. In your own handler implementation and service layer that implement the generated interface
- B. In the Gin router config
- C. In the OpenAPI YAML
- D. Inside the generated file

**Answer: A** — Generated code is the boundary only.

### CP1-Q078 · Hard
How do you pin the oapi-codegen version for reproducible builds?

- A. Install latest on each CI run
- B. Track it as a tool dependency in go.mod (tools.go or go tool directive) and run that version
- C. Download a random binary
- D. Use the version in the YAML comment

**Answer: B** — Unpinned generators produce noisy diffs.

### CP1-Q079 · Easy ★
Which input file does oapi-codegen read?

- A. Dockerfile
- B. The OpenAPI document (e.g. api/openapi.yaml)
- C. main.go
- D. go.mod

**Answer: B** — The spec is the single source of truth.

### CP1-Q080 · Medium
What does the `embedded-spec` option generate?

- A. A Swagger UI server
- B. The spec embedded in Go so it can be served or used for request validation
- C. A Dockerfile
- D. Database migrations

**Answer: B** — Useful for validation middleware.

### CP1-Q081 · Hard
A new required field is added to the request schema. What breaks first if you regenerate?

- A. Compilation or tests where the handler/client constructs the request without it
- B. Only Kong
- C. Nothing ever breaks
- D. Only the database

**Answer: A** — Type-safety surfaces contract changes early.

### CP1-Q082 · Medium
Why commit generated code to the repo instead of generating only in CI?

- A. Git requires it
- B. Generated code cannot be rebuilt
- C. It hides changes
- D. Reviewers see contract impact and builds work without the generator installed

**Answer: D** — Plus the CI diff check guarantees it matches.

### CP1-Q083 · Hard
Strict handler returns `CreateOrder400ApplicationProblemPlusJSONResponse`. What does that guarantee?

- A. A redirect
- B. An empty body
- C. Any status code
- D. Status 400 with the documented problem+json body type

**Answer: D** — Responses are tied to the contract.

### CP1-Q084 · Easy
Which language does oapi-codegen generate?

- A. TypeScript only
- B. Java
- C. Go
- D. Python

**Answer: C** — It is a Go tool.

### CP1-Q085 · Medium
What should happen if the contract and handler disagree?

- A. Tests are skipped
- B. Kong fixes it
- C. The server ignores the contract
- D. The build fails because the implementation does not satisfy the generated interface

**Answer: D** — That is the point of contract-first generation.

## Related
- [HTTP & REST](http-rest.md) — see-also: same checkpoint.
- [OpenAPI 3.0](openapi-3-0.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
