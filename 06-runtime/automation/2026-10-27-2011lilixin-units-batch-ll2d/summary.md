# 2011 册 units 批次 LL2d（从规范化的完善看造物体系的形成）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2011lilixin-units-batch-ll2d/`
- 来源：李立新《中国设计艺术史论》（2011），doc_id `2011-lilixin-zhongguo-sheji-yishu-shilun`
- 候选范围：L741-L847 内的 unit 候选，共 13 条待裁
- 裁定结果：新建 7 条、更新 3 条、rejected 3 条、no_delta 0 条
- 状态：applied（13 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：L741-L847。第六节“从规范化的完善看造物体系的形成”标题（L741）至节末苏轼语（L847），含 L743-L749 规范化的定义与分期、L751-L759 浮具到木板船的三阶段、L761 三翼与平山木船、L766 秦律工律、L768 汉代造船、L773-L779 伍家岭船模与标准化四点、L781-L783 普遍规范与孟子、L788-L847 技术成熟、功能设计、官营制度、意匠化四目。
- 截断点：L849 为第二章“开放融合与风格转变”标题，整章归 LL2e；本批未读入该章正文。
- 图注：图1-30 至图1-38 共 9 条图注读到文字，未视觉核验图像。图1-33 图题嵌在 L804 末尾，L806 续接被隔断的正文；图1-34、图1-35、图1-36 三条图题分别落在 L809、L812、L817。
- 候选跨度并集：12 段共 28 行（L743、L745、L753、L757、L761、L766、L768、L773-L775、L783-L786、L804-L809、L811-L814、L816-L819）。本批复读 L741-L847 全节，但不把节内每个无候选的行都记入候选跨度；候选跨度只记 13 条候选 payload 的 `source_span` 并集。
- 无候选的行：L790 起四目的分述（如 L798 斗拱、青瓷、造纸，L827 官营制度，L835 云气纹，L840 画像石与《鲁灵光殿赋》）未生成 unit 候选，本批未据以建条，留待 claim/evidence 或后续批次处理。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-02-146 | 规范化 | 新建 | `terms/guifanhua.md` |
| cand-02-77 | 腰舟 | 新建 | `terms/yaozhou.md` |
| cand-02-81 | 吴越春秋 | 新建 | `publications/wuyue-chunqiu.md` |
| cand-02-82 | 三翼 | 更新 | `terms/chunqiu-zhanguo-zhanchuan-zhonglei.md` |
| cand-02-153 | 史记·夏本纪 | 更新 | `publications/shiji.md` |
| cand-02-79 | 系辞下 | 更新 | `publications/zhouyi.md` |
| cand-02-84 | 秦律·工律 | 新建 | `publications/qinlv-gonglv.md` |
| cand-02-154 | 酉阳杂俎 | 新建 | `publications/youyang-zazu.md` |
| cand-02-97 | 雁鱼铜灯 | 新建 | `works/yanyu-tongdeng.md` |
| cand-02-145 | 青铜连枝灯 | 新建 | `works/qingtong-lianzhideng.md` |
| cand-02-86 | 伍家岭汉代木船模型 | rejected | `places/changsha-wujialing.md` |
| cand-02-87 | 伏羲女娲手执规矩图 | rejected | `places/wuliangci.md` |
| cand-02-98 | 马王堆漆案及杯盘 | rejected | `places/mawangdui-hanmu.md` |

## 4. 新建 7 条

- terms 2：`guifanhua`（规范化）、`yaozhou`（腰舟）。
- publications 3：`wuyue-chunqiu`（吴越春秋）、`qinlv-gonglv`（秦律·工律）、`youyang-zazu`（酉阳杂俎）。
- works 2：`yanyu-tongdeng`（雁鱼铜灯）、`qingtong-lianzhideng`（青铜连枝灯）。
- 置信度：medium 4 条（`guifanhua`、`yaozhou`、`wuyue-chunqiu`、`qinlv-gonglv`）、low 3 条（`youyang-zazu`、`yanyu-tongdeng`、`qingtong-lianzhideng`）。
- 文献条限制：`wuyue-chunqiu`、`qinlv-gonglv`、`youyang-zazu` 均无作者、成书年代、版本与卷次，条目内逐项写明缺口；`youyang-zazu` 只有一条豫章大船引文，按 low 定级。
- 图版限制：2 条 works 均据图题与正文合述建立，条目内写明“未视觉核验”；`yanyu-tongdeng` 另注明正文的灯罩、导烟说明是灯具类的合述，不是逐器描述。

## 5. 更新 3 条

- `publications/shiji.md`：补李立新 L745《夏本纪》准绳、规矩与考古印证两条要点、两册分工一条，描述补一句；来源增至 3 册，补 `secondary_dimensions: B`，版本升为 2。
- `publications/zhouyi.md`：补李立新 L757《系辞下》舟楫句与规范化判断、四册分工，描述补一句；来源增至 4 册，版本升为 4。
- `terms/chunqiu-zhanguo-zhanchuan-zhonglei.md`：补李立新 L761 三翼与翼船、大翼载员、中翼与小翼尺度、双层船体、平山木船五条要点与三册分工，描述补一句；来源增至 3 册，版本升为 3，参考文献补赵农与李立新两册。
- 三条更新均不据新册改写旧册判断，旧册文字与原引文保持不变。

## 6. 判重 3 条

| 候选 | 实体 | 已覆盖条目 | 判据 |
|---|---|---|---|
| cand-02-86 | 伍家岭汉代木船模型 | `places/changsha-wujialing.md` | 该条已收船舷钉孔、三间舱房、十六根木桨（长52.8厘米、桨叶25.6厘米）、长约100厘米的尾桨 |
| cand-02-87 | 伏羲女娲手执规矩图 | `places/wuliangci.md` | 该条已收图1-32 图题、规被人形化、孟子语境与“物”“道”双重规范的论述用途 |
| cand-02-98 | 马王堆漆案及杯盘 | `places/mawangdui-hanmu.md` | 该条已收耳杯一件、卮二件、盘五件、竹箸与七只耳杯盒的组合，并标“耳环”当为“耳杯”之疑 |

三条均保留 `target_ref`，不另建条目。

## 7. 语义判断与内部张力

- **规范化与审曲面势的分工**：`terms/shenqu-mianshi.md` 是《考工记》造物原则的概念条，`terms/guifanhua.md` 是规范、标准制定与贯彻的过程概念；两条互链，不合并。`terms/baigong.md` 的主语是百工的职能与分工，也不与规范化条合并。
- **腰舟、筏子、独木舟、木板船四层**：`terms/yaozhou.md` 只承担最初的复合浮具，`terms/dugout-canoe.md` 承担独木舟，`terms/plank-boat.md` 承担木板船；李立新把浮具到筏子、舟船的进化作为规范化三阶段的第一阶段，本条只记腰舟与筏子，不把四者写成同一器物。
- **三翼一句分入两条**：L761 的同一句既建 `publications/wuyue-chunqiu.md` 承担文献与引文，又更新 `terms/chunqiu-zhanguo-zhanchuan-zhonglei.md` 承担船型与尺度；前者是书目锚点，后者是船型综条，各有检索用途，引用同一句但论证对象不同。
- **《夏本纪》与《系辞下》并入上位文献条**：cand-02-153 的 payload 原拟 slug 为 `shiji-xia-benji`，cand-02-79 原拟 slug 为 `xicixia`；本批按上位文献条归并到 `publications/shiji.md` 与 `publications/zhouyi.md`，不另建篇目子条，避免同一文献被拆成多个碎片条目。两条均在描述中写明篇目。
- **“并舟”异文**：L757 原文作“刳木并舟，剡木为楫”，与通行本用字不同；`publications/zhouyi.md` 照录来源，注明与通行本不同，不据外部版本径改，也未做版本核对。
- **雁鱼铜灯的合述句被图题隔断**：L804 止于“这些青铜灯具的设计充分”，中间隔图1-33 图题，L806 接“发挥了照明的功能”；条目按两截分引，不连读，也不把灯具类的合述当作雁鱼铜灯的逐器描述。
- **连枝灯与十五连盏铜灯的区分**：新建 `works/qingtong-lianzhideng.md` 只承担李立新 L817、L819 所列的汉代连枝灯类型；`works/shiwu-lianzhan-tongdeng.md` 是战国十五连盏铜灯，两条分属不同器物，互链而不合并。
- **伍家岭、武梁祠、马王堆三处判重**：三处图注与正文均已被既有 place 条完整覆盖，单独立条只重复同一段，故 rejected 而不新建 works 子条。
- **豫章大船的史料性质**：L768 的“可载千人”出自《酉阳杂俎》对汉武帝豫章大船的追记，来源未给船体尺寸与考古实物；`publications/youyang-zazu.md` 按 low 定级，照录引文而不把它当作已核实的载员数据。
- **秦律的引述层级**：L766 的“车同轨”“书同文”是李立新对秦代政策的概括，《工律》律文只一句；条目并列政策背景与律文，不把概括当作律文原文。

## 8. 跨批维护

- `terms/chang-deng.md`：`相关知识元` 把“连枝灯尚无独立 KU”一句改为指向 `works/qingtong-lianzhideng.md` 的链接，版本升为 2，日期改为 2026-10-27／2027-04-27。该处为 extras，`candidate_id` 挂 cand-02-145，记入 apply-plan 与 manifest 的 `paths_updated`；不计入 `outputs.knowledge_units.update` 的决策计数。
- `publications/shiji.md`：全库引文审计暴露 `2016 该条记“原文未详”` 一处分析性引号，改为不加引号的“2016 该条未署作者”。
- `publications/zhouyi.md`：全库引文审计暴露两处既有引号问题，按原义修正而不改知识内容：`“孔子晚而喜《易》……韦编三绝”` 恢复为来源自带的省略号形式 `“孔子晚而喜《易》，……读《易》，韦编三绝”`；`“道器在形内”` 两处分析性引号改为不加引号。
- 上述引号修正均为既有文本的审计缺陷，不是本批新增知识；除这三处外未改动旧册文字。

## 9. 生成态与门禁

- `_zn_checklines_ll2d.py`：7 条新建加 3 条更新的 55 处引文全部在所指单行内命中，problems 0。
- `_zn_struct.py`：11 个文件字段、六节、链接、日期、版本全部通过，problems 0。
- `_zn_audit.py`：11 个文件全库引文审计 findings 0。
- 候选索引：`needs_evidence` 1468 → 1455，`applied` 2778 → 2788，`rejected` 863 → 866，`no_delta` 230 不变；总行数 5339 不变；active 1468 → 1455，terminal 3871 → 3884。
- 工作包：ledger 36 行、apply-plan 11 行、canonical-mapping 13 条；13 条候选的跨度并集 12 段共 28 行，复读范围 L741-L847。
- 生成态：`build_discovery_index.py`、`build_translation_index.py`、`build_runtime_index.py` 已重建；闭包状态见 `06-runtime/state/current-health.json` 与 `06-runtime/automation/index.md`。
- 完整闭包：`scripts/run_sync_closure.py --refresh-generated --full` 通过 18/18，测试 250 passed、16 subtests passed。
- 生成态发布门禁：工作树未提交，`--check-generated` 在 `[17/17] check generated snapshots` 失败，状态记 `blocked_pending_commit`；本批未获 commit 授权，不处理。

## 10. 未决事项

- 李立新 2011 册 unit 候选在本批后余 87 条 `needs_evidence`。
- 本节 L798 斗拱、青瓷、造纸，L827 官营制度，L835 云气纹，L840 画像石与《文选·鲁灵光殿赋》等段落无 unit 候选，未建条；留待 claim/evidence 或后续批次处理。
- 五条长跨度候选仍待覆盖终点后单独裁定：cand-01-01 李立新（L5-L2464）、cand-01-57 张道一（L341-L2446）、cand-01-72 意匠化设计（L368-L1169）、cand-04-06 胡正言（L1246-L1846）、cand-04-29 工商食官（L1394-L1831）。
- 田自秉 2010 册仍有 5 条 unit 候选待裁（cand-03-09 二里头铜爵与 L82/L92/L95/L101 四个单行图注锚点）。
- claim/evidence 流尚未启动：全库 claim 候选 1363 条，须走 collect → evidence JSONL → apply，写回入口 `scripts/verify_apply_evidence.py`。
- 本批无 commit、无 push；索引与生成态改动留在工作树，等待用户明确授权。

## 11. 下一跳

- 下一批 LL2e：李立新 2011 册 L849 起第二章“开放融合与风格转变”，从 L849 标题与 L859“一、传统、外来、时尚”起处理该章 unit 候选。
- 之后继续李立新册余下 unit 候选（87 条），再转田自秉册 5 条与 claim/evidence 流。
