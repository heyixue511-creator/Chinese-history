# -*- coding: utf-8 -*-
"""Verify the Gaofeng 2004 procedure batch against ledger, plan, mapping, KU files and index."""
import hashlib
import json
from pathlib import Path

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009xiayanjing-procedures-batch-2")
PREFIX = "2009-xiayanjing-zhongguo-shejishi:"
errors = []
checks = {}


def read_jsonl(path):
    rows = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                errors.append(f"{path.name}:{lineno} {exc}")
    return rows


def fp(path):
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


ledger = read_jsonl(BATCH / "candidate-decision-ledger.jsonl")
plan = read_jsonl(BATCH / "apply-plan.jsonl")
mapping = json.loads((BATCH / "canonical-mapping.json").read_text(encoding="utf-8"))

checks["ledger_rows"] = len(ledger)
checks["plan_rows"] = len(plan)
checks["mapping_rows"] = len(mapping)
if len(ledger) != 21:
    errors.append(f"ledger rows {len(ledger)} != 21")
if len(plan) != 7:
    errors.append(f"plan rows {len(plan)} != 5")
if len(mapping) != 7:
    errors.append(f"mapping rows {len(mapping)} != 5")

# Ledger chain: every candidate has needs_evidence -> ready_for_review -> approved -> applied, a single terminal row.
by_cand = {}
for row in ledger:
    if not row.get("candidate_id", "").startswith(PREFIX):
        errors.append(f"ledger candidate prefix {row.get('candidate_id')}")
    by_cand.setdefault(row["candidate_id"], []).append(row)

final_rows = {}
for cid, rows in by_cand.items():
    states = [r["state"] for r in rows]
    if states != ["ready_for_review", "approved", "applied"]:
        errors.append(f"{cid} chain {states}")
        continue
    for expected, row in zip(["needs_evidence", "ready_for_review", "approved"], rows):
        if row.get("expected_state") != expected:
            errors.append(f"{cid} expected_state {row.get('expected_state')} at {expected}")
        if row.get("decision", {}).get("decided_by") != "Agent":
            errors.append(f"{cid} decided_by")
        if row.get("decision", {}).get("decided_at") != "2026-10-25":
            errors.append(f"{cid} decided_at")
    if "target_ref" not in rows[-1]:
        errors.append(f"{cid} terminal target_ref missing")
    for row in rows[:-1]:
        if "target_ref" in row:
            errors.append(f"{cid} non-terminal target_ref present")
    final_rows[cid] = rows[-1]

checks["candidates"] = len(by_cand)
checks["terminal_applied"] = len(final_rows)

# apply-plan: create targets exist with matching fingerprint and null before; update carries before object.
plan_by_cand = {}
for row in plan:
    cid = row["candidate_id"]
    plan_by_cand[cid] = row
    target = ROOT / row["target_ref"]
    if not target.exists():
        errors.append(f"plan target missing {row['target_ref']}")
        continue
    actual = fp(target)
    for key in ("sha256", "bytes", "lines"):
        got = actual["sha256"] if key == "sha256" else actual[key]
        want = row["after_sha256"] if key == "sha256" else row[key]
        if got != want:
            errors.append(f"{row['target_ref']} {key} {got} != {want}")
    if row["action"] == "create":
        if row["before"] is not None:
            errors.append(f"{cid} create before not null")
        if not row["target_ref"].startswith("04-knowledge/units/procedures/"):
            errors.append(f"{cid} create not in procedures")
    elif row["action"] == "update":
        before = row["before"]
        if not isinstance(before, dict) or not before.get("sha256", "").startswith("sha256:"):
            errors.append(f"{cid} update before malformed")
        if before["sha256"] == row["after_sha256"]:
            errors.append(f"{cid} update fingerprint unchanged")
    else:
        errors.append(f"{cid} unknown action {row['action']}")
    if final_rows.get(cid, {}).get("target_ref") != row["target_ref"]:
        errors.append(f"{cid} ledger/plan target mismatch")

checks["plan_create"] = sum(1 for r in plan if r["action"] == "create")
checks["plan_update"] = sum(1 for r in plan if r["action"] == "update")
if checks["plan_create"] != 6:
    errors.append(f"create count {checks['plan_create']} != 6")
if checks["plan_update"] != 1:
    errors.append(f"update count {checks['plan_update']} != 1")

# Mapping set covers exactly the plan candidates.
mapped = {m["canonical_candidate"] for m in mapping}
if mapped != set(plan_by_cand):
    errors.append(f"mapping set mismatch {sorted(mapped)} vs {sorted(plan_by_cand)}")
for m in mapping:
    row = plan_by_cand.get(m["canonical_candidate"])
    if row and row["target_ref"] != m["target_ref"]:
        errors.append(f"{m['canonical_candidate']} mapping target mismatch")
    if row and row["action"] != m["action"]:
        errors.append(f"{m['canonical_candidate']} mapping action mismatch")

# KU structure: YAML frontmatter, six sections, source_count matches sources, references count.
def check_ku(path: Path):
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        errors.append(f"{path.name} no frontmatter")
        return
    fm_block, body = text.split("---\n", 2)[1], text.split("---\n", 2)[2]
    fm = {}
    for ln in fm_block.splitlines():
        if ln.startswith("source_count:"):
            fm["source_count"] = int(ln.split(":", 1)[1].strip())
        if ln.startswith("type:"):
            fm["type"] = ln.split(":", 1)[1].strip()
        if ln.startswith("sub_type:"):
            fm["sub_type"] = ln.split(":", 1)[1].strip()
    src = fm_block.count("  - citation:")
    if fm.get("source_count") != src:
        errors.append(f"{path.name} source_count {fm.get('source_count')} != {src}")
    if fm.get("type") != "procedure":
        errors.append(f"{path.name} type {fm.get('type')}")
    for heading in ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]:
        if heading not in body:
            errors.append(f"{path.name} missing {heading}")
    refs = sum(1 for ln in body.splitlines() if ln[:1].isdigit() and ". " in ln[:4])
    if refs != src:
        errors.append(f"{path.name} references {refs} != sources {src}")
    return fm


for row in plan:
    check_ku(ROOT / row["target_ref"])

# Candidate index: every candidate applied with matching target_ref.
index = {}
for row in read_jsonl(ROOT / "06-runtime/state/candidate-index.jsonl"):
    if row.get("candidate_id", "").startswith(PREFIX):
        index[row["candidate_id"]] = row

missing = sorted(set(by_cand) - set(index))
if missing:
    errors.append(f"index missing {missing}")
for cid in sorted(by_cand):
    row = index.get(cid)
    if not row:
        continue
    if row.get("state") != "applied":
        errors.append(f"{cid} index state {row.get('state')}")
    if row.get("target_ref") != plan_by_cand[cid]["target_ref"]:
        errors.append(f"{cid} index target_ref {row.get('target_ref')}")
    if row.get("lifecycle_class") != "terminal":
        errors.append(f"{cid} index lifecycle {row.get('lifecycle_class')}")

checks["index_applied"] = sum(1 for cid in by_cand if index.get(cid, {}).get("state") == "applied")
checks["index_candidates"] = len(index)
if checks["index_applied"] != 7:
    errors.append(f"index applied {checks['index_applied']} != 7")

checks["errors"] = len(errors)
report = {"checks": checks, "errors": errors}
print(json.dumps(report, ensure_ascii=False, indent=2))
