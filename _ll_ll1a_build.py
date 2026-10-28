# -*- coding: utf-8 -*-
"""Build 李立新 2011 claim rows, batch ll1a (绪言、上编导论与第一章导言, 36 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
SRC = "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"
DATE = "2026-10-27"
CH = "绪言、上编导论与第一章导言（设计史新视野、工艺史与设计史、设计史任务、大历史观与分期）"

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
    "claim-1048", "cand-01-03", "historiographic_claim",
    "有人误认为中国过去没有艺术设计，这种看法不仅割断了历史，也会造成无源之水，出现数典忘祖的现象。",
    "Some mistakenly believe that China had no art design in the past; such a view not only cuts off history but also leaves design without a source, amounting to forgetting one's own origins.",
    [T + "sheji.md", T + "yishu-sheji.md"],
    "断言语义取 L88（代序）。原文所批评的是“中国过去没有艺术设计”的判断，claim 保留批评对象，不把“误认为”的主体具体化。",
    88, 88, [88], "设计史新视野（代序）"))

rows.append(C(
    "claim-1049", "cand-01-09", "interpretive_claim",
    "“设计”一词作为造物活动的专用词汇存在两方面问题：其内涵过于广泛，几乎涉及人的行为活动的所有方面；又将造物活动看成单项因素的作用，难以说明造物活动的结构特性与形成过程。“工业设计”虽缩小了范围，但依然含糊不清，且作为大工业生产的产物容易将传统造物设计排除在外。",
    "As a term for making, design has two problems: its scope is so broad that it covers almost every aspect of human activity, and it treats making as the effect of a single factor, making it hard to explain the structural character and formation of making. Industrial design narrows the scope but remains vague and, as a product of large-scale industry, tends to exclude traditional design.",
    [T + "sheji.md", T + "yishu-sheji.md", T + "xiandai-gongyi.md"],
    "断言语义取 L173-L175。原文由“设计”而“工业设计”逐层限定，claim 保留两层批评；“单项因素”指原文对造物活动解释方式的判断。",
    173, 175, [173, 175], "绪言 一、关于研究的主题与研究范围"))

rows.append(C(
    "claim-1050", "cand-01-10", "evaluative_claim",
    "过去那种把设计艺术排斥在艺术之外的看法与做法是偏颇的，甚至是错误的或无知的；设计艺术应作为艺术世界系统整体中的一个分支系统来建构。",
    "The past view and practice of excluding design art from art is biased, even mistaken or ignorant; design art should be constructed as a branch system within the whole system of the art world.",
    [T + "yishu-sheji.md", T + "yishu-shejishi.md"],
    "断言语义取 L177。评价强度按原文保留“偏颇—错误—无知”三级；“艺术世界”为原文术语，未改译为“艺术界”。",
    177, 177, [177], "绪言 一、关于研究的主题与研究范围"))

rows.append(C(
    "claim-1051", "cand-01-14", "historiographic_claim",
    "设计艺术史研究无论在国内或国外，都还是一门前沿性的、未曾建立的学科分支，国内尤为薄弱，几乎是一个空白。",
    "Design-art history is, at home and abroad, still a frontier branch not yet established, and in China it is especially weak, almost a blank.",
    [T + "yishu-shejishi.md", T + "sheji.md"],
    "断言语义取 L192。属作者对学科状况的判断，未列文献计量或机构调查；“几乎是一个空白”为评价性强度，claim 保留。",
    192, 192, [192], "绪言 一、关于研究的主题与研究范围"))

rows.append(C(
    "claim-1052", "cand-01-15", "evaluative_claim",
    "具有悠久历史、连绵不断发展的中国造物设计艺术，在世界设计艺术史上不能不说是一个举世无双的成功典范。",
    "China's craft design, with its long history and continuous development, must be called an unparalleled model of success in world design history.",
    [T + "chuantong-sheji.md", T + "gongyi-meishu.md"],
    "断言语义取 L202。“举世无双”为作者评价，未给跨文明比较的指标体系；claim 保留原文评价强度。",
    202, 202, [202], "绪言 一、关于研究的主题与研究范围"))

rows.append(C(
    "claim-1053", "cand-01-19", "historiographic_claim",
    "20世纪一百年间有三次大的名称改动：图案—工艺美术—设计艺术；三个名称代表三个不同阶段，其演变意味着认识角度的转换，而基本内涵没有根本性差别。",
    "The twentieth century saw three major changes of name: pattern, arts and crafts, design art; the three names represent three stages, and their succession marks a shift of viewpoint rather than a fundamental change of content.",
    [T + "gongyi-meishu.md", T + "yishu-sheji.md", T + "sheji.md"],
    "断言语义取 L219-L221。原文将三次改名与“认识角度转换”相连，claim 保留“基本内涵没有根本性差别”的判断，不扩及学科目录变动的具体年份。",
    219, 221, [219, 221], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1054", "cand-01-20", "historiographic_claim",
    "工艺与设计之间没有特别清晰的界限：设计离开工艺制作只是纸上谈兵，工艺没有设计规划也缺少依据；但二者又有一定区别，工艺史与设计史存在不同分野。",
    "There is no sharply clear boundary between craft and design: design without craft production is merely paper planning, and craft without design planning lacks a basis; yet the two differ, and craft history and design history have distinct fields.",
    [T + "gongyi-meishu.md", T + "yishu-sheji.md"],
    "断言语义取 L223。原文先讲一体、再讲分野，claim 保留这一转折结构，不把二者合并为同一学科。",
    223, 223, [223], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1055", "cand-01-27", "historiographic_claim",
    "设计史不可能脱离工艺史而独立存在；工艺史关注的材料、工艺等问题是设计史不可忽略的因素，设计离开材料工艺的支撑将失去物化的可能，离开工艺史的设计史无法说清中国造物艺术的历史。",
    "Design history cannot exist independently of craft history; the materials and techniques that concern craft history are indispensable to design history, design without material and technical support cannot be realized, and design history apart from craft history cannot explain the history of Chinese making.",
    [T + "gongyi-meishu.md", T + "yishu-shejishi.md"],
    "断言语义取 L225-L246。原文以“首先”引出设计史对工艺史的依赖，claim 取该段主论点，不重复其后对工艺史著作的批评。",
    225, 246, [225, 246], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1056", "cand-01-29", "interpretive_claim",
    "材料的多样性带来造物设计的多样化，从自然材料到复合材料的发展直接促进了人类造物设计的发展与变迁；青铜、高分子复合材料、半导体材料等分别催生了新的设计语言、方法与形式。",
    "The diversity of materials produces diversity in design; the development from natural to composite materials has directly driven the development and change of human making, as bronze, polymer composites and semiconductor materials each generated new design languages, methods and forms.",
    [T + "sheji.md", T + "chuantong-sheji.md"],
    "断言语义取 L236。原文以青铜、玻璃钢与塑料、半导体三例证成材料—设计关系，claim 概括其因果链，不把例证当作全部材料史。",
    236, 236, [236], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1057", "cand-01-32", "evaluative_claim",
    "工艺史研究仍处在相当落后的状态，远不能适应现代教学需要；迄今所做大多只是对造物发展外在表象的、孤立的、断续的描述，尚未对整个中国造物历史或一般造物历史作内在逻辑的统贯而完整的把握。",
    "Craft-history research remains quite backward and far from meeting modern teaching needs; most work so far gives external, isolated and discontinuous descriptions of making and has not achieved a coherent, complete grasp of the internal logic of Chinese or general craft history.",
    [T + "gongyi-meishu.md", T + "yishu-shejishi.md"],
    "断言语义取 L248。“相当落后”“大多只是”为作者评价，未附抽样或统计；claim 保留原文对研究现状的判断。",
    248, 248, [248], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1058", "cand-01-33", "evaluative_claim",
    "近二十年有影响的与无影响的工艺通史、专史多因教学讲义而格式标准化，甚少各自特点，更少新概念、范畴与命题；其共同趋势是时代—产品—评论三段式，论述工艺美术成为对历史时代的说明，这是许多工艺史面目酷肖、似曾相识的原因。",
    "Craft histories and monographs of the past two decades, influential or not, tend to follow a standardized lecture-note format with few individual features and few new concepts, categories or propositions; their common pattern is period-product-commentary, making craft history an explanation of historical periods, which is why many such histories look alike.",
    [T + "gongyi-meishu.md", T + "yishu-shejishi.md"],
    "断言语义取 L254。原文把“三段式”归因于教学讲义体制，claim 保留这一制度性解释；“近二十年”以作者写作时点为基准，未换算为绝对年份。",
    254, 254, [254], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1059", "cand-01-36", "interpretive_claim",
    "一个造物品类的诞生、成长、繁盛、消亡并不与时代或朝代同步；造物被社会认识并应用于实际生活首先是因为它是产品，产品的更迭有其内在机制，时代的影响并不是主要的。",
    "The birth, growth, flourishing and disappearance of a category of made things do not synchronize with periods or dynasties; a made thing is socially recognized and applied first as a product, and product succession has its own internal mechanism, with period influence not the main factor.",
    [T + "sheji.md", T + "chuantong-sheji.md"],
    "断言语义取 L262。“时代的影响并不是主要的”为作者对产品更迭机制的判断，claim 保留其相对化表述，不改为“无关”。",
    262, 262, [262], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1060", "cand-01-37", "historiographic_claim",
    "既有的工艺史以经典的、宫廷的、陈设的、为权贵阶层服务的少数工艺品为研究对象，忽视了大量为普通民众服务的日用品；设计史研究应从“中心”转向“边缘”，从“经典”转向“一般”，从“宫廷”转向“民间”，从“陈设”转向“生活”。",
    "Existing craft history studies the few classic, courtly, display-oriented objects made for the elite and neglects the many daily goods made for ordinary people; design history should shift from centre to margin, classic to ordinary, court to folk, display to life.",
    [T + "gongyi-meishu.md", T + "chuantong-sheji.md"],
    "断言语义取 L264（并见 L7 扉页题解）。原文以四组对立概括研究对象的转移，claim 保留四组方向，不把“边缘”具体化为某一社会阶层。",
    264, 264, [264], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1061", "cand-01-38", "historiographic_claim",
    "设计史应着眼于造物的全过程：忽视制造、生产前的需求和计划，设计史只能是技术制造史；忽视技术、工艺这一造物后过程，设计史也只是设计方案规划史；理想的设计史是设想与制作、计划与工艺相互制约下的完善，并重视人在造物过程中的主体作用。",
    "Design history should cover the whole process of making: without the pre-production stages of demand and planning it becomes only a history of technical manufacture; without the post-production stage of technique and craft it becomes only a history of design schemes; the ideal design history is one of mutual constraint between conception and making, planning and craft, attentive to human agency in making.",
    [T + "sheji.md", T + "gongyi-meishu.md"],
    "断言语义取 L266-L271。原文以两个“如果忽视”构成正反论证，claim 保留双向条件，不把设计史等同于任一阶段史。",
    266, 271, [266, 271], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1062", "cand-01-40", "historiographic_claim",
    "设计史是一个边界不定的研究领域，需要社会史、政治史、经济史、文化史、宗教史、工艺史等为其营建叙述背景，也需要在宏观把握中对文献、实物等细微处做扎实的统计。",
    "Design history is a field with unsettled boundaries; it needs social, political, economic, cultural, religious and craft history to provide narrative context, and it also needs solid statistics on documents and objects within a macro grasp.",
    [T + "sheji.md", T + "yishu-shejishi.md"],
    "断言语义取 L275。原文同时强调“边界不定”与“背景学科”，claim 保留开放性定义，不把设计史列为任一背景学科的附庸。",
    275, 275, [275], "绪言 二、工艺史与设计史"))

rows.append(C(
    "claim-1063", "cand-01-41", "historiographic_claim",
    "为避免落入主客观认识论的陷阱，研究应贯彻四项原则：整体性把握造物历史；加强寻因、寻根意识以实现理论创造；建立设计艺术发展的逻辑结构；从民族文化与心理结构角度把握中国设计艺术史的进程。",
    "To avoid the trap of subject-object epistemology, research should follow four principles: grasp the history of making as a whole; strengthen causal and root-seeking inquiry for theoretical creation; establish a logical structure of design-art development; and grasp the course of Chinese design-art history through national culture and psychological structure.",
    [T + "yishu-shejishi.md", T + "minzu-wenhua-xinli-jiegou.md"],
    "断言语义取 L281。四项原则为作者自述的方法论纲领，claim 逐项保留，不评价其可操作性。",
    281, 281, [281], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1064", "cand-01-44", "historiographic_claim",
    "设计史研究不能脱离大的历史研究背景，但“史学就是史料学”不能变味为“史料就是史学”，使设计史仅仅成为史料的堆积；史料是设计历史的第一重存在，离开史料研究就没有客观基础。",
    "Design-history research cannot be separated from the wider historical research context, but the dictum that history is the science of sources must not turn into sources being history, reducing design history to a pile of sources; sources are the first order of design history, without which research has no objective basis.",
    [T + "yishu-shejishi.md", T + "sheji.md"],
    "断言语义取 L293。原文先承认史料的基础地位，再反对史料堆砌，claim 保留两层，不把作者误读为轻视史料。",
    293, 293, [293], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1065", "cand-01-47", "historiographic_claim",
    "只看到设计历史的第一重存在，不认识第一重存在必须通过人认识历史的第二重存在而存在，就会出现一个与任何认识主体无关的绝对客观的设计“历史”；这种绝对客观的历史实际上做不到。",
    "To see only the first order of design history and not recognize that it exists through the second order of human historical understanding produces an absolutely objective design history independent of any knowing subject; such absolute objectivity is in fact unattainable.",
    [T + "yishu-shejishi.md", T + "sheji.md"],
    "断言语义取 L295-L301。原文以“第一重存在/第二重存在”区分史料与史学认识，claim 保留这一术语，不简化为“客观/主观”二分。",
    295, 301, [295, 301], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1066", "cand-01-51", "interpretive_claim",
    "春秋战国是造物设计全面繁荣的时期，原始性、神秘性在造物设计中大大衰退，人性化设计开始抬头；汉代造物则表现出恢弘的格局与博大的气势，世俗的、生活的、现实的东西大量涌现。",
    "The Spring and Autumn and Warring States period was one of all-round flourishing in design: the primitive and the mysterious receded greatly and humanized design began to rise; Han making showed a grand scale and broad spirit, with secular, everyday and realistic elements appearing in abundance.",
    [T + "chunqiu-zhanguo.md", T + "yishu-shejishi.md"],
    "断言语义取 L315。两个时代的风格判断为作者举例，未给器物序列或统计；claim 保留“开始抬头”的渐进语气。",
    315, 315, [315], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1067", "cand-01-54", "historiographic_claim",
    "造物历史的进程与一个民族的文化—心理结构的发展过程相一致；中国造物设计在制度、形式、装饰、思想、发展、走向等方面都有迥异于西方的历史殊象，若不从民族文化与心理结构角度把握，就很难懂得这一进程最深的底蕴。",
    "The course of making is consistent with the development of a nation's cultural-psychological structure; Chinese design differs from the West in institutions, forms, decoration, thought, development and direction, and without grasping it through national culture and psychological structure one cannot understand the deepest content of that course.",
    [T + "minzu-wenhua-xinli-jiegou.md", T + "chuantong-sheji.md"],
    "断言语义取 L323-L330。原文引费正清“以中国看中国”并批评机械套用“图腾”概念，claim 取主命题，不展开引文。",
    323, 330, [323, 330], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1068", "cand-01-61", "evaluative_claim",
    "从世界艺术史的观察视角看，中国设计艺术史应是工业革命前世界造物艺术史上最完整也是最成功的范例。",
    "From the perspective of world art history, Chinese design art is arguably the most complete and most successful example in the history of world making before the Industrial Revolution.",
    [T + "chuantong-sheji.md", T + "yishu-shejishi.md"],
    "断言语义取 L352。“应是”保留原文推测语气；“工业革命前”为限定范围，claim 不扩及现代设计。",
    352, 352, [352], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1069", "cand-01-62", "interpretive_claim",
    "中国设计艺术的历史是一个延续的历史，而西亚、印度、埃及、希腊以及美洲玛雅的造物设计都有一次或多次的断裂过程。",
    "Chinese design art has a continuous history, whereas the design traditions of West Asia, India, Egypt, Greece and Maya America underwent one or more ruptures.",
    [T + "chuantong-sheji.md", T + "yishu-shejishi.md"],
    "断言语义取 L352。“断裂”未在原文定义，claim 保留原词，不代为判定各文明断裂的性质与程度。",
    352, 352, [352], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1070", "cand-01-63", "evaluative_claim",
    "艺术的范畴应包含所有的人造物品，而不仅仅是那些无用的、美丽的和富有诗意的东西；将艺术强分尊卑是人为的文化偏见。",
    "The category of art should include all human-made objects, not only useless, beautiful and poetic things; arbitrarily ranking arts as superior and inferior is a cultural prejudice.",
    [T + "yishu-sheji.md", T + "yishu-shejishi.md"],
    "断言语义取 L352。原文以两条脚注支撑“艺术范畴”与“文化偏见”的判断，claim 未展开脚注文献。",
    352, 352, [352], "绪言 三、设计史的任务及其研究意义"))

rows.append(C(
    "claim-1071", "cand-01-65", "historiographic_claim",
    "有人以中国古代只有“手工艺”而没有“设计”，这种将造物历史一截二段的认识会造成古代造物只重技艺而缺乏设计的误解；从起源与基本特征看，古代中国造物具有明显特殊的设计艺术形态，因此“手工艺”与“设计”是认识方法的差异而不是时代概念。",
    "Some hold that ancient China had only handicraft and no design; this splitting of craft history into two misleads us into thinking ancient making valued technique but lacked design. In origin and basic features ancient Chinese making is a distinct design-art form, so handicraft and design are differences of approach, not period concepts.",
    [T + "chuantong-sheji.md", T + "xiandai-gongyi.md"],
    "断言语义取 L362。原文以“传统设计”与“现代设计”两相对应，claim 保留这一对概念，不把“手工艺”等同于前现代阶段。",
    362, 362, [362], "上编 一、大历史观下的造物设计发展"))

rows.append(C(
    "claim-1072", "cand-01-66", "interpretive_claim",
    "传统设计向现代设计的转变，是所有民族、国家或迟或早都必须经历的历史性跨越，除非中途夭折，如西亚、埃及、玛雅。",
    "The transition from traditional to modern design is a historical crossing that every people and country must undergo sooner or later, unless cut short, as in West Asia, Egypt and Maya.",
    [T + "chuantong-sheji.md", T + "xiandai-gongyi.md"],
    "断言语义取 L364。“除非中途夭折”为例外条件，claim 保留；原文未给“夭折”的判定标准。",
    364, 364, [364], "上编 一、大历史观下的造物设计发展"))

rows.append(C(
    "claim-1073", "cand-01-69", "historiographic_claim",
    "只有打通古代设计史与现代设计史、中国设计史与外国设计史以及工艺史与设计史，才能在互为参照的情况下描述中国设计艺术自身的特征。",
    "Only by connecting ancient and modern design history, Chinese and foreign design history, and craft history and design history can the features of Chinese design art be described through mutual reference.",
    [T + "yishu-shejishi.md", T + "chuantong-sheji.md"],
    "断言语义取 L364。原文以“大历史”方法提出三重打通，claim 保留三组关系，不把“打通”具体化为比较框架。",
    364, 364, [364], "上编 一、大历史观下的造物设计发展"))

rows.append(C(
    "claim-1074", "cand-01-70", "evaluative_claim",
    "宋代之后的设计再无以前那种意匠化局面，几乎被写实风格所垄断；宫廷画院促进书画高度发展，设计受工笔绘画影响，折枝纹替代对称格律式卷草纹，整体气韵丧失，写实性不断加强，刺绣、缂丝模仿绘画现象不乏其例，这股暗流使宋之后纹样设计越来越僵化、呆板。",
    "After the Song, design no longer had the earlier yi-jiang (craft-conception) character and was almost monopolized by realism; the court painting academy promoted painting, design was influenced by fine brushwork, broken-branch motifs replaced symmetrical scroll patterns, overall spirit was lost, realism intensified, and embroidery and kesi imitated painting—a hidden current that made post-Song pattern design increasingly rigid and dull.",
    [T + "yijianghua-sheji.md", T + "xieshixing-sheji.md"],
    "断言语义取 L368-L370。原文将这一判断归于张道一先生的提示，claim 保留作者转述关系；“暗流”为原文比喻。",
    368, 370, [368, 370], "上编 一、大历史观下的造物设计发展"))

rows.append(C(
    "claim-1075", "cand-01-71", "synthetic_claim",
    "宋之前是意匠化的设计，宋之后则倾向于写实性设计；这一转变使中国造物设计在整体上形成两种不同风格。",
    "Before the Song, design was yi-jiang (craft-conception) oriented; after the Song it tended toward realism, and this shift gave Chinese making two broadly different styles.",
    [T + "yijianghua-sheji.md", T + "xieshixing-sheji.md"],
    "断言语义取 L368-L384。跨度含风格判断与三期分期的依据，claim 只取风格二分，不重复三期框架。",
    368, 384, [368, 384], "上编 一、大历史观下的造物设计发展"))

rows.append(C(
    "claim-1076", "cand-01-74", "historiographic_claim",
    "过去的工艺史按历史朝代划分造物工艺的历史时段；设计史若也按王朝框架陈述，做成时代王朝、工艺造物、经济文化三板块，将会陷入社会发展史的机械教条模式。",
    "Past craft history periodized making by dynasty; if design history also follows the dynastic frame in three blocks of period, craft and economy-culture, it will fall into the mechanical dogma of social-development history.",
    [T + "yishu-shejishi.md", T + "sheji.md"],
    "断言语义取 L378。原文反对王朝框架，但同段承认设计史与时代、政治、社会、经济相关，claim 保留这一张力。",
    378, 378, [378], "上编 二、设计艺术历史分期的思考"))

rows.append(C(
    "claim-1077", "cand-01-78", "synthetic_claim",
    "本书以汉魏之际和宋元之间为两个大转折，将设计历史划分为三个时段：第一时段从原始社会至汉代，第二时段从魏晋至两宋，第三时段从元代至近代；三大块段与王朝更迭没有直接对应关系。",
    "The book takes the Han-Wei transition and the Song-Yuan transition as two great turning points and divides design history into three periods: prehistory to Han, Wei-Jin to the two Songs, and Yuan to modern times; these blocks do not correspond directly to dynastic succession.",
    [T + "yishu-shejishi.md", T + "chuantong-sheji.md"],
    "断言语义取 L382-L384。三期为作者自拟框架，claim 保留分期界限与“与王朝无直接对应”的声明。",
    382, 384, [382, 384], "上编 二、设计艺术历史分期的思考"))

rows.append(C(
    "claim-1078", "cand-01-81", "interpretive_claim",
    "世界各地最早、最有代表性的石器几乎无一例外由砾石制成，这反映出人类造物的“设计”意识与第一件石器同时产生；人类造物的功能、审美、观念、形式都为了适应人的需要，包括物质与精神两方面。",
    "The earliest and most representative stone tools worldwide are almost invariably made of cobbles, reflecting that the design consciousness of human making arose with the first stone tool; the functions, aesthetics, concepts and forms of making all answer human needs, material and spiritual.",
    [T + "sheji.md", T + "xinshiqi-shidai.md"],
    "断言语义取 L404。“几乎无一例外”为作者概括，未列石器样本；claim 保留这一强度，并保留“设计意识”加引号的原术语。",
    404, 404, [404], "第一章 造物起源与体系形成（导言）"))

rows.append(C(
    "claim-1079", "cand-01-82", "historiographic_claim",
    "20世纪20年代以来甘肃、河南、青海等地的一系列重大考古发现，使我们在讨论人类造物史时很难确信古籍记载的史料价值，只能把它们作为先民的集体性历史记忆来认识；这种“集体无意识”反映出黄帝之世的文物制度已经详备、文明已露曙光。",
    "Major archaeological discoveries in Gansu, Henan, Qinghai and elsewhere since the 1920s make it hard to trust ancient texts as historical sources for the history of making; they can only be understood as the collective historical memory of early people, a collective unconscious reflecting that the institutions of the Yellow Emperor's age were already elaborate and civilization had dawned.",
    [T + "yishu-shejishi.md", T + "xinshiqi-shidai.md"],
    "断言语义取 L396-L398。原文先列《淮南子》《世本》《路史》《墨子》诸说，再以考古发现质疑其史料价值，claim 取质疑结论，不逐一复述古籍。",
    396, 398, [396, 398], "第一章 造物起源与体系形成（导言）"))

rows.append(C(
    "claim-1080", "cand-01-83", "synthetic_claim",
    "历经春秋战国“轴心时代”的人性觉悟、造物设计的普遍多样性与造物思想的多元化，到一统天下的秦汉，各种变数集聚为“变数的总和”，由此奠定两千年中国设计艺术发展的坚实基础，确立中国造物文化的基本框架，逐步形成完整规范的中国造物设计艺术体系。",
    "After the axial-age awakening of the Spring and Autumn and Warring States, the general diversity of design and the pluralism of craft thought, the unified Qin and Han gathered the variables into a sum of variables, laying a firm foundation for two thousand years of Chinese design, establishing the basic frame of Chinese craft culture and gradually forming a complete and normative design-art system.",
    [T + "chunqiu-zhanguo.md", T + "chuantong-sheji.md"],
    "断言语义取 L402。“变数的总和”为原文术语，claim 保留引号；秦汉并称，不把体系形成完全归于某一朝代。",
    402, 402, [402], "第一章 造物起源与体系形成（导言）"))

rows.append(C(
    "claim-1081", "cand-01-84", "interpretive_claim",
    "造物规范的出现，是造物设计在追求质量、数量、管理过程中必然要产生的：一方面是造物本身所需，另一方面也由特定时代的社会经济文化条件促成；其完善从一个角度反映出造物体系的形成。",
    "The emergence of craft norms was inevitable as design pursued quality, quantity and management: it was required by making itself and also promoted by the socioeconomic and cultural conditions of a particular age; its perfection reflects from one angle the formation of the craft system.",
    [T + "chuantong-sheji.md", T + "sheji.md"],
    "断言语义取 L406。原文以“必然要产生”表述规律性判断，claim 保留，不降低为或然；两方面条件并列，未分主次。",
    406, 406, [406], "第一章 造物起源与体系形成（导言）"))

rows.append(C(
    "claim-1082", "cand-01-85", "historiographic_claim",
    "用历史说明造物，用造物说明历史，都需要一种历史观和理论；视角的转向会改变造物研究的性质，使造物活动映射出人的本质力量和创造作用。",
    "To explain making through history and history through making both require a historical view and theory; a shift of perspective changes the nature of craft research and lets making reflect human essential power and creativity.",
    [T + "yishu-shejishi.md", T + "sheji.md"],
    "断言语义取 L161。原文以“历史似乎兜了一个圈子”起论，claim 取其对历史观与理论的必要性的判断，不重复该比喻。",
    161, 161, [161], "绪言 一、关于研究的主题与研究范围"))

rows.append(C(
    "claim-1083", "cand-01-86", "historiographic_claim",
    "设计历史不可避免地与时代、政治、社会、经济相关联，但这些方面只能作为全面体现造物设计的旁证，而不是把设计作为那些学科的实物图像例证；设计史应服从于“设计”的发展这一目标，围绕揭示设计特征和演变线索两大任务有重点地展开。",
    "Design history is inevitably related to period, politics, society and economy, but these can only serve as circumstantial evidence for fully presenting design, not as material for illustrating those disciplines; design history should serve the development of design and focus on revealing design features and lines of change.",
    [T + "yishu-shejishi.md", T + "sheji.md"],
    "断言语义取 L378。与 `claim-1076` 同段而论点不同：一为反对王朝框架，一为界定背景学科的位置，未合并。",
    378, 378, [378], "上编 二、设计艺术历史分期的思考"))

out = ROOT / "_ll_ll1a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print("rows", len(rows))
from collections import Counter
print(Counter(r["claim_type"] for r in rows))
links = [p for r in rows for p in r["supported_by"]]
print("links", len(links), "distinct", len(set(links)))
print("span kinds", Counter(r["source"]["source_span"]["span_kind"] for r in rows))
