# Quickstart Validation Guide: AiMentor Platform Healer Agent

**Branch**: `003-healer-agent` | **Date**: 2026-11-24

---

## Prerequisites

- Claude Code running with the ai-mentor plugin: `claude --plugin-dir ./plugin/ai-mentor`
- Working directory: `~/Documents/AiMentor`
- Portal artifact accessible at `https://claude.ai/artifact/ACBVYCSsYnWtD5ngzXz3dW`

---

## Scenario 1 — Baseline clean run (SC-001, SC-002)

**Goal**: Confirm all 7 checks run and return a valid `result:` block in one turn.

**Steps:**
1. Invoke `/heal`
2. Read the `result:` block

**Expected outcome:**
- `status: done` or `status: partial` (if Artifact tool unavailable)
- Exactly 7 `checks` entries (or fewer in degraded mode, with a note)
- `fixes_applied` and `needs_human` both present (may be empty arrays)
- `writes` present

---

## Scenario 2 — Auto-fix: stale portal URL (FR-002, SC-002)

**Goal**: Verify the healer detects and fixes a stale URL in a plugin file.

**Setup:** Edit `plugin/ai-mentor/README.md` and change the portal URL slug to `CFwkey5bsgH7TobusYViVE` (a known stale value).

**Steps:**
1. Invoke `/heal`
2. Read `result.checks` for `url-consistency`
3. Read `result.fixes_applied`

**Expected outcome:**
- `url-consistency.status: fixed`
- `fixes_applied` contains an entry with `path: plugin/ai-mentor/README.md:35`
- `plugin/ai-mentor/README.md` now contains the correct slug `ACBVYCSsYnWtD5ngzXz3dW`

---

## Scenario 3 — Auto-fix: missing reference file (FR-003)

**Goal**: Verify the healer copies a missing repo-root reference file.

**Setup:** Delete `references/rubrics.md`.

**Steps:**
1. Invoke `/heal`
2. Read `result.checks` for `file-references`

**Expected outcome:**
- `file-references.status: fixed`
- `fixes_applied` contains an entry mentioning `references/rubrics.md`
- `references/rubrics.md` exists again

---

## Scenario 4 — Auto-fix: missing portal capability (FR-001)

**Goal**: Verify the healer republishes the portal when a capability is missing.

**Setup:** This requires republishing the portal with one capability removed (e.g., remove `sample` from the declaration). Do this via the Artifact tool or note it as a manual test.

**Steps:**
1. Invoke `/heal`
2. Read `result.checks` for `capability-audit`
3. Read `result.writes`

**Expected outcome:**
- `capability-audit.status: fixed`
- `writes` contains `"portal capability declaration (republish)"`
- Portal artifact (re-read) now has `sample` declared again

---

## Scenario 5 — Idempotency (SC-005)

**Goal**: Verify running `/heal` twice produces the same report when no changes occur between runs.

**Steps:**
1. Invoke `/heal` — record `result`
2. Invoke `/heal` again immediately — record `result`

**Expected outcome:**
- Both `result` blocks are identical in `checks[*].status`, `fixes_applied`, `needs_human`, and `writes`
- No new fixes applied in the second run

---

## Scenario 6 — Pre-flight skip (FR-008)

**Goal**: Verify the healer skips re-running in pre-flight when all 7 checks were `ok`.

**Setup:** Run `/heal` until all 7 checks return `ok`. Then invoke `/full-flow` (which triggers pre-flight).

**Expected outcome:**
- The full-flow summary notes "healer skipped (ran cleanly this session)"
- No second healer dispatch occurs

**Counter-test:** If any check returned `fixed` or `needs_human` in the last run, the healer MUST re-run on the next `/full-flow`. Verify by checking the full-flow dispatch log.

---

## Scenario 7 — Degraded mode (edge case: Artifact tool unavailable)

**Goal**: Verify the healer completes file checks even without portal access.

**Setup:** Run from a Claude Code session that does not have the Artifact tool available.

**Expected outcome:**
- `status: partial`
- `portal-reachability.status: blocked` with detail "Artifact tool not available in this session"
- `capability-audit.status: blocked` (depends on portal)
- Remaining 5 checks (`url-consistency`, `file-references`, `db-smoke-test`, `agent-frontmatter`, `full-flow-wiring`) run normally

---

## Scenario 8 — Human-data protection (FR-007, SC-004)

**Goal**: Verify the healer never modifies trainee, score, DoD, or progress data.

**Steps:**
1. Add a trainee to the portal with a known score
2. Invoke `/heal`
3. Read the portal `trainees/<id>` and `scores/<id>_M1` documents

**Expected outcome:**
- Both documents are identical to their pre-heal state
- `result.writes` does not list any trainee, score, dod, or progress paths
