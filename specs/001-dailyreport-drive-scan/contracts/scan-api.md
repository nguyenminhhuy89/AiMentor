# Contract: DailyReport Scan

The portal's DailyReport scan is a browser-side operation exposed via a single UI button. This contract documents its observable interface — inputs, outputs, and side effects — so that the exam-grader agent and dashboard-publish skill can depend on stable behavior.

---

## Trigger

**Actor:** Mentor-lead or program owner (role gate checked before dispatch)
**UI:** "Scan DailyReport" button in the **Daily progress reports** tab
**Gate:** `S.canWrite === true` AND user has edit access to portal (checked via `claude.use('user')`)

---

## Inputs (resolved at scan time)

| Input | Source | Description |
|---|---|---|
| Drive folder ID | Hardcoded: `1iQLe_c_h2J8a5JXFZ7_7TyFb5evwA5fb` | DailyReport folder in AiMentor Drive |
| Cohort roster | `S.trainees` (Firestore live snapshot) | Used to validate extracted TraineeIDs |
| Current bootcamp day | `workDay()` | Computed from `settings/program.startDate` |
| Scan timestamp | `new Date().toISOString()` | Written as `scannedAt` |

---

## Outputs

### Firestore writes (one per matched trainee)

Path: `progress/<traineeId>`

Schema: see [data-model.md](../data-model.md#progresstraineeid-existing-extended)

Guarantees:
- Overwrites any prior record for the same trainee (no duplicates).
- Never written for unmatched or failed sheets.
- Never overwrites a record that has `isSample: true` — sample records are excluded from match targets.
- `by` is always `"portal scan"`.

### UI side effects

- **During scan:** `repMsg` shows per-file progress ("Reading N of M: filename…")
- **After scan:** `repMsg` cleared; `repSummary` panel rendered with `ScanSummary` (see data-model)
- **Progress table** (`repTable`) reflects updated Firestore snapshot via live listener (no explicit re-render needed)

---

## Error Conditions

| Condition | Behavior |
|---|---|
| Drive connector unavailable | `repMsg` shows actionable error; button re-enabled; no Firestore writes |
| DailyReport folder not found by ID | `repMsg` shows "DailyReport folder not found — check Setup"; scan aborted |
| Sheet read fails mid-scan | Sheet added to `failed[]`; scan continues; other sheets processed normally |
| Extracted TraineeID not in roster | Sheet added to `unmatched[]` with reason; no Firestore write |
| Two sheets resolve to same TraineeID | Both added to `unmatched[]` with "duplicate" reason; neither written |
| Sheet missing Topic Tracker or DoD tab | Sheet added to `unmatched[]` with "incomplete sheet" reason |
| User lacks edit role | Scan button disabled; `repMsg` shows "Edit access required" if attempted |

---

## Stability Contract

The following are **stable** (downstream agents may depend on them):
- Firestore path `progress/<traineeId>` and all schema fields listed in data-model.md
- `by: "portal scan"` as the authorship value
- `isSample: true` as the marker for non-real records

The following are **internal** (may change without notice):
- UI element IDs (`repBtn`, `repMsg`, `repSummary`, `repTable`)
- Drive search pagination logic
- `parseReport()` column indices (tied to template structure)
