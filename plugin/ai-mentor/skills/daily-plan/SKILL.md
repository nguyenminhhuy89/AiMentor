---
name: daily-plan
description: Produce today's bootcamp plan — the syllabus day, goals, lab steps, who is behind and what to do about it. Use for "today's plan", "kế hoạch hôm nay", "stand-up", "what's on day 7", "/daily-plan".
---

# Daily plan

1. Load `mentor-core`. Read `settings/program.startDate` from the portal; compute the bootcamp day (working days only, D1–D15). Accept an explicit `D<n>` argument instead.
2. From `references/syllabus.md` take that day's topics, depth levels, lab output and check.
3. From the portal read `scores` and `dod` to find trainees who failed or have not submitted the latest module exam, or have open MUST items.
4. Output, in this order:
   - **Day N — Module, theme** (one line)
   - Learning goals (3 bullets, verb-first, measurable)
   - Schedule using the daily rhythm, with the concrete lab steps for this day
   - Tutor agent on duty (module tutor name)
   - At-risk trainees and the action for each (pair-up, remediation slot, 1:1), using the `flags` collection for the next checkpoint
   - On a checkpoint day: the exam window (exam 16:30, upload to Drive by 17:00), that exam-grader runs overnight, and that the dashboard refreshes next morning
   - Results expected today and the owner of each (tutor flags, exam-grader scores, dod-auditor items)
   - End-of-day quiz topic list (hand to `module-quiz`)
Keep it to one screen. Post-ready for Jira/Confluence if asked.
