import re, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule

src = open("/tmp/claude-tool-results/eaa8b5b4-f20c-5391-a68a-5e8f9405bf84/mcp-claude-artifacts-blob-1795484330810-tjecn9-8389f4e3.html", encoding="utf-8").read()
# topic data from the published syllabus (rebuilt in /home/claude/mt4/gen.py, DAYS block)
gen = open("/home/claude/mt4/gen.py", encoding="utf-8").read()
days_js = re.search(r"const DAYS = \[(.*?)\n\];", gen, re.S).group(1)
DAYS = []
for m in re.finditer(r"\['(M\d)','([^']*)',\[(.*?)\],'([^']*)','([^']*)'\]", days_js):
    topics = re.findall(r"\['([^']*)','([HGA])'\]", m.group(3))
    DAYS.append((m.group(1), m.group(2), topics, m.group(4), m.group(5)))
assert len(DAYS) == 15, len(DAYS)
dates = [datetime.date(2026,11,30)+datetime.timedelta(days=d) for d in [0,1,2,3,4,7,8,9,10,11,14,15,16,17,18]]
MODS = {"M0":"Onboarding & Go","M1":"Contract & Core API","M2":"Data & Encryption","M3":"Async & Event-Driven","M4":"Gateway, Network & Security","M5":"Runtime, IaC & CI/CD","M6":"Quality, Observability & Ops"}
COL = {"M0":"4B5563","M1":"1D4ED8","M2":"0F766E","M3":"C2410C","M4":"6D28D9","M5":"B42318","M6":"15803D"}

F = "Arial"
def font(**k): return Font(name=F, size=k.pop("size",10), **k)
HDR = PatternFill("solid", fgColor="14171C"); YEL = PatternFill("solid", fgColor="FFF2CC"); GREY = PatternFill("solid", fgColor="F3F4F6")
thin = Side(style="thin", color="D1D5DB"); BOX = Border(left=thin,right=thin,top=thin,bottom=thin)
wrap = Alignment(wrap_text=True, vertical="top")

def header(ws, row, labels, widths):
    for i,(l,w) in enumerate(zip(labels,widths),1):
        c = ws.cell(row=row, column=i, value=l); c.font = font(bold=True, color="FFFFFF"); c.fill = HDR; c.alignment = Alignment(wrap_text=True, vertical="center"); c.border = BOX
        ws.column_dimensions[c.column_letter].width = w
    ws.row_dimensions[row].height = 30
def title(ws, text, sub):
    ws["A1"] = text; ws["A1"].font = font(bold=True, size=16)
    ws["A2"] = sub; ws["A2"].font = font(color="4B5563")

wb = Workbook()
# ---------- Read me ----------
rm = wb.active; rm.title = "Read me"
title(rm, "AiMentor · Daily Progress Report", "One copy per trainee. Update it every training day (D1 30 Nov to D15 18 Dec 2026).")
lines = [
 ("How to use", None),
 ("1","Make a copy of this sheet. Rename it  <TraineeID>_<FullName>_Progress  (example: FA001_NguyenMinhAn_Progress)."),
 ("2","Fill the Profile tab once. Yellow cells are yours to edit; white cells are formulas, do not overwrite them."),
 ("3","Each day: set every topic's Status on the Topic Tracker (Not started / In progress / Done) and paste a link as Evidence for each Done topic."),
 ("4","At each checkpoint (D2, D5, D8, D10, D12, D14, D15): answer the DoD Checklist for that module and paste proof."),
 ("5","Keep the sheet in the DailyReport Drive folder. Do not rename, move or delete tabs, rows or columns. The grading agent reads fixed positions."),
 ("",""),
 ("Status legend", None),
 ("Not started","You have not begun this topic."),
 ("In progress","You started it but cannot show the result yet."),
 ("Done","You can show the result and explain it (Copilot-generated code included). Evidence link is required."),
 ("",""),
 ("Evidence rules", None),
 ("Link","Paste a link to your PR, commit, Jira ticket, Confluence page, CI run or screenshot. No link means the agent counts the topic as In progress."),
 ("Honest status","A late Done is fine. A Done with no proof is flagged for your mentor."),
]
r = 4
for a,b in lines:
    if b is None and a:
        rm.cell(row=r, column=1, value=a).font = font(bold=True, size=12)
    else:
        rm.cell(row=r, column=1, value=a).font = font(bold=True)
        c = rm.cell(row=r, column=2, value=b); c.font = font(); c.alignment = wrap
    r += 1
rm.column_dimensions["A"].width = 16; rm.column_dimensions["B"].width = 110

# ---------- Profile ----------
pf = wb.create_sheet("Profile")
title(pf, "Profile", "Fill once. The agent reads B4:B9 by position.")
fields = [("Trainee ID","FA001"),("Full name",""),("Squad",""),("Mentor",""),("Repo / capstone link",""),("Start date",datetime.date(2026,11,30))]
for i,(l,v) in enumerate(fields):
    row = 4+i
    pf.cell(row=row, column=1, value=l).font = font(bold=True)
    c = pf.cell(row=row, column=2, value=v if l!="Trainee ID" else None); c.fill = YEL; c.font = font(color="0000FF"); c.border = BOX
pf["B9"].number_format = "d mmm yyyy"
pf["C4"] = "Example: FA001 (set to your ID)"; pf["C4"].font = font(color="6B7280", italic=True)
pf.column_dimensions["A"].width = 24; pf.column_dimensions["B"].width = 48; pf.column_dimensions["C"].width = 34

# ---------- Topic Tracker ----------
tt = wb.create_sheet("Topic Tracker")
title(tt, "Topic Tracker", "One row per syllabus topic. H = hands-on, A = awareness. Set Status and paste an evidence link.")
header(tt, 4, ["Day","Date","Module","Topic","Depth","Status","Done date","Evidence link","Jira key","Note"], [7,12,9,58,8,14,12,40,14,34])
row = 5
for i,(mod,ttl,topics,lab,chk) in enumerate(DAYS):
    for (x,l) in topics:
        vals = [i+1, dates[i], mod, x, l, "Not started", None, None, None, None]
        for j,v in enumerate(vals,1):
            c = tt.cell(row=row, column=j, value=v); c.font = font(); c.border = BOX; c.alignment = wrap
        tt.cell(row=row, column=2).number_format = "d mmm"
        for j in (6,7,8,9,10): tt.cell(row=row, column=j).fill = YEL
        tt.cell(row=row, column=7).number_format = "d mmm"
        row += 1
TT_LAST = row-1
dv = DataValidation(type="list", formula1='"Not started,In progress,Done"', allow_blank=False); tt.add_data_validation(dv); dv.add(f"F5:F{TT_LAST}")
tt.conditional_formatting.add(f"F5:F{TT_LAST}", CellIsRule(operator="equal", formula=['"Done"'], fill=PatternFill("solid", bgColor="C6EFCE", fgColor="C6EFCE")))
tt.conditional_formatting.add(f"F5:F{TT_LAST}", CellIsRule(operator="equal", formula=['"In progress"'], fill=PatternFill("solid", bgColor="FFEB9C", fgColor="FFEB9C")))
tt.freeze_panes = "E5"

# ---------- DoD Checklist ----------
dd = wb.create_sheet("DoD Checklist")
title(dd, "DoD Checklist", "Definition of Done per module, from the grading rubric. MUST items cap the module at 69 if failed.")
header(dd, 4, ["Module","Checkpoint","Item","Type","Points","Met?","Proof link","Note"], [9,12,76,9,8,11,40,30])
R = [
 ("M1","CP1",[("100% of endpoints defined in OpenAPI 3.0 with JSON Schema for request, response and error","MUST",10),("oapi-codegen v2 output committed via go generate, zero manual edits (CI diff check)","MUST",10),("Gin middleware: request/trace ID, structured logging, recovery, consistent RFC 7807 error body","Scored",15),("Handlers delegate to a service layer; validation errors return 400 with schema detail","Scored",10),("Can explain Copilot-generated code line by line (oral)","Scored",5)]),
 ("M2","CP2",[("PII fields (email, phone) encrypted with AWS KMS before persist; no plaintext PII in DB or logs","MUST",15),("SDK uses the default credential chain, no keys in code","MUST",5),("DynamoDB table design with conditional writes; RDS access via repository interface","Scored",15),("S3 upload plus presigned URL with expiry","Scored",10),("Tests with mocks or LocalStack for each store","Scored",5)]),
 ("M3","CP3",[("Every SQS queue has a DLQ with redrive policy","MUST",10),("Consumers idempotent: duplicate-message test proves a single side effect","MUST",15),("CloudWatch alarm on DLQ ApproximateNumberOfMessagesVisible > 0","MUST",10),("SNS to SQS fan-out and EventBridge rule wired, event schema documented","Scored",10),("EventBridge Scheduler job (cancel unpaid orders)","Scored",5)]),
 ("M4","CP4",[("Zero hardcoded secrets (secret scan clean); Secrets Manager for credentials, Parameter Store for config, AppConfig for feature flags","MUST",10),("Least-privilege IAM policy per service, no * actions or resources on data stores","MUST",10),("Kong: route, Cognito JWT auth, rate limiting returns 429","Scored",15),("Network design: private subnets, SGs, VPC endpoints, Route 53 record, CloudTrail on (diagram + explanation)","Scored",10),("Apigee to Kong mapping table (policies to plugins)","Scored",5)]),
 ("M5","CP5",[("Multi-stage, non-root image; 0 critical/high vulnerabilities in scan","MUST",10),("All infrastructure in CloudFormation; drift detection shows no drift","MUST",15),("ECS service or Lambda deployed from the pipeline","Scored",10),("GitHub Actions: lint, build, test, scan, required on PR","Scored",10),("Buildkite deploy pipeline with manual approval step","Scored",5)]),
 ("M6","CP6",[("100% pass of go lint, build, test in CI; business-logic coverage at or above team threshold","MUST",10),("Trace/correlation ID propagated API to queue to consumer, visible in Datadog APM and logs","MUST",15),("Dashboard (Datadog or CloudWatch) with latency, error rate, DLQ depth","Scored",10),("PagerDuty alert routed from a monitor","Scored",5),("Runbook in Confluence linked from the alert; Jira tickets for all work","Scored",10)]),
]
row = 5; rows_by_mod = {}
for mod,cp,items in R:
    start = row
    for it,tp,pts in items:
        for j,v in enumerate([mod,cp,it,tp,pts,None,None,None],1):
            c = dd.cell(row=row, column=j, value=v); c.font = font(bold=(j==4 and tp=="MUST")); c.border = BOX; c.alignment = wrap
        for j in (6,7,8): dd.cell(row=row, column=j).fill = YEL
        row += 1
    rows_by_mod[mod] = (start, row-1)
DD_LAST = row-1
dv5 = DataValidation(type="list", formula1='"Yes,Partly,No"', allow_blank=True); dd.add_data_validation(dv5); dv5.add(f"F5:F{DD_LAST}")
dd.conditional_formatting.add(f"F5:F{DD_LAST}", CellIsRule(operator="equal", formula=['"No"'], fill=PatternFill("solid", bgColor="F8CBAD", fgColor="F8CBAD")))
dd.freeze_panes = "D5"

wb._sheets = [wb["Read me"], wb["Profile"], wb["Topic Tracker"], wb["DoD Checklist"]]
for ws in wb: ws.sheet_view.showGridLines = False
out = "/home/claude/dr/AiMentor Daily Progress Report - TEMPLATE.xlsx"
wb.save(out); print(out, "topics", TT_LAST-4, "dod", DD_LAST-4)
