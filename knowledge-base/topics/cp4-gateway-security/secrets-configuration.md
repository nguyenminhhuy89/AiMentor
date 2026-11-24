---
id: 20261124-cp4-secrets-configuration
title: CP4 · Secrets & configuration
tags: [question-bank, cp4]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp4-iam-least-privilege, 20261124-cp4-vpc-subnets-security-groups, 20261124-exam-blueprint]
summary: 20 CP4 questions on Secrets & configuration (6 easy, 9 medium, 5 hard) with answers and explanations.
---

# CP4 · Secrets & configuration

> Summary: 20 CP4 questions on Secrets & configuration (6 easy, 9 medium, 5 hard) with answers and explanations.

## Context
Part of the CP4 Gateway, Network & Security bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP4).

## Questions

### CP4-Q021 · Easy ★
Which service is meant for credentials like DB passwords with rotation?

- A. AWS Secrets Manager
- B. Parameter Store standard parameters
- C. AWS AppConfig
- D. S3

**Answer: A** — Secrets Manager supports automatic rotation.

### CP4-Q022 · Easy ★
Which service fits plain configuration values like table names?

- A. KMS
- B. SSM Parameter Store
- C. CloudTrail
- D. Secrets Manager

**Answer: B** — Cheap hierarchical config.

### CP4-Q023 · Easy
Which service fits feature flags changed at runtime with safe rollout?

- A. AWS AppConfig
- B. Parameter Store only
- C. Route 53
- D. Secrets Manager

**Answer: A** — AppConfig adds validation and deployment strategies.

### CP4-Q024 · Easy
What does "zero hardcoded secrets" mean in the DoD?

- A. Secrets in environment files committed to Git are OK
- B. Only production secrets matter
- C. Secrets must be short
- D. No passwords, keys or tokens in code, images, config files or Git history

**Answer: D** — Secret scanning must be clean.

### CP4-Q025 · Medium
What is a SecureString parameter?

- A. A Docker secret
- B. A Parameter Store value encrypted with KMS
- C. A Kong credential
- D. A Secrets Manager secret

**Answer: B** — Fine for small sensitive config without rotation needs.

### CP4-Q026 · Medium
How should ECS inject a DB password?

- A. Pass it as a command-line flag in Git
- B. Bake it into the image
- C. Reference the Secrets Manager ARN in the task definition secrets section
- D. Put it in the Dockerfile ENV

**Answer: C** — ECS fetches at start using the execution role.

### CP4-Q027 · Medium
Why cache secrets in the service rather than fetching on every request?

- A. Caching is more secure
- B. Secrets never change
- C. AWS requires it
- D. Avoids latency, cost and throttling; refresh periodically for rotation

**Answer: D** — Use a TTL cache.

### CP4-Q028 · Medium
What does an AppConfig deployment strategy control?

- A. Docker build speed
- B. How fast a configuration change rolls out and when it bakes before completing
- C. IAM rotation
- D. Route 53 TTL

**Answer: B** — Gradual rollout with rollback on alarm.

### CP4-Q029 · Medium ★
Which tool can detect secrets in Git history in CI?

- A. golangci-lint
- B. Trivy only for images
- C. gitleaks (or trufflehog)
- D. cfn-lint

**Answer: C** — Secret scanning is a DoD check.

### CP4-Q030 · Medium
Which naming helps scope parameters per service and environment?

- A. config1
- B. /order-service/sandbox/table-name
- C. tableName
- D. prod

**Answer: B** — Hierarchies enable path-based IAM.

### CP4-Q031 · Hard
A secret was committed and pushed. Correct order of actions?

- A. Delete the file only
- B. Rename the variable
- C. Rotate/revoke the secret, then remove it from history and add scanning to prevent recurrence
- D. Make the repo private

**Answer: C** — Assume it is compromised immediately.

### CP4-Q032 · Hard
How does AppConfig protect against a bad config change?

- A. It deletes the old config
- B. It encrypts the change
- C. Validators (JSON Schema/Lambda) and automatic rollback on CloudWatch alarms
- D. It cannot

**Answer: C** — Safe config deployment.

### CP4-Q033 · Hard ★
Why is putting secrets in plain ECS environment variables (not the secrets field) a risk?

- A. They are slower
- B. ECS rejects them
- C. They are visible in the task definition to anyone who can describe it
- D. They are encrypted twice

**Answer: C** — Use the secrets field or fetch at runtime.

### CP4-Q034 · Easy
Which file should never be committed to Git?

- A. .env files with real credentials
- B. README.md
- C. openapi.yaml
- D. go.mod

**Answer: A** — Add .env to .gitignore.

### CP4-Q035 · Medium
Parameter Store vs Secrets Manager cost and features: which statement is true?

- A. They are identical
- B. Secrets Manager is free
- C. Secrets Manager costs per secret and offers rotation; Parameter Store standard is cheaper without native rotation
- D. Parameter Store has built-in rotation for RDS

**Answer: C** — Choose by scope.

### CP4-Q036 · Medium ★
What IAM permission lets the service read a SecureString?

- A. kms:CreateKey
- B. ssm:* only
- C. secretsmanager:GetSecretValue
- D. ssm:GetParameter on the parameter plus kms:Decrypt on its key

**Answer: D** — Both are needed for SecureString.

### CP4-Q037 · Hard
Where should feature flag defaults live if AppConfig is unreachable?

- A. Enable all features
- B. Safe in-code defaults with the last known good config cached
- C. Crash the service
- D. Disable the service

**Answer: B** — Fail safe.

### CP4-Q038 · Easy
Which is a secret?

- A. A third-party API key
- B. The AWS region
- C. The log level
- D. The DynamoDB table name

**Answer: A** — Names and regions are config, not secrets.

### CP4-Q039 · Medium
What is secret rotation?

- A. Copying secrets to S3
- B. Encrypting secrets twice
- C. Periodically replacing credentials so leaked old values stop working
- D. Renaming secrets

**Answer: C** — Secrets Manager can rotate RDS credentials.

### CP4-Q040 · Hard
What should logs do with configuration values at startup?

- A. Log secrets at debug level
- B. Log every value for debugging
- C. Log nothing ever
- D. Log non-sensitive config only and redact secrets

**Answer: D** — Redaction prevents leaks into Datadog.

## Related
- [IAM least privilege](iam-least-privilege.md) — see-also: same checkpoint.
- [VPC, subnets & security groups](vpc-subnets-security-groups.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
