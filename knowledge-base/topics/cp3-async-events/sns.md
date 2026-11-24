---
id: 20261124-cp3-sns
title: CP3 · SNS
tags: [question-bank, cp3]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp3-event-driven-concepts, 20261124-cp3-sqs, 20261124-exam-blueprint]
summary: 20 CP3 questions on SNS (6 easy, 10 medium, 4 hard) with answers and explanations.
---

# CP3 · SNS

> Summary: 20 CP3 questions on SNS (6 easy, 10 medium, 4 hard) with answers and explanations.

## Context
Part of the CP3 Async & Event-Driven bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP3).

## Questions

### CP3-Q016 · Easy ★
What is Amazon SNS?

- A. A pub/sub messaging service that pushes messages to subscribers
- B. A database
- C. A queue that stores messages for polling
- D. An email client

**Answer: A** — Topics deliver to SQS, Lambda, HTTP, email...

### CP3-Q017 · Easy
What is an SNS topic?

- A. A VPC
- B. A Lambda function
- C. A named channel publishers send messages to
- D. A queue

**Answer: C** — Subscribers attach to topics.

### CP3-Q018 · Easy
Which API sends a message to a topic?

- A. Invoke
- B. SendMessage
- C. Publish
- D. PutItem

**Answer: C** — SendMessage is SQS.

### CP3-Q019 · Medium
What is the SNS → SQS fan-out pattern?

- A. One queue for all consumers
- B. SQS polling SNS
- C. SNS storing messages forever
- D. A topic with several SQS queue subscriptions so each consumer gets its own copy

**Answer: D** — Each consumer scales and fails independently.

### CP3-Q020 · Medium
What must the SQS queue policy allow for an SNS subscription?

- A. kms:CreateKey
- B. sqs:SendMessage from the SNS topic ARN (aws:SourceArn condition)
- C. s3:PutObject
- D. sns:Publish from the queue

**Answer: B** — Otherwise messages never arrive.

### CP3-Q021 · Medium
What does raw message delivery do for SQS subscribers?

- A. Compresses the message
- B. Removes attributes
- C. Delivers the original message body without the SNS JSON envelope
- D. Encrypts the message

**Answer: C** — Simpler parsing in consumers.

### CP3-Q022 · Medium ★
What is an SNS subscription filter policy?

- A. A rate limit
- B. A rule that delivers only messages whose attributes (or body) match
- C. A DLQ
- D. An IAM policy

**Answer: B** — Consumers receive only events they care about.

### CP3-Q023 · Medium ★
Does SNS standard guarantee ordering?

- A. No, standard topics are best-effort ordering; FIFO topics preserve order per message group
- B. Only with filters
- C. Only for email
- D. Yes, always

**Answer: A** — Use FIFO topics + FIFO queues when order matters.

### CP3-Q024 · Medium
How do you propagate a trace ID through SNS?

- A. As a message attribute (e.g. traceparent) read by consumers
- B. It is impossible
- C. In the topic name
- D. In the IAM role

**Answer: A** — Enables end-to-end tracing in Datadog.

### CP3-Q025 · Hard ★
If an SQS subscriber's KMS key policy does not allow SNS, what happens?

- A. The topic is deleted
- B. Messages are delivered unencrypted
- C. SNS retries forever successfully
- D. SNS cannot deliver to the encrypted queue

**Answer: D** — Grant sns.amazonaws.com kms:GenerateDataKey/Decrypt.

### CP3-Q026 · Hard
What is a DLQ on an SNS subscription for?

- A. Ordering messages
- B. Storing all messages
- C. Filtering messages
- D. Capturing messages SNS could not deliver to the endpoint after retries

**Answer: D** — Distinct from an SQS queue's own DLQ.

### CP3-Q027 · Easy
SNS FIFO topics can deliver to which subscribers?

- A. SMS
- B. Any HTTP endpoint
- C. Email
- D. SQS FIFO queues

**Answer: D** — FIFO topics pair with FIFO queues.

### CP3-Q028 · Medium
What is the maximum message size for SNS and SQS?

- A. 256 KB
- B. 4 KB
- C. 10 MB
- D. 1 MB

**Answer: A** — Larger payloads: store in S3 and send a pointer.

### CP3-Q029 · Medium
Which attribute is useful for filtering order events by type?

- A. The region
- B. eventType message attribute
- C. The topic ARN
- D. The account ID

**Answer: B** — e.g. eventType = OrderPlaced.

### CP3-Q030 · Hard
Why might you publish to EventBridge instead of SNS?

- A. SNS cannot fan out
- B. EventBridge is a queue
- C. EventBridge is cheaper for every workload
- D. Rich content-based routing rules, schema registry and many AWS/SaaS targets

**Answer: D** — Choose per routing needs.

### CP3-Q031 · Easy ★
Which IAM action does the Order Service need to publish?

- A. sns:Publish on the topic ARN
- B. sqs:ReceiveMessage
- C. sns:*
- D. sns:DeleteTopic

**Answer: A** — Least privilege.

### CP3-Q032 · Medium
An SNS publish fails due to throttling. What should the producer do?

- A. Create a new topic
- B. Drop the event silently
- C. Retry with backoff (the SDK does by default) and surface errors
- D. Return 200 and ignore

**Answer: C** — Never lose events silently.

### CP3-Q033 · Hard
A message is published to SNS but the consumer queue is empty. First thing to check?

- A. Subscription exists/confirmed, queue policy allows the topic, and filter policy matches
- B. Change the region
- C. Restart Kong
- D. Increase Lambda memory

**Answer: A** — Most issues are permissions or filters.

### CP3-Q034 · Easy
Can one SNS topic have subscribers of different types (SQS and Lambda)?

- A. Yes
- B. Only email
- C. No
- D. Only in FIFO

**Answer: A** — Protocol per subscription.

### CP3-Q035 · Medium
What does message deduplication ID do on SNS FIFO?

- A. Encrypts messages
- B. Sets visibility
- C. Prevents duplicate publishes within the dedup interval from being delivered twice
- D. Sets TTL

**Answer: C** — 5-minute dedup window.

## Related
- [Event-driven concepts](event-driven-concepts.md) — see-also: same checkpoint.
- [SQS](sqs.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
