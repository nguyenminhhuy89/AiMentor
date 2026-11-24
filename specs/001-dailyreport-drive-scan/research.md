# Research: DailyReport Drive Scan

## Existing Code Audit

The portal already contains a `scanReports()` function in `portal/index.html` (lines ~386–428). This eliminates most unknowns — the planning phase is a targeted gap-fill, not a greenfield build.

---

### Decision: Folder lookup strategy
**Decision:** Use the Drive folder ID `1iQLe_c_h2J8a5JXFZ7_7TyFb5evwA5fb` directly in `search_files` rather than searching by name (`title contains 'DailyReport'`).
**Rationale:** Name search can hit the wrong folder if the owner renames it or has a similarly-named folder. The ID is stable and already in CLAUDE.md.
**Alternatives considered:** Searching by name (current code) — fragile if folder is renamed.

---

### Decision: Evidence URL detection (FR-003)
**Decision:** Existing code already uses `r[7]` with `/^https?:\/\//i` regex to detect proof links. Column index 7 corresponds to the "Evidence Link" column in the Topic Tracker tab's layout. This matches clarification answer A.
**Rationale:** The template's Topic Tracker columns are: Day | Week | Module | Topic | Depth | Status | Notes | Evidence Link. Index 7 (0-based) = Evidence Link.
**Alternatives considered:** None — the column position is fixed by the template structure.

---

### Decision: Trainee matching strategy (FR-002, FR-006, FR-007)
**Decision:** Two-tier matching:
1. Primary: extract TraineeID from Profile tab field `Trainee ID` (most reliable — explicitly typed).
2. Fallback: parse filename pattern `<TraineeID>_<FullName>_Progress` (regex `^([A-Za-z0-9-]+)_(.+?)_Progress`).
If neither yields a valid ID: **unmatched** (not added to `bad[]` read-errors).
If the extracted ID matches zero roster entries AND no auto-add is intended: **unmatched**.
If two files resolve to the same TraineeID before writing: **duplicate flagged**, neither written.
**Rationale:** Current code conflates unmatched and read-errors into one `bad[]` array, making it impossible to distinguish "can't identify" from "Drive read failed". Separating these gives mentors actionable information (unmatched = fix the sheet name; failed = check Drive permissions).
**Alternatives considered:** Auto-add unknown trainees (current behavior) — rejected per FR-006 (spec says flag, not auto-add).

---

### Decision: Role check for scan trigger (FR-012)
**Decision:** Use `claude.use('user')` → `u.can('role')` or `u.can('data.write')` to gate the Scan DailyReport button. The portal already checks `u.can('data.write')` to set `S.canWrite`. Extend this to disable the scan button for non-mentors.
**Rationale:** The `claude.use('user')` connector is already in use in the portal — no new capability needed. The role check at button click time (not just initial load) handles late permission changes.
**Alternatives considered:** Server-side Firestore rules — correct long-term, but out of scope for this portal-only change. The button-disable is a UX gate consistent with how the rest of the portal gates writes.

---

### Decision: Scan summary panel (FR-014)
**Decision:** Replace the single `repMsg` text line with a structured summary `<div id="repSummary">` rendered after scan completion, showing: matched count, unmatched list (with reasons), failed-read list (with error codes). Keep `repMsg` for in-progress status.
**Rationale:** A text message like "Scanned 3 report(s) · could not read: foo.xlsx (error)" is not scannable at a glance when there are many trainees. A structured panel matches the portal's existing table pattern and allows linking to unmatched sheets.
**Alternatives considered:** Inline repMsg only — rejected per FR-014 requirement for a summary panel alongside the updated progress view.

---

### Decision: Sample data labeling (FR-008)
**Decision:** Add an `isSample: true` field to any progress record written as demo/test data, and exclude records with `isSample: true` from real scan reads and aggregated KPI counts. Display a "SAMPLE" badge in the portal table row for such records.
**Rationale:** No existing mechanism distinguishes sample from real data. The simplest implementation is a boolean field on the Firestore document, which is cheap to filter on and easy to query.
**Alternatives considered:** Separate Firestore collection for sample data — overkill for a small cohort; a field on the same collection is simpler and consistent with the existing schema.

---

### Decision: Duplicate sheet detection (FR-007)
**Decision:** Before writing any progress records, build a map of `{traineeId → [files]}` from all resolved matches. Any trainee ID that maps to 2+ files → both files added to an `unmatched[]` list with reason "duplicate sheets for same trainee", and neither written.
**Rationale:** A second scan of the same folder could have genuine duplicates (trainee re-uploaded with a different filename). Silently picking one and writing it would corrupt the progress record without the mentor knowing.
**Alternatives considered:** Write the most-recently-modified file — rejected because "most recent" is ambiguous for simultaneous uploads, and the constitution requires human judgment on ambiguous matches.
