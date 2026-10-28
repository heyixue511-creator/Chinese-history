# -*- coding: utf-8 -*-
"""Build _zn_decisions_ch5.json for 赵农 2009 册第五章 unit 候选（88 条）。"""
import io
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"

# cid 后缀 -> (entity, action, target, analysis, approve, apply_note, note)
T = {}

def add(cid, entity, action, target, analysis, approve, apply_note, note):
    T[cid] = dict(entity=entity, action=action, target=target,
                  analysis=analysis, approve=approve, apply_note=apply_note, note=note)

# ---------------- persons ----------------
add("cand-05-45", "诸葛亮", "create", "04-knowledge/units/persons/zhuge-liang.md",
    "L3269 以诸葛亮为三国叙事的轴心；L3309 将其木牛流马与马钧翻车并列为高超设计器具；L3330 引《三国志·蜀书·诸葛亮传》“性长于巧思，损益连弩，木牛流马，皆出其意”与木牛“载一岁粮，日行二十里，而人不大劳”；L3332 引宋高承《事物纪原》的独轮车解释。四段合起来足以支撑人物条，但生卒、籍贯均未载。",
    "新建 persons/zhuge-liang.md：sub_type statesman，primary_dimension B，secondary D。只承载赵农册所记设计相关事迹：连弩、木牛流马与后世解释，不收生平年表与战役。",
    "六节齐全；核心分「设计身份」「连弩与木牛流马」「后世解释与争议」三组；引文内外层引号按来源分层；生卒写未载；不把诸葛亮写成独轮车发明者。",
    "canonical 为新建人物条；器物端见 works/muniu-liuma.md、terms/dulunche.md，与马钧见 persons/ma-jun.md，均不合并。")

add("cand-05-69", "王羲之", "create", "04-knowledge/units/persons/wang-xi-zhi.md",
    "L3498 记官拜右军将军、又称王右军；L3498-L3503 记少年书学卫夫人、草书学张芝、楷书学钟繇、由山东至江南吸收民间书法，并引《晋书·王羲之传》“尤善草隶，为古今之冠”，形成行楷融合的新书体；L3503 列存世勾摹本与怀仁集王书《圣教序》；L3289 与 L4087 给出《兰亭集序》的两处语境。材料足以立人物条，生卒未载。",
    "新建 persons/wang-xi-zhi.md：sub_type calligrapher，primary_dimension C，secondary A。只写书学师承、书体贡献与存世摹本，不写“书圣”等来源未用称谓，不收仕宦生平。",
    "六节齐全；L3498-L3499 被图 5-19 图注隔断（“楷书”／“学钟繇”），分引并说明；引文中的“天下第一行书”只作《兰亭集序》条转述，不在本条作定论。",
    "canonical 为新建人物条；作品端见 works/lan-ting-ji-xu.md，书体端见 terms/xing-shu.md，前辈书家见 persons/zhong-yao.md。")

add("cand-05-71", "陆机", "create", "04-knowledge/units/persons/lu-ji.md",
    "L3489 记“现存最早的书法作品真迹，是西晋文学家陆机手书的《平复帖》”；L3494 记其为著名文学家、杰出书法家，并称《平复帖》使后人看到魏晋书法的真实面貌。两处仅及书法一端，家世、籍贯、生平均未载。",
    "新建 persons/lu-ji.md：sub_type scholar，primary_dimension C，secondary A。只承载《平复帖》相关材料，不扩写文学成就与生平。",
    "六节齐全；核心仅两条：真迹地位、书家身份；生卒与籍贯写未载；不引来源外陆机诗文。",
    "canonical 为新建人物条；作品见 works/ping-fu-tie.md，书体见 terms/zhang-cao.md、terms/jin-cao.md。")

add("cand-05-130", "王献之", "create", "04-knowledge/units/persons/wang-xian-zhi.md",
    "L3505 一行记王献之为王羲之第七子，与父并称二王，流传《鸭头丸帖》《中秋帖》《洛神赋》《二十九日帖》。仅此一处，且来源未说明《洛神赋》为书法还是画作。",
    "新建 persons/wang-xian-zhi.md：sub_type calligrapher，primary_dimension C，confidence low。只照录一行材料，书名照录不解释。",
    "六节齐全；核心分「家世与并称」「流传作品」；《洛神赋》只作书名照录并注明来源未辨书迹与画作；不补生卒、官历。",
    "canonical 为新建人物条；与 persons/wang-xi-zhi.md 是父子分工，不合并。")

add("cand-06-20", "嵇康", "create", "04-knowledge/units/persons/ji-kang.md",
    "L3271 列其为玄学代表人物之一（与何晏、王弼并列）；L3273 有“《广陵散》从此绝矣”的回荡；L3705 记其结局是被杀；L3876-L3878 记其善弹《广陵散》、能创新曲与提出音乐理论，并述《声无哀乐论》“和”与“和声无象”。材料跨思想、政治结局与音乐三端。",
    "新建 persons/ji-kang.md：sub_type thinker，primary_dimension A，secondary B。写玄学身份、政治结局与音乐理论，不收生平年表与诗文。",
    "六节齐全；L3876-L3877 书名被分页隔断（“《声无哀乐”／“论》”），分引并说明；《广陵散》与《声无哀乐论》分别归作品与文献条。",
    "canonical 为新建人物条；文献见 publications/sheng-wu-ai-le-lun.md，同道见 persons/ruan-ji.md，思潮见 terms/xuanxue.md。")

add("cand-06-108", "阮籍", "create", "04-knowledge/units/persons/ruan-ji.md",
    "L3705 记“阮籍的结局是佯醉”；L3878 记其为与嵇康交好的诗人，其《乐论》认为音乐是天地的本体、万物的本性，能使音乐和谐达到万物一体。仅两处，材料薄。",
    "新建 persons/ruan-ji.md：sub_type thinker，primary_dimension A，confidence low。只写佯醉避祸与《乐论》主张，不补生平与诗作。",
    "六节齐全；核心两条并列；不引《咏怀》等来源外诗篇；《乐论》另见 publications/yue-lun.md。",
    "canonical 为新建人物条；与 publications/yue-lun.md 为人物与文献分工。")

add("cand-06-110", "郦道元", "create", "04-knowledge/units/persons/li-dao-yuan.md",
    "L3988-L3990 记北魏地理学家郦道元，其《水经注》描绘武州川水、石祗园舍、灵岩、山堂水殿、烟寺相望，可见当时佛教寺院繁盛。仅一处，且以引文为主。",
    "新建 persons/li-dao-yuan.md：sub_type scholar，primary_dimension A，secondary B，confidence low。只写地理学家身份与《水经注》的云冈记载。",
    "六节齐全；引文按来源断句照录；不补生卒、仕历与《水经注》卷次。",
    "canonical 为新建人物条；文献见 publications/shui-jing-zhu.md，地点见 places/yungang-shiku.md。")

# ---------------- publications ----------------
add("cand-05-57", "《博物志》", "create", "04-knowledge/units/publications/bo-wu-zhi.md",
    "L3415 记西晋文学家张华的著作《博物志》载“剡溪古藤甚多，可造纸，故即名纸为剡藤”，是剡藤纸的唯一文献依据。来源只此一句，卷数、成书年代、版本均未载。",
    "新建 publications/bo-wu-zhi.md：sub_type miscellany，primary_dimension A，secondary B，confidence low。只承载剡藤纸的文献依据，不补全书内容。",
    "六节齐全；核心只一条引文与用途说明；publication_year、edition 写未载。",
    "canonical 为新建文献条；所载名物见 terms/shan-teng-zhi.md。")

add("cand-05-89", "《抱朴子》", "create", "04-knowledge/units/publications/bao-pu-zi.md",
    "L3584 引东晋葛洪《抱朴子》“丧乱以来，衣物屡变。冠履衣服，袖袂财制，日月改易，无复一定”，用以说明胡汉服饰融合后的混乱样式。仅一条引文。",
    "新建 publications/bao-pu-zi.md：sub_type classical_text，primary_dimension A，secondary B，confidence low。只记服饰变迁的这一条引文。",
    "六节齐全；引文照录；不补葛洪生平、内外篇结构与道教内容。",
    "canonical 为新建文献条；所论服饰见 terms/hufu.md、terms/bao-yi-bo-dai.md。")

add("cand-05-103", "《洛阳伽蓝记》", "create", "04-knowledge/units/publications/luo-yang-qie-lan-ji.md",
    "L3657 引《城北》里坊制“方三百步为一里……合有二百二十里”；L3659-L3661 引市东、市南、市西、市北各二里的行业分布与“天下难得之货，咸悉在焉”；L3928 记北魏洛阳1300余座寺院、最著名永宁寺与白马寺。三段分别支撑里坊、市场与佛寺三题。",
    "新建 publications/luo-yang-qie-lan-ji.md：sub_type geography，primary_dimension A，secondary D。按里坊、市场、佛寺三组承载引文，不写作者与成书背景（来源未署作者）。",
    "六节齐全；L3659-L3661 引文跨页跨图注，分段引并说明，不合并为一句；author 与 publication_year 写未载，正文不补“杨衒之”。",
    "canonical 为新建文献条；所记城市见 places/luoyang.md，制度见 terms/lifang-zhi.md，寺院见 works/yong-ning-si.md、works/bai-ma-si.md。")

add("cand-06-21", "《声无哀乐论》", "create", "04-knowledge/units/publications/sheng-wu-ai-le-lun.md",
    "L3876-L3878 记嵇康在《声无哀乐论》中认为音乐的精神终极应是“和”，并提出“和声无象”。书名在来源被分页隔断。",
    "新建 publications/sheng-wu-ai-le-lun.md：sub_type treatise，primary_dimension A，confidence low。只记“和”与“和声无象”两个命题。",
    "六节齐全；注明书名跨页隔断；不补篇目结构、成书年代与后世论争。",
    "canonical 为新建文献条；作者见 persons/ji-kang.md；与 publications/yue-lun.md 分立。")

add("cand-06-109", "《乐论》", "create", "04-knowledge/units/publications/yue-lun.md",
    "L3878 记阮籍《乐论》认为音乐是天地的本体、是万物的本性，能够使音乐和谐达到万物一体。仅一句。",
    "新建 publications/yue-lun.md：sub_type treatise，primary_dimension A，confidence low。只记这一命题，不与《声无哀乐论》合并。",
    "六节齐全；核心一条；不补篇目与成书年代。",
    "canonical 为新建文献条；作者见 persons/ruan-ji.md。")

add("cand-06-111", "《水经注》", "create", "04-knowledge/units/publications/shui-jing-zhu.md",
    "L3988-L3990 记北魏郦道元《水经注》描绘武州川水、石祗园舍、灵岩、山堂水殿、烟寺相望，可见佛教寺院繁盛。仅一条引文。",
    "新建 publications/shui-jing-zhu.md：sub_type geographical_text，primary_dimension A，secondary B，confidence low。只记云冈相关记载。",
    "六节齐全；引文按来源断句照录；不补卷次、成书年代与水系条目总数。",
    "canonical 为新建文献条；作者见 persons/li-dao-yuan.md，地点见 places/yungang-shiku.md。")

# ---------------- works: 碑刻与法书 ----------------
BEI = [
    ("cand-05-67", "《张猛龙碑》", "works/zhang-meng-long-bei.md", "北魏",
     "L3440 把北魏《张猛龙碑》与东魏《司马升墓志铭》并举为“已经是非常成熟的楷书”；L3479 评“雄强挺健，变化自如，书体精美玉润，婀娜多姿”；L3471 为图 5-15。",
     "新建 works/zhang-meng-long-bei.md：sub_type inscription，primary_dimension C。写楷书成熟例证与书风评价两层。"),
    ("cand-05-73", "《兰亭集序》", "works/lan-ting-ji-xu.md", "东晋",
     "L3444 评其书法“挥洒自如，风韵雅逸，实有‘天下第一行书’的美誉”；L3503 记现存均为勾摹本、存20余种；L3717 引流觞曲水一段；L4087 引“当其欣于所遇”与“后之视今”两句。四处合起来可立作品条。",
     "新建 works/lan-ting-ji-xu.md：sub_type calligraphy，primary_dimension C，secondary A。书法评价、摹本状况与两处文句分列，不作文献学分析。"),
    ("cand-05-115", "《司马升墓志铭》", "works/si-ma-sheng-mu-zhi-ming.md", "东魏",
     "L3440 仅一句，与《张猛龙碑》并举为成熟楷书例证。出土地、尺寸、志主生平均未载。",
     "新建 works/si-ma-sheng-mu-zhi-ming.md：sub_type inscription，primary_dimension C，confidence low。只写楷书例证一层。"),
    ("cand-05-65", "《天发神谶碑》", "works/tian-fa-shen-chen-bei.md", "东吴",
     "L3452 记其为南方碑刻代表，原碑刻于公元276年，笔意在于篆隶之间，字势雄伟，以方见圆。一句而含年代与书风。",
     "新建 works/tian-fa-shen-chen-bei.md：sub_type inscription，primary_dimension C。写年代、篆隶之间与以方见圆三点。"),
    ("cand-05-66", "《石门铭》", "works/shi-men-ming.md", "北魏",
     "L3465 记其为摩崖石刻，描写褒斜谷道的开拓情景，并引清人康有为“飞逸奇浑，分行流宕，翩翩欲仙”的评语；L3468 为图 5-14。",
     "新建 works/shi-men-ming.md：sub_type inscription，primary_dimension C。摩崖性质、题材与康有为评语分列，不补碑文与书丹者。"),
    ("cand-05-116", "《禅国山碑》", "works/chan-guo-shan-bei.md", "东吴",
     "L3452 仅一句，与《天发神谶碑》同时期，“以篆书中寓隶意，浑厚苍雄”。",
     "新建 works/chan-guo-shan-bei.md：sub_type inscription，primary_dimension C，confidence low。只写篆隶相兼的书风。"),
    ("cand-05-117", "《爨宝子碑》", "works/cuan-bao-zi-bei.md", "东晋",
     "L3454 记其“仿汉制而立”，以方笔运行，字体错落笨拙，却古朴凝重、寓静于动。",
     "新建 works/cuan-bao-zi-bei.md：sub_type inscription，primary_dimension C，confidence low。照录“仿汉制而立”，不补云南出土与年代。"),
    ("cand-05-118", "《好大王碑》", "works/hao-da-wang-bei.md", "未载（来源置于东晋段）",
     "L3454 仅一句“吉林《好大王碑》也有方正古朴的寓意”。朝代、族属、碑文内容均未载。",
     "新建 works/hao-da-wang-bei.md：sub_type inscription，primary_dimension C，confidence low。只写地点与方正古朴一层，不补高句丽与集安。"),
    ("cand-05-119", "《广武将军碑》", "works/guang-wu-jiang-jun-bei.md", "十六国前秦",
     "L3461 记其“随意纵横，体格多变，体现了北方游牧民族的文化特征”。",
     "新建 works/guang-wu-jiang-jun-bei.md：sub_type inscription，primary_dimension C，confidence low。只写书风与来源的文化归因。"),
    ("cand-05-120", "《爨龙颜碑》", "works/cuan-long-yan-bei.md", "南朝宋",
     "L3463 记南朝碑刻“以楷书文字风格刻碑”，并称《爨龙颜碑》“生动雄强，姿态奇逸”。",
     "新建 works/cuan-long-yan-bei.md：sub_type inscription，primary_dimension C，confidence low。写楷书刻碑与书风评价。"),
    ("cand-05-121", "《瘗鹤铭》", "works/yi-he-ming.md", "南朝梁",
     "L3463 评其“仙气逼人，萧散飞动，却厚重古朴，有南北书风合一的气象”；L3459 为图 5-13。来源只称石刻，未言摩崖。",
     "新建 works/yi-he-ming.md：sub_type inscription，primary_dimension C。写南北书风合一的气象，format 只作石刻，不补摩崖与焦山。"),
    ("cand-05-122", "《张黑女墓志》", "works/zhang-hei-nv-mu-zhi.md", "北魏",
     "L3479 仅一句“端庄媚妩，遒厚精古”。",
     "新建 works/zhang-hei-nv-mu-zhi.md：sub_type inscription，primary_dimension C，confidence low。只写书风一层。"),
    ("cand-05-123", "《敬史君碑》", "works/jing-shi-jun-bei.md", "东魏",
     "L3479 仅一句“清婉秀丽，细巧宜人”。",
     "新建 works/jing-shi-jun-bei.md：sub_type inscription，primary_dimension C，confidence low。只写书风一层。"),
]
for cid, ent, tgt, yr, ana, appr in BEI:
    add(cid, ent, "create", "04-knowledge/units/" + tgt,
        ana, appr + "confidence 按材料厚薄定：一句者 low，两处以上者 medium。",
        "六节齐全；尺寸、字数、书丹者、现存地点一律写原文未载；康有为评语只照录 L3465；图版未核。",
        "canonical 为新建作品条；书体链 terms/wei-bei.md、terms/kai-shu.md、terms/li-shu.md；同类作品互链，不合并。")

add("cand-05-124", "《泰山经石峪金刚经》", "create", "04-knowledge/units/works/tai-shan-jing-shi-yu-jin-gang-jing.md",
    "L3481 记“相传北齐时期的《泰山经石峪金刚经》，也为摩崖刻石，字大径尺，以隶书为主，兼有篆、楷、行书体。气吞河山，雄浑无比”；L3474 与 L3477 两图注一名“泰山金刚经”、一名“北齐《泰山金刚经》”。",
    "新建 works/tai-shan-jing-shi-yu-jin-gang-jing.md：sub_type inscription，primary_dimension C。年代写“相传北齐”，不写成确证。",
    "六节齐全；两图注名称不一致须说明；不补经文字数、书丹者与现存状况。",
    "canonical 为新建作品条；书体见 terms/li-shu.md、terms/wei-bei.md。")

add("cand-05-125", "《西岳华山碑》", "create", "04-knowledge/units/works/xi-yue-hua-shan-bei.md",
    "L3481 仅一句“北周《西岳华山碑》上承北魏，清朗和平，端庄雅致”。",
    "新建 works/xi-yue-hua-shan-bei.md：sub_type inscription，primary_dimension C，confidence low。只写上承北魏与书风两点。",
    "六节齐全；尺寸、碑文、现存地写原文未载；图版未核。",
    "canonical 为新建作品条；与 terms/wei-bei.md 为风格承接关系。")

add("cand-05-72", "《平复帖》", "create", "04-knowledge/units/works/ping-fu-tie.md",
    "L3489 记其为“现存最早的书法作品真迹”，为西晋陆机手书；L3494 记其书体“为章草和今草之间的一种书体，含隶含篆，笔法奇倔”，并称其使后人看到魏晋书法真实面貌；L3492 为图 5-18。",
    "新建 works/ping-fu-tie.md：sub_type calligraphy，primary_dimension C。写真迹地位、书体位置与史料意义三层。",
    "六节齐全；“章草和今草之间”写为来源判断，不作定论；尺寸、行数、收藏地写未载。",
    "canonical 为新建作品条；作者见 persons/lu-ji.md，书体见 terms/zhang-cao.md、terms/jin-cao.md。")

# ---------------- works: 器物、绘画、园林 ----------------
add("cand-05-78", "青瓷谷仓罐（永安三年，公元260年）", "create", "04-knowledge/units/works/qing-ci-gu-cang-guan.md",
    "L3525 记青瓷谷仓罐“在口沿上以人物、飞禽为雕饰，而在罐腹部以羊、龟、蛇、鱼等动物为浮雕造型，整个造型由两个罐粘接而成，将制器和雕塑融为一体”，并记“碑文标志为‘永安三年’（公元260年）”的孙吴实例；L3754 为图 5-36 南朝青瓷谷仓罐。",
    "新建 works/qing-ci-gu-cang-guan.md：sub_type porcelain_jar，primary_dimension B。形制、铭文年代与图注分列；原文“碑文标志”疑为「铭文标志」，照录标疑。",
    "六节齐全；不补通高、出土墓号与收藏地；图 5-36 图版未核，不据图补纹样细节。",
    "canonical 为新建作品条；瓷系见 terms/qing-ci.md，窑口见 places/yue-kiln.md。")

add("cand-05-93", "《洛神赋图》", "create", "04-knowledge/units/works/luo-shen-fu-tu.md",
    "L3620 以《洛神赋图》中的妇女形象作为“上着襦、衫，下垂长裙，而襦、衫以右衽为主”的当时写照；L3625、L3644、L3655 三条图注均为“东晋 顾恺之《洛神赋图》局部”。本条价值在服饰图像证据。",
    "新建 works/luo-shen-fu-tu.md：sub_type painting，primary_dimension B，secondary C。只写服饰写照与三条图注，不补画卷内容、材质、尺寸与收藏地。",
    "六节齐全；明确图版未核，不据图补写人物、构图与设色；三图注同属一本，分列不合并。",
    "canonical 为新建作品条；作者见 persons/gu-kai-zhi.md，服饰见 terms/ru.md、terms/qun.md。")

add("cand-06-01", "金谷园", "create", "04-knowledge/units/works/jin-gu-yuan.md",
    "L3707 记“即使是石崇的金谷园，也是政治势力较量的结果”，并引杜牧《金谷园》“日暮东风怨啼鸟，落花犹似坠楼人”，说明指石崇失败后绿珠坠楼（原文“石祟”疑误）；L3715 引石崇《金谷诗序》自述别庐在金谷涧中，有清泉茂林、众果竹柏、草药、水碓、鱼池、土窑，并给出“物备”到“娱目欢心”的解读。",
    "新建 works/jin-gu-yuan.md：sub_type private_garden，primary_dimension B，secondary A、D。写园林构成、经济性解读与政治背景三层。",
    "六节齐全；“石祟”照录标疑为「石崇」，不径改；不补园林尺度、方位与今地名；图版未核。",
    "canonical 为新建作品条；地点背景见 places/luoyang.md，名士群体见 terms/zhu-lin-qi-xian.md。")

add("cand-06-09", "朱然墓黑红漆几", "create", "04-knowledge/units/works/zhu-ran-mu-hei-hong-qi-ji.md",
    "L3770 记“魏晋时期的凭几是一种三足形，几面呈扁平圆弧形，如安徽马鞍山东吴朱然墓中的黑红漆几，高26厘米，弧形弦长69.5厘米，几面宽13厘米，可知此类凭几的使用已经相当成熟”。尺寸是三件中唯一实测数据。",
    "新建 works/zhu-ran-mu-hei-hong-qi-ji.md：sub_type lacquer_furniture，primary_dimension B。写器形、三项尺寸与作者的成熟度判断。",
    "六节齐全；尺寸照录厘米；不补胎骨、髹饰层次与墓室编号；图版未核。",
    "canonical 为新建作品条；器类见 terms/ji-furniture.md，配套见 terms/yin-nang.md，时代对照见 terms/han-ta.md。")

add("cand-06-107", "《斫琴图》", "create", "04-knowledge/units/works/zhuo-qin-tu.md",
    "L3874 仅一句“此时，制造古琴的经验也很丰富，相传东晋顾恺之作有《斫琴图》，可见南方制作乐器工序的严格”。",
    "新建 works/zhuo-qin-tu.md：sub_type painting，primary_dimension B，confidence low。只写相传作者与制琴工序的史料价值。",
    "六节齐全；“相传”保留，不写成顾恺之确作；不补画面内容、材质与收藏地。",
    "canonical 为新建作品条；作者见 persons/gu-kai-zhi.md。")

add("cand-06-42", "《帝后礼佛图》", "create", "04-knowledge/units/works/di-hou-li-fo-tu.md",
    "L4017 为图 5-55“北魏《帝后礼佛图》”；L4030-L4032 记其“利用了浮雕的效果，表现的是帝后礼佛的场面”，并以中原浮雕技巧刻画佛教活动故事，体现佛教文化与中原艺术的结合。同段宾阳中洞营构与花饰雕凿属洞窟整体，不归本图。",
    "新建 works/di-hou-li-fo-tu.md：sub_type stone_relief，primary_dimension B，secondary C。写浮雕手法、题材与艺术融合三点，地点归宾阳中洞。",
    "六节齐全；L4030 行末“充分刻画出了佛”与 L4032 行首“教活动的故事”为分页断句，分引并说明；不补尺寸、流失与现藏。",
    "canonical 为新建作品条；洞窟见 places/longmen-grottoes.md。")

# ---------------- works: 工程与建筑 ----------------
add("cand-05-49", "翻车（龙骨水车）", "create", "04-knowledge/units/works/fanche-longgu-shuiche.md",
    "L3342 记马钧为三国能工巧匠式设计家、有“巧思绝世”之说，句末“首推”被图 5-6 隔断；L3347 续以“‘翻车’，即后世的龙骨水车”，并引《三国志·魏书·方技》“乃作翻车，令儿童转之，而灌水自覆，更入更出，其巧百倍于常”，另评其改变农人劳作的被动、提高生产效率。",
    "新建 works/fanche-longgu-shuiche.md：sub_type agricultural_machine，primary_dimension B。写马钧身份、翻车即龙骨水车、史书效能记载与社会效果三层。",
    "六节齐全；“首推”与“翻车”跨图注断句须分引并说明；不补翻车结构图说与后世水车谱系；图版未核。",
    "canonical 为新建作品条；作者见 persons/ma-jun.md，独轮车端见 terms/dulunche.md、works/muniu-liuma.md。")

add("cand-05-51", "千里船", "create", "04-knowledge/units/works/qian-li-chuan.md",
    "L3367 引《南齐书·祖冲之传》“又造千里船，于新亭江试之，日行百余里”，并判断“这应是一种人力脚踏车轮的推动船”。一句引文加一句推断。",
    "新建 works/qian-li-chuan.md：sub_type watercraft，primary_dimension B。写文献记载与作者的技术推断两层，推断保留“应是”。",
    "六节齐全；不把“人力脚踏车轮”写成确证；不补船体尺度、载重与新亭江今地。",
    "canonical 为新建作品条；船类见 terms/louchuan.md，水域见 places/nanjing.md。")

add("cand-06-26", "永宁寺", "create", "04-knowledge/units/works/yong-ning-si.md",
    "L3928 记北魏洛阳1300余座寺院中最著名者为永宁寺与白马寺；L3930 记其516年兴建、534年毁于大火，经考古勘探位于宫城南1公里、长方形、周长1060米，中心有塔基并出土陶塑石雕与建筑材料，原为九层木塔、推测高度不低于75米。",
    "新建 works/yong-ning-si.md：sub_type temple，primary_dimension B，secondary A。写文献地位、兴毁年代、勘探数据与木塔推测高度。",
    "六节齐全；高度写“推测”，不写成实测；不补塔基边长、寺院布局细目与出土件数。",
    "canonical 为新建作品条；文献见 publications/luo-yang-qie-lan-ji.md，城市见 places/luoyang.md，塔制见 terms/fota.md。")

add("cand-06-27", "白马寺", "create", "04-knowledge/units/works/bai-ma-si.md",
    "L3928 记其为洛阳最著名寺院之一；L3932 记“白马寺至今完好”，并引《洛阳伽蓝记·城西》“白马寺，汉明帝所立也，佛入中国之始……时白马负经而来，因以为名”，末评其为中国佛教传入之初的建筑、在佛教建筑中有特殊地位。原文“谴使”疑为「遣使」。",
    "新建 works/bai-ma-si.md：sub_type temple，primary_dimension B，secondary A。写始建传说、名称由来与建筑史地位三层。",
    "六节齐全；“谴使”照录标疑为「遣使」，不径改；“佛入中国之始”注明为《洛阳伽蓝记》语；不补寺址沿革、现存殿宇与年代。",
    "canonical 为新建作品条；文献见 publications/luo-yang-qie-lan-ji.md，同城寺院见 works/yong-ning-si.md。")

add("cand-06-36", "昙曜五窟", "create", "04-knowledge/units/works/tan-yao-wu-ku.md",
    "L3992 记约公元453年“昙曜白帝，于京城西武州塞，凿山石壁，开窟五所，镌建佛像各一。高者七十尺，次者六十尺，雕饰奇伟，冠于一时”，称其为开凿云冈石窟的最早时间；L3998 记早期昙曜五窟“基本上是一种穹隆式大洞结构，以大佛为主”，为云冈标志性雕塑。",
    "新建 works/tan-yao-wu-ku.md：sub_type cave_temple，primary_dimension B，secondary A。写开凿年代与主持者、五窟与佛像尺度、穹隆式形制三层。",
    "六节齐全；年代写“大约”，佛像高度照引文尺数不换算；不补五窟编号、对应帝王与现藏。",
    "canonical 为新建作品条；石窟群见 places/yungang-shiku.md，文献见 publications/shui-jing-zhu.md。")

add("cand-06-113", "义县万佛堂", "create", "04-knowledge/units/works/yi-xian-wan-fo-tang.md",
    "L4079 记“义县万佛堂在辽宁义县，为北朝时期开凿，但是后来受河流影响，加上明清时期的改造，其原始风貌已经丧失”，但仍“作为北朝造像的系统”有研究价值；L4069 同一石窟名单中写作“辽宁义县万佛寺”，名称不一致。",
    "新建 works/yi-xian-wan-fo-tang.md：sub_type cave_temple，primary_dimension B，confidence low。写地点、开凿期、原貌丧失与研究价值四点。",
    "六节齐全；须写明来源前后名称不一致（万佛寺／万佛堂），标题取“万佛堂”；不补窟数、造像与保护级别。",
    "canonical 为新建作品条；同类见 places/yungang-shiku.md、places/longmen-grottoes.md。")

# ---------------- terms: G5 ----------------
add("cand-05-39", "魏晋玄学", "create", "04-knowledge/units/terms/xuanxue.md",
    "L3271 记汉代经学衰败后出现以何晏、王弼、嵇康为代表的玄学；L3273 记其“以老庄、易经的精神为依托，关注个人的生存现实，讨论人与社会、人与自然的特殊关系的学说”，并有“《广陵散》从此绝矣”的回荡；L3726 记魏晋玄学崇尚自然、完善个人生命的觉醒，成为园林繁盛的文化因素。",
    "新建 terms/xuanxue.md：sub_type intellectual_current，primary_dimension A。写代表人物、学说取向与文化后果三层。",
    "六节齐全；不补“贵无”“名教与自然”等来源外哲学史内容；三处引文分列。",
    "canonical 为第五章玄学条（cand-06-04 并入本条）；人物见 persons/ji-kang.md，群体见 terms/zhu-lin-qi-xian.md。")

add("cand-05-40", "南秀北雄", "create", "04-knowledge/units/terms/nan-xiu-bei-xiong.md",
    "L3289 记“南北疆土分裂的结果，最终是文化意义上的分化，南秀北雄的审美趣味成为后来文化风格的散逸”，并以苍雄的北朝摩崖石刻与柔美的南方文人书札对举；L3291 记南北朝继续“南朝的旖旎和北方的豪爽”；L3487 记写经书体也体现这一风格。",
    "新建 terms/nan-xiu-bei-xiong.md：sub_type aesthetic_concept，primary_dimension A。写命题、书法例证与写经例证三层。",
    "六节齐全；写明是作者的审美概括，不作风格史定论；不补南北宗论。",
    "canonical 为新建术语条；例证见 works/yi-he-ming.md、terms/wei-bei.md。")

add("cand-05-52", "牛车", "create", "04-knowledge/units/terms/niu-che.md",
    "L3379 记贵族以牛车代步并演变为社会时尚，引《晋书·舆服志》述汉魏以来由“贫者至乘牛车”到“天子至士遂以为常乘”的转变；L3384 记牛车用途扩大、速度已达马车、乘坐姿势改变，立乘只在重大礼仪出现；L3382 为图 5-8。",
    "新建 terms/niu-che.md：sub_type vehicle，primary_dimension B，secondary D。写社会时尚、制度引文与乘坐方式变化三层。",
    "六节齐全；引文照录；不补车厢形制、载重与牛种；图版未核。",
    "canonical 为新建术语条；车制背景见 terms/shuang-yuan-che.md、terms/che-tong-gui.md。")

add("cand-05-55", "剡藤纸", "create", "04-knowledge/units/terms/shan-teng-zhi.md",
    "L3415 记活动帘床纸模的抄纸法，并引《博物志》“剡溪古藤甚多，可造纸，故即名纸为剡藤”，注明剡溪在浙江嵊县、从西晋到唐代驰名数百年。",
    "新建 terms/shan-teng-zhi.md：sub_type paper，primary_dimension B。写抄纸法背景、得名由来与产地年代三点。",
    "六节齐全；不补纸质检测、帘纹与唐以后衰落原因。",
    "canonical 为新建术语条；文献见 publications/bo-wu-zhi.md。")

add("cand-05-60", "行书", "create", "04-knowledge/units/terms/xing-shu.md",
    "L3425 记章草、行书、楷书在魏晋南北朝成熟稳定；L3442 记“介于楷书和草书之间的行书也成熟起来”；L3444 记行书出现于汉代而独立与楷书有关，张弛起伏、字迹清晰，并称《兰亭集序》有“天下第一行书”之誉。",
    "新建 terms/xing-shu.md：sub_type calligraphy_script，primary_dimension C。写成熟时点、与楷草的关系、特征与代表作四层。",
    "六节齐全；“天下第一行书”写为誉称转述；不补行书笔法术语与后世名家谱系。",
    "canonical 为新建术语条；对照见 terms/kai-shu.md、terms/jin-cao.md，作品见 works/lan-ting-ji-xu.md。")

add("cand-05-114", "草书（今草）", "create", "04-knowledge/units/terms/jin-cao.md",
    "L3425 记章草在魏晋南北朝成熟；L3442 记“草书随着书体改革，将章草演变为今草，去掉章草的波磔，而加强笔势的转变，迅速发展成一种独立的书体”，并评其流畅飞扬、能表现内心情绪，也指出随意性带来表达模糊；L3494 以《平复帖》为章草与今草之间的书体。",
    "新建 terms/jin-cao.md：sub_type calligraphy_script，primary_dimension C。写章草到今草的演变、笔势特征与得失评价三层。",
    "六节齐全；与既有 terms/zhang-cao.md 分工，只补今草；不补张芝、二王草书谱系。",
    "canonical 为新建术语条；前身见 terms/zhang-cao.md，实例见 works/ping-fu-tie.md。")

add("cand-05-63", "碑学", "create", "04-knowledge/units/terms/bei-xue.md",
    "L3450 仅一句“魏晋以来，石刻文字广为流行，其中分为墓志和碑刻，后人统称为碑学”。",
    "新建 terms/bei-xue.md：sub_type calligraphy_concept，primary_dimension C，confidence low。只写墓志与碑刻合称这一层。",
    "六节齐全；不得引入清代碑学运动、阮元与康有为等来源外内容；L3465 康有为评语归 terms/wei-bei.md 与 works/shi-men-ming.md，不在本条展开。",
    "canonical 为新建术语条；书风见 terms/wei-bei.md，例证见 works/zhang-meng-long-bei.md。")

add("cand-05-64", "魏碑", "create", "04-knowledge/units/terms/wei-bei.md",
    "L3465 小标题“魏碑”下列《龙门二十品》中的《始平公造像记》《杨大眼造像记》为“质朴天然，开张纵逸”，《石门铭》为摩崖石刻并附康有为“飞逸奇浑，分行流宕，翩翩欲仙”评语；L3481 补北齐《泰山经石峪金刚经》以隶为主兼篆楷行、北周《西岳华山碑》上承北魏。",
    "新建 terms/wei-bei.md：sub_type calligraphy_style，primary_dimension C。写代表作品、书风评价与北朝后期的延续三层。",
    "六节齐全；不写“魏碑十美”等来源外提法；康有为评语照录。",
    "canonical 为新建术语条；作品见 works/shi-men-ming.md、works/zhang-meng-long-bei.md，窟群见 places/longmen-grottoes.md。")

add("cand-05-82", "匣钵", "create", "04-knowledge/units/terms/xia-bo.md",
    "L3546 记南北朝窑址出土许多窑具，匣钵对瓷器成型有重要作用；L3548 记其防挤压变形、以隔离避免烟尘熏染与釉色减弱；L3550 记其体现窑工经验、在有限空间内掌握温度变化并提高质地纯度，该句与 L3548 行末“匣钵的”跨页断句。",
    "新建 terms/xia-bo.md：sub_type kiln_furnishing，primary_dimension B。写成型保护、防熏染与控温三项功能。",
    "六节齐全；“匣钵的／使用”跨页断句须分引并说明；不补匣钵材质、尺寸与装烧工序。",
    "canonical 为新建术语条；窑炉见 terms/longyao.md，瓷器见 terms/qing-ci.md、terms/baici.md。")

add("cand-05-84", "冕冠与冕旒", "create", "04-knowledge/units/terms/mian-guan-mian-liu.md",
    "L3556 记冠冕为魏晋贵族士人的地位象征，冕为帝王头饰、分冕板与冕旒，冕板宽7寸、长1尺2寸、前圆后方、固定在通天冠上，冕旒前后各垂12旒、由珊瑚珠制成；并记阎立本《历代帝王图》晋武帝像与南朝12、9、8、6旒的等级规定。",
    "新建 terms/mian-guan-mian-liu.md：sub_type headwear，primary_dimension B，secondary D。写形制、图像例证与南朝等级三层。",
    "六节齐全；尺寸照原文寸尺不换算；“各垂挂12旒由珊瑚珠制成的冕旒”原文重复用字，照录标疑；不补历代冕制演变。",
    "canonical 为新建术语条；冠类见 terms/futou.md，服制见 terms/yuanling-paoshan.md、terms/handai-guanzhi.md。")

add("cand-05-87", "襦", "create", "04-knowledge/units/terms/ru.md",
    "L3586 小标题“襦衣和短袄”下首句原文作“補，是一种短衣”，其后引《说文解字》“襦，短衣也”，记其多为布制、也有纱罗；L3591 记襦与袄相近、袄为北朝皮制短袄；L3620 记日常女服上着襦、衫，下垂长裙，襦衫以右衽为主。",
    "新建 terms/ru.md：sub_type garment_form，primary_dimension B。写定义与用材、与袄的关系、女服中的位置三层。",
    "六节齐全；原文“補”照录标疑为「襦」，不径改；L3586 行末“襦与袄相”与 L3591 行首“近”被图 5-23 隔断，分引并说明；不补唐宋襦制演变。",
    "canonical 为新建术语条；近缘见 terms/ao.md、terms/qun.md、terms/shan-liang-dang-shan.md。")

add("cand-05-88", "木屐（谢公屐）", "create", "04-knowledge/units/terms/mu-ji.md",
    "L3606 记木屐为居家冶游的鞋具、脚底两齿以践踏泥水，江南中原均流行；并记传说谢灵运好名山游、多着木屐而有“谢公屐”之说，引李白《梦游天姥吟留别》“脚著谢公屐，身登青云梯。半壁见海日，空中闻天鸡”；末言其适于江南湿润温暖气候。",
    "新建 terms/mu-ji.md：sub_type footwear，primary_dimension B。写形制、谢公屐典故与气候适应三层。",
    "六节齐全；谢灵运事保留“传说中的”；不补屐齿材质、形制复原与日本影响。",
    "canonical 为新建术语条；鞋类见 terms/mao.md，坐具对照见 terms/huchuang.md。")

add("cand-05-126", "袄", "create", "04-knowledge/units/terms/ao.md",
    "L3591 仅一句半：“而袄早期应为北朝的皮制短袄，袖口窄紧，亦为北方游牧民族的打扮，在南北朝时期广泛流传于南方。”前半句“襦与袄相”在 L3586 行末。",
    "新建 terms/ao.md：sub_type garment_form，primary_dimension B，confidence low。只写早期形态、族属来源与南传三点。",
    "六节齐全；与 L3586 的跨图注断句分别引；不补唐宋以后袄的形制演变。",
    "canonical 为新建术语条；近缘见 terms/ru.md、terms/qiu.md、terms/hufu.md。")

add("cand-05-127", "衫（两裆衫）", "create", "04-knowledge/units/terms/shan-liang-dang-shan.md",
    "L3593 记衫本为汉制便服、无袖口、衣袖宽大、多为夏季居家便服；并记两裆衫前后两片布衣、肩部以布带连缀、缘起于铠甲样式，因简洁适用而流行。",
    "新建 terms/shan-liang-dang-shan.md：sub_type garment_form，primary_dimension B。写衫的特征与两裆衫结构、来源两层。",
    "六节齐全；保留来源用字“两裆”，不写成“裲裆”或“两当”；不补两裆铠与唐代半臂。",
    "canonical 为新建术语条；对照见 terms/ru.md、terms/qun.md，甲制见 terms/han-armor.md。")

add("cand-05-128", "裘", "create", "04-knowledge/units/terms/qiu.md",
    "L3595 仅一句：“裘衣与大氅，均为皮制御寒保暖的衣服。贵族与普通人的裘衣区别，仅仅是皮料的差异。”",
    "新建 terms/qiu.md：sub_type garment_form，primary_dimension B，confidence low。只写皮制保暖与等级差别在皮料两点。",
    "六节齐全；不补狐裘、羔裘等礼制等级（来源未载）。",
    "canonical 为新建术语条；并称见 terms/da-chang.md，族属见 terms/hufu.md。")

add("cand-05-131", "大氅", "create", "04-knowledge/units/terms/da-chang.md",
    "L3595 仅一句：“而大氅一般无袖，比皮裘宽敞肥大，后来亦称‘披风’，着衣行走，飘逸欲仙，成为魏晋名士冬季喜爱的衣物。”",
    "新建 terms/da-chang.md：sub_type garment_form，primary_dimension B，confidence low。写无袖、宽大、又称披风与名士服用四点。",
    "六节齐全；不补披风在后世的形制演变。",
    "canonical 为新建术语条；并称见 terms/qiu.md，披帛见 terms/pibo.md。")

add("cand-05-129", "裙", "create", "04-knowledge/units/terms/qun.md",
    "L3597 记“裙亦名裳，多与襦配置，由于裤的兴起，裙虽然仍为正式场合的服饰，但是在魏晋以后被裤替代”；L3620 记女裙因身份而异，贵族有复裙、双裙、长度摇曳拖地，劳动妇女裙摆紧短明快。",
    "新建 terms/qun.md：sub_type garment_form，primary_dimension B。写与襦相配、被裤替代、女裙的等级差异三层。",
    "六节齐全；两处分属“裙裤”与“女服”两节，分别标注；不补裙幅、褶数与织物。",
    "canonical 为新建术语条；上装见 terms/ru.md，替代者见 terms/ku.md，图像见 works/luo-shen-fu-tu.md。")

add("cand-05-132", "裤", "create", "04-knowledge/units/terms/ku.md",
    "L3599 行末“裤起到了保护腿部的作用，并改变了以前着衣的上衣下”与 L3601 行首“裳，为上衣下裤的衣式”分页断句；L3601 记此为北方游牧民族马背生活习俗对中原的影响，裤式因袍衫长衣有时裆部无须缝合、短衣时合裆裤流行；L3745 记汉魏以后裤裆合缝、裤代替裳，坐姿才随意自由。",
    "新建 terms/ku.md：sub_type garment_form，primary_dimension B。写上衣下裤之变、族属来源、合裆与否、与坐姿的关系四层。",
    "六节齐全；“上衣下／裳”跨页断句须分引并用「 」注明拼合；不补裈、裆、袴的字形考辨。",
    "canonical 为新建术语条；对照见 terms/qun.md、terms/hufu.md，坐姿见 terms/huchuang.md。")

# ---------------- terms: G6 ----------------
add("cand-05-91", "假髻", "create", "04-knowledge/units/terms/jia-ji.md",
    "L3627 记魏晋南北朝妇女头饰复杂，除各种发式外普遍使用假髻，并引《北齐书·帝纪第八》“而危邪之状如飞鸟，至于南面，则髻心正西。始自宫内为之，被于四远”，末言其改变头发造型、影响深远。",
    "新建 terms/jia-ji.md：sub_type headwear，primary_dimension B。写普遍使用、文献形容与影响三点。",
    "六节齐全；引文首字“而”与“髻心正西”照录，不校改；不补假髻材质与制作工艺。",
    "canonical 为新建术语条；同类头饰见 terms/qing-dai-shoushi-toushi.md，妆饰见 terms/dai.md。")

add("cand-05-92", "黛", "create", "04-knowledge/units/terms/dai.md",
    "L3627 记假髻带来化妆技术与观念的兴盛，包括白粉、红粉与黛的使用；L3629 记“黛原指将眉毛剃去，而以青黑色的颜料描出眉毛”，并引陶渊明《闲情赋》“愿在眉而为黛，随瞻视以闲扬”，续记粉黛连称与《木兰辞》《东飞伯劳歌》《子夜歌》诸例。",
    "新建 terms/dai.md：sub_type cosmetic，primary_dimension B。写妆饰风气、黛的用法与文学例证三层。",
    "六节齐全；“黛原指将眉毛剃去”照录；文学例证择一二即可，不必全引；不补石黛、螺子黛等名物。",
    "canonical 为新建术语条；头饰见 terms/jia-ji.md，妆饰图像见 terms/huazhuangtu.md。")

add("cand-06-02", "竹林七贤", "create", "04-knowledge/units/terms/zhu-lin-qi-xian.md",
    "L3307 记“竹林七贤”的高迈散淡对后世影响深刻；L3705 以竹林比喻朝廷与山水之间的过渡，并记嵇康被杀、阮籍佯醉、山涛王戎进入权力中心；L3265 与 L3710 两图注分别为“竹林七贤——嵇康”“竹林七贤《阮咸》”。",
    "新建 terms/zhu-lin-qi-xian.md：sub_type social_group，primary_dimension A。写群体气质、政治处境与图注三点。",
    "六节齐全；来源未列全七人姓名，不得补全名单；不写南京墓砖画（另有条目）；两条图注图版未核。",
    "canonical 为新建术语条；人物见 persons/ji-kang.md、persons/ruan-ji.md，思潮见 terms/xuanxue.md。")

add("cand-06-15", "储具", "create", "04-knowledge/units/terms/chu-ju.md",
    "L3809 记“储具的使用是社会生活富裕的象征”；L3811 记橱（厨）为大型储具、带门，柜有抽屉，并引《晋书·顾恺之传》橱画故事与“书厨”戏指；L3813 记柜通匮、金匮为铜制小柜，大者为柜、次者为匣、小者为椟；L3815 记匣带推拉抽屉、有漆匣玉函；L3817 记箱有书箱衣箱、漆箱竹衣箱；L3819-L3821 记箧为小箱、装书用竹木、装珠宝用金银箧。",
    "新建 terms/chu-ju.md：sub_type furniture_category，primary_dimension B。按橱、柜、匣、箱、箧五类并列，每条只取来源原句要点。",
    "六节齐全；须在描述中说明本条是类目聚合条而非单一器物；不补尺寸、出土地与榫卯；五类互不替代。",
    "canonical 为新建类目条；相关器物见 terms/duozi-he.md、terms/qi-jiuju-baozhuang-he.md、terms/xiangxie.md。")

add("cand-06-95", "隐囊", "create", "04-knowledge/units/terms/yin-nang.md",
    "L3770 末句“与三足几配套使用的是隐囊”；L3772 记“隐囊是棉锦织物的靠垫。将隐囊放置于移动的三足几上，身体可以前后左右依靠休息，减轻了长期跽坐的疲劳”。",
    "新建 terms/yin-nang.md：sub_type furniture，primary_dimension B，confidence low。写材质、与三足几的配套用法与功能三点。",
    "六节齐全；不补图像、尺寸与出土实例。",
    "canonical 为新建术语条；配套见 terms/ji-furniture.md、works/zhu-ran-mu-hei-hong-qi-ji.md。")

add("cand-06-96", "筌台", "create", "04-knowledge/units/terms/quan-tai.md",
    "L3774 记“在坐具中还有一种名叫‘筌台’的腰鼓形坐墩，也称‘筌蹄’”，其形象为腰鼓、在魏晋佛教造像中屡屡出现，中原本有墩的造型，佛教进入中原时被引入寺院成为实用坐具。",
    "新建 terms/quan-tai.md：sub_type furniture，primary_dimension B，confidence low。写别名、腰鼓形、造像例证与寺院来源四点。",
    "六节齐全；不补“筌蹄”与佛教譬喻的关系等来源外内容；不补尺寸与实物。",
    "canonical 为新建术语条；坐具谱系见 terms/huchuang.md、terms/yin-nang.md。")

add("cand-06-98", "承尘", "create", "04-knowledge/units/terms/cheng-chen.md",
    "L3825 仅一句：“承尘是在室内的床榻上方悬挂的席子或木板，可防止灰尘下落到居住者的身上。”",
    "新建 terms/cheng-chen.md：sub_type furnishing，primary_dimension B，confidence low。只写位置、材质与功能三点。",
    "六节齐全；不补承尘的尺寸、悬挂方式与图像。",
    "canonical 为新建术语条；同类陈设见 terms/weizhang.md、terms/ping-feng.md。")

add("cand-06-100", "帘子", "create", "04-knowledge/units/terms/lian-zi.md",
    "L3836 记帘子为房门口或室内悬挂的丝织或竹编垂具，有曲隐遮蔽与安全回避的作用；同段原文重复错乱，“垂帘听政”误作“垂帝听政”且句子重出，只能引用未错乱的分句。",
    "新建 terms/lian-zi.md：sub_type furnishing，primary_dimension B，confidence low。只写材质、位置与两项功能。",
    "六节齐全；必须写明原文此段有重复与脱字、照录标疑、不据以补写；不得把“垂帘听政”复原为完整引文。",
    "canonical 为新建术语条；相邻陈设见 terms/ping-feng.md、terms/weizhang.md、terms/cheng-chen.md。")

add("cand-06-18", "琵琶", "create", "04-knowledge/units/terms/pi-pa.md",
    "L3850 记琵琶在秦汉曾是弹拨乐器总称，并引刘熙《释名》“枇杷，本出于胡中，马上所鼓也。推手前曰枇，引手却曰枇杷，像其鼓时，因以为名也”（末句疑衍“杷”字）；L3852 记“琵是手向前弹，琶是手向后弹”，句末被三张图注隔断；L3862 记乌孙公主传说与汉琵琶“中虚外实、盘圆柄直，有四弦、十二柱”，后也称阮咸；L3864 记曲项琵琶、五弦琵琶4世纪经印度传入西北，并见于北魏敦煌壁画。",
    "新建 terms/pi-pa.md：sub_type musical_instrument，primary_dimension B，secondary E。写总称与得名、汉琵琶传说、曲项与五弦三组。",
    "六节齐全；《释名》引文末“枇杷”照录标疑为衍字；L3852 与 L3862 跨图注断句分段引；“传说”保留；不补唐代琵琶与演奏技法。",
    "canonical 为新建术语条；近缘见 terms/ruan-xian.md，文献见 publications/shiming.md，图像见 places/dunhuang-mogao-ku.md。")

add("cand-06-19", "阮咸", "create", "04-knowledge/units/terms/ruan-xian.md",
    "L3862 记汉琵琶“此名为‘汉琵琶’，后也称‘阮咸’”；L3710 图 5-32 题为“竹林七贤《阮咸》”，所指为人物，与乐器同名。来源未说明乐器何以得名。",
    "新建 terms/ruan-xian.md：sub_type musical_instrument，primary_dimension B。写汉琵琶别名一层，并说明与人物同名而来源未言命名缘由。",
    "六节齐全；不得据人物图注补乐器形制；不补“阮咸善弹此器故称”之类因果；图版未核。",
    "canonical 为新建术语条；母题见 terms/pi-pa.md，人物见 terms/zhu-lin-qi-xian.md。")

add("cand-06-23", "筚篥", "create", "04-knowledge/units/terms/bi-li.md",
    "L3872 将筚篥列入魏晋新见乐器；L3893 小标题段首原文作“算篥”，记其为木制管子、九孔、上有芦哨、与笳近似，原为龟兹乐器、南北朝传入中原，并分大、小、竖小、桃皮、双筚篥五种形式。同段后文自用“筚篥”正字。",
    "新建 terms/bi-li.md：sub_type musical_instrument，primary_dimension B，secondary E。写形制、来源与五种形式三层。",
    "六节齐全；“算篥”照录标疑为「筚篥」，并以同段正字为内证；不补西域乐部与唐代筚篥名家。",
    "canonical 为新建术语条；近缘见 terms/hu-jia.md，乐种见 terms/xi-liang-yue.md。")

add("cand-06-102", "笛", "create", "04-knowledge/units/terms/di.md",
    "L3866 记汉时笛为横吹乐器，原本在张骞出使西域带回吹笛经验的基础上重新研制；记笛与羌笛的区别在横吹与竖吹；并记荀勖于公元274年制成12支高音笛、完善乐律要求，其笛未流传而制笛原理水平很高。",
    "新建 terms/di.md：sub_type musical_instrument，primary_dimension B。写横吹、与羌笛的分辨、荀勖十二笛三点。",
    "六节齐全；不补笛的孔数与开孔法；荀勖事只照录。",
    "canonical 为新建术语条；对照见 terms/qiang-di.md，同类见 terms/kong-hou.md。")

add("cand-06-103", "羌笛", "create", "04-knowledge/units/terms/qiang-di.md",
    "L3850 将羌笛列入秦汉乐器；L3866 记“羌笛是甘肃、四川一带的羌族乐器，是后来箫的雏形。笛和羌笛的区别是横吹和竖吹”。",
    "新建 terms/qiang-di.md：sub_type musical_instrument，primary_dimension B，confidence low。只写族属地域、与箫的关系、横竖吹之别三点。",
    "六节齐全；“箫的雏形”写为来源判断；不补羌笛形制与诗词典故。",
    "canonical 为新建术语条；对照见 terms/di.md，同类见 terms/hu-jia.md。")

add("cand-06-104", "胡笳", "create", "04-knowledge/units/terms/hu-jia.md",
    "L3868 小标题“胡笳”下记秦汉笳几乎失传、记载中的“芦笳”以芦叶卷起吹奏，后把芦苇制成哨装到管子上称为胡笳；同段并记角由天然动物角改为竹、木、皮、铜加工。",
    "新建 terms/hu-jia.md：sub_type musical_instrument，primary_dimension B。分「笳与胡笳」「角」两小节，不把角混入标题义。",
    "六节齐全；不补《胡笳十八拍》等来源外内容；两种乐器分列。",
    "canonical 为新建术语条；近缘见 terms/bi-li.md、terms/qiang-di.md。")

add("cand-06-105", "箜篌", "create", "04-knowledge/units/terms/kong-hou.md",
    "L3850 将箜篌列入秦汉乐器；L3870 记汉代箜篌最初横弹、为“卧箜篌”亦称箜篌瑟，竖箜篌大约公元2世纪从朝鲜传到中原，汉乐府《箜篌引》叙述有关箜篌的故事；L3872 记魏晋乐器群中仍有卧箜篌。",
    "新建 terms/kong-hou.md：sub_type musical_instrument，primary_dimension B。写卧箜篌与竖箜篌两类、传来说与文献例证三层。",
    "六节齐全；“从朝鲜传到中原”照录，不改为西域；不补弦数、音箱形制与图像。",
    "canonical 为新建术语条；同类见 terms/pi-pa.md、terms/di.md。")

add("cand-06-22", "西凉乐", "create", "04-knowledge/units/terms/xi-liang-yue.md",
    "L3885 引《隋书·音乐志》记外来乐器多来自西凉、龟兹、天竺、康国、安国、疏勒、高丽等国；L3887 记西凉为十六国之一、在酒泉敦煌一带立国，西凉乐指凉州音乐、凉州即今甘肃武威，是在吸收龟兹音乐基础上加以改变并融入部分中原古乐；L3889 另记龟兹、天竺、康国、安国、疏勒、高丽的地理。",
    "新建 terms/xi-liang-yue.md：sub_type music_genre，primary_dimension B，secondary E。写政区背景、乐种定义与构成来源三层。",
    "六节齐全；只写西凉乐，不把龟兹乐并入；地名沿革照来源；不补乐部制度与曲目。",
    "canonical 为新建术语条；乐器见 terms/pi-pa.md、terms/bi-li.md，地域见 places/dunhuang-mogao-ku.md。")

add("cand-06-24", "羯鼓", "create", "04-knowledge/units/terms/jie-gu.md",
    "L3872 将羯鼓列入魏晋新见并广为流行的乐器；L3910 记“羯鼓，南北朝时期从西域传入中原的打击乐器。如桶置于架上，以两杖击之”。",
    "新建 terms/jie-gu.md：sub_type musical_instrument，primary_dimension B，confidence low。写传入侵入期、桶形置架与两杖击奏三点。",
    "六节齐全；不补唐玄宗羯鼓事与曲名。",
    "canonical 为新建术语条；乐种见 terms/xi-liang-yue.md，图像见 places/dunhuang-mogao-ku.md。")

add("cand-06-32", "中心塔柱式", "create", "04-knowledge/units/terms/zhong-xin-ta-zhu-shi.md",
    "L3968 记北朝洞窟结构为中心塔柱式：主室后部建中心塔柱、四周开佛龛，主室前部凿人字披屋顶式供僧人居住，窟壁绘千佛故称千佛洞；L3970 记其与印度支提窟的渊源，支提窟为窟内一圆塔而塔顶与窟顶分离，北朝中心柱窟吸收斗拱、枋子、椽子等中原木构特点并出现方形塔意味。",
    "新建 terms/zhong-xin-ta-zhu-shi.md：sub_type cave_form，primary_dimension B。写结构描述、支提窟对比、中原化三点。",
    "六节齐全；“中心塔柱式”与“中心柱窟”作同义并用；不补云冈、巩义实例排比（可引 L3998 云冈一句）；不补窟数统计。",
    "canonical 为新建术语条；窟群见 places/dunhuang-mogao-ku.md、places/yungang-shiku.md，塔制见 terms/fota.md。")

# ---------------- update ----------------
add("cand-06-06", "榻", "update", "04-knowledge/units/terms/han-ta.md",
    "L3747-L3751 补出床榻分工的由来（长八尺为床、长三尺五寸的“榻版”为坐具亦称枰）、榻也称小床且可合坐可独坐、独坐称独榻以示礼敬、《世说新语》独榻与连榻两事、河南郸城西汉晚期墓石质坐榻为已知最早、南京大学校园东晋墓陶榻长125宽65高28厘米为魏晋小榻样式。既有条目只记高丰的汉代榻，缺魏晋一段。",
    "更新 terms/han-ta.md：title 由“汉榻”扩为“榻”，aliases 增汉榻、独榻、小床；新增赵农来源条，source_count 1→2，version 1→2；保留高丰原有全部内容，只增第五节与相应字段。",
    "新增「五、魏晋南北朝的榻与独榻、连榻」；跨书新增 source 条；层级说明与验证状态同步改为两册；图 5-38 北周石榻图版未核，不据图补写。",
    "canonical 为 terms/han-ta.md；与 terms/ping-furniture.md（枰）、terms/ji-furniture.md（凭几）分工，不合并。")

add("cand-06-97", "案（几案）", "update", "04-knowledge/units/terms/an-furniture.md",
    "L3783-L3802 补南北朝大案与带足案的普遍、长案与圆案之分、书案／奏案／食案／香案四类用途、几案混称与《魏书·邢昕传》“兼长几案”、书案《南史·江秉之传》、奏案《三国志·周瑜传》、食案“举案齐眉”与多子盒、香案置庙堂、漆与陶瓷两类材质。既有条目已收高丰、夏燕靖与赵农 L2301，缺魏晋功能分化一段。",
    "更新 terms/an-furniture.md：aliases 增奏案、香案、几案；赵农来源条由 L2301 扩为 L2301, L3783-L3800，同书多跨度不增 source_count；version 2→3；保留原有全部内容。",
    "新增「南北朝大案与功能分化」诸条；跨页与跨图注断句分别引；尺寸未载处如实保留；图版未核。",
    "canonical 为 terms/an-furniture.md；与 terms/ji-furniture.md（几）互见而不合并，与 terms/duozi-he.md（多子盒）分工。")

add("cand-06-29", "浮图", "update", "04-knowledge/units/terms/fota.md",
    "L3940-L3942 补出佛塔原称浮图、为梵文音译，古印度原型为自下而上的半球体覆钵，覆钵之上有平头与伞盖形成刹、以中心柱贯通象征宇宙之柱，后受希腊文化影响出现方形与矩形基座；东汉末中原已有浮屠寺，佛塔成为佛的化身与象征，并与中国建筑结合出密檐式、楼阁式、亭阁式、金刚宝座式、喇嘛塔五式与木、砖、砖木、砖石四类材料。既有条目只有夏燕靖一册。另 L3936 嵩岳寺塔作高39.5米，与 2016 册 41 米不一致。",
    "更新 terms/fota.md：aliases 增浮图、浮屠；新增赵农来源条（L3936、L3940-L3942），source_count 1→2，version 1→2；保留 2016 册全部内容，新增「赵农 2009 册所述语源与形制层次」一节，并在验证状态记录两源高度不一致。",
    "跨源高度冲突并列保留、不作取舍；覆钵—平头—伞盖—刹的层次照录；佛塔样式与材料分类照录；图版未核。",
    "canonical 为 terms/fota.md；塔实例见 works/songyue-si-ta-523.md，窟形见 terms/zhong-xin-ta-zhu-shi.md。")

add("cand-06-112", "南北响堂山石窟", "update", "04-knowledge/units/places/xiangtangshan-shiku.md",
    "L4069 将“河北南北响堂山石窟”列入丝路以外的重要石窟；L4073 记其在河北峰峰市、属北齐时期开凿，因位于北齐故都安阳附近山峦而得名，自北齐开窟后隋唐宋明不断增补。既有条目只有夏燕靖 2016 的一条图注，缺地点、朝代与沿革。",
    "更新 places/xiangtangshan-shiku.md：新增赵农来源条（L4069、L4073），source_count 1→2，version 1→2，confidence low→medium；改写描述与核心内容，删去“只到朝代、未给北齐”的旧判断。",
    "补地点（河北峰峰）、北齐开窟、得名缘由、隋唐宋明增补、石窟名单位置；记录“邯郸／河北峰峰市”两册用字不一致；窟名、窟数、造像仍写未载。",
    "canonical 为 places/xiangtangshan-shiku.md；同谱系见 places/longmen-grottoes.md、places/yungang-shiku.md。")

# ---------------- no_delta ----------------
add("cand-06-17", "步障", "no_delta", "04-knowledge/units/terms/ping-feng.md",
    "L3834 记步障多以室外布置为主、临时使用、以竹木漆竿插地将丝织物围挂遮蔽，并引《世说新语·汰侈》石崇与王恺斗富“君夫作紫丝布步障碧绫裹四十里，石崇作锦步障五十里以敌之”。既有 terms/ping-feng.md 第五节已完整覆盖步障，含同一引文。",
    "判 no_delta：不新建步障独立条，也不改动 ping-feng.md；步障在来源中始终作为屏风的近缘物出现，独立成条会与既有第五节重复。",
    "不写回；仅在 canonical-mapping 记录并入位置。",
    "canonical 为 terms/ping-feng.md 第五节；若日后要独立，须先把该节迁出，避免双记。")

add("cand-05-95", "金墉城", "no_delta", "04-knowledge/units/places/luoyang.md",
    "L3648 记魏晋重修洛阳时在西北隅修建城中城金墉城，由南北相连的三座小城以城门通连、犹如堡垒、高大坚固，形成防卫制高点，北朝时期一直是军事重地。既有 places/luoyang.md 已含金墉城全部要点与同一叙述。",
    "判 no_delta：金墉城在来源中是洛阳城防体系的一环，材料不足以独立成 place 条；既有洛阳条已完整承载。",
    "不写回；记录并入位置。",
    "canonical 为 places/luoyang.md；如后续获得金墉城独立材料，再评估拆分。")

add("cand-06-40", "古阳洞", "no_delta", "04-knowledge/units/places/longmen-grottoes.md",
    "L4023 记北魏宗室比丘慧成从公元495年开始开凿龙门石窟即古阳洞，呈窑洞形式、周壁数百中小型佛龛、以造像题记著称、保存《龙门二十品》中的十九品。既有 places/longmen-grottoes.md 已含慧成、495年与十九品全部要点。",
    "判 no_delta：古阳洞作为龙门石窟的洞窟单元，既有龙门条已完整记录；单独拆条会与窟群条重复且缺独立材料。",
    "不写回；记录并入位置。",
    "canonical 为 places/longmen-grottoes.md。")

add("cand-06-41", "宾阳洞", "no_delta", "04-knowledge/units/places/longmen-grottoes.md",
    "L4023-L4028 引《魏书·释老志》景明初诏白整准代京灵岩寺石窟于洛南伊阙山为高祖、文昭皇太后营石窟二所，永平中刘腾奏为世宗复造一所、凡为三所，自景明元年至正光四年六月用功八十万二千三百六十六。既有 places/longmen-grottoes.md 已含该长引文与景明元年（500）系年。",
    "判 no_delta：宾阳洞材料已完整落在龙门石窟条内；本批另建 works/di-hou-li-fu-tu.md 承载洞内浮雕，不重复建洞窟条。",
    "不写回；记录并入位置。",
    "canonical 为 places/longmen-grottoes.md；浮雕见 works/di-hou-li-fo-tu.md。")

add("cand-05-100", "铜雀台", "no_delta", "04-knowledge/units/places/yecheng.md",
    "L3695 记曹操在建安十五年修建游乐场所铜雀台，聚集建安七子（孔融、王粲、刘祯、阮瑀、徐幹、陈琳、应玚）与三曹父子唱和，把政治斗争演义成艺术生活。既有 places/yecheng.md 已含铜雀台、建安七子与三曹全部要点。",
    "判 no_delta：铜雀台是邺城宫苑的构成部分，既有邺城条已完整承载；来源未给台体尺度与形制，不足以独立成 work 条。",
    "不写回；记录并入位置。",
    "canonical 为 places/yecheng.md。")

# ---------------- rejected ----------------
add("cand-06-03", "《兰亭集序》（文献义）", "rejected", "04-knowledge/units/works/lan-ting-ji-xu.md",
    "L3717 与 L4087 引《兰亭集序》文句，L3289 亦以之为士人心声的例证；但同一文本已由 cand-05-73 以书法作品身份建为 works/lan-ting-ji-xu.md，本条候选的 publication 归类与之重复。",
    "判 rejected：同一实体不建第二类型条目。《兰亭集序》在本库按法书作品立条，文献引用面并入该条；canonical 取 cand-05-73。",
    "不新建 publication 条；两处引文已在 works/lan-ting-ji-xu.md 内承载。",
    "canonical 为 works/lan-ting-ji-xu.md（cand-05-73）；本条为重复归类，不入库。")

add("cand-06-04", "玄学", "rejected", "04-knowledge/units/terms/xuanxue.md",
    "L3726 记魏晋玄学崇尚自然、完善个人生命的觉醒，为园林繁盛的文化因素；与 cand-05-39 的“魏晋玄学”（L3271、L3273）为同一概念的两处叙述，分列会造成同一术语双条。",
    "判 rejected：合并到 cand-05-39 所建 terms/xuanxue.md，本条不单独建条。",
    "不新建条；L3726 的园林语境作为该条的一处引文来源，已在建条时纳入。",
    "canonical 为 terms/xuanxue.md（cand-05-39）。")

# ---------------- emit ----------------
rows = json.load(io.open(ROOT / "_zn_ch5_rows.json", encoding="utf-8"))
by_suffix = {}
for r in rows:
    cid = r["candidate_id"]
    by_suffix[cid.split(":")[1]] = cid

decisions = []
missing = []
for suffix in sorted(T):
    if suffix not in by_suffix:
        missing.append(suffix)
        continue
    d = T[suffix]
    decisions.append({
        "cid": by_suffix[suffix],
        "entity": d["entity"],
        "action": d["action"],
        "target": d["target"],
        "analysis": d["analysis"],
        "approve": d["approve"],
        "apply_note": d["apply_note"],
        "note": d["note"],
    })

not_covered = sorted(set(by_suffix) - set(T))
out = {
    "doc": DOC,
    "file": SRC,
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "同书多跨度更新：sources 单条 citation 内逗号分隔，source_count 不增，version 加 1",
        "跨册更新：新增 source 条，source_count 加 1，version 加 1，review_due 延至 2027-04-26",
        "逐字引文用“ ”，校正与拼接用「 」，正文禁 ASCII 双引号",
        "原文疑误照录标疑，不径改",
        "重复实体只保留一个 canonical，另一候选判 rejected",
        "已完整覆盖的候选判 no_delta，不改写既有条目",
    ],
    "decisions": decisions,
    "notes": "赵农 2009 册第五章 unit 候选 88 条：create 77、update 4、no_delta 5、rejected 2。",
}
(ROOT / "_zn_decisions_ch5.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("decisions:", len(decisions), "missing:", missing, "not_covered:", not_covered)
from collections import Counter
print(Counter(d["action"] for d in decisions))
