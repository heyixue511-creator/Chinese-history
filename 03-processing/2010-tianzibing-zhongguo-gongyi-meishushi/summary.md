# 处理摘要：中国工艺美术史（修订本）（田自秉，2010）

- **doc_id**：`2010-tianzibing-zhongguo-gongyi-meishushi`
- **处理 profile**：`compact-v4`
- **来源**：`03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md`
- **输入指纹**：`sha256:b269d1519eecebb1c6450ece930da553c884b1ed31d09c300a61aefbc04a04c6`
- **状态**：`completed`（独立语义复读与去重复核完成；结论 `accepted_with_findings`）

## 覆盖

- source blocks：378，已读/已合并/已排除：378，未读：0
- 无候选且无排除理由的块：0
- 复读范围：5738/5738 行（`full_asset`，单一全文资产）
- semantic units：504
- candidates：1068（unit 790，claim 278）

## 候选分布

- 按状态：`{"needs_evidence": 1068}`
- 按类型：`{"claim": 278, "unit": 790}`
- 按 unit_type：`{"event": 32, "institution": 49, "person": 87, "place": 96, "procedure": 57, "publication": 34, "term": 256, "work": 179}`

## 复读与修订

- 14 个分块独立复读：13 个 `accepted_with_findings`，1 个 `needs_revision`（chunk-07）；初轮共 225 项发现（1 blocking、95 major、129 minor）。chunk-07 定向修补后 delta 复评 `accepted_with_findings`（3 项：2 major、1 minor），累计 228 项。
- chunk-08 补入 9 个候选并更新 14 个候选、3 个单元、11 个块引用；chunk-11 的 5 个证据越界在应用阶段修正（2010-tianzibing-zhongguo-gongyi-meishushi:cand-11-18、2010-tianzibing-zhongguo-gongyi-meishushi:cand-11-25、2010-tianzibing-zhongguo-gongyi-meishushi:cand-11-54、2010-tianzibing-zhongguo-gongyi-meishushi:cand-11-55、2010-tianzibing-zhongguo-gongyi-meishushi:cand-11-56），未新增知识判断。
- 去重：先按 34 组、37 个折叠候选由 1111 降至 1074；独立复核为 `needs_revision`，记录 8 项发现（1 blocking、6 major、1 minor）。修补后补并 6 个候选——越窑组补并 `2010-tianzibing-zhongguo-gongyi-meishushi:cand-08-33`，另并 5 组图注与正文同器 work 重复（2010-tianzibing-zhongguo-gongyi-meishushi:cand-01-09→2010-tianzibing-zhongguo-gongyi-meishushi:cand-03-09、2010-tianzibing-zhongguo-gongyi-meishushi:cand-01-11→2010-tianzibing-zhongguo-gongyi-meishushi:cand-03-30、2010-tianzibing-zhongguo-gongyi-meishushi:cand-01-12→2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-01、2010-tianzibing-zhongguo-gongyi-meishushi:cand-01-15→2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-08、2010-tianzibing-zhongguo-gongyi-meishushi:cand-01-17→2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-11）——最终为 39 组、43 个折叠候选、1068 个候选。
- 去重修补 delta 复评 `accepted_with_findings`，仅 1 项 minor（辅助审计记录未同步）；已把 `cross-type-decisions.json` 的辫绣 period 改为“战国至唐（原文称战国以来）”，并在 `dedupe-log.json` 保留历史快照、以 `equivalents-final.json` 和 `book6-dedupe-remediation-log.json` 续记最终 39 组/43 folds/1068。
- 跨类型裁决 5 组：越窑归 `place`（并入 2010-tianzibing-zhongguo-gongyi-meishushi:cand-08-33、2010-tianzibing-zhongguo-gongyi-meishushi:cand-09-35）、辫绣归 `procedure`（并入 2010-tianzibing-zhongguo-gongyi-meishushi:cand-07-13）、蜡缬归 `procedure`（并入 2010-tianzibing-zhongguo-gongyi-meishushi:cand-10-26、2010-tianzibing-zhongguo-gongyi-meishushi:cand-13-45）、雕漆归 `term`（并入 2010-tianzibing-zhongguo-gongyi-meishushi:cand-09-15、2010-tianzibing-zhongguo-gongyi-meishushi:cand-11-04）、磁州窑归 `place`（并入 2010-tianzibing-zhongguo-gongyi-meishushi:cand-13-49）。
- 合并后字段统一 42 处：22 个 period、5 个 name、2 个 title、11 个 definition、2 个 location；另按原文恢复 8 个“画象石/画象砖”标题（2010-tianzibing-zhongguo-gongyi-meishushi:cand-07-28、29、31、32、33、34、65、66）。
- 全部复读、去重复核与修补 delta 合计 237 项发现（2 blocking、103 major、132 minor）；2 项 blocking 均已修复并复评。
- 机械审计：block 覆盖、未读、未知引用、span/evidence、引文与数字、重复 slug、unit_type 均为 0 异常；`check_reverse_refs.py` 返回 `ok=true`、`count=0`。

## 边界

- 本包只处理前六本书目中的第 6 本；其余书目不在本轮范围。
- 图版未逐张视觉核验；图注只按文字处理。涉及彩版、插图的候选均已注明“图版未视觉核验”。
- OCR 异文按原文保留，未据外部版本校改；未做外部书目、窑址或实物核对。
- 全部候选保持 `needs_evidence` / `decision.status=pending`；未写入 `04-knowledge/`。
- 已知字段语义限制：2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-01、2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-08、2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-11 的 `culture` 字段沿用原文出土地/墓葬信息，delta 复读已提示但不计为事实错误，留待后续字段规范统一处理。
- 来源文件未改写；未 commit、未 push，未创建分支或 worktree。
