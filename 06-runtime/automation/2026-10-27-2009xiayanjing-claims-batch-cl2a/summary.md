# 夏燕靖 2009 册 claim 批次 CL2a（33 条候选）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2009xiayanjing-claims-batch-cl2a/`
- 来源：夏燕靖《中国设计史》（2009，上海人民美术出版社），doc_id `2009-xiayanjing-zhongguo-shejishi`
- 候选范围：该册 223 条 claim 候选中的前 33 条，位于序言、原始社会的艺术设计、夏商周时期的艺术设计三章（L66-L766；春秋战国章自 L787 起）
- 分章候选数：序言 4、原始社会 11、夏商周 18
- 背景：`04-knowledge/quality/claim-registry.yml` 已有高丰 2004 册 36 条 claim（`claim-0001` 至 `claim-0036`），本批接续编号
- 裁定结果：新建 33 条 claim，33 条候选全部 applied；合并 0、rejected 0、no_delta 0
- 状态：33 条候选均为 terminal，`target_ref` 指向 `claim/claim-0037` 至 `claim/claim-0069`

## 2. 来源与复读范围

- 来源文件共 5409 行，UTF-8 无 BOM、LF；本批只读，不改写。
- 33 条候选的包围跨度合计 349 行，去重后 300 个源行；实际复读 336 个唯一源行，含候选跨度外的必要上下文。
- 复读集中：
  - 序言 L64-L81（编写宗旨、设计史与工艺美术史的分野、现当代叙述范围）。
  - 原始社会 L228-L237、L260-L279、L298-L307、L327-L346、L389-L436（设计起源、石器二次加工与磨制、陶器设计特点、舞蹈纹盆、纺编织物、居住雏形）。
  - 夏商周 L459-L500、L533-L582、L648-L687、L694-L771（夏朝国家形态、青铜时代年代、礼制与风格、陶器与原始瓷、车船、建筑与城建、丝织与深衣）。
- 未复读春秋战国及以后章节；图像、图注、脚注与参考文献未在本批逐条核对。

## 3. 裁定结果

| 处置 | 候选数 | claim 行 |
|---|---:|---:|
| 新建 | 33 | 33 |
| 同义合并 | 0 | 0 |
| rejected | 0 | 0 |
| no_delta | 0 | 0 |
| 合计 | 33 | 33 |

候选分组：`cand-01` 33 条，按章为序言 4、原始社会 11、夏商周 18。

## 4. 新建 33 条

- `claim-0037` 至 `claim-0069`，ID 连续，无空号。
- 类型：historiographic 10、interpretive 16、factual 7；evaluative 0、synthetic 0、contested 0。
- 置信度：high 21、medium 12、low 0。
- 跨度类型：line 32、bounded 1（`claim-0058`，L548-L556）、contiguous 0。
- 全部 33 条含 `statement_zh`、`statement_en`、`source.doc_id`、`source.source_span`、`consensus: tentative`、`review_status: source_backed`。
- 33 条均有 `supported_by`，共 55 条链接，覆盖 41 个不同 KU 路径；按链接计 terms 41、procedures 5、works 2、places 3、events 2、persons 1、institutions 1。
- 代表条目：
  - `claim-0037`：摆脱工艺美术史叙事、以艺术设计眼光重述造物历程，historiographic，L68。
  - `claim-0038`：设计史与工艺美术史的最大区别在设计与功能对工艺与欣赏，historiographic，L70。
  - `claim-0040`：设计史取材以生产生活器具与环境建筑为重点，不重点列入陈设欣赏工艺品，historiographic，L70。
  - `claim-0046`：舞蹈纹彩陶盆纹样五说并存，historiographic，L342。
  - `claim-0052`：夏朝为中国文明史开端并由原始社会进入奴隶社会，historiographic，L461。
  - `claim-0056`：《周礼》九鼎等级与“藏礼于器”，factual，L538。
  - `claim-0058`：殷商青铜器审美追求强烈而标准不一，interpretive，L548-L556。
  - `claim-0062`：中国至迟在商代中期已发明瓷器，historiographic，L678。
  - `claim-0069`：周代深衣制及其在近现代服装中的延续，interpretive，L750。

## 5. 判重、合并与支持链接

- 本批无同义合并。序言 L66-L73 同一 block 产生 4 条 claim，但分别对应研究方法、学科分野、现当代叙述重点、取材范围，语义不重复。
- 跨册不做合并：高丰 2004 的 `claim-0001` 与夏燕靖 2009 的 `claim-0037`、`claim-0038` 都讨论设计史与工艺美术史的分野，但作者与版本不同，保留为独立断言；跨版判重留待夏燕靖 2016 批次。
- 链接原则：只链直接承载该断言的 KU；宏观分期与整体评价类断言挂接相应 term，不强行补齐。55 条链接中，`yishu-shejishi` 与 `qingtong-liqi` 各被引用 4 次，`gongyi-meishu` 3 次。
- `cand-01-04` 与 `cand-01-92` 的 `claim_scope` 为 `definition`，本批按内容判为学科对象与取材范围问题，路由 `historiographic_claim`；这是对 CL1“definition 默认按 interpretive 处理”的窄幅偏离，已在第六节说明，未新建 term。
- 55 条 `supported_by` 经闭包投影为 claim 与 KU 之间的双向关系条目 110 条，与 CL1 的 52 条合计 162 条；这是生成态关系索引的增长，不是新增的编辑性 relation。

## 6. 语义判断与内部张力

- 类型映射：interpretation 路由 interpretive；periodization 路由 historiographic；basic_fact、attribution 路由 factual；definition 仅在涉及学科对象与取材范围时路由 historiographic，其余仍按 interpretive 处理。
- 断言主语保留来源归属：`statement_zh` 统一以“夏燕靖认为”“夏燕靖把”“夏燕靖据”“夏燕靖引”起句，factual 条目也不改写成无主语的客观事实。
- 不确定状态保留：`claim-0041` 保留“朦胧、不自觉”的限定；`claim-0045` 保留尖底瓶力学解释“只是一种看法，仍有待查考”；`claim-0046` 并列五说而不判定唯一解释。
- 区分转引与作者判断：`claim-0063` 把《尚书·甘誓》的誓师词与《吕氏春秋·简读》的“良车七十乘”分开归属；`claim-0048` 把《易·繫辞篇》原文与夏燕靖的“统治方式”解释分开；`claim-0056`、`claim-0060` 的《周礼》《左传》引文与作者概括保持距离。
- 跨册术语张力：高丰 `claim-0009` 把“真正瓷器”定在东汉，夏燕靖 `claim-0062` 称“至迟商代中期已发明瓷器”，但同段随即称其为“原始瓷”“原始青瓷”。两者是“瓷器”与“真正瓷器/原始瓷”的术语层次差异，不构成直接矛盾；本批不合并，留待 evidence 或 reconcile 阶段并置。
- 单来源规则：33 条均为单来源，`consensus` 一律 tentative，`review_status` 一律 source_backed，不写 confirmed。
- 本批未建 evidence 记录，`supports` 为空；`source_span` 是当前可追溯证据，evidence 与 claim 互链留待 verify 阶段。
- 未新建术语条；`definition` 候选若确需术语定义，应回流 ingest，不在 claim 层留替身。

## 7. 跨批维护

- `04-knowledge/quality/claim-registry.yml`：54097 bytes 变为 102064 bytes；header 为 `# Claim Registry v1.0`、`# generated: 2026-10-27`、`# total: 69`。
- before hash `sha256:83236e8122d8e711992d9c7abcb7de040909c8ee213f03c74b2a83a4bef28375`；after hash `sha256:7f209f047b0238e629039324d191732437f81a28b154107c8e9a2be9b32b99b6`。
- 候选索引：5339 行不变；applied 2909→2942；needs_evidence 1326→1293；rejected 871；no_delta 233；active 1326→1293，terminal 4013→4046。
- 33 条候选写入 `state: applied`、`target_ref: claim/claim-00XX`、`lifecycle_class: terminal`、`decision.status: approved`、`decided_by: Agent`、`decided_at: 2026-10-27`。
- 未改动任何 KU 文件；未新增术语条；未手工改动 `translation-index.yml`（闭包重建后仍为 2178 entries）。
- 包内工件：`manifest.json`、`claim-rows.jsonl`（33 行）、`apply-plan.jsonl`（33 行）、`candidate-decision-ledger.jsonl`（33 行）、`canonical-mapping.json`（33 条）、`summary.md`。
- 未 commit、未 push。

## 8. 生成态与门禁

- 写回前校验：`_zn_claim_xyj09a_build.py` 检查 33 条 ID 唯一、claim_type 词表、中英文非空、中文无双引号、doc_id 与 source_file、跨度边界、key_lines 落在跨度内、supported_by 路径存在；`_zn_claim_xyj09a_apply.py` 再检查 baseline registry 为 36 行、header 为 36、33 条候选均为 needs_evidence 且类型为 claim、claim 跨度落在候选包围跨度内、写入后 YAML 可解析为 69 行、旧 36 行未变、新 33 行 ID 连续。
- 写回后检查：`claim-registry.yml` 可解析 69 行，`audit_rule_drift.check_claim_registry_header` 无 `claim_registry_total_mismatch`；33 条候选全部 applied，无残留 needs_evidence。
- 完整闭包：`python scripts/run_sync_closure.py --refresh-generated --full` 18/18 通过，250 项测试与 16 项子测试通过。
- 健康快照：结构体检 103/130 → 104/130；traceability 14/15 → 15/15；`rule_drift=0`。
- claim 指标：total_claims 69、with_source 69、with_source_span 69、with_supported_by 54、with_supports 0、with_statement_en 69。
- 关系索引：52 → 162 条，全部由 claim-registry 的 `supported_by` 投影生成（81 条链接的双向条目），不是新增编辑性关系。
- 内容质量：`content_quality_findings=20` 不变（16 个空 frontmatter 值、1 个跨类型同名、3 个 placeholder），均为本批之前的存量项。
- 候选债务：1326 → 1293 条 claim 候选，全部为 needs_evidence。
- 运行索引：批次目录 152 → 153 个，文件 744 → 750 个。
- 发布门禁：`python scripts/run_sync_closure.py --refresh-generated --full --check-generated` 在 `[17/19] check generated snapshots` 失败（exit=1）；11 个生成态文件相对 HEAD 有差异，原因是工作树内未提交批次累积，不是本批写入错误。状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。
- 闭包运行期间出现一次子进程 stderr 的 GBK 解码告警（UnicodeDecodeError in reader thread），相关步骤仍返回成功，未影响 18/18 结果；属于 Windows 终端编码问题，不是知识写回失败。

## 9. 未决事项

- 夏燕靖 2009 册剩余 190 条 claim 候选：春秋战国 33、秦汉 12、魏晋南北朝 17、隋唐五代 34、宋辽金西夏 29、元代 25、明清 18、近现代 9、新中国 11、后记 2。
- 全库剩余 1293 条 claim 候选：赵农 2009 376、田自秉 2010 278、夏燕靖 2016 254、夏燕靖 2009 190、李立新 2011 195。
- 跨版判重：夏燕靖 2009 与 2016 两版可能大量近义断言，需在 2016 批次逐条比对 2009 的 claim，优先合并并补 `corroborating_spans`，不重复建条。
- 跨册术语张力：`claim-0009`（东汉真正瓷器）与 `claim-0062`（商代中期瓷器/原始瓷）需在 evidence 或 reconcile 阶段并置，当前不合并、不改写。
- evidence 层未建：69 条 claim 的 `supports` 仍为 0，尚无 evidence JSONL；verify 阶段的 claim-evidence 互链尚未执行。
- `cand-01-04`、`cand-01-92` 的 definition 路由已作窄幅偏离；后续 definition 候选仍需逐条判定，避免把一般定义误标为史学断言。
- 无 commit、无 push；registry、候选索引与生成态改动留在工作树，等待用户明确授权。

## 10. 下一跳

- 下一批 CL2b：夏燕靖 2009 春秋战国章 33 条 claim 候选（L787-L1278），沿用 CL2a 的 build、validate、exact change-set apply 流程。
- 随后按章推进：秦汉 12、魏晋南北朝 17、隋唐五代 34、宋辽金西夏 29、元代 25、明清 18、近现代 9、新中国 11、后记 2。
- 夏燕靖 2009 完成后进入 2016 版（254 条），先与 2009 版逐条对读，能合并的补 `corroborating_spans` 或并列来源，不重复建条。
- 每批结束重建 discovery 与 health，并记录 claim registry 总行数、supported_by 比例、candidate 状态迁移与关系索引投影增量。
- 全库 claim 完成后，再进入 relation 层与 hierarchy 补全。
