# 处理状态补记 01：中国设计艺术史论（李立新，2011）

- **记录日期**：2026-10-24
- **doc_id**：`2011-lilixin-zhongguo-sheji-yishu-shilun`
- **处理包**：`03-processing/2011-lilixin-zhongguo-sheji-yishu-shilun/`
- **处理 profile**：`compact-v4`
- **当前状态**：`completed`（独立语义复读、修补与收尾已完成）

本文件是 `status-2026-10-24.md` 的追加补记；原状态文件保持只读，不改写。

## 补记原因

原状态记录停在“六段复读进行中、chunk-04 待 delta review”。此后完成了复读修补、去重、跨类型裁决、补充复核与收尾：

- chunk-03、chunk-04 的 `needs_revision` 修复均已应用并完成定向 delta 复评，结论均为 `accepted_with_findings`。
- 去重专项完成 6 组同类型同名合并，541 降至 535；复核记录 3 项发现（dd-01 major、dd-02/03 minor），均已修补。复核后又补并第 7 组“意匠化（设计）”与“意匠化设计”，535 降至 534。
- 指南车跨类型裁决：`cand-05-15`（work）并入 `cand-03-61`（term），`cand-05-15` 保留为 `rejected` 并恢复块级 provenance。
- 补充复核记录 6 项发现（sd-01/02 两项 blocking、sd-03 major、sd-04/05/06 minor）。sd-02 恢复 `b0093` 对 `cand-05-15` 的反向引用；sd-04/05 修正 `cand-01-72` 的“宋之前／中国古代造物／汉代以来”范围表述，span 延至 L1169；sd-06 为 `cand-03-61` 补 L892、L897 证据。
- 修补后定向 delta 复评结论为 `accepted`，`findings=[]`。
- 收尾刷新 `summary.md` 计数与复读记录，重新计算四类输出文件哈希并写回 `manifest.output_hashes`，写入 `semantic_acceptance`，状态置为 `completed`。

## 最终计数

- source blocks：149；复读 149，未读 0；无候选且无理由块 0。
- semantic units：221。
- candidates：534（unit 339、claim 195）；状态 `needs_evidence` 533、`rejected` 1。
- unit_type 分布：event 11、institution 19、person 60、place 38、procedure 12、publication 45、term 80、work 74。
- 复读与修订发现合计 111 项（4 blocking、44 major、63 minor）：六段初轮 96 项、两个 delta 6 项、去重复核 3 项、补充复核 6 项；修补 delta 0 项。

## 复核结果

- 机械审计：block 覆盖、未读、未知引用、span/evidence、引文与数字、重复 slug、非法 unit_type 均为 0 异常。
- `check_reverse_refs.py`：`ok=true`、`count=0`。
- 仓库校验：`python scripts/validate_processing_package.py "03-processing/2011-lilixin-zhongguo-sheji-yishu-shilun"` 返回 `valid: true`、`issues: []`。
- `semantic_acceptance`：`reread_status=accepted_with_findings`、`reviewer_kind=agent`、`omission_count=0`、`source_version` 与聚合输入指纹一致。

## 指纹

- 聚合输入指纹：`sha256:76a0d14b9bcc29b56170cb15c9a16cc62b8dc21d504970dfd805bc6168370f99`
- 来源聚合指纹未变；`semantic_acceptance.source_version` 与之一致。

## 边界

- 本补记不表示候选已写入 `04-knowledge/`；全部候选仍为 `needs_evidence` / `decision.status=pending`（1 个去重 `rejected`）。
- 未做图版逐张视觉核验；未做外部书目或实物核对；OCR 异文按原文保留。
- 未 commit、未 push；未创建分支或 worktree；来源文件未改写。
- 本补记不构成写入、提交或推送授权。
