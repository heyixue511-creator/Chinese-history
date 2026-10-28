# -*- coding: utf-8 -*-
"""Apply the CL1 Gao Feng 2004 claim batch.

Writes 36 claim rows to 04-knowledge/quality/claim-registry.yml, applies the
37 candidate-index transitions, and writes the work-package artifacts.
"""
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2004-gaofeng-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md"
REG = ROOT / "04-knowledge" / "quality" / "claim-registry.yml"
CAND = ROOT / "06-runtime" / "state" / "candidate-index.jsonl"
PKG = ROOT / "06-runtime" / "automation" / "2026-10-27-2004gaofeng-claims-batch-cl1"
DATE = "2026-10-27"
CLAIM_TYPES = {
    "factual_claim", "interpretive_claim", "synthetic_claim",
    "evaluative_claim", "contested_claim", "historiographic_claim",
}


def sha256_text(text: str) -> str:
    data = text.replace("\r\n", "\n").encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


def load_rows():
    rows = json.loads(read_text(ROOT / "_zn_claim_gf_rows.json"))
    assert isinstance(rows, list) and len(rows) == 36
    return rows


def validate_rows(rows):
    src_lines = read_text(ROOT / SRC).splitlines()
    ids = set()
    for row in rows:
        cid = row["claim_id"]
        assert cid.startswith("claim-") and cid not in ids, cid
        ids.add(cid)
        assert row["claim_type"] in CLAIM_TYPES, row["claim_type"]
        assert row["statement_zh"].strip() and row["statement_en"].strip()
        assert '"' not in row["statement_zh"], cid
        assert row["consensus"] == "tentative"
        assert row["review_status"] == "source_backed"
        src = row["source"]
        assert src["doc_id"] == DOC
        assert src["source_file"] == SRC
        span = src["source_span"]
        assert 1 <= span["line_start"] <= span["line_end"] <= len(src_lines), cid
        assert span["key_lines"] and all(span["line_start"] <= n <= span["line_end"] for n in span["key_lines"]), cid
        assert span["span_kind"] in {"line", "contiguous", "bounded"}, cid
        assert src["candidate_id"].startswith(DOC + ":")
        for path in row["supported_by"]:
            assert (ROOT / path).is_file(), path


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
    rows = load_rows()
    validate_rows(rows)

    before = read_text(REG)
    assert before.strip().endswith("[]"), "claim registry is not empty"
    before_hash = sha256_text(before)

    # candidate index preflight
    lines = CAND.read_text(encoding="utf-8").splitlines()
    index = [json.loads(line) for line in lines if line.strip()]
    by_cid = {r["candidate_id"]: r for r in index}
    assert len(by_cid) == len(index)

    cid_to_claim = {}
    for row in rows:
        candidate_ids = [row["source"]["candidate_id"]]
        candidate_ids += row["source"].get("merged_candidate_ids") or []
        for cid in candidate_ids:
            assert cid not in cid_to_claim, cid
            cid_to_claim[cid] = row["claim_id"]

    assert len(cid_to_claim) == 37, len(cid_to_claim)
    for cid, claim_id in cid_to_claim.items():
        assert cid in by_cid, cid
        assert by_cid[cid]["state"] == "needs_evidence", (cid, by_cid[cid]["state"])
        assert by_cid[cid]["candidate_type"] == "claim", cid

    text = registry_text(rows)
    assert text.count("\n- claim_id:") == len(rows), text.count("\n- claim_id:")
    parsed = yaml.safe_load(text)
    assert len(parsed) == len(rows)

    write_atomic(REG, text)

    # candidate-index apply
    before_counts = Counter(r["state"] for r in index)
    merged_cids = {
        cid for row in rows
        for cid in (row["source"].get("merged_candidate_ids") or [])
    }
    applied = 0
    for cid, claim_id in cid_to_claim.items():
        row = dict(by_cid[cid])
        row["state"] = "applied"
        row["target_ref"] = f"claim/{claim_id}"
        row["lifecycle_class"] = "terminal"
        row["updated_at"] = DATE
        row["decision"] = {
            "decided_at": DATE,
            "decided_by": "Agent",
            "reason": (
                f"已应用：与同册同义断言合并为 {claim_id}，补 corroborating span。"
                if cid in merged_cids
                else f"已应用：写入 claim-registry.yml {claim_id}。"
            ),
            "status": "approved",
        }
        by_cid[cid] = row
        applied += 1

    assert applied == 37
    ordered = [by_cid[r["candidate_id"]] for r in index]
    after_counts = Counter(r["state"] for r in ordered)
    write_atomic(
        CAND,
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in ordered),
    )

    # work package artifacts
    PKG.mkdir(parents=True, exist_ok=True)
    claim_rows = []
    for row in rows:
        claim_rows.append(json.dumps(row, ensure_ascii=False, sort_keys=True))
    (PKG / "claim-rows.jsonl").write_text("\n".join(claim_rows) + "\n", encoding="utf-8", newline="\n")

    apply_rows = []
    for row in rows:
        canonical = json.dumps(row, ensure_ascii=False, sort_keys=True)
        candidate_ids = [row["source"]["candidate_id"]]
        candidate_ids += row["source"].get("merged_candidate_ids") or []
        apply_rows.append({
            "action": "claim_create" if len(candidate_ids) == 1 else "claim_create_merged",
            "claim_id": row["claim_id"],
            "candidate_ids": candidate_ids,
            "target_ref": f"claim/{row['claim_id']}",
            "after_sha256": sha256_text(canonical),
            "bytes": len(canonical.encode("utf-8")),
            "before": None,
            "note": (
                "新建 claim-registry 行；来源 " + SRC
                + ("" if len(candidate_ids) == 1 else "；合并 " + ", ".join(candidate_ids[1:]))
            ),
        })
    (PKG / "apply-plan.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in apply_rows),
        encoding="utf-8", newline="\n",
    )

    ledger = []
    for cid, claim_id in cid_to_claim.items():
        merged = "；同义合并，补 corroborating span L1835" if cid.endswith("cand-02-20") else ""
        ledger.append({
            "candidate_id": cid,
            "expected_state": "needs_evidence",
            "state": "applied",
            "target_ref": f"claim/{claim_id}",
            "decision": {
                "status": "approved",
                "reason": f"已写入 claim-registry.yml {claim_id}{merged}。",
                "decided_by": "Agent",
                "decided_at": DATE,
            },
            "updated_at": DATE,
        })
    (PKG / "candidate-decision-ledger.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in ledger),
        encoding="utf-8", newline="\n",
    )

    (PKG / "canonical-mapping.json").write_text(
        json.dumps(cid_to_claim, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n",
    )

    manifest = {
        "package_id": PKG.name,
        "profile": "claim-batch-v1",
        "goal": "高丰 2004 册 37 条 claim 候选写回 claim-registry",
        "doc_id": DOC,
        "source_file": SRC,
        "date": DATE,
        "candidate_count": 37,
        "claim_rows": len(rows),
        "merged_candidates": 1,
        "with_supported_by": sum(1 for r in rows if r["supported_by"]),
        "scope_spans": sorted({
            (row["source"]["source_span"]["line_start"], row["source"]["source_span"]["line_end"])
            for row in rows
        }),
        "before_sha256": before_hash,
        "after_sha256": sha256_text(text),
        "before_bytes": len(before.encode("utf-8")),
        "after_bytes": len(text.encode("utf-8")),
        "baseline": {
            "claim_registry_total": 0,
            "candidate_needs_evidence": before_counts["needs_evidence"],
            "candidate_applied": before_counts["applied"],
        },
        "result": {
            "claim_registry_total": len(rows),
            "candidate_needs_evidence": after_counts["needs_evidence"],
            "candidate_applied": after_counts["applied"],
        },
    }
    (PKG / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n",
    )

    print(json.dumps({
        "claim_rows": len(rows),
        "candidate_applied": applied,
        "registry_after_sha256": manifest["after_sha256"],
        "package": PKG.name,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
