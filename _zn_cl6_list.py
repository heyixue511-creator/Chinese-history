# -*- coding: utf-8 -*-
"""List candidates for the Wei-Jin chapter (L2065-L2460)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
rows = [r for r in index if r["candidate_id"].startswith(DOC + ":")
        and r["candidate_type"] == "claim"
        and 2065 <= r["payload"]["source_span"]["line_start"] <= 2460]
rows.sort(key=lambda r: r["payload"]["source_span"]["line_start"])
print("count", len(rows))
for r in rows:
    sp = r["payload"]["source_span"]
    print(r["candidate_id"].split(":")[1], sp["line_start"], sp["line_end"],
          sp["block_ids"], r["payload"]["claim_scope"], r["state"],
          "|", r["payload"]["claim_text"][:110])
print("--- headings ---")
lines = (ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md").read_text(encoding="utf-8").splitlines()
for i in range(2065, 2461):
    l = lines[i - 1]
    if l.startswith("#"):
        print(i, l[:80])
