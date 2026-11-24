---
id: 20261124-cp5-buildkite
title: CP5 · Buildkite
tags: [question-bank, cp5]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp5-docker, 20261124-cp5-ecs, 20261124-exam-blueprint]
summary: 15 CP5 questions on Buildkite (5 easy, 7 medium, 3 hard) with answers and explanations.
---

# CP5 · Buildkite

> Summary: 15 CP5 questions on Buildkite (5 easy, 7 medium, 3 hard) with answers and explanations.

## Context
Part of the CP5 Runtime, IaC & CI/CD bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP5).

## Questions

### CP5-Q106 · Easy
What is Buildkite?

- A. A monitoring tool
- B. A CI/CD platform where pipelines run on your own agents
- C. A container registry
- D. A Git host

**Answer: B** — Used for deployment pipelines here.

### CP5-Q107 · Easy
Where does a Buildkite pipeline usually get its steps?

- A. A Jira ticket
- B. A pipeline.yml in the repo (e.g. .buildkite/pipeline.yml)
- C. go.mod
- D. The Buildkite UI only

**Answer: B** — Pipelines as code.

### CP5-Q108 · Easy ★
What is a Buildkite agent?

- A. A small program on your infrastructure that runs pipeline jobs
- B. A user account
- C. A plugin marketplace
- D. A Docker image registry

**Answer: A** — Agents can run in your AWS account.

### CP5-Q109 · Medium
What does a block step do?

- A. Runs steps in parallel
- B. Pauses the pipeline until someone manually unblocks it (approval gate)
- C. Deletes the build
- D. Blocks all builds forever

**Answer: B** — DoD: manual gate before deploy.

### CP5-Q110 · Medium
What does a wait step do?

- A. Sleeps for 60 seconds
- B. Waits for a Git push
- C. Pauses for approval
- D. Waits for all previous steps to pass before continuing

**Answer: D** — Separates stages.

### CP5-Q111 · Medium
Why run Buildkite agents inside your own AWS account?

- A. They are faster than any SaaS
- B. They can use IAM roles to deploy without exposing credentials externally
- C. They are mandatory
- D. They avoid IAM

**Answer: B** — Elastic CI Stack for AWS is common.

### CP5-Q112 · Medium ★
How do you pass the image tag from CI to the deploy step?

- A. Re-build the image in deploy
- B. Use build metadata or an artifact (e.g. buildkite-agent meta-data set image_tag)
- C. Email it
- D. Hardcode latest

**Answer: B** — Promote the same artifact.

### CP5-Q113 · Medium
Why promote the same image from sandbox to later environments instead of rebuilding?

- A. It is required by ECS
- B. Images cannot be copied
- C. Rebuilding is not allowed
- D. Guarantees what was tested is what is deployed

**Answer: D** — Build once, deploy many.

### CP5-Q114 · Hard
How should secrets be provided to Buildkite steps?

- A. In build messages
- B. In the repo
- C. In pipeline.yml env
- D. Through agent-side secret hooks/Secrets Manager, not in pipeline.yml

**Answer: D** — Keep secrets out of version control.

### CP5-Q115 · Medium
What are Buildkite plugins used for?

- A. Kong routing
- B. Reusable step behavior, e.g. Docker or ECR login
- C. IAM policies
- D. Database migrations only

**Answer: B** — Pin plugin versions.

### CP5-Q116 · Easy ★
What is the difference in roles between GitHub Actions and Buildkite in this bootcamp?

- A. GitHub Actions runs PR CI checks; Buildkite runs the deploy pipeline with an approval gate
- B. They do exactly the same
- C. GitHub Actions runs Kong
- D. Buildkite hosts code

**Answer: A** — Each tool has a clear job.

### CP5-Q117 · Hard ★
A deploy step fails after the block step. What should happen?

- A. The pipeline stops; ECS circuit breaker/CloudFormation rollback restores the last good version and the team investigates
- B. Unblock again repeatedly
- C. Keep deploying other steps
- D. Delete the stack

**Answer: A** — Safe failure path.

### CP5-Q118 · Medium
What does "concurrency" with a concurrency group do in Buildkite?

- A. Caches builds
- B. Encrypts jobs
- C. Limits how many jobs of a group run at once, e.g. one deploy at a time
- D. Runs all jobs in parallel

**Answer: C** — Prevents overlapping deploys.

### CP5-Q119 · Hard
How do you make deployments auditable?

- A. Skip approvals
- B. Each deploy records commit, image tag, approver and time in the pipeline and links to the Jira issue
- C. Delete build logs
- D. Deploy from laptops

**Answer: B** — Traceability end to end.

### CP5-Q120 · Easy
Which step type is used to require human approval before production-like deploys?

- A. wait
- B. block
- C. command
- D. trigger

**Answer: B** — block/input steps gate progress.

## Related
- [Docker](docker.md) — see-also: same checkpoint.
- [ECS](ecs.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
