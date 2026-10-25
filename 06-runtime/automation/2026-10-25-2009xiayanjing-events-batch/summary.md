# 夏燕靖《中国设计史》2009 册事件候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009xiayanjing-events-batch/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从夏燕靖《中国设计史》（2009）的未分组 unit 候选中，取 10 个 `event` 候选逐条回读原文并作语义裁决；这是六册 event 候选的最后一批。
- 3 个判 `create`，新建 event KU；7 个判 `update`，向既有以 2016 升级版为来源的 event KU 补入 2009 册同一记载。无 `no_delta`、无 `rejected`。
- KU 总数由 606 增至 609，event 类型由 112 增至 115；3 条新建中 `historical_event` 2 条、`professional_event` 1 条。
- 候选索引投影后：applied 662、no_delta 43、rejected 801、needs_evidence 3,833；active 3,833、terminal 1,506。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地点 | 主要增量 |
|---|---|---|
| events/6th-century-fangzhi-jishu-waichuan.md | 公元 6 世纪；中国、中亚、西亚、日本、波斯、拜占庭 | 脚踏纺车、提花机经阿富汗、伊朗西传；中国工匠到中亚、西亚传艺；和服“吴服”与江浙丝绸；波斯以竹筒带蚕种回国；东罗马派波斯僧侣藏蚕种于空心竹杖的异说；杀红花法、造靛法传入日本 |
| events/1972-1976-dingci-huifu.md | 1972—1976 年；北京、河北曲阳 | 田中角荣询问定瓷、周恩来答正在恢复；1974 年定瓷厂建立；两年后恢复工作展开；两次发掘定窑遗址，得“始烧于唐、兴盛于宋、失传于元”初步定论 |
| events/zhongguo-gongyi-meishupin-baihuajiang.md | 1981—1984 年；北京 | 第一至四届百花奖的评比与颁奖时间；各届代表性金杯奖作品与件数；第四届“中国工艺美术百花奖”名称异写 |

## 三、update 清单

| 候选 | 既有 KU | 补入内容 |
|---|---|---|
| cand-03-81 孝文改制 | events/xiao-wen-gai-zhi.md | 夏燕靖 2009 年表同条，文字与 2016 升级版基本一致 |
| cand-07-04 全国工艺美术艺人代表会议（1957） | events/national-craft-artists-conference-1957.md | 2009 年表明确记 7 月 22 日，与 2016 正文“1957 年 7 月”一致；补“保护、发展和提高”方针与“适用、经济、美观”原则的同一记载 |
| cand-07-11 周恩来 1972 年提倡手工艺 | events/zhou-enlai-handicraft-1972.md | 2009 年表同条，文字与 2016 基本一致 |
| cand-07-12 向联合国总部赠送工艺品（1974） | events/united-nations-gift-1974.md | 2009 年表所记 10 月 7 日赠送与天津、北京产地；任务下达与尺寸仍仅 2016 所记 |
| cand-07-13 全国工艺美术艺人、创作设计人员代表大会（1979） | events/crafts-artist-title-1979.md | 2009 年表同条，文字与 2016 基本一致，并同记 1 月赴日展览与 8 月 11 日学会恢复 |
| cand-07-16 全国高等院校工艺美术教学座谈会（1982） | events/national-crafts-education-symposium-1982.md | 2009 年表同条，文字与 2016 基本一致 |
| cand-07-20 中国工业设计代表团首次参加 ICSID'89 | events/icsid-1989-nagoya.md | 2009 年表同条，文字与 2016 基本一致 |

## 四、no_delta 判定

本批无 `no_delta`。7 个候选的既有 KU 虽已完整覆盖内容，但来源只列 2016 升级版，未列 2009 册；本批按“既有 KU 可承载但缺该来源”判 update，补入 2009 并在匹配质量中注明两版关系。

## 五、本批的判断

1. **同作者两版不作独立互证**：2009《中国设计史》与 2016《中国艺术设计史（升级版）》为同一作者的前后版，年表条目文字基本一致。本批在 `source_count` 中并列两版，是为记录版本连续性；`consensus` 仍为 `tentative`，不因两版同文而升为多源互证。
2. **先查既有专条再定 create / update**：1982 年教学座谈会、1957 年代表会议、周恩来讲话、联合国赠礼、1979 年称号、ICSID'89、孝文改制均已有 2016 版专条，故判 update，不另建重复条目；纺织外传、定瓷恢复、百花奖无既有专条，判 create。
3. **定瓷恢复与定窑 place KU 分工**：`places/ding-kiln.md` 已引 2009 L4331 记“始烧于唐、兴盛于宋、失传于元”的定论，但未展开 1972—1976 年恢复过程；本批新建 event KU 记恢复过程，并在相关知识元指向 place 条目，避免把窑系沿革与当代恢复混为一条。
4. **百花奖按届记，不合并为单次事件**：候选跨 1981—1984 年四届，来源逐届记评比、颁奖与代表作；KU 以“第一至四届”为时间范围，逐届列金杯奖作品，未把四届压成一次评奖。
5. **纺织外传的文本边界**：来源在“可见，我国丝绸的名贵，牵动”处中断，KU 照录并注明原文中断，不补写结句；和服上溯三国、蚕种传入拜占庭在 6 世纪中叶等时间差写入 date_note。
6. **维度判断**：纺织外传 E 维度（跨文化技术传播）、定瓷恢复 B 维度（工艺复原）、百花奖 D 维度（评奖制度）；三条均登记 `secondary_dimensions`。
7. **日期与名称照录**：1957 年会议日期以 2009 年表“7 月 22 日”与 2016 正文“1957 年 7 月”并列；第四届百花奖来源作“中国工艺美术百花奖”，与前三届“中国工艺美术品百花奖”名称略异，KU 两存。

## 六、本批的方法判断

- 10 个候选逐条回读原文段落，核对时间、地点、参与者、作品、引文与结果后再动笔；对应来源行段 10 处，其中 `L4694-L4711` 由周恩来讲话与联合国赠礼两个候选共用，已在 mapping 与 summary 中标明。
- update 先在磁盘取 `before` 指纹，再改文件，改后重算 `after`；apply-plan 的 before/after 双向核对通过。
- 7 个 update 均只补来源、`source_count`、匹配质量与参考文献，不改写既有正文事实；新建 3 条沿用事件 KU 的六节结构，`source_count: 1`、`confidence: medium`、`consensus: tentative`。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析、来源数与参考文献数一致性、六节结构检查，10/10 全部通过。
- 判定与写回分离：台账 30 行（10×3）、apply-plan 10 行（create 3、update 7）、mapping 10 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：30 行，10 个候选各 3 行；终态 applied 10。
- `apply-plan.jsonl`：10 行；create 3 行 `before` 为 null，update 7 行 `before` 为改前指纹对象；10/10 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：10 条（create 3、update 7），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:aaa3c28b…`（applied 652、no_delta 43、needs_evidence 3,843、rejected 801），批后 `sha256:3a715412…`（applied 662、no_delta 43、needs_evidence 3,833、rejected 801）；重建幂等。
- 内容质量审计：609 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 609/609 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 7 个 update 的第二来源为同一作者 2009 年前版，文字与 2016 升级版基本一致，不构成独立来源；后续若有其他作者或档案来源，应优先补证。
- 定瓷恢复未给定瓷厂规模、恢复品种、技师姓名与两次发掘报告；百花奖未记主办单位、评选标准、评委与参评规模；纺织外传未给外传具体年份、工匠姓名与日本遣使次数，且来源末句文本中断。
- 结构层仍为 0/4，层级完整挂载 0/609，正式 relation 0 条，Theme／Topic 均未实体化。
- 六册 event 候选已清空；剩余 `needs_evidence` unit 候选 2,470 个（event 0），另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_xiayanjing_batch_emit.py`、`_tmp_xiayanjing_batch_verify.py` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
