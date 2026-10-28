# -*- coding: utf-8 -*-
"""List 2016 candidates for the Qin-Han chapter and nearby headings."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"

lines = SRC.read_text(encoding="utf-8").splitlines()
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
rows = [r for r in index
        if r["candidate_type"] == "claim"
        and r["candidate_id"].startswith(DOC + ":")
        and r["state"] == "needs_evidence"]
rows.sort(key=lambda r: r["payload"]["source_span"]["line_start"])

print("headings 1600-2200:")
for i in range(1600, 2201):
    if lines[i - 1].startswith("# "):
        print(i, lines[i - 1])

print("\nremaining 2016 candidates from 1609:")
n = 0
for r in rows:
    sp = r["payload"]["source_span"]
    if sp["line_start"] < 1609:
        continue
    n += 1
    print(json.dumps({
        "candidate_id": r["candidate_id"],
        "span": [sp["line_start"], sp["line_end"]],
        "scope": r["payload"].get("claim_scope"),
        "match": r["payload"].get("knowledge_match"),
        "text": r["payload"].get("claim_text"),
    }, ensure_ascii=False))
print("count_from_1609", n)
