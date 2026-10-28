# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz8a (Qing ceramics tail through Taiping, 34 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "清代陶瓷末至近代工艺（清代中后期至太平天国）"

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
    "claim-0992", "cand-12-02", "factual_claim",
    "粉彩与五彩在五项上存在区别：粉彩以玻璃白涂底、用渲染法使颜色由深到浅、以油料调色、烧成温度约700℃、呈温润匀静之美；五彩不打底、多用单线平涂、以胶水着色、烧成温度约800℃、呈清新透彻之美，故二者有软硬之别。",
    "Famille rose and wucai differ in five respects: famille rose uses a glass-white ground, shading from dark to light, oil-based colour, and fires at about 700°C for a warm even effect; wucai omits the ground, uses flat single-line colouring and glue-based pigment, fires at about 800°C, and appears crisp and clear, hence the soft-versus-hard distinction.",
    [T + "fencai.md", T + "wucai.md", PR + "ming-qing-caici-zhuangshi.md", W + "yongzheng-fencai-sangnv-pan.md"],
    "断言语义取 L4552 粉彩与五彩五项区别，按原文顺序压缩为一句，不扩及粉彩起源与雍正成就的上下文。原文化学式夹排 LaTeX、半角逗号，本 claim 只保留工艺要点，不复制公式。",
    4552, 4552, [4552], "第十一章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-0993", "cand-12-04", "evaluative_claim",
    "《陶雅》评雍正粉彩为清代最美，称其鲜妍夺目、工致殊常；作者引此评说明雍正粉彩彩绘工整精巧，装饰花纹以花鸟为主、多采用折枝花。",
    "Tao Ya judged Yongzheng famille rose the finest of the Qing, calling it dazzlingly fresh and exceptionally refined; the author cites this to characterize Yongzheng famille rose as meticulously painted, with flower-and-bird motifs, mostly cut branches.",
    [B + "taoya.md", T + "fencai.md", W + "yongzheng-fencai-sangnv-pan.md"],
    "断言语义取 L4554。《陶雅》评语为晚清鉴赏判断，非统计结论；原文未注版本卷次，claim 保留其评价性质，不升格为事实定论。",
    4554, 4554, [4554], "第十一章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-0994", "cand-12-06", "evaluative_claim",
    "乾隆时期瓷器流行模仿其他材料的作法，作者认为以瓷器模仿他物只是特技工巧而非艺术创造；用低级材料模拟高级材料外观尚可称巧，用高级材料模拟低级材料外观则只能说是拙。",
    "Qianlong porcelain favoured imitations of other materials; the author holds that making porcelain imitate other substances is technical virtuosity, not artistic creation. Simulating a superior material with an inferior one may still count as clever, but simulating an inferior material with a superior one is merely clumsy.",
    [T + "fencai.md", T + "liaoqi.md", PR + "ming-qing-caici-zhuangshi.md"],
    "断言语义取 L4560。原文引《陶说》列戗金、镂银、琢石、髹漆、螺钿、竹木、匏蠡诸作，claim 概括为模仿他物，不逐一列举。原文“尤可称为巧”之“尤”疑为“犹”之讹，语义按让步关系理解。",
    4560, 4560, [4560], "第十一章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-0995", "cand-12-08", "evaluative_claim",
    "康熙、雍正、乾隆三朝陶瓷风格可分别概括为刚健、雅致、华缛；康熙装饰多用人物，雍正流行花鸟，乾隆早期尚奇巧、晚期重模仿，三朝五彩、粉彩、珐琅彩的制作工艺均达到很高水平。",
    "The ceramic styles of Kangxi, Yongzheng and Qianlong may be summed up as robust, elegant and ornate respectively; Kangxi decoration favoured figures, Yongzheng flower-and-bird motifs, and Qianlong prized novelty early and imitation late, while wucai, famille rose and falangcai all reached high technical levels.",
    [T + "fencai.md", T + "wucai.md", T + "falangcai.md", PR + "ming-qing-caici-zhuangshi.md"],
    "断言语义取 L4576。三字概括（刚健、雅致、华缛）与同段乾隆早晚期分期并置，概括不能覆盖各朝内部变化，claim 保留两套表述而不强行统一。",
    4576, 4576, [4576], "第十一章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-0996", "cand-12-17", "factual_claim",
    "清初在江南等地设织造局，征用大批优秀染织工匠入官营工场；同时对民营机户限制甚严，规定每户织机不得超过百张并缴纳重税，极大妨碍民间纺织业发展，康熙五十一年（1712）因纺织发展需要而废除该限制。",
    "In the early Qing, imperial textile bureaus in Jiangnan and elsewhere conscripted skilled weavers into government workshops, while private weaving households were restricted to no more than one hundred looms each and heavily taxed, greatly hindering private textile production; the limit was abolished in 1712 (Kangxi 51) as textile production expanded.",
    [E + "kangxi-abolish-loom-quota-1712.md", T + "tihuaji.md", T + "qing-dai-sizhi-pinzhong.md"],
    "断言语义取 L4599。原文“织造局”指官营机构，而“每户织机不得超过百张”指民营机户，claim 分述两层，避免把官营征匠与民营限额混为一事。",
    4599, 4599, [4599], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-0997", "cand-12-18", "historiographic_claim",
    "清代织花纹样依服用者身份和职业分为贡货、时新、官服、吏服、商服、农服、僧道等类，据《蚕桑萃编》摘录；作者指出其中许多纹样已不知具体形象、并有错别字，但整体仍可见浓厚的封建色彩。",
    "Qing woven patterns were graded by the wearer's status and occupation into tribute goods, fashionable, official, clerical, merchant, farming and monastic categories, as excerpted from Cansang Cuibian; the author notes that many motif names can no longer be matched to images and some are miswritten, yet the scheme as a whole retains a strong feudal character.",
    [B + "cansang-cuibian.md", T + "qing-dai-sizhi-pinzhong.md", T + "zhuanghua.md", T + "kuduan.md"],
    "断言语义取 L4609-L4625。原文按类罗列数百个纹样名，claim 只保留分类原则、文献来源与作者对史料局限和封建色彩的判断，不复制纹样清单。",
    4609, 4625, [4609, 4611, 4615, 4619, 4623, 4625], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-0998", "cand-12-20", "interpretive_claim",
    "雍正时期改进织机、采用多层经纬织法，使丝织纹样更为丰富、色彩更加华丽，丝织工艺在用色方面取得较高成就。",
    "Yongzheng weavers improved the loom and adopted multi-layer warp-and-weft techniques, enriching silk patterns and colour and achieving notable success in silk dyeing and colouring.",
    [T + "tihuaji.md", PR + "tihua-jishu.md", T + "qing-dai-sizhi-pinzhong.md"],
    "断言语义取 L4627。原文以织机改进与多层经纬织法解释纹样、色彩变化，属因果解释；claim 不把“多层经纬”具体化为某一机具名称，避免超出原文。",
    4627, 4627, [4627], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-0999", "cand-12-24", "historiographic_claim",
    "云锦得名通常认为因其纹饰色彩灿烂辉煌、有如天上云彩，但清代文献并无具体记载；作者补充其纹饰多用云纹，也可作为定名依据。",
    "The name yunjin is usually explained by its brilliant colouring resembling clouds in the sky, but Qing sources contain no explicit record of this; the author adds that its frequent cloud motifs may also ground the name.",
    [T + "nanjing-yunjin.md", T + "zhuanghua.md", T + "kuduan.md"],
    "断言语义取 L4633。原文先陈述通行说法，再指出文献无载，最后以云纹使用提出补充依据；claim 保留三层论证，不把通行说法当作已证结论。",
    4633, 4633, [4633], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-1000", "cand-12-29", "evaluative_claim",
    "清代缂丝常在织造不到的细微处用笔墨描绘，称为补笔；作者认为这种以画代织的方法较之明代全用织工完成作品已略逊一筹。",
    "Qing kesi often used brushwork to fill in fine details the loom could not reach, a practice called bubi; the author judges this substitution of painting for weaving to be somewhat inferior to Ming work completed entirely by the weaver.",
    [T + "kesi.md", PR + "tihua-jishu.md"],
    "断言语义取 L4639。“补笔”为清代缂丝术语，原文未注出处；claim 同时保留技法描述与作者的优劣评价，不将评价改写成技法事实。",
    4639, 4639, [4639], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-1001", "cand-12-30", "factual_claim",
    "清代刺绣因工艺发展而形成不同地方体系，最著名者为苏绣、粤绣、蜀绣、湘绣、京绣，此外还有鲁绣、汴绣、瓯绣等。",
    "Qing embroidery developed distinct regional systems, the best known being Su, Yue, Shu, Xiang and Jing embroidery, alongside Lu, Bian and Ou embroidery.",
    [T + "sida-mingxiu.md", T + "suxiu.md", T + "yuexiu.md", T + "shuxiu.md", T + "xiangxiu.md", T + "jingxiu.md"],
    "断言语义取 L4649。原文列五大名绣又列鲁、汴、瓯三系，未使用“四大名绣”之名；claim 按原文列名，不把后世四大名绣分类回填。",
    4649, 4649, [4649], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-1002", "cand-12-35", "historiographic_claim",
    "有学者据长沙马王堆汉墓出土的大量刺绣，提出汉代马王堆刺绣应为湘绣先声；作者认为此说可以成立，但并不排斥湘绣在近代才形成独特体系的立论。",
    "On the basis of the large embroidered finds from Mawangdui in Changsha, some scholars have proposed Han-dynasty Mawangdui embroidery as a precursor of Xiang embroidery; the author accepts this as tenable without excluding the view that Xiang embroidery formed its distinctive system only in modern times.",
    [T + "xiangxiu.md", T + "sida-mingxiu.md", PR + "han-dai-zhijin-cixiu.md"],
    "断言语义取 L4661。“此说固可成立”为让步语，claim 保留其非定论性质；先声与体系形成被分为两个可并存的命题。",
    4661, 4661, [4661], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-1003", "cand-12-46", "factual_claim",
    "清代刮印花即后世通称的蓝印花布，刷印法则称彩印花布，为蓝印花布的进一步发展；清代彩印花布多产于河南及河北高阳等地。",
    "Qing scraped printing corresponds to what is now called blue calico, while brush printing produced colour calico, a further development of blue calico; Qing colour calico came mainly from Henan and Gaoyang in Hebei.",
    [PR + "lan-yinhua-bu.md", PR + "shua-yin-fa.md", T + "tu-an.md"],
    "断言语义取 L4687。原文先引《松江府志》《长洲县志》述药斑布与两种染法，再作古今名实对应；claim 保留刮印花、刷印法与蓝印花布、彩印花布的对应关系，不展开染法细节。",
    4687, 4687, [4687], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-1004", "cand-12-49", "factual_claim",
    "清代中叶地毯工艺由西北传入北京、天津；咸同年间喇嘛僧胡其昌携二徒自西藏经甘肃、绥远至北平，在报国寺设地毯织制公司，北平地毯由此日渐发展，其二徒织法分东门法、西门法。",
    "In the mid-Qing, carpet making spread from the northwest to Beijing and Tianjin; during the Xianfeng-Tongzhi years the lama monk Hu Qichang brought two disciples from Tibet through Gansu and Suiyuan to Beiping and founded a carpet company at Baoguo Temple, after which Beiping carpets grew, his two disciples giving rise to the East-Gate and West-Gate methods.",
    [T + "ditan.md", R + "hu-qichang.md", P + "beijing.md", P + "tianjin.md"],
    "断言语义取 L4695。原文于胡其昌名后加问号，作者自疑其人名；“清代中叶”与“咸、同年间”时间口径不完全一致，claim 并存两说，不改写为确定纪年。",
    4695, 4695, [4695], "第十一章 第三节 染织工艺"))

rows.append(C(
    "claim-1005", "cand-12-53", "historiographic_claim",
    "画珐琅与明代铜胎掐丝珐琅的主要区别在于：掐丝珐琅先掐丝显花再填珐琅料，画珐琅先涂珐琅再画花纹；作者认为画珐琅并非从外国传入，而是掐丝珐琅的一种演进。",
    "Painted enamel differs from Ming cloisonné chiefly in that cloisonné first lays wire outlines and then fills them with enamel, whereas painted enamel coats the body with enamel and then paints the design; the author holds that painted enamel was not introduced from abroad but evolved from cloisonné.",
    [T + "hua-falang.md", T + "jingtai-lan.md", T + "falangcai.md", PR + "jingtailan-zhizuo.md"],
    "断言语义取 L4715。原文以“铜胎画珐琅”与“铜胎掐丝珐琅”对举，二者同属铜胎珐琅，claim 保留技法差异，不把“画珐琅”与“珐琅彩”混为一名。",
    4715, 4715, [4715], "第十一章 第四节 金属工艺"))

rows.append(C(
    "claim-1006", "cand-12-54", "evaluative_claim",
    "乾隆时期画珐琅出现大件器皿并应用于家具，除模拟作品外还出现西洋装饰风格的作品；作者评价其工艺技巧有所提高，而艺术水平却已下降。",
    "Qianlong painted enamel produced large vessels and was applied to furniture; besides imitative works, pieces in Western decorative styles appeared. The author judges that technical skill rose while artistic quality fell.",
    [T + "hua-falang.md", W + "hua-falang-kuihua-pan.md", W + "hua-falang-xiaoping.md", T + "falangcai.md"],
    "断言语义取 L4721。原文“这时期”承前指乾隆，claim 明示时代主语；“工艺技巧提高、艺术水平下降”为作者评价，保留其二元判断。",
    4721, 4721, [4721], "第十一章 第四节 金属工艺"))

rows.append(C(
    "claim-1007", "cand-12-60", "synthetic_claim",
    "清代雕漆与明代相比有四项显著差异：漆色由暗红变鲜红，刀法由圆润多磨光变刀痕显露不打磨，花纹由庄重浑厚变繁缛纤细，胎骨由多为木胎变为兼有瓷胎、紫砂胎、皮胎等。",
    "Qing carved lacquer differs from Ming in four respects: colour from dark to bright red; cutting from rounded and polished to exposed knife marks left unpolished; ornament from grave and dense to elaborate and fine; and body from mostly wood to porcelain, zisha and leather as well.",
    [T + "diao-qi.md", W + "zitan-tihong-baozuo.md", W + "tihei-diaoqi-flower-bird-plate.md", W + "miaojin-duidiao-qihe.md"],
    "断言语义取 L4749。四项差异为作者归纳，未注取样范围与早晚分期；claim 保留比较结构，不把“清代鲜红”推广为清代全期通例。",
    4749, 4749, [4749], "第十一章 第五节 漆器工艺"))

rows.append(C(
    "claim-1008", "cand-12-68", "factual_claim",
    "清代漆器对欧洲影响很大；18世纪英国著名家具工艺家汤姆·齐平特曾以中国漆家具为蓝本进行设计，风行一时，被称为齐平特时代。",
    "Qing lacquerware strongly influenced Europe; in the eighteenth century the English furniture maker Tom Chippendale designed after Chinese lacquer furniture, a fashion so widespread that it was called the Chippendale age.",
    [T + "diao-qi.md", R + "tom-qipinte.md"],
    "断言语义取 L4772。“汤姆·齐平特”今通译托马斯·齐彭代尔（Thomas Chippendale），claim 从原文译名；“齐平特时代”为西方家具史习称，原文未注出处。",
    4772, 4772, [4772], "第十一章 第五节 漆器工艺"))

rows.append(C(
    "claim-1009", "cand-12-70", "evaluative_claim",
    "清代玉器工艺在乾隆时达到极盛，其特色为多巨型玉雕、多精巧作品，代表作品有《大禹治水图玉山》与《白玉嵌金红宝石碗》。",
    "Qing jade craft reached its zenith under Qianlong, characterized by numerous giant jade carvings and exquisite small works, represented by the Jade Mountain of Yu Taming the Waters and the White Jade Bowl Inlaid with Gold and Rubies.",
    [W + "dayu-zhishui-yushan.md", PR + "yudiao-taocai-qiaose.md"],
    "断言语义取 L4782。原文以乾隆一朝为极盛，未及嘉庆以后；claim 保留作者的分期评价，不补入原文未述的衰变过程。",
    4782, 4782, [4782], "第十一章 第六节 雕刻工艺"))

rows.append(C(
    "claim-1010", "cand-12-71", "factual_claim",
    "《大禹治水图玉山》是乾隆时期制作的巨型玉雕，高2.24米、宽0.96米、重约7吨，前后历时13年完成。",
    "The Jade Mountain of Yu Taming the Waters is a giant Qianlong-period jade carving, 2.24 metres high, 0.96 metres wide and about seven tonnes in weight, completed over thirteen years.",
    [W + "dayu-zhishui-yushan.md", PR + "yudiao-taocai-qiaose.md"],
    "断言语义取 L4782。尺寸与重量为原文所记，未注实测来源与厚度；“13年”含原料运输与制作，原文未分段，claim 不拆分年限。",
    4782, 4782, [4782], "第十一章 第六节 雕刻工艺"))

rows.append(C(
    "claim-1011", "cand-12-86", "evaluative_claim",
    "清代家具与明代家具风格截然不同：明式简练、以造型取胜，清式繁琐、以装饰见长；清代家具并形成苏作、广作、京作三大地方特色。",
    "Qing furniture differs sharply from Ming: Ming style is concise and wins by form, Qing style elaborate and excels in ornament; Qing furniture further developed the Su, Guang and Jing regional traditions.",
    [T + "ming-style-furniture.md", T + "qing-style-furniture.md", T + "qingdai-jiaju-sanda-mingzuo.md"],
    "断言语义取 L4836-L4840。原文句子被空行截为三行，claim 按语义合并；三大作的地域命名与匠人来源（扬州、惠州海丰、冀州）不完全对应，claim 不展开匠籍问题。",
    4836, 4840, [4836, 4838, 4840], "第十一章 第七节 其他工艺"))

rows.append(C(
    "claim-1012", "cand-12-91", "historiographic_claim",
    "吉祥图案是明清以来最流行的一类图案，所占比重极大；明清时期大部分装饰图案遵循图必有意、意必吉祥的原则。",
    "Auspicious motifs were the most popular class of pattern from the Ming-Qing period onward and accounted for a very large share; most Ming-Qing decorative patterns followed the principle that every image carries a meaning and every meaning is auspicious.",
    [T + "jixiang-tu-an.md", T + "tu-an.md", B + "zhuangzi.md"],
    "断言语义取 L4859。原文引《庄子》“虚室生白，吉祥止止”及成玄英疏以释“吉祥”，claim 只保留明清图案的流行程度与意义原则，不复制经疏。",
    4859, 4859, [4859], "第十一章 第八节 吉祥图案"))

rows.append(C(
    "claim-1013", "cand-12-92", "evaluative_claim",
    "作者主张对广泛流行于民间的吉祥图案应分辨精华与糟粕，既不能一概否定也不能全盘接受；其中宣扬封建迷信、封建统治阶级伦理道德、忠孝节义、升官发财的部分属于糟粕，应加批判和摈弃。",
    "The author argues that popular auspicious motifs must be divided into essence and dross, neither wholly rejected nor wholly accepted; those promoting feudal superstition, feudal ethics, loyalty and filial piety, or official advancement and wealth are dross to be criticized and discarded.",
    [T + "jixiang-tu-an.md", T + "tu-an.md"],
    "断言语义取 L4877-L4887。原文列五点，前四点肯定吉祥图案的生活气息、艺术生命力与表现手法，第五点指认糟粕；claim 保留总判断与否定项，不把肯定项并入。",
    4877, 4887, [4877, 4879, 4887], "第十一章 第八节 吉祥图案"))

rows.append(C(
    "claim-1014", "cand-12-93", "evaluative_claim",
    "作者认为清代工艺美术整体上缺乏较高的美学境界，将艺术与技术等同，虽技艺精绝却不能给人以美的陶冶；但在科学上其制作水平远超前代，技术获得飞跃发展。",
    "The author holds that Qing arts and crafts as a whole lacked a high aesthetic realm, equating art with technique; though technically superb, they offered no aesthetic cultivation. Scientifically, however, their production far surpassed earlier periods and technique advanced by leaps.",
    [T + "gongyi-meishu.md", T + "qing-style-furniture.md", T + "jixiang-tu-an.md"],
    "断言语义取 L4891。原文先列赞赏与贬抑两派评价，再以“科学的二分法”提出艺术、科学两层判断；claim 保留两层结构，不把“缺乏美学境界”扩大到技术层面。",
    4891, 4891, [4891], "第十一章 第九节 结语"))

rows.append(C(
    "claim-1015", "cand-12-94", "evaluative_claim",
    "清代工艺美术的艺术特点是繁缛、精巧，绘画式装饰占主导地位；作者认为这种装饰不论在与工艺品用途的结合上，还是在与器物的协调上，都有很大不足。",
    "Qing arts and crafts are characterized artistically by elaboration and refinement, with painting-style ornament dominant; the author finds this ornament gravely deficient both in serving an object's use and in harmonizing with its form.",
    [T + "gongyi-meishu.md", T + "qing-style-furniture.md", T + "fencai.md"],
    "断言语义取 L4893。“绘画式的装饰”与“繁缛、精巧”并列，claim 保留二者；原文末句“一直到现在还存在”为作者对当代的批评，超出清代范围，未纳入。",
    4893, 4893, [4893], "第十一章 第九节 结语"))

rows.append(C(
    "claim-1016", "cand-12-95", "historiographic_claim",
    "清代工艺美术领域逐渐形成民间工艺与宫廷工艺两个体系，各有不同艺术风格、为不同对象服务；前者淳朴自然、富于生活气息，后者矫饰造作、具有匠气和雕琢气。",
    "Qing arts and crafts gradually formed two systems, folk and court, with distinct styles serving different audiences; the former is plain and natural, full of everyday life, the latter affected and contrived, marked by craftsmanly and carved fussiness.",
    [T + "gongyi-meishu.md", T + "qing-style-furniture.md", T + "huishan-niren.md"],
    "断言语义取 L4897。此二分与第十章明代“宫廷工艺和民间工艺两大体系”（claim-0989）表述相近，但一为明代、一为清代，claim 不合并，保留各自时代语境。",
    4897, 4897, [4897], "第十一章 第九节 结语"))

rows.append(C(
    "claim-1017", "cand-12-97", "factual_claim",
    "1840年鸦片战争后，中国从长期封建社会一步步沦为半殖民地半封建社会，揭开中国近代史的序幕。",
    "After the Opium War of 1840, China was reduced step by step from a long-standing feudal society to a semi-colonial and semi-feudal society, opening the prologue of modern Chinese history.",
    [E + "opium-war.md", T + "gongyi-meishu.md"],
    "断言语义取 L4905。“半殖民地半封建”为既有史学范畴，原文未注出处；claim 保留原文的社会性质判断与近代史分期，不扩展条约内容。",
    4905, 4905, [4905], "第十二章 第一节 概说"))

rows.append(C(
    "claim-1018", "cand-12-98", "interpretive_claim",
    "外国资本主义输入及随之而来的机器生产，使中国工艺美术生产受到极大影响并产生现代工艺；作者强调列强输入新技术并非要把封建中国变为资本主义中国，而是要把中国变成其殖民地和半殖民地以加强掠夺。",
    "The influx of foreign capitalism and the machine production that followed greatly affected Chinese craft production and gave rise to modern craft; the author stresses that the powers introduced new technology not to turn feudal China capitalist but to reduce it to colony and semi-colony for harsher exploitation.",
    [E + "opium-war.md", T + "xiandai-gongyi.md", T + "gongyi-meishu.md"],
    "断言语义取 L4909。原文“现代工艺”指近代机器生产下的新工艺，与1949年后“现代工艺”（L5331）所指不同；claim 按本节语境使用，未与当代义合并。",
    4909, 4909, [4909], "第十二章 第一节 概说"))

rows.append(C(
    "claim-1019", "cand-12-99", "factual_claim",
    "近代中国工艺生产逐年衰落：南京丝织机由1853年50000架降至1880年5000架，苏州由12000架降至5500架，景德镇瓷窑由道光时期270至290座降至1869年60座。",
    "Modern Chinese craft production declined year by year: Nanjing silk looms fell from 50,000 in 1853 to 5,000 in 1880, Suzhou from 12,000 to 5,500, and Jingdezhen porcelain kilns from 270-290 in the Daoguang period to 60 in 1869.",
    [T + "qing-dai-sizhi-pinzhong.md", T + "tihuaji.md", P + "nanjing.md", P + "suzhou.md", P + "jingdezhen.md"],
    "断言语义取 L4913-L4915 表格。原文用ASCII波浪号记270~290座，claim 改写为“270至290座”；三组数字口径不同（丝织机按架、瓷窑按座），未合并计算。",
    4913, 4915, [4913, 4915], "第十二章 第一节 概说"))

rows.append(C(
    "claim-1020", "cand-12-101", "factual_claim",
    "太平天国在文艺内容上要求言贵从心、文以纪实，反对徒事清谈与吟花咏柳；形式上要求朴实明晓、切实明透、一目了然；创作方法上要求仰视俯察、观察生活，并提出文艺尤属政治所关、应为革命事业服务。",
    "In literary content the Taiping Heavenly Kingdom demanded that words come from the heart and writing record facts, opposing empty talk and the singing of flowers and willows; in form it required plain clarity and immediate intelligibility; in method it asked authors to observe life, and held that literature and art were bound up with politics and must serve the revolutionary cause.",
    [E + "taiping-tianguo.md", P + "tianjing.md"],
    "断言语义取 L4929。原文出处作《戒浮文巧言谕》，claim 保留文献依据但不引原文长句；“吟花咏柳”为原文用语，未改作“吟风弄月”。",
    4929, 4929, [4929], "第十二章 第二节 太平天国的工艺美术"))

rows.append(C(
    "claim-1021", "cand-12-105", "factual_claim",
    "太平天国提出益民的工艺观，创作上要求以有用之物为宝、精奇利便、以坚固轻便捷巧为妙；服饰上主张中国有中国之形象、中国有中国之衣冠。",
    "The Taiping Heavenly Kingdom advanced a craft doctrine of benefiting the people, requiring that useful things be treasured, that goods be ingenious and convenient, and that sturdiness, lightness, portability and cleverness be prized; in dress it insisted that China keep its own forms and its own garments and caps.",
    [E + "taiping-tianguo.md", B + "zizheng-xinpian.md"],
    "断言语义取 L4935。“益民”为作者概括之词，原文分别引《资政新篇》与《奉天讨胡檄布四方谕》；claim 标明两项文献来源，不把服饰主张与工艺观混为一条出处。",
    4935, 4935, [4935], "第十二章 第二节 太平天国的工艺美术"))

rows.append(C(
    "claim-1022", "cand-12-107", "factual_claim",
    "太平天国工艺政策规定：能造精奇利便之物者准其自售，他人仿造者收为己有或招为徒；器小者赏五年、器大者赏十年、益民多者加多年限，无益之物有责无赏、限满他人仿做。作者据此指出其鼓励创造发明、以益民大小为奖励标准，并已提出禁止仿造的版权保护。",
    "Taiping craft policy allowed inventors of ingenious and convenient goods to sell them, with imitators reduced to servitude or apprenticed; rewards ran five years for small wares and ten for large, increased for greater public benefit, while useless goods earned blame and no reward and became free to copy after the term. The author reads this as encouraging invention, grading rewards by public benefit, and asserting copyright against imitation.",
    [E + "taiping-tianguo.md", B + "zizheng-xinpian.md"],
    "断言语义取 L4937。原文“器小者赏五年，大者赏十年”未说明赏的是专利年限还是赏金，claim 保留“赏五年/十年”的原文表述，不解释为专利期；作者“版权问题”之说明确归入作者判断。",
    4937, 4937, [4937], "第十二章 第二节 太平天国的工艺美术"))

rows.append(C(
    "claim-1023", "cand-12-108", "historiographic_claim",
    "太平天国图案排除封建腐朽内容，禁止龙德龙颜、百灵承运、鹤算龟年、三生有幸等题材，重视劳动题材与民间图案，具有浓厚的民间艺术风格。",
    "Taiping designs excluded feudal and decadent content, banning themes such as dragon virtue and dragon countenance, the hundred spirits bearing the mandate, crane longevity and turtle years, and three lives of good fortune; they valued labour themes and folk patterns and had a strongly popular artistic character.",
    [E + "taiping-tianguo.md", T + "jixiang-tu-an.md", T + "tu-an.md"],
    "断言语义取 L4945。所禁题材引号内文字未注出处；claim 保留四组例证，不把“排除封建内容”扩大为太平天国全部装饰的总体定性。",
    4945, 4945, [4945], "第十二章 第二节 太平天国的工艺美术"))

rows.append(C(
    "claim-1024", "cand-12-111", "evaluative_claim",
    "作者评价太平天国是一场没有无产阶级思想指导而失败的农民革命，对封建文化的批判有力但不彻底；然而其工艺美术业绩在工艺美术史上仍占有一定地位。",
    "The author judges the Taiping Heavenly Kingdom a peasant revolution that failed for lack of proletarian ideological leadership; its critique of feudal culture was forceful but incomplete, yet its achievements in arts and crafts still hold a place in craft history.",
    [E + "taiping-tianguo.md", I + "zhujiangying.md", I + "baigongya.md"],
    "断言语义取 L4959。原文先述生产组织化“百工技艺，各有所归”的成效，再作革命性质与历史地位评价；claim 保留评价部分，生产组织成效另由诸匠营、百工衙条目承载。",
    4959, 4959, [4959], "第十二章 第二节 太平天国的工艺美术"))

rows.append(C(
    "claim-1025", "cand-12-115", "historiographic_claim",
    "1921年中国共产党成立后建立革命根据地和解放区，党的经济政策、文化政策与毛泽东《在延安文艺座谈会上的讲话》为工艺美术开辟新道路并产生新的工艺美术；解放区工艺美术为人民创造、为人民所用，改变了数千年来为劳动人民创造却被剥削阶级占有的状况，发生质的变化。",
    "After the founding of the Chinese Communist Party in 1921, revolutionary base areas and liberated areas were established; the Party's economic and cultural policies and Mao Zedong's Talks at the Yan'an Forum on Literature and Art opened a new path and produced a new arts and crafts. In the liberated areas craft was created by and for the people, ending millennia in which the labouring people created it while the exploiting classes possessed it, a qualitative change.",
    [I + "yanan-bolichang.md", I + "jiefangqu-diyige-taoci-yanjiusuo.md", T + "xiandai-gongyi.md"],
    "断言语义取 L4923。原文将1921年建党与根据地、解放区建立及1942年延安讲话并置，时间跨度被压缩；claim 保留原文叙述顺序，不改写为单一年份事件。",
    4923, 4923, [4923], "第十二章 第一节 概说"))

out = ROOT / "_tz_tz8a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print("rows", len(rows))
from collections import Counter
print(Counter(r["claim_type"] for r in rows))
links = [p for r in rows for p in r["supported_by"]]
print("links", len(links), "distinct", len(set(links)))
print("span kinds", Counter(r["source"]["source_span"]["span_kind"] for r in rows))
