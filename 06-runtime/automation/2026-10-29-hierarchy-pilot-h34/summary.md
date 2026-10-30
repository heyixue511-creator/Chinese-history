# h34 批次摘要：B.7 玻璃与料器（仿玉、输入与本土生产）

## 一、目标与范围

本批新建 B 维度第三条前近代 Theme：B.7「玻璃与料器：仿玉、输入与本土生产」，下建 3 个 Topic，挂载 10 个 KU（8 个主挂载、2 个次挂载）。

基线为 v1.24：21 Theme、63 Topic、477 membership、473 complete assignments、2097 个 KU 未挂载、relation index 6948。本批不动 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`，不改写任何既有 KU 的正文证据，只更新其层级字段与「在层级体系中的位置」段。

## 二、结构物化

### 新建 B.7「玻璃与料器：仿玉、输入与本土生产」

- `theme_code: B.7`、`primary_dimension: B`、`secondary_dimensions: [E, D]`，`source_basis` 六册，`date: 2026-10-29`。
- 核心问题四层：
  - 三名分裂：田自秉给琉璃两个义项（原始玻璃／建筑铅釉陶），并记玻璃制品后称料器；琉璃、玻璃、料器三名指同一材料的不同阶段与用途。B.5.4 已取第二义，B.7 取第一义。
  - 仿玉：琉璃璧最大直径 16 厘米，剑饰、印章多仿玉器作代用品；长沙 100 多座楚墓中 80 多座出琉璃璧；两汉玻璃器 6500 余件（碗、带钩、璧、耳珰、珠），并有模仿「金缕玉衣」的玻璃衣片；铸造成型法由仿件要求决定。
  - 沉浮：李立新的玻璃器序列（春秋末已有、战国西汉具规模、东汉魏晋衰落、隋唐再兴、唐后低潮、元末明初博山作坊、清康熙宫廷玻璃厂、近代设厂）与田自秉的两条解释（替代材料竞争、「质地没有过关」）。
  - 成分冲突：田自秉与高丰记铅钡玻璃，李立新记钠钡玻璃，六册均无检测数据。
- 边界 8 条，明确排除建筑琉璃（B.5.4）、玉器本体（玉石线未建）、伊斯兰与萨珊玻璃流通（E.2）、造办处机构（D.6.6）、近代玻璃工厂的资本与产业制度（D.1／B.4）、延安玻璃厂（B.4.2）、玻璃器纹样母题与造型风格（C）。
- 三个 Topic 按「代用—输入—工业」分工，三者是三种进入方式，不是三个进步阶段。
- 支撑结构 10 个 KU（B.7.1 三、B.7.2 二、B.7.3 五），`term_anchor` 3、`geographical_context` 2、`boundary_case` 1、`representative_work` 2、`evidence_event` 1、`procedure` 1；未解决问题 13 条。

### 新建三个 Topic

- **B.7.1「仿玉与代用：战国至两汉的玻璃器」**（`research_question` 185 字）：支撑琉璃（`term_anchor`，次挂载）、长沙楚墓群（`geographical_context`）、带钩（`boundary_case`）。三层「器形代用—材料命名—量化普及」，三条判断：代用不只决定器形也决定成型法；成分名由对比框架而非样本建立；普及度只能证到「楚墓中常见」与「两汉已有相当数量」。
- **B.7.2「输入与本土：魏晋至隋唐的玻璃器」**（183 字）：支撑网纹玻璃杯（`representative_work`）、法门寺塔基地宫（`evidence_event`，次挂载）。三层「本土制造物证—输入物证—兴衰解释」，三条判断：四批出土能证「境内能造」而证不到「本土吹制」；输入依赖器类与风格而非成分或产地标记；「沉浮」在本段是解释对象而不是已证事实。
- **B.7.3「料器与玻璃工业：博山、造办处玻璃厂与近代设厂」**（185 字）：支撑料器与玻璃（`term_anchor`）、套料（`procedure`）、荷花纹套红料缸（`representative_work`，图注级）、山东博山（`geographical_context`）。三层「料器作为工艺子类—三种生产组织—材料工业转向」，三条判断：料器是玻璃的工艺子类；三种组织不能排成演进线；转向的标志是用途与成型法，但完成时点无法确定。

### 既有结构更新

- `hierarchy/index.md` v1.24→v1.25；`archive/v1.24.md` 为改动前原样副本（46,111 字节，逐字节一致，`sha256:a855defd…`）。
- `themes/README.md`（21→22 Theme，新增 B.7 段）、`topics/README.md`（63→66，新增 B.7 下 3 个与分工段）、`dimension-candidates.md`（三十三批 473→三十四批 481，新增 B.7 bullet，B 维度未挂载约 1157→1149，全库 2097→2089）同步。
- `themes/b5-…md` 与 `topics/b5-diwen-you-tao-sanci-liuli.md` 中「第一义待玻璃材料 Theme 建立后另处挂载」改为「已由 B.7.1 以次挂载承接」；`topics/b6-youtao-dao-ci-zaoqi-ciqi.md` 支撑表法门寺行补注「伊斯兰玻璃器一环另由 B.7.2 次挂载」。

## 三、10 个 KU 的挂载

| KU | 类型 | role | Topic | version |
|---|---|---|---|---|
| `places/changsha-chumuqun.md` | place | `geographical_context` | B.7.1 | 2→3 |
| `terms/belt-hook.md` | term | `boundary_case` | B.7.1 | 2→3 |
| `works/wangwen-boli-bei.md` | work | `representative_work` | B.7.2 | 1→2 |
| `terms/liaoqi.md` | term | `term_anchor` | B.7.3 | 1→2 |
| `procedures/taoliao.md` | procedure | `procedure` | B.7.3 | 1→2 |
| `works/hehua-wen-taohong-liaogang.md` | work | `representative_work` | B.7.3 | 1→2 |
| `places/shandong-boshan.md` | place | `geographical_context` | B.7.3 | 1→2 |
| `terms/glass.md` | term | `term_anchor` | B.7.3 | 1→2 |
| `terms/liuli.md` | term | `term_anchor` | B.7.1（次挂载，B.5.4 仍为主挂载） | 3→4 |
| `places/famen-si-digong.md` | place | `evidence_event` | B.7.2（次挂载，B.6.1 仍为主挂载） | 4→5 |

- 8 个主挂载 KU 均写入 `primary_theme: B.7`、`secondary_themes: []`、`role_in_theme`、一条带 `primary: true` 与 `scope_note` 的 `topic_memberships`，`hierarchy_scope_note` 与 `scope_note` 逐字相同并保持为 frontmatter 末字段；正文「在层级体系中的位置」为六行段。
- 2 个次挂载 KU 保留原 `primary_theme`（B.5／B.6）与原主挂载，在既有 membership 后追加 `primary: false` 条目；`hierarchy_scope_note` 改为合并句，`hierarchy_scope_note` 仍为末字段；正文 `topic_memberships` 行并列两条并附主／次标记。

scope 摘要：长沙楚墓群只取「100 多座中 80 多座出琉璃璧」一条量化证据；带钩只取两汉玻璃带钩与铸造成型法，带钩的服饰用法归服饰线；网纹玻璃杯只取器物本体；料器取定义、品种与四法；套料取套烧—磨花工序；荷花纹套红料缸为图注级单器，仅证明套红为套料配色之一；山东博山取元末明初作坊、清代百余家与近代设厂的时间序列；玻璃取原料、五道工序、吹塑与模压、四类用途与 1949 年后建厂布局；琉璃次挂载只取第一义；法门寺次挂载只取 20 件伊斯兰玻璃器与萨珊风格一环。

## 四、边界处置

| 对象 | 处置 | 理由 |
|---|---|---|
| 建筑琉璃与琉璃烧造 | 归 B.5.4 | 琉璃的第二义（铅釉陶、琉璃瓦、琉璃塔）与 `procedures/liuli-shaozhao.md` 仍由 B.5.4 主挂载 |
| 玉器本体（玉璧、玉具剑、玉印、玉衣） | 不挂载 | 玉石线尚未建立，B.7 只取玻璃仿玉的代用关系 |
| 伊斯兰玻璃、萨珊玻璃的流通 | 归 E.2 | 本 Theme 只取「中国境内出土的输入品」一面 |
| 造办处机构沿革、编制与匠役 | 归 D.6.6 | B.7.3 只取玻璃厂作为玻璃生产组织的一环 |
| 近代玻璃工厂的资本与产业制度 | 归 D.1／B.4 | B.7.3 只取材料与成型工艺的转变 |
| 延安玻璃厂 | 归 B.4.2 | 只在近代玻璃工业处交叉引用，不重复挂载 |
| 料器的纹样母题、配色与花球造型 | 归 C | B.7.3 只把套红、搅料作为工序 |
| 隋李静训墓玻璃器 | 不单独立目 | 只有一句，无件数、器类与尺寸，只作 B.7.2 旁证 |
| 山东莒县陶尊等图注单条 | 不挂载 | 无功能或工艺结构可指认，保留在图注待核队列 |

## 五、执行与验证

- `scripts/hierarchy_stress_test.py` → `hierarchy_version: v1.25`、themes 22、topics 66、topic_memberships 487、complete_assignments 481、incomplete_assignments 2089、themes_without_topics 0、cross_dimension_topics []、apply_permitted false。
- `scripts/build_relation_index.py` → 6966 条（explicit 5998、inferred_by_rule 968、migrated_from_related 0）。较基线 +18：10 条新 membership 各生成 1 条 topic `member_of`（+10），8 个主挂载另各生成 1 条 theme `member_of`（+8）；琉璃与法门寺的 `primary_theme` 不变，不生成第二条 theme 边。
- `scripts/write_current_health.py` → v1.25、complete 481、missing 2089、relation 6966、isolated 1280、structural_health 130、knowledge_structure_quality 56/65、rule_drift 0、system_p0 0。
- `apply-plan.jsonl` 22 行（4 `structure_node_create`、10 `hierarchy_mount`、8 `structure_index_update`），闭包后复核 22/22 哈希与磁盘一致。
- 闭包首次运行后 `05-outputs/index/index.md` 的 relation 快照由 6948 更新为 6966，而 `current-health.json` 在生成序列中先写，曾记录 `output_navigation_snapshot_stale`；重跑 `write_current_health.py` 后 `rule_drift` 归 0。

## 六、指标变化

| 指标 | v1.24 基线 | v1.25 结果 |
|---|---|---|
| Theme | 21 | 22 |
| Topic | 63 | 66 |
| Topic membership | 477 | 487 |
| 完成五级挂载 KU | 473 | 481 |
| 未挂载 KU | 2097 | 2089 |
| relation index | 6948 | 6966 |
| member_of | 950 | 968 |
| 隔离单元 | 1283 | 1280 |
| structural_health | 130 | 130 |
| knowledge_structure_quality | 56/65 | 56/65 |
| 库存 KU | 2570 | 2570 |

B.7 主挂载 8 个 KU、次挂载 2 个，共 10 条 membership。隔离单元只减 3（套料、荷花纹套红料缸、山东博山），其余 5 个新挂载 KU 原已有显式关系；次挂载不改变琉璃与法门寺的既有关系位置。

## 七、语义边界

1. B.7 不写「中国玻璃发展史」，只写三种进入方式各自能证到什么程度：代用层缺成分数据，输入层缺窑址与工艺痕迹，工业层缺产量与配方。
2. 三名不统一：琉璃、玻璃、料器按来源用词照录；琉璃两义中建筑铅釉陶义仍归 B.5.4，B.7 只取第一义。
3. 成分名铅钡（田自秉、高丰）与钠钡（李立新）并列不裁；六册均无检测数据，本库不据来源外材料补写。
4. 「代用决定成型法」是本库解释，不是来源原话：来源只说「制作方法相似，采用铸造成型法」，未把因果写成「因仿玉而铸造」。
5. 四批出土能证「魏晋南北朝中国境内能生产玻璃器皿」，不能证「四批都是本土吹制、且与输入品可区分」；成分与工艺痕迹均缺。
6. 宫廷玻璃厂、博山作坊群与近代工厂是三种并存的组织记录，不是「宫廷—作坊—工厂」演进线；三者之间无沿革、人员、产品或产量的承接记录。
7. 荷花纹套红料缸为图注级证据（`confidence: low`），只证明套红为套料配色之一，不作器形或装饰的独立证据。
8. 玻璃与瓷器、漆器、铜器的替代关系只有田自秉一句「铜器、漆器、瓷器大量生产」与「质地没有过关」，不据此写替代率或价格比较。

## 八、生成态与门禁

- `hierarchy/index.md` 升版并归档 `archive/v1.24.md`（46,111 字节，与改动前逐字节一致，`sha256:a855defd6493cc47f9a7fee0246e82657ed492f0fb4f5a4a3e5938d3c75cd651`）。
- `relation-index.yml`、`current-health.json`、`governance-backlog.md`、`generated-projections-manifest.json`、`06-runtime/automation/index.md` 由刷新步骤重建，不在 apply-plan 内。
- `run_sync_closure.py --refresh-generated --full` → **18/18 通过**（`sync closure passed`，`250 passed, 16 subtests passed`，69.91s）。
- `run_sync_closure.py --refresh-generated --check-generated` → **[17/17] FAILED (exit=1)**，原因为本批未提交，生成态快照与工作区不一致；这是提交前门禁的预期结果，不是失败信号。提交后须重跑至通过。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动。
- `apply-plan.jsonl` 22/22 哈希在闭包后复核仍与磁盘一致。

## 九、未决事项与下一跳

- 未决：成分命名冲突不可裁；玻璃起源与最早制造无年代、成分与制作地点；琉璃璧只有 16 厘米上限；战国琉璃窑址未发现；两汉 6500 余件无构成与分布；玻璃衣片无墓葬与件数；本土与输入无成分依据；琉璃／玻璃在法门寺同批并用；料器铅含量与套烧温度全无；博山原料、炉窑、工匠与产量全无；宫廷玻璃厂隶属未定；近代工厂只有城市名单；玻璃与瓷器、漆器、铜器的替代关系无量化。
- 下一跳候选：玉石线 Theme（玉璧、玉具剑、玉印、玉衣等玉器本体）；青铜器形序列 Topic（鼎、壶、豆、簋、斝、甗、鬲）；制陶生产组织 Topic（商代王室作坊、周代职官、秦汉官营陶窑、郑韩故城）；重复候选 reconcile 4 组；图注单条待核 12 条；存量债务（未挂载 2089、单源 1919、tentative 2570、低置信 496、隔离 1280）。
- 本批不 commit、不 push；commit 与 push 须用户当次明确授权。
