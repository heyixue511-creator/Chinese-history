# 第四批写回：跨三书 9 组 canonical 知识元

- 工作包：`06-runtime/automation/2026-10-25-three-book-canonical-units/`
- 状态：`applied`
- 日期：2026-10-25
- 范围：Books 1–6（前六本）；Book 7 及以后不启动

## 一、批次范围

从 `duplicate-groups.jsonl` 中筛出 `doc_count = 3` 的组，共 **103 组、309 条候选**。本批只取其中 institution／procedure／event 三类实体，共 **9 组、27 条候选**：

- 9 组在本批写回（27 条候选）；
- 余 94 组（282 条候选）属 person／place／publication／term／work，本批不处置，仍为 `needs_evidence`。

本批 9 组每组均为 `member_count = 3`，处置方式一致：1 条升为 canonical 并写回 KU，2 条转为 `rejected` 并注明并入目标。

组内 slug 写法有分歧而被判为同一实体的有 5 组：`xdup-0064`（`xingwenshu` / `xingwen-shu`）、`xdup-0070`（`bintieju` / `bintie-ju`）、`xdup-0065`（`yu-qi-chang` / `yuqichang` / `imperial-porcelain-factory`）、`xdup-0067`（`fujian-chuanzhengju` / `fu-jian-chuan-zheng-ju` / `fujian-navy-yard`）、`xdup-0097`（`sectional-casting` / `fenzhu-fa` / `separate-casting`）。各合并写入一个 KU。

本批新增全库第一个 `event` 类型知识元（鸦片战争），**类型覆盖由 7/8 升至 8/8**；同时首次建立 `04-knowledge/units/events/` 目录。

## 二、canonical 映射

| 组 | 实体 | 类型 | canonical 候选 | 写回文件 | KU source_count |
|---|---|---|---|---|---|
| xdup-0063 | 鸦片战争 | event | `2009-zhaonong-…:cand-12-121` | `04-knowledge/units/events/opium-war.md` | 5 |
| xdup-0064 | 兴文署 | institution | `2009-xiayanjing-…:cand-05-58` | `04-knowledge/units/institutions/xingwenshu.md` | 3 |
| xdup-0065 | 御器厂 | institution | `2004-gaofeng-…:cand-06-13` | `04-knowledge/units/institutions/yuqichang.md` | 5 |
| xdup-0066 | 江宁织造局 | institution | `2016-…-upgrade:cand-07-10` | `04-knowledge/units/institutions/jiangning-zhizaoju.md` | 3 |
| xdup-0067 | 福建船政局 | institution | `2009-xiayanjing-…:cand-06-28` | `04-knowledge/units/institutions/fujian-chuanzhengju.md` | 3 |
| xdup-0068 | 织染署 | institution | `2010-tianzibing-…:cand-08-43` | `04-knowledge/units/institutions/zhiranshu.md` | 5 |
| xdup-0069 | 锦署 | institution | `2009-xiayanjing-…:cand-03-77` | `04-knowledge/units/institutions/jinshu.md` | 4 |
| xdup-0070 | 镔铁局 | institution | `2009-xiayanjing-…:cand-05-40` | `04-knowledge/units/institutions/bintieju.md` | 3 |
| xdup-0097 | 分铸法 | procedure | `2010-tianzibing-…:cand-03-29` | `04-knowledge/units/procedures/fenzhu-fa.md` | 4 |

KU 的 `source_count` 按该实体在六册中是否有字面命中计数，与本组 `member_count = 3` 不等：鸦片战争 5 册、御器厂 5 册、织染署 5 册、锦署 4 册、分铸法 4 册。差额来自 `doc_count = 3` 之外的册次，已在各 KU 的 `sources` 中列明。李立新一册虽多处叙述鸦片战争背景，但无「鸦片战争」四字，未计入 `sources`。

## 三、方法

1. **语义复读**：逐组读三册原文窗口，按行号定点回查，确认候选 payload 与正文一致后才落笔；`sources[].location` 可回溯到行。`xdup-0063` 的 canonical 候选 payload 把战争年份写作 1842，而赵农同册另有「道光20年（1840年）……发动了鸦片战争」，本批以原文为准，两说并列写入 KU，未沿用 payload 的单一取值。
2. **差异记录而非裁决**：来源之间的冲突（纪年、隶属、职能范围、术语次序）原文并列保留，写入 `## 核心内容` 并标注出处，不做偏好性裁定。
3. **状态链**：canonical 走 `needs_evidence → ready_for_review → approved → applied`；同组其余 2 条走 `needs_evidence → rejected`，reason 中写明 canonical 目标。
4. **追加式台账**：`candidate-decision-ledger.jsonl` 共 45 行（27 + 9 + 9），覆盖 27 个唯一 `candidate_id`，只以 transition 叠加，不改写历史 R1 台账。
5. **类型化写回**：`apply-plan.jsonl` 为 9 条 `create`，无 `update`、无 `delete`；逐条重算 `sha256 / bytes / lines`（CRLF→LF 归一）并与磁盘核对，9/9 一致。
6. **验证分级克制**：9 个 KU 一律 `confidence: medium`、`consensus: tentative`、`evidence_status: source_backed`，不填 `verification_level`。`分铸法` 来源内部冲突激烈，但按字段契约 `consensus: disputed` 须配 L1–L7 验证层级，本批未做外部验证，故不升为 `disputed`。

## 四、主要来源差异

| 实体 | 差异 |
|---|---|
| 鸦片战争 | 赵农同册并存「道光20年（1840年）……发动了鸦片战争」与「1842 年，英国发动鸦片战争」；高丰以「1856年至1860年的第二次鸦片战争」为洋务运动契机；「最早的民族近代工业」是否系于缫丝业仅夏燕靖两版作此判断且措辞不同；郑观应《盛世危言》引文作者名「郑观应」（李立新）与「郑观庆」（高丰）、用字「业冶／业治」「投闲／偷闲」并存；赵农「英国生铁产量达到 139 吨」「龙门火炮」两处原文异常 |
| 兴文署 | 《元史·百官志》「属集贤院」与《元秘书监志》「属秘书监」在同一段内互相冲突；赵农另点《通志》与「官方审查制度严格」，为夏燕靖两版所无；两版同作「文艺监」；人员编制（镌字匠四十名、印匠十六等）仅夏燕靖两版 |
| 御器厂 | 高丰与田自秉同作「洪武三十五年」设置（明代纪年洪武止于三十一年，原文照录）；地点「珠山」与钦限／部限分工仅田自秉一家；夏燕靖两版与田自秉另一处的「御器厂或官窑的前身」系对唐越窑的追述，不构成对明代御器厂的独立证据 |
| 江宁织造局 | 曹氏任职年数在夏燕靖 2016 同段内并存「58年」与「前后60余年」；「曹颙、曹頡」与「孙颙、頫」为同段两处异写；职能表述「特织御用云锦」（夏燕靖两版）与「管理织锦的生产」（田自秉）侧重不同；田自秉所引「173张／800张、667人／2330人」系于苏州织造而非江宁 |
| 福建船政局 | 夏燕靖两版同册并存「1872年……奏报创办福建船政局意图」与「1866年5月，上奏清廷创办福建船政局」；「沈葆祯」用字；「用35年的时间，造船舰40艘」未给起讫年，无法与李立新「1869年6月建造了中国第一艘近代蒸汽船」直接核对 |
| 织染署 | 田自秉给出隋代司染署与司织署合并为织染署的沿革，其余四册只记唐制；职掌「负责织造」（高丰）与「掌供冠冕、组绶及织纴、色染」（赵农引《新唐书·百官志》）宽窄不同；用字「织纴」（赵农）与「织衽」（田自秉）并存；**赵农「25 个『作』」与田自秉所引四类分项 10+5+4+6＝25 相合，构成来源内互证**；「右东道」原文如此 |
| 锦署 | 田自秉所记「织锦署」在后赵邺城，与东晋「锦署」同名异实（时代、地点、名称均不同），仅作对照，不计入本实体证据；夏燕靖两版把设置系于刘裕灭后秦迁关中工匠，李立新只作「晋室南渡后，成立锦署」；设置地点四册均未明写 |
| 镔铁局 | 夏燕靖两版作「专门冶炼铁铜等金属产品」（冶铸），赵农作「管理镔铁镂刻、镶嵌金银的制作」（装饰加工），两说属不同工序环节；「工部总管府」原文如此，与同段「集宁路总管府」含义不同 |
| 分铸法 | 田自秉作「浑铸→分铸→焊接」三段递进，李立新作「分铸法最初是浑铸……后改为焊接」，对同一组三个术语给出相反排列；同一件司母戊鼎在四册中分别被定性为分铸法（田自秉）、一次性整体铸造（赵农）、接铸（夏燕靖两版）；李立新「分铸法是工匠在长期技术经验中产生的一个技术设计」为六册中唯一的技术设计定性 |

## 五、验证结果

| 门禁 | 结果 |
|---|---|
| `apply-plan` 哈希核对 | 9/9 与磁盘一致（sha256、bytes、lines；CRLF 归一） |
| `build_discovery_index.py` | total 5339，applied 43，needs_evidence 5146，rejected 150，无 issue |
| `audit_content_quality.py` | 0 项发现（71 个知识元） |
| `audit_repo.py` | structural health 122/130；类型覆盖 8/8；Frontmatter 缺失 0；类型值不匹配 0；验证语义问题 0；证据引用 71/71 可解析 |
| `build_runtime_index.py` | 已刷新 `06-runtime/automation/index.md` |
| `run_sync_closure.py --refresh-generated --full --check-generated` | sync closure passed |
| `pre_commit_check.py` | 规则漂移 0 |

既有台账的口径差异（非本批引入）：`discovery-manifest.json` 的 `applied_candidate_transition_counts["needs_evidence->rejected"]` 为 149，而 `by_state["rejected"]` 为 150。两者统计口径不同（前者只计 transition 事件，后者含无对应 transition 的终态行），前一批已存在同一差 1，本批未改变该差异的性质。

## 六、边界与未解决项

- 未 commit、未 push；仅工作树变更。
- 未建分支、未建 worktree；`main` 为唯一主线。
- `02-sources/` 只读，未改写；本批实际读取的源目录为 `03基础书籍-md文档/`。
- 未使用外部验证平台，证据仅限六册 Markdown 文本；未做图版或实物核验。
- `primary_theme` 与 `topic_memberships` 留空：Theme / Topic 节点尚未 materialize，已计入 research debt。
- 未写入正式 `relations`：9 个 KU 均处于 isolated 状态，跨 KU 共现只在正文以非断言方式记述。
- `doc_count = 3` 一层 103 组中，本批仅覆盖 9 组（institution／procedure／event）；余 94 组（282 条候选）仍为 `needs_evidence`，未作状态推进，属 research debt。
- 类型覆盖 8/8 已达成，但 `event` 类型当前只有 1 个 KU，样本极薄；`place` 与 `publication` 之外的其他类型分布不均衡，后续批次不宜据「覆盖齐全」推断各类均已充分。
