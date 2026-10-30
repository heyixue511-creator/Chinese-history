# h47 冶铁、炼钢与叠铸：B.9.7「冶铁、炼钢与叠铸：从生铁到灌钢」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h47/`
- 基线：v1.37（26 Theme／84 Topic／708 membership／698 complete／1872 incomplete／relation 7404／member_of 1406／isolated 1156／ksq 57/65／structural 130）。
- 目标：在 Theme **B.9** 下物化 B.9.7「冶铁、炼钢与叠铸：从生铁到灌钢」，把前六册中冶铁、炼钢、铁器成形与供风设备的 14 个 KU 主挂载进去，兑现 B.9.6 两条边界器物 `scope_note` 写下的承接承诺。
- 结果：v1.38（26 Theme／85 Topic／722 membership／712 complete／1858 incomplete／relation 7432／member_of 1434／isolated 1149／ksq 57/65／structural 130）。B.9 至此七个 Topic、105 个 KU。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Topic `04-knowledge/structure/topics/b9-yetie-liangang-yu-diezhu.md`：`node_type: topic`、`primary_dimension: B`、`parent_theme: B.9`、`secondary_themes: [D, A]`、`status: pilot`、`date: 2026-10-30`、`research_question` 一句、15 个 tags；七节齐备，支撑材料表 14 行。
- 核心判断有五条。**三册分工而非三册互证**：十四条全部来自夏燕靖 2016（8 条）、夏燕靖 2009（7 条）与赵农 2009（3 条），田自秉、高丰与李立新对本主题无关联条目；夏版在战国钢剑处结束，赵农从秦汉百炼钢接起，六册没有一处把两端连写。**块炼法与生铁冶铸并行是中国路线的核心判断**，全 Topic 只有 `terms/iron-three-brothers` 一条技术路线判断，其余都是单点工序或遗址描述。**供风与成形是两条不涉及成分的前置条件**，不能与炒钢、百炼钢、灌钢排成同一条成分调整序列。**名实两条术语不得互相解释**：美金／恶金是春秋语词化石，铁氏三兄弟是 2016 册的现代含碳量分类。**断代锚点分散在四处**（冶铁术出现、西周晚期人工冶铁、战国早期柔化、东汉温县叠铸），六册未在同一处并列。
- B.9 七线分工：前六线（器形、工艺、铜镜、表面装饰、金银与珐琅、兵器与甲胄）都停在单点器类、工序名或遗址名，B.9.7 第一次把「铁从矿石到钢的成分调整」与「供风、成形两条前置条件」分开排列，并显式拒绝排成一条演化线。
- 快照：`hierarchy/index.md` 旧版归档为 `hierarchy/archive/v1.37.md`（70630 字节），再改写 index.md 为 v1.38。

## 三、14 个 KU 挂载

全部为主挂载（`primary_theme: B.9`，`role_in_theme` 与 membership 同值，`primary: true`），无次挂载。

- `procedure` 11：`procedures/ye-tie-shu-qi-yuan`、`procedures/sheng-tie-ye-zhu-ji-shu`、`procedures/sheng-tie-rou-hua-ji-shu`、`procedures/lian-gang-ji-shu`、`procedures/chao-gang`、`procedures/bai-lian-gang`、`procedures/guan-gang-fa`、`procedures/paituo-gufeng`、`procedures/shuili-gufeng`、`procedures/diezhu-jishu`、`procedures/tiefan-zhuzao`。
- `historical_context` 1：`terms/tieqi-shidai`（只作技术史分期与世界／中国两个年代锚点）。
- `term_anchor` 2：`terms/iron-three-brothers`（生铁／钢／熟铁按含碳量三分）、`terms/meijin-ejin`（铜为美金、铁为恶金）。

类型与角色：procedure 11、term 3；`procedure` 11、`historical_context` 1、`term_anchor` 2。`primary_dimension` 全部为 B，无新增跨维度挂载。B.9 累计 105 个 KU（procedure 27、term 42、work 36；`procedure` 26、`term_anchor` 40、`representative_work` 32、`boundary_case` 6、`historical_context` 1）。

## 四、边界处置

- **承接是显式的**：B.9.6 的 `works/iron-blade-bronze-yue` 与 `works/jade-handle-iron-sword` 已在 `scope_note` 写明「陨铁与人工冶铁之别、块炼法与冶铁起源归后续铁器 Topic」与「铁料与锻制工序归后续铁器 Topic」。本批即该条承诺的落点，器物归 B.9.6、材料与工序归 B.9.7；两件器物不重复挂载，只作年代锚点引用。
- **不收有色金属**：`procedures/jintong-fa`（浸铜法／湿法炼铜）是铜的化学提取，与铁技术不同线。
- **不收装饰工艺**：`procedures/tiehua-zhizuo`（清代芜湖铁画）材料为低碳钢，对象是书画仿制；`persons/tang-tianchi` 属名匠人物线，二者不入冶金技术 Topic。
- **农具与货币留待各自 Topic**：犁壁、犁刀、曲辕犁、耦犁、踏犁、铁搭、V 形铁铧冠等在六册中与冶铁分开叙述，材料线与器用线不合并；元代纸币、金代交钞、人民币、大清银币的铸造面与铁冶金无直接记载关系。
- **兵器与甲胄已在 B.9.6**：本 Topic 只取钢料工序（长沙杨家山钢剑、易县燕下都钢剑钢戟钢矛的检验结果），兵器形制不重复挂载。
- **叠铸不归 B.9.2**：温县烘范窑的实物是东汉车马器泥范，不是青铜容器工艺；B.9.2 的边界自 v1.28 起已写明。
- **不据名称补条**：`procedures/lian-gang-ji-shu` 与 `procedures/guan-gang-fa` 名称相近但是两种不同工序（前者为块炼铁渗碳锻打成钢，后者为生铁与熟铁合炼），不合并。

## 五、执行与验证

1. 语义裁决先于执行：逐条复读 14 个 KU 的正文、`sources` 与 `hierarchy_scope_note`，逐条判定 role 与 `scope_note`；机械脚本 `h47_mount.py` 只消费已裁决清单。
2. 来源统计脚本实算：按完整 `evidence_ref.doc_id` 聚合（不用年份正则），得夏燕靖 2016 覆盖 8 条、夏燕靖 2009 覆盖 7 条、赵农 2009 覆盖 3 条；单册 10、两册 4；medium 13、low 1；tentative 14。
3. 写后复核实测：14 个文件 YAML 全部可解析，`primary_theme == 'B.9'`、`primary_dimension == 'B'`、`topic_memberships` 长度 1 且 `primary is True`、Topic 路径一致，`bad 0`；`hierarchy_scope_note` 中「Theme/Topic 尚未 materialize」全部消去。
4. `python scripts/hierarchy_stress_test.py`：v1.38、26 Theme、85 Topic、722 membership、712 complete、1858 incomplete、`cross_dimension_topics` 为空、`apply_permitted: false`。
5. `python scripts/build_relation_index.py`：7404→7432（explicit 5998 不变，inferred／member_of 1406→1434）。
6. `python scripts/write_current_health.py`：v1.38、complete 712、missing 1858、relation 7432、structural 130/130、ksq 57/65、content 0。
7. `python scripts/audit_relation_consistency.py`：isolated 1156→1149（减 7，见第六节）；broken target 0、invalid relation_type 0、missing inverse 0。
8. `python scripts/run_sync_closure.py --refresh-generated --full`：250 tests + 16 subtests 通过；刷新前 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，刷新后归 0。
9. apply-plan 20 行逐行复核 `after_sha256` 与磁盘一致（`rows 20 bad 0`）；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree、HEAD 仍为 `c249c6fe`。

## 六、指标变化

| 指标 | v1.37 | v1.38 | 变化 |
|---|---|---|---|
| Theme | 26 | 26 | 0 |
| Topic | 84 | 85 | +1（B.9.7） |
| topic_memberships | 708 | 722 | +14 |
| 已完成挂载 KU | 698 | 712 | +14 |
| 未挂载 KU | 1872 | 1858 | −14 |
| B 维度未挂载 | 1157 | 1143 | −14 |
| relation_index | 7404 | 7432 | +28 |
| member_of | 1406 | 1434 | +28 |
| 隔离单元 | 1156 | 1149 | −7 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 28 = 14 条主挂载 ×（topic `member_of` + theme `member_of`）。隔离单元减 7 而非 14，因为实测 14 条中有 7 条原已有显式关系。B 维度减 14，因为 14 条主挂载的 `primary_dimension` 全部为 B。membership 仍比 KU 多 10，双挂载与次挂载清单不变。

## 七、语义边界（并列不裁）

- **路线是重建而非来源判断**：六册从未把「块炼法—生铁冶铸—柔化—炼钢—炒钢—百炼钢—灌钢」排成一条线。本 Topic 的排列依据各条 KU 的时代标签，两套叙事在「炼钢之后」断开，该断口在 Topic、Theme 与 manifest 三处同时登记。
- **记载深度分四档且互不推导**：有出土实物或遗址的五项（玉柄铁剑、六合程桥铁丸、洛阳铁锛铁铲、大冶六角锄、易县农具、长沙杨家山钢剑、燕下都钢兵器、温县烘范窑、兴隆与磁县铁范）；只有工序描述的两项（炒钢、百炼钢）；只有一句「灌钢法得以推广」的一项（low）；只有设备名而无结构参数的两项（排橐、水力鼓风）。「已挂载」不等于「已记录」。
- **冶铁术出现两说并列**：商代已有铁器说（据《尚书》《诗经》《左传》推断西周开始使用）与春秋战国之交发明说。来源采后说并以藁城台西、平谷刘家河、雍城秦公墓三处考古为据，但三处「铁刃铜」原文末字缺，也未给镍含量检测，陨铁与人工冶铁的界线因此不能由这三处裁定。
- **人工冶铁的上限只有一件器物**：三门峡虢国玉柄铁剑（西周晚期）；正文作「玉柄」而知识链接作「铜柄」，两说并列不裁。
- **两处同段异称**：东汉南阳段先说「铁制鼓风炉」后说「水力鼓风炉」，是同一设备的不同称法还是两种设备未说明；易县农具在两版中作「铁鏤」与「铁鐏」，照录不统一。
- **叠铸的改造方向照录**：「由原来的双孔浇铸改为单孔浇铸」，孔位、孔径与金属液流向差异未说明，不能据此推断效率提升的机制。
- **名实两条不能互释**：「恶金」不是低碳钢，「美金」不等于高锡青铜；「铁氏三兄弟」是 2016 册的现代分类，不是先秦的自我认识。
- **confidence 全 tentative**：medium 13、low 1，无一条 high。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- 生成态陷阱复现并消解：relation 数变化后 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，全量闭包刷新后归 0。与 h13 以来历批一致。
- `--refresh-generated --check-generated` 用于发布前比对：本批未 commit，工作区存在计划内改动，第 17 步 `check generated snapshots`（`git diff --exit-code HEAD`）以 `exit=1` 报漂移，属预期而非失败。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；250 tests + 16 subtests 通过。
- 本批 changed_files 28 = apply-plan 20 行（1 结构节点新建 + 14 主挂载 + 1 Theme 节点更新 + 4 索引更新）+ 8 个闭包重建的生成态／导航文件；归档 `hierarchy/archive/v1.37.md` 按 h44–h46 口径不计入。口径差异：本批起把被改写的 Theme 节点登记为 `structure_node_update` 一行，h45、h46 改写了 B.11 节点但未登记，历史批次未回改。

## 九、未决事项与下一跳

- **B.9 的七线已各有一个 Topic 落点，但货币与农具仍无落点**：B.9 的边界自 v1.28 起就把货币与农具列为「B.9 后续 Topic」，本次仍未物化；两条的材料在库内已有条目（货币类 4 条、农具类 10 余条），但六册把它们与冶铁分开叙述，需另立 Topic 而非并入 B.9.7。
- **铁冶金与农具线的分工需一次显式裁决**：`procedures/sheng-tie-rou-hua-ji-shu` 的例证（洛阳铁锛、大冶六角锄、易县农具）与 `procedures/tiefan-zhuzao` 的器类（镰、锄、双镰、斧、双凿范）都涉及农具，本批以「工序侧归 B.9.7、器形侧归待建农具 Topic」处置，该分工尚未在 Theme 层写下明文边界，留待农具 Topic 建立时对读。
- **家具与木作 Theme 仍是最大缺口**：朱然墓漆几、鸟足漆凭几、黑漆朱绘鸟足漆案、两件宝座的形制谱系都指向尚未建立的家具线。
- **存量结构缺口**：货币 Topic、农具 Topic、前近代服饰与甲胄等级 Theme 未物化。
- **重复候选 reconcile 9 组**未处理：`works/fuhao-jade-figure` 与 `works/fuhao-mu-yuren`；`works/yudiaolong` 与 `works/da-yulong`；`terms/youlihong-ci` 与 `terms/youlihong`；`terms/bai-tao` 与 `terms/shangdai-baitao`；鲁山窑瓷拍鼓与花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` 与 `works/zhulin-qixian-rongqiqi-zhuanhua`；`terms/chunqiu-zhanguo-qingtong-chuishiqi` 与单器条；`terms/huasi` 与 `terms/hua-si-gong-yi`；`terms/pi-pa` 与 `terms/ruan-xian`。
- **图注待核 12 条**、图 7-29 两指问题、未核图版 5-32 仍挂账。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1858、隔离 1149、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- **小债务**：`works/caihui-niaoshou-yuwen-qi-ge.md` 的「相关知识元」把 `simajinlong-mu-qi-pingfeng` 说成「马王堆漆屏风」，与实际文件不符，未擅改。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
