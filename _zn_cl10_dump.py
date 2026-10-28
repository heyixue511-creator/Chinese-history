# -*- coding: utf-8 -*-
"""Dump full payloads of the 21 Ming-Qing claim candidates."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"

WANT = ["cand-07-72", "cand-07-101", "cand-07-74", "cand-07-75", "cand-07-76",
        "cand-07-93", "cand-08-95", "cand-08-96", "cand-08-97", "cand-08-100",
        "cand-08-101", "cand-08-102", "cand-08-99", "cand-08-103", "cand-08-104",
        "cand-08-105", "cand-08-106", "cand-08-107", "cand-08-108", "cand-08-98",
        "cand-08-109"]
ids = {DOC + ":" + w for w in WANT}
rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows if r["candidate_id"] in ids]
print("count", len(sel))
for r in sel:
    print(json.dumps({
        "id": r["candidate_id"].split(":")[1],
        "state": r["state"],
        "payload": r["payload"],
    }, ensure_ascii=False, indent=1))
    print("=" * 60)
