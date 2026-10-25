# 术语批次 D — 陶瓷类九组知识元写回

- 工作包：`06-runtime/automation/2026-10-25-five-book-ceramic-term-units/`
- 状态：`applied`
- 日期：2026-10-25
- 上一批：`2026-10-25-three-book-work-units-c/`

---

## 一、批次范围

本批处理陶瓷类术语的 **10 个同名组**（9 个实体）、**31 个候选**，写入 **9 个知识元**，22 个候选转 `rejected`，并修补 **2 条**因新建青花瓷条目而失效的既有陈述。

| 实体 | 组 | 写入文件 | sub_type | 来源数 | bytes | lines | after_sha256（前 12 位） |
|---|---|---|---|---|---|---|---|
| 几何印纹陶 | xdup-0115 | `terms/geometric-stamped-pottery.md` | ceramic_type | 3 | 8937 | 117 | `sha256:95b97bc32bc9` |
| 几何印纹硬陶 | xdup-0114 | `terms/geometric-stamped-hard-pottery.md` | ceramic_type | 4 | 9403 | 123 | `sha256:b5ae9dde3b6c` |
| 暗纹陶 | xdup-0126 | `terms/dark-pattern-pottery.md` | ceramic_type | 3 | 7477 | 110 | `sha256:5ca4b54e835f` |
| 彩绘陶 | xdup-0123 | `terms/caihui-tao.md` | ceramic_type | 4 | 10627 | 123 | `sha256:3e0d68651c9f` |
| 釉下彩 | xdup-0138 | `terms/underglaze-color.md` | ceramic_decoration | 5 | 10502 | 130 | `sha256:417ed714815e` |
| 粉彩 | xdup-0133 | `terms/fencai.md` | ceramic_decoration | 4 | 8925 | 118 | `sha256:df0308797598` |
| 珐琅彩 | xdup-0130 | `terms/falangcai.md` | ceramic_decoration | 4 | 9498 | 129 | `sha256:265a9b07f966` |
| 青花瓷 | xdup-0141＋xdup-0142 | `terms/blue-and-white-porcelain.md` | ceramic_type | 5 | 18422 | 162 | `sha256:f313fa6c6fd5` |
| 黑瓷 | xdup-0146 | `terms/black-porcelain.md` | ceramic_type | 5 | 13285 | 144 | `sha256:bd084e4742a2` |

来源范围仍为前六册，书籍 7 及以后不启动。本批 9 个 KU 均为 `confidence=medium`、`consensus=tentative`、`evidence_status=source_backed`，未做外部验证。

---

## 二、三处结构性判断

### 1. 青花与青花瓷是同一实体的两个组

`xdup-0141`（青花，赵农／田自秉／夏燕靖 2016）与 `xdup-0142`（青花瓷，高丰／夏燕靖 2009／赵农）在语义上是同一实体，合并为 **1 个 KU、6 个候选、5 册来源**。赵农一册在两处各出一候选（`cand-11-033` 与 `cand-07-97`），**不重复计册**。canonical 取赵农 `cand-07-97`，因其 `proposed_slug` 与最终文件名 `blue-and-white-porcelain` 一致。

### 2. 几何印纹陶与几何印纹硬陶是上下位，不是重复

田自秉原文有"可以分为印纹软陶和印纹硬陶两种"，两者是同一个大类下的软、硬两类。本批写 **2 个 KU**，并在两条的"相关知识元"段互指；不按同名组做合并。这也是两条来源数不同的原因：软陶无高丰条目，硬陶另有高丰商周段。

### 3. 釉下彩由 procedure 改判 term

赵农候选 `2009-zhaonong-zhongguo-yishu-shejishi:cand-07-98` 原判 `procedure`。改判理由写在 KU 的**立条类型说明**段：

- 四册原文都把它当作"瓷器釉彩装饰的一种"（夏燕靖两版），是分类对象而非操作规程；
- 仓内先例 `terms/doucai.md` 以 `ceramic_decoration` 立在 term 目录；
- `procedures/` 收的是可执行步骤（如三彩施釉），釉下彩只有赵农一册给三步概述，其余四册均为分类描述。

该候选在台账中记 `rejected`（原候选记录不再单独写回），其证据已并入 `terms/underglaze-color.md`；`candidate-index.jsonl` 的 `unit_type` 原值未改——改判属写入判定，不属候选回填。

---

## 三、本批最重要的语义发现：彩绘陶的工序定义分成相反两组

- **田自秉、高丰**：彩绘陶是**在烧成的陶坯上画花**。田自秉并明确"在名称中加一绘字"以与彩陶区别："彩陶是在陶胎上画花后再进行烧制，而彩绘陶则是在烧成了的陶坯上画花，因而花纹易于脱落"。
- **夏燕靖 2009、2016**：彩绘陶"是在陶胎上绘出花纹后再进行烧制"——这正是田自秉给**彩陶**的工序。两版同段末句又把"彩绘陶"径直写作"彩陶"，文内自相矛盾。

按册数为 2 对 2，但**夏燕靖 2009 与 2016 是同一作者的先后版本，2016 该段与 2009 逐字相同，不构成独立佐证**；独立表述只有田自秉、高丰两家。KU 并列原话不裁定，`consensus` 仍为 `tentative`，未升级为 `disputed`——只做册内复读、未做外部验证时，不冒充已裁定。

同类但分量较轻的分歧还有：青花起源四说（唐／宋／元代流行／"未获澄清"）、釉下彩三国点彩的定性、粉彩起点措辞、珐琅彩定义对象（彩料／瓷器）、黑瓷德清釉是否纯黑。全部并列写入正文与 manifest 的 `source_variance_notes`。

---

## 四、canonical 映射

| 组 | 实体 | canonical 候选 | 并入成员 | KU |
|---|---|---|---|---|
| xdup-0115 | 几何印纹陶 | 夏燕靖 2016 `cand-01-49` | 夏燕靖 2009 `cand-01-38`、田自秉 `cand-02-03` | `terms/geometric-stamped-pottery.md` |
| xdup-0114 | 几何印纹硬陶 | 夏燕靖 2016 `cand-02-41` | 夏燕靖 2009 `cand-02-25`、田自秉 `cand-05-23` | `terms/geometric-stamped-hard-pottery.md` |
| xdup-0126 | 暗纹陶 | 夏燕靖 2016 `cand-02-76` | 夏燕靖 2009 `cand-02-22`、田自秉 `cand-05-21` | `terms/dark-pattern-pottery.md` |
| xdup-0123 | 彩绘陶 | 田自秉 `cand-05-22` | 夏燕靖 2009 `cand-02-23`、夏燕靖 2016 `cand-02-77` | `terms/caihui-tao.md` |
| xdup-0138 | 釉下彩 | 田自秉 `cand-08-38` | 夏燕靖 2009 `cand-05-82`、夏燕靖 2016 `cand-08-63`、赵农 `cand-07-98`（procedure） | `terms/underglaze-color.md` |
| xdup-0133 | 粉彩 | 夏燕靖 2016 `cand-08-68` | 赵农 `cand-11-042`、田自秉 `cand-12-01` | `terms/fencai.md` |
| xdup-0130 | 珐琅彩 | 夏燕靖 2016 `cand-08-67` | 赵农 `cand-11-043`、田自秉 `cand-12-07` | `terms/falangcai.md` |
| xdup-0141＋0142 | 青花瓷 | 赵农 `cand-07-97` | 高丰 `cand-05-04`、夏燕靖 2009 `cand-05-23`、赵农 `cand-11-033`、田自秉 `cand-10-58`、夏燕靖 2016 `cand-06-60` | `terms/blue-and-white-porcelain.md` |
| xdup-0146 | 黑瓷 | 夏燕靖 2016 `cand-04-40` | 夏燕靖 2009 `cand-03-72`、田自秉 `cand-07-47` | `terms/black-porcelain.md` |

canonical 选择规则：**优先选 `proposed_slug` 与最终文件名一致的候选；无一致者取 2016 夏燕靖升级版候选。** 例外是彩绘陶——2016 的 `proposed_slug` 作 `painted-pottery`，与既有 `terms/painted-pottery.md`（彩陶）冲突，故取 `caihui-tao` 一致的田自秉候选。

---

## 五、两条失效陈述的修补（update）

`terms/blue-and-white-porcelain.md` 建立后，两条既有 KU 的相关知识元段出现失效陈述：

| 文件 | 原句 | 改为 | before | after |
|---|---|---|---|---|
| `terms/doucai.md` | "青花、五彩尚未单独成 KU" | "青花已由同批 `terms/blue-and-white-porcelain.md` 立条，五彩尚未单独成 KU" | `sha256:40af4cfc5bf9`／11704 B／135 行 | `sha256:c635b7f30f84`／11759 B／135 行 |
| `terms/youlihong.md` | "青花、钧窑尚未单独成 KU" | "青花已由同批 `terms/blue-and-white-porcelain.md` 立条，钧窑尚未单独成 KU" | `sha256:aaacc6e09c2a`／12076 B／137 行 | `sha256:ee5750238488`／12131 B／137 行 |

两行 `candidate_id` 为 `null`，`before` 记修订前指纹，`note` 说明这是非候选驱动的文本修订；只替换失效分句，保留"五彩／钧窑尚未单独成 KU"的现存判断。

---

## 六、校验

| 门禁 | 结果 |
|---|---|
| `build_discovery_index.py` | total 5339；applied 112；needs_evidence 4920；rejected 307 |
| `audit_content_quality.py` | 140 个知识元，总发现 0 |
| `audit_repo.py` | 结构门禁健康 122/130；Frontmatter 缺失 0；验证语义问题 0；Markdown 断链 0；证据引用 140/140 |
| `apply-plan` 指纹核对 | 11 行（9 create + 2 update）逐行核对 sha256／bytes／lines，全部一致 |
| `pre_commit_check.py` | 通过；规则漂移 0 |
| `run_sync_closure.py --refresh-generated --full --check-generated` | 通过；19 步；250 tests + 16 subtests |
| `candidate-index.jsonl` 指纹 | `sha256:320eaa57…`／7,153,006 B；逐行比对确认仅 31 行（9 applied + 22 rejected）变化，其余 5,308 行不变 |

---

## 七、剩余量

本批之后：

- `doc_count = 3` 层的 term 组由 **34 组 102 条**降为 **24 组 72 条**（本批关闭 10 组 30 条）。
- `doc_count = 4` 层仍有 **8 组 32 条**开放。其中部分实体已有 KU（如 `terms/proto-porcelain.md`），按上一批 manifest 的明确边界"已由既有 KU 覆盖的组不回填候选"，其候选保持 `needs_evidence`；其余为尚未立条的文化与器物类术语。
- `doc_count = 5` 层的 term 组已全部处置。

下一批起继续处理 `doc_count = 3` 的剩余 24 组，先做考古学文化（大汶口、红山、良渚、马家窑、旧石器时代）与器物形制两类。

---

## 八、边界

- 不 commit、不 push；只改工作树。
- 不新建分支或 worktree；只保留 `main`。
- `02-sources/` 与 `03基础书籍-md文档/` 只读。
- 未使用外部验证平台，未做图版或器物的视觉核对。
- `primary_theme` 与 `topic_memberships` 留空，Theme/Topic 尚未 materialize，记为研究债。
- 未写入正式 `relations`；跨条目共现只作非断言性叙述。
- 邻近的作品、事件、地点、procedure 候选（鬼谷下山罐、2005 年拍卖、洛阳、青花烧造工艺、铜胎画珐琅等）保持 `needs_evidence`，不在本批处置。
