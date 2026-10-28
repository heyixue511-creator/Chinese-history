# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz5a (Tang metal end + Song ceramics, 22 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "唐代金属工艺末、宋代工艺与辽代陶瓷（唐末至辽代工艺美术）"

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
    "claim-0930", "cand-09-71", "historiographic_claim",
    "唐代金银器装饰风格的演变大体可分早、中、晚三期：早期多用忍冬纹，做法工整精细、纹样程式化；中期多以鸟或花朵为中心组成团纹，四周围绕缠枝，繁缛富丽；晚期多为单独的花枝或动物，常采用对称格式，具有写实作风。",
    "Tang gold-and-silver vessel ornament passes through three phases: early honeysuckle scrolls, neat and stylised; middle bird- or flower-centred medallions ringed by scrolling vines, rich and dense; late isolated sprays or animals in symmetrical formats, more naturalistic.",
    [T + "tangcao-wen.md", T + "tuanhua-wen.md", W + "liujin-wuma-xianbei-yinhu.md"],
    "断言语义取 L3319，原文以忍冬、团纹缠枝、单独花枝动物分述金银器装饰三期，属纹样史分期判断；同段未给器物断代统计。",
    3319, 3319, [3319], "第七章 第四节 金属工艺 一、金银器"))

rows.append(C(
    "claim-0931", "cand-09-72", "interpretive_claim",
    "唐镜制作兴盛的原因，一方面是瓷器兴起后许多生活用品由铜器改为瓷器，金属工艺技术集中到铜镜上；另一方面是唐代形成以铜镜献礼、馈赠的社会风尚，玄宗生日“千秋节”群臣以铜镜祝寿或互赠。",
    "Tang mirror production flourished partly because porcelain replaced bronze for daily vessels, concentrating metalworking skill on mirrors, and partly because mirrors became gifts for birthdays and the Qiangqiu festival.",
    [T + "tongjing.md", T + "tang-dai-qingci-yao.md", W + "shuangluan-ruishou-kuihua-jing.md"],
    "断言语义取 L3327，原文以铜器日用品改瓷与千秋节献镜两种原因解释唐镜兴盛，属作者的双因解释；同段引《唐书·礼乐志》。",
    3327, 3327, [3327], "第七章 第四节 金属工艺 二、铜镜"))

rows.append(C(
    "claim-0932", "cand-09-73", "historiographic_claim",
    "1980年陕西蓝田出土窖藏银饰两件，上涂白色珐琅釉质，由此证明在金属上涂饰珐琅的工艺在唐代确有存在，这是明代景泰蓝的滥觞。",
    "Two silver ornaments with white enamel glaze from a 1980 Lantian hoard show that enamelling on metal existed in the Tang and is the forerunner of Ming cloisonné.",
    [T + "falangcai.md", T + "jingtai-lan.md"],
    "断言语义取 L3370 唐镜装饰加工段末，原文由两件蓝田银饰推及唐代珐琅工艺并上溯景泰蓝源流，属源流判断，未给成分检测报告。",
    3370, 3370, [3370], "第七章 第四节 金属工艺 二、铜镜"))

rows.append(C(
    "claim-0933", "cand-09-74", "historiographic_claim",
    "金银平脱的研磨工艺又称“推光”，唐以前未见，是当时新创的一种制漆工艺法。",
    "The grinding process of gold-and-silver pingtuo, also called tuiguang, is not seen before the Tang and was a newly created lacquer technique.",
    [PR + "jinyin-pingtuo.md", T + "qiangjin.md"],
    "断言语义取 L3388，原文在叙述平脱作法后断定推光为唐以前未见的新创工艺，属工艺史判断；未给唐以前反证清单。",
    3388, 3388, [3388], "第七章 第五节 漆器工艺 一、金银平脱"))

rows.append(C(
    "claim-0934", "cand-09-75", "historiographic_claim",
    "雕漆是唐代创造的新产品：先在漆胎上涂漆数十层，待一定厚度再雕刻，这种作法现在称为剔红；唐代雕漆至今未发现实物，只能据《髹饰录》记载推知其刀法古拙。",
    "Carved lacquer was a Tang invention: dozens of lacquer coats were built up and then carved, the technique now called tihong; no Tang example survives, and its archaic knife work is known only from the Xiu Shi Lu.",
    [T + "diao-qi.md", B + "xiu-shi-lu.md"],
    "断言语义取 L3396，原文以《髹饰录》为唯一依据推断唐代雕漆，并明确“到现在还未发现实物”，属文献支撑的工艺史判断。",
    3396, 3396, [3396], "第七章 第五节 漆器工艺 三、雕漆"))

rows.append(C(
    "claim-0935", "cand-09-76", "interpretive_claim",
    "唐代家具的品种和样式正经历着自古以来席地而坐到垂足而坐的过渡阶段；到唐代后期已经出现桌椅，虽未广泛流行，但对人们的生活方式产生了很大影响。",
    "Tang furniture was passing from floor-sitting to chair-sitting; by the late Tang tables and chairs had appeared, not yet widespread but already affecting daily life.",
    [T + "qimu-jiaju.md", T + "gaoxing-jiaju.md", T + "han-dai-jia-ju.md"],
    "断言语义取 L3411，原文以桌椅出现解释起居方式与器形变化，属生活方式—家具形制关系的推断。",
    3411, 3411, [3411], "第七章 第六节 家具工艺"))

rows.append(C(
    "claim-0936", "cand-09-77", "synthetic_claim",
    "唐代工艺美术的鼎盛时期大体在初唐、盛唐，特别是开元、天宝年间；其原因可归纳为经济高度发展、自信和开放的政策、中外工艺美术生产的交流、工艺美术生产的传统发展四个方面。",
    "The peak of Tang craft lay in the early and high Tang, especially the Kaiyuan and Tianbao eras, explained by four factors: economic growth, confident and open policy, international craft exchange, and inherited craft tradition.",
    [T + "tang-dai-qingci-yao.md", T + "sichou-zhilu.md", T + "tangcao-wen.md"],
    "断言语义取 L3446，原文以经济、政策、交流、传统四条并列归纳鼎盛原因，属多因素综合解释，故归 synthetic_claim。",
    3446, 3446, [3446], "第七章 第八节 结语"))

rows.append(C(
    "claim-0937", "cand-09-78", "historiographic_claim",
    "唐代是我国封建历史阶段工艺美术发展的一个重要转折时期：从艺术风格看，唐代起脱离商、周和汉、魏、六朝以来的古朴特色，具有近代装饰风貌的因素；从题材内容看，自唐代开始大量采用花草等植物纹样。",
    "The Tang was a turning point in Chinese craft: stylistically it left behind the archaic manner of Shang-Zhou and Han-Wei-Six Dynasties for factors of modern ornament, and plant motifs began to dominate its subject matter.",
    [T + "tangcao-wen.md", T + "tuanhua-wen.md", T + "mudan.md"],
    "断言语义取 L3448，原文从风格与题材两方面提出唐代转折说，并以狩猎—农耕生产方式解释纹样演变，属分期判断。",
    3448, 3448, [3448], "第七章 第八节 结语"))

rows.append(C(
    "claim-0938", "cand-09-79", "evaluative_claim",
    "唐代工艺美术的艺术风格具有博大清新、华丽丰满的特点，可用“满”字形容；由于它富于情趣化，也可用“情”字来形容。",
    "Tang craft style is broad, fresh, sumptuous and full, best summed up as full (man); because it is rich in sentiment, it can also be summed up as feeling (qing).",
    [T + "tangcao-wen.md", T + "baoxianghua-wen.md"],
    "断言语义取 L3466，原文以“满”“情”二字概括唐代工艺风格，属作者的评价性总结。",
    3466, 3466, [3466], "第七章 第八节 结语"))

rows.append(C(
    "claim-0939", "cand-09-80", "evaluative_claim",
    "宋代的陶瓷是工艺美术中最为杰出的一个品种，是我国古代陶瓷发展的鼎盛时期，也可以说宋代是“瓷的时代”，人们简称它为宋瓷。",
    "Song ceramics were the most outstanding craft of the period and the peak of ancient Chinese ceramic development; the Song may be called the age of porcelain, and its wares are known as Song ci.",
    [T + "songdai-yaoxi.md", T + "qing-ci.md", T + "baici.md"],
    "断言语义取 L3518，原文对宋瓷历史地位的总评价，并以名窑遍布、釉色与装饰丰富为据。",
    3518, 3518, [3518], "第八章 第二节 陶瓷工艺 二、宋瓷"))

rows.append(C(
    "claim-0940", "cand-09-81", "evaluative_claim",
    "论瓷者往往把定、汝、官、哥、钧称为宋代五大名窑，显然有偏颇之处；官窑作品固然精美，但北方的磁州窑、南方的吉州窑等民窑也以清新、朴质的风格大放异彩。",
    "The common listing of Ding, Ru, Guan, Ge and Jun as the five great Song kilns is biased; Guan wares are fine, but popular kilns such as Cizhou in the north and Jizhou in the south also excelled with fresh, plain styles.",
    [T + "wuda-mingyao.md", T + "songdai-yaoxi.md", T + "guan-yao.md"],
    "断言语义取 L3522，原文明确批评五大名窑说的偏颇，属评价性判断；同段以磁州窑、吉州窑为反例。",
    3522, 3522, [3522], "第八章 第二节 陶瓷工艺 二、宋瓷"))

rows.append(C(
    "claim-0941", "cand-09-82", "historiographic_claim",
    "定窑在北宋初曾烧造宫廷用器，后因“定器有芒”，即器物口沿无釉、涩边，不适于作食器，所以另外兴建了汝窑。",
    "Ding kiln supplied the court in the early Northern Song, but because Ding wares had unglazed gritty mouth rims unsuitable for food, Ru kiln was established instead.",
    [T + "wuda-mingyao.md", T + "guan-yao.md", T + "qing-ci.md"],
    "断言语义取 L3554-L3556，原文引宋叶真《坦斋笔衡》“本朝以定州白瓷器有芒，遂命汝州造青窑器”解释汝窑兴建，属文献转述的窑业史判断。",
    3554, 3556, [3554, 3556], "第八章 第二节 陶瓷工艺 二、宋瓷 汝窑"))

rows.append(C(
    "claim-0942", "cand-09-83", "interpretive_claim",
    "钧瓷原属青瓷系统，釉呈乳浊现象；由于原料中有铜的元素，经还原焰烧制而呈现绿或紫红斑，在青釉上打破一色釉的单调，形成对比妍丽的艺术风格；这种色斑变化被称为“窑变”。",
    "Jun ware belongs to the celadon system with an opaque glaze; copper in the body, fired in reduction, produces green or purple-red splashes that break the monotony of a single glaze and create striking contrast, a change called yaobian.",
    [T + "yaobian.md", T + "songdai-yaoxi.md"],
    "断言语义取 L3588，原文以铜元素与还原焰解释钧釉呈色，属工艺机理推断；同段承认最初可能偶然形成。",
    3588, 3588, [3588], "第八章 第二节 陶瓷工艺 二、宋瓷 钧窑"))

rows.append(C(
    "claim-0943", "cand-09-84", "historiographic_claim",
    "磁州窑系以黑白对比为装饰，画花是在白釉上画黑色花纹，在黑釉上画褐色花纹的称铁锈花，笔力豪放洗练；这种画花开创了后世着重花绘的装饰领域。",
    "The Cizhou kiln系 used black-and-white contrast: painting black on white glaze, or brown iron-rust flowers on black glaze, with bold simple brushwork; this painting opened the later field of painted decoration.",
    [T + "song-ci-zhuangshi-shoufa.md", T + "black-porcelain.md", T + "songdai-yaoxi.md"],
    "断言语义取 L3601，原文将磁州窑画花与雕釉并列为两大装饰法，并作开创花绘领域的判断。",
    3601, 3601, [3601], "第八章 第二节 陶瓷工艺 二、宋瓷 磁州窑"))

rows.append(C(
    "claim-0944", "cand-09-85", "interpretive_claim",
    "哥窑釉面的裂纹即开片，是由于釉和胎的收缩率不同而在冷却过程中形成的；最先原是烧制上的一种缺陷，由于纹理具有特殊效果，以后就人为地使它形成自然的装饰。",
    "Ge ware crackle forms during cooling because glaze and body shrink at different rates; originally a firing defect, its special texture was later induced deliberately as natural decoration.",
    [T + "kaipian.md", T + "ge-yao.md"],
    "断言语义取 L3625，原文以釉胎收缩率差解释开片成因，并说明由缺陷转为装饰，属工艺机理与装饰史判断。",
    3625, 3625, [3625], "第八章 第二节 陶瓷工艺 二、宋瓷 哥窑"))

rows.append(C(
    "claim-0945", "cand-09-86", "historiographic_claim",
    "传世哥窑在考古发掘中没有发现确定的烧造地点，在宋墓中也未发现典型器皿；据近年研究，有认为其胎、釉成分与景德镇所制仿哥产品同类型，所以传世哥窑还有待进一步探讨。",
    "No definite kiln site or typical Song tomb example of transmitted Ge ware has been found; recent research notes its body and glaze resemble Jingdezhen imitations, so the question remains open.",
    [T + "ge-yao.md", T + "kaipian.md"],
    "断言语义取 L3630，原文明确保留传世哥窑的未定状态，属史学存疑判断，不与哥窑开片成因合并。",
    3630, 3630, [3630], "第八章 第二节 陶瓷工艺 二、宋瓷 哥窑"))

rows.append(C(
    "claim-0946", "cand-09-87", "interpretive_claim",
    "宋代喝发酵的茶，茶有白沫，用黑釉茶盏在斗茶时容易检验，故以建窑茶具为珍贵。",
    "Song tea was fermented and frothed white; black-glazed bowls made the foam easy to judge in tea contests, so Jian ware was prized.",
    [T + "black-porcelain.md", T + "songdai-yaoxi.md", T + "song-ci-zhuangshi-shoufa.md"],
    "断言语义取 L3638，原文以斗茶检验白沫解释黑釉盏流行，属功能—审美关系推断；同段引《格古要论》。",
    3638, 3638, [3638], "第八章 第二节 陶瓷工艺 二、宋瓷 建窑"))

rows.append(C(
    "claim-0947", "cand-09-88", "evaluative_claim",
    "吉州窑无论从瓷种或装饰等方面看，和宋代其他任何瓷窑比，都应是首屈一指的；它生产青瓷、白瓷、黑瓷，还生产彩瓷和绿釉瓷，并用木叶和剪纸粘贴施釉形成花纹。",
    "In variety of wares and decoration Jizhou kiln should rank first among Song kilns: it made celadon, white, black, painted and green-glazed wares, and used leaf and paper-cut resist decoration.",
    [T + "songdai-yaoxi.md", T + "song-ci-zhuangshi-shoufa.md", T + "black-porcelain.md"],
    "断言语义取 L3642，原文对吉州窑瓷种与装饰多样性的高度评价，属评价性判断；同段列举木叶、剪纸贴饰与玳瑁斑。",
    3642, 3642, [3642], "第八章 第二节 陶瓷工艺 二、宋瓷 吉州窑"))

rows.append(C(
    "claim-0948", "cand-09-89", "historiographic_claim",
    "宋三彩是在白釉的碗、碟上加红绿色彩绘，再低温烧成；它开启了明清时代釉上五彩的发展。",
    "Song sancai applied red and green painting over white-glazed bowls and dishes and fired them at low temperature; it opened the way for Ming-Qing overglaze polychrome decoration.",
    [T + "song-sancai.md", T + "youshang-cai.md"],
    "断言语义取 L3682，原文对宋三彩工艺与后续釉上五彩源流关系的判断。",
    3682, 3682, [3682], "第八章 第二节 陶瓷工艺 三、宋三彩"))

rows.append(C(
    "claim-0949", "cand-09-90", "historiographic_claim",
    "发掘材料证明辽代陶瓷主要仿定窑瓷系：辽代遗址瓷片中定瓷片占50%—80%，不少仿定窑系白瓷有“官”字款，可证辽代也设立了官窑。",
    "Excavations show Liao ceramics mainly imitated the Ding system: Ding sherds make up 50-80 percent of Liao site ceramics, and many Ding-style white wares bear an official mark, indicating Liao official kilns.",
    [T + "liao-ci.md", T + "liao-sancai.md", T + "songdai-yaoxi.md"],
    "断言语义取 L3695，原文以定瓷片比例与“官”字款两项证据推断辽瓷仿定及辽代官窑，属考古材料支撑的判断；比例未注样本量。",
    3695, 3695, [3695], "第八章 第二节 陶瓷工艺 四、辽代的陶瓷"))

rows.append(C(
    "claim-0950", "cand-09-98", "historiographic_claim",
    "唐代铜镜的装饰花纹，早期多为四神镜、十二生肖镜、瑞兽镜、海兽葡萄镜；中期多为鸾鸟镜、花鸟镜、瑞花镜、人物镜、盘龙镜；晚期多为八卦镜、万字镜等。",
    "Tang mirror ornament runs in three phases: early Four Spirits, zodiac, auspicious-beast and sea-beast-grape mirrors; middle phoenix, flower-and-bird, floral, figure and coiled-dragon mirrors; late bagua and wan-character mirrors.",
    [T + "tongjing.md", T + "haishou-putao-wen.md", T + "shuangluan-xianshou-wen.md"],
    "断言语义取 L3366，原文按早中晚三序列举唐镜题材，属纹样史分期判断；与 L3319 金银器三期、L3460 装饰纹样三期分属不同对象，未合并。",
    3366, 3366, [3366], "第七章 第四节 金属工艺 二、铜镜"))

rows.append(C(
    "claim-0951", "cand-09-99", "historiographic_claim",
    "唐代装饰纹样早期秀美、工整，受传统图案影响；中期富丽、丰满，常见色衬、对比、晕絅、撇丝等表现手法；晚期较洗练、简朴，失去初唐的清秀和盛唐的富丽特色。",
    "Tang ornament is neat and refined in the early phase under traditional influence, rich and full in the middle with colour grounds, contrast, graded shading and dry-brush effects, and simpler in the late phase, losing early Tang elegance and high Tang richness.",
    [T + "tangcao-wen.md", T + "tuanhua-wen.md", T + "mudan.md"],
    "断言语义取 L3460，原文以早中晚三期概述唐代装饰纹样风格与技法变化，属分期判断；同段“晕絅”用字与 L3220“晕絰”互异，未据以改写原文。",
    3460, 3460, [3460], "第七章 第八节 结语"))

out = ROOT / "_tz_tz5a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

import collections
types = collections.Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({p for r in rows for p in r["supported_by"]})
kinds = collections.Counter(r["source"]["source_span"]["span_kind"] for r in rows)
print("rows", len(rows), "types", dict(types), "links", links, "distinct", distinct, "kinds", dict(kinds))
