# 2009 册 units 批次 AR 摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-26-2009xiayanjing-units-batch-ar/`
- 来源：夏燕靖《中国设计史》（2009），doc_id `2009-xiayanjing-zhongguo-shejishi`
- 候选范围：2009 册 unit 候选 24 条（cand-03）
- 裁定结果：新建 15 条、更新 4 条、no_delta 5 条、rejected 0 条
- 状态：applied（24 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

24 个候选共 24 处来源区间，并集 216 行：

`L1319-L1332, L1380-L1387, L1388-L1391, L1418-L1432, L1442-L1445, L1446-L1461, L1462-L1469, L1472-L1490, L1487-L1489, L1516-L1521, L1539-L1544, L1559-L1573, L1590-L1593, L1594-L1606, L1683-L1701, L1695, L1708-L1713, L1714-L1717, L1718-L1732, L1787-L1790, L1791-L1826, L1811-L1826`

其中 L1539-L1544 由双辕车、斧车两候选共读；L1590-L1593 由上林苑、一池三岛两候选共读；L1487-L1489 由汉代青瓷候选单读，落在 L1472-L1490 的陶瓷段内；L1791-L1826 与 L1811-L1826 由衲裆、杂裾垂髯两候选交叠复读。L1695 为魏晋南北朝青瓷窑口候选的单行区间。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-03-08 | 犁壁 | create | `terms/li-bi.md` |
| cand-03-109 | 魏晋南北朝青瓷窑口 | no_delta | `terms/qing-ci.md` |
| cand-03-110 | 汉代青瓷 | update | `terms/qing-ci.md` |
| cand-03-16 | 虹管灯（缸灯） | create | `terms/hong-guan-deng.md` |
| cand-03-18 | 汉代铜壶（钟、钫） | no_delta | `terms/hu-vessel.md` |
| cand-03-24 | 绒圈锦（起毛锦） | create | `terms/rongquan-jin.md` |
| cand-03-27 | 秦代服饰 | create | `terms/qin-dai-fu-shi.md` |
| cand-03-28 | 汉代袍服 | create | `terms/han-dai-pao-fu.md` |
| cand-03-29 | 汉代妇女深衣 | update | `terms/shenyi.md` |
| cand-03-30 | 始皇陵夔凤纹大瓦当 | create | `works/shihuangling-kuifengwen-dawadang.md` |
| cand-03-38 | 金银扣器 | update | `terms/kouqi.md` |
| cand-03-42 | 双辕车 | create | `terms/shuang-yuan-che.md` |
| cand-03-43 | 斧车 | create | `terms/fu-che.md` |
| cand-03-48 | 橹 | create | `terms/lu-oar.md` |
| cand-03-53 | 上林苑 | create | `places/shanglinyuan.md` |
| cand-03-54 | 一池三岛 | no_delta | `terms/yichi-sanshan.md` |
| cand-03-56 | 汉代家具 | create | `terms/han-dai-jia-ju.md` |
| cand-03-69 | 鸡头壶（天鸡壶） | no_delta | `terms/tianji-hu.md` |
| cand-03-73 | 黑釉四系盘口壶 | create | `works/hei-you-si-xi-pan-kou-hu.md` |
| cand-03-74 | 白釉绿彩四系莲瓣缸 | create | `works/bai-you-lv-cai-si-xi-lian-ban-gang.md` |
| cand-03-75 | 北方铅釉陶 | update | `terms/qian-you-tao.md` |
| cand-03-84 | 幅巾 | create | `terms/fujin.md` |
| cand-03-86 | 衲裆 | create | `terms/na-dang.md` |
| cand-03-87 | 杂裾垂髯 | no_delta | `terms/zaju-chuishao-fu.md` |

## 4. 新建 15 条

**秦汉农具与铜器（2）**：犁壁、虹管灯（缸灯）。

**秦汉纺织与服饰（3）**：绒圈锦（起毛锦）、秦代服饰、汉代袍服。

**秦汉车船与家具（4）**：双辕车、斧车、橹、汉代家具。

**秦汉至北朝陶瓷（3）**：始皇陵夔凤纹大瓦当、黑釉四系盘口壶、白釉绿彩四系莲瓣缸。

**秦汉园林与魏晋南北朝服饰（3）**：上林苑、幅巾、衲裆。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，日期 created/updated/last_verified 为 2026-10-26、review_due 为 2027-04-26。15 条 `academic_translation_status` 均为 `provisional`，因来源未给英文名。

类型处理说明：

- `terms/rongquan-jin.md`：候选原标 `unit_type: work`，但绒圈锦是织锦类型，不是单件作品，按 term 写回；`hierarchy_scope_note` 已记录该判断。
- `places/shanglinyuan.md`：候选原标 `unit_type: work`，但上林苑是宫苑空间，按 place 写回；`hierarchy_scope_note` 已记录该判断。
- `works/shihuangling-kuifengwen-dawadang.md`：以单件器物立 work 锚点，瓦当类型仍由既有 `terms/wadang.md` 承载。
- `works/hei-you-si-xi-pan-kou-hu.md`、`works/bai-you-lv-cai-si-xi-lian-ban-gang.md`：以有明确器名与收藏/出土背景的单件器物立 work 锚点。

## 5. 更新 4 条

- `terms/qing-ci.md`：补汉代早期青瓷、浙江上虞/余姚/宁波/永嘉东汉窑址、陶瓷共烧与专门瓷窑、龙窑 1300℃、高岭土原料、早期品种与挂釉装饰、汉代后期陶瓷普及与装饰方法；`source location` 改为 `L1487-L1489, L1677-L1682`，`version` 2→3，`source_count` 仍为 3（赵农、夏燕靖 2009、夏燕靖 2016）。
- `terms/kouqi.md`：补汉代金银扣器价值为同类铜器 10 倍、《盐铁论》引文、汉代漆器生产组织与六至八道工序；新增“四、汉代金银扣器（夏燕靖 2009）”一节；`source location` 改为 `L947, L1520`，`version` 1→2，`source_count` 仍为 3。
- `terms/qian-you-tao.md`：补北魏施釉创新、黄地/白地加绿彩与黄绿褐三彩、山西大同太和八年（484）深绿釉陶器、山东高唐寨里窑酱色釉陶器、北齐釉层匀润；`source location` 改为 `L1497-L1500, L1722`，`version` 2→3。
- `terms/shenyi.md`：补“长沙马王堆汉墓女主人在帛画中的穿着服式是可信的具体形象资料”一条；`source location` 改为 `L1444, L1457, L1462-L1466`，`version` 1→2。

四条均只并入既有条目缺载的 2009 册事实，不另立“汉代青瓷”“金银扣器”“北方铅釉陶”“汉代妇女深衣”等按时代或地域切分的近义条，避免同一实体碎片化。

## 6. no_delta 5 条

| 候选 | 既有承载 | 理由 |
|---|---|---|
| 魏晋南北朝青瓷窑口 | `terms/qing-ci.md` | 已逐项覆盖越、瓯、婺、德清四窑口及南北差异，窑口分类无新增事实 |
| 汉代铜壶（钟、钫） | `terms/hu-vessel.md` | 已载汉代圆壶称钟、方壶称钫、量器性质与鼓腹小颈、铺首衔环等器形定式 |
| 一池三岛 | `terms/yichi-sanshan.md` | 已载秦上林苑长池蓬莱山、汉武帝扩大 150 公里与离宫 70 所、建章宫太液池三岛 |
| 鸡头壶（天鸡壶） | `terms/tianji-hu.md` | 已载盘口壶基础、鸡头装饰、东晋加长与唐代龙耳壶，候选无超出内容 |
| 杂裾垂髯 | `terms/zaju-chuishao-fu.md` | 已载纤髯、华髯、华带飞髯、南北朝去长带加尖角、北魏左衽窄袖与女子服用 |

## 7. 语义判断与内部张力

1. **绒圈锦的层级纠正**：候选摘要把它标为 work，但来源句“织锦中有一种立体感极强的绒圈锦（起毛锦）”定义的是织锦类型；单件织物实例与织造技术分别由 `works/` 与 `terms/tihuaji.md` 承载，故按 term 写回，并在条目内显式记录候选类型与写回类型的差异。
2. **上林苑的层级纠正**：候选标为 work，但来源叙述的是秦代始建、汉武帝修复扩大的皇家苑囿，属于可容纳多个建筑与景观要素的场所，按 place 写回；其“一池三岛”布局范式仍由 `terms/yichi-sanshan.md` 承载，二者分工为空间实体与设计范式。
3. **青瓷按瓷种合并、不按时代拆分**：cand-03-110 的汉代青瓷事实并入 `terms/qing-ci.md`，cand-03-109 的四窑口判 no_delta；若另立“汉代青瓷”“魏晋青瓷窑口”会使同一瓷种按时代碎片化。该条现已同时容纳赵农的东汉末年说、2016 的商代中期说与 2009 的汉代早期说，三说并列不裁定。
4. **扣器按器类合并**：cand-03-38 的“金银扣器”是扣器的高档形态，既有 `terms/kouqi.md` 已载战国铜箍扣器；新增“汉代金银扣器”一节，保留来源中“金属铸器铭文”与漆器生产并置的文本张力，不据“金属铸器”推断漆器铭文必铸于金属器。
5. **铅釉陶按工艺总类合并**：cand-03-75 的北方铅釉陶并入 `terms/qian-you-tao.md`，不另立“北方铅釉陶”；该条现覆盖汉代低温铅釉到北朝施釉创新，`hierarchy_scope_note` 与正文 scope 同步改为“汉代至北朝”。
6. **深衣按形制总类合并**：cand-03-29 的汉代妇女深衣并入 `terms/shenyi.md`，只补马王堆帛画形象资料；深衣的起始时代、直裾归属与服用等级三组分歧仍按既有条目并列，不因新增汉代材料而裁定。
7. **瓦当的 work/term 分工**：`terms/wadang.md` 已载始皇陵夔凤纹大瓦当的尺寸事实，但那是类型条中的实例；本批以 `works/` 立单件器物锚点，记直径、生产背景与“原文未载”的纹样构图，二者不重复。
8. **鸡头壶判 no_delta**：`terms/tianji-hu.md` 为三源条，已覆盖鸡头壶的盘口、鸡头装饰、东晋加长与唐代龙耳壶；候选所述内容未超出既有条，故不新建 `works/` 单件条。
9. **铜壶判 no_delta**：`terms/hu-vessel.md` 已完整承载汉代铜壶的钟/钫称谓、量器性质与器形定式，候选只是同段复述，故不另立“汉代铜壶”条。
10. **引文与图版边界**：新建条目以来源复读后的概述为主，未把来源图版当作已视觉核验的材料；`qin-dai-fu-shi` 删除误挂的图 4-14、4-15，`fu-che` 明确图 4-23、4-24 为记里鼓车与指南车，`han-dai-jia-ju` 明确图 4-28 至 4-30 为建筑屋顶，`lu-oar` 明确图 4-25 图注为“舵”而非橹。
11. **别名清理**：删除来源未直接使用的“汉袍”“汉上林苑”“汉代竹木家具”“德清窑黑釉四系盘口壶”“白釉绿彩莲瓣缸”等描述性别名；保留来源原词“缸灯”“起毛锦”“秦服”“轻车”“双辕马车”“秦上林苑”。
12. **引证范围校正**：`rongquan-jin` 的引证由 L1424 扩为 L1422-L1429，以覆盖马王堆丝织、汉锦特征与图 4-12 图注；`hei-you-si-xi-pan-kou-hu` 补 L1725 图注，`bai-you-lv-cai-si-xi-lian-ban-gang` 补 L1728 图注，使“晋代”“北齐”的年代判断可回溯到图注原文。

## 8. 生成态与门禁

- 工作包：apply-plan 19 行（15 create、4 update）、candidate-decision-ledger 72 行（24×3）、canonical-mapping 24 条、manifest 1 份。
- 引文审计：19 个改动文件的新增正文与 frontmatter 中，凡使用 ASCII 双引号的来源引文均与 2009 册源文去空白比对；新增内容无未匹配引文。比对中出现的 3 处未匹配项均为 `kouqi`、`shenyi` 旧有段落中来自高丰 2004 或夏燕靖 2016 的引文，因重排被差异算法计为新增，不属本批新引文。
- 索引重建：`python scripts/build_discovery_index.py` 已运行；total 5339 不变，applied 1448→1467、no_delta 123→128、needs_evidence 2956→2932、rejected 812 不变。
- 内容质量审查：`python scripts/audit_content_quality.py` 审查 1302 个知识元，总发现 0。
- 生成态：`python scripts/run_sync_closure.py --refresh-generated --full` 18 步全部通过（250 tests passed, 16 subtests passed）；随后 `--check-generated` 17/17 FAILED exit=1，差异为 `06-runtime/state/generated-projections-manifest.json`、`06-runtime/automation/index.md`、`current-health.json`、`governance-backlog.md` 等工作树快照相对 HEAD 的未提交变化（automation 文件数 437→447、knowledge/quality 文件数 1315→1340），属 `blocked_pending_commit` 的设计行为，不是内容审查失败。

## 9. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- `works/shihuangling-kuifengwen-dawadang.md` 为 low confidence：来源只给直径与“形体之大少有”的评价，未给夔凤纹构图、边轮、当心、出土位置与收藏地。
- 2009 册 unit 候选剩余 40 条未处理；其余五册 unit 候选与 1363 条 claim 候选未启动，claim-registry 仍为空表。
- Book 7 及以后不启动（用户范围限定）。
