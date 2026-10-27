# 夏燕靖 2016 升级版 claim 批次 CL6a（元代章 17 条）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl6a/`
- 来源：夏燕靖《中国艺术设计史（升级版）》（2016，上海人民美术出版社），doc_id `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade`
- 候选范围：该册第 8 章“元代的设计交融”的 17 条 claim 候选，对应正文 L3595-L4110
- 分节候选分布：知识链接（取消科举制）1、瓷器工艺与设计 4、染织工艺及其品种设计 3、金属工艺及品种设计特色 3、农业器具与天文器具的设计记载 1、建筑与装饰纹样设计 2、印刷、家具与商业美术 3
- 背景：CL5a 完成后 `04-knowledge/quality/claim-registry.yml` 为 337 条；本批接续编号并继续与 2009 版逐条对读
- 裁定结果：新建 8 条 claim；9 条并入 2009 版既有 claim 并补 `corroborating_spans`；无同义合并入新建 claim、无 rejected、无 no_delta；17 条候选全部 terminal
- 状态：17 条候选均 `state: applied`；`target_ref` 指向 `claim/claim-0338` 至 `claim/claim-0345` 及 9 条既有 claim
- 册级进度：夏燕靖 2016 册已处理 181 条 claim 候选（180 applied、1 no_delta），剩余 73 条 needs_evidence

## 2. 来源与复读范围

- 来源文件共 6538 行，UTF-8 无 BOM、LF；本批只读，不改写。
- 本批复读第 8 章 L3595-L4110（516 行）；L4081-L4106 为练习思考题，本批无候选，未逐条重读；L4107 起为第 9 章，不属于本章。
- 章内结构：章标题与导论 L3595-L3606；1. 瓷器工艺与设计 L3607-L3704（知识链接：元朝制度形态 L3613-L3617、取消科举制 L3619-L3621；1）元代名窑 L3630-L3649；2）元代瓷器的造型特色 L3651-L3690；知识链接：元代青花瓷、《饮流斋说瓷》、影青瓷、鬼谷下山青花罐 L3659-L3681；3）元代瓷器的装饰风格 L3692-L3704）；2. 染织工艺及其品种设计 L3706-L3784（知识链接：元代釉里红瓷 L3716-L3720；1）丝织工艺和织金锦工艺 L3728-L3744；知识链接：元代丝织纹样特色、黄道婆、《碎金》 L3736-L3770；2）棉织工艺与印染工艺 L3746-L3784）；3. 服饰工艺与服饰设计 L3786-L3859（1）男子服饰的形制 L3790-L3820、2）顾姑冠与女服款式 L3822-L3859）；知识链接：古代铜产量与金属制器 L3843-L3847、元代兵器 L3849-L3851；4. 金属工艺及品种设计特色 L3861-L3895（1）金属工艺的继承与发展 L3865-L3869、2）金属工艺中的精制品种 L3871-L3895、知识链接：朱碧山 L3887-L3891）；5. 农业器具与天文器具的设计记载 L3897-L3950（1）王祯《农书》和秧马记载 L3901-L3926、知识链接：王祯《农书》L3915-L3919、2）郭守敬发明的天文简仪 L3928-L3950）；6. 建筑与装饰纹样设计 L3952-L4006（1）民族文化的渗透与交流 L3958-L3994、知识链接：元大都城规划、《经世大典》 L3973-L3981、2）元代建筑装饰纹样的构成特色 L4000-L4006）；7. 印刷、家具与商业美术 L4008-L4079（知识链接：王祯与印刷术 L4021-L4025、1）印刷业与印刷工艺 L4042-L4046、2) 家具及制作工艺 L4048-L4054、知识链接：马可·波罗与《马可·波罗游记》 L4062-L4066、3）商业的繁荣与商业美术 L4068-L4079）；练习思考题 L4081-L4106。
- 17 条候选包围跨度合计 182 行，去重后 14 个不同跨度、147 行；新建 claim 引用跨度合计 8 行，去重后 8 个不同跨度；9 条并入跨度合计 9 行，去重后 9 个不同跨度。候选跨度与关键行均已复读，包含章首、知识链接框、图注边界与各小节标题。
- 图版未逐张视觉核验；图注只在候选包围跨度内读取。练习思考题与第 9 章未逐条核对。

**来源完整性提示**：

- L3597 把元朝分为两阶段并称其为疆域广阔的王朝、第一个由少数民族建立的大一统帝国，未给疆域面积、人口或政区数据。
- L3599 称元代整体生产力不如宋朝，未给产量、耕地或财政的量化比较。
- L3621 以取消科举解释民间工艺发达，未给士人数量、行业分布或工艺产量数据。
- L3636 的元钧与宋钧比较以《饮流斋说瓷》与故宫藏品对照为据，未给釉料化验、窑址统计或断代序列。
- L3708 以建康路东织染局一局数据推及“一个新的高峰”，未给全国织造总量或与宋、明的比较。
- L3730 称黄道婆改进具有重大历史意义，未给棉布产量、纺车效率或织户数量统计。
- L3847 的元代铜产量“百万斤”未给出处、统计口径与年度序列；唐代至宋代的对比数字同缺出处。
- L3869 称兵器制造技术有较大提高，未给兵器产量、工场数量或技术指标。
- L3926 的秧马“插秧和拔秧综合器具”是作者针对学界“仅用于插秧”说提出的判断，未给考古实物或推广范围统计。
- L3954 的“600多年”与 L3977 的“完全符合”“严格按照”为概括性判断，未给纪年序列、《周礼·考工记》原文比对或考古实测。
- L4077 称商业美术促进了商业发展，未给商号数量、广告支出或销售增长数据。

## 3. 裁定结果

| 处置 | 候选数 | claim 行 |
|---|---:|---:|
| 新建（主候选） | 8 | 8 |
| 并入新建 claim（同义重复） | 0 | 0 |
| 并入 2009 版既有 claim | 9 | 0 |
| rejected | 0 | 0 |
| no_delta | 0 | 0 |
| 合计 | 17 | 8 |

- 候选编号：`cand-06-75`、`06-76`、`07-64`、`07-63`、`07-65`、`07-66`、`07-67`、`07-68`、`07-96`、`07-98`、`07-99`、`07-73`、`07-69`、`07-70`、`07-91`、`07-71`、`07-92`。
- 新建主候选：`cand-07-64`、`07-66`、`07-67`、`07-96`、`07-99`、`07-69`、`07-70`、`07-92`，分别对应 `claim-0338` 至 `claim-0345`。
- 9 条并入既有 claim 的候选均为 2009 版同义或近义断言，只补 `merged_candidate_ids` 与 `corroborating_spans`，不重复建条；本批每条既有 claim 各接收 1 条候选。

## 4. 新建 8 条

- `claim-0338` 至 `claim-0345`，ID 连续，无空号。
- 类型：interpretive 3（`0340`、`0344`、`0345`）、factual 2（`0341`、`0342`）、historiographic 2（`0339`、`0343`）、evaluative 1（`0338`）。
- 置信度：medium 8、high 0、low 0。
- 跨度类型：line 8（各条均为单行断言）。
- 全部 8 条含 `statement_zh`、`statement_en`、`source.doc_id`、`source.source_span`、`consensus: tentative`、`review_status: source_backed`。
- 8 条均有 `supported_by`；共 20 条链接，覆盖 17 个不同 KU 路径（`works/yuan-huoqiang.md`、`procedures/jintong-fa.md` 各支撑 2 条，`places/yuan-dadu.md` 支撑 2 条）；按链接计 works 5、institutions 3、terms 3、places 3、publications 3、persons 1、procedures 1。
- 代表条目：
  - `claim-0338`：元代钧瓷能有意识地使蓝紫两种釉料分别聚散成形、掌握釉料变化并提高烧造技术，是元代钧窑的进步；但釉质粗糙、胎骨笨厚，不及宋钧精细，evaluative，L3636。
  - `claim-0339`：为满足贵族统治者奢华生活需要，官府投入极大精力经营染织业，同时使元代染织工艺水平达到一个新的高峰，historiographic，L3708。
  - `claim-0340`：黄道婆对棉纺织工具和技术的改进具有重大历史意义，推动长江下游棉纺织业发展；从此棉织与丝织并列，成为我国纺织业的两大体系，interpretive，L3730。
  - `claim-0341`：元代铜器制作虽呈萎缩趋势，但铜的年产量仍维持在百万斤的水平，factual，L3847。
  - `claim-0342`：元代兵器工业是优先发展的行业；灭南宋后朝廷从组织管理机构方面予以保证并对制造技术进行督导，兵器制造技术因此有较大提高，factual，L3869。
  - `claim-0343`：元大都是自唐都长安以来又一个规模巨大而有完整规划的都城，并为明清两代继承，奠定以后 600 多年以北京为政治中心的统一国家都城局面，historiographic，L3954。
  - `claim-0344`：元大都总体布局符合我国古代传统文化地理观念，严格按《易经》思想指导下的《周礼·考工记》规划，充分体现“周王礼制”的国都规划制度，interpretive，L3977。
  - `claim-0345`：元代商业美术设计作为促销手段之一，确实为商业的发展起到了促进作用，interpretive，L4077。

## 5. 判重、合并与支持链接

- 跨版判重：9 条 2016 候选与 2009 版既有 claim 同义或近义，未重复建条，改为在既有 claim 的 `source.merged_candidate_ids` 补 2016 候选编号，并在 `source.corroborating_spans` 补 2016 来源跨度。
  - `cand-06-75` → `claim-0197`（L3619-L3629，关键行 L3621，取消科举与士人流入市井）
  - `cand-06-76` → `claim-0198`（L3619-L3629，关键行 L3628，青花、釉里红与釉下彩新阶段）
  - `cand-07-63` → `claim-0200`（L3651-L3660，关键行 L3653，元瓷造型硕大、胎骨厚重）
  - `cand-07-65` → `claim-0202`（L3692-L3705，关键行 L3694，划花主流与明清彩绘先声）
  - `cand-07-68` → `claim-0206`（L3728-L3745，关键行 L3744，加金织物兴盛的黄金来源）
  - `cand-07-98` → `claim-0209`（L3865-L3870，关键行 L3867，宋元金属工艺相互联系而有发展）
  - `cand-07-73` → `claim-0211`（L3915-L3927，关键行 L3926，秧马为插秧与拔秧综合器具）
  - `cand-07-91` → `claim-0216`（L4008-L4020，关键行 L4010，锡质活字与木质活字用于刻书）
  - `cand-07-71` → `claim-0218`（L4048-L4061，关键行 L4054，元代家具三点风格判断）
- 同章近邻对读：
  - `cand-06-75` 与 `cand-06-76` 共享 L3619-L3629 跨度，但一为科举废止、一为青花釉里红，分别并入 `claim-0197`、`claim-0198`，彼此不合并。
  - `cand-07-64`（元钧评价）独立建条；`cand-07-63`（造型总述）、`cand-07-65`（装饰方法）分别并入 `claim-0200`、`claim-0202`，三者在同章但对象不同。
  - `cand-07-66`（染织新高峰）、`cand-07-67`（黄道婆与棉丝并列）独立建条；`cand-07-68`（加金织物原因）并入 `claim-0206`。2009 版 `claim-0204` 只记官营染织规模，未含“新高峰”评价，故不合并。
  - `cand-07-96`（铜产量百万斤）、`cand-07-99`（兵器工业）独立建条；`cand-07-98`（宋元金属工艺总体）并入 `claim-0209`。2009 版 `claim-0209` 的 notes 明确把铜产量数据留在来源，`claim-0210` 只记浸铜法，故二者另立。
  - `cand-07-69`（元大都历史地位）、`cand-07-70`（元大都规划思想）分属城市史分期与规划观念，分别建条，不互相合并；2009 版 `claim-0213` 只记“上承宋辽金、下启明清”的总体分期。
  - `cand-07-91`（印刷）、`cand-07-71`（家具）并入 2009 版既有 claim；`cand-07-92`（商业美术的促销功能）独立建条，2009 版 `claim-0219` 只记商业美术的发展与市肆规制，未含因果功能判断。
- 链接原则：只链与该断言直接相关的 KU；`claim-0339`、`0340`、`0342`、`0344` 各 3 条，其余各 2 条；`places/jun-kiln.md`、`persons/huang-daopo.md`、`places/yuan-dadu.md`、`publications/kaogongji.md`、`works/yuan-huoqiang.md` 为本批核心锚点。
- 20 条 `supported_by` 经闭包投影为 claim 与 KU 之间的双向关系条目 40 条，与既有 1676 条合计 1716 条；这是生成态关系索引的增长，不是新增的编辑性 relation。
- 未新建或改动任何 KU 文件；未手工改动 `translation-index.yml`。

## 6. 语义判断与内部张力

- 类型映射：`claim-0339`（染织新高峰）、`0343`（元大都城市史地位）路由 historiographic；`claim-0338`（元钧进步与不足的双向评价）路由 evaluative；`claim-0340`（黄道婆改进的因果与棉丝并立）、`0344`（规划思想阐释）、`0345`（商业美术功能）路由 interpretive；`claim-0341`（铜产量）、`0342`（兵器工业组织与技术）按来源陈述路由 factual。
- `claim-0338` 保留“进步”与“不及宋钧精细”的双向判断，不补釉料化验与断代序列。
- `claim-0339` 保留官营染织与“新高峰”的因果评价，不把一局数据写成全国总量。
- `claim-0340` 保留黄道婆改进与棉丝两大体系的历史判断，不补产量与效率统计。
- `claim-0341` 只记元代百万斤的产量判断，唐代至宋代的对比序列留在来源，不写成统计表。
- `claim-0342` 保留机构保证、技术督导与“较大提高”的因果链，不补兵器产量或技术指标。
- `claim-0343`、`0344` 保留元大都的历史地位与规划思想阐释，不把“600多年”“完全符合”写成已证结论。
- `claim-0345` 保留促销功能的因果判断，不补商业数据；同段的“装点门面”仍由 `claim-0219` 承载。
- 单来源规则：8 条均为单来源，`consensus` 一律 tentative，`review_status` 一律 source_backed，不写 confirmed。
- 本批未建 evidence 记录，`supports` 为空；`source_span` 是当前可追溯证据，evidence 与 claim 互链留待 verify 阶段。

## 7. 跨批维护

- `04-knowledge/quality/claim-registry.yml`：617180 bytes 变为 635658 bytes；header 为 `# Claim Registry v1.0`、`# generated: 2026-10-27`、`# total: 345`。
- before hash `sha256:640302c213661bde5d5acc79cf4aa7f1bee9d66f430d3871f235039ee8f3ad0f`；after hash `sha256:1821a7b023efe1329ee830a60e990d6e18d59259e8088d600b7536ff687033c2`。
- 候选索引：5339 行不变；applied 3295→3312；needs_evidence 939→922；rejected 871；no_delta 234；active 922，terminal 4417。
- 17 条候选写入 `state: applied`、`lifecycle_class: terminal`、`decision.status: approved`、`decided_by: Agent`、`decided_at: 2026-10-27`。
- 夏燕靖 2016 册：254 条 claim 候选已处理 181 条（180 applied、1 no_delta），剩余 73 条 needs_evidence。
- 全库 claim 候选债务：922 条，其中 2016 册 73、赵农 2009 376、田自秉 2010 278、李立新 2011 195。
- 关系索引：1676→1716 条，全部由 claim-registry 的 `supported_by` 投影生成。
- 未改动任何 KU 文件；未新增术语条；未手工改动 `translation-index.yml`。
- 包内工件：`manifest.json`、`claim-rows.jsonl`（8 行）、`claim-updates.jsonl`（9 行）、`apply-plan.jsonl`（17 行：8 create + 9 update）、`candidate-decision-ledger.jsonl`（17 行）、`canonical-mapping.json`（17 条）、`summary.md`。
- 未 commit、未 push。

## 8. 生成态与门禁

- 写回前校验：`_zn_cl9_preflight.py` 检查 registry 为 337 行、header 为 337、8 条新行 ID 连续、9 条 patch 目标均为 2009 版且无既有 `merged_candidate_ids`、17 条候选均为 needs_evidence 且类型为 claim、第 8 章 L3595-L4110 范围内恰为 17 条候选、claim 与 patch 跨度及 block_ids 落在候选包围跨度内、关键行含预期关键词、`supported_by` 路径存在，结果 `chapter_candidates 17`、`used_candidates 17`、`bad 0`。
- `_zn_cl9_apply.py` 再检查 baseline registry 为 337 行、header 为 337、写入后 YAML 可解析为 345 行、8 条新行 ID 连续、9 条既有 claim 的 2016 跨度可反查、17 条候选迁移计数一致（primary 8、merged_existing 9、merged_new 0）。
- 写回后检查：`_zn_cl9_verify.py` 验证 345 行、8 条新 claim 的类型/置信度/跨度类型/支持链接（20 条、17 个不同路径）、91 条含跨版本佐证的 claim（82 条存量 + 9 条本批）、9 条 CL6a patch 目标、9 条合并跨度、17 条 applied 的 `target_ref`、2016 册剩余 73 条 needs_evidence、包内工件计数（8/9/17/17/17）与 manifest 一致。
- 完整闭包：`python scripts/run_sync_closure.py --refresh-generated --full` 18/18 通过，250 项测试与 16 项子测试通过。
- 健康快照：结构体检 104/130 不变；traceability 15/15；`rule_drift=0`；关系一致性 broken target 0、missing inverse 0、weak evidence 0。
- claim 指标：total_claims 345、with_source 345、with_source_span 345、with_supported_by 327、with_supports 0、with_statement_en 345。
- 生成态：translation-index 2178 条；knowledge-graph-data 2566 个节点；relation-candidates 排除正式 relation 后仍为 5 个 s7_name_overlap 候选（dry run）。
- 内容质量：`content_quality.total_findings=20` 不变（16 个空 frontmatter 值、1 个跨类型同名、3 个 placeholder），均为本批之前的存量项。
- 运行索引：本摘要写入并刷新后自动化目录为 860 个 R1 provenance 文件，字节数与摘要索引见 `06-runtime/automation/index.md`。
- 发布门禁：`python scripts/run_sync_closure.py --refresh-generated --full --check-generated` 在 check generated snapshots 步骤失败（exit=1）；11 个生成态文件相对 HEAD 有差异，原因是工作树内未提交批次累积，不是本批写入错误。状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。

## 9. 未决事项

- `claim-0338` 的元钧与宋钧比较缺釉料化验、窑址统计与断代序列；《饮流斋说瓷》的记载范围与故宫藏品对照样本未展开。
- `claim-0339` 的“新高峰”由建康路东织染局一局数据推及，缺全国织造总量与宋、明比较。
- `claim-0340` 的黄道婆改进缺棉布产量、纺车效率与织户数量统计；三锭脚踏纺棉车的技术细节留在知识链接。
- `claim-0341` 的百万斤缺出处、统计口径与年度序列；唐代至宋代的对比数字同缺出处。
- `claim-0342` 的兵器工业缺产量、工场数量与技术指标；“优先发展”的判断需兵工史复核。
- `claim-0343`、`0344` 的“600多年”“完全符合”“严格按照”缺纪年序列、原文比对与考古实测。
- `claim-0345` 的促销功能缺商业数据；招牌、店匾与陈列各自的效果未分。
- 来源排录异常：L3597、L3599、L3621、L3636、L3708、L3730、L3847、L3869、L3926、L3954、L3977、L4077，均已在对应 claim 的 notes 记录。
- 跨版判重尚未完成：2016 册其余 73 条候选仍需与 2009 版 claim 逐条比对，优先合并并补 `corroborating_spans`，不重复建条。
- evidence 层未建：345 条 claim 的 `supports` 仍为 0，尚无 evidence JSONL；verify 阶段的 claim-evidence 互链尚未执行。
- 无 commit、无 push；registry、候选索引与生成态改动留在工作树，等待用户明确授权。

## 10. 下一跳

- 夏燕靖 2016 册下一批进入明清时期的设计渐变章（21 条 claim 候选，L4111 起）。
- 后续按章推进：近现代 12、新中国 22、年表 16、后记 2。
- 每批继续先与 2009 版逐条对读：能合并的补 `corroborating_spans` 或并列来源，不重复建条；新增断言再建新 claim。
- 2016 册完成后，依次处理赵农 2009 376 条、田自秉 2010 278 条、李立新 2011 195 条。
- 每批结束重建 discovery 与 health，并记录 claim registry 总行数、supported_by 比例、candidate 状态迁移与关系索引投影增量。
- 全库 claim 完成后，再进入 evidence 层、relation 层与 hierarchy 补全。
