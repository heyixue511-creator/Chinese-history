# h33 批次摘要：B.5 史前功能陶器（B.5.7）

## 一、目标与范围

本批在 v1.12 所建 B.5「陶器、制陶工艺与陶瓷传统」下新建第 7 个 Topic：B.5.7「史前功能陶器：炊煮、蒸食、仿生与发声」，收 5 个陶器术语条目。

基线为 v1.23：21 Theme、62 Topic、472 membership、468 complete assignments、2102 个 KU 未挂载、relation index 6938。本批不动 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/`，不新建 Theme。

## 二、结构物化

### 新建 B.5.7「史前功能陶器：炊煮、蒸食、仿生与发声」

- `parent_theme: B.5`、`primary_dimension: B`，`research_question` 184 字，`date: 2026-10-29`。
- 支撑材料 5 个 KU，全部 `term`、全部 `term_anchor`：陶鬶、陶甑、陶埙、鱼鳍形足陶鼎、水鸟形陶壶。
- 以「受热—蒸汽—发声—仿生」四种功能组织材料，四者对应四种可指认（或不可指认）的结构：
  - 受热：陶鬶三条中空款足「扩大受热面积」，足肥大、颈高拔、流作鸟喙；田自秉给出大汶口→龙山完整演变链（圆腹小颈→腹扁口前移→实足变空足、绳纽把手→「冲天流」），是六册唯一把仿生与功能写成同一过程的器形链。
  - 蒸汽：陶甑穿孔底把「加热」与「盛放」分开，完全无仿生成分，来源评价落在「煮食向蒸食的过渡」。
  - 发声：陶埙以音孔仿鸟鸣以诱捕，仿「声」不仿「形」；同段陶号角「模仿牛角的造型和声音」，两件并列可见仿形／仿声／形声双仿三路。
  - 仿生：良渚两器只有「具有代表性」「摹拟自然形态」的类型判断，无尺寸、足部形态与出土单位，列为「仿生可辨、功能不可辨」一档。
- 三条判断：其一，功能结构的可指认程度决定记载方式（可数结构越多，记载越具体）；其二，「像」与「用」的关系有三档——同向、无关、仿生可辨而功能不可辨，陶埙另立「仿声」一档；其三，「功能陶器」指有可指认功能结构的陶器，不是一切史前陶器。
- 10 条未解决问题，含「功能陶器」边界无法由来源证成、陶鬶演变链无遗址与层位、陶甑孔径孔数孔位全无、陶埙测音数据与「诱捕」功能无实证、良渚两器尺寸与出土单位全无等。

### 既有结构更新

- Theme `b5-taoqi-gongyi-yu-taoxi-chuantong.md`：tags 17→23；核心问题新增第四条线索（「用」如何变成「形」，四种功能解释）；纳入清单补「史前功能陶器」一组；下属 Topic 6→7，并新增 B.5.7 与 B.5.1／B.5.3 的分工说明；实证 82→87 KU；后续 Topic 列表删去已物化的「史前功能陶器」、增「青铜器形序列（鼎、壶、豆、簋、斝、甗、鬲）」；未解决问题 +5 条。
- `hierarchy/index.md` v1.23→v1.24；`archive/v1.23.md` 为改动前原样副本（44,402 字节，逐字节一致）。
- `themes/README.md`、`topics/README.md`、`dimension-candidates.md` 同步。

## 三、5 个 KU 的挂载

| KU | 类型 | role | Topic | version |
|---|---|---|---|---|
| `terms/tao-gui.md` | term | `term_anchor` | B.5.7 | 2→3 |
| `terms/tao-zeng.md` | term | `term_anchor` | B.5.7 | 1→2 |
| `terms/taoxun.md` | term | `term_anchor` | B.5.7 | 1→2 |
| `terms/yuqixingzu-taoding.md` | term | `term_anchor` | B.5.7 | 1→2 |
| `terms/shuiniaoxing-taohu.md` | term | `term_anchor` | B.5.7 | 1→2 |

每个 KU 均写入 `primary_theme: B.5`、`secondary_themes: []`、`role_in_theme: term_anchor`、一条 `topic_memberships`（含 `primary: true` 与 `scope_note`），`hierarchy_scope_note` 与 `scope_note` 逐字相同并保持为 frontmatter 末字段；正文「在层级体系中的位置」替换为六行段；`version` +1、`updated: 2026-10-29`。

scope 摘要：陶鬶「龙山文化炊煮器；空足受热与鸟喙流合一，大汶口至龙山有完整演变链」；陶甑「河姆渡文化蒸食器；穿孔底把加热与盛放分离，功能与仿生无关」；陶埙「半坡与河姆渡的陶制吹奏器；仿声诱捕，与陶号角的形声双仿对照」；鱼鳍形足陶鼎「良渚文化陶鼎；鱼鳍足可辨、功能不可辨，只有类型判断」；水鸟形陶壶「良渚文化陶壶；水鸟造型可辨、功能不可辨，与鱼鳍形足陶鼎同段并提」。

## 四、边界处置

| 对象 | 处置 | 理由 |
|---|---|---|
| 山东莒县陶尊 | 不挂载 | `primary_dimension` 为 C 的刻画符号与日出崇拜条目，来源只有一句符号释读且正文符号在 Markdown 中缺失，无功能结构可指认；若日后建立 C 维度符号与文字 Topic 应优先复核 |
| 甗（`terms/yan-steamer.md`） | 不挂载 | 青铜煮食器，只在陶甑的「蒸」功能处引用其甑鬲组合原理 |
| 釜、鬲、甑（`terms/fu-li-zeng.md`） | 不挂载 | 三器合条跨出单器范围，组合描述只作引用 |
| 鼎、壶、豆、簋、斝等青铜器形 | 不挂载 | 形制序列归未来青铜器 Topic；本 Topic 只取陶质的鱼鳍形足陶鼎与水鸟形陶壶 |
| 陶号角 | 不单独立目 | 只作陶埙条「仿声」的旁证 |
| 陶鼓、陶铃等陶制乐器 | 暂不创建 | 六册材料不足，本 Topic 只取陶埙一件 |
| 良渚两器 | 同段不互证 | 同出夏燕靖 2016 同一段同一判断，不构成两条独立证据 |

## 五、执行与验证

- `scripts/hierarchy_stress_test.py` → `hierarchy_version: v1.24`、themes 21、topics 63、topic_memberships 477、complete_assignments 473、incomplete_assignments 2097、themes_without_topics 0、cross_dimension_topics []、apply_permitted false。
- `scripts/build_relation_index.py` → 6948 条（explicit 5998、inferred_by_rule 950、migrated_from_related 0）。
- `scripts/write_current_health.py` → v1.24、complete 473、missing 2097、relation 6948、isolated 1283、structural_health 130、knowledge_structure_quality 56/65。
- `apply-plan.jsonl` 12 行（1 `structure_node_create`、5 `hierarchy_mount`、6 `structure_index_update`），12/12 哈希与磁盘一致。
- 本批 12 个 authored 文件写入后逐条校验：Topic 的 frontmatter 字段与七节结构、5 个 KU 的层级字段块与末键、theme 与三个索引的计数行。

## 六、指标变化

| 指标 | v1.23 基线 | v1.24 结果 |
|---|---|---|
| Theme | 21 | 21 |
| Topic | 62 | 63 |
| Topic membership | 472 | 477 |
| 完成五级挂载 KU | 468 | 473 |
| 未挂载 KU | 2102 | 2097 |
| relation index | 6938 | 6948 |
| member_of | 940 | 950 |
| 隔离单元 | 1283 | 1283 |
| structural_health | 130 | 130 |
| knowledge_structure_quality | 56/65 | 56/65 |
| 库存 KU | 2570 | 2570 |

B.5 累计挂载 87 个 KU，七个 Topic 覆盖成形烧成、陶系分区、三重分化、低温釉、胎面、构件与功能七点。

## 七、语义边界

1. 「功能陶器」是本库的分析框架，不是来源分类：六册从未使用这一名称，本 Topic 的定义（有可指认的功能结构）用于排除陶尊与纯装饰陶器。
2. 「像」与「用」三档不可升格为演化序列：陶鬶同向、陶甑无关、良渚两器不可辨，三档是并存关系，无早晚。
3. 陶鬶演变链的「既是逐渐走向形象化，又不断提高实用功能」是田自秉的判断，本库照录，不据此推出史前陶器普遍规律。
4. 陶埙的「模仿鸟鸣」「诱捕禽兽」是来源的功能解释，无测音、民族志或实验证据；本 Topic 只记其「仿声」方向，不写声学结论。
5. 良渚两器同段并提，不互证；本 Topic 不把「摹拟自然形态」的总判断当作功能证据。
6. 陶尊不挂载是可复核边界，不是永久排除：其所属 C 维度若建立符号与文字 Topic，应优先复核。

## 八、生成态与门禁

- `hierarchy/index.md` 升版并归档 `archive/v1.23.md`（44,402 字节，与改动前逐字节一致，`sha256:23ffbece…`）。
- `relation-index.yml`、`current-health.json`、`governance-backlog.md`、`generated-projections-manifest.json` 由刷新步骤重建，不在 apply-plan 内。
- `run_sync_closure.py --refresh-generated --full` → **18/18 通过**（`sync closure passed`，`250 passed, 16 subtests passed`，64.74s）。
- `run_sync_closure.py --refresh-generated --check-generated` → **[17/17] FAILED (exit=1)**，原因为本批未提交，生成态快照与工作区不一致；这是提交前门禁的预期结果，不是失败信号。提交后须重跑至通过。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动。
- `apply-plan.jsonl` 12/12 哈希在闭包后复核仍与磁盘一致。

## 九、未决事项与下一跳

- 未决：「功能陶器」边界无法由来源证成；陶鬶讹字与器形关系；陶鬶演变链无层位；陶甑孔径孔数孔位；陶埙测音与诱捕功能无实证；良渚两器尺寸与出土单位全无；青铜器形序列与制陶生产组织两组候选未物化。
- 下一跳候选：青铜器形序列 Topic（鼎、壶、豆、簋、斝、甗、鬲）；制陶生产组织 Topic（商代王室作坊、周代职官、秦汉官营陶窑、郑韩故城）；玻璃材料 Theme；重复候选 reconcile 4 组；图注单条待核 12 条；存量债务（未挂载 2097、单源 1919、tentative 2570、低置信 496、隔离 1283）。
- 本批不 commit、不 push；commit 与 push 须用户当次明确授权。
