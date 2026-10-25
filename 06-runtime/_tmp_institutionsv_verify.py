import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-v"
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

if len(ledger) != 25: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 9: fail(f"candidates {len(cands)}")
expected = {f"{DOC}:{n}" for n in [
    "cand-11-53", "cand-12-21", "cand-12-34", "cand-12-51",
    "cand-12-102", "cand-12-103", "cand-13-10", "cand-13-11", "cand-13-12",
]}
if cands != expected: fail(f"candidate ids {sorted(cands)}")

terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
if len(applied) != 8: fail(f"applied {len(applied)}")
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

if len(plan) != 8: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 7: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 1: fail("plan update count")
targets = [r["target_ref"] for r in plan]
if len(set(targets)) != len(targets): fail("duplicate plan targets")
expected_before = {
    "04-knowledge/units/institutions/neiwufu-zaobanchu.md": {"sha256": "sha256:31a38778d346c3bee412243f3ffa4485d22407338e54d1878705c10c917fab02", "bytes": 6177, "lines": 103},
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
if sum(1 for e in mapping if e["action"] == "create") != 7: fail("mapping create")
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
    "guoyuanchang.md": ("government_office", 2, 1, "medium", "D", ["果园厂", "永乐", "张德刚", "包亮", "雕漆", "填漆", "厂制", "嘉兴派", "云南派", "造办处漆作", "L4385-L4391", "L4626"]),
    "wucaixia-xiufang.md": ("craft_workshop", 1, 1, "medium", "D", ["吴彩霞绣坊", "胡莲仙", "光绪", "司门口", "湘绣", "魏氏", "袁家坪", "L4659"]),
    "zhujiangying.md": ("government_office", 1, 1, "medium", "D", ["诸匠营", "军制", "土营", "木营", "金匠营", "织营", "绣锦营", "镌刻营", "3,000 余人", "百工衙", "L4933"]),
    "baigongya.md": ("government_office", 1, 1, "medium", "D", ["百工衙", "典织衙", "缝衣衙", "国帽衙", "金靴衙", "梳篦衙", "典妆衙", "典木衙", "油漆衙", "典铜衙", "典竹衙", "典石衙", "洋遮衙", "镌刻衙", "刷书衙", "绣锦衙", "结彩衙", "绣锦营", "L4933"]),
    "zhongguo-fangzhi-jianshe-gongsi.md": ("commercial_enterprise", 1, 1, "low", "D", ["中国纺织建设公司", "四大家族", "江南", "棉纺织", "官僚资本", "L4995"]),
    "zhongguo-cansi-gongsi.md": ("commercial_enterprise", 1, 1, "low", "D", ["中国蚕丝公司", "中支蚕丝组织", "江浙", "盛泽", "国民党", "L4995"]),
    "qiaoergou-taocichang.md": ("craft_workshop", 1, 1, "medium", "B", ["桥儿沟", "1944 年 5 月 13 日", "解放日报", "石膏模型", "窑炉", "200 余种", "白瓷", "本地瓷土", "第七次代表大会", "L5023-L5025"]),
    "neiwufu-zaobanchu.md": ("government_office", 4, 3, "medium", "D", ["田自秉", "康熙五十七年", "珐琅作", "粤东祥林店", "造办处漆作", "玉器", "果园厂", "L4707", "L4778"]),
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
if idx["by_state"] != {"applied": 912, "needs_evidence": 3559, "no_delta": 56, "rejected": 812}:
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
