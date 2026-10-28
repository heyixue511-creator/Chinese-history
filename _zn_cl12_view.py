# -*- coding: utf-8 -*-
"""Compact view of 2016 chapter-11 claim candidates."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"

rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows
       if r["candidate_id"].startswith(DOC + ":")
       and r["candidate_type"] == "claim"
       and r["state"] == "needs_evidence"
       and 5124 <= r["payload"]["source_span"]["line_start"] <= 5544]
sel.sort(key=lambda r: r["payload"]["source_span"]["line_start"])
print("count", len(sel))
for r in sel:
    p = r["payload"]
    sp = p["source_span"]
    print(r["candidate_id"].split(":")[1], "|", p["claim_scope"], "|",
          "L%d-%d" % (sp["line_start"], sp["line_end"]), "|", sp["block_ids"])
    print("  ", p["claim_text"])
    print("   note:", (p.get("support_note") or "")[:260])
    print("-" * 60)
