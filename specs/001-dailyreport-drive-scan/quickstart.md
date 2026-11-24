# Quickstart Validation Guide: DailyReport Drive Scan

## Prerequisites

1. The portal artifact is published and accessible at its claude.ai URL.
2. You are signed into claude.ai with the account that owns the portal (chiaseanhneonguyen@gmail.com).
3. Google Drive connector is authorized for the AiMentor Drive.
4. At least one trainee exists in the portal (Trainees tab) with a known TraineeID (e.g., HUYNM27).
5. The trainee's daily report sheet is present in the DailyReport folder (`1iQLe_c_h2J8a5JXFZ7_7TyFb5evwA5fb`), named `HUYNM27_<FullName>_Progress`, with Topic Tracker and DoD Checklist tabs populated.

---

## Scenario 1 — Happy path: scan reads a real trainee's sheet (FR-001 through FR-005)

1. Open portal → **Daily progress reports** tab.
2. Click **Scan DailyReport**.
3. **During scan:** verify `repMsg` shows "Reading 1 of N: HUYNM27_…" progress text.
4. **After scan:** verify:
   - A scan summary panel appears (not just a text line) showing "Matched: 1".
   - The progress table shows a row for HUYNM27 with non-zero `topicsTotal`.
   - `doneWithProof` reflects only topics whose Evidence Link column starts with `https://`.
   - `doneNoProof` reflects topics marked Done with no URL in that column.
   - `dodMet` / `dodTotal` match the DoD Checklist's Met/Not-Met counts.
   - `scannedAt` is a recent timestamp.

**Expected outcome:** HUYNM27's progress record in Firestore (`progress/HUYNM27`) contains accurate topic and DoD counts, and the portal table row reflects them without manual entry.

---

## Scenario 2 — Unmatched sheet: filename doesn't identify a roster trainee (FR-006)

1. Upload a test sheet to the DailyReport folder named `UNKNOWN99_Test_Progress` (TraineeID not in roster, no Profile tab entry).
2. Click **Scan DailyReport**.
3. **After scan:** verify:
   - Scan summary panel shows "Unmatched: 1" with the filename and reason.
   - No new document appears in `progress/UNKNOWN99`.
   - HUYNM27's progress record is unchanged.

---

## Scenario 3 — Duplicate sheets for same trainee (FR-007)

1. Upload a second sheet for HUYNM27, named `HUYNM27_<FullName>_Progress_copy`.
2. Click **Scan DailyReport**.
3. **After scan:** verify:
   - Both HUYNM27 sheets appear in the unmatched/flagged section with reason "duplicate sheets for trainee HUYNM27".
   - Neither sheet's data was written (or if the original scan had already written a record, it was not overwritten by either duplicate).

---

## Scenario 4 — Sample data remains labeled and excluded (FR-008)

1. Confirm a sample progress record exists in Firestore with `isSample: true`.
2. Inspect the portal table: the sample row shows a "SAMPLE" badge or label.
3. Click **Scan DailyReport** (with real sheets present).
4. **After scan:** verify the sample record's `scannedAt` has not changed (scan did not touch it).
5. KPI aggregates (Avg score, DoD done) do not include the sample record's values.

---

## Scenario 5 — Single sheet read failure mid-scan (FR-013)

1. Revoke the portal's read permission on one specific sheet in the DailyReport folder (or use a sheet in a sub-folder the connector cannot reach).
2. Click **Scan DailyReport** (with 2+ sheets present, one inaccessible).
3. **After scan:** verify:
   - Scan summary shows the failed sheet in a "Failed reads" section with an error code.
   - Other trainees' progress records were still written successfully.
   - `repMsg` or summary indicates partial success, not a complete failure.

---

## Scenario 6 — Access control: non-mentor cannot trigger scan (FR-012)

1. Open the portal as a user without edit/mentor access (or with `S.canWrite = false`).
2. Navigate to the **Daily progress reports** tab.
3. **Verify:** the "Scan DailyReport" button is disabled or absent; attempting to invoke the scan via devtools returns an error message, not a scan run.

---

## Verifying Firestore directly

In the portal's Setup tab (or via firebase console for the owning account), inspect `progress/<traineeId>` documents to confirm:
- `by === "portal scan"` on all real records
- `isSample` absent or `false` on all real records
- `scannedAt` matches the scan timestamp shown in the summary panel
