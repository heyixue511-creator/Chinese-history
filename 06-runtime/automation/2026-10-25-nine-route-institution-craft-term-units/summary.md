# 术语批次 G — 通道、制度与工艺九组知识元写回

- 工作包：`06-runtime/automation/2026-10-25-nine-route-institution-craft-term-units/`
- 状态：`applied`
- 日期：2026-10-25
- 上一批：`2026-10-25-nine-object-dress-term-units/`

---

## 一、批次范围

本批处理通道、建筑、工艺、商业、制度与概念交叉的 **9 个同名组**、**27 个候选**，写入 **9 个知识元**，18 个同组重复候选转 `rejected`。另有赵农册的 1 条 `place` 候选（`cand-04-62`，丝绸之路）因类型误标转 `rejected`，其文本仍作为 `terms/sichou-zhilu.md` 的来源使用。同批修订 **2 个既有 publication 条目**中因新条建立而失效的陈述。

| 实体 | 组 | 写入文件 | sub_type | 来源数 | bytes | lines | after_sha256（前 12 位） |
|---|---|---|---|---|---|---|---|
| 丝绸之路 | xdup-0112 | `terms/sichou-zhilu.md` | trade_route | 5 | 13875 | 160 | `sha256:c244c94e909d` |
| 匠人营国 | xdup-0116 | `terms/jiangren-yingguo.md` | planning_doctrine | 3 | 11330 | 138 | `sha256:80d9568548b0` |
| 工业设计 | xdup-0119 | `terms/industrial-design.md` | design_discipline | 3 | 11944 | 135 | `sha256:f191580b4cae` |
| 幌子 | xdup-0120 | `terms/huangzi.md` | advertising_form | 4 | 17679 | 167 | `sha256:ccd6b880c3ad` |
| 干栏式建筑 | xdup-0122 | `terms/ganlan-shi-jianzhu.md` | building_type | 4 | 14129 | 149 | `sha256:7317e07e294c` |
| 木版年画 | xdup-0127 | `terms/muban-nianhua.md` | print_genre | 4 | 15827 | 174 | `sha256:ffd567f8295b` |
| 百工 | xdup-0131 | `terms/baigong.md` | craft_system | 4 | 16676 | 161 | `sha256:6ba4af9a30c3` |
| 纬锦 | xdup-0135 | `terms/weft-brocade.md` | textile_type | 4 | 13406 | 157 | `sha256:7a5fbcc155d1` |
| 饕餮纹 | xdup-0143 | `terms/taotie-motif.md` | decorative_motif | 4 | 18026 | 171 | `sha256:95c39aae26ab` |

来源范围仍为前六册，书籍 7 及以后不启动。9 条 KU 均为 `confidence=medium`、`consensus=tentative`、`evidence_status=source_backed`，未做外部验证。

**来源数与候选组册数不一致，必须在阅读时区分**：9 个组的 `doc_count` 都是 3，但高丰 2004 在丝绸之路、幌子、干栏式建筑、木版年画、百工、纬锦、饕餮纹七条中提供了候选组之外的实质文本，赵农在丝绸之路另提供海上通道、张骞与班超等文本，故 8 条 `source_count=4`、丝绸之路为 5。`source_count` 记的是文档数，不是独立来源数：夏燕靖 2009 与 2016 两版文字高度重合。

| 更新文件 | 触发新条 | before | after | 修改内容 |
|---|---|---|---|---|
| `publications/lvshi-chunqiu.md` | 饕餮纹 | 13464 B／142 行 | 13500 B／142 行 | “窃曲纹、饕餮纹、夔纹等纹样尚未立条”改为“窃曲纹、夔纹等尚未立条；饕餮纹已建立为 `terms/taotie-motif.md`” |
| `publications/dongjing-menghua-lu.md` | 幌子 | 9449 B／114 行 | 9480 B／114 行 | “幌子、瓦舍等词条尚未建立”改为“幌子已建立为 `terms/huangzi.md`；瓦舍等尚未建立” |

---

## 二、五处结构性判断

### 1. 丝绸之路只立一条 term，不另立 place

赵农册的 `cand-04-62` 标题同为“丝绸之路”，但 `unit_type` 标为 `place`，slug 为 `silk-road`，未进入 term 组 `xdup-0112`。本批判定其语义是跨区域贸易通道概念，不是可定点的地方条目，转 `rejected` 并指向 `terms/sichou-zhilu.md`；该候选的 doc 仍作为 KU 的第五个来源。故 `source_count=5`，而候选组 `doc_count=3`。

### 2. 工业设计按“门类术语”建条，不把工业设计与艺术设计合并

`sub_type` 取 `design_discipline`。夏燕靖两版给的是“在有序与无序之间，在科技与艺术之间进行的交叉设计活动”，核心是批量生产的工业产品；李立新给的是对“工业设计”命名的批评，主张以“艺术设计／设计艺术”限定艺术性造物。两者不是同一层定义，KU 并列“活动定义”与“学科命名批评”，不把两个词当同义词。`academic_translation_status` 取 `established`，因李立新明确给出 Industrial Design；其余 8 条为 `provisional`。

### 3. 干栏式建筑只写类型层，与河姆渡既有条目分工

`places/hemudu-site.md` 与 `terms/hemudu-culture.md` 已记部分干栏内容。本批新建 `terms/ganlan-shi-jianzhu.md`，只取类型层定义、地域分布、构造组型与册际分歧，并在 `hierarchy_scope_note` 与“相关知识元”中说明分工，未改写既有条目，也未把河姆渡遗址或河姆渡文化并入本条。

### 4. 两条 update 只修失效陈述，不改实体内容

全批检查了可能因新条而失效的既有条目，只有 `publications/lvshi-chunqiu.md`（饕餮纹）与 `publications/dongjing-menghua-lu.md`（幌子）两处需要修订。`publications/kaogongji.md`、`persons/han-fei-zi.md`、`publications/shanhai-jing.md`、`persons/yuwen-kai.md` 等未出现“尚未立条／尚未建立”类失效陈述，故不写 update。

### 5. 维度分工按“概念的主功能”定，不按出现册数定

丝绸之路归 D（通道与贸易制度）／E、B；匠人营国归 B（营建）／D；工业设计归 D（学科与教育）／B、E；幌子归 C（视觉传达）／D、B；干栏式建筑归 B；木版年画归 C（印刷视觉）／B、D；百工归 D（制度）／B；纬锦归 B；饕餮纹归 B（造物装饰）／C。九条都不写正式 `relations`，跨条目共现只作非断言性叙述。

---

## 三、本批最重要的语义发现

### 1. 丝绸之路在五册中不是同一条路

- **组内三册**只覆盖陆上通道，终点作“地中海东岸”一线；**赵农**另记海上丝绸之路、陶瓷之路、“长安—罗马”、张骞两次出使、班超 73 年与西南通道；**高丰**补“通过丝绸之路，使中国以‘丝国’而驰名世界”。
- 终点有地中海东岸、罗马、红海、西域诸说；性质有官营外销、赏赐、商品交流诸说；海上路线是否属“丝绸之路”也未统一。KU 并列，不把陆上单线定义扩写为唯一定义。

### 2. 工业设计的“建筑外延”与“批量产品核心”互相拉扯

夏燕靖把“建筑物及其内外装饰”列入工业设计举例，同段又把核心定为“批量生产的工业产品”。建筑通常不是批量产品，来源未解释这一列举与定义的张力。李立新则从另一侧指出“工业设计”容易把工业布局、工厂管理乃至传统造物排除在外。两条批评方向相反，不能合并为“定义不统一”一句。

### 3. 幌子的构成与最早形态，四册给出四种起点

- **高丰**：“招幌”是招牌与幌子的合称，幌子系于酒旗源流；**赵农**把墙面单字也纳入幌子，并记宋称“望子”；**夏燕靖**称幌子“土生土长”，2016 又以近代黄旗为幌子。
- 最早形态有春秋酒旗、酒店幌子、实物广告三说；2016 同册既有“望子”又有“黄旗幌子”，册内未统一。KU 并列，不裁断哪种是“最早”。

### 4. 饕餮纹的定名是两层，不是一次命名

- 一层是《吕氏春秋·先识览》“周鼎著饕餮，有首无身”的文本记载；另一层是北宋金石学把这类纹样命名为“饕餮纹”。两层的时代与命名主体不同，不能压成一句“最早出自《吕氏春秋》”。
- 称名另有“兽面纹”一说；功能有戒贪、符号、通神、祭祀牺牲诸说；分期自商早期延至战国。高丰册“饕殄纹”为异文，照录不改。

### 5. 纬锦的出现时间与织法，三套描述不能互相翻译

- 出现时间：夏燕靖两版作“南北朝后”，高丰作“唐代新创造”，田自秉只把纬锦与唐锦对应，未给起点。
- 织法：夏燕靖作“两组纬线＋一组经线”，田自秉作“二层或三层经线夹纬、经畦纹组织”，高丰作“多重多色纬线起花”而不给组数。三者不是详略关系，KU 不代作纺织学裁定。
- 另有两处原文疑点：夏燕靖纹样清单“对称纹”重复；高丰“晕绸锦”与田自秉“晕絰”是否同物待核。

### 6. 干栏式建筑的“最早”是三种不同的竞赛

高丰称“最早的干栏式建筑”，夏燕靖称河姆渡“世界上最早的木构建筑”；构造定位又有穿斗式组型、南方基本风格、木构架雏形三说。2016 知识链接以“良渚文化区”起句却引河姆渡，册内不一致。KU 并列三种“最早”，不把“干栏式”与“木构建筑”当同一层级。

其余较轻的分歧也已写入正文与 `source_variance_notes`：匠人营国的“营建师／制度”二义与“前朝后市／面朝后市”、木版年画的产地名单与“短版／饱版／饅版”、百工的 30／31 工种算术矛盾与“商族／商旅”、工业设计的 2009“现代艺术设计”对 2016“现代设计”。

---

## 四、canonical 映射

| 组 | 实体 | canonical 候选 | 并入成员 | KU |
|---|---|---|---|---|
| xdup-0112 | 丝绸之路 | 夏燕靖 2016 `cand-03-111` | 夏燕靖 2009 `cand-03-21`、田自秉 `cand-06-43`；赵农 `cand-04-62` 另转 rejected | `terms/sichou-zhilu.md` |
| xdup-0116 | 匠人营国 | 夏燕靖 2016 `cand-03-24` | 夏燕靖 2009 `cand-02-49`、赵农 `cand-03-125` | `terms/jiangren-yingguo.md` |
| xdup-0119 | 工业设计 | 夏燕靖 2016 `cand-10-09` | 夏燕靖 2009 `cand-06-49`、李立新 `cand-01-06` | `terms/industrial-design.md` |
| xdup-0120 | 幌子 | 夏燕靖 2016 `cand-06-35` | 夏燕靖 2009 `cand-04-109`、赵农 `cand-10-45` | `terms/huangzi.md` |
| xdup-0122 | 干栏式建筑 | 夏燕靖 2016 `cand-01-70` | 夏燕靖 2009 `cand-01-47`、赵农 `cand-01-24` | `terms/ganlan-shi-jianzhu.md` |
| xdup-0127 | 木版年画 | 夏燕靖 2016 `cand-08-119` | 夏燕靖 2009 `cand-06-78`、赵农 `cand-10-115` | `terms/muban-nianhua.md` |
| xdup-0131 | 百工 | 夏燕靖 2016 `cand-03-69` | 赵农 `cand-02-31`、李立新 `cand-02-52` | `terms/baigong.md` |
| xdup-0135 | 纬锦 | 夏燕靖 2009 `cand-04-34` | 田自秉 `cand-08-53`、夏燕靖 2016 `cand-05-37` | `terms/weft-brocade.md` |
| xdup-0143 | 饕餮纹 | 夏燕靖 2016 `cand-02-81` | 赵农 `cand-03-38`、田自秉 `cand-03-34` | `terms/taotie-motif.md` |

canonical 选择规则：**优先选 `proposed_slug` 与最终文件名一致的候选；多个一致时取 2016 夏燕靖升级版候选；无 2016 且多条一致时取出版年最早者。** 本批八组落在 2016；纬锦组 2016 候选 slug 为 `weijin`，与文件名不一致，2009 夏燕靖与田自秉均为 `weft-brocade`，取出版年最早的 2009 夏燕靖。赵农 `cand-04-62` 虽被语义复读使用，因类型为 `place` 不进入 canonical 竞争。

---

## 五、校验

| 门禁 | 结果 |
|---|---|
| `build_discovery_index.py` | total 5339；applied 136；needs_evidence 4847；rejected 356 |
| `audit_content_quality.py` | 164 个知识元，总发现 0 |
| `audit_repo.py` | 结构门禁健康 122/130；知识结构完整性 55/65；证据链完整性 55/55；Frontmatter 缺失 0；验证语义问题 0；Markdown 断链 0；证据引用 164/164；层级完整挂载 0/164 |
| `apply-plan` 指纹核对 | 11 行（9 create + 2 update）逐行核对 sha256／bytes／lines，全部一致 |
| `pre_commit_check.py` | 通过；规则漂移 0（首次因 runtime index 快照陈旧失败，重建后通过） |
| `run_sync_closure.py --refresh-generated --full --check-generated` | 通过；19 步；250 tests + 16 subtests |
| `candidate-index.jsonl` 指纹 | 应用前 `sha256:f5b244f4…`／7,156,926 B；应用后 `sha256:1616b071…`／7,162,436 B；行数均 5,339，复核后重跑生成器与 sync closure 不变 |

`audit_repo.py` 的健康分仍为 **122/130**，层级完整挂载为 **0/164**（上批为 0/155）。这是 Theme/Topic 尚未 materialize 的系统性缺口，本批只新增 9 个挂在 Dimension 上的 KU，**未改善、也未声称改善**该分数。

---

## 六、剩余量

本批之后：

- `doc_count = 3` 层的 term 组由 **9 组 27 条**降为 **0 组 0 条**。批次 F 留下的九组全部关闭。
- `doc_count >= 3` 的开放 term 组只剩 `doc_count = 4` 的 **8 组 32 条**：仰韶文化（xdup-0043）、六齐（xdup-0044）、原始青瓷（xdup-0045）、尖底瓶（xdup-0046）、带钩（xdup-0047）、河姆渡文化（xdup-0051）、瓦当（xdup-0053）、龙山文化（xdup-0061）。
- 其中瓦当、河姆渡文化已有既有 KU（`terms/wadang.md`、`terms/hemudu-culture.md`），下一批须先做复用判断，不能盲目新建；其余各组也须先查是否已有同实体条目。
- `doc_count = 2` 仍有 **134 组 269 条**开放，`doc_count = 1` 有 **3 组 6 条**开放。这些是较低召回强度的组，本批未处理。
- 本批只覆盖前六册；Book 7 及以后未启动。

---

## 七、边界

- 不 commit、不 push；只改工作树。
- 不新建分支或 worktree；只保留 `main`。
- `02-sources/` 与 `03基础书籍-md文档/` 只读，未改写、未删除。
- 未使用外部验证平台，未做图版、器物或考古报告的视觉与实物核对。
- `primary_theme` 与 `topic_memberships` 留空，Theme/Topic 尚未 materialize，记为研究债。
- 未写入正式 `relations`；跨条目共现只作非断言性叙述。
- 来源分歧（定义、时代、构造、名称、性质、评价）一律并列保留，不做调和。
- 2 条 update 只修正因新条建立而失效的“尚未立条／尚未建立”陈述，不改写既有条目的实体内容。
- 本批只覆盖前六册；Book 7 及以后未启动。
