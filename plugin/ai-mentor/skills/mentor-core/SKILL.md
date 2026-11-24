---
name: mentor-core
description: Core knowledge for the AiMentor 3-week Go/AWS bootcamp — syllabus, daily timeline, depth levels, rubrics and Definition of Done. Load whenever a request mentions the bootcamp, a trainee, a module (M1–M6), the capstone Order Service, exams, rubrics, or "what are we doing today".
---

# AiMentor core

Load `references/syllabus.md` for the 15-day timeline and `references/rubrics.md` for grading.

## Ground rules for every agent on the team
- Trainees are freshers. Explain from first principles, one concept at a time, with a runnable Go example. Never dump a full solution for a graded lab — give hints in three levels (nudge → pointer → partial snippet) and ask what they tried.
- Everything builds the same capstone: the **Order Service** repo. Tie every answer back to it.
- Respect depth levels: H (must build), G (template + help), A (explain/diagram only). Don't push freshers into A-level topics beyond awareness.
- Use LocalStack or the sandbox AWS account. Never ask a trainee for AWS keys, passwords or tokens; never paste secrets into chat, Jira or Confluence.
- Copilot is allowed; the trainee must be able to explain what they commit.
- Reply in the trainee's language (Vietnamese or English).
- Agents do not edit `timeline/master-timeline.html`. Only `dashboard-publish` writes to it.

## Members, checkpoints and modules
- A **member** is a trainee (`trainees/<id>`). Trainee IDs match the Drive file naming `<TraineeID>_<FullName>_M<n>`.
- Checkpoint n maps to module n: CP0 onboarding (D2, mentor sign-off), CP1 = M1 exam (D5), CP2 = M2 (D8), CP3 = M3 (D10), CP4 = M4 (D12), CP5 = M5 (D14), CP6 = M6 exam and final DoD (D15).
- Pass mark 70 / 100. A failed MUST item caps the module at 69.

## Portal
The AiMentor portal (Claude artifact) is the source of truth for trainees, scores, DoD status and flags.
Portal slug: `ACBVYCSsYnWtD5ngzXz3dW` (https://claude.ai/artifact/ACBVYCSsYnWtD5ngzXz3dW). Data paths:
- `trainees/<id>` → `{name, email, team, active}`
- `scores/<traineeId>_M<n>` → `{traineeId, module, theory, practical, quality, total, pass, musts, feedback, fileId, fileName, gradedBy, gradedAt}`
- `dod/<traineeId>_<itemKey>` → `{done, note, by, at}`
- `flags/<traineeId>_CP<n>` → `{flag, note, by, at}` — at-risk flag for the next checkpoint, set by mentor-lead from tutor and grader results
- `progress/<traineeId>` → one row per trainee's daily report sheet (Topic Tracker + DoD Checklist tabs), written by the `daily-plan`/portal Drive scan: `{traineeId, name, sheetId, sheetName, url, scannedAt, bootcampDay, topicsTotal, topicsDone, doneWithProof, doneNoProof, due, behind, dodMet, dodTotal, status, flags, by}`. This is the per-topic signal (Not started / In progress / Done, each Done needing an evidence link) — distinct from `scores`, which holds exam results. `dashboard-publish` reads this collection to drive the master timeline's member sync-up section.
- `settings/program` → `{startDate, driveFolder}`
Read with `db_list` / `db_get`, write with `db_write` (read first to get `ifVersion` for existing docs).

## Result contract
Every agent ends its reply with exactly one fenced `yaml` block, so mentor-lead can summarize and publish without re-reading the chat:

```yaml
result:
  agent: <agent name>
  scope: <M<n> or D<n>>
  status: done | partial | blocked
  members:
    - id: <TraineeID>
      checkpoint: CP<n>        # omit for tutor-only help
      score: <0-100 or null>   # exam-grader only
      dod_done: <0-15>         # dod-auditor only
      flag: true | false       # true = mentor attention needed before the next checkpoint
      note: <one line>
  needs_human: [<items>]
  writes: [<portal paths written, or "none">]
```

Rules:
- Use `null` for anything the agent did not measure. Never invent a score or a DoD count.
- A tutor sets `flag: true` only when a trainee is still stuck on a MUST item after all three hint levels.
- `writes` lists only what was actually written to the portal in this run.

## Dashboard
`timeline/master-timeline.html` is the team dashboard. It shows the sync-up of members by checkpoint. Its member data sits between `MEMBERS:BEGIN` and `MEMBERS:END`, and `dashboard-publish` owns that block.
