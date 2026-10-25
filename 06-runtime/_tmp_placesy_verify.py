import hashlib
import json
import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-xiayanjing2009-places-batch-y"
DOC = "2009-xiayanjing-zhongguo-shejishi"
DATE = "2026-10-25"
TARGETS = {
    "04-knowledge/units/places/sanxingdui.md": {"action": "update", "sources": 3, "version": 2},
    "04-knowledge/units/places/zhenghan-gucheng-taofang-yizhi.md": {"action": "create", "sources": 1, "version": 1},
    "04-knowledge/units/places/sanshan-wuyuan.md": {"action": "create", "sources": 1, "version": 1},
}
SECTIONS = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
TITLE_RE = re.compile(r'[一-鿿].*[（(][^（）)]*[A-Za-zÀ-ÿ][^（）)]*[）)]')
errors = []


def check(cond, message):
    if not cond:
        errors.append(message)


def fp(path):
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {"sha256": "sha256:" + hashlib.sha256(data).hexdigest(), "bytes": len(data), "lines": text.count("\n")}


def parse(path):
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    return text, yaml.safe_load(text[4:end]), text[end + 5:]


ledger = [json.loads(l) for l in (PKG / "candidate-decision-ledger.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
check(len(ledger) == 9, f"ledger rows {len(ledger)} != 9")
by = {}
for row in ledger:
    by.setdefault(row["candidate_id"], []).append(row)
check(len(by) == 3, f"candidates {len(by)} != 3")
for cid, rows in by.items():
    check(len(rows) == 3, f"{cid}: {len(rows)} rows")
    check([r["state"] for r in rows] == ["ready_for_review", "approved", "applied"], f"{cid}: states")
    check([r["expected_state"] for r in rows] == ["needs_evidence", "ready_for_review", "approved"], f"{cid}: expected")
    check(rows[-1].get("target_ref") in TARGETS, f"{cid}: target_ref")
    for r in rows:
        check(r["updated_at"] == DATE and r["decision"]["decided_at"] == DATE and r["decision"]["decided_by"] == "Agent", f"{cid}: metadata")

plan = [json.loads(l) for l in (PKG / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
check(len(plan) == 3, f"plan rows {len(plan)} != 3")
check({r["target_ref"] for r in plan} == set(TARGETS), "plan target set")
check(sum(1 for r in plan if r["action"] == "create") == 2, "create count")
check(sum(1 for r in plan if r["action"] == "update") == 1, "update count")
for row in plan:
    ref = row["target_ref"]
    exp = TARGETS[ref]
    check(row["action"] == exp["action"], f"{ref}: action")
    if exp["action"] == "update":
        check(isinstance(row.get("before"), dict), f"{ref}: before missing")
    else:
        check(row.get("before") is None, f"{ref}: before not null")
    actual = fp(ROOT / ref)
    check(row["after_sha256"] == actual["sha256"], f"{ref}: sha")
    check(row["bytes"] == actual["bytes"] and row["lines"] == actual["lines"], f"{ref}: size")

mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
check(len(mapping) == 3, f"mapping {len(mapping)} != 3")
check({m["target_ref"] for m in mapping} == set(TARGETS), "mapping targets")
check(all(m["merged_candidates"] == [] for m in mapping), "mapping merged")

for ref, exp in TARGETS.items():
    text, front, body = parse(ROOT / ref)
    check(front.get("type") == "place", f"{ref}: type")
    check(front.get("sub_type") in {"archaeological_site", "garden", "kiln_site", "city"}, f"{ref}: sub_type {front.get('sub_type')}")
    check(front.get("source_count") == exp["sources"] == len(front.get("sources") or []), f"{ref}: source count")
    check(front.get("version") == exp["version"], f"{ref}: version")
    check(str(front.get("created")) == DATE and str(front.get("updated")) == DATE, f"{ref}: dates")
    check(front.get("evidence_status") == "source_backed" and front.get("consensus") == "tentative", f"{ref}: evidence/consensus")
    check(TITLE_RE.search(front.get("title", "")), f"{ref}: title")
    h2 = [line.strip() for line in body.splitlines() if line.startswith("## ")]
    check(h2 == SECTIONS, f"{ref}: H2 {h2}")

sx = (ROOT / "04-knowledge/units/places/sanxingdui.md").read_text(encoding="utf-8")
for phrase in ["皮、革、丝、麻", "提花几何纹的锦、绮", "奴隶主和贵族以穿着此种材质为荣", "2009"]:
    check(phrase in sx, f"sanxingdui missing {phrase!r}")

proc = subprocess.run([sys.executable, "scripts/build_discovery_index.py"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
check(proc.returncode == 0, f"index build failed: {proc.stderr[-500:]}")
index_path = ROOT / "06-runtime" / "state" / "candidate-index.jsonl"
index = [json.loads(l) for l in index_path.read_text(encoding="utf-8").splitlines() if l.strip()]
check(len(index) == 5339, f"index rows {len(index)}")
counts = {}
for r in index:
    counts[r["state"]] = counts.get(r["state"], 0) + 1
check(counts == {"applied": 933, "needs_evidence": 3537, "no_delta": 57, "rejected": 812}, f"counts {counts}")
by_id = {r["candidate_id"]: r for r in index}
for cid, rows in by.items():
    check(by_id[cid]["state"] == "applied", f"{cid}: index state")
    check(by_id[cid].get("target_ref") == rows[-1]["target_ref"], f"{cid}: index target")

print(json.dumps({
    "ok": not errors,
    "errors": errors,
    "ledger_rows": len(ledger),
    "plan_rows": len(plan),
    "mapping_entries": len(mapping),
    "index_rows": len(index),
    "index_sha256": fp(index_path)["sha256"],
    "counts": counts,
}, ensure_ascii=False, indent=2))
raise SystemExit(0 if not errors else 1)
