# 2011 册 units 批次 LL2g（风格论——学术史的追溯）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2011lilixin-units-batch-ll2g/`
- 来源：李立新《中国设计艺术史论》（2011），doc_id `2011-lilixin-zhongguo-sheji-yishu-shilun`
- 候选范围：L1030-L1051 内的 unit 候选，共 13 条待裁
- 裁定结果：新建 11 条、更新 0 条、no_delta 1 条、rejected 1 条
- 状态：applied（13 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：L1030-L1051。第二章第三节“风格论——学术史的追溯”全节，含 L1032 风格语源与刘勰八体说、司空图二十四诗品，L1034 西方风格概念与 maniera 入艺，L1036-L1038 近代风格理论诸家，L1040 两个基本含义与中西类型论比较，L1044 风格即人及其限制，L1046 森珀与里格尔，L1048 艺术意志评价与庞薰琹，L1050 《中国装饰风格研究》。
- 截断点：L1052 为第四节“由‘华丽丰腴’到‘典雅质朴’”标题，整节归 LL2h；本批未读入该节正文。
- 图注：本节 L1030-L1051 无图题或插图标记，本批无图注条目，未做视觉核验。
- 候选跨度并集：3 段共 13 行（L1032-L1040、L1046、L1048-L1050）。本批复读 L1030-L1051 全节，但候选跨度只记 13 条候选 payload 的 `source_span` 并集，不把节内每个无候选的行计入。
- 无候选或已终态的行：L1034、L1036-L1038、L1044 的西方风格理论诸家与“风格即人”判断已由 cand-03-68 的风格条覆盖，不另立人物条；L1050 的《中国装饰风格研究》只有写作计划，随 cand-03-54 处理。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-03-06 | 刘勰 | 新建 | `persons/liu-xie.md` |
| cand-03-07 | 司空图 | 新建 | `persons/si-kong-tu.md` |
| cand-03-50 | 《文心雕龙》 | 新建 | `publications/wen-xin-diao-long.md` |
| cand-03-51 | 《二十四诗品》 | 新建 | `publications/er-shi-si-shi-pin.md` |
| cand-03-68 | 风格（maniera） | 新建 | `terms/feng-ge-maniera.md` |
| cand-03-69 | 八体说 | 新建 | `terms/ba-ti-shuo.md` |
| cand-03-08 | 森珀 | 新建 | `persons/sen-po.md` |
| cand-03-09 | 里格尔 | 新建 | `persons/li-ge-er.md` |
| cand-03-52 | 《工艺美术与建筑的风格》 | 新建 | `publications/gong-yi-mei-shu-yu-jian-zhu-de-feng-ge.md` |
| cand-03-53 | 《风格问题——装饰艺术史的基础》 | 新建 | `publications/feng-ge-wen-ti.md` |
| cand-03-70 | 艺术意志（Kunstwollen） | 新建 | `terms/yi-shu-yi-zhi.md` |
| cand-03-10 | 庞薰桀/庞薰栗（原文异写） | no_delta | `persons/pang-xunqin.md` |
| cand-03-54 | 《中国装饰风格研究》 | rejected | `persons/pang-xunqin.md` |

## 4. 新建 11 条

- persons 4：`liu-xie`（刘勰）、`si-kong-tu`（司空图）、`sen-po`（森珀）、`li-ge-er`（里格尔），均 medium。
- publications 4：`wen-xin-diao-long`（《文心雕龙》）、`er-shi-si-shi-pin`（《二十四诗品》）、`gong-yi-mei-shu-yu-jian-zhu-de-feng-ge`（《工艺美术与建筑的风格》）、`feng-ge-wen-ti`（《风格问题——装饰艺术史的基础》），均 medium。
- terms 3：`feng-ge-maniera`（风格）、`ba-ti-shuo`（八体说）、`yi-shu-yi-zhi`（艺术意志），均 medium。
- 森珀、里格尔两条只写来源所记的姓氏、机构、著作与理论；来源未给本名、生卒、国籍细节与著作年代，一律记为未载，不据来源外知识补写。
- 刘勰、司空图两条只承载 L1032、L1040 的风格论称引与类型论评价，不补文学史生平。

## 5. no_delta 1 条

- `cand-03-10` 指向 `persons/pang-xunqin.md`。既有 KU 已把李立新 L1048、L1050 列入来源，正文“装饰艺术研究”条逐句抄录“两千多年来……”与《中国装饰风格研究》未完成、‘简和变’等同一材料，字形统计亦记李立新 L1048 作“桀”、L1050 作“栗”。候选无新增事实，不修改文件，保留 `target_ref`。

## 6. rejected 1 条

| 候选 | 实体 | 已覆盖条目 | 判据 |
|---|---|---|---|
| cand-03-54 | 《中国装饰风格研究》 | `persons/pang-xunqin.md` | 来源只记 20 世纪 60 年代准备撰写而未完成，无成书、目录、出版社或内容结构；未完成著作不构成可独立著录的出版物 |

该书名与未完成事实已完整见于 `persons/pang-xunqin.md`，不另建 publication 条。

## 7. 语义判断与内部张力

- **人物—文献—概念三分**：L1032 一句同时出现刘勰、《文心雕龙》与八体说，L1046 一句同时出现森珀、里格尔、两部著作与艺术意志。若按句合并，会把作者、书名与概念压成一条，无法分别检索与引用；本批按 4 人物、4 文献、3 概念分建 11 条，并以 `相关知识元` 互链。
- **八体说与二十四诗品的处理差异**：八体说有独立 term 候选（cand-03-69），故建 `terms/ba-ti-shuo.md`；《二十四诗品》只有 publication 候选（cand-03-51），来源未提出“二十四品”作为独立术语，本批不越出候选另造 term，二十四品名目暂存于司空图条与《二十四诗品》条。
- **风格条与艺术意志条的分工**：`terms/feng-ge-maniera.md` 收 maniera 的汉语对应、西方词义与入艺、近代普适理论、两个基本含义、风格即人及其限制；`terms/yi-shu-yi-zhi.md` 只收 Kunstwollen 的提出、内涵与李立新评价。两条都引 L1046-L1048，但一为风格概念史，一为里格尔的专门理论，不合并。
- **森珀与里格尔的对照**：森珀以连续的、线性的艺术史与地域、气候、时代、习俗、材料、工具等因素解释风格定型；里格尔以艺术意志强调心智的精神性活动，批评森珀的机械性被动性反应理论，并以创造性选择补足技术材料的多样性要求。两条人物条互链，并各自链到其著作与艺术意志条。
- **庞薰琹条不重复写入**：cand-03-10 的 proposed_slug 为 `pang-xun-jie`，是来源“庞薰桀”异写；规范条为 `persons/pang-xunqin.md`。既有条已完整覆盖 L1048、L1050，故标 no_delta 而不新建 `pang-xun-jie`，避免同一人物因字形分裂成两条。
- **未完成著作不立目**：《中国装饰风格研究》只有一句写作计划，且同一事实已由庞薰琹条承载；若未来出现成书、目录或手稿，再按 publication 重开，不在本批据书名建空条。
- **本节无图注**：L1030-L1051 未见图题、插图编号或图版说明，本批没有图注锚点，也未做视觉核验。

## 8. 跨批维护

- 本批无 extras；无 update，`outputs.knowledge_units.update` 为 0。
- 11 条新建均为 version 1、source_count 1、created/updated/last_verified 2026-10-27、review_due 2027-04-27。
- `persons/pang-xunqin.md` 因 no_delta 未改动，其 updated/last_verified 仍为 2026-10-25，source_count 6、version 1。
- 本批未发现既有条目的引文缺陷，未做额外的引号修正。

## 9. 生成态与门禁

- `_zn_checklines_ll2g.py`：11 条新建的 54 处引文全部在所指单行或全库归一文本内命中，problems 0。
- `_zn_struct.py`：11 个文件字段、六节、链接、日期、版本全部通过，problems 0。
- `_zn_audit.py`：11 个文件全库引文审计 findings 0。首轮曾报 5 处 NESTED，集中在 `li-ge-er.md`、`feng-ge-wen-ti.md`、`yi-shu-yi-zhi.md` 的“艺术意志”句：句内再含引号而外层仍用“”；已把外层改为「」，重生成三文件后复检为 0。
- 内容质量审计：首轮闭包报 `content_quality_findings=24`，其中 4 项落在 `publications/feng-ge-wen-ti.md`，因英文名 `Problems of Style: Foundations for a History of Ornament` 含冒号加空格，YAML 解析后 `title`、`name_en`、`sub_type`、`tags` 被判为空。已把英文名改为 `Problems of Style — Foundations for a History of Ornament`（破折号，无冒号），重生成该文件，并同步刷新 apply-plan 中该条的 `after_sha256`、`bytes`、`lines`。复跑后 `content_quality_findings=20`，全部为本批之前的存量项：16 项 frontmatter 空字段（`liezi-tangwen`、`qinlv-gonglv`、`songshi-yufuzhi`、`zhongguo-dalishi` 各 4 项）、1 项跨类型同名 `armillary sphere`、3 项占位内容（`zhao-nong`、`zhongguo-yishu-shejishi-zhaonong-2009`、`he-zun`）。本批 11 条新建文件无内容质量发现。
- 候选索引：`needs_evidence` 1441 → 1428，`applied` 2798 → 2809，`rejected` 870 → 871，`no_delta` 230 → 231；总行数 5339 不变；active 1441 → 1428，terminal 3888 → 3911。
- 工作包：ledger 38 行、apply-plan 11 行、canonical-mapping 13 条；13 条候选的跨度并集 3 段共 13 行，复读范围 L1030-L1051。
- 生成态：`build_discovery_index.py`（5339 行）、`build_translation_index.py`（2127 条）、`build_runtime_index.py`（140 个批次目录、683 个文件）已重建；`06-runtime/automation/index.md` 已收录本包，列为最近批次首条。
- 完整闭包：`scripts/run_sync_closure.py --refresh-generated --full` 通过 18/18，测试 250 passed、16 subtests passed；`structural_health=96`。
- 生成态发布门禁：`scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 失败，差异含 `05-outputs/index/index.md` 哈希、automation 投影 `files` 437→683 与 digest、quality 投影 `files` 1315→2557 与 digest、`06-runtime/state/current-health.json` 与 `06-runtime/governance/governance-backlog.md` 哈希；工作树未提交，状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。

## 10. 未决事项

- 李立新 2011 册 unit 候选在本批后余 60 条 `needs_evidence`。
- 第四节“由‘华丽丰腴’到‘典雅质朴’”（L1052-L1133）的 unit 候选归 LL2h：宝相花（cand-03-63，L1060）、欧阳修（cand-03-12，L1107-L1111）等。
- 第五节“院画的扩张与意匠化设计的衰落”（L1134 起）的 unit 候选归 LL2i：沈子蕃缂丝《花鸟图》（cand-03-44，L1143-L1155）、朱克柔缂丝《牡丹》（cand-03-43，L1150-L1151）、院体画（cand-03-71，L1155-L1157）、粉本（cand-03-72，L1161）、早期工业化（cand-03-73，L1175-L1226）、李贽（cand-03-17，L1192）、《焚书》（cand-03-56，L1192）等。
- 五条长跨度候选仍待覆盖终点后单独裁定：cand-01-01 李立新（L5-L2464）、cand-01-57 张道一（L341-L2446）、cand-01-72 意匠化设计（L368-L1169）、cand-04-06 胡正言（L1246-L1846）、cand-04-29 工商食官（L1394-L1831）。
- 田自秉 2010 册仍有 5 条 unit 候选待裁（cand-03-09 二里头铜爵与 L82/L92/L95/L101 四个单行图注锚点）。
- `works/yin-xunlu.md` 与 `works/wensiyuan-yin-xunlu.md` 的重复条待后续去重治理。
- claim/evidence 流尚未启动：全库 claim 候选 1363 条，须走 collect → evidence JSONL → apply，写回入口 `scripts/verify_apply_evidence.py`。
- 本批无 commit、无 push；索引与生成态改动留在工作树，等待用户明确授权。

## 11. 下一跳

- 下一批 LL2h：李立新 2011 册 L1052-L1133，第四节“由‘华丽丰腴’到‘典雅质朴’”，处理该节 unit 候选。
- 之后继续 LL2i（L1134 起）与李立新册余下 unit 候选（60 条），再转田自秉册 5 条与 claim/evidence 流。
