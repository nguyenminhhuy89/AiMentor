# Feature Specification: DailyReport Drive Scan

**Feature Branch**: `001-dailyreport-drive-scan`

**Created**: 2026-11-24

**Status**: Draft

**Input**: User description: "Wire the AiMentor portal's DailyReport scan to the Google Drive "DailyReport" folder (1iQLe_c_h2J8a5JXFZ7_7TyFb5evwA5fb), so the portal reads each trainee's daily progress sheet (Topic Tracker and DoD Checklist tabs) directly from that folder instead of relying on manually-entered or sample progress data. The scan must match each sheet to a trainee by TraineeID/name, parse Topic Tracker status per topic and DoD Checklist Met/Not-Met items into the portal's progress collection (per mentor-core's documented schema), flag sheets that don't match a known trainee instead of guessing, and keep sample/mock data clearly labeled and excluded from real scans. This builds on today's existing portal progress-record work for trainee HUYNM27."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Mentor sees real per-trainee progress on demand (Priority: P1)

A mentor-lead or program owner opens the portal and triggers a DailyReport scan. The portal reads every trainee's daily progress sheet directly from the Drive DailyReport folder and shows each trainee's current topic completion and DoD status, replacing hand-entered or sample numbers.

**Why this priority**: This is the core value of the feature — without it, the portal shows stale, manually-typed, or sample data, which is exactly what today's HUYNM27 record already exposed as a problem (pre-start scan with mismatched DoD total, empty email/team fields).

**Independent Test**: Can be fully tested by running a scan against the DailyReport folder with at least one real trainee sheet present, and confirming the portal's progress record for that trainee updates with topic and DoD counts read from the sheet, not typed in by a mentor.

**Acceptance Scenarios**:

1. **Given** a trainee's daily progress sheet exists in the DailyReport folder with a Topic Tracker tab, **When** a scan runs, **Then** the portal's progress record for that trainee shows topicsTotal/topicsDone/doneWithProof/doneNoProof counts matching the sheet's current status values.
2. **Given** the same sheet also has a DoD Checklist tab, **When** a scan runs, **Then** the progress record's dodMet/dodTotal counts match the Met/Not-Met items on that tab.
3. **Given** a scan has already populated a progress record for a trainee, **When** the scan runs again after the trainee updates their sheet, **Then** the existing record is overwritten with the new counts and a new `scannedAt` timestamp, not duplicated.
4. **Given** a scan completes with some sheets matched and some unmatched or failed, **When** the mentor views the portal, **Then** a scan summary panel shows the matched count, unmatched/flagged count, and failed-read count alongside the updated progress view.

---

### User Story 2 - Mentor is warned about sheets that can't be matched to a trainee (Priority: P2)

A mentor runs a scan and one or more sheets in the DailyReport folder don't clearly belong to any known trainee (missing/garbled TraineeID, name typo, or a sheet for someone not in the cohort roster). The scan does not guess; it lists these sheets separately so a human can resolve them.

**Why this priority**: Guessing a wrong match would silently attribute one trainee's progress to another, corrupting grading-adjacent data — the constitution's "Human Judgement Over Automation" principle requires this kind of ambiguity to go to a human, not be resolved automatically.

**Independent Test**: Can be fully tested by placing a sheet in the folder whose name/ID doesn't match any roster entry, running a scan, and confirming it appears in an "unmatched" list with no progress record created or altered for any trainee.

**Acceptance Scenarios**:

1. **Given** a sheet whose filename does not parse into a recognizable TraineeID or name, **When** a scan runs, **Then** the sheet is listed as unmatched and no trainee's progress record is created or changed from it.
2. **Given** a sheet whose TraineeID does not exist in the current cohort roster, **When** a scan runs, **Then** the sheet is listed as unmatched with the reason "unknown trainee ID", and existing progress records are left untouched.
3. **Given** two sheets in the folder appear to belong to the same trainee (e.g., a duplicate), **When** a scan runs, **Then** both are flagged for human review instead of one being silently chosen.

---

### User Story 3 - Mentor can trust that sample data never looks like a real scan (Priority: P3)

A mentor or program owner viewing the portal can always tell sample/mock progress data apart from data produced by a real Drive scan, so a demo or test run never gets mistaken for real cohort progress.

**Why this priority**: Today's portal mock data and timeline sample rows are not labeled as sample, which risks a trainee's displayed status being mistaken for real progress — a lower-frequency but still real trust problem once real scans exist alongside any leftover samples.

**Independent Test**: Can be fully tested by inspecting the progress collection and portal UI and confirming every sample/mock record carries a visible marker distinguishing it from scan-produced records, and that a real scan run never reads or merges sample records.

**Acceptance Scenarios**:

1. **Given** sample progress records exist from earlier demos, **When** a real scan runs, **Then** the scan does not read, update, or count those sample records as part of cohort progress.
2. **Given** a mentor views the portal's progress list, **When** a record originated as sample/mock data, **Then** it is visibly labeled as sample in the UI.

### Edge Cases

- What happens when the DailyReport folder is unreachable (Drive auth expired, folder moved/renamed)? The scan MUST fail visibly with an actionable error, not silently show stale or empty data as if it were current.
- What happens when a trainee's sheet exists but a Topic Tracker or DoD Checklist tab is missing or renamed? The sheet MUST be flagged as incomplete rather than scored with assumed zeros.
- What happens when a sheet's Topic Tracker shows a topic "Done" with no evidence link? Per the existing `doneWithProof`/`doneNoProof` distinction, it MUST count as `doneNoProof`, not plain `topicsDone`-without-caveat.
- What happens when the scan runs mid-edit, i.e., a trainee has the sheet open and partially changed? The scan MUST read whatever the sheet currently contains without special handling of unsaved client-side edits in the trainee's browser (Sheets autosaves).
- How does the system handle a sheet that matches a trainee who has withdrawn or is no longer in the cohort roster? It MUST be treated as unmatched/flagged, not auto-removed or auto-merged.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The portal MUST scan the entire Google Drive "DailyReport" folder (ID `1iQLe_c_h2J8a5JXFZ7_7TyFb5evwA5fb`) for per-trainee progress sheets in a single operation (full cohort scan); per-trainee selective scanning is out of scope for v1.
- **FR-002**: For each sheet in the folder, the scan MUST attempt to match it to exactly one trainee in the current cohort roster using the sheet's TraineeID and/or name.
- **FR-003**: For each matched sheet, the scan MUST read the Topic Tracker tab and compute topicsTotal, topicsDone, doneWithProof, and doneNoProof. A topic counts as `doneWithProof` only when its status is "Done" AND its dedicated "Evidence" or "Link" column contains a non-empty URL; otherwise a "Done" topic without that URL counts as `doneNoProof`.
- **FR-004**: For each matched sheet, the scan MUST read the DoD Checklist tab and compute dodMet and dodTotal from its Met/Not-Met items.
- **FR-005**: The scan MUST write one progress record per matched trainee to the portal's `progress/<traineeId>` collection, using the schema `{traineeId, name, sheetId, sheetName, url, scannedAt, bootcampDay, topicsTotal, topicsDone, doneWithProof, doneNoProof, due, behind, dodMet, dodTotal, status, flags, by}` documented in mentor-core, overwriting any prior record for that trainee rather than creating a duplicate.
- **FR-006**: The scan MUST NOT guess a match for a sheet when the TraineeID/name does not clearly resolve to exactly one roster entry; such sheets MUST be reported in an unmatched/flagged list instead, with a reason, and MUST NOT result in a progress record being created or altered.
- **FR-007**: The scan MUST flag (not silently resolve) the case of two or more sheets that appear to match the same trainee.
- **FR-008**: Sample or mock progress records (e.g., portal demo data, timeline sample rows) MUST be visibly labeled as sample in the portal UI and MUST be excluded from the set of records a real scan reads, writes, or aggregates.
- **FR-009**: Every write the scan makes to the progress collection MUST record `by` naming the scan as its author, consistent with the portal's existing requirement that every write name its author.
- **FR-012**: Only mentor-lead and program owner roles MUST be able to trigger a DailyReport scan; trainees and read-only roles MUST NOT have access to the scan action.
- **FR-010**: If the DailyReport folder cannot be reached (authentication or access failure), the scan MUST surface a visible, actionable error and MUST NOT leave the mentor believing displayed progress is current when it is not.
- **FR-011**: If a matched sheet is missing its Topic Tracker or DoD Checklist tab, the scan MUST flag that trainee's sheet as incomplete rather than recording zero/default values for the missing tab's metrics.
- **FR-013**: If the scan fails to read one trainee's sheet mid-run (e.g., a permissions error on that file), the scan MUST continue processing the remaining sheets and report the failed sheet in the same flagged list as unmatched sheets, with the reason for failure. Progress records for successfully read sheets MUST still be written.
- **FR-014**: After a scan completes, the portal MUST display a scan summary panel showing the counts of matched sheets (progress records written), unmatched/flagged sheets (with reasons), and failed reads; this panel MUST appear alongside the updated progress view so mentors can assess data completeness at a glance.

### Key Entities

- **Progress record** (`progress/<traineeId>`): One per trainee, produced by a scan of their Drive daily report sheet; holds topic-completion counts, DoD counts, a status/flags summary, and scan provenance (`scannedAt`, `by`, `sheetId`/`url`). Defined in mentor-core.
- **Unmatched sheet entry**: A sheet found in the DailyReport folder that the scan could not confidently attribute to one roster trainee; holds the sheet's identity, a reason, and is surfaced for human resolution. It does not become a progress record.
- **Cohort roster**: The set of currently enrolled trainees (TraineeID, name) a scan matches sheets against; sheets for IDs outside this set are treated as unmatched.
- **Sample/mock progress record**: A progress-shaped record not produced by a real scan (demo or test data), visibly labeled as such and excluded from real-scan reads and writes.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A mentor can view up-to-date topic and DoD progress for every matched trainee within one scan run, with no manual data entry required.
- **SC-002**: 100% of sheets that cannot be confidently matched to a roster trainee are surfaced for human review, and 0% result in a progress record being created or changed for the wrong trainee.
- **SC-003**: 0% of sample/mock progress records are mistaken for real progress in the portal UI (every sample record is visibly labeled) or counted in a real scan's results.
- **SC-004**: When the DailyReport folder is unreachable, 100% of scan attempts surface a visible error instead of showing unflagged stale data.

## Clarifications

### Session 2026-11-24

- Q: How does a trainee's daily progress sheet indicate that a "Done" topic has evidence attached? → A: A non-empty URL/link in a dedicated "Evidence" or "Link" column next to the topic row; any "Done" topic without that URL counts as `doneNoProof`.
- Q: Who is allowed to trigger a DailyReport scan in the portal? → A: Only mentor-lead and program owners; trainees and read-only roles cannot trigger a scan.
- Q: Should a scan always cover the full cohort or allow single-trainee targeting? → A: Full cohort only for v1; per-trainee selective scanning is out of scope.
- Q: If one trainee's sheet fails mid-run, should the scan continue or abort? → A: Continue and report per-sheet failures in the flagged list; successfully read sheets still get their progress records written.
- Q: After a scan completes, what does the mentor see — a summary panel or just the updated progress view? → A: A scan summary panel showing counts of matched, unmatched/flagged, and failed sheets, displayed alongside the updated progress view after each scan.

## Assumptions

- The cohort roster (TraineeID, name, email, team) is available to the scan from the portal's existing trainee records; this feature does not define how the roster itself is populated.
- The DailyReport folder continues to hold one progress sheet per trainee, created from the daily report template (per CLAUDE.md), with Topic Tracker and DoD Checklist tabs named consistently enough to be located by tab name.
- "On demand" scanning (triggered by a mentor action in the portal) is sufficient for v1; a scheduled/automatic recurring scan is out of scope unless requested later.
- The pending decision to remove the Dashboard and Daily Report tabs from the template is independent of this feature and does not block it, since this feature only reads the Topic Tracker and DoD Checklist tabs.
- Matching logic can rely on the sheet filename convention (`<TraineeID>_<FullName>_...` per the Drive layout in CLAUDE.md) plus an in-sheet TraineeID/name field as a cross-check; exact fuzzy-matching thresholds are an implementation detail for the planning phase, not this spec.
