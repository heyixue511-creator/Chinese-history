# h50 层级试点批次总结：B.14 家具与起居方式

- 批次：`2026-10-30-hierarchy-pilot-h50`
- profile：`hierarchy-pilot-v1`
- 层级版本：v1.40 → v1.41
- 变更文件：51（apply-plan 43 行 + 闭包重建的 8 个生成态／导航文件）
- 结论：家具器物层自此有 Theme 与两个 Topic；木作工艺层、风格层与近代家具线仍未物化。

---

## 一、目标与范围

本批要闭合 h49 summary 第九节与 manifest `unresolved` 同时登记的一条债务：「家具与木作 Theme 仍是最大缺口：朱然墓漆几、鸟足漆凭几、黑漆朱绘鸟足漆案、两件宝座的形制谱系都指向尚未建立的家具线」。

范围限定在前六册（2004 高丰、2009 夏燕靖、2009 赵农、2010 田自秉、2011 李立新、2016 夏燕靖升级版）内已存在的 KU，不新增来源、不改写 `02-sources/`、不新建 KU、不回改 B.11 主题文件正文。

基线（v1.40）：Theme 28、Topic 90、Topic membership 762、完成五级字段挂载 752、未完成 1818、relation 7512（explicit 5998／inferred 1514）、隔离单元 1131、KU 2570、B 维度未挂载 1103、结构健康 130/130、知识结构质量 57/65。

---

## 二、结构物化

新建 **Theme B.14「家具与起居方式：坐卧具、屏风与承具」**（`structure/themes/b14-jiaju-yu-qiju-fangshi-zuowoju-pingfeng-yu-chengju.md`）：

- `node_type: theme`、`theme_code: B.14`、`primary_dimension: B`、`secondary_dimensions: [D, C]`、`status: pilot`、`date: 2026-10-30`。
- 核心问题三条：家具的高度变化是器物史还是起居方式史；器物层极厚而数据层极薄；家具在六册中没有独立位置。
- 边界纳入坐具 20 项与卧具／屏风／承具 16 项；排除建筑与营造、图像本体、纺织与夹缬屏风、漆器髹饰、青铜器本体、交通器具、近代家具线、木作工艺与风格层。

下建两个 Topic：

| 代码 | 标题 | 挂载 | 分工 |
|---|---|---|---|
| `B.14.1` | 起居方式与坐具：从跽坐到垂足而坐 | 20 | 回答人怎样坐、坐具怎样随坐姿变高 |
| `B.14.2` | 卧具、屏风与承具：床榻、屏风、几案桌椅 | 16 | 回答人怎样卧、怎样围合空间、怎样承放器物 |

这一刀是本库取舍，不是来源的分组：六册从未把家具立章，家具材料分散在建筑（汉代竹木作业与木构架）、漆器（漆木家具与马王堆漆屏风）、起居（跽坐与胡床）与工艺（明式清式）各章，榻本身「实际是一种小床」，坐具与卧具常在同段并列。分工已在 Theme 与两个 Topic 三处写明。

层级版本升 v1.41：Theme 28 → 29，Topic 90 → 92，并归档旧版 `hierarchy/archive/v1.40.md`（79147 字节）。

---

## 三、36 个 KU 挂载

`h50_mount.py` 输出 `mounted 36 bad []`；`h50_verify.py` 以 `yaml.safe_load` 复验 36 个 KU frontmatter，输出 `kUs 36 bad []`：

| 维度 | 分布 |
|---|---|
| Topic | B.14.1 20；B.14.2 16 |
| 类型 | term 35；work 1 |
| role | `term_anchor` 31；`representative_work` 1；`boundary_case` 2；`historical_context` 2 |
| confidence | medium 27；low 9 |
| consensus | tentative 36 |
| 来源册数 | 单册 29；双册 6；六册 1（胡床） |

来源分布（按完整 `evidence_ref.doc_id` 计，非年份正则）：赵农 2009 **24**、夏燕靖 2016 **10**、高丰 2004 **9**、夏燕靖 2009 **3**、李立新 2011 **2**、田自秉 2010 **1**。

B.14 与 B.13 的覆盖形态相反：B.13 有四册零覆盖，B.14 六册俱全、无一册为零；但单册来源仍达 29 条，六册全覆盖只有胡床一条。家具不是某一册的专属叙述对象，而是六册都不立章、各取一角的对象。

`source_count` 按**来源册数**记：B.14.1 = 6、B.14.2 = 4，不是 KU 数。

role 分配理由：铜禁与俎以 `boundary_case` 入内（礼器由功能类比取得家具身份，「雏形」与家具之间的界线来源未划）；隐囊与承尘以 `historical_context` 入内（起居配套物而非家具本体，各只有一至两句证据）。三处同步登记。

---

## 四、边界处置

本批在边界之外留下四组，均已在 Theme 的「边界」与「未解决问题」中写明落点：

1. **木作工艺层与风格层 14 条**：`procedures/sunmao-jiegou`、`procedures/cuanbian`、`terms/banshi-jiegou`、`terms/hongmu`、`terms/qimu-jiaju`、`terms/muhua`、`works/muhua-qiju`、`terms/ming-style-furniture`、`terms/qing-style-furniture`、`terms/qingdai-jiaju-sanda-mingzuo`、`publications/yanji-tu`、`publications/mingshi-jiaju-yanjiu`、`publications/lubanjing`、`publications/xianqing-ouji`。榫卯结构本身虽是家具技术，其条目内容以干栏式建筑为据，本批不挂，留待该层统一处置。
2. **近代家具线 3 条**：`terms/renzao-cailiao-jiaju`、`terms/gonggong-qiju`、`persons/zhang-shuiquan`，已越出前近代范围，需独立批次。
3. **归他处**：建筑与营造 → B.3；图像本体只作条目内证据、不建 KU；夹缬屏风 → B.2／C；漆工技法与漆器实物 → B.11；`works/yunwen-tongjin` → B.9.2；轿子不入。
4. **未挂**：建筑类与墓葬类 place 条目（江陵楚墓群、信阳楚墓、平山中山王墓、荣成松郭家村遗址）与 `publications/qinggongbu-zaobanchchu-dangan`。

在工艺层物化之前，B.14 只能回答「家具长什么样」，不能回答「家具怎样做、何时成为风格」。明式家具为五册共识高峰、清式家具三册评价一致偏低而落点不同（权势压过实用／技巧压过艺术／繁琐雕琢），须待该层物化后判读。

---

## 五、执行与验证

| 步骤 | 命令 | 结果 |
|---|---|---|
| 挂载 | `h50_mount.py` | `mounted 36 bad []` |
| 复验 | `h50_verify.py` | `kUs 36 bad []`，role／type／confidence／topic／source 分布与 Theme、Topic 文件所写完全一致 |
| 结构压力测试 | `scripts/hierarchy_stress_test.py` | v1.41、themes 29、topics 92、membership 798、complete 788、incomplete 1782、`cross_dimension_topics: []`、`apply_permitted: false` |
| 关系索引 | `scripts/build_relation_index.py` | 7584（explicit 5998 不变、inferred／member_of 1586） |
| 关系一致性 | `scripts/audit_relation_consistency.py` | broken 0、invalid type 0、missing inverse 0、weak evidence 0、over-connected 10、isolated 1110 |
| 健康快照 | `scripts/write_current_health.py` | structural 130/130、ksq 58/65、content_findings 0、isolated 1110 |
| 计划生成 | `h50_plan.py` | `rows 43` |
| 计划复核 | 逐行 `after_sha256` 与磁盘比对 | `rows 43 bad []` |

apply-plan 行形状：43 = 1 Theme 新建 + 2 Topic 新建 + 36 `hierarchy_mount` + 4 `structure_index_update`。

索引更新：`hierarchy/index.md` 升 v1.41；`themes/README.md` 29 个 Theme 并补 B.14 段；`topics/README.md` 92 个 Topic 并补 B.14 段；`dimension-candidates.md` 更新为五十批 788 个挂载、B 维度未挂载 1067。

---

## 六、指标变化

| 指标 | v1.40 | v1.41 | 变化 |
|---|---|---|---|
| Theme | 28 | 29 | +1 |
| Topic | 92 | 92 → **92** | +2（90 → 92） |
| Topic membership | 762 | 798 | +36 |
| 完成五级字段挂载 | 752 | 788 | +36 |
| 未完成挂载 | 1818 | 1782 | −36 |
| B 维度未挂载 | 1103 | 1067 | −36 |
| relation 总数 | 7512 | 7584 | +72 |
| 其中 inferred／member_of | 1514 | 1586 | +72 |
| 隔离单元 | 1131 | **1110** | **−21** |
| 结构健康 | 130/130 | 130/130 | — |
| 知识结构质量 | 57/65 | 58/65 | +1 |

推导口径：

- relation +72 = 36 条主挂载 ×（topic `member_of` + theme `member_of`），explicit 5998 不变，与 `build_relation_index.py` 实测一致。
- 隔离单元 1131 → 1110 减 21 而非 36，取自 `audit_relation_consistency.py` 前后两次实测（36 条中有 15 条原已有显式关系）。该差值**不按条数推算**。
- ksq 57/65 → 58/65（`hierarchy_assignment` 2/10 → 3/10），是已挂载 KU 由 752 增至 788 带来的机械项变化，**不代表结构验收通过**；缺口仍在 `hierarchy_assignment`（3/10）。
- 无新增跨维度主挂载：36 条 `primary_dimension` 全部为 B；两个 Topic 的 `secondary_themes` 为裸维度码 D／C，按 `scripts/hierarchy_stress_test.py:828` 的 `"." in code` 规则不计入维度集合，`cross_dimension_topics` 仍为空。

---

## 七、语义边界：并列不裁

本批不替来源做它没做的裁决，以下五处并列保留：

1. **四处胡床不一致**：传入方向、改称「绳床」的时点、绳床与胡床是否同物、社会评价，六册四处互不相同，赵农一册内部亦不自一致。
2. **坐姿线与器物线分层**：二十条中只有胡床、椅子、高型家具承担坐姿叙述，椅凳墩榻各条从不提结构；全 Theme 唯一的结构判断「梁柱式的框架结构代替了以前的箱形壶门结构」只出现在 `terms/gaoxing-jiaju` 一条总论，无法由器物条反证，「箱形壶门结构」的形制、年代上限与被替代时点亦无。
3. **罗汉床与清式榻**：来源自己宣告「榻面加大加宽，几乎与大床相似，罗汉床与榻混淆一体」。本批按来源分两条挂载，二者能否分立未裁。
4. **礼器「雏形」界线**：若按功能类比，青铜礼器整体皆可入家具史；若按性质，家具史失去起源条。以 `boundary_case` 挂载，界线仍空。
5. **名实错位**：太师椅只有交椅—圈椅—太师椅的造型关系，名称来历、出现年代与使用阶层全无；玫瑰椅、龙墩同属名先于器、器只见于一句的条目，不据家具史通识补写。

数据层在 B.14 范围内基本为零：唯一尺度是汉榻推测（长 75－100、宽 60－100、高 12－28 厘米，来源自述为按人榻比例推测而非实测），不能外推到魏晋榻；其余 35 条无尺寸、无构件清单、无用材比例，B.14.2 十六条无一处尺寸。图像证据（图 5-40、图 6-36、马王堆两件漆屏风、《清明上河图》、《西厢记》插图、唐高元圭墓壁画、敦煌壁画、望都 1 号东汉墓壁画、妇好墓跽坐玉人）全部未做视觉核验，本批不据图补写形制。

---

## 八、生成态与门禁

按 h49 教训，`manifest.json` 与 `summary.md` 先落盘，再跑全量闭包，避免第 3 步 build runtime index 之后写 manifest 导致第 14 步 `audit rule drift` 报 `runtime_index_snapshot_stale`。

- `run_sync_closure.py --refresh-generated --full`：18 步全量闭包。
- `run_sync_closure.py --refresh-generated --check-generated`：17 步，第 17 步实为 `git diff --exit-code HEAD`；因本批未提交，该步以 `exit=1` 报生成态与 HEAD 不一致，**属预期**。

闭包重建的 8 个生成态／导航文件：`relation-index.yml`、`current-health.json`、`governance-backlog.md`、`06-runtime/automation/index.md`、`generated-projections-manifest.json`、`05-outputs/index/index.md`、`knowledge-graph-data.js`、`knowledge-graph-data.json`。`changed_files` = 43 + 8 = **51**；archive 快照不计入。

保护路径零改动：`02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`。分支 `main`、单一 worktree、HEAD 仍为 `c249c6fe`。**本包不 commit、不 push。**

---

## 九、未决事项与下一跳

### 下一跳（h51）

1. **B.14 木作工艺层与风格层 Topic**：14 条候选（榫卯、攒边、板式结构、红木、漆木家具、木画、木画棋局、明式家具、清式家具、清代家具三大名作、《燕几图》《明式家具研究》《鲁班经》《闲情偶寄》）。
2. **近代家具线 3 条**另行登记（人造材料家具、公共器具、章水泉竹家具）。

### 债

- 家具的制度与阶层面未物化：龙墩的「权力、地位和身份的象征」、鹿角椅的「武功文治的政治象征」、玫瑰椅在江南园林中的双人联座、杌凳为「妇女常备坐具」、长凳为「贵族饮宴合坐」——五条线索分属不同朝代与不同册，D 维度前近代线仍只有 D.6 官府手工业。
- 宋元明清断代依据普遍薄弱：高束腰凳与罗涡椅同据《西厢记》明弘治十一年重刻本一种插图，腰圆凳与长方凳各据一条图注，抽屉桌据山西文水北峪口元墓壁画《备餐图》，折叠桌据《清明上河图》虹桥段，均无实物、无墓例、无款识。
- 承具六条只给本义、用途与样式；储具为类目条，五类并列而无一件实物。
- 图注待核 12 条；图 7-29 两指问题；未核图版 5-32、8-57、8-58、10-48。
- 重复候选 reconcile 9 组未处理。
- 其他结构缺口：简单机械线（杠杆、滑轮）、水利工程线（都江堰、灵渠、郑国渠、西门渠）、前近代服饰与甲胄等级 Theme；B.9 主题文件「货币归后续 Topic」文字需回改指向 B.13。
- A 维度遗留：A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》未挂载。
- 存量债务：未挂载 1782、隔离 1110、单源 1919、low confidence 496、tentative 2570。
- 小债务：`works/caihui-niaoshou-yuwen-qi-ge.md` 的「相关知识元」把 `simajinlong-mu-qi-pingfeng` 说成「马王堆漆屏风」；h48 的 Theme 与 Topic 文献支撑把赵农书名写作《中国艺术史》（本批与 h49 均按 KU `sources.citation` 与 doc_id 作《中国艺术设计史》）。
