import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-q"
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

if len(ledger) != 28: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 10: fail(f"candidates {len(cands)}")
expected = {f"{DOC}:{n}" for n in [
    "cand-09-64", "cand-10-105", "cand-10-110", "cand-10-135", "cand-10-148",
    "cand-10-149", "cand-10-150", "cand-10-151", "cand-10-47", "cand-10-48",
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

rej_id = f"{DOC}:cand-10-135"
if rejected != [rej_id]: fail(f"rejected id {rejected}")
rs = terminal[rej_id]
if len(rs) != 1: fail(f"rejected rows {len(rs)}")
else:
    r = rs[0]
    if r["expected_state"] != "needs_evidence" or r["state"] != "rejected": fail("rejected row state")
    if r["decision"]["status"] != "rejected": fail("rejected decision status")
    if r.get("target_ref") is not None: fail("rejected has target_ref")

for c in applied:
    rs = terminal[c]
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}"); continue
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
        if not isinstance(r["before"], dict): fail(f"update before not object {r['target_ref']}")
        else:
            if r["before"]["sha256"] == f["sha256"]: fail(f"update before equals after {r['target_ref']}")
            if r["before"]["sha256"] != "sha256:b37a0deac1808c89754ffd2a9b2109fdb0e324afbeb6af0dc89e7ae52e0cb560":
                fail(f"update before sha unexpected {r['before']['sha256']}")
    if r["after_sha256"] != f["sha256"]: fail(f"after sha mismatch {r['target_ref']}")
    if r["bytes"] != f["bytes"] or r["lines"] != f["lines"]: fail(f"size mismatch {r['target_ref']}")

if len(mapping) != 9: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 8: fail("mapping create")
if sum(1 for e in mapping if e["action"] == "update") != 1: fail("mapping update")
if any(e["action"] == "rejected" for e in mapping): fail("mapping has rejected")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")

new_files = [
    "sinongsi.md", "huitongguan.md", "jinling-shuju.md", "hunan-sixian-shuju.md",
    "zhejiang-shuju.md", "chengdu-cungu-shuju.md", "liubiju.md", "wangmazi-jiandao-pu.md",
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
    "sinongsi.md": ["司农司", "劝农官", "国以民为本", "提刑按察司", "风土之所宜"],
    "huitongguan.md": ["会通馆", "宋诸臣奏议", "现存最早的铜活字印刷书籍", "秩序化"],
    "jinling-shuju.md": ["金陵书局", "曾国藩", "同治年间", "二十四史", "流布雅俗"],
    "hunan-sixian-shuju.md": ["思贤书局", "王船山遗书", "王船山", "社会变革"],
    "zhejiang-shuju.md": ["浙江书局", "二十二子", "革故鼎新"],
    "chengdu-cungu-shuju.md": ["存古书局", "说文解字注", "革故鼎新"],
    "liubiju.md": ["六必居", "酱菜", "流传至今", "招牌"],
    "wangmazi-jiandao-pu.md": ["王麻子剪刀铺", "9-15", "商业信誉", "剪刀"],
}
for name, needles in checks.items():
    text = (ROOT / "04-knowledge" / "units" / "institutions" / name).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text: fail(f"{name} missing {needle}")

wy = (ROOT / "04-knowledge" / "units" / "institutions" / "wuyingdian-xiushuchu.md").read_text(encoding="utf-8")
wy_fm = parse_frontmatter(wy)
if wy_fm.get("source_count") != "2": fail(f"wuyingdian source_count {wy_fm.get('source_count')}")
if wy_fm.get("version") != "2": fail(f"wuyingdian version {wy_fm.get('version')}")
if len([l for l in wy.split("---", 2)[1].splitlines() if l.strip().startswith("- citation:")]) != 2:
    fail("wuyingdian citation count")
for needle in ["武英殿", "英武殿本", "殿本", "十三经", "二十一史", "79,000", "1,669",
               "武英殿聚珍版程式", "赵农", "- 武英殿"]:
    if needle not in wy: fail(f"wuyingdian missing {needle}")

# index idempotence
before = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
after = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
if before != after: fail("index rebuild not idempotent")
idx = json.loads(after)
if idx["by_state"] != {"applied": 866, "needs_evidence": 3609, "no_delta": 56, "rejected": 808}:
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
