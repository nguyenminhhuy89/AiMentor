---
id: 20261124-exam-submission-convention
title: Exam submission convention
tags: [exam]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-exam-blueprint]
summary: Google Drive folders, file naming and the grading flow for checkpoint exams.
---

# Exam submission convention

> Summary: Google Drive folders, file naming and the grading flow for checkpoint exams.

## Context
The exam-grader agent and the AiMentor portal find submissions by folder and file name, so the convention must be followed exactly.

## Details
### Google Drive layout
- `AiMentor/1. Question Banks` — the full bank workbook (mentors).
- `AiMentor/2. Exam Templates` — one exam form per checkpoint (a Google Sheet).
- `AiMentor/3. Answer Keys (mentors only)` — one key + scoring sheet per checkpoint. Never share with trainees.
- `AiMentor/AiMentor Exams/M0-Onboarding … M6-Quality-Ops` — trainee submissions.

### Trainee steps
1. Make a copy of the checkpoint's exam template (File › Make a copy).
2. Name it `<TraineeID>_<FullName>_M<n>`, e.g. `FA001_NguyenMinhAn_M1`, and save it in the module's folder under `AiMentor Exams`.
3. Fill Trainee ID, name, squad and date; choose one answer (A–D) per question from the dropdown.

### Grading
- The exam-grader agent (or a mentor) pastes the 30 answers into the key's "Score a submission" tab, or reads the copy directly from Drive.
- The Theory score (out of 30) is saved to the portal with Practical and Code-quality scores.

## Related
- [Exam blueprint](exam-blueprint.md) — prerequisite: what is in each exam.
