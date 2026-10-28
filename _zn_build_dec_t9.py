# -*- coding: utf-8 -*-
"""Build T9 decisions JSON for the 2010 Tian Zibing Song chapter."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
U = "04-knowledge/units/"

RULES = [
    "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
    "同实体更新：跨册追加 source block，source_count+1、version+1、日期续期；同册多跨段追加 citation，source_count 不变",
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
    "cand-09-32", "荷叶敞口银杯", "works/heye-changkou-yinbei.md",
    "候选为辽代巴林窖藏所出荷叶敞口银杯（L3486）。检索 `works/` 无同器条目，`terms/` 无辽代金银器总条；来源给器名、同组金银器清单与注酒后的光学效果，未给尺寸、容量、藏地与图版。按单器建 work 条，与同段新建的契丹鞍分列（饮器与鞍具不同器类）。",
    "批准新建 works/heye-changkou-yinbei.md；单册单源，consensus=tentative。",
    "写入 works/heye-changkou-yinbei.md，新建；来源 L3486；尺寸、容量、藏地与图版未载。",
))

D.append(C(
    "cand-09-91", "契丹鞍", "works/qidan-an.md",
    "候选为契丹鞍（L3486）。检索 `works/` 无鞍具条，`terms/` 无马具总条；来源引《袖中锦》记契丹鞍与定瓷、蜀锦、端砚齐名，称天下第一，并记 1954 年赤峰大营子辽墓出土银质鎏金鞍饰，未给鞍的形制、尺寸与材质组合。建 work 条，所出鞍饰是否即《袖中锦》所称契丹鞍留作存疑。",
    "批准新建 works/qidan-an.md；单册单源，consensus=tentative。",
    "写入 works/qidan-an.md，新建；来源 L3486；形制、尺寸、藏地与鞍饰归属未载。",
))

D.append(C(
    "cand-09-54", "影青执壶（带温酒器）", "works/yingqing-zhihu.md",
    "候选为安徽宿松出土影青执壶（L3619）。`terms/yingqing.md` 记影青瓷类与田自秉 L3611-L3613，未收此器；`works/` 无同器。来源给流、把手、覆杯状盖与蹲兽纽、花瓣状温酒器与垂瓣，及胎釉描述，未给尺寸、窑口与藏地。按单器建 work 条，与影青术语条互指。",
    "批准新建 works/yingqing-zhihu.md；单册单源，consensus=tentative。",
    "写入 works/yingqing-zhihu.md，新建；来源 L3619；尺寸、窑口与藏地未载。",
))

D.append(C(
    "cand-09-63", "舒翁", "persons/shu-weng.md",
    "候选为吉州窑民窑窑主舒翁（L3649）。检索 `persons/` 无舒翁；`places/jizhou-kiln.md` 记吉州窑但未及窑主。来源记其所制紫、白色釉，大花瓶值金数两，善造瓷玩具，未给生卒、籍贯、窑名与作品存世。建 person 条，与吉州窑互指。",
    "批准新建 persons/shu-weng.md；单册单源，consensus=tentative。",
    "写入 persons/shu-weng.md，新建；来源 L3649；生卒、籍贯、窑名与作品存世未载。",
))

D.append(C(
    "cand-09-64", "舒娇", "persons/shu-jiao.md",
    "候选为舒翁之女舒娇（L3649）。检索 `persons/` 无舒娇；来源称其作品更佳，所造瓷炉几与哥窑等价，未给生卒、籍贯与作品存世，也未说明是否独立主持窑业。建 person 条，与舒翁条并列，不合并为家族合条。",
    "批准新建 persons/shu-jiao.md；单册单源，consensus=tentative。",
    "写入 persons/shu-jiao.md，新建；来源 L3649；生卒、籍贯、窑名与作品存世未载。",
))

D.append(C(
    "cand-09-66", "宋三彩（宋加彩）", "terms/song-sancai.md",
    "候选为宋三彩（L3682）。检索 `terms/` 有 `tang-sancai.md`、`liao-sancai.md`，无宋三彩条；`terms/mise-ci.md` 等他条不涉。来源记在白釉碗碟上加红绿彩绘再低温烧制、寥寥数笔、开启明清釉上五彩，并记禹县扒村与鲁山宋窑发现，未给胎土、烧成温度与铅含量。按陶瓷类型建 term 条，与唐三彩、辽三彩互指。",
    "批准新建 terms/song-sancai.md；单册单源，consensus=tentative。",
    "写入 terms/song-sancai.md，新建；来源 L3682；胎土、烧成温度、铅含量与器物清单未载。",
))

D.append(C(
    "cand-09-69", "鸡腿坛", "terms/jitui-tan.md",
    "候选为鸡腿坛（L3706-L3708）。`terms/liao-ci.md` 在标签与正文列鸡腿坛为契丹式器形，但无体形、用途与时代的具体记述；`terms/` 无独立条。来源记体形细长、小口、流行至金代，并列装酒发酵与帐中抱取两说，未给尺寸、容量与实例。按辽瓷器形建 term 条，补 liao-ci 的概括。",
    "批准新建 terms/jitui-tan.md；单册单源，consensus=tentative。",
    "写入 terms/jitui-tan.md，新建；来源 L3706-L3708；尺寸、容量、胎釉与出土实例未载。",
))

D.append(C(
    "cand-09-70", "白瓷盘口长颈瓶", "works/baici-pankou-changjing-ping.md",
    "候选为 1953 年赤峰西大营子村西山辽墓出土白瓷盘口长颈瓶（L3704）。`works/` 无此器；`terms/` 无盘口长颈瓶条，且 `terms/pan-kou-hu.md` 为六朝盘口壶，器类不同，不作合并。来源记辽瓷常见式样、与唐瓷宋瓷的传统联系及朱彩画龙贴金，未给尺寸、釉色细节与藏地。建 work 条。",
    "批准新建 works/baici-pankou-changjing-ping.md；单册单源，consensus=tentative。",
    "写入 works/baici-pankou-changjing-ping.md，新建；来源 L3704；尺寸、釉色细节、藏地与图版未载。",
))

D.append(C(
    "cand-10-89", "凤首壶", "terms/fengshou-hu.md",
    "候选为凤首壶（L3721-L3723）。`terms/liao-ci.md` 列凤首瓶，非凤首壶；`works/` 无辽代凤首壶条目。来源记其为辽瓷常见品种、与有系扁提壶并列、式样仿唐式演变，插图 16 图注列凤首壶，未给尺寸、釉色与出土实例。按器形建 term 条，图注只录原文。",
    "批准新建 terms/fengshou-hu.md；单册单源，consensus=tentative。",
    "写入 terms/fengshou-hu.md，新建；来源 L3721-L3723；尺寸、釉色、出土实例与唐辽形制差异未载。",
))

D.append(C(
    "cand-10-31", "正定龙兴寺铜佛", "works/zhengding-longxingsi-tongfo.md",
    "候选为正定龙兴寺铜佛（L3843）。`works/` 无此器，`places/zhengding.md` 未建；来源记高七丈三尺、42 臂、分 7 次铸成，引《正定县志》记自莲花台座逐层升至头顶的七接铸法，地基用工役 3000 人，未给始铸年代、主持者、铜料用量与现存状况。建 work 条。",
    "批准新建 works/zhengding-longxingsi-tongfo.md；单册单源，consensus=tentative。",
    "写入 works/zhengding-longxingsi-tongfo.md，新建；来源 L3843；始铸年代、主持者、铜料用量与现存状况未载。",
))

D.append(C(
    "cand-10-32", "新铜器", "terms/xin-tongqi.md",
    "候选为新铜器（L3847）。检索 `terms/` 无新铜器条，`places/` 无句容、台州铜作条；来源记其为后人为区别商周铜器而对宋代铜器的称法，引《文房肆考》记句容、台州铸地，未给器形清单、合金与断代标准。按器物类别建 term 条，与宋镜条互指。",
    "批准新建 terms/xin-tongqi.md；单册单源，consensus=tentative。",
    "写入 terms/xin-tongqi.md，新建；来源 L3847；器形清单、合金成分与断代标准未载。",
))

D.append(C(
    "cand-10-34", "宋镜", "terms/song-jing.md",
    "候选为宋镜（L3853-L3871）。`terms/tongjing.md` 记铜镜总类与四期说，田自秉来源只引 L1822-L1865，未及宋代；`terms/liuchao-tongjing.md` 记六朝镜，器类时代不同。来源对宋镜的胎质、装饰、图案组织、镜式、产地与铸镜局有系统记述，足以另立时代类型条，避免把宋镜细节塞回通史条。",
    "批准新建 terms/song-jing.md；单册单源，consensus=tentative。",
    "写入 terms/song-jing.md，新建；来源 L3853-L3871；各期年代与尺寸未载。",
))

D.append(C(
    "cand-10-07", "绮", "terms/qi-silk.md",
    "候选为绮（L3759）。检索 `terms/` 无绮条；`terms/ling-silk.md` 记绫，`terms/luo.md` 等未建。来源引《六书·古文》《释名》《大藏音义》释名义与斜纹组织、记一色与两色、杯文棋文，并记金坛南宋墓四种小花绮的几何纹与折枝花绮，未给尺寸、密度与织机。按丝织类型建 term 条。",
    "批准新建 terms/qi-silk.md；单册单源，consensus=tentative。",
    "写入 terms/qi-silk.md，新建；来源 L3759；尺寸、密度与织机结构未载。",
))

D.append(C(
    "cand-10-08", "宋罗", "terms/song-luo.md",
    "候选为宋罗（L3763-L3773）。检索 `terms/` 无罗条；`procedures/lan-yinhua-bu.md` 等他条不涉。来源记罗与纱的区别、链式罗结构、宋罗生产与贡罗数量、素罗花罗、薛景石花罗织机、实地亮花与亮地暗花、名目与出土实例，材料足以建 term 条；薛景石与《梓人遗制》另由既有 publication 条承担，不重复立人物条。",
    "批准新建 terms/song-luo.md；单册单源，consensus=tentative。",
    "写入 terms/song-luo.md，新建；来源 L3763-L3773；尺寸、密度与各名目组织差异未载。",
))

D.append(C(
    "cand-10-12", "茂花闪色锦", "terms/maohua-shanse-jin.md",
    "候选为 1975 年银川西夏陵区所出茂花闪色锦（L3783-L3790）。检索 `terms/` 无此锦；`terms/kesi.md` 记缂丝，工艺不同。来源记分段扎染经线、织后直向参差彩斑、与和田印经类似、可能由西域回鹘工匠织造、经密 80～84 根每厘米与纬密 36～38 根，未给尺寸与完整纹样。建 term 条。",
    "批准新建 terms/maohua-shanse-jin.md；单册单源，consensus=tentative。",
    "写入 terms/maohua-shanse-jin.md，新建；来源 L3783-L3790；织物尺寸、完整纹样与藏地未载。",
))

D.append(C(
    "cand-10-23", "莲塘乳鸭图", "works/liantang-ruya-tu.md",
    "候选为朱克柔《莲塘乳鸭图》（L3818）。`persons/zhu-kerou.md` 已在人物条内记此图与藏地，但 `works/` 无独立作品条；来源（田自秉）只给作者、图名与古澹清雅的代表作判断，未给尺寸、材质、画面与工序，另册藏地信息属人物条既有来源，不在本条单源内补写。建最小 work 锚点，与朱克柔条互指。",
    "批准新建 works/liantang-ruya-tu.md；单册单源，consensus=tentative。",
    "写入 works/liantang-ruya-tu.md，新建；来源 L3818；尺寸、材质、藏地、画面与缂织工序未载。",
))

D.append(C(
    "cand-10-25", "唐仲友", "persons/tang-zhongyou.md",
    "候选为唐仲友（L3824）。检索 `persons/` 无唐仲友；`procedures/lan-yinhua-bu.md` 已引《朱文公集》记其彩帛铺，但无人物条。来源只记到任后关集工匠、雕造花板、印染数十片发归彩帛铺，未给生卒、官职、铺的规模与经营时间。建 person 条，与蓝印花布条互指。",
    "批准新建 persons/tang-zhongyou.md；单册单源，consensus=tentative。",
    "写入 persons/tang-zhongyou.md，新建；来源 L3824；生卒、官职、彩帛铺规模与经营时间未载。",
))

D.append(C(
    "cand-10-30", "对鸟对羊刺绣包首", "works/duiniao-duiyang-baoshou.md",
    "候选为新疆阿拉尔出土北宋对鸟对羊刺绣包首（L3834-L3837）。`works/` 无此器；`institutions/xiuyuan.md` 记绣院与宋绣，但无此包首。来源只记出土地、对鸟对羊花纹与宋绣平绣为主兼用锁线，未给尺寸、地色、绣线与藏地。建 work 条，图版信息未视觉核验。",
    "批准新建 works/duiniao-duiyang-baoshou.md；单册单源，consensus=tentative。",
    "写入 works/duiniao-duiyang-baoshou.md，新建；来源 L3834-L3837；尺寸、地色、绣线与藏地未载。",
))

D.append(C(
    "cand-10-38", "描金堆雕漆盒", "works/miaojin-duidiao-qihe.md",
    "候选为浙江瑞安出土描金堆雕漆盒（L3889）。`works/` 无此器；`terms/miaojin.md` 同批新建但为技法条。来源详记盒形、须弥座、连弧开光、描金人物波涛火焰散花、堆贴卷草与动物、珍珠嵌饰，并与密县三彩琉璃舍利盒比较，未给尺寸、漆色层次与藏地。建 work 条。",
    "批准新建 works/miaojin-duidiao-qihe.md；单册单源，consensus=tentative。",
    "写入 works/miaojin-duidiao-qihe.md，新建；来源 L3889；尺寸、漆色层次与藏地未载。",
))

D.append(C(
    "cand-10-40", "螺钿", "terms/luodian.md",
    "候选为螺钿（L3895，合并 cand-11-59 的 L4406 明段）。检索 `terms/` 无螺钿条；`terms/diao-qi.md` 记雕漆，`terms/xipi.md` 记犀皮，工艺不同。来源分记宋代的螺钿盒、柳箱、禁制与白螺片嵌铜丝，明代段又分硬螺钿、软螺钿、甸螺、甸砂与姜千里式；两段同一工艺而时代不同，合为一条并按段标注。",
    "批准新建 terms/luodian.md，收录 L3895 宋段与合并候选所指 L4406 明段；单册单源，consensus=tentative。",
    "写入 terms/luodian.md，新建；来源 L3895、L4406；宋代胎骨、嵌片厚度与器物清单未载。",
    "canonical: 04-knowledge/units/terms/luodian.md。cand-10-40 与 cand-11-59 合并入该条。",
))

D.append(C(
    "cand-10-42", "剔犀", "terms/tixi.md",
    "候选为剔犀（L3903-L3912）。`terms/diao-qi.md` 记雕漆总类与剔红、剔彩、剔黄、剔绿、剔黑，剔犀只经高丰来源提及；`terms/xipi.md` 为犀皮，非剔犀。来源给红黑漆相间涂后再雕、斜面形成红黑线纹，并以剔犀执镜盒与金坛雕漆扇柄为例，未给漆层总数、髹涂遍数与产地。建独立 term 条，与雕漆、犀皮分列。",
    "批准新建 terms/tixi.md；单册单源，consensus=tentative。",
    "写入 terms/tixi.md，新建；来源 L3903-L3912；漆层总数、髹涂遍数与产地未载。",
))

D.append(C(
    "cand-10-43", "剔犀执镜盒", "works/tixi-zhijinghe.md",
    "候选为剔犀执镜盒（L3905-L3906）。来源只以插图 21 图注作“剔犀执镜盒（南宋）”，正文无尺寸、形制、纹样与藏地；`works/` 无此器，剔犀工艺由同批 terms/tixi.md 承担。所指器物无其他条目承担，按图版锚点建最小 work 条，标未视觉核验与逐项未载。",
    "批准新建 works/tixi-zhijinghe.md；单册单源，图注仅记器名与时代，consensus=tentative。",
    "写入 works/tixi-zhijinghe.md，新建；来源 L3905-L3906 图注；尺寸、形制、纹样、藏地与出土信息未载，图版未视觉核验。",
))

D.append(C(
    "cand-10-44", "雕漆扇柄", "works/diaoqi-shanbing.md",
    "候选为 1975 年金坛宋墓团扇雕漆扇柄（L3912）。`works/` 无此器；`terms/tixi.md` 同批记剔犀工艺，本条为实例。来源记扇轴转动结构、雕镂与脱胎结合的制法、橄榄形轴头与脱离剂、透雕云头如意纹、君玉二字与红黑相间漆层，未给扇柄长度、扇面材质与藏地。建 work 条。",
    "批准新建 works/diaoqi-shanbing.md；单册单源，consensus=tentative。",
    "写入 works/diaoqi-shanbing.md，新建；来源 L3912；扇柄长度、扇面材质与藏地未载。",
))

D.append(C(
    "cand-10-85", "吴煦", "persons/wu-xu.md",
    "候选为南宋缂丝名手吴煦（L3818）。检索 `persons/` 无吴煦；`persons/zhu-kerou.md`、`persons/shen-zifan.md` 记另两位名家。来源只记其与朱克柔、沈子蕃并列为云间名家，及《蟠桃图》甚为精美，未给生卒、籍贯、师承与其他作品。建 person 条。",
    "批准新建 persons/wu-xu.md；单册单源，consensus=tentative。",
    "写入 persons/wu-xu.md，新建；来源 L3818；生卒、籍贯、师承与其他作品未载。",
))

D.append(C(
    "cand-10-86", "梅鹊图", "works/meique-tu.md",
    "候选为沈子蕃《梅鹊图》（L3818）。`persons/shen-zifan.md` 已记此图并另有《花鸟图》，`works/` 无独立条。来源只给作者、图名与甚为精美的判断，未给尺寸、材质、藏地与画面，建最小 work 锚点，与沈子蕃条互指。",
    "批准新建 works/meique-tu.md；单册单源，consensus=tentative。",
    "写入 works/meique-tu.md，新建；来源 L3818；尺寸、材质、藏地、画面与缂织工序未载。",
))

D.append(C(
    "cand-10-87", "蟠桃图", "works/pantao-tu.md",
    "候选为吴煦《蟠桃图》（L3818）。`works/` 无此图；吴煦人物条由同批新建。来源只给作者、图名与甚为精美的判断，未给尺寸、材质、藏地与画面，建最小 work 锚点。",
    "批准新建 works/pantao-tu.md；单册单源，consensus=tentative。",
    "写入 works/pantao-tu.md，新建；来源 L3818；尺寸、材质、藏地、画面与缂织工序未载。",
))

D.append(C(
    "cand-10-88", "描金", "terms/miaojin.md",
    "候选为描金（L3887）。检索 `terms/` 有 `qiangjin.md` 记戗金，描金只作并列品种提及；无描金专条。来源记描金亦称泥金、日本人称莳绘，并以阳江南宋墓黑漆底描金漆盒为例，未给用金量、胶结材料与产地。按漆器技法建 term 条，与戗金、雕漆互指。",
    "批准新建 terms/miaojin.md；单册单源，consensus=tentative。",
    "写入 terms/miaojin.md，新建；来源 L3887；用金量、胶结材料、绘制工具与产地未载。",
))

# updates
D.append(UPD(
    "cand-09-48", "宋徽宗（赵佶）", "persons/zhao-ji.md",
    "候选为宋徽宗（L3595）。`persons/zhao-ji.md` 已据赵农 2009 立条，记瘦金体、崇宁通宝、艮岳与结论评价，未收田自秉的钧窑字铭与提倡黑瓷饮茶两事。按同实体跨册更新：追加 2010 册 source block，source_count 1→2，version 1→2；两册各记不同设计活动，并列不裁断。",
    "批准更新 persons/zhao-ji.md：补田自秉 L3595、L3638，保留赵农 2009 叙述。",
    "追加田自秉 L3595、L3638；source_count 1→2，version 1→2；补钧窑字铭与黑瓷饮茶，未给诏令与参与设计的具体环节。",
    "canonical: 04-knowledge/units/persons/zhao-ji.md。cand-09-48 并入该条。",
))

D.append(UPD(
    "cand-10-02", "辽三彩盘", "terms/liao-sancai.md",
    "候选为辽三彩盘（L3723-L3725）。`terms/liao-sancai.md` 已据 2016、2009 两册立条，记技术来源、釉色作法与低温釉陶性质，未收田自秉的器形、素烧挂釉工序、印花装饰与凤首壶同段信息。按同实体跨册更新：追加 2010 册 source block，source_count 2→3，version 2→3；低温釉一说与 2009 相合，铅成分三册均未记。",
    "批准更新 terms/liao-sancai.md：补田自秉 L3723-L3725，保留 2016、2009 叙述。",
    "追加田自秉 L3723-L3725；source_count 2→3，version 2→3；补三彩盘器形、素烧挂釉与印花，铅含量仍未载。",
    "canonical: 04-knowledge/units/terms/liao-sancai.md。cand-10-02 并入该条。",
))

D.append(UPD(
    "cand-10-24", "蓝印花布", "procedures/lan-yinhua-bu.md",
    "候选为蓝印花布（L3824，合并 cand-12-43 的清段）。`procedures/lan-yinhua-bu.md` 已据高丰、2016 与田自秉 L4687 立条，田自秉只引清段；2016 已记宋段但称绞缬印花。田自秉 L3824 另引《嘉定县志》《朱文公集》，与 2016 同源而文字略异，并上溯于田六朝物证。按同册多跨段更新：田自秉 citation 追加 L3824，source_count 不变，version 4→5；两册宋段并列，不改写绞缬名实张力。",
    "批准更新 procedures/lan-yinhua-bu.md：田自秉 citation 追加 L3824，保留 L4687；source_count 3 不变，version 4→5。",
    "追加田自秉 L3824；source_count 3 不变，version 4→5；补宋段《嘉定县志》引文、于田物证与唐仲友彩帛铺，名实张力并列不裁断。",
    "canonical: 04-knowledge/units/procedures/lan-yinhua-bu.md。cand-10-24 与 cand-12-43 合并入该条。",
))

# no_delta
D.append(N(
    "cand-09-56", "章生一", "terms/ge-yao.md",
    "候选为章生一（L3623）。检索 `terms/ge-yao.md` 已据本段立哥窑条，记章生一、章生二兄弟分窑与“是否真有其兄弟二人，已无可考”的存疑；`persons/` 无章氏兄弟条。来源对章生一只有与弟分窑的传说性一句，无生卒、作品与窑址，单独立人物条会把传说坐实，故记 no_delta，材料保留在哥窑条。",
    "不新建章生一条；L3623 的兄弟分窑说已由 terms/ge-yao.md 承担并存疑。",
    "cand-09-56 记 no_delta，target 指向 terms/ge-yao.md。",
    "canonical: 04-knowledge/units/terms/ge-yao.md。cand-09-56 并入该条。",
))

D.append(N(
    "cand-09-57", "章生二", "terms/ge-yao.md",
    "候选为章生二（L3623）。与 cand-09-56 同段同源，`terms/ge-yao.md` 已并记兄弟二人与存疑，来源无独立于哥窑传说之外的生平或作品材料，单独立条只会重复同一句。记 no_delta，材料保留在哥窑条。",
    "不新建章生二条；L3623 的兄弟分窑说已由 terms/ge-yao.md 承担并存疑。",
    "cand-09-57 记 no_delta，target 指向 terms/ge-yao.md。",
    "canonical: 04-knowledge/units/terms/ge-yao.md。cand-09-57 并入该条。",
))

D.append(N(
    "cand-09-61", "建窑黑釉斑纹（兔毫、鹧鸪斑、油滴）", "places/jian-kiln.md",
    "候选为建窑黑釉斑纹（L3638）。检索 `places/jian-kiln.md` 已据本段立建窑条，记兔毫、鹧鸪斑、油滴三种斑纹、供御与进盏铭、斗茶与天目釉称法；`terms/` 无另立三种斑纹的必要材料，来源对每种斑纹只有一句比喻，无成因、成分与标本差异。记 no_delta，材料保留在建窑条。",
    "不新建兔毫、鹧鸪斑、油滴分条；L3638 的斑纹与贡铭已由 places/jian-kiln.md 承担。",
    "cand-09-61 记 no_delta，target 指向 places/jian-kiln.md。",
    "canonical: 04-knowledge/units/places/jian-kiln.md。cand-09-61 并入该条。",
))

D.append(N(
    "cand-10-10", "薛景石", "publications/ziren-yizhi.md",
    "候选为薛景石（L3769）。检索 `publications/ziren-yizhi.md` 已据本段立《梓人遗制》条并记薛景石为宋人、花罗织机；`persons/` 无薛景石，但来源对人物只有书名归属一句，无生卒、籍贯、职业与其余著作。记 no_delta，人物材料保留在《梓人遗制》条。",
    "不新建薛景石人物条；L3769 的撰者信息已由 publications/ziren-yizhi.md 承担。",
    "cand-10-10 记 no_delta，target 指向 publications/ziren-yizhi.md。",
    "canonical: 04-knowledge/units/publications/ziren-yizhi.md。cand-10-10 并入该条。",
))

D.append(N(
    "cand-10-18", "织成", "terms/kesi.md",
    "候选为织成（L3816）。检索 `terms/kesi.md` 已据本段立缂丝条，并在正文区分缂丝与织成，记织成为按成品形状与规格织造的织品；`terms/` 无另立织成条所需的工序、实物与产地材料。记 no_delta，材料保留在缂丝条。",
    "不新建织成条；L3816 的织成与缂丝区别已由 terms/kesi.md 承担。",
    "cand-10-18 记 no_delta，target 指向 terms/kesi.md。",
    "canonical: 04-knowledge/units/terms/kesi.md。cand-10-18 并入该条。",
))

D.append(N(
    "cand-10-28", "神针", "institutions/xiuyuan.md",
    "候选为神针（L3830-L3832）。检索 `institutions/xiuyuan.md` 已据本段立绣院条，记绣院三百余人、神针之名与《筠清轩秘录》《存素堂丝绣录》所记；`terms/` 无神针专条，来源对神针只有称名一句，无针法图、工序或传人。记 no_delta，材料保留在绣院条。",
    "不新建神针条；L3830-L3832 的神针称名已由 institutions/xiuyuan.md 承担。",
    "cand-10-28 记 no_delta，target 指向 institutions/xiuyuan.md。",
    "canonical: 04-knowledge/units/institutions/xiuyuan.md。cand-10-28 并入该条。",
))

D.append(N(
    "cand-10-29", "宋绣金刚般若波罗蜜经", "institutions/xiuyuan.md",
    "候选为宋绣《金刚般若波罗蜜经》（L3832）。检索 `institutions/xiuyuan.md` 已据本段记经卷为 5996 字、56 页与平绣锁线针法，`works/` 无此经；来源对经卷只有字数、页数与针法，无尺寸、绣工、藏地与图像，单独立 work 条会与绣院条重复且缺项过多。记 no_delta，材料保留在绣院条。",
    "不新建宋绣金刚经条；L3832 的字数、页数与针法已由 institutions/xiuyuan.md 承担。",
    "cand-10-29 记 no_delta，target 指向 institutions/xiuyuan.md。",
    "canonical: 04-knowledge/units/institutions/xiuyuan.md。cand-10-29 并入该条。",
))

cfg = {
    "doc": DOC,
    "file": SRC,
    "rules": RULES,
    "scope_spans": [[3468, 3948], [4406, 4406]],
    "scope_note": "田自秉 2010 册第八章宋代的工艺美术（L3468-L3948）逐段复读，含五代宋初概说、辽金西夏工艺、陶瓷、染织、刺绣、金属、铜镜、漆器与砚台，至宋代结语。插图 8、12、16、21 及彩版只读图注，未视觉核验。合并候选 cand-11-59 所指明代螺钿段 L4406 随 terms/luodian.md 一并收录，故 scope_spans 另记 L4406；cand-10-24 的候选跨度延至 L4689，其中清段 L4687 已由既有蓝印花布条承担，本批只新增 L3824 宋段，不宣称复读 L3949-L4688。",
    "decisions": D,
}

out = ROOT / "_zn_decisions_t9.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"decisions": len(D), "create": sum(1 for d in D if d["action"] == "create"),
                  "update": sum(1 for d in D if d["action"] == "update"),
                  "no_delta": sum(1 for d in D if d["action"] == "no_delta")}, ensure_ascii=False))
