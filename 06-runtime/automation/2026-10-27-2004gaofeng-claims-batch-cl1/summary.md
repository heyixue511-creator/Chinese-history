# 高丰 2004 册 claim 批次 CL1（37 条候选）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2004gaofeng-claims-batch-cl1/`
- 来源：高丰《中国设计史》（2004，广西美术出版社），doc_id `2004-gaofeng-zhongguo-shejishi`
- 候选范围：该册全部 37 条 claim 候选，来自 `06-runtime/state/candidate-index.jsonl`
- 背景：`04-knowledge/quality/claim-registry.yml` 此前为空 `[]`，本批是全库第一条 claim 写回链路的试点
- 裁定结果：新建 36 条 claim，37 条候选全部 applied；1 条同义合并；rejected 0、no_delta 0
- 状态：37 条候选均为 terminal，`target_ref` 指向 `claim/claim-00XX`

## 2. 来源与复读范围

- 来源文件共 5240 行，UTF-8 无 BOM、LF；本批只读，不改写。
- 37 条候选的原始包围跨度合计 982 行；其中 15 条为 bounded 跨度，未逐行通读，只复读候选注明的关键句及其上下文。
- 实际复读 260 个唯一源行，集中在：
  - 序言 L120（张道一序）。
  - 绪论 L376-L522、L653-L655（设计史与工艺美术史的分野、汉字与平面设计、设计与科技）。
  - 第一章 L863-L897（大汶口陶符与汉字起源）。
  - 第三章 L1403-L1405、L1657-L1659（春秋战国青铜器第二高峰、战国漆器包装）。
  - 第四章 L1829-L1899、L2001-L2013、L2153-L2171、L2266-L2293、L2373-L2379（秦汉手工业、汉代铜镜图案、青铜灯具、吉祥图案、瓷器发明、汉代家具）。
  - 第五章 L2532-L2567、L3065-L3071（唐代南青北白、家具由低型向高型过渡）。
  - 第六章 L3160-L3391、L3480-L3508、L3900-L3922（宋瓷黄金时代、青花与审美风尚、宋代家具）。
  - 第七章 L4150-L4155、L4451-L4460、L4652-L4724（明代瓷器高峰、明式家具、宋体字与线装书）。
  - 第八章 L4764-L4837、L5023-L5025、L5163（清代设计得失、清式家具、清代书籍装帧）。
  - 第九章 L5211-L5223（近代工业与洋货冲击）。
- 第二章无 claim 候选；其余正文、图版、脚注与参考文献未在本批复读。

## 3. 裁定结果

| 处置 | 候选数 | claim 行 |
|---|---:|---:|
| 新建 | 36 | 36 |
| 同义合并 | 1 | 并入 `claim-0005` |
| rejected | 0 | 0 |
| no_delta | 0 | 0 |
| 合计 | 37 | 36 |

候选分组：cand-01 7 条、cand-02 1 条（另一条并入 claim-0005）、cand-03 3 条、cand-04 3 条、cand-05 2 条、cand-06 5 条、cand-07 4 条、cand-sup 11 条。

## 4. 新建 36 条

- `claim-0001` 至 `claim-0036`，ID 连续，无空号。
- 类型：historiographic 16、interpretive 12、factual 4、evaluative 4；synthetic 0、contested 0。
- 置信度：high 27、medium 9、low 0。
- 跨度类型：line 13、contiguous 8、bounded 15。
- 全部 36 条含 `statement_zh`、`statement_en`、`source.doc_id`、`source.source_span`、`consensus: tentative`、`review_status: source_backed`。
- 21 条有 `supported_by`，覆盖 19 个不同 KU 路径，共 26 条链接；15 条无支持链接。
- 代表条目：
  - `claim-0001`：设计史与工艺美术史的分野，historiographic，L376-L378。
  - `claim-0005`：汉代第一个高峰、第一个黄金时代，合并 cand-01-18 与 cand-02-20。
  - `claim-0009`：真正瓷器发明定在东汉，书中叙述为东汉晚期，L2280-L2282。
  - `claim-0017`：从设计史看明代而非清代康雍乾是瓷器高峰，L4152。
  - `claim-0020`：宋体字于明代中叶定型，L4660-L4675。
  - `claim-0028`：张道一序言中造物与寓意关系的判断，L120。
  - `claim-0036`：郑观庆《盛世危言》洋货冲击记述，L5219。

## 5. 判重、合并与支持链接

- 唯一合并：cand-01-18（L400）与 cand-02-20（L1835）都称汉代为中国设计史的第一个高峰或第一个黄金时代，合并为 `claim-0005`；主跨度取 L400，L1835 记入 `corroborating_spans`，不重复建条。
- 其余候选与 claim 一一对应：35 条单候选加 1 组双候选合并，共 36 条 claim。
- 支持链接覆盖 19 个既有 KU：陶器、青铜礼器、青铜器、瓦当、铜镜、越窑、邢窑、高型家具、汉代家具、明式家具、清式家具、青花瓷、景德镇窑、宋体字、线装、雕漆、活字印刷、套色印刷、长信宫灯。
- 链接原则：只链直接承载该断言的 KU；宏观分期与整体评价类断言不强行挂接。
- 本批为单册，不做跨册判重；夏燕靖 2009 与 2016 两版的近义断言留待后续批次合并。

## 6. 语义判断与内部张力

- 类型映射：periodization 路由 historiographic；interpretation 路由 interpretive，谓词以价值判断为主时路由 evaluative；basic_fact、attribution、source_claim、bibliographic_fact 路由 factual；definition 候选按 interpretive 处理，不写成 term，也不新建术语条。
- 断言主语保留来源归属：`statement_zh` 统一以“高丰认为”“高丰把”“高丰引”起句，factual 条目也不改写成无主语的客观事实。
- `claim-0002` 保留原文“倾向于认为”的推测语气，confidence 取 medium。
- `claim-0009` 保留“定在东汉”与书中叙述“东汉晚期”的张力，不把二者抹平。
- `claim-0011` 区分雷圭元《中外图案装饰风格》的转引与高丰关于典型民族风格的引申。
- `claim-0028` 归张道一，不归高丰；序言作者与正文作者分开。
- `claim-0036` 原文作者名作“郑观庆”，通行为“郑观应”，照录并加注，不改原文。
- 单来源规则：36 条均为单来源，consensus 一律 tentative，review_status 一律 source_backed，不写 confirmed。
- 本批未建 evidence 记录，`supports` 为空；`source_span` 是当前可追溯证据，evidence 与 claim 互链留待 verify 阶段。

## 7. 跨批维护

- `04-knowledge/quality/claim-registry.yml`：53 bytes 的 `[]` 变为 54097 bytes；header 为 `# Claim Registry v1.0`、`# generated: 2026-10-27`、`# total: 36`。
- before hash `sha256:8b0b9000e7cb43774a26af96101c2f9f6b49a1e1ca9779975ac884bf462cf679`；after hash `sha256:83236e8122d8e711992d9c7abcb7de040909c8ee213f03c74b2a83a4bef28375`。
- 候选索引：5339 行不变；applied 2872→2909；needs_evidence 1363→1326；rejected 871；no_delta 233；active 1363→1326，terminal 3976→4013。
- 37 条候选写入 `state: applied`、`target_ref: claim/claim-00XX`、`lifecycle_class: terminal`、`decision.status: approved`、`decided_by: Agent`、`decided_at: 2026-10-27`。
- 未改动任何 KU 文件；未新增术语条；未改动 `translation-index.yml`。
- 包内工件：`manifest.json`、`claim-rows.jsonl`（36 行）、`apply-plan.jsonl`（36 行）、`candidate-decision-ledger.jsonl`（37 行）、`canonical-mapping.json`（37 条）、`summary.md`。
- 未 commit、未 push。

## 8. 生成态与门禁

- 写回前校验：`_zn_claim_gf_build.py` 对 36 条逐条检查 ID 唯一、claim_type 词表、中英文非空、中文无双引号、doc_id 与 source_file、跨度边界、key_lines 落在跨度内、claim 前缀、supported_by 路径存在；`_zn_claim_gf_apply.py` 再校验 registry 原为空、37 条候选均为 needs_evidence 且类型为 claim、写入后 header 计数为 36、YAML 可解析为 36 行。
- 写回后检查：`claim-registry.yml` 可解析 36 行，`audit_rule_drift.check_claim_registry_header` 无 `claim_registry_total_mismatch`；37 条候选全部 applied，无残留 needs_evidence。
- 完整闭包：`python scripts/run_sync_closure.py --refresh-generated --full` 18/18 通过，250 项测试与 16 项子测试通过。
- 健康快照：结构体检 96/130 → 101/130（claim 可追溯性 7/15 → 12/15，+5）；完整闭包重建 relation index 后为 103/130（traceability 14/15，另 +2 来自 52 条显式关系的证据覆盖）。本批 claim 相关增量为 +5，relation 增量为闭包重建既有关系索引所致，不全部计入本批。
- claim 指标：total_claims 36、with_source 36、with_source_span 36、with_supported_by 21、with_supports 0、with_statement_en 36。
- 内容质量：`content_quality_findings=20` 不变（16 个空 frontmatter 值、1 个跨类型同名、3 个 placeholder），均为本批之前的存量项；本批未改动 KU，未新增内容质量发现。
- 规则漂移：首轮闭包后 `current-health.json` 内嵌 `output_navigation_snapshot_stale` 仍以旧快照为期望值，二次闭包后归零；原因是 `write_current_health.py` 在同一次 `build_results` 中读取上一版 health 作为导航页期望值，存在一轮滞后。最终 `rule_drift=0`。
- 运行索引：`06-runtime/automation/index.md` 由 151 个批次目录、738 个文件变为 152 个目录、744 个文件；本包被计入快照，但 `Recent Batches` 只列 15 个按目录名排序的最新包，`2004...` 前缀不会出现在该列表。
- 发布门禁：`python scripts/run_sync_closure.py --refresh-generated --full --check-generated` 在 `[17/19] check generated snapshots` 失败，原因是工作树内未提交批次累积的生成态与 HEAD 不一致；状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。

## 9. 未决事项

- 高丰 2004 册 claim 候选清零：37 applied、0 needs_evidence。
- 全库剩余 1326 条 claim 候选：赵农 2009 376、田自秉 2010 278、夏燕靖 2016 254、夏燕靖 2009 223、李立新 2011 195。
- 跨版判重：夏燕靖 2009 与 2016 两版可能大量近义断言，需在 2016 批次逐条比对 2009 的 claim，优先合并并补 `corroborating_spans`，不重复建条。
- evidence 层未建：36 条 claim 的 `supports` 为空，尚无 evidence JSONL；verify 阶段的 claim-evidence 互链尚未执行。
- definition 类候选若确为术语定义，应回流 ingest 建 term KU；不得在 claim 层留下术语替身。
- 高丰册的 claim 类型分布中 historiographic 占 16 条，比例偏高；后续册需注意不要把一般史实误标为史学断言。
- 无 commit、无 push；registry、候选索引与生成态改动留在工作树，等待用户明确授权。

## 10. 下一跳

- 下一批 CL2：夏燕靖《中国设计史》（2009）223 条 claim 候选，沿用 CL1 的 build、validate、exact change-set apply 流程；先抽样 10 条校准类型与英文句式，再整册写回。
- 随后：夏燕靖 2016（254 条，与 2009 对读判重）、赵农 2009（376 条）、田自秉 2010（278 条）、李立新 2011（195 条）。
- 每批结束重建 discovery 与 health，并记录 claim registry 总行数、supported_by 比例、candidate 状态迁移。
- 全库 claim 完成后，再进入 relation 层与 hierarchy 补全。
