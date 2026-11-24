# ai-mentor — AI training team for the AiMentor bootcamp

3-week (15 working days) cloud-native Go bootcamp for freshers: Go (Gin) + OpenAPI/oapi-codegen v2, AWS data/encryption, async events, gateway/network/security, runtime/IaC-CI/CD, quality/observability/ops.

## How the team works
mentor-lead is the orchestrator. It reads the request or the bootcamp day, splits the work into packages, dispatches them to specialist agents in parallel, collects each agent's result block, summarizes, and publishes member results to the master timeline dashboard.

```
mentor-lead ──► tutor-*            lab help, at-risk flags
            ──► exam-grader        Drive exams → portal scores
            ──► dod-auditor        repo checks → portal DoD (after human approval)
            ──► summary ──► dashboard-publish ──► timeline/master-timeline.html
```

Every agent ends with the same `result:` YAML block, defined in the `mentor-core` skill (Result contract).

## Agents
| Agent | Role | Returns |
|---|---|---|
| mentor-lead | Orchestrator: daily plan, dispatch, summary, dashboard, weekly report, escalation | Plans, summaries, dashboard updates |
| tutor-contract-api | M1 Contract & Core API (D1–D5) | Flags for trainees stuck on MUST items |
| tutor-data-encryption | M2 Data & Encryption (D6–D8) | Flags |
| tutor-async-events | M3 Async & Event-Driven (D9–D10) | Flags |
| tutor-gateway-security | M4 Gateway, Network & Security (D11–D12) | Flags |
| tutor-runtime-cicd | M5 Runtime, IaC & CI/CD (D13–D14) | Flags |
| tutor-quality-ops | M6 Quality, Observability & Ops (every day + D15) | Flags |
| exam-grader | Scans Google Drive exams, grades by rubric, saves scores to the portal | Scores, human-review items |
| dod-auditor | Runs DoD checks on code with evidence | DoD items done per trainee |

## Skills
`/full-flow [D<n>|M<n>]` (whole team run via mentor-lead) · `/daily-plan` · `/grade-exams [M1–M6|new]` · `/module-quiz D<n> | M<n> exam` · `/dod-check <trainee> <repo>` · `/progress-report [week n]` · `/dashboard-publish` · `mentor-core` (syllabus, rubrics, result contract; loaded automatically)

## Connections
- **Google Drive** (claude.ai connector, already connected): exams live in `AiMentor/Exams/M<n>-<name>/`, files named `<TraineeID>_<FullName>_M<n>`.
- **AiMentor portal** (Claude artifact): https://claude.ai/artifact/ACBVYCSsYnWtD5ngzXz3dW. Scores, DoD, flags and trainees are read and written with the artifact database tools.
- **Master timeline dashboard**: `timeline/master-timeline.html` (repo). Updated only by `dashboard-publish`.
- Optional: Jira / Confluence / Atlassian Rovo connectors for posting plans, runbooks and reports; GitHub for repo checks.

## Changelog
- 0.2.0: Fixed agent frontmatter (all agents failed YAML parsing). mentor-lead is now the orchestrator with a dispatch → collect → summarize → publish workflow. Added the shared result contract, the `dashboard-publish` skill and the `flags` portal collection. Daily plan, progress report, grading and DoD skills now return results to mentor-lead.
