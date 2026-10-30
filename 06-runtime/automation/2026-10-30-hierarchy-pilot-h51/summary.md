# h51 层级试点批次总结：B.14 解释层四个 Topic

- 批次：`2026-10-30-hierarchy-pilot-h51`
- profile：`hierarchy-pilot-v1`
- 日期：2026-10-30
- 层级版本：v1.41 → **v1.42**
- 范围：Theme B.14 续建 B.14.3／B.14.4／B.14.5／B.14.6 四个 Topic，主挂载 14 个 KU

---

## 一、目标与范围

h50 把前六册（2004 高丰、2009 夏燕靖、2009 赵农、2010 田自秉、2011 李立新、2016 夏燕靖升级版）中坐具与坐姿 20 条、卧具屏风承具 16 条共 36 个 KU 挂进了 Theme B.14 的器物层，并在 Theme 未解决问题、summary 第九节与 manifest 三处同时登记同一笔债：

> 木作工艺层与风格层（14 条）与近代家具线（3 条）仍空，须由 B.14 的后续 Topic 承接。

本批处置的是这 14 条中的前 14 条——即木作工艺、用材、装饰、风格与文献五层，不含近代家具线。四刀的分工是：

| Topic | 覆盖内容 | KU | 册数口径 source_count |
|---|---|---|---|
| B.14.3 木作工艺与结构：榫卯、攒边与板式 | 结构 3 条 | 3 | 2 |
| B.14.4 家具用材与装饰：红木、漆木与木画镶嵌 | 用材与装饰 4 条 | 4 | 4 |
| B.14.5 明清家具风格与地域流派：明式、清式与三大名作 | 风格与流派 3 条 | 3 | 5 |
| B.14.6 家具文献与设计思想：从《燕几图》到《闲情偶寄》 | 文献与思想 4 条 | 4 | 3 |

`source_count` 记的是**来源册数**，不是 KU 条数——B.14.3 有三条却只出两册，B.14.6 四条也只得三册。

不纳入本批的六类边界（与 h50 一致）：建筑与营造本体（B.3）、漆器技法体系与漆器产品（B.11）、近代家具材料线（仍空）、图像本体（只作证据）、屏风织物（B.2／C）、四大名绣与竹木牙角雕刻（B.10／C）。

---

## 二、结构物化

### 2.1 四个 Topic

- **B.14.3「木作工艺与结构：榫卯、攒边与板式」**，`secondary_themes: [C]`。研究问题：三条里榫卯只有一句概述、攒边是唯一写出榫头—通槽装配关系的条目、板式只给结果不给节点——「连接方式在这三条里是以一种做法被描述，还是以一次结构转型被描述？」
- **B.14.4「家具用材与装饰：红木、漆木与木画镶嵌」**，`secondary_themes: [A, C]`。研究问题：「家具是以材料被人认识，还是以装饰被人认识？」
- **B.14.5「明清家具风格与地域流派：明式、清式与三大名作」**，`secondary_themes: [A, C]`。研究问题：「风格在六册里究竟由时代、宫廷还是产地界定？」
- **B.14.6「家具文献与设计思想：从《燕几图》到《闲情偶寄》」**，`secondary_themes: [A]`。研究问题：「家具知识在六册里是以『可照做的条目』被记录，还是以『名人名句』被引用？」

四个 Topic 均 `status: pilot`、`primary_dimension: B`、`parent_theme: B.14`，七节齐备（研究问题／边界／支撑材料／理论支撑／实证材料支撑／文献支撑／未解决问题）。

### 2.2 Theme B.14 更新

六处改动：

1. **核心问题**：由「三十六条」改为「五十条」；数据层段由「全 Theme 唯一一处推测尺度」改述为五处可用的尺度，并说明其中三组（漆木家具）出自同两条、只用来说明「低矮」或「不舒适」、不构成序列。
2. **边界**：新增解释层纳入一条（木作工艺、用材、装饰、风格与文献五层，B.14.3/4/5/6）；榫卯排除句改为「已挂入 B.14.3，建筑本体仍在 B.3」；漆器句改为「漆器技法体系与漆器产品归 B.11；漆木家具作为家具类别挂入 B.14.4」；近代线句补「板式结构只以结构侧挂入 B.14.3，材料侧与该线三条仍空」。
3. **下属 Topic**：增列四个链接，并把分工段改写为「器物层两个／解释层四个」，明写「六刀都是本库的取舍」。
4. **支撑结构**：理论支撑改为「结构判断层原有三条，后两条由 B.14.3 落地，第一条仍无器物条复现；数据层共五处」；实证改为 50 KU（term 42、work 2、procedure 2、publication 4；term_anchor 37、source_publication 4、procedure 3、boundary_case 2、historical_context 2、representative_work 2；medium 41 low 9；赵农 29、夏燕靖 2016 17、高丰 13、田自秉 8、夏燕靖 2009 5、李立新 2）；文献支撑改为田自秉提供攒边/板式/木画、李立新只参与两条。
5. **未解决问题**：删去已闭合的「木作工艺层与风格层未物化」，替换前三条并新增至十二条。
6. **tags**：补 `榫卯/攒边/红木/漆木家具/木画/明式家具/清式家具/家具文献`。

### 2.3 索引

- `hierarchy/index.md` 升 **v1.42**，`evaluation_baseline: 2570 KU；802 KU 已挂载`，Topic 96，Level 5 `802 个…1768 个…812 条`；旧版归档为 `hierarchy/archive/v1.41.md`（83807 字节）。
- `themes/README.md`、`topics/README.md`、`dimension-candidates.md` 同步：五十一批共挂载 802 个；B 维度未挂载 1053 个；全库未挂载 1768 个。

---

## 三、14 个 KU 挂载

主挂载逐条（role 均为本批判定）：

| KU | 类型 | role | 承担什么 |
|---|---|---|---|
| `procedures/sunmao-jiegou` | procedure | procedure | 只取「干栏式建筑采用了榫卯结构」一句与建筑史判断；榫卯类型、构件部位、工具与工序全无 |
| `procedures/cuanbian` | procedure | procedure | 四边 45 度格角榫、中心板出榫入通槽、伸缩余量、不露截板纹三项作用 |
| `terms/banshi-jiegou` | term | term_anchor | 「由传统的框式向板式结构发展」的结果判断与材料前提 |
| `terms/hongmu` | term | term_anchor | 明清稀有硬木统称、「从一开始就不是某一特定树种」、性脆味酸、南方称酸枝 |
| `terms/qimu-jiaju` | term | term_anchor | 以木为胎、髹漆为饰的类别定义、五品种与三组尺寸 |
| `terms/muhua` | term | procedure | 染色象牙鹿角黄杨木制花纹、镶嵌于木器的装饰工艺 |
| `works/muhua-qiju` | work | representative_work | 木画纹样、两侧金环抽屉与相连机关、屉内龟形盒 |
| `terms/ming-style-furniture` | term | term_anchor | 五册共识的年代、两类用材、榫卯结构、审美概括与杨耀的概念史 |
| `terms/qing-style-furniture` | term | term_anchor | 三期说、三产地、三条整体风格与太师椅座高 50－52 厘米 |
| `terms/qingdai-jiaju-sanda-mingzuo` | term | term_anchor | 苏作广作京作的合称与两句地方特色 |
| `publications/yanji-tu` | publication | source_publication | 宋黄伯思撰、几桌拼接与「由实践上升到理论」的组合设计意识 |
| `publications/lubanjing` | publication | source_publication | 明万历刊、图 1 卷文 3 卷、实用指南通书、含家具形制与尺寸 |
| `publications/mingshi-jiaju-yanjiu` | publication | source_publication | 王世襄专著；只取鸡翅木分老新两类这一鉴定依据 |
| `publications/xianqing-ouji` | publication | source_publication | 1671 年成书、六卷卷目、功能实用第一与「宜简不宜繁」判准 |

分布：type `procedure 2 / term 7 / work 1 / publication 4`；role `procedure 3 / term_anchor 6 / representative_work 1 / source_publication 4`；confidence `medium 14`；consensus `tentative 14`；来源 `夏燕靖 2016 7 / 田自秉 2010 7 / 赵农 2009 5 / 高丰 2004 4 / 夏燕靖 2009 2`，李立新 2011 在解释层零覆盖；来源重叠 `单册 7 / 双册 5 / 三册 1 / 五册 1`，无六册全覆盖条目。

每条 KU 的写回动作（同一模板）：在 `primary_dimension: B` 之后插入 `primary_theme`、`secondary_themes`（把既有 `secondary_dimensions` 镜像为裸码）、`role_in_theme`、`topic_memberships`；同步 `updated: 2026-10-30`、`version+1`、`hierarchy_scope_note` 去尾标点后拼「已挂载 <TOPIC_CODE>（<THEME_TITLE>）。」；正文补 `## 在层级体系中的位置` 四行。

---

## 四、边界处置

| 对象 | 处置 |
|---|---|
| 干栏式建筑本体、抬梁穿斗井干三式、应县木塔、拼合梁 | 归 B.3。榫卯只以「干栏式建筑采用了榫卯结构」一句与建筑史判断挂入 B.14.3 |
| 漆器技法体系与漆器产品 | 归 B.11。仅漆木家具作为家具类别挂入 B.14.4 |
| 人造材料家具、公共器具、章水泉竹家具 | 仍空，待独立批次；板式结构只取结构侧挂入 B.14.3，材料侧不挂 |
| 《韩熙载夜宴图》《重屏会棋图》《捣练图》《清明上河图》《十八学士图》、敦煌壁画 | 只作条目内证据，不建 KU，不据图补写形制 |
| 夹缬屏风、宋锦、八达晕 | 归 B.2／C；本 Theme 只取屏风的器物形制 |
| 四大名绣与竹木牙角雕刻工艺 | 归 B.10／C；木画与红木只取家具装饰侧 |

另有三处**同层归属裁决**，均记入对应 Topic 的边界节而非 Theme 边界：攒边工序归 B.14.3（风格条不重复收）、具体器物形制归 B.14.1／B.14.2（风格条只取风格侧）、三作差异只在清式条内展开而不另立条目。

---

## 五、执行与验证

| 检查 | 入口 | 结果 |
|---|---|---|
| 挂载写回 | 本批 mount 脚本（Temp，不入库） | `mounted 14 bad []` |
| frontmatter 复核 | 本批 verify 脚本（Temp，不入库） | `KUs 14 bad []`；role/type/conf/topic/source/secondary 六组分布与四个 Topic 文件所写一致 |
| 结构压力测试 | `scripts/hierarchy_stress_test.py` | v1.42、themes 29、topics 96、membership 812、complete 802、incomplete 1768、`cross_dimension_topics: []`、`apply_permitted: false` |
| 关系索引 | `scripts/build_relation_index.py` | 7612（explicit 5998、inferred 1614、3/67） |
| 健康快照 | `scripts/write_current_health.py` | structural 130、ksq 58/65、content 0 |
| 关系一致性 | `scripts/audit_relation_consistency.py` | broken 0、invalid 0、missing inverse 0、weak evidence 0、unbaselined 0、isolated **1102**、over-connected 10 |
| 全量闭包 | `scripts/run_sync_closure.py --refresh-generated --full` | 连跑两次均 18 步全通过（250 tests + 16 subtests），第二次后 `rule_drift.findings` 归 0、backlog P0 清空 |
| 生成态对账 | `scripts/run_sync_closure.py --refresh-generated --check-generated` | 17/17 步执行，第 17 步 `check generated snapshots` 以 exit=1 报生成态与 HEAD 不一致，属未 commit 的预期 |

闭包前 `write_current_health.py` 曾使 `system_p0` 由 0 变 1：`rule_drift` 报唯一一条 `output_navigation_snapshot_stale`，`05-outputs/index/index.md` 声明 relation 数 7584 而期望 7612。原因是先在索引编辑前重建了 `relation-index.yml`，尚未跑闭包第 9 步 build output gallery——属闭包前的**预期中间态**。

需要如实记录一处**闭包内的快照次序**：单跑一次全量闭包并不能清掉这条 P0。闭包第 8 步 `write health and backlog` 先于第 9 步 `build output gallery and navigation`，所以第一次闭包写出的 health／backlog 读到的仍是上一版 `05-outputs/index/index.md`（7584），P0 仍在；第 9 步把该文件改为 7612 之后，**第二次全量闭包**的第 8 步才读到正确值，`rule_drift.findings` 归 0、backlog 显示「No active items」。这不是缺陷而是生成态的写入次序，任何改动 relation 总数的批次都会如此，处理办法是连续跑两次闭包，第二次确认归零。

---

## 六、指标变化

| 指标 | v1.41 | v1.42 | 变化 |
|---|---|---|---|
| Theme | 29 | 29 | — |
| Topic | 92 | **96** | +4 |
| Topic membership | 798 | **812** | +14 |
| KU 已挂载（complete） | 788 | **802** | +14 |
| KU 未挂载（incomplete） | 1782 | **1768** | −14 |
| B 维度未挂载 | 1067 | **1053** | −14 |
| relation 总数 | 7584 | **7612** | +28 |
| member_of／inferred | 1586 | **1614** | +28 |
| 隔离单元 | 1110 | **1102** | **−8** |
| 结构健康 | 130/130 | 130/130 | — |
| 知识结构质量 | 58/65 | 58/65 | —（`hierarchy_assignment` 3/10 未变） |
| content findings | 0 | 0 | — |

两条口径必须分开说：

- **relation +28 = 14 × 2**（每条主挂载生成 topic 的 `member_of` 与 theme 的 `member_of`），explicit 5998 不变。
- **隔离单元 −8 不是 −14**：14 条中有 6 条原本已有显式关系，取自 `audit_relation_consistency.py` 前后两次实测，不按条数推算。

---

## 七、语义边界：并列不裁

本批遇到四处来源内部不一致，全部并列保留，不做合并或择优：

1. **红木两义**——既说「明清以来对稀有硬木的统称」，又说「从一开始就不是某一特定树种」；前义指向一个材料类别，后义否定该类别有固定外延。
2. **苏作评价两说**——一说苏作为明式正宗与精雅代表，一说苏作清中期后因追求繁复而衰退；两说分属不同册、不同段落，来源未作时间切分。
3. **清式三说**——一册以三期说与造办处广木作立论，一册以三产地立论并用太师椅座高 50－52 厘米作风格分析，一册以三作工艺差别立论；评价方向一致偏低，但判据不同，不可合并为一句。
4. **《鲁班经》两处文字**——「年荣」疑为「午荣」之讹、「雕新」疑 OCR 有误，照录标疑，未据他本回改；《闲情偶寄》书名「寄／记」异写同样照录。

另有两处**本库判断**（不是来源判断），已在 Topic 与 manifest unresolved 中标明：三条结构判断之间无过渡证据；器物层与解释层不共享任何来源段。

---

## 八、生成态与门禁

本批实际变化 8 个生成态／导航文件（不计入 apply-plan，计入 changed_files）：

`04-knowledge/quality/relation-index.yml`、`06-runtime/state/current-health.json`、`06-runtime/governance/governance-backlog.md`、`06-runtime/automation/index.md`、`06-runtime/state/generated-projections-manifest.json`、`05-outputs/index/index.md`、`knowledge-graph-data.js`、`knowledge-graph-data.json`。

`changed_files: 31 = apply-plan 23 行 + 8`。archive 快照 `hierarchy/archive/v1.41.md` 按 h44–h46 口径不计入。

门禁状态：保护路径零改动；分支 `main`、单一 worktree；HEAD 仍为 `c249c6fe`；**不 commit、不 push**。

---

## 九、未决事项与下一跳

### 已闭合

- h50 登记的「木作工艺层与风格层 14 条仍空」——14 条全部挂入 B.14.3–B.14.6，Theme 的未解决问题、README 与 dimension-candidates 三处同步改写。

### 仍空（下一跳候选）

1. **近代家具线 4 条**：`terms/renzao-cailiao-jiaju`（人造材料家具）、`terms/gonggong-qiju`（公共器具）、`persons/zhang-shuiquan`（章水泉竹家具），以及板式结构的材料侧。这是 h49/h50/h51 三批连续挂账的同一笔债，建议作为 h52 的独立批次。
2. **Style／文献层的四条债务**：明式与明代家具的界线未划清、三大名作未展开三作差异、《鲁班经》与《闲情偶寄》原书未核、《明式家具研究》只作鉴定依据。
3. **全库存量**：未挂载 1768、隔离 1102、B 维度未挂载 1053；`hierarchy_assignment` 仍 3/10 未变，本批不声称提升。
4. **其他待办**（非家具线）：B.9 主题文件「货币归后续 Topic」需回改指向 B.13；水利 Topic（都江堰、灵渠、郑国渠、西门渠）；简单机械线（杠杆、滑轮）；前近代服饰与甲胄等级 Theme；重复候选 reconcile 9 组；图注待核 12 条与未核图版 5 条；A 维度遗留（A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》）。
5. **小债务**：`works/caihui-niaoshou-yuwen-qi-ge.md` 误称马王堆漆屏风；h48 赵农书名误作《中国艺术史》；h50 summary 指标表 `| Topic | 92 | 92 → **92** | +2（90 → 92） |` 一行冗余写法待回改。
