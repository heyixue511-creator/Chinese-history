# -*- coding: utf-8 -*-
"""Build CL2f claim rows (Xia Yanjing 2009, ch.7 Song-Liao-Jin-Western Xia)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
CH = "宋辽金西夏时期的艺术设计"

ROWS = []


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, section):
    ROWS.append({
        "claim_id": None,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": {
            "doc_id": DOC,
            "source_file": SRC,
            "source_span": {
                "line_start": start,
                "line_end": end,
                "span_kind": kind,
                "key_lines": key_lines,
                "block_ids": block_ids,
                "chapter": CH,
                "section": section,
            },
            "candidate_id": DOC + ":" + cid,
        },
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    })


C("cand-04-80", "historiographic_claim",
  "夏燕靖认为，宋代统治者实行“守内虚外”政策，比较有效地维护了社会的长期稳定，农业、手工业、商业均达到相当高的水平并大大超过唐代，成为我国经济发展史上的又一高峰。",
  "Xia Yanjing argues that the Song policy of guarding the interior while leaving the frontier lightly held maintained long-term social stability comparatively effectively, so that agriculture, handicrafts, and commerce all reached a high level, greatly surpassing the Tang and forming another peak in Chinese economic history.",
  "high",
  ["04-knowledge/units/terms/yeshi.md",
   "04-knowledge/units/terms/washe.md"],
  "候选作 periodization，路由 historiographic；候选跨度 L2444-L2459 含章标题、两幅历史地图、北宋南宋政权更迭与 L2458 的经济高峰判断，断言只取 L2458；同段“中华民族相互交融”与“艺术设计史上不可忽视的重要阶段”留在来源。",
  2458, 2458, "line", [2458], ["b0317"], "章首导论")

C("cand-04-81", "interpretive_claim",
  "夏燕靖认为，北宋手工业生产规模、技术水平与产品数量和质量均胜过前朝，其原因是经济运行方式发生了变革：官营手工业的工匠大部分为招募而来、人身有了自由，民间作坊的经营也更为开放。",
  "Xia Yanjing argues that Northern Song handicrafts surpassed earlier dynasties in scale, technical level, and the quantity and quality of products because the mode of economic operation had changed: most state-workshop artisans were now recruited and personally free, and private workshops operated more openly.",
  "high",
  ["04-knowledge/units/terms/guanying-shougongye.md",
   "04-knowledge/units/terms/shougongye-hanghui.md"],
  "候选作 interpretation；L2462 以“这是由于经济运行方式得到了变革的结果”明确因果，断言保留作者归因；汴梁百万人口、商户6400余家、10万户城市增至40余个等数据在 L2464，未并入本条。",
  2462, 2462, "line", [2462], ["b0318"], "1. 手工业的发展与对外贸易的形成")

C("cand-04-85", "factual_claim",
  "夏燕靖据《天盛律令》指出，西夏具有完备的典章制度，曾设制金司、织绢院、铁工院、木工院、纸工院、砖瓦院、造车院等机构，可见其专业分工相当细致。",
  "Citing the Tiansheng Lvling, Xia Yanjing notes that Western Xia had a complete set of statutes and institutions, including the Gold-making Office, Silk-weaving Bureau, Iron Works, Wood Works, Paper Works, Brick-and-Tile Works, and Carriage Works, showing a finely differentiated division of labour.",
  "high",
  ["04-knowledge/units/publications/tiansheng-lvling.md",
   "04-knowledge/units/institutions/xi-xia-guan-ying-shou-gong-ye-jigou.md",
   "04-knowledge/units/institutions/xi-xia-wensiyuan.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L2478-L2500 含《东京梦华录》《梦粱录》《南海一号》三个知识链接框与辽金手工业段，断言取 L2488 西夏段；西夏190年、十代帝王与贺兰山墓葬出土留在来源。",
  2488, 2488, "line", [2488], ["b0322"], "1. 手工业的发展与对外贸易的形成")

C("cand-04-86", "historiographic_claim",
  "夏燕靖认为，宋代瓷窑遍布各地，因地域和传统工艺差异而各有创新，形成多种瓷窑体系与流派纷呈的兴盛景象；五大名窑即汝窑、官窑、钧窑、哥窑、定窑，是其中的突出代表。",
  "Xia Yanjing argues that Song kilns were spread throughout the country and, differing by region and craft tradition, each innovated, forming multiple kiln systems and a flourishing diversity of schools; the Five Great Kilns—Ru, Guan, Jun, Ge, and Ding—were their outstanding representatives.",
  "high",
  ["04-knowledge/units/terms/wuda-mingyao.md",
   "04-knowledge/units/terms/songdai-yaoxi.md",
   "04-knowledge/units/places/ru-kiln.md",
   "04-knowledge/units/places/jun-kiln.md",
   "04-knowledge/units/places/ding-kiln.md",
   "04-knowledge/units/terms/ge-yao.md",
   "04-knowledge/units/terms/guan-yao.md"],
  "候选作 periodization，路由 historiographic；候选跨度 L2503-L2547 含制瓷业发展、三大特点、五大名窑分述与哥窑考据，断言取 L2515 与 L2517（L2516 为空行），记 contiguous；汝窑支钉、官窑开片、定窑覆烧、钧窑窑变、哥窑金丝铁线等分述留在来源。",
  2515, 2517, "contiguous", [2515, 2517], ["b0324"], "2. 宋瓷的生产规模与设计成就｜1）制瓷业的发展与五大名窑的特色")

C("cand-04-92", "interpretive_claim",
  "夏燕靖认为，钧瓷釉色千变万化，是烧制过程中配料掺入铜的氧化物所造成的艺术效果，这是我国制瓷史上的一大发明，称为“窑变”。",
  "Xia Yanjing argues that the ever-changing colours of Jun ware glazes resulted from copper oxides added to the batch during firing, an artistic effect that was a major invention in Chinese ceramic history and is called kiln transmutation (yaobian).",
  "high",
  ["04-knowledge/units/places/jun-kiln.md",
   "04-knowledge/units/terms/yaobian.md"],
  "候选作 interpretation；来源作“铜的气化物”，按现代术语写“铜的氧化物”并在校记保留原词；钧窑两次烧成、蚯蚓走泥纹与“夕阳紫翠忽成岚”诗句留在来源。",
  2536, 2536, "line", [2536], ["b0324"], "2. 宋瓷的生产规模与设计成就｜1）制瓷业的发展与五大名窑的特色")

C("cand-04-94", "interpretive_claim",
  "夏燕靖认为，靖康之变后大量北方窑工南迁，对江南瓷业生产起到促进作用；南宋江南瓷业大发展以建窑、德化窑、吉州窑相继进入兴旺期为开端。",
  "Xia Yanjing argues that after the Jingkang catastrophe the southward migration of many northern kiln workers promoted porcelain production in Jiangnan, and that the great Southern Song expansion of Jiangnan ceramics began with Jian, Dehua, and Jizhou kilns successively entering their flourishing period.",
  "medium",
  ["04-knowledge/units/places/jian-kiln.md",
   "04-knowledge/units/places/dehua-yao.md",
   "04-knowledge/units/places/jizhou-kiln.md"],
  "候选作 interpretation；候选跨度 L2548-L2551 即“宋代江南瓷业的发展”知识链接框，断言取 L2550；龙泉窑、景德镇窑系、青白瓷、黑瓷与支圈覆烧留在来源。",
  2550, 2550, "line", [2550], ["b0325"], "知识链接：宋代江南瓷业的发展")

C("cand-04-96", "historiographic_claim",
  "夏燕靖认为，宋代中期以后陶瓷装饰更具艺术表现力，往往采用综合手法，如在刻花或印花花纹上用梳栉状工具划出线条表示叶脉或水波；除传统纹饰外又发展出莲瓣、蕉叶、葵瓣、回纹、桂花边、如意云头等辅助纹饰，磁州窑、耀州窑首开纹样装饰之先河。",
  "Xia Yanjing argues that after the mid-Song ceramic decoration became more expressive, often combining techniques—for example incising leaf veins or waves over carved or stamped patterns with a comb-like tool; besides traditional motifs, auxiliary motifs such as lotus petals, banana leaves, mallow petals, meander, osmanthus border, and ruyi-cloud heads developed, with Cizhou and Yaozhou kilns pioneering patterned decoration.",
  "medium",
  ["04-knowledge/units/places/cizhou-kiln.md",
   "04-knowledge/units/places/yaozhou-kiln.md",
   "04-knowledge/units/procedures/pearl-ground-sgraffito.md"],
  "候选作 periodization，路由 historiographic；候选跨度 L2552-L2589 含印花、刻花、划花、剔花、贴花、镂花、弦纹、春字纹、珍珠地划花八种技法分述，断言取 L2582 的综合手法与辅助纹饰总结；各技法定义留在来源。",
  2582, 2582, "line", [2582], ["b0326"], "2. 宋瓷的生产规模与设计成就｜2）宋瓷的装饰手法")

C("cand-04-97", "factual_claim",
  "夏燕靖据《宋会要稿》指出，“上供”丝织物中北方各路仅占1/4，江浙占1/3以上，丝绵则超过2/3，可见江南丝织生产已在五代基础上进一步发展并超过北方。",
  "Citing the Song Huiyao, Xia Yanjing notes that in the silk textiles submitted as tribute, the northern circuits accounted for only a quarter, Jiangzhe for more than a third, and silk floss for over two thirds, showing that Jiangnan silk production had developed further on the Five Dynasties basis and surpassed the north.",
  "high",
  ["04-knowledge/units/publications/song-huiyao-jigao.md",
   "04-knowledge/units/institutions/song-dai-ranzhi-guanli-jigou.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L2592-L2605 含文思院、绫锦院、裁造院、文绣院与各地官方机构，断言取 L2594 的《宋会要稿》比例；宋锦、云锦、蜀锦与“千室夜机鸣”留在来源。",
  2594, 2594, "line", [2594], ["b0328"], "3. 宋代丝织、染缬工艺的发展｜1）丝织工艺的兴盛")

C("cand-04-98", "interpretive_claim",
  "夏燕靖认为，唐代丝织纹样以艳丽、豪华、丰满为特色，宋代则以清淡自然与端重为突出时代风格；宝相花、对鸟、对兽等纹样趋向衰退，写生折枝花、穿枝花及花鸟纹成为主要内容，色彩淡雅柔和、纹样逼真写实。",
  "Xia Yanjing argues that Tang silk patterns were characterized by brilliance, luxury, and fullness, while the Song style was markedly cool, natural, and dignified; motifs such as the baoxiang flower, paired birds, and paired beasts declined, while realistic flowering branches, scrolling floral branches, and bird-and-flower motifs became dominant, with pale, soft colours and lifelike drawing.",
  "high",
  ["04-knowledge/units/terms/baoxianghua-wen.md",
   "04-knowledge/units/works/shen-zifan-hua-niao-tu.md"],
  "候选作 interpretation；候选跨度 L2606-L2614 含纹样设计总论、社会审美背景与图 7-17，断言分置 L2608 与 L2613，中间隔图注行，记 contiguous；二方连续、散点、团花等组织形式留在来源。",
  2608, 2613, "contiguous", [2608, 2613], ["b0329"], "3. 宋代丝织、染缬工艺的发展｜2）丝织纹样设计")

C("cand-04-101", "interpretive_claim",
  "夏燕靖指出，南宋时广西瑶族地区已见蜡染工艺并称“瑶斑布”，当时蜡染技术有很大发展、具备成批生产条件；海南岛黎族妇女织成的棉布“染以杂色，异纹炳然”，证明染缬在少数民族地区也非常盛行。",
  "Xia Yanjing notes that wax-resist dyeing was already found among the Yao of Guangxi in the Southern Song, where it was called yaoban cloth, and that the technique had advanced enough for batch production; cotton cloth woven by Li women on Hainan, “dyed in mixed colours with brilliant distinct patterns,” shows that resist dyeing also flourished among minority peoples.",
  "medium",
  ["04-knowledge/units/procedures/la-ran.md",
   "04-knowledge/units/terms/dian-la-man.md"],
  "候选作 interpretation；断言自 L2623 起、经“宋代官服配饰”知识链接框后在 L2637 收束，记 contiguous 并以 b0330、b0331 为断言所属块，不把 b0332 的官服内容计入；点蜡幔与《诸蕃志》引文按来源保留。",
  2623, 2637, "contiguous", [2623, 2637], ["b0330", "b0331"], "3. 宋代丝织、染缬工艺的发展｜3）染缬工艺的发展")

C("cand-04-99", "factual_claim",
  "夏燕靖指出，北宋末年镂空印花版开始改用桐油竹纸代替以前的木版捺印，使印花纹饰更加精细；为防止染液渗化，还在染液里加入胶粉调成浆状后再印花。宋代因南方航海业兴盛，染缬工艺传到欧洲各国，并很快取代当地用油料加颜料调成的涂料印花。",
  "Xia Yanjing notes that in the late Northern Song the openwork printing block changed from wooden block stamping to oiled bamboo paper, making printed patterns finer, and gum powder was added to the dye liquor to prevent bleeding. Because Southern Song maritime trade flourished, resist-dyeing techniques reached Europe and quickly replaced local pigment-and-oil painted printing.",
  "high",
  ["04-knowledge/units/terms/jiaxie.md",
   "04-knowledge/units/procedures/lan-yinhua-bu.md"],
  "候选作 basic_fact，路由 factual；断言分置 L2617 与 L2619，中间隔 L2618 引《洛阳绅缙旧闻》“李装花”，记 contiguous；夹缬专门化与婺州唐仲友彩帛铺留在来源。",
  2617, 2619, "contiguous", [2617, 2619], ["b0330"], "3. 宋代丝织、染缬工艺的发展｜3）染缬工艺的发展")

C("cand-04-102", "interpretive_claim",
  "夏燕靖指出，宋代每年按品级分送“臣僚袄子锦”共七等，高级官吏各有一定花纹；这些锦缎中的动物图案继承唐代武则天所赐百官纹饰之制而更为具体，也为后来的明代补子图案确定了较详细的种类与范围。",
  "Xia Yanjing notes that the Song court annually distributed “official's jacket brocade” in seven grades, each senior official having a prescribed pattern; the animal designs inherited the system of bestowing patterns on officials under Empress Wu of the Tang but were more specific, and they defined in some detail the types and range of the later Ming rank badges.",
  "medium",
  ["04-knowledge/units/terms/buzi.md"],
  "候选作 interpretation；“为明代补子确定种类与范围”是作者的制度史溯源判断，保留判断语气；翠毛、宜男、云雁细锦、狮子、练雀等具体花纹留在来源。",
  2635, 2635, "line", [2635], ["b0332"], "知识链接：宋代官服配饰")

C("cand-04-103", "interpretive_claim",
  "夏燕靖认为，宋代衣冠服饰基本承袭前朝制度，制订了上自皇帝、皇太子、诸王、宫妃及各级品官，下及吏庶的各类服饰；又因抬高道教使释、道服饰更趋规范，并与契丹、女真、党项、蒙古族多边交往及海外贸易发展，在保留本民族特点的同时广泛吸取“众家”之长。",
  "Xia Yanjing argues that Song dress largely inherited earlier dynastic systems, with garments prescribed from emperor, crown prince, princes, and palace women down through officials to clerks and commoners; the elevation of Daoism made Buddhist and Daoist dress more regulated, while multi-sided contacts with the Khitan, Jurchen, Tangut, and Mongol peoples and the growth of overseas trade led Song dress to absorb widely from others while keeping its own character.",
  "medium",
  ["04-knowledge/units/terms/gongfu.md"],
  "候选作 interpretation；候选跨度 L2639-L2642 为服饰节总论，断言取 L2641；下文品冠服饰沿袭唐制、佩鱼袋、乾德服色与贵族女服留在来源。",
  2641, 2641, "line", [2641], ["b0333"], "4. 宋代服饰与艺术设计风格")

C("cand-04-105", "interpretive_claim",
  "夏燕靖指出，1975年福建浮仓山出土的南宋贵族妇女墓，陪葬衣装配件十分齐全，为研究宋代女子衣饰特别是贵妇、宫妃服饰提供了极好的材料；其服式绝大部分为直领对襟、无带无扣，颈部外缘重叠缝制护领，均采用衣袖相连的裁剪方式。",
  "Xia Yanjing notes that the 1975 excavation of a Southern Song aristocratic woman's tomb at Fucangshan, Fujian, yielded a remarkably complete set of garments and accessories, providing excellent material for studying Song women's dress, especially that of noblewomen and palace women; most garments were straight-collared and front-opening, without ties or buttons, with a protective collar overlapping at the neck, and all were cut with sleeves joined to the body.",
  "high",
  ["04-knowledge/units/events/fucangshan-tomb.md",
   "04-knowledge/units/terms/beizi.md"],
  "候选作 interpretation；出土物清单含袍、袄、裙、衫、裤、肚兜、绶带、鞋、袜、香囊等，断言只取墓葬价值与服式共性；印金、刺绣、彩绘与牡丹、山茶、梅花、百合纹样留在来源。",
  2649, 2649, "line", [2649], ["b0334"], "4. 宋代服饰与艺术设计风格｜1）品冠服饰的类别")

C("cand-04-106", "factual_claim",
  "夏燕靖指出，宋代平民百姓服饰大多是短衣、紧腿、缚鞋、褐布，便于劳作；其他工商各行均有特定服饰，素有“百工百衣”之称，《东京梦华录》称士、农、商诸行百户衣装各有本色、不敢越外。",
  "Xia Yanjing notes that ordinary Song people mostly wore short jackets, tight trousers, tied shoes, and coarse brown cloth for ease of work; other trades had their own dress, hence the saying “a hundred trades, a hundred garments,” and the Dongjing Menghua Lu records that scholars, farmers, merchants, and the various trades each had their proper dress and dared not exceed it.",
  "high",
  ["04-knowledge/units/terms/yanju-fu.md",
   "04-knowledge/units/publications/dongjing-menghua-lu.md",
   "04-knowledge/units/works/qingming-shanghe-tu.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L2657-L2671 含燕居服、男子服饰种类、妇女常服与首饰，断言取 L2663；《清明上河图》数百人物与僧侣服、衙役服、兵服留在来源。",
  2663, 2663, "line", [2663], ["b0335"], "4. 宋代服饰与艺术设计风格｜2）常服的类别")

C("cand-04-107", "interpretive_claim",
  "夏燕靖认为，宋代雕版印刷技术已臻成熟，宋版书的主要特点可概括为版式、字体、用纸和插图4项；从版式看，北宋刻本大多是白口、左右双栏或四周双栏，南宋中叶开始流行黑口，多见于建本。",
  "Xia Yanjing argues that woodblock printing had matured by the Song, and the main features of Song editions can be summarized under four heads: format, typeface, paper, and illustration; as to format, Northern Song editions were mostly white-mouthed with double side borders or double borders all round, while from the mid-Southern Song black-mouthed format became popular, especially in Jian editions.",
  "high",
  ["04-knowledge/units/terms/songban-shu.md",
   "04-knowledge/units/procedures/diaoban-yinshua.md"],
  "候选作 interpretation；断言分置 L2678 与 L2682，中间隔 L2680 图注与 L2681 空行，记 contiguous；字体（欧颜柳）、用纸（竹纸、皮纸）与插图（《开宝藏》扉画、56幅连环版画）留在来源。",
  2678, 2682, "contiguous", [2678, 2682], ["b0337"], "5. 雕版印刷与商业美术设计｜1）雕版印刷")

C("cand-04-111", "interpretive_claim",
  "夏燕靖认为，宋代小商品生产日趋活跃，南宋以后家庭手工业作坊繁多、商品竞争随之而来；最初没有商标和正式广告，只把生产者姓名用刻印图章的形式写在商品上，形成陶瓷、漆器、金银器、铜镜等标记，这是宋朝商业美术的萌芽，并逐步发展形成行业。",
  "Xia Yanjing argues that petty commodity production became increasingly active in the Song, and after the Southern Song household workshops multiplied, bringing market competition; at first there were no trademarks or formal advertisements, only the maker's name stamped on goods—ceramic, lacquer, gold-and-silver, and bronze-mirror marks—which was the germ of Song commercial art and gradually developed into a trade.",
  "high",
  ["04-knowledge/units/terms/shangbiao.md",
   "04-knowledge/units/terms/huangzi.md",
   "04-knowledge/units/terms/zhaopai.md",
   "04-knowledge/units/works/jinan-liujia-zhenpu-tongban.md"],
  "候选作 interpretation；候选跨度 L2689-L2701 含市镇、幌子与《济南刘家功夫针铺》铜版，断言取 L2693 的商标萌芽段；张家造、湖州石家念二叔照子等标记留在来源。",
  2693, 2693, "line", [2693], ["b0338"], "5. 雕版印刷与商业美术设计｜2）商业美术设计")

C("cand-04-112", "interpretive_claim",
  "夏燕靖指出，宋代日用品铜器多为杯、盘、罐、壶、盒、炉之类，杭州老和山宋墓、长沙宋墓、苏州虎丘云岩寺塔、山西忻县宋墓及山西襄汾赵康地区均有出土；这些宋代日用铜器表现出质朴的风格。",
  "Xia Yanjing notes that Song everyday bronze vessels were mostly cups, dishes, jars, ewers, boxes, and censers, excavated from Song tombs at Laoheshan in Hangzhou, Changsha, the Yunyan Temple pagoda at Huqiu in Suzhou, Xinxian in Shanxi, and Zhaokang in Xiangfen, Shanxi; these daily bronzes show a plain and unadorned style.",
  "medium",
  ["04-knowledge/units/works/bronze-ewer.md"],
  "候选作 interpretation；断言取 L2706 的类型、出土地与“质朴”风格判断；铜执壶、匜形提染锅的造型分析留在来源，另以 works/bronze-ewer 承接执壶。",
  2706, 2706, "line", [2706], ["b0340"], "6. 金属制器与工艺设计｜1）铜器工艺")

C("cand-04-113", "factual_claim",
  "夏燕靖据《梦粱录》指出，宋代金银制器仍作为财富宝藏，被视为可用作货币的替代品；北宋输往辽、西夏的物资除粮食、茶叶、布帛、瓷器、漆器外，还使用大量金银制器，一是用于相互间交换货物的结算，二是馈赠辽、西夏上层统治者以谋求和平相处。",
  "Citing the Mengliang Lu, Xia Yanjing notes that Song gold and silver vessels still served as treasure and were regarded as substitutes for money; Northern Song goods sent to Liao and Western Xia included, besides grain, tea, cloth, porcelain, and lacquerware, large quantities of gold and silver vessels, used both to settle exchanges and as gifts to Liao and Western Xia rulers to secure peace.",
  "high",
  ["04-knowledge/units/events/deyang-xiaoquan-silver-find.md",
   "04-knowledge/units/works/wensiyuan-yin-xunlu.md"],
  "候选作 basic_fact，路由 factual；断言跨 L2717 与 L2719，中间隔 L2718 空行与图注行，记 contiguous；临安金银盐钞引交易铺、德阳117件银器与银熏炉留在来源。",
  2717, 2719, "contiguous", [2717, 2719], ["b0341"], "6. 金属制器与工艺设计｜2）金银器工艺")

C("cand-04-114", "interpretive_claim",
  "夏燕靖认为，宋代木构架建筑采用了以“材”为标准的模数制和工料定额制，使建筑设计施工达到了一定程度的规范化。",
  "Xia Yanjing argues that Song timber-frame architecture adopted a module system based on the “cai” standard and a system of labour-and-material quotas, bringing a degree of standardization to architectural design and construction.",
  "high",
  ["04-knowledge/units/publications/yingzao-fashi.md"],
  "候选作 interpretation；候选跨度 L2730-L2735 含汴梁沿街设店、晋祠圣母殿、辽金建筑与砖石塔，断言取 L2734 的材模数与定额制；开封相国寺塔28种琉璃砖、定县瞭敌塔84米留在来源。",
  2734, 2734, "line", [2734], ["b0343"], "7. 宋代建筑及家具设计｜1）建筑与建筑彩绘设计")

C("cand-05-02", "interpretive_claim",
  "夏燕靖据《营造法式》指出，宋代建筑彩画有五彩遍装、碾玉装、青绿叠晕棱间装、解绿装、丹粉刷装、杂间装六种类型，制作分“衬地”“衬色”“细色”“贴金”四步，并盛行退晕和对晕手法；明清两代的建筑漆绘彩画都由此发展而来。",
  "Citing the Yingzao Fashi, Xia Yanjing notes that Song architectural painting had six types—polychrome overall, jade-grinding, blue-green layered corner, green-relief, cinnabar-powder, and mixed—executed in four stages (grounding, colour grounding, fine colour, gold application), with graded and mirrored shading; Ming and Qing architectural lacquer painting developed from this.",
  "high",
  ["04-knowledge/units/publications/yingzao-fashi.md",
   "04-knowledge/units/procedures/song-dai-jianzhu-caihua.md"],
  "候选作 interpretation；来源作“青绿叠罩绫间装”，按《营造法式》通行文本写“青绿叠晕棱间装”，并在校记保留原词；《营造法式》四部分内容留在 L2740 知识链接框。",
  2742, 2742, "line", [2742], ["b0345"], "知识链接：《营造法式》")

C("cand-05-03", "interpretive_claim",
  "夏燕靖认为，宋代家具以梁柱式框架结构取代箱形壶门结构，并大量应用线脚与拼合梁做法，其造型与结构创新为元、明、清家具发展奠定了基础。",
  "Xia Yanjing argues that Song furniture replaced the box-and-lotus-panel construction with a post-and-beam frame, widely applied mouldings and built-up beams, and that its formal and structural innovations laid the foundation for Yuan, Ming, and Qing furniture.",
  "high",
  ["04-knowledge/units/terms/gaoxing-jiaju.md",
   "04-knowledge/units/procedures/pinhe-liang.md",
   "04-knowledge/units/terms/ming-style-furniture.md"],
  "候选作 interpretation；断言分置 L2746（结构转变与线脚）与 L2764（为元明清奠基），中间隔家具品种、拼合梁实例与图注，记 contiguous；束腰、牙条、罗锅枨、霸王枨、矮老、龟脚、马蹄足等构件名留在来源。",
  2746, 2764, "contiguous", [2746, 2764], ["b0346"], "7. 宋代建筑及家具设计｜2）家具")

C("cand-05-04", "interpretive_claim",
  "夏燕靖认为，辽瓷与邢窑、定窑关系最为密切，其器形一为模仿中原传统的定瓷风格，一为契丹族特有的鸡冠壶、凤首瓶、鸡腿坛等，形成双轨并存的器形体系。",
  "Xia Yanjing argues that Liao ceramics were most closely related to the Xing and Ding kilns, with two parallel form systems: imitations of Central Plains Ding-style wares, and distinctive Khitan forms such as the chicken-crest ewer, phoenix-head vase, and chicken-leg jar.",
  "high",
  ["04-knowledge/units/terms/liao-ci.md",
   "04-knowledge/units/terms/jiguang-hu.md",
   "04-knowledge/units/places/ding-kiln.md",
   "04-knowledge/units/places/xing-kiln.md",
   "04-knowledge/units/terms/liao-sancai.md"],
  "候选作 interpretation；来源列三角碟、四方碟、海棠盘、长颈瓶、凤首瓶、鸡冠壶、鸡腿坛，断言取“双轨并存”的概括并保留代表器名；辽三彩釉陶与素胎、釉色装饰留在来源。",
  2777, 2777, "line", [2777], ["b0348"], "8. 辽和金时期的艺术设计｜1）辽瓷的工艺特色")

C("cand-05-05", "factual_claim",
  "夏燕靖指出，金代钧窑在青釉上显现红斑，开创了彩瓷的先声。",
  "Xia Yanjing notes that Jin dynasty Jun ware showed red patches on celadon glaze, heralding the beginning of polychrome porcelain.",
  "medium",
  ["04-knowledge/units/places/jun-kiln.md",
   "04-knowledge/units/terms/yaobian.md"],
  "候选作 attribution，按类型映射路由 factual；“开创了彩瓷的先声”是作者的技术史定位，随文保留而不另升为 evaluative；金代定窑砂圈叠烧、磁州窑宋加彩、耀州窑印花留在来源。",
  2794, 2794, "line", [2794], ["b0349"], "8. 辽和金时期的艺术设计｜2）金瓷的工艺特色")

C("cand-05-09", "interpretive_claim",
  "夏燕靖认为，辽代金银制品在器形与缠枝花、云龙纹等纹样上继承唐宋中原传统，同时以马具、银丝手套、野鹿含花、猎犬搏鹿等题材保留浓厚的契丹边疆色彩。",
  "Xia Yanjing argues that Liao gold and silver work inherited Tang-Song Central Plains traditions in forms and in motifs such as scrolling flowers and cloud-dragon, while subjects such as horse harness, silver-wire gloves, deer-with-flower, and hound-seizing-deer retained a strong Khitan frontier character.",
  "medium",
  ["04-knowledge/units/works/qidan-an.md"],
  "候选作 interpretation；候选跨度 L2830-L2835 含辽代金银矿冶与赤峰、义县、泰来、北京出土清单，断言取 L2834 的风格判断；“铜镜一类几乎全为内地所造”留在来源。",
  2834, 2834, "line", [2834], ["b0352"], "8. 辽和金时期的艺术设计｜5）辽代金属工艺")

C("cand-05-10", "evaluative_claim",
  "夏燕靖认为，金代的银铜及铁制器工艺得益于官营冶铸业的提高与民间冶铁业的发展，其铸冶工艺水平和器皿造型样式都已超过北宋。",
  "Xia Yanjing holds that Jin silver, bronze, and iron work benefited from improved state smelting and the growth of private iron making, and that both its casting and smelting techniques and vessel forms had surpassed those of the Northern Song.",
  "medium",
  ["04-knowledge/units/terms/jin-dai-tongjin.md",
   "04-knowledge/units/procedures/sheng-tie-ye-zhu-ji-shu.md"],
  "候选作 interpretation，但断言主体是“超过北宋”的高下比较，按以评价为主改路由 evaluative；候选跨度 L2836-L2850 含铜禁、上京巡警院款镜、肇州七百余件铁器，断言取 L2849 的总结评价。",
  2849, 2849, "line", [2849], ["b0353"], "8. 辽和金时期的艺术设计｜6）金代银铜及铁制器工艺的形成与发展")

C("cand-05-11", "interpretive_claim",
  "夏燕靖据马可·波罗记载指出，西夏毛织业生产水平较高，其驼毛布被记为“世界最佳美”，说明西夏毛织品已引起世人注意。",
  "Citing Marco Polo, Xia Yanjing notes that Western Xia wool production was of a high level, its camel-wool cloth being recorded as “the best in the world,” showing that Western Xia woollens had attracted wide attention.",
  "medium",
  ["04-knowledge/units/terms/pulu.md"],
  "候选作 interpretation；候选跨度 L2855-L2862 含西夏畜牧区、鞣皮纺毛与氆氇毛褐毡毯，断言取 L2861 的马可·波罗记载与推断；来源记“白驼毛布是白羊毛做的”前后矛盾，断言只取“世界最佳美”评语，未复述该句。",
  2861, 2861, "line", [2861], ["b0355"], "9. 西夏时期的艺术设计｜1）西夏的毛织工艺")

C("cand-05-13", "evaluative_claim",
  "夏燕靖认为，西夏瓷器虽有特色精品，但总体制作水平不高、质量不稳定，与宋瓷不可同日而语。",
  "Xia Yanjing holds that although Western Xia porcelain included distinctive fine pieces, overall its production level was not high and quality was unstable, so it could not be mentioned in the same breath as Song porcelain.",
  "medium",
  ["04-knowledge/units/events/xixia-mausoleum.md",
   "04-knowledge/units/works/xixia-wangling.md"],
  "候选作 interpretation，但断言主体是制作水平与宋瓷的高下比较，按以评价为主改路由 evaluative；候选跨度 L2870-L2887 含活字印刷知识链接与西夏瓷器釉色、器形、圈足特征，断言取 L2879 的总评。",
  2879, 2879, "line", [2879], ["b0357"], "9. 西夏时期的艺术设计｜2）西夏的瓷器工艺")

C("cand-05-15", "interpretive_claim",
  "夏燕靖认为，西夏活字印刷术在向西方传播的过程中起到了桥梁作用。",
  "Xia Yanjing argues that Western Xia movable-type printing served as a bridge in the transmission of the technique westward.",
  "medium",
  ["04-knowledge/units/procedures/huozi-yinshua.md",
   "04-knowledge/units/works/xixia-movable-type-print.md"],
  "候选作 interpretation；断言在“西夏工艺技术成就”知识链接框内 L2874 末句，以“从时间的演进和交流地域推见”保留推测语气；西夏砖雕、瓦当、夏国剑、刻字司留在同框。",
  2874, 2874, "line", [2874], ["b0357"], "知识链接：西夏工艺技术成就")


def main():
    assert len(ROWS) == 29, len(ROWS)
    types = {"factual_claim", "interpretive_claim", "synthetic_claim",
             "evaluative_claim", "contested_claim", "historiographic_claim"}
    seen = set()
    for i, row in enumerate(ROWS):
        row["claim_id"] = "claim-%04d" % (166 + i)
        assert row["claim_type"] in types, row["claim_type"]
        assert row["confidence"] in {"high", "medium", "low"}
        assert row["statement_zh"].startswith("夏燕靖"), row["claim_id"]
        assert row["statement_en"].strip()
        assert row["discussion_notes"].strip()
        assert row["consensus"] == "tentative"
        assert row["review_status"] == "source_backed"
        cid = row["source"]["candidate_id"]
        assert cid not in seen, cid
        seen.add(cid)
        sp = row["source"]["source_span"]
        assert 2444 <= sp["line_start"] <= sp["line_end"] <= 2915, sp
        assert sp["key_lines"] and all(sp["line_start"] <= x <= sp["line_end"] for x in sp["key_lines"]), sp
        assert sp["block_ids"], sp
        assert sp["span_kind"] in {"line", "contiguous", "bounded"}
        if sp["span_kind"] == "line":
            assert sp["line_start"] == sp["line_end"]
        for p in row["supported_by"]:
            assert p.startswith("04-knowledge/units/"), p
            assert (ROOT / p).exists(), p
    assert len({r["source"]["candidate_id"] for r in ROWS}) == 29
    (ROOT / "_zn_claim_xyj09f_rows.json").write_text(
        json.dumps(ROWS, ensure_ascii=False, indent=2), encoding="utf-8")
    from collections import Counter
    print(json.dumps({
        "claims": len(ROWS),
        "with_support": sum(1 for r in ROWS if r["supported_by"]),
        "links": sum(len(r["supported_by"]) for r in ROWS),
        "distinct_support": len({p for r in ROWS for p in r["supported_by"]}),
        "types": dict(Counter(r["claim_type"] for r in ROWS)),
        "confidence": dict(Counter(r["confidence"] for r in ROWS)),
        "span_kinds": dict(Counter(r["source"]["source_span"]["span_kind"] for r in ROWS)),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
