# -*- coding: utf-8 -*-
"""List claim candidates in a line range of the 2016 source."""
import json
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"

start = int(sys.argv[1])
end = int(sys.argv[2])
lines = SRC.read_text(encoding="utf-8").splitlines()
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
rows = [r for r in index
        if r["candidate_type"] == "claim"
        and r["candidate_id"].startswith(DOC + ":")
        and r["state"] == "needs_evidence"
        and start <= r["payload"]["source_span"]["line_start"] <= end]
rows.sort(key=lambda r: (r["payload"]["source_span"]["line_start"],
                         r["candidate_id"]))
print("count", len(rows))
for r in rows:
    sp = r["payload"]["source_span"]
    print("-", r["candidate_id"].split(":")[1], f"L{sp['line_start']}-{sp['line_end']}",
          sp.get("span_kind"), sp.get("block_ids"))
    refs = [x.rsplit("#", 1)[-1] for x in r.get("evidence_refs") or []]
    print("    scope:", r["payload"].get("claim_scope"), "| refs:", ",".join(refs))
    print("    text:", r["payload"].get("claim_text", "")[:260])
    print("    note:", (r["payload"].get("support_note") or "")[:160])
print("keys", sorted(rows[0]["payload"].keys()) if rows else [])
