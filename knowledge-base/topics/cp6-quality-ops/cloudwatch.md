---
id: 20261124-cp6-cloudwatch
title: CP6 · CloudWatch
tags: [question-bank, cp6]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp6-code-quality-in-ci, 20261124-cp6-tracing-datadog-apm, 20261124-exam-blueprint]
summary: 20 CP6 questions on CloudWatch (6 easy, 10 medium, 4 hard) with answers and explanations.
---

# CP6 · CloudWatch

> Summary: 20 CP6 questions on CloudWatch (6 easy, 10 medium, 4 hard) with answers and explanations.

## Context
Part of the CP6 Quality, Observability & Ops bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP6).

## Questions

### CP6-Q066 · Easy
What is Amazon CloudWatch?

- A. AWS's monitoring service for metrics, logs, alarms and dashboards
- B. A CI tool
- C. A database
- D. A gateway

**Answer: A** — AWS services publish metrics there automatically.

### CP6-Q067 · Easy
What is a CloudWatch alarm?

- A. A Lambda
- B. A watcher on a metric that changes state (OK/ALARM) when a threshold is breached
- C. A dashboard
- D. A log group

**Answer: B** — Can notify SNS → PagerDuty.

### CP6-Q068 · Easy ★
Where do ECS awslogs-driver logs go?

- A. CloudWatch Logs log groups
- B. S3 only
- C. Jira
- D. Kong

**Answer: A** — Then optionally forwarded to Datadog.

### CP6-Q069 · Medium ★
Which namespace holds SQS metrics?

- A. Custom/Queues
- B. AWS/ECS only
- C. AWS/SNS
- D. AWS/SQS

**Answer: D** — Use the queue name dimension.

### CP6-Q070 · Medium
What is CloudWatch Logs Insights?

- A. A metrics database
- B. An APM tracer
- C. A dashboard theme
- D. A query language to search and aggregate log data

**Answer: D** — e.g. filter level = "error" then stats count() by bin(5m).

### CP6-Q071 · Medium
What does "datapoints to alarm 2 out of 3" do?

- A. Sends 3 notifications
- B. Requires 2 breaching datapoints within 3 periods before alarming, reducing noise
- C. Disables the alarm
- D. Alarms twice

**Answer: B** — Tune sensitivity.

### CP6-Q072 · Medium
How should missing data be treated for the DLQ depth alarm?

- A. notBreaching (no data = no messages)
- B. breaching
- C. missing data cannot be configured
- D. ignore always triggers alarm

**Answer: A** — Avoid false alarms when the metric is absent.

### CP6-Q073 · Medium
What is a metric filter on a log group?

- A. A Kong filter
- B. A way to delete logs
- C. A pattern that turns matching log events into a CloudWatch metric
- D. An IAM filter

**Answer: C** — e.g. count of "level":"error".

### CP6-Q074 · Hard
What is a composite alarm?

- A. An alarm on two regions
- B. A dashboard
- C. A Lambda alarm only
- D. An alarm combining other alarms with AND/OR logic to reduce noise

**Answer: D** — Alert on symptoms, not every cause.

### CP6-Q075 · Hard
What is Embedded Metric Format (EMF)?

- A. Structured JSON logs that CloudWatch extracts into metrics automatically
- B. An image format
- C. A YAML template
- D. A Datadog format

**Answer: A** — Metrics from logs without API calls.

### CP6-Q076 · Medium
Why set a retention policy on log groups?

- A. Logs cannot be deleted otherwise
- B. Required by Go
- C. Retention speeds queries
- D. Default is never expire, which grows cost; set retention per need

**Answer: D** — Define it in CloudFormation.

### CP6-Q077 · Medium
Where should CloudWatch alarms be defined?

- A. In Jira
- B. In Confluence
- C. Clicked in the console
- D. In CloudFormation with the resources they watch

**Answer: D** — IaC: zero drift.

### CP6-Q078 · Easy
What does the metric ApproximateNumberOfMessagesVisible on a DLQ greater than 0 mean?

- A. The queue is healthy
- B. The consumer is idle
- C. The queue is empty
- D. Some messages failed processing and need attention

**Answer: D** — Classic DLQ alarm.

### CP6-Q079 · Medium
Which ECS metrics are standard in CloudWatch?

- A. Git commits
- B. CPUUtilization and MemoryUtilization per service
- C. Code coverage
- D. Kong routes

**Answer: B** — Container Insights adds more.

### CP6-Q080 · Hard
An alarm keeps flapping between OK and ALARM. Good fixes?

- A. Send alerts to email only
- B. Delete the alarm
- C. Lower the threshold to 0
- D. Increase evaluation periods/datapoints, smooth with a longer period or use anomaly detection

**Answer: D** — Reduce alert fatigue.

### CP6-Q081 · Easy
What is a CloudWatch dashboard?

- A. An IAM console
- B. A code editor
- C. A customizable page of metric and log widgets
- D. A VPC diagram

**Answer: C** — DoD: dashboards configured.

### CP6-Q082 · Medium ★
What is CloudWatch anomaly detection?

- A. Builds an expected band from history and alarms when metrics leave it
- B. Detects IAM anomalies
- C. Detects Go bugs
- D. Scans images

**Answer: A** — Useful for traffic with daily patterns.

### CP6-Q083 · Hard ★
Datadog and CloudWatch both monitor the service. How to avoid duplicate pages?

- A. Disable CloudWatch completely
- B. Decide one alerting source per signal and route both to the same PagerDuty service with dedup keys
- C. Page from both always
- D. Page nobody

**Answer: B** — Clear ownership of alerts.

### CP6-Q084 · Medium
How does a CloudWatch alarm notify PagerDuty?

- A. Through S3
- B. Directly via Kong
- C. Alarm action → SNS topic → PagerDuty integration endpoint
- D. It cannot

**Answer: C** — SNS bridges to many destinations.

### CP6-Q085 · Easy ★
Which AWS service records who changed an alarm?

- A. CloudWatch Logs Insights
- B. Kong
- C. CloudTrail
- D. SQS

**Answer: C** — API changes are audited in CloudTrail.

## Related
- [Code quality in CI](code-quality-in-ci.md) — see-also: same checkpoint.
- [Tracing & Datadog APM](tracing-datadog-apm.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
