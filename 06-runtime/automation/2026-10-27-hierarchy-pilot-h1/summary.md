# h1 批次摘要：1840–1949 层级试点

日期：2026-10-27
批次包：`06-runtime/automation/2026-10-27-hierarchy-pilot-h1`
范围：`04-knowledge/structure/` 首批 Theme/Topic materialize 与 27 个知识元的五级字段挂载
入口：`build-hierarchy`、`hierarchy-field.md`、`晚清至民国设计史主题归并报告_2026-10-26.md`

## 1. 目标与范围

本批把晚清至民国主题归并报告中的候选主题，转为可审计的首批结构节点：

- materialize 2 个 `pilot` Theme：`B.1` 近代造物技术转型、`D.1` 洋务企业与近代工业组织；
- materialize 5 个 `pilot` Topic，其中 B.1 下 2 个、D.1 下 3 个；
- 为 27 个已逐对象复读的 KU 写入 `primary_theme`、`secondary_themes`、`role_in_theme`、`topic_memberships` 与修订后的 `hierarchy_scope_note`；
- 同步层级索引、维度观察队列与两个结构目录 README 的过期状态；
- 附带清除 2 条跨类型同名但缺 `disambiguation` 字段的残留发现。

本批不新增 KU、claim、candidate 或来源字节，不改写 `03基础书籍-md文档/` 与 `02-sources/`，不执行 commit 或 push。

## 2. 结构物化

### 2.1 Theme

| 代码 | 标题 | 主维度 | 次维度 | Topic 数 |
|---|---|---|---|---|
| `B.1` | 近代造物技术转型 | B | D、E | 2 |
| `D.1` | 洋务企业与近代工业组织 | D | B、E | 3 |

两个 Theme 均声明 `node_type: theme`、唯一 `theme_code`、`primary_domain` 与 `primary_dimension`；`theme_code` 前缀与主维度一致，仓库审计的 `theme_dimension_mismatch` 为 0。

### 2.2 Topic

| 代码 | 标题 | 父 Theme | 主维度 | 成员数 |
|---|---|---|---|---|
| `B.1.1` | 机器纺织与造纸技术 | B.1 | B | 5 |
| `B.1.2` | 造船、铁路与近代工程 | B.1 | B | 7 |
| `D.1.1` | 洋务军工与造船企业 | D.1 | D | 8 |
| `D.1.2` | 近代纺织企业与实业家 | D.1 | D | 3 |
| `D.1.3` | 交通、电信与金融组织 | D.1 | D | 4 |

每个 Topic 均声明 `node_type: topic`、`primary_domain`、`primary_dimension`、`parent_theme` 与 `secondary_themes`，并在正文列出显式 `../../units/...` 成员链接及 role。Topic 的 `primary_dimension` 与父 Theme 一致，`topic_dimension_mismatch` 为 0。

## 3. 27 个 KU 的挂载

### 3.1 按 Topic 分配

- B.1.1 机器纺织与造纸技术（5）：
  - `institutions/shanghai-jiqi-zhibuju`、`institutions/jichanglong-sichang`、`institutions/hengyuan-zhahuachang`、`institutions/lunzhang-zaozhi-ju` — `key_institution`；
  - `procedures/xiandai-zaozhi-jishu` — `procedure`。
- B.1.2 造船、铁路与近代工程（7）：
  - `works/huanghu-hao`、`works/jingzhang-tielu`、`works/tangxu-tielu`、`works/wusong-tielu`、`works/longhao-jiche` — `representative_work`；
  - `persons/xu-shou`、`persons/zhan-tianyou` — `key_person`。
- D.1.1 洋务军工与造船企业（8）：
  - `institutions/jiangnan-zhizao-zongju`、`institutions/fujian-chuanzhengju`、`institutions/anqing-junxiesuo`、`institutions/hubei-qiangpaochang`、`institutions/tianjin-jiqiju`、`institutions/jinling-jiqiju` — `key_institution`；
  - `persons/li-hongzhang`、`persons/zuo-zongtang` — `key_person`。
- D.1.2 近代纺织企业与实业家（3）：
  - `institutions/dasheng-shachang`、`institutions/shenxin-fangzhi-gongsi` — `key_institution`；
  - `persons/zhang-jian` — `key_person`。
- D.1.3 交通、电信与金融组织（4）：
  - `institutions/lunchuan-zhaoshangju`、`institutions/zhongtian-dianjichang`、`institutions/zhongguo-renmin-yinhang` — `key_institution`；
  - `persons/zhou-renzhai` — `key_person`。

### 3.2 字段写回规则

- 保留原 `primary_domain`、`primary_dimension` 与 `secondary_dimensions`，不因 Theme code 前缀强制改写维度。
- `secondary_themes` 只在原 `secondary_dimensions` 已含对应维度时填写：B 侧 KU 有 D 维度者填 `D.1`，D 侧 KU 有 B 维度者填 `B.1`；无对应已物化 Theme 的维度保持 `secondary_themes: []`。
- 每个 KU 恰好一个 `topic_memberships`，含 `topic`、`role`、`primary: true` 与逐对象 `scope_note`。
- `hierarchy_scope_note` 改写为 v0.2 表述：说明主 Theme、已承接的次 Theme、尚未 materialize 的 E/C 类 Theme，并标注“本次为首批 Topic 挂载”。
- 27 个文件的 `updated` 统一为 `2026-10-27`；`last_verified` 不变，因为本批不重新做事实核验。

### 3.3 附带质量修复

`publications/shijing.md` 与 `terms/shijing.md` 仅拼音同名，前者为《诗经》诗歌总集，后者为石经刻石类别。两者各补 `disambiguation` frontmatter 字段并更新 `updated`，使 5 组跨类型同名的 10 个文件全部具备消歧说明。

## 4. 执行与验证

- 写回前逐文件读取 frontmatter，按对象替换层级段，未批量重写正文。
- 27 个 KU 的结构化自检：YAML 解析 27/27 通过，`primary_theme`、`primary_dimension`、`role_in_theme`、`topic_memberships`、Topic 目标存在性、`updated` 全部零错误。
- `python scripts/hierarchy_stress_test.py`：
  - `hierarchy_version: v0.2`；
  - `themes: 2`，`themes_without_topics: 0`；
  - `topics: 5`，`topic_memberships: 27`；
  - `complete_assignments: 27`，`incomplete_assignments: 2543`；
  - `cross_dimension_topics: []`，`apply_permitted: false`。
- `python scripts/audit_content_quality.py`：总发现 0。
- `python scripts/audit_repo.py`：退出码 0；Markdown 断链 0；Frontmatter 缺失/格式错误 0；层级结构问题 0；同名跨类型组 5，消歧说明 10/10。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18/18 通过，`250 passed, 16 subtests passed`（54.72s）。
- 工作包建立后再次执行 `--refresh-generated`：16/16 通过。

## 5. 指标变化

| 指标 | 批次前 | 批次后 |
|---|---:|---:|
| 层级版本 | v0.1 | v0.2 |
| Theme | 0 | 2 |
| Topic | 0 | 5 |
| Topic membership | 0 | 27 |
| 完整五级挂载 | 0 | 27 |
| 未完整挂载 | 2570 | 2543 |
| `structure_node_coverage` | 0/4 | 2/4 |
| relation index | 5998 | 6052 |
| `member_of` 关系 | 0 | 54 |
| 关系类型覆盖 | 2/67 | 3/67 |
| 隔离单元 | 1524 | 1515 |
| 结构健康 | 130/130 | 130/130 |
| 内容质量发现 | 0 | 0 |
| KU 总数 | 2570 | 2570 |
| claim registry | 1242 | 1242 |
| candidate index | 5339 | 5339 |
| translation index | 2178 | 2178 |

`member_of` 的 54 条 = 27 个 KU ×（1 条 Theme 关系 + 1 条 Topic 关系），由 `build_relation_index.py` 依据 `role_in_theme` 与 `topic_memberships` 生成，不是手工新增关系。

## 6. 语义边界

- 本批只证明 27 个 KU 已完成逐对象挂载，不证明 2570 个 KU 的层级已全量建立。
- Theme/Topic 为 `pilot` 状态，不是最终分类；T2–T7 仍未 materialize，E/C 类 Theme 仍为空。
- `secondary_themes: []` 表示当前没有已物化的对应 Theme，不表示该维度不存在；原 `secondary_dimensions` 与 `hierarchy_scope_note` 保留该信息。
- `member_of` 是结构成员关系，不是因果关系、影响关系或历史先后关系。
- 隔离单元减少 9 个，只表示这 9 个 KU 因结构成员关系不再完全孤立，不表示其证据密度提高。

## 7. 生成态与门禁

- `06-runtime/state/current-health.json`：结构健康 130/130；`structure_node_coverage` 为 `2/4`；`hierarchy_version` 为 `v0.2`；完整挂载 27，缺挂载 2543。
- `06-runtime/governance/governance-backlog.md`：P0/P1/P2 均为 `No active items.`；研究债 4 项（单源 1919、tentative 2570、低置信 496、缺层级 2543）；`OPP-ISOLATED` 1515。
- `06-runtime/automation/index.md`：批次目录 203 → 204；文件 1087 → 1090（本包 manifest、apply-plan、summary）。
- 发布门禁 `python scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 处以 `EXIT=1` 失败，因为生成态快照相对 HEAD 仍有未提交差异；状态为 `blocked_pending_commit`。
- 本批未执行 commit 或 push；外部状态变更仍待用户明确授权。

## 8. 未决事项与下一跳

- 2543 个 KU 仍缺 `primary_theme` 与 `topic_memberships`，按研究债保留。
- 晚清至民国报告的 T2–T7 候选主题尚未 materialize；下一批应继续按维度拆分 Theme，避免用 Theme code 前缀强制改写已审 `primary_dimension`。
- E 维度（跨文化技术转移）与 C 维度（商业、视觉与传播）尚无 Theme；相关 KU 的 `secondary_themes` 暂时为空。
- `scripts/apply_topic_memberships.py` 是登记在案的批量执行器，但被 `scripts/agent_guard.py` 的 shell 规则阻断（`python scripts/apply_*.py` 被拒），本批因此采用逐文件精确 Edit。后续若要恢复 sanctioned bulk writer，应走 `system-upgrade` 审查 guard 例外，不应绕过门禁。
- 证据层仍无 claim evidence；关系层仍以 claim↔KU 投影和结构成员关系为主。
- commit/push 仅在用户明确授权后执行。
