# 第十四批：person doc_count=2 组（L 批）裁决总结

## 一、本批做了什么

本批处理 14 个 `doc_count=2` 的 person 同名组，共 28 个候选：

- 13 组新建 person KU；
- 1 组（xdup-0211 夏燕靖）整组拒绝：两册候选均为来源作者简历／版本元数据，属来源 paratext，不进入中国设计史知识层；
- 13 个同组非 canonical 候选以“同一 entity、语义已并入”rejected；
- 0 个 no_delta，0 个既有 KU 更新。

状态链：13 条 canonical 走 `needs_evidence -> ready_for_review -> approved -> applied`；13 条 merged member 与 2 条夏燕靖候选走 `needs_evidence -> rejected`。台账共 54 行，apply-plan 共 13 行 create。

## 二、十三个新建 KU

| group_id | 实体 | slug | 维度 | sub_type | 主要来源 |
|---|---|---|---|---|---|
| xdup-0203 | 丰子恺 | `feng-zikai` | C | designer | 赵农 2009 L8105-L8136；夏燕靖 2016 L5034 |
| xdup-0205 | 刘昼 | `liu-zhou` | A | philosopher | 夏燕靖 2009 L1931-L1943；2016 L2425-L2432 |
| xdup-0206 | 利玛窦 | `li-madou` | E | scholar | 赵农 2009 L6635-L6652；李立新 2011 L1236-L1239 |
| xdup-0207 | 卫改 | `wei-gai` | B | craftsman | 田自秉 2010 L2639；李立新 2011 L1848-L1853 |
| xdup-0208 | 吕彦直 | `lu-yanzhi` | B | architect | 赵农 2009 L7780-L7811；夏燕靖 2016 L5063-L5090 |
| xdup-0209 | 商汤 | `shang-tang` | D | statesman | 赵农 2009 L1067-L1098；夏燕靖 2016 L624-L627 |
| xdup-0212 | 大禹 | `dayu` | D | other | 赵农 2009 L1040-L1071；夏燕靖 2016 L774-L787 |
| xdup-0214 | 孙中山 | `sun-yat-sen` | D | statesman | 赵农 2009 L7754-L7785；夏燕靖 2016 L4877-L4891 |
| xdup-0215 | 张光宇 | `zhang-guang-yu` | C | designer | 赵农 2009 L8105-L8136；夏燕靖 2016 L5991-L5998 |
| xdup-0217 | 张衡 | `zhang-heng` | B | scientist | 赵农 2009 L2523-L2554；夏燕靖 2016 L1720-L1726 |
| xdup-0219 | 曾国藩 | `zeng-guofan` | D | statesman | 赵农 2009 L8504-L8506；夏燕靖 2016 L4929-L4960 |
| xdup-0221 | 朱启钤 | `zhu-qijian` | D | scholar | 赵农 2009 L7868-L7871；夏燕靖 2016 L6247-L6252 |
| xdup-0222 | 朱熹 | `zhu-xi` | A | philosopher | 赵农 2009 L5746-L5753；李立新 2011 L1111-L1132 |

## 三、夏燕靖整组拒绝

xdup-0211 的两个候选分别是：

- 夏燕靖 2009 `cand-01-02`，L54-L65，作者简历；
- 夏燕靖 2016 `cand-01-01`，L11-L6538，全书 front matter 范围。

两者都是来源元数据，不是设计史主体。本批不建 person KU，也不把它们并入任何既有条目。该判定同时为后续批次立下规则：来源作者、编者、出版社信息不进入 KU 层。

## 四、canonical 与 rejected

- canonical 选择以“内容最完整、proposed_slug 与最终文件名最接近”为准：13 组分别落在赵农、夏燕靖、李立新、田自秉四册。
- 13 个非 canonical 候选均因同一 entity 合并而 rejected，`target_ref` 指向新建 KU。
- 夏燕靖 2 条 rejected 无 `target_ref`；`build_discovery_index.py` 允许 `target_ref` 缺省。
- 异写 slug 统一：`feng-zi-kai`／`feng-zikai` 取 `feng-zikai`；`zhu-qidian` 取 `zhu-qijian`；`sun-yatsen` 取 `sun-yat-sen`；`yu-the-great` 取 `dayu`。

## 五、关键发现

1. **民国书籍装帧谱系成形**：丰子恺、张光宇与既有陈之佛 KU 在赵农 2009 的同一段谱系中被并列，C 维度首次出现三人并置。
2. **A 维度的设计思想线索连续化**：墨子“先质后文”、孔子“文质彬彬”、刘昼“施用有宜”、朱熹“简易／致用／道即器，器即道”构成从先秦到宋的连续讨论。
3. **D 维度人物密度上升**：孙中山、曾国藩、朱启钤、商汤、大禹五人进入 D 维度，覆盖王朝建立、洋务工业、近代建筑制度与服制改革。
4. **B 维度出现技术—艺术复合人物**：张衡（浑天仪、地动仪）、吕彦直（中山陵）、卫改（武氏祠画像石），分别对应汉代仪器、近代建筑与汉代石刻。
5. **跨文化节点前移**：利玛窦把西器与科学知识传入放到明末，与既有郎世宁、圆明园叙事形成早晚两端。
6. **paratext 混入被识别**：夏燕靖组说明候选生成会把作者简历当 person；后续 doc1 组与 ungrouped 中的作者名需按同一规则判别。
7. **来源内部张力多处保留**：商汤立国年代（前 1711／前 1600）、刘昼朝代（北朝／北齐）与引文用字（黡／麕）、张衡被误作“张仪”，均并列照录，未做调和。

## 六、状态与验证

| 项目 | 结果 |
|---|---|
| 新建 KU | 13 |
| 更新 KU | 0 |
| rejected 候选 | 15 |
| ledger 行 | 54 |
| apply-plan 行 | 13 |
| apply-plan 哈希核对 | 13/13 |
| KU 总数 | 187 |
| 候选索引 | 5,339 行；applied 178、no_delta 10、rejected 469、needs_evidence 4,682 |
| lifecycle | active 4,682、terminal 657 |
| 内容质量审查 | 187 KU，0 findings |
| 仓库审查 | 0 问题；evidence 187/187；persons 53 |
| pre-commit | 规则漂移 0 |
| sync closure | 19 steps；250 passed, 16 subtests |
| doc_count=2 同名组 | 共 352，已关闭 29，剩余 323 |
| doc_count≥3 open | 0 |
| doc_count=1 open | 6 |
| open members | 647 |

## 七、边界与研究债

- 未 commit、未 push；只改工作树。
- 未新建分支或 worktree；只保留 `main`。
- `02-sources/` 与 `03基础书籍-md文档/` 只读。
- 未使用外部验证平台；未做图版、器物、手稿或档案核对。
- 13 条 KU 均为 `confidence=medium`、`consensus=tentative`、`evidence_status=source_backed`。
- `primary_theme` 与 `topic_memberships` 留空；Theme/Topic 尚未 materialize。
- 未写入正式 `relations`；同段并置只作非断言性叙述。
- 本批只覆盖前六册；Book 7 及以后未启动。
