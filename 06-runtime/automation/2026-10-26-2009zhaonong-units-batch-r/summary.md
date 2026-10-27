# 2026-10-26-2009zhaonong-units-batch-r 收口

## 一、范围与目标

- 来源：赵农《中国艺术设计史》（高等教育出版社，2009）Markdown 文本。
- 范围：「总结」L8484–L8560。
- 目标：把总结段 9 条 unit 候选全部裁定为新建，并完成写回、索引重建与同步闭合。
- 本批不处理附录、参考文献与图版来源；不启动 Book 7 及以后；未做 commit / push。

## 二、覆盖与复读

| 段落主题 | 行范围 | 候选 | 新建 | 说明 |
|---|---:|---:|---:|---|
| 鸦片战争与洋务运动 | L8502–L8515 | 4 | 4 | 林则徐、水晶宫、魏源、冯桂芬 |
| 自强著述 | L8506 | 1 | 1 | 《校邠庐抗议》 |
| 新文化运动 | L8533 | 3 | 3 | 陈独秀、胡适、康有为 |
| 欧洲中国风 | L8540 | 1 | 1 | 中国风 |
| 合计 | L8484–L8560 | 9 | 9 | 无 update、no_delta、rejected |

复读方式：逐段阅读总结正文与图注；候选 `source_span` 为块级粗跨度，实际引用行逐条回查。图总结-1 至图总结-7 未做视觉核验。

## 三、9 条裁定总表

| # | 候选 | 实体 | 裁定 | 目标 | 证据 |
|---:|---|---|---|---|---|
| 1 | cand-12-122 | 林则徐 | create | persons/lin-zexu.md | L8502 |
| 2 | cand-12-124 | 水晶宫 | create | works/shuijinggong.md | L8502 |
| 3 | cand-12-125 | 魏源 | create | persons/wei-yuan.md | L8504 |
| 4 | cand-12-128 | 冯桂芬 | create | persons/feng-guifen.md | L8506 |
| 5 | cand-12-129 | 《校邠庐抗议》 | create | publications/xiaobinlu-kangyi.md | L8506 |
| 6 | cand-12-144 | 陈独秀 | create | persons/chen-duxiu.md | L8533 |
| 7 | cand-12-146 | 胡适 | create | persons/hu-shi.md | L8533 |
| 8 | cand-12-148 | 康有为 | create | persons/kang-youwei.md | L8533 |
| 9 | cand-12-149 | 中国风 | create | terms/zhongguo-feng.md | L8540 |

## 四、9 条新建分型

- 人物 6：林则徐、魏源、冯桂芬、陈独秀、胡适、康有为。
- 作品 1：水晶宫。
- 出版物 1：《校邠庐抗议》。
- 术语 1：中国风。

维度分布：primary E 6 条、primary D 2 条、primary B 1 条；secondary D 4 条、secondary E 4 条、secondary A 1 条。confidence：medium 7 条、low 2 条。

## 五、合并与分层边界

- 冯桂芬与《校邠庐抗议》分列人物与著述，不因同句出现合并。
- 水晶宫作为建筑作品入 works，不按博览会机构立目。
- 中国风作为欧洲接受中国工艺的文化风尚入术语，不与中国工艺品类条目合并。
- 曾国藩、左宗棠、李鸿章、张之洞、张謇、孙中山、郑观应、詹天佑等虽有提及，但不在本批候选内，未新建。
- 《海国图志》《新青年》《建国方略》《盛世危言》等未在本批立目，避免超出候选范围扩写。

## 六、语义复读修正

1. **年份存疑照录**：林则徐条原文把英国发动鸦片战争系于 1842 年，与他处常见分期可能不合；条目照录并标注存疑，不径改。
2. **人物与著作分层**：冯桂芬条只记其人与引文，成书信息留给《校邠庐抗议》条；两条互不替代。
3. **宏观判断不扩写**：中国风条只著录来源所列瓷器、丝织品、漆器、壁纸、印刷术、火药、文化典籍，不补具体国家、年代分段与器物谱系。
4. **图版未视觉核验**：图总结-1 至图总结-7 只作位置记录，未据图扩写。

## 七、验证与门禁

- `_zn_struct.py _zn_ch10r_files.txt`：problems 0（9 文件）。
- `_zn_audit.py _zn_ch10r_files.txt`：findings 0。
- `_zn_audit_strict.py _zn_ch10r_files.txt`：findings 0。
- `_zn_checklines_ch10r.py`：9 条、20 处引文，problems 0。
- 工作包 `2026-10-26-2009zhaonong-units-batch-r`：ledger 27 行，apply-plan 9 行，create 9。
- 候选索引写回 9 条，全部 `needs_evidence → applied`，`lifecycle_class: terminal`。
- 索引与闭合：`build_discovery_index.py` 5339 条，`build_translation_index.py` 1707 条；`run_sync_closure.py --refresh-generated --full` 通过，250 tests + 16 subtests。
- 状态：applied 2338、rejected 852、no_delta 193、needs_evidence 1956、terminal 3383；total_units 2099；health 102/130。
- 内容审计 12 项，均为既有问题，无一项落在本批文件。

## 八、赵农 2009 册收口状态

- 赵农 2009 册第十章 unit 候选已全部处理完毕：batch O 31、batch P 32、batch Q 21、batch R 9，共 93 条。
- 本册剩余 `needs_evidence` 中已无赵农 2009 的 unit 候选；后续如有 claim 候选另按 claim 流程处理。
- 本册新建与更新的 KU 已进入索引、翻译索引与生成态投影；未做来源外核对。

## 九、下一跳

- 转入 2010 田自秉《中国工艺美术史》（404 条候选），再处理 2011 李立新（189 条 unit、1363 条 claim）。
- 仍按单册单源、逐段复读、候选逐条裁定的节奏推进；每批完成写回、索引、闭合与 summary。
- 未 commit、未 push；`03基础书籍-md文档/` 未改写；未创建分支或 worktree；Book 7 及以后未启动。
