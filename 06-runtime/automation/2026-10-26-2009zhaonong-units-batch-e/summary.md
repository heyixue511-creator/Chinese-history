# 2009 赵农《中国艺术设计史》— 第五章 unit 批次（batch-e）

- 工作包：`2026-10-26-2009zhaonong-units-batch-e`
- 来源（只读）：`03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md`
- doc_id：`2009-zhaonong-zhongguo-yishu-shejishi`
- 日期：2026-10-26
- 候选范围：第五章（魏晋南北朝）L3258-L4095 内的 88 条 unit 候选（编号混有 `cand-05-*` 与 `cand-06-*`，章节归属以 `payload.source_span.chapter` 为准）
- 结果：create 77、update 4（4 个文件）、no_delta 5、rejected 2
- 语义验收：Agent 逐条复读全部 88 条候选，并独立复读 77 个新建条目与 4 个更新条目；未使用外部平台

## 一、裁定汇总

| 候选 | 实体 | 动作 | 目标 |
|---|---|---|---|
| cand-05-39 | 魏晋玄学 | create | `terms/xuanxue.md` |
| cand-05-40 | 南秀北雄 | create | `terms/nan-xiu-bei-xiong.md` |
| cand-05-45 | 诸葛亮 | create | `persons/zhuge-liang.md` |
| cand-05-49 | 翻车（龙骨水车） | create | `works/fanche-longgu-shuiche.md` |
| cand-05-51 | 千里船 | create | `works/qian-li-chuan.md` |
| cand-05-52 | 牛车 | create | `terms/niu-che.md` |
| cand-05-55 | 剡藤纸 | create | `terms/shan-teng-zhi.md` |
| cand-05-57 | 《博物志》 | create | `publications/bo-wu-zhi.md` |
| cand-05-60 | 行书 | create | `terms/xing-shu.md` |
| cand-05-63 | 碑学 | create | `terms/bei-xue.md` |
| cand-05-64 | 魏碑 | create | `terms/wei-bei.md` |
| cand-05-65 | 《天发神谶碑》 | create | `works/tian-fa-shen-chen-bei.md` |
| cand-05-66 | 《石门铭》 | create | `works/shi-men-ming.md` |
| cand-05-67 | 《张猛龙碑》 | create | `works/zhang-meng-long-bei.md` |
| cand-05-69 | 王羲之 | create | `persons/wang-xi-zhi.md` |
| cand-05-71 | 陆机 | create | `persons/lu-ji.md` |
| cand-05-72 | 《平复帖》 | create | `works/ping-fu-tie.md` |
| cand-05-73 | 《兰亭集序》 | create | `works/lan-ting-ji-xu.md` |
| cand-05-78 | 青瓷谷仓罐 | create | `works/qing-ci-gu-cang-guan.md` |
| cand-05-82 | 匣钵 | create | `terms/xia-bo.md` |
| cand-05-84 | 冕冠与冕旒 | create | `terms/mian-guan-mian-liu.md` |
| cand-05-87 | 襦 | create | `terms/ru.md` |
| cand-05-88 | 木屐（谢公屐） | create | `terms/mu-ji.md` |
| cand-05-89 | 《抱朴子》 | create | `publications/bao-pu-zi.md` |
| cand-05-91 | 假髻 | create | `terms/jia-ji.md` |
| cand-05-92 | 黛 | create | `terms/dai.md` |
| cand-05-93 | 《洛神赋图》 | create | `works/luo-shen-fu-tu.md` |
| cand-05-95 | 金墉城 | no_delta | `places/luoyang.md` |
| cand-05-100 | 铜雀台 | no_delta | `places/yecheng.md` |
| cand-05-103 | 《洛阳伽蓝记》 | create | `publications/luo-yang-qie-lan-ji.md` |
| cand-05-114 | 草书（今草） | create | `terms/jin-cao.md` |
| cand-05-115 | 《司马升墓志铭》 | create | `works/si-ma-sheng-mu-zhi-ming.md` |
| cand-05-116 | 《禅国山碑》 | create | `works/chan-guo-shan-bei.md` |
| cand-05-117 | 《爨宝子碑》 | create | `works/cuan-bao-zi-bei.md` |
| cand-05-118 | 《好大王碑》 | create | `works/hao-da-wang-bei.md` |
| cand-05-119 | 《广武将军碑》 | create | `works/guang-wu-jiang-jun-bei.md` |
| cand-05-120 | 《爨龙颜碑》 | create | `works/cuan-long-yan-bei.md` |
| cand-05-121 | 《瘗鹤铭》 | create | `works/yi-he-ming.md` |
| cand-05-122 | 《张黑女墓志》 | create | `works/zhang-hei-nv-mu-zhi.md` |
| cand-05-123 | 《敬史君碑》 | create | `works/jing-shi-jun-bei.md` |
| cand-05-124 | 《泰山经石峪金刚经》 | create | `works/tai-shan-jing-shi-yu-jin-gang-jing.md` |
| cand-05-125 | 《西岳华山碑》 | create | `works/xi-yue-hua-shan-bei.md` |
| cand-05-126 | 袄 | create | `terms/ao.md` |
| cand-05-127 | 衫（两裆衫） | create | `terms/shan-liang-dang-shan.md` |
| cand-05-128 | 裘 | create | `terms/qiu.md` |
| cand-05-129 | 裙 | create | `terms/qun.md` |
| cand-05-130 | 王献之 | create | `persons/wang-xian-zhi.md` |
| cand-05-131 | 大氅 | create | `terms/da-chang.md` |
| cand-05-132 | 裤 | create | `terms/ku.md` |
| cand-06-01 | 金谷园 | create | `works/jin-gu-yuan.md` |
| cand-06-02 | 竹林七贤 | create | `terms/zhu-lin-qi-xian.md` |
| cand-06-03 | 《兰亭集序》（文献义） | rejected | `works/lan-ting-ji-xu.md` |
| cand-06-04 | 玄学 | rejected | `terms/xuanxue.md` |
| cand-06-06 | 榻 | update | `terms/han-ta.md` |
| cand-06-09 | 朱然墓黑红漆几 | create | `works/zhu-ran-mu-hei-hong-qi-ji.md` |
| cand-06-15 | 储具 | create | `terms/chu-ju.md` |
| cand-06-17 | 步障 | no_delta | `terms/ping-feng.md` |
| cand-06-18 | 琵琶 | create | `terms/pi-pa.md` |
| cand-06-19 | 阮咸 | create | `terms/ruan-xian.md` |
| cand-06-20 | 嵇康 | create | `persons/ji-kang.md` |
| cand-06-21 | 《声无哀乐论》 | create | `publications/sheng-wu-ai-le-lun.md` |
| cand-06-22 | 西凉乐 | create | `terms/xi-liang-yue.md` |
| cand-06-23 | 筚篥 | create | `terms/bi-li.md` |
| cand-06-24 | 羯鼓 | create | `terms/jie-gu.md` |
| cand-06-26 | 永宁寺 | create | `works/yong-ning-si.md` |
| cand-06-27 | 白马寺 | create | `works/bai-ma-si.md` |
| cand-06-29 | 浮图 | update | `terms/fota.md` |
| cand-06-32 | 中心塔柱式 | create | `terms/zhong-xin-ta-zhu-shi.md` |
| cand-06-36 | 昙曜五窟 | create | `works/tan-yao-wu-ku.md` |
| cand-06-40 | 古阳洞 | no_delta | `places/longmen-grottoes.md` |
| cand-06-41 | 宾阳洞 | no_delta | `places/longmen-grottoes.md` |
| cand-06-42 | 《帝后礼佛图》 | create | `works/di-hou-li-fo-tu.md` |
| cand-06-95 | 隐囊 | create | `terms/yin-nang.md` |
| cand-06-96 | 筌台 | create | `terms/quan-tai.md` |
| cand-06-97 | 案（几案） | update | `terms/an-furniture.md` |
| cand-06-98 | 承尘 | create | `terms/cheng-chen.md` |
| cand-06-100 | 帘子 | create | `terms/lian-zi.md` |
| cand-06-102 | 笛 | create | `terms/di.md` |
| cand-06-103 | 羌笛 | create | `terms/qiang-di.md` |
| cand-06-104 | 胡笳 | create | `terms/hu-jia.md` |
| cand-06-105 | 箜篌 | create | `terms/kong-hou.md` |
| cand-06-107 | 《斫琴图》 | create | `works/zhuo-qin-tu.md` |
| cand-06-108 | 阮籍 | create | `persons/ruan-ji.md` |
| cand-06-109 | 《乐论》 | create | `publications/yue-lun.md` |
| cand-06-110 | 郦道元 | create | `persons/li-dao-yuan.md` |
| cand-06-111 | 《水经注》 | create | `publications/shui-jing-zhu.md` |
| cand-06-112 | 南北响堂山石窟 | update | `places/xiangtangshan-shiku.md` |
| cand-06-113 | 义县万佛堂 | create | `works/yi-xian-wan-fo-tang.md` |

## 二、新建 77 条

### 分类构成

- person：7 条（诸葛亮、王羲之、王献之、陆机、嵇康、阮籍、郦道元）
- publication：6 条（《博物志》《抱朴子》《乐论》《声无哀乐论》《水经注》《洛阳伽蓝记》）
- work：28 条（翻车、千里船、平复帖、兰亭集序、洛神赋图、青瓷谷仓罐、金谷园、朱然墓黑红漆几、斫琴图、永宁寺、白马寺、昙曜五窟、义县万佛堂、帝后礼佛图，以及《天发神谶碑》《石门铭》《张猛龙碑》《司马升墓志铭》《禅国山碑》《爨宝子碑》《好大王碑》《广武将军碑》《爨龙颜碑》《瘗鹤铭》《张黑女墓志》《敬史君碑》《泰山经石峪金刚经》《西岳华山碑》14 种碑志）
- term：36 条（魏晋玄学、南秀北雄、牛车、剡藤纸、行书、草书、碑学、魏碑、匣钵、冕冠与冕旒、襦、木屐、假髻、黛、袄、衫、裘、裙、大氅、裤、储具、琵琶、阮咸、西凉乐、筚篥、羯鼓、中心塔柱式、隐囊、筌台、承尘、帘子、笛、羌笛、胡笳、箜篌、竹林七贤）

### 置信度

- medium：48 条
- low：29 条（14 种碑志中的 9 种只承一句评语或一行著录，另有袄、裘、大氅、王献之、碑学、帘子、羌笛、羯鼓、隐囊、筌台、承尘、《博物志》《抱朴子》《斫琴图》《乐论》《水经注》《声无哀乐论》、阮籍、郦道元、义县万佛堂等以一两句为主的条目）

### 维度分布

- primary_dimension A：12 条（书法、碑学、书画文献与史观类）
- primary_dimension B：42 条（器物、服饰、家具、乐器、窑具、石窟与建筑类）
- primary_dimension C：23 条（书体、碑刻文字与图绘类）

### 字段约定

- 全部 `consensus: tentative`、`evidence_status: source_backed`、`source_count: 1`、`version: 1`、`created = updated = last_verified = 2026-10-26`、`review_due: 2027-04-26`。
- 六节齐全；正文 ASCII 双引号 0；逐字引文用“”，校正字形、拼接句、自拟概括与交叉引用用「」。
- 同书多跨度条目在单条 `sources.citation` 内以逗号分隔行号，`source_count` 保持 1。

## 三、更新 4 条

| 候选 | 实体 | 文件 | 版本 | source_count | 要点 |
|---|---|---|---|---|---|
| cand-06-06 | 榻 | `terms/han-ta.md` | v1→v2 | 1→2 | 并入赵农 L3747、L3749、L3751 榻的尺度规定、独榻与连榻、榻上跽坐与凭几；与高丰册汉代家具叙述并存，不裁决 |
| cand-06-29 | 浮图 | `terms/fota.md` | v1→v2 | 1→2 | 并入赵农 L3936、L3940-L3942 浮图名义、嵩岳寺塔与塔的汉化；嵩岳寺塔高度赵农作 39.5 米、夏燕靖册作 41 米，并列保留 |
| cand-06-97 | 案（几案） | `terms/an-furniture.md` | v2→v3 | 2→3 | 并入赵农 L2301、L3783-L3800 南北朝大案、长案与圆案之分、书案／奏案／食案／香案、几案混称与多子盒 |
| cand-06-112 | 南北响堂山石窟 | `places/xiangtangshan-shiku.md` | v1→v2 | 1→2 | 并入赵农 L4069、L4073 南北响堂山的位置、开凿年代、中心塔柱与卷草浮雕；与夏燕靖册图注“邯郸”并存，不合并 |

- `updated` 与 `review_due` 同步顺延至 2026-10-26 / 2027-04-26。

## 四、rejected 2 条

| 候选 | 实体 | 指向 | 理由 |
|---|---|---|---|
| cand-06-03 | 《兰亭集序》（文献义） | `works/lan-ting-ji-xu.md` | 同一文本已由 cand-05-73 以法书作品立条，不在 publication 下另建同实体条目；文献引用面并入该条 |
| cand-06-04 | 玄学 | `terms/xuanxue.md` | 与 cand-05-39「魏晋玄学」为同一概念的两处叙述，合并到该条，不另建 |

### no_delta 5 条

| 候选 | 实体 | 承载条目 | 理由 |
|---|---|---|---|
| cand-05-95 | 金墉城 | `places/luoyang.md` | 来源中为洛阳城防体系一环，既有洛阳条已含全部要点，材料不足以独立成 place 条 |
| cand-05-100 | 铜雀台 | `places/yecheng.md` | 邺城宫苑的构成部分，既有邺城条已含铜雀台、建安七子与三曹；来源无台体尺度与形制 |
| cand-06-17 | 步障 | `terms/ping-feng.md` | 既有屏风条第五节已完整覆盖步障与《世说新语》斗富引文；独立成条会重复 |
| cand-06-40 | 古阳洞 | `places/longmen-grottoes.md` | 龙门窟群条已含慧成、495 年与《龙门二十品》十九品 |
| cand-06-41 | 宾阳洞 | `places/longmen-grottoes.md` | 龙门条已含《魏书·释老志》长引文与景明元年系年；洞内浮雕另由 `works/di-hou-li-fo-tu.md` 承载 |

## 五、原文错字与内部不一致

- **复核撤销的旧疑**：任务准备阶段曾据误记称《释名》作“引手却曰枇杷”、疑「杷」为衍字；经回查 L3850 实作“推手前曰枇，引手却曰杷”，与「推手前曰枇」对文完整，`terms/pi-pa.md` 照录原句，不标疑。
- **形近之误**：L3586 首句「補，是一种短衣」之「補」疑为「襦」（`terms/ru.md` 照录标疑，并以紧接的《说文解字》引文为内证）；L3893 段首「算篥」为「筚篥」之误，同段后文五处均作「筚篥」（`terms/bi-li.md`）；L3932 引文「谴使」疑为「遣使」（`works/bai-ma-si.md`）；《洛阳伽蓝记》引文「整齐化一」之「化一」疑为「划一」（`publications/luo-yang-qie-lan-ji.md`）；《抱朴子》引文「袖袂财制」之「财」疑为「裁」（`publications/bao-pu-zi.md`）；L4087「怏然自足」之「怏然」与「自足」语义不合，疑形近误录（`persons/wang-xi-zhi.md`、`works/lan-ting-ji-xu.md`）。
- **人名不一致**：L3707-L3715 内「石崇」「石祟」并见，`works/jin-gu-yuan.md` 照录标疑，「石祟」当作「石崇」。
- **器物语境用字**：L3525「碑文标志」于谷仓罐语境当为「铭文」，`works/qing-ci-gu-cang-guan.md` 照录标疑。
- **重出与脱字**：L3556「各垂挂12旒由珊瑚珠制成的冕旒」冕旒二字重复（`terms/mian-guan-mian-liu.md`）；L3836 帘子段中段自「帘者本有廉耻的意思」以下句子重出、脱字、「垂帘听政」误作「垂帝听政」并引号错置，只有首尾分句可用（`terms/lian-zi.md`）；L3747「有较了较大的发展」疑为「有了较大的发展」（`terms/han-ta.md`）。
- **名称前后不一**：L4069 作「辽宁义县万佛寺」、L4079 小标题与正文均作「义县万佛堂」，标题取「万佛堂」，两处照录不统一改字（`works/yi-xian-wan-fo-tang.md`）。
- **跨源计量不一致**：嵩岳寺塔高度，夏燕靖 2016 册作 41 米、赵农 L3936 作 39.5 米，两源均未注测量依据，`terms/fota.md` 并列保留不作取舍。
- **跨源行政区划用字**：赵农作「河北峰峰市」，今为邯郸市峰峰矿区；夏燕靖册图注作「邯郸」，两说相容，`places/xiangtangshan-shiku.md` 照录不合并。
- **来源推断与传说限定**：L3367「这应是一种人力脚踏车轮的推动船」用「应是」立说（`works/qian-li-chuan.md`）；L3606「传说中的南朝宋谢灵运……有‘谢公屐’之说」（`terms/mu-ji.md`）；《斫琴图》作者用「相传」系于顾恺之（`works/zhuo-qin-tu.md`）；王献之条未说明《洛神赋》是书法还是画作，只照录书名（`persons/wang-xian-zhi.md`）。
- **异文照录**：L3627《北齐书》引文「髻心正西」、L3852「传说汉代」句被三幅图注隔断而保留「传说」二字，均照录不校改。
- **未采来源外内容**：`works/tan-yao-wu-ku.md` 的 `location` 原写「山西大同云冈石窟」，因指定行段未给今省县，改为「云冈石窟（北魏京城西武州塞；来源未给今省县）」。

## 六、图注与证据边界

- L3852「传说汉代」止于行末，被图 5-42、图 5-43、图 5-44 三幅图注隔断，续句在 L3862；`terms/pi-pa.md` 分引并说明，不作连续引文。
- L3586「襦与袄相」与 L3591 行首「近」被图 5-23 图注隔断，`terms/ru.md` 分引。
- L3622 起句与 L3627 续句之间为图 5-25 图注，`terms/jia-ji.md` 分段引录并说明拼合关系。
- L3787「办公行政的同」与 L3792「义词」被图 5-39「北朝 乐伎俑」图注隔断，两截拼合读作「同义词」，`terms/an-furniture.md` 分引不作连续引文。
- L4030 行末与 L4032 行首之间断开，`works/di-hou-li-fo-tu.md` 分别照录，不拼作连续引文。
- L3459 图 5-13 与《瘗鹤铭》同段，`works/yi-he-ming.md` 未据图补写石质、形制与字数。
- 图 5-36 注为南朝青瓷谷仓罐，与前举孙吴永安三年纪年罐不是同一表述，`works/qing-ci-gu-cang-guan.md` 标出图注朝代与纪年实例不一致，未据图补写。
- 所有新建与更新条目均声明图版未作视觉核验，不据图补形制、纹样、尺寸与图像细节。

## 七、引文审计与独立复核

- 结构检查：`_zn_struct.py _zn_ch5_creates.txt` → `problems: 0`（六节、frontmatter 必需字段、正文 ASCII 双引号、反引号 KU 链接可解析、日期与版本）。
- 六册合并语料引文回查：`_zn_audit.py @_zn_ch5_creates.txt` → `findings: 0`。
- 赵农册严格回查：`_zn_audit_strict.py @_zn_ch5_new.txt`（77 个新建文件）→ `findings: 0`；该脚本只查赵农册，4 个更新文件含高丰、夏燕靖引文，按设计不纳入单册严格回查，改由六册脚本覆盖。
- 内部链接：77 个新建条目中的全部反引号 KU 路径均可解析，缺失 0。
- 独立复读：7 个 person、6 个 publication、28 个 work、36 个 term 均由 Agent 逐条复读；复读中修正 `tan-yao-wu-ku` 的 `location` 来源外省县、`han-ta` 的一处非逐字引文、`pi-pa` 的《释名》引文与释名重出说明、`an-furniture` 的跨图注拼接引文，并把 3 处自拟概括由“”改为「」。
- 维度分配：A 12、B 42、C 23；无一文件缺 `primary_dimension`。

## 八、跨度说明

- 第五章候选来自两个切块器，编号混有 `cand-05-*` 与 `cand-06-*`；本包按 `payload.source_span.chapter` 归入第五章，不按编号前缀另立批次。
- 来源跨度 L3258-L3314、L3317-L3405、L3408-L3512、L3515-L4095，共 832 行，覆盖第五章全部候选所在行段。
- 同书多跨度更新（han-ta、fota、an-furniture、xiangtangshan-shiku）各新增一条赵农来源，`source_count` 加 1，`version` 加 1；`updated` 与 `review_due` 同步顺延。

## 九、状态与下一跳

- 候选状态变化：`needs_evidence` 2602 → 2514；`applied` 1749 → 1830；`rejected` 822 → 824；`no_delta` 166 → 171；总数 5339 不变。
- 生成态：`scripts/build_discovery_index.py` 重建候选索引；`scripts/build_translation_index.py` 重建翻译索引（1238 条）；`scripts/run_sync_closure.py --refresh-generated --full` 全部通过（250 tests, 16 subtests）。首次运行在写 `candidate-index.jsonl` 时报 `OSError: [Errno 22]`，重跑即恢复，属临时文件占用，非数据错误。
- `--check-generated`：因工作树尚未提交，`check generated snapshots` 按预期失败，记为 `blocked_pending_commit`；提交后重跑可闭合。
- 未提交、未推送：`commit`、`push` 等外部状态变更须由用户当次明确授权。
- 下一跳：赵农册第六章 91 条、第七章 126、第八章 63、第九章 156、第十章 113、总结 9 条 unit 候选。
