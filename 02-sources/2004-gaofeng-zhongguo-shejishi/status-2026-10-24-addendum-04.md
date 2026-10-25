# 处理状态记录补编 04（2026-10-24）

- **doc_id**：`2004-gaofeng-zhongguo-shejishi`
- **记录性质**：追加状态说明；不修改 `source-record.md`、`source-record-addendum-01.md`、`status-2026-10-24.md` 及其补编 01–03。
- **处理包**：`03-processing/2004-gaofeng-zhongguo-shejishi/`
- **处理 profile**：`compact-v4`
- **当前状态**：`completed`

## 本轮完成的变化

- 七块独立语义复读全部完成，总体 `accepted_with_findings`：28 处遗漏、18 条准确性 findings、8 条类型 findings（7 个唯一候选）、3 条覆盖映射 findings。
- 已补立 28 个语义单元与 43 个候选，全部保持 `needs_evidence`、`decision.status=pending`；未裁决、未写入 `04-knowledge/`。
- 已修正 `b0083`、`b0277`、`b0291` 的块级 provenance，并回挂相应语义单元与候选。
- 复读报告中的 chunk-01 `b0039`/`su-01-34` 覆盖问题不适用于本书：本书 `b0039` 为 L963–993，`su-01-34` 为 L915–930 的居住单元，L388 属 `b0016`；按误报处理，未改动。
- 类型修正：`cand-01-03` 《考工记》及 `cand-06-02/04/06/09/11` 由 `work` 改为 `publication`；`cand-01-04` 百工制度由 `institution` 改为 `term`。
- 四组独立增量复读覆盖全部 28 个补立单元与 43 个补立候选；28/28 遗漏逐项确认闭合，无 `blocking`。
- 四组增量复读共 17 条 minor；16 条已修正，1 条保留：候选层 `claim_scope` 沿用包内简写 `interpretation`/`periodization`，与 `claim-evidence-governance.md` 的 `*_claim` 正式枚举存在映射差异，写回 KU 时统一映射，本轮不单点改写既有 claim 候选。
- 复读包提出的“联珠纹、雕漆、吉祥图案及《长物志》《髹饰录》《天工开物》无独立候选”经核对为包外既有候选：`cand-04-09`、`cand-05-12`、`cand-07-02`、`cand-06-04`、`cand-06-09`、`cand-06-11`；未重复立目。

## 最终计数

- semantic units：303。
- candidates：223（unit 186，claim 37），全部 `needs_evidence`。
- 按 unit_type：`{"institution": 14, "person": 27, "place": 5, "procedure": 9, "publication": 19, "term": 68, "work": 44}`。
- 覆盖：308/308 个 source block，5582/5582 行；未读 0，无候选且无排除理由的块 0。

## 验收字段

`manifest.json` 已写入：

- `reread_status`：`accepted_with_findings`
- `reviewer_kind`：`agent`
- `reviewer_id`：`independent-seven-chunk-review+four-delta-reviews-2026-10-24`
- `reviewed_at`：`2026-10-24T20:25:00+08:00`
- `source_version`：`sha256:b3295895271742bbb175b0063f43b594dbd97344e02f15fd985ea9e87e55b177`
- `omission_count`：0（首轮 28 处已全部闭合）
- `acceptance_boundary`：见 `manifest.json`；只覆盖原文语义召回与复读状态，不证明候选已写入 `04-knowledge/`，不证明事实经外部核实，也不声称已逐张视觉核验图版。

## 机械校验

- `python scripts/validate_processing_package.py 03-processing/2004-gaofeng-zhongguo-shejishi` 返回 `valid: true`，`issues: []`。
- `source-map.jsonl`、`semantic-units.jsonl`、`candidate-ledger.jsonl`、`summary.md` 的输出哈希已按当前内容重算并写入 `manifest.json`。

## 边界

- `completed` 只表示摄入、语义复读与增量复读流程闭合；不表示学术验收通过，不表示候选已裁决或写入知识库。
- 随书图版 476 张，本次仅抽查 3 张；其余未逐张视觉核验，图版判断仅依据图注与正文。
- 未 commit、未 push，未创建分支或 worktree；来源文件未改写，`02-sources/` 既有记录未修改。
- 书目 `_catalog.md` 的 `status` 未由本记录改动。
- 本记录不构成写入、提交或推送授权；`status-2026-10-24.md` 及补编 01–03 中“仍为 running”的表述，以本补编为准。
