import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-s"
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


def citations(text: str) -> int:
    return len([l for l in text.split("---", 2)[1].splitlines() if l.strip().startswith("- citation:")])


ledger = [json.loads(l) for l in (PKG / "candidate-decision-ledger.jsonl").read_text(encoding="utf-8").splitlines()]
plan = [json.loads(l) for l in (PKG / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines()]
mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))

if len(ledger) != 33: fail(f"ledger rows {len(ledger)}")
cands = {r["candidate_id"] for r in ledger}
if len(cands) != 11: fail(f"candidates {len(cands)}")
expected = {f"{DOC}:{n}" for n in [
    "cand-12-27", "cand-12-29", "cand-12-38", "cand-12-68",
    "cand-12-85", "cand-12-86", "cand-12-92", "cand-12-93",
    "cand-12-95", "cand-12-137", "cand-12-165",
]}
if cands != expected: fail(f"candidate ids {sorted(cands)}")

terminal = {}
for r in ledger:
    terminal.setdefault(r["candidate_id"], []).append(r)
applied = [c for c, rs in terminal.items() if rs[-1]["state"] == "applied"]
rejected = [c for c, rs in terminal.items() if rs[-1]["state"] == "rejected"]
no_delta = [c for c, rs in terminal.items() if rs[-1]["state"] == "no_delta"]
if len(applied) != 11: fail(f"applied {len(applied)}")
if len(rejected) != 0: fail(f"rejected {len(rejected)}")
if len(no_delta) != 0: fail(f"no_delta {len(no_delta)}")

for c in applied:
    rs = terminal[c]
    if len(rs) != 3: fail(f"three-row {c} -> {len(rs)}"); continue
    if rs[-1].get("target_ref") is None: fail(f"terminal no target_ref {c}")
    if rs[0]["expected_state"] != "needs_evidence" or rs[0]["state"] != "ready_for_review": fail(f"row1 {c}")
    if rs[1]["expected_state"] != "ready_for_review" or rs[1]["state"] != "approved": fail(f"row2 {c}")
    if rs[2]["expected_state"] != "approved": fail(f"row3 expected {c}")

if len(plan) != 11: fail(f"plan rows {len(plan)}")
if sum(1 for r in plan if r["action"] == "create") != 11: fail("plan create count")
if sum(1 for r in plan if r["action"] == "update") != 0: fail("plan update count")
targets = [r["target_ref"] for r in plan]
if len(set(targets)) != len(targets): fail("duplicate plan targets")
for r in plan:
    p = ROOT / r["target_ref"]
    if not p.exists(): fail(f"missing target {r['target_ref']}"); continue
    f = fp_bytes(p.read_bytes())
    if r["action"] == "create" and r["before"] is not None: fail(f"create before not null {r['target_ref']}")
    if r["after_sha256"] != f["sha256"]: fail(f"after sha mismatch {r['target_ref']}")
    if r["bytes"] != f["bytes"] or r["lines"] != f["lines"]: fail(f"size mismatch {r['target_ref']}")

if len(mapping) != 11: fail(f"mapping entries {len(mapping)}")
if sum(1 for e in mapping if e["action"] == "create") != 11: fail("mapping create")
if any(e["action"] != "create" for e in mapping): fail("mapping non-create")
merged = [m for e in mapping for m in e["merged_candidates"]]
if merged: fail(f"merged {merged}")
if {e["target_ref"] for e in mapping} != set(targets): fail("mapping targets differ from plan")

files = {
    "dasheng-shachang.md": (2, ["大生纱厂", "1899", "南通", "张謇", "官商一体", "大生二厂", "高丰", "赵农"]),
    "yiwensi-tushu-gongsi.md": (2, ["伊文思图书公司", "1926", "南京东路", "南京路", "吊灯广告", "霓虹灯", "皇家牌", "打字机"]),
    "lunzhang-zaozhi-ju.md": (1, ["纶章造纸局", "1891", "李鸿章", "第一家", "上海", "待核"]),
    "guangzhou-zaozhichang.md": (1, ["广州造纸厂", "民国时期", "新闻纸", "进口纸浆", "抗日战争", "规模化"]),
    "yingmei-yancao-gongsi.md": (5, ["英美烟草公司", "广告部", "规模最大", "胡伯翔", "张光宇", "丁纳", "丁讷", "月份牌", "驻厂设计师", "哈德门", "老刀牌", "红锡包"]),
    "zhongguo-renmin-yinhang.md": (1, ["中国人民银行", "1948", "人民币", "5 套", "元、角、分", "十进位", "防伪"]),
    "fuzhou-mawei-chuanzheng-xuetang-huishiyuan.md": (1, ["绘事院", "1867", "福州马尾船政学堂", "江南船政局", "福建船政局"]),
    "jiangnan-chuanzhengju-gongyi-xuetang.md": (1, ["江南船政局工艺学堂", "1888", "江南制造总局", "待核"]),
    "beiping-guoli-yizhuan.md": (1, ["北平国立艺专", "图案系", "杭州国立艺专", "1949", "蔡元培"]),
    "hangzhou-guoli-yizhuan.md": (2, ["杭州国立艺专", "国立杭州艺术专科学校", "图案系", "1950", "中央美术学院华东分院", "实用美术系", "1956", "田自秉", "中央工艺美术学院"]),
    "qinggongbu-qinggong-xueyuan.md": (1, ["无锡轻工学院", "大连轻工学院", "北京轻工学院", "西北轻工学院", "轻工部", "市场调研", "院校群"]),
}
sections = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
for name, (ncitation, needles) in files.items():
    p = ROOT / "04-knowledge" / "units" / "institutions" / name
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"): fail(f"BOM {name}")
    text = raw.decode("utf-8")
    if not text.endswith("\n"): fail(f"no trailing newline {name}")
    for s in sections:
        if s not in text: fail(f"missing section {s} {name}")
    fm = parse_frontmatter(text)
    if fm.get("type") != "institution": fail(f"type {name}")
    if fm.get("sub_type") != "design_school" and name in {"fuzhou-mawei-chuanzheng-xuetang-huishiyuan.md", "jiangnan-chuanzhengju-gongyi-xuetang.md", "beiping-guoli-yizhuan.md", "hangzhou-guoli-yizhuan.md", "qinggongbu-qinggong-xueyuan.md"}:
        fail(f"sub_type {name}")
    if fm.get("source_count") != str(ncitation): fail(f"source_count {name} = {fm.get('source_count')}")
    if citations(text) != ncitation: fail(f"citation count {name} = {citations(text)}")
    if fm.get("version") != "1": fail(f"version {name}")
    if fm.get("evidence_status") != "source_backed": fail(f"evidence_status {name}")
    if fm.get("primary_dimension") not in {"A", "B", "C", "D", "E"}: fail(f"dimension {name}")
    if fm.get("confidence") != "medium": fail(f"confidence {name}")
    if fm.get("consensus") != "tentative": fail(f"consensus {name}")
    if name != "hangzhou-guoli-yizhuan.md" and DOC not in text: fail(f"doc_id missing {name}")
    for needle in needles:
        if needle not in text: fail(f"{name} missing {needle}")

# index idempotence
before = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
after = subprocess.check_output(["python", "scripts/build_discovery_index.py"], cwd=ROOT)
if before != after: fail("index rebuild not idempotent")
idx = json.loads(after)
if idx["by_state"] != {"applied": 887, "needs_evidence": 3588, "no_delta": 56, "rejected": 808}:
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
