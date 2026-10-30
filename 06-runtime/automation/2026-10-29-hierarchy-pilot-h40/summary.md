# h40 金银器与珐琅线：B.9.5「金银器与金属胎珐琅：细工、器类与珐琅工艺」

## 一、目标与范围

本批在既有 Theme B.9「青铜与金属：器形、铸造与装饰」内新建第五个 Topic B.9.5「金银器与金属胎珐琅：细工、器类与珐琅工艺」，并主挂载 20 个金银器、细工与珐琅 KU。不改 B.9.1／B.9.2／B.9.3／B.9.4 的既有挂载，不新建 Theme，不新建 Dimension。

范围限定为六册 Markdown 文本中的金银器与金属胎珐琅材料：五个名物条目（花丝、花丝工艺、金细工艺、景泰蓝、画珐琅）、两个工序条目（景泰蓝制作七过程、银熏炉制作工序）与十三件器物（战国螭纹金盏与镂空金匙、西汉鎏金银竹节高柄铜薰炉、唐刻花金碗、唐银香囊、唐论语玉烛、唐文思院造鎏金朵带银熏炉、辽荷叶敞口银杯、宋乳钉狮纹鎏金银盏、元四合如意金盘、元银果盒、元银镜架、元朱碧山银槎、清画珐琅葵花式盘）。

基线：v1.30（24 Theme／75 Topic／565 membership／558 complete／2012 incomplete／relation 7121／member_of 1123／isolated 1247／ksq 57/65／structural 130）。

## 二、结构物化

`04-knowledge/structure/topics/b9-jinyinqi-yu-jinshutai-falang-xigong-qilei-yu-falang-gongyi.md`

- `node_type: topic`、`parent_theme: B.9`、`primary_dimension: B`、`secondary_themes: [C, D]`、`status: pilot`、`date: 2026-10-29`。
- `research_question` 178 字（171–185 区间内），以「细工名—器物—胎珐琅三层能否排成技术序列」与「三套命名是否同源」为问题骨架。
- 七节 body：研究问题 / 边界（12 条）/ 支撑材料（20 行表格）/ 理论支撑 / 实证材料支撑 / 文献支撑 / 未解决问题（19 条）。
- 三层组织：细工名（花丝、花丝工艺、金细工艺）—器物（战国至清十三件金银器）—胎珐琅（景泰蓝、画珐琅、景泰蓝七步、银熏炉工序）。
- 命名理由：不叫「金银器史」或「珐琅工艺」，因为六册提供的是工艺名、朝代器物与胎珐琅名目三套互不校对的条目，而不是一条从胎体到表面的技术序列；「金银器与金属胎珐琅」保留材料与胎体范围，副题列出细工、器类与珐琅三层。

## 三、20 个 KU 挂载

全部为主挂载，`primary: true`；`secondary_memberships` 为 0。

| KU | 类型 | role | 承担什么 |
|---|---|---|---|
| `terms/huasi` | term | `term_anchor` | 花丝通名：金银细丝、编堆穿镶錾五类技法、盘盆瓶炉与首饰、北京上海成都三产地 |
| `terms/hua-si-gong-yi` | term | `term_anchor` | 西晋花丝断代：细丝盘绕花形、洛阳金村／宜兴／南京栖霞山三批出土、「错采镂金」总评 |
| `terms/jinxi-gongyi` | term | `term_anchor` | 元代金器以掐、累、镶嵌为尖端；五品以上用金玉茶酒器的制度限制；无实例与工序 |
| `terms/jingtai-lan` | term | `term_anchor` | 铜胎掐丝珐琅的学名与俗称、景泰年间最精、明清生产与清代釉色演变、北京产地 |
| `terms/hua-falang` | term | `term_anchor` | 画珐琅与掐丝珐琅的分工、田自秉「演进非外来」判断、康乾时期、白里蓝底通例、造办处与广东 |
| `procedures/jingtailan-zhizuo` | procedure | `procedure` | 制胎、掐丝、烧焊、点蓝、烧蓝、磨光、镀金七步与白芨糊、焊药、点烧三次以上 |
| `procedures/yin-xunlu-zhizuo` | procedure | `procedure` | 文思院炉的钣金成型、附件浇铸、纹饰涂金三道工序与盖身、莲瓣镂空、五兽足、朵带装配 |
| `works/yichiwen-jinzhan-loukong-jinshi` | work | `representative_work` | 战国随县「单纯用金银制作器皿」例证；图注「蟻螭纹」照录存疑 |
| `works/liujin-yinzhu-jie-xunlu` | work | `representative_work` | 西汉茂陵、高 58 厘米、五节竹节柄与蟠龙座、盖口字铭记器名重量与制作输送年份 |
| `works/kehua-jinwan` | work | `representative_work` | 唐早期何家村金碗：两层莲瓣纹切分装饰区，内填鸳鸯鹦鹉鹿狐与珍珠地 |
| `works/tang-yin-xiangnang` | work | `representative_work` | 唐银香囊：同心圆机环与活轴保持金盂平衡；法门寺 12.8 厘米；香囊／熏球／香球三名并存 |
| `works/lunyu-yuzhu` | work | `representative_work` | 丹徒丁卯桥唐银器：龟座负筒、龙凤卷草、「论语玉烛」四字、五十支银酒筹 |
| `works/wensiyuan-yin-xunlu` | work | `representative_work` | 法门寺地宫、咸通十年文思院造铭文、29.5×25.9×7 厘米、5.363 千克；295 厘米异文并列 |
| `works/heye-changkou-yinbei` | work | `representative_work` | 辽巴林窖藏：荷叶敞口、内壁曲线细纹、注水如涟漪；尺寸与藏地无载 |
| `works/ruding-shishi-liujin-yinzhan` | work | `boundary_case` | 宋代图注孤证：图 7-29 同时指乳钉狮纹盏与德阳圆球镂空银熏炉，图号两指 |
| `works/sihe-ruyi-jinpan` | work | `representative_work` | 1959 年吴县元墓：四个如意头组成四瓣花式、柿蒂纹中心、西番莲缠枝 |
| `works/yinguohe` | work | `representative_work` | 1955 年合肥元窖藏：十莲瓣、盖格底三部分、重 76 两、双凤折枝与十种折枝花 |
| `works/yuan-yinjingjia` | work | `representative_work` | 1964 年苏州张士诚父母墓：折叠前后支架、32.8×17.8 厘米、仿木构镶三片雕镂银皮 |
| `works/zhu-bishan-yincha` | work | `representative_work` | 朱碧山银槎：15.2×19.8 厘米、老树槎形与老者、至正乙酉（1345）年款、七言诗与印 |
| `works/hua-falang-kuihua-pan` | work | `representative_work` | 清代画珐琅图注孤证：插图 4「画珐琅葵花式盘（清）」，葵花式为唯一造型信息 |

## 四、边界处置

- 鎏金、错金银与错铜、错石、刻划、金银平脱等表面装饰工序归 B.9.4；本 Topic 只在器物铭文、器形与「鎏金」「涂金」描述处引用。
- 青铜容器的器形、礼器组合与铭文内容归 B.9.1；金银器不是青铜礼器，不并入鼎簋鬲甗序列。
- 铜镜的型式、纹样与铸镜归 B.9.3；银镜架只取折叠支架与雕镂银皮，不并入铜镜谱系。
- 珐琅彩（瓷胎画珐琅）归 B.6；本 Topic 只处理金属胎珐琅，不把瓷胎与铜胎混为一类。
- 搪瓷工业、新中国的花丝机械化与液化石油气焊、景泰蓝的文革生产史只在名物条目尾部出现，本 Topic 不展开。
- 金银器纹样母题、器形审美与图像叙事归 C；本 Topic 只取纹饰的工艺归属与器物著录。
- 文思院、造办处珐琅作、金银铺与五品以上用金玉茶酒器等作坊与制度史归 D（D.6／D.1）；本 Topic 只把铭文、产地与制度句作器物的制作背景。
- 金饼、银锭、金银作为财富宝藏与货币替代品的经济史材料不纳入；宋器条目中的「输辽、西夏用于结算」只作时代背景。
- 辽、宋、元金银器的区域类型学与窖藏逐件清单不建立；本 Topic 每代只取一至四件单器锚点。
- 花丝（`terms/huasi`）与花丝工艺（`terms/hua-si-gong-yi`）是同一工艺名的通名条与西晋断代条，来源未说明是否应合并；本 Topic 分列并登记 reconcile 候选。
- 银熏炉是同名异器的器型名：西汉竹节炉、唐文思院炉、唐银香囊（熏球）与宋德阳圆球炉不是同一件器物；本 Topic 只取前三类中有独立 KU 的器物。
- 不据「精巧」「细致」「繁密」推算丝径、金层厚度、釉料配比、烧成温度或工时；六册唯一的完整工序链是景泰蓝七步。

## 五、执行与验证

1. `scripts/hierarchy_stress_test.py`：v1.31、2570 KU、24 Theme、76 Topic、585 membership、578 complete、1992 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`（试点态）。
2. `scripts/build_relation_index.py`：7161 条（explicit 5998、inferred_by_rule 1163、migrated 0），类型覆盖 3/67。
3. `scripts/write_current_health.py`：v1.31、complete 578、missing 1992、relation 7161、isolated 1233、structural 130/130、ksq 57/65、rule_drift 0、system_p0 0。
4. 20 个 KU 逐一复核：`primary_theme: B.9`、恰好 1 条 `topic_memberships`、role 与计划一致、frontmatter 与 body 各恰好 1 个 `hierarchy_scope_note`、`updated: 2026-10-29`。
5. Topic 复核：`node_type: topic`、`parent_theme: B.9`、`research_question` 178 字、七节齐备、支撑表 20 行、未解决问题 19 条。
6. 文档复核：Topic 76、B.9 下 5 个、B.9 主挂载 71 KU、全库未挂载 1992；`topics/README.md` 与 `themes/README.md` 的 B.9 段已补 B.9.5。

## 六、指标变化

| 指标 | v1.30（基线） | v1.31（结果） | 变化 |
|---|---:|---:|---:|
| Theme | 24 | 24 | 0 |
| Topic | 75 | 76 | +1 |
| Topic membership | 565 | 585 | +20 |
| 完成挂载 KU | 558 | 578 | +20 |
| 未挂载 KU | 2012 | 1992 | −20 |
| relation index | 7121 | 7161 | +40 |
| `member_of` | 1123 | 1163 | +40 |
| 隔离单元 | 1247 | 1233 | −14 |
| structural health | 130/130 | 130/130 | 0 |
| knowledge structure quality | 57/65 | 57/65 | 0 |

relation 增量 40 = 20 条 topic `member_of` + 20 条 theme `member_of`。隔离单元只减 14，因为 20 个新挂载 KU 中 6 个原已有显式关系。

## 七、语义边界（并列不裁）

1. **三层不能排成技术序列**：细工名、器物、胎珐琅之间没有一件共同器物，六册也没有「胎体—细工—表面」的工序次序；三层是整理框架，不是来源结论。
2. **花丝与花丝工艺两条同名条目未合并**：一条是通名与近现代技法，一条是西晋断代与出土物；来源未说明是否同一工艺的不同层次，本批分列并登记 reconcile 候选。
3. **银熏炉同名异器**：西汉竹节高柄炉、唐文思院炉、唐银香囊（熏球）与宋德阳圆球炉四类器物的形制、尺寸与用途不同，六册没有统一类型学。
4. **文思院炉尺寸两说**：夏燕靖记通高 29.5 厘米、腹深 7 厘米，李立新记 295 厘米、70 厘米；两册重量一致（5363 克＝5.363 千克），长度相差十倍，照录不径改。
5. **唐银香囊三名与三径**：高丰称「银熏球」、夏燕靖称「银香囊」、李立新图注称「鎏金忍冬纹镂孔银香球」；法门寺 2 件、沙坡村 4 件、何家村 1 件，直径 12.8、5.4、4.5 厘米三种记录。
6. **宋乳钉狮纹盏图号两指**：图 7-29 同时被指为乳钉狮纹鎏金银盏与德阳圆球镂空银熏炉，`confidence` 为 low，只作 boundary_case。
7. **画珐琅来源判断未调和**：田自秉说画珐琅是掐丝珐琅的演进、并非外来，同段又记乾隆出现西洋装饰风格的作品；来源未给珐琅料成分、胎体做法或工匠谱系的中外比较。
8. **景泰蓝命名史只有一句**：「景泰蓝」一词辛亥革命前后才采用，未给文献依据；「以景泰年间最精」没有器物清单与款识统计。

## 八、生成态与门禁

- 工作包建立后运行 `scripts/run_sync_closure.py --refresh-generated --full`，执行 18 步闭包（250 tests + 16 subtests）。
- 生成态顺序陷阱：第 8 步写 health 早于第 9 步重建 05-outputs 导航；relation 数变化时首次闭包可能记 `output_navigation_snapshot_stale`（rule_drift 1），需重跑 `scripts/write_current_health.py` 后再全量闭包一次。
- `--refresh-generated --check-generated` 用于发布门禁；工作区未提交时第 17 步 `[17/17] FAILED (exit=1)` 为预期，不作为本批失败。
- apply-plan 26/26 行须逐一复核 `after_sha256` 与磁盘字节一致；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 须零改动。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。

## 九、未决事项与下一跳

- 19 条未解决问题见 Topic 的「未解决问题」节与 `manifest.json.unresolved`，集中于工序参数缺失、同名异器、尺寸异文与来源分布不均。
- 16 条单源：花丝、花丝工艺、金细工艺、画珐琅、景泰蓝七过程、银熏炉工序、战国金盏金匙、西汉竹节炉、唐刻花金碗、唐论语玉烛、辽荷叶杯、宋乳钉盏、元金盘、元银果盒、元朱碧山槎、清画珐琅盘。
- 来源分布：田自秉 11 条，夏燕靖两版合计 10 条，李立新 3 条，高丰 3 条；赵农 2009 册不在本批来源中。
- 下一跳：B.9 兵器 Topic（戈、矛、钺、剑、戟、弩）；其后为乐器 Topic（编钟、八音、十二平均律）、铁器与叠铸 Topic、漆器 Theme。
- 新增 reconcile 候选：`terms/huasi` 与 `terms/hua-si-gong-yi` 同名异层；既有的 6 组重复候选与 12 条图注待核仍按原清单排队。
- 存量债务不变：全库未挂载 1992、隔离 1233、单源与低置信条目按既有 backlog 处理。
