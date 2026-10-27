# 2011 册 units 批次 LL2e（传统、外来、时尚）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2011lilixin-units-batch-ll2e/`
- 来源：李立新《中国设计艺术史论》（2011），doc_id `2011-lilixin-zhongguo-sheji-yishu-shilun`
- 候选范围：L849-L943 内的 unit 候选，共 4 条待裁
- 裁定结果：新建 2 条、更新 1 条、rejected 1 条、no_delta 0 条
- 状态：applied（4 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：L849-L943。第二章“开放融合与风格转变”标题（L849）与第一节“传统、外来、时尚”全节（L859-L942），含 L851-L857 全章总论、L861-L865 南北分裂与纺织业、L867-L897 牛车、鹿车、指南车与记里鼓车、L902 青瓷与缥瓷、L907-L928 佛教纹样与莲花尊、L930-L940 胡服胡床与发式时尚、L942 节末。
- 截断点：L944 为第二节“佛教的渗透及其设计史意义”标题，整节归 LL2f；本批未读入该节正文。
- 图注：图2-1 至图2-12 共 12 条图注读到文字，未视觉核验图像。图2-1 图题跨 L870-L871 两行，图2-3 图题在 L881、正文续于 L883，图2-8 图题在 L914、正文续于 L916。
- 候选跨度并集：2 段共 69 行（L863-L930、L935）。本批复读 L849-L943 全节，但候选跨度只记 4 条候选 payload 的 `source_span` 并集，不把节内每个无候选的行计入。
- 无候选或已终态的行：牛车（犊车）、鹿车、指南车、记里鼓车、缥瓷、越窑、锦署、忍冬纹等已有 applied 或 rejected 候选，本批不重开。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-03-01 | 孝文帝 | 新建 | `persons/xiaowendi.md` |
| cand-03-35 | 青瓷仰覆莲花尊 | 更新 | `works/lianhua-zun.md` |
| cand-03-36 | 腊缬棉布 | rejected | `places/niya-site.md` |
| cand-03-64 | 飞天髻 | 新建 | `terms/feitian-ji.md` |

## 4. 新建 2 条

- persons 1：`xiaowendi`（孝文帝），medium。
- terms 1：`feitian-ji`（飞天髻），medium。
- 人物条只收李立新册所记两事（奖劝农桑与朝服设计），与两条既有事件条互链，不复制事件条的完整叙述。
- 发式条只据 L935 一行，图2-11 未视觉核验，条目内写明尺寸与年代上限未载。

## 5. 更新 1 条

- `works/lianhua-zun.md`：补李立新 L923-L926 图2-10 图题与“(河北景县封氏墓群出土)”两条要点、两册分工一条，描述补一句；来源增至 6 册，版本升为 3。
- 旧册的造型、层数、40／66.5／85 厘米三种尺度与南京林山两件均保持原样，不据李立新册改写。

## 6. 判重 1 条

| 候选 | 实体 | 已覆盖条目 | 判据 |
|---|---|---|---|
| cand-03-36 | 腊缬棉布 | `places/niya-site.md` | 该条已收 1959 年尼雅出土、蓝色印花、半身裸体人物像、希腊丰收女神或伊什塔尔解释、狮尾角杯葡萄等文化因素与图2-8 图题 |

保留 `target_ref`，不另建 works 条。

## 7. 语义判断与内部张力

- **孝文帝人物条与两条事件条的分工**：`events/xiaowendi-jiangquan-nongsang.md` 记奖劝农桑与官营丝织作坊，`events/xiaomingdi-fushi-gaige.md` 记孝文帝朝服设计与孝明帝改制；新人物条只把这两条线上的统治者行为收拢为人物锚点，叙述从简，并把两条事件条作为下一跳，不把事件条全文复制进人物条。
- **青瓷仰覆莲花尊的归并**：候选 payload 的 proposed_slug 为 `qing-ci-yang-fu-lian-hua-zun`，与既有 `works/lianhua-zun.md` 的别名“仰覆莲花瓷尊”同指一器；本批按别名归并到上位器形条，不另建子条。李立新册只给图题与出土地，未给尺寸、件数与收藏，故只作增量更新。
- **腊缬棉布的归属**：该布是尼雅遗址出土的单件织物，但全部信息（发现年份、工艺、图像、解释、图题）已由 `places/niya-site.md` 承担；再建 works 条会把同一段文本拆成两条，故 rejected。
- **飞天髻与假髻的区分**：`terms/jia-ji.md` 记假髻这一饰件类型，`terms/feitian-ji.md` 记一种具体的结发样式；两者互链而不合并。灵蛇髻、撷子髻、流苏髻、双螺髻、双环髻只在飞天髻条中作同时流行的名目，未逐一建条。
- **已终态候选不重开**：缥瓷、越窑、锦署、鹿车、指南车、记里鼓车、忍冬纹等在本节出现，但候选状态已为 applied 或 rejected；本批不因复读同一节而重开，避免候选索引回退。

## 8. 跨批维护

- `events/xiaowendi-jiangquan-nongsang.md`：`相关知识元` 补入 `persons/xiaowendi.md` 链接，版本升为 2，日期改为 2026-10-27／2027-04-27。
- `events/xiaomingdi-fushi-gaige.md`：`相关知识元` 补入 `persons/xiaowendi.md` 链接，版本升为 2，日期改为 2026-10-27／2027-04-27。
- 上述两处均为 extras，`candidate_id` 挂 cand-03-01，记入 apply-plan 与 manifest 的 `paths_updated`；不计入 `outputs.knowledge_units.update` 的决策计数。
- 本批未发现既有条目的引文缺陷，未做额外的引号修正。

## 9. 生成态与门禁

- `_zn_checklines_ll2e.py`：2 条新建加 1 条更新的 12 处引文全部在所指单行内命中，problems 0。
- `_zn_struct.py`：5 个文件字段、六节、链接、日期、版本全部通过，problems 0。
- `_zn_audit.py`：5 个文件全库引文审计 findings 0。
- 候选索引：`needs_evidence` 1455 → 1451，`applied` 2788 → 2791，`rejected` 866 → 867，`no_delta` 230 不变；总行数 5339 不变；active 1455 → 1451，terminal 3884 → 3888。
- 工作包：ledger 11 行、apply-plan 5 行、canonical-mapping 4 条；4 条候选的跨度并集 2 段共 69 行，复读范围 L849-L943。
- 生成态：`build_discovery_index.py`、`build_translation_index.py`、`build_runtime_index.py` 已重建；闭包状态见 `06-runtime/state/current-health.json` 与 `06-runtime/automation/index.md`。
- 完整闭包：`scripts/run_sync_closure.py --refresh-generated --full` 通过 18/18，测试 250 passed、16 subtests passed。
- 生成态发布门禁：`scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 失败，差异为 `06-runtime/state/current-health.json`、`06-runtime/governance/governance-backlog.md` 与生成态投影清单的 `files`／`digest`；工作树未提交，状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。
- `06-runtime/automation/index.md` 已收录本包，列为最近批次首条。

## 10. 未决事项

- 李立新 2011 册 unit 候选在本批后余 83 条 `needs_evidence`。
- 第二节“佛教的渗透及其设计史意义”（L944-L1029）的 11 条 unit 候选归 LL2f：傅抱石、杨泓、石兴邦、曼荼罗、捧真身菩萨、金刚经卷首图、五供、银熏炉、金刚经、阮咸、秘色瓷碗。
- 五条长跨度候选仍待覆盖终点后单独裁定：cand-01-01 李立新（L5-L2464）、cand-01-57 张道一（L341-L2446）、cand-01-72 意匠化设计（L368-L1169）、cand-04-06 胡正言（L1246-L1846）、cand-04-29 工商食官（L1394-L1831）。
- 田自秉 2010 册仍有 5 条 unit 候选待裁（cand-03-09 二里头铜爵与 L82/L92/L95/L101 四个单行图注锚点）。
- claim/evidence 流尚未启动：全库 claim 候选 1363 条，须走 collect → evidence JSONL → apply，写回入口 `scripts/verify_apply_evidence.py`。
- 本批无 commit、无 push；索引与生成态改动留在工作树，等待用户明确授权。

## 11. 下一跳

- 下一批 LL2f：李立新 2011 册 L944 起第二节“佛教的渗透及其设计史意义”，处理该节 11 条 unit 候选。
- 之后继续李立新册余下 unit 候选（83 条），再转田自秉册 5 条与 claim/evidence 流。
