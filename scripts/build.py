"""Parse raw banks -> bank.json; build Markdown knowledge base; pick exams."""
import json, random, re, os, shutil
from collections import Counter, defaultdict

ROOT = '/home/claude/qb'
CPS = [
    ('CP0', 'M0', 'Onboarding & Go essentials', 2, 'Onboarding'),
    ('CP1', 'M1', 'Contract & Core API', 5, 'Contract-API'),
    ('CP2', 'M2', 'Data & Encryption', 8, 'Data-Encryption'),
    ('CP3', 'M3', 'Async & Event-Driven', 10, 'Async-Events'),
    ('CP4', 'M4', 'Gateway, Network & Security', 12, 'Gateway-Security'),
    ('CP5', 'M5', 'Runtime, IaC & CI/CD', 14, 'Runtime-CICD'),
    ('CP6', 'M6', 'Quality, Observability & Ops', 15, 'Quality-Ops'),
]
DATES = {2: '1 Dec 2026', 5: '4 Dec 2026', 8: '9 Dec 2026', 10: '11 Dec 2026', 12: '15 Dec 2026', 14: '17 Dec 2026', 15: '18 Dec 2026'}
LV = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}
slug = lambda s: re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s.lower())).strip('-')

bank = []
for cp, mod, name, day, short in CPS:
    lines = [l for l in open(f'{ROOT}/raw/{cp.lower()}.txt', encoding='utf-8').read().splitlines() if l.strip() and not l.startswith('#')]
    for i, l in enumerate(lines, 1):
        topic, lvl, q, c, w1, w2, w3, x = [p.strip() for p in l.split('|')]
        bank.append(dict(id=f'{cp}-Q{i:03d}', cp=cp, module=mod, cpName=name, topic=topic, level=LV[lvl],
                         question=q, _c=c, _w=[w1, w2, w3], explanation=x))

# ---------- exam selection: 30 Q, topics proportional, ~40/40/20 E/M/H ----------
exams = {}
for cp, *_ in CPS:
    rng = random.Random('exam-v1-' + cp)
    qs = [b for b in bank if b['cp'] == cp]
    by_topic = defaultdict(list)
    for b in qs: by_topic[b['topic']].append(b)
    topics = list(dict.fromkeys(b['topic'] for b in qs))
    raw = {t: 30 * len(by_topic[t]) / len(qs) for t in topics}
    alloc = {t: int(raw[t]) for t in topics}
    for t in sorted(topics, key=lambda t: raw[t] - alloc[t], reverse=True)[:30 - sum(alloc.values())]: alloc[t] += 1
    picked = []
    for t in topics:
        n = alloc[t]
        want = {'Easy': round(n * .4), 'Hard': max(1, round(n * .2))}
        want['Medium'] = n - want['Easy'] - want['Hard']
        pool = {lv: [b for b in by_topic[t] if b['level'] == lv] for lv in LV.values()}
        sel = []
        for lv in ['Easy', 'Medium', 'Hard']:
            p = pool[lv][:]; rng.shuffle(p); sel += p[:want[lv]]
        rest = [b for b in by_topic[t] if b not in sel]; rng.shuffle(rest)
        sel += rest[:n - len(sel)]
        picked += sel
    order = {'Easy': 0, 'Medium': 1, 'Hard': 2}
    picked.sort(key=lambda b: (topics.index(b['topic']), order[b['level']]))
    exams[cp] = [b['id'] for b in picked]
json.dump(exams, open(f'{ROOT}/exams.json', 'w'), indent=1)

# balanced answer letters: exam subset and the rest each cycle evenly over A-D
for cp, *_ in CPS:
    rng = random.Random('letters-' + cp)
    for group in ([b for b in bank if b['cp'] == cp and b['id'] in exams[cp]], [b for b in bank if b['cp'] == cp and b['id'] not in exams[cp]]):
        letters = list('ABCD' * (len(group) // 4 + 1))[:len(group)]; rng.shuffle(letters)
        for b, L in zip(group, letters):
            w = b.pop('_w'); rng.shuffle(w); c = b.pop('_c')
            opts = w[:]; opts.insert('ABCD'.index(L), c)
            b.update(A=opts[0], B=opts[1], C=opts[2], D=opts[3], answer=L)
    for b in bank: assert 'answer' in b or b['cp'] != cp
for b in bank:  # keep key order tidy
    ex = b.pop('explanation'); b['explanation'] = ex
json.dump(bank, open(f'{ROOT}/bank.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---------- knowledge base ----------
KB = f'{ROOT}/knowledge-base'
shutil.rmtree(KB, ignore_errors=True)
TODAY = '2026-11-24'
reg = []  # (section, id, title, path, summary)
tags_all = ['syllabus', 'exam', 'question-bank', 'rubric'] + [c[0].lower() for c in CPS]

def note(path, nid, title, tags, related, summary, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fm = f"---\nid: {nid}\ntitle: {title}\ntags: [{', '.join(tags)}]\ncreated: {TODAY}\nupdated: {TODAY}\nrelated: [{', '.join(related)}]\nsummary: {summary}\n---\n\n# {title}\n\n> Summary: {summary}\n\n"
    open(path, 'w', encoding='utf-8').write(fm + body)

# program notes
prog_ids = {'syl': f'{TODAY.replace("-", "")}-syllabus-3-weeks', 'bp': f'{TODAY.replace("-", "")}-exam-blueprint', 'conv': f'{TODAY.replace("-", "")}-exam-submission-convention'}
syl = open('/home/claude/ai-mentor/skills/mentor-core/references/syllabus.md', encoding='utf-8').read()
syl_body = syl.split('\n', 1)[1]
note(f'{KB}/topics/program/syllabus-3-weeks.md', prog_ids['syl'], 'Three-week syllabus and timeline', ['syllabus'], [prog_ids['bp']],
     'The 15-day bootcamp timeline, daily rhythm, depth levels (H/G/A) and assessment model.',
     '## Context\nSource of truth for what each checkpoint examines. Question banks are written against these days and depth levels.\n\n## Details\n' + syl_body.replace('\n## ', '\n### ') + '\n\n## Related\n- [Exam blueprint](exam-blueprint.md) — supports: how exams are drawn from these topics.\n')
bp_rows = '\n'.join(f'| {cp} | {mod} {name} | D{day} · {DATES[day]} | 120 | 30 |' for cp, mod, name, day, _ in CPS)
note(f'{KB}/topics/program/exam-blueprint.md', prog_ids['bp'], 'Exam blueprint', ['exam', 'question-bank'], [prog_ids['syl'], prog_ids['conv']],
     'How each 30-question checkpoint exam is drawn from its 120-question bank and scored.',
     f"""## Context
Each checkpoint has a bank of 120 single-answer multiple-choice questions. The checkpoint exam is the Theory part (30 of 100 points) of the module grade.

## Details
### Checkpoints
| Checkpoint | Module | Exam day | Bank size | Exam size |
|---|---|---|---|---|
{bp_rows}

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
""")
note(f'{KB}/topics/program/exam-submission-convention.md', prog_ids['conv'], 'Exam submission convention', ['exam'], [prog_ids['bp']],
     'Google Drive folders, file naming and the grading flow for checkpoint exams.',
     """## Context
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
""")
reg.append(('program', prog_ids['syl'], 'Three-week syllabus and timeline', 'topics/program/syllabus-3-weeks.md', 'The 15-day bootcamp timeline, daily rhythm, depth levels (H/G/A) and assessment model.'))
reg.append(('program', prog_ids['bp'], 'Exam blueprint', 'topics/program/exam-blueprint.md', 'How each 30-question checkpoint exam is drawn from its 120-question bank and scored.'))
reg.append(('program', prog_ids['conv'], 'Exam submission convention', 'topics/program/exam-submission-convention.md', 'Google Drive folders, file naming and the grading flow for checkpoint exams.'))
open(f'{KB}/topics/program/_topic.md', 'w').write('# Program\n\nHow the bootcamp runs and how exams are built and submitted.\n\n- [Three-week syllabus](syllabus-3-weeks.md) — timeline, rhythm and assessment model.\n- [Exam blueprint](exam-blueprint.md) — how 30-question exams are drawn and scored.\n- [Exam submission convention](exam-submission-convention.md) — Drive folders and file naming.\n')

for cp, mod, name, day, short in CPS:
    folder = f'{cp.lower()}-{slug(short)}'
    qs = [b for b in bank if b['cp'] == cp]
    topics = list(dict.fromkeys(b['topic'] for b in qs))
    tids = {t: f'{TODAY.replace("-", "")}-{cp.lower()}-{slug(t)}' for t in topics}
    tmap = [f'# {cp} · {name}\n', f'Question bank for checkpoint {cp} ({mod}), examined on Day {day} ({DATES[day]}). 120 questions in {len(topics)} topic notes; the exam draws 30.\n']
    for t in topics:
        tq = [b for b in qs if b['topic'] == t]
        lv = Counter(b['level'] for b in tq)
        summ = f'{len(tq)} {cp} questions on {t} ({lv["Easy"]} easy, {lv["Medium"]} medium, {lv["Hard"]} hard) with answers and explanations.'
        rel = [tids[o] for o in topics if o != t][:2] + [prog_ids['bp']]
        body = [f'## Context\nPart of the {cp} {name} bank. Exam questions marked ★ are in the current exam (seed exam-v1-{cp}).\n\n## Questions\n']
        for b in tq:
            star = ' ★' if b['id'] in exams[cp] else ''
            body.append(f"### {b['id']} · {b['level']}{star}\n{b['question']}\n\n- A. {b['A']}\n- B. {b['B']}\n- C. {b['C']}\n- D. {b['D']}\n\n**Answer: {b['answer']}** — {b['explanation']}\n")
        body.append('## Related\n' + '\n'.join(f'- [{o}]({slug(o)}.md) — see-also: same checkpoint.' for o in topics if tids[o] in rel) + '\n- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.\n')
        note(f'{KB}/topics/{folder}/{slug(t)}.md', tids[t], f'{cp} · {t}', ['question-bank', cp.lower()], rel, summ, '\n'.join(body))
        reg.append((f'{cp.lower()} · {name}', tids[t], f'{cp} · {t}', f'topics/{folder}/{slug(t)}.md', summ))
        tmap.append(f'- [{t}]({slug(t)}.md) — {len(tq)} questions.')
    open(f'{KB}/topics/{folder}/_topic.md', 'w', encoding='utf-8').write('\n'.join(tmap) + '\n')

sections = list(dict.fromkeys(r[0] for r in reg))
idx = ["# AiMentor Knowledge Base — Index\n",
       "## How to use this KB (for agents)\n1. Read this index first. Pick notes by their descriptions; open only those.\n2. To find questions for a checkpoint, open that checkpoint's topic notes; ★ marks questions in the current exam.\n3. Cite the note `id` and question ID (e.g. `CP3-Q017`) when you use information from it.\n",
       "## How to update this KB (for agents)\n- New idea → create a new note (atomic). Same idea changed → edit the note in place and bump `updated`.\n- Any create / rename / delete MUST update this registry and the topic's `_topic.md` in the same change.\n- Question IDs are permanent: retire a question by marking it `Retired` instead of renumbering.\n- Use only tags from the controlled vocabulary below; add a new tag here before using it.\n",
       "## Controlled tags\n" + ', '.join(f'`{t}`' for t in tags_all) + '\n', "## Registry"]
for s in sections:
    idx.append(f'### {s}')
    idx += [f'- `{i}` — **{t}** — `{p}` — {d}' for sec, i, t, p, d in reg if sec == s]
    idx.append('')
open(f'{KB}/INDEX.md', 'w', encoding='utf-8').write('\n'.join(idx))

# stats
print(len(bank), 'questions;', len(reg), 'notes')
for cp, *_ in CPS:
    q = [b for b in bank if b['cp'] == cp]; e = [b for b in bank if b['id'] in exams[cp]]
    print(cp, dict(Counter(b['answer'] for b in q)), 'exam', len(e), dict(Counter(b['level'] for b in e)), dict(Counter(b['answer'] for b in e)))
