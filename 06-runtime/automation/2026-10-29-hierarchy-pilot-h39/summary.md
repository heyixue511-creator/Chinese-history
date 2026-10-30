# h39 金属表面装饰线：B.9.4「金属表面装饰：印纹、镶嵌、错金银、鎏金与刻划」

## 一、目标与范围

本批在既有 Theme B.9「青铜与金属：器形、铸造与装饰」内新建第四个 Topic B.9.4「金属表面装饰：印纹、镶嵌、错金银、鎏金与刻划」，并主挂载 18 个金属装饰工序与器物 KU。不改 B.9.1／B.9.2／B.9.3 的既有挂载，不新建 Theme，不新建 Dimension。

范围限定为六册 Markdown 文本中的金属表面装饰材料：八条工序（印纹、三叠法、青铜镶嵌、错金银与错铜、错石、鎏金、刻划、金银平脱）与十件器物（栾书缶、水陆攻战纹鉴、错金银龙凤鹿方案、错金博山炉、错金银鸟篆文壶、金银错狩猎纹铜车饰、越王勾践剑、鎏金铜酒樽、鎏金舞马衔杯银壶、雕金镶玉银带钩）。

基线：v1.29（24 Theme／74 Topic／547 membership／540 complete／2030 incomplete／relation 7085／member_of 1087／isolated 1258／ksq 57/65／structural 130）。

## 二、结构物化

`04-knowledge/structure/topics/b9-jinshu-biaomian-zhuangshi-yinwen-xiangqian-cuojin-liujin-kehua.md`

- `node_type: topic`、`parent_theme: B.9`、`primary_dimension: B`、`secondary_themes: [C, D]`、`status: pilot`、`date: 2026-10-29`。
- `research_question` 183 字（171–185 区间内），以「四路能否排成工序序列」与「各章命名是否只是表面处理」为问题骨架。
- 七节 body：研究问题 / 边界（12 条）/ 支撑材料（18 行表格）/ 理论支撑 / 实证材料支撑 / 文献支撑 / 未解决问题（20 条）。
- 四路组织：铸前制模（印纹、三叠法）—铸后嵌饰（青铜镶嵌、错金银与错铜、错石）—表面镀饰（鎏金）—铸后刻饰（刻划）；金银平脱作漆胎与金银箔结合的跨材质边界（`boundary_case`）。
- 命名理由：不叫「金属装饰工艺」或「错金银」，因为六册提供的是分属四条工序时点的名称与器物锚点，而不是一条按年代或工序排列的装饰序列；「金属表面装饰」保留材料的表面处理范围，副题列出五组名称。

## 三、18 个 KU 挂载

全部为主挂载，`primary: true`；`secondary_memberships` 为 0。

| KU | 类型 | role | 承担什么 |
|---|---|---|---|
| `procedures/yin-wen-mo-yin` | procedure | `procedure` | 商周器模雕纹到春秋印纹的转折、一模多用、四周衔接、单独纹样—二方连续—四方连续的格式变化 |
| `procedures/san-die-fa` | procedure | `procedure` | 商代后期刻花三层花纹定义：主纹、地纹之外在较粗花纹上再勾刻细线；无器物实例 |
| `procedures/qingtong-xiangqian` | procedure | `procedure` | 青铜镶嵌总类与松石、红铜、金银丝三类嵌料，春秋红铜镶嵌与战国金银错的时段差异 |
| `procedures/cuo-jin-yin-cuo-tong` | procedure | `procedure` | 错金银与错铜定名、春秋中期发展、栾书缶错金铭文、燕赵蔡错铜、刻槽嵌入磨错工序与厝石释名 |
| `procedures/turquoise-inlay` | procedure | `procedure` | 错石定义：绿松石以漆汁粘嵌铜器錾槽打磨；越王勾践剑剑格兽面纹为唯一实例 |
| `procedures/liujin` | procedure | `procedure` | 金汞齐、涂器、炭火烤汞的鎏金工序，一比七金泥配比，战国中期已应用 |
| `procedures/kehua` | procedure | `procedure` | 战国铁工具出现后以刻刀直接刻铜的线刻装饰、辉县宴乐铜鉴等四例与「细如毫发」线条 |
| `procedures/jinyin-pingtuo` | procedure | `boundary_case` | 漆胎与金银箔结合：剪刻、胶漆粘贴、髹漆研磨推光与「平脱／平文」之别，只作跨材质边界 |
| `works/luanshu-fou` | work | `representative_work` | 春秋错金铭文 40 余字，错金银工艺的早期实物锚点 |
| `works/shuilu-gongzhan-jian` | work | `representative_work` | 战国红铜镶嵌战争场景、约 300 人、1935 年汲县山彪镇出土、藏台湾 |
| `works/cuo-jinyi-longfenglu-fangan` | work | `representative_work` | 战国中山王墓四鹿四龙四凤结构与错金银装饰；尺寸与出土年份两说并列 |
| `works/cuojin-boshanlu` | work | `representative_work` | 西汉满城汉墓炉体错金云气纹与「汉代博山炉典型」评价 |
| `works/cuojin-yin-niaozhuanwen-hu` | work | `representative_work` | 西汉满城汉墓遍体鸟虫文字与两句铭文，错金银与文字装饰结合的实例 |
| `works/jinyincuo-shouliewen-tongcheshi` | work | `representative_work` | 1965 年定县汉墓竹管轮节四段、金银错与圆形菱形绿松石镶嵌、26.5×3.6 厘米 |
| `works/yuewang-goujian-jian` | work | `representative_work` | 只取剑格错石（绿松石漆汁嵌錾槽）；蓝色琉璃、珐琅釉两说并列 |
| `works/liujin-tong-jiuzun` | work | `representative_work` | 汉代右玉鎏金铜酒樽的鎏金表面与腹部两带动物纹、高 24.5／口径 23.4 厘米 |
| `works/liujin-wuma-xianbei-yinhu` | work | `representative_work` | 盛唐何家村舞马局部鎏金、锤揲皮囊形与「十三两半」墨书 |
| `works/diaojin-xiangyu-yin-daigou` | work | `representative_work` | 战国辉县固围村包金镶嵌与蟠龙鹦鹉浮雕；「雕金」与「包金镶嵌」关系无载 |

## 四、边界处置

- 青铜容器的器形、礼器组合与铭文内容归 B.9.1；本 Topic 只取器物上的装饰工序。
- 合范、浑铸、分铸、失蜡、六齐与焊接归 B.9.2；印纹与三叠法虽在制模阶段，只作表面装饰工序处理，不重复合范五步。
- 铜镜的型式、纹样与铸镜归 B.9.3；唐镜七种装饰只在工序名称处引用，不重复挂载铜镜器物。
- 纹样母题、图像叙事、铭文书法与文例归 C；官营作坊、工官、匠役与生产组织归 D.6。
- 铁器冶铸、铁范、叠铸、生铁柔化与炒钢归后续铁器 Topic；刻划只在「铁工具提高」一句处引用铁器。
- 陶瓷刻花、划花、印花、彩绘与釉装饰归 B.5／B.6；漆器的髹漆、描金、戗金、螺钿、雕漆、剔犀、百宝嵌归后续漆器 Theme；金银平脱只作跨材质边界。
- 花丝、金细工艺、景泰蓝、银熏炉制作与唐代金银器谱系归后续 B.9.5。
- 兵器形制、防锈与合金成分归后续兵器 Topic；越王勾践剑只取剑格错石。
- 四路不是年代序列：同一时代可同时存在多条路线，来源未给同一器物的工序叠加证据。
- 不据「薄」「细」「流畅」推算槽深、丝径、金层厚度或工时；六册唯一工艺配比是鎏金一比七，唯一具体尺寸是车饰 26.5×3.6 厘米、酒樽高 24.5／口径 23.4 厘米、舞马壶通高 18.5 厘米。

## 五、执行与验证

1. `scripts/hierarchy_stress_test.py`：v1.30、2570 KU、24 Theme、75 Topic、565 membership、558 complete、2012 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`（试点态）。
2. `scripts/build_relation_index.py`：7121 条（explicit 5998、inferred_by_rule 1123、migrated 0），类型覆盖 3/67。
3. `scripts/write_current_health.py`：v1.30、complete 558、missing 2012、relation 7121、isolated 1247、structural 130/130、ksq 57/65、rule_drift 0、system_p0 0。
4. 18 个 KU 逐一复核：`primary_theme: B.9`、恰好 1 条 `topic_memberships`、role 与计划一致、frontmatter 与 body 各恰好 1 个 `hierarchy_scope_note`、`updated: 2026-10-29`。
5. Topic 复核：`node_type: topic`、`parent_theme: B.9`、`research_question` 183 字、七节齐备、支撑表 18 行。
6. 文档复核：Topic 75、B.9 下 4 个、B.9 主挂载 51 KU、全库未挂载 2012；`topics/README.md` 的 B.9.4 段已移至四 Topic 分工段内。

## 六、指标变化

| 指标 | v1.29（基线） | v1.30（结果） | 变化 |
|---|---:|---:|---:|
| Theme | 24 | 24 | 0 |
| Topic | 74 | 75 | +1 |
| Topic membership | 547 | 565 | +18 |
| 完成挂载 KU | 540 | 558 | +18 |
| 未挂载 KU | 2030 | 2012 | −18 |
| relation index | 7085 | 7121 | +36 |
| `member_of` | 1087 | 1123 | +36 |
| 隔离单元 | 1258 | 1247 | −11 |
| structural health | 130/130 | 130/130 | 0 |
| knowledge structure quality | 57/65 | 57/65 | 0 |

relation 增量 36 = 18 条 topic `member_of` + 18 条 theme `member_of`。隔离单元只减 11，因为 18 个新挂载 KU 中 7 个原已有显式关系。

## 七、语义边界（并列不裁）

1. **四路不能排成工序序列**：六册从未在同一件器物上比较两种装饰工序，也无「铸前—铸后—镀饰—刻饰」的先后记载；四路是整理框架，不是来源结论。
2. **错金银起始三说**：夏燕靖「春秋中期有所发展」、赵农「春秋时期创立」、田自秉「春秋战国时期的新创造」；「发展」「创立」「新创造」是否同一判据，来源未说明。
3. **青铜镶嵌起点两说**：夏燕靖「商周开始出现镶嵌绿松石」、田自秉「春秋战国时期流行」；是否同一类嵌饰，来源未说明。
4. **鎏金起始两说**：赵农「战国中期已应用」、田自秉字段「春秋战国」；田自秉正文只给工序与配比，未给起始年代。
5. **印纹盖印时机两说**：夏燕靖「模胎尚未冷却」、田自秉「模胎尚未全干」；「冷却」与「全干」是否同一状态、印模是陶是木，来源未说明。
6. **「错石」一名两指**：田自秉的「错石（厝石）」是磨错用的细砂岩，赵农的「错石工艺」是绿松石嵌饰；两条 KU 已分列，不合并。
7. **越王勾践剑同一处嵌饰三说**：蓝色琉璃和绿松石、剑格兽面纹错石、剑柄珐琅釉；部位、材料与工艺三层混写，本批只取剑格错石。
8. **鎏金铜酒樽器名两存**：高丰称「酒樽」并记口径 23.4 厘米，田自秉称「铜奁」并记盖、活环、铺首耳与三兽足；两名不裁。
9. **金银平脱与贴金银／包金银三说**：夏燕靖作同义，高丰并列为三种特种工艺，田自秉单列并以「平文」区别；本批作 boundary_case，不并入工序序列。
10. **错金银龙凤鹿方案三处分歧**：出土年份 1977／1997、尺寸两套、案面材质与结构描述不一致；三项并列，不据一说不裁另一说。

## 八、生成态与门禁

- `scripts/run_sync_closure.py --refresh-generated --full` 首次执行 18 步闭包（250 tests + 16 subtests）通过，但 `rule_drift` 记为 1，唯一 finding 为 `output_navigation_snapshot_stale`（`05-outputs/index/index.md` 仍记 relation 7085，期望 7121）。
- 按生成态顺序陷阱处置：重跑 `scripts/write_current_health.py` 后再执行一次全量闭包，18 步通过，`rule_drift` 归 0。
- `--refresh-generated --check-generated` 执行 17 步，第 17 步 `[17/17] FAILED (exit=1)`；原因为工作区尚未提交，与 h38 先例一致，不作为本批失败。
- apply-plan 24/24 行逐一复核 `after_sha256` 与磁盘字节一致（0 处不符）。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 在 `git status` 中零改动。
- `06-runtime/automation/index.md` 已收录 h39；本批不 commit、不 push；HEAD 仍为 `c249c6fe`，分支仍为 `main`，无额外 worktree。

## 九、未决事项与下一跳

- 20 条未解决问题见 Topic 的「未解决问题」节与 `manifest.json.unresolved`，集中于工序参数缺失、起始时段多说、同名异说与来源分布不均。
- 7 条单源：三叠法、青铜镶嵌、错石、刻划、错金银鸟篆文壶、金银错狩猎纹铜车饰、雕金镶玉银带钩。
- 来源分布：田自秉覆盖 15 条；高丰 2004 册无工序专条；李立新只覆盖 2 条；夏燕靖两版与赵农补足其余。
- 下一跳：B.9.5 金银器与珐琅 Topic（花丝、金细工艺、景泰蓝、银熏炉、唐代金银器谱系）；其后为兵器 Topic、乐器 Topic、铁器与叠铸 Topic。
- 存量债务不变：全库未挂载 2012、隔离 1247、单源与低置信条目按既有 backlog 处理。
- 重复候选 reconcile 6 组、图注单条待核 12 条仍按既有清单排队，不在本批处理。
