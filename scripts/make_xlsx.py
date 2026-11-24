import json, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

ROOT = '/home/claude/qb'; OUT = f'{ROOT}/xlsx'; os.makedirs(OUT, exist_ok=True)
bank = json.load(open(f'{ROOT}/bank.json', encoding='utf-8'))
exams = json.load(open(f'{ROOT}/exams.json'))
CPS = [('CP0', 'M0', 'Onboarding & Go essentials', 2, '1 Dec 2026', 'M0-Onboarding'),
       ('CP1', 'M1', 'Contract & Core API', 5, '4 Dec 2026', 'M1-Contract-API'),
       ('CP2', 'M2', 'Data & Encryption', 8, '9 Dec 2026', 'M2-Data-Encryption'),
       ('CP3', 'M3', 'Async & Event-Driven', 10, '11 Dec 2026', 'M3-Async-Events'),
       ('CP4', 'M4', 'Gateway, Network & Security', 12, '15 Dec 2026', 'M4-Gateway-Security'),
       ('CP5', 'M5', 'Runtime, IaC & CI/CD', 14, '17 Dec 2026', 'M5-Runtime-CICD'),
       ('CP6', 'M6', 'Quality, Observability & Ops', 15, '18 Dec 2026', 'M6-Quality-Ops')]
F = 'Arial'
base = Font(name=F, size=10); bold = Font(name=F, size=10, bold=True)
title = Font(name=F, size=16, bold=True); sub = Font(name=F, size=10, color='4B5563')
hdr_font = Font(name=F, size=10, bold=True, color='FFFFFF')
HDR = PatternFill('solid', fgColor='14171C'); INPUT = PatternFill('solid', fgColor='FFF2B3')
EX = PatternFill('solid', fgColor='EEF0F3'); BAND = PatternFill('solid', fgColor='F7F8FA')
thin = Side(style='thin', color='C9CDD3'); box = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(wrap_text=True, vertical='top'); center = Alignment(horizontal='center', vertical='top', wrap_text=True)

def widths(ws, w):
    for i, x in enumerate(w, 1): ws.column_dimensions[get_column_letter(i)].width = x

def header(ws, row, labels):
    for i, l in enumerate(labels, 1):
        c = ws.cell(row, i, l); c.font = hdr_font; c.fill = HDR; c.alignment = center; c.border = box

# ---------------- question bank workbook ----------------
wb = Workbook(); rd = wb.active; rd.title = 'Read me'
rd['A1'] = 'AiMentor question banks'; rd['A1'].font = title
lines = ['840 single-answer questions: 120 per checkpoint (CP0–CP6), written against the 3-week syllabus.',
         'Columns: ID (permanent), Module, Topic, Level (Easy/Medium/Hard), Question, options A–D, Correct, Explanation, In exam (Yes = in the current 30-question exam, seed exam-v1).',
         'Mentors only: this workbook contains the answers. Do not share with trainees.',
         'To retire a question, set its Level to "Retired" rather than deleting the row, so IDs stay stable.',
         'Source: written for the AiMentor bootcamp on 24 Nov 2026; mirrored in the Markdown knowledge base (INDEX.md).']
for i, l in enumerate(lines, 3): rd.cell(i, 1, l).font = base
rd.column_dimensions['A'].width = 140
sm = wb.create_sheet('Summary')
sm['A1'] = 'Bank summary'; sm['A1'].font = title
header(sm, 3, ['Checkpoint', 'Module', 'Easy', 'Medium', 'Hard', 'Total', 'In exam'])
for r, (cp, mod, name, *_ ) in enumerate(CPS, 4):
    sm.cell(r, 1, f'{cp} · {name}').font = base; sm.cell(r, 2, mod).font = base
    for j, lv in enumerate(['Easy', 'Medium', 'Hard'], 3):
        sm.cell(r, j, f'=COUNTIF({cp}!$D:$D,"{lv}")').font = base
    sm.cell(r, 6, f'=SUM(C{r}:E{r})').font = bold
    sm.cell(r, 7, f'=COUNTIF({cp}!$L:$L,"Yes")').font = base
tr = 4 + len(CPS)
sm.cell(tr, 1, 'All checkpoints').font = bold
for j in range(3, 8):
    L = get_column_letter(j); sm.cell(tr, j, f'=SUM({L}4:{L}{tr-1})').font = bold
widths(sm, [40, 10, 10, 10, 10, 10, 10])
for cp, mod, name, *_ in CPS:
    ws = wb.create_sheet(cp)
    header(ws, 1, ['ID', 'Module', 'Topic', 'Level', 'Question', 'A', 'B', 'C', 'D', 'Correct', 'Explanation', 'In exam'])
    for r, b in enumerate([b for b in bank if b['cp'] == cp], 2):
        vals = [b['id'], mod, b['topic'], b['level'], b['question'], b['A'], b['B'], b['C'], b['D'], b['answer'], b['explanation'], 'Yes' if b['id'] in exams[cp] else '']
        for j, v in enumerate(vals, 1):
            c = ws.cell(r, j, v); c.font = base; c.alignment = center if j in (2, 4, 10, 12) else wrap
    ws.freeze_panes = 'A2'; ws.auto_filter.ref = f'A1:L{r}'
    widths(ws, [11, 8, 24, 9, 48, 30, 30, 30, 30, 9, 40, 9])
wb.save(f'{OUT}/AiMentor Question Banks.xlsx')

# ---------------- exam forms + answer keys ----------------
for cp, mod, name, day, date, folder in CPS:
    qs = [next(b for b in bank if b['id'] == i) for i in exams[cp]]
    n = len(qs)
    # exam form
    wb = Workbook(); ws = wb.active; ws.title = 'Exam'
    ws['A1'] = f'AiMentor · {cp} {name} — checkpoint exam'; ws['A1'].font = title
    ws['A2'] = f'Module {mod[1:]} · Day {day} · {date} · {n} questions · 1 point each ({n} points = Theory part) · 45 minutes'; ws['A2'].font = sub
    info = [('Trainee ID', 'e.g. FA001'), ('Full name', 'e.g. Nguyen Minh An'), ('Squad', 'e.g. Squad A'), ('Date', date)]
    for i, (lab, hint) in enumerate(info, 4):
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=2)
        ws.cell(i, 1, lab).font = bold
        ws.merge_cells(start_row=i, start_column=3, end_row=i, end_column=4)
        for k in (3, 4): ws.cell(i, k).fill = INPUT; ws.cell(i, k).border = box
        ws.cell(i, 3).font = base
        ws.cell(i, 5, hint).font = sub
    ws['A9'] = 'How to answer'; ws['A9'].font = bold
    ws['A10'] = (f'1) File › Make a copy, rename it TraineeID_FullName_{mod} (e.g. FA001_NguyenMinhAn_{mod}) and move it to AiMentor/AiMentor Exams/{folder}.  '
                 '2) Fill the yellow cells above.  3) In the yellow "Your answer" column pick one letter A–D per question.  4) Do not edit any other cell. Yellow = cells you fill in.')
    ws.merge_cells('A10:I10'); ws['A10'].font = base; ws['A10'].alignment = wrap; ws.row_dimensions[10].height = 42
    header(ws, 12, ['No.', 'Topic', 'Level', 'Question', 'A', 'B', 'C', 'D', 'Your answer'])
    ex = ['Ex.', 'Example (not scored)', 'Easy', 'Which HTTP status code means a resource was created?', '404', '201', '500', '302', 'B']
    for j, v in enumerate(ex, 1):
        c = ws.cell(13, j, v); c.font = Font(name=F, size=10, italic=True, color='4B5563'); c.fill = EX; c.border = box; c.alignment = center if j in (1, 3, 9) else wrap
    dv = DataValidation(type='list', formula1='"A,B,C,D"', allow_blank=True, showErrorMessage=True, errorTitle='Pick A, B, C or D', error='Choose one letter from the list.')
    ws.add_data_validation(dv)
    first = 14
    for k, b in enumerate(qs):
        r = first + k
        vals = [k + 1, b['topic'], b['level'], b['question'], b['A'], b['B'], b['C'], b['D'], None]
        for j, v in enumerate(vals, 1):
            c = ws.cell(r, j, v); c.font = base; c.border = box; c.alignment = center if j in (1, 3, 9) else wrap
            if j < 9 and k % 2: c.fill = BAND
        ws.cell(r, 9).fill = INPUT; ws.cell(r, 9).font = Font(name=F, size=12, bold=True)
        dv.add(f'I{r}')
    last = first + n - 1
    ws.cell(last + 2, 8, 'Answered').font = bold
    c = ws.cell(last + 2, 9, f'=COUNTA(I{first}:I{last})'); c.font = bold; c.alignment = center
    ws.cell(last + 2, 10, f'of {n}').font = sub
    widths(ws, [6, 20, 9, 46, 26, 26, 26, 26, 11, 6])
    ws.print_title_rows = '12:12'; ws.page_setup.orientation = 'landscape'; ws.page_setup.fitToWidth = 1; ws.sheet_properties.pageSetUpPr.fitToPage = True; ws.page_setup.fitToHeight = 0
    wb.save(f'{OUT}/{cp} Exam - {name.replace("/", "-")}.xlsx')

    # answer key + scoring
    wb = Workbook(); ak = wb.active; ak.title = 'Answer key'
    ak['A1'] = f'{cp} {name} — answer key (mentors only)'; ak['A1'].font = title
    ak['A2'] = f'Matches the exam template "{cp} Exam" row by row (No. 1–{n}). Source: AiMentor question bank, seed exam-v1-{cp}.'; ak['A2'].font = sub
    header(ak, 4, ['No.', 'Question ID', 'Topic', 'Level', 'Question', 'Correct', 'Correct option text', 'Explanation'])
    for k, b in enumerate(qs):
        r = 5 + k
        vals = [k + 1, b['id'], b['topic'], b['level'], b['question'], b['answer'], b[b['answer']], b['explanation']]
        for j, v in enumerate(vals, 1):
            c = ak.cell(r, j, v); c.font = bold if j == 6 else base; c.border = box; c.alignment = center if j in (1, 2, 4, 6) else wrap
    ak.freeze_panes = 'A5'
    widths(ak, [6, 12, 22, 9, 50, 9, 34, 44])
    sc = wb.create_sheet('Score a submission')
    sc['A1'] = f'{cp} — score a submission'; sc['A1'].font = title
    sc['A2'] = 'Yellow = inputs. Paste or pick the trainee\'s answers in column C (rows match the exam). Points and totals are formulas.'; sc['A2'].font = sub
    for i, lab in enumerate(['Trainee ID', 'Full name', 'Submission file'], 4):
        sc.cell(i, 1, lab).font = bold
        c = sc.cell(i, 2); c.fill = INPUT; c.border = box; c.font = base
    header(sc, 8, ['No.', 'Correct', 'Trainee answer', 'Point', 'Topic', 'Level'])
    dv2 = DataValidation(type='list', formula1='"A,B,C,D"', allow_blank=True); sc.add_data_validation(dv2)
    for k in range(n):
        r = 9 + k; kr = 5 + k
        sc.cell(r, 1, k + 1)
        sc.cell(r, 2, f"='Answer key'!F{kr}")
        c = sc.cell(r, 3); c.fill = INPUT; dv2.add(f'C{r}')
        sc.cell(r, 4, f'=IF(UPPER(TRIM(C{r}))=B{r},1,0)')
        sc.cell(r, 5, f"='Answer key'!C{kr}")
        sc.cell(r, 6, f"='Answer key'!D{kr}")
        for j in range(1, 7):
            cc = sc.cell(r, j); cc.font = base; cc.border = box; cc.alignment = center if j != 5 else wrap
    lr = 9 + n - 1
    sc['H8'] = 'Result'; sc['H8'].font = hdr_font; sc['H8'].fill = HDR; sc['I8'].fill = HDR
    res = [('Correct answers', f'=SUM(D9:D{lr})', '0'), ('Questions', f'=COUNTA(A9:A{lr})', '0'),
           ('Theory score (/30)', f'=ROUND(I9/I10*30,1)', '0.0'), ('Percent correct', f'=IF(I10=0,0,I9/I10)', '0.0%'),
           ('Answered', f'=COUNTA(C9:C{lr})', '0')]
    for i, (lab, f, nf) in enumerate(res, 9):
        sc.cell(i, 8, lab).font = bold; c = sc.cell(i, 9, f); c.font = bold; c.number_format = nf; c.border = box
    sc.cell(15, 8, 'By topic').font = hdr_font; sc.cell(15, 8).fill = HDR
    for j, l in enumerate(['Correct', 'Asked', '%'], 9):
        c = sc.cell(15, j, l); c.font = hdr_font; c.fill = HDR
    topics = list(dict.fromkeys(b['topic'] for b in qs))
    for i, t in enumerate(topics, 16):
        sc.cell(i, 8, t).font = base
        sc.cell(i, 9, f'=SUMIFS($D$9:$D${lr},$E$9:$E${lr},H{i})').font = base
        sc.cell(i, 10, f'=COUNTIF($E$9:$E${lr},H{i})').font = base
        c = sc.cell(i, 11, f'=IF(J{i}=0,0,I{i}/J{i})'); c.font = base; c.number_format = '0%'
    widths(sc, [6, 9, 14, 7, 26, 9, 3, 26, 10, 8, 8])
    wb.save(f'{OUT}/{cp} Answer Key - {name.replace("/", "-")}.xlsx')
print(sorted(os.listdir(OUT)))
