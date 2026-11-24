---
id: 20261124-cp3-eventbridge-scheduler
title: CP3 · EventBridge & Scheduler
tags: [question-bank, cp3]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp3-event-driven-concepts, 20261124-cp3-sns, 20261124-exam-blueprint]
summary: 20 CP3 questions on EventBridge & Scheduler (5 easy, 11 medium, 4 hard) with answers and explanations.
---

# CP3 · EventBridge & Scheduler

> Summary: 20 CP3 questions on EventBridge & Scheduler (5 easy, 11 medium, 4 hard) with answers and explanations.

## Context
Part of the CP3 Async & Event-Driven bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP3).

## Questions

### CP3-Q080 · Easy ★
What is Amazon EventBridge?

- A. A container service
- B. A database
- C. A queue
- D. A serverless event bus that routes events to targets using rules

**Answer: D** — Supports custom buses and AWS events.

### CP3-Q081 · Easy
What is an EventBridge rule?

- A. A pattern that matches events and sends them to targets
- B. A Kong route
- C. An IAM rule
- D. A schema

**Answer: A** — e.g. source = order.service, detail-type = OrderPlaced.

### CP3-Q082 · Easy ★
Which API sends custom events to a bus?

- A. Publish
- B. PutEvents
- C. PutItem
- D. SendMessage

**Answer: B** — Up to 10 entries per call.

### CP3-Q083 · Medium
What are the main fields of an EventBridge event entry?

- A. Key, Value, TTL
- B. Source, DetailType, Detail (JSON), EventBusName
- C. Topic, Body, Region
- D. Queue, Message, Delay

**Answer: B** — Rules match on these.

### CP3-Q084 · Medium ★
Which event pattern matches OrderPlaced events from the Order Service?

- A. source = *
- B. {"source":["order.service"],"detail-type":["OrderPlaced"]}
- C. {"type":"OrderPlaced"} only
- D. {"queue":"orders"}

**Answer: B** — Patterns use arrays of allowed values.

### CP3-Q085 · Medium
What is EventBridge Scheduler used for in the capstone?

- A. Encrypting messages
- B. A scheduled job that cancels unpaid orders
- C. Routing HTTP traffic
- D. Storing events

**Answer: B** — Cron/rate/one-time schedules invoking targets.

### CP3-Q086 · Medium
Which expressions does EventBridge Scheduler support?

- A. Only rate()
- B. cron(), rate() and at() one-time schedules
- C. Only cron() in UTC with no time zone
- D. SQL expressions

**Answer: B** — Scheduler supports time zones too.

### CP3-Q087 · Medium
What does the Scheduler need to invoke a target?

- A. A Kong token
- B. The trainee's access key
- C. An IAM execution role it can assume with permission to call the target
- D. Nothing

**Answer: C** — Least-privilege role per schedule.

### CP3-Q088 · Medium
Why use a custom event bus instead of the default bus?

- A. Default bus cannot have rules
- B. Required for SQS targets
- C. Separate application events from AWS service events and control permissions
- D. Custom buses are faster

**Answer: C** — Organize and secure domain events.

### CP3-Q089 · Medium
What is the EventBridge Schema Registry for?

- A. Running Lambda
- B. Rate limiting
- C. Discovering and documenting event schemas and generating code bindings
- D. Storing messages

**Answer: C** — Helps consumers understand events.

### CP3-Q090 · Hard
EventBridge delivery to a target fails. What protects against losing the event?

- A. Nothing can
- B. Increase the bus size
- C. Retry policy plus a DLQ (SQS) configured on the rule target
- D. Use a bigger Lambda

**Answer: C** — Targets support retries and DLQs.

### CP3-Q091 · Hard
Is EventBridge delivery exactly-once?

- A. No, at-least-once; consumers must be idempotent
- B. Yes
- C. Only for custom buses
- D. Only for SQS targets

**Answer: A** — Same rule as SQS.

### CP3-Q092 · Easy
Can an EventBridge rule target an SQS queue?

- A. Only via Lambda
- B. Only FIFO queues
- C. Yes
- D. No

**Answer: C** — Common for buffering.

### CP3-Q093 · Medium
What is an input transformer?

- A. Reshapes the matched event before sending it to the target
- B. A rate limiter
- C. A schema validator
- D. An encryption step

**Answer: A** — Send only what the target needs.

### CP3-Q094 · Hard ★
Why should the "cancel unpaid orders" job be idempotent?

- A. Scheduler never retries
- B. Schedules can fire more than once or overlap and orders must not be cancelled twice with side effects
- C. It runs only once a year
- D. Idempotency is only for HTTP

**Answer: B** — Use conditional updates on status.

### CP3-Q095 · Medium ★
Which is better for "run once at 2026-12-10T09:00 Asia/Saigon"?

- A. SQS delay of 10 days
- B. A cron rule on the default bus in UTC only
- C. A Lambda sleeping until then
- D. EventBridge Scheduler at() with a time zone

**Answer: D** — One-time schedules are native in Scheduler.

### CP3-Q096 · Medium
What does archive and replay on an event bus allow?

- A. Encrypting events
- B. Storing events and replaying them later, e.g. after fixing a consumer
- C. Routing HTTP
- D. Deleting events

**Answer: B** — Useful for recovery (awareness).

### CP3-Q097 · Hard
How do you test an EventBridge rule pattern before deploying?

- A. Use go vet
- B. Use TestEventPattern with a sample event
- C. Deploy to prod and watch
- D. Guess

**Answer: B** — Validates matching logic.

### CP3-Q098 · Easy
Which service would you use to run a task every night at 01:00?

- A. S3
- B. EventBridge Scheduler
- C. SNS
- D. KMS

**Answer: B** — Cron schedules.

### CP3-Q099 · Medium
Where should the trace ID go in an EventBridge event?

- A. In the rule name
- B. Inside detail (e.g. detail.metadata.traceId) so consumers can continue the trace
- C. Nowhere
- D. In the bus ARN

**Answer: B** — Keep correlation end to end.

## Related
- [Event-driven concepts](event-driven-concepts.md) — see-also: same checkpoint.
- [SNS](sns.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
