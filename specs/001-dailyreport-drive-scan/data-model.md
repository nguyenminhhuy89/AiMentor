# Data Model: DailyReport Drive Scan

## Firestore Collections

### `progress/<traineeId>` (existing, extended)

One document per trainee. Written exclusively by the portal scan; `dashboard-publish` reads it for the master timeline.

| Field | Type | Source | Notes |
|---|---|---|---|
| `traineeId` | string | Profile tab / filename | Matches `trainees/<id>` |
| `name` | string | Profile tab "Full name" | |
| `sheetId` | string | Drive file ID | |
| `sheetName` | string | Drive file title | |
| `url` | string | Drive `viewUrl` | Must start with `https://` |
| `scannedAt` | ISO 8601 string | Scan time | |
| `bootcampDay` | number | `workDay()` at scan time | Day 0 = before start |
| `topicsTotal` | number | Topic Tracker rows with numeric Day | |
| `topicsDone` | number | rows where status === "Done" | |
| `doneWithProof` | number | Done AND `r[7]` matches `^https?://` | Column 7 = Evidence Link |
| `doneNoProof` | number | Done AND no valid URL in Evidence Link | |
| `due` | number | topics where Day ≤ bootcampDay | |
| `behind` | number | due topics where NOT (Done AND proof) | |
| `dodMet` | number | DoD Checklist rows where met === "Yes" | |
| `dodTotal` | number | DoD Checklist rows matching `^M[1-6]$` | |
| `flags` | string[] | Computed warnings (see Flag Rules) | |
| `status` | "On track" \| "Watch" \| "At risk" | Derived from behind + mustNo | |
| `by` | string | `"portal scan"` | Authorship per constitution |
| `isSample` | boolean? | Set to `true` only on demo records | Absent or `false` = real scan |

**Flag Rules:**
- `doneNoProof > 0` → `"{n} topic(s) marked Done with no evidence link"`
- Topics with Day > bootcampDay marked Done → `"{n} topic(s) marked Done before their day"`
- MUST DoD items where met !== "Yes" → `"MUST not met: {mod}"`
- Profile fields missing (Squad, Mentor, Repo link) → `"Profile missing: {fields}"`

**Status Rules:**
- `mustNo.length > 0` OR `behind >= 6` → `"At risk"`
- `behind >= 3` → `"Watch"`
- Otherwise → `"On track"`

---

### `trainees/<traineeId>` (existing — no longer auto-created by scan)

The scan previously auto-created trainee records for unknown IDs. Under FR-006, the scan MUST NOT create trainee records for IDs not already in the roster. Auto-creation is removed.

---

## Scan Result Objects (in-memory, not persisted)

### `UnmatchedEntry`

Sheets the scan could not confidently attribute to a roster trainee, or detected as duplicates. Surfaced in the summary panel; never written to Firestore.

| Field | Type | Description |
|---|---|---|
| `title` | string | Drive file title |
| `fileId` | string | Drive file ID |
| `reason` | string | "no TraineeID found", "unknown trainee ID: {id}", "duplicate sheets for trainee {id}", "incomplete sheet: missing Topic Tracker tab", "incomplete sheet: missing DoD Checklist tab" |

### `FailedEntry`

Sheets the scan attempted to read but hit a Drive error.

| Field | Type | Description |
|---|---|---|
| `title` | string | Drive file title |
| `fileId` | string | Drive file ID |
| `errorCode` | string | Drive error code or "error" |

### `ScanSummary`

Rendered in the summary panel after scan completes.

| Field | Type | Description |
|---|---|---|
| `matched` | number | Progress records successfully written |
| `unmatched` | UnmatchedEntry[] | Sheets with identity or duplicate issues |
| `failed` | FailedEntry[] | Sheets that couldn't be read |
| `scannedAt` | ISO 8601 string | When the scan ran |

---

## Topic Tracker Tab — Column Layout

The portal reads the Topic Tracker tab as a markdown table (via Drive connector). Column indices (0-based):

| Index | Column Name |
|---|---|
| 0 | Day |
| 1 | Week |
| 2 | Module |
| 3 | Topic |
| 4 | Depth (H/G/A) |
| 5 | Status |
| 6 | Notes |
| 7 | Evidence Link |

A row is a valid topic when `r[0]` is a numeric string (Day number).
A topic is "Done with proof" when `r[5] === "Done"` AND `r[7]` matches `/^https?:\/\//i`.

---

## DoD Checklist Tab — Column Layout

| Index | Column Name |
|---|---|
| 0 | Module (M1–M6) |
| 1 | Day |
| 2 | Item |
| 3 | Type (MUST/SHOULD) |
| 4 | Notes |
| 5 | Met (Yes/No) |

A row is a valid DoD item when `r[0]` matches `/^M[1-6]$/`.
