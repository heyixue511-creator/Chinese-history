# -*- coding: utf-8 -*-
"""Build T11 decisions JSON for the 2010 Tian Zibing Ming chapter."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
U = "04-knowledge/units/"

RULES = [
    "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
    "同实体更新：跨册追加 source block，source_count+1、version+1、日期续期；同册多跨段追加 citation/location，source_count 不变、version+1",
    "逐字引文用“ ”，跨行拼接用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号，嵌套引号用‘ ’",
    "图版只著录图注原文并标未视觉核验，不据图像补写尺寸、藏地与出土地点",
    "同名异物或同词两义并列著录，不合并为单一定义",
    "来源未给作者、正字或年代时照录原文并存疑，不据来源外材料补写",
    "只有图注、且所指器物已由其他条目承担的候选记 no_delta；所指器物无其他条目承担时，建图版锚点作品条并标未视觉核验与逐项未载",
    "类型条与单器条分工：总类、制法、纹样与题材归术语条，单件器物的尺寸、出土与画面归作品条",
    "候选 unit_type 与实体性质不符时按实体改写：织物与纹样类型记 term，单件器物与单幅画作记 work",
    "同段并列条目按证据层级分列：工艺总类归 term，实例器物归 work，人物归 person，不因同段而合并",
]


def C(cid, entity, target, analysis, approve, apply_note, note=None):
    return {
        "cid": f"{DOC}:{cid}",
        "entity": entity,
        "action": "create",
        "target": U + target,
        "analysis": analysis,
        "approve": approve,
        "apply_note": apply_note,
        "note": note or f"canonical: {U}{target}。{cid} 并入该条。",
    }


def UPD(cid, entity, target, analysis, approve, apply_note, note=None):
    d = C(cid, entity, target, analysis, approve, apply_note, note)
    d["action"] = "update"
    return d


def N(cid, entity, target, analysis, approve, apply_note, note=None):
    d = C(cid, entity, target, analysis, approve, apply_note, note)
    d["action"] = "no_delta"
    return d


D = []

D.append(C(
    "cand-11-24", "成化斗彩鸡缸杯", "works/chenghua-jigang-cup.md",
    "候选为成化鸡纹酒杯，又称鸡缸杯（L4220）。`terms/doucai.md` 与 `publications/tao-shuo.md` 都提到鸡缸杯，但 `works/` 无单器条；来源给别名、子母鸡题材、画面内容、造型评语与两条文献评语，还带“成窑一件衣”的彩绘特征。按单器建 work 条，与斗彩总类条和《陶说》条互指，不重复斗彩定义。",
    "批准新建 works/chenghua-jigang-cup.md；单册单源，consensus=tentative。",
    "写入 works/chenghua-jigang-cup.md，新建；来源 L4220；尺寸、胎釉、款识、藏地与图版未载。",
))

D.append(C(
    "cand-11-82", "宣德青花缠枝花卉执壶", "works/xuande-blue-white-pot.md",
    "候选为插图1图注所记宣德青花缠枝花卉执壶（L4206-L4207）。`terms/blue-and-white-porcelain.md` 记青花总类与苏泥勃青，不收单器；`works/` 无此器。来源只有图注器名与时代，正文同段讲宣德青花胎料、青料与纹样，未描述此壶形制。按图版锚点建 work 条，标未视觉核验，不据器名补写流、柄、尺寸与藏地。",
    "批准新建 works/xuande-blue-white-pot.md；单册单源，consensus=tentative。",
    "写入 works/xuande-blue-white-pot.md，新建；来源 L4206-L4207；尺寸、胎釉、款识、藏地与图版核验未载。",
))

D.append(C(
    "cand-11-31", "赤绘", "terms/chihui.md",
    "候选为赤绘（L4246-L4250）。`terms/` 无赤绘条；`places/dehua-yao.md` 明言 L4246 的赤绘不并入德化窑条。来源给日本称法、与我国“五彩”的对应关系、明末传入日本与“赤绘”一名在日本流行的经过，并列出技术交流的对向流动。按陶瓷装饰类型建 term 条，产出 slug 由候选的 chihui-export-porcelain 收敛为 chihui。",
    "批准新建 terms/chihui.md；单册单源，consensus=tentative。",
    "写入 terms/chihui.md，新建；来源 L4246-L4250；具体器物、传入年代上限与日本接受史细节未载。",
))

D.append(C(
    "cand-11-30", "何朝宗", "persons/he-chaozong.md",
    "候选为何朝宗（L4244）。`places/dehua-yao.md` 已在窑口条内记何朝宗与德化瓷塑，但 `persons/` 无人物条；来源给籍贯、身份、瓷塑题材与“天下共宝之”的评语。建 person 条，与德化窑条互指，不重复窑口总述。",
    "批准新建 persons/he-chaozong.md；单册单源，consensus=tentative。",
    "写入 persons/he-chaozong.md，新建；来源 L4244；生卒、师承、传世作品清单、款识与藏地未载。",
))

D.append(C(
    "cand-11-84", "填彩", "terms/tian-cai.md",
    "候选为填彩（L4215）。`terms/doucai.md` 讨论斗彩与填彩的关系，但只引“斗彩”一侧的操作定义，未收填彩自身的工序描述；`terms/` 无填彩条。来源一句给先画轮廓、再填彩色釉料的两步工序，并把它与斗彩并列为青花加彩的两种表现方法。建 term 条，与斗彩条互指，不合并为一条。",
    "批准新建 terms/tian-cai.md；单册单源，consensus=tentative。",
    "写入 terms/tian-cai.md，新建；来源 L4215；彩料成分、烧成次数、典型器物与盛行年代未载。",
))

D.append(C(
    "cand-11-85", "斗彩葡萄杯", "works/doucai-grape-cup.md",
    "候选为插图2图注所记斗彩葡萄杯（L4218）。`works/` 无此器；`terms/doucai.md` 只作为鸡缸杯等器物提及，不收单器。来源只有图注器名与时代。按图版锚点建 work 条，标未视觉核验，不据器名补写纹样细节、尺寸与藏地。",
    "批准新建 works/doucai-grape-cup.md；单册单源，consensus=tentative。",
    "写入 works/doucai-grape-cup.md，新建；来源 L4218；尺寸、胎釉、款识、藏地与图版核验未载。",
))

D.append(C(
    "cand-11-86", "斗彩斗鸡杯", "works/doucai-cock-cup.md",
    "候选为插图2图注所记斗彩斗鸡杯（L4218）。与同图注的斗彩葡萄杯并列，`works/` 均无单器条。来源只有图注器名与时代，正文未描述。按图版锚点建 work 条，标未视觉核验；器名作“斗鸡杯”，不据“鸡缸杯”条改写。",
    "批准新建 works/doucai-cock-cup.md；单册单源，consensus=tentative。",
    "写入 works/doucai-cock-cup.md，新建；来源 L4218；尺寸、胎釉、款识、藏地与图版核验未载。",
))

D.append(C(
    "cand-11-87", "斗彩八卦炉", "works/doucai-bagua-censer.md",
    "候选为插图3图注所记斗彩八卦炉（L4231）。`terms/` 无八卦炉条；`terms/doucai.md` 不收单器。来源只有图注器名与时代，正文同段讲嘉靖道教题材与八卦、云鹤等纹样，未描述此炉。按图版锚点建 work 条，标未视觉核验。",
    "批准新建 works/doucai-bagua-censer.md；单册单源，consensus=tentative。",
    "写入 works/doucai-bagua-censer.md，新建；来源 L4231；尺寸、胎釉、款识、藏地与图版核验未载。",
))

D.append(C(
    "cand-11-88", "五彩人物洗", "works/wucai-figure-washer.md",
    "候选为插图4图注所记五彩人物洗（L4234）。`terms/wucai.md` 记五彩总类，但未收此器，也未引田自秉明章此段；`works/` 无此器。来源只有图注器名与时代。按图版锚点建 work 条，标未视觉核验；不据“人物洗”补写画面内容。",
    "批准新建 works/wucai-figure-washer.md；单册单源，consensus=tentative。",
    "写入 works/wucai-figure-washer.md，新建；来源 L4234；尺寸、胎釉、款识、藏地与图版核验未载。",
))

D.append(C(
    "cand-11-40", "天水冰山录", "publications/tianshui-bingshanlu.md",
    "候选为《天水冰山录》（L4302）。`terms/gaiji.md` 只把该书当作改机名目的出处，`publications/` 无书条。来源给严嵩抄家本事、染织品种清单、缎的细类、花纹与色彩名目及史料价值，未给作者、成书年与卷数。按著作建 publication 条，与改机条互指。",
    "批准新建 publications/tianshui-bingshanlu.md；单册单源，consensus=tentative。",
    "写入 publications/tianshui-bingshanlu.md，新建；来源 L4302；作者、成书年、卷数、抄家年份与账簿体例未载。",
))

D.append(C(
    "cand-11-42", "阮弼", "persons/ruan-bi.md",
    "候选为万历时芜湖染局商人阮弼（L4340）。`persons/` 无阮弼；来源给时代、姓名、芜湖染局、五方购者与分局范围，并据此判断芜湖已成全国性染业产地，未给生卒、籍贯与资本。建 person 条，与匠户条及地域印染条互指。",
    "批准新建 persons/ruan-bi.md；单册单源，consensus=tentative。",
    "写入 persons/ruan-bi.md，新建；来源 L4340；生卒、籍贯、字号、染局规模与经营资本未载。",
))

D.append(C(
    "cand-11-43", "顾绣", "terms/gu-embroidery.md",
    "候选为顾绣（L4348-L4352）。`terms/sida-mingxiu.md` 记四大名绣，未收顾绣；`persons/shen-shou.md` 只把顾绣当刺绣史背景。来源给得名、露香园与韩媛绣别称、缪氏与韩希孟与顾兰玉三代人物、画绣特点、技艺评语、顾绣庄与欣赏工艺转向，未给针法谱系与作品清单。建 term 条，与韩希孟人物条互指。",
    "批准新建 terms/gu-embroidery.md；单册单源，consensus=tentative。",
    "写入 terms/gu-embroidery.md，新建；来源 L4348-L4352；针法谱系、作品清单、传承代数、尺寸与藏地未载。",
))

D.append(C(
    "cand-11-44", "韩希孟", "persons/han-ximeng.md",
    "候选为韩希孟（L4350）。`persons/` 无韩希孟；`terms/gu-embroidery.md` 同批新建并已详记顾氏家族，但人物条需独立承担生卒、身份与技艺项。来源给顾寿僭妻身份、谙通六法、画绣与韩媛绣别称及画绣的装饰性，未给生卒与作品。建 person 条，与顾绣条互指。",
    "批准新建 persons/han-ximeng.md；单册单源，consensus=tentative。",
    "写入 persons/han-ximeng.md，新建；来源 L4350；生卒、籍贯、师承、作品清单、款识与藏地未载。",
))

D.append(C(
    "cand-11-46", "大钟寺大钟", "works/dazhongsi-bell.md",
    "候选为北京大钟寺永乐大钟（L4358）。`works/` 无此器；`terms/tongjin.md` 记铜禁与铜器制度，不收单器。来源给地点、年代、高6.75米、口径3.3米、重44.6吨、最大铜钟地位与冶铜工艺评价。按单器建 work 条，与宣德炉条分列。",
    "批准新建 works/dazhongsi-bell.md；单册单源，consensus=tentative。",
    "写入 works/dazhongsi-bell.md，新建；来源 L4358；铸造工场、铜料配比、合金成分、钟钮与纹饰未载。",
))

D.append(C(
    "cand-11-47", "宣德炉", "terms/xuande-censer.md",
    "候选为宣德炉（L4364-L4366）。`terms/` 无宣德炉条；`terms/tongjin.md` 与 `terms/jingtai-lan.md` 分别记铜器制度与铜胎珐琅，不收此器类。来源给工部铸炉缘起、十二炼、用铜与金银用量、鎏金渗金与呈色、耳五十余式与边口足各式、后世仿造与北南苏三铸及铸铜能手。按金属工艺类型建 term 条。",
    "批准新建 terms/xuande-censer.md；单册单源，consensus=tentative。",
    "写入 terms/xuande-censer.md，新建；来源 L4364-L4366；具体铸炉数量、传世品清单、每器尺寸与款识、合金配比未载。",
))

D.append(C(
    "cand-11-55", "周翥", "persons/zhou-zhu.md",
    "候选为扬州百宝嵌名家周翥（L4387、L4408）。`terms/baibaoqian.md` 同批新建，已详记周制与《骨董琐记》引文；`persons/` 无周翥。来源给扬州、明末、周制得名与嵌料嵌件范围。建 person 条，与百宝嵌条互指，不重复嵌器工艺总述。",
    "批准新建 persons/zhou-zhu.md；单册单源，consensus=tentative。",
    "写入 persons/zhou-zhu.md，新建；来源 L4387、L4408；生卒、师承、作坊、传世作品与款识未载。",
))

D.append(C(
    "cand-11-56", "蒋回回", "persons/jiang-huihui.md",
    "候选为苏州金漆艺人蒋回回（L4387、L4412）。`persons/` 无蒋回回；`terms/jin-qi.md` 同批新建，已记金漆工艺与蒋回回、杨埙二人。来源给苏州、金漆彩绘与制作精湛的评语。建 person 条，与金漆条及杨埙条互指。",
    "批准新建 persons/jiang-huihui.md；单册单源，consensus=tentative。",
    "写入 persons/jiang-huihui.md，新建；来源 L4387、L4412；生卒、师承、作坊、传世作品与款识未载。",
))

D.append(C(
    "cand-11-57", "张德刚", "persons/zhang-degang.md",
    "候选为果园厂雕漆名手张德刚（L4391）。`institutions/guoyuanchang.md` 已记果园厂与张德刚、包亮，但 `persons/` 无人物条；候选给籍贯、父张成、永乐召入与官职。建 person 条，与果园厂条、张成条互指，不重复官营作场总述。",
    "批准新建 persons/zhang-degang.md；单册单源，consensus=tentative。",
    "写入 persons/zhang-degang.md，新建；来源 L4391；生卒、任职年份、作品清单与款识未载。",
))

D.append(C(
    "cand-11-91", "包亮", "persons/bao-liang.md",
    "候选为果园厂雕漆名手包亮（L4391）。`institutions/guoyuanchang.md` 已并记包亮，但 `persons/` 无人物条；来源只给姓名、营缮所副职与与张德刚同召的语境，未给籍贯与师承。建 person 条并逐项标未载，不据同段张德刚条补写。",
    "批准新建 persons/bao-liang.md；单册单源，consensus=tentative。",
    "写入 persons/bao-liang.md，新建；来源 L4391；籍贯、生卒、师承、作品与款识未载。",
))

D.append(C(
    "cand-11-61", "杨埙", "persons/yang-xun.md",
    "候选为金漆名家杨埙（L4412）。`persons/` 无杨埙；`terms/jin-qi.md` 同批新建，已记其赴日学艺、仿倭漆与杨倭漆之名。来源加大村西崖评语，给“习倭法而加以己意”与五色金钿缥霞山水人物的评述。建 person 条，与金漆条、蒋回回条互指。",
    "批准新建 persons/yang-xun.md；单册单源，consensus=tentative。",
    "写入 persons/yang-xun.md，新建；来源 L4412；生卒、籍贯、赴日年代、传世作品与款识未载。",
))

D.append(C(
    "cand-11-60", "百宝嵌", "terms/baibaoqian.md",
    "候选为百宝嵌（L4408、L4757-L4762）。`terms/` 无百宝嵌条；`persons/zhou-zhu.md` 同批新建，承担周翥个人与周制得名。来源给扬州产地、周制与《骨董琐记》全段引文，列嵌料与嵌件范围；另一跨段在清章重述周制。按工艺类型建 term 条，scope 记为明章全章加清章 L4757-L4762 一段，清章其余部分留待 T12。",
    "批准新建 terms/baibaoqian.md；单册单源，consensus=tentative；scope 含清章 L4757-L4762 的合并候选段。",
    "写入 terms/baibaoqian.md，新建；来源 L4408、L4757-L4762；嵌件工序、胎骨种类、尺寸与传世品清单未载。",
))

D.append(C(
    "cand-11-69", "陆子冈", "persons/lu-zigang.md",
    "候选为琢玉名家陆子冈（L4464）。`persons/` 无陆子冈；`procedures/yudiao-taocai-qiaose.md` 记玉雕巧色，不载人物。来源给吴中、琢玉、所选玉料与“吴中绝技”评语，并记其作品与茶晶花插。建 person 条，与茶晶花插作品条互指。",
    "批准新建 persons/lu-zigang.md；单册单源，consensus=tentative。",
    "写入 persons/lu-zigang.md，新建；来源 L4464；生卒、师承、作坊、传世作品清单与款识未载。",
))

D.append(C(
    "cand-11-70", "陆子冈梅花茶晶花插", "works/lu-zigang-tea-crystal-vase.md",
    "候选为陆子冈梅花茶晶花插（L4460-L4464）。`works/` 无此器；`persons/lu-zigang.md` 同批新建，只承担人物。来源给茶晶材质、梅花题材与器名花插，未给尺寸、藏地与款识。按单器建 work 条，标未视觉核验。",
    "批准新建 works/lu-zigang-tea-crystal-vase.md；单册单源，consensus=tentative。",
    "写入 works/lu-zigang-tea-crystal-vase.md，新建；来源 L4460-L4464；尺寸、藏地、款识位置与图版核验未载。",
))

D.append(C(
    "cand-11-71", "嘉定派", "terms/jiading-school.md",
    "候选为嘉定派竹刻（L4470-L4472）。`terms/` 无嘉定派条；来源给嘉定产地、朱鹤开创、朱小松与朱三松传承及风格评语。建 term 条承担流派，人物另立朱鹤、朱小松、朱三松三条，作品另立竹刻香薰条，不把流派、人物与单器混为一条。",
    "批准新建 terms/jiading-school.md；单册单源，consensus=tentative。",
    "写入 terms/jiading-school.md，新建；来源 L4470-L4472；流派成员全谱、刀法分类与传世作品清单未载。",
))

D.append(C(
    "cand-11-72", "金陵派", "terms/jinling-school.md",
    "候选为金陵派竹刻（L4474）。`terms/` 无金陵派条；来源给金陵产地、濮仲谦为代表与风格评语。建 term 条承担流派，濮仲谦另立人物条，与嘉定派条并列而不合并。",
    "批准新建 terms/jinling-school.md；单册单源，consensus=tentative。",
    "写入 terms/jinling-school.md，新建；来源 L4474；流派成员全谱、刀法分类与传世作品清单未载。",
))

D.append(C(
    "cand-11-73", "濮仲谦", "persons/pu-zhongqian.md",
    "候选为金陵竹刻名家濮仲谦（L4474）。`persons/` 无濮仲谦；`terms/jinling-school.md` 同批新建，只在流派条内提名。来源给金陵、姓名、以竹刻著称与风格评语，未给生卒与作品。建 person 条，与金陵派条互指。",
    "批准新建 persons/pu-zhongqian.md；单册单源，consensus=tentative。",
    "写入 persons/pu-zhongqian.md，新建；来源 L4474；生卒、师承、作坊、传世作品与款识未载。",
))

D.append(C(
    "cand-11-74", "朱鹤", "persons/zhu-he.md",
    "候选为嘉定竹刻开创者朱鹤（L4472）。`persons/` 无朱鹤；`terms/jiading-school.md` 同批新建，只在流派条内记开创。来源给字号松邻、嘉定、开创竹刻与风格评语。建 person 条，与嘉定派条、朱小松条、朱三松条互指。",
    "批准新建 persons/zhu-he.md；单册单源，consensus=tentative。",
    "写入 persons/zhu-he.md，新建；来源 L4472；生卒、师承、传世作品与款识未载。",
))

D.append(C(
    "cand-11-96", "朱小松", "persons/zhu-xiaosong.md",
    "候选为朱小松（L4472）。`persons/` 无朱小松；`terms/jiading-school.md` 同批新建，只在流派条内记传承。来源给字号、为朱鹤之子与风格评语，并带竹刻香薰作品。建 person 条，与嘉定派条及竹刻香薰作品条互指。",
    "批准新建 persons/zhu-xiaosong.md；单册单源，consensus=tentative。",
    "写入 persons/zhu-xiaosong.md，新建；来源 L4472；生卒、师承细节、传世作品清单与款识未载。",
))

D.append(C(
    "cand-11-97", "朱三松", "persons/zhu-sansong.md",
    "候选为朱三松（L4472）。`persons/` 无朱三松；`terms/jiading-school.md` 同批新建，只在流派条内记传承。来源给字号、为朱小松之侄与风格评语。建 person 条，与嘉定派条及朱小松条互指。",
    "批准新建 persons/zhu-sansong.md；单册单源，consensus=tentative。",
    "写入 persons/zhu-sansong.md，新建；来源 L4472；生卒、师承细节、传世作品与款识未载。",
))

D.append(C(
    "cand-11-98", "嘉定朱小松竹刻香薰", "works/jiading-zhu-xiaosong-bamboo-censer.md",
    "候选为嘉定朱小松竹刻香薰（L4477）。`works/` 无此器；`persons/zhu-xiaosong.md` 同批新建，只承担人物。来源给器名、材质、作者与图注语境，未给尺寸、藏地与纹样细节。按单器建 work 条，标未视觉核验。",
    "批准新建 works/jiading-zhu-xiaosong-bamboo-censer.md；单册单源，consensus=tentative。",
    "写入 works/jiading-zhu-xiaosong-bamboo-censer.md，新建；来源 L4477；尺寸、藏地、纹样细节与图版核验未载。",
))

D.append(C(
    "cand-11-99", "花纹犀角杯", "works/rhinoceros-horn-cup.md",
    "候选为花纹犀角杯（L4480）。`works/` 无此器；`places/dehua-yao.md` 只记德化窑仿犀角杯，不收原作。来源给器名、材质与花纹，未给尺寸、藏地与刻工；同段提到的包天成、蒋烈卿尚未立条，按来源缺载处理，不提前建人物条。建 work 条，标未视觉核验。",
    "批准新建 works/rhinoceros-horn-cup.md；单册单源，consensus=tentative。",
    "写入 works/rhinoceros-horn-cup.md，新建；来源 L4480；尺寸、藏地、刻工、纹样细节与图版核验未载。",
))

D.append(C(
    "cand-11-92", "雕漆小盒", "works/diaoqi-small-box.md",
    "候选为雕漆小盒（L4398）。`terms/diao-qi.md` 记雕漆分类与工序，不收单器；`works/` 无此器。来源给器名、雕漆品种与盒的器形，未给尺寸、藏地与纹样。按单器建 work 条，标未视觉核验。",
    "批准新建 works/diaoqi-small-box.md；单册单源，consensus=tentative。",
    "写入 works/diaoqi-small-box.md，新建；来源 L4398；尺寸、藏地、纹样细节与图版核验未载。",
))

D.append(C(
    "cand-11-93", "填漆", "terms/tianqi-lacquer.md",
    "候选为填漆（L4402）。`terms/` 无填漆条；`institutions/guoyuanchang.md` 记果园厂填漆，但没有工艺定义条。来源给填漆的作法与与雕漆的分工描述。建 term 条，与雕漆条、果园厂条互指，不把填漆并入雕漆。",
    "批准新建 terms/tianqi-lacquer.md；单册单源，consensus=tentative。",
    "写入 terms/tianqi-lacquer.md，新建；来源 L4402；填漆用料、工序细节、典型器物与产地未载。",
))

D.append(C(
    "cand-11-94", "姜千里", "persons/jiang-qianli.md",
    "候选为嘉兴螺钿名家姜千里（L4406）。`terms/luodian.md` 已记姜千里式，但 `persons/` 无人物条；来源给嘉兴、姓名、独创风格与姜千里式之名。建 person 条，与螺钿条互指，不重复螺钿工艺总述。",
    "批准新建 persons/jiang-qianli.md；单册单源，consensus=tentative。",
    "写入 persons/jiang-qianli.md，新建；来源 L4406；生卒、师承、作坊、传世作品与款识未载。",
))

D.append(C(
    "cand-11-95", "金漆", "terms/jin-qi.md",
    "候选为金漆（L4412）。`terms/` 无金漆条；`persons/jiang-huihui.md` 与 `persons/yang-xun.md` 同批新建，分别承担两位艺人。来源给苏州金漆、蒋回回的金漆彩绘与杨埙仿倭漆两条线索，未给金漆工艺的配料与工序。建 term 条，与两条人物条互指，工艺细节逐项标未载。",
    "批准新建 terms/jin-qi.md；单册单源，consensus=tentative。",
    "写入 terms/jin-qi.md，新建；来源 L4412；金漆配料、髹涂工序、典型器物与产地分布未载。",
))

D.append(UPD(
    "cand-11-15", "明代工匠轮班、存留、住坐制度", "terms/jianghu.md",
    "候选为明代工匠的轮班、存留、住坐三类（L4176-L4178）。`terms/jianghu.md` 已据高丰记匠籍、轮班与住坐，并已引田自秉 L3957-L3959 的元代段；本条新增同册 L4178 的存留一类、洪武十二年班制令、“月役一句”、宣德附籍与嘉靖征银，属同册多跨段。按同册规则追加 citation 与 location，source_count 保持 3，version 2→3，并补五条核心内容。",
    "批准更新 terms/jianghu.md；田自秉 citation 追加 L4176-L4178，source_count 保持 3、version 2→3、日期续期。",
    "更新 terms/jianghu.md，追加同册 L4176-L4178 与存留、班制令、月役、嘉靖征银五条；原元代段保留。",
))

D.append(UPD(
    "cand-11-63", "《髹饰录》三法", "publications/xiu-shi-lu.md",
    "候选为《髹饰录》三法（L4416）。`publications/xiu-shi-lu.md` 已立条并已从高丰收“巧法造化，质则人身，文象阴阳”，但无田自秉的三法释义，且其田自秉 citation 误记 L4240、location 误记 L4236-L4260，实为龙泉窑顾氏段。本批把田自秉 citation 更正为 L4387 与 L4416，补三法释义、内容范围与“现存唯一”原句，属同册更正加补写。source_count 保持 5，version 1→2。",
    "批准更新 publications/xiu-shi-lu.md；田自秉 citation 更正为 L4387、L4416，补三法释义与内容范围，source_count 保持 5、version 1→2。",
    "更新 publications/xiu-shi-lu.md，更正错位引文并补三法释义；原高丰三法条保留。",
))

D.append(N(
    "cand-11-35", "法花", "terms/fahua-qi.md",
    "候选为法花（L4268）。`terms/fahua-qi.md` 已引 L4268 全文，并已处理法花、珐华、法华三名、釉陶胎、凸线轮廓、蓝紫绿釉、山西阳城与长治与平阳产地及万历最佳等要点。若另立条或再更新，只会在同一来源同一句上重复。记 no_delta，目标 terms/fahua-qi.md。",
    "批准 no_delta；法花由 terms/fahua-qi.md 承担，本批不重复写回。",
    "no_delta：L4268 已由 terms/fahua-qi.md 全文收录，不另建条、不重复追加。",
))

cfg = {
    "doc": DOC,
    "file": SRC,
    "rules": RULES,
    "scope_spans": [[4170, 4502], [4757, 4762]],
    "scope_note": "第十章明代的工艺美术（L4170-L4502）全章；另含合并候选 cand-11-60 的清代跨段 L4757-L4762（百宝嵌周制重述），清代其余章节留待 T12。图版只读图注，未视觉核验。",
    "decisions": D,
}

out = ROOT / "_zn_decisions_t11.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({"decisions": len(D), "creates": sum(1 for d in D if d["action"] == "create"), "updates": sum(1 for d in D if d["action"] == "update"), "no_delta": sum(1 for d in D if d["action"] == "no_delta")}, ensure_ascii=False))
