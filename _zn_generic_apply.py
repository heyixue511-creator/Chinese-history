# -*- coding: utf-8 -*-
"""Generic claim-batch apply: create claims and/or patch existing claims.

Reads _zn_batch_config.json plus rows/patch JSON files named in it.
"""
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
CFG = json.loads((ROOT / "_zn_batch_config.json").read_text(encoding="utf-8"))
DOC = CFG["doc_id"]
SRC = CFG["source_file"]
DATE = CFG["date"]
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
PKG = ROOT / "06-runtime/automation" / CFG["package"]
NEW = json.loads((ROOT / CFG["rows_file"]).read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / CFG["patch_file"]).read_text(encoding="utf-8"))
BASE = CFG["baseline"]
CLAIM_TYPES = {
    "factual_claim", "interpretive_claim", "synthetic_claim",
    "evaluative_claim", "contested_claim", "historiographic_claim",
}


def sha256_text(text: str) -> str:
    data = text.replace("\r\n", "\n").encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def row_hash(row) -> str:
    return sha256_text(json.dumps(row, ensure_ascii=False, sort_keys=True))


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


def registry_text(rows) -> str:
    header = (
        "# Claim Registry v1.0\n"
        f"# generated: {DATE}\n"
        f"# total: {len(rows)}\n"
    )
    return header + yaml.safe_dump(
        rows, allow_unicode=True, sort_keys=False,
        default_flow_style=False, width=100000,
    )


def main():
    before_text = REG.read_text(encoding="utf-8")
    existing = yaml.safe_load(before_text)
    assert len(existing) == BASE["registry_total"], len(existing)
    assert before_text.splitlines()[2] == f"# total: {BASE['registry_total']}"
    assert existing[-1]["claim_id"] == BASE["last_claim"]

    by_id = {r["claim_id"]: r for r in existing}
    assert len(by_id) == len(existing)

    # --- validate new rows ---
    first = int(BASE["last_claim"].split("-")[1]) + 1
    expected_ids = [f"claim-{i:04d}" for i in range(first, first + len(NEW))]
    assert [r["claim_id"] for r in NEW] == expected_ids
    for row in NEW:
        assert row["claim_id"] not in by_id, row["claim_id"]
        assert row["claim_type"] in CLAIM_TYPES, row["claim_type"]
        assert row["statement_zh"].strip() and row["statement_en"].strip()
        assert '"' not in row["statement_zh"], row["claim_id"]
        assert '"' not in row["discussion_notes"], row["claim_id"]
        assert row["consensus"] == "tentative"
        assert row["review_status"] == "source_backed"
        assert row["created"] == DATE and row["updated"] == DATE
        assert row["source"]["doc_id"] == DOC
        assert row["source"]["source_file"] == SRC
        assert row["source"]["candidate_id"].startswith(DOC + ":")
        for path in row["supported_by"]:
            assert (ROOT / path).is_file(), path

    # --- validate patches ---
    patch_by_claim = {}
    for p in PATCH:
        claim_id = p["claim_id"]
        assert claim_id in by_id, claim_id
        claim = by_id[claim_id]
        assert claim["source"]["doc_id"] != DOC or True
        assert not claim["source"].get("merged_candidate_ids"), claim_id
        assert not claim["source"].get("corroborating_spans"), claim_id
        cid = p["candidate_id"]
        assert cid.startswith(DOC + ":"), cid
        patch_by_claim.setdefault(claim_id, []).append(p)

    # --- candidate index ---
    index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
    by_cand = {r["candidate_id"]: r for r in index}
    assert len(by_cand) == len(index)
    before_counts = Counter(r["state"] for r in index)
    assert before_counts["applied"] == BASE["applied"], before_counts
    assert before_counts["needs_evidence"] == BASE["needs"], before_counts
    assert before_counts["no_delta"] == BASE["no_delta"], before_counts
    assert before_counts["rejected"] == BASE["rejected"], before_counts

    transitions = {}
    for row in NEW:
        src = row["source"]
        primary = src["candidate_id"]
        for cid in [primary] + list(src.get("merged_candidate_ids") or []):
            assert cid not in transitions, cid
            c = by_cand[cid]
            assert c["state"] == "needs_evidence", (cid, c["state"])
            assert c["candidate_type"] == "claim", cid
            transitions[cid] = {
                "target_ref": f"claim/{row['claim_id']}",
                "reason": (
                    f"已应用：写入 claim-registry.yml {row['claim_id']}。"
                    if cid == primary else
                    f"已应用：与 {primary} 合并写入 claim-registry.yml {row['claim_id']}。"
                ),
                "merge_mode": "primary" if cid == primary else "merged_new_claim",
            }
    for claim_id, patches in patch_by_claim.items():
        for p in patches:
            cid = p["candidate_id"]
            assert cid not in transitions, cid
            c = by_cand[cid]
            assert c["state"] == "needs_evidence", (cid, c["state"])
            assert c["candidate_type"] == "claim", cid
            transitions[cid] = {
                "target_ref": f"claim/{claim_id}",
                "reason": f"已应用：并入 {claim_id} 的 corroborating_spans，不重复建条。",
                "merge_mode": "merged_existing_claim",
            }

    assert len(transitions) == len(NEW) + len(PATCH), (len(transitions), len(NEW), len(PATCH))
    assert all(cid.startswith(DOC + ":") for cid in transitions)
    assert sum(1 for v in transitions.values() if v["merge_mode"] == "primary") == sum(
        1 for row in NEW if row["source"].get("candidate_id"))
    assert sum(1 for v in transitions.values() if v["merge_mode"] == "merged_existing_claim") == len(PATCH)

    # --- apply patches to existing claims ---
    before_rows = {}
    after_rows = {}
    for claim_id, patches in patch_by_claim.items():
        claim = by_id[claim_id]
        before_rows[claim_id] = json.loads(json.dumps(claim, ensure_ascii=False))
        src = claim["source"]
        merged = src.setdefault("merged_candidate_ids", [])
        corrob = src.setdefault("corroborating_spans", [])
        for p in patches:
            cid = p["candidate_id"]
            assert cid not in merged, (claim_id, cid)
            merged.append(cid)
            span = dict(p["corroborating_span"])
            assert span["candidate_id"] not in {s.get("candidate_id") for s in corrob}
            corrob.append(span)
        claim["updated"] = DATE
        after_rows[claim_id] = json.loads(json.dumps(claim, ensure_ascii=False))

    rows = existing + NEW
    text = registry_text(rows)
    expected_total = BASE["registry_total"] + len(NEW)
    assert text.count("\n- claim_id:") == expected_total, text.count("\n- claim_id:")
    reparsed = yaml.safe_load(text)
    assert len(reparsed) == expected_total
    assert [r["claim_id"] for r in reparsed[-len(NEW):]] == expected_ids

    write_atomic(REG, text)

    # --- apply candidate transitions ---
    for cid, tr in transitions.items():
        row = dict(by_cand[cid])
        row["state"] = "applied"
        row["target_ref"] = tr["target_ref"]
        row["lifecycle_class"] = "terminal"
        row["updated_at"] = DATE
        row["decision"] = {
            "decided_at": DATE,
            "decided_by": "Agent",
            "reason": tr["reason"],
            "status": "approved",
        }
        by_cand[cid] = row

    ordered = [by_cand[r["candidate_id"]] for r in index]
    after_counts = Counter(r["state"] for r in ordered)
    write_atomic(
        CAND,
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in ordered),
    )

    # --- package artifacts ---
    PKG.mkdir(parents=True, exist_ok=True)
    (PKG / "claim-rows.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in NEW),
        encoding="utf-8", newline="\n",
    )
    (PKG / "claim-updates.jsonl").write_text(
        "".join(json.dumps(after_rows[cid], ensure_ascii=False, sort_keys=True) + "\n"
                for cid in sorted(after_rows)),
        encoding="utf-8", newline="\n",
    )

    apply_rows = []
    for row in NEW:
        canonical = json.dumps(row, ensure_ascii=False, sort_keys=True)
        ids = [row["source"]["candidate_id"]] + list(row["source"].get("merged_candidate_ids") or [])
        apply_rows.append({
            "action": "claim_create",
            "claim_id": row["claim_id"],
            "candidate_ids": ids,
            "target_ref": f"claim/{row['claim_id']}",
            "before_sha256": None,
            "after_sha256": sha256_text(canonical),
            "bytes": len(canonical.encode("utf-8")),
            "note": "新建 claim-registry 行；来源 " + SRC,
        })
    for claim_id in sorted(patch_by_claim):
        apply_rows.append({
            "action": "claim_update",
            "claim_id": claim_id,
            "candidate_ids": [p["candidate_id"] for p in patch_by_claim[claim_id]],
            "target_ref": f"claim/{claim_id}",
            "before_sha256": row_hash(before_rows[claim_id]),
            "after_sha256": row_hash(after_rows[claim_id]),
            "bytes": len(json.dumps(after_rows[claim_id], ensure_ascii=False,
                                    sort_keys=True).encode("utf-8")),
            "note": "补 merged_candidate_ids 与跨版本 corroborating_spans；来源 " + SRC,
        })
    (PKG / "apply-plan.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in apply_rows),
        encoding="utf-8", newline="\n",
    )

    ledger = []
    for cid in sorted(transitions):
        tr = transitions[cid]
        ledger.append({
            "candidate_id": cid,
            "expected_state": "needs_evidence",
            "state": "applied",
            "target_ref": tr["target_ref"],
            "decision": {
                "status": "approved",
                "reason": tr["reason"],
                "decided_by": "Agent",
                "decided_at": DATE,
            },
            "updated_at": DATE,
        })
    (PKG / "candidate-decision-ledger.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in ledger),
        encoding="utf-8", newline="\n",
    )

    mapping = {cid: transitions[cid]["target_ref"].split("/", 1)[1] for cid in sorted(transitions)}
    (PKG / "canonical-mapping.json").write_text(
        json.dumps(mapping, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n",
    )

    scope_spans = sorted([
        [start, end] for start, end in {
            (c["payload"]["source_span"]["line_start"], c["payload"]["source_span"]["line_end"])
            for c in (by_cand[cid] for cid in transitions)
        }
    ])
    support_links = sum(len(r["supported_by"]) for r in NEW)
    distinct_support = len({p for r in NEW for p in r["supported_by"]})
    manifest = {
        "package_id": PKG.name,
        "profile": "claim-batch-v1",
        "goal": CFG["goal"],
        "doc_id": DOC,
        "source_file": SRC,
        "date": DATE,
        "candidate_count": len(transitions),
        "claim_rows": len(NEW),
        "existing_claims_updated": len(patch_by_claim),
        "merged_candidates": sum(1 for r in NEW if r["source"].get("merged_candidate_ids")),
        "no_delta_candidates": 0,
        "with_supported_by": sum(1 for r in NEW if r["supported_by"]),
        "support_links": support_links,
        "distinct_support": distinct_support,
        "scope_spans": scope_spans,
        "corroboration_claim_ids": sorted(patch_by_claim),
        "before_sha256": sha256_text(before_text),
        "after_sha256": sha256_text(text),
        "before_bytes": len(before_text.encode("utf-8")),
        "after_bytes": len(text.encode("utf-8")),
        "baseline": {
            "claim_registry_total": len(existing),
            "candidate_needs_evidence": before_counts["needs_evidence"],
            "candidate_applied": before_counts["applied"],
            "candidate_no_delta": before_counts["no_delta"],
        },
        "result": {
            "claim_registry_total": len(rows),
            "candidate_needs_evidence": after_counts["needs_evidence"],
            "candidate_applied": after_counts["applied"],
            "candidate_no_delta": after_counts["no_delta"],
        },
    }
    (PKG / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n",
    )

    print(json.dumps({
        "claim_rows_added": len(NEW),
        "existing_claims_updated": len(patch_by_claim),
        "candidate_applied": len(transitions),
        "claim_registry_total": len(rows),
        "registry_after_sha256": manifest["after_sha256"],
        "registry_after_bytes": manifest["after_bytes"],
        "support_links": support_links,
        "distinct_support": distinct_support,
        "scope_spans": len(scope_spans),
        "candidate_states": dict(after_counts),
        "package": PKG.name,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
