# -*- coding: utf-8 -*-
"""Build 赵农 2009 第一章 claim rows (26 new claims, no merges)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "第一章 文明的曙光——石器时期的设计"


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
    "claim-0404", "cand-01-13", "historiographic_claim",
    "赵农认为，人类的历史就是从设计和制造器具开始的，艺术设计史是伴随人类早期发生而不断进步的过程。",
    "Zhao Nong holds that human history begins with designing and making implements, and that design history is a process advancing with the emergence of early humanity.",
    ["04-knowledge/units/terms/yishu-sheji.md"],
    "断言取 L364。原文以人类历史与器具制造的关系立论，属作者的历史观；来源未给人类起源年代与器物谱系。概念见 terms/yishu-sheji。",
    360, 371, [364], ["b0007"], "第一节 绪论"))

rows.append(C(
    "claim-0405", "cand-01-15", "interpretive_claim",
    "赵农认为工具是武器之母，人类的工具是由石器的进化和发展而形成的。",
    "Zhao Nong holds that tools are the mother of weapons and that human tools developed out of the evolution of stone implements.",
    [],
    "断言取 L392。原文以砾石、打磨技术与弓箭为例展开；工具与武器的发生关系为作者判断，来源未给考古学上的武器起源序列。",
    372, 419, [392], ["b0008"], "第一节 绪论"))

rows.append(C(
    "claim-0406", "cand-01-17", "interpretive_claim",
    "赵农认为，农耕民族的定居生活使他们在采集渔猎之余有充分的思维发育条件，可以积累和完善早期生活经验，从而生成知识与智慧。",
    "Zhao Nong argues that the sedentary life of agrarian peoples gave them ample conditions for developing thought beyond gathering and hunting, allowing early experience to accumulate and knowledge and wisdom to emerge.",
    ["04-knowledge/units/terms/yuanshi-nongju.md"],
    "断言取 L519。原文以生活范围稳定、人口增加、村落到集市的发展解释知识与智慧的生成；来源未给聚落人口数据与比较样本。概念见 terms/yuanshi-nongju。",
    513, 558, [519], ["b0013"], "第三节 石器与玉器"))

rows.append(C(
    "claim-0407", "cand-01-36", "interpretive_claim",
    "赵农认为，对于人类而言设计思想和技术的根本是实用，好用即实用，笨人的工具绝不是设计。",
    "Zhao Nong holds that use is the foundation of design thought and technique: being easy to use is being useful, and a clumsy person's tool is not design at all.",
    [],
    "断言取 L436-L438。好用即实用与笨人的工具绝不是设计均为作者的价值判断；来源未给工具效能测试与反例。",
    422, 455, [436, 438], ["b0010"], "第二节 上古传说的设计"))

rows.append(C(
    "claim-0408", "cand-01-42", "interpretive_claim",
    "赵农指出，良渚文化遗址中的钺、琮、璧等玉器重物是新石器时期中国东部地区的现象；玉钺为兵权、玉琮为神器、玉璧为财富，说明玉器一开始便成为政治权力和个人财富的表现。",
    "Zhao Nong notes that the heavy jades—yue, cong and bi—found at Liangzhu sites are a Neolithic phenomenon in eastern China; the yue stood for military power, the cong for sacral power and the bi for wealth, showing that jades served from the outset as expressions of political power and personal wealth.",
    ["04-knowledge/units/places/liangzhu-gucheng.md",
     "04-knowledge/units/terms/yue-battle-axe.md",
     "04-knowledge/units/terms/yu-yue-cong-bi.md",
     "04-knowledge/units/terms/yushi.md"],
    "断言取 L602。原文先述玉钺为兵权、玉琮为神器、玉璧为财富，再作新石器时期东部地区的一般判断；来源未给良渚墓葬统计与等级序列。器物与概念见 places/liangzhu-gucheng、terms/yue-battle-axe、terms/yu-yue-cong-bi、terms/yushi。",
    592, 603, [602], ["b0015"], "第三节 石器与玉器"))

rows.append(C(
    "claim-0409", "cand-01-47", "historiographic_claim",
    "赵农认为，彩陶三足鼎是中国鼎文化的开端，使鼎成为艺术设计中一种特殊的器具。",
    "Zhao Nong holds that the painted-pottery three-legged ding marks the beginning of Chinese ding culture and made the ding a distinctive implement in design.",
    ["04-knowledge/units/terms/ding.md",
     "04-knowledge/units/terms/taoqi.md"],
    "断言取 L653。原文由三足架钵、留下火塘空间的组合原理推论鼎文化开端；来源未给早期陶鼎的年代序列与类型比较。概念见 terms/ding、terms/taoqi。",
    628, 669, [653], ["b0018"], "第四节 陶器与彩陶"))

rows.append(C(
    "claim-0410", "cand-01-62", "interpretive_claim",
    "赵农认为，骨针技术的运用对手指功能开发有重要的进化意义，使手指灵活性明显提高并促进脑智力发育；骨针的出现还可能带来职业分工变化，老年女性从事缝制、青壮年女性从事制陶、男性从事农耕或狩猎。",
    "Zhao Nong argues that bone needles had evolutionary significance for the development of finger function, improving manual dexterity and stimulating brain development; their appearance may also have brought a division of labour, with older women sewing, younger women making pottery and men farming or hunting.",
    ["04-knowledge/units/terms/shandingdong-ren-guzhen.md",
     "04-knowledge/units/terms/yuanshi-fuzhuang.md"],
    "断言取 L750-L752。骨针与手指、脑智力、职业分工的关系为作者推论；来源未给骨针使用痕迹与人群性别年龄的考古鉴定。概念见 terms/shandingdong-ren-guzhen、terms/yuanshi-fuzhuang。",
    731, 753, [750, 752], ["b0023"], "第五节 骨器与箭器"))

rows.append(C(
    "claim-0411", "cand-01-67", "historiographic_claim",
    "赵农认为，父系社会的出现是在知识与力量的较量中完成的，夫妻父母之道对人类智力和身体发育产生重要作用并形成家庭与部落关系；伏羲的思想是中国父系智慧文化的精神来源，也是力量与意志的象征。",
    "Zhao Nong holds that patrilineal society emerged through a contest of knowledge and force, that the norms of husband and wife and parents and children shaped human intelligence and physical development and formed family and tribal relations, and that Fuxi's thought is the spiritual source of Chinese patrilineal wisdom.",
    ["04-knowledge/units/terms/bagua.md"],
    "断言取 L464。父系社会出现与伏羲思想的判断均属作者的历史解释；来源未给父系社会断代与伏羲传说的文献层累。相关概念见 terms/bagua。",
    464, 464, [464], ["b0011"], "第二节 上古传说的设计"))

rows.append(C(
    "claim-0412", "cand-01-68", "interpretive_claim",
    "赵农认为，春秋时期萧史吹箫引凤、与弄玉升天的故事亦有反抗封建的意义，鲤鱼跳龙门的传说则体现了人生的一种挑战。",
    "Zhao Nong reads the story of Xiao Shi piping to attract phoenixes and ascending with Nong Yu as also carrying anti-feudal meaning, while the legend of the carp leaping the dragon gate embodies a challenge in life.",
    [],
    "断言取 L505-L507。反抗封建与人生挑战为作者对神话的解读；来源未给故事文本出处与年代。",
    505, 507, [505, 507], ["b0011"], "第二节 上古传说的设计"))

rows.append(C(
    "claim-0413", "cand-01-69", "interpretive_claim",
    "赵农认为，每一个器具的起源传说都是理性与浪漫的结合，中国古老传说中的设计类型反映了中国人与自然、自然与技术以及中国人的生活观念。",
    "Zhao Nong holds that every origin legend of an implement combines reason and romance, and that the design types in ancient Chinese legends reflect the relations between people and nature, nature and technology, and Chinese conceptions of life.",
    [],
    "断言取 L525-L527。理性与浪漫的结合为作者对传说的方法论判断；来源未给传说类型划分与样本。",
    525, 527, [525, 527], ["b0013"], "第三节 石器与玉器"))

rows.append(C(
    "claim-0414", "cand-01-70", "historiographic_claim",
    "赵农认为，石器是人类在生活生产中第一次将设计知识进行全面而有意义的应用所产生的，石器设计提供了人与器具关系的基本原理，使中国艺术设计的本质具有特殊的进步意义。",
    "Zhao Nong holds that stone tools resulted from the first comprehensive and meaningful application of design knowledge in production and life, that they supplied a basic principle of the relation between people and implements, and that they gave Chinese design a distinctive progressive significance.",
    [],
    "断言取 L565。第一次、基本原理与特殊的进步意义均为作者评价；来源未给石器功能分析与设计知识定义。",
    565, 565, [565], ["b0014"], "第三节 石器与玉器"))

rows.append(C(
    "claim-0415", "cand-01-71", "factual_claim",
    "赵农指出，从旧石器时期的打制到磨制工具，再到人类第一回研制的复合材料陶器，经历了数十万年。",
    "Zhao Nong states that the passage from Palaeolithic chipped tools to ground tools and then to pottery, humanity's first composite material, took several hundred thousand years.",
    [],
    "断言取 L618。数十万年为原文给出的时间跨度，未给测年依据与分期标准。候选作 basic_fact，按语义映射为 factual_claim。",
    618, 618, [618], ["b0017"], "第四节 陶器与彩陶"))

rows.append(C(
    "claim-0416", "cand-01-72", "factual_claim",
    "赵农指出，烧煮器具为人们体质增强创造了基本条件；陶器出现后木藤材料成为辅助生活用品，藤木作为原生材料被专门用于编织，成为实用的藤编器具。",
    "Zhao Nong states that cooking vessels provided basic conditions for physical development, and that after pottery appeared wood and rattan became auxiliary materials, rattan being devoted to weaving into practical baskets and mats.",
    ["04-knowledge/units/terms/taoqi.md",
     "04-knowledge/units/terms/shougong-bianzhi.md"],
    "断言取 L620-L622。烧煮器具增强体质、陶器出现后藤木转为编织的因果为作者叙述；来源未给体质人类学与编织遗物统计。候选作 basic_fact，按语义映射为 factual_claim。概念见 terms/taoqi、terms/shougong-bianzhi。",
    620, 622, [620, 622], ["b0017"], "第四节 陶器与彩陶"))

rows.append(C(
    "claim-0417", "cand-01-73", "evaluative_claim",
    "赵农评价新石器时期的制陶技术复杂而神奇，对后来中国长期作为陶瓷大国有着积极而深远的影响。",
    "Zhao Nong evaluates Neolithic pottery technology as complex and remarkable, with a positive and far-reaching influence on China's long standing as a ceramic power.",
    ["04-knowledge/units/terms/heitao.md",
     "04-knowledge/units/terms/taoqi.md"],
    "断言取 L689。复杂而神奇、积极而深远为作者评价；来源未给龙山黑陶的工艺参数与陶瓷史影响评估。概念见 terms/heitao、terms/taoqi。",
    689, 689, [689], ["b0019"], "第四节 陶器与彩陶"))

rows.append(C(
    "claim-0418", "cand-02-61", "interpretive_claim",
    "赵农认为，弓箭的设计思想对后来生活有极大影响，这不仅是武器的产生，更是复杂设计思维的形成；由近及远的思维方式通过自然与人力对比在器具设计中具体体现。",
    "Zhao Nong argues that the design thinking behind the bow and arrow greatly influenced later life: it was not merely a weapon but the formation of complex design thought, in which a near-to-far mode of thinking is embodied through the contrast of natural and human force.",
    ["04-knowledge/units/terms/gongjian.md"],
    "断言取 L776。由近及远的思维方式为作者的设计学解释；来源未给弓箭弹道、射程实验与认知考古证据。概念见 terms/gongjian。",
    768, 792, [776], ["b0025"], "第五节 骨器与箭器"))

rows.append(C(
    "claim-0419", "cand-02-62", "interpretive_claim",
    "赵农引恩格斯《家庭、私有制和国家的起源》语，认为弓箭对于蒙昧时代如同铁剑对于野蛮时代、火器对于文明时代一样，是决定性的武器。",
    "Quoting Engels in The Origin of the Family, Private Property and the State, Zhao Nong holds that the bow and arrow were as decisive a weapon for savagery as the iron sword for barbarism and firearms for civilization.",
    ["04-knowledge/units/terms/gongjian.md"],
    "断言取 L787。原文直接引用恩格斯著作中译句，属转引；来源未给版本、页码与译者。候选作 source_claim，按语义映射为 interpretive_claim。概念见 terms/gongjian。",
    768, 792, [787], ["b0025"], "第五节 骨器与箭器"))

rows.append(C(
    "claim-0420", "cand-02-63", "interpretive_claim",
    "赵农认为，建筑的萌生取决于安居意识、物质的力量与文化的选择三个条件；安全是首位考虑，建筑最初首先是因地制宜的方式选择。",
    "Zhao Nong holds that architecture arose from three conditions—a sense of dwelling, material power and cultural choice—with safety the first consideration and local adaptation the earliest mode of building.",
    ["04-knowledge/units/places/banpo-site.md",
     "04-knowledge/units/places/hemudu-site.md",
     "04-knowledge/units/terms/bandixue-shi-jianzhu.md",
     "04-knowledge/units/terms/ganlan-shi-jianzhu.md"],
    "断言取 L816-L822。三条件说是作者的理论概括；半坡半地穴式与河姆渡干栏式为例证，来源未给建筑遗构的完整复原。见 places/banpo-site、places/hemudu-site、terms/bandixue-shi-jianzhu、terms/ganlan-shi-jianzhu。",
    812, 829, [816, 818, 820, 822], ["b0028"], "第六节 建筑与村落"))

rows.append(C(
    "claim-0421", "cand-02-64", "interpretive_claim",
    "赵农认为，从新石器时期仰韶文化开始，中国原始先民就有面南而居的特征，最终形成中国人居住的心理习惯，面南而居成为中国建筑的方位意识。",
    "Zhao Nong holds that from the Yangshao culture of the Neolithic, Chinese people favoured south-facing dwellings, a preference that became a psychological habit and the orientation principle of Chinese architecture.",
    ["04-knowledge/units/places/banpo-site.md"],
    "断言取 L824-L828。面南而居的心理习惯为作者由半坡房屋朝向所作的推论；来源未给全部房屋朝向统计。遗址见 places/banpo-site。",
    812, 829, [824, 826, 828], ["b0028"], "第六节 建筑与村落"))

rows.append(C(
    "claim-0422", "cand-02-65", "historiographic_claim",
    "赵农认为，城堡的出现使技术职业专门化成为可能，制陶、琢玉、纺织、冶金等行业与农业开始剥离，出现具有手工业设计意义的劳作，器具设计生产明显进步；城堡同时成为权力中心。",
    "Zhao Nong holds that the rise of walled towns made craft specialization possible: pottery, jade working, textiles and metallurgy began to separate from agriculture, handicraft design appeared and implement production advanced, while the town became a centre of power.",
    ["04-knowledge/units/places/xishan-chengzhi.md"],
    "断言取 L878-L880。城堡与技术职业专门化的因果为作者由城墙、陶质下水管道、作坊与铜渣所作的推论；来源未给手工业作坊的定量分析。城址见 places/xishan-chengzhi。",
    863, 881, [878, 880], ["b0030"], "第六节 建筑与村落"))

rows.append(C(
    "claim-0423", "cand-02-66", "interpretive_claim",
    "赵农认为，中国原始先民对蚕桑的认识和驯养知识缘于农耕定居生活。",
    "Zhao Nong holds that the knowledge of sericulture and silkworm domestication among early Chinese peoples derived from sedentary agrarian life.",
    ["04-knowledge/units/persons/leizu.md",
     "04-knowledge/units/terms/qi-silk.md"],
    "断言取 L886。蚕桑驯养缘于农耕定居为作者因果判断；来源未给蚕桑起源的考古证据与年代。人物与概念见 persons/leizu、terms/qi-silk。",
    884, 900, [886], ["b0032"], "第七节 纺织与饰品"))

rows.append(C(
    "claim-0424", "cand-02-67", "historiographic_claim",
    "赵农认为，纺轮利用转动使丝线螺旋缠绕、形成合股，替代了用手搓制绳线，使丝线均匀、连绵不绝，提高了纺织技术，为织布业大量出现确立了坚实基础。",
    "Zhao Nong holds that the spinning whorl used rotation to twist fibres into uniform, continuous plied thread, replacing hand twisting, raising textile technique and laying a firm basis for large-scale weaving.",
    ["04-knowledge/units/terms/fanglun.md"],
    "断言取 L913。纺轮的技术替代与产业意义为作者总结；来源未给纺轮转速、纱线支数与织机关系的实验。概念见 terms/fanglun。",
    901, 935, [913], ["b0033"], "第七节 纺织与饰品"))

rows.append(C(
    "claim-0425", "cand-02-68", "interpretive_claim",
    "赵农认为，货币的出现说明先民已经确立计数概念，对数和量有了一定认识，并逐渐改变物物交换的原始商品观念，开始货币价值的交换行为。",
    "Zhao Nong argues that the appearance of currency shows that early people had formed a concept of counting and some grasp of number and quantity, gradually changing barter and beginning exchange by monetary value.",
    ["04-knowledge/units/terms/beibi.md"],
    "断言取 L962。由贝币推论计数概念与交换行为的变化，属作者解释；来源未给海贝、石贝的计量与出土情境统计。概念见 terms/beibi。",
    936, 963, [962], ["b0034"], "第七节 纺织与饰品"))

rows.append(C(
    "claim-0426", "cand-02-69", "historiographic_claim",
    "赵农认为，文字在漫长演变中逐渐规范并具有约定俗成的意义，是中华民族思维方式的第一次重大飞跃，是由量到质的变化。",
    "Zhao Nong holds that writing gradually became standardized and conventionally meaningful over a long evolution, constituting the first major leap in Chinese modes of thought and a change from quantity to quality.",
    ["04-knowledge/units/terms/banpo-kehua-fuhao.md"],
    "断言取 L970。第一次重大飞跃与由量到质为作者对文字起源的评价；来源未给半坡符号的释读与文字定义。概念见 terms/banpo-kehua-fuhao。",
    964, 984, [970], ["b0035"], "第七节 纺织与饰品"))

rows.append(C(
    "claim-0427", "cand-02-70", "synthetic_claim",
    "赵农认为，中华民族早期的定居生活方式是地理环境影响促使文化较快成熟的必然结果，也是在劳作生活中观察自然、反复实践的体现；人的智慧发挥与手艺提高促使艺术设计文化诞生。",
    "Zhao Nong holds that early Chinese sedentary life was a necessary outcome of geographical influences hastening cultural maturity and of repeated observation and practice in work and life, and that human intelligence and improving craft gave rise to design culture.",
    [],
    "断言取 L1022。第八节结论综合全章材料；地理环境决定论与文化成熟的关系为作者判断，来源未给环境考古与比较样本。",
    1020, 1027, [1022], ["b0037"], "第八节 结论"))

rows.append(C(
    "claim-0428", "cand-02-95", "evaluative_claim",
    "赵农评价西安半坡出土的磨制骨角质渔钩是一种奇异的设计发明和设计思想的成熟；钓鱼比渔网、鱼叉或弓箭捕鱼的心理活动更丰富，是意志与耐力的体现，其过程形成一种哲学观念。",
    "Zhao Nong evaluates the ground bone and antler fishhooks from Banpo as a remarkable invention and a sign of mature design thinking; fishing with a hook, he argues, involves richer mental activity than nets, spears or bows, embodies will and endurance and constitutes a philosophical process.",
    ["04-knowledge/units/places/banpo-site.md"],
    "断言取 L789-L791。奇异的设计发明、设计思想的成熟与哲学观念均为作者评价；来源未给渔钩的形态测量、使用痕迹与效率实验。遗址见 places/banpo-site。",
    789, 791, [789, 791], ["b0025"], "第五节 骨器与箭器"))

rows.append(C(
    "claim-0429", "cand-02-97", "interpretive_claim",
    "赵农认为，从饰物到图案的递进是一步之遥；原始先民以贝壳、彩石连缀饰物，既体现秩序与变化的法则，也包含色彩与线条的装饰观念，并与新石器时期彩陶二方连续图案的成熟有明确关系。",
    "Zhao Nong holds that the step from ornament to pattern is a short one: shell and coloured-stone strings embody a law of order and variation and a decorative sense of colour and line, and are clearly related to the maturity of two-direction continuous patterns on Neolithic painted pottery.",
    ["04-knowledge/units/terms/caihui-tao.md"],
    "断言取 L954-L956。由饰物连缀推论二方连续图案的成熟，属作者判断；来源未给饰物组合与彩陶纹样的统计对应。概念见 terms/caihui-tao。",
    954, 956, [954, 956], ["b0034"], "第七节 纺织与饰品"))

for row in rows:
    assert row["statement_zh"].strip() and row["statement_en"].strip()

(ROOT / "_zn_zn1b_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_zn1b_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")

from collections import Counter
print(json.dumps({
    "rows": len(rows),
    "types": dict(Counter(r["claim_type"] for r in rows)),
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
}, ensure_ascii=False))
