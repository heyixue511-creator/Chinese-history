import json
from pathlib import Path
p=Path(r"D:/中国设计史研究/06-runtime/state/candidate-index.jsonl")
rows=[json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
doc="2010-tianzibing-zhongguo-gongyi-meishushi:"
cs=[r for r in rows if r["candidate_id"].startswith(doc) and r["state"]=="needs_evidence" and r["candidate_type"]=="unit" and 2069<=r["payload"]["source_span"]["line_start"]<=2437]
for r in sorted(cs,key=lambda r:(r["payload"]["source_span"]["line_start"],r["candidate_id"])):
    pl=r["payload"]
    print(r["candidate_id"].split(":")[1], pl["source_span"]["line_start"], pl["source_span"]["line_end"], pl.get("unit_type"), pl.get("proposed_slug"), "|", pl.get("title"))
print("total",len(cs))
