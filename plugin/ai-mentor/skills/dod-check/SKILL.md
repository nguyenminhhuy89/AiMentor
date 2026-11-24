---
name: dod-check
description: Audit a trainee's capstone repository or PR against the Definition of Done and update DoD status in the portal. Use for "check DoD", "scan Huy's repo", "is the PR done", "kiểm tra DoD", "/dod-check <trainee> <repo-or-path>".
---

# Definition of Done check

1. Load `mentor-core` and `references/rubrics.md` (MUST items are the DoD).
2. Get the code: a local path, an attached zip, or a GitHub repo the session can clone. If none is reachable, ask for it — don't grade from memory.
3. Run what can be run, and record evidence:
   - `golangci-lint run ./...`, `go build ./...`, `go test ./... -cover` (report per-package coverage of business logic)
   - `go generate ./... && git diff --exit-code` → generated code untouched
   - secret scan (`gitleaks detect` or grep for AKIA/aws_secret/password=)
   - Dockerfile: multi-stage, `USER` non-root; `trivy image` or `trivy fs` if available
   - CloudFormation: `cfn-lint`; list resources not defined in templates
   - IAM JSON: flag `"Action": "*"` or `"Resource": "*"` on data stores
   - SQS: every queue has `RedrivePolicy`; consumer has an idempotency check
   - logs/middleware: trace/correlation ID set and forwarded on publish
4. For each DoD item output ✅ / ❌ / ⚠️ (can't verify) with file:line evidence.
5. Write results to the portal `dod/<traineeId>_<itemKey>` (keys: m1-contract, m1-codegen, m2-kms, m3-dlq, m3-idem, m4-secrets, m4-iam, m4-kong, m4-network, m5-image, m5-cfn, m5-pipeline, m6-ci, m6-trace, m6-ops) only after the human approves. When run by mentor-lead, the approval covers the whole batch that mentor-lead listed.
6. End with the 3 most important fixes, ordered by DoD impact.
7. End with a `result:` block (Result contract in `mentor-core`): `dod_done` per trainee (count of ✅ items out of 15), `needs_human` for ⚠️ items, and `writes` with the `dod/...` paths actually written.
