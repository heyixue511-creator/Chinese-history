# -*- coding: utf-8 -*-
"""Map line numbers to 2016 source-map block ids."""
import json
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
P = ROOT / "03-processing/2016-xiayanjing-zhongguo-yishu-shejishi-upgrade/source-map.jsonl"
rows = [json.loads(l) for l in P.read_text(encoding="utf-8").splitlines() if l.strip()]


def block_of(n):
    hits = [r for r in rows if r["line_start"] <= n <= r["line_end"]]
    return [(r["block_id"], r["line_start"], r["line_end"], r["block_type"]) for r in hits]


for a in sys.argv[1:]:
    n = int(a)
    print(n, block_of(n))
