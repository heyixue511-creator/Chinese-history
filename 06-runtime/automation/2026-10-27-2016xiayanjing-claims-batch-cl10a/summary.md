# 夏燕靖 2016 升级版 claim 批次 CL10a（年表、文献索引与后记 18 条）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl10a/`
- 来源：夏燕靖《中国艺术设计史（升级版）》（2016，上海人民美术出版社），doc_id `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade`
- 候选范围：该册书末三段的 18 条 claim 候选——当代中国工艺美术、艺术设计大事年表（L5545-L6110，8 条）、中国古典设计文献索引（L6111-L6349，8 条）、后记（L6479-L6538，2 条）
- 背景：CL9a 完成后 `04-knowledge/quality/claim-registry.yml` 为 378 条；本批是该册最后一批 claim 候选，接续编号至 393
- 裁定结果：新建 15 条 claim；3 条并入 2009 版既有 claim 并补 `corroborating_spans`；无同义合并入新建 claim、无 rejected、无 no_delta；18 条候选全部 terminal
- 状态：18 条候选均 `state: applied`；`target_ref` 指向 `claim/claim-0379` 至 `claim/claim-0393` 及 3 条既有 claim
- 册级进度：夏燕靖 2016 册 254 条 claim 候选全部处理完毕（253 applied、1 no_delta），剩余 0 条 needs_evidence

## 2. 来源与复读范围

- 来源文件共 6538 行，UTF-8 无 BOM、LF；本批只读，不改写。
- 本批复读三块书末材料：
  - 大事年表 L5545-L6110：标题“当代中国工艺美术、艺术设计大事年表（1949-2000）”与 1949-2000 各年小节；本批只取 1957、1983、1994、1998、1999、2000 六个年份小节。
  - 中国古典设计文献索引 L6111-L6349：从《周易》到《丝绣笔记》共 60 余条；本批只取《周易》《考工记》《墨子·节用》《唐六典》《天工开物》《长物志》《髹饰录》《清工部工程做法》八条。
  - 后记 L6479-L6538：含修订缘起、五方面修订说明、致谢与 2013 年省级重点立项教材说明；正文至 L6505 署名与日期，L6507 起为 PDF 元数据，不属于正文。
- 18 条候选包围跨度去重后 15 个，合计 907 行；其中 5641-5656 与 6009-6018 各含 2 条候选，6479-6538 含 2 条后记候选。关键行已逐句复读，年份标题行与文献条目标题行纳入 `key_lines`，使年份/书名可直接从跨度复核。
- 未读部分：年表未列入本批的其余年份条目、文献索引其余条目、参考书目 L6351-L6477 未逐条建候选；图版未逐张视觉核验。

**来源完整性提示**：

- L5647 记 1957 年 7 月 22 日全国工艺美术艺人代表会议；田自秉 2010 记“1958 年，举行首次全国艺人代表会议”，相差一年，事件 KU 已并存两说。
- L5651 称南京市云锦研究所为“新中国第一家工艺美术研究机构”；L5194 称 1954 年云锦研究工作组为“新中国建立初期最早的工艺美术研究机构”，两处“最早/第一家”比较对象与范围不同，来源未作机构普查。
- L6013 称全国技术美学研讨会为“美学第一次对艺术设计进行理论思考的专题研讨会”，未给“第一次”的比较依据。
- L6017 的 1994 年成衣出口统计来自纺织工业部，未给统计口径与商品分类范围。
- L6087 只记 1999 年合并日期与结果，未记合并方案与院系调整。
- L6093 只记 2000 年初建成，未给大道名称、长度、起止与设计单位。
- L6115、L6237、L6245、L6249 的文献评价均为作者判断；《髹饰录》“现存唯一”、《天工开物》“第一部”未给普查与命名依据。
- L6333 作“宋代李诚”，同一索引 L6197 作“李诫”，两处不一致；本条照录 L6333 并在 notes 记录，不据 L6197 改写。
- L6489 与 L6501 为作者自述的修订与立项事实，无外部文件可核。

## 3. 裁定结果

| 处置 | 候选数 | claim 行 |
|---|---:|---:|
| 新建（主候选） | 15 | 15 |
| 并入新建 claim（同义重复） | 0 | 0 |
| 并入 2009 版既有 claim | 3 | 0 |
| rejected | 0 | 0 |
| no_delta | 0 | 0 |
| 合计 | 18 | 15 |

- 候选编号：`cand-10-61`、`10-62`、`10-63`、`10-64`、`10-65`、`cand-11-99`、`11-100`、`11-101`、`11-102`、`11-103`、`11-104`、`11-105`、`11-106`、`11-107`、`11-108`、`11-109`、`11-110`、`11-111`。
- 新建主候选：`cand-10-62`、`10-63`、`10-65`、`cand-11-100`、`11-101`、`11-102`、`11-103`、`11-104`、`11-105`、`11-106`、`11-107`、`11-108`、`11-109`、`11-110`、`11-111`，分别对应 `claim-0379` 至 `claim-0393`。
- 并入既有 claim 的 3 条候选均为 2009 版同义断言：`cand-10-64` → `claim-0255`、`cand-10-61` → `claim-0256`、`cand-11-99` → `claim-0257`；只补 `merged_candidate_ids` 与 `corroborating_spans`，不重复建条。

## 4. 新建 15 条

- `claim-0379` 至 `claim-0393`，ID 连续，无空号。
- 类型：historiographic 5（`0379`、`0380`、`0384`、`0387`、`0391`）、evaluative 3（`0381`、`0388`、`0390`）、factual 5（`0382`、`0383`、`0385`、`0392`、`0393`）、interpretive 2（`0386`、`0389`）。
- 置信度：medium 15、high 0、low 0。
- 跨度类型：bounded 15。
- 章节归属：附录 13（年表 5 条、文献索引 8 条）、后记 2。
- 全部 15 条含 `statement_zh`、`statement_en`、`source.doc_id`、`source.source_span`、`consensus: tentative`、`review_status: source_backed`。
- 15 条全部有 `supported_by`；共 22 条链接，覆盖 21 个不同 KU 路径（publications 11 条链接/10 个路径、events 3、terms 3、institutions 2、places 2、persons 1）。
- 代表条目：
  - `claim-0379`：1957 年 7 月 22 日全国工艺美术艺人代表会议在北京举行，提出“保护、发展和提高”方针与“适用、经济、美观”生产原则，为第二个五年计划指明方向，historiographic，L5647。
  - `claim-0380`：1957 年 7 月江苏省人民政府批准建立南京市云锦研究所，这是新中国第一家工艺美术研究机构，historiographic，L5651。
  - `claim-0381`：1994 年 10 月下旬全国技术美学研讨会在天津举行，作者称这是美学第一次对艺术设计进行理论思考的专题研讨会，evaluative，L6013。
  - `claim-0382`：1999 年 11 月 20 日中央工艺美术学院与清华大学合并，成立清华大学美术学院，factual，L6087。
  - `claim-0383`：2000 年初上海建成中国第一条生态景观大道，是上海迎接新世纪的标志性工程，factual，L6093。
  - `claim-0384`：《周易》的设计思想主要体现在“道”与“器”的关系上，成为传统造物思想与设计方法亘古不变的主题，historiographic，L6115。
  - `claim-0385`：《考工记》所记工艺分 6 大类 30 个工种，涉及制车、兵器、礼器、钟磬、练染、建筑、水利等，并及天文、生物、数学、物理、化学，factual，L6119。
  - `claim-0386`：《墨子·节用》包含墨子的工艺思想，强调“节用”当为制造日用器物的原则和要求，interpretive，L6149。
  - `claim-0387`：《唐六典》全称《大唐六典》，是唐代行政法典，也是我国最早的行政法典，historiographic，L6185。
  - `claim-0388`：《天工开物》较完整记载明朝中叶以前的生产技术，被称之为世界上第一部关于农业和手工业生产的综合性著作，evaluative，L6237。
  - `claim-0389`：《长物志》始终贯穿“以用为本”的思想，其价值体现为一种物质的实用性，interpretive，L6245。
  - `claim-0390`：明代黄成所撰《髹饰录》是我国现存唯一的古代漆工专著，evaluative，L6249。
  - `claim-0391`：清雍正十二年（1734）清工部颁布《工程做法》74 卷；作者认为它与宋代李诚《营造法式》是我国古代官方颁布建筑标准的仅有两部古籍，historiographic，L6333。
  - `claim-0392`：后记说明本次修订在第一章、第五章、第六章、第九章、第十一章各增一节（原始农业生产器具设计、漆工艺的发展与特色漆器品种、唐代设计理论述要、明清贸易瓷的历史演变与特色、社会主义建设时期的工业产品设计），factual，L6489。
  - `claim-0393`：后记说明本教材于 2013 年 10 月获江苏省级重点立项教材，并推荐为全省高校设计专业用书，factual，L6501。

## 5. 判重、合并与支持链接

- 跨版判重：3 条 2016 候选与 2009 版既有 claim 同义，未重复建条，改为在既有 claim 的 `source.merged_candidate_ids` 补 2016 候选编号，并在 `source.corroborating_spans` 补 2016 来源跨度。
  - `cand-10-64` → `claim-0255`（L5843-L5858，关键行 L5843、L5845，1983 年 1 月《工艺美术参考》转向工业设计教育文论并引发讨论）
  - `cand-10-61` → `claim-0256`（L6009-L6018，关键行 L6009、L6017，1994 年底成衣出口世界第一、232.7 亿美元）
  - `cand-11-99` → `claim-0257`（L6059-L6072，关键行 L6059、L6071，1998 年 7 月教育部专业目录改名）
- 同段近邻对读：
  - `cand-10-62`（1957 年艺人代表会议方针）与 `cand-10-63`（1957 年云锦研究所）同处 L5641-L5656：一为会议方针与意义判断、一为机构建立与“第一家”判断，分别建 `claim-0379`、`claim-0380`。
  - `cand-10-61`（成衣出口统计）与 `cand-10-65`（技术美学研讨会）同处 L6009-L6018：前者并入 `claim-0256`，后者为独立会议评价，建 `claim-0381`。
  - `cand-11-100`（院系合并）、`cand-11-101`（生态景观大道）分别落在 1999、2000 年小节，建 `claim-0382`、`claim-0383`。
  - `cand-11-102` 至 `11-109` 为文献索引八条，各自对应一部典籍，逐条建 claim，未互相合并。
  - `cand-11-110`（增补五节）与 `cand-11-111`（省级立项教材）同处后记，分别建 `claim-0392`、`claim-0393`。
- 链接原则：只链与该断言直接相关的 KU；`claim-0380` 3 条最多，`claim-0381`、`0382`、`0385`、`0387`、`0388`、`0389`、`0390`、`0392`、`0393` 各 1 条。`publications/zhongguo-yishu-shejishi-upgraded.md` 同时支撑两条后记 claim，是 22 条链接与 21 个路径差额的来源。
- 22 条 `supported_by` 经闭包投影为 claim 与 KU 之间的双向关系条目 44 条，与既有 1844 条合计 1888 条；这是生成态关系索引的增长，不是新增的编辑性 relation。
- 未新建或改动任何 KU 文件；未手工改动 `translation-index.yml`。

## 6. 语义判断与内部张力

- 类型映射：
  - `basic_fact` 3 条（`cand-11-100`、`11-101`、`11-103`）按语义映射为 factual_claim。
  - `bibliographic_fact` 2 条（`cand-11-110`、`11-111`）不在 claim registry 的六类之列，按语义映射为 factual_claim；两条记述的是修订与立项事实，不是书目类型断言。
  - `historiographic_claim` 5 条、`evaluative_claim` 3 条、`interpretive_claim` 2 条按候选原值写入。
- `claim-0380` 的“新中国第一家”与 `claim-0364` 的“新中国建立初期最早”是两个机构、两个比较范围：1954 年工作组与 1957 年研究所，本条在 notes 明确区分，不把两者合并为同一机构。
- `claim-0381` 的“第一次”、`claim-0388` 的“第一部”、`claim-0390` 的“唯一”、`claim-0391` 的“仅有的两部”均保留来源评价口吻，未补比较依据或改写为确定事实。
- `claim-0391` 照录 L6333 的“李诚”，不据 L6197 的“李诫”统一；异文写入 notes，留待后续裁决。
- 年表与文献索引 claim 的 `key_lines` 均含年份标题行或文献条目标题行，使年份与书名可从跨度直接复核；`statement_zh` 不依赖标题行也能独立成立。
- 单来源规则：15 条均为单来源，`consensus` 一律 tentative，`review_status` 一律 source_backed，不写 confirmed。
- 本批未建 evidence 记录，`supports` 为空；`source_span` 是当前可追溯证据，evidence 与 claim 互链留待 verify 阶段。

## 7. 跨批维护

- `04-knowledge/quality/claim-registry.yml`：709301 bytes 变为 735170 bytes；header 为 `# Claim Registry v1.0`、`# generated: 2026-10-27`、`# total: 393`。
- before hash `sha256:8b75909331ffab09f3375cffa256136c34fd991686a49f094fb5b5b6b8587193`；after hash `sha256:03ff421add5898095348dcf111e416cecb3efe76dd11e534a21a0d56c9f14d63`。
- 候选索引：5339 行不变；applied 3367→3385；needs_evidence 867→849；rejected 871；no_delta 234；active 849，terminal 4490。
- 18 条候选写入 `state: applied`、`lifecycle_class: terminal`、`decision.status: approved`、`decided_by: Agent`、`decided_at: 2026-10-27`。
- 夏燕靖 2016 册：254 条 claim 候选全部处理（253 applied、1 no_delta），剩余 0 条 needs_evidence；该册另有 957 条非 claim 候选已终止（656 applied、234 rejected、67 no_delta），不在本批范围。
- 全库 claim 候选债务：849 条，其中 2016 册 0、赵农 2009 376、田自秉 2010 278、李立新 2011 195。
- 关系索引：1844→1888 条，全部由 claim-registry 的 `supported_by` 投影生成；新增 44 条中 22 条为 claim→KU，22 条为 KU→claim。
- 未改动任何 KU 文件；未新增术语条；未手工改动 `translation-index.yml`。
- 包内工件：`manifest.json`、`claim-rows.jsonl`（15 行）、`claim-updates.jsonl`（3 行）、`apply-plan.jsonl`（18 行：15 create + 3 update）、`candidate-decision-ledger.jsonl`（18 行）、`canonical-mapping.json`（18 条）、`summary.md`。
- 未 commit、未 push。

## 8. 生成态与门禁

- 写回前校验：`_zn_cl13_preflight.py` 检查 registry 为 378 行、header 为 378、15 条新行 ID 连续、3 条 patch 目标均为 2009 版且无既有 `merged_candidate_ids`、18 条候选均为 needs_evidence 且类型为 claim、候选集合恰为 2016 册剩余 18 条、claim 与 patch 跨度及 block_ids 落在候选包围跨度内、关键行含年份/书名/数值关键词、`supported_by` 路径存在，结果 `remaining_2016 18`、`used_candidates 18`、`bad 0`。
- 首轮 preflight 曾报 10 条关键词缺失，原因是年份与书名位于小节标题行、`key_lines` 只取断言行；修正为把标题行纳入 `key_lines` 后全部通过，未改动断言文本。
- `_zn_cl13_apply.py` 再检查 baseline registry 为 378 行、header 为 378、写入后 YAML 可解析为 393 行、15 条新行 ID 连续、3 条既有 claim 的 2016 跨度可反查、18 条候选迁移计数一致（primary 15、merged_existing 3、merged_new 0）。
- 写回后检查：`_zn_cl13_verify.py` 验证 393 行、15 条新 claim 的类型/置信度/跨度类型/支持链接（22 条、21 个不同路径）、116 条含跨版本佐证的 claim（113 条存量 + 3 条本批）、3 条 CL10a patch 目标、18 条 applied 的 `target_ref`、2016 册剩余 0 条 needs_evidence、包内工件计数（15/3/18/18/18）与 manifest 一致。
- 完整闭包：`python scripts/run_sync_closure.py --refresh-generated --full` 18/18 通过，250 项测试与 16 项子测试通过。
- 健康快照：结构体检 104/130 不变；traceability 15/15；`rule_drift=0`；关系一致性 explicit 1888、inferred 0、weak evidence 0、missing inverse 0。
- claim 指标：total_claims 393、with_source 393、with_source_span 393、with_supported_by 374、with_supports 0、with_statement_en 393。
- 生成态：translation-index 2178 条不变；knowledge-graph-data 2566 个节点不变；evidence_quality 55/55；content_quality total_findings 20 不变（16 个空 frontmatter 值、1 个跨类型同名、3 个 placeholder），均为本批之前的存量项。
- 运行索引：本摘要写入并刷新后自动化目录为 888 个 R1 provenance 文件、174 个批次目录，字节数与摘要索引见 `06-runtime/automation/index.md`。
- 发布门禁：`python scripts/run_sync_closure.py --refresh-generated --full --check-generated` 在 check generated snapshots 步骤失败（exit=1）；生成态文件相对 HEAD 有差异，原因是工作树内未提交批次累积，不是本批写入错误。状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。

## 9. 未决事项

- `claim-0379` 的会议年份与田自秉 2010 的“1958 年”相差一年，缺会议文件与主办机关。
- `claim-0380` 的“第一家”缺全国机构普查依据，且与 `claim-0364` 的“最早”比较范围不同。
- `claim-0381` 的“第一次”缺主办单位、参会人数、论文篇目与比较依据。
- `claim-0382` 缺合并方案、院系调整与后续建制；清华大学机构 KU 尚未建立。
- `claim-0383` 缺大道名称、长度、起止与设计单位。
- `claim-0384` 缺《周易》出处篇目与注家。
- `claim-0385` 的 6 大类 30 工种未展开分类名目与原文依据。
- `claim-0386` 未引《墨子·节用》成句。
- `claim-0387` 的“最早行政法典”缺比较范围。
- `claim-0388` 的“第一部”缺提出者与比较依据。
- `claim-0389` 的“以用为本”未指出自哪一卷。
- `claim-0390` 的“现存唯一”缺普查依据。
- `claim-0391` 的“李诚/李诫”异文未统一，“仅有的两部”缺书目普查依据。
- `claim-0392`、`claim-0393` 为作者自述的修订与立项事实，缺外部文件与立项文号。
- 3 条并入 claim 的 2016 佐证同样缺量化材料：`claim-0255` 缺期刊期数与讨论范围，`claim-0256` 缺统计口径，`claim-0257` 缺专业目录原文。
- evidence 层未建：393 条 claim 的 `supports` 仍为 0，尚无 evidence JSONL；verify 阶段的 claim-evidence 互链尚未执行。
- 无 commit、无 push；registry、候选索引与生成态改动留在工作树，等待用户明确授权。

## 10. 下一跳

- 夏燕靖 2016 册 claim 候选已全部关闭（254 条：253 applied、1 no_delta）；该册的 claim 层工作完成。
- 下一册进入赵农 2009（376 条 claim 候选）。
- 之后依次处理田自秉 2010（278 条）、李立新 2011（195 条），完成前六本的 claim 层。
- 每批继续先与 2009 版及同书前版逐条对读：能合并的补 `corroborating_spans` 或并列来源，不重复建条；新增断言再建新 claim。
- 每批结束重建 discovery 与 health，并记录 claim registry 总行数、supported_by 比例、candidate 状态迁移与关系索引投影增量。
- 全库 claim 完成后，再进入 evidence 层、relation 层与 hierarchy 补全。
