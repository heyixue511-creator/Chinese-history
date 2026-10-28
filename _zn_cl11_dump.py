# -*- coding: utf-8 -*-
"""Dump payloads of 2016 chapter-10 claim candidates by line range."""
import json
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"

lo, hi = int(sys.argv[1]), int(sys.argv[2])
rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows
       if r["candidate_id"].startswith(DOC + ":")
       and r["candidate_type"] == "claim"
       and r["state"] == "needs_evidence"
       and lo <= r["payload"]["source_span"]["line_start"] <= hi]
print("count", len(sel))
for r in sel:
    print(json.dumps({
        "id": r["candidate_id"].split(":")[1],
        "state": r["state"],
        "payload": r["payload"],
    }, ensure_ascii=False, indent=1))
    print("=" * 60)
