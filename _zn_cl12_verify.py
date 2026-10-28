# -*- coding: utf-8 -*-
"""Verify CL9a write-back: registry, candidates, package artifacts, manifest."""
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
PKG = ROOT / "06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl9a"
DATE = "2026-10-27"

text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
lines = text.splitlines()
assert len(rows) == 378, len(rows)
assert lines[2] == "# total: 378", lines[2]
assert rows[-1]["claim_id"] == "claim-0378"
assert text.count("\n- claim_id:") == 378

new = [r for r in rows if 364 <= int(r["claim_id"].split("-")[1]) <= 378]
assert [r["claim_id"] for r in new] == [f"claim-{i:04d}" for i in range(364, 379)]
assert Counter(r["claim_type"] for r in new) == {
    "factual_claim": 6, "interpretive_claim": 3, "synthetic_claim": 1,
    "historiographic_claim": 4, "evaluative_claim": 1,
}
assert Counter(r["confidence"] for r in new) == {"medium": 15}
assert all(r["consensus"] == "tentative" for r in new)
assert all(r["review_status"] == "source_backed" for r in new)
assert all(r["created"] == DATE and r["updated"] == DATE for r in new)
assert all(r["source"]["doc_id"] == DOC for r in new)
assert all(r["source"]["candidate_id"].startswith(DOC + ":") for r in new)
kinds = Counter(r["source"]["source_span"]["span_kind"] for r in new)
assert kinds == {"line": 15}, kinds

links = sum(len(r["supported_by"]) for r in new)
distinct = len({p for r in new for p in r["supported_by"]})
assert links == 26, links
assert distinct == 25, distinct
for r in new:
    for p in r["supported_by"]:
        assert (ROOT / p).is_file(), (r["claim_id"], p)

patched = [r for r in rows if r["source"].get("corroborating_spans")]
assert len(patched) == 113, len(patched)
cl9a_claims = ["claim-0247", "claim-0248", "claim-0249", "claim-0250",
               "claim-0251", "claim-0252", "claim-0253"]
by_id = {r["claim_id"]: r for r in rows}
merged_total = 0
for cid in cl9a_claims:
    r = by_id[cid]
    src = r["source"]
    assert src["doc_id"] == "2009-xiayanjing-zhongguo-shejishi", cid
    assert len(src["merged_candidate_ids"]) == 1, cid
    assert len(src["corroborating_spans"]) == 1, cid
    assert all(c.startswith(DOC + ":") for c in src["merged_candidate_ids"]), cid
    assert r["updated"] == DATE, cid
    merged_total += 1
assert merged_total == 7, merged_total

required = {"doc_id", "source_file", "line_start", "line_end", "span_kind",
            "key_lines", "block_ids", "chapter", "section", "candidate_id"}
for r in rows:
    for s in r["source"].get("corroborating_spans") or []:
        assert {"line_start", "line_end", "key_lines", "block_ids"} <= set(s), (
            r["claim_id"], set(s))
        assert s["line_start"] <= min(s["key_lines"]) <= max(s["key_lines"]) <= s["line_end"], r["claim_id"]
        if s.get("doc_id") == DOC:
            assert required <= set(s), (r["claim_id"], required - set(s))
            assert s["key_lines"], r["claim_id"]

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
states = Counter(r["state"] for r in cand_rows)
lifecycle = Counter(r["lifecycle_class"] for r in cand_rows)
assert states == {"applied": 3367, "rejected": 871, "no_delta": 234,
                  "needs_evidence": 867}, states
assert lifecycle == {"terminal": 4472, "active": 867}, lifecycle

is2016 = lambda r: r["candidate_id"].startswith(DOC + ":")
applied_2016 = sum(1 for r in cand_rows
                   if is2016(r) and r["candidate_type"] == "claim" and r["state"] == "applied")
needs_2016 = sum(1 for r in cand_rows if is2016(r) and r["state"] == "needs_evidence")
assert applied_2016 == 235, applied_2016
assert needs_2016 == 18, needs_2016
claim_debt = sum(1 for r in cand_rows
                 if r["candidate_type"] == "claim" and r["state"] == "needs_evidence")
assert claim_debt == 867, claim_debt


# Package artifacts.
def jl(name):
    return [json.loads(l) for l in (PKG / name).read_text(encoding="utf-8").splitlines() if l.strip()]


claim_rows = jl("claim-rows.jsonl")
updates = jl("claim-updates.jsonl")
plan = jl("apply-plan.jsonl")
ledger = jl("candidate-decision-ledger.jsonl")
mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))

assert len(claim_rows) == 15, len(claim_rows)
assert len(updates) == 7, len(updates)
assert len(plan) == 22, len(plan)
assert len(ledger) == 22, len(ledger)
assert len(mapping) == 22, len(mapping)
assert Counter(p["action"] for p in plan) == {"claim_create": 15, "claim_update": 7}
assert len({l["candidate_id"] for l in ledger}) == 22
assert all(l["state"] == "applied" and l["expected_state"] == "needs_evidence" for l in ledger)
assert all(l["updated_at"] == DATE for l in ledger)
assert set(mapping) == {l["candidate_id"] for l in ledger}
assert all(cid.startswith(DOC + ":") for cid in mapping)
assert Counter(mapping.values())["claim-0247"] == 1

assert manifest["candidate_count"] == 22
assert manifest["claim_rows"] == 15
assert manifest["existing_claims_updated"] == 7
assert manifest["merged_candidates"] == 0
assert manifest["no_delta_candidates"] == 0
assert manifest["support_links"] == 26
assert manifest["distinct_support"] == 25
assert manifest["with_supported_by"] == 14
expected_spans = sorted([
    [a, b] for a, b in {
        (json.loads(l)["payload"]["source_span"]["line_start"],
         json.loads(l)["payload"]["source_span"]["line_end"])
        for l in CAND.read_text(encoding="utf-8").splitlines()
        if l.strip() and json.loads(l)["candidate_id"] in mapping
    }
])
assert manifest["scope_spans"] == expected_spans, (len(manifest["scope_spans"]), len(expected_spans))
assert len(manifest["scope_spans"]) == 13, len(manifest["scope_spans"])
assert manifest["baseline"] == {
    "claim_registry_total": 363, "candidate_needs_evidence": 889,
    "candidate_applied": 3345, "candidate_no_delta": 234,
}
assert manifest["result"] == {
    "claim_registry_total": 378, "candidate_needs_evidence": 867,
    "candidate_applied": 3367, "candidate_no_delta": 234,
}
assert manifest["after_bytes"] == len(text.encode("utf-8"))

print(json.dumps({
    "registry": len(rows),
    "new_claims": len(new),
    "types": dict(Counter(r["claim_type"] for r in new)),
    "span_kinds": dict(kinds),
    "support_links": links,
    "distinct_support": distinct,
    "patched_total": len(patched),
    "cl9a_patched": len(cl9a_claims),
    "merged_total": merged_total,
    "candidate_states": dict(states),
    "lifecycle": dict(lifecycle),
    "applied_2016": applied_2016,
    "needs_2016": needs_2016,
    "claim_debt": claim_debt,
    "package": {"rows": len(claim_rows), "updates": len(updates), "plan": len(plan),
                "ledger": len(ledger), "mapping": len(mapping)},
    "manifest_result": manifest["result"],
}, ensure_ascii=False, indent=2))
