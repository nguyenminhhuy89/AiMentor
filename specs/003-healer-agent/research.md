# Research: AiMentor Platform Healer Agent

**Date**: 2026-11-24 | **Branch**: `003-healer-agent`

No NEEDS CLARIFICATION items were found in the spec or plan. The decisions below are derived from the existing plugin pattern and the clarification session.

---

## Decision 1: Agent implementation pattern

**Decision**: Markdown instruction file (`healer.md`) in `plugin/ai-mentor/agents/`, matching the pattern of all other specialist agents (exam-grader, dod-auditor, tutors).

**Rationale**: All AiMentor specialist agents follow this pattern. It allows mentor-lead to dispatch the healer via the Agent tool with `subagent_type: "healer"` when the ai-mentor plugin is loaded, and also allows direct `/heal` invocation.

**Alternatives considered**: A standalone script (Python/Bash) — rejected because the healer needs Claude tools (Artifact, ArtifactData) that are only available in a Claude agent context.

---

## Decision 2: Skill structure

**Decision**: Single `SKILL.md` file at `plugin/ai-mentor/skills/heal/SKILL.md` with 7 numbered check steps, matching the structure of `dod-check/SKILL.md` and `grade-exams/SKILL.md`.

**Rationale**: Consistent with the existing skill pattern. Skills are loaded by agents via `Load mentor-core` / `follow the heal skill` instruction. A single file is simpler to maintain and version.

**Alternatives considered**: Splitting into sub-skills per check — rejected; the checks are few, fast, and always run together.

---

## Decision 3: Pre-flight skip threshold

**Decision**: Skip pre-flight re-run only when all 7 checks returned `ok` in the same session (FR-008, clarified 2026-11-24).

**Rationale**: Any `fixed`, `blocked`, or `needs_human` result means the platform state changed or has an open issue — the healer should re-run to confirm the fix held or to surface the issue again. A strict `all-ok` threshold ensures the pre-flight is never silently skipped when there is still work to do.

**Alternatives considered**: Skip when no check is `blocked` — rejected by the user (Option A chosen over B/C).

---

## Decision 4: Session-state storage for pre-flight skip

**Decision**: In-memory flag only (`all_checks_ok: boolean`). No portal db write required.

**Rationale**: The skip only needs to persist for the duration of one `/full-flow` orchestration session. A db write would require a portal collection entry for healer state, which adds complexity and touches portal data beyond capability declarations. In-memory is sufficient and consistent with how mentor-lead tracks run state for other agents.

**Alternatives considered**: Write a `healer/last-run` document to portal db — rejected; this would require relaxing FR-007's data-write constraint for infrastructure state, adding a new collection to the portal schema, and making the healer stateful across sessions (unnecessary).

---

## Decision 5: Capability republish strategy

**Decision**: Read the live portal artifact, extract all `claude.use('x')` calls from the HTML, compare against the `<artifact-stored-declaration>` block, and republish with the **union** of declared + missing capabilities. Never remove a currently-declared capability.

**Rationale**: Additive-only republish is safer (cannot accidentally break a capability that was deliberately declared) and aligns with FR-001's "additive only — never removes" rule. Capability cleanup (removing incorrectly declared capabilities) is a human action.

**Alternatives considered**: Full replace (overwrite the declaration with exactly what the page needs) — rejected because it could silently remove a capability that the user intentionally added for a future feature.

---

## Decision 6: Degraded-mode behaviour

**Decision**: When the Artifact tool is unavailable (e.g., plain CLI without claude.ai context), portal-related checks (Check 1 portal-reachability, Check 2 capability-audit) are skipped and noted as `blocked: Artifact tool not available in this session` in the result block. File checks (Checks 2–6) proceed normally.

**Rationale**: The healer should provide maximum value even in degraded environments. File checks (URL grep, reference file copy, frontmatter validation) require only Bash/Read/Edit and work in any session.

**Alternatives considered**: Abort entirely if Artifact tool is unavailable — rejected; file checks are still valuable and don't depend on the portal.
