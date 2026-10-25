# 术语批次 F — 器物、服饰与家具九组知识元写回

- 工作包：`06-runtime/automation/2026-10-25-nine-object-dress-term-units/`
- 状态：`applied`
- 日期：2026-10-25
- 上一批：`2026-10-25-six-prehistoric-term-units/`

---

## 一、批次范围

本批处理器物、服饰与家具的 **9 个同名组**、**27 个候选**，写入 **9 个知识元**，18 个候选转 `rejected`。全部为新建，无 update、无 delete。

| 实体 | 组 | 写入文件 | sub_type | 来源数 | bytes | lines | after_sha256（前 12 位） |
|---|---|---|---|---|---|---|---|
| 几 | xdup-0113 | `terms/ji-furniture.md` | furniture_form | 3 | 8795 | 110 | `sha256:fd8730e38ea2` |
| 博山炉 | xdup-0117 | `terms/boshanlu.md` | vessel_form | 3 | 9574 | 116 | `sha256:b25011fbaa98` |
| 扣器 | xdup-0124 | `terms/kouqi.md` | lacquerware_type | 3 | 7329 | 109 | `sha256:91850cb1939d` |
| 铜镜 | xdup-0139 | `terms/tongjing.md` | device_type | 3 | 9004 | 118 | `sha256:6ee6360c70b0` |
| 汉镜 | xdup-0128 | `terms/hanjing.md` | device_type | 3 | 9384 | 124 | `sha256:334c2f2e826a` |
| 清式家具 | xdup-0129 | `terms/qing-style-furniture.md` | furniture_style | 3 | 11950 | 121 | `sha256:6dbf9e81015c` |
| 秦砖汉瓦 | xdup-0132 | `terms/qin-zhuan-han-wa.md` | building_component | 3 | 8986 | 123 | `sha256:b1f9c54d19dd` |
| 幞头 | xdup-0121 | `terms/futou.md` | headwear_form | 3 | 9000 | 128 | `sha256:e864e6648f3d` |
| 霞帔 | xdup-0140 | `terms/xiapei.md` | clothing_accessory | 3 | 7922 | 117 | `sha256:1498cc7d66c5` |

来源范围仍为前六册，书籍 7 及以后不启动。9 个 KU 均为 `confidence=medium`、`consensus=tentative`、`evidence_status=source_backed`，未做外部验证。每组的 3 册来源即该组的全部 doc_count，`ku_source_count` 均为 3。

---

## 二、四处结构性判断

### 1. 铜镜与汉镜分成通名与断代两条

`xdup-0139`（铜镜）与 `xdup-0128`（汉镜）是两组独立召回，但语义上是总类与汉代分段的关系。本批分写两条：`terms/tongjing.md` 记通名、战国四大特点、赵农的齐家文化起源说与唐镜；`terms/hanjing.md` 记汉代三期、规矩镜、铭文、商标与透光镜。两篇互相指认，不合并为一条，也不把汉镜写成铜镜的重复候选。

铜镜组的 canonical 取 2016 候选，汉镜组同取 2016，保持同一册的断代口径；赵农的汉镜段虽更详，仍作为 canonical 的第二来源并入。

### 2. 清式家具是风格概念，不是清代家具全称

高丰明确分期：清初至康熙前期仍是明式延续，典型清式产生于康熙晚期至乾隆，嘉庆道光后衰落。故 `terms/qing-style-furniture.md` 的 `sub_type` 取 `furniture_style`，与既有 `terms/ming-style-furniture.md` 成对；不取 `furniture_form`，也不把"清代家具"整体等同于清式。

### 3. 秦砖汉瓦是合称，瓦当另有单条

`terms/wadang.md` 已存在。本批新建 `terms/qin-zhuan-han-wa.md`，`sub_type` 取 `building_component`，覆盖砖、瓦、瓦当与砌拱，正文明确"瓦当条只记瓦当，本条兼记砖、瓦、瓦当与砌拱"。两条不合并，边界写入 scope_note 与相关知识元，未写入正式 `relations`。

### 4. 服饰两条按部件分层

幞头在头，取 `headwear_form`；霞帔在身，取 `clothing_accessory`。二者同属服饰类但部件不同，不成上下位关系。霞帔与既有 `terms/buzi.md` 都以禽纹示品级，正文只作非断言性并置。

---

## 三、本批最重要的语义发现

### 1. 汉镜的镜体厚薄，两册方向相反

- **夏燕靖两版**："汉代铜镜的设计特点是：体薄、平边、圆钮"。
- **赵农**："镜体比战国铜镜加大增厚"。
- 夏燕靖在同册战国段又说战国镜"胎体很薄，不如汉唐铜镜的厚重"，与赵农的"比战国加大增厚"同向，却与夏燕靖自己的汉镜"体薄"句相反。两处可能各以不同参照立论，来源未说明，KU 并列不裁定。

### 2. 铜镜的起点，战国与齐家文化相差整个商周

- **夏燕靖两版**："铜镜从战国时期开始出现并流行"。
- **赵农**："铜镜的起源是在新石器时期晚期的齐家文化"，并举甘肃齐家坪素面镜、青海贵南七星纹镜；商周"已有 20 余面铜镜出土"，妇好墓 4 面。

这与 `places/yinxu.md` 所记高丰"殷商时期铜镜至今才发现 5 面，其中 4 面出土于妇好墓"的统计口径不同。本批不合并两套计数，只在铜镜 KU 的"相关知识元"中指明差异。

### 3. 霞帔的时代、性质与形态，三处同时分歧

- **夏燕靖两版**：只说明代，"恩赐贵妇专用"饰品，深青缎绣云霞禽纹，一至七品各有禽纹。
- **赵农**：宋代一般女服即"大袖、长裙、霞帔"；明清"霞帔为佩带的饰物，是用彩带连缀的金玉坠子，多为贵族妇女所佩"。

两套描述不仅时代不同，形态也不同：一为绣禽纹的深青缎饰，一为彩带连缀的金玉坠子。KU 并列，不把"恩赐贵妇专用"扩写为宋元通制，也不把坠饰等同于明代霞帔。

### 4. 秦砖汉瓦的得名句与两处原文疑点

夏燕靖两版都说砖瓦"烧成后吸水有声，故后世有'秦砖汉瓦'之称"。"吸水有声"与常见的"叩之有声"不合，两版相同，未径改，标为待核。2016 又引《三国志》记汉武帝"杜陵南山下，有成瓦窑数千处"；《三国志》成书晚于汉武帝，书名与所记事不合，同样照录待核。

其余较轻的分歧还有：几的定性（"放置东西或者可以倚伏"对"小的或矮的桌子"）、扣器的外延（高丰总类对夏燕靖窄义）、清式家具的苏作评价（高丰"明式风格已几乎丧失"对田自秉"大体继承明式"）、幞头的汉代来源（"幞头、幅巾"对"幅巾"）、博山炉的两篇《薰炉铭》、2016 霞帔"崔纹"当为"翟纹"，均并列写入正文与 manifest 的 `source_variance_notes`。

---

## 四、canonical 映射

| 组 | 实体 | canonical 候选 | 并入成员 | KU |
|---|---|---|---|---|
| xdup-0113 | 几 | 夏燕靖 2016 `cand-03-36` | 夏燕靖 2009 `cand-02-56`、赵农 `cand-04-151` | `terms/ji-furniture.md` |
| xdup-0117 | 博山炉 | 高丰 `cand-02-14` | 赵农 `cand-05-15`、田自秉 `cand-06-31` | `terms/boshanlu.md` |
| xdup-0124 | 扣器 | 夏燕靖 2016 `cand-02-80` | 高丰 `cand-sup-09`、夏燕靖 2009 `cand-02-29` | `terms/kouqi.md` |
| xdup-0139 | 铜镜 | 夏燕靖 2016 `cand-03-41` | 夏燕靖 2009 `cand-02-59`、赵农 `cand-03-136` | `terms/tongjing.md` |
| xdup-0128 | 汉镜 | 夏燕靖 2016 `cand-03-132` | 夏燕靖 2009 `cand-03-14`、赵农 `cand-05-12` | `terms/hanjing.md` |
| xdup-0129 | 清式家具 | 高丰 `cand-07-06` | 赵农 `cand-10-75`、田自秉 `cand-12-85` | `terms/qing-style-furniture.md` |
| xdup-0132 | 秦砖汉瓦 | 夏燕靖 2016 `cand-04-06` | 夏燕靖 2009 `cand-03-36`、赵农 `cand-04-112` | `terms/qin-zhuan-han-wa.md` |
| xdup-0121 | 幞头 | 夏燕靖 2016 `cand-05-46` | 夏燕靖 2009 `cand-04-46`、赵农 `cand-07-52` | `terms/futou.md` |
| xdup-0140 | 霞帔 | 夏燕靖 2016 `cand-08-59` | 夏燕靖 2009 `cand-05-74`、赵农 `cand-08-159` | `terms/xiapei.md` |

canonical 选择规则：**优先选 `proposed_slug` 与最终文件名一致的候选；多个一致时取 2016 夏燕靖升级版候选；无 2016 且多条一致时取出版年最早者。** 本批七组落在 2016；博山炉三候选 slug 均为 `boshanlu`、无 2016 候选，取出版年最早的高丰 2004；清式家具因 2004-gaofeng 的 slug `qing-style-furniture` 与文件名精确一致，取高丰而非 2016（该组无 2016 候选）。

---

## 五、校验

| 门禁 | 结果 |
|---|---|
| `build_discovery_index.py` | total 5339；applied 127；needs_evidence 4875；rejected 337 |
| `audit_content_quality.py` | 155 个知识元，总发现 0 |
| `audit_repo.py` | 结构门禁健康 122/130；知识结构完整性 55/65；证据链完整性 55/55；Frontmatter 缺失 0；验证语义问题 0；Markdown 断链 0；证据引用 155/155；层级完整挂载 0/155 |
| `apply-plan` 指纹核对 | 9 行 create 逐行核对 sha256／bytes／lines，全部一致 |
| `pre_commit_check.py` | 通过；规则漂移 0 |
| `run_sync_closure.py --refresh-generated --full --check-generated` | 通过；19 步；250 tests + 16 subtests |
| `candidate-index.jsonl` 指纹 | 应用前 `sha256:ca905391…`／7,156,734 B；应用后 `sha256:f5b244f4…`／7,156,926 B；行数均 5,339，复核后重跑生成器与 sync closure 不变 |

`audit_repo.py` 的健康分仍为 **122/130**，层级完整挂载为 **0/155**（上批为 0/146）。这是 Theme/Topic 尚未 materialize 的系统性缺口，本批只新增 9 个挂在 Dimension 上的 KU，**未改善、也未声称改善**该分数。

---

## 六、剩余量

本批之后：

- `doc_count = 3` 层的 term 组由 **18 组 54 条**降为 **9 组 27 条**（本批关闭 9 组 27 条）。
- 剩余 9 组：丝绸之路（xdup-0112）、匠人营国（xdup-0116）、工业设计（xdup-0119）、幌子（xdup-0120）、干栏式建筑（xdup-0122）、木版年画（xdup-0127）、百工（xdup-0131）、纬锦（xdup-0135）、饕餮纹（xdup-0143）。
- `doc_count = 4` 层仍有 **8 组 32 条**开放；`doc_count = 5` 层的 term 组已全部处置。

下一批（批次 G）处理剩余 9 组，按类别为：建筑与工艺（干栏式建筑、纬锦、饕餮纹）、民俗与商业（幌子、木版年画、丝绸之路）、制度与概念（匠人营国、百工、工业设计）。其中饕餮纹建条前需检查 `publications/lvshi-chunqiu.md`、`publications/shanhai-jing.md` 等既有"尚未立条"类陈述是否需补 update。

---

## 七、边界

- 不 commit、不 push；只改工作树。
- 不新建分支或 worktree；只保留 `main`。
- `02-sources/` 与 `03基础书籍-md文档/` 只读。
- 未使用外部验证平台，未做图版或器物的视觉核对，未查考古发掘报告与服饰实物。
- `primary_theme` 与 `topic_memberships` 留空，Theme/Topic 尚未 materialize，记为研究债。
- 未写入正式 `relations`；跨条目共现只作非断言性叙述。
- 来源分歧（时代、起源、定义、形态、评价）一律保留，不做调和。
- 既有 KU（`terms/wadang.md`、`terms/ming-style-furniture.md`、`terms/buzi.md` 等）不在本批重写，本批新建条目未使其陈述失效，故无 update 行。
- 本批只覆盖前六册；Book 7 及以后未启动。
