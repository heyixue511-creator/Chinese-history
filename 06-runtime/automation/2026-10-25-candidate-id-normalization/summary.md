# 候选 ID 全局规范化（2026-10-25）

## 目标

统一候选索引要求全局唯一 `candidate_id`；六册处理包此前各自从 `cand-01-01` 起编号，造成跨包冲突，`build_discovery_index.py` 因此 fail closed。本工作包只做标识符迁移，不改候选语义、状态或证据。

## 执行

- 包数：6
- 迁移 ID 数：5605
- 新格式：`<doc_id>:<原 candidate_id>`，例如 `2004-gaofeng-zhongguo-shejishi:cand-01-01`
- 覆盖文件：candidate-ledger、source-map、semantic-units、summary、manifest 中的候选 ID 引用
- 写法：逐包原始 UTF-8 文本替换；写入前验证逆替换可逐字节还原原文，证明只改了 ID
- 备份：`C:\Users\lenovo\AppData\Local\Temp\book-id-normalization-20261025\backup-20261025-004937`
- 映射表：`id-mapping.jsonl`

## 后续修复

ID 迁移后运行 `check_reverse_refs.py`，发现 Books 1–3 存在迁移前即已存在的反向引用缺口（Book 1：18 项；Book 2：48 项；Book 3：143 项）。已按确定性规则重建块引用：

- `semantic_unit_refs` 由 `semantic-units.jsonl` 的 `source_block_refs` 派生；
- `candidate_refs` 由候选 `payload.source_span.block_ids` 派生；
- 仅 Books 1–3 实际变更（4/16、16/49、0/144 个块），Books 4–6 无变化。

修复明细见 `reverse-ref-repair.json`；备份在 `reverse-ref-backup-20261025-005045`。修复后六包 validator 全部 `valid`，`check_reverse_refs` 全部 `ok`。

## 边界

- 未改变任何候选的 payload、state、decision、evidence_refs 或 source_span。
- 未改变来源文件。
- 语义验收不因标识符迁移或反向引用重建而重开；但索引与验证需重新运行。
