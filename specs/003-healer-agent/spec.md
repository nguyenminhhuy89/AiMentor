# Feature Specification: AiMentor Platform Healer Agent

**Feature Branch**: `003-healer-agent`

**Created**: 2026-11-24

**Status**: Draft

**Input**: User description: "Auto-healing agent for the AiMentor platform. The agent (healer) reviews, smoke-tests and auto-fixes infrastructure issues: (1) portal capability declarations, (2) stale artifact URLs, (3) missing skill cross-reference files, (4) portal db connectivity, (5) agent frontmatter completeness. Auto-fixes what is safe. Escalates what needs a human. Lives in plugin/ai-mentor/agents/healer.md + plugin/ai-mentor/skills/heal/SKILL.md."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Run a full platform health check (Priority: P1)

A mentor-lead or program owner wants to verify the AiMentor platform is correctly wired before running the daily bootcamp flow. They invoke `/heal` and receive a structured report of what was checked, what was auto-fixed, and what still needs their attention.

**Why this priority**: Without a working portal and consistent file references, every downstream agent (exam-grader, dod-auditor, tutors) fails silently or produces phantom data. This is the foundational safety net.

**Independent Test**: Can be fully tested by invoking `/heal` on a clean repo and verifying the report lists all 5 check categories, shows their status, and correctly identifies at least one pre-seeded issue.

**Acceptance Scenarios**:

1. **Given** the platform has a stale portal URL in one skill file, **When** `/heal` runs, **Then** the file is edited to the correct URL and the fix is listed in `fixes_applied`.
2. **Given** all 5 checks pass with no issues, **When** `/heal` runs, **Then** the report shows all checks as `ok` and `fixes_applied` is empty.
3. **Given** the portal is missing the `db` capability declaration, **When** `/heal` runs, **Then** the portal is republished with the missing capability added and the fix is recorded.

---

### User Story 2 - Pre-flight check before full-flow (Priority: P2)

Before running `/full-flow`, mentor-lead automatically dispatches the healer as a pre-flight step. If the healer detects a blocking portal issue (unreachable artifact, missing `db` capability), the full-flow is halted and the issue reported before any specialist agents waste effort.

**Why this priority**: Running the full team flow against a broken portal produces a cascade of agent failures and confusing `needs_human` lists. The pre-flight stops the cascade at the source.

**Independent Test**: Can be fully tested by injecting a known capability gap, triggering `/full-flow`, and observing that the healer's `blocked` check halts the flow before any specialist agents are dispatched.

**Acceptance Scenarios**:

1. **Given** the portal artifact is unreachable, **When** pre-flight runs, **Then** `status: blocked` is returned and full-flow does not dispatch specialist agents.
2. **Given** all 7 checks returned `ok` in this session, **When** pre-flight runs again, **Then** the healer is skipped (not re-dispatched) to avoid redundant work. If any check returned `fixed`, `blocked`, or `needs_human` in the previous run, the healer re-runs.

---

### User Story 3 - Review what needs human action (Priority: P3)

After the healer auto-fixes what it can, the remaining issues (missing trainee cohort, missing `settings/program`, Drive connector not connected) are surfaced as a prioritised `needs_human` list so the mentor can act on them in one place.

**Why this priority**: Separating auto-fixable issues from human-required ones prevents alert fatigue and focuses attention where it is actually needed.

**Independent Test**: Can be fully tested by running `/heal` with 0 trainees enrolled and no `settings/program` document, and verifying the `needs_human` list contains both items with actionable descriptions.

**Acceptance Scenarios**:

1. **Given** 0 trainees are in the portal, **When** `/heal` runs, **Then** `needs_human` includes "add trainee cohort before D1 (2026-11-30)".
2. **Given** `settings/program` is absent, **When** `/heal` runs, **Then** `needs_human` includes "seed settings/program via portal Setup tab".
3. **Given** Google Drive is not connected, **When** `/heal` runs, **Then** `needs_human` includes "connect Google Drive in claude.ai Settings → Connectors".

---

### Edge Cases

- What happens when the portal artifact is owned by a different claude.ai account (cannot be republished)? → Healer reports it under `needs_human: republish portal from the owning account` and does not attempt the write.
- What if a file edit introduces a syntax error in YAML frontmatter? → Healer validates the edit result before saving; if validation fails, it reverts and escalates.
- What if the healer itself is dispatched without the ai-mentor plugin loaded? → Healer runs in degraded mode (file and db checks only); portal checks that require the Artifact tool are skipped and noted in the report.
- What if two checks conflict (e.g., URL check says stale, but capability check requires a republish anyway)? → Capability republish includes the corrected URL, eliminating the separate URL edit for that file.
- What if `references/rubrics.md` exists at the repo root but is older than the canonical copy in the skill? → Healer reports the age discrepancy under `needs_human`; it does not auto-overwrite because the file may have intentional local changes.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The healer MUST check that every `claude.use('x')` call in the portal HTML has a corresponding entry in the portal's stored capability declaration, and MUST republish the portal with any missing capabilities added (additive only — never removes declared capabilities).
- **FR-002**: The healer MUST grep all `.md` files under `plugin/` for artifact URLs and MUST edit any file where the URL slug does not match the canonical portal slug in `plugin/ai-mentor/skills/mentor-core/SKILL.md`.
- **FR-003**: The healer MUST check that every file referenced by a `Load references/X` instruction in any skill exists at the repo-root `references/` path, and MUST copy the file from the skill's own `references/` directory when the repo-root copy is missing.
- **FR-004**: The healer MUST perform a db smoke test by listing the `trainees` collection and reading the `settings/program` document from the portal, and MUST report the trainee count and start date without writing any portal data.
- **FR-005**: The healer MUST read every `.md` file under `plugin/ai-mentor/agents/` and MUST verify that YAML frontmatter contains `name`, `description`, and `model` fields; it MUST add `model: inherit` when only `model` is missing, and MUST escalate under `needs_human` when `description` is absent (cannot infer intent).
- **FR-006**: The healer MUST produce a `result:` yaml block at the end of every run, structured per the mentor-core Result contract extended with per-check status entries.
- **FR-007**: The healer MUST NOT overwrite portal data written by humans (scores, DoD ticks, trainee records set by mentors) — its portal writes are limited to the capability declaration (artifact republish only).
- **FR-008**: The healer MUST be invocable as `/heal` directly and as a pre-flight step within `/full-flow`; in pre-flight mode it MUST skip re-running only when all 7 checks returned `ok` in the same session — if any check returned `fixed`, `blocked`, or `needs_human`, the healer MUST re-run on the next invocation.
- **FR-009**: The healer MUST check whether the full-flow skill's agent dispatch table references any specialist agent that has no corresponding `.md` file in `plugin/ai-mentor/agents/`, and MUST report any gap under `needs_human`.

### Key Entities

- **Check**: One named verification step (e.g., `portal-capabilities`). Has a name, status (`ok | fixed | blocked | needs_human`), and a one-line detail.
- **Fix**: A change applied automatically. Has a description and affected path.
- **Escalation** (`needs_human` item): An issue the healer detected but cannot resolve. Has an actionable description and optionally a suggested resolution command.
- **Portal artifact**: The Claude artifact (`ACBVYCSsYnWtD5ngzXz3dW`) that holds trainee, score, DoD, progress, and settings data. The healer may republish it to correct capability declarations; it MUST NOT modify its data documents.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A complete heal run (all 7 checks) finishes and returns a `result:` block within a single agent turn.
- **SC-002**: After `/heal` runs on a repo with known issues (stale URL, missing capability, missing rubrics.md), 100% of auto-fixable issues are resolved with no manual intervention required.
- **SC-003**: The `needs_human` list contains only items that genuinely cannot be resolved without human action — zero false positives (items the healer could have fixed but didn't).
- **SC-004**: The healer never modifies portal trainee, score, DoD, or progress data — verified by comparing portal db contents before and after a heal run.
- **SC-005**: Running `/heal` twice in succession with no intervening changes produces an identical report (idempotent).

## Clarifications

### Session 2026-11-24

- Q: What check-result threshold allows the pre-flight step to skip a re-run ("ran cleanly")? → A: All 7 checks must return `ok` — any `fixed`, `blocked`, or `needs_human` result causes the healer to re-run on the next invocation.

## Assumptions

- The healer runs in the same Claude session that has access to the Artifact tool (to read and republish the portal). In sessions without Artifact access (e.g., plain CLI), portal capability checks are skipped and noted.
- The canonical portal slug is always read from `plugin/ai-mentor/skills/mentor-core/SKILL.md` at run time — it is never hardcoded in the heal skill itself.
- "Safe" auto-fixes are limited to: (a) editing `.md` files in the repo, (b) copying files within the repo, and (c) republishing the portal artifact to add missing capabilities. All other portal db writes require human approval.
- The healer does not check Google Drive connectivity directly; it relies on the absence of `mcp__Google_Drive__*` tools in the session to determine whether Drive is connected.
- Trainee personal data (names, emails, scores) surfaced during the db smoke test MUST NOT be logged or written anywhere outside the portal.
- The healer is a maintenance agent, not a teaching agent. It does not interact with trainees.
