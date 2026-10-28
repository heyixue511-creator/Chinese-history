# -*- coding: utf-8 -*-
"""Build T13 decisions JSON for the 2010 Tian Zibing modern chapters (12-13)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
U = "04-knowledge/units/"

RULES = [
    "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
    "更新既有条目：只追加本批复读的新段落，不据新段改写原有段落的记述，version+1，source_count 按来源册数不变",
    "逐字引文用“ ”，跨行拼接用「 」，作者自撰短语不引号，正文禁 ASCII 双引号，嵌套引号用‘ ’",
    "图版只著录图注原文并标未视觉核验，不据图像补写尺寸、藏地与出土地点",
    "同名异物或同词两义并列著录，不合并为单一定义",
    "来源未给作者、正字或年代时照录原文并存疑，不据来源外材料补写",
    "类型条与单器条分工：总类、制法、纹样与题材归术语条，单件器物的尺寸、出土与画面归作品条",
    "人物条只承担籍贯、身份、师承、得名与评语；工艺定义、工序与产地归术语条，两组互指不合并",
    "T12 保留的跨章合并候选在本批复读全跨度后裁定，不沿用上一批的合并跨度作为已读证明",
    "单册内相距较远的两段合为一条时，逐段标注行号，不把中间未引段落算作已引",
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


D = []

D.append(C(
    "cand-12-106", "《资政新篇》", "publications/zizheng-xinpian.md",
    "候选为《资政新篇》（L4935-L4937）。`publications/` 无该文献条；`terms/` 与 `institutions/` 记太平天国工艺制度的有 `institutions/zhujiangying.md`（诸匠营）、`institutions/baigongya.md`（百工衙），二者记生产组织，不收文献。来源两处连续引用同一文献，分别给益民的工艺观（以有用之物为宝、精奇利便、以坚固轻便捷巧为妙）与保护创造发明的工艺政策（准其自售、仿造收为己有或招为徒、按器之大小与益民多寡给赏、限满他人仿做），并称其已提出版权问题。建 publication 条，与诸匠营、百工衙互指而不合并。",
    "批准新建 publications/zizheng-xinpian.md；单册单源，consensus=tentative。",
    "写入 publications/zizheng-xinpian.md，新建；来源 L4935、L4937；作者、成书与刊行年代、卷数、版本与全书体例未载。",
))

D.append(C(
    "cand-12-109", "直捣清廷", "works/zhidao-qingting.md",
    "候选为《直捣清廷》石雕（L4951）。`works/` 无太平天国石雕条；`terms/` 无谐音象征题材条。来源只一句，给画面构成（战船前方一只向下坠落的蜻蜓）与全段共有的谐音象征手法（用蜻蜓示清廷），据此把器物与其手法一并著录。按单器建 work 条，标未视觉核验；尺寸、石料、作者与收藏地未载。",
    "批准新建 works/zhidao-qingting.md；单册单源，consensus=tentative，confidence=low。",
    "写入 works/zhidao-qingting.md，新建；来源 L4951；尺寸、石料、作者、出土或收藏地、制作年份与图像未载。",
))

D.append(C(
    "cand-12-110", "消灭清廷", "works/xiaomie-qingting.md",
    "候选为《消灭清廷》石雕（L4951）。与 cand-12-109 同段并列而各自成器，画面为凤凰傲立、回首怒视身后的蜻蜓，寓意清廷将亡。`works/` 无该器条。两器共用谐音手法但构图与寓意不同，分建两条并互指，不合并为一条题材条。",
    "批准新建 works/xiaomie-qingting.md；单册单源，consensus=tentative，confidence=low。",
    "写入 works/xiaomie-qingting.md，新建；来源 L4951；尺寸、石料、作者、出土或收藏地、制作年份与图像未载。",
))

D.append(C(
    "cand-13-01", "崔来志", "persons/cui-laizhi.md",
    "候选为崔来志（L5013）。`persons/` 无该人条；`terms/` 无自来格或花布设计条。来源给其身份（359 旅排长）、设计成果（70 多种花布）、织机改造（织毯机改作织布机、不必换梭而织出自来格）与出席边区群英大会，并把大生产运动的纺织规模作为背景数据同段列出。人物条只承担设计者身份与成果，不把边区纺织统计并入。",
    "批准新建 persons/cui-laizhi.md；单册单源，consensus=tentative。",
    "写入 persons/cui-laizhi.md，新建；来源 L5013；生卒、籍贯、受教育经历、花布图样与织机改造的具体结构未载。",
))

D.append(C(
    "cand-13-09", "解放日报", "publications/jiefang-ribao.md",
    "候选为《解放日报》（L5013-L5025）。`publications/` 无该报条。来源两处引用：L5013 记党中央机关报曾三次发表纺织社论并列出三篇篇名与日期，L5025 记 1944 年 5 月 13 日报道延安桥儿沟陶瓷厂以石膏模型与改造窑炉提高产量质量。建 publication 条，只承担报纸身份与所引报道，社论内容归相关工艺条，报纸沿革不据来源外材料补写。",
    "批准新建 publications/jiefang-ribao.md；单册单源，consensus=tentative。",
    "写入 publications/jiefang-ribao.md，新建；来源 L5013、L5025；创刊与终刊年份、社长与主编、发行量与发行范围、三篇社论的作者未载。",
))

D.append(C(
    "cand-13-50", "选花会", "terms/xuanhuahui.md",
    "候选为选花会（L5126）。`terms/` 无该制度条；`institutions/` 记设计机构的有 `institutions/zhongguo-fangzhi-jianshe-gongsi.md` 等生产公司，不收群众性征询活动。来源给设立缘由（提高印花布艺术设计、多次召开设计会议、了解人民需要并听取群众对图案的意见）、名称与性质判断（社会主义制度的产物）。名称所指是活动而非常设机构，故建 term 条而不建 institution 条。",
    "批准新建 terms/xuanhuahui.md；单册单源，consensus=tentative。",
    "写入 terms/xuanhuahui.md，新建；来源 L5126；起始年份、举办频次、组织单位、评选程序与入选图案的去向未载。",
))

D.append(C(
    "cand-13-79", "化学纤维", "terms/huaxue-xianwei.md",
    "候选为化学纤维（L5132-L5134）。`terms/` 记纺织材料的有 `terms/kesi.md`、`terms/zhijin.md` 与刺绣体系的 `terms/suxiu.md`，均以天然纤维为前提，不收化纤。来源给人造纤维与合成纤维的分类、各自原料（天然纤维素；煤、石油、天然气）、十万吨化纤折合二三百万亩棉田的经济意义、两类纤维的性能差异与混纺取长补短的理由。建 term 条，材料属性归 B 维度，经济意义归 D 维度。",
    "批准新建 terms/huaxue-xianwei.md；单册单源，consensus=tentative。",
    "写入 terms/huaxue-xianwei.md，新建；来源 L5097、L5132-L5134；各纤维的化学组成、生产工艺、产量数据与价格未载。",
))

D.append(C(
    "cand-13-02", "杨守玉", "persons/yang-shouyu.md",
    "候选为杨守玉（L5142）。`persons/` 无该人条。来源只说她是丹阳正则女校的刺绣创作者、乱针绣（正则绣、缤纹绣）的创始人，并给该针法的特征；生卒、籍贯、师承与作品均未载。人物条与针法条分建：人物条承担创绣身份与校名，针法条承担技法定义与在苏绣中的位置。",
    "批准新建 persons/yang-shouyu.md；单册单源，consensus=tentative。",
    "写入 persons/yang-shouyu.md，新建；来源 L5142；生卒、籍贯、师承、任教经历、作品清单与该绣法的传习范围未载。",
))

D.append(C(
    "cand-13-44", "乱针绣", "terms/luanzhenxiu.md",
    "候选为乱针绣（L5142）。`terms/` 无该针法条；`terms/suxiu.md` 记双面绣与苏绣体系，本批同时新建并把乱针绣列为苏绣发展较快的两种针法之一，两条互指不合并。来源给创者、两个别名（正则绣、缤纹绣）与针法特征（长短不一、直斜交错的综合针法，表现形体与色光效果而有立体感）。",
    "批准新建 terms/luanzhenxiu.md；单册单源，consensus=tentative。",
    "写入 terms/luanzhenxiu.md，新建；来源 L5140-L5142；具体操作步骤、用线规格、色线层数与代表作品未载。",
))

D.append(C(
    "cand-13-24", "《长城》壁挂", "works/changcheng-bigua.md",
    "候选为《长城》壁挂（L5154）。`works/` 无该件条；`terms/ditan.md` 记地毯的产地、帮派、纹样与栽绒工艺，不收单件。来源只在地毯品种处一句，给赠送对象（我国送给联合国）与巨型挂毯的定位，并给地毯与丝毯的定义、解放以来踏毯卧毯挂毯的品种序列。建 work 条并标未视觉核验；尺寸、制作单位、设计者与年代未载。",
    "批准新建 works/changcheng-bigua.md；单册单源，consensus=tentative，confidence=low。",
    "写入 works/changcheng-bigua.md，新建；来源 L5154；尺寸、制作单位、设计者、完成年代、陈列地点与图像未载。",
))

D.append(C(
    "cand-13-32", "花丝", "terms/huasi.md",
    "候选为花丝（L5164-L5170）。`terms/` 记金属细工与珐琅的有 `terms/jingtai-lan.md`（铜胎掐丝珐琅）、`terms/hua-falang.md`（铜胎画珐琅），二者以铜胎为体，本条以金银细丝为体，材质路径不同。来源给定义、前身（战国金银错与唐代平脱）、材料可塑性、编堆穿镶錾五种技法、产品与首饰清单、三处产地与液化石油气灯代替吹灯烧焊的改进。",
    "批准新建 terms/huasi.md；单册单源，consensus=tentative。",
    "写入 terms/huasi.md，新建；来源 L5164-L5170；金银丝拉制与退火工序、五种技法各自的操作、成色与克重、作坊与产量未载。",
))

D.append(C(
    "cand-13-33", "斑铜", "terms/bantong.md",
    "候选为斑铜（L5182）。`terms/tongjin.md` 记铜禁与铜器制度，`terms/xuande-censer.md` 记宣德炉用料，均不收云南地方铜器品种。来源给产地与地位、得名、生斑与熟斑的分法、与古代青铜器基本相同的五道工序、虎牛等题材与庄重浑厚的风格。建 term 条，生熟两类并列著录。",
    "批准新建 terms/bantong.md；单册单源，consensus=tentative。",
    "写入 terms/bantong.md，新建；来源 L5182；铜料成分与杂质比例、加锌量、着色剂、艺人、作坊与产量未载。",
))

D.append(UPD(
    "cand-13-34", "铁画", "procedures/tiehua-zhizuo.md",
    "候选为铁画的新中国段（L5186）。`procedures/tiehua-zhizuo.md` 已据本册清代段 L4733-L4735 建条，记创制者汤天池、材料与五道工序，不含产地，location 明记来源未给具体产地。L5186 给出产地主要在安徽芜湖、解放后北京上海山东等地生产、大型挂屏与题材扩展到神话传说与历史故事。同一实体同一来源的续记，作 update 追加，不另建条。",
    "批准更新 procedures/tiehua-zhizuo.md；追加 L5186，source_count 仍为 1，version 2。",
    "更新 procedures/tiehua-zhizuo.md；来源 L4733-L4735, L5186；补产地、产品与题材三项并将 location 由未记产地改为芜湖等；钢片厚度、含碳量与各产地规模仍未载。",
    note=f"canonical: {U}procedures/tiehua-zhizuo.md。cand-13-34 并入该条，不另建。",
))

D.append(UPD(
    "cand-13-35", "北京雕漆", "terms/diao-qi.md",
    "候选为北京雕漆（L5192-L5196）。`terms/diao-qi.md` 已据高丰与田自秉两册建条，记唐宋元明的源流、命名与清代造办处，不含北京果园厂源流、继古斋、1914 年巴拿马博览会与新中国雕漆厂。L5192-L5196 为同一工艺的北京一路续记，作 update 追加，不另建北京雕漆条。",
    "批准更新 terms/diao-qi.md；追加 L5192-L5196，source_count 仍为 2，version 2。",
    "更新 terms/diao-qi.md；来源 L5192-L5196；补北京源流、近代获奖与民国畸形发展、新中国雕漆厂与镂空手法；既有田自秉跨段位置待核的说明保留。",
    note=f"canonical: {U}terms/diao-qi.md。cand-13-35 并入该条，不另建北京雕漆条。",
))

D.append(C(
    "cand-13-36", "扬州螺钿", "terms/yangzhou-luodian.md",
    "候选为扬州螺钿（L5200-L5202）。`terms/luodian.md` 记螺钿的宋明源流与软硬之分，`terms/dianluo.md` 记同属扬州的点螺，`works/luodian-zhuiqi-zanhe.md` 记单器攒盒，均不收扬州螺钿的平嵌一路。来源给时代、平嵌做法、光线下变幻的光泽、朴素典雅的风格、大件与小件的器类与解放前后的产销状况。扬州一路有独立做法与器类体系，建独立 term 条并与螺钿、点螺互指。",
    "批准新建 terms/yangzhou-luodian.md；单册单源，consensus=tentative。",
    "写入 terms/yangzhou-luodian.md，新建；来源 L5200-L5202；起始年代、贝壳种类、嵌片厚度、艺人、作坊与产量未载。",
))

D.append(C(
    "cand-13-03", "李芝卿", "persons/li-zhiqing.md",
    "候选为李芝卿（L5206）。`persons/` 无该人条；`terms/tuotai-qiqi.md` 已记脱胎的工艺与沈沼安，并将在本批追加福州传统与三种装饰方法，但不过录艺人姓名。来源给其身份（著名漆艺老艺人）与赤宝砂的创制，以及赤宝砂、绿宝砂、金丝玛瑙的做法与效果。人物条承担创制者身份与三种变体，工艺定义归脱胎条。",
    "批准新建 persons/li-zhiqing.md；单册单源，consensus=tentative。",
    "写入 persons/li-zhiqing.md，新建；来源 L5206；生卒、籍贯、师承、从业年代、作品目录与传习谱系未载。",
))

D.append(UPD(
    "cand-13-37", "福州脱胎漆器", "terms/tuotai-qiqi.md",
    "候选为福州脱胎漆器（L5206）。`terms/tuotai-qiqi.md` 已据田自秉 L4770 与夏燕靖 2016 建条，记夹纻工艺、沈沼安创制与三宝，不含田自秉对福州一路的记述。L5206 给清代以来的传统定位、轻巧艳丽的器体、赤宝砂与李芝卿、沉花平花浮花三法、生活器皿与汽车等工业产品的应用。同一实体同一来源的续记，作 update 追加，不另建福州脱胎条。",
    "批准更新 terms/tuotai-qiqi.md；追加 L5204-L5206，source_count 仍为 2，version 2。",
    "更新 terms/tuotai-qiqi.md；来源 L4770, L5204-L5206；补福州传统、赤宝砂与三种装饰方法、工业产品应用；胎骨层数与重量数据仍未载。",
    note=f"canonical: {U}terms/tuotai-qiqi.md。cand-13-37 并入该条，不另建福州脱胎条。",
))

D.append(C(
    "cand-13-38", "研磨彩绘", "terms/yanmo-caihui.md",
    "候选为研磨彩绘（L5212）。`terms/` 无该技法条；`terms/tuotai-qiqi.md` 记沉花平花浮花三种装饰方法，属福州一路，本条是重庆解放后兴起的罩漆研磨一路，工序不同。来源给兴起地点与时段、四步工序（描绘金银花纹加彩漆、干后全面罩漆、研磨显出花纹）与代表作金鱼漆盘。",
    "批准新建 terms/yanmo-caihui.md；单册单源，consensus=tentative。",
    "写入 terms/yanmo-caihui.md，新建；来源 L5212；金银材料、彩漆层数、研磨用料、工序时长与艺人未载。",
))

D.append(C(
    "cand-13-85", "金鱼漆盘", "works/jinyu-qipan.md",
    "候选为金鱼漆盘（L5212）。`works/` 无该器条；`terms/yanmo-caihui.md` 在本次同时新建并以它为代表作，技法条收工序，本条收单器的画面效果与两次世界青年联欢节获奖。来源未给尺寸、作者、年份与收藏地，标未视觉核验。",
    "批准新建 works/jinyu-qipan.md；单册单源，consensus=tentative，confidence=low。",
    "写入 works/jinyu-qipan.md，新建；来源 L5212；尺寸、作者、制作年份、收藏地点、获奖届次与图像未载。",
))

D.append(C(
    "cand-13-04", "龚玉璋", "persons/gong-yuzhang.md",
    "候选为龚玉璋（L5232）。`persons/` 无该人条。来源给其所处世代（龚扇第二代）、技艺贡献（发展与提高、闻名中外、多次出国展览）与龚扇的源起（清末龚姓一家所创）。人物条承担艺人身份与贡献，器类定义与用工数据归龚扇条。",
    "批准新建 persons/gong-yuzhang.md；单册单源，consensus=tentative。",
    "写入 persons/gong-yuzhang.md，新建；来源 L5232；生卒、籍贯、师承、传艺谱系、作品目录与展览场次未载。",
))

D.append(C(
    "cand-13-26", "龚扇（自贡竹丝扇）", "terms/gongshan.md",
    "候选为龚扇（L5232）。`terms/` 无该器类条；`procedures/zhubian-yishu-jiagong.md` 记竹编五种艺术加工方法，不收具体扇种。来源给源起、材质效果（薄如蝉翼、光泽似绢、扇面织图案字画）、用丝数量与穿纬次数、复杂处的劈丝处理。器类条与艺人条分建互指。",
    "批准新建 terms/gongshan.md；单册单源，consensus=tentative。",
    "写入 terms/gongshan.md，新建；来源 L5232；竹种、劈丝工序、扇框材料、器形尺寸与产量未载。",
))

D.append(C(
    "cand-13-05", "章水泉", "persons/zhang-shuiquan.md",
    "候选为章水泉（L5240）。`persons/` 无该人条；`places/` 下广济尚未立条，不据外部资料补建地名条。来源给其竹家具名手身份、拼竹技法（小竹片拼椅面、竹枝牙拼图案）与风格评价，并以广济古称蕲州、韩愈诗与《群芳谱》引文记产地沿革。人物条承担艺人身份与技法，产地文献引证随条著录而不另建 place 条。",
    "批准新建 persons/zhang-shuiquan.md；单册单源，consensus=tentative。",
    "写入 persons/zhang-shuiquan.md，新建；来源 L5240；生卒、籍贯、师承、作品目录、家具尺寸与制作年代未载。",
))

D.append(C(
    "cand-13-48", "特种工艺", "terms/tezhong-gongyi.md",
    "候选为特种工艺（L5266）。`terms/` 无该类称条；`terms/xiaopin-diaoke.md` 记清代小品雕刻、`terms/xiangyazhu.md` 与 `terms/huasi.md` 记具体品类，均不收类称。来源给类称由来（材料昂贵、作工精细而由实用品转为欣赏品）、旧中国被洋行买办掠夺摧残与半殖民地烙印、民间木雕石雕泥塑面塑的对照、新中国剔除糟粕吸收精华并开展创新。类称属生产体制与分类概念，建 term 条并归 D 维度。",
    "批准新建 terms/tezhong-gongyi.md；单册单源，consensus=tentative。",
    "写入 terms/tezhong-gongyi.md，新建；来源 L5266；类称的起始年代、外销数量与价格、各工种从业人员规模未载。",
))

D.append(C(
    "cand-13-06", "翁五章", "persons/weng-wuzhang.md",
    "候选为翁五章（L5272）。`persons/` 无该人条。来源给创始者身份、传艺第四代与层数进展（几十层、目前四十层左右）。人物条承担创始与传艺，器类定义与清代十余层的技术起点归象牙球条。",
    "批准新建 persons/weng-wuzhang.md；单册单源，consensus=tentative。",
    "写入 persons/weng-wuzhang.md，新建；来源 L5272；生卒、籍贯、师承、创制年份、作品目录与传艺谱系未载。",
))

D.append(C(
    "cand-13-28", "象牙球", "terms/xiangyazhu.md",
    "候选为象牙球（L5272）。`terms/` 无该器类条；`terms/xiaopin-diaoke.md` 记清代小品雕刻的类目与艺人，不收象牙球。来源跨两段：清代段 L4822 记牙雕用染色与拼镶、象牙球已能刻十余层；新中国段 L5272 记广州牙雕以象牙球闻名、翁五章创始、传艺四代与四十层左右。两段合成一条并逐段标行号。",
    "批准新建 terms/xiangyazhu.md；单册单源，consensus=tentative。",
    "写入 terms/xiangyazhu.md，新建；来源 L4822, L5272；球径、每层厚度、掏层工具、工序时长与成品数量未载。",
))

D.append(C(
    "cand-13-25", "《红旗插上珠穆朗玛峰》玉雕", "works/hongqi-chashang-zhumulangmafeng.md",
    "候选为《红旗插上珠穆朗玛峰》玉雕（L5290）。`works/` 无该件条；`works/dayu-zhishui-yushan.md` 记清代大禹治水图玉山，`procedures/yudiao-taocai-qiaose.md` 记玉雕套裁与巧色，均不收本件。来源一句给题材（四十一个登山运动员）、重量（三吨）与作品地位，同段另给玉雕产地序列。建 work 条并标未视觉核验。",
    "批准新建 works/hongqi-chashang-zhumulangmafeng.md；单册单源，consensus=tentative。",
    "写入 works/hongqi-chashang-zhumulangmafeng.md，新建；来源 L5290；创作年份、作者姓名、玉料种类、尺寸、收藏地点与图像未载。",
))

D.append(C(
    "cand-13-30", "藏族饲养员（黄杨木雕）", "works/zangzu-siyangyuan-huangyangmudiao.md",
    "候选为图注所记藏族饲养员黄杨木雕（L5297）。`works/` 无该件条。来源只有图注器名与时代，另在 L5299 给木雕品种序列、L5301 给黄杨木的千年矮之称与材质、技法特色。按图版锚点建 work 条，标未视觉核验与逐项未载；不据图注补写作者与流派。",
    "批准新建 works/zangzu-siyangyuan-huangyangmudiao.md；单册单源，consensus=tentative，confidence=low。",
    "写入 works/zangzu-siyangyuan-huangyangmudiao.md，新建；来源 L5297-L5301；作者、尺寸、创作年份、收藏地点与图像细节未载，未查看图像文件。",
))

D.append(C(
    "cand-13-29", "《蟹篓》寿山石雕", "works/xielou-shoushan.md",
    "候选为《蟹篓》（L5317）。`works/` 无该件条；`terms/shoushan-shidiao.md` 记寿山石雕的产地、沿革与艺人，不收单件。来源两句给寿山石雕的镂空手法与蟹篓的画面（鱼篓内外螃蟹的各种动态、刻划入微）。建 work 条，与同段并列的《花果累累》分建互指。",
    "批准新建 works/xielou-shoushan.md；单册单源，consensus=tentative。",
    "写入 works/xielou-shoushan.md，新建；来源 L5317；作者、尺寸、石种、创作年份、收藏地点与图像细节未载。",
))

D.append(C(
    "cand-13-84", "《花果累累》", "works/huaguo-leilei.md",
    "候选为《花果累累》（L5317）。与 cand-13-29 同段并列，来源只一句给作品名、较大体量与精美评价，无题材细节与尺寸。`works/` 无该件条。单器条目照录原文，不据作品名补写花果内容，confidence=low。",
    "批准新建 works/huaguo-leilei.md；单册单源，consensus=tentative，confidence=low。",
    "写入 works/huaguo-leilei.md，新建；来源 L5317；作者、尺寸、石种、创作年份、收藏地点与图像细节未载。",
))

D.append(C(
    "cand-13-07", "张景祜", "persons/zhang-jinghu.md",
    "候选为张景祜（L5323）。`persons/` 无该人条；同批新建的 `terms/nirenzhang.md` 记流派与五代世系，`persons/zhang-mingshan.md` 记第二代张明山。来源给其第四代位置与钻研新艺术理论、提高作品水平的作用，生卒与作品未载。人物条与流派条分建互指。",
    "批准新建 persons/zhang-jinghu.md；单册单源，consensus=tentative。",
    "写入 persons/zhang-jinghu.md，新建；来源 L4828, L5323；生卒、籍贯、作品目录、任教或任职经历与理论著述未载。",
))

D.append(C(
    "cand-13-27", "大阿福", "terms/da-a-fu.md",
    "候选为大阿福（L5325）。`terms/` 无该题材条；同批新建的 `terms/huishan-niren.md` 记惠山泥人的总称、沿革与简满明三字。来源跨两段：L4830 记因以制作阿福最有特色而得名大阿福或惠山泥阿福，L5325 记早期品种、著名传统题材与别称。题材条与品种条分建互指。",
    "批准新建 terms/da-a-fu.md；单册单源，consensus=tentative。",
    "写入 terms/da-a-fu.md，新建；来源 L4830, L5325；大阿福的造型细节、尺寸、泥料与彩绘工序、创制年代未载。",
))

D.append(C(
    "cand-13-08", "面人汤", "persons/mianren-tang.md",
    "候选为面人汤（L5327）。`persons/` 无该人条；`terms/` 无面塑条。来源给面塑定义与产地（面粉染色捏塑小型玩赏品，北京上海等地生产）、面人汤的身份、文学戏曲修养、观察生活的方法与细如线薄如纸、形态生动色调明快的效果。本名与生平未载，条名照录称号。",
    "批准新建 persons/mianren-tang.md；单册单源，consensus=tentative。",
    "写入 persons/mianren-tang.md，新建；来源 L5327；本名、生卒、籍贯、师承、作品目录与面泥配方未载。",
))

D.append(C(
    "cand-13-47", "现代工艺", "terms/xiandai-gongyi.md",
    "候选为现代工艺（L5331）。`terms/` 无该类称条；`terms/tezhong-gongyi.md` 在本次同时新建，记以欣赏品为主的类称，本条与之相对而记以新材料新技术生产的现代美术设计品。来源给类称定义、范围交错（染织化纤与光电提花、陶瓷新釉彩与滚压成型与隧道窑）、只就玻璃塑料搪瓷铝制品与人造材料家具作简略介绍，并明确否认绝对划分标准。",
    "批准新建 terms/xiandai-gongyi.md；单册单源，consensus=tentative。",
    "写入 terms/xiandai-gongyi.md，新建；来源 L5331；现代工艺的统计范围、产值、从业人数与分类标准未载。",
))

D.append(C(
    "cand-13-78", "铝制品", "terms/luzhipin.md",
    "候选为铝制品（L5361-L5363）。`terms/` 无该材器条；`terms/tongjin.md` 记铜器制度、`terms/bantong.md` 在本次同时新建记云南斑铜，铝器对铜锡铁器皿的替代关系不并入上述任一条。来源给材质（轻银之称）、替代关系、铝矿分布、辊压模压挤压拉制四法、磨光抛光洗白与电化镀色、造型为艺术表现主要手段与品种清单。",
    "批准新建 terms/luzhipin.md；单册单源，consensus=tentative。",
    "写入 terms/luzhipin.md，新建；来源 L5361-L5363；铝材牌号与厚度、各成型法的工艺参数、产量与价格未载。",
))

D.append(C(
    "cand-14-01", "人造材料家具", "terms/renzao-cailiao-jiaju.md",
    "候选为人造材料家具（L5365-L5370）。`terms/` 记家具的有 `terms/gaoxing-jiaju.md`（宋代高型家具）、`terms/ming-style-furniture.md` 与 `terms/qing-style-furniture.md`（明清两式）、`terms/qimu-jiaju.md`（漆木家具），均以天然木材为前提。来源给历代以木材为主的前提、人造板与钢管塑料的材料替代、由框式向板式的结构转变、省工轻便简洁明快的效果与钢管的型材与表面处理。",
    "批准新建 terms/renzao-cailiao-jiaju.md；单册单源，consensus=tentative。",
    "写入 terms/renzao-cailiao-jiaju.md，新建；来源 L5365-L5370；各类人造板的性能数据、钢管规格、家具品种清单与产量未载。",
))

D.append(C(
    "cand-14-02", "板式结构", "terms/banshi-jiegou.md",
    "候选为板式结构（L5367）。`terms/` 无该结构条；`terms/ming-style-furniture.md` 记明式硬木家具的榫卯与框式做法，本条是由框式转为板式的结构变化。来源一段给结构转变、材料前提与设计效果，节点与板材参数未载。结构概念独立成条，与人造材料家具条互指。",
    "批准新建 terms/banshi-jiegou.md；单册单源，consensus=tentative。",
    "写入 terms/banshi-jiegou.md，新建；来源 L5367；节点做法、连接件、板材厚度与规格、典型器例未载。",
))

D.append(C(
    "cand-14-07", "适用、经济、美观", "terms/shiyong-jingji-meiguan.md",
    "候选为适用、经济、美观（L5389）。`terms/` 无设计原则条；`01-domain/` 不收具体原则的条文。来源一句给原则名称与古为今用、推陈出新的方针，L5387 给民族风格与时代特色的双重要求。原则的提出年份、文件出处与逐项释义未载，照录不补。",
    "批准新建 terms/shiyong-jingji-meiguan.md；单册单源，consensus=tentative。",
    "写入 terms/shiyong-jingji-meiguan.md，新建；来源 L5387-L5389；提出年份、文件出处、三项原则的逐项定义与评价标准未载。",
))

D.append(C(
    "cand-14-08", "日用品美术化，工艺品实用化", "terms/riyongpin-meishuhua-gongyipin-shiyonghua.md",
    "候选为日用品美术化、工艺品实用化（L5389）。`terms/` 无该方针条；与 cand-14-07 同段而所指不同：一条给设计原则，一条给发展方向与双重属性的论证。来源给工艺美术的物质生产与精神生产双重属性、由此提出该方向。两条分建互指。",
    "批准新建 terms/riyongpin-meishuhua-gongyipin-shiyonghua.md；单册单源，consensus=tentative。",
    "写入 terms/riyongpin-meishuhua-gongyipin-shiyonghua.md，新建；来源 L5389；提出年份、文件出处、实施措施与成效评估未载。",
))

D.append(C(
    "cand-12-31", "苏绣", "terms/suxiu.md",
    "候选为苏绣（L4651-L5140）。T12 因候选跨度延伸至近代章之后未复读该段，保留 needs_evidence；本批复读全跨度，两段均在本册内可查。`terms/sida-mingxiu.md` 记四大名绣并称，`terms/xiangxiu.md`、`terms/shuxiu.md`、`terms/jingxiu.md` 分记另三种地方绣，无苏绣专条。来源清代段给《上海县志》引文、八字特点与 43 种针法；新中国段给从业人员最多、1957 年苏州刺绣研究所、猫与金鱼代表作、双面绣与乱针绣。建独立 term 条。",
    "批准新建 terms/suxiu.md；单册单源，consensus=tentative。",
    "写入 terms/suxiu.md，新建；候选跨度 L4651-L5140，实际引用 L4649、L4651-L4655、L5140-L5142；起始年代、绣工数量、各针法操作与传世品目录未载。",
))

D.append(C(
    "cand-12-80", "翻簧", "terms/fanhuang.md",
    "候选为翻簧（L4816-L5244）。T12 因跨度延伸至近代章未裁定；本批复读全跨度。`terms/liuqing.md` 记同列的留青，`terms/jiading-school.md`、`terms/jinling-school.md` 记竹刻流派，`procedures/zhubian-yishu-jiagong.md` 记竹编五种艺术加工方法，均无翻簧专条。来源清代段给技法分种、乾隆后期流行、去青皮煮压的制法与象牙质感；新中国段给竹编加工法中的位置、单双刀与火绘电绘、三处产地。",
    "批准新建 terms/fanhuang.md；单册单源，consensus=tentative。",
    "写入 terms/fanhuang.md，新建；候选跨度 L4816-L5244，实际引用 L4810、L4816、L5228、L5244；竹簧层厚、煮压温度与时间、器皿清单、艺人与作坊组织未载。",
))

D.append(C(
    "cand-12-82", "泥人张", "terms/nirenzhang.md",
    "候选为泥人张（L4826-L5323）。T12 因跨度延伸至近代章未裁定；本批复读全跨度。`terms/` 无泥人张条；`persons/zhang-mingshan.md` 记第二代张明山，本批另建 `persons/zhang-jinghu.md` 记第四代。来源清代段给得名、张万全至张铭张钺的五代世系与彩塑标准；新中国段给工艺定义、现实主义特色与张景祜的作用。流派条与人物条分建互指。",
    "批准新建 terms/nirenzhang.md；单册单源，consensus=tentative。",
    "写入 terms/nirenzhang.md，新建；候选跨度 L4826-L5323，实际引用 L4826-L4828、L5323；各代生卒、作品目录、泥料配方与传世品清单未载。",
))

D.append(C(
    "cand-12-84", "惠山泥人", "terms/huishan-niren.md",
    "候选为惠山泥人（L4830-L5325）。T12 因跨度延伸至近代章未裁定；本批复读全跨度。`terms/` 无惠山泥人条，`places/` 下无锡尚未立条，不据外部资料补建地名条。来源清代段给总称、大阿福别称、夸张与强烈色彩、香汛旺季与南洋销路；新中国段给四百年说、早期品种、1936 年后转用石膏与简满明三字。本批另建 `terms/da-a-fu.md` 记题材，两条互指。",
    "批准新建 terms/huishan-niren.md；单册单源，consensus=tentative。",
    "写入 terms/huishan-niren.md，新建；候选跨度 L4830-L5325，实际引用 L4830、L5325；四百年说的依据、泥料与彩绘工序、艺人姓名、作坊与产量未载。",
))

D.append(C(
    "cand-12-87", "料器", "terms/liaoqi.md",
    "候选为料器（L4846-L5339）。T12 因跨度延伸至近代章未裁定；本批复读全跨度。`terms/liuli.md` 记琉璃与玻璃的两个义项、`terms/glass.md` 记玻璃材料、`procedures/taoliao.md` 记套料配色与磨花、`works/hehua-wen-taohong-liaogang.md` 记单器，均无料器条。来源清代段给含铅低熔点的定义、造办处玻璃厂、产地、品种色彩与套料搅料等装饰法；新中国段给火焰喷头前拉制与小鸟兽花球类产品。",
    "批准新建 terms/liaoqi.md；单册单源，consensus=tentative。",
    "写入 terms/liaoqi.md，新建；候选跨度 L4846-L5339，实际引用 L4846、L4848-L4855、L5339；铅含量配比、烧成温度、套烧与磨花工序细节、各产地产量未载。",
))

cfg = {
    "doc": DOC,
    "file": SRC,
    "rules": RULES,
    "scope_spans": [[4901, 5389]],
    "scope_note": "第十二章近代的工艺美术（L4901-L5039）与第十三章新中国的工艺美术（L5041-L5389）全章复读并裁定 43 条：本范围内 38 条 needs_evidence 候选，加 T12 保留的 5 条跨章合并候选（cand-12-31 苏绣 L4651-L5140、cand-12-80 翻簧 L4816-L5244、cand-12-82 泥人张 L4826-L5323、cand-12-84 惠山泥人 L4830-L5325、cand-12-87 料器 L4846-L5339），后者两段现均在已复读范围内，故本批裁定 terminal。同范围内另有 25 条 unit 候选已于 2026-10-25 批次 applied，本批不重复裁定。L5391-L5715 为主要参考书目、L5717-L5737 为后记，二者无 unit 候选，未纳入本批复读范围，不记已复读。图版只读图注，未视觉核验。",
    "decisions": D,
}

out = ROOT / "_zn_decisions_t13.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({
    "decisions": len(D),
    "creates": sum(1 for d in D if d["action"] == "create"),
    "updates": sum(1 for d in D if d["action"] == "update"),
    "no_delta": sum(1 for d in D if d["action"] == "no_delta"),
}, ensure_ascii=False))
