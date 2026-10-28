# -*- coding: utf-8 -*-
"""Build 赵农 2009 第九章 claim rows (31 new claims, no merges)."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "第九章 专制的文化——明清时期的设计"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"
I = "04-knowledge/units/institutions/"
PR = "04-knowledge/units/procedures/"
E = "04-knowledge/units/events/"

MAP = ROOT / "03-processing/2009-zhaonong-zhongguo-yishu-shejishi/source-map.jsonl"
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
    "claim-0681", "cand-10-13", "historiographic_claim",
    "赵农指出，明清时期是指1368年至1911年，共543年。",
    "Zhao Nong states that the Ming-Qing period runs from 1368 to 1911, 543 years in all.",
    [R + "sun-yat-sen.md", W + "beijing-zijincheng.md"],
    "断言语义取 L6603。543 年为 1911 减 1368 的首尾相减结果，原文未说明是否含首尾；辛亥革命条为目标终点，紫禁城条为贯穿明清的都城建筑。与 claim-0662（辽金西夏元分期）为同册前后章近邻，未合并。",
    6601, 6652, [6603], "第一节 绪论"))

rows.append(C(
    "claim-0682", "cand-10-14", "historiographic_claim",
    "赵农认为，雍正朝驱逐大多数传教士，清王朝长期实行海禁，加上文字狱的精神压迫，使清朝远离科学文明、闭关锁国，最终导致中国近代的衰败。",
    "Zhao Nong holds that the expulsion of most missionaries under the Yongzheng emperor, the long-standing maritime ban and the mental pressure of literary inquisitions turned the Qing away from scientific civilisation and into isolation, ultimately causing China's modern decline.",
    [R + "li-madou.md", E + "kangxi-ditu-cehui.md"],
    "断言语义取 L6621。因果链为作者的史论概括；同段以康熙朝传教士来华与地图测绘为对照，利玛窦条代表西学输入，康熙测绘条代表此前的开放。海禁与文字狱的具体措施原文未展开。",
    6601, 6652, [6621], "第一节 绪论"))

rows.append(C(
    "claim-0683", "cand-10-15", "interpretive_claim",
    "赵农认为，明清艺术设计的发展历史受到明清政治制度的深刻影响：紫禁城是明清艺术设计的集大成者，江南私家园林是对政治专制的逃遁，明式家具则是明清时期的典范。",
    "Zhao Nong holds that Ming-Qing design history was deeply shaped by Ming-Qing political institutions: the Forbidden City is the summation of Ming-Qing design, Jiangnan private gardens were an escape from political autocracy, and Ming-style furniture is the period's exemplar.",
    [W + "beijing-zijincheng.md", T + "jiangnan-yuanlin.md", T + "ming-style-furniture.md"],
    "断言语义取 L6639-L6641 三句。“逃遁”“典范”为作者的解释与评价；紫禁城条、江南园林条、明式家具条分别对应三项例证。与 claim-0693/0695/0696 分论园林，为同章近邻，未合并。",
    6601, 6652, [6639, 6641], "第一节 绪论"))

rows.append(C(
    "claim-0684", "cand-10-24", "historiographic_claim",
    "赵农认为，明代北京城的整体布局是在国都向北京转移的特定背景下合理规划及设计的结果，其中的设计思想与明代国家制度的需求有很大关系；中轴线的确立和城市营造的规模、水平较以前朝代有明显进步，清代入关后仅作局部修缮而未改变城市根本格局，使北京城完整延续下来。",
    "Zhao Nong holds that the overall layout of Ming Beijing resulted from rational planning and design against the background of the capital's transfer to Beijing, and that its design thinking was closely related to the needs of Ming state institutions; the establishment of the central axis and the scale and level of urban construction marked clear progress over earlier dynasties, and after entering the pass the Qing made only partial repairs without changing the city's fundamental layout, allowing Beijing to survive intact.",
    [W + "beijing-zijincheng.md", W + "tiantan.md", R + "kuaixiang.md"],
    "断言语义取 L6724-L6726。中轴线三段与九门、外城诸门见 L6668-L6679；紫禁城规划者蒯祥见 L6687。较前代“明显进步”为作者的比较判断，未给城市面积、人口与工程量的对照数据。与 claim-0635（宋代都城布局）为同册前后章近邻，未合并。",
    6655, 6727, [6724, 6726], "第二节 城市与建筑"))

rows.append(C(
    "claim-0685", "cand-10-28", "interpretive_claim",
    "赵农认为，仅仅依靠城墙的坚固不能获得持久的安定。",
    "Zhao Nong holds that the strength of city walls alone cannot secure lasting stability.",
    [W + "nanjing-chengqiang.md"],
    "断言语义取 L6743，紧接南京城在朱棣起兵、清兵灭南明、太平天国与湘军等战事中屡次被攻破的叙述；城墙周长 33.70 公里、高 14 至 21 米、13 座城门见 L6741。“不能获得持久安定”为作者由史实提出的判断。",
    6728, 6761, [6743], "第二节 城市与建筑"))

rows.append(C(
    "claim-0686", "cand-10-44", "historiographic_claim",
    "赵农认为，清代疆域辽阔、各民族共存同荣，万里长城几乎失去了军事战略的实用价值，成为后人凭吊文物故事之地。",
    "Zhao Nong holds that with the Qing's vast territory and the coexistence of its peoples, the Great Wall almost lost its practical military-strategic value and became a place for later generations to contemplate the past.",
    [W + "ming-changcheng.md", P + "badaling.md", PR + "ming-changcheng-qiangti-gouzhu.md"],
    "断言语义取 L6832。明长城西起嘉峪关、东至山海关并延伸辽东边墙，全长 12700 多里见 L6817；墙体砖石包砌、黄土石灰江米黏合见 L6819。“几乎失去”为作者的形势判断，未给清代边防部署材料。",
    6813, 6833, [6832], "第二节 城市与建筑"))

rows.append(C(
    "claim-0687", "cand-10-74", "historiographic_claim",
    "赵农认为，明式家具在尺度、比例、均衡、对比、节奏、韵律等方面始终简洁明快、流畅自如；明代初期家具以功能为主、崇尚简朴实用，明代后期社会风气浮华使家具风格出现雕琢，但整体仍保持简洁流畅的特点。",
    "Zhao Nong holds that Ming-style furniture remained crisp, bright and fluent in scale, proportion, balance, contrast, rhythm and cadence; early Ming furniture was function-led and admired simplicity and practicality, late Ming luxury produced carved ornament, yet the overall character stayed simple and fluent.",
    [T + "ming-style-furniture.md", T + "taishi-yi.md", T + "guanmao-yi.md"],
    "断言语义取 L6971-L6973。明初以紫檀、黄花梨硬木制作、装饰多利用材质，明后期雕琢增华见同段；太师椅、官帽椅形制见 L6979-L6981。“始终简洁明快”为作者对全期的概括，与同段“后期雕琢”并置。与 claim-0650（宋代椅子）为同册前后章近邻，未合并。",
    6961, 7036, [6971, 6973], "第三节 商业与民居"))

rows.append(C(
    "claim-0688", "cand-10-80", "historiographic_claim",
    "赵农认为，清代家具较之明式家具更显繁琐雕琢、富丽华贵，其形制与清代政治文化对社会生活意识的影响有着密切关系。",
    "Zhao Nong holds that Qing furniture was more elaborate, carved and sumptuous than Ming-style furniture, and that its forms were closely related to the influence of Qing political culture on social life.",
    [T + "qing-style-furniture.md", T + "qingshi-ta.md"],
    "断言语义取 L7039-L7041。清代太师椅为雕花扶手椅、厚重宽大、花饰繁琐见 L7039；架子床毗卢帽、床柜、榻背屏五七九之制见 L7043。“政治文化影响”为作者的归因，未给清代家具使用场合与阶层分布材料。",
    7037, 7052, [7039, 7041], "第三节 商业与民居"))

rows.append(C(
    "claim-0689", "cand-10-91", "interpretive_claim",
    "赵农认为，笔墨纸砚是中国古代文化的载体，有着非常重要的实际作用；历代能工巧匠和知识分子对笔墨纸砚的研究，促使笔墨纸砚的材质更加丰富、形式更加多样，用途也被不断拓展。",
    "Zhao Nong holds that brush, ink, paper and inkstone were carriers of ancient Chinese culture with highly important practical functions; craftsmen's and scholars' work on them enriched materials, diversified forms and continuously extended their uses.",
    [T + "hubi.md", T + "huimo.md", T + "xuan-zhi.md", T + "she-yan.md", T + "duan-yan.md"],
    "断言语义取 L7123，为本节末段总结。湖笔“尖齐圆健”标准与近 100 道工序见 L7074-L7076；徽墨八道工序与集锦墨见 L7087-L7089；宣纸三类与生熟笺之分见 L7097；四大名砚与歙端洮澄泥见 L7111。“文化载体”为作者的价值判断。",
    7055, 7124, [7123], "第四节 文具与书籍"))

rows.append(C(
    "claim-0690", "cand-10-107", "historiographic_claim",
    "赵农认为，明代对书籍印刷管理相对宽松，印刷比较随意，没有太大的限制，有能力的人都可以出资印刷；除官方印制外，坊刻的书籍也非常普及，书籍印刷发行的巨大利润，也是明代出版业繁盛的一个原因。",
    "Zhao Nong holds that Ming book printing was relatively loosely administered and unrestricted, so anyone with means could fund printing; besides official printing, commercial workshop editions were widespread, and the large profits of book publishing were one reason for the prosperity of Ming publishing.",
    [B + "yongle-dadian.md", R + "mao-jin.md", I + "huitongguan.md"],
    "断言语义取 L7130。同段随即指出明初官方仍垄断书籍印刷并控制历书，与本条“管理宽松”构成前后张力；毛晋刻书 600 余种、版 109000 余块见 L7169，会通馆铜活字见 L7206。与 claim-0613（宋代活字未广用）、claim-0616（坊刻排版紧密）为同册前后章近邻，未合并。",
    7125, 7209, [7130], "第四节 文具与书籍"))

rows.append(C(
    "claim-0691", "cand-10-108", "evaluative_claim",
    "赵农评价，短版技术的应用使书籍印刷技术产生了创造性的突破，使画面色调层次、阴阳变化得以加强，从朱、墨色扩展到朱、墨、黛、紫、黄的套色印刷。",
    "Zhao Nong judges that the use of duoban block printing brought a creative breakthrough in book printing, strengthening tonal gradation and light-dark variation and extending colour printing from vermilion and ink to vermilion, ink, blue-black, purple and yellow.",
    [PR + "duanban-taoyin.md", W + "shizhuzhai-jianpu.md", B + "shizhuzhai-huapu.md", R + "hu-zheng-yan.md"],
    "断言语义取 L7195。“创造性地突破”为作者评价；吴发祥《萝轩变古笺谱》、胡正言《十竹斋笺谱》《十竹斋书画谱》见同段，拱花压印见 L7202。原文未给套印色数与印次的量化比较。",
    7125, 7209, [7195], "第四节 文具与书籍"))

rows.append(C(
    "claim-0692", "cand-10-121", "evaluative_claim",
    "赵农评价，清代的雕版插图在明代的基础上有所发展，但是艺术的趣味和质量不如明代。",
    "Zhao Nong judges that Qing woodblock illustrations developed on the Ming foundation but fell short of the Ming in artistic taste and quality.",
    [B + "jieziyuan-huazhuan.md", R + "chen-hongshou.md"],
    "断言语义取 L7233。该句被图版说明与《芥子园画传》段落分隔；作者随即举萧云从《离骚》插图、《太平山图画》、王原祁《佩文斋书画谱》、焦秉贞《耕织图》为清初优秀者。“趣味和质量不如明代”为作者的总评，未给版本与刻工的比较标准。与 claim-0620（插图是书籍装帧重要内容）为同册前后章近邻，未合并。",
    7210, 7258, [7233], "第四节 文具与书籍"))

rows.append(C(
    "claim-0693", "cand-10-134", "evaluative_claim",
    "赵农评价，在艺术设计发展中，明清时期的园林设计是一个闪光点，尤其是清代皇家园林借助国家财力大肆修建，聚天下园林之精华、荟萃一园，成为蔚为大观的景致。",
    "Zhao Nong judges that garden design is a highlight of Ming-Qing design history, especially the Qing imperial gardens built lavishly with state resources, gathering the finest gardens of the realm into one and forming a magnificent spectacle.",
    [W + "qianlong-huayuan.md", T + "jiangnan-yuanlin.md"],
    "断言语义取 L7301。同段列举北海、颐和园、香山静宜园、故宫乾隆花园、承德避暑山庄与被毁的圆明园；“借助国家财力”“聚天下园林之精华”为作者的评价，未给营造费用与用工数据。乾隆花园长 160 米、宽 37 米见 L7331。",
    7299, 7345, [7301], "第五节 园林与瓷器"))

rows.append(C(
    "claim-0694", "cand-10-138", "historiographic_claim",
    "赵农认为，晚清政府的封建专制的政治体制，不断地消解着技术的先进因素，并限制着科学技术在中国近代社会的迅速发展；即使具有政治性的“戊戌变法”亦无法从根本上动摇清政府的愚昧自大。",
    "Zhao Nong holds that the late Qing autocratic political system continually dissolved the advanced elements of technology and restricted the rapid development of science and technology in modern China; even the political reform movement of 1898 could not fundamentally shake the Qing government's ignorance and self-importance.",
    [I + "jiangnan-zhizao-zongju.md", R + "zhang-zhidong.md"],
    "断言语义取 L6629。前文述洋务官僚引进西方技术、开办兵工厂见 L6623-L6629；江南制造总局 1865 年成立见 L7549，张之洞机器铸龙洋见 L6886。“消解”“限制”为作者的制度归因，未给洋务企业技术消化与失败的案例。",
    6629, 6629, [6629], "第一节 绪论"))

rows.append(C(
    "claim-0695", "cand-11-003", "historiographic_claim",
    "赵农认为，江南私人园林的兴盛有两个原因：个人经济富裕带来生活水平和文化意识提高，为私人造园提供经济保证及智慧支持；个人意志的拓展与国家政权专制的冲突，使不少文人选择独善其身，有时间营造私人园林。",
    "Zhao Nong holds that the rise of Jiangnan private gardens had two causes: personal wealth raised living standards and cultural awareness, providing economic security and intellectual support for garden building; and the conflict between individual aspiration and state autocracy led many literati to cultivate themselves apart, giving them time to build gardens.",
    [T + "jiangnan-yuanlin.md", W + "zhuozhengyuan.md", W + "liuyuan.md"],
    "断言语义取 L7348，同句列举苏州拙政园、留园、狮子林、网师园、沧浪亭、环秀山庄、退思园、艺圃及扬州、无锡、上海、杭州诸园。两项原因为作者的归纳，未给造园者的资产、身份与造园时间的统计。与 claim-0683（园林是对政治专制的逃遁）同章呼应，未合并。",
    7346, 7416, [7348], "第五节 园林与瓷器"))

rows.append(C(
    "claim-0696", "cand-11-021", "interpretive_claim",
    "赵农认为，江南园林融住宅和娱乐功能于一体，寄予造园者的人文理想和生活意识，并表达主人的哲学、文学、艺术、人生观念；园林通过借聚隐透、曲幽疏露的方法，在有限空间中表现隐逸趣味。",
    "Zhao Nong holds that Jiangnan gardens combined residence and recreation, carrying the builders' humanistic ideals and life sensibilities and expressing their philosophical, literary, artistic and existential views; through borrowing, gathering, concealing and revealing, and through winding seclusion and selective disclosure, they expressed reclusive taste within limited space.",
    [T + "jiangnan-yuanlin.md", W + "zhuozhengyuan.md", W + "liuyuan.md"],
    "断言语义取 L7357。同段引《论语》“仁者乐山，知者乐水”说明山水情怀；“壶中天地”出《后汉书·方术传》见 L7352。“借聚隐透、曲幽疏露”为作者对手法的概括，未给具体园例的空间分析。",
    7346, 7416, [7357], "第五节 园林与瓷器"))

rows.append(C(
    "claim-0697", "cand-11-024", "interpretive_claim",
    "赵农认为，《园冶》中“三分匠七分主人”的说法，说明人作为造物的主人，应最大程度地符合“能主”的审美需求。",
    "Zhao Nong holds that the saying in Yuan Ye that three parts belong to the craftsman and seven to the master shows that human beings, as masters of making, should meet the aesthetic demands of the capable master to the greatest extent.",
    [B + "yuan-ye.md", R + "ji-cheng.md"],
    "断言语义取 L7423。计成生平、《园冶》崇祯四年（1631）成书、三卷结构与 235 幅插图见 L7421-L7423；“虽由人作，宛自天成”“巧于因借，精在体宜”同段。“能主”的审美需求为作者的解释。与 claim-0641（有定式而无定法）为同册前后章近邻，未合并。",
    7417, 7430, [7423], "第五节 园林与瓷器"))

rows.append(C(
    "claim-0698", "cand-11-036", "synthetic_claim",
    "赵农认为，明代的制瓷业朝着两个极端方向发展：一方面观赏瓷满足人们精神审美的需要，另一方面民用瓷大量生产，白瓷、青花瓷进入寻常人家，成为普通的生活用品。",
    "Zhao Nong holds that Ming porcelain developed toward two extremes: on one hand ornamental porcelain met spiritual and aesthetic needs, on the other civilian ware was mass-produced, with white and blue-and-white porcelain entering ordinary households as everyday utensils.",
    [I + "yuqichang.md", T + "blue-and-white-porcelain.md", T + "wucai.md"],
    "断言语义取 L7444。明代景德镇白瓷“甜白”、青花用波斯苏泥勃青料、御器厂不惜工本制贡品见 L7439；粗瓷烧制技术提高见同段。“两个极端方向”为作者对官窑贡品与民窑量产并行的综合概括，未给产量与价格数据。",
    7431, 7445, [7444], "第五节 园林与瓷器"))

rows.append(C(
    "claim-0699", "cand-11-064", "historiographic_claim",
    "赵农认为，明代造船和航海技术本处于领先地位，却因明代“海禁”制度而逐渐衰退；自宣德年间郑和七下西洋之后，明代彻底实行海禁，甚至出现因制造双桅大船使工匠和船主遭遇逮捕的现象。",
    "Zhao Nong holds that Ming shipbuilding and navigation were originally in a leading position but gradually declined because of the maritime ban; after Zheng He's seven voyages in the Xuande reign the ban became total, with craftsmen and shipowners even arrested for building large two-masted ships.",
    [E + "zhenghe-voyages.md", W + "zhenghe-baochuan.md", T + "shachuan.md", T + "fuchuan.md"],
    "断言语义取 L7539。宝船长 44 丈 4 尺、宽 18 丈、12 帆，1405 至 1433 年七下西洋、27000 余人、30 余国见 L7525；沙船、福船、广船三大船型见 L7533-L7535。“本处于领先”与“逐渐衰退”为作者的比较判断。",
    7513, 7550, [7539], "第六节 服饰与交通"))

rows.append(C(
    "claim-0700", "cand-11-065", "historiographic_claim",
    "赵农认为，中国明清统治者一直不认为海域应该作为国家领土的一部分，几乎放弃了中华民族的海洋疆域，使近代中国海军远远落后于世界先进水平。",
    "Zhao Nong holds that Ming and Qing rulers never regarded maritime space as part of the national territory and all but abandoned China's maritime domain, leaving the modern Chinese navy far behind the world's advanced level.",
    [E + "zhenghe-voyages.md", W + "humen-huopao.md"],
    "断言语义取 L7543。前文述康熙迁海令、沿海渔民内迁 30 里见 L7541；后文述西方夹板船使中国木船退入内河见 L7545。郑和航海条代表此前的海上能力，虎门火炮条代表晚清海防。“一直不认为”为作者的长时段判断，未给历代海疆政策文本。",
    7513, 7550, [7543], "第六节 服饰与交通"))

rows.append(C(
    "claim-0701", "cand-11-066", "historiographic_claim",
    "赵农认为，鸦片战争中西方的坚船利炮粉碎了大清帝国闭关锁国的昏梦，刺激了晚清洋务运动的开展；造船也成为向西方科学技术学习的一个标志，揭开了中国近代工业和科技发展的序幕。",
    "Zhao Nong holds that the Western gunboats in the Opium War shattered the Qing empire's isolationist illusions and stimulated the late Qing self-strengthening movement; shipbuilding became a marker of learning Western science and technology and opened the prologue to modern Chinese industry and technology.",
    [I + "jiangnan-zhizao-zongju.md", I + "lunchuan-zhaoshangju.md", R + "xu-shou.md", W + "humen-huopao.md"],
    "断言语义取 L7547。1865 年徐寿等造“黄鹄”轮船、江南制造总局成立，福州船政局、天津机器局、广东军装机器局、旅顺船坞相继兴建见 L7549。“粉碎”“揭开序幕”为作者的转折判断，未给洋务企业的产量与技术转移评估。与 claim-0659（技术为管理机制牺牲）同册呼应，未合并。",
    7513, 7550, [7547], "第六节 服饰与交通"))

rows.append(C(
    "claim-0702", "cand-11-083", "historiographic_claim",
    "赵农认为，1909年詹天佑设计修筑的京张铁路成功通车，取得了中国科学技术近代化的初步成就。",
    "Zhao Nong holds that the successful opening of the Jingzhang railway, designed and built by Zhan Tianyou, in 1909 marked an initial achievement in the modernisation of Chinese science and technology.",
    [W + "jingzhang-tielu.md", R + "zhan-tianyou.md"],
    "断言语义取 L7591。詹天佑耶鲁大学铁路科毕业、京张铁路总工程师、青龙桥“人”字形线路与石拱桥见 L7593-L7595。“初步成就”为作者的评价；同节另述 1876 年吴淞铁路、1881 年唐胥铁路，作为京张之前的铺垫。",
    7579, 7596, [7591], "第六节 服饰与交通"))

rows.append(C(
    "claim-0703", "cand-11-086", "synthetic_claim",
    "赵农认为，《天工开物》实为中国古代手工业、农业的百科全书；其中纺织、服饰、砖瓦、陶瓷、车船、兵器、颜料、珠玉等部分，为设计史研究保存和提供了极其重要的文献资料。",
    "Zhao Nong holds that Tiangong Kaiwu is effectively an encyclopedia of ancient Chinese handicraft and agriculture; its sections on textiles, dress, bricks and tiles, ceramics, vehicles and ships, weapons, pigments, and pearls and jade preserve and provide extremely important documentary material for design history.",
    [B + "tiangong-kaiwu.md", R + "song-yingxing.md"],
    "断言语义取 L7608。全书 1637 年刊印、上中下三部分、按技术分为 18 卷、121 幅插图见 L7606-L7608；“贵五谷而贱金玉”为编排思想。“百科全书”为作者的性质判断；设计史相关门类为作者的选择性列举。",
    7599, 7609, [7608], "第七节 设计文献"))

rows.append(C(
    "claim-0704", "cand-11-091", "historiographic_claim",
    "赵农认为，明代书籍印刷的昌盛，为《三才图会》这样的类书提供了技术的保证。",
    "Zhao Nong holds that the prosperity of Ming book printing provided the technical guarantee for encyclopedias such as Sancai Tuhui.",
    [B + "sancai-tuhui.md", PR + "huozi-yinshua.md"],
    "断言语义取 L7628。《三才图会》嘉靖年间王圻、王思义编纂，106 卷、14 门类、一事一图见同段；明代印刷的雕版、活字两种技术与坊刻普及见 L7130。“技术保证”为作者的因果判断，未给《三才图会》的刻版数量与印工组织材料。与 claim-0615（宋体字成为标准字）为同册前后章近邻，未合并。",
    7626, 7629, [7628], "第七节 设计文献"))

rows.append(C(
    "claim-0705", "cand-11-093", "historiographic_claim",
    "赵农认为，《大清工部工程做法》是继宋代《营造法式》之后官方制订的又一建筑标准书，在提高建筑质量、减少浪费、确定建筑规范和标准、保障建筑实施工程顺利等方面起到一定作用。",
    "Zhao Nong holds that the Qing Gongbu Gongcheng Zuofa is another officially promulgated building standard after the Song Yingzao Fashi, playing a role in improving quality, reducing waste, fixing norms and standards and ensuring the smooth execution of construction.",
    [B + "gongcheng-zuofa.md", B + "yingzao-fashi.md"],
    "断言语义取 L7632-L7634。全书雍正年间颁行、74 卷、四部分，卷 1 至 27 列 27 种建筑样式与构件尺寸，卷 28 至 40 为斗拱制法见 L7632。“一定作用”为作者的有限评价，未给工程质量与浪费减少的量化证据。",
    7630, 7635, [7634], "第七节 设计文献"))

rows.append(C(
    "claim-0706", "cand-11-098", "interpretive_claim",
    "赵农认为，明清时期的文人对社会生活的研究非常多，虽然不是设计史的内容，但客观上也介入了设计史的诸多问题，对研究明清的设计观念有一定的意义。",
    "Zhao Nong holds that Ming-Qing literati wrote extensively on social life; although not design history proper, this work objectively engaged many design-historical questions and has some significance for studying Ming-Qing design concepts.",
    [B + "changwu-zhi.md", R + "wen-zhenheng.md", R + "li-yu.md", R + "dai-zhen.md"],
    "断言语义取 L7641。文震亨《长物志》12 卷见 L7643；戴震《考工记图》图录礼乐、车舆、宫室、武器见 L7645-L7647；李渔《闲情偶寄》“居室”“器玩”部见 L7649。“客观上介入”为作者的学科边界判断。与 claim-0641（文震亨与《长物志》的近邻讨论）同册呼应，未合并。",
    7636, 7652, [7641], "第七节 设计文献"))

rows.append(C(
    "claim-0707", "cand-11-099", "historiographic_claim",
    "赵农认为，明清时期中国古代社会进入缓慢发展的阶段；明代朱元璋政权虽驱逐蒙古族统治，但汉族社会机制并没有明显进步，明代政治的残酷制度制约了中华文明的积极发展，张居正等改革无法从根本上挽回颓败时局。",
    "Zhao Nong holds that Ming-Qing China entered a stage of slow development; although Zhu Yuanzhang's regime expelled Mongol rule, Han social mechanisms did not clearly advance, the harsh institutions of Ming politics constrained the positive development of Chinese civilisation, and reforms such as Zhang Juzheng's could not fundamentally reverse the decline.",
    [],
    "断言语义取 L7655-L7657。“缓慢发展”为总判断，明代制度与张居正改革为两项论据；张居正改革的具体内容原文未展开。库内无适龄的明代制度或张居正条目，未强行链接。与 claim-0657（宋代滞留下滑）、claim-0658（变法坏于制度）为同册前后章近邻，未合并。",
    7653, 7669, [7655, 7657], "第八节 结论"))

rows.append(C(
    "claim-0708", "cand-11-100", "historiographic_claim",
    "赵农认为，清政府在早期的文治武功在一定意义上保证了社会生活的安定，出现了“康乾盛世”的繁荣；但随着政治体制中积垢渐多，再次出现朝纲混乱、外忧内患，西方坚船利炮打开清帝国大门，许多仁人志士的改良努力被清政府昏庸腐败、丧权辱国的机制阻碍。",
    "Zhao Nong holds that the Qing's early civil and military achievements secured social stability to a degree and produced the prosperity of the Kang-Qian era; but as abuses accumulated in the political system, court disorder and internal and external troubles returned, Western gunboats forced open the Qing empire, and the reform efforts of many patriots were blocked by the government's incompetent, corrupt and treaty-selling machinery.",
    [E + "kangxi-ditu-cehui.md", W + "humen-huopao.md"],
    "断言语义取 L7659。康熙朝地图测绘条代表前期文治，虎门火炮条代表西方坚船利炮与晚清海防。“一定意义”为作者的限定；改良努力被机制阻碍为作者的制度归因，未给戊戌变法等具体案例。",
    7653, 7669, [7659], "第八节 结论"))

rows.append(C(
    "claim-0709", "cand-11-101", "evaluative_claim",
    "赵农评价，回望明清时期的设计史，最有意义的是宋应星等人的研究成果，最为壮观的是詹天佑成功设计的京张铁路。",
    "Zhao Nong judges that looking back on Ming-Qing design history, the most significant achievements are the research of Song Yingxing and others, and the most spectacular is the Jingzhang railway designed by Zhan Tianyou.",
    [B + "tiangong-kaiwu.md", R + "song-yingxing.md", W + "jingzhang-tielu.md", R + "zhan-tianyou.md"],
    "断言语义取 L7666，为全章结论的价值排序。“最有意义”“最为壮观”为主观评价，原文未给排序标准；同段以故宫、圆明园、江南园林、虎门炮台作对照。与 claim-0703、claim-0702 为同章近邻，未合并。",
    7653, 7669, [7666], "第八节 结论"))

rows.append(C(
    "claim-0710", "cand-11-169", "interpretive_claim",
    "赵农认为，江南私家园林原本是明清官宦巨商退养之地，他们斥资修筑，却不能张扬。",
    "Zhao Nong holds that Jiangnan private gardens were originally retirement retreats for Ming-Qing officials and wealthy merchants, who spent heavily on them but could not display them openly.",
    [T + "jiangnan-yuanlin.md"],
    "断言语义取 L7359。该句紧接江南园林借聚隐透、表现隐逸趣味的段落；“退养”“不能张扬”为作者对造园者身份与心态的解释，未给园主名录与政治处境的个案。与 claim-0696 同节近邻，前者论功能与手法、后者论营造者，未合并。",
    7359, 7359, [7359], "第五节 园林与瓷器"))

rows.append(C(
    "claim-0711", "cand-11-170", "evaluative_claim",
    "赵农认为，中国社会在封建腐败的机制下缓慢运行，腐败到了极致，革命的需求也就如星火燎原之势；因此晚清的历史，也是中华民族百折不挠、可歌可泣的历史。回望明清时期的设计史，虽有明清故宫的壮观，也有圆明园的毁灭；既有江南园林的闲逸之地，也有虎门炮台惨烈的硝烟。",
    "Zhao Nong holds that Chinese society moved slowly under a corrupt feudal mechanism until corruption reached its limit and the demand for revolution spread like wildfire; late Qing history is therefore also a history of unyielding and moving national struggle. Looking back on Ming-Qing design history, there is both the grandeur of the imperial palace and the destruction of the Yuanmingyuan, both the leisure of Jiangnan gardens and the bitter smoke of the Humen batteries.",
    [W + "beijing-zijincheng.md", T + "jiangnan-yuanlin.md", W + "humen-huopao.md"],
    "断言语义取 L7664-L7666。紫禁城条对应“明清故宫的壮观”，江南园林条对应“闲逸之地”，虎门火炮条对应“虎门炮台惨烈的硝烟”；圆明园库内无适龄条目。“星火燎原”“百折不挠”为作者的史论修辞，未给晚清革命组织的具体材料。与 claim-0709 同段，前者为对照式总评、后者为成就排序，未合并。",
    7664, 7666, [7664, 7666], "第八节 结论"))

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

(ROOT / "_zn_zn9a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_zn9a_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")
print("written _zn_zn9a_rows.json / _zn_zn9a_patch.json")
