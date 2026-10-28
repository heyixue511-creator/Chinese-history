# -*- coding: utf-8 -*-
import collections
import json

LEDGER = r"D:/中国设计史研究/03-processing/2009-zhaonong-zhongguo-yishu-shejishi/candidate-ledger.jsonl"
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
st = collections.Counter()
typ = collections.Counter()
for line in open(LEDGER, encoding="utf-8"):
    d = json.loads(line)
    cid = d["candidate_id"]
    doc = cid.split(":")[0]
    if doc != DOC:
        continue
    st[d["state"]] += 1
    if d.get("candidate_type") == "claim" or d.get("type") == "claim":
        typ[d["state"]] += 1
print("doc_states", dict(st))
print("doc_claim_states", dict(typ))
