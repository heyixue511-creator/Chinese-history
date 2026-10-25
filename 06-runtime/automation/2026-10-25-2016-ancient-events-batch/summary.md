# 2016 册古代至元代事件候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2016-ancient-events-batch/`
状态：`applied`

## 一、本批做了什么

- 从夏燕靖《中国艺术设计史（升级版）》（2016）的未分组 unit 候选中，取 27 个古代至元代的 `event` 候选（`cand-02-88` 至 `cand-08-90`）逐条回读原文并作语义裁决。
- 22 个判 `create`，新建 event KU；5 个判 `no_delta`（鬼谷下山罐、质孙服、授时历、妙应寺白塔、克拉克号，均已由既有 KU 完整覆盖）；无 `update`、无 `rejected`。
- KU 总数由 511 增至 533，event 类型由 17 增至 39；本批新增中 `historical_event` 18 条、`discovery` 4 条。
- 候选索引投影后：applied 570、no_delta 32、rejected 801、needs_evidence 3,936；active 3,936、terminal 1,403。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地点 | 主要增量 |
|---|---|---|
| events/yu-casts-nine-cauldrons.md | 传说夏代，荆山之下 | 收九牧之金铸九鼎、魑魅魍魉纹、迁鼎与定鼎、天子九鼎八簋至元上三鼎一簋、楚庄公问鼎 |
| events/ganshi-battle.md | 夏代，甘泽 | 《尚书·甘誓》车战与阵法、比喜克索斯人战车早 300 年、一车三人甲士与徒卒、夏后启修德故事 |
| events/shang-tang-overthrows-xia.md | 商代建立前后 | “良车七十乘”、奚仲任车正、“挠曲为轮，因直为辕”、全木轮至有辐车轮 |
| events/king-wu-conquers-zhou.md | 商末，孟津 | 战车 300 辆、近卫军 3000 人、甲士 4.5 万人；舟字八形、舢板船与舵桨最早记载 |
| events/jin-casting-legal-cauldron.md | 公元前 513 年，晋国汝水旁 | “赋晋国一鼓铁，以铸刑鼎”、生铁冶铸序列、程桥白口铁丸、排橐与 300 人鼓风 |
| events/mozi-zhi-chu-gong-song.md | 约公元前 444 年，楚宋之间 | 公输盘造云梯、墨子九距攻城机变、禽滑厘等 300 人守宋、墨守成规 |
| events/qin-mie-liuguo.md | 公元前 221 年 | 第一个大一统帝国、统一文字货币度量衡、万里长城与宫殿陵墓、秦俑评价 |
| events/zhangqian-chushi-xiyu.md | 前 138、前 119 年 | 两次出使、长安至中亚西亚及地中海东岸、陆上丝绸之路、统一商业市场 |
| events/qin-qian-yetie-haozu.md | 秦代，四川、南阳 | 强迁冶铁业、卓氏程氏孔氏三例、集中控制与缴除武装、技术交流后果、铁官 |
| events/han-wudi-duzun-rushu.md | 汉武帝时期 | 罢黜百家、董仲舒四权一体、服饰等级、男子以袍为贵与祛袂曲裾直裾 |
| events/xiao-wen-gai-zhi.md | 北魏 | 改拓跋姓氏、“群臣皆服汉魏衣冠”、秦汉冠服旧制延续 |
| events/jingkang-zhibian.md | 1126—1127 年 | 徽钦二帝被掳、南迁临安、淮水大散关界线、崇文抑武与 1276 年临安陷落 |
| events/fucangshan-tomb.md | 1975 年，福建浮仓山 | 南宋贵族妇女墓、袍袄裙衫裤肚兜等成组衣饰、直领对襟与印金刺绣彩绘 |
| events/deyang-xiaoquan-silver-find.md | 1959 年，四川德阳孝泉镇 | 宋代银器 117 件、24 种器类、圆球形镂空卷草纹银熏炉、各地宋墓参照 |
| events/xixia-mausoleum.md | 20 世纪 70 年代初，西夏王陵 | 丝织残片 10 余片（锦、罗）、烟色素罗与工字绫等组织、茂花闪色绵 3 片 |
| events/yuan-abolish-keju.md | 元代初年 | 取消科举、士人浪迹酒楼茶肆、与民间艺人结合、民间工艺发达的原因判断 |
| events/qingshousi-tomb-textiles.md | 1955 年，北京西长安街 | 4 片纳石失金锦、紫阳荷花缂丝、酱色素绸与织花绸、喀左元墓参照 |
| events/boyan-collects-song-regalia.md | 至元十二年（1272） | 伯颜收取衮冕圭壁符玺图籍车辂仪仗、服饰转向汉制、蒙古男子发式与笠子帽 |
| events/yanyou-fuse.md | 延祐元年（1314） | 一品至三品浑金、四品五品金答子、六品以下销金并金纱答子、顾姑冠与蒙汉女服 |
| events/queue-and-dress-edicts.md | 清初 | “留头不留发，留发不留头”、金之俊“十从十不从”全文、服饰保持明制 |
| events/zhenghe-voyages.md | 明永乐三年（1405）左右 | 七下西洋、贸易瓷第一次高峰、阿拉伯王宫镶嵌瓷器、八地博物馆藏青花 |
| events/qing-opens-sea-ban-1684.md | 1684 年 | 开放海禁、福建四船厂、苏州扬州厦门民营造船、明初官营船厂与轮班船木匠 |

## 三、no_delta 判定

| 候选 | 既有 KU | 覆盖依据 |
|---|---|---|
| cand-07-56 2005 年“鬼谷下山”青花罐伦敦拍卖 | works/guiguxiashan-qinghua-guan.md | 已记 2005-07-12、克里斯蒂、埃斯凯纳齐、1568.8 万英镑、高 27.5／直径 33 厘米、存世 8 件、1968 年克利夫兰展览 |
| cand-07-60 1321 年元英宗定制质孙服 | terms/zhisun-fu.md | 已记 1321 年定制、汉语“一色衣”、上衣连下裳上紧下短、腰间襞积、肩背大珠、冬 11 等夏 15 等 |
| cand-07-57 1276 年设太史局编《授时历》 | persons/guo-shoujing.md | 已记 1276 年诏令、太史局、王恂与郭守敬、1280 年成历、4 年创制 17 种仪器、简仪与圆柱体轴承 |
| cand-07-58 至元八年建妙应寺白塔 | works/miaoying-si-baita.md | 已记 1271 年、阿尼哥设计、覆钵式喇嘛塔、高 50.9 米、三层亚字形须弥座、40 块铜板瓦华盖、36 只流苏风铃、刹顶小塔 5 米 40 吨 |
| cand-08-89 克拉克号被捕获 | terms/blue-and-white-porcelain.md | 已记 1602 年荷兰东印度公司捕获葡萄牙商船“克拉克号”、因不明产地命名、漳州平和窑址与分水技法 |

## 四、本批的判断

1. **事件与器物／人物／术语分工**：事件条只记“何时、何地、谁参与、做了什么、来源据此说明什么”；器物尺寸、纹样与形制归 work 条，人物生卒与官职归 person 条，工艺定义与分级归 term 条。鬼谷下山罐、质孙服、授时历、妙应寺白塔、克拉克号五项均由既有条完整承载，判 `no_delta`。
2. **discovery 与 historical_event 分用**：浮仓山墓、德阳银器、西夏王陵、庆寿寺双塔属考古发现或清理，`sub_type` 用 `discovery`；其余 18 条为历史事件，用 `historical_event`。
3. **传说事件照录**：禹铸九鼎、甘泽之战均按来源的传说叙述建条，`date` 只写“传说夏代”“夏代”，不据外部考订补年份、战场或器物对应；`date_note` 与“证据边界”明确写出。
4. **原文异文不改写**：《吕氏春秋·己篇》《吕氏春秋·简读》、周定王使臣“公孙满”、列鼎“元上三鼎一簋”等均照录来源，必要时在句内注明“原文如此”；不据传世本校正。
5. **跨册分工**：郑和下西洋条只取 2016 册贸易瓷第一次高峰、亚非“中国风”与收藏地点；宝船尺度与船队规模仍由 `works/zhenghe-baochuan.md` 承载。克拉克号事件判 no_delta，克拉克瓷的窑址、器形与分水技法留给后续 term 候选 `cand-08-71` 建 `terms/kelake-ci.md`。
6. **维度判断**：B 维度 10 条（器物、冶铸、纺织、车船、攻守器械），D 维度 8 条（统一制度、官营手工业、服色与选官政策），E 维度 4 条（丝路、汉化、宋室南迁、下西洋）。维度按候选核心议题判定，不按朝代机械分配。

## 五、本批的方法判断

- 27 个候选对应的 27 处原文跨度逐条回读（L774-L787、L893-L921、L899-L921、L922-L930、L1077-L1084、L1487-L1499、L1609-L1619、L1635-L1642、L1643-L1660、L1790-L1799、L2225-L2228、L3060-L3067、L3301-L3330、L3397、L3530-L3542、L3619-L3629、L3678-L3691、L3728-L3745、L3786-L3789、L3790-L3798、L3822-L3842、L3928-L3951、L3958-L3972、L4264-L4269、L4403-L4422、L4423-L4426、L4596-L4618），核对时间、地点、数量、引文与工艺描述后再动笔。
- 建条前比对 5 个判 no_delta 的既有 KU，以及 `terms/ding.md`、`terms/lieding-system.md`、`terms/jili-guche.md`、`terms/zhisun-fu.md`、`works/zhenghe-baochuan.md`、`persons/guo-shoujing.md` 等相邻条目，确认增量边界。
- 模板沿用 `events/xianrendong-taoci-chutu.md` 的六节结构；`source_count: 1`、`confidence: medium`、`consensus: tentative`，不越级标 `high` 或 L1–L7。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析与六节结构检查，22/22 通过。
- 判定与写回分离：台账 81 行（27×3）、apply-plan 22 行、mapping 27 条，与磁盘、索引三方核对，0 错误。

## 六、状态与验证

- `candidate-decision-ledger.jsonl`：81 行，27 个候选各 3 行；终态 applied 22、no_delta 5。
- `apply-plan.jsonl`：22 行，均为 create，`before` 为 null；22/22 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：27 条（create 22、no_delta 5），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:c9d02400…`（applied 548、no_delta 27、needs_evidence 3,963），批后 `sha256:533311a7…`（applied 570、no_delta 32、needs_evidence 3,936）；重建幂等。
- 内容质量审计：533 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据引用 533/533 可解析，断链 0，Frontmatter 缺失 0，events 39。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 22 条新建 KU 均为 `source_count: 1`（夏燕靖 2016），未标 high confidence；传说事件与来源内单一叙述的事实密度有限，后续若有第二来源应优先补证。
- 浮仓山、德阳、西夏王陵、庆寿寺四条只记来源给出的年代、地点、数量与工艺特征；墓葬编号、墓主姓名、纤维检测、金线成色等来源未载信息均留在“证据边界”，未引外部材料补全。
- 结构层仍为 0/4，层级挂载 0/533，正式 relation 0 条，Theme／Topic 均未实体化。
- 2016 册现代设计大事记仍有 37 个 event 候选（`cand-09-10` 至 `cand-11-114`）待分诊；其余册的 event 候选按 2016 古代批之后的顺序继续。
- 本批临时脚本（`_tmp_2016_events_emit.py`、`_tmp_2016_events_batch_emit.py`、`_tmp_2016_events_batch_verify.py`、`_tmp_2016_ancient_ids.txt`、`_tmp_2016_ancient_spans.txt` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
