import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-t"
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
manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))

if len(ledger) != 26: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 10: fail(f"candidates {len(cands)}")
expected = {f"{DOC}:{n}" for n in [
    "cand-01-04", "cand-03-31", "cand-06-04", "cand-06-05", "cand-06-07",
    "cand-07-10", "cand-07-11", "cand-07-18", "cand-07-87", "cand-08-06",
]}
if cands != expected: fail(f"candidate ids {sorted(cands)}")

terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
if len(applied) != 8: fail(f"applied {len(applied)}")
if len(rejected) != 2: fail(f"rejected {len(rejected)}")
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

if len(plan) != 8: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 5: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 3: fail("plan update count")
targets = [r["target_ref"] for r in plan]
if len(set(targets)) != len(targets): fail("duplicate plan targets")
expected_before = {
    "04-knowledge/units/institutions/shangfang.md": {"sha256": "sha256:56610b01c400d3e0e7ae7bff9db14d6881ed1f78c64a52a1e27d83183488d9d0", "bytes": 4379, "lines": 90},
    "04-knowledge/units/institutions/dongxi-zhishi.md": {"sha256": "sha256:115f5b57e3c814a60f6dcbae2648671da7bdb8b81c106456c621c45724b06d5c", "bytes": 4279, "lines": 89},
    "04-knowledge/units/institutions/han-dai-qiqi-zuofang-guan-yuan.md": {"sha256": "sha256:8bd97fd08287bf52e50c7e81e47cdb62336a7a100e4b3e38c5ae8e06cd0a051a", "bytes": 5232, "lines": 91},
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

if len(mapping) != 8: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 5: fail("mapping create")
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
    "shujun-chengdu-guanghanjun-gongguan.md": (1, 1, ["蜀郡", "成都", "广汉郡", "工官", "L2145", "L2561", "五百万", "少府", "尚方令", "考工令"]),
    "baoshi.md": (1, 1, ["暴室", "未央宫", "掖庭", "织作染练", "三辅黄图", "平准令"]),
    "pingzhunling.md": (1, 1, ["平准令", "续汉书", "主练染作彩色", "暴室", "南朝", "不作沿革合并"]),
    "yandao-muguan.md": (1, 1, ["严道", "木官", "运输木材", "汉书·地理志", "规模很大", "品种繁多"]),
    "nanchao-ranshu.md": (1, 1, ["南朝", "少府", "平准令", "染署", "宋顺帝", "刘准", "避讳", "北朝司染署"]),
    "shangfang.md": (2, 2, ["少府", "左、中、右三官署", "中尚方", "鼎壶", "弩机", "装饰具", "镜、槃、釜", "蔡伦", "永元九年"]),
    "dongxi-zhishi.md": (2, 2, ["东织室令丞", "西织室令丞", "河平元年", "绥和", "少府", "贡禹", "三工官费五千万", "东汉", "时代"]),
    "han-dai-qiqi-zuofang-guan-yuan.md": (2, 2, ["八郡", "广汉郡", "蜀郡", "河内郡", "河南郡", "颍川郡", "南阳郡", "济南郡", "泰山郡", "梓潼郡", "武都郡", "五百万", "乐浪", "6—8", "11 种分工", "金属铸器铭文"]),
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
if idx["by_state"] != {"applied": 895, "needs_evidence": 3578, "no_delta": 56, "rejected": 810}:
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
