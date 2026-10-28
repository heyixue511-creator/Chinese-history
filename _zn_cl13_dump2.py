# -*- coding: utf-8 -*-
"""Dump full payloads of CL10a candidates."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
IDS = ["cand-10-62", "cand-10-61", "cand-11-106", "cand-11-108", "cand-11-110"]

rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
sel = {r["candidate_id"]: r for r in rows}
for suffix in IDS:
    r = sel[DOC + ":" + suffix]
    print(json.dumps(r, ensure_ascii=False, indent=1))
    print("=" * 60)
