# 田自秉《中国工艺美术史（修订本）》2010 册机构候选批次（二）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2010tianzibing-institutions-batch-u/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 处理田自秉《中国工艺美术史（修订本）》（2010）institution 候选 10 个（源行号 L2918—L4072，十六国至元代），逐条回读原文并作语义裁决。
- 结果：6 个 `create`、3 个 `update`、0 个 `no_delta`、1 个 `rejected`；无候选并入其他条目。
- 10 个候选终态：applied 9、rejected 1。
- KU 总数由 797 增至 803；institution 类型由 116 增至 122；events 仍为 115。
- 候选索引投影后：applied 904、needs_evidence 3,568、no_delta 56、rejected 811；总数 5,339。
- `02-sources/` 未改动；`03基础书籍-md文档/` 只读；本会话未执行 commit／push。

**范围说明**：2010 田自秉册共有 37 个 institution 候选，批次 T、U（10＋10）已处理 20 个，剩 17 个；六册 institution 候选剩 28 个（2010 田自秉 17、2011 李立新 11）。

**台账行数说明**：本批 ledger 为 **28 行**。9 个 applied 候选各走完整三行，9 × 3 = 27；1 个 rejected 为单行，1 × 1 = 1。

## 二、新建清单

| 文件 | 来源位置 | 主要增量 |
|---|---|---|
| institutions/houzhao-yecheng-zhijinshu.md | 2010 L2918 | 后赵邺城织锦署：引晋·陵朔《邺中记》记后赵邺城设织锦署，列大登高、小登高、大明光、小明光、大博山、小博山、大茱萸、小茱萸、大交龙、小交龙、蒲桃文锦、斑文锦、凤凰朱雀锦、韬文锦、核桃文锦等锦名，以及青、白、黄、绿、紫、蜀六色绨；“工巧百数，不可尽名”。与东晋锦署同名异实，`institutions/jinshu.md` 已作对照，本条不并入。未给设置年份、隶属、员额、工匠来源、作坊址与产品去向 |
| institutions/ciyaoguan.md | 2010 L3693 | 瓷窑官：辽代因瓷业兴起设专管窑务的“瓷窑官”；引《宋会要辑稿》太平兴国四年六月“幽州神武厅直乡岳四百余人来归山后八军伪瓷窑官三人以所授处牌印来献”，作者判断设置当在太平兴国以前。窑场分布与“官”字款只作旁证，不推断瓷窑官驻窑。未给官名全称、品级、员额、隶属、治所与职掌 |
| institutions/sichuan-jinyuan.md | 2010 L3792-L3794 | 四川锦院：元丰六年（1083）建院，募军匠 500 人，用挽综工 164、杼工 54、练染工 11、纺绎工 110，织机 154 张，用丝 125,000 两、红蓝紫染料 211,000 斤；南宋初又设 3 个织造厂，乾道四年（1168）合并为锦院；列上贡锦、官诰锦、臣僚袄子锦、广西锦四类及锦名。与汴梁绫锦院分条 |
| institutions/xiuyuan.md | 2010 L3830-L3832 | 绣院：宋代设绣院，绣工 300 余人，制人物花鸟、山水楼阁，针法称“神针”，除服饰用品外向欣赏品发展，成为后来的画绣；引《筠清轩秘录》评宋绣与《存素堂丝绣录》所载《金刚般若波罗蜜经》5,996 字、56 页。来源作“绣院”，与“文绣院”是否同一机构未说明，不合并 |
| institutions/nashishiju.md | 2010 L4036-L4042 | 纳失失局：元代织金锦名“纳石失／纳失失／纳失思／纳克实”，在弘州（今原阳）、荨麻林（今万全西北）设局，移入 3,300 多户回族工匠；织染杂造人匠都总管府下设弘州、荨麻林纳失失局；别失八里局、忽丹八里局（忽丹即今和田）亦产纳失失；并录“织金锦原称纳失失，元代改译为畏兀兀”的译名张力。各局是否同级来源未说明 |
| institutions/mumian-tijusi.md | 2010 L4072 | 木棉提举司：至元二十六年（1289）在浙东、江东、江西、湖广、福建等地设置，以都提举司总管，每年上缴棉布 10 万匹；松江以棉织为副业者 1,000 多家；《嘉禾志》作“松江者佳”。未给各司驻地、员额、品级、征收方式、棉布规格与存续时间 |

- 6 个新建均 `source_count: 1`、`version: 1`、`evidence_status: source_backed`、`confidence: medium`、`consensus: tentative`。
- 维度：6 条均为 D 主导（商业、制度与设计教育），兼 B（造物、工艺与生产技术）。
- title 均为“中文（English）”双语形式。
- after 指纹（前 19 位）：houzhao-yecheng-zhijinshu `sha256:7abc0874bda2…`（5,712 bytes／92 行）；ciyaoguan `9f28ee541fc3…`（5,744／90）；sichuan-jinyuan `63535f864e5c…`（6,195／100）；xiuyuan `2dbbdf9ec2a7…`（5,827／93）；nashishiju `3a21b5e203f6…`（7,192／99）；mumian-tijusi `95e34c3bdb7f…`（5,744／91）。

## 三、update 清单

| 文件 | 来源位置 | 主要增量 | 批前 → 批后 |
|---|---|---|---|
| institutions/lingjinyuan.md | 2010 L3488 | 同名跨朝代绫锦院条补田自秉辽代材料：上京、祖州等地设绫锦院；《辽史》载灵、锦、显、霸四州植桑麻，宜州“民工织纴，多技巧”；辽代对外赠与锦、罗、绮、纱、縠、缎等；赤峰辽墓出土织金丝织品。不据此补员额、隶属与产品分配 | `2e1cb436…`（7,699／119）→ `285abd09…`（8,734／122）；version 3、source_count 6 |
| institutions/xi-xia-guan-ying-shou-gong-ye-jigou.md | 2010 L3494 | 补田自秉同一七机构清单（制金司、织绢院、铁工院、木工院、纸工院、砖瓦院、出车（造车）院）、毡毯／氆氇／毛布与银川贺兰山墓葬；并录“造车院／出车（造车）院”用字差异，不另立第八个机构 | `4bb0068d…`（4,868／99）→ `08bf4afd…`（6,680／114）；version 2、source_count 2 |
| institutions/jiankanglu-zhiranju.md | 2010 L4030 | 补田自秉同引《金陵新志》东织染局“三千六户、机 154 张、额造 4,527 段”与元代设司／局背景、至元十六年（1279）掠夺工匠 42 万人；并录“三千六户／三千六百户”两写；加别名“建康织染局” | `515e29fc…`（5,050／90）→ `e9cadb97…`（7,014／103）；version 2、source_count 2 |

- 3 个更新均保留既有来源，新增田自秉 2010 行；`source_count` 按实际来源数：绫锦院原 6 源仍 6（田自秉已在源内），西夏群 1→2，建康路 1→2。

## 四、no_delta 判定

本批无 `no_delta`。

## 五、rejected 判定

| 候选 | 来源位置 | 判定理由 |
|---|---|---|
| 正仓院（日本）（cand-09-14） | 2010 L3388、L3392 | 候选由“在日本正仓院，还保存有我国唐代的螺钿工艺多种”触发，L3388 亦仅记正仓院藏金银平脱器；两处都只把正仓院作唐代漆器的收藏地，未给机构沿革、职能、管理制度、隶属或院址，与“中国历史博物馆”同类，不足以立 institution 条目 |

- 该 rejected 为单行记录：`expected_state: needs_evidence`、`state: rejected`、`decision.status: rejected`，无 `target_ref`，不进入 apply-plan 与 canonical-mapping。

## 六、本批的判断

1. **同名异实不合并**：后赵邺城织锦署（十六国、邺城）与东晋锦署（晋室南渡后、江南）分条；四川锦院与汴梁绫锦院分条；绣院与“文绣院”不互训。三组都因时代、地点、隶属或名实关系来源未说明，只并录对照，不强行归一。
2. **收藏地不立机构**：正仓院在来源中只作唐代漆器的收藏地，虽有藏品描述，但无机构史；“现藏／保存于某处”不足以支撑 institution 条目，故 rejected。
3. **同名跨朝代合并条只 update 不拆**：`lingjinyuan.md` 已把宋、辽、金、元四朝同名绫锦院合并登记；本批辽代材料按 update 补入，不另建“辽代绫锦院”分条，避免把同一制度名拆成互不关联的朝代条目。
4. **机构群按候选粒度合并**：西夏七机构与元代纳失失诸局都只有名称、地点或隶属线索，按机构群立目，正文并列各局名，不拆成只有名称的薄条目；也不把“别失八里局”“忽丹八里局”直接写成“纳失失局”的别名，各局是否同级来源未说明。
5. **来源用字与数字照录**：建康路东织染局“三千六户”（田自秉）与“三千六百户”（夏燕靖）并存；西夏“造车院”与“出车（造车）院”并存；纳失失的“纳石失／纳失失／纳失思／纳克实”与“畏兀兀”并存；《邺中记》作者“陵朔”原文如此。以上均不据一册改另一册。
6. **作者判断与制度数据分开**：瓷窑官的“设置当在太平兴国以前”、辽瓷“官”字款证明官窑、纳失失“可能是波斯语的讹译”等，均标为作者判断或推测，不写成已证事实。
7. **人物与技术传播不并入机构**：黄道婆条只作木棉提举司的时代背景，不并入机构条目；瓷窑官不把各窑场生产细节写成官职职掌；四川锦院不把蜀锦工艺史全部纳入。
8. **内容审计首轮 0 findings**：6 个新 KU 的 title、六节结构、source_count 与 citation 数一致，未出现批次 S 的 title 问题。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：28 行；10 个候选；applied 9（各 3 行）、rejected 1（1 行）；applied 终态行均带 `target_ref`，rejected 无。
- `apply-plan.jsonl`：9 行；create 6、update 3；create 的 `before` 为 null；update 的 `before` 与预期指纹一致；9/9 的 after 指纹、bytes、lines 与磁盘一致。
- `canonical-mapping.json`：9 条（create 6、update 3）；`merged_candidates` 全为空；与 apply-plan 的目标、动作、候选一一对应。
- 候选索引：5,339 行；批前 `sha256:05dd4761…`（applied 895、needs_evidence 3,578、no_delta 56、rejected 810），批后 `sha256:85ff2f6b…`（applied 904、needs_evidence 3,568、no_delta 56、rejected 811）；重建幂等。
- 内容质量审计：803 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 803/803 可解析，断链 0，类型覆盖 8/8，institutions 122、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；803 个 KU 均未建立正式 relation。
- 规则漂移审计：0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过；pytest 250 项、16 subtests 通过（failures 0、errors 0、skipped 0）。
- Sync closure：`--refresh-generated --full` 运行 18/18 通过；另以 `--refresh-generated --check-generated --full` 复核，第 1—16 步完成，第 17 步因工作树未提交、10 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。10 个文件为：`04-knowledge/quality/translation-index.yml`、`05-outputs/index/index.md`、`05-outputs/knowledge-graph-data.js`、`05-outputs/knowledge-graph-data.json`、`06-runtime/automation/index.md`、`06-runtime/governance/governance-backlog.md`、`06-runtime/state/candidate-index.jsonl`、`06-runtime/state/current-health.json`、`06-runtime/state/discovery-manifest.json`、`06-runtime/state/generated-projections-manifest.json`。

## 八、边界与研究债

- 6 个新建均为单源（田自秉 2010），3 个更新为两源或六源；全部 `consensus: tentative`，验证层级未评定，图版未视觉核验。
- 具体缺项：后赵织锦署缺设置年份、隶属、员额、工匠来源、作坊址、产品数量与去向；瓷窑官缺官名全称、品级、员额、隶属、治所、任期与职掌；四川锦院缺隶属、设官、工匠身份与待遇、作坊址、产品分配、产量与存续时间；绣院缺隶属、设官、院址、工匠来源、产品分配与存续时间；纳失失局缺各局设置年份、员额、织机数、产量、产品分配、工匠待遇与存续时间，3,300 多户的分配未说明；木棉提举司缺各司驻地、员额、品级、征收方式、棉布规格与用途、存续时间；绫锦院辽代部分仍缺上京、祖州两院的员额、隶属与产品分配；西夏群仍缺各机构隶属、设官、员额、职掌、产品与规模；建康路织染局仍缺全局规模、西织染局、设官、工匠来源与产品分配。
- 已并存未释的张力：后赵织锦署与东晋锦署的同名异实；四川锦院与汴梁绫锦院的关系；绣院与文绣院是否同一机构；纳失失的“纳石失／纳失失／纳失思／纳克实”与“畏兀兀”译名关系；纳失失诸局是否同级；建康路“三千六户／三千六百户”；西夏“造车院／出车（造车）院”；《邺中记》“陵朔”署名。
- 结构层仍为 0/4，层级完整挂载 0/803，正式 relation 0 条，Theme／Topic 均未实体化。
- 2010 田自秉 37 个 institution 候选已处理 20 个，剩 17 个：cand-11-53 果园厂、cand-12-21 苏州织造、cand-12-34 吴彩霞绣坊、cand-12-51 造办处、cand-12-102 诸匠营、cand-12-103 百工衙、cand-13-10 中国纺织建设公司、cand-13-11 中国蚕丝公司、cand-13-12 桥儿沟陶瓷厂、cand-13-82 建华瓷厂、cand-13-83 解放区第一个陶瓷研究所（磁州）、cand-13-13 延安玻璃厂、cand-13-81 云锦研究所、cand-13-15 苏州刺绣研究所、cand-13-14 北京珐琅厂、cand-13-16 广东南海藤厂、cand-14-21 杭州国立艺术专科学校。
- `cand-14-21` 杭州国立艺术专科学校与既有 `institutions/hangzhou-guoli-yizhuan.md` 指称相近，下一批需先对账，按 update／no_delta／rejected 裁决，不直接新建。
- 下一批（批次 V）继续 2010 田自秉剩余 17 个 institution 候选，建议按明代、清代、近现代分 2 批（9＋8）处理。
- 本批临时脚本（`_tmp_institutionstu_emit.py`、`_tmp_institutionstu_verify.py`、`_tmp_institutionstu_finalize.py`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理；`_tmp_u_closure18.txt`、`_tmp_u_closure19.txt`、`_tmp_u_repo.json`、`_tmp_u_repo.err` 同批待清理。
