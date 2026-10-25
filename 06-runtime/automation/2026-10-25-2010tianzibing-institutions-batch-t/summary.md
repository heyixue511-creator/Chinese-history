# 田自秉《中国工艺美术史（修订本）》2010 册机构候选批次（一）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2010tianzibing-institutions-batch-t/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 处理田自秉《中国工艺美术史（修订本）》（2010）institution 候选 10 个（源行号 L23—L2916，含版权页误触发、汉代工官与南朝染署），逐条回读原文并作语义裁决。
- 结果：5 个 `create`、3 个 `update`、0 个 `no_delta`、2 个 `rejected`；无候选并入其他条目。
- 10 个候选终态：applied 8、rejected 2。
- KU 总数由 792 增至 797；institution 类型由 111 增至 116；events 仍为 115。
- 候选索引投影后：applied 895、needs_evidence 3,578、no_delta 56、rejected 810；总数 5,339。
- `02-sources/` 未改动；`03基础书籍-md文档/` 只读；本会话未执行 commit／push。

**范围说明**：2010 田自秉册共有 37 个 institution 候选，本批处理 10 个，剩 27 个；六册 institution 候选剩 38 个（2010 田自秉 27、2011 李立新 11）。

**台账行数说明**：本批 ledger 为 **26 行**。8 个 applied 候选各走完整三行，8 × 3 = 24；2 个 rejected 各为单行，2 × 1 = 2。

## 二、新建清单

| 文件 | 来源位置 | 主要增量 |
|---|---|---|
| institutions/shujun-chengdu-guanghanjun-gongguan.md | 2010 L2145、L2561 | 蜀郡、成都、广汉郡工官：L2145 与尚方令、考工令并列，同属官方制铜机构，蜀郡、广汉所制最精；L2561 记三处工官每年各用费五百万。来源未给设置年代、员额、隶属、治所与产品分配。“成都”与“蜀郡”是否同级、是否同一治所，来源未说明，条目照录三名，不擅自并为二 |
| institutions/baoshi.md | 2010 L2519 | 暴室：引《三辅黄图》记未央宫有暴室，为主掖庭织作染练之署；与平准令并列。来源未给隶属、员额、设置年代与产品去向 |
| institutions/pingzhunling.md | 2010 L2519 | 平准令：引《续汉书·百官志》记其主练染作彩色；与暴室并列。不据官名补入来源未记的平准物价职能，也不与南朝平准令合并；隶属、员额、设置年代未给 |
| institutions/yandao-muguan.md | 2010 L2697 | 严道木官：引《汉书·地理志》“严道有木官”，为专事运输木材的官吏；作者“规模很大，品种繁多”标为来源判断，不当作独立数据。隶属、员额、运输路线与木材品种未给 |
| institutions/nanchao-ranshu.md | 2010 L2912-L2916 | 南朝染署：南朝少府下有平准令管理染织生产，后避宋顺帝刘准讳改名染署。北朝司染署与隋唐织染署不并入本条，沿革关系来源未给；设置年份、员额与内部署作未给 |

- 5 个新建均 `source_count: 1`、`version: 1`、`evidence_status: source_backed`、`confidence: medium`、`consensus: tentative`。
- 维度：5 条均为 D 主导（商业、制度与设计教育），兼 B（造物、工艺与生产技术）。
- title 均为“中文（English）”双语形式。
- after 指纹（前 19 位）：shujun-chengdu-guanghanjun-gongguan `sha256:480a82b6fd49…`（5,192 bytes／88 行）；baoshi `7e25b3beebba…`（4,173／86）；pingzhunling `a0888435aea2…`（4,043／84）；yandao-muguan `f29e4088fc32…`（4,272／85）；nanchao-ranshu `d4ad0c3f7a2f…`（4,309／87）。

## 三、update 清单

| 文件 | 来源位置 | 主要增量 | 批前 → 批后 |
|---|---|---|---|
| institutions/shangfang.md | 2010 L2145、L2249 | 补少府隶属、汉武帝分左／中／右三官署、中尚方制鼎壶；引《后汉书》“尚方……掌上手工作御刀剑玩好器物”，左尚方主弩机、中尚方主装饰具、右尚方主镜／槃／釜。与赵农蔡伦条并录，不裁断“尚方令”与三官署的统属细节 | `56610b01…`（4,379／90）→ `0685ec12…`（7,569／113） |
| institutions/dongxi-zhishi.md | 2010 L2442 | 补《汉书·百官公卿表》少府属东织室令丞、西织室令丞；河平元年（前28）省东织、更名西织为织室，绥和（前7）废；《贡禹传》“三工官费五千万，东西织室亦然”。与夏燕靖 2016“东汉时……在长安设有东、西织室”并录，标时代冲突，不裁断 | `115f5b57…`（4,279／89）→ `1d776a06…`（7,189／109） |
| institutions/han-dai-qiqi-zuofang-guan-yuan.md | 2010 L2561-L2567 | 补八郡名单（广汉、蜀、河内、河南、颍川、南阳、济南、泰山）、蜀郡／成都／广汉工官每年各用费五百万、梓潼／武都工官、蜀郡广汉主要中心、乐浪铭文与约百年铭文年代（前85—69）；11 种分工另见 `procedures/han-dai-qiqi-zhizuo-fengong.md`。并录“6—8 道 vs 11 种分工”“金属铸器铭文 vs 漆器铭文”两处张力 | `8bd97fd0…`（5,232／91）→ `07979e2b…`（9,715／128） |

- 3 个更新均 `version: 2`、`source_count: 2`；新增来源行均带 `evidence_ref`。
- update 的 `before` 指纹取各自创建批次的 `apply-plan.jsonl` 终态行；三个目标文件在本批前仍为未跟踪文件，HEAD 无原版，故不以 `git show HEAD:` 取指纹。

## 四、no_delta 判定

本批无 `no_delta`。

## 五、rejected 判定

| 候选 | 来源位置 | 判定理由 |
|---|---|---|
| 东方出版中心（cand-01-04） | 2010 L23-L61 | 该段为 CIP／版权页，只有出版发行、地址、电话、印刷、开本、字数、印张、版次、ISBN、定价，非设计史机构，未提供可立目的机构史内容 |
| 中国历史博物馆（cand-03-31） | 2010 L953 | 候选仅因“司母戊鼎现陈列于中国历史博物馆”而触发；来源未记该馆的机构沿革、职能、藏品管理或设计史活动，仅作展陈地点，不足以立 institution 条目 |

- 2 个 rejected 均为单行记录：`expected_state: needs_evidence`、`state: rejected`、`decision.status: rejected`，无 `target_ref`，不进入 apply-plan 与 canonical-mapping。

## 六、本批的判断

1. **版权页不立机构条目**：东方出版中心是出版者，不是设计史叙述对象；来源对其只有出版发行信息，若立目会把书目元数据误当机构史。
2. **“被提及”不等于可立目**：中国历史博物馆只作司母戊鼎的展陈地点出现，没有机构沿革、职能或设计史活动；同类“现藏／现陈列于”表述不足以支撑 institution 条目，故 rejected 而非 create。
3. **同一实体跨门类合并一次**：蜀郡、成都、广汉郡工官在铜器条与漆器条两见，按来源所列三名立一条，合两处材料；成都与蜀郡的层级关系来源未给，条目不擅自合并为二，也不拆成三条。
4. **官名相同而时代不同者不合并**：汉代平准令主练染作彩色，南朝平准令管染织生产并改名染署；两条分属不同朝代与不同沿革，来源未给连续性，故汉代平准令 new、南朝染署另立，不合并。北朝司染署与隋唐织染署同样不并入南朝染署。
5. **不据官名补职能**：平准令在来源中只记“主练染作彩色”，不据“平准”二字补入平准物价、均输等来源未记职能。
6. **冲突并录，不裁断**：东织室的“东汉”（夏燕靖 2016）与“西汉河平、绥和间省改废”（田自秉引《汉书·百官公卿表》）并存；漆器工序“6—8 道”（夏燕靖）与“11 种分工”（田自秉）并存；铭文载体“金属铸器”（夏燕靖）与“漆器铭文”（田自秉）并存。三条均注明差异，不据新源改写旧源。
7. **作者判断与来源数据分开**：严道木官条把“规模很大，品种繁多”标为作者判断，不写成独立统计；暴室、平准令的“并列”关系只照录来源，不补分工。
8. **子条目引用而非重复**：汉代漆器 11 种分工已在 procedure KU 中展开，本批 update 只引用条目标题，不复制工种清单，避免同一材料在两处维护。
9. **内容审计首轮 0 findings**：5 个新 KU 的 title 均按“中文（English）”写，未重演批次 S 的 title 问题。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：26 行；10 个候选；applied 8（各 3 行）、rejected 2（各 1 行）；applied 终态行均带 `target_ref`，rejected 均无。
- `apply-plan.jsonl`：8 行；create 5、update 3；create 的 `before` 为 null；update 的 `before` 与预期指纹一致；8/8 的 after 指纹、bytes、lines 与磁盘一致。
- `canonical-mapping.json`：8 条（create 5、update 3）；`merged_candidates` 全为空；与 apply-plan 的目标、动作、候选一一对应。
- 候选索引：5,339 行；批前 `sha256:8cefbf52…`（applied 887、needs_evidence 3,588、no_delta 56、rejected 808），批后 `sha256:05dd4761…`（applied 895、needs_evidence 3,578、no_delta 56、rejected 810）；重建幂等。
- 内容质量审计：797 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 797/797 可解析，断链 0，类型覆盖 8/8，institutions 116、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；797 个 KU 均未建立正式 relation。
- 规则漂移审计：0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过；pytest 250 项、16 subtests 通过（failures 0、errors 0、skipped 0）。
- Sync closure：`--refresh-generated --full` 运行 18/18 通过；另以 `--refresh-generated --check-generated --full` 复核，第 1—16 步完成，第 17 步因工作树未提交、10 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。10 个文件为：`04-knowledge/quality/translation-index.yml`、`05-outputs/index/index.md`、`05-outputs/knowledge-graph-data.js`、`05-outputs/knowledge-graph-data.json`、`06-runtime/automation/index.md`、`06-runtime/governance/governance-backlog.md`、`06-runtime/state/candidate-index.jsonl`、`06-runtime/state/current-health.json`、`06-runtime/state/discovery-manifest.json`、`06-runtime/state/generated-projections-manifest.json`。

## 八、边界与研究债

- 5 个新建均为单源（田自秉 2010），3 个更新为两源；全部 `consensus: tentative`，验证层级未评定，图版未视觉核验。
- 具体缺项：蜀郡成都广汉工官缺设置年代、员额、隶属、治所、产品分配与三处分工；暴室缺隶属、员额、设置年代、产品去向与与平准令的分工；平准令缺隶属、员额、设置年代与染练品种；严道木官缺隶属、员额、运输路线、木材品种与采伐组织；南朝染署缺设置年份、员额、内部署作与北朝司染署的沿革关系；尚方缺员额、作坊址、工匠组织与产品数量；东、西织室缺二室分工、员额、作坊址与产品名目；汉代漆器作坊官员缺各郡工官员额、隶属层级、作坊址与产品分配。
- 已并存未释的张力：东、西织室的“东汉（夏燕靖）／西汉河平绥和间省废（田自秉引《汉书》）”；漆器工序“6—8 道／11 种分工”；铭文载体“金属铸器／漆器铭文”；“尚方令”与左中右三官署的统属；“成都”与“蜀郡”的层级；汉代平准令与南朝平准令、南朝染署与北朝司染署／隋唐织染署的沿革关系。
- 结构层仍为 0/4，层级完整挂载 0/797，正式 relation 0 条，Theme／Topic 均未实体化。
- 2010 田自秉 37 个 institution 候选已处理 10 个，剩 27 个：cand-08-07 后赵邺城织锦署、cand-09-14 正仓院、cand-09-33 辽代绫锦院、cand-09-34 西夏官营手工业机构群、cand-09-95 瓷窑官、cand-10-15 四川锦院、cand-10-27 绣院、cand-10-66 建康织染局、cand-10-68 纳失失局、cand-10-72 木棉提举司、cand-11-53 果园厂、cand-12-21 苏州织造、cand-12-34 吴彩霞绣坊、cand-12-51 造办处、cand-12-102 诸匠营、cand-12-103 百工衙、cand-13-10 中国纺织建设公司、cand-13-11 中国蚕丝公司、cand-13-12 桥儿沟陶瓷厂、cand-13-82 建华瓷厂、cand-13-83 解放区第一个陶瓷研究所（磁州）、cand-13-13 延安玻璃厂、cand-13-81 云锦研究所、cand-13-15 苏州刺绣研究所、cand-13-14 北京珐琅厂、cand-13-16 广东南海藤厂、cand-14-21 杭州国立艺术专科学校。
- `cand-14-21` 杭州国立艺术专科学校与既有 `institutions/hangzhou-guoli-yizhuan.md` 指称相近，下一批需先对账，按 update／no_delta／rejected 裁决，不直接新建。
- 下一批（批次 U）继续 2010 田自秉剩余 27 个 institution 候选，建议按时代分组（魏晋至宋元、明代、清代、近现代）分 3 批处理。
- 本批临时脚本（`_tmp_institutionst_emit.py`、`_tmp_institutionst_verify.py`、`_tmp_institutionst_finalize.py`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理；`_tmp_t_repo.json`、`_tmp_t_closure18.txt`、`_tmp_t_closure19.txt` 同批待清理。
