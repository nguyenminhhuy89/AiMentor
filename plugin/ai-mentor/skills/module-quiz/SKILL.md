---
name: module-quiz
description: Generate a daily check quiz or a full module theory exam (with answer key) for the Go/AWS bootcamp. Use for "make a quiz for day 4", "tạo đề M3", "theory exam for module 2", "/module-quiz M5 exam".
---

# Module quiz / exam

Arguments: `D<n>` (daily quiz, 10 questions) or `M<n> exam` (theory exam, 20 questions, 30 points).

1. Load `mentor-core`; take topics from the syllabus day/module and the rubric's "Theory" line.
2. Mix: 60% MCQ (4 options, one correct, plausible distractors), 25% short answer, 15% "read this Go/YAML snippet and find the bug".
3. Only H and G topics are examinable in depth; A topics get at most one conceptual question.
4. Use the capstone Order Service in scenarios.
5. Output two parts: **Trainee copy** (questions only) and **Answer key** (answer + one-line why + points). For exams, also offer to save the trainee copy as a Google Doc in `AiMentor/Exams/<module folder>/_template` via the Google Drive connector — ask before creating files.
