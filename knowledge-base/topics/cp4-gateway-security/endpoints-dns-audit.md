---
id: 20261124-cp4-endpoints-dns-audit
title: CP4 · Endpoints, DNS & audit
tags: [question-bank, cp4]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp4-iam-least-privilege, 20261124-cp4-secrets-configuration, 20261124-exam-blueprint]
summary: 20 CP4 questions on Endpoints, DNS & audit (6 easy, 11 medium, 3 hard) with answers and explanations.
---

# CP4 · Endpoints, DNS & audit

> Summary: 20 CP4 questions on Endpoints, DNS & audit (6 easy, 11 medium, 3 hard) with answers and explanations.

## Context
Part of the CP4 Gateway, Network & Security bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP4).

## Questions

### CP4-Q061 · Easy ★
What does a VPC endpoint do?

- A. Lets resources in the VPC reach AWS services privately without the internet
- B. Creates a public IP
- C. Replaces IAM
- D. Encrypts disks

**Answer: A** — Gateway and interface endpoints.

### CP4-Q062 · Easy
Which services use gateway endpoints?

- A. SQS and SNS
- B. S3 and DynamoDB
- C. Secrets Manager only
- D. KMS and STS

**Answer: B** — Others use interface endpoints (PrivateLink).

### CP4-Q063 · Medium
What is AWS PrivateLink?

- A. A public API
- B. A VPN product
- C. Private connectivity to services via interface endpoints (ENIs) in your subnets
- D. A Direct Connect location

**Answer: C** — Powers interface endpoints and partner services.

### CP4-Q064 · Medium
Why use endpoints for SQS, KMS and Secrets Manager from private subnets?

- A. They are required by Go
- B. Traffic stays on the AWS network and you can drop or reduce NAT dependency
- C. They make calls free
- D. They bypass IAM

**Answer: B** — Also allows endpoint policies.

### CP4-Q065 · Medium ★
What is an endpoint policy?

- A. A NACL rule
- B. A DNS record
- C. A resource policy on the endpoint restricting which actions/resources can be reached through it
- D. An IAM user policy

**Answer: C** — Extra guardrail.

### CP4-Q066 · Easy
What is Amazon Route 53?

- A. AWS's DNS service with domain registration and health checks
- B. A load balancer
- C. A CDN
- D. A VPN

**Answer: A** — Maps names like api.sandbox.example.com.

### CP4-Q067 · Medium
What is a Route 53 alias record?

- A. A CNAME to any website
- B. A record pointing a name to AWS resources like a load balancer, including at the zone apex
- C. An IP whitelist
- D. A TXT record

**Answer: B** — Alias works at apex and is free for AWS targets.

### CP4-Q068 · Medium
What is a private hosted zone?

- A. A hidden public domain
- B. A Kong route
- C. A paid DNS tier
- D. DNS names resolvable only inside associated VPCs

**Answer: D** — Internal service names.

### CP4-Q069 · Medium
What does a low TTL on a DNS record allow?

- A. No DNS lookups
- B. Faster propagation of changes at the cost of more queries
- C. Better encryption
- D. Permanent caching

**Answer: B** — Lower TTL before migrations.

### CP4-Q070 · Easy
What is AWS CloudTrail?

- A. A metric store
- B. A log shipper for app logs
- C. A tracing tool for Go
- D. A service that records AWS API calls for audit and security analysis

**Answer: D** — DoD: CloudTrail auditing enabled.

### CP4-Q071 · Medium
Which CloudTrail event type records actions like CreateTable or PutBucketPolicy?

- A. Data events only
- B. Management events
- C. Insights events only
- D. Network events

**Answer: B** — Data events (e.g. S3 object-level) are optional and extra.

### CP4-Q072 · Medium ★
Where should CloudTrail logs be stored for audit?

- A. The service's own logs
- B. An S3 bucket with restricted access, encryption and log file validation
- C. A Jira ticket
- D. A developer laptop

**Answer: B** — Tamper-evident storage.

### CP4-Q073 · Hard
How would you find who deleted a DynamoDB table in the sandbox?

- A. Check Datadog RUM
- B. Ask in chat only
- C. Check Kong logs
- D. Search CloudTrail for DeleteTable events and read userIdentity

**Answer: D** — CloudTrail answers who did what, when.

### CP4-Q074 · Easy
What is Megaport?

- A. A Kong plugin
- B. A network-as-a-service provider offering private connectivity, e.g. to AWS Direct Connect
- C. An AWS database
- D. A CI tool

**Answer: B** — Awareness level in this bootcamp.

### CP4-Q075 · Medium
Why would a company use Megaport/Direct Connect?

- A. To run Lambda
- B. Private, predictable connectivity between on-premises/data centers and AWS instead of the public internet
- C. To replace IAM
- D. To host Docker images

**Answer: B** — Hybrid connectivity.

### CP4-Q076 · Hard ★
What must be planned before a hybrid link via Megaport?

- A. Jira workflows
- B. Docker tags
- C. Non-overlapping IP ranges, routing (BGP) and which VPCs/services are reachable
- D. Only the domain name

**Answer: C** — Awareness: network planning.

### CP4-Q077 · Medium
What is a Route 53 health check used for?

- A. Monitoring endpoint health and failing DNS over to healthy targets
- B. Scanning images
- C. Checking Go tests
- D. Checking IAM policies

**Answer: A** — Supports failover routing.

### CP4-Q078 · Hard
Interface endpoint created but SDK still goes through NAT. Likely cause?

- A. Kong misrouting
- B. Wrong Go version
- C. Private DNS not enabled on the endpoint, so the default service name resolves publicly
- D. IAM policy too strict

**Answer: C** — Enable private DNS.

### CP4-Q079 · Easy ★
Which DoD item does CloudTrail satisfy?

- A. Code coverage
- B. Image scanning
- C. Auditing of access and changes
- D. Rate limiting

**Answer: C** — Security & Network DoD.

### CP4-Q080 · Medium
What does CloudTrail log file integrity validation provide?

- A. Proof that delivered log files were not modified or deleted
- B. Encryption
- C. Faster search
- D. Compression

**Answer: A** — Digest files for tamper evidence.

## Related
- [IAM least privilege](iam-least-privilege.md) — see-also: same checkpoint.
- [Secrets & configuration](secrets-configuration.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
