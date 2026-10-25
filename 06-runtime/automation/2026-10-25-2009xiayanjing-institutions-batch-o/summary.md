# 夏燕靖《中国设计史》2009 册机构候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009xiayanjing-institutions-batch-o/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 处理夏燕靖《中国设计史》（2009）institution 候选 5 个（源行号 L1405—L4824，秦汉至 1985 年），逐条回读原文并作语义裁决。
- 2 个判 `create`，新建 institution KU；3 个判 `no_delta`，落点为既有机构条目；无 `update`、无 `rejected`、无并入。
- 5 个候选终态：applied 2、no_delta 3。
- KU 总数由 754 增至 756；institution 类型由 73 增至 75。
- 候选索引投影后：applied 848、no_delta 55、rejected 807、needs_evidence 3,629；总数 5,339。
- `02-sources/` 未改动；`03基础书籍-md文档/` 只读；本会话未执行 commit／push。

**范围说明**：2009 夏燕靖册共有 5 个 institution 候选，本批一次处理完毕。六册 institution 候选共 142 个：2016 夏燕靖 39 个、2004 高丰 9 个、本批 2009 夏燕靖 5 个均已处理；剩余 89 个分布在 2009 赵农 41 个、2010 田自秉 37 个、2011 李立新 11 个。

**台账行数说明**：本批 ledger 为 **15 行**。5 个候选各走完整三行，其中 applied 2、no_delta 3；5×3 = 15。

## 二、新建清单

| 文件 | 来源位置 | 主要增量 |
|---|---|---|
| institutions/han-dai-guan-ying-sizhi-zuofang.md | 2009 L1405-L1416 | 汉代官营丝织作坊网络：自秦至汉丝织业生产技术与产量提升显著，缫丝工具和织机改进；官营作坊规模扩大，采用先进提花织机，生产锦绣绮罗；品种含素纱、绮、罗、锦、纨、纻、缣、缦、绢、绫、缟、绨、绣、毂等；引王充《论衡》“齐部世刺绣……襄邑俗织锦……”；汉时成都为蜀锦集散中心，长安设东、西织室，临淄、襄邑设服官，织工多达数千人；官作坊织物供皇室、赏赐与对外贸易；张骞通西域后开辟丝绸之路。未给各作坊设置年代、隶属、编制、作坊址、机台数、产量与产品分配比例 |
| institutions/quanguo-gaoxiao-gongye-sheji-xuehui.md | 2009 L4824 | 全国高校工业设计学会：1985 年 3 月 2—6 日在北京成立，同时召开第一次全国工业设计教育学术交流会。来源只有一句，未给发起院校、会员规模、章程、理事长与理事会、分支机构、挂靠单位、会址、刊物、会议论文、后续活动与存续状态；成立大会另见 `events/industrial-design-society-1985.md` |

- 2 个新建均 `source_count: 1`（仅 2009 夏燕靖一条来源）、`version: 1`、`evidence_status: source_backed`、`confidence: medium`、`consensus: tentative`。
- 维度：汉代官营丝织作坊为 D 主导兼 B；全国高校工业设计学会为 D 主导兼 A。
- after 指纹（前 12 位）：han-dai-guan-ying-sizhi-zuofang `6097d4069875…`（6,246 bytes／94 行）；quanguo-gaoxiao-gongye-sheji-xuehui `0e151fc5dddc…`（4,501／85）。

## 三、update 清单

本批无 `update`。5 个候选均落在 create、no_delta 两类。

## 四、no_delta 判定

| 候选 | 落点 | 判定依据 |
|---|---|---|
| cand-03-37 汉代官营漆器作坊 | institutions/han-dai-qiqi-zuofang-guan-yuan.md | 既有 KU 已据 2016 升级版覆盖 2009 L1516-L1518 的全部语义：秦代设官府管理的漆器作坊；汉代从中央到郡国设管理漆器生产的作坊官员；作坊分布于山东、河南、陕西、江苏、广东、广西；漆器成为牟利新兴商品；蜀郡、广汉郡金银饰与漆器最著名；金属铸器铭文记录制作地点、年代、工序、工官姓名；漆器工序 6—8 道；金银扣器价值为同类铜器 10 倍；并保留“金属铸器铭文”与漆器生产之间的文本张力 |
| cand-05-14 西夏刻字司 | institutions/kezisi.md | 既有 KU 已据 2016 升级版覆盖 2009 L2874 的全部语义：西夏朝廷设刻字司专印书籍，佛经最多，兼刻文学、法律、医术、日历、卜筮、咒文；西夏保存与宋同时的活字印本；推见活字印刷术西传桥梁作用 |
| cand-06-54 中央手工业管理局 | institutions/zhongyang-shougongye-guanliju.md | 既有 KU 已据 2016 升级版覆盖 2009 L4550-L4568：1954 年 12 月 8 日中央手工业管理局成立，之后举行第四次全国手工业生产合作会议；2016 另含 1955 年总社筹委会、1956 年毛泽东谈话、1960 年工艺美术教育会议、1961 年恢复总局、1965 年撤消改建第二轻工业部 |

- 三个候选均为夏燕靖同一作者的前后版本：2009 为较早版本，2016 升级版对同段内容有更完整记载；2009 没有超出既有 KU 的新语义，故不重复立目、不追加第二来源。
- no_delta 是终态，三条均带 `target_ref`；mapping 中登记 `action: "no_delta"` 与判定说明，不进入 apply-plan。

## 五、rejected 判定

本批无 `rejected`。

## 六、本批的判断

1. **同一作者前后版本按“语义增量”而非“书名数量”对账**：汉代官营漆器作坊、西夏刻字司、中央手工业管理局三条，2016 升级版已经覆盖 2009 同段且更完整；2009 没有新增事实，故判 no_delta，不把同一作者的较早版本当作第二来源重复计入。
2. **网络型机构与单一机构分层立目**：汉代官营丝织作坊是跨长安、临淄、襄邑、成都的生产网络，承载作坊规模、提花织机、织物品种与产品流向；长安东、西织室与临淄、襄邑服官已有独立 KU，本条只写网络整体，不重复两处的制度细节。这与宋代染织管理机构“中央四院 + 地方九处”的合并写法一致。
3. **“集散中心”不写成“官营作坊”**：来源只说汉时成都已成为蜀锦集散中心，没有说成都设官营丝织作坊；条目把成都登记为网络节点，不据此推断作坊设置。
4. **学会与成立大会分属两种实体**：全国高校工业设计学会是 institution，成立大会是 event。既有 `events/industrial-design-society-1985.md` 记成立大会与同期事件；本批新建学会本体条目，只登记成立时间、地点与成立场合，两条并存、不互相替代。
5. **薄条目降低断言强度**：全国高校工业设计学会只有来源一句，正文只写成立时间、地点、成立场合与组织性质，不补发起院校、章程、负责人、会员规模与后续活动；“全国高校”是否指会员范围，明确标为来源未释。
6. **引文与品种照录**：汉代官营丝织作坊的织物品种按来源逐一登记，不合并为“丝织品若干”；王充《论衡》引文照录，不据引文推断齐、襄邑两地官营作坊的隶属关系。
7. **“丝绸之路”只作产品流向**：来源把张骞通西域后的外销放在官作坊产品流向之后；条目据此登记“丝帛锦绣运销中亚、西亚乃至地中海东岸”，不把丝绸之路写成由官营作坊单独开辟。
8. **单一来源不补外部知识**：2 个新建都只有 2009 一条来源，全部 `source_count: 1`、`consensus: tentative`；来源没给的设置年代、隶属、编制、产量、章程、会员与存续状态，一律留在“证据边界”。
9. **来源只读与状态诚实**：`03基础书籍-md文档/` 只读；3 个 no_delta 不写回、不追加来源；本批不把 no_delta 记作 applied，也不把来源未给的“首次”“最早”扩写为通史判断。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：15 行；5 个候选各 3 行；终态 applied 2、no_delta 3、rejected 0；5 条终态行均带 `target_ref`。
- `apply-plan.jsonl`：2 行；均为 create，`before` 为 null；2/2 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：5 条（2 条 create + 3 条 no_delta）；`merged_candidates` 全为空；rejected 不进入 mapping。
- 候选索引：5,339 行；批前 `sha256:160a6fa5…`（applied 846、no_delta 52、needs_evidence 3,634、rejected 807），批后 `sha256:701e4dac…`（applied 848、no_delta 55、needs_evidence 3,629、rejected 807）；重建幂等。
- 内容质量审计：756 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 756/756 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，institutions 75、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；756 个 KU 均未建立正式 relation。
- 规则漂移审计：0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过；pytest 250 项、16 subtests 通过（failures 0、errors 0、skipped 0）。
- Sync closure：`--refresh-generated --full` 运行 18/18 通过；另以 `--refresh-generated --check-generated --full` 复核，第 1—16 步完成，第 17 步因工作树未提交、10 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。10 个文件为：`04-knowledge/quality/translation-index.yml`、`05-outputs/index/index.md`、`05-outputs/knowledge-graph-data.js`、`05-outputs/knowledge-graph-data.json`、`06-runtime/automation/index.md`、`06-runtime/governance/governance-backlog.md`、`06-runtime/state/candidate-index.jsonl`、`06-runtime/state/current-health.json`、`06-runtime/state/discovery-manifest.json`、`06-runtime/state/generated-projections-manifest.json`。

## 八、边界与研究债

- 全部条目只依据 2009 册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 2 个新建均为单源 2009 册，且 `source_count: 1`；汉代官营丝织作坊的来源是两段总体描述，缺单一作坊的制度细节；全国高校工业设计学会的来源只有一句。
- 具体缺项：汉代官营丝织作坊缺各作坊设置年代、隶属官署、编制、作坊址、机台数、产量与产品分配比例，未说明成都集散中心是否同时设官营作坊，也未说明官营作坊与东、西织室、服官的统属关系；全国高校工业设计学会缺发起院校、会员规模、章程、理事长与理事会、分支机构、挂靠单位、会址、刊物、会议论文、后续活动与存续状态。
- 已并存未裁定或未释的张力：汉代官营丝织作坊的“秦至汉”是来源的连续叙述，具体机构只系于汉；全国高校工业设计学会名称中的“全国高校”是否指会员范围，来源未释；学会与 1985 年成立大会的实体边界，按 institution／event 分条登记，不合并。
- 结构层仍为 0/4，层级完整挂载 0/756，正式 relation 0 条，Theme／Topic 均未实体化。
- 2009 夏燕靖 5 个 institution 候选已全部处理完毕；六册 `institution` 候选剩余 89 个，分布在 2009 赵农 41 个、2010 田自秉 37 个、2011 李立新 11 个。
- 下一批（批次 P）转入 2009 赵农 41 个 institution 候选，先按实体对账、分批处理后再写回。
- 本批临时脚本（`_tmp_institutionso_emit.py`、`_tmp_institutionso_verify.py`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
