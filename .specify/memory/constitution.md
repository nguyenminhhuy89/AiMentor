<!--
SYNC IMPACT REPORT (scratch for human review; remove before committing)
Version change: template (unversioned) → 1.0.0 (initial ratification)
Modified principles: all placeholders replaced (none existed before).
Added sections: "Data Confidentiality & Drive Conventions", "Delivery & Checkpoint Workflow".
Removed sections: none. Template examples (Library-First, CLI Interface, TDD, Versioning) do not
  apply to this project and were dropped.
Templates checked: .specify/templates/* (not modified).
Deferred TODOs:
  - TODO(M1_COVERAGE): syllabus.md says "≥70% coverage on business logic" for M1, while
    rubrics.md and the M6 MUST item use "team threshold (default 80%)". Confirm one threshold.
  - TODO(BUILD_PATHS): scripts/build.py and make_xlsx.py hard-code ROOT = '/home/claude/qb'.
    Regeneration fails on any other machine until these are made relative to the repo.
  - TODO(RATIFICATION_DATE): set to the date this constitution was first adopted (2026-11-24,
    the date the project files were created). Change it if the program owner adopted it earlier.
-->

# AiMentor Constitution

## Core Principles

### I. One Capstone, Graded Depth
Every trainee MUST build the same capstone, the Order Service, in one repository that grows
daily. Every lab MUST be a commit to that repository. Topics MUST carry a depth tag from
docs/syllabus.md: H (hands-on, the trainee builds it), G (guided, built from a template with
help), or A (awareness, the trainee explains or draws it). Content MUST NOT be promoted from A
or G to H without a syllabus change. Module 6 (lint, build, test) MUST run as a thread from
Day 2, not as a single week.
Rationale: freshers have three weeks. A shared capstone makes progress visible and keeps
checkpoints comparable.

### II. Assessment Integrity
Grading MUST follow docs/rubrics.md. Each module is scored out of 100 (Theory 30, Practical
50, Code quality 20). A trainee passes a module only with a total of at least 70 and no failed
MUST item. A failed MUST item MUST cap the module at 69 regardless of points. A retake MUST
be offered within 48 hours, with at most one retake per module. Every grade MUST include the
rubric feedback format (score table, MUST ticks, top 3 strengths, top 3 gaps with fixes,
remediation plan if failed). The exam-grader agent MUST NOT overwrite a score that a human set;
it MUST propose the change instead. Scores in the 65–74 range, suspected plagiarism, and
unreadable files MUST be flagged for human review.
Rationale: a fixed gate keeps grades consistent across tutors and cohorts.

### III. Generated Artifacts Are Rebuilt, Not Hand-Edited
The question banks (question-banks/raw), exam workbooks (exams/), answer keys
(answer-keys-mentors-only/), knowledge base (knowledge-base/), and the daily report template
(daily-report/) MUST be regenerated from their sources through scripts/build.py and
scripts/make_xlsx.py. Generated files MUST NOT be hand-edited. To change a question, change its
raw source or bank.json, then rebuild. Question IDs are permanent: a retired question MUST be
marked "Retired", not deleted. Changes to the shared template MUST be made in the template
source and then propagated, not by editing a copy in Google Drive by hand.
Rationale: hand-edited output drifts from its source, and the answer keys and exam files must
match exactly.

### IV. Safe Cloud and No Secrets in Conversation
Labs MUST run against LocalStack or the shared sandbox AWS account with a permissions
boundary. Personal AWS accounts MUST NOT be used. No agent or mentor MUST ask a trainee for
AWS keys, passwords, or tokens, and none MUST paste secrets into chat, Jira, or Confluence.
Application code MUST read credentials through the default AWS credential chain. Credentials
MUST live in Secrets Manager, configuration in Parameter Store, and feature flags in AppConfig.
IAM policies MUST NOT use `*` actions or resources on data stores. Secret scans MUST be clean
before any PR is accepted.
Rationale: freshers make mistakes, and a leaked key or an over-permissive role costs real money
and exposes customer PII.

### V. Human Judgement Over Automation for Trainee Status
Automated agents (mentor-lead, tutor agents, exam-grader, dod-auditor) MAY draft plans,
feedback, grades, and DoD evidence. A human mentor MUST confirm any decision on a trainee's
status, including retakes, remediation, pairing at risk, and escalation. Agents MUST escalate
repeated failures, suspected plagiarism, and wellbeing concerns to a human. The portal MUST
be the record of trainees, scores, and DoD status, and every write MUST name its author
(`gradedBy`, `by`).
Rationale: grades affect people's careers. The agents are fast but cannot be accountable.

## Data Confidentiality & Drive Conventions

- Answer keys MUST stay in answer-keys-mentors-only/ and MUST NOT be shared with trainees, or
  placed in any trainee-visible Drive folder, the portal, or a published artifact.
- The question banks (question-banks/) contain the answers and are mentor-only.
- Trainee personal data (names, emails, team, scores) MUST appear only in the portal and in the
  AiMentor Drive folders. It MUST NOT be committed to this repository. Sample data in
  timeline/ or portal mock data MUST be labelled as sample and MUST be removed before use with
  real cohorts.
- Drive layout: AiMentor/Exams/ holds one subfolder per module (M1-Contract-API through
  M6-Quality-Ops). Submission files MUST be named `<TraineeID>_<FullName>_M<n>`. Files that do
  not match MUST be listed as unmatched and MUST NOT be guessed. The DailyReport folder holds
  one progress sheet per trainee, created from the daily report template.
- Exam submissions MUST include the repository or PR link for the practical part.
- The portal's settings/program record (start date, Drive folder) is the source for dates. The
  default start is Monday 30 Nov 2026 and the end is Friday 18 Dec 2026.

## Delivery & Checkpoint Workflow

- The program runs 15 working days in three weeks. Checkpoints CP0 (Day 2), CP1 (Day 5),
  CP2 (Day 8), CP3 (Day 10), CP4 (Day 12), CP5 (Day 14), and CP6 (Day 15) MUST each have an
  exam with 30 questions drawn from the module's bank, plus the Definition of Done check
  where the rubric names one.
- Daily rhythm (syllabus.md) is fixed: stand-up at 09:00, concept at 09:15, labs 10:30 and
  13:30, daily check quiz at 16:30, and commit, PR, learning log, and Jira update at 17:00.
  Changing this rhythm MUST be recorded as an amendment to syllabus.md.
- Every PR MUST carry a description and a Jira key. Every module MUST have a Confluence
  learning log. Pull requests MUST pass lint, build, test, and scan in GitHub Actions before
  merge.
- Pace rule: if more than a third of trainees fail a module exam, the mentor-lead MUST propose a
  schedule change (trim an A-level topic or add a remediation block). H-level content MUST NOT
  be skipped silently.

## Governance

This constitution supersedes all other practices in this repository. CLAUDE.md, README.md, and
the plugin's skills and agents are runtime guidance and MUST NOT contradict it. Where they do,
this document wins and the guidance MUST be fixed.

Amendments MUST be recorded in this file with a Sync Impact Report, approved by the program owner
(the human mentor lead), and accompanied by any changes to the affected syllabus, rubric,
script, agent, or skill. A change to a MUST rule in Principles I–V or the Data Confidentiality
section is a MAJOR amendment only if it removes or weakens a rule. Adding a rule or a section
is MINOR. Wording fixes are PATCH.

Versioning follows semantic versioning: MAJOR for removed or redefined principles, MINOR for
added principles or materially expanded guidance, PATCH for clarifications.

Compliance: every PR and every exam grade MUST be checked against this constitution before it
is accepted. The dod-auditor agent MUST cite the principle when it reports a violation. Each
checkpoint (CP0–CP6) MUST include a review of answer-key and secret handling. A violation found
after the fact MUST be logged and fixed before the next checkpoint.

**Version**: 1.0.0 | **Ratified**: 2026-11-24 | **Last Amended**: 2026-11-24
