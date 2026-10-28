# -*- coding: utf-8 -*-
"""Tighten two CL2j statements to the source wording, then refresh artifacts."""
import hashlib
import json
import os
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
PKG = ROOT / "06-runtime/automation/2026-10-27-2009xiayanjing-claims-batch-cl2j"
DATE = "2026-10-27"


def sha256_text(text: str) -> str:
    data = text.replace("\r\n", "\n").encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


rows = json.loads((ROOT / "_zn_claim_xyj09j_rows.json").read_text(encoding="utf-8"))
by_id = {r["claim_id"]: r for r in rows}

by_id["claim-0251"]["statement_zh"] = (
    "夏燕靖指出，“文革”时期书籍装帧成为当时非常突出的一项设计内容，"
    "几乎所有图书的封面设计都与政治挂钩，主要参照毛泽东著作和马恩列斯著作的版式设计；"
    "《红旗》《解放军文艺》是当时期刊装帧设计的代表，“红、光、亮”审美原则主宰了当时的书籍设计，"
    "书籍装帧呈现空洞、单调、贫乏的面貌。"
)
by_id["claim-0251"]["statement_en"] = (
    "Xia Yanjing points out that book binding became a particularly prominent area of design "
    "during the Cultural Revolution: almost all book covers were tied to politics and mainly "
    "followed the layouts of Mao Zedong's works and those of Marx, Engels, Lenin and Stalin; "
    "Red Flag and Liberation Army Literature and Art were representative periodical designs of "
    "the time, and the red, bright and shining aesthetic principle dominated book design, which "
    "presented an empty, monotonous and impoverished appearance."
)
by_id["claim-0251"]["discussion_notes"] = (
    "候选作 interpretation，路由 interpretive；断言取 L4358。来源的量化范围是"
    "“几乎所有图书的封面设计”，不是全部书籍装帧，本条按封面设计表述，不扩大到所有装帧要素；"
    "末句“空洞、单调、贫乏”是来源的评价性总结，保留为作者判断，不改写为可量化事实，"
    "也不单独路由 evaluative，因为断言主干是政治化装帧与审美原则的历史描述。"
)

by_id["claim-0253"]["statement_zh"] = (
    "夏燕靖认为，面向21世纪，我国现代设计仍然处于摸索之中，许多设计实践尚处在引进、"
    "学习与消化过程中；影响我国现代设计发展的核心因素仍然是科技创新与设计研发，"
    "除提高基础工业外，关键问题还在于设计教育与制造产业的需求如何形成有效接口。"
)
by_id["claim-0253"]["statement_en"] = (
    "Xia Yanjing argues that, facing the twenty-first century, China's modern design is still "
    "groping its way, and many design practices are still in the process of importation, learning "
    "and digestion; the core factor affecting the development of modern design remains technological "
    "innovation and design research and development, and, apart from strengthening basic industry, "
    "the key question is how design education and the needs of the manufacturing industry can form "
    "an effective interface."
)
by_id["claim-0253"]["discussion_notes"] = (
    "候选作 interpretation，路由 interpretive；断言取 L4456 与 L4460，记 contiguous。"
    "两关键行之间的 L4457-L4459 是“知识链接：动画”框，排录插入正文，故首句“工业产品”"
    "与次句“设计，从电器到手机”被切断；本条只取框前后的论断，不把动画内容并入。"
    "来源在关键问题前有“除了提高基础工业外”的限定，本条保留，不把设计教育写成唯一因素；"
    "设计教育与制造产业接口的判断无统计支撑，记 medium。"
)

# The chronology entries state only the month or “year-end”; include the
# year heading in the bounded span so the statement's year is source-visible.
for cid, start, end in (
    ("claim-0255", 4788, 4790),
    ("claim-0256", 4952, 4960),
    ("claim-0257", 5002, 5016),
):
    sp = by_id[cid]["source"]["source_span"]
    sp["line_start"] = start
    sp["line_end"] = end
    sp["span_kind"] = "bounded"
    sp["key_lines"] = [start, end]
    by_id[cid]["discussion_notes"] += (
        " 断言跨度上括年份小节标题，记为 bounded，便于从源文直接复核年份。"
    )

(ROOT / "_zn_claim_xyj09j_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

registry_rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
assert len(registry_rows) == 259
index = {r["claim_id"]: i for i, r in enumerate(registry_rows)}
patched = ("claim-0251", "claim-0253", "claim-0255", "claim-0256", "claim-0257")
for cid in patched:
    i = index[cid]
    registry_rows[i]["statement_zh"] = by_id[cid]["statement_zh"]
    registry_rows[i]["statement_en"] = by_id[cid]["statement_en"]
    registry_rows[i]["source"]["source_span"] = by_id[cid]["source"]["source_span"]
    registry_rows[i]["discussion_notes"] = by_id[cid]["discussion_notes"]
    registry_rows[i]["updated"] = DATE

header = "# Claim Registry v1.0\n# generated: 2026-10-27\n# total: 259\n"
text = header + yaml.safe_dump(
    registry_rows, allow_unicode=True, sort_keys=False,
    default_flow_style=False, width=100000,
)
assert text.count("\n- claim_id:") == 259
write_atomic(REG, text)

(PKG / "claim-rows.jsonl").write_text(
    "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows),
    encoding="utf-8", newline="\n",
)

apply_rows = []
for row in rows:
    canonical = json.dumps(row, ensure_ascii=False, sort_keys=True)
    apply_rows.append({
        "action": "claim_create",
        "claim_id": row["claim_id"],
        "candidate_ids": [row["source"]["candidate_id"]],
        "target_ref": f"claim/{row['claim_id']}",
        "after_sha256": sha256_text(canonical),
        "bytes": len(canonical.encode("utf-8")),
        "before": None,
        "note": "新建 claim-registry 行；来源 " + row["source"]["source_file"],
    })
(PKG / "apply-plan.jsonl").write_text(
    "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in apply_rows),
    encoding="utf-8", newline="\n",
)

manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
manifest["after_sha256"] = sha256_text(text)
manifest["after_bytes"] = len(text.encode("utf-8"))
manifest["claim_rows"] = len(rows)
(PKG / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n",
)

print(json.dumps({
    "after_sha256": manifest["after_sha256"],
    "after_bytes": manifest["after_bytes"],
    "patched": list(patched),
}, ensure_ascii=False))
