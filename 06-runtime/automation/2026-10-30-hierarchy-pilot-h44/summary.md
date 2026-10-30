# h44 漆器与髹饰：B.11「漆器与髹饰：胎骨、髹涂与装饰」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h44/`
- 基线：v1.34（25 Theme／80 Topic／639 membership／629 complete／1941 incomplete／relation 7266／member_of 1268／isolated 1198／ksq 57/65／structural 130）。
- 目标：新建 Theme **B.11**，把前六册中漆器与髹饰的 25 个 KU 从「无 Theme 可挂」的存量中提出来，按「胎骨与漆层—装饰」两路物化为 B.11.1、B.11.2 两个 Topic，并补齐 B 维度长期缺失的漆器线。
- 结果：v1.35（26 Theme／82 Topic／664 membership／654 complete／1916 incomplete／relation 7316／member_of 1318／isolated 1184／ksq 57/65／structural 130）。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Theme `04-knowledge/structure/themes/b11-qiqi-yu-xiushi-taigu-xiutu-yu-zhuangshi.md`：`node_type: theme`、`theme_code: B.11`、`primary_dimension: B`、`secondary_dimensions: [C, D]`、`status: pilot`、`date: 2026-10-30`、`source_basis` 六册齐列；核心问题为「六册把漆器的哪一层写清楚了、哪一层只有名字」；边界十一条；未解决问题二十条。
- 新建 Topic `04-knowledge/structure/topics/b11-taigu-xiutu-yu-zhizuo-fengong-cong-mutai-dao-tuotai.md`：B.11.1「胎骨、髹涂与制作分工：从木胎到脱胎」，`parent_theme: B.11`、`secondary_themes: [D, C]`、`research_question` 175 字、支撑 9 个 KU；按「胎骨路线—灰与糙漆—制作分工—器物锚点」四层组织，四层互不推导；未解决问题十三条。
- 新建 Topic `04-knowledge/structure/topics/b11-xiushi-jifa-jinqi-ketian-moxian-yu-xiangqian.md`：B.11.2「髹饰技法：金饰、刻填、磨显与镶嵌」，`parent_theme: B.11`、`secondary_themes: [C, D]`、`research_question` 196 字、支撑 16 个 KU；按「动手时点」分金饰、刻填、磨显、镶嵌四路，另立元代技法合述与库路真名产边界；未解决问题十六条。
- 两大 Topic 分工：B.11.1 回答漆器的胎怎么成形、漆层怎么上、生产怎么分工；B.11.2 回答同一层漆被处理成什么效果、这些技法名各按什么方式成立。二者不是前后阶段，而是同一批漆器的胎骨面与装饰面。
- 四个候选池登记不物化：B.11.3「漆器器物与墓葬标本」（约二十件器物候选）、B.11.4「髹饰文献与名工」（约十七项文献与名工候选）；本版不建空 Topic。
- 快照：`hierarchy/index.md` 归档为 `hierarchy/archive/v1.34.md`（65725 字节），再改写 index.md 为 v1.35。

## 三、25 个 KU 挂载

全部为主挂载（`primary_theme: B.11`，`role_in_theme` 与 membership 同值，`primary: true`），无次挂载。

B.11.1 九条：

- `procedure` 6：`procedures/xiu-qi`、`procedures/qiqi-mutai-san-zuofa`、`procedures/jiazhu-tai`、`procedures/quan-die-fa`、`procedures/juan-su-tai-gu-hei-guang`、`procedures/han-dai-qiqi-zhizuo-fengong`。
- `term_anchor` 2：`terms/tuotai-qiqi`、`terms/kouqi`。
- `representative_work` 1：`works/hemudu-zhui-muwan`（作漆器起源的器物锚点，非器形标本）。

B.11.2 十六条：

- `term_anchor` 14：`terms/miaojin`、`terms/qiangjin`、`terms/jin-qi`、`terms/diao-qi`、`terms/tixi`、`terms/tianqi-lacquer`、`terms/xipi`、`terms/ban-qi`、`terms/lvchen-qi`、`terms/yanmo-caihui`、`terms/luodian`、`terms/dianluo`、`terms/yangzhou-luodian`、`terms/baibaoqian`。
- `historical_context` 1：`terms/yuan-dai-qiqi-zhuangshi`（元代技法断代合述）。
- `boundary_case` 1：`terms/kuluzhen`（唐代襄州贡漆器名产，「不知具体内容」，不并入任何一路）。

类型与角色：term 18、procedure 6、work 1；`term_anchor` 16、`procedure` 6、`representative_work` 1、`historical_context` 1、`boundary_case` 1。`primary_dimension` 全部为 B，无新增跨维度挂载。

## 四、边界处置

- 技法内部：B.11.2 按「动手时点」而非年代或器类分四路——金饰（描金、戗金、金漆）在髹涂前后落在漆面之上，刻填（雕漆、剔犀、填漆）在漆层半干时去掉漆料，磨显（犀皮、斑漆、绿沉漆、研磨彩绘）靠层层叠色后磨平，镶嵌（螺钿、点螺、扬州螺钿、百宝嵌）另加异质嵌片。
- 不并入本 Theme：金银平脱归 B.9.4、螺钿镜归 B.9.3、螺钿乐器（五弦琵琶、漆双凤鼓）归 B.10.3；果园厂归 D.6.6、汉代漆器作坊官员与工官隶属归 D.6.5；北京雕漆厂、继古斋与 1914 年巴拿马赛会归 B.4／E.1；木画归木器镶嵌（家具木作线）；家具形制术语与明式清式家具留家具线；纹样母题与铭文归 C。
- 同一 KU 不重复挂载：25 条全部只挂一个 Topic；`terms/jiazhu-tai` 与 `terms/tuotai-qiqi` 在胎骨链上前后相邻但不互相并入（前者是去胎工序，后者是清代脱胎器类名）。
- 不据名称补条：髹饰录、黄成、张成、杨茂、周翥等名工与文献均已在库但本批不挂 B.11，登记为 B.11.4 候选池；B.11.3 的二十余件器物同样只作候选。
- 不推算：不据「漆层约 80 道」推其余器物的髹涂遍数；不据「0.2 厘米杉木条」推唐宋全部圈叠器的壁厚；不据「十倍」推扣器的实际成本；不据「二十余种嵌料」推百宝嵌的工序顺序。

## 五、执行与验证

1. 语义裁决先于执行：逐条复读 18 个 term、6 个 procedure、1 个 work 的 KU 正文与 `sources`，决定主挂载、Topic 归属与 `scope_note`；机械脚本 `h44_mount.py` 只消费已裁决清单，不生成归属。
2. 自审修正（写回前）：来源统计原按年份正则聚合，导致夏燕靖 2009 与赵农 2009 折叠为一个「2009」；改用完整 doc_id 统计后，重写两 Topic 的「实证材料支撑」「文献支撑」与三处统计型未解决问题，并同步修正 Theme 两处统计。
3. 归属修正：初稿曾把「汉代已有戗金」归给高丰（实为夏燕靖 2009 秦汉代表）、把朱然墓东吴羽觞归给田自秉（实为高丰）、把「唐代已有雕漆」归给赵农与高丰（实为田自秉「唐代新创而唐实物未发现」），逐条回原件改正。
4. 写后复核实测：25 个文件 YAML 全部可解析，`primary_theme == 'B.11'`、`topic_memberships` 长度 1、`primary is True`，`bad 0`；`hierarchy_scope_note` 中「Theme/Topic 尚未 materialize」全部消去。
5. `python scripts/hierarchy_stress_test.py`：v1.35、26 Theme、82 Topic、664 membership、654 complete、1916 incomplete、`cross_dimension_topics` 为空（`secondary_themes` 用裸维度码 `D`、`C`，按 `hierarchy_stress_test.py:828` 的 `"." in code` 规则不计入维度集合）、`apply_permitted: false`。
6. `python scripts/build_relation_index.py`：7266→7316（explicit 5998 不变，inferred／member_of 1268→1318）。
7. `python scripts/write_current_health.py`：v1.35、complete 654、missing 1916、relation 7316、structural 130/130、ksq 57/65、content 0。
8. `python scripts/run_sync_closure.py --refresh-generated --full` 连跑两次：均 250 tests + 16 subtests 通过；首次必现 `rule_drift {'findings': 1, 'output_navigation_snapshot_stale', 'relation 7266 vs 7316}`，重跑 `write_current_health.py` 后第二次 `rule_drift 0`。
9. apply-plan 32 行逐行复核 `after_sha256` 与磁盘一致（`rows 32 bad 0`）；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree、HEAD 仍为 `c249c6fe`。

## 六、指标变化

| 指标 | v1.34 | v1.35 | 变化 |
|---|---|---|---|
| Theme | 25 | 26 | +1（B.11） |
| Topic | 80 | 82 | +2（B.11.1、B.11.2） |
| topic_memberships | 639 | 664 | +25 |
| 已完成挂载 KU | 629 | 654 | +25 |
| 未挂载 KU | 1941 | 1916 | −25 |
| B 维度未挂载 | 1226 | 1201 | −25 |
| relation_index | 7266 | 7316 | +50 |
| member_of | 1268 | 1318 | +50 |
| 隔离单元 | 1198 | 1184 | −14 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 50 = 25 条主挂载 ×（topic `member_of` + theme `member_of`）。隔离单元减 14 而非 25，因为 25 个新挂载 KU 中有 11 个原已有显式关系。B 维度减 25，因为 25 条主挂载的 `primary_dimension` 全部为 B。membership 仍比 KU 多 10，双挂载与次挂载清单不变。

## 七、语义边界（并列不裁）

- **名实分离是本批主判断**：25 条中只有雕漆一处给出量化（「漆层约 80 道」）；斑漆有文献而无遗物；库路真「不知具体内容」；金漆、绿沉漆无工艺定义。因此本 Theme 的核心问题写成「哪一层写清楚、哪一层只有名字」，而不是写成漆器工艺史。
- **三处断代冲突并列**：戗金（田自秉记宋代新创造／夏燕靖 2009 归秦汉代表）、犀皮（田自秉记宋代新创造／高丰记朱然墓东吴最早实物）、雕漆（田自秉记唐代新创而同处称唐实物未发现）。三者均不裁，在 Topic 与 Theme 同时登记。
- **胎骨四路线不成演化线**：汉代旋制、剜削、卷制三法与战国夹纻去胎、唐宋木条圈卷、元代旋床胶粘脆松薄片，分属不同册的不同器类，从未在同册内比较，不写成从木胎到脱胎的技术进步序列。
- **漆层记载只有两份**：夏燕靖 2009 的战国三类工艺名（描彩漆、镶嵌、针刻）与田自秉 2010 引《辍耕录》的卷素—揩光全工序；后者是六册唯一漆层配方，不可回推汉唐。
- **元代合述与分条不互相替代**：`yuan-dai-qiqi-zhuangshi` 作为 `historical_context` 只作断代合述，与剔红、剔犀、螺钿、戗金分条并列；其同册张力（「并未得到元代重视」对「产生许多漆雕佳品」）照录不改。
- **来源覆盖不均**：田自秉 2010 覆盖 21 条（其中 14 条为唯一来源），高丰 2004 覆盖 6 条，夏燕靖 2009 与赵农 2009 各覆盖 4 条与 2 条，夏燕靖 2016 只覆盖 3 条，李立新 2011 无关联来源；单册来源 17 条、两册 6 条、三册 1 条（扣器）、四册 1 条（夹纻胎）。
- **confidence 全 medium、consensus 全 tentative**：本批无一条达到 high，在 Theme 未解决问题末条明示，不以「已挂载」等同于「已确认」。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- 生成态陷阱复现并消解：relation 数变化后首次全量闭包必报 `output_navigation_snapshot_stale`（rule_drift 1，relation 7266 对 7316），重跑 `write_current_health.py` 后再全量闭包归 0。此现象与 h13 以来历批一致，属生成顺序而非内容缺陷。
- `--refresh-generated --check-generated` 用于发布前比对：本批未 commit，工作区存在计划内改动，第 17 步 `audit system upgrade chain` 预期以 `exit=1` 报未提交索引／状态漂移，属预期而非失败。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；250 tests + 16 subtests 通过。
- 本批 changed_files 40 = apply-plan 32 行（3 结构节点新建 + 25 主挂载 + 4 索引更新）+ 8 个闭包重建的生成态／导航文件；README.md 与其余 `04-knowledge` 改动属 h13–h43 未提交批次，不计入本包。

## 九、未决事项与下一跳

- **B.11 收口后的缺口**：B.11.3 器物层（约二十件）与 B.11.4 文献名工层（约十七项）只有候选池，未物化；二者是本 Theme 下一步最直接的增量。
- **存量结构缺口**：铁器与叠铸 Topic、货币与农具 Topic、前近代服饰与甲胄等级 Theme、家具与木作 Theme 仍未物化；漆器已从「无 Theme 可挂」材料组中移出。
- **重复候选 reconcile 9 组**未处理：`works/fuhao-jade-figure` 与 `works/fuhao-mu-yuren`；`works/yudiaolong` 与 `works/da-yulong`；`terms/youlihong-ci` 与 `terms/youlihong`；`terms/bai-tao` 与 `terms/shangdai-baitao`；鲁山窑瓷拍鼓与花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` 与 `works/zhulin-qixian-rongqiqi-zhuanhua`；`terms/chunqiu-zhanguo-qingtong-chuishiqi` 与单器条；`terms/huasi` 与 `terms/hua-si-gong-yi`；`terms/pi-pa` 与 `terms/ruan-xian`。
- **图注待核 12 条**、图 7-29 两指问题仍挂账；本批新增未核图版 5-32。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1916、隔离 1184、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
