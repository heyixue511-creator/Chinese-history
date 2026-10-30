# h52 层级试点批次总结：B.14.7 近现代家具

- 批次：`2026-10-30-hierarchy-pilot-h52`
- profile：`hierarchy-pilot-v1`
- 日期：2026-10-30
- 层级版本：v1.42 → **v1.43**
- 范围：Theme B.14 补建 B.14.7「近现代家具：人造材料、公共器具与竹作」，主挂载 3 个 KU

---

## 一、目标与范围

h50 在 Theme 未解决问题与 manifest 中登记「木作工艺层与风格层（14 条）与近代家具线（3 条）仍空」；h51 处置了前 14 条，把近代线剩为一笔：

> 近代家具线仍空：人造材料家具、公共器具、章水泉竹家具三条待独立批次。

本批处置的就是这三条。它们分属两种材料判断与一种使用场合判断，在来源中无一互引，也没有任何一册把它们并置。

| Topic | 覆盖内容 | KU | 册数口径 source_count |
|---|---|---|---|
| B.14.7 近现代家具：人造材料、公共器具与竹作 | 人造材料家具、公共器具、章水泉 | 3 | 2 |

不纳入的六类边界：竹编工艺体系（`procedures/zhubian-yishu-jiagong` 仍未挂载）、办公文具本体、器物形制、工业组织与生产体制（D 维度）、板式结构本体（结构侧已在 B.14.3）、明清器物与风格（B.14.4／B.14.5）。

---

## 二、结构物化

### 2.1 B.14.7

`primary_dimension: B`、`parent_theme: B.14`、`secondary_themes: [C, D]`、`status: pilot`，七节齐备。

研究问题：

> 三条各执一端——人造材料家具讲材料替代与结构转型，公共器具讲使用场合与配置，章水泉讲小竹片拼椅面——「家具在近代的变化，在六册里是被写成一条工业化的连续叙述，还是三处互不相干的片段？」

答案落在三条判断上，均写进 Topic 的理论支撑与未解决问题：

1. **三条的「近代」不在同一时点**——人造材料条以「解放后」为界，公共器具条只称「现代」，章水泉条只有广济／蕲州的产地沿革。
2. **竹作与工业化方向相反**——以小竹片拼合维持手工与地方材料，与以人造材料替代木材求省工相对；六册从未对照。
3. **板式结构的材料侧与结构侧出自同一段来源**（田自秉 L5367），本库拆挂两处，是七个 Topic 中唯一在证据侧不彻底的一刀。

### 2.2 Theme B.14 更新

- **核心问题**：五十条 → 五十三条，其余四十八条无尺寸；数据层五处不变。
- **边界**：新增近代三条纳入一条；原「近代家具线归待建 Topic，材料侧仍空」改写为「材料侧随人造材料家具条挂入 B.14.7、不重复挂载」；新增竹编工艺体系排除一条。
- **下属 Topic**：增列 B.14.7，分工段改为七个 Topic、两层，并明写「B.14.7 与 B.14.3 的分工是唯一在证据侧不彻底的一刀」。
- **支撑结构**：53 条、七个 Topic、role `term_anchor` 39／`source_publication` 4／`procedure` 3／`boundary_case` 2／`historical_context` 2／`representative_work` 2／`key_person` 1；来源赵农 30、夏燕靖 2016 17、高丰 13、田自秉 10、夏燕靖 2009 5、李立新 2。
- **未解决问题**：删除两条已闭合的「近代家具线未物化」，新增四条。
- **tags**：补 `人造板`、`钢管家具`、`板式结构`、`公共器具`、`章水泉`、`竹家具`。

### 2.3 索引

- `hierarchy/index.md` 升 **v1.43**，`evaluation_baseline: 2570 KU；805 KU 已挂载`，Topic 97；旧版归档为 `hierarchy/archive/v1.42.md`（87828 字节）。
- `themes/README.md`、`topics/README.md`、`dimension-candidates.md` 同步：五十二批共挂载 805 个；B 维度未挂载 1050 个；全库未挂载 1765 个。

同时修正了 h51 遗留的一处计数：`themes/README.md` 的 B.14 段来源分布仍是 h50 的 24/10/9/3/2/1，本批按实测改为 30/17/13/10/5/2，单册 39（双册 11、三册 1、五册 1）。

---

## 三、3 个 KU 挂载

| KU | 类型 | role | 承担什么 |
|---|---|---|---|
| `terms/renzao-cailiao-jiaju` | term | `term_anchor` | 解放后材料被人造板、钢管、塑料逐步替代；结构由框式向板式发展；更省工、轻便、简洁明快；钢管型材与电镀、深冲、冷弯、静电喷涂、红外烘烤 |
| `terms/gonggong-qiju` | term | `term_anchor` | 办公家具与公共场所器具两分、两类清单、「家具社会化的热闹景象」、按场合区分木材塑料压缩板材 |
| `persons/zhang-shuiquan` | person | `key_person` | 湖北广济（古称蕲州）竹家具名手；「用小竹片拼成椅面，用竹枝牙拼成图案」；端庄雅致；韩愈诗与《群芳谱》两处引证 |

分布：type `term 2 / person 1`；role `term_anchor 2 / key_person 1`；confidence `medium 3`；consensus `tentative 3`；来源 `田自秉 2010 2 / 赵农 2009 1`；来源重叠 `单册 3`——B.14.7 是 B.14 七个 Topic 中来源最薄的一处。

写回动作同 h51 模板：插入 `primary_theme`、`secondary_themes`、`role_in_theme`、`topic_memberships`；同步 `updated`、`version+1`、`hierarchy_scope_note`；正文补 `## 在层级体系中的位置` 四行。

---

## 四、边界处置

| 对象 | 处置 |
|---|---|
| 竹编工艺体系（`procedures/zhubian-yishu-jiagong`） | 仍未挂载。本 Topic 只取章水泉个人的拼竹做法，竹编方法与工具留待传统工艺线 |
| 办公文具（铅笔、钢笔、圆珠笔、橡皮、尺子、削刀、墨水） | 只作赵农「办公用品范围」的列举，不另立 KU，不判断文具是否属家具 |
| 办公桌椅、文件柜、沙发、折叠椅、影剧院座椅等 | 只作类别列举，不据列补形制、尺寸或图式 |
| 工厂、产量、采购与配置制度 | 归 D 维度（D.1、D.5） |
| `terms/banshi-jiegou` | 结构侧已在 B.14.3；材料侧同出一段来源，随本条挂入 B.14.7，不重复挂载 |
| 明式、清式、三大名作、红木、漆木家具、木画 | 归 B.14.4／B.14.5 |

---

## 五、执行与验证

| 检查 | 入口 | 结果 |
|---|---|---|
| 挂载写回 | 本批 mount 脚本（Temp，不入库） | `mounted 3 bad []` |
| frontmatter 复核 | 本批 verify 脚本（Temp，不入库） | 3 条 `primary_theme`、`role_in_theme`、`secondary_themes` 均符合；`version` 各 +1 |
| 结构压力测试 | `scripts/hierarchy_stress_test.py` | v1.43、themes 29、topics 97、membership 815、complete 805、incomplete 1765、`cross_dimension_topics: []`、`apply_permitted: false` |
| 关系索引 | `scripts/build_relation_index.py` | 7618（explicit 5998、inferred 1620、3/67） |
| 健康快照 | `scripts/write_current_health.py` | structural 130、ksq 58/65、content 0、`system_p0=0` |
| 关系一致性 | `scripts/audit_relation_consistency.py` | broken 0、invalid 0、missing inverse 0、weak evidence 0、unbaselined 0、isolated **1100**、over-connected 10 |
| 全量闭包 | `scripts/run_sync_closure.py --refresh-generated --full` | 连续两次全通过（250 tests + 16 subtests），第二次后 `rule_drift.findings` 归 0、backlog P0 清空 |
| 生成态对账 | `scripts/run_sync_closure.py --refresh-generated --check-generated` | 17/17 步执行，第 17 步以 exit=1 报生成态与 HEAD 不一致，属未 commit 的预期 |

闭包须连续跑两次的原因已在 h51 实测中确定：第 8 步 `write health and backlog` 先于第 9 步 `build output gallery and navigation`，单跑一次时 health 读到的仍是上一版 `05-outputs/index/index.md` 的 relation 数。

---

## 六、指标变化

| 指标 | v1.42 | v1.43 | 变化 |
|---|---|---|---|
| Theme | 29 | 29 | — |
| Topic | 96 | **97** | +1 |
| Topic membership | 812 | **815** | +3 |
| KU 已挂载（complete） | 802 | **805** | +3 |
| KU 未挂载（incomplete） | 1768 | **1765** | −3 |
| B 维度未挂载 | 1053 | **1050** | −3 |
| relation 总数 | 7612 | **7618** | +6 |
| member_of／inferred | 1614 | **1620** | +6 |
| 隔离单元 | 1102 | **1100** | **−2** |
| 结构健康 | 130/130 | 130/130 | — |
| 知识结构质量 | 58/65 | 58/65 | —（`hierarchy_assignment` 3/10 未变） |
| content findings | 0 | 0 | — |

两条口径：**relation +6 = 3 × 2**；**隔离单元 −2 不是 −3**（3 条中有 1 条原已有显式关系，取自前后两次实测，不按条数推算）。

---

## 七、语义边界：并列不裁

1. **「近代」的三个时点**——「解放后」／「现代」／只有产地沿革，三条无法排成序列，本库不替来源补年代。
2. **板式结构的双重归属**——材料侧与结构侧同出一段来源，拆挂 B.14.7 与 B.14.3，如实登记为「唯一在证据侧不彻底的一刀」，不合并、不改写来源段落。
3. **「拼」的两种含义**——章水泉的小竹片拼椅面是做法，板式结构的人造板是材料；来源未作区别，本库照录不裁。
4. **文具是否属家具**——赵农把文具列入办公用品范围，未作界定，本库照录不裁。

---

## 八、生成态与门禁

实际变化 8 个生成态／导航文件（计入 changed_files）：

`04-knowledge/quality/relation-index.yml`、`06-runtime/state/current-health.json`、`06-runtime/governance/governance-backlog.md`、`06-runtime/automation/index.md`、`06-runtime/state/generated-projections-manifest.json`、`05-outputs/index/index.md`、`knowledge-graph-data.js`、`knowledge-graph-data.json`。

`changed_files: 17 = apply-plan 9 行 + 8`。archive 快照 `hierarchy/archive/v1.42.md` 不计入。

门禁状态：保护路径零改动；分支 `main`、单一 worktree；HEAD 仍为 `c249c6fe`；**不 commit、不 push**。

---

## 九、未决事项与下一跳

### 已闭合

- h50／h51 连续登记的「近代家具线 3 条」——三条全部挂入 B.14.7。
- h49 以来的家具线缺口：B.14 至此七个 Topic 五十三条，器物层、解释层与近代线均有落点。

### 仍空（下一跳候选）

1. **竹编工艺体系**：`procedures/zhubian-yishu-jiagong` 无 `primary_theme`、无 `topic_memberships`；本批只取章水泉个人做法，竹编的选料、劈丝、编织与工具全无归属，需在传统工艺线（B.4）另立 Topic 或并入既有 Topic。
2. **D 维度生产体制**：人造材料家具的工厂、产量、材料工业与公共器具的采购配置制度均未挂，B.14.7 只覆盖材料、场合与做法三条。
3. **全库存量**：未挂载 1765、隔离 1100、B 维度未挂载 1050；`hierarchy_assignment` 仍 3/10 未变，本批不声称提升。
4. **文本债务**：B.14.3 边界「材料侧与该线三条仍空」一句未回改指向 B.14.7；h52 之外的存量债务不变（B.9 货币指向 B.13、水利 Topic、简单机械线、前近代服饰与甲胄等级 Theme、重复候选 reconcile 9 组、图注待核、A 维度遗留）。
5. **小债务**：`works/caihui-niaoshou-yuwen-qi-ge.md` 误称马王堆漆屏风；h48 赵农书名误作《中国艺术史》；h50 summary 指标表冗余写法；h51 未同步 `themes/README.md` 的 B.14 来源分布（本批已修正）。
