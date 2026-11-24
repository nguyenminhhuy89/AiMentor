---
id: 20261124-cp3-idempotency
title: CP3 · Idempotency
tags: [question-bank, cp3]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp3-event-driven-concepts, 20261124-cp3-sns, 20261124-exam-blueprint]
summary: 20 CP3 questions on Idempotency (5 easy, 9 medium, 6 hard) with answers and explanations.
---

# CP3 · Idempotency

> Summary: 20 CP3 questions on Idempotency (5 easy, 9 medium, 6 hard) with answers and explanations.

## Context
Part of the CP3 Async & Event-Driven bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP3).

## Questions

### CP3-Q100 · Easy
What does idempotent mean?

- A. It never fails
- B. It is encrypted
- C. Processing the same request or message multiple times has the same effect as once
- D. It runs faster

**Answer: C** — Required because delivery is at-least-once.

### CP3-Q101 · Easy
Why must SQS consumers be idempotent?

- A. For performance
- B. For encryption
- C. SQS never duplicates
- D. SQS standard can deliver a message more than once

**Answer: D** — DoD: consumers strictly idempotent.

### CP3-Q102 · Easy ★
What is an idempotency key?

- A. An API key
- B. A KMS key
- C. A sort key
- D. A unique ID (e.g. eventId) used to detect repeats

**Answer: D** — Stored with a TTL.

### CP3-Q103 · Medium
How do you record that a message was processed using DynamoDB?

- A. PutItem with attribute_not_exists(pk) on an idempotency table keyed by eventId
- B. Scan the table for the eventId
- C. Write a log line
- D. Store it in memory only

**Answer: A** — Conditional put is atomic.

### CP3-Q104 · Medium
If the conditional put fails with ConditionalCheckFailedException, the consumer should…

- A. Move it to DLQ
- B. Process it again
- C. Crash
- D. Treat it as already processed, skip side effects, and delete the message

**Answer: D** — Duplicate detected.

### CP3-Q105 · Medium
Why put a TTL on idempotency records?

- A. To expire old keys automatically and control table size
- B. To slow writes
- C. To lock them
- D. To encrypt them

**Answer: A** — Keep at least as long as possible redelivery windows.

### CP3-Q106 · Medium ★
Which is naturally idempotent?

- A. Send an email
- B. Increment balance by 10
- C. SET status = 'PAID' where orderId = X
- D. Append a row to a ledger without a key

**Answer: C** — Absolute state changes are idempotent; increments are not.

### CP3-Q107 · Hard
The consumer records the key, then crashes before doing the work. What happens on redelivery?

- A. The DLQ fixes it
- B. The work is skipped wrongly unless status is tracked (e.g. IN_PROGRESS/DONE with expiry) or done atomically
- C. The message is lost forever
- D. Everything is fine

**Answer: B** — Record completion, not just receipt, or use transactions.

### CP3-Q108 · Hard ★
How can you make "save order + mark event processed" atomic in DynamoDB?

- A. Two separate PutItem calls
- B. Use S3
- C. TransactWriteItems with both writes and conditions
- D. A Scan then Put

**Answer: C** — All-or-nothing.

### CP3-Q109 · Hard
What is the best test proving idempotency?

- A. Read the docs
- B. Check the code compiles
- C. Deliver the same message twice in a test and assert exactly one side effect
- D. Run the consumer once

**Answer: C** — DoD requires a duplicate-message test.

### CP3-Q110 · Medium
What should the HTTP API do with a repeated Idempotency-Key and the same body?

- A. Create a second order
- B. Return the original stored response
- C. Return 500
- D. Ignore the key

**Answer: B** — Same key + same body → same result.

### CP3-Q111 · Hard
Repeated Idempotency-Key but a different request body?

- A. Return the old response silently
- B. Delete the old order
- C. Reject with an error (e.g. 409/422) because the key is being reused for a different request
- D. Process it as new

**Answer: C** — Prevents accidental misuse.

### CP3-Q112 · Easy
Which field is the best idempotency key for an EventBridge/SNS event?

- A. The event's unique ID
- B. The event type
- C. The region
- D. The timestamp

**Answer: A** — Timestamps and types repeat.

### CP3-Q113 · Medium
Is sending a confirmation email idempotent by default?

- A. Only with SES
- B. Only on FIFO
- C. No, sending twice sends two emails; you must guard it with a key
- D. Yes

**Answer: C** — External side effects need explicit guards.

### CP3-Q114 · Medium ★
Exactly-once processing in practice usually means…

- A. A special AWS setting on all services
- B. Using only FIFO
- C. At-least-once delivery plus idempotent processing
- D. Never retrying

**Answer: C** — Effectively-once.

### CP3-Q115 · Hard
Two duplicates arrive at the same moment on two consumers. What makes only one win?

- A. A sleep before processing
- B. Logging both
- C. An in-memory map in each consumer
- D. An atomic conditional write on the idempotency key

**Answer: D** — In-memory checks do not work across instances.

### CP3-Q116 · Medium
Where should idempotency logic live in the code?

- A. In the consumer/service layer wrapping the side effects
- B. In the OpenAPI spec
- C. In the Dockerfile
- D. In Kong

**Answer: A** — Close to the business operation.

### CP3-Q117 · Hard
Why is "check then write" (GetItem then PutItem) not safe for idempotency?

- A. A race lets two consumers both see "not processed" and both write
- B. It costs more
- C. GetItem is slow
- D. PutItem cannot follow GetItem

**Answer: A** — Use a single conditional write.

### CP3-Q118 · Easy ★
Which HTTP methods are not idempotent by definition?

- A. HEAD and OPTIONS
- B. DELETE and GET
- C. GET and PUT
- D. POST and PATCH

**Answer: D** — They need idempotency keys for safe retries.

### CP3-Q119 · Medium
What TTL is reasonable for idempotency records of SQS messages?

- A. 5 minutes always
- B. Never expire
- C. Longer than the maximum time a duplicate could arrive, e.g. at least the queue retention
- D. 1 second

**Answer: C** — Match the redelivery window.

## Related
- [Event-driven concepts](event-driven-concepts.md) — see-also: same checkpoint.
- [SNS](sns.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
