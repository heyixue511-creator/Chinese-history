# -*- coding: utf-8 -*-
import json

LEDGER = r"D:/中国设计史研究/03-processing/2009-zhaonong-zhongguo-yishu-shejishi/candidate-ledger.jsonl"
out = []
for line in open(LEDGER, encoding="utf-8"):
    d = json.loads(line)
    if d.get("state") != "needs_evidence":
        continue
    p = d.get("payload", {})
    if "claim_scope" not in p:
        continue
    sp = p.get("source_span") or {}
    ls = sp.get("line_start")
    le = sp.get("line_end")
    if ls is None or le is None:
        continue
    if 4942 <= ls <= 5824 and 4942 <= le <= 5824:
        out.append((d["candidate_id"], p.get("claim_scope"), ls, le, p.get("claim_text", ""), p.get("support_note", "")))
print("count", len(out))
with open(r"D:/中国设计史研究/_zn_ch7_cands.txt", "w", encoding="utf-8", newline="\n") as f:
    for cid, sc, ls, le, txt, note in out:
        f.write("=== %s  [%s]  L%d-%d\n%s\nNOTE: %s\n" % (cid, sc, ls, le, txt, note))
