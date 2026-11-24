---
id: 20261124-cp3-event-driven-concepts
title: CP3 · Event-driven concepts
tags: [question-bank, cp3]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp3-sns, 20261124-cp3-sqs, 20261124-exam-blueprint]
summary: 15 CP3 questions on Event-driven concepts (5 easy, 7 medium, 3 hard) with answers and explanations.
---

# CP3 · Event-driven concepts

> Summary: 15 CP3 questions on Event-driven concepts (5 easy, 7 medium, 3 hard) with answers and explanations.

## Context
Part of the CP3 Async & Event-Driven bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP3).

## Questions

### CP3-Q001 · Easy ★
What is an event?

- A. A database table
- B. A request asking a service to do something
- C. A Kong route
- D. A record that something already happened, e.g. OrderPlaced

**Answer: D** — Events are facts in the past tense.

### CP3-Q002 · Easy ★
What is a command?

- A. A fact that happened
- B. A log line
- C. A request for a specific service to perform an action, e.g. ChargePayment
- D. A metric

**Answer: C** — Commands have one intended handler; events can have many.

### CP3-Q003 · Easy
What does "producer" mean?

- A. The queue itself
- B. The service that publishes messages or events
- C. The database
- D. The service that consumes messages

**Answer: B** — The Order Service produces OrderPlaced.

### CP3-Q004 · Easy
What is a consumer?

- A. The message broker
- B. The API gateway
- C. A service that receives and processes messages
- D. A user of the website

**Answer: C** — Consumers read from SQS.

### CP3-Q005 · Medium
What does "loose coupling" mean in event-driven systems?

- A. There is no network
- B. Services call each other synchronously
- C. Services share one database
- D. Producers do not need to know who consumes their events

**Answer: D** — New consumers can be added without changing the producer.

### CP3-Q006 · Medium
Why does POST /orders often return 202 Accepted in async designs?

- A. 202 is required for POST
- B. The request is accepted but processing continues asynchronously
- C. The order failed
- D. The order was deleted

**Answer: B** — Clients poll or receive notification later.

### CP3-Q007 · Medium
What is eventual consistency?

- A. Different parts of the system converge to the same state after some delay
- B. Only DynamoDB has it
- C. All reads are instantly consistent
- D. Data is never consistent

**Answer: A** — Async systems trade immediacy for decoupling.

### CP3-Q008 · Medium
What should an event payload contain?

- A. Only a free-text message
- B. Passwords
- C. The full database dump
- D. An event ID, type, time, source, version and the minimal business data needed

**Answer: D** — Include a schema version for evolution.

### CP3-Q009 · Medium ★
Why include an eventId in every event?

- A. Consumers use it for de-duplication and tracing
- B. It is required by HTTP
- C. It sets priority
- D. It encrypts the message

**Answer: A** — Idempotency relies on stable IDs.

### CP3-Q010 · Hard
What is the "dual write" problem?

- A. Writing to the DB and publishing an event separately can leave them inconsistent if one fails
- B. Writing to two regions
- C. Writing the same row twice
- D. Two producers on one topic

**Answer: A** — Outbox pattern or transactional approaches address it (awareness).

### CP3-Q011 · Hard
What is the outbox pattern?

- A. A Kong plugin
- B. A Gmail feature
- C. A DLQ setting
- D. Store the event in the same transaction as the business change, then publish it from the outbox reliably

**Answer: D** — Avoids lost events after DB commits.

### CP3-Q012 · Medium
Fan-out means…

- A. One message is delivered to multiple consumers
- B. Messages are encrypted
- C. One consumer reads many queues
- D. Messages are deleted

**Answer: A** — SNS → multiple SQS queues.

### CP3-Q013 · Hard ★
Why should events avoid carrying PII where possible?

- A. SNS rejects PII
- B. It breaks ordering
- C. PII makes messages too large
- D. Events are copied to many consumers, queues, logs and DLQs, multiplying exposure

**Answer: D** — Send IDs and let authorized consumers fetch details.

### CP3-Q014 · Easy
Which AWS service is a fully managed message queue?

- A. Amazon SNS
- B. Amazon S3
- C. AWS KMS
- D. Amazon SQS

**Answer: D** — SNS is pub/sub; SQS is a queue.

### CP3-Q015 · Medium
How should an event schema change in a backward-compatible way?

- A. Add optional fields; never remove or rename existing fields without a new version
- B. Remove unused fields any time
- C. Rename fields freely
- D. Change types silently

**Answer: A** — Consumers may lag behind producers.

## Related
- [SNS](sns.md) — see-also: same checkpoint.
- [SQS](sqs.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
