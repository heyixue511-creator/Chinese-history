# -*- coding: utf-8 -*-
"""Dump 2009 claims in an ID range with spans."""
import sys

import yaml
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
rows = yaml.safe_load((ROOT / "04-knowledge/quality/claim-registry.yml").read_text(encoding="utf-8"))
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for r in rows:
    n = int(r["claim_id"].split("-")[1])
    if not lo <= n <= hi:
        continue
    doc = r["source"]["doc_id"].split("-")[0]
    sp = r["source"]["source_span"]
    print(r["claim_id"], doc, r["claim_type"], "L%d-%d" % (sp["line_start"], sp["line_end"]))
    print("  ", r["statement_zh"][:400])
    print("   notes:", (r["discussion_notes"] or "")[:200])
    print()
