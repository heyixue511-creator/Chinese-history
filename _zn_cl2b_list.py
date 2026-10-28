# -*- coding: utf-8 -*-
import json
from pathlib import Path

root = Path(r"D:/中国设计史研究")
rows = [json.loads(l) for l in (root / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
claims = [
    r for r in rows
    if r.get("candidate_type") == "claim"
    and r["candidate_id"].startswith("2009-xiayanjing-zhongguo-shejishi:")
]
print("total", len(claims))

bounds = [
    ("序言", 66, 219),
    ("原始社会", 220, 458),
    ("夏商周", 459, 786),
    ("春秋战国", 787, 1278),
    ("秦汉", 1279, 1661),
    ("魏晋南北朝", 1662, 1966),
    ("隋唐五代", 1967, 2443),
    ("宋辽金西夏", 2444, 2915),
    ("元代", 2916, 3376),
    ("明清", 3377, 3805),
    ("近现代", 3806, 4156),
    ("新中国", 4157, 5375),
    ("后记", 5376, 5409),
]
from collections import Counter
c = Counter()
for name, a, b in bounds:
    sel = [r for r in claims if a <= (r["payload"]["source_span"]["line_start"]) <= b]
    c[name] = len(sel)
print(dict(c))

sel = [r for r in claims if 787 <= r["payload"]["source_span"]["line_start"] <= 1278]
print("selected", len(sel))
for r in sorted(sel, key=lambda x: x["payload"]["source_span"]["line_start"]):
    sp = r["payload"]["source_span"]
    p = r.get("payload") or {}
    print("\t".join([
        r["candidate_id"].split(":")[1],
        f'{sp["line_start"]}-{sp["line_end"]}',
        p.get("claim_scope", ""),
        (p.get("claim_text") or "").replace("\n", " ")[:80],
        str(p.get("knowledge_match", ""))[:120],
    ]))
