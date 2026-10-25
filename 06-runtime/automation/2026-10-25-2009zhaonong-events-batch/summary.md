# 赵农《中国艺术设计史》2009 册事件候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009zhaonong-events-batch/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从赵农《中国艺术设计史》（2009）的未分组 unit 候选中，取 23 个 `event` 候选逐条回读原文并作语义裁决。
- 20 个判 `create`，新建 event KU；3 个判 `no_delta`（靖康之变、1912 剪辫易服、1998 年专业目录调整，均已由既有 KU 完整覆盖）；无 `update`、无 `rejected`。
- KU 总数由 566 增至 586，event 类型由 72 增至 92；本批新增中 `historical_event` 17 条、`exhibition` 2 条、`discovery` 1 条。
- 候选索引投影后：applied 623、no_delta 39、rejected 801、needs_evidence 3,876；active 3,876、terminal 1,463。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地点 | 主要增量 |
|---|---|---|
| events/dayu-flood-control.md | 传说夏代，中国 | 引《孟子》《越绝书》记禹疏九河、以铜为兵凿伊阙；禹疏导、鲧堵塞对比；“疏胜于堵”成为政治文化规范 |
| events/yu-chuan-qi.md | 传说夏代 | 禹传位于启，禅让制度终结；来源评为“社会秩序的进步” |
| events/ji-zha-gift-sword.md | 春秋，徐国 | 季札心许徐君之剑，徐君死后解剑系冢树而去；“始吾心已许之” |
| events/yangjiacun-bronze-hoard-2003.md | 2003 年 1 月，陕西宝鸡眉县杨家村 | 出土 27 件青铜器、4000 个铭文，对西周历史有进一步明确记载 |
| events/shang-yang-reforms.md | 战国，秦国 | 变法使秦国崛起；来源以霸业建立在武器设计研制基础上作解 |
| events/wen-jing-zhi-zhi.md | 西汉中期 | 休养生息为汉武帝时代铺垫；鼓励民间经济，推动铁器时代全面到来 |
| events/sui-pinghui-jiankang.md | 589 年，建康 | 隋文帝灭陈后“建康城邑宫室，并平荡耕垦”；来源称政治性的根本摧毁 |
| events/feishui-zhizhan.md | 383 年 | 前秦与东晋对峙，以少胜多；南北较量结果形成南北朝局面 |
| events/xiaowendi-qian-du-luoyang.md | 北魏 | 自平城（山西大同）迁都洛阳；游牧民族向农业文明转化的一例 |
| events/xiaomingdi-fushi-gaige.md | 北魏后期 | 孝明帝改革服饰，“羽仪服式，悉如魏法”，江表士庶竞相模楷 |
| events/qianqiu-festival.md | 唐代，八月初五 | 传说唐玄宗定千秋节，以铜镜赠百官，民间以镜相赠成社会风尚 |
| events/chenqiao-mutiny.md | 960 年，陈桥驿 | 赵匡胤兵变建北宋；杯酒释兵权、守内虚外，皇帝集大权于一身 |
| events/wang-anshi-reforms.md | 宋神宗时 16 年 | 变法流产，新、旧、蜀、洛党争；“变法坏于制度之朽” |
| events/qingli-xinzheng.md | 庆历年间 | 范仲淹新政不能实施；使“先天下之忧而忧”有了更深刻的内容 |
| events/kangxi-ditu-cehui.md | 康熙时期 | 康熙领导完成中国地图测绘，当时具有世界先进水平 |
| events/jiawu-haizhan.md | 甲午年 | 来源列为洋务运动失败的军事标志，为后来中国经济改革带来无穷后患 |
| events/xinwenhua-yundong.md | 民国初期 | 陈独秀、胡适以《新青年》倡民主与科学、白话文；文化方向远离传统轨迹 |
| events/1851-wanguo-bolanhui.md | 1851 年，英国 | 钢铁玻璃结构“水晶宫”出现，揭开现代艺术设计序幕 |
| events/ma-gaerni-shihua.md | 1793 年，中国 | 马葛尔尼使华，600 箱工业科技产品，跪拜争议，和珅逐客拒绝贸易 |
| events/shanghai-expo-2010.md | 2010 年，上海 | 来源作于 2008 年，记“即将举行”与 1851—2010 年 159 年历史判断 |

## 三、no_delta 判定

| 候选 | 既有 KU | 覆盖依据 |
|---|---|---|
| cand-08-210 靖康之变 | events/jingkang-zhibian.md | 已记 1126—1127 年金人掳徽钦二帝、宋室南迁临安、与金划淮水大散关为界 |
| cand-11-155 剪辫子 | events/jianbian-yifu-1912.md | 已记 1912 年《剪辫通令》与《服制条例》颁行、衣冠等级制度被冲垮、中山装定为礼服 |
| cand-12-96 1998 年专业学科目录调整 | events/1998-moe-major-catalog.md | 已记 1998 年 7 月教育部本科专业目录调整、“工艺美术专业”改为“艺术设计专业” |

## 四、本批的判断

1. **事件与既有 KU 分工**：靖康之变、1912 剪辫易服、1998 年专业目录调整三项在既有 event KU 中已有同题专条且内容完整，判 `no_delta`，不重复建条。
2. **“顺带提及”不构成 no_delta**：1851 年万国博览会与马葛尔尼使华在既有 `events/opium-war.md` 中被提及，但只作为鸦片战争背景的一两句；本批仍为二者建专条，避免重大设计史节点被埋在更大事件条内。
3. **传说事件照录传说属性**：大禹治水、禹传启、千秋节三条均按来源的“传说”表述建条，不据外部考订改写为史实，也不补来源未给的年代。
4. **来源两处记载并列保留**：文景之治（“四五十年之后”与“西汉中期”）、王安石变法与庆历新政（正文与结论两处）、1851 年博览会（“万国博览会”与“世界博览会”两称）均并列照录，不代为拼合成单一表述。
5. **来源未载即写入证据边界**：甲午海战未给交战方、战场、舰船与公历年份；康熙地图测绘未给图名、范围与方法；2010 年上海世博会来源作于 2008 年，只记预期；三条均不引外部资料补全。
6. **维度判断**：D 维度 10 条（治水与王位制度、变法、都城、军事政治、宫廷节俗），E 维度 6 条（迁都、服饰汉化、对外战争、通商冲突、博览会），A 维度 2 条（季札赠剑的信义典故、新文化运动的文化转向），B 维度 2 条（青铜器出土、地图测绘）。维度按候选核心议题判定，不按年代机械分配。

## 五、本批的方法判断

- 23 个候选逐条回读原文段落，核对时间、地点、参与者、数量、引文与事件结果后再动笔；20 个新建候选对应 27 个来源行段，行段互不重复。
- 建条前比对 3 个判 no_delta 的既有 KU，以及 `events/opium-war.md`、`events/xiao-wen-gai-zhi.md`、`persons/dayu.md`、`publications/xin-qingnian.md` 等相邻条目，确认增量边界。
- 模板沿用事件 KU 的六节结构；`source_count: 1`、`confidence: medium`、`consensus: tentative`，不越级标 `high` 或 L1–L7。
- 本批在 `primary_dimension` 之外启用 `secondary_dimensions` 字段，记录跨维度归属；`hierarchy_scope_note` 与正文层级节同步说明。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析与六节结构检查，20/20 通过。
- 判定与写回分离：台账 69 行（23×3）、apply-plan 20 行、mapping 23 条，与磁盘、索引三方核对，0 错误。

## 六、状态与验证

- `candidate-decision-ledger.jsonl`：69 行，23 个候选各 3 行；终态 applied 20、no_delta 3。
- `apply-plan.jsonl`：20 行，均为 create，`before` 为 null；20/20 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：23 条（create 20、no_delta 3），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:83ce7412…`（applied 603、no_delta 36、needs_evidence 3,899、rejected 801），批后 `sha256:1d7195a2…`（applied 623、no_delta 39、needs_evidence 3,876、rejected 801）；重建幂等。
- 内容质量审计：586 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 586/586 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，events 92；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 20 条新建 KU 均为 `source_count: 1`（赵农 2009），未标 high confidence；单册事件叙述多为章节背景句，事实密度有限，后续若有第二来源应优先补证。
- 甲午海战、康熙地图测绘、2010 年上海世博会三条的事实边界最窄：来源分别只给名称与后果判断、领导者与世界先进水平评价、预期举办地与年份，KU 保留空位而不补外部史实。
- 结构层仍为 0/4，层级完整挂载 0/586，正式 relation 0 条，Theme／Topic 均未实体化。
- 六册剩余 `needs_evidence` unit 候选 2,513 个，其中 event 43 个（田自秉 22、李立新 11、夏燕靖 2009 10）；另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_zhaonong_events_a.py`、`_tmp_zhaonong_events_b.py`、`_tmp_zhaonong_events_c.py`、`_tmp_zhaonong_events_emit.py`、`_tmp_zhaonong_batch_emit.py`、`_tmp_zhaonong_batch_verify.py`、`_tmp_update_zhaonong_manifest.py` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
