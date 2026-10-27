# 2009 册 unit 批次 AT 摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-26-2009xiayanjing-units-batch-at/`
- 来源：夏燕靖《中国设计史》（2009），doc_id `2009-xiayanjing-zhongguo-shejishi`
- 候选范围：2009 册 unit 候选最后 16 条（cand-05 至 cand-07）
- 裁定结果：新建 8 条、更新 3 条、no_delta 4 条、rejected 1 条
- 状态：applied；16 条候选均进入终态，其中 applied 11、no_delta 4、rejected 1

## 2. 来源与复读范围

16 个候选共 16 处来源区间，去重后 13 段，并集 298 行：

`L3245, L3443, L3445, L3514, L3530, L3627-L3659, L3754-L3769, L3969-L3991, L4167-L4183, L4225-L4274, L4768-L4803, L5258-L5375`

其中 L3627-L3659 由大报恩寺塔与《工程作法》两候选共读；L4225-L4274 含飞鸽自行车，L4248-L4250 为地方与民族工艺美术品种清单，是前段子区间；L5258-L5375 由田自秉、王家树、龙宗鑫三本书目候选共读。L3443 前有 L3439 末句“云锦织”与 L3441 图 9-7 图注隔断，已按上下文读作云锦花纹样分类，并在条目内标明图版未视觉核验。

候选索引基线：5,339 行，CRLF→LF 归一后 `sha256:6766ba4eaf9bea62c19d1da0c8bbe9b24236a2e4bd614c61ec143d837ced155a`；裁定前计数 needs_evidence 2,908、applied 1,479、rejected 812、no_delta 140。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-05-88 | 元代寺庙壁画 | create | `terms/yuan-dai-simiao-bihua.md` |
| cand-05-90 | 云锦纹样七类 | update | `terms/nanjing-yunjin.md` |
| cand-05-92 | 清代丝织品种 | create | `terms/qing-dai-sizhi-pinzhong.md` |
| cand-05-93 | 明代女装与凤冠 | create | `terms/ming-dai-nvzhuang.md` |
| cand-05-94 | 清代首饰与头饰 | create | `terms/qing-dai-shoushi-toushi.md` |
| cand-06-02 | 金陵大报恩寺琉璃塔 | update | `works/dabaoensi-liuli-ta.md` |
| cand-06-04 | 《工程作法》 | update | `publications/gongcheng-zuofa.md` |
| cand-06-12 | 饾版 | no_delta | `procedures/duanban-taoyin.md` |
| cand-06-24 | 剪辫易服 | no_delta | `events/jianbian-yifu-1912.md` |
| cand-06-39 | 五星红旗 | no_delta | `works/prc-national-flag.md` |
| cand-06-43 | 飞鸽自行车 | no_delta | `works/flying-pigeon-bicycle.md` |
| cand-06-80 | 地方与民族工艺美术品种 | rejected | — |
| cand-07-17 | 《工艺美术参考》 | create | `publications/gongyi-meishu-cankao.md` |
| cand-07-32 | 田自秉《中国工艺美术史》 | create | `publications/tian-zizhu-zhongguo-gongyi-meishu-shi.md` |
| cand-07-33 | 王家树《中国工艺美术史》 | create | `publications/wang-jiashu-zhongguo-gongyi-meishu-shi.md` |
| cand-07-34 | 龙宗鑫《中国工艺美术史》 | create | `publications/long-zongxin-zhongguo-gongyi-meishu-shi.md` |

## 4. 新建 8 条

**服饰与织绣（3）**：清代丝织品种、明代女装与凤冠、清代首饰与头饰。三者均为清单级 term，分别记品种、服装形制与首饰头饰，不拆成单品种、单冠式或单首饰的微条。

**建筑装饰（1）**：元代寺庙壁画。作类型级 term，记元代建筑风格多样、寺庙壁画为重要建筑壁饰、道释题材与植物几何纹；具体寺院实例仍由 `works/sajia-si.md` 承载。

**出版与教育（1）**：《工艺美术参考》。期刊条，记 1982 年 7 月 1 日中央工艺美术学院编辑出版，1983 年起重点发表工业设计教育文论并引发全国设计教育培养方向讨论；归 D 维度。

**书目（3）**：田自秉《中国工艺美术史》（知识出版社 1985）、王家树《中国工艺美术史》（文化艺术出版社 1994）、龙宗鑫《中国工艺美术史》（陕西人民出版社 1985）。各条只记 2009 册参考书目所载作者、书名、出版者与年份，不扩写未载内容。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，created/updated/last_verified 为 2026-10-26、review_due 为 2027-04-26。四条 term 与《工艺美术参考》为 medium，三本书目条因仅一行书目信息定为 low。

## 5. 更新 3 条

| 目标 | 补入内容 | 版本变化 |
|---|---|---|
| `terms/nanjing-yunjin.md` | 2009 L3443 云锦花纹样依身份职业分贡品、时新、官服、吏服、商服、农服、僧道服饰七类；`term_note` 标明 L3439/L3441 的断行与图注隔断 | version 2→3，source_count 3 不变 |
| `works/dabaoensi-liuli-ta.md` | 2009 L3640、L3646-L3648 寺史沿革：孙吴赤乌三年长干寺及阿育王塔，历东晋、南朝、隋唐，南唐军营庐舍，北宋端拱元年僧可政得玄奘顶骨舍利建塔，天禧元年改天禧寺、塔名“圣感”，元至元二十五年改“元兴慈恩旌忠教寺”，明初复称天禧寺；并记西方七大奇观比较 | version 1→2，source_count 1→2 |
| `publications/gongcheng-zuofa.md` | 2009 L3658 异名“工程作法”、雍正十二年颁行、27 种构件、斗栱装修石作瓦作土作用工用料、加快施工但不利多样化；收“工程作法”为别名 | version 1→2，source_count 1→2 |

更新均只并入既有条目缺载的 2009 册事实，不改写原有来源内容。

## 6. no_delta 4 条

| 候选 | 既有承载 | 理由 |
|---|---|---|
| 饾版 | `procedures/duanban-taoyin.md` | 既有四源条已载分色分版、拱花、南京中心、1626《萝轩变古笺谱》与《十竹斋》两种，并说明“饾版”为来源外写法、“饱版”为 2016 同段异写，明确不另立条 |
| 剪辫易服 | `events/jianbian-yifu-1912.md` | 既有事件条已载限 20 天剪辫、孙中山“礼服在所必更，常服赐听民自便”与中山装设计；政策归 event，形制归 `terms/zhongshanzhuang.md` |
| 五星红旗 | `works/prc-national-flag.md` | 既有条已载 3,012 份应征、曾联松设计、田汉从淘汰图案中选图、去镰刀斧头与 9 月 27 日政协通过 |
| 飞鸽自行车 | `works/flying-pigeon-bicycle.md` | 既有条已载 1950 年 4 月试制、解剖菲利浦/堀井/凤头、640 毫米上管、大炉铜焊、十辆样品与 1951 年 1 月投放 |

## 7. rejected 1 条

cand-06-80“地方与民族工艺美术品种”跨 20 余省区与 10 余民族，来源 L4248-L4250 在同一段并列数十个产区与品种，不构成单一 term 边界；候选 `review_notes` 已声明“本候选是清单级聚合，不作为单一 KU 直接写回；落地时应按产区拆为 place 或按品种拆为 term/work”。本批 rejected，不写 KU；后续按产区或品种拆分另立批次，并逐项取证。

## 8. 语义判断与内部张力

1. **类型与实例分列**：元代寺庙壁画是类型条，`works/sajia-si.md` 是萨迦寺实例条；不把萨迦寺壁画等同为全部元代寺庙壁画。
2. **七类并入云锦条**：七类是云锦花纹样的身份职业分类，不是独立工艺；并入 `terms/nanjing-yunjin.md`，不另立“云锦纹样七类”微条。同数七类亦见于《蚕桑萃编》所记清代丝织品纹样，但主体不同，来源未说明二者关系，不合并。
3. **云锦与清代丝织品种分列**：`terms/qing-dai-sizhi-pinzhong.md` 记苏州、松江贡缎、广缎、洋缎、羽毛缎与杭州 14 大类、200 多品种、2,000 余花色，以及康熙八达晕、雍正多层经纬、乾隆巴洛克/洛可可三期风格；云锦另见 `terms/nanjing-yunjin.md`，八达晕另见 `terms/badayun.md`。
4. **凤冠霞帔分工**：明代女装条合记士庶女服、贵族高冠、后妃命妇凤冠与万历四种凤冠名目；霞帔的地色、禽纹与品级细节交 `terms/xiapei.md`。
5. **清代首饰按满汉、年龄与身份分记**：满族金镂花、银珐琅，汉族珠点翠、纸胎纱裱大花；少女簪钗栉环、中年“勒子”与“纂”、老年“冠子”与“网子”、贵妇“钿子之制”，合为一条而不拆微条。
6. **大报恩寺塔不新建同名 work**：既有条已载塔的形制、风铃 152、塔灯 140 与耗银 250 万两；2009 册补的是寺史沿革与西方七大奇观比较，故 update。
7. **《工程作法》与《工程做法》异名同指**：2009 册作“工程作法”，2016 册作“工程做法”；收异名为 alias，统一条目标题，不新建异名条。
8. **“饾版/短版/饱版”异写**：2009 册正文作“短版”，2016 册同段作“饱版”，候选作“饾版”；既有条以“短版”立目并说明异写，故 no_delta。
9. **政策与形制分工**：剪辫易服归 1912 年事件条，中山装形制归 `terms/zhongshanzhuang.md`；五星红旗归国旗 work；飞鸽自行车归自行车 work。
10. **书目条只记一行**：田自秉、王家树、龙宗鑫三本同名书各按 2009 册参考书目立条，不与 2010 田自秉修订本来源文档合并，也不据书名推补目录或观点。
11. **低置信条目**：三本书目条只有一行书目信息，《工艺美术参考》只有创刊与 1983 年办刊方向两点，四者 confidence 均为 low；其余四条 term 为 medium。
12. **图版未视觉核验**：云锦七类所在 L3443 前有图 9-7 图注，元代寺庙壁画、明代女装、清代首饰均涉及图版；相关条目未据图补形制、色彩或图版描述。

## 9. 引文审计与事后修正

- 引文审计：8 个新建条目与 3 个更新条目的净新增正文共 35 处双引号引文，逐条与来源去空白比对，0 遗漏。其中 33 处可在 2009 册找到逐字对应，2 处“工程做法”为 2016 册既有书名用语；ASCII 双引号未用于自拟表述。
- 事后修正：`terms/nanjing-yunjin.md` 原 `term_note` 把来源断句写作“花纹样……”（含省略号），与 L3443 原文不能逐字对应；改为只引“花纹样”，省略号移出引号，语义未变。修正后 sha256 `sha256:8d500e54be1c44c8f9d2f4b3d3abc84f5e2c6d94fc42cebe6a78023b9a9415c6`、5,894 字节、98 行；apply-plan 保留应用时原值 `sha256:a8e6affb...`，差异记入 `post-apply-corrections.json`。

## 10. 生成态与门禁

- 一致性复核：candidate-decision-ledger 46 行（15 候选×3 + cand-06-80 单行 rejected）、apply-plan 11 行（8 create + 3 update）、canonical-mapping 16 条；索引终态、target_ref、apply 后哈希/字节/行数、update 的 HEAD blob、六节结构均 0 问题。
- 索引重建：total 5,339 不变；applied 1,479→1,490、no_delta 140→144、rejected 812→813、needs_evidence 2,908→2,892；active 2,892、terminal 2,447。
- 内容审计：1,321 个知识元，0 发现。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18 步全部通过（250 tests passed, 16 subtests passed）。
- `python scripts/run_sync_closure.py --refresh-generated --check-generated`：[17/17] `check generated snapshots` FAILED exit=1，差异为工作树未提交的知识元与生成态快照，记 `blocked_pending_commit`，属设计行为。

## 11. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- 3 条 low confidence 书目条与 1 条 low confidence 期刊条只有来源内一行或两点信息，待后续册或来源外材料补证。
- cand-06-80 的产区与品种清单尚未拆分；后续需按 place 或 term/work 另立批次。
- 2009 册 unit 候选已全部处理完毕；本册 claim 候选尚未启动。
- Book 7 及以后不启动（用户范围限定）。
