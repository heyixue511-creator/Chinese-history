# -*- coding: utf-8 -*-
"""Build Tian Zibing 2010 batch T3 (Zhou chapter) decisions JSON."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-04-07", "周公", "04-knowledge/units/persons/zhou-gong.md",
     "周公是西周初年与手工业政策和礼乐制度相关的政治家。检索 persons 下无周公条，仅有五个知识元在正文提及。新建依据 L1292 的两事：周公令杀违禁饮酒的人，唯对手工业工人违禁可以不杀，此政策使周代手工业迅速发展；周公长子为鲁公，分鲁公以殷民六族。另据 L1431，周代礼乐在周公时汇集增补并建立法定制度。来源未给姓名、生卒年、官职与摄政经过，confidence 取 medium。",
     "写入 04-knowledge/units/persons/zhou-gong.md（新建）；引用 L1292、L1431；不据来源外材料补生平。"),
    ("cand-04-09", "八材", "04-knowledge/units/terms/ba-cai.md",
     "八材是《史记》所记周代珠、玉、石、象（牙）、木、金、革、羽八种材料的分类。检索 terms 下无八材条，`baigong.md` 只记《考工记》六工三十工种，未收《史记》八材。新建依据 L1338 一句，并记其紧接六工之后、分属材料分类与工种分工两套体系。来源未给各材用途、对应工种与分类原则，confidence 取 medium。",
     "写入 04-knowledge/units/terms/ba-cai.md（新建）；引用 L1338；只列名目，不排八材与六工对应表。"),
    ("cand-04-11", "刖足奴铜鬲", "04-knowledge/units/works/yuezu-nu-tong-li.md",
     "刖足奴铜鬲是西周青铜鬲。检索 works 下无同实体条目；`terms/li-cauldron.md` 记鬲的器类并以本品为例，但那是器类条，不是作品条。新建依据 L1357：鬲下方座的守门者是受了刖刑（断足）的奴隶，来源称其为特殊作品；同段记西周前期鬲少见、后期鬲体由纵深式演变为横宽式。图注 L1383 作“削足奴铜鬲”，与正文异文，条目两存。来源未给尺寸、铭文与藏地，confidence 取 medium。",
     "写入 04-knowledge/units/works/yuezu-nu-tong-li.md（新建）；引用 L1357、L1383；正文与图注异文并列，插图 3 未视觉核验。"),
    ("cand-04-41", "礼乐制度", "04-knowledge/units/terms/li-yue-zhidu.md",
     "礼乐制度是周代由周公汇集、增补并建立法定制度的等级规范。检索 terms 下无礼乐制度条，`baigong.md` 只记官营手工业制度，`terms/twelve-symbols.md` 只记服饰纹样。新建依据 L1431 三句：礼乐沿袭商代而周公建立法定制度、礼乐制度实际就是等级制度、一切视听言行与五礼都要合乎礼乐制度；并以 L1458“礼非乐不履”与钟的等级分组补充乐制。来源未给条文、执行机构与年代，confidence 取 medium。",
     "写入 04-knowledge/units/terms/li-yue-zhidu.md（新建）；引用 L1431、L1458；制度条文与执行机构未载。"),
    ("cand-04-16", "另鼎（音勿）", "04-knowledge/units/works/ling-ding.md",
     "另鼎是西周恭王时青铜鼎，清末毁于兵火。检索 works 下无同实体条目，`works/da-yu-ding.md` 等记其他西周鼎。新建依据 L1443：铭文 410 字，其中有一匹马和一束丝买五个奴隶的记载，反映奴隶价值不如马匹。来源原文作“另(音勿)鼎”，字形与注音不合，未给正字；本条照录，不据来源外材料改题，confidence 取 medium。",
     "写入 04-knowledge/units/works/ling-ding.md（新建）；引用 L1443；器名照录“另(音勿)”，不改为来源外的正字。"),
    ("cand-04-18", "两周金文辞大系图录考释", "04-knowledge/units/publications/liangzhou-jinwen-ci-daxi-tulu-kaoshi.md",
     "《两周金文辞大系图录考释》是田自秉引用的周代青铜铭文著录。检索 publications 下无同书条目。新建依据 L1452：据其所载 167 篇周代青铜铭文统计，作器记事以祭祖先的有 85 篇；L1454 以此论证周代制器服从礼的需要、藏礼于器。来源未给作者、编者、出版年与出版社；`persons/guo-moruo.md` 虽记郭沫若，但来源在此未提作者，故不据来源外材料归给郭沫若，confidence 取 medium。",
     "写入 04-knowledge/units/publications/liangzhou-jinwen-ci-daxi-tulu-kaoshi.md（新建）；引用 L1452、L1454；不补作者与出版信息。"),
    ("cand-04-20", "窃曲纹", "04-knowledge/units/terms/qiequ-wen.md",
     "窃曲纹是周代青铜器的重要装饰纹样。检索 terms 下无窃曲纹条；`persons/guo-moruo.md` 已记郭沫若的木材纹说与来源反驳，但那是人物条。新建依据 L1460 一段：《吕氏春秋》定义、穷曲纹异名、郭沫若木材纹说、来源的动物纹反驳，以及 S 形、直中有圆、圆中有方的形式特征。来源未给型式分类与年代序列，confidence 取 medium。",
     "写入 04-knowledge/units/terms/qiequ-wen.md（新建）；引用 L1460；与郭沫若条互指但不合并，插图 8 未视觉核验。"),
    ("cand-04-75", "鸟纹", "04-knowledge/units/terms/niao-wen.md",
     "鸟纹是周代盛行的青铜器装饰纹样。检索 terms 下无鸟纹条，`terms/feng-wen.md` 记凤纹为另一纹样。新建依据 L1462 两句：周代盛行鸟纹；商代鸟纹头向前、身体成一字形，周代鸟纹头向回看、尾亦下卷，基本构成 S 形骨架。来源只有这一组对比，未给型式分类与年代序列，confidence 取 medium。",
     "写入 04-knowledge/units/terms/niao-wen.md（新建）；引用 L1462；只记商周形式对比。"),
    ("cand-04-22", "环带纹", "04-knowledge/units/terms/huan-dai-wen.md",
     "环带纹是周代应用较多的青铜器装饰纹样。检索 terms 下无环带纹条。新建依据 L1477：组成波状连续的带状，以上下左右的反复产生节奏感和秩序感，常用于器物的主要部位。来源未给单元形制、型式分类与年代序列，confidence 取 medium。",
     "写入 04-knowledge/units/terms/huan-dai-wen.md（新建）；引用 L1477；彩版 8、插图 9 未视觉核验。"),
    ("cand-04-23", "重环纹", "04-knowledge/units/terms/chong-huan-wen.md",
     "重环纹是周代青铜器的带状装饰纹样。检索 terms 下无重环纹条。新建依据 L1488：以一个椭圆形的环为单位连续组成带状，环的一端成圆形、一端成两锐角，有一重、两重、三重之分。来源未给各重式的年代与器物分布，confidence 取 medium。",
     "写入 04-knowledge/units/terms/chong-huan-wen.md（新建）；引用 L1488；插图 10 下未视觉核验。"),
    ("cand-04-24", "垂鳞纹", "04-knowledge/units/terms/chui-lin-wen.md",
     "垂鳞纹是周代青铜器的装饰纹样。检索 terms 下无垂鳞纹条。新建依据 L1490：组成类似鳞片状的装饰，大体构成 U 字纹带状，成错位重叠排列。来源未给单元形制与年代，confidence 取 medium。",
     "写入 04-knowledge/units/terms/chui-lin-wen.md（新建）；引用 L1490；插图 10 上未视觉核验。"),
    ("cand-04-25", "瓦纹", "04-knowledge/units/terms/wa-wen.md",
     "瓦纹是周代青铜器的简朴装饰纹样，又称横线纹，陶瓷上也称弦纹。检索 terms 下无瓦纹条。新建依据 L1492 的名称与构成句，以及 L1503 的地位与施用句；两句之间隔三幅插图，L1503 句为残句，故只逐字引 L1492 的完整句，L1503 改为转述，不拼接为引文。来源未给横条间距与年代，confidence 取 medium。",
     "写入 04-knowledge/units/terms/wa-wen.md（新建）；引用 L1492、L1503；L1503 残句只转述，不拼接引文。"),
    ("cand-04-45", "圭", "04-knowledge/units/terms/gui.md",
     "圭是周代玉礼器的一类。检索 terms 下无圭的专条；`terms/rui-yu-liuqi.md` 记六器成套规范并给圭一句形制，但未收命圭等级与四类圭。新建依据 L1601 的命圭四级（镇圭、桓圭、信圭、躬圭）与玉质等级（全、陇、瓒、将），以及 L1605-L1613 的大圭、琬圭、琰圭、穀圭。来源未给实物、尺寸实测与年代，confidence 取 medium。",
     "写入 04-knowledge/units/terms/gui.md（新建）；引用 L1601、L1605、L1607、L1609、L1611、L1613；与六器条分工，不重复成套规范。"),
    ("cand-04-46", "璧", "04-knowledge/units/terms/bi.md",
     "璧是周代玉礼器的一种。检索 terms 下无璧的专条；`terms/rui-yu-liuqi.md` 记六器成套规范并给璧、环、瑗的边孔比例，`terms/yu-yue-cong-bi.md` 记良渚玉璧，均不收周代璧的等类。新建依据 L1617 的《周礼》璧羡度尺与《尔雅》肉倍好，L1619 的大璧（苍璧）、穀璧、蒲璧、系璧与《说文》。来源未给实物与尺寸，confidence 取 medium。",
     "写入 04-knowledge/units/terms/bi.md（新建）；引用 L1617、L1619；与六器条、良渚玉璧条分工。"),
    ("cand-04-47", "琮", "04-knowledge/units/terms/cong.md",
     "琮是周代祭地的玉器。检索 terms 下无琮的专条；`terms/rui-yu-liuqi.md` 记六器成套规范并给琮一句形制，`terms/yu-yue-cong-bi.md` 记良渚玉琮，均不收《周礼》注的祭地解释。新建依据 L1621：《周礼》注“琮之言宗也，八方所宗故”及外八方象地、中虚圆象地之德，来源称这是儒家解释；形制为圆筒形而外呈方形，如同车釭。来源未给尺寸与源流，confidence 取 medium。",
     "写入 04-knowledge/units/terms/cong.md（新建）；引用 L1621；祭地之义标明为儒家解释。"),
    ("cand-04-48", "璇玑", "04-knowledge/units/terms/xuanji.md",
     "璇玑是周代玉器，圆形、中有孔、周边有牙。检索 terms 下无璇玑条。新建依据 L1623 两句：形制与“有谓是从天文仪器演变而来，其意义难以明了”；图注 L1653 列其为插图 15 的第 7 器。来源只有一句，且自陈意义难明，confidence 取 low。",
     "写入 04-knowledge/units/terms/xuanji.md（新建）；引用 L1623、L1653；天文仪器说标为“有谓”，不补用途。"),
    ("cand-05-30", "周代玉礼器", "04-knowledge/units/terms/zhou-yu-liqi.md",
     "周代玉礼器是周代用于祭祀、朝聘、礼仪与陪葬的玉器组合。检索 terms 下无周代玉礼器的系统条；`terms/rui-yu-liuqi.md` 记《周礼》六器，但不含伦理地位、玦璜、陪葬位置与佩饰。新建依据 L1599 玉与伦理道德、L1603 礼器用途、L1625 玦璜、L1655 陪葬与圭左璋首琥右璜足璧背琮腹的位置、L1662 总结、L1664 佩饰。来源未给成套实物与组合数量，confidence 取 medium。",
     "写入 04-knowledge/units/terms/zhou-yu-liqi.md（新建）；引用 L1599、L1603、L1625、L1655、L1662、L1664；与六器条、圭璧琮璇玑分条互指。"),
    ("cand-05-14", "玉鹿（宝鸡西周墓）", "04-knowledge/units/works/yu-lu.md",
     "玉鹿是宝鸡西周墓出土的西周玉器。检索 works 下无玉鹿条。新建依据 L1664：大鹿向前奔走、小鹿回首张望，形象生动；与洛阳东郊西周墓玉人并举，称二者都是精巧工艺品，反映周代玉器工艺的高度水平。图注 L1658 作“玉鹿(西周)”。来源未给尺寸、玉料与墓号，confidence 取 medium。",
     "写入 04-knowledge/units/works/yu-lu.md（新建）；引用 L1658、L1664；插图 16 未视觉核验。"),
    ("cand-05-87", "玉人（洛阳东郊西周墓）", "04-knowledge/units/works/yu-ren-luoyang.md",
     "玉人是洛阳东郊西周墓出土的西周玉器。检索 works 下无同实体条；`works/fuhao-mu-yuren.md` 是商代妇好墓跪坐玉人，另有专条，不合并。新建依据 L1664：头戴高冠、拱手而立；与宝鸡西周墓玉鹿并举为精巧工艺品。来源未给尺寸、玉料与墓号，confidence 取 medium。",
     "写入 04-knowledge/units/works/yu-ren-luoyang.md（新建）；引用 L1664；与商代妇好墓玉人分条。"),
]

UPDATES = [
    ("cand-04-08", "周代六工", "04-knowledge/units/terms/baigong.md",
     "候选为《考工记》六工三十工种（L1296-L1337）。检索发现 `terms/baigong.md` 已收六职、30 与 31 的算术矛盾、六类工种的名称清单，但未收田自秉逐一列出的三十工种职司，也未收 L1340 的多工种协作与工师、巫、工三级管理。仅记 no_delta 会丢失职司层，故按同实体更新：补六类职司段、协作与三级管理，追加田自秉 citation。跨册更新，source_count 4→5，version 1→2。",
     "批准更新 04-knowledge/units/terms/baigong.md：补田自秉的 30 工种职司、协作生产与三级管理，不新建重复工种条。",
     "追加田自秉 L1296-L1337、L1340；source_count 4→5，version 1→2；田自秉名单的讹字照录不径改。",
     "canonical: 04-knowledge/units/terms/baigong.md。cand-04-08 并入既有百工条。"),
    ("cand-04-36", "十二章", "04-knowledge/units/terms/twelve-symbols.md",
     "候选为田自秉所记十二章（L1541-L1545）：《书经·益稷篇》全文、宗教意义的十二种图案、西周以来历代帝王采用、袁世凯以十二章定服式、前六章绘衣后六章绣裳、汉宋注家与逐章含义。检索发现 `terms/twelve-symbols.md` 只据夏燕靖 2016 记清单、绘绣分工与《三礼图》释义，未收上述材料。按同实体更新：补田自秉一节，citation 追加 2010 册。跨册更新，source_count 1→2，version 1→2。",
     "批准更新 04-knowledge/units/terms/twelve-symbols.md：补田自秉的《书经》全文、历代沿用、注家与逐章含义。",
     "追加田自秉 L1541-L1545；source_count 1→2，version 1→2；两册释义并列，不合并为西周原义。",
     "canonical: 04-knowledge/units/terms/twelve-symbols.md。cand-04-36 并入既有十二章条。"),
]


decisions = []
for suffix, entity, target, analysis, apply_note in CREATES:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": entity,
        "action": "create",
        "target": target,
        "analysis": analysis,
        "approve": f"批准新建 {target}：单册单源，consensus=tentative，confidence 按证据厚度评定。",
        "apply_note": apply_note,
        "note": f"canonical: {target}。",
    })

for suffix, entity, target, analysis, approve, apply_note, note in UPDATES:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": entity,
        "action": "update",
        "target": target,
        "analysis": analysis,
        "approve": approve,
        "apply_note": apply_note,
        "note": note,
    })

cfg = {
    "doc": DOC,
    "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "同实体更新：跨册追加 source block，source_count+1、version+1、日期续期；同册多跨段追加 citation，source_count 不变",
        "逐字引文用“ ”，跨行拼接用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号，嵌套引号用‘ ’",
        "图版只著录图注原文并标未视觉核验，不据图像补写尺寸、藏地与出土地点",
        "同名异物或同词两义并列著录，不合并为单一定义",
        "来源未给作者、正字或年代时照录原文并存疑，不据来源外材料补写",
    ],
    "scope_spans": [[1276, 1673]],
    "scope_note": "田自秉 2010 册第三章周代的工艺美术（L1276-L1673）逐段复读，含概说、青铜工艺、陶瓷、染织、漆器、玉雕与结语。彩版 7-8 与插图 1-16 只读图注，未视觉核验。",
    "decisions": decisions,
    "notes": "田自秉 2010 册 batch T3：周代 unit 候选 21 条，create 19、update 2、no_delta 0。新建含周公、八材、礼乐制度、六种纹样、圭璧琮璇玑与周代玉礼器、四件青铜与玉器作品、一部金文著录；更新百工（30 工种职司）与十二章（《书经》全文与逐章含义）。跨章的战国漆座屏、龙凤虎纹绣衣两候选留春秋战国批次。",
}

out = ROOT / "_zn_decisions_t3.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
