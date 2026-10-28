# -*- coding: utf-8 -*-
"""Build CL2d claim rows (Xia Yanjing 2009, ch.5 Wei-Jin Southern-Northern)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
CH = "魏晋南北朝时期的艺术设计"

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


C("cand-03-64", "historiographic_claim",
  "夏燕靖认为，魏晋南北朝长期分裂动乱使私营手工业普遍低迷、一般手工业多为官府垄断，但官营手工业与政权存亡密切相关而备受重视，生产技术仍有所提高，因此这一时期艺术设计在曲折中有所发展。",
  "Xia Yanjing argues that the long division and turmoil of the Wei, Jin, and Southern and Northern Dynasties left private handicrafts depressed and most general handicrafts under official monopoly; yet official workshops, tied to the survival of the regime, were highly valued and still raised their production techniques, so art design of the period developed along a tortuous path.",
  "high",
  ["04-knowledge/units/terms/liuchao-gongjiang-zhidu.md",
   "04-knowledge/units/institutions/jinshu.md",
   "04-knowledge/units/institutions/nanchao-ranshu.md"],
  "候选作 periodization，按类型映射路由 historiographic；候选跨度 L1662-L1670 含章标题与图注，实际断言句被空行分为 L1667 与 L1669 两段，故记 contiguous 并以两句为 key_lines；图 5-1 与历史地图说明未写入断言。",
  1667, 1669, "contiguous", [1667, 1669], ["b0227"], "章首导论")

C("cand-03-65", "interpretive_claim",
  "夏燕靖指出，北齐时北方成功烧出白瓷，白瓷的出现是瓷器发展史上划时代的大事；有了白瓷，才有青花、釉里红、斗彩、五彩、粉彩等各种彩绘瓷器。",
  "Xia Yanjing holds that northern potters succeeded in firing white porcelain under the Northern Qi, an epoch-making event in ceramic history, because only with white porcelain could later painted wares such as blue-and-white, underglaze red, doucai, wucai, and famille rose emerge.",
  "high",
  ["04-knowledge/units/terms/baici.md",
   "04-knowledge/units/terms/blue-and-white-porcelain.md",
   "04-knowledge/units/terms/youlihong-ci.md",
   "04-knowledge/units/terms/doucai.md"],
  "候选作 interpretation，默认路由 interpretive；“划时代”与“有了白瓷才有各种彩绘瓷”是作者的技术史判断，保留原表述；同段前半述青瓷、黑瓷烧制技术发展，未并入本条。",
  1675, 1675, "line", [1675], ["b0228"], "1. 瓷器时代的形成与陶瓷器的设计")

C("cand-03-67", "factual_claim",
  "夏燕靖认为，魏晋南北朝南北青瓷形成两个体系、各有千秋：南方瓷秀丽轻巧、含氧化铁较多、釉色青翠，北方瓷浑朴厚重、含氧化铝和氧化钛较多、青中泛黄。",
  "Xia Yanjing observes that Southern and Northern celadons formed two distinct systems, each with its own strengths: southern wares are delicate and light, richer in iron oxide, with verdant glazes, while northern wares are sturdy and heavy, richer in aluminium and titanium oxides, with glazes tending to yellow within the blue-green.",
  "high",
  ["04-knowledge/units/terms/qing-ci.md",
   "04-knowledge/units/terms/piao-ci.md",
   "04-knowledge/units/terms/black-porcelain.md",
   "04-knowledge/units/procedures/liuchao-qingci-zhuangshi-liufa.md"],
  "候选作 basic_fact，路由 factual；L1681 以“例如”列举胎质、釉色差异，结论句“两个体系，各有千秋”是本条断言核心；上一条 L1679 的越窑、瓯窑、婺窑、德清窑四系统未混入。",
  1681, 1681, "line", [1681], ["b0229"], "1）青瓷")

C("cand-03-78", "factual_claim",
  "夏燕靖指出，北魏时河北定州（今保定）、江南广陵（今扬州）、四川成都为高级丝织物的三大中心。",
  "Xia Yanjing identifies Dingzhou in Hebei (present-day Baoding), Guangling in the Jiangnan region (present-day Yangzhou), and Chengdu in Sichuan as the three major centres of high-grade silk textiles under the Northern Wei.",
  "high",
  ["04-knowledge/units/terms/zhijin.md",
   "04-knowledge/units/terms/jingjin.md",
   "04-knowledge/units/institutions/jinshu.md"],
  "候选跨度 L1737-L1759 覆盖整节纺织业叙述，实际断言在 L1745 末句，故取单行；同段所列平城官营作坊、孝文帝遣工匠教织与菱纹锦等纹样名，留在来源，不并入本条。",
  1745, 1745, "line", [1745], ["b0237"], "2. 织印染服装业的恢复和发展与其设计特色｜1）纺织印染业的恢复和发展")

C("cand-03-82", "interpretive_claim",
  "夏燕靖认为，受魏晋风度影响，士人以宽衣博带、风袂飘举的衣饰体现风度，一改汉代朴素端庄且封闭内敛的服饰特点，男子追求敞领宽衫，女子深衣也出现华带飞髻。",
  "Xia Yanjing argues that, under the influence of the Wei-Jin demeanour, scholars expressed their bearing through loose robes, broad sashes, and fluttering sleeves, breaking with the plain, dignified, closed style of the Han; men favoured open-collared, loose shirts, and women's deep robes acquired ornate sashes and flying coiffures.",
  "high",
  ["04-knowledge/units/terms/bao-yi-bo-dai.md",
   "04-knowledge/units/terms/zaju-chuishao-fu.md",
   "04-knowledge/units/works/zhulin-qixian-huaxiang-zhuan.md"],
  "候选作 interpretation；本条属知识链接“旷世奇服”框，作者以魏晋风度解释服饰转向，保留“受此风潮影响”的归因；陶渊明、阮籍的士风例证未写入断言。",
  1779, 1779, "line", [1779], ["b0240"], "知识链接：旷世奇服")

C("cand-03-83", "factual_claim",
  "夏燕靖据《三国志·夏侯尚传》指出，魏初文帝曹丕采纳吏部尚书陈群的建议制定九品官位制度，以紫、绯、绿三色为九品之别；又依战事提倡从俭，规定大将军以上服绫、锦、罗、纨、绮、素及金银饰镂之物，以下杂采之服通行于贱人。",
  "Citing the Sanguozhi biography of Xiahou Shang, Xia Yanjing notes that in the early Wei, Emperor Wen (Cao Pi) adopted the proposal of Minister of Personnel Chen Qun and instituted the nine-rank office system, using purple, crimson, and green to distinguish the nine grades; in keeping with wartime austerity he further ruled that those from general of the highest rank upward might wear silk twill, brocade, gauze, fine white silk, damask, and plain silk with gold and silver ornaments, while mixed-coloured garments below that rank were reserved for commoners.",
  "high",
  ["04-knowledge/units/terms/pinse-yi.md",
   "04-knowledge/units/terms/gongfu.md",
   "04-knowledge/units/terms/mianfu-zhidu.md"],
  "候选作 basic_fact，路由 factual；两条引文均出自《三国志·夏侯尚传》，断言以“据”保留文献中介，未写成曹丕本人自述；幅巾代冠、诸葛亮纶巾与西晋“套服”等邻接内容未并入。",
  1789, 1789, "line", [1789], ["b0242"], "2）服饰设计的艺术特色")

C("cand-03-90", "interpretive_claim",
  "夏燕靖认为，魏晋南北朝铜镜流行“袁氏”“尹氏”“黄龙元年陈世造”等铭文，反映了铜镜的私有商品性质；江南绍兴、扬州一带为铸镜基地。",
  "Xia Yanjing argues that inscriptions such as Yuan shi, Yin shi, and made by Chen Shi in the first year of Huanglong were common on Wei-Jin and Southern-Northern Dynasty bronze mirrors, reflecting the mirrors' character as privately owned commodities, and that Shaoxing and Yangzhou in Jiangnan were mirror-casting centres.",
  "medium",
  ["04-knowledge/units/terms/liuchao-tongjing.md",
   "04-knowledge/units/works/wu-zixu-huaxiang-jing.md",
   "04-knowledge/units/terms/tongjing.md"],
  "候选作 interpretation，默认路由 interpretive；来源将袁氏、尹氏与“黄龙元年陈世造”并列而统称纪年铭文，其中前两者为姓氏标识而非年号，断言按原文列举、不统称纪年，避免以偏概全；伍子胥画像镜的题材意义留作同框例证，未写入本条。",
  1829, 1829, "line", [1829], ["b0245"], "知识链接：铜镜")

C("cand-03-93", "interpretive_claim",
  "夏燕靖认为，魏晋南北朝佛教流行、广铸佛像耗铜极多，加之大量铸造钱币，造成铜矿供不应求与铜的缺乏；这一时期瓷器的发展又导致日用铜器生产衰落，铜镜成为较多见的铜器。",
  "Xia Yanjing argues that the popularity of Buddhism and the casting of large numbers of Buddha images, together with heavy coin production, strained copper supplies and produced a copper shortage; the growth of ceramics meanwhile caused daily-use bronze vessels to decline, leaving bronze mirrors as the more commonly seen bronze objects.",
  "medium",
  ["04-knowledge/units/terms/liuchao-tongjing.md",
   "04-knowledge/units/terms/tongjing.md",
   "04-knowledge/units/events/fojiao-chuanru-zhongguo.md",
   "04-knowledge/units/terms/qing-ci.md"],
  "候选作 interpretation；铜耗、铜缺与铜器衰落之间的因果链是作者的综合判断，保留“促使”“导致”的推论语气；《洛阳伽蓝记》佛像用铜十万斤与杜牧诗未逐句写入断言。",
  1839, 1839, "line", [1839], ["b0248"], "3. 金属工艺与纹饰设计｜1）冶铜业的发展")

C("cand-03-96", "factual_claim",
  "夏燕靖指出，魏晋南北朝时期钢铁兵器已普遍取代铜兵器；河南渑池县冶铁作坊遗址和北魏铁器窖藏发现铁器达4000余件，后赵石勒一次征调诸州造甲工匠50万人。",
  "Xia Yanjing notes that iron and steel weapons had generally replaced bronze weapons by the Wei-Jin and Southern-Northern Dynasties; the iron-smelting workshop site and Northern Wei iron hoard at Mianchi in Henan yielded more than 4,000 iron objects, and the Later Zhao ruler Shi Le once conscripted 500,000 armourers from the provinces in a single levy.",
  "high",
  ["04-knowledge/units/terms/tieqi-shidai.md",
   "04-knowledge/units/procedures/ye-tie-shu-qi-yuan.md",
   "04-knowledge/units/terms/tong-xiu-kai.md",
   "04-knowledge/units/terms/mingguang-kai.md"],
  "候选作 basic_fact，路由 factual；L1860 同段先述战争需求推动冶铁，后半列渑池遗址、石勒征匠与钢铁代铜三项，断言取此三项；L1862 兜鍪、筒袖铠、衲裆铠、明光铠的形制细节留在来源。",
  1860, 1860, "line", [1860], ["b0250"], "3）冶铁业与兵器的发展")

C("cand-03-102", "factual_claim",
  "夏燕靖据《晋书》指出，西晋皇帝大驾卤薄是目前所见皇帝卤薄最早的完整记录，皇帝出行所乘金银车驾六匹骏马，属车八十一乘，前后另有司南车、武刚车、金根车等众多车型。",
  "Citing the Jinshu, Xia Yanjing states that the Western Jin emperor's grand ceremonial procession is the earliest complete recorded imperial lubu: the gold-and-silver chariot was drawn by six horses, eighty-one accompanying carriages followed, and numerous types such as the south-pointing carriage, wugang carriage, and jingen carriage preceded and followed.",
  "high",
  ["04-knowledge/units/terms/lubu.md",
   "04-knowledge/units/terms/shuang-yuan-che.md"],
  "候选作 basic_fact，路由 factual；候选块 b0255 同时述东汉牛车、战车与蜀汉独轮车，断言只取《晋书》大驾卤薄一段；“司南车”是卤薄中的车型，与磁性指向器“司南”不是一物，故不链 terms/sinan.md。",
  1881, 1881, "line", [1881], ["b0255"], "4. 车船制造及木作业设计｜1）车船制造设计｜① 车")

C("cand-03-104", "factual_claim",
  "夏燕靖指出，北朝自北魏起官府造船业有很大发展，公元430年在冀、定、相三州即造船3000艘，大船载重达两万斛（合两千吨位），表明当时造船设计与生产技术都达到很高水平。",
  "Xia Yanjing notes that official shipbuilding expanded greatly in the Northern Dynasties from the Northern Wei onward: in 430 CE, 3,000 vessels were built in the Ji, Ding, and Xiang prefectures, with the largest carrying 20,000 hu (roughly 2,000 tons), indicating that ship design and production techniques had reached a high level.",
  "high",
  ["04-knowledge/units/terms/louchuan.md",
   "04-knowledge/units/terms/plank-boat.md",
   "04-knowledge/units/terms/sida-chuanxing.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L1891-L1896 含南朝飞龙、翔凤、金翅、青雀等船名与拍竿装置，断言取末段北朝造船数据；吨位换算是作者给出的折算，随文保留。",
  1895, 1895, "line", [1895], ["b0256"], "4. 车船制造及木作业设计｜1）车船制造设计｜② 船")

C("cand-03-105", "factual_claim",
  "夏燕靖指出，魏晋以来随着房屋增高扩大，家具相应加高加大，出现圆案、橱柜、扶手椅、束腰圆凳、方凳、长杌等高形家具，垂足而坐渐推广，家具结构更加简化并出现金属连接件。",
  "Xia Yanjing notes that as houses grew taller and larger from the Wei-Jin period onward, furniture was made higher and bulkier: high-form pieces such as round tables, cupboards, armchairs, waisted round stools, square stools, and long benches appeared, sitting with feet down spread, furniture construction simplified, and metal connectors came into use.",
  "high",
  ["04-knowledge/units/terms/gaoxing-jiaju.md",
   "04-knowledge/units/terms/huchuang.md",
   "04-knowledge/units/terms/han-dai-jia-ju.md"],
  "候选作 basic_fact，路由 factual；候选块 b0257 还含谢灵运木屐与图 5-23，断言取家具一段；圆案、橱柜、扶手椅等名目按来源照录，未据后世家具形制反向释读。",
  1899, 1899, "line", [1899], ["b0257"], "4. 车船制造及木作业设计｜2）木作业设计")

C("cand-04-02", "interpretive_claim",
  "夏燕靖认为，高型坐具的流行直接改变了坐礼、社交礼仪与房屋格局，如窗户提高、家具数量增加。",
  "Xia Yanjing argues that the spread of high seating directly transformed rules of sitting, social etiquette, and interior layout, raising windows and increasing the number of furniture pieces.",
  "medium",
  ["04-knowledge/units/terms/huchuang.md",
   "04-knowledge/units/terms/gaoxing-jiaju.md"],
  "候选作 interpretation；知识链接“胡床”框把胡床经唐代椅子到宋代流行连成一线，本条只取“坐礼—社交礼仪—房屋格局”的后果判断，不把唐宋演化并入魏晋断言；窗户提高与家具增多的因果为作者解释。",
  1913, 1913, "line", [1913], ["b0259"], "知识链接：胡床")

C("cand-04-04", "factual_claim",
  "夏燕靖指出，北魏佛教兴盛使寺院建筑大量涌现，寺院檐脊较多使用琉璃瓦；当时各州郡寺院三万余所，仅洛阳就有千余所。",
  "Xia Yanjing notes that the flourishing of Buddhism under the Northern Wei produced large numbers of monastery buildings, whose eaves and ridges often used glazed tiles; there were more than 30,000 monasteries across the prefectures, over 1,000 in Luoyang alone.",
  "high",
  ["04-knowledge/units/events/fojiao-chuanru-zhongguo.md",
   "04-knowledge/units/terms/liuli.md",
   "04-knowledge/units/procedures/liuli-shaozhao.md",
   "04-knowledge/units/terms/fota.md"],
  "候选作 basic_fact，路由 factual；L1925 同段还述江南用砖、青砖与窖水技术、嵩岳寺塔，断言取寺院数量与琉璃瓦两项；塔高 41 米、15 层密檐等数据留在来源。",
  1925, 1925, "line", [1925], ["b0261"], "5. 建筑与雕刻工艺设计｜1）砖石建筑")

C("cand-04-07", "interpretive_claim",
  "夏燕靖认为，石窟寺自印度传入中国后，中国石刻工匠很快创造出中国形式的造像艺术，未长期停留在犍陀罗模仿阶段。",
  "Xia Yanjing argues that after cave temples entered China from India, Chinese stone carvers quickly created a Chinese form of image-making and did not remain long in imitation of Gandhara models.",
  "medium",
  ["04-knowledge/units/events/liuchao-buddhist-caves.md",
   "04-knowledge/units/places/yungang-shiku.md",
   "04-knowledge/units/places/longmen-grottoes.md",
   "04-knowledge/units/places/xiangtangshan-shiku.md"],
  "候选作 interpretation，默认路由 interpretive；“很快创造”“未长期停留”是作者对风格转译速度的判断，保留判断语气；云冈、龙门、莫高窟开凿于北朝与南朝陵墓石雕的评价未并入本条。",
  1929, 1929, "line", [1929], ["b0262"], "5. 建筑与雕刻工艺设计｜2）石刻与纹饰设计")

C("cand-04-08", "interpretive_claim",
  "夏燕靖认为，“气韵生动”不仅是评论古代绘画的标准，也是古代设计思想的优秀传统精髓。",
  "Xia Yanjing argues that qiyun shengdong, the principle of spirited resonance, is not only a standard for judging ancient painting but also a vital part of the finest tradition of ancient design thought.",
  "medium",
  ["04-knowledge/units/persons/xie-he.md",
  "04-knowledge/units/terms/ba-ti-shuo.md",
  "04-knowledge/units/publications/wen-xin-diao-long.md",
  "04-knowledge/units/persons/gu-kai-zhi.md",
  "04-knowledge/units/terms/xuanxue.md"],
  "候选作 interpretation；本条与 cand-04-10 同处 b0263，L1940 论气韵生动向设计思想的迁移，L1942 论刘昼“施用有宜”，分建两条；器物装饰与绘画合流的中介论证保留在来源，未压缩为单一因果。",
  1940, 1940, "line", [1940], ["b0263"], "6. 设计思想的形成")

C("cand-04-10", "interpretive_claim",
  "夏燕靖指出，北朝刘昼认为美丑是相对的，衡量标准在于“施用有宜”，评价物品应看其是否适用，而不只看材质高贵、外表漂亮。",
  "Xia Yanjing notes that Liu Zhou of the Northern Dynasties held beauty and ugliness to be relative, judged by whether a thing is fit for its use (shiyong youyi); objects should be evaluated by their usefulness, not merely by costly materials or handsome appearance.",
  "medium",
  ["04-knowledge/units/persons/liu-zhou.md",
   "04-knowledge/units/publications/liuzi.md"],
  "候选作 interpretation，默认路由 interpretive；来源引《刘子》“物有美恶，施用用宜”与“施用有宜”并存，断言取正文评述所用“施用有宜”；“这也是中国古代审美应用学理论重视实用的传统的发扬”是作者的评价，未写成刘昼原意。",
  1942, 1942, "line", [1942], ["b0263"], "6. 设计思想的形成")


def main():
    assert len(ROWS) == 17, len(ROWS)
    types = {"factual_claim", "interpretive_claim", "synthetic_claim",
             "evaluative_claim", "contested_claim", "historiographic_claim"}
    seen = set()
    for i, row in enumerate(ROWS):
        row["claim_id"] = "claim-%04d" % (115 + i)
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
        assert 1662 <= sp["line_start"] <= sp["line_end"] <= 1966, sp
        assert sp["key_lines"] and all(sp["line_start"] <= x <= sp["line_end"] for x in sp["key_lines"]), sp
        assert sp["block_ids"], sp
        assert sp["span_kind"] in {"line", "contiguous", "bounded"}
        if sp["span_kind"] == "line":
            assert sp["line_start"] == sp["line_end"]
        for p in row["supported_by"]:
            assert p.startswith("04-knowledge/units/"), p
            assert (ROOT / p).exists(), p
    assert len({r["source"]["candidate_id"] for r in ROWS}) == 17
    (ROOT / "_zn_claim_xyj09d_rows.json").write_text(
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
