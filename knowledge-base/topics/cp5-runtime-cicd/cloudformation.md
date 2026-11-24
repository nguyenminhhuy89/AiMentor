---
id: 20261124-cp5-cloudformation
title: CP5 · CloudFormation
tags: [question-bank, cp5]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp5-docker, 20261124-cp5-ecs, 20261124-exam-blueprint]
summary: 25 CP5 questions on CloudFormation (6 easy, 13 medium, 6 hard) with answers and explanations.
---

# CP5 · CloudFormation

> Summary: 25 CP5 questions on CloudFormation (6 easy, 13 medium, 6 hard) with answers and explanations.

## Context
Part of the CP5 Runtime, IaC & CI/CD bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP5).

## Questions

### CP5-Q061 · Easy ★
What is AWS CloudFormation?

- A. A CI/CD service
- B. Infrastructure as code: templates that create and manage AWS resources as stacks
- C. A container runtime
- D. A monitoring tool

**Answer: B** — DoD: 100% of infra via CloudFormation.

### CP5-Q062 · Easy
What is a stack?

- A. A set of resources created and managed together from one template
- B. A Jira board
- C. A Go call stack
- D. A Docker layer

**Answer: A** — Update and delete as one unit.

### CP5-Q063 · Easy
Which template section declares the AWS resources?

- A. Resources
- B. Outputs
- C. Mappings
- D. Parameters

**Answer: A** — The only required section.

### CP5-Q064 · Easy
What are Parameters for?

- A. Secret values in plain text
- B. Outputs of resources
- C. IAM users
- D. Inputs that customize a template per environment

**Answer: D** — e.g. EnvName, ImageTag.

### CP5-Q065 · Medium
What does !Ref do?

- A. Creates a reference document
- B. Imports a file
- C. Deletes a resource
- D. Returns the value of a parameter or the default identifier of a resource

**Answer: D** — e.g. !Ref OrdersTable returns the table name.

### CP5-Q066 · Medium
What does !GetAtt return?

- A. A Git attribute
- B. A parameter value
- C. A specific attribute of a resource, e.g. a table's Arn
- D. A tag

**Answer: C** — !GetAtt OrdersTable.Arn.

### CP5-Q067 · Medium
What are Outputs used for?

- A. Defining resources
- B. Running tests
- C. Exposing values like queue URLs, optionally exported for other stacks
- D. Storing secrets

**Answer: C** — Cross-stack references with Export/ImportValue.

### CP5-Q068 · Medium
What is a change set?

- A. A Git diff
- B. A Lambda version
- C. A preview of the changes a stack update will make before executing it
- D. A rollback

**Answer: C** — Review replacements before applying.

### CP5-Q069 · Medium ★
What is stack drift?

- A. A failed rollback
- B. Differences between the deployed resources and the template due to manual changes
- C. A template syntax error
- D. A slow deploy

**Answer: B** — DoD: zero drift.

### CP5-Q070 · Medium
How do you check for drift?

- A. Count resources
- B. Run go vet
- C. Check Kong logs
- D. Run DetectStackDrift and review drift status per resource

**Answer: D** — Fix by updating the template, not the console.

### CP5-Q071 · Medium
What happens when a stack update fails?

- A. It ignores the error
- B. Resources are deleted
- C. CloudFormation rolls back to the last known good state by default
- D. It retries forever

**Answer: C** — Read the events to find the cause.

### CP5-Q072 · Medium ★
Which tool lints CloudFormation templates in CI?

- A. cfn-lint
- B. Trivy only
- C. golangci-lint
- D. Spectral

**Answer: A** — Catch errors before deploy.

### CP5-Q073 · Hard
Some property changes cause "Replacement". Why is that dangerous for a DynamoDB table?

- A. A new table is created and the old one deleted, losing data unless protected
- B. It is faster
- C. Nothing happens
- D. It saves cost

**Answer: A** — Use DeletionPolicy/UpdateReplacePolicy: Retain and review change sets.

### CP5-Q074 · Hard ★
What does DeletionPolicy: Retain do?

- A. Retains old versions of code
- B. Keeps the resource when it is removed from the stack or the stack is deleted
- C. Deletes faster
- D. Encrypts the resource

**Answer: B** — Protects stateful resources.

### CP5-Q075 · Hard
Someone changed a security group rule in the console. Correct fix per DoD?

- A. Delete the stack
- B. Document it in Confluence only
- C. Leave it
- D. Update the template (or revert the manual change) and redeploy so drift returns to zero

**Answer: D** — Template is the source of truth.

### CP5-Q076 · Easy ★
Which file formats can templates use?

- A. XML
- B. Go
- C. YAML or JSON
- D. HCL

**Answer: C** — YAML is more readable.

### CP5-Q077 · Medium ★
What does the AWS::SQS::Queue RedrivePolicy property set?

- A. Visibility timeout
- B. Encryption
- C. The DLQ ARN and maxReceiveCount
- D. FIFO mode

**Answer: C** — DLQs as code.

### CP5-Q078 · Medium
What is a nested stack?

- A. A Docker layer
- B. A stack in another region
- C. A stack created as a resource inside another stack to modularize templates
- D. A failed stack

**Answer: C** — Reuse common components.

### CP5-Q079 · Hard
Why pass the image tag as a parameter instead of hardcoding it?

- A. The pipeline can deploy each new commit SHA without editing the template
- B. Hardcoding is illegal
- C. It speeds up ECS
- D. Parameters are encrypted

**Answer: A** — Immutable tags flow through the pipeline.

### CP5-Q080 · Medium
What are stack policies used for?

- A. Kong routing
- B. IAM user policies
- C. Rate limiting
- D. Preventing updates to critical resources during stack updates

**Answer: D** — Extra protection for prod.

### CP5-Q081 · Hard
Which permission model is safer for the pipeline deploying stacks?

- A. Root user
- B. Admin keys on the CI server
- C. The trainee's personal role
- D. A CloudFormation service role with scoped permissions passed via iam:PassRole

**Answer: D** — Least privilege for deployments.

### CP5-Q082 · Easy
Which command deploys a template from the CLI?

- A. aws stack up
- B. aws cloudformation deploy --template-file ... --stack-name ...
- C. cfn apply
- D. aws cfn run

**Answer: B** — deploy creates or updates via change sets.

### CP5-Q083 · Medium
What does the Conditions section allow?

- A. Choosing regions automatically
- B. Running tests
- C. Branching Git
- D. Creating resources or setting properties only for certain environments

**Answer: D** — e.g. IsProd.

### CP5-Q084 · Hard
What does "100% of infrastructure managed via CloudFormation" exclude?

- A. Nothing created by hand in the console for the service, except bootstrap items explicitly documented
- B. Only networking
- C. Everything in the sandbox
- D. Only IAM roles

**Answer: A** — Manual resources must be imported or recreated.

### CP5-Q085 · Medium
What does !Sub do?

- A. Creates a subnet
- B. Subscribes to SNS
- C. Substitutes variables into a string, e.g. "arn:aws:sqs:${AWS::Region}:${AWS::AccountId}:orders"
- D. Subtracts numbers

**Answer: C** — Pseudo parameters help build ARNs.

## Related
- [Docker](docker.md) — see-also: same checkpoint.
- [ECS](ecs.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
