---
id: 20261124-cp6-logs-metrics-rum
title: CP6 · Logs, metrics & RUM
tags: [question-bank, cp6]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp6-code-quality-in-ci, 20261124-cp6-tracing-datadog-apm, 20261124-exam-blueprint]
summary: 20 CP6 questions on Logs, metrics & RUM (5 easy, 10 medium, 5 hard) with answers and explanations.
---

# CP6 · Logs, metrics & RUM

> Summary: 20 CP6 questions on Logs, metrics & RUM (5 easy, 10 medium, 5 hard) with answers and explanations.

## Context
Part of the CP6 Quality, Observability & Ops bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP6).

## Questions

### CP6-Q046 · Easy ★
What are the three pillars of observability?

- A. Logs, metrics and traces
- B. Git, CI and CD
- C. CPU, memory and disk
- D. Jira, Confluence and Slack

**Answer: A** — Each answers different questions.

### CP6-Q047 · Easy ★
What is a metric?

- A. A JSON body
- B. A log line
- C. A numeric measurement over time, e.g. request count or latency
- D. A trace

**Answer: C** — Cheap to store and alert on.

### CP6-Q048 · Easy
What is Datadog RUM?

- A. A Go linter
- B. A backend profiler
- C. A queue metric
- D. Real User Monitoring of front-end performance and user sessions

**Answer: D** — Awareness level in the bootcamp.

### CP6-Q049 · Medium
What are the four golden signals?

- A. Latency, traffic, errors, saturation
- B. Logs, metrics, traces, RUM
- C. CPU, RAM, disk, network only
- D. Build, test, scan, deploy

**Answer: A** — From Google SRE.

### CP6-Q050 · Medium ★
Which log level should normal successful requests use?

- A. error
- B. fatal
- C. panic
- D. info (or debug for detailed data)

**Answer: D** — Reserve error for real failures.

### CP6-Q051 · Medium
What is log cardinality risk with metrics tags?

- A. Metrics stop working at 10 tags
- B. Tagging metrics with unbounded values (e.g. orderId) explodes the number of series and cost
- C. Logs become encrypted
- D. Too few tags

**Answer: B** — Use bounded tags like endpoint, status.

### CP6-Q052 · Medium
What is a Datadog log pipeline used for?

- A. Parsing, enriching and remapping logs (e.g. status, trace_id) on ingestion
- B. Encrypting data
- C. Shipping images
- D. Running CI

**Answer: A** — Structured JSON makes it easy.

### CP6-Q053 · Medium
What should a custom business metric for the capstone be?

- A. Customer email as a tag
- B. orders.created count tagged by status/env
- C. The full request body
- D. One metric per orderId

**Answer: B** — Business KPIs alongside technical ones.

### CP6-Q054 · Medium
How should PII appear in logs?

- A. Not at all, or masked (e.g. a***@example.com)
- B. Only at debug level
- C. Base64 encoded
- D. Fully in plaintext

**Answer: A** — Datadog sensitive data scanner adds a safety net.

### CP6-Q055 · Hard
RUM sessions show slow page loads while API latency is fine. What does that suggest?

- A. Front-end issues (assets, rendering, network) rather than backend
- B. Kong is down
- C. The database is slow
- D. SQS is full

**Answer: A** — RUM complements APM.

### CP6-Q056 · Hard
How can RUM link front-end actions to backend traces?

- A. Enable RUM-APM trace correlation so browser requests carry trace headers to allowed origins
- B. Put trace IDs in the URL path
- C. It cannot
- D. Use cookies with passwords

**Answer: A** — Configure allowedTracingUrls.

### CP6-Q057 · Medium ★
What is a Datadog monitor?

- A. A tracer
- B. A log index
- C. A rule that evaluates metrics/logs/traces and notifies when thresholds are crossed
- D. A dashboard widget only

**Answer: C** — Routes to PagerDuty.

### CP6-Q058 · Easy
What is a dashboard for?

- A. Writing tests
- B. Deploying code
- C. Visualizing key metrics and status in one place
- D. Storing logs

**Answer: C** — DoD: dashboards configured.

### CP6-Q059 · Medium
Which widgets belong on the Order Service dashboard?

- A. Request rate, error rate, p95 latency, DLQ depth, consumer lag
- B. Git commit count only
- C. Jira story points
- D. Office temperature

**Answer: A** — Golden signals plus queue health.

### CP6-Q060 · Hard
What is the difference between a log-based metric and a raw log search?

- A. They are identical
- B. Log metrics store full logs
- C. Searches are cheaper for alerting
- D. A log-based metric aggregates counts over time cheaply for dashboards/alerts; searches inspect individual events

**Answer: D** — Use metrics for alerting.

### CP6-Q061 · Medium
What is log retention?

- A. Log level
- B. Log size
- C. Log format
- D. How long logs are kept searchable before deletion or archive

**Answer: D** — Balance cost and audit needs.

### CP6-Q062 · Hard ★
Why log in JSON with consistent field names (trace_id, service, status)?

- A. Datadog only accepts JSON
- B. To encrypt logs
- C. JSON is smaller
- D. Pipelines can parse once and queries/alerts work across services

**Answer: D** — Consistency across teams.

### CP6-Q063 · Easy
Which tool is used for AWS-native metrics and logs in the DoD?

- A. Amazon SNS
- B. Kong
- C. Amazon CloudWatch
- D. AWS KMS

**Answer: C** — Alongside Datadog.

### CP6-Q064 · Medium
What is an SLI?

- A. A log file
- B. A measured indicator of service level, e.g. % of requests under 300 ms
- C. A Jira label
- D. A security group

**Answer: B** — SLOs set targets on SLIs.

### CP6-Q065 · Hard
What is an error budget?

- A. The number of bugs allowed in Jira
- B. A CloudWatch quota
- C. The allowed amount of unreliability (1 − SLO) over a period, used to balance releases and stability
- D. A finance budget for errors

**Answer: C** — Awareness: SRE practice.

## Related
- [Code quality in CI](code-quality-in-ci.md) — see-also: same checkpoint.
- [Tracing & Datadog APM](tracing-datadog-apm.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
