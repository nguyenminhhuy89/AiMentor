---
id: 20261124-cp0-github-copilot
title: CP0 · GitHub Copilot
tags: [question-bank, cp0]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp0-git-github-flow, 20261124-cp0-jira-confluence, 20261124-exam-blueprint]
summary: 15 CP0 questions on GitHub Copilot (5 easy, 7 medium, 3 hard) with answers and explanations.
---

# CP0 · GitHub Copilot

> Summary: 15 CP0 questions on GitHub Copilot (5 easy, 7 medium, 3 hard) with answers and explanations.

## Context
Part of the CP0 Onboarding & Go essentials bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP0).

## Questions

### CP0-Q021 · Easy
What is GitHub Copilot?

- A. A GitHub plan for private repositories
- B. A CI/CD service for GitHub
- C. An AI pair programmer that suggests code in the editor
- D. A static code analyzer for Go only

**Answer: C** — Copilot generates suggestions; you remain responsible for the code.

### CP0-Q022 · Easy
The bootcamp rule for Copilot-generated code is…

- A. Copilot is forbidden in labs
- B. You may use it, but you must be able to explain every line you commit
- C. Only mentors may use Copilot
- D. Copilot code never needs review

**Answer: B** — AI-first, not AI-only: understanding is checked in oral review.

### CP0-Q023 · Easy ★
Which input usually improves Copilot suggestions the most?

- A. A longer file name
- B. A clear function name, comment or test describing the intent
- C. Turning off syntax highlighting
- D. Writing code without any comments

**Answer: B** — Copilot uses surrounding context to infer intent.

### CP0-Q024 · Medium
What is a good "test-first" Copilot workflow?

- A. Skip tests because Copilot is accurate
- B. Ask Copilot for the whole service and commit it
- C. Write the table-driven test cases, then let Copilot propose the implementation and verify with go test
- D. Let Copilot write tests after merging

**Answer: C** — Tests define the behavior and catch wrong suggestions.

### CP0-Q025 · Medium ★
Copilot suggests code that hardcodes an API key. What should you do?

- A. Accept it and add a TODO
- B. Accept it because it compiles
- C. Reject it and load the secret from Secrets Manager or environment config
- D. Commit it to a private branch only

**Answer: C** — Hardcoded secrets violate the Definition of Done.

### CP0-Q026 · Medium
Copilot Chat is most useful for…

- A. Explaining unfamiliar code, proposing refactors and generating test cases
- B. Approving pull requests automatically
- C. Replacing code review
- D. Deploying to AWS

**Answer: A** — Use chat to learn and draft, then verify.

### CP0-Q027 · Medium
Why must you review Copilot output for Go error handling?

- A. Copilot cannot write Go
- B. Go has no errors
- C. Copilot always panics on errors
- D. It may ignore returned errors or wrap them incorrectly

**Answer: D** — Unchecked errors are a common AI-generated bug.

### CP0-Q028 · Medium
Which file should NOT be generated or edited by hand or by Copilot in this project?

- A. *_test.go files
- B. Code produced by oapi-codegen
- C. openapi.yaml
- D. README.md

**Answer: B** — Generated code must have zero manual edits; change the contract and regenerate.

### CP0-Q029 · Hard
Copilot proposes a function copied verbatim from a public repo with an unknown license. Best action?

- A. Accept it if it passes tests
- B. Do not accept it blindly; rewrite or verify the license and enable duplicate-detection filtering
- C. Accept it, public code is free to use
- D. Rename variables so it looks different

**Answer: B** — Licensing and originality matter; Copilot offers a public-code filter.

### CP0-Q030 · Easy ★
What does pressing Tab usually do with a Copilot inline suggestion?

- A. Accepts the suggestion
- B. Opens Copilot Chat
- C. Runs the tests
- D. Rejects the suggestion

**Answer: A** — Tab accepts, Esc dismisses.

### CP0-Q031 · Medium
You do not understand a Copilot suggestion. What is the right next step?

- A. Ask Copilot Chat or the tutor to explain it, then write a test for it
- B. Disable Copilot permanently
- C. Commit it and ask later
- D. Delete the whole file

**Answer: A** — Never commit code you cannot explain.

### CP0-Q032 · Hard ★
What is the main risk of pasting production logs with customer data into an AI chat?

- A. The logs become read-only
- B. Leaking PII to a third-party service
- C. The chat becomes slower
- D. Copilot stops suggesting code

**Answer: B** — Never share secrets or PII with AI tools.

### CP0-Q033 · Easy
Copilot suggestions are best treated as…

- A. Official Go documentation
- B. Guaranteed-correct code
- C. Security-approved code
- D. A draft written by a fast but fallible teammate

**Answer: D** — Always review, test and understand.

### CP0-Q034 · Medium
Which prompt is most likely to give a useful Gin handler?

- A. "make it work"
- B. "handler please"
- C. "write code"
- D. "Gin handler for POST /orders that binds CreateOrderRequest, calls svc.Create and returns 201 or RFC 7807 error"

**Answer: D** — Specific inputs, outputs and error behavior guide the model.

### CP0-Q035 · Hard
Copilot keeps suggesting `interface{}` everywhere. What is the better fix?

- A. Switch off Go modules
- B. Accept interface{} for flexibility
- C. Use reflection for all data
- D. Define concrete types (or generated models) and let Copilot follow them

**Answer: D** — Strong types make code safer and suggestions better.

## Related
- [Git & GitHub flow](git-github-flow.md) — see-also: same checkpoint.
- [Jira & Confluence](jira-confluence.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
