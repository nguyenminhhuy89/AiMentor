---
name: progress-report
description: Weekly or end-of-program cohort report from the AiMentor portal — scores per module, pass rates, DoD completion, at-risk trainees and recommendations. Use for "weekly report", "báo cáo tiến độ", "how is the cohort doing", "/progress-report week 2".
---

# Progress report

1. Load `mentor-core`. Read `trainees`, `scores`, `dod`, `flags` from the portal (db_list). Use the result blocks from this week's agent runs if mentor-lead passed them in.
2. Compute — by running code, not by estimating: per-module average, pass rate, retakes; per-trainee running grade (modules ×0.8 + capstone ×0.2 when available); DoD completion %.
3. Report: headline finding first; table per trainee; at-risk list (any fail, or DoD < 60% by D10, or missing submission); 3 recommendations for the next week (content pace, pairing, remediation).
4. Hand the numbers to mentor-lead, which runs `dashboard-publish` so the timeline sync-up matches this report. Offer to publish the report to Confluence (if connected) or as a doc. Never send it to anyone without the user's explicit approval.
5. End with a `result:` block (Result contract in `mentor-core`) with `scope: week <n>` and `writes: none`.
