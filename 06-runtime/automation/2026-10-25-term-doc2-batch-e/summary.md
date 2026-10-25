# term doc_count=2 第五批（xdup-0444—xdup-0470）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-term-doc2-batch-e/`
状态：`applied`

## 一、本批做了什么

- 覆盖 term 类型 doc_count=2 重复组的全部剩余 26 组，共 52 个候选（xdup-0444—xdup-0470，其中 0446 已在早前批次关闭）。
- 25 组新建 term KU，1 组更新既有 KU。
- 26 个 canonical `applied`，26 个同组重复候选 `rejected`。
- 候选索引投影后：applied 329、no_delta 11、rejected 628、needs_evidence 4371；active 4371、terminal 968。
- **term doc2 累计关闭 136 组，全部关闭（136/136）**；person doc2 维持 48/48 全关。

## 二、新建的 25 个 term KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0444 | 褐彩（Brown Splash Decoration） | ceramic_decoration | B | 田自秉 2010、夏燕靖 2009 |
| xdup-0445 | 褒衣博带（Loose Robe, Broad Sash） | garment_form | E | 夏燕靖 2009、赵农 2009 |
| xdup-0447 | 豆（Dou） | vessel_form | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0448 | 质孙服（Zhisun Robe） | garment_form | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0449 | 釉上彩（Overglaze Decoration） | ceramic_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0450 | 釉里红瓷（Underglaze Red Porcelain） | ceramic_type | B | 夏燕靖 2009、赵农 2009 |
| xdup-0451 | 里坊制（Lifang Ward System） | urban_system | D | 赵农 2009、夏燕靖 2016 |
| xdup-0452 | 铁器时代（Iron Age） | archaeological_period | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0453 | 铅釉陶（Lead-Glazed Pottery） | ceramic_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0454 | 铸鼎象物（Casting Ding to Image Things） | design_concept | A | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0455 | 陶甑（Pottery Zeng） | vessel_form | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0456 | 陶鬶（Pottery Gui） | vessel_form | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0457 | 雕漆（Diaoqi） | lacquer_technique | B | 高丰 2004、田自秉 2010 |
| xdup-0458 | 青瓷（Celadon） | ceramic_type | B | 赵农 2009、夏燕靖 2009 |
| xdup-0459 | 青铜（Bronze） | material_type | B | 高丰 2004、田自秉 2010 |
| xdup-0460 | 青铜时代（Bronze Age） | archaeological_period | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0461 | 青铜水器（Bronze Water Vessels） | vessel_category | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0462 | 青铜礼器（Bronze Ritual Vessels） | vessel_category | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0463 | 青铜酒器（Bronze Wine Vessels） | vessel_category | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0464 | 青铜食器（Bronze Food Vessels） | vessel_category | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0465 | 非物质文化遗产（Intangible Cultural Heritage） | heritage_concept | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0466 | 顾姑冠（Gugu Hat） | headwear | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0467 | 鱼袋（Fish Tally Bag） | official_accessory | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0469 | 齐家文化（Qijia Culture） | archaeological_culture | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0470 | 龙窑（Dragon Kiln） | ceramic_kiln | B | 赵农 2009、田自秉 2010 |

维度分布：A 1、B 19、C 0、D 4、E 1。

## 三、更新：鸡头壶／天鸡壶

`xdup-0468` 的两个候选（田自秉 2010、夏燕靖 2016）指向既有 `terms/tianji-hu.md`。既有条目只作六朝与隋代的代际比较，缺形制来源与唐代去向。本批以 update 方式补入：

- sources 新增田自秉 2010 L2786-L3162，`source_count` 2→3。
- 描述改写：盘口壶基础上肩部一面加鸡头、另一面安把手接盘口；早期鸡头纯装饰，东晋以后加长，并有羊头、牛头、虎头及两侧刻双翅者；唐代演变为龙耳壶；另有“一边鸡头、一边龙柄、颈部作竹节形”的变体。
- 核心内容新增 5 条：定义改为盘口壶改造说、早期形态、东晋以后、源流（由罐发展而来）、唐代演变、变体描述。
- `version` 1→2，匹配质量改为三册对照，参考文献插入田自秉并重排。

## 四、并列处理的语义分歧

1. **盘与虢季子白盘**：2009 称盘“圆形浅腹”，2016 称虢季子白盘“长方形盥洗器”。两说并列。
2. **盛食器用字**：2009 作“盌”，2016 作“盨”，两者为不同字形。已并列并在正文标注。
3. **齐家文化分期**：田自秉作“约等于龙山文化时期，基本与夏代相始终”，2016 作“新石器中晚期”。已并列。
4. **褒衣博带的两义**：夏燕靖指魏晋南北朝宽衫大袖的世俗服饰风尚（《竹林七贤画像砖》为证），赵农指云冈石窟采用的中原样式佛像服饰。二者同词异域，合于一条并分列“世俗义／佛教义”。
5. **陶鬶用字**：2016 原文多作“陶鬻”，为“鬶”的讹字，已标注，未改来源。
6. **青铜定义口径**：高丰作“铜、锡、铅等元素的合金”，田自秉作“红铜加锡的一种合金”，并补红铜与铜石并用时代。并列。

## 五、本批的方法判断

- **褒衣博带合为一条**：世俗服饰与佛像服饰共享同一词形，且后者正是前者被移用于佛教造像的结果；分成两条会切断这一语词传播链，故合条并在核心内容中分列两义。
- **质孙服、鱼袋、里坊制、非遗入 D 维度**：四者都以制度、等级或遗产管理为骨架，不是单纯的器物形制。
- **青铜四类（食器、酒器、水器、礼器）并立**：前六册按功能分四类叙述，四类器名互有交叉（如鼎既在食器又在礼器），本批保留原书分类而不合并，礼器条只讲制度属性，不重复器类清单。
- **青铜与青铜时代分立**：前者是材料，后者是分期；二者的定义来源不同册，合并会掩盖“合金配比”与“文明阶段”两种叙述层次。

## 六、状态与验证

- `apply-plan.jsonl`：26 行（25 create + 1 update），哈希 26/26 与磁盘一致（update 行的 before 为更新前指纹 `b9774b6c…f0933`）。
- `candidate-decision-ledger.jsonl`：104 行（26 条三段 applied 链 + 26 条 rejected）。
- 内容质量审计：336 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 336/336 可解析。
- 候选索引：`sha256:63ed6cf3…caebb`，7,243,359 B，5,339 行。
- 规则漂移 0；sync closure 19 步全部通过，250 tests + 16 subtests。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 田自秉“雕漆”条 location L3394-L4753、赵农“龙窑”条 L3539-L5533 均为多段拼接的超大跨度，正文已标注“具体段落位置待核”。
- 青铜四类未给各器类的尺寸序列与容量；齐家文化未给测年数据；顾姑冠未给冠高实测。
- 「相关知识元」中仍有指向未建立 `terms/*.md` 的悬空路径（如 `terms/an.md`、`terms/guan-ying-shou-gong-ye.md`），内容质量审计不检查此项，留待统一清理。
- Theme/Topic 均未 materialize；relation 未审查。
- term doc2 已全关；下一阶段转入其余 doc2 类型（work 52、publication 46、institution 26、place 25、procedure 10、event 9）与 doc1 组。
