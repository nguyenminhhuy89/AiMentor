---
name: dashboard-publish
description: Publish member results from the AiMentor portal to the master timeline dashboard (timeline/master-timeline.html) — topic-tracker progress, evidence coverage, DoD count and at-risk status per trainee. Use after a DailyReport scan, a DoD audit, a flag change or the Friday report, or for "publish dashboard", "update the timeline", "cập nhật dashboard".
---

# Publish member results to the dashboard

Only mentor-lead runs this skill. It reads the portal and writes one file: `timeline/master-timeline.html` in the repo. It never writes to the portal.

The dashboard's member sync-up tracks **Topic Tracker** progress (per-topic Not started / In progress / Done, with
evidence links) from each trainee's daily report sheet — not exam scores. Exam pass/fail still lives in the `scores`
collection and the exam-grader's own reports; it is not shown on this dashboard.

1. Load `mentor-core`. Read from the portal with `db_list`: `trainees`, `progress`, `dod`. Read `settings/program` for
   the start date and syllabus day count (60 topics across 15 days, D1–D15 — the same list as `DAYS` in
   `timeline/master-timeline.html`).
2. If a trainee's `progress/<id>` row is missing or older than their current DailyReport sheet, run the DailyReport
   Drive scan first (same logic as the portal's "Daily reports" tab: `search_files` the DailyReport folder, parse
   each sheet's Profile / Topic Tracker / DoD Checklist tabs, recompute, and `db_write` `progress/<id>`). Never guess
   a trainee's numbers from a stale row.
3. Build one row per trainee with `active: true`, sorted by TraineeID:
   `[TraineeID, name, team, url, topicStatus, doneWithProof, due, behind, dodMet, dodTotal, status, flags]`
   - `topicStatus`: a 60-character string, one letter per syllabus topic in the same flattened Day/Module/Topic order
     as `DAYS` in `timeline/master-timeline.html` (day 1's topics first, then day 2's, …) — `D` for Done, `I` for In
     progress, `N` for Not started. Build it from `progress/<id>`'s underlying Topic Tracker rows (the scan has
     them before it aggregates); never reconstruct it by guessing from the aggregate counts alone.
   - `doneWithProof`: `progress/<id>.doneWithProof` (Done topics that also carry an evidence link).
   - `due`, `behind`: `progress/<id>.due` / `.behind` (topics due by today's bootcamp day; behind = due but not
     Done-with-proof).
   - `dodMet`, `dodTotal`: `progress/<id>.dodMet` / `.dodTotal` (out of 30: 5 DoD items × 6 modules).
   - `status`: `progress/<id>.status` (`On track` / `Watch` / `At risk`), or `Not started` if `topicsDone +
     topicsInProgress` is 0.
   - `flags`: `progress/<id>.flags` (evidence missing, early "Done", MUST items not met, profile gaps).
   - `url`: the trainee's progress sheet link (`progress/<id>.url`), so a mentor can open it straight from the
     dashboard.
4. Edit `timeline/master-timeline.html`. Replace the text between `// MEMBERS:BEGIN` and `// MEMBERS:END` with:
   - `const PUBLISHED="<YYYY-MM-DD HH:mm>";` (current local time, GMT+7)
   - `const T=[` followed by one row per line, then `];`
   Keep everything outside that block unchanged.
5. Verify. Extract the text between `<script>` and `</script>` into a file in the scratchpad and run `node --check`
   on it. If node is not installed, say so. Confirm the number of rows equals the number of active trainees, and
   that every `topicStatus` string is exactly 60 characters. If a check fails, restore the previous block and
   report the error.
6. Report: rows published, anyone with `due > 0 && behind > 0` (behind schedule), anyone flagged, and any trainee
   with no `progress/<id>` row yet (no report submitted). Remind the user that the file contains trainee names, so
   it should stay out of git and outside the team.

Progress is never estimated. A trainee with no scanned report is published with `status: "Not started"` and an
all-`N` `topicStatus`, not with a guess.
