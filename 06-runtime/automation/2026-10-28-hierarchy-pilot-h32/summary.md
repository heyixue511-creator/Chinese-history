# h32 批次摘要：D.6 地方工官与内廷制作（D.6.5、D.6.6）

## 一、目标与范围

本批在 v1.22 所建 D.6「前近代官府手工业：职官、匠役与设计控制」下续建两个 Topic：

- D.6.5「地方工官与特种作坊：从秦工室到西夏局院」——收 7 个地方层级与特种行业机构；
- D.6.6「内廷御用制作：画院、果园厂与造办处」——收 4 个内廷机构与 1 个设立事件。

基线为 v1.22：21 Theme、60 Topic、460 membership、456 complete assignments、2114 个 KU 未挂载、relation index 6914。本批不动 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`，不新建 Theme。

## 二、结构物化

### 新建 D.6.5「地方工官与特种作坊：从秦工室到西夏局院」

- `parent_theme: D.6`、`primary_dimension: D`，`research_question` 173 字。
- 支撑材料 7 个 KU，全部 `institution`、全部 `key_institution`：秦代工室与工官、蜀郡成都广汉郡工官、汉代漆器作坊官员、镔铁局、兴文署、西夏官营手工业机构、西夏文思院。
- 以「名目—经费—编制」三层组织材料，三层即三种证据形态：西夏七机构、汉代八郡、秦代县工官三组都只有名单；「岁费五百万」是唯一可量化的地方经费线索但币值、年份与口径全无；兴文署的完整人员编制是六册唯一一份。核心发现是「官府手工业的编制证据，只在刻书这一行留下完整一份」，故「专」只能判为名称层面的分类。
- 10 条未解决问题，含地方工官的统属关系无法证成、三处工官是否兼营铜漆、镔铁局两说不可调和、西夏七机构的机构性质未明等。

### 新建 D.6.6「内廷御用制作：画院、果园厂与造办处」

- `parent_theme: D.6`、`primary_dimension: D`，`research_question` 175 字。
- 支撑材料 5 个 KU：宋代宫廷画院、果园厂、武英殿修书处、内务府造办处（`key_institution`），宋代宫廷画院设立（`evidence_event`）。
- 以「规范—技艺—程式—指示」四种控制形态组织材料，四者按介入粒度由粗到细排列。三条发现：控制强度与作坊规模不成正比；成文的「程式」只出现在印刷，与 D.6.5 的唯一完整编制同属印刷机构；四种形态不能互相替代。
- 9 条未解决问题，含四个机构不能证成「内廷造办系统」、画院「格法」的具体内容全无、造办处两个名称是否同一机构未明等。

### 既有结构更新

- Theme `d6-guanfu-shougongye-zhiguan-jiangyi-sheji-kongzhi.md`：tags 24→35；核心问题新增第四条线索（中央、地方、内廷三端记载落差，证据密度按「产品可否分解计数」分布）；纳入清单补两组；下属 Topic 4→6；新增 v1.23 跨 Topic 判断；实证 33→45 KU；文献支撑补两线来源；未解决问题 +12 条；边界说明补石渠阁、武英殿 C→D、西夏文思院三条。
- `hierarchy/index.md` v1.22→v1.23；`archive/v1.22.md` 为改动前原样副本（41,984 字节，逐字节一致）。
- `themes/README.md`、`topics/README.md`、`dimension-candidates.md` 同步。

## 三、12 个 KU 的挂载

| KU | 类型 | role | Topic | version |
|---|---|---|---|---|
| `institutions/qin-gongshi-gongguan.md` | institution | `key_institution` | D.6.5 | 1→2 |
| `institutions/shujun-chengdu-guanghanjun-gongguan.md` | institution | `key_institution` | D.6.5 | 1→2 |
| `institutions/han-dai-qiqi-zuofang-guan-yuan.md` | institution | `key_institution` | D.6.5 | 2→3 |
| `institutions/bintieju.md` | institution | `key_institution` | D.6.5 | 1→2 |
| `institutions/xingwenshu.md` | institution | `key_institution` | D.6.5 | 1→2 |
| `institutions/xi-xia-guan-ying-shou-gong-ye-jigou.md` | institution | `key_institution` | D.6.5 | 2→3 |
| `institutions/xi-xia-wensiyuan.md` | institution | `key_institution` | D.6.5 | 1→2 |
| `institutions/neiwufu-zaobanchu.md` | institution | `key_institution` | D.6.6 | 4→5 |
| `institutions/guoyuanchang.md` | institution | `key_institution` | D.6.6 | 1→2 |
| `institutions/wuyingdian-xiushuchu.md` | institution | `key_institution` | D.6.6 | 2→3 |
| `institutions/song-dai-huayuan.md` | institution | `key_institution` | D.6.6 | 1→2 |
| `events/song-dai-huayuan-sheli.md` | event | `evidence_event` | D.6.6 | 1→2 |

每个 KU 均写入 `primary_theme: D.6`、`secondary_themes: []`、`role_in_theme`、一条 `topic_memberships`（含 `primary: true` 与 `scope_note`），`hierarchy_scope_note` 与 `scope_note` 逐字相同并保持为 frontmatter 末字段；正文「在层级体系中的位置」替换为六行段；`version` +1、`updated: 2026-10-28`。

## 四、边界处置

| 对象 | 处置 | 理由 |
|---|---|---|
| 石渠阁 | 不挂载 | 汉代皇家藏书与档案机构，来源只有「珍藏秦王朝留下的大量地图和书籍」一句，无生产或设计活动记载 |
| 武英殿修书处 | C→D 跨维度挂载 | `primary_dimension` 为 C，取生产组织侧；沿用秦汉官营陶窑 B→D 先例 |
| 西夏文思院 | 不合并 | 与唐宋文思院同名而异时、异政权，不排沿革 |
| 造车院／出车（造车）院 | 并录不裁 | 夏燕靖与田自秉用字不同，不据一册改写另一册，不另立第八机构 |
| 镔铁局两说 | 并存不裁 | 冶铸（夏燕靖）与装饰加工（赵农）指向不同生产环节 |
| 兴文署上级 | 并存不裁 | 《元史·百官志》属集贤院、《元秘书监志》属秘书监 |
| 蜀郡、成都、广汉三工官 | 照录不合并 | 「成都」与「蜀郡」的层级关系未明，铜、漆是否同一批机构未明 |
| 秦代工室与工官 | 合并立目 | 工室作背景，只取县工官作地方侧证据 |
| 画院下游四机构 | 只引用「影响」 | 不虚构行文或验收关系；甲库不单独立目 |
| 内廷四机构 | 不作系统 | 来源从未并列，果园厂到造办处漆作只有一句工艺传承 |
| 画院设立事件 | 同源不互证 | 与机构条同出李立新 2011，只承担设立与制度来源 |
| 乾隆逐件指示 | 不补写 | 只有一句概括，无指示原文、尺寸单或验收记录 |

## 五、执行与验证

- `scripts/hierarchy_stress_test.py` → `hierarchy_version: v1.23`、themes 21、topics 62、topic_memberships 472、complete_assignments 468、incomplete_assignments 2102、themes_without_topics 0、cross_dimension_topics []、apply_permitted false。
- `scripts/build_relation_index.py` → 6938 条（explicit 5998、inferred_by_rule 940、migrated_from_related 0），member_of 940。
- `scripts/write_current_health.py` → v1.23、complete 468、missing 2102、relation 6938、isolated 1283、structural_health 130、knowledge_structure_quality 56/65。
- `apply-plan.jsonl` 20 行（2 `structure_node_create`、12 `hierarchy_mount`、6 `structure_index_update`），20/20 哈希与磁盘一致。
- 本批 20 个 authored 文件全部经内联脚本一次写入、逐条断言：`primary_dimension` 锚点唯一、`primary_theme` 原为空、`hierarchy_scope_note` 原存在、`updated` 与 `version` 各唯一、YAML 解析后逐字段与末键断言。

## 六、指标变化

| 指标 | v1.22 基线 | v1.23 结果 |
|---|---|---|
| Theme | 21 | 21 |
| Topic | 60 | 62 |
| Topic membership | 460 | 472 |
| 完成五级挂载 KU | 456 | 468 |
| 未挂载 KU | 2114 | 2102 |
| relation index | 6914 | 6938 |
| member_of | 916 | 940 |
| 隔离单元 | 1287 | 1283 |
| structural_health | 130 | 130 |
| knowledge_structure_quality | 56/65 | 56/65 |
| 库存 KU | 2570 | 2570 |

D.6 累计挂载 45 个 KU（`key_institution` 38、`boundary_case` 3、`historical_context` 2、`geographical_context` 1、`evidence_event` 1），覆盖 43 个 institution、1 个 place、1 个 event。跨维度挂载两条：秦汉官营陶窑 B→D、武英殿修书处 C→D。

## 七、语义边界

1. D.6.5 的「专」只能判为名称层面的分类：西夏七机构、汉代八郡、秦代县工官三组均无隶属、员额、产品与规模，来源的「专业分工相当细致」是评价而非证据。
2. 「岁费五百万」只用于证明三处工官有独立核算，不用于推算产能：来源未给币值、年份、经费来源与用费口径。
3. 兴文署的完整编制是六册唯一一份机构编制表，但它是印刷机构而非器物制作机构；本库不据以推断器物作坊的人员结构。
4. D.6.6 的四种控制形态是本库的分析框架，不是来源的分类；六册没有任何一处记载两层同时在场。
5. 画院对下游四机构的「影响」只有一词，本库不把它写成制度化的样式下达；「格法」的具体内容（粉本、程式、考核标准）全无。
6. 「内廷造办系统」不成立：四个机构来源从未并列，果园厂到造办处漆作只有一句工艺传承，无机构沿革、隶属转移或人员承接。
7. 跨 Topic 判断「证据密度按产品可否分解计数分布」是本库解释，不是来源结论；两处印刷机构（兴文署、武英殿修书处）的不对称同属这一解释，但只有两个样本。

## 八、生成态与门禁

- `hierarchy/index.md` 升版并归档 `archive/v1.22.md`（41,984 字节，与改动前逐字节一致，`sha256:78d5c1a4…`）。
- `relation-index.yml`、`current-health.json`、`governance-backlog.md`、`generated-projections-manifest.json` 由刷新步骤重建，不在 apply-plan 内。
- `run_sync_closure.py --refresh-generated --full` → **18/18 通过**（`sync closure passed`，`250 passed, 16 subtests passed`，66.46s）。
- `run_sync_closure.py --refresh-generated --check-generated` → **[17/17] FAILED (exit=1)**，原因为本批未提交，生成态快照与工作区不一致；这是提交前门禁的预期结果，不是失败信号。提交后须重跑至通过。
- `06-runtime/automation/index.md` 已由生成步骤收录 h32。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动（`git status --porcelain` 为空）。
- `apply-plan.jsonl` 20/20 哈希在闭包后复核仍与磁盘一致。

## 九、未决事项与下一跳

- 未决：地方工官的统属层级无法证成；三处工官是否兼营铜漆；镔铁局两说；兴文署上级两说与编制年份；西夏七机构的机构性质与文思院产品归属；画院「格法」内容与下游行文关系；果园厂与造办处的年份、员额与产品流向；武英殿修书处的内部机构与《聚珍版程式》执行程度。
- 下一跳候选：B.5 史前功能陶器（6 条）；玻璃材料 Theme；重复候选 reconcile 4 组；图注单条待核 12 条；存量债务（未挂载 2102、单源 1919、tentative 2570、低置信 496、隔离 1283）。
- 本批不 commit、不 push；commit 与 push 须用户当次明确授权。
