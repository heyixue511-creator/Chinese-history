# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz6a (Jin ceramics tail + Song/Yuan crafts, 16 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "金代陶瓷末、宋元工艺（金代至元代工艺美术）"

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
    "claim-0952", "cand-10-05", "historiographic_claim",
    "金代钧窑在陶瓷中占有突出的地位，并作出了重要贡献；它主要是在青釉上显现红斑，开创了彩瓷的先声，河北、山西、河南等地不少产品与钧瓷相似，说明其影响深远。",
    "The Jin Jun kiln held a prominent place and made an important contribution: red splashes on celadon glaze opened the way for painted porcelain, and similar wares across Hebei, Shanxi and Henan show its wide influence.",
    [P + "jun-kiln.md", T + "yaobian.md", T + "qing-ci.md"],
    "断言语义取 L3745 金代钧窑条，原文以青釉红斑推为“彩瓷的先声”，属陶瓷史地位判断；同段以北方各地相似产品说明影响。",
    3745, 3745, [3745], "第八章 第二节 陶瓷工艺 金代陶瓷"))

rows.append(C(
    "claim-0953", "cand-10-20", "historiographic_claim",
    "从织法看，缂丝与织成两者近似而又有区别，所以通经断纬并不是缂丝的唯一特征：缂丝在织纬时花纹若呈垂直线，经丝截然分开，需加修整工序；织成则在垂直线两经相接处，部分纬线与地纹经纬相交，并按特定服装形式织造。朱启钤《丝绣笔记》也谓二者“是一是二，尚待论定”。",
    "Kesi and zhicheng are similar in weave but distinct, so discontinuous weft is not kesi's only feature: in kesi vertical motif edges separate the warp and require finishing, while zhicheng joins part of the weft across the two warps and is woven to a garment's form; Zhu Qiqian likewise left their identity open.",
    [T + "kesi.md", R + "zhu-qijian.md", B + "sixiu-biji.md"],
    "断言语义取 L3816，原文比较缂丝与织成织法，明确“通经断纬并不是缂丝的唯一特征”，并以朱启钤“尚待论定”保留争议，故归史学辨析而非事实定论。",
    3816, 3816, [3816], "第八章 第三节 染织工艺 二、缂丝"))

rows.append(C(
    "claim-0954", "cand-10-36", "factual_claim",
    "南宋铜镜的产地以湖州和饶州为中心，两地设有铸镜局；所产铜镜多有柄，且一律素地无纹，唯镜背一旁有长方形阴刻款式，注明铸镜地及名号。因宋时缺铜禁铜，官方严格管理生产，有刻款的铜镜才可携带。",
    "Southern Song mirror production centred on Huzhou and Raozhou, where mirror-casting bureaus were set up; their mirrors mostly had handles, plain undecorated grounds, and a rectangular incised mark naming place and maker, since copper shortage and official control allowed only marked mirrors to be carried.",
    [T + "tongjing.md", T + "xin-tongqi.md"],
    "断言语义取 L3871，原文以铸镜局、长方形阴刻款和缺铜禁铜制度说明南宋铜镜生产与流通，属制度—器物事实陈述。",
    3871, 3871, [3871], "第八章 第四节 金属工艺 一、铜镜"))

rows.append(C(
    "claim-0955", "cand-10-45", "evaluative_claim",
    "综观各地所出的宋代漆器，它们也如宋瓷一样，以造型取胜；多数漆器朴素无华，而表现出器物结构比例的韵律美。",
    "Taken together, Song lacquerware from various sites, like Song ceramics, wins by form; most pieces are plain and unornamented, expressing a rhythmic beauty of structural proportion.",
    [T + "diao-qi.md", T + "jin-qi.md", B + "xiu-shi-lu.md"],
    "断言语义取 L3916，原文对宋代漆器总体风格的审美评价，以“以造型取胜”“结构比例的韵律美”为据。",
    3916, 3917, [3916, 3917], "第八章 第五节 漆器工艺"))

rows.append(C(
    "claim-0956", "cand-10-48", "evaluative_claim",
    "如果把唐代的工艺美术风格概括为“情”，宋代则可概括为“理”：唐代华丽，宋代幽雅；唐代开廓恢宏，宋代严谨含蓄。",
    "If Tang craft style is summed up as feeling, Song may be summed up as principle: Tang is sumptuous, Song refined; Tang expansive and grand, Song strict and reserved.",
    [T + "gongyi-meishu.md", T + "wenzhi.md"],
    "断言语义取 L3934，原文以“情”“理”二字对举唐宋工艺风格，属作者的评价性概括，非因果解释。",
    3934, 3934, [3934], "第八章 第七节 结语"))

rows.append(C(
    "claim-0957", "cand-10-49", "interpretive_claim",
    "宋代哲学领域里理学占据统治地位，其核心思想“存天理，灭人欲”以及理学家所提出的“言理而不言情”，都与工艺美术的社会任务和要求背道而驰，因而直接或间接地影响着工艺美术的风格。",
    "Neo-Confucianism dominated Song philosophy; its core doctrine of preserving heavenly principle and extinguishing human desire, and its saying of speaking of principle but not feeling, ran counter to craft's social task and directly or indirectly shaped craft style.",
    [T + "lixue.md", T + "gongyi-meishu.md"],
    "断言语义取 L3940，原文以理学核心命题解释工艺风格，末句有“直接或间接”限定，属思想—风格因果推断。",
    3940, 3940, [3940], "第八章 第七节 结语"))

rows.append(C(
    "claim-0958", "cand-10-50", "historiographic_claim",
    "宋代工艺美术在特定社会条件下明显向两个方向发展：一是结合实用的生活用品，一是专供欣赏的工艺品；后者虽未能成为主流，却对明清工艺美术创作产生了重要影响。",
    "Under particular social conditions Song craft clearly moved in two directions: practical daily utensils and purely appreciative objects; the latter, though never mainstream, strongly influenced Ming-Qing craft.",
    [T + "riyongpin-meishuhua-gongyipin-shiyonghua.md", I + "song-dai-huayuan.md", T + "gongyi-meishu.md"],
    "断言语义取 L3947，原文以画院建立、绘画进入工艺为背景提出两方向说，并判断其对明清的影响，属工艺史分期判断。",
    3947, 3947, [3947], "第八章 第七节 结语"))

rows.append(C(
    "claim-0959", "cand-10-52", "factual_claim",
    "据《元史》记载，1276年元军取得杭州后“籍江南民为工匠，凡三十万户”；1279年又“籍人匠四十二万，立局院七十余所”（《秋涧文集》）。工匠分为制造兵器的军匠与其他技艺的系官人匠（官匠），一般称为匠户。",
    "The Yuan Shi records that after taking Hangzhou in 1276 the Yuan registered 300,000 Jiangnan households as artisans, and in 1279 registered 420,000 artisans and set up over seventy bureaus; artisans became military or government craftsmen, generally called artisan households.",
    [T + "jianghu.md", T + "guanying-shougongye.md"],
    "断言语义取 L3957，原文转引《元史》《秋涧文集》的工匠籍没数字与匠户分类，属文献记载的事实陈述；两处数字未注卷次与统计口径。",
    3957, 3957, [3957], "第九章 第一节 概说"))

rows.append(C(
    "claim-0960", "cand-10-53", "evaluative_claim",
    "元代的工艺美术发展极不平衡，有的畸形繁荣，有的凋零衰落；一部分奢侈享用的工艺品，制作堪称精美。",
    "Yuan craft developed very unevenly: some sectors prospered abnormally while others withered; some luxury objects were exquisitely made.",
    [T + "gongyi-meishu.md", T + "guanying-shougongye.md"],
    "断言语义取 L3963，原文对元代工艺总体格局的评价，以官营庞大、民间凋零与奢侈品精美对举。",
    3963, 3963, [3963], "第九章 第一节 概说"))

rows.append(C(
    "claim-0961", "cand-10-54", "historiographic_claim",
    "棉织工艺在元代得到普遍发展，它代替了传统的麻织品，实用、价廉、物美，为广大人民所欢迎，对人民的服饰产生了重大的影响。",
    "Cotton weaving spread widely in the Yuan and replaced traditional hemp cloth; practical, cheap and good, it was welcomed by ordinary people and greatly affected their dress.",
    [I + "mumian-tijusi.md", R + "huang-daopo.md", P + "songjiang-fu.md"],
    "断言语义取 L3965，原文把棉织替代麻织列为元代工艺的重要成就，属染织史判断；同段以木棉提举司与松江棉织为制度与产地背景。",
    3965, 3965, [3965], "第九章 第一节 概说"))

rows.append(C(
    "claim-0962", "cand-10-55", "evaluative_claim",
    "元代陶瓷的总趋势是较为衰落：制瓷工艺除官办窑场外，民间瓷窑大都质量不高；然而这时期制瓷技术仍有新的发展，如青花和釉里红的兴起、彩瓷的大量流行，白瓷已成为瓷器的主要品种。",
    "Yuan ceramics declined on the whole: apart from official kilns, folk kilns were mostly of low quality; yet technique still advanced, with blue-and-white and underglaze red arising, painted wares spreading, and white ware becoming dominant.",
    [T + "yuan-dai-ciqi-qixing.md", T + "qing-ci.md", T + "baici.md"],
    "断言语义取 L3971，原文同时给出“总趋势衰落”与“技术仍有新发展”的双重评价，未把二者化约为单一衰退论。",
    3971, 3971, [3971], "第九章 第二节 陶瓷工艺 一、陶瓷"))

rows.append(C(
    "claim-0963", "cand-10-60", "historiographic_claim",
    "1976年在韩国木浦附近海域发现的元代沉船，载有青瓷三千多件、白瓷两千多件，多系景德镇和龙泉产品，却无一件青花瓷器；因此青花的开始流行可能在元代中期以后，元代后期青花制作已达到成熟阶段。",
    "A Yuan shipwreck found in 1976 near Mokpo carried over 3,000 celadons and 2,000 white wares, mostly Jingdezhen and Longquan products, but no blue-and-white; blue-and-white therefore probably became popular after the mid-Yuan, and by the late Yuan its production had matured.",
    [T + "blue-and-white-porcelain.md", T + "youlihong.md", W + "qinghua-baleng-longwen-ping.md"],
    "断言语义取 L3994，原文以沉船瓷货组合推断青花流行年代，属考古材料支撑的分期判断；沉船未在原文命名，通常称新安沉船。",
    3994, 3994, [3994], "第九章 第二节 陶瓷工艺 一、陶瓷"))

rows.append(C(
    "claim-0964", "cand-10-71", "interpretive_claim",
    "由于当时中外交通发展，回回锦（又名天方锦）、缅甸锦、波斯罽等著名外国染织品传入我国，使我国染织工艺的艺术风格为之一变，而多采用西法。",
    "Because foreign transport developed, famous textiles such as Huihui brocade, Burmese brocade and Persian rugs entered China, changing the artistic style of Chinese weaving and dyeing toward Western methods.",
    [T + "nashishi.md", T + "zhijin.md", T + "sichou-zhilu.md"],
    "断言语义取 L4058，原文把外来染织品传入与风格变化连为因果，属交流—风格解释；“西法”未具体界定。",
    4058, 4058, [4058], "第九章 第三节 染织工艺 一、丝织"))

rows.append(C(
    "claim-0965", "cand-10-75", "synthetic_claim",
    "黄道婆在棉纺织工艺上的重大贡献可归纳为四个方面：改进“用手剖去其子”的去棉子方法，运用轧车进入半机械化；改进“线弦竹弧”的弹棉工具，运用新式弹弓；把纺纱由一个纺锭增加到三个纺锭；发展棉织提花方法，使普通棉布呈现折枝、团凤、棋局、字样等花纹。",
    "Huang Daopo's contributions to cotton spinning can be summarized in four areas: a roller gin replacing hand seed removal; a new bow replacing the string-and-bamboo tool; three spindles instead of one; and improved figure-weaving that gave plain cloth floral, phoenix, chessboard and character patterns.",
    [R + "huang-daopo.md", I + "mumian-tijusi.md", P + "songjiang-fu.md"],
    "断言语义取 L4080，原文以（一）至（四）分列黄道婆四项技术贡献，属多要点综合，故归 synthetic_claim。",
    4080, 4080, [4080], "第九章 第三节 染织工艺 三、棉织"))

rows.append(C(
    "claim-0966", "cand-10-79", "evaluative_claim",
    "各地元墓和遗址出土的刺绣实物证明，古人对元绣的评价是不切实际的；明高濂《燕闲清赏笺》谓元绣“不及宋”，作者认为这种说法是不公正的。",
    "Embroidery from Yuan tombs and sites shows that old appraisals of Yuan embroidery were unrealistic; the author rejects as unfair Gao Lian's Ming judgment that Yuan embroidery was inferior to Song.",
    [T + "yuan-dai-cixiu-zhenfa.md", W + "jininglu-cixiu-jiashan.md", B + "yanxian-qingshang-jian.md"],
    "断言语义取 L4104，原文以集宁路等出土实物反驳高濂《燕闲清赏笺》的宋元优劣论，属评价性修正。",
    4104, 4104, [4104], "第九章 第三节 染织工艺 四、刺绣"))

rows.append(C(
    "claim-0967", "cand-10-84", "historiographic_claim",
    "元代铜镜的制作工艺已不如以前讲究：出土元镜有的饰简略的缠枝牡丹纹、云鹤纹，双鱼纹仍较流行，有的只铸“寿山福海”四字，多数为素面，制作粗糙，少见精致产品；有人估计元代已渐使用玻璃镜，但缺乏记载。",
    "Yuan mirror craftsmanship was less careful than before: excavated mirrors show simplified peony scrolls or cloud-and-crane designs, double-fish motifs remained popular, some bear only the four characters shou shan fu hai, most are plain and coarse, and fine pieces are rare; glass mirrors may have come into use, but no record confirms it.",
    [T + "tongjing.md", T + "xin-tongqi.md", P + "yuan-dadu.md"],
    "断言语义取 L4128，原文以西安、大同、苏州元墓及大都窖藏铜镜描述元代铜镜衰退，并保留玻璃镜“缺乏记载”的估计。",
    4128, 4128, [4128], "第九章 第四节 金属工艺"))

out = ROOT / "_tz_tz6a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

import collections
types = collections.Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({p for r in rows for p in r["supported_by"]})
kinds = collections.Counter(r["source"]["source_span"]["span_kind"] for r in rows)
print("rows", len(rows), "types", dict(types), "links", links, "distinct", distinct, "kinds", dict(kinds))
