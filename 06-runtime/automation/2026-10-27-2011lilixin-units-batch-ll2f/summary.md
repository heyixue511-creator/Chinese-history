# 2011 册 units 批次 LL2f（佛教的渗透）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2011lilixin-units-batch-ll2f/`
- 来源：李立新《中国设计艺术史论》（2011），doc_id `2011-lilixin-zhongguo-sheji-yishu-shilun`
- 候选范围：L944-L1029 内的 unit 候选，共 10 条待裁
- 裁定结果：新建 5 条、更新 2 条、rejected 3 条、no_delta 0 条
- 状态：applied（10 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：L944-L1029。第二章第二节“佛教的渗透及其设计史意义”全节，含 L946 佛教向艺术领域渗透与傅抱石称引、L953-L960 造像建寺与江南佛教器物、L964-L966 汉化佛教法器与庄严具、L971-L983 曼荼罗与法门寺地宫、L985-L990 供具与银熏炉、L992-L1005 钟鼓磬木鱼、L1007-L1009 佛教与设计观念、L1014-L1028 佛教造物艺术研究的三项内容。
- 截断点：L1030 为第三节“风格论——学术史的追溯”标题，整节归 LL2g；本批未读入该节正文。
- 图注：图2-13 至图2-24 共 12 条图注读到文字，未视觉核验图像。图2-16 图题跨 L974-L975 两行，图2-20 图题分置 L996-L998，图2-18 图题在 L981、正文续于 L985。
- 候选跨度并集：2 段共 70 行（L946、L960-L1028）。本批复读 L944-L1029 全节，但候选跨度只记 10 条候选 payload 的 `source_span` 并集，不把节内每个无候选的行计入。
- 无候选或已终态的行：敦煌莫高窟、云冈石窟、龙门石窟、北魏嵩岳寺塔、法门寺塔基地宫、忍冬纹、秘色瓷等已有 applied 或 rejected 候选，本批不重开。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-03-05 | 傅抱石 | 新建 | `persons/fu-bao-shi.md` |
| cand-03-03 | 杨泓 | 新建 | `persons/yang-hong.md` |
| cand-03-04 | 石兴邦 | 新建 | `persons/shi-xing-bang.md` |
| cand-03-65 | 曼荼罗 | 新建 | `terms/man-tuo-luo.md` |
| cand-03-66 | 五供 | 新建 | `terms/wu-gong.md` |
| cand-03-39 | 唐咸通九年木刻版画《金刚般若波罗蜜经》卷首图 | 更新 | `publications/jingangjing-868.md` |
| cand-03-40 | 鎏金卧龟莲花纹朵带五足银熏炉 | 更新 | `works/wensiyuan-yin-xunlu.md` |
| cand-03-38 | 捧真身菩萨 | rejected | `places/famen-si-digong.md` |
| cand-03-41 | 阮咸（日本正仓院藏） | rejected | `institutions/shosoin.md` |
| cand-03-42 | 葵口圈足秘色瓷碗 | rejected | `terms/mise-porcelain.md` |

cand-03-55《金刚般若波罗蜜经》跨度为 L985-L1141，越过本节进入后文；本批只读至 L1029，未作裁定，保留 `needs_evidence`，留待覆盖 L1141 后的批次处理。

## 4. 新建 5 条

- persons 3：`fu-bao-shi`（傅抱石）、`yang-hong`（杨泓）、`shi-xing-bang`（石兴邦），均 medium。
- terms 2：`man-tuo-luo`（曼荼罗）、`wu-gong`（五供），均 medium。
- 三个人物条只承载李立新册的称引与研究结论，生卒、身份、机构与出处一律记为未载；不据来源外知识补写生平。
- `yang-hong` 与既有 `persons/yang-xun.md`（明代杨埙）分立，避免同名混条。

## 5. 更新 2 条

- `publications/jingangjing-868.md`：补李立新 L981 图题与 L985 卷首图内容两条、两册分工一条；描述补一句，tags 补版画、卷首图、五供；来源增至 2 册，版本升为 2。
- `works/wensiyuan-yin-xunlu.md`：补尺寸异文、汉化判断、金刚结、八吉祥与两册分工五条；描述补一句，tags 补汉化、金刚结、八吉祥；来源增至 2 册，版本升为 2。
- 两条旧册的实测、工艺、铭文、藏地与扉页说法图均保持原样，不据李立新册改写。

## 6. 判重 3 条

| 候选 | 实体 | 已覆盖条目 | 判据 |
|---|---|---|---|
| cand-03-38 | 捧真身菩萨 | `places/famen-si-digong.md` | 该条已收侧面观图2-17、莲花底座即典型曼荼罗坛，并置于地宫陈设叙述；候选无尺寸、材质、出土位置与年代 |
| cand-03-41 | 阮咸（日本正仓院藏） | `institutions/shosoin.md` | 该条已收图2-23 阮咸与 L1020-L1023 东传判断；`terms/ruan-xian.md` 记乐器本体；候选只到图题一级 |
| cand-03-42 | 葵口圈足秘色瓷碗 | `terms/mise-porcelain.md` | 该条已收 L1025、L1028 两行，含十三件口径、方法论意义与图2-24 图版条；候选只补图题 |

均保留 `target_ref`，不另建 works 条。

## 7. 语义判断与内部张力

- **人物条的边界**：傅抱石只有一句转引，杨泓有两处研究结论，石兴邦有一段完整判断；三条都按“称引锚点”建条，不把地方或事件条中的器物叙述复制进人物条，也不补来源外的生卒与任职。石兴邦判断同时见于 `places/famen-si-digong.md`，两条互链而分工不同：地宫条记陈设与器物，人物条记判断归属。
- **曼荼罗与法门寺地宫的分工**：`terms/man-tuo-luo.md` 承担定义、南亚来源、现图曼荼罗、图2-16 与宋代以后流变；`places/famen-si-digong.md` 承担地宫实物、后室陈设与形制对应。曼荼罗是跨遗址的概念，不能只寄存在地宫条内。
- **五供与《金刚经》的分工**：`terms/wu-gong.md` 记三具足／五具足的计数、称法与唐元两处图例；`publications/jingangjing-868.md` 记同一卷的版画定名与佛前供器。供具组合条与印本条互链，不把卷首图拆成独立作品条。
- **金刚经卷首图的归并**：候选 payload 的 proposed_slug 为 `xian-tong-jingang-jing-juan-shou`，但卷首图是咸通九年《金刚经》印本的一部分，既有 `publications/jingangjing-868.md` 已收赵农所记同一卷；本批按同本异称更新印本条，不另建 works 条。
- **银熏炉的归并**：候选 payload 的 proposed_slug 为 `yin-xun-lu`，与既有 `works/yin-xunlu.md`（唐宋同名异器合条）、`works/wensiyuan-yin-xunlu.md`（文思院造专条）同指；本批选最精确的专条承载李立新的汉化判断与尺寸异文，不新建条。
- **尺寸异文不径改**：李立新 L985 原文作高 295cm、腹深 70cm，按器物尺度疑脱小数点；夏燕靖 2016 作 29.5 厘米、7 厘米。两说并列，`works/wensiyuan-yin-xunlu.md` 与 `places/famen-si-digong.md` 均标疑而不改写。
- **已有重复条不合并**：`works/yin-xunlu.md` 与 `works/wensiyuan-yin-xunlu.md` 同记法门寺文思院造银熏炉，属旧批次遗留的重复；本批只指定 canonical 目标，不做删除或合并，留待后续去重治理。
- **长跨度候选不提前裁定**：cand-03-55 的摘要含《存素堂丝绣录》所记宋代绫地绣《金刚般若波罗蜜经》五十六页、五千九百九十六字，位于 L1141，超出本批范围；本批不据未见文本裁定。

## 8. 跨批维护

- 本批无 extras；两条更新均为决策内 update，计入 `outputs.knowledge_units.update`。
- `publications/jingangjing-868.md` 与 `works/wensiyuan-yin-xunlu.md` 的版本、来源数与日期同步升为 2／2／2026-10-27。
- 本批未发现既有条目的引文缺陷，未做额外的引号修正。

## 9. 生成态与门禁

- `_zn_checklines_ll2f.py`：5 条新建加 2 条更新的 29 处引文全部在所指单行内命中，problems 0。
- `_zn_struct.py`：7 个文件字段、六节、链接、日期、版本全部通过，problems 0。
- `_zn_audit.py`：7 个文件全库引文审计 findings 0。
- 候选索引：`needs_evidence` 1451 → 1441，`applied` 2791 → 2798，`rejected` 867 → 870，`no_delta` 230 不变；总行数 5339 不变；active 1451 → 1441，terminal 3888 → 3898。
- 工作包：ledger 27 行、apply-plan 7 行、canonical-mapping 10 条；10 条候选的跨度并集 2 段共 70 行，复读范围 L944-L1029。
- 生成态：`build_discovery_index.py`、`build_translation_index.py`、`build_runtime_index.py` 已重建；闭包状态见 `06-runtime/state/current-health.json` 与 `06-runtime/automation/index.md`。
- 完整闭包：`scripts/run_sync_closure.py --refresh-generated --full` 通过 18/18，测试 250 passed、16 subtests passed。
- 生成态发布门禁：`scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 失败，差异为 `06-runtime/state/current-health.json`、`06-runtime/governance/governance-backlog.md` 与生成态投影清单的 `files`／`digest`；工作树未提交，状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。
- `06-runtime/automation/index.md` 已收录本包，列为最近批次首条。

## 10. 未决事项

- 李立新 2011 册 unit 候选在本批后余 73 条 `needs_evidence`，其中含本批未裁的 cand-03-55。
- 第三节“风格论——学术史的追溯”（L1030 起）的 unit 候选归 LL2g：刘勰、司空图、《文心雕龙》、《二十四诗品》、风格（maniera）、八体说、森珀、里格尔、两部风格论著作、艺术意志、庞薰琹、《中国装饰风格研究》、宝相花、欧阳修等。
- 五条长跨度候选仍待覆盖终点后单独裁定：cand-01-01 李立新（L5-L2464）、cand-01-57 张道一（L341-L2446）、cand-01-72 意匠化设计（L368-L1169）、cand-04-06 胡正言（L1246-L1846）、cand-04-29 工商食官（L1394-L1831）。
- 田自秉 2010 册仍有 5 条 unit 候选待裁（cand-03-09 二里头铜爵与 L82/L92/L95/L101 四个单行图注锚点）。
- `works/yin-xunlu.md` 与 `works/wensiyuan-yin-xunlu.md` 的重复条待后续去重治理。
- claim/evidence 流尚未启动：全库 claim 候选 1363 条，须走 collect → evidence JSONL → apply，写回入口 `scripts/verify_apply_evidence.py`。
- 本批无 commit、无 push；索引与生成态改动留在工作树，等待用户明确授权。

## 11. 下一跳

- 下一批 LL2g：李立新 2011 册 L1030 起第三节“风格论——学术史的追溯”，处理该节 unit 候选。
- 之后继续李立新册余下 unit 候选（73 条），再转田自秉册 5 条与 claim/evidence 流。
