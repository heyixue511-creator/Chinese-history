# -*- coding: utf-8 -*-
"""Search existing claims (2004/2009) for overlap with the Tang chapter."""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
DOCS = {"2004-gaofeng-zhongguo-shejishi", "2009-xiayanjing-zhongguo-shejishi"}

keywords = sys.argv[1:]
rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
hits = []
for r in rows:
    if r["source"]["doc_id"] not in DOCS:
        continue
    text = r["statement_zh"] + " " + (r["discussion_notes"] or "")
    matched = [k for k in keywords if k in text]
    if matched:
        hits.append((r["claim_id"], r["source"]["doc_id"].split("-")[0], r["claim_type"],
                     matched, r["statement_zh"]))
print("hits", len(hits))
for cid, doc, ctype, matched, text in hits:
    print(f"- {cid} [{doc}] {ctype} match={matched}")
    print("   ", text[:240])
