import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-w"
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

if len(ledger) != 24: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 8: fail(f"candidates {len(cands)}")
expected = {f"{DOC}:{n}" for n in [
    "cand-13-82", "cand-13-83", "cand-13-13", "cand-13-81",
    "cand-13-15", "cand-13-14", "cand-13-16", "cand-14-21",
]}
if cands != expected: fail(f"candidate ids {sorted(cands)}")

terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
if len(applied) != 7: fail(f"applied {len(applied)}")
if len(rejected) != 0: fail(f"rejected {len(rejected)}")
if len(no_delta) != 1: fail(f"no_delta {len(no_delta)}")

for c in applied + no_delta:
    rs = terminal[c]
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}"); continue
    if rs[-1].get("target_ref") is None: fail(f"terminal no target_ref {c}")
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "ready_for_review": fail(f"row1 {c}")
    if rs[1]["expected_state"] != "ready_for_review" or rs[1]["state"] != "approved": fail(f"row2 {c}")
    if rs[2]["expected_state"] != "approved": fail(f"row3 expected {c}")

for c in no_delta:
    if terminal[c][-1]["decision"]["status"] != "approved": fail(f"no_delta decision status {c}")
    if terminal[c][-1]["target_ref"] != "04-knowledge/units/institutions/hangzhou-guoli-yizhuan.md": fail(f"no_delta target {c}")

if len(plan) != 7: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 6: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 1: fail("plan update count")
targets = [r["target_ref"] for r in plan]
if len(set(targets)) != len(targets): fail("duplicate plan targets")
expected_before = {
    "04-knowledge/units/institutions/nanjing-yunjin-yanjiusuo.md": {"sha256": "sha256:e7a06c22a3e5c7d5e18ccd5c712aa2fc9f947537e8d38a151e884662670c6254", "bytes": 3598, "lines": 84},
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

if len(mapping) != 7: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 6: fail("mapping create")
if sum(1 for e in mapping if e["action"] == "update") != 1: fail("mapping update")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")
if {e["target_ref"] for e in mapping} != set(targets): fail("mapping targets differ from plan")
for e in mapping:
    pr = next((r for r in plan if r["target_ref"] == e["target_ref"]), None)
    if pr is None: fail(f"mapping no plan row {e['target_ref']}")
    elif pr["action"] != e["action"]: fail(f"mapping action differs {e['target_ref']}")
    elif pr["candidate_id"] != e["canonical_candidate"]: fail(f"mapping candidate differs {e['target_ref']}")

files = {
    "jianhua-cichang.md": ("craft_workshop", 1, 1, "medium", "B", ["建华瓷厂", "衣食村", "细瓷", "古铜", "淡红", "陇东", "L5023-L5025"]),
    "jiefangqu-diyige-taoci-yanjiusuo.md": ("research_institute", 1, 1, "low", "D", ["解放区第一个陶瓷研究所", "磁州", "陶瓷生产", "正式所名", "L5023-L5025"]),
    "yanan-bolichang.md": ("craft_workshop", 1, 1, "medium", "B", ["1941", "延安", "玻璃厂", "石英", "坩埚", "灯罩", "微带绿色", "L5027"]),
    "suzhou-cixiu-yanjiusuo.md": ("research_institute", 1, 1, "medium", "B", ["1957", "苏州刺绣研究所", "猫", "金鱼", "双面绣", "乱针绣", "20 多种", "L5138-L5142"]),
    "beijing-falangchang.md": ("craft_workshop", 1, 1, "low", "B", ["北京珐琅厂", "景泰蓝", "规模较大", "北京工艺美术厂", "上海", "L5176-L5178"]),
    "guangdong-nanhai-tengchang.md": ("craft_workshop", 1, 1, "low", "B", ["广东南海藤厂", "藤编", "大型", "合丝", "沙丝", "梨皮", "L5258"]),
    "nanjing-yunjin-yanjiusuo.md": ("research_institute", 3, 2, "medium", "B", ["田自秉", "1957年7月", "云锦研究所", "量题定格", "天华锦", "雨花锦", "双面锦", "凹凸锦", "L5103"]),
}
sections = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
for name, (sub_type, ncitation, version, confidence, dimension, needles) in files.items():
    p = ROOT / "04-knowledge" / "units" / "institutions" / name
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"): fail(f"BOM {name}")
    text = raw.decode("utf-8")
    if not text.endswith("\n"): fail(f"no trailing newline {name}")
    for s in sections:
        if s not in text: fail(f"missing section {s} {name}")
    fm = parse_frontmatter(text)
    if fm.get("type") != "institution": fail(f"type {name}")
    if fm.get("sub_type") != sub_type: fail(f"sub_type {name} = {fm.get('sub_type')}")
    if fm.get("source_count") != str(ncitation): fail(f"source_count {name} = {fm.get('source_count')}")
    if citations(text) != ncitation: fail(f"citation count {name} = {citations(text)}")
    if fm.get("version") != str(version): fail(f"version {name} = {fm.get('version')}")
    if fm.get("evidence_status") != "source_backed": fail(f"evidence_status {name}")
    if fm.get("primary_dimension") != dimension: fail(f"dimension {name}")
    if fm.get("confidence") != confidence: fail(f"confidence {name}")
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
if idx["by_state"] != {"applied": 919, "needs_evidence": 3551, "no_delta": 57, "rejected": 812}:
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
