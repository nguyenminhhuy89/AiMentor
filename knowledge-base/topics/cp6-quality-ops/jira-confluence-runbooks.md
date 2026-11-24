---
id: 20261124-cp6-jira-confluence-runbooks
title: CP6 · Jira, Confluence & runbooks
tags: [question-bank, cp6]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp6-code-quality-in-ci, 20261124-cp6-tracing-datadog-apm, 20261124-exam-blueprint]
summary: 20 CP6 questions on Jira, Confluence & runbooks (6 easy, 10 medium, 4 hard) with answers and explanations.
---

# CP6 · Jira, Confluence & runbooks

> Summary: 20 CP6 questions on Jira, Confluence & runbooks (6 easy, 10 medium, 4 hard) with answers and explanations.

## Context
Part of the CP6 Quality, Observability & Ops bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP6).

## Questions

### CP6-Q101 · Easy ★
What is a runbook?

- A. A Go test
- B. Step-by-step instructions for operating or troubleshooting a system
- C. A Docker image
- D. An IAM policy

**Answer: B** — DoD: runbooks documented in Confluence.

### CP6-Q102 · Easy ★
Where are runbooks stored in this programme?

- A. Docker image
- B. Local laptop
- C. Jira comments only
- D. Confluence (searchable with Atlassian Rovo)

**Answer: D** — Linked from alerts.

### CP6-Q103 · Easy
What should every Jira issue for the capstone have before Done?

- A. Linked PR/commits and acceptance criteria met
- B. No description
- C. A screenshot of the IDE
- D. Only a title

**Answer: A** — Traceability per DoD.

### CP6-Q104 · Medium ★
A good runbook for "DLQ has messages" includes…

- A. Only "restart everything"
- B. How to inspect messages, find the trace in Datadog, fix, and safely redrive
- C. The admin password
- D. Customer phone numbers

**Answer: B** — Actionable steps.

### CP6-Q105 · Medium
How does Atlassian Rovo help during on-call?

- A. It replaces PagerDuty
- B. It writes Go code into prod
- C. It can search and summarize related runbooks, past incidents and Jira issues
- D. It deploys fixes

**Answer: C** — Faster knowledge retrieval.

### CP6-Q106 · Medium
What should link a monitor, a runbook and a Jira epic?

- A. URLs in the alert message and runbook, and the runbook linked on the service's Jira epic/Confluence space
- B. A Docker label
- C. Nothing
- D. A shared password

**Answer: A** — Cross-linking speeds response.

### CP6-Q107 · Medium ★
What is an architecture decision record (ADR)?

- A. A database record
- B. A short document capturing a decision, context and consequences
- C. A Jira status
- D. A test case

**Answer: B** — Keeps reasoning discoverable.

### CP6-Q108 · Hard
Why keep runbooks next to dashboards and review them after incidents?

- A. It increases page views
- B. Stale runbooks mislead responders; reviews keep steps accurate
- C. Confluence deletes old pages
- D. They are decorative

**Answer: B** — Living documentation.

### CP6-Q109 · Easy
Which Jira artifact groups all capstone work?

- A. A label only
- B. A comment
- C. A watcher
- D. An epic

**Answer: D** — Stories roll up to the epic.

### CP6-Q110 · Medium
What is the Definition of Done's role at sprint review?

- A. It is optional
- B. Only for documentation
- C. Work is shown as done only if every DoD item is met with evidence
- D. Only for bugs

**Answer: C** — Quality gate before acceptance.

### CP6-Q111 · Medium
What should the Confluence page for the Order Service contain?

- A. Only the team photo
- B. Overview, architecture diagram, API contract link, runbooks, dashboards and owners
- C. Copied Go source code
- D. The database password

**Answer: B** — Single entry point for the service.

### CP6-Q112 · Hard ★
How can Jira automation help the DoD?

- A. Auto-close all issues
- B. Assign everything to the mentor
- C. Block transitions to Done unless the linked PR is merged and checks pass
- D. Delete stale issues

**Answer: C** — Enforce process with automation.

### CP6-Q113 · Easy
What is a Jira dashboard useful for in the bootcamp?

- A. Deploying code
- B. Seeing progress per trainee/module at a glance
- C. Hosting runbooks
- D. Running tests

**Answer: B** — Complements the AiMentor portal.

### CP6-Q114 · Medium
What belongs in the capstone demo on Day 15?

- A. Only code walkthrough
- B. Only slides
- C. The working flow end to end, the DoD evidence, dashboards/alerts, and lessons learned
- D. A list of Jira tickets

**Answer: C** — Show, don't tell.

### CP6-Q115 · Hard
A trainee's runbook contains a production password. What do you do?

- A. Leave it, the space is private
- B. Remove it, rotate the credential, check page history/access, and point to Secrets Manager
- C. Blur it in a screenshot
- D. Move it to a comment

**Answer: B** — Treat as a leak.

### CP6-Q116 · Medium
What makes a Confluence page easy for Rovo and humans to find?

- A. No headings
- B. Attachments only
- C. Very long titles with dates only
- D. Clear title, labels, summary at the top and links to related pages

**Answer: D** — Structure aids search.

### CP6-Q117 · Easy
What does linking a Jira key in a commit message do?

- A. Deploys the code
- B. Shows the commit on the Jira issue's development panel
- C. Assigns the mentor
- D. Closes the sprint

**Answer: B** — With the GitHub for Jira integration.

### CP6-Q118 · Medium
What is a blameless culture?

- A. Focusing on systems and process improvements rather than blaming individuals
- B. Hiding mistakes
- C. Blaming the newest member
- D. Never discussing incidents

**Answer: A** — Encourages honest reporting.

### CP6-Q119 · Hard
Which evidence best proves the Observability & Ops DoD?

- A. A Jira status only
- B. Links to the dashboard, a fired test alert in PagerDuty, the runbook page and the trace screenshot with IDs
- C. A statement "done"
- D. A code comment

**Answer: B** — Evidence-based DoD.

### CP6-Q120 · Medium
What is the purpose of the Day 15 final DoD audit?

- A. Verify every DoD item across modules with evidence before graduation
- B. Delete the sandbox immediately
- C. Assign new trainees
- D. Collect feedback only

**Answer: A** — dod-auditor + mentor review.

## Related
- [Code quality in CI](code-quality-in-ci.md) — see-also: same checkpoint.
- [Tracing & Datadog APM](tracing-datadog-apm.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
