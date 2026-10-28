# -*- coding: utf-8 -*-
"""Preflight CL3c: validate 17 claim rows, 15 patches, spans, blocks, keywords."""
import json
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
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 282, len(reg)
assert reg_text.splitlines()[2] == "# total: 282", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0282"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(283, 300)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 15

KEYWORDS = {
    "claim-0283": ["匠人", "小农阶层", "地主阶层", "百家争鸣"],
    "claim-0284": ["最早出现冶铁术", "商代", "春秋、战国之交", "生铁与块炼铁同时发展"],
    "claim-0285": ["器模上雕纹", "印纹阶段", "错金银", "错铜"],
    "claim-0286": ["胎骨厚重", "木片卷粘胎", "夹纻胎", "扣器"],
    "claim-0287": ["男耕女织", "自然经济", "通用货币"],
    "claim-0288": ["数十匹", "千余匹"],
    "claim-0289": ["描彩漆", "镶嵌", "针刻", "气韵生动"],
    "claim-0290": ["曲裾深衣", "深衣成熟", "衣作绣，锦为沿"],
    "claim-0291": ["156", "7个单元", "提花机"],
    "claim-0292": ["7个工官", "画缋", "钟人染羽", "梁人掌染草"],
    "claim-0293": ["一器而工聚焉者，车为多", "车有六等之数", "6种不同的劳动部门"],
    "claim-0294": ["跽坐", "低矮的形制", "延续至汉代"],
    "claim-0295": ["越王勾践剑", "蓝色琉璃", "错金鸟篆", "十余层纸"],
    "claim-0296": ["用与美", "文与质", "多元审美观念"],
    "claim-0297": ["齐国官书", "稷下学宫", "春秋末至战国初年", "河间献王刘德"],
    "claim-0298": ["侯马、邯郸", "大致相同", "深远影响"],
    "claim-0299": ["《墨经》", "杠杆原理", "滑轮和斜面", "重要古籍"],
}

PATCH_KEYWORDS = {
    "claim-0072": ["生铁柔化", "早于欧洲1700年以上"],
    "claim-0083": ["墨家", "荀子", "韩非子"],
    "claim-0084": ["上衣下裳", "深衣", "纹样寓意"],
    "claim-0076": ["钟鸣鼎食", "失去祭祀和礼器的特性"],
    "claim-0085": ["营国制度", "持续而深刻影响"],
    "claim-0086": ["车战的黄金时代", "千辆以上"],
    "claim-0087": ["车有六等之数", "六尺有六寸", "1.3米"],
    "claim-0093": ["文质兼备", "质胜文则野"],
    "claim-0094": ["利于人谓之巧", "器完而不饰", "质真而素朴"],
    "claim-0095": ["有之以为利，无之以为用", "空间观念"],
    "claim-0097": ["去淫丽", "去智巧", "以文害用"],
    "claim-0098": ["第一部手工艺专著", "30项"],
    "claim-0099": ["金有六齐", "现代金属学原理"],
    "claim-0100": ["天有时，地有气", "材有美，工有巧", "辩证唯物论"],
    "claim-0101": ["材美工巧", "基本法则"],
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
    for p in row["supported_by"]:
        assert (ROOT / p).is_file(), (cid, p)
    used_candidates.add(src["candidate_id"])

# Patch validation.
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

# no_delta candidate.
nd = cand[DOC + ":cand-02-114"]
assert nd["state"] == "needs_evidence", nd["state"]
assert nd["candidate_type"] == "claim"
print("no_delta_candidate", nd["candidate_id"], nd["payload"].get("claim_scope"))

assert len(used_candidates) == 32, len(used_candidates)
assert len(patched) == 15, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 1027 <= r["payload"]["source_span"]["line_start"] <= 1588]
print("chapter_candidates", len(chapter))
assert len(chapter) == 33, len(chapter)
assert len(used_candidates) + 1 == 33

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
