# -*- coding: utf-8 -*-
"""Build 赵农 2009 总结与后记 claim rows (6 new claims, no merges)."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "总结与后记"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"
I = "04-knowledge/units/institutions/"
PR = "04-knowledge/units/procedures/"
E = "04-knowledge/units/events/"

MAP = ROOT / "03-processing/2009-zhaonong-zhongguo-yishu-shejishi/source-map.jsonl"
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
    "claim-0764", "cand-12-150", "historiographic_claim",
    "赵农认为，中国古代是在农耕文化和游牧文化的相互磨合中发展的，农业文化以其稳定的社会方式接纳并融合了其他文化；丝绸之路的拓通加强了东西方经济与文化的联系。中国古代社会后期在大陆文明与海洋文明的较量中，传统文化已不再具有优势，封建专制的桎梏加剧了国力渐败渐衰的进程。",
    "Zhao Nong holds that ancient China developed through the mutual adjustment of agrarian and pastoral cultures, with the agrarian culture absorbing and integrating other cultures through its stable social forms; the opening of the Silk Road strengthened economic and cultural links between East and West. In the later period, as continental and maritime civilisations contended, traditional Chinese culture lost its advantage, and the shackles of feudal autocracy deepened the decline of national strength.",
    [T + "sichou-zhilu.md", W + "gengzhi-tu.md"],
    "断言语义取 L8495。农业与游牧、大陆与海洋两组对照为作者的长时段解释；丝绸之路条对应“拓通”，耕织图条对应农业文化。原文以“这不是地理问题，而是政治文化的原因”收束，属归因判断，未给气候、人口与财政数据。与 claim-0682（清代闭关锁国导致近代衰败）为同册前后章近邻，均论制度性衰败，未合并。",
    8484, 8560, [8495], "总结"))

rows.append(C(
    "claim-0765", "cand-12-151", "historiographic_claim",
    "赵农认为，“洋务运动”的失败，无论是军事意义的“甲午海战”，还是官商一体的封建经济体系，都为后来中国经济改革带来无穷的后患；官商一体的制度导致资本主义进展缓慢，也阻碍中国现代化的改革。",
    "Zhao Nong holds that the failure of the Self-Strengthening Movement, whether in the military defeat at the Battle of the Yellow Sea or in the feudal economic system of official-merchant fusion, brought endless consequences for later Chinese economic reform; the official-merchant system slowed capitalist development and obstructed China's modernising reforms.",
    [E + "yangwu-yundong.md", I + "jiangnan-zhizao-zongju.md", I + "jinling-jiqiju.md", I + "fujian-chuanzhengju.md", I + "tianjin-jiqiju.md", I + "hubei-qiangpaochang.md", I + "dasheng-shachang.md", R + "zhang-jian.md", R + "li-hongzhang.md", R + "zhang-zhidong.md", R + "zuo-zongtang.md", R + "zeng-guofan.md"],
    "断言语义取 L8506、L8513、L8523。洋务运动条对应总事件；江南制造总局、金陵机器局、福建船政局、天津机器局、湖北枪炮厂五条对应原文企业清单；大生纱厂与张謇条对应官商一体案例；李鸿章、张之洞、左宗棠、曾国藩四条对应原文所举官员。甲午海战库内无独立条目。“无穷后患”“阻碍现代化”为作者的因果评价，未给企业资本、产量与亏损数据。与 claim-0682 跨章近邻，均论晚清制度性衰败，未合并。",
    8484, 8560, [8506, 8513, 8523], "总结"))

rows.append(C(
    "claim-0766", "cand-12-152", "historiographic_claim",
    "赵农认为，回顾中国历史文化绝不仅仅是温故而知新，更需痛定思定，吸取中国文化从盛到衰的沉重教训；设计文化的鼎盛就是社会的进步，社会的进步也必然推动设计文化的进步。",
    "Zhao Nong holds that reviewing Chinese history and culture is far more than recalling the old to know the new; it requires learning from the heavy lesson of China's rise and decline. The flourishing of design culture is social progress, and social progress necessarily advances design culture.",
    [T + "industrial-design.md", T + "gongyi-meishu.md"],
    "断言语义取 L8542、L8547。“绝不仅仅是”“必然”为作者的价值主张与因果判断；工业设计条与工艺美术条对应设计文化的两个学科落点。原文未给“社会进步”的衡量指标与设计产业数据。与 claim-0769（民生与民主）同章近邻，前者论设计文化与社会进步、后者论民生与民主，未合并。",
    8484, 8560, [8542, 8547], "总结"))

rows.append(C(
    "claim-0767", "cand-12-157", "historiographic_claim",
    "赵农认为，1793年马葛尔尼使华因跪拜争议被逐，清政府断然拒绝贸易活动，此后大清帝国在昏睡中下滑到危机边缘而仍不自省，失去了历史进步的机遇。",
    "Zhao Nong holds that the 1793 Macartney embassy was expelled after the dispute over kneeling, the Qing court flatly rejected trade, and the empire thereafter slid sleeping toward crisis without awakening, losing the opportunity for historical progress.",
    [E + "ma-gaerni-shihua.md", P + "beijing.md"],
    "断言语义取 L8749。马葛尔尼使华条对应事件，北京条对应使团目的地与清廷决策地点。“昏睡中下滑”“失去历史进步的机遇”为作者的评价；原文另述 600 箱工业科技产品、和珅逐客与鸦片战争后果。与 claim-0682 跨章近邻，均论清廷闭关，未合并。",
    8745, 8800, [8749], "后记"))

rows.append(C(
    "claim-0768", "cand-12-158", "historiographic_claim",
    "赵农认为，文化的发展是从器具的更新开始的，设计的出现便是人类对物化精准的认识和把握，以至形成规律性的方法；不同时代和民族有不同的审美需求，相应地形成不同的制作过程和表现手法，艺术设计的风格也在这种变化中形成。",
    "Zhao Nong holds that cultural development begins with the renewal of implements; design emerges as humanity's precise cognition and grasp of materialisation, eventually forming regular methods. Different eras and peoples have different aesthetic needs and correspondingly different production processes and expressive techniques, and design styles form through this change.",
    [B + "kaogongji.md", W + "gengzhi-tu.md", T + "gongyi-meishu.md"],
    "断言语义取 L8753。“从器具的更新开始”为作者的文化史命题，接近《考工记》的器物传统；考工记条与耕织图条分别对应工艺典籍与器用图像，工艺美术条对应设计风格的学科语境。原文未给考古学或技术史的分期证据。与 claim-0764（农耕与游牧长时段）同章近邻，未合并。",
    8745, 8800, [8753], "后记"))

rows.append(C(
    "claim-0769", "cand-12-171", "historiographic_claim",
    "赵农认为，艺术设计的根本着眼点在于“民生”的利益，而“民生”的根本又在于“民主”。",
    "Zhao Nong holds that the fundamental focus of art design is the interest of people's livelihood, and the root of people's livelihood lies in democracy.",
    [],
    "断言语义取 L8535。“民生—民主”的递进为作者的核心判断；同段以西方 20 世纪初设计文化转入“设计”轨道、中国工业基础薄弱、经济贫困为对照背景。库内无民生、民主或民本条目，未强行链接。与 claim-0766 同章近邻，前者论设计文化与社会进步、后者论民生与民主，未合并。",
    8535, 8535, [8535], "总结"))

types = Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({p for r in rows for p in r["supported_by"]})
print(json.dumps({
    "claims": len(rows),
    "first": rows[0]["claim_id"],
    "last": rows[-1]["claim_id"],
    "types": dict(types),
    "links": links,
    "distinct": distinct,
}, ensure_ascii=False, indent=1))

(ROOT / "_zn_zn11a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_zn11a_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")
print("written _zn_zn11a_rows.json / _zn_zn11a_patch.json")
