# -*- coding: utf-8 -*-
"""Build 李立新 2011 claim rows, batch ll2a (第一章 造物起源与体系形成, 45 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
SRC = "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"
DATE = "2026-10-27"
CH = "第一章 造物起源与体系形成（设计意识、适应性、原始设计、早期设计世界、轴心时代造物思想、规范化与体系形成）"

T = "04-knowledge/units/terms/"

MAP = ROOT / "03-processing/2011-lilixin-zhongguo-sheji-yishu-shilun/source-map.jsonl"
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
    "claim-1084", "cand-02-100", "historiographic_claim",
    "目前设计史的任务不是寻找“第一把石刀”，而是透过石器的发生学，从石器的打制过程去体味最初造物的“设计”特色。",
    "The task of design history is not to search for the first stone knife but, through the genesis of stone tools, to discern the design character of the earliest artifacts in their knapping process.",
    [T + "yishu-shejishi.md", T + "paleolithic-period.md", T + "beijingren-moshi.md"],
    "断言语义取 L410。原文以贾兰坡推测及蓝田、元谋等更早材料说明“第一把石刀”难以确定；claim 保留方法论判断，不把“设计特色”扩张为审美评价。",
    410, 410, [410], "一、最初的“设计”意识"))

rows.append(C(
    "claim-1085", "cand-02-101", "interpretive_claim",
    "造物目的决定着制作方法和对造物材料的选择；按“何种形式”造物，体现出造物具有目的性、预见性、自觉性、规则性，这是理解最初“设计”意识产生的关键。",
    "The purpose of making determines the production method and the choice of materials; making in a certain form embodies purposiveness, foresight, self-awareness and regularity, which is the key to understanding the emergence of the earliest design consciousness.",
    [T + "sheji.md", T + "beijingren-moshi.md"],
    "断言语义取 L412。原文将“何种形式”作为造物方式的核心提法；claim 保留四性并列，不把它归为单一心理能力。",
    412, 412, [412], "一、最初的“设计”意识"))

rows.append(C(
    "claim-1086", "cand-02-102", "synthetic_claim",
    "最初的设计发展可分为三个阶段：第一阶段是利用自然物的设计，出现于前猿人时期；第二阶段是简易的加工设计，出现在整个旧石器时代；第三阶段是制造工具设计，成于旧石器时代晚期和新石器时代。",
    "The earliest development of design falls into three stages: design by using natural objects in the pre-Peking-Man period; simple processing design throughout the Paleolithic; and tool-making design completed in the Upper Paleolithic and Neolithic.",
    [T + "paleolithic-period.md", T + "xinshiqi-shidai.md", T + "sanzhong-zaowu-sheji.md"],
    "断言语义取 L453。三阶段为原文对石器发生过程的综合；claim 保留阶段名称与时代下限，不补绝对年代。",
    453, 453, [453], "一、最初的“设计”意识"))

rows.append(C(
    "claim-1087", "cand-02-103", "interpretive_claim",
    "造物是一种“适应性设计”，从自然本能的适应到创造性适应，进而推动造物设计向前发展。",
    "Making is a kind of adaptive design: it moves from instinctive adaptation to creative adaptation and thereby drives artifact design forward.",
    [T + "shiyingxing-sheji.md", T + "sheji.md"],
    "断言语义取 L461。原文以此作为本节把握远古造物文化特征的线索；claim 保留“适应性设计”的概念框定。",
    461, 461, [461], "二、适应性：环境、创造、进化"))

rows.append(C(
    "claim-1088", "cand-02-104", "interpretive_claim",
    "磨制石器诞生的最直接因素是农耕生产，其次是磨制、切割、钻孔的石器制作技术，再是装饰审美和原始宗教的因素。",
    "The most direct factor in the emergence of polished stone tools was agricultural production, followed by polishing, cutting and drilling techniques, and then by decorative taste and primitive religion.",
    [T + "shiyingxing-sheji.md", T + "xinshiqi-shidai.md"],
    "断言语义取 L495。原文列农业、技术、装饰、审美、宗教五因子并以农耕为首；claim 保留排序与“最直接”的限定，不改为唯一原因。",
    495, 495, [495], "二、适应性：环境、创造、进化"))

rows.append(C(
    "claim-1089", "cand-02-105", "interpretive_claim",
    "“适应”的概念不仅符合生物学形式，而且也适合造物艺术学应用。",
    "The concept of adaptation not only fits biological form but is also applicable to the study of artifact art.",
    [T + "shiyingxing-sheji.md"],
    "断言语义取 L504。原文以石器工具案例说明概念的跨域适用；claim 只保留适用性判断，不扩展为生物决定论。",
    504, 504, [504], "二、适应性：环境、创造、进化"))

rows.append(C(
    "claim-1090", "cand-02-106", "interpretive_claim",
    "石器造型经历了由圆形到几何形的发展序列：旧石器时代圆形→磨制石器初期方圆结合的过渡形→矩形方形→新石器中期简单的几何化形→新石器晚期复杂的几何化形；方形是在由打制到磨制的过程中，从砾石的圆形基础上发展起来的。",
    "Stone-tool form follows a sequence from round to geometric: Paleolithic round forms, transitional round-square forms in the early polished stage, rectangular-square forms, simple geometric forms in the middle Neolithic, and complex geometric forms in the late Neolithic; the square developed from the round cobble in the shift from knapping to polishing.",
    [T + "yuanzaoxing.md", T + "xinshiqi-shiqi-leixing.md", T + "paleolithic-period.md"],
    "断言语义取 L519-L523。原文以仰韶、大汶口、马家浜、良渚石斧石钺为例；claim 保留五段序列，不把序列当作单线年代标尺。",
    519, 523, [519, 523], "三、原始设计：多样性与统一性"))

rows.append(C(
    "claim-1091", "cand-02-107", "evaluative_claim",
    "庙底沟先民6000年前在多样统一基础上创立的图案格式，成为后世人们在装饰中广泛应用的重要图案组织形式；现在我们经常运用的图案形式，包括国外引进的“构成”，都没有超过庙底沟的模式。",
    "The pattern formats that Miaodigou people created on the basis of unity in diversity 6,000 years ago became important organizing forms widely used in later decoration; current pattern forms, including the imported composition method, have not surpassed the Miaodigou model.",
    [T + "miaodigou-xing-caitao.md", T + "caihui-tao.md"],
    "断言语义取 L538。评价性判断；claim 保留“没有超过”的原文强度，不补跨文化比较样本。",
    538, 538, [538], "三、原始设计：多样性与统一性"))

rows.append(C(
    "claim-1092", "cand-02-108", "interpretive_claim",
    "六大设计区域与苏秉琦的六大考古文化区域完全对应，实际上也是中国文明的六个发端地，是“满天星斗”的文明火花，也是中国设计文化的“总根系”。",
    "The six design regions correspond exactly to Su Bingqi's six archaeological culture regions; they are also the six cradles of Chinese civilization, its scattered sparks, and the root system of Chinese design culture.",
    [T + "liuda-sheji-quyu.md", T + "yangshao-culture.md", T + "longshan-culture.md"],
    "断言语义取 L557。六个区域名见 L553-L557；claim 以“六大设计区域”概括，不重复列举各区域特征。",
    557, 557, [557], "三、原始设计：多样性与统一性"))

rows.append(C(
    "claim-1093", "cand-02-109", "interpretive_claim",
    "中国早期设计的历史范围与中国青铜时代大体相当，有大约1500年之久，这是中国设计史上重要的发展时期。",
    "The historical scope of early Chinese design broadly coincides with the Chinese Bronze Age and lasts about 1,500 years; it is an important period in Chinese design history.",
    [T + "qingtong-shiqi.md", T + "qingtong-shidai.md", T + "xianqin-sandai.md"],
    "断言语义取 L591。原文“大体相当”“大约”保留模糊度；claim 不把1500年落实为精确起止年。",
    591, 591, [591], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1094", "cand-02-110", "interpretive_claim",
    "三代青铜器设计“内圆外方”的造型并不是完全重新创造的；虽不能说是从原始设计的玉琮造型直接蜕变而来，但两者所具有的共同特点不能用偶然性来解释，显然有密切的联系。",
    "The inner-round, outer-square form of Bronze Age ritual vessels was not entirely newly created; although it cannot be said to have evolved directly from the jade cong, their shared features cannot be explained by coincidence and point to a close connection.",
    [T + "cong.md", T + "yu-yue-cong-bi.md", T + "qingtong-liqi.md", T + "taotie-motif.md"],
    "断言语义取 L600-L602。原文同时以造型及良渚兽面纹与商周饕餮纹的关系作证；claim 只取造型一句，纹饰关系留给 claim-1095。",
    600, 602, [600, 602], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1095", "cand-02-111", "interpretive_claim",
    "中国早期设计世界从此开始出现尊卑之别，“象”之器成为“神”之器，早期设计就不只是一种普通的造物活动，而是一种与政治伦理相应的造物活动了。",
    "From this point the early Chinese design world began to distinguish high from low; vessels of image became vessels of spirit, and early design became not merely ordinary making but making answerable to political ethics.",
    [T + "qingtong-liqi.md", T + "taotie-motif.md", T + "li-yue-zhidu.md"],
    "断言语义取 L612。承 L602-L612 兽面纹伦理化论述；claim 保留“象”与“神”的原文对照。",
    612, 612, [612], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1096", "cand-02-112", "interpretive_claim",
    "中外学者一致认为，中国青铜冶铸走了一条与世界其他地区截然不同的道路，即用陶土制模作范的范铸法；由范铸法铸造的青铜器精美绝伦、坚实耐用，使中国青铜器设计成为世界青铜文化的典范。",
    "Chinese and foreign scholars agree that Chinese bronze casting followed a path fundamentally different from other regions, namely clay mold and piece-mold casting; the resulting vessels are exquisite and durable, making Chinese bronze design a model of world bronze culture.",
    [T + "qingtong.md", T + "qingtongqi.md", T + "qingtong-shiqi.md"],
    "断言语义取 L631。“中外学者一致认为”为作者转述，claim 保留归属短语，不把转述升级为独立论证。",
    631, 631, [631], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1097", "cand-02-113", "interpretive_claim",
    "一件新品种的出现，首先不是发生在实用与精神审美之间，而是在工艺技术材料的突破上。",
    "A new artifact type first emerges not from the tension between utility and spiritual aesthetics but from a breakthrough in craft technique and material.",
    [T + "qingtong.md", T + "sheji.md"],
    "断言语义取 L644。原文以此总结三代建筑、纺织、车、漆器等技术规模发展；claim 保留“首先”的因果排序。",
    644, 644, [644], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1098", "cand-02-114", "interpretive_claim",
    "三代之前是原始的自然宗教表现，夏商时期发展为人为的祭祀宗教表现，到西周又形成了理性的伦理宗教表现。",
    "Before the Three Dynasties religion appeared as primitive natural religion; in the Xia and Shang it developed into deliberate sacrificial religion; by the Western Zhou it had become a rational ethical religion.",
    [T + "li-yue-zhidu.md", T + "xianqin-sandai.md"],
    "断言语义取 L660。原文借弗雷泽《金枝》区分巫术与宗教；claim 采用其三分序列，不评价该框架本身。",
    660, 660, [660], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1099", "cand-02-115", "interpretive_claim",
    "思维、功能、工艺、宗教中许多不同于其他文明的因素，作为坚实的基础，在中国造物设计体系的形成中起到了关键的作用。",
    "Many factors in thought, function, craft and religion that differ from other civilizations served as a firm foundation and played a key role in the formation of the Chinese artifact-design system.",
    [T + "sheji.md", T + "xianqin-sandai.md"],
    "断言语义取 L670。原文列举方位天地观念、琢玉、合范铸铜、礼仪、服饰形制、官僚控制等；claim 以“许多因素”概括，不逐项展开。",
    670, 670, [670], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1100", "cand-02-116", "historiographic_claim",
    "“轴心”说的框架不足以完全把握中国历史的演进，也不足以把握中国造物历史文化的特殊性；以儒家思想规范造物设计并未在春秋战国时期完成。",
    "The Axial Age framework cannot fully grasp the course of Chinese history or the particularity of Chinese artifact culture; the regulation of design by Confucian thought was not completed in the Spring and Autumn and Warring States period.",
    [T + "zhouxin-shidai.md", T + "chunqiu-zhanguo.md", T + "yishu-shejishi.md"],
    "断言语义取 L674。原文先述雅斯贝斯，再作框架批评；claim 保留“不足以完全把握”的分寸，不否定轴心说本身。",
    674, 674, [674], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1101", "cand-02-117", "evaluative_claim",
    "诸子言论只是借题发挥，其目的仍在于治国平天下，不可能提出真正有利于造物发展的思想。",
    "The various masters used making as a pretext for argument; their aim remained ordering the state and pacifying the realm, so they could not propose ideas genuinely conducive to the development of making.",
    [T + "jiuliu-shijia.md", T + "zhouxin-shidai.md"],
    "断言语义取 L739。评价针对诸子整体，原文同时承认墨子为造物设计家；claim 保留整体判断，不据此否认个别技术论述。",
    739, 739, [739], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1102", "cand-02-118", "evaluative_claim",
    "墨子“用财少而为利多”的造物原则，与今日现代主义设计以功能为第一的原则如出一辙，令人深思。",
    "Mozi's principle of using little wealth to produce much benefit is strikingly similar to the function-first principle of modern design, which merits reflection.",
    [T + "jiuliu-shijia.md", T + "wenzhi.md"],
    "断言语义取 L729。原文作“始出一辙”，疑为“如出一辙”之讹；statement 用通行写法，note 保留原文异文。跨时代类比属作者评价。",
    729, 729, [729], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1103", "cand-02-119", "interpretive_claim",
    "老子的“大器晚成”实有大器免饰之意；其装饰不是一般意义上的外表装饰，而是追求一种不装饰的装饰。",
    "Laozi's late completion of the great vessel in fact means the great vessel is left unadorned; his ornament is not ordinary surface decoration but the pursuit of an unornamented ornament.",
    [T + "jiuliu-shijia.md"],
    "断言语义取 L731。原文据《帛书》乙本“大器免成”及萧兵说作解；claim 保留作者解释，不把“免饰”当作唯一定论。",
    731, 731, [731], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1104", "cand-02-120", "evaluative_claim",
    "庄子和谐的生态理想是人类最早的造物理性哲学思考；在当代工业社会无节制地大量生产与消耗、无限制地控制占有物的世界的时候，庄子为现代人类造物提供了可借鉴的有益的思想。",
    "Zhuangzi's ecological ideal of harmony is the earliest rational philosophical reflection on making; amid modern industry's unrestrained production, consumption and possession, it offers a useful reference for contemporary making.",
    [T + "jiuliu-shijia.md"],
    "断言语义取 L733。评价跨古今；claim 保留“人类最早”的强判断与“可借鉴”的限定，不扩展为生态设计理论。",
    733, 733, [733], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1105", "cand-02-121", "evaluative_claim",
    "韩非继承商鞅和荀况的“务本禁末”思想，把本与农、末与工商包括“綦组锦绣刻画”直接联系，形成“重本抑末”的思想，这在一定程度上扼杀了造物的创造性活动，给后世造物设计带来了很大的负面影响。",
    "Han Fei inherited the Shang Yang and Xunzi doctrine of attending to the root and prohibiting the branch, linking the root to agriculture and the branch to craft and commerce, including fine weaving and carving; this formed the idea of valuing the root and suppressing the branch, which to some extent stifled creative making and had a strong negative influence on later design.",
    [T + "jiuliu-shijia.md", T + "gong-shang-shi-guan.md"],
    "断言语义取 L735。原文以楚人鬻珠、秦伯嫁女说明文有害于质；claim 取“重本抑末”及其后果，不合并前句文质论。",
    735, 735, [735], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1106", "cand-02-122", "evaluative_claim",
    "管仲的思想立足于经济管理，从造物生产活动到商品流通市场、促进造物设计的繁荣及从市场调节中获利；这是最早的设计经济学论述，是极有价值的。",
    "Guanzi's thought is grounded in economic management, moving from production to market circulation, promoting the prosperity of design and profiting through market adjustment; it is the earliest discussion of design economics and is highly valuable.",
    [T + "jiuliu-shijia.md", T + "gong-shang-shi-guan.md"],
    "断言语义取 L737。原文同时说这些思想“并不系统”、调节作用“不得而知”；claim 保留“最早”“极有价值”的评价，note 保留其不确定处。",
    737, 737, [737], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1107", "cand-02-123", "interpretive_claim",
    "规范化在战国时期已制度化，至秦汉而逐渐完善；这种情形非独发生于船舶设计，而是一种普遍的造物现象。",
    "Standardization was institutionalized by the Warring States and gradually perfected through the Qin and Han; this occurred not only in ship design but as a general phenomenon of making.",
    [T + "guifanhua.md", T + "xianqin-sandai.md"],
    "断言语义取 L781。原文以制铜“六分其金”、制车分工、建筑“明堂之制”为例；claim 保留“普遍现象”的总判断。",
    781, 781, [781], "六、从规范化的完善看造物体系的形成"))

rows.append(C(
    "claim-1108", "cand-02-124", "interpretive_claim",
    "造物“规范”的意识最初源于人体；“布指知寸，布手知尺”，尺的汉字就是用手计量物体的象形。",
    "The awareness of normative measure in making originally derived from the human body; a finger's breadth gives the inch and a hand's spread gives the foot, and the character for chi is a pictograph of measuring with the hand.",
    [T + "guifanhua.md", T + "baigong.md"],
    "断言语义取 L747。原文引《说文解字·尸部》说明以人体为法；claim 保留字源解释，不把它当作所有度量制的唯一起源。",
    747, 747, [747], "六、从规范化的完善看造物体系的形成"))

rows.append(C(
    "claim-1109", "cand-02-125", "evaluative_claim",
    "木板船在设计史上具有重大意义：它不仅摆脱了自然原木大小的限制，也使设计标准化迈进了一大步。",
    "The plank boat is of great significance in design history: it not only escaped the size limits of natural logs but also advanced design standardization by a major step.",
    [T + "plank-boat.md", T + "dugout-canoe.md"],
    "断言语义取 L759。原文以周武王300条战船与“泛舟之役”说明批量生产能力；claim 只保留设计史意义判断。",
    759, 759, [759], "六、从规范化的完善看造物体系的形成"))

rows.append(C(
    "claim-1110", "cand-02-126", "interpretive_claim",
    "汉代造纸的发明弥补了“缣贵而简重”的缺点，为平面设计开拓了新领域。",
    "The Han invention of papermaking remedied the defects of expensive silk and heavy bamboo slips and opened a new field for graphic design.",
    [T + "ma-zhi.md", T + "yishu-shejishi.md"],
    "断言语义取 L798。原文以书籍、年画等新设计形式说明“新领域”；claim 保留因果判断，不把造纸归为单一发明人。",
    798, 798, [798], "1. 造物技术的成熟及设计领域的拓展"))

rows.append(C(
    "claim-1111", "cand-02-127", "evaluative_claim",
    "汉代合理的功能结构设计与系统齐全的品种类型，体现出卓越的设计思想；这种科学系统的设计只有在优化、协调、组合的规范原则下才能实现。",
    "The rational functional and structural design and the complete system of types in the Han dynasty embody an outstanding design thinking; such scientific and systematic design could only be realized under the normative principles of optimization, coordination and combination.",
    [T + "guifanhua.md", T + "dongwuxing-dengju.md"],
    "断言语义取 L823。原文例证为长信宫灯、雁鱼铜灯与马王堆漆食具；claim 保留“只有……才能”的必要条件表述。",
    823, 823, [823], "2. 更为合理的功能设计和品类的系统齐全"))

rows.append(C(
    "claim-1112", "cand-02-128", "interpretive_claim",
    "三代宗教信仰与原始时期从原始思维形态中自发形成的宗教形式不同，在社会行为上已摆脱非理性的神秘巫术力量，演化为各种相应的礼仪制度，成为人为的、可控的、理性的行为。",
    "The religious belief of the Three Dynasties differed from the spontaneously formed religion of primitive thought; in social action it had escaped irrational magical forces and evolved into corresponding ritual institutions, becoming deliberate, controllable and rational behavior.",
    [T + "li-yue-zhidu.md", T + "xianqin-sandai.md"],
    "断言语义取 L646。原文以此作为讨论三代宗教与造物设计关系的前提；claim 保留“已摆脱”的强判断。",
    646, 646, [646], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1113", "cand-02-129", "factual_claim",
    "早在商代，中国已有与范铸法不同的打锻、锤揲工艺技术出现，西周时普遍应用于金属加工；但自夏商以来出土的青铜容器达10万件以上，未有一件是应用打锻法成形的。",
    "As early as the Shang, China had forging and hammering techniques distinct from piece-mold casting, and by the Western Zhou they were widely used in metalworking; yet of the more than 100,000 bronze vessels excavated from the Xia and Shang onward, none was formed by forging.",
    [T + "qingtong.md", T + "qingtongqi.md", T + "qingtong-shiqi.md"],
    "断言语义取 L635。事实陈述含数量与全称否定；claim 保留原文统计口径，不补样本来源与统计方法。",
    635, 635, [635], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1114", "cand-02-130", "evaluative_claim",
    "提花技术丰富了丝织品的内容，自商代到春秋战国逐渐发展定型，至汉代成为标准化的提花织物，之后传至国外，对世界纺织技术的发展产生了很大的影响。",
    "Figured weaving enriched silk textiles, developed and stabilized from the Shang through the Spring and Autumn and Warring States, became standardized figured fabric in the Han, and later spread abroad, greatly influencing world textile technology.",
    [T + "tihuaji.md", T + "shangzhou-sizhiwu.md", T + "zhijin.md", T + "qi-silk.md"],
    "断言语义取 L794。原文以藁城铜觥织物痕迹、瑞典远东古物博物馆藏青铜钺丝织物残痕等为证；claim 保留技术传播的总体评价。",
    794, 794, [794], "1. 造物技术的成熟及设计领域的拓展"))

rows.append(C(
    "claim-1115", "cand-02-131", "interpretive_claim",
    "造物的美是依存的美，它依附于器物的实用目的，但其美的形式也具有社会的内涵。",
    "The beauty of artifacts is dependent beauty: it attaches to the practical purpose of the object, yet its beautiful form also carries social meaning.",
    [T + "wenzhi.md"],
    "断言语义取 L627。原文接下以“美”字设计为例；claim 只取依存美命题，不合并文字设计判断（见 claim-1116）。",
    627, 627, [627], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1116", "cand-02-132", "interpretive_claim",
    "“美”的文字设计的价值取向，必然影响到民族审美范畴的形成。",
    "The value orientation embodied in the character design of mei inevitably shaped the formation of the national aesthetic category.",
    [T + "oracle-bone-script.md", T + "wenzhi.md"],
    "断言语义取 L629。原文以“羊大”为美及六畜统计作证；claim 保留“必然影响”的强因果表述。",
    629, 629, [629], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1117", "cand-02-133", "interpretive_claim",
    "王室衰微、权力下移和官营手工业的削弱，使造物设计一度与宗法秩序和王朝政治渐次脱钩，私营手工业获得新的发展契机，造物设计呈现出自由竞争的局面。",
    "The decline of the royal house, the downward shift of power and the weakening of state-run handicraft detached design for a time from clan order and dynastic politics; private handicraft gained new opportunities and design entered a phase of free competition.",
    [T + "chunqiu-zhanguo.md", T + "guanying-shougongye.md", T + "gong-shang-shi-guan.md", T + "jiuliu-shijia.md"],
    "断言语义取 L716-L718。原文以莲鹤方壶与士人流动说明新格局；claim 保留“一度”“渐次”的程度限定。",
    716, 718, [716, 718], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1118", "cand-02-134", "interpretive_claim",
    "日神是远古残遗的信仰，在中国并没有发展成如同古希腊、埃及那样的人格神或国家主神，因此造型纹饰也停留在象形阶段，未有更为深化的表现。",
    "Sun worship was a surviving archaic belief; in China it did not develop into the personal or state deity found in ancient Greece and Egypt, so its forms and motifs remained at a pictographic stage without further elaboration.",
    [T + "qingtongqi.md", T + "xianqin-sandai.md"],
    "断言语义取 L646。原文以圆涡纹、涡纹、火纹为日神表现；claim 保留跨文明比较与“因此”的因果推断。",
    646, 646, [646], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1119", "cand-02-159", "interpretive_claim",
    "狩猎—采集者并不缺乏食物；他们制造石器并不是直接用于狩猎、挖掘或处理食物，而是出于加工木器工具的需要。",
    "Hunter-gatherers did not lack food; they made stone tools not directly for hunting, digging or processing food but for working wooden tools.",
    [T + "shiyingxing-sheji.md", T + "paleolithic-period.md"],
    "断言语义取 L470-L474。原文以卡拉哈里布须曼人、哈德扎人每周获取食物12至19小时为证；claim 保留“并不是直接用于”的排除式表述。",
    470, 474, [470, 474], "二、适应性：环境、创造、进化"))

rows.append(C(
    "claim-1120", "cand-02-160", "interpretive_claim",
    "造物功能最初是合一的，之后逐渐分离，但合是原始造物的主导；功能的分与合的过程正是造物设计对环境的适应过程，这是理解中国造物历史现象的一个关键。",
    "Artifact functions were initially unified and later gradually separated, but unity dominated primitive making; this process of separation and reunion is precisely design's adaptation to its environment and a key to understanding Chinese artifact history.",
    [T + "shiyingxing-sheji.md", T + "li-cauldron.md"],
    "断言语义取 L506。原文以功能分合解释造物更迭；claim 保留“合是主导”的判断，不把分离视为单向进步。",
    506, 506, [506], "二、适应性：环境、创造、进化"))

rows.append(C(
    "claim-1121", "cand-02-161", "evaluative_claim",
    "造物的多样性，标志着中国设计开始进入了第一个全面繁荣的时代。",
    "The diversity of artifacts marks the beginning of the first era of all-round prosperity in Chinese design.",
    [T + "xinshiqi-shiqi-leixing.md", T + "xinshiqi-shidai.md"],
    "断言语义取 L512。原文以石器家族、玉器、骨器、织物、漆器、青铜器等类型说明多样性；claim 保留“第一个全面繁荣”的分期评价。",
    512, 512, [512], "三、原始设计：多样性与统一性"))

rows.append(C(
    "claim-1122", "cand-02-162", "interpretive_claim",
    "石器以来的每一件设计造型都被置于一个几何化的序列之中，彼此之间组成有机的关联，从而构成多样性与统一性、共同性与独特性的辩证统一。",
    "Every design form since the Stone Age is placed within a geometric sequence and organically related to the others, constituting a dialectical unity of diversity and unity, commonality and distinctiveness.",
    [T + "yuanzaoxing.md", T + "xinshiqi-shiqi-leixing.md"],
    "断言语义取 L529。原文以圆形、对称、均衡说明序列；claim 保留“每一件”的全称表述与辩证统一判断。",
    529, 529, [529], "三、原始设计：多样性与统一性"))

rows.append(C(
    "claim-1123", "cand-02-163", "interpretive_claim",
    "造物的多样性往往带有思维观念、工艺技术与精神文化成熟的背景；设计历史越往后演进，就越显示出这一背景的重要作用。",
    "The diversity of artifacts usually presupposes mature thought, craft technique and spiritual culture; the later design history develops, the more important this background proves to be.",
    [T + "sheji.md", T + "yishu-shejishi.md"],
    "断言语义取 L582。原文以此回应多样性成因问题；claim 保留“往往”“越……越……”的程度与递进关系。",
    582, 582, [582], "三、原始设计：多样性与统一性"))

rows.append(C(
    "claim-1124", "cand-02-164", "interpretive_claim",
    "将天圆地方、四方神祇及社会伦理掺和进设计之中，是早期设计世界的普遍现象，反映了这一时期造物设计由日常生活用器进一步转化为礼器和设计主体人的思维观念的发展状况。",
    "Blending round heaven and square earth, deities of the four directions and social ethics into design was a general phenomenon of the early design world; it reflects both the transformation of daily vessels into ritual vessels and the development of the designer's thought.",
    [T + "yinyang-wuxing.md", T + "cong.md", T + "qingtong-liqi.md"],
    "断言语义取 L593。原文以良渚玉琮内圆外方及《周礼》苍璧黄琮为证；claim 保留“普遍现象”的总判断。",
    593, 593, [593], "四、早期设计世界：思维、功能、工艺、宗教"))

rows.append(C(
    "claim-1125", "cand-02-165", "interpretive_claim",
    "规范化是设计的一个重要原则；造物设计通过规范、标准的制定和贯彻，来规划、组织、安排、管理、监督和检测，以确保其产品生产的速度、质量和实效。",
    "Standardization is an important principle of design; through formulating and implementing norms and standards, making plans, organizes, arranges, manages, supervises and inspects production in order to secure speed, quality and effectiveness.",
    [T + "guifanhua.md", T + "sheji.md"],
    "断言语义取 L743。原文以周代设官、战国制度化、秦汉完善为历史线索；claim 只取规范化的定义性判断。",
    743, 743, [743], "六、从规范化的完善看造物体系的形成"))

rows.append(C(
    "claim-1126", "cand-02-166", "interpretive_claim",
    "“审曲面势”是先秦造物设计的主要思想，揭示了中国造物工艺的一个规律，即从观察物质材料的特性开始，物质特性决定制作工艺和设计方法。",
    "Observing materials and assessing circumstances was the main idea of pre-Qin design; it reveals a rule of Chinese craft: begin from observing material properties, which then determine technique and design method.",
    [T + "shenqu-mianshi.md", T + "tianshi-diqi-caimei-gongqiao.md", T + "baigong.md"],
    "断言语义取 L678。原文引《考工记》“审曲面势，以饬五材，以辨民器，谓之百工”；claim 保留“主要思想”与“规律”的判断。",
    678, 678, [678], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1127", "cand-02-167", "interpretive_claim",
    "孔子以“饰”为“道”的装饰与工具，“礼自外作，故文”，饰是礼的一部分；其“文质彬彬”“绘事后素”主张质先于文、文质谐和。",
    "Confucius treated ornament as the decoration and instrument of the Way; ritual takes outward form, hence ornament, and ornament is part of ritual; his ideals of graceful balance and painting after the plain ground hold that substance precedes ornament and the two are harmonized.",
    [T + "wenzhi-tongyi.md", T + "wenzhi.md", T + "li-yue-zhidu.md"],
    "断言语义取 L725-L727。原文分述“立于礼，成于乐”“博学于文，约之于礼”与“文质彬彬”“绘事后素”；claim 合并其饰道论与文质论。",
    725, 727, [725, 727], "五、轴心时代的造物思想"))

rows.append(C(
    "claim-1128", "cand-02-168", "interpretive_claim",
    "墨子提出“为乐非也”，主张“利人乎即为，不利人乎即止”，以实用主义立场反对奢侈文饰；其“用财少而为利多”的造物原则与功能第一相通。",
    "Mozi declared that making music is wrong and held that what benefits people should be done while what harms them should stop; from a pragmatic standpoint he opposed luxurious ornament, and his principle of little expense for great benefit converges with function-first design.",
    [T + "jiuliu-shijia.md", T + "wenzhi.md"],
    "断言语义取 L729。与 claim-1102 同段：本条概述墨子主张，claim-1102 评价其与现代主义相通，论题不同，未合并。",
    729, 729, [729], "五、轴心时代的造物思想"))

out = ROOT / "_ll_ll2a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
types = Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({x for r in rows for x in r["supported_by"]})
print("rows", len(rows), "types", dict(types), "links", links, "distinct", distinct)
print("wrote", out)
