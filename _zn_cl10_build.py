# -*- coding: utf-8 -*-
"""Build CL7a claim rows (14 new) and 7 cross-edition corroboration patches.

Chapter: 明清时期的设计渐变 (L4111-L4712), 21 claim candidates.
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


CH = "明清时期的设计渐变"
rows = []

rows.append(C(
    "claim-0346", "factual_claim",
    "夏燕靖指出，明清时期桑、麻、棉的栽植面积得到进一步扩大；明代江南区域和珠江三角洲逐渐成为主要养蚕区。",
    "Xia Yanjing notes that in the Ming and Qing the acreage devoted to mulberry, hemp and cotton expanded further, and that in the Ming Jiangnan and the Pearl River Delta gradually became major sericulture regions.",
    "medium",
    ["04-knowledge/units/terms/mingdai-sizhi-sida-changu.md",
     "04-knowledge/units/publications/cansang-cuibian.md"],
    "断言取 L4133 前两句。同段山东柞蚕法与柞丝绸、明末清初柞蚕放养扩展至河南、陕西、云南，以及 L4144 接续的贵州、辽东植棉留在来源；未给栽植面积、产量或区域比例数据。四大产区另见 terms/mingdai-sizhi-sida-changu，清代蚕桑文献见 publications/cansang-cuibian。",
    4131, 4133, "line", [4133], ["b0512"],
    "1. 纺织印染业的高度繁荣与染织品种设计"))

rows.append(C(
    "claim-0347", "evaluative_claim",
    "夏燕靖认为，以挖花回纬为主要显花手段的重纬织物妆花缎，代表了我国古代织锦技术的最高水平。",
    "Xia Yanjing holds that zhuanghua satin, a heavy-weft fabric figuring mainly by supplementary-warp patterning, represents the highest level of ancient Chinese brocade technique.",
    "medium",
    ["04-knowledge/units/terms/zhuanghua.md",
     "04-knowledge/units/terms/nanjing-yunjin.md"],
    "断言取 L4179 的末句评价。南京云锦大花楼木质提花机、挑花结本、花本重量与长度留在 L4175 知识链接；妆花缎 17 个品种、彩纬 6 至 9 色、“巧变日出，花色日新”与江宁织造局留在同段。来源未给与其他织锦的量化比较，“最高水平”为作者评价。纹样组织见 terms/zhuanghua，云锦品种见 terms/nanjing-yunjin。",
    4173, 4188, "line", [4179], ["b0518"],
    "1. 纺织印染业的高度繁荣与染织品种设计 / 1）丝织工艺的产区与品种特色 / 知识链接：南京云锦"))

rows.append(C(
    "claim-0348", "factual_claim",
    "夏燕靖据统计指出，至鸦片战争爆发前夕，全国农户近半数（六七千万户）织布，棉布半数进入市场，年产约3.1亿匹，仅次于粮食，是手工业中产值最大的部门。",
    "Xia Yanjing cites statistics that on the eve of the Opium War nearly half of all rural households (60-70 million) wove cloth, half of the cotton cloth entered the market, annual output reached about 310 million bolts, and the sector ranked second only to grain as the largest handicraft industry by output value.",
    "medium",
    ["04-knowledge/units/places/songjiang-fu.md"],
    "断言取 L4193 首句。全国最大棉布产区苏松地区、苏州年产约 4500 万匹与 L4217 的“南京土布”外销留在来源；本条只取全国总量与织布户数。3.1 亿匹与六七千万户为教材引用的统计值，未给出处与核算口径。松江府棉织中心另见 places/songjiang-fu。",
    4189, 4194, "line", [4193], ["b0519"],
    "1. 纺织印染业的高度繁荣与染织品种设计 / 2）棉织工艺与品种"))

rows.append(C(
    "claim-0349", "interpretive_claim",
    "夏燕靖认为，清廷接纳了明遗臣金之俊“十从十不从”建议中的“倡从而优伶不从”，优伶演戏时可以穿明代衣着，戏曲因此在清朝统治下仍保留着前朝的服饰。",
    "Xia Yanjing argues that the Qing court accepted the clause “advocates follow, actors do not” in Jin Zhijun's “ten follow, ten do not follow” advice, so actors could wear Ming dress on stage and opera thus retained the previous dynasty's costume under Qing rule.",
    "medium",
    ["04-knowledge/units/persons/jin-zhijun.md",
     "04-knowledge/units/events/queue-and-dress-edicts.md"],
    "断言取 L4215 的因果链。同段另列吴三桂臂助、南方反清形势、《研堂见闻杂录》所记入关初衣冠承汉制、顺治三年剃发易服令与“十从十不从”全文；本条只取“倡从而优伶不从”与戏曲服饰保留明制的制度解释。未给剧种、剧目或戏衣实物统计。金之俊见 persons/jin-zhijun，剃发易服见 events/queue-and-dress-edicts；与 claim-0352 同源而断言不同。",
    4213, 4218, "line", [4215], ["b0524"],
    "1. 纺织印染业的高度繁荣与染织品种设计 / 知识链接：戏曲服饰"))

rows.append(C(
    "claim-0350", "evaluative_claim",
    "夏燕靖认为，明清印染工艺发展的标志是染料转以植物染料为主，靛蓝等染料广泛应用并远销国外。",
    "Xia Yanjing holds that the hallmark of Ming-Qing dyeing was the shift to plant dyes, with indigo and other dyes widely used and exported abroad.",
    "medium",
    ["04-knowledge/units/terms/lanran-gongyi.md"],
    "断言取 L4221 首句。明代精练丝绸两步法、芜湖与京口印染中心、清代苏州踹染、康熙三十四年采办青蓝布 30 万匹、药斑布与“苏印”工艺留在同段；本条只取植物染料为主的总判断。未给染料产量、贸易额或产地分布数据。蓝染工艺另见 terms/lanran-gongyi。",
    4219, 4222, "line", [4221], ["b0525"],
    "1. 纺织印染业的高度繁荣与染织品种设计 / 3）印染工艺与品种"))

rows.append(C(
    "claim-0351", "factual_claim",
    "夏燕靖据《明史·舆服志》指出，古代官服制度中真正代表官位的补服定型于明代；洪武二十四年（1391）规定官吏常服为盘领大袍，胸前、背后各缀一块方形补子，文官绣禽，武官绣兽。",
    "Citing the Ming History's treatise on carriages and dress, Xia Yanjing states that the rank badge proper took fixed form in the Ming; in 1391 official everyday dress was stipulated as a round-collar robe with a square badge on front and back, birds for civil and beasts for military officials.",
    "medium",
    ["04-knowledge/units/terms/buzi.md"],
    "断言取 L4248 的前两句。同段“衣冠禽兽”成语的由来与贬义化留在来源；L4233、L4256 的明代文武九品补子序列与儒士服细节另属官服形制段，未并入。来源未给补子实物、图像或出土统计。补子形制见 terms/buzi。",
    4246, 4263, "line", [4248], ["b0529"],
    "2. 服装工艺与服装设计 / 知识链接：“衣冠禽兽”成语典故"))

rows.append(C(
    "claim-0352", "interpretive_claim",
    "夏燕靖认为，清康熙时期为缓解日益尖锐的民族矛盾，清廷采纳明遗臣金之俊“十从十不从”的建议，在服饰方面尽可能保持明代汉制服饰面貌，大大缓解了因强行剃发易服而引起的民怨。",
    "Xia Yanjing argues that in the Kangxi reign, to ease sharpening ethnic conflict, the Qing court adopted Jin Zhijun's “ten follow, ten do not follow” advice, preserving Ming Han dress as far as possible and greatly relieving the resentment caused by the forced queue and dress edicts.",
    "medium",
    ["04-knowledge/units/persons/jin-zhijun.md",
     "04-knowledge/units/events/queue-and-dress-edicts.md"],
    "断言取 L4266 的后半句。“留头不留发，留发不留头”的极端措施、汉人抵制与“十从十不从”全文留在同段；本条只取康熙朝采纳建议、保持明制与缓解民怨的因果解释。未给民怨强度、政策覆盖面或效果的量化证据。与 claim-0349 同引“十从十不从”，但一为戏曲服饰、一为易服政策，故分列。",
    4264, 4269, "line", [4266], ["b0530"],
    "2. 服装工艺与服装设计 / 2）清代服饰"))

rows.append(C(
    "claim-0353", "evaluative_claim",
    "夏燕靖认为，康、雍、乾时期都重视制瓷业，雍正重奖制瓷工匠，乾隆酷爱瓷器精品，促使制瓷业工艺水平和产量都达到历史上的高峰，堪称我国制瓷史上的黄金时代。",
    "Xia Yanjing holds that Kangxi, Yongzheng and Qianlong all valued porcelain; Yongzheng rewarded craftsmen and Qianlong prized fine wares, bringing technique and output to a historical peak, a golden age of Chinese porcelain.",
    "medium",
    ["04-knowledge/units/places/jingdezhen-kiln.md",
     "04-knowledge/units/terms/fencai.md",
     "04-knowledge/units/terms/falangcai.md"],
    "断言取 L4345 的末句。明代景德镇官窑 58 座、成化斗彩、康熙十九年后官窑复兴、单色釉、珐琅彩与粉彩奠基留在同段；本条只取康雍乾“黄金时代”的总体评价。未给官窑产量、窑座数或外销数据。官窑与瓷都见 places/jingdezhen-kiln，粉彩与珐琅彩见 terms/fencai、terms/falangcai。",
    4341, 4367, "line", [4345], ["b0539"],
    "3. 陶瓷业的繁荣与品种发展 / 1）瓷器工艺的改进与特色形成"))

rows.append(C(
    "claim-0354", "factual_claim",
    "夏燕靖指出，明清两代的青花瓷大量外销；仅荷兰东印度公司在1602-1682年的80年中，便贩运中国青花瓷1600万件以上。",
    "Xia Yanjing notes that Ming-Qing blue-and-white porcelain was exported in great quantities; the Dutch East India Company alone carried away more than 16 million pieces of Chinese blue-and-white in the eighty years from 1602 to 1682.",
    "medium",
    ["04-knowledge/units/terms/maoyi-ci.md",
     "04-knowledge/units/works/fanchuan-tujing-cipan.md"],
    "断言取 L4353 的荷兰东印度公司数据。同段苏麻离青、回青、葫芦瓶造型、青花烧成的釉料与还原焰要求留在来源；本条只取外销数量。1600 万件为教材引用值，未给出处、统计口径与件类构成。贸易瓷见 terms/maoyi-ci，东印度公司帆船纹盘见 works/fanchuan-tujing-cipan。",
    4341, 4367, "line", [4353], ["b0539"],
    "3. 陶瓷业的繁荣与品种发展 / 1）瓷器工艺的改进与特色形成"))

rows.append(C(
    "claim-0355", "synthetic_claim",
    "夏燕靖认为，在明清两朝长达数百年的贸易瓷交易过程中，曾出现过两次高峰。",
    "Xia Yanjing argues that the several-hundred-year trade-porcelain exchange of the Ming and Qing had two peaks.",
    "medium",
    ["04-knowledge/units/terms/maoyi-ci.md",
     "04-knowledge/units/events/zhenghe-voyages.md"],
    "断言取 L4407 的分期判断。第一次高峰在明永乐三年（1405）前后随郑和下西洋出现、亚非诸国宫殿与博物馆收藏中国青花瓷见 L4409；第二次高峰在 17-19 世纪欧洲各国、荷兰东印度公司每年至少贩运 300 万件见 L4417；两次高峰的展开留在来源，本条只作综括。贸易瓷见 terms/maoyi-ci，郑和下西洋见 events/zhenghe-voyages。",
    4403, 4422, "line", [4407], ["b0543"],
    "4. 明清贸易瓷的历史演变与特色"))

rows.append(C(
    "claim-0356", "evaluative_claim",
    "夏燕靖认为，明清贸易瓷具有深刻的文化内涵和很高的学术价值，曾在世界上产生巨大影响，但至今没有引起国内学界的足够重视；国外博物馆收藏丰富，重视程度与研究总体水平高于国内。",
    "Xia Yanjing holds that Ming-Qing trade porcelain has deep cultural content and high scholarly value and exerted great worldwide influence, yet has not received sufficient attention from Chinese scholars; foreign museums hold rich collections and foreign research generally outpaces domestic work.",
    "medium",
    ["04-knowledge/units/terms/maoyi-ci.md",
     "04-knowledge/units/works/yongzheng-fencai-sangnv-pan.md",
     "04-knowledge/units/works/fanchuan-tujing-cipan.md"],
    "断言取 L4443 的对比评价。欧洲加彩、描金等二次装饰、广州口岸在“西学东渐”与“东风西渐”中的先锋角色留在同段；本条只取国内外研究水平的比较。未给论文、展览、收藏或研究项目的量化比较。贸易瓷见 terms/maoyi-ci，展览实例见 works/yongzheng-fencai-sangnv-pan、works/fanchuan-tujing-cipan。",
    4427, 4452, "line", [4443], ["b0545"],
    "4. 明清贸易瓷的历史演变与特色 / 知识链接：贸易瓷的变化"))

rows.append(C(
    "claim-0357", "interpretive_claim",
    "夏燕靖认为，北京紫禁城经历明清两代的不断营造，已是我国现存最大的古代宫殿建筑群，也是我国古代建筑的杰作；其规模宏伟、布局严整、主次分明，体现着皇权至高无上的设计思想。",
    "Xia Yanjing argues that the Forbidden City, built up through the Ming and Qing, is China's largest surviving ancient palace complex and a masterpiece of ancient Chinese architecture, its grand scale, strict layout and clear hierarchy embodying the supreme authority of imperial power.",
    "medium",
    ["04-knowledge/units/works/beijing-zijincheng.md",
     "04-knowledge/units/places/beijing.md"],
    "断言取 L4477 的评价句。明南京、北京宫城营造的《明史·舆服志》引文、洪武至永乐间的宫殿沿革、大报恩寺琉璃塔、布达拉宫、扎什伦布寺与承德外八庙留在同节；本条只取紫禁城的现存地位与皇权设计思想。未给建筑实测、遗产比较或规划复原数据。紫禁城见 works/beijing-zijincheng，北京城见 places/beijing。",
    4465, 4480, "line", [4477], ["b0549"],
    "5. 建筑设计与建筑彩画艺术 / 1）建筑设计"))

rows.append(C(
    "claim-0358", "evaluative_claim",
    "夏燕靖认为，明式家具的特色是简洁内敛、极少张扬；家具造型以线为主、素逸剔透，给人以恬静、文气、阴柔之感。",
    "Xia Yanjing holds that Ming-style furniture is restrained and understated, its forms dominated by line, plain and translucent, conveying a quiet, literati, feminine sensibility.",
    "medium",
    ["04-knowledge/units/terms/ming-style-furniture.md",
     "04-knowledge/units/publications/mingshi-jiaju-yanjiu.md",
     "04-knowledge/units/terms/gaoxing-jiaju.md"],
    "断言取 L4555 的风格判断。明代家具用材、六大类型、官帽椅、灯挂椅、圈椅等品种与文人生活关系留在同段；本条只取“简洁内敛、以线为主”的审美概括。未给比例、尺寸或装饰元素的量化分析。明式家具见 terms/ming-style-furniture，王世襄研究见 publications/mingshi-jiaju-yanjiu，高型家具见 terms/gaoxing-jiaju。",
    4545, 4558, "line", [4555], ["b0559"],
    "6. 家具种类与工艺设计 / 1）明代家具的设计特色与品种"))

rows.append(C(
    "claim-0359", "synthetic_claim",
    "夏燕靖认为，明清两代为满足漕运和远洋贸易的需要，造船设计业达到了顶峰；郑和宝船长约150米、舵杆长11米、张12帆，规模之大为当时世界航海业所仅有。",
    "Xia Yanjing argues that Ming-Qing shipbuilding reached its peak to meet grain-transport and overseas trade needs; Zheng He's treasure ship, about 150 m long with an 11 m rudder stock and twelve sails, was unmatched in the world's maritime industry at the time.",
    "medium",
    ["04-knowledge/units/works/zhenghe-baochuan.md",
     "04-knowledge/units/terms/sida-chuanxing.md",
     "04-knowledge/units/institutions/longjiang-chuanchang.md"],
    "断言取 L4605 的前两句。郑和船队舰船一两百艘、宝船 60 多艘、载 2.7 万多人、沙船鸟船福船广船四大类、船型千种与海洋渔船三四百种留在同段；L4607 的龙江船厂舵杆长 11.07 米与年造 3000 余只另属同节。本条只取“造船顶峰”与宝船尺度的综合判断。宝船尺度为文献记载与复制模型推算，未给考古实测。宝船见 works/zhenghe-baochuan，四大船型见 terms/sida-chuanxing，龙江船厂见 institutions/longjiang-chuanchang。",
    4596, 4618, "line", [4605], ["b0565"],
    "7. 车船种类与造船业"))

patches = [
    P("claim-0220", "cand-07-72", 4111, 4130, "line", [4117], ["b0511"],
      "知识链接：明中晚的经济状况"),
    P("claim-0227", "cand-08-97", 4274, 4301, "line", [4288], ["b0532"],
      "2. 服装工艺与服装设计 / 知识链接：公服“补子”"),
    P("claim-0231", "cand-08-101", 4341, 4367, "line", [4353], ["b0539"],
      "3. 陶瓷业的繁荣与品种发展 / 1）瓷器工艺的改进与特色形成"),
    P("claim-0229", "cand-08-99", 4341, 4367, "line", [4343], ["b0539"],
      "3. 陶瓷业的繁荣与品种发展 / 1）瓷器工艺的改进与特色形成"),
    P("claim-0234", "cand-08-106", 4483, 4496, "line", [4487], ["b0551"],
      "5. 建筑设计与建筑彩画艺术 / 1）建筑设计"),
    P("claim-0235", "cand-08-107", 4527, 4540, "line", [4539], ["b0557"],
      "5. 建筑设计与建筑彩画艺术 / 3）园林设计"),
    P("claim-0236", "cand-08-98", 4559, 4572, "line", [4571], ["b0560"],
      "6. 家具种类与工艺设计 / 2）清代家具的设计特色"),
]

MAP = {
    "claim-0346": "cand-07-101",
    "claim-0347": "cand-07-74",
    "claim-0348": "cand-07-75",
    "claim-0349": "cand-07-76",
    "claim-0350": "cand-07-93",
    "claim-0351": "cand-08-95",
    "claim-0352": "cand-08-96",
    "claim-0353": "cand-08-100",
    "claim-0354": "cand-08-102",
    "claim-0355": "cand-08-103",
    "claim-0356": "cand-08-104",
    "claim-0357": "cand-08-105",
    "claim-0358": "cand-08-108",
    "claim-0359": "cand-08-109",
}
for r in rows:
    r["source"]["candidate_id"] = DOC + ":" + MAP[r["claim_id"]]

(ROOT / "_zn_cl10_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_cl10_patch.json").write_text(
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
