# 2010 册 units 批次 T10（元代）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2010tianzibing-units-batch-t10/`
- 来源：田自秉《中国工艺美术史（修订本）》（2010），doc_id `2010-tianzibing-zhongguo-gongyi-meishushi`
- 候选范围：第九章元代的工艺美术（L3949-L4169）的 unit 候选 16 条
- 裁定结果：新建 14 条、更新 1 条、no_delta 1 条、rejected 0 条
- 状态：applied（16 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：第九章元代的工艺美术（L3949-L4169），含概说（蒙古兴起、匠户制度、工艺门类总述）、陶瓷（枢府窑、影青、蓝釉、龙泉、钧窑、磁州窑、青花、釉里红、火石底、元代器形与装饰）、琉璃（任塘香炉、三彩龙凤香炉）、染织（纳石失、织金技法、织锦名目、毛织、棉织、黄道婆）、刺绣（七种针法、集宁路夹衫、李裕庵墓）、金属工艺（朱碧山等银工、金坛窖藏、合肥窖藏、吴县窖藏、铜器与铜镜）与漆器（卷素黑光、雕漆、张成杨茂、彭君宝、螺钿），至元代结语止。
- 截断点：L3948 为宋代结语末，已由 T9 处理；L4170 起为第十章明代，归下一批。
- 插图 1、2、3、4、5、6、7 只读图注，未视觉核验。
- `cand-10-70` 的候选跨度 L4050-L4112 覆盖《辍耕录》五处引文中的四处，另补 L4136、L4151 两处同书引文，`manifest.json.inputs.source.spans` 仍记全章 `[[3949, 4169]]`。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-10-57 | 蓝釉描金匜 | 新建 | `works/lanyou-miaojin-yi.md` |
| cand-10-59 | 青花八棱海水龙纹瓶 | 新建 | `works/qinghua-baleng-longwen-ping.md` |
| cand-10-64 | 三彩龙凤琉璃釉香炉 | 新建 | `works/sancai-longfeng-liuliyou-xianglu.md` |
| cand-10-65 | 任塘 | 新建 | `persons/rentang.md` |
| cand-10-90 | 火石底 | 新建 | `terms/huoshidi.md` |
| cand-10-76 | 元代刺绣针法 | 新建 | `terms/yuan-dai-cixiu-zhenfa.md` |
| cand-10-77 | 集宁路刺绣夹衫 | 新建 | `works/jininglu-cixiu-jiashan.md` |
| cand-10-81 | 凸花人物故事盘 | 新建 | `works/tuhua-renwu-gushipan.md` |
| cand-10-82 | 银果盒 | 新建 | `works/yinguohe.md` |
| cand-10-83 | 四合如意金盘 | 新建 | `works/sihe-ruyi-jinpan.md` |
| cand-11-07 | 张成剔红山水人物圆盒 | 新建 | `works/zhang-cheng-tihong-box.md` |
| cand-11-11 | 彭君宝 | 新建 | `persons/peng-junbao.md` |
| cand-11-12 | 广寒宫螺钿漆盘残片 | 新建 | `works/guanghan-palace-luodian-plate.md` |
| cand-11-83 | 剔黑雕漆花鸟纹盘 | 新建 | `works/tihei-diaoqi-flower-bird-plate.md` |
| cand-10-70 | 辍耕录 | 更新 | `publications/nancun-chuogenglu.md` |
| cand-10-56 | 枢府窑 | no_delta | `places/jingdezhen-kiln.md` |

## 4. 新建 14 条

**陶瓷与琉璃（3）**：蓝釉描金匜、青花八棱海水龙纹瓶、三彩龙凤琉璃釉香炉。

**陶瓷术语（1）**：火石底。

**琉璃人物（1）**：任塘。

**刺绣（2）**：元代刺绣针法、集宁路刺绣夹衫。

**金银器（3）**：凸花人物故事盘、银果盒、四合如意金盘。

**漆器（4）**：张成剔红山水人物圆盒、彭君宝、广寒宫螺钿漆盘残片、剔黑雕漆花鸟纹盘。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，created/updated/last_verified 为 2026-10-27、review_due 为 2027-04-27，`academic_translation_status` 均为 provisional。confidence：10 条 medium、4 条 low（青花八棱海水龙纹瓶、任塘、彭君宝、剔黑雕漆花鸟纹盘），缺项已逐项标未载。

## 5. 更新 1 条

- `publications/nancun-chuogenglu.md`：跨册更新，追加田自秉 L4050（元代织锦花纹名目与绫的花色）、L4078（黄道婆自崖州来与错纱配色综线絜花之法）、L4112（浙西银工朱碧山、谢君余、谢君和、唐俊卿）、L4136（卷素、梢当、粗中细灰、糙漆与黑光工序）、L4151（嘉兴斜塘杨汇髹工戗金戗银法条题）；`source_count` 1→2，version 1→2。原 2016 册黄道婆条保留，两册引文并见，不据一方删并另一方。

## 6. 语义判断与内部张力

1. **枢府窑记 no_delta**：`places/jingdezhen-kiln.md` 已引 L3973 全文并处理“枢府”字铭、“太”“僖”字与太僖机构的两存；`terms/luanbai-you-ci.md` 又把“枢府窑”列为卵白釉异名。另立 `terms/shufu-yao.md` 会与窑口条、卵白釉条三重复，故目标记 `places/jingdezhen-kiln.md`。
2. **蓝釉描金匜与窑口条分工**：`places/jingdezhen-kiln.md` 已用 L3977 作元代蓝釉品种举例；本批另立单器条，收器名、出土、釉色、金绘流云折枝花与两种蓝白对比处理，窑口条继续承担窑业总述，二者互指不互抄。
3. **青花八棱海水龙纹瓶只据图注**：L3991-L3992 只有图版与“青花八棱海水龙纹瓶(元)”一行，正文未描述此器。按图版锚点建 work 条，标未视觉核验，不据器名补写尺寸、胎釉、款识与藏地。
4. **三彩龙凤琉璃釉香炉的“风纹”**：L4026 原文作“风纹”，按器名“三彩龙凤琉璃釉香炉”及上下文疑为“凤纹”，照录不改，条内标疑；不据来源外材料改字。
5. **任塘的“琉璃待诏”**：来源只给“至大元年汾阳琉璃待诏任塘刻铭”，本批据此建 person 条，职名照录；所属机构、品秩与任职方式均标未载，不代补元代官制。
6. **《辍耕录》跨册更新**：原条只据 2016 册黄道婆一条，source_count 为 1；田自秉册五处引文分属织锦名目、棉织人物、银工名录、髹漆工序与戗金技法，覆盖染织、金属、漆器三门。按跨册更新追加 source block，source_count 1→2、version 1→2，不把五处引文拆成五条 publication。
7. **元代刺绣针法作清单级 term**：`procedures/bian-xiu.md` 已记辫绣历代沿革与清代“拉梭子”称谓，`procedures/yun-jian-xiu.md` 已记唐代纭裥绣与抢针绣别名。本批不拆七条 procedure，而建 `terms/yuan-dai-cixiu-zhenfa.md` 记元代七种针法的名称、别称与效果，单针法沿革仍归既有 procedure 条。
8. **集宁路夹衫的江南制作推测**：L4100 原文判断夹衫具有江南刺绣特点，可能江南制作或由江南绣工在北方官府工场制作。条内照录两说，不裁断产地，也不把推测写成定论。
9. **金坛窖藏的三件银器**：凸花人物故事盘、银果盒、四合如意金盘分属金坛、合肥、吴县三处窖藏，来源同章并列而不同器。本批各立单器条，不合并为“元代金银器窖藏”总条；窖藏本身尚无 structure node。
10. **银果盒与吴县八棱银果盒**：L4116 的合肥银果盒为十莲瓣形、重76两；L4118 的吴县器另有八棱银果盒，来源只列器名。本批只据 L4116-L4121 建合肥银果盒条，不把吴县八棱器并入，避免同名异物合一。
11. **张成剔红山水人物圆盒的器名游移**：L4140 前称“剔红山水人物圆盒”，L4145 后文改称“水人物圆盘”又以“盒面”称其面。条内两存并标未统一，不据一处表述改写另一处。
12. **彭君宝补既有条目明言的缺口**：`persons/zhang-cheng.md`、`persons/yang-mao.md` 均注“彭君宝尚未单独成 KU”，`places/jiaxing-xitang-yanghui.md` 只在产地条内记其戗金。本批据 L4151-L4156 建 person 条，与两雕漆名手、产地条和 `terms/qiangjin.md` 互指。
13. **广寒宫螺钿盘与元代螺钿总述**：`terms/luodian.md` 只记宋、明两段，元代段未收；`places/jiaxing-xitang-yanghui.md` 已说明大同元墓与后英房两件属元代漆器总述、不入产地条。本批先建单器 work 条，元代螺钿总述留待 `terms/luodian.md` 后续补写，不据单器条改写总类。
14. **剔黑盘的图注与正文歧异**：L4143 图注作“剔黑雕漆花鸟纹盘”，L4138 正文插图6 紧接“漆层有多色的，称为剔彩”之后，品种名不一致。条内照录图注并标歧异，图版未视觉核验，不裁断为剔黑或剔彩。
15. **候选 unit_type 与实体性质核对**：14 个新建候选均按实体性质落位——单器与残片记 work，针法清单与胎体处理记 term，工匠记 person；无需要改写 unit_type 的条目。

## 7. 生成态与门禁

- 结构审计：`_zn_struct.py` 对 15 个文件（14 新建 + 1 更新），0 问题（13 个 frontmatter 字段、六节正文、ASCII 引号、悬空反引号链接、日期与状态字段均通过）。
- 引文审计：`_zn_checklines_t10.py` 覆盖 14 个新建条目、62 处双引号逐字引文与田自秉 2010 册源文去标点比对，0 遗漏、0 越界、0 行号错配。
- 全库引文审计：`_zn_audit.py` 对 15 个文件（含更新条）0 条发现。
- 索引重建：`build_discovery_index.py` 后 total 5339 不变；applied 2569→2584、needs_evidence 1692→1676、no_delta 226→227、rejected 852 不变；terminal 3647→3663、active 1676。`build_translation_index.py` 后 translation index 1921 条（T9 后 1907，+14）。
- 工作包：apply-plan 15 行（14 create、1 update）、candidate-decision-ledger 48 行（16×3）、canonical-mapping 16 条、manifest 1 份。工作包在 candidate-index 写回前构建，`counts_before` 与 `sha256_before` 为写回前真实值（needs_evidence 1692、applied 2569、rejected 852、no_delta 226，rows 5339）。
- 生成态闭包与 `--check-generated` 结果见第 9 节。

## 8. 跨批修正

- 本批初稿的引文门禁未报出问题；生成前自查修正两处：三彩龙凤香炉原把自撰的“凤纹”加引号，改为照录“风纹”并以非引号文字注疑；张成圆盒与彭君宝的器名、村名异写两条补上 `（L…）` 行号断言。
- 未改动本批以外的知识元；`terms/youlihong.md` 与 `terms/youlihong-ci.md` 并存等既有条目分工问题，留待后续 lint 或 reconcile。

## 9. 生成态闭包

- `python scripts/run_sync_closure.py --refresh-generated --full`：18 步全部通过（250 tests passed, 16 subtests passed），含关系索引、运行时索引、翻译索引、知识图谱、发现索引、健康与 backlog、输出画廊、生成态投影清单与三项审计。
- `python scripts/run_sync_closure.py --refresh-generated --check-generated`：17 步中前 16 步通过，[17/17] check generated snapshots FAILED exit=1，因本批与既有未提交知识元、生成态快照未提交，记 `blocked_pending_commit`，属设计行为。
- 生成态闭包运行后，`06-runtime/automation/index.md` 已收录本工作包。

## 10. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- 2010 册 unit 候选剩余量：明 38、清 43、近代 38 条；claim 候选 278 条未启动。本批 L3949-L4169 范围内另有 16 条 claim 候选仍为 needs_evidence，留给 claim/evidence 流程。
- `terms/luodian.md` 元代段未收（大同元墓螺钿花绘圆盒、后英房广寒宫残盘），本批只建广寒宫单器条，总类补写待后续批次。
- 青花八棱海水龙纹瓶、三彩龙凤琉璃釉香炉、银果盒、四合如意金盘、张成剔红山水人物圆盒、广寒宫螺钿漆盘残片、剔黑雕漆花鸟纹盘等条多据图注或图版，未视觉核验。
- 蓝釉描金匜、张成剔红盒等单器的尺寸、重量与藏地多未载；任塘、彭君宝的生卒、师承与作品存世未载。
- Book 7 及以后不启动（用户范围限定）。

## 11. 下一跳

- 执行 T11：第十章明代的工艺美术（L4170-L4502）unit 候选 38 条。
- 之后依次：清 43、近代 38；再进入 claim/evidence 流程（田自秉 278 条 claim 候选）。
