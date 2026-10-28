# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz9a (late Republican decline, liberated areas, early PRC, 14 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "近代工艺衰落、解放区与新中国工艺（国民党统治末至新中国）"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
W = "04-knowledge/units/works/"
PR = "04-knowledge/units/procedures/"
E = "04-knowledge/units/events/"
I = "04-knowledge/units/institutions/"

MAP = ROOT / "03-processing/2010-tianzibing-zhongguo-gongyi-meishushi/source-map.jsonl"
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
    "claim-1026", "cand-13-62", "interpretive_claim",
    "在国民党几十年统治下，旧中国工艺美术出现严重衰落：鸦片战争后洋布、洋瓷等外国日用品大量倾销，传统工艺受摧残、新兴现代工艺也受影响；一战期间因列强忙于混战、暂时放松侵略而一度微弱发展，抗战开始后国统区遭搜刮、沦陷区遭破坏，抗战胜利后美货倾销、工厂倒闭，工艺美术生产被摧残殆尽。",
    "Under decades of Nationalist rule, craft in old China declined severely: after the Opium War the dumping of foreign cloth, porcelain and daily goods damaged traditional crafts and affected modern craft; a brief weak recovery during the First World War, when the powers relaxed their aggression, ended with the War of Resistance, when the Nationalist areas were squeezed and occupied areas devastated, and after 1945 American dumping and factory closures reduced craft production to ruin.",
    [E + "opium-war.md", T + "xiandai-gongyi.md", T + "gongyi-meishu.md"],
    "断言语义取 L4963-L4965。原文以“国民党几十年统治”与“鸦片战争以后”两个起点并述，claim 保留双层时间结构，不把衰落全部归因于国民党统治。",
    4963, 4965, [4963, 4965], "第十二章 第三节 国民党统治下工艺美术的衰落"))

rows.append(C(
    "claim-1027", "cand-13-63", "historiographic_claim",
    "大生产运动取得巨大成绩并发展了新的工艺美术，使解放区军民渡过严重困难，也为抗日战争最后胜利奠定物质基础；运动开展后染织、陶瓷、玻璃、木工、编织、装潢等工艺应运而生，开创了工艺美术史上的新篇章。",
    "The Great Production Campaign achieved major results and developed a new arts and crafts, carrying the military and people of the liberated areas through severe hardship and laying a material basis for final victory in the War of Resistance; textile, ceramic, glass, wood, basketry and decorative crafts arose with the campaign, opening a new chapter in craft history.",
    [E + "da-shengchan-yundong.md", T + "gongyi-meishu.md", I + "yanan-bolichang.md"],
    "断言语义取 L5007-L5009。原文将大生产运动定在1941-1942年困难时期，claim 不重复具体年份；玻璃工艺以延安玻璃厂为实例，故链接该机构条目。",
    5007, 5009, [5007, 5009], "第十二章 第四节 解放区的工艺美术"))

rows.append(C(
    "claim-1028", "cand-13-64", "evaluative_claim",
    "解放区工艺美术是新中国工艺美术的雏形、无产阶级工艺美术的前驱、我国工艺美术的光辉榜样，在工艺美术史上写下了灿烂的一页。",
    "The arts and crafts of the liberated areas were the prototype of New China's craft, the forerunner of proletarian craft and a shining model for Chinese craft, writing a brilliant page in its history.",
    [I + "jiefangqu-diyige-taoci-yanjiusuo.md", E + "da-shengchan-yundong.md", T + "gongyi-meishu.md"],
    "断言语义取 L5039。“雏形”“前驱”“榜样”三重评价带强烈政治话语色彩，claim 保留原文评价层级，不转写为中性史实。",
    5039, 5039, [5039], "第十二章 第四节 解放区的工艺美术"))

rows.append(C(
    "claim-1029", "cand-13-65", "evaluative_claim",
    "工艺美术的迅速繁荣发展充分显示了社会主义制度的优越性，也是党的经济政策和文化政策正确指引的结果；虽在十年动乱中受极左思潮影响，但十一届三中全会以来经过拨乱反正又迅速恢复和发展。",
    "The rapid flourishing of arts and crafts fully demonstrated the superiority of the socialist system and resulted from the correct guidance of Party economic and cultural policy; although the decade of turmoil and ultra-left thinking affected it, recovery and development resumed quickly after the Third Plenary Session of the Eleventh Central Committee.",
    [T + "gongyi-meishu.md", E + "craft-recovery-transformation-1950s.md", E + "party-third-plenum.md"],
    "断言语义取 L5049。“十年动乱”“极左”为原文特定历史表述，claim 保留；繁荣与制度、政策的因果关系属作者判断，不改为统计结论。",
    5049, 5049, [5049], "第十三章 第一节 概说"))

rows.append(C(
    "claim-1030", "cand-13-66", "interpretive_claim",
    "科学技术应用已根本改变解放前陶瓷生产成型靠手工、练泥靠体力、干燥靠太阳、烧窑靠松柴的“四靠”落后面貌；手工操作逐步为机械代替，成型、施釉、装饰大部分实现机械化，印花薄膜、电子喷花与自动流水线逐步建立，柴窑普遍改为煤窑或隧道窑。",
    "Scientific and technological application has fundamentally changed the backward pre-1949 porcelain production summed up as four reliances: shaping on handwork, clay preparation on muscle, drying on the sun and firing on pine firewood; hand operations are increasingly replaced by machinery, shaping, glazing and decoration are largely mechanized, film printing, electronic spraying and automatic lines are being introduced, and wood-fired kilns are generally converted to coal or tunnel kilns.",
    [T + "gongyi-meishu.md", P + "jingdezhen-kiln.md", I + "jingdezhen-ciye-gongsi.md"],
    "断言语义取 L5059。“四靠”为原文对旧陶瓷生产方式的概括，claim 逐项引出四项，避免把“四靠”当作既有术语而不作解释。",
    5059, 5059, [5059], "第十三章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-1031", "cand-13-67", "factual_claim",
    "景德镇过去漫长岁月只能烧制30多种色釉，新中国仅一个建国瓷厂就能生产100多种彩色缤纷的釉彩，其中鲜红、桃红、翠绿等高温釉与金星绿、苹果绿等低温釉都已超过历史水平。",
    "For long ages Jingdezhen could fire only some thirty glaze colours; in New China a single Jianguo Porcelain Factory produced more than a hundred, among them high-temperature reds, peach red and emerald green and low-temperature gold-star green and apple green, all surpassing historical levels.",
    [P + "jingdezhen-kiln.md", I + "jingdezhen-ciye-gongsi.md", T + "gongyi-meishu.md"],
    "断言语义取 L5065。“30多种”“100多种”未注统计口径、比较年份与瓷厂范围，claim 保留原文数量表述，不推算增长率。",
    5065, 5065, [5065], "第十三章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-1032", "cand-13-68", "synthetic_claim",
    "磁州窑装饰以黑白对比为主要特点，有画花和刻花两种：画花以斑化石作绘料在白地或黑地上形成黑花、褐彩，称为铁锈花；刻花剔刻地色形成白色与瓷胎或黑色与瓷胎的对比；题材多用花鸟、鱼虫、婴戏、历史故事，笔力豪放粗犷、刻划生动流畅，富于浓厚民间艺术特色。",
    "Cizhou ware decoration is chiefly characterized by black-and-white contrast, in two modes: painted decoration uses banhuashi ore as pigment to produce black flowers on white or brown on black, called iron-rust flower; carved decoration cuts back the ground to contrast white or black with the body. Motifs are popular flower-and-bird, fish-and-insect, child-play and historical-story themes, bold and free in brushwork and lively in carving, with a strongly popular artistic character.",
    [P + "cizhou-kiln.md", T + "gongyi-meishu.md"],
    "断言语义取 L5073。“斑化石”原文括注为含氧化铁的贫铁矿石，claim 保留原名而不代以矿物学定名；“铁锈花”为俗称，未注别称来源。",
    5073, 5073, [5073], "第十三章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-1033", "cand-13-69", "historiographic_claim",
    "云锦的艺术特点仍大体保持明代风格，花朵较大、色彩明快、富于装饰性；云锦在明清时期生产极盛，而云锦一词至近代才采用，多用作蒙藏少数民族的衣帽服饰。",
    "Yunjin still broadly retains Ming stylistic traits, with large flowers, bright colour and strong ornament; its production peaked in the Ming-Qing period, while the name yunjin was adopted only in modern times, and it served mainly for the dress and hats of Mongol and Tibetan minorities.",
    [T + "nanjing-yunjin.md", I + "nanjing-yunjin-yanjiusuo.md"],
    "断言语义取 L5103。“云锦一词至近代才采用”与 tz8a `claim-0999` 的得名考辨互补：一述名称启用时代，一述得名依据，未合并。",
    5103, 5103, [5103], "第十三章 第三节 染织工艺"))

rows.append(C(
    "claim-1034", "cand-13-70", "factual_claim",
    "蜀锦保持唐代以前经锦的传统特点，是现今唯一用多色经丝与纬线交织起花的一种织锦；其图案组织分为方方、雨丝、条花、散花等类，形成几何组织与纹饰结合的独特风格。",
    "Shu brocade preserves the pre-Tang warp-faced tradition and is now the only brocade that patterns by interweaving multi-coloured warp threads with weft; its pattern structures include square, rain-thread, striped-flower and scattered-flower types, forming a distinctive style that combines geometric organization with ornament.",
    [T + "shu-brocade.md", T + "gongyi-meishu.md"],
    "断言语义取 L5105。“现今唯一”为作者判断，未注调查范围与比较样本；claim 保留这一限定语，不改为绝对事实。",
    5105, 5105, [5105], "第十三章 第三节 染织工艺"))

rows.append(C(
    "claim-1035", "cand-13-71", "evaluative_claim",
    "“选花会”是社会主义制度的产物，体现党和政府对人民生活的关怀；其建立旨在了解人民对花布的需要和喜爱、广泛听取群众对花布图案的意见。",
    "The pattern-selection fair was a product of the socialist system and expressed Party and government concern for people's livelihood; it was established to learn people's needs and preferences in printed cloth and to solicit public opinion on pattern design.",
    [T + "gongyi-meishu.md", T + "tu-an.md"],
    "断言语义取 L5126。原文“选花会”加引号，claim 保留制度名称；“社会主义制度的产物”为作者评价，与后句目的陈述并列而不混为事实。",
    5126, 5126, [5126], "第十三章 第三节 染织工艺"))

rows.append(C(
    "claim-1036", "cand-13-72", "historiographic_claim",
    "在长期封建社会里，刺绣一方面是民间自绣自用，一方面是封建统治者设置绣坊、为剥削阶级所有；随着地区与技艺演变，形成苏绣、湘绣、广绣、蜀绣以及少数民族刺绣等系统。",
    "In the long feudal period embroidery was on the one hand a folk craft for household use and on the other a workshop production owned by the ruling class; with regional and technical differentiation it formed the Su, Xiang, Guang, Shu and minority embroidery systems.",
    [T + "suxiu.md", T + "xiangxiu.md", T + "shuxiu.md", T + "yuexiu.md", T + "kesi.md", T + "gongyi-meishu.md"],
    "断言语义取 L5138。原文作“广绣”，与 tz8a `claim-1001` 的“粤绣”为同一绣种的不同称法，本 claim 保留原文“广绣”，并在支持链接中指向粤绣条目，名称统一留待 reconcile。",
    5138, 5138, [5138], "第十三章 第三节 染织工艺"))

rows.append(C(
    "claim-1037", "cand-13-73", "evaluative_claim",
    "北京雕漆从明代果园厂发展而来，明代永乐、清代乾隆生产兴盛；清代后期官营作坊消失，私营继古斋继续生产；1914年巴拿马博览会获一等奖后在民国初年一度畸形发展，但艺术上多为仿清作品、无多大特色。",
    "Beijing carved lacquer descended from the Ming Guoyuanchang workshop and flourished under Yongle and Qianlong; in the late Qing official workshops disappeared and the private Jiguzhai firm continued production; after winning first prize at the 1914 Panama Exposition it grew abnormally in the early Republic, yet artistically most pieces imitated Qing work and showed little distinction.",
    [T + "diao-qi.md", I + "guoyuanchang.md", I + "neiwufu-zaobanchu.md"],
    "断言语义取 L5194-L5196。“畸形发展”为作者评价；1914年获奖与“民国初年”时间衔接未注博览会正式名称与奖项类别。",
    5194, 5196, [5194, 5196], "第十三章 第五节 漆器工艺"))

rows.append(C(
    "claim-1038", "cand-13-74", "interpretive_claim",
    "玉雕的高度技巧在于套裁与巧色：套裁充分利用刻制器物的余料再刻成器体部件，如从瓶腹内挖出玉材制成与器体相连的连环链条；巧色根据玉石里外不同色泽表现不同形象、去瑕显瑜、因材施艺；整个制作过程也就是设计过程。",
    "The great skill of jade carving lies in interlocking cutting and colour adaptation: interlocking cutting uses leftover material to carve parts of the vessel, as when jade removed from a vase's belly becomes a linked chain joined to the body; colour adaptation uses the stone's inner and outer colouring for different images, hiding flaws and revealing beauty. The whole making process is also the design process.",
    [PR + "yudiao-taocai-qiaose.md", W + "hongqi-chashang-zhumulangmafeng.md", T + "gongyi-meishu.md"],
    "断言语义取 L5288。套裁、巧色为工艺术语，原文未注英文与工序细节；claim 以原文瓶腹取料制链为例，不扩及具体工具。",
    5288, 5288, [5288], "第十三章 第七节 雕塑工艺"))

rows.append(C(
    "claim-1039", "cand-13-75", "historiographic_claim",
    "编织工艺历史悠久，其起源可能更早于陶器；战国竹器、汉代彩箧制作已相当精美，唐代草席产地普遍，闽广藤器、沧州柳箱、蒲州麦秆扇等已成著名产品。",
    "Basketry and plaiting have a long history and may predate pottery; Warring States bamboo wares and Han painted cases were already finely made, Tang grass mats were widely produced, and Fujian-Guangdong rattan, Cangzhou willow boxes and Puzhou wheat-straw fans were already famous products.",
    [PR + "bianzhi.md", T + "shougong-bianzhi.md", PR + "zhubian-yishu-jiagong.md", T + "gongyi-meishu.md"],
    "断言语义取 L5222。“可能更早于陶器”为推测，claim 保留“可能”；战国竹器、汉代彩箧为出土实物，唐代草席与地方名产为文献记载，两类证据未分级。",
    5222, 5222, [5222], "第十三章 第六节 编织工艺"))

out = ROOT / "_tz_tz9a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print("rows", len(rows))
from collections import Counter
print(Counter(r["claim_type"] for r in rows))
links = [p for r in rows for p in r["supported_by"]]
print("links", len(links), "distinct", len(set(links)))
print("span kinds", Counter(r["source"]["source_span"]["span_kind"] for r in rows))
