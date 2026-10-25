# 田自秉《中国工艺美术史》2010 册工艺候选批次（一）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2010tianzibing-procedures-batch-e/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从田自秉《中国工艺美术史（修订本）》（2010）的 47 个 `procedure` 候选中，取前 15 个逐条回读原文并作语义裁决。
- 8 个判 `create`，新建 procedure KU；7 个判 `update`，补入既有 procedure KU；无 `no_delta`、无 `rejected`。
- KU 总数由 662 增至 670，procedure 类型由 65 增至 73。
- 候选索引投影后：applied 736、no_delta 43、rejected 801、needs_evidence 3,759；active 3,759、terminal 1,580。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地域 | 主要增量 |
|---|---|---|
| procedures/caihui-tao-zhizuo.md | 新石器时代晚期；河南渑池仰韶村、西安半坡 | 彩陶为绘黑红花纹的红褐或棕黄陶器；手捏成形，陶坯未全干时以木片、卵石打磨表里，绘花纹后入窑；红彩为赤铁矿、黑彩为锰化物；半坡遗址发现 6 座烧彩陶陶窑 |
| procedures/fengyao-jishu.md | 父系氏族社会；黄河流域、长江流域 | 严密封窑使陶坯铁元素还原，烧成较硬的灰陶；控制烧成末期窑内空气与温度烧成黑陶；瓷土烧白陶；黑陶窑火口小、火膛窄深，便于封闭还原 |
| procedures/sao-si-piaobai.md | 周代；中国 | 《考工记》以灰水沤丝使柔软；栏木灰与蜃灰漂白丝帛；晾丝“去地尺暴之”，太高易脆、太低近潮不易干 |
| procedures/bangpao-xiangqian.md | 周代（西周）；西安普渡村、濬县辛村、宝鸡斗鸡台、洛阳庞家沟 | 蚌泡镶嵌为周代漆器流行装饰；推测木胎或编织胎外涂漆再镶蚌泡；辛村圆盒边缘、庞家沟漆器托两例；为后世螺钿前身 |
| procedures/san-die-fa.md | 商代后期；中国 | 商代铜器装饰早期脱胎于陶器拍印，后期用刻花；除主纹、地纹外，在较粗花纹或主体花纹上再勾刻细线，称三层花纹或“三叠法” |
| procedures/hanjie.md | 春秋战国；中国 | 焊接以热加工把部件或局部连接在主体上；浑铸为范块一次铸成，分铸为部件先铸再与主体一次铸成，焊接可在主体铸成后补接；便利铸制并丰富造型 |
| procedures/kehua.md | 战国；辉县、长治、琉璃阁、上海博物馆藏品 | 刻划随铁工具提高而出现，铁坚韧易刻铜；战国刻纹宴乐铜鉴、刻纹铜匜、刻纹铜奁、刻纹铜杯；线条细如毫发、流畅如线纹装饰画 |
| procedures/qingtong-xiangqian.md | 春秋战国；中国 | 镶嵌为在青铜器上嵌松石、红铜或金银丝；春秋多用红铜镶嵌，产生色彩对比与金属光泽；战国金银错更富丽辉煌 |

## 三、update 清单

| 文件 | 候选 | 变更 |
|---|---|---|
| procedures/mozhi-shiqi.md | cand-02-50 | 增田自秉 L459；source_count 2→3；tags 增打击、作窝、琢制、管钻、两面对钻；补石器制作五序、管钻与两面对钻、四处遗址就地取材与审美判断；层级说明改为旧石器至新石器 |
| procedures/lunzhi-fa.md | cand-02-73 | 增田自秉 L746；source_count 1→2；tags 增黑陶、蛋壳黑陶、封窑、龙山文化、良渚文化；补黑陶轮制、器形与器胎效果、生产力提高、封窑技术与窑室结构 |
| procedures/bianzhi.md | cand-03-02 | 增田自秉 L833-L835；source_count 1→2；tags 增钱山漾、席纹、竹编用具；补编织早于陶器的起源、半坡庙底沟席纹、钱山漾 200 多件竹编、篾条加工与辫子口 |
| procedures/hefan-fa.md | cand-03-21 | 增田自秉 L913-L915；source_count 1→2；aliases 增陶范法、泥模法；补炼矿制范熔铸条件、朱笔绘纹、澄滤细泥外范、支钉子母榫、绳索厚泥加固与蜡模法线索 |
| procedures/dyeing.md | cand-04-34 | 增田自秉 L1535；source_count 1→2；tags 增一入、七入、繻、赪、玄、缁；补《考工记》一入至七入的浸染递深色序 |
| procedures/cuo-jin-yin-cuo-tong.md | cand-05-34 | 增田自秉 L1808；source_count 2→3；tags 增错石、厝石、细砂岩；补错石（厝石）为细砂岩的释名与“它山之石”文献依据；注明与绿松石“错石工艺”同名异指 |
| procedures/yin-wen-mo-yin.md | cand-05-36 | 增田自秉 L1780-L1782；source_count 1→2；补印纹阶段判断、盖印时机、一模多用与纹样格式演变；并录“尚未冷却／尚未全干”差异 |

- 7 条 before／after 指纹均与磁盘及 pre-image 一致：mozhi `804f2a73…`→`e26f8c44…`（7,678→10,501 bytes，92→111 行）；lunzhi `b62b351c…`→`ab38964b…`（3,686→6,023，73→92）；bianzhi `02dfd858…`→`0ff6dbd8…`（4,592→7,082，81→98）；hefan `8713f506…`→`a124806d…`（4,155→6,991，74→96）；dyeing `4e1fe952…`→`416581f5…`（4,446→6,125，80→98）；cuojin `aad8f5b4…`→`c75c3008…`（5,617→7,631，90→107）；yinwen `7e2ffc4b…`→`c6605fea…`（4,135→6,410，75→89）。

## 四、no_delta 判定

本批无 `no_delta`。15 个候选逐一与既有 procedure KU 对账：

- 石器制作、轮制、编织、陶范法、染色、金银错、模印七项均有同名或同实体的既有条目，判 update；既有条目已覆盖主体工序，但缺田自秉所记的环节、别名或参数，故补写而不另立重复条目。
- 彩陶制作、封窑、缫丝漂白与晾丝、蚌泡镶嵌、三叠法、焊接、刻划、青铜镶嵌八项在既有 procedure KU 中无对应实体，判 create。
- `封窑` 虽与 `轮制法` 同出 L421，但一为烧成气氛控制、一为成形，工序单位不同，分列互指；`缫丝漂白与晾丝` 与 `染色` 同出《考工记》染整段，但为染色前的丝帛处理，分列互指；`青铜镶嵌` 为总类条目，`错金银与错铜`、`错石工艺` 为专条，分列互指。

## 五、本批的判断

1. **磨制石器补全工序链**：既有条目以“打制粗坯→研磨”为主，田自秉给出打击、作窝、琢制、磨制、钻孔的完整序列及管钻、两面对钻的技术改革意义，属同一石器加工实体，判 update。
2. **黑陶轮制并入轮制法，封窑另立**：黑陶的器形、器胎与生产力效果是轮制成形的内容，并入 `lunzhi-fa.md`；封窑与还原烧成是窑炉气氛控制，另立 `fengyao-jishu.md`，两条互指，不把烧成技术写成轮制的一部分。
3. **彩陶制作独立成条**：既有 `zhitao.md` 记制陶的一般工序，`lunzhi-fa.md` 记轮制成形，均不载彩陶的打磨、绘彩与矿物颜料；彩陶制作的手捏、表里打磨、绘彩后烧成构成独立工序链，判 create。
4. **陶范法以既有合范法承载**：田自秉明言“陶范法，或称泥模法”，与既有 `hefan-fa.md` 同实异名；补入朱笔绘纹、支钉子母榫、绳索厚泥加固等工序，并把别名写入 aliases。
5. **错石同名异指必须区分**：田自秉的“错石（厝石）”是磨错用的细砂岩，赵农的“错石工艺”是以绿松石嵌饰；两义同名，本条在正文与相关知识元两处注明，不把细砂岩并进绿松石条。
6. **印纹盖印时机两说并录**：夏燕靖作“模胎尚未冷却”，田自秉作“模胎尚未全干”；本条并录不裁定，并在证据边界标出差异。
7. **焊接、刻划、镶嵌按工序分列**：三项同出“青铜器的装饰”一节，但焊接是部件连接、刻划是铸后线刻、镶嵌是表面嵌饰，工序单位不同；镶嵌作总类，错金银、错铜、错石另有条目，避免把总类写成某一嵌料的专条。
8. **蚌泡镶嵌与螺钿前身**：来源明言蚌泡镶嵌是“现今漆器中螺钿的前身”，本条照录这一定位，不把后世螺钿的工艺参数回溯写入西周条目。

## 六、本批的方法判断

- 15 个候选逐条回读原文行段：石器 L459、彩陶 L494、轮制与封窑 L419-L421 与 L746、编织 L833-L835、陶范 L913-L915、三叠 L1164、染色 L1535、缫丝 L1537、蚌泡 L1590、模印 L1780-L1782、焊接 L1802、刻划 L1804、镶嵌 L1806、金银错 L1808；核对材料、步骤、工具、引文与例证后再动笔。
- 候选 payload 的 `summary` 与 `proposed_fields` 为机器提取，span 常为章级；本批一律以原文行段为准，机器摘要只作索引，不作阅读替代。
- 8 个 create 均 `source_count: 1`、`consensus: tentative`、`confidence: medium`；7 个 update 的 `source_count` 为 2（6 条）或 3（mozhi、cuojin）。
- KU 文件以 UTF-8 写入；写后做 YAML 解析、来源数与参考文献数一致性、六节结构与 BOM 检查，15/15 通过。
- 判定与写回分离：台账 45 行（15×3）、apply-plan 15 行（create 8、update 7）、mapping 15 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：45 行，15 个候选各 3 行；终态 applied 15。
- `apply-plan.jsonl`：15 行，create 8 行 `before` 为 null，update 7 行带 before 指纹；15/15 的 after 指纹与磁盘一致，7/7 的 before 与 pre-image 一致。
- `canonical-mapping.json`：15 条，候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:813de48a…`（applied 721、no_delta 43、needs_evidence 3,774、rejected 801），批后 `sha256:df8689e7…`（applied 736、no_delta 43、needs_evidence 3,759、rejected 801）；重建幂等。
- 内容质量审计：670 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 670/670 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，procedures 73、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；670 个 KU 均未建立正式 relation。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 266 项通过（failures 0、errors 0、skipped 0）。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 8 个新建均只有田自秉 2010 单一来源，不构成独立互证；7 个 update 中，mozhi、cuojin 得三册来源，lunzhi、bianzhi、hefan、dyeing、yinwen 得两册来源。
- 彩陶未给颜料研磨与调和、绘彩工具、烧成温度与气氛、陶窑结构；封窑未给密封材料、气氛浓度、温度曲线与成品率；缫丝未给灰水浓度、浸泡时长、温度与配比；蚌泡未给蚌泡加工、粘接材料与髹漆工序；三叠法未给勾刻工具、线宽与实例；焊接未给焊料、温度、接头与强度；刻划未给刻刀、线宽与工序；青铜镶嵌未给嵌槽、固定与磨错工序。
- 结构层仍为 0/4，层级完整挂载 0/670，正式 relation 0 条，Theme／Topic 均未实体化。
- 田自秉 2010 册尚有 32 个 `procedure` 候选待处理；六册剩余 `needs_evidence` unit 候选 2,396 个，其中 procedure 77 个（田自秉 32、李立新 10、夏燕靖 2016 35）；另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 下一批应续接田自秉 2010 册第 16—30 个 `procedure` 候选（秦兵马俑模塑、汉代漆器十一工种、漆器木胎三作法、画像石剔地法、六朝青瓷装饰六法等）。
- 本批临时脚本（`_tmp_tianzibing_procedurese_emit.py`、`_tmp_tianzibing_procedurese_verify.py`、`_tmp_update_tianzibing_procedurese_manifest.py`、`_tmp_pre_e_*.md`、`_tmp_pre_e_hashes.json`、`_tmp_closure_e.log`、`_tmp_pytest_e.log`、`_tmp_pytest_e.xml` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
