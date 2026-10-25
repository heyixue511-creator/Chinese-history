# 夏燕靖《中国设计史》2009 册工艺候选批次（二）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009xiayanjing-procedures-batch-2/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从夏燕靖《中国设计史》（2009）的未分组 unit 候选中，取剩余 7 个 `procedure` 候选逐条回读原文并作语义裁决。
- 6 个判 `create`，新建 procedure KU；1 个判 `update`，向既有蜡染 KU 补入 2009 册记载。无 `no_delta`、无 `rejected`。
- KU 总数由 621 增至 627，procedure 类型由 24 增至 30。
- 候选索引投影后：applied 682、no_delta 43、rejected 801、needs_evidence 3,813；active 3,813、terminal 1,526。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地域 | 主要增量 |
|---|---|---|
| procedures/xiu-qi.md | 战国；中国 | 髹漆工艺有描彩漆、镶嵌、针刻；纹样行动物纹、云纹、几何图案；色彩丰富、线条奔放、勾勒交错、气韵生动 |
| procedures/lian-gang-ji-shu.md | 春秋战国；长沙、易县、楚地 | 长沙杨家山春秋晚期钢剑含碳 0.5%～0.6%、中碳钢；易县燕下都战国晚期钢剑（104 厘米）、钢戟、钢矛为块炼铁渗碳锻打；楚地钢铁兵器闻名 |
| procedures/han-dai-zhijin-cixiu.md | 汉代；中国 | 织锦经线显花，云气、鸟兽、文字、几何、人物骑猎纹；用色五种以上；东汉蜀锦加金；刺绣针法平针、锁绣、钉线绣 |
| procedures/zhi-quan-fu-shao.md | 南宋中期；景德镇等窑 | 支圈覆烧在南方推广；窑具一次性使用，保证质量、减少变形、提高装烧密度 |
| procedures/pearl-ground-sgraffito.md | 宋代；磁州窑系 | 主题纹样空隙处划饰又细又密的珍珠纹，为磁州窑系装饰方法之一 |
| procedures/ming-qing-caici-zhuangshi.md | 明成化—清康熙；景德镇、北京 | 斗彩的青花轮廓加釉上填彩；正德素三彩；明嘉靖万历五彩；康熙五彩、珐琅彩、粉彩的彩料与工序 |

## 三、update 清单

| 候选 | 既有 KU | 补入内容 |
|---|---|---|
| cand-03-26 蜡染（蜡缬） | procedures/la-ran.md | 夏燕靖 2009：西南少数民族秦汉已掌握蜡染、当时称“阑干斑布”；点、线结合的纹样设计与色彩层次；蜡染传入中原再传亚洲各国；民丰汉代蓝白印花布反映蜡染工艺已相当精（原文中断）。`source_count` 由 1 增至 2 |

## 四、no_delta 判定

本批无 `no_delta`。蜡染候选与既有 KU 同实体但既有 KU 只引高丰 2004，缺夏燕靖 2009 的西南少数民族线索与“阑干斑布”名称，故判 update；其余 6 个候选无对应实体，判 create。

## 五、本批的判断

1. **蜡染 update 与蓝印花布分列**：夏燕靖 2009 把新疆民丰出土的“蓝白印花布”视为蜡染工艺证据，高丰 2004 则把尼雅“蜡染花布”与洛甫“蓝印花布”并列。本批只在 `la-ran.md` 记录 2009 的命名与判断，不改写 `lan-yinhua-bu.md`，避免把两册对同一出土物的不同命名强行合并。
2. **髹漆与胎骨、表面装饰分工**：`procedures/xiu-qi.md` 记战国漆器涂饰与描彩漆、镶嵌、针刻；`procedures/jiazhu-tai.md` 与 `procedures/quan-die-fa.md` 记胎骨；`procedures/jinyin-pingtuo.md` 与 `terms/diao-qi.md` 记其他表面装饰。四条互指，不重复。
3. **炼钢与生铁冶铸、柔化分工**：`procedures/lian-gang-ji-shu.md` 记块炼铁渗碳锻打；`procedures/sheng-tie-ye-zhu-ji-shu.md` 记生铁铸造；`procedures/sheng-tie-rou-hua-ji-shu.md` 记白口铁退火柔化。三条技术路线并列，不压成一条。
4. **织锦刺绣与术语条目分工**：本条记汉代织造与绣制工序及纹样、针法；`terms/jingjin.md` 记经锦、`terms/weft-brocade.md` 记纬锦、`terms/shu-brocade.md` 记蜀锦、`terms/yuexiu.md` 记粤绣，均为织物类型或地方绣种，不替代工序条。
5. **支圈覆烧的边界**：来源只记南宋中期景德镇等窑在南方推广，未及定窑的组合支圈覆烧，也未给支圈形制与装烧层数；KU 不据他册补写，证据边界保留。
6. **珍珠地划花与划花区分**：同节所记划花用梳栉状工具划出花纹、以定瓷为代表；珍珠地划花在主题纹样空隙处划珍珠纹、属磁州窑系。两者工具与施纹位置不同，分列而不合并。
7. **明清彩瓷按工艺分述**：斗彩、素三彩、五彩、珐琅彩、粉彩逐项记彩料、绘制位置与烧成次序，不按器形归类，也不为提及的瓷杯、御器另建 works 条目。
8. **文本截断与命名差异照录**：夏燕靖 2009 L1440 末句在“相当精”处中断，KU 照录并注明；高丰“蜡染花布”与夏燕靖“蓝白印花布”的命名差异在匹配质量中并列，不裁定。

## 六、本批的方法判断

- 7 个候选逐条回读原文行段：髹漆 L956-L961、炼钢 L1140-L1147、汉代织锦与刺绣 L1426-L1431、蜡染 L1433-L1441、支圈覆烧 L2548-L2551、珍珠地划花 L2552-L2589、明清彩瓷 L3589-L3591；核对工序、材料、工具、例证与引文后再动笔。
- update 先在上一批 apply-plan 取 `before` 指纹（`sha256:7b54521f…`、3,114 bytes、79 lines），再改文件，改后重算 `after`；before／after 双向核对通过。
- 6 个 create 均 `source_count: 1`、`confidence: medium`、`consensus: tentative`，沿用 procedure KU 的六节结构；update 只补来源、`source_count`、描述与核心内容、匹配质量与参考文献，不改写既有高丰记载。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析、来源数与参考文献数一致性、六节结构检查，7/7 全部通过。
- 判定与写回分离：台账 21 行（7×3）、apply-plan 7 行（create 6、update 1）、mapping 7 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：21 行，7 个候选各 3 行；终态 applied 7。
- `apply-plan.jsonl`：7 行；create 6 行 `before` 为 null，update 1 行 `before` 为改前指纹对象；7/7 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：7 条（create 6、update 1），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:6cf8954a…`（applied 675、no_delta 43、needs_evidence 3,820、rejected 801），批后 `sha256:f25748cc…`（applied 682、no_delta 43、needs_evidence 3,813、rejected 801）；重建幂等。
- 内容质量审计：627 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 627/627 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，procedures 30；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过（合计 266 项）。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 6 个新建均只有夏燕靖 2009 单一来源；蜡染虽有高丰 2004 与夏燕靖 2009 两册，但均为通史性叙述，且对同一民丰出土物命名不一，不构成独立互证。
- 髹漆未给底胎处理、漆层遍数与干燥工序；炼钢未给渗碳温度、锻打次数与热处理制度；织锦刺绣未给织机、经纬密度与金线材质；支圈覆烧未给支圈形制与装烧层数；珍珠地划花未给工具、单元尺寸与烧成；明清彩瓷未给彩料配方、烧成温度与次数。
- 夏燕靖 2009 L1440 末句中断，属文本截断，未据他册补字。
- 结构层仍为 0/4，层级完整挂载 0/627，正式 relation 0 条，Theme／Topic 均未实体化。
- 夏燕靖 2009 册的 15 个 procedure 候选已全部处理完毕；六册剩余 `needs_evidence` unit 候选 2,450 个（procedure 131，其余为 institution、place、publication、person、work、term），另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_xiayanjing_procedures2_emit.py`、`_tmp_xiayanjing_procedures2_verify.py`、`_tmp_update_xiayanjing_procedures2_manifest.py` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
