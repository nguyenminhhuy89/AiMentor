# Implementation Plan: AiMentor Platform Healer Agent

**Branch**: `003-healer-agent` | **Date**: 2026-11-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/003-healer-agent/spec.md`

## Summary

A Claude plugin agent (`healer`) and companion skill (`heal`) that run 7 ordered infrastructure checks against the AiMentor platform, auto-fix safe issues (file edits, portal capability republish), and return a structured `result:` block. The agent loads as a plugin specialist via `claude --plugin-dir ./plugin/ai-mentor` and is also invocable from mentor-lead as a pre-flight step before `/full-flow`. All portal data writes are strictly limited to capability-declaration republishes; no trainee, score, DoD, or progress data is ever written by the healer.

## Technical Context

**Language/Version**: Markdown (agent/skill instruction files); Bash for grep/edit/copy operations at runtime

**Primary Dependencies**: Claude Code plugin system; Artifact tool (portal read + republish); ArtifactData tool (db smoke test — `db_list`, `db_get`); Bash, Read, Edit, Write tools (file checks and fixes)

**Storage**: Local filesystem (repo `.md` files, `references/`); Portal artifact db (read-only except capability declaration republish)

**Testing**: Manual — invoke `/heal` and inspect `result:` block; inject known issue and verify auto-fix; run twice to confirm idempotency (SC-005)

**Target Platform**: Claude Code (VS Code extension, CLI) with ai-mentor plugin loaded; portal checks degrade gracefully when Artifact tool is unavailable

**Project Type**: Claude plugin agent + skill (Markdown instruction files)

**Performance Goals**: All 7 checks complete and `result:` block returned within a single agent turn (SC-001)

**Constraints**: Portal writes additive-only (capabilities only); never touch trainee/score/DoD/progress data; never edit generated artifacts (question-banks/, exams/, answer-keys-mentors-only/)

**Scale/Scope**: ~10 agent files, ~8 skill files, 1 portal artifact, ~5 reference files — bounded, no scalability concern

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Healer Status |
|---|---|---|
| I — One Capstone, Graded Depth | Agents must not promote depth levels or change syllabus | ✅ Healer is infrastructure-only; never touches syllabus or labs |
| II — Assessment Integrity | exam-grader must not overwrite human scores; every grade must credit an author | ✅ Healer never touches scores or grades |
| III — Generated Artifacts Rebuilt | question-banks/, exams/, answer-keys-mentors-only/, daily-report/ must not be hand-edited | ✅ Healer's file edits target only plugin/*.md and references/; generated dirs are out of scope (FR-007, Constraints) |
| IV — Safe Cloud, No Secrets | No secrets in conversation or files | ✅ Healer reads portal db for smoke test but logs no PII (Assumption 5); no credentials handled |
| V — Human Judgement Over Automation | Agents may draft; human must confirm trainee status decisions; every write must name its author | ✅ Healer auto-fixes infrastructure only; all trainee-status decisions escalated; portal republish is a capability declaration, not a data write |
| Data Confidentiality | Answer keys must never leave answer-keys-mentors-only/ | ✅ Healer's file scope is plugin/ and references/ only |
| Governance | Skills/agents must not contradict the constitution | ✅ healer.md and heal/SKILL.md will be validated against constitution before merge |

**Gate result: PASS** — no violations, no complexity justifications needed.

## Project Structure

### Documentation (this feature)

```text
specs/003-healer-agent/
├── plan.md              ← this file
├── research.md          ← Phase 0 output
├── data-model.md        ← Phase 1 output
├── quickstart.md        ← Phase 1 output
├── contracts/
│   └── result-contract.md   ← Phase 1 output
└── tasks.md             ← /speckit-tasks output (not yet created)
```

### Source Code (repository root)

```text
plugin/ai-mentor/
├── agents/
│   └── healer.md              ← agent instruction file (exists, will be revised from spec)
└── skills/
    └── heal/
        └── SKILL.md           ← skill instruction file (exists, will be revised from spec)

references/
├── syllabus.md                ← already exists
└── rubrics.md                 ← already exists (copied by healer during first run)
```

**Structure Decision**: Single plugin agent + single skill. No new source directories needed — the deliverables are Markdown instruction files within the existing plugin layout.

## Complexity Tracking

No constitution violations requiring justification.
