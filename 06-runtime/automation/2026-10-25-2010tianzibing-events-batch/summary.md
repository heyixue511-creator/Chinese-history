# 田自秉《中国工艺美术史（修订本）》2010 册事件候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2010tianzibing-events-batch/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从田自秉《中国工艺美术史（修订本）》（2010）的未分组 unit 候选中，取 22 个 `event` 候选逐条回读原文并作语义裁决。
- 12 个判 `create`，新建 event KU；8 个判 `update`，向既有 event KU 补入田自秉 2010 的记载；2 个判 `no_delta`；无 `rejected`。
- KU 总数由 586 增至 598，event 类型由 92 增至 104；12 条新建中 `historical_event` 10 条、`professional_event` 2 条。
- 8 个 update 文件的 `sources` 由 9 条增至 17 条（banama-saihui 增至 3 源，其余 7 个各 2 源）。
- 候选索引投影后：applied 643、no_delta 41、rejected 801、needs_evidence 3,854；active 3,854、terminal 1,485。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地点 | 主要增量 |
|---|---|---|
| events/ping-wang-dong-qian.md | 公元前 771 年，镐京→洛邑 | 平王东迁；迁都前称西周、迁都后称东周 |
| events/zhou-initial-wine-ban.md | 周初（未给年份） | 周初禁酒令；商代发达酒器工艺渐衰，爵、斝、觚、觯、卣至西周后期消失或绝迹 |
| events/huangjin-uprising.md | 东汉末年 | 黄巾大起义；山东画像石制作随之衰落 |
| events/liuchao-buddhist-caves.md | 六朝，云冈／龙门／敦煌 | 北方大凿石窟、南方广建寺院；吸收犍陀罗艺术并创造新风格 |
| events/sui-conquers-chen.md | 589 年，南朝陈 | 隋灭陈，结束 260 多年南北分裂，为唐代经济文化繁荣打下基础 |
| events/tang-ban-jinyin-pingtuo.md | 唐肃宗、代宗时 | 两朝严加禁止金银平脱；禁令因工艺费时、价格昂贵 |
| events/taiping-tianguo.md | 清代后期，天京 | 太平天国诸匠营、百工衙；“益民”工艺观与奖励发明政策；生丝输出由 1853 年前 2 万多包增至 1860 年间 8 万多包 |
| events/kangxi-abolish-loom-quota-1712.md | 康熙五十一年（1712） | 废除机户织机百张限额，染织工艺得以继续发展 |
| events/da-shengchan-yundong.md | 1941—1942 起，陕甘宁边区 | 大生产运动；染织、陶瓷、玻璃、木工、编织、装潢等工艺应运而生 |
| events/national-lacquer-conference-1959.md | 1959 年，福州 | 全国漆器交流参观会议，19 个省市自治区参加；来源称漆工艺史上的一件大事 |
| events/party-third-plenum.md | 来源作“党的三中全会”，另处作“党的十一届三中全会”，未给年份 | 拨乱反正、改革开放；工艺美术在十年动乱后迅速恢复和发展 |
| events/zhongguo-gongyi-meishushi-completed.md | 1982 年冬，北京 | 《中国工艺美术史》编写完成并作后记；来源自述“引玉之砖” |

## 三、update 清单

| 候选 | 既有 KU | 补入内容 |
|---|---|---|
| cand-04-42 武王灭商 | events/king-wu-conquers-zhou.md | 周文王时国势渐强、武王联合各部落灭商建周、建都镐京；加别名“武王灭商” |
| cand-06-49 秦统一六国 | events/qin-mie-liuguo.md | 商鞅变法基础、灭国顺序（韩赵魏楚燕齐）、吸收他国文化、没收民间兵器运咸阳销毁、“统一性和巨大性”判断 |
| cand-09-03 千秋节 | events/qianqiu-festival.md | 引《唐书·礼乐志》、群臣献甘露寿酒与铜镜祝寿互赠、“千秋金鉴节”别称、赏赐／纪念／有柄舞镜等用途 |
| cand-09-28 北宋建立 | events/chenqiao-mutiny.md | 960 年赵匡胤夺取政权、定都东京（今开封）、结束唐末以来分裂割据、辽与西夏并立；田自秉未用“陈桥驿”之名 |
| cand-09-29 靖康之变与南迁 | events/jingkang-zhibian.md | 1125 年辽亡于金、1127 年金兵破开封、宋室南迁临安、宋金对峙、1279 年南宋亡于元 |
| cand-11-18 郑和七下西洋 | events/zhenghe-voyages.md | 成祖派太监郑和、远到亚非 30 多个国家、扩大中外经济文化交流；迁都北京与安定西北的同期举措 |
| cand-13-58 1958 年首次全国艺人代表会议 | events/national-craft-artists-conference-1957.md | 1958 年“首次全国艺人代表会议”与 1979 年代表会议；艺人归队政策背景 |
| cand-13-61 1914 年巴拿马博览会北京雕漆获奖 | events/banama-saihui.md | 北京雕漆 1914 年获一等奖、民国初年畸形发展、多仿清作品；解放后雕漆厂品种与镂空手法 |

## 四、no_delta 判定

| 候选 | 既有 KU | 覆盖依据 |
|---|---|---|
| cand-13-59 1979 年全国工艺美术艺人、创作设计人员代表大会 | events/crafts-artist-title-1979.md | 已记 1979-08-08—16 会议、杨士惠等 34 人获“工艺美术家”称号、8 月 11 日学会恢复 |
| cand-14-18 中央工艺美术学院成立 | institutions/central-academy-arts-design.md | 已记 1956-05-21 国务院批准、11-01 建院典礼，并明记田自秉只记 1956 年学院成立 |

## 五、本批的判断

1. **create / update / no_delta 三分**：既有同题 KU 已存在但缺田自秉 2010 记载的判 `update`（8 条）；既有专条已完整覆盖的判 `no_delta`（2 条）；无对应实体的判 `create`（12 条）。更新而非另建，避免同一事件出现并列专条。
2. **三处年份分歧并列保留**：1957-07-22（夏燕靖 2016）对 1958 年首次全国艺人代表会议（田自秉）；1915-02-20 开幕（两册夏燕靖）对 1914 年北京雕漆获奖（田自秉）；南宋亡于 1276 年临安陷落（夏燕靖 2016）对 1279 年亡于元（田自秉）。三处均写 `date_note` 与匹配质量，不作来源外裁决，也不改写既有日期。
3. **名实不符照录**：田自秉记 960 年赵匡胤夺取政权、建都东京、结束分裂，全段未用“陈桥驿”之名；条目保留事件名而注明田自秉未用该名，未据外部史实补写兵变过程。
4. **来源未载即写入证据边界**：大生产运动未给结束年，太平天国未给起止年，黄巾起义未给年份，党的三中全会未给年份与届次；均照录为待补，不引外部资料。
5. **同段多事分别建条**：田自秉 L3476 一段同记北宋建立、辽亡、靖康南迁与南宋亡，按事件边界分入 `chenqiao-mutiny` 与 `jingkang-zhibian` 两条，并在两处注明同源段落，不重复叙述对方内容。
6. **维度判断**：12 条新建中 D 维度 10 条（迁都、禁酒、起义、统一战争、工艺禁令、农民政权、匠役政策、根据地生产、行业会议、政策转向），B 维度 1 条（六朝石窟与佛教工艺），A 维度 1 条（工艺美术史书写完成）；其中 10 条同时登记 `secondary_dimensions`，记录工艺生产与制度、跨文化的交叉归属。

## 六、本批的方法判断

- 22 个候选逐条回读原文段落，核对时间、地点、参与者、数量、引文与结果后再动笔；对应来源行段 23 处，`L3476` 与 `L5051` 各由两个候选共用，已在 mapping 与 summary 中标明。
- 8 个 update 先在磁盘取 `before` 指纹，再改文件，改后重算 `after`；apply-plan 的 before/after 双向核对通过，避免覆盖他人未记录的改动。
- 模板沿用事件 KU 的六节结构；新建 12 条为 `source_count: 1`、`confidence: medium`、`consensus: tentative`，不越级标 `high` 或 L1–L7。
- update 同步维护 `source_count`、`sources`、`source_basis`、描述、核心内容、匹配质量与参考文献七处，避免出现“来源两条、参考文献一条”的半更新状态；写后脚本复核 `source_count == len(sources) == 参考文献条数`。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入；写后用 YAML 解析与六节结构检查，12/12 与 8/8 全部通过。
- 判定与写回分离：台账 66 行（22×3）、apply-plan 20 行（create 12、update 8）、mapping 22 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：66 行，22 个候选各 3 行；终态 applied 20、no_delta 2。
- `apply-plan.jsonl`：20 行；create 12 行 `before` 为 null，update 8 行 `before` 为改前指纹对象；20/20 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：22 条（create 12、update 8、no_delta 2），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:1d7195a2…`（applied 623、no_delta 39、needs_evidence 3,876、rejected 801），批后 `sha256:781faf8b…`（applied 643、no_delta 41、needs_evidence 3,854、rejected 801）；重建幂等。
- 内容质量审计：598 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 598/598 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，events 104；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 规则漂移审计 0 findings；Skill registry 18 个 leaf、0 router；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 250 项通过、16 项 subtests 通过。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 12 条新建均为 `source_count: 1`（田自秉 2010），未标 high confidence；田自秉叙述多为章节概说与制度背景，事件过程细节有限，后续若有第二来源应优先补证。
- 3 条新建的事实边界最窄：黄巾起义只记“山东画像石衰落”的后果，党的三中全会未给届次与年份，大生产运动未给结束年；KU 保留空位而不补外部史实。
- 8 个 update 中 7 个为双源、1 个为三源，但仍未做来源外核对；两册分歧只并列不裁决，`consensus` 仍为 `tentative`。
- 结构层仍为 0/4，层级完整挂载 0/598，正式 relation 0 条，Theme／Topic 均未实体化。
- 六册剩余 `needs_evidence` unit 候选 2,491 个，其中 event 21 个（李立新 11、夏燕靖 2009 10）；另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 本批临时脚本（`_tmp_tianzibing_events_items.py`、`_tmp_tianzibing_events_emit.py`、`_tmp_tianzibing_batch_emit.py`、`_tmp_tianzibing_batch_verify.py`、`_tmp_tianzibing_update_verify.py` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
