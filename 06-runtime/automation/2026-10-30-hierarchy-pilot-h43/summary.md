# h43 弦管与鼓线：B.10.3「弦管与鼓：丝竹匏革四目的乐器与鼓器」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h43/`
- 基线：v1.33（25 Theme／79 Topic／620 membership／611 complete／1959 incomplete／relation 7229／member_of 1231／isolated 1210／ksq 57/65／structural 130）。
- 目标：物化 h42 留待的 **B.10.3 弦管与鼓**，把八音中丝、竹、匏、革四目的乐器与鼓器挂入 B.10，并把 B.10、B.10.1、B.10.2 中三处「留待 B.10.3」回填为已承接。
- 结果：v1.34（25 Theme／80 Topic／639 membership／629 complete／1941 incomplete／relation 7266／member_of 1268／isolated 1198／ksq 57/65／structural 130）。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Topic `04-knowledge/structure/topics/b10-xianguan-yu-gu-sizhu-paoge-simu-de-yueqi-yu-guqi.md`：`node_type: topic`、`primary_dimension: B`、`parent_theme: B.10`、`secondary_themes: [D, C]`、`status: pilot`、`date: 2026-10-30`、`research_question` 179 字、25 个 tags；七节齐备（研究问题／边界／支撑材料／理论支撑／实证材料支撑／文献支撑／未解决问题），支撑材料表 19 行。
- 直属分工：B.10.1 回答「六册把乐器分成什么、记到哪一层」，B.10.2 回答「钟磬四层记载各自能证到什么程度」，B.10.3 回答「丝竹匏革四目的乐器与鼓器各按什么方式立条、这些条目能否连成器物序列」。三者不是前后阶段，来源分别出自赵农的乐器节与明代印刷节、田自秉的器类定义与单器段加李立新的《天工开物》插图、赵农「乐器」各节加田自秉漆器与螺钿章节。
- 分工形式与 B.10.2 不同：B.10.2 按「器类定义—成组与等级—单器体量—工序图像」四层排器物序列，B.10.3 按「名称与族属—出土器物—图注与画名」三种证据形态分层；该差异在 Theme 理论支撑段与 `themes/README.md` 同时登记，Theme 因此同时容纳两种组织方式，二者不可互相推导。
- 三处存量表述回填：Theme B.10 边界「弦管乐器与革类鼓归后续 B.10.3」改为「已由 v1.34 的 B.10.3 承接」；B.10.1 边界与未解决问题末条、B.10.2 边界同步改写；B.10.1 末条由「丝竹匏革木五类均无条目、只有金石土三目有实例」改为「金石土由本试点承接、丝竹匏革由 B.10.3 承接、唯木一目无任何对应条目」。
- 快照：`hierarchy/index.md` 归档为 `hierarchy/archive/v1.33.md`（63501 字节，先复制、`cmp` 逐字节一致后再改 index.md）。

## 三、19 个 KU 挂载

主挂载 18 个（`primary_theme: B.10`，`version` 1→2，`role_in_theme` 与 membership 同值）：

- 名称与族属层 `term_anchor` 12：琴、笙、竽、笛、羌笛、胡笳、筚篥、琵琶、阮咸、箜篌、奚琴、羯鼓（`04-knowledge/units/terms/`）。
- 出土器物层 `representative_work` 3：彩绘鹿鼓、漆双凤鼓、螺钿五弦琵琶（`04-knowledge/units/works/`）。
- 边界层 `boundary_case` 3：骨笛（terms）、鲁山窑瓷拍鼓、斫琴图（works）。

次挂载 1 个：

- 花釉腰鼓（`works/huayou-yaogu.md`）：`version` 2→3，保留 `primary_theme: B.6`，追加 `primary: false` 的 B.10.3 membership（`representative_work`），只取「陶瓷中的鼓形器」一面；`hierarchy_scope_note` 末尾登记「已次挂载 B.10.3（…），主挂载仍为 B.6.1」。

类型与角色：term 13、work 6（含 1 条次挂载）；`term_anchor` 12、`representative_work` 4、`boundary_case` 3。`primary_dimension` 全部为 B，无新增跨维度挂载。

## 四、边界处置

- 乐器内部：分类与律制归 B.10.1，金石两目与铜鼓归 B.10.2，弦管与鼓归 B.10.3；同一 KU 不重复计入两个 Topic 的主挂载。
- 花釉腰鼓双层：主挂载 B.6.1 取釉色、斑纹与器类（唐代花釉代表作），B.10.3 次挂载只取鼓形器一面；釉色分类与窑口判定仍归 B.5.4 与 B.6。
- 不设条目：瑟、箫、篪在全库无 KU；排箫、方响、锣、钹、星、达卜、齐鼓、担鼓在来源叙述中出现但无独立条目，均记为缺口、不据名称补条。
- 骨笛：骨质不属金、石、土、革、丝、木、匏、竹八类，以 `boundary_case` 登记，既是竹以外的管类实例，又标记八音分类边界；不据测音复原音列。
- 不挂载：`works/changlegong-zhong`（名含「钟」而 `sub_type` 为青铜酒器）；`places/zenghouyi-tomb`（编钟出土单位，归 B.10.2 地域挂载）；`institutions/shosoin`（正仓院，制度侧归 D）；`persons/gu-kai-zhi`（画史与人物评价归 C，本批只取「相传……可见南方制作乐器工序的严格」一句）。
- 归 B.9：青铜容器器形与礼器组合（B.9.1）、合范浑铸分铸失蜡六齐（B.9.2）。
- 归 D：礼乐制度与大乐司的官制与制度史解释。归 C：纹样母题、钟磬铭文、乐器图像与《斫琴图》的画史解释。归 A：乐论思想与琴人思想。
- 不推算：不据「36 簧」「九孔」「四弦十二柱」推音域、调式或律制；不据「鼓径 1.4 厘米」修正其与鹿高 28 厘米的比例；不据「相传顾恺之」补画面与工序；图 5-32、图 3-45、图 6-11 等图版均未视觉核验。

## 五、执行与验证

1. 语义裁决先于执行：逐条复读 13 个名称条目、5 件器物与《斫琴图》的 KU 正文与 `sources`，决定纳入、次挂载或边界排除；机械执行脚本 `h43_mount.py` 只消费已裁决的清单与 `scope_note`，不生成归属。
2. 自审修正（写回前）：新 Topic 的研究问题段原写「18 个主挂载……第一层 12 条」合计仅 17，改为 13 条并补骨笛整句；未解决问题中「名称层 12 条中 11 条没有形制数据」与竽、筚篥、阮咸有数字冲突，改为「除三处数字外其余 9 条」；`terms/ruan-xian.md` 的 `scope_note` 笔误修正；`works/huayou-yaogu.md` 的 `hierarchy_scope_note` 双括号修正。
3. 写后复核实测：`h43_src.py` 显示 19 条来源为赵农 2009 14、田自秉 2010 4、夏燕靖 2016 1，与 Topic 内原写「赵农 13」不符，遂在 Topic 的实证材料支撑与文献支撑、Theme 的文献支撑与分工段、`dimension-candidates.md` 一并改为 14，并修掉名称层「无数据」清单中误列筚篥、漏列奚琴的问题。
4. `python scripts/hierarchy_stress_test.py`：v1.34、25 Theme、80 Topic、639 membership、629 complete、1941 incomplete、`cross_dimension_topics` 为空（`secondary_themes` 用裸维度码 `D`、`C`，按 `hierarchy_stress_test.py:828` 的 `"." in code` 规则不计入维度集合）、`apply_permitted: false`。
5. `python scripts/build_relation_index.py`：7229→7266（explicit 5998 不变，inferred／member_of 1231→1268）。
6. `python scripts/write_current_health.py`：v1.34、complete 629、missing 1941、relation 7266、structural 130/130、ksq 57/65、content 0。
7. `python scripts/audit_relation_consistency.py`：broken target 0、invalid relation_type 0、missing inverse 0、weak evidence 0、isolated 1198。
8. `python scripts/run_sync_closure.py --refresh-generated --full` → `--refresh-generated --check-generated`：结果见第八节。
9. apply-plan 28 行逐行复核 `after_sha256` 与磁盘一致；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree。

## 六、指标变化

| 指标 | v1.33 | v1.34 | 变化 |
|---|---|---|---|
| Theme | 25 | 25 | 0 |
| Topic | 79 | 80 | +1（B.10.3） |
| topic_memberships | 620 | 639 | +19 |
| 已完成挂载 KU | 611 | 629 | +18 |
| 未挂载 KU | 1959 | 1941 | −18 |
| B 维度未挂载 | 1244 | 1226 | −18 |
| C 维度未挂载 | 280 | 280 | 0 |
| relation_index | 7229 | 7266 | +37 |
| member_of | 1231 | 1268 | +37 |
| 隔离单元 | 1210 | 1198 | −12 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 37 = 18 条主挂载 ×（topic `member_of` + theme `member_of`）+ 1 条次挂载 × topic `member_of`。隔离单元减 12 而非 18，因为 18 个新挂载 KU 中 6 个原已有显式关系。B 维度减 18，因为 18 条主挂载的 `primary_dimension` 全部为 B；花釉腰鼓已计入原库存，其次挂载只增加 membership、不减少未挂载数。

## 七、语义边界（并列不裁）

- **三层证据形态不换算**：名称与族属层 13 条全部出自赵农 2009「乐器」各节；出土器物层 3 件全部出自田自秉 2010 的漆器与螺钿章节；图注与画名层只有鲁山窑瓷拍鼓一条图注与《斫琴图》一句。名称层与器物层没有一件乐器共指，工序层只有《斫琴图》一句，因此不写成从史前骨笛到宋代奚琴的乐器演化线。
- **四组数字不成序列**：竽 36 簧、筚篥九孔、阮咸四弦十二柱分属匏、竹、丝三目三种乐器，彩绘鹿鼓的鹿高、身长与鼓径属另一件漆木器；四组之间既非同器演进，也无测量口径说明。
- **骨笛的八音归属**：舞阳 18 支七孔骨笛约 8000 年、河姆渡数十支二至三孔，骨质不属八类，只作边界登记；它同时说明八音是材料分类而非器物清单。
- **重复候选诚实保留**：鲁山窑瓷拍鼓（只有图注）与花釉腰鼓（主挂载 B.5.4）同为唐代河南窑口瓷鼓，本批分列并登记为合并候选；琵琶与阮咸（汉琵琶）在名称层部分重叠，本批分列不合并；阮咸与竹林七贤同名，得名缘由无载。
- **八音七目有实例、木目无条目**：但七目中除金石两目较厚，其余五目多为单条名称条目，不能据「七目有实例」判断八音在实际器物中的分布。
- **两处照录**：筚篥段首「算篥」标疑未改；竖箜篌「约公元 2 世纪从朝鲜传到中原」照录不改西域说。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- `--refresh-generated --check-generated` 用于发布前比对：本批未 commit，工作区存在 28 个计划内改动，第 17 步 `audit system upgrade chain` 预期以 `exit=1` 报未提交索引／状态漂移，属预期而非失败。
- `rule_drift` 与 `runtime_index_snapshot_stale`：新增包目录与 relation 数变化分别触发运行索引与 output 导航的快照陈旧，同一次全量闭包内消解；细节见本节末尾的实测记录。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；250 tests + 16 subtests 通过。

## 九、未决事项与下一跳

- **B.10 收口后的缺口**：八音「木」一目在六册中无任何对应器物条目；丝、竹、匏、革四目虽有实例但多为单条名称条目，形制数据合计只有四组。
- **存量结构缺口**：铁器与叠铸 Topic、货币与农具 Topic、漆器 Theme、前近代服饰与甲胄等级 Theme 仍未物化。
- **重复候选 reconcile 8 组**未处理：`works/fuhao-jade-figure` 与 `works/fuhao-mu-yuren`；`works/yudiaolong` 与 `works/da-yulong`；`terms/youlihong-ci` 与 `terms/youlihong`；`terms/bai-tao` 与 `terms/shangdai-baitao`；鲁山窑瓷拍鼓与花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` 与 `works/zhulin-qixian-rongqiqi-zhuanhua`；`terms/chunqiu-zhanguo-qingtong-chuishiqi` 与单器条；`terms/huasi` 与 `terms/hua-si-gong-yi`。本批新增候选：`terms/pi-pa` 与 `terms/ruan-xian`。
- **图注待核 12 条**、图 7-29 两指问题仍挂账；本批新增未核图版：图 5-32（阮咸，所指为人物）。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1941、隔离 1198、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
