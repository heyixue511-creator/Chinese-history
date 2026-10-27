# h2 批次摘要：T2 纺织、服饰与生活样式的维度拆分

日期：2026-10-27
批次包：`06-runtime/automation/2026-10-27-hierarchy-pilot-h2`
范围：`04-knowledge/structure/` 第二批 Theme/Topic materialize 与 21 个知识元的五级字段挂载
入口：`build-hierarchy`、`hierarchy-field.md`、`晚清至民国设计史主题归并报告_2026-10-26.md`

## 1. 目标与范围

本批处理晚清至民国主题归并报告的 T2「纺织、服饰与生活样式」。T2 的原候选同时包含织绣工艺、染织产品、服制法令与中山装，主维度并不一致；若整体放进 B 维度，会与 `scripts/apply_topic_memberships.py` 的 Theme code 前缀规则冲突，并强制改写已审的 `primary_dimension`。因此本批按主维度拆为两个 sibling Theme：

- `B.2` 近代织绣与服装工艺（B）：承接材料、针法、图案、产品与制作；
- `D.2` 服饰制度与近代生活（D）：承接剪辫易服、服制条例、中山装与国家礼服。

本批 materialize 2 个 `pilot` Theme 与 4 个 `pilot` Topic，并为 21 个已逐对象复读的 KU 写入 `primary_theme`、`secondary_themes`、`role_in_theme`、`topic_memberships` 与修订后的 `hierarchy_scope_note`。其中王才运以 B.2.2 为主挂载、D.2.2 为次挂载，共形成 22 条新 membership。

本批不新增 KU、claim、candidate 或来源字节，不改写 `03基础书籍-md文档/` 与 `02-sources/`，不执行 commit 或 push。

## 2. 结构物化

### 2.1 Theme

| 代码 | 标题 | 主维度 | 次维度 | Topic 数 |
|---|---|---|---|---:|
| `B.2` | 近代织绣与服装工艺 | B | D、E | 2 |
| `D.2` | 服饰制度与近代生活 | D | B、E | 2 |

两个 Theme 均声明 `node_type: theme`、唯一 `theme_code`、`primary_domain` 与 `primary_dimension`；`theme_code` 前缀与主维度一致。B.2 与 D.2 互为 `secondary_themes`，不合并、不重复计数。

### 2.2 Topic

| 代码 | 标题 | 父 Theme | 主维度 | 成员数 |
|---|---|---|---|---:|
| `B.2.1` | 近代纺织品与染织图案 | B.2 | B | 4 |
| `B.2.2` | 刺绣、缂丝与服装工艺 | B.2 | B | 12 |
| `D.2.1` | 剪辫易服与服制改革 | D.2 | D | 3 |
| `D.2.2` | 中山装与国家礼服 | D.2 | D | 3（含 1 个次挂载） |

每个 Topic 均声明 `node_type: topic`、`primary_domain`、`primary_dimension`、`parent_theme` 与 `secondary_themes`，并在正文列出显式 `../../units/...` 成员链接及 role。Topic 的 `primary_dimension` 与父 Theme 一致；`cross_dimension_topics` 为 `[]`。

## 3. 21 个 KU 与 22 条 membership

### 3.1 按 Topic 分配

- B.2.1 近代纺织品与染织图案（4）：
  - `terms/yangbu`、`terms/yindanshilin-sebu`、`terms/jindai-ranchou-ye` — `term_anchor`；
  - `publications/cansang-cuibian` — `source_publication`。
- B.2.2 刺绣、缂丝与服装工艺（12）：
  - `persons/shen-shou`、`persons/shen-jinshui`、`persons/wang-maoxian`、`persons/yang-shouyu`、`persons/du-jinsheng`、`persons/huang-longsheng`、`persons/wang-caiyun` — `key_person`；
  - `publications/xuehuan-xiupu` — `source_publication`；
  - `terms/luanzhenxiu`、`terms/kesi`、`terms/zhijin` — `term_anchor`；
  - `works/jiuxi-shibajian` — `representative_work`。
- D.2.1 剪辫易服与服制改革（3）：
  - `events/jianbian-yifu-1912` — `evidence_event`；
  - `publications/jianbian-tongling`、`publications/fuzhi-tiaoli` — `source_publication`。
- D.2.2 中山装与国家礼服（3）：
  - `persons/sun-yat-sen` — `key_person`；
  - `terms/zhongshanzhuang` — `term_anchor`；
  - `persons/wang-caiyun` — `key_person`，`primary: false`。

### 3.2 字段写回规则

- 保留原 `primary_domain`、`primary_dimension` 与 `secondary_dimensions`，不因 Theme code 前缀强制改写维度。
- `secondary_themes` 只在原 `secondary_dimensions` 已含对应维度时填写：B 侧 KU 有 D 维度者填 `D.2`；D 侧 KU 原 `secondary_dimensions` 未列 B 者保持 `[]`。
- 每个 KU 至少一个 `topic_memberships`，含 `topic`、`role`、`primary` 与逐对象 `scope_note`；王才运有两个 membership，分别主挂 B.2.2、次挂 D.2.2。
- `hierarchy_scope_note` 改写为 v0.3 表述：说明主 Theme、已承接的次 Theme、尚未 materialize 的 E/C 类 Theme，并标注“本次为首批 Topic 挂载”。
- 21 个文件的 `updated` 统一为 `2026-10-27`；`last_verified` 不变，因为本批不重新做事实核验。

### 3.3 语义判断记录

- 洋布、阴丹士林色布、近代染绸业与《蚕桑萃编》归 B.2.1：它们分别是产品、行业与知识文本，不重复挂载已在 B.1.1/D.1.2 的机器纺织企业。
- 沈寿、杨守玉、沈金水、王茂仙、都锦生与《九溪十八涧》归 B.2.2：以针法、绣稿、缂丝产品与丝织风景为工艺主线。
- 黄隆生只挂 B.2.2：其主维度为 B，原 `secondary_dimensions` 为空，不把“参与中山装设计”自动升级为 D.2.2 的制度成员。
- 王才运同时挂 B.2.2 与 D.2.2：其主维度为 B、次维度为 D，前者记裁缝与制作，后者记国家礼服的制作关系人身份。
- 旗袍主维度为 E，当前 E 类 Theme 未 materialize，本批不挂载；只在 B.2/D.2 的边界说明中登记为待复审项。

## 4. 执行与验证

- 写回前逐文件读取 frontmatter，按对象替换层级段，未批量重写正文。
- 21 个 KU 的结构化自检：YAML 解析通过，`primary_theme`、`primary_dimension`、`role_in_theme`、`topic_memberships`、Topic 目标存在性、`updated` 均无错误。
- `python scripts/hierarchy_stress_test.py`：
  - `hierarchy_version: v0.3`；
  - `themes: 4`，`themes_without_topics: 0`；
  - `topics: 9`，`topic_memberships: 49`；
  - `complete_assignments: 48`，`incomplete_assignments: 2522`；
  - `cross_dimension_topics: []`，`apply_permitted: false`。
- `python scripts/audit_content_quality.py`：总发现 0。
- `python scripts/audit_repo.py`：退出码 0；Markdown 断链 0；Frontmatter 缺失/格式错误 0；类型值不匹配 0；层级结构问题 0；同名跨类型组 5，消歧说明 10/10。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18/18 通过，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：32 行，`structure_node_create` 6、`hierarchy_mount` 21、`structure_index_update` 5；32/32 `after_sha256` 校验通过。

## 5. 指标变化

| 指标 | 批次前 | 批次后 |
|---|---:|---:|
| 层级版本 | v0.2 | v0.3 |
| Theme | 2 | 4 |
| Topic | 5 | 9 |
| Topic membership | 27 | 49 |
| 完整五级挂载 | 27 | 48 |
| 未完整挂载 | 2543 | 2522 |
| `structure_node_coverage` | 2/4 | 2/4 |
| relation index | 6052 | 6095 |
| `member_of` 关系 | 54 | 97 |
| 关系类型覆盖 | 3/67 | 3/67 |
| 隔离单元 | 1515 | 1504 |
| 结构健康 | 130/130 | 130/130 |
| 内容质量发现 | 0 | 0 |
| KU 总数 | 2570 | 2570 |
| claim registry | 1242 | 1242 |
| candidate index | 5339 | 5339 |
| translation index | 2178 | 2178 |

`member_of` 的 97 条 = 48 个已挂载 KU 的 48 条 Theme 关系 + 49 条 Topic 关系，由 `build_relation_index.py` 依据 `role_in_theme` 与 `topic_memberships` 生成，不是手工新增关系。

## 6. 语义边界

- 本批只证明 48 个 KU 已完成逐对象挂载，不证明 2570 个 KU 的层级已全量建立。
- Theme/Topic 为 `pilot` 状态，不是最终分类；T3–T7 仍未 materialize，E/C 类 Theme 仍为空。
- `secondary_themes: []` 表示当前没有已物化的对应 Theme，不表示该维度不存在；原 `secondary_dimensions` 与 `hierarchy_scope_note` 保留该信息。
- B.2 与 D.2 的拆分是维度分工，不是对 T2 原主题的否定；两 Theme 的正文互相引用，不把同一 KU 重复计入两个主挂载。
- 隔离单元减少 11 个，只表示这些 KU 因结构成员关系不再完全孤立，不表示其证据密度提高。
- 中山装设计者与早期纽扣数在来源间存在并列表述，本批只记录差异，不在 Theme/Topic 层裁决真伪。

## 7. 生成态与门禁

- `06-runtime/state/current-health.json`：结构健康 130/130；`structure_node_coverage` 为 `2/4`；`hierarchy_version` 为 `v0.3`；完整挂载 48，缺挂载 2522；隔离单元 1504。
- `06-runtime/governance/governance-backlog.md`：P0/P1/P2 均为 `No active items.`；研究债 4 项（单源 1919、tentative 2570、低置信 496、缺层级 2522）；`OPP-ISOLATED` 1504。
- `06-runtime/automation/index.md`：批次目录 204 → 205；文件 1090 → 1093（本包 manifest、apply-plan、summary）。
- 发布门禁 `python scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 处以 `EXIT=1` 失败，因为生成态快照相对 HEAD 仍有未提交差异；状态为 `blocked_pending_commit`。
- 本批未执行 commit 或 push；外部状态变更仍待用户明确授权。

## 8. 未决事项与下一跳

- 2522 个 KU 仍缺 `primary_theme` 与 `topic_memberships`，按研究债保留。
- 晚清至民国报告的 T3–T7 候选主题尚未 materialize；下一批应继续按维度拆分 Theme，避免用 Theme code 前缀强制改写已审 `primary_dimension`。
- E 维度（跨文化技术转移）与 C 维度（商业、视觉与传播）尚无 Theme；旗袍、月份牌广告、书籍装帧等 KU 的 `secondary_themes` 暂时为空。
- B.2 与 D.2 的边界目前以 21 个 KU 的试点为准；后续若出现同时以工艺与制度为主问题的条目，应复审其主维度，而不是自动追加第二个主挂载。
- `scripts/apply_topic_memberships.py` 仍被 `scripts/agent_guard.py` 的 shell 规则阻断（`python scripts/apply_*.py` 被拒），本批继续采用逐文件精确 Edit。后续若要恢复 sanctioned bulk writer，应走 `system-upgrade` 审查 guard 例外，不应绕过门禁。
- 证据层仍无 claim evidence；关系层仍以 claim↔KU 投影和结构成员关系为主。
- commit/push 仅在用户明确授权后执行。
