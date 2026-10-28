# batch-d 写作规格（赵农 2009 第四章）

本文件只给子代理使用。只读来源，不修改来源，不碰索引、台账、manifest 与 Git。

## 0. 来源与范围

- 来源文件（只读）：`03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md`
- doc_id：`2009-zhaonong-zhongguo-yishu-shejishi`
- 本章范围：L2475-L3257（第四章 统一的气量——秦汉时期的设计）
- 每个条目只使用规格表给出的行段；不得引用其他书籍，不得引用未给行段的章节。
- 图版（`![](...)` 与图注）未做视觉核验，不得据图补写器形、纹饰、尺寸。

## 1. 通用写作规则

1. 中文正文；代码、路径、字段名、标准名保留英文。
2. 引文：逐字照录原文用 `“ ”`；压缩改写、自拟概括、被页眉/图注隔断的拼接句用 `「 」`；嵌套内层用 `‘ ’`。
3. 正文不得出现 ASCII 双引号 `"`（只允许在 frontmatter 的 citation/location 里）。
4. 所有引文必须能在给定行段内逐字找到；找不到就改成「 」概括，不要硬引。
5. 原文明显错字照录并标疑（`疑为「某」`），不径改；来源内部矛盾两存不裁。
6. 不写来源没有的事实：不补生卒、籍贯、尺寸、重量、件数、收藏地、英文名。
7. `hierarchy_scope_note` 与「在层级体系中的位置」的 scope_note 必须同文。
8. 六节标题固定且顺序固定：`## 描述`、`## 核心内容`、`## 在层级体系中的位置`、`## 相关知识元`、`## 验证状态`、`## 参考文献`。
9. `## 相关知识元` 只写规格表列出的既有路径，每条形如：`` `works/dujiangyan.md` 记都江堰工程 ``；末尾统一写 `relation 未审查，不写入正式 \`relations\`。`
10. 新建条目统一：`consensus: tentative`、`evidence_status: source_backed`、`source_count: 1`、`version: 1`、`created: 2026-10-26`、`updated: 2026-10-26`、`last_verified: 2026-10-26`、`review_due: 2027-04-26`、`primary_domain: chinese-design-history`。
11. `confidence`：材料有一段以上实质描述记 `medium`；只有一句、一句半、或只有图注记 `low`。规格表已给出，不得自行上调。
12. `## 验证状态` 的「匹配质量」要写清：哪些行给什么信息、来源缺什么、confidence 依据。
13. `## 参考文献` 只列：`1. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009.`
14. 文件末尾保留一个换行。

## 2. 四类 frontmatter 模板

### 2.1 person

```yaml
---
title: 中文（English）
name_en: English
type: person
sub_type: ruler | thinker | historian | calligrapher | engineer | craftsman | official | general
name_original: 中文
language_original: zh
name_zh: 中文
translation_status: provisional
translation_note: 采用通行拼音 X；来源未给既定英译，不另拟意译。
tags:
  - 秦汉
  - ……
aliases:
  - 中文
birth_death: 未载
nationality: 秦 | 西汉 | 东汉
period: 秦 | 西汉 | 东汉
occupation: ……
contribution_scope: ……
sources:
  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L####-L####."
    location: "L####-L####"
    evidence_ref:
      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi
      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md
      chapter_id: null
      chunk_id: null
created: 2026-10-26
updated: 2026-10-26
confidence: medium
consensus: tentative
source_count: 1
last_verified: 2026-10-26
review_due: 2027-04-26
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: B
secondary_dimensions:
  - A
hierarchy_scope_note: 一句话说明该人物在维度中的位置与 Theme/Topic 未 materialize。
---
```

### 2.2 work

```yaml
---
title: 中文（English）
name_en: English
type: work
sub_type: inscription | measuring_vessel | manuscript | calligraphy | road | waterway_engineering | bridge | palace | defensive_wall | sculpture | map | agricultural_machine
title_original: 中文
title_original_language: zh
title_zh: 中文
translation_note: 采用音译/通行译名 X；来源未给英译。
format: ……
year: ……
location: ……
dimensions: 未记
collection: 未记
tags:
  - 秦汉
  - ……
aliases:
  - 中文
sources:
  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L####."
    location: "L####"
    evidence_ref:
      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi
      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md
      chapter_id: null
      chunk_id: null
created: 2026-10-26
updated: 2026-10-26
confidence: medium
consensus: tentative
source_count: 1
last_verified: 2026-10-26
review_due: 2027-04-26
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: B
hierarchy_scope_note: 一句话……
---
```

### 2.3 publication

```yaml
---
title: 中文（English）
name_en: English
type: publication
sub_type: classical_text | history | essay_collection | literary_work
title_original: 中文
title_original_language: zh
title_zh: 中文
translation_note: 采用音译加通行意译 X；来源未给英译。
tags:
  - 秦汉
  - ……
aliases:
  - 中文
  - 《中文》
sources:
  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L####."
    location: "L####"
    evidence_ref:
      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi
      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md
      chapter_id: null
      chunk_id: null
created: 2026-10-26
updated: 2026-10-26
confidence: medium
consensus: tentative
source_count: 1
last_verified: 2026-10-26
review_due: 2027-04-26
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: A
hierarchy_scope_note: 一句话……
---
```

### 2.4 term

```yaml
---
title: 中文（English）
name_en: English
type: term
sub_type: cosmology | iconography | currency | script | institution_term | transport_term | weapon | armor | agricultural_implement | measuring_tool | architecture_term | burial_term | dress_term | lighting_device | mechanism
term_original: 中文
term_zh: 中文
academic_translation_status: provisional
translation_note: 采用通行译名 X；来源未提供英文名。
tags:
  - 秦汉
  - ……
aliases: []
sources:
  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L####-L####."
    location: "L####-L####"
    evidence_ref:
      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi
      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md
      chapter_id: null
      chunk_id: null
created: 2026-10-26
updated: 2026-10-26
confidence: medium
consensus: tentative
source_count: 1
last_verified: 2026-10-26
review_due: 2027-04-26
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: B
secondary_dimensions:
  - D
hierarchy_scope_note: 一句话……
---
```

## 3. 分组任务

### G1 persons（17 个）

1. `persons/qin-shi-huang.md` — 秦始皇（Qin Shi Huang），medium，B（secondary A、D），sub_type ruler。
   行段：L2488-L2492、L2571、L2653、L2672-L2674、L2817-L2829、L2848-L2850、L2922、L3027。
   要点：李白《古风》引句、以武力统一与中央集权、焚书坑儒与宫苑陵墓、统一文字用小篆、车同轨与驰道、兵马俑与铜车马、统一度量衡、宫殿遍天下、派蒙恬连长城、秦人尚黑。相关：`terms/xiaozhuan.md`、`terms/che-tong-gui.md`（本批新建，可链）、`works/qin-chi-dao.md`（本批新建）、`works/qin-bing-ma-yong.md`、`works/qinling-tongchema.md`、`terms/qin-quan.md`（本批新建）、`works/qin-han-changcheng.md`（本批新建）、`places/xianyang.md`。
2. `persons/han-wu-di.md` — 汉武帝（Emperor Wu of Han），medium，D（secondary A、B），sub_type ruler。
   行段：L2505、L2509-L2513、L2561、L2633-L2639、L2694-L2698、L2799、L2924。
   要点：文景之治后的国威、击败匈奴与地理版图、盐铁酒官营、耦犁二牛三人、董仲舒与独尊儒术、货币改革（白金、皮币、上林三官、五铢）、黄金库存与马蹄金麟趾金、张骞通西域、赵过耦犁耧车、卫青霍去病。相关：`events/han-wudi-duzun-rushu.md`、`events/zhangqian-chushi-xiyu.md`、`terms/han-wu-zhu.md`（本批新建）、`institutions/shanglin-sanguan.md`、`terms/ou-li.md`（本批新建）、`terms/sichou-zhilu.md`、`places/huoqubing-mu.md`。
3. `persons/dong-zhong-shu.md` — 董仲舒（Dong Zhongshu），low，A。
   行段：L2513。
   要点：公元前179—前104年、以《春秋公羊传》大义为依托、推崇儒术、外儒内法、罢黜百家独尊儒术、儒学成为政治伦理教义。相关：`events/han-wudi-duzun-rushu.md`、`persons/confucius.md`。
4. `persons/si-ma-qian.md` — 司马迁（Sima Qian），medium，A。
   行段：L2515、L2692。
   要点：约公元前145年生、忍辱负重著《史记》、鲁迅“千古之绝唱，无韵之离骚”语、自述青年游历的《史记·太史公自序》长引文说明道路通达。相关：`publications/shiji.md`。
5. `persons/ban-gu.md` — 班固（Ban Gu），low，A。
   行段：L2517。
   要点：公元32—92年、《汉书》延续司马迁、开创历朝断代史。相关：`publications/han-shu.md`（本批新建）、`publications/shiji.md`。
6. `persons/xu-shen.md` — 许慎（Xu Shen），medium，C（secondary A）。
   行段：L2517-L2525、L2609-L2616。
   要点：约公元58—约147年、《说文解字》、字叔重、汝南召陵（河南郾城）人、太尉南閤祭酒、“五经无双许叔重”、六书、以小学训诂为传统基础。相关：`publications/shuowen-jiezi.md`、`terms/liu-shu.md`、`terms/xiaozhuan.md`。
7. `persons/li-si.md` — 李斯（Li Si），medium，C（secondary D）。
   行段：L2527、L2571、L2590、L2592、L2831。
   要点：整理规范小篆、丞相身份颁布全国、据石鼓文与商鞅方升铭文制定标准文字、泰山/峄山/会稽刻石、《史记·李斯列传》“平斗桶度量文章”引句。相关：`terms/xiaozhuan.md`、`works/shi-gu-wen.md`（本批新建）、`works/shang-yang-fang-sheng.md`（本批新建）、`terms/li-shu.md`（本批新建）。
8. `persons/cai-lun.md` — 蔡伦（Cai Lun），medium，B。
   行段：L2529、L3127-L3138。
   要点：公元62—121年、字敬仲、桂阳（湖南耒阳）人、汉和帝时尚方令、监作秘剑及诸器械“莫不精工坚密，为后世法”、《后汉书·宦官传》造纸引文、元兴元年奏上、蔡侯纸、西汉麻纸发现。相关：`procedures/zaozhishu.md`、`institutions/shangfang.md`。
9. `persons/zhang-qian.md` — 张骞（Zhang Qian），medium，D（secondary E）。
   行段：L2696、L2698。
   要点：汉武帝派其出使西域联络大月氏、玉门关外被匈奴扣留十余年、第二次带丝帛金币、西域设管理机构、商队与物产交流、长安到罗马四年行程。相关：`events/zhangqian-chushi-xiyu.md`、`terms/sichou-zhilu.md`。
10. `persons/ban-chao.md` — 班超（Ban Chao），low，D（secondary E）。
    行段：L2700。
    要点：公元73年出使西域、获得威望、巩固丝绸之路通畅、使其成为国际性交通要道。相关：`terms/sichou-zhilu.md`、`events/zhangqian-chushi-xiyu.md`。
11. `persons/wang-mang.md` — 王莽（Wang Mang），medium，D（secondary B）。
    行段：L2561、L2641、L2643。
    要点：西汉末期改制复古、抑制商业、变更货币未果、废五铢行刀布贝、材质扩至银贝龟甲、错金金错刀、以泉称钱、食古不化导致混乱、东汉恢复五铢。相关：`terms/jin-cuo-dao.md`（本批新建）、`terms/han-wu-zhu.md`（本批新建）、`terms/huan-qian.md`。
12. `persons/zhong-yao.md` — 钟繇（Zhong Yao），low，C。
    行段：L2607。
    要点：东汉末年书法家、最早楷书、《宣示表》为代表作、横波顿挫、减少隶书捺挑。相关：`terms/kai-shu.md`（本批新建）、`works/xuan-shi-biao.md`（本批新建）、`terms/li-shu.md`（本批新建）。
13. `persons/cheng-miao.md` — 程邈（Cheng Miao），low，C。
    行段：L2592。
    要点：传说囚徒程邈创造民间自发文字结构、后世称秦隶、代表作品为睡虎地秦简文字；来源用“传说”，须保留不确定语气。相关：`terms/li-shu.md`（本批新建）、`works/shuihudi-qin-bamboo-slips.md`（本批新建）。
14. `persons/xiao-he.md` — 萧何（Xiao He），medium，A（secondary B、D）。
    行段：L2858。
    要点：营作未央宫、立东阙北阙前殿武库太仓、刘邦怒其过度、萧何“非壮丽无以重威”答语、“高祖乃说”；这是建筑规模与皇权关系的直接材料。相关：`works/weiyang-palace.md`（本批新建）、`places/han-chang-an.md`。
15. `persons/meng-tian.md` — 蒙恬（Meng Tian），medium，B（secondary D）。
    行段：L2657、L2922。
    要点：太子扶苏与大将蒙恬修筑北通九原驰道（长约1400公里）、公元前214年率30万军民连结秦赵燕旧长城、西起临洮东入辽东。相关：`works/qin-chi-dao.md`（本批新建）、`works/qin-han-changcheng.md`（本批新建）。
16. `persons/huo-qu-bing.md` — 霍去病（Huo Qubing），medium，B（secondary A）。
    行段：L2924、L2975-L2980。
    要点：汉武帝时期青年将军、对匈奴决定性胜利、英年早逝年仅24岁、墓置于茂陵之侧、封土模拟祁连山。相关：`places/huoqubing-mu.md`、`works/horse-treading-xiongnu.md`（本批新建）。
17. `persons/shi-lu.md` — 史禄（Shi Lu），low，B。
    行段：L2723。
    要点：公元前219年秦始皇派史禄到广西兴安、开凿湘江漓江、修33公里灵渠、连通长江珠江水系。相关：`works/ling-qu.md`（本批新建）。

### G2 works A（9 个）

1. `works/shi-gu-wen.md` — 石鼓文（Stone Drum Inscriptions），low，C，sub_type inscription。
   行段：L2586、L2590。
   要点：秦国文字代表、亦称大篆或籀文、与西周金文有关联、李斯据其书写特点制定小篆。相关：`terms/xiaozhuan.md`、`persons/li-si.md`（本批新建）；不得写“石鼓”形制、字数、现藏。
2. `works/shang-yang-fang-sheng.md` — 商鞅方升（Shang Yang Fang Sheng），medium，B（secondary D），sub_type measuring_vessel。
   行段：L2586、L2590、L2819-L2821。
   要点：商鞅变法时量器、铭刻文字、李斯据其铭文书写特点制定小篆、商鞅“平权衡正度量”引《战国策·秦策》、秦始皇依秦制颁全国、廿六年诏书“法度量则不壹歉疑者皆明壹之”、山东秦陶量有诏书。相关：`terms/qin-liang.md`（本批新建）、`terms/qin-quan.md`（本批新建）、`terms/xiaozhuan.md`。
3. `works/shuihudi-qin-bamboo-slips.md` — 睡虎地秦简（Shuihudi Qin Bamboo Slips），low，C，sub_type manuscript。
   行段：L2592。
   要点：湖北云梦睡虎地出土、秦隶代表作品；只有一句，不得补简数、内容、墓主。相关：`terms/li-shu.md`（本批新建）、`places/shuihudi-qinmu.md`、`persons/cheng-miao.md`（本批新建）。
4. `works/juyan-han-slips.md` — 居延汉简（Juyan Han Slips），low，C，sub_type manuscript。
   行段：L2603。
   要点：甘肃居延出土、西汉末年草书字体的代表、运笔以隶书为基点、飘逸活泼、笔意连缀；只有一句。相关：`terms/zhang-cao.md`（本批新建）、`terms/li-shu.md`（本批新建）。
5. `works/xuan-shi-biao.md` — 宣示表（Xuanshi Biao），low，C，sub_type calligraphy。
   行段：L2607。
   要点：钟繇代表作、最早楷书作品、横波顿挫、减少隶书捺挑、整洁简练；来源未给内容、流传与拓本。相关：`persons/zhong-yao.md`（本批新建）、`terms/kai-shu.md`（本批新建）。
6. `works/qin-chi-dao.md` — 秦驰道（Qin Chi Dao (Imperial Highway)），medium，B（secondary D），sub_type road。
   行段：L2651-L2672。
   要点：以咸阳为中心辐射、宽约60米、高出地面、分皇帝专用道/军事道/常人道、每10里一管理亭、北通九原约1400公里由扶苏蒙恬修、三天三夜赴阴山、《汉书·贾山传》引文、汉代扩为长安中心道路。相关：`terms/che-tong-gui.md`（本批新建）、`persons/meng-tian.md`（本批新建）、`persons/qin-shi-huang.md`（本批新建）。
7. `works/baoxie-road.md` — 褒斜道（Baoxie Road），medium，B，sub_type road。
   行段：L2710-L2719。
   要点：秦惠王时修、连接秦岭北麓眉县斜水谷与南麓褒水谷、长200余公里、石孔30厘米见方50厘米深、上中下三层（雨篷/木板道路/支架）、《史记·货殖列传》“栈道千里…唯褒斜道绾毂其口”、刘邦烧绝栈道、韩信明修栈道暗渡陈仓。相关：`terms/zhan-dao.md`（本批新建）。
8. `works/ling-qu.md` — 灵渠（Ling Qu），medium，B，sub_type waterway_engineering。
   行段：L2723-L2725。
   要点：公元前219年史禄主持、广西兴安、连通湘江漓江、长33公里、连通长江珠江水系、船闸提高平衡水位、分水工程保持水源、桂林广州雷州半岛设行政机构。相关：`persons/shi-lu.md`（本批新建）。
9. `works/weishui-three-bridges.md` — 渭水三桥（Three Bridges over the Wei River），medium，B，sub_type bridge。
   行段：L2727。
   要点：东中西三座、中渭桥战国已修秦始皇加固翻修、长约525米宽约13.8米、750根木桩67个桥墩、横梁桥面、雕花护栏、中间高两边斜下呈八字、石灯华表、汉代增修东西两桥。相关：`places/xianyang.md`、`works/ba-bridge.md`（本批新建）。

### G3 works B（9 个）

1. `works/ba-bridge.md` — 灞桥（Ba Bridge），medium，B，sub_type bridge。
   行段：L2729。
   要点：西安灞河、汉代古桥、初为木桥、王莽时烧毁、屡毁屡修、十里相送灞柳相别；来源未给长度、形制细节。相关：`works/weishui-three-bridges.md`（本批新建）。
2. `works/xianyang-palace.md` — 咸阳宫（Xianyang Palace），medium，B，sub_type palace。
   行段：L2852-L2854。
   要点：咸阳原上、多重楼台建筑群、主殿侧殿卧室浴室、回廊甬道连通、陶制下水管道、灭一国即仿建其宫殿、六国宫殿别称、六国纹饰瓦当。相关：`places/xianyang.md`、`works/epang-palace.md`（本批新建）。
3. `works/weiyang-palace.md` — 未央宫（Weiyang Palace），medium，B（secondary D），sub_type palace。
   行段：L2856-L2860。
   要点：汉长安城重要建筑、遗址为南北200余米东西100余米高10余米夯土高台、《史记·高祖本纪》萧何营作与“非壮丽无以重威”长引文、张衡《西京赋》“正紫宫于未央”引句、长安城周长25公里、夯土板筑。相关：`places/han-chang-an.md`、`persons/xiao-he.md`（本批新建）、`terms/dougong.md`。
4. `works/songshan-three-que.md` — 嵩山三阙（Three Que of Mount Song），low，B，sub_type que。
   行段：L2881。
   要点：东汉营造、石质、坛庙性祭祀建筑遗迹、现存汉代地表建筑仅存阙；来源未给三阙具体名称、位置与尺寸。相关：`terms/men-que.md`（本批新建）、`places/wushi-ci.md`。
5. `works/epang-palace.md` — 阿房宫（Epang Palace），medium，B（secondary A），sub_type palace。
   行段：L2893-L2911。
   要点：夯土高台上大型木构架建筑群、四川湖北木材运关中、《史记·秦始皇本纪》长引文（东西五百步南北五十丈、上坐万人下建五丈旗、阁道复道、未成）、“阿，近也”颜师古语与“我的房子”解、七十余万人分作、蜀山兀阿房出、项羽烧秦宫室火三月不灭但未确指阿房宫、遗址尚存。相关：`persons/qin-shi-huang.md`（本批新建）、`publications/efang-palace-fu.md`（本批新建）、`places/xianyang.md`。
6. `works/qin-han-changcheng.md` — 秦汉长城（Qin-Han Great Wall），medium，B（secondary D），sub_type defensive_wall。
   行段：L2917-L2928。
   要点：战国边墙、秦拆中原城墙保留北方边墙、公元前214年蒙恬率30万军民连结秦赵燕旧长城、西起临洮东入辽东、汉武帝向西延2000里至阳关、阴山以北外长城、板筑夯土与草木芦苇石块、烽燧报警、王昌龄《出塞》引诗、明代砌砖护面。相关：`persons/meng-tian.md`（本批新建）、`terms/feng-sui.md`（本批新建）、`procedures/rammed-earth-board-construction.md`、`procedures/ming-changcheng-qiangti-gouzhu.md`。
7. `works/horse-treading-xiongnu.md` — 马踏匈奴（Horse Treading a Xiongnu Warrior），medium，B（secondary A），sub_type sculpture。
   行段：L2973、L2982。
   要点：霍去病墓石刻群的中心、纪念碑式石雕、写意雕凿、以石赋形化形寓意、浮雕线雕圆雕结合、石刻约16件以马牛虎羊象猪鱼怪兽熊人为形象。相关：`places/huoqubing-mu.md`、`persons/huo-qu-bing.md`（本批新建）。
8. `works/mawangdui-boditu.md` — 马王堆帛地图（Mawangdui Silk Maps），medium，C（secondary B），sub_type map。
   行段：L3183-L3193。
   要点：1973年长沙马王堆出土、三幅帛地图（地形图、驻军图、城邑图）、西汉重要地图资料、繁密而井然详备而明晰、地形图18万分之一、驻军图8万分之一、《汉书·地理志》地理记录。相关：`places/mawangdui-hanmu.md`。
9. `works/winnowing-machine.md` — 风车（Winnowing Machine），medium，B，sub_type agricultural_machine。
   行段：L2805。
   要点：汉代发明、叶形风扇、摇动生风分离秕壳与籽粒、吹去杂草、粮食加工便利器具；来源未给尺寸、材质、传动结构。相关：`works/san-jiao-lou.md`、`works/shui-dui.md`、`terms/ou-li.md`（本批新建）。

### G4 terms A（13 个）

1. `terms/huntian-theory.md` — 浑天说（Huntian Theory），medium，A（secondary B），sub_type cosmology。
   行段：L2531。
   要点：张衡提出、“浑天如鸡子，天体圆如弹丸，地如鸡中黄，孤居于内，天大而地小”（《浑天仪图注》）、与地动仪地图指南车并列为汉代地理天文知识。相关：`persons/zhang-heng.md`、`works/huntianyi.md`。
2. `terms/si-shen.md` — 四神（Four Divine Creatures），medium，A（secondary B、C），sub_type iconography。
   行段：L2535、L2879、L3079。
   要点：左青龙右白虎上朱雀下玄武、代表地理方位、推动建筑技术、五行与五色对应（东青西白南朱北玄中央尚黄）、面南而居的解释、规矩四神纹铜镜以十二地支为铭。相关：`terms/wadang.md`、`terms/hanjing.md`、`terms/wenjiu-tongbeilu.md`。
3. `terms/qin-ban-liang.md` — 秦半两（Qin Ban Liang），medium，D（secondary B），sub_type currency。
   行段：L2559、L2625-L2631。
   要点：圆形方孔、方孔穿木棍打磨锉齐统一重量、半两重、各地份量差异、天圆地方为后人推测的文化联想、《史记·平准书》“铜钱识曰半两，重如其文”、优于刀布、从贝币记数到记重、黄金上币铜钱下币。相关：`terms/huan-qian.md`、`terms/dao-bi.md`、`terms/bu-bi.md`、`terms/han-wu-zhu.md`（本批新建）。
4. `terms/han-wu-zhu.md` — 汉五铢（Han Wu Zhu），medium，D（secondary B），sub_type currency。
   行段：L2633-L2639。
   要点：汉承秦制黄金铜钱、汉半两笨重、榆荚半两、白金（银锡合金）与皮币、上林三官、罢半两行五铢、半两12铢一铢1/24两、吸收半两样式与刀币边缘轮廓、耐磨、铜质精美色泽稳定文字庄重、重量适中便于携带计数、行至隋代。相关：`terms/qin-ban-liang.md`（本批新建）、`institutions/shanglin-sanguan.md`、`terms/huan-qian.md`。
5. `terms/li-shu.md` — 隶书（Clerical Script），medium，C，sub_type script。
   行段：L2527、L2592-L2601。
   要点：汉代演绎成汉隶、传说程邈创秦隶、睡虎地秦简为代表、圆曲变方折加快书写、方笔符号化、结体简洁笔画减少、“隶变”、小篆典雅隶书洒脱、文字成熟定型。相关：`terms/xiaozhuan.md`、`terms/zhang-cao.md`（本批新建）、`terms/kai-shu.md`（本批新建）、`works/shuihudi-qin-bamboo-slips.md`（本批新建）、`persons/cheng-miao.md`（本批新建）。
6. `terms/zhang-cao.md` — 章草（Zhangcao Cursive），medium，C，sub_type script。
   行段：L2603-L2605。
   要点：西汉末年草书、居延汉简为代表、以隶书为基点飘逸活泼笔意连缀、东汉规范为章草、缘于奏章之意、保留隶书捺挑笔锋由扁归圆、由隶变楷的重要阶段、集体设计创造意识。相关：`terms/li-shu.md`（本批新建）、`terms/kai-shu.md`（本批新建）、`works/juyan-han-slips.md`（本批新建）。
7. `terms/kai-shu.md` — 楷书（Regular Script），medium，C，sub_type script。
   行段：L2607。
   要点：最早楷书为东汉末年钟繇作品、《宣示表》为代表、横波顿挫、减少隶书捺挑、整洁简练的新型书体、为中华文明传播起作用。相关：`persons/zhong-yao.md`（本批新建）、`works/xuan-shi-biao.md`（本批新建）、`terms/li-shu.md`（本批新建）、`terms/zhang-cao.md`（本批新建）。
8. `terms/che-tong-gui.md` — 车同轨（Che Tong Gui (Standardized Track Width)），medium，B（secondary D），sub_type institution_term。
   行段：L2653、L2672。
   要点：车辆零件标准化、军事政治目的、提高运输能力加强国防、带来驰道统一修建、统一车轨宽度以六尺为准约合今1.66米、秦始皇乘舆金饰技术从车81辆；来源未给六尺与秦尺的换算依据。相关：`works/qin-chi-dao.md`（本批新建）、`terms/shuang-yuan-che.md`、`persons/qin-shi-huang.md`（本批新建）。
9. `terms/zhan-dao.md` — 栈道（Plank Road），medium，B，sub_type road。
   行段：L2704-L2719。
   要点：山地因地制宜的道路、河谷岩壁凿30厘米见方50厘米深石孔、方木嵌入、上中下三层（雨篷/木板道路/支架）、《史记·货殖列传》引文、刘邦烧绝栈道、明修栈道暗渡陈仓、依壁临水修筑难度大。相关：`works/baoxie-road.md`（本批新建）。
10. `terms/huan-shou-dao.md` — 环首刀（Ring-Pommel Saber），medium，B，sub_type weapon。
    行段：L2780。
    要点：刀柄铸成环形、刀长100厘米、骑兵步兵手持、逐渐代替铁剑、铁剑不再是士兵主要武器、剑器仅为少数官员佩饰。相关：`terms/jian-sword.md`、`terms/dao-knife.md`、`terms/han-armor.md`（本批新建）。
11. `terms/gou-xiang.md` — 钩镶（Gou Xiang (Hooked Shield)），medium，B，sub_type weapon。
    行段：L2782。
    要点：东汉出现、铁盾缩小、盾中短锥、上下铸铁钩、盾后手柄、可攻可防；来源未给尺寸、重量、出土实物。相关：`terms/leather-armor.md`、`terms/han-armor.md`（本批新建）、`terms/huan-shou-dao.md`（本批新建）。
12. `terms/han-armor.md` — 汉代铠甲（Han Dynasty Armor），medium，B，sub_type armor。
    行段：L2784、L3069-L3073。
    要点：汉代以铁甲为主普遍装备、鱼鳞甲与札甲、秦俑甲衣变化多样、将士服饰以战争需要和等级差别为设计原则、将军俑战袍外罩护甲甲衣留阔边胸前佩饰、武士俑编缀甲衣、汉代士兵“三甲”（兜鍪盆领膝甲）、御手俑护袖。相关：`terms/leather-armor.md`、`works/qin-bing-ma-yong.md`、`terms/qin-dai-fu-shi.md`。
13. `terms/ou-li.md` — 耦犁（Ou Li (Two-Ox Plow)），medium，B，sub_type agricultural_implement。
    行段：L2509、L2799-L2801。
    要点：汉武帝时推广、二牛三人、二牛抬杠、一人前导牛一人后扶犁一人中间压辕、搜粟都尉赵过推行、黄河流域普及、提高农业生产力；與耧车配套。相关：`persons/zhao-guo.md`、`works/san-jiao-lou.md`、`terms/v-shaped-iron-ploughshare-cap.md`、`works/winnowing-machine.md`（本批新建）。

### G5 terms B（12 个）

1. `terms/qin-quan.md` — 秦权（Qin Weight），medium，B（secondary D），sub_type measuring_tool。
   行段：L2823-L2829。
   要点：秦权器为石钧24斤16斤9斤8斤5斤1斤半两、铜质秦权作砝码、衡标一端实物一端秦权、提钮在中心、衡标平稳则物重相等、秦一斤约今250克、秦一尺约23厘米、一升约200毫升（原文作“200毫克”，标疑）。相关：`terms/qin-liang.md`（本批新建）、`terms/hengqi-balance.md`、`works/shang-yang-fang-sheng.md`（本批新建）。
2. `terms/qin-liang.md` — 秦量（Qin Measure），medium，B（secondary D），sub_type measuring_tool。
   行段：L2821-L2829。
   要点：铜量与陶量、铜量制1/2、1/3、1/4斗量、陶量制半斗一斗一斛（100升）、秦始皇廿六年诏书见于各种衡器量器、山东出土秦陶量有诏书、“一法度衡石丈尺”（《史记·秦始皇本纪》）、检验严格（《史记·李斯列传》引句）、汉承秦制。相关：`terms/qin-quan.md`（本批新建）、`works/shang-yang-fang-sheng.md`（本批新建）、`persons/li-si.md`（本批新建）。
3. `terms/men-que.md` — 门阙（Men Que (Gate Towers)），medium，B（secondary A），sub_type architecture_term。
   行段：L2848、L2881。
   要点：汉代地表建筑仅存阙、石质嵩山三阙为坛庙祭祀遗迹、四川山东陵墓性门阙如武氏祠阙、活动领域范围象征、用于宫殿坛庙陵墓城门、标志性建筑、“表南山之巅以为阙”的门阙观念。相关：`works/songshan-three-que.md`（本批新建）、`places/wushi-ci.md`、`works/gao-yi-que.md`。
4. `terms/feng-sui.md` — 烽燧（Feng Sui (Beacon Tower)），medium，B（secondary D），sub_type architecture_term。
   行段：L2926。
   要点：秦汉长城设置、明确防御与报警作用、边界战乱时大漠尘烟十里一报信号竞传、因地制宜草木芦苇石块夯土垒集、汉武帝阴山以北外长城建城堡烽燧。相关：`works/qin-han-changcheng.md`（本批新建）。
5. `terms/fudou-xing-fengtu-fangzhong.md` — 覆斗形封土（方中）（Fudou-shaped Burial Mound (Fangzhong)），medium，B（secondary A），sub_type burial_term。
   行段：L2995-L3004。
   要点：春秋中期出现封土、战国植树封土成制度、《周礼·冢人》“以爵等为丘封之度与其树数”、封土植树祭祀与昭示权威、帝王封土多覆斗形、底边正四边形向上内收层层夯土、讳称“方中”寓意地方、方形为帝王规格、后妃亲王之外一般人为圆形、秦始皇陵内在外在夯土围墙与尺寸。相关：`works/qin-shi-huang-ling.md`、`places/huoqubing-mu.md`、`places/qianling.md`。
6. `terms/handai-guanzhi.md` — 汉代冠制（Han Dynasty Headgear System），medium，D（secondary B），sub_type dress_term。
   行段：L3052-L3054。
   要点：冠与帻关系、文官进贤冠配介帻、武将武弁大冠配平巾帻、进贤冠前有梁以梁多少区分等级、武弁大冠漆纱制又称笼冠、冕冠为帝王冠、长冠宦官内侍、法官法冠、帻为头巾普通人只能戴帻、平巾帻与介帻之别、冠服“冠服致美佩纷玺玉”。相关：`terms/qin-dai-fu-shi.md`、`terms/han-dai-pao-fu.md`、`terms/futou.md`。
7. `terms/chanyi.md` — 禅衣（Chan Yi (Unlined Robe)），low，B（secondary D），sub_type dress_term。
   行段：L3063。
   要点：一种衬衣样式、有面无里的单衣；来源只有一句，不得补马王堆实物数据（该数据在既有素纱禅衣条目）。相关：`works/susha-chanyi.md`、`terms/shenyi.md`、`terms/han-dai-pao-fu.md`。
8. `terms/lv-de-zhonglei.md` — 履的种类（Types of Lu (Footwear)），low，B（secondary D），sub_type dress_term。
   行段：L3063。
   要点：舄为祭祀用鞋、屦为家居用鞋、屐为雨天践泥的木制鞋；来源只有一句，未给形制、材质差异与等级规定。相关：`terms/han-dai-pao-fu.md`、`terms/chanyi.md`（本批新建）。
9. `terms/dongwuxing-dengju.md` — 动物形灯与树形灯（Animal-shaped and Tree-shaped Lamps），low，B，sub_type lighting_device。
   行段：L3208。
   要点：牛灯羊灯朱雀灯树形灯、造型优美功能明确、动物姿态与灯具结合、朱雀衔环、羊背开盖羊身盛油燃芯、牛身另置灯具灯罩可旋转利用虹吸油烟入牛腹；图版未核。相关：`works/tong-niu-deng.md`、`works/changxin-palace-lamp.md`、`persons/ding-huan.md`、`terms/boshanlu.md`。
10. `terms/sinan.md` — 司南（Si Nan (South-Pointing Ladle)），medium，B，sub_type mechanism。
    行段：L3161。
    要点：利用磁石指极特性、战国发现、秦汉广为使用、王充《论衡·是应篇》“司南之杓，投之于地，其柢指南”、唐宋被指南针替代、天然磁石加工磁性散失、准确性不够；来源未给形制尺寸与实物。相关：`terms/zhinan-che.md`、`terms/magnetite.md`、`terms/jili-guche.md`。
11. `terms/jin-cuo-dao.md` — 金错刀（Jin Cuo Dao (Gold-Inlaid Knife Coin)），medium，D（secondary B），sub_type currency。
    行段：L2641、L2643。
    要点：西汉末年王莽托古改制、废五铢、刀布贝等形式、错金技术制成金错刀、张衡《四愁诗》“美人赠我金错刀，何以报之英琼瑶”、成为礼品有馈赠收藏价值但缺乏实用意义、王莽货币误区、以泉称钱。相关：`persons/wang-mang.md`（本批新建）、`terms/dao-bi.md`、`terms/han-wu-zhu.md`（本批新建）、`terms/han-dai-jin-bi.md`（本批新建）。
12. `terms/han-dai-jin-bi.md` — 汉代金币（马蹄金、麟趾金、金五铢）（Han Gold Currency），medium，D（secondary B），sub_type currency。
    行段：L2635。
    要点：黄金赏赐库存朝贡、汉武帝时库存50万斤为全国一半、秦汉黄金制形以金饼金钣为主、《汉书·食货志》“黄金方寸而重一斤”、汉武帝铸马蹄金麟趾金与金五铢、黄金一斤等于铜钱一万、东汉黄金货币功能减退转为金银器皿。别名：马蹄金、麟趾金、金五铢。相关：`terms/jin-ban.md`、`persons/han-wu-di.md`（本批新建）、`terms/han-wu-zhu.md`（本批新建）。

### G6 publications（4 个）

1. `publications/han-shu.md` — 汉书（Han Shu / Book of Han），medium，A，sub_type history。
   行段：L2517、L2633、L2637、L2672、L2702、L2833。
   要点：东汉班固撰、公元32—92年、延续《史记》开断代史、《武帝本纪》《食货志》《律历志》《贾山传》被来源引用；不得写卷数、体例细节。相关：`persons/ban-gu.md`（本批新建）、`publications/shiji.md`。
2. `publications/lun-heng.md` — 论衡（Lun Heng），low，A，sub_type essay_collection。
   行段：L2525、L3161。
   要点：王充（公元27—约97年）著、推崇文章情感真实、《论衡·是应篇》司南引文；来源未给篇目总数与版本。相关：`terms/sinan.md`（本批新建）。
3. `publications/xijing-zaji.md` — 西京杂记（Xijing Zaji (Miscellanies of the Western Capital)），medium，A（secondary B），sub_type essay_collection。
   行段：L3113、L3171、L3199。
   要点：记西汉长安工匠丁缓卧褥香炉与常满灯、“为机环转运四周而炉体常平”、记里鼓车“记道车驾四中道”、长安巧工丁缓“七龙五凤杂以芙蓉莲藕之奇”；来源未给作者、卷数、成书年代。相关：`persons/ding-huan.md`、`terms/jili-guche.md`、`works/changxin-palace-lamp.md`。
4. `publications/efang-palace-fu.md` — 阿房宫赋（Efang Gong Fu (Rhapsody on the Epang Palace)），medium，A（secondary C），sub_type literary_work。
   行段：L2903-L2907。
   要点：唐代杜牧作、“覆压三百余里隔离天日”长段引文、“秦人不暇自哀而后人哀之”议论、借景寓意演成历史政治警惕观念、来源追问“杜牧的阿房宫还是秦始皇的阿房宫哪个更真实”。相关：`works/epang-palace.md`（本批新建）。
