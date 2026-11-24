---
id: 20261124-cp3-dlq-redrive
title: CP3 · DLQ & redrive
tags: [question-bank, cp3]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp3-event-driven-concepts, 20261124-cp3-sns, 20261124-exam-blueprint]
summary: 20 CP3 questions on DLQ & redrive (5 easy, 9 medium, 6 hard) with answers and explanations.
---

# CP3 · DLQ & redrive

> Summary: 20 CP3 questions on DLQ & redrive (5 easy, 9 medium, 6 hard) with answers and explanations.

## Context
Part of the CP3 Async & Event-Driven bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP3).

## Questions

### CP3-Q060 · Easy
What is a dead-letter queue (DLQ)?

- A. A deleted queue
- B. A queue that receives messages that failed processing too many times
- C. A backup database
- D. A queue for logs

**Answer: B** — Isolates failures for inspection.

### CP3-Q061 · Easy ★
Which setting moves a message to the DLQ?

- A. maxReceiveCount in the source queue's redrive policy
- B. Message size
- C. Retention period
- D. DelaySeconds

**Answer: A** — After N receives without deletion.

### CP3-Q062 · Easy ★
In the DoD, which queues need a DLQ?

- A. Only production queues
- B. Every SQS queue
- C. Only FIFO queues
- D. None

**Answer: B** — DoD: every queue has a DLQ with active alerting.

### CP3-Q063 · Medium
What is a reasonable maxReceiveCount for the capstone consumer?

- A. 1 for all queues
- B. 3–5
- C. 1000
- D. 0

**Answer: B** — Allow transient retries but isolate poison messages quickly.

### CP3-Q064 · Medium ★
What does "redrive" mean?

- A. Increasing retention
- B. Encrypting messages
- C. Moving messages from the DLQ back to the source queue after fixing the cause
- D. Deleting the DLQ

**Answer: C** — SQS supports DLQ redrive via console/API.

### CP3-Q065 · Medium
What must match between a standard source queue and its DLQ?

- A. The DLQ must also be a standard queue (FIFO source needs FIFO DLQ) in the same account/region
- B. The same retention exactly
- C. The same name
- D. The same KMS alias

**Answer: A** — Type must match.

### CP3-Q066 · Medium
Why should DLQ retention be longer than the source queue's?

- A. It makes redrive faster
- B. It reduces cost
- C. It is required by SNS
- D. So failed messages are not expired before someone investigates

**Answer: D** — Retention clock does not reset on move (enqueue timestamp kept for standard queues).

### CP3-Q067 · Medium
Which CloudWatch alarm fits the DoD?

- A. NumberOfMessagesSent on source < 1
- B. ApproximateNumberOfMessagesVisible on the DLQ > 0 for 1 datapoint
- C. Lambda duration > 1 s
- D. CPU > 80% on Kong

**Answer: B** — Any message in DLQ needs attention.

### CP3-Q068 · Medium
Where should the DLQ alarm notify?

- A. A Jira comment
- B. The trainee's personal email only
- C. Nowhere
- D. An SNS topic integrated with PagerDuty (or the team channel)

**Answer: D** — Module 6 wires PagerDuty.

### CP3-Q069 · Hard
Before redriving messages, what must you do?

- A. Delete the source queue
- B. Nothing
- C. Increase maxReceiveCount to 1000
- D. Fix and deploy the root cause, and ensure the consumer is idempotent

**Answer: D** — Otherwise they fail again or duplicate side effects.

### CP3-Q070 · Hard
What is the redrive allow policy?

- A. A KMS policy
- B. An IAM user policy
- C. A Kong policy
- D. A setting on the DLQ that controls which source queues may use it as a DLQ

**Answer: D** — Restricts DLQ usage.

### CP3-Q071 · Hard ★
How should you investigate a message in the DLQ?

- A. Delete it immediately
- B. Read its body/attributes and trace ID, find the consumer logs in Datadog, reproduce in a test
- C. Restart all services
- D. Redrive repeatedly

**Answer: B** — Use correlation IDs to find the failure.

### CP3-Q072 · Easy
Where is the redrive policy configured?

- A. On the DLQ only
- B. On the source queue
- C. On the IAM role
- D. On SNS

**Answer: B** — RedrivePolicy: deadLetterTargetArn + maxReceiveCount.

### CP3-Q073 · Medium
How is a DLQ defined in CloudFormation?

- A. An IAM role
- B. A second AWS::SQS::Queue referenced in the source queue's RedrivePolicy
- C. An S3 bucket
- D. A Lambda function

**Answer: B** — Infra as code in Module 5.

### CP3-Q074 · Hard
Which is the best DoD evidence that DLQ handling works?

- A. The queue name ends in -dlq
- B. A Confluence page saying it works
- C. A screenshot of the console
- D. A test that sends a poison message, observes it in the DLQ after N receives, and the alarm fires

**Answer: D** — Prove behavior, not configuration.

### CP3-Q075 · Easy
What does "poison message" mean?

- A. A very large message
- B. An encrypted message
- C. A message that always fails processing
- D. A malicious user

**Answer: C** — It would block retries without a DLQ.

### CP3-Q076 · Medium ★
Lambda async invocations can also send failures to…

- A. Kong
- B. An on-failure destination or DLQ (SQS/SNS)
- C. RDS
- D. GitHub

**Answer: B** — EventBridge Scheduler targets also support DLQs.

### CP3-Q077 · Hard
Why log the eventId and receive count when a message fails?

- A. To encrypt the message
- B. To correlate retries and identify messages that will go to the DLQ
- C. Because SQS requires it
- D. To speed up processing

**Answer: B** — Observability of retries.

### CP3-Q078 · Medium
What happens to a message in the DLQ if nobody acts?

- A. It is redriven automatically
- B. It stays forever
- C. It is emailed to the owner
- D. It expires after the DLQ retention period

**Answer: D** — Alerting is essential.

### CP3-Q079 · Hard
A DLQ alarm fires repeatedly with the same malformed payload from one producer. Best fix?

- A. Delete the DLQ
- B. Increase maxReceiveCount
- C. Disable the alarm
- D. Fix the producer/contract validation and add schema validation at publish time

**Answer: D** — Address the root cause upstream.

## Related
- [Event-driven concepts](event-driven-concepts.md) — see-also: same checkpoint.
- [SNS](sns.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
