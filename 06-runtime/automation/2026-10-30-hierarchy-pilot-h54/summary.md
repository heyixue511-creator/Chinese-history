# h54 层级试点：另立 Theme B.16「简单机械与力学原理」并建立 Topic B.16.1

- 批次：`06-runtime/automation/2026-10-30-hierarchy-pilot-h54`
- profile：`hierarchy-pilot-v1`
- 日期：2026-10-30
- 层级版本：v1.44 → **v1.45**
- apply-plan：13 行；changed_files 21

## 一、目标与范围

本批把「简单机械线」从连续四批登记的债务变成结构节点。闭合对象是四处已落盘文本中的同一句话：

1. B.13 主题文件边界：「杠杆（`terms/lever`）与滑轮（`terms/pulley`）是力学原理与起重器具，不是计量标准；二者的概念雏形只在本 Theme 作参照引用，主归属留待简单机械线」。
2. B.13.2 Topic 边界：「不收杠杆与滑轮：两者是有原理而无器物的力学条目，属待建简单机械线」。
3. B.13 未解决问题：「杠杆与滑轮两条落在本 Theme 之外……简单机械线尚未物化」。
4. B.15 与 B.15.1 边界：「杠杆、滑轮归待建简单机械线」。

以及 h50、h51、h52、h53 四份 summary 第九节连续登记的下一跳。

不并入 B.12 或 B.13 的理由：B.12 的对象是农具与提水，B.13 的对象是标准物的可信度；两条原理条无器物、目的不在计量也不在提水，强行并入会使两个既有 Theme 的边界被撑破。

## 二、结构物化

- **Theme B.16**「简单机械与力学原理：杠杆、滑轮与省力器具」：`theme_code=B.16`、`primary_dimension=B`、`secondary_dimensions=[A]`、`status=pilot`、`source_basis` 六册。正文五节齐备。
- **Topic B.16.1**「省力原理与器具的分置：杠杆、滑轮、桔槔、辘轳与权衡秤器」：`primary_dimension=B`、`parent_theme=B.16`、`secondary_themes=[A]`、`status=pilot`、`source_count=4`。研究问题：**两条原理条声明无实物，四条器具条只写动作，二者在六册中从不互相引用——「省力」在这几册里是一条可推演的原理，还是一组各自使力气的器具？**

层级主轴仍为 `domain → dimension → theme → topic → KU`；B.16 是第 31 个 Theme、B.16.1 是第 99 个 Topic。

## 三、7 条 membership：本库首个「主挂载少于次挂载」的 Theme

| KU | 类型 | role | 归属 |
|---|---|---|---|
| [杠杆](../../../04-knowledge/units/terms/lever.md) | term | `term_anchor` | 主挂载（原无 Theme） |
| [滑轮](../../../04-knowledge/units/terms/pulley.md) | term | `term_anchor` | 主挂载（原无 Theme） |
| [墨经](../../../04-knowledge/units/publications/mo-jing.md) | publication | `supporting_source` | 主挂载（原无 Theme，跨三册） |
| [桔槔](../../../04-knowledge/units/terms/jiegou-well-sweep.md) | term | `term_anchor` | 次挂载（主挂 B.12.2） |
| [辘轳](../../../04-knowledge/units/terms/windlass.md) | term | `term_anchor` | 次挂载（主挂 B.12.2） |
| [权衡秤器](../../../04-knowledge/units/terms/hengqi-balance.md) | term | `term_anchor` | 次挂载（主挂 B.13.2） |
| [陶井](../../../04-knowledge/units/works/taojing.md) | work | `representative_work` | 次挂载（主挂 B.5.3） |

- 主挂载 3、次挂载 4。**这是本库首次出现主挂载对象少于次挂载对象**：六册中「简单机械」从未作为类别出现，能作主挂载的只有两条声明无实物的原理条与一部力学文本；真正有构造描述的器具全部主挂在提水、计量、明器三条既有线上，其主归属不应因本 Theme 建立而迁移。
- role：`term_anchor` 5、`supporting_source` 1、`representative_work` 1；类型 term 5、publication 1、work 1。
- 来源（按 KU 计，跨册重复计入）：赵农 2009 6、夏燕靖 2009 1、夏燕靖 2016 1、李立新 2011 1；`source_count` 4（按册计）。高丰 2004、田自秉 2010 零覆盖。
- confidence：medium 5、low 2（杠杆、陶井）；consensus 全部 tentative。

## 四、边界处置

`excluded_by_boundary` 已写入 manifest，八条。其中三条需要点明：

1. **翻车不入次挂载**：翻车是链式提水，与杠杆、轮轴、滑轮三者无直接原理关联；B.12.2 内部已把桔槔（杠杆配重）、辘轳（轮轴缠绕）、翻车（链式提水）三者列为「三种原理」，本批只取前两者的原理关联，不据「提水器具」这一集合标签收第三条。
2. **车轮、指南车、水碓不收**：同属轮轴或机械装置，但六册没有把它们与杠杆、滑轮并读；本批不据原理相似性扩收，避免把 Theme 变成按近邻词堆出来的容器。
3. **次挂载主归属未回改**：B.12.2、B.13.2、B.5.3 的正文与边界仍写「简单机械线尚未物化」，本批只登记为债务，不改动这三处正文。

## 五、执行与验证

- 写回：`h54_mount.py` 输出 `primary 3 secondary 4 bad []`；frontmatter 复核 3 条主挂载 `primary_theme: B.16`，4 条次挂载 `primary_theme` 保持 B.12／B.13／B.5 且各含 2 条 `topic_memberships`（一 `primary: true`、一 `primary: false`）。
- 索引升版四处：`hierarchy/index.md` → v1.45（Theme 30→31、Topic 98→99、Level 5 816/1754/830、double-mount 清单 10→14）；`themes/README.md`（31、新增 B.16 全段）；`topics/README.md`（99、新增 B.16.1 全段）；`dimension-candidates.md`（五十四批 816、B 未挂载 1039、全库 1754）。旧版归档为 `hierarchy/archive/v1.44.md`（92404 字节）。
- 实测：`hierarchy_stress_test.py` 报 themes 31、topics 99、membership 830、complete 816、incomplete 1754、`cross_dimension_topics` 为空、`apply_permitted: false`；`build_relation_index.py` 7644（explicit 5998、inferred 1646、3/67）；`audit_relation_consistency.py` broken 0、invalid 0、missing inverse 0、weak evidence 0、isolated 1093、over-connected 10；`write_current_health.py` structural 130/130、ksq 58/65（hierarchy_assignment 3/10）、content 0、`system_p0=0`。
- **生成态次序**：`run_sync_closure.py --refresh-generated --full` 的第 8 步早于第 9 步，relation 数变化后单跑一次会残留 `output_navigation_snapshot_stale`，必须连续跑两次；本批按此处理。
- `--check-generated` 为 17 步，第 17 步 `git diff --exit-code HEAD` 在未 commit 时必然 exit=1，属预期。

## 六、指标变化

| 指标 | v1.44 | v1.45 | 变化 |
|---|---|---|---|
| Theme | 30 | **31** | +1 |
| Topic | 98 | **99** | +1 |
| topic_memberships | 823 | **830** | +7 |
| complete assignments | 813 | **816** | +3 |
| incomplete assignments | 1757 | **1754** | −3 |
| double-mount KU | 10 | **14** | +4 |
| relation index | 7634 | **7644** | +10 |
| member_of / inferred | 1636 | **1646** | +10 |
| explicit | 5998 | 5998 | 0 |
| 隔离单元 | 1094 | **1093** | −1 |
| B 维度未挂载 | 1042 | **1039** | −3 |
| structural health | 130/130 | 130/130 | 0 |
| ksq | 58/65 | 58/65 | 0 |

**两处非整数推导，必须按实测记录，不按条数推算：**

- relation +10 而非 +14：3 条主挂载 × 2 = 6，4 条次挂载 × 1 = 4（次挂载侧原主归属已生成 theme `member_of`，只新增 topic `member_of`）。
- 隔离单元只减 1 而非 2：杠杆原有 2 条显式关系、原本不隔离；只有滑轮由隔离转为有边。

## 七、语义边界：并列不裁与不做的事

本批的三处判断是「并列照录」而非「择优裁定」：

1. **名实照录**：「滑车亦称滑轮」为同物两名；杠杆条把「权衡」与「衡器」并列为概念雏形而未区分所指；桔槔与辘轳同为井上装置而原理不同（配重／轮轴），来源未作对比。
2. **推测性回溯照录**：「杠杆原理是在石器时期，原始先民使用木棒猎取食物或撬动石块时体验和发现到的」无考古器物或图像支持，照录并标 low confidence，不把石器时期的木棒当作杠杆实物。
3. **《墨经》照录不训**：引文篇名未给，《经上》《经下》《经说》层次未分，「绳制挈之也」「挈，长重者下，短轻者上」只作平衡原理的解释，本库不逐句训释、不据引文反推构件。

不做的事：不从「省力」推比值。七条中无一处给力臂比、配重比、轮径比、起重能力或功率，因此「哪种器具更省力」在本 Topic 内不可比较，本库不据原理补写参数。

## 八、生成态与门禁

- 次序：manifest 与 summary 先落盘，再跑闭包。
- 全量闭包连续两次后，`rule_drift.findings` 归 0、backlog 为「No active items」。
- `--check-generated` 17 步，第 17 步 exit=1 属预期（未 commit）。
- 保护路径 `02-sources/` 零改动；分支 `main`、单一 worktree；HEAD 仍为 `c249c6fe`。
- **本包不 commit、不 push**——commit/push 需用户当次明确授权。

## 九、未决事项与下一跳

本批 12 条 unresolved 已写入 `manifest.json`，要点归四类：

**证据结构类**
- 原理条无实物、器具条无原理：两条原理条都不给支点位置、力臂长度、轮径或绳径；四条器具条只写动作。
- 唯一的实物证据来自别的线：权衡秤器（实物＋文本＋术语三层齐备）主挂 B.13.2，陶井图注（滑轮唯一器物侧证据）主挂 B.5.3；本 Topic 只能经次挂载读出。
- 证据类型三种而不通约：图像（泗水捞鼎）、实物（长沙楚墓等臂秤具、大冶铜绿山辘轳两件）、图注（陶井）。

**量化类**
- 全 Topic 零量化：无省力比值、无配重比与力臂比、无起重能力；唯一数量级信息是辘轳「两件」的件数。

**结构自陈类**
- 「简单机械」不是六册的类别，是本库为安置两条无实物的原理条而设的结构；3+4 的主次结构属本库首次，无同型先例可比，若后续认定器具主归属应迁移，需重估。

**跨批债务**
- B.12.2、B.13.2、B.5.3 三处正文与边界仍写「简单机械线尚未物化」，未回改指向 B.16.1。
- B.12 主题文件边界仍写水利工程「归待建水利 Topic 或 B.3」，未回改指向 B.15（h53 遗留）。

**下一跳优先级**：竹编工艺方法（`procedures/zhubian-yishu-jiagong`，仍无 `primary_theme` 与 `topic_memberships`）→ 前近代服饰与甲胄等级 Theme → B.9「货币归后续 Topic」等跨批文本回改批次。
