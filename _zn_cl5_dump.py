# -*- coding: utf-8 -*-
"""Dump full payloads for the Qin-Han chapter candidates."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
ids = """cand-03-85 cand-03-88 cand-03-91 cand-03-94 cand-03-95 cand-03-96
cand-03-102 cand-03-103 cand-03-105 cand-03-112 cand-03-114 cand-03-118
cand-03-120 cand-03-122 cand-04-01 cand-04-07 cand-04-09 cand-04-11
cand-04-13 cand-04-76 cand-04-20 cand-04-21 cand-04-27 cand-04-77 cand-04-31""".split()
by = {r["candidate_id"].split(":")[1]: r for r in index
      if r["candidate_id"].startswith(DOC + ":")}
for cid in ids:
    r = by[cid]
    print("=" * 70)
    print(cid, r["state"], json.dumps(r["payload"], ensure_ascii=False, indent=1))
