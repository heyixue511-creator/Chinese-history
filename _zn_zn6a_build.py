# -*- coding: utf-8 -*-
"""Build 赵农 2009 第六章 claim rows (54 new claims, no merges)."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "第六章 繁盛的浮华——隋唐时期的设计"

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
    "claim-0553", "cand-06-58", "historiographic_claim",
    "赵农认为，隋唐时期是从公元581年至公元907年，共326年；这是中国古代社会发展中的巅峰阶段。",
    "Zhao Nong holds that the Sui-Tang period runs from 581 to 907 CE, 326 years in all, and is the peak stage of ancient Chinese social development.",
    [],
    "断言语义取 L4112。起讫年与326年为原文直述，未给历法换算与纪年依据；巅峰阶段为作者的总评价。库内无隋唐分期术语条目，未强行链接。",
    4110, 4173, [4112], ["b0168"], "第一节 绪论"))

rows.append(C(
    "claim-0554", "cand-06-59", "evaluative_claim",
    "赵农认为，唐朝是一个有着丰富物质生活而无甚深刻思想、有着严密宗教而无系统哲学的时代；儒、道、释并行而佛教尤为盛行，因此唐朝的政治是在用与无用之间。",
    "Zhao Nong characterises the Tang as an age rich in material life but without deep thought, with an elaborate religion but no systematic philosophy; Confucianism, Daoism and Buddhism coexisted with Buddhism especially prevalent, so Tang politics stood between the useful and the useless.",
    [],
    "断言语义取 L4134 与 L4136，原文被版面断为两行。丰富物质/无深刻思想、严密宗教/无系统哲学为作者的评价性对举，未给思想史与制度史论证。库内无适龄条目，未强行链接。",
    4110, 4173, [4134, 4136], ["b0168"], "第一节 绪论"))

rows.append(C(
    "claim-0555", "cand-06-68", "interpretive_claim",
    "赵农认为，巨型的建筑物往往多是出于政治家的需要而修建，而不在于是否具有实用的意义。",
    "Zhao Nong holds that monumental buildings were usually erected to meet the needs of statesmen rather than for practical utility.",
    [P + "luoyang-cheng.md", R + "wu-zetian.md"],
    "断言语义取 L4230，由洛阳明堂个案上升为一般判断。明堂为武则天所建，原文记其高294尺、后造天堂、改通天宫，并称唐玄宗拆去上层改建乾元殿；明堂本身库内无条目，故链接隋唐洛阳城与武则天。实用意义的判断未给建筑功能分析。",
    4207, 4231, [4230], ["b0171"], "第二节 城市与建筑"))

rows.append(C(
    "claim-0556", "cand-06-75", "historiographic_claim",
    "赵农认为，赵州桥设计精巧、选址合理、桥基牢固，历经千余年自然洗礼依然结实，是世界上最早的石拱桥。",
    "Zhao Nong holds that the Zhaozhou Bridge, ingeniously designed, well sited and firmly founded, remains sound after more than a millennium and is the world's earliest stone arch bridge.",
    [W + "zhaozhou-qiao-595-605.md", R + "li-chun.md"],
    "断言语义取 L4264。原文自身先述汉代已有拱桥、并引《水经注》282年洛阳旅人桥，再以赵州桥为最早石拱桥，形成内部张力；与夏燕靖 claim-0330（现存最早双曲石拱桥、敞肩拱首创）为跨作者近邻，后者措辞较窄，未合并。见 works/zhaozhou-qiao-595-605、persons/li-chun。",
    4247, 4276, [4264], ["b0173"], "第二节 城市与建筑"))

rows.append(C(
    "claim-0557", "cand-06-82", "evaluative_claim",
    "赵农评价，就外观而言，大雁塔笔直挺拔、巍峨雄浑，而小雁塔端庄秀丽、丰润优雅；坚挺与柔和，是对大唐风韵的绝妙诠释。",
    "Zhao Nong judges that in appearance the Giant Wild Goose Pagoda is upright and majestic while the Small Wild Goose Pagoda is graceful and elegant; firmness and softness together interpret the Tang manner.",
    [W + "dayan-ta-652.md", W + "xiaoyan-ta.md"],
    "断言语义取 L4297。原文并记大雁塔现存7层、高64米，小雁塔原15层、明代地震后存13层；外观对举为作者审美评价，未给比例与轮廓测量。见 works/dayan-ta-652、works/xiaoyan-ta。",
    4277, 4314, [4297], ["b0174"], "第二节 城市与建筑"))

rows.append(C(
    "claim-0558", "cand-06-88", "synthetic_claim",
    "赵农认为，石经的经典意义使抄录成为迫切而细致的工作，造纸水平提高与纸张应用使拓本技术的出现成为可能，为印刷术的产生提供了必要条件；印章从封泥演变为蘸印泥钤印于纸上，是印刷术的雏形；汉代画像石、画像砖与魏晋墓志铭等形式也起到推动作用。",
    "Zhao Nong argues that the canonical status of stone classics made copying urgent and meticulous, and that improved papermaking and the spread of paper made rubbings possible, providing a necessary condition for printing; seals evolving from clay-seal impressions to ink-stamped paper were the prototype of printing; Han pictorial stones and tiles and Wei-Jin epitaphs also contributed.",
    [T + "shijing.md", W + "xiping-shijing.md", W + "zhengshi-shijing.md", W + "kaicheng-shijing.md",
     PR + "zaozhishu.md", PR + "diaoban-yinshua.md"],
    "断言语义取 L4354、L4356 与 L4358。石经经典意义—抄录—拓本—印刷为作者归纳的技术谱系，未给拓本实物序列与印章钤印的年代上限；《熹平石经》《正始石经》《开成石经》见三件单独条目。",
    4317, 4361, [4354, 4356, 4358], ["b0176"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0559", "cand-06-94", "historiographic_claim",
    "赵农认为，雕版印刷术的出现与文字书写规范化有很大关系；从书法角度看楷书的艺术趣味削弱了，但从文字设计角度看楷书容易推广流行，因为雕版对文字有规范要求；唐太宗令大臣摹写《兰亭集序》，除个人艺术趣味外也有文化规范与统一国度文化政策的需要。",
    "Zhao Nong holds that the rise of woodblock printing was closely tied to the standardisation of writing: regular script lost some artistic interest but was easy to disseminate as lettering design because carving demanded standard forms; Emperor Taizong's order that ministers copy the Lantingji Xu served cultural standardisation and a unified realm's cultural policy as well as personal taste.",
    [T + "kai-shu.md", R + "wang-xi-zhi.md", W + "lan-ting-ji-xu.md"],
    "断言语义取 L4364 与 L4368，并以 L4366 唐太宗摹兰亭为佐证。楷书艺术趣味与推广效率的对举、摹兰亭的文化政策解释均为作者判断；与 claim-0560 同段近邻（后者在 L4366 评唐以后楷书质量），前者论唐初规范与印刷适应，后者论艺术质量，未合并。",
    4362, 4401, [4364, 4368], ["b0177"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0560", "cand-06-124", "evaluative_claim",
    "赵农认为，唐以后的楷书似乎缺乏魏晋书体的内在质量；由于文字不断被规范以适应书写技术的操作，因而缺乏了魏晋时期楷书草创期的散漫自由的天性。",
    "Zhao Nong suggests that post-Tang regular script seems to lack the inner quality of Wei-Jin calligraphy: as writing was continually standardised to suit technique, it lost the free, unconstrained temperament of regular script's formative Wei-Jin stage.",
    [T + "kai-shu.md"],
    "断言语义取 L4366。原文用“似乎”限定，属作者的审美判断；规范化与天性丧失的因果为作者解释，未给书迹样本比较。与 claim-0559 同段，未合并。",
    4366, 4366, [4366], ["b0177"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0561", "cand-07-07", "interpretive_claim",
    "赵农认为，任何有意义的设计活动都必须有引发的契机；对雕版印刷术而言，唐代佛教文化盛行、借印刷弘扬佛法是早期印刷术发展的主要契机，因此世界上现存最早的一批印刷品几乎都是佛经。",
    "Zhao Nong holds that every meaningful design activity needs a triggering occasion: for woodblock printing, the prevalence of Tang Buddhism and the wish to propagate the faith through printing was the main occasion for its early development, so nearly all the world's earliest surviving printed matter consists of Buddhist sutras.",
    [PR + "diaoban-yinshua.md", B + "jingangjing-868.md", E + "fojiao-chuanru-zhongguo.md"],
    "断言语义取 L4421。韩国佛国寺《无垢净光大陀罗尼经》、成都唐墓《陀罗尼经咒》与吐鲁番《妙法莲花经》为原文所举早期印刷品；佛国寺本断代依赖武周新字，学界仍有争议，原文“发现最早”说未给独立断代报告。见 procedures/diaoban-yinshua、publications/jingangjing-868。",
    4402, 4432, [4421], ["b0178"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0562", "cand-07-08", "interpretive_claim",
    "赵农认为，唐代中后期书写、绘制、刻工、纸张、墨色以及阴刻阳刻、反字刻制等雕版技术实施条件都已具备，众多刻工在长期印章镌刻中已训练得心应手。",
    "Zhao Nong holds that by the mid-to-late Tang the conditions for woodblock printing were all in place: writing, drawing, carving, paper and ink, together with intaglio and relief carving and reversed-character cutting, while many carvers had been trained by long practice in seal engraving.",
    [PR + "diaoban-yinshua.md", PR + "zaozhishu.md"],
    "断言语义取 L4419。条件清单为原文列举；雕版与印章镌刻的技术关联为作者解释，未给刻工名录或作坊遗址。见 procedures/diaoban-yinshua、procedures/zaozhishu。",
    4402, 4432, [4419], ["b0178"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0563", "cand-07-16", "historiographic_claim",
    "赵农认为，虽然无法保存最早的雕版印刷品，但雕版印刷术最早出现应在隋唐之间，唐代中后期才广为流行。",
    "Zhao Nong holds that although the earliest woodblock prints cannot be preserved, woodblock printing most likely emerged between the Sui and Tang and only became widespread in the mid-to-late Tang.",
    [PR + "diaoban-yinshua.md"],
    "断言语义取 L4435。“隋唐之间”为作者的推断，未给实物断代或文献上限；与夏燕靖 claim-0181（宋版书成熟）分属不同技术阶段，未合并。",
    4433, 4476, [4435], ["b0179"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0564", "cand-07-17", "interpretive_claim",
    "赵农认为，旋风装与龙鳞装并非两种不同样式，而应是一物两名；故宫博物院藏唐抄本《王仁昫刊谬补缺切韵》是典型的旋风装。",
    "Zhao Nong holds that whirlwind binding and dragon-scale binding are not two distinct formats but two names for one thing; the Tang manuscript copy of Wang Renxu's Kanmiu Buque Qieyun in the Palace Museum is a typical whirlwind binding.",
    [T + "xuanfeng-zhuang.md"],
    "断言语义取 L4469。原文明言前人曾认为是两种样式，作者判定为一物两名；未给两种装帧的形制比较图与实物清单。故宫藏本书名原文作《王仁昫刊谬补缺切韵》。龙鳞装库内无独立条目。",
    4433, 4476, [4469], ["b0179"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0565", "cand-07-18", "historiographic_claim",
    "赵农认为，任何一种书籍装帧设计都是在前人经验基础上的延续，但没有单一形式的继承，而是在综合融会中不断发展；书籍装帧形式导致后来雕版印刷技术的提高，并进一步促使活字印刷术出现。",
    "Zhao Nong holds that every book-binding design continues earlier experience, yet no single form is inherited as such: binding developed through synthesis, and binding formats in turn drove improvements in woodblock printing and helped bring about movable-type printing.",
    [T + "jingzhe-zhuang.md", T + "xuanfeng-zhuang.md", PR + "diaoban-yinshua.md", PR + "huozi-yinshua.md"],
    "断言语义取 L4471。综合融会与装帧—雕版—活字的因果链为作者判断，未给装帧实物编年与技术传递环节。见 terms/jingzhe-zhuang、terms/xuanfeng-zhuang、procedures/diaoban-yinshua、procedures/huozi-yinshua。",
    4433, 4476, [4471], ["b0179"], "第三节 印刷与书籍"))

rows.append(C(
    "claim-0566", "cand-07-22", "evaluative_claim",
    "赵农评价，曲辕犁是传统犁农具发展中的重大突破，改变犁辕、犁箭、犁梢、犁底模式，使犁架变小、操作简便、深浅自如，为中国农业精耕细作提供工具保证，也奠定后来犁具的基础。",
    "Zhao Nong judges the curved-shaft plough a major breakthrough in traditional ploughing implements: by reworking the shaft, strut, handle and sole it made the frame smaller, easier to operate and adjustable in depth, guaranteed tools for intensive farming and laid the basis for later ploughs.",
    [T + "quyuan-li.md"],
    "断言语义取 L4481。原文并称曲辕犁又称江东犁，将汉代直长辕与二牛抬杠改为一牛耕犁；“重大突破”“奠定后来犁具基础”为作者评价，未给犁具实测与农耕效率数据。",
    4479, 4494, [4481], ["b0181"], "第四节 农具与家具"))

rows.append(C(
    "claim-0567", "cand-07-23", "factual_claim",
    "赵农指出，《耒耜经》作者陆龟蒙（？—约881年）为唐代姑苏诗人，与皮日休并称皮陆；《耒耜经》是中国最早记载和研究农具的书籍，其中记录爬（耙）、砺、夯等农具。",
    "Zhao Nong notes that the Leisi Jing was written by Lu Guimeng (d. c. 881), a Tang poet from Gusu who was paired with Pi Rixiu; it is China's earliest book recording and studying farming implements, including the harrow, roller and tamping tools.",
    [B + "leisi-jing.md", T + "leisi.md"],
    "断言语义取 L4493。候选原类型 bibliographic_fact 按语义映射为 factual_claim；作者生卒与“皮陆”并称见原文；“最早记载和研究农具的书籍”为作者判断，未给书目学比较。见 publications/leisi-jing、terms/leisi。",
    4479, 4494, [4493], ["b0181"], "第四节 农具与家具"))

rows.append(C(
    "claim-0568", "cand-07-30", "historiographic_claim",
    "赵农认为，椅子的广泛使用改变了中华民族的生活习惯：秦汉时期中原人士还是席地而坐，椅子从西域渐入中原，随佛教文化传播成为生活中不可缺少的家具物品。",
    "Zhao Nong holds that the widespread use of the chair changed Chinese living habits: in the Qin and Han the Central Plains still sat on the floor, and the chair entered from the Western Regions and, with the spread of Buddhism, became an indispensable household item.",
    [T + "yizi.md", T + "huchuang.md"],
    "断言语义取 L4506。椅子先为高僧说法宝座、后转入上流社会与民间的过程见同段；与 claim-0540（胡床为椅子到来作准备）为同册前后章互补，与夏燕靖 claim-0321（胡床推动家具高型化）为跨作者近邻，均未合并。见 terms/yizi、terms/huchuang。",
    4495, 4531, [4506], ["b0182"], "第四节 农具与家具"))

rows.append(C(
    "claim-0569", "cand-07-31", "historiographic_claim",
    "赵农认为，桌、椅、凳、墩在唐代的制形完善，标志着高足家具进入中华民族的社会生活之中，提升了人们的物质水平，也改变着人们的精神文化。",
    "Zhao Nong holds that the maturing of tables, chairs, stools and drum stools in the Tang marks the entry of high-seated furniture into Chinese social life, raising material standards and changing mental culture.",
    [T + "yizi.md", T + "dengdun.md", T + "wu-deng.md", T + "an-furniture.md"],
    "断言语义取 L4526。前文分述绳床、胡床、凳与杌、墩、桌案与屏风；制形完善与物质/精神提升的因果为作者判断。凳墩、杌凳见 terms/dengdun、terms/wu-deng，桌案联称见 terms/an-furniture。",
    4495, 4531, [4526], ["b0182"], "第四节 农具与家具"))

rows.append(C(
    "claim-0570", "cand-07-35", "factual_claim",
    "赵农指出，唐高祖武德四年（621）废五铢钱而铸开元通宝，以一枚为一钱、十枚为一两，废除铢制，改为厘、分、钱、两的十进位计算，钱因而成为固定的重量单位。",
    "Zhao Nong notes that in 621 the Tang court abolished the wuzhu coin and cast the Kaiyuan Tongbao, one coin weighing one qian and ten coins one liang; the zhu system was abolished in favour of the decimal li, fen, qian, liang scheme, making the qian a fixed weight unit.",
    [T + "kaiyuan-tongbao.md"],
    "断言语义取 L4539。武德四年与废五铢、十进位换算为原文直述；未给钱币实测重量与钱范资料。见 terms/kaiyuan-tongbao。",
    4532, 4565, [4539], ["b0183"], "第四节 农具与家具"))

rows.append(C(
    "claim-0571", "cand-07-36", "factual_claim",
    "赵农指出，通宝钱币以朝代年号为文字标志，仍为圆形方孔制，从唐代至清末共流通了1290年。",
    "Zhao Nong notes that tongbao coinage used reign titles as its inscription and retained the round-with-square-hole form, circulating from the Tang to the end of the Qing, 1,290 years in all.",
    [T + "kaiyuan-tongbao.md"],
    "断言语义取 L4541。621—1911 合1290年，与原文一致；通宝钱在各代的年号标识差异未展开。见 terms/kaiyuan-tongbao。",
    4532, 4565, [4541], ["b0183"], "第四节 农具与家具"))

rows.append(C(
    "claim-0572", "cand-07-37", "interpretive_claim",
    "赵农认为，唐代以绢帛作为货币象征，用于赏赐、借贷、药费、稿酬等报酬；以物代币成为一种货币样式，是货币实物化的标志。",
    "Zhao Nong holds that Tang silk cloth served as a monetary symbol for rewards, loans, medical fees and author's fees; payment in goods became a monetary form and marks the materialisation of currency.",
    [],
    "断言语义取 L4550。L4543-L4548 文句被图版与页眉打乱，白居易诗引与“支票的流通方式”残句未纳入语义；绢帛货币与书帖、飞钱并见同节，书帖与飞钱各有专段。库内无绢帛货币条目，未强行链接。",
    4532, 4565, [4550], ["b0183"], "第四节 农具与家具"))

rows.append(C(
    "claim-0573", "cand-07-43", "evaluative_claim",
    "赵农评价，僧一行与梁令瓒改造张衡水运浑象，注水激轮使其自转，并安装自动报时器，成为原始天文钟；它既能表示天象又能记时，是真正意义的机械钟，较早期刻漏先进。",
    "Zhao Nong judges that Yixing and Liang Lingzan's reworking of Zhang Heng's water-driven armillary sphere, with water-driven rotation and an automatic time-reporting device, became a proto-astronomical clock: showing both celestial motion and time, it was a true mechanical clock and more advanced than earlier clepsydras.",
    [T + "hunyi.md", R + "seng-yixing.md"],
    "断言语义取 L4572，引《旧唐书·天文志》“注水激轮，令其自转，一日一夜，天转一周”。机械钟与刻漏先进性的比较为作者评价；梁令瓒库内无独立条目，未强行建链。与夏燕靖 claim-0212（郭守敬简仪）分属不同仪器。",
    4566, 4575, [4572], ["b0184"], "第四节 农具与家具"))

rows.append(C(
    "claim-0574", "cand-07-44", "historiographic_claim",
    "赵农记述，唐代传说工匠韩志和制作过一架飞行器，能飞到100尺高空、飞行距离达450尺，并认为这是中国早期第一次对飞行原理的实践。",
    "Zhao Nong records the Tang legend that the artisan Han Zhihe made a flying device reaching a height of 100 chi and a distance of 450 chi, and regards it as China's first early practice of the principles of flight.",
    [R + "han-zhihe.md"],
    "断言语义取 L4574。原文明确标为“传说”；100尺与450尺未给尺度换算、结构与动力说明，“第一次对飞行原理的实践”为作者判断；同段并记东晋葛洪的飞行器设想，未见实施。见 persons/han-zhihe。",
    4566, 4575, [4574], ["b0184"], "第四节 农具与家具"))

rows.append(C(
    "claim-0575", "cand-07-50", "historiographic_claim",
    "赵农认为，隋唐丝绸生产质量提高与纺织工具改革密切相关；纺织机械的设计制作不仅标志工具技术提高，还标志隋唐时期的国家统一与社会富饶，使人们的生活视野更为广阔、技术更为精湛。",
    "Zhao Nong holds that the improvement of Sui-Tang silk production was closely tied to textile-tool reform; the design and making of textile machinery signalled not only technical advance but also unification and prosperity, broadening horizons and refining skills.",
    [PR + "tihua-jishu.md", T + "tihuaji.md", T + "saoche.md"],
    "断言语义取 L4598。前文分述斜织机、竖织机、花楼式束综提花机与手摇缫车；工具改革—质量提高的关联为作者判断，国家统一与社会富饶为评价性延伸。见 procedures/tihua-jishu、terms/tihuaji、terms/saoche。",
    4578, 4599, [4598], ["b0186"], "第五节 纺织与服饰"))

rows.append(C(
    "claim-0576", "cand-07-51", "factual_claim",
    "赵农指出，唐代纺织技术进步使纬锦和花纱的产量明显提高；南北朝时期纬锦数量不多，纬锦以纬线呈现花纹，比经线受的限制小，可以不断改变花色纹饰。",
    "Zhao Nong notes that Tang textile advances markedly increased the output of weft-faced brocade and figured gauze; weft brocade, rare in the Northern and Southern Dynasties, displays pattern through the weft, which is less constrained than the warp and allows patterns to be changed continuously.",
    [T + "weft-brocade.md", T + "huasha.md"],
    "断言语义取 L4592。纬锦显花原理与南北朝数量对比为原文直述；与夏燕靖 claim-0146（唐锦以纬锦为主并达高水平）近邻，但本条只述技术与产量，未合并。见 terms/weft-brocade、terms/huasha。",
    4578, 4599, [4592], ["b0186"], "第五节 纺织与服饰"))

rows.append(C(
    "claim-0577", "cand-07-55", "factual_claim",
    "赵农指出，隋唐服饰出现法服与常服并存的特点；据《新唐书·车服志》，隋时除帝王外，百官常服同于庶人。",
    "Zhao Nong notes that Sui-Tang dress combined ceremonial and everyday wear; according to the Xin Tangshu, in the Sui all officials below the emperor wore the same everyday dress as commoners.",
    [],
    "断言语义取 L4606。法服/常服并存与百官常服同庶人见《新唐书·车服志》引文；库内无“法服”或“常服”条目，袍衫条目所述为唐代男子常服形制，与本条范围不完全对应，未强行链接。",
    4604, 4621, [4606], ["b0188"], "第五节 纺织与服饰"))

rows.append(C(
    "claim-0578", "cand-07-56", "historiographic_claim",
    "赵农认为，隋唐立国均起于北方，服饰样式深受北方游牧民族影响，形成豪迈通脱的社会风气；唐代女装与女扮男装是其明显表现。",
    "Zhao Nong holds that both Sui and Tang rose from the north, so dress was deeply influenced by northern pastoral peoples and a bold, unrestrained social atmosphere took shape, evident in Tang women's dress and cross-dressing.",
    [T + "hufu.md", T + "huzhuang.md", T + "yuanling-paoshan.md"],
    "断言语义取 L4614。同段并记幞头、圆领袍衫、皮靴与胡装、女扮男装；与夏燕靖 claim-0151（中唐前胡服流行、盛唐后转宽衣）存在时段强弱差异。见 terms/hufu、terms/huzhuang、terms/yuanling-paoshan。",
    4604, 4621, [4614], ["b0188"], "第五节 纺织与服饰"))

rows.append(C(
    "claim-0579", "cand-07-62", "evaluative_claim",
    "赵农评价，乾陵石刻体现了唐代雕刻艺术的最高水平；蹲狮、翼马、鸵鸟等因材施艺、强调整体、减去繁缛、精心刻画。",
    "Zhao Nong judges that the Qianling stone carvings represent the highest level of Tang sculpture: crouching lions, winged horses and ostriches are shaped to the material, emphasising overall mass, paring away ornament and carefully worked.",
    [P + "qianling.md"],
    "断言语义取 L4648。“最高水平”为作者评价，未给雕刻技法与作品比较指标；乾陵现存石刻100余件见 L4640。见 places/qianling。",
    4624, 4651, [4648], ["b0190"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0580", "cand-07-63", "evaluative_claim",
    "赵农评价，昭陵石刻在于洗练而刚健，乾陵石刻却因典雅而华美。",
    "Zhao Nong judges that Zhaoling's carvings are spare and vigorous while Qianling's are refined and ornate.",
    [P + "zhaoling.md", P + "qianling.md"],
    "断言语义取 L4648。风格对举为作者审美评价；昭陵六骏三组形态与现存四座在碑林、两座在美国宾夕法尼亚大学博物馆见 L4646，未据以另立条目。",
    4624, 4651, [4648], ["b0190"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0581", "cand-07-69", "factual_claim",
    "赵农指出，龙门石窟现存的2000多个佛窟和佛龛，绝大多数是唐代开凿的。",
    "Zhao Nong notes that of the more than 2,000 caves and niches surviving at Longmen, the great majority were cut in the Tang.",
    [P + "longmen-grottoes.md"],
    "断言语义取 L4654。2000余窟龛与唐代占多数为原文数字，未给分区统计与断代依据；龙门兴盛与东都地位的关系见同段。见 places/longmen-grottoes。",
    4652, 4675, [4654], ["b0191"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0582", "cand-07-70", "evaluative_claim",
    "赵农评价，奉先寺卢舍那大佛以其宏大饱满的气魄、雍容高贵的形象，召唤着世俗社会的精神向往。",
    "Zhao Nong judges that the Vairocana Buddha of Fengxian Temple, with its grand and full presence and dignified image, summons the spiritual aspirations of the secular world.",
    [P + "longmen-grottoes.md"],
    "断言语义取 L4666。大佛通高约17米、武则天助两万贯脂粉钱、历时13年以上见同段；奉先寺与卢舍那库内无独立条目，链接龙门石窟。召唤世俗向往为作者评价。",
    4652, 4675, [4666], ["b0191"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0583", "cand-07-73", "historiographic_claim",
    "赵农认为，乐山大佛感天地、泣鬼神的建造过程，正是中华民族精神意志的张扬；佛教造像的东渐过程，就是外来文明与中华文化的融合过程。",
    "Zhao Nong holds that the extraordinary construction of the Leshan Giant Buddha was an assertion of Chinese spiritual will, and that the eastward spread of Buddhist images was a process of fusion between foreign civilisation and Chinese culture.",
    [W + "leshan-dafo.md"],
    "断言语义取 L4685。海通和尚舍身开凿、三江汇流与90年工期见同段，其中手抠双目为传说性叙述；精神意志与文明融合为作者评价。见 works/leshan-dafo。",
    4676, 4686, [4685], ["b0192"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0584", "cand-07-77", "historiographic_claim",
    "赵农认为，唐代莫高窟艺术改变了北朝画风苦涩沉重的面貌，将秀骨清像的造型演变为丰满华丽，佛教活动场面充满人间欢乐情趣，使佛教东渐随时间推移融为中原文化的一部分。",
    "Zhao Nong holds that Tang Mogao art changed the bitter, heavy manner of Northern Dynasties painting, turning the slender, clear-featured figure into a full and splendid one, filling Buddhist scenes with worldly joy and making eastward-spreading Buddhism part of Central Plains culture over time.",
    [P + "dunhuang-mogao-ku.md", T + "jingbian.md"],
    "断言语义取 L4701。莫高窟现存492窟中280余窟为唐代开凿见 L4699，为原文数字；北朝苦涩—唐代丰满的风格转变为作者分期判断，与赵农 claim-0545（北朝中心柱窟）为同册前后章互补。经变见 terms/jingbian。",
    4687, 4723, [4701], ["b0193"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0585", "cand-07-78", "historiographic_claim",
    "赵农认为，佛教文化的世俗化引发了社会积极而广泛的反响；文化的多元性和包容性正是一个民族兴旺发达的基石。",
    "Zhao Nong holds that the secularisation of Buddhist culture provoked a positive and wide response in society, and that cultural pluralism and inclusiveness are the cornerstone of a nation's flourishing.",
    [P + "dunhuang-mogao-ku.md", T + "jingbian.md"],
    "断言语义取 L4703。由莫高窟经变个案上升为文明判断，未给社会反响的文献与图像统计；“多元包容为兴旺基石”为作者史观表述。",
    4687, 4723, [4703], ["b0193"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0586", "cand-07-87", "historiographic_claim",
    "赵农认为，隋唐时期国力鼎盛、重视立碑作传，因此隋唐碑刻极多，其碑额高阔、碑身高大、碑座坚实，书法湛精高古、丰姿绰约，均为隋唐一流书法家的杰作，千百年以来为中国书法的传承奠定了基础。",
    "Zhao Nong holds that the Sui-Tang state's strength and its emphasis on steles produced a great many inscriptions with broad tops, tall bodies and solid bases, whose calligraphy by leading masters has underpinned the transmission of Chinese calligraphy for a millennium.",
    [T + "bei-xue.md", W + "fuzi-miaotang-bei.md"],
    "断言语义取 L4726。L4728 把李邕《麓山寺碑》系于开元十八年而注公元703年，与开元十八年（730）不合，属原文纪年错误；本条只取总体判断，不沿用该纪年。虞世南《夫子庙堂碑》见 works/fuzi-miaotang-bei。",
    4724, 4737, [4726], ["b0194"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0587", "cand-07-88", "evaluative_claim",
    "赵农评价，颜真卿书法石刻有《多宝塔》《颜勤礼碑》《麻姑仙坛记》《东方朔画赞》《大唐中兴颂》等，数量众多、结体丰厚、气象磅礴、雄伟壮美，实为唐代书法的最高峰。",
    "Zhao Nong judges that Yan Zhenqing's many stone inscriptions, including the Duobao Pagoda, Yan Qinli, Magu Xiantan, Dongfang Shuo Huazan and Tang Zhongxing Song, are rich in number, generous in structure and grand in spirit, the very peak of Tang calligraphy.",
    [R + "yan-zhenqing.md", R + "liu-gongquan.md"],
    "断言语义取 L4734。“最高峰”为作者评价，未给书迹比较与品评依据；同段并称柳公权《玄秘塔碑》《神策军碑》与颜书并称颜筋柳骨，未另立条目。",
    4724, 4737, [4734], ["b0194"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0588", "cand-07-100", "historiographic_claim",
    "赵农认为，白釉和白瓷的同时出现，标志着中国瓷器进入了一个崭新的阶段；唐代邢窑白瓷胎质细腻、釉色洁白，改变了北朝白瓷泛青黄的釉斑现象。",
    "Zhao Nong holds that the simultaneous appearance of white glaze and white porcelain marked a new stage in Chinese ceramics: Tang Xing ware had fine bodies and pure white glaze, correcting the yellowish-green patches of Northern Dynasties white ware.",
    [T + "baici.md", P + "xing-kiln.md"],
    "断言语义取 L4766，并以 L4768 铁含量小于0.7%的原理说明为背景。与夏燕靖 claim-0116（北齐白瓷划时代）措辞相近而时段不同；与赵农 claim-0534（北朝白瓷为制瓷技术奠基、为彩瓷铺垫）为同册前后章近邻，均未合并。见 terms/baici、places/xing-kiln。",
    4738, 4779, [4766], ["b0195"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0589", "cand-07-101", "factual_claim",
    "赵农指出，唐三彩是一种明器，往往反映墓主人生前的豪华生活，从牛马房仓到神兽动物，展示了唐代丰富多彩的社会生活。",
    "Zhao Nong notes that Tang sancai was a burial ware reflecting the deceased's luxurious life in life, ranging from oxen, horses, houses and granaries to divine beasts, thus displaying the richness of Tang social life.",
    [T + "tang-sancai.md"],
    "断言语义取 L4776。唐三彩胎釉与烧成工艺见 L4774；明器说与“展示社会生活”并置，未给墓葬出土统计与器物组合。与夏燕靖 claim-0327（唐三彩冥器按品级随葬）近邻，未合并。",
    4738, 4779, [4776], ["b0195"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0590", "cand-07-102", "historiographic_claim",
    "赵农认为，唐代长沙窑烧制出釉下彩瓷器，克服瓷土不纯的困难，在瓷胎上绘制纹样后上釉烧制，改变了瓷器单色的状态；长沙窑以其独特创造价值，为瓷器发展开拓新思路，为后世釉下彩技术的完善奠定了基础。",
    "Zhao Nong holds that the Tang Changsha kiln produced underglaze-painted porcelain, overcoming impure clay by painting motifs on the body before glazing and firing, thus ending the monochrome state of ceramics; its originality opened a new path and laid the basis for later underglaze techniques.",
    [T + "blue-and-white-porcelain.md", T + "tang-dai-qingci-yao.md"],
    "断言语义取 L4772。长沙窑库内无独立条目，链接青花瓷（釉下彩主干品种）与唐代著名青瓷窑（含长沙窑）。克服瓷土不纯与“奠定基础”为作者判断，未给胎釉成分检测与窑址产量。",
    4738, 4779, [4772], ["b0195"], "第六节 雕刻与陶瓷"))

rows.append(C(
    "claim-0591", "cand-07-109", "historiographic_claim",
    "赵农认为，何家村镂空银熏球上下两个半圆透雕飞鸟葡萄纹，中心有同心圆机环与轴承环香盂，香盂始终保持平衡；这种设计技艺是对汉代被中香炉的进一步发展。",
    "Zhao Nong holds that the openwork silver incense ball from Hejiacun, with two hemispheres carved with birds and grapes and a central pair of concentric rings carrying a bearing-mounted incense cup that stays level, further develops the Han dynasty 'incense burner in the quilt'.",
    [P + "hejiacun-jiaocang.md", W + "tang-yin-xiangnang.md"],
    "断言语义取 L4792。香盂平衡结构的描述未给剖面图与实测；被中香炉为汉代器物名，库内无独立条目。何家村窖藏见 places/hejiacun-jiaocang，唐代银香囊见 works/tang-yin-xiangnang。",
    4782, 4797, [4792], ["b0197"], "第七节 金银器与铜镜"))

rows.append(C(
    "claim-0592", "cand-07-110", "historiographic_claim",
    "赵农认为，唐代官府对工匠技术的培训和提高，促使了金银器水平的发达，形成了唐代设计文化璀璨绚丽的繁华局面。",
    "Zhao Nong holds that official training and upgrading of artisans' skills drove the high level of Tang gold and silver work and produced the brilliant flourishing of Tang design culture.",
    [P + "hejiacun-jiaocang.md", I + "shaofujian.md"],
    "断言语义取 L4796。前段列举钣金、浇铸、焊接、刻凿、切削、抛光、铆镀等工艺并称借鉴西亚波斯技术；官方培训—金银器发达的因果为作者判断。少府监为官方手工业主管机构。",
    4782, 4797, [4796], ["b0197"], "第七节 金银器与铜镜"))

rows.append(C(
    "claim-0593", "cand-07-114", "historiographic_claim",
    "赵农认为，隋唐时期的铜镜是中国历史上铜镜的繁盛期：铜质饱和、镜体厚重、纹饰精美，除传统圆形、方形外还有菱形、八弧形、海棠花形、亚字形、带柄等样式，纹饰有四神、十二生肖、瑞兽葡萄、瑞兽鸾凤、人物故事等。",
    "Zhao Nong holds that Sui-Tang mirrors mark the flourishing period of Chinese bronze mirrors: saturated metal, heavy bodies and fine ornament, with lobed, octagonal, begonia, 亞-shaped and handled forms alongside round and square ones, decorated with the Four Symbols, zodiac, auspicious beasts and grapes, phoenixes and figural scenes.",
    [T + "tongjing.md", T + "liuchao-tongjing.md"],
    "断言语义取 L4805，形制与纹饰清单见 L4805-L4807。与夏燕靖 claim-0329（唐镜铜锡铅配比与微凸镜面）分论工艺与形制，未合并；六朝铜镜见 terms/liuchao-tongjing。",
    4798, 4878, [4805], ["b0198", "b0199"], "第七节 金银器与铜镜"))

rows.append(C(
    "claim-0594", "cand-07-115", "interpretive_claim",
    "赵农认为，唐太宗以铜为鉴、以古为鉴、以人为鉴的感叹将铜镜与古今得失联系在一起，铜镜的使用不仅是一种实物，还寄托着精神的导向。",
    "Zhao Nong holds that Emperor Taizong's lament on using bronze as a mirror, antiquity as a mirror and people as a mirror linked mirrors to historical judgement, so that mirrors were not merely objects but carried spiritual direction.",
    [T + "tongjing.md"],
    "断言语义取 L4803。引文系于《新唐书·卷九十七》，与通行《旧唐书·魏徵传》出处不一致且文字有节略；千秋节赠镜为传说性叙述，未给宫廷制度依据。见 terms/tongjing。",
    4798, 4878, [4803], ["b0198", "b0199"], "第七节 金银器与铜镜"))

rows.append(C(
    "claim-0595", "cand-07-120", "historiographic_claim",
    "赵农认为，门神是年画的最早样式，是辟邪驱鬼、护卫家园的精神象征。",
    "Zhao Nong holds that door gods are the earliest form of New Year pictures and a spiritual symbol for warding off evil and guarding the home.",
    [T + "menshen.md"],
    "断言语义取 L4818。神荼郁垒、尉迟敬德与秦琼、钟馗等形象谱系见 L4818-L4825，属传说性叙述；“最早样式”为作者判断。见 terms/menshen。",
    4816, 4848, [4818], ["b0199"], "第七节 金银器与铜镜"))

rows.append(C(
    "claim-0596", "cand-07-121", "historiographic_claim",
    "赵农认为，剪纸成为窗户的装饰应在宋元之间；此前剪纸多用于屏风、额颊、面饰与招魂等。",
    "Zhao Nong holds that papercut only became a window decoration around the Song-Yuan period; earlier it was used on screens, foreheads and cheeks, as facial ornament and in soul-summoning.",
    [T + "jianzhi.md"],
    "断言语义取 L4838。吐鲁番唐墓人形剪纸、杜甫“剪纸招我魂”与南北朝镂金剪彩见同段；“宋元之间”为作者的推断，未给窗花实物或文献序列。见 terms/jianzhi。",
    4816, 4848, [4838], ["b0199"], "第七节 金银器与铜镜"))

rows.append(C(
    "claim-0597", "cand-07-122", "factual_claim",
    "赵农指出，唐代出现走马灯，利用灯光产生的热气流推动灯罩内人物马形流转，产生光怪陆离的灯影效果。",
    "Zhao Nong notes that the Tang saw the walk-horse lantern, in which heat from the lamp drives figures of people and horses around inside the shade, producing dazzling moving shadows.",
    [T + "zouma-deng.md"],
    "断言语义取 L4847。唐代说仅此一句，未给文献出处；宋代灯事记载更充分，唐代起源说宜存疑。见 terms/zouma-deng。",
    4816, 4848, [4847], ["b0199"], "第七节 金银器与铜镜"))

rows.append(C(
    "claim-0598", "cand-07-127", "factual_claim",
    "赵农指出，将作监负责大型工程及设备的设计制造，而少府负责日常生活的器具生产；其中少府的染织、将作监的建筑是最繁重的工作。",
    "Zhao Nong notes that the Directorate of Imperial Construction handled large-scale works and equipment while the Court of the Imperial Workshops produced everyday utensils; dyeing and weaving under the latter and construction under the former were the heaviest tasks.",
    [I + "jiangzuojian.md", I + "shaofujian.md"],
    "断言语义取 L4875。前文分述少府五署与将作监四署职掌，并记少府技术官员与工匠19850人、将作监15000人；两组数字为原文所记，未给史料出处比对。见 institutions/jiangzuojian、institutions/shaofujian。",
    4851, 4909, [4875], ["b0201", "b0202"], "第八节 设计行业管理"))

rows.append(C(
    "claim-0599", "cand-07-128", "interpretive_claim",
    "赵农认为，少府和将作监的工作任务虽然各有不同侧重，但都是官方集权垄断的行政管理机构；只有严格的分工管理，才能达到器物制作的精良。",
    "Zhao Nong holds that although the Court of the Imperial Workshops and the Directorate of Imperial Construction had different emphases, both were centralised monopolistic administrative organs; only strict division of labour could achieve fine workmanship.",
    [I + "shaofujian.md", I + "jiangzuojian.md"],
    "断言语义取 L4877。集权垄断与严格分工导致精良为作者判断，未给行政效率或产品质量的比较材料。见 institutions/shaofujian、institutions/jiangzuojian。",
    4851, 4909, [4877], ["b0201", "b0202"], "第八节 设计行业管理"))

rows.append(C(
    "claim-0600", "cand-07-133", "historiographic_claim",
    "赵农认为，官方和民间手工业设计相互促进：民间设计文化为少府、将作监输入大量优秀人才，官方技术的综合优势和信息激励民间设计技术发展，不同地区民间手工业设计技术也有广泛交流。",
    "Zhao Nong holds that official and folk craft design stimulated each other: folk design supplied talented artisans to the central workshops, official technical advantages and information encouraged folk techniques, and techniques circulated widely between regions.",
    [I + "shaofujian.md", I + "jiangzuojian.md", T + "shougongye-hanghui.md"],
    "断言语义取 L4892。白居易“天上取样人间织”、越州妇女学织故事见同段，为官样民间织造的例证；“相互促进”为作者判断。手工业行会见 terms/shougongye-hanghui。",
    4879, 4909, [4892], ["b0202"], "第八节 设计行业管理"))

rows.append(C(
    "claim-0601", "cand-07-134", "factual_claim",
    "赵农指出，唐代私营手工业行业有严格行规，出现行肆、行头、牙人；行肆指店铺，行指同行业，行头为身服徭役的行业领袖，牙人相当于经纪人；隋朝丰都市有100行，唐代西京市有220行。",
    "Zhao Nong notes that Tang private craft trades had strict rules and produced shops, trade guilds, guild heads and brokers; the Sui Fengdu market had 100 trades and the Tang Western Capital market 220.",
    [T + "shougongye-hanghui.md"],
    "断言语义取 L4904。行、肆、行头、牙人的界定见同段；100行与220行为原文数字，未给文献出处与统计口径。见 terms/shougongye-hanghui。",
    4879, 4909, [4904], ["b0202"], "第八节 设计行业管理"))

rows.append(C(
    "claim-0602", "cand-07-135", "historiographic_claim",
    "赵农认为，唐代手工业艺人多依附于自己生产产品的商行，因此对商业市场需求有直面的职业敏感，这对行业之间的技术交流有积极影响。",
    "Zhao Nong holds that Tang artisans mostly attached to the guilds selling their products, and so had a direct professional sensitivity to market demand that positively affected technical exchange between trades.",
    [T + "shougongye-hanghui.md"],
    "断言语义取 L4904。艺人依附商行—市场敏感—技术交流为作者因果解释，未给行规文本或工匠个案。见 terms/shougongye-hanghui。",
    4879, 4909, [4904], ["b0202"], "第八节 设计行业管理"))

rows.append(C(
    "claim-0603", "cand-07-137", "interpretive_claim",
    "赵农认为，大运河是骄奢淫逸的隋炀帝的无意之举，却为后世中国人的生存拓展了真实的地理水利空间。",
    "Zhao Nong holds that the Grand Canal was an unintended act of the extravagant Emperor Yang of Sui, yet it expanded a real geographic and hydraulic space for later Chinese life.",
    [W + "dayunhe.md"],
    "断言语义取 L4912。沟通海河、黄河、淮河、长江、钱塘江五大水系见同段；“无意之举”与“骄奢淫逸”为作者评价，未给开凿动机的史料辨析。见 works/dayunhe。",
    4910, 4931, [4912], ["b0203"], "第九节 结论"))

rows.append(C(
    "claim-0604", "cand-07-138", "historiographic_claim",
    "赵农认为，隋唐的一步步演变，从隋文帝、唐太宗的英武到隋炀帝、唐玄宗的淫逸，从盛到衰、从自满到衰败，就不仅仅是隋唐的故事，而是中华民族的悲痛遭遇的缩影。",
    "Zhao Nong holds that the Sui-Tang trajectory from the vigour of Emperors Wen and Taizong to the extravagance of Yang and Xuanzong, from flourishing to decline, is not merely the Sui-Tang story but an epitome of the Chinese nation's grievous experience.",
    [E + "anshi-zhiluan.md"],
    "断言语义取 L4914。晚唐藩镇、朋党、宦官与缺少纠错机制的叙述见同段；由隋唐个案上升为民族缩影为作者史观表述。与 claim-0606 同段近邻（后者述贞观—开元—安史的人物因果），未合并。见 events/anshi-zhiluan。",
    4910, 4931, [4914], ["b0203"], "第九节 结论"))

rows.append(C(
    "claim-0605", "cand-07-139", "historiographic_claim",
    "赵农认为，隋唐时期的艺术设计史是在中华民族鼎盛时期的背景中完成的；其中产生无数教训和经验，也包含无奈的选择，因而给后来留下许多回味思考的价值。",
    "Zhao Nong holds that the art-design history of the Sui-Tang was completed against the background of the Chinese nation's zenith; it produced countless lessons and experiences, including helpless choices, and so leaves much for later reflection.",
    [],
    "断言语义取 L4930。教训、经验与无奈选择为作者总结性判断，未给设计史案例清单；库内无适龄条目，未强行链接。",
    4910, 4931, [4930], ["b0203"], "第九节 结论"))

rows.append(C(
    "claim-0606", "cand-07-194", "historiographic_claim",
    "赵农认为，贞观之治奠定开元盛世的基础；唐玄宗李隆基昏昏然、群小蚁附、远离贤良，终究酿成安史之乱；政治衰败必然导致人事残破，国家不幸诗家幸，一段悲欢离合的大唐王朝留给诗人反复咏唱。",
    "Zhao Nong holds that the Zhenguan era laid the basis for the Kaiyuan heyday, but the gifted Li Longji grew muddled, surrounded himself with petty men and turned from worthies, finally bringing on the An Lushan rebellion; political decline inevitably brought personal ruin, and in the nation's misfortune the poets found their fortune, leaving the Tang's joys and sorrows to be sung again and again.",
    [E + "anshi-zhiluan.md"],
    "断言语义取 L4922。原文“天下英雄尽入我毂中”之“毂”通行作“彀”；“国家不幸诗家幸”为引语，非赵农自创；与 claim-0604 同段，前者述人物与治乱因果、后者述盛衰缩影，未合并。见 events/anshi-zhiluan。",
    4922, 4922, [4922], ["b0203"], "第九节 结论"))


types = Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({p for r in rows for p in r["supported_by"]})
print(json.dumps({
    "claims": len(rows),
    "first": rows[0]["claim_id"],
    "last": rows[-1]["claim_id"],
    "types": dict(types),
    "links": links,
    "distinct": distinct,
}, ensure_ascii=False, indent=1))

(ROOT / "_zn_zn6a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_zn6a_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")
print("written _zn_zn6a_rows.json / _zn_zn6a_patch.json")
