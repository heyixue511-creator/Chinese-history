# h8 批次摘要：T7 B 维度「传统工艺的近代生产与转型」的 B.4 物化

- 批次：`2026-10-28-hierarchy-pilot-h8`
- 日期：2026-10-28
- 层级版本：v0.8 → v0.9
- 结论：新增 1 个 Theme、2 个 Topic，主挂载 4 个 KU；12 个 authored 文件加 3 个 runtime 文件，12/12 哈希匹配。未 commit、未 push。

## 一、目标与范围

T7「传统工艺的近代命运」在归并报告中同时覆盖 B 维度（瓷业与解放区日用工艺生产）、D 维度（太平天国工艺组织、南洋劝业会、广东工艺局、解放区陶瓷研究所）与 E 维度（巴拿马赛会、1851 年万国博览会）。现有 KUs 的 `primary_dimension` 与 `primary_theme` 前缀必须一致，`scripts/apply_topic_memberships.py` 也按 `primary_theme.split(".", 1)[0]` 推导维度；若用一个跨维度 Theme 直接挂 B/D/E 三类 KU，会产生维度前缀冲突。

因此本批只 materialize T7 的 B 维度部分，建立 B.4「传统工艺的近代生产与转型」：

- B.4.1 近代瓷业公司与瓷业改良；
- B.4.2 解放区日用工艺生产。

D 维度的太平天国、诸匠营、百工衙、南洋劝业会、广东工艺局与磁州陶瓷研究所留待后续 D 维度 Theme；E 维度的巴拿马赛会与 1851 年万国博览会仍不并入。此拆分沿用 T2 的 B.2/D.2、T5 的 B.3/D.3 先例，不表示 T7 已经整体闭合。

## 二、结构物化

新增 Theme `04-knowledge/structure/themes/b4-chuantong-gongyi-jindai-shengchan-zhuanxing.md`：

- `node_type: theme`
- `theme_code: B.4`
- `primary_domain: chinese-design-history`
- `primary_dimension: B`
- `secondary_dimensions: [D, E]`
- `status: pilot`

新增 Topic：

| Topic | 研究问题 | 支撑 KU |
|---|---|---|
| B.4.1 近代瓷业公司与瓷业改良 | 1910 年景德镇瓷业公司与清末民初湖南瓷业公司，如何以“本厂守旧、分厂试验”和“学校—公司—产品”两种路径，把机器制瓷、煤窑烧炼与釉下花瓷引入传统产瓷区？ | 景德镇瓷业公司、湖南瓷业公司 |
| B.4.2 解放区日用工艺生产 | 1941 年延安玻璃厂与 1944 年桥儿沟陶瓷厂，如何在原料本地化、坩埚制作、石膏模型与窑炉改造的条件下生产日用器，并把边区工艺纳入战时供给？ | 延安玻璃厂、桥儿沟陶瓷厂 |

两个 Topic 按“市场导向的瓷业改良—战时边区的日用器生产”分工，不重复计入同一 KU。

## 三、4 个 KU 的挂载与语义决定

4 个 KU 全部为单主挂载、`secondary_themes: []`、`primary: true`，写入 `updated: 2026-10-28`、`version: 2`；`last_verified` 不改。

### B.4.1（2 个）

- **景德镇瓷业公司**（institution，`key_institution`）：以 1910 年成立、景德镇本厂与鄱阳分厂、陶业学堂“拟用机器制瓷、试验煤窑烧炼”为锚点。公司制度与学堂归 D 次维度，机器与煤窑的跨文化技术来源归 E 次维度；本批不新增次维度。
- **湖南瓷业公司**（institution，`key_institution`）：以 1906 年湖南瓷业学校、官商合办、圆器厂／琢器厂／机械室／电灯室／化学室与釉下花瓷为锚点；南洋劝业会与巴拿马、意大利博览会获奖归 E 次维度，本 Topic 只把获奖当作产品旁证，不展开展赛史。

### B.4.2（2 个）

- **延安玻璃厂**（institution，`key_institution`）：以 1941 年延安建厂、石英／白土／石碱本地原料、坩埚制作与杯瓶灯罩等日用器为锚点；工厂组织与边区工业政策归 D 次维度，本批不另设 D 挂载。
- **桥儿沟陶瓷厂**（institution，`key_institution`）：以 1944 年《解放日报》报道的石膏模型、窑炉改造、近 200 种产品、白瓷杯碟与本地瓷土为锚点；工厂组织与边区工业政策归 D 次维度，本批不另设 D 挂载。

字段处理：4 个 KU 均保留原有 `secondary_dimensions`，不因挂入 B.4 而改写主维度；`secondary_themes` 全部为空，因为 B.4 的相邻 Theme（D 维度传统工艺组织）尚未 materialize，不写未审的 Theme 引用。

## 四、执行与验证

- `scripts/hierarchy_stress_test.py`：v0.9，10 Theme、23 Topic、121 membership、118 complete、2452 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`。
- `scripts/audit_content_quality.py`：总发现 0。
- `scripts/audit_repo.py`：EXIT=0，断链 0，Frontmatter 0，类型值不匹配 0，同名消歧 10/10。
- `scripts/run_sync_closure.py --refresh-generated --full`：18/18，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：12 行（3 个 structure_node_create、4 个 hierarchy_mount、5 个 structure_index_update），12/12 `after_sha256` 重新计算匹配。
- 结构健康 130/130；知识结构质量 55/65，`hierarchy_assignment` 仍为 0，这是 2452 个 KU 未挂载的覆盖度信号，不是本批新增结构错误。

## 五、指标变化

| 指标 | h7 后 v0.8 | h8 后 v0.9 | 变化 |
|---|---:|---:|---:|
| Theme | 9 | 10 | +1 |
| Topic | 21 | 23 | +2 |
| Topic membership | 117 | 121 | +4 |
| 完整挂载 KU | 114 | 118 | +4 |
| 未挂载 KU | 2456 | 2452 | −4 |
| Relation 总数 | 6229 | 6237 | +8 |
| `member_of` | 231 | 239 | +8 |
| 隔离单元 | 1466 | 1464 | −2 |
| 结构健康 | 130 | 130 | 0 |
| 知识结构质量 | 55/65 | 55/65 | 0 |
| 内容质量发现 | 0 | 0 | 0 |
| KU / claim / candidate / translation | 2570 / 1242 / 5339 / 2178 | 同左 | 0 |

`member_of` 增加 8：4 个新主挂载各生成 1 条 Theme 关系与 1 条 Topic 关系。隔离单元只减少 2，表示另外 2 个新挂载 KU 原本已有其他显式关系；不能据此推断它们已被充分研究。

## 六、语义边界

- 本批只证明 118 个 KU 完成五级字段挂载，不证明 2570 个 KU 全量挂载，也不证明 B.4 已是稳定分类。
- B.4 是 `pilot` Theme，不表示 T7 已验收或结构闭合；T7 的 D 维度组织、展赛与政策材料尚未 materialize。
- 2452 个未挂载 KU 仍是研究债务；`structure_node_coverage` 仍为 2/4，因为 Domain 与 Dimension 尚未 materialize。
- 巴拿马赛会主维度为 E，1851 年万国博览会不是中国设计对象；两者均不并入 B.4。巴拿马赛会可作为后续 D 维度展赛 Topic 的次挂载候选，但本批不预判。
- 王大凡《富贵寿考瓷板》只有图注一行、confidence 为 low，且与巴拿马赛会绑定；本批不为凑数制造部分挂载，保留为研究债务。
- 两家瓷业公司与两家解放区工厂均只有单源一段；资本、股东、设备、工人数、产量、销售、分配与停办时间全缺，不能写成完整瓷业史或边区工业史。
- 景德镇“拟用机器制瓷、试验煤窑烧炼”是计划表述，来源未说明是否落实；本批不把“拟用”写成“已用”。
- 湖南瓷业公司“1907—1912 年”获奖与公司创办年份的关系未厘清，来源未给正式创办年份；本批不排公司年表。
- 延安玻璃厂与桥儿沟陶瓷厂的“第一个”均无比较范围，不能写成边区工业首创史。
- 磁州解放区陶瓷研究所、子长瓷窑、关中建华瓷厂不在本批挂载；它们与延安两厂的组织或技术联系，来源未说明。

## 七、生成态与门禁

- `06-runtime/automation/index.md` 与 `06-runtime/state/generated-projections-manifest.json` 由完整闭包刷新；本批新增 1 个批次目录与 3 个 runtime 文件（`apply-plan.jsonl`、`manifest.json`、`summary.md`）。
- 生成态只作投影，不是知识裁决本体；automation 文件数由闭包索引确定，本摘要不把估算值写成事实。
- h8 尚未 commit，发布门禁 `--refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 以 `EXIT=1` 结束；该步等价于 `git diff --exit-code HEAD -- <GENERATED_PATHS>`，失败表示生成态快照与 HEAD 有差异，不是内容审计失败，也不是脚本给出的独立状态名。
- 本批未 commit、未 push；外部状态变更等待用户当次明确授权。

## 八、未决事项与下一跳

1. **T7 D 维度**：太平天国、诸匠营、百工衙、南洋劝业会、广东工艺局与磁州陶瓷研究所尚未 materialize；应建立 D 维度 Theme（暂拟 D.5「传统工艺的近代组织、展赛与政策」）与 2–3 个 Topic，并评估巴拿马赛会的次挂载。
2. **巴拿马赛会**：主维度 E，暂不单列 Theme；若 D 维度展赛 Topic 成立，可作 `primary: false` 次挂载，但不得改写其 E 主维度。
3. **王大凡瓷板**：证据过薄，未挂载；需补图版核验、尺寸、题识、参展类别与获奖记录后再裁决。
4. **瓷业公司数据**：景德镇与湖南两家公司缺资本、设备、产量、销售与停办时间；需查《中国的瓷器》、公司档案与地方瓷业史，不能据一段转述写公司史。
5. **解放区工厂数据**：延安玻璃厂与桥儿沟陶瓷厂缺正式厂名、隶属、人员、产量与分配；需查 1944 年《解放日报》原报与陕甘宁边区工业史料。
6. **存量挂载**：2452 个 KU 仍缺五级字段；单源 1919、tentative 2570、低置信 496、隔离 1464 继续作为研究债。
7. **既有欠账**：qian-juntao 重复、shenghuo-weekly 的 C.1.2 回填、h4 排除项复审，均未在本批处理。
