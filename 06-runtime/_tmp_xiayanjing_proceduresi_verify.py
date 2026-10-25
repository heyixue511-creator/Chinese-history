# -*- coding: utf-8 -*-
"""Verify Xia Yanjing 2016 procedure batch I artifacts against disk and candidate index."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2016xiayanjing-procedures-batch-i")
INDEX = Path("06-runtime/state/candidate-index.jsonl")
PREFIX = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:"
PRE = {
    f"04-knowledge/units/procedures/{n}.md": Path(f"06-runtime/_tmp_pre_i_{n}.md")
    for n in "shiqi-dazhi-sanfa mozhi-shiqi sheng-tie-rou-hua-ji-shu dyeing".split()
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
    "04-knowledge/units/procedures/sunmao-jiegou.md": 1,
    "04-knowledge/units/procedures/hunzhu-fa.md": 1,
    "04-knowledge/units/procedures/fenshi-fa.md": 1,
    "04-knowledge/units/procedures/paituo-gufeng.md": 1,
    "04-knowledge/units/procedures/chelun-jiance-fa.md": 1,
    "04-knowledge/units/procedures/diezhu-jishu.md": 1,
    "04-knowledge/units/procedures/shuili-gufeng.md": 1,
    "04-knowledge/units/procedures/shiqi-dazhi-sanfa.md": 2,
    "04-knowledge/units/procedures/mozhi-shiqi.md": 4,
    "04-knowledge/units/procedures/sheng-tie-rou-hua-ji-shu.md": 2,
    "04-knowledge/units/procedures/dyeing.md": 3,
}
NO_DELTA_TARGETS = {
    "04-knowledge/units/procedures/lunzhi-fa.md",
    "04-knowledge/units/procedures/hefan-fa.md",
    "04-knowledge/units/procedures/yin-wen-mo-yin.md",
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
if len(plan) != 11:
    errors.append(f"plan rows {len(plan)} != 11")
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
terminal_no_delta = 0
for cid, rows in by_candidate.items():
    if len(rows) != 3:
        errors.append(f"{cid} ledger rows {len(rows)} != 3")
        continue
    states = [r["state"] for r in rows]
    if states[:2] != ["ready_for_review", "approved"]:
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
    elif rows[2]["state"] == "no_delta":
        terminal_no_delta += 1
    else:
        errors.append(f"{cid} terminal {rows[2]['state']}")

if len(by_candidate) != 14:
    errors.append(f"candidates {len(by_candidate)} != 14")
if terminal_applied != 11:
    errors.append(f"applied {terminal_applied} != 11")
if terminal_no_delta != 3:
    errors.append(f"no_delta {terminal_no_delta} != 3")

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
    if fm.get("primary_dimension") != "B":
        errors.append(f"{target} dimension {fm.get('primary_dimension')}")
    for section in SECTIONS:
        if section not in text:
            errors.append(f"{target} missing {section}")

mapping_targets = {m["target_ref"] for m in mapping}
expected_targets = set(plan_by_target) | NO_DELTA_TARGETS
if mapping_targets != expected_targets:
    errors.append(f"mapping targets differ: {mapping_targets ^ expected_targets}")
mapping_candidates = set()
for m in mapping:
    cid = m["canonical_candidate"]
    mapping_candidates.add(cid)
    mapping_candidates.update(m.get("merged_candidates") or [])
    if cid not in by_candidate:
        errors.append(f"mapping candidate {cid} not in ledger")
    if m["action"] == "no_delta":
        if m["target_ref"] not in NO_DELTA_TARGETS:
            errors.append(f"mapping no_delta target {m['target_ref']}")
    else:
        if m["target_ref"] not in plan_by_target:
            errors.append(f"mapping target {m['target_ref']} not in plan")
        elif m["action"] != plan_by_target[m["target_ref"]]["action"]:
            errors.append(f"mapping action {m['action']} != plan {plan_by_target[m['target_ref']]['action']}")

if mapping_candidates != set(by_candidate):
    errors.append(f"mapping candidate union differs: {mapping_candidates ^ set(by_candidate)}")

index_rows = {}
for line in INDEX.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    row = json.loads(line)
    if row["candidate_id"].startswith(PREFIX) and row["candidate_id"] in by_candidate:
        index_rows[row["candidate_id"]] = row

index_applied = 0
index_no_delta = 0
for cid in by_candidate:
    row = index_rows.get(cid)
    if row is None:
        errors.append(f"index missing {cid}")
        continue
    expected_state = "no_delta" if cid in {m["canonical_candidate"] for m in mapping if m["action"] == "no_delta"} else "applied"
    if row.get("state") != expected_state:
        errors.append(f"index {cid} state {row.get('state')} != {expected_state}")
    elif expected_state == "applied":
        index_applied += 1
    else:
        index_no_delta += 1
    if row.get("decision", {}).get("status") != "approved":
        errors.append(f"index {cid} decision {row.get('decision')}")

index_bytes = INDEX.read_bytes()
index_text = index_bytes.decode("utf-8").replace("\r\n", "\n")
index_hash = "sha256:" + hashlib.sha256(index_text.encode("utf-8")).hexdigest()
from collections import Counter

counts = Counter(json.loads(l)["state"] for l in index_text.splitlines() if l.strip())

print(json.dumps({
    "ledger_rows": len(ledger),
    "plan_rows": len(plan),
    "mapping_rows": len(mapping),
    "candidates": len(by_candidate),
    "terminal_applied": terminal_applied,
    "terminal_no_delta": terminal_no_delta,
    "plan_create": sum(1 for r in plan if r["action"] == "create"),
    "plan_update": sum(1 for r in plan if r["action"] == "update"),
    "index_applied": index_applied,
    "index_no_delta": index_no_delta,
    "index_rows": len(index_text.splitlines()),
    "index_sha256": index_hash,
    "index_counts": dict(counts),
    "manifest_status": manifest.get("status"),
    "errors": errors,
}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
