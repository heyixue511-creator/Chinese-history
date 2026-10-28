# -*- coding: utf-8 -*-
import collections
import json
import os

ROOT = r"D:/中国设计史研究"
SRC = ROOT + "/03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
LEDGER = ROOT + "/03-processing/2009-zhaonong-zhongguo-yishu-shejishi/candidate-ledger.jsonl"

rows = json.load(open(ROOT + "/_zn_zn6a_rows.json", encoding="utf-8"))
paths = [p.replace(os.sep, "/") for r in rows for p in r["supported_by"]]
print("links_by_type", dict(collections.Counter(p.split("/")[2] for p in paths)))
cnt = collections.Counter(paths)
print("multi", {k: v for k, v in sorted(cnt.items()) if v > 1})

cands = {}
for line in open(LEDGER, encoding="utf-8"):
    d = json.loads(line)
    cands[d["candidate_id"]] = d
diffs = []
for r in rows:
    cid = r["source"]["candidate_id"]
    got = cands[cid]["payload"]["claim_scope"]
    if got != r["claim_type"]:
        diffs.append((r["claim_id"], cid, got, r["claim_type"]))
print("type_map", diffs)

lines = open(SRC, encoding="utf-8").read().split("\n")
for n in (4184, 4200, 4423, 4554, 4604, 4608, 4728):
    print("L%d: %s" % (n, lines[n - 1].strip()[:160]))
