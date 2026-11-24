---
id: 20261124-cp5-ecs
title: CP5 · ECS
tags: [question-bank, cp5]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp5-docker, 20261124-cp5-lambda, 20261124-exam-blueprint]
summary: 20 CP5 questions on ECS (6 easy, 10 medium, 4 hard) with answers and explanations.
---

# CP5 · ECS

> Summary: 20 CP5 questions on ECS (6 easy, 10 medium, 4 hard) with answers and explanations.

## Context
Part of the CP5 Runtime, IaC & CI/CD bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP5).

## Questions

### CP5-Q026 · Easy
What is Amazon ECS?

- A. A managed container orchestration service
- B. A DNS service
- C. A Git server
- D. A database

**Answer: A** — Runs the Order Service containers.

### CP5-Q027 · Easy ★
What is AWS Fargate?

- A. A serverless compute engine for containers — no servers to manage
- B. A load balancer
- C. A Kong plugin
- D. A CI tool

**Answer: A** — ECS on Fargate is the target runtime.

### CP5-Q028 · Easy
What is a task definition?

- A. A Jira task
- B. A running container
- C. A blueprint describing containers, image, CPU/memory, ports, roles and env
- D. A CloudFormation stack

**Answer: C** — Versioned revisions.

### CP5-Q029 · Easy ★
What is an ECS service?

- A. A single container run
- B. A Lambda
- C. A VPC
- D. Keeps a desired number of tasks running and replaces failed ones

**Answer: D** — Also integrates with load balancers.

### CP5-Q030 · Medium
What is the task execution role used for?

- A. CloudFormation deploys
- B. Pulling images from ECR, writing logs and fetching secrets referenced in the task definition
- C. The app's DynamoDB calls
- D. Kong auth

**Answer: B** — App calls use the task role.

### CP5-Q031 · Medium
Which network mode does Fargate use?

- A. bridge
- B. none
- C. awsvpc (each task gets its own ENI and security group)
- D. host

**Answer: C** — Per-task SGs enable least privilege.

### CP5-Q032 · Medium
How does ECS perform a rolling deployment?

- A. Stops all tasks then starts new
- B. Creates a new cluster
- C. Rebuilds the image
- D. Starts new tasks with the new revision and drains old ones per min/max healthy percent

**Answer: D** — Configurable deployment settings.

### CP5-Q033 · Medium
What does the deployment circuit breaker do?

- A. Detects failing deployments and can roll back automatically
- B. Limits API requests
- C. Encrypts tasks
- D. Stops CloudFormation drift

**Answer: A** — Enable with rollback.

### CP5-Q034 · Medium
How do container logs reach CloudWatch or Datadog?

- A. Through Kong
- B. They cannot
- C. By SSH
- D. Via the log driver (awslogs) or FireLens/Datadog agent sidecar

**Answer: D** — Configured in the task definition.

### CP5-Q035 · Medium
What triggers ECS service auto scaling?

- A. Target tracking on metrics like CPU, memory or ALB request count (or SQS backlog via custom metric)
- B. Git commits
- C. Jira tickets
- D. Route 53 TTL

**Answer: A** — Scale on real load signals.

### CP5-Q036 · Hard
Tasks start then stop repeatedly with exit code 1. First place to look?

- A. The container logs and stopped task reason in ECS
- B. Kong config
- C. Route 53
- D. Jira

**Answer: A** — Often missing env/secret or bad config.

### CP5-Q037 · Hard
Why set stopTimeout and handle SIGTERM in Go?

- A. SIGTERM is ignored by ECS
- B. To speed up startup
- C. ECS sends SIGTERM then SIGKILL; graceful shutdown finishes requests/messages
- D. To skip health checks

**Answer: C** — Avoids dropped work during deploys.

### CP5-Q038 · Medium ★
Where are ECS tasks placed per the DoD?

- A. Public subnets with public IPs
- B. Private subnets with security groups allowing only needed traffic
- C. Any subnet
- D. The default VPC

**Answer: B** — Matches the network DoD.

### CP5-Q039 · Easy
Which ECS component defines CPU and memory for Fargate?

- A. The service name
- B. The task definition (task-level cpu/memory)
- C. The cluster
- D. The ECR repo

**Answer: B** — Fargate needs valid CPU/memory combos.

### CP5-Q040 · Medium
What is ECS Exec?

- A. A CI runner
- B. A Kong plugin
- C. A feature to run commands in a running container securely via SSM
- D. SSH access

**Answer: C** — Audited debugging access.

### CP5-Q041 · Hard
Should a consumer reading SQS be a separate ECS service from the HTTP API?

- A. Only on EC2
- B. Never
- C. It must be the same container
- D. Usually yes, so they scale and deploy independently

**Answer: D** — Different workloads, different scaling signals.

### CP5-Q042 · Medium ★
What does the ALB target group health check decide?

- A. Image vulnerabilities
- B. IAM permissions
- C. DNS TTL
- D. Whether a task receives traffic and stays registered

**Answer: D** — Unhealthy targets are drained.

### CP5-Q043 · Easy
Which file in the repo describes the task definition as code?

- A. go.sum
- B. openapi.yaml
- C. README.md
- D. A CloudFormation template (AWS::ECS::TaskDefinition)

**Answer: D** — All infra via CloudFormation.

### CP5-Q044 · Hard ★
Fargate task cannot fetch a Secrets Manager secret at start. Likely cause?

- A. Wrong Go version
- B. Task role lacks dynamodb:PutItem
- C. Kong is down
- D. Execution role lacks secretsmanager:GetSecretValue (and kms:Decrypt) or no network path/endpoint

**Answer: D** — Startup secrets use the execution role.

### CP5-Q045 · Medium
What does desiredCount = 2 across two AZs give you?

- A. No benefit
- B. Basic high availability if one task or AZ fails
- C. Double encryption
- D. Half the cost

**Answer: B** — Spread tasks across AZs.

## Related
- [Docker](docker.md) — see-also: same checkpoint.
- [Lambda](lambda.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
