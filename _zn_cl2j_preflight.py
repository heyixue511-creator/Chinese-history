# -*- coding: utf-8 -*-
"""Preflight CL2j rows against the live registry and candidate index."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
SRC = ROOT / "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"

text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
print("registry", len(rows), "header", text.splitlines()[2])
assert len(rows) == 246
assert "# total: 246" in text
assert rows[-1]["claim_id"] == "claim-0246"

new = json.loads((ROOT / "_zn_claim_xyj09j_rows.json").read_text(encoding="utf-8"))
assert len(new) == 13
assert [r["claim_id"] for r in new] == ["claim-%04d" % i for i in range(247, 260)]
assert {r["source"]["candidate_id"] for r in new} == {
    DOC + ":cand-" + n for n in
    ["06-67", "06-68", "06-69", "06-70", "06-71", "06-72", "06-73",
     "07-10", "07-18", "07-22", "07-23", "07-24", "07-25"]
}

index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
by = {r["candidate_id"]: r for r in index}
src_lines = SRC.read_text(encoding="utf-8").splitlines()
bad = []
for row in new:
    cid = row["source"]["candidate_id"]
    sp = row["source"]["source_span"]
    c = by.get(cid)
    if not c:
        bad.append((cid, "missing candidate"))
        continue
    if c["state"] != "needs_evidence" or c["candidate_type"] != "claim":
        bad.append((cid, c["state"], c["candidate_type"]))
    csp = (c.get("payload") or {}).get("source_span") or {}
    if not (csp["line_start"] <= sp["line_start"] <= sp["line_end"] <= csp["line_end"]):
        bad.append((cid, "span", csp, sp["line_start"], sp["line_end"]))
    cblocks = set(csp.get("block_ids") or [])
    if not set(sp["block_ids"]) <= cblocks:
        bad.append((cid, "blocks", sorted(cblocks), sp["block_ids"]))
    for k in sp["key_lines"]:
        if not (1 <= k <= len(src_lines)) or len(src_lines[k - 1].strip()) < 10:
            bad.append((cid, "empty key line", k))
    if row["claim_id"] not in {r["claim_id"] for r in rows}:
        pass
print("bad", len(bad))
for item in bad:
    print("BAD", item)
assert not bad
print("candidate_states", {s: sum(1 for r in index if r["state"] == s) for s in
      sorted({r["state"] for r in index})})
