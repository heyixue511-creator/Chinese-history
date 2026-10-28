# -*- coding: utf-8 -*-
"""Verify CL3a registry, corroboration patches, and candidate transitions."""
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
PKG = ROOT / "06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl3a"

text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
print("total", len(rows), "header", text.splitlines()[2])
assert len(rows) == 272
assert text.splitlines()[2] == "# total: 272"
assert rows[-1]["claim_id"] == "claim-0272"
assert [r["claim_id"] for r in rows[259:]] == [f"claim-{i:04d}" for i in range(260, 273)]
print("ids_ok", True)

new = rows[259:]
print("types", dict(Counter(r["claim_type"] for r in new)))
print("confidence", dict(Counter(r["confidence"] for r in new)))
print("supported_by", sum(1 for r in new if r.get("supported_by")))
print("links", sum(len(r.get("supported_by") or []) for r in new))
print("distinct", len({p for r in new for p in r.get("supported_by") or []}))
print("tentative", all(r["consensus"] == "tentative" for r in rows))
print("source_backed", all(r["review_status"] == "source_backed" for r in rows))
print("empty_support", [r["claim_id"] for r in new if not r.get("supported_by")])
print("span_kinds", dict(Counter(r["source"]["source_span"]["span_kind"] for r in new)))

assert new[-1]["source"]["candidate_id"] == DOC + ":cand-01-112"
assert new[-1]["source"]["merged_candidate_ids"] == [DOC + ":cand-01-79"]

# Corroboration patches.
patched = []
for r in rows[:259]:
    src = r["source"]
    if src.get("merged_candidate_ids") or src.get("corroborating_spans"):
        assert src.get("merged_candidate_ids"), r["claim_id"]
        assert src.get("corroborating_spans"), r["claim_id"]
        if not any(cid.startswith(DOC + ":") for cid in src["merged_candidate_ids"]):
            continue
        for cid in src["merged_candidate_ids"]:
            assert cid.startswith(DOC + ":"), (r["claim_id"], cid)
        for sp in src["corroborating_spans"]:
            assert sp["doc_id"] == DOC, r["claim_id"]
            assert sp["source_file"].endswith("中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md")
            assert sp["candidate_id"].startswith(DOC + ":"), r["claim_id"]
            assert sp["line_start"] <= sp["line_end"], r["claim_id"]
            assert sp["key_lines"], r["claim_id"]
            assert all(sp["line_start"] <= n <= sp["line_end"] for n in sp["key_lines"]), r["claim_id"]
        patched.append(r["claim_id"])
print("patched_claims", len(patched), patched)
assert len(patched) == 13

# Candidate index.
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
by = {r["candidate_id"]: r for r in index}
print("cand_rows", len(index))
print("cand_states", dict(Counter(r["state"] for r in index)))
print("cand_lifecycle", dict(Counter(r["lifecycle_class"] for r in index)))
targets = sorted(cid for cid in by if cid.startswith(DOC + ":"))
new_targets = []
for cid in targets:
    r = by[cid]
    if r.get("target_ref", "").startswith("claim/") and r["state"] == "applied":
        new_targets.append(cid)
print("2016_applied_to_claim", len(new_targets))
assert len(new_targets) >= 27
for cid in new_targets:
    r = by[cid]
    assert r["candidate_type"] == "claim", cid
    assert r["lifecycle_class"] == "terminal", cid
    assert r["decision"]["status"] == "approved", cid
    assert r["decision"]["decided_by"] == "Agent", cid
    assert r["decision"]["decided_at"] == "2026-10-27", cid

# Specific CL3a transitions.
expected = {}
for r in new:
    expected[r["source"]["candidate_id"]] = r["claim_id"]
    for cid in r["source"].get("merged_candidate_ids") or []:
        expected[cid] = r["claim_id"]
patch_map = {
    "claim-0038": "cand-01-07", "claim-0041": "cand-01-16",
    "claim-0042": "cand-01-20", "claim-0043": "cand-01-30",
    "claim-0044": "cand-01-40", "claim-0045": "cand-01-45",
    "claim-0046": "cand-01-48", "claim-0047": "cand-01-64",
    "claim-0048": "cand-01-69", "claim-0049": "cand-01-72",
    "claim-0050": "cand-01-75", "claim-0051": "cand-01-71",
    "claim-0091": "cand-01-21",
}
for claim_id, short in patch_map.items():
    expected[DOC + ":" + short] = claim_id
assert len(expected) == 27, len(expected)
for cid, claim_id in expected.items():
    assert by[cid]["state"] == "applied", (cid, by[cid]["state"])
    assert by[cid]["target_ref"] == "claim/" + claim_id, (cid, by[cid]["target_ref"])
print("cl3a_transitions", len(expected), "all_ok", True)
print("cl3a_targets", sorted({v for v in expected.values()}))

rem16 = sum(1 for r in index
            if r["candidate_type"] == "claim" and r["candidate_id"].startswith(DOC + ":")
            and r["state"] == "needs_evidence")
remall = sum(1 for r in index if r["candidate_type"] == "claim" and r["state"] == "needs_evidence")
print("2016_remaining", rem16)
print("all_claim_remaining", remall)
print("by_doc_remaining", dict(Counter(r["candidate_id"].split(":")[0] for r in index
                                       if r["candidate_type"] == "claim" and r["state"] == "needs_evidence")))

# Package artifacts.
for name in ("manifest.json", "claim-rows.jsonl", "claim-updates.jsonl",
             "apply-plan.jsonl", "candidate-decision-ledger.jsonl",
             "canonical-mapping.json"):
    p = PKG / name
    assert p.is_file(), name
print("package_files", sorted(p.name for p in PKG.iterdir()))
mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
assert len(mapping) == 27
assert mapping[DOC + ":cand-01-112"] == "claim-0272"
assert mapping[DOC + ":cand-01-79"] == "claim-0272"
print("mapping_ok", True)
