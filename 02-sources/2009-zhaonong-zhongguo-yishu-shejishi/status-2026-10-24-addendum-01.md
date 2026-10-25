# 状态补编 01：独立复读、补立与验收

- 补编日期：2026-10-24
- 关联记录：`status-2026-10-24.md`
- 处理包：`03-processing/2009-zhaonong-zhongguo-yishu-shejishi/`

## 本轮新增事实

- 12 个分段独立语义复读完成，首轮补立 94 个语义单元、237 个候选；修正 33 个语义单元、85 个候选（88 条更新）、123 个块；跳过 8 条包外或不可执行 finding。
- 四组独立增量复读互不重叠，覆盖 127 个语义单元与 322 个候选（全部 94 个/237 个补立项，另抽检 33 个/85 个原有项）；初判 30 条 findings（`blocking` 1、`major` 5、`minor` 24），定点复核另记录 3 条 minor（`daf-1-07`、`dcf-1-02`、`daf-1-08`）；最终 33 条全部闭合，`still_open` 0。
- 主要修正：殳按西周/春秋战国拆分；清末地方官书局拆为 1 个 term 类别与 4 个 institution；罗汉床改 work；民俗村改 term；何家村统一 place；门神补汉唐；大汶口文化证据范围收窄；明代西安城统一；书籍装帧分组按原文两组改写；16 条 evidence 路径修正；修改候选的 `updated_at` 回填。
- 最终计数：semantic units 705；candidates 1696（unit 1320，claim 376）。
- `manifest.json` 状态由 `running` 改为 `completed`，并写入 `semantic_acceptance`：
  - `reread_status`：`accepted_with_findings`
  - `omission_count`：0（33 条 findings 全部闭合）
  - `source_version`：`sha256:8205f54c5dbc80c38a01c32d9cf491e3f242274c2734d70034e43c051603d951`
- `scripts/validate_processing_package.py`：`valid: true`，`issues: []`。

## 边界

- 验收只覆盖原文语义召回与复读状态；不证明候选已写入 `04-knowledge/`，不证明事实已经外部核实，也不声称已逐张视觉核验图版。
- 全部 1696 个候选保持 `needs_evidence` / `decision.status=pending`；未写入知识库。
- 未 commit、未 push，未创建分支或 worktree；来源文件未改写。
- 本补编不改变来源指纹与覆盖范围；`status-2026-10-24.md` 中“尚未完成独立语义复读”等未完成事项，以本补编为准。
