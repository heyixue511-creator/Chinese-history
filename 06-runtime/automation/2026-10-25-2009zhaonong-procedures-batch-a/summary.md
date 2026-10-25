# 赵农《中国艺术设计史》2009 册工艺候选批次（一）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-a/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从赵农《中国艺术设计史》（2009）的未分组 unit 候选中，取前 9 个 `procedure` 候选逐条回读原文并作语义裁决。
- 7 个判 `create`，新建 procedure KU；2 个判 `update`，向既有磨制石器与错金银 KU 补入赵农 2009 记载。无 `no_delta`、无 `rejected`。
- KU 总数由 627 增至 634，procedure 类型由 30 增至 37。
- 候选索引投影后：applied 691、no_delta 43、rejected 801、needs_evidence 3,804；active 3,804、terminal 1,535。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地域 | 主要增量 |
|---|---|---|
| procedures/daogeng-huozhong.md | 新石器时代；中国 | 砍伐森林→晒干→烧荒→木棒尖头点孔种植；“烈山氏”传说；前期弃地轮换、后期翻耕连作，石锄作用重要 |
| procedures/zhitao.md | 新石器时代；中国 | 陶为黏土、水、火复合的新材料；拌泥、淘洗、加料、盘泥、拉坯、制器；藤器粘泥烘烤启示说；陶质刀、锉、纺轮；专业陶作坊与分工 |
| procedures/bianzhi.md | 新石器时代；河姆渡、良渚、仰韶 | 河姆渡苇席残片最大 1 平方米，绳索粗 1.2 厘米、细 2—3 毫米；良渚十字纹、人字纹、梅花眼、辫子口；仰韶条带式、缠结式、棋盘格纹；骨锥、骨匕 |
| procedures/divination.md | 商代；中原 | 龟腹甲背甲分开打磨、牛肩胛骨去骨臼刮磨；背面钻孔不穿透；蓍草烧灼取兆；“兆璽”（原文如此）；龟曰卜、蓍曰筮；“王占曰” |
| procedures/dyeing.md | 商周；中国 | 草染与石染；线染、匹染、多次浸染、媒染；染色成为社会生产职业；《考工记》“典丝”与“染人”等职 |
| procedures/rammed-earth-board-construction.md | 商代—战国；雍城、咸阳、蒲城、华阴 | 雍城遗址东西 3300 米、南北 3200 米；挖槽、夯土坚实、板筑；木板改圆木使受力均匀；咸阳平夯与窝夯；秦魏长城夯层明显 |
| procedures/turquoise-inlay.md | 春秋战国；湖北江陵 | 绿松石用漆汁粘嵌铜器錾槽中打磨；越王勾践剑剑格兽面纹错石为剑器应用典型 |

## 三、update 清单

| 候选 | 既有 KU | 补入内容 |
|---|---|---|
| cand-01-18 磨制技术 | procedures/mozhi-shiqi.md | 赵农 2009：砺石加砂子与水的磨制介质；石质与玉质材料的区分；刀脊与刀刃区分重量等级、工具与武器分离；旧石器晚期磨制骨针鹿角与钻孔饰物；石纺轮；绑捆加重的复合工具；玉材最初为石器补充。`source_count` 由 1 增至 2 |
| cand-03-142 错金银 | procedures/cuo-jin-yin-cuo-tong.md | 赵农 2009：错金银为春秋时期创立的技术；金银或其他金属丝片嵌入铜器表面成纹饰，以磨石错平、磨光；战国兵器、带钩、车器、铜镜多用；汲县《水陆攻战图鉴》为错铜作品。`source_count` 由 1 增至 2 |

## 四、no_delta 判定

本批无 `no_delta`。9 个候选逐一与既有 procedure KU 对账：磨制技术、错金银有同实体条目且既有 KU 缺赵农 2009 记载，判 update；刀耕火种、制陶、编织、占卜、染色、夯土板筑、错石工艺无对应实体，判 create。

## 五、本批的判断

1. **磨制技术 update 不改写夏燕靖记载**：既有 KU 的夏燕靖 2009 工序、加工效果与“新石器革命”判断原样保留，只按来源分列补入赵农的砺石砂水、石玉区分、工具武器分离与复合绑捆；两册详略差异在匹配质量中并列。
2. **错金银与错石分列**：赵农在同一段先记错金银、错铜，再记错石。错石以绿松石为嵌料、以漆汁粘接，与金属丝片嵌入后磨错的错金银在材料与工序上不同，故单列 `procedures/turquoise-inlay.md`，两条件互指而不合并。
3. **命名差异并列**：赵农称汲县出土战国器为《水陆攻战图鉴》，既有 work 条题作“水陆攻战纹鉴”；本条两存，不裁定名称。
4. **制陶与泥条盘筑、轮制法分工**：`zhitao.md` 记从黏土到成器的整体工序、陶质工具与陶作坊分工；`ni-tiao-panzhu.md` 只记“盘泥”环节，`lunzhi-fa.md` 只记“拉坯”环节的后续发展，三者层级不同，不互相替代。
5. **刀耕火种与磨制石器分工**：`daogeng-huozhong.md` 记耕作方式与前后两期，石斧、石锄、石铲、石镰、石磨盘等器形归 `mozhi-shiqi.md` 与相关农具条；本条只在核心内容列配套农具，不另立器形描述。
6. **编织不收纺轮与拈杆**：候选行段 L909-L915 所记纺轮、拈杆与纺麻葛属纺织，不属编织；本条只记苇席、竹编、绳索、渔网与骨锥骨匕，纺织另条处理。
7. **占卜只记工序**：祭祀天、地、日、月、祖先与青铜器形制多样化在本条只作关联记一句，礼器形制归青铜器相关条；占卜的钻孔参数、灼点排列与人员分工来源未载，写入证据边界。
8. **染色与防染印花分工**：`dyeing.md` 记草染、石染、四种染色方法与《考工记》职官；蜡染、蓝印花布、夹缬属防染印花，另条互指。
9. **原文照录**：占卜条“兆璽”、染色条“慌人”、错金银条“水陆攻战图鉴”、刀耕火种条“烈山氏”均按原文录入，疑似讹字或异名不加改。

## 六、本批的方法判断

- 9 个候选逐条回读原文行段：磨制 L513-L558、刀耕火种 L559-L591、制陶 L606-L627、编织 L901-L935、占卜 L1128-L1185、染色 L1435-L1456、夯土板筑 L2100-L2139、错金银与错石 L2192-L2252；核对材料、步骤、工具、实例与引文后再动笔。
- 候选 payload 的 `summary` 与 `proposed_fields` 为机器提取，span 常为章级；本批一律以原文行段为准，不用 payload 文句替代阅读。
- update 先取上一批 apply-plan 的 `before` 指纹，再改文件，改后重算 `after`；before／after 双向核对通过。
- 7 个 create 均 `source_count: 1`、`confidence: medium`、`consensus: tentative`，沿用 procedure KU 的六节结构；2 个 update 只补来源、`source_count`、描述与核心内容、匹配质量与参考文献，不改写既有记载。
- KU 文件以 UTF-8 写入；写后做 YAML 解析、来源数与参考文献数一致性、六节结构与 BOM 检查，9/9 通过。
- 判定与写回分离：台账 27 行（9×3）、apply-plan 9 行（create 7、update 2）、mapping 9 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：27 行，9 个候选各 3 行；终态 applied 9。
- `apply-plan.jsonl`：9 行；create 7 行 `before` 为 null，update 2 行 `before` 为改前指纹对象；9/9 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：9 条（create 7、update 2），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:f25748cc…`（applied 682、no_delta 43、needs_evidence 3,813、rejected 801），批后 `sha256:c104eef4…`（applied 691、no_delta 43、needs_evidence 3,804、rejected 801）；重建幂等。
- 内容质量审计：634 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 634/634 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，procedures 37；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 266 项通过（failures 0、errors 0、skipped 0）。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 7 个新建均只有赵农 2009 单一来源；2 个 update 虽有夏燕靖 2009 与赵农 2009 两册，但均为通史性叙述，不构成独立互证。
- 刀耕火种未给火候、休耕年限、作物种类与亩产；制陶未给窑温、窑型、泥料配比与烧成时间；编织未给编结方法、经纬密度与工时；占卜未给钻孔孔径深度、灼点排列与卜甲卜骨比例；染色未给染料、媒染剂、浓度与色牢度；夯土板筑未给夯层厚度、夯具形制、土料配比与模板尺寸；错石未给錾槽工具、槽深、绿松石加工与漆汁配方。
- 赵农 2009 对错金银起始时段作“春秋时期创立”，夏燕靖 2009 作“春秋中期有所发展”，两说并录，本条不裁定。
- 结构层仍为 0/4，层级完整挂载 0/634，正式 relation 0 条，Theme／Topic 均未实体化。
- 赵农 2009 册另有 30 个 `procedure` 候选待处理；六册剩余 `needs_evidence` unit 候选 2,441 个中 procedure 122 个（赵农 30、田自秉 47、李立新 10、夏燕靖 2016 35），其余为 person 273、term 875、work 652、institution 142、publication 207、place 170，另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_zhaonong_proceduresa_emit.py`、`_tmp_zhaonong_proceduresa_verify.py`、`_tmp_update_zhaonong_proceduresa_manifest.py`、`_tmp_zhaonong_a_junit.xml` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
