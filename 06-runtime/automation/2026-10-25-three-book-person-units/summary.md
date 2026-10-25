# 第六批写回：跨三书 9 组 person 知识元

- 工作包：`06-runtime/automation/2026-10-25-three-book-person-units/`
- 状态：`applied`
- 日期：2026-10-25
- 范围：Books 1–6（前六本）；Book 7 及以后不启动

## 一、批次范围

`doc_count = 3` 一层共 **103 组、309 条候选**。本批取其中 `person` 一类的首批，共 **9 组、27 条候选**（`xdup-0071`–`xdup-0079`）：

- 9 组在本批写回，每组 `member_count = 3`：1 条升为 canonical 并写回 KU，2 条转为 `rejected` 并注明并入目标；
- `doc_count = 3` 一层累计已覆盖 27 组（前两批 institution／procedure／event 9 组 + place 9 组 + 本批 person 9 组）；
- 余 **76 组、228 条候选**仍为 `needs_evidence`：person 8 组 24 条（`xdup-0080`–`xdup-0087`）、publication 14 组 42 条、term 34 组 102 条、work 20 组 60 条。

`person` 类知识元由 13 个增至 **22 个**；基础类型覆盖仍为 8/8。

组内 slug 写法有分歧的有 4 组：`xdup-0071`（`ding-huan` / `dinghuan` / `ding-huan`）、`xdup-0073`（`yuwen-kai` / `yu-wen-kai` / `yuwen-kai`）、`xdup-0075`（`zhuang-zi-person` / `zhuangzi` / `zhuangzi`，前者疑为哲学家与书名消歧）、`xdup-0077`（`zhang-zhidong` / `zhang-zhidong` / `zhang-zhi-dong`）。`xdup-0076` 三条 slug 一致（`pang-xunli`），但该 slug 本身编码的是姓名的 OCR 讹形，不是异读。

**本批最重要的一项边界判断**：`xdup-0076` 三册候选均作“庞薰栗”。这不是另一个人，而是讹字——六册共出现 **8 种字形**（栞、琴、栗、琍、某、渠、桀、杲），**无一处写作规范字“琹”**。KU 标题取规范名“庞薰琹”，八种字形在正文单列统计，候选标题不沿用。同类但较轻的两处：文震亨的曾祖在高丰作“文徵明”、在赵农作“文征明”；夏燕靖两版作“沈葆祯”，通行为“沈葆桢”，仅记录未改字。

## 二、canonical 映射

| 组 | 实体 | 类型 / sub_type | canonical 候选 | 写回文件 | KU source_count |
|---|---|---|---|---|---|
| xdup-0071 | 丁缓 | person / craftsman | `2004-gaofeng-…:cand-01-13` | `04-knowledge/units/persons/ding-huan.md` | 3 |
| xdup-0072 | 奚仲 | person / craftsman | `2009-xiayanjing-…:cand-01-79` | `04-knowledge/units/persons/xi-zhong.md` | 5 |
| xdup-0073 | 宇文恺 | person / architect | `2009-xiayanjing-…:cand-04-67` | `04-knowledge/units/persons/yuwen-kai.md` | 3 |
| xdup-0074 | 左宗棠 | person / statesman | `2009-xiayanjing-…:cand-06-27` | `04-knowledge/units/persons/zuo-zongtang.md` | 3 |
| xdup-0075 | 庄子 | person / philosopher | `2009-zhaonong-…:cand-04-31` | `04-knowledge/units/persons/zhuangzi.md` | 6 |
| xdup-0076 | 庞薰琹 | person / designer | `2010-tianzibing-…:cand-01-03` | `04-knowledge/units/persons/pang-xunqin.md` | 6 |
| xdup-0077 | 张之洞 | person / statesman | `2004-gaofeng-…:cand-07-21` | `04-knowledge/units/persons/zhang-zhidong.md` | 3 |
| xdup-0078 | 张謇 | person / industrialist | `2004-gaofeng-…:cand-07-15` | `04-knowledge/units/persons/zhang-jian.md` | 4 |
| xdup-0079 | 文震亨 | person / scholar | `2004-gaofeng-…:cand-06-03` | `04-knowledge/units/persons/wen-zhenheng.md` | 5 |

KU 的 `source_count` 按该实体在六册中是否有字面命中计数，与本组 `member_count = 3` 不等。庄子、庞薰琹两组六册全有命中；奚仲 5 册（田自秉不记）、文震亨 5 册（田自秉引《长物志》但未提撰者，不计）、张謇 4 册（田自秉、李立新不记）、丁缓／宇文恺／左宗棠／张之洞各 3 册。差额来自 `doc_count = 3` 之外的册次，已在各 KU 的 `sources` 中列明。

## 三、方法

1. **六册复读而非三册**：每组除三册召回来源外，另在其余三册中检索该实体。庄子、庞薰琹两组因此从 3 册扩到 6 册；文震亨、奚仲各扩到 5 册。只读召回的三册会漏掉高丰为丁缓给出的万向支架原理段、李立新为奚仲给出的证据等级警告、高丰为文震亨单设的一整节。
2. **差异记录而非裁决**：纪年、字数、职衔、评价取向的冲突全部原文并列保留并标注出处。本批冲突密度高于前两批，典型者为宇文恺大兴城工期“9 个月”与“30 余年”、张謇“先驱”与“官商一体”、文震亨《长物志》的“雅俗”与“以用为本”两种读法。
3. **状态链**：canonical 走 `needs_evidence → ready_for_review → approved → applied`；同组其余 2 条走 `needs_evidence → rejected`，reason 中写明 canonical 目标。
4. **追加式台账**：`candidate-decision-ledger.jsonl` 共 45 行（27 + 9 + 9），覆盖 27 个唯一 `candidate_id`，只以 transition 叠加，不改写历史 R1 台账。
5. **类型化写回**：`apply-plan.jsonl` 为 9 条 `create` + 1 条 `update`，无 `delete`；逐条重算哈希并核对。**这是本库第一条 `update` 行动**。
6. **更新的边界**：`persons/chen-zhifo.md` 原有一句“庞薰琹……尚未单独成 KU”，在本批写出 `pang-xunqin.md` 后即为假。只改这一句，其余字段不动；行内记 `before` 与 `after` 的 sha256／bytes／lines，`candidate_id` 为 `null` 并在 note 中说明——该文件由更早批次写回，未生成过 apply-plan 行，不能借用别的候选 id 冒充来源。
7. **不重复既有对象**：文震亨条的《长物志》书志细节交给 `publications/changwu-zhi.md`，左宗棠条的船政局细节交给 `institutions/fujian-chuanzhengju.md`，两条均在正文与“相关知识元”段明写这一分工。人物条只做身份、动因、评价与跨书差异的合成。
8. **验证分级克制**：9 个 KU 一律 `confidence: medium`、`consensus: tentative`、`evidence_status: source_backed`，不填 `verification_level`。张謇、张之洞、庞薰琹三条的来源评价已足以支撑 `disputed`，但字段契约要求 `consensus: disputed` 必须配 L1–L7 验证层级，本批未做外部验证，故不升级。

## 四、主要来源差异

| 实体 | 差异 |
|---|---|
| 丁缓 | 常满灯（高丰、赵农）与“恒满灯”（田自秉）；七龙五凤与九龙五凤；赵农所引《西京杂记》含“本出房风，其法后绝，至缓始更为之”故判为“恢复和延续”，田自秉引文脱去该句且作“机环转之者，运四周”，高丰未引该句并判为“发明”；七轮扇仅高丰记载；三册身份定位分别为设计家、工匠、巧工 |
| 奚仲 | “黄帝造车”与“奚仲作车”两说仅高丰并列并以“难以定夺”收束；板轮改辐轮被赵农明确系于奚仲，夏燕靖两版只陈述技术变化而不系于人；李立新引《墨子·非儒篇》并把古籍记载降为“先民的集体性历史记忆”，是六册中唯一的证据等级警告；李立新另把奚仲读作“薛地制车业”的地望标记，赵农读作单个发明家 |
| 宇文恺 | 大兴城工期“仅用了 9 个月”（夏燕靖两版）与“用了 30 余年……完成了规模宏伟的大兴城的修建”（赵农，若自 582 年起算 30 年已越其卒年 612）；里坊数 108（夏燕靖两版）与 110 坊（赵农，同册两处一致）；宇文恺的明堂仅系“建议按古制建筑明堂”，赵农所记建成者为武则天垂拱四年所造，两者不可混同；高丰、田自秉、李立新不记其人 |
| 左宗棠 | 夏燕靖两版同段并存“1872 年，他在奏报创办福建船政局意图时说”与“1866 年 5 月，他上奏清廷创办福建船政局”——前者为事后追述、后者为创议之年，来源未加说明；“用 35 年的时间，造船舰 40 艘”跨越其卒年 1885，应指船政事业整体存续期；“沈葆祯”与通行“沈葆桢”字形不同；赵农只在总结章列入洋务官员名单并给“强政府非民生”的批判框架 |
| 庄子 | 籍属“宋国”（高丰、赵农）与“蒙人也”（田自秉引《史记》）；生卒前 369—前 286 仅夏燕靖 2016 给出；李立新同册既称其生态理想为“人类最早的造物理性哲学思考”，又称诸子思想“并没有真正影响到当时的造物行为”，评价与效力判断分属两层；夏燕靖 2016 记内篇为庄子所作，而六册所引《天道》《秋水》《知北游》《盗跖》《说剑》《天下》多属外杂篇 |
| 庞薰琹 | 姓名 8 种字形且同页异写（高丰 L5479 先“琍”两次后“栗”两次；夏燕靖 2009 L4194 先“琍”后“某”两次）；机构名与结局——高丰作“工商美术社”并记其开办与办展，李立新作“大熊工商美术社”并记“尚在筹建中即遭流产”；《巩固民间美术工艺的成就》叙述文均作 1953 年 12 月 7 日而年表均列于 1954 年条下；庞薰琹美术馆开馆年 2009 版系于 1990 年、2016 版系于 1991 年 |
| 张之洞 | 命题三表述：“中学为体，西学为用”（高丰）／“旧（中）学为体，西学为用”（赵农标张之洞语）／“中体西用”（李立新）；奏议同侪“两江总督刘坤一”（高丰）与“赵尔巽、张之洞等人”（李立新）；督职写法高丰同册并存“湖广总督”（L5239）与“两湖总督”（L5453，清代无此职），赵农作“两广总督”（L6886，与光绪年间铸龙洋相符，非 1901 年之职）；李瑞清职衔“学堂监督”（高丰）与“督学”（李立新） |
| 张謇 | 高丰称“中国近代纺织教育和纺织工业的先驱”并与沈寿并列为近代织绣两位人物，赵农以“官商一体”判其“无法推动中国社会生产力的进步”，四册事实无冲突而评价对立；耀徐玻璃公司年份只作“其后”，“这两家玻璃公司不久即停业或倒闭”为合并判断未分列；田自秉、李立新不记其人，而《雪宦绣谱》在两册均有完整章节记述 |
| 文震亨 | 《长物志》主旨两种读法：高丰据《几榻》《器具》读作“古式”“古制”的雅俗体系，夏燕靖两版（尤其 2016 增写“长物”典出《世说新语》一段）读作“以用为本”的实用性；高丰分卷统计“五卷”加“六卷”共十一卷，未归组者为“衣饰”；赵农造园家名单把文震亨与其曾祖文征明、以及虚构人物曹雪芹并列；“宁古勿时，宁朴勿巧，宁俭勿俗”与“令居之者忘忧，寓之者忘归，游之者忘倦”仅赵农引 |

## 五、验证结果

| 门禁 | 结果 |
|---|---|
| `apply-plan` 哈希核对 | 10/10 与磁盘一致（9 create 的 after-sha256；1 update 的 before／after；bytes、lines；CRLF 归一） |
| `build_discovery_index.py` | total 5339，applied 61，needs_evidence 5092，rejected 186，无 issue |
| `audit_content_quality.py` | 0 项发现（89 个知识元） |
| `audit_repo.py` | structural health 122/130；类型覆盖 8/8（person 13→22）；deprecated_type_drift 0；验证语义问题 0 |
| `build_runtime_index.py` | 已刷新 `06-runtime/automation/index.md`（8 个批次目录） |
| `run_sync_closure.py --refresh-generated --full --check-generated` | sync closure passed（250 tests、16 subtests、19 步全过） |
| `pre_commit_check.py` | 规则漂移 0 |

状态迁移的算术核对：前批 needs_evidence 5119 → 本批 9 条 canonical 转 `applied`、18 条重复候选转 `rejected` → 5119 − 9 − 18 = **5092**。applied 52 → 61，rejected 168 → 186。另 1 条 `update` 不涉及候选状态，只改既有 KU 的一行表述。

## 六、边界与未解决项

- 未 commit、未 push；仅工作树变更。
- 未建分支、未建 worktree；`main` 为唯一主线。
- `02-sources/` 只读，未改写；本批实际读取的源目录为 `03基础书籍-md文档/`。
- 未使用外部验证平台，证据仅限六册 Markdown 文本；未做图版、遗址、器物或人物肖像核验。
- `primary_theme` 与 `topic_memberships` 留空：Theme / Topic 节点尚未 materialize，已计入 research debt。
- 未写入正式 `relations`：9 个 KU 均处于 isolated 状态，跨 KU 共现（如庞薰琹—陈之佛的两条设计教育线、文震亨—《长物志》的人物—著作配对）只在正文以非断言方式记述。
- `doc_count = 3` 一层 103 组中已覆盖 27 组；余 **76 组（228 条候选）**仍为 `needs_evidence`，未作状态推进。
- **Batch B 已定界但未启动**：person 余 8 组 `xdup-0080`–`xdup-0087`（李春、李渔、毛晋、沈寿、王祯、计成、赵过、韩非子）。
- 人物类结构性缺口（本批暴露）：沈葆桢、魏源、刘坤一、赵尔巽、阎立德、李瑞清、高颎、陶行知、雷圭元、李有行、张光宇、郑可、沈福文、张仃、祝大年、吴劳、梅健鹰、吕凤子、姜丹书、计成、李渔、高濂、张涟父子、陈启源等在六册中均有可引文本但尚无 KU，已作为研究债务写入相关 KU 的“相关知识元”段。
- 著作类结构性缺口：《雪宦绣谱》在夏燕靖两版有完整章节记述，`publications/` 下无条目，导致张謇条的人物—著作关系缺一端；《劝学篇》、癸卯学制章程、丁佩《绣谱》同属此类。
- 机构类结构性缺口：湖北工艺学堂、三江师范学堂、江南储才学堂、兰州制造局、甘肃织呢局、南通学院均无 `institutions/` 条目。
- 庞薰琹的 8 种字形未做版本学溯源：无法判定哪些属原书排印、哪些属 OCR 转录所致，来源本身不含图版比对信息。
- 张謇、张之洞、庞薰琹三条的评价对立（先驱／官商一体、创始人／强政府、开办／流产）在来源内无法判定，需外部文献才能推进，属 open dispute。
