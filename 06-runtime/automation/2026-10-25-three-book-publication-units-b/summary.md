# Publication 批次 B — 七组书志知识元写回

- 工作包：`06-runtime/automation/2026-10-25-three-book-publication-units-b/`
- 状态：`applied`
- 日期：2026-10-25
- 上一批：`2026-10-25-three-book-publication-units-a/`

---

## 一、批次范围

本批收口 `doc_count = 3` 层里剩下的七个 `publication` 召回组（`xdup-0105` 至 `xdup-0111`），共 **21 个候选**（每组 3 个），写入 **7 个书志知识元**，同组 14 个同名候选转 `rejected`。另改写 **2 个既有 person 知识元**（`persons/shen-shou.md`、`persons/zhang-jian.md`），属非候选驱动的失效陈述更正。

本批之后，`doc_count = 3` 层内的 `publication` 组 **14/14 全部关闭**。此前的 7 组由批次 A 关闭，本批关闭末 7 组。

| 实体 | 组 | 写入文件 | 来源数 | bytes | lines | after_sha256（前 12 位） |
|---|---|---|---|---|---|---|
| 王祯农书 | xdup-0105 | `publications/wang-zhen-nongshu.md` | 4 | 14750 | 141 | `sha256:04e2f` |
| 程氏墨苑 | xdup-0106 | `publications/chengshi-moyuan.md` | 5 | 9650 | 129 | `sha256:0f12e` |
| 茶经 | xdup-0107 | `publications/chajing.md` | 3 | 12748 | 124 | `sha256:15b84` |
| 诗经 | xdup-0108 | `publications/shijing.md` | 6 | 22147 | 157 | `sha256:93350` |
| 陶说 | xdup-0109 | `publications/tao-shuo.md` | 4 | 13107 | 141 | `sha256:30f18` |
| 雪宦绣谱 | xdup-0110 | `publications/xuehuan-xiupu.md` | 4 | 12328 | 139 | `sha256:27727` |
| 马可波罗游记 | xdup-0111 | `publications/makeboluo-youji.md` | 5 | 15765 | 146 | `sha256:11b4b` |

两条 update 行：

| 实体 | 文件 | before | after |
|---|---|---|---|
| 沈寿 | `persons/shen-shou.md` | 12439 bytes / 134 lines | 12534 / 134（`sha256:1d84e`） |
| 张謇 | `persons/zhang-jian.md` | 11685 bytes / 136 lines | 11749 / 136（`sha256:7ff28`） |

来源范围仍为前六册，书籍 7 及以后不启动。

---

## 二、canonical 映射与 slug 归一

每组取覆盖最广的成员作 canonical，其余两名并入同一 KU 并转 `rejected`：

| 组 | 实体 | canonical 候选 | 并入成员（2） | KU |
|---|---|---|---|---|
| xdup-0105 | 王祯农书 | `2009-zhaonong-zhongguo-yishu-shejishi:cand-09-65` | 夏燕靖 2009 `cand-05-46`、夏燕靖 2016 `cand-07-31` | `publications/wang-zhen-nongshu.md` |
| xdup-0106 | 程氏墨苑 | `2009-xiayanjing-zhongguo-shejishi:cand-06-76` | 李立新 `cand-05-44`、夏燕靖 2016 `cand-08-55` | `publications/chengshi-moyuan.md` |
| xdup-0107 | 茶经 | `2004-gaofeng-zhongguo-shejishi:cand-04-08` | 田自秉 `cand-08-34`、夏燕靖 2016 `cand-05-33` | `publications/chajing.md` |
| xdup-0108 | 诗经 | `2009-zhaonong-zhongguo-yishu-shejishi:cand-02-60` | 田自秉 `cand-04-31`、夏燕靖 2016 `cand-02-48` | `publications/shijing.md` |
| xdup-0109 | 陶说 | `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-08-49` | 高丰 `cand-sup-70`、田自秉 `cand-12-05` | `publications/tao-shuo.md` |
| xdup-0110 | 雪宦绣谱 | `2009-xiayanjing-zhongguo-shejishi:cand-07-31` | 田自秉 `cand-12-42`、夏燕靖 2016 `cand-11-88` | `publications/xuehuan-xiupu.md` |
| xdup-0111 | 马可波罗游记 | `2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-07-30` | 夏燕靖 2009 `cand-05-62`、赵农 `cand-08-194` | `publications/makeboluo-youji.md` |

**slug 归一（4 个实体、5 个非规范写法）**：文件名一律取规范连字符形式，候选流水线里的原写法不采用。

| 规范化 | 候选中的写法 | 说明 |
|---|---|---|
| `wang-zhen-nongshu` | `wangzhen-nongshu` | 姓名连写 |
| `chajing` | `cha-jing` | 词内多余连字符 |
| `tao-shuo` | `taoshuo` | 书名连写 |
| `makeboluo-youji` | `make-polo-youji`、`make-polou-youji` | 后者 `polo` 误拼作 `polou`，不采用 |

`chengshi-moyuan`、`shijing`、`xuehuan-xiupu` 三个组内三册写法一致，无需归一。

---

## 三、方法

1. **逐组复读六册**，不依赖候选摘要。每组都回到召回段的原文，并另扫全六册检索同一实体。
2. **书名号与人名分离计数**。带《》的题名与不带书名号的作者、器物、地名分开统计，避免把人物提及当作书证：
   - 赵农 L4748 只提“陆羽”而无《茶经》，不计入来源；
   - 李立新 L971 的“**波罗子**”是法门寺地宫器物名（“波罗子和银芙蕖”），与马可·波罗无关，直接排除；
   - 夏燕靖 2009 L2861 引马可·波罗而无书名，仅因同册另有本书专条才计入，并在 KU 内注明这一取证方式。
3. **来源扩充而非收缩**。召回组的 `doc_count = 3` 是流水线的名义计数，复读六册后有 6 组实际来源多于 3：

   | 实体 | group_doc_count | KU source_count | 增出的册 |
   |---|---|---|---|
   | 王祯农书 | 3 | 4 | 高丰 |
   | 程氏墨苑 | 3 | 5 | 高丰、赵农 |
   | 茶经 | 3 | 3 | — |
   | 诗经 | 3 | 6 | 高丰、夏燕靖 2009、李立新 |
   | 陶说 | 3 | 4 | 夏燕靖 2009 |
   | 雪宦绣谱 | 3 | 4 | 高丰 |
   | 马可波罗游记 | 3 | 5 | 高丰、田自秉 |

   增出的每一册都在 KU 的 `sources` 中逐行登记，不是笼统补数。
4. **不裁定分歧**。年份、章名、引文用字、责任者、性质判断的差异一律并存记录，各注明出自何册何行；KU 只做“哪册说了什么”的对照，不做“哪个对”的判断。
5. **截断引文按跨度取证**。原文被误插的章节标题或图题截断时，记录行号跨度而不只摘后半句：程氏墨苑（赵农 L7174—L7178，中间插入“第九章 专制的文化——明清时期的设计”）、诗经（夏燕靖 2016 L909—L914，中间插入图题“2-29. 商代 甲骨文‘车’的拓片”）。
6. **状态诚实**。七个 KU 一律 `confidence: medium`、`consensus: tentative`、`evidence_status: source_backed`，不填 `verification_level`，不标 confirmed。
7. **两条非候选 update 行**。`candidate_id` 为 `null`，因二者不是候选驱动的写回，而是本批建立 `publications/xuehuan-xiupu.md` 后原文陈述失效：
   - `persons/shen-shou.md` 原写“`publications/` 下现无该书条目，属研究债务”；
   - `persons/zhang-jian.md` 原写“沈寿……无独立 KU”与“《雪宦绣谱》应建 publication 条目而无”。

   两处均只替换该段，行数不变（134、136），不改任何事实陈述。`before` 指纹由逆向复原该段替换后计算，复原脚本对每条替换作 `assert` 校验。

---

## 四、主要来源差异

| 实体 | 分歧点 | 各册说法 |
|---|---|---|
| 王祯农书 | 卷数 | 夏燕靖 2009：37 集 371 目、约 13 万余字；夏燕靖 2016：37 集本（6＋11＋20）与 22 卷本（6＋4＋12）两版并给、13.6 万字、插图 281 幅；赵农：36 卷（1—6、7—26、27—36）、13 万 6 千字、281 幅 |
| | 第三部分名 | 百谷谱（夏燕靖两版）／谷谱（赵农） |
| | 活字实践 | 赵农：活木字三万多个、印 6 万字《旌德县志》、音韵轮与杂字轮；高丰：大德元年（1297）、转轮排字盘；夏燕靖两版：只列《杂录》篇目“造活字印书法” |
| | 讹写 | 高丰 L3634 书名作《农布》、作者作“王桢”；夏燕靖 2016 图题作“简车”（2009 作“筒车”） |
| 程氏墨苑 | 年份 | 夏燕靖两版与李立新：1605 年；高丰：只作万历年间；赵农：不给 |
| | 刻工名 | 李立新：黄**鏻**；赵农：黄**磷** |
| | 套印色数 | 仅高丰给数：“近 50 幅插图……四色或五色”，并举《巨川舟楫图》五色；李立新只作“五色套印” |
| | 技术名 | 三册三讹：高丰“饅版”、夏燕靖 2009“短版”、李立新“恒版”，通行作“饾版” |
| 茶经 | 性质 | 高丰：“世界上第一部综合论茶的著作”；夏燕靖 2016：“我国乃至世界现存最早，又是最全面介绍茶艺的一部著作”——“第一部”与“现存最早”不是同一种断言 |
| | 茶碗品第详略 | 高丰引全文（六州次第＋“邢不如越”三条理由）；田自秉只作“越州上”“类玉”“类冰”；田自秉另处只列 5 州且不带次第 |
| | 独有项 | 十节全名、24 种饮茶用具、后续茶书谱系（《茶录》《大观茶论》《茶谱》《茶史》等）仅夏燕靖 2016 给 |
| 诗经 | 使用层次 | 赵农立“资料性文献”一目、以四十余处引诗覆盖十余类器物；田自秉给工序与形式法则（青铜器“二方连续”对《诗经》“一唱三叹”）；夏燕靖两版给六条史证；高丰给五条单证；李立新只取“道”的引申 |
| | 引文用字 | “十亩之间”：赵农作“桑者闲闲兮”并另给“十亩之外兮，桑者泄泄兮”，其余三册同作“十亩之间兮，桑者泄泄兮”；“萋兮斐兮”夏燕靖 2016 作“蔓兮斐兮”；毳衣句 2009 脱一字、2016 作“如英(tǎn)”（当作菼） |
| | 讹写 | 赵农 L2401“《诗经》《诗经》”书名重出；夏燕靖 2016 L909—L914 句读被图题截断 |
| 陶说 | 卷次 | 夏燕靖 2009：说今、说古、说明、说器上、说器中、说器下（六篇）；夏燕靖 2016：四大部分辖六卷（卷 4—6 为说器） |
| | 版本 | 仅 2016：正文条作“乾隆三十九年（1774）鲍廷博刻本”，附录条只作“初刻本 1774”而不提鲍廷博 |
| | 定位 | “我国第一部陶瓷史”仅 2016 作，且正文条与附录条措辞不同；2009 不作此判 |
| | 同句两用 | “戗金、镂银……无不以陶为之，仿效而肖”一句，田自秉本多“于是”二字并读作材料本性（“只能说是拙”），高丰本无“于是”并读作官搭民烧与社会风气 |
| 雪宦绣谱 | 末章章名 | 夏燕靖两版：“绣通”；田自秉：“绣道” |
| | 记录者 | 高丰与夏燕靖两版：“张謇记录整理”（两版另给张謇撰序）；田自秉：只作“有人根据……沈寿的口述” |
| | 断代与性质 | 清末（夏燕靖两版）／清末民初（田自秉）／晚年（高丰）；“理论著作”／“苏绣的艺术实践经验”／“经验的积累”与“总结” |
| | 册内错误 | 夏燕靖 2016 L4139 把丁佩《绣谱》系于“明代”（田自秉作清末道光），同句又把《农政全书》写作《农事全书》 |
| 马可波罗游记 | 作者身份 | “意大利旅行家”（2009，附 1254—1324）／“旅行家和商人”（2016）／“传说中的”（赵农）／“欧洲最伟大的旅行家”（高丰） |
| | 成书方式 | 2009：“回国后写成了”；2016：“海战中被俘，在监狱里他口述……由狱友鲁斯蒂谦（Rustichello da Pisa）写出” |
| | 书名与又名 | 2009 给《东方闻见录》；2016 删去该名而增 Il Milione；田自秉一律作《马可波罗游记》不带间隔号 |
| | 大都人口 | 夏燕靖两版：“约十万户”；赵农：“人口百万”——计量单位不同，两说并存而不互校 |
| | 同句两用 | “百物输入之众，有如川流之不息”：赵农证商业繁盛，田自秉证丝织原料巨量输入与劳民伤财（“仅丝一项，每日入城者计有千车”） |
| | 文本讹误 | 夏燕靖 2016 L4070“大街宽 **24 四步**”（2009 作“二十四步”） |

---

## 五、验证结果

| 检查 | 结果 |
|---|---|
| `build_discovery_index.py` | total 5339；applied 83（本批前 76）；needs_evidence 5024（前 5045）；rejected 232（前 218）；issues 空 |
| `audit_content_quality.py` | 111 个知识元，总发现 **0** |
| `audit_repo.py` | 结构健康 122/130（与基线同）、知识结构 55/65、证据链 55/55；知识元 111；`publications` 15 → **22**；type coverage 8/8；同名跨类型组 1 / 无消歧说明 0；Frontmatter 问题 0；证据引用 111/111 |
| `build_runtime_index.py` | `06-runtime/automation/index.md` 已刷新 |
| `pre_commit_check.py` | 规则漂移 **0** |
| `run_sync_closure.py --refresh-generated --full --check-generated` | **sync closure passed**（250 tests、16 subtests、19 步） |
| apply-plan 独立复核 | **9/9** 行与磁盘一致（7 create 的 after 指纹与字节行数、2 update 的 after 指纹与 before 指纹） |
| 台账不变量 | 35 行 / 21 个唯一 `candidate_id` / 状态计数 `rejected 14`、`ready_for_review 7`、`approved 7`、`applied 7` |

**剩余量核算（逐组回算，不按每组 3 条估算）**。

批次 A 收尾时记“本批之后余 61 组、182 条”。本批完成后重新从 `candidate-index.jsonl` 逐组回算：

```
closed groups by type {'event': 1, 'institution': 7, 'person': 17, 'place': 9, 'procedure': 1, 'publication': 14}
open   groups by type {'term': 34, 'work': 20}
open   members by type {'term': 102, 'work': 59}
total open groups 54   open members 161
```

- 本批前：61 组 / 182 条 = term 34/102 ＋ work 20/59 ＋ publication 7/21 —— 与批次 A 的记载相符，**不是算术错误**；
- 本批关闭 publication 末 7 组 / 21 条，故本批后为 **54 组 / 161 条**；
- 需要注意 **work 20 组只有 59 条**（其中一组仅 2 名成员），任何按“每组 3 条”估算剩余量的算法都会多算 1 条。

---

## 六、边界与未解决项

**本批未做的事**

- 未 commit、未 push，改动只留在工作树。
- 未创建分支或额外 worktree，`main` 是唯一主线。
- `02-sources/` 未触碰；本批实际只读 `03基础书籍-md文档/`。
- 未使用任何外部验证平台；证据范围仅限于六册 Markdown 文本，未查原书、未查图版、未核馆藏。
- `primary_theme`、`topic_memberships` 一律留空，因 Theme/Topic 节点尚未 materialize。
- 未写入任何正式 `relations`；跨条目共现只在正文以非断言方式提及。

**照录不改的册内错误**（属来源事实，不属本批修订权限）

- 夏燕靖 2016：丁佩《绣谱》系于明代、《农事全书》、“大街宽 24 四步”。
- 赵农：《诗经》《诗经》书名重出；程氏墨苑句被章节标题截断。
- 高丰：《农布》、“王桢”、“饅版”。
- 夏燕靖 2009：“短版”；李立新：“恒版”。三册对“饾版”的讹写各不相同。
- 田自秉：《雪宦绣谱》记录者只作“有人”，本批不替它补名。

**留给后续治理的债**

1. `sub_type` 取值超出 taxonomy 枚举。`taxonomy.md` 对 `publication` 只列 `monograph | journal_article | manifesto | report | textbook | edited_volume`，而磁盘上已有 `classic`（吕氏春秋、孟子、墨经、山海经、周礼，本批新增诗经）、`reference_work`（古今图书集成，本批新增程氏墨苑）、`lexicographic_work`（说文解字）三种越界值。`audit_repo.py` 与 `audit_content_quality.py` 均不校验该枚举，故未阻断。本批取最小改动：沿用已存在的越界值，不新增第四种（王祯农书、陶说、雪宦绣谱、马可波罗游记一律 `monograph`）。
2. 《韩非子》的 `publication` 组 `xdup-0329` 为 `doc_count = 2`（赵农 `cand-04-25`、夏燕靖 2016 `cand-01-65`），不在本批关闭的 `doc_count = 3` 层内，仍为 `needs_evidence`；`publications/` 下仍无该书条目。
3. 候选 slug 存在误拼，除本批已归一者外，尚有 `ziyan-yizhi`（梓误作子，属上一批）。
4. 剩余工作量为 **term 34 组 102 条**、**work 20 组 59 条**，两组均为 `needs_evidence`，本批未启动。
