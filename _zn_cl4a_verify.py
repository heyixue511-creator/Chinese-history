# -*- coding: utf-8 -*-
"""Verify CL3b registry, corroboration patches, and candidate transitions."""
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
PKG = ROOT / "06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl3b"
PATCH = json.loads((ROOT / "_zn_cl4a_patch.json").read_text(encoding="utf-8"))

text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
print("total", len(rows), "header", text.splitlines()[2])
assert len(rows) == 282
assert text.splitlines()[2] == "# total: 282"
assert rows[-1]["claim_id"] == "claim-0282"
assert [r["claim_id"] for r in rows[272:]] == [f"claim-{i:04d}" for i in range(273, 283)]
print("ids_ok", True)

new = rows[272:]
print("types", dict(Counter(r["claim_type"] for r in new)))
print("confidence", dict(Counter(r["confidence"] for r in new)))
print("supported_by", sum(1 for r in new if r.get("supported_by")))
print("links", sum(len(r.get("supported_by") or []) for r in new))
print("distinct", len({p for r in new for p in r.get("supported_by") or []}))
print("tentative", all(r["consensus"] == "tentative" for r in rows))
print("source_backed", all(r["review_status"] == "source_backed" for r in rows))
print("empty_support", [r["claim_id"] for r in new if not r.get("supported_by")])
print("span_kinds", dict(Counter(r["source"]["source_span"]["span_kind"] for r in new)))

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
assert len(patched) == 26
assert set(p["claim_id"] for p in PATCH) <= set(patched)

# Exact CL3b patch mapping.
by_id = {r["claim_id"]: r for r in rows}
for p in PATCH:
    src = by_id[p["claim_id"]]["source"]
    assert p["candidate_id"] in src["merged_candidate_ids"], p["claim_id"]
    assert any(sp["candidate_id"] == p["candidate_id"] for sp in src["corroborating_spans"]), p["claim_id"]

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
assert len(new_targets) >= 50
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
assert len(expected) == 23, len(expected)
for cid, claim_id in expected.items():
    assert by[cid]["state"] == "applied", (cid, by[cid]["state"])
    assert by[cid]["target_ref"] == "claim/" + claim_id, (cid, by[cid]["target_ref"])
print("cl3b_transitions", len(expected), "all_ok", True)
print("cl3b_targets", sorted({v for v in expected.values()}))

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
assert len(mapping) == 23
assert set(mapping) == set(expected)
for cid, claim_id in expected.items():
    assert mapping[cid] == claim_id, cid
print("mapping_ok", True)

ledger = [json.loads(l) for l in (PKG / "candidate-decision-ledger.jsonl").read_text(
    encoding="utf-8").splitlines() if l.strip()]
assert len(ledger) == 23
for row in ledger:
    assert set(row) == {"candidate_id", "expected_state", "state", "target_ref",
                        "decision", "updated_at"}, row["candidate_id"]
print("ledger_ok", True, "rows", len(ledger))
