# 夏燕靖《中国设计史》2009 册早期工艺候选批次（一）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009xiayanjing-procedures-batch-1/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从夏燕靖《中国设计史》（2009）的未分组 unit 候选中，取 8 个早期工艺 `procedure` 候选逐条回读原文并作语义裁决。
- 8 个全部判 `create`，新建 procedure KU；无 `update`、无 `no_delta`、无 `rejected`。
- KU 总数由 613 增至 621，procedure 类型由 16 增至 24。
- 候选索引投影后：applied 675、no_delta 43、rejected 801、needs_evidence 3,820；active 3,820、terminal 1,519。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地域 | 主要增量 |
|---|---|---|
| procedures/mozhi-shiqi.md | 约 10000 多年前；中国 | 选石打制石斧、石刀、石锛、石铲、石凿粗坯后研磨；器形规整、刃口锋利、表面光洁；新石器革命；遗址 7000 余处；带柄工具的力学与动量原理 |
| procedures/lunzhi-fa.md | 仰韶文化中期起；黄河流域、长江中下游 | 手制与轮制两法；慢轮（幔轮）用于盘筑、加印纹饰、修整器口；轮制以快速转动提拉成形；器形规整、厚薄均匀、平行密集轮纹、器底线割偏心纹 |
| procedures/hefan-fa.md | 商周；中国 | 泥模雕纹→外范分块做三角榫→内范刮模或另制→子母扣合范、留浇铸孔→浇铸脱范打磨；耳部等突出部分用分铸法 |
| procedures/ye-tie-shu-qi-yuan.md | 商代—春秋战国；河北藁城、北京平谷、陕西雍城 | 冶铁术起源两说；商代铁刃铜器与西周晚期人工冶铁；春秋后期掌握冶铁并普遍使用铁器；战国铁器成为主要农具 |
| procedures/sheng-tie-ye-zhu-ji-shu.md | 春秋中期；晋国、南京六合 | 块炼铁到生铁铸造；公元前 513 年“铸刑鼎”；六合程桥白口铸铁铁丸为最早实物；排橐鼓风、300 人；白口铁性能与铁器时代 |
| procedures/sheng-tie-rou-hua-ji-shu.md | 战国早期；洛阳、大冶铜绿山、河北易县 | 生铁柔化（锻化）为重大发明；洛阳铁锛铁镈成白心与黑心可锻铸铁；铜绿山六角锄、易县铁鐏；早于欧洲 1700 年以上；性能介于钢与铸铁之间 |
| procedures/yin-wen-mo-yin.md | 春秋战国；中国 | 商周器模雕纹到春秋印纹阶段；印花模子趁模胎未冷盖印、一模多用；刻模须考虑四周衔接；纹样由单独纹样、二方连续到四方连续 |
| procedures/cuo-jin-yin-cuo-tong.md | 春秋中期；燕、赵、蔡 | 商周镶嵌绿松石，稍后产生错金银；春秋中期发展；栾书缶错金铭文 40 余字；燕赵蔡以红铜镶嵌图案（错铜） |

## 三、update 清单

本批无 `update`。8 个候选在 621 个 KU 中均无对应实体；与既有 procedure KU 的标题和内容逐一比对后，确认没有可承载的同题条目。

## 四、no_delta 判定

本批无 `no_delta`。几何印纹陶、几何印纹硬陶两个 term 虽含“印纹”字样，但记陶器拍印纹饰与器物类型，与本条青铜器模印装饰的材质、工序均不同，不构成 no_delta 依据。

## 五、本批的判断

1. **procedure 候选按实体而非 slug 对账**：先与既有 16 个 procedure KU 的标题、sub_type 与来源行段逐一比对，再定 create／update。8 个候选均无同题条目，故全部新建。
2. **合范法与分铸法分工**：`procedures/hefan-fa.md` 记整体制范五步与合范操作；`procedures/fenzhu-fa.md` 记耳部等突出部件先铸后合的工艺分化。两条互指，合范条只保留“突出部分用分铸法”一句，不重复分铸的定义与争议。
3. **冶铁术出现与生铁冶铸分工**：`procedures/ye-tie-shu-qi-yuan.md` 记起源年代的两说与商代铁刃器；`procedures/sheng-tie-ye-zhu-ji-shu.md` 记块炼铁到生铁铸造、铸刑鼎、排橐鼓风与白口铁性能。两段工序与证据不同，不压成一条。
4. **生铁柔化承接生铁冶铸**：柔化处理的是生铁冶铸所产白口铁，因退火（锻化）工序与冶铸不同而单列，并在相关知识元指向冶铸条。
5. **印纹（模印）与几何印纹陶区分**：本条是青铜器纹饰的复制工序（春秋印纹阶段），`terms/geometric-stamped-pottery.md` 与 `terms/geometric-stamped-hard-pottery.md` 是陶器拍印纹饰的器物类型；材质与工序不同，分列并在相关知识元说明，不合并。
6. **错金银与鎏金、金银平脱区分**：`procedures/liujin.md` 为金属表面鎏金，`procedures/jinyin-pingtuo.md` 为漆器表面金银片镶嵌；本条为青铜器表面刻槽镶嵌，三者工序与载体不同，分列互指。
7. **文本截断照录**：来源 L818 两处“铁刃铜”末字缺失，KU 照录并注明“原文作‘铁刃铜’，末字缺”，不补字改写原文。
8. **来源判断与数量照录**：磨制石器的遗址 7000 余处、正式发掘 100 余处，生铁柔化“早于欧洲 1700 年以上”，均按来源主语记录，不升为独立验证结论。

## 六、本批的方法判断

- 8 个候选逐条回读原文行段：磨制石器 L278-L297、轮制法 L322-L327、合范法 L499-L510、冶铁术 L812-L824、生铁冶铸 L825-L838、生铁柔化 L839-L844、印纹与错金银 L872-L882；核对工序、材料、工具、产量、例证与引文后再动笔。
- 8 个 create 均 `source_count: 1`、`confidence: medium`、`consensus: tentative`，沿用 procedure KU 的六节结构；`sub_type` 按工序材质取 `stoneworking_technique`、`ceramic_technique` 与 `metalworking_technique`。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析、来源数与参考文献数一致性、六节结构检查，8/8 全部通过。
- 判定与写回分离：台账 24 行（8×3）、apply-plan 8 行（create 8）、mapping 8 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：24 行，8 个候选各 3 行；终态 applied 8。
- `apply-plan.jsonl`：8 行，全部 create、`before` 为 null；8/8 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：8 条，候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:d7c810b7…`（applied 667、no_delta 43、needs_evidence 3,828、rejected 801），批后 `sha256:6cf8954a…`（applied 675、no_delta 43、needs_evidence 3,820、rejected 801）；重建幂等。
- 内容质量审计：621 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 621/621 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，procedures 24；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过（合计 266 项）。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 8 个新建均只有夏燕靖 2009 单一来源，无第二来源互证；后续若有田自秉、赵农、李立新等册的相应记载，应优先补证。
- 磨制石器未给砺石与砂水介质、工时、石料差异；轮制法未给陶轮结构与转速；合范法未给泥料配比、焙烧温度与合金配比；冶铁术未给两说各自的学者与著作、陨铁判据；生铁冶铸未给炉温、矿石与金相数据；生铁柔化未给退火参数与黑白心组织比例；印纹未给印模规格与工效数据；错金银未给刻槽、嵌入、磨错工序与材料规格。
- 来源 L818“铁刃铜”末字缺失，属文本截断，未据他册补字。
- 结构层仍为 0/4，层级完整挂载 0/621，正式 relation 0 条，Theme／Topic 均未实体化。
- 剩余 `needs_evidence` unit 候选 2,457 个（event 0、procedure 138），另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_xiayanjing_procedures_emit.py`、`_tmp_xiayanjing_procedures_verify.py`、`_tmp_update_xiayanjing_procedures_manifest.py` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
