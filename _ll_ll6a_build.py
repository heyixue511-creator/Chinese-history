# -*- coding: utf-8 -*-
"""Build 李立新 2011 claim rows, batch ll6a (后记, 2 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
SRC = "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"
DATE = "2026-10-27"
CH = "后记（成书与答辩）"

MAP = ROOT / "03-processing/2011-lilixin-zhongguo-sheji-yishu-shilun/source-map.jsonl"
BLOCKS = []
for line in MAP.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    d = json.loads(line)
    BLOCKS.append((d["block_id"], d["line_start"], d["line_end"]))


def blocks(start, end):
    return [b for b, s, e in BLOCKS if s <= end and e >= start]


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(claim_id, cand, ctype, zh, en, supported, note, start, end, key_lines, section):
    for p in supported:
        assert (ROOT / p).is_file(), p
    return {
        "claim_id": claim_id,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": {
            "doc_id": DOC,
            "source_file": SRC,
            "source_span": {
                "line_start": start,
                "line_end": end,
                "span_kind": "line" if start == end else "bounded",
                "key_lines": key_lines,
                "block_ids": blocks(start, end),
                "chapter": CH,
                "section": section,
            },
            "candidate_id": DOC + ":" + cand,
        },
        "confidence": "medium",
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    }


rows = []

rows.append(C(
    "claim-1241", "cand-06-06", "factual_claim",
    "李立新自述，本书是在其博士论文《造物之迹——中国设计艺术史引论》的基础上修改完成的。",
    "Li Lixin states that the present book was revised and completed on the basis of his doctoral dissertation, Zaowu Zhi Ji: An Introduction to the History of Chinese Design Art.",
    ["04-knowledge/units/publications/zaowu-zhi-ji.md", "04-knowledge/units/persons/li-lixin.md"],
    "断言语义取 L2444。原文为后记首段的作者自述，明确交代本书的文本来源；claim 保留“自述”归属，不把它写成第三方书目考证结论。",
    2444, 2444, [2444], "后记（成书与答辩）"))

rows.append(C(
    "claim-1242", "cand-06-07", "factual_claim",
    "李立新的博士论文于2002年6月15日在东南大学艺术学系通过答辩。",
    "Li Lixin's doctoral dissertation was defended and passed at the Department of Art Studies, Southeast University, on 15 June 2002.",
    ["04-knowledge/units/events/li-lixin-doctoral-defense-2002.md", "04-knowledge/units/persons/li-lixin.md"],
    "断言语义取 L2448。原文同时列出同行评审与答辩委员会名单；claim 只写日期、单位与通过结果，不推断评审意见或答辩过程细节。",
    2448, 2448, [2448], "后记（成书与答辩）"))

out = ROOT / "_ll_ll6a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("rows", len(rows))
print("links", sum(len(r["supported_by"]) for r in rows))
print("distinct", len({x for r in rows for x in r["supported_by"]}))
from collections import Counter
print("types", dict(Counter(r["claim_type"] for r in rows)))
