# h38 铜镜线：B.9.3「铜镜：型式、纹样与铸镜」

## 一、目标与范围

本批在既有 Theme B.9「青铜与金属：器形、铸造与装饰」内新建第三个 Topic B.9.3「铜镜：型式、纹样与铸镜」，并主挂载 13 个铜镜 KU。不改 B.9.1／B.9.2 的既有挂载，不新建 Theme，不新建 Dimension。

范围限定为六册 Markdown 文本中的铜镜材料：通名（铜镜）、四个断代条目（汉镜、六朝铜镜、唐镜、宋镜）、两个专门类型（规矩镜、透光镜）、一个光学边界条目（阳燧）与五件器物（伍子胥画像镜、龙纹葵花镜、双鸾瑞兽葵花镜、花鸟人物螺钿镜、玉平脱双葡萄镜）。

基线：v1.28（24 Theme／73 Topic／534 membership／527 complete／2043 incomplete／relation 7059／member_of 1061／isolated 1263／ksq 57/65／structural 130）。

## 二、结构物化

`04-knowledge/structure/topics/b9-tongjing-xingzhi-wenyang-yu-zhuzao.md`

- `node_type: topic`、`parent_theme: B.9`、`primary_dimension: B`、`secondary_themes: [C, D]`、`status: pilot`、`date: 2026-10-29`。
- `research_question` 184 字（171–185 区间内），以铜镜起点三说、四期说、汉镜厚薄两说与「无一件尺寸」为问题骨架。
- 七节 body：研究问题 / 边界 / 支撑材料（13 行表格）/ 理论支撑 / 实证材料支撑 / 文献支撑 / 未解决问题（16 条）。
- 三层组织：型式（镜式、钮制、曲率、厚薄）—纹样（战国八类、汉规矩四神与铭文、六朝四类、唐五类、宋缠枝与联珠）—铸镜（楚、绍兴、扬州、湖州饶州铸镜局、七种装饰工艺）。
- 命名理由：不叫「铜镜史」或「汉唐铜镜」，因为六册提供的是三套互不校验的名称与著录，而不是一条连续发展线；「型式、纹样与铸镜」对应材料实际回答的三组问题。

## 三、13 个 KU 挂载

全部为主挂载，`primary: true`；`secondary_memberships` 为 0。

| KU | 类型 | role | 承担什么 |
|---|---|---|---|
| `terms/tongjing` | term | `term_anchor` | 通名、起源三说、战国四大特点、鉴水到鉴镜、四期说、南北两系、八类战国纹样、唐镜形制与纹饰 |
| `terms/hanjing` | term | `term_anchor` | 体薄平边圆钮与三期、加大增厚、半球钮柿蒂座、铭文镜、规矩四神镜、商标、透光镜 |
| `terms/liuchao-tongjing` | term | `term_anchor` | 早晚工艺差、龙虎／翔鹤飞鸿／兽形生肖三镜、绍兴浮雕、工匠姓氏与纪年、私人商品生产 |
| `terms/tangjing` | term | `term_anchor` | 扬州贡镜、七种装饰加工、70:25:5、镜面微凸与沈括 |
| `terms/song-jing` | term | `term_anchor` | 铜料紧张、早晚与轻薄胎、旋转式缠枝花草、联珠纹、五种镜式、铸镜局、素地阴刻款、铜禁携带 |
| `terms/guijujing` | term | `term_anchor` | TLV 与六博棋格、四神、镜缘纹样、方座八乳、流行最长 |
| `terms/touguang-jing` | term | `term_anchor` | 西汉透光镜、镜背影像、铸造应力与研磨压应力、上博「内清质以昭明」、隋唐流传 |
| `terms/yang-sui-burning-mirror` | term | `boundary_case` | 凹面取火镜、西周普遍使用、《庄子》两鉴相照，只作光学边界 |
| `works/wu-zixu-huaxiang-jing` | work | `representative_work` | 绍兴画像镜、浮雕五人物、上博藏、历史题材首见 |
| `works/longwen-kuihua-jing` | work | `representative_work` | 图 6-4 图注一行，唐龙纹葵花镜锚点，confidence low |
| `works/shuangluan-ruishou-kuihua-jing` | work | `representative_work` | 图 6-32 双鸾瑞兽葵花镜与同页唐镜工艺总结 |
| `works/huaniao-renwu-luodian-jing` | work | `representative_work` | 1956 洛阳唐墓、弹琴听琴侍童、细线刻划、松石屑填饰 |
| `works/yu-pingtuo-shuang-putao-jing` | work | `representative_work` | 五代前蜀王建墓镜匣、漆平脱双玉葡萄、跨材质 |

role 分布：`term_anchor` 7、`boundary_case` 1、`representative_work` 5。类型分布：term 8、work 5。版本递增：`terms/tongjing` 2→3，其余 12 个 1→2；13 个 KU 的 `updated` 均为 2026-10-29。

## 四、边界处置

1. **阳燧只作边界**：凹面取火镜与照容镜同用「鉴」字而功能不同，来源未打通称名演变，故以 `boundary_case` 挂载、不并入铜镜型式序列。
2. **容器器形与铸造工序归 B.9.1／B.9.2**：本 Topic 不重复鼎、簋、鬲、甗、爵、觚、尊、壶、豆与合范、浑铸、分铸、失蜡、六齐。
3. **纹样与铭文归 C**：铜镜纹样的图像母题、铭文书法与文例不在 B.9.3 展开，只取型式与谱系著录。
4. **铸镜局与铜禁归 D.6**：湖州、饶州铸镜局与「有刻款才可携带」只作产地与制度线索，不写制度史。
5. **玻璃镜归 B.7**：宋代以后玻璃镜传入只作铜镜衰落背景，不并入本 Topic。
6. **其他日用铜器归后续**：汉代铜灯、博山炉、铜洗等不入 B.9.3。
7. **不推算数值**：六册无合金检测、曲率半径、焦距与尺寸，本 Topic 不据「微凸」「轻薄」换算毫米或度。

## 五、执行与验证

1. 13 个候选全部逐条复读，确认 `primary_dimension: B`、无 `primary_theme`、无 `topic_memberships`。
2. 写入 B.9.3 结构文件；断言 `research_question` 184 字、支撑表 13 行、13 个相对链接均指向存在文件。
3. 结构化挂载 13 个 KU；逐文件断言唯一 `primary_dimension: B`、无既有 `primary_theme`／`topic_memberships`、`hierarchy_scope_note` 唯一；用 YAML 解析复核 `primary_theme`、`topic_memberships` 与 `hierarchy_scope_note`。
4. `scripts/hierarchy_stress_test.py`：themes 24、topics 74、memberships 547、complete 540、incomplete 2030、themes_without_topics 0、cross_dimension_topics []、apply_permitted false。
5. `scripts/build_relation_index.py`：7085 条（explicit 5998、inferred 1087、migrated 0），类型覆盖 3/67。
6. `scripts/write_current_health.py`：v1.29、complete 540、missing 2030、relation 7085、isolated 1258、ksq 57/65、structural 130、rule_drift 0、system_p0 0。
7. 归档 v1.28：55,032 字节，与改动前 `hierarchy/index.md` 逐字节一致，sha256 `822f9e8a479525cd38da0d1f100f8ccdd18fa15b926a8b4ce4b61d29626b5033`。
8. apply-plan 19 行：1 个 `structure_node_create`、13 个 `hierarchy_mount`、5 个 `structure_index_update`；生成后逐行复核哈希。
9. 全量闭包（`--refresh-generated --full`）与 `--check-generated` 的结果见第八节。

## 六、指标变化

| 指标 | 基线 v1.28 | 结果 v1.29 | 变化 |
|---|---|---|---|
| Theme | 24 | 24 | 0 |
| Topic | 73 | 74 | +1 |
| Topic membership | 534 | 547 | +13 |
| 完成挂载 KU | 527 | 540 | +13 |
| 未挂载 KU | 2043 | 2030 | -13 |
| relation index | 7059 | 7085 | +26 |
| member_of | 1061 | 1087 | +26 |
| 隔离单元 | 1263 | 1258 | -5 |
| knowledge_structure_quality | 57/65 | 57/65 | 0 |
| structural_health | 130/130 | 130/130 | 0 |

relation 新增 26 条 = 13 条 topic `member_of` + 13 条 theme `member_of`。隔离单元只减 5，因为 13 个 KU 中 8 个原有显式关系。

## 七、语义边界（并列不裁）

1. **铜镜起点三说**：夏燕靖两版「铜镜从战国时期开始出现并流行」；赵农「起源在新石器时期晚期的齐家文化」，并称「商周时制镜开始发达，至今已有 20 余面铜镜出土」；田自秉引 1976 年妇好墓早期镜，「把过去认为铜镜产生于战国时期或春秋时期的历史，又推前了几百年」。三说的时间跨度相差整个商周，本批并列，不裁定。
2. **汉镜厚薄两说**：夏燕靖「体薄、平边、圆钮」与赵农「镜体比战国铜镜加大增厚」相反；夏燕靖同册战国段又称战国镜「胎体很薄，不如汉唐铜镜的厚重」，同册内两处参照不同，本批不替作者弥合。
3. **透光镜原理两说**：田自秉「铸造应力和研磨压力造成的镜面曲率」与赵农「铜质材料在冷却时加工研磨所产生的内质变化原理，镜中材质出现了分子不匀」，两说是否同一机制，来源未说明。
4. **四期说与断代条目并存**：田自秉四期说只列战国镜、汉镜、唐镜、宋镜；六朝与五代两条不在四期内，本批不把两条硬塞进四期。
5. **「六朝」与「魏晋南北朝」**：两种断代覆盖范围不同，伍子胥画像镜的时代归属因此不唯一。

## 八、生成态与门禁

- 全量闭包（`--refresh-generated --full`）第一次 18/18 步通过，但 `rule_drift` 为 1：`05-outputs/index/index.md` 仍写 relation 7059，原因是第 8 步写 health 早于第 9 步重建导航。按既有处置重跑 `scripts/write_current_health.py` 清零，再跑第二次全量闭包，18/18 步通过，`rule_drift` 0、`system_p0` 0。
- h38 已进入 `06-runtime/automation/index.md`：`| hierarchy | 38 | [summary](2026-10-29-hierarchy-pilot-h38/summary.md) |`，并列入 recent 列表。
- `--check-generated`：17 步运行至第 17 步 `FAILED: check generated snapshots (exit=1)`；工作区未提交，生成态快照与 HEAD 必然不一致，此为预期结果。
- apply-plan 19/19 行哈希在两次闭包后复核一致。
- 保护路径 `02-sources/`、`03-processing/`、`.agents/`、`scripts/`、`01-domain/` 零改动。
- 未 commit、未 push；HEAD 仍为 `c249c6fe`。

## 九、未决事项与下一跳

本批未决 16 条，详见 `manifest.json` 的 `unresolved` 与 Topic 的「未解决问题」，核心是：无一件镜的直径、厚度、重量或曲率半径；铜镜起点、汉镜厚薄、透光镜原理三组两说/三说不可裁；唐镜 70:25:5 是唯一合金比例；高丰册无铜镜专条。

下一跳：

1. B.9 装饰工艺 Topic：错金银、镶嵌、刻划、金银平脱、三叠法；唐镜七种装饰工艺可在此与铜器装饰合并，但本 Topic 已保留铜镜自身的工艺名称，不重复挂载。
2. B.9 兵器 Topic：戈、矛、钺、剑、戟、弩。
3. B.9 乐器 Topic：编钟、八音、十二平均律。
4. 铁器与叠铸 Topic：生铁冶铸、铁范、`procedures/diezhu-jishu`。
5. 重复候选 reconcile 6 组与图注单条待核 12 条，仍按既有清单推进。
