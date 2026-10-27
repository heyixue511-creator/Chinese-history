# 2010 册 units 批次 T3（周代）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-26-2010tianzibing-units-batch-t3/`
- 来源：田自秉《中国工艺美术史（修订本）》（2010），doc_id `2010-tianzibing-zhongguo-gongyi-meishushi`
- 候选范围：2010 册周代章节 unit 候选 21 条（cand-04 18 条、cand-05 3 条）
- 裁定结果：新建 19 条、更新 2 条、no_delta 0 条、rejected 0 条
- 状态：applied（21 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 复读区间：第三章周代的工艺美术（L1276-L1673），含概说、青铜工艺（烹饪器、食器、酒器、水器、乐器、兵器、工具与装饰）、陶瓷工艺、染织工艺、漆器工艺、玉雕工艺与结语。
- 彩版 7-8 与插图 1-16 只读图注，未视觉核验。
- 跨章的 `cand-05-08`（彩绘漆座屏）与 `cand-05-11`（龙凤虎纹绣衣）跨度落在战国章节，留春秋战国批次，不在本批裁定。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-04-07 | 周公 | create | `persons/zhou-gong.md` |
| cand-04-09 | 八材 | create | `terms/ba-cai.md` |
| cand-04-11 | 刖足奴铜鬲 | create | `works/yuezu-nu-tong-li.md` |
| cand-04-16 | 另鼎（音勿） | create | `works/ling-ding.md` |
| cand-04-18 | 两周金文辞大系图录考释 | create | `publications/liangzhou-jinwen-ci-daxi-tulu-kaoshi.md` |
| cand-04-20 | 窃曲纹 | create | `terms/qiequ-wen.md` |
| cand-04-22 | 环带纹 | create | `terms/huan-dai-wen.md` |
| cand-04-23 | 重环纹 | create | `terms/chong-huan-wen.md` |
| cand-04-24 | 垂鳞纹 | create | `terms/chui-lin-wen.md` |
| cand-04-25 | 瓦纹 | create | `terms/wa-wen.md` |
| cand-04-41 | 礼乐制度 | create | `terms/li-yue-zhidu.md` |
| cand-04-45 | 圭 | create | `terms/gui.md` |
| cand-04-46 | 璧 | create | `terms/bi.md` |
| cand-04-47 | 琮 | create | `terms/cong.md` |
| cand-04-48 | 璇玑 | create | `terms/xuanji.md` |
| cand-04-75 | 鸟纹 | create | `terms/niao-wen.md` |
| cand-05-14 | 玉鹿（宝鸡西周墓） | create | `works/yu-lu.md` |
| cand-05-30 | 周代玉礼器 | create | `terms/zhou-yu-liqi.md` |
| cand-05-87 | 玉人（洛阳东郊西周墓） | create | `works/yu-ren-luoyang.md` |
| cand-04-08 | 周代六工 | update | `terms/baigong.md` |
| cand-04-36 | 十二章 | update | `terms/twelve-symbols.md` |

## 4. 新建 19 条

**作品（4）**：刖足奴铜鬲、另鼎、玉鹿、玉人。

**术语（13）**：八材、礼乐制度、窃曲纹、鸟纹、环带纹、重环纹、垂鳞纹、瓦纹、圭、璧、琮、璇玑、周代玉礼器。

**人物（1）**：周公。

**文献（1）**：《两周金文辞大系图录考释》。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，日期 created/updated/last_verified 为 2026-10-26、review_due 为 2027-04-26，`academic_translation_status` / `translation_status` 均为 provisional。confidence：medium 18 条、low 1 条（璇玑）。

## 5. 更新 2 条

| 候选 | 既有条目 | 追加内容 | 计数变化 |
|---|---|---|---|
| cand-04-08 | `terms/baigong.md` | 田自秉据《考工记》的 30 工种职司、多工种协作、工师巫工三级管理；citation 追加 L1296-L1337、L1340 | source_count 4→5，version 1→2 |
| cand-04-36 | `terms/twelve-symbols.md` | 田自秉《书经·益稷篇》全文、十二章性质与历代沿用、袁世凯定服式、绘衣绣裳、汉宋注家、逐章含义；citation 追加 L1541-L1545 | source_count 1→2，version 1→2 |

两条均为跨册更新，新增 source block；原来源材料保留，正文另起段落，未覆盖。

## 6. 语义判断与内部张力

1. **六工由 no_delta 改判 update**：`terms/baigong.md` 已收六类工种的名称与 30／31 的算术矛盾，但未收田自秉逐一列出的 30 工种职司，也未收 L1340 的多工种协作与工师、巫、工三级管理。只记 no_delta 会丢失职司层，故按同实体更新，不新建重复工种条。
2. **十二章是跨册更新**：`terms/twelve-symbols.md` 原只据夏燕靖 2016 记清单、绘绣分工与《三礼图》释义，未收田自秉的《书经》全文、历代沿用、汉宋注家与逐章含义；两册释义同属儒家解释，并列而不合并为西周原义。
3. **另鼎器名存疑**：来源作“另(音勿)鼎”，字形与注音不合，未给正字。条目照录来源形式，slug 用 `ling-ding`，不据来源外材料改为通行器名。
4. **刖足奴与削足奴异文**：正文 L1357 作“刖足奴铜鬲”，图注 L1383 作“削足奴铜鬲”。条目从正文，图注原文并存，未径改。
5. **瓦纹第二句被图版隔断**：L1492 末句与 L1503 续句之间隔三幅插图，L1503 为残句。条目只逐字引 L1492 的完整句，L1503 改为转述，不用「 」拼接残句。
6. **玉器分条的分工**：`terms/rui-yu-liuqi.md` 记《周礼》六器成套规范，`terms/yu-yue-cong-bi.md` 记良渚玉钺、玉琮、玉璧。本批另立圭、璧、琮、璇玑四条类型条与周代玉礼器一条制度条：类型条只记形制、等类与用途，制度条记伦理地位、礼器用途、玦璜、陪葬位置与佩饰，互指而不重复。
7. **命圭等级的归属**：镇圭、桓圭、信圭、躬圭与天子用全、上公陇、侯瓒、伯将均属圭的等级，写入 `terms/gui.md`；周代玉礼器条只总述“体现等级名分”，不重复四级尺寸。
8. **两周金文辞大系图录考释不归作者**：来源只引其统计，未提作者；`persons/guo-moruo.md` 虽记郭沫若，本条不据来源外材料把书归给郭沫若。
9. **璇玑取 low confidence**：来源只有一句形制与“有谓是从天文仪器演变而来，其意义难以明了”，条目照录存疑，不补用途。
10. **八材的“象（牙）”**：来源括注指象牙，不是象这种动物；八材只列名目，不排与六工的对应表。
11. **玉鹿与玉人分条**：二者同出 L1664 一句并举，但分属宝鸡西周墓与洛阳东郊西周墓，形象与器类不同，各立作品条；洛阳玉人另与商代妇好墓跪坐玉人分条。
12. **图版层与正文层分开**：彩版 7-8、插图 1-16 只著录图注，不据图补尺寸、藏地与出土层位；刖足奴铜鬲、玉鹿等器的尺寸与墓号来源未载。

## 7. 生成态与门禁

- 结构审计：`_zn_struct.py` 19 个新建文件与 2 个更新文件 0 问题。
- 引文审计：19 个新建条目 74 处双引号逐字引文，逐条与田自秉 2010 册源文去标点比对，0 遗漏、0 行号错配；更新条目的新增引文另核 L1296-L1340、L1541-L1545，均落在所标行。
- 全库引文审计：`_zn_audit.py` 对两个更新文件报 6 条既有问题（“百工是谁”“百工做什么”、《礼记·曲礼》引文、“覩氏”“㡛氏”、“商族/商旅”），均在 T3 新增段落之外，属既有文本；本批未新增。
- 索引重建：total 5339 不变；applied 2387→2408、needs_evidence 1905→1884、rejected 852 不变、no_delta 195 不变；terminal 3434→3455。知识元 2143→2162；translation index 1751→1770。
- 工作包：apply-plan 21 行（19 create、2 update）、candidate-decision-ledger 63 行（21×3）、canonical-mapping 21 条、manifest 1 份。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18 步全部通过（250 tests passed, 16 subtests passed）；结构健康分 102、类型覆盖 8/8；内容质量发现 12 条均为既有问题（liezi-tangwen、songshi-yufuzhi、armillary sphere、zhao-nong、zhongguo-yishu-shejishi-zhaonong-2009、he-zun），本批未新增；relation 审计 0 broken、0 invalid、0 missing inverse，孤立知识元 2162。
- `python scripts/run_sync_closure.py --refresh-generated --check-generated`：[17/17] FAILED exit=1，因本批与既有未提交知识元、生成态快照未提交，记 `blocked_pending_commit`，属设计行为。

## 8. 跨批修正

- 本批无跨批语义修正。
- `terms/baigong.md` 由 version 1 升为 2，`terms/twelve-symbols.md` 由 version 1 升为 2；两条的 `updated` / `last_verified` 续为 2026-10-26，`review_due` 续为 2027-04-26。
- manifest 的 outputs 说明由“三件青铜与玉器作品”更正为“四件”，与新建清单一致。

## 9. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- 2010 册 unit 候选剩余 332 条（353−21）；claim 候选 278 条未启动。
- 战国章节的彩绘漆座屏（cand-05-08）、龙凤虎纹绣衣（cand-05-11）留春秋战国批次。
- 璇玑条为 low confidence：来源自陈意义难明，只有形制与一说。
- 另鼎的器名正字、刖足奴铜鬲的尺寸与藏地、玉鹿与玉人的墓号均未载，未做来源外核对。
- 图版彩版 7-8 与插图 1-16 未视觉核验。
- Book 7 及以后不启动（用户范围限定）。
