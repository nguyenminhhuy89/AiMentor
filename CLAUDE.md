# AiMentor: 3-week cloud-native Go bootcamp for freshers

Mentoring program: 6 modules (M1 Contract & Core API, M2 Data & Encryption, M3 Async & Event-Driven, M4 Gateway/Network/Security, M5 Runtime/IaC/CI-CD, M6 Quality/Observability/Ops) over 15 working days, 30 Nov to 18 Dec 2026. Checkpoints CP0 to CP6. Pass mark 70, a failed MUST item caps a module at 69.

## Layout
- plugin/ai-mentor: agent team (mentor-lead, 6 tutors, exam-grader, dod-auditor) and skills. Run `claude --plugin-dir ./plugin/ai-mentor`.
- docs/: syllabus and rubrics (source of truth for depth and DoD).
- question-banks/: 7 banks x 120 questions (raw text, bank.json, exams.json).
- exams/: one 30-question Google-Sheet-style exam per checkpoint. answer-keys-mentors-only/ must never be shared with trainees.
- knowledge-base/: Markdown notes of the banks (INDEX.md first).
- timeline/: Master Timeline design pages (4 pages).
- portal/index.html: management portal source.
- daily-report/: daily progress template (build.py regenerates it).
- scripts/: build.py (banks to notes/json), make_xlsx.py (exam and key workbooks).

## Google Drive (owner chiaseanhneonguyen@gmail.com)
- AiMentor root folder id 1ldtz_3l8YP1mgVaVRsSH-O4mIKjEeQrQ
- Exam submissions folder "AiMentor Exams" 1lxjy4Pv2NWEEgjcQHGWb6DB1vqjEu7QJ (subfolders M0 to M6)
- Daily report folder "DailyReport" 1iQLe_c_h2J8a5JXFZ7_7TyFb5evwA5fb
- Daily report template sheet 1yBBGGxgEVShSh7FC27gnWxj8MQS6rp0Qzzh4LPpUrHQ

## Pending decisions
- Daily report template: remove Dashboard and Daily Report tabs (keep Read me, Profile, Topic Tracker, DoD Checklist). Not yet applied to the Drive copy.
- Wire the portal scan to the DailyReport folder.
