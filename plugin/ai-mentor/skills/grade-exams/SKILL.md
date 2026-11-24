---
name: grade-exams
description: Scan Google Drive for submitted bootcamp exams and grade them against the module rubric, then save scores and feedback to the AiMentor portal. Use for "grade the exams", "chấm bài", "check M3 submissions", "any new exams on Drive?", "/grade-exams M2".
---

# Grade exams from Google Drive

Argument (optional): a module `M1`–`M6`, a trainee ID, or `new` (default: all ungraded).

1. Load the `mentor-core` skill and read `../mentor-core/references/rubrics.md`.
2. Find submissions with the Google Drive connector `search_files`:
   - Folder first: `title contains 'AiMentor' and mimeType = 'application/vnd.google-apps.folder'`, then `title contains 'Exams'` under it, then module subfolders (`M1-Contract-API` … `M6-Quality-Ops`).
   - Files: `'<moduleFolderId>' in ancestors and trashed = false`.
   - Parse `<TraineeID>_<FullName>_M<n>` from the title. If the name doesn't match, list it as "unmatched" — never guess the trainee.
3. Skip files already graded: `db_list` collection `scores` on the portal; a score with the same `fileId` and `gradedAt` later than the file's `modifiedTime` is done.
4. For each file, `read_file_content` (fileId). If it links a GitHub repo/PR, note it — practical items you cannot verify from the document are marked "needs code check" and routed to the `dod-auditor` agent rather than guessed.
5. Grade strictly by the rubric: Theory /30, Practical /50, Quality /20. Apply MUST gates (any ❌ caps total at 69). Write feedback in the rubric's required format, in the trainee's language.
6. Save each result with `db_write` op `merge` to `scores/<traineeId>_M<n>` (read first; pass `ifVersion` if it exists). Set `gradedBy: "exam-grader agent"`, `gradedAt` ISO time.
7. Report a table: trainee · module · total · pass/fail · MUST failures · "needs human review" flag. Flag for human review when: score 65–74, plagiarism suspicion (near-identical answers across trainees), or unreadable file.
8. End with a `result:` block (Result contract in `mentor-core`): one entry per graded trainee with `checkpoint` and `score`, `needs_human` for the review flags, and `writes` listing the `scores/...` paths. Do not touch the dashboard; mentor-lead runs `dashboard-publish`.

Never change a score a human set (`gradedBy` not containing "agent") — propose the change instead.
