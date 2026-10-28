# -*- coding: utf-8 -*-
"""Build 赵农 2009 第三章 claim rows (30 new claims, no merges)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "第三章 霸业的冲撞——春秋战国时期的设计"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(claim_id, cand, ctype, zh, en, supported, note, start, end, key_lines, block_ids, section):
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
                "block_ids": block_ids,
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
    "claim-0471", "cand-03-66", "historiographic_claim",
    "赵农把春秋战国视为中国历史上的巨大转型时期，认为其始于公元前770年周平王东迁洛阳、止于公元前221年秦朝建立，共549年；并认为这一时期以百家争鸣的思想奠定了中国文化博大精深的历史根基，成为东方文明的辉煌证明。",
    "Zhao Nong treats the Spring and Autumn and Warring States period as a great transformation in Chinese history, beginning with King Ping's eastward move to Luoyang in 770 BCE and ending with the Qin founding in 221 BCE, 549 years in all; he holds that its Hundred Schools thought laid the broad and deep foundation of Chinese culture and stands as brilliant proof of Eastern civilization.",
    [T + "chunqiu-zhanguo.md", T + "hundred-schools.md"],
    "断言取 L1772 与 L1811。分期起讫与549年为原文直述，未给历法换算与诸侯纪年依据；百家争鸣奠定文化根基为作者评价。概念见 terms/chunqiu-zhanguo、terms/hundred-schools。",
    1767, 1814, [1772, 1811], ["b0067"], "第一节 绪论"))

rows.append(C(
    "claim-0472", "cand-03-67", "historiographic_claim",
    "赵农认为，铁器导致生产力提高、耕作条件和质量明显改进；优质铁农具和先进水利灌溉技术使农田中的“私田”与“公室”出现明显差距，西周以来的“井田制”开始衰败，新兴地主阶层因经济力量逐渐进入政治舞台。",
    "Zhao Nong argues that iron tools raised productivity and markedly improved cultivation; superior iron farm tools and advanced irrigation widened the gap between private fields and ducal holdings, so the Western Zhou well-field system declined and a new landlord class entered politics on the strength of its economic power.",
    [T + "tieqi-shidai.md", T + "iron-farm-tools.md", T + "jingtian-zhi.md"],
    "断言取 L1794。铁器、生产力、井田制与地主阶层的因果链为原文直述，未给农具出土量、亩产量与土地制度变化的统计。概念见 terms/tieqi-shidai、terms/iron-farm-tools、terms/jingtian-zhi。",
    1767, 1814, [1794], ["b0067"], "第一节 绪论"))

rows.append(C(
    "claim-0473", "cand-03-68", "historiographic_claim",
    "赵农认为，社会动荡使原有政治统治松弛，学术思想进入非常活跃的时期，知识分子以积极姿态成为社会文化主流；诸子百家或著书立说、或设坛讲学、或身体力行，思想的力量成为推动中国社会进步的基础。",
    "Zhao Nong holds that social upheaval loosened the old political order and made intellectual life unusually active, with intellectuals taking a positive role as the mainstream of social culture; the Hundred Schools wrote, lectured, or practiced their ideas, and the power of thought became a basis for social progress in China.",
    [T + "hundred-schools.md"],
    "断言取 L1776 并以 L1784“的局面”收束。社会动荡与思想活跃的关系为原文论述；来源未给学派数量、著作年代与传播范围的统计。概念见 terms/hundred-schools。",
    1767, 1814, [1776, 1784], ["b0067"], "第一节 绪论"))

rows.append(C(
    "claim-0474", "cand-03-95", "historiographic_claim",
    "赵农认为，从春秋战国开始中国已经全面进入铁器时代，铸铁技术、锻铸技术遥遥领先，提高了铁器具制作技术水平并加快制作速度；战国中期铁制兵器、农具、工具大量出现，中国社会全面进入铁器时代，成为中古时期世界先进文化的代表之一。",
    "Zhao Nong holds that from the Spring and Autumn and Warring States period China entered the Iron Age in full, with casting and forging techniques far ahead, raising the technical level and speed of iron implement production; by the mid Warring States iron weapons, farm tools, and tools appeared in quantity, making Chinese society fully iron-using and one of the representative advanced cultures of the medieval world.",
    [T + "tieqi-shidai.md", T + "iron-farm-tools.md"],
    "断言合并 L1792 与 L1974 两处“全面进入铁器时代”的表述。领先地位与“中古时期世界先进文化”为作者评价，未给技术比较与器物统计。概念见 terms/tieqi-shidai、terms/iron-farm-tools。",
    1767, 1987, [1792, 1974], ["b0074", "b0067"], "第一节 绪论"))

rows.append(C(
    "claim-0475", "cand-03-71", "factual_claim",
    "赵农指出，春秋战国的战争方式分为步战和车战两种，车战是当时最重要的作战形式，战车成为当时兵器的特殊力量。",
    "Zhao Nong states that Spring and Autumn and Warring States warfare took two forms, infantry and chariot combat; chariot warfare was the most important operational form, and the war chariot became a special military force of the period.",
    [T + "war-chariot.md", T + "chunqiu-zhanguo-zhanche-zhonglei.md", T + "xianqin-mache.md"],
    "断言取 L1824，并引《孙子兵法·作战》“驰车千驷，革车千乘，带甲十万”为据。车战首要地位为原文判断，未给战役统计与车制复原。概念见 terms/war-chariot、terms/chunqiu-zhanguo-zhanche-zhonglei、terms/xianqin-mache。",
    1817, 1839, [1824], ["b0069"], "第二节 车辆与兵器"))

rows.append(C(
    "claim-0476", "cand-03-72", "historiographic_claim",
    "赵农认为，车战减少的原因是骑兵的出现；骑兵不受地形限制，在春秋战国北方晋、赵、燕等国与草原游牧民族的持续征战中，车战不如骑兵和步兵灵活。",
    "Zhao Nong argues that the decline of chariot warfare was caused by the rise of cavalry; unrestricted by terrain, cavalry proved more flexible than chariots and infantry in the prolonged conflicts of Jin, Zhao, and Yan with steppe pastoralists.",
    [R + "zhao-wulingwang.md", T + "war-chariot.md"],
    "断言取 L1838。骑兵起源与车战衰退的因果关系为原文判断；赵武灵王公元前307年组建中原第一支骑兵的说法未给文献出处。概念见 persons/zhao-wulingwang、terms/war-chariot。",
    1817, 1839, [1838], ["b0069"], "第二节 车辆与兵器"))

rows.append(C(
    "claim-0477", "cand-03-80", "historiographic_claim",
    "赵农指出，河南南阳生产的铁矛开始进入战争，《荀子·议兵》“宛钜铁钺，惨如蜂虿”可见其锋利坚韧；铁矛的出现使常规武器发生变化，铁矛成为步兵的武器。",
    "Zhao Nong notes that iron spears from Nanyang entered warfare, their sharpness and toughness attested by the Xunzi line “Wan steel and iron axes, cruel as wasps and scorpions”; the iron spear changed conventional weaponry and became an infantry weapon.",
    [T + "mao.md", B + "xunzi.md"],
    "断言取 L1854。铁矛成为步兵武器为原文判断；《荀子·议兵》引文未给版本、篇次与注释。概念见 terms/mao、publications/xunzi。",
    1840, 1887, [1854], ["b0070"], "第二节 车辆与兵器"))

rows.append(C(
    "claim-0478", "cand-03-85", "factual_claim",
    "赵农描述，湖北江陵出土的“越王鸠浅（勾践）自作用剑”剑体为合金所制，不同剑身有不同金属含量：剑刃含锡比例较高，剑脊含锡比例较低，因此剑身富于弹性、剑刃锋利，削铁如泥。",
    "Zhao Nong describes the sword inscribed “King Goujian of Yue made this for his own use,” unearthed at Jiangling, Hubei: its body is an alloy with different metal contents in different parts, the edges higher in tin and the spine lower, giving the blade elasticity and a sharp edge that cuts iron like mud.",
    [T + "jian-sword.md", T + "qingtong.md"],
    "断言取 L1911。合金配比与“削铁如泥”为原文描述，未给成分检测报告与硬度数据；出土地点按原文记江陵。概念见 terms/jian-sword、terms/qingtong。",
    1888, 1925, [1911], ["b0071"], "第二节 车辆与兵器"))

rows.append(C(
    "claim-0479", "cand-03-91", "historiographic_claim",
    "赵农认为，船只的大量制造和使用使中国南方地区较早进入水上交通的发达阶段，促进了人们生活方式的改变；人们在征服自然、利用水产资源中也提高了自身生存能力。",
    "Zhao Nong holds that the mass production and use of boats brought southern China early into a developed stage of water transport and changed people's ways of life; in mastering nature and using aquatic resources, people also improved their own capacity to survive.",
    [T + "plank-boat.md", T + "chunqiu-zhanguo-zhanchuan-zhonglei.md"],
    "断言取 L1962，并以河南汲县《水陆攻战纹铜鉴》所见图象为据。水上交通与生活方式的关系为作者解释，未给船只遗存与航运规模的统计。概念见 terms/plank-boat、terms/chunqiu-zhanguo-zhanchuan-zhonglei。",
    1926, 1963, [1962], ["b0072"], "第二节 车辆与兵器"))

rows.append(C(
    "claim-0480", "cand-03-96", "historiographic_claim",
    "赵农认为，石磨的出现使面食逐渐成为北方人的生活习惯，面食的长期食用彻底改变了人们的心理习性，也使农耕生活方式与渔猎生活方式开始分离，并带来一系列器具使用的变化。",
    "Zhao Nong argues that the appearance of the stone quern made wheat foods a habit of northerners; long-term consumption of wheat foods thoroughly changed their mental habits, began the separation of farming from hunting-fishing ways of life, and brought a series of changes in implement use.",
    [T + "shi-mo.md"],
    "断言取 L1986。石磨直径约55厘米、砂岩石制为原文所记；面食改变心理习性与生活方式分离为作者推论，未给饮食结构与植物考古证据。概念见 terms/shi-mo。",
    1966, 1987, [1986], ["b0074"], "第三节 农具与工具"))

rows.append(C(
    "claim-0481", "cand-03-107", "historiographic_claim",
    "赵农认为，杠杆原理是石器时期原始先民使用木棒猎取食物或撬动石块时体验和发现到的；有意利用杠杆原理制成平衡器具，成为“权衡”或“衡器”概念的雏形。",
    "Zhao Nong holds that the lever principle was experienced and discovered by Stone Age people when they used wooden sticks to hunt or pry up rocks; deliberately using it to make balance devices produced the prototype of the concepts of quanying and hengqi.",
    [T + "lever.md", T + "hengqi-balance.md"],
    "断言取 L1994。杠杆原理的史前经验来源为作者追溯，未给旧石器工具力学分析；权衡器具的年代与形制未展开。概念见 terms/lever、terms/hengqi-balance。",
    1990, 2039, [1994], ["b0076"], "第三节 农具与工具"))

rows.append(C(
    "claim-0482", "cand-03-111", "interpretive_claim",
    "赵农认为，毛笔的出现使书写的文字有了发展和规范的可能；战国帛画、漆器纹饰绘制及书简书写都需要使用毛笔，而毛笔的书写技巧对汉字作为书法的意义尤为关键。",
    "Zhao Nong argues that the brush made the development and standardization of written characters possible; Warring States silk paintings, lacquer decoration, and bamboo-slip writing all required brushes, and brush technique was crucial to the significance of Chinese characters as calligraphy.",
    [T + "maobi.md", T + "jiance-bamboo-slip-books.md"],
    "断言取 L2045，并以长沙左家公山、信阳长台关战国墓出土竹杆毛笔及《庄子·田子方》“舐笔和墨”为据。毛笔与书法意义的关系为作者解释，未给笔毫材质与书写痕迹的检测。概念见 terms/maobi、terms/jiance-bamboo-slip-books。",
    2040, 2054, [2045], ["b0077"], "第三节 农具与工具"))

rows.append(C(
    "claim-0483", "cand-03-119", "factual_claim",
    "赵农记述，李冰于公元前256年起用六年时间烧山凿石兴建都江堰，利用岷江沙洲修筑鱼嘴分流，并在沙洲尾部与离堆构筑飞沙堰、将部分岷江水引入宝瓶口，形成内外江，这是世界上历史最长的无坝引水工程。",
    "Zhao Nong records that Li Bing, beginning in 256 BCE, spent six years burning rock and cutting stone to build Dujiangyan; he shaped a sandbar in the Min River into a fish-mouth diversion and built the Feisha Weir at its tail and the Leidui, leading part of the Min into the Baoping mouth to form inner and outer channels—the world's longest continuously used damless diversion works.",
    [W + "dujiangyan.md", R + "li-bing.md"],
    "断言取 L2062。公元前256年、六年工期与“世界上历史最长”为原文直述，未给工程测量与水利史认定依据。概念见 works/dujiangyan、persons/li-bing。",
    2055, 2097, [2062], ["b0078"], "第三节 农具与工具"))

rows.append(C(
    "claim-0484", "cand-03-120", "evaluative_claim",
    "赵农评价，任何设计成就的产生都是当时生活的迫切需求，而民间传说的公输般是一个集大成的智慧人物；他观察总结自然现象、依靠个人聪明智慧设计发明便利生活的器具并予以推广，受到老百姓爱戴。",
    "Zhao Nong evaluates: every design achievement arises from an urgent need of its time, and the legendary Gongshu Pan is a synthesizing figure of wisdom who observed natural phenomena, invented implements that made life easier through his own intelligence, spread them among the people, and was beloved for it.",
    [R + "gongshu-pan.md"],
    "断言取 L2096。公输般为“民间传说”人物，原文未区分传说与史实；“集大成的智慧人物”为作者评价。概念见 persons/gongshu-pan。",
    2055, 2097, [2096], ["b0078"], "第三节 农具与工具"))

rows.append(C(
    "claim-0485", "cand-03-126", "historiographic_claim",
    "赵农认为，中国古代城市的特征是城与池的修筑，这是农业文明的基本规律；聚居为市、筑土为城，逐渐形成社会系统结构，并演变为一个地区政治、经济、文化的中心。",
    "Zhao Nong holds that the defining feature of ancient Chinese cities was the building of walls and moats, a basic rule of agricultural civilization; settlement formed markets and pounded earth formed walls, gradually producing a social system that became a regional political, economic, and cultural center.",
    [T + "city-walls-and-moats.md"],
    "断言取 L2102。“农业文明的基本规律”为作者概括，未给中外城市比较与城墙起源的考古序列。概念见 terms/city-walls-and-moats。",
    2100, 2139, [2102], ["b0080"], "第四节 城市与建筑"))

rows.append(C(
    "claim-0486", "cand-03-127", "synthetic_claim",
    "赵农综合临淄城址探测材料指出，齐国临淄是战国大城市，有大小二城：大城为郭城、周长14公里，小城为宫城、周长7公里，城外南、北有宽30米城壕；小城北部为宫殿区、南部为官营手工业作坊，大城北部为平民手工业作坊，官吏居小城宫殿附近、平民居城门左右、工匠商人住市场两旁，其城市特征基本反映了春秋战国列国都城的布局规律。",
    "Synthesizing survey data on the Linzi site, Zhao Nong states that Qi's capital Linzi was a major Warring States city with two walled sections: the outer city, 14 km in perimeter, and the inner palace city, 7 km, with 30-m-wide moats north and south; the inner city held palaces in the north and state workshops in the south, the outer city commoner workshops in the north, officials near the palace, commoners by the gates, and artisans and merchants beside the markets—a pattern basically reflecting the layout of Warring States capitals.",
    [P + "linzi.md", T + "city-walls-and-moats.md", B + "guanzi.md"],
    "断言综合 L2116、L2118、L2120、L2122。周长、城壕宽度与功能分区为原文所记探测结果，未给发掘报告编号与面积数据；“基本反映列国都城布局规律”为作者概括。概念见 places/linzi、terms/city-walls-and-moats、publications/guanzi。",
    2100, 2139, [2116, 2118, 2120, 2122], ["b0080"], "第四节 城市与建筑"))

rows.append(C(
    "claim-0487", "cand-03-128", "interpretive_claim",
    "赵农认为，公元前841年西周周厉王“暴虐侈傲，国人谤王”（《史记·周本纪》）的风波，国人的反抗和咒骂实际上是城市居民对统治者暴虐行为的抗议。",
    "Zhao Nong argues that the 841 BCE upheaval against King Li of Zhou, recorded in the Shiji as “cruel and extravagant, so that the people of the capital slandered the king,” was in effect urban residents protesting a ruler's tyranny.",
    [B + "shiji.md"],
    "断言取 L2138。把“国人”解释为城市居民、把谤王解释为政治抗议，是作者的解释；《史记·周本纪》引文未给版本与页次。概念见 publications/shiji。",
    2100, 2139, [2138], ["b0080"], "第四节 城市与建筑"))

rows.append(C(
    "claim-0488", "cand-03-131", "evaluative_claim",
    "赵农评价，代表春秋战国建筑水平的是当时的宫殿建筑；春秋时期诸侯力量崛起，在列国大兴土木、修建宫殿以示威仪，巨室以宫殿建筑的豪华和庞大体现统治者威严，却也展示了当时的建筑水平。",
    "Zhao Nong evaluates the palaces of the period as the representative achievement of Spring and Autumn and Warring States architecture: as feudal lords rose, they built on a grand scale to display their dignity, and the great houses expressed rulership through luxurious, massive palaces that nonetheless demonstrated the era's architectural level.",
    [T + "high-terrace-architecture.md"],
    "断言取 L2148，并以 L2150 高台建筑与邯郸、淄博土台遗存为上下文。“代表建筑水平”为作者评价，未给宫殿遗址的面积、工期与工匠组织数据。概念见 terms/high-terrace-architecture。",
    2140, 2161, [2148], ["b0081"], "第四节 城市与建筑"))

rows.append(C(
    "claim-0489", "cand-03-137", "evaluative_claim",
    "赵农评价，从服饰功能看，胡服非常简便，带来了生活和作战的迅达；赵武灵王将服饰改革与国家兴盛关联，是中原地区的人们向游牧民族学习、获得国强民富实际效果的例证。",
    "Zhao Nong evaluates the hu dress as highly convenient, bringing speed and ease to daily life and combat; King Wuling of Zhao tied dress reform to national strength, exemplifying how Central Plains peoples learned from pastoral nomads and achieved real prosperity.",
    [T + "hufu.md", R + "zhao-wulingwang.md"],
    "断言取 L2177。胡服功能优势与改革效果为作者评价，未给赵国军力与服饰形制的对比材料。概念见 terms/hufu、persons/zhao-wulingwang。",
    2164, 2191, [2177], ["b0083"], "第五节 服饰与货币"))

rows.append(C(
    "claim-0490", "cand-03-138", "interpretive_claim",
    "赵农认为，从鉴于水到鉴于镜，不仅仅是材料和形式的改变，而且也是文化意识的提高。",
    "Zhao Nong holds that the shift from using water as a mirror to using bronze mirrors was not merely a change of material and form but also a rise in cultural consciousness.",
    [T + "tongjing.md", T + "jian-basin.md"],
    "断言取 L2190。铜镜纹饰（四山纹、羽状纹、蟠螭纹、狩猎纹）为原文所记；“文化意识的提高”为作者解释，未给铜镜出土量与使用人群统计。概念见 terms/tongjing、terms/jian-basin。",
    2164, 2191, [2190], ["b0083"], "第五节 服饰与货币"))

rows.append(C(
    "claim-0491", "cand-03-146", "evaluative_claim",
    "赵农评价，春秋时期的莲鹤方壶体现了青铜器具装饰风格的演变，其构思精巧、制器典雅，是当时的壶器典范，一扫西周礼器沉郁简朴的样式。",
    "Zhao Nong evaluates the Spring and Autumn Lotus-and-Crane hu as embodying the evolution of bronze decorative style: ingenious in conception and elegant in execution, it was the model hu of its day and swept away the somber simplicity of Western Zhou ritual vessels.",
    [T + "hu-vessel.md", T + "qingtongqi.md"],
    "断言取 L2233。壶身蟠龙纹、龙形大耳、莲叶与仙鹤为原文描述；“壶器典范”“一扫西周样式”为作者评价，未给器物的尺寸、收藏地与断代报告。概念见 terms/hu-vessel、terms/qingtongqi。",
    2192, 2252, [2233], ["b0084"], "第五节 服饰与货币"))

rows.append(C(
    "claim-0492", "cand-04-04", "interpretive_claim",
    "赵农认为，在青铜材质的钱币出现时，象形货币成为具有特殊意义的存在；货币形制借用人们熟悉的器物形象（钱铲、镈、刀、纺轮、贝），以满足交换时的精神和心理需求。",
    "Zhao Nong argues that when bronze coinage appeared, pictographic money became a special category; its forms borrowed familiar implement images—spade-money, bo, knife, spinning wheel, and cowrie—to satisfy the spiritual and psychological needs of exchange.",
    [T + "qingtong-qian-chan.md", T + "bu-bi.md", T + "dao-bi.md",
     T + "huan-qian.md", T + "yi-bi-qian.md", T + "beibi.md"],
    "断言综合 L2257 与 L2266-L2274。钱铲、镈、刀、纺轮、贝五种原型为原文分述；“满足精神和心理需求”为作者解释，未给货币出土窖藏与流通范围统计。概念见 terms/qingtong-qian-chan、terms/bu-bi、terms/dao-bi、terms/huan-qian、terms/yi-bi-qian、terms/beibi。",
    2253, 2279, [2257, 2266, 2270, 2272, 2274], ["b0085"], "第五节 服饰与货币"))

rows.append(C(
    "claim-0493", "cand-04-129", "interpretive_claim",
    "赵农引《易经·系辞传下》“日中为市，致天下之民，聚天下之货，交易而退，各得其所”，认为其所指是物物交易的时代；易物习俗有许多不便之处，于是以货币充当中介，固定成为一种特殊的货币。",
    "Quoting the Xici commentary to the Yijing—“At midday markets are held, gathering the people and goods of the realm; after trading they withdraw, each getting what they need”—Zhao Nong takes it to describe an age of barter; because barter was inconvenient, money came to serve as intermediary and became a fixed special currency.",
    [B + "zhouyi.md", T + "beibi.md"],
    "断言取 L2257。《系辞传下》引文未给版本、页次与注家；由物物交易到货币中介的过渡为作者解释。概念见 publications/zhouyi、terms/beibi。",
    2257, 2257, [2257], ["b0085"], "第五节 服饰与货币"))

rows.append(C(
    "claim-0494", "cand-04-09", "evaluative_claim",
    "赵农评价，战国灯具的使用和普及是设计文化的一个显著基本，它改变了以往燃木聚火的被动取光，而代以油脂、蜡烛等材料，拓展了生活空间、延长了活动时间并提高了生活质量。",
    "Zhao Nong evaluates the use and spread of lamps in the Warring States as a notable foundation of design culture: replacing passive light from burning wood with oil and candles, lamps expanded living space, lengthened activity, and improved the quality of life.",
    [],
    "断言取 L2325。油脂、蜡烛等照明材料与三项生活效果为原文直述；来源未给战国灯具的出土数量、燃料类型与照明时长。库内灯具条目多为秦汉，未强行链接以避免时代错置。",
    2309, 2342, [2325], ["b0088"], "第六节 家具与乐器"))

rows.append(C(
    "claim-0495", "cand-04-14", "historiographic_claim",
    "赵农认为，春秋战国时期冶铁业蓬勃兴起，同时青铜技术熟练并得到提高，因此导致了许多新的设计技术的出现，这是中华民族在秦汉历史时期实现腾飞的基础保证之一。",
    "Zhao Nong holds that the vigorous rise of ironworking and the maturing of bronze technology in the Spring and Autumn and Warring States period led to many new design techniques, providing one of the foundations for China's leap forward in the Qin and Han.",
    [T + "tieqi-shidai.md", T + "qingtongqi.md", B + "kaogongji.md"],
    "断言取 L2349。冶铁、青铜技术进步导致新设计技术为原文因果句；“秦汉腾飞的基础保证”为作者评价，未给技术门类清单与传播路径。概念见 terms/tieqi-shidai、terms/qingtongqi、publications/kaogongji。",
    2343, 2352, [2349], ["b0089"], "第七节 先秦设计文献"))

rows.append(C(
    "claim-0496", "cand-04-147", "interpretive_claim",
    "赵农认为，以往较多把道与器的关系对立起来认识，缺少整体理解；“形而上”与“形而下”首先是在形的范畴之中，“上”“下”的区别也在形的规范之内，制形的精神中贯穿着“道”理，体现制形的过程是“器”具；这个立论在庄子著述中阐发得最为具体深刻而生动。",
    "Zhao Nong argues that the relation of dao and qi has often been treated as opposition rather than understood as a whole: the metaphysical and the physical both lie first within the category of form, their difference falls within the norm of form, the spirit of making form is pervaded by dao, and the process that embodies form is the qi implement; Zhuangzi expounded this most concretely, deeply, and vividly.",
    [B + "zhouyi.md", B + "zhuangzi.md"],
    "断言取 L2364，前引《系辞传上》“形而上者谓之道；形而下者谓之器”。道器整体解释为作者立论，未给庄子原文篇次与历代注疏；《系辞传》引文未给版本。概念见 publications/zhouyi、publications/zhuangzi。",
    2364, 2364, [2364], ["b0090"], "第七节 先秦设计文献"))

rows.append(C(
    "claim-0497", "cand-04-21", "historiographic_claim",
    "赵农认为，春秋战国诸子百家论述政治主张时有意或无意记载了许多器具知识，大量文学作品也反映了器具在生活、战争中的状态；文学的情节性描写使《周礼》等典籍中的器具还原成为真实的氛围，因此研究春秋战国的器具设计离不开这些资料性的原始文献。",
    "Zhao Nong holds that the Hundred Schools, in arguing political positions, recorded much implement knowledge intentionally or not, and that literary works reflected the place of implements in life and war; literary narrative restored the implements of texts such as the Zhouli to a real atmosphere, so research on Warring States design cannot do without these primary documentary sources.",
    [B + "shijing.md", B + "zhouli.md"],
    "断言取 L2399，并以《诗经》《楚辞》的文学描写为论据；库内无《楚辞》条目，未链接。诸子与文学记载的器具知识为作者判断，未给逐条文献对照。概念见 publications/shijing、publications/zhouli。",
    2397, 2408, [2399], ["b0091"], "第七节 先秦设计文献"))

rows.append(C(
    "claim-0498", "cand-04-35", "synthetic_claim",
    "赵农综合认为，春秋战国时期的器具设计得力于诸多学者、思想家、工匠的实践活动，也形成了许多规律性的经验总结，表现出卓越的设计艺术思想。",
    "Zhao Nong concludes that Warring States implement design drew on the practice of scholars, thinkers, and artisans, produced many regularized summaries of experience, and displayed outstanding design thought.",
    [T + "hundred-schools.md", B + "kaogongji.md"],
    "断言取 L2450，前文以儒、道、墨、法、兵诸家与平民教育为背景。“卓越的设计艺术思想”为作者总括评价，未给经验总结的文本清单与工匠组织材料。概念见 terms/hundred-schools、publications/kaogongji。",
    2448, 2464, [2450], ["b0094"], "第八节 结论"))

rows.append(C(
    "claim-0499", "cand-04-36", "historiographic_claim",
    "赵农认为，由于冶铁业的发展，促进了社会化的政治改革，也推动了设计文化的发展；东周列国借助技术手段增强了争霸实力，走向诸侯雄起的列国时代。",
    "Zhao Nong holds that ironworking promoted socially organized political reform and also drove design culture forward; the Eastern Zhou states used technological means to strengthen themselves in the struggle for hegemony, entering the age of contending lords.",
    [T + "tieqi-shidai.md"],
    "断言取 L2457。冶铁、政治改革与设计文化的因果结构为原文直述，未给列国变法与技术传播的对照材料。概念见 terms/tieqi-shidai。",
    2448, 2464, [2457], ["b0094"], "第八节 结论"))

rows.append(C(
    "claim-0500", "cand-04-39", "historiographic_claim",
    "赵农指出，欧洲社会此时尚在罗马帝国阶段，东征西讨、横跨欧亚非大陆；此时东西方已经基本形成各自文明的显著特征。",
    "Zhao Nong notes that Europe was then still in the Roman imperial stage, campaigning across Europe, Asia, and Africa; by this time East and West had basically formed the distinctive features of their respective civilizations.",
    [],
    "断言取 L2463。罗马帝国与春秋战国的并置为文明比较判断；来源未给罗马帝国的时间分期与东西方比较的指标体系。库内无对应比较条目，未强行链接。",
    2448, 2464, [2463], ["b0094"], "第八节 结论"))

for row in rows:
    assert row["statement_zh"].strip() and row["statement_en"].strip()

(ROOT / "_zn_zn3a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_zn3a_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")

from collections import Counter
print(json.dumps({
    "rows": len(rows),
    "types": dict(Counter(r["claim_type"] for r in rows)),
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
}, ensure_ascii=False))
