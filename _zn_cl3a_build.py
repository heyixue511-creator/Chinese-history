# -*- coding: utf-8 -*-
"""Build the CL3a 2016 Xia Yanjing claim rows and corroboration patches.

Front matter + chapter 1 (原始社会) of the 2016 upgraded edition: 27 claim
candidates. 13 new claims (one of which merges two candidates); 13 candidates
corroborate existing 2009 claims, 1 candidate merges into a new claim.
"""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
DATE = "2026-10-27"
OUT = ROOT / "_zn_cl3a_rows.json"
PATCH = ROOT / "_zn_cl3a_patch.json"


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, chapter, section, merged=None):
    source = {
        "doc_id": DOC,
        "source_file": SRC,
        "source_span": {
            "line_start": start,
            "line_end": end,
            "span_kind": kind,
            "key_lines": key_lines,
            "block_ids": block_ids,
            "chapter": chapter,
            "section": section,
        },
        "candidate_id": DOC + ":" + cid,
    }
    if merged:
        source["merged_candidate_ids"] = [DOC + ":" + m for m in merged]
    return {
        "claim_id": None,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": source,
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    }


ROWS = []

# 0260
ROWS.append(C(
    "cand-01-113", "historiographic_claim",
    "夏燕靖指出，按照我国传统学科分类法，设计当属“技艺”与“营造”诸门类；"
    "他据此说明类书与古代文献中的设计史料范围。",
    "Xia Yanjing points out that, according to China's traditional classification "
    "of disciplines, design falls under the categories of craft/skill (jiyi) and "
    "building/construction (yingzao); he uses this to explain the range of design "
    "materials found in encyclopedias and ancient texts.",
    "medium", [],
    "候选作 historiographic；断言取 L109。作者没有展开“技艺”“营造”的古今义，"
    "也没有给出这一分类的文献依据，本条只保留分类判断，不把随后列举的类书部卷"
    "写成已经逐条核验的设计门类。",
    109, 109, "line", [109], ["b0007"],
    "再版序言", "关于中国艺术设计史的脉络梳理",
))

# 0261
ROWS.append(C(
    "cand-01-108", "interpretive_claim",
    "夏燕靖认为，人与古猿的区别主要在于制造工具和使用工具；能否制造工具是人和动物相区别的标志。",
    "Xia Yanjing argues that the distinction between humans and the great apes "
    "lies mainly in making and using tools, and that the ability to make tools is "
    "the mark distinguishing humans from animals.",
    "high", ["04-knowledge/units/procedures/shiqi-dazhi-sanfa.md"],
    "候选作 historiographic，路由 interpretive：这是关于人与动物界限的一般命题，"
    "不是设计史分期判断。断言取 L289 与 L363，两处相隔较远，记 bounded。"
    "本条不把“主要在于”扩展为唯一标准，也不把制造工具等同于设计意识。",
    289, 363, "bounded", [289, 363], ["b0018", "b0031"],
    "原始社会的设计缘起", "章首概述 / 1. 设计起源与石器制作",
))

# 0262
ROWS.append(C(
    "cand-01-11", "historiographic_claim",
    "夏燕靖认为，华夏文明的发展是多点起源而非单一化的文明；他以北方、东方、中原、东南、"
    "西南、南方六个新石器文化区域，以及仰韶、红山、龙山、齐家、良渚等文化并列为据。",
    "Xia Yanjing argues that Chinese civilization developed from multiple origins "
    "rather than a single source, citing six Neolithic cultural regions—northern, "
    "eastern, central plains, southeastern, southwestern and southern—together with "
    "Yangshao, Hongshan, Longshan, Qijia and Liangzhu cultures.",
    "high", [
        "04-knowledge/units/terms/yangshao-culture.md",
        "04-knowledge/units/terms/liangzhu-culture.md",
    ],
    "候选作 historiographic；断言取 L298。六个区域与文化的并列是来源的叙述框架，"
    "不是考古学定论；本条保留“多点起源”的判断，不把区域数量写成唯一分期，"
    "也不把“华夏文明”与考古学文化直接等同。",
    298, 298, "line", [298], ["b0018"],
    "原始社会的设计缘起", "章首概述",
))

# 0263
ROWS.append(C(
    "cand-01-14", "historiographic_claim",
    "夏燕靖认为，从旧石器中晚期起，黄河流域就成为我国远古文化的发展中心；"
    "他并称从中石器时代起，黄河流域就是我国远古文化的中心区域，并为历代王朝在此建都奠定基础。",
    "Xia Yanjing argues that the Yellow River basin became the developmental center "
    "of China's remote antiquity from the middle and late Paleolithic, and that from "
    "the Mesolithic it was the central region of China's ancient culture, laying the "
    "foundation for successive dynasties to establish their capitals there.",
    "medium", [
        "04-knowledge/units/terms/yangshao-culture.md",
        "04-knowledge/units/places/banpo-site.md",
        "04-knowledge/units/places/erlitou-site.md",
    ],
    "候选作 historiographic；断言取 L308 与 L334。来源先说“从旧石器中晚期起”，"
    "又说“因此从中石器时代起”，两种起点表述并不完全一致；本条并列保留，"
    "不合并为单一起点。“发展中心”是作者的文明史判断，不是单一遗址的测年结论；"
    "L308 的都城序列含传说与后世都城，未逐项核验。",
    306, 334, "bounded", [308, 334], ["b0019", "b0026"],
    "原始社会的设计缘起", "知识链接：黄河流域文化遗址 / 中石器时代",
))

# 0264
ROWS.append(C(
    "cand-01-15", "interpretive_claim",
    "夏燕靖认为，我国原始社会的设计，其实就是代表着人类有意识的、用艺术创造力所体现的造物活动；"
    "更确切地说，是我们的祖先在造物过程中运用智慧和技巧发展起来的特殊的劳作成果。",
    "Xia Yanjing defines the design of China's primitive society as the conscious "
    "creation of artifacts embodying artistic creativity—more precisely, the special "
    "labor achievements developed by our ancestors through wisdom and skill in the "
    "process of making things.",
    "medium", ["04-knowledge/units/terms/sheji.md"],
    "候选作 interpretive；断言取 L312。“其实就是”与“更确切地说”是作者的定义性表述，"
    "不是考古学定义；本条保留“有意识”“艺术创造力”“智慧和技巧”三个限定，"
    "不扩展为一般设计定义，也不把原始社会所有造物都写成自觉设计。",
    312, 312, "line", [312], ["b0019"],
    "原始社会的设计缘起", "章首概述：原始社会设计的界定",
))

# 0265
ROWS.append(C(
    "cand-01-38", "factual_claim",
    "夏燕靖称，就我国陶器产生而言，已发现的最早陶器是1962年在江西万年县仙人洞出土的"
    "8000多年以前的陶器。",
    "Xia Yanjing states that, as far as the origin of pottery in China is concerned, "
    "the earliest pottery discovered to date is that unearthed in 1962 at Xianrendong "
    "in Wannian County, Jiangxi, dating to more than 8,000 years ago.",
    "medium", [
        "04-knowledge/units/places/xianrendong-site.md",
        "04-knowledge/units/terms/taoqi.md",
    ],
    "候选作 basic_fact，路由 factual；断言取 L422。来源未给测年方法；同章 L298 又写作"
    "“江西万县仙人洞”，地名前后不一致，本条按 L422 的“万年县”表述并保留校勘问题。"
    "“最早”是来源所记的考古发现判断，不是本条独立核验的结论。",
    422, 422, "line", [422], ["b0040"],
    "原始社会的设计缘起", "2. 陶器制作与器形设计 / 1）陶器产生",
))

# 0266
ROWS.append(C(
    "cand-01-42", "interpretive_claim",
    "夏燕靖据仰韶文化遗址的石斧、骨锄、粟、家畜骨骼、陶器、弓箭以及玉片、海贝等遗存推测，"
    "仰韶文化期手工业的发展在氏族内部开始有某种程度的分工，并有了私有制度萌芽。",
    "Drawing on stone axes, bone hoes, millet, animal bones, pottery, bows and arrows, "
    "jade pieces and cowrie shells from Yangshao culture sites, Xia Yanjing infers that "
    "handicraft production during the Yangshao period began to involve a certain degree "
    "of division of labor within the clan and that private property was beginning to emerge.",
    "medium", ["04-knowledge/units/terms/yangshao-culture.md"],
    "候选作 interpretive；断言取 L445。原文用“由此推测”限定，本条保留“推测”，"
    "不把分工与私有制萌芽写成已证事实；玉片、海贝被作者视为地区交换的佐证，"
    "交换与私有制之间的因果未展开，本条也不补写。",
    445, 445, "line", [445], ["b0045"],
    "原始社会的设计缘起", "知识链接：仰韶文化",
))

# 0267
ROWS.append(C(
    "cand-01-109", "evaluative_claim",
    "夏燕靖从社会进化角度评价，陶器比石器更为重要；陶器的出现促进了家畜豢养、五谷种植"
    "以及安定和文明的生活形成。",
    "From the perspective of social evolution, Xia Yanjing evaluates pottery as more "
    "important than stone tools, arguing that its emergence promoted animal "
    "domestication, grain cultivation and the formation of settled and civilized life.",
    "medium", ["04-knowledge/units/terms/taoqi.md"],
    "候选作 evaluative；断言取 L447。“更为重要”是作者的比较性评价，来源未给比较指标；"
    "本条不把它改写为可量化结论，也不把“促进”写成单向因果。",
    447, 447, "line", [447], ["b0045"],
    "原始社会的设计缘起", "2. 陶器制作与器形设计 / 1）陶器产生",
))

# 0268
ROWS.append(C(
    "cand-01-110", "evaluative_claim",
    "夏燕靖以龙山文化的陶鬻（原文如此，通行名陶鬶）为例，认为其三足中空扩大受热面积、"
    "颈部高拔、口前有鸟喙状长流，体现了陶匠师实用与美观有机结合的造型设计思想。",
    "Taking the Longshan culture pottery gui (written 鬻 in the source, conventionally "
    "鬶) as an example, Xia Yanjing argues that its hollow tripod legs enlarged the "
    "heated surface, its tall neck and bird-beak spout show that the potter combined "
    "practical use with visual appeal in his design thinking.",
    "medium", ["04-knowledge/units/terms/tao-gui.md"],
    "候选作 evaluative；断言取 L495。来源多写作“陶鬻”，通行名为“陶鬶”，"
    "本条并存两名并以“原文如此”标明；三足、长流等形制描述来自来源，"
    "未给尺寸与出土单位。",
    495, 495, "line", [495], ["b0053"],
    "原始社会的设计缘起", "2. 陶器制作与器形设计 / 2）重要的陶文化期 / ③ 龙山文化",
))

# 0269
ROWS.append(C(
    "cand-01-57", "evaluative_claim",
    "夏燕靖称，良渚古城是目前所发现的新石器时代我国最大城址，堪称“中华第一城”；"
    "其年代上限很可能是公元前2600—前2300年。",
    "Xia Yanjing states that the Liangzhu ancient city is the largest Neolithic city "
    "site discovered in China to date and can be called 'China's first city'; its upper "
    "date is very likely 2600–2300 BCE.",
    "medium", [
        "04-knowledge/units/places/liangzhu-gucheng.md",
        "04-knowledge/units/terms/liangzhu-culture.md",
    ],
    "候选作 evaluative；断言取 L506。“最大城址”“中华第一城”是来源的评价性判断，"
    "年代用“很可能”限定。该行只称良渚文化遗址群“有座古城”，未在本行使用"
    "“良渚古城”这一专名；本条按候选与 KU 的通行名表述，并保留这一称名差异。"
    "本条不把良渚古城直接写成中国最早城市。",
    506, 506, "line", [506], ["b0055"],
    "原始社会的设计缘起", "知识链接：良渚文化",
))

# 0270
ROWS.append(C(
    "cand-01-60", "interpretive_claim",
    "夏燕靖认为，良渚文化的鱼鳍形足陶鼎和水鸟形陶壶，均是人类在摹拟自然形态的基础上"
    "积累造型经验，进而按照生活需要创造出的人工形态，即根据生活需要而造型。",
    "Xia Yanjing argues that the Liangzhu culture's fish-fin-legged pottery ding and "
    "waterbird-shaped pottery hu both reflect accumulated modeling experience based on "
    "imitating natural forms, from which human-made forms were created according to the "
    "needs of life—that is, modeling for life's needs.",
    "medium", [
        "04-knowledge/units/terms/yuqixingzu-taoding.md",
        "04-knowledge/units/terms/shuiniaoxing-taohu.md",
        "04-knowledge/units/terms/liangzhu-culture.md",
    ],
    "候选作 interpretive；断言取 L515。相关句子从 L497“良渚文化的水鸟形陶壶是以动物形态"
    "为造型”起，被图版与“河姆渡文化”知识链接隔断，至 L515“依据的”续完；"
    "候选跨度 L508-L516 只覆盖续句，本条按 L515 表述并记录这一排录断裂。",
    515, 515, "line", [515], ["b0056"],
    "原始社会的设计缘起", "知识链接：良渚文化（续）",
))

# 0271
ROWS.append(C(
    "cand-01-111", "interpretive_claim",
    "夏燕靖认为，原始建筑是在巢居和穴居的基础上发展起来的，其基本形式是利用固体材料"
    "建造居住空间，以满足人的居住需要；在建筑实践中，人又按照美的规律营造出样式各异的建筑。",
    "Xia Yanjing argues that primitive architecture developed from nest dwellings and "
    "cave dwellings; its basic form uses solid materials to build dwelling space to meet "
    "human habitation needs, while in building practice people also created diverse forms "
    "according to the laws of beauty.",
    "medium", [
        "04-knowledge/units/terms/chaoju.md",
        "04-knowledge/units/terms/xueju.md",
        "04-knowledge/units/terms/bandixue-shi-jianzhu.md",
        "04-knowledge/units/terms/ganlan-shi-jianzhu.md",
    ],
    "候选作 interpretive；断言取 L572。“按照美的规律”是作者的建筑美学判断，"
    "来源未给实例逐条对应；本条保留这一规范性表述，不把它写成所有原始建筑的共同规律。",
    572, 572, "line", [572], ["b0063"],
    "原始社会的设计缘起", "4. 原始居住设计的雏形",
))

# 0272
ROWS.append(C(
    "cand-01-112", "historiographic_claim",
    "夏燕靖称，江浙地区是原始农业稻作发育区，良渚文化区是典型的稻作区域，"
    "因而也是我国最早实现犁耕的地区；许多遗址发现所谓石犁等耘田器。"
    "但他同时指出，良渚文化的石犁是否真正用作犁耕、良渚文化是否有犁耕农业，学界尚有争议。"
    "若三角形石犁能够确认为犁铧，则说明良渚文化农业已由耜耕农业发展到犁耕农业。",
    "Xia Yanjing states that the Jiangnan region was a rice-growing area of primitive "
    "agriculture and that the Liangzhu culture area was a typical rice-growing region "
    "and therefore the earliest area in China to practice plough agriculture; many sites "
    "have yielded so-called stone ploughs and other field-implement tools. He nevertheless "
    "notes that whether Liangzhu stone ploughs were actually used for ploughing, and whether "
    "Liangzhu culture had plough agriculture at all, remains disputed. If the triangular "
    "stone ploughs can be confirmed as ploughshares, then Liangzhu agriculture had developed "
    "from spade cultivation to plough cultivation.",
    "medium", [
        "04-knowledge/units/terms/liangzhu-shili.md",
        "04-knowledge/units/terms/yuanshi-nongju.md",
        "04-knowledge/units/terms/liangzhu-culture.md",
    ],
    "候选 01-79 与 01-112 同段重出，合并为一条；01-112 为主候选，01-79 记"
    "merged_candidate_ids。断言取 L580-L587。来源先说“最早实现犁耕”，随即以学界争议"
    "和“如果能够确认”收回强度，本条保留这一前后张力，不把良渚犁耕写成定论；"
    "商代青铜犁、战国铁犁的比较未展开。",
    580, 587, "bounded", [580, 587], ["b0064"],
    "原始社会的设计缘起", "5. 原始农业生产器具设计",
    merged=["cand-01-79"],
))

for i, row in enumerate(ROWS, start=260):
    row["claim_id"] = f"claim-{i:04d}"

assert [r["claim_id"] for r in ROWS] == [f"claim-{i:04d}" for i in range(260, 273)]

# Cross-edition corroboration patches to existing 2009 claims.
PATCHES = {
    "claim-0038": [("cand-01-07", 107, 107, "line", [107], ["b0007"],
                    "再版序言", "关于中国艺术设计史的脉络梳理")],
    "claim-0041": [("cand-01-16", 340, 340, "line", [340], ["b0027"],
                    "原始社会的设计缘起", "1. 设计起源与石器制作 / 1）设计起源")],
    "claim-0042": [("cand-01-20", 372, 372, "line", [372], ["b0032"],
                    "原始社会的设计缘起", "1. 设计起源与石器制作 / ② 石器的二次加工")],
    "claim-0043": [("cand-01-30", 416, 416, "line", [416], ["b0038"],
                    "原始社会的设计缘起", "1. 设计起源与石器制作 / ③ 石器的磨制技术")],
    "claim-0044": [("cand-01-40", 436, 436, "line", [436], ["b0043"],
                    "原始社会的设计缘起", "2. 陶器制作与器形设计 / 原始陶器的设计特点")],
    "claim-0045": [("cand-01-45", 453, 453, "line", [453], ["b0047"],
                    "原始社会的设计缘起", "2. 陶器制作与器形设计 / 2）重要的陶文化期 / ① 仰韶文化")],
    "claim-0046": [("cand-01-48", 468, 468, "line", [468], ["b0050"],
                    "原始社会的设计缘起", "知识链接：舞蹈纹盆的多种文化意义")],
    "claim-0047": [("cand-01-64", 521, 521, "line", [521], ["b0057"],
                    "原始社会的设计缘起", "2. 陶器制作与器形设计 / ④ 河姆渡文化")],
    "claim-0048": [("cand-01-69", 533, 533, "line", [533], ["b0059"],
                    "原始社会的设计缘起", "3. 纺编织物的产生与设计形式 / 1）纺编织物的产生")],
    "claim-0049": [("cand-01-72", 564, 564, "line", [564], ["b0062"],
                    "原始社会的设计缘起", "3. 纺编织物的产生与设计形式 / 2）纺编织物的设计形式")],
    "claim-0050": [("cand-01-75", 570, 570, "line", [570], ["b0063"],
                    "原始社会的设计缘起", "4. 原始居住设计的雏形")],
    "claim-0051": [("cand-01-71", 558, 558, "line", [558], ["b0061"],
                    "原始社会的设计缘起", "知识链接：干栏式建筑")],
    "claim-0091": [("cand-01-21", 324, 324, "line", [324], ["b0023"],
                    "原始社会的设计缘起", "知识链接：人类早期造物活动的发展线索")],
}

patch_rows = []
for claim_id, spans in PATCHES.items():
    for cid, start, end, kind, key_lines, blocks, chapter, section in spans:
        patch_rows.append({
            "claim_id": claim_id,
            "candidate_id": DOC + ":" + cid,
            "corroborating_span": {
                "doc_id": DOC,
                "source_file": SRC,
                "line_start": start,
                "line_end": end,
                "span_kind": kind,
                "key_lines": key_lines,
                "block_ids": blocks,
                "chapter": chapter,
                "section": section,
                "candidate_id": DOC + ":" + cid,
            },
        })

OUT.write_text(json.dumps(ROWS, ensure_ascii=False, indent=1), encoding="utf-8")
PATCH.write_text(json.dumps(patch_rows, ensure_ascii=False, indent=1), encoding="utf-8")

print(json.dumps({
    "claims": len(ROWS),
    "ids": [ROWS[0]["claim_id"], ROWS[-1]["claim_id"]],
    "types": {t: sum(1 for r in ROWS if r["claim_type"] == t)
              for t in sorted({r["claim_type"] for r in ROWS})},
    "confidence": {c: sum(1 for r in ROWS if r["confidence"] == c)
                   for c in sorted({r["confidence"] for r in ROWS})},
    "with_support": sum(1 for r in ROWS if r["supported_by"]),
    "links": sum(len(r["supported_by"]) for r in ROWS),
    "distinct_support": len({p for r in ROWS for p in r["supported_by"]}),
    "patches": len(patch_rows),
    "patch_claims": len(PATCHES),
}, ensure_ascii=False))
