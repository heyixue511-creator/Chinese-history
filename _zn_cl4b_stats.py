# -*- coding: utf-8 -*-
"""Compute CL3c coverage and support statistics for summary.md."""
import json
from collections import Counter, OrderedDict
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl4b_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl4b_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
print("source_lines", len(lines))
rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
new = rows[282:]

print("\n== headings 1020-1615 ==")
for i in range(1020, 1616):
    t = lines[i - 1]
    if t.startswith("#"):
        print(i, t)

print("\n== chapter candidates by section ==")
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in index}
heads = [(n, lines[n - 1]) for n in range(1027, 1607) if lines[n - 1].startswith("#")]
print("heads", heads)


def section_of(n):
    cur = "章首"
    for ln, t in heads:
        if ln <= n:
            cur = t
    return cur


chapter = [r for r in index
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and 1027 <= r["payload"]["source_span"]["line_start"] <= 1588]
used = [r for r in chapter if r["candidate_id"] in
        {x["source"]["candidate_id"] for x in ROWS} | {p["candidate_id"] for p in PATCH}
        | {DOC + ":cand-02-114"}]
print("chapter", len(chapter), "used", len(used))
dist = OrderedDict()
for r in sorted(chapter, key=lambda r: r["payload"]["source_span"]["line_start"]):
    s = section_of(r["payload"]["source_span"]["line_start"])
    dist.setdefault(s, []).append(r["candidate_id"].split(":")[1])
for s, ids in dist.items():
    print(len(ids), s, ids)


def span_stats(spans):
    total = sum(b - a + 1 for a, b in spans)
    union = set()
    for a, b in spans:
        union.update(range(a, b + 1))
    return total, len(union), (min(a for a, b in spans), max(b for a, b in spans))


cspans = [(r["payload"]["source_span"]["line_start"], r["payload"]["source_span"]["line_end"])
          for r in used]
print("\ncandidate spans", span_stats(cspans))
nspans = [(r["source"]["source_span"]["line_start"], r["source"]["source_span"]["line_end"])
          for r in new]
print("new claim spans", span_stats(nspans))
pspans = [(p["corroborating_span"]["line_start"], p["corroborating_span"]["line_end"])
          for p in PATCH]
print("patch spans", span_stats(pspans))

print("\n== support distribution ==")
top = Counter()
for r in new:
    for p in r["supported_by"]:
        top[p.split("/")[0]] += 1
print("by_link", dict(top))
kuc = Counter()
for r in new:
    for p in set(r["supported_by"]):
        kuc[p.split("/")[0]] += 1
print("by_distinct_link", dict(kuc))
paths = Counter(p for r in new for p in r["supported_by"])
print("top_paths", paths.most_common(8))

print("\n== new claims ==")
for r in new:
    sp = r["source"]["source_span"]
    print("|".join([
        r["claim_id"], r["claim_type"], r["confidence"],
        f'{sp["line_start"]}-{sp["line_end"]}', sp["span_kind"],
        r["source"]["candidate_id"], str(len(r["supported_by"])),
        r["statement_zh"][:120],
    ]))

print("\n== manifest ==")
man = json.loads((ROOT / "06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl3c/manifest.json"
                  ).read_text(encoding="utf-8"))
for k in ("before_bytes", "after_bytes", "before_sha256", "after_sha256",
          "scope_spans", "baseline", "result"):
    print(k, man[k])
