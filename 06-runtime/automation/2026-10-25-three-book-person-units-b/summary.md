# 第七批写回：跨三书 8 组 person 知识元

- 工作包：`06-runtime/automation/2026-10-25-three-book-person-units-b/`
- 状态：`applied`
- 日期：2026-10-25
- 范围：Books 1–6（前六本）；Book 7 及以后不启动

## 一、批次范围

`doc_count = 3` 一层共 **103 组、309 条候选**。本批取 `person` 类的第二批，共 **8 组、24 条候选**（`xdup-0080`–`xdup-0087`）：

- 8 组在本批写回，每组 `member_count = 3`：1 条升为 canonical 并写回 KU，2 条转为 `rejected` 并注明并入目标；
- 另把 `doc_count = 2` 组 `xdup-0249` 的两条候选（赵农、李立新均题作“韩非”）按**同一实体**并入 `persons/han-fei-zi.md`。这两条不在本批 `doc_count = 3` 的组规则内，属跨组同实体合并，理由逐条写进 rejected 的 `reason`；
- 至此 `person` 类的 `doc_count = 3` 组**清零**：17 组全部处置完毕（前批 9 组 + 本批 8 组）；
- 余 **68 组、203 条**仍为 `needs_evidence`：`term` 34 组、`work` 20 组、`publication` 14 组。本批之后已无 `person`／`place`／`institution`／`event`／`procedure` 的 `doc_count = 3` 组。

`person` 类知识元由 22 个增至 **30 个**；基础类型覆盖仍为 8/8。

组内 slug 写法有分歧的有 2 组：`xdup-0084`（`wangzhen` / `wangzhen` / `wang-zhen`）、`xdup-0087`（`han-fei-zi` / `hanfeizi` / `hanfeizi-person`）。两组的文件名均取带连字符形式（`wang-zhen.md`、`han-fei-zi.md`），归一关系记入 manifest 的 `canonical_mapping`。其余 6 组三种 slug 写法一致。

**本批的一次跨批修正**：写 `persons/ji-cheng.md` 时发现 `publications/yuan-ye.md` 有两处误系——其一，该条把李立新《中国设计艺术史论》L1013 列为来源并单列“李立新定位”一条，而全册“园冶”零命中、“计成”七处全为“设计成”连写造成的字面误配（另有“不计成本”一处）；其二，该条把“附图 235 幅”系于高丰，而 235 只见于夏燕靖 2009、夏燕靖 2016、赵农三册，高丰只给三卷与篇目、不给图幅数。两处在 apply-plan 中以 `update` 行动留痕（`candidate_id` 为 `null`，注明非候选驱动），并连带删去六册零命中的别名“园牧”、把“1634 刊行”标为年号换算。该文件的 `before` 指纹取首批写回时 apply-plan 的 create 行记录，并以逐条逆向复原的文本核对一致（`95e4f035…`，5858 字节，120 行）。

## 二、canonical 映射

| 组 | 实体 | 类型 / sub_type | canonical 候选 | 写回文件 | KU source_count |
|---|---|---|---|---|---|
| xdup-0080 | 李春 | person / craftsman | `2009-xiayanjing-…:cand-04-66` | `04-knowledge/units/persons/li-chun.md` | 3 |
| xdup-0081 | 李渔 | person / scholar | `2004-gaofeng-…:cand-06-05` | `04-knowledge/units/persons/li-yu.md` | 4 |
| xdup-0082 | 毛晋 | person / other | `2009-xiayanjing-…:cand-06-11` | `04-knowledge/units/persons/mao-jin.md` | 4 |
| xdup-0083 | 沈寿 | person / artist | `2004-gaofeng-…:cand-07-16` | `04-knowledge/units/persons/shen-shou.md` | 4 |
| xdup-0084 | 王祯 | person / engineer | `2009-xiayanjing-…:cand-05-48` | `04-knowledge/units/persons/wang-zhen.md` | 5 |
| xdup-0085 | 计成 | person / designer | `2004-gaofeng-…:cand-06-01` | `04-knowledge/units/persons/ji-cheng.md` | 5 |
| xdup-0086 | 赵过 | person / engineer | `2009-xiayanjing-…:cand-03-58` | `04-knowledge/units/persons/zhao-guo.md` | 3 |
| xdup-0087 | 韩非子 | person / philosopher | `2009-xiayanjing-…:cand-02-77` | `04-knowledge/units/persons/han-fei-zi.md` | 6 |

`毛晋` 的 `sub_type` 取 `other`：`person` 的子类型枚举为 designer／craftsman／scholar／educator／artist／engineer／architect／other，无“出版家”，正文已说明取 `other` 的理由。

## 三、方法

- 逐组复读召回该实体的 Markdown 原文，并在**六册**范围内把同一人物的所有出现位置再核一遍（不只是组内三册），因此 5 个 KU 的 `source_count` 大于组的 `doc_count`；
- 两处字面陷阱已在检索时规避：
  - “计成”须用 `(?<!设)计成` —— 同一语料中“设计成”连写，直接检索李立新一册得 7 处假阳性；
  - “王祯”须与“王桢”同查 —— 赵农与高丰两册一律作“王桢”，只查“王祯”会得出两册不记此人的假阴性；
- 候选组的“册数”是召回时的标称值，与实体在六册中的字面命中数不等。本批实测：李春 3、李渔 4（田自秉、李立新零命中）、毛晋 4（高丰、田自秉零命中）、沈寿 4（李立新零命中）、王祯 5（含两册作“王桢”）、计成 5（李立新为“设计成”误配，不计）、赵过 3（高丰、田自秉、李立新零命中）、韩非子 6；
- 逐条差异**记录而不裁决**：纪年、字数、卷数、职衔、评价取向的冲突一律原文并列，另在“验证状态”的“未见于来源”栏列出六册未载项；
- 状态诚实：8 个 KU 一律 `confidence: medium`、`consensus: tentative`、`evidence_status: source_backed`，不填 `verification_level`（未做外部验证）。

## 四、主要来源差异

- **李春**：建桥年代（595—605 十年区间／605 单年）；“最早”所指（现存双曲石拱桥／世界石拱桥）；三册同源于唐《安济桥铭》一句，无一册给出铭文出处。高丰、田自秉、李立新三册既无“李春”也无“赵州桥”。
- **李渔**：生卒 1610—1680 仅高丰孤证；赵农同册“《闲情偶寄》／《闲情偶记》”互见；“阚铎／阐铎”“笺简／笺筒”“联匮／联匾”三组字形；《芥子园画谱／画传》的书名与李渔的参与程度三说并存（含赵农同册两处不一致）。
- **毛晋**：汲古阁的雇工规模、刻书种数、书板数在四册间互不相同；李立新把套版与拱花另立一线且两处均作“恒版”（通行作“饾版”），只记录不改字。
- **沈寿**：《雪宦绣谱》记录者（张謇记录整理／田自秉作“有人”不指名）；末章章名（绣道／绣通）；该书性质三说；相邻断代分歧（丁佩《绣谱》明代／清末道光）。
- **王祯**：七处分歧——姓名用字（王祯／王桢）、《农书》卷数（37 集／22 卷／36 卷／37 卷）、第三部分名（百谷谱／谷谱）、木活字发明权的表述、转轮装置称名（盘／法／架／无专名）、农具名目用字（鏻-鐏、糬-耰、麴-麹）、夏燕靖 2016 的生卒 1271—1368（与元朝起讫年完全相同）。
- **计成**：《园冶》地位的四种逐级加强断言；分卷两种拆法；卷二与装折的层级归属；“三分匠，七分主人”的两种解释；插图数在夏燕靖 2016 同段内自相矛盾（235 幅／200 余幅／235 张）。
- **赵过**：发明对象（三脚耧／耧车）；战国耧车是否存在；耦犁推广是否归赵过；“代田法”六册零命中。
- **韩非子**：“外储说／外诸说”同段两种写法；利口与文采的评价同段并存；木鸢引文“蜚／飞”与两版解释转向；师承仅赵农一册给出。

另记录若干**册内自相矛盾**与文本残缺，均按原样写出、不代改：夏燕靖 2016 的计成段先“附图 235 幅”后“200 余幅”再“插图 235 张”，且有一分句重复两遍；夏燕靖 2009 L3692 的对应句在“这是我国古代最系统的园林设”处截断、句未终；高丰 L3634 把《农书》误作《农布》；夏燕靖 2016 作“简车”“未耜”“汜胜之”（应作筒车、耒耜、氾胜之）；赵农 L5332 与高丰 L3634／L4001 作“王桢”。

## 五、验证结果

| 检查 | 结果 |
|---|---|
| `build_discovery_index.py` | total 5339；applied 61→**69**；needs_evidence 5092→**5066**；rejected 186→**204**；issues 0 |
| `audit_content_quality.py` | 97 个知识元，总发现 **0** |
| `audit_repo.py --summary` | 结构健康 **122/130**（与基线同）；type coverage 8/8；deprecated_type_drift 0 |
| `build_runtime_index.py` | `06-runtime/automation/index.md` 已刷新 |
| `run_sync_closure.py --refresh-generated --full --check-generated` | **sync closure passed**（250 tests、16 subtests、19 步） |
| `pre_commit_check.py` | 规则漂移 **0**，exit 0 |
| apply-plan 哈希复核 | **9/9** 与磁盘一致（8 条 create 的 after、1 条 update 的 after；update 的 before 与首批 create 行记录一致） |
| 台账不变量 | 42 行、26 个唯一 `candidate_id`、8×3 条 canonical transition + 18 条 rejected |

## 六、边界与未解决项

- **未提交**：本批只在工作树内完成，未 commit、未 push；用户未就该次外部状态变更给出授权。
- **未建分支／worktree**：只保留 `main`。
- **`02-sources/` 未动**：实际读取的是 `03基础书籍-md文档/`（只读）。
- **未决候选**：`xdup-0329`（`doc_count = 2`，`publication`）的两条《韩非子》书志候选保留 `needs_evidence` —— 本批写的是人物 KU，`publications/` 下仍无《韩非子》条目，不把未写的条目记为已写。
- **研究债务（已在各 KU 的“相关知识元”段登记）**：赵州桥无 `works/` 条目（桥体数据暂由 `li-chun.md` 承载）；《雪宦绣谱》《闲情偶寄》《王祯农书》《韩非子》无 `publications/` 条目；汲古阁无 `institutions/` 条目；耧车、耦犁、三脚耧、秧马、木鸢无 `works/` 条目。
- **未建正式关系**：本批所有跨条并置（`ji-cheng` ↔ `wen-zhenheng` ↔ `li-yu`；`shen-shou` ↔ `zhang-jian`；`zhao-guo` ↔ `wang-zhen` ↔ `xi-zhong`；`han-fei-zi` ↔ `mozi` ↔ `xunzi` ↔ `zhuangzi`）只写作非断言性散文，`relations` 未写入任何一条。
- **层级未 materialize**：8 个 KU 的 `primary_theme`、`topic_memberships` 均留空，`hierarchy_scope_note` 说明当前只到 Dimension。
- **后续批次**：`doc_count = 3` 余 68 组、203 条（`term` 34 组、`work` 20 组、`publication` 14 组）。按用户范围限定，仍只在前六本内推进。
