# 六书跨源候选归并与首批知识写回（2026-10-25）

## 目标

前六本来源已完成摄入，产出 5339 条统一候选，但 `04-knowledge/` 仍为空。本工作包处理跨六书全命中的 7 组同实体候选，作为知识写回的 pilot：每组选出一条 canonical 候选写入知识单元，其余同组候选追加裁决为 rejected，不留下含糊的活跃重复项。

范围限定为前六本；Book 7 及以后不启动。

## 结果

- 处理候选组：7
- 处理候选：42（canonical 7 + 重复 35）
- 新建知识单元：7
- 更新知识单元：0
- 新增 relation：0
- 新增 claim：0
- 修改来源文件：0

### canonical 与写回目标

| 实体 | 类型 | canonical candidate | 写回目标 |
|---|---|---|---|
| 孔子 | person | `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-03-49` | `04-knowledge/units/persons/confucius.md` |
| 黄道婆 | person | `2004-gaofeng-zhongguo-shejishi:cand-05-10` | `04-knowledge/units/persons/huang-daopo.md` |
| 越窑 | place | `2010-tianzibing-zhongguo-gongyi-meishushi:cand-07-48` | `04-knowledge/units/places/yue-kiln.md` |
| 考工记 | publication | `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-01-04` | `04-knowledge/units/publications/kaogongji.md` |
| 天工开物 | publication | `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-01-05` | `04-knowledge/units/publications/tiangong-kaiwu.md` |
| 营造法式 | publication | `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-06-40` | `04-knowledge/units/publications/yingzao-fashi.md` |
| 莲鹤方壶 | work | `2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-01` | `04-knowledge/units/works/lianhe-fanghu.md` |

35 条重复候选一律 `needs_evidence -> rejected`，理由中写明并入的 canonical 与目标 KU。

## 方法

1. 以 2026-10-25 跨书召回结果为输入，锁定六书全命中的 7 组。
2. 逐组回读六册 Markdown 原文，核对实体是否同名同物，以及各来源的表述差异。
3. 每组保留一条 canonical 候选，走 `needs_evidence -> ready_for_review -> approved -> applied`；其余走 `needs_evidence -> rejected`。
4. 裁决写入本包 `candidate-decision-ledger.jsonl`，以追加 transition 叠加，不改写历史 R1 账本。
5. 写回采用 exact change-set：7 条 `create`，无 update、无 delete；`apply-plan.jsonl` 记录目标路径、candidate_id 与写入后的 sha256、字节数、行数。
6. 写回后统一重建候选投影、刷新生成态投影并跑全部机械门禁。

## 来源差异（保留，未强行统一）

- **考工记**：成书年代有春秋末期、周代、战国、先秦、春秋末至战国初五说；作者未署，来源转述“齐国官书／稷下学宫”为学术意见，非本库考证。
- **黄道婆**：籍贯有“松江乌泥泾（今上海华泾镇）”与夏燕靖“江苏松江乌泥泾”两说；崖州在赵农笔下作海南岛三亚。
- **越窑**：烧造起点有东汉、东汉末、商周、六朝四说；本 KU 只确认唐五代为鼎盛期，上限不裁定。窑址范围与“秘色”称谓各来源亦有出入。
- **天工开物**：成书年 1636／1637；卷数 18／19；插图数 121／122／123。三组异文并存。
- **营造法式**：卷数 35／36；作者用字“李诫／李诚”；彩画分类高丰作三大类、夏燕靖 2016 作六类。
- **莲鹤方壶**：年代“春秋／春秋中期”；高度 118／122 厘米；器名“莲鹤方壶／莲鹤铜方壶”。
- **孔子**：无实体性冲突；差异集中在评价取向，高丰既肯定其审美观念又批评其“因循守旧”。

## 验证

| 门禁 | 结果 |
|---|---|
| `build_discovery_index.py` | total 5339；applied 7；rejected 36；needs_evidence 5296；issues 空 |
| `run_sync_closure.py --refresh-generated --full --check-generated` | passed |
| `audit_content_quality.py` | total_findings 0 |
| `audit_relation_consistency.py` | broken target 0；invalid relation_type 0；missing inverse 0；weak evidence 0；isolated units 7 |
| `audit_repo.py --summary` | structural 122/130 |
| `generate_governance_backlog.py` | P0/P1/P2 均无活跃项 |
| `pre_commit_check.py` | 规则漂移 0 |

七单元统一取 `confidence: medium`、`consensus: tentative`、`evidence_status: source_backed`；没有任何单元被标为 confirmed、externally_verified 或 L1–L7 已验证。

## 边界与未解决项

- 未 commit、未 push；改动只在工作树。
- 未创建分支或额外 worktree，主线仍只有 `main`。
- `02-sources/` 未改动，来源只读。
- 未使用外部验证平台，证据仅限六册 Markdown 文本。
- 未做图版与器物视觉核验。
- Theme 与 Topic 尚未 materialize，7 个 KU 的 `primary_theme` 与 `topic_memberships` 留空，`hierarchy_assignment` 仍为 0 分，属研究债务。
- 未写入正式 `relations`；KU 之间的共现只在正文中以“不构成关系断言”的说明出现。
- 剩余 5296 条 active 候选仍为 `needs_evidence`，尚未做语义裁决。
