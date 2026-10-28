# -*- coding: utf-8 -*-
"""Build 李立新 2011 claim rows, batch ll3a (第一章末段至第三章开篇, 37 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
SRC = "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"
DATE = "2026-10-27"
CH = "第一章末段、第二章与第三章开篇（官营制度定型、意匠化与政教功利、传统外来时尚、佛教渗透、风格论、唐宋风格转变、院画扩张与意匠化衰落、天工开物与早期工业化）"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/persons/"
B = "04-knowledge/units/publications/"

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
    "claim-1129", "cand-03-84", "interpretive_claim",
    "汉代官府为组织大规模生产，常从各地征调有经验的工匠，促使地域性设计相互交流并在规范上逐步统一；官营制度与民间规范由此形成互相促进的关系。",
    "To organize large-scale production, Han government offices often requisitioned experienced craftsmen from across the realm, prompting exchanges among regional designs and gradual standardization; official workshops and folk norms thus reinforced each other.",
    [T + "guanying-shougongye.md", T + "handai-guanzhi.md", T + "guifanhua.md"],
    "断言语义取 L829。原文同时指出官营整合并未取消“因地制宜”，故 claim 保留统一与地方差异并存的限定。",
    829, 829, [829], "3. 官营制度的定型与地域设计的聚集"))

rows.append(C(
    "claim-1130", "cand-03-85", "interpretive_claim",
    "汉代设计纹饰虽发生显著变革和意义更替，但其设计形式仍与三代乃至上古的意匠化方式保持前后连贯与传承。",
    "Although Han decorative motifs underwent substantial change and semantic replacement, their design forms remained continuous with the craft-conscious manner of the Three Dynasties and even earlier antiquity.",
    [T + "wenzhi.md", T + "yunqi-wen.md", T + "huaxiangshi.md"],
    "断言语义取 L833。L835 以云气纹的格律化说明形式延续；claim 保留“变革而不断裂”的总体判断，不把纹饰意义更替等同于形式传统中断。",
    833, 833, [833], "4. 设计意匠化与政教功利"))

rows.append(C(
    "claim-1131", "cand-03-86", "interpretive_claim",
    "汉代画像石、画像砖、织物和漆器中的神话人物与珍禽异兽纹样具有政教功能；“恶以戒世，善以示后”的理性实用功利成为评价造物的标准，使汉代物质文化带有明显儒学印记。",
    "Mythological figures and rare animals in Han reliefs, bricks, textiles and lacquerware served moral-political functions; the rational utilitarianism of rewarding good and warning against evil became a standard for judging artifacts, leaving a clear Confucian imprint on Han material culture.",
    [T + "li-yue-zhidu.md", T + "huaxiangshi.md", T + "jixiang-tu-an.md"],
    "断言语义取 L840。原文以《鲁灵光殿赋》“恶以戒世，善以示后”说明纹样的伦理教化功能；claim 限于汉代装饰的意义结构，不推断所有纹样均出自儒学。",
    840, 840, [840], "4. 设计意匠化与政教功利"))

rows.append(C(
    "claim-1132", "cand-03-87", "evaluative_claim",
    "以现代标准化理论的科学性、政策性、技术性、经济性和法制性衡量，两汉设计规范已具备这些特点，形成独特体系并为后世造物提供楷模。",
    "Measured by the scientific, policy, technical, economic and legal dimensions of modern standardization theory, Han design norms already possessed these features, forming a distinctive system and a model for later artifact making.",
    [T + "guifanhua.md", T + "handai-guanzhi.md", T + "guanying-shougongye.md"],
    "断言语义取 L845。这是作者以现代标准化框架作出的评价性判断，原文以“我们看到”表述；claim 保留其评价立场，不把它写成普遍共识。",
    845, 845, [845], "4. 设计意匠化与政教功利"))

rows.append(C(
    "claim-1133", "cand-03-88", "synthetic_claim",
    "以宋为界，两千年中国设计史可划分为前后两个高峰期与两种新局面：前段由三代至唐宋，后段由元明清再呈高峰。",
    "With the Song as the dividing line, two millennia of Chinese design history can be divided into two peak periods and two new configurations: the earlier span from the Three Dynasties through Tang-Song, and the later span from Yuan-Ming-Qing onward.",
    [T + "feng-ge-maniera.md", T + "yishu-shejishi.md", T + "songdai-yaoxi.md"],
    "断言语义取 L851-L853。原文先以“大一统”历史观说明体系长期延续，再以动态历史过程提出二分；claim 保留分期框架，不把“高峰”具体化为某一朝代。",
    851, 853, [851, 853], "第二章 开放融合与风格转变（导论）"))

rows.append(C(
    "claim-1134", "cand-03-89", "synthetic_claim",
    "宋代商品经济发展与市民文化兴起，使造物设计明显转向民间和日用；理学家的复古主张对造物设计没有实质性影响。",
    "The growth of a commodity economy and urban culture in the Song turned design markedly toward folk and everyday uses; the antiquarian proposals of Neo-Confucians had no substantive effect on design.",
    [T + "shi-class.md", T + "lixue.md", T + "riyongpin-meishuhua-gongyipin-shiyonghua.md"],
    "断言语义取 L855。原文将“转向民间、转向日用”与“复古主张无实质影响”并置；claim 保留这两个判断，不引申为理学与造物完全无关。",
    855, 855, [855], "第二章 开放融合与风格转变（导论）"))

rows.append(C(
    "claim-1135", "cand-03-90", "interpretive_claim",
    "宋代工笔绘画直接进入刺绣、陶瓷等设计领域，使造物以表现绘画为目的，汉代以来中国造物的意匠化设计至宋代告一段落。",
    "In the Song, fine-brush painting entered embroidery and ceramics directly, making the depiction of painting a goal of artifact making; the craft-conscious design tradition dating from the Han came to an end in the Song.",
    [T + "song-ci-zhuangshi-shoufa.md", T + "kesi.md", T + "gongyi-meishu.md"],
    "断言语义取 L857。原文限定“虽然只限于刺绣、陶瓷等领域”；claim 保留领域限制，不把绘画化扩展为宋代全部造物。",
    857, 857, [857], "第二章 开放融合与风格转变（导论）"))

rows.append(C(
    "claim-1136", "cand-03-91", "interpretive_claim",
    "牛车、鹿车、指南车、记里鼓车及霹雳车、磨车均依据秦汉旧有制车规范改制，其结构安排体现设计创造力，反映传统造物从内部孕育的再生活力。",
    "Ox carts, wheelbarrows, south-pointing chariots, distance-recording drums, and the contemporary thunderbolt and mill carts were all modified from Qin-Han cart norms; their structural arrangements show design creativity and the regenerative vitality of tradition working from within.",
    [T + "niu-che.md", T + "zhinan-che.md", T + "jili-guche.md", T + "dulunche.md", T + "guifanhua.md"],
    "断言语义取 L892-L897。原文强调“依据秦汉旧有的制车规范形制改制”，故 claim 把它定位为规范内部的革新，而非外来技术移植。",
    892, 897, [892, 897], "一、传统、外来、时尚"))

rows.append(C(
    "claim-1137", "cand-03-92", "interpretive_claim",
    "青瓷器的成熟表明先民在胎料选择、窑炉设计和烧成技术上长期积累进步，是造物从内部孕育新品的典型例证。",
    "The maturity of celadon shows cumulative progress in clay selection, kiln design and firing technology; it is a typical case of a new product gestated from within the craft tradition.",
    [T + "qing-ci.md", T + "proto-porcelain.md", T + "tang-dai-qingci-yao.md"],
    "断言语义取 L902。原文以越窑、瓯窑、婺州窑、德清窑等南北体系说明青瓷成熟；claim 只保留“内部孕育”的机制判断，不评价具体窑口优劣。",
    902, 902, [902], "一、传统、外来、时尚"))

rows.append(C(
    "claim-1138", "cand-03-93", "historiographic_claim",
    "设计史呈多线错综：内在机制决定推进进度，外在历史条件的变动又造成大跨度进退，因此设计史并非单轨向前。",
    "Design history is multilinear and tangled: internal mechanisms set the pace of advance, while shifts in external historical conditions cause wide swings forward or backward; design history therefore does not move on a single track.",
    [T + "yishu-shejishi.md", T + "chuantong-sheji.md"],
    "断言语义取 L907-L909。这是作者的方法论判断；claim 保留“多线”与“非单轨”，不据此否认具体时期的整体趋势。",
    907, 909, [907, 909], "一、传统、外来、时尚"))

rows.append(C(
    "claim-1139", "cand-03-94", "synthetic_claim",
    "佛教区别于其他宗教的一个特点是利用造型形象传播教义；佛教艺术品在中国的发现标志佛教传入，传入后以独特传播方式在短期内对各地区造物设计产生广泛影响。",
    "A distinctive feature of Buddhism is its use of visual forms to spread doctrine; the discovery of Buddhist artworks marks its entry into China, after which it rapidly and widely affected artifact design across regions.",
    [T + "shikusi.md", T + "fota.md", T + "huaxiangshi.md"],
    "断言语义取 L916。原文列举尼雅腊缬棉布、沂南画像石墓佛像、孔望山摩崖造像等；claim 保留“标志传入”和“广泛影响”，不把单件器物当作教义传播的全部证据。",
    916, 916, [916], "一、传统、外来、时尚"))

rows.append(C(
    "claim-1140", "cand-03-95", "synthetic_claim",
    "传统、外来与时尚三者合力构成魏晋南北朝造物设计的图像背景，孕育出清秀的造物形式和新格局；该时期是佛教与造物艺术相结合的初生期。",
    "Tradition, foreign influence and fashion together formed the visual background of Six Dynasties design and produced a refined artifact idiom and new configuration; the period was the nascent stage of Buddhist-artifact integration.",
    [T + "liuchao-gongjiang-zhidu.md", T + "lianhua-wen.md", T + "rendong-wen.md", T + "liuchao-tongjing.md"],
    "断言语义取 L942。原文把汉制内部变革、佛教传入与南北文化碰撞、社会时尚并列为合力；claim 保留三重条件，不把清秀风格归因于单一外来影响。",
    942, 942, [942], "一、传统、外来、时尚"))

rows.append(C(
    "claim-1141", "cand-03-96", "factual_claim",
    "据杨泓研究，魏晋南北朝时期佛教艺术造型在江南主要用作装饰器物的图纹，并未被尊为礼拜的圣像。",
    "According to Yang Hong, Buddhist figural art in the Jiangnan region during the Six Dynasties was mainly used as decorative motifs on utensils and was not yet venerated as icons for worship.",
    [P + "yang-hong.md", T + "hunping.md", T + "liuchao-tongjing.md"],
    "候选原标 source_claim，按证据层规范映射为 factual_claim；该判断转述杨泓研究，claim 保留“据研究”的归属，不把它写成考古定论。",
    960, 960, [960], "二、佛教的渗透及其设计史意义"))

rows.append(C(
    "claim-1142", "cand-03-97", "historiographic_claim",
    "佛教自东汉传入后借助造物设计进行佛事活动，使一部分中国造物佛教化；中国造物对佛教器物的融会改造又使佛教造物中国化，这一双向过程几乎改变了汉代以后中国造物设计史的进程。",
    "After entering China in the Eastern Han, Buddhism used artifact design for religious practice, Buddhistizing part of Chinese material culture; Chinese artifact making in turn absorbed and transformed Buddhist implements, Sinicizing Buddhist design. This two-way process almost changed the course of Chinese design history after the Han.",
    [T + "fota.md", T + "shikusi.md", T + "man-tuo-luo.md"],
    "断言语义取 L1005。原文以法器、供具、寺院造物等说明双向过程；claim 保留“几乎改变进程”的强判断及其作者立场。",
    1005, 1005, [1005], "二、佛教的渗透及其设计史意义"))

rows.append(C(
    "claim-1143", "cand-03-98", "interpretive_claim",
    "佛教渗入造物不仅表现于纹饰造型，还影响造物观念与器物评判：建筑借象征营造崇高感，绘画产生阴影晕染与连环图式，禅宗语汇则催生“类玉类冰”“类雪类银”的器物品质标准。",
    "Buddhist influence on artifacts was not limited to decorative form but reached design concepts and evaluation: architecture used symbolism for sublimity, painting developed shading and continuous narrative schemes, and Chan vocabulary gave rise to connoisseurship standards such as jade-like or ice-like, snow-like or silver-like ware.",
    [T + "mise-porcelain.md", T + "qing-ci.md", T + "jingbian.md", T + "man-tuo-luo.md"],
    "断言语义取 L1007-L1009。原文将建筑象征、晕染、连环图式与禅宗评价标准并置；claim 保留这些不同层面的影响，不把“类玉类冰”直接归于佛教教义。",
    1007, 1009, [1007, 1009], "二、佛教的渗透及其设计史意义"))

rows.append(C(
    "claim-1144", "cand-03-99", "synthetic_claim",
    "几千年来中国造物艺术在交流、吸收、融化、变异与创新中发展，同时始终保持民族造物特征。",
    "For millennia Chinese artifact art has developed through exchange, absorption, assimilation, variation and innovation while always retaining its national characteristics.",
    [T + "chuantong-sheji.md", T + "sichou-zhilu.md", T + "liuli.md"],
    "断言语义取 L1020。原文以丝绸之路佛教艺术、萨珊金银器与玻璃器、正仓院藏品为例；claim 保留“变与不变”的总体判断，不把它简化为封闭不变。",
    1020, 1020, [1020], "二、佛教的渗透及其设计史意义"))

rows.append(C(
    "claim-1145", "cand-03-100", "historiographic_claim",
    "艺术风格有两个基本含义：一是内容—评价风格，二是形式—描述风格；二者都表达关于艺术事实的经验和看法，可为中国造物史研究提供参照。",
    "Artistic style has two basic senses: style as content-based evaluation and style as formal description; both express experience and views about artistic facts and can serve as references for studying Chinese artifact history.",
    [T + "feng-ge-maniera.md", T + "yishu-shejishi.md"],
    "断言语义取 L1040。原文由刘勰、司空图与沃尔夫林、佩特森两组传统对照得出；claim 保留二分及其认识论定位，不把两者化约为同一。",
    1040, 1040, [1040], "三、风格论——学术史的追溯"))

rows.append(C(
    "claim-1146", "cand-03-101", "historiographic_claim",
    "造物设计史的风格特征不能简单等同于作家、诗人或艺术家的独创性；其价值意味植根于造物的文化土壤与历史发展，是历史性发展的自然展现。",
    "Stylistic traits in artifact design cannot be simply equated with the originality of writers, poets or artists; their value is rooted in the cultural soil and historical development of artifact making and is a natural manifestation of that development.",
    [T + "feng-ge-maniera.md", T + "chuantong-sheji.md", T + "yishu-shejishi.md"],
    "断言语义取 L1044。原文先引“文如其人”“风格即人”，随即限定造物风格不同；claim 保留这一限定。",
    1044, 1044, [1044], "三、风格论——学术史的追溯"))

rows.append(C(
    "claim-1147", "cand-03-102", "historiographic_claim",
    "森珀《工艺美术与建筑的风格》把从远古至当代的艺术史视为连续线性发展，认为风格由地域、气候、时代、习俗及材料、工具等因素决定；里格尔以“艺术意志”强调设计是心智的精神性活动，批评森珀的机械被动反应论。",
    "Semper's Style in the Technical and Tectonic Arts treated art history from antiquity to the present as a continuous linear development shaped by region, climate, period, custom and especially materials and tools; Riegl's Kunstwollen emphasized design as mental-spiritual activity and criticized Semper's mechanical, passive-response theory.",
    [B + "gong-yi-mei-shu-yu-jian-zhu-de-feng-ge.md", B + "feng-ge-wen-ti.md", P + "li-ge-er.md", T + "yi-shu-yi-zhi.md", T + "feng-ge-maniera.md"],
    "断言语义取 L1046。原文并列两人的方法论；claim 保留各自立场，不裁决何者正确。",
    1046, 1046, [1046], "三、风格论——学术史的追溯"))

rows.append(C(
    "claim-1148", "cand-03-103", "synthetic_claim",
    "初唐起，魏晋以来的“清秀”基调逐渐被打破，至盛唐确立以华丽丰腴为主流的造物新风格，器物造型由清瘦俊朗转向雍容圆润，构成唐代造物风格的总体特征。",
    "From the early Tang the Six Dynasties' refined idiom was gradually broken; by High Tang a sumptuous and full-bodied style became dominant, with vessel forms shifting from slender to rounded and dignified, forming the overall character of Tang design.",
    [T + "tang-sancai.md", T + "baoxianghua-wen.md", T + "tang-dai-qingci-yao.md"],
    "断言语义取 L1058-L1060。原文以锦绫纹饰由骨架式向缠枝卷草、宝相花演变说明转折；claim 保留风格转折的总体判断，不把某一纹样当作唯一标志。",
    1058, 1060, [1058, 1060], "1. 华丽丰腴是造物富于美感的自然呈现"))

rows.append(C(
    "claim-1149", "cand-03-104", "interpretive_claim",
    "从造型发展看，初唐、盛唐是摆脱外来影响的转折期，中晚唐是风格特征明确化的定型期。",
    "In terms of form, the Early and High Tang were the transitional period in which foreign influence was shed, while the Mid- and Late Tang were the period in which stylistic traits became clearly fixed.",
    [T + "tang-sancai.md", T + "tang-dai-qingci-yao.md", T + "feng-ge-maniera.md"],
    "断言语义取 L1094。原文以金银器脚杯由柱状清瘦到多瓣圆润、再到隆满增大的过程为据；claim 保留三阶段划分。",
    1094, 1094, [1094], "1. 华丽丰腴是造物富于美感的自然呈现"))

rows.append(C(
    "claim-1150", "cand-03-105", "synthetic_claim",
    "宋代士阶层兴起为造物注入新活力，其价值取向与艺术趣味影响造物面貌；朱熹等理学家提出“简易”“致用”的设计思想，儒学原则的世俗化、生活化和实用化促使造物风格转变。",
    "The rise of the scholar stratum in the Song brought new vitality to artifact making, its values and aesthetic tastes shaping design; Neo-Confucians such as Zhu Xi proposed simplicity and practical use, and the secularization, domestication and pragmatization of Confucian principles drove a stylistic shift.",
    [T + "shi-class.md", P + "zhu-xi.md", T + "lixue.md", T + "riyongpin-meishuhua-gongyipin-shiyonghua.md"],
    "断言语义取 L1107-L1117。原文以苏轼、欧阳修“平淡”论与朱熹、欧阳修、王安石“适用为本”论并列；claim 保留士人审美与理学实用观两条线索。",
    1107, 1117, [1107, 1117], "2. 文人士大夫的情趣孕育了造物设计的“典雅”风格"))

rows.append(C(
    "claim-1151", "cand-03-106", "synthetic_claim",
    "宋代一般造物的重要特征是“质朴”：日用器物大量生产且以简单、质朴、实用为主，虽有个别逾制奢侈现象，文献与实物仍显示质朴为主导。",
    "A major feature of ordinary Song artifacts is plainness: everyday wares were produced in quantity with simplicity, plainness and practicality dominant; despite isolated excesses, texts and objects still show plainness as the norm.",
    [T + "songdai-yaoxi.md", T + "riyongpin-meishuhua-gongyipin-shiyonghua.md", T + "song-ci-zhuangshi-shoufa.md"],
    "断言语义取 L1123。原文承认制度未必自觉遵行、地方有“壮丽相夸”，claim 保留这一反证而不把质朴绝对化。",
    1123, 1123, [1123], "3. 质朴：宋代一般造物状况"))

rows.append(C(
    "claim-1152", "cand-03-107", "evaluative_claim",
    "写实花鸟与山水界画因过分强调“形似”而束缚设计意匠，按实描摹成为桎梏；这一消极面不仅影响纯观赏工艺品，也影响宋之后生活实用品的装饰设计，使元明清乃至近代设计缺乏意匠的生动表现。",
    "Realistic bird-and-flower painting and ruled-line landscape, by overemphasizing formal likeness, constrained design invention; literal copying became a shackle that affected not only purely ornamental crafts but also later everyday wares, leaving Yuan-Ming-Qing and even modern design short of lively inventiveness.",
    [T + "song-ci-zhuangshi-shoufa.md", T + "kesi.md", T + "jindai-ranchou-ye.md"],
    "断言语义取 L1159。原文明确说“许多人都没有提及消极的一面”；claim 保留作者的评价立场及其对后世的强影响判断。",
    1159, 1159, [1159], "五、院画的扩张与意匠化设计的衰落"))

rows.append(C(
    "claim-1153", "cand-03-108", "synthetic_claim",
    "元代以来文化艺术分化出上层宫廷文人与下层民间市民两大支流：上层追求精巧繁复、强化文人情趣，民间以世俗吉祥含义蓬勃发展，二者相互影响融合并显示更新趋势。",
    "Since the Yuan, culture and art split into two streams, an upper court-literati one and a lower folk-urban one: the former pursued refinement and complexity with literati taste, the latter flourished through worldly auspicious meanings; the two interacted, merged and showed a renewing tendency.",
    [T + "shi-class.md", T + "yuan-dai-ciqi-qixing.md", T + "jixiang-tu-an.md"],
    "断言语义取 L1169。原文在承认汉唐传统延续的同时提出两大支流；claim 保留“分化—互动”结构，不把两者写成彼此隔绝。",
    1169, 1169, [1169], "五、院画的扩张与意匠化设计的衰落"))

rows.append(C(
    "claim-1154", "cand-03-109", "interpretive_claim",
    "明代中叶以来早期工业化已为现代设计准备了一定生产基础，西方现代设计的最初引入在中国不是单纯被动，而是传统设计积累与工场手工业基础上的积极“回应”；现代设计不能“克隆”，并非外因决定。",
    "From the mid-Ming, early industrialization had already prepared a production basis for modern design; the initial introduction of Western modern design in China was not purely passive but an active response grounded in traditional design accumulation and manufacture; modern design cannot be cloned and is not externally determined.",
    [T + "zaoqi-gongyehua.md", T + "xiandai-gongyi.md", T + "industrial-design.md"],
    "断言语义取 L1175-L1177。原文以“冲击—回应”框架讨论中国现代设计起步；claim 保留作者的反外因决定论立场，不否认西方工业化的重要作用。",
    1175, 1177, [1175, 1177], "第三章 延续更新与近代困境（导论）"))

rows.append(C(
    "claim-1155", "cand-03-110", "evaluative_claim",
    "《天工开物》是两千年来几乎唯一将手工业等几十个门类技术设计综合研究的著作；全书十八章中十三章与造物设计有关，大体分为农用工具、衣料染织、金属铸锻、陶瓷砖瓦、造纸、交通工具、珠宝琉璃七大类。",
    "The Tiangong Kaiwu is virtually the only work in two millennia to synthesize technical design across dozens of handicraft branches; thirteen of its eighteen chapters concern artifact design, grouped into seven categories: agricultural tools, textiles and dyeing, metal casting and forging, ceramics and bricks, papermaking, transport, and jewels/glass.",
    [B + "tiangong-kaiwu.md", B + "kaogongji.md", P + "song-yingxing.md"],
    "断言语义取 L1183-L1190。原文将《天工开物》与《考工记》以来只涉单一领域且多失传的专著对比；claim 保留“综合性”与“七大类”的具体判断。",
    1183, 1190, [1183, 1190], "一、《天工开物》：传统造物的历史镜像"))

rows.append(C(
    "claim-1156", "cand-03-111", "synthetic_claim",
    "宋应星时代民间经营的棉麻纺织、造船、陶瓷、砖瓦、造纸等手工业规模已超过官营并占主导；自元到明是传统造物第三阶段，其造物随商品经济和市民文化发展而突破汉唐伦理规范界限。",
    "In Song Yingxing's time, privately operated cotton and linen textile, shipbuilding, ceramics, brick-tile and papermaking industries exceeded official workshops in scale and became dominant; the Yuan-to-Ming span is the third stage of traditional artifact making, in which commodity economy and urban culture pushed beyond Han-Tang ethical norms.",
    [T + "guanying-shougongye.md", B + "tiangong-kaiwu.md", T + "li-yue-zhidu.md"],
    "断言语义取 L1192-L1196。原文以《天工开物》分卷重民用和明末棉布取代丝麻毛为例；claim 保留“第三阶段”与“突破伦理规范”的判断。",
    1192, 1196, [1192, 1196], "一、《天工开物》：传统造物的历史镜像"))

rows.append(C(
    "claim-1157", "cand-03-112", "historiographic_claim",
    "《天工开物》体现传统造物的三个基本特性：造物的系统性、生产的密集型、设计的适应自然与物尽其用；其中的“设计科学化”倾向虽不同于现代系统规划，却在相当程度上与现代设计精神相符。",
    "The Tiangong Kaiwu embodies three basic traits of traditional artifact making: systemic organization, labor-intensive production, and design that adapts to nature and uses materials fully; its tendency toward a science of design differs from modern system planning yet substantially agrees with the spirit of modern design.",
    [B + "tiangong-kaiwu.md", T + "chuantong-sheji.md", T + "industrial-design.md"],
    "断言语义取 L1198-L1202。原文以冶铸、锤锻、陶埏、舟车的流程分析说明系统性，以“一杯功过手七十二”说明密集型；claim 保留三特性归纳。",
    1198, 1202, [1198, 1202], "一、《天工开物》：传统造物的历史镜像"))

rows.append(C(
    "claim-1158", "cand-03-113", "historiographic_claim",
    "两千年来真正诠释造物中人与自然关系的是宋应星；“天工开物”四字体现中国传统造物设计的真正内涵，故作者把《天工开物》视为设计史上传统设计的终结。",
    "Song Yingxing was the one who, over two millennia, truly interpreted the relation between making and nature; the phrase tiangong kaiwu embodies the real content of Chinese traditional design, and the author therefore treats the Tiangong Kaiwu as the end of traditional design in design history.",
    [P + "song-yingxing.md", B + "tiangong-kaiwu.md", T + "chuantong-sheji.md", T + "tianren-xiangfen.md"],
    "断言语义取 L1218-L1220。原文考释“天工”既可指自然力也可指自然力与人工合力，但都归于适应自然、物尽其用；claim 保留作者的终结判断。",
    1218, 1220, [1218, 1220], "一、《天工开物》：传统造物的历史镜像"))

rows.append(C(
    "claim-1159", "cand-03-114", "interpretive_claim",
    "汉代官营手工业机构庞大、组织管理严密，中央与郡县分级并设工官，从规模、分工与管理看，其官手工业制度已相当完善、组织形式和管理机构基本定型。",
    "Han official handicraft institutions were large and tightly organized, with central and commandery-county levels and craft offices in developed regions; in scale, division of labor and management, the official handicraft system was already well developed and its organizational forms basically fixed.",
    [T + "handai-guanzhi.md", T + "guanying-shougongye.md", T + "guifanhua.md"],
    "断言语义取 L827。原文列举少府、尚方、考工室及太常、将作大匠等系统；claim 保留制度定型判断，不逐一复述官署。",
    827, 827, [827], "3. 官营制度的定型与地域设计的聚集"))

rows.append(C(
    "claim-1160", "cand-03-115", "historiographic_claim",
    "汉之后的魏晋南北朝造物发展是一种转向，是汉代以来首次具有时代转折意义的变迁，魏晋南北朝乃至唐宋的造物新境域在这一变迁与突破中诞生。",
    "The post-Han development of Six Dynasties artifact making was a turn, the first change since the Han with epochal significance; the new domains of Six Dynasties and even Tang-Song artifact making were born in this transformation and breakthrough.",
    [T + "liuchao-gongjiang-zhidu.md", T + "liuchao-tongjing.md", T + "qing-ci.md"],
    "断言语义取 L861。原文把魏晋南北朝置于承继与革新、吸收与变异的运动方式中；claim 保留“首次时代转折”的分期判断。",
    861, 861, [861], "一、传统、外来、时尚"))

rows.append(C(
    "claim-1161", "cand-03-116", "historiographic_claim",
    "风格理论模式应从作品中归纳而来，而不是相反；中国设计史的风格演变必须从几千年大量造物中归纳区分，风格描述与评判才能经受事实检验。",
    "Stylistic theory must be induced from works, not the reverse; the evolution of style in Chinese design history must be induced and differentiated from the vast corpus of artifacts over millennia so that description and judgment can withstand factual testing.",
    [P + "pang-xunqin.md", T + "feng-ge-maniera.md", T + "yishu-shejishi.md"],
    "断言语义取 L1050。原文在评述庞薰琹比较研究体与西方风格系统后提出这一方法论；claim 保留“从作品到理论”的方向。",
    1050, 1050, [1050], "三、风格论——学术史的追溯"))

rows.append(C(
    "claim-1162", "cand-03-117", "historiographic_claim",
    "唐宋造物风格转折的许多环节仍需深入研究，应考察其形成背景与演化过程，从多样造物作风中寻找共有特征，进而把握这一时期造物艺术变异又延续的发展状况。",
    "Many links in the Tang-Song stylistic transition still require deeper study: their formative background and evolutionary process should be examined, common traits sought amid diverse artifact manners, and the simultaneous variation and continuity of the period grasped.",
    [T + "feng-ge-maniera.md", T + "tang-dai-qingci-yao.md", T + "songdai-yaoxi.md"],
    "断言语义取 L1054。原文针对前辈“厚、满、雍容、绚丽”与“理、严谨、隽雅”等归纳提出补充研究路径；claim 保留其研究纲领性质。",
    1054, 1054, [1054], "四、由“华丽丰腴”到“典雅质朴”"))

rows.append(C(
    "claim-1163", "cand-03-118", "interpretive_claim",
    "宋代造物审美与风格的转换来自政治权力和院体画的扩张：宫廷奖励画艺、画院强调“格法”与“形似”，写实花鸟画由此带来审美观念和造物艺术的深刻变化。",
    "The Song transformation of artifact aesthetics and style came from political power and the expansion of academic painting: the court rewarded painting, the academy stressed rules and formal likeness, and realistic bird-and-flower painting brought profound changes in aesthetic values and artifact art.",
    [T + "song-ci-zhuangshi-shoufa.md", T + "kesi.md", T + "shi-class.md"],
    "断言语义取 L1157。原文以画院制度、文思院等宫中制作机构及绣品受院体画影响为据；claim 保留“政治权力—院体画—造物”的因果链。",
    1157, 1157, [1157], "五、院画的扩张与意匠化设计的衰落"))

rows.append(C(
    "claim-1164", "cand-03-119", "interpretive_claim",
    "设计艺术是一种特殊的造型结构形式，与再现性绘画不同，它是非写实的“人造”符号；模仿绘画、追求清晰真实的自然形象会脱离实用功能并丧失绘画的意趣神韵。",
    "Design art is a distinctive kind of formative structure; unlike representational painting it is a non-realistic human-made sign. Imitating painting and pursuing clear, faithful natural images departs from practical function and loses painting's expressive spirit.",
    [T + "yishu-sheji.md", T + "yuanzaoxing.md", T + "chuantong-sheji.md"],
    "断言语义取 L1161。原文以平绣法、白瓷、粉本等条件说明写实装饰的兴盛；claim 保留设计符号与再现绘画的区分。",
    1161, 1161, [1161], "五、院画的扩张与意匠化设计的衰落"))

rows.append(C(
    "claim-1165", "cand-03-120", "interpretive_claim",
    "早期工业化与近代工业化没有必然因果关系，早期工业化中发展的造物设计也未直接产生近代设计，但它为近代设计准备了必要条件，可视为近现代设计的早期先行阶段。",
    "Early industrialization had no necessary causal relation to modern industrialization, and the artifact design developed within it did not directly produce modern design; it did prepare necessary conditions, however, and can be seen as an early precursor stage of modern design.",
    [T + "zaoqi-gongyehua.md", T + "jindai-ranchou-ye.md", T + "industrial-design.md"],
    "断言语义取 L1226。原文同时指出早期工业化仍以手工业为主、机器使用有限；claim 保留“先行阶段”而非“直接起源”的限定。",
    1226, 1226, [1226], "二、早期工业化时期一般造物设计的发展（导论）"))

out = ROOT / "_ll_ll3a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

from collections import Counter
types = Counter(r["claim_type"] for r in rows)
links = [p for r in rows for p in r["supported_by"]]
print("rows", len(rows))
print("types", dict(types))
print("links", len(links), "distinct", len(set(links)))
print("range", rows[0]["claim_id"], "-", rows[-1]["claim_id"])
