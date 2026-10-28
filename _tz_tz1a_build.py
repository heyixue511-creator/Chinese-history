# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz1a (chapters 1-2, 30 claims)."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "内容介绍与第一章 原始社会的工艺美术"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"

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


def C(claim_id, cand, ctype, zh, en, supported, note, start, end, key_lines, section, chapter=CH):
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
                "chapter": chapter,
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
    "claim-0770", "cand-01-29", "evaluative_claim",
    "出版方称《中国工艺美术史》为国内第一部中国工艺美术史著作，是田自秉三十多年探索和研究的心血之作，也是研究中国工艺美术发展历程的权威著作。",
    "The publisher describes Zhongguo Gongyi Meishu Shi as the first history of Chinese arts and crafts in China, the fruit of Tian Zibing's more than thirty years of exploration and research, and an authoritative work on the development of Chinese arts and crafts.",
    [B + "tian-zizhu-zhongguo-gongyi-meishu-shi.md", B + "zhongguo-gongyi-meishu-shi-xiudingben.md", R + "tian-zizhu.md"],
    "断言语义取 L11“内容介绍”。“第一部”“权威著作”属出版方推介，未给同行评议、获奖或再版记录；同段“庞薰栗”疑为“庞薰琹”之讹。与 claim-0771 同段近邻，分论著作地位与内容范围，未合并。",
    11, 11, [11], "内容介绍"))

rows.append(C(
    "claim-0771", "cand-01-30", "factual_claim",
    "本书汇集和整理了我国自原始社会至20世纪80年代以来的工艺美术史料，系统阐述了工艺美术的历史沿革与发展，并分析了不同历史时期的艺术特色。",
    "The book collects and arranges Chinese arts-and-crafts materials from primitive society to the 1980s, systematically sets out the historical development of arts and crafts, and analyses the artistic characteristics of different periods.",
    [B + "tian-zizhu-zhongguo-gongyi-meishu-shi.md", B + "zhongguo-gongyi-meishu-shi-xiudingben.md", R + "tian-zizhu.md", T + "gongyi-meishu.md"],
    "断言语义取 L11“内容介绍”，为出版方对本书范围的说明；未给章节结构、史料来源与图版统计。与 claim-0770 同段近邻，未合并。",
    11, 11, [11], "内容介绍"))

rows.append(C(
    "claim-0772", "cand-01-31", "factual_claim",
    "距今约50万年前，北京房山周口店居住着“北京人”（或称“中国猿人”），他们生活在石灰岩山洞中，主要掌握石器和火两种征服自然的工具。",
    "About 500,000 years ago Peking Man, also called Sinanthropus, lived in limestone caves at Zhoukoudian in Fangshan, Beijing, and possessed two principal means of mastering nature: stone tools and fire.",
    [T + "beijingren.md", P + "zhoukoudian-site.md"],
    "断言语义取 L395。原文以“北京人”与“中国猿人”并称；周口店遗址年代与用火证据此后有新的测年与争论，本批按原文记录，未据新研究改写。与 claim-0773 同节近邻，分论旧石器早期与仰韶、河姆渡，未合并。",
    395, 395, [395], "第一节 概说"))

rows.append(C(
    "claim-0773", "cand-01-32", "factual_claim",
    "黄河流域的仰韶文化因最早发现于河南渑池仰韶村而得名；长江流域则有河姆渡文化。",
    "The Yangshao culture of the Yellow River basin is named after its first discovery at Yangshao village in Mianchi, Henan; the Yangtze basin has the Hemudu culture.",
    [T + "yangshao-culture.md", T + "hemudu-culture.md", P + "hemudu-site.md"],
    "断言语义取 L405。原文以流域对举两大文化；仰韶村首次发掘的年份与地层未展开。与 claim-0774 同段近邻，前者论命名与分布、后者论母系氏族繁荣，未合并。",
    405, 405, [405], "第一节 概说"))

rows.append(C(
    "claim-0774", "cand-01-33", "interpretive_claim",
    "黄河流域仰韶文化的半坡村遗址与长江流域河姆渡文化的河姆渡遗址，反映了原始社会母系氏族的繁荣阶段。",
    "The Banpo site of the Yangshao culture in the Yellow River basin and the Hemudu site of the Hemudu culture in the Yangtze basin reflect the flourishing stage of matrilineal clans in primitive society.",
    [P + "banpo-site.md", P + "hemudu-site.md", T + "yangshao-culture.md", T + "hemudu-culture.md"],
    "断言语义取 L405。母系氏族繁荣的判断依据聚落规模、房屋与墓葬，原文未给碳十四年代序列与墓葬统计。与 claim-0773 同段近邻，未合并。",
    405, 405, [405], "第一节 概说"))

rows.append(C(
    "claim-0775", "cand-01-35", "evaluative_claim",
    "彩陶的制作是半坡人重要的艺术成就，鱼纹和人面纹装饰具有鲜明的特色。",
    "The making of painted pottery was an important artistic achievement of the Banpo people, and its fish and human-face motifs are distinctive.",
    [T + "caihui-tao.md", T + "banpo-xing-caitao.md", W + "renmian-yuwen-caitao-pen.md"],
    "断言语义取 L409。鱼纹与人面纹的组合含义有图腾说、巫术说等不同解释，原文未展开；本批只记录作者的评价。与 claim-0785 同章近邻，前者论艺术成就、后者论鱼纹演变，未合并。",
    409, 409, [409], "第一节 概说"))

rows.append(C(
    "claim-0776", "cand-01-34", "interpretive_claim",
    "在此之前，人们对自然材料的工艺加工只是改变其外在形状；制陶则通过火的应用，使泥土改变其内在性质。",
    "Earlier craft working of natural materials changed only their external shape; pottery making, through the use of fire, changed the internal nature of clay.",
    [T + "taoqi.md", T + "taoyao.md"],
    "断言语义取 L413。属技术史判断；“内在性质”指粘土经火烧结的物理化学变化，原文未给烧成温度与矿物分析。与 claim-0777 同段近邻，分论制陶的技术意义与社会意义，未合并。",
    413, 413, [413], "第一节 概说"))

rows.append(C(
    "claim-0777", "cand-01-39", "evaluative_claim",
    "制陶工艺是母系氏族社会手工业的重要组成部分，也是氏族社会形成后的一项重要成就；这时的制陶不只求合于实用，而且体现了对美的要求。",
    "Pottery making was an important part of handicraft in matrilineal clan society and a major achievement after the formation of clan society; it sought not only practical fitness but also the requirements of beauty.",
    [T + "taoqi.md", T + "caihui-tao.md"],
    "断言语义取 L413。评价性表述；原文以化妆土、彩画、刻镂、堆贴等装饰为据，未给器物组合与使用场景统计。与 claim-0776 同段近邻，未合并。",
    413, 413, [413], "第一节 概说"))

rows.append(C(
    "claim-0778", "cand-01-36", "synthetic_claim",
    "从母系氏族社会向父系氏族社会转化，已发现的有淮海地区的大汶口文化、长江中下游的青莲冈文化和屈家岭文化、长江上游的大溪文化等。",
    "Evidence for the transition from matrilineal to patrilineal clan society includes the Dawenkou culture in the Huai-Hai region, the Qingliangang and Qujialing cultures in the middle and lower Yangtze, and the Daxi culture in the upper Yangtze.",
    [T + "dawenkou-culture.md", T + "qujialing-wenhua.md"],
    "断言语义取 L415。“青莲冈”通行作“青莲岗”，大溪文化库内无独立条目；“淮海地区”为原文的地理表述。综合判断，未给各文化的年代序列与墓葬证据。",
    415, 415, [415], "第一节 概说"))

rows.append(C(
    "claim-0779", "cand-01-37", "factual_claim",
    "进入父系氏族社会后，黄河中下游产生了龙山文化，因最早发现于山东历城龙山镇而得名；河南庙底沟二期和后冈二期称河南龙山文化，客省庄二期称陕西龙山文化；长江流域苏南浙北地区则有良渚文化。",
    "With the rise of patrilineal clan society the Longshan culture emerged in the middle and lower Yellow River, named after its first discovery at Longshan town in Licheng, Shandong. The Miaodigou II and Hougang II phases in Henan are called Henan Longshan, the Keshengzhuang II phase Shaanxi Longshan, and the Liangzhu culture occupied southern Jiangsu and northern Zhejiang.",
    [T + "longshan-culture.md", T + "liangzhu-culture.md"],
    "断言语义取 L417。类型划分按原文；庙底沟二期属龙山早期，与庙底沟型彩陶不同，未混用条目。与 claim-0794 同章近邻，前者论类型与分布、后者论文化分期，未合并。",
    417, 417, [417], "第一节 概说"))

rows.append(C(
    "claim-0780", "cand-02-54", "factual_claim",
    "父系氏族社会的制陶技术更为提高，封窑技术和轮制是突出成就；烧制时严密封窑使陶坯中的铁元素还原，制成硬度较高的灰陶，并能通过控制烧制末期的窑内空气和温度制成黑陶。",
    "Pottery technology improved further in patrilineal clan society, with kiln sealing and the potter's wheel as outstanding achievements; sealing the kiln reduced iron in the clay to produce harder grey pottery, and controlling the kiln atmosphere and temperature at the end of firing produced black pottery.",
    [T + "taolun.md", T + "taoyao.md", T + "heitao.md", T + "danke-heitao.md"],
    "断言语义取 L419-L421。技术叙述按原文；未给烧成温度曲线与还原气氛的检测数据。与 claim-0795 同章近邻，前者论技术条件、后者论早期龙山陶器特征，未合并。",
    419, 421, [419], "第一节 概说"))

rows.append(C(
    "claim-0781", "cand-02-55", "historiographic_claim",
    "祖国各地的远古工艺文化具有各自特色：北方仰韶文化的彩陶发达，南方河姆渡文化的雕塑出色，东部龙山文化的黑陶以造型取胜；大量考古发掘改变了过去认为只有黄河流域才是中华民族文化摇篮的传统说法。",
    "Remote antiquity's craft cultures had regional characters: Yangshao in the north excelled in painted pottery, Hemudu in the south in sculpture, and Longshan in the east in black-pottery forms. Extensive excavation has overturned the traditional view that the Yellow River basin alone was the cradle of Chinese culture.",
    [T + "yangshao-culture.md", T + "hemudu-culture.md", T + "longshan-culture.md"],
    "断言语义取 L423。属史学史判断；“文化摇篮”说法的转变未给具体考古发现、年代与学者论述。与 claim-0779 同节近邻，分论区域特色与史学观念，未合并。",
    423, 423, [423], "第一节 概说"))

rows.append(C(
    "claim-0782", "cand-02-56", "interpretive_claim",
    "山顶洞人把石块、骨片、兽牙、海贝等制成装饰品，有的还染成红色加以美化；这些装饰品可以说是我国最早的工艺品。在生产力极低的社会里，这种爱美的表现往往具有宗教意义，审美的功利性高于艺术性。",
    "Upper Cave people made ornaments from stone, bone, animal teeth and sea shells, some dyed red; these ornaments may be called China's earliest craft objects. In a society with extremely low productive forces such display of beauty often carried religious meaning, and the utilitarian aspect of aesthetics took precedence over artistry.",
    [T + "shandingdong-ren-guzhen.md", P + "zhoukoudian-site.md"],
    "断言语义取 L439、L443。“最早的工艺品”与“审美的功利性高于艺术性”均为作者的判断；山顶洞人年代原文未给测年数据。与 claim-0799 同章近邻，前者论装饰品与审美、后者论骨针与缝纫，未合并。",
    439, 443, [439, 443], "第二节 装饰的萌芽"))

rows.append(C(
    "claim-0783", "cand-02-57", "interpretive_claim",
    "石器和玉器有直接联系，玉器工艺由石器工艺发展演变而来：玉圭由石斧演变，玉璧由环状石斧演变，玉璋由石刀演变。",
    "Stone and jade implements are directly related, jade working having evolved from stone working: the jade gui tablet from the stone axe, the bi disc from the ring-shaped stone axe, and the zhang blade from the stone knife.",
    [T + "gui.md", T + "bi.md"],
    "断言语义取 L463。演变链属作者的类型学推断；原文未给器形测量与出土层位对照。玉璋库内无独立条目，未强行链接。与 claim-0782 同节近邻，分论装饰品与玉器源流，未合并。",
    463, 463, [463], "第三节 石器工艺"))

rows.append(C(
    "claim-0784", "cand-02-58", "factual_claim",
    "1962年在江西万年县仙人洞出土了距今8000多年的陶器，是我国目前发现的最早的陶器资料。",
    "Pottery dating to more than 8,000 years ago was unearthed in 1962 at Xianrendong in Wannian county, Jiangxi, and is the earliest pottery material so far found in China.",
    [P + "xianrendong-site.md", T + "taoqi.md"],
    "断言语义取 L484。按原文记录；仙人洞陶器此后已有约2万年前的测年报道，本批不改写原文，证据层复核时需注意年代更新。与 claim-0785 同节近邻，分论陶器起源与鱼纹演变，未合并。",
    484, 484, [484], "第四节 陶器工艺 一、彩陶"))

rows.append(C(
    "claim-0785", "cand-02-59", "interpretive_claim",
    "半坡型彩陶的鱼纹由写实手法逐渐演变为鱼体的分割与重新组合，走向抽象化、几何化、样式化，形成横式直边三角形与线纹组成的装饰图案。",
    "The fish motif of Banpo painted pottery evolved from realistic depiction to the division and recombination of the fish body, becoming abstract, geometric and stylised, and forming decorative patterns of horizontal straight-sided triangles and linear ornament.",
    [T + "banpo-xing-caitao.md", W + "renmian-yuwen-caitao-pen.md"],
    "断言语义取 L519。演变序列据器物排比；原文未给分期标尺与统计样本。与 claim-0775 同章近邻，前者论鱼纹演变、后者论半坡艺术成就，未合并。",
    519, 519, [519], "第四节 陶器工艺 一、彩陶"))

rows.append(C(
    "claim-0786", "cand-02-60", "factual_claim",
    "庙底沟型彩陶是在半坡型基础上发展起来的；庙底沟型陶器中的彩陶比半坡型增多，约占10%~15%，黑白双关是其纹饰特色。",
    "Miaodigou painted pottery developed from the Banpo type; painted wares increased to about 10-15 per cent of Miaodigou pottery, and black-and-white double-reading is its distinctive decorative feature.",
    [T + "miaodigou-xing-caitao.md", T + "shuangguan-fa.md"],
    "断言语义取 L554、L558。10%~15%为原文估值，未注统计口径与样本量；黑白双关的解释见 claim-0792。与 claim-0787 同节近邻，分论庙底沟型与马家窑型，未合并。",
    550, 558, [554, 558], "第四节 陶器工艺 一、彩陶 2. 庙底沟型"))

rows.append(C(
    "claim-0787", "cand-02-61", "historiographic_claim",
    "马家窑型彩陶晚于半坡型和庙底沟型，根据出土地层分析，它是由庙底沟型发展和分化出来的；其艺术风格可用旋动、流畅来形容。",
    "Majiayao painted pottery postdates the Banpo and Miaodigou types and, on stratigraphic evidence, developed and differentiated from the Miaodigou type; its style may be described as swirling and fluent.",
    [T + "majiayao-xing-caitao.md", T + "majiayao-culture.md"],
    "断言语义取 L568、L585。年代关系据地层与类型排比，未给碳十四数据；“旋动、流畅”为风格评价。与 claim-0786 同节近邻，未合并。",
    568, 585, [568, 585], "第四节 陶器工艺 一、彩陶 3. 马家窑型"))

rows.append(C(
    "claim-0788", "cand-02-62", "evaluative_claim",
    "半山型彩陶从造型和装饰上说，是彩陶工艺中最为精美的；它精巧繁密、饱满凝重，艺术风格可用富丽、精巧来形容。",
    "In form and ornament Banshan painted pottery is the most refined of painted-pottery wares: delicate and dense, full and grave, its style may be described as sumptuous and exquisite.",
    [T + "banshan-xing-caitao.md"],
    "断言语义取 L591。“最为精美”属评价；原文以锯齿纹、红黑相间与壶体比例为例，未给类型学量化比较。与 claim-0789 同节近邻，分论半山型与马厂型，未合并。",
    591, 591, [591], "第四节 陶器工艺 一、彩陶 4. 半山型"))

rows.append(C(
    "claim-0789", "cand-02-63", "evaluative_claim",
    "马厂型彩陶保持半山型的制作特色并有新的发展，但总体已渐趋衰落；其装饰不及半山型精致，显得粗犷、庄重、豪放，艺术风格可用简练、刚劲来形容。",
    "Machang painted pottery retained Banshan features and developed them further, but on the whole declined; its ornament is less refined than Banshan's, appearing rough, grave and unrestrained, and its style may be described as concise and vigorous.",
    [T + "machang-xing-caitao.md"],
    "断言语义取 L610-L641。“渐趋衰落”为作者的艺术评价，非产量或聚落规模证据；原文以人形纹简化、四大圈纹与陶衣为例。与 claim-0788 同节近邻，未合并。",
    610, 641, [641], "第四节 陶器工艺 一、彩陶 5. 马厂型"))

rows.append(C(
    "claim-0790", "cand-02-70", "interpretive_claim",
    "彩陶的装饰位置一般与器皿的使用条件相适应：罐多饰于肩部，钵多饰于内侧，注意视线的接触面；装饰布局已注意从不同视角体现完整效果。",
    "The placement of painted decoration generally suited the vessel's use: jars were decorated on the shoulder, bowls on the interior, attending to the line of sight; layout already considered complete effect from different viewing angles.",
    [T + "caihui-tao.md", T + "duoxiao-zhuangshi-fa.md"],
    "断言语义取 L645-L649。属设计分析；原文以罐、钵与俯视、侧视效果为例，未给使用者行为观察或实验数据。与 claim-0792 同节近邻，分论装饰位置与双关法，未合并。",
    645, 649, [645], "第四节 陶器工艺 一、彩陶 6. 彩陶的装饰艺术"))

rows.append(C(
    "claim-0791", "cand-02-64", "synthetic_claim",
    "彩陶装饰基本上以几何纹形式出现，其产生主要有四方面原因：编织的模拟、劳动的节奏感、图腾的表号化、自然物的抽象化。",
    "Painted-pottery ornament is basically geometric; its emergence is attributed to four causes: imitation of weaving, the rhythm of labour, the emblemisation of totems, and the abstraction of natural forms.",
    [T + "caihui-tao.md"],
    "断言语义取 L653-L661。四因为作者的归纳，属发生学解释；编织说引恩格斯《家庭、私有制和国家的起源》，其余三因未注出处。与 claim-0790 同节近邻，未合并。",
    653, 661, [653], "第四节 陶器工艺 一、彩陶 6. 彩陶的装饰艺术"))

rows.append(C(
    "claim-0792", "cand-02-65", "interpretive_claim",
    "彩陶的双关法与欧美近代流行的欧普美术（色效应美术）有相似之处，表明早在六七千年前我国彩陶装饰已运用视幻觉原理，产生变幻多端的艺术效果。",
    "The double-reading method of painted pottery resembles Op art, or colour-effect art, popular in the modern West, showing that six or seven thousand years ago Chinese painted-pottery ornament already used optical illusion to produce changing effects.",
    [T + "shuangguan-fa.md", T + "caihui-tao.md"],
    "断言语义取 L682-L684。跨时代类比属作者的比较判断；欧普美术为20世纪概念，原文未给知觉实验或形式分析数据。与 claim-0791 同节近邻，分论双关法与几何纹成因，未合并。",
    682, 684, [684], "第四节 陶器工艺 一、彩陶 6. 彩陶的装饰艺术"))

rows.append(C(
    "claim-0793", "cand-02-72", "synthetic_claim",
    "彩陶艺术特点比较表将半坡型、庙底沟型、马家窑型、半山型、马厂型的造型、装饰、表现手法、艺术风格与距今年代并列：半坡型约7000~6000年前，庙底沟型约6000~5000年前，马家窑型约5000年前，半山型约4500年前，马厂型约4000年前。",
    "The comparative table of painted-pottery characteristics sets out form, ornament, technique, style and approximate date for the Banpo, Miaodigou, Majiayao, Banshan and Machang types: Banpo c. 7000-6000 BP, Miaodigou c. 6000-5000 BP, Majiayao c. 5000 BP, Banshan c. 4500 BP and Machang c. 4000 BP.",
    [T + "banpo-xing-caitao.md", T + "miaodigou-xing-caitao.md", T + "majiayao-xing-caitao.md", T + "banshan-xing-caitao.md", T + "machang-xing-caitao.md"],
    "断言语义取 L721-L726 的比较表。表列年代为约数，未注测年方法；“距今年代”与考古学文化分期可能存在口径差异。与 claim-0788、0789 同章近邻，未合并。",
    721, 726, [724, 726], "第四节 陶器工艺 一、彩陶 6. 彩陶的装饰艺术"))

rows.append(C(
    "claim-0794", "cand-02-69", "historiographic_claim",
    "龙山文化和仰韶文化是历史发展的前后不同阶段。",
    "The Longshan and Yangshao cultures represent successive stages of historical development.",
    [T + "longshan-culture.md", T + "yangshao-culture.md"],
    "断言语义取 L732。属文化分期判断；原文随后以分布范围与陶器类型展开，未给地层叠压或测年序列。与 claim-0779 同章近邻，前者论文化分期、后者论类型与分布，未合并。",
    732, 732, [732], "第四节 陶器工艺 二、黑陶"))

rows.append(C(
    "claim-0795", "cand-02-74", "factual_claim",
    "早期龙山文化的陶器以泥条盘筑法为主，多为粗灰陶，纹饰以篮纹最多、绳纹次之；薄而光的蛋壳黑陶有少量发现，多为陶鼎和陶斝而无陶鬲，这是早期龙山文化的显著特征。",
    "Early Longshan pottery was mainly coil-built and largely coarse grey ware, with basket impressions most common and cord impressions next; a small quantity of thin, lustrous eggshell black pottery occurs, mostly ding and jia but no li, which is the distinctive feature of early Longshan.",
    [T + "longshan-culture.md", T + "heitao.md", T + "danke-heitao.md"],
    "断言语义取 L736。器物组合特征按原文；未给各遗址的陶片统计比例。与 claim-0780 同章近邻，分论制陶技术与早期龙山陶器，未合并。",
    736, 736, [736], "第四节 陶器工艺 二、黑陶"))

rows.append(C(
    "claim-0796", "cand-02-66", "evaluative_claim",
    "黑陶工艺具有黑、薄、光、纽四个特点；如果说彩陶工艺以彩绘装饰见长，黑陶工艺则以造型取胜。",
    "Black pottery is characterised by blackness, thinness, lustre and handles or knobs; whereas painted pottery excelled in painted ornament, black pottery excelled in form.",
    [T + "heitao.md", T + "danke-heitao.md"],
    "断言语义取 L751-L753。四特点为作者归纳；“以造型取胜”属评价，原文以器类增多与附件丰富为据。与 claim-0795 同节近邻，未合并。",
    751, 753, [751], "第四节 陶器工艺 二、黑陶"))

rows.append(C(
    "claim-0797", "cand-02-67", "interpretive_claim",
    "鬶的造型从大汶口文化时期到龙山文化时期经历复杂演变，既逐渐走向形象化，又不断提高实用功能，体现了原始社会工艺制作者实用与美观有机结合的设计思想。",
    "The gui tripod pourer underwent a complex evolution from the Dawenkou to the Longshan period, becoming more figural while steadily improving its practical function, embodying the primitive craftsman's design idea of combining use and beauty.",
    [T + "tao-gui.md", T + "dawenkou-culture.md", T + "longshan-culture.md"],
    "断言语义取 L763-L768。演变序列据器形排比；未给大汶口至龙山各期的标本数量与年代。“设计思想”为作者的阐释。与 claim-0796 同节近邻，分论鬶的演变与黑陶总体特点，未合并。",
    763, 768, [768], "第四节 陶器工艺 二、黑陶"))

rows.append(C(
    "claim-0798", "cand-02-68", "evaluative_claim",
    "几何印纹陶的几何纹连续反复，形成有规律的图案美，因此被誉为最优秀的东方沿海的古代文化。",
    "The repeated geometric impressions on geometric-stamped pottery form a regular patterned beauty, for which it has been praised as the finest ancient culture of the eastern seaboard.",
    [T + "geometric-stamped-pottery.md", T + "geometric-stamped-hard-pottery.md"],
    "断言语义取 L788。“最优秀”为引述性评价，原文未注评价者与比较范围；几何印纹陶下限晚至周汉，与文化命名的时间跨度需注意。",
    788, 788, [788], "第四节 陶器工艺 三、几何印纹陶"))

rows.append(C(
    "claim-0799", "cand-02-71", "interpretive_claim",
    "原始社会的染织处于萌芽状态；山顶洞人遗址出土的磨制骨针标志着人们已能缝制简单的衣服。",
    "Dyeing and weaving in primitive society were at a budding stage; the polished bone needle from the Upper Cave shows that people could already sew simple garments.",
    [T + "shandingdong-ren-guzhen.md", P + "zhoukoudian-site.md"],
    "断言语义取 L820。骨针只证明缝纫能力，不能直接证明纺织；原文同时引《墨子》《韩非子》说明以兽皮为衣。与 claim-0782 同章近邻，分论骨针与装饰品，未合并。",
    820, 820, [820], "第五节 其他工艺 二、染织"))

types = Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({p for r in rows for p in r["supported_by"]})
print(json.dumps({
    "claims": len(rows),
    "first": rows[0]["claim_id"],
    "last": rows[-1]["claim_id"],
    "types": dict(types),
    "links": links,
    "distinct": distinct,
}, ensure_ascii=False, indent=1))

(ROOT / "_tz_tz1a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_tz_tz1a_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")
print("written _tz_tz1a_rows.json / _tz_tz1a_patch.json")
