import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2004gaofeng-institutions-batch-n"
DOC = "2004-gaofeng-zhongguo-shejishi"
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


ledger = [json.loads(l) for l in (PKG / "candidate-decision-ledger.jsonl").read_text(encoding="utf-8").splitlines()]
plan = [json.loads(l) for l in (PKG / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines()]
mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))

if len(ledger) != 27: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 9: fail(f"candidates {len(cands)}")
terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
if len(terminal) != 9: fail("terminal count")
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
if len(applied) != 9: fail(f"applied {len(applied)}")
if len(no_delta) != 0: fail(f"no_delta {len(no_delta)}")
if len(rejected) != 0: fail(f"rejected {len(rejected)}")
for c, rs in terminal.items():
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}")
    if rs[-1].get("target_ref") is None: fail(f"terminal no target_ref {c}")
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "ready_for_review": fail(f"row1 {c}")
    if rs[1]["expected_state"] != "ready_for_review" or rs[1]["state"] != "approved": fail(f"row2 {c}")
    if rs[2]["expected_state"] != "approved": fail(f"row3 expected {c}")

if len(plan) != 9: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 8: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 1: fail("plan update count")
for r in plan:
    p = ROOT / r["target_ref"]
    if not p.exists(): fail(f"missing target {r['target_ref']}"); continue
    f = fp_bytes(p.read_bytes())
    if r["action"] == "create" and r["before"] is not None: fail(f"create before not null {r['target_ref']}")
    if r["action"] == "update":
        head = subprocess.check_output(["git", "show", f"HEAD:{r['target_ref']}"], cwd=ROOT)
        hf = fp_bytes(head)
        if r["before"] != hf: fail(f"before mismatch {r['target_ref']}")
    if r["after_sha256"] != f["sha256"]: fail(f"after sha mismatch {r['target_ref']}")
    if r["bytes"] != f["bytes"] or r["lines"] != f["lines"]: fail(f"size mismatch {r['target_ref']}")

if len(mapping) != 9: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 8: fail("mapping create")
if sum(1 for e in mapping if e["action"] == "update") != 1: fail("mapping update")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")

new_files = [
    "yuan-dai-huaju.md", "wuyingdian-xiushuchu.md", "hunan-ciye-gongsi.md",
    "jichanglong-sichang.md", "shanghai-jiqi-zhibuju.md", "jingdezhen-ciye-gongsi.md",
    "dian-shizhai.md", "qiyi-gongsi.md",
]
sections = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
for name in new_files:
    p = ROOT / "04-knowledge" / "units" / "institutions" / name
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"): fail(f"BOM {name}")
    text = raw.decode("utf-8")
    if not text.endswith("\n"): fail(f"no trailing newline {name}")
    for s in sections:
        if s not in text: fail(f"missing section {s} {name}")
    fm = parse_frontmatter(text)
    if fm.get("type") != "institution": fail(f"type {name}")
    if fm.get("source_count") != "1": fail(f"source_count {name} = {fm.get('source_count')}")
    if len([l for l in text.split("---", 2)[1].splitlines() if l.strip().startswith("- citation:")]) != 1:
        fail(f"citation count {name}")
    if fm.get("version") != "1": fail(f"version {name}")
    if fm.get("evidence_status") != "source_backed": fail(f"evidence_status {name}")
    if fm.get("primary_dimension") not in {"A", "B", "C", "D", "E"}: fail(f"dimension {name}")

checks = {
    "yuan-dai-huaju.md": ["至元十五年", "从八品", "掌描造诸色样制", "百余户", "将作院"],
    "wuyingdian-xiushuchu.md": ["500 余种", "金简", "25.3 万个", "134 种 2389 卷"],
    "hunan-ciye-gongsi.md": ["熊希龄", "1906 年", "陶画、辘轳、模型", "五万元", "釉下花瓷", "1907—1912"],
    "jichanglong-sichang.md": ["1872 年", "陈启源", "广东南海", "法国", "直缫坐缫机"],
    "shanghai-jiqi-zhibuju.md": ["1878 年", "第一个近代纺织厂", "英、美", "1890 年"],
    "jingdezhen-ciye-gongsi.md": ["1910 年", "江西瓷业公司", "鄱阳", "陶业学堂", "煤窑"],
    "dian-shizhai.md": ["1876 年", "英商", "蒸汽机", "200 名工人", "同文书局"],
    "qiyi-gongsi.md": ["1917 年", "美商", "最早的灯泡企业", "电光源"],
}
for name, needles in checks.items():
    text = (ROOT / "04-knowledge" / "units" / "institutions" / name).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text: fail(f"{name} missing {needle}")

lj = (ROOT / "04-knowledge" / "units" / "institutions" / "liangjiang-shifan-xuetang.md").read_text(encoding="utf-8")
lfm = parse_frontmatter(lj)
if lfm.get("version") != "2": fail("liangjiang version")
if lfm.get("source_count") != "3": fail(f"liangjiang source_count {lfm.get('source_count')}")
for needle in ["L5461", "李瑞清", "呈准学部", "吕凤子", "姜丹书", "两届"]:
    if needle not in lj: fail(f"liangjiang missing {needle}")
if len([l for l in lj.split("---", 2)[1].splitlines() if l.strip().startswith("- citation:")]) != 3:
    fail("liangjiang citation count")

# index idempotence
before = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
after = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
if before != after: fail("index rebuild not idempotent")
idx = json.loads(after)
if idx["by_state"] != {"applied": 846, "needs_evidence": 3634, "no_delta": 52, "rejected": 807}:
    fail(f"index state {idx['by_state']}")
index_path = ROOT / "06-runtime" / "state" / "candidate-index.jsonl"

print(json.dumps({
    "ledger_rows": len(ledger), "candidates": len(terminal), "terminal_applied": len(applied),
    "terminal_no_delta": len(no_delta), "terminal_rejected": len(rejected), "plan_rows": len(plan),
    "plan_create": sum(1 for r in plan if r["action"] == "create"),
    "plan_update": sum(1 for r in plan if r["action"] == "update"),
    "mapping_entries": len(mapping), "merged": merged,
    "index_counts": idx["by_state"], "index_sha256": fp_bytes(index_path.read_bytes())["sha256"],
    "errors": errors,
}, ensure_ascii=False, indent=2))
