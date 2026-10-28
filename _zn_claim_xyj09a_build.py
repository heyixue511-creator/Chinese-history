# -*- coding: utf-8 -*-
"""Build the CL2a Xia Yanjing 2009 claim rows (preface, primitive, Xia-Shang-Zhou)."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
ROWS = []


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, chapter, section=None, merged=None, corrob=None):
    src = {
        "doc_id": DOC,
        "source_file": SRC,
        "source_span": {
            "line_start": start,
            "line_end": end,
            "span_kind": kind,
            "key_lines": key_lines,
            "block_ids": block_ids,
            "chapter": chapter,
        },
        "candidate_id": DOC + ":" + cid,
    }
    if section:
        src["source_span"]["section"] = section
    if merged:
        src["merged_candidate_ids"] = [DOC + ":" + m for m in merged]
    if corrob:
        src["corroborating_spans"] = corrob
    ROWS.append({
        "claim_id": None,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": src,
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    })


C("cand-01-03", "historiographic_claim",
  "夏燕靖认为，中国艺术设计史研究应摆脱沿袭已久的工艺美术史叙事方式与研究方法，用艺术设计的眼光重新认识造物行为的发展历程，并揭示“匠作之业”的思维方式与设计演变过程。",
  "Xia Yanjing argues that the study of Chinese design history should break away from the long-established narrative methods of craft-art history, re-examine the development of making activities through the lens of art design, and reveal the ways of thinking and design evolution embodied in the “crafting trades.”",
  "high",
  ["04-knowledge/units/terms/yishu-shejishi.md", "04-knowledge/units/terms/gongyi-meishu.md"],
  "序言 L68 明确提出以艺术设计眼光钩沉史料、考镜源流，并批评工艺美术史叙事沿袭已久。",
  68, 68, "line", [68], ["b0005"], "序言", "序言")

C("cand-01-04", "historiographic_claim",
  "夏燕靖把中国艺术设计史与工艺美术史的最大区别概括为：前者侧重设计与功能，后者侧重工艺与欣赏；并以原始陶器和青铜器为例，说明设计史关注功能与形态构成，工艺美术史则侧重彩陶纹样或商周青铜装饰赏析。",
  "Xia Yanjing defines the chief difference between Chinese design history and craft-art history as a shift in emphasis from craft and appreciation to design and function, illustrating it with prehistoric pottery and bronzes: design history studies function and form, while craft-art history studies painted-pottery ornament or late Shang and early Western Zhou bronze decoration.",
  "high",
  ["04-knowledge/units/terms/yishu-shejishi.md", "04-knowledge/units/terms/gongyi-meishu.md"],
  "序言 L70 以“最大区别”直接提出，并用原始陶器、青铜器研究重点的差异作例证。",
  70, 70, "line", [70], ["b0005"], "序言", "序言")

C("cand-01-05", "historiographic_claim",
  "夏燕靖把现当代中国艺术设计的叙述重点定为：近代以上世纪初叶机器工业的起步与发展为中心，介绍纺织印染、机器制造与商业贸易中的设计；当代则突出工业设计与多媒体艺术设计，并遵循“以史带论”、突出重点的原则。",
  "Xia Yanjing sets the modern and contemporary focus of the narrative on the rise of machine industry in the early twentieth century—textile printing and dyeing, machine manufacture and commercial trade—and, for the contemporary period, on industrial design and multimedia art design, following the principle of “using history to carry argument” and highlighting key developments.",
  "high",
  ["04-knowledge/units/terms/yishu-shejishi.md"],
  "序言 L70 在说明现当代叙述范围后，明确提出“以史带论”和突出重点的编写原则。",
  70, 70, "line", [70], ["b0005"], "序言", "序言")

C("cand-01-92", "historiographic_claim",
  "夏燕靖认为，中国艺术设计史的取材应以生产生活器具以及城镇布局、建筑构造、室内装修与陈设、庭园布置等环境建筑内容为重点；以陈设欣赏为主的玉器、刺绣、雕刻、艺术瓷等工艺品不重点列入，这构成设计史与工艺美术史在对象范围上的又一区别。",
  "Xia Yanjing argues that Chinese design history should center on production and everyday utensils as well as environmental and architectural subjects such as town layout, building construction, interior furnishing and garden design, while display-oriented crafts such as jade, embroidery, carving and art porcelain should not be given major emphasis—another difference in scope from craft-art history.",
  "high",
  ["04-knowledge/units/terms/yishu-shejishi.md", "04-knowledge/units/terms/gongyi-meishu.md"],
  "序言 L70 明确列出不重点列入的工艺品类别与应纳入的生产生活器具、环境建筑内容，并以此区分设计史与工艺美术史。",
  70, 70, "line", [70], ["b0005"], "序言", "序言")

C("cand-01-07", "interpretive_claim",
  "夏燕靖认为设计的起源与人类起源同步：约300万年前猿人形成时已开始制造石器，最早石器具有一定形态规格和初级形式感，因此“一切人造物即意味着设计”；但最初的设计仍处于朦胧、不自觉的状态。",
  "Xia Yanjing holds that the origin of design coincides with the origin of humanity: by about three million years ago hominins were making stone tools with definite formal specifications and an elementary sense of form, so that “every human-made object implies design,” although this earliest design remained indistinct and not yet self-conscious.",
  "medium",
  ["04-knowledge/units/terms/sheji.md", "04-knowledge/units/procedures/shiqi-dazhi-sanfa.md"],
  "原文由天然工具使用、300万年前猿人形成和最早石器形态，推出设计起源上限与“设计起源与人类起源同步”的命题，并自注其推测性。",
  233, 233, "line", [233], ["b0014", "b0015"], "原始社会的艺术设计", "1. 设计的起源与石器的制作设计 / 1）设计的起源")

C("cand-01-15", "interpretive_claim",
  "夏燕靖认为，石器第二步修整加工的产生不仅在工具设计制造史上具有重要意义，在改造客观世界上同样重要，它标志着人类设计能力与主观能动性的进一步提高。",
  "Xia Yanjing argues that the emergence of secondary retouch on stone tools was significant not only in the history of tool design and manufacture but also in the human transformation of the objective world, marking a further advance in design capacity and conscious agency.",
  "high",
  ["04-knowledge/units/procedures/shiqi-dazhi-sanfa.md", "04-knowledge/units/terms/sanleng-jianzhuang-shiqi.md"],
  "原文在述及丁村文化少量石器出现第二步修整加工后，直接作出此评价。",
  264, 264, "line", [264], ["b0021"], "原始社会的艺术设计", "1. 设计的起源与石器的制作设计 / ② 石器的二次加工")

C("cand-01-19", "interpretive_claim",
  "夏燕靖认为，新石器时代中期经打制后磨制的石器在形状规则性、表面光洁度和材料选择上已超出实用需要，兼具形式意义；从纯功能性设计到对审美的自觉追求，是设计文明的一大进步。",
  "Xia Yanjing argues that the ground stone tools of the mid-Neolithic, with their regularity of shape, smooth surfaces and selected materials, exceeded practical requirements and carried formal meaning; the move from purely functional design to a conscious pursuit of beauty marked a major advance in design civilization.",
  "high",
  ["04-knowledge/units/procedures/mozhi-shiqi.md", "04-knowledge/units/terms/xinshiqi-shiqi-leixing.md"],
  "原文由磨制石器的形状、表面和选材特征推出其已具形式意义，并作出设计文明进步的判断。",
  304, 304, "line", [304], ["b0023"], "原始社会的艺术设计", "2. 陶器的制作与器形的设计 / ③ 石器的磨制技术")

C("cand-01-28", "interpretive_claim",
  "夏燕靖把原始陶器的设计特点归纳为三点：制作与生活息息相关，既满足物质需要又满足审美需要，制作者同时是使用者与欣赏者；实用与审美完整统一；装饰纹样来源于当时的社会生活形态，是社会生活的真实写照与艺术反映。",
  "Xia Yanjing summarizes the design characteristics of prehistoric pottery in three points: production was closely bound to daily life, with the maker also the user and viewer; utility and beauty were fully unified; and decorative motifs derived from contemporary social life, serving as both a true record and an artistic reflection of it.",
  "high",
  ["04-knowledge/units/terms/taoqi.md", "04-knowledge/units/terms/painted-pottery.md"],
  "原文以“综合原始陶器的用途及装饰形式”列出三点，并以彩陶纹样位置、陶罐口小腹大为例。",
  330, 330, "line", [330], ["b0030"], "原始社会的艺术设计", "2. 陶器的制作与器形的设计 / 原始陶器的设计特点")

C("cand-01-26", "interpretive_claim",
  "夏燕靖指出，考古学界较普遍地认为尖底瓶是制造者掌握一定力学原理后的产品，但这只是一种看法；当时的制造者是否具备这样的意识，仍有待进一步查考。",
  "Xia Yanjing notes that archaeologists generally regard the pointed-bottom jar as a product of the makers' grasp of mechanical principles, but treats this only as one view; whether the makers actually possessed such awareness still requires further investigation.",
  "medium",
  ["04-knowledge/units/terms/pointed-bottom-jar.md"],
  "原文在描述尖底瓶重心与自动直立现象后，对“掌握力学原理”说作出明确保留。",
  344, 344, "line", [344], ["b0032"], "原始社会的艺术设计", "2. 陶器的制作与器形的设计 / 知识链接：舞蹈纹盆的多种文化意义")

C("cand-01-30", "historiographic_claim",
  "夏燕靖把舞蹈纹彩陶盆纹样的解释归纳为五说：原始装饰成型期的范例、叙事型绘画风格的代表、生殖崇拜与“求偶舞”的写照、原始祭祀活动的“化石”资料、图腾与氏族社会联系的佐证；他未判定唯一解释，而称其象征含义十分丰富。",
  "Xia Yanjing lists five interpretations of the dancing-figure painted pottery basin—an example of formative prehistoric ornament, a representative of narrative painting, a depiction of fertility cult and courtship dance, a “fossil” of primal ritual, and evidence of totemic clan ties—without deciding among them, instead emphasizing the richness of its symbolism.",
  "medium",
  ["04-knowledge/units/works/wudaowen-caitao-pen.md"],
  "知识链接逐条列出五说，作者未判定唯一解释，并称其象征含义丰富。",
  342, 342, "line", [342], ["b0032"], "原始社会的艺术设计", "2. 陶器的制作与器形的设计 / 知识链接：舞蹈纹盆的多种文化意义")

C("cand-01-41", "interpretive_claim",
  "夏燕靖认为河姆渡文化陶甑的设计是我国烹饪工艺的一大突破，标志着陶器时代的到来，也意味着以熟食、热食为主要特征的饮食文化风格的形成。",
  "Xia Yanjing argues that the Hemudu pottery steamer (zeng) was a major breakthrough in Chinese cooking technology, marking the arrival of the pottery age and the formation of a food culture centered on cooked and heated food.",
  "high",
  ["04-knowledge/units/terms/tao-zeng.md", "04-knowledge/units/terms/fu-li-zeng.md"],
  "原文在描述陶甑通蒸汽小孔后连续作出“一大突破”“标志陶器时代到来”“饮食文化风格形成”的判断。",
  392, 392, "line", [392], ["b0040"], "原始社会的艺术设计", "2. 陶器的制作与器形的设计 / ⑤ 河姆渡文化")

C("cand-01-42", "interpretive_claim",
  "夏燕靖把《易·繫辞篇》“黄帝、尧、舜垂衣裳而天下治，盖取诸乾坤”解释为一种统治方式：无论“垂拱”还是“垂衣裳”都与“天下治”构成因果关系；并据此认为新石器时代中晚期已有纺织衣料，黄帝、尧、舜时代已有成型衣服，服装形式定型为上衣下裳。",
  "Xia Yanjing reads the Yijing passage “Huangdi, Yao and Shun let their robes hang down and the world was governed, taking the pattern from Qian and Kun” as describing a mode of rule in which “hanging down the hands” or “hanging down the robes” is the cause and “the world governed” the effect; on this basis he holds that woven cloth existed in the mid-to-late Neolithic and that formed garments, fixed as upper garment and lower skirt, existed by the age of Huangdi, Yao and Shun.",
  "medium",
  ["04-knowledge/units/terms/yuanshi-fuzhuang.md", "04-knowledge/units/persons/huangdi-legend.md"],
  "作者将“垂衣裳而天下治”拆解为“垂拱”为因、“天下治”为果，并联系上衣下裳的服装形制。",
  398, 398, "line", [398], ["b0041", "b0042"], "原始社会的艺术设计", "3.纺编织物的产生与设计形式 / 1）纺编织物的产生")

C("cand-01-45", "factual_claim",
  "夏燕靖据良渚文化早期丝织物遗存指出，我国早在四五千年前就开始养蚕织绢，是世界上最早出产丝织品的国家。",
  "Citing early Liangzhu culture silk remains, Xia Yanjing states that China began sericulture and silk weaving as early as four to five thousand years ago and was the world's earliest producer of silk textiles.",
  "medium",
  ["04-knowledge/units/terms/liangzhu-culture.md", "04-knowledge/units/terms/ling-silk.md"],
  "原文由良渚文化早期丝麻织物遗存直接推出养蚕织绢时间及“世界最早”判断。",
  416, 416, "line", [416], ["b0043"], "原始社会的艺术设计", "3.纺编织物的产生与设计形式 / 2）纺编织物的设计形式")

C("cand-01-48", "interpretive_claim",
  "夏燕靖认为，半地穴式、干栏式等早期原始木构架建筑奠定了未来木构架建筑的雏形，揭开了我国建筑设计的序幕。",
  "Xia Yanjing argues that early timber-frame dwellings—semi-subterranean houses and stilt buildings—established the prototype of later timber-frame architecture and opened the history of architectural design in China.",
  "high",
  ["04-knowledge/units/terms/ganlan-shi-jianzhu.md"],
  "原文在综述半地穴、庙底沟、龙山套间和干栏式居住形式后，作出此总体评价。",
  420, 420, "line", [420], ["b0044"], "原始社会的艺术设计", "4. 原始居住设计的雏形")

C("cand-01-50", "factual_claim",
  "夏燕靖在解释干栏式建筑时指出，河姆渡遗址发现的干栏式建筑遗迹是迄今为止世界上最早的木构建筑。",
  "In his account of ganlan (stilt) architecture, Xia Yanjing states that the ganlan remains found at Hemudu are the world's earliest timber structures known to date.",
  "medium",
  ["04-knowledge/units/terms/ganlan-shi-jianzhu.md", "04-knowledge/units/places/hemudu-site.md"],
  "知识链接在定义干栏式建筑后直接给出“迄今世界上最早”的判断，未展开比较依据。",
  435, 435, "line", [435], ["b0046"], "原始社会的艺术设计", "4. 原始居住设计的雏形 / 知识链接：干栏式建筑")

C("cand-01-51", "historiographic_claim",
  "夏燕靖把夏朝定为中国文明史的开端，认为它意味着由原始社会进入奴隶社会；二里头遗址及偃师商城等考古材料证明，夏代晚期已具备宫殿、手工作坊和礼仪青铜器、玉器等国家政治中心条件。",
  "Xia Yanjing treats the Xia dynasty as the beginning of Chinese civilization and the transition from primitive to slave society, citing Erlitou and Yanshi Shang City as evidence that by the late Xia there were palaces, workshops and ritual bronzes and jades—the conditions of a state political center.",
  "high",
  ["04-knowledge/units/places/erlitou-site.md", "04-knowledge/units/places/yanshi-shangcheng.md"],
  "原文以夏朝为“我国文明史的开端”，并以二里头等遗址作为夏代晚期国家形态的证据。",
  461, 461, "line", [461], ["b0050"], "夏商周时期的艺术设计", "章首")

C("cand-01-55", "historiographic_claim",
  "夏燕靖把中国青铜时代的年代框架定为：约公元前2000年开始形成，历时大约15个世纪，相当于夏商周三代。",
  "Xia Yanjing dates the Chinese Bronze Age from about 2000 BCE and gives it a duration of roughly fifteen centuries, corresponding to the Xia, Shang and Zhou dynasties.",
  "high",
  ["04-knowledge/units/terms/qingtong-shidai.md"],
  "原文在“青铜器的出现”一节给出该年代框架。",
  477, 477, "line", [477], ["b0052"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 1）青铜器的出现")

C("cand-01-57", "interpretive_claim",
  "夏燕靖认为商周时期青铜器主要是统治权力的象征，权力的更替也通过青铜器来体现；《左传》所记“桀有昏德，鼎迁于商”“商纣暴虐，迁鼎于周”即是其表现。",
  "Xia Yanjing argues that in the Shang and Zhou bronzes served chiefly as symbols of ruling power, with changes of power expressed through them—as in the Zuozhuan records that “Jie had muddled virtue, and the cauldrons moved to Shang” and “Zhou Xin was cruel, and the cauldrons moved to Zhou.”",
  "high",
  ["04-knowledge/units/terms/qingtong-liqi.md"],
  "知识链接以“封建王朝政治”解释青铜时代高峰，并引《左传》鼎迁记载。",
  489, 489, "line", [489], ["b0055", "b0056"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 知识链接：青铜器与封建王朝的统治")

C("cand-01-59", "interpretive_claim",
  "夏燕靖认为，青铜器的礼制设计含有浓厚的“藏礼于器”思想与文化观念，不仅造就了夏商周三代青铜器的形制风格与特色，也成为历朝历代设计文化中的重要命题。",
  "Xia Yanjing argues that the ritual design of bronzes embodied a strong idea and cultural conception of “ritual stored in vessels,” which shaped the forms and styles of Xia-Shang-Zhou bronzes and remained an important theme in design culture through later dynasties.",
  "high",
  ["04-knowledge/units/terms/cangli-yuqi.md", "04-knowledge/units/terms/qingtong-liqi.md"],
  "原文在论述“礼治”四点后作出该总结性判断。",
  493, 493, "line", [493], ["b0057"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 青铜器的礼制意义")

C("cand-01-64", "factual_claim",
  "夏燕靖指出，西周奴隶主为加强统治规定了一整套礼制，对祭祀和典礼所用礼器的数量与规格作严格限制，使贵贱有等、上下有别，即“藏礼于器”；《周礼》所载天子九鼎、诸侯七鼎、大夫五鼎、士三鼎是其制度表现。",
  "Xia Yanjing shows that Western Zhou rulers established a ritual system strictly limiting the number and specifications of vessels used in sacrifices and ceremonies, so that noble and base, high and low were distinguished—the principle of “ritual stored in vessels”—as in the Zhouli quotas of nine ding for the Son of Heaven, seven for lords, five for ministers and three for officers.",
  "high",
  ["04-knowledge/units/terms/cangli-yuqi.md", "04-knowledge/units/terms/qingtong-liqi.md"],
  "原文在“礼制器具设计”节引《周礼》与《左传》，并以“藏礼于器”概括。",
  538, 538, "line", [538], ["b0062"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 3）礼制器具设计")

C("cand-01-65", "historiographic_claim",
  "夏燕靖把春秋时期视为礼制松弛、青铜器风格转变的阶段：日用青铜器开始失去祭祀与礼器特性，造型设计摆脱商周以来的神话气氛，向较活泼的风格发展，莲鹤方壶是这种风格的典型代表。",
  "Xia Yanjing treats the Spring and Autumn period as a phase in which ritual constraints loosened and bronze style changed: daily bronzes began to lose their sacrificial and ritual character, design shed the mythological atmosphere inherited from Shang and Zhou, and a livelier style emerged, exemplified by the Lotus and Crane Square Hu.",
  "high",
  ["04-knowledge/units/works/lianhe-fanghu.md"],
  "原文以春秋中期莲鹤方壶为例，说明礼制松弛后青铜器风格与实用器型的变化。",
  540, 540, "line", [540], ["b0062"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 3）礼制器具设计")

C("cand-01-67", "interpretive_claim",
  "夏燕靖认为殷商时期青铜器超出实用功能之上的审美追求表现得异常强烈，但缺乏统一标准：一部分器物凝重浑厚，一部分被夸张到怪诞神秘，还有一部分考虑实用功能、另一部分则不予考虑。",
  "Xia Yanjing argues that Shang bronzes display an unusually strong aesthetic pursuit beyond practical function but lack a unified standard: some vessels are grave and massive, others exaggerated to the grotesque and mysterious, and some accommodate practical use while others do not.",
  "high",
  ["04-knowledge/units/terms/shangdai-qingtongqi-balei.md", "04-knowledge/units/terms/qingtongqi.md"],
  "原文以司母戊鼎、四羊尊、龙虎尊、食人卣、人面纹铜钺及五爵中的觚、角、方彝为例展开对比。",
  548, 556, "bounded", [548, 556], ["b0063"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 4）设计风格")

C("cand-01-68", "interpretive_claim",
  "夏燕靖认为青铜既具有石器的坚硬，又具有陶器的可塑性，可以按设计者的需要自由创造实用而美观的器形；这是继制陶之后人类在产品设计领域的又一伟大创造。",
  "Xia Yanjing argues that bronze combines the hardness of stone with the plasticity of clay, allowing makers to create useful and beautiful forms freely according to design intent—a second great invention in product design after pottery.",
  "high",
  ["04-knowledge/units/terms/qingtongqi.md", "04-knowledge/units/terms/qingtong.md"],
  "原文在“形制设计”总述中比较青铜与石器、陶器的材料特性后作出该评价。",
  566, 566, "line", [566], ["b0064"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 5）形制设计")

C("cand-01-70", "interpretive_claim",
  "夏燕靖指出，鼎是青铜礼器中最重要的品种，被看作国家政权的象征；传说大禹制九鼎象征九州，古文献多以占有九鼎为取得政权的象征，“桀有乱德，鼎迁于殷”“商纣暴虐，鼎迁于周”以及楚庄王问鼎轻重都说明这一点。",
  "Xia Yanjing notes that the ding was the most important bronze ritual vessel and was regarded as a symbol of state power: legend credits Yu with casting nine cauldrons for the nine provinces, early texts treat possession of the nine cauldrons as legitimate rule, and the migrations of the cauldrons under Jie and Zhou Xin, together with King Zhuang of Chu's inquiry about their weight, all express this symbolism.",
  "medium",
  ["04-knowledge/units/events/yu-casts-nine-cauldrons.md", "04-knowledge/units/terms/qingtong-liqi.md"],
  "知识链接把九鼎传说、鼎迁记载与“问鼎”典故串联为政权象征的论证。",
  574, 574, "line", [574], ["b0066", "b0067"], "夏商周时期的艺术设计", "1. 青铜鼎器与礼制性设计 / 知识链接：鼎的重要象征")

C("cand-01-74", "interpretive_claim",
  "夏燕靖认为，夏代陶瓮的底由平底改为凹形，有助于陶瓮中的食物或水在加温时提高热力，说明当时工匠的设计意识已经逐步成熟。",
  "Xia Yanjing argues that the Xia-period pottery urn's change from a flat to a concave base helped raise the heat when food or water was warmed, showing that craftsmen's design awareness was gradually maturing.",
  "medium",
  ["04-knowledge/units/terms/taoqi.md"],
  "原文在“陶器”节以夏代陶瓮凹底为例，直接推出工匠设计意识成熟的判断。",
  654, 654, "line", [654], ["b0070", "b0071"], "夏商周时期的艺术设计", "2. 原始陶瓷器的形成与实用设计 / 1）陶器")

C("cand-01-76", "historiographic_claim",
  "夏燕靖据各地出土的商周时期大量青釉瓷断定，我国至迟在商代中期已经发明了瓷器。",
  "On the evidence of the many glazed stoneware finds of Shang and Zhou date from sites across China, Xia Yanjing concludes that porcelain was invented in China no later than the mid-Shang.",
  "high",
  ["04-knowledge/units/terms/proto-porcelain.md"],
  "原文在列举东下冯原始青瓷残片后，以商周青釉瓷的普遍发现作出该年代判断。",
  678, 678, "line", [678], ["b0072"], "夏商周时期的艺术设计", "2. 原始陶瓷器的形成与实用设计 / 2）瓷器")

C("cand-01-78", "factual_claim",
  "夏燕靖据《尚书·甘誓》所载夏启与有扈氏战于甘泽的誓师词指出，甘泽之战是历史上最早的车战，比喜克索斯人使用战车提早了300年；又引《吕氏春秋·简读》称商汤灭夏时其军中主力便是“良车七十乘”。",
  "Citing the oath in the Shangshu “Ganshi” sworn by Xia Qi before battle with the Youhu at Ganze, Xia Yanjing states that the Battle of Ganze was the earliest chariot battle in history, three hundred years before the Hyksos used chariots; he also quotes the Lüshi Chunqiu to the effect that Tang's army in the conquest of Xia was led by “seventy fine chariots.”",
  "medium",
  ["04-knowledge/units/events/ganshi-battle.md", "04-knowledge/units/terms/war-chariot.md"],
  "原文引《尚书·甘誓》与《吕氏春秋·简读》，并直接给出“最早车战”“提早300年”的比较判断。",
  698, 698, "line", [698], ["b0075", "b0076"], "夏商周时期的艺术设计", "3. 交通运输工具的设计规范 / 1）车")

C("cand-01-80", "interpretive_claim",
  "夏燕靖指出，我国春秋以前的马车都是独辕，车辕前部向上昂起，前端设衡轭以驭马；这种轭鞞式系驾法较当时西方的颈式系驾法先进得多。",
  "Xia Yanjing notes that Chinese horse-drawn chariots before the Spring and Autumn period all had a single shaft that rose at the front and carried a yoke for the horses, and that this yoke-and-harness method was considerably more advanced than the neck-harness method then used in the West.",
  "medium",
  ["04-knowledge/units/terms/xianqin-mache.md", "04-knowledge/units/terms/war-chariot.md"],
  "原文在商代车结构叙述后，对中西系驾法作出比较判断。",
  700, 700, "line", [700], ["b0076"], "夏商周时期的艺术设计", "3. 交通运输工具的设计规范 / 1）车")

C("cand-01-82", "factual_claim",
  "夏燕靖据甲骨文字形与《说文》“象舟之旋”的释义指出，这是关于舵桨的最早记载，说明商代已能制造控制方向的舵桨。",
  "On the evidence of oracle-bone graphs and the Shuowen gloss “images the turning of a boat,” Xia Yanjing identifies this as the earliest record of a steering oar, showing that the Shang could already make devices for controlling a boat's direction.",
  "medium",
  ["04-knowledge/units/terms/lu-oar.md", "04-knowledge/units/terms/plank-boat.md"],
  "原文由甲骨文字形与《说文》释义推出“最早记载”和商代已有舵桨的判断。",
  712, 712, "line", [712], ["b0077"], "夏商周时期的艺术设计", "3. 交通运输工具的设计规范 / 2）船")

C("cand-01-83", "historiographic_claim",
  "夏燕靖认为，夏商周时代以夯土墙和木构架为主体的建筑开始出现；夯土技术萌芽于新石器时代、至商代趋于成熟，木构架经商周不断改进，逐步发展成为我国古代建筑的主要结构形式，并出现前所未有的院落群组合。",
  "Xia Yanjing argues that buildings with rammed-earth walls and timber frames first appeared in the Xia-Shang-Zhou era: rammed-earth technique emerged in the Neolithic and matured by the Shang, while timber framing was progressively improved through Shang and Zhou until it became the principal structural form of Chinese architecture, with unprecedented courtyard complexes.",
  "high",
  ["04-knowledge/units/procedures/rammed-earth-board-construction.md"],
  "原文在“建筑设计与城建布局”节总述夯土与木构架的发展脉络。",
  723, 723, "line", [723], ["b0078", "b0079"], "夏商周时期的艺术设计", "4. 建筑设计与城建布局 / 1）建筑设计")

C("cand-01-85", "factual_claim",
  "夏燕靖指出，周代统治者把营建都邑即筑城看作立国之本，每个都邑都以城郭沟池为最基本的构筑；各都邑按封爵大小而建，王城方九里、公城方七里、侯伯城方五里、子男城方三里。",
  "Xia Yanjing shows that Zhou rulers regarded founding capitals—city building—as the basis of the state, each capital being constituted first of all by walls and moats; cities were built according to noble rank, with the royal city nine li square, ducal cities seven, marquis and earl cities five, and viscount and baron cities three.",
  "high",
  ["04-knowledge/units/terms/city-walls-and-moats.md"],
  "原文在“城建布局”节引“周之所封四百余，服国八百余”及城制等级，并作出“立国之本”的判断。",
  734, 734, "line", [734], ["b0080"], "夏商周时期的艺术设计", "4. 建筑设计与城建布局 / 2）城建布局")

C("cand-01-87", "factual_claim",
  "夏燕靖据《周礼》指出，周代有“染人”和“掌染草”等职业名称，表示从事印染和染料生产的人；《周礼·考工记》还记载了缫丝、漂白、晾丝等操作方法。",
  "Citing the Zhouli, Xia Yanjing notes that the Zhou had occupational titles such as “dyer” (ranren) and “dye-plant officer” (zhangrancao) for those engaged in dyeing and dye production, and that the Zhouli Kaogongji also records methods for reeling, bleaching and drying silk.",
  "high",
  ["04-knowledge/units/institutions/zhou-ranren-zhangrancao.md", "04-knowledge/units/procedures/sao-si-piaobai.md"],
  "知识链接引《周礼》说明周代印染职业与《考工记》所载丝织处理工序。",
  746, 746, "line", [746], ["b0083", "b0084"], "夏商周时期的艺术设计", "5. 丝纺织物与服饰艺术设计 / 知识链接：蚕示三牢")

C("cand-01-89", "interpretive_claim",
  "夏燕靖据先秦服饰资料指出，周代已采用深衣制，即在上衣下裳的基础上将上衣与围裙连接起来；这种形式成为我国历代服装的基本特征，近代男子的长衫、女子的旗袍、连衣裙都是深衣制的延续。",
  "On the evidence of pre-Qin dress materials, Xia Yanjing states that the Zhou had adopted the shenyi system, joining the upper garment to the skirt; this form became a basic feature of Chinese dress through the dynasties, and the modern men's long gown, women's qipao and one-piece dress all continue the shenyi system.",
  "medium",
  ["04-knowledge/units/terms/shenyi.md", "04-knowledge/units/terms/qipao.md"],
  "原文在说明深衣形制后，直接列举长衫、旗袍、连衣裙作为其延续。",
  750, 750, "line", [750], ["b0085"], "夏商周时期的艺术设计", "5. 丝纺织物与服饰艺术设计 / 2）服饰的制式与设计")


def main():
    assert len(ROWS) == 33, len(ROWS)
    ids = [f"claim-{i:04d}" for i in range(37, 70)]
    for row, cid in zip(ROWS, ids):
        row["claim_id"] = cid
    seen = set()
    for row in ROWS:
        assert row["claim_id"] not in seen
        seen.add(row["claim_id"])
        for path in row["supported_by"]:
            assert (ROOT / path).is_file(), path
    out = ROOT / "_zn_claim_xyj09a_rows.json"
    out.write_text(json.dumps(ROWS, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({
        "claims": len(ROWS),
        "with_support": sum(1 for r in ROWS if r["supported_by"]),
        "types": dict(Counter(r["claim_type"] for r in ROWS)),
        "confidence": dict(Counter(r["confidence"] for r in ROWS)),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
