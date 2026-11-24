---
id: 20261124-cp6-pagerduty-incident-response
title: CP6 · PagerDuty & incident response
tags: [question-bank, cp6]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp6-code-quality-in-ci, 20261124-cp6-tracing-datadog-apm, 20261124-exam-blueprint]
summary: 15 CP6 questions on PagerDuty & incident response (5 easy, 7 medium, 3 hard) with answers and explanations.
---

# CP6 · PagerDuty & incident response

> Summary: 15 CP6 questions on PagerDuty & incident response (5 easy, 7 medium, 3 hard) with answers and explanations.

## Context
Part of the CP6 Quality, Observability & Ops bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP6).

## Questions

### CP6-Q086 · Easy ★
What is PagerDuty used for?

- A. Docker builds
- B. Database backups
- C. Code hosting
- D. On-call alerting, escalation and incident coordination

**Answer: D** — DoD: PagerDuty alerts active.

### CP6-Q087 · Easy
What is an escalation policy?

- A. A Jira workflow
- B. Rules for who is notified and when, if an alert is not acknowledged
- C. A firewall rule
- D. A rate limit

**Answer: B** — e.g. primary → secondary after 10 minutes.

### CP6-Q088 · Easy ★
What does "acknowledge" mean in PagerDuty?

- A. Someone has seen the incident and is working on it
- B. The alert is deleted
- C. The incident is resolved
- D. The service is disabled

**Answer: A** — Stops escalation.

### CP6-Q089 · Medium
What makes an alert actionable?

- A. It shows CPU every minute
- B. It signals real user impact or imminent risk and links to a runbook
- C. It has a long title
- D. It fires often

**Answer: B** — Avoid alert fatigue.

### CP6-Q090 · Medium ★
What should an alert payload include?

- A. The full log file
- B. Customer PII
- C. Service, environment, what's wrong, dashboard link, runbook link and trace/correlation hints
- D. Only "ERROR"

**Answer: C** — Context speeds response.

### CP6-Q091 · Medium
What is a postmortem?

- A. A deployment
- B. Punishing the on-call engineer
- C. A blameless review of an incident: timeline, root cause, impact and action items
- D. A Jira status

**Answer: C** — Learn and prevent recurrence.

### CP6-Q092 · Medium
Severity levels (SEV1/SEV2…) are used to…

- A. Sort Git branches
- B. Prioritize response based on impact
- C. Rank trainees
- D. Set log levels

**Answer: B** — Higher severity = broader response.

### CP6-Q093 · Hard
During an incident, what is the first priority?

- A. Write the postmortem
- B. Mitigate customer impact (rollback, failover, disable feature) before deep root-cause analysis
- C. Refactor the code
- D. Find who caused it

**Answer: B** — Stop the bleeding first.

### CP6-Q094 · Hard ★
What is alert fatigue?

- A. Long Jira tickets
- B. Responders ignoring alerts because too many are noisy or non-actionable
- C. Being tired after a deploy
- D. Too few alerts

**Answer: B** — Tune or remove noisy alerts.

### CP6-Q095 · Easy
Which DoD-linked alert should page in the capstone?

- A. Messages in the SQS DLQ (and high error rate on the API)
- B. Each successful request
- C. CPU at 30%
- D. Every Git push

**Answer: A** — Page on user-impacting signals.

### CP6-Q096 · Medium
What is the role of the incident commander?

- A. Writes all the code fixes
- B. Coordinates the response, assigns roles and communicates status
- C. Approves PRs only
- D. Owns the Jira board forever

**Answer: B** — Separates coordination from fixing.

### CP6-Q097 · Medium
How do PagerDuty dedup keys help?

- A. They schedule on-call
- B. They delete alerts
- C. Repeated alerts for the same issue group into one incident
- D. They encrypt alerts

**Answer: C** — Less noise.

### CP6-Q098 · Hard
An alert fires but the runbook link is broken. Postmortem action item?

- A. Blame the author
- B. Ignore it
- C. Delete the alert
- D. Fix the link and add a check that every monitor has a valid runbook URL

**Answer: D** — Improve the system.

### CP6-Q099 · Medium
What is MTTR?

- A. Maximum test time
- B. Mean time to restore/resolve service after an incident
- C. Monthly traffic rate
- D. Mean time to release

**Answer: B** — Track it to improve ops.

### CP6-Q100 · Easy
Where should incident follow-up tasks be tracked?

- A. Jira issues linked to the postmortem
- B. In the Dockerfile
- C. In someone's memory
- D. In Slack only

**Answer: A** — Track to completion.

## Related
- [Code quality in CI](code-quality-in-ci.md) — see-also: same checkpoint.
- [Tracing & Datadog APM](tracing-datadog-apm.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
