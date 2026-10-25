# 李立新《中国设计艺术史论》2011 册事件候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2011lilixin-events-batch/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从李立新《中国设计艺术史论》（2011）的未分组 unit 候选中，取 11 个 `event` 候选逐条回读原文并作语义裁决。
- 8 个判 `create`，新建 event KU；1 个判 `update`，向既有 event KU 补入李立新 2011 的记载；2 个判 `no_delta`（法门寺秘色瓷、天工开物，已由既有 term／publication KU 完整覆盖并已引李立新）；无 `rejected`。
- KU 总数由 598 增至 606，event 类型由 104 增至 112；8 条新建中 `historical_event` 4 条、`professional_event` 4 条。
- 候选索引投影后：applied 652、no_delta 43、rejected 801、needs_evidence 3,843；active 3,843、terminal 1,496。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地点 | 主要增量 |
|---|---|---|
| events/dongnan-daxue-yishuxuexi-1994.md | 1994 年 6 月，东南大学 | 张道一倡导组建，率先设立我国第一个艺术学系；北大、浙大、厦大等随后组建 |
| events/sheji-yishuxue-1998.md | 1998 年，中国 | 国务院学位委员会在研究生专业目录用“设计艺术学”取代“工艺美术学”；不只是名称更换，而是概念、范围、命题的转变 |
| events/fojiao-chuanru-zhongguo.md | 东汉，中国 | 丝路、西南、海路三路传入说；尼雅东汉腊缬棉布、沂南画像石佛像、孔望山摩崖造像、彭山一佛二菩萨像 |
| events/xiaowendi-jiangquan-nongsang.md | 北魏统一中原后，平城 | 设官营丝织作坊（“婢使千余人织绫锦”），又任民织造、遣散宫中机织工匠，民间纺织业再度活跃 |
| events/song-dai-huayuan-sheli.md | 宋代，宫廷 | 继西蜀、南唐设宫廷画院；“格法”“形似”成院体画特质，影响文思院、甲库、文绣院、绫锦院的设计生产 |
| events/xu-shou-hua-hengfang-zhengqi-ji.md | 同治元年 | 徐寿、华衡芳研制成中国第一部蒸汽机，来源称已达当时世界水平；因造价、材料能源与旧价值观未获实用 |
| events/wangzichao-shijian.md | 东周末年，周景王二十五年 | 王子朝率“旧官百工之丧职秩者”作乱；卫国两次工匠暴动；促使食官制衰落、匠人回归民间 |
| events/li-lixin-doctoral-defense-2002.md | 2002 年 6 月 15 日，东南大学 | 博士论文答辩通过；评审与答辩委员会名单；本书由论文《造物之迹——中国设计艺术史引论》修改完成 |

## 三、update 清单

| 候选 | 既有 KU | 补入内容 |
|---|---|---|
| cand-03-121 北魏孝文帝、孝明帝服饰改制 | events/xiaomingdi-fushi-gaige.md | 孝文帝制订朝服吸收熟悉南朝典制者参与设计；孝明帝改制后服饰趋向博大、程度超过南朝；胡服后演变为隋唐流行服装 |

## 四、no_delta 判定

| 候选 | 既有 KU | 覆盖依据 |
|---|---|---|
| cand-03-81 1987 年法门寺塔基地宫发现十三件秘色瓷 | terms/mise-porcelain.md | 已记 1987 年发现、李立新“十三件”说与夏燕靖 16 件、赵农“十余件”三说并列，并已引李立新 2011 原文 |
| cand-03-83 《天工开物》成书（1636 年） | publications/tiangong-kaiwu.md | 已记李立新作 1636 年撰成，与高丰、夏燕靖 1637 年刊行说并列，并已引李立新 2011 |

## 五、本批的判断

1. **create / update / no_delta 三分**：无对应实体者建专条（8 条）；既有 KU 主体相同但缺李立新记载者补写（1 条）；既有 term／publication 条目已完整覆盖并已引李立新者判 no_delta（2 条）。事件候选落到非 event 类型的既有 KU，说明候选的 `unit_type` 是提议而非裁决。
2. **候选兼含两帝时的归属**：`北魏孝文帝、孝明帝服饰改制` 跨越孝文帝朝服设计与孝明帝改制两个环节。既有 `xiaomingdi-fushi-gaige.md` 以孝明帝改制为主体，本批以 update 补入孝文帝环节作为前奏，并在 mapping 注明孝文帝整体汉化另见 `events/xiao-wen-gai-zhi.md`，不另建重复专条。
3. **来源判断照录主语**：佛教“艺术品的发现标志着佛教的传入”、尼雅人物为“希腊丰收女神或西亚女神伊什塔尔”、蒸汽机“已达当时世界水平”，均按来源原话保留“来源认为／有学者认为／来源称”，不提升为定论。
4. **同类事件不合并**：1998 年研究生专业目录改名与既有 `events/1998-moe-major-catalog.md`（本科专业目录调整）为两项不同层级的制度动作，本批另建 `sheji-yishuxue-1998`，两处互相链接而不合并。
5. **来源未载即写入证据边界**：东南大学艺术学系未给系所规模与审批文件；佛教传入未给年份与教团史料；蒸汽机未给形制、功率与试验记录；王子朝事件未给经过与人数；博士论文答辩未给决议与评分。均不引外部资料补全。
6. **维度判断**：8 条新建中 D 维度 5 条（学科建制、目录改名、农桑政策、画院制度、匠人身份），E 维度 1 条（佛教传入），B 维度 1 条（蒸汽机），A 维度 1 条（博士论文答辩）；其中 6 条登记 `secondary_dimensions`，记录工艺生产、视觉风格与学科训练的交叉归属。

## 六、本批的方法判断

- 11 个候选逐条回读原文段落，核对时间、地点、参与者、名单、引文与结果后再动笔；对应来源行段 11 处，`L341` 由两个候选共用（1994 年艺术学系与 1998 年目录改名），已在 mapping 与 summary 中标明。
- update 先在磁盘取 `before` 指纹，再改文件，改后重算 `after`；apply-plan 的 before/after 双向核对通过。
- 模板沿用事件 KU 的六节结构；新建 8 条为 `source_count: 1`、`confidence: medium`、`consensus: tentative`，不越级标 `high` 或 L1–L7。
- 佛教传入一条的时间、路线与实物证据均出自来源同一节的连续叙述，未拆分建条；宋代画院一条同时记录来源对院体画“贡献”与“束缚设计意匠”的正反判断，不代作者取舍。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析与六节结构检查，8/8 与 1/1 全部通过。
- 判定与写回分离：台账 33 行（11×3）、apply-plan 9 行（create 8、update 1）、mapping 11 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：33 行，11 个候选各 3 行；终态 applied 9、no_delta 2。
- `apply-plan.jsonl`：9 行；create 8 行 `before` 为 null，update 1 行 `before` 为改前指纹对象；9/9 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：11 条（create 8、update 1、no_delta 2），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:781faf8b…`（applied 643、no_delta 41、needs_evidence 3,854、rejected 801），批后 `sha256:aaa3c28b…`（applied 652、no_delta 43、needs_evidence 3,843、rejected 801）；重建幂等。
- 内容质量审计：606 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 606/606 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，events 112；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 8 条新建均为 `source_count: 1`（李立新 2011），未标 high confidence；本书偏重史学论证与制度判断，事件细节密度不均，后续若有第二来源应优先补证。
- 佛教传入与王子朝事件两条的年代边界最宽：来源分别只给“源头在东汉”“周景王二十五年”，未给公元纪年与前后过程；KU 保留空位而不补外部史实。
- `xiaomingdi-fushi-gaige.md` 为双源（赵农 2009、李立新 2011），但两册叙述高度重叠，增量集中在孝文帝环节与胡服去向；`consensus` 仍为 `tentative`。
- 结构层仍为 0/4，层级完整挂载 0/606，正式 relation 0 条，Theme／Topic 均未实体化。
- 六册剩余 `needs_evidence` unit 候选 2,480 个，其中 event 10 个（夏燕靖 2009）；另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_lilixin_events_items.py`、`_tmp_lilixin_events_emit.py`、`_tmp_lilixin_batch_emit.py`、`_tmp_lilixin_batch_verify.py` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
