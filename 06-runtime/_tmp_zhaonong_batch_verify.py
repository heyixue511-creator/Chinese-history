# -*- coding: utf-8 -*-
"""Verify Zhaonong event batch artifacts against disk and candidate index."""
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_zhaonong_events_a import ITEMS_A
from _tmp_zhaonong_events_b import ITEMS_B
from _tmp_zhaonong_events_c import ITEMS_C

WP = Path("06-runtime/automation/2026-10-25-2009zhaonong-events-batch")
PREFIX = "2009-zhaonong-zhongguo-yishu-shejishi:"
INDEX = Path("06-runtime/state/candidate-index.jsonl")
ITEMS = ITEMS_A + ITEMS_B + ITEMS_C
errors = []


def fingerprint(path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {"sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
            "bytes": len(payload), "lines": text.count("\n")}


ledger = [json.loads(l) for l in (WP / "candidate-decision-ledger.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
plan = [json.loads(l) for l in (WP / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
mapping = json.loads((WP / "canonical-mapping.json").read_text(encoding="utf-8"))
if len(ledger) != 69:
    errors.append(f"ledger rows {len(ledger)} != 69")
by_cand = defaultdict(list)
for row in ledger:
    by_cand[row["candidate_id"]].append(row)
if len(by_cand) != 23:
    errors.append(f"ledger candidates {len(by_cand)} != 23")
for cid, rows in by_cand.items():
    if len(rows) != 3:
        errors.append(f"{cid}: {len(rows)} rows")
        continue
    if [r["expected_state"] for r in rows] != ["needs_evidence", "ready_for_review", "approved"]:
        errors.append(f"{cid}: expected_state chain")
    if rows[-1]["state"] not in {"applied", "no_delta"}:
        errors.append(f"{cid}: final {rows[-1]['state']}")
    if "target_ref" not in rows[-1]:
        errors.append(f"{cid}: no target_ref")
final_counts = Counter(rows[-1]["state"] for rows in by_cand.values())
if final_counts != Counter({"applied": 20, "no_delta": 3}):
    errors.append(f"final counts {dict(final_counts)}")
if len(plan) != 20:
    errors.append(f"plan rows {len(plan)} != 20")
for row in plan:
    if row["action"] != "create" or row["before"] is not None:
        errors.append(f"plan action/before {row['candidate_id']}")
        continue
    fp = fingerprint(Path(row["target_ref"]))
    if (fp["sha256"], fp["bytes"], fp["lines"]) != (row["after_sha256"], row["bytes"], row["lines"]):
        errors.append(f"plan fingerprint mismatch {row['target_ref']}")
if len(mapping) != 23:
    errors.append(f"mapping entries {len(mapping)} != 23")
if {m["canonical_candidate"] for m in mapping} != {c for c in by_cand}:
    errors.append("mapping candidate set mismatch")
plan_targets = {r["target_ref"] for r in plan}
ledger_targets = {rows[-1]["target_ref"] for rows in by_cand.values() if rows[-1]["state"] == "applied"}
if plan_targets != ledger_targets:
    errors.append("plan/ledger applied target set mismatch")

for item in ITEMS:
    path = Path("04-knowledge/units/events") / f"{item['slug']}.md"
    if not path.exists():
        errors.append(f"missing KU {path}")
        continue
    text = path.read_text(encoding="utf-8")
    data = yaml.safe_load(text.split("---\n", 2)[1])
    if data.get("type") != "event" or data.get("primary_dimension") != item["dim"]:
        errors.append(f"frontmatter {path}")
    if data["sources"][0]["evidence_ref"]["doc_id"] != "2009-zhaonong-zhongguo-yishu-shejishi":
        errors.append(f"doc_id {path}")
    for section in ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]:
        if section not in text:
            errors.append(f"section {path}: {section}")

index_rows = [json.loads(l) for l in INDEX.read_text(encoding="utf-8").splitlines() if l.strip()]
by_index = {r["candidate_id"]: r for r in index_rows}
for cid, rows in by_cand.items():
    final = rows[-1]
    row = by_index[cid]
    if row["state"] != final["state"]:
        errors.append(f"index state {cid}: {row['state']} != {final['state']}")
    if row.get("target_ref") != final.get("target_ref"):
        errors.append(f"index target_ref {cid}")

print("errors", len(errors))
for e in errors[:40]:
    print(" -", e)
print("ledger_rows", len(ledger), "candidates", len(by_cand), "final", dict(final_counts))
print("plan_rows", len(plan), "mapping", len(mapping), "units", len(ITEMS))
print("index_sha256", fingerprint(INDEX)["sha256"], "index_rows", len(index_rows))
