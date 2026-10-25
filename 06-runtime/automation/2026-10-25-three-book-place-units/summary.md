# 第五批写回：跨三书 9 组 place 知识元

- 工作包：`06-runtime/automation/2026-10-25-three-book-place-units/`
- 状态：`applied`
- 日期：2026-10-25
- 范围：Books 1–6（前六本）；Book 7 及以后不启动

## 一、批次范围

从 `duplicate-groups.jsonl` 中筛出 `doc_count = 3` 的组，共 **103 组、309 条候选**。本批只取其中 `place` 一类实体，共 **9 组、27 条候选**（`xdup-0088`–`xdup-0096`）：

- 9 组在本批写回，每组 `member_count = 3`：1 条升为 canonical 并写回 KU，2 条转为 `rejected` 并注明并入目标；
- `doc_count = 3` 一层累计已覆盖 18 组（前批 institution／procedure／event 9 组 + 本批 place 9 组）；
- 余 **85 组、255 条候选**属 person／publication／term／work 等，本批不处置，仍为 `needs_evidence`。

`place` 类知识元由 7 个增至 **16 个**，基础类型覆盖仍为 8/8（前批已达成）。

组内 slug 写法有分歧而被判为同一实体的有 7 组：`xdup-0088`（`erlitou-yizhi` / `erlitou-site`）、`xdup-0089`（`yuandadu` / `khanbaliq` / `yuan-dadu`，`khanbaliq` 为同一城的蒙古语名）、`xdup-0090`（`jiangzhai-site` / `jiangzhai-yizhi`）、`xdup-0091`（`ding-kiln` / `dingyao` / `ding-yao`）、`xdup-0093`（`jing-de-zhen-yao` / `jingdezhen-yao`）、`xdup-0095`（`longquanyao` / `long-quan-yao` / `longquan-yao`）、`xdup-0096`（`long-men-shiku` / `long-men-shi-ku` / `longmen-shiku`）。`xdup-0092`（`jingdezhen`）与 `xdup-0094`（`yinxu`）三册写法一致。

**本批最重要的一项边界判断**：`xdup-0092`（景德镇）与 `xdup-0093`（景德镇窑）指向重叠对象——一座城与城中的窑场——曾考虑合并，最终分立两 KU。地名条承担建制、人口、御器厂、手工工场、瓷业公司与近现代产业形态；窑场条承担釉色、窑具、款识与外销。赵农「3. 景德镇」一节兼述二者，已在两条正文中互相标注。

## 二、canonical 映射

| 组 | 实体 | 类型 / sub_type | canonical 候选 | 写回文件 | KU source_count |
|---|---|---|---|---|---|
| xdup-0088 | 二里头遗址 | place / archaeological_site | `2009-zhaonong-…:cand-02-26` | `04-knowledge/units/places/erlitou-site.md` | 6 |
| xdup-0089 | 元大都 | place / city | `2009-zhaonong-…:cand-09-31` | `04-knowledge/units/places/yuan-dadu.md` | 4 |
| xdup-0090 | 姜寨遗址 | place / archaeological_site | `2011-lilixin-…:cand-02-155` | `04-knowledge/units/places/jiangzhai-site.md` | 3 |
| xdup-0091 | 定窑 | place / kiln_site | `2010-tianzibing-…:cand-09-39` | `04-knowledge/units/places/ding-kiln.md` | 6 |
| xdup-0092 | 景德镇 | place / city | `2009-zhaonong-…:cand-08-138` | `04-knowledge/units/places/jingdezhen.md` | 6 |
| xdup-0093 | 景德镇窑 | place / kiln_site | `2010-tianzibing-…:cand-09-52` | `04-knowledge/units/places/jingdezhen-kiln.md` | 6 |
| xdup-0094 | 殷墟 | place / archaeological_site | `2010-tianzibing-…:cand-03-12` | `04-knowledge/units/places/yinxu.md` | 6 |
| xdup-0095 | 龙泉窑 | place / kiln_site | `2010-tianzibing-…:cand-09-55` | `04-knowledge/units/places/longquan-kiln.md` | 6 |
| xdup-0096 | 龙门石窟 | place / archaeological_site | `2009-zhaonong-…:cand-06-39` | `04-knowledge/units/places/longmen-grottoes.md` | 6 |

KU 的 `source_count` 按该实体在六册中是否有字面命中计数，与本组 `member_count = 3` 不等：本批 9 组中有 7 组 `source_count = 6`，即六册全部有字面命中；元大都 4 册（李立新、田自秉不记此城）、姜寨遗址 3 册。差额来自 `doc_count = 3` 之外的册次，已在各 KU 的 `sources` 中列明。高丰与李立新两册对龙门石窟各仅一句，仍计为有效来源。

## 三、方法

1. **六册复读而非三册**：每组除三册召回来源外，另在其余三册中检索该实体；定窑、景德镇、景德镇窑、殷墟、龙泉窑、龙门石窟六组在六册中均有文本，故 `source_count = 6`。只读召回的三册会漏掉高丰的釉料学判断与李立新的框架性引用。
2. **差异记录而非裁决**：纪年、窑数、款识、官民归属、地名来源的冲突全部原文并列保留，写入 `## 核心内容` 并标注出处。本批的冲突密度高于前批，典型者为「三百余座窑」被田自秉系于宋、被高丰系于元（同一引文），以及「太禧」（夏燕靖两版）与「太僖」（田自秉）。
3. **状态链**：canonical 走 `needs_evidence → ready_for_review → approved → applied`；同组其余 2 条走 `needs_evidence → rejected`，reason 中写明 canonical 目标。
4. **追加式台账**：`candidate-decision-ledger.jsonl` 共 45 行（27 + 9 + 9），覆盖 27 个唯一 `candidate_id`，只以 transition 叠加，不改写历史 R1 台账。
5. **类型化写回**：`apply-plan.jsonl` 为 9 条 `create`，无 `update`、无 `delete`；逐条重算 `sha256 / bytes / lines`（CRLF→LF 归一）并与磁盘核对，9/9 一致。
6. **验证分级克制**：9 个 KU 一律 `confidence: medium`、`consensus: tentative`、`evidence_status: source_backed`，不填 `verification_level`。二里头、定窑、景德镇、龙泉窑四条的来源冲突已足以支撑 `disputed`，但字段契约要求 `consensus: disputed` 必须配 L1–L7 验证层级，本批未做外部验证，故不升级。
7. **sub_type 取值**：`kiln_site` 不在 taxonomy 的 place 枚举内（枚举为 archaeological_site / design_institution / city / geographical_region / museum / school），沿用既有磁州窑、汝窑、钧窑、邢窑、越窑先例；龙门石窟取 `archaeological_site`（枚举无 grotto 值），景德镇取 `city`。

## 四、主要来源差异

| 实体 | 差异 |
|---|---|
| 二里头遗址 | 年代定性三说：夏代晚期（高丰、夏燕靖两版）／「是否就是夏文化，考古界还有不同的看法」（田自秉）／商代早期（赵农全册一律作「商代早期宫殿」「商都」）；两件铜爵尺寸不同（田自秉 13.3 厘米三镂孔／夏燕靖 2016 长流爵高 22.5 厘米、流至尾长 35 厘米）；「最早青铜器」两种口径（甘肃东乡林家村马家窑青铜刀约前 3000 年／二里头长流爵）；夏燕靖 2016 同册并存「新石器时代晚期文化」与「青铜时代」两种分期位置 |
| 元大都 | 夏燕靖两版同段作「周长 28600 米，面积 50 余万平方公里」——周长与面积不相容，原文照录未改字；两版用字「凤池坊／风池坊」「建设基础／区域基础」；白塔建造年份与高度仅赵农给出（至元八年、53 米）；「十万户」（夏燕靖引马可·波罗）与「人口百万」（赵农）一为户数一为口数，来源未换算 |
| 姜寨遗址 | 三册均以遗址为论据而非叙述对象，遗址面积、房址数、年代分期在来源内缺失；赵农记石砚等绘制工具为 1973 年、夏燕靖 2016 记陶钵编织席印痕为 1972 年，所指遗物不同；李立新「一期两件距今 6600 多年黄铜制品、含锌 25%」为六册中最具体的冶金数据，并给出正式报告出处（《姜寨》，文物出版社 1988 年版） |
| 定窑 | 窑址村名两套：「涧磁村及东西燕山村」（高丰）、「灵山镇附近」（田自秉）、「北镇村通天河一带」（夏燕靖 2009）；断代下限——田自秉「唐经五代至北宋鼎盛」，夏燕靖引 1970 年代定论「失传于元」而同册下文又记「金代定窑，这是北宋定瓷的直接继续」；款识三份清单（高丰「官、新官」／夏燕靖「奉华、聚秀、慈福、官」／田自秉「尚食局、尚药局、五王府、慈福」）交集仅「官」「慈福」；赵农图题作「宋 定窑青瓷瓶」，与其白瓷定性不符，原文异常照录 |
| 景德镇 | 得名落点三说：改镇名并设监镇（高丰）／贡品上书写「景德」标志（赵农）／《陶录》器底书「景德年制」四字（田自秉）；始烧年代——武德年间（赵农）／唐以来有窑址（田自秉）／「唐代以后」（高丰）；窑数四种口径（元蒋祈《陶纪略》三百余座被田自秉系于宋、被高丰系于元；《浮梁县志》三百座→三千座；明代民窑 900 多 vs 传教士 3000 座 vs 唐英 300 区；道光 270~290 座→1869 年 60 座）；原文异常两处「洪武三十五年」「景德镇石陶瓷研究所」 |
| 景德镇窑 | 「太禧」（夏燕靖两版）与「太僖」（田自秉，且释为掌管宗室祭祀的机构）字形与释义不同；三百余座窑系于宋／元；支圈覆烧南传时间——夏燕靖 2016「始创于北宋中期定窑……南宋时传到南方景德镇」与同册「南宋中期景德镇等窑出现支圈覆烧」并不完全对齐；青花时序——高丰「元代发展起来」，田自秉据木浦沉船「无一件青花瓷器」推断「开始流行可能在元代中期以后」；影青创烧系于「北宋中期」（夏燕靖两版）而高丰只作「宋代以景德镇窑为代表创烧」 |
| 殷墟 | 《竹书纪年》年数三说：夏燕靖两版同段并存「二百五十三年」与「计七十三年」，赵农引古本作「二百七十三年」；妇好墓铜器「468 件」（田自秉）与「460 余件」（高丰），玉器「755 件」（田自秉）与「近 600 件」（赵农）；铜镜「至今才发现 5 面，其中 4 面出土于妇好墓」（高丰）与田自秉「推前了几百年」判断取向不同；铸铜遗址面积「10 000 平方米以上」田自秉与赵农未互相引用而一致 |
| 龙泉窑 | 创烧年代三说：「北宋早期」（高丰）／以「五代越窑衰落」为起点（赵农）／「一个宋代南方青瓷产区」（田自秉）；元代窑址「约 150 余处」（夏燕靖 2009）与「约有 150 处」（2016）；龙泉窑与弟窑、哥窑的关系——赵农「即为弟窑」为既定事实，田自秉「是否真有其兄弟二人，已无可考」，夏燕靖 2009 另称「研究者普遍认为传世哥窑属于宋代官办瓷窑」；赵农「在元代初年很快恢复生产」隐含元初曾中断，其余五册未作此表述 |
| 龙门石窟 | 赵农同册两处统计不一：北魏段「现存大小佛龛 2137 个，造像约 10 万尊，其中北朝的占三分之一」，唐代段「2000 多个佛窟和佛龛，绝大多数是唐代开凿的」；四大石窟名单四册各不相同（高丰克孜尔／敦煌／云冈／龙门；田自秉云冈／龙门／响堂山／栖霞山；李立新另列麦积山；夏燕靖 2016 另列天龙山）；《魏书·释老志》引文起句被截断（起于「窟二所」）而赵农未补 |

## 五、验证结果

| 门禁 | 结果 |
|---|---|
| `apply-plan` 哈希核对 | 9/9 与磁盘一致（sha256、bytes、lines；CRLF 归一） |
| `build_discovery_index.py` | total 5339，applied 52，needs_evidence 5119，rejected 168，无 issue |
| `audit_content_quality.py` | 0 项发现（80 个知识元） |
| `audit_repo.py` | structural health 122/130；类型覆盖 8/8（place 7→16）；deprecated_type_drift 0；验证语义问题 0 |
| `build_runtime_index.py` | 已刷新 `06-runtime/automation/index.md` |
| `run_sync_closure.py --refresh-generated --full --check-generated` | sync closure passed |
| `pre_commit_check.py` | 规则漂移 0 |

状态迁移的算术核对：前批 needs_evidence 5146 → 本批 9 条 canonical 转 `applied`、18 条重复候选转 `rejected` → 5146 − 9 − 18 = **5119**。applied 43 → 52，rejected 150 → 168。

## 六、边界与未解决项

- 未 commit、未 push；仅工作树变更。
- 未建分支、未建 worktree；`main` 为唯一主线。
- `02-sources/` 只读，未改写；本批实际读取的源目录为 `03基础书籍-md文档/`。
- 未使用外部验证平台，证据仅限六册 Markdown 文本；未做图版、遗址或实物核验。
- `primary_theme` 与 `topic_memberships` 留空：Theme / Topic 节点尚未 materialize，已计入 research debt。
- 未写入正式 `relations`：9 个 KU 均处于 isolated 状态，跨 KU 共现（如定窑—景德镇窑的覆烧南传、景德镇—龙泉窑的沉船并列）只在正文以非断言方式记述。
- `doc_count = 3` 一层 103 组中已覆盖 18 组；余 **85 组（255 条候选）**仍为 `needs_evidence`，未作状态推进，属 research debt。
- 人物类知识元整体缺失：刘秉忠（元大都）、慧成／白整／刘腾（龙门石窟）、唐英（景德镇督陶官）、顾仕成（龙泉窑明代匠人）、章生一／章生二（哥窑传说）在六册中均有可引文本，但 `persons/` 尚无对应条目，已作为研究债务写入相关 KU 的「相关知识元」段。
- 两处候选 span 为跨全书召回而非连续段落（赵农 `cand-08-138` L5617–L7952、夏燕靖 2016 `cand-06-62` L3607–L6058，均因抽取器合并了对景德镇的所有提及），本批按候选自带的 evidence ref 分块读取，未当作单一连续段落使用。
- 哥窑与弟窑尚无独立 KU，「是否官窑」的分歧暂记于 `longquan-kiln.md` 的验证状态；定窑、景德镇窑的款识问题、二里头的朝代定性仍为 open dispute，需外部文献才能推进。
