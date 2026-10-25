# 赵农《中国艺术设计史》2009 册工艺候选批次（二）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-b/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从赵农《中国艺术设计史》（2009）的未分组 unit 候选中，续取第 10—17 个 `procedure` 候选逐条回读原文并作语义裁决。
- 8 个全部判 `create`，新建 procedure KU；无 `update`、无 `no_delta`、无 `rejected`。
- KU 总数由 634 增至 642，procedure 类型由 37 增至 45。
- 候选索引投影后：applied 699、no_delta 43、rejected 801、needs_evidence 3,796；active 3,796、terminal 1,543。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地域 | 主要增量 |
|---|---|---|
| procedures/zhuo-yu.md | 商周；二里头、殷墟、宝鸡 | 玉料选择、切割、磨制、钻孔、雕刻；金属工具广泛使用；铊子（砣机）为圆形工具，装车床脚踏转动；西周阴刻、浮雕、圆雕、透雕 |
| procedures/bai-lian-gang.md | 秦汉；中国 | 块铁多次加热锻打，杂质减少、体积变小、韧度与强度加大而转化为钢；“百炼成钢”出处；生产强度大、速度慢的局限 |
| procedures/chao-gang.md | 西汉中期；中国 | 生铁加热、添入矿石搅拌以降低含炭程度，再锻制，提高百炼钢制器的速度和质量 |
| procedures/chromate-oxidation-treatment.md | 秦代；秦始皇兵马俑坑 | 青铜剑长 90 厘米、脊刃对称，表面经铬盐氧化防锈处理，出土后仍寒光闪烁、锋利无比 |
| procedures/zaozhishu.md | 西汉出现；东汉蔡伦改进；罗布泊、灞桥、耒阳 | 树肤、麻头、敝布、鱼网为原料；元兴元年奏上称蔡侯纸；西汉麻纸两处出土；蔡伦尚方令职掌 |
| procedures/han-dai-qiqi-zhizuo-fengong.md | 汉代；中国；马王堆 | 漆器铭文见素工、髹工、上工、黄涂工、画工、雕工、清工、供工、造工九类工种，分工细致 |
| procedures/huodong-lianchuang-zhimo.md | 三国以后；浙江嵊县剡溪 | 竹帘置框架连续抄捞湿纸并晾晒；剡藤纸；纸药、施胶、涂布的作用与时段 |
| procedures/ran-zhi.md | 东汉开始；魏晋沿用；中国 | 黄柏皮柏碱加入纸浆染纸，增美观并防虫蛀；“装潢”词源；《齐民要术》潢纸不宜太深 |

## 三、update 清单

本批无 `update`。

## 四、no_delta 判定

本批无 `no_delta`。8 个候选逐一与既有 procedure KU 对账：琢玉、百炼钢、炒钢、铬盐氧化防锈处理、造纸术、汉代漆器制作分工、活动帘床纸模抄纸法、染纸均无对应实体，判 create；既有 `xiu-qi`、`jiazhu-tai`、`quan-die-fa` 只覆盖漆器胎骨与表面装饰，不能承载“制作分工”的工种序列，故漆器分工另立新条。

## 五、本批的判断

1. **百炼钢与炒钢分列**：百炼钢以块铁反复加热锻打去杂，炒钢以生铁加矿石搅拌脱碳；两者原料与工序不同，且赵农明言炒钢是对百炼钢大批量生产局限的后续解决，故分建互指，不压成一条。
2. **铬盐氧化防锈处理只照录来源判断**：赵农只记秦俑坑青铜剑表面经铬盐氧化防锈处理与出土效果，未给任何工艺参数；本条不据来源外材料补写工序，也不把“处理”扩写成铬盐配方或膜层工艺。
3. **造纸术与活动帘床纸模、染纸分列**：`zaozhishu.md` 记东汉蔡侯纸的原料、奏上年号与蔡伦职掌；`huodong-lianchuang-zhimo.md` 记三国以后的帘床纸模、纸药、施胶与涂布；`ran-zhi.md` 记东汉以来的潢纸。三条时段与工序层级不同，互指而不合并。
4. **漆器分工与髹漆、胎骨分工**：`han-dai-qiqi-zhizuo-fengong.md` 只记九类工种的名称与分工判断；髹涂与描彩、镶嵌、针刻归 `xiu-qi.md`，夹纻胎与圈叠法归 `jiazhu-tai.md`、`quan-die-fa.md`，三者不重复。
5. **琢玉与磨制石器分列**：琢玉条记玉料选择、铊子与四种雕刻手法；磨制石器条记石器打制后砺石加砂水的研磨。两者材料与工具不同，分列而不互相替代。
6. **染纸与纺织染色分列**：`ran-zhi.md` 记纸张载体上的柏碱染色与防虫；`dyeing.md` 记草染、石染与线染、匹染等纺织染色，载体不同。
7. **原文照录**：炒钢条“含炭程度”、染纸条“潢纸，灭白便是”均按原文录入，不改为“含碳”或改写引文。
8. **蔡伦记载的双重身份**：来源一面记其造纸“造意”，一面记其尚方令监作秘剑及诸器械“莫不精工坚密，为后世法”；本条两存，不把器械监制混入造纸工序。

## 六、本批的方法判断

- 8 个候选逐条回读原文行段：琢玉 L1686-L1690、百炼钢与炒钢 L2743-L2747、铬盐氧化防锈处理 L2763、造纸术 L3127-L3138、汉代漆器制作分工 L3230-L3234、活动帘床纸模抄纸法 L3413-L3421、染纸 L3419；核对材料、步骤、工具、引文与例证后再动笔。
- 候选 payload 的 `summary` 与 `proposed_fields` 为机器提取，span 常为章级；本批一律以原文行段为准。
- 8 个 create 均 `source_count: 1`、`confidence: medium`、`consensus: tentative`，沿用 procedure KU 的六节结构。
- KU 文件以 UTF-8 写入；写后做 YAML 解析、来源数与参考文献数一致性、六节结构与 BOM 检查，8/8 通过。
- 判定与写回分离：台账 24 行（8×3）、apply-plan 8 行（create 8）、mapping 8 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：24 行，8 个候选各 3 行；终态 applied 8。
- `apply-plan.jsonl`：8 行，全部 `create`，`before` 为 null；8/8 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：8 条，候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:c104eef4…`（applied 691、no_delta 43、needs_evidence 3,804、rejected 801），批后 `sha256:9b749968…`（applied 699、no_delta 43、needs_evidence 3,796、rejected 801）；重建幂等。
- 内容质量审计：642 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 642/642 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，procedures 45；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 266 项通过（failures 0、errors 0、skipped 0）。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 8 个新建均只有赵农 2009 单一来源，不构成独立互证。
- 琢玉未给铊子尺寸与转速、解玉砂、工序次序与工时；百炼钢未给温度、锻打次数与炉型；炒钢未给炉温、矿石配比、搅拌工具与脱碳终点；铬盐氧化防锈处理未给任何工艺参数；造纸术未给沤煮捣抄晒工序与原料配比；漆器分工未给各工职掌与工序衔接；帘床纸模未给帘床尺寸、纸药植物与用量；染纸未给柏碱浓度、配比与时间。
- 铬盐氧化防锈处理一条完全依赖赵农的转述判断，来源未附检测数据；本条照录并降级为 `tentative`，不作技术定论。
- 结构层仍为 0/4，层级完整挂载 0/642，正式 relation 0 条，Theme／Topic 均未实体化。
- 赵农 2009 册另有 22 个 `procedure` 候选待处理；六册剩余 `needs_evidence` unit 候选 2,433 个中 procedure 114 个（赵农 22、田自秉 47、李立新 10、夏燕靖 2016 35），另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_zhaonong_proceduresb_emit.py`、`_tmp_zhaonong_proceduresb_verify.py`、`_tmp_update_zhaonong_proceduresb_manifest.py`、`_tmp_zhaonong_b_junit.xml` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
