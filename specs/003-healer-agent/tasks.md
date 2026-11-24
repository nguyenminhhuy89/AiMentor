# Tasks: AiMentor Platform Healer Agent

**Input**: Design documents from `specs/003-healer-agent/`

**Prerequisites**: plan.md ✅ · spec.md ✅ · research.md ✅ · data-model.md ✅ · contracts/ ✅ · quickstart.md ✅

**Tests**: Not explicitly requested in spec. Validation scenarios from quickstart.md are included as Polish tasks.

**Organization**: Tasks grouped by user story — US1 (7-check health run), US2 (pre-flight integration), US3 (needs_human list quality).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: Which user story this task belongs to

---

## Phase 1: Setup

**Purpose**: Confirm existing files match plan.md structure before rewriting.

- [x] T001 Verify `plugin/ai-mentor/agents/healer.md` and `plugin/ai-mentor/skills/heal/SKILL.md` exist and their frontmatter parses as valid YAML (name, description, model fields present per plan.md project structure)
- [x] T002 Confirm all `specs/003-healer-agent/` design artifacts are present: plan.md, research.md, data-model.md, contracts/result-contract.md, quickstart.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared infrastructure both the agent and skill depend on — must complete before US1 work begins.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T003 Update `plugin/ai-mentor/agents/healer.md` principles section — add explicit statements of: (a) portal writes are strictly limited to capability declaration republish (FR-007); (b) pre-flight skip requires all 7 checks to return `ok` (FR-008 / data-model.md `SessionState.all_checks_ok`); (c) degraded mode: skip portal checks and note them as `blocked` when Artifact tool is unavailable
- [x] T004 Verify `plugin/ai-mentor/skills/mentor-core/SKILL.md` Result contract is compatible with the healer's extended `result:` schema — confirm the base `agent`, `scope`, `status`, `needs_human`, `writes` fields are present and that adding `checks[]` and `fixes_applied[]` does not conflict; document any delta in `contracts/result-contract.md` notes section

**Checkpoint**: healer.md principles and Result contract compatibility confirmed — US1 can begin.

---

## Phase 3: User Story 1 — Run a Full Platform Health Check (Priority: P1) 🎯 MVP

**Goal**: `/heal` runs all 7 checks, auto-fixes safe issues, and returns a valid `result:` block in one turn.

**Independent Test**: Invoke `/heal` on a clean repo; verify the result block has exactly 7 `checks` entries, each with `name`, `status`, and `detail` fields per `data-model.md CheckResult`; verify `fixes_applied` and `needs_human` are present arrays; verify `writes` is present (quickstart.md Scenario 1).

- [x] T005 [P] [US1] Rewrite Check 1 (portal-reachability) in `plugin/ai-mentor/skills/heal/SKILL.md` — read the portal artifact using the slug from `mentor-core/SKILL.md`; set `CheckResult.status: ok` when artifact loads and title contains "AiMentor", `blocked` otherwise; never hardcode the slug
- [x] T006 [P] [US1] Rewrite Check 2 (capability-audit) in `plugin/ai-mentor/skills/heal/SKILL.md` — grep portal HTML for all `claude.use('x')` calls; compare against `<artifact-stored-declaration>`; compute union of declared + missing; republish portal with union set if delta is non-empty (additive-only per research.md Decision 5); record one `Fix` per data-model.md with `path: "portal artifact ACBVYCSsYnWtD5ngzXz3dW (capability declaration)"`; set status `fixed` or `ok`
- [x] T007 [P] [US1] Rewrite Check 3 (url-consistency) in `plugin/ai-mentor/skills/heal/SKILL.md` — grep all `.md` files under `plugin/` for `artifact/` URL slugs; compare each against the canonical slug from `mentor-core/SKILL.md`; Edit each file with a stale slug; record one `Fix` per data-model.md with `path: "<file>:<line> <old> → <new>"`; set status `fixed` or `ok`
- [x] T008 [P] [US1] Rewrite Check 4 (file-references) in `plugin/ai-mentor/skills/heal/SKILL.md` — parse each skill's SKILL.md under `plugin/ai-mentor/skills/` for `Load references/X` patterns; for each referenced file, check for existence at `references/<X>` (repo root); if missing, copy from `plugin/ai-mentor/skills/mentor-core/references/<X>`; record one `Fix` per data-model.md; escalate under `needs_human` if the source copy also does not exist; set status `fixed`, `ok`, or `needs_human`
- [x] T009 [US1] Rewrite Check 5 (db-smoke-test) in `plugin/ai-mentor/skills/heal/SKILL.md` — load ArtifactData via ToolSearch; run `db_list` on `trainees` collection and `db_get` on `settings/program`; record trainee count and `startDate` in `CheckResult.detail`; never write portal data; add one `Escalation` per data-model.md for: (a) 0 trainees → "Add trainee cohort before D1 (2026-11-30)", hint: "Open portal → Trainees tab → Add trainee"; (b) missing settings/program → "Seed settings/program via portal Setup tab", hint: "Open portal → Setup tab → Save"; set status `ok` or `needs_human`
- [x] T010 [P] [US1] Rewrite Check 6 (agent-frontmatter) in `plugin/ai-mentor/skills/heal/SKILL.md` — Read each `.md` file under `plugin/ai-mentor/agents/`; verify YAML frontmatter has `name` (matches filename stem), `description` (non-empty), `model` (non-empty); add `model: inherit` only when `model` is absent; record one `Fix` per data-model.md for each edit; escalate under `needs_human` when `description` is absent (cannot infer intent); set status `fixed`, `ok`, or `needs_human`
- [x] T011 [P] [US1] Rewrite Check 7 (full-flow-wiring) in `plugin/ai-mentor/skills/heal/SKILL.md` — grep `plugin/ai-mentor/skills/full-flow/SKILL.md` for specialist agent names (tutor-*, exam-grader, dod-auditor, healer); for each name found, verify a `.md` exists at `plugin/ai-mentor/agents/<name>.md`; add one `Escalation` per missing agent; set status `ok` or `needs_human`
- [x] T012 [US1] Rewrite the result-block section of `plugin/ai-mentor/skills/heal/SKILL.md` — emit `HealResult` per `contracts/result-contract.md` schema: `agent: healer`, `scope: system`, `status` derived from check outcomes (done/partial/blocked per rules table in contracts), `checks[]` with all 7 `CheckResult` entries, `fixes_applied[]`, `needs_human[]` with `message` + `hint` fields per data-model.md `Escalation`, `writes[]`

**Checkpoint**: `/heal` returns a valid 7-check result block — US1 is independently testable.

---

## Phase 4: User Story 2 — Pre-flight Check Before Full-flow (Priority: P2)

**Goal**: mentor-lead dispatches healer as pre-flight; skip re-run when `SessionState.all_checks_ok`; block full-flow when portal is unreachable.

**Independent Test**: Inject a known capability gap; trigger `/full-flow`; verify healer pre-flight runs and either fixes the gap or blocks the flow before specialist agents dispatch (quickstart.md Scenario 6).

- [x] T013 [US2] Update `plugin/ai-mentor/skills/full-flow/SKILL.md` pre-flight section — document the skip condition explicitly: "skip only when all 7 checks returned `ok` in this session (`SessionState.all_checks_ok` per data-model.md); if any check returned `fixed`, `blocked`, or `needs_human`, re-run on next invocation (FR-008)"
- [x] T014 [US2] Update `plugin/ai-mentor/agents/healer.md` — add a Principles line stating: "Pre-flight skip: track `all_checks_ok` in-memory only (data-model.md SessionState); never write this flag to portal db; the flag is lost when the session ends — this is intentional (research.md Decision 4)"

**Checkpoint**: Pre-flight integration complete — US2 independently testable by triggering `/full-flow` and observing healer dispatch behaviour.

---

## Phase 5: User Story 3 — Review What Needs Human Action (Priority: P3)

**Goal**: `needs_human` list is complete, actionable, and free of false positives after every heal run.

**Independent Test**: Run `/heal` with 0 trainees and no `settings/program`; verify `needs_human` contains both items with `message` and `hint`; verify no auto-fixable item appears in `needs_human` (quickstart.md Scenario 3 from US3 acceptance scenarios).

- [x] T015 [US3] Audit all 7 check implementations in `plugin/ai-mentor/skills/heal/SKILL.md` — for every path that sets `status: needs_human` or `status: blocked`, verify an `Escalation` entry exists with both `message` (actionable) and `hint` (resolution step) per data-model.md; add missing hints for: Google Drive not connected ("Connect Google Drive in claude.ai Settings → Connectors"), portal owned by different account ("Republish portal from the owning account")
- [x] T016 [US3] Verify `writes` field logic in `plugin/ai-mentor/skills/heal/SKILL.md` result-block section — confirm it emits `["portal capability declaration (republish)"]` when Check 2 republished, and `["none"]` otherwise; confirm no trainee/score/dod/progress path ever appears in `writes` (FR-007 / SC-004)

**Checkpoint**: All 3 user stories complete — platform is fully spec-compliant.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T017 [P] Validate `heal/SKILL.md` Check 3 (url-consistency) against quickstart.md Scenario 2 — inject stale URL `CFwkey5bsgH7TobusYViVE` in `plugin/ai-mentor/README.md`; run `/heal`; confirm `url-consistency.status: fixed`, fix path includes `plugin/ai-mentor/README.md:35`, correct slug restored
- [ ] T018 [P] Validate `heal/SKILL.md` degraded-mode path against quickstart.md Scenario 7 — run from a session without Artifact tool; confirm `status: partial`, portal checks are `blocked` with reason "Artifact tool not available in this session", remaining 5 checks run normally
- [ ] T019 [P] Run quickstart.md Scenario 1 (baseline) and Scenario 5 (idempotency) — invoke `/heal` twice with no intervening changes; record both `result:` blocks; verify SC-001 (completes in one turn) and SC-005 (both blocks identical)
- [ ] T020 [P] Run quickstart.md Scenario 8 (human-data protection) — add a trainee with a known score; run `/heal`; re-read portal `trainees/<id>` and `scores/<id>_M1`; confirm both documents unchanged; confirm `result.writes` contains no trainee/score/dod/progress path (SC-004)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — BLOCKS all user stories
- **US1 (Phase 3)**: Depends on Phase 2 — 7 check tasks (T005–T011) parallelisable; T012 depends on T005–T011
- **US2 (Phase 4)**: Depends on Phase 3 complete (needs valid result block from US1)
- **US3 (Phase 5)**: Depends on Phase 3 complete (checks must exist before auditing escalation paths)
- **Polish (Phase 6)**: Depends on all 3 user stories complete

### User Story Dependencies

- **US1 (P1)**: Starts after Foundational — no dependency on US2 or US3
- **US2 (P2)**: Depends on US1 (pre-flight reads the result block US1 defines)
- **US3 (P3)**: Depends on US1 (needs_human paths are part of each check defined in US1)

### Within US1

- T005–T011 (the 7 checks): all marked [P] — can be drafted in parallel since each targets a different section of `heal/SKILL.md`
- T012 (result block): depends on T005–T011 being complete (references all 7 check names and status rules)

---

## Parallel Example: User Story 1

```text
# Launch all 7 check rewrites in parallel (different sections of heal/SKILL.md):
Task T005: Check 1 — portal-reachability
Task T006: Check 2 — capability-audit
Task T007: Check 3 — url-consistency
Task T008: Check 4 — file-references
Task T009: Check 5 — db-smoke-test  (not [P] — references Escalation items from T008 pattern)
Task T010: Check 6 — agent-frontmatter
Task T011: Check 7 — full-flow-wiring

# Then T012 (result block) once all 7 checks are written
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T002)
2. Complete Phase 2: Foundational (T003–T004)
3. Complete Phase 3: US1 — 7 checks + result block (T005–T012)
4. **STOP and VALIDATE**: Run quickstart.md Scenario 1
5. MVP complete: `/heal` works end-to-end

### Incremental Delivery

1. Setup + Foundational → agent and skill principles aligned
2. US1 → `/heal` returns valid 7-check result block (MVP)
3. US2 → pre-flight integration with `/full-flow`
4. US3 → needs_human list complete and actionable
5. Polish → idempotency and data-protection scenarios validated

### Notes

- [P] tasks in Phase 3 edit different sections of `heal/SKILL.md` — coordinate section boundaries to avoid conflicts if working in parallel
- T009 (db smoke test) is NOT [P] because it loads ArtifactData via ToolSearch, which must complete before the Escalation pattern can be verified
- Commit after each phase checkpoint to preserve a known-good state
- The existing `healer.md` and `heal/SKILL.md` are draft versions — these tasks revise them in-place per the spec rather than deleting and recreating
