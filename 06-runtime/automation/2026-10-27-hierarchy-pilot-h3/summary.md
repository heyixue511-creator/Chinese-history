# h3 批次摘要：T3 商业美术与广告的 C.1 物化

日期：2026-10-27
批次包：`06-runtime/automation/2026-10-27-hierarchy-pilot-h3`
范围：`04-knowledge/structure/` 第三批 Theme/Topic materialize 与 14 个知识元的五级字段挂载
入口：`build-hierarchy`、`hierarchy-field.md`、`晚清至民国设计史主题归并报告_2026-10-26.md`

## 1. 目标与范围

本批处理晚清至民国主题归并报告的 T3「商业美术与广告」。候选索引中 C 维度共 78 条；按“晚清至民国”时段逐条复读后，保留 14 条以 C 为主维度的广告、报刊、画报与机构标识条目，排除改革开放后的书籍装帧、国徽与铁路标志、2008 年奥运标志等 1949 年后条目。排除项不删除，仍留在候选索引中，留给 C.2 或后续 Theme 复审。

本批 materialize 1 个 `pilot` Theme 与 2 个 `pilot` Topic，并为 14 个已逐对象复读的 KU 写入 `primary_theme`、`secondary_themes`、`role_in_theme`、`topic_memberships` 与修订后的 `hierarchy_scope_note`。14 个 KU 均为单一主挂载，无次挂载；共形成 14 条新 membership。

本批不新增 KU、claim、candidate 或来源字节，不改写 `03基础书籍-md文档/` 与 `02-sources/`，不执行 commit 或 push。

## 2. 结构物化

### 2.1 Theme

| 代码 | 标题 | 主维度 | 次维度 | Topic 数 |
|---|---|---|---|---:|
| `C.1` | 商业美术与广告 | C | D、E | 2 |

C.1 声明 `node_type: theme`、唯一 `theme_code`、`primary_domain: chinese-design-history` 与 `primary_dimension: C`。本批候选的主维度均为 C，因此不再像 T2 那样按主维度拆分；Theme code 前缀与主维度一致，不触发 `apply_topic_memberships.py` 的强制改写规则。

C.1 的边界：

- 纳入月份牌、月份牌画家、英美烟草公司广告部、《良友》画报广告、《申报》《上海新报》报纸广告、《中国一日》书籍广告、幌子、招贴、粤汉铁路徽章与北洋机器局标志。
- 排除书籍装帧、封面设计、印刷技术与出版机构，留给 C.2。
- 排除 1949 年后的广告与标志。
- 月份牌的消费市场与广告经营只在 D 维度作次维度，不主挂 D.2。

### 2.2 Topic

| 代码 | 标题 | 父 Theme | 主维度 | 成员数 |
|---|---|---|---|---:|
| `C.1.1` | 月份牌与商业广告 | C.1 | C | 7 |
| `C.1.2` | 报刊广告与机构标识 | C.1 | C | 7 |

每个 Topic 均声明 `node_type: topic`、`primary_domain`、`primary_dimension`、`parent_theme` 与 `secondary_themes`，并在正文列出显式 `../../units/...` 成员链接及 role。两个 Topic 的 `primary_dimension` 与父 Theme 一致；`cross_dimension_topics` 为 `[]`。

两个 Topic 的 `secondary_themes` 均为 `[]`：现有 D.2 为服饰制度与近代生活、B.2 为织绣与服装工艺，均不承接广告市场或广告工艺；E 类 Theme 尚未 materialize。故不把“D/E 次维度存在”误写成“已有对应次 Theme”。

## 3. 14 个 KU 与 14 条 membership

### 3.1 按 Topic 分配

- C.1.1 月份牌与商业广告（7）：
  - `terms/yuefenpai` — `term_anchor`；
  - `persons/zheng-mantuo`、`persons/hang-zhiying`、`persons/jin-meisheng`、`persons/li-mubai` — `key_person`；
  - `institutions/yingmei-yancao-gongsi` — `key_institution`；
  - `publications/liangyou` — `source_publication`。
- C.1.2 报刊广告与机构标识（7）：
  - `publications/shenbao`、`publications/shanghai-xinbao` — `source_publication`；
  - `works/zhongguo-yiri-guanggao` — `representative_work`；
  - `terms/huangzi`、`terms/zhao-tie` — `term_anchor`；
  - `works/yuehan-tielu-huizhang`、`works/beiyang-jiqiju-biaozhi` — `representative_work`。

### 3.2 字段写回规则

- 保留原 `primary_domain`、`primary_dimension` 与 `secondary_dimensions`，不因 Theme code 前缀强制改写维度。
- `primary_theme` 统一为 `C.1`；`secondary_themes` 统一为 `[]`，因为本批没有与 D/E/B 次维度匹配的已物化 Theme。`[]` 不表示次维度不存在，原 `secondary_dimensions` 与 `hierarchy_scope_note` 保留该信息。
- 每个 KU 一个 `topic_memberships`，含 `topic`、`role`、`primary: true` 与逐对象 `scope_note`；本批无次挂载。
- `hierarchy_scope_note` 改写为 v0.4 表述：说明 C.1 的主 Theme、次维度为何未挂 Theme，并标注“本次为首批 Topic 挂载”。
- 14 个文件的 `updated` 统一为 `2026-10-27`；`last_verified` 不变，因为本批不重新做事实核验。

### 3.3 语义判断记录

- 月份牌形式、四位月份牌画家、英美烟草公司与《良友》画报归 C.1.1：这 7 条共同构成“图像技法—广告机构—画报媒介”的商业广告链。
- 《申报》《上海新报》《中国一日》广告、幌子、招贴、粤汉铁路徽章与北洋机器局标志归 C.1.2：这 7 条共同构成“报纸版面—书刊广告—店铺标识—机构徽章”的视觉传达链。
- `works/zhongguo-yiri-guanggao` 的候选 JSONL 曾写作 `publications/`，实际文件在 `works/`；本批按实际路径写回，未移动文件。
- 金梅生、李慕白的 `secondary_dimensions` 含 D，但 D 指的是月份牌的广告市场属性，不是 D.2 的服饰制度；英美烟草公司的 D/E 指外资经营与跨文化互动，也不是 D.2。故四者均不强行挂 D.2。
- 幌子、招贴是跨时段术语，古代段材料比例高；本批只把近代商业美术用法纳入 C.1.2，古代段作为谱系背景，不作为近代证据。
- 英美烟草公司条目明确记“来源未说明四位月份牌代表是否均受雇于公司”，本批不据此推断雇佣关系。
- 北洋机器局标志的图注作“民国”，而北洋机器局为清末机构；本批照录并保留时段张力，不在 Theme/Topic 层裁决年代。
- 1949 年后的广告、包装、国徽、铁路标志与奥运标志不并入 C.1；它们仍留在候选索引，等待 C.2 或其他 Theme。

## 4. 执行与验证

- 写回前逐文件读取 frontmatter，按对象替换层级段，未批量重写正文。
- 14 个 KU 与 3 个结构文件的结构化自检：YAML 解析通过，`primary_theme`、`primary_dimension`、`role_in_theme`、`topic_memberships`、Topic 目标存在性、`updated` 均无错误。
- `python scripts/hierarchy_stress_test.py`：
  - `hierarchy_version: v0.4`；
  - `themes: 5`，`themes_without_topics: 0`；
  - `topics: 11`，`topic_memberships: 63`；
  - `complete_assignments: 62`，`incomplete_assignments: 2508`；
  - `cross_dimension_topics: []`，`apply_permitted: false`。
- `python scripts/audit_content_quality.py`：总发现 0。
- `python scripts/audit_repo.py`：退出码 0；Markdown 断链 0；Frontmatter 缺失/格式错误 0；类型值不匹配 0；层级结构问题 0；同名跨类型组 5，消歧说明 10/10。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18/18 通过，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：22 行，`structure_node_create` 3、`hierarchy_mount` 14、`structure_index_update` 5；22/22 `after_sha256` 校验通过。

## 5. 指标变化

| 指标 | 批次前 | 批次后 |
|---|---:|---:|
| 层级版本 | v0.3 | v0.4 |
| Theme | 4 | 5 |
| Topic | 9 | 11 |
| Topic membership | 49 | 63 |
| 完整五级挂载 | 48 | 62 |
| 未完整挂载 | 2522 | 2508 |
| `structure_node_coverage` | 2/4 | 2/4 |
| relation index | 6095 | 6123 |
| `member_of` 关系 | 97 | 125 |
| 关系类型覆盖 | 3/67 | 3/67 |
| 隔离单元 | 1504 | 1495 |
| 结构健康 | 130/130 | 130/130 |
| 内容质量发现 | 0 | 0 |
| KU 总数 | 2570 | 2570 |
| claim registry | 1242 | 1242 |
| candidate index | 5339 | 5339 |
| translation index | 2178 | 2178 |

`member_of` 的 125 条 = 62 个已挂载 KU 的 62 条 Theme 关系 + 63 条 Topic 关系，由 `build_relation_index.py` 依据 `role_in_theme` 与 `topic_memberships` 生成，不是手工新增关系。

## 6. 语义边界

- 本批只证明 62 个 KU 已完成逐对象挂载，不证明 2570 个 KU 的层级已全量建立。
- C.1 为 `pilot` 状态，不是最终分类；T4–T7 仍未 materialize，C.2 书籍装帧与印刷、E 维度跨文化技术转移仍为空。
- `secondary_themes: []` 表示当前没有已物化的对应 Theme，不表示该维度不存在；原 `secondary_dimensions` 与 `hierarchy_scope_note` 保留该信息。
- C.1 与 C.2 是同一 C 维度内的媒介分工：C.1 解释“商品与机构如何被看见”，C.2 解释“书刊如何被制作与出版”；两 Theme 不重复计数同一 KU。
- 隔离单元减少 9 个，只表示这些 KU 因结构成员关系不再完全孤立，不表示其证据密度提高。
- 月份牌与 D 维度的消费市场关系尚未建立正式 relation，只在本 Topic 边界说明中记录。
- 证据层仍无 claim evidence；关系层仍以 claim↔KU 投影和结构成员关系为主。

## 7. 生成态与门禁

- `06-runtime/state/current-health.json`：结构健康 130/130；`structure_node_coverage` 为 `2/4`；`hierarchy_version` 为 `v0.4`；完整挂载 62，缺挂载 2508；隔离单元 1495。
- `06-runtime/governance/governance-backlog.md`：P0/P1/P2 均为 `No active items.`；研究债 4 项（单源 1919、tentative 2570、低置信 496、缺层级 2508）；`OPP-ISOLATED` 1495。
- `06-runtime/automation/index.md`：批次目录 205 → 206；文件 1093 → 1096（本包 manifest、apply-plan、summary）。
- 发布门禁 `python scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 处以 `EXIT=1` 失败，因为生成态快照相对 HEAD 仍有未提交差异；状态为 `blocked_pending_commit`。
- 本批未执行 commit 或 push；外部状态变更仍待用户明确授权。

## 8. 未决事项与下一跳

- 2508 个 KU 仍缺 `primary_theme` 与 `topic_memberships`，按研究债保留。
- 晚清至民国报告的 T4「书籍装帧、印刷与出版」应 materialize 为 C.2，与本批 C.1 分工；T5 建筑/城市/室内、T6 设计教育/职业/机构、T7 传统工艺的近代命运仍待处理。
- E 维度（跨文化技术转移）仍无 Theme；旗袍、月份牌中的西式技法来源等条目继续暂缓。
- 月份牌原稿、报纸广告图像、徽章与标志实物均未视觉核验；多数画家条目只有列名，证据密度不均。
- 证据层仍无 claim evidence；关系层仍以 claim↔KU 投影和结构成员关系为主。
- commit/push 仅在用户明确授权后执行。
