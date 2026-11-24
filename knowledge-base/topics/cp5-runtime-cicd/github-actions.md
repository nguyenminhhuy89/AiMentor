---
id: 20261124-cp5-github-actions
title: CP5 · GitHub Actions
tags: [question-bank, cp5]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp5-docker, 20261124-cp5-ecs, 20261124-exam-blueprint]
summary: 20 CP5 questions on GitHub Actions (5 easy, 11 medium, 4 hard) with answers and explanations.
---

# CP5 · GitHub Actions

> Summary: 20 CP5 questions on GitHub Actions (5 easy, 11 medium, 4 hard) with answers and explanations.

## Context
Part of the CP5 Runtime, IaC & CI/CD bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP5).

## Questions

### CP5-Q086 · Easy
What is GitHub Actions?

- A. A code editor
- B. GitHub's CI/CD platform running workflows defined in YAML
- C. A Kong plugin
- D. A Git command

**Answer: B** — Workflows live in .github/workflows.

### CP5-Q087 · Easy
What triggers a workflow on every pull request?

- A. on: never
- B. on: release only
- C. on: pull_request
- D. on: schedule only

**Answer: C** — Also on: push for main.

### CP5-Q088 · Easy ★
What is a job?

- A. A Git commit
- B. A single shell command
- C. A Docker image
- D. A set of steps that run on the same runner

**Answer: D** — Jobs can run in parallel or depend on each other.

### CP5-Q089 · Medium ★
What does actions/setup-go do?

- A. Installs a specific Go version (with caching) on the runner
- B. Lints YAML
- C. Deploys to ECS
- D. Creates a Go module

**Answer: A** — Pin the version to match go.mod.

### CP5-Q090 · Medium
What is the CI step order in the DoD pipeline?

- A. push → test → lint
- B. test only
- C. lint → build → test → scan → push
- D. scan → deploy → build

**Answer: C** — Cheap checks first; push only green builds.

### CP5-Q091 · Medium
How should GitHub Actions authenticate to AWS?

- A. The root account
- B. Hardcoded keys in the workflow
- C. Long-lived access keys in repo secrets
- D. OIDC federation with aws-actions/configure-aws-credentials assuming a role

**Answer: D** — No static credentials.

### CP5-Q092 · Medium
What does "needs: build" on a job do?

- A. Makes the job wait for the build job to succeed
- B. Runs in parallel always
- C. Installs dependencies
- D. Caches files

**Answer: A** — Defines job dependencies.

### CP5-Q093 · Medium
How do you make CI required before merging?

- A. Mark the workflow checks as required status checks in branch protection
- B. Add a comment
- C. Name the workflow "required"
- D. Use workflow_dispatch

**Answer: A** — Enforced by GitHub.

### CP5-Q094 · Medium ★
Why cache Go modules in CI?

- A. To reduce coverage
- B. Faster builds by reusing downloaded dependencies
- C. To skip tests
- D. To store secrets

**Answer: B** — setup-go has built-in caching.

### CP5-Q095 · Medium
Where should CI secrets be stored?

- A. In README
- B. GitHub encrypted secrets/environments (and preferably OIDC instead of keys)
- C. In the workflow YAML
- D. In the Docker image

**Answer: B** — Never echo them in logs.

### CP5-Q096 · Hard
Why pin third-party actions to a full commit SHA?

- A. Tags are not allowed
- B. SHAs run faster
- C. It enables caching
- D. To prevent a compromised or retagged action from running malicious code

**Answer: D** — Supply-chain security.

### CP5-Q097 · Hard
Which permission setting reduces risk for workflows?

- A. permissions: write-all
- B. No permissions block ever
- C. Admin token in secrets
- D. Set minimal permissions (e.g. contents: read, id-token: write only where needed)

**Answer: D** — Least privilege for the GITHUB_TOKEN.

### CP5-Q098 · Easy
Where do workflow files live?

- A. .github/workflows/*.yml
- B. /workflows
- C. Dockerfile
- D. .circleci

**Answer: A** — Version-controlled with code.

### CP5-Q099 · Medium
What is a matrix build?

- A. Running the same job across multiple configurations, e.g. Go versions
- B. A Kong route table
- C. A test report
- D. A parallel database

**Answer: A** — Useful for libraries.

### CP5-Q100 · Hard ★
A PR from a fork should not get AWS credentials. Which trigger choice protects you?

- A. Disable CI
- B. Use pull_request (no secrets for forks) and avoid running untrusted code with pull_request_target
- C. Use pull_request_target for everything
- D. Share keys with forks

**Answer: B** — Fork PRs are untrusted input.

### CP5-Q101 · Medium
How can the workflow upload coverage results for reviewers?

- A. Upload as an artifact or post a summary to the job summary/PR
- B. Write to Confluence manually
- C. Email the trainee
- D. Not possible

**Answer: A** — Visibility of quality metrics.

### CP5-Q102 · Easy ★
What does a red X on a PR check mean?

- A. The PR is approved
- B. The PR is merged
- C. The workflow failed and the PR should not be merged
- D. The check is skipped

**Answer: C** — Fix before merging.

### CP5-Q103 · Medium
What does the go generate + git diff step in CI protect?

- A. Docker image size
- B. That generated code matches the contract with zero manual edits
- C. AWS costs
- D. Kong config

**Answer: B** — Module 1 DoD in CI.

### CP5-Q104 · Hard
Where should deployment to the sandbox be triggered from?

- A. A developer laptop
- B. Any feature branch automatically
- C. A protected main branch after CI passes, with an environment and approvals as needed
- D. Pull requests from forks

**Answer: C** — Controlled path to environments.

### CP5-Q105 · Medium
What is the GITHUB_SHA useful for?

- A. Tagging images and artifacts with the exact commit
- B. Naming branches
- C. Encrypting secrets
- D. Choosing Go version

**Answer: A** — Traceability from image to commit.

## Related
- [Docker](docker.md) — see-also: same checkpoint.
- [ECS](ecs.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
