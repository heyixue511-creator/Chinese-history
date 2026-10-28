# -*- coding: utf-8 -*-
"""Build CL3e claim rows (5 new) and 8 cross-edition corroboration patches."""
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


CH = "魏晋南北朝时期的设计变迁"
rows = []

rows.append(C(
    "claim-0317", "historiographic_claim",
    "夏燕靖认为，魏晋南北朝时期已进入到瓷器的时代；瓷器坚固耐用、质量较高，尤其耐酸碱、盛食不变味、易洗涤，因而深受民众欢迎。",
    "Xia Yanjing holds that the Wei, Jin, and Southern and Northern Dynasties had entered the age of porcelain: porcelain was durable and of relatively high quality, especially resistant to acid and alkali, did not taint stored food, and was easy to wash, and was therefore widely welcomed.",
    "medium",
    ["04-knowledge/units/terms/qing-ci.md",
     "04-knowledge/units/works/lianhua-qingci-tuowan.md",
     "04-knowledge/units/procedures/liuchao-qingci-zhuangshi-liufa.md"],
    "断言取 L2076。“进入到瓷器的时代”是来源的分期判断，依据为瓷器耐用、耐酸碱、盛食不变味、易洗涤等使用优势；来源未给瓷器的产量、普及率或替代陶器的量化数据。本条保留分期判断，不把它写成陶瓷考古的统一定名。",
    2074, 2079, "bounded", [2076], ["b0285"],
    CH, "1. 瓷器时代的出现与陶瓷器设计"))

rows.append(C(
    "claim-0318", "synthetic_claim",
    "夏燕靖认为，魏晋南北朝漆器生产规模扩大、产地分布更广；髹漆工艺在髹涂基础上出现彩绘、描金、戗金、填漆等新工艺，并镶玛瑙、琉璃珠、金银扣及金银箔镂刻人物神怪鸟兽，逐渐使漆器走向装饰艺术化。",
    "Xia Yanjing argues that lacquer production in the Wei, Jin, and Southern and Northern Dynasties expanded in scale and spread over a wider area. Beyond simple coating, lacquer crafts added painted decoration, gold tracing, incised gold, and filled lacquer, inlaid agate and glass beads, gold and silver bands, and gold or silver foil cut with figures, deities, birds, and beasts, gradually turning lacquerware toward decorative art.",
    "medium",
    ["04-knowledge/units/terms/diao-qi.md",
     "04-knowledge/units/terms/tuotai-qiqi.md",
     "04-knowledge/units/works/simajinlong-mu-qi-pingfeng.md",
     "04-knowledge/units/terms/liuli.md"],
    "断言取 L2152。来源称新工艺“前所未有”并归纳为漆器“走向装饰艺术化”，但未给各工艺的实物序列、产地统计或产量数据；“生产规模扩大、产地分布更广”也只有扬州、徽州、天水等发掘地点作例证。本条保留来源的工艺清单与趋势判断，不把它写成全时段统一的生产统计。",
    2150, 2157, "bounded", [2152], ["b0294"],
    CH, "2. 漆工艺的发展与特色漆器品种"))

rows.append(C(
    "claim-0319", "factual_claim",
    "夏燕靖指出，北魏时锦的织造和锦纹设计多为平纹经线彩锦，兼有纬线起花；还引进中亚、西亚的菱纹锦、龙纹锦、瑞兽锦、狮纹锦、忍冬菱纹锦、忍冬带联珠纹锦、双兽对鸟纹锦等纹样。",
    "Xia Yanjing states that Northern Wei brocade weaving and pattern design mostly used plain-weave warp-faced polychrome brocade with some weft patterning, and that patterns from Central and West Asia were introduced, including lozenge, dragon, auspicious-beast, lion, honeysuckle-lozenge, honeysuckle with linked-pearl, and paired-beast-and-bird designs.",
    "medium",
    ["04-knowledge/units/terms/zhijin.md",
     "04-knowledge/units/terms/jingjin.md",
     "04-knowledge/units/works/shuxia-duiniao-duiyang-wenjin.md",
     "04-knowledge/units/works/lianzhu-yezhutou-wen-jin.md"],
    "断言取 L2193。来源列出七类引进纹样，但未给各纹样的出土实例、年代序列与传播路线；同句末的“定州、广陵、成都为高级丝织物三大中心”已由 2009 版 claim-0118 记录，本条不重复。平纹经线彩锦与纬线起花的比例，来源只作概括，未给织物组织分析。",
    2193, 2193, "line", [2193], ["b0301"],
    CH, "3. 织印染与服装业的恢复及形成的设计特色 / 1）纺织印染业的恢复和发展 / ② 纺织业的艰难步履"))

rows.append(C(
    "claim-0320", "factual_claim",
    "夏燕靖指出，公元6世纪，脚踏纺车、提花机经大月氏国和波斯传到西方，熟练工匠到中亚、西亚传授纺织工艺；日本多次派专使到江浙求工匠，和服早期用江浙丝绸制成故称“吴服”；6世纪波斯派人学习养蚕丝织并将蚕种带回，6世纪中叶传到拜占庭。",
    "Xia Yanjing states that in the sixth century the treadle spinning wheel and the figured loom reached the West through the Da Yuezhi and Persia, while skilled artisans went to Central and West Asia to teach textile techniques. Japan repeatedly sent envoys to Jiangsu and Zhejiang to seek artisans, and the early kimono was made from Jiangnan silk, hence the name Wufu (Wu costume). In the sixth century Persia sent people to learn sericulture and silk weaving and brought silkworm eggs back, and by the mid-sixth century the technique had reached Byzantium.",
    "medium",
    ["04-knowledge/units/events/6th-century-fangzhi-jishu-waichuan.md",
     "04-knowledge/units/terms/tihuaji.md",
     "04-knowledge/units/terms/jiaota-tizong-xiezhi-ji.md"],
    "断言取 L2239。来源把脚踏纺车、提花机西传、日本求工匠与吴服、波斯学养蚕、拜占庭得蚕种并置叙述，未逐条标注出处；蚕种外传同段另存东罗马皇帝派波斯僧侣藏蚕种于空心竹杖一说，本条保留两说并存，不把单一路径写成定论。",
    2239, 2239, "line", [2239], ["b0308"],
    CH, "3. 织印染与服装业的恢复及形成的设计特色 / 1）纺织印染业的恢复和发展 / ② 印染业的发展"))

rows.append(C(
    "claim-0321", "historiographic_claim",
    "夏燕靖认为，胡床最初以异域“服妖”之物出现在中国家具史上，南梁时已被视为普通日常用具；由此推断中国跪坐传统在魏晋南北朝发生变化，与家具由矮型向高型发展密切相关，胡床的流传和普及推动整个家具形制向高型方向发展，影响远及唐宋。",
    "Xia Yanjing argues that the folding stool (huchuang) first entered Chinese furniture history as an exotic object classed among ominous “strange garments,” and by the Southern Liang was already regarded as an ordinary everyday item. He infers that the Chinese kneeling posture changed during the Wei, Jin, and Southern and Northern Dynasties, closely related to furniture developing from low to high forms, and that the spread and popularization of the huchuang pushed the whole furniture repertoire toward high forms, with influence reaching the Tang and Song.",
    "medium",
    ["04-knowledge/units/terms/huchuang.md",
     "04-knowledge/units/terms/gaoxing-jiaju.md",
     "04-knowledge/units/terms/qimu-jiaju.md",
     "04-knowledge/units/terms/xi-mat.md"],
    "断言取 L2374、L2376、L2378。来源据《后汉书·五行志》与庾肩吾《咏胡床应教诗》推断跪坐传统与家具高型化的关系，并以礼制衰微、士人追求舒适作解释，未给坐姿变化的图像或实物序列；2009 版 claim-0126 已记家具加高与垂足而坐的结果，本条侧重胡床的接受史与因果推断，不重复家具清单。",
    2372, 2386, "bounded", [2374, 2376, 2378], ["b0325"],
    CH, "5. 车船制造及木作业设计 / 2）木作业设计"))

for row in rows:
    row["source"]["candidate_id"] = {
        "claim-0317": DOC + ":cand-04-33",
        "claim-0318": DOC + ":cand-04-44",
        "claim-0319": DOC + ":cand-04-48",
        "claim-0320": DOC + ":cand-04-78",
        "claim-0321": DOC + ":cand-04-57",
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


P("claim-0115", "cand-04-32", 2065, 2073, "bounded", [2070, 2072], ["b0284"],
  "章首")
P("claim-0116", "cand-04-34", 2074, 2079, "bounded", [2078], ["b0285"],
  "1. 瓷器时代的出现与陶瓷器设计")
P("claim-0117", "cand-04-36", 2080, 2085, "bounded", [2084], ["b0286"],
  "1. 瓷器时代的出现与陶瓷器设计 / 1）青瓷")
P("claim-0119", "cand-04-51", 2229, 2232, "bounded", [2231], ["b0307"],
  "知识链接：旷世奇服")
P("claim-0122", "cand-04-53", 2288, 2291, "bounded", [2290], ["b0314"],
  "4. 金属工艺与纹饰设计 / 1）冶铜业的发展")
P("claim-0129", "cand-05-86", 2413, 2424, "bounded", [2415], ["b0330"],
  "6. 建筑与雕刻工艺设计 / 3）石刻与纹饰设计")
P("claim-0130", "cand-05-136", 2429, 2429, "line", [2429], ["b0331"],
  "7. 设计思想的多样性")
P("claim-0131", "cand-05-137", 2431, 2431, "line", [2431], ["b0331"],
  "7. 设计思想的多样性")

(ROOT / "_zn_cl6_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_cl6_patch.json").write_text(
    json.dumps(patches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

print(json.dumps({
    "rows": len(rows),
    "patches": len(patches),
    "types": {t: sum(1 for r in rows if r["claim_type"] == t)
              for t in sorted({r["claim_type"] for r in rows})},
    "confidence": {c: sum(1 for r in rows if r["confidence"] == c)
                   for c in sorted({r["confidence"] for r in rows})},
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
}, ensure_ascii=False))
