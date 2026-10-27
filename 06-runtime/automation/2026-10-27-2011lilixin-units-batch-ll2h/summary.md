# 2011 册 units 批次 LL2h（由“华丽丰腴”到“典雅质朴”）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2011lilixin-units-batch-ll2h/`
- 来源：李立新《中国设计艺术史论》（2011），doc_id `2011-lilixin-zhongguo-sheji-yishu-shilun`
- 候选范围：L1052-L1133 内的 unit 候选，共 2 条待裁
- 裁定结果：新建 1 条、更新 1 条、no_delta 0 条、rejected 0 条
- 状态：applied（2 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：L1052-L1133。第二章第四节“由‘华丽丰腴’到‘典雅质朴’”全节，含 L1054 前辈学者的唐宋风格归纳，L1056-L1099 唐代华丽丰腴与金银器造型演变，L1103-L1119 文人士大夫情趣与“典雅”风格，L1121-L1132 宋代一般造物的“质朴”状况。
- 截断点：L1134 为第五节“院画的扩张与意匠化设计的衰落”标题，整节归 LL2i；本批未读入该节正文。
- 图注：本节有图2-25 至图2-32 共 8 个图号、9 个图像文件，另有 L1113-L1115“图表四 魏晋南北朝至宋造物设计风格演变图示”。图注只读到文字，未视觉核验图像；图2-30 由两幅图与一个总图题组成。
- 候选跨度并集：2 段共 6 行（L1060、L1107-L1111）。本批复读 L1052-L1133 全节，但候选跨度只记 2 条候选 payload 的 `source_span` 并集，不把节内每个无候选的行计入。
- 无 unit 候选的实体：颜真卿（L1078、L1083 图2-29）、苏轼（L1107）、梅尧臣（L1109）、杜甫与韩幹（L1109）、宋仁宗与刘贵妃（L1109）、真宗（L1109）、王安石（L1111）、陆游（L1128）、王禹偁（L1130）、蔡京（L1109 引《蔡京太清侍宴记》）等。这些行只有 claim 候选或无候选，本批不越出 unit 候选另建条目，留作研究债务。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-03-63 | 宝相花 | 更新 | `terms/baoxianghua-wen.md` |
| cand-03-12 | 欧阳修 | 新建 | `persons/ou-yang-xiu.md` |

## 4. 新建 1 条

- `persons/ou-yang-xiu.md`（欧阳修），medium。承载 L1107 士阶层语境与“平淡”说、L1109 端溪绿石枕、L1111“以适用为本”与文辞器用比喻。
- 来源未给其生卒、籍贯、官职、著述与诗文原出处，一律记为未载，不据来源外知识补写。
- 与 `persons/su-shi.md` 分工：苏轼条已收同段 L1109 及赵农、李立新 L847-L878 的“平淡”材料，本条只收欧阳修本人的三处称引。

## 5. 更新 1 条

- `terms/baoxianghua-wen.md`：候选 payload 的 `knowledge_match` 记 `novel`、称 04-knowledge 无 KU，但该条以“宝相花”为别名，已收 2016 册的定义、平面团形与立面层叠形、唐三彩载体及宋代衰退。李立新 L1060 提供的是新增的历时演变与团窠关系，故按 update 并入，不新建 `bao-xiang-hua` 条。
- 补六条：初唐转折（瓣式、蕾形宝相花与卷草走出“瘦窄”）、盛唐流行（骨架式消失、缠枝卷草与宝相花广泛流行）、主体与形式（莲花与牡丹、瓣形／蕾形／侧式）、团窠（正圆形轮廓与卷草环、柿蒂纹统称）、团窠层叠（套叠十多层、环行到组合环行、散点式到缠枝式）、图注（图2-26 唐代宝相花琵琶锦袋，日本正仓院藏）。
- 描述补一段李立新的纹样演变；tags 补团窠、牡丹、正仓院；来源增至 2 册，版本升为 2，日期同步为 2026-10-27。

## 6. 判重与别名复核

| 候选 | 实体 | 既有条目 | 判据 |
|---|---|---|---|
| cand-03-63 | 宝相花 | `terms/baoxianghua-wen.md` | 既有条 aliases 收“宝相花”，来源为夏燕靖 2016；候选筛查只按 slug 与标题检索，未命中别名，故误记 novel |

本条是 LL2g 之后第二例“候选 knowledge_match 记 novel、实际已有别名条”的情况（LL2g 的 cand-03-10 为字形异写，本批为纹样别名）。两例均按 update／no_delta 归并，不重复建条。

## 7. 语义判断与内部张力

- **宝相花的历时与共时分工**：2016 册给共时形式分类（平面团形、立面层叠形、唐三彩载体）与宋代衰退；李立新给初唐至盛唐的历时演变（骨架式→缠枝卷草与宝相花→团窠层叠）与“团窠”的统称关系。两条材料互补，合为一条比拆成“宝相花”与“宝相花纹”两条更利于检索。
- **“团窠”不另建条**：李立新把宝相花、卷草环、柿蒂纹等圆形轮廓纹样统称“团窠”，但既有 `terms/tuanhua-wen.md` 已收团花纹、团窠纹与“团窠即团花”的田自秉说，且本条候选只指向宝相花；本批在宝相花条内记团窠关系并链到团花纹条，不另立团窠条。
- **欧阳修与苏轼的分工**：L1107 同段先引苏轼“当使气象峥嵘，五色绚烂，渐老渐熟，乃造平淡”，再引欧阳修“作诗无古今，唯有平淡难”。苏轼条已收 L1109 与“平淡”材料，欧阳修条只收欧阳修三处，避免把同段两人合并成“宋代文人”泛条。
- **“适用为本”的归属**：L1111 原文作“欧阳修、王安石都主张器物‘以适用为本’”，是二人并提的共同主张。本条把该句收在欧阳修条，并在相关知识元注明 `persons/wang-anshi.md` 尚未收此句；王安石条现为 D 维度变法人物、材料仅赵农一句，若补入 A 维度设计思想需另做维度调整，留作研究债务。
- **朱熹条已终态**：cand-03-13 朱熹（L1111-L1132）在早前批次已 applied，本批不重开；欧阳修条只链到朱熹条，不复制“简易”“致用”材料。
- **图注只作锚点**：图2-26 用于宝相花条的图版锚点；图2-25、2-27 至 2-32 与图表四无对应 unit 候选，本批不建单图条，留待后续按需处理。
- **唐宋转折的叙述层次**：本节把唐代“华丽丰腴”与宋代“典雅质朴”作为风格转折，原因分三层：造物自身规律、皇家贵族嗜好与社会欣赏风气、文人士大夫情趣与理学“简易”“致用”。本批只落宝相花与欧阳修两条，风格转折本身尚无 structure node 或 theme 承载，属层级债务。

## 8. 跨批维护

- 本批无 extras；1 条 update 计入 `outputs.knowledge_units.update`，1 条 create 计入 `create`。
- `terms/baoxianghua-wen.md` 由 version 1、source_count 1 升为 version 2、source_count 2；created 保留 2026-10-26，updated/last_verified 改 2026-10-27，review_due 改 2027-04-27。
- `persons/ou-yang-xiu.md` 为 version 1、source_count 1、created/updated/last_verified 2026-10-27、review_due 2027-04-27。
- 本批未发现既有条目的引文缺陷，未做额外的引号修正。

## 9. 生成态与门禁

- `_zn_checklines_ll2h.py`：1 条新建加 1 条更新的 18 处引文全部在所指单行或全库归一文本内命中，problems 0。
- `_zn_struct.py`：2 个文件字段、六节、链接、日期、版本全部通过，problems 0。
- `_zn_audit.py`：2 个文件全库引文审计 findings 0。
- 内容质量审计：`content_quality_findings=20`，全部为本批之前的存量项：16 项 frontmatter 空字段（`liezi-tangwen`、`qinlv-gonglv`、`songshi-yufuzhi`、`zhongguo-dalishi` 各 4 项）、1 项跨类型同名 `armillary sphere`、3 项占位内容（`zhao-nong`、`zhongguo-yishu-shejishi-zhaonong-2009`、`he-zun`）。本批新建与更新文件无内容质量发现。
- 候选索引：`needs_evidence` 1428 → 1426，`applied` 2809 → 2811，`rejected` 871 不变，`no_delta` 231 不变；总行数 5339 不变；active 1428 → 1426，terminal 3911 → 3913。
- 工作包：ledger 6 行、apply-plan 2 行、canonical-mapping 2 条；2 条候选的跨度并集 2 段共 6 行，复读范围 L1052-L1133。
- 生成态：`build_discovery_index.py`（5339 行）、`build_translation_index.py`（2128 条）、`build_runtime_index.py` 已重建；`06-runtime/automation/index.md` 已收录本包，列为最近批次首条。
- 完整闭包：`scripts/run_sync_closure.py --refresh-generated --full` 通过 18/18，测试 250 passed、16 subtests passed；`structural_health=96`。
- 生成态发布门禁：`scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 失败，差异仍为未提交工作树引起的生成态投影与 `current-health.json`、`governance-backlog.md` 哈希漂移；状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。

## 10. 未决事项

- 李立新 2011 册 unit 候选在本批后余 58 条 `needs_evidence`。
- 第五节“院画的扩张与意匠化设计的衰落”（L1134 起）的 unit 候选归 LL2i：沈子蕃缂丝《花鸟图》（cand-03-44，L1143-L1155）、朱克柔缂丝《牡丹》（cand-03-43，L1150-L1151）、院体画（cand-03-71，L1155-L1157）、粉本（cand-03-72，L1161）、早期工业化（cand-03-73，L1175-L1226）、李贽（cand-03-17，L1192）、《焚书》（cand-03-56，L1192）等。
- 五条长跨度候选仍待覆盖终点后单独裁定：cand-01-01 李立新（L5-L2464）、cand-01-57 张道一（L341-L2446）、cand-01-72 意匠化设计（L368-L1169）、cand-04-06 胡正言（L1246-L1846）、cand-04-29 工商食官（L1394-L1831）。
- 田自秉 2010 册仍有 5 条 unit 候选待裁（cand-03-09 二里头铜爵与 L82/L92/L95/L101 四个单行图注锚点）。
- 本批识别的研究债务：王安石条未收 L1111“适用为本”句；苏轼条未收 L1107“气象峥嵘……乃造平淡”句；颜真卿、梅尧臣、陆游、王禹偁、蔡京等只有称引或图注，无独立 KU；图2-25、2-27 至 2-32 与图表四无单图条；唐宋风格转折无 theme/topic 承载。
- `works/yin-xunlu.md` 与 `works/wensiyuan-yin-xunlu.md` 的重复条待后续去重治理。
- claim/evidence 流尚未启动：全库 claim 候选 1363 条，须走 collect → evidence JSONL → apply，写回入口 `scripts/verify_apply_evidence.py`。
- 本批无 commit、无 push；索引与生成态改动留在工作树，等待用户明确授权。

## 11. 下一跳

- 下一批 LL2i：李立新 2011 册 L1134 起，第五节“院画的扩张与意匠化设计的衰落”，处理该节 unit 候选。
- 之后继续李立新册余下 unit 候选（58 条），再转田自秉册 5 条与 claim/evidence 流。
