# h41 兵器与甲胄线：B.9.6「兵器与甲胄：长兵、短兵、远射与防护」

## 一、目标与范围

本批在既有 Theme B.9「青铜与金属：器形、铸造与装饰」内新建第六个 Topic B.9.6「兵器与甲胄：长兵、短兵、远射与防护」，主挂载 20 个兵器、甲胄与造作 KU，并以次挂载承接越王勾践剑的兵器一面。不改 B.9.1／B.9.2／B.9.3／B.9.4／B.9.5 的既有挂载，不新建 Theme，不新建 Dimension。

范围限定为六册 Markdown 文本中的兵器、甲胄与造作材料：十三个器名与形制条目（戈、矛、钺、戟、铍、青铜剑、殳、钩镶、环首刀、弩、汉代铠甲、明光铠、筒袖铠）、两个造作条目（造剑、造甲）与五件器物（吴王夫差矛、人面纹铜钺、铁刃铜钺、玉柄铁剑、神臂弓）。

基线：v1.31（24 Theme／76 Topic／585 membership／578 complete／1992 incomplete／relation 7161／member_of 1163／isolated 1233／ksq 57/65／structural 130）。

## 二、结构物化

`04-knowledge/structure/topics/b9-bingqi-yu-jiazhou-changbing-duanbing-yuanshe-yu-fanghu.md`

- `node_type: topic`、`parent_theme: B.9`、`primary_dimension: B`、`secondary_themes: [D, C]`、`status: pilot`、`date: 2026-10-29`。
- `research_question` 179 字（171–185 区间内），以「这些条目能否排成从长兵到防护的装备序列，还是各自孤立的名物层」与「来源四册是否共用同一分类」为问题骨架。
- 七节 body：研究问题 / 边界（13 条）/ 支撑材料（20 行表格）/ 理论支撑 / 实证材料支撑 / 文献支撑 / 未解决问题（19 条）。
- 三层组织：长兵（戈、矛、钺、戟、铍、殳）—短兵与远射（青铜剑、环首刀、弩、钩镶）—防护与工序（汉代铠甲、筒袖铠、明光铠、造剑、造甲），另有五件器物锚点。
- 命名理由：不叫「兵器史」或「甲胄工艺」，因为六册提供的是器名条、形制条与朝代工序条三套互不校对的条目，而不是一条从长兵到防护的装备序列；「兵器与甲胄」保留器类与防护范围，副题列出长兵、短兵与远射、防护与工序三层。

## 三、20 个 KU 挂载

20 条全部为主挂载，`primary: true`；另有 1 条次挂载（越王勾践剑），`secondary_memberships` 为 1。

| KU | 类型 | role | 承担什么 |
|---|---|---|---|
| `terms/ge-dagger-axe` | term | `term_anchor` | 镰形农具渊源、戈头援内胡三部、二里头青铜戈、安阳 320 件、直内戈曲内戈与西周胡戈 |
| `terms/mao` | term | `term_anchor` | 石木角矛到青铜矛、矛头七部位、殷墟 700 余支、酋矛夷矛长度、春秋血槽与南阳铁矛 |
| `terms/yue-battle-axe` | term | `term_anchor` | 石斧渊源、《说文》大小之别、穿绳与銎孔之分、良渚玉钺与妇好墓 9 公斤双虎食人钺 |
| `terms/ji-halberd` | term | `term_anchor` | 戈矛复合、蒿城最早青铜戟、西周合铸、贵族使用、燕下都 12 件铁戟与卜形戟 |
| `terms/pi-sword-spear` | term | `term_anchor` | 剑形长兵、禁卫用途、《史记》「人皆持铍」、与矛剑比较、失传与秦俑坑实证 |
| `terms/jian-sword` | term | `term_anchor` | 剑身剑柄八部位、蚩尤造剑传说、商晚期北方短剑、沣镐柳叶形剑、30 厘米以内与车战近搏 |
| `terms/shu-staff` | term | `term_anchor` | 无刃长兵与五兵、圆球与棱刺殳头、仪仗与杖杀、曾侯乙墓三棱矛形铜殳头通长 3.30 米 |
| `terms/gou-xiang` | term | `term_anchor` | 东汉特殊盾牌：缩小的铁盾、盾中短锥、上下铁钩与盾后手柄，攻防一体 |
| `terms/huan-shou-dao` | term | `term_anchor` | 刀柄铸环、刀长 100 厘米、骑步兵手持、汉代代替铁剑、剑退为官员佩饰 |
| `terms/nu-crossbow` | term | `term_anchor` | 臂弓机三部分、竹弓硬木臂、扳机与钩心、秦汉弩机、汉代加刻度 |
| `terms/han-armor` | term | `term_anchor` | 铁甲为主、鱼鳞甲与札甲、秦俑甲衣多样、兜鍪盆领膝甲三型与将士服饰的等级原则 |
| `terms/mingguang-kai` | term | `term_anchor` | 北周新兴形制、胸背左右两块圆护、俗称护心镜、与筒袖铠衲裆铠并列为三种基本形制 |
| `terms/tong-xiu-kai` | term | `term_anchor` | 晋代形制：小块鱼鳞或龟背甲片前后连缀成筒形甲身、护肩装筒袖、头盔仍称兜鍪 |
| `procedures/zao-jian` | procedure | `procedure` | 宋代造剑的材料选择：不用太钢劲的钢材、剑身以柔铁为主、百炼成钢、以弹力与韧性为取向 |
| `procedures/zao-jia` | procedure | `procedure` | 宋代造甲的坚固程度：「五十步强弩射之不能入」、箭自钻空钻穿而铁皆反卷、与造弩技术联动 |
| `works/wu-wang-fuchai-spear` | work | `representative_work` | 春秋江陵楚墓、长 29.5 厘米、宛如短剑、矛脊铸血槽、错金铭文「吴王夫差自作用口」 |
| `works/shenbi-gong` | work | `representative_work` | 北宋强弩：「射三百步，能洞重札」、郓州铜弩机、望山与小矩、勾股法计算 |
| `works/human-face-bronze-yue` | work | `boundary_case` | 殷商兵器上的怪诞纹饰评述「神秘甚至恐怖」，形制、尺寸与出土无载 |
| `works/iron-blade-bronze-yue` | work | `boundary_case` | 商代陨铁锻刃嵌青铜身的过渡证据：藁城台西村与平谷刘家河各 1 件 |
| `works/jade-handle-iron-sword` | work | `boundary_case` | 西周晚期人工冶铁的上限证据：三门峡虢国墓、正文玉柄与知识链接铜柄两说 |

role 分布：`term_anchor` 13、`procedure` 2、`representative_work` 2（吴王夫差矛、神臂弓）、`boundary_case` 3（人面纹铜钺、铁刃铜钺、玉柄铁剑）。类型分布：term 13、procedure 2、work 5。

次挂载：`works/yuewang-goujian-jian`（version 2→3），新增 `topic_memberships` 第二条 `primary: false`，role 为 `representative_work`；`scope_note` 限定为「只追加兵器形制、防锈三因与吴越冶剑谱系一面；剑格错石仍归 B.9.4，剑柄珐琅釉仍归 B.9.5，三说的部位与材料并列不裁」。

## 四、边界处置

- 青铜容器的器形与礼器组合归 B.9.1，合范、浑铸、分铸、失蜡与六齐归 B.9.2；本 Topic 不把兵器的装柄、铸造写入工序序列。
- 铜镜的型式、纹样与铸镜归 B.9.3；印纹、镶嵌、错金银与鎏金等表面装饰归 B.9.4；花丝、景泰蓝与金银器归 B.9.5。
- 玉钺的礼制义归 B.8.4；本 Topic 只取钺的石斧渊源、穿绳与銎孔之别与妇好墓实例。
- 冶铁技术史（陨铁、块炼铁、铁范、叠铸、百炼钢、炒钢）归后续铁器与叠铸 Topic；铁刃铜钺与玉柄铁剑只作战器边界，燕下都 12 件铁戟与南阳铁矛只作形制对照引用。
- 弓箭、箭器、火药、火铳与旋风炮不纳入；六册相关内容不成器名序列，无法逐条挂载。
- 车战编制、战车、斧车与战船属编制与交通工具，不纳入本 Topic。
- 甲胄与服饰的等级关联归服饰 Theme；汉代铠甲的服饰段材料只作并列陈述，不与兵器段合并为统一分类。
- 季札赠剑（`events/ji-zha-gift-sword`）`primary_dimension` 为 A，属叙事事件，不挂载。
- 春秋战国青铜炊食器十类合条与单器条重叠，本批不挂载、登记为后续合并候选，沿用 h28 起的既有登记。
- 兵器纹样母题与人面纹构图解释归 C；本 Topic 只取器名、形制与工序。
- 不据「锋利」「坚固」「杀伤力大」推算硬度、含碳量、拉力、射程、工时或成品率；造剑、造甲两条工序 `confidence` 均为 low。

## 五、执行与验证

1. `scripts/hierarchy_stress_test.py`：v1.32、2570 KU、24 Theme、77 Topic、606 membership、598 complete、1972 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`（试点态）。
2. `scripts/build_relation_index.py`：7202 条（explicit 5998、inferred_by_rule 1204、migrated 0），类型覆盖 3/67。
3. `scripts/write_current_health.py`：v1.32、complete 598、missing 1972、relation 7202、isolated 1220、structural 130/130、ksq 57/65、rule_drift 0。
4. 21 个 KU 逐一复核：`primary_theme: B.9`、主挂载恰好 1 条并在 frontmatter 与 body 各出现 1 次、role 与计划一致、frontmatter 与 body 各恰好 1 个 `hierarchy_scope_note`／`scope_note`、`updated: 2026-10-29`、无残留「Theme/Topic 尚未 materialize。」标记。
5. Topic 复核：`node_type: topic`、`parent_theme: B.9`、`research_question` 179 字、七节齐备、支撑表 20 行、未解决问题 19 条。
6. 文档复核：Topic 77、B.9 下 6 个、B.9 主挂载 91 KU（term_anchor 38／representative_work 32／procedure 15／boundary_case 6，按磁盘实测）、全库未挂载 1972；`topics/README.md`、`themes/README.md`、`hierarchy/index.md` 与 `dimension-candidates.md` 的 B.9 段均已补 B.9.6。
7. 归档：`04-knowledge/structure/hierarchy/archive/v1.31.md`（59569 字节），与改动前 `index.md` 逐字节一致，在改 `index.md` 之前复制。

## 六、指标变化

| 指标 | v1.31（基线） | v1.32（结果） | 变化 |
|---|---:|---:|---:|
| Theme | 24 | 24 | 0 |
| Topic | 76 | 77 | +1 |
| Topic membership | 585 | 606 | +21 |
| 完成挂载 KU | 578 | 598 | +20 |
| 未挂载 KU | 1992 | 1972 | −20 |
| relation index | 7161 | 7202 | +41 |
| `member_of` | 1163 | 1204 | +41 |
| 隔离单元 | 1233 | 1220 | −13 |
| structural health | 130/130 | 130/130 | 0 |
| knowledge structure quality | 57/65 | 57/65 | 0 |

relation 增量 41 = 20 条 topic `member_of` + 20 条 theme `member_of` + 1 条次挂载 topic `member_of`。membership 增量 21 = 20 条主挂载 + 1 条次挂载。隔离单元只减 13，因为 20 个新挂载 KU 中 7 个原已有显式关系。

## 七、语义边界（并列不裁）

1. **三层不能排成装备序列**：长兵、短兵与远射、防护与工序之间没有一件共同的攻防对应，六册也没有「攻—防—工序」的对应记载；三层是整理框架，不是来源结论。
2. **戈与钺的渊源方向两说**：戈条记「戈后来发展为钺、戟、矛、殳」，同书钺条记「从石斧中发展起来」；一处把钺列为戈的后继，一处把钺归石斧，两存不裁。
3. **酋矛兵种两说**：同一册一处称酋矛为步兵所用、长 2 丈，另一处把酋矛列为车兵常规利器（身高 1.5 倍），前后不一致，两存待考。
4. **甲胄三条只有形制名**：筒袖铠的甲片尺寸、编缀材料与筒袖长度无载；明光铠的两块圆护直径、铜铁之别与抛光工艺无载；汉代铠甲的鱼鳞甲与札甲只有名称，没有甲片规格与编缀方式。
5. **汉代铠甲两段主题未合并**：兵器段讲材质与类型，服饰段讲秦俑、汉俑的甲衣、等级与防护，来源自己标明主题不同，并列呈现不合成统一分类。
6. **玉柄铁剑柄部材质两说**：正文作「玉柄铁剑」，同章知识链接作「铜柄铁剑」，来源未交代是否同一件，照录并列不代为判定。
7. **神臂弓与弩的记载分属两册两处**：一册给臂弓机结构与汉代刻度，同册另引《梦溪笔谈》给神臂弓性能与望山小矩；刻度加在弩机哪个部件、单位为何未说明，不得写成现代瞄准具。
8. **原文用字未统一**：「秘」疑为「柲」、戈条作「镈」而通行作「鐏」、殳条首句「反」为「殳」之误、戟条「蒿城」通行作「藁城」、钺条首句「钱」为「钺」之误；已标疑照录，未径改。

## 八、生成态与门禁

- 工作包建立后运行 `scripts/run_sync_closure.py --refresh-generated --full`，执行 18 步闭包（250 tests + 16 subtests）。
- 生成态顺序陷阱：第 8 步写 health 早于第 9 步重建 05-outputs 导航；relation 数变化时首次闭包记 `output_navigation_snapshot_stale`（rule_drift 1，05-outputs/index/index.md 声明 relation 7161、期望 7202），重跑 `scripts/write_current_health.py` 后再全量闭包一次，rule_drift 归零。
- `--refresh-generated --check-generated` 用于发布门禁；工作区未提交时第 17 步 `[17/17] FAILED (exit=1)` 为预期，不作为本批失败。
- apply-plan 27/27 行须逐一复核 `after_sha256` 与磁盘字节一致；保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 须零改动。
- 本批不 commit、不 push；HEAD 仍为 `c249c6fe`。

## 九、未决事项与下一跳

- 19 条未解决问题见 Topic 的「未解决问题」节与 `manifest.json.unresolved`，集中于工序参数缺失、甲胄无规格、用字异文与来源分布不均。
- 19 条单册来源：除明光铠有同一作者两版互证外，其余 19 条均为单册支撑。来源分布：赵农 2009 册 15 条（戈、矛、钺、戟、铍、青铜剑、殳、钩镶、环首刀、弩、汉代铠甲、造剑、造甲、吴王夫差矛、神臂弓），夏燕靖 2016 册独覆盖 3 条（人面纹铜钺、铁刃铜钺、玉柄铁剑），筒袖铠由夏燕靖 2009 册独覆盖；高丰 2004、田自秉 2010、李立新 2011 三册无直接来源。
- 时段与空白：本 Topic 止于北宋，东汉至隋唐之间无兵器条目，甲胄形制止于北周；宋以后甲胄、火器与冷热兵器交替不在六册范围内。
- 下一跳：B.9 乐器 Topic（编钟、八音、十二平均律）；其后为铁器与叠铸 Topic（生铁冶铸、铁范、叠铸、百炼钢与炒钢）、B.9 货币与农具 Topic、漆器 Theme、前近代服饰与甲胄等级 Theme。
- 既有重复候选（8 组）与图注单条待核 12 条仍按原清单排队；本批不新增重复候选。
- 存量债务更新：全库未挂载 1972、隔离 1220、单源与低置信条目按既有 backlog 处理。
