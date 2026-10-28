# -*- coding: utf-8 -*-
"""Verify CL3c registry, corroboration patches, and candidate transitions."""
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
PKG = ROOT / "06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl3c"
PATCH = json.loads((ROOT / "_zn_cl4b_patch.json").read_text(encoding="utf-8"))

text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
print("total", len(rows), "header", text.splitlines()[2])
assert len(rows) == 299
assert text.splitlines()[2] == "# total: 299"
assert rows[-1]["claim_id"] == "claim-0299"
assert [r["claim_id"] for r in rows[282:]] == [f"claim-{i:04d}" for i in range(283, 300)]
print("ids_ok", True)

new = rows[282:]
print("types", dict(Counter(r["claim_type"] for r in new)))
print("confidence", dict(Counter(r["confidence"] for r in new)))
print("supported_by", sum(1 for r in new if r.get("supported_by")))
print("links", sum(len(r.get("supported_by") or []) for r in new))
print("distinct", len({p for r in new for p in r.get("supported_by") or []}))
print("tentative", all(r["consensus"] == "tentative" for r in rows))
print("source_backed", all(r["review_status"] == "source_backed" for r in rows))
print("empty_support", [r["claim_id"] for r in new if not r.get("supported_by")])
print("span_kinds", dict(Counter(r["source"]["source_span"]["span_kind"] for r in new)))
assert dict(Counter(r["claim_type"] for r in new)) == {
    "synthetic_claim": 2, "historiographic_claim": 7, "factual_claim": 3,
    "interpretive_claim": 3, "evaluative_claim": 1, "contested_claim": 1}
assert dict(Counter(r["confidence"] for r in new)) == {"high": 6, "medium": 11}
assert sum(len(r.get("supported_by") or []) for r in new) == 50
assert len({p for r in new for p in r.get("supported_by") or []}) == 37
assert dict(Counter(r["source"]["source_span"]["span_kind"] for r in new)) == {
    "bounded": 4, "line": 13}

# Corroboration patches.
patched = []
for r in rows:
    src = r["source"]
    if src.get("merged_candidate_ids") or src.get("corroborating_spans"):
        if src.get("merged_candidate_ids") and not src.get("corroborating_spans"):
            continue
        assert src.get("merged_candidate_ids"), r["claim_id"]
        assert src.get("corroborating_spans"), r["claim_id"]
        assert len(src["merged_candidate_ids"]) == len(src["corroborating_spans"]), r["claim_id"]
        for cid in src["merged_candidate_ids"]:
            assert ":" in cid, (r["claim_id"], cid)
        for sp in src["corroborating_spans"]:
            if not str(sp.get("candidate_id", "")).startswith(DOC + ":"):
                continue
            assert sp["doc_id"] == DOC, r["claim_id"]
            assert sp["line_start"] <= sp["line_end"], r["claim_id"]
            assert sp["key_lines"], r["claim_id"]
            assert all(sp["line_start"] <= n <= sp["line_end"] for n in sp["key_lines"]), r["claim_id"]
        patched.append(r["claim_id"])
print("patched_claims", len(patched))
assert len(patched) == 42, len(patched)
assert len(set(patched)) == 42

# Exact CL3c patch mapping.
by_id = {r["claim_id"]: r for r in rows}
for p in PATCH:
    src = by_id[p["claim_id"]]["source"]
    assert p["candidate_id"] in src["merged_candidate_ids"], p["claim_id"]
    assert any(sp["candidate_id"] == p["candidate_id"] for sp in src["corroborating_spans"]), p["claim_id"]
print("cl3c_patch_targets", len({p["claim_id"] for p in PATCH}))
assert len({p["claim_id"] for p in PATCH}) == 15

# Candidate index.
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
by = {r["candidate_id"]: r for r in index}
print("cand_rows", len(index))
print("cand_states", dict(Counter(r["state"] for r in index)))
print("cand_lifecycle", dict(Counter(r["lifecycle_class"] for r in index)))
assert dict(Counter(r["state"] for r in index)) == {
    "applied": 3214, "rejected": 871, "no_delta": 234, "needs_evidence": 1020}
assert dict(Counter(r["lifecycle_class"] for r in index)) == {
    "terminal": 4319, "active": 1020}
targets = sorted(cid for cid in by if cid.startswith(DOC + ":"))
new_targets = []
for cid in targets:
    r = by[cid]
    if r.get("target_ref", "").startswith("claim/") and r["state"] == "applied":
        new_targets.append(cid)
print("2016_applied_to_claim", len(new_targets))
assert len(new_targets) == 82
for cid in new_targets:
    r = by[cid]
    assert r["candidate_type"] == "claim", cid
    assert r["lifecycle_class"] == "terminal", cid
    assert r["decision"]["status"] == "approved", cid
    assert r["decision"]["decided_by"] == "Agent", cid
    assert r["decision"]["decided_at"] == "2026-10-27", cid

expected = {}
for p in PATCH:
    expected[p["candidate_id"]] = p["claim_id"]
for r in new:
    expected[r["source"]["candidate_id"]] = r["claim_id"]
    for cid in r["source"].get("merged_candidate_ids") or []:
        expected[cid] = r["claim_id"]
assert len(expected) == 32, len(expected)
for cid, claim_id in expected.items():
    assert by[cid]["state"] == "applied", (cid, by[cid]["state"])
    assert by[cid]["target_ref"] == "claim/" + claim_id, (cid, by[cid]["target_ref"])
print("cl3c_transitions", len(expected), "all_ok", True)
print("cl3c_targets", sorted({v for v in expected.values()}))

nd_id = DOC + ":cand-02-114"
nd = by[nd_id]
assert nd["state"] == "no_delta", nd["state"]
assert nd["lifecycle_class"] == "terminal"
assert nd["target_ref"] == "claim/claim-0080"
assert nd["decision"]["status"] == "approved"
assert nd["decision"]["decided_by"] == "Agent"
assert nd["decision"]["decided_at"] == "2026-10-27"
print("no_delta_ok", nd_id, nd["target_ref"])

rem16 = sum(1 for r in index
            if r["candidate_type"] == "claim" and r["candidate_id"].startswith(DOC + ":")
            and r["state"] == "needs_evidence")
remall = sum(1 for r in index if r["candidate_type"] == "claim" and r["state"] == "needs_evidence")
print("2016_remaining", rem16)
print("all_claim_remaining", remall)
print("by_doc_remaining", dict(Counter(r["candidate_id"].split(":")[0] for r in index
                                       if r["candidate_type"] == "claim" and r["state"] == "needs_evidence")))
assert rem16 == 171
assert remall == 1020

# Package artifacts.
for name in ("manifest.json", "claim-rows.jsonl", "claim-updates.jsonl",
             "apply-plan.jsonl", "candidate-decision-ledger.jsonl",
             "canonical-mapping.json"):
    p = PKG / name
    assert p.is_file(), name
print("package_files", sorted(p.name for p in PKG.iterdir()))
mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
assert len(mapping) == 32
assert set(mapping) == set(expected)
for cid, claim_id in expected.items():
    assert mapping[cid] == claim_id, cid
print("mapping_ok", True)

ledger = [json.loads(l) for l in (PKG / "candidate-decision-ledger.jsonl").read_text(
    encoding="utf-8").splitlines() if l.strip()]
assert len(ledger) == 33
for row in ledger:
    assert set(row) == {"candidate_id", "expected_state", "state", "target_ref",
                        "decision", "updated_at"}, row["candidate_id"]
assert sum(1 for r in ledger if r["state"] == "applied") == 32
assert sum(1 for r in ledger if r["state"] == "no_delta") == 1
print("ledger_ok", True, "rows", len(ledger))

claim_rows = [json.loads(l) for l in (PKG / "claim-rows.jsonl").read_text(
    encoding="utf-8").splitlines() if l.strip()]
claim_updates = [json.loads(l) for l in (PKG / "claim-updates.jsonl").read_text(
    encoding="utf-8").splitlines() if l.strip()]
apply_plan = [json.loads(l) for l in (PKG / "apply-plan.jsonl").read_text(
    encoding="utf-8").splitlines() if l.strip()]
assert len(claim_rows) == 17
assert len(claim_updates) == 15
assert len(apply_plan) == 32
assert sum(1 for r in apply_plan if r["action"] == "claim_create") == 17
assert sum(1 for r in apply_plan if r["action"] == "claim_update") == 15
print("package_counts", len(claim_rows), len(claim_updates), len(apply_plan))

manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
print("manifest_support", manifest["support_links"], manifest["distinct_support"])
print("manifest_result", manifest["result"])
assert manifest["support_links"] == 50
assert manifest["distinct_support"] == 37
assert manifest["result"] == {
    "claim_registry_total": 299,
    "candidate_needs_evidence": 1020,
    "candidate_applied": 3214,
    "candidate_no_delta": 234,
}
print("manifest_ok", True)
