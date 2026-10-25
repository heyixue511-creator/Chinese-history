import hashlib
import json
import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2011lilixin-places-batch-z"
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
DATE = "2026-10-25"
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
check(len(ledger) == 75, f"ledger rows {len(ledger)} != 75")
by = {}
for row in ledger:
    by.setdefault(row["candidate_id"], []).append(row)
check(len(by) == 25, f"candidates {len(by)} != 25")
applied = {cid for cid, rows in by.items() if rows[-1]["state"] == "applied"}
no_delta = {cid for cid, rows in by.items() if rows[-1]["state"] == "no_delta"}
check(len(applied) == 24, f"applied {len(applied)}")
check(no_delta == {f"{DOC}:cand-05-08"}, f"no_delta {no_delta}")
for cid, rows in by.items():
    check(len(rows) == 3, f"{cid}: {len(rows)} rows")
    expect_states = ["ready_for_review", "approved", "no_delta"] if cid in no_delta else ["ready_for_review", "approved", "applied"]
    check([r["state"] for r in rows] == expect_states, f"{cid}: states")
    check([r["expected_state"] for r in rows] == ["needs_evidence", "ready_for_review", "approved"], f"{cid}: expected")
    check(rows[0].get("target_ref") is None and rows[1].get("target_ref") is None, f"{cid}: early target_ref")
    check(bool(rows[-1].get("target_ref")), f"{cid}: terminal target_ref")
    for r in rows:
        check(r["updated_at"] == DATE and r["decision"]["decided_at"] == DATE and r["decision"]["decided_by"] == "Agent", f"{cid}: metadata")

plan = [json.loads(l) for l in (PKG / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
check(len(plan) == 24, f"plan rows {len(plan)} != 24")
check(sum(1 for r in plan if r["action"] == "create") == 21, "create count")
check(sum(1 for r in plan if r["action"] == "update") == 3, "update count")
targets = {r["target_ref"] for r in plan}
check(len(targets) == 24, f"unique targets {len(targets)}")
check({r["candidate_id"] for r in plan} == applied, "plan candidates != applied set")
for row in plan:
    ref = row["target_ref"]
    if row["action"] == "update":
        check(isinstance(row.get("before"), dict), f"{ref}: before missing")
    else:
        check(row.get("before") is None, f"{ref}: before not null")
    actual = fp(ROOT / ref)
    check(row["after_sha256"] == actual["sha256"], f"{ref}: sha")
    check(row["bytes"] == actual["bytes"] and row["lines"] == actual["lines"], f"{ref}: size")

mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
check(len(mapping) == 24, f"mapping {len(mapping)} != 24")
check({m["target_ref"] for m in mapping} == targets, "mapping targets")
check({m["canonical_candidate"] for m in mapping} == applied, "mapping canonical set")
for m in mapping:
    if m["target_ref"] == "04-knowledge/units/places/famen-si-digong.md":
        check(m["merged_candidates"] == [f"{DOC}:cand-05-08"], "famen merged")
    else:
        check(m["merged_candidates"] == [], f"{m['target_ref']}: merged not empty")

for row in plan:
    ref = row["target_ref"]
    text, front, body = parse(ROOT / ref)
    check(front.get("type") == "place", f"{ref}: type")
    check(front.get("sub_type") in {"archaeological_site", "garden", "geographical_region", "city"}, f"{ref}: sub_type {front.get('sub_type')}")
    check(front.get("source_count") == len(front.get("sources") or []), f"{ref}: source count")
    check(str(front.get("created")) == DATE and str(front.get("updated")) == DATE, f"{ref}: dates")
    check(front.get("evidence_status") == "source_backed" and front.get("consensus") == "tentative", f"{ref}: evidence/consensus")
    check(TITLE_RE.search(front.get("title", "")), f"{ref}: title")
    h2 = [line.strip() for line in body.splitlines() if line.startswith("## ")]
    check(h2 == SECTIONS, f"{ref}: H2 {h2}")

update_expectations = {
    "04-knowledge/units/places/daxing-cheng.md": ["唐长安城", "明德门", "100多个", "规模最大"],
    "04-knowledge/units/places/fuhao-tomb.md": ["755件", "刮摩治玉", "426件"],
    "04-knowledge/units/places/mawangdui-hanmu.md": ["耳杯七只", "六只顺扣", "三角形", "竹箸"],
}
for ref, phrases in update_expectations.items():
    text = (ROOT / ref).read_text(encoding="utf-8")
    for phrase in phrases:
        check(phrase in text, f"{ref} missing {phrase!r}")
    _, front, _ = parse(ROOT / ref)
    check(front.get("version") == 2 and front.get("source_count") == 3, f"{ref}: update version/source")

place_files = list((ROOT / "04-knowledge" / "units" / "places").glob("*.md"))
check(len(place_files) == 62, f"place file count {len(place_files)} != 62")

proc = subprocess.run([sys.executable, "scripts/build_discovery_index.py"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
check(proc.returncode == 0, f"index build failed: {proc.stderr[-500:]}")
index_path = ROOT / "06-runtime" / "state" / "candidate-index.jsonl"
index = [json.loads(l) for l in index_path.read_text(encoding="utf-8").splitlines() if l.strip()]
check(len(index) == 5339, f"index rows {len(index)}")
counts = {}
for r in index:
    counts[r["state"]] = counts.get(r["state"], 0) + 1
check(counts == {"applied": 957, "needs_evidence": 3512, "no_delta": 58, "rejected": 812}, f"counts {counts}")
by_id = {r["candidate_id"]: r for r in index}
for cid, rows in by.items():
    check(by_id[cid]["state"] == rows[-1]["state"], f"{cid}: index state")
    check(by_id[cid].get("target_ref") == rows[-1]["target_ref"], f"{cid}: index target")

print(json.dumps({
    "ok": not errors,
    "errors": errors,
    "ledger_rows": len(ledger),
    "plan_rows": len(plan),
    "mapping_entries": len(mapping),
    "place_files": len(place_files),
    "index_rows": len(index),
    "index_sha256": fp(index_path)["sha256"],
    "counts": counts,
}, ensure_ascii=False, indent=2))
raise SystemExit(0 if not errors else 1)
