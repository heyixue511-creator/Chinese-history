# -*- coding: utf-8 -*-
"""Build CL2c claim rows (Xia Yanjing 2009, ch.4 Qin-Han)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
CH = "秦汉时期的艺术设计"

ROWS = []


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, section):
    ROWS.append({
        "claim_id": None,
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
            "candidate_id": DOC + ":" + cid,
        },
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    })


C("cand-03-06", "interpretive_claim",
  "夏燕靖认为，秦代冶铁业属官营并设有铁官；秦每得一地，必先将该地的冶铁业强迁到秦的大后方或统治稳固的地区，如迁卓氏、程氏于四川，迁孔氏于南阳，其目的是集中控制冶铁业、彻底缴除六国敌对势力的武装；这一措施在客观上使各地冶铁技术得以交流和全面提高。",
  "Xia Yanjing argues that Qin iron smelting was state-run under iron officials; whenever Qin took a territory it first forcibly relocated that region's iron industry to its rear areas or firmly held regions, for example moving the Zhuo and Cheng clans to Sichuan and the Kong clan to Nanyang, in order to centralize control of iron production and completely disarm the hostile forces of the six states; objectively, this measure allowed iron-smelting techniques from different regions to be exchanged and comprehensively raised.",
  "high",
  ["04-knowledge/units/events/qin-qian-yetie-haozu.md",
   "04-knowledge/units/institutions/qin-gongshi-gongguan.md",
   "04-knowledge/units/procedures/ye-tie-shu-qi-yuan.md",
   "04-knowledge/units/terms/iron-farm-tools.md"],
  "候选跨度 L1302-L1314 覆盖小节标题与“铁器时代”知识框，实际断言集中在 L1304 一段，故取单行并以 b0181 为首证块；“彻底缴除六国敌对势力的武装”是作者对政策目的判断，保留原表述，不写成已证史实。",
  1304, 1304, "line", [1304], ["b0181"], "1. 铁制工具的广泛使用")

C("cand-03-09", "historiographic_claim",
  "夏燕靖据文献与出土材料指出，铁器尤其是铁农具的使用兴起于春秋，发展于战国、秦朝，至汉代完全占统治地位，这在我国古代冶金史上占有重要的历史地位。",
  "Citing documents and excavated material, Xia Yanjing states that iron implements, especially iron farm tools, arose in the Spring and Autumn period, developed through the Warring States and Qin, and became fully dominant by the Han; this holds an important place in the history of Chinese metallurgy.",
  "high",
  ["04-knowledge/units/terms/iron-farm-tools.md",
   "04-knowledge/units/terms/tieqi-shidai.md",
   "04-knowledge/units/terms/li-bi.md",
   "04-knowledge/units/terms/ou-li.md",
   "04-knowledge/units/procedures/sheng-tie-ye-zhu-ji-shu.md",
   "04-knowledge/units/publications/yantielun.md"],
  "候选作 periodization，按类型映射路由 historiographic；断言句被图注分隔在 L1329 与 L1331，故记 contiguous 并同时保留两句为 key_lines。犁壁、环首铁刀等例证留在 L1329 前段，未逐项写入断言。",
  1329, 1331, "contiguous", [1329, 1331], ["b0183"], "1. 铁制工具的广泛使用｜秦汉时期的农具")

C("cand-03-10", "interpretive_claim",
  "夏燕靖认为，秦汉时期虽说铁器已非常普遍，但冶铜业的生产规模仍超过之前的战国，冶铸技术有了进一步提高；此时的青铜器制作开始注重生活化和艺术性，铜器除铜镜、灯、炉及盥洗日用品外，还有印符、度量衡、礼器、乐器和工艺品，其中最大宗的便是铸铜钱。",
  "Xia Yanjing argues that although iron implements were already very common in the Qin and Han, the scale of copper smelting still exceeded that of the preceding Warring States and casting techniques improved further; bronze production now began to stress everyday use and artistry, and besides mirrors, lamps, braziers and washing vessels, bronzes included seals and tallies, weights and measures, ritual vessels, musical instruments and crafts, with coin casting the largest category.",
  "high",
  ["04-knowledge/units/terms/qingtongqi.md",
   "04-knowledge/units/terms/qingtong-liqi.md",
   "04-knowledge/units/terms/qin-ban-liang.md",
   "04-knowledge/units/terms/han-wu-zhu.md",
   "04-knowledge/units/institutions/shanglin-sanguan.md"],
  "候选作 interpretation，默认路由 interpretive；候选跨度含 L1333-L1334 的小节标题（b0184），断言本身在 L1337（b0185），故只记 b0185。",
  1337, 1337, "line", [1337], ["b0185"], "2. 冶铜业与铜器设计｜1）冶铜业的发展与青铜制器的提升")

C("cand-03-15", "interpretive_claim",
  "夏燕靖认为，东汉时期铜镜的镜面微凸，可以照出人面的全部，比前期更符合科学原理。",
  "Xia Yanjing argues that in the Eastern Han the mirror surface became slightly convex, so that a person's whole face could be reflected, making it more scientifically sound than earlier mirrors.",
  "high",
  ["04-knowledge/units/terms/tongjing.md",
   "04-knowledge/units/terms/hanjing.md",
   "04-knowledge/units/terms/guijujing.md"],
  "候选作 interpretation；L1375 同段前半还述西汉平雕、中期规矩镜，断言只取东汉镜面微凸一条，不把三期演变整体并入。",
  1375, 1375, "line", [1375], ["b0188"], "2. 冶铜业与铜器设计｜3）铜器的分类型设计｜① 汉镜")

C("cand-03-22", "factual_claim",
  "夏燕靖指出，“丝绸之路”并非汉代已有的固定名称：1877年德国地理学家李希霍芬在《中国》一书中首次把汉代中国和中亚南部、西部以及印度之间以丝绸贸易为主的交通路线称作“丝绸之路”；1910年德国历史学家赫尔曼在《中国和叙利亚之间的古代丝绸之路》中根据新发现的文物考古资料，进一步把丝绸之路延伸到地中海西岸和小亚细亚，并确定为它的基本内涵。",
  "Xia Yanjing notes that “Silk Road” was not a fixed name in Han times: in 1877 the German geographer Ferdinand von Richthofen, in his China, first called the mainly silk-trading routes between Han China, southern and western Central Asia, and India the “Silk Road”; in 1910 the German historian Albert Herrmann, in The Ancient Silk Road between China and Syria, extended it on new archaeological evidence to the eastern Mediterranean and Asia Minor and fixed its basic meaning.",
  "high",
  ["04-knowledge/units/terms/sichou-zhilu.md",
   "04-knowledge/units/events/zhangqian-chushi-xiyu.md"],
  "候选作 attribution，按类型映射路由 factual；这是学术命名史而非汉代事实，断言以“并非汉代已有的固定名称”限定，避免把近代概念回溯为汉代自称。",
  1411, 1411, "line", [1411], ["b0196"], "3. 丝织、印染与服饰设计｜1）绸织造、印染技术提升与丝绸之路开辟｜知识链接：丝绸之路")

C("cand-03-32", "historiographic_claim",
  "夏燕靖认为，随着原料和烧造技术的改进，到东汉晚期，浙江地区终于烧制出成熟的青瓷器。",
  "Xia Yanjing argues that with improvements in raw materials and firing techniques, mature celadon was finally produced in the Zhejiang region by the late Eastern Han.",
  "high",
  ["04-knowledge/units/terms/qing-ci.md",
   "04-knowledge/units/terms/proto-porcelain.md",
   "04-knowledge/units/places/shangyu-yaozhi.md",
   "04-knowledge/units/places/yue-kiln.md",
   "04-knowledge/units/works/donghan-qingci-gaozu-wan.md"],
  "候选作 periodization，路由 historiographic；L1474 同段前半述秦汉官营陶窑与秦砖，断言只取末句的瓷器成熟时点与地域。",
  1474, 1474, "line", [1474], ["b0203"], "4. 陶瓷设计日臻完善｜1）制陶业的进步与瓷器烧制技术的成熟")

C("cand-03-33", "factual_claim",
  "夏燕靖指出，汉代官府制陶业主要是烧制建筑材料，供宫殿、官府衙门修造之用；民间的砖瓦生产也十分发达，多用于民居和墓室的建造。",
  "Xia Yanjing states that Han state pottery production was mainly devoted to building materials for palaces and government offices, while private brick-and-tile production was also well developed and mostly used for houses and tomb chambers.",
  "high",
  ["04-knowledge/units/institutions/qin-han-guan-ying-tao-yao.md",
   "04-knowledge/units/terms/qin-zhuan-han-wa.md",
   "04-knowledge/units/terms/tao-wa.md",
   "04-knowledge/units/terms/wadang.md",
   "04-knowledge/units/terms/huaxiangzhuan.md"],
  "候选作 basic_fact，路由 factual；《三国志》“杜陵南山下，有成瓦窑数千处”是支撑例证，未写入主句。",
  1493, 1493, "line", [1493], ["b0204"], "4. 陶瓷设计日臻完善｜2）建筑材料")

C("cand-03-41", "interpretive_claim",
  "夏燕靖认为，汉代漆器的制作特点首先从实用出发，考虑到使用的方便和放置的容积，其次才考虑装饰效果；多子盒即多件盒在一个大圆盒中容纳多种不同形式的小盒，既节省位置又美观协调，是一种集约性的设计。",
  "Xia Yanjing argues that Han lacquerware making began from practical use, considering convenience of handling and capacity for storage, and only then decorative effect; the multi-compartment box (duozi he) held various small boxes inside one large round box, saving space while remaining visually harmonious—a design of intensive integration.",
  "medium",
  ["04-knowledge/units/terms/qi-jiuju-baozhuang-he.md",
   "04-knowledge/units/procedures/qiqi-mutai-san-zuofa.md",
   "04-knowledge/units/procedures/han-dai-qiqi-zhizuo-fengong.md",
   "04-knowledge/units/works/wunv-qilian.md"],
  "候选作 interpretation；“集约性的设计”是作者以现代设计概念回译汉代器物，保留该判断而不改写为当时人的自我表述；云梦9件漆奁的配色例证未并入。",
  1535, 1535, "line", [1535], ["b0209"], "5. 漆器业的兴盛与漆艺设计｜2）漆艺设计的丰富样式")

C("cand-03-46", "historiographic_claim",
  "夏燕靖把我国造船业的发展概括为三大时期，即秦汉、宋元和明代。",
  "Xia Yanjing summarizes the development of China's shipbuilding industry as three great periods: the Qin-Han, the Song-Yuan, and the Ming.",
  "high",
  ["04-knowledge/units/terms/louchuan.md",
   "04-knowledge/units/terms/plank-boat.md",
   "04-knowledge/units/works/zhenghe-baochuan.md",
   "04-knowledge/units/works/penglai-yuan-zhanshu.md",
   "04-knowledge/units/terms/sida-chuanxing.md"],
  "候选作 periodization，路由 historiographic；L1555 后文列举秦船队、汉楼船、隋唐龙舟海船、宋船与郑和宝船，属分期论证，未逐条写入断言。",
  1555, 1555, "line", [1555], ["b0214"], "6. 车船设计水平的提高｜造船业的发展")

C("cand-03-49", "factual_claim",
  "夏燕靖指出，有学者认为广州发掘的一处遗址是秦汉时的造船工场，它有3个造船平台，船台和滑道相结合，在当时已相当先进；据分析，可造宽8米、长30米、载重60吨的船舶。",
  "Xia Yanjing notes that some scholars regard a site excavated in Guangzhou as a Qin-Han shipyard with three building platforms combining slipways and launch ways, quite advanced for its time; analysis suggests it could build vessels 8 m wide, 30 m long and of 60-ton capacity.",
  "medium",
  ["04-knowledge/units/places/guangzhou-qin-han-zaochuan-gongchang-yizhi.md",
   "04-knowledge/units/institutions/chuangong.md",
   "04-knowledge/units/terms/louchuan.md",
   "04-knowledge/units/terms/plank-boat.md"],
  "候选作 basic_fact，路由 factual；来源以“有学者认为”“据分析”双重限定，断言保留归因，不写成定论。",
  1561, 1561, "line", [1561], ["b0215"], "6. 车船设计水平的提高｜2）造船业与船运")

C("cand-03-57", "interpretive_claim",
  "夏燕靖认为，张骞出使西域时在大夏市场上见到从印度转运去的四川竹杖和蜀布，说明巴蜀到印度再到西亚早就存在一条通道，这便是史家按惯例所称的“南方丝绸之路”。",
  "Xia Yanjing argues that when Zhang Qian went to the Western Regions he saw Sichuan bamboo staffs and Shu cloth in the markets of Daxia, brought there via India, which shows that a route from Ba-Shu through India to West Asia already existed—what historians conventionally call the “Southern Silk Road.”",
  "medium",
  ["04-knowledge/units/persons/zhang-qian.md",
   "04-knowledge/units/events/zhangqian-chushi-xiyu.md",
   "04-knowledge/units/terms/sichou-zhilu.md"],
  "候选作 interpretation；由市场见闻反推通道存在的推论性质保留在“说明”一词，未改写为直接考古证明；“南方丝绸之路”标明为史家惯例称谓。",
  1596, 1596, "line", [1596], ["b0219"], "7. 建筑设计与木作业｜3）竹木作业")

C("cand-03-63", "interpretive_claim",
  "夏燕靖认为，秦汉时期是我国古代设计理论形成的重要时期，其开始形成的主要特征是文献中出现重皇权以及典章制度制定和执行的记述；汉代“罢黜百家、独尊儒术”后，美学乃至工艺理论中贯穿的主要是儒家的礼教观点。",
  "Xia Yanjing argues that the Qin-Han was an important period for the formation of ancient Chinese design theory, whose main emerging feature was the appearance in texts of records stressing imperial authority and the making and enforcement of statutes and institutions; after the Han “rejected the Hundred Schools and revered Confucianism alone,” aesthetics and craft theory were pervaded mainly by Confucian ritual doctrine.",
  "medium",
  ["04-knowledge/units/events/han-wudi-duzun-rushu.md",
   "04-knowledge/units/terms/li-yue-zhidu.md",
   "04-knowledge/units/terms/cangli-yuqi.md",
   "04-knowledge/units/terms/zhiqi-shangxiang.md",
   "04-knowledge/units/publications/liji.md",
   "04-knowledge/units/terms/handai-guanzhi.md"],
  "候选作 interpretation，默认路由 interpretive；本条兼具分期判断，但主语是“设计理论形成的重要时期”及其特征，未改路由 historiographic。董仲舒《春秋繁露》与《后汉书·舆服志》引文留在来源，未逐句写入断言。",
  1638, 1638, "line", [1638], ["b0223"], "9. 秦汉时期的文献典籍中的设计理论")


def main():
    assert len(ROWS) == 12, len(ROWS)
    types = {"factual_claim", "interpretive_claim", "synthetic_claim",
             "evaluative_claim", "contested_claim", "historiographic_claim"}
    seen = set()
    for i, row in enumerate(ROWS):
        row["claim_id"] = "claim-%04d" % (103 + i)
        assert row["claim_type"] in types, row["claim_type"]
        assert row["confidence"] in {"high", "medium", "low"}
        assert row["statement_zh"].startswith("夏燕靖"), row["claim_id"]
        assert row["statement_en"].strip()
        assert row["discussion_notes"].strip()
        assert row["consensus"] == "tentative"
        assert row["review_status"] == "source_backed"
        cid = row["source"]["candidate_id"]
        assert cid not in seen, cid
        seen.add(cid)
        sp = row["source"]["source_span"]
        assert 1279 <= sp["line_start"] <= sp["line_end"] <= 1661, sp
        assert sp["key_lines"] and all(sp["line_start"] <= x <= sp["line_end"] for x in sp["key_lines"]), sp
        assert sp["block_ids"], sp
        assert sp["span_kind"] in {"line", "contiguous", "bounded"}
        if sp["span_kind"] == "line":
            assert sp["line_start"] == sp["line_end"]
        for p in row["supported_by"]:
            assert p.startswith("04-knowledge/units/"), p
            assert (ROOT / p).exists(), p
    assert len({r["source"]["candidate_id"] for r in ROWS}) == 12
    (ROOT / "_zn_claim_xyj09c_rows.json").write_text(
        json.dumps(ROWS, ensure_ascii=False, indent=2), encoding="utf-8")
    from collections import Counter
    print(json.dumps({
        "claims": len(ROWS),
        "with_support": sum(1 for r in ROWS if r["supported_by"]),
        "links": sum(len(r["supported_by"]) for r in ROWS),
        "distinct_support": len({p for r in ROWS for p in r["supported_by"]}),
        "types": dict(Counter(r["claim_type"] for r in ROWS)),
        "confidence": dict(Counter(r["confidence"] for r in ROWS)),
        "span_kinds": dict(Counter(r["source"]["source_span"]["span_kind"] for r in ROWS)),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
