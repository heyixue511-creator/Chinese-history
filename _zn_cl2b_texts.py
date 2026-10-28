# -*- coding: utf-8 -*-
import json
from pathlib import Path

root = Path(r"D:/中国设计史研究")
rows = [json.loads(l) for l in (root / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows if r.get("candidate_type") == "claim" and r["candidate_id"].startswith("2009-xiayanjing-zhongguo-shejishi:cand-02-")]
sel.append(next(r for r in rows if r["candidate_id"] == "2009-xiayanjing-zhongguo-shejishi:cand-03-03"))
out = []
for r in sorted(sel, key=lambda x: x["payload"]["source_span"]["line_start"]):
    p = r["payload"]
    sp = p["source_span"]
    out.append(f'## {r["candidate_id"].split(":")[1]}  L{sp["line_start"]}-{sp["line_end"]}  {p.get("claim_scope","")}')
    out.append(f'claim_text: {p.get("claim_text","")}')
    out.append(f'summary: {p.get("summary","")}')
    out.append(f'knowledge_match: {json.dumps(p.get("knowledge_match",{}),ensure_ascii=False)}')
    out.append("")
(root / "_zn_cl2b_texts.txt").write_text("\n".join(out), encoding="utf-8")
print(len(sel))
