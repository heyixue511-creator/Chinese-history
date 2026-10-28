# -*- coding: utf-8 -*-
"""Build CL8a claim rows (4 new) and 8 cross-edition corroboration patches.

Chapter: 近现代史上的设计更新 (L4713-L5123), 12 claim candidates.
"""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
DATE = "2026-10-27"


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, section):
    for p in supported:
        assert (ROOT / p).is_file(), p
    return {
        "claim_id": cid,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": {
            "doc_id": DOC,
            "source_file": SRC,
            "source_span": {
                "line_start": start,
                "line_end": end,
                "span_kind": kind,
                "key_lines": key_lines,
                "block_ids": block_ids,
                "chapter": CH,
                "section": section,
            },
            "candidate_id": None,
        },
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    }


def P(claim_id, cand, start, end, kind, key_lines, block_ids, section):
    return {
        "claim_id": claim_id,
        "candidate_id": DOC + ":" + cand,
        "corroborating_span": {
            "doc_id": DOC,
            "source_file": SRC,
            "line_start": start,
            "line_end": end,
            "span_kind": kind,
            "key_lines": key_lines,
            "block_ids": block_ids,
            "chapter": CH,
            "section": section,
            "candidate_id": DOC + ":" + cand,
        },
    }


CH = "近现代史上的设计更新"
rows = []

rows.append(C(
    "claim-0360", "evaluative_claim",
    "夏燕靖评价，李有行通过染织纹样设计总结出的“限色”写生与变化方法，乃是国内设计界的首创，成为业界普遍应用的设计与教学方法。",
    "Xia Yanjing evaluates Li Youxing's “limited-colour” sketching and variation method, distilled from textile pattern design, as the first of its kind in Chinese design circles and a widely adopted design and teaching method.",
    "medium",
    ["04-knowledge/units/persons/li-youxing.md",
     "04-knowledge/units/persons/chen-zhifo.md"],
    "断言取 L4796 末句评价。陈之佛“十六字诀”、尚美图案馆、柴扉吸收唐宋瓷器图案，以及工艺美术品种类与外贸数据留在同节；本条只取李有行“限色”方法的首创性与传播范围。来源未给方法的具体步骤、采用院校或教材统计，“首创”与“普遍应用”均属作者评价。李有行生平见 persons/li-youxing，同代染织设计家见 persons/chen-zhifo。",
    4783, 4813, "line", [4796], ["b0586"],
    "1. 伴随近代手工业和对外贸易发展起来的艺术设计 / 2）以手工业与外贸发展促进艺术设计行业的进步"))

rows.append(C(
    "claim-0361", "factual_claim",
    "夏燕靖指出，1901-1911年间全国兴办的织布手工工场如雨后春笋般涌现，计有新设织布工场300余家，江苏常州、常熟与广东广州、佛山等地涌现大批采用新式织机的手工工场，是近代棉织业发展的黄金时代；同期洋纱、洋布挤占土纱、土布市场，导致土纱、土布织业逐步解体。",
    "Xia Yanjing notes that between 1901 and 1911 more than 300 weaving workshops were newly established across China, concentrated in Changzhou and Changshu (Jiangsu) and Guangzhou and Foshan (Guangdong), marking a golden age of modern cotton weaving; meanwhile imported yarn and cloth squeezed out homespun yarn and cloth, gradually breaking up the indigenous spinning and weaving industry.",
    "medium",
    ["04-knowledge/units/terms/yangbu.md",
     "04-knowledge/units/places/guangzhou.md"],
    "断言合并 L4833 的工场数量、地区分布与市场后果三层。20 世纪初手拉织布机与脚踏铁木织机的引进、洋经土纬到洋经洋纬的替代过程留在同段；“黄金时代”为作者概括。来源未给 300 余家工场的资本、织机台数或产量统计。洋布见 terms/yangbu，广州口岸见 places/guangzhou。",
    4828, 4834, "line", [4833], ["b0591"],
    "2. 纺织印染业的发展与新兴花色品种 / 1）纺织印染业的技术改进与发展 / ① 棉织业"))

rows.append(C(
    "claim-0362", "factual_claim",
    "夏燕靖称，1861年外商首先在上海设立近代缫丝厂，这是我国最早的民族近代工业，也可以说缫丝业是我国近代民族工业的摇篮。",
    "Xia Yanjing states that in 1861 foreign merchants first set up a modern silk-reeling factory in Shanghai, calling it China's earliest modern national industry and silk reeling the cradle of China's modern national industry.",
    "medium",
    ["04-knowledge/units/institutions/jichanglong-sichang.md",
     "04-knowledge/units/terms/saoche.md"],
    "断言取 L4841 首句。1872 年后广东足踏缫丝车、顺德蒸汽缫丝厂 145 家与农村手工缫丝长期维持留在同段。来源把“外商设立”与“我国最早的民族近代工业”并置，主体与定性存在张力，本条照录不调和；继昌隆缫丝厂作为民族资本机器缫丝厂另见 institutions/jichanglong-sichang，缫车见 terms/saoche。",
    4839, 4842, "line", [4841], ["b0593"],
    "2. 纺织印染业的发展与新兴花色品种 / 1）纺织印染业的技术改进与发展 / ③ 缫丝业"))

rows.append(C(
    "claim-0363", "historiographic_claim",
    "夏燕靖认为，1912年民国政府首先颁行《剪辫通令》，随后又参照西洋诸国服饰制度发布《服制条例》，使得五彩纷呈的现代服装终于冲垮了历代积习下来的衣冠等级制度。",
    "Xia Yanjing holds that in 1912 the Republican government first promulgated the Queue-Cutting Order and then, modelling on Western dress systems, issued the Dress Regulations, so that modern dress finally broke down the hierarchy of ceremonial attire accumulated over successive dynasties.",
    "medium",
    ["04-knowledge/units/events/jianbian-yifu-1912.md",
     "04-knowledge/units/publications/jianbian-tongling.md",
     "04-knowledge/units/publications/fuzhi-tiaoli.md"],
    "断言取 L4871-L4875 的政策与制度后果链。图 10-13 与图注把句子切成两段，按文意以 L4875 为关键行；传统袍衫袄裤裙受西服影响、新款时装与“服装改制的新历史时期”留在同段。来源未给《服制条例》条文、实施范围或服饰等级解体的具体指标。剪辫易服见 events/jianbian-yifu-1912，两个法令分别见 publications/jianbian-tongling、publications/fuzhi-tiaoli。",
    4869, 4876, "line", [4875], ["b0597"],
    "3. 服饰设计水平的提高"))

patches = [
    P("claim-0239", "cand-08-111", 4731, 4736, "line", [4733, 4735], ["b0577"],
      "1. 伴随近代手工业和对外贸易发展起来的艺术设计"),
    P("claim-0240", "cand-08-110", 4739, 4742, "line", [4741], ["b0579"],
      "1. 伴随近代手工业和对外贸易发展起来的艺术设计 / 知识链接：我国资本主义产生的历史背景"),
    P("claim-0241", "cand-09-98", 4877, 4885, "line", [4881], ["b0598"],
      "3. 服饰设计水平的提高 / 1）男装新制"),
    P("claim-0242", "cand-09-101", 4918, 4928, "line", [4922], ["b0602"],
      "4. 新兴产业的出现与艺术设计的新发展"),
    P("claim-0243", "cand-09-100", 4946, 4972, "line", [4969, 4971], ["b0605"],
      "4. 新兴产业的出现与艺术设计的新发展 / 1）国外技术的引进与机器制造业的产生"),
    P("claim-0244", "cand-09-104", 5013, 5054, "line", [5015], ["b0609"],
      "4. 新兴产业的出现与艺术设计的新发展 / 3）书籍装帧艺术设计的发展与特色"),
    P("claim-0245", "cand-09-102", 5063, 5090, "line", [5067], ["b0612"],
      "5. 建筑艺术的变迁与建筑装饰的兴起 / 2）从中国固有式建筑到现代中国样建筑"),
    P("claim-0246", "cand-09-103", 5063, 5090, "line", [5081], ["b0612"],
      "5. 建筑艺术的变迁与建筑装饰的兴起 / 2）从中国固有式建筑到现代中国样建筑"),
]

MAP = {
    "claim-0360": "cand-08-112",
    "claim-0361": "cand-08-113",
    "claim-0362": "cand-08-114",
    "claim-0363": "cand-09-99",
}
for row in rows:
    row["source"]["candidate_id"] = DOC + ":" + MAP[row["claim_id"]]

out_rows = ROOT / "_zn_cl11_rows.json"
out_patch = ROOT / "_zn_cl11_patch.json"
out_rows.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8", newline="\n")
out_patch.write_text(json.dumps(patches, ensure_ascii=False, indent=1) + "\n",
                     encoding="utf-8", newline="\n")

from collections import Counter
print(json.dumps({
    "rows": len(rows),
    "patches": len(patches),
    "patch_claims": len({p["claim_id"] for p in patches}),
    "types": dict(Counter(r["claim_type"] for r in rows)),
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
}, ensure_ascii=False))
