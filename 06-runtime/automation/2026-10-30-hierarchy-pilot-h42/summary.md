# h42 乐器与八音线：B.10「乐器与八音：材质分类、乐律与钟磬」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h42/`
- 基线：v1.32（24 Theme／77 Topic／606 membership／598 complete／1972 incomplete／relation 7202／member_of 1204／isolated 1220／ksq 57/65／structural 130）。
- 目标：在原计划的「B.9 乐器 Topic」处作结构改判，另立 Theme **B.10 乐器与八音：材质分类、乐律与钟磬**，下辖两个 Topic，主挂载 13 个 KU、次挂载 1 个。
- 结果：v1.33（25 Theme／79 Topic／620 membership／611 complete／1959 incomplete／relation 7229／member_of 1231／isolated 1210／ksq 57/65／structural 130）。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Theme `04-knowledge/structure/themes/b10-yueqi-yu-bayin-caizhi-fenlei-lelv-yu-zhongqing.md`：`theme_code: B.10`、`primary_dimension: B`、`secondary_dimensions: [D, C]`、`status: pilot`、`date: 2026-10-30`、六册 `source_basis`。
- 新建 Topic `B.10.1 八音与乐律：材质分类、律制与乐学文献`（`research_question` 181 字，5 个 KU）与 `B.10.2 钟磬与青铜乐器：编钟、编磬、镈与铜鼓`（`research_question` 175 字，9 个 KU）；两者 `secondary_themes: [D, C]`。
- 直属分工：B.10.1 回答「六册把乐器分成什么、记到哪一层」，B.10.2 回答「钟磬四层记载各自能证到什么程度」；B.10.3 弦管与革类鼓留待后续。
- **改判登记**：B.9 原边界写「乐器（编钟）归后续 B.9 Topic」。本批判定八音本身是跨材料分类——磬属石、埙属土、琴瑟属丝、笙竽属匏、笛箫属竹，编钟与铜鼓只占金类一支；整条乐器线若挂在 B.9「青铜与金属」之下，非金属乐器无处安放、B.9 边界亦被撑破。故另立 Theme，而非增设 B.9.7。该理由在 Theme 边界末尾、`hierarchy/index.md` v1.33 版本边界段、`themes/README.md`、`topics/README.md`、`dimension-candidates.md` 五处同时登记。
- B.9 节点四处更正：边界中「乐器归后续 B.9 Topic」改写为另立 B.10 的说明，并把兵器、铜镜改标为已由 B.9.6／B.9.3 承接；未解决问题同步；「下属 Topic」由 2 条补足为 6 条；支撑结构由「两个 Topic 合计 20 个 KU」按实测改为「六个 Topic 合计主挂载 91 个 KU（term 39、work 36、procedure 16）＋1 条次挂载，`term_anchor` 38、`representative_work` 32、`boundary_case` 6、`procedure` 15」。后两项是 v1.29–v1.32 未回填的存量陈旧，本批一并更正。
- 快照：`hierarchy/index.md` 归档为 `hierarchy/archive/v1.32.md`（60830 字节，先复制、`cmp` 逐字节一致后再改 index.md）。

## 三、14 个 KU 挂载

主挂载 13 条（全部 `primary: true`，`version` +1、`updated: 2026-10-30`）：

| KU | Topic | role | 承担什么 |
|---|---|---|---|
| `terms/ba-yin.md` | B.10.1 | `term_anchor` | 金石土革丝木匏竹八类、周代约 70 种与《诗经》29 种、编磬编钟与琴的地位 |
| `terms/shier-pingjun-lv.md` | B.10.1 | `term_anchor` | 朱载堉发明、对近代乐器制造的积极作用、键盘乐器依此定音 |
| `persons/zhu-zaiyu.md` | B.10.1 | `key_person` | 郑藩宗室、著《乐律全书》、发明十二平均律 |
| `publications/yuelv-quanshu.md` | B.10.1 | `supporting_source` | 郑藩刻本与印刷精良；跨维度主挂载（`primary_dimension` 为 C） |
| `terms/bianzhong.md` | B.10.2 | `term_anchor` | 与特钟之别、铙到钟的甬与旋、商三件一组与西周八件一套 |
| `terms/qing.md` | B.10.2 | `term_anchor` | 孔子击磬于卫、图 3-45 图注、曾侯乙墓 124 件乐器清单 |
| `terms/tonggu.md` | B.10.2 | `term_anchor` | 乐器转权力象征、滇粤两系、四类纹样名 |
| `works/zenghouyi-bianzhong.md` | B.10.2 | `representative_work` | 三层悬挂、五个八度、中部十二半音、64 与 65 两说、浑铸法 |
| `works/huwen-da-shiqing.md` | B.10.2 | `representative_work` | 84×42×2.5 厘米、1950 年武官村大墓、双钩线刻虎形 |
| `works/qin-gong-bo.md` | B.10.2 | `boundary_case` | 「西周后期出现正挂之镈」一句与图 3-46 图注 |
| `works/jingyun-er-nian-dazhong.md` | B.10.2 | `representative_work` | 景云二年、约 12000 斤、四类纹饰 |
| `works/dazhongsi-bell.md` | B.10.2 | `representative_work` | 高 6.75 米、口径 3.3 米、44.6 吨、现存最大铜钟 |
| `works/chao-zhong-tong-fa.md` | B.10.2 | `boundary_case` | 《天工开物》图 3-3 图注，唯一铸钟图像线索，`confidence` low |

次挂载 1 条：`terms/taoxun.md`（`version` 2→3）追加 B.10.1 membership（`term_anchor`，`primary: false`），主挂载仍为 B.5.7。

role 分布：`term_anchor` 6、`representative_work` 4、`boundary_case` 2、`key_person` 1、`supporting_source` 1。类型分布：term 4、work 6、person 1、publication 1。

## 四、边界处置

- 乐器内部：分类与律制归 B.10.1，金石两目与铜鼓归 B.10.2，弦管与革类鼓归后续 B.10.3；B.10.1 与 B.10.2 不重复计入同一 KU 的主挂载。
- 陶埙双层：主挂载 B.5.7 取史前成形、烧成与仿声诱捕，B.10.1 次挂载只取「八音土类」一面，次挂载不重复计入主挂载范围。
- 归 B.9：青铜容器器形与礼器组合（B.9.1）、合范浑铸分铸失蜡六齐（B.9.2）、铜镜（B.9.3）、金属表面装饰（B.9.4）、金银器与金属胎珐琅（B.9.5）、兵器与甲胄（B.9.6）。
- 归 D：礼乐制度（`terms/li-yue-zhidu`）与大乐司（`institutions/da-yuesi`）的官制与制度史解释；本批只留「西周有专门的音乐机构，属大乐司」一句背景。
- 归 C：钟磬与铜鼓的纹样母题、编钟铭文的语词与书法、《乐律全书》的版式字体刊刻与藩王刻书制度。
- 归 A：《乐记》《乐论》《声无哀乐论》与嵇康、阮籍属音乐思想，不入本 Theme。
- 不挂载：`works/changlegong-zhong`（名含「钟」而 `sub_type` 为青铜酒器）；`terms/fou-vessel`（陶质盛酒器，器形归陶系，「击缶」只作边界）。
- 不推算：不据「44.6 吨」「约一万二千多斤」推合金用量、炉数与工时；不据「五个八度」「十二个半音」推音列、调式或律制；不据「几乎所有的键盘乐器」推音分与频率比；不据图 3-45、图 3-46、图 3-3、图 1-49 补写器形、纹样与工序（四条图版均未视觉核验）。

## 五、执行与验证

1. 语义裁决先于执行：逐条复读八音、十二平均律、朱载堉、《乐律全书》、编钟、磬、铜鼓与五件钟磬单器的 KU 正文与 `sources`，决定纳入、次挂载或边界排除；机械执行脚本 `h42_mount.py` 只消费已裁决的清单，不生成归属。
2. `python scripts/hierarchy_stress_test.py`：v1.33、25 Theme、79 Topic、620 membership、611 complete、1959 incomplete、`cross_dimension_topics` 为空（`secondary_themes` 用裸维度码 `D`、`C`，按 `hierarchy_stress_test.py:828` 的 `"." in code` 规则不计入维度集合）、`apply_permitted: false`。
3. `python scripts/build_relation_index.py`：7202→7229（explicit 5998 不变，inferred／member_of 1204→1231）。
4. `python scripts/write_current_health.py`：v1.33、complete 611、missing 1959、relation 7229、structural 130/130、ksq 57/65、content 0。
5. `python scripts/run_sync_closure.py --refresh-generated --full`：首次 18 步通过，但 health 第 8 步早于第 9 步的 output 导航重建，报 `output_navigation_snapshot_stale`（relation 7202 对 7229）；重写 health 后第二次全量闭包通过，`rule_drift` 归 0。
6. `python scripts/audit_relation_consistency.py`：broken target 0、invalid relation_type 0、missing inverse 0、weak evidence 0、isolated 1210。
7. apply-plan 23 行逐行复核 `after_sha256` 与磁盘一致；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree。

## 六、指标变化

| 指标 | v1.32 | v1.33 | 变化 |
|---|---|---|---|
| Theme | 24 | 25 | +1（B.10） |
| Topic | 77 | 79 | +2（B.10.1、B.10.2） |
| topic_memberships | 606 | 620 | +14 |
| 已完成挂载 KU | 598 | 611 | +13 |
| 未挂载 KU | 1972 | 1959 | −13 |
| B 维度未挂载 | 1256 | 1244 | −12 |
| C 维度未挂载 | 281 | 280 | −1 |
| relation_index | 7202 | 7229 | +27 |
| member_of | 1204 | 1231 | +27 |
| 隔离单元 | 1220 | 1210 | −10 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 27 = 13 条主挂载 ×（topic `member_of` + theme `member_of`）+ 1 条次挂载 × topic `member_of`。隔离单元只减 10，因为 13 个新挂载 KU 中 3 个原已有显式关系。B 维度减 12 而非 13，因为《乐律全书》的 `primary_dimension` 为 C。

## 七、语义边界（并列不裁）

- **分类层与律制层不推导**：八音给出八个材料名与两个总数（周代约 70 种、《诗经》29 种）而无器物清单；十二平均律只有两句（发明、键盘乐器依此定音）而无音分数据。两者之间没有一份按八音分目的器物清册，也没有一条把律制与任何一件乐器或一段音列连起来的记录。
- **载体层与内容层错位**：《乐律全书》在六册中以「印刷精良」的藩王刻本立条，其律学内容不在来源叙述内；本批只能证明「书存在且被记入明代刻本景观」，不能替代律制层。
- **八音是材料分类而非音阶**：这是本批的整理判断，来源未作此辨析；八音与五声、七声、十二律的关系六册亦无交代。
- **钟磬四层不成谱系**：器类定义给部件名（甬、干、枚、旋、簴、纽）与形状描述而非实测；成组与等级给数字（商三件、西周八件、天子四组至士一组）而非墓葬清点；单器量纲互不统一；工序只有一幅图注。因此不写成从商代铙到明代大钟的铸造演化线。
- **件数与官名两处照录**：曾侯乙编钟 64 与 65 两说不裁，未说明是否含楚惠王所赠镈；「大乐司」与通行《周礼》官名「大司乐」不一致，标疑照录未改；「簴」在田自秉册作「虞」为 OCR 之误，照录并已在 KU 内标注。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- `--refresh-generated --check-generated` 用于发布前比对：本批未 commit，工作区存在 23 个计划内改动，第 17 步 `audit system upgrade chain` 预期以 `exit=1` 报未提交索引／状态漂移，属预期而非失败。
- `rule_drift`：首次闭包 1 条（`output_navigation_snapshot_stale`），重写 health 后第二次闭包归 0。
- `runtime_index_snapshot_stale`：新增包目录导致第 3 步 runtime index 陈旧，同一次全量闭包内已消解。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；`check whitespace` 通过；250 tests + 16 subtests 通过。

## 九、未决事项与下一跳

- **h43 弦管线**：琴、瑟、笙、竽、笛、箫、篪、筚篥、胡笳、羌笛、琵琶、阮咸、箜篌、奚琴、羯鼓、拍鼓、腰鼓、漆双凤鼓、彩绘鹿鼓、螺钿五弦琵琶、鲁山窑瓷拍鼓、斫琴图、顾恺之 → B.10.3。B.10 至此方由「金石土」三目扩至完整八音。
- **存量结构缺口**：铁器与叠铸 Topic、货币与农具 Topic、漆器 Theme、前近代服饰与甲胄等级 Theme 仍未物化。
- **重复候选 reconcile 8 组**未处理：`works/fuhao-jade-figure` 与 `works/fuhao-mu-yuren`；`works/yudiaolong` 与 `works/da-yulong`；`terms/youlihong-ci` 与 `terms/youlihong`；`terms/bai-tao` 与 `terms/shangdai-baitao`；鲁山窑瓷拍鼓与花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` 与 `works/zhulin-qixian-rongqiqi-zhuanhua`；`terms/chunqiu-zhanguo-qingtong-chuishiqi` 与单器条；`terms/huasi` 与 `terms/hua-si-gong-yi`。
- **图注待核 12 条**、图 7-29 两指问题仍挂账。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1959、隔离 1210、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
