# h45 漆器实物与墓葬标本：B.11.3「漆器实物与墓葬标本：从包山双联杯到新中国漆盘」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h45/`
- 基线：v1.35（26 Theme／82 Topic／664 membership／654 complete／1916 incomplete／relation 7316／member_of 1318／isolated 1184／ksq 57/65／structural 130）。
- 目标：在 h44 建成的 Theme **B.11** 下物化 B.11.3「漆器实物与墓葬标本：从包山双联杯到新中国漆盘」，把前六册中 27 件漆器与墓葬标本 work KU 主挂载进去，补齐 h44 只登记为候选池的器物层。
- 结果：v1.36（26 Theme／83 Topic／691 membership／681 complete／1889 incomplete／relation 7370／member_of 1372／isolated 1166／ksq 57/65／structural 130）。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Topic `04-knowledge/structure/topics/b11-qiqi-shijian-yu-muzang-biaoben.md`：`node_type: topic`、`primary_dimension: B`、`parent_theme: B.11`、`secondary_themes: [C, D]`、`status: pilot`、`date: 2026-10-30`、`research_question` 一句、18 个 tags；七节齐备，支撑材料表 27 行。
- Topic 的核心判断是**按记载深度分层而非按年代排列**：六册对这批器物的著录极不均衡，有器物尺寸的一层、有器名与名工款识的一层、只有图注一行的一层、以推测或后世作品登记的一层。四层互不推导——有尺寸不等于有断代，有款识不等于有工序，有图注不等于有藏地。
- B.11 三层分工自此闭合：B.11.1 回答胎怎么成形、漆层怎么上、生产怎么分工；B.11.2 回答同一层漆被处理成什么效果、技法名各按什么方式成立；B.11.3 回答六册究竟著录了哪些实物、每件被记到器用、胎骨与工序、纹饰与绘画、名工与款识哪一层。三者不是前后阶段，而是同一批漆器的工序面、装饰面与器物面。
- 快照：`hierarchy/index.md` 旧版归档为 `hierarchy/archive/v1.35.md`（68043 字节），再改写 index.md 为 v1.36。

## 三、27 个 KU 挂载

全部为主挂载（`primary_theme: B.11`，`role_in_theme` 与 membership 同值，`primary: true`），无次挂载。

- `representative_work` 24：`works/caihui-fengniao-shuanglian-qi-jiubei`、`works/wunv-qilian`、`works/caihui-niaoshou-yuwen-qi-ge`、`works/caiqi-mudiao-dongwu-zuoping`、`works/zenghouyi-lacquer-clothing-chests`、`works/zenghouyi-tianxiang-tu`、`works/simajinlong-mu-qi-pingfeng`、`works/zhu-ran-mu-hei-hong-qi-ji`、`works/qiyu-yunmeng-shuihudi-33`、`works/qihui-mushu-mubi`、`works/xiangyang-leigutai-qiren-wen-qilian`、`works/heiqizhuhui-niaozu-qian`、`works/waguan-si-jiazhu-foxiang`、`works/zhang-cheng-tihong-box`、`works/zhang-cheng-yun-wen-ti-xi-qi-he`、`works/yang-mao-ti-hong-guan-pu-tu-ba-fang-pan`、`works/tixi-zhijinghe`、`works/diaoqi-shanbing`、`works/tihei-diaoqi-flower-bird-plate`、`works/luodian-huaniao-wen-jinghan`、`works/luodian-zhuiqi-zanhe`、`works/guanghan-palace-luodian-plate`、`works/miaojin-duidiao-qihe`、`works/diaoqi-small-box`。
- `boundary_case` 3：`works/jinqi-diaolong-baozuo`、`works/zitan-tihong-baozuo`（只取髹饰一面，宝座形制与清式家具谱系归家具线）、`works/jinyu-qipan`（1949 年后作品，只取研磨彩绘效果，产业属 E）。

类型与角色：work 27；`representative_work` 24、`boundary_case` 3。`primary_dimension` 全部为 B，无新增跨维度挂载。B.11 累计 52 个 KU（term 18、procedure 6、work 28；`term_anchor` 16、`procedure` 6、`representative_work` 25、`historical_context` 1、`boundary_case` 4）。

## 四、边界处置

- **维度字段决定边界**：`works/beiwei-muban-qihua` 虽属漆绘材料，但 `primary_dimension` 为 C（绘画线），不入 B.11.3。漆器线与绘画线在司马金龙墓这一处材料上因此不闭合，登记为未决。
- 不入本 Topic：`works/huaniao-renwu-luodian-jing` 归 B.9.3（铜镜）、`works/luodian-wuxian-pipa` 与 `works/qi-shuangfeng-gu` 归 B.10.3（弦管与鼓）、`works/he-mudu-zhuqi-muwan` 已由 h44 挂 B.11.1。
- 两件宝座与 1949 年后金鱼漆盘以 `boundary_case` 登记，`scope_note` 明确「只取髹饰一面」，形制谱系归家具线、产业归属归 E。
- 器名不裁：张成剔红盒「圆盒／圆盘」并列；望山座屏「50 余」与「51 只」并列；描金堆雕漆盒的「舍利盒」用途标为来源推测。
- 不合并跨册分记：张成 80 层（田自秉）与张成云纹剔犀盒刀口 1 厘米（李立新）分属两器，不推为张成通例；曾侯乙衣箱（赵农）与天象图衣箱（李立新）分属两条；朱然墓漆槅（高丰）与朱然墓漆几（赵农）分属两器。
- 不据名称补条：B.11.4 的《髹饰录》、黄成、杨茂、张成、沈沼安、李芝卿等文献与名工仍只作候选池，不在本批挂载。

## 五、执行与验证

1. 语义裁决先于执行：逐条复读 27 件 work KU 的正文与 `sources`，决定主挂载、role 与 `scope_note`；机械脚本 `h45_mount.py` 只消费已裁决清单，不生成归属。
2. 来源统计脚本实算：按完整 `evidence_ref.doc_id` 聚合（不用年份正则），得田自秉 15（14 唯一）、高丰 4、李立新 4、夏燕靖 2016 3、赵农 2、夏燕靖 2009 1；单册 26、三册 1；medium 20、low 7；tentative 27。
3. 写后复核实测：27 个文件 YAML 全部可解析，`primary_theme == 'B.11'`、`primary_dimension == 'B'`、`topic_memberships` 长度 1 且 `primary is True`、Topic 路径一致，`bad 0`；`hierarchy_scope_note` 中「Theme/Topic 尚未 materialize」全部消去。
4. `python scripts/hierarchy_stress_test.py`：v1.36、26 Theme、83 Topic、691 membership、681 complete、1889 incomplete、`cross_dimension_topics` 为空（`secondary_themes` 用裸维度码 `C`、`D`，按 `hierarchy_stress_test.py:828` 的 `"." in code` 规则不计入维度集合）、`apply_permitted: false`。
5. `python scripts/build_relation_index.py`：7316→7370（explicit 5998 不变，inferred／member_of 1318→1372）。
6. `python scripts/write_current_health.py`：v1.36、complete 681、missing 1889、relation 7370、structural 130/130、ksq 57/65、content 0。
7. `python scripts/audit_relation_consistency.py`：isolated 1184→1166（减 18，见第六节）；broken target 0、invalid relation_type 0、missing inverse 0。
8. `python scripts/run_sync_closure.py --refresh-generated --full`：250 tests + 16 subtests 通过；刷新前 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，刷新后归 0。
9. `python scripts/run_sync_closure.py --refresh-generated --check-generated`：第 17 步以 `exit=1` 报生成态与 HEAD 不一致，属未 commit 的预期而非失败。
10. apply-plan 32 行逐行复核 `after_sha256` 与磁盘一致（`rows 32 bad 0`）；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree、HEAD 仍为 `c249c6fe`。

## 六、指标变化

| 指标 | v1.35 | v1.36 | 变化 |
|---|---|---|---|
| Theme | 26 | 26 | 0 |
| Topic | 82 | 83 | +1（B.11.3） |
| topic_memberships | 664 | 691 | +27 |
| 已完成挂载 KU | 654 | 681 | +27 |
| 未挂载 KU | 1916 | 1889 | −27 |
| B 维度未挂载 | 1201 | 1174 | −27 |
| relation_index | 7316 | 7370 | +54 |
| member_of | 1318 | 1372 | +54 |
| 隔离单元 | 1184 | 1166 | −18 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 54 = 27 条主挂载 ×（topic `member_of` + theme `member_of`）。隔离单元减 18 而非 27，因为实测 27 条中有 9 条原已有显式关系。B 维度减 27，因为 27 条主挂载的 `primary_dimension` 全部为 B。membership 仍比 KU 多 10，双挂载与次挂载清单不变。

## 七、语义边界（并列不裁）

- **记载深度取代年代顺序是本批主判断**：27 件中只有四件给出器物尺寸（包山双联杯 9.2／17.6／7 厘米、望山座屏高 15 长 51.8 厘米、朱然墓漆几 26／69.5／13 厘米、擂鼓台漆奁 25／9.7／23.8／8.8 厘米），只有两件带名工款识（张成剔红盒针刻「张成造」、雕漆扇柄「君玉」），五件只有图注一行。按年代排会把这批器物压成一条虚假的时间线。
- **三处图注与正文互不一致**：朱然墓漆槅图注作「槁」而正文作「槅」；剔黑雕漆花鸟纹盘图注作「剔黑」而正文作「剔彩」；螺钿花鸟纹经函图版 6-49／6-50 交错。三处均照录不裁，在 Topic 与 Theme 同时登记。
- **跨册分记不合并**：张成 80 层与刀口 1 厘米分属两器；曾侯乙衣箱与天象图衣箱分属两条；朱然墓漆槅与漆几分属两器。同一墓葬、同一名工在六册中从未被同一段文本合并著录。
- **维度字段而非题材决定边界**：北魏木板漆画属漆绘材料，但 `primary_dimension: C`，留在绘画线；漆器线与绘画线在司马金龙墓这一处不闭合。
- **推测照录**：描金堆雕漆盒的「舍利盒」用途、司马金龙墓屏风的「核桃油调漆」、包山双联杯的「合卺杯」均标为来源推测，不升格为定论。
- **来源覆盖不均**：田自秉 2010 覆盖 15 件（14 件为唯一来源），高丰 4 件，李立新 4 件，夏燕靖 2016 3 件，赵农 2 件，夏燕靖 2009 1 件；单册 26 件、三册 1 件。李立新 2011 在 h44 的 25 条中无一关联，本批却占 4 件，说明 B.11 的覆盖不能按批次推断。
- **confidence 全 tentative**：medium 20、low 7，无一条 high。器物层「已挂载」不等于「已确认」。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- 生成态陷阱复现并消解：relation 数变化后 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，全量闭包刷新后归 0。与 h13 以来历批一致，属生成顺序而非内容缺陷。
- `--refresh-generated --check-generated` 用于发布前比对：本批未 commit，工作区存在计划内改动，第 17 步 `check generated snapshots`（`git diff --exit-code HEAD`）以 `exit=1` 报漂移，属预期而非失败。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；250 tests + 16 subtests 通过。
- 本批 changed_files 40 = apply-plan 32 行（1 结构节点新建 + 27 主挂载 + 4 索引更新）+ 8 个闭包重建的生成态／导航文件；归档 `hierarchy/archive/v1.35.md` 按 h44 口径不计入，README.md 与其余 `04-knowledge` 改动属 h13–h44 未提交批次。

## 九、未决事项与下一跳

- **B.11 收口后的缺口**：B.11.4「髹饰文献与名工」（约十七项：髹饰录、黄大成／黄成、杨茂、张成、张德刚、包亮、周翥、蒋回回、杨埙、姜千里、彭君宝、沈沼安、卢葵生、李芝卿、格古要论、燕闲清赏笺、废艺斋集稿、南村辍耕录）仍只有候选池，是 B.11 最后一块未物化的层。
- **家具与木作 Theme 的缺口被本批放大**：朱然墓漆几、鸟足漆凭几、两件宝座的形制谱系都指向尚未建立的家具线，目前只能挂在 B.11.3 的 `scope_note` 之外。
- **存量结构缺口**：铁器与叠铸 Topic、货币与农具 Topic、前近代服饰与甲胄等级 Theme 仍未物化。
- **重复候选 reconcile 9 组**未处理：`works/fuhao-jade-figure` 与 `works/fuhao-mu-yuren`；`works/yudiaolong` 与 `works/da-yulong`；`terms/youlihong-ci` 与 `terms/youlihong`；`terms/bai-tao` 与 `terms/shangdai-baitao`；鲁山窑瓷拍鼓与花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` 与 `works/zhulin-qixian-rongqiqi-zhuanhua`；`terms/chunqiu-zhanguo-qingtong-chuishiqi` 与单器条；`terms/huasi` 与 `terms/hua-si-gong-yi`；`terms/pi-pa` 与 `terms/ruan-xian`。
- **图注待核 12 条**、图 7-29 两指问题仍挂账；本批新增未核图版 5-32。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1889、隔离 1166、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- **小债务**：`works/caihui-niaoshou-yuwen-qi-ge.md` 的「相关知识元」把 `simajinlong-mu-qi-pingfeng` 说成「马王堆漆屏风」，与实际文件不符，本批不擅改。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
