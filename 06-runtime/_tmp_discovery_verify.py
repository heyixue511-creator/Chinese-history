# -*- coding: utf-8 -*-
"""Cross-check the discovery-events batch against disk and the rebuilt index."""
import hashlib
import json
from pathlib import Path

WP = Path("06-runtime/automation/2026-10-25-discovery-events-batch")
errors = []

ledger = [json.loads(l) for l in (WP / "candidate-decision-ledger.jsonl").read_text(encoding="utf-8").splitlines() if l]
plan = [json.loads(l) for l in (WP / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines() if l]
mapping = json.loads((WP / "canonical-mapping.json").read_text(encoding="utf-8"))
index = {}
for line in Path("06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        row = json.loads(line)
        index[row["candidate_id"]] = row

if len(ledger) != 21:
    errors.append(f"ledger rows {len(ledger)} != 21")
by_cid = {}
for row in ledger:
    by_cid.setdefault(row["candidate_id"], []).append(row)
if len(by_cid) != 7:
    errors.append(f"ledger candidates {len(by_cid)} != 7")
for cid, rows in by_cid.items():
    if len(rows) != 3:
        errors.append(f"{cid}: {len(rows)} rows")
        continue
    if [r["state"] for r in rows[:2]] != ["ready_for_review", "approved"]:
        errors.append(f"{cid}: state sequence {[r['state'] for r in rows]}")
    if [r["expected_state"] for r in rows] != ["needs_evidence", "ready_for_review", "approved"]:
        errors.append(f"{cid}: expected_state sequence")
    final = rows[2]["state"]
    if final not in ("applied", "no_delta"):
        errors.append(f"{cid}: final {final}")
    target = rows[2].get("target_ref")
    idx = index.get(cid)
    if idx is None:
        errors.append(f"{cid}: missing from index")
    else:
        if idx.get("state") != final:
            errors.append(f"{cid}: index state {idx.get('state')} != ledger {final}")
        if idx.get("target_ref") != target:
            errors.append(f"{cid}: index target {idx.get('target_ref')} != ledger {target}")

if len(plan) != 6:
    errors.append(f"apply-plan rows {len(plan)} != 6")
for row in plan:
    path = Path(row["target_ref"])
    if row["action"] != "create":
        errors.append(f"{row['target_ref']}: action {row['action']}")
    if row["before"] is not None:
        errors.append(f"{row['target_ref']}: before not null")
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    sha = "sha256:" + hashlib.sha256(payload).hexdigest()
    if sha != row["after_sha256"]:
        errors.append(f"{row['target_ref']}: sha mismatch")
    if len(payload) != row["bytes"]:
        errors.append(f"{row['target_ref']}: bytes mismatch")
    if text.count("\n") != row["lines"]:
        errors.append(f"{row['target_ref']}: lines mismatch")

if len(mapping) != 7:
    errors.append(f"mapping entries {len(mapping)} != 7")
actions = {}
for item in mapping:
    actions[item["action"]] = actions.get(item["action"], 0) + 1
    if not Path(item["target_ref"]).exists():
        errors.append(f"mapping target missing {item['target_ref']}")
if actions != {"create": 6, "no_delta": 1}:
    errors.append(f"mapping actions {actions}")

plan_candidates = {r["candidate_id"] for r in plan}
map_candidates = {m["canonical_candidate"] for m in mapping}
if plan_candidates | {m["canonical_candidate"] for m in mapping if m["action"] == "no_delta"} != set(by_cid):
    errors.append("candidate sets differ")

print("errors", len(errors))
for e in errors:
    print(" -", e)

sha = "sha256:" + hashlib.sha256(Path("06-runtime/state/candidate-index.jsonl").read_bytes()).hexdigest()
print("index_sha256", sha)
print("index_rows", len(index))
