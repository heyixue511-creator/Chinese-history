# h59 层级试点：在 Theme B.18 下建立 Topic B.18.6「鞋履与甲胄」并主挂载 4 个 KU

- 批次：`06-runtime/automation/2026-10-31-hierarchy-pilot-h59`
- profile：`hierarchy-pilot-v1`
- 日期：2026-10-31
- 层级版本：v1.49 → **v1.50**
- apply-plan：10 行；changed_files 18

## 一、目标与范围

本批把 h56 边界登记、h58 再次点名的「鞋履与甲胄四条待建」从债务变成结构节点，B.18 至此闭合。

四条是：履的种类、云头锦鞋、花盆底鞋、皮甲。全部已在库中且全部无 `primary_theme`，本批全部作主挂载，无次挂载。B.18 待建数由 4 条减为 0。

不并入 B.18.2 的理由：B.18.2 的九条是衣装本体（上衣下裳、深衣、袍服与成衣实物），四条是足部与护具，对象不同。不并入 B.18.5 的理由：B.18.5 的六条是头、冠、发、面、肩五处的首服与妆饰，位于身体上半部；四条位于足部并含一件护具。不并入 B.9.6 的理由：Theme B.9「青铜与金属」以材质为界，B.9.6 已收汉代铠甲、明光铠、筒袖铠与造甲工序，皮甲以皮革合制、以皮条串联，材质不属金属。不并入 E.6 的理由：E.6 只管近代女装与身体改装（弓鞋与缠足的影响在本 Topic 内只作背景）。

## 二、结构物化

- **Topic B.18.6**「鞋履与甲胄：履的种类、云头锦鞋、花盆底鞋与皮甲」：`primary_dimension=B`、`parent_theme=B.18`、`secondary_themes=[D]`、`status=pilot`、`source_count=3`、`confidence=low`、`consensus=tentative`、`version=1`。
- 研究问题：**四条分处汉（舄、屦、屐按用途三分）、唐（云头锦鞋的晕絰彩条里衬）、清（旗女高木底鞋的绸缎绣花与镶珠宝）与春秋战国（皮甲的合甲、七札与甲札串联），只有汉代那一条按用途写、其余三条全按材料与工艺写，且四条无一给尺寸——足服与护具在六册里是按用途分的一条线，还是按材料与工艺分的一条线？**
- 正文七节齐备：研究问题／边界（9 条）／支撑材料（4 行表）／理论支撑（5 条）／实证材料支撑（5 条）／文献支撑（5 条）／未解决问题（10 条）。
- B.18.6 是第 107 个 Topic；B.18 累计 6 个 Topic、40 条主挂载，待建清零。

`secondary_themes=[D]` 的依据：四条中两条把鞋履写成服用场合或身体改装——履的种类按祭祀、家居、雨天践泥三分，花盆底鞋连写旗女天足与汉族缠足弓鞋的影响——D 是共同旁支。该判断只作用于 Topic 层，不回写到其余两条 KU；四条中 `terms/lv-de-zhonglei.md` 与 `terms/huapendi-xie.md` 原有 `secondary_dimensions: [D]`，按原值镜像，不算新增维度归属；`works/yuntou-jin-xie.md` 与 `terms/leather-armor.md` 无此字段，跳过不写空列表。

## 三、4 条 membership：全部为主挂载

| KU | 类型 | role | 承担什么 |
|---|---|---|---|
| [履的种类](../../../04-knowledge/units/terms/lv-de-zhonglei.md) | term | `term_anchor` | 唯一按用途分类的一条：汉代鞋履三分——「有舄，为祭祀用鞋」「屦，是家居用鞋」「屐，是雨天践泥的木制鞋子」；形制、尺寸、材质差异与等级规定全缺，来源只有一句 |
| [云头锦鞋](../../../04-knowledge/units/works/yuntou-jin-xie.md) | work | `representative_work` | 唯一给出用料名的一条：阿斯塔那出土唐代锦鞋「里衬也采用有蓝、绿、浅红等色的彩条晕絰锦」；鞋长、鞋宽、鞋头结构与鞋面鞋底材料全缺，「云头」来源未释义 |
| [花盆底鞋](../../../04-knowledge/units/terms/huapendi-xie.md) | term | `term_anchor` | 唯一给出形与饰的一条：「前圆后方为『马蹄底』」「侧面为内弧线，又称『花盆底』」，绸缎面绣花纹并镶珠宝；两名同指一鞋，木底高度与工艺未给 |
| [皮甲](../../../04-knowledge/units/terms/leather-armor.md) | term | `boundary_case` | 唯一给出工艺工序的一条：「皮甲以合甲为主」「数层皮革合制在一起，最多时可以有七甲」，「将牛皮切割成小片，然后用皮条串联起来……其连缀方法与竹简书札相似，亦称甲札」；尺寸、甲片数量与编缀图式全缺 |

- 主挂载 4、次挂载 0。B.18 至此仍是纯主挂载 Theme（40 条全部主挂载）。
- role：`term_anchor` 2、`representative_work` 1、`boundary_case` 1；类型 term 3、work 1。
- 来源（按 KU 计）：赵农 2009 二（履的种类、皮甲）、田自秉 2010 一（云头锦鞋）、夏燕靖 2016 一（花盆底鞋）；`source_count` 3。高丰 2004、夏燕靖 2009、李立新 2011 零覆盖。
- 来源重合：四条全部为单册来源，无一条跨册互证——这是 B.18 六个 Topic 中唯一的全单册 Topic。
- confidence：medium 1（皮甲）、low 3；consensus 全部 tentative。低置信占 3/4，是 B.18 六个 Topic 中证据强度最低的一个。

## 四、边界处置

`excluded_by_boundary` 已写入 manifest，七条。其中三条需要点明：

1. **皮甲归 B.18.6 而不归 B.9.6 是本批的结构判断，不是来源结论**：Theme B.9「青铜与金属」的主题边界以材质为名，B.9.6 已收汉代铠甲、明光铠、筒袖铠三种金属铠甲与造甲工序；皮甲以皮革合制、皮条串联，且本 Theme 标题「冕服、深衣、袍衫、裙制与甲胄」本就以甲胄为一项。B.9.6 的边界「甲胄与服饰等级的关系归服饰 Topic」是同向处置。**必须并列登记的是原语境**：赵农把皮甲与戈、矛、戟、殳、弩写在同一「兵器」段内，六册从未把皮革甲与铁甲并列比较；本库按材质取用并保留原段位置说明。
2. **两裆衫的对照不重复挂载**：两裆衫「形制缘起于铠甲」归 B.18.3，皮甲条以 `boundary_case` 入 B.18.6，两者在 Theme 层对照而不在同一 Topic 内并置；本批不把两裆衫次挂到 B.18.6，以免制造跨 Topic 的重复入账。
3. **身体改装与制度只作背景**：缠足与弓鞋对旗女的影响、旗女天足与汉族缠足的对举在条目内照录，身体改装归 E.6、制度与习俗问题归 D，与本条的问题（足服按什么分类）分开。

**待建登记**：无。B.18 六个 Topic 全部建立，四十条全部主挂载。

## 五、执行与验证

- 写回：`h59_mount.py` 输出 `mounted 4 bad []`；frontmatter 复核 4/4 全部 `primary_theme: B.18`、各含 1 条 `topic_memberships`（`primary: true`）、`updated` 全部为 2026-10-31、`version` 各 +1、无残留 `尚未 materialize` 占位。
- 索引升版四处：`hierarchy/index.md` → v1.50（Level 4 106→107、B.18 下 5→6、Level 5 868/1702/882、追加 v1.50 段）；`themes/README.md`（B.18 改 6 个 Topic／40 KU、补 B.18.6、覆盖数改、新增足服与护具段、结尾改待建清零）；`topics/README.md`（107、B.18 下 6 个、新增 B.18.6 全段）；`dimension-candidates.md`（五十九批 868、B 未挂载 987、全库 1702）。**旧版先归档**为 `hierarchy/archive/v1.49.md`（109201 字节），再编辑 index.md。
- 实测：`hierarchy_stress_test.py` 报 themes 33、topics 107、membership 882、complete 868、incomplete 1702、`apply_permitted: false`；`build_relation_index.py` 7748（explicit 5998、inferred 1750、3/67）；`audit_relation_consistency.py` broken 0、invalid 0、missing inverse 0、weak evidence 0、isolated 1057、over-connected 10；`write_current_health.py` structural 130/130、ksq 58/65（`hierarchy_assignment` 3/10）、`system_p0=0`。B 维度未挂载实测 987（`primary_dimension` 为 B 且无 `primary_theme` 计数）。
- **一处本批自纠**：Theme 实证段初稿把 role 分布写成「`term_anchor` 30、`boundary_case` 2」，实为 `term_anchor` 31、`boundary_case` 1（皮甲）；断代序列初稿把「春秋战国（皮甲）」误置于元代之后，已按时间轴移到西周与战国之间。两处均在 apply-plan 生成前改正，哈希所记为改正后状态。
- **一处工具细节**：`works/yuntou-jin-xie.md` 与 `terms/leather-armor.md` 的 `secondary_dimensions` 为空（null），镜像时跳过而不写空列表，与 h58 处理 `terms/fozhuang.md` 的口径一致。
- **生成态次序**：manifest 与 summary 先落盘，再连跑两次 `run_sync_closure.py --refresh-generated --full`；第 8 步早于第 9 步，单跑会残留 `output_navigation_snapshot_stale`。
- `--check-generated` 为 17 步，第 17 步 `git diff --exit-code HEAD` 在未 commit 时必然 exit=1，属预期。

## 六、指标变化

| 指标 | v1.49 | v1.50 | 变化 |
|---|---|---|---|
| Theme | 33 | 33 | 0 |
| Topic | 106 | **107** | +1 |
| topic_memberships | 878 | **882** | +4 |
| complete assignments | 864 | **868** | +4 |
| incomplete assignments | 1706 | **1702** | −4 |
| double-mount KU | 14 | 14 | 0 |
| relation index | 7740 | **7748** | +8 |
| member_of / inferred | 1742 | **1750** | +8 |
| explicit | 5998 | 5998 | 0 |
| 隔离单元 | 1061 | **1057** | −4 |
| B 维度未挂载 | 991 | **987** | −4 |
| structural health | 130/130 | 130/130 | 0 |
| ksq | 58/65 | 58/65 | 0 |

- relation 增量 8 = 4 条主挂载 ×（topic `member_of` + theme `member_of`），与实测一致。
- **隔离单元减 4 是整数**：本批四条挂载前全部为隔离单元，无 h58 那种「原本已有显式关系」的例外，取自 `audit_relation_consistency.py` 前后两次实测（1061→1057）。
- B.18 累计：6 Topic、40 KU（term 32／work 8；`term_anchor` 31、`representative_work` 8、`boundary_case` 1）；六册分布为夏 2016 十六、赵 16、夏 2009 十三、田 6、高丰 2、李 2；confidence medium 31／low 9。

## 七、语义边界：并列不裁与不做的事

本批的判断仍是「并列照录」而非「择优裁定」：

1. **足服与护具成材料工艺线，不成用途线**：四条中只有汉代履的种类以服用场合为分类标准（舄、屦、屐），其余三条全按材料与工艺写。这不能反推六册「没有用途分类」，只能记「本批所见用途分类只有起点一条」；本库只记「本批未见」，不记「原书未载」。
2. **尺寸全缺，可数的只有层数**：皮甲的「七甲」是皮革层数，「七札」是札数，来源先言层数后言札数、单位不同而未调和。本库并列两个计量对象，不代为统一，也不把「七札」当作甲片数的记载。
3. **皮甲的归属是结构判断而非来源结论**：本次按 Theme B.9 的材质边界与本 Theme 的甲胄项把皮甲归 B.18.6，并在边界、未解决问题与 manifest 三处自陈；若日后 B.9.6 改为跨材质收甲胄，本条的归属应重估而非默认沿用。
4. **「连缀」只作词面接触，不作谱系证据**：皮甲「连缀方法与竹简书札相似」与两裆衫「在肩部用布带连缀」共用一词并按身体部位配置，但两册分属不同作者与章节、从未互引。本库只并列，不据此建立源流关系。
5. **两名同指一鞋靠来源自证**：花盆底鞋的「马蹄底」（前圆后方的底面）与「花盆底」（侧面内弧线）是同一双鞋的两种描述，来源未明说同物；本库按上下文并列，并在未解决问题中登记「若他书以此为两种鞋式，本条的合并需重估」。

不做的事：不从名目推形制。履的三种鞋式、云头锦鞋的鞋头云形、花盆底的木底高度、皮甲的甲片尺寸与编缀图式在六册中全无，本库不据「前圆后方」「云头」「合甲」复原任何一件；也不把 B.18.2 素纱禅衣的尺寸口径借给足服——不同类别，不跨条回填。

## 八、生成态与门禁

- 次序：apply-plan、manifest、summary 先落盘，再跑闭包。
- 全量闭包连续两次后，`rule_drift.findings` 归 0、backlog 为「No active items」。
- `--check-generated` 17 步，第 17 步 exit=1 属预期（未 commit）。
- apply-plan 10 行逐行 `after_sha256` 与磁盘复核一致（10/10）。
- 保护路径 `02-sources/` 零改动；分支 `main`、单一 worktree。
- **本包不 commit、不 push**——commit/push 需用户当次明确授权。

## 九、未决事项与下一跳

本批 10 条 unresolved 已写入 `manifest.json`，要点归四类：

**用途与尺寸类**
- 用途分类只有汉代一条且只有一句：形制、尺寸、材质（仅屐明言木制）与等级规定全缺，汉代以后鞋履如何分类六册不载。
- 尺寸全线缺失：无鞋长、鞋宽、底高、鞋头高度，也无甲片尺寸与甲片数量；唯一数量「最多七甲」是皮革层数，与「七札」是否同一制度来源未说明。

**归属与名实类**
- 皮甲与金属铠甲分处两个 Theme，六册从未并列比较；本批处置为结构判断，须随 B.9 边界变化重估。
- 「七甲」与「七札」是否同指未裁（层数与札数、单位不同）。
- 花盆底鞋两名同物靠来源自证；云头锦鞋的「云头」不释义，只知里衬。

**证据与断代类**
- 图版未核且不对题：图 9-21 未核，图 3-6、3-7 是铜戈图而非皮甲图；履与云头锦鞋无图。
- 断代不连续：四条各占春秋战国、汉、唐、清一段，秦汉之间、魏晋至明四段零覆盖。
- 覆盖最薄且低置信：三条来源、四条全单册，low 占 3/4，是 B.18 六个 Topic 中证据强度最低的一个。

**结构自陈类**
- 足服与护具之间无一条连接（履不讲甲、皮甲不讲鞋）；Theme 层唯一的连接是「连缀」一词，且只在护具—衣裳之间。

**下一跳优先级**：跨批文本回改批次（B.14.7 → B.17.1、B.12.2／B.13.2／B.5.3 → B.16.1、B.12 → B.15、B.9「货币归后续 Topic」→ B.13、B.14.3 边界材料侧 → B.14.7、B.9.6「甲胄与服饰等级」→ B.18，其中 B.9.6 一句因 B.18 闭合已成为可回改对象）→ 重复候选 reconcile 9 组 → 图注待核 12 条与未核图版（5-32、8-57、8-58、10-48、图 4-32「铁犁」归属）→ A 维度遗留（A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》）。
