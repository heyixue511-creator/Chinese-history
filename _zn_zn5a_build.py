# -*- coding: utf-8 -*-
"""Build 赵农 2009 第五章 claim rows (28 new claims, no merges)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "第五章 丧乱的文明——三国两晋南北朝时期的设计"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"
I = "04-knowledge/units/institutions/"
PR = "04-knowledge/units/procedures/"
E = "04-knowledge/units/events/"


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(claim_id, cand, ctype, zh, en, supported, note, start, end, key_lines, block_ids, section):
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
                "block_ids": block_ids,
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
    "claim-0525", "cand-05-38", "historiographic_claim",
    "赵农认为，三国两晋南北朝时期是从公元220年的曹魏建立至公元581年的北周灭亡，共361年；这是天翻地覆、南北分裂的年代，这段时期也称魏晋南北朝。",
    "Zhao Nong holds that the Three Kingdoms, Two Jins, and Northern and Southern Dynasties period runs from the founding of Cao Wei in 220 CE to the fall of Northern Zhou in 581 CE, 361 years in all; this era of upheaval and north-south division is also called Wei-Jin-Nanbeichao.",
    [],
    "断言语义取 L3262。起讫年与361年为原文直述，未给历法换算与纪年依据；来源把三国两晋南北朝与魏晋南北朝并称。库内无分期术语条目，未强行链接。",
    3258, 3314, [3262], ["b0130"], "第一节 绪论"))

rows.append(C(
    "claim-0526", "cand-05-43", "interpretive_claim",
    "赵农认为，北朝佛教的兴盛是社会现实的结果：汉末之后连年战乱，尤其北方生灵涂炭、民不聊生，使人们寻找对于人生的精神信仰与寄托，佛教济世慈怀的宗教主张吸引着许多流离失所的人们。",
    "Zhao Nong holds that the flourishing of Buddhism in the Northern Dynasties was a result of social reality: after the late Han, years of war, especially in the north where lives were devastated and livelihood impossible, led people to seek spiritual belief and consolation, so Buddhism's compassionate teaching attracted many displaced people.",
    [E + "fojiao-chuanru-zhongguo.md", T + "shikusi.md"],
    "断言语义取 L3299，并以 L3301“北朝佛教的兴盛正是社会现实的结果”收束。战乱—信仰需求—佛教兴盛的因果为作者解释，未给寺院数量、僧尼统计与信仰人群的地域分布。背景见 events/fojiao-chuanru-zhongguo，洞窟形制见 terms/shikusi。",
    3258, 3314, [3299, 3301], ["b0130"], "第一节 绪论"))

rows.append(C(
    "claim-0527", "cand-05-47", "interpretive_claim",
    "赵农认为，诸葛亮巧用心机，使一种独轮车改换添置了牛马的形象，其身体部分成为载粮食的斗箱，起到了鼓舞士气的作用。",
    "Zhao Nong holds that Zhuge Liang ingeniously modified a wheelbarrow by adding ox-and-horse imagery, with its body serving as a grain hopper, thereby raising morale.",
    [R + "zhuge-liang.md", W + "muniu-liuma.md", T + "dulunche.md"],
    "断言语义取 L3332。牛马形象与斗箱为原文对木牛流马的推测性描述，“鼓舞士气”为作者判断；来源未给木牛流马的复原图、尺寸与运量实测。见 persons/zhuge-liang、works/muniu-liuma、terms/dulunche。",
    3317, 3335, [3332], ["b0132"], "第二节 交通与工具"))

rows.append(C(
    "claim-0528", "cand-05-50", "historiographic_claim",
    "赵农据《三国志·魏书·方技》指出，马钧把旧绫机五十综者五十蹑、六十综者六十蹑皆改为十二蹑，以适应人们现实生活的操作需要；马钧的设计对后来唐宋时期的农具发明有一定的影响。",
    "Citing the Sanguozhi, Zhao Nong notes that Ma Jun reduced the old pattern loom from fifty healds and fifty treadles, or sixty of each, to twelve treadles to suit practical operation, and that Ma Jun's designs had some influence on later Tang-Song agricultural implements.",
    [R + "ma-jun.md", W + "ti-hua-ling-ji.md"],
    "断言语义取 L3349。绫机蹑数见《三国志·魏书·方技》引文；“对唐宋农具发明有一定影响”为作者判断，未给技术传承链与实物比较。见 persons/ma-jun、works/ti-hua-ling-ji。",
    3336, 3352, [3349], ["b0133"], "第二节 交通与工具"))

rows.append(C(
    "claim-0529", "cand-05-53", "interpretive_claim",
    "赵农认为，以牛车代替马车的脚力，与人们的生活观念变化有着明显的关系。",
    "Zhao Nong holds that replacing horse-drawn carriages with ox carts for transport is clearly related to changes in people's attitudes toward life.",
    [T + "niu-che.md"],
    "断言语义取 L3379，前引《晋书·舆服志》“古之贵者不乘牛车”一段。牛车由贱转贵的社会史过程见 terms/niu-che；“生活观念变化”未给具体观念内容与阶层差异。",
    3373, 3405, [3379], ["b0135"], "第二节 交通与工具"))

rows.append(C(
    "claim-0530", "cand-05-61", "interpretive_claim",
    "赵农认为，魏晋书体改变的一个重要原因是社会政治制度的急剧变化；书写变化的另一个原因，是书写工具和材料的变化，如纸张广泛应用于书写过程之中、逐渐代替简牍的材料，使书写的笔画无需着力按捺顿挑。",
    "Zhao Nong holds that one important cause of script change in the Wei-Jin period was abrupt political-institutional change; another was the change in writing tools and materials, as paper came into wide use and gradually replaced bamboo slips, so strokes no longer required forceful pressing and pauses.",
    [T + "kai-shu.md", PR + "zaozhishu.md"],
    "断言语义取 L3427 与 L3438。政治制度与纸张替代简牍两条因果为作者解释；敦煌藏经洞西晋纸本《道德经》为原文所举旁证。概念见 terms/kai-shu、procedures/zaozhishu。",
    3423, 3447, [3427, 3438], ["b0138"], "第三节 造纸与文字"))

rows.append(C(
    "claim-0531", "cand-05-62", "historiographic_claim",
    "赵农认为，楷书成为中华民族表达文化意志的正式书体；文字代表着一个民族成熟的心智，也是文字设计家们探索中产生的智慧建构。",
    "Zhao Nong holds that regular script became the formal script through which the Chinese people express cultural will; writing represents a nation's mature mind and is an intellectual construction produced by the explorations of lettering designers.",
    [T + "kai-shu.md"],
    "断言语义取 L3442 与 L3446。“正式书体”与“民族成熟心智”为作者的历史文化评价，未给历代官文书体制度或字样标准。概念见 terms/kai-shu。",
    3423, 3447, [3442, 3446], ["b0138"], "第三节 造纸与文字"))

rows.append(C(
    "claim-0532", "cand-05-68", "factual_claim",
    "赵农指出，由于西晋时期禁止立碑，所以当时墓志铭特别多；东晋时期仍然禁碑，墓志铭非常盛行。",
    "Zhao Nong notes that because stele erection was prohibited in the Western Jin, epitaphs were especially numerous then; the Eastern Jin continued the prohibition, and epitaphs remained very prevalent.",
    [T + "bei-xue.md"],
    "断言语义取 L3452 与 L3454。禁碑与墓志盛行的对应关系为原文直述，未给禁碑诏令原文与墓志出土统计；同段所举《天发神谶碑》《爨宝子碑》为碑刻实例。概念见 terms/bei-xue。",
    3448, 3482, [3452, 3454], ["b0139"], "第三节 造纸与文字"))

rows.append(C(
    "claim-0533", "cand-05-74", "factual_claim",
    "赵农指出，现存最早的书法作品真迹，是西晋文学家陆机手书的《平复帖》。",
    "Zhao Nong states that the earliest extant original work of calligraphy is the Pingfu Tie handwritten by the Western Jin literatus Lu Ji.",
    [W + "ping-fu-tie.md", R + "lu-ji.md"],
    "断言语义取 L3489。“现存最早”为原文判断，未给历代鉴藏著录与断代依据；书体与流传见 works/ping-fu-tie，作者见 persons/lu-ji。",
    3483, 3512, [3489], ["b0140"], "第三节 造纸与文字"))

rows.append(C(
    "claim-0534", "cand-05-80", "historiographic_claim",
    "赵农认为，白瓷的出现，为制瓷技术的提高奠定了坚实的基础；制瓷业的争奇斗艳，也为釉底类的彩瓷出现起到了铺垫作用。",
    "Zhao Nong holds that the emergence of white porcelain laid a firm foundation for advances in porcelain technology, and that competition among kilns also prepared the ground for underglaze polychrome wares.",
    [T + "baici.md"],
    "断言语义取 L3537。减少胎釉含铁量以保洁白的工艺为原文所记；“为彩瓷出现铺垫”为技术史判断。夏燕靖 claim-0116 有更强的“划时代”表述，本条按赵农口径单独建条，不作跨作者合并。概念见 terms/baici。",
    3515, 3538, [3537], ["b0142"], "第四节 制瓷与服饰"))

rows.append(C(
    "claim-0535", "cand-05-83", "historiographic_claim",
    "赵农认为，南北朝的窑具是不断实践的结果，推动了中国制瓷业的发展。",
    "Zhao Nong holds that the kiln furniture of the Northern and Southern Dynasties resulted from continual practice and drove the development of Chinese porcelain production.",
    [T + "longyao.md", T + "xia-bo.md"],
    "断言语义取 L3550。龙窑分段烧成与匣钵隔离为原文所记的两项窑具改进；“推动制瓷业发展”为作者评价，未给窑址产量与成品率数据。概念见 terms/longyao、terms/xia-bo。",
    3539, 3551, [3550], ["b0143"], "第四节 制瓷与服饰"))

rows.append(C(
    "claim-0536", "cand-05-86", "evaluative_claim",
    "赵农评价，北魏后期孝明帝进一步改革服饰，出现“羽仪服式，悉如魏法，江表士庶，竞相模楷，裹衣博带，被及秣陵”的局面，这印证了北魏汉化的历史进步意义。",
    "Zhao Nong evaluates the late Northern Wei dress reforms under Emperor Xiaoming, when ceremonial dress followed Wei norms and southern gentry and commoners alike emulated the loose-robed, broad-sashed style as far as Moling, as confirming the historical progressiveness of Northern Wei sinicization.",
    [E + "xiaomingdi-fushi-gaige.md", T + "bao-yi-bo-dai.md", B + "luo-yang-qie-lan-ji.md"],
    "断言语义取 L3571，引《洛阳伽蓝记·城东》。“历史进步意义”为作者评价；同段先引《南齐书·魏虏传》《南史·陈伯之传》说明胡汉杂糅的混乱，再以孝明帝改革作转折。见 events/xiaomingdi-fushi-gaige、terms/bao-yi-bo-dai、publications/luo-yang-qie-lan-ji。",
    3552, 3581, [3571], ["b0144"], "第四节 制瓷与服饰"))

rows.append(C(
    "claim-0537", "cand-05-90", "interpretive_claim",
    "赵农认为，裤起到了保护腿部的作用，并改变了以前着衣的上衣下裳，为上衣下裤的衣式；这也是北方游牧民族马背生活的习俗对中原地带的一种影响。",
    "Zhao Nong holds that trousers protected the legs and changed the earlier upper-garment-plus-skirt form into upper garment with trousers; this was one influence of the northern nomadic horseback way of life on the Central Plains.",
    [T + "ku.md", T + "hufu.md"],
    "断言语义取 L3599 与 L3601。裤裆是否缝合随袍衫长短而变，为原文所记的形制细节；游牧影响为作者解释，未给图像编年与出土实物序列。概念见 terms/ku、terms/hufu。",
    3582, 3615, [3599, 3601], ["b0145"], "第四节 制瓷与服饰"))

rows.append(C(
    "claim-0538", "cand-05-102", "historiographic_claim",
    "赵农认为，公元589年隋文帝灭陈后，有感于南陈的腐朽奢侈以及陈朝的复辟势力，下令将建康城邑宫室平荡耕垦；这是中国古代城市建筑史上的悲剧，不是毁灭于临时战乱，而是政治性的根本摧毁。",
    "Zhao Nong holds that after conquering Chen in 589, Emperor Wen of Sui, moved by Southern Chen's decadence and its restoration forces, ordered Jiankang's city and palaces razed and plowed; he calls this a tragedy in Chinese urban architectural history, a fundamental political destruction rather than damage from passing war.",
    [E + "sui-pinghui-jiankang.md", E + "sui-conquers-chen.md"],
    "断言语义取 L3684，引《资治通鉴》卷177。“政治性的根本摧毁”为作者评价；建康六朝屡毁于苏峻之乱、侯景之乱为同节前文所记。见 events/sui-pinghui-jiankang、events/sui-conquers-chen。",
    3637, 3700, [3684], ["b0148"], "第五节 建筑与园林"))

rows.append(C(
    "claim-0539", "cand-06-05", "historiographic_claim",
    "赵农认为，魏晋时期的庄园更多是一种文化意识的选择；魏晋南北朝士族庄园从对物质需求的“庄园”演变为寻求精神寄托的“园林”，魏晋以来的园林之胜成为一种“超隐”的时尚。",
    "Zhao Nong holds that the manors of the Wei-Jin period were more a choice of cultural consciousness; gentry estates evolved from manors serving material needs into gardens sought as spiritual refuge, and the fashion for gardens from the Wei-Jin onward became a kind of transcendent reclusion.",
    [W + "jin-gu-yuan.md", W + "lan-ting-ji-xu.md"],
    "断言语义取 L3703 与 L3726。石崇《金谷诗序》、王羲之《兰亭集序》、庾信《小园赋》、谢灵运山水经营为原文所举园林文本；“文化意识选择”与“超隐”为作者解释。见 works/jin-gu-yuan、works/lan-ting-ji-xu。",
    3701, 3727, [3703, 3726], ["b0149"], "第五节 建筑与园林"))

rows.append(C(
    "claim-0540", "cand-06-10", "historiographic_claim",
    "赵农认为，胡床的出现改变了人们的坐姿，人们开始将榻加高以便小腿下垂，为后来椅子的到来作好了心理和生理的准备。",
    "Zhao Nong holds that the folding stool changed people's sitting posture; people began raising couches so the lower legs could hang down, preparing psychologically and physically for the later arrival of the chair.",
    [T + "huchuang.md", T + "han-ta.md"],
    "断言语义取 L3768。胡床形如马扎、踞胡床使小腿下垂为原文所记；“心理和生理的准备”为作者推论，未给坐具高度序列与图像统计。概念见 terms/huchuang、terms/han-ta。夏燕靖 claim-0321 亦论胡床推动家具高型化，本条按赵农口径单独建条。",
    3730, 3780, [3768], ["b0151"], "第六节 家具与乐器"))

rows.append(C(
    "claim-0541", "cand-06-11", "historiographic_claim",
    "赵农认为，先秦以来的跽、跪、踞坐、箕踞等坐姿习惯与下裳及胫绔相关联：由于先有裳无裤，下体容易暴露，跽、跪、踞坐显示端庄合礼，箕踞则粗俗无礼；汉魏以后裤裆合缝、裤代替裳，加之坐具改革，人们坐姿才随意自由。",
    "Zhao Nong holds that pre-Qin sitting postures, kneeling upright, kneeling, squatting, and sprawling, were bound up with skirts and leg-wraps: with skirts and no trousers the lower body was easily exposed, so formal kneeling displayed propriety while sprawling seemed vulgar; only after Han-Wei times, when trousers were sewn at the crotch and replaced skirts and seating was reformed, did sitting become free and casual.",
    [T + "ku.md", T + "xi-mat.md"],
    "断言语义取 L3745。荆轲“箕踞以骂”见《战国策·燕策》，为原文所举礼俗例证；坐姿与衣制的对应为作者解释，未给图像与人体工学测量。概念见 terms/ku、terms/xi-mat。",
    3730, 3780, [3745], ["b0151"], "第六节 家具与乐器"))

rows.append(C(
    "claim-0542", "cand-06-13", "interpretive_claim",
    "赵农认为，南北朝时期案具有长案、圆案之分，并按书案、奏案、食案、香案等不同用途细化，说明造物意识和生活质量已不断提高。",
    "Zhao Nong holds that by the Northern and Southern Dynasties tables were divided into long and round forms and further differentiated by use, as writing, memorial, dining, and incense tables, showing rising design consciousness and quality of life.",
    [T + "an-furniture.md"],
    "断言语义取 L3783。《南史·江秉之传》《三国志·周瑜传》《后汉书·梁鸿传》分别为书案、奏案、食案所举例证；“造物意识和生活质量提高”为作者判断。概念见 terms/an-furniture。",
    3781, 3803, [3783], ["b0152"], "第六节 家具与乐器"))

rows.append(C(
    "claim-0543", "cand-06-14", "historiographic_claim",
    "赵农认为，由于陶瓷业兴盛，以陶瓷为材料的案具开始流行；陶瓷制作速度快、数量多、器具光洁玉润、价格便宜，很快为社会各层人士广泛接受。",
    "Zhao Nong holds that with the prosperity of the ceramic industry, ceramic tables came into fashion; because ceramics could be made quickly and in quantity, were smooth and lustrous, and were inexpensive, they were soon widely accepted across social strata.",
    [T + "an-furniture.md", T + "qing-ci.md"],
    "断言语义取 L3802。陶瓷案具取代漆木案具的社会扩散为作者判断，未给窑址产量、价格记录与使用阶层统计；同段先说漆案“华贵富丽，是上流社会的喜爱之物”。概念见 terms/an-furniture、terms/qing-ci。",
    3781, 3803, [3802], ["b0152"], "第六节 家具与乐器"))

rows.append(C(
    "claim-0544", "cand-06-25", "synthetic_claim",
    "赵农认为，魏晋南北朝中原大乱、秦汉音乐失传，西域音乐东传在一定意义上填补和丰富了中原的音乐；大量乐器传入加上秦汉中原原有乐器，使魏晋南北朝乐器水平发展到新阶段，为隋唐盛世作好准备，也使西域及朝鲜的许多艺术形式被吸收融进中原文化。",
    "Zhao Nong holds that as the Central Plains fell into chaos and Qin-Han music was lost, the eastward transmission of Western-Region music filled and enriched Central Plains music; the influx of many instruments together with surviving Qin-Han instruments brought instrument making to a new stage, prepared for the Tang golden age, and absorbed many artistic forms from the Western Regions and Korea into Central Plains culture.",
    [T + "pi-pa.md", T + "kong-hou.md", T + "bi-li.md", T + "jie-gu.md", T + "di.md", T + "hu-jia.md"],
    "断言语义取 L3885 与 L3916。筚篥、贝、方响、锣、钹、腰鼓、齐鼓、羯鼓、星、达卜等为原文所举乐器；“填补”“新阶段”为作者综合判断，未给乐律测量与曲目比较。概念见 terms/pi-pa、terms/kong-hou、terms/bi-li、terms/jie-gu、terms/di、terms/hu-jia。",
    3880, 3917, [3885, 3916], ["b0156"], "第六节 家具与乐器"))

rows.append(C(
    "claim-0545", "cand-06-33", "historiographic_claim",
    "赵农认为，北朝莫高窟的中心柱窟吸收了斗拱、枋子、椽子等中原木构建筑的特点，并出现了方形塔的意味，同时也因地制宜地利用石质特点选择不同的制窟方法，从而丰富了中国佛教的洞窟形式。",
    "Zhao Nong holds that the central-pillar caves at Mogao absorbed Central Plains timber-frame features such as brackets, beams, and rafters and acquired a sense of the square pagoda, while adapting cave-cutting methods to the local stone, thereby enriching Chinese Buddhist cave forms.",
    [P + "dunhuang-mogao-ku.md", T + "shikusi.md", E + "liuchao-buddhist-caves.md"],
    "断言语义取 L3970。中心柱窟与印度支提窟的渊源、塔顶与窟顶分离为原文所记；“丰富了中国佛教的洞窟形式”为作者评价。见 places/dunhuang-mogao-ku、terms/shikusi、events/liuchao-buddhist-caves。",
    3950, 3978, [3970], ["b0159"], "第七节 石窟与雕刻"))

rows.append(C(
    "claim-0546", "cand-06-34", "interpretive_claim",
    "赵农认为，敦煌地处甘肃河西走廊西端、汉代丝绸之路开通以来的交通要道，周边大片沙漠戈壁中却有天然绿洲分布、草木茂盛、泉水充沛，因此无论社会生活、经济贸易还是佛教传播，敦煌都是一个理想的聚散地。",
    "Zhao Nong holds that Dunhuang, at the western end of the Hexi Corridor on the route opened by the Han Silk Road, had natural oases with lush vegetation and abundant springs amid desert and gobi, making it an ideal gathering and dispersal point for social life, trade, and Buddhist transmission.",
    [P + "dunhuang-mogao-ku.md", T + "sichou-zhilu.md"],
    "断言语义取 L3952。地理与绿洲条件为原文直述；“理想的聚散地”为作者判断，未给人口、商队与僧侣流动的统计。见 places/dunhuang-mogao-ku、terms/sichou-zhilu。",
    3950, 3978, [3952], ["b0159"], "第七节 石窟与雕刻"))

rows.append(C(
    "claim-0547", "cand-06-38", "historiographic_claim",
    "赵农认为，云冈石窟是河西走廊的敦煌、麦积山等地佛教向东传播的结果；它虽吸收西域某些佛教造像方法，却融进了中原本土文化的观念和技术，并将北方游牧民族审美风尚与中原社会习俗相结合，改变了早期佛像“踖陀罗式”的造像方法，把“偏袒右肩式”及“通肩式”佛像服饰改为“褒衣博带”的中原样式，反映了佛教中原化的积极发展结果。",
    "Zhao Nong holds that the Yungang caves resulted from the eastward spread of Buddhism from Dunhuang, Maijishan, and other Hexi Corridor sites; while absorbing some Western-Region sculptural methods, they fused Central Plains concepts and techniques and combined nomadic aesthetics with Central Plains custom, changing the early Gandhara-style Buddha image and replacing the bare-right-shoulder and full-shoulder robes with the Central Plains loose-robe-and-broad-sash style, an active result of Buddhist sinicization.",
    [P + "yungang-shiku.md", W + "tan-yao-wu-ku.md", T + "bao-yi-bo-dai.md"],
    "断言语义取 L4002。昙曜五窟、迁都洛阳前四五十年的大中型窟开凿为同节所记；“踖陀罗式”按原文用字保留，通常作“犍陀罗”。见 places/yungang-shiku、works/tan-yao-wu-ku、terms/bao-yi-bo-dai。",
    3979, 4003, [4002], ["b0160"], "第七节 石窟与雕刻"))

rows.append(C(
    "claim-0548", "cand-06-45", "historiographic_claim",
    "赵农认为，麦积山的地理位置正是佛教由西到东传播的出口处，也是中原文化沿丝绸之路西进的接纳之地，因此在麦积山石窟中可以看到北朝在融汇中西文化的过程中所起的特殊文化作用。",
    "Zhao Nong holds that Maijishan's location made it both the outlet for Buddhism's spread from west to east and the receiving point for Central Plains culture moving west along the Silk Road, so its caves show the special cultural role the Northern Dynasties played in fusing Chinese and Western cultures.",
    [P + "maijishan-shiku.md", T + "shikusi.md", E + "liuchao-buddhist-caves.md"],
    "断言语义取 L4063 与 L4065。麦积山开凿于后秦、以泥塑壁画为主、栈道连接洞窟为同节所记；“特殊文化作用”为作者评价。见 places/maijishan-shiku、terms/shikusi、events/liuchao-buddhist-caves。",
    4036, 4066, [4063, 4065], ["b0162"], "第七节 石窟与雕刻"))

rows.append(C(
    "claim-0549", "cand-06-48", "historiographic_claim",
    "赵农认为，文化的发展需要积极的相互交流，但魏晋南北朝时期的文化交流大多数情况是因为战争的掠夺而被迫完成的；其中有许多悲欢离合的故事，却促进了中华民族文化艺术的繁荣，中国艺术设计史由此一步步走向深入，到达一种崭新的文化境界。",
    "Zhao Nong holds that cultural development requires active mutual exchange, yet most cultural exchange in the Wei-Jin-Nanbeichao period was forced through wartime plunder; despite its many stories of separation and sorrow, it promoted the flourishing of Chinese culture and art, carrying design history step by step toward a new cultural realm.",
    [],
    "断言语义取 L4085。“大多数情况因战争掠夺而被迫完成”为作者的总括判断，未给战争、人口迁徙与工艺传播的统计或个案清单；库内无对应条目，未强行链接。",
    4083, 4095, [4085], ["b0164"], "第八节 结论"))

rows.append(C(
    "claim-0550", "cand-06-49", "historiographic_claim",
    "赵农认为，艺术设计的历史最终是人性的历史；无论何时何地，人的本质命运的选择，是决定历史进步的原点，也是促进艺术设计历史发展的根本动力。",
    "Zhao Nong holds that the history of design is ultimately the history of human nature; wherever and whenever, the choice of humanity's essential destiny is the origin that determines historical progress and the fundamental force driving design history.",
    [],
    "断言语义取 L4094。这是全章结论的史观表述，不是可检验的因果命题；来源未给论证展开。库内无可承载的器具或制度条目，未强行链接。",
    4083, 4095, [4094], ["b0164"], "第八节 结论"))

rows.append(C(
    "claim-0551", "cand-06-101", "historiographic_claim",
    "赵农认为，由于文人和士族进入了音乐创作和音乐理论之中，乐器的属性不断被发掘和研制，使秦汉以来的乐器设计有了新的拓展。",
    "Zhao Nong holds that as literati and gentry entered music composition and theory, the properties of instruments were continually explored and developed, giving instrument design since Qin-Han times a new expansion.",
    [B + "sheng-wu-ai-le-lun.md", B + "yue-lun.md", R + "ji-kang.md", R + "ruan-ji.md"],
    "断言语义取 L3848。嵇康《声无哀乐论》、阮籍《乐论》、顾恺之《斫琴图》为同节所举文人与理论例证；“新的拓展”为作者判断，未给乐器形制序列。见 publications/sheng-wu-ai-le-lun、publications/yue-lun、persons/ji-kang、persons/ruan-ji。",
    3848, 3848, [3848], ["b0155"], "第六节 家具与乐器"))

rows.append(C(
    "claim-0552", "cand-06-114", "historiographic_claim",
    "赵农认为，魏晋南北朝时期的文化艺术，最重要的特征在于个人意识的觉醒；竹林七贤的玄学清谈、陶渊明的精神回归、王羲之的群贤雅集，以及大量诗人学者的咏叹议论，都构成个人对生命价值的不停追问。",
    "Zhao Nong holds that the most important feature of Wei-Jin-Nanbeichao culture and art was the awakening of individual consciousness; the Seven Sages' metaphysical conversation, Tao Yuanming's spiritual return, Wang Xizhi's elegant gathering of worthies, and the laments and discussions of many poets and scholars all constituted an unceasing personal inquiry into the value of life.",
    [T + "zhu-lin-qi-xian.md", W + "zhulin-qixian-huaxiang-zhuan.md", W + "lan-ting-ji-xu.md", R + "wang-xi-zhi.md", R + "ji-kang.md", R + "ruan-ji.md"],
    "断言语义取 L4087。《兰亭集序》“当其欣于所遇”“后之视今”两处引文为同段例证；“个人意识的觉醒”为作者的时代判断，未给思想史文献清单。见 terms/zhu-lin-qi-xian、works/zhulin-qixian-huaxiang-zhuan、works/lan-ting-ji-xu、persons/wang-xi-zhi、persons/ji-kang、persons/ruan-ji。",
    4087, 4087, [4087], ["b0164"], "第八节 结论"))

out = ROOT / "_zn_zn5a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
(ROOT / "_zn_zn5a_patch.json").write_text("[]", encoding="utf-8", newline="\n")
print("rows", len(rows))
print("links", sum(len(r["supported_by"]) for r in rows))
print("distinct", len({p for r in rows for p in r["supported_by"]}))
from collections import Counter
print("types", dict(Counter(r["claim_type"] for r in rows)))
print("spans", len({(r["source"]["source_span"]["line_start"], r["source"]["source_span"]["line_end"]) for r in rows}))
print("line_spans", sum(1 for r in rows if r["source"]["source_span"]["span_kind"] == "line"))
