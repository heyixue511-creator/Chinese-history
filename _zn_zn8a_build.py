# -*- coding: utf-8 -*-
"""Build 赵农 2009 第八章 claim rows (19 new claims, no merges)."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "第八章 游牧的强悍——辽金西夏元时期的设计"

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
    "claim-0662", "cand-08-195", "historiographic_claim",
    "赵农指出，辽、金、西夏、元时期自公元907年至1368年，共461年；五代、两宋与辽、金、西夏及元前期共有372年，时间基本重叠，元灭南宋后统治中国89年；这是游牧民族文化与中原汉文化并行的发展阶段。",
    "Zhao Nong notes that the Liao, Jin, Western Xia and Yuan period ran from 907 to 1368, 461 years in all; the Five Dynasties and two Songs overlapped for 372 years with the Liao, Jin, Western Xia and early Yuan, and the Yuan ruled China for 89 years after destroying the Southern Song; it was a stage in which pastoral and Central Plains Han cultures developed in parallel.",
    [R + "yelv-abaoji.md", R + "aguda.md", R + "li-yuanhao.md", R + "chengjisihan.md"],
    "断言语义取 L5832。461年、372年、89年为原文数字；四个政权并行的分期判断为作者直述，未给历法换算与政权年表。四个建立者条目为四朝代表，未按民族建链。与 claim-0663/0664 同处绪论节，前者分期、后两者作总评，未合并。",
    5827, 5906, [5832], "第一节 绪论"))

rows.append(C(
    "claim-0663", "cand-08-196", "historiographic_claim",
    "赵农认为，这段历史是中原汉民族的农耕文化和北方草原游牧民族文化的较量，结果是中原文化的软弱而导致了游牧民族的胜利。",
    "Zhao Nong holds that this history was a contest between the agrarian culture of the Central Plains Han and the pastoral culture of the northern grasslands, and that the weakness of Central Plains culture led to the victory of the pastoral peoples.",
    [E + "jingkang-zhibian.md", R + "hubilie.md"],
    "断言语义取 L5858。“软弱”“胜利”为作者的史观式因果判断，未给军事、财政与制度的比较数据；靖康之变为北宋败亡节点，忽必烈灭南宋为元代统一节点。与 claim-0675（精湛导致文弱）同章首尾呼应，未合并。",
    5827, 5906, [5858], "第一节 绪论"))

rows.append(C(
    "claim-0664", "cand-08-197", "synthetic_claim",
    "赵农认为，辽、金、西夏、元的经历是草原文化在向农耕文化征服中的一种失败，同时也是不同程度接受和学习中原农耕文化的过程，因此在艺术设计史上有着较高的研究和参照意义。",
    "Zhao Nong holds that the Liao, Jin, Western Xia and Yuan experience was a failure of pastoral culture in its conquest of agrarian culture, and at the same time a process of varying degrees of acceptance and learning from Central Plains agrarian culture, giving it considerable value for research and reference in design history.",
    [T + "liao-sancai.md", P + "yuan-dadu.md"],
    "断言语义取 L5876。“征服中的一种失败”为作者的辩证判断；辽三彩继承唐三彩、元大都按汉族城市规模修建为作者在下文举出的接受例证（L5884、L6142-L6146）。与 claim-0662 同段，前者分期、后者总评，未合并。",
    5827, 5906, [5876], "第一节 绪论"))

rows.append(C(
    "claim-0665", "cand-08-198", "interpretive_claim",
    "赵农认为，马上得天下，却不能马上治天下，如辽国和元朝；同时，马上得天下，也不能用北宋末年的方法治理，如金朝。",
    "Zhao Nong holds that one may win the empire on horseback but cannot govern it on horseback, as with Liao and Yuan; and that having won it on horseback, one cannot govern it by the methods of the late Northern Song, as with Jin.",
    [R + "hubilie.md", R + "aguda.md"],
    "断言语义取 L5858 与 L5874，原文被图版与书眉分隔：“然而，马上得天下，”在 L5858，“却不能马上治天下，如辽国和元朝；……”在 L5874。两个分句分别评辽元与金，未拆条；治理方式判断为作者史论，未给辽、元、金的制度比较。",
    5827, 5906, [5858, 5874], "第一节 绪论"))

rows.append(C(
    "claim-0666", "cand-09-70", "historiographic_claim",
    "赵农认为，文字的使用和完善是一个民族智慧成熟的标志；中国北方的游牧、渔猎民族创建文字，表述民族的意志，从部落文明走向定居生活。",
    "Zhao Nong holds that the use and refinement of writing marks the maturing of a people's wisdom; the pastoral and fishing peoples of northern China created scripts to express their collective will and moved from tribal to settled life.",
    [T + "qidan-wenzi.md", T + "nvzhen-wenzi.md", T + "xixia-wenzi.md", T + "basiba-zi.md"],
    "断言语义取 L5913。契丹、女真、西夏、八思巴四套文字分述见 L5915-L5960；“智慧成熟的标志”为作者的文明史判断，未给文字与社会组织的比较材料。与 claim-0667 同节，前者论文字与文明成熟、后者论文字形成的社会积累，未合并。",
    5909, 5961, [5913], "第二节 文字与印刷"))

rows.append(C(
    "claim-0667", "cand-09-71", "historiographic_claim",
    "赵农认为，任何文字的形成，都是社会生活积累的结果，最后仅仅是由某个人整理完成。",
    "Zhao Nong holds that any script is the result of accumulated social life, merely brought to completion by an individual at the end.",
    [T + "xixia-wenzi.md", T + "basiba-zi.md"],
    "断言语义取 L5945。原文先引沈括《梦溪笔谈》称西夏文字由元昊同党遇乞创造、元昊推广，再提出此一般性判断；八思巴字由八思巴整理为另一例。与 claim-0666 同节，未合并。",
    5909, 5961, [5945], "第二节 文字与印刷"))

rows.append(C(
    "claim-0668", "cand-09-72", "interpretive_claim",
    "赵农认为，辽代对中原文化的企慕，造成汉文字典籍的大量印制。",
    "Zhao Nong holds that Liao admiration for Central Plains culture caused the mass printing of Chinese-language classics.",
    [B + "liaozang.md", B + "mengqiu.md"],
    "断言语义取 L5973。因果解释在列举《史记》《汉书》及经书、医学、诗歌印制之后给出；《辽藏》大字本5000卷、1974年应县木塔出土12卷、《蒙求》与佛教版画6幅见 L5964-L5966。“企慕”为作者的心理化解释，未给辽廷藏书与刻书政策文献。",
    5962, 6017, [5973], "第二节 文字与印刷"))

rows.append(C(
    "claim-0669", "cand-09-73", "interpretive_claim",
    "赵农认为，元代的印刷由于官方审查制度严格，印刷水平的提高较为缓慢。",
    "Zhao Nong holds that because of strict official censorship, the level of Yuan printing improved relatively slowly.",
    [I + "xingwenshu.md", B + "yuhai.md"],
    "断言语义取 L6001。同段列举兴文署刻胡三省《音注资治通鉴》、郑樵《通志》、1340年庆元路刻《玉海》204卷、元代《大藏经》约6500卷；“缓慢”为作者的比较判断，未给刻书数量与审改案例。",
    5962, 6017, [6001], "第二节 文字与印刷"))

rows.append(C(
    "claim-0670", "cand-09-74", "historiographic_claim",
    "赵农认为，元人的书法是对五代至宋书法“尚意”风格的修正，将个人书写和古人法度结合起来，主观也有异族统治下对传统文化的无奈选择，既保存了汉文字的传统书写方式，又延续和充实了中华民族的文化意蕴。",
    "Zhao Nong holds that Yuan calligraphy corrected the 'expressive intent' style of Five Dynasties and Song calligraphy, joining personal writing to ancient rules; subjectively it also embodied a resigned choice of tradition under foreign rule, preserving the traditional writing of Chinese characters while continuing and enriching Chinese cultural meaning.",
    [R + "zhao-mengfu.md"],
    "断言语义取 L6038。原文在叙述赵孟頫影响（鲜于枢、方从义、柯九思、康里嘤嘤、倪瓒）后作整体解释；“无奈选择”为作者的心理与政治解释，未给元廷文化政策文本。赵孟頫“欧颜柳赵”评价见 L6036。与 claim-0671 同段，前者论取向、后者论价值，未合并。",
    6032, 6049, [6038], "第二节 文字与印刷"))

rows.append(C(
    "claim-0671", "cand-09-75", "evaluative_claim",
    "赵农评价，元人书法的规范化，加强了书法艺术的观赏性，却淡化了书写的实用价值。",
    "Zhao Nong judges that the standardisation of Yuan calligraphy strengthened its value as an art to be viewed while weakening the practical value of writing.",
    [R + "zhao-mengfu.md"],
    "断言语义取 L6048，为书法节末段的价值判断。“加强/淡化”为作者的权衡评价，未给书法用途与观赏场景的统计；与 claim-0670 同段，未合并。",
    6032, 6049, [6048], "第二节 文字与印刷"))

rows.append(C(
    "claim-0672", "cand-09-76", "evaluative_claim",
    "赵农评价，以瓷器模仿皮囊壶、形成扁形鸡冠瓷壶，是契丹民族创造性的制瓷设计。",
    "Zhao Nong judges that imitating the leather flask in porcelain to create the flat cockscomb-shaped ewer was a creative ceramic design of the Khitan people.",
    [T + "jiguang-hu.md"],
    "断言语义取 L6325。皮绳缝制痕迹、扁圆造型、管状壶口与环形提梁见同段；“创造性”为作者评价。辽代制瓷多仿邢、定白瓷见 L6323；与 claim-0677（借鉴与改造的总体评价）为同章近邻，未合并。",
    6321, 6355, [6325], "第六节 制瓷和杂器"))

rows.append(C(
    "claim-0673", "cand-09-77", "historiographic_claim",
    "赵农认为，棉花纺织技术的广泛应用，使棉布量产成为可能，这逐渐地改变了人们服饰形态，提高了社会生活水平，也使后来的服饰文化有了新的发展契机。",
    "Zhao Nong holds that the wide application of cotton spinning made mass cotton cloth possible, gradually changing dress forms, raising living standards and giving later dress culture a new starting point.",
    [R + "huang-daopo.md", T + "jiaoche.md", T + "dafangche.md"],
    "断言语义取 L6317，为黄道婆节的总结判断。黄道婆改进轧花车、弹棉椎弓、踏车、织机并传授织造技术见 L6315；“量产—服饰形态—生活水平”的因果为作者判断。与 claim-0653（宋代服饰商品化）为同册前后章近邻，未合并。",
    6310, 6318, [6317], "第五节 服饰和纺织"))

rows.append(C(
    "claim-0674", "cand-09-78", "historiographic_claim",
    "赵农认为，宋代兵器和战术是当时最先进的，但最根本的因素应是人。",
    "Zhao Nong holds that Song weapons and tactics were the most advanced of the time, but that the most fundamental factor should be people.",
    [T + "shibaban-bingqi.md", E + "jingkang-zhibian.md"],
    "断言语义取 L6579。原文在比较宋与辽金元屡败之后提出；“最先进”“最根本”为作者的判断，未给兵器性能与战役结果的统计。与 claim-0659（技术与管理机制的矛盾）为同册前后章近邻，未合并。",
    6577, 6588, [6579], "第八节 结论"))

rows.append(C(
    "claim-0675", "cand-09-79", "historiographic_claim",
    "赵农认为，这是中原文明的精湛所导致的文弱与衰落，而北方游牧民族的野蛮粗犷，在不断冲击中原政权的同时，也为中国社会注入了阳刚豪迈的风俗。",
    "Zhao Nong holds that this was the refinement of Central Plains civilisation producing weakness and decline, while the crude vigour of the northern pastoral peoples, in repeatedly striking Central Plains regimes, also injected a masculine, bold custom into Chinese society.",
    [E + "jingkang-zhibian.md"],
    "断言语义取 L6583。“精湛导致文弱”“野蛮注入阳刚”为作者的文明史对举，未给社会风俗的实证材料；同段还言游牧政权重蹈覆辙与元代压迫汉民族，分见 claim-0676。与 claim-0663（农耕与游牧的较量）同章首尾呼应，未合并。",
    6577, 6588, [6583], "第八节 结论"))

rows.append(C(
    "claim-0676", "cand-09-80", "historiographic_claim",
    "赵农认为，游牧民族在破坏了中原政权之后，也未能有“前车之鉴”的清醒认识，最终还是重蹈覆辙，如金代。",
    "Zhao Nong holds that after destroying Central Plains regimes the pastoral peoples likewise failed to learn from the past and in the end repeated the same collapse, as with the Jin.",
    [R + "aguda.md", T + "jin-dai-jiaochao.md"],
    "断言语义取 L6583，以金代为例；“前车之鉴”“重蹈覆辙”为作者的史论修辞，未给金代政治腐败与财政崩溃的具体材料；同段还及元代压迫汉民族带来失败结局，未拆条。",
    6577, 6588, [6583], "第八节 结论"))

rows.append(C(
    "claim-0677", "cand-09-81", "synthetic_claim",
    "赵农认为，辽、金、西夏、元时期北方游牧民族高度重视器具设计及工匠，在实践中展示了诸多器具设计的真实水平；这其中有对宋代设计文化的借鉴，也有根据民族实际的改造。",
    "Zhao Nong holds that during the Liao, Jin, Western Xia and Yuan the northern pastoral peoples attached great importance to artifact design and craftsmen, demonstrating real levels of design practice; this involved both borrowing from Song design culture and adaptation to their own conditions.",
    [T + "jianghu.md", T + "jiguang-hu.md", T + "liao-sancai.md"],
    "断言语义取 L6585，综合全章材料。“高度重视器具设计及工匠”与“借鉴/改造”为作者的总体评价；同章 L5888 匠户制度、L6325 鸡冠壶、L5884 辽三彩可互证。与 claim-0672 为同章近邻，未合并。",
    6577, 6588, [6585], "第八节 结论"))

rows.append(C(
    "claim-0678", "cand-09-82", "historiographic_claim",
    "赵农认为，宋代毕昇的陶泥活字技术提供了活字印刷的思想，但后来极少有人继承操作，而王祯的实践使活字印刷开始进入了社会生活的文化流通中。",
    "Zhao Nong holds that Bi Sheng's ceramic movable type provided the idea of movable-type printing but was rarely practised afterwards, whereas Wang Zhen's practice brought movable type into the cultural circulation of social life.",
    [R + "wang-zhen.md", B + "wang-zhen-nongshu.md", PR + "huozi-yinshua.md", R + "bi-sheng.md"],
    "断言语义取 L6541。王祯刻活木字三万余、印《旌德县志》六万字见 L6539；木字制作与音韵轮检字见 L6541。“后来极少有人继承”与 claim-0613（宋代未广用）为同册前后章近邻，未合并。",
    6520, 6542, [6541], "第七节 农具和货币"))

rows.append(C(
    "claim-0679", "cand-09-83", "historiographic_claim",
    "赵农认为，人具有自然和文化的双重属性，一方面为了满足生存的需要，发明和创造了许多器物；另一方面又因为生活的富足而多生惰性，而渐积腐朽，以至量变到质变。对于国家来讲，就是天翻地覆的巨变，导致“后人哀之而不鉴之”的必然结果。",
    "Zhao Nong holds that human beings have a dual natural and cultural nature: on one hand they invent and create many artifacts to meet the needs of survival; on the other, prosperity breeds inertia that accumulates into decay until quantitative change becomes qualitative. For a state this means earth-shaking upheaval and the inevitable outcome that 'later generations grieve for it without taking warning'.",
    [],
    "断言语义取 L6581，为结论第二段。“自然/文化双重属性”为作者的哲学人类学解释；“后人哀之而不鉴之”出杜牧《阿房宫赋》，原文未注出处。库内无适龄条目，未强行链接。",
    6581, 6581, [6581], "第八节 结论"))

rows.append(C(
    "claim-0680", "cand-09-84", "evaluative_claim",
    "赵农评价，金代后期的风俗中，男性的衣饰也有红黄颜色，与妇女相差无几，并用金珠等贵重材料装饰，非常华丽；而金地的汉族富贵者也竞相效仿，至此，金代已有亡国之象。",
    "Zhao Nong judges that in late Jin custom men's dress also used red and yellow, scarcely differing from women's, and was lavishly decorated with gold, pearls and other precious materials; wealthy Han in Jin territory imitated it, so that by then the Jin already showed the signs of a fallen state.",
    [],
    "断言语义取 L6269，由男性衣饰华丽、汉族富贵者效仿直接推出“亡国之象”。“非常华丽”“亡国之象”为作者的因果与价值判断，未给金代舆服制度与财政数据；同段接着转入蒙古崛起。库内无适龄条目，未强行链接。",
    6269, 6269, [6269], "第五节 服饰和纺织"))

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

(ROOT / "_zn_zn8a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_zn8a_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")
print("written _zn_zn8a_rows.json / _zn_zn8a_patch.json")
