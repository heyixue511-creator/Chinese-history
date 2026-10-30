# h30 批次摘要：前近代官府手工业（D.6）

- 批次：`2026-10-28-hierarchy-pilot-h30`
- 日期：2026-10-28
- 层级版本：v1.20 → v1.21
- 结论：在 D 维度新建 D.6「前近代官府手工业：职官、匠役与设计控制」与 2 个 Topic（D.6.1 中央工官、D.6.2 官窑与窑政），挂载 14 个 KU；22 个 authored 文件，22/22 哈希匹配。未 commit、未 push。

## 一、目标与范围

h29 收尾时把下一批的候选登记为三项：B.5 的「制陶生产组织」（4 条候选）、「史前功能陶器」（6 条候选）与自 h23 起挂起的 D 维度前近代官手工业材料。本批选第三项，理由不是它材料最多，而是它被两处明文指认：

- `04-knowledge/structure/topics/b6-yaoxi-mingyao-yaoye-zuzhi.md`（B.6.3，v1.14）写明「御器厂、浮梁瓷局、瓷窑官、景德镇四条的 `primary_dimension` 为 D……本批不为它们制造跨维度挂载……制度本体留待 D 维度前近代官手工业 Theme」；
- `04-knowledge/structure/themes/d5-chuantong-gongyi-jindai-zuzhi-zhanzhan-zhengce.md` 的边界明文排除「古代工官、匠籍、御器厂、官府作坊」。

两处共同指向一个尚不存在的落点，h30 即是还这笔债。**本批不是新开维度**：A–E 五个试运行维度对这批材料完全可容纳，缺的是 Theme 层。

六项判断：

1. **归 D 不归 B。** B.6.3 已把制度侧证据让出，B.5.4 也把琉璃渠的机构事实留在 `procedures/liuli-shaozhao.md`，两处都指向 D。
2. **新建 Theme 不并入 D.5。** D.5 的边界明文排除这批对象，并入会使 D.5 的近代组织边界失效。
3. **Theme 得建而不是并成一个 Topic。** 清点 D 维度未挂载的前近代官手工业机构，命中三十余条：少府监（7 源）、将作监（6 源）、工部、中尚署、尚方、文思院、元代画局、镔铁局（3 源）、绫锦院（6 源）、织染署（5 源）、内务府造办处（5 源）、江宁织造局（4 源）、西夏官营手工业机构群、蜀郡成都广汉郡工官等。规模足以支撑多批次 Theme。
4. **本批只取两块：中央工官 7 条、官窑窑政 7 条。** 两者在六册中分处不同段落、不同章节，唯一的连接是元代画局「供官方窑场生产制作」一句。
5. **边界处置五条**（详见第四节）。
6. **一条跨维度挂载。** 秦汉官营陶窑的 `primary_dimension` 为 B，按制度侧取用，构成 B→D。

## 二、结构物化

### 新建 D.6 Theme

`04-knowledge/structure/themes/d6-guanfu-shougongye-zhiguan-jiangyi-sheji-kongzhi.md`

- `theme_code: D.6`，`primary_dimension: D`，`secondary_dimensions: [B]`，`status: pilot`
- 核心问题两条线索：其一，把官府介入拆成三种**可以分离**的手段——设官分职（谁有权管）、征调匠役（谁出力、如何训练与考课）、指定样式（谁决定做成什么样）；三者不总同时在场，西周只有工种名而无官署、元代画局只有设计权而无制作、明代御器厂把主要产能让给民窑而只保留产品分配权。其二，「官」字四义分离——作坊（王室作坊、官营陶窑）、职官（瓷窑官、尚方令）、机构（浮梁瓷局、御器厂）、产品等级（「官」字款、钦限与部限）。
- 关键发现：三层的证据密度依次递减（职官名号与品秩最完整，工匠与训练次之，样式控制最薄），**制度史的能量集中在对「谁管」的记录上，对「做成什么样」则几乎不记**——这也是本 Theme 只能把「设计控制」当解释框架的原因。
- 未解决问题 15 条。

### 新建 D.6.1「中央工官：设官分职与工匠训练」

`04-knowledge/structure/topics/d6-zhongyang-gongguan-jigou-gongjiang-guanli.md`

- `parent_theme: D.6`，`primary_dimension: D`，`research_question` 179 字
- 支撑材料 7 个 KU，全部 `institution`、全部 `key_institution`
- 三层组织：机构分工（产品／工程／政令三分）—工匠组织（固定工匠、短番匠、征调与雇佣、奴婢与刑徒，9 个月至 4 年分档训练、季度测试年终考试）—设计分离（元代画局）
- 核心判断：**六册能说清「谁管」，说不清「管什么、管到哪一步」**——工匠组织与职官体系之间的断层是最可靠的负面发现

### 新建 D.6.2「官窑与窑政：从王室作坊到御器厂」

`04-knowledge/structure/topics/d6-guanyao-yaozheng-wangshi-zuofang-yuqichang.md`

- `parent_theme: D.6`，`primary_dimension: D`，`research_question` 184 字
- 支撑材料 7 个 KU：`key_institution` 5、`boundary_case` 1（周代制陶职官）、`geographical_context` 1（景德镇）
- 三层组织：作坊层—职官层—产品分配层
- 核心判断：**「产品分配」而非「机构设置」是这条线索的关键证据**——机构的名单可以排得很长，能说明官府究竟拿走了什么的只有钦限与部限这一段（田自秉记「钦限瓷器则往往由民窑承担」，御器厂「主要烧造部限瓷器」）。它与高丰记清代官搭民烧合起来，说明官方需求与民间产能不是替代关系，而是分层承接。

### 既有结构更新

| 文件 | 变更 |
|---|---|
| `04-knowledge/structure/hierarchy/index.md` | v1.20→v1.21：21 Theme、58 Topic、441 membership、437 完整挂载、2133 未挂载；补 `D.6` 与「D.6 下 2 个」；追加 v1.21 版本边界长段 |
| `04-knowledge/structure/hierarchy/archive/v1.20.md` | 新建归档：36006 字节，`sha256:c6ca7c9a7ade43f9ae438bdc0d8182fa268c9e8fd58a09720d6603d66bdd72bb`，与 v1.20 版 index.md 逐字节一致 |
| `04-knowledge/structure/themes/README.md` | 20→21 个 Theme；首段清单补 `D.6`；新增 D.6 段 |
| `04-knowledge/structure/topics/README.md` | 56→58 个 Topic；首段补「D.6 下 2 个」；新增两 Topic 分工说明 |
| `04-knowledge/structure/dimension-candidates.md` | 二十九批 423→三十批 437；新增 D.6 v1.21 条目；缺口行补 v1.21；未挂载 2147→2133 |

## 三、14 个 KU 的挂载

| KU | 类型 | role | primary_dimension | 版本 |
|---|---|---|---|---|
| [少府监](../../../04-knowledge/units/institutions/shaofujian.md) | institution | `key_institution` | D | v2→v3 |
| [将作监](../../../04-knowledge/units/institutions/jiangzuojian.md) | institution | `key_institution` | D | v3→v4 |
| [工部](../../../04-knowledge/units/institutions/gongbu.md) | institution | `key_institution` | D | v1→v2 |
| [中尚署](../../../04-knowledge/units/institutions/zhongshang-shu.md) | institution | `key_institution` | D | v1→v2 |
| [尚方](../../../04-knowledge/units/institutions/shangfang.md) | institution | `key_institution` | D | v2→v3 |
| [文思院](../../../04-knowledge/units/institutions/wensiyuan.md) | institution | `key_institution` | D | v1→v2 |
| [元代画局](../../../04-knowledge/units/institutions/yuan-dai-huaju.md) | institution | `key_institution` | D | v1→v2 |
| [商代王室制陶作坊](../../../04-knowledge/units/institutions/shang-royal-pottery-workshop.md) | institution | `key_institution` | D | v1→v2 |
| [周代制陶职官](../../../04-knowledge/units/institutions/zhou-pottery-officials.md) | institution | `boundary_case` | D | v1→v2 |
| [秦汉官营陶窑](../../../04-knowledge/units/institutions/qin-han-guan-ying-tao-yao.md) | institution | `key_institution` | B | v1→v2 |
| [瓷窑官](../../../04-knowledge/units/institutions/ciyaoguan.md) | institution | `key_institution` | D | v1→v2 |
| [浮梁瓷局](../../../04-knowledge/units/institutions/fuliang-ciju.md) | institution | `key_institution` | D | v2→v3 |
| [御器厂](../../../04-knowledge/units/institutions/yuqichang.md) | institution | `key_institution` | D | v2→v3 |
| [景德镇](../../../04-knowledge/units/places/jingdezhen.md) | place | `geographical_context` | D | v1→v2 |

来源覆盖：少府监 7、将作监 6、景德镇 6、御器厂 5、浮梁瓷局 4、尚方／文思院各 2，工部、中尚署、元代画局、商代作坊、周代职官、秦汉陶窑、瓷窑官各 1。本轮未写入任何新 KU，只做层级字段与版本号增量。

## 四、边界处置

| 对象 | 处置 | 依据 |
|---|---|---|
| 琉璃渠窑场「黑窑、御窑」 | 留在 `procedures/liuli-shaozhao.md`（已挂 B.5.4），不重挂 | 同一 KU 不做部分挂载；若需以御窑为机构专题，须另立 KU |
| `places/jingdezhen-kiln.md` | 不重挂（已挂 B.6.3） | B.6.3 取窑侧证据，本 Theme 取制度侧证据 |
| `places/chifeng-gangwayaotun-liaoyao.md` | 不重挂（已挂 B.6.3） | 它是瓷窑官唯一的窑场旁证，只在瓷窑官 KU 内引用结论 |
| `places/zhenghan-gucheng-taofang-yizhi.md` | 排除 | 来源只记窑址群、作坊建筑群、陶制排水管道与陶洗池，从未说官营；据「制陶作坊」一词推断会超出证据 |
| 元代画局 | 归 D.6.1 不归 D.6.2 | 将作院属设计机构，不属窑政；D.6.2 边界明文排除 |
| 秦汉官营陶窑 | B→D 跨维度挂载 | 沿用 D.2.2（B 主维度 KU 入 D Topic）与 D.4.3（C 主维度 KU 入 D Topic）先例 |
| 唐代工匠数四说 | 并列保留，不裁 | 统计口径来源均未说明；不据任一数字推算产能、工资或人均产出 |

## 五、执行与验证

- 写回方式：内联 heredoc + `pathlib` 精确替换。`scripts/apply_*.py` 被 `scripts/agent_guard.py` 硬阻断，本批不使用。
- 14 个 KU 的字段块顺序为 `primary_dimension` → `primary_theme` → `secondary_themes` → `role_in_theme` → `topic_memberships`；`hierarchy_scope_note` 留在 frontmatter 末位，取值为 `topic_memberships[].scope_note` 的同一字符串。
- body 的「在层级体系中的位置」按 h24 惯例六行（`primary_domain` / `primary_dimension` / `primary_theme` / `topic_memberships` / `role_in_theme` / `scope_note`），不保留 `secondary_dimensions`，其后不留空行。
- 结构压力测试（`scripts/hierarchy_stress_test.py`）：`v1.21`、`themes 21`、`topics 58`、`topic_memberships 441`、`complete_assignments 437`、`incomplete_assignments 2133`、`themes_without_topics 0`、`cross_dimension_topics []`、`apply_permitted false`。
- 关系索引（`scripts/build_relation_index.py` v2.1）：6876 条，explicit 5998、inferred 878；`member_of` 878 = Theme 437 + Topic 441。
- `apply-plan.jsonl` 22 行：`structure_node_create` 3（Theme + 2 Topic）、`hierarchy_mount` 14、`structure_index_update` 5；`after_sha256` 按当前磁盘字节逐一计算，22/22 匹配。

## 六、指标变化

| 指标 | v1.20 | v1.21 | 变化 |
|---|---:|---:|---:|
| Theme | 20 | 21 | +1 |
| Topic | 56 | 58 | +2 |
| Topic membership | 427 | 441 | +14 |
| 完整挂载 KU | 423 | 437 | +14 |
| 未挂载 KU | 2147 | 2133 | −14 |
| 关系总数 | 6848 | 6876 | +28（14 Theme member_of + 14 Topic member_of） |
| `member_of` 关系 | 850 | 878 | +28 |
| 隔离单元 | 1304 | 1297 | −7 |
| 结构健康 | 130 | 130 | 0 |
| 知识结构质量 | 56/65 | 56/65 | 0 |

隔离单元只减少 7：14 个 KU 中 7 个原本已通过其他关系入图（此数为 `current-health.json` 实测值；本批初稿按投影未预估该值，闭包后以实测为准）。

## 七、语义边界

1. **三种可分离手段是本库的整理框架，不是来源结论。** 六册没有哪一处把「设官分职—征调匠役—指定样式」并置；把它们拆开使用的正当性来自材料本身的不齐——三者的证据密度相差一个量级。
2. **「官」字四义不合并。** 作坊、职官、机构、产品等级四类对象被六册按朝代排成一条线，本身即是一种书写顺序；本库要求每条 KU 的 `scope_note` 写明所占之义。
3. **「从王室作坊到御器厂」的推移标为解释框架。** 六个节点分属四类对象，来源从未并列提出；若后续来源给出跨节点的直接记载，此判断须撤销。
4. **「设计从制造中分离」只在元代画局一处有明文，且是单一来源。** 高丰在同一段把画局比作「现代的国家艺术设计院」，来源未区分记载与类比。
5. **产品分配重于机构设置。** 机构名单可以排得很长，但六册唯一说清「官府究竟拿走了什么」的只有钦限与部限那一段。
6. **D.6 是多批次 Theme。** 官营染织、地方工官与内廷造办三块留有候选池；本批不预先物化空 Topic，也不把三十余条候选一次性写回。
7. **本批不表示 D 维度前近代骨架已建立。** 只表示 D 维度有了第一条前近代 Theme，D 维度未挂载 KU 仍有 292 个。

## 八、生成态与门禁

- 完整闭包 `scripts/run_sync_closure.py --refresh-generated --full`：18/18 通过（含 pytest）。
- 生成态核查 `--refresh-generated --check-generated`：17 步，在未提交时 `[17/17] FAILED (exit=1)` 为预期结果——它等价于 `git diff --exit-code HEAD -- <GENERATED_PATHS>`，用于阻断未提交的索引或状态漂移。
- 保护路径（`02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`）零改动。
- 本批未 commit、未 push。

## 九、未决事项与下一跳

1. **D.6 后续三块**：官营染织机构（绫锦院、织染署、东西织室、三服官、江宁织造局、四川锦院、绣院、纳失失局、建康路织染局、木棉提举司、后赵邺城织锦署、南朝染署、宋代染织管理机构群、周代染人）；地方工官与特种作坊（蜀郡成都广汉郡工官、秦工室工官、汉代漆器作坊工官、镔铁局、兴文署、西夏官营手工业机构群、西夏文思院）；内廷造办（内务府造办处、果园厂、石渠阁、武英殿修书处、宋代画院）。
2. **B.5 制陶生产组织的剩余处置**：商代王室制陶作坊、周代制陶职官、秦汉官营陶窑、郑韩故城制陶作坊遗址四条候选，前三条本批已按制度侧挂入 D.6.2，B.5 侧不再另设 Topic；郑韩故城维持不挂载。
3. **B.5 史前功能陶器**：陶鬶、陶甑、陶埙、鱼鳍形足陶鼎、水鸟形陶壶、山东莒县陶尊（6 条候选，与 B.5.1／B.5.2 的边界待判）。
4. **玻璃材料 Theme**：琉璃第一义、铅钡与钠钡玻璃、战国琉璃璧、长沙楚墓群、李立新玻璃器沉浮。
5. **重复候选 reconcile**（4 组）：`terms/youlihong-ci` vs `terms/youlihong`；`terms/bai-tao` vs `terms/shangdai-baitao`；鲁山窑瓷拍鼓 vs 花釉腰鼓；`works/zhulin-qixian-huaxiang-zhuan` vs `works/zhulin-qixian-rongqiqi-zhuanhua`。
6. **图注单条待核队列**（12 条）：五彩人物洗、珐琅彩竹菊鹌鹑瓶、铜官窑釉罐、追韩信图梅瓶、蒙恬将军玉壶春瓶、山东莒县陶尊、陶井、三彩罐、紫砂瓜形壶、紫砂「东陵瓜」、双鹿瓦当、始皇陵夔凤纹大瓦当。
7. **存量债务**（v1.21）：未挂载 2133、单源 1919、tentative 2570、低置信 496、隔离 1297。
8. **A 维度遗留**：A.1.2 命名逐条对照；1917 年许衍灼《中国工艺沿革史略》未挂载。
