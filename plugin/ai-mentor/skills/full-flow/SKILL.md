---
name: full-flow
description: Run the full AiMentor team flow for a day or module — dispatch the specialist agents in parallel, collect their results, summarize for the human, publish the dashboard, and list anything needing a human decision. Use for "/full-flow", "/full-flow D7", "/full-flow M1", "run the full team flow".
---

# Full flow

Only mentor-lead runs this skill; it is the orchestrator's top-level entry point. Argument (optional): `D<n>` (a bootcamp day) or `M<n>` (a module); empty means today's bootcamp day from `settings/program.startDate`.

1. Load `mentor-core` (syllabus, rubrics, portal paths, Result contract). Resolve the argument to a bootcamp day and/or module using `references/syllabus.md` and `settings/program`.
2. **Split.** Build one work package per owner that applies to this day/module, per mentor-lead's Owners table:
   - The module tutor for the module in scope (M1 → tutor-contract-api, M2 → tutor-data-encryption, M3 → tutor-async-events, M4 → tutor-gateway-security, M5 → tutor-runtime-cicd, M6 → tutor-quality-ops) — only if there is a concrete question, lab check or stuck trainee to hand it; an empty module scope with nothing pending gets no tutor package.
   - `exam-grader` (`grade-exams`) — scan Drive for new submissions in this module's folder.
   - `dod-auditor` (`dod-check`) — only for trainees with a repo link on file; never invent one.
   - `daily-plan` (you) when the argument is a day, or at the start of any run, for today's plan and at-risk list.
3. **Dispatch in parallel.** Send independent packages in the same turn with the Agent tool, naming the agent as the subagent type (requires the `ai-mentor` plugin loaded: `claude --plugin-dir ./plugin/ai-mentor`). Order only where a dependency exists: grading and DoD audits finish before `progress-report` or `dashboard-publish` runs.
4. **Collect.** Each agent ends with a `result:` block (mentor-core's Result contract). Missing or `status: blocked` → re-dispatch once naming the gap; still missing → record under `needs_human`.
5. **Summarize.** Headline first, then one table: member · checkpoint · score · pass/retake · DoD x/15 · flag · owner · next action. One screen.
6. **Publish.** If any `result:` block's `writes` is non-empty (a score, DoD tick, flag or progress record changed), run `dashboard-publish` so `timeline/master-timeline.html` (or the published Master Timeline artifact) reflects it. Say which members were published and which still lack data.
7. **Writes.** exam-grader writes scores under its own rules (never overwrites a human-set score). dod-auditor never writes DoD evidence without the human's approval: list its proposed writes in your summary and ask once for the whole batch before running them.
8. **Escalate.** Anything mentor-lead cannot resolve itself — repeated failures, suspected plagiarism, wellbeing concerns, any decision on a trainee's status, or a tool/connector that is unavailable — goes under `needs_human` in the summary, not silently skipped.

If the portal, Google Drive, or the plugin's own agents are unreachable in this session, say so plainly in the summary instead of fabricating scores, flags, or a `result:` block on an agent's behalf.

## Pre-flight (optional)
Before the first run of a session, dispatch `healer` (`heal` skill) first — before any specialist agents. The healer checks portal capabilities, URL consistency, file references and db connectivity, auto-fixes what it can, and returns a `result:` block.

**Pre-flight skip condition** (FR-008 / data-model.md `SessionState.all_checks_ok`): skip only when all 7 checks returned `ok` in this session — meaning the last `HealResult` had `status: done` AND every `checks[*].status == ok`. If any check returned `fixed`, `blocked`, or `needs_human` in the last run, re-run the healer on the next invocation. Track this in memory only; never write the flag to the portal db.

Only proceed with the main specialist-agent flow once the healer's status is `done` or `partial` with no blocking portal issues.
