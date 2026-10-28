# -*- coding: utf-8 -*-
"""Compact span/block table for Qin-Han candidates."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
rows = [r for r in index if r["candidate_id"].startswith(DOC + ":")
        and r["candidate_type"] == "claim"
        and 1609 <= r["payload"]["source_span"]["line_start"] <= 2064]
rows.sort(key=lambda r: r["payload"]["source_span"]["line_start"])
for r in rows:
    sp = r["payload"]["source_span"]
    print(r["candidate_id"].split(":")[1], sp["line_start"], sp["line_end"],
          sp["block_ids"], r["payload"]["claim_scope"],
          "|", r["payload"]["claim_text"][:60])
