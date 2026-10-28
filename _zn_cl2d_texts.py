# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
rows = [json.loads(l) for l in (ROOT / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
blocks = [json.loads(l) for l in (ROOT / "03-processing/2009-xiayanjing-zhongguo-shejishi/source-map.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows if r.get("candidate_type") == "claim" and r["candidate_id"].startswith(DOC + ":") and 1662 <= r["payload"]["source_span"]["line_start"] <= 1966]
out = []
for r in sorted(sel, key=lambda x: (x["payload"]["source_span"]["line_start"], x["candidate_id"])):
    p = r["payload"]; sp = p["source_span"]
    overlap = [b for b in blocks if b["line_start"] <= sp["line_end"] and b["line_end"] >= sp["line_start"]]
    out.append(f'## {r["candidate_id"].split(":")[1]}  L{sp["line_start"]}-{sp["line_end"]}  {p.get("claim_scope","")}')
    out.append(f'claim_text: {p.get("claim_text","")}')
    out.append("blocks: " + ",".join(f'{b["block_id"]}:{b["line_start"]}-{b["line_end"]}' for b in overlap))
    out.append("")
(ROOT / "_zn_cl2d_texts.txt").write_text("\n".join(out), encoding="utf-8")
print("count", len(sel))
