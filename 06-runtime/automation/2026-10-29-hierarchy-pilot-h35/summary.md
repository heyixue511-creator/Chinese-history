# h35 批次摘要：B.8 玉石与治玉（礼制、工艺与巨型玉器）

## 一、目标与范围

本批新建 B 维度第四条前近代 Theme：B.8「玉石与治玉：礼制、工艺与巨型玉器」，下建 3 个 Topic，主挂载 12 个 KU。

基线为 v1.25：22 Theme、66 Topic、487 membership、481 complete assignments、2089 个 KU 未挂载、relation index 6966、隔离单元 1280。本批不动 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`，不改写任何既有 KU 的正文证据，只更新其层级字段与「在层级体系中的位置」段。

## 二、结构物化

### 新建 B.8「玉石与治玉：礼制、工艺与巨型玉器」

- `theme_code: B.8`、`primary_dimension: B`、`secondary_dimensions: [D, C]`，`source_basis` 六册，`date: 2026-10-29`。
- 核心问题四层：
  - 材料定义：赵农称「玉石也称美石」，分硬玉（翡翠）与软玉（透闪石、阳起石），原始制玉以软玉为主；玉石被视为原始先民在石器制作中发现的「不同于普通砾石的美石」。定义把玉放回石器传统，但无矿物学判据。
  - 礼制化：田自秉记周代玉器与伦理道德直接联系，成为修身标准与等级名分标志；《周礼·大宗伯》六器配五色四方；璧、琮、圭形制；命圭四等与玉石配比；陪葬位置圭左、璋首、琥右、璜足、璧背、琮腹。全部出自《周礼》《考工记》，无成套实物与年代序列。
  - 治玉：赵农记商周选料、切割、磨制、钻孔、雕刻五工序与铊子／砣机；李立新记《考工记》「刮摩」、雕琢六步、良渚与三代砣具、解玉砂；田自秉记套裁与巧色。工序名齐全而参数全无；砣具驱动方式两册不同。
  - 巨型玉器：渎山大玉海高 70 厘米、口径 182 厘米、重 3500 公斤（现存状态，经多次修磨）；大禹治水图玉山高 2.24 米、宽 0.96 米、重约 7 吨、历 13 年，青玉采自和田密勒塔山，造办处出坯、扬州雕琢；白玉嵌金红宝石碗嵌 180 颗红宝石，据诗注判断为御殿赐奶茶之器。三件记录密度不同。
- 边界 8 条，明确排除史前玉器（B.8 后续 Topic）、纹样母题（C）、玉料贸易与玉石之路（E.2）、服饰佩戴（B.2／E.5）、造办处机构（D.6.6）、玉器市场（D.1），并声明 B.7 只取玻璃仿玉的代用关系、B.8 只取玉器本体，两线不合并。
- 三个 Topic 按「制度—工艺—器物」分工，三者不是三个阶段：礼制文本、工序记载与单件器物各自独立。
- 支撑结构 12 个 KU（B.8.1 五、B.8.2 四、B.8.3 三），`term_anchor` 6、`procedure` 2、`key_person` 1、`representative_work` 3；未解决问题 13 条。

### 新建三个 Topic

- **B.8.1「礼制与器形：瑞玉六器、璧琮圭与周代等级」**（`research_question` 178 字）：支撑瑞玉六器、璧、琮、圭、周代玉礼器，全部 `term_anchor`。三层「文本规范—形制描述—等级刻度」，三条判断：六器的「成套」只在文本内成立；形制定义是比例与轮廓，等级定义是尺寸与玉石配比，两者无对应实物；赵农书内六器数目不一致（L1684 五器缺琥、L1692 六器含琥），两存不裁。
- **B.8.2「治玉工艺与玉工：选料、琢玉、套裁巧色与陆子冈」**（184 字）：支撑玉石（`term_anchor`）、琢玉（`procedure`）、玉雕套裁与巧色（`procedure`）、陆子冈（`key_person`）。三层「材料判断—工序链—设计判断」，三条判断：工序名可排顺序而每一步无参数；砣具驱动方式两册不同，不裁；套裁与巧色把选料与设计压在一起，但唯一可指认实例只有陆子冈茶晶花插。
- **B.8.3「巨型玉器与宫廷用玉：渎山大玉海、大禹治水图玉山与乾隆玉碗」**（180 字）：支撑渎山大玉海、大禹治水图玉山、白玉嵌金红宝石碗，全部 `representative_work`。三层「单器记录—生产链—组织方式」，三条判断：数字不等于原状（玉海经修磨）；一条生产链不等于一套制度（只有玉山留下分工）；用途判断不等于使用记录（玉碗赐奶茶出自诗注）。

### 既有结构更新

- `hierarchy/index.md` v1.25→v1.26；`archive/v1.25.md` 为改动前原样副本（48,383 字节，逐字节一致，`sha256:6999cc66…`）。
- `themes/README.md`（22→23 Theme，新增 B.8 段）、`topics/README.md`（66→69，新增 B.8 下 3 个与分工段）、`dimension-candidates.md`（三十四批 481→三十五批 493，新增 B.8 bullet，B 维度未挂载约 1149→1137，全库 2089→2077）同步。
- `themes/b7-…md` 与 `topics/b7-fangyu-yu-daiyong-zhanguo-lianghan-boliqi.md` 中「玉器本体归玉石线（尚未建 Theme）」改为「归 B.8（玉石与治玉）」；`themes/README.md` 与 `topics/README.md` 的 B.7 段同步。

## 三、12 个 KU 的挂载

| KU | 类型 | role | Topic | version |
|---|---|---|---|---|
| `terms/rui-yu-liuqi.md` | term | `term_anchor` | B.8.1 | 1→2 |
| `terms/bi.md` | term | `term_anchor` | B.8.1 | 1→2 |
| `terms/cong.md` | term | `term_anchor` | B.8.1 | 1→2 |
| `terms/gui.md` | term | `term_anchor` | B.8.1 | 1→2 |
| `terms/zhou-yu-liqi.md` | term | `term_anchor` | B.8.1 | 1→2 |
| `terms/yushi.md` | term | `term_anchor` | B.8.2 | 1→2 |
| `procedures/zhuo-yu.md` | procedure | `procedure` | B.8.2 | 2→3 |
| `procedures/yudiao-taocai-qiaose.md` | procedure | `procedure` | B.8.2 | 2→3 |
| `persons/lu-zigang.md` | person | `key_person` | B.8.2 | 1→2 |
| `works/dushan-dayuhai.md` | work | `representative_work` | B.8.3 | 1→2 |
| `works/dayu-zhishui-yushan.md` | work | `representative_work` | B.8.3 | 1→2 |
| `works/baiyu-qianjin-hongbaoshi-wan.md` | work | `representative_work` | B.8.3 | 1→2 |

- 12 个 KU 全部为主挂载，均写入 `primary_theme: B.8`、`secondary_themes: []`、`role_in_theme`、一条带 `primary: true` 与 `scope_note` 的 `topic_memberships`；`hierarchy_scope_note` 与 `scope_note` 逐字相同并保持为 frontmatter 末字段；正文「在层级体系中的位置」为六行段。
- 10 个 KU 原已有 `secondary_dimensions`，插入位置为 `primary_dimension` 之后、`secondary_dimensions` 之前；`procedures/zhuo-yu.md` 与 `procedures/yudiao-taocai-qiaose.md` 原无 `secondary_dimensions`，插入块后直接接 `hierarchy_scope_note`。
- 所有 KU 的正文证据、`sources`、`confidence`、`consensus` 未改动；只更新 `version`、`updated` 与层级字段。

scope 摘要：瑞玉六器只取《周礼·大宗伯》六器成套规范与五色四方对应；璧只取形制与四类等级用途；琮只取祭地之义与形制；圭只取命圭四等与四类圭；周代玉礼器只取伦理地位、礼器用途与陪葬位置；玉石只取「美石」定义与硬玉／软玉二分；琢玉只取商周五工序与铊子／砣机两册记载；套裁巧色只取定义与商代、宋代、新中国三段用例；陆子冈只取明代苏州琢玉身份与三件代表作；渎山大玉海只取元代酒器定位、现存尺寸与修磨状态；大禹治水图玉山只取尺寸、工期、玉料、运输与三地分工；白玉嵌金红宝石碗只取材料、形制与装饰组合。

## 四、边界处置

| 对象 | 处置 | 理由 |
|---|---|---|
| 史前玉器（良渚、红山、妇好墓玉器群） | 留 B.8 后续 Topic | 本批只取周代礼制、商周治玉与元清巨型玉器，不把史前玉器与周礼六器连成演化线 |
| 玉器纹样母题（神人兽面、龙凤、穀纹、蒲纹） | 归 C | B.8 只取器形、工序与制度 |
| 玉料贸易、玉石之路与和田玉运输路线 | 归 E.2 | B.8 只取来源所记「和田玉」「南阳玉」的材料判断 |
| 玉器在服饰中的佩戴方式（组玉佩、玉步摇、佩璜） | 归 B.2／E.5 | B.8 只取佩玉作为器类 |
| 造办处机构沿革、编制与匠役 | 归 D.6.6 | B.8.3 只取其在巨型玉器制作中的角色 |
| 玉器鉴定、拍卖与当代市场 | 归 D.1 | B.8 只取来源所记工艺与器物 |
| 玻璃仿玉的代用关系 | 归 B.7 | B.8 只取玉器本体，两线不合并 |
| 渎山大玉海的元明清宫廷流转 | 归 D | B.8.3 只记流转事实，不解释制度 |
| 玉山画面、题诗与错金花草纹的视觉分析 | 归 C | B.8.3 只记装饰构成，不解释风格 |

## 五、执行与验证

- `scripts/hierarchy_stress_test.py` → `hierarchy_version: v1.26`、themes 23、topics 69、topic_memberships 499、complete_assignments 493、incomplete_assignments 2077、themes_without_topics 0、cross_dimension_topics []、apply_permitted false。
- `scripts/build_relation_index.py` → 6990 条（explicit 5998、inferred_by_rule 992、migrated_from_related 0）。较基线 +24：12 条新 membership 各生成 1 条 topic `member_of`（+12），12 个主挂载另各生成 1 条 theme `member_of`（+12）；本批无次挂载，不产生「只加 topic 边」的情形。
- `scripts/write_current_health.py` → v1.26、complete 493、missing 2077、relation 6990、isolated 1275、structural_health 130、knowledge_structure_quality 56/65、rule_drift 0、system_p0 0。
- `apply-plan.jsonl` 23 行（4 `structure_node_create`、12 `hierarchy_mount`、7 `structure_index_update`），闭包后复核 23/23 哈希与磁盘一致。
- 隔离单元由 1280 减至 1275：12 个新挂载中 5 个原无显式关系，其余 7 个已因既有术语互引而进入关系图。

## 六、指标变化

| 指标 | v1.25 基线 | v1.26 结果 |
|---|---|---|
| Theme | 22 | 23 |
| Topic | 66 | 69 |
| Topic membership | 487 | 499 |
| 完成五级挂载 KU | 481 | 493 |
| 未挂载 KU | 2089 | 2077 |
| relation index | 6966 | 6990 |
| member_of | 968 | 992 |
| 隔离单元 | 1280 | 1275 |
| structural_health | 130 | 130 |
| knowledge_structure_quality | 56/65 | 56/65 |
| 库存 KU | 2570 | 2570 |

## 七、语义边界

1. B.8 不写「中国玉器发展史」，只写四层各自能证到什么程度：材料层缺矿物学判据，制度层缺成套实物，工艺层缺工序参数，器物层只有三件元清玉器且记录密度不同。
2. 玉、石、玉髓、玻璃的边界不由六册判定；「玉石也称美石」是赵农的定义，不是矿物学判据。
3. 六器的「六」在赵农书内不一致：L1684 列举只有璧、琮、圭、璋、璜五器，L1692 六器含琥；来源未说明差异，本库两存。
4. 命圭四等与玉石配比是文献等级，不是实测器物等级；本库不据以判定任何出土玉器的年代、等级或用途。
5. 砣具驱动方式两册不同：赵农记铊子装在车床上用脚踏，李立新记三代玉人席地跪坐拨动青铜砣具、良渚砣具由弓弦或绳筋拉动；本库并列，不裁为时代、地域或描述差异。
6. 「整个制作过程也就是设计过程」是田自秉的判断，不是工序记录；唯一可指认的巧色实例是陆子冈茶晶花插，本库不据此为其他玉器推定设计过程。
7. 渎山大玉海的尺寸重量是现存状态，来源明说经多次修磨、已非元代旧貌；本库不用这组数字讨论元代玉雕的体量上限。
8. 大禹治水图玉山的造办处出坯、扬州雕琢是单件器物的分工记录，不是乾隆朝巨型玉器的普遍制度；同类三件大型玉雕只有名称，不构成「乾隆巨型玉器群」的实证。
9. 白玉嵌金红宝石碗的「御殿赐奶茶」出自乾隆诗与《高宗御制诗集》注，是帝王自述与后人判断，本库不把它升级为宫廷筵宴制度的结论。

## 八、生成态与门禁

- `hierarchy/index.md` 升版并归档 `archive/v1.25.md`（48,383 字节，与改动前逐字节一致，`sha256:6999cc66bc32ede9e7b15b6f92bd5f97d556ac7925dadb3645975cfd0c89e0c9`）。
- `relation-index.yml`、`current-health.json`、`governance-backlog.md`、`generated-projections-manifest.json`、`06-runtime/automation/index.md` 由刷新步骤重建，不在 apply-plan 内。
- `run_sync_closure.py --refresh-generated --full` 实测 `sync closure passed`：18/18 步通过，pytest 250 passed、16 subtests passed。首次闭包后 `rule_drift` 记 1 条 `output_navigation_snapshot_stale`（`05-outputs/index/index.md` 仍写 relation 6966），系第 8 步写 health 早于第 9 步重建导航的固定顺序所致；重跑 `write_current_health.py` 清零后再次全量闭包，`rule_drift` 稳定为 0，`structural_health` 130、`knowledge_structure_quality` 56/65。
- `run_sync_closure.py --refresh-generated --check-generated` 实测 `[17/17] FAILED: check generated snapshots (exit=1)`，符合未提交工作树下的预期：生成态文件与 `HEAD` 不一致即被阻断，须在授权提交后复查。
- `relation-index.yml` 复核 6990 条：`member_of` 992、`supports_claim` 2999、`supported_by` 2999；含 `b8-` 的边 24 条，与预期一致。按关系索引统计隔离单元 1275。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动。
- `apply-plan.jsonl` 闭包后逐行复核：23 行，23/23 `after_sha256` 与磁盘字节一致，0 缺失、0 失配。
- 本批未 `git add`、未 commit、未 push；`git log` 仍停在 `c249c6fe`。

## 九、未决事项与下一跳

- 未决：玉石无矿物学判据；玉器起源无遗址与年代；六器无成套实物；璧琮圭无实测；命圭无实物；陪葬位置无墓例；商周五工序无参数；砣具驱动两说不可裁；玉料产地单源；套裁巧色无工艺细节；陆子冈无生平与作品系年；渎山大玉海无制作信息且现存状态非原状；大禹治水图玉山无工匠名录与分段工期；白玉碗无尺寸、年份与镶嵌工艺。
- 下一跳候选：B.8 续批史前玉器 Topic（玉钺、玉琮、玉璧、神人兽面纹玉琮、大玉龙、玉雕龙、两城镇、北阴阳营、花厅墓地、妇好墓 426 件玉器、汉八刀、佩璜、璇玑、天圆地方）；青铜器形序列 Topic（鼎、壶、豆、簋、斝、甗、鬲）；制陶生产组织 Topic（商代王室作坊、周代职官、秦汉官营陶窑、郑韩故城）；重复候选 reconcile 4 组；图注单条待核 12 条；存量债务（未挂载 2077、单源 1919、tentative 2570、低置信 496、隔离 1275）。
- 本批不 commit、不 push；commit 与 push 须用户当次明确授权。
