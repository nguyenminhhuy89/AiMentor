---
id: 20261124-cp6-code-quality-in-ci
title: CP6 · Code quality in CI
tags: [question-bank, cp6]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp6-tracing-datadog-apm, 20261124-cp6-logs-metrics-rum, 20261124-exam-blueprint]
summary: 20 CP6 questions on Code quality in CI (6 easy, 10 medium, 4 hard) with answers and explanations.
---

# CP6 · Code quality in CI

> Summary: 20 CP6 questions on Code quality in CI (6 easy, 10 medium, 4 hard) with answers and explanations.

## Context
Part of the CP6 Quality, Observability & Ops bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP6).

## Questions

### CP6-Q001 · Easy
What does the DoD require for go lint, build and test in CI?

- A. 100% pass rate on every PR
- B. 80% pass rate
- C. Only build must pass
- D. Tests are optional on Fridays

**Answer: A** — Any failure blocks the merge.

### CP6-Q002 · Easy ★
What is code coverage?

- A. The percentage of code executed by tests
- B. The number of linters
- C. The number of tests
- D. The time tests take

**Answer: A** — A signal, not a guarantee of quality.

### CP6-Q003 · Easy
What is the default business-logic coverage threshold in this programme?

- A. 10%
- B. 100% of every file
- C. 50% of generated code
- D. 80%

**Answer: D** — Team threshold, measured on business logic.

### CP6-Q004 · Medium
How can CI fail when coverage drops below the threshold?

- A. Use go vet
- B. It cannot
- C. Use Trivy
- D. Parse go test -coverprofile output (go tool cover -func) and exit non-zero below the threshold

**Answer: D** — Make quality gates automatic.

### CP6-Q005 · Medium ★
Which flag enables race detection in tests?

- A. -cover
- B. -short
- C. -v
- D. -race

**Answer: D** — Run in CI for concurrent code.

### CP6-Q006 · Medium
What does staticcheck find?

- A. YAML errors
- B. IAM issues
- C. Bugs, dead code and simplifications beyond go vet
- D. Docker CVEs

**Answer: C** — Included in golangci-lint.

### CP6-Q007 · Medium
Why exclude generated code from lint and coverage?

- A. It cannot compile
- B. It is not hand-written and would add noise or false signals
- C. Linters crash on it
- D. It is always perfect

**Answer: B** — Configure exclusions in .golangci.yml.

### CP6-Q008 · Medium
What is a flaky test?

- A. A test that sometimes passes and sometimes fails without code changes
- B. A test with a typo
- C. A slow test
- D. A skipped test

**Answer: A** — Fix or quarantine; never ignore.

### CP6-Q009 · Medium
What is the purpose of integration tests with LocalStack in CI?

- A. Replace unit tests
- B. Scan images
- C. Measure UI speed
- D. Verify real AWS API interactions (DynamoDB, SQS, S3) without the cloud

**Answer: D** — Run them after unit tests.

### CP6-Q010 · Hard ★
A PR raises coverage to 85% by testing getters only. What is wrong?

- A. Coverage went up but critical business paths (errors, edge cases) are still untested
- B. Getters cannot be tested
- C. Nothing
- D. Coverage must be 100%

**Answer: A** — Review what is tested, not just the number.

### CP6-Q011 · Hard
Which practice reduces "works on my machine" problems in CI?

- A. Pin tool versions (Go, golangci-lint, oapi-codegen) and run the same make targets locally and in CI
- B. Run CI only weekly
- C. Use latest everywhere
- D. Skip CI for small PRs

**Answer: A** — Reproducibility.

### CP6-Q012 · Easy
What does `go test -short` usually do?

- A. Disables coverage
- B. Shortens test names
- C. Runs only one test
- D. Skips long-running tests that check testing.Short()

**Answer: D** — Useful to separate fast and slow suites.

### CP6-Q013 · Medium
What is a good PR size?

- A. As large as possible
- B. One file per PR always
- C. Small and focused, reviewable in under ~30 minutes
- D. One PR per week

**Answer: C** — Small PRs get better reviews.

### CP6-Q014 · Medium ★
What should a reviewer check besides correctness?

- A. Only formatting
- B. Only commit messages
- C. Tests, error handling, security (secrets/PII), naming and DoD items
- D. Only the PR title

**Answer: C** — Reviews protect quality.

### CP6-Q015 · Hard
Mutation testing measures…

- A. Build speed
- B. Whether tests fail when the code is deliberately changed, revealing weak assertions
- C. Docker size
- D. Line coverage

**Answer: B** — Awareness: stronger than coverage alone.

### CP6-Q016 · Easy ★
Which file configures golangci-lint?

- A. .golangci.yml
- B. lint.json in /etc
- C. .lintrc.go
- D. go.sum

**Answer: A** — Version it with the repo.

### CP6-Q017 · Medium
What is a benchmark in Go?

- A. A Docker metric
- B. A coverage report
- C. A unit test with assertions
- D. func BenchmarkX(b *testing.B) measuring performance

**Answer: D** — Run with go test -bench.

### CP6-Q018 · Hard
How should test data with PII be handled?

- A. Use colleagues' real phone numbers
- B. Use production exports
- C. Use synthetic data only; never copy real customer data into tests or fixtures
- D. Encrypt and commit real data

**Answer: C** — Privacy applies to tests too.

### CP6-Q019 · Medium
What is the benefit of a Makefile (make lint test build)?

- A. One consistent set of commands for developers and CI
- B. It speeds up the compiler
- C. It replaces Go modules
- D. It is required by GitHub

**Answer: A** — Same commands everywhere.

### CP6-Q020 · Easy
What does a green CI badge on main mean?

- A. The latest main build passed all checks
- B. The code has no bugs
- C. Coverage is 100%
- D. The app is deployed

**Answer: A** — Necessary, not sufficient.

## Related
- [Tracing & Datadog APM](tracing-datadog-apm.md) — see-also: same checkpoint.
- [Logs, metrics & RUM](logs-metrics-rum.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
