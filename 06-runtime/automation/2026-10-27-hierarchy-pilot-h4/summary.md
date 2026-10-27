# h4 批次摘要：T4 书籍装帧、印刷与出版的 C.2 物化

日期：2026-10-27
批次包：`06-runtime/automation/2026-10-27-hierarchy-pilot-h4`
范围：`04-knowledge/structure/` 第四批 Theme/Topic materialize 与 27 个知识元的五级字段挂载
入口：`build-hierarchy`、`hierarchy-field.md`、`晚清至民国设计史主题归并报告_2026-10-26.md`

## 1. 目标与范围

本批处理晚清至民国主题归并报告的 T4「书籍装帧、印刷与出版」。候选索引中的 C 维度条目经逐条复读后，保留 27 条以书籍生产、封面设计、书籍形态与阅读文化为主旨的晚清民国条目；改革开放后的书籍装帧、印刷技术与出版机构条目不并入。

本批 materialize 1 个 `pilot` Theme 与 3 个 `pilot` Topic，并为 27 个已逐对象复读的 KU 写入 `primary_theme`、`secondary_themes`、`role_in_theme`、`topic_memberships` 与修订后的 `hierarchy_scope_note`。27 个 KU 均为单一主挂载，无次挂载；共形成 27 条新 membership。

本批不新增 KU、claim、candidate 或来源字节，不改写 `03基础书籍-md文档/` 与 `02-sources/`，不执行 commit 或 push。

## 2. 结构物化

### 2.1 Theme

| 代码 | 标题 | 主维度 | 次维度 | Topic 数 |
|---|---|---|---|---:|
| `C.2` | 书籍装帧、印刷与出版 | C | B、D、E | 3 |

C.2 声明 `node_type: theme`、唯一 `theme_code`、`primary_domain: chinese-design-history` 与 `primary_dimension: C`。本批候选的主维度均为 C，因此不按主维度拆分；Theme code 前缀与主维度一致，不触发 `apply_topic_memberships.py` 的强制改写规则。

C.2 的边界：

- 纳入石印、铅印、铜版与照相制版，清末官办书局与点石斋石印局，民国书装家群体，以及《北平笺谱》《点石斋画报》《坟》《冯小青》《呐喊》《彷徨》《万象》《新青年》等书籍／期刊样本。
- 排除月份牌、报纸广告、书刊广告与机构标识，留给 C.1；《生活周刊》的内容是书刊与商品广告，应归 C.1.2，本批不挂 C.2。
- 排除商务印书馆与伊文思图书公司：两条目的实际内容分别是 1920 年广告画家练习生培养与 1926 年打字机霓虹灯／吊灯广告，不因机构名并入书籍出版。
- 排除短版套印与丝网印刷：前者为明代创造、清代盛行，后者只有“现代”一句且为低置信，均不足以支撑晚清民国书籍生产主题。
- 排除 1949 年后的书籍装帧、印刷技术与出版机构。

### 2.2 Topic

| 代码 | 标题 | 父 Theme | 主维度 | 成员数 |
|---|---|---|---|---:|
| `C.2.1` | 石印、铅印技术与出版机构 | C.2 | C | 9 |
| `C.2.2` | 书装家群体与封面设计 | C.2 | C | 10 |
| `C.2.3` | 书籍形态与阅读文化 | C.2 | C | 8 |

每个 Topic 均声明 `node_type: topic`、`primary_domain`、`primary_dimension`、`parent_theme` 与 `secondary_themes`，并在正文列出显式 `../../units/...` 成员链接及 role。三个 Topic 的 `primary_dimension` 与父 Theme 一致；`cross_dimension_topics` 为 `[]`。

三个 Topic 的 `secondary_themes` 均为 `[]`：B.2 为织绣与服装工艺、D.2 为服饰制度与近代生活、E 类 Theme 尚未 materialize，均不承接书籍生产或书装作者群体。故不把“B/D/E 次维度存在”误写成“已有对应次 Theme”。

## 3. 27 个 KU 与 27 条 membership

### 3.1 按 Topic 分配

- C.2.1 石印、铅印技术与出版机构（9）：
  - `institutions/chengdu-cungu-shuju`、`institutions/dian-shizhai`、`institutions/hunan-sixian-shuju`、`institutions/jinling-shuju`、`institutions/zhejiang-shuju` — `key_institution`；
  - `procedures/qianzi-yinshua`、`procedures/shiyin-ben`、`procedures/tongban-yinshua`、`procedures/zhaoxiang-zhiban` — `procedure`。
- C.2.2 书装家群体与封面设计（10）：
  - `persons/lu-xun`、`persons/chen-zhifo`、`persons/feng-zikai`、`persons/tao-yuanqing`、`persons/qian-junfou`、`persons/sun-fuxi`、`persons/si-tuqiao`、`persons/wen-yiduo`、`persons/ye-lingfeng`、`persons/zhang-guang-yu` — 均为 `key_person`。
- C.2.3 书籍形态与阅读文化（8）：
  - `publications/beiping-jianpu`、`publications/dianshizhai-huabao`、`publications/fen`、`publications/feng-xiaoqing`、`publications/nahan`、`publications/panghuang`、`publications/wanxiang`、`publications/xin-qingnian` — 均为 `representative_work`。

### 3.2 字段写回规则

- 保留原 `primary_domain`、`primary_dimension` 与 `secondary_dimensions`，不因 Theme code 前缀强制改写维度。
- `primary_theme` 统一为 `C.2`；`secondary_themes` 统一为 `[]`，因为本批没有与 B/D/E 次维度匹配的已物化 Theme。`[]` 不表示次维度不存在，原 `secondary_dimensions` 与 `hierarchy_scope_note` 保留该信息。
- 每个 KU 一个 `topic_memberships`，含 `topic`、`role`、`primary: true` 与逐对象 `scope_note`；本批无次挂载。
- `hierarchy_scope_note` 改写为 v0.5 表述：说明 C.2 的主 Theme、次维度为何未挂 Theme，并标注“本次为首批 Topic 挂载”。
- 27 个文件的 `updated` 统一为 `2026-10-27`；`last_verified` 不变，因为本批不重新做事实核验。
- 五个出版物文件原为空的 `secondary_dimensions:`，本批规范为 `secondary_dimensions: []`：`fen`、`feng-xiaoqing`、`nahan`、`panghuang`、`wanxiang`；不改变其维度语义。

### 3.3 语义判断记录

- C.2.1 采用“技术—机构”合一的 Topic：石印、铅印、铜版、照相制版四种工艺与成都存古书局、点石斋石印局、湖南思贤书局、金陵书局、浙江书局五家机构共同回答书籍如何被印制与发行。点石斋既是机构又是《点石斋画报》的出版者，本批只在 C.2.1 挂机构条目，画报样本挂 C.2.3，不重复计数同一 KU。
- C.2.2 以鲁迅为提携者与设计实践者，连同陈之佛、丰子恺、陶元庆、钱君匋、孙福熙、司徒乔、闻一多、叶灵凤、张光宇，构成“作者—题字—插图—版式”的书装家群体。部分人物只有列名或单句评语，证据密度不均，仍按 `key_person` 挂载并在 `scope_note` 标明首批边界。
- C.2.3 以 8 个书籍／期刊样本回答新式印刷与封面设计如何改变开本、版式、图版与阅读方式；《北平笺谱》兼有传统笺纸谱录与现代出版合作性质，按“书籍形态”样本处理，不另立工艺 Theme。
- `qian-juntao` 与 `qian-junfou` 极可能是同一人的异写重复；本批只挂 `qian-junfou`，`qian-juntao` 保留未动，不双挂、不合并，记为研究债。
- `shenghuo-weekly` 的实际内容是书刊广告与商品广告，应归 C.1.2；本批不挂 C.2，留待 C.1 回填。
- `shangwu-yinshuguan` 与 `yiwensi-tushu-gongsi` 虽为出版／图书机构名，但条目内容是广告画家培养与打字机广告，故不并入 C.2；不据机构名推断书籍出版业务。
- `duanban-taoyin` 属明代创造、清代盛行，`siwang-yinsha` 只有“现代”一句且 low confidence；两者均不并入 C.2，避免把跨时段工艺或孤证写成晚清民国书籍生产证据。
- 1949 年后的书籍装帧、印刷技术与出版机构不并入 C.2；它们仍留在候选索引，等待后续 Theme。

## 4. 执行与验证

- 写回前逐文件读取 frontmatter，按对象替换层级段，未批量重写正文。
- 27 个 KU 与 4 个结构文件的结构化自检：YAML 解析通过，`primary_theme`、`primary_dimension`、`role_in_theme`、`topic_memberships`、Topic 目标存在性、`updated` 均无错误。
- `python scripts/hierarchy_stress_test.py`：
  - `hierarchy_version: v0.5`；
  - `themes: 6`，`themes_without_topics: 0`；
  - `topics: 14`，`topic_memberships: 90`；
  - `complete_assignments: 89`，`incomplete_assignments: 2481`；
  - `cross_dimension_topics: []`，`apply_permitted: false`。
- `python scripts/audit_content_quality.py`：总发现 0。
- `python scripts/audit_repo.py`：退出码 0；Markdown 断链 0；Frontmatter 缺失／格式错误 0；类型值不匹配 0；层级结构问题 0；同名跨类型组 5，消歧说明 10/10。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18/18 通过，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：36 行，`structure_node_create` 4、`hierarchy_mount` 27、`structure_index_update` 5；36/36 `after_sha256` 校验通过。

## 5. 指标变化

| 指标 | 批次前 | 批次后 |
|---|---:|---:|
| 层级版本 | v0.4 | v0.5 |
| Theme | 5 | 6 |
| Topic | 11 | 14 |
| Topic membership | 63 | 90 |
| 完整五级挂载 | 62 | 89 |
| 未完整挂载 | 2508 | 2481 |
| `structure_node_coverage` | 2/4 | 2/4 |
| relation index | 6123 | 6177 |
| `member_of` 关系 | 125 | 179 |
| 关系类型覆盖 | 3/67 | 3/67 |
| 隔离单元 | 1495 | 1476 |
| 结构健康 | 130/130 | 130/130 |
| 内容质量发现 | 0 | 0 |
| KU 总数 | 2570 | 2570 |
| claim registry | 1242 | 1242 |
| candidate index | 5339 | 5339 |
| translation index | 2178 | 2178 |

`member_of` 的 179 条 = 89 个已挂载 KU 的 89 条 Theme 关系 + 90 条 Topic 关系，由 `build_relation_index.py` 依据 `role_in_theme` 与 `topic_memberships` 生成，不是手工新增关系。

## 6. 语义边界

- 本批只证明 89 个 KU 已完成逐对象挂载，不证明 2570 个 KU 的层级已全量建立。
- C.2 为 `pilot` 状态，不是最终分类；T5 建筑／城市／室内、T6 设计教育／职业／机构、T7 传统工艺的近代命运仍未 materialize。
- `secondary_themes: []` 表示当前没有已物化的对应 Theme，不表示该维度不存在；原 `secondary_dimensions` 与 `hierarchy_scope_note` 保留该信息。
- C.1 与 C.2 是同一 C 维度内的媒介分工：C.1 解释“商品与机构如何被看见”，C.2 解释“书刊如何被制作、装帧与阅读”；两 Theme 不重复计数同一 KU。
- 隔离单元减少 19 个，只表示这些 KU 因结构成员关系不再完全孤立，不表示其证据密度提高。
- 书籍封面、插图与版式的视觉核验尚未完成；部分书装家条目只有列名或单句评语，证据密度不均。
- 证据层仍无 claim evidence；关系层仍以 claim↔KU 投影和结构成员关系为主。
- `knowledge_structure_quality` 为 55/65，其中 `hierarchy_assignment` 为 0；这是 2481 个 KU 尚未完整挂载的既有覆盖度信号，不是本批新增结构错误。结构门禁仍为 130/130。

## 7. 生成态与门禁

- `06-runtime/state/current-health.json`：结构健康 130/130；`structure_node_coverage` 为 `2/4`；`hierarchy_version` 为 `v0.5`；完整挂载 89，缺挂载 2481；隔离单元 1476。
- `06-runtime/governance/governance-backlog.md`：P0/P1/P2 均为 `No active items.`；研究债 4 项（单源 1919、tentative 2570、低置信 496、缺层级 2481）；`OPP-ISOLATED` 1476。
- `06-runtime/automation/index.md`：批次目录 206 → 207；文件 1096 → 1099（本包 manifest、apply-plan、summary）。
- 发布门禁 `python scripts/run_sync_closure.py --refresh-generated --check-generated` 在 `[17/17] check generated snapshots` 处以 `EXIT=1` 失败，因为生成态快照相对 HEAD 仍有未提交差异；状态为 `blocked_pending_commit`。
- 本批未执行 commit 或 push；外部状态变更仍待用户明确授权。

## 8. 未决事项与下一跳

- 2481 个 KU 仍缺 `primary_theme` 与 `topic_memberships`，按研究债保留。
- 晚清至民国报告的 T5 建筑／城市／室内、T6 设计教育／职业／机构、T7 传统工艺的近代命运仍待 materialize。
- E 维度（跨文化技术转移）仍无 Theme；旗袍、月份牌中的西式技法来源等条目继续暂缓。
- `qian-juntao` 与 `qian-junfou` 的身份重复待裁决；在裁决前不合并、不双挂。
- `shenghuo-weekly` 待回填 C.1.2；`shangwu-yinshuguan`、`yiwensi-tushu-gongsi`、`duanban-taoyin`、`siwang-yinsha` 待有新证据时复审是否进入 C.2。
- 书籍封面、插图与版式实物均未视觉核验；多数书装家条目只有列名，证据密度不均。
- 证据层仍无 claim evidence；关系层仍以 claim↔KU 投影和结构成员关系为主。
- commit/push 仅在用户明确授权后执行。
