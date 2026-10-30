# h49 货币与度量衡：B.13「货币与度量衡：交换媒介与计量标准」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h49/`
- 基线：v1.39（27 Theme／88 Topic／752 membership／742 complete／1828 incomplete／relation 7492／member_of 1494／isolated 1135／ksq 57/65／structural 130）。
- 目标：另立 Theme **B.13**「货币与度量衡：交换媒介与计量标准」，下建 B.13.1、B.13.2 两个 Topic，把前六册中货币与度量衡的 10 个 KU 主挂载进去，闭合 B.9 自 v1.28 起把货币列为「后续 Topic」的承诺。
- 结果：v1.40（28 Theme／90 Topic／762 membership／752 complete／1818 incomplete／relation 7512／member_of 1514／isolated 1131／ksq 57/65／structural 130）。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Theme `04-knowledge/structure/themes/b13-huobi-yu-duliangheng-jiaohuan-meijie-yu-jiliang-biaozhun.md`：`node_type: theme`、`theme_code: B.13`、`primary_dimension: B`、`secondary_dimensions: [D]`、`status: pilot`、16 个 tags；核心问题、边界、下属 Topic、支撑结构、未解决问题五节齐备。
- 新建两个 Topic：B.13.1「货币：从交钞到人民币」（支撑表 6 行）、B.13.2「度量衡：方升、秦量与权衡秤器」（4 行），七节齐备。
- 核心判断有四条。**覆盖不对称到极限是本 Theme 的第一事实**：10 条全部来自赵农 2009，高丰、夏燕靖两版、田自秉与李立新五册零覆盖，是本库第一条完全单册来源的 Theme（此前最偏的 B.12 为 21/30）；本批只登记该结构事实，不据此判定其余五册漏收。**器物面与制度面在来源中从未分开**：10 条只有两处量化（光绪龙洋「重 7 钱 2 分」与秦制换算「一尺约 23 厘米、一斤约 250 克、一升约 200 毫克」，末项照录标疑），纸币无印版尺寸与面额序列、银元无重量成色与版别、秦量秦权无单件实测、商鞅方升无尺寸容积与铭文字数。**可信度有四种来源且并列**：纸币写在票面（阑与花纹、料号、篆书「伪造交钞者斩」、印押、蒙汉两文并书），银元靠同重与统一（龙洋对齐鹰洋 7 钱 2 分、袁大头「质量稳定，币型统一」），度量衡写在诏书上（廿六年诏书见于山东出土的秦陶量），秤器靠杠杆本身（长沙楚墓春秋等臂秤具实物＋《墨子·墨经》衡木、本、标、权）。**货币与计量并置是本库的问题选择，不是来源的关联**：货币集中在赵农册第八章与第十章，度量衡集中在第三章「工具」与第四章「农具与工具」，六册从未并列讨论二者；本 Theme 并置的理由是它们同答「标准物靠什么取得可信度」。
- 快照：`hierarchy/index.md` 旧版归档为 `hierarchy/archive/v1.39.md`（76289 字节），再改写 index.md 为 v1.40。

## 三、10 个 KU 挂载

全部为主挂载（`primary_theme: B.13`，`role_in_theme` 与 membership 同值，`primary: true`），无次挂载。

- **B.13.1 货币（6）**：`terms/jin-dai-jiaochao`、`terms/yuan-dai-zhibi`、`terms/renminbi`（`term_anchor` 3）；`works/daqing-yinbi`、`works/yuandatou`（`representative_work` 2）；`works/moxige-yingyang`（`boundary_case` 1）。
- **B.13.2 度量衡（4）**：`terms/qin-liang`、`terms/qin-quan`、`terms/hengqi-balance`（`term_anchor` 3）；`works/shang-yang-fang-sheng`（`representative_work` 1）。

类型与角色：term 6、work 4；`term_anchor` 6、`representative_work` 3、`boundary_case` 1。`primary_dimension` 全部为 B，无新增跨维度挂载。`secondary_dimensions` 原为 D 的六条（三枚银元、两张纸币、人民币）保留 D，其余四条为空，本批不改动该字段。

## 四、边界处置

- **不收杠杆与滑轮**：`terms/lever`（low，只有原理与概念雏形、无实物）与 `terms/pulley`（定滑轮改变方向、《墨经》「绳制挈之也」、汉画像石「泗水捞鼎」）是力学原理与起重器具，不是计量标准；二者的概念雏形只在 Theme 内作参照引用，主归属留待待建简单机械线。
- **不收水利工程**：都江堰、灵渠、郑国渠、西门渠归待建水利 Topic 或 B.3。
- **不收货币制度与金融史**：交钞库、印造机构、通货膨胀成因、币制改革与铸造局归 D 维度；`primary_dimension` 为 D 的货币制度条目不入。
- **不收铸币与印钞工序**：合范、浑铸、分铸、失蜡、叠铸、铁范与六齐归 B.9.2 与 B.9.7；本 Theme 只取币面与票面的形制与流通事实。
- **不收票证、证券与邮票**：归 C 维度。
- **不收同章交通工具与近代机器**（自行车、人力车、汽车、磁悬浮、神舟五号）：虽同在赵农册第十章，与本 Theme 无共同问题。
- **不补建龙洋条目**：光绪龙洋的正面满汉文「光绪元宝」、背面蟠龙、重 7 钱 2 分只作为 `works/daqing-yinbi` 的「前承」存在，库内无独立 KU；本批不据钱币学通识补建。
- **鹰洋以 `boundary_case` 挂载**：它是 10 条中唯一的非中国制作品，却承担给龙洋提供重量锚点的功能；挂 `boundary_case` 而不作同类项，使「锚点来自外部」这一判断在表内可追踪。
- **不为《墨子》《史记》《战国策》建 publication 条目**：三书在库内无条目，本批只引赵农转录的引文。

## 五、执行与验证

1. 语义裁决先于执行：先扫描 B 维度未挂载 KU 得货币 6 条与度量衡 4 条，逐条读毕描述与 `hierarchy_scope_note`；另读 `terms/lever`、`terms/pulley` 评估归属，裁定排除。机械脚本 `h49_mount.py` 只消费已裁决清单。
2. 来源统计脚本实算：按完整 `evidence_ref.doc_id` 聚合（不用年份正则），得赵农 2009 覆盖 10 条（10/10），其余五册 0 条；单册 10；medium 8、low 2；tentative 10。
3. 写后复核实测：10 个文件 YAML 全部可解析，`primary_theme == 'B.13'`、`primary_dimension == 'B'`、`topic_memberships` 长度 1 且 `primary is True`、role 与 `role_in_theme` 一致，`bad []`；role 实测 `term_anchor` 6、`representative_work` 3、`boundary_case` 1，type 实测 term 6、work 4；`hierarchy_scope_note` 中「Theme/Topic 尚未 materialize」全部消去并改为「已挂载 B.13.1／B.13.2（货币与度量衡：交换媒介与计量标准）」。
4. `python scripts/hierarchy_stress_test.py`：v1.40、28 Theme、90 Topic、762 membership、752 complete、1818 incomplete、`cross_dimension_topics` 为空、`apply_permitted: false`。
5. `python scripts/build_relation_index.py`：7492→7512（explicit 5998 不变，inferred／member_of 1494→1514）。
6. `python scripts/write_current_health.py`：v1.40、complete 752、missing 1818、structural 130/130、ksq 57/65、content 0。
7. `python scripts/audit_relation_consistency.py`：isolated 1135→1131（减 4，见第六节）；broken target 0、invalid relation_type 0、missing inverse 0、weak evidence 0。
8. `python scripts/run_sync_closure.py --refresh-generated --full`：250 tests + 16 subtests 通过；刷新前 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，刷新后归 0。
9. apply-plan 17 行逐行复核 `after_sha256` 与磁盘一致（`rows 17 bad []`）；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree、HEAD 仍为 `c249c6fe`。

## 六、指标变化

| 指标 | v1.39 | v1.40 | 变化 |
|---|---|---|---|
| Theme | 27 | 28 | +1（B.13） |
| Topic | 88 | 90 | +2（B.13.1–B.13.2） |
| topic_memberships | 752 | 762 | +10 |
| 已完成挂载 KU | 742 | 752 | +10 |
| 未挂载 KU | 1828 | 1818 | −10 |
| B 维度未挂载 | 1113 | 1103 | −10 |
| relation_index | 7492 | 7512 | +20 |
| member_of | 1494 | 1514 | +20 |
| 隔离单元 | 1135 | 1131 | −4 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 20 = 10 条主挂载 ×（topic `member_of` + theme `member_of`）。隔离单元减 4 而非 10，因为实测 10 条中有 6 条原已有显式关系；该差值取自 `audit_relation_consistency.py` 前后两次实测，不是按条数推算。B 维度减 10，因为 10 条主挂载的 `primary_dimension` 全部为 B。membership 仍比 KU 多 10，双挂载与次挂载清单不变。

## 七、语义边界（并列不裁）

- **单册覆盖只作记录不作评价**：10 条全部来自赵农 2009，五册零覆盖。本库不据此判定五册「漏收」——六册的取材对象不同，但六册都没有明说取舍标准，因此该判断只以覆盖数字呈现。
- **两套杠杆原理并存不裁**：秦权条的称量法是等臂对称（提钮在衡标中心，「衡标平稳则物重相等，衡标不平则物重不等」），《墨子·墨经》引文讲的是不等臂关系（「本短标长」「标得权」）；二者是同一器制的两种表述还是两种器具，来源未说明，本批不裁。
- **丝本位与银本位两说并列**：元代纸币初以丝为本（《元史》「每银五十两易丝钞一千两」）、后改白银本位，转换时点未载；同段「禁金属货币」与「以铜币面值为交换单位」并存，如何相容亦未说明。
- **交钞与元代纸币的形制描述全部为史书摘引**：来源自己说明不据引文复原票面版式，本批遵守，不做版式推断，也不补钞版或票面摹本。
- **1154—1948 不排成演化线**：六条之间只有两处承继句（龙洋→大清银币的币制沿革、元代纸币「图案仿照宋代和金代交钞的样式」）；纸币与银元之间、银元与人民币之间均无连接句，按年代排列是本 Topic 的编排而非来源的判断。
- **「200 毫克」照录标疑**：秦制换算末项单位可疑（升应对应毫升），来源如此，本批不径改。
- **商鞅方升的跨域身份由来源给出**：「李斯根据秦国的石鼓文字和商鞅方升铭文的书写特点，制定了一种标准文字——小篆」是来源的连接句；但来源未描述方升形制与铭文内容，连接只有结论没有材料。
- **confidence 全 tentative**：medium 8、low 2（大清银币、鹰洋为 low），无一条 high；大清银币与鹰洋各只有一两句，`works/daqing-yinbi` 的 7 钱 2 分属表外前承而非其自身重量。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- 生成态陷阱复现并消解：relation 数变化后 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，全量闭包刷新后归 0。与 h13 以来历批一致。
- 首次闭包在第 14 步 `audit rule drift` 以 `exit=1` 终止，报 `runtime_index_snapshot_stale`，原因是 `manifest.json` 写在第 3 步 `build runtime index` 之后，索引缺少本批 manifest 字段。把 manifest 与 summary 落盘后重跑 `--refresh-generated --full`，18/18 步全部通过（250 tests + 16 subtests，126.27s），再复检 `audit_rule_drift.py` 为 0。该次失败如实记录，不改写为一次通过。
- `--refresh-generated --check-generated` 用于发布前比对：本批未 commit，工作区存在计划内改动，第 17 步 `check generated snapshots`（`git diff --exit-code HEAD`）以 `exit=1` 报漂移，属预期而非失败。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；250 tests + 16 subtests 通过。
- 本批 changed_files 25 = apply-plan 17 行（1 个 Theme 新建 + 2 个 Topic 新建 + 10 条主挂载 + 4 个索引更新）+ 8 个闭包重建的生成态／导航文件；归档 `hierarchy/archive/v1.39.md`（76289 字节）按 h44–h46 口径不计入。本批无需 Theme 节点更新行：被改写的 Theme 是新建的 B.13，已由 `structure_node_create` 覆盖。

## 九、未决事项与下一跳

- **货币线自此闭合，B.9 的边界文字尚未回改**：B.9 自 v1.28 起把货币列为「B.9 后续 Topic」，本批在结构上闭合该承诺，但 `themes/b9-*.md` 的边界与未解决问题两行仍写着「货币归后续 Topic」，需后续批次同步改写指向 B.13；本批不改 h48 以前的既有节点文字，以免与已归档的 apply-plan 哈希冲突。
- **简单机械线仍未物化**：杠杆（`terms/lever`）与滑轮（`terms/pulley`）自此明确落在本 Theme 之外，二者的原理与秤器、桔槔、辘轳、翻车都相关，但既非计量也非农具，尚无落点。
- **水利工程线仍未物化**：都江堰、灵渠、郑国渠、西门渠在库内已有条目，仍归待建水利 Topic 或 B.3。
- **家具与木作 Theme 仍是最大缺口**：朱然墓漆几、鸟足漆凭几、黑漆朱绘鸟足漆案、两件宝座的形制谱系都指向尚未建立的家具线。
- **前近代服饰与甲胄等级 Theme 未物化**。
- **D 维度前近代线仍只有 D.6（官府手工业六点）**：货币制度、计量制度与农政均不在其中。
- **重复候选 reconcile 9 组**未处理：鲁山窑瓷拍鼓与花釉腰鼓、琵琶与阮咸、白陶与商代白陶、花丝与花丝工艺、富好玉人与妇好墓玉人、玉雕龙与大玉龙、釉里红两写、竹里棋仙砖两写、青铜锤饰与单器条。
- **图注待核 12 条**、图 7-29 两指问题、未核图版 5-32 仍挂账；本批新增三处未核图版（图 8-57「元 钱币」、图 8-58「元 铁铸古阿拉伯数字六阶幻方」、图 10-48「壹佰圆人民币」），另有 `terms/qin-quan` 行段内的图 4-32「铁犁」图注归属待核。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1818、隔离 1131、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- **小债务**：`works/caihui-niaoshou-yuwen-qi-ge.md` 的「相关知识元」把 `simajinlong-mu-qi-pingfeng` 说成「马王堆漆屏风」，与实际文件不符，未擅改；h48 的 Theme 与 Topic 文献支撑把赵农书名写作《中国艺术史》，本批统一按 KU `sources.citation` 作《中国艺术设计史》，h48 文件未回改。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
