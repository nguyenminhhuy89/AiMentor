---
id: 20261124-exam-blueprint
title: Exam blueprint
tags: [exam, question-bank]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-syllabus-3-weeks, 20261124-exam-submission-convention]
summary: How each 30-question checkpoint exam is drawn from its 120-question bank and scored.
---

# Exam blueprint

> Summary: How each 30-question checkpoint exam is drawn from its 120-question bank and scored.

## Context
Each checkpoint has a bank of 120 single-answer multiple-choice questions. The checkpoint exam is the Theory part (30 of 100 points) of the module grade.

## Details
### Checkpoints
| Checkpoint | Module | Exam day | Bank size | Exam size |
|---|---|---|---|---|
| CP0 | M0 Onboarding & Go essentials | D2 · 1 Dec 2026 | 120 | 30 |
| CP1 | M1 Contract & Core API | D5 · 4 Dec 2026 | 120 | 30 |
| CP2 | M2 Data & Encryption | D8 · 9 Dec 2026 | 120 | 30 |
| CP3 | M3 Async & Event-Driven | D10 · 11 Dec 2026 | 120 | 30 |
| CP4 | M4 Gateway, Network & Security | D12 · 15 Dec 2026 | 120 | 30 |
| CP5 | M5 Runtime, IaC & CI/CD | D14 · 17 Dec 2026 | 120 | 30 |
| CP6 | M6 Quality, Observability & Ops | D15 · 18 Dec 2026 | 120 | 30 |

### Drawing rules
- Questions per topic area are proportional to that topic's share of the bank (e.g. 25 of 120 → 6 of 30).
- Within a topic, the target mix is about 40% Easy, 40% Medium, 20% Hard (at least one Hard per topic).
- Selection is seeded (`exam-v1-<CP>`), so the same exam can be regenerated; change the seed for a retake version.
- Options are shuffled once per bank with a fixed seed, so correct answers are spread across A–D.

### Scoring
- 1 point per correct answer, 30 points = the Theory part of the module (see the rubric for Practical 50 and Code quality 20).
- Pass mark for the whole module is 70/100; a failed MUST item caps it at 69.
- A retake uses a different seed, so it shares at most a few questions with the first sitting.

## Related
- [Three-week syllabus](syllabus-3-weeks.md) — prerequisite: topics and depth levels.
- [Exam submission convention](exam-submission-convention.md) — see-also: where answered exams go.
