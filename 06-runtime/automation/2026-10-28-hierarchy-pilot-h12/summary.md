# h12 批次摘要：中国设计史书写与学科建构

- 批次：`2026-10-28-hierarchy-pilot-h12`
- 日期：2026-10-28
- 层级版本：v1.2 → v1.3
- 结论：新建 1 个 Theme（A.1 中国设计史书写与学科建构）与 2 个 Topic（A.1.1、A.1.2），挂载 14 个 KU；22 个 authored 文件，22/22 哈希匹配。未 commit、未 push。

## 一、目标与范围

h1–h11 已 materialize 11 个 Theme、27 个 Topic，并挂载 133 个 KU，覆盖 B、C、D 三个维度；A 维度有 198 个未挂载 KU，却没有任何 Theme 落点。本批为 A 维度建立首个 Theme，但严格限定在 `dimension-registry` 对 A 的定义——“如何写设计史”，而不是把器物、工艺、广告等具体史实搬入 A。

选择标准：

1. KU 的 `primary_dimension` 与目标 Theme 的维度一致；
2. KU 的核心内容属于“写史、命名、学科建构”，不是被书写的历史对象；
3. 同一对象只设一个主挂载；具体史实内容仍留在 B/C/D 的既有 Theme。

本批 14 个 KU 分两组：

- A.1.1 工艺美术史通史书写：田自秉、田自秉出版著作（1985）、田自秉修订本（2010）、王家树、龙宗鑫、1982 年《中国工艺美术史》编写完成事件；
- A.1.2 从工艺美术史到设计史：高丰、赵农、李立新、高丰《中国设计史》、夏燕靖《中国设计史》、赵农《中国艺术设计史》（2009）、夏燕靖《中国艺术设计史》（升级版）、《造物之迹》。

## 二、结构物化

### 新建 A.1

`04-knowledge/structure/themes/a1-zhongguo-shejishi-shuxie-xueke-jiangou.md`：

- `node_type: theme`、`theme_code: A.1`、`primary_domain: chinese-design-history`、`primary_dimension: A`、`secondary_dimensions: [D]`；
- 核心问题：1982–2016 年的工艺美术史／设计史通史如何建立研究对象、命名、分期与学科谱系；
- 边界纳入 4 位人物、9 部著作／学位论文与 1 个事件；排除具体设计史内容、D.4 的设计教育制度、设计思想史、西方设计史原典与 1949 年后的设计实践；
- 下属 Topic A.1.1、A.1.2；支撑结构 14 个 KU（4 人物、9 著作／学位论文、1 事件）；
- 未解决问题 9 条，含 1985／2010 版本关系、王家树与龙宗鑫书目一行、高丰出版年、夏燕靖两版对照、赵农十章结构、李立新后记一段、计划合写的《中国设计艺术史》未出版、1917 年许衍灼未挂载、分期概念留待 A.1.3。

### 新建 A.1.1

`04-knowledge/structure/topics/a1-gongyi-meishushi-tongshi-shuxie.md`：

- `node_type: topic`、`primary_dimension: A`、`parent_theme: A.1`、`secondary_themes: []`；
- `research_question` 追问 1980s–1990s 的中国工艺美术通史如何建立“工艺美术”的研究对象与通史体例，田自秉从 1982 年完成到 1985 年出版、2010 年修订的写作过程，与王家树、龙宗鑫的通史如何构成设计史之前的学科基础；
- 支撑材料 6 条：田自秉（key_person）、修订本（representative_work）、1985 年版／王家树／龙宗鑫（supporting_source）、1982 年编写完成（evidence_event）；
- 未解决问题集中于版本谱系、写作过程与“工艺美术”对象的历史性。

### 新建 A.1.2

`04-knowledge/structure/topics/a1-cong-gongyi-meishushi-dao-shejishi.md`：

- `node_type: topic`、`primary_dimension: A`、`parent_theme: A.1`、`secondary_themes: []`；
- `research_question` 追问 1990s–2010s 的“设计史”“艺术设计史”教材如何在对象、命名与分期上从“工艺美术史”分化出来，高丰、夏燕靖、赵农、李立新如何分别以“设计”“艺术设计”“造物”统摄中国通史；
- 支撑材料 8 条：高丰、赵农、李立新（key_person）；高丰书、夏燕靖 2009、赵农 2009、升级版（representative_work）；《造物之迹》（supporting_source）。

### 索引与导航更新

| 结构 | 修改 |
|---|---|
| 层级索引 | v1.3：12 Theme、29 Topic、151 membership、147 完整挂载、2423 未挂载；归档 v1.2 |
| themes/README、topics/README、dimension-candidates | 补 A.1 段、2 个 Topic 分工、12 Theme／29 Topic 计数与十二批挂载观察 |

A.1 与 D.4 的分工是本批的边界设计：A.1 取“如何写设计史”，D.4 取设计教育制度；具体设计史内容仍归 B/C/D。A.1.1 与 A.1.2 按“通史奠基—学科命名”分工，不重复计数同一 KU。

## 三、14 个 KU 的挂载与语义决定

14 个 KU 均写入 `updated: 2026-10-28`、`version: 2`；`last_verified` 不变。

### A.1.1（6 个主挂载）

- **田自秉**（person，`key_person`）：以 1982 年完成、1985 年出版、2010 年修订的《中国工艺美术史》写作过程为锚点。
- **田自秉《中国工艺美术史》修订本**（publication，`representative_work`）：以 2010 年修订本的体例与增补为锚点。
- **田自秉《中国工艺美术史》1985 年版**（publication，`supporting_source`）：作为修订本的版本对照，不写成另一部独立通史。
- **王家树《中国工艺美术史》**（publication，`supporting_source`）：只有书目一行，保留低置信度。
- **龙宗鑫《中国工艺美术史》**（publication，`supporting_source`）：只有书目一行，保留低置信度。
- **1982 年《中国工艺美术史》编写完成**（event，`evidence_event`）：作为写作过程的时间锚点，不作学科制度事件。

### A.1.2（8 个主挂载）

- **高丰**（person，`key_person`）：以《中国设计史》与“设计”命名的教材建构为锚点。
- **赵农**（person，`key_person`）：以《中国艺术设计史》的十章结构与“艺术设计”命名为锚点。
- **李立新**（person，`key_person`）：以《造物之迹》与“造物”统摄中国设计的论述为锚点。
- **高丰《中国设计史》**（publication，`representative_work`）：1990s–2000s 以“设计”命名的通史样本。
- **夏燕靖《中国设计史》**（publication，`representative_work`）：2009 年版教材样本。
- **赵农《中国艺术设计史》2009**（publication，`representative_work`）：以“艺术设计”命名的教材样本。
- **夏燕靖《中国艺术设计史》升级版**（publication，`representative_work`）：2010 年代教材修订与增补的样本；原 `hierarchy_scope_note` 误写“古代设计文献的锚点”，本批改为与 2016 教材相符的表述。
- **《造物之迹》**（publication，`supporting_source`）：李立新博士论文，作为“造物”命名的理论来源，不作独立教材。

人物取 `key_person`、核心教材取 `representative_work`、仅有书目一行或后记一段者取 `supporting_source`，是本批的置信度分层：不把王家树、龙宗鑫与田自秉写成同等详细的文本样本。

## 四、执行与验证

- `scripts/hierarchy_stress_test.py`：v1.3，12 Theme、29 Topic、151 membership、147 complete、2423 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`。
- `scripts/build_relation_index.py`：relation 6296（explicit 5998、inferred 298），`member_of` 298。
- `scripts/run_sync_closure.py --refresh-generated --full`：18/18，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：22 行（3 个 `structure_node_create`、14 个 `hierarchy_mount`、5 个 `structure_index_update`），22/22 `after_sha256` 重新计算匹配。
- 结构健康 130/130；知识结构质量 55/65，`hierarchy_assignment` 仍为 0，这是 2423 个 KU 未挂载的覆盖度信号。
- 内容质量发现 0；同名消歧 10/10；仓库审计断链 0。

## 五、指标变化

| 指标 | h11 后 v1.2 | h12 后 v1.3 | 变化 |
|---|---:|---:|---:|
| Theme | 11 | 12 | +1 |
| Topic | 27 | 29 | +2 |
| Topic membership | 137 | 151 | +14 |
| 完整挂载 KU | 133 | 147 | +14 |
| 未挂载 KU | 2437 | 2423 | −14 |
| Relation 总数 | 6268 | 6296 | +28 |
| `member_of` | 270 | 298 | +28 |
| 隔离单元 | 1456 | 1448 | −8 |
| 结构健康 | 130 | 130 | 0 |
| 知识结构质量 | 55/65 | 55/65 | 0 |
| 内容质量发现 | 0 | 0 | 0 |
| KU / claim / candidate / translation | 2570 / 1242 / 5339 / 2178 | 同左 | 0 |

`member_of` 增加 28：14 个 KU 各生成 1 条 Theme 关系，14 条 membership 各生成 1 条 Topic 关系。隔离单元只减少 8，表示 14 个新挂载 KU 中有 6 个原本已有其他显式关系；不能据此推断其余对象已被充分研究。

## 六、语义边界

- 本批只证明 147 个 KU 完成五级字段挂载，不证明全量挂载，也不证明 A.1 已是稳定分类。
- A.1 是“如何写设计史”的维度落点，不是“设计史内容”的容器；具体器物、工艺、广告、建筑、教育史实仍归 B/C/D，不因 A.1 建立而搬移。
- 田自秉 1985 年版与 2010 年修订本登记为两部著作，但两版的修订范围、增补章节与图版差异尚未核对；不能把修订本直接当作 1985 年版的重印。
- 王家树与龙宗鑫各只有书目一行；出版社、出版年、篇幅与具体章节均无法在现有语料中交叉验证，置信度低于田自秉。
- 高丰《中国设计史》的出版年与版次在不同来源中不一致，本批保留待核状态。
- 夏燕靖 2009 与 2016 两版是同一作者的两个教材版本，本批分挂 A.1.2 的两个样本位置，不合并为一条。
- 赵农《中国艺术设计史》的十章结构来自单一段落；章节标题与分期依据未逐章核对。
- 李立新《造物之迹》是博士论文，不是通史教材；本批只把它作为“造物”命名的理论来源，`supporting_source` 不升级为 `representative_work`。
- 李立新计划合写的《中国设计艺术史》只记录为未出版计划，不建 KU、不计入已完成著作。
- 1917 年许衍灼《中国工艺沿革史略》仍未挂载；它早于 1980s 通史，是否应扩展 A.1.1 的时间上限留待 A.1.3 或单独立项。
- 设计史分期与解释框架（大历史观、长时段、轴心时代、阶段性突破推进、变与统、六大设计文化区域、南秀北雄、本元特征、艺术设计史术语）尚未纳入，留待 A.1.3。
- E 维度仍不 materialize；巴拿马赛会、1851 年万国博览会、外来式建筑术语与旗袍继续作跨主题债务。

## 七、生成态与门禁

- `06-runtime/automation/index.md` 与 `06-runtime/state/generated-projections-manifest.json` 由完整闭包刷新；本批新增 1 个批次目录与 3 个 runtime 文件（`apply-plan.jsonl`、`manifest.json`、`summary.md`）。
- 生成态只作投影，不是知识裁决本体。
- h12 尚未 commit，发布门禁 `--refresh-generated --check-generated` 预期在 `[17/17] check generated snapshots` 以 `EXIT=1` 结束；该步等价于 `git diff --exit-code HEAD -- <GENERATED_PATHS>`，失败表示生成态快照与 HEAD 有差异，不是内容审计失败，也不是脚本给出的独立状态名。
- 本批未 commit、未 push；外部状态变更等待用户当次明确授权。

## 八、未决事项与下一跳

1. **A.1.3 设计史分期与解释框架**：大历史观、长时段、轴心时代、阶段性突破推进、变与统、六大设计文化区域、南秀北雄、本元特征与“艺术设计史”术语尚未 materialize；需先复读李立新与夏燕靖的相关章节，再决定是并入 A.1 还是单立 Theme。
2. **1917 年许衍灼《中国工艺沿革史略》**：民国时期工艺史书写是否纳入 A.1.1，需单独立项评估时间边界。
3. **田自秉两版对照**：1985 年版与 2010 年修订本的修订范围、增补章节与图版差异未核对。
4. **王家树、龙宗鑫**：只有书目一行；需查原书与出版信息，否则保持低置信度。
5. **高丰出版年**：不同来源的出版年与版次不一致，需核对版权页。
6. **赵农十章结构**：章节标题与分期依据来自单一段落，需逐章核对。
7. **夏燕靖两版对照**：2009 与 2016 两版的对象、章节与增补差异未逐条比较。
8. **计划合写的《中国设计艺术史》**：只记录为未出版计划，不建 KU。
9. **存量扩挂**：2423 个 KU 仍缺五级字段；单源 1919、tentative 2570、低置信 496、隔离 1448 继续作为研究债。
10. **E 维度**：仍不 materialize；巴拿马赛会、1851 年万国博览会、外来式建筑术语与旗袍继续作跨主题债务。
