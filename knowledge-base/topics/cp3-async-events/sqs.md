---
id: 20261124-cp3-sqs
title: CP3 · SQS
tags: [question-bank, cp3]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp3-event-driven-concepts, 20261124-cp3-sns, 20261124-exam-blueprint]
summary: 25 CP3 questions on SQS (6 easy, 13 medium, 6 hard) with answers and explanations.
---

# CP3 · SQS

> Summary: 25 CP3 questions on SQS (6 easy, 13 medium, 6 hard) with answers and explanations.

## Context
Part of the CP3 Async & Event-Driven bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP3).

## Questions

### CP3-Q036 · Easy
What does SQS do?

- A. Stores messages until consumers poll and delete them
- B. Pushes to all subscribers
- C. Stores files
- D. Runs code

**Answer: A** — Pull-based queue.

### CP3-Q037 · Easy ★
Which API sends a message to a queue?

- A. Publish
- B. Invoke
- C. SendMessage
- D. PutObject

**Answer: C** — Batch variant: SendMessageBatch.

### CP3-Q038 · Easy
Which API reads messages from a queue?

- A. Poll
- B. GetMessage
- C. Query
- D. ReceiveMessage

**Answer: D** — Then DeleteMessage after processing.

### CP3-Q039 · Easy
When should a consumer delete a message?

- A. After it has been processed successfully
- B. Before processing
- C. As soon as it is received
- D. Never

**Answer: A** — Deleting early can lose messages.

### CP3-Q040 · Medium
What is the visibility timeout?

- A. How long messages are retained
- B. The max message size
- C. How long a received message stays hidden from other consumers before reappearing
- D. The delay before first delivery

**Answer: C** — Set longer than processing time.

### CP3-Q041 · Medium
What happens if processing takes longer than the visibility timeout?

- A. It goes to DLQ immediately
- B. The message becomes visible again and may be processed twice
- C. The queue pauses
- D. It is deleted

**Answer: B** — Extend with ChangeMessageVisibility or raise the timeout.

### CP3-Q042 · Medium
What is long polling?

- A. Polling from another region
- B. Polling every millisecond
- C. ReceiveMessage waits up to 20 seconds for messages, reducing empty responses and cost
- D. A FIFO feature only

**Answer: C** — Set WaitTimeSeconds=20.

### CP3-Q043 · Medium
Standard queue delivery guarantee?

- A. Strict ordering
- B. At-most-once
- C. At-least-once, with best-effort ordering
- D. Exactly-once

**Answer: C** — Consumers must be idempotent.

### CP3-Q044 · Medium ★
What does a FIFO queue add?

- A. Ordering per message group and exactly-once processing within the dedup window
- B. Push delivery
- C. Bigger messages
- D. Unlimited throughput

**Answer: A** — Name must end with .fifo.

### CP3-Q045 · Medium ★
What is the default message retention period?

- A. 4 days (configurable from 1 minute to 14 days)
- B. 30 days
- C. Forever
- D. 1 hour

**Answer: A** — Unprocessed messages expire.

### CP3-Q046 · Medium
What is the max number of messages ReceiveMessage can return per call?

- A. 1
- B. 10
- C. 100
- D. 1000

**Answer: B** — Process batches and delete each handled one.

### CP3-Q047 · Medium
What is DelaySeconds?

- A. Polling interval
- B. Retention period
- C. Postpones delivery of new messages up to 15 minutes
- D. Visibility timeout

**Answer: C** — Queue-level or per-message delay.

### CP3-Q048 · Hard
In a Go consumer loop, how should you stop cleanly on SIGTERM?

- A. Delete the queue
- B. os.Exit(1) immediately
- C. Cancel the context, stop receiving, finish in-flight messages, then exit
- D. Ignore the signal

**Answer: C** — In-flight messages otherwise reappear and get reprocessed.

### CP3-Q049 · Hard
What does ApproximateReceiveCount tell you?

- A. How many times the message has been received; used to decide when to DLQ
- B. Queue length
- C. Message size
- D. Number of consumers

**Answer: A** — maxReceiveCount compares against it.

### CP3-Q050 · Hard ★
A consumer partially processes a batch of 10 and 3 fail. Best practice with Lambda SQS triggers?

- A. Ignore the failures
- B. Delete all 10
- C. Report batch item failures so only the 3 are retried
- D. Fail the whole batch

**Answer: C** — ReportBatchItemFailures avoids reprocessing successes.

### CP3-Q051 · Easy ★
Is SQS push or pull?

- A. Pull: consumers poll
- B. Neither
- C. Both by default
- D. Push

**Answer: A** — SNS pushes; SQS is polled.

### CP3-Q052 · Medium
Which IAM actions does a consumer need?

- A. sns:Publish
- B. sqs:CreateQueue
- C. sqs:*
- D. sqs:ReceiveMessage, sqs:DeleteMessage, sqs:GetQueueAttributes (and ChangeMessageVisibility if used)

**Answer: D** — Least privilege.

### CP3-Q053 · Medium ★
Which metric shows the backlog of a queue?

- A. ApproximateAgeOfOldestQueue only
- B. ApproximateNumberOfMessagesVisible
- C. SentMessageSize
- D. NumberOfMessagesDeleted

**Answer: B** — Use it for scaling and alerts.

### CP3-Q054 · Hard
Which metric best signals that consumers are falling behind?

- A. NumberOfEmptyReceives
- B. ApproximateAgeOfOldestMessage rising
- C. NumberOfMessagesSent
- D. SentMessageSize

**Answer: B** — Old messages = processing lag.

### CP3-Q055 · Easy
Max size of a single SQS message?

- A. 1 MB
- B. 4 KB
- C. 10 MB
- D. 256 KB

**Answer: D** — Use S3 pointer pattern for bigger payloads.

### CP3-Q056 · Medium
Why encrypt queues with SSE?

- A. Messages at rest are protected; required for queues that may hold sensitive data
- B. It removes IAM checks
- C. It enables FIFO
- D. It speeds up delivery

**Answer: A** — SSE-SQS or SSE-KMS.

### CP3-Q057 · Hard
Two consumers process the same message concurrently. How can this happen in standard SQS?

- A. Only with FIFO
- B. At-least-once delivery or visibility timeout expiry
- C. Only with long polling
- D. It can never happen

**Answer: B** — Design for duplicates.

### CP3-Q058 · Medium
What does PurgeQueue do?

- A. Deletes all messages in the queue
- B. Pauses the queue
- C. Moves messages to DLQ
- D. Re-drives messages

**Answer: A** — Use carefully, never in prod casually.

### CP3-Q059 · Hard
How should poison messages (always failing) be handled?

- A. Delete them silently
- B. Retry forever
- C. Restart the consumer
- D. Let them move to a DLQ after maxReceiveCount and alert on DLQ depth

**Answer: D** — DLQs isolate bad messages.

### CP3-Q120 · Medium
What is MessageGroupId used for in a FIFO queue?

- A. Messages with the same group ID are delivered in order, one group at a time
- B. It picks the DLQ
- C. It sets encryption
- D. It sets the region

**Answer: A** — Different groups can be processed in parallel.

## Related
- [Event-driven concepts](event-driven-concepts.md) — see-also: same checkpoint.
- [SNS](sns.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
