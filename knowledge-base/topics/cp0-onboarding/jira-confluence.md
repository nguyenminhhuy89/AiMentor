---
id: 20261124-cp0-jira-confluence
title: CP0 · Jira & Confluence
tags: [question-bank, cp0]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp0-git-github-flow, 20261124-cp0-github-copilot, 20261124-exam-blueprint]
summary: 15 CP0 questions on Jira & Confluence (6 easy, 7 medium, 2 hard) with answers and explanations.
---

# CP0 · Jira & Confluence

> Summary: 15 CP0 questions on Jira & Confluence (6 easy, 7 medium, 2 hard) with answers and explanations.

## Context
Part of the CP0 Onboarding & Go essentials bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP0).

## Questions

### CP0-Q036 · Easy ★
In Jira, what is an issue?

- A. A unit of work such as a story, task or bug
- B. A Slack channel
- C. A Confluence page
- D. A Git branch

**Answer: A** — Issues are tracked on boards and linked to commits.

### CP0-Q037 · Easy
Where should a trainee write the daily learning log?

- A. In the Go source code
- B. Jira comment on a random ticket
- C. In the Git commit hash
- D. Confluence

**Answer: D** — The bootcamp keeps a Confluence log per trainee.

### CP0-Q038 · Easy
What does a Jira board column like "In Progress" represent?

- A. The sprint number
- B. The assignee's team
- C. The issue priority
- D. A workflow status of the issue

**Answer: D** — Columns map to workflow statuses.

### CP0-Q039 · Easy
What is the Jira issue key in "ORD-42"?

- A. The sprint ID
- B. ORD-42 as a whole: project key ORD plus number 42
- C. Only ORD
- D. Only 42

**Answer: B** — Use the key in branches, commits and PRs.

### CP0-Q040 · Medium ★
Why put the Jira key in the branch name, e.g. feature/ORD-42-create-order?

- A. So Jira can link the branch, commits and PR to the issue automatically
- B. It makes the branch private
- C. Git requires it
- D. It speeds up CI

**Answer: A** — Development info appears on the Jira issue.

### CP0-Q041 · Medium
A good Jira story for the capstone includes…

- A. The full code diff
- B. A clear description, acceptance criteria and estimate
- C. The trainee's password
- D. Only a title

**Answer: B** — Acceptance criteria define done for that story.

### CP0-Q042 · Medium
What is Confluence best used for in this programme?

- A. Running unit tests
- B. Hosting Docker images
- C. Storing secrets
- D. Runbooks, design notes, diagrams and learning logs

**Answer: D** — Confluence is the team's documentation space.

### CP0-Q043 · Medium
What is Atlassian Rovo?

- A. A Jira workflow status
- B. A Confluence page template
- C. An AI assistant that searches and summarizes across Jira, Confluence and connected tools
- D. A Git hosting service

**Answer: C** — Rovo helps find knowledge across the Atlassian workspace.

### CP0-Q044 · Medium
You are blocked for half a day. What should you do in Jira?

- A. Close the issue as Done
- B. Flag the issue/move to Blocked and mention the blocker at stand-up
- C. Delete the issue
- D. Do nothing until the end of the sprint

**Answer: B** — Visibility lets mentors unblock you fast.

### CP0-Q045 · Hard
What makes a runbook page useful during an incident?

- A. Symptoms, dashboards/alerts links, step-by-step checks and escalation contacts
- B. Personal opinions about the design
- C. A long history of the project
- D. Screenshots of the IDE

**Answer: A** — Runbooks are actionable under pressure.

### CP0-Q046 · Easy ★
What does "Definition of Done" mean?

- A. The deadline for a task
- B. The final day of the bootcamp
- C. The agreed checklist a piece of work must meet before it is complete
- D. The last Jira status only

**Answer: C** — DoD is a quality gate, not just a status.

### CP0-Q047 · Medium
What is a sprint?

- A. A fixed time box in which the team completes a set of issues
- B. A Git command
- C. A load test
- D. A Confluence space

**Answer: A** — Scrum teams plan work in sprints.

### CP0-Q048 · Easy
Which Jira issue type fits "Consumer processes duplicate messages twice"?

- A. Story
- B. Sub-task of onboarding
- C. Epic
- D. Bug

**Answer: D** — Defects in behavior are bugs.

### CP0-Q049 · Medium
An epic in Jira is…

- A. A single line of code
- B. A Confluence comment
- C. A large body of work that groups many stories
- D. A dashboard widget

**Answer: C** — E.g. "Order Service capstone" can be an epic.

### CP0-Q050 · Hard ★
Why should Confluence pages never contain real secrets or customer PII?

- A. It slows down the page
- B. Pages are widely readable, indexed by search and AI tools, and kept in history
- C. It breaks Jira links
- D. Confluence cannot store text longer than 1 KB

**Answer: B** — Secrets belong in Secrets Manager, not docs.

## Related
- [Git & GitHub flow](git-github-flow.md) — see-also: same checkpoint.
- [GitHub Copilot](github-copilot.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
