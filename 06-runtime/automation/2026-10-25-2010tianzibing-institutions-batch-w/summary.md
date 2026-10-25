# 田自秉《中国工艺美术史（修订本）》2010 册机构候选批次（四）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2010tianzibing-institutions-batch-w/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 处理田自秉《中国工艺美术史（修订本）》（2010）institution 候选 8 个（源行号 L5023—L5723，解放区至中华人民共和国成立后），逐条回读原文并作语义裁决。
- 结果：6 个 `create`、1 个 `update`、1 个 `no_delta`、0 个 `rejected`；无候选并入其他条目。
- 8 个候选终态：applied 7、no_delta 1。
- KU 总数由 810 增至 816；institution 类型由 129 增至 135；events 仍为 115。
- 候选索引投影后：applied 919、needs_evidence 3,551、no_delta 57、rejected 812；总数 5,339。
- `02-sources/` 未改动；`03基础书籍-md文档/` 只读；本会话未执行 commit／push。

**范围说明**：2010 田自秉册 37 个 institution 候选至此全部处理完毕（批次 T、U、V、W：10＋10＋9＋8）。六册 institution 候选仅剩 2011 李立新 11 个。

**台账行数说明**：本批 ledger 为 **24 行**。7 个 applied 候选各走完整三行，7 × 3 = 21；1 个 no_delta 亦走完整三行，1 × 3 = 3；无 rejected 单行。

## 二、新建清单

| 文件 | 来源位置 | 主要增量 |
|---|---|---|
| institutions/jianhua-cichang.md | 田自秉 2010 L5023-L5025 | 建华瓷厂：关中衣食村设厂，生产质地较好的细瓷，有古铜、淡红、白、黑等色釉；产品除供应本区外，还运销陇东一带。来源未给创设年份、隶属、规模、产量与存续时间 |
| institutions/jiefangqu-diyige-taoci-yanjiusuo.md | 田自秉 2010 L5023-L5025 | 解放区第一个陶瓷研究所：河北磁州解放后立即恢复陶瓷生产，并成立该所，为发展解放区陶瓷工艺生产作出贡献。来源只以描述性称法指称，未给正式所名、年份、隶属、人员与研究内容，confidence 定为 low |
| institutions/yanan-bolichang.md | 田自秉 2010 L5027 | 延安玻璃厂：1941 年在延安白手起家创建第一个玻璃厂，克服原料调配与坩埚制作困难，生产杯、瓶、灯罩等日用器皿；原料含少量铁质，器皿微带绿色。来源未给正式厂名，条目名按地点与通称转写 |
| institutions/suzhou-cixiu-yanjiusuo.md | 田自秉 2010 L5138-L5142 | 苏州刺绣研究所：1957 年成立，专门从事苏绣传统技艺的研究和创新工作；同段记“猫”“金鱼”代表作、双面绣与乱针绣。段内指代不明，不把整段苏绣成就全部归所 |
| institutions/beijing-falangchang.md | 田自秉 2010 L5176-L5178 | 北京珐琅厂：景泰蓝仍以北京为生产中心，北京珐琅厂规模较大；北京工艺美术厂设景泰蓝车间，上海等地也发展生产。单句来源，confidence 定为 low |
| institutions/guangdong-nanhai-tengchang.md | 田自秉 2010 L5258 | 广东南海藤厂：解放后我国建立许多大型藤编工艺厂，该厂为其中之一。同段藤编工艺背景（合丝、沙丝、梨皮等）不专属该厂；单句来源，confidence 定为 low |

- 6 个新建全部为单源（田自秉 2010）、`version: 1`、`evidence_status: source_backed`、`consensus: tentative`。
- confidence：3 个 `medium`（建华瓷厂、延安玻璃厂、苏州刺绣研究所），3 个 `low`（解放区第一个陶瓷研究所、北京珐琅厂、广东南海藤厂）。
- 维度：6 个均以 B 为主导，兼 D 次要（工厂／研究所的建制与生产组织）。
- title 均为“中文（English）”双语形式。
- after 指纹（前 19 位）：jianhua-cichang `sha256:dabdcb4873cb…`（4,662 bytes／86 行）；jiefangqu-diyige-taoci-yanjiusuo `3472e09406dd…`（4,744／83）；yanan-bolichang `267a2d5f74ea…`（5,058／86）；suzhou-cixiu-yanjiusuo `ce1cfa4bd917…`（5,380／91）；beijing-falangchang `f0f17942f2bf…`（4,387／84）；guangdong-nanhai-tengchang `70b538812abd…`（4,580／84）。

## 三、update 清单

| 文件 | 来源位置 | 主要增量 | 批前 → 批后 |
|---|---|---|---|
| institutions/nanjing-yunjin-yanjiusuo.md | 田自秉 2010 L5103 | 候选“云锦研究所”与既有南京市云锦研究所对账，判同一机构 update：补南京解放前夕云锦仅剩几架陈旧织机、生产衰落，解放后恢复扩大生产并建所；研究所总结云锦艺人创作经验、研究整理传统图案、开展创新；补八句口诀、团花／缠枝／散花／满花／锦群五类图案组织（锦群又名天华锦，即古代八达晕演变）、雨花锦／双面锦／凹凸锦等新创生活用品及其用途与外销；补 alias“云锦研究所” | `e7a06c22a3e5…`（3,598／84）→ `2a5c6f0f21b3…`（6,579／104）；version 2、source_count 3 |

- 更新保留夏燕靖 2009、2016 两源，新增田自秉 2010 为第三源；`source_count` 2→3，`version` 1→2。
- 不另建 `yunjin-yanjiusuo.md` 重复条目。田自秉只称“云锦研究所”，未给正式全名与年份；合并依据是地点（南京）、名称与“解放后建立”的时期一致，来源未明说同指，名实张力已写入验证状态。
- 品种归属张力并存：夏燕靖记“双面锦”“凹凸锦”为 1954 年云锦研究工作组恢复的失传品种；田自秉记“雨花锦、双面锦、凹凸锦”为云锦工艺近年新创的生活用品。两说并录，不裁定。

## 四、no_delta 判定

| 候选 | 既有条目 | 判定理由 |
|---|---|---|
| 杭州国立艺术专科学校（cand-14-21） | `04-knowledge/units/institutions/hangzhou-guoli-yizhuan.md` | 既有条目 sources 已含田自秉 2010 L5723，正文完整照录“解放前在杭州国立艺术专科学校做学生、常去浙江省图书馆阅览《格古要论》《骨董琐记》”及作者自述的治学取向，并在描述与核心内容中讨论“杭州国立艺专／国立杭州艺术专科学校”名称差异。候选无新增语义，判 no_delta，不重复写回 |

- 该 no_delta 为完整三行：`needs_evidence → ready_for_review → approved → no_delta`；终态行 `decision.status: approved`，带 `target_ref` 指向既有条目。
- 不把 no_delta 记作 applied，也不新建重复条目。

## 五、rejected 判定

本批无 `rejected`。

## 六、本批的判断

1. **先对账再定动作**：`cand-13-81` 的候选名“云锦研究所”与既有 `nanjing-yunjin-yanjiusuo.md` 指称相近。回读既有条目后确认二者同为南京、同为解放后建立的云锦研究机构，故判 update 而非 create；若按候选名直接新建，会制造一个与既有条目并行的重复机构。
2. **候选内容已被既有条目完整覆盖时判 no_delta**：`cand-14-21` 的校名写法与既有条目的来源、正文完全对应，既有条目甚至已讨论校名差异；再写一次只会产生同义重复，故判 no_delta，并在 ledger 终态保留 `target_ref` 以便追溯。
3. **研究机构与窑口分记**：`cand-13-83` 是 1940 年代磁州解放后设立的陶瓷研究所，`places/cizhou-kiln.md` 是宋元磁州窑窑口与白地黑花传统；两者只共用地名，来源未说研究所即以古窑址为研究对象，不能互训，也不合并。
4. **描述性称法不补造成正式名**：田自秉只写“解放区第一个陶瓷研究所”，未给正式所名；本条以该描述作条目名，并在 `name_original` 与正文标明，不据“磁州”二字补造“磁州陶瓷研究所”一类正式名。延安玻璃厂同理：来源只称“第一个玻璃厂”，条目名按地点与通称转写，正文明确这是工作名而非来源所给厂名。
5. **段内指代不扩大归属**：苏州刺绣研究所一段在记所之后紧接着写“猫”“金鱼”、双面绣与乱针绣，但来源没有明说这些创作或发展都由该所完成；本条只把“专门从事苏绣传统技艺的研究和创新工作”归所，其余作为同段苏绣背景照录，并标注指代不明。
6. **单句来源保留低置信**：北京珐琅厂、广东南海藤厂各只有一句，厂名、地点与“规模较大／大型”的判断明确，但成立年份、隶属、人员、产品、产量与存续时间全缺；两条均判 create 而非 rejected，因来源确实给出了工厂实体与生产地位，但 confidence 定为 low。解放区第一个陶瓷研究所同样只有一句且无正式名，亦定 low。
7. **同段并置的厂、所不合并**：建华瓷厂、桥儿沟陶瓷厂、子长瓷窑、磁州陶瓷研究所同出“解放区的陶瓷生产”一段；北京珐琅厂与北京工艺美术厂景泰蓝车间、上海等地景泰蓝生产同出一句；广东南海藤厂与“许多大型藤编工艺厂”同出一句。本批只登记候选所指的单一实体，不把同段其他生产单位并入。
8. **工艺背景与工厂史料分开**：广东南海藤厂条把“合丝／沙丝／梨皮”的藤丝分类、编织品类与机械化生产标为同段工艺背景，不写成该厂独有流程；北京珐琅厂条 likewise 只登记厂名、地点与规模判断，不把景泰蓝七过程写成该厂工艺。
9. **多源只用于确有增补且能对账的条目**：本批唯一 update 的南京市云锦研究所新增田自秉为第三源，是因为田自秉提供了既有两版没有的建立背景、研究所工作、口诀、图案组织与新创用品；6 个新建在六册中没有第二处可资印证的直接记载，保持单源，不把背景性提及算作第二源。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：24 行；8 个候选；applied 7（各 3 行）、no_delta 1（3 行）；7 个 applied 终态行与 1 个 no_delta 终态行均带 `target_ref`。
- `apply-plan.jsonl`：7 行；create 6、update 1；create 的 `before` 为 null；update 的 `before` 与预期指纹一致；7/7 的 after 指纹、bytes、lines 与磁盘一致。
- `canonical-mapping.json`：7 条（create 6、update 1）；`merged_candidates` 全为空；与 apply-plan 的目标、动作、候选一一对应。
- 候选索引：5,339 行；批前 `sha256:0f317aa0…`（applied 912、needs_evidence 3,559、no_delta 56、rejected 812），批后 `sha256:d4acbebb…`（applied 919、needs_evidence 3,551、no_delta 57、rejected 812）；重建幂等。
- 内容质量审计：816 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 816/816 可解析，断链 0，类型覆盖 8/8，结构节点覆盖 0/4，层级挂载 0/816；institutions 135、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；816 个 KU 均未建立正式 relation。
- 规则漂移审计：0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过；pytest 250 项、16 subtests 通过（failures 0、errors 0、skipped 0）。
- Sync closure：`--refresh-generated --full` 运行 18/18 通过；另以 `--refresh-generated --check-generated --full` 复核，第 1—16 步完成，第 17 步因工作树未提交、10 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。10 个文件为：`04-knowledge/quality/translation-index.yml`、`05-outputs/index/index.md`、`05-outputs/knowledge-graph-data.js`、`05-outputs/knowledge-graph-data.json`、`06-runtime/automation/index.md`、`06-runtime/governance/governance-backlog.md`、`06-runtime/state/candidate-index.jsonl`、`06-runtime/state/current-health.json`、`06-runtime/state/discovery-manifest.json`、`06-runtime/state/generated-projections-manifest.json`。

## 八、边界与研究债

- 6 个新建全部为单源；1 个更新为三源。全部 `consensus: tentative`，验证层级未评定，图版未视觉核验。
- 具体缺项：建华瓷厂缺创设年份、隶属、创办人、资本、规模、工人数、窑炉数、产量、产品分配、存续时间与“建华”厂名来历；解放区第一个陶瓷研究所缺正式所名、成立年份、隶属、所址、所长与研究人员、研究项目、成果与存续时间；延安玻璃厂缺正式厂名、隶属、厂长与技术人员、工人数、炉窑数、产量、分配、销售与结束时间，以及原料配比、坩埚制法与烧成温度；苏州刺绣研究所缺隶属、所址、所长与研究人员、规模、经费、成果目录与存续时间，且“猫”“金鱼”、双面绣、乱针绣的归属不明；北京珐琅厂缺成立年份、厂址、隶属、所有制、职工数、产品品种、产量、销售与存续时间；广东南海藤厂缺成立年份、厂址、隶属、所有制、职工数、产品、产量、销售与存续时间；南京市云锦研究所仍缺所址、隶属细节、首任所长、人员编制与田自秉所记年份。
- 已并存未释的张力：田自秉“云锦研究所”与夏燕靖“南京市云锦研究所”的名实与系年；“双面锦／凹凸锦”是工作组恢复的失传品种还是云锦工艺近年新创的生活用品；田自秉“解放区第一个陶瓷研究所”的“第一个”比较范围；杭州艺专的校名写法差异（既有条目已记录）。
- 结构层仍为 0/4，层级完整挂载 0/816，正式 relation 0 条，Theme／Topic 均未实体化。
- 2010 田自秉 37 个 institution 候选已全部处理；六册 institution 候选剩 2011 李立新 11 个。
- 下一批（批次 X）转 2011 李立新《中国设计艺术史论》11 个 institution 候选；完成后六册 institution 候选清零，转入 place 等其他 unit 类型或 claim 流程。
- 本批临时脚本（`_tmp_institutionsw_emit.py`、`_tmp_institutionsw_verify.py`、`_tmp_institutionsw_finalize.py`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理；`_tmp_w_closure18.txt`、`_tmp_w_closure19.txt` 同批待清理。
