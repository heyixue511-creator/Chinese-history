# -*- coding: utf-8 -*-
"""Verify Xia Yanjing 2016 procedure batch J artifacts against disk and candidate index."""
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2016xiayanjing-procedures-batch-j")
INDEX = Path("06-runtime/state/candidate-index.jsonl")
PREFIX = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:"

SECTIONS = [
    "## 描述",
    "## 核心内容",
    "## 在层级体系中的位置",
    "## 相关知识元",
    "## 验证状态",
    "## 参考文献",
]

CREATES = {
    "cand-05-30": ("procedures/erci-shaocheng-fa.md", "二次烧成法", "ceramic_technique", 2, "B"),
    "cand-06-18": ("procedures/zhiding-zhishao.md", "支钉支烧法", "ceramic_technique", 2, "B"),
    "cand-05-42": ("procedures/jiezhi-yinhua.md", "介质印花", "textile_technique", 2, "B"),
    "cand-06-43": ("procedures/song-dai-jianzhu-caihua.md", "宋代建筑彩画", "construction_technique", 2, "B"),
    "cand-06-45": ("procedures/pinhe-liang.md", "拼合梁", "woodworking_technique", 2, "B"),
    "cand-07-100": ("procedures/jintong-fa.md", "浸铜法", "metalworking_technique", 2, "B"),
    "cand-07-54": ("procedures/tiaohua-jieben.md", "挑花结本", "textile_technique", 2, "B"),
    "cand-07-55": ("procedures/chuai-ran.md", "踹染", "textile_technique", 2, "B"),
    "cand-08-83": ("procedures/chuiyou-fa.md", "吹釉法", "ceramic_technique", 2, "B"),
    "cand-09-79": ("procedures/fengxiang-nisu.md", "凤翔泥塑", "sculpture_technique", 2, "B"),
}

UPDATES = {
    "cand-06-49": ("procedures/die-shao.md", "叠烧", "ceramic_technique", 2, "B", "die-shao"),
    "cand-07-52": ("procedures/nianjin-pianjin.md", "捻金与片金", "textile_technique", 2, "B", "nianjin-pianjin"),
    "cand-07-87": ("procedures/huozi-yinshua.md", "活字印刷", "printing_technique", 2, "C", "huozi-yinshua"),
    "cand-08-84": ("procedures/duanban-taoyin.md", "短版套印", "printing_technique", 4, "C", "duanban-taoyin"),
}

NO_DELTA = {
    "cand-05-55": "procedures/chuihui-fa.md",
    "cand-06-26": "procedures/nian-ya.md",
    "cand-07-50": "terms/blue-and-white-porcelain.md",
    "cand-07-51": "terms/youlihong.md",
}

MERGED = {"cand-05-31": "procedures/zhiding-zhishao.md"}
REJECTS = {"cand-08-86", "cand-10-14"}

PRE = json.loads(Path("06-runtime/_tmp_pre_j_hashes.json").read_text(encoding="utf-8"))
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

if len(ledger) != 59:
    errors.append(f"ledger rows {len(ledger)} != 59")
if len(plan) != 14:
    errors.append(f"plan rows {len(plan)} != 14")
if len(mapping) != 18:
    errors.append(f"mapping rows {len(mapping)} != 18")

by_candidate = {}
for row in ledger:
    by_candidate.setdefault(row["candidate_id"], []).append(row)
    if row["decision"]["decided_by"] != "Agent":
        errors.append(f"decided_by {row['candidate_id']}")
    if row["decision"]["decided_at"] != "2026-10-25":
        errors.append(f"decided_at {row['candidate_id']}")

if len(by_candidate) != 21:
    errors.append(f"candidates {len(by_candidate)} != 21")

terminal_applied = 0
terminal_no_delta = 0
terminal_rejected = 0
for cid, rows in by_candidate.items():
    if cid.split(":")[1] in REJECTS:
        if len(rows) != 1:
            errors.append(f"{cid} rejected rows {len(rows)} != 1")
            continue
        row = rows[0]
        if row["expected_state"] != "needs_evidence" or row["state"] != "rejected":
            errors.append(f"{cid} reject transition {row['expected_state']}->{row['state']}")
        if row["decision"]["status"] != "rejected":
            errors.append(f"{cid} reject status {row['decision']['status']}")
        if "target_ref" in row:
            errors.append(f"{cid} reject has target_ref")
        terminal_rejected += 1
        continue
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

if terminal_applied != 15:
    errors.append(f"applied {terminal_applied} != 15")
if terminal_no_delta != 4:
    errors.append(f"no_delta {terminal_no_delta} != 4")
if terminal_rejected != 2:
    errors.append(f"rejected {terminal_rejected} != 2")

plan_by_target = {row["target_ref"]: row for row in plan}
if len(plan_by_target) != len(plan):
    errors.append("duplicate plan target")

expected = {}
for cid, (rel, title, sub, sc, dim) in CREATES.items():
    expected[cid] = (rel, title, sub, sc, dim, None)
for cid, (rel, title, sub, sc, dim, slug) in UPDATES.items():
    expected[cid] = (rel, title, sub, sc, dim, slug)
for cid, rel in MERGED.items():
    expected[cid] = (rel, "支钉支烧法", "ceramic_technique", 2, "B", None)

for cid, (rel, title, sub, sc, dim, slug) in expected.items():
    target = f"04-knowledge/units/{rel}"
    path = ROOT / target
    if not path.exists():
        errors.append(f"missing {target}")
        continue
    fp = fingerprint(path)
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
    if title not in fm.get("title", ""):
        errors.append(f"{target} title {fm.get('title')}")
    if fm.get("type") != "procedure":
        errors.append(f"{target} type {fm.get('type')}")
    if fm.get("sub_type") != sub:
        errors.append(f"{target} sub_type {fm.get('sub_type')}")
    if fm.get("source_count") != sc or len(fm.get("sources") or []) != sc:
        errors.append(f"{target} source_count {fm.get('source_count')} sources {len(fm.get('sources') or [])} != {sc}")
    if fm.get("primary_dimension") != dim:
        errors.append(f"{target} dimension {fm.get('primary_dimension')} != {dim}")
    if fm.get("evidence_status") != "source_backed":
        errors.append(f"{target} evidence_status {fm.get('evidence_status')}")
    for section in SECTIONS:
        if section not in text:
            errors.append(f"{target} missing {section}")

for row in plan:
    target = row["target_ref"]
    path = ROOT / target
    if not path.exists():
        errors.append(f"missing plan {target}")
        continue
    fp = fingerprint(path)
    if row["action"] not in {"create", "update"}:
        errors.append(f"{target} action {row['action']}")
    if row["action"] == "create":
        if row["before"] is not None:
            errors.append(f"{target} create before not null")
    else:
        slug = UPDATES[row["candidate_id"].split(":")[1]][5]
        pre_fp = fingerprint(Path(f"06-runtime/_tmp_pre_j_{slug}.md"))
        if row["before"] != pre_fp:
            errors.append(f"{target} before mismatch plan={row['before']} pre={pre_fp}")
        if PRE[slug] != pre_fp:
            errors.append(f"{target} before hash snapshot mismatch")
    if row["after_sha256"] != fp["sha256"] or row["bytes"] != fp["bytes"] or row["lines"] != fp["lines"]:
        errors.append(
            f"{target} after mismatch plan={row['after_sha256']}/{row['bytes']}/{row['lines']} disk={fp['sha256']}/{fp['bytes']}/{fp['lines']}"
        )

mapping_targets = {m["target_ref"] for m in mapping}
expected_targets = set(plan_by_target) | {f"04-knowledge/units/{p}" for p in NO_DELTA.values()}
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
        if m["canonical_candidate"].split(":")[1] not in NO_DELTA:
            errors.append(f"mapping no_delta {m['canonical_candidate']}")
    else:
        if m["target_ref"] not in plan_by_target:
            errors.append(f"mapping target {m['target_ref']} not in plan")
        elif m["action"] != plan_by_target[m["target_ref"]]["action"]:
            errors.append(f"mapping action {m['action']} != plan {plan_by_target[m['target_ref']]['action']}")

rejected_full = {cid for cid in by_candidate if cid.split(":")[1] in REJECTS}
if mapping_candidates != set(by_candidate) - rejected_full:
    errors.append(f"mapping candidate union differs: {mapping_candidates ^ (set(by_candidate) - rejected_full)}")

index_rows = {}
index_text = INDEX.read_bytes().decode("utf-8").replace("\r\n", "\n")
for line in index_text.splitlines():
    if not line.strip():
        continue
    row = json.loads(line)
    if row["candidate_id"].startswith(PREFIX):
        cid = row["candidate_id"].split(":")[1]
        index_rows[cid] = row

for cid in by_candidate:
    short = cid.split(":")[1]
    row = index_rows.get(short)
    if row is None:
        errors.append(f"index missing {cid}")
        continue
    if short in REJECTS:
        want = "rejected"
    elif short in NO_DELTA:
        want = "no_delta"
    else:
        want = "applied"
    if row.get("state") != want:
        errors.append(f"index {cid} state {row.get('state')} != {want}")
    want_decision = "rejected" if short in REJECTS else "approved"
    if row.get("decision", {}).get("status") != want_decision:
        errors.append(f"index {cid} decision {row.get('decision')}")

index_hash = "sha256:" + hashlib.sha256(index_text.encode("utf-8")).hexdigest()
counts = Counter(json.loads(l)["state"] for l in index_text.splitlines() if l.strip())

print(json.dumps({
    "ledger_rows": len(ledger),
    "plan_rows": len(plan),
    "mapping_rows": len(mapping),
    "candidates": len(by_candidate),
    "terminal_applied": terminal_applied,
    "terminal_no_delta": terminal_no_delta,
    "terminal_rejected": terminal_rejected,
    "plan_create": sum(1 for r in plan if r["action"] == "create"),
    "plan_update": sum(1 for r in plan if r["action"] == "update"),
    "merged": sorted(MERGED),
    "index_rows": len(index_text.splitlines()),
    "index_sha256": index_hash,
    "index_counts": dict(counts),
    "manifest_status": manifest.get("status"),
    "errors": errors,
}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
