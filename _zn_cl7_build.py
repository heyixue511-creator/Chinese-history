# -*- coding: utf-8 -*-
"""Build CL4a claim rows (11 new) and 18 cross-edition corroboration patches.

Chapter: 隋唐五代时期的设计繁荣 (L2461-L3055), 29 claim candidates.
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
      key_lines, block_ids, chapter, section):
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


CH = "隋唐五代时期的设计繁荣"
rows = []

rows.append(C(
    "claim-0322", "factual_claim",
    "夏燕靖指出，隋朝结束了魏晋以来长达300多年的分裂局面，开创了自秦汉以后又一个统一局面，为唐朝的繁荣奠定了坚实基础；隋朝创立的三省六部制、科举制推动了封建政治昌明，大运河的开挖为南北沟通与经济繁荣开创了新局面。",
    "Xia Yanjing states that the Sui dynasty ended more than three centuries of division since the Wei and Jin, created another unified order after Qin and Han, and laid a solid foundation for the prosperity of the Tang. The Three Departments and Six Ministries and the imperial examination system established under the Sui promoted orderly government, and the digging of the Grand Canal opened a new phase of north-south communication and economic prosperity.",
    "medium",
    ["04-knowledge/units/events/sui-conquers-chen.md",
     "04-knowledge/units/events/sui-pinghui-jiankang.md"],
    "断言取 L2477。来源把三省六部制、科举制与大运河并列为隋朝遗产，未给制度文本、运河长度或经济后果数据；“300多年”按来源口径保留。隋唐鼎盛的分期判断另由 claim-0132 承接，本条不重复。",
    2477, 2477, "line", [2477], ["b0336"],
    CH, "章首"))

rows.append(C(
    "claim-0323", "historiographic_claim",
    "夏燕靖把隋唐文化概括为丰富多彩、兼容并蓄、承前启后三大特点，认为它是我国封建时代文化发展的高峰标志，唐代文化尤被誉为“诗意华章”。",
    "Xia Yanjing summarizes Sui-Tang culture under three features — rich and varied, inclusive and syncretic, and carrying the past into the future — and regards it as the peak marker of culture in China's feudal era, with Tang culture in particular praised as “poetic splendor”.",
    "medium",
    ["04-knowledge/units/terms/tangzhuang.md",
     "04-knowledge/units/publications/quan-tangshi.md"],
    "断言取 L2496。“三大特点”与“高峰标志”是来源的总括判断；“诗意华章”在来源中兼指诗文与服饰，本条保留合称，不拆成文学史与服饰史两条，也未给文化史分期依据。",
    2491, 2503, "bounded", [2496], ["b0339"],
    CH, "知识链接：隋唐文化"))

rows.append(C(
    "claim-0324", "interpretive_claim",
    "夏燕靖认为，唐中期实行的纳资代役使工匠获得较大自由、有利于劳动生产率提高，在一定程度上也是促进手工业行会自身改进的动力。",
    "Xia Yanjing argues that the mid-Tang substitution of taxes for corvée (nazi daiyi) gave artisans greater freedom and favored higher labor productivity, and was to a certain extent a driving force for the improvement of craft guilds themselves.",
    "medium",
    ["04-knowledge/units/terms/shougongye-hanghui.md",
     "04-knowledge/units/terms/li-yue-zhidu.md"],
    "断言取 L2525。来源同时指出纳资代役意味着剥削量增加，本条保留“在一定程度上”的限定，不把它写成行会改进的唯一原因；行首、师傅、徒工等组织细节留在来源。",
    2518, 2528, "bounded", [2525], ["b0343"],
    CH, "1. 手工业的兴盛与设计水平的提升 / 3）手工业行会组织"))

rows.append(C(
    "claim-0325", "historiographic_claim",
    "夏燕靖认为，从隋唐五代手工业繁荣的形势看，这是我国手工业技术发展的关键时期；在此基础上，我国设计和工艺制造业形成了特有且已具成熟的经验体系。",
    "Xia Yanjing holds that, judging from the prosperity of handicraft in the Sui, Tang, and Five Dynasties, this was a key period in the development of Chinese handicraft technology, and that design and craft manufacturing formed a distinctive and already mature body of experience on that basis.",
    "medium",
    ["04-knowledge/units/terms/shougong-gongchang.md",
     "04-knowledge/units/terms/tangci.md",
     "04-knowledge/units/terms/tangzhuang.md"],
    "断言取 L2533。同段“中外文化科技交流的高潮”已由 2009 版 claim-0136 记录，本条不重复；“关键时期”与“经验体系”是作者的总括判断，未给技术指标或行业统计。",
    2529, 2534, "bounded", [2533], ["b0344"],
    CH, "1. 手工业的兴盛与设计水平的提升 / 4）五代手工业"))

rows.append(C(
    "claim-0326", "historiographic_claim",
    "夏燕靖认为，我国制瓷业经过三国两晋南北朝的大发展，到唐代形成我国陶瓷史上第一个高峰，青瓷则是其主流；唐代青瓷窑场众多，南方几乎各省区皆有，北方青瓷也得到发展，青瓷仍是唐代居民最钟爱、使用最普遍的瓷器。",
    "Xia Yanjing holds that after the great expansion of porcelain making in the Three Kingdoms, Jin, and Southern and Northern Dynasties, the Tang formed the first peak in China's ceramic history, with celadon as its mainstream. Tang celadon kilns were numerous, found in almost every southern province, northern celadon also developed, and celadon remained the porcelain most favored and most widely used by Tang residents.",
    "medium",
    ["04-knowledge/units/terms/tang-dai-qingci-yao.md",
     "04-knowledge/units/places/yue-kiln.md",
     "04-knowledge/units/terms/mise-porcelain.md"],
    "断言取 L2578。“第一个高峰”与“主流”是来源的分期与结构判断，未给窑址统计或产量数据；同段列举的瓯窑、婺州窑、岳州窑、长沙窑、洪州窑、寿州窑、邛窑等窑名留在来源。",
    2576, 2585, "bounded", [2578], ["b0350"],
    CH, "2. 陶瓷工艺与陶瓷设计的发展 / 2）重要的陶瓷类别 / ① 青瓷（知识链接：唐代著名青瓷窑）"))

rows.append(C(
    "claim-0327", "interpretive_claim",
    "夏燕靖认为，唐贞观以后国力强盛、百业俱兴导致厚葬之风日盛；唐三彩作为冥器曾被列入官府丧葬明文规定，按品级随葬，这是唐三彩迅速在中原地区发展和兴起的一个主要原因。",
    "Xia Yanjing argues that after the Zhenguan era the Tang's strong national power and general prosperity led to a growing vogue for lavish burials; Tang sancai, used as a tomb figurine ware, was written into official burial regulations with grades of grave goods, and this was a principal reason for its rapid rise and spread in the Central Plains.",
    "medium",
    ["04-knowledge/units/terms/tang-sancai.md",
     "04-knowledge/units/terms/mingqi.md",
     "04-knowledge/units/works/sancai-shuangyu-hu.md"],
    "断言取 L2618。来源把厚葬制度与风气列为唐三彩兴起的主因，未给官府丧葬令原文、随葬品数量或窑址产量；安史之乱后唐三彩衰退的叙述留在来源，唐三彩三期兴衰另由 claim-0143 承接。",
    2607, 2627, "bounded", [2618], ["b0356"],
    CH, "2. 陶瓷工艺与陶瓷设计的发展 / 2）重要的陶瓷类别 / ④ 唐三彩"))

rows.append(C(
    "claim-0328", "evaluative_claim",
    "夏燕靖认为，介质印花以助剂为印染原料，须依染料性能浸染：碱剂可使生丝胶膨胀脱落而显出白色花纹，也可用明矾胶浆等媒染剂印花或清除媒染剂印花；介质印花是我国古代印染技术的一大进步。",
    "Xia Yanjing holds that medium printing (jiezi yinhua) uses assistants as printing materials and requires immersion dyeing according to the dye's properties: alkali can swell and remove sericin to reveal white patterns, and alum paste or similar mordants can be used to print or to clear mordants; medium printing was a major advance in ancient Chinese dyeing technology.",
    "medium",
    ["04-knowledge/units/procedures/jiezhi-yinhua.md",
     "04-knowledge/units/terms/jiaxie.md"],
    "断言取 L2711。“一大进步”是来源的评价性判断；碱剂印花与媒染剂印花两种做法并列，本条不把它们写成同一工艺，也未给工艺试验或年代序列。",
    2709, 2714, "bounded", [2711], ["b0371"],
    CH, "4. 服装工艺与服饰设计的特色形成 / 知识链接：介质印花"))

rows.append(C(
    "claim-0329", "factual_claim",
    "夏燕靖指出，唐镜制作符合科学原理，铜锡铅比例约为70:25:5，加锡较多使镜面呈白色、花纹清晰；为在小镜面上照到全脸，镜面微向外凸，类似现代汽车的反光镜，沈括《梦溪笔谈》已有相关说明。",
    "Xia Yanjing states that Tang mirrors were made on scientific principles, with a copper-tin-lead ratio of about 70:25:5; the high tin content gave a white surface with clear patterns. To reflect a whole face in a small mirror the surface was made slightly convex, similar to a modern car mirror, as already explained in Shen Kuo's Dream Pool Essays.",
    "medium",
    ["04-knowledge/units/terms/tangjing.md",
     "04-knowledge/units/works/tang-dai-tong-zhenzhi.md",
     "04-knowledge/units/terms/tangjing-tuzhi-wushi.md"],
    "断言取 L2847。合金比例与凸面设计按来源照录；“非常符合科学原理”是来源的现代解释，本条保留数字与功能说明，不写成检测报告；沈括引文只作佐证，未核对版本与页码。",
    2845, 2848, "bounded", [2847], ["b0383"],
    CH, "5. 金属工艺设计的成熟 / 3）铜器工艺的高度发达"))

rows.append(C(
    "claim-0330", "evaluative_claim",
    "夏燕靖认为，李春于595-605年设计修建的赵州桥是现存最早的双曲石拱桥，大桥拱两端各有两个小拱，是世界上首创“敞肩拱”桥型；从建筑设计角度说，赵州桥在桥址选择、建筑材料与力学性能等方面都达到了当时建桥的最高水平。",
    "Xia Yanjing holds that the Zhaozhou Bridge, designed and built by Li Chun in 595-605, is the earliest surviving double-curved stone arch bridge; with two small arches at each end of the main arch, it pioneered the open-spandrel arch type. In architectural design terms, it reached the highest level of bridge building of its time in site selection, materials, and structural performance.",
    "medium",
    ["04-knowledge/units/works/zhaozhou-qiao-595-605.md",
     "04-knowledge/units/terms/gongzixing-jiegou.md"],
    "断言取 L2894。“世界首创”与“最高水平”是来源的评价，未给同类桥梁的比较范围与断代依据；桥长50余米、宽9米多、跨度37米余等数据留在来源。",
    2892, 2953, "bounded", [2894], ["b0387"],
    CH, "7. 建筑设计的成熟与繁荣"))

rows.append(C(
    "claim-0331", "evaluative_claim",
    "夏燕靖指出，大兴城于开皇二年（582）6月开始营建，当年12月基本竣工，次年3月迁入使用，前后仅用9个月，是世界都市建设史上的一大奇迹。",
    "Xia Yanjing states that Daxing City began construction in the sixth month of Kaihuang 2 (582), was essentially completed in the twelfth month of that year, and was occupied in the third month of the next year — nine months in all — which he calls a marvel in the history of world urban construction.",
    "medium",
    ["04-knowledge/units/places/daxing-cheng.md",
     "04-knowledge/units/persons/yuwen-kai.md"],
    "断言取 L2926。营建起止月份按来源照录，“9个月”是来源的合计；“世界都市建设史上的一大奇迹”是评价性判断，未给同时期世界城市的比较数据。城区区划判断另由 claim-0158 承接。",
    2892, 2953, "bounded", [2926], ["b0387"],
    CH, "7. 建筑设计的成熟与繁荣 / 宇文恺"))

rows.append(C(
    "claim-0332", "historiographic_claim",
    "夏燕靖指出，隋唐佛教建筑遍布全国，留存至今的唐代木结构殿堂建筑仅两座，即山西五台山境内的南禅寺大殿和佛光寺大殿；二者以内外柱列和梁枋互相联结组成稳固整体，至今十分完好。",
    "Xia Yanjing states that Buddhist architecture spread throughout the country in the Sui and Tang, but only two Tang timber-frame halls survive: the Main Hall of Nanchan Temple and the Main Hall of Foguang Temple, both at Mount Wutai in Shanxi. Both join inner and outer colonnades with beams to form a stable whole and remain in good condition.",
    "medium",
    ["04-knowledge/units/works/nanchan-si-dadian.md",
     "04-knowledge/units/works/foguang-si-dadian.md"],
    "断言取 L2944。“仅两座”是来源的存世数量判断，未给普查范围与断代依据；斗拱、出檐、琉璃与砖塔三型等形制描述留在来源，建筑整体风格评价另由 claim-0159 承接。",
    2892, 2953, "bounded", [2944], ["b0387"],
    CH, "7. 建筑设计的成熟与繁荣"))

for row in rows:
    row["source"]["candidate_id"] = {
        "claim-0322": DOC + ":cand-05-88",
        "claim-0323": DOC + ":cand-05-138",
        "claim-0324": DOC + ":cand-05-90",
        "claim-0325": DOC + ":cand-05-139",
        "claim-0326": DOC + ":cand-05-92",
        "claim-0327": DOC + ":cand-05-95",
        "claim-0328": DOC + ":cand-05-140",
        "claim-0329": DOC + ":cand-05-103",
        "claim-0330": DOC + ":cand-05-105",
        "claim-0331": DOC + ":cand-05-106",
        "claim-0332": DOC + ":cand-05-109",
    }[row["claim_id"]]

patches = []


def P(claim_id, candidate_id, start, end, kind, key_lines, block_ids, section):
    patches.append({
        "claim_id": claim_id,
        "candidate_id": DOC + ":" + candidate_id,
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
            "candidate_id": DOC + ":" + candidate_id,
        },
    })


P("claim-0132", "cand-05-87", 2463, 2482, "bounded", [2475, 2479], ["b0336"], "章首")
P("claim-0134", "cand-05-89", 2485, 2511, "bounded", [2487, 2510],
  ["b0338", "b0339", "b0340", "b0341"], "1. 手工业的兴盛与设计水平的提升 / 1）官营手工业的兴盛")
P("claim-0139", "cand-05-91", 2563, 2566, "bounded", [2565], ["b0347"],
  "2. 陶瓷工艺与陶瓷设计的发展 / 2）重要的陶瓷类别")
P("claim-0140", "cand-05-93", 2576, 2585, "bounded", [2582], ["b0350"],
  "2. 陶瓷工艺与陶瓷设计的发展 / 2）重要的陶瓷类别 / ① 青瓷")
P("claim-0141", "cand-05-94", 2600, 2606, "bounded", [2605], ["b0355"],
  "2. 陶瓷工艺与陶瓷设计的发展 / 知识链接：唐代秘色瓷")
P("claim-0145", "cand-05-96", 2634, 2639, "bounded", [2636], ["b0358"],
  "3. 纺织及印染业的进步与品种的丰富多彩 / 1）丝织业")
P("claim-0146", "cand-05-98", 2659, 2666, "bounded", [2663], ["b0362"],
  "3. 纺织及印染业的进步与品种的丰富多彩 / ② 锦")
P("claim-0147", "cand-05-97", 2642, 2654, "bounded", [2644], ["b0360"],
  "3. 纺织及印染业的进步与品种的丰富多彩 / 知识链接：陵阳公样")
P("claim-0150", "cand-05-99", 2715, 2730, "bounded", [2723], ["b0372"],
  "4. 服装工艺与服饰设计的特色形成 / 1）男服")
P("claim-0153", "cand-05-100", 2796, 2820, "bounded", [2798], ["b0380"],
  "5. 金属工艺设计的成熟 / 2）金银器的制作工艺与设计特色")
P("claim-0154", "cand-05-101", 2835, 2848, "bounded", [2837], ["b0383"],
  "5. 金属工艺设计的成熟 / 知识链接：伊斯兰文化")
P("claim-0154", "cand-05-102", 2835, 2848, "bounded", [2837], ["b0383"],
  "5. 金属工艺设计的成熟 / 知识链接：伊斯兰文化")
P("claim-0155", "cand-05-141", 2835, 2848, "bounded", [2845], ["b0383"],
  "5. 金属工艺设计的成熟 / 3）铜器工艺的高度发达")
P("claim-0156", "cand-05-104", 2851, 2863, "bounded", [2857], ["b0385"],
  "6. 造船与家具制造业的发展与设计特色 / 1）造船业")
P("claim-0163", "cand-05-108", 2995, 3021, "bounded", [3020], ["b0394"],
  "9. 唐代设计理论述要")
P("claim-0163", "cand-06-63", 3024, 3027, "bounded", [3026], ["b0396"],
  "9. 唐代设计理论述要 / 知识链接：〈梓人传〉")
P("claim-0164", "cand-05-142", 2974, 2981, "bounded", [2980], ["b0391"],
  "8. 五代十国时期的设计特征 / 1）陶瓷工艺")
P("claim-0165", "cand-05-107", 2986, 2994, "bounded", [2990], ["b0393"],
  "8. 五代十国时期的设计特征")

(ROOT / "_zn_cl7_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_cl7_patch.json").write_text(
    json.dumps(patches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

print(json.dumps({
    "rows": len(rows),
    "patches": len(patches),
    "patch_claims": len({p["claim_id"] for p in patches}),
    "types": {t: sum(1 for r in rows if r["claim_type"] == t)
              for t in sorted({r["claim_type"] for r in rows})},
    "confidence": {c: sum(1 for r in rows if r["confidence"] == c)
                   for c in sorted({r["confidence"] for r in rows})},
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
}, ensure_ascii=False))
