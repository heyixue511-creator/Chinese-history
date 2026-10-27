# 赵农 2009《中国艺术设计史》claim 批次 zn1a（序言与导论 10 条）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2009zhaonong-claims-batch-zn1a/`
- 来源：赵农《中国艺术设计史》（2009，高等教育出版社），doc_id `2009-zhaonong-zhongguo-yishu-shejishi`
- 候选范围：序言 L84-L110 的 2 条 claim 候选（`cand-01-03`、`cand-01-04`）与导论 L280-L357 的 8 条 claim 候选（`cand-01-05`、`01-07`、`01-08`、`01-10`、`01-11`、`01-63`、`01-64`、`01-65`），共 10 条
- 背景：CL10a 完成后 `04-knowledge/quality/claim-registry.yml` 为 393 条；赵农册 376 条 claim 候选此前全部为 `needs_evidence`，本批是该册第一批写回
- 裁定结果：新建 10 条 claim（`claim-0394` 至 `claim-0403`）；无同义合并入新建 claim、无并入既有 claim、无 rejected、无 no_delta；10 条候选全部 terminal
- 状态：10 条候选均 `state: applied`，`target_ref` 指向 `claim/claim-0394` 至 `claim/claim-0403`
- 册级进度：赵农册 376 条 claim 候选已处理 10 条，剩余 366 条 `needs_evidence`

## 2. 来源与复读范围

- 来源文件共 8800 行，UTF-8 无 BOM、LF；本批只读，不改写。
- 本批复读两段：
  - 序言 L84-L110：L84 标题，L86-L106 正文，L108 署名，L110 日期“2008年9月9日于风物长宜之轩”。正文含作者自述 1999 年开始写作、宋代以后沈括等五人的努力因专制社会限制而被扼杀、中国古代艺术设计是农耕文明下的文化现象、本次教材重新编定章节四层内容。
  - 导论 L280-L357：含设计史研究对象、文化冲撞融合论、复古鼎新、Design 译名序列、工艺美术史研究局限、使用价值与适用观念、22 位设计家、十阶段分期、何尊与“中国”词义演变。
- 10 条候选的语义行去重后为 10 个单行：L96、L100、L286、L302、L304、L312、L318、L337、L339、L343。候选信封中序言两条的包围跨度为 L18-L111（block `b0003`），本批把 `source_span` 收窄到实际断言所在的 L96、L100，并在 notes 说明；block 归属仍为 `b0003`。
- 未读部分：封面、目录图版与书内插图未逐张视觉核验；导论中未立项的段落只作上下文复读，不建候选。

**来源张力提示**：

- L286 以“两种以上的文明”概括文化进步条件，未给“文明”的界定、比较样本与“欧洲大陆历史”的具体所指。
- L304 的 Design 译名序列未给出处、提倡者与年代边界；“失去了本质的文化意义”是作者判断。
- L312 对既有工艺美术史研究的三点批评未列具体著作与作者。
- L337 列 22 人，第 22 人原文作“庞薰栗”，与通行写法“庞薰琹”不一致；第 17 人“黄成”与人物 KU 的“黄大成”亦不一致。本批只订正“庞薰栗”并记异体，其余照录。
- L339 的十阶段是作者分期方案，未给分期标准与断代依据。
- L343 的“最早出现”未给何尊铭文拓本、器号与著录。
- L96 的“农耕文明”未给时间边界，“积极作用”未给评估标准。

## 3. 裁定结果

| 处置 | 候选数 | claim 行 |
|---|---:|---:|
| 新建（主候选） | 10 | 10 |
| 并入新建 claim（同义重复） | 0 | 0 |
| 并入既有 claim | 0 | 0 |
| rejected | 0 | 0 |
| no_delta | 0 | 0 |
| 合计 | 10 | 10 |

- 候选编号：`cand-01-03`、`01-04`、`01-05`、`01-07`、`01-08`、`01-10`、`01-11`、`01-63`、`01-64`、`01-65`，与 `claim-0394` 至 `claim-0403` 一一对应。

## 4. 新建 10 条

- `claim-0394` 至 `claim-0403`，ID 连续，无空号。
- 类型：historiographic 8（`0394`、`0395`、`0396`、`0399`、`0400`、`0401`、`0402`、`0403`）、factual 1（`0397`）、evaluative 1（`0398`）。
- 置信度：medium 10、high 0、low 0。
- 跨度类型：line 10（10 条均为单行断言）。
- 章节归属：序言 2（`0402`、`0403`）、导论 8（`0394` 至 `0401`）。
- 10 条全部含 `statement_zh`、`statement_en`、`source.doc_id`、`source.source_span`、`consensus: tentative`、`review_status: source_backed`。
- 代表条目：
  - `claim-0394`：任何一种文化的进步必须有两种以上文明经过冲撞、磨擦、融合；中华民族每一回冲撞的结果没有使中原汉文化灭亡，而是更强大、更具包容性，historiographic，L286。
  - `claim-0395`：Design 在 20 世纪初期被译为“图案”，转而为“美术工艺”“实用美术”“工艺美术”；因战乱与经济落后，工艺美术局限于实用美术，设计仅成一种手法并失去本质的文化意义，historiographic，L304。
  - `claim-0396`：中国艺术设计史按时代分为石器、商周、春秋战国、秦汉、三国两晋南北朝、隋唐、五代两宋、辽金西夏元、明清、现代十个阶段，本书以下分十章论述，historiographic，L339。
  - `claim-0397`：现存古籍文献中最早出现“中国”一词的是西周早期青铜器何尊，铭文为周成王训词，已有“中央”“京师”概念，factual，L343。
  - `claim-0398`：鲁班、李冰、李斯、程邈、赵过、丁缓、张衡、马钧、阎立德、窦师伦、李诫、毕昇、王祯、黄道婆、宋应星、计成、黄成、李渔、詹天佑、梁思成、陈之佛、庞薰琹等是一流的设计家，贡献出杰出智慧，evaluative，L337。
  - `claim-0399`：中国艺术设计史研究是经历西学东渐诸多回合后寻找中国文化底蕴的复古鼎新思路，也是对现代设计中模糊地域特征与民族文化现象的拨正，historiographic，L302。
  - `claim-0400`：以往工艺美术史多研究图案、装饰，古代研究局限于生活必需品或材料工艺阐释；西方现代设计文化的引进隔离了工艺与设计，当代社会转型导致工艺美术转型与设计文化勃兴，historiographic，L312。
  - `claim-0401`：器具的使用价值是决定设计发展变化的重要因素；中国古代设计观念首先不是用风格制定器物样式，而是用适用观念完善器物功能，historiographic，L318。
  - `claim-0402`：宋代以后沈括、毕昇、王祯、徐光启、宋应星等不断努力，但这种几乎与欧洲文艺复兴同步的个人化努力因专制社会限制几乎被扼杀，historiographic，L100。
  - `claim-0403`：中国古代艺术设计可以说是在农耕文明下形成的文化现象，对满足当时社会生活的物质和精神需要起到积极作用，historiographic，L96。

## 5. 判重、合并与支持链接

- 判重：10 条候选逐条与既有 393 条 claim 对读，未发现同义断言，全部新建；本批无 `merged_candidate_ids`、无 `corroborating_spans`。
- 同段近邻对读：
  - 序言 `cand-01-03`（五人努力被扼杀）与 `cand-01-04`（农耕文明文化现象）同处 L96-L100，一为历史归因、一为性质判断，分别建 `claim-0402`、`claim-0403`。
  - 导论 `cand-01-05`（文化冲撞融合）与 `cand-01-63`（复古鼎新）分处 L286、L302，均属研究取向与历史判断，但论题不同，未合并。
  - `cand-01-07`（Design 译名）与 `cand-01-64`（工艺美术史局限）都涉及工艺美术范畴，前者为译名与学科史，后者为研究范围批评，分别建条。
  - `cand-01-10`（何尊）与 `cand-01-11`（22 位设计家）同处导论末段，一为器物实证、一为人物评价，类型不同，未合并。
- 链接原则：只链与断言直接相关的 KU。17 条 `supported_by` 覆盖 14 个不同路径：
  - 人物 12 条链接 / 11 个路径：`claim-0398` 7 条（公输般、李冰、张衡、黄道婆、宋应星、梁思成、庞薰琹），`claim-0402` 5 条（沈括、毕昇、王祯、徐光启、宋应星）；`song-yingxing` 同时支撑两条 claim，是链接数与路径数差额的来源。
  - 器物 1 条：`claim-0397` → `works/he-zun`。
  - 术语 4 条 / 2 个路径：`claim-0395`、`claim-0400` 各链 `terms/gongyi-meishu` 与 `terms/yishu-sheji`。
  - `claim-0394`、`0396`、`0399`、`0401`、`0403` 为无直接 KU 可链的历史判断，`supported_by` 为空。
- 17 条 `supported_by` 经闭包投影为 claim 与 KU 之间的双向关系条目 34 条，与既有 1888 条合计 1922 条；这是生成态关系索引的增长，不是新增的编辑性 relation。
- 未新建或改动任何 KU 文件；未手工改动 `translation-index.yml`。

## 6. 语义判断与内部张力

- 类型映射：9 条候选原值为 `historiographic_claim`，按原值写入；`cand-01-10` 原值为 `basic_fact`，按语义映射为 `factual_claim`。`claim-0398` 原值为 `evaluative_claim`，照写。
- `claim-0398` 的 22 人名单按原文顺序照录；仅把第 22 人“庞薰栗”订正为“庞薰琹”，异体与订正理由写入 `discussion_notes`；第 17 人“黄成”与 KU“黄大成”的差异保留在 notes，未据 KU 改写原文。
- `claim-0396` 的十阶段是作者的分期方案，`statement_zh` 用“按时代划分为”，未写成唯一分期；notes 保留“来源未给分期标准与断代依据”。
- `claim-0397` 的“最早”保留来源的比较口吻，未补全国青铜器铭文普查；notes 明示缺拓本、器号与著录。
- `claim-0402` 的“几乎与欧洲文艺复兴同步”“专制社会的限制”“几乎被扼杀”均按作者判断保留，未改写为已证史实。
- `claim-0403` 保留“可以说”的限定语气；`claim-0394` 保留“必须有两种以上的文明”的规范性表述，二者均不升级为确定事实。
- 单来源规则：10 条均为单来源，`consensus` 一律 tentative，`review_status` 一律 source_backed，不写 confirmed。
- 本批未建 evidence 记录，`supports` 为空；`source_span` 是当前可追溯证据，evidence 与 claim 互链留待 verify 阶段。

## 7. 跨批维护

- `04-knowledge/quality/claim-registry.yml`：735170 bytes 变为 751582 bytes；header 为 `# Claim Registry v1.0`、`# generated: 2026-10-27`、`# total: 403`。
- before hash `sha256:03ff421add5898095348dcf111e416cecb3efe76dd11e534a21a0d56c9f14d63`；after hash `sha256:9f7e005b21e584855039e728c86cc1454563ddd3c38ab00820a5c68f699f041a`。
- 候选索引：5339 行不变；applied 3385→3395；needs_evidence 849→839；rejected 871；no_delta 234；terminal 4490→4500，active 839。
- 10 条候选写入 `state: applied`、`lifecycle_class: terminal`、`decision.status: approved`、`decided_by: Agent`、`decided_at: 2026-10-27`。
- 赵农册：claim 候选 376→366 条 needs_evidence；该册全部候选 applied 1052、needs 366、rejected 227、no_delta 51。
- 全库 claim 候选债务：839 条，其中赵农 366、田自秉 278、李立新 195。
- 关系索引：1888→1922 条，全部由 claim-registry 的 `supported_by` 投影生成；新增 34 条中 17 条为 claim→KU，17 条为 KU→claim。
- 未改动任何 KU 文件；未新增术语条；未手工改动 `translation-index.yml`。
- 包内工件：`manifest.json`、`claim-rows.jsonl`（10 行）、`claim-updates.jsonl`（0 行）、`apply-plan.jsonl`（10 行 create）、`candidate-decision-ledger.jsonl`（10 行）、`canonical-mapping.json`（10 条）、`summary.md`。
- 未 commit、未 push。

## 8. 生成态与门禁

- 写回前校验：`_zn_generic_preflight.py` 读取 `_zn_batch_config.json`，检查 registry 为 393 行、header 为 393、候选状态为 applied 3385 / needs 849 / no_delta 234 / rejected 871、10 条新行候选均为 needs_evidence 且类型为 claim、跨度落在 L18-L357、`key_lines` 落在跨度内、block 归属可反查、关键词逐条命中、`supported_by` 路径存在，并核对范围内 10 条 claim 候选与使用集合完全一致；结果 `claims 10`、`scope_claim_candidates 10`、`used 10`、`missing 0`、`extra 0`、`problem_count 0`。
- 首轮 preflight 报 1 条关键词缺失：`claim-0400` 配置写“生活必需品”，原文作“生活的必需品”；改配置后通过，未改断言文本。
- `_zn_generic_apply.py` 再检查 baseline、候选状态、跨度、YAML 可解析为 403 行；写回结果 `claim_rows_added 10`、`candidate_applied 10`、`registry_after_bytes 751582`、`support_links 17`、`distinct_support 14`。
- 写回后检查：`_zn_generic_verify.py` 验证 403 行、10 条新 claim 的类型/日期/来源/跨度、17 条链接与 14 个不同路径、候选状态 applied 3395 / needs 839、lifecycle terminal 4500 / active 839、赵农册 needs 366、claim 债务 839、包内工件计数（10/0/10/10/10）与 manifest 一致。
- 完整闭包：`python scripts/run_sync_closure.py --refresh-generated --full` 18/18 通过，250 项测试与 16 项子测试通过。
- 健康快照：结构体检 104/130 不变；traceability 15/15；`rule_drift=0`；关系一致性 explicit 1922、inferred 0、weak evidence 0、missing inverse 0。
- claim 指标：total_claims 403、with_source 403、with_source_span 403、with_supported_by 379、with_supports 0、with_statement_en 403。
- 生成态：translation-index 2178 条不变；knowledge-graph-data 2566 个节点不变；evidence_quality 55/55；content_quality total_findings 20 不变（16 个空 frontmatter 值、1 个跨类型同名、3 个 placeholder），均为本批之前的存量项。
- 运行索引：本批目录使自动化批次目录增至 175 个；摘要写入后再执行一次闭包刷新 `06-runtime/automation/index.md`。
- 发布门禁：`python scripts/run_sync_closure.py --refresh-generated --full --check-generated` 在 check generated snapshots 步骤失败（exit=1）；相对 HEAD 有 11 个生成态文件差异：relation-index、translation-index、05-outputs/index/index.md、knowledge-graph-data.js、knowledge-graph-data.json、automation/index.md、governance-backlog.md、candidate-index.jsonl、current-health.json、discovery-manifest.json、generated-projections-manifest.json。原因是工作树内未提交批次累积，不是本批写入错误。状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。

## 9. 未决事项

- `claim-0394` 的“两种以上的文明”缺“文明”界定、比较样本与欧洲史所指。
- `claim-0395` 的译名序列缺出处、提倡者与年代边界；“失去本质的文化意义”缺论证。
- `claim-0396` 的十阶段缺分期标准、断代依据与各期考古学文化对应。
- `claim-0397` 的“最早”缺何尊铭文拓本、器号、著录与比较范围。
- `claim-0398` 的 22 人仅列 7 个代表性 KU；其余 15 人未建链，人物生卒与身份未逐条核。
- `claim-0399` 的“西学东渐诸多回合”缺回合数、代表人物与著作。
- `claim-0400` 的三点批评缺具体著作、作者与统计；“转型”缺分期。
- `claim-0401` 的“使用价值”“适用观念”缺界定与器物样本。
- `claim-0402` 的“与欧洲文艺复兴同步”“几乎被扼杀”缺比较依据与具体事件。
- `claim-0403` 的“农耕文明”缺时间边界，“积极作用”缺评估标准。
- evidence 层未建：403 条 claim 的 `supports` 仍为 0，尚无 evidence JSONL；verify 阶段的 claim-evidence 互链尚未执行。
- 无 commit、无 push；registry、候选索引与生成态改动留在工作树，等待用户明确授权。

## 10. 下一跳

- 赵农册下一批：第一章（L358-L1037）26 条 claim 候选，拟编号 `zn1b`，claim 从 `claim-0404` 起。
- 之后按章推进：第二章 41、第三章 30、第四章 24、第五章 28、第六章 54、第七章 55、第八章 19、第九章 31、第十章 52、总结 4、后记 2。
- 赵农册完成后处理田自秉 2010（278 条）与李立新 2011（195 条）。
