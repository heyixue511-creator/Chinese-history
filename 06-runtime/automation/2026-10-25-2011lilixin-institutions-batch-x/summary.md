# 李立新《中国设计艺术史论》2011 册机构候选批次（五）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2011lilixin-institutions-batch-x/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 处理李立新《中国设计艺术史论》（2011）institution 候选 11 个（源行号 L179—L1683），逐条回读原文并作语义裁决。
- 结果：9 个 `create`、2 个 `update`、0 个 `no_delta`、0 个 `rejected`；无候选并入其他条目，东南大学候选合并 `cand-06-03`。
- 11 个候选终态全部为 `applied`。
- KU 总数由 816 增至 825；institution 类型由 135 增至 144；events 仍为 115。
- 候选索引投影后：applied 930、needs_evidence 3,540、no_delta 57、rejected 812；总数 5,339。
- `02-sources/` 未改动；`03基础书籍-md文档/` 只读；本会话未执行 commit／push。

**范围说明**：2011 李立新册 11 个 institution 候选至此全部处理完毕。六册 institution 候选清零；`needs_evidence` 中不再有 `institution` 类型。下一批转 place（170 个 needs_evidence）或其他 unit 类型。

**台账行数说明**：本批 ledger 为 **33 行**。11 个 applied 候选各走完整三行，11 × 3 = 33；无 no_delta、无 rejected 单行。

## 二、新建清单

| 文件 | 来源位置 | 主要增量 | confidence | after 指纹（前 19 位） |
|---|---|---|---|---|
| institutions/guowuyuan-xuewei-weiyuanhui.md | 李立新 2011 L179-L181；夏燕靖 2016 L5905；高丰 2004 L136-L140 | 国务院学位委员会：本科目录用“艺术设计”、研究生目录用“设计艺术”，作者判二者内涵相同、通用；补 1986 年 7 月批准中央工艺美术学院博士学位授予点、张道一任艺术学科评议组召集人 | medium | `sha256:942db2aabaf9`（6,420 bytes／100 行） |
| institutions/zhongyang-lishi-yuyan-yanjiusuo.md | 李立新 2011 L283 | 中央历史语言研究所：傅斯年主持，倡导“上穷碧落下黄泉，动手动脚找东西”，引“一分材料出一分货”与“史学便是史料学”三句话；未给成立年份、隶属、所址、组织与人员 | low | `sha256:ad072300fbb5`（5,316／89） |
| institutions/southeast-university.md | 李立新 2011 L341, L2446-L2448；高丰 2004 L136-L140；夏燕靖 2016 L6021 | 东南大学：1994 年 6 月张道一倡导组建我国第一个艺术学系；李立新 1999 年 9 月入学、2002 年 6 月 15 日答辩；补艺术学系主任题署与 1995 年计算机艺术会议承办 | medium | `sha256:7edfed17e692`（6,832／108） |
| institutions/swedish-museum-of-far-eastern-antiquities.md | 李立新 2011 L794 | 瑞典远东古物博物馆：藏中国青铜钺，钺上丝织物残痕为平纹底起菱形花纹的提花织物；未给馆史、藏品总目与入藏信息 | low | `sha256:ddcc1bd73329`（5,154／89） |
| institutions/shosoin.md | 李立新 2011 L1020-L1023；田自秉 2010 L3254, L3392；高丰 2004 L2998；夏燕靖 2009 L2148 | 正仓院：藏中国设计物品可证中国造物东传日本；唐代夹缬屏风、螺钿琵琶／阮咸、55 面唐代铜镜；“奈良东大寺正仓院”称法并存 | medium | `sha256:d3f3b7ea81f3`（7,394／119） |
| institutions/song-dai-huayuan.md | 李立新 2011 L1155-L1157 | 宋代宫廷画院：宫廷画院、院体画与格法／形似，及对文思院、甲库、文绣院、绫锦院等工艺机构的影响；与既有设立事件条目分工 | medium | `sha256:78841b18f058`（5,931／96） |
| institutions/qingjiang-chuanchang.md | 李立新 2011 L1204；夏燕靖 2009 L3750；夏燕靖 2016 L4607 | 清江船厂：《漕船志》记 8,873 名工匠、七类工种、十六府及“军余工办”征调；主要造内河漕船、也造部分海船；明初官营合计不归本厂 | medium | `sha256:2ac637869568`（6,766／111） |
| institutions/chengyi-gongsuo.md | 李立新 2011 L1261 | 成衣公所：据《长州县禁止无业游民在成衣公所寻衅滋扰碑》登记清代苏州成衣业行会；未给成立年份、公所址、行规、成员、经费与存续时间 | low | `sha256:a5fa028d29d3`（4,875／88） |
| institutions/china-commercial-art-writers-association.md | 李立新 2011 L1313 | 中国商业美术作家协会：1934 年上海成立，入会者 500 余人，同年办展览，先后出版工商业美术作品选集两辑；同段事务所与画会不并入 | medium | `sha256:83d29f27d0f6`（5,262／89） |

- 9 个新建均 `version: 1`、`evidence_status: source_backed`、`consensus: tentative`；source_count 分别为 3、1、3、1、4、1、3、1、1。
- 维度：国务院学位委员会、东南大学、成衣公所、中国商业美术作家协会以 D 为主导；中央历史语言研究所、瑞典远东古物博物馆、正仓院、宋代宫廷画院、清江船厂按主题分别以 A、D／B、D／B、D／C、B／D 为主导，详见各条 frontmatter。
- title 均为“中文（English）”双语形式。

## 三、update 清单

| 文件 | 来源位置 | 主要增量 | 批前 → 批后 | source_count／version |
|---|---|---|---|---|
| institutions/jiangnan-zhizao-zongju.md | 李立新 2011 L1293 | 江南制造总局：补上海江南制造局自创办至 1904 年生产机器设备 467 台（座）、机器零件及工具 115.3 万件；补官办企业制造枪炮、轮船与机器设备的序列；福建船政局 1869 年第一艘近代蒸汽船作同段参照，不归本局；alias 增“江南制造局”“上海江南制造局” | `sha256:126c9a3037f0…`（6,039／100）→ `sha256:7a5b053d880a…`（8,135／116） | 3→4；2→3 |
| institutions/neiwufu-zaobanchu.md | 李立新 2011 L1683 | 内务府造办处：补康熙时设宫廷玻璃厂、雇用欧洲工匠制造精细工艺品、玻璃器生产恢复；区分元末明初博山作坊、清代博山百余家与近代大型玻璃厂；与既有造办处玻璃厂按同一机构合并，隶属与名实待考 | `sha256:6740bbbaa34f…`（8,829／120）→ `sha256:d53a68310db6…`（10,940／134） | 4→5；3→4 |

- 江南制造总局更新保留夏燕靖 2009、赵农 2009、夏燕靖 2016 三源，新增李立新 2011 为第四源；李立新只给 1904 年前累计产量与官办企业定位，未给统计口径、资料来源、局址、隶属、资本与工人数。
- 内务府造办处更新保留高丰 2004、夏燕靖 2016、赵农 2009、田自秉 2010 四源，新增李立新 2011 为第五源；李立新只称“宫廷玻璃厂”，未明说隶属造办处，合并依据是高丰所记造办处下设玻璃厂，正文标为编者按语并留“名实待考”。
- 两处更新均未另建重复条目（不建 `gongting-boli-chang.md`），保留既有别名的多称并存。

## 四、no_delta 判定

本批无 `no_delta`。

## 五、rejected 判定

本批无 `rejected`。

## 六、本批的判断

1. **机构本体与设立事件分记**：`cand-03-22` 宋代宫廷画院的来源段与既有 `events/song-dai-huayuan-sheli.md` 高度重叠。既有条目记“宋代宫廷画院设立”这一事件，本批新建 `institutions/song-dai-huayuan.md` 记画院作为机构的创作规范、院体画与对文思院、甲库、文绣院、绫锦院的影响；两者 type 与指称侧面不同，故不判 no_delta，也不把 event 条文直接改写为 institution。
2. **候选所指为既有机构的一部分时判 update**：`cand-05-09` 只称“宫廷玻璃厂”。高丰 2004 已记造办处下设玻璃厂，故判 update 既有 `neiwufu-zaobanchu.md`；李立新未明说该厂隶属造办处，正文同时保留“按同一机构合并”的编者判断与“隶属、设立细节待考”的边界，不把或然关系写成确定事实。
3. **名称不同不等于机构不同**：`cand-04-17` 的“江南制造局”与既有 `jiangnan-zhizao-zongju.md` 的“江南制造总局”为同一机构的不同称法；既有条目已记 1865 年创办、曾国藩／李鸿章、兵工厂、造船与翻译馆，故只补李立新第四源与 1904 年前产量，不新建 `jiangnan-zhizaoju.md` 一类平行条目。
4. **相邻船厂不合并**：`cand-03-23` 清江船厂与既有 `longjiang-chuanchang.md` 的南京龙江船厂同为明代官营船厂，但来源分记不同厂名、地点与职能；龙江船厂条只列“清江船厂”名称而未收 8,873 名工匠等数据，故清江船厂判 create，不并入龙江船厂。明初官营船厂“2 万余人、年造 3,000 余只”的合计亦不归清江船厂。
5. **合并候选与事件分记**：`cand-01-56` 东南大学合并 `cand-06-03`，canonical-mapping 记录该合并；1994 年艺术学系设立、2002 年李立新答辩、1995 年计算机艺术会议分别由既有事件条目承载，本条只登记学校与艺术学系本体、培养关系及会议承办，不重复事件叙述。
6. **命名分工不重复事件**：`cand-01-11` 国务院学位委员会只登记委员会本体与“本科艺术设计／研究生设计艺术”的命名分工，补 1986 年学位授权与张道一学科评议职务；1998 年本科目录与研究生目录两次调整仍由 `events/1998-moe-major-catalog.md`、`events/sheji-yishuxue-1998.md` 承载，不在本条重写。
7. **单源且信息面窄的条目保留 low**：中央历史语言研究所、瑞典远东古物博物馆、成衣公所各只有一处直接记载，均缺成立年份、隶属、组织、人员或经费等基本项；三条均判 create 而非 rejected，因来源确实给出机构实体与可核事实，但 confidence 定为 low，并在验证状态列明缺项。
8. **译名与文件名按通名，不把或然当确定**：瑞典远东古物博物馆文件名用 `swedish-museum-of-far-eastern-antiquities.md`，正仓院文件名用 `shosoin.md`，均与候选 slug（`sweden-museum`、`zheng-cang-yuan`）不同；前者英文名按该馆通名、来源未给英译，后者采用通行罗马字，名实对应均标为待外部核对。
9. **多源只用于确有增补且能对账的条目**：正仓院用四源，是因为李立新、田自秉、高丰、夏燕靖各提供了东传、夹缬、铜镜与“东大寺”称法等不同侧面；江南制造总局与内务府造办处的 update 亦因新源确有产量、玻璃厂细节等增量。其余单源条目保持单源，不把同段背景性提及算作第二源。
10. **同段并置实体不扩大归属**：中国商业美术作家协会条只登记协会本体，同段尚美图案馆、大熊工商美术社、上海美术供应社与月份牌画家工作室均不并入；成衣公所条只登记碑刻所见的行会，同段江宁、苏州、杭州成衣业与湖州双林镇衣庄作背景，不写成公所产业；清江船厂条把福建船政局、龙江船厂与明初官营合计分别标为同段参照或他厂数据。
11. **照录来源写法，不据外部常识改写**：中国商业美术作家协会条中来源写作“庞薰栗”，正文照录并标“原文如此”，不改为“庞薰琹”；中央历史语言研究所与东南大学的 `location` 写“来源未给”，不把“南京”等来源外常识写入 frontmatter；宫廷玻璃厂的隶属判断以编者按语显式标出。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：33 行；11 个候选；applied 11（各 3 行）；11 个终态行均带 `target_ref`。
- `apply-plan.jsonl`：11 行；create 9、update 2；create 的 `before` 为 null；update 的 `before` 与批前指纹一致；11/11 的 after 指纹、bytes、lines 与磁盘一致。
- `canonical-mapping.json`：11 条（create 9、update 2）；东南大学 `merged_candidates` 为 `["2011-lilixin-zhongguo-sheji-yishu-shilun:cand-06-03"]`，其余为空；与 apply-plan 的目标、动作、候选一一对应。
- 候选索引：5,339 行；批前 `sha256:d4acbebb…`（applied 919、needs_evidence 3,551、no_delta 57、rejected 812），批后 `sha256:0fb76ef9…`（applied 930、needs_evidence 3,540、no_delta 57、rejected 812）；重建幂等。
- 内容质量审计：825 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 825/825 可解析，断链 0，类型覆盖 8/8，结构节点覆盖 0/4，层级挂载 0/825；institutions 144、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；825 个 KU 均未建立正式 relation。
- 规则漂移审计：0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过；pytest 250 项、16 subtests 通过（failures 0、errors 0、skipped 0）。
- Sync closure：`--refresh-generated --full` 运行 18/18 通过；另以 `--refresh-generated --check-generated --full` 复核，第 1—16 步完成，第 17 步因工作树未提交、10 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。10 个文件为：`04-knowledge/quality/translation-index.yml`、`05-outputs/index/index.md`、`05-outputs/knowledge-graph-data.js`、`05-outputs/knowledge-graph-data.json`、`06-runtime/automation/index.md`、`06-runtime/governance/governance-backlog.md`、`06-runtime/state/candidate-index.jsonl`、`06-runtime/state/current-health.json`、`06-runtime/state/discovery-manifest.json`、`06-runtime/state/generated-projections-manifest.json`。

## 八、边界与研究债

- 9 个新建中 4 个为单源（中央历史语言研究所、瑞典远东古物博物馆、成衣公所、宋代宫廷画院）；正仓院四源、国务院学位委员会三源、东南大学三源、清江船厂三源；2 个更新分别为四源、五源。全部 `consensus: tentative`，验证层级未评定，图版未视觉核验。
- 具体缺项：国务院学位委员会缺成立年份、组成、历届委员与学位授权审核程序；中央历史语言研究所缺正式全名、成立年份、隶属、所址、组织、人员与主要成果；东南大学缺校史沿革与艺术学系 1994 年后的组织细节；瑞典远东古物博物馆缺建馆年份、馆址、藏品总目、青铜钺入藏信息与丝织物残痕的检测报告；正仓院缺藏品总目、各件入藏年代与来源、东传路线；宋代宫廷画院缺设立年份、院址、员额、职官与画院制度；清江船厂缺厂址、创设年份、隶属、官员、船坞数、年造船量、工匠分工细节与存续时间；成衣公所缺成立年份、公所址、行规、成员、经费、职能与碑刻原文；江南制造总局缺统计口径、资料来源、局址、隶属、资本、工人数与各年产量；中国商业美术作家协会缺发起人、章程、组织架构、会员构成、展览名称、作品选集全名与终止时间；内务府造办处仍缺玻璃厂的正式厂名、设立年份、厂址、工匠名册与欧洲工匠来源。
- 已并存未释的张力：“宫廷玻璃厂”与造办处玻璃厂的名实关系；“江南制造总局／江南机器制造总局／上海江南制造局”三式名称；“正仓院／奈良正仓院／奈良东大寺正仓院”称法；宋代画院与既有设立事件的叙述分工；成衣公所碑刻年代与行会成立时间；瑞典远东古物博物馆英文名与馆名的名实对应。
- 结构层仍为 0/4，层级完整挂载 0/825，正式 relation 0 条，Theme／Topic 均未实体化。
- 六册 institution 候选已全部处理；`needs_evidence` 余 claim 1,363、term 875、work 652、person 273、publication 207、place 170。
- 下一批转 place（170 个 needs_evidence）；完成后依次处理 publication、person、work、term，再进入 claim 1,363 个的 claim/evidence 流程。
- 本批临时脚本（`_tmp_institutionsx_emit.py`、`_tmp_institutionsx_verify.py`、`_tmp_institutionsx_finalize.py`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理；`_tmp_x_closure18.txt`、`_tmp_x_closure19.txt`、`_tmp_x_content_audit.txt`、`_tmp_x_repo_audit.txt`、`_tmp_x_relation_audit.txt` 同批待清理。
