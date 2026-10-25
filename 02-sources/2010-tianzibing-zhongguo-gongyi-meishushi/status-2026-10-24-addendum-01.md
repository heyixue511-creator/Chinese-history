# 处理状态补记 01：中国工艺美术史（修订本）（田自秉，2010）

- **记录日期**：2026-10-24
- **doc_id**：`2010-tianzibing-zhongguo-gongyi-meishushi`
- **处理包**：`03-processing/2010-tianzibing-zhongguo-gongyi-meishushi/`
- **处理 profile**：`compact-v4`
- **当前状态**：`completed`（十四段独立复读、去重复核与修补已完成）

本文件是 `status-2026-10-24.md` 的追加补记；原状态文件保持只读，不改写。

## 补记原因

原状态记录停在“chunk-05 至 chunk-14 复读进行中、去重与最终验收未执行”。此后完成了：

- 14 个分块独立复读：13 个 `accepted_with_findings`，1 个 `needs_revision`（chunk-07）。chunk-07 修补后完成定向 delta 复评（`accepted_with_findings`，3 项：2 major、1 minor）。
- chunk-08 补入 9 个候选并更新 14 个候选、3 个单元、11 个块引用；chunk-11 的 5 个证据越界在应用阶段修正（cand-11-18、25、54、55、56），并保留修正记录。
- 按原文恢复 8 个“画象石/画象砖”标题（cand-07-28、29、31、32、33、34、65、66）。
- 跨类型裁决 5 组：越窑→`place`、辫绣→`procedure`、蜡缬→`procedure`、雕漆→`term`、磁州窑→`place`。
- 去重：初始 34 组、37 个折叠候选，1111 降至 1074；独立复核为 `needs_revision`（8 项：1 blocking、6 major、1 minor）。修补补并 6 个候选（越窑 cand-08-33，加 5 组图注/正文同器 work 重复：cand-01-09→03-09、01-11→03-30、01-12→05-01、01-15→05-08、01-17→05-11），最终 39 组、43 个折叠候选、1068 个候选。
- 合并后字段统一 42 处（22 period、5 name、2 title、11 definition、2 location）。
- 去重修补 delta 复评 `accepted_with_findings`，仅 1 项 minor（辅助审计记录未同步）；已更新 `cross-type-decisions.json`、`dedupe-log.json`、`equivalents-final.json` 与 `book6-dedupe-remediation-log.json`，并经同一复读代理只读复核确认 `resolved`。
- 收尾刷新 `summary.md`、`manifest.semantic_acceptance` 与 `output_hashes`，状态置为 `completed`。

## 最终计数

- source blocks：378；复读 378，未读 0；无候选且无理由块 0；复读范围 5738/5738 行。
- semantic units：504。
- candidates：1068（unit 790、claim 278）；状态全部 `needs_evidence`。
- unit_type 分布：event 32、institution 49、person 87、place 96、procedure 57、publication 34、term 256、work 179。
- 全部复读与复核发现合计 237 项（2 blocking、103 major、132 minor）：14 段初轮 225 项、chunk-07 delta 3 项、去重复核 8 项、去重修补 delta 1 项；2 项 blocking 均已修复并复评。

## 复核结果

- 机械审计：block 覆盖、未读、未知引用、span/evidence、引文与数字、重复 slug、非法 unit_type 均为 0 异常。
- `check_reverse_refs.py`：`ok=true`、`count=0`。
- 仓库校验：`python scripts/validate_processing_package.py "03-processing/2010-tianzibing-zhongguo-gongyi-meishushi"` 返回 `valid: true`、`issues: []`。
- `semantic_acceptance`：`reread_status=accepted_with_findings`、`reviewer_kind=agent`、`omission_count=0`、`source_version` 与聚合输入指纹一致。

## 指纹

- 聚合输入指纹：`sha256:b269d1519eecebb1c6450ece930da553c884b1ed31d09c300a61aefbc04a04c6`
- 来源聚合指纹未变；`semantic_acceptance.source_version` 与之一致。

## 边界

- 本补记不表示候选已写入 `04-knowledge/`；全部候选仍为 `needs_evidence` / `decision.status=pending`。
- 未做图版逐张视觉核验；图注只按文字处理；未做外部书目、窑址或实物核对；OCR 异文按原文保留。
- cand-05-01、cand-05-08、cand-05-11 的 `culture` 字段沿用出土地/墓葬信息，属已知字段语义限制，未计为事实错误。
- 未 commit、未 push；未创建分支或 worktree；来源文件未改写。
- 本补记不构成写入、提交或推送授权。
