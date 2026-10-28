# -*- coding: utf-8 -*-
"""Stats for CL3d summary."""
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"

lines = SRC.read_text(encoding="utf-8").splitlines()
print("source_lines", len(lines))
rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
new = rows[299:]
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]

cands = [r for r in index if r["candidate_id"].startswith(DOC + ":")
         and r["candidate_type"] == "claim"
         and 1609 <= r["payload"]["source_span"]["line_start"] <= 2064]
spans = [r["payload"]["source_span"] for r in cands]
print("candidates", len(cands))
print("cand_span_sum", sum(s["line_end"] - s["line_start"] + 1 for s in spans))
covered = set()
for s in spans:
    covered.update(range(s["line_start"], s["line_end"] + 1))
print("cand_span_dedup", len(covered))
print("new_span_sum", sum(r["source"]["source_span"]["line_end"] - r["source"]["source_span"]["line_start"] + 1 for r in new))
newcov = set()
for r in new:
    s = r["source"]["source_span"]
    newcov.update(range(s["line_start"], s["line_end"] + 1))
print("new_span_dedup", len(newcov))

patched = []
for r in rows:
    for sp in r["source"].get("corroborating_spans") or []:
        if str(sp.get("candidate_id", "")).startswith(DOC + ":"):
            patched.append((r["claim_id"], sp))
print("patch_spans", len(patched))
print("patch_span_sum", sum(sp["line_end"] - sp["line_start"] + 1 for _, sp in patched))
pcov = set()
for _, sp in patched:
    pcov.update(range(sp["line_start"], sp["line_end"] + 1))
print("patch_span_dedup", len(pcov))
for claim_id, sp in patched:
    print("PATCH", claim_id, sp["candidate_id"].split(":")[1], sp["line_start"], sp["line_end"],
          sp["span_kind"], sp["block_ids"])

paths = [p for r in new for p in r["supported_by"]]
print("links", len(paths), "distinct", len(set(paths)))
print("by_type", dict(Counter(p.split("/")[1] for p in paths)))
print("distinct_by_type", dict(Counter(p.split("/")[1] for p in set(paths))))
print("freq", Counter(paths).most_common())

heads = [(i + 1, l) for i, l in enumerate(lines) if l.startswith("# ")]
print("headings", [h for h in heads if 1500 <= h[0] <= 2100])
