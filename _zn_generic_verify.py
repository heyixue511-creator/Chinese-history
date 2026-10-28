# -*- coding: utf-8 -*-
"""Generic claim-batch verification after apply."""
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
CFG = json.loads((ROOT / "_zn_batch_config.json").read_text(encoding="utf-8"))
DOC = CFG["doc_id"]
SRC = CFG["source_file"]
DATE = CFG["date"]
BASE = CFG["baseline"]
EXP = CFG["expected"]
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
PKG = ROOT / "06-runtime/automation" / CFG["package"]

text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
assert len(rows) == EXP["registry_total"], len(rows)
assert text.splitlines()[2] == f"# total: {EXP['registry_total']}"
assert text.count("\n- claim_id:") == EXP["registry_total"]
n_new = EXP["claims"]
assert rows[-n_new]["claim_id"] == f"claim-{int(BASE['last_claim'].split('-')[1]) + 1:04d}"
new = rows[-n_new:]

assert Counter(r["claim_type"] for r in new) == Counter(EXP["types"]), Counter(
    r["claim_type"] for r in new)
assert all(r["consensus"] == "tentative" for r in new)
assert all(r["review_status"] == "source_backed" for r in new)
assert all(r["created"] == DATE and r["updated"] == DATE for r in new)
assert all(r["source"]["doc_id"] == DOC for r in new)
assert all(r["source"]["source_file"] == SRC for r in new)
assert all(r["source"]["candidate_id"].startswith(DOC + ":") for r in new)
for r in new:
    span = r["source"]["source_span"]
    assert CFG["scope"]["line_start"] <= span["line_start"] <= span["line_end"] <= CFG["scope"]["line_end"]
    assert span["key_lines"] and min(span["key_lines"]) >= span["line_start"]
    assert max(span["key_lines"]) <= span["line_end"]
    assert '"' not in r["statement_zh"] and '"' not in r["discussion_notes"]

links = sum(len(r["supported_by"]) for r in new)
distinct = len({p for r in new for p in r["supported_by"]})
assert links == EXP["links"], links
assert distinct == EXP["distinct"], distinct
for r in new:
    for p in r["supported_by"]:
        assert (ROOT / p).is_file(), (r["claim_id"], p)

by_id = {r["claim_id"]: r for r in rows}
patched = []
for claim_id in CFG.get("patch_claim_ids", []):
    r = by_id[claim_id]
    patched.append(claim_id)
    assert len(r["source"]["merged_candidate_ids"]) == 1, claim_id
    assert len(r["source"]["corroborating_spans"]) == 1, claim_id
    assert r["updated"] == DATE, claim_id
assert len(patched) == EXP["patches"], len(patched)

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
states = Counter(r["state"] for r in cand_rows)
lifecycle = Counter(r["lifecycle_class"] for r in cand_rows)
assert states["applied"] == EXP["applied"], states
assert states["needs_evidence"] == EXP["needs"], states
assert states["no_delta"] == EXP["no_delta"], states
assert states["rejected"] == EXP["rejected"], states
assert lifecycle["terminal"] == EXP["lifecycle_terminal"], lifecycle
assert lifecycle["active"] == EXP["lifecycle_active"], lifecycle

is_doc = lambda r: r["candidate_id"].startswith(DOC + ":")
applied_doc = sum(1 for r in cand_rows if is_doc(r) and r["state"] == "applied")
needs_doc = sum(1 for r in cand_rows if is_doc(r) and r["state"] == "needs_evidence")
assert applied_doc == EXP["applied_doc"], applied_doc
assert needs_doc == EXP["needs_doc"], needs_doc
claim_debt = sum(1 for r in cand_rows
                 if r["candidate_type"] == "claim" and r["state"] == "needs_evidence")
assert claim_debt == EXP["claim_debt"], claim_debt


def jl(name):
    return [json.loads(l) for l in (PKG / name).read_text(encoding="utf-8").splitlines() if l.strip()]


claim_rows = jl("claim-rows.jsonl")
updates = jl("claim-updates.jsonl")
plan = jl("apply-plan.jsonl")
ledger = jl("candidate-decision-ledger.jsonl")
mapping = json.loads((PKG / "canonical-mapping.json").read_text(encoding="utf-8"))
manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))

assert len(claim_rows) == n_new
assert len(updates) == EXP["patches"]
assert len(plan) == n_new + EXP["patches"]
assert len(ledger) == EXP["candidates"]
assert len(mapping) == EXP["candidates"]
expected_actions = {"claim_create": n_new}
if EXP["patches"]:
    expected_actions["claim_update"] = EXP["patches"]
assert Counter(p["action"] for p in plan) == expected_actions, Counter(p["action"] for p in plan)
assert len({l["candidate_id"] for l in ledger}) == EXP["candidates"]
assert all(l["state"] == "applied" and l["expected_state"] == "needs_evidence" for l in ledger)
assert all(l["updated_at"] == DATE for l in ledger)
assert set(mapping) == {l["candidate_id"] for l in ledger}
assert all(cid.startswith(DOC + ":") for cid in mapping)

assert manifest["candidate_count"] == EXP["candidates"]
assert manifest["claim_rows"] == n_new
assert manifest["existing_claims_updated"] == EXP["patches"]
assert manifest["support_links"] == EXP["links"]
assert manifest["distinct_support"] == EXP["distinct"]
assert manifest["with_supported_by"] == sum(1 for r in new if r["supported_by"])
assert manifest["baseline"] == {
    "claim_registry_total": BASE["registry_total"],
    "candidate_needs_evidence": BASE["needs"],
    "candidate_applied": BASE["applied"],
    "candidate_no_delta": BASE["no_delta"],
}
assert manifest["result"] == {
    "claim_registry_total": EXP["registry_total"],
    "candidate_needs_evidence": EXP["needs"],
    "candidate_applied": EXP["applied"],
    "candidate_no_delta": EXP["no_delta"],
}
assert manifest["after_bytes"] == len(text.encode("utf-8")), (
    manifest["after_bytes"], len(text.encode("utf-8")))
expected_spans = sorted([
    [a, b] for a, b in {
        (json.loads(l)["payload"]["source_span"]["line_start"],
         json.loads(l)["payload"]["source_span"]["line_end"])
        for l in CAND.read_text(encoding="utf-8").splitlines()
        if l.strip() and json.loads(l)["candidate_id"] in mapping
    }
])
assert manifest["scope_spans"] == expected_spans

print(json.dumps({
    "registry": len(rows),
    "new_claims": len(new),
    "types": dict(Counter(r["claim_type"] for r in new)),
    "links": links,
    "distinct": distinct,
    "patched": len(patched),
    "candidate_states": dict(states),
    "lifecycle": dict(lifecycle),
    "applied_doc": applied_doc,
    "needs_doc": needs_doc,
    "claim_debt": claim_debt,
    "package": {"rows": len(claim_rows), "updates": len(updates), "plan": len(plan),
                "ledger": len(ledger), "mapping": len(mapping)},
    "registry_sha256": manifest["after_sha256"],
    "registry_bytes": manifest["after_bytes"],
}, ensure_ascii=False, indent=2))
print("VERIFY OK")
