# h5 批次摘要：T5 B 维度「近代建筑、室内与建造技术」的 B.3 物化

- 批次：`2026-10-27-hierarchy-pilot-h5`
- 日期：2026-10-27（批次开始；收尾跨至 2026-10-28）
- 层级版本：v0.5 → v0.6
- 结论：新增 1 个 Theme、2 个 Topic，主挂载 8 个 KU；14 个 authored 文件加 2 个结构节点文件共 16 个变更文件，16/16 哈希匹配。未 commit、未 push。

## 一、目标与范围

T5「建筑、城市与室内设计」在归并报告中同时覆盖 B 维度（建筑技术、室内与建造）与 D 维度（城市、机构、规划），并触及 E 维度（外来式建筑）。现有 97 个已挂载 KU 的 `primary_dimension` 与 `primary_theme` 前缀全部一致，`scripts/apply_topic_memberships.py` 也按 `primary_theme.split(".", 1)[0]` 强制推导维度；若用一个跨维度 Theme 直接挂 B/D/E 三类 KU，会产生维度前缀冲突。

因此本批只 materialize T5 的 B 维度部分，建立 B.3「近代建筑、室内与建造技术」：

- B.3.1 通商口岸建筑与室内；
- B.3.2 民族形式与纪念建筑。

D 维度的上海/南京/广州城市史、中国营造学社、朱启钤、盖茨公司、上海市市中心区域规划、亚平艺术装饰公司留待后续 D 维度 Theme；E 维度「外来式建筑」术语留待 E Theme。此拆分沿用 T2 按主维度拆 B.2/D.2 的先例，不表示 T5 已经整体闭合。

## 二、结构物化

新增 Theme `04-knowledge/structure/themes/b3-jindai-jianzhu-shinei-jianzao-jishu.md`：

- `node_type: theme`
- `theme_code: B.3`
- `primary_domain: chinese-design-history`
- `primary_dimension: B`
- `secondary_dimensions: [D, E]`
- `status: pilot`

新增 Topic：

| Topic | 研究问题 | 支撑 KU |
|---|---|---|
| B.3.1 通商口岸建筑与室内 | 钢筋混凝土、钢架与新型建材如何进入通商口岸商业建筑，外来式立面如何组织银行、饭店内部空间与装饰？ | 上海砖瓦锯木厂、上海汇丰银行、沙逊大厦 |
| B.3.2 民族形式与纪念建筑 | 中国固有式建筑如何借公开竞图、传统陵墓形制与现代结构，把纪念建筑转化为近代民族形式？ | 中山陵、吕彦直、中国固有式建筑、梁思成、《中国建筑史》 |

两 Topic 按「建造条件—民族形式」分工，不重复计入同一 KU。

## 三、8 个 KU 的挂载与语义决定

8 个 KU 全部为单主挂载、`secondary_themes: []`、`primary: true`，写入 `updated: 2026-10-27`；`last_verified` 不改。

### B.3.1（3 个）

- **上海砖瓦锯木厂**（institution，`key_institution`）：1853 年英商在上海租界开设，专为租界建筑供材。租界市场与外资经营归 D/E 次维度，本批只取建材供应。
- **上海汇丰银行**（work，`representative_work`）：钢筋混凝土承重、外包仿砖石、爱奥尼柱廊与藻井天花，说明新材料首先用于复刻古典样式，而非直接生成新形式。
- **沙逊大厦**（work，`representative_work`）：钢架结构、10 层、A 字形平面、芝加哥学派立面；设计者与内部空间缺载，不作补写。

### B.3.2（5 个）

- **中山陵**（work，`representative_work`）：牌坊—墓道—陵门—碑亭—石阶—祭堂—墓室中轴序列与钟形平面；征图 1927 与设计 1929 两说并存，不排年表。钟形平面有「木铎警世」与「晨钟暮鼓」两说，均保留，不择一。
- **吕彦直**（person，`key_person`）：中山陵竞图首奖，南京中山陵与广州中山纪念堂设计者；竞图制度与规划背景归 D 次维度。
- **中国固有式建筑**（term，`term_anchor`）：20 世纪二三十年代受西方建筑思潮影响、近于折中主义的民族形式类型；上海市市中心区域规划的制度推动归 D 次维度。
- **梁思成**（person，`key_person`）：以抗战时期中国建筑史研究与清华学派民族形式主张为锚点；1949 年后国徽、天安门广场、1961 年文章只作边界说明，不纳入本期。
- **《中国建筑史》**（publication，`supporting_source`）：梁思成抗战时期撰写；目前来源只有一句转述，成书年份、版本与章节缺失，confidence 维持 low。

字段处理：5 个 KU 原先没有 `secondary_dimensions`，本批显式写为 `[]`；其余 3 个保留原有次维度，不因挂入 B.3 而改写主维度。所有 `secondary_themes` 为空，因为 B.3 的相邻主题尚未 materialize，不写不存在或未审的 Theme 引用。

## 四、执行与验证

- `scripts/hierarchy_stress_test.py`：v0.6，7 Theme、16 Topic、98 membership、97 complete、2473 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`。
- `scripts/audit_content_quality.py`：总发现 0。
- `scripts/audit_repo.py`：EXIT=0，断链 0，Frontmatter 0，类型值不匹配 0，同名消歧 10/10。
- `scripts/run_sync_closure.py --refresh-generated --full`：18/18，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：16 行（3 个 structure_node_create、8 个 hierarchy_mount、5 个 structure_index_update），16/16 `after_sha256` 重新计算匹配。
- 结构健康 130/130；知识结构质量 55/65，`hierarchy_assignment` 仍为 0，这是 2473 个 KU 未挂载的覆盖度信号，不是本批新增结构错误。

## 五、指标变化

| 指标 | h4 后 v0.5 | h5 后 v0.6 | 变化 |
|---|---:|---:|---:|
| Theme | 6 | 7 | +1 |
| Topic | 14 | 16 | +2 |
| Topic membership | 90 | 98 | +8 |
| 完整挂载 KU | 89 | 97 | +8 |
| 未挂载 KU | 2481 | 2473 | −8 |
| Relation 总数 | 6177 | 6193 | +16 |
| `member_of` | 179 | 195 | +16 |
| 隔离单元 | 1476 | 1473 | −3 |
| 结构健康 | 130 | 130 | 0 |
| 知识结构质量 | 55/65 | 55/65 | 0 |
| 内容质量发现 | 0 | 0 | 0 |
| KU / claim / candidate / translation | 2570 / 1242 / 5339 / 2178 | 同左 | 0 |

`member_of` 增加 16 而不是 8：每个 KU 为 `role_in_theme` 生成 1 条 Theme 关系，为 `topic_memberships` 生成 1 条 Topic 关系。隔离单元只减少 3，表示另外 5 个 KU 原本已有其他显式关系；不能据此推断它们已被充分研究。

## 六、语义边界

- 本批只证明 97 个 KU 完成五级字段挂载，不证明 2570 个 KU 全量挂载，也不证明 B.3 已是稳定分类。
- B.3 是 `pilot` Theme，不表示 T5 已验收或结构闭合。
- 2473 个未挂载 KU 仍是研究债务；`structure_node_coverage` 仍为 2/4，因为 Domain 与 Dimension 尚未 materialize。
- 8 个 KU 的材料来自既有来源复读，本批没有重新摄入来源，也没有新增 claim。
- 中山陵的年代冲突与钟形平面两说保留为不确定性，不伪装成已有定论。
- 梁思成条目的 1949 年后内容只作边界说明，不进入 B.3 的近代范围。
- 建筑图版、照片与室内空间尚未做视觉核验；本批的形态判断以文字来源为限。

## 七、生成态与门禁

- `06-runtime/automation/index.md` 与 `06-runtime/state/generated-projections-manifest.json` 由完整闭包刷新；生成态只作投影，不是知识裁决本体。
- h5 尚未 commit，发布门禁 `--refresh-generated --check-generated` 预期在 `[17/17] check generated snapshots` 以 `EXIT=1` 结束，状态为 `blocked_pending_commit`；这不是内容失败，而是未提交状态下的预期结果。
- 本批未 commit、未 push；外部状态变更等待用户当次明确授权。

## 八、未决事项与下一跳

1. **D 维度 T5 材料**：上海、南京、广州城市史，中国营造学社、朱启钤、盖茨公司、上海市市中心区域规划、亚平艺术装饰公司，待建 D.3「近代城市、建筑制度与职业」。
2. **E 维度**：`wailaishi-jianzhu` 主维度为 E，暂不挂载；归并报告把 E 视为跨主题的维度标签，不单列 Theme，故不预设 E Theme 必然建立。
3. **1949 年后建筑**：人民大会堂、北京十大建筑、国徽、1961 年文章不并入 B.3。
4. **T6/T7**：设计教育/职业/机构、传统工艺的近代命运尚未 materialize。
5. **存量挂载**：2473 个 KU 仍缺五级字段；单源 1919、tentative 2570、低置信 496、隔离 1473 继续作为研究债。
6. **待复核**：中山陵年代与钟形平面两说、《中国建筑史》低置信来源、建筑图版视觉核验。
7. **既有欠账**：qian-juntao 重复、shenghuo-weekly 的 C.1.2 回填、h4 排除项复审，均未在本批处理。
