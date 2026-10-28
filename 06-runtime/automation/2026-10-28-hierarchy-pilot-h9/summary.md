# h9 批次摘要：T7 D 维度「传统工艺的近代组织、展赛与政策」的 D.5 物化

- 批次：`2026-10-28-hierarchy-pilot-h9`
- 日期：2026-10-28
- 层级版本：v0.9 → v1.0
- 结论：新增 1 个 Theme、3 个 Topic，主挂载 6 个 KU；15 个 authored 文件加 3 个 runtime 文件，15/15 哈希匹配。未 commit、未 push。

## 一、目标与范围

h8 已把 T7「传统工艺的近代命运」的 B 维度部分 materialize 为 B.4，并明确把太平天国、诸匠营、百工衙、南洋劝业会、广东工艺局与磁州陶瓷研究所留待 D 维度 Theme。本批完成这部分：

- D.5.1 太平天国工艺组织与工艺政策；
- D.5.2 清末民初工艺局、劝业会与工艺评价；
- D.5.3 解放区工艺研究机构。

新建 Theme `D.5`「传统工艺的近代组织、展赛与政策」，`primary_dimension: D`，`secondary_dimensions: [B, E]`。这样 T7 按 B（B.4）／D（D.5）两个主维度完成试点拆分，沿用 T2 的 B.2/D.2、T5 的 B.3/D.3 先例，不表示 T7 整体闭合。

E 维度仍不单列 Theme：巴拿马赛会主维度为 E，1851 年万国博览会不是中国设计对象；两者均不挂载，避免为凑齐维度制造部分挂载。

## 二、结构物化

新增 Theme `04-knowledge/structure/themes/d5-chuantong-gongyi-zuzhi-zhansai-zhengce.md`：

- `node_type: theme`
- `theme_code: D.5`
- `primary_domain: chinese-design-history`
- `primary_dimension: D`
- `secondary_dimensions: [B, E]`
- `status: pilot`

新增 Topic：

| Topic | 研究问题 | 支撑 KU |
|---|---|---|
| D.5.1 太平天国工艺组织与工艺政策 | 太平天国如何以诸匠营的军制编组与百工衙的门类分工，把工艺工人组织为政权生产体系，并以“益民”工艺观与奖励发明政策规范工艺？ | 太平天国、诸匠营、百工衙 |
| D.5.2 清末民初工艺局、劝业会与工艺评价 | 广东工艺局如何以地方工艺行政与洋庄外销组织工艺品生产？南洋劝业会如何以 24 部 420 类、5269 件获奖的展评制度把全国工艺品纳入市场评价？ | 广东工艺局、南洋劝业会 |
| D.5.3 解放区工艺研究机构 | 磁州解放后设立的“解放区第一个陶瓷研究所”如何在恢复陶瓷生产与支持解放区工艺生产中发挥作用？为何只有一句来源，仍值得作为机构样本？ | 磁州解放区陶瓷研究所 |

三个 Topic 按“政权组织—地方工艺行政与展赛—解放区研究机构”分工，不重复计入同一 KU；B.4 已承接的瓷业公司与解放区日用工艺生产不在 D.5 重挂。

## 三、6 个 KU 的挂载与语义决定

6 个 KU 全部为单主挂载、`secondary_themes: []`、`primary: true`，写入 `updated: 2026-10-28`、`version: 2`；`last_verified` 不改。

### D.5.1（3 个）

- **太平天国**（event，`historical_context`）：以太平天国政权、恢复工艺生产、《招贤榜》、“益民”工艺观与奖励发明政策为锚点；事件条只作政权与政策背景，诸匠营与百工衙另由机构条目承担，避免同一材料在事件条重复展开。保留原 `secondary_dimensions: [B]`。
- **诸匠营**（institution，`key_institution`）：以军制编组、土营／木营／金匠营／织营／绣锦营／镌刻营、招贤榜与杭州招贤馆为锚点。
- **百工衙**（institution，`key_institution`）：以服用、建筑、日用品、印刷、美术五类门类及典织衙、缝衣衙、绣锦衙、结彩衙等分工为锚点。

### D.5.2（2 个）

- **南洋劝业会**（event，`evidence_event`）：以 1910 年南洋通商大臣倡办、南京丁家桥会场、24 部 420 类、100 多万件展品与 5269 件获奖为锚点。原 KU 未列次维度，本批不新增 `secondary_dimensions`，只记录 `primary_dimension: D`。
- **广东工艺局**（institution，`key_institution`）：以光绪年间设立、主管工艺品生产、洋庄外销、潮绣经汕头口岸出口与 1900 年广东海关绣品出口值为锚点；保留原 `secondary_dimensions: [E, B]`。

### D.5.3（1 个）

- **解放区第一个陶瓷研究所**（institution，`key_institution`）：以磁州解放后恢复陶瓷生产并成立“解放区第一个陶瓷研究所”一句为锚点；组织、人员、项目、成果与存续时间均缺，`confidence: low`、`consensus: tentative` 保持不变；保留原 `secondary_dimensions: [B]`。

字段处理：6 个 KU 均保留原有 `secondary_dimensions`，不因挂入 D.5 而改写主维度；`secondary_themes` 全部为空，D.5 的相邻 Theme（B.4）不写未审的 Theme 引用。

## 四、执行与验证

- `scripts/hierarchy_stress_test.py`：v1.0，11 Theme、26 Topic、127 membership、124 complete、2446 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`。
- `scripts/audit_content_quality.py`：总发现 0。
- `scripts/audit_repo.py`：EXIT=0，断链 0，Frontmatter 0，类型值不匹配 0，同名消歧 10/10。
- `scripts/build_relation_index.py`：relation 6249（explicit 5998、inferred 251），`member_of` 251。
- `scripts/run_sync_closure.py --refresh-generated --full`：18/18，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：15 行（4 个 structure_node_create、6 个 hierarchy_mount、5 个 structure_index_update），15/15 `after_sha256` 重新计算匹配。
- 结构健康 130/130；知识结构质量 55/65，`hierarchy_assignment` 仍为 0，这是 2446 个 KU 未挂载的覆盖度信号，不是本批新增结构错误。

## 五、指标变化

| 指标 | h8 后 v0.9 | h9 后 v1.0 | 变化 |
|---|---:|---:|---:|
| Theme | 10 | 11 | +1 |
| Topic | 23 | 26 | +3 |
| Topic membership | 121 | 127 | +6 |
| 完整挂载 KU | 118 | 124 | +6 |
| 未挂载 KU | 2452 | 2446 | −6 |
| Relation 总数 | 6237 | 6249 | +12 |
| `member_of` | 239 | 251 | +12 |
| 隔离单元 | 1464 | 1462 | −2 |
| 结构健康 | 130 | 130 | 0 |
| 知识结构质量 | 55/65 | 55/65 | 0 |
| 内容质量发现 | 0 | 0 | 0 |
| KU / claim / candidate / translation | 2570 / 1242 / 5339 / 2178 | 同左 | 0 |

`member_of` 增加 12：6 个新主挂载各生成 1 条 Theme 关系与 1 条 Topic 关系。隔离单元只减少 2，表示另外 4 个新挂载 KU 原本已有其他显式关系；不能据此推断它们已被充分研究。

## 六、语义边界

- 本批只证明 124 个 KU 完成五级字段挂载，不证明 2570 个 KU 全量挂载，也不证明 D.5 已是稳定分类。
- D.5 是 `pilot` Theme，不表示 T7 已验收或结构闭合；E 维度仍未 materialize。
- 2446 个未挂载 KU 仍是研究债务；`structure_node_coverage` 仍为 2/4，因为 Domain 与 Dimension 尚未 materialize。
- 巴拿马赛会主维度为 E，1851 年万国博览会不是中国设计对象；两者均不挂载，也不改写主维度。巴拿马赛会若后续建立 E Theme 或 D 维度展赛次挂载，需重新做语义裁决。
- 王大凡《富贵寿考瓷板》仍只有图注一行、confidence 为 low，本批继续不挂载。
- 太平天国条只作政权与政策背景，诸匠营与百工衙的组织细节分别由机构条承担，不把三者合成一篇工艺制度史。
- 南洋劝业会的 24 部 420 类、100 多万件展品与 5269 件获奖均出自同一段转述；评奖标准、评审过程与展品清单未详，不能据此写全国性展评制度史。
- 广东工艺局缺正式设立年份、组织结构、人员、资本与产量；1900 年海关绣品出口值是单一数值，无时间序列与计价口径，不能写成外销增长曲线。
- 磁州解放区陶瓷研究所只有一句来源，“第一个”无比较范围；本批只登记制度位置，不补造所名、年份与成果。
- D.5 与 B.4 的分工是“生产／技术”与“组织／展赛／政策”的解释性切分，不是来源自带的分类；后续若出现同时覆盖两侧的 KU，应逐对象裁决主维度，不得按文件名批量归并。

## 七、生成态与门禁

- `06-runtime/automation/index.md` 与 `06-runtime/state/generated-projections-manifest.json` 由完整闭包刷新；本批新增 1 个批次目录与 3 个 runtime 文件（`apply-plan.jsonl`、`manifest.json`、`summary.md`）。
- 生成态只作投影，不是知识裁决本体；automation 文件数由闭包索引确定，本摘要不把估算值写成事实。
- h9 尚未 commit，发布门禁 `--refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 以 `EXIT=1` 结束；该步等价于 `git diff --exit-code HEAD -- <GENERATED_PATHS>`，失败表示生成态快照与 HEAD 有差异，不是内容审计失败，也不是脚本给出的独立状态名。
- 本批未 commit、未 push；外部状态变更等待用户当次明确授权。

## 八、未决事项与下一跳

1. **E 维度**：巴拿马赛会、1851 年万国博览会、外来式建筑术语、旗袍等 E 主维度条目仍未 materialize；需评估是否建立 E Theme，或继续作为跨主题标签与 `secondary_dimensions` 使用。
2. **T7 收束**：B.4 与 D.5 已完成 T7 的 B／D 试点拆分；T7 是否可标记为“试点完成、非闭合”，需在 evolve-hierarchy 中显式裁决。
3. **太平天国材料**：诸匠营与百工衙的组织细节同出单源；需查《天朝田亩制度》相关史料与太平天国工艺政策原文，不能仅据一段转述写制度史。
4. **南洋劝业会**：24 部 420 类、5269 件获奖等数字需查《南洋劝业会纪事》或农商部档案；评奖标准与评审过程未详。
5. **广东工艺局**：设立年份、隶属、经费、产能与外销渠道缺；1900 年海关出口值需补时间序列与计价口径。
6. **磁州研究所**：只有一句来源；需查晋冀鲁豫边区工业史料、磁州地方志或陶瓷研究所档案。
7. **存量挂载**：2446 个 KU 仍缺五级字段；单源 1919、tentative 2570、低置信 496、隔离 1462 继续作为研究债。
8. **既有欠账**：qian-juntao 重复、shenghuo-weekly 的 C.1.2 回填、h4 排除项复审，均未在本批处理。
