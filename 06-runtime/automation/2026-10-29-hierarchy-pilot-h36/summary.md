# h36 批次摘要：B.8 续批（B.8.4 史前玉器、B.8.5 商代玉器）

## 一、目标与范围

本批在既有 Theme B.8「玉石与治玉：礼制、工艺与巨型玉器」下续建 B.8.4「史前玉器与玉礼器的起源：良渚、红山与龙山」与 B.8.5「商代玉器与妇好墓：用途三分、佩玉与玉人」两个 Topic，并挂载 15 个 KU（14 主挂载 + 1 次挂载）。

基线为 v1.26：23 Theme、69 Topic、499 membership、493 complete assignments、2077 个 KU 未挂载、relation index 6990、隔离单元 1275。本批不动 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`，不改写任何既有 KU 的正文证据，只更新其层级字段与「在层级体系中的位置」段。

## 二、结构物化

### 新建 B.8.4「史前玉器与玉礼器的起源：良渚、红山与龙山」

- `parent_theme: B.8`、`primary_dimension: B`、`secondary_themes: [D, C]`，`research_question` 177 字，`date: 2026-10-29`。
- 理论三层「器物记录—象征解释—礼制追溯」：器物记录层有数量与尺寸（反山 1100 余件组／按单件 3200 余件、大玉龙 42.2 厘米、玉锛厚 0.2～0.5 厘米、花厅 500 余件），象征解释层是来源判断（玉钺兵权、玉琮神器、玉璧财富，琮的内圆外方象征天地），礼制追溯层把晚出文献投射到史前器物（《周礼》苍璧礼天、黄琮礼地）。
- 三条限度：数量不等于组合（反山总数无逐墓分项）、象征不等于用途（兵权／神器／财富无装柄、祭祀与财富使用记录）、追溯不等于同时（《周礼》晚于良渚两千余年，来源自称「西周以下的礼仪」）。
- 边界 9 条：周代六器归 B.8.1、治玉工序归 B.8.2、商代玉器归 B.8.5、巨型玉器归 B.8.3、纹样母题归 C、玉料贸易归 E.2、服饰佩戴归 B.2／E.5、三文化分区与陶器归 B.5.2；并声明良渚、红山、龙山不是一条连续发展线。
- 支撑结构 10 个 KU（term 4、work 3、place 3），role 为 `term_anchor` 2、`representative_work` 3、`historical_context` 2、`geographical_context` 2、`boundary_case` 1；未解决问题 12 条。

### 新建 B.8.5「商代玉器与妇好墓：用途三分、佩玉与玉人」

- `parent_theme: B.8`、`primary_dimension: B`、`secondary_themes: [D, C]`，`research_question` 172 字，`date: 2026-10-29`。
- 理论三层「库存—分类—单件」：库存层有 426／755／近 600 三种数字而口径不明；分类层有礼仪用品／生活用品／装饰物品三分而无人分项数量；单件层有高 7 厘米跪坐玉人的发式、服饰与云纹回纹而无玉料检测与出土编号。
- 三条限度：库存不等于分类（三种数字均无分项）、一座墓葬不等于一个时代（妇好墓是殷墟晚期王室墓，二里头无同类库存）、判断不等于工序（李立新以 755 件成品判定刮摩技术「已经成熟」，无工具、工序与工艺痕迹）。
- 边界 10 条：周代六器归 B.8.1、治玉工序归 B.8.2、史前玉器归 B.8.4、巨型玉器归 B.8.3、妇好墓青铜器与墓葬形制归 D.6 与青铜器 Topic、妇好身份考证归 A／D、纹样母题归 C、玉料贸易归 E.2、商代服饰制度归 B.2；并声明三种玉器数目并列不改。
- 支撑结构 5 个 KU（term 2、person 1、place 1、work 1），role 为 `term_anchor` 2、`key_person` 1、`geographical_context` 1、`representative_work` 1；未解决问题 11 条。

### 既有结构更新

- `hierarchy/index.md` v1.26→v1.27；`archive/v1.26.md` 为改动前原样副本（50,554 字节，逐字节一致，`sha256:a86241382148b76a94235c908c3d089760a149339ed239e3a1d9e9e5d3f9ddeb`）。
- `themes/README.md`（B.8 段四层→五层：5 Topic、主挂载 26、次挂载 1）、`topics/README.md`（69→71，B.8 下 5 个，B.8 五 Topic 分工段重写）、`dimension-candidates.md`（第三十六批 493→507，B.8 bullet 扩写 v1.27，B 维度未挂载旧估值 1123 更正为实测 1347，全库 2077→2063）同步。
- 根 `README.md` 首段「知识库为空（0 KU / 0 Theme / 0 Topic）」是过期状态说明，改为指向 `06-runtime/state/current-health.json` 的实时计数；该文件属治理文档，不在 apply-plan 内。

## 三、15 个 KU 的挂载

| KU | 类型 | role | Topic | version |
|---|---|---|---|---|
| `terms/yu-yue-cong-bi.md` | term | `term_anchor` | B.8.4 | 3→4 |
| `works/shenren-shoumianwen-yucong.md` | work | `representative_work` | B.8.4 | 1→2 |
| `works/da-yulong.md` | work | `representative_work` | B.8.4 | 1→2 |
| `works/yu-ben.md` | work | `representative_work` | B.8.4 | 1→2 |
| `terms/tianyuan-difang.md` | term | `term_anchor` | B.8.4 | 1→2 |
| `terms/hongshan-culture.md` | term | `historical_context` | B.8.4 | 1→2 |
| `places/liangchengzhen-site.md` | place | `geographical_context` | B.8.4 | 1→2 |
| `places/beiyinyangying-site.md` | place | `geographical_context` | B.8.4 | 1→2 |
| `places/huating-mudi.md` | place | `boundary_case` | B.8.4 | 1→2 |
| `terms/shangdai-yuqi-fenlei.md` | term | `term_anchor` | B.8.5 | 1→2 |
| `terms/pei-huang.md` | term | `term_anchor` | B.8.5 | 1→2 |
| `persons/fu-hao.md` | person | `key_person` | B.8.5 | 1→2 |
| `places/fuhao-tomb.md` | place | `geographical_context` | B.8.5 | 4→5 |
| `works/fuhao-mu-yuren.md` | work | `representative_work` | B.8.5 | 1→2 |
| `terms/liangzhu-culture.md` | term | `historical_context` | B.8.4（次挂载） | 2→3 |

- 14 个主挂载写入 `primary_theme: B.8`、`secondary_themes: []`、`role_in_theme`、一条带 `primary: true` 与 `scope_note` 的 `topic_memberships`；`hierarchy_scope_note` 与 `scope_note` 逐字相同并保持为 frontmatter 末字段；正文「在层级体系中的位置」为六行段。
- 良渚文化保留 `primary_theme: B.5`，`topic_memberships` 追加一条 `primary: false` 的 B.8.4 条目；`secondary_themes` 仍为 `[]`；`hierarchy_scope_note` 写明「B.5.2 主挂载分区框架与黑陶三说、B.8.4 次挂载玉器门类、反山数量与砣具判断，两处不合并」，正文成员行以 `；` 分隔并标注 `primary` / `secondary`。
- 所有 KU 的正文证据、`sources`、`confidence`、`consensus` 未改动；只更新 `version`、`updated` 与层级字段。

scope 摘要：玉钺玉琮玉璧只取三器的兵权／神器／财富分工与玉琮形制两说；神人兽面纹玉琮只取图版器名与反山数量、三类用途、线割锯切管钻抛光；大玉龙只取 C 型 42.2 厘米与绿玉佩饰；玉锛只取两城镇半成品玉材与厚度；天圆地方只取玉琮方圆象征与「始于原始设计时期」；良渚文化只取玉器门类、反山数量与砣具判断；红山文化只取动物纹群、大玉龙与图版名称差异；两城镇只取玉材坑与玉锛；北阴阳营只取 280 多件玉玛瑙制品与璜玦位置；花厅只取 500 余件良渚风格玉器与交换判断；商代玉器分类只取三分框架与佩玉辟邪；佩璜只取玩赏性质与四类纹饰演变；妇好只取王妃身份与 426 件玉器分类；妇好墓只取三种数目、1976 年发掘与治玉成熟判断；妇好墓玉人只取 7 厘米跪坐像的发式、服饰与云纹回纹。

## 四、边界处置

| 对象 | 处置 | 理由 |
|---|---|---|
| 妇好墓玉雕人俑（夏燕靖 2016） | 不挂载，留待 reconcile | 与田自秉的妇好墓玉人疑为同一器物，图题与描述不足以判定，`knowledge_match` 为 undetermined 时不得写回 |
| 玉雕龙（李立新图题） | 不挂载，留待 reconcile | 与田自秉 C 型大玉龙疑为同一器物，来源未给对应关系 |
| 玉器纹样母题（神人兽面、龙纹、云纹、回纹） | 归 C | B.8.4／B.8.5 只取器名、形制与工序记录 |
| 玉料贸易、玉石之路与和田玉运输 | 归 E.2 | 只取来源所记玉材判断 |
| 玉器在服饰中的佩戴方式 | 归 B.2／E.5 | 只取佩玉、佩璜作为器类 |
| 良渚、红山、龙山的陶器、黑陶与考古学文化分区 | 归 B.5.2 | B.8.4 只取玉器门类与玉礼器问题 |
| 石器石材选择与七孔石刀 | 归石器线 | B.8.4 只取玉锛与半成品玉材 |
| 妇好墓青铜器、铜镜、纺织与墓葬形制 | 归 D.6 与青铜器 Topic | B.8.5 只取玉器库存与玉人 |
| 汉代及以后玉器（汉八刀、璇玑、佩玉） | 待评估 | 本批不建立史前—商代—汉代的玉器演化线 |

## 五、执行与验证

- `scripts/hierarchy_stress_test.py` 在升版前实测：themes 23、topics 71、topic_memberships 514、complete_assignments 507、incomplete_assignments 2063、themes_without_topics 0、cross_dimension_topics []、apply_permitted false。
- `scripts/build_relation_index.py` → 7019 条（explicit 5998、inferred_by_rule 1021、migrated_from_related 0）。较基线 +29：15 条新 membership 各生成 1 条 topic `member_of`（+15），14 个主挂载另各生成 1 条 theme `member_of`（+14）；良渚文化为次挂载，只加 topic 边。`b8-` 相关边由 24 增至 53。
- `scripts/write_current_health.py` → v1.27、complete 507、missing 2063、relation 7019、isolated 1268、structural_health 130、knowledge_structure_quality 56/65、rule_drift 0、system_p0 0。
- `apply-plan.jsonl` 22 行（2 `structure_node_create`、15 `hierarchy_mount`、5 `structure_index_update`），闭包后复核 22/22 哈希与磁盘一致。
- 隔离单元由 1275 减至 1268：15 个新挂载中 7 个原无显式关系，其余 8 个已因既有术语互引而进入关系图。

## 六、指标变化

| 指标 | v1.26 基线 | v1.27 结果 |
|---|---|---|
| Theme | 23 | 23 |
| Topic | 69 | 71 |
| Topic membership | 499 | 514 |
| 完成五级挂载 KU | 493 | 507 |
| 未挂载 KU | 2077 | 2063 |
| relation index | 6990 | 7019 |
| member_of | 992 | 1021 |
| 隔离单元 | 1275 | 1268 |
| structural_health | 130 | 130 |
| knowledge_structure_quality | 56/65 | 56/65 |
| 库存 KU | 2570 | 2570 |

## 七、语义边界

1. 史前与商代两段只到「器物记录—分类框架—单件著录」三层，不能为《周礼》六器的礼制起源提供闭环证据；苍璧黄琮的文本追溯晚于良渚两千余年。
2. 良渚、红山、龙山不是一条连续发展线；三者各有年代与地域，六册未给工艺传承记录，本库不建立「中国史前玉器谱系」。
3. 玉钺兵权、玉琮神器、玉璧财富是赵农的三项概括，不是出土情境的复原；三器是否成套、同出一墓、分属等级，六册未载。
4. 反山 1100 余件组与按单件 3200 余件是墓地群总数，不是单墓组合；本库不用总数讨论良渚社会的玉器分配。
5. 「天圆地方」是李立新的解释框架，不是良渚人的自述；观念的最早出处与从玉琮到青铜器的传承环节均未给。
6. 妇好墓玉器的 426／755／近 600 三种数目并列不改：来源未说明是否含残件、工具、礼器、串饰与兵器，三种数字不能互相换算。
7. 商代玉器三分是「大约」的概括，无常量比例与分项数量；礼仪用品与礼器在三分中是两层，礼器只列五器、缺玉琥。
8. 李立新以 755 件成品判定殷商刮摩治玉技术「已经成熟」，是以数量反推技术的史学判断，不是工序复原。
9. 妇好墓是殷墟晚期王室墓，不能代表商代早期二里头玉器，也不能代表商代全部墓葬；本库不据玉器数字推断墓葬等级。
10. 妇好墓跪坐玉人的发式与服饰只有文字描述，无玉料鉴定、出土编号与图版核验；本库不据此裁定深衣成立年代。

## 八、生成态与门禁

- `hierarchy/index.md` 升版并归档 `archive/v1.26.md`（50,554 字节，与改动前逐字节一致，`sha256:a86241382148b76a94235c908c3d089760a149339ed239e3a1d9e9e5d3f9ddeb`）。
- `relation-index.yml`、`current-health.json`、`governance-backlog.md`、`generated-projections-manifest.json`、`06-runtime/automation/index.md` 等生成态文件由刷新步骤重建，不在 apply-plan 内。
- `run_sync_closure.py --refresh-generated --full` 实测 `sync closure passed`：18/18 步通过，pytest 250 passed、16 subtests passed。首次闭包后 `rule_drift` 记 1 条 `output_navigation_snapshot_stale`（`05-outputs/index/index.md` 仍写 relation 6990），系第 8 步写 health 早于第 9 步重建导航的固定顺序所致；重跑 `write_current_health.py` 清零后再次全量闭包，`rule_drift` 稳定为 0，`structural_health` 130、`knowledge_structure_quality` 56/65。
- `run_sync_closure.py --refresh-generated --check-generated` 实测 `[17/17] FAILED: check generated snapshots (exit=1)`，符合未提交工作树下的预期：生成态文件与 `HEAD` 不一致即被阻断，须在授权提交后复查。
- `relation-index.yml` 复核 7019 条：`member_of` 1021、`supports_claim` 2999、`supported_by` 2999；含 `b8-` 的边 53 条。按关系索引统计隔离单元 1268。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动。
- `apply-plan.jsonl` 闭包后逐行复核：22 行，22/22 `after_sha256` 与磁盘字节一致，0 缺失、0 失配。
- 本批未 `git add`、未 commit、未 push；`git log` 仍停在 `c249c6fe`。

## 九、未决事项与下一跳

- 未决：良渚、红山、龙山无年代序列与玉料检测；玉器由工具转礼器无过渡器物；玉钺玉琮玉璧无尺寸与出土单位；反山总数无逐墓分项；神人兽面纹两说并存；红山玉器无墓葬与工艺；大玉龙无出土与藏地；两城镇玉材坑无坑口信息；北阴阳营无器类数量；花厅无逐件比对；天圆地方无文献出处序列；商代三分无分项数量；二里头与殷墟无分期序列；佩璜无实物与年代；妇好墓三种数目口径不明；跪坐玉人无玉料与出土信息；两组重复候选（妇好墓玉雕人俑 vs 玉人、玉雕龙 vs 大玉龙）未裁。
- 下一跳候选：重复候选 reconcile 6 组（本批新增 2 组，另有 youlihong 釉里红 2 条、白陶 2 条、鲁山窑瓷拍鼓 vs 花釉腰鼓、竹林七贤砖 2 条）；青铜器形序列 Topic（鼎、壶、豆、簋、斝、甗、鬲）；制陶生产组织 Topic（商代王室作坊、周代职官、秦汉官营陶窑、郑韩故城）；汉代及以后玉器线（汉八刀、璇玑、佩玉）评估；图注单条待核 12 条；存量债务（未挂载 2063、单源 1919、tentative 2570、低置信 496、隔离 1268）。
- 本批不 commit、不 push；commit 与 push 须用户当次明确授权。
