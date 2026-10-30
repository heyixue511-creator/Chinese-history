# h46 髹饰文献与名工：B.11.4「髹饰文献与名工：从《髹饰录》到李芝卿」

## 一、目标与范围

- 包目录：`06-runtime/automation/2026-10-30-hierarchy-pilot-h46/`
- 基线：v1.36（26 Theme／83 Topic／691 membership／681 complete／1889 incomplete／relation 7370／member_of 1372／isolated 1166／ksq 57/65／structural 130）。
- 目标：在 Theme **B.11** 下物化 B.11.4「髹饰文献与名工：从《髹饰录》到李芝卿」，把四部髹饰相关文献与十三位漆艺名工共 17 个 KU 主挂载进去，补齐 h44 登记、h45 仍未物化的文献名工层。
- 结果：v1.37（26 Theme／84 Topic／708 membership／698 complete／1872 incomplete／relation 7404／member_of 1406／isolated 1156／ksq 57/65／structural 130）。B.11 至此四个 Topic、69 个 KU，Theme 收口。
- 来源范围仍为前六本（高丰 2004、夏燕靖 2009、赵农 2009、田自秉 2010、李立新 2011、夏燕靖 2016），第 7 本及以后未启动。

## 二、结构物化

- 新建 Topic `04-knowledge/structure/topics/b11-xiushi-wenxian-yu-minggong.md`：`node_type: topic`、`primary_dimension: B`、`parent_theme: B.11`、`secondary_themes: [C, D]`、`status: pilot`、`date: 2026-10-30`、`research_question` 一句、18 个 tags；七节齐备，支撑材料表 17 行。
- 核心判断有两条。**文献分两种形态**：《髹饰录》是工序书（乾坤二集十八章、三法二戒、材料与弊病、色漆配制与装饰方法），《格古要论》《燕闲清赏笺》是品第式鉴赏（漆器只占一论或数条，记造型、堆漆层数与名家评骘），两种形态不能互相替代——工序书不记器名与款识，鉴赏书不记工序。**名工分三种记载密度**：有作品、尺寸、层数与款识的只有张成、杨茂；有技法归属与风格评语的九位；只有职衔或身份的三位。
- 人书不合并：黄大成是名工，《髹饰录》是文献，二者分列；张德刚、包亮以名工入，果园厂作为官营机构的制度面归 D.6.6。
- B.11 四个 Topic 的分工自此闭合：B.11.1 胎骨与漆层、B.11.2 装饰技法、B.11.3 器物实物、B.11.4 文献与名工；四者不是前后阶段，而是同一批漆器的工序面、装饰面、器物面与记载面。
- 快照：`hierarchy/index.md` 旧版归档为 `hierarchy/archive/v1.36.md`（69342 字节），再改写 index.md 为 v1.37。

## 三、17 个 KU 挂载

全部为主挂载（`primary_theme: B.11`，`role_in_theme` 与 membership 同值，`primary: true`），无次挂载。

- `source_publication` 1：`publications/xiu-shi-lu`（《髹饰录》，唯一漆艺专著）。
- `supporting_source` 3：`publications/gegu-yaolun`（《格古要论》，十三论中含「古漆器」一论）、`publications/yanxian-qingshang-jian`（《燕闲清赏笺》，宋漆器与宋雕漆）、`publications/feiyizhai-jigao`（《废艺斋集稿》，含脱胎一册）。
- `key_person` 13：`persons/huang-dacheng`、`persons/yang-mao`、`persons/zhang-cheng`、`persons/zhang-degang`、`persons/bao-liang`、`persons/zhou-zhu`、`persons/jiang-huihui`、`persons/yang-xun`、`persons/jiang-qianli`、`persons/peng-junbao`、`persons/shen-zhaoan`、`persons/lu-kuisheng`、`persons/li-zhiqing`。

类型与角色：publication 4、person 13；`source_publication` 1、`supporting_source` 3、`key_person` 13。`primary_dimension` 全部为 B，无新增跨维度挂载。B.11 累计 69 个 KU（procedure 6、term 18、work 28、publication 4、person 13）。

## 四、边界处置

- **人书分列**：黄大成与《髹饰录》各占一条，名工的记载密度与文献的成书结构分开评估。
- **通鉴类只取漆器一面**：《格古要论》只取「古漆器」一论及其对元嘉兴剔红的记载，古铜器、古窑器等诸论不入；《燕闲清赏笺》只取宋漆盒盘匣造型与宋雕漆堆朱记载，元绣评语只作旁证。两者以 `supporting_source` 登记，并在 Topic 与 Theme 的未解决问题中同时写明：若日后另立鉴赏文献线，其主归属应重新评估。
- **按维度字段排除**：`publications/nancun-chuogenglu` 的 `primary_dimension` 为 A（古代文献锚点），其「卷素胎骨」条已由 B.11.1 引用，不重复挂载；`persons/shen-fuwen` 是 D 维度教育人物；`institutions/guoyuanchang` 归 D.6.6；`persons/cao-xueqin` 属人物线，《废艺斋集稿》按文献收。
- **单件作品不重复挂**：张成剔红盒、杨茂八方盘等已在 B.11.3，本 Topic 只记名工本人的记载层次。
- **不据名称补条**：《髹饰录》注者杨明未在库内成条，不据文献名目补建；地方志所载匠户同样不补。

## 五、执行与验证

1. 语义裁决先于执行：逐条复读 4 部文献与 13 位名工的 KU 正文与 `sources`，逐条判定 role 与 `scope_note`；机械脚本 `h46_mount.py` 只消费已裁决清单。
2. 来源统计脚本实算：按完整 `evidence_ref.doc_id` 聚合，得田自秉 15（11 唯一）、高丰 4、夏燕靖 2016 3、李立新 2、夏燕靖 2009 1、赵农 2009 1；单册 11、两册 5、五册 1（《髹饰录》）；medium 13、low 4；tentative 17。
3. 写后复核实测：17 个文件 YAML 全部可解析，`primary_theme == 'B.11'`、`primary_dimension == 'B'`、`topic_memberships` 长度 1 且 `primary is True`、Topic 路径一致，`bad 0`；`hierarchy_scope_note` 中「Theme/Topic 尚未 materialize」全部消去。
4. `python scripts/hierarchy_stress_test.py`：v1.37、26 Theme、84 Topic、708 membership、698 complete、1872 incomplete、`cross_dimension_topics` 为空、`apply_permitted: false`。
5. `python scripts/build_relation_index.py`：7370→7404（explicit 5998 不变，inferred／member_of 1372→1406）。
6. `python scripts/write_current_health.py`：v1.37、complete 698、missing 1872、relation 7404、structural 130/130、ksq 57/65、content 0。
7. `python scripts/audit_relation_consistency.py`：isolated 1166→1156（减 10，见第六节）；broken target 0、invalid relation_type 0、missing inverse 0。
8. `python scripts/run_sync_closure.py --refresh-generated --full`：250 tests + 16 subtests 通过；刷新前 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，刷新后归 0。
9. apply-plan 22 行逐行复核 `after_sha256` 与磁盘一致（`rows 22 bad 0`）；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动；分支 `main`、单一 worktree、HEAD 仍为 `c249c6fe`。

## 六、指标变化

| 指标 | v1.36 | v1.37 | 变化 |
|---|---|---|---|
| Theme | 26 | 26 | 0 |
| Topic | 83 | 84 | +1（B.11.4） |
| topic_memberships | 691 | 708 | +17 |
| 已完成挂载 KU | 681 | 698 | +17 |
| 未挂载 KU | 1889 | 1872 | −17 |
| B 维度未挂载 | 1174 | 1157 | −17 |
| relation_index | 7370 | 7404 | +34 |
| member_of | 1372 | 1406 | +34 |
| 隔离单元 | 1166 | 1156 | −10 |
| structural_health | 130/130 | 130/130 | 0 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| content_findings | 0 | 0 | 0 |

relation 增量 34 = 17 条主挂载 ×（topic `member_of` + theme `member_of`）。隔离单元减 10 而非 17，因为实测 17 条中有 7 条原已有显式关系。B 维度减 17，因为 17 条主挂载的 `primary_dimension` 全部为 B。membership 仍比 KU 多 10，双挂载与次挂载清单不变。

## 七、语义边界（并列不裁）

- **两种文献形态不能互换**：《髹饰录》记工具、材料、弊病、色漆配制与装饰方法，不记器名与款识；《格古要论》《燕闲清赏笺》记造型、堆漆层数与名家评骘，不记工序。把后者当作技法史料使用，会把评语当工序。
- **名工的三种密度对应三种证据强度**：只有张成（约 80 层、针刻「张成造」）与杨茂（渣斗径 12.8、高 9.5 厘米）可反查实物；九位只有一句评价；张德刚、包亮、蒋回回连作品都没有。三者不能并列引用。
- **谱系线只有一处**：张成—张德刚是六册中唯一写明的师承关系；其余十二位名工各自孤悬，地域线（嘉兴、扬州、苏州、吴中、新安、福州）比谱系线完整。本 Topic 因此不排师承谱。
- **东传是双向的**：张成、杨茂被日本取字合称「堆朱杨成」，杨埙反向赴日本学倭漆而成「杨倭漆」。不能写成单向输出或单向输入。
- **清代以后名工转向品种创新**：沈沼安的脱胎、卢葵生的漆沙砚、李芝卿的赤宝砂都创新品种而非改良既有技法，与元明名工以剔红、戗金、螺钿得名的路径不同。
- **归类是有保留的**：黄大成名字三写、《髹饰录》成书年代两说、彭君宝村名「西塘／斜塘」两写，均照录不裁；《格古要论》《燕闲清赏笺》的通鉴性质使本 Topic 的挂载只代表「漆器一面」的主张，不代表二者在知识体系中的主归属。
- **confidence 全 tentative**：medium 13、low 4，无一条 high。

## 八、生成态与门禁

- 生成态刷新：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`05-outputs` 导航、`generated-projections-manifest.json` 均由脚本重建，未手改。
- 生成态陷阱复现并消解：relation 数变化后 `audit_rule_drift.py` 报 `runtime_index_snapshot_stale` 与 `output_navigation_snapshot_stale` 两项，全量闭包刷新后归 0。
- 编码：全部写入文件为 UTF-8 无 BOM、LF；250 tests + 16 subtests 通过。
- 本批 changed_files 30 = apply-plan 22 行（1 结构节点新建 + 17 主挂载 + 4 索引更新）+ 8 个闭包重建的生成态／导航文件；归档 `hierarchy/archive/v1.36.md` 按前两批口径不计入，README.md 与其余 `04-knowledge` 改动属 h13–h45 未提交批次。

## 九、未决事项与下一跳

- **B.11 已收口**：四个 Topic（胎骨与漆层、装饰、实物、文献与名工）覆盖 69 个 KU，h44 登记的两个候选池全部物化。剩余的是内部对接：**《髹饰录》十八章分类体系与 B.11.2 的十六条技法术语之间仍缺逐条对照表**；注者杨明在库内无人物条目。
- **通鉴类文献的主归属待评估**：《格古要论》《燕闲清赏笺》目前只以漆器一面挂 B.11.4，若日后另立鉴赏文献线（铜、瓷、漆、锦并置的品第体系），应重新评估其主 Theme。
- **家具与木作 Theme 仍是最大缺口**：朱然墓漆几、鸟足漆凭几、黑漆朱绘鸟足漆案、两件宝座的形制谱系都指向尚未建立的家具线。
- **存量结构缺口**：铁器与叠铸 Topic、货币与农具 Topic、前近代服饰与甲胄等级 Theme 未物化。
- **重复候选 reconcile 9 组**未处理：`works/fuhao-jade-figure` 与 `works/fuhao-mu-yuren`；`works/yudiaolong` 与 `works/da-yulong`；`terms/youlihong-ci` 与 `terms/youlihong`；`terms/bai-tao` 与 `terms/shangdai-baitao`；鲁山窑瓷拍鼓与花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` 与 `works/zhulin-qixian-rongqiqi-zhuanhua`；`terms/chunqiu-zhanguo-qingtong-chuishiqi` 与单器条；`terms/huasi` 与 `terms/hua-si-gong-yi`；`terms/pi-pa` 与 `terms/ruan-xian`。
- **图注待核 12 条**、图 7-29 两指问题仍挂账；本批新增未核图版 5-32。
- **A 维度遗留**：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- **存量债务**：未挂载 1872、隔离 1156、单源与 tentative 条目按既有 backlog 处理；`knowledge_structure_quality` 缺口仍在 `hierarchy_assignment`（2/10）。
- **小债务**：`works/caihui-niaoshou-yuwen-qi-ge.md` 的「相关知识元」把 `simajinlong-mu-qi-pingfeng` 说成「马王堆漆屏风」，与实际文件不符，未擅改。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。
