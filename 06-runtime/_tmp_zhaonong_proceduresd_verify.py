# -*- coding: utf-8 -*-
"""Verify Zhaonong 2009 procedure batch D artifacts against disk and candidate index."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-d")
INDEX = Path("06-runtime/state/candidate-index.jsonl")
PREFIX = "2009-zhaonong-zhongguo-yishu-shejishi:"
PRE = {
    "04-knowledge/units/procedures/huozi-yinshua.md": Path("06-runtime/_tmp_pre_d_huozi-yinshua.md"),
    "04-knowledge/units/procedures/duanban-taoyin.md": Path("06-runtime/_tmp_pre_d_duanban-taoyin.md"),
}
SECTIONS = [
    "## 描述",
    "## 核心内容",
    "## 在层级体系中的位置",
    "## 相关知识元",
    "## 验证状态",
    "## 参考文献",
]
EXPECTED_SOURCES = {
    "04-knowledge/units/procedures/duanban-taoyin.md": 2,
}

errors = []


def fingerprint(path: Path):
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        errors.append(f"BOM {path}")
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


ledger = [json.loads(line) for line in (BATCH / "candidate-decision-ledger.jsonl").read_text(encoding="utf-8").splitlines() if line]
plan = [json.loads(line) for line in (BATCH / "apply-plan.jsonl").read_text(encoding="utf-8").splitlines() if line]
mapping = json.loads((BATCH / "canonical-mapping.json").read_text(encoding="utf-8"))
manifest = json.loads((BATCH / "manifest.json").read_text(encoding="utf-8"))

if len(ledger) != 42:
    errors.append(f"ledger rows {len(ledger)} != 42")
if len(plan) != 14:
    errors.append(f"plan rows {len(plan)} != 14")
if len(mapping) != 14:
    errors.append(f"mapping rows {len(mapping)} != 14")

by_candidate = {}
for row in ledger:
    by_candidate.setdefault(row["candidate_id"], []).append(row)
    if row["decision"]["decided_by"] != "Agent":
        errors.append(f"decided_by {row['candidate_id']}")
    if row["decision"]["decided_at"] != "2026-10-25":
        errors.append(f"decided_at {row['candidate_id']}")

terminal_applied = 0
for cid, rows in by_candidate.items():
    if len(rows) != 3:
        errors.append(f"{cid} ledger rows {len(rows)} != 3")
        continue
    states = [r["state"] for r in rows]
    if states != ["ready_for_review", "approved", "applied"]:
        errors.append(f"{cid} states {states}")
    if rows[0]["expected_state"] != "needs_evidence":
        errors.append(f"{cid} first expected_state {rows[0]['expected_state']}")
    if rows[2]["expected_state"] != "approved":
        errors.append(f"{cid} last expected_state {rows[2]['expected_state']}")
    if "target_ref" not in rows[2]:
        errors.append(f"{cid} missing target_ref")
    for r in rows[:2]:
        if "target_ref" in r:
            errors.append(f"{cid} premature target_ref")
    if rows[2]["state"] == "applied":
        terminal_applied += 1

plan_by_target = {row["target_ref"]: row for row in plan}
if len(plan_by_target) != len(plan):
    errors.append("duplicate plan target")

for row in plan:
    target = row["target_ref"]
    path = ROOT / target
    if not path.exists():
        errors.append(f"missing {target}")
        continue
    fp = fingerprint(path)
    if row["action"] not in {"create", "update"}:
        errors.append(f"{target} action {row['action']}")
    if row["action"] == "create":
        if row["before"] is not None:
            errors.append(f"{target} create before not null")
    else:
        pre = PRE.get(target)
        if pre is None or not pre.exists():
            errors.append(f"{target} missing pre-image")
        else:
            pre_fp = fingerprint(pre)
            if row["before"] != pre_fp:
                errors.append(f"{target} before mismatch plan={row['before']} pre={pre_fp}")
    if row["after_sha256"] != fp["sha256"] or row["bytes"] != fp["bytes"] or row["lines"] != fp["lines"]:
        errors.append(
            f"{target} after mismatch plan={row['after_sha256']}/{row['bytes']}/{row['lines']} disk={fp['sha256']}/{fp['bytes']}/{fp['lines']}"
        )
    text = path.read_text(encoding="utf-8")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        errors.append(f"{target} frontmatter split")
        continue
    try:
        fm = yaml.safe_load(parts[1])
    except Exception as exc:
        errors.append(f"{target} yaml {exc}")
        continue
    if fm.get("type") != "procedure":
        errors.append(f"{target} type {fm.get('type')}")
    expected_sources = EXPECTED_SOURCES.get(target, 1)
    if fm.get("source_count") != expected_sources:
        errors.append(f"{target} source_count {fm.get('source_count')} != {expected_sources}")
    if len(fm.get("sources") or []) != expected_sources:
        errors.append(f"{target} sources len {len(fm.get('sources') or [])} != {expected_sources}")
    if fm.get("evidence_status") != "source_backed":
        errors.append(f"{target} evidence_status {fm.get('evidence_status')}")
    if fm.get("primary_dimension") not in {"B", "C"}:
        errors.append(f"{target} dimension {fm.get('primary_dimension')}")
    for section in SECTIONS:
        if section not in text:
            errors.append(f"{target} missing {section}")

mapping_targets = {m["target_ref"] for m in mapping}
if mapping_targets != set(plan_by_target):
    errors.append(f"mapping targets differ: {mapping_targets ^ set(plan_by_target)}")
for m in mapping:
    cid = m["canonical_candidate"]
    if cid not in by_candidate:
        errors.append(f"mapping candidate {cid} not in ledger")
    action = plan_by_target[m["target_ref"]]["action"]
    if m["action"] != action:
        errors.append(f"mapping action {m['action']} != plan {action}")

index_rows = {}
for line in INDEX.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    row = json.loads(line)
    if row["candidate_id"].startswith(PREFIX):
        index_rows[row["candidate_id"]] = row

index_applied = 0
for cid in by_candidate:
    row = index_rows.get(cid)
    if row is None:
        errors.append(f"index missing {cid}")
        continue
    if row.get("state") != "applied":
        errors.append(f"index {cid} state {row.get('state')}")
    else:
        index_applied += 1
    if row.get("decision", {}).get("status") != "approved":
        errors.append(f"index {cid} decision {row.get('decision')}")

print(json.dumps({
    "ledger_rows": len(ledger),
    "plan_rows": len(plan),
    "mapping_rows": len(mapping),
    "candidates": len(by_candidate),
    "terminal_applied": terminal_applied,
    "plan_create": sum(1 for r in plan if r["action"] == "create"),
    "plan_update": sum(1 for r in plan if r["action"] == "update"),
    "index_applied": index_applied,
    "manifest_status": manifest.get("status"),
    "errors": errors,
}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
