# -*- coding: utf-8 -*-
"""Verify Tianzibing 2010 event batch artifacts against disk and candidate index."""
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_tianzibing_events_items import ITEMS_TZ

WP = Path("06-runtime/automation/2026-10-25-2010tianzibing-events-batch")
PREFIX = "2010-tianzibing-zhongguo-gongyi-meishushi:"
INDEX = Path("06-runtime/state/candidate-index.jsonl")
BEFORE = json.loads((Path(__file__).parent / "_tmp_tianzibing_before.json").read_text(encoding="utf-8"))
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SECTIONS = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
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
if len(ledger) != 66:
    errors.append(f"ledger rows {len(ledger)} != 66")
by_cand = defaultdict(list)
for row in ledger:
    by_cand[row["candidate_id"]].append(row)
if len(by_cand) != 22:
    errors.append(f"ledger candidates {len(by_cand)} != 22")
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
if final_counts != Counter({"applied": 20, "no_delta": 2}):
    errors.append(f"final counts {dict(final_counts)}")
if len(plan) != 20:
    errors.append(f"plan rows {len(plan)} != 20")
if Counter(r["action"] for r in plan) != Counter({"create": 12, "update": 8}):
    errors.append("plan action counts")

for row in plan:
    fp = fingerprint(Path(row["target_ref"]))
    if fp["bytes"] != row["bytes"] or fp["lines"] != row["lines"]:
        errors.append(f"plan size mismatch {row['target_ref']}")
    if fp["sha256"] != row["after_sha256"]:
        errors.append(f"plan after_sha mismatch {row['target_ref']}")
    if row["action"] == "create":
        if row["before"] is not None:
            errors.append(f"create before not null {row['target_ref']}")
    else:
        slug = row["target_ref"].rsplit("/", 1)[1][:-3]
        if row["before"] != BEFORE.get(slug):
            errors.append(f"update before mismatch {row['target_ref']}")

if len(mapping) != 22:
    errors.append(f"mapping entries {len(mapping)} != 22")
if {m["canonical_candidate"] for m in mapping} != {c for c in by_cand}:
    errors.append("mapping candidate set mismatch")
plan_targets = {r["target_ref"] for r in plan}
ledger_targets = {rows[-1]["target_ref"] for rows in by_cand.values() if rows[-1]["state"] == "applied"}
if plan_targets != ledger_targets:
    errors.append("plan/ledger applied target set mismatch")

for item in ITEMS_TZ:
    path = Path("04-knowledge/units/events") / f"{item['slug']}.md"
    if not path.exists():
        errors.append(f"missing KU {path}")
        continue
    text = path.read_text(encoding="utf-8")
    data = yaml.safe_load(text.split("---\n", 2)[1])
    if data.get("type") != "event" or data.get("primary_dimension") != item["dim"]:
        errors.append(f"frontmatter {path}")
    if data["sources"][0]["evidence_ref"]["doc_id"] != DOC:
        errors.append(f"doc_id {path}")
    if data.get("source_count") != 1:
        errors.append(f"create source_count {path}")
    for section in SECTIONS:
        if section not in text:
            errors.append(f"section {path}: {section}")

for row in plan:
    if row["action"] != "update":
        continue
    text = Path(row["target_ref"]).read_text(encoding="utf-8")
    data = yaml.safe_load(text.split("---\n", 2)[1])
    doc_ids = [s["evidence_ref"]["doc_id"] for s in data["sources"]]
    if DOC not in doc_ids:
        errors.append(f"update missing tianzibing source {row['target_ref']}")
    if data.get("source_count") != len(data["sources"]):
        errors.append(f"update source_count {row['target_ref']}")
    n_ref = len(re.findall(r"^\d+\. ", text.split("## 参考文献", 1)[1], re.M))
    if n_ref != len(data["sources"]):
        errors.append(f"update refs {row['target_ref']}")
    for section in SECTIONS:
        if section not in text:
            errors.append(f"update section {row['target_ref']}: {section}")

for nd in [rows[-1] for rows in by_cand.values() if rows[-1]["state"] == "no_delta"]:
    if not Path(nd["target_ref"]).exists():
        errors.append(f"no_delta target missing {nd['target_ref']}")

index_rows = [json.loads(l) for l in INDEX.read_text(encoding="utf-8").splitlines() if l.strip()]
by_index = {r["candidate_id"]: r for r in index_rows}
for cid, rows in by_cand.items():
    final = rows[-1]
    row = by_index.get(cid)
    if row is None:
        errors.append(f"index missing {cid}")
        continue
    if row["state"] != final["state"]:
        errors.append(f"index state {cid}: {row['state']} != {final['state']}")
    if row.get("target_ref") != final.get("target_ref"):
        errors.append(f"index target_ref {cid}")

print("errors", len(errors))
for e in errors[:40]:
    print(" -", e)
print("ledger_rows", len(ledger), "candidates", len(by_cand), "final", dict(final_counts))
print("plan_rows", len(plan), "mapping", len(mapping), "units", len(ITEMS_TZ))
print("index_sha256", fingerprint(INDEX)["sha256"], "index_rows", len(index_rows))
print("state", dict(Counter(r["state"] for r in index_rows)))
