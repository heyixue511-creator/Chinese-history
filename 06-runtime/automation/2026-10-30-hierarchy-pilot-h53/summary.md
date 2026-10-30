# h53 层级试点：另立 Theme B.15「水利工程：灌溉、航运与治水经验」并建立 Topic B.15.1

- 批次：`06-runtime/automation/2026-10-30-hierarchy-pilot-h53`
- profile：`hierarchy-pilot-v1`
- 日期：2026-10-30
- 层级版本：v1.43 → **v1.44**
- apply-plan：14 行；changed_files 22

## 一、目标与范围

本批只做一件事：把前六册中全部可挂的水利条目从「无 Theme 可挂的工程组」里取出，另立 Theme **B.15**，并在其下建立唯一 Topic **B.15.1**。

选择另立 Theme 而不是并入 B.12，理由来自 B.12 主题文件本身的边界：B.12 明文写「排除：水利工程——都江堰、郑国渠、灵渠、西门渠属灌溉工程与土木营造，归待建水利 Topic 或 B.3，本 Theme 只取器具而不取工程」。本批闭合的正是这一句，以及 h50、h51、h52 三份 summary 第九节连续登记的「水利 Topic」下一跳。

不并入 B.12 的实质理由：B.12 的分工原则是「是否改变水系」——B.12 取提水与灌水的器具（翻车、辘轳、桔槔），B.15 取改变水系的工程。这一刀是结构性的，不是数量凑合。

## 二、结构物化

- **Theme B.15**「水利工程：灌溉、航运与治水经验」：`theme_code=B.15`、`primary_dimension=B`、`secondary_dimensions=[D]`、`status=pilot`、`source_basis` 六册。正文五节：核心问题三问、边界九条、下属 Topic、支撑结构四层、未解决问题十一条。
- **Topic B.15.1**「先秦至秦的灌溉与航运工程：都江堰、郑国渠、西门渠与灵渠」：`primary_dimension=B`、`parent_theme=B.15`、`secondary_themes=[D]`、`status=pilot`、`source_count=1`。研究问题：**四条工程各有主持者、年代、一句效果与至多一句结构，唯一的口诀化知识只出自都江堰——「水利工程在六册里是以『工程』被写，还是以『人物的功绩』被写？」** 正文七节齐备，支撑材料 8 行。

层级主轴仍为 `domain → dimension → theme → topic → KU`；B.15 是第 30 个 Theme、B.15.1 是第 98 个 Topic。

**只有一个 Topic 是库存限制，不是取舍。** 前六册中汉代以后的水利条目（白渠、龙首渠、大运河、圩田、海塘）均未立条，因此不按朝代切第二个 Topic，也不为凑结构制造占位 Topic。

## 三、8 个 KU 挂载

全部 8 条 `primary_dimension` 均为 B，主挂载到 B.15.1，`primary_theme=B.15`，`secondary_themes=[D]`。

| KU | 类型 | role | 出处 |
|---|---|---|---|
| [都江堰](../../../04-knowledge/units/works/dujiangyan.md) | work | `representative_work` | 赵农 2009 L2060/L2062/L2066 |
| [郑国渠](../../../04-knowledge/units/works/zhengguo-canal.md) | work | `representative_work` | 赵农 2009 L2068/L2070 |
| [西门渠](../../../04-knowledge/units/works/ximen-canal.md) | work | `representative_work` | 赵农 2009 L2072 |
| [灵渠](../../../04-knowledge/units/works/ling-qu.md) | work | `representative_work` | 赵农 2009 L2723/L2725 |
| [李冰](../../../04-knowledge/units/persons/li-bing.md) | person | `key_person` | 赵农 2009 L2060-L2070 |
| [郑国](../../../04-knowledge/units/persons/zheng-guo.md) | person | `key_person` | 赵农 2009 L2068/L2070 |
| [西门豹](../../../04-knowledge/units/persons/ximen-bao.md) | person | `key_person` | 赵农 2009 L2072 |
| [史禄](../../../04-knowledge/units/persons/shi-lu.md) | person | `key_person` | 赵农 2009 L2723-L2725 |

- role：`representative_work` 4、`key_person` 4；类型 work 4、person 4。
- 来源：赵农 2009 8 条；高丰 2004、夏燕靖 2009、田自秉 2010、李立新 2011、夏燕靖 2016 五册零覆盖。单册 8 条，无跨册。
- confidence：medium 7、low 1（史禄）；consensus 全部 tentative。
- 断代：战国 6 条、秦 2 条。

四条工程与四位主持者严格一一对应，不拆成两个 Topic——来源的叙述单位就是「某人主持某项工程」，拆开会使两条边的任一侧失去所指。

## 四、边界处置

`excluded_by_boundary` 已写入 manifest，八条：提水机具（B.12.2）、农具与耕作（B.12）、其他土木营造、制度与治理（D 维度）、水利图像与图籍、治水神话与礼俗、简单机械（待建线）、近代水利与水电（无对象）。

其中两条需要点明：

1. **简单机械**（`terms/lever`、`terms/pulley`）仍无落点。二者与 B.13 的权衡原理、B.12 的提水器具都有关联，但既未另立 Theme 也未并入既有 Topic；本批明确不取，登记为独立债务。
2. **B.12 的文件本身未回改**：其排除句仍写「归待建水利 Topic 或 B.3」，需改指向 B.15。本批不改动 B.12 的正文，属于跨批文本维护，登记为 debt 而非顺手补。

## 五、执行与验证

- 写回：`h53_mount.py` 输出 `mounted 8 bad []`；frontmatter 复核 roles `{representative_work: 4, key_person: 4}`、types `{work: 4, person: 4}`、conf `{medium: 7, low: 1}`、docs `{2009-zhaonong…: 8}`。
- 索引升版四处：`hierarchy/index.md` → v1.44（Theme 29→30、Topic 97→98、Level 5 813/1757/823）；`themes/README.md`（新增 B.15 全段）；`topics/README.md`（98、新增 B.15.1 全段）；`dimension-candidates.md`（五十三批 813、B 未挂载 1042、全库 1757）。旧版归档为 `hierarchy/archive/v1.43.md`（89763 字节）。
- 实测：`hierarchy_stress_test.py` 报 themes 30、topics 98、membership 823、complete 813、incomplete 1757、`cross_dimension_topics` 为空、`apply_permitted: false`；`build_relation_index.py` 7634（explicit 5998、inferred 1636、3/67）；`audit_relation_consistency.py` broken 0、invalid 0、missing inverse 0、weak evidence 0、isolated 1094、over-connected 10；`write_current_health.py` structural 130/130、ksq 58/65（hierarchy_assignment 3/10）、content 0、`system_p0=0`。
- **生成态次序**：`run_sync_closure.py --refresh-generated --full` 的第 8 步（write health and backlog）早于第 9 步（build output gallery and navigation），relation 数变化后**单跑一次仍会残留 `output_navigation_snapshot_stale`（P0）**，必须**连续跑两次**才能让 `rule_drift.findings` 归 0。本批按此处理。
- `--check-generated` 为 17 步，第 17 步 `check generated snapshots`（`git diff --exit-code HEAD`）在未 commit 时必然 FAILED exit=1，属预期，不是失败。

## 六、指标变化

| 指标 | v1.43 | v1.44 | 变化 |
|---|---|---|---|
| Theme | 29 | **30** | +1 |
| Topic | 97 | **98** | +1 |
| topic_memberships | 815 | **823** | +8 |
| complete assignments | 805 | **813** | +8 |
| incomplete assignments | 1765 | **1757** | −8 |
| structure node coverage | 2/4 | 2/4 | 0 |
| relation index | 7618 | **7634** | +16 |
| member_of / inferred | 1620 | **1636** | +16 |
| explicit | 5998 | 5998 | 0 |
| 隔离单元 | 1100 | **1094** | −6 |
| B 维度未挂载 | 1050 | **1042** | −8 |
| structural health | 130/130 | 130/130 | 0 |
| ksq | 58/65 | 58/65 | 0 |
| content findings | 0 | 0 | 0 |

口径说明：relation +16 = 8 条 ×（topic `member_of` + theme `member_of`）。隔离单元减 6 而非 8，取自前后两次 `audit_relation_consistency.py` 实测（8 条中有 2 条原有显式关系），不是按条数推算。

## 七、语义边界：并列不裁

本批有三处判断是「并列照录」而非「择优裁定」，需在 summary 明写：

1. **「西门渠／漳水十二渠」名实并列**：来源在同一段把二者并称，未说明是同一工程的总名与分名，还是主持者名与渠系名的并称；「十二渠」是否确为十二条渠也无说明。本库不裁。
2. **效果语言的「地／路」两分是本库读法**：三条灌溉渠的效果都落在土地产出，灵渠的效果落在水系连通与航运。来源从未把四条并列比较，灵渠的行政配套（桂林、广州、雷州半岛设治）还被写在同一段。分类是读法，不是来源的判断。
3. **三处文本异常照录**：都江堰条「都江水利」与「都江堰」并存、L2062 与 L2066 之间被页眉隔断（「被后人加以继」／「承」）；郑国渠条「气奄息息」疑为「气息奄奄」、「进入秦国内向秦王嬴政建议」疑脱句读。八条中三条带文本问题，比例高于本库其他 Theme；均未据来源外知识改写。

同样重要的是**不做什么**：不从口诀反推工程参数。「深掏滩，低作堰」「水竭不见足，盛不没肩」两句在来源中只作经验总结出现，未与鱼嘴、飞沙堰、宝瓶口的任何尺寸或高程对应，本库不据口诀补写参数。

## 八、生成态与门禁

- 次序：manifest 与 summary **先落盘**，再跑闭包；否则 `automation/index.md` 会记录旧的 manifest 字节数，触发 `runtime_index_snapshot_stale`。
- 全量闭包连续两次后，`rule_drift.findings` 归 0、backlog 为「No active items」。
- `--check-generated` 17 步，第 17 步 exit=1 属预期（未 commit）。
- 保护路径 `02-sources/` 零改动；分支 `main`、单一 worktree；HEAD 仍为 `c249c6fe`。
- **本包不 commit、不 push**——commit/push 需用户当次明确授权，历史授权与工作惯例均不替代。

## 九、未决事项与下一跳

本批新增 14 条 unresolved，均写入 `manifest.json`，要点归四类：

**证据结构类**
- 八条全部出自赵农 2009 的两处文本，其余五册零覆盖；水利工程在六册中是赵农的叙述对象而非共同对象。
- 郑国渠与西门渠零结构：渠首、渠线、断面、比降、闸堰形制全部未载，「工程怎样做」在这两条上不可回答。
- 都江堰的「无坝引水」与灵渠的「船闸」仅有的两项技术判断，均无结构细节支撑。

**量化类**
- 无一条给灌溉面积、土方量、工役人数、断面与比降；量化只有三个年代、一处长度（灵渠 33 公里）与一处工期（都江堰六年）。

**制度与人物类**
- 四位主持者身份各异（行政长官二人、技术人员一人、无官职记载一人），来源未讨论身份与工程成败的关系，也未记载任何组织形态。
- 制度与治理面全部未物化：蜀郡太守、邺令、秦设岭南行政机构均指向 D 维度，水利行政与漕运不在 D.6 官府手工业六点之内。

**跨批债务**
- B.12 主题文件边界仍写「归待建水利 Topic 或 B.3」，未回改指向 B.15。
- 简单机械线（`terms/lever`、`terms/pulley`）仍无 `primary_theme` 与 `topic_memberships`。
- 汉代以后的水利条目在六册中零覆盖，B.15 只覆盖战国至秦约四十年，不能代表整部水利史。

**下一跳优先级**：简单机械线 → 竹编工艺方法（`procedures/zhubian-yishu-jiagong`）落点 → 前近代服饰与甲胄等级 Theme。B.15 内部在六册库存内已无第二个 Topic 可建，不做无对象扩展。
