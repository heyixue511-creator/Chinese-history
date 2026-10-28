# -*- coding: utf-8 -*-
"""Dump CL3d claim statements for summary writing."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
for r in rows[299:]:
    s = r["source"]["source_span"]
    print("=" * 72)
    print(r["claim_id"], r["claim_type"], r["confidence"],
          s["span_kind"], s["line_start"], s["line_end"], s["key_lines"], s["block_ids"])
    print("ZH:", r["statement_zh"])
    print("NOTES:", r["discussion_notes"])
    print("SUP:", [p.split("/")[-1].replace(".md", "") for p in r["supported_by"]])
for cid in ("claim-0103", "claim-0104", "claim-0106", "claim-0107",
            "claim-0108", "claim-0110", "claim-0114"):
    r = [x for x in rows if x["claim_id"] == cid][0]
    print("=" * 72)
    print("PATCH TARGET", cid, r["statement_zh"])
    print("MERGED", r["source"]["merged_candidate_ids"])
    for sp in r["source"]["corroborating_spans"]:
        print(" SPAN", sp.get("candidate_id"), sp["line_start"], sp["line_end"], sp["span_kind"])
