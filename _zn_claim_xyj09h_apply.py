# -*- coding: utf-8 -*-
"""Apply the CL2h Xia Yanjing 2009 claim batch (ch.9 Ming-Qing).

Appends 18 claim rows to 04-knowledge/quality/claim-registry.yml, applies the
18 candidate-index transitions, and writes the work-package artifacts.
"""
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
REG = ROOT / "04-knowledge" / "quality" / "claim-registry.yml"
CAND = ROOT / "06-runtime" / "state" / "candidate-index.jsonl"
PKG = ROOT / "06-runtime" / "automation" / "2026-10-27-2009xiayanjing-claims-batch-cl2h"
DATE = "2026-10-27"
CLAIM_TYPES = {
    "factual_claim", "interpretive_claim", "synthetic_claim",
    "evaluative_claim", "contested_claim", "historiographic_claim",
}
N = 18
BASE = 219
FIRST = BASE + 1
LAST = BASE + N


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
    rows = json.loads(read_text(ROOT / "_zn_claim_xyj09h_rows.json"))
    assert isinstance(rows, list) and len(rows) == N
    return rows


def load_existing():
    text = read_text(REG)
    parsed = yaml.safe_load(text)
    assert isinstance(parsed, list) and len(parsed) == BASE, f"expected {BASE} baseline claims"
    assert f"# total: {BASE}" in text, "baseline header mismatch"
    return parsed


def validate_rows(rows, existing):
    src_lines = read_text(ROOT / SRC).splitlines()
    ids = {row["claim_id"] for row in existing}
    expected_ids = [f"claim-{i:04d}" for i in range(FIRST, LAST + 1)]
    assert [row["claim_id"] for row in rows] == expected_ids
    for row in rows:
        cid = row["claim_id"]
        assert cid not in ids, cid
        ids.add(cid)
        assert row["claim_type"] in CLAIM_TYPES, row["claim_type"]
        assert row["statement_zh"].strip() and row["statement_en"].strip()
        assert '"' not in row["statement_zh"], cid
        assert row["consensus"] == "tentative"
        assert row["review_status"] == "source_backed"
        assert row["created"] == DATE and row["updated"] == DATE
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
    new_rows = load_rows()
    existing = load_existing()
    validate_rows(new_rows, existing)
    rows = existing + new_rows

    before = read_text(REG)
    before_hash = sha256_text(before)

    lines = CAND.read_text(encoding="utf-8").splitlines()
    index = [json.loads(line) for line in lines if line.strip()]
    by_cid = {r["candidate_id"]: r for r in index}
    assert len(by_cid) == len(index)

    cid_to_claim = {}
    for row in new_rows:
        cid = row["source"]["candidate_id"]
        assert cid not in cid_to_claim, cid
        cid_to_claim[cid] = row["claim_id"]

    assert len(cid_to_claim) == N
    for cid, claim_id in cid_to_claim.items():
        assert cid in by_cid, cid
        c = by_cid[cid]
        assert c["state"] == "needs_evidence", (cid, c["state"])
        assert c["candidate_type"] == "claim", cid
        cspan = (c.get("payload") or {}).get("source_span") or {}
        row = next(r for r in new_rows if r["claim_id"] == claim_id)
        span = row["source"]["source_span"]
        assert cspan["line_start"] <= span["line_start"] <= span["line_end"] <= cspan["line_end"], (
            cid, cspan, span["line_start"], span["line_end"])

    text = registry_text(rows)
    assert text.count("\n- claim_id:") == len(rows), text.count("\n- claim_id:")
    parsed = yaml.safe_load(text)
    assert len(parsed) == len(rows)
    assert [r["claim_id"] for r in parsed[-N:]] == [r["claim_id"] for r in new_rows]

    write_atomic(REG, text)

    before_counts = Counter(r["state"] for r in index)
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
            "reason": f"已应用：写入 claim-registry.yml {claim_id}。",
            "status": "approved",
        }
        by_cid[cid] = row
        applied += 1

    assert applied == N
    ordered = [by_cid[r["candidate_id"]] for r in index]
    after_counts = Counter(r["state"] for r in ordered)
    write_atomic(
        CAND,
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in ordered),
    )

    PKG.mkdir(parents=True, exist_ok=True)
    (PKG / "claim-rows.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in new_rows),
        encoding="utf-8", newline="\n",
    )

    apply_rows = []
    for row in new_rows:
        canonical = json.dumps(row, ensure_ascii=False, sort_keys=True)
        cid = row["source"]["candidate_id"]
        apply_rows.append({
            "action": "claim_create",
            "claim_id": row["claim_id"],
            "candidate_ids": [cid],
            "target_ref": f"claim/{row['claim_id']}",
            "after_sha256": sha256_text(canonical),
            "bytes": len(canonical.encode("utf-8")),
            "before": None,
            "note": "新建 claim-registry 行；来源 " + SRC,
        })
    (PKG / "apply-plan.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in apply_rows),
        encoding="utf-8", newline="\n",
    )

    ledger = []
    for cid, claim_id in cid_to_claim.items():
        ledger.append({
            "candidate_id": cid,
            "expected_state": "needs_evidence",
            "state": "applied",
            "target_ref": f"claim/{claim_id}",
            "decision": {
                "status": "approved",
                "reason": f"已写入 claim-registry.yml {claim_id}。",
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
        "goal": "夏燕靖 2009 册明清章 18 条 claim 候选写回 claim-registry",
        "doc_id": DOC,
        "source_file": SRC,
        "date": DATE,
        "candidate_count": N,
        "claim_rows": len(new_rows),
        "merged_candidates": 0,
        "with_supported_by": sum(1 for r in new_rows if r["supported_by"]),
        "scope_spans": sorted({
            (row["source"]["source_span"]["line_start"], row["source"]["source_span"]["line_end"])
            for row in new_rows
        }),
        "before_sha256": before_hash,
        "after_sha256": sha256_text(text),
        "before_bytes": len(before.encode("utf-8")),
        "after_bytes": len(text.encode("utf-8")),
        "baseline": {
            "claim_registry_total": len(existing),
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
        "claim_rows_added": len(new_rows),
        "claim_registry_total": len(rows),
        "candidate_applied": applied,
        "registry_after_sha256": manifest["after_sha256"],
        "registry_after_bytes": manifest["after_bytes"],
        "package": PKG.name,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
