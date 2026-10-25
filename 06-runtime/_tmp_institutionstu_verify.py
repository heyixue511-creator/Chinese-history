import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-u"
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
errors = []


def fail(msg):
    errors.append(msg)


def fp_bytes(raw: bytes) -> dict:
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {"sha256": "sha256:" + hashlib.sha256(data).hexdigest(), "bytes": len(data), "lines": text.count("\n")}


def parse_frontmatter(text: str) -> dict:
    fm = text.split("---", 2)[1]
    out = {}
    key = None
    for line in fm.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - "):
            if key is None:
                continue
            out.setdefault(key, []).append(line[4:].strip())
        elif re.match(r"^[A-Za-z_]+:", line):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            out[key] = val if val else []
    return out


def citations(text: str) -> int:
    return len([l for l in text.split("---", 2)[1].splitlines() if l.strip().startswith("- citation:")])


ledger = [json.loads(l) for l in (PKG / "candidate-decision-ledger.jsonl").read_text(encoding="utf-8").splitlines()]
plan = [json.loads(l) for l in (PKG / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines()]
mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))

if len(ledger) != 28: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 10: fail(f"candidates {len(cands)}")
expected = {f"{DOC}:{n}" for n in [
    "cand-08-07", "cand-09-14", "cand-09-33", "cand-09-34", "cand-09-95",
    "cand-10-15", "cand-10-27", "cand-10-66", "cand-10-68", "cand-10-72",
]}
if cands != expected: fail(f"candidate ids {sorted(cands)}")

terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
if len(applied) != 9: fail(f"applied {len(applied)}")
if len(rejected) != 1: fail(f"rejected {len(rejected)}")
if len(no_delta) != 0: fail(f"no_delta {len(no_delta)}")

for c in applied:
    rs = terminal[c]
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}"); continue
    if rs[-1].get("target_ref") is None: fail(f"terminal no target_ref {c}")
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "ready_for_review": fail(f"row1 {c}")
    if rs[1]["expected_state"] != "ready_for_review" or rs[1]["state"] != "approved": fail(f"row2 {c}")
    if rs[2]["expected_state"] != "approved": fail(f"row3 expected {c}")

for c in rejected:
    rs = terminal[c]
    if len(rs) != 1: fail(f"rejected rows {c} -> {len(rs)}"); continue
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "rejected": fail(f"rejected state {c}")
    if rs[0]["decision"]["status"] != "rejected": fail(f"rejected decision {c}")
    if "target_ref" in rs[0]: fail(f"rejected target_ref {c}")

if len(plan) != 9: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 6: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 3: fail("plan update count")
targets = [r["target_ref"] for r in plan]
if len(set(targets)) != len(targets): fail("duplicate plan targets")
expected_before = {
    "04-knowledge/units/institutions/lingjinyuan.md": {"sha256": "sha256:2e1cb4360a3e54f899c4cb0d032e2d12ad2c62ce78e1b8b91dd618d752deab58", "bytes": 7699, "lines": 119},
    "04-knowledge/units/institutions/xi-xia-guan-ying-shou-gong-ye-jigou.md": {"sha256": "sha256:4bb0068d90e3262be1a71aac5130144a58a6fbb6632d1e999d8266b7716a05d8", "bytes": 4868, "lines": 99},
    "04-knowledge/units/institutions/jiankanglu-zhiranju.md": {"sha256": "sha256:515e29fc47c0c69564eb0b18e937ee176fbc58d1d1def4f4fe2a3426c85f01ad", "bytes": 5050, "lines": 90},
}
for r in plan:
    p = ROOT / r["target_ref"]
    if not p.exists(): fail(f"missing target {r['target_ref']}"); continue
    f = fp_bytes(p.read_bytes())
    if r["action"] == "create" and r["before"] is not None: fail(f"create before not null {r['target_ref']}")
    if r["action"] == "update":
        if r["before"] != expected_before.get(r["target_ref"]): fail(f"update before mismatch {r['target_ref']}: {r['before']}")
    if r["after_sha256"] != f["sha256"]: fail(f"after sha mismatch {r['target_ref']}")
    if r["bytes"] != f["bytes"] or r["lines"] != f["lines"]: fail(f"size mismatch {r['target_ref']}")

if len(mapping) != 9: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 6: fail("mapping create")
if sum(1 for e in mapping if e["action"] == "update") != 3: fail("mapping update")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")
if {e["target_ref"] for e in mapping} != set(targets): fail("mapping targets differ from plan")
for e in mapping:
    pr = next((r for r in plan if r["target_ref"] == e["target_ref"]), None)
    if pr is None: fail(f"mapping no plan row {e['target_ref']}")
    elif pr["action"] != e["action"]: fail(f"mapping action differs {e['target_ref']}")
    elif pr["candidate_id"] != e["canonical_candidate"]: fail(f"mapping candidate differs {e['target_ref']}")

files = {
    "houzhao-yecheng-zhijinshu.md": (1, 1, ["织锦署", "邺城", "邺中记", "大登高", "蒲桃文锦", "蜀绨", "工巧百数", "东晋", "同名异实", "L2918"]),
    "ciyaoguan.md": (1, 1, ["瓷窑官", "窑务", "宋会要辑稿", "太平兴国", "幽州", "伪瓷窑官", "赤峰缸瓦窑屯", "官”字款", "L3693"]),
    "sichuan-jinyuan.md": (1, 1, ["元丰六年", "军匠 500 人", "挽综工", "杼工", "练染工", "纺绎工", "154 张", "125,000 两", "211,000 斤", "上贡锦", "官诰锦", "广西锦", "乾道四年", "L3792-L3794"]),
    "xiuyuan.md": (1, 1, ["绣院", "300 余人", "神针", "画绣", "筠清轩秘录", "存素堂丝绣录", "5,996 字", "56 页", "文绣院", "L3830-L3832"]),
    "nashishiju.md": (1, 1, ["纳失失", "纳石失", "纳失思", "纳克实", "弘州", "荨麻林", "3,300 多户", "织染杂造人匠都总管府", "别失八里局", "忽丹八里局", "畏兀兀", "L4036-L4042"]),
    "mumian-tijusi.md": (1, 1, ["木棉提举司", "至元二十六年", "1289", "浙东", "江东", "江西", "湖广", "福建", "都提举司", "10 万匹", "松江", "L4072"]),
    "lingjinyuan.md": (6, 3, ["L3488", "灵、锦、显、霸", "宜州", "织金丝织品", "上京、祖州"]),
    "xi-xia-guan-ying-shou-gong-ye-jigou.md": (2, 2, ["出车（造车）院", "氆氇", "毛布", "L3494"]),
    "jiankanglu-zhiranju.md": (2, 2, ["建康织染局", "三千六户", "三千六百户", "42 万", "L4030"]),
}
sections = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
for name, (ncitation, version, needles) in files.items():
    p = ROOT / "04-knowledge" / "units" / "institutions" / name
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"): fail(f"BOM {name}")
    text = raw.decode("utf-8")
    if not text.endswith("\n"): fail(f"no trailing newline {name}")
    for s in sections:
        if s not in text: fail(f"missing section {s} {name}")
    fm = parse_frontmatter(text)
    if fm.get("type") != "institution": fail(f"type {name}")
    if fm.get("sub_type") != "government_office": fail(f"sub_type {name}")
    if fm.get("source_count") != str(ncitation): fail(f"source_count {name} = {fm.get('source_count')}")
    if citations(text) != ncitation: fail(f"citation count {name} = {citations(text)}")
    if fm.get("version") != str(version): fail(f"version {name} = {fm.get('version')}")
    if fm.get("evidence_status") != "source_backed": fail(f"evidence_status {name}")
    if fm.get("primary_dimension") != "D": fail(f"dimension {name}")
    if fm.get("confidence") != "medium": fail(f"confidence {name}")
    if fm.get("consensus") != "tentative": fail(f"consensus {name}")
    title = fm.get("title", "")
    if "（" not in title or "）" not in title or not re.search(r"[A-Za-z]", title.split("（", 1)[1]): fail(f"title not bilingual {name}: {title}")
    if DOC not in text: fail(f"doc_id missing {name}")
    for needle in needles:
        if needle not in text: fail(f"{name} missing {needle}")

# index idempotence
before = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
after = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
if before != after: fail("index rebuild not idempotent")
idx = json.loads(after)
if idx["by_state"] != {"applied": 904, "needs_evidence": 3568, "no_delta": 56, "rejected": 811}:
    fail(f"index state {idx['by_state']}")
index_path = ROOT / "06-runtime" / "state" / "candidate-index.jsonl"
if idx["total"] != 5339: fail(f"index total {idx['total']}")

print(json.dumps({
    "ledger_rows": len(ledger), "candidates": len(terminal), "terminal_applied": len(applied),
    "terminal_no_delta": len(no_delta), "terminal_rejected": len(rejected), "plan_rows": len(plan),
    "plan_create": sum(1 for r in plan if r["action"] == "create"),
    "plan_update": sum(1 for r in plan if r["action"] == "update"),
    "mapping_entries": len(mapping), "merged": merged,
    "index_counts": idx["by_state"], "index_sha256": fp_bytes(index_path.read_bytes())["sha256"],
    "errors": errors,
}, ensure_ascii=False, indent=2))
