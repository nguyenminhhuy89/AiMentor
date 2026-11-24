# AiMentor — 3-Week Cloud-Native Go Bootcamp (Freshers)

**Audience:** freshers, no industry experience. **Duration:** 15 working days (Mon–Fri × 3).
**Default start:** Mon 30 Nov 2026 → ends Fri 18 Dec 2026 (editable in the portal).
**Capstone:** every trainee builds one service end-to-end — the **Order Service** (customers place orders; customer email/phone are PII). Each module adds a layer to the same repo, so by Day 15 the service meets the Definition of Done.

## Design principles for freshers
1. **One repo, one service, growing daily.** No throw-away labs; every lab is a commit to the capstone.
2. **Three depth levels.** H = hands-on (must build it), G = guided (build from a template with mentor/AI help), A = awareness (explain it, draw it, no build). 3 weeks is tight for freshers, so Megaport, Apigee→Kong migration and RUM are A/G, not H.
3. **Safe cloud.** Days 6–10 run against LocalStack first, then a shared sandbox AWS account with a permissions boundary. Never personal accounts.
4. **Module 6 is a thread, not a week.** `go lint / build / test` runs from Day 2, Jira from Day 1, a Confluence page per module, trace IDs from Day 4.
5. **AI-first, not AI-only.** GitHub Copilot is allowed in every lab; trainees must explain every line they commit (checked in oral review).

## Daily rhythm
| Time | Block |
|---|---|
| 09:00–09:15 | Stand-up (Jira board), mentor-lead agent posts today's plan |
| 09:15–10:30 | Concept session (human mentor + module tutor agent) |
| 10:30–12:00 | Lab part 1 |
| 13:30–16:30 | Lab part 2 — AI tutor on call, human mentor office hours 15:00 |
| 16:30–17:00 | Daily check quiz (10 Q, AI-graded) |
| 17:00–17:30 | Commit, PR, Confluence learning log, Jira update |

## Timeline

### Week 1 — Foundations + Module 1: Contract & Core API
| Day | Module | Topics (depth) | Lab output | Check |
|---|---|---|---|---|
| D1 Mon | Onboarding | Program, Git/GitHub flow (H), GitHub Copilot setup (H), Jira & Confluence basics (H), how a cloud backend fits together (A) | Repo from template, first PR, Jira ticket, Confluence profile page | Day quiz |
| D2 Tue | Go essentials + M6 thread | Go syntax, structs, interfaces, errors, modules, context (H); `go build`, `go test`, golangci-lint (H) | `pkg/order` domain types + table-driven tests; lint passes | Day quiz |
| D3 Wed | M1 | REST & HTTP basics (H); OpenAPI 3.0 + JSON Schema: paths, components, `$ref`, validation, error schema (H) | `api/openapi.yaml` for Order Service (create/get/list/cancel) | Contract review |
| D4 Thu | M1 | oapi-codegen v2 (strict server, Gin, client, types) (H); Gin middleware: request-ID/trace-ID, structured logging, recovery, auth stub, RFC 7807 errors (H) | Generated code (zero manual edits, `go generate` in CI), middleware chain | Day quiz |
| D5 Fri | M1 | Handlers + service layer + in-memory repo (H); Copilot for tests & refactors (H) | Working API, ≥70% coverage on business logic | **Module 1 exam** |

### Week 2 — Module 2: Data & Encryption · Module 3: Async & Event-Driven
| Day | Module | Topics (depth) | Lab output | Check |
|---|---|---|---|---|
| D6 Mon | M2 | AWS basics: regions, IAM users vs roles, CLI profiles (H); AWS SDK for Go v2 config & credentials chain (H); S3 put/get/presigned URL (H) | Invoice upload to S3 | Day quiz |
| D7 Tue | M2 | DynamoDB: keys, GSIs, conditional writes (H); RDS Postgres via pgx + migrations (G); when to use which (A) | Orders in DynamoDB, customers in RDS, repository interfaces | Day quiz |
| D8 Wed | M2 | AWS KMS: CMKs, envelope encryption, encryption context (H); encrypt PII fields before persist, decrypt on read (H) | PII never stored in plain text; unit tests with KMS mock | **Module 2 exam** |
| D9 Thu | M3 | Events vs commands (A); SNS fan-out → SQS (H); EventBridge bus, rules, schema (H); EventBridge Scheduler (G) | `OrderPlaced` published; consumer service reads SQS; scheduled "cancel unpaid orders" job | Day quiz |
| D10 Fri | M3 | At-least-once delivery, idempotency keys with DynamoDB conditional put (H); SQS DLQ, maxReceiveCount, redrive (H); CloudWatch alarm on DLQ depth (G) | Idempotent consumer + DLQ + alarm; duplicate-message test | **Module 3 exam** |

### Week 3 — Module 4: Gateway, Network & Security · Module 5: Runtime, IaC & CI/CD · Module 6: Quality, Observability & Ops
| Day | Module | Topics (depth) | Lab output | Check |
|---|---|---|---|---|
| D11 Mon | M4 | Least-privilege IAM policies (H); Secrets Manager vs Parameter Store vs AppConfig — scope rules (H); VPC, public/private subnets, security groups (G); VPC endpoints / PrivateLink (G); Route 53 (G); Megaport / hybrid connectivity (A); CloudTrail (G) | Zero hardcoded secrets; IAM policy per service; network diagram in Confluence | Day quiz |
| D12 Tue | M4 | Kong: services, routes, JWT plugin, rate-limiting (H); AWS Cognito user pool & tokens (H); Apigee Edge → Kong migration mapping (A) | Kong in front of the service; Cognito JWT enforced; 429 on rate limit | **Module 4 exam** |
| D13 Wed | M5 | Docker multi-stage, distroless, non-root, image scan (H); ECS Fargate service (G); Lambda for the scheduler job (G); CloudFormation stacks, parameters, drift detection (H) | Image with 0 critical/high vulns; CFN templates for DynamoDB, SQS+DLQ, ECS | Day quiz |
| D14 Thu | M5 | GitHub Actions: lint → build → test → scan → push (H); Buildkite deploy pipeline with manual gate (G); branch protection (H) | Green CI on every PR, automated deploy to sandbox | **Module 5 exam** |
| D15 Fri | M6 | Datadog APM, Logs, Metrics (H), RUM (A); trace/correlation ID end-to-end (H); CloudWatch dashboards & alarms (G); PagerDuty routing (G); runbooks in Confluence, Atlassian Rovo search (G) | Dashboard + alert + runbook; **capstone demo** | **Module 6 exam + final DoD audit** |

## Assessment model (per module)
| Part | Weight | How |
|---|---|---|
| Theory quiz | 30% | 15–20 MCQ + short answer, auto/AI-graded |
| Practical lab | 50% | Rubric mapped to the Definition of Done (see rubrics.md) |
| Code quality | 20% | go lint/build/test green, coverage, PR hygiene |

- **Pass:** total ≥ 70 and no DoD "must" item failed.
- **< 70:** tutor agent writes a remediation plan; retake within 48 h (max one retake per module).
- **Final grade:** average of 6 modules × 0.8 + capstone demo × 0.2.

## Exam submission (Google Drive)
Folder: `AiMentor/Exams/` → one subfolder per module (`M1-Contract-API` … `M6-Quality-Ops`).
File name: `<TraineeID>_<FullName>_M<n>` (Google Doc, PDF or .docx). The doc must include the repo/PR link for the practical part.
The exam-grader agent and the portal both scan this folder, grade against the rubric, and store results in the portal.
