# 来源状态更新记录：2026-10-24

本文件按 `_catalog.md` 规则 4「只追加、不改写」新增，用于记录 2026-10-24 前六本处理后的来源状态推进。`_catalog.md` 表格中的 `registered` 保留为登记时快照，不静默覆盖；状态以本记录与各书 `status-*.md` 为准。

## 状态推进

| doc_id | 书名 | 处理包状态 | 语义验收 | 更新依据 |
|---|---|---|---|---|
| `2004-gaofeng-zhongguo-shejishi` | 中国设计史（高丰） | `completed` | `accepted_with_findings` | `03-processing/2004-gaofeng-zhongguo-shejishi/manifest.json` |
| `2009-xiayanjing-zhongguo-shejishi` | 中国设计史（夏燕靖） | `completed` | `accepted_with_findings` | 同上 |
| `2009-zhaonong-zhongguo-yishu-shejishi` | 中国艺术设计史（赵农） | `completed` | `accepted_with_findings` | 同上 |
| `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade` | 中国艺术设计史（升级版） | `completed` | `accepted_with_findings` | 同上 |
| `2011-lilixin-zhongguo-sheji-yishu-shilun` | 中国设计艺术史论（李立新） | `completed` | `accepted_with_findings` | `02-sources/2011-lilixin-zhongguo-sheji-yishu-shilun/status-2026-10-24-addendum-01.md` |
| `2010-tianzibing-zhongguo-gongyi-meishushi` | 中国工艺美术史（修订本）（田自秉） | `completed` | `accepted_with_findings` | `02-sources/2010-tianzibing-zhongguo-gongyi-meishushi/status-2026-10-24-addendum-01.md` |

## 状态语义

- 对应 `_catalog.md` 规则 5 的 `processed`：处理包五件套已闭合，独立语义复读与去重复核完成，机械校验通过。
- **不等于 `verified`，更不等于知识成立**：六册全部候选仍为 `needs_evidence` / `decision.status=pending`，未走 `collect -> evidence JSONL -> apply` 写回，`04-knowledge/` 未新增任何内容。
- 其余 18 册保持 `registered`，未启动摄入。

## 边界

- 本记录只追加，不改写 `_catalog.md` 既有行。
- 未 commit、未 push；未创建分支或 worktree。
