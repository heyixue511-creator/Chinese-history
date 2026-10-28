# -*- coding: utf-8 -*-
"""Preflight CL10a: validate 15 rows, 3 patches, spans, blocks, keywords, scope."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl13_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl13_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 378, len(reg)
assert reg_text.splitlines()[2] == "# total: 378", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0378"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(379, 394)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 3
assert len({p["claim_id"] for p in PATCH}) == 3
assert {p["claim_id"] for p in PATCH} == {"claim-0255", "claim-0256", "claim-0257"}

KEYWORDS = {
    "claim-0379": ["1957年", "7月22日", "保护、发展和提高", "适用、经济、美观"],
    "claim-0380": ["1957年", "7月", "江苏省人民政府", "云锦研究所", "第一家工艺美术研究机构"],
    "claim-0381": ["1994年", "10月下旬", "全国技术美学研讨会", "第一次"],
    "claim-0382": ["1999年", "11月20日", "中央工艺美术学院", "清华大学美术学院"],
    "claim-0383": ["2000年", "第一条生态景观大道"],
    "claim-0384": ["道", "器", "亘古不变"],
    "claim-0385": ["6大类30个工种", "制车", "兵器", "礼器", "钟磬", "练染"],
    "claim-0386": ["墨子·节用", "节用", "日用器物"],
    "claim-0387": ["唐六典", "最早的一部行政法典"],
    "claim-0388": ["天工开物", "第一部关于农业和手工业生产的综合性著作"],
    "claim-0389": ["长物志", "以用为本", "物质的实用性"],
    "claim-0390": ["髹饰录", "现存唯一的古代漆工专著"],
    "claim-0391": ["雍正十二年", "仅有的两部古籍"],
    "claim-0392": ["原始农业生产器具设计", "漆工艺的发展与特色漆器品种",
                   "唐代设计理论述要", "明清贸易瓷的历史演变与特色",
                   "社会主义建设时期的工业产品设计"],
    "claim-0393": ["2013 年 10 月", "江苏省级重点立项教材", "全省高校设计专业用书"],
}

PATCH_KEYWORDS = {
    "claim-0255": ["工艺美术参考", "工业设计教育"],
    "claim-0256": ["232.7亿美元", "世界第一位"],
    "claim-0257": ["1998年", "普通高等学校本科专业目录", "艺术设计专业"],
}

used_candidates = set()
bad = 0
for row in ROWS:
    cid = row["claim_id"]
    src = row["source"]
    c = cand[src["candidate_id"]]
    assert c["state"] == "needs_evidence", (cid, c["state"])
    assert c["candidate_type"] == "claim", cid
    cspan = c["payload"]["source_span"]
    span = src["source_span"]
    assert cspan["line_start"] <= span["line_start"] <= span["line_end"] <= cspan["line_end"], (
        cid, cspan, span)
    assert set(span["block_ids"]) <= set(cspan["block_ids"]), (cid, span["block_ids"], cspan["block_ids"])
    assert span["key_lines"] and all(span["line_start"] <= n <= span["line_end"] for n in span["key_lines"]), cid
    assert span["span_kind"] in {"line", "contiguous", "bounded"}, cid
    text = "\n".join(lines[n - 1] for n in span["key_lines"])
    missing = [k for k in KEYWORDS[cid] if k not in text]
    if missing:
        bad += 1
        print("MISSING_KEYWORD", cid, missing, text[:200])
    assert '"' not in row["statement_zh"], cid
    assert '"' not in row["discussion_notes"], cid
    assert row["consensus"] == "tentative" and row["review_status"] == "source_backed"
    assert row["created"] == "2026-10-27" and row["updated"] == "2026-10-27"
    assert row["confidence"] == "medium", cid
    for p in row["supported_by"]:
        assert (ROOT / p).is_file(), (cid, p)
    used_candidates.add(src["candidate_id"])
    for mc in src.get("merged_candidate_ids") or []:
        m = cand[mc]
        assert m["state"] == "needs_evidence", (cid, mc, m["state"])
        used_candidates.add(mc)

reg_by_id = {r["claim_id"]: r for r in reg}
patched = set()
for p in PATCH:
    claim_id = p["claim_id"]
    assert claim_id in reg_by_id, claim_id
    claim = reg_by_id[claim_id]
    assert claim["source"]["doc_id"] == "2009-xiayanjing-zhongguo-shejishi", claim_id
    assert not claim["source"].get("merged_candidate_ids"), claim_id
    assert not claim["source"].get("corroborating_spans"), claim_id
    cid = p["candidate_id"]
    c = cand[cid]
    assert c["state"] == "needs_evidence", (cid, c["state"])
    assert c["candidate_type"] == "claim", cid
    cspan = c["payload"]["source_span"]
    span = p["corroborating_span"]
    assert cspan["line_start"] <= span["line_start"] <= span["line_end"] <= cspan["line_end"], (
        cid, cspan, span)
    assert set(span["block_ids"]) <= set(cspan["block_ids"]), (cid, span["block_ids"], cspan["block_ids"])
    assert span["key_lines"] and all(span["line_start"] <= n <= span["line_end"] for n in span["key_lines"]), cid
    text = "\n".join(lines[n - 1] for n in span["key_lines"])
    missing = [k for k in PATCH_KEYWORDS[claim_id] if k not in text]
    if missing:
        bad += 1
        print("PATCH_MISSING_KEYWORD", claim_id, cid, missing, text[:200])
    assert text.strip(), cid
    used_candidates.add(cid)
    patched.add(claim_id)

assert len(used_candidates) == 18, len(used_candidates)
assert len(patched) == 3, len(patched)

remaining = [r for r in cand_rows
             if r["candidate_type"] == "claim"
             and r["candidate_id"].startswith(DOC + ":")
             and r["state"] == "needs_evidence"]
print("remaining_2016", len(remaining))
assert len(remaining) == 18, len(remaining)
assert used_candidates == {r["candidate_id"] for r in remaining}
# scope must sit in the tail sections: timeline, literature index, postscript
assert all(5545 <= r["payload"]["source_span"]["line_start"] <= 6538 for r in remaining)

print("registry", len(reg), "header", reg_text.splitlines()[2])
print("rows", len(ROWS), "patches", len(PATCH), "patched_claims", len(patched))
print("used_candidates", len(used_candidates), "bad", bad)
print("candidate_states", {s: sum(1 for r in cand_rows if r["state"] == s)
                           for s in sorted({r["state"] for r in cand_rows})})
print("2016_needs", sum(1 for r in cand_rows
                        if r["candidate_type"] == "claim"
                        and r["candidate_id"].startswith(DOC + ":")
                        and r["state"] == "needs_evidence"))
assert bad == 0
