# 2026-10-26-2009zhaonong-units-batch-f 收口

## 一、范围与目标

- 来源：赵农《中国艺术设计史》（高等教育出版社，2009），`doc_id: 2009-zhaonong-zhongguo-yishu-shejishi`。
- 范围：第六章「繁盛的浮华——隋唐时期的设计」L4108–L4941，共 834 行，九节。
- 候选：91 条 unit 候选，全部完成检索、语义裁定、类型化写回与独立复读。
- 目标：把隋唐章的城桥、印刷书籍、农具家具、货币仪器、纺织服饰、雕刻陶瓷、金银器与行业管理，转为可追踪的知识元。
- 边界：`03基础书籍-md文档/` 只读；不 commit、不 push；单主线 `main`。

## 二、覆盖与复读

全章按节逐段阅读，候选分布与写回如下：

| 节 | 行段 | 候选 | 写回要点 |
|---|---|---|---|
| 第一节 绪论 | L4110–L4173 | 9 | 武则天、玄奘、《大唐西域记》、敦煌学、长安总述 |
| 第二节 城市与建筑 | L4174–L4314 | 11 | 宝带桥、天津桥、小雁塔、四门塔、栖霞寺舍利塔、千寻塔 |
| 第三节 印刷与书籍 | L4315–L4476 | 20 | 石经四目、蔡邕、硬黄纸、玉版宣、薛涛笺、雕版佛经与装帧 |
| 第四节 农具与家具 | L4477–L4575 | 15 | 曲辕犁、筒车、《耒耜经》、椅子、杌凳、屏风 |
| 第五节 纺织与服饰 | L4576–L4621 | 5 | 斜织机、缫车、花纱、胡装、袍衫 |
| 第六节 雕刻与陶瓷 | L4622–L4779 | 19 | 唐陵、乐山大佛、海通、经变、书法碑刻、四大名砚 |
| 第七节 金银器与铜镜 | L4780–L4848 | 6 | 何家村窖藏、被中香炉、银熏球 |
| 第八节 设计行业管理 | L4849–L4909 | 4 | 少府监、短番匠、行会、缭绫名目 |
| 第九节 结论 | L4910–L4941 | 2 | 唐代设计总结中的器物与制度判断 |

独立语义复读对象为全部 69 个写回文件（63 新建 + 6 更新），逐个 dump frontmatter 选键与「描述／核心内容／层级位置／相关知识元／验证状态」五节，与赵农册原文逐条对照；跨册条目另回查夏燕靖 2016 册 L2512–L2533、L2855 等行。复读中发现的问题与修正见第八节。

三重机械审计（写回与修正后重跑）：

| 审计 | 范围 | 结果 |
|---|---|---|
| `_zn_struct.py` | 69 个写回文件 | `problems: 0` |
| `_zn_audit.py` | 六册合并语料回查 | `findings: 0` |
| `_zn_audit_strict.py` | 仅赵农册、仅单源新建 | `findings: 0` |

## 三、91 条裁定总表

| # | 实体 | 裁定 | 目标 | 依据摘要 |
|---|---|---|---|---|
| 1 | 蔡邕 | create | `persons/cai-yong.md` | L4342 记蔡邕主持熹平石经刊刻、书丹上石；来源未给生卒、官职与其他著作。人物以石经事功立条。 |
| 2 | 葛洪 | create | `persons/ge-hong.md` | L4574 记东晋葛洪参照老鹰飞行、以牛皮革和枣木制飞行器、腹置动力器械但未见实施；来源未提《抱朴子》。 |
| 3 | 海通和尚 | create | `persons/haitong-heshang.md` | L4681 记其发起开凿乐山大佛；L4683 记传说立志造像、化缘遭州官戏弄、手抠双目明志；除发起外均为来源标明的传说。 |
| 4 | 韩志和 | create | `persons/han-zhihe.md` | L4574 记传说唐代工匠韩志和制飞行器飞 100 尺、飞行 450 尺，并能作飞动龙床、飞鹤等器具；“传说”限定明确。 |
| 5 | 李淳风 | create | `persons/li-chunfeng.md` | L4570 仅一句记其改造北魏铁浑仪、633 年制成浑天黄道铜仪；材料薄。 |
| 6 | 柳公权 | create | `persons/liu-gongquan.md` | L4736 记柳公权以《玄秘塔碑》《神策军碑》闻名，书“刚劲饱满、工稳清晰”，与颜书并称“颜筋柳骨”；来源仅一句。 |
| 7 | 僧一行 | create | `persons/seng-yixing.md` | L4146 记大衍历；L4570 记与梁令瓒于 725 年改进浑仪；L4572 记改造水运浑象、自动报时并制大衍历；三处互证。 |
| 8 | 韦诞 | create | `persons/wei-dan.md` | L4390 记三国时期韦诞既是造笔名家、也是制墨高手，贾思勰《齐民要术》载其“合墨法”，后世称其为制墨祖师；来源未及其他书艺与题署。 |
| 9 | 武则天 | create | `persons/wu-zetian.md` | L4132 作者评“雄才大略”；L4215 记其洛阳宫城建明堂并引《旧唐书·则天皇后纪》；L4217 记改号武周与热衷明堂；L4225 记天堂、通天宫、九鼎与乾元殿；L4291… |
| 10 | 玄奘 | create | `persons/xuanzang.md` | L4286 记俗姓陈、河南偃师人、少年出家、贞观元年（627）出发、前后 19 年、归国译经 74 部 1335 卷 1300 万字；L4284 记大雁塔为其存经场所；L414… |
| 11 | 颜真卿 | create | `persons/yan-zhenqing.md` | L4734 记颜真卿为开元进士、曾任平原太守、封鲁郡开国公、为人忠烈刚直，石刻有《多宝塔》《颜勤礼碑》《麻姑仙坛记》《东方朔画赞》《大唐中兴颂》等，并评“数量众多、结体丰厚、气… |
| 12 | 《大唐西域记》 | create | `publications/da-tang-xiyu-ji.md` | L4146 记其为中亚和南亚 110 多个国家地区漫游十六载之后的考察记录；L4286 评“资料详实、叙述生动”，为后世研究西域的珍贵文献。两条均直接述书。 |
| 13 | 《国史补》 | create | `publications/guo-shi-bu.md` | L4894 记李肇《国史补》所载越州妇女本不会织布、浙江东道节度使出钱让未婚士兵娶北方织妇、每年数百名北方纺织巧手到南方的故事；来源未给成书年、卷数、体例与版本。 |
| 14 | 《金刚经》（咸通九年本） | create | `publications/jingangjing-868.md` | L4162 与 L4417 记咸通九年（868）王玠为二亲敬造普施的《金刚经》刻本，是现存最早有明确纪年的雕版印刷品之一；题记完整。 |
| 15 | 《开元杂报》 | create | `publications/kaiyuan-zabao.md` | L4439 记唐玄宗开元年间（公元713年起）唐朝官方出版中国最早的报纸《开元杂报》，属政府公文邸报性质，并称其标志印刷术进入新闻领域；材料一段。 |
| 16 | 《耒耜经》 | create | `publications/leisi-jing.md` | L4493 记陆龟蒙（？—约881）、姑苏人、与皮日休并称“皮陆”，《耒耜经》为中国最早记载和研究农具的书籍，并记爬（耙）、砺、夯等农具。 |
| 17 | 《妙法莲花经》（吐鲁番出土本） | create | `publications/miaofa-lianhua-jing.md` | L4427 记吐鲁番出土《妙法莲华经》印本残卷，为唐代西州雕印实物；来源作“妙法莲花经”，通行作“莲华”。 |
| 18 | 《女则》 | create | `publications/nvze.md` | L4431 记传说唐太宗为纪念长孙皇后雕版印刷其著述《女则》10 卷，并称“若是事实，应当是最早的雕版印刷书籍”；来源只此一句且带传说限定。 |
| 19 | 《陀罗尼经咒》 | create | `publications/tuoluoni-jingzhou.md` | L4425 记 1944 年成都唐墓出土《陀罗尼经咒》印本、卞家刻印，为早期民间雕版印刷实物。 |
| 20 | 《王仁昫刊谬补缺切韵》 | create | `publications/wang-renxu-qieyun.md` | L4469 记《王仁昫刊谬补缺切韵》为唐代韵书、采用旋风装，是现存旋风装实物依据。 |
| 21 | 《无垢净光大陀罗尼经》 | create | `publications/wugou-jingguang-daluoni-jing.md` | L4423 记 1966 年韩国庆州佛国寺释迦塔发现的《无垢净光大陀罗尼经》印本，来源以“推断”“应是”称其为唐长安印本。 |
| 22 | 敦煌学 | create | `terms/dunhuangxue.md` | L4705 记莫高窟保存唐代社会文献、经近代西方学者发掘利用引起中国学术界重视、成为现代“敦煌学”的学术基础；仅两句。 |
| 23 | 梵夹装 | create | `terms/fanjia-zhuang.md` | L4463-L4465 记梵夹装（又称梵荚装）于隋朝从印度传入，将贝多树叶上抄写的佛经以木板或竹板夹之、用绳穿串；并影响经折装。 |
| 24 | 飞钱 | create | `terms/feiqian.md` | L4554 记飞钱为类似汇票的异地汇兑，唐宪宗年间地方政府在京城设进凑院，商人存钱领凭证、返乡兑付；“本阜”“进凑院”均疑误。 |
| 25 | 花灯 | create | `terms/huadeng.md` | L4843-L4845 记花灯又叫灯彩、为汉代以来元宵节民俗，述汉文帝与正月十五的相传、上元与元宵称谓、佛教燃灯，以及盛唐上元灯节的灯火、鱼灯龙灯灯楼。 |
| 26 | 花纱 | create | `terms/huasha.md` | L4592-L4594 记唐代纬锦与花纱产量提高、纬锦以纬线显花，花纱指纱质印染，并有绞缬、夹缬、蜡缬、介质印花四法；总述手工印染传承。 |
| 27 | 浑仪 | create | `terms/hunyi.md` | L4570 记浑仪定义、李淳风改造北魏铁浑仪并于 633 年制浑天黄道铜仪、僧一行与梁令瓒于 725 年改进；仪器史脉络完整。 |
| 28 | 胡装 | create | `terms/huzhuang.md` | L4618-L4620 记盛唐妇女翻领细袖上衣、卷沿胡帽与西域服饰影响，引《旧唐书·舆服志》“贵人御馔，尽供胡食，士女皆竟衣胡服”“开元初，从驾宫人骑马者，皆著胡帽”及元稹诗，… |
| 29 | 经变 | create | `terms/jingbian.md` | L4701-L4703 记唐代莫高窟画风由“秀骨清像”转“丰满华丽”、经变故事充满人间欢乐、菩萨飞天佛陀力士成为唐代社会影像；来源未下正式定义。 |
| 30 | 经折装 | create | `terms/jingzhe-zhuang.md` | L4461、L4463-L4467 记经折装即折子装，受卷轴装与梵夹装影响，将佛经卷折叠成一定宽度、前后用硬纸或木板夹护裱糊为书皮，因佛经流行而兴起；材料充分。 |
| 31 | 卷轴装 | create | `terms/juanzhou-zhuang.md` | L4443-L4445 记卷轴装以纸卷、轴、褾、带组成，是唐代以前书籍主要装帧；结构完整。 |
| 32 | 开元通宝 | create | `terms/kaiyuan-tongbao.md` | L4539-L4541 记武德四年（621）废五铢、铸开元通宝、“意即新世开元，流通宝货”，一枚一钱、十枚一两、废铢制、厘分钱两十进位、钱成固定重量单位，通宝钱共流通 1290… |
| 33 | 曲辕犁 | create | `terms/quyuan-li.md` | L4481 详记江东犁即曲辕犁：将汉代直长辕改为短曲辕、二牛抬杠改一牛耕犁，并改变犁辕、犁箭、犁梢、犁底，使犁架变小、操作简便、深浅自如；L4152 绪论并举。形制演变完整。 |
| 34 | 缫车 | create | `terms/saoche.md` | L4590 记缫车为抽丝工具、战国出现手摇轱辘雏形、唐代手摇缫车广泛使用，并引陆龟蒙“每和烟雨掉缫车”、王建“檐头索索缫车鸣”。 |
| 35 | 石经 | create | `terms/shijing.md` | L4338-L4340 总述石经刊刻传统与固定经学文本的功能，L4342、L4344、L4346 分记熹平、正始、开成三刻；总述足以立术语条，三刻各立 works。 |
| 36 | 书帖 | create | `terms/shutie.md` | L4552、L4548 记唐代西市钱庄存钱、商人以书帖列交易账目与款项、收款者持帖到钱庄支取现钱，来源类比支票；两句被图版与页眉隔断。 |
| 37 | 四大名砚 | create | `terms/si-da-ming-yan.md` | L4396 以合称记唐代四大名砚并逐一列名；既有 terms/duan-yan.md、terms/she-yan.md 只及单砚，无合称条。 |
| 38 | 筒车 | create | `terms/tongche.md` | L4483 记水转筒车以竹木作轮、架于水边、下轮浸水、借水力转动、小水桶携水上升注入高渠；L4152 与曲辕犁并举。 |
| 39 | 杌凳 | create | `terms/wu-deng.md` | L4516-L4520 记床榻前踏登与几相似后成凳、“机本有树桩之意”、南北朝杌凳联称、隋唐高足坐具流行，并记唐画《捣练图》《簪花仕女图》、高矮方圆半圆凳与长凳。 |
| 40 | 旋风装 | create | `terms/xuanfeng-zhuang.md` | L4469 记旋风装吸收经折装与卷轴装优点、单页折起双面文字后从右向左排压、宛如鱼鳞或旋风，所有书页装裱于一张长纸可卷起；并明记故宫博物院藏唐抄本《王仁昫刊谬补缺切韵》为典型实… |
| 41 | 薛涛笺 | create | `terms/xuetao-jian.md` | L4388 记薛涛笺的创制、形制与用途，是唐代染色加工纸的专名；既有 terms/xuan-zhi.md 只记清代“仿薛涛笺”，未覆盖唐代原产。 |
| 42 | 颜筋柳骨 | create | `terms/yan-jin-liu-gu.md` | L4734-L4736 给两家书风评语与并称，未解释“筋”“骨”所指，也未给并称出处与最早用例；术语身份明确。 |
| 43 | 硬黄纸 | create | `terms/yinghuang-zhi.md` | L4382 记唐代黄纸中有一种加蜡处理的纸、非常名贵、称为“硬黄纸”，并记敦煌藏经洞唐人写经中就有这种纸；是唐代加工纸专名。 |
| 44 | 椅子 | create | `terms/yizi.md` | L4506-L4510 记隋唐出现椅子、从西域渐入、由佛教高僧宝座转人民间、椅本意为倚、改变坐姿与身体重心，并记唐高元圭墓壁画与敦煌壁画中的中原化样式。 |
| 45 | 玉版宣 | create | `terms/yuban-xuan.md` | L4386 记唐代舒州与宣州造纸之地隔江相望，此时产生以檀皮为原料的名贵“玉版宣”纸；纸名、原料与产地构成独立术语身份，既有纸类条未收。 |
| 46 | 帙 | create | `terms/zhi-book-wrapper.md` | L4457 记帙为包裹卷轴书的书衣，以数卷为一帙；是卷轴装的配套护书用具。 |
| 47 | 走马灯 | create | `terms/zouma-deng.md` | L4847 一句记唐代走马灯利用灯光热气流推动灯罩内人物马形流转，产生光怪陆离的灯影效果。 |
| 48 | 宝带桥 | create | `works/baodai-qiao.md` | L4266 记 816 年（唐元和十一年）苏州葑门外六里建多孔石拱桥，刺史王仲舒捐宝带资助得名；L4271 记长 317 米、53 孔、两端 6.1 米、中央 4.1 米、最大… |
| 49 | 崇圣寺千寻塔 | create | `works/chongsheng-si-qianxun-ta.md` | L4303-L4309 记云南大理崇圣寺千寻塔为唐代密檐式塔、高 16 层、约 58 米、外观柔美简洁，并以“造型雅致庆典”评之；16 层与 58 米两处被图版与页眉隔断。 |
| 50 | 《夫子庙堂碑》 | create | `works/fuzi-miaotang-bei.md` | L4728 记虞世南《夫子庙堂碑》为武德九年（公元629年），并以“方中见圆、平中见奇、笔力秀健、精气饱满”评之；原文纪年与公元换算不符。 |
| 51 | 《九成宫醴泉铭》 | create | `works/jiuchenggong-liquan-ming.md` | L4728 记欧阳询《九成宫醴泉铭》为贞观六年（632）立、欧阳询 75 岁奉唐太宗诏书，并以“笔力刚劲、峻利凝重、法度严谨”评之，有“唐楷之冠”称誉。 |
| 52 | 《开成石经》 | create | `works/kaicheng-shijing.md` | L4346 记开成二年（837）刻成十二经、立于长安国子监、碑石 114 块、约 65 万字；材料完整。 |
| 53 | 乐山大佛 | create | `works/leshan-dafo.md` | L4681-L4685 记开元年间海通发起、前后 90 年、依山造像、高 71 米、三江汇流凌云山、袈裟袒胸倚坐、传说抠目明志、“石破山开，大佛凿成”与民族精神评语。 |
| 54 | 《龙藏寺碑》 | create | `works/longzang-si-bei.md` | L4726 记隋唐立碑风气与碑额、碑身、碑座，隋《龙藏寺碑》为开皇六年（586），有“整密瘦健”“一线之延”评语与“隋碑第一”俗称，并影响初唐虞世南、褚遂良。 |
| 55 | 《麓山寺碑》 | create | `works/lushan-si-bei.md` | L4728 记李邕《麓山寺碑》为开元十八年（公元703年）所立，有“李北海第一”说法，并以“天姿矫健、英华高卓”评之；原文纪年与公元换算不符。 |
| 56 | 栖霞寺舍利塔 | create | `works/qixia-si-sheli-ta.md` | L4301 一句记 601 年（隋文帝仁寿元年）始建、南唐重建、八角五层密檐式、南方佛塔秀丽玲珑样式。 |
| 57 | 水运浑天仪（水运浑象） | create | `works/shuiyun-huntianyi.md` | L4572 记僧一行与梁令瓒改造张衡水运浑象、注水激轮使一日一夜天转一周、安装自动报时器成原始天文钟、后因失养锈蚀停转；L4568 小节名作“水运浑天仪”。 |
| 58 | 四门塔 | create | `works/simen-ta.md` | L4299 一段记现存最早的仿木单檐石塔、济南青龙山神通寺、方形青石、高 15 米、塔心柱佛像、须弥座山华蕉叶相轮宝顶、四面圆形拱门与“隋代佛塔的典范”评语。 |
| 59 | 天津桥 | create | `works/tianjin-qiao.md` | L4273 一句记 605 年（隋大业元年）洛阳天津桥为铁链联接船只组成的浮桥，与西安灞桥并称隋唐天下闻名。 |
| 60 | 小雁塔 | create | `works/xiaoyan-ta.md` | L4295 记 707 年建、又称荐福寺塔、为纪念唐高宗而修、因规模小于大雁塔得名；L4297 记砖结构密檐式方塔、叠涩塔檐、原 15 层、明中期关中大地震坍顶两层、现存 13… |
| 61 | 《熹平石经》 | create | `works/xiping-shijing.md` | L4342 记熹平四年（175）蔡邕主持刊刻七经、立于洛阳太学门外、碑石 46 块、观览摹写者车乘日千余辆；材料完整。 |
| 62 | 《雁塔圣教序》 | create | `works/yanta-shengjiao-xu.md` | L4728 记褚遂良《雁塔圣教序》为奉唐太宗之命而书，并以“婉媚遒逸、波拂如铁”评之；未给立碑年与碑址。 |
| 63 | 《正始石经》 | create | `works/zhengshi-shijing.md` | L4344 一句记正始年间以古文、篆、隶三体刻《尚书》《春秋》等，又称三体石经。 |
| 64 | 短番匠 | update | `institutions/jiangzuojian.md` | 更新 institutions/jiangzuojian.md：赵农 citation 补入 L4890，同书增列跨度，source_count 不变，version 加 1；… |
| 65 | 阎立德 | update | `persons/yan-lide.md` | 更新 persons/yan-lide.md：追加赵农 citation（L4148, L4192, L4200），source_count 1→2，version 1→2，c… |
| 66 | 斜织机 | update | `terms/jiaota-tizong-xiezhi-ji.md` | 更新 terms/jiaota-tizong-xiezhi-ji.md：追加赵农 citation（L4580, L4584），source_count 1→2，version… |
| 67 | 缭绫 | update | `terms/ling-silk.md` | 更新 terms/ling-silk.md：追加赵农 citation（L4900），source_count 2→3，version 1→2；新增民间名目条。 |
| 68 | 行头 | update | `terms/shougongye-hanghui.md` | 更新 terms/shougongye-hanghui.md：追加赵农 citation（L4904），source_count 1→2，version 1→2，confide… |
| 69 | 袍衫 | update | `terms/yuanling-paoshan.md` | 更新 terms/yuanling-paoshan.md：追加赵农 citation（L4610），source_count 2→3，version 1→2；保留旧说。 |
| 70 | 含元殿 | no_delta | `places/daxing-cheng.md` | 判 no_delta：殿为宫城构成，既有条已完整承载；来源未给台基尺度与殿身构架，不足以独立成 work 条。 |
| 71 | 太极宫 | no_delta | `places/daxing-cheng.md` | 判 no_delta：宫名沿革与朝政材料已被既有长安城条覆盖。 |
| 72 | 卢舍那大佛 | no_delta | `places/longmen-grottoes.md` | 判 no_delta：造像细节已被龙门石窟条覆盖。 |
| 73 | 明堂 | no_delta | `places/luoyang-cheng.md` | 判 no_delta：明堂为洛阳宫城中心建筑，既有条已完整承载形制与沿革。 |
| 74 | 南青北白 | no_delta | `places/xing-kiln.md` | 判 no_delta：格局判断已被邢窑、越窑两条覆盖。 |
| 75 | 唐陵 | no_delta | `places/zhaoling.md` | 判 no_delta：总述已分散于两陵条，无独立于两陵的新对象。 |
| 76 | 昭陵六骏 | no_delta | `places/zhaoling.md` | 判 no_delta：六骏全部细节已在昭陵条内。 |
| 77 | 顺陵走狮 | no_delta | `places/zhaoling.md` | 判 no_delta：石狮材料已被两陵条覆盖。 |
| 78 | 绳床 | no_delta | `terms/huchuang.md` | 判 no_delta：绳床材料已被胡床条完整覆盖。 |
| 79 | 镂空银熏球 | no_delta | `works/tang-yin-xiangnang.md` | 判 no_delta：器物形制、机环结构与技术谱系均已在既有条内。 |
| 80 | 敞肩型 | no_delta | `works/zhaozhou-qiao-595-605.md` | 判 no_delta：该词在本章用于赵州桥，无独立于桥条的新材料。 |
| 81 | 旅人桥 | no_delta | `works/zhaozhou-qiao-595-605.md` | 判 no_delta：桥名与文献均属赵州桥条已有材料。 |
| 82 | 被中香炉 | rejected | `persons/ding-huan.md` | 判 rejected：重复实体，canonical 取 persons/ding-huan.md；本条不另建。 |
| 83 | 金花鹦鹉提梁银罐 | rejected | `places/hejiacun-jiaocang.md` | 判 rejected：清单列名与图注不足以立 work 条；材料保留在何家村条。 |
| 84 | 金花八曲银杯 | rejected | `places/hejiacun-jiaocang.md` | 判 rejected：材料不足，且与既有器物的同一性未定；不立条、不并入 2016 册条目。 |
| 85 | 乾陵翼马 | rejected | `places/qianling.md` | 判 rejected：图注材料不足以立 work 条；不写回。 |
| 86 | 《金刚经》 | rejected | `publications/jingangjing-868.md` | 判 rejected：与 cand-07-02 重复，canonical 为 publications/jingangjing-868.md；不另建泛称条。 |
| 87 | 《纪泰山铭》 | rejected | `terms/bei-xue.md` | 判 rejected：图注材料不足以成条，不写回。 |
| 88 | 曲辕犁 | rejected | `terms/quyuan-li.md` | 判 rejected：重复归类，canonical 取 cand-07-19 的 terms/quyuan-li.md；本候选不另建 work 条。 |
| 89 | 菩萨身躯（图6-56） | rejected | `terms/shikusi.md` | 判 rejected：图注材料不足以成条，不写回。 |
| 90 | 唐三彩骆驼乐伎俑 | rejected | `terms/tang-sancai.md` | 判 rejected：图注材料不足以立 work 条；不写回。 |
| 91 | 筒车 | rejected | `terms/tongche.md` | 判 rejected：重复归类，canonical 取 cand-07-20 的 terms/tongche.md；本候选不另建 work 条。 |

## 四、63 条新建分型

按类型：terms 26、works 16、persons 11、publications 10。按维度：B 40、C 14、D 6、A 3（A 仅玄奘、《大唐西域记》、敦煌学三条，属史料与学术基础，不涉及史学方法）。按置信度：medium 33、low 30。

- **terms（26）**：玉版宣、薛涛笺、硬黄纸、四大名砚、石经、敦煌学、卷轴装、帙、经折装、梵夹装、旋风装、曲辕犁、筒车、椅子、杌凳、开元通宝、书帖、飞钱、浑仪、缫车、花纱、胡装、经变、颜筋柳骨、花灯、走马灯。
- **works（16）**：宝带桥、天津桥、小雁塔、四门塔、栖霞寺舍利塔、崇圣寺千寻塔、熹平石经、正始石经、开成石经、乐山大佛、水运浑天仪、龙藏寺碑、九成宫醴泉铭、夫子庙堂碑、雁塔圣教序、麓山寺碑。
- **persons（11）**：武则天、玄奘、蔡邕、韦诞、李淳风、僧一行、葛洪、韩志和、海通和尚、颜真卿、柳公权。
- **publications（10）**：《大唐西域记》《国史补》《金刚经》868 本、《开元杂报》《耒耜经》《妙法莲华经》吐鲁番本、《女则》《陀罗尼经咒》《王仁昫刊谬补缺切韵》《无垢净光大陀罗尼经》。

## 五、6 条更新

| 目标 | 变动 | 结果 |
|---|---|---|
| `persons/yan-lide.md` | 追加赵农 L4148、L4192、L4200 | source_count 1→2，version 1→2，confidence low→medium；补长安城设计监工身份，与洪州造船并列 |
| `terms/jiaota-tizong-xiezhi-ji.md` | 追加赵农 L4580、L4584 | source_count 1→2，version 1→2；补唐代斜织机的提花与踏板记载 |
| `terms/yuanling-paoshan.md` | 追加赵农 L4610 | source_count 2→3，version 1→2；唐代袍衫形制与旧说并列 |
| `institutions/jiangzuojian.md` | 赵农 citation 增列 L4890 | source_count 6 不变，version 2→3；扩写短番匠轮番服役 |
| `terms/shougongye-hanghui.md` | 追加赵农 L4904 | source_count 1→2，version 1→2；补行肆、行头、牙人与两京行数 |
| `terms/ling-silk.md` | 追加赵农 L4900 | source_count 2→3，version 1→2；补缭绫名目与民间纺织基础 |

## 六、12 条 no_delta

均已存在完整承载条目，来源未给独立于既有条目的新材料：

- 含元殿、太极宫 → `places/daxing-cheng.md`
- 明堂 → `places/luoyang-cheng.md`
- 敞肩型、旅人桥 → `works/zhaozhou-qiao-595-605.md`
- 绳床 → `terms/huchuang.md`
- 唐陵、昭陵六骏、顺陵走狮 → `places/zhaoling.md`
- 卢舍那大佛 → `places/longmen-grottoes.md`
- 南青北白 → `places/xing-kiln.md`
- 镂空银熏球 → `works/tang-yin-xiangnang.md`

## 七、10 条 rejected

- **重复归类或重复实体（4）**：曲辕犁（work 候选并入 `terms/quyuan-li.md`）、筒车（work 候选并入 `terms/tongche.md`）、《金刚经》泛称（并入 `publications/jingangjing-868.md`）、被中香炉（并入 `persons/ding-huan.md`）。
- **图注或清单材料不足（6）**：菩萨身躯（图 6-56）、〈纪泰山铭〉、金花鹦鹉提梁银罐、金花八曲银杯、唐三彩骆驼乐伎俑、乾陵翼马。这些候选只有图注、清单列名或一句描述，不足以立条；材料保留在原条目的图版说明或窖藏条目中，不另建 KU。

## 八、语义复读修正与原文疑误

### 维度修正

初稿把「在设计史叙述中的位置」「审美评价」「信仰背景」「史料依据」系统性归入 A 维度，违反 `01-domain/dimension-registry.md` 对 A 的边界（「处理如何写设计史，不是设计思想史本身」）。复读后定向修正 16 个文件：

- 删除次要 A 维度 14 个：小雁塔、曲辕犁、《耒耜经》、椅子、浑仪、水运浑天仪、李淳风、僧一行、葛洪、武则天、经变、颜筋柳骨、柳公权、颜真卿。
- 乐山大佛：次要 A → E（佛教东渐与跨文化宗教传播）。
- 海通和尚：primary A → B，次要维度清空（发起开凿属造像工程，来源未涉史学方法）。

保留 A 的仅玄奘、《大唐西域记》、敦煌学三条。

### 内容修正

- `works/zhengshi-shijing.md`：曹芳是正始年间的帝号纪年参照，不是「主持者」；改为「时代与帝号」。
- `persons/cai-yong.md`：`occupation` 由「书法家」改为「《熹平石经》书写者」；八分书归于今存残石，不直接归于蔡邕所书。
- `terms/yinghuang-zhi.md`：删去与硬黄纸无文本关联的《历代名画记》链接，改链玉版宣。
- `publications/jingangjing-868.md`：`edition` 由「卷轴」改为「7纸连接印本」，不替来源判定装帧形制。
- `works/simen-ta.md`：标题去掉嵌套括号，统一为「四门塔（Simen Pagoda）」。
- `works/chongsheng-si-qianxun-ta.md`：`dimensions` 由「高16层」改为「16层，约58米」，保留正文引文原样。
- 19 个文件的「L1-L7」统一为全库体例「L1–L7」。

### 原文疑误与边界

- 「造型雅致庆典」原文如此，「庆典」疑为「典雅」之误，照录标疑，不径改。
- 夏燕靖 2016 册作「闫立德」，赵农 2009 册作「阎立德」，两册并存，标题取通行字并设 aliases。
- 图 6-20 开成石经、图 6-22 金刚经扉页等图版未核，相关条目只写文字所载，不据图补写构图、人物数量与刻工。
- 候选 `source_span` 粗于实际引用行：本章候选并集为 L4110–L7124，因薛涛笺合并 cand-07-163（远端 L5038）、四大名砚合并 cand-10-84（远端 L7124）、小雁塔合并 cand-07-126（L4909）三条跨章合并候选而超出本章。manifest 的 `spans` 记本章实读范围 L4108–L4941，另设 `candidate_spans_union` 与说明，避免把远端行冒充为本包复读内容。

## 九、状态与下一跳

- 工作包状态：`applied`；决策链 91 条全部落账（create 63、update 6、no_delta 12、rejected 10）。
- 生成态：`build_discovery_index.py` 重建后 applied 1899、no_delta 183、rejected 834、needs_evidence 2423；`build_translation_index.py` 与 `run_sync_closure.py --refresh-generated --full` 通过（250 tests + 16 subtests）。
- 未做：未 commit、未 push；`--check-generated` 在工作树未提交时预期为 `blocked_pending_commit`。
- 下一跳：赵农册第七章「文弱的精湛——五代两宋时期的设计」L4942–L5824，126 条 unit 候选；后续依次第八章 63 条、第九章 156 条、第十章 113 条、总结 9 条，再转 2010 田自秉与 2011 李立新。
