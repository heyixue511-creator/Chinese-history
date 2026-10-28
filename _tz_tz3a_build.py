# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz3a (ch.3 end + ch.4-5.6, 43 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "第三章末、春秋战国与秦汉（东周至汉代工艺美术）"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"
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
    "claim-0841", "cand-05-56", "interpretive_claim",
    "周代玉器是伦理道德与等级名位的标志，是统治者尊贵的特殊工艺品，带有浓厚的封建伦理观念。",
    "Zhou jades served as markers of ethical conduct and rank; they were precious status objects for rulers and carried a strong feudal ethical charge.",
    [T + "zhou-yu-liqi.md", T + "li-yue-zhidu.md", T + "gui.md"],
    "断言语义取 L1662，为第三章第六节玉器的总判断。玉器种类与用途见 L1603-L1625，本 claim 只取总论，不重复器类细节。与 claim-0842 礼治总论相邻，未合并。",
    1662, 1662, [1662], "第三章 第六节 玉器"))

rows.append(C(
    "claim-0842", "cand-05-57", "interpretive_claim",
    "礼的特点是等级和秩序，它反映在周代各个方面；从工艺美术看，青铜器制作与玉器使用都体现等级差别、适应礼治需要，因此器物式样常有固定规格，装饰上表现出显著的秩序感。",
    "Ritual is characterised by hierarchy and order and pervades Zhou society; bronzes and jades alike expressed rank and served ritual governance, so vessel forms were standardised and decoration showed a marked sense of order.",
    [T + "li-yue-zhidu.md", T + "qingtong-liqi.md", T + "zhou-yu-liqi.md", T + "lieding-system.md"],
    "断言语义取 L1672，为第三章结语以德与礼治对照商代宗教迷信与尚武的总论。与 claim-0841 玉器总判断相邻，分论礼制与玉器，未合并。",
    1672, 1672, [1672], "第三章 第七节 结语"))

rows.append(C(
    "claim-0843", "cand-05-58", "interpretive_claim",
    "春秋战国青铜器以钟鸣鼎食为组合，已失去祭祀和礼器的特性，向生活日用器物发展，增加了许多以实用为主的用品。",
    "In the Spring and Autumn and Warring States periods bronzes formed bell-and-ding sets for daily life; they lost their sacrificial and ritual character and moved toward domestic utensils with many practical wares added.",
    [T + "qingtong-liqi.md", T + "chunqiu-zhanguo-qingtong-chuishiqi.md"],
    "断言语义取 L1692，与同段商代酒器组合、周代食器组合作三段对照。钟鸣鼎食为作者概括，未给器物组合统计。",
    1692, 1692, [1692], "第四章 第二节 青铜工艺"))

rows.append(C(
    "claim-0844", "cand-05-59", "evaluative_claim",
    "从艺术风格看，春秋时期青铜器装饰比较疏简，战国时期则趋于繁缛。",
    "Stylistically, Spring and Autumn bronze decoration is relatively sparse and simple, while Warring States decoration tends toward density and elaboration.",
    [T + "chunqiu-zhanguo.md", T + "panchi-wen.md", T + "chunqiu-zhanguo-qingtong-chuishiqi.md"],
    "断言语义取 L1694，为风格分期的评价性判断；疏简与繁缛的具体标尺未给。与 claim-0845 装饰格式演变同段，分论风格与格式，未合并。",
    1694, 1694, [1694], "第四章 第二节 青铜工艺"))

rows.append(C(
    "claim-0845", "cand-05-60", "synthetic_claim",
    "青铜器装饰格式的演变是：商代以单独纹样为主并运用中轴对称，周代进而为左右连续反复的二方连续纹样，春秋战国则构成上下左右连续的四方连续纹样。",
    "The decorative layout of bronzes developed from Shang single motifs with axial symmetry, to Zhou two-direction repeat bands, and then to Spring and Autumn and Warring States four-direction continuous patterns.",
    [T + "taotie-motif.md", T + "panchi-wen.md", T + "chunqiu-zhanguo-qingtong-chuishiqi.md"],
    "断言语义取 L1782，为装饰格式的三段归纳；与 L1818 青铜器艺术特点比较表互相印证。模印工艺与格式变化的关系见 claim-0846 前后文。",
    1782, 1782, [1782], "第四章 第二节 二、青铜器的装饰"))

rows.append(C(
    "claim-0846", "cand-05-61", "factual_claim",
    "战国时期冶铁已大量应用，我国冶铁工业比欧洲早一千六百多年。",
    "Iron smelting was already widely applied in the Warring States period, and China's iron industry preceded Europe's by more than 1,600 years.",
    [T + "tieqi-shidai.md", PR + "ye-tie-shu-qi-yuan.md"],
    "断言语义取 L1684，为冶铁应用与年代优先的事实性判断。早一千六百多年的比较未注具体标本与测年依据，属作者所据 20 世纪技术史表述。",
    1684, 1684, [1684], "第四章 第一节 概说"))

rows.append(C(
    "claim-0847", "cand-05-62", "factual_claim",
    "失蜡法的记载最早见于《唐会要》《洞天清录集》等古籍。",
    "The earliest textual records of lost-wax casting are found in the Tang Huiyao and the Dongtian Qinglu Ji.",
    [PR + "lost-wax-casting.md", W + "zenghouyi-zunpan.md"],
    "断言语义取 L1812，为文献著录的事实性判断。古籍成书年代与失蜡法实际使用年代不同，出土实物早于文献记载，见 claim-0848。",
    1812, 1812, [1812], "第四章 第二节 三、青铜器的加工"))

rows.append(C(
    "claim-0848", "cand-05-63", "factual_claim",
    "1979 年河南淅川下寺春秋墓出土的铜禁和铜盏，其盖纽及腿足采用失蜡法制作，是目前发现最早的失蜡法制件，把失蜡法历史向前提早了一百多年。",
    "The bronze jin and zhan from the 1979 Xiasi tomb at Xichuan, Henan, have lost-wax cast lid knobs and legs; they are the earliest known lost-wax castings and push the technique's history back more than a century.",
    [PR + "lost-wax-casting.md", W + "zenghouyi-zunpan.md"],
    "断言语义取 L1814，与同段 1977 年曾侯乙尊盘的失蜡法装饰并列。淅川下寺墓在库内无独立 place 条目，未强链。",
    1814, 1814, [1814], "第四章 第二节 三、青铜器的加工"))

rows.append(C(
    "claim-0849", "cand-05-64", "factual_claim",
    "1976 年河南安阳殷墟妇好墓出土几面早期铜镜，把过去认为铜镜产生于战国或春秋时期的历史推前了几百年，是目前所见最早的铜镜。",
    "Several early bronze mirrors from the 1976 Fu Hao tomb at Yinxu push the accepted origin of Chinese bronze mirrors back several centuries from the Warring States or Spring and Autumn period; they are the earliest mirrors known at the time of writing.",
    [T + "tongjing.md", P + "fuhao-tomb.md"],
    "断言语义取 L1832。妇好墓铜器另有 L905 的 468 件与 1625 公斤统计，属另一 claim 的语境，未合并。此后更早铜镜仍有发现，原文为 20 世纪表述。",
    1832, 1832, [1832], "第四章 第二节 四、铜镜、带钩和铜剑"))

rows.append(C(
    "claim-0850", "cand-05-65", "synthetic_claim",
    "战国铜镜可归纳为四个特点：薄胎、卷边、川字纽（弦纹纽）、双层纹。",
    "Warring States bronze mirrors show four traits: a thin body, a rolled rim, a chuan-shaped or bow-string knob, and two-layer decoration with a main motif over a ground pattern.",
    [T + "tongjing.md"],
    "断言语义取 L1836，为四特点的归纳。汉代与唐代铜镜的厚重、圆乳钉纽作为对照见同段，未展开。",
    1836, 1836, [1836], "第四章 第二节 四、铜镜、带钩和铜剑"))

rows.append(C(
    "claim-0851", "cand-05-66", "factual_claim",
    "山字纹是战国时期具有特色的铜镜花纹，数量最多，几达楚镜出土数的百分之八十。",
    "The mountain-character motif is a distinctive Warring States mirror pattern and is the most numerous, amounting to nearly 80 percent of mirrors excavated from Chu tombs.",
    [T + "tongjing.md", T + "panchi-wen.md"],
    "断言语义取 L1847，为数量占比的事实性判断。百分之八十为作者估值，未注统计样本与楚墓范围。",
    1847, 1847, [1847], "第四章 第二节 四、铜镜、带钩和铜剑"))

rows.append(C(
    "claim-0852", "cand-05-67", "factual_claim",
    "据现有材料，带钩约始于春秋初期，广泛流行于战国，直到西汉。",
    "On present evidence belt hooks begin around the early Spring and Autumn period, became widespread in the Warring States period, and continued in use into the Western Han.",
    [T + "belt-hook.md", W + "diaojin-xiangyu-yin-daigou.md"],
    "断言语义取 L1869，为带钩起始与流行年代的事实性判断。同段并列饰件钩、武器钩、衣襟钩的用法区分。",
    1869, 1869, [1869], "第四章 第二节 四、铜镜、带钩和铜剑"))

rows.append(C(
    "claim-0853", "cand-05-68", "factual_claim",
    "春秋战国铜剑表面已采用镀铬工艺，以防青铜氧化腐蚀，因此出土铜剑经长期埋藏仍光泽闪烁、锋利如新。",
    "Spring and Autumn and Warring States bronze swords were chrome-plated to prevent oxidation, so excavated examples still shine and remain sharp after long burial.",
    [T + "jian-sword.md"],
    "断言语义取 L1877，为铜剑表面处理的事实性判断。镀铬说为 20 世纪检测结论，原文未注检测报告与样本。",
    1877, 1877, [1877], "第四章 第二节 四、铜镜、带钩和铜剑"))

rows.append(C(
    "claim-0854", "cand-05-69", "factual_claim",
    "彩陶是在陶胎上画花后再烧制，彩绘陶是在烧成的陶坯上画花，因而花纹易于脱落；彩绘陶始于春秋，到战国得到发展，一直延续到两汉。",
    "Painted pottery (caihui) was decorated before firing, whereas painted-after-firing pottery (caihui tao) was painted on fired bodies and its decoration easily flakes; the latter began in the Spring and Autumn period, developed in the Warring States period, and continued into the Han.",
    [T + "caihui-tao.md", T + "taoqi-qixing.md"],
    "断言语义取 L1897，为彩陶与彩绘陶的工艺区别及年代判断。名称加绘字以区别彩陶，见同段。",
    1897, 1897, [1897], "第四章 第三节 二、彩绘陶"))

rows.append(C(
    "claim-0855", "cand-05-70", "interpretive_claim",
    "彩绘陶主要用作明器，战国两汉厚葬之风盛行是彩绘陶兴盛的主要原因。",
    "Painted-after-firing pottery was mainly made as mingqi burial goods; the prevalence of lavish burial in the Warring States and Han periods was the main reason for its flourishing.",
    [T + "caihui-tao.md", T + "mingqi.md"],
    "断言语义取 L1899，为用途与兴盛原因的因果判断。分布地区见同段，未给墓葬数量与随葬组合统计。",
    1899, 1899, [1899], "第四章 第三节 二、彩绘陶"))

rows.append(C(
    "claim-0856", "cand-05-71", "factual_claim",
    "春秋战国时期最著名的是齐鲁地区，齐纨、鲁缟已全国闻名，齐国染织生产量最大，有冠带衣履天下的比喻。",
    "The most famous textile region of the Spring and Autumn and Warring States periods was Qi-Lu: Qi silk and Lu gauze were known nationwide, Qi produced the largest volume, and contemporary rhetoric described it as clothing the whole world.",
    [T + "qiwan-lugao.md", T + "qi-silk.md", T + "shangzhou-sizhiwu.md"],
    "断言语义取 L1954，为齐鲁染织地位的事实性判断。九州产布帛的文献分列见 L1936-L1952，未并入本 claim。",
    1954, 1954, [1954], "第四章 第四节 染织工艺"))

rows.append(C(
    "claim-0857", "cand-05-72", "historiographic_claim",
    "1982 年湖北江陵马山砖厂一号墓出土大批战国丝织品，是我国继长沙马王堆汉墓以后在丝织品方面的又一重大发现，其品种和数量超过此前多次发现的战国丝织品。",
    "The large Warring States silk assemblage from 1982 at Mashan Brick Factory Tomb No. 1, Jiangling, Hubei, was another major textile discovery after Mawangdui and exceeded earlier Warring States finds in variety and quantity.",
    [E + "mashan-yihao-mu-sichupin.md", P + "jiangling-mashan-yihao-chumu.md", T + "zhijin.md", PR + "han-dai-zhijin-cixiu.md"],
    "断言语义取 L1962，为发现意义的研究史判断。马王堆为西汉墓，原文以之作为比较基准，未注两批织物的具体统计。",
    1962, 1962, [1962], "第四章 第四节 染织工艺"))

rows.append(C(
    "claim-0858", "cand-05-73", "factual_claim",
    "战国时期舞蹈人图案在织锦上出现尚属首见，舞人高举双袖、束带飘动，是当时流行的纹样题材。",
    "Dancer figures appear for the first time on Warring States brocade; with raised sleeves and floating sashes they were a fashionable motif of the period.",
    [W + "wudao-renwu-dongwu-wen-sanse-jin.md", T + "zhijin.md"],
    "断言语义取 L1966，为纹样题材首次出现的事实性判断。舞人动物纹锦的构图与色彩见同段，未展开。",
    1966, 1966, [1966], "第四章 第四节 染织工艺"))

rows.append(C(
    "claim-0859", "cand-05-74", "interpretive_claim",
    "各种工艺品的兴衰除社会与生活原因外，工艺材料也具有决定因素；战国时期漆树大量种植、漆工艺兴起，一部分生活用品开始由漆器代替青铜器。",
    "Beyond social and practical causes, materials are a decisive factor in the rise and fall of crafts; in the Warring States period extensive lacquer cultivation and the rise of lacquer craft led some daily wares to be replaced by lacquer.",
    [PR + "xiu-qi.md", T + "qimu-jiaju.md", PR + "han-dai-qiqi-zhizuo-fengong.md"],
    "断言语义取 L1976-L1978，为材料替代的因果判断。漆器优点与楚地生产见同节，未并入。",
    1976, 1978, [1976], "第四章 第五节 漆器工艺"))

rows.append(C(
    "claim-0860", "cand-05-75", "factual_claim",
    "我国古代玻璃属铅钡玻璃，西方玻璃属钠钙玻璃；我国出土古代玻璃制品带有谷粒纹、柿蒂纹、云纹、蟠龙纹及汉字印章等传统装饰，说明我国古代已能自造玻璃。",
    "Ancient Chinese glass is lead-barium glass while Western glass is soda-lime glass; Chinese glass finds carry traditional motifs such as grain, persimmon-calyx, cloud and coiled-dragon patterns and seals with Chinese characters, showing that China made glass independently.",
    [T + "glass.md", T + "liuli.md"],
    "断言语义取 L2041，为成分体系与自制能力的事实性判断。同段以西方玻璃较早流传引出本土自制问题。",
    2041, 2041, [2041], "第四章 第六节 其他工艺"))

rows.append(C(
    "claim-0861", "cand-05-76", "interpretive_claim",
    "春秋战国青铜器缠绕穿插的装饰风格与《楚辞》回荡法的文学格式有异质同构之处，说明同时代不同艺术门类互相影响，并受时代社会思想与审美风尚支配。",
    "The interwoven decoration of Spring and Autumn and Warring States bronzes is structurally analogous to the echoing method of the Chu Ci, showing that contemporary arts influenced one another under shared social thought and taste.",
    [B + "chuci.md", T + "panchi-wen.md"],
    "断言语义取 L2059，为跨门类同构的阐释性判断。文学史评家语见同段，未注具体评论者。",
    2059, 2059, [2059], "第四章 第七节 结语"))

rows.append(C(
    "claim-0862", "cand-05-77", "interpretive_claim",
    "孔子主张文质兼备，认为质胜文则野、文胜质则史，即要求内容与形式统一，否则或流于粗俗，或流于浮夸。",
    "Confucius advocated the union of substance and refinement: substance without refinement is rustic, refinement without substance is pedantic; content and form should be unified.",
    [R + "confucius.md", B + "lunyu.md"],
    "断言语义取 L2063，为孔子工艺美学观的思想史阐释。同段并列墨子、老庄、孟子、荀子、韩非子，分条各建 claim。",
    2063, 2063, [2063], "第四章 第七节 结语"))

rows.append(C(
    "claim-0863", "cand-05-78", "interpretive_claim",
    "墨子主张先质而后文，以衣必常暖然后求丽、居必常安然后求乐说明实用第一性，并以功利作为美的评价基础，功利于人谓之巧、不利于人谓之拙。",
    "Mozi put substance before ornament, arguing that clothing must first warm and dwellings first shelter before beauty and pleasure matter; utility is the basis of aesthetic judgment, and what benefits people is skilful while what harms them is clumsy.",
    [R + "mozi.md", B + "mozi-jieyong.md"],
    "断言语义取 L2063，为墨子功利主义工艺观的思想史阐释。与 claim-0862 孔子条同段并列，分论两家，未合并。",
    2063, 2063, [2063], "第四章 第七节 结语"))

rows.append(C(
    "claim-0864", "cand-05-79", "interpretive_claim",
    "老庄的虚无观可理解为扩大的空间概念，与现代设计要求相通；埏埴以为器、凿户牖以为屋说明有之以为利、无之以为用，有无辩证关系丰富了设计思维。",
    "The Lao-Zhuang idea of nothingness can be read as an expanded concept of space relevant to modern design; the clay vessel and the windowed house show that being provides the advantage while non-being provides the use, enriching design thinking.",
    [R + "laozi.md", R + "zhuangzi.md", B + "zhuangzi.md"],
    "断言语义取 L2063，为老庄空间观的设计学阐释。原文以今天的话来说作跨时代类比，未给接受史证据。",
    2063, 2063, [2063], "第四章 第七节 结语"))

rows.append(C(
    "claim-0865", "cand-05-80", "historiographic_claim",
    "战国时期工艺专著《考工记》提出天有时、地有气、材有美、工有巧、合此四者然后可以为良的观点，是我国最早的关于工艺制作的专门论述。",
    "The Warring States craft treatise Kaogongji states that timely weather, suitable earth, fine materials and skilled workmanship must combine for a good product; it is China's earliest specialised discussion of craft production.",
    [B + "kaogongji.md", B + "kaogongji-tu.md"],
    "断言语义取 L2065，为《考工记》四原则及其文献地位的研究史判断。时、空、工、材的现代对应见同段，属作者引申。",
    2065, 2065, [2065], "第四章 第七节 结语"))

rows.append(C(
    "claim-0866", "cand-06-51", "interpretive_claim",
    "秦政府统一文字、货币、度量衡等集权措施反映在工艺生产上，形成统一性和巨大性的特点。",
    "Qin centralising measures such as standardising script, coinage and weights and measures were reflected in craft production, giving it the traits of uniformity and monumental scale.",
    [R + "qin-shi-huang.md", W + "qin-bing-ma-yong.md", W + "qin-shi-huang-ling.md"],
    "断言语义取 L2079，为政治制度与工艺特征关系的阐释。始皇陵陶俑的宏伟规模见同段，作为例证未展开。",
    2079, 2079, [2079], "第五章 第一节 概说"))

rows.append(C(
    "claim-0867", "cand-06-52", "synthetic_claim",
    "汉代手工业发展可分为三个时期：西汉初期为恢复期，西汉中期至东汉前期为迅速发展与繁荣期，东汉末期为衰落期。",
    "Han handicraft development falls into three phases: recovery in the early Western Han, rapid growth and prosperity from the mid-Western Han to the early Eastern Han, and decline in the late Eastern Han.",
    [T + "handai-guanzhi.md", I + "han-dai-guan-ying-sizhi-zuofang.md"],
    "断言语义取 L2085，为三期的归纳。采铜每年十万人以上等例证见同段，未注文献来源。",
    2085, 2085, [2085], "第五章 第一节 概说"))

rows.append(C(
    "claim-0868", "cand-06-53", "synthetic_claim",
    "汉代装饰题材大量反映现实生活，表现手法多采用平面的剪影式，同时注意把握物象的动态和典型特征，极富图案装饰味。",
    "Han decorative themes largely depict real life; the treatment is flat and silhouette-like, capturing movement and typical features, and is strongly ornamental.",
    [T + "huaxiangshi.md", T + "huaxiangzhuan.md", W + "yishe-shouhuo-huaxiangzhuan.md"],
    "断言语义取 L2089，为题材与手法的归纳。宴饮、舞乐、狩猎、攻战、耕种等题材见同段，未逐项建 claim。",
    2089, 2089, [2089], "第五章 第一节 概说"))

rows.append(C(
    "claim-0869", "cand-06-54", "factual_claim",
    "秦代早期有些器物是从其他国家转运来的：宝鸡西高泉村秦墓铜壶和铜豆原为周室器物，凤翔高庄秦墓中山鼎为中山国器物，泌阳官庄秦墓平安君鼎为卫国器物。",
    "Some early Qin vessels were transferred from other states: the bronze hu and dou from Xigaoquan, Baoji, were Zhou royal wares; the Zhongshan ding from Gaozhuang, Fengxiang, was a Zhongshan vessel; the Ping'an Jun ding from Guanzhuang, Biyang, was a Wey vessel.",
    [T + "qingtong-liqi.md", R + "qin-shi-huang.md"],
    "断言语义取 L2095，为秦墓器物来源的事实性判断。三例均属发掘简报信息，原文未注报告编号。",
    2095, 2095, [2095], "第五章 第二节 秦代的工艺美术"))

rows.append(C(
    "claim-0870", "cand-06-55", "factual_claim",
    "据《睡虎地秦简》记载，秦漆工到别县领漆要运到官府测试，可见当时制漆有严格的组织管理和统一的质量标准。",
    "According to the Shuihudi Qin bamboo slips, lacquer workers collecting raw lacquer in another county had it tested at the government office, showing strict organisation and uniform quality standards in Qin lacquer production.",
    [PR + "xiu-qi.md", W + "qiyu-yunmeng-shuihudi-33.md"],
    "断言语义取 L2104，为秦漆官营管理的事实性判断。云梦睡虎地秦墓漆器见同段，作为实物旁证。",
    2104, 2104, [2104], "第五章 第二节 秦代的工艺美术"))

rows.append(C(
    "claim-0871", "cand-06-56", "evaluative_claim",
    "秦代工艺美术重实用，富有敦厚质朴的艺术特色，器用造型洗练，一般只以几道弦纹为饰，反映出一种质朴的美。",
    "Qin craft is practical and marked by a plain, honest character; vessel forms are concise and usually decorated only with a few string lines, expressing a restrained beauty.",
    [W + "qin-bing-ma-yong.md", T + "taoqi-qixing.md"],
    "断言语义取 L2139，为秦代工艺风格的评价性判断。以吏治清明、民俗淳朴解释风格，属作者引申。",
    2139, 2139, [2139], "第五章 第二节 秦代的工艺美术"))

rows.append(C(
    "claim-0872", "cand-06-57", "factual_claim",
    "汉代铜器已向生活日用器皿发展，制作上不如商、周、战国多饰花纹，而以素器最为流行，或仅有简练弦纹，或仅饰铺首。",
    "Han bronzes shifted toward daily utensils; unlike Shang, Zhou and Warring States wares they were mostly plain, with only simple string lines or mask handles.",
    [T + "qingtong-liqi.md", T + "boshanlu.md"],
    "断言语义取 L2143，为汉铜器器形与装饰的事实性判断。鎏金、金银错等华贵做法见同段，未并入。",
    2143, 2143, [2143], "第五章 第三节 铜器工艺"))

rows.append(C(
    "claim-0873", "cand-06-58", "evaluative_claim",
    "汉代铜灯造型丰富多彩、灯体优美，既适应实用要求也符合科学原理，既可作灯又可作室内陈设，达到实用与美观的统一。",
    "Han bronze lamps are varied and elegant, meeting practical needs and scientific principles alike; they serve as lamps and as interior furnishings, uniting utility and beauty.",
    [W + "changxin-palace-lamp.md", W + "yanyu-tongdeng.md"],
    "断言语义取 L2207，为汉铜灯设计成就的评价性判断。虹管灯、盘灯、行灯等类型见 L2185-L2203，未逐类建 claim。",
    2207, 2207, [2207], "第五章 第三节 一、铜灯"))

rows.append(C(
    "claim-0874", "cand-06-59", "synthetic_claim",
    "汉代铜镜的特点是体薄、平边、圆纽、装饰程式化；其发展分三期：前期为西汉，中期为西汉末至王莽时期，后期为东汉。",
    "Han mirrors are thin-bodied with flat rims, round knobs and conventionalised decoration; they develop in three phases: Western Han, late Western Han to Wang Mang, and Eastern Han.",
    [T + "hanjing.md", T + "tongjing.md", T + "guijujing.md"],
    "断言语义取 L2253-L2255，为汉镜特点与三期的归纳。各期代表镜式见同节，未逐式建 claim。",
    2253, 2255, [2253], "第五章 第三节 六、铜镜"))

rows.append(C(
    "claim-0875", "cand-06-60", "factual_claim",
    "规矩镜上的 TLV 纹实际上是古代六博的棋格；山东费县曾出土石六博盘，长沙马王堆三号墓曾出土全套博具，其博局上有 TLV 规矩纹。",
    "The TLV pattern on Han rule mirrors is in fact the board layout of the ancient liubo game; a stone liubo board was found at Fei County, Shandong, and a complete liubo set with TLV markings in Mawangdui Tomb No. 3.",
    [T + "guijujing.md", T + "hanjing.md"],
    "断言语义取 L2263-L2268，为 TLV 来源的事实性判断。六博规则引《古博经》见同段，未展开。",
    2263, 2268, [2263], "第五章 第三节 六、铜镜"))

rows.append(C(
    "claim-0876", "cand-06-61", "interpretive_claim",
    "铜鼓原是一种打击乐器，以后逐渐演化为权力的象征。",
    "The bronze drum was originally a percussion instrument and gradually became a symbol of power.",
    [T + "tonggu.md"],
    "断言语义取 L2301，为铜鼓社会功能演变的阐释。白居易诗与西南民族使用见同段，未并入。",
    2301, 2301, [2301], "第五章 第三节 七、铜鼓"))

rows.append(C(
    "claim-0877", "cand-06-62", "factual_claim",
    "铅釉陶是汉代陶瓷工艺的一种创造，最早生产于关中地区。",
    "Lead-glazed pottery was an innovation of Han ceramic craft and was first produced in the Guanzhong region.",
    [T + "qian-you-tao.md", T + "mingqi.md", T + "proto-porcelain.md"],
    "断言语义取 L2355，为铅釉陶起源的事实性判断。南北釉陶软硬之别与铅釉成分见同节，未并入。",
    2355, 2355, [2355], "第五章 第五节 一、釉陶"))

rows.append(C(
    "claim-0878", "cand-06-63", "factual_claim",
    "汉代早期瓷器取得很大成就，特别是东汉中后期已进入完成阶段。",
    "Early Han porcelain scored major achievements, and by the middle to late Eastern Han it had reached maturity.",
    [T + "qing-ci.md", T + "proto-porcelain.md", W + "donghan-qingci-gaozu-wan.md"],
    "断言语义取 L2369，为汉代瓷器成熟阶段的事实性判断。上虞窑址、龙窑与 1300℃ 烧成见同段，未并入。",
    2369, 2369, [2369], "第五章 第五节 三、早期瓷器"))

rows.append(C(
    "claim-0879", "cand-06-64", "factual_claim",
    "浙江上虞帐子山瓷窑发现东汉黑瓷，把过去认为最早的黑瓷是东晋德清窑的看法向前提早了几百年。",
    "Black porcelain of the Eastern Han was found at the Zhangzishan kiln in Shangyu, Zhejiang, pushing back by several centuries the earlier view that the earliest black porcelain was made at the Eastern Jin Deqing kiln.",
    [T + "black-porcelain.md", T + "qing-ci.md"],
    "断言语义取 L2379，为黑瓷年代提前的事实性判断。1972 至 1977 年发掘见同段，未注报告。",
    2379, 2379, [2379], "第五章 第五节 三、早期瓷器"))

rows.append(C(
    "claim-0880", "cand-06-65", "factual_claim",
    "汉代把四神看作与辟邪求福有关，又用以表示季节和方位：青龙为东、春季，白虎为西、秋季，朱雀为南、夏季，玄武为北、冬季。",
    "Han people regarded the Four Divine Creatures as apotropaic and auspicious and also as markers of season and direction: Azure Dragon east and spring, White Tiger west and autumn, Vermilion Bird south and summer, Dark Warrior north and winter.",
    [T + "si-shen.md", T + "wadang.md", T + "hanjing.md"],
    "断言语义取 L2412，为四神方位与季节对应的事实性判断。四神瓦当的设计评价见同段，未并入。",
    2412, 2412, [2412], "第五章 第五节 四、砖瓦"))

rows.append(C(
    "claim-0881", "cand-06-66", "evaluative_claim",
    "汉代陶塑的艺术成就，在于表现各种物象的主要特征，形象生动简练，装饰性很强。",
    "The achievement of Han pottery sculpture lies in capturing the essential features of its subjects; the figures are lively and concise and strongly decorative.",
    [W + "shuochangyong.md", T + "mingqi.md"],
    "断言语义取 L2436，为汉陶塑艺术成就的评价性判断。说唱俑等实例见同段，未展开。",
    2436, 2436, [2436], "第五章 第五节 五、陶塑"))

rows.append(C(
    "claim-0882", "cand-06-67", "factual_claim",
    "汉代丝织品已成为国际经济文化交流的重要物品，形成了通向西域的著名丝绸之路。",
    "Han silk became an important medium of international economic and cultural exchange and gave rise to the famous Silk Road to the Western Regions.",
    [T + "sichou-zhilu.md", T + "zhijin.md", I + "han-dai-guan-ying-sizhi-zuofang.md"],
    "断言语义取 L2458，为丝织品外传与丝路形成的事实性判断。赐匈奴缯帛与各地出土汉锦见同段，未并入。",
    2458, 2458, [2458], "第五章 第六节 染织工艺"))

rows.append(C(
    "claim-0883", "cand-06-68", "evaluative_claim",
    "汉代铜镜花纹丰富多彩，纹饰复杂、图案组织多样，纹样变化简约而富于程式化，是学习古代适合纹样的一份珍贵资料。",
    "Han mirror decoration is rich and varied, with complex ornament and diverse pattern organisations; its simplified, conventionalised motifs make it a valuable resource for studying traditional fit-to-shape patterns.",
    [T + "hanjing.md", T + "tongjing.md", T + "guijujing.md"],
    "断言语义取 L2295-L2296，为汉镜装饰价值的评价性判断，属第五章第三节铜镜的总结。六种图案组织见 L2293，未并入。",
    2295, 2296, [2295], "第五章 第三节 六、铜镜"))

out = ROOT / "_tz_tz3a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
types = Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({x for r in rows for x in r["supported_by"]})
print("rows", len(rows), "types", dict(types), "links", links, "distinct", distinct)
print("span kinds", Counter(r["source"]["source_span"]["span_kind"] for r in rows))
print("written", out)
