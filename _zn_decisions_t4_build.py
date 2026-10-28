# -*- coding: utf-8 -*-
"""Build Tian Zibing 2010 batch T4 (Spring-Autumn / Warring States) decisions JSON."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-05-05", "鹰首壶", "04-knowledge/units/works/yingshou-hu.md",
     "候选为 1970 年山东诸城出土的战国鹰首壶（L1750、L1758）。检索 works 下无同器条；`terms/xiangsheng-xing.md` 已把鹰首壶列为春秋战国象生造型的实例，并注“尚未成条”，但那是类型条，不是器物条。新建器物条：记鹰首口盖、活环相联、开启而不脱落与图注，并把类型讨论留在象生造型条。来源未给尺寸、藏地、墓号与同出器物，confidence 取 medium。",
     "批准新建 04-knowledge/units/works/yingshou-hu.md：器物层单独立条，象生造型的类型讨论不重复。",
     "写入 works/yingshou-hu.md（新建）；引用 L1750、L1758；不据来源外材料补尺寸与藏地。"),
    ("cand-05-06", "雕金镶玉银带钩", "04-knowledge/units/works/diaojin-xiangyu-yin-daigou.md",
     "候选为 1953 年辉县固围村出土的战国雕金镶玉银带钩（L1869、L1871）。检索 works 下无同器条；`terms/belt-hook.md` 已在代表作一条引用同一句，但该条是带钩类型与胡服渊源的条目，不承担单器登记。新建器物条：记包金镶嵌、浮雕蟠龙鹦鹉与“精美的作品”的评价，并保留带钩约始于春秋初期的年代范围。来源未给尺寸、重量、藏地与墓号，confidence 取 medium。",
     "批准新建 04-knowledge/units/works/diaojin-xiangyu-yin-daigou.md：类型条继续记带钩制度与用途，本条只记单器。",
     "写入 works/diaojin-xiangyu-yin-daigou.md（新建）；引用 L1869、L1871；与 terms/belt-hook.md 互指而不重复。"),
    ("cand-05-09", "彩绘鹿鼓", "04-knowledge/units/works/caihui-lugu.md",
     "候选为 1972 年江陵拍马山楚墓出土的彩绘鹿鼓二件（L2022）。检索 works 下无同器条；`places/jiangling-chumuqun.md` 已提及彩绘鹿鼓并标出鼓径 1.4 厘米与鹿身长 33 厘米的比例异常，但那是遗址条。新建器物条：记鹿高 28、身长 33 厘米，伏卧侧视，鹿背凹凸榫安小鼓，鼓径 1.4 厘米，黑漆鹿身朱黄斑纹，鼓面卷云纹；比例照录，不代为解释。来源未给藏地、墓号与木质，confidence 取 medium。",
     "批准新建 04-knowledge/units/works/caihui-lugu.md：单器立条，鼓径与鹿身的比例只照录。",
     "写入 works/caihui-lugu.md（新建）；引用 L2022；与 places/jiangling-chumuqun.md 互指。"),
    ("cand-05-10", "舞女漆奁", "04-knowledge/units/works/wunv-qilian.md",
     "候选为长沙楚墓出土的舞女漆奁（L2016）。检索 works 下无同器条；`places/changsha-chumuqun.md` 已记长沙楚墓出舞女漆奁与 11 个舞女，但未单独立条。新建器物条：记奁身黑红带状分割、红地黑衣白袖领的色彩对比，以及 11 个舞女有立有坐、有正有侧的姿态。来源未给尺寸、胎质、藏地与墓号，confidence 取 medium。",
     "批准新建 04-knowledge/units/works/wunv-qilian.md：单器立条，人物画与色彩配置归本条。",
     "写入 works/wunv-qilian.md（新建）；引用 L2016；与 places/changsha-chumuqun.md 互指。"),
    ("cand-05-11", "龙凤虎纹绣衣", "04-knowledge/units/works/longfenghuwen-xiuyi.md",
     "候选为江陵马山砖厂一号墓出土的战国龙凤虎纹绣衣（L1972，彩版图注 L104）。检索 works 下无同器条；`procedures/ci-xiu-hua.md` 记刺绣针法，但不是器物条。新建器物条：记绣地多用绢、针法以辫绣为主局部平绣、蟠曲龙与飞舞凤、昂首扬尾猛虎及红黑斑纹，并并存正文“绣衣”与图注“绣罗禅衣局部”两名。来源未给尺寸、墓号与藏地，confidence 取 medium。",
     "批准新建 04-knowledge/units/works/longfenghuwen-xiuyi.md：器物层立条，针法条继续记工艺。",
     "写入 works/longfenghuwen-xiuyi.md（新建）；引用 L1972、L104；正文器名与图注名并存。"),
    ("cand-05-13", "几何纹凤鸟纹锦", "04-knowledge/units/works/jihexingwen-fengniaowen-jin.md",
     "候选为江陵马山砖厂一号墓出土的几何纹凤鸟纹锦（L1962、L1964）。检索 works 下无同器条；`works/wudao-renwu-dongwu-wen-sanse-jin.md` 是同墓所出的另一件三色锦，不合并。新建器物条：记双色锦、花纹带状排列、凤纹与六边形/菱形纹组成并列二方连续、色彩交替使简单纹样产生复杂效果。来源未给尺寸、经纬密度、织物组织与藏地，confidence 取 medium。",
     "批准新建 04-knowledge/units/works/jihexingwen-fengniaowen-jin.md：与同墓舞人动物纹锦分条。",
     "写入 works/jihexingwen-fengniaowen-jin.md（新建）；引用 L1962、L1964；不补密度与组织。"),
    ("cand-05-16", "蟠螭纹", "04-knowledge/units/terms/panchi-wen.md",
     "候选为春秋战国青铜器最主要的装饰纹样蟠螭纹（L1784、L1787、L1818、L1855）。检索 terms 下无蟠螭纹专条；`terms/taotie-motif.md` 只在兽面纹条提及蟠螭的流行，`terms/kui-wen.md` 记夔纹，均不收蟠螭的释名与蟠虺关系。新建术语条：记蟠为缠绕叠压、螭为无角小龙，后期蟠虺纹，虺为小蛇；并收青铜器比较表的四方连续与铜镜上的镂空、活环实例。图注“蟻螭纹”为 OCR 异文，两存。来源未给型式分类与年代序列，confidence 取 medium。",
     "批准新建 04-knowledge/units/terms/panchi-wen.md：纹样专条，与兽面纹、夔纹条互指。",
     "写入 terms/panchi-wen.md（新建）；引用 L1784、L1787、L1818、L1855；OCR 异文照录不径改。"),
    ("cand-05-18", "四叶纹", "04-knowledge/units/terms/siye-wen.md",
     "候选为战国铜镜的四叶纹（L1840、L1845）。检索 terms 下无四叶纹专条；`terms/tongjing.md` 的田自秉更新会总述八类镜纹，但总类条不收单纹的形制、地纹与正名讨论。新建术语条：记叶纹的蟠桃/枫叶/团扇/佛光/绒球等形，中心嵌宝石，羽状或回纹作地，荷花说与《楚辞》《古今注》《尔雅》引文，以及“四瓣花纹”正名与战国中期流行期。两段之间隔插图 10，未跨行拼接引文。来源未给型式分类与楚镜占比，confidence 取 medium。",
     "批准新建 04-knowledge/units/terms/siye-wen.md：单纹立条，铜镜总类条只作索引。",
     "写入 terms/siye-wen.md（新建）；引用 L1840、L1845；荷花说标明为来源判断。"),
    ("cand-05-19", "山字纹", "04-knowledge/units/terms/shanzi-wen.md",
     "候选为战国楚镜的山字纹（L1847）。检索 terms 下无山字纹专条；`terms/tongjing.md` 的更新只作八类镜纹总述。新建术语条：记数量最多、几达楚镜出土数 80%，四山为早期、五六山较晚，四山对称、五山环转并构成五角星状空间，雷纹演变说与古金文说，以及《礼记》郑玄注、《释名》《说文》的安定养物之义。80% 为来源统计表述，未给口径与样本量，照录不换算。confidence 取 medium。",
     "批准新建 04-knowledge/units/terms/shanzi-wen.md：单纹立条，统计口径照录。",
     "写入 terms/shanzi-wen.md（新建）；引用 L1847；80% 不换算为绝对数。"),
    ("cand-05-26", "齐纨鲁缟", "04-knowledge/units/terms/qiwan-lugao.md",
     "候选为春秋战国齐鲁地区最著名的丝织品齐纨、鲁缟（L1954、L1956、L1958）。检索 terms 下无齐纨鲁缟条；`terms/ling-silk.md` 记绫类丝织品，`places/linzi.md` 记齐国临淄，均不收齐鲁染织名产。新建术语条：记齐纨鲁缟全国闻名、齐国染织产量最大与“冠带衣履天下”之喻，并收《韩非子·说林上》鲁人织屦妻织缟的故事与《左传》楚国索鲁国缝工、织工各百人的记载。来源未给纨、缟的织法与规格，confidence 取 medium。",
     "批准新建 04-knowledge/units/terms/qiwan-lugao.md：名产立条，与临淄、绫类条互指。",
     "写入 terms/qiwan-lugao.md（新建）；引用 L1954、L1956、L1958；不补织法与产量。"),
    ("cand-05-28", "蚀花石髓", "04-knowledge/units/terms/shihua-shisui.md",
     "候选为石髓经化学腐蚀显花的蚀花石髓（L2035）。检索 terms 下无蚀花石髓条；`places/xichuan-xiasi-chumu.md` 已记淅川下寺楚墓出蚀花石髓，但那是遗址条。新建术语条：记石髓即玉髓、硬度 7、肉红石髓，花纹不用雕刻而用碳酸钠或碳酸铅溶液绘画、炭火烘烤、酸腐蚀使肉红变白，形状有枣核/圆/方，纹样有圆圈/直线/十字/曲线，河南淅川春秋楚墓发现最早实物。来源未给件数、尺寸与石髓产地，confidence 取 medium。",
     "批准新建 04-knowledge/units/terms/shihua-shisui.md：工艺术语立条，与淅川遗址条互指。",
     "写入 terms/shihua-shisui.md（新建）；引用 L2035；“最早实物”标明为来源判断。"),
    ("cand-05-29", "琉璃", "04-knowledge/units/terms/liuli.md",
     "候选为琉璃，跨度含战国原始玻璃（L2039-L2045）与元代建筑琉璃（L4015-L4017、L4024）两义。检索 terms 下无琉璃通条；`procedures/liuli-shaozhao.md` 只记明清建筑琉璃烧造，`terms/bi.md` 记玉璧，均不覆盖两义。新建术语条并列两义：第一义为原始玻璃，中国自制属铅钡玻璃、西方属钠钙玻璃，战国能作大件，琉璃璧最大直径 16 厘米，楚墓八十多座出土琉璃璧，多仿玉作代用品；第二义为建筑铅釉陶，汉代普遍制造、六朝用于建筑、唐“剪边琉璃”、宋《营造法式》釉料配方、元代山西产地最著。两义不合并。来源未给化学成分数据与窑址，confidence 取 medium；scope_spans 因此加读 L4013-L4026。",
     "批准新建 04-knowledge/units/terms/liuli.md：两义并列，不合并为单一定义。",
     "写入 terms/liuli.md（新建）；引用 L2039-L2045、L4015-L4017、L4024；两义分界写入正文。"),
    ("cand-05-86", "漆双凤鼓", "04-knowledge/units/works/qi-shuangfeng-gu.md",
     "候选为江陵楚墓出土的漆双凤鼓（L2022、L2025）。检索 works 下无同器条；`places/jiangling-chumuqun.md` 已提及漆双凤悬鼓，但那是遗址条。新建器物条：记双凤作鼓架、两兽作鼓座、双凤首悬一圆鼓，造形优美、极富装饰性；正文作“漆双凤悬鼓”，图注作“漆双凤鼓”，两名并存。来源未给尺寸、藏地、墓号与鼓面材质，confidence 取 medium。",
     "批准新建 04-knowledge/units/works/qi-shuangfeng-gu.md：单器立条，正文与图注名并存。",
     "写入 works/qi-shuangfeng-gu.md（新建）；引用 L2022、L2025；与彩绘鹿鼓互指。"),
    ("cand-05-81", "蔡侯鼎", "04-knowledge/units/works/caihou-ding.md",
     "候选只有图注“蔡侯鼎(春秋)”（L1705）。检索 works 下无同器条；`terms/ding.md` 记鼎的器类与形制演变，但图注未给蔡侯鼎的个体形制。图注紧接 L1702 鼎的形制演变段，该段讲春秋战国鼎的一般演变，未点名蔡侯鼎，不能把一般描述归到本器。新建作品条只登记图注层信息：器名、春秋、图注位置；尺寸、铭文、出土墓与藏地均未载，confidence 取 low。",
     "批准新建 04-knowledge/units/works/caihou-ding.md：只登记图注层，不据图补写器形。",
     "写入 works/caihou-ding.md（新建）；引用 L1705；confidence=low，图版未视觉核验。"),
]

UPDATES = [
    ("cand-05-02", "宴乐水陆攻战铜壶", "04-knowledge/units/works/yanle-shuilu-gongzhan-wen-hu.md",
     "候选为田自秉所记宴乐水陆攻战铜壶（L1760、L1768）。检索发现 `works/yanle-shuilu-gongzhan-wen-hu.md` 已据高丰、赵农立条，但只记成都百花潭一件与上、下段题材，未收田自秉的两件存世、镶嵌、三层六组与三角形连续卷云纹花边。按同实体更新：补田自秉一节，注明其未说明所描述的是哪一件；追加 2010 册 citation。跨册更新，source_count 2→3，version 2→3。",
     "批准更新 works/yanle-shuilu-gongzhan-wen-hu.md：补两件存世、三层六组与花边，画面描述标为类属描述。",
     "追加田自秉 L1760、L1768；source_count 2→3，version 2→3；器名异文并存为别名。",
     "canonical: 04-knowledge/units/works/yanle-shuilu-gongzhan-wen-hu.md。cand-05-02 并入既有壶条。"),
    ("cand-05-07", "曾侯乙墓铜尊、铜盘", "04-knowledge/units/works/zenghouyi-zunpan.md",
     "候选为曾侯乙墓铜尊、铜盘（L1812、L1814）。检索发现 `works/zenghouyi-zunpan.md` 已据赵农、夏燕靖 2016 立条，但只记尊立于盘上、透雕与内外两层铜梗，未收失蜡法异名、文献线索、四项特点与淅川下寺最早制件。按同实体更新：补田自秉的失蜡法一节，并保留原两册的组合与结构描述；追加 2010 册 citation。跨册更新，source_count 2→3，version 1→2。",
     "批准更新 works/zenghouyi-zunpan.md：补失蜡法异名、四项特点、曾侯乙例证与淅川最早制件。",
     "追加田自秉 L1812、L1814；source_count 2→3，version 1→2；四特点逐条照录。",
     "canonical: 04-knowledge/units/works/zenghouyi-zunpan.md。cand-05-07 并入既有尊盘条。"),
    ("cand-05-08", "彩绘漆座屏", "04-knowledge/units/works/caiqi-mudiao-dongwu-zuoping.md",
     "候选为江陵楚墓的彩绘漆座屏（L2022，彩版 13 图注 L99）。检索发现 `works/caiqi-mudiao-dongwu-zuoping.md` 已据夏燕靖两版立条，记 50 余个动物与黑底朱红金银灰绿，但未收尺寸、51 只之数、天星观近似屏座与“彩绘漆座屏”器名。按同实体更新：补田自秉一节，并列 50 余与 51 两只计数，不互相折算；追加 2010 册 citation。跨册更新，source_count 2→3，version 1→2。",
     "批准更新 works/caiqi-mudiao-dongwu-zuoping.md：补尺寸、51 只、天星观近似器与器名异文。",
     "追加田自秉 L2022、L99；source_count 2→3，version 1→2；两套计数并列。",
     "canonical: 04-knowledge/units/works/caiqi-mudiao-dongwu-zuoping.md。cand-05-08 并入既有座屏条。"),
    ("cand-05-12", "舞人动物纹锦", "04-knowledge/units/works/wudao-renwu-dongwu-wen-sanse-jin.md",
     "候选为田自秉所记舞人动物纹锦（L1962、L1966）。检索发现 `works/wudao-renwu-dongwu-wen-sanse-jin.md` 已据夏燕靖两版立条，记 7 单元、5.5×49.1 厘米与 156×52 根/平方厘米，但未收龙凤麒麟舞蹈人、波折三角形骨架、双菱纹与 S 纹及“首见”“最华丽最有特色”的评价。两册器名不同而特征相合，按同实体更新并加同器判断与拆分条件；追加 2010 册 citation。跨册更新，source_count 2→3，version 1→2。",
     "批准更新 works/wudao-renwu-dongwu-wen-sanse-jin.md：补田自秉的图案构成与评价，并标同器判断。",
     "追加田自秉 L1962、L1966；source_count 2→3，version 1→2；器名不同，暂按一器处理。",
     "canonical: 04-knowledge/units/works/wudao-renwu-dongwu-wen-sanse-jin.md。cand-05-12 并入既有锦条。"),
    ("cand-05-15", "钟鸣鼎食", "04-knowledge/units/terms/chunqiu-zhanguo-qingtong-chuishiqi.md",
     "候选为钟鸣鼎食的组合（L1692）。检索发现 `terms/chunqiu-zhanguo-qingtong-chuishiqi.md` 已据夏燕靖 2016 记“失去祭祀和礼器的特性”与十类器形，但未收商代酒器、周代食器、春秋战国钟鸣鼎食的三段对照。按同实体更新：补三段说，不新建重复的钟鸣鼎食术语条；追加 2010 册 citation。跨册更新，source_count 1→2，version 1→2。",
     "批准更新 terms/chunqiu-zhanguo-qingtong-chuishiqi.md：补商、周、春秋战国三段组合的对照。",
     "追加田自秉 L1692；source_count 1→2，version 1→2；十类器形原表保留。",
     "canonical: 04-knowledge/units/terms/chunqiu-zhanguo-qingtong-chuishiqi.md。cand-05-15 并入既有炊食器条。"),
    ("cand-05-17", "战国铜镜", "04-knowledge/units/terms/tongjing.md",
     "候选为田自秉所记战国铜镜（L1822-L1836、L1838-L1865）。检索发现 `terms/tongjing.md` 已据夏燕靖两版、赵农立条，记四大特点、齐家文化说与唐镜，但未收田自秉的四期说、宋以后玻璃镜、淮式/秦式即楚镜、妇好墓早期镜、南北两系、楚为产地与八类镜纹。按同实体更新：补田自秉一节，连弧纹与地纹为前三册未收；追加 2010 册 citation。跨册更新，source_count 3→4，version 1→2。",
     "批准更新 terms/tongjing.md：补四期、形制、楚镜判断、南北两系与八类镜纹。",
     "追加田自秉 L1822-L1836、L1838-L1865；source_count 3→4，version 1→2；四特点与夏燕靖并列。",
     "canonical: 04-knowledge/units/terms/tongjing.md。cand-05-17 并入既有铜镜条。"),
    ("cand-05-38", "干将、莫邪", "04-knowledge/units/persons/ganjiang.md",
     "候选为干将、莫邪（L1873-L1877）。检索发现 `persons/ganjiang.md` 已据赵农 L1905 记《吴越春秋》故事，但未收田自秉的剑器兴起、吴越制剑、传说流传于吴国、龙泉与季札挂剑。按同实体更新：补田自秉一节，并明确他只说传说流传于吴国，未称干将本人为吴国人，nationality 仍作“未载”；追加 2010 册 citation。跨册更新，source_count 1→2，version 1→2。",
     "批准更新 persons/ganjiang.md：补吴越制剑背景与季札挂剑，不把传说地域改写为国籍。",
     "追加田自秉 L1873-L1877；source_count 1→2，version 1→2；国别边界写入正文。",
     "canonical: 04-knowledge/units/persons/ganjiang.md。cand-05-38 并入既有干将条。"),
]

NODELTA = [
    ("cand-05-27", "羽觞", "04-knowledge/units/terms/qi-erbei.md",
     "候选为羽觞（L1996）。`terms/qi-erbei.md` 已收羽觞为别名，并记杯体椭圆、双耳、《楚辞》“瑶浆蜜勺，实羽觞些”与定名/形制/制法/成本。田自秉同句只把“蜜勺”作“密勺”，无新增属性；版本异文不足以改条，故记 no_delta。",
     "不新建：羽觞已由 terms/qi-erbei.md 以别名与正文承载，田自秉仅提供一处异文。",
     "no_delta：目标 terms/qi-erbei.md 已覆盖 L1996；异文“密勺”不单独立条。",
     "canonical: 04-knowledge/units/terms/qi-erbei.md。cand-05-27 并入既有耳杯条。"),
    ("cand-05-37", "庄子（庄周）", "04-knowledge/units/persons/zhuangzi.md",
     "候选为庄子（L1980）。`persons/zhuangzi.md` 已收《史记》“庄子者，蒙人也，名周，尝为漆园吏”全句与专官管理漆园的解释，并已引田自秉 L1105、L1980、L4859。候选无新增属性，故记 no_delta。",
     "不新建：庄子的姓名、籍贯、漆园吏与专官管理已由 persons/zhuangzi.md 承载。",
     "no_delta：目标 persons/zhuangzi.md 已引田自秉 L1980；不新建。",
     "canonical: 04-knowledge/units/persons/zhuangzi.md。cand-05-37 并入既有庄子条。"),
    ("cand-05-41", "老子（老庄）", "04-knowledge/units/persons/laozi.md",
     "候选为老子与老庄并称（L2063）。`persons/laozi.md` 已据夏燕靖两版收《老子》“埏埴以为器，当其无，有器之用”与有无空间观；田自秉同句只多一“也”字并作老庄并称，无新增命题，故记 no_delta。",
     "不新建：埏埴与有无空间观已由 persons/laozi.md 承载，老庄并称不构成新条。",
     "no_delta：目标 persons/laozi.md 已覆盖 L2063 的命题；不新建。",
     "canonical: 04-knowledge/units/persons/laozi.md。cand-05-41 并入既有老子条。"),
    ("cand-05-82", "金错铜豆（战国）", "04-knowledge/units/terms/dou-vessel.md",
     "候选只有图注“金错铜豆(战国)”（L1736）。`terms/dou-vessel.md` 已记豆的器类、盖可翻置作盘与形制，图注未给该器的尺寸、藏地、纹样与金银错细节，无法立器物条；图版也未视觉核验。故记 no_delta，不新建只有图注的作品条。",
     "不新建：仅有图注，无器物数据；豆的器类已由 terms/dou-vessel.md 承载。",
     "no_delta：L1736 只有图注；不据图补写尺寸与纹样。",
     "canonical: 04-knowledge/units/terms/dou-vessel.md。cand-05-82 不另立。"),
    ("cand-05-83", "“金银错鸟耳”壶（战国）", "04-knowledge/units/terms/hu-vessel.md",
     "候选只有图注“金银错鸟耳”壶(战国)（L1796）。`terms/hu-vessel.md` 已记壶的器类与式样；图注未给该器的尺寸、藏地、鸟耳形制与金银错纹样，无法立器物条。故记 no_delta，不新建只有图注的作品条。",
     "不新建：仅有图注，无器物数据；壶的器类已由 terms/hu-vessel.md 承载。",
     "no_delta：L1796 只有图注；不据图补写尺寸与纹样。",
     "canonical: 04-knowledge/units/terms/hu-vessel.md。cand-05-83 不另立。"),
    ("cand-05-84", "山字纹镜（战国）", "04-knowledge/units/terms/shanzi-wen.md",
     "候选只有图注“山字纹镜(战国)”（L1843）。本批新建的 `terms/shanzi-wen.md` 已记山字纹的形制、四山/五山、构图与释义；图注未给该镜的尺寸、藏地与型式，无法另立器物条。故记 no_delta，指向山字纹条。",
     "不新建：图注只有纹样名；山字纹已由本批 terms/shanzi-wen.md 承载。",
     "no_delta：L1843 只有图注；不据图补写镜式与尺寸。",
     "canonical: 04-knowledge/units/terms/shanzi-wen.md。cand-05-84 不另立。"),
    ("cand-05-85", "连弧夔纹镜（战国）", "04-knowledge/units/terms/tongjing.md",
     "候选只有图注“连弧夔纹镜(战国)”（L1863）。本批更新的 `terms/tongjing.md` 已收连弧纹的弧数、装饰位置与战国末期至汉代的流行期，并收夔凤纹；图注未给该镜的尺寸、藏地与型式，无法另立器物条。故记 no_delta，指向铜镜条。",
     "不新建：图注只有纹样名；连弧纹与夔凤纹已由本批 terms/tongjing.md 承载。",
     "no_delta：L1863 只有图注；不据图补写镜式与尺寸。",
     "canonical: 04-knowledge/units/terms/tongjing.md。cand-05-85 不另立。"),
]


decisions = []
for suffix, entity, target, analysis, approve, apply_note in CREATES:
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

for suffix, entity, target, analysis, approve, apply_note, note in NODELTA:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": entity,
        "action": "no_delta",
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
        "只有图注、无器物数据的候选记 no_delta，不新建只有图注的作品条",
    ],
    "scope_spans": [[1674, 2068], [4013, 4026]],
    "scope_note": "田自秉 2010 册第四章春秋战国的工艺美术（L1674-L2068）逐段复读，含概说、青铜工艺、陶瓷、染织、漆器、玉器与结语；另因琉璃候选的两义，定点复读元代琉璃节 L4013-L4026。彩版 9-15 与插图 1-14 只读图注，未视觉核验。",
    "decisions": decisions,
    "notes": "田自秉 2010 册 batch T4：春秋战国 unit 候选 28 条，create 14、update 7、no_delta 7。新建含六件青铜与漆器作品、一件刺绣衣、一件织锦、六种纹样与名产术语（蟠螭、四叶、山字、齐纨鲁缟、蚀花石髓、琉璃）、一件仅有图注的蔡侯鼎；更新宴乐水陆攻战壶、曾侯乙尊盘、彩绘漆座屏、舞人动物纹锦、春秋战国青铜炊食器、铜镜与干将；七条图注或既有条目以 no_delta 关闭。",
}

out = ROOT / "_zn_decisions_t4.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
