# 第二批写回：跨五书 15 组 canonical 知识元

- 工作包：`06-runtime/automation/2026-10-25-five-book-canonical-units/`
- 状态：`applied`
- 日期：2026-10-25
- 范围：Books 1–6（前六本）；Book 7 及以后不启动

## 一、批次范围

从 `duplicate-groups.jsonl` 中筛出 `doc_count = 5` 的组，共 15 组，覆盖 75 条候选。相邻的 `xdup-0012`（荀子）为 `doc_count = 4`，不属于跨五书组，本批未处理，留待后续。

各组 5 条候选的处置方式一致：1 条升为 canonical 并写回 KU，4 条转为 `rejected` 并注明并入目标。

## 二、canonical 映射

| 组 | 实体 | 类型 | canonical 候选 | 写回文件 |
|---|---|---|---|---|
| xdup-0008 | 中央工艺美术学院 | institution | `2016-…-upgrade:cand-09-67` | `04-knowledge/units/institutions/central-academy-arts-design.md` |
| xdup-0009 | 少府监 | institution | `2010-tianzibing-…:cand-08-27` | `04-knowledge/units/institutions/shaofujian.md` |
| xdup-0010 | 墨子 | person | `2016-…-upgrade:cand-03-51` | `04-knowledge/units/persons/mozi.md` |
| xdup-0011 | 宋应星 | person | `2016-…-upgrade:cand-08-07` | `04-knowledge/units/persons/song-yingxing.md` |
| xdup-0013 | 磁州窑 | place | `2004-gaofeng-…:cand-04-15` | `04-knowledge/units/places/cizhou-kiln.md` |
| xdup-0014 | 邢窑 | place | `2010-tianzibing-…:cand-08-37` | `04-knowledge/units/places/xing-kiln.md` |
| xdup-0015 | 失蜡法 | procedure | `2010-tianzibing-…:cand-05-33` | `04-knowledge/units/procedures/lost-wax-casting.md` |
| xdup-0016 | 园冶 | publication | `2016-…-upgrade:cand-08-46` | `04-knowledge/units/publications/yuan-ye.md` |
| xdup-0017 | 髹饰录 | publication | `2004-gaofeng-…:cand-06-09` | `04-knowledge/units/publications/xiu-shi-lu.md` |
| xdup-0018 | 唐三彩 | term | `2004-gaofeng-…:cand-04-03` | `04-knowledge/units/terms/tang-sancai.md` |
| xdup-0019 | 彩陶 | term | `2010-tianzibing-…:cand-01-28` | `04-knowledge/units/terms/painted-pottery.md` |
| xdup-0020 | 明式家具 | term | `2004-gaofeng-…:cand-06-07` | `04-knowledge/units/terms/ming-style-furniture.md` |
| xdup-0021 | 缂丝 | term | `2010-tianzibing-…:cand-10-17` | `04-knowledge/units/terms/kesi.md` |
| xdup-0022 | 陵阳公样 | term | `2004-gaofeng-…:cand-04-02` | `04-knowledge/units/terms/lingyang-gong-pattern.md` |
| xdup-0023 | 长信宫灯 | work | `2004-gaofeng-…:cand-03-03` | `04-knowledge/units/works/changxin-palace-lamp.md` |

## 三、方法

1. **语义复读**：逐组读五册原文窗口，对每个关键事实做定点回查，确认候选 payload 与正文一致。
2. **差异记录而非裁决**：来源之间的冲突（年代、数量、字形、窑址、技术上限）原文并列保留，写入 `## 核心内容` 并标注出处，不做偏好性裁定。
3. **状态链**：canonical 走 `needs_evidence → ready_for_review → approved → applied`；同组其余 4 条走 `needs_evidence → rejected`，reason 中写明 canonical 目标。
4. **追加式台账**：`candidate-decision-ledger.jsonl` 共 105 行（15×3 + 60），覆盖 75 个唯一 `candidate_id`，只以 transition 叠加，不改写历史 R1 台账。
5. **类型化写回**：`apply-plan.jsonl` 为 15 条 `create`，无 `update`、无 `delete`；逐条重算 `sha256 / bytes / lines` 并与磁盘核对（`all_match = True`）。

## 四、主要来源差异

| 实体 | 差异 |
|---|---|
| 中央工艺美术学院 | 副院长用字「庞薰琍」（2009）／「庞薰杲」（2016）；附设机构「中央工艺美术研究所」／「中央工艺美术科学研究所」 |
| 少府监 | 玄宗时工匠「八百多人」（田自秉）／少府监、将作监「各万余人」（夏燕靖 2009、2016） |
| 墨子 | 生卒四说：约前 468—前 396（高丰）／前 468—前 376（赵农，亦见 2016 一处）／前 478—前 392（2016 主条） |
| 宋应星 | 《天工开物》成书或刊行 1636（李立新）／1637（高丰、赵农、夏燕靖 2016） |
| 磁州窑 | 元代「衰落」（高丰）／「元代名窑、元初设官窑课税」（夏燕靖 2016） |
| 邢窑 | 「主要遗址至今尚未发现」（夏燕靖 2009、2016）／1980 年临城普查发现唐窑址（田自秉） |
| 失蜡法 | 出现上限「春秋早中期」（高丰）／「春秋晚期至战国」（夏燕靖 2009、2016） |
| 园冶 | 成稿 1631、刊行 1634（夏燕靖 2016）／泛称明末（赵农） |
| 髹饰录 | 作者「黄成」（高丰）／「黄大成」（田自秉）；成书「隆庆年间」／「天启年间」 |
| 唐三彩 | 器类「四大类」（高丰）／「三类」（田自秉）；烧成「一次约 900℃」／「素烧 1000—1100℃ 加釉烧 900℃」 |
| 彩陶 | 夏燕靖 2009「也称仰韶文化」的表述在 2016 版被自注为倒置；五型划分仅田自秉给出 |
| 明式家具 | 用材清单、六大类器类、概念史（杨耀，1930 年代）分别仅部分来源记录 |
| 缂丝 | 田自秉书该节标题原文误作「绯丝」，正文作「缂丝」；本批按正文统一 |
| 陵阳公样 | 人名「窦师伦」（高丰）／「窦师纶」（田自秉、李立新）；母题「对雉」／「对鸡」；2016 原文误作「对风」 |

## 五、验证结果

| 门禁 | 结果 |
|---|---|
| `apply-plan` 哈希核对 | 15/15 与磁盘一致 |
| `build_discovery_index.py` | total 5339，applied 22，needs_evidence 5221，rejected 96，无 issue |
| `run_sync_closure.py --refresh-generated --full --check-generated` | `sync closure passed`（含 250 项测试） |
| `audit_content_quality.py` | 0 项发现（22 个知识元） |
| `audit_repo.py` | structural health 122/130；rule drift 0；relation 索引 0 条关系 |
| `pre_commit_check.py` | 通过 |

## 六、边界与未解决项

- 未 commit、未 push；仅工作树变更。
- 未建分支、未建 worktree；`main` 为唯一主线。
- `02-sources/`（实际目录 `03基础书籍-md文档/`）只读，未改写。
- 未使用外部验证平台，证据仅限六册 Markdown 文本；未做图版或实物核验。
- `primary_theme` 与 `topic_memberships` 留空：Theme / Topic 节点尚未 materialize，已计入 research debt（22 个 KU 均缺层级指派）。
- 未写入正式 `relations`：22 个 KU 均处于 isolated 状态，跨 KU 共现只在正文以非断言方式记述。
- `xdup-0012`（荀子，`doc_count = 4`）本批未处理。
- 类型覆盖 7/8：`event` 类型尚无 KU。
