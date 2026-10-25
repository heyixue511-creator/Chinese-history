# 第八批写回：跨六书 7 组 publication 知识元

- 工作包：`06-runtime/automation/2026-10-25-three-book-publication-units-a/`
- 状态：`applied`
- 日期：2026-10-25
- 范围：Books 1–6（前六本）；Book 7 及以后不启动

## 一、批次范围

`doc_count = 3` 一层共 **103 组、309 条候选**。上一批清完 `person` 类后，本批取 `publication` 类的前半，共 **7 组、21 条候选**（`xdup-0098`–`xdup-0104`）：

| 组 | 实体 | canonical 候选 | 写回文件 | KU source_count |
|---|---|---|---|---|
| xdup-0098 | 东京梦华录 | `2009-xiayanjing-…:cand-04-82` | `publications/dongjing-menghua-lu.md` | 3 |
| xdup-0099 | 古今图书集成 | `2004-gaofeng-…:cand-07-12` | `publications/gujin-tushu-jicheng.md` | 3 |
| xdup-0100 | 吕氏春秋 | `2009-zhaonong-…:cand-04-26` | `publications/lvshi-chunqiu.md` | **6** |
| xdup-0101 | 墨经 | `2009-xiayanjing-…:cand-03-01` | `publications/mo-jing.md` | 3 |
| xdup-0102 | 孟子 | `2009-zhaonong-…:cand-04-34` | `publications/mengzi.md` | **4** |
| xdup-0103 | 山海经 | `2009-zhaonong-…:cand-03-60` | `publications/shanhai-jing.md` | **5** |
| xdup-0104 | 梓人遗制 | `2009-zhaonong-…:cand-09-27` | `publications/ziren-yizhi.md` | **4** |

- 每组 `member_count = 3`：1 条升为 canonical 并写回 KU，2 条转为 `rejected` 并注明并入目标；
- `publication` 类 `doc_count = 3` 共 14 组，本批处置前 7 组，余 **7 组、21 条**（`xdup-0105`–`xdup-0111`：王祯农书、程氏墨苑、茶经、诗经、陶说、雪宦绣谱、马可波罗游记）；
- 本批之后 `doc_count = 3` 余 **61 组、182 条**：`term` 34 组、`work` 20 组、`publication` 7 组。

`publication` 类知识元由 8 个增至 **15 个**；基础类型覆盖仍为 8/8。

## 二、canonical 映射与 slug 归一

7 组的 slug 写法只有 4 组不一致，文件名一律取带连字符形式：

- `xdup-0098`：`dongjing-meng-hua-lu` / `dongjing-menghualu` / `dongjing-menghua-lu` → `dongjing-menghua-lu.md`
- `xdup-0100`：`lv-shi-chun-qiu` / `lvshi-chunqiu` / `lushi-chunqiu` → `lvshi-chunqiu.md`
- `xdup-0101`：`mo-jing` / `mojing` / `mojing` → `mo-jing.md`
- `xdup-0102`：`meng-zi` / `mengzi` / `mengzi` → `mengzi.md`
- `xdup-0103`：`shanhaijing` / `shanhaijing` / `shanhai-jing` → `shanhai-jing.md`
- `xdup-0104`：`ziren-yizhi` / `ziren-yizhi` / **`ziyan-yizhi`** → `ziren-yizhi.md`（`ziyan` 为“梓”误作“子”，不采用）
- `xdup-0099`：三册 slug 一致。

**同名跨类型**：`publications/mengzi.md` 与既有的 `persons/mengzi.md` basename 相同，是本库第一次出现同名跨类型组。两个文件都新增了 `disambiguation` 字段：人物条沿用 `Mencius`（该条的 `translation_note` 早已为此预留），典籍条用 `Mengzi`。`audit_repo.py` 报“同名跨类型组 1 / 有消歧说明 2 / 无消歧说明 0”，未触发扣分。

## 三、方法

- 逐组复读召回该书的 Markdown 原文，并在**六册**范围内把同一书名的所有出现位置再核一遍。检索时把**带书名号的《书名》**与**不带书名号的人名、学派名**分开计数——例如“孟子”在六册共 40 余处，其中多数是人物与篇名引用，只有 zn 4 处、tzb 1 处、xy16 3 处、llx 1 处（《孟子·离娄章句》）是典籍面证据；
- 因此 4 个 KU 的 `source_count` 大于组的 `doc_count`：
  - 吕氏春秋 **6**：六册全部引用（候选组只召回赵农、李立新、夏燕靖 2016；复读另补高丰 3 处、夏燕靖 2009 2 处、田自秉 2 处）；
  - 山海经 **5**：另补高丰 2 处、田自秉 2 处；
  - 孟子 **4**：另补田自秉 2 处；
  - 梓人遗制 **4**：另补夏燕靖 2009 L5144–L5146。
- 逐条差异**记录而不裁决**：纪年、卷数、引文用字、篇名、书的范围、作者断代一律原文并列，另在“验证状态”的“未见于来源”栏列出六册未载项；
- 状态诚实：7 个 KU 一律 `confidence: medium`、`consensus: tentative`、`evidence_status: source_backed`，不填 `verification_level`（未做外部验证）。

## 四、主要来源差异

- **东京梦华录**：卷数（十卷）仅夏燕靖 2009 给、问世年（1147）仅夏燕靖 2016 正文给，两条从未并见；服饰引文赵农作“士农工商”、夏燕靖两版作“士、农、商”（脱“工”）；“三更”／“三鼓”；“瓦舍 50 多所”为赵农三书合记、“园林 18 处”为本书独记，取证强度不同，已分注。
- **古今图书集成**：年代三说（雍正四年 1726 两年印成／雍正年间完成／不给年）；性质两说（世界最大百科全书／百科全书式工具书）；字体与插图为高丰独有、函数（522 函）为赵农独有；同段活字谱系在枣木活字字数、丛书卷数、华燧印书年三处互有出入，丛书名亦作《武英殿珍版丛书》／《武英殿聚珍版丛书》。
- **吕氏春秋**：六册用法分四簇互不重叠；全书结构 8 览 6 论 12 纪仅夏燕靖 2016 给；饕餮纹引文三处用字不同（纹／无纹、其／己、又／以）；**夏燕靖两版正文均作《简读》而同册文献表均作《简选》，两版讹字相同**，可判同一底稿；《己篇》一名六册仅一见（通行本作《先己》）；高丰 L536 引文“未者，尤之时”残损并作“《商群书》”。
- **墨经**：夏燕靖两版正文近乎逐字相同（差异仅四字句）；**夏燕靖 2016 册内定义冲突**——正文把几何学、光学、力学归《墨经》，书末条目却把“墨经”限定为六篇“着重阐述认识论和逻辑思想”，并把工艺思想归《墨子·节用》；赵农三条原理原文为六册唯一；“桔槔”归《墨子》不归《墨经》。
- **孟子**：同一引文两册写法不同（李立新脱“继之以”、把“以为”作“以”）；篇名仅李立新给《离娄章句》；评价口径三说（政治观／幻想／对设计功用的指导）；**夏燕靖 2016“四书五经”并称只列 8 种，且把被解释的《论语》排除在名单外**。
- **山海经**：五册各引一段、无两册引同一段；夔的引文高丰作“状如华”、田自秉作“状如牛”且多出“黄帝得之……声闻五百里”；凤皇与鸾鸟末句同为“见则天下安宁”而主角不同，两册互不提及；李立新“《山海经》所绘”一语已标注其表述强度，不读作原书有图之证。
- **梓人遗制**：断代三说（宋人／元代／宋末元初语境）；全书范围两说（两部分／织机专著）；罗机子释义（罗织机／交织机）；田自秉“不用棱子”当作“不用梭子”，照录不改。

另记录若干**册内自相矛盾**与文本残缺，均按原样写出、不代改：夏燕靖 2016 墨经条、孟子“四书五经”条、夏燕靖两版吕氏春秋篇名条，以及高丰“未者，尤之时”与“《商群书》”。

## 五、验证结果

| 检查 | 结果 |
|---|---|
| `build_discovery_index.py` | total 5339；applied 69→**76**；needs_evidence 5066→**5045**；rejected 204→**218**；issues 0 |
| `audit_content_quality.py` | 104 个知识元，总发现 **0** |
| `audit_repo.py` | 结构健康 **122/130**（与基线同）；type coverage 8/8；同名跨类型组 1 / 无消歧说明 0 |
| `build_runtime_index.py` | `06-runtime/automation/index.md` 已刷新 |
| `run_sync_closure.py --refresh-generated --full --check-generated` | **sync closure passed**（250 tests、16 subtests、19 步） |
| `pre_commit_check.py` | 规则漂移 **0**，exit 0 |
| apply-plan 哈希复核 | **8/8** 与磁盘一致（7 条 create 的 after 指纹 + 1 条 update 的 after 与 before） |
| 台账不变量 | 35 行、21 个唯一 `candidate_id`、7×3 条 canonical transition + 14 条 rejected |

## 六、边界与未解决项

- **未提交**：本批只在工作树内完成，未 commit、未 push；用户未就该次外部状态变更给出授权。
- **未建分支／worktree**：只保留 `main`。
- **`02-sources/` 未动**：实际读取的是 `03基础书籍-md文档/`（只读）。
- **未决候选**：`publication` 类余 7 组 21 条（`xdup-0105`–`xdup-0111`）；`xdup-0329` 的两条《韩非子》书志候选仍保留 `needs_evidence`。
- **研究债务（已在各 KU 的“相关知识元”段登记）**：《商君书》《诗经》《左传》《淮南子》《管子》《荀子》《世本》《庄子》《春秋公羊传》《论语》等无 `publications/` 条目；吕不韦、宋尹学派、萧兵、公输般、有扈氏、夏后启、伶伦、孟元老、薛景石、郭璞、驺衍、尸佼、惠施、陈梦雷、蒋廷锡、金简、翟金生、番禺、吉光均无条目；中国营造学社无 `institutions/` 条目；夔纹、饕餮纹、窃曲纹、凤皇纹、双鸾衔绶纹、镇墓兽、子弹库帛书、秤、桔槔、辘轳、滑轮、云梯、华机子等无 `works/` 条目；“规矩”“准绳”“淫巧”“度程”无 `terms/` 条目。
- **未建正式关系**：本批所有跨条并置（`lvshi-chunqiu` ↔ `kaogongji` ↔ `zhouli`；`mo-jing` ↔ `kaogongji` ↔ `mozi`；`mengzi`（publication）↔ `mengzi`（person）↔ `lvshi-chunqiu`；`shanhai-jing` ↔ `lvshi-chunqiu` ↔ `shuowen-jiezi` ↔ `xi-zhong`；`ziren-yizhi` ↔ `yuan-ye` ↔ `wang-zhen` ↔ `huang-daopo`）只写作非断言性散文，`relations` 未写入任何一条。
- **层级未 materialize**：7 个 KU 的 `primary_theme`、`topic_memberships` 均留空，`hierarchy_scope_note` 说明当前只到 Dimension。
