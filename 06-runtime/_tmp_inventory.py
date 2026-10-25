# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path

led = Path("03-processing/2009-zhaonong-zhongguo-yishu-shejishi/candidate-ledger.jsonl")
rows = [json.loads(l) for l in led.read_text(encoding="utf-8").splitlines() if l.strip()]
print("rows", len(rows))
print("keys", list(rows[0].keys()))
print(json.dumps(rows[0], ensure_ascii=False, indent=1)[:2500])
print("--- type-ish keys ---")
for key in rows[0]:
    vals = Counter(str(r.get(key)) for r in rows)
    if len(vals) < 12:
        print(key, dict(vals))
