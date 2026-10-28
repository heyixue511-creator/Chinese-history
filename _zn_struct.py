import json, re, sys
from pathlib import Path

root = Path(r"D:/中国设计史研究")
files = [x.strip() for x in (root / sys.argv[1]).read_text(encoding="utf-8").splitlines() if x.strip()]
REQ = ["title", "type", "created", "updated", "confidence", "consensus", "source_count",
       "last_verified", "review_due", "version", "evidence_status", "primary_domain",
       "primary_dimension"]
SECTIONS = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
problems = []
for f in files:
    p = root / f
    if not p.exists():
        problems.append(f"{f}: MISSING FILE")
        continue
    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        problems.append(f"{f}: no frontmatter")
        continue
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        problems.append(f"{f}: unterminated frontmatter")
        continue
    fm = {}
    cur = None
    for ln in lines[1:end]:
        m = re.match(r"^([a-z_]+):\s*(.*)$", ln)
        if m:
            cur = m.group(1)
            fm[cur] = m.group(2)
        elif cur and ln.startswith("  - "):
            fm[cur] = (fm.get(cur, "") + " | " + ln.strip()[2:]).strip(" |")
    for key in REQ:
        if key not in fm or not fm[key].strip():
            problems.append(f"{f}: missing field {key}")
    body = "\n".join(lines[end + 1:])
    for s in SECTIONS:
        if s not in body:
            problems.append(f"{f}: missing section {s}")
    if '"' in body:
        for i, ln in enumerate(lines[end + 1:], start=end + 2):
            if '"' in ln:
                problems.append(f"{f}:{i}: ASCII quote in body")
    # link check
    for m in re.finditer(r"`([a-z-]+/[a-z0-9-]+\.md)`", body):
        rel = m.group(1)
        if not (root / "04-knowledge/units" / rel).exists():
            problems.append(f"{f}: dangling link {rel}")
    # date/version consistency
    if not re.match(r"^2026-10-\d{2}$", fm.get("created") or "") or fm.get("updated") != "2026-10-27" or fm.get("last_verified") != "2026-10-27":
        problems.append(f"{f}: date inconsistency created={fm.get('created')} updated={fm.get('updated')} lv={fm.get('last_verified')}")
    if fm.get("review_due") != "2027-04-27":
        problems.append(f"{f}: review_due={fm.get('review_due')}")
    if fm.get("consensus") != "tentative":
        problems.append(f"{f}: consensus={fm.get('consensus')}")
    if fm.get("evidence_status") != "source_backed":
        problems.append(f"{f}: evidence_status={fm.get('evidence_status')}")
    if fm.get("confidence") not in ("low", "medium", "high"):
        problems.append(f"{f}: confidence={fm.get('confidence')}")
    if not re.match(r"^[1-9]\d*$", fm.get("version") or ""):
        problems.append(f"{f}: version={fm.get('version')}")
    print(f"{f}\tversion={fm.get('version')}\tsource_count={fm.get('source_count')}\tconfidence={fm.get('confidence')}\ttype={fm.get('type')}")
out = root / "_zn_struct_result.json"
out.write_text(json.dumps(problems, ensure_ascii=False, indent=1), encoding="utf-8")
print("problems:", len(problems))
