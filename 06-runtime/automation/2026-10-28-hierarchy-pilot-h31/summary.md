# h31 批次摘要：D.6 染织线（官营织造与染练官署）

- 批次：`2026-10-28-hierarchy-pilot-h31`
- 日期：2026-10-28
- 层级版本：v1.21 → v1.22
- 结论：在既有 D.6 下续建 D.6.3「官营织造：从织室到织造局」与 D.6.4「染练官署：从暴室到织染署」两个 Topic，挂载 19 个 KU；27 个 authored 文件，27/27 哈希匹配。未 commit、未 push。

## 一、目标与范围

h30 的 manifest 把下一批候选登记为五项，其中「D.6 官营染织机构 Topic」列为第一项，并给出候选池：绫锦院（6 源）、织染署（5 源）、东西织室、三服官、江宁织造局（4 源）、四川锦院、绣院、纳失失局、建康路织染局、木棉提举司、后赵邺城织锦署、南朝染署、宋代染织管理机构群、周代染人。本批选这一项，三项判断如下。

第一，它是 D.6 内部的欠账，不是新开边界。D.6 在 v1.21 就标为多批次 Theme，染织线明写在候选池里；`04-knowledge/structure/themes/README.md` 与 `dimension-candidates.md` 两处都记着「官营染织机构尚未物化」。本批只是把这条线补上，不改 D.6 的边界。

第二，候选池在复读中扩大。复读 `04-knowledge/units/institutions/` 下全部未挂载文件后，D 维度未挂载的官营染织机构与染练官署共 19 条，比 h30 登记的多 5 条：汉代官营丝织作坊、锦署、暴室、平准令、典丝。多出的条目不是新发现，而是 h30 只按「名称显眼」登记，漏掉了聚合条与职名条。

第三，19 条不能塞进一个 Topic。命名依据分成四类、时代横跨汉至清、其中 6 条讲的是染而不是织；若合并成一个 Topic，research_question 会同时问「机构沿革」与「织染分合」两件事，违反「Topic 是可回答的具体问题」这一条。因此按织造／染练切开，13 + 6。

## 二、结构物化

### 新建 D.6.3「官营织造：从织室到织造局」

- 文件：`04-knowledge/structure/topics/d6-guanying-zhizao-cong-zhishi-dao-zhizaoju.md`
- 字段：`parent_theme: D.6`、`primary_dimension: D`、`status: pilot`、`date: 2026-10-28`；`research_question` 172 字（目标区间 171–185）；tags 12 项。
- 支撑材料 13 行：`key_institution` 11（东、西织室、三服官、后赵邺城织锦署、锦署、绫锦院、四川锦院、绣院、纳失失局、建康路织染局、木棉提举司、江宁织造局）、`historical_context` 2（汉代官营丝织作坊、宋代染织管理机构）。
- 四项核心判断：
  1. 命名依据四分——按工序（织室、织锦署）、按产品（绫锦院、锦院、绣院、纳失失局、木棉提举司）、按服务对象（三服官）、按技术来源（锦署）。命名依据不同，机构之间不可比，把它们排成一条线是用一个不存在的共同标准覆盖四类对象。
  2. 同名异实不合并：「绫锦院」宋辽金元四朝各有建制、六册无一句说明沿革；「锦署」（东晋江南）与「织锦署」（后赵邺城）名称近而时代地点皆异。本 Topic 只承认同一朝代内部的连续。
  3. 工匠征调的数字六组（作工各数千人、汴梁锦工 200 人／织机 400 余张、四川军匠 500 人＋挽综 164＋杼 54＋练染 11＋纺绎 110、建康路 3,600 户／154 机、纳失失局 3,300 多户、至元十六年掠工匠 42 万人），单位分别是人、户、军匠、移入户，**不换算、不合计**；共同点是规模总以人口形式出现，不以产量或产值形式出现。
  4. 产品指定是官府索取的主要形式：四川锦院四类锦逐类开列锦名、建康路额造 4,527 段、木棉提举司岁输 10 万匹、江宁织造局特织御用云锦三类。四处都不是市场交易。
- 三层证据密度：有任职序列与年份的 1 条（江宁织造局）、有工匠与设备数字的 3 条（四川锦院、建康路织染局、纳失失局）、只有局名或职掌一句的 9 条。
- 未解决问题 14 条。

### 新建 D.6.4「染练官署：从暴室到织染署」

- 文件：`04-knowledge/structure/topics/d6-ranlian-guanshu-cong-baoshi-dao-zhiranshu.md`
- 字段：`parent_theme: D.6`、`primary_dimension: D`、`status: pilot`、`date: 2026-10-28`；`research_question` 181 字；tags 10 项。
- 支撑材料 6 行：`key_institution` 4（暴室、平准令、南朝染署、织染署）、`boundary_case` 2（周代染人与掌染草、典丝）。
- **本 Topic 在复读中改写了自己的原假设**。初稿按「染练的独立性只停留在官名上」立论，写完后逐条核对田自秉原文，发现一条更实的记载：北朝拓跋魏早期设少府管染织，后少府改为太府，有司染署，下属京坊、河东、信都三局；同一段又记中尚方领泾州丝局、雍州丝局与定州绸绫局。这条说明染练确曾独立设署、且有下属局，织与染在北朝是两条并行的官署线。若沿用初稿，Topic 的核心判断就是错的，因此整篇重写：research_question 由「染练是否曾经独立设署」改为「独立设署在北朝是否已成建制，为什么唯一的分工细目反而出现在它被并入织造之后」。
- 改写后的三层：「官名—职掌—局属」。官名层五个官名的改制动因分别是宫禁服务、少府职掌、避讳、官署合并，没有一处提到染练本身；职掌层五句都说了「管什么」而没说「管多少」；局属层给出北朝三局与中尚方三局，是三层的唯一实证。
- 核心发现：**染练的独立设署与其记载密度成反比**——唯一可证成独立设署的北朝只有三局地名，唯一有分工细目的隋唐已在合并之后。本 Topic 把原因标为取材体例的推测（独立官署入职官表、合并分工入工序表），不作定论。
- 未解决问题 10 条。

### 既有结构更新

- `04-knowledge/structure/themes/d6-guanfu-shougongye-zhiguan-jiangyi-sheji-kongzhi.md`：下属 Topic 2→4；支撑结构 14→33 个 KU，role 分布改为 `key_institution` 27、`boundary_case` 3、`historical_context` 2、`geographical_context` 1；核心问题新增第三条线索（染织线与陶窑线对照：陶窑线记载随朝代累积，染织线随朝代重置）；支撑结构新增 v1.22 跨 Topic 判断；文献支撑补染织线六册分工；tags 补 12 项；未解决问题补 9 条。
- `04-knowledge/structure/hierarchy/index.md`：v1.21→v1.22，Topic 58→60，membership 441→460，完整挂载 437→456，未挂载 2133→2114，Level 4 的 D.6 行由 2 个改为 4 个，末尾追加 v1.22 版本边界段。
- `04-knowledge/structure/hierarchy/archive/v1.21.md`：39602 字节，与 v1.21 版 index.md 逐字节一致（`sha256:1737b5f8…`，即 h30 apply-plan 的 after_sha256）。
- `04-knowledge/structure/themes/README.md`：D.6 段改为两批四 Topic 分述，新增染织线两条判断段，未物化清单删去官营染织机构。
- `04-knowledge/structure/topics/README.md`：58→60 个 Topic，D.6 段改为「陶窑线＋染织线」两线说明。
- `04-knowledge/structure/dimension-candidates.md`：三十批 437→三十一批 456，新增 v1.22 续建条目，前近代缺口行补 v1.22，未挂载 2133→2114。

## 三、19 个 KU 的挂载

| KU | 类型 | Topic | role | 源数 | version |
|---|---|---|---|---|---|
| `institutions/dongxi-zhishi.md` 长安东、西织室 | institution | D.6.3 | `key_institution` | 2 | 2→3 |
| `institutions/sanfuguan.md` 三服官 | institution | D.6.3 | `key_institution` | 2 | 1→2 |
| `institutions/han-dai-guan-ying-sizhi-zuofang.md` 汉代官营丝织作坊 | institution | D.6.3 | `historical_context` | 1 | 1→2 |
| `institutions/houzhao-yecheng-zhijinshu.md` 后赵邺城织锦署 | institution | D.6.3 | `key_institution` | 1 | 1→2 |
| `institutions/jinshu.md` 锦署 | institution | D.6.3 | `key_institution` | 4 | 1→2 |
| `institutions/lingjinyuan.md` 绫锦院 | institution | D.6.3 | `key_institution` | 6 | 3→4 |
| `institutions/song-dai-ranzhi-guanli-jigou.md` 宋代染织管理机构 | institution | D.6.3 | `historical_context` | 1 | 1→2 |
| `institutions/sichuan-jinyuan.md` 四川锦院 | institution | D.6.3 | `key_institution` | 1 | 1→2 |
| `institutions/xiuyuan.md` 绣院 | institution | D.6.3 | `key_institution` | 1 | 1→2 |
| `institutions/nashishiju.md` 纳失失局 | institution | D.6.3 | `key_institution` | 1 | 1→2 |
| `institutions/jiankanglu-zhiranju.md` 建康路织染局 | institution | D.6.3 | `key_institution` | 2 | 2→3 |
| `institutions/mumian-tijusi.md` 木棉提举司 | institution | D.6.3 | `key_institution` | 1 | 1→2 |
| `institutions/jiangning-zhizaoju.md` 江宁织造局 | institution | D.6.3 | `key_institution` | 4 | 2→3 |
| `institutions/zhou-ranren-zhangrancao.md` 周代染人与掌染草 | institution | D.6.4 | `boundary_case` | 1 | 1→2 |
| `institutions/dian-si.md` 典丝 | institution | D.6.4 | `boundary_case` | 1 | 1→2 |
| `institutions/baoshi.md` 暴室 | institution | D.6.4 | `key_institution` | 1 | 1→2 |
| `institutions/pingzhunling.md` 平准令 | institution | D.6.4 | `key_institution` | 1 | 1→2 |
| `institutions/nanchao-ranshu.md` 南朝染署 | institution | D.6.4 | `key_institution` | 1 | 1→2 |
| `institutions/zhiranshu.md` 织染署 | institution | D.6.4 | `key_institution` | 5 | 2→3 |

写入方式：脚本按 `primary_dimension: D` 行后插入 `primary_theme`／`secondary_themes`／`role_in_theme`／`topic_memberships`；`hierarchy_scope_note` 整行替换且与 `topic_memberships[0].scope_note` 逐字相同；`secondary_dimensions`（16 条有）保持在块之后、`hierarchy_scope_note` 之前，`hierarchy_scope_note` 仍是 frontmatter 最后一字段；`version` +1、`updated: 2026-10-28`；正文「在层级体系中的位置」替换为六行段。每条写回后重新 `yaml.safe_load` 并断言全部字段。

## 四、边界处置

| 边界对象 | 处置 | 依据 |
|---|---|---|
| 织染署 | 归 D.6.4，其「织衽十作」只在 D.6.3 对照时引用 | 它是唯一把织与染写进同一官名的机构，织染分合的判断需要一处落点，不能两处各挂一半 |
| 北朝中尚方三局（泾州、雍州丝局，定州绸绫局） | 归 D.6.4 与司染署三局并列处理，D.6.3 不另挂载 | 二者同出田自秉一段记载，拆开就看不到「织三局 vs 染三局」的并行结构 |
| 周代染人、掌染草、典丝 | 以 `boundary_case` 挂载 | 三者为职名，员额、隶属与职掌细目全无；不升格为官署 |
| 汉代官营丝织作坊、宋代染织管理机构 | 以 `historical_context` 挂载 | 两条为聚合条，承载网络范围而不重复分条细节 |
| 后赵织锦署 vs 东晋锦署 | 不合并 | 名称近而时代、地点皆异，六册无一句说明关系 |
| 绫锦院四朝（宋、辽、金、元） | 不排沿革，只列异制 | 宋代属少府监、辽在上京与祖州、金五处、元属织染杂造人匠总管府，来源无沿革说明 |
| 东、西织室的时代 | 东汉（夏燕靖）与西汉末（田自秉引《汉书》）两说并存不裁 | 两说不能同时成立，本库不据来源外知识断代 |
| 建康路「三千六百户」与「三千六户」 | 两写并录 | 两者相差两个数量级，来源未说明何者为准；只覆盖东织染局 |
| 工匠数字六组 | 不换算、不合计 | 人、户、军匠、移入户四种单位并列，统计口径来源均未说明 |
| 织染工艺、染料、染缬 | 归 B.2 与 `procedures/` | 本批只取机构、编制、产品与产品分配 |
| 民间机户、机房、包买主、江南染坊与踹布业 | 不并入 | 本 Theme 是官府手工业；「千室夜机鸣」只作背景 |
| 近代丝织棉纺企业与 1949 年后研究机构 | 归 B.1／D.1 与当代段 | D.5 已明文排除古代工官，反向亦然 |

## 五、执行与验证

1. 候选清点：`04-knowledge/units/institutions/` 下 D 维度未挂载文件逐条复读，得 19 条；内容摘要写入临时文件后逐条核对，不以文件名或 tags 裁决。
2. 结构设计：初定单 Topic 19 KU，复读后改为 13 + 6；D.6.4 因发现北朝司染署三局，整篇重写一次。
3. 写回：19 条 KU 一次脚本写入，逐条断言；两个 Topic 文件用 Write 工具创建；六处索引用脚本精确替换（每次 `count == 1` 断言）。
4. `scripts/hierarchy_stress_test.py` → v1.22、21 Theme、60 Topic、460 membership、456 complete、2114 incomplete、`themes_without_topics` 0、`cross_dimension_topics` []、`apply_permitted` false。
5. `scripts/build_relation_index.py` → 6914（explicit 5998、inferred 916）。
6. `scripts/run_sync_closure.py --refresh-generated --full` → **18/18 通过**，`250 passed, 16 subtests passed in 63.46s`，`sync closure passed`。
7. apply-plan 27 行，27/27 哈希匹配。
8. 保护路径（`02-sources`、`03-processing`、`.agents`、`scripts`、`01-domain`）零改动。
9. `--check-generated` 在未提交时 `[17/17] FAILED (exit=1)`，与 h29／h30 一致，属预期。

## 六、指标变化

| 指标 | v1.21 | v1.22 | 变化 |
|---|---|---|---|
| Level 3 Theme | 21 | 21 | 0 |
| Level 4 Topic | 58 | 60 | +2 |
| Topic membership | 441 | 460 | +19 |
| 完整挂载 KU | 437 | 456 | +19 |
| 未挂载 KU | 2133 | 2114 | −19 |
| 关系总数 | 6876 | 6914 | +38 |
| `member_of` 关系 | 878 | 916 | +38 |
| 隔离 KU | 1297 | 1287 | −10 |
| `structural_health` | 130 | 130 | 0 |
| `knowledge_structure_quality` | 56/65 | 56/65 | 0 |
| 单源 KU | 1919 | 1919 | 0 |
| 低置信 KU | 496 | 496 | 0 |
| tentative KU | 2570 | 2570 | 0 |
| candidate index | 5339 | 5339 | 0 |
| translation index | 2178 | 2178 | 0 |
| claim registry | 1242 | 1242 | 0 |

关系增量为 38 = 19 条 KU × 2（`member_of` 指向 Theme 与 Topic 各一条），与 v1.21 的 28 = 14 × 2 同构。隔离 KU 只减 10 而非 19，是因为其中 9 条原有关系已足以脱离隔离集合。

## 七、语义边界

1. **不写织造通史。** 13 条机构横跨汉至清、彼此无沿革记载，本 Topic 只承认同朝代内部连续；跨朝同名一律标为待证。
2. **不裁断两说。** 东、西织室的时代、建康路的两组户数、曹氏任职的 58 年与 60 余年、江宁织造局「曹颙、曹頡」与「孙颙、頫」的异写，全部并列保留。
3. **不合并同名机构。** 后赵织锦署与东晋锦署、绫锦院四朝、平准令（汉）与南朝染署（避讳改名），都不排成一条线。
4. **不换算工匠数字。** 六组数字单位不同、口径不明，本批不合计、不推算产能或工资。
5. **不把「官」当成统一主体。** 沿用 D.6 的既有约定：作坊、职官、机构、产品等级四义分离，每条 KU 的 `scope_note` 写明所占之义。
6. **不把解释框架写成来源结论。** 染练「独立设署与记载密度成反比」是本库观察；「取材按职官表与工序表分别进行」标为推测。织造「命名依据四分」是从六册归纳的，来源未作此分类。
7. **不填补空缺。** 北朝三局只有地名，不据后世地理补写「京坊＝洛阳」；锦署地点只写「江南」，不补「建康」；四川锦院不补隶属与设官。

## 八、生成态与门禁

- 生成态刷新：`06-runtime/state/current-health.json`（v1.22）、`06-runtime/governance/governance-backlog.md`、`06-runtime/automation/index.md`（h31 已入索引）、`04-knowledge/quality/relation-index.yml`（6914）、`06-runtime/state/generated-projections-manifest.json`、`06-runtime/state/candidate-index.jsonl`（5339）、`04-knowledge/quality/translation-index.yml`（2178）等，均由 `run_sync_closure.py --refresh-generated --full` 重建，未手工编辑。
- `06-runtime/state/generated-projections-manifest.json` 不追踪 `06-runtime/automation/<pkg>/manifest.json` 与 `summary.md`，因此本文件的后续修订不需重跑闭包；但 automation 索引记录其字节数，若改动这两个文件，须重跑第 3 步。
- 门禁：`--check-generated` 在未提交时按设计失败（`[17/17] FAILED (exit=1)`），等价于 `git diff --exit-code HEAD -- <generated paths>`；**该失败不表示本批有缺陷，而表示工作树尚未提交**。
- 本批未 commit、未 push：commit 与 push 属外部状态变更，须由用户当次明确授权。

## 九、未决事项与下一跳

1. **D.6 剩余两块**：地方工官与特种作坊（蜀郡成都广汉郡工官、秦工室工官、汉代漆器作坊工官、镔铁局 3 源、兴文署、西夏官营手工业机构群、西夏文思院）；内廷造办（内务府造办处 5 源、果园厂、石渠阁、武英殿修书处、宋代画院 `song-dai-huayuan`）。两块补齐后 D.6 的前近代官府手工业骨架可告一段落。
2. **D.6 民间与局院侧**：民间机户、机房、包买主、江南染坊与踹布业；元代绣局、纹锦总院、涿州罗局。这些不属于「官府手工业」，须另定边界（可能落 D.2 或新的 D 维度 Topic）。
3. **B.5 史前功能陶器**：陶鬶、陶甑、陶埙、鱼鳍形足陶鼎、水鸟形陶壶、山东莒县陶尊（6 条候选），自 h29 起挂起。
4. **玻璃材料 Theme**：琉璃第一义、铅钡与钠钡玻璃、战国琉璃璧、长沙楚墓群、李立新玻璃器沉浮。
5. **重复候选 4 组待 reconcile**：`terms/youlihong-ci` vs `terms/youlihong`；`terms/bai-tao` vs `terms/shangdai-baitao`；鲁山窑瓷拍鼓 vs 花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` vs `works/zhulin-qixian-rongqiqi-zhuanhua`。
6. **图注单条待核队列 12 条**：五彩人物洗、珐琅彩竹菊鹌鹑瓶、铜官窑釉罐、追韩信图梅瓶、蒙恬将军玉壶春瓶、山东莒县陶尊、陶井、三彩罐、紫砂瓜形壶、紫砂「东陵瓜」、双鹿瓦当、始皇陵夔凤纹大瓦当。
7. **存量债务（v1.22）**：未挂载 2114、单源 1919、tentative 2570、低置信 496、隔离 1287。
8. **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺沿革史略》未挂载。
