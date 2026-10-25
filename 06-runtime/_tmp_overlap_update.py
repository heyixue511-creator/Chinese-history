# -*- coding: utf-8 -*-
"""Apply the 39 update targets + 1 create for the 2026-10-25 overlap batch."""
import hashlib
import json
import re
import sys
from pathlib import Path

UNITS = Path("04-knowledge/units")
DRY = "--check" in sys.argv

SOURCES = {
    "2004": {
        "citation": "高丰, *中国设计史* (广西美术出版社, 2004), {loc}.",
        "doc_id": "2004-gaofeng-zhongguo-shejishi",
        "source_file": "03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md",
    },
    "2009xy": {
        "citation": "夏燕靖, *中国设计史* (上海: 上海人民美术出版社, 2009), {loc}.",
        "doc_id": "2009-xiayanjing-zhongguo-shejishi",
        "source_file": "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md",
    },
    "2009zn": {
        "citation": "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), {loc}.",
        "doc_id": "2009-zhaonong-zhongguo-yishu-shejishi",
        "source_file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    },
    "2010": {
        "citation": "田自秉, *中国工艺美术史（修订本）* (上海: 东方出版中心, 2010), {loc}.",
        "doc_id": "2010-tianzibing-zhongguo-gongyi-meishushi",
        "source_file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
    },
    "2011": {
        "citation": "李立新, *中国设计艺术史论* (北京: 人民出版社, 2011), {loc}.",
        "doc_id": "2011-lilixin-zhongguo-sheji-yishu-shilun",
        "source_file": "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md",
    },
    "2016": {
        "citation": "夏燕靖, *中国艺术设计史（升级版）* (上海: 上海人民美术出版社, 2016), {loc}.",
        "doc_id": "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade",
        "source_file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
    },
}
ORDER = ["2004", "2009xy", "2009zn", "2010", "2011", "2016"]


def last_range(loc):
    return loc.split(", ")[-1]


def source_block(key, loc):
    meta = SOURCES[key]
    return (
        f'  - citation: "{meta["citation"].format(loc=last_range(loc))}"\n'
        f'    location: "{loc}"\n'
        f"    evidence_ref:\n"
        f"      doc_id: {meta['doc_id']}\n"
        f"      source_file: {meta['source_file']}\n"
        f"      chapter_id: null\n"
        f"      chunk_id: null\n"
    )


UPDATES = [
    {
        "key": "terms/an-furniture.md",
        "candidates": ["2004-gaofeng-zhongguo-shejishi:cand-sup-22"],
        "new": [("2004", "L2383-L2401")],
        "bullets": [
            "- **汉代两型**: 汉代食案分无足（类似托盘）与有足两种，有足者案面长方形，装柱状或蹄状案足（高丰）",
            "- **尺度**: 有足食案长约 1 米、宽约半米、高约 10—20 厘米，多为木制，也有铜、陶制（高丰）",
            "- **铜圆案实例**: 广州沙河顶 5054 号东汉墓出土铜圆案，面径 40 厘米、高 8.6 厘米，上置大小铜耳杯 6 个（高丰）",
        ],
        "note": "补汉代食案两型、柱状与蹄状足、尺度及广州沙河顶东汉铜圆案",
    },
    {
        "key": "terms/jianghu.md",
        "candidates": ["2004-gaofeng-zhongguo-shejishi:cand-sup-33"],
        "new": [("2004", "L4110-L4149")],
        "bullets": [
            "- **明代匠籍**: 明初将工匠划入匠籍，须按规定时间轮流赴京服役，称“轮班工匠”，即所谓“岁率轮班（匠）至京受役”（高丰）",
            "- **轮班人数**: 据洪武二十六年统计，全国轮班工匠共 232089 名，分布在 62 个行业（高丰）",
            "- **班次**: 《明会典》载各行业班次自五年一班至一年一班不等，如木匠、裁缝匠五年一班，铁匠四年一班，织匠、染匠三年一班，银匠两年一班（高丰）",
            "- **住坐**: 另有住坐京城及其附近服役的工匠，与轮班工匠合计构成明代官手工业的庞大队伍（高丰）",
        ],
        "replace": [
            (
                "  - 元代\n  - 匠籍",
                "  - 元代\n  - 明代\n  - 匠籍",
            ),
            (
                "《元典章》载系官诸色正匠免差，实际是一种工奴。\n\n## 核心内容",
                "《元典章》载系官诸色正匠免差，实际是一种工奴。明代改称匠籍，工匠须按规定时间轮班赴京服役。\n\n## 核心内容",
            ),
            (
                'hierarchy_scope_note: "匠户是 D 维度下元代工匠户籍与官营手工业制度的条目。Theme/Topic 尚未 materialize。"',
                'hierarchy_scope_note: "匠户／匠籍是 D 维度下元明工匠户籍与官营手工业制度的条目。Theme/Topic 尚未 materialize。"',
            ),
            (
                "- scope_note: 匠户是 D 维度下元代工匠户籍与官营手工业制度的条目。Theme/Topic 尚未 materialize。",
                "- scope_note: 匠户／匠籍是 D 维度下元明工匠户籍与官营手工业制度的条目。Theme/Topic 尚未 materialize。",
            ),
        ],
        "note": "并入明代匠籍、轮班与住坐、洪武二十六年 232089 名与 62 行业、班次序列，条目由元代扩为元明",
    },
    {
        "key": "works/yuan-yinjingjia.md",
        "candidates": ["2004-gaofeng-zhongguo-shejishi:cand-sup-66"],
        "new": [("2004", "L3921")],
        "bullets": [
            "- **纹饰**: 主要部位雕镂双凤戏牡丹纹和玉兔、蟾蜍、灵芝纹（高丰）",
            "- **造型**: 整体造型犹如一把豪华的小交椅，可立放又可折合（高丰）",
        ],
        "note": "补双凤戏牡丹／玉兔蟾蜍灵芝纹与“豪华小交椅”造型评价",
    },
    {
        "key": "terms/tihuaji.md",
        "candidates": ["2009-xiayanjing-zhongguo-shejishi:cand-03-23"],
        "new": [("2009xy", "L1418-L1432")],
        "bullets": [
            "- **从斜织机发展**: 汉代布机已广泛使用脚踏提综斜织机，提花机由布机发展而来并用于生产，效果显著（夏燕靖 2009）",
            "- **西传**: 李约瑟《中国古代科技史》称西方提花机由中国传去，采用时代比中国晚 4 个世纪（夏燕靖 2009）",
        ],
        "note": "补脚踏提综斜织机到提花机的发展关系与李约瑟“西方晚 4 个世纪”说",
    },
    {
        "key": "terms/longyao.md",
        "candidates": ["2009-xiayanjing-zhongguo-shejishi:cand-03-31"],
        "new": [("2009xy", "L1472-L1490")],
        "bullets": [
            "- **东汉窑址**: 20 世纪五六十年代在浙江上虞、余姚、宁波、永嘉等地发现大量东汉窑址，多属陶、瓷共烧，后又出现专门瓷窑（夏燕靖 2009）",
            "- **原料**: 选用高岭土之类材料为制瓷原料，能在较低火候中烧出强度较高的瓷器（夏燕靖 2009）",
        ],
        "note": "补浙江上虞等地东汉窑址、陶瓷共烧转专窑及高岭土原料",
    },
    {
        "key": "terms/dougong.md",
        "candidates": ["2009-xiayanjing-zhongguo-shejishi:cand-03-55"],
        "new": [("2009xy", "L1594-L1606")],
        "bullets": [
            "- **秦汉木构体系**: 以木结构为主的建筑体系秦汉时已初步形成，广泛使用斗栱，硬山、悬山、歇山、庑殿顶均已出现（夏燕靖 2009）",
            "- **门窗与层叠**: 板门、交棂窗十分广泛；东汉多层建筑发展，梁柱上再加梁柱的叠架技术有重大发展（夏燕靖 2009）",
        ],
        "note": "补斗栱所处的秦汉木构体系、四类屋顶、板门交棂窗与梁柱叠架",
    },
    {
        "key": "places/yungang-shiku.md",
        "candidates": ["2009-xiayanjing-zhongguo-shejishi:cand-04-05"],
        "new": [("2009xy", "L1927-L1930")],
        "bullets": [
            "- **源流与中国化**: 石窟寺源于印度，公元 3 世纪传入中国；早期造像模仿犍陀罗风格，时过不久便创造出中国形式的造像（夏燕靖 2009）",
        ],
        "note": "补石窟寺印度源流、3 世纪传入与“中国形式”造像的形成",
    },
    {
        "key": "terms/chai-yao.md",
        "candidates": ["2009-xiayanjing-zhongguo-shejishi:cand-04-73"],
        "new": [("2009xy", "L2379-L2382")],
        "bullets": [
            "- **吴越贡瓷**: 五代陶瓷仍以越窑青瓷为主；吴越钱氏家族以瓷器向中原王朝送礼，最多一次达 14 万件，贡品中有秘色瓷器，为当时瓷器上品（夏燕靖 2009）",
            "- **文献与推测**: 明人记“柴窑片瓦值千金”；窑址在郑州之说无确切考据，或许是周世宗向钱氏提出的贡瓷要求，属越窑秘色瓷一类（夏燕靖 2009）",
        ],
        "note": "补吴越钱氏 14 万件贡瓷、秘色瓷上品、“片瓦值千金”与周世宗贡瓷推测",
    },
    {
        "key": "terms/guan-yao.md",
        "candidates": ["2009-xiayanjing-zhongguo-shejishi:cand-04-88"],
        "new": [("2009xy", "L2503-L2547")],
        "bullets": [
            "- **仿古器形与宫廷风格**: 主要器形有瓶、尊、洗、盘、碗，也有仿周、汉青铜器的鼎、炉、觚、彝等式样，造型带雍容典雅的宫廷风格（夏燕靖 2009）",
            "- **开片成因**: 胎体较厚、天青釉略带粉红、釉面开大纹片，是胎、釉受热后膨胀系数不同所致，为北宋官窑典型特征（夏燕靖 2009）",
        ],
        "note": "补鼎炉觚彝仿古器形、宫廷风格与开片的胎釉膨胀系数成因",
    },
    {
        "key": "terms/kesi.md",
        "candidates": ["2009-xiayanjing-zhongguo-shejishi:cand-06-81"],
        "ext": [("2009xy", "L3942-L3952, L4265")],
        "bullets": [
            "- **南宋产地与生产形态**: 南宋时已在苏州、松江一带流传，一直作为向皇家进贡的贡品；又为苏州一带乡村农闲副业，技艺父子世代相传（夏燕靖 2009）",
            "- **新中国新作**: 新中国成立后继承宋以来名家传统，发展镶色技巧，创制屏风、中堂、人物、山水等新作（夏燕靖 2009）",
        ],
        "note": "扩展 2009 版位置至 L4265，补南宋苏州松江产地、贡品与乡村副业、父子相传及新中国镶色新作",
    },
    {
        "key": "terms/qingtong-liqi.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-03-12"],
        "new": [("2009zn", "L1546-L1577")],
        "bullets": [
            "- **礼的起源**: 礼的兴起肇始于“致其敬于鬼神”（《礼记·礼运》），由万物有灵观念形成；孔子称“祭如在，祭神如神在”（《论语·八佾》）（赵农）",
            "- **祀与戎**: “国家大事，在祀与戎”，商周丧葬、朝聘、征伐、宴乐均需通过祭祀完成，礼器应运而生（赵农）",
            "- **玉礼器**: 《周礼·春官》“以苍璧礼天，以黄琮礼地”；良渚文化所见玉琮、玉璧证明此制（赵农）",
            "- **器用交织**: 礼器造型多与饮食器具相关，饮食器与祭祀器常交织互促（赵农）",
        ],
        "note": "补礼的鬼神起源、祀与戎、苍璧黄琮与良渚玉礼器、饮食器与礼器交织",
    },
    {
        "key": "works/san-jiao-lou.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-04-101"],
        "new": [("2009zn", "L2786-L2812")],
        "bullets": [
            "- **耧车结构**: 耧车又称耧犁，把底部有孔的木斗与铁耧脚连通，开土时种子流入土中；两辕两扶把，便于牛拉人扶（赵农）",
            "- **效率**: 播种功效可提高十几倍，有“日种一顷”的播种速度（赵农）",
            "- **耦犁**: 汉武帝时推广二牛三人的耦犁，由搜粟都尉赵过推行（赵农）",
        ],
        "note": "补木斗与铁耧脚连通的耧车结构、两辕两扶把、日种一顷及二牛三人耦犁",
    },
    {
        "key": "publications/zhouyi.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-04-15"],
        "new": [("2009zn", "L2353-L2396")],
        "bullets": [
            "- **文王与孔子**: 有“文王拘而演《周易》”之说；“孔子晚而喜《易》……韦编三绝”（《史记·孔子世家》），赋予其思想主题（赵农）",
            "- **《系辞传》制器四则**: “以制器者尚其象”“形乃谓之器，制而用之谓之法”“备物致用，立出器以为天下利”“形而上者谓之道，形而下者谓之器”（赵农；原文作“立出器”）",
            "- **道器在形内**: 赵农强调“形而上”“形而下”首先在“形”的范畴内，制形精神贯穿“道”，制形过程体现为“器”，不宜把道器简单对立（赵农）",
        ],
        "note": "补文王演易、韦编三绝、《系辞传》四则制器原文与“道器在形内”的整体理解",
    },
    {
        "key": "persons/mozi.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-04-18"],
        "ext": [("2009zn", "L1767-L2097, L2387-L2395")],
        "bullets": [
            "- **科技门类**: 《墨子》对光学、力学、数学、声学、机械、土木等的研究，成为春秋时期科学与设计技术的精彩篇章（赵农）",
            "- **材质观**: 《墨子·佚文》“大匠不能斫金，巧冶不能铄木……埏埴以为器，刳木而为舟，烁铁而为刃，铸金而为钟，因其可也”，强调因材施工（赵农）",
        ],
        "note": "扩展赵农位置至 L2395，补光学力学数学声学机械土木六类研究与《墨子·佚文》因材施工的材质观",
    },
    {
        "key": "works/houfeng-dizhenyi.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-04-55"],
        "new": [("2009zn", "L3148-L3152")],
        "bullets": [
            "- **纪年**: 《后汉书·张衡传》记“阳嘉元年，复造候风地动仪”（赵农）",
            "- **饰纹与机构**: 尊上饰以篆文山龟鸟兽之形，中有都柱，傍行八道，施关发机（赵农）",
            "- **验证**: 一龙发机而七首不动，寻其方面乃知震之所在，验之以事合契若神；今人复制了地动仪的木质模型（赵农）",
        ],
        "note": "补阳嘉元年、篆文山龟鸟兽饰纹、一龙发机七首不动与合契若神、木质模型",
    },
    {
        "key": "terms/dulunche.md",
        "candidates": [
            "2009-zhaonong-zhongguo-yishu-shejishi:cand-04-81",
            "2011-lilixin-zhongguo-sheji-yishu-shilun:cand-03-59",
        ],
        "new": [("2011", "L883-L890")],
        "ext": [("2009zn", "L2684, L3317-L3405")],
        "bullets": [
            "- **别称**: 鹿车也称独轮车，四川称“鸡公车”，江南称“羊角车”；其雏形在汉代四川画像砖中已有反映（李立新）",
            "- **使用方式**: 绳带缚于辕梢、行运时绕于肩颈以匀力，上坡可倒拉，必要时两人一拉一推；车辕下木棒支撑，既保持平衡亦可坐歇（赵农）",
        ],
        "note": "新增李立新源并扩展赵农位置至 L2684，补鸡公车／羊角车别称、汉代画像砖雏形与绳带绕颈、倒拉、木棒支撑的使用方式；同组“鹿车”候选合并写入本 KU",
    },
    {
        "key": "places/dunhuang-mogao-ku.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-06-31"],
        "new": [("2009zn", "L3950-L3970")],
        "bullets": [
            "- **地理位置**: 敦煌地处甘肃河西走廊西端，是汉代以来中原至西域的交通要道；莫高窟在县城南约 25 公里鸣沙山与三危山之间的河谷地带（赵农）",
            "- **开创年代两说**: 唐人称前秦建元二年（366）乐傅和尚来敦煌始建佛龛；《沙洲土境》则记永和九年（353）已建最早佛龛（赵农）",
            "- **地质与规模**: 鸣沙山体属砂砾岩质，难以雕刻，主要以泥塑和壁画表现；现存 492 个洞窟，十六国与北朝早期洞窟约 39 个（赵农）",
            "- **中心塔柱与千佛洞**: 北朝洞窟为主室后部建中心塔柱、四周开龛，前部凿人字披屋顶；窟壁绘千佛，故称“千佛洞”（赵农）",
            "- **印度渊源**: 中心柱窟与印度支提窟有渊源，但吸收斗栱、枋子、椽子等中原木构特点，并出现方形塔的意味（赵农）",
        ],
        "note": "补河西走廊位置、366／353 两说、砂砾岩与 492 窟 39 早期窟、中心塔柱与人字披、支提窟渊源",
    },
    {
        "key": "terms/lifang-zhi.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-08-79"],
        "ext": [("2009zn", "L3637-L3700, L5388-L5425")],
        "bullets": [
            "- **北宋废里坊**: 北宋立国不久便消除唐代流传下来的里坊制度，城市管理废除夜禁，出现“夜市”，开封成为商业化城市（赵农）",
            "- **开封城制**: 后周时大修开封城，分外城、京城（内城）、宫城三重，外城周围达 40 里；汴河、蔡河、金水河、五丈河“四水贯都”；御道为京城中轴线，大内居城市中心（赵农）",
        ],
        "note": "扩展赵农位置至 L5388-L5425，补北宋废里坊、废夜禁与夜市，及开封三重城、40 里、四水贯都、御道中轴",
    },
    {
        "key": "works/kaifeng-xiangguosi-pagoda.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-08-94"],
        "new": [("2009zn", "L5444-L5458")],
        "bullets": [
            "- **琉璃与色泽**: 塔身加筑褐色琉璃瓦，如锈铁色泽，坚硬如铁，故名“铁塔”（赵农）",
            "- **塔内结构**: 塔身有螺旋式蹬道，使塔壁与中心塔柱紧密联结；宋塔多六角或八角形、以楼阁式为主（赵农）",
        ],
        "note": "补褐色琉璃瓦与锈铁色泽得名、螺旋蹬道联结塔壁与中心塔柱；与既有“28 种琉璃砖”说并列",
    },
    {
        "key": "works/miaoying-si-baita.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-09-40"],
        "new": [("2009zn", "L6198")],
        "bullets": [
            "- **高度异文**: 赵农记塔高 53 米，与两版所记 50.9 米不同，并列保留（赵农）",
            "- **塔身**: 呈现宝瓶塔身，是元大都建筑的喇嘛塔样式（赵农）",
        ],
        "note": "补赵农 53 米异文与宝瓶塔身、元大都喇嘛塔样式；高度两说并列不裁定",
    },
    {
        "key": "institutions/fujian-chuanzhengju.md",
        "candidates": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-11-063"],
        "new": [("2009zn", "L7549, L8508")],
        "bullets": [
            "- **近代造船起点**: 1865 年徐寿等制造“黄鹄”机械轮船，为近代造船业开始；同年江南制造总局成立，开始造船修船（赵农）",
            "- **船政序列**: 此后福州船政局、天津机器局、广东军装机器局、旅顺船坞等造船工场陆续兴建；福州船政局（1866）与江南制造总局（1865）、金陵机器局（1865）、天津机器局（1867）、湖北枪炮厂（1891）并列（赵农）",
        ],
        "note": "补 1865 年徐寿“黄鹄”轮与江南制造总局、福州／天津／广东军装／旅顺船坞序列及洋务企业年表",
    },
    {
        "key": "procedures/lost-wax-casting.md",
        "candidates": ["2010-tianzibing-zhongguo-gongyi-meishushi:cand-03-22"],
        "ext": [("2010", "L915, L1810-L1816")],
        "bullets": [
            "- **出现上限**: 蜡模法的创造和使用约在商代以后；据文物出土，公元前五六世纪的春秋时代已有蜡模法青铜器实物（田自秉）",
        ],
        "note": "扩展田自秉位置至 L915，补“约商代以后、公元前五六世纪春秋已有实物”的上限说",
    },
    {
        "key": "procedures/jiazhu-tai.md",
        "candidates": [
            "2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-32",
            "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-02-79",
        ],
        "new": [("2010", "L1990, L2963"), ("2016", "L1195, L1873")],
        "bullets": [
            "- **行像**: 魏晋南北朝佛教盛行，教徒用夹纻工艺塑佛像以便车载游行，称“行像”；晋代戴逵以夹纻行像著名，为南京瓦棺寺作夹纻佛像五躯，与顾恺之维摩诘像、狮子国玉像并称“瓦棺寺三绝”（田自秉）",
            "- **汉代硬胎**: 2016 记汉代制作方法有木胎、竹胎和夹纻胎（用漆夹麻布制成硬胎），以木胎为主（夏燕靖 2016）",
        ],
        "note": "新增田自秉与 2016 两源，补行像、戴逵瓦棺寺三绝与汉代夹纻硬胎；同组“夹纻胎”候选合并写入本 KU",
    },
    {
        "key": "terms/qian-you-tao.md",
        "candidates": ["2010-tianzibing-zhongguo-gongyi-meishushi:cand-06-39"],
        "new": [("2010", "L2353-L2357")],
        "bullets": [
            "- **釉的组成**: 陶瓷釉一般以硅酸（二氧化矽）为主体，以氧化钙、氧化钠、氧化铅等为媒熔剂；以铅为盐基的称铅釉（田自秉）",
            "- **产地与呈色**: 铅釉陶最早生产于关中地区；西汉时多为黄、褐、绿等色，绿釉特别流行，长期埋藏后釉面泛银光，又称银釉（田自秉）",
            "- **代表器形**: 釉陶壶鼓腹、长颈、盘口，肩部浮雕狩猎纹或铺首衔环或弦纹；陶奁、陶盒、陶博山炉均流行（田自秉）",
            "- **南北软硬釉**: 北方铅釉陶火度低、釉质软，称软釉；南方青釉陶火度高、釉质硬，称硬釉，是青瓷发展的过渡（田自秉）",
        ],
        "note": "补硅酸主体与钙钠铅媒熔剂、关中最早产地、西汉呈色与器形、南北软硬釉",
    },
    {
        "key": "terms/rendong-wen.md",
        "candidates": ["2010-tianzibing-zhongguo-gongyi-meishushi:cand-08-21"],
        "ext": [("2010", "L2853, L2992")],
        "bullets": [
            "- **卷草结构与实例**: 卷草纹枝干成二方连续卷曲状，主要由叶子组成，叶形变化丰富；响堂山石窟浮雕卷草为代表，并见于佛光、石碑边侧与敦煌藻井（田自秉）",
        ],
        "note": "扩展田自秉位置至 L2992，补二方连续卷曲结构、响堂山浮雕及佛光、石碑边侧、敦煌藻井实例",
    },
    {
        "key": "terms/jiaoxie.md",
        "candidates": ["2010-tianzibing-zhongguo-gongyi-meishushi:cand-08-60"],
        "new": [("2010", "L3260")],
        "bullets": [
            "- **唐代实物**: 新疆阿斯塔那古墓出土唐垂拱四年（688）绞缬裙，由绛紫、茄紫等色形成菱形网格图案，制作精巧（田自秉）",
        ],
        "note": "补阿斯塔那唐垂拱四年（688）绞缬裙及绛紫、茄紫菱形网格",
    },
    {
        "key": "works/liujin-wuma-xianbei-yinhu.md",
        "candidates": ["2010-tianzibing-zhongguo-gongyi-meishushi:cand-08-71"],
        "new": [("2010", "L3306-L3311")],
        "bullets": [
            "- **唐诗与舞马**: 壶上舞马颈系彩带、口衔杯、前腿直立后腿曲膝，正如唐诗“屈膝衔杯赴节，倾心献寿无疆”（田自秉）",
            "- **千秋节表演**: 唐玄宗时舞乐极盛，每逢玄宗生日“千秋节”或皇室大典举行宴会，表演舞马；马身披锦绣、饰金银，随乐曲舞蹈（田自秉）",
        ],
        "note": "补“屈膝衔杯赴节”唐诗、千秋节舞马表演与马身锦绣金银饰物",
    },
    {
        "key": "terms/wuda-mingyao.md",
        "candidates": ["2010-tianzibing-zhongguo-gongyi-meishushi:cand-09-38"],
        "new": [("2010", "L3522")],
        "bullets": [
            "- **“偏颇”之评**: 田自秉称论瓷者以定、汝、官、哥、钧为宋代五大名窑“显然有偏颇之处”，并举北方磁州窑、南方吉州窑等民窑以其清新朴质风格大放异彩（田自秉）",
        ],
        "note": "补田自秉“显然有偏颇”之评与磁州窑、吉州窑民窑贡献",
    },
    {
        "key": "terms/nanjing-yunjin.md",
        "candidates": ["2010-tianzibing-zhongguo-gongyi-meishushi:cand-12-23"],
        "new": [("2010", "L4633-L4637, L5103")],
        "bullets": [
            "- **得名异说**: 一说纹饰色彩灿烂如天上云彩，故名；此说清代文献无具体记载，田自秉另提“纹饰多用云纹”也可作为定名依据（田自秉）",
            "- **妆花配色**: 妆花彩色丰富，一般 6 色或 9 色，多至 18 色，用“过管”边织边配色，同一排花朵可出现完全不同的色彩（田自秉）",
            "- **明式风格与用途**: 妆花花纹多保留明式风格，程式化而富装饰味；云锦多用作蒙藏少数民族的衣帽服饰（田自秉）",
        ],
        "note": "补得名两说与清代文献无载、妆花 6／9／18 色过管配色、明式风格与蒙藏衣帽用途",
    },
    {
        "key": "terms/wenzhi.md",
        "candidates": ["2011-lilixin-zhongguo-sheji-yishu-shilun:cand-02-66"],
        "new": [("2011", "L727")],
        "bullets": [
            "- **绘事后素**: 孔子以“绘事后素”为造物统一思想的基本定位，即质先于文、从质始而后赋文，最后达到不偏不倚的适宜中正之境（李立新）",
        ],
        "note": "补“绘事后素”、质先文后与不偏不倚的中正之境",
    },
    {
        "key": "works/yuanmingyuan.md",
        "candidates": ["2011-lilixin-zhongguo-sheji-yishu-shilun:cand-04-09"],
        "new": [("2011", "L1236-L1242")],
        "bullets": [
            "- **西洋楼设计者**: 清乾隆时郎世宁等欧洲设计师参与修建圆明园，使其融合中西建筑风格（李立新）",
            "- **室内与图版**: 室内置罗可可风格的家具、壁毯和各式西洋器物；图 3-7 为圆明园东长春园西洋楼谐奇趣北面铜版画（李立新）",
        ],
        "note": "补郎世宁等欧洲设计师、罗可可家具壁毯与谐奇趣铜版画",
    },
    {
        "key": "terms/yuefenpai.md",
        "candidates": ["2011-lilixin-zhongguo-sheji-yishu-shilun:cand-04-21"],
        "new": [("2011", "L1305-L1311")],
        "bullets": [
            "- **作者与渊源**: 月份牌作者大都未接受正规西洋画训练，最初以木刻形式出现，似有年画影子，后融会中西表现手法（李立新）",
            "- **评价**: 以通俗内容、多样形式赢得普通民众欢迎，虽对中西结合的理解简单甚至肤浅，其独特形式却“空前绝后”（李立新）",
        ],
        "note": "补作者多未受正规西画训练、木刻与年画渊源、“简单甚至肤浅”及“空前绝后”之评",
    },
    {
        "key": "terms/zisha-tao.md",
        "candidates": ["2011-lilixin-zhongguo-sheji-yishu-shilun:cand-04-38"],
        "new": [("2011", "L1461")],
        "bullets": [
            "- **明代名家**: 龚春、时大彬等工艺大师明代不在少数；董翰、赵梁、元畅、时朋称“制壶四大家”（李立新）",
            "- **清代名家与风格**: 清代高手林立，著名者有陈鸣远、杨彭年兄妹和邵大亨；诸家依托前贤遗存各抒其长，形成宜兴紫砂造物的“块团形式”（李立新）",
        ],
        "note": "补龚春、时大彬、制壶四大家、陈鸣远、杨彭年兄妹、邵大亨与“块团形式”",
    },
    {
        "key": "works/qin-shi-huang-ling.md",
        "candidates": ["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-03-84"],
        "new": [("2016", "L1671-L1675")],
        "ext": [("2009zn", "L2674-L2676, L2841-L3011")],
        "bullets": [
            "- **铜车马出土与复原**: 1980 年发掘两组大型铜制御车马，出土时破碎为 1555 块，复原花费 12 年；各由 3000 多个部件构成（夏燕靖 2016）",
            "- **比例与重量**: 两组铜车马是秦始皇生前出巡车马的复制品，比原车马缩小 1/2，总重 1200 多千克（夏燕靖 2016）",
            "- **工艺**: 综合使用铸造、焊接、嵌铸、镶嵌及多种机械连接工艺，解决了车舆、马饰名称与系驾关系等问题（夏燕靖 2016）",
            "- **两车形制**: 一为戎车，长 2.25 米、高 1.52 米；一为安车，长 3.28 米、高 1.04 米；伞盖分别 1.12 与 2.3 平方米，厚仅 0.4 厘米（赵农）",
        ],
        "note": "新增 2016 源并扩展赵农位置至 L2674-L2676，补 1980 年两组铜车马、1555 块／12 年复原、3000 部件、1:2 与 1200 千克、工艺及戎车安车尺寸伞盖",
    },
    {
        "key": "terms/yuexiu.md",
        "candidates": ["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-08-120"],
        "replace": [
            (
                "光绪年间广东成立工艺局主管工艺品生产，潮州刺绣经汕头口岸输往新加坡、泰国、马来西亚",
                "光绪年间广东成立工艺局主管工艺品生产，其工艺品种通过洋庄源源输向世界各地，潮州刺绣则经汕头口岸输向新加坡、泰国、马来西亚",
            )
        ],
        "bullets": [],
        "note": "在既有 2009 引得句中补“通过洋庄源源输向世界各地”的外销渠道；无新增源",
    },
    {
        "key": "terms/zhongshanzhuang.md",
        "candidates": ["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-09-11"],
        "new": [("2016", "L4877-L4885")],
        "bullets": [
            "- **结构与廓形**: 早期背面有缝、后背中腰有带，上下衣袋均有“胖裥”；定型后后背整块无缝，上面两个小衣袋为平贴袋、底角圆弧、袋盖中间弧形尖出；整体廓形垫肩收腰、均衡对称（夏燕靖 2016）",
        ],
        "note": "补早期背面有缝与中腰带、胖裥、定型后后背无缝、平贴袋与袋盖弧形、垫肩收腰廓形",
    },
    {
        "key": "institutions/zhongguo-meishuguan.md",
        "candidates": ["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-09-133"],
        "ext": [("2016", "L5290, L5306-L5317, L5709-L5720")],
        "bullets": [
            "- **国庆工程**: 为迎接新中国成立 10 周年，中央人民政府从 1958 年 9 月确定国庆工程建设任务，决定在北京兴建人民大会堂等十项大型建筑（夏燕靖 2016）",
            "- **建筑装饰**: 中国美术馆的建筑装饰如彩画、木雕等，是传统工艺与现代建筑结合的成功范例；图 11-25 题“北京十大建筑（中国美术馆）”（夏燕靖 2016）",
        ],
        "note": "扩展 2016 位置至 L5290-L5317，补 1958 年 9 月国庆工程十项、彩画木雕装饰与图 11-25 十大建筑题名",
    },
    {
        "key": "persons/hang-zhiying.md",
        "candidates": ["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-09-35"],
        "new": [("2016", "L5009")],
        "bullets": [
            "- **商务印书馆练习生**: 1920 年商务印书馆招收练习生，有李泳青、杭稚英、金梅生、金雪尘、鲁少飞、戈湘岚、陈在新、张荻寒等；聘德国、日本画家授课，并请吴待秋传授中国画（夏燕靖 2016）",
            "- **广告画家群**: 与周慕桥、郑曼陀、谢之光、徐青等并列为当时知名广告画家；这批人后来成长为中国早期商业招贴广告设计专家（夏燕靖 2016）",
        ],
        "note": "补 1920 年商务印书馆练习生名单、德日画家授课与吴待秋教中国画、广告画家群及早期商业招贴专家身份",
    },
    {
        "key": "persons/guan-zhong.md",
        "candidates": ["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-03-56"],
        "ext": [("2016", "L1500-L1503, L6125-L6128")],
        "bullets": [
            "- **字与称谓**: 名夷吾，字仲；助齐桓公称霸，被称为“春秋第一相”（夏燕靖 2016）",
        ],
        "note": "扩展 2016 位置至 L1500-L1503，补“字仲”与“春秋第一相”称谓；候选标题“管子”指人物，写回 persons/guan-zhong，不写 publications/guanzi",
    },
]

EVENT = """---
title: 胡服骑射（Hufu Qishe Reform）
name_en: Hufu Qishe Reform
type: event
sub_type: historical_event
date: "战国时期（赵武灵王执政期间）"
date_note: "来源未给具体年份，只作“战国时期”“赵武灵王在执政赵国期间”"
location: "赵国"
participants: "赵武灵王；赵国贵族王室"
cause: "赵国长年与草原游牧民族作战，服饰不便使战斗力受到影响"
result: "奠定赵国强盛的基础；胡服推广使战斗力提高，并深入中原诸国"
source_basis: "赵农有直接记载，作为服饰改革与跨文化采纳的案例"
tags:
  - 战国
  - 赵国
  - 赵武灵王
  - 胡服
  - 服饰改革
  - 带钩
sources:
  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L2175-L2179."
    location: "L2175-L2179"
    evidence_ref:
      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi
      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md
      chapter_id: null
      chunk_id: null
created: 2026-10-25
updated: 2026-10-25
confidence: medium
consensus: tentative
source_count: 1
last_verified: 2026-10-25
review_due: 2027-04-25
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: E
hierarchy_scope_note: "胡服骑射是 E 维度下战国时期赵国引进北方游牧民族服饰的制度改革，用于说明服饰功能与跨文化采纳。Theme/Topic 尚未 materialize。"
---

## 描述

胡服骑射是战国时期赵武灵王在赵国推行的服饰与军事改革。赵农记赵国地处北方，长年与草原游牧民族作战，服饰不便使战斗力受到影响；赵武灵王力排众议引进胡服骑射，提高战斗能力，并说服贵族王室，最终奠定赵国强盛的基础。来源未给具体年份。

## 核心内容

- **时代与地点**：战国时期，赵国（赵农）
- **改革者**：赵武灵王，执政赵国期间力排众议推行（赵农）
- **动因**：赵国长年与草原游牧民族作战，服饰不便使战斗力受到影响（赵农）
- **胡服形制**：北方草原游牧民族服装，特征为短衣、长裤、靴子（赵农）
- **改革说辞**：《史记·赵世家》记赵武灵王“吾不疑胡服也”“世有顺我者，胡服之功未可知也”“夫服者，所以便用也；礼者，所以便事也”（赵农）
- **结果**：提高战斗能力，说服贵族王室，奠定赵国强盛的基础；胡服推广深入中原诸国，使各国开始重视改革服饰（赵农）
- **带钩**：胡服引进出现带钩一类附件，类似皮带钩，当时称“钩络带”，较丝绳绑扎更便捷，提高穿衣速度与效率（赵农）
- **设计史意义**：赵农从服饰功能角度称胡服“非常简便，带来了生活和作战的迅达”，并把服饰改革与国家兴盛直接关联；这是中原向游牧民族学习、以“便用”为标准采纳异文化的案例（赵农）

## 在层级体系中的位置

- primary_domain: chinese-design-history
- primary_dimension: E（现代性与跨文化互动）
- primary_theme: 未建立；Theme 尚未 materialize
- topic_memberships: 无；Topic 尚未 materialize
- role_in_theme: 未定
- scope_note: 胡服骑射是 E 维度下战国时期赵国引进北方游牧民族服饰的制度改革，用于说明服饰功能与跨文化采纳。Theme/Topic 尚未 materialize。

## 相关知识元

`terms/hufu.md` 记胡服形制；`terms/belt-hook.md` 记带钩；`terms/shenyi.md` 记与胡服并行的深衣。relation 未审查。

## 验证状态

- 证据状态: source_backed（来源内复读）
- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7
- 验证平台: 未使用外部平台
- 匹配质量: 赵农一节集中记述改革的动因、说辞、结果与带钩附件，未给具体年份，也未记改革起始年；六册其余各册未见同题专段。
- 验证日期: 2026-10-25
- 证据范围: 仅前六册 Markdown 文本；未做来源外核对

## 参考文献

1. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009.
"""


def fingerprint(text_bytes):
    return {
        "sha256": "sha256:" + hashlib.sha256(text_bytes.replace(b"\r\n", b"\n")).hexdigest(),
        "bytes": len(text_bytes.replace(b"\r\n", b"\n")),
        "lines": text_bytes.replace(b"\r\n", b"\n").count(b"\n"),
    }


def insert_sources(lines, start, end, new):
    """Insert new source blocks in canonical doc order within lines[start:end]."""
    blocks = []
    i = start + 1
    while i < end:
        if lines[i].startswith("  - citation:"):
            j = i
            while j + 1 < end and not lines[j + 1].startswith("  - citation:"):
                j += 1
            doc = None
            for k in range(i, j + 1):
                m = re.match(r"      doc_id: (\S+)$", lines[k])
                if m:
                    doc = m.group(1)
                    break
            blocks.append((i, j, doc))
            i = j + 1
        else:
            i += 1
    for key, loc in new:
        doc_id = SOURCES[key]["doc_id"]
        block = source_block(key, loc).split("\n")
        if block and block[-1] == "":
            block.pop()
        pos = None
        for b_start, b_end, doc in blocks:
            if doc and ORDER.index(doc_key(doc)) > ORDER.index(key):
                pos = b_start
                break
        if pos is None:
            pos = blocks[-1][1] + 1 if blocks else end
        lines[pos:pos] = block
        end += len(block)
        blocks = []
        i = start + 1
        while i < end:
            if lines[i].startswith("  - citation:"):
                j = i
                while j + 1 < end and not lines[j + 1].startswith("  - citation:"):
                    j += 1
                doc = None
                for k in range(i, j + 1):
                    m = re.match(r"      doc_id: (\S+)$", lines[k])
                    if m:
                        doc = m.group(1)
                        break
                blocks.append((i, j, doc))
                i = j + 1
            else:
                i += 1
    return lines, end


def doc_key(doc_id):
    for key, meta in SOURCES.items():
        if meta["doc_id"] == doc_id:
            return key
    raise KeyError(doc_id)


def apply_update(entry):
    path = UNITS / entry["key"]
    before = fingerprint(path.read_bytes())
    text = path.read_text(encoding="utf-8")
    original = text

    for old, new in entry.get("replace", []):
        if old not in text:
            raise SystemExit(f"replace not found in {path}: {old[:60]}")
        text = text.replace(old, new, 1)

    lines = text.split("\n")
    start = lines.index("sources:")
    end = next(i for i, line in enumerate(lines) if line.startswith("created:"))
    for key, new_loc in entry.get("ext", []):
        doc_id = SOURCES[key]["doc_id"]
        found = False
        for idx in range(start + 1, end):
            if lines[idx].startswith("  - citation:") and any(
                lines[k] == f"      doc_id: {doc_id}" for k in range(idx, min(idx + 6, end))
            ):
                old_loc = None
                for k in range(idx, min(idx + 6, end)):
                    m = re.match(r'    location: "(.*)"$', lines[k])
                    if m:
                        old_loc = m.group(1)
                        lines[k] = f'    location: "{new_loc}"'
                        break
                if old_loc is None:
                    raise SystemExit(f"location not found for {path} {key}")
                old_last, new_last = last_range(old_loc), last_range(new_loc)
                cit = lines[idx]
                if not re.search(r", [^,]+\.\"$", cit):
                    raise SystemExit(f"citation suffix mismatch in {path}: {cit}")
                lines[idx] = re.sub(r", [^,]+\.\"$", f', {new_last}."', cit, count=1)
                found = True
                break
        if not found:
            raise SystemExit(f"extend target missing in {path}: {key}")

    if entry.get("new"):
        lines, end = insert_sources(lines, start, end, entry["new"])

    text = "\n".join(lines)

    if entry["bullets"]:
        marker = "\n\n## 在层级体系中的位置"
        if marker not in text:
            raise SystemExit(f"hierarchy marker missing in {path}")
        text = text.replace(marker, "\n" + "\n".join(entry["bullets"]) + marker, 1)

    new_count = len(entry.get("new", []))
    if new_count:
        m = re.search(r"^source_count: (\d+)$", text, re.M)
        text = re.sub(
            r"^source_count: \d+$",
            f"source_count: {int(m.group(1)) + new_count}",
            text,
            count=1,
            flags=re.M,
        )

    m = re.search(r"^version: (\d+)$", text, re.M)
    text = re.sub(r"^version: \d+$", f"version: {int(m.group(1)) + 1}", text, count=1, flags=re.M)
    text = re.sub(r"^updated: .*$", "updated: 2026-10-25", text, count=1, flags=re.M)

    if entry.get("note"):
        m = re.search(r"^- 匹配质量: .*$", text, re.M)
        if not m:
            raise SystemExit(f"match-quality line missing in {path}")
        text = text[: m.start()] + m.group(0).rstrip("。") + f"；2026-10-25 复核补：{entry['note']}" + text[m.end():]

    if text == original:
        raise SystemExit(f"no change produced for {path}")
    payload = text.encode("utf-8")
    if DRY:
        preview = Path("06-runtime/_tmp_preview") / entry["key"]
        preview.parent.mkdir(parents=True, exist_ok=True)
        preview.write_bytes(payload)
    else:
        path.write_bytes(payload)
    after = fingerprint(payload)
    return before, after


def main():
    results = {"updates": [], "create": None}
    for entry in UPDATES:
        before, after = apply_update(entry)
        path = UNITS / entry["key"]
        text = path.read_text(encoding="utf-8")
        title = re.search(r"^title: (.+)$", text, re.M).group(1)
        entity = re.sub(r"（.*?）$", "", title).strip()
        results["updates"].append(
            {
                "target_ref": path.as_posix(),
                "entity": entity,
                "candidate_ids": entry["candidates"],
                "primary": entry["candidates"][0],
                "before": before,
                "after": after,
                "note": entry["note"],
            }
        )
        print("updated", path.as_posix(), before["sha256"][:14], "->", after["sha256"][:14])

    event_path = UNITS / "events/hufu-qishe.md"
    if event_path.exists():
        raise SystemExit("event target already exists")
    if not DRY:
        event_path.write_bytes(EVENT.encode("utf-8"))
    results["create"] = {
        "target_ref": event_path.as_posix(),
        "entity": "胡服骑射",
        "candidate_ids": ["2009-zhaonong-zhongguo-yishu-shejishi:cand-03-134"],
        "primary": "2009-zhaonong-zhongguo-yishu-shejishi:cand-03-134",
        "after": fingerprint(EVENT.encode("utf-8")),
        "note": "新建战国服饰改革事件：胡服形制、赵武灵王说辞、带钩与跨文化采纳",
    }
    print("created", event_path.as_posix())

    if DRY:
        print("DRY RUN OK")
        return
    Path("06-runtime/_tmp_overlap_update_result.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("updates", len(results["updates"]), "create", 1)


if __name__ == "__main__":
    main()
