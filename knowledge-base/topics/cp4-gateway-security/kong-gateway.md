---
id: 20261124-cp4-kong-gateway
title: CP4 · Kong gateway
tags: [question-bank, cp4]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp4-iam-least-privilege, 20261124-cp4-secrets-configuration, 20261124-exam-blueprint]
summary: 20 CP4 questions on Kong gateway (6 easy, 9 medium, 5 hard) with answers and explanations.
---

# CP4 · Kong gateway

> Summary: 20 CP4 questions on Kong gateway (6 easy, 9 medium, 5 hard) with answers and explanations.

## Context
Part of the CP4 Gateway, Network & Security bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP4).

## Questions

### CP4-Q081 · Easy
What is Kong?

- A. An API gateway that routes traffic and applies plugins like auth and rate limiting
- B. A CI tool
- C. A database
- D. A monitoring agent

**Answer: A** — Fronts the Order Service.

### CP4-Q082 · Easy ★
In Kong, what is a Service?

- A. A plugin
- B. A user
- C. A Docker container
- D. The upstream backend API that Kong proxies to

**Answer: D** — e.g. http://order-service.internal:8080.

### CP4-Q083 · Easy
In Kong, what is a Route?

- A. An IAM policy
- B. A queue
- C. Rules (paths, methods, hosts) that match requests and send them to a Service
- D. A DNS record

**Answer: C** — e.g. /v1/orders → order-service.

### CP4-Q084 · Easy
Which Kong plugin limits requests per consumer per time window?

- A. cors
- B. file-log
- C. rate-limiting
- D. request-transformer

**Answer: C** — Returns 429 when exceeded.

### CP4-Q085 · Medium
Which Kong plugin validates Cognito-issued JWTs?

- A. jwt (or openid-connect in Enterprise) configured with the Cognito issuer keys
- B. key-auth
- C. basic-auth
- D. ip-restriction only

**Answer: A** — Verify signature, issuer, audience, expiry.

### CP4-Q086 · Medium
What is a Kong Consumer?

- A. A route
- B. A backend service
- C. An entity representing a client app/user that credentials and plugins can attach to
- D. A database table

**Answer: C** — Rate limits can be per consumer.

### CP4-Q087 · Medium
Where can plugins be applied?

- A. Only per database
- B. Only in code
- C. Globally, per Service, per Route or per Consumer
- D. Only globally

**Answer: C** — Most specific wins.

### CP4-Q088 · Medium ★
What is decK used for?

- A. Building Docker images
- B. Managing Kong configuration declaratively from versioned YAML
- C. Encrypting secrets
- D. Running Go tests

**Answer: B** — Config as code for the gateway.

### CP4-Q089 · Medium
What should the gateway forward to the service after validating the JWT?

- A. The Cognito client secret
- B. Identity claims (e.g. sub) in headers and the trace ID, never the raw secret keys
- C. Nothing at all
- D. The user's password

**Answer: B** — Service trusts gateway-validated identity.

### CP4-Q090 · Medium ★
Rate limiting policy "local" vs "redis" in Kong: what's the difference?

- A. No difference
- B. Local counts per node; redis/cluster shares counts across nodes for accurate limits
- C. Redis is only for logging
- D. Local is for databases

**Answer: B** — Accuracy across multiple gateway nodes.

### CP4-Q091 · Hard
How do you prove Kong enforces auth (DoD)?

- A. Read the config
- B. A test: request without token → 401, invalid token → 401, valid token → 200
- C. Ask the mentor
- D. Check Kong is running

**Answer: B** — Behavioral evidence.

### CP4-Q092 · Hard
Migrating from Apigee Edge to Kong: how do Apigee policies map?

- A. Policies become Lambda functions
- B. Proxies → Services/Routes; policies (VerifyJWT, SpikeArrest/Quota) → plugins (jwt, rate-limiting)
- C. One-to-one code copy
- D. They cannot be migrated

**Answer: B** — Awareness: build a mapping table.

### CP4-Q093 · Hard
How should traffic be migrated from Apigee to Kong safely?

- A. Switch everything at once on Friday
- B. Gradually via DNS/weighted routing with monitoring and rollback, after contract parity tests
- C. Ask clients to change URLs immediately
- D. Delete Apigee first

**Answer: B** — Weighted Route 53 records help.

### CP4-Q094 · Easy
What HTTP status does Kong return when the rate limit is exceeded?

- A. 429
- B. 503
- C. 401
- D. 200

**Answer: A** — With RateLimit headers.

### CP4-Q095 · Medium
Why should Kong strip or override X-User-Id headers coming from clients?

- A. Clients could forge identity headers; only the gateway should set them after auth
- B. Headers are illegal
- C. To save bandwidth
- D. For speed

**Answer: A** — Prevent header spoofing.

### CP4-Q096 · Medium
What does the correlation-id plugin do?

- A. Adds a unique ID header to each request for tracing
- B. Rate limits
- C. Validates JWT
- D. Encrypts requests

**Answer: A** — Combine with the service's trace propagation.

### CP4-Q097 · Hard ★
Kong returns 502 for /v1/orders. First checks?

- A. Upstream service health/DNS, security groups between Kong and service, and service port
- B. Rebuild the Docker image
- C. Increase rate limit
- D. Rotate Cognito keys

**Answer: A** — 502 = bad gateway, upstream problem.

### CP4-Q098 · Easy ★
Which file format does decK use?

- A. YAML (or JSON) declarative config
- B. SQL
- C. HCL
- D. Go source

**Answer: A** — Versioned in Git.

### CP4-Q099 · Medium
Why version the API in the route path (/v1/orders)?

- A. Allows running v1 and v2 side by side during migration
- B. It speeds up routing
- C. It is required by Kong
- D. It improves security

**Answer: A** — Supports non-breaking evolution.

### CP4-Q100 · Hard
What is the risk of doing JWT validation only in the service and not in Kong?

- A. Kong breaks
- B. None
- C. JWTs expire faster
- D. Unauthenticated traffic reaches services and consumes resources; inconsistent enforcement

**Answer: D** — Validate at the edge; services may re-check claims.

## Related
- [IAM least privilege](iam-least-privilege.md) — see-also: same checkpoint.
- [Secrets & configuration](secrets-configuration.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
