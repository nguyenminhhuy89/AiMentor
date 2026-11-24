---
id: 20261124-cp2-aws-fundamentals-iam-basics
title: CP2 · AWS fundamentals & IAM basics
tags: [question-bank, cp2]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp2-aws-sdk-for-go-v2, 20261124-cp2-s3, 20261124-exam-blueprint]
summary: 20 CP2 questions on AWS fundamentals & IAM basics (8 easy, 8 medium, 4 hard) with answers and explanations.
---

# CP2 · AWS fundamentals & IAM basics

> Summary: 20 CP2 questions on AWS fundamentals & IAM basics (8 easy, 8 medium, 4 hard) with answers and explanations.

## Context
Part of the CP2 Data & Encryption bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP2).

## Questions

### CP2-Q001 · Easy
What is an AWS Region?

- A. A separate geographic area containing multiple Availability Zones
- B. A single data center
- C. A VPC subnet
- D. An IAM group

**Answer: A** — e.g. ap-southeast-1 (Singapore).

### CP2-Q002 · Easy
What is an Availability Zone?

- A. A country
- B. A CloudFormation stack
- C. A DNS record
- D. One or more isolated data centers within a Region

**Answer: D** — Deploy across AZs for resilience.

### CP2-Q003 · Easy ★
What is an IAM role?

- A. A permanent user with a password
- B. A security group
- C. An identity with permissions that is assumed temporarily by services or users
- D. A billing account

**Answer: C** — Roles issue temporary credentials.

### CP2-Q004 · Easy ★
Why should an ECS task use an IAM role instead of access keys?

- A. ECS cannot read environment variables
- B. Roles give short-lived, automatically rotated credentials with no secrets in code
- C. Access keys are faster
- D. Roles are free and keys are not

**Answer: B** — Never bake keys into containers.

### CP2-Q005 · Easy
What is an IAM policy?

- A. A VPC route
- B. A JSON document that allows or denies actions on resources
- C. A password rule only
- D. A Lambda trigger

**Answer: B** — Effect, Action, Resource, Condition.

### CP2-Q006 · Easy
Which file stores named AWS CLI profiles locally?

- A. /etc/hosts
- B. .gitignore
- C. go.mod
- D. ~/.aws/config and ~/.aws/credentials

**Answer: D** — aws configure --profile sandbox.

### CP2-Q007 · Medium
In IAM, when an explicit Deny and an Allow both match, the result is…

- A. Random
- B. Deny
- C. The newest policy wins
- D. Allow

**Answer: B** — Explicit deny always wins.

### CP2-Q008 · Medium ★
What is the default for any action not explicitly allowed?

- A. Allowed for read actions
- B. Allowed
- C. Implicitly denied
- D. Logged but allowed

**Answer: C** — IAM is deny-by-default.

### CP2-Q009 · Medium
What does an ARN identify?

- A. A Docker image tag
- B. A specific AWS resource uniquely
- C. An account password
- D. A region name only

**Answer: B** — arn:aws:dynamodb:region:account:table/Orders.

### CP2-Q010 · Medium
Which command shows which identity your CLI is using?

- A. aws configure list-users
- B. aws iam whoami
- C. aws s3 ls
- D. aws sts get-caller-identity

**Answer: D** — Always check before running commands on a shared account.

### CP2-Q011 · Medium
What is a permissions boundary in the sandbox account?

- A. A maximum permission limit that identity policies cannot exceed
- B. An S3 bucket policy
- C. A network firewall
- D. A billing alarm

**Answer: A** — It keeps trainees safe even if they write broad policies.

### CP2-Q012 · Medium
Why practice on LocalStack first?

- A. It has more services than AWS
- B. It is free, fast and cannot break shared cloud resources
- C. It is the production environment
- D. It removes the need for IAM

**Answer: B** — Then move to the sandbox account.

### CP2-Q013 · Hard
A trainee asks to share their AWS access key in chat so a mentor can debug. Correct response?

- A. Share it but rotate next week
- B. Share it in a private message
- C. Post it in Confluence
- D. Refuse; never share keys — the mentor uses their own role or a screen share

**Answer: D** — Credentials are personal and must stay secret.

### CP2-Q014 · Hard
What does STS AssumeRole return?

- A. A new AWS account
- B. A permanent IAM user
- C. Temporary access key, secret key and session token with an expiry
- D. An encryption key

**Answer: C** — The SDK refreshes these automatically.

### CP2-Q015 · Easy
Which AWS service records API calls for auditing?

- A. Amazon CloudWatch Logs only
- B. Amazon SQS
- C. AWS CloudTrail
- D. AWS KMS

**Answer: C** — Covered more in Module 4.

### CP2-Q016 · Medium ★
Shared responsibility model: who encrypts your application's PII fields?

- A. Kong
- B. Nobody needs to
- C. AWS automatically for every field
- D. You (the customer), e.g. with KMS

**Answer: D** — AWS secures the cloud; you secure what you put in it.

### CP2-Q017 · Medium
What is the purpose of resource tagging (e.g. owner, env)?

- A. Cost allocation, ownership and automation
- B. Versioning code
- C. Encryption
- D. Routing traffic

**Answer: A** — Tag everything in the sandbox with your trainee ID.

### CP2-Q018 · Hard
Least privilege for the Order Service on DynamoDB means…

- A. Read-only on all tables
- B. AdministratorAccess
- C. dynamodb:* on *
- D. Only the needed actions (GetItem, PutItem, Query, UpdateItem) on the Orders table ARN

**Answer: D** — Scope actions and resources.

### CP2-Q019 · Easy
What is the AWS free tier relevant to trainees?

- A. Only EC2 is free
- B. Everything is free forever
- C. Free tier disables billing
- D. Some services have limited free usage, but the sandbox can still incur cost — clean up resources

**Answer: D** — Delete what you create.

### CP2-Q020 · Hard ★
Why should trainees never use the root user?

- A. Root has no MFA
- B. Root is slower
- C. Root has unrestricted access and cannot be limited by IAM policies
- D. Root cannot use the CLI

**Answer: C** — Use IAM roles/SSO; lock root with MFA.

## Related
- [AWS SDK for Go v2](aws-sdk-for-go-v2.md) — see-also: same checkpoint.
- [S3](s3.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
