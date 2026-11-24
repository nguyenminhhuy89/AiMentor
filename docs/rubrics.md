# Grading rubrics — mapped to the Definition of Done

Each module is scored out of 100: Theory 30 · Practical 50 · Code quality 20.
"MUST" items are DoD gates: failing any MUST caps the module at 69 (fail) regardless of points.

## M1 — Contract & Core API
Practical (50):
- MUST: 100% of endpoints defined in OpenAPI 3.0 with JSON Schema for request/response/error (10)
- MUST: oapi-codegen v2 output committed via `go generate`, zero manual edits (CI diff check) (10)
- Gin middleware: request/trace ID, structured logging, recovery, consistent RFC 7807 error body (15)
- Handlers delegate to a service layer; validation errors return 400 with schema detail (10)
- Can explain Copilot-generated code line by line (oral, 5)
Theory topics: HTTP verbs & status codes, OpenAPI structure, `$ref`, JSON Schema keywords, Go interfaces/errors, middleware order.

## M2 — Data & Encryption
- MUST: PII fields (email, phone) encrypted with AWS KMS before persist; no plaintext PII in DB or logs (15)
- DynamoDB table design with conditional writes; RDS access via repository interface (15)
- S3 upload + presigned URL with expiry (10)
- SDK config uses default credential chain — no keys in code (MUST, 5)
- Tests with mocks/LocalStack for each store (5)
Theory: IAM role vs user, DynamoDB keys/GSI, SQL vs NoSQL choice, envelope encryption, encryption context.

## M3 — Async & Event-Driven
- MUST: every SQS queue has a DLQ with redrive policy (10)
- MUST: consumers idempotent — duplicate message test proves single side-effect (15)
- SNS→SQS fan-out and EventBridge rule wired, event schema documented (10)
- EventBridge Scheduler job (cancel unpaid orders) (5)
- CloudWatch alarm on DLQ `ApproximateNumberOfMessagesVisible > 0` (MUST, 10)
Theory: at-least-once vs exactly-once, visibility timeout, maxReceiveCount, fan-out, event vs command.

## M4 — Gateway, Network & Security
- MUST: zero hardcoded secrets (secret scan clean); Secrets Manager for credentials, Parameter Store for config, AppConfig for feature flags (10)
- MUST: least-privilege IAM policy per service — no `*` actions/resources on data stores (10)
- Kong: route, Cognito JWT auth, rate limiting returns 429 (15)
- Network design: private subnets, SGs, VPC endpoints, Route 53 record, CloudTrail on — diagram + explanation (10)
- Apigee→Kong mapping table (policies → plugins) (5)
Theory: CIDR/subnets, SG vs NACL, PrivateLink, JWT structure, OAuth2 flows, Megaport role in hybrid links.

## M5 — Runtime, IaC & CI/CD
- MUST: multi-stage, non-root image; 0 critical/high vulnerabilities in scan (10)
- MUST: all infra in CloudFormation; drift detection shows no drift (15)
- ECS service or Lambda deployed from pipeline (10)
- GitHub Actions: lint → build → test → scan, required on PR (10)
- Buildkite deploy pipeline with manual approval step (5)
Theory: image layers, ECS task vs service, Lambda limits, CFN stack/changeset/drift, CI vs CD.

## M6 — Quality, Observability & Ops
- MUST: 100% pass of go lint/build/test in CI; business-logic coverage ≥ team threshold (default 80%) (10)
- MUST: trace/correlation ID propagated API → queue → consumer and visible in Datadog APM + logs (15)
- Dashboard (Datadog or CloudWatch) with latency, error rate, DLQ depth (10)
- PagerDuty alert routed from a monitor (5)
- Runbook in Confluence linked from the alert; Jira tickets for all work (10)
Theory: golden signals, logs vs metrics vs traces, SLO/SLI, alert fatigue, incident flow.

## Code quality (20, every module)
- go lint clean (5) · build green (5) · tests green + coverage target (5) · PR hygiene: small PR, description, Jira key (5)

## Feedback format (required for every grade)
1. Score table (Theory / Practical / Quality / Total / Pass-Fail)
2. MUST items: ✅/❌ each
3. Top 3 strengths (specific, quote their work)
4. Top 3 gaps with a concrete fix each
5. If fail: remediation plan (≤ 2 days, linked to syllabus days to redo)
