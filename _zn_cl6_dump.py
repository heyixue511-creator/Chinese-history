# -*- coding: utf-8 -*-
"""Dump full payloads for Wei-Jin chapter candidates."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
ids = """cand-04-32 cand-04-33 cand-04-34 cand-04-36 cand-04-44 cand-04-48
cand-04-51 cand-04-78 cand-04-53 cand-04-57 cand-05-86 cand-05-136 cand-05-137""".split()
by = {r["candidate_id"].split(":")[1]: r for r in index
      if r["candidate_id"].startswith(DOC + ":")}
for cid in ids:
    r = by[cid]
    print("=" * 70)
    print(cid, r["state"], json.dumps(r["payload"], ensure_ascii=False, indent=1))
