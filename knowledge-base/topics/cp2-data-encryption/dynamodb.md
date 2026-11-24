---
id: 20261124-cp2-dynamodb
title: CP2 · DynamoDB
tags: [question-bank, cp2]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp2-aws-fundamentals-iam-basics, 20261124-cp2-aws-sdk-for-go-v2, 20261124-exam-blueprint]
summary: 25 CP2 questions on DynamoDB (7 easy, 12 medium, 6 hard) with answers and explanations.
---

# CP2 · DynamoDB

> Summary: 25 CP2 questions on DynamoDB (7 easy, 12 medium, 6 hard) with answers and explanations.

## Context
Part of the CP2 Data & Encryption bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP2).

## Questions

### CP2-Q061 · Easy
What is Amazon DynamoDB?

- A. A fully managed NoSQL key-value and document database
- B. An object store
- C. A cache only
- D. A relational database

**Answer: A** — Orders are stored here.

### CP2-Q062 · Easy
What is a partition key?

- A. A secondary table
- B. A foreign key
- C. The attribute DynamoDB hashes to distribute and locate items
- D. A sort order

**Answer: C** — Choose high-cardinality keys like orderId.

### CP2-Q063 · Easy
What does a sort key add?

- A. Encryption
- B. Lets multiple items share a partition key, ordered by the sort key
- C. A second table
- D. A TTL

**Answer: B** — Composite primary key: PK + SK.

### CP2-Q064 · Easy ★
Which operation reads one item by its full primary key?

- A. GetItem
- B. Query
- C. BatchWriteItem
- D. Scan

**Answer: A** — GetItem is the cheapest lookup.

### CP2-Q065 · Easy ★
Which operation writes or replaces an item?

- A. PutItem
- B. GetItem
- C. ListTables
- D. DescribeTable

**Answer: A** — UpdateItem modifies attributes.

### CP2-Q066 · Medium
What is the difference between Query and Scan?

- A. Query reads items for one partition key efficiently; Scan reads the whole table
- B. Scan uses indexes; Query does not
- C. They are the same
- D. Query only works on GSIs

**Answer: A** — Avoid Scan in request paths.

### CP2-Q067 · Medium
What is a Global Secondary Index (GSI)?

- A. A primary key
- B. A backup
- C. An index with a different partition/sort key to support another access pattern
- D. A second region

**Answer: C** — e.g. GSI on customerId to list a customer's orders.

### CP2-Q068 · Medium
How do you prevent overwriting an existing order on create?

- A. Read first then write
- B. PutItem with ConditionExpression attribute_not_exists(PK)
- C. Use a larger table
- D. Use Scan

**Answer: B** — Conditional writes are atomic.

### CP2-Q069 · Medium ★
What does ConditionalCheckFailedException mean?

- A. The table does not exist
- B. Encryption failed
- C. The write's condition was false, so nothing was written
- D. Throttling

**Answer: C** — Map to 409 Conflict when appropriate.

### CP2-Q070 · Medium
What is optimistic locking in DynamoDB?

- A. A Kong feature
- B. Using transactions for every read
- C. Locking the table
- D. A version attribute checked in a condition on update to prevent lost updates

**Answer: D** — ConditionExpression version = :expected.

### CP2-Q071 · Medium
Which capacity mode suits an unpredictable training workload?

- A. On-demand
- B. Reserved
- C. Provisioned with high RCUs
- D. Spot

**Answer: A** — Pay per request, no capacity planning.

### CP2-Q072 · Medium ★
What is TTL in DynamoDB?

- A. Transaction time limit
- B. An attribute with an epoch time after which items are deleted automatically
- C. A backup schedule
- D. A query timeout

**Answer: B** — Great for idempotency keys.

### CP2-Q073 · Medium
How do you list all orders of customer C1 efficiently?

- A. BatchGetItem all
- B. GetItem with customerId
- C. Query a GSI with partition key customerId = C1
- D. Scan with a filter

**Answer: C** — Design keys for access patterns.

### CP2-Q074 · Hard
Why does a FilterExpression on Scan not reduce read cost?

- A. It does reduce cost
- B. Filters are not supported
- C. Filters run on the client
- D. Items are read first, then filtered, so capacity is consumed for all read items

**Answer: D** — Model access patterns with keys/indexes.

### CP2-Q075 · Hard
What is a hot partition?

- A. A partition with TTL
- B. An encrypted partition
- C. A partition key receiving disproportionate traffic, causing throttling
- D. A partition stored on SSD

**Answer: C** — Choose keys that spread load.

### CP2-Q076 · Hard
What does TransactWriteItems provide?

- A. All-or-nothing writes across multiple items
- B. Faster single writes
- C. Automatic backups
- D. Cross-region replication

**Answer: A** — Useful for order + idempotency record together.

### CP2-Q077 · Medium ★
What is the maximum item size in DynamoDB?

- A. 1 GB
- B. 400 KB
- C. 4 MB
- D. 64 KB

**Answer: B** — Store large blobs in S3 instead.

### CP2-Q078 · Medium
What does UpdateItem with UpdateExpression "SET #s = :s" do?

- A. Replaces the item
- B. Creates a new table
- C. Deletes the item
- D. Sets the status attribute without replacing the whole item

**Answer: D** — Use expression attribute names for reserved words.

### CP2-Q079 · Hard
Why should PII be encrypted at the field level even though DynamoDB encrypts at rest?

- A. DynamoDB does not encrypt
- B. It reduces item size
- C. At-rest encryption does not stop anyone with read access from seeing plaintext; field encryption limits exposure
- D. It makes queries faster

**Answer: C** — Defense in depth for PII.

### CP2-Q080 · Easy
Which consistency does GetItem use by default?

- A. Strongly consistent reads
- B. No consistency
- C. Transactional reads
- D. Eventually consistent reads

**Answer: D** — Set ConsistentRead: true when needed.

### CP2-Q081 · Hard ★
Single-table design means…

- A. Only one item per table
- B. Storing multiple entity types in one table with generic PK/SK patterns to serve access patterns
- C. One table per entity
- D. Using RDS instead

**Answer: B** — Awareness level for freshers.

### CP2-Q082 · Medium
Which attribute type is best for createdAt sorting as a sort key?

- A. ISO-8601 string (lexicographically sortable) or epoch number
- B. Boolean
- C. Binary image
- D. Free-text date like "Dec 1st"

**Answer: A** — Consistent formats sort correctly.

### CP2-Q083 · Easy
Which tool lets you run DynamoDB locally?

- A. LocalStack (or DynamoDB Local)
- B. Datadog
- C. Buildkite
- D. Kong

**Answer: A** — Used in Week 2 labs.

### CP2-Q084 · Hard
BatchWriteItem returns UnprocessedItems. What should the code do?

- A. Delete the table
- B. Retry the unprocessed items with backoff
- C. Ignore them
- D. Treat as success

**Answer: B** — Batches can partially succeed.

### CP2-Q085 · Medium
What does a projection expression do?

- A. Creates an index
- B. Projects data to S3
- C. Encrypts attributes
- D. Returns only selected attributes

**Answer: D** — Reduces response size.

## Related
- [AWS fundamentals & IAM basics](aws-fundamentals-iam-basics.md) — see-also: same checkpoint.
- [AWS SDK for Go v2](aws-sdk-for-go-v2.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
