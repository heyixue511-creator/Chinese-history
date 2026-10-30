# h37 批次摘要：B.9 青铜与金属（B.9.1 器形与礼器组合、B.9.2 铸造工艺）

## 一、目标与范围

本批新建 Theme B.9「青铜与金属：器形、铸造与装饰」，下建 B.9.1「青铜器形与礼器组合：鼎簋鬲甗与酒器序列」与 B.9.2「铸造工艺：合范、浑铸、分铸、失蜡与六齐」两个 Topic，并主挂载 20 个 KU。

基线为 v1.27：23 Theme、71 Topic、514 membership、507 complete assignments、2063 个 KU 未挂载、relation index 7019、隔离单元 1268。本批不动 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`，不改写任何既有 KU 的正文证据，只新增层级字段与「在层级体系中的位置」段。

B.9 是 B 维度第五条前近代 Theme（前四条为 B.5 陶器、B.6 瓷器、B.7 玻璃、B.8 玉石），选材依据是 `dimension-candidates.md` 自 v1.24 起反复登记的「青铜器形序列」候选与 218 个青铜相关未挂载 B 维度 KU。

## 二、结构物化

### 新建 B.9「青铜与金属：器形、铸造与装饰」

- `primary_dimension: B`、`secondary_dimensions: [C, D]`、`source_basis` 为六册，`date: 2026-10-29`。
- 四层「材料—器形—组合—工序」：材料层有两种合金定义（高丰铜锡铅合金／田自秉红铜加锡）而无一件成分检测；器形层有九类容器的定义与分期，九类中只有爵与壶有尺寸；组合层有九鼎八簋、列鼎三说与两套礼器名称，全部出自礼书引文而无一座墓葬的完整组合；工序层有合范五步、范铸八阶段、浑铸／分铸／焊接、失蜡与六齐，而泥料配比、焙烧温度、浇注温度与成品率全无。
- 边界 9 条：陶器器形归 B.5、玉礼器归 B.8、纹样与铭文归 C、礼制制度史归 D.6、兵器乐器铜镜货币农具归后续 Topic、铁器与叠铸归后续金属 Topic、十类合条不挂载；并声明「青铜器不等于礼器」。
- 支撑 20 个 KU（term 13、work 3、procedure 4；`term_anchor` 13、`representative_work` 3、`procedure` 4）；未解决问题 13 条。

### 新建 B.9.1「青铜器形与礼器组合：鼎簋鬲甗与酒器序列」

- `parent_theme: B.9`、`primary_dimension: B`、`secondary_themes: [C, D]`，`research_question` 183 字，`date: 2026-10-29`。
- 三层「形制定义—序列演变—礼制配置」：形制定义有实物可指（鼎的腹足耳、簋的圆腹圈足、豆的盘柄圈足），序列演变有器名可系（鼎的腹深浅与足形、鬲的深腹到横宽、壶的贯耳到半环耳），礼制配置只有文本（九鼎八簋、列鼎奇数、簋偶数）。
- 三条限度：器名不等于器类（鼎的两套三分、簋的方座与三足式是否同类未说明）、数字不等于组合（九鼎八簋无墓葬实例，高丰另有「一说用十二鼎」）、单件不等于序列（杜岭方鼎、何尊、莲鹤方壶分属商早期、西周早期、春秋中期，不能排成演变线）。
- 边界 10 条：陶器器形归 B.5、玉礼器归 B.8、纹样归 C、铭文归 C、制度史归 D.6、兵器乐器铜镜货币农具归后续、十类合条不挂载；并声明器形序列按「食器—炊器—酒器—盛食器」排列而非年代序列。
- 支撑 14 个 KU（term 11、work 3），全部主挂载；未解决问题 15 条。

### 新建 B.9.2「铸造工艺：合范、浑铸、分铸、失蜡与六齐」

- `parent_theme: B.9`、`primary_dimension: B`、`secondary_themes: [C, D]`，`research_question` 180 字，`date: 2026-10-29`。
- 三层「材料—工序—参数」：材料有文本配比（六齐六条）、工序有名称与顺序（合范五步、八阶段、浑铸／分铸／焊接、失蜡程序）、参数完全没有（泥料配比、焙烧温度、浇注温度、范块数、成品率）。
- 三条限度：工序名不等于工序（五步与八阶段都只是名称排列）、顺序不等于因果（田自秉三段递进与李立新次序说相反排列）、实物不等于工艺（曾侯乙尊盘、淅川下寺铜禁只有器名与年代，无范块、浇口与合金数据）。
- 边界 8 条：陶器成形归 B.5、叠铸与铁器归后续、焊接接口与装饰工艺归后续、纹样与铭文归 C、作坊组织归 D.6；并声明「工序名与工序顺序是两回事」。
- 支撑 6 个 KU（term 2、procedure 4），全部主挂载；未解决问题 12 条。

### 既有结构更新

- `hierarchy/index.md` v1.27→v1.28；`archive/v1.27.md` 为改动前原样副本（52,655 字节，逐字节一致，`sha256:5427cb28baf2d0af67db4d026f2a18d68393c58a8de9da10f1e6ac002bd973ee`）。
- `themes/README.md`（23→24，新增 B.9 段：四层、20 个主挂载、五处不裁）、`topics/README.md`（71→73，B.9 下 2 个，B.9 两 Topic 分工段）、`dimension-candidates.md`（第三十六批 507→第三十七批 527，新增 B.9 bullet，材料组清单移除青铜与金属，B 维度未挂载 1347→1327，全库 2063→2043）同步。

## 三、20 个 KU 的挂载

| KU | 类型 | role | Topic | version |
|---|---|---|---|---|
| `terms/qingtongqi.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/qingtong-liqi.md` | term | `term_anchor` | B.9.1 | 2→3 |
| `terms/ding.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/gui-vessel.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/li-cauldron.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/yan-steamer.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/jue-vessel.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/gu-vessel.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/zun-vessel.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `terms/hu-vessel.md` | term | `term_anchor` | B.9.1 | 2→3 |
| `terms/dou-vessel.md` | term | `term_anchor` | B.9.1 | 1→2 |
| `works/du-ling-fang-ding.md` | work | `representative_work` | B.9.1 | 1→2 |
| `works/he-zun.md` | work | `representative_work` | B.9.1 | 1→2 |
| `works/lianhe-fanghu.md` | work | `representative_work` | B.9.1 | 1→2 |
| `terms/qingtong.md` | term | `term_anchor` | B.9.2 | 1→2 |
| `terms/liuqi.md` | term | `term_anchor` | B.9.2 | 1→2 |
| `procedures/hefan-fa.md` | procedure | `procedure` | B.9.2 | 2→3 |
| `procedures/hunzhu-fa.md` | procedure | `procedure` | B.9.2 | 1→2 |
| `procedures/fenzhu-fa.md` | procedure | `procedure` | B.9.2 | 1→2 |
| `procedures/lost-wax-casting.md` | procedure | `procedure` | B.9.2 | 3→4 |

- 20 个均为首次挂载、均为主挂载：写入 `primary_theme: B.9`、`secondary_themes: []`、`role_in_theme`、一条带 `primary: true` 与 `scope_note` 的 `topic_memberships`；`hierarchy_scope_note` 与 `scope_note` 逐字相同并保持为 frontmatter 末字段；正文「在层级体系中的位置」为六行段。
- 三个原有 `secondary_dimensions` 的 KU（鼎 D／C、杜岭方鼎 C、何尊 C）保留原字段，位置在 `topic_memberships` 之后、`hierarchy_scope_note` 之前，顺序符合字段契约。
- 所有 KU 的正文证据、`sources`、`confidence`、`consensus` 未改动；只更新 `version`、`updated` 与层级字段。

scope 摘要：青铜器只取合金定义、时代上限、最早铜刀与权力象征；青铜礼器只取礼器定义、陈设取向与成套礼制；鼎只取定义、分期、三足三解、两套三分与列鼎三说；簋只取盛食器形与方座；鬲只取袋足、起源三说与两线演变；甗只取甑鬲合成与上下分铸；爵只取五爵、二里头最早容器与长流爵尺寸；觚只取喇叭口与圈足小铃；尊只取盛酒器与鸟兽形尊；壶只取贯耳到半环耳与钟钫之名；豆只取盘柄圈足与盖翻置；杜岭方鼎只取两件方鼎的形制与纹饰；何尊只取西周早期锚点与图版；莲鹤方壶只取莲瓣立鹤与高度两说；青铜（材料）只取两种合金定义与性能；六齐只取六条配比、17% 换算与实测对照；合范法只取五步、别名、八阶段与一模翻数范；浑铸法只取整体浇铸与编钟实例；分铸法只取部件先铸、两套次序与鼎耳例证；失蜡法只取程序、1:10 比例、两处实物与上限两说。

## 四、边界处置

| 对象 | 处置 | 理由 |
|---|---|---|
| 春秋战国青铜炊食器（十类合条） | 不挂载，留待 reconcile | 与鼎、壶、豆、簋、甗等单器条目重叠，合条与单条不能同时计入两层 |
| 叠铸技术（`procedures/diezhu-jishu`） | 不挂载 | 实物为东汉温县烘范窑车马器泥范，属铁器工艺，不属青铜容器铸造 |
| 陶鼎、陶鬲、陶甗、陶豆 | 归 B.5 | 本批只取青铜器形，陶器器形只作来源线索 |
| 玉礼器（璧、琮、圭） | 归 B.8 | 不把玉礼器与青铜礼器连成一条组合线 |
| 青铜器纹样（饕餮、蟠龙、云雷） | 归 C | 本批只取来源对纹样的著录事实 |
| 青铜器铭文（含何尊「中国」） | 归 C | 何尊只作西周早期器物锚点 |
| 列鼎制度的政治功能、官营作坊 | 归 D.6 | 本批只取礼书所记数字与器类名称 |
| 兵器、乐器、铜镜、货币、农具 | 留后续 B.9 Topic | 本批只取容器与铸造 |
| 铁器、生铁冶铸、铁范 | 留后续金属 Topic | 材料与工序均不属青铜 |

## 五、执行与验证

- `scripts/hierarchy_stress_test.py` 在升版前实测：themes 24、topics 73、topic_memberships 534、complete_assignments 527、incomplete_assignments 2043、themes_without_topics 0、cross_dimension_topics []、apply_permitted false。
- `scripts/build_relation_index.py` → 7059 条（explicit 5998、inferred_by_rule 1061、migrated_from_related 0）。较基线 +40：20 条新 membership 各生成 1 条 topic `member_of`（+20），20 个主挂载另各生成 1 条 theme `member_of`（+20）。`b9-` 相关边 40 条。
- `scripts/write_current_health.py` → v1.28、complete 527、missing 2043、relation 7059、isolated 1263、structural_health 130、knowledge_structure_quality 57/65、rule_drift 0、system_p0 0。
- `apply-plan.jsonl` 28 行（1 theme create、2 topic create、20 `hierarchy_mount`、5 `structure_index_update`），闭包后复核 28/28 哈希与磁盘一致。
- 隔离单元由 1268 减至 1263：20 个新挂载中 5 个原无显式关系，其余 15 个已因既有术语互引而进入关系图。
- knowledge_structure_quality 由 56/65 升至 57/65，增量来自 `hierarchy_assignment`（挂载覆盖率提高），其余分项不变。

## 六、指标变化

| 指标 | v1.27 基线 | v1.28 结果 |
|---|---|---|
| Theme | 23 | 24 |
| Topic | 71 | 73 |
| Topic membership | 514 | 534 |
| 完成五级挂载 KU | 507 | 527 |
| 未挂载 KU | 2063 | 2043 |
| relation index | 7019 | 7059 |
| member_of | 1021 | 1061 |
| 隔离单元 | 1268 | 1263 |
| structural_health | 130 | 130 |
| knowledge_structure_quality | 56/65 | 57/65 |
| 库存 KU | 2570 | 2570 |

## 七、语义边界

1. 九类器形的分期来自夏燕靖 2016 器类表与田自秉、高丰的简版，三者分段与术语不完全对应，本库不合成统一类型学序列。
2. 九鼎八簋、七鼎六簋、五鼎四簋全部出自礼书引文；六册没有给任何一座墓葬的完整组合，本库不用礼书数字讨论具体墓葬的等级。
3. 列鼎三说并列不裁：高丰「卿大夫七鼎」与田自秉、夏燕靖的「诸侯七、卿大夫五」不一致，高丰另有「一说用十二鼎」；三说不能同时成立，也不取一说为准。
4. 鼎的「列鼎即最早系列化设计」是高丰的设计史判断，其依据「一模数范、母模子模递减」是工艺推断，六册无范的实物计数与尺寸序列。
5. 三件器物（杜岭方鼎、何尊、莲鹤方壶）分属商早期、西周早期与春秋中期，不能排成一条器形演变线；莲鹤方壶的「划时代意义」是六册共同的风格判断，不是形制序列的节点。
6. 何尊只有图版与铭文引述，器形、尺寸、出土与藏地全无；本库不据铭文讨论「中国」词义史（归 C）。
7. 合范法五步与范铸八阶段不是同一颗粒度：八阶段含选矿与初炼，五步只含铸造成形；两者可以并置，但都不能支持工艺复原。
8. 浑铸、分铸、焊接的先后两说相反，本库不裁先后，只记录分歧；同一件司母戊鼎在四册中的三种工艺定性并列保留。
9. 失蜡法的宋代记载（赵希鹄《洞天清禄集》）原文未用「失蜡法」一词，本库按程序归入，不把原文称谓改写为「失蜡」。
10. 六齐的换算基准（合金总量／纯铜）在五册中未声明，高丰的 17% 换算、田自秉的司母戊鼎实测与六条配比不能逐条对应；本库不裁定六齐是否成立。
11. 兵器、乐器、铜镜、货币、农具与铁器均未建 Topic，本库不因 B.9 建立而声称青铜器或金属工艺已覆盖。

## 八、生成态与门禁

- `hierarchy/index.md` 升版并归档 `archive/v1.27.md`（52,655 字节，与改动前逐字节一致，`sha256:5427cb28baf2d0af67db4d026f2a18d68393c58a8de9da10f1e6ac002bd973ee`）。
- `relation-index.yml`、`current-health.json`、`governance-backlog.md`、`generated-projections-manifest.json`、`06-runtime/automation/index.md` 等生成态文件由刷新步骤重建，不在 apply-plan 内。
- `run_sync_closure.py --refresh-generated --full` 实测 `sync closure passed`：18/18 步通过，pytest 250 passed、16 subtests passed。首次闭包后 `rule_drift` 记 1 条（05-outputs 导航仍写 relation 7019），系第 8 步写 health 早于第 9 步重建导航的固定顺序所致；重跑 `write_current_health.py` 清零后再次全量闭包，`rule_drift` 稳定为 0，`structural_health` 130、`knowledge_structure_quality` 57/65。
- `relation-index.yml` 复核 7059 条：`member_of` 1061、`supports_claim` 2999、`supported_by` 2999；含 `b9-` 的边 40 条。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动。
- `apply-plan.jsonl` 闭包后逐行复核：28 行，28/28 `after_sha256` 与磁盘字节一致，0 缺失、0 失配。
- 本批未 `git add`、未 commit、未 push；`git log` 仍停在 `c249c6fe`。

## 九、未决事项与下一跳

- 未决：青铜成分无实测；时代起点只有一句且铜刀无测定；九类器形只有爵与壶有尺寸；列鼎三说无墓葬组合校验；礼器两套名称不能对应；三足三解与四点式无实测；鬲起源三说不可裁；甗孔数与孔径未给；杜岭方鼎与何尊信息过薄；莲鹤方壶年代与高度两说；浑铸／分铸次序两说；司母戊鼎三种定性；失蜡法上限两说与 1:10 比例无验证；合范法全部参数缺失；六齐基准未声明；十类合条与单器条重叠未合并。
- 下一跳候选：B.9 装饰工艺 Topic（错金银、镶嵌、刻划、金银平脱、三叠法）；B.9 铜镜 Topic（汉镜、规矩镜、唐镜、宋镜、透光镜）；B.9 兵器 Topic（戈、矛、钺、剑、戟、弩）；B.9 乐器 Topic（编钟、八音、十二平均律）；铁器与叠铸 Topic（生铁冶铸、铁范、叠铸）；重复候选 reconcile 6 组（妇好墓玉雕人俑 vs 玉人、玉雕龙 vs 大玉龙、youlihong 釉里红 2 条、白陶 2 条、鲁山窑瓷拍鼓 vs 花釉腰鼓、竹林七贤砖 2 条）；制陶生产组织 Topic；汉代及以后玉器线评估；图注单条待核 12 条；存量债务（未挂载 2043、单源、tentative、低置信、隔离 1263）。
- 本批不 commit、不 push；commit 与 push 须用户当次明确授权。
