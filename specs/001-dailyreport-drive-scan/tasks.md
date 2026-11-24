# Tasks: DailyReport Drive Scan

**Input**: Design documents from `specs/001-dailyreport-drive-scan/`

**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/scan-api.md ✓, quickstart.md ✓

**Tests**: Not requested — validation covered by quickstart.md scenarios.

**Organization**: Tasks grouped by user story. All changes are targeted edits to `portal/index.html` only.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different functions/sections, no dependency on incomplete tasks)
- **[Story]**: Which user story this task belongs to

---

## Phase 1: Setup

**Purpose**: Load current portal state before any edits.

- [x] T001 Read `portal/index.html` in full to establish current state before editing

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core prerequisites that every user story depends on. Must complete before US phases.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T002 Add `const DAILY_REPORT_FOLDER_ID = '1iQLe_c_h2J8a5JXFZ7_7TyFb5evwA5fb'` constant near top of the script block in `portal/index.html`, then replace the two-step folder name search in `scanReports()` with a direct `search_files` query using `'${DAILY_REPORT_FOLDER_ID}' in ancestors` — removing the intermediate folder lookup entirely (research.md: Folder lookup strategy; FR-001)
- [x] T003 [P] Gate the `repBtn` in `portal/index.html`: set it `disabled` on initial render when `!S.canWrite`; add an early return at the top of `scanReports()` that calls `say('repMsg','Edit access required to run a scan.','fail')` and returns without any Drive call if `!db || !S.canWrite` (FR-012)

**Checkpoint**: Scan button uses correct folder ID and is gated to editors only.

---

## Phase 3: User Story 1 — Mentor sees real per-trainee progress on demand (Priority: P1) 🎯 MVP

**Goal**: A full-cohort scan reads every matched trainee's Topic Tracker and DoD Checklist tabs and writes accurate progress records to Firestore, replacing any manually-entered or stale data.

**Independent Test**: Run quickstart.md Scenario 1 — trigger a scan with HUYNM27's sheet present, confirm `progress/HUYNM27` in Firestore shows correct topicsTotal/doneWithProof/dodMet counts, and that `repMsg` shows per-file progress during the run.

- [x] T004 [US1] Refactor the per-sheet processing loop in `scanReports()` in `portal/index.html` to build three buckets instead of a single `bad[]`: `matched = []` for sheets with a valid, roster-confirmed TraineeID; `unmatched = []` for identity failures; `failed = []` for Drive read errors — for each sheet, resolve TraineeID first from the Profile tab field `Trainee ID`, then fall back to the filename regex `^([A-Za-z0-9-]+)_(.+?)_Progress`; push to `unmatched` with reason `"unknown trainee ID: {id}"` if the ID is absent from `S.trainees`, or with reason `"no TraineeID found"` if neither source yields a valid ID (FR-002, FR-006; data-model.md `UnmatchedEntry.reason`, `progress/<traineeId>.traineeId`)
- [x] T005 [US1] Remove the auto-add-to-roster block from `scanReports()` in `portal/index.html` (the lines that call `db.doc('trainees/'+tid).set(...)` and push to `S.trainees`) — after T004, trainees absent from the roster are already in `unmatched[]`, so this block is unreachable and must be deleted (FR-006)
- [x] T006 [US1] Write progress records for `matched[]` entries in `portal/index.html`: for each `{tid, pname, f, parsed}` in `matched`, compute all counts per data-model.md field definitions (`topicsTotal`, `topicsDone`, `doneWithProof` where `r[7]` matches `/^https?:\/\//i`, `doneNoProof`, `due`, `behind`, `dodMet`, `dodTotal`, `flags`, `status`, `bootcampDay`), then call `db.doc('progress/'+tid).set({...})` with `by:'portal scan'`; skip writing if the existing Firestore record has `isSample === true` (FR-005, FR-009; data-model.md `progress/<traineeId>` all fields including `doneWithProof` column-7 rule, `isSample`)
- [x] T007 [US1] Add `<div id="repSummary" class="card" style="display:none;margin-top:12px"></div>` to the Daily progress reports section in `portal/index.html` immediately after `repMsg`; implement `renderScanSummary({matched, unmatched, failed, scannedAt})` function that shows matched count in pass color and timestamp; call `renderScanSummary(summary)` and clear `repMsg` at the end of `scanReports()` (FR-014; data-model.md `ScanSummary`)

**Checkpoint**: US1 fully functional — scan reads real sheets, writes progress records, shows matched count.

---

## Phase 4: User Story 2 — Mentor warned about unmatched sheets (Priority: P2)

**Goal**: Any sheet that can't be confidently attributed to a roster trainee, fails to read, or is a duplicate surfaces in the scan summary panel with a reason — no progress record is ever created from ambiguous input.

**Independent Test**: Run quickstart.md Scenario 2 (unknown TraineeID), Scenario 3 (duplicate), and Scenario 5 (per-sheet failure) — each should appear in the summary panel with the correct reason, and no Firestore write should occur for them.

- [x] T008 [US2] Add duplicate detection in `scanReports()` in `portal/index.html` immediately after the per-sheet loop, before writing: group `matched[]` entries by `tid`; for any `tid` with 2 or more entries, move all of them to `unmatched[]` with reason `"duplicate sheets for trainee {tid}"` and remove them from `matched[]` so neither is written (FR-007; data-model.md `UnmatchedEntry.reason`)
- [x] T009 [US2] Extend `renderScanSummary()` in `portal/index.html` to render the `unmatched[]` list: when non-empty, add a "Flagged / unmatched" sub-section showing each entry as `<div class="sm fail">{title} — {reason}</div>` (FR-006, FR-007, FR-014; data-model.md `UnmatchedEntry`)
- [x] T010 [US2] Extend `renderScanSummary()` in `portal/index.html` to render the `failed[]` list: when non-empty, add a "Failed reads" sub-section showing each entry as `<div class="sm fail">{title} ({errorCode})</div>`; ensure the per-sheet catch block in `scanReports()` pushes `{title:f.title, fileId:f.id, errorCode:(e&&e.code)||'error'}` to `failed[]` instead of `bad[]` (FR-013, FR-014; data-model.md `FailedEntry`)

**Checkpoint**: US2 fully functional — unmatched and failed sheets surface with reasons; no silent drops.

---

## Phase 5: User Story 3 — Sample data never looks like a real scan (Priority: P3)

**Goal**: Progress records with `isSample: true` display a visible "SAMPLE" badge in the portal table and are excluded from KPI calculations, so a demo run is never mistaken for real cohort progress.

**Independent Test**: Run quickstart.md Scenario 4 — confirm sample record shows SAMPLE badge, KPI tiles exclude its values, and running a real scan leaves its `scannedAt` unchanged.

- [x] T011 [US3] In `renderReports()` in `portal/index.html`, append a `<span class="tag" style="--c:#9aa3af;font-size:11px;vertical-align:middle">SAMPLE</span>` after the trainee name text in the first table cell for any row where `p.isSample === true` (FR-008; data-model.md `progress/<traineeId>.isSample`)
- [x] T012 [P] [US3] In the KPI tile computations in `portal/index.html` (the functions that derive `kD` DoD-done and any progress-based averages), filter out records where `p.isSample === true` before aggregating so sample data never inflates or deflates cohort metrics (FR-008; data-model.md `progress/<traineeId>.isSample`)

**Checkpoint**: US3 fully functional — sample records visually labeled and excluded from metrics.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Error message quality, artifact publish, and end-to-end validation.

- [x] T013 Improve `driveErr()` in `portal/index.html` to detect auth-expired error codes (e.g., `401`, `authError`, `invalid_credentials`) and return `"Google Drive authorization expired — re-open the portal on claude.ai and allow Google Drive when prompted"` instead of the generic message; keep the existing fallback for other errors (FR-010)
- [ ] T014 Read the current published portal artifact, then republish `portal/index.html` as the portal artifact (overwriting the current version) — ⚠️ BLOCKED: portal artifact is owned by chiaseanhneonguyen@gmail.com; republish from that account's claude.ai session using the updated local `portal/index.html`
- [ ] T015 Validate the published portal against quickstart.md Scenarios 1 and 2 (happy path and unmatched sheet) — confirm matched record appears in progress table with correct counts, and the unmatched sheet appears in the summary panel with reason

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 — BLOCKS all user stories
- **Phase 3 (US1)**: Depends on Phase 2 — no dependency on US2 or US3
- **Phase 4 (US2)**: Depends on Phase 3 (builds on matched/unmatched/failed buckets from T004)
- **Phase 5 (US3)**: Depends on Phase 2 — independent of US1 and US2 (different functions)
- **Phase 6 (Polish)**: Depends on all user story phases complete

### User Story Dependencies

- **US1 (P1)**: Can start after Foundational (Phase 2)
- **US2 (P2)**: Depends on US1 (T004 defines the bucket architecture US2 extends)
- **US3 (P3)**: Can start after Foundational (Phase 2) — independent of US1/US2 at function level

### Within Each User Story

- T004 → T005 → T006 → T007 (sequential in US1 — each builds on the refactored loop)
- T008 → T009, T010 (T009 and T010 are independent of each other but both need T008)
- T011 and T012 are independent of each other [P]

### Parallel Opportunities

- T002 and T003 (Phase 2) touch different parts of the file — can run in parallel
- T011 and T012 (US3) touch different functions — can run in parallel
- T009 and T010 (US2) both extend `renderScanSummary()` — safer to run sequentially to avoid conflicts

---

## Parallel Example: Phase 2

```
# Both can run in parallel (different sections of portal/index.html):
Task T002: Add DAILY_REPORT_FOLDER_ID constant and replace folder search
Task T003: Gate repBtn and add early return in scanReports()
```

## Parallel Example: User Story 3

```
# Both touch different functions:
Task T011: Add SAMPLE badge in renderReports()
Task T012: Exclude isSample from KPI aggregation
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002, T003)
3. Complete Phase 3: US1 (T004–T007)
4. **STOP and VALIDATE**: Run quickstart.md Scenario 1
5. Publish and demo — real scan data flows to portal

### Incremental Delivery

1. Setup + Foundational → folder ID fixed, button gated
2. US1 → real scan writes to Firestore with summary panel (MVP)
3. US2 → unmatched/duplicate flagging surfaces in panel
4. US3 → sample data badges and KPI exclusion
5. Polish → error messages improved, artifact republished, validation complete

---

## Notes

- All 15 tasks edit exactly one file: `portal/index.html`
- [P] tasks touch different functions and can run concurrently
- No new connector capabilities needed — `claude.use('db')`, `claude.use('mcp')`, `claude.use('user')` are already declared
- T014 requires reading the live artifact before republishing (Artifact tool read → then publish)
- Commit `portal/index.html` after each phase checkpoint, not after each individual task
