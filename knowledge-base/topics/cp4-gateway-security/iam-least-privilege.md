---
id: 20261124-cp4-iam-least-privilege
title: CP4 · IAM least privilege
tags: [question-bank, cp4]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp4-secrets-configuration, 20261124-cp4-vpc-subnets-security-groups, 20261124-exam-blueprint]
summary: 20 CP4 questions on IAM least privilege (6 easy, 9 medium, 5 hard) with answers and explanations.
---

# CP4 · IAM least privilege

> Summary: 20 CP4 questions on IAM least privilege (6 easy, 9 medium, 5 hard) with answers and explanations.

## Context
Part of the CP4 Gateway, Network & Security bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP4).

## Questions

### CP4-Q001 · Easy ★
What does "least privilege" mean?

- A. Use one role for all services
- B. Grant read access to everything
- C. Grant admin to avoid errors
- D. Grant only the permissions needed for the task, on only the needed resources

**Answer: D** — DoD: least-privilege IAM enforced.

### CP4-Q002 · Easy
Which part of an IAM statement lists API calls like dynamodb:GetItem?

- A. Principal
- B. Effect
- C. Resource
- D. Action

**Answer: D** — Action + Resource + Effect (+ Condition).

### CP4-Q003 · Easy
Which policy statement is a red flag for least privilege?

- A. "Effect": "Deny" on delete actions
- B. A Condition on aws:SourceArn
- C. "Action": "*", "Resource": "*"
- D. "Action": "sqs:SendMessage" on one queue ARN

**Answer: C** — Wildcards on both are effectively admin.

### CP4-Q004 · Easy
What is a trust policy on a role?

- A. It lists allowed S3 buckets
- B. It configures MFA
- C. It sets the password policy
- D. It defines which principals may assume the role

**Answer: D** — e.g. ecs-tasks.amazonaws.com may assume the task role.

### CP4-Q005 · Medium
ECS has two roles. Which one does the application code use to call DynamoDB?

- A. The task execution role
- B. The EC2 instance profile always
- C. The task role
- D. The CloudFormation service role

**Answer: C** — Execution role pulls images and writes logs; task role is for app calls.

### CP4-Q006 · Medium
What does the Condition element allow?

- A. Changing the action name
- B. Creating users
- C. Logging requests
- D. Restricting when a statement applies, e.g. by source ARN, tags or encryption context

**Answer: D** — Fine-grained control.

### CP4-Q007 · Medium
What is IAM Access Analyzer useful for?

- A. Encrypting S3
- B. Finding resources shared externally and generating least-privilege policies from activity
- C. Deploying code
- D. Scanning Docker images

**Answer: B** — Helps tighten policies.

### CP4-Q008 · Medium ★
Why should each service have its own role?

- A. AWS requires it
- B. To speed up calls
- C. Roles are free so use many
- D. Compromise or bug in one service cannot use another service's permissions

**Answer: D** — Blast-radius reduction.

### CP4-Q009 · Medium ★
What does sts:AssumeRole with an external ID protect against?

- A. The confused deputy problem with third parties
- B. SQL injection
- C. Brute-force passwords
- D. DDoS attacks

**Answer: A** — Awareness level.

### CP4-Q010 · Medium
An inline policy vs a managed policy: which is reusable across roles?

- A. Neither
- B. Customer managed policy
- C. Both equally
- D. Inline policy

**Answer: B** — Inline policies belong to one identity.

### CP4-Q011 · Hard ★
Which policy allows only reading one secret?

- A. Allow secretsmanager:* on *
- B. Allow kms:* on *
- C. Allow ssm:* on *
- D. Allow secretsmanager:GetSecretValue on arn:...:secret:order-service/db-*

**Answer: D** — Scope to the secret ARN prefix.

### CP4-Q012 · Hard
How do you verify a policy allows exactly what you intend before deploying?

- A. Ask Copilot
- B. Use the IAM policy simulator / access analyzer checks and test with the role in the sandbox
- C. Deploy to production and see
- D. Trust the template

**Answer: B** — Validate, then test.

### CP4-Q013 · Hard
A Lambda needs to read from SQS and write to DynamoDB Orders. Which is least privilege?

- A. AmazonSQSFullAccess + AmazonDynamoDBFullAccess
- B. AdministratorAccess
- C. AWSLambdaFullAccess
- D. sqs:ReceiveMessage/DeleteMessage/GetQueueAttributes on the queue ARN and dynamodb:PutItem/UpdateItem on the table ARN

**Answer: D** — Managed full-access policies are too broad.

### CP4-Q014 · Easy
Can IAM policies be stored in CloudFormation?

- A. No
- B. Only in JSON files outside Git
- C. Only in the console
- D. Yes, as part of AWS::IAM::Role/Policy resources

**Answer: D** — IaC makes them reviewable.

### CP4-Q015 · Medium
What is a service control policy (SCP)?

- A. An Organization-level guardrail limiting what accounts can do
- B. An S3 bucket policy
- C. A CloudWatch alarm
- D. A Kong plugin

**Answer: A** — Awareness: guardrails above IAM.

### CP4-Q016 · Hard
Why use aws:SourceArn conditions in resource policies (e.g. SQS allowing SNS)?

- A. It is cosmetic
- B. To encrypt messages
- C. To speed up delivery
- D. To allow only the specific topic, not any SNS topic

**Answer: D** — Prevents other principals abusing the service permission.

### CP4-Q017 · Medium
Which is better for human access to the sandbox account?

- A. AWS IAM Identity Center (SSO) with short-lived role sessions
- B. Shared IAM user with a password in Confluence
- C. Long-lived access keys in email
- D. Root user

**Answer: A** — Federated, auditable, temporary.

### CP4-Q018 · Easy ★
What does MFA add?

- A. A second factor so a stolen password alone is not enough
- B. Faster login
- C. Encryption at rest
- D. More permissions

**Answer: A** — Enable on all human identities.

### CP4-Q019 · Hard
A pipeline role needs to deploy CloudFormation but should not be able to escalate privileges. Key control?

- A. Use root keys
- B. Give iam:*
- C. Allow iam:CreateUser
- D. Restrict iam:PassRole to specific role ARNs

**Answer: D** — PassRole abuse is a common escalation path.

### CP4-Q020 · Medium
What does "Effect": "Deny" with "dynamodb:DeleteTable" achieve?

- A. Nothing
- B. Blocks table deletion even if another policy allows it
- C. Allows deletion
- D. Logs deletion only

**Answer: B** — Explicit deny wins.

## Related
- [Secrets & configuration](secrets-configuration.md) — see-also: same checkpoint.
- [VPC, subnets & security groups](vpc-subnets-security-groups.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
