# Contract: Healer Result Block

**Branch**: `003-healer-agent` | **Date**: 2026-11-24

The healer agent MUST end every run with exactly one fenced `yaml` block following this schema. This extends the mentor-core Result contract with healer-specific fields.

---

## Schema

```yaml
result:
  agent: healer
  scope: system
  status: done | partial | blocked

  checks:
    - name: portal-reachability
      status: ok | fixed | blocked | needs_human
      detail: "<one line — what was found or done>"
    - name: capability-audit
      status: ok | fixed | blocked | needs_human
      detail: "<capabilities added, or 'all present', or error reason>"
    - name: url-consistency
      status: ok | fixed | blocked | needs_human
      detail: "<files fixed, or 'all consistent'>"
    - name: file-references
      status: ok | fixed | blocked | needs_human
      detail: "<files copied or missing>"
    - name: db-smoke-test
      status: ok | needs_human | blocked
      detail: "<trainee count, startDate, or error>"
    - name: agent-frontmatter
      status: ok | fixed | blocked | needs_human
      detail: "<agents fixed, or 'all valid'>"
    - name: full-flow-wiring
      status: ok | needs_human | blocked
      detail: "<missing agents, or 'all wired'>"

  fixes_applied:
    - description: "<human-readable summary>"
      path: "<repo-relative path, e.g. plugin/ai-mentor/README.md:35>"

  needs_human:
    - message: "<actionable item>"
      hint: "<optional suggested resolution>"

  writes:
    - "<portal path written, e.g. 'portal capability declaration (republish)'>
    # or the string "none"
```

---

## Rules

| Rule | Detail |
|---|---|
| `checks` length | Exactly 7 when `status: done`; fewer when `status: partial` (degraded mode); 0 when `status: blocked` |
| `fixes_applied` | Empty array `[]` when nothing changed — never omitted |
| `needs_human` | Empty array `[]` when nothing requires human action — never omitted |
| `writes` | `["none"]` when no portal write occurred; `["portal capability declaration (republish)"]` when republished |
| `status: blocked` | Only when `portal-reachability` check fails AND the healer cannot proceed with any other check |
| `status: partial` | When one or more checks were skipped due to degraded mode (Artifact tool unavailable) |
| `status: done` | All 7 checks ran, regardless of individual check outcomes |

---

## Pre-flight skip signal

When mentor-lead reads this block to decide whether to skip the next pre-flight run, it checks:

```
all_checks_ok = (status == "done") AND (all checks[*].status == "ok")
```

If `all_checks_ok` is true, the healer is not re-dispatched in the same session.

---

## Example: clean run

```yaml
result:
  agent: healer
  scope: system
  status: done
  checks:
    - name: portal-reachability
      status: ok
      detail: "artifact ACBVYCSsYnWtD5ngzXz3dW readable, Version 3"
    - name: capability-audit
      status: ok
      detail: "db, user, sample, mcp(Google Drive) all declared"
    - name: url-consistency
      status: ok
      detail: "all consistent"
    - name: file-references
      status: ok
      detail: "syllabus.md and rubrics.md present at repo root"
    - name: db-smoke-test
      status: needs_human
      detail: "0 trainees enrolled; settings/program missing"
    - name: agent-frontmatter
      status: ok
      detail: "all 10 agents valid"
    - name: full-flow-wiring
      status: ok
      detail: "all wired"
  fixes_applied: []
  needs_human:
    - message: "Add trainee cohort before D1 (2026-11-30)"
      hint: "Open portal → Trainees tab → Add trainee"
    - message: "Seed settings/program via portal Setup tab"
      hint: "Open portal → Setup tab → Save"
  writes:
    - none
```
