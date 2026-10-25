import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-r"
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
    "cand-10-56", "cand-10-93", "cand-10-98", "cand-11-045", "cand-11-046",
    "cand-11-105", "cand-11-130", "cand-12-132", "cand-12-134", "cand-12-135",
]}
if cands != expected: fail(f"candidate ids {sorted(cands)}")

terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
if len(applied) != 10: fail(f"applied {len(applied)}")
if len(rejected) != 0: fail(f"rejected {len(rejected)}")
if len(no_delta) != 0: fail(f"no_delta {len(no_delta)}")

for c in applied:
    rs = terminal[c]
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}"); continue
    if rs[-1].get("target_ref") is None: fail(f"terminal no target_ref {c}")
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "ready_for_review": fail(f"row1 {c}")
    if rs[1]["expected_state"] != "ready_for_review" or rs[1]["state"] != "approved": fail(f"row2 {c}")
    if rs[2]["expected_state"] != "approved": fail(f"row3 expected {c}")

if len(plan) != 10: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 8: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 2: fail("plan update count")
expected_before = {
    "04-knowledge/units/institutions/neiwufu-zaobanchu.md": "sha256:6bfb1f01b150e03572c16603cc9a3c81303fb56f07e78a3890461f0c14c488db",
    "04-knowledge/units/institutions/jiangning-zhizaoju.md": "sha256:bf167c67b62131bd1827182f5cfc4347db82b0d48629575a1496064845090749",
}
for r in plan:
    p = ROOT / r["target_ref"]
    if not p.exists(): fail(f"missing target {r['target_ref']}"); continue
    f = fp_bytes(p.read_bytes())
    if r["action"] == "create" and r["before"] is not None: fail(f"create before not null {r['target_ref']}")
    if r["action"] == "update":
        if not isinstance(r["before"], dict): fail(f"update before not object {r['target_ref']}")
        else:
            if r["before"]["sha256"] == f["sha256"]: fail(f"update before equals after {r['target_ref']}")
            if r["before"]["sha256"] != expected_before[r["target_ref"]]:
                fail(f"update before sha unexpected {r['target_ref']} {r['before']['sha256']}")
    if r["after_sha256"] != f["sha256"]: fail(f"after sha mismatch {r['target_ref']}")
    if r["bytes"] != f["bytes"] or r["lines"] != f["lines"]: fail(f"size mismatch {r['target_ref']}")

if len(mapping) != 10: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 8: fail("mapping create")
if sum(1 for e in mapping if e["action"] == "update") != 2: fail("mapping update")
if any(e["action"] == "rejected" for e in mapping): fail("mapping has rejected")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")

new_files = [
    "taiwan-youzheng-zongju.md", "jingchang.md", "jianyang-shufang.md", "bauhaus.md",
    "zhongguo-yingzao-xueshe.md", "jinling-jiqiju.md", "tianjin-jiqiju.md", "hubei-qiangpaochang.md",
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
    "taiwan-youzheng-zongju.md": ["台湾邮政总局", "刘铭传", "1888", "台湾邮票", "邮政商票", "存根", "商业邮政"],
    "jingchang.md": ["经厂", "司礼监", "内府", "200 余种", "折配工", "装订工", "文字错误较多"],
    "jianyang-shufang.md": ["建阳书坊", "80 余家", "插图本", "朱熹", "吕祖谦", "24 家", "10 余家"],
    "bauhaus.md": ["包豪斯", "1919", "Bauhuas", "学科剥离", "装饰艺术运动"],
    "zhongguo-yingzao-xueshe.md": ["中国营造学社", "朱启钤", "1925", "1930", "1946", "梁思成", "刘敦桢", "园冶", "梓人遗制", "中国建筑史"],
    "jinling-jiqiju.md": ["金陵机器局", "1865", "官商一体", "江南制造总局"],
    "tianjin-jiqiju.md": ["天津机器局", "1867", "官商一体", "江南制造总局"],
    "hubei-qiangpaochang.md": ["湖北枪炮厂", "1891", "官商一体", "江南制造总局"],
}
for name, needles in checks.items():
    text = (ROOT / "04-knowledge" / "units" / "institutions" / name).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text: fail(f"{name} missing {needle}")

nei = (ROOT / "04-knowledge" / "units" / "institutions" / "neiwufu-zaobanchu.md").read_text(encoding="utf-8")
nei_fm = parse_frontmatter(nei)
if nei_fm.get("source_count") != "3": fail(f"neiwufu source_count {nei_fm.get('source_count')}")
if nei_fm.get("version") != "2": fail(f"neiwufu version {nei_fm.get('version')}")
if len([l for l in nei.split("---", 2)[1].splitlines() if l.strip().startswith("- citation:")]) != 3:
    fail("neiwufu citation count")
if "- 养心殿造办处" not in nei: fail("neiwufu missing alias")
for needle in ["养心殿造办处", "服饰", "赵农", "名称差异"]:
    if needle not in nei: fail(f"neiwufu missing {needle}")

jn = (ROOT / "04-knowledge" / "units" / "institutions" / "jiangning-zhizaoju.md").read_text(encoding="utf-8")
jn_fm = parse_frontmatter(jn)
if jn_fm.get("source_count") != "4": fail(f"jiangning source_count {jn_fm.get('source_count')}")
if jn_fm.get("version") != "2": fail(f"jiangning version {jn_fm.get('version')}")
if len([l for l in jn.split("---", 2)[1].splitlines() if l.strip().startswith("- citation:")]) != 4:
    fail("jiangning citation count")
if "- 江南织造" not in jn: fail("jiangning missing alias")
for needle in ["江南织造", "采买丝绸织物", "在南京设立", "赵农", "指称范围"]:
    if needle not in jn: fail(f"jiangning missing {needle}")

# index idempotence
before = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
after = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
if before != after: fail("index rebuild not idempotent")
idx = json.loads(after)
if idx["by_state"] != {"applied": 876, "needs_evidence": 3599, "no_delta": 56, "rejected": 808}:
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
