# h48 农具与农业技术：B.12「农具与农业技术：耕作、收割与提水」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h48/`
- 基线：v1.38（26 Theme／85 Topic／722 membership／712 complete／1858 incomplete／relation 7432／member_of 1434／isolated 1149／ksq 57/65／structural 130）。
- 目标：另立 Theme **B.12**「农具与农业技术：耕作、收割与提水」，下建 B.12.1、B.12.2、B.12.3 三个 Topic，把前六册中农具、农业作业与农书的 30 个 KU 主挂载进去。
- 结果：v1.39（27 Theme／88 Topic／752 membership／742 complete／1828 incomplete／relation 7492／member_of 1494／isolated 1135／ksq 57/65／structural 130）。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Theme `04-knowledge/structure/themes/b12-nongju-yu-nongye-jishu-gengzuo-shouge-yu-tishui.md`：`node_type: theme`、`theme_code: B.12`、`primary_dimension: B`、`secondary_dimensions: [D]`、`status: pilot`、20 个 tags；核心问题、边界、下属 Topic、支撑结构、未解决问题五节齐备。
- 新建三个 Topic：B.12.1「耕作与播种：从耒耜到曲辕犁」（支撑表 18 行）、B.12.2「收割、加工与提水：镰、磨、翻车与辘轳」（8 行）、B.12.3「农书：从《耒耜经》到《农政全书》」（4 行），七节齐备。
- 核心判断有四条。**覆盖极不对称是本 Theme 的第一事实**：赵农 2009 一册覆盖 21 条（70%），夏燕靖 2016 覆盖 10 条，夏燕靖 2009 覆盖 4 条，李立新 2 条，高丰 1 条，田自秉 2010 一条也没有。田自秉把工艺美术的对象限定在器物与装饰，农具被排除在外；六册均未明说该取舍，本批只记覆盖数字而不代为判断。**材料递进线全是断语**：良渚石犁是否用于犁耕「学界尚有争议」、商代青铜犁铧只有一句且无器形与出土地、西周青铜锄与青铜镰各只有一件、铁制农具的推广只有种类名单；因此三十条拒绝排成石—骨—青铜—铁演化线，只按作业环节分组。**形制层与操作组织层是两套证据**：形制层（犁壁、犁刀、曲辕犁的辕箭梢底重组、铁搭四齿六齿、踏犁横木）是部件名加功能句，操作组织层（耦犁二牛三人、三脚耧一次三行、踏犁脚踏）是分工描述，两层不互相推导。**农书与器物从未对读**：《王祯农书》「有农器图谱」、《耒耜经》「载耙、砺、夯」，而 B.12.1、B.12.2 的器物条没有一条引用农书原文。
- 快照：`hierarchy/index.md` 旧版归档为 `hierarchy/archive/v1.38.md`（73001 字节），再改写 index.md 为 v1.39。

## 三、30 个 KU 挂载

全部为主挂载（`primary_theme: B.12`，`role_in_theme` 与 membership 同值，`primary: true`），无次挂载。

- **B.12.1 耕作与播种（18）**：`terms/yuanshi-nongju`、`terms/gusi`、`terms/leisi`、`persons/shennong-shi`、`procedures/daogeng-huozhong`、`terms/liangzhu-shili`、`works/zhuangbing-shican-fuyuan-tu`、`terms/qingtong-lihua`、`terms/li-bi`、`terms/lidao`、`terms/quyuan-li`、`terms/ou-li`、`persons/zhao-guo`、`works/san-jiao-lou`、`terms/iron-farm-tools`、`terms/qingtong-chu`、`terms/tieda`、`terms/tali`。role 为 `term_anchor` 13、`key_person` 2、`representative_work` 2、`procedure` 1。
- **B.12.2 收割、加工与提水（8）**：`terms/shilian`、`terms/qingtong-lian`、`terms/shimopan-mobang`、`works/peiligang-shimopan`、`terms/shi-mo`、`works/fanche-longgu-shuiche`、`terms/windlass`、`terms/jiegou-well-sweep`。role 为 `term_anchor` 6、`representative_work` 2。
- **B.12.3 农书（4）**：`publications/leisi-jing`、`publications/wang-zhen-nongshu`、`publications/nongsang-jizao`（`source_publication`），`publications/nongzheng-quanshu`（`supporting_source`）。

类型与角色：term 19、work 4、publication 4、person 2、procedure 1；`term_anchor` 19、`representative_work` 4、`source_publication` 3、`key_person` 2、`procedure` 1、`supporting_source` 1。`primary_dimension` 全部为 B，无新增跨维度挂载。

## 四、边界处置

- **承接 h47 的显式清单**：h47 manifest 与 summary 把农具类逐条列名（犁壁、犁刀、曲辕犁、耦犁、踏犁、铁搭、V 形铁铧冠、铁制农具等）并写明「归待建农具 Topic；农具在六册中与冶铁分开叙述」。本批按该清单核对 18 条耕作播种与 8 条收割加工提水条目，全部落在原清单内；铁器工序侧仍归 B.9.7、器形侧归 B.12，分工自此闭合。
- **不收磨制石器**：`procedures/mozhi-shiqi` 是一般石器工艺而非农具，只作石铲、石犁的技术前提引用。
- **不收水利工程**：都江堰、郑国渠、灵渠、西门渠是灌溉工程与土木营造，归待建水利 Topic 或 B.3；本 Theme 只取翻车、辘轳、桔槔三件器具。
- **不收农政制度与礼俗**：`institutions/sinongsi`、`terms/jingtian-zhi`、`terms/nangeng-nvzhi`、`works/xiannongtan`、`events/xiaowendi-jiangquan-nongsang` 的 `primary_dimension` 为 D，归 D 维度。
- **不收图像与文献旁支**：`works/gengzhi-tu` 为 C、`publications/nancun-chuogenglu` 为 A，均不入。
- **不合并近似名**：石磨（战国以后旋转式，砂岩石直径约 55 厘米）与石磨盘磨棒（新石器研磨式）分立为两条；耒耜的文献名义与骨耜的实物形制分立为两条，`scope_note` 互指而不合并。
- **降级挂载**：`publications/nongzheng-quanshu` 全条只有赵农一句「保留了许多农具和其他生产器具的资料」，无卷数、年代、版本与器目，以 `supporting_source` 挂载，使「一句总评」在表内可追踪而不抬高其证据地位。
- **不据名称补条**：`works/baolian-zaojing`（藻井）与农具无关，按名称相近排除。

## 五、执行与验证

1. 语义裁决先于执行：先扫描 B 维度未挂载 KU 得 27 条农具相关，逐条读毕描述与 `hierarchy_scope_note`；再补扫 5 条（神农氏、刀耕火种、农桑辑要、王祯农书、装柄石铲复原图），最终定下 30 条与三个 Topic 的分工，机械脚本 `h48_mount.py` 只消费已裁决清单。
2. 来源统计脚本实算：按完整 `evidence_ref.doc_id` 聚合（不用年份正则），得赵农 2009 覆盖 21 条、夏燕靖 2016 覆盖 10 条、夏燕靖 2009 覆盖 4 条、李立新 2 条、高丰 1 条、田自秉 0 条；单册 26、两册 1、三册 2、四册 1；medium 21、low 9；tentative 30。
3. 写后复核实测：30 个文件 YAML 全部可解析，`primary_theme == 'B.12'`、`primary_dimension == 'B'`、`topic_memberships` 长度 1 且 `primary is True`、role 与 `role_in_theme` 一致，`bad []`；role 实测 `term_anchor` 19、`representative_work` 4、`source_publication` 3、`key_person` 2、`procedure` 1、`supporting_source` 1；`hierarchy_scope_note` 中「Theme/Topic 尚未 materialize」全部消去。
4. `python scripts/hierarchy_stress_test.py`：v1.39、27 Theme、88 Topic、752 membership、742 complete、1828 incomplete、`cross_dimension_topics` 为空、`apply_permitted: false`。
5. `python scripts/build_relation_index.py`：7432→7492（explicit 5998 不变，inferred／member_of 1434→1494）。
6. `python scripts/write_current_health.py`：v1.39、complete 742、missing 1828、structural 130/130、ksq 57/65、content 0。
7. `python scripts/audit_relation_consistency.py`：isolated 1149→1135（减 14，见第六节）；broken target 0、invalid relation_type 0、missing inverse 0。
8. `python scripts/run_sync_closure.py --refresh-generated --full`：250 tests + 16 subtests 通过；刷新前 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，刷新后归 0。
9. apply-plan 38 行逐行复核 `after_sha256` 与磁盘一致（`rows 38 bad []`）；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree、HEAD 仍为 `c249c6fe`。

## 六、指标变化

| 指标 | v1.38 | v1.39 | 变化 |
|---|---|---|---|
| Theme | 26 | 27 | +1（B.12） |
| Topic | 85 | 88 | +3（B.12.1–B.12.3） |
| topic_memberships | 722 | 752 | +30 |
| 已完成挂载 KU | 712 | 742 | +30 |
| 未挂载 KU | 1858 | 1828 | −30 |
| B 维度未挂载 | 1143 | 1113 | −30 |
| relation_index | 7432 | 7492 | +60 |
| member_of | 1434 | 1494 | +60 |
| 隔离单元 | 1149 | 1135 | −14 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 60 = 30 条主挂载 ×（topic `member_of` + theme `member_of`）。隔离单元减 14 而非 30，因为实测 30 条中有 16 条原已有显式关系。B 维度减 30，因为 30 条主挂载的 `primary_dimension` 全部为 B。membership 仍比 KU 多 10，双挂载与次挂载清单不变。

## 七、语义边界（并列不裁）

- **覆盖不对称只作记录不作评价**：赵农一册覆盖 21 条、田自秉 0 条。本库不据此判定田自秉「漏收」或赵农「过详」——六册的取材对象本来就不同，但六册也都没有明说取舍标准，因此该判断只以覆盖数字呈现。
- **材料线不排成演化线**：三十条按「耕作—收割加工提水—文献」分组，不按石—骨—青铜—铁分组。若按材料排，骨耜（骨）会排到石犁（石）之后，而来源的叙述顺序相反；分组的依据是作业环节，不是技术难度或年代。
- **形制层与操作组织层不互推**：曲辕犁「一牛耕犁取代二牛抬杠」是形制变化带来操作变化的唯一明写，其余各条都不说明形制与人力、畜力配置的对应关系。
- **效率判断只有一条**：三脚耧「开沟、下种、覆盖三工序合并于一机」并被称为「现代播种机的雏形」；犁壁「提高了耕作效率」、铁制农具「廉价高效」都是无数据的形容。
- **良渚石犁的争议照录**：同一 KU 内「我国最早实现犁耕的地区」与「学界尚有争议」两句并列，本批不裁。
- **赵过的两说分工照录**：夏燕靖两版作三脚耧设计者、赵农作耧车与耦犁推行者；「代田法」六册一次也未出现，不补。
- **《王祯农书》四说不选正**：卷数、部分名与字数四册互不相同，高丰一处并把书名误作《农布》；来源未给版本，选正即等于引入来源外信息。
- **农政与农具、工程与器具两处分界是本库取舍**：赵过的官职与推广组织、司农司官署归 D 维度，都江堰等渠堰归待建水利 Topic；六册并未作此分界，分界由本库为守住 Theme 边界而设。
- **confidence 全 tentative**：medium 21、low 9，无一条 high；B.12.2 八条全为单册、四条 low，整条 `confidence` 记为 low。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- 生成态陷阱复现并消解：relation 数变化后 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，全量闭包刷新后归 0。与 h13 以来历批一致。
- `--refresh-generated --check-generated` 用于发布前比对：本批未 commit，工作区存在计划内改动，第 17 步 `check generated snapshots`（`git diff --exit-code HEAD`）以 `exit=1` 报漂移，属预期而非失败。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；250 tests + 16 subtests 通过。
- 本批 changed_files 46 = apply-plan 38 行（1 个 Theme 新建 + 3 个 Topic 新建 + 30 条主挂载 + 4 个索引更新）+ 8 个闭包重建的生成态／导航文件；归档 `hierarchy/archive/v1.38.md` 按 h44–h46 口径不计入。本批无需 Theme 节点更新行：被改写的 Theme 是新建的 B.12，已由 `structure_node_create` 覆盖。

## 九、未决事项与下一跳

- **农具线已物化，货币线仍空**：h47 manifest 登记的「货币 Topic、农具 Topic 未物化」中农具一项自此闭合；元代纸币、金代交钞、人民币与大清银币仍无落点，且 B.9 的边界自 v1.28 起就把货币列为「B.9 后续 Topic」。
- **水利工程线仍未物化**：都江堰、郑国渠、灵渠、西门渠四条在库内已有条目，本批以「本 Theme 只取提水器具」处置；若另立水利 Topic，须与 B.3（建筑与建造技术）作一次显式分工。
- **农政制度侧无落点**：赵过的搜粟都尉、司农司、井田制、男耕女织、先农坛与孝文帝劝农桑全在 D 维度，D 维度前近代线目前只有 D.6（官府手工业）六点，农政不在其中。
- **家具与木作 Theme 仍是最大缺口**：朱然墓漆几、鸟足漆凭几、黑漆朱绘鸟足漆案、两件宝座的形制谱系都指向尚未建立的家具线；本批的`terms/tieda`、`terms/tali` 虽属木作器具，但对象是农具，不并入家具。
- **前近代服饰与甲胄等级 Theme 未物化**。
- **重复候选 reconcile 9 组**未处理：`works/fuhao-jade-figure` 与 `works/fuhao-mu-yuren`；`works/yudiaolong` 与 `works/da-yulong`；`terms/youlihong-ci` 与 `terms/youlihong`；`terms/bai-tao` 与 `terms/shangdai-baitao`；鲁山窑瓷拍鼓与花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` 与 `works/zhulin-qixian-rongqiqi-zhuanhua`；`terms/chunqiu-zhanguo-qingtong-chuishiqi` 与单器条；`terms/huasi` 与 `terms/hua-si-gong-yi`；`terms/pi-pa` 与 `terms/ruan-xian`。
- **图注待核 12 条**、图 7-29 两指问题、未核图版 5-32 仍挂账；本批新增五处未核图版（图 1-6、图 1-8、图 5-5、图 5-6、装柄石铲复原图）。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1828、隔离 1135、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- **小债务**：`works/caihui-niaoshou-yuwen-qi-ge.md` 的「相关知识元」把 `simajinlong-mu-qi-pingfeng` 说成「马王堆漆屏风」，与实际文件不符，未擅改。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
