# -*- coding: utf-8 -*-
"""Build CL6a claim rows (8 new) and 9 cross-edition corroboration patches.

Chapter: 元代的设计交融 (L3595-L4110), 17 claim candidates.
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


CH = "元代的设计交融"
rows = []

rows.append(C(
    "claim-0338", "evaluative_claim",
    "夏燕靖认为，元代钧瓷能有意识地使蓝紫两种釉料分别聚散成形，掌握釉料变化并提高烧造技术，是元代钧窑的进步；但其釉质粗糙、胎骨笨厚，不及宋钧精细。",
    "Xia Yanjing holds that Yuan Jun ware shows deliberate control in dispersing and gathering blue and purple glazes and improved firing technique, marking progress for the Yuan Jun kiln; yet its glaze is coarse and its body thick and clumsy, less refined than Song Jun ware.",
    "medium",
    ["04-knowledge/units/places/jun-kiln.md",
     "04-knowledge/units/terms/yaobian.md"],
    "断言取 L3636 的对比评价。来源先引许之衡《饮流斋说瓷》区分元钧与宋钧的釉色，再以故宫藏品对照，作出“进步”与“不及宋钧精细”的双向判断；未给窑址统计、化验数据或断代序列。窑变机理另见 terms/yaobian。",
    3636, 3636, "line", [3636], ["b0458"],
    "1. 瓷器工艺与设计 / 1）元代名窑"))

rows.append(C(
    "claim-0339", "historiographic_claim",
    "夏燕靖认为，为满足贵族统治者奢华生活的需要，官府投入极大精力经营染织业，同时使元代染织工艺水平达到一个新的高峰。",
    "Xia Yanjing argues that to satisfy the luxurious life of the aristocratic rulers the government devoted great effort to state-run weaving and dyeing, which also brought Yuan textile craft to a new peak.",
    "medium",
    ["04-knowledge/units/institutions/jiankanglu-zhiranju.md",
     "04-knowledge/units/institutions/nashishiju.md",
     "04-knowledge/units/terms/nashishi.md"],
    "断言取 L3708 的因果评价，前接《金陵新志》所记建康路东织染局人匠三千六百户、织机一百五十四张、额造段匹四千五百二十七段。来源未给全国织造总量或与宋、明的量化比较；官营染织机构另见 institutions/jiankanglu-zhiranju、nashishiju，织金锦“纳石失”另见 terms/nashishi。",
    3708, 3708, "line", [3708], ["b0466"],
    "2. 染织工艺及其品种设计"))

rows.append(C(
    "claim-0340", "interpretive_claim",
    "夏燕靖认为，黄道婆对棉纺织工具和技术的改进具有重大历史意义，推动了长江下游棉纺织业的发展；从此棉织与丝织并列，成为我国纺织业的两大体系。",
    "Xia Yanjing argues that Huang Daopo's improvements to cotton spinning tools and techniques were of major historical significance, advancing cotton textiles in the lower Yangtze region; thereafter cotton and silk stood side by side as the two great systems of Chinese textile production.",
    "medium",
    ["04-knowledge/units/persons/huang-daopo.md",
     "04-knowledge/units/places/songjiang-fu.md",
     "04-knowledge/units/publications/wang-zhen-nongshu.md"],
    "断言取 L3730。黄道婆生平、三锭脚踏纺棉车与《辍耕录》引文在 L3762-L3764 知识链接，未并入断言；松江“衣被天下”与棉植范围另见 claim-0207。来源未给棉布产量、纺车效率或长江下游织户数量的统计，“重大历史意义”为作者评价。",
    3730, 3730, "line", [3730], ["b0469"],
    "2. 染织工艺及其品种设计 / 1）丝织工艺和织金锦工艺"))

rows.append(C(
    "claim-0341", "factual_claim",
    "夏燕靖指出，元代铜器制作虽呈萎缩趋势，但铜的年产量仍维持在百万斤的水平。",
    "Xia Yanjing notes that although bronze vessel making declined in the Yuan, annual copper output was still maintained at the level of one million jin.",
    "medium",
    ["04-knowledge/units/procedures/jintong-fa.md",
     "04-knowledge/units/works/yuan-huoqiang.md"],
    "断言取 L3847。同段所记唐代宣宗年间 26 万斤、宋太宗时 412 万斤、神宗时 1460 万斤的对比序列留在来源，未写入断言；浸铜法与铜质火铳分别见 procedures/jintong-fa、works/yuan-huoqiang。百万斤为教材概括，未给出处、统计口径与年度序列。",
    3847, 3847, "line", [3847], ["b0483"],
    "知识链接：古代铜产量与金属制器"))

rows.append(C(
    "claim-0342", "factual_claim",
    "夏燕靖指出，元代兵器工业是优先发展的行业；灭南宋后，朝廷从组织管理机构方面予以保证，并对制造技术进行督导，兵器制造技术因此有较大提高。",
    "Xia Yanjing states that the weapons industry was a priority sector in the Yuan; after conquering the Southern Song the court guaranteed it through organizational and administrative bodies and supervised manufacturing techniques, so that weapons production technology improved considerably.",
    "medium",
    ["04-knowledge/units/works/yuan-huoqiang.md",
     "04-knowledge/units/works/zhishun-sannian-tong-huoqiang.md",
     "04-knowledge/units/procedures/jintong-fa.md"],
    "断言取 L3869 的机构保证、技术督导与提高判断；同段的铜质火铳表面光净、浸铜法与应用化学方法留在来源，浸铜法已由 claim-0210 承接。来源未给兵器产量、工场数量或技术指标；元代火铳实物另有 works/yuan-huoqiang、zhishun-sannian-tong-huoqiang。",
    3869, 3869, "line", [3869], ["b0486"],
    "4. 金属工艺及品种设计特色 / 1）金属工艺的继承与发展"))

rows.append(C(
    "claim-0343", "historiographic_claim",
    "夏燕靖认为，元大都是自唐都长安以来又一个规模巨大而有完整规划的都城，并为明清两代继承下来，奠定了以后600多年以北京为政治中心的统一国家都城局面。",
    "Xia Yanjing argues that Yuan Dadu was another vast and fully planned capital after Tang Chang'an; inherited by the Ming and Qing, it established Beijing as the political center of a unified state for more than 600 years.",
    "medium",
    ["04-knowledge/units/places/yuan-dadu.md",
     "04-knowledge/units/works/beijing-zijincheng.md"],
    "断言取 L3954。“600多年”为来源概括，未给辽、金、元、明、清建都北京的完整纪年序列；城墙长度、面积与九经九纬布局在 L3977 知识链接，另由 claim-0344 承接规划思想。明清北京城对元大都的继承见 works/beijing-zijincheng。",
    3954, 3954, "line", [3954], ["b0494"],
    "6. 建筑与装饰纹样设计"))

rows.append(C(
    "claim-0344", "interpretive_claim",
    "夏燕靖认为，元大都的总体布局完全符合我国古代传统文化地理观念，也是严格按照《易经》思想指导下的《周礼·考工记》来规划布局，充分体现了“周王礼制”的国都规划制度。",
    "Xia Yanjing argues that the overall layout of Yuan Dadu fully accords with traditional Chinese cultural-geographical ideas and was laid out strictly according to the Zhouli Kaogongji as guided by Yijing thought, fully embodying the Zhou royal ritual system of capital planning.",
    "medium",
    ["04-knowledge/units/places/yuan-dadu.md",
     "04-knowledge/units/publications/zhouli.md",
     "04-knowledge/units/publications/kaogongji.md"],
    "断言取 L3977 知识链接末段。方形城制、周长 28600 米、九经九纬与祖庙、社稷坛位置留在同段；“完全符合”“严格按照”为作者的规划思想阐释，未给《周礼·考工记》原文比对或考古实测。城址另见 places/yuan-dadu，文献另见 publications/zhouli、kaogongji。",
    3977, 3977, "line", [3977], ["b0497"],
    "知识链接：元大都城规划"))

rows.append(C(
    "claim-0345", "interpretive_claim",
    "夏燕靖认为，元代商业美术设计作为促销的手段之一，确实为商业的发展起到了促进作用。",
    "Xia Yanjing holds that commercial art and design in the Yuan, as one means of sales promotion, did promote the development of commerce.",
    "medium",
    ["04-knowledge/units/terms/zhaopai.md",
     "04-knowledge/units/publications/zhongguo-guanggao.md"],
    "断言取 L4077 首句。同段的“装点门面”与沿袭宋代“俗以招幌，谓之装潢”之说已由 claim-0219 承接，本条只记促销功能的因果判断；来源未给商号数量、广告支出或销售增长的统计，也未区分招牌、店匾与陈列各自的效果。招牌形制见 terms/zhaopai。",
    4077, 4077, "line", [4077], ["b0507"],
    "7. 印刷、家具与商业美术 / 3）商业的繁荣与商业美术"))

patches = [
    P("claim-0197", "cand-06-75", 3621, 3621, "line", [3621], ["b0457"],
      "知识链接：取消科举制"),
    P("claim-0198", "cand-06-76", 3628, 3628, "line", [3628], ["b0457"],
      "1. 瓷器工艺与设计"),
    P("claim-0200", "cand-07-63", 3653, 3653, "line", [3653], ["b0459"],
      "1. 瓷器工艺与设计 / 2）元代瓷器的造型特色"),
    P("claim-0202", "cand-07-65", 3694, 3694, "line", [3694], ["b0465"],
      "1. 瓷器工艺与设计 / 3）元代瓷器的装饰风格"),
    P("claim-0206", "cand-07-68", 3744, 3744, "line", [3744], ["b0469"],
      "2. 染织工艺及其品种设计 / 1）丝织工艺和织金锦工艺"),
    P("claim-0209", "cand-07-98", 3867, 3867, "line", [3867], ["b0486"],
      "4. 金属工艺及品种设计特色 / 1）金属工艺的继承与发展"),
    P("claim-0211", "cand-07-73", 3926, 3926, "line", [3926], ["b0492"],
      "5. 农业器具与天文器具的设计记载 / 1）王祯《农书》和秧马记载"),
    P("claim-0216", "cand-07-91", 4010, 4010, "line", [4010], ["b0500"],
      "7. 印刷、家具与商业美术"),
    P("claim-0218", "cand-07-71", 4054, 4054, "line", [4054], ["b0504"],
      "7. 印刷、家具与商业美术 / 2) 家具及制作工艺"),
]

MAP = {
    "claim-0338": "cand-07-64",
    "claim-0339": "cand-07-66",
    "claim-0340": "cand-07-67",
    "claim-0341": "cand-07-96",
    "claim-0342": "cand-07-99",
    "claim-0343": "cand-07-69",
    "claim-0344": "cand-07-70",
    "claim-0345": "cand-07-92",
}
for r in rows:
    r["source"]["candidate_id"] = DOC + ":" + MAP[r["claim_id"]]

(ROOT / "_zn_cl9_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_cl9_patch.json").write_text(
    json.dumps(patches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

print(json.dumps({
    "rows": len(rows),
    "patches": len(patches),
    "patch_claims": len({p["claim_id"] for p in patches}),
    "types": {t: sum(1 for r in rows if r["claim_type"] == t)
              for t in sorted({r["claim_type"] for r in rows})},
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
}, ensure_ascii=False))
