# term doc_count=2 第一批（xdup-0137、xdup-0333—xdup-0358）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-term-doc2-batch-a/`
状态：`applied`

## 一、本批做了什么

- 覆盖 27 个 term 类型 doc_count=2 重复组，共 55 个候选。
- 新建 25 个 term KU（`04-knowledge/units/terms/`）。
- 更新 1 个既有 KU：`terms/proto-porcelain.md`（原始青瓷），补高丰 2004 来源并修正原正文“高丰一册全书无此词”的误判。
- 整组拒绝 1 组：`xdup-0354` 原始瓷（2 个候选），理由是与既有 `proto-porcelain.md` 同实体，内容由 `xdup-0355` 的 update 并入。
- 其余 29 个同组重复候选按“内容已并入 canonical”`rejected`。
- 候选索引投影后：applied 223、no_delta 10、rejected 521、needs_evidence 4585；active 4585、terminal 754。

## 二、新建的 25 个 term KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0137 | 透光镜（Light-Transmitting Mirror） | bronze_mirror_type | B | 赵农 2009、田自秉 2010 |
| xdup-0333 | 丁村文化（Dingcun Culture） | archaeological_culture | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0334 | 中国固有式建筑（Chinese Inherent-Style Architecture） | building_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0335 | 中山装（Zhongshan Suit） | garment_form | D | 夏燕靖 2009、赵农 2009 |
| xdup-0336 | 五代十国（Five Dynasties and Ten Kingdoms） | historical_period | B | 赵农 2009、夏燕靖 2016 |
| xdup-0337 | 五大名窑（Five Great Kilns） | ceramic_kiln_group | B | 赵农 2009、夏燕靖 2016 |
| xdup-0338 | 五彩（Wucai / Polychrome Porcelain） | ceramic_type | B | 赵农 2009、夏燕靖 2016 |
| xdup-0339 | 仿宋体（Fangsong Typeface） | typeface | C | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0340 | 作铺（Zuopu / Tang Urban Workshop） | craft_system | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0341 | 佩璜（Peihuang / Ornamental Jade Pendant） | jade_ornament | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0342 | 俎（Zu / Ritual Chopping Stand） | vessel_form | B | 高丰 2004、夏燕靖 2016 |
| xdup-0343 | 元谋人（Yuanmou Man） | hominin | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0344 | 凭几（Pingji / Arm Rest） | furniture_form | B | 高丰 2004、赵农 2009 |
| xdup-0345 | 列鼎制度（Graduated Ding System） | ritual_system | D | 赵农 2009、田自秉 2010 |
| xdup-0346 | 剪纸（Papercut） | folk_craft | B | 赵农 2009、田自秉 2010 |
| xdup-0347 | 包买主（Baomaizhu / Putting-Out Merchant） | economic_role | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0348 | 化妆土（Slip / Ceramic Coating） | ceramic_technique | B | 夏燕靖 2009、田自秉 2010 |
| xdup-0349 | 北京人（Peking Man） | hominin | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0350 | 匜（Yi / Pouring Vessel） | vessel_form | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0351 | 匠户（Jianghu / Artisan Household） | craft_system | D | 赵农 2009、田自秉 2010 |
| xdup-0352 | 半地穴式建筑（Semi-Subterranean Dwelling） | building_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0353 | 南京云锦（Nanjing Yunjin Brocade） | textile_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0356 | 吉祥图案（Auspicious Motifs） | decorative_motif | C | 高丰 2004、田自秉 2010 |
| xdup-0357 | 哥窑（Ge Kiln） | ceramic_kiln | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0358 | 喜克索斯人（Hyksos） | social_group | E | 夏燕靖 2009、夏燕靖 2016 |

维度分布：A 0、B 19、C 2、D 4、E 1。

## 三、1 个 update：`terms/proto-porcelain.md`

- 原正文称“五册来源有直接记载（高丰一册全书无此词）”。复读高丰 2004 L1246-L1258 后确认：该册专设“陶瓷和原始瓷器的产生”一节，使用“原始瓷器”之名，引《中国陶瓷史》（文物出版社，1982，第 78 页）“原始瓷器是陶器向瓷器过渡阶段的产物……属于瓷器的低级阶段”，并记商代至东汉成熟瓷器约 1000 多年的过渡。
- 处理：新增高丰来源条目（L1246-L1258），正文改为“六册来源均有直接记载”，新增“命名由来与‘原始瓷器’”核心条目，aliases 增“原始瓷器（高丰用语）”，`source_count` 5→6，`version` 2→3，参考文献与验证状态同步补正。
- `xdup-0355` 的田自秉候选 rejected：该册原有来源绑定 L1917-L1919 已覆盖其内容，不重复计入。

## 四、1 个整组拒绝：`xdup-0354` 原始瓷

两册候选（夏燕靖 2009 L676-L684、李立新 2011 L640）均与既有 `proto-porcelain.md` 同指“陶—瓷过渡阶段的青釉器”，且该 KU 已绑定这两册的相应位置（夏燕靖 L678-L680、L683；李立新 L666）。因此整组不另立条目，2 个候选全部 rejected 并指向该 KU。这也消除了“原始瓷／原始瓷器／原始青瓷”三名并立的重复风险。

## 五、关键语义发现

1. **同名不同实的合称类条目**：五大名窑被赵农明确限定为“仅仅是一种习惯说法”，本批把这一限定写进正文，避免后续被当成严格分类。
2. **年代数值冲突的正规处理**：北京人存在“60 万至 23 万年前”（夏燕靖 2009）与“约 50 万年”（2016）两说；五代十国存在“53 年＋319 年”（赵农）与“约半个世纪”（2016）两种表述。均并列保留、不裁定。
3. **制度类条目的维度归属**：列鼎制度、作铺、匠户、包买主归 D（商业、制度与设计教育），而非 B；中山装归 D（服制与政治象征），避免与 B 的工艺条目混淆。
4. **过渡形态条目**：俎被高丰与夏燕靖同时指为后世几、案、桌的雏形，本批以“礼器—家具过渡形态”定位，未与凭几合并。
5. **“图必有意，意必吉祥”的分期差异**：高丰称形成于汉代、清代达高潮；田自秉只说明清最流行。两者并列。

## 六、状态与验证

- 工作包 `apply-plan.jsonl`：26 行（25 create + 1 update），哈希 26/26 与磁盘一致。
- `candidate-decision-ledger.jsonl`：107 行，状态链连续（26 条 canonical 三段链 + 29 条 rejected）。
- 内容质量审计：231 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 231/231 可解析。
- 候选索引：`sha256:e82bd95f...aca82`，7,209,591 B，5,339 行。
- 重复组关闭：term doc2 共 136 组，已关闭 29 组（本批 27 组），仍开 107 组、214 个成员；person doc2 保持 48/48 全部关闭。

## 七、边界与研究债

- 26 个条目均只依据前六册 Markdown 文本，未做来源外核对；`consensus` 统一为 `tentative`，验证层级未评定。
- 哥窑窑址、五大名窑排序、北京人与元谋人的绝对年代、南京云锦的具体藏品等，来源本身未给出一手数据，本批不补写。
- 透光镜的“铸造应力＋研磨压应力”解释仅见田自秉转述，未核原研究文献。
- Theme/Topic 均未 materialize，25 个条目只落到 Dimension；relation 未审查，正文只写导航性相关条目，不构成关系断言。
- 剩余 term doc2 107 组待下一批处理；`xdup-0364` 天鸡壶与 `xdup-0468` 鸡头壶天鸡壶须合并为一条，`xdup-0409` 百工制度与 `xdup-0450` 釉里红瓷按 `no_delta` 处理。
