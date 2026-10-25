# 高丰《中国设计史》2004 册工艺候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2004gaofeng-procedures-batch/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从高丰《中国设计史》（2004）的未分组 unit 候选中，取 5 个 `procedure` 候选逐条回读原文并作语义裁决。
- 4 个判 `create`，新建 procedure KU；1 个判 `update`，向既有雕版印刷 KU 补入高丰册的工艺记载。无 `no_delta`、无 `rejected`。
- KU 总数由 609 增至 613，procedure 类型由 12 增至 16。
- 候选索引投影后：applied 667、no_delta 43、rejected 801、needs_evidence 3,828；active 3,828、terminal 1,511。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地点 | 主要增量 |
|---|---|---|
| procedures/quan-die-fa.md | 宋代；湖北监利福田寺宋墓 | 杉木切约 0.2 厘米薄长条卷制成胎，承汉代薄片卷木胎而来；胎型轻薄结实、不易变形；宋代实用漆器广泛运用；花瓣形圈足黑漆碗实例，器表黑褐色漆、器内朱漆 |
| procedures/la-ran.md | 东汉；新疆民丰县尼雅 | 出土蜡染花布；来源据此判断汉代蜡染工艺技术已经成熟；与蓝印花布同条并记 |
| procedures/lan-yinhua-bu.md | 汉代；洛甫县 | 出土蓝印花布；来源据此判断汉代蓝印花布工艺技术已成熟；与尼雅蜡染同条并记 |
| procedures/duanban-taoyin.md | 明代创造、清代盛行；中国 | 《芥子园画传》采用明代短版套印并有所发展；清代后期多色套印更盛；《劝善金科》五色；1834 年卢坤刊《杜工部集》25 卷六色，正文墨笔，眉批、注、标点用紫、绿、黄、蓝、红，为古代色彩最多的彩色套印刻本 |

## 三、update 清单

| 候选 | 既有 KU | 补入内容 |
|---|---|---|
| cand-04-13 雕版印刷术 | procedures/diaoban-yinshua.md | 高丰 L3102-L3118：明胡应麟“雕本肇于隋时，行于唐世”与隋代实物未发现；1974 年西安唐墓唐初梵文陀罗尼咒、1906 年吐鲁番唐武周《妙法莲华经》残卷（不晚于 690—699）；制备木板→反贴图文稿→雕刻反体图文→刷印四步程序；梓木、梨木、枣木用材；刻工决定效果；日印 1500—2000 印张、每版连印万次、效率提高百倍。`source_count` 由 2 增至 3 |

## 四、no_delta 判定

本批无 `no_delta`。雕版印刷虽有既有专条，但只引赵农 2009 与夏燕靖 2016，缺高丰 2004 的发明时间考辨、工艺程序、用材与产量，故判 update 而非 no_delta；其余 4 个候选在 613 个 KU 中无对应实体，判 create。

## 五、本批的判断

1. **procedure 候选按实体而非 slug 对账**：既有 procedure KU 与候选 slug 并非一一对应（如 `procedures/chuihui-fa.md` 已覆盖候选 `chuihui-fa-lianyin`）。本批先把候选标题与既有 12 个 procedure KU 的实体名称对齐，再定 create／update；5 个候选中仅雕版印刷已有专条。
2. **蜡染与蓝印花布同条并记，仍分建两条**：高丰 L2181 以一句并记尼雅东汉蜡染花布与洛甫汉代蓝印花布，并同时判断两种工艺均已成熟。二者材料与防染原理不同，KU 分建并在“相关知识元”互指，不压成一条。
3. **来源判断照录，不升为定论**：来源由单件出土实物推断“工艺技术已经成熟”，KU 写“来源据此判断”，并在证据边界注明未给工艺细节；不把推断改写为既有共识。
4. **圈叠法与夹纻胎分工**：`procedures/jiazhu-tai.md` 记夹纻胎，圈叠法记杉木薄长条卷制木胎；同属漆器胎骨工艺，但材料与工序不同，分列并互指。
5. **短版套印与雕版印刷分工**：雕版印刷条记单色雕印的发明考辨、程序、用材与产量；短版套印条记明代创造的多色套印与清代实例。《芥子园画传》在两处各取所需，不重复叙述同一段原文。
6. **证据边界逐条写清**：每条末尾列出源未给的工序参数（卷制工具、粘接材料、圈叠层数、用蜡与染料、花版与浆料、分版数量与套准、颜料与纸张），不以常识补写。
7. **维度判断**：圈叠法 B（漆器胎骨）、蜡染与蓝印花布 B（纺织印染）、短版套印 C（书籍印刷）；雕版印刷维持 C。新建 4 条为 B、B、B、C。

## 六、本批的方法判断

- 5 个候选逐条回读原文行段：圈叠法 L3692-L3697、蜡染与蓝印花布 L2181、短版套印 L5174、雕版印刷 L3102-L3118（工艺程序见 L3106、产量见 L3117）；核对材料、步骤、工具、产量、实例与引文后再动笔。
- update 先在磁盘取 `before` 指纹（`sha256:0c83f919…`、3,836 bytes、82 lines），再改文件，改后重算 `after`；apply-plan 的 before／after 双向核对通过。
- 4 个 create 均 `source_count: 1`、`confidence: medium`、`consensus: tentative`，沿用 procedure KU 的六节结构；update 只补来源、`source_count`、描述与核心内容、匹配质量与参考文献，不改写既有事实。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析、来源数与参考文献数一致性、六节结构检查，5/5 全部通过。
- 判定与写回分离：台账 15 行（5×3）、apply-plan 5 行（create 4、update 1）、mapping 5 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：15 行，5 个候选各 3 行；终态 applied 5。
- `apply-plan.jsonl`：5 行；create 4 行 `before` 为 null，update 1 行 `before` 为改前指纹对象；5/5 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：5 条（create 4、update 1），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:3a715412…`（applied 662、no_delta 43、needs_evidence 3,833、rejected 801），批后 `sha256:d7c810b7…`（applied 667、no_delta 43、needs_evidence 3,828、rejected 801）；重建幂等。
- 内容质量审计：613 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 613/613 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，procedures 16；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过（合计 266 项）。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 4 个新建均只有高丰 2004 单一来源，无第二来源互证；后续若有其他册或考古报告，应优先补证蜡染、蓝印花布与短版套印。
- 圈叠法未给卷制工具、粘接材料、圈叠层数与干燥工序；蜡染未给用蜡、工具、染料与纹样；蓝印花布未给花版材质、防染浆料、染料、纹样与出土情境；短版套印未给分版数量、刻版与套准工序、颜料与纸张；雕版印刷的印版尺寸、墨料配方、刻工组织与流通价格三册均未展开。
- 结构层仍为 0/4，层级完整挂载 0/613，正式 relation 0 条，Theme／Topic 均未实体化。
- 剩余 `needs_evidence` unit 候选 2,465 个（event 0、procedure 146），另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_gaofeng_procedures_emit.py`、`_tmp_gaofeng_procedures_verify.py`、`_tmp_update_gaofeng_procedures_manifest.py`、`_tmp_repo_audit.txt`、`_tmp_rule_drift.txt`、`_tmp_pytest.xml`、`_tmp_pytest_out.txt`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
