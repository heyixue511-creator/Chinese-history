# -*- coding: utf-8 -*-
"""Build CL2h claim rows (Xia Yanjing 2009, ch.9 Ming-Qing)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
CH = "明清时期的艺术设计"

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


C("cand-05-63", "historiographic_claim",
  "夏燕靖指出，明朝中后期江南苏州等地的丝织业中出现带有手工工场性质的“机房”，其“机房出资、机工出力”的生产方式就是资本主义雇佣剥削的生产关系的萌芽，是我国封建社会前所未见的现象。",
  "Xia Yanjing notes that in the mid-to-late Ming, silk-weaving workshops of a manufactory character appeared in Suzhou and other Jiangnan places, and that their arrangement in which the workshop supplied capital and the weavers supplied labour was the germ of capitalist wage exploitation, a phenomenon unprecedented in Chinese feudal society.",
  "high",
  ["04-knowledge/units/terms/jifang.md",
   "04-knowledge/units/terms/zaoqi-gongyehua.md"],
  "候选作 periodization，按分期史判断路由 historiographic；候选跨度 L3383-L3394 含知识链接标题、两幅疆域图与章首导论；断言取 L3385 的“机房”判断句；同行的 30 多座工商业城市、白银流通与 L3387 的明清手工业总述留在来源。来源未给“机房”的规模、雇工数与工资形态，“资本主义萌芽”为史学命题，保留作者归属，不作已证事实。",
  3385, 3385, "line", [3385], ["b0411"], "知识链接：明中期以后的经济与手工业")

C("cand-05-64", "factual_claim",
  "夏燕靖指出，明代丝织形成江浙、四川、山西、闽广四大产区：江浙为全国丝织生产中心，苏州、杭州、嘉兴及吴江震泽、盛泽等市镇兴盛；四川以蜀锦著称；山西潞绸行销天下；闽广则有福建改机、漳州天鹅绒与广东纱。",
  "Xia Yanjing notes that Ming silk weaving comprised four major regions: Jiangzhe was the national centre, with Suzhou, Hangzhou, Jiaxing, and the new towns of Zhenze and Shengze; Sichuan was known for Shu brocade; Shanxi for Lu silk; and Fujian-Guangdong for Fujian gaiji, Zhangzhou velvet, and Guangdong gauze.",
  "high",
  ["04-knowledge/units/terms/mingdai-sizhi-sida-changu.md",
   "04-knowledge/units/terms/shu-brocade.md",
   "04-knowledge/units/terms/lu-chou.md",
   "04-knowledge/units/terms/gaiji.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L3409-L3423 含四大产区逐条分述与图 9-3、9-4；断言取 L3411 的总述并压缩各地产物；蜀锦“特设织锦坊供御用”、潞安绸机一万三千余张、改机四层织法与“走马看妆花”等细节留在来源。候选说明把“潞绸”写作产区代表，原文为山西产品名，断言按原文改正。",
  3411, 3411, "line", [3411], ["b0413"], "1. 纺织印染业的高度繁荣与染织品种设计｜1）丝织工艺的产区与品种特色")

C("cand-05-91", "historiographic_claim",
  "夏燕靖认为，清代丝织品种的艺术特色可分三期：康熙年间大体承继明代风格，以“八达晕”一类图案最有特色；雍正时期改进织机、采用多层经纬织法，纹样更丰富、色彩更华丽；乾隆时期吸收法国巴洛克和洛可可式样，总体显得过于堆砌和繁缛。",
  "Xia Yanjing periodizes the artistic character of Qing silk fabrics into three phases: under Kangxi the Ming style largely continued, with badayun medallion patterns most distinctive; under Yongzheng improved looms and multi-layer warp-and-weft weaving enriched patterns and colour; and under Qianlong French Baroque and Rococo models were adopted, producing an overall effect he judges over-elaborate and congested.",
  "high",
  ["04-knowledge/units/terms/qing-dai-sizhi-pinzhong.md",
   "04-knowledge/units/terms/badayun.md",
   "04-knowledge/units/terms/nanjing-yunjin.md"],
  "候选作 periodization，路由 historiographic；断言取 L3445 的三期分述；候选跨度仅 L3445，杭州 14 大类、200 多品种、2000 余花色与苏州、松江诸品种留在同段前半；乾隆期“过于堆砌和繁缛”为作者评价，保留归属。",
  3445, 3445, "line", [3445], ["b0415"], "1. 纺织印染业的高度繁荣与染织品种设计｜1）丝织工艺的产区与品种特色")

C("cand-05-69", "factual_claim",
  "夏燕靖指出，明代棉织业发展很快、几乎遍及全国，明代后期棉布已取代丝、麻、毛，成为人们最重要的衣被材料。",
  "Xia Yanjing notes that Ming cotton weaving developed rapidly and spread throughout the country, and that by the late Ming cotton cloth had replaced silk, hemp, and wool as the most important material for clothing and bedding.",
  "high",
  ["04-knowledge/units/places/songjiang-fu.md",
   "04-knowledge/units/terms/ma-bu.md"],
  "候选作 basic_fact，路由 factual；断言取 L3449；候选跨度 L3447-L3452 含明初至永乐棉布征收数、松江府民谣、明代棉布品种与清代棉布产量；征收 60 万至 180 万匹、标布、扣布、稀布、丁娘子布与清代 3.1 亿匹等数据未并入。麻布条只承载被替代材料之一，属语境链接。",
  3449, 3449, "line", [3449], ["b0416"], "1. 纺织印染业的高度繁荣与染织品种设计｜2）棉织工艺与品种")

C("cand-05-70", "interpretive_claim",
  "夏燕靖认为，明代精练丝绸分两步，初练用草木灰汤，复练用猪胰汤或瓜蒌汤；这种利用动植物生物酶使生丝脱胶的方法，使中国利用生物酶的技术在世界处于领先地位。",
  "Xia Yanjing argues that Ming silk scouring proceeded in two steps, an initial boil in wood-ash lye and a second treatment with pig pancreas or Trichosanthes broth, and that this use of plant and animal enzymes to degum raw silk placed China's enzyme technology in a leading position in the world.",
  "medium",
  ["04-knowledge/units/procedures/daolian-fa.md",
   "04-knowledge/units/procedures/sao-si-piaobai.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3455；候选跨度 L3453-L3462 含印染中心、清代苏州踹染与药斑布工艺；芜湖、京口中心、康熙三十四年采办 30 万匹、苏州布号与染匠万人、“苏印”等留在来源。捣练法条只覆盖草木灰与脱胶的早期方法，缫丝漂白条覆盖漂白晾丝，二者均非明代猪胰、瓜蒌复练的直接记载，属技术谱系链接。“世界领先”保留作者评价语气，不作已证事实。",
  3455, 3455, "line", [3455], ["b0417"], "1. 纺织印染业的高度繁荣与染织品种设计｜3）印染工艺与品种")

C("cand-05-71", "factual_claim",
  "夏燕靖指出，清代以满族习俗改制换样，顺治九年（1652）颁布《服色肩舆条例》，废除浓厚汉民族色彩的冠冕衣裳，男子改蓄辫、穿马蹄袖箭衣、紧袜深统靴，与明代男子蓄发挽髻、宽衣长袜浅鞋的面貌形成对比。",
  "Xia Yanjing notes that the Qing remodelled dress according to Manchu custom, promulgating the Regulations on Dress Colour and Sedan Chairs in the ninth year of Shunzhi (1652), which abolished the crown-and-robe system strongly marked by Han tradition and replaced the Ming male mode of coiled hair, loose robes, long socks, and low shoes with the queue, horse-hoof-sleeved archer's coat, tight socks, and tall boots.",
  "high",
  ["04-knowledge/units/events/queue-and-dress-edicts.md",
   "04-knowledge/units/terms/qipao.md"],
  "候选作 basic_fact，路由 factual；断言取 L3465；候选跨度 L3463-L3466 仅含本节导论；明代服饰“上采周汉，下取唐宋”与戏曲戏装化留在同段前半。现行 KU 无《服色肩舆条例》专条，剃发易服事件条只记清初易服令与“十从十不从”，未记 1652 年与条例名；旗袍条只承载满族袍服一线，属语境链接。条例名与年份为来源孤证，保留原文。",
  3465, 3465, "line", [3465], ["b0418"], "2. 服装工艺与服装设计")

C("cand-05-75", "factual_claim",
  "夏燕靖指出，清代官服补子采用青缎地绣，文官补子绣白鹤、锦鸡、孔雀、云雁、白鹇、鹭鸶、鹌鹑、练雀等禽纹，武官补子绣麒麟、狮子、豹、虎、熊、彪、犀牛、海马等兽纹，各有九品，构成多种方形综合纹样。",
  "Xia Yanjing notes that Qing official rank badges were embroidered on dark-blue satin: civil officials' badges bore birds such as the white crane, golden pheasant, peacock, wild goose, silver pheasant, egret, quail, and painted quail, while military officials' badges bore beasts such as the qilin, lion, leopard, tiger, bear, young tiger, rhinoceros, and sea horse, each with nine grades and forming a variety of square composite designs.",
  "high",
  ["04-knowledge/units/terms/buzi.md"],
  "候选作 basic_fact，路由 factual；断言取 L3512 的“公服‘补子’”知识链接框；候选跨度 L3510-L3515 含框题、框内文字与紧接的女服残段；框内白鹤“丹顶黑尾”、红日三蝠蓝云、四边水红花朵等细部留在来源。来源此处文官表列“鹌鹑、练雀”而正文 L3473 的明制九品为“鹌鹑、海马”，明清两表不同，本条只记清制，未与明制合并。",
  3512, 3512, "line", [3512], ["b0423"], "2. 服装工艺与服装设计｜知识链接：公服“补子”")

C("cand-05-76", "interpretive_claim",
  "夏燕靖认为，清代服饰制度是我国历代服饰规制中条文规章最为庞杂、繁缛的一种；由于去今不远、文献与实物保存相对完整，它既保留了汉族服制中的某些特点，又不失满族本民族的习俗礼仪。",
  "Xia Yanjing holds that the Qing dress system was the most elaborate and cumbersome body of regulations among the dress codes of Chinese dynasties, and that because the period is recent and documents and objects survive relatively intact, it preserved certain features of Han dress while retaining Manchu customs and etiquette.",
  "high",
  ["04-knowledge/units/terms/buzi.md",
   "04-knowledge/units/terms/qipao.md",
   "04-knowledge/units/persons/jin-zhijun.md",
   "04-knowledge/units/events/queue-and-dress-edicts.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3526 的判断句；候选跨度 L3516-L3547 含“十从十不从”全文、皇帝朝服、龙袍、蟒袍、旗袍源流、汉族女装与鞋制；十二章、海水江涯、蟒袍品级、旗袍曲线美等细节未并入。评价句为作者判断，保留“算是”的限定。",
  3526, 3526, "line", [3526], ["b0424"], "2. 服装工艺与服装设计｜2）清代服饰")

C("cand-05-78", "factual_claim",
  "夏燕靖指出，明清陶瓷在两宋全面发展的基础上又迈向一个高峰，景德镇成为瓷都、宜兴成为陶都，两大陶瓷基地的地位日益突出；同时琉璃烧造成为最大宗，瓦脊等建筑用陶与日用器皿成为市场行销产品。",
  "Xia Yanjing notes that Ming-Qing ceramics reached a further peak on the foundation of Song development: Jingdezhen became the porcelain capital and Yixing the pottery capital, the two ceramic bases grew increasingly prominent, and architectural glazed tiles and ridge ornaments together with domestic wares became major market goods.",
  "high",
  ["04-knowledge/units/places/jingdezhen.md",
   "04-knowledge/units/places/yixing.md",
   "04-knowledge/units/terms/zisha-tao.md"],
  "候选作 basic_fact，路由 factual；断言取 L3550；候选跨度 L3548-L3551 含节题与总述；琉璃一节的具体窑址与“十样”规格在 L3619-L3621，未并入本条。景德镇条以城市史与官窑建制为主，宜兴条与紫砂条承载陶都一线。",
  3550, 3550, "line", [3550], ["b0425"], "3. 陶瓷业的繁荣与品种的发展")

C("cand-05-79", "interpretive_claim",
  "夏燕靖认为，明代制瓷技术的最大成就是高质量白釉的烧制成功；工匠掌握了釉料中氧化铝和二氧化硅的比例，使釉色纯白如奶、晶莹明亮，为颜色釉和彩瓷的发展创造了条件。",
  "Xia Yanjing argues that the greatest achievement of Ming ceramic technology was the successful firing of high-quality white glaze: craftsmen mastered the proportion of alumina and silica in the glaze, producing a pure milk-white, luminous glaze and creating the conditions for the development of monochrome and polychrome wares.",
  "high",
  ["04-knowledge/units/procedures/chuiyou-fa.md",
   "04-knowledge/units/procedures/ming-qing-caici-zhuangshi.md",
   "04-knowledge/units/places/jingdezhen-kiln.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3554 的前三句；候选跨度 L3552-L3565 含官窑淘炼、利刀法、吹釉法、窑身扩大、清代蛋形窑与康雍乾官窑；白度“超过 75℃”的单位照录问题留在吹釉法条，未在本条复述。“最大成就”为作者判断，保留归属。",
  3554, 3554, "line", [3554], ["b0426"], "3. 陶瓷业的繁荣与品种的发展｜1）瓷器工艺的改进与特色形成")

C("cand-05-80", "interpretive_claim",
  "夏燕靖指出，明代青花各时期装饰题材不同：宣德多用缠枝花、一束莲、牡丹、鹊梅、三友图，成化多用婴戏、人物仕女、草虫小景，嘉靖多用莲花鱼藻、云鹤、海马、寿山福海、祥麟瑞兽、人物楼台，万历多用寿字树、狮鹿、凤穿牡丹；从艺术风格看，宣德浑厚、成化清雅、嘉靖逸趣、万历秀美。",
  "Xia Yanjing notes that Ming blue-and-white decoration varied by reign: Xuande wares favoured scrolling flowers, a bundle of lotus, peony, magpie-and-plum, and the Three Friends; Chenghua wares favoured children at play, ladies, insects, and small scenes; Jiajing wares favoured lotus and fish among waterweeds, cloud cranes, sea horses, auspicious beasts, and figures with pavilions; and Wanli wares favoured longevity-character trees, lion and deer, and phoenix among peonies, with the styles summed up as robust under Xuande, refined under Chenghua, diverting under Jiajing, and elegant under Wanli.",
  "high",
  ["04-knowledge/units/terms/blue-and-white-porcelain.md",
   "04-knowledge/units/procedures/ming-qing-caici-zhuangshi.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3568 的“青花装饰”知识链接框；候选跨度 L3566-L3569 含框题与框内全文；弘治正德、隆庆万历与晚明三段题材压缩并入“各时期不同”，未逐朝罗列。四个风格词“浑厚、清雅、逸趣、秀美”为作者评语，保留原文。",
  3568, 3568, "line", [3568], ["b0427"], "3. 陶瓷业的繁荣与品种的发展｜知识链接：青花装饰")

C("cand-05-83", "interpretive_claim",
  "夏燕靖认为，青花瓷以胎釉洁润、色泽浓淡相间、层次丰富、极富水墨画情趣、色彩深入胎骨经久不变等优点，成为我国瓷器的主流，历经六百年不衰。",
  "Xia Yanjing argues that blue-and-white porcelain, with its clean lustrous body and glaze, varied tonal density, rich layering, affinity to Chinese ink painting, and colour fixed in the body so that it does not fade, became the mainstream of Chinese ceramics and remained so for six hundred years.",
  "high",
  ["04-knowledge/units/terms/blue-and-white-porcelain.md",
   "04-knowledge/units/works/qinghua-baleng-longwen-ping.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3583；候选跨度 L3574-L3592 含“釉上彩”“釉下彩”两个知识链接框、祭红、郎窑红、豇豆红、苏麻离青、回青、葫芦瓶与外销数据；1602-1682 年荷兰东印度公司贩运 1600 万件以上未并入。青花八棱海水龙纹瓶只作明代青花实例，属示例链接。",
  3583, 3583, "line", [3583], ["b0429"], "3. 陶瓷业的繁荣与品种的发展｜1）瓷器工艺的改进与特色形成")

C("cand-05-85", "interpretive_claim",
  "夏燕靖认为，石湾陶艺长期依赖大宗日用陶器的制作而存在，一直是石湾窑赖以维持的经济来源；假如没有日用陶器生产，陶艺充其量只是石湾窑的“锦上之花”。",
  "Xia Yanjing argues that Shiwan ceramic art long depended on the production of bulk domestic pottery, which remained the economic mainstay of the Shiwan kilns; without that domestic ware, he suggests, the art wares would at most be a decorative embellishment on the kiln's output.",
  "medium",
  ["04-knowledge/units/places/shiwan-yao.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3603 的依存关系句，保留“假如”的假设语气；候选跨度 L3593-L3616 含宜兴窑、蜀山龙窑、紫砂壶、石湾窑源流与“瘦骨仙”“弥勒佛”“金蟾”“福狮”；本条以石湾窑条为唯一承载单元，属单链接条目，需在 enrich 阶段补足石湾陶塑或日用陶器条。",
  3603, 3603, "line", [3603], ["b0430"], "3. 陶瓷业的繁荣与品种的发展｜2）陶器品种与工艺特色")

C("cand-06-55", "historiographic_claim",
  "夏燕靖认为，明清建筑是继秦汉建筑和唐宋建筑之后我国古代建筑的最后一个高峰，其高度发达的建筑设计、建筑彩画和园林艺术为后世留下了极其宝贵的财富。",
  "Xia Yanjing holds that Ming-Qing architecture was the last peak of ancient Chinese architecture after the Qin-Han and Tang-Song peaks, and that its highly developed architectural design, polychrome painting, and garden art left an extremely valuable legacy.",
  "high",
  ["04-knowledge/units/works/beijing-zijincheng.md",
   "04-knowledge/units/works/ming-shisanling.md",
   "04-knowledge/units/works/budala-gong.md"],
  "候选作 periodization，路由 historiographic；断言取 L3625；候选跨度 L3623-L3626 含节题与总述；南京、北京城池宫殿、金刚宝座塔、大报恩寺塔、布达拉宫、札什伦布寺、外八庙、《工程作法》与南北彩画派系留在 L3629-L3680。本条为分期总判断，三例证只作实例链接，不把各建筑成就并入。",
  3625, 3625, "line", [3625], ["b0432"], "4. 建筑设计与建筑彩画艺术")

C("cand-06-56", "interpretive_claim",
  "夏燕靖认为，清雍正十二年颁行的《工程作法》列举二十七种建筑物的各种构件尺寸与作法，并规定斗栱、装修、石作、瓦作、土作等做法和用工用料；它虽可加快设计施工进度，却不利于建筑设计的多样化发展，造成官式建筑装饰日趋繁缛、雕梁画栋。",
  "Xia Yanjing argues that the Gongcheng Zuofa promulgated in the twelfth year of the Yongzheng reign listed accurate dimensions and methods for the components of twenty-seven building types and regulated the making and labour-and-material quotas of bracket sets, joinery, stonework, tilework, and earthwork; while it could speed design and construction, it discouraged diversification in architectural design and led official buildings toward ever more elaborate decoration and painted beams.",
  "high",
  ["04-knowledge/units/publications/gongcheng-zuofa.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3658；候选跨度 L3627-L3659 含明南京、北京宫城营造文献与雷发达知识链接；本条只取对《工程作法》的利弊评价，明初宫室“朴素不为雕饰”、永乐迁都、正统复建与布达拉宫未并入。来源作《工程作法》，现行工程做法条并列《工程做法》与《工程作法》两名，本条保留来源用字。",
  3658, 3658, "line", [3658], ["b0433"], "4. 建筑设计与建筑彩画艺术｜1）建筑设计")

C("cand-06-57", "interpretive_claim",
  "夏燕靖认为，中国园林设计以曲折多变的造型和自然野逸在世界园林设计史上享有崇高地位；早在七八世纪已传到日本，十八世纪又远传欧洲，英、荷、德、法等国园林设计者纷纷仿效，中国园林因此被誉为世界园林之母。",
  "Xia Yanjing holds that Chinese garden design, with its winding, changing forms and natural rusticity, occupies a lofty place in the history of world garden design; it reached Japan as early as the seventh or eighth century and spread to Europe in the eighteenth, where English, Dutch, German, and French designers imitated it, earning Chinese gardens the title mother of the world's gardens.",
  "medium",
  ["04-knowledge/units/publications/yuan-ye.md",
   "04-knowledge/units/persons/ji-cheng.md",
   "04-knowledge/units/terms/jiangnan-yuanlin.md",
   "04-knowledge/units/works/zhuozhengyuan.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3706；候选跨度 L3699-L3707 含知识链接框题、苏州园林图注与《园冶》成书说明；同段“因借”之法、“以有限面积造无限空间”与《园冶》崇祯四年成稿留在 L3704 与 L3772。“世界园林之母”为来源评价，未给具体传播证据与年代依据，保留 medium。",
  3706, 3706, "line", [3706], ["b0438"], "4. 建筑设计与建筑彩画艺术｜3）园林设计")

C("cand-06-58", "evaluative_claim",
  "夏燕靖认为，清代宫廷与达官显贵使用的家具为追求富丽堂皇、华贵气派，滥用雕镂、镶嵌、彩绘、剔犀、堆漆等手法以及象牙、玉石、陶瓷、螺钿等材料，往往只重技巧、忽略效果，繁琐堆砌，破坏了家具的整体美感，背离了家具设计的实用简练原则。",
  "Xia Yanjing judges that the furniture used by the Qing court and high officials, in pursuit of sumptuous splendour, overused carving, inlay, painting, carved lacquer, and piled lacquer together with ivory, jade, ceramics, and mother-of-pearl, often valuing technique over effect and piling ornament upon ornament until the overall beauty was destroyed and the plain, practical principle of furniture design abandoned.",
  "high",
  ["04-knowledge/units/terms/qing-style-furniture.md",
   "04-knowledge/units/terms/qingdai-jiaju-sanda-mingzuo.md"],
  "候选作 interpretation，但断言主体是对清代宫廷家具装饰的高下评价，按 dominantly evaluative 路由 evaluative；断言取 L3735；候选跨度 L3731-L3736 含清家具体量、组合柜、折叠拆装、用材与苏作、广作、京作三大名作；民间家具“仍以实用、经济为主”的判断留在同段末，未并入。来源列举的剔犀、堆漆、螺钿等工艺名未逐条建链。",
  3735, 3735, "line", [3735], ["b0441"], "5. 家具种类与工艺设计｜2）清代家具的设计特色")

C("cand-06-77", "interpretive_claim",
  "夏燕靖指出，明万历年间彩色画风行，多为红、黑或五色套版印刷，先在一块木板上涂几种颜色彩印；1605 年刻印的《程氏墨苑》比欧洲第一次套色印刷早百余年。",
  "Xia Yanjing notes that colour printing flourished in the Wanli period, mostly in red-and-black or five-colour block printing in which several colours were applied to a single block, and that the Chengshi Moyuan printed in 1605 preceded Europe's first colour printing by more than a century.",
  "medium",
  ["04-knowledge/units/publications/chengshi-moyuan.md",
   "04-knowledge/units/procedures/duanban-taoyin.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3766；候选跨度仅 L3766，同段另述短版、拱花、《萝轩变古笺谱》与《十竹斋画谱》《笺谱》；本条只取《程氏墨苑》的中西年代比较，短版与拱花另见后续条目。来源未给欧洲第一次套色印刷的年代与依据，“早百余年”保留作者判断，medium。程氏墨苑条记五册均以之为中国彩色套印最早标本，与来源一致；短版套印条只承载技法背景。",
  3766, 3766, "line", [3766], ["b0443"], "7. 印刷工艺与印刷设计")


def main():
    assert len(ROWS) == 18, len(ROWS)
    out = []
    for i, row in enumerate(ROWS):
        row["claim_id"] = "claim-%04d" % (220 + i)
        sp = row["source"]["source_span"]
        assert 3377 <= sp["line_start"] <= sp["line_end"] <= 3805, row["claim_id"]
        assert sp["key_lines"] and all(sp["line_start"] <= k <= sp["line_end"] for k in sp["key_lines"]), row["claim_id"]
        assert sp["block_ids"], row["claim_id"]
        assert sp["span_kind"] in {"line", "contiguous", "bounded"}, row["claim_id"]
        if sp["span_kind"] == "line":
            assert sp["line_start"] == sp["line_end"], row["claim_id"]
        for p in row["supported_by"]:
            assert p.startswith("04-knowledge/units/"), p
            assert (ROOT / p).exists(), p
        out.append(row)
    (ROOT / "_zn_claim_xyj09h_rows.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    print(json.dumps({
        "claims": len(out),
        "with_support": sum(1 for r in out if r["supported_by"]),
        "links": sum(len(r["supported_by"]) for r in out),
        "distinct_support": len({p for r in out for p in r["supported_by"]}),
        "types": dict(Counter(r["claim_type"] for r in out)),
        "confidence": dict(Counter(r["confidence"] for r in out)),
        "span_kinds": dict(Counter(r["source"]["source_span"]["span_kind"] for r in out)),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
