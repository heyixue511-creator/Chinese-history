"""Merge chapter-4 decision parts and assert exact 79-candidate coverage."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
parts = []
for name in ("_zn_decisions_ch4_a.json", "_zn_decisions_ch4_b1.json", "_zn_decisions_ch4_b2.json"):
    parts.extend(json.loads((ROOT / name).read_text(encoding="utf-8")))

rows = json.loads((ROOT / "_zn_ch4_rows.json").read_text(encoding="utf-8"))
pending = {r["candidate_id"] for r in rows}
seen = [d["cid"] for d in parts]
assert len(seen) == len(set(seen)), "duplicate cid in decisions"
missing = pending - set(seen)
extra = set(seen) - pending
assert not missing, f"missing: {sorted(missing)}"
assert not extra, f"extra: {sorted(extra)}"
assert len(parts) == 79, len(parts)

from collections import Counter
print(Counter(d["action"] for d in parts))
tgt = [d["target"] for d in parts if d["action"] in ("create", "update")]
assert len(tgt) == len(set(tgt)), "duplicate create/update target"

cfg = {
    "doc": "2009-zhaonong-zhongguo-yishu-shejishi",
    "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    "rules": [
        "第四章 79 条 unit 候选逐条语义复读后分流为 create 64 / update 6 / rejected 9；cand-04-* 与 cand-05-* 混编，章节归属以 payload.source_span.chapter 为准。",
        "新建条目统一 consensus=tentative、evidence_status=source_backed、source_count=1、version=1；更新按实际并入来源数提高 source_count，same-book 跨度不增 source_count。",
        "原文错字、内部矛盾与分页拼接照录并标注，不径改；只有一句话或一句半的材料 confidence 记 low，不据图补形制。",
        "同一实体命中多条候选时只保留一条 canonical（create 或 update），其余走 rejected 并指向同一目标文件，不重复建 KU。",
    ],
    "decisions": parts,
    "notes": "第六章章内混编的 cand-05-* 候选（起绒锦、冠制、禅衣、履、透光镜、卧褥香炉、西京杂记、地动仪、蔡侯纸、司南、马王堆帛地图、动物形灯）与 cand-04-* 同批处理，不另立批次。",
}
out = ROOT / "_zn_decisions_ch4.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", out, "decisions", len(parts))
