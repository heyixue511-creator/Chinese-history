# -*- coding: utf-8 -*-
"""Verify overlap batch artifacts against disk and the pre-batch candidate index."""
import json
from collections import Counter, defaultdict
from pathlib import Path

WP = Path("06-runtime/automation/2026-10-25-overlap-candidates-batch")


def fp(path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    import hashlib

    return {
        "sha256": "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "bytes": len(text.encode("utf-8")),
        "lines": text.count("\n"),
    }


def load_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


ledger = load_jsonl(WP / "candidate-decision-ledger.jsonl")
plan = load_jsonl(WP / "apply-plan.jsonl")
mapping = json.loads((WP / "canonical-mapping.json").read_text(encoding="utf-8"))
index = load_jsonl(Path("06-runtime/state/candidate-index.jsonl"))

errors = []

# 1. ledger shape
by_cid = defaultdict(list)
for row in ledger:
    by_cid[row["candidate_id"]].append(row)
if len(ledger) != 159 or len(by_cid) != 53:
    errors.append(f"ledger shape {len(ledger)} rows / {len(by_cid)} candidates")
seq = ["ready_for_review", "approved"]
for cid, rows in by_cid.items():
    if [r["state"] for r in rows[:2]] != seq or len(rows) != 3:
        errors.append(f"{cid} state sequence {[r['state'] for r in rows]}")
    if rows[0]["expected_state"] != "needs_evidence" or rows[1]["expected_state"] != "ready_for_review" or rows[2]["expected_state"] != "approved":
        errors.append(f"{cid} expected_state mismatch")
    if rows[2]["state"] not in ("applied", "no_delta"):
        errors.append(f"{cid} final state {rows[2]['state']}")
final = Counter(rows[2]["state"] for rows in by_cid.values())
if final != {"applied": 42, "no_delta": 11}:
    errors.append(f"final states {dict(final)}")

# 2. every candidate's current index state matches the ledger final state
idx_state = {row["candidate_id"]: row for row in index}
for cid, rows in by_cid.items():
    row = idx_state.get(cid)
    if row is None:
        errors.append(f"{cid} missing from index")
        continue
    if row["state"] != rows[2]["state"]:
        errors.append(f"{cid} index state {row['state']} vs ledger {rows[2]['state']}")
    if row.get("target_ref") != rows[2].get("target_ref"):
        errors.append(f"{cid} target_ref {row.get('target_ref')!r} vs {rows[2].get('target_ref')!r}")

# 3. apply-plan fingerprints
if len(plan) != 40:
    errors.append(f"apply-plan rows {len(plan)}")
for row in plan:
    path = Path(row["target_ref"])
    if not path.exists():
        errors.append(f"{row['target_ref']} missing")
        continue
    now = fp(path)
    if (row["after_sha256"], row["bytes"], row["lines"]) != (now["sha256"], now["bytes"], now["lines"]):
        errors.append(f"{row['target_ref']} after mismatch")
    if row["action"] == "update" and row["before"] == now:
        errors.append(f"{row['target_ref']} unchanged despite update")
    if row["action"] == "create" and row["before"] is not None:
        errors.append(f"{row['target_ref']} create before not null")

# 4. mapping
if len(mapping) != 50:
    errors.append(f"mapping entries {len(mapping)}")
refs = Counter(m["target_ref"] for m in mapping)
dupes = {k: v for k, v in refs.items() if v > 1}
if dupes:
    errors.append(f"mapping target_ref duplicated: {dupes}")
actions = Counter(m["action"] for m in mapping)
if actions != {"update": 39, "create": 1, "no_delta": 10}:
    errors.append(f"mapping actions {dict(actions)}")
all_mapped = {m["canonical_candidate"] for m in mapping} | {c for m in mapping for c in m["merged_candidates"]}
if all_mapped != set(by_cid):
    errors.append(f"mapping candidates {len(all_mapped)} vs ledger {len(by_cid)}")

print("ledger rows", len(ledger), "candidates", len(by_cid), dict(final))
print("apply-plan", len(plan), dict(Counter(r["action"] for r in plan)))
print("mapping", len(mapping), dict(actions))
print("errors", len(errors))
for e in errors:
    print(" -", e)
