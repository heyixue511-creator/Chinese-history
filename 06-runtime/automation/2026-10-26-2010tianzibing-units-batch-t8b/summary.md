# 2010 册 units 批次 T8b（隋唐后半）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-26-2010tianzibing-units-batch-t8b/`
- 来源：田自秉《中国工艺美术史（修订本）》（2010），doc_id `2010-tianzibing-zhongguo-gongyi-meishushi`
- 候选范围：第七章隋唐的工艺美术后半（L3248-L3467）的 unit 候选 19 条
- 裁定结果：新建 17 条、更新 1 条、no_delta 1 条、rejected 0 条
- 状态：applied（19 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：第七章隋唐的工艺美术后半（L3248-L3467），含刺绣（神丝绣被、卢眉娘）、金属工艺（铜镇纸、景云二年大钟、金银器、银薰炉、论语玉烛）、铜镜（海兽葡萄纹、双鸾衔绶纹、图案组织五式、装饰加工、铭文、合金比例、规格）、漆器（金银平脱、平文、螺钿、雕漆、库路真、制胎）、家具（木画、挟轼、棋局、双六局、桌、椅）与其他工艺（牙雕、石雕），至卷草、牡丹与唐代结语止。
- 截断点：L3246 为百鸟毛裙条末，已由 T8a 处理；L3468 起为第八章宋代，归下一批。
- 本批候选的 source span 并集经工作包计算覆盖 L3248-L3467；`manifest.json.inputs.source.spans` 记 `[[3248, 3467]]`。
- 插图 13、16、17 与相关彩版只读图注，未视觉核验。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-08-63 | 神丝绣被 | create | `works/shensi-xiu-bei.md` |
| cand-08-64 | 卢眉娘 | create | `persons/lu-meiniang.md` |
| cand-08-66 | 唐代铜镇纸 | create | `works/tang-dai-tong-zhenzhi.md` |
| cand-08-67 | 唐睿宗景云二年铭文大钟 | create | `works/jingyun-er-nian-dazhong.md` |
| cand-08-70 | 唐代银薰炉 | create | `works/tang-dai-yin-xunlu.md` |
| cand-09-02 | 涂金龟负“论语玉烛” | create | `works/lunyu-yuzhu.md` |
| cand-09-04 | 海兽葡萄纹 | create | `terms/haishou-putao-wen.md` |
| cand-09-05 | 双鸾衔绶纹 | create | `terms/shuangluan-xianshou-wen.md` |
| cand-09-06 | 唐镜图案组织五式 | create | `terms/tangjing-tuzhi-wushi.md` |
| cand-09-09 | 平文 | no_delta | `procedures/jinyin-pingtuo.md` |
| cand-09-13 | 螺钿五弦琵琶 | create | `works/luodian-wuxian-pipa.md` |
| cand-09-17 | 库路真 | create | `terms/kuluzhen.md` |
| cand-09-19 | 木画 | create | `terms/muhua.md` |
| cand-09-21 | 唐代木画棋局 | create | `works/muhua-qiju.md` |
| cand-09-94 | 双六局 | create | `terms/shuangliu-ju.md` |
| cand-09-23 | 《萧翼赚兰亭图》 | create | `works/xiaoyi-zhuan-lanting-tu.md` |
| cand-09-25 | 大智禅师碑 | create | `works/dazhi-chanshi-bei.md` |
| cand-09-26 | 卷草（唐草） | update | `terms/tangcao-wen.md` |
| cand-09-93 | 牡丹 | create | `terms/mudan.md` |

## 4. 新建 17 条

**刺绣与人物（2）**：神丝绣被、卢眉娘。

**金属工艺（4）**：唐代铜镇纸、景云二年大钟、唐代银薰炉、涂金龟负“论语玉烛”。

**铜镜纹样与分类（3）**：海兽葡萄纹、双鸾衔绶纹、唐镜图案组织五式。

**漆器（3）**：螺钿五弦琵琶、库路真、木画。

**家具与博戏（3）**：唐代木画棋局、双六局、《萧翼赚兰亭图》。

**碑刻与纹样（2）**：大智禅师碑、牡丹。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，日期 created/updated/last_verified 为 2026-10-26、review_due 为 2027-04-26，`academic_translation_status` 均为 provisional。confidence：17 条均为 medium（每条均有来源原句支撑的形制、纹样或制度描述，缺项已逐项标未载）。

## 5. 语义判断与内部张力

1. **卷草名称两说并列，不裁断**：2016 册称通称卷草纹、因盛行于唐代故名唐草纹；2010 册称由于在唐代盛行，日本人称为“唐草”。两册对“唐草”一名的来源表述不同，`terms/tangcao-wen.md` 两说并录，不改写任何一册，也不把日本称名写成唯一来源。
2. **卷草补源流，不覆盖 2016 结构描述**：2010 册补汉代已有、六朝石刻边饰的三片一叶分列、唐代叶片卷曲与叶脉旋转、牡丹主花、明中期以后莲花串枝；2016 册的 S 形波状、二方连续与取材描述保留，两册层级不同（结构 vs 源流），并列而非互校。
3. **平文不另立条**：L3388 的平文句已由 `procedures/jinyin-pingtuo.md` 收入，且候选无工序、工具、实物与产地，单独立条只会与平脱条重复；记 no_delta，材料保留在原条。
4. **库路真不归入平脱**：来源只据《新唐书·地理志》记襄州土贡、鲜卑语名称、二十品乘与花文五乘、“天下以为法”与“襄样”，并明言不知其具体内容；本段未说库路真属平脱或何种做法，条目不作技法归属断言。原文“库路真”一词被排版分断为 L3400 末“库路”与 L3402 首“真系鲜卑语”，条目照录并说明，不据分行改字。
5. **木画用材照录，不采初稿误记**：来源 L3415 明记木画用染色的象牙、鹿角、黄杨木，非沉香、桑寄生；初稿曾据常见木画定义误写四类用材，已在生成前的语义复核中改正。木画与螺钿（贝壳片）、平脱（金银片）材料不同，三条分列。
6. **棋局与双六局分开**：L3425 同段并称二者为唐代流行的娱乐家具，但棋局明记用木画装饰雉、雁、狮、象、鹿及胡人牵驼，双六局只记长方形、月牙门、十二花眼，新疆所出为螺钿双六棋盘；故木画归 `terms/muhua.md` 与 `works/muhua-qiju.md`，双六局单立 `terms/shuangliu-ju.md`，不把双六局写成木画器。
7. **《萧翼赚兰亭图》以家具史料立条**：来源 L3429 明记作者阎立本、唐太宗遣监察御史骗取辨才所藏《兰亭序》真迹、辨才坐高背竹椅，并引《唐语林》颜鲁公立藤子事，结论竹椅和藤椅唐代早期已使用。条目主维度取 B（家具）、C 为次，与 `works/buniantu.md` 的 B 类先例一致；画题叙事不作为书法流传史证据，与 `works/lan-ting-ji-xu.md` 分工。
8. **大智禅师碑纹样名从来源**：L3442 称碑侧花纹用卷曲波折的牡丹构成带状花边，未称卷草；条目照录牡丹，不代改为卷草，只与 `terms/tangcao-wen.md` 互指。碑主法号、立碑年代、撰书人与碑高均未载，不据碑刻常识补写。
9. **牡丹条兼收三处**：L3464 给唐人所爱赏、异名、国色天香、赏花风习与“卷草以牡丹为主体”的社会原因；L3458 给植物纹多以牡丹为主题；L3462 给唐代卷草多以牡丹为主花。三处层次不同，条目并列并逐处标注行号。
10. **螺钿五弦琵琶只写来源所见**：L3392 只列正仓院所藏螺钿花鸟纹镜、螺钿紫檀琵琶、螺钿紫檀阮咸与五弦琵琶最精，并录《正仓院考古记》的背板描述；来源未给四弦四柱、通长、弦制与入藏经过，初稿曾据琵琶通制误写四弦四柱，已在语义复核中删除。不另建《正仓院考古记》出版物条，避免与 `institutions/shosoin.md` 重复。
11. **镜纹三条分工**：`terms/tangjing.md` 记唐镜总类与断代；`terms/haishou-putao-wen.md` 记海兽葡萄纹的满花构图与过梁葡萄；`terms/shuangluan-xianshou-wen.md` 记双鸾衔绶的绶寿谐音与千秋节关联；`terms/tangjing-tuzhi-wushi.md` 记田自秉的五式分类。四者互指，不合并为单一唐镜条。
12. **双鸾衔绶纹与双鸾瑞兽葵花镜不合并**：`works/shuangluan-ruishou-kuihua-jing.md` 器名作双鸾瑞兽、未提衔绶，来源亦未说二者同器；只作相关条目互指，不视为同一实体。
13. **单器条只记来源所给**：铜镇纸、景云二年大钟、银薰炉、论语玉烛四条的尺寸、重量、出土地、藏地与图版多有缺项，逐项标未载；银薰炉只记机环与活轴结构，不据现代机械常识补写原理细节。
14. **图版与插图处理**：插图 13（双鸾衔绶纹相关）、16（皮胎八角漆镜盒）、17（大智禅师碑石刻花纹局部）只读图注，未视觉核验，条目不据图像补写尺寸、纹样分布与藏地。
15. **候选 unit_type 与实体性质一致**：本批 17 个新建候选的 unit_type 均与实体性质相符（纹样与工艺类型记 term，单器与单幅画作记 work，人物记 person），无需改写。

## 6. 生成态与门禁

- 结构审计：`_zn_struct.py` 对 18 个文件（17 新建 + 1 更新），0 问题（13 个 frontmatter 字段、六节正文、ASCII 引号、悬空反引号链接、日期与状态字段均通过）。
- 引文审计：`_zn_checklines_t8b.py` 覆盖 17 个新建条目、82 处双引号逐字引文与田自秉 2010 册源文去标点比对，0 遗漏、0 越界、0 行号错配。
- 全库引文审计：`_zn_audit.py` 对 18 个文件（含更新条）0 条发现。
- 索引重建：`build_discovery_index.py` 后 total 5339 不变；applied 2521→2539、needs_evidence 1748→1729、no_delta 218→219、rejected 852 不变；terminal 3591→3610、active 1748→1729。`build_translation_index.py` 后 translation index 1880 条（T8a 后 1863，+17）；知识元 2272 条（T8a 后 2255，+17 新建）。
- 工作包：apply-plan 18 行（17 create、1 update）、candidate-decision-ledger 57 行（19×3）、canonical-mapping 19 条、manifest 1 份。工作包在 candidate-index 写回前构建，`counts_before` 与 `sha256_before` 为写回前真实值（needs_evidence 1748、applied 2521、rejected 852、no_delta 218，rows 5339）。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18 步全部通过（250 tests passed, 16 subtests passed）。运行日志开头有一条读取子进程输出的 `UnicodeDecodeError: 'gbk' codec` 线程异常，来自 Windows 子进程读取线程，未导致任何步骤失败，18 步 exit 均为通过。
- `python scripts/run_sync_closure.py --refresh-generated --check-generated`：实测 [17/17] check generated snapshots FAILED exit=1，因本批与既有未提交知识元、生成态快照未提交，记 `blocked_pending_commit`，属设计行为。

## 7. 跨批修正

- 本批初稿有 4 个条目的引文与来源不符，均由 `_zn_checklines_t8b.py` 报出后改正：螺钿五弦琵琶原写“四弦四柱，腹部为覆手”，来源无此句；库路真原写“是一种平脱漆器”，来源未作技法归属；木画原写沉香、桑寄生与“木画和金银平脱并用”，来源只记染色的象牙、鹿角、黄杨木；大智禅师碑原写“流丽工整”“装饰性较强”，来源作“最典型的作品”“花叶繁茂，形态丰满”。另有《萧翼赚兰亭图》《牡丹》《双六局》等条目的引文按来源原句重写。以上均在生成前修正，未进入正式条目。
- `terms/tangcao-wen.md` 原 `term_note` 称“来源明确通称卷草纹”，只对 2016 册成立；本批改为两册并录，并注明 2010 册的日本称名说。
- `terms/tangcao-wen.md` 原 scope_note 与正文只称“唐代染织纹样”；本批补碑刻边饰源流后改为“唐代装饰纹样”，避免把条目范围窄化为染织。
- 未改动本批以外的知识元。`procedures/jinyin-pingtuo.md` 正文 L78、L83、L89 仍有 ASCII 双引号，属该条既有文本，不在本批范围，留待后续 lint 或该条所属批次修正。

## 8. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- 2010 册 unit 候选剩余量：宋 37、元 16、明 38、清 43、近代 38 条；claim 候选 278 条未启动。本批 L3248-L3467 范围内另有 15 条 claim 候选仍为 needs_evidence，留给 claim/evidence 流程。
- 神丝绣被的尺寸、地色、针法、绣工与藏地未载；卢眉娘的生卒、师承、针法与绣作存佚未载。
- 唐代铜镇纸的尺寸、重量、兽种与藏地未载；景云二年大钟的通高、口径、钟纽、铭文与铸地未载；银薰炉的尺寸、重量、出土地与所据实物未载；论语玉烛的尺寸、涂金范围、酒筹长度与藏地未载。
- 海兽葡萄纹的葡萄与海兽数目、镜径与年代序列未载；双鸾衔绶纹的镜径、鸾鸟细部与出土实例未载；唐镜五式的年代序列、数量比例与镜例清单未载。
- 螺钿五弦琵琶的通长、弦制、螺钿片数与入藏经过未载；库路真的器形、胎骨、纹样、工序与具体内容未载；木画的工序、胶料、嵌片厚度与产地未载。
- 木画棋局的尺寸、木质、棋盘道数未载；双六局的尺寸、盘面布局细节、博法规则与掷具未载。
- 《萧翼赚兰亭图》的材质、尺寸、收藏地与画面其余细节未载；大智禅师碑的碑主法号、立碑年代、撰书人、碑高与具体陈列位置未载；牡丹纹的构成式样、年代序列与器物实例未载。
- 插图 13、16、17 未视觉核验。
- Book 7 及以后不启动（用户范围限定）。

## 9. 下一跳

- 执行 T9：第八章宋代的工艺美术（L3468-L3948）unit 候选 37 条，含 cand-09-32 荷叶敞口银杯、cand-09-48 宋徽宗、cand-09-54 影青执壶（带温酒器）、cand-09-56/57 章生一/章生二、cand-09-61 建窑黑釉斑纹、cand-09-63/64 舒翁/舒娇、cand-09-66 宋三彩（宋加彩）、cand-09-69 鸡腿坛、cand-09-70 白瓷盘口长颈瓶、cand-09-91 契丹鞍、cand-10-02 辽三彩盘、cand-10-07 绮、cand-10-08 宋罗、cand-10-10 薛景石、cand-10-12 茂花闪色锦、cand-10-18 织成、cand-10-23 莲塘乳鸭图、cand-10-24 蓝印花布、cand-10-25 唐仲友、cand-10-28 神针、cand-10-29 宋绣金刚般若波罗蜜经、cand-10-30 对鸟对羊刺绣包首、cand-10-31 正定龙兴寺铜佛、cand-10-32 新铜器、cand-10-34 宋镜、cand-10-38 描金堆雕漆盒、cand-10-40 螺钿、cand-10-42 剔犀、cand-10-43 剔犀执镜盒、cand-10-44 雕漆扇柄、cand-10-85 吴煦、cand-10-86 梅鹊图、cand-10-87 蟠桃图、cand-10-88 描金、cand-10-89 凤首壶。
- 之后依次：元 16、明 38、清 43、近代 38；再进入 claim/evidence 流程（田自秉 278 条 claim 候选）。
