---
description: Run the full AiMentor team flow through mentor-lead (daily plan, tutors, exam grading, dashboard publish)
argument-hint: [D<n> | M<n>]
---

Run the full AiMentor team flow orchestrated by the mentor-lead agent.

1. Read `plugin/ai-mentor/skills/full-flow/SKILL.md` and follow it exactly.
2. Also load `plugin/ai-mentor/skills/mentor-core/SKILL.md` (Result contract and portal paths) before dispatching.
3. Argument: `$ARGUMENTS` (empty means today's bootcamp day from `settings/program.startDate`).

Dispatch the specialist agents from `plugin/ai-mentor/agents/` in parallel, collect their `result:` blocks, summarize for the human, run `dashboard-publish` if anything changed, and list anything needing a human decision. Do not write DoD results to the portal without approval.
