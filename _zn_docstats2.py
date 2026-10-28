# -*- coding: utf-8 -*-
import collections
import json

CAND = r"D:/中国设计史研究/06-runtime/state/candidate-index.jsonl"
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
st = collections.Counter()
for line in open(CAND, encoding="utf-8"):
    d = json.loads(line)
    cid = d.get("candidate_id", "")
    if cid.split(":")[0] != DOC:
        continue
    st[("claim" if d.get("candidate_type") == "claim" else "unit", d["state"])] += 1
print(sorted(st.items()))
