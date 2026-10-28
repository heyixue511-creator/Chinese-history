# -*- coding: utf-8 -*-
"""List 2009 claims whose span starts within a line range."""
import sys
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
DOC = "2009-xiayanjing-zhongguo-shejishi"

lo, hi = int(sys.argv[1]), int(sys.argv[2])
rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
sel = []
for r in rows:
    if r["source"]["doc_id"] != DOC:
        continue
    sp = r["source"]["source_span"]
    if lo <= sp["line_start"] <= hi:
        sel.append(r)
sel.sort(key=lambda r: r["source"]["source_span"]["line_start"])
print("count", len(sel))
for r in sel:
    sp = r["source"]["source_span"]
    print(r["claim_id"], r["claim_type"], "L%d-%d" % (sp["line_start"], sp["line_end"]),
          "|", sp.get("chapter", ""), "|", sp.get("section", ""))
    print("  ", r["statement_zh"][:300])
    print("   notes:", (r["discussion_notes"] or "")[:180])
    print("   links:", ", ".join(r["supported_by"]))
