# qb1 批次摘要：治理 backlog 质量缺陷清理

日期：2026-10-27
批次包：`06-runtime/automation/2026-10-27-quality-backlog-batch-qb1`
范围：`04-knowledge/units/` 中 20 个知识元的 P0/P1/P2 机械发现
入口：`06-runtime/governance/governance-backlog.md`、`scripts/audit_content_quality.py`

## 1. 目标与范围

本批处理治理 backlog 中可在不新增证据、不改写来源的前提下直接修复的质量缺陷：

- P0：3 个知识元在 `source_count: 1` 时仍标 `confidence: high`；
- P1：8 个知识元缺少翻译覆盖字段，共 27 个字段缺口；
- 内容质量：4 个出版类知识元因 YAML 冒号解析失败被误报为 frontmatter 空字段，合计 16 条发现；
- 内容质量：3 个知识元的正文含占位词或与占位词重合的直引，合计 3 条发现；
- 内容质量：`terms/hunyi` 与 `works/huntianyi` 的 `name_en` 同名但类型不同，合计 1 条发现。

本批不新增 claim、不新增 KU、不修改 candidate index、claim registry、relation index 或来源文件。

## 2. 修复分类与逐项裁定

### 2.1 P0 单源高置信

将以下 3 个知识元的 `confidence` 由 `high` 降为 `medium`，保留 `source_count: 1` 与 `evidence_status: source_backed`：

- `works/baiyu-qianjin-hongbaoshi-wan.md`
- `works/dayu-zhishui-yushan.md`
- `terms/hua-falang.md`

裁定边界：单册来源内复读足以建立 `source_backed`，但不足以支持 `high` 置信；本批只改置信等级，不补外部证据，也不把单源条目降为 `low`。

### 2.2 P1 翻译字段覆盖

按类型补齐缺失字段，原值为中文，英文名保持既有 `name_en` / 描述性译名：

- persons：`fu-hao`、`pan-geng`、`wang-yirong` 补 `name_original`、`language_original: zh`、`name_zh`、`translation_status: provisional`；
- works：`lingtai`、`qin-gong-bo`、`shi-qiang-pan` 补 `title_original`、`title_original_language: zh`、`title_zh`；
- publications：`jiaguwen-bian`、`jinwen-bian` 补 `title_original`、`title_original_language: zh`、`title_zh`。

裁定边界：`translation_status` 统一为 `provisional`，因为来源未提供官方英文名；不把描述性译名写成已确认标准译名。

### 2.3 内容质量：YAML 解析失败

以下 4 个出版类知识元的 `title`、`name_en`、`translation_note` 含未加引号的 ASCII 冒号，导致 `yaml.safe_load` 失败，审计器将 frontmatter 视为空对象并误报 16 条空字段：

- `publications/liezi-tangwen.md`
- `publications/qinlv-gonglv.md`
- `publications/songshi-yufuzhi.md`
- `publications/zhongguo-dalishi.md`

修复方式：给上述三个标量加双引号，不改写字段内容。修复后 4 个文件均可正常解析，16 条发现全部消失。

### 2.4 内容质量：占位措辞

- `persons/zhao-nong.md`：`scope_note` 的“均待补充”改为“来源未载”；核心内容中同一段直引的“压缩和调整了相关内容”改为间接表述“压缩调整原有内容”，保留原意。
- `publications/zhongguo-yishu-shejishi-zhaonong-2009.md`：同一序言直引改为间接表述，移除“相关内容”字样。
- `works/he-zun.md`：`scope_note` 的“器形与铭文释文均待补充”改为“来源未载器形与铭文释文”。

裁定边界：三处均属“来源确实未载”或“直引中恰好含审计关键词”，不是把已有内容删空；改写后仍保留“来源未载”的诚实状态。

### 2.5 内容质量：跨类型同名

`terms/hunyi.md` 与 `works/huntianyi.md` 的 `name_en` 均为 `Armillary Sphere`，但前者是仪器类型/概念，后者是具体器物。两文件分别在“相关知识元”节增加含“类型消歧”字样的说明，明确 `term` 与 `work` 的边界。

裁定边界：不合并、不改名；同名是类型差异而非重复条目。

## 3. 执行与验证

- 逐文件先读后写，仅改目标字段或目标句，未批量重写正文。
- 全部 20 个文件修改后执行 frontmatter 解析与必需字段检查，20/20 通过。
- `python scripts/audit_content_quality.py`：总发现 20 → 0。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18/18 通过，测试 250 passed + 16 subtests（51.21s）。
- 健康快照重新生成后，`verification_semantic_issues` 的 `source_count_1_high_confidence` 由 3 条降为 0 条。

## 4. 指标变化

- 结构健康：104/130 → 130/130。
- 内容质量发现：20 → 0。
- 系统缺陷：P0 1 → 0；P1 10 → 0；P2 2 → 0。
- 验证语义冲突：3 → 0。
- 知识元总数：2570，未变。
- claim registry：1242 条，未变。
- candidate index：5339 条（applied 4234、no_delta 234、rejected 871、active 0），未变。
- translation-index：2178 条，条目数未变；8 个知识元的字段内容已补齐。
- relation-index：5998 条，未变。
- knowledge graph：2570 节点、0 链接，未变。
- 自动化索引：目录 202 → 203；文件 1084 → 1087（本包 manifest、apply-plan、summary 三个文件）。
- 研究债仍为 4 项：RD-SINGLE 1919、RD-TENTATIVE 2570、RD-LOW-CONFIDENCE 496、RD-HIERARCHY 2570。
- 候选机会仍为 1 项：OPP-ISOLATED 1524。

## 5. 语义边界

- 本批只处理机械可判定的质量缺陷，不评估知识价值、事实充分性或叙述密度。
- 置信降级不等于否定条目；单源条目仍为 `source_backed`，只是不再声称 `high`。
- 翻译字段补齐不产生新的翻译裁决；`provisional` 明确表示英文名为描述性译名。
- 占位措辞改写不新增来源信息；“来源未载”是范围声明，不是补写。
- 类型消歧只解释 `term` 与 `work` 的差异，不建立正式 relation。

## 6. 生成态与门禁

- 闭包刷新后，`06-runtime/state/current-health.json` 与 `06-runtime/governance/governance-backlog.md` 均显示 P0/P1/P2 为空。
- `06-runtime/state/generated-projections-manifest.json` 已随闭包更新。
- 发布门禁在 `[17/17] check generated snapshots` 处以 `EXIT=1` 失败，因为生成态快照相对 HEAD 仍有未提交差异，状态为 `blocked_pending_commit`。
- 本批未执行 commit 或 push；外部状态变更仍待用户明确授权。

## 7. 闭包结果

- 18 个闭包步骤全部通过；无失败步骤。
- 内容审计、关系一致性审计、仓库审计、规则漂移、Skill 注册表、空白检查、升级链审计与测试均通过。
- 本批未修改 `02-sources/` 或 `03基础书籍-md文档/` 的任何来源字节。
- 本批未创建分支、未创建 worktree。

## 8. 未决事项与下一跳

- 机械质量缺陷已清零；剩余为研究债与结构缺口，不是本轮可机械修复的系统缺陷。
- 证据层：claim 的 `supports` 仍为空，evidence JSONL 尚未建立；`verify_apply_evidence.py` 目前只写 KU，不写 claim evidence。
- 关系层：relation-index 仍只有 claim↔KU 的 `supported_by` 投影，67 类关系中仅覆盖 2 类。
- 层级层：Theme/Topic 仍为 0，2570 个 KU 缺完整层级指派；`structure_node_coverage` 为 0/4。
- 下一阶段应优先进入层级节点 materialize 或 evidence 层建设；commit/push 仅在用户明确授权后执行。
