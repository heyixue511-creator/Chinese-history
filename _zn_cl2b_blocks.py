# -*- coding: utf-8 -*-
import json
from pathlib import Path

root = Path(r"D:/中国设计史研究")
cands = [json.loads(l) for l in (root / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [
    r for r in cands
    if r.get("candidate_type") == "claim"
    and r["candidate_id"].startswith("2009-xiayanjing-zhongguo-shejishi:cand-02-")
]
blocks = [json.loads(l) for l in (root / "03-processing/2009-xiayanjing-zhongguo-shejishi/source-map.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
for r in sorted(sel, key=lambda x: x["payload"]["source_span"]["line_start"]):
    sp = r["payload"]["source_span"]
    overlap = [b for b in blocks if b["line_start"] <= sp["line_end"] and b["line_end"] >= sp["line_start"]]
    print(r["candidate_id"].split(":")[1], f'{sp["line_start"]}-{sp["line_end"]}', ",".join(f'{b["block_id"]}:{b["block_type"]}' for b in overlap))
