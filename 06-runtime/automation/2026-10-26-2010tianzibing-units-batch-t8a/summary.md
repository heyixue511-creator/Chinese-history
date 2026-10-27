# 2010 册 units 批次 T8a（隋唐前半）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-26-2010tianzibing-units-batch-t8a/`
- 来源：田自秉《中国工艺美术史（修订本）》（2010），doc_id `2010-tianzibing-zhongguo-gongyi-meishushi`
- 候选范围：第七章隋唐工艺美术前半（L3016-L3246）的 unit 候选 24 条（cand-08-24 至 cand-08-108 之间的 needs_evidence 项）
- 裁定结果：新建 17 条、更新 6 条、no_delta 1 条、rejected 0 条
- 状态：applied（24 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：第七章隋唐的工艺美术前半（L3016-L3246），含隋唐概说、隋代陶瓷、唐代青瓷与白瓷、釉下彩与唐三彩、唐代染织的丝织品种、纹样、印染、刺绣，至百鸟毛裙条止。
- 截断点：L3246 为百鸟毛裙条末；L3248 起的刺绣、金属、漆木、家具与碑刻归 T8b。本章后半不提前纳入本批。
- 本批候选的 source span 并集经工作包计算为 60 行，见 `manifest.json.inputs.source.candidate_spans_union`。
- 插图 1 至 8 与相关彩版只读图注，未视觉核验。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-08-24 | 均田制 | create | `terms/juntian-zhi.md` |
| cand-08-29 | 经行记 | create | `publications/jingxing-ji.md` |
| cand-08-32 | 隋代龙柄双身壶 | create | `terms/sui-longbing-shuangshen-hu.md` |
| cand-08-104 | 越窑莲花碗荷叶形托（唐） | create | `works/yue-kiln-lianhua-wan-heye-tuo.md` |
| cand-08-105 | 白釉莲座烛台（唐） | create | `works/baiyou-lianzuo-zhutai.md` |
| cand-08-106 | 铜官窑釉罐（唐） | create | `works/tongguan-yao-you-guan.md` |
| cand-08-39 | 绞胎 | create | `terms/jiaotai.md` |
| cand-08-40 | 鲁山窑瓷拍鼓（唐） | create | `works/lushan-yao-ci-paigu.md` |
| cand-08-107 | 三彩罐（唐） | create | `works/sancai-guan.md` |
| cand-08-42 | 三彩女俑（唐） | create | `works/sancai-nv-yong.md` |
| cand-08-44 | “胡王”锦 | create | `works/huwang-jin.md` |
| cand-08-50 | 晕絰（原文写法） | create | `terms/yunjian.md` |
| cand-08-51 | 晕絰提花锦裙 | create | `works/yunjian-jin-qun.md` |
| cand-08-52 | 云头锦鞋 | create | `works/yuntou-jin-xie.md` |
| cand-08-55 | 桂管布 | create | `terms/guiguan-bu.md` |
| cand-08-56 | 白叠布 | create | `terms/baidie-bu.md` |
| cand-08-57 | 红线毯 | create | `terms/hongxian-tan.md` |
| cand-08-30 | 隋代白瓷 | update | `terms/baici.md` |
| cand-08-35 | 秘色 | update | `terms/mise-porcelain.md` |
| cand-08-36 | 青釉凤头龙柄壶 | update | `works/fengshou-longbing-hu.md` |
| cand-08-47 | 团窠纹 | update | `terms/tuanhua-wen.md` |
| cand-08-54 | 联珠鹿纹锦（唐） | update | `works/lianzhu-luwen-jin.md` |
| cand-08-58 | 百鸟毛裙 | update | `works/anle-gongzhu-yuqun.md` |
| cand-08-108 | 凤首龙柄壶（唐） | no_delta | `works/fengshou-longbing-hu.md` |

## 4. 新建 17 条

**制度与文献（2）**：均田制、《经行记》。

**陶瓷（8）**：隋代龙柄双身壶、越窑莲花碗荷叶形托、白釉莲座烛台、铜官窑釉罐、绞胎、鲁山窑瓷拍鼓、三彩罐、三彩女俑。

**染织与服饰（7）**：胡王锦、晕絰、晕絰提花锦裙、云头锦鞋、桂管布、白叠布、红线毯。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，日期 created/updated/last_verified 为 2026-10-26、review_due 为 2027-04-26，`academic_translation_status` 均为 provisional。confidence：medium 7 条（《经行记》、绞胎、胡王锦、晕絰、晕絰提花锦裙、桂管布、红线毯），low 10 条（均田制、龙柄双身壶、五件图版锚点器物、三彩女俑、云头锦鞋、白叠布）。

## 5. 语义判断与内部张力

1. **T8a/T8b 截断按候选定，不按整章记账**：本批复读止于 L3246，工作包 `scope_spans` 记 `[3016, 3246]`；L3248-L3467 的 19 条候选留给 T8b，不把整章写成已裁定。
2. **均田制只承担一句**：来源以一句带过，未述授田对象、亩数、年限与户籍；条目只记制度名称与“起了一定的促进作用”的判断，不据制度史常识补写，与 `terms/zuyongdiao.md` 分工互指。
3. **《经行记》是转引锚点**：来源只引杜环记大食首都京兆人樊淑、刘泚作画与河东人乐环、吕礼织络一条，用以说明唐代工匠国外传艺；原书体例、卷数与版本未载，不补。
4. **龙柄双身壶记器形不记器**：来源只有一句“六朝所未见、至唐代变为单身”，附图1 为隋代陶瓷造型总图；按器形条建 `terms/sui-longbing-shuangshen-hu.md`，与唐代 `works/fengshou-longbing-hu.md` 分列，不合并。
5. **图版锚点条的判据收窄**：原 T7 规则“只有图注的候选记 no_delta”过宽；本批改为：所指器物已由其他条目承担时记 no_delta，无其他条目承担时才建图版锚点作品条，并把尺寸、釉色、出土地、图像细节逐项标未载。越窑莲花碗荷叶形托、白釉莲座烛台、铜官窑釉罐、鲁山窑瓷拍鼓、三彩罐、三彩女俑、云头锦鞋七条据此建立。
6. **绞胎两处措辞并录**：L3134 一处称“绞胎是寿州窑的创造”，另一处称“绞釉和绞胎，出产在寿州”；条目并列，不合并为单一断言，也不补胎土配比与烧成温度。
7. **三彩三层分工**：`terms/tang-sancai.md` 记低温铅釉、器类与色彩的总类；`works/sancai-guan.md` 记器皿类图注；`works/sancai-nv-yong.md` 记人物俑类型描述。三者互指，不互相覆盖。
8. **胡王锦标隋代**：来源把胡王锦列在阿斯塔那古墓所出隋代丝织品，图案为一人牵骆驼；与唐代联珠鹿纹锦等分属两朝，不并入唐锦系统。
9. **晕絰照录原文写法**：原文作“晕絰”，与常见晕裥、晕繝不同；条目照录并记异写，不替来源裁定本字，也不与 `terms/yunse.md` 的晕色技法合并。
10. **桂管布与白叠布并列**：二者同为唐代棉布，但一为岭南桂管产地、一为长安市场记载，文献与信息层不同；分列两条，不因“都是棉布”合并。
11. **红线毯的丝毯判断归来源**：田自秉据白居易诗称红线毯以丝为原料、即现代所称丝毯，并称其比太原毛毯、蜀都锦毯更温且柔；条目把原料判断标为来源判断，不补宣州贡额与织法。
12. **白瓷补隋代烧成，不改北齐发明说**：`terms/baici.md` 原记北齐发明、范粹墓实物与邢窑；本批补田自秉的隋代烧成、由青瓷演变、精炼瓷土减铁与火度掌握、创始年代待考及隋代胎体与护胎釉。北齐与隋代两说层次不同，并列不裁断。
13. **秘色官督造两册并录**：`terms/mise-porcelain.md` 原把“御器厂或官窑前身”只归夏燕靖 2016；本批据田自秉 L3101 补唐代越窑设官督造与秘色得名，改正旧表述，但仍不裁断官督造的起止年代与机构名称。
14. **团窠即团花，四出忍冬不普适**：田自秉称团窠纹就是现在所称的团花，常以宝相花为主题，四窠之间缀忍冬而称四出忍冬；条目把它与高丰的自由式团花散点构成并列，不把四出忍冬写成所有团花的固定配置，也不把团窠等同于宝相花。
15. **联珠纹本土说照录不裁断**：田自秉以“联珠纹在我国一直运用着，而且具有极为悠久的历史”反驳波斯传入说；条目照录该论证，不把本土说写成已证结论，也不删除旧有的中西融合说。
16. **凤首龙柄壶窑口仍不作断言**：2010 册把青釉凤头龙柄壶写在越窑装饰段，可补 2016 册图注位置所缺的正文关联；但三册均无窑址或胎釉检测证据，条目只记田自秉的越窑归属，不升级为确定窑口。
17. **百鸟毛裙“目中”与“日中”并存**：夏燕靖 2016 作“目中为一色”，田自秉引《旧唐书·五行志》作“日中为一色”；条目仍照录 2016 原文并标疑，以 2010 册作旁证，不改字。
18. **重复图注记 no_delta**：cand-08-108 为插图9“凤首龙柄壶(唐)”图注，所指器物已由 cand-08-36 并入 `works/fengshou-longbing-hu.md`；单独立条只会得到重复空条，故记 no_delta。

## 6. 生成态与门禁

- 结构审计：`_zn_struct.py` 对 23 个文件（17 新建 + 6 更新），0 问题（13 个 frontmatter 字段、六节正文、ASCII 引号、悬空反引号链接、日期与状态字段均通过）。
- 引文审计：`_zn_checklines_t8a.py` 覆盖 17 个新建条目、64 处双引号逐字引文与田自秉 2010 册源文去标点比对，0 遗漏、0 越界、0 行号错配。
- 全库引文审计：`_zn_audit.py` 对 23 个文件初报 4 条 MISS，逐条修正后复跑 0 条发现。
- 索引重建：`build_discovery_index.py` 后 total 5339 不变；applied 2498→2521、needs_evidence 1772→1748、no_delta 217→218、rejected 852 不变；terminal 3567→3591、active 1772→1748。`build_translation_index.py` 后 translation index 1863 条（T7 后 1846，+17）；知识元 2255 条（T7 后 2238，+17 新建）。
- 工作包：apply-plan 23 行（17 create、6 update）、candidate-decision-ledger 72 行（24×3）、canonical-mapping 24 条、manifest 1 份。工作包在 candidate-index 写回前构建，`counts_before` 与 `sha256_before` 为写回前真实值（needs_evidence 1772、applied 2498、rejected 852、no_delta 217，rows 5339）。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18 步全部通过（250 tests passed, 16 subtests passed）。
- `python scripts/run_sync_closure.py --refresh-generated --check-generated`：实测 [17/17] check generated snapshots FAILED exit=1，因本批与既有未提交知识元、生成态快照未提交，记 `blocked_pending_commit`，属设计行为。

## 7. 跨批修正

- 规则收窄：`_zn_decisions_t8a.json` 与工作包 `manifest.json` 的“只有图注、无器物数据的候选记 no_delta”改为“所指器物已由其他条目承担时记 no_delta；无其他条目承担时建图版锚点作品条并标未视觉核验与逐项未载”，与本批 7 条图版锚点条的实际做法一致。
- `terms/mise-porcelain.md` 旧文把“御器厂或官窑前身”之说只归夏燕靖 2016；本批据田自秉 L3101 改为两册并录，并在匹配质量中说明表述范围。
- `terms/mise-porcelain.md` 正文原有 ASCII 双引号，结构审计报 18 条问题；已全部改为中文引号。
- `terms/mise-porcelain.md` 的 1987 年法门寺引文漏“陕西省”之“省”，与 2009 册原文不符；已补。
- `terms/mise-porcelain.md` 的李立新引文原用“……”省略图号括注，引文内省略号不合规且破坏逐字比对；已拆为两段引文，并注明原文图号括注不并入。
- `terms/mise-porcelain.md` 匹配质量中的自撰短语“官窑前身”原加引号，全库引文审计判 MISS；已去引号。
- `terms/baici.md` 的自撰短语“降铁”原加引号，全库引文审计判 MISS；已改为“降低含铁量技术”。

## 8. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- T8b 尚待执行：隋唐后半（L3248-L3467）19 条候选，18 新建 + 1 更新。
- 2010 册 unit 候选剩余量：T8b 19 条，另宋 37、元 16、明 38、清 43、近代 38 条；claim 候选 278 条未启动。
- 均田制的授田对象、亩数、年限、户籍与实施范围未载；《经行记》的卷数、成书年代与版本未载。
- 龙柄双身壶的尺寸、釉色、出土地与单体图注未载；图版锚点七件的尺寸、釉色、纹样细节、墓号与藏地均未载。
- 绞胎的胎土配比、绞合方法与烧成温度未载；三彩各件的窑口与产地未载。
- 胡王锦的尺寸、组织与藏地未载；晕絰的异写与本字关系未裁，提花锦裙与云头锦鞋的尺寸、组织未载。
- 桂管布、白叠布的幅宽、织法、产地范围与语源未载；红线毯的尺寸、织法与贡额未载。
- 白瓷的含铁量数值未载；秘色瓷的官督造起止年代与机构名称未决；凤首龙柄壶的窑口未定。
- 图版插图 1 至 8 未视觉核验。
- Book 7 及以后不启动（用户范围限定）。

## 9. 下一跳

- 执行 T8b：cand-08-63 神丝绣被、cand-08-64 卢眉娘、cand-08-66 唐代铜镇纸、cand-08-67 景云二年大钟、cand-08-70 唐代银薰炉、cand-09-02 论语玉烛、cand-09-04 海兽葡萄纹、cand-09-05 双鸾衔绶纹、cand-09-06 唐镜图案组织五式、cand-09-09 平文、cand-09-13 螺钿五弦琵琶、cand-09-17 库路真、cand-09-19 木画、cand-09-21 木画棋局、cand-09-94 双六局、cand-09-23 《萧翼赚兰亭图》、cand-09-25 大智禅师碑、cand-09-93 牡丹；更新 cand-09-26 卷草（唐草）→ `terms/tangcao-wen.md`。
