# Data Model: AiMentor Platform Healer Agent

**Branch**: `003-healer-agent` | **Date**: 2026-11-24

The healer agent operates on two categories of data: **in-memory run state** (never persisted) and **portal artifact capability declaration** (the only write the healer performs). All other portal collections (trainees, scores, dod, progress, settings) are read-only for the healer.

---

## Entities

### CheckResult

Represents the outcome of one of the 7 named verification steps.

| Field | Type | Constraints |
|---|---|---|
| `name` | string | One of: `portal-reachability`, `capability-audit`, `url-consistency`, `file-references`, `db-smoke-test`, `agent-frontmatter`, `full-flow-wiring` |
| `status` | enum | `ok` \| `fixed` \| `blocked` \| `needs_human` |
| `detail` | string | One-line description of what was found or done. Required. |

### Fix

Represents a change the healer applied automatically during the run.

| Field | Type | Constraints |
|---|---|---|
| `description` | string | Human-readable summary of the change. Required. |
| `path` | string | Repo-relative file path affected (e.g., `plugin/ai-mentor/README.md:35`). Required. |

### Escalation

Represents an issue the healer detected but cannot resolve without human action.

| Field | Type | Constraints |
|---|---|---|
| `message` | string | Actionable description (e.g., "Add trainee cohort before D1 (2026-11-30)"). Required. |
| `hint` | string | Optional suggested resolution (e.g., "Open portal → Trainees tab → Add trainee"). |

### HealResult

The top-level output of a heal run. Serialised as the `result:` yaml block in the agent's final message.

| Field | Type | Constraints |
|---|---|---|
| `agent` | string | Always `"healer"` |
| `scope` | string | Always `"system"` |
| `status` | enum | `done` (all checks ran) \| `partial` (some checks skipped, e.g., degraded mode) \| `blocked` (portal unreachable and no fallback) |
| `checks` | CheckResult[] | Exactly 7 entries when status is `done`; fewer when `partial` |
| `fixes_applied` | Fix[] | Empty array when nothing was changed |
| `needs_human` | Escalation[] | Empty array when nothing requires human action |
| `writes` | string[] | Portal paths written, or `["none"]` |

### SessionState (in-memory only)

Tracks whether the current session's last heal run was fully clean, to implement the pre-flight skip (FR-008).

| Field | Type | Constraints |
|---|---|---|
| `all_checks_ok` | boolean | `true` only when the last `HealResult.checks` contained exactly 7 entries all with `status: ok`. Never persisted. |

---

## Portal Collections (read-only for healer)

The healer reads these collections during Check 4 (db smoke test). It never writes to them.

| Collection | Key pattern | Healer reads |
|---|---|---|
| `trainees` | `trainees/<id>` | Count only — does not log individual trainee records |
| `settings/program` | `settings/program` | `startDate`, `driveFolder` fields only |

---

## Portal Capability Declaration (write target)

The healer's only portal write is an artifact republish that updates the stored capability declaration. The declaration is a JSON object at the artifact level, not a db document.

| Capability | Required by portal | Healer adds if missing |
|---|---|---|
| `db` | Yes — all db operations | Yes |
| `user` | Yes — write-permission check | Yes |
| `sample` | Yes — AI grading in portal | Yes |
| `mcp` | Yes — Google Drive scan | Yes (with `servers: [{server: "Google Drive", tools: ["search_files","read_file_content"]}]`) |

**Additive-only rule**: The healer computes `union(currently_declared, missing_required)`. If a capability is currently declared but not in the required set, it is kept. No capability is ever removed.
