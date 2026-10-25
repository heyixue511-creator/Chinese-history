import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-p"
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
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

if len(ledger) != 30: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 10: fail(f"candidates {len(cands)}")
expected = {f"{DOC}:{n}" for n in [
    "cand-02-59", "cand-03-23", "cand-04-116", "cand-04-73", "cand-05-105",
    "cand-05-22", "cand-08-39", "cand-08-64", "cand-09-26", "cand-09-61",
]}
if cands != expected: fail(f"candidate ids {sorted(cands)}")
terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
if len(terminal) != 10: fail("terminal count")
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
if len(applied) != 9: fail(f"applied {len(applied)}")
if len(no_delta) != 1: fail(f"no_delta {len(no_delta)}")
if len(rejected) != 0: fail(f"rejected {len(rejected)}")
for c, rs in terminal.items():
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}")
    if rs[-1].get("target_ref") is None: fail(f"terminal no target_ref {c}")
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "ready_for_review": fail(f"row1 {c}")
    if rs[1]["expected_state"] != "ready_for_review" or rs[1]["state"] != "approved": fail(f"row2 {c}")
    if rs[2]["expected_state"] != "approved": fail(f"row3 expected {c}")

if len(plan) != 9: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 9: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 0: fail("plan update count")
for r in plan:
    p = ROOT / r["target_ref"]
    if not p.exists(): fail(f"missing target {r['target_ref']}"); continue
    f = fp_bytes(p.read_bytes())
    if r["action"] == "create" and r["before"] is not None: fail(f"create before not null {r['target_ref']}")
    if r["after_sha256"] != f["sha256"]: fail(f"after sha mismatch {r['target_ref']}")
    if r["bytes"] != f["bytes"] or r["lines"] != f["lines"]: fail(f"size mismatch {r['target_ref']}")

if len(mapping) != 10: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 9: fail("mapping create")
if sum(1 for e in mapping if e["action"] == "no_delta") != 1: fail("mapping no_delta")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")

new_files = [
    "dian-si.md", "da-yuesi.md", "shiquge.md", "shanglin-sanguan.md", "shangfang.md",
    "jiaoziwu.md", "shibosi.md", "yuan-dai-yizhan.md", "xi-xia-wensiyuan.md",
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
    if DOC not in text: fail(f"doc_id missing {name}")

checks = {
    "dian-si.md": ["典丝", "筐人", "慌人", "典妇功", "zhou-ranren-zhangrancao.md"],
    "da-yuesi.md": ["大乐司", "最早的音乐教育管理部门", "70 种", "29 种"],
    "shiquge.md": ["石渠阁", "地图和书籍", "秦王朝"],
    "shanglin-sanguan.md": ["上林三官", "罢半两钱，行五铢钱", "铜质钱范", "三官"],
    "shangfang.md": ["尚方令", "蔡伦", "永元九年", "秘剑", "精工坚密"],
    "jiaoziwu.md": ["天圣元年（1023）", "益州", "铁币", "钱引", "1,256,340"],
    "shibosi.md": ["泉州港", "市舶司", "管理船政和贸易", "三千二百三十七艘"],
    "yuan-dai-yizhan.md": ["70 里", "1,500 个", "急递铺", "朝令夕至", "瘫痪"],
    "xi-xia-wensiyuan.md": ["西夏政府设置文思院", "金、银、玉、犀", "wensiyuan.md", "同名"],
}
for name, needles in checks.items():
    text = (ROOT / "04-knowledge" / "units" / "institutions" / name).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text: fail(f"{name} missing {needle}")

nod = (ROOT / "04-knowledge" / "units" / "institutions" / "han-dai-guan-ying-sizhi-zuofang.md").read_text(encoding="utf-8")
for needle in ["东、西织室", "文绣之服", "对外贸易", "L1405-L1416"]:
    if needle not in nod: fail(f"no_delta target missing {needle}")

# index idempotence
before = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
after = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
if before != after: fail("index rebuild not idempotent")
idx = json.loads(after)
if idx["by_state"] != {"applied": 857, "needs_evidence": 3619, "no_delta": 56, "rejected": 807}:
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
