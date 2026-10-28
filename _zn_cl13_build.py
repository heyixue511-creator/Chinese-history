# -*- coding: utf-8 -*-
"""Build CL10a claim rows (15 new) and 3 cross-edition corroboration patches.

Scope: 2016 年表 (L5545-L6110), 中国古典设计文献索引 (L6111-L6349), 后记 (L6479-L6538).
18 claim candidates: 15 new claims claim-0379..0393, 3 merged into 2009 claims.
"""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
DATE = "2026-10-27"
TIMELINE = "当代中国工艺美术、艺术设计大事年表（1949-2000）"
INDEX = "中国古典设计文献索引"


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, key_lines,
      block_ids, chapter, section):
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
                "span_kind": "bounded",
                "key_lines": key_lines,
                "block_ids": block_ids,
                "chapter": chapter,
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


def P(claim_id, cand, start, end, key_lines, block_ids, section):
    return {
        "claim_id": claim_id,
        "candidate_id": DOC + ":" + cand,
        "corroborating_span": {
            "doc_id": DOC,
            "source_file": SRC,
            "line_start": start,
            "line_end": end,
            "span_kind": "bounded",
            "key_lines": key_lines,
            "block_ids": block_ids,
            "chapter": "附录",
            "section": f"{TIMELINE} / {section}",
            "candidate_id": DOC + ":" + cand,
        },
    }


rows = []

# --- 年表 ---
rows.append(C(
    "claim-0379", "historiographic_claim",
    "夏燕靖记述，1957年7月22日全国工艺美术艺人代表会议在北京举行，会议提出对工艺美术“保护、发展和提高”的方针以及“适用、经济、美观”的生产原则，为第二个五年计划的工艺美术发展指明了方向。",
    "Xia Yanjing records that on 22 July 1957 the National Conference of Craft Art Artisans was held in Beijing, where the policy of protecting, developing and improving craft art and the production principle of suitability, economy and beauty were put forward, charting the direction of craft art for the Second Five-Year Plan.",
    "medium",
    ["04-knowledge/units/events/national-craft-artists-conference-1957.md",
     "04-knowledge/units/terms/gongyi-meishu.md"],
    "断言取 L5647。年表条目记会期、地点、方针与原则，并以“为第二个五年计划的工艺美术发展指明了方向”作历史意义判断，故按候选作 historiographic。田自秉 2010 记“1958年，举行首次全国艺人代表会议”，与 2016 年表相差一年，事件 KU 已并存两说，本条只取 2016 口径。会议见 events/national-craft-artists-conference-1957，概念见 terms/gongyi-meishu。来源未给会议文件、主办机关与代表名单。",
    5641, 5656, [5641, 5647], ["b0658"],
    "附录", f"{TIMELINE} / 1957年"))

rows.append(C(
    "claim-0380", "historiographic_claim",
    "夏燕靖记述，1957年7月江苏省人民政府批准建立南京市云锦研究所，这是新中国第一家工艺美术研究机构。",
    "Xia Yanjing records that in July 1957 the Jiangsu Provincial People's Government approved the establishment of the Nanjing Yunjin Research Institute, the first craft art research institution in New China.",
    "medium",
    ["04-knowledge/units/institutions/nanjing-yunjin-yanjiusuo.md",
     "04-knowledge/units/terms/nanjing-yunjin.md",
     "04-knowledge/units/places/nanjing.md"],
    "断言取 L5651。年表以“新中国第一家工艺美术研究机构”作历史地位判断，故按候选作 historiographic。1954 年 6 月南京市文化处组织的“云锦研究工作组”与 1957 年 7 月批准建立的“南京市云锦研究所”是两个机构，本条只记研究所，不与 claim-0364 的工作组混同；两处“最早/第一家”的比较范围不同，来源未作机构普查。见 institutions/nanjing-yunjin-yanjiusuo、terms/nanjing-yunjin、places/nanjing。来源未给批准文号与首任负责人。",
    5641, 5656, [5641, 5651], ["b0658"],
    "附录", f"{TIMELINE} / 1957年"))

rows.append(C(
    "claim-0381", "evaluative_claim",
    "夏燕靖记述，1994年10月下旬“全国技术美学研讨会”在天津举行，并称这是美学第一次对艺术设计进行理论思考的专题研讨会。",
    "Xia Yanjing records that in late October 1994 the National Symposium on Technical Aesthetics was held in Tianjin, which he calls the first symposium in which aesthetics reflected theoretically on art design.",
    "medium",
    ["04-knowledge/units/events/technical-aesthetics-symposium-1994.md"],
    "断言取 L6013。年表原文“这是美学第一次对艺术设计进行理论思考的专题研讨会”是作者的史学评价，按候选作 evaluative；来源未给主办单位、参会人数、论文篇目与“第一次”的比较依据。会议见 events/technical-aesthetics-symposium-1994。",
    6009, 6018, [6009, 6013], ["b0687"],
    "附录", f"{TIMELINE} / 1994年"))

rows.append(C(
    "claim-0382", "factual_claim",
    "夏燕靖记述，1999年11月20日中央工艺美术学院与清华大学合并，成立清华大学美术学院。",
    "Xia Yanjing records that on 20 November 1999 the Central Academy of Arts and Design merged with Tsinghua University, forming the Tsinghua University Academy of Arts and Design.",
    "medium",
    ["04-knowledge/units/institutions/central-academy-arts-design.md"],
    "断言取 L6087。候选作 basic_fact，按语义映射为 factual_claim。年表只记合并日期与结果，未记合并方案、院系调整与后续建制；中央工艺美术学院见 institutions/central-academy-arts-design。清华大学的机构 KU 尚未建立，supported_by 暂只列合并前身。",
    6073, 6090, [6073, 6087], ["b0692"],
    "附录", f"{TIMELINE} / 1999年"))

rows.append(C(
    "claim-0383", "factual_claim",
    "夏燕靖记述，2000年初上海建成中国第一条生态景观大道，它是上海迎接新世纪的标志性工程。",
    "Xia Yanjing records that in early 2000 Shanghai completed China's first ecological landscape avenue, a landmark project marking the city's entry into the new century.",
    "medium",
    ["04-knowledge/units/events/2000-shanghai-eco-landscape-avenue.md",
     "04-knowledge/units/places/shanghai.md"],
    "断言取 L6093。候选作 basic_fact，按语义映射为 factual_claim。年表未给大道名称、长度、起止与设计单位；“中国第一条”为来源表述，未见比较依据。事件见 events/2000-shanghai-eco-landscape-avenue，城市见 places/shanghai。",
    6091, 6110, [6091, 6093], ["b0693"],
    "附录", f"{TIMELINE} / 2000年"))

# --- 中国古典设计文献索引 ---
rows.append(C(
    "claim-0384", "historiographic_claim",
    "夏燕靖认为，《周易》所包含的设计思想主要体现在“道”与“器”的关系上，成为传统造物思想与设计方法亘古不变的主题。",
    "Xia Yanjing holds that the design thought contained in the Book of Changes centres on the relation between dao and qi, which became the unchanging theme of traditional thought on making and of design method.",
    "medium",
    ["04-knowledge/units/publications/zhouyi.md",
     "04-knowledge/units/terms/daoqi-tongyi.md"],
    "断言取 L6115。文献索引条目先叙《周易》成书、六十四卦与阴阳观，末句给出作者对设计思想主题的判断，故按候选作 historiographic。文献见 publications/zhouyi，道器关系见 terms/daoqi-tongyi。来源未给出处篇目与注家。",
    6113, 6116, [6115], ["b0695"],
    "附录", f"{INDEX} / 《周易》"))

rows.append(C(
    "claim-0385", "factual_claim",
    "《考工记》所记工艺分6大类30个工种，内容涉及制车、兵器、礼器、钟磬、练染、建筑、水利等手工艺技术，还涉及天文、生物、数学、物理、化学等自然科学。",
    "The Artificers' Record divides its crafts into six categories and thirty trades, covering cart making, weapons, ritual vessels, bells and chimes, dyeing, architecture and waterworks, and also touching astronomy, biology, mathematics, physics and chemistry.",
    "medium",
    ["04-knowledge/units/publications/kaogongji.md"],
    "断言取 L6119。候选作 basic_fact，按语义映射为 factual_claim。条目并记《考工记》为春秋时期记述齐国官手工艺的典籍、西汉河间献王刘德取以补《周礼·冬官》佚缺，以及历代注家郑玄、贾公彦、戴震、程瑶田、孙诒让；本条只取工种数与内容范围。6大类30工种按原文，未展开分类名目。文献见 publications/kaogongji。",
    6117, 6120, [6119], ["b0696"],
    "附录", f"{INDEX} / 《考工记》"))

rows.append(C(
    "claim-0386", "interpretive_claim",
    "夏燕靖认为，《墨子·节用》包含墨子的工艺思想，强调“节用”当为制造日用器物的原则和要求。",
    "Xia Yanjing holds that the chapter on economy in expenditure in the Mozi contains Mozi's craft thought, insisting that economy should be the principle and requirement for making everyday utensils.",
    "medium",
    ["04-knowledge/units/publications/mozi-jieyong.md",
     "04-knowledge/units/persons/mozi.md"],
    "断言取 L6149。条目先叙墨子生卒、墨家学派与《墨子》篇卷，末句是作者对《节用》工艺思想的概括，按候选作 interpretive。原文未引《节用》成句。文献见 publications/mozi-jieyong，人物见 persons/mozi。",
    6147, 6150, [6149], ["b0703"],
    "附录", f"{INDEX} / 《墨子·节用》"))

rows.append(C(
    "claim-0387", "historiographic_claim",
    "《唐六典》全称《大唐六典》，是唐代一部行政法典，也是我国最早的一部行政法典。",
    "The Tang liudian, in full the Great Tang Six Canons, is an administrative code of the Tang dynasty and the earliest administrative code in China.",
    "medium",
    ["04-knowledge/units/publications/tang-liudian.md"],
    "断言取 L6185。条目并记唐玄宗时官修、旧题玄宗撰李林甫等注、实为张说张九龄等编纂、成书于开元二十六年（738）、分30卷、按《周官》六典分目而实际依唐代官制编纂；本条只取性质与“最早”判断。“我国最早的一部行政法典”为来源表述，未给比较范围。文献见 publications/tang-liudian。",
    6183, 6186, [6185], ["b0712"],
    "附录", f"{INDEX} / 《唐六典》"))

rows.append(C(
    "claim-0388", "evaluative_claim",
    "《天工开物》较为完整地记载了明朝中叶以前我国的各项生产技术，被称之为世界上第一部关于农业和手工业生产的综合性著作。",
    "The Exploitation of the Works of Nature records fairly completely the production techniques of China before the mid-Ming and has been called the world's first comprehensive work on agriculture and handicraft production.",
    "medium",
    ["04-knowledge/units/publications/tiangong-kaiwu.md"],
    "断言取 L6237。条目并记宋应星撰、崇祯十年（1637）初刊、3篇18卷、121幅插图与130多项生产技术；本条只取记载范围与“第一部”评价。“被称之为”保留来源的转述口吻，未给提出者与比较依据。文献见 publications/tiangong-kaiwu。",
    6235, 6238, [6235, 6237], ["b0725"],
    "附录", f"{INDEX} / 《天工开物》"))

rows.append(C(
    "claim-0389", "interpretive_claim",
    "夏燕靖认为，《长物志》始终贯穿“以用为本”的思想，其价值体现为一种物质的实用性。",
    "Xia Yanjing holds that the Treatise on Superfluous Things is consistently informed by the idea of use as the foundation, its value lying in a material practicality.",
    "medium",
    ["04-knowledge/units/publications/changwu-zhi.md"],
    "断言取 L6245。条目并记文震亨撰、明末天启年间刊行、12卷分类与“长物”典出《世说新语》；本条只取作者对全书思想的概括。“以用为本”按原文引号，未指出自哪一卷。文献见 publications/changwu-zhi。",
    6243, 6246, [6243, 6245], ["b0727"],
    "附录", f"{INDEX} / 《长物志》"))

rows.append(C(
    "claim-0390", "evaluative_claim",
    "明代黄成所撰《髹饰录》是我国现存唯一的古代漆工专著。",
    "The Record of Lacquer Decoration by the Ming craftsman Huang Cheng is the only surviving ancient monograph on lacquer craft in China.",
    "medium",
    ["04-knowledge/units/publications/xiu-shi-lu.md"],
    "断言取 L6249。条目并记黄成为明隆庆（1567-1572）年间漆工、天启五年（1625）杨明逐条加注并撰序、1927年朱启钤据流传日本的钞本刊刻、分乾坤两集18章186条；本条只取作者与“唯一”判断。“现存唯一”为来源表述，未给普查依据。文献见 publications/xiu-shi-lu。",
    6247, 6252, [6247, 6249], ["b0728"],
    "附录", f"{INDEX} / 《髹饰录》"))

rows.append(C(
    "claim-0391", "historiographic_claim",
    "清雍正十二年（1734）清工部颁布《工程做法》，共74卷；夏燕靖认为《清工部工程做法》与宋代李诚《营造法式》是我国古代由官方颁布的关于建筑标准的仅有的两部古籍。",
    "In the twelfth year of Yongzheng (1734) the Qing Board of Works promulgated the Construction Methods in seventy-four juan; Xia Yanjing holds that it and Li Cheng's Song-dynasty Building Standards are the only two ancient Chinese books on building standards issued by official authority.",
    "medium",
    ["04-knowledge/units/publications/gongcheng-zuofa.md",
     "04-knowledge/units/publications/yingzao-fashi.md"],
    "断言取 L6333。原文作“李诚”，同一文献索引《营造法式》条 L6197 作“李诫”，两处不一致；本条照录 L6333 的“李诚”并在 statement 保留，未据 L6197 改写。两书“仅有的两部”为来源判断，未给书目普查依据；卷1至卷74的分卷内容留在同条。文献见 publications/gongcheng-zuofa、publications/yingzao-fashi。",
    6331, 6338, [6333], ["b0748", "b0749"],
    "附录", f"{INDEX} / 《清工部工程做法》"))

# --- 后记 ---
rows.append(C(
    "claim-0392", "factual_claim",
    "夏燕靖在2016年升级版后记中说明，本次修订在第一章增加“原始农业生产器具设计”，第五章增加“漆工艺的发展与特色漆器品种”，第六章增加“唐代设计理论述要”，第九章增加“明清贸易瓷的历史演变与特色”，第十一章增加“社会主义建设时期的工业产品设计”。",
    "In the postscript to the 2016 upgraded edition Xia Yanjing states that the revision added Design of Primitive Agricultural Production Tools to chapter 1, The Development of Lacquer Craft and Characteristic Lacquer Varieties to chapter 5, An Outline of Tang Design Theory to chapter 6, The Historical Evolution and Characteristics of Ming-Qing Export Porcelain to chapter 9, and Industrial Product Design in the Socialist Construction Period to chapter 11.",
    "medium",
    ["04-knowledge/units/publications/zhongguo-yishu-shejishi-upgraded.md"],
    "断言取 L6489。候选 claim_scope 为 bibliographic_fact，不在 claim registry 的六类之列，按语义映射为 factual_claim：本条记述修订事实。后记共列五方面修订，本条取第一方面（增补五节）；其余四方面见 L6491-L6497。五个章节题按原文，未核对正文标题逐字。文献见 publications/zhongguo-yishu-shejishi-upgraded。",
    6479, 6538, [6489], ["b0754"],
    "后记", "修订说明"))

rows.append(C(
    "claim-0393", "factual_claim",
    "夏燕靖在2016年升级版后记中说明，本教材于2013年10月获江苏省级重点立项教材，并推荐为全省高校设计专业用书。",
    "In the postscript to the 2016 upgraded edition Xia Yanjing states that the textbook was designated a Jiangsu provincial key textbook project in October 2013 and recommended for design programmes in the province's universities.",
    "medium",
    ["04-knowledge/units/publications/zhongguo-yishu-shejishi-upgraded.md"],
    "断言取 L6501。候选 claim_scope 为 bibliographic_fact，按语义映射为 factual_claim。后记另记“到2016年，历时十年修订五次”“于2013年10月获江苏省级重点立项教材”；本条只取立项与推荐两项，未给立项文号与推荐文件。文献见 publications/zhongguo-yishu-shejishi-upgraded。",
    6479, 6538, [6501], ["b0754"],
    "后记", "教材立项说明"))

for row in rows:
    assert row["statement_zh"].strip() and row["statement_en"].strip()
    assert '"' not in row["statement_zh"], row["claim_id"]

cands = {
    "claim-0379": "cand-10-62",
    "claim-0380": "cand-10-63",
    "claim-0381": "cand-10-65",
    "claim-0382": "cand-11-100",
    "claim-0383": "cand-11-101",
    "claim-0384": "cand-11-102",
    "claim-0385": "cand-11-103",
    "claim-0386": "cand-11-104",
    "claim-0387": "cand-11-109",
    "claim-0388": "cand-11-107",
    "claim-0389": "cand-11-105",
    "claim-0390": "cand-11-106",
    "claim-0391": "cand-11-108",
    "claim-0392": "cand-11-110",
    "claim-0393": "cand-11-111",
}
assert len(cands) == len(rows) == 15
for row in rows:
    row["source"]["candidate_id"] = DOC + ":" + cands[row["claim_id"]]

patches = [
    P("claim-0255", "cand-10-64", 5843, 5858, [5843, 5845], ["b0675"], "1983年"),
    P("claim-0256", "cand-10-61", 6009, 6018, [6009, 6017], ["b0687"], "1994年"),
    P("claim-0257", "cand-11-99", 6059, 6072, [6059, 6071], ["b0691"], "1998年"),
]
assert len(patches) == 3

(ROOT / "_zn_cl13_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_cl13_patch.json").write_text(
    json.dumps(patches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

from collections import Counter
print(json.dumps({
    "rows": len(rows),
    "patches": len(patches),
    "types": dict(Counter(r["claim_type"] for r in rows)),
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
    "with_supported_by": sum(1 for r in rows if r["supported_by"]),
}, ensure_ascii=False))
