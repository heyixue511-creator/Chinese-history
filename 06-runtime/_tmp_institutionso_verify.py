import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009xiayanjing-institutions-batch-o"
DOC = "2009-xiayanjing-zhongguo-shejishi"
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

if len(ledger) != 15: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 5: fail(f"candidates {len(cands)}")
expected = {
    f"{DOC}:cand-03-20", f"{DOC}:cand-03-37", f"{DOC}:cand-05-14",
    f"{DOC}:cand-06-54", f"{DOC}:cand-07-19",
}
if cands != expected: fail(f"candidate ids {sorted(cands)}")
terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
if len(terminal) != 5: fail("terminal count")
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
if len(applied) != 2: fail(f"applied {len(applied)}")
if len(no_delta) != 3: fail(f"no_delta {len(no_delta)}")
if len(rejected) != 0: fail(f"rejected {len(rejected)}")
for c, rs in terminal.items():
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}")
    if rs[-1].get("target_ref") is None: fail(f"terminal no target_ref {c}")
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "ready_for_review": fail(f"row1 {c}")
    if rs[1]["expected_state"] != "ready_for_review" or rs[1]["state"] != "approved": fail(f"row2 {c}")
    if rs[2]["expected_state"] != "approved": fail(f"row3 expected {c}")

if len(plan) != 2: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 2: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 0: fail("plan update count")
for r in plan:
    p = ROOT / r["target_ref"]
    if not p.exists(): fail(f"missing target {r['target_ref']}"); continue
    f = fp_bytes(p.read_bytes())
    if r["action"] == "create" and r["before"] is not None: fail(f"create before not null {r['target_ref']}")
    if r["after_sha256"] != f["sha256"]: fail(f"after sha mismatch {r['target_ref']}")
    if r["bytes"] != f["bytes"] or r["lines"] != f["lines"]: fail(f"size mismatch {r['target_ref']}")

if len(mapping) != 5: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 2: fail("mapping create")
if sum(1 for e in mapping if e["action"] == "no_delta") != 3: fail("mapping no_delta")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")

new_files = ["han-dai-guan-ying-sizhi-zuofang.md", "quanguo-gaoxiao-gongye-sheji-xuehui.md"]
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
    "han-dai-guan-ying-sizhi-zuofang.md": [
        "L1405-L1416", "提花织机", "素纱", "绮、罗", "锦", "纨、纻、缣、缦、绢、绫、缟、绨、绣、毂",
        "齐部世刺绣", "成都", "蜀锦", "东、西织室", "临淄", "襄邑", "数千人", "丝绸之路",
        "dongxi-zhishi.md", "sanfuguan.md", "tihuaji.md", "sichou-zhilu.md",
    ],
    "quanguo-gaoxiao-gongye-sheji-xuehui.md": [
        "L4824", "1985 年 3 月 2 日至 6 日", "北京", "第一次全国工业设计教育学术交流会",
        "events/industrial-design-society-1985.md", "professional_society",
    ],
}
for name, needles in checks.items():
    text = (ROOT / "04-knowledge" / "units" / "institutions" / name).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text: fail(f"{name} missing {needle}")

nod_checks = {
    "04-knowledge/units/institutions/han-dai-qiqi-zuofang-guan-yuan.md": [
        "秦代", "郡国", "山东", "蜀郡", "广汉", "6—8 道", "金银扣器",
    ],
    "04-knowledge/units/institutions/kezisi.md": [
        "刻字司", "佛经为最多", "文学、法律、医术、日历、卜筮、咒文", "活字印本", "桥梁作用",
    ],
    "04-knowledge/units/institutions/zhongyang-shougongye-guanliju.md": [
        "1954 年 12 月 8 日", "第四次全国手工业生产合作会议", "1961 年 9 月", "第二轻工业部",
    ],
}
for rel, needles in nod_checks.items():
    p = ROOT / rel
    if not p.exists():
        fail(f"missing no_delta target {rel}"); continue
    text = p.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text: fail(f"{rel} missing {needle}")

# index idempotence
before = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
after = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
if before != after: fail("index rebuild not idempotent")
idx = json.loads(after)
if idx["by_state"] != {"applied": 848, "needs_evidence": 3629, "no_delta": 55, "rejected": 807}:
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
