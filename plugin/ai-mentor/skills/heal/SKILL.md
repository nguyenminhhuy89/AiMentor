---
name: heal
description: Automated health check and self-repair for the AiMentor platform. Audits the portal, skill/agent files, file references and db connectivity, then auto-fixes what it can. Use for "/heal", "system check", "auto-fix", "kiểm tra hệ thống".
---

# Heal

Run every check below in order. Auto-fix immediately when the fix is safe (file edit, portal republish). Never write to trainee, score, dod, progress, or settings portal db documents. Always produce a `result:` block at the end using the schema in the **Result block** section.

---

## Check 1 — Portal reachability (`portal-reachability`)

Read the portal artifact slug from `mentor-core/SKILL.md` — locate the line that sets the portal artifact URL. Use that slug to read the live artifact via the Artifact tool.

- **Pass** (`status: ok`): artifact loads, title contains "AiMentor".
- **Artifact tool unavailable** (`status: blocked`): set `detail: "Artifact tool not available in this session"`. Also set Check 2 to `blocked` with the same reason. Set `HealResult.status: partial`. Continue with Checks 3–7.
- **Fail / 404** (`status: needs_human`): add Escalation:
  - `message: "Portal artifact unreachable — slug in mentor-core/SKILL.md may be stale"`
  - `hint: "Open portal at claude.ai/artifact/<slug> in a browser to verify; update mentor-core/SKILL.md if the URL has changed"`

Do not attempt to fix the slug blindly.

---

## Check 2 — Capability audit (`capability-audit`)

From the portal HTML read in Check 1, grep for every `claude.use('x')` call. Compare against the `<artifact-stored-declaration>` block returned by the artifact read.

Required capabilities: `db`, `user`, `sample`, `mcp`.

| Missing capability | Config to add |
|---|---|
| `db` | `{"db":{}}` |
| `user` | `{"user":{}}` |
| `sample` | `{"sample":{}}` |
| `mcp` | `{"mcp":{"servers":[{"server":"Google Drive","tools":["search_files","read_file_content"]}]}}` |

Compute `union(currently_declared, missing_required)` and republish only when the union differs from the current declaration — never remove a declared capability.

For each capability added, record one `Fix` in `fixes_applied`:
- `description: "Added missing capability <name> to portal declaration"`
- `path: "portal artifact <slug> (capability declaration)"`

Set `status: fixed` if any capability was added; `ok` if all were already present; `blocked` if Artifact tool unavailable (skipped per Check 1).

---

## Check 3 — Portal URL consistency (`url-consistency`)

Read the canonical slug from `mentor-core/SKILL.md`. Then grep for artifact URL slugs in plugin files:

```bash
grep -rn "artifact/" plugin/ --include="*.md"
```

If `docs/` exists, grep there too.

Extract every slug found. Compare each against the canonical slug.

- **Pass** (`status: ok`): all slugs match, or no artifact URLs found.
- **Fix** (`status: fixed`): for each file containing a stale slug, Edit the file replacing only that slug. Record one `Fix` per edit:
  - `description: "Updated stale portal URL slug in <file>"`
  - `path: "<repo-relative file>:<line> <old-slug> → <new-slug>"`

---

## Check 4 — Skill cross-reference integrity (`file-references`)

For each skill under `plugin/ai-mentor/skills/`, read its `SKILL.md` and extract every pattern matching `Load references/X` or `` load `references/X` ``.

For each referenced file `X`, check existence in this order:

| Location | Action |
|---|---|
| `references/<X>` exists at repo root | `ok` for this reference |
| Only in `plugin/ai-mentor/skills/<skill>/references/<X>` | Copy to `references/<X>` at repo root; record Fix: `description: "Copied <X> to repo-root references/"`, `path: "references/<X>"` |
| Missing everywhere | Escalation: `message: "Missing reference file: references/<X> (referenced by <skill>)"`, `hint: "Check plugin/ai-mentor/skills/<skill>/references/ or recreate from the syllabus"` |

Set `status: fixed` if any copy was made, `needs_human` if any source is absent, `ok` if all references resolve.

---

## Check 5 — Portal db smoke test (`db-smoke-test`)

Load `ArtifactData` via ToolSearch (`select:ArtifactData`). Run:
1. `db_list` on collection `trainees` of the portal artifact → record count
2. `db_get` on document `settings/program` → record `startDate`, `driveFolder`

Do **not** write any portal data in this check.

| Result | Action |
|---|---|
| `db_list` succeeds, 0 trainees | Escalation: `message: "Add trainee cohort before D1 (2026-11-30)"`, `hint: "Open portal → Trainees tab → Add trainee"` |
| `db_list` succeeds, N > 0 trainees | Record count in `detail` |
| `db_list` fails (capability error) | db not declared — noted in `detail`; covered by Check 2 |
| `settings/program` missing | Escalation: `message: "Seed settings/program via portal Setup tab"`, `hint: "Open portal → Setup tab → fill Start Date and Drive folder → Save"` |
| `settings/program` present | Record `startDate` in `detail` |
| ArtifactData tool unavailable | `status: blocked`, `detail: "ArtifactData tool not available in this session"` |
| Drive scan auth error on `mcp` call | Escalation: `message: "Google Drive not connected"`, `hint: "Open claude.ai Settings → Connectors → enable Google Drive"` |

Set `status: ok` when no escalations are added, `needs_human` when at least one escalation is added, `blocked` when tool unavailable.

---

## Check 6 — Agent frontmatter completeness (`agent-frontmatter`)

Read each `.md` file under `plugin/ai-mentor/agents/`. Verify YAML frontmatter contains `name`, `description`, and `model`.

| Field situation | Action |
|---|---|
| `name` absent | Add `name: <filename-stem>`; record Fix: `description: "Added missing name field"`, `path: "<file>:<line>"` |
| `model` absent | Add `model: inherit`; record Fix: `description: "Added model: inherit"`, `path: "<file>:<line>"` |
| `description` absent | Escalation: `message: "Agent <filename> is missing a description — cannot infer intent"`, `hint: "Edit plugin/ai-mentor/agents/<filename>.md and add a description field"` |

Set `status: fixed` if any field was auto-added, `needs_human` if any description is absent, `ok` if all agents are valid.

---

## Check 7 — Full-flow wiring (`full-flow-wiring`)

Verify specialist agent names referenced in full-flow match agents on disk:

```bash
grep -E "tutor-|exam-grader|dod-auditor|healer" plugin/ai-mentor/skills/full-flow/SKILL.md
```

For each agent name found, verify `plugin/ai-mentor/agents/<name>.md` exists. For each missing file, add one Escalation:
- `message: "Agent <name> referenced in full-flow but plugin/ai-mentor/agents/<name>.md does not exist"`
- `hint: "Create plugin/ai-mentor/agents/<name>.md with name, description, and model frontmatter"`

Set `status: ok` if all referenced agents exist, `needs_human` if any are missing.

---

## Result block

End with exactly one fenced `yaml` block:

**HealResult status rules:**
- `done` — all 7 checks ran (regardless of individual check outcomes)
- `partial` — Checks 1–2 blocked (Artifact tool unavailable); Checks 3–7 ran normally
- `blocked` — portal unreachable and no checks could proceed

**Array rules:**
- `fixes_applied` — array of `{description, path}` Fix objects; `[]` when nothing changed — never omitted
- `needs_human` — array of `{message, hint}` Escalation objects; `[]` when nothing requires human action — never omitted
- `writes` — `["portal capability declaration (republish)"]` when Check 2 republished; `["none"]` otherwise; never lists trainee/score/dod/progress paths

```yaml
result:
  agent: healer
  scope: system
  status: done | partial | blocked
  checks:
    - name: portal-reachability
      status: ok | blocked | needs_human
      detail: "<one line — what was found or done>"
    - name: capability-audit
      status: ok | fixed | blocked
      detail: "<capabilities added, or 'all present', or error reason>"
    - name: url-consistency
      status: ok | fixed
      detail: "<files fixed, or 'all consistent'>"
    - name: file-references
      status: ok | fixed | needs_human
      detail: "<files copied or missing>"
    - name: db-smoke-test
      status: ok | needs_human | blocked
      detail: "<trainee count, startDate, or error>"
    - name: agent-frontmatter
      status: ok | fixed | needs_human
      detail: "<agents fixed, or 'all valid'>"
    - name: full-flow-wiring
      status: ok | needs_human
      detail: "<missing agents, or 'all wired'>"
  fixes_applied:
    - description: "<human-readable summary of change>"
      path: "<repo-relative path, e.g. plugin/ai-mentor/README.md:35>"
  needs_human:
    - message: "<actionable item>"
      hint: "<suggested resolution step>"
  writes:
    - "<portal capability declaration (republish)>"
    # or: - "none"
```
