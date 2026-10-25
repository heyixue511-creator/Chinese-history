# term doc_count=2 第二批（xdup-0359—xdup-0389）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-term-doc2-batch-b/`
状态：`applied`

## 一、本批做了什么

- 覆盖 27 个 term 类型 doc_count=2 重复组，共 54 个候选。
- 新建 27 个 term KU，全部落在 `04-knowledge/units/terms/`。
- 每组一个 canonical 候选 `applied`，另一成员按“内容已并入”`rejected`。
- 候选索引投影后：applied 250、no_delta 10、rejected 548、needs_evidence 4531；active 4531、terminal 808。
- term doc2 累计关闭 56 组，仍开 80 组、160 个成员。

## 二、新建的 27 个 term KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0359 | 圆领袍衫（Round-Collar Robe） | garment_form | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0360 | 塑料（Plastic） | material_type | B | 赵农 2009、田自秉 2010 |
| xdup-0361 | 士（Shi / Scholar-Gentry） | social_group | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0362 | 壮锦（Zhuang Brocade） | textile_type | B | 高丰 2004、田自秉 2010 |
| xdup-0363 | 多子盒（Duozi Box） | container_form | B | 赵农 2009、田自秉 2010 |
| xdup-0364 | 天鸡壶（Tianji Ewer） | vessel_form | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0365 | 夹缬（Jiaxie） | textile_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0366 | 妆花（Zhuanghua） | textile_technique | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0367 | 宋体字（Songti Typeface） | typeface | C | 高丰 2004、赵农 2009 |
| xdup-0368 | 宋版书（Song Block-Printed Books） | print_genre | C | 赵农 2009、夏燕靖 2016 |
| xdup-0369 | 官窑（Guan Kiln） | ceramic_kiln | B | 赵农 2009、夏燕靖 2016 |
| xdup-0370 | 官营手工业（State-Run Handicraft Industry） | craft_system | D | 田自秉 2010、李立新 2011 |
| xdup-0372 | 小篆（Small Seal Script） | calligraphy_script | C | 高丰 2004、赵农 2009 |
| xdup-0374 | 工艺美术（Arts and Crafts） | design_discipline | D | 赵农 2009、李立新 2011 |
| xdup-0375 | 带柄工具（Hafted Tools） | tool_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0376 | 席（Mat） | furniture_form | B | 高丰 2004、夏燕靖 2016 |
| xdup-0377 | 帷帐（Curtain and Canopy） | interior_textile | B | 高丰 2004、赵农 2009 |
| xdup-0378 | 开片（Crackle Glaze） | ceramic_decoration | B | 赵农 2009、田自秉 2010 |
| xdup-0379 | 影青（Yingqing / Qingbai） | ceramic_type | B | 赵农 2009、田自秉 2010 |
| xdup-0380 | 忍冬纹（Honeysuckle Scroll Motif） | decorative_motif | C | 田自秉 2010、李立新 2011 |
| xdup-0381 | 戗金（Qiangjin） | lacquer_technique | B | 夏燕靖 2009、田自秉 2010 |
| xdup-0382 | 披帛（Pibo / Silk Shawl） | garment_accessory | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0385 | 提花机（Figured Loom） | device_type | B | 赵农 2009、夏燕靖 2016 |
| xdup-0386 | 搪瓷（Enamelware） | enamelware_type | B | 赵农 2009、田自秉 2010 |
| xdup-0387 | 敦（Dui） | vessel_form | B | 夏燕靖 2009、赵农 2009 |
| xdup-0388 | 文质（Wen and Zhi） | aesthetic_concept | A | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0389 | 斗拱（Dougong） | building_component | B | 赵农 2009、夏燕靖 2016 |

维度分布：A 1、B 20、C 3、D 3、E 0。

## 三、并列处理的三处语义分歧

1. **多子盒三义**：赵农给“多格食器”与“宋代耀州窑瓷盒”两义，田自秉给“汉代漆器多件套盒”一义。三者同名而材质、年代、功能不同，KU 以三义并列，不合并为单一定义。
2. **敦的功能两说**：夏燕靖称盛黍稷的食器，赵农称圆球体炖肉器具（上半部压力较重、加快熟烂）。器形与时代一致，功能判断冲突，未裁定。
3. **戗金的创始时代**：田自秉称宋代新创造、起源于战国针刻；夏燕靖将其列为秦汉漆器代表。两说并存。

另：官窑兼具“五大名窑之一”的窑口义与“官府生产体制”的制度义，正文已标明双重身份；天鸡壶与鸡头壶／鸡首壶为同一器类，别名并列，后续 `xdup-0468` 将并入本条而不另立。

## 四、维度判断说明

- 士、官营手工业、工艺美术归 D：分别对应社会阶层与知识制度、官府生产体制、学科与教育体制。
- 席、帷帐、多子盒、凭几等起居器物统一归 B，避免把家具史材料分散到 D。
- 文质归 A：它是“装饰与功能”命题在中国思想史中的最早表述，属设计观念而非造物技术。
- 宋体字、宋版书、小篆、忍冬纹归 C；忍冬纹按“跨门类表面装饰”处理，与吉祥图案同维度。

## 五、状态与验证

- `apply-plan.jsonl`：27 行 create，哈希 27/27 与磁盘一致。
- `candidate-decision-ledger.jsonl`：108 行，27 条 canonical 三段链 + 27 条 rejected。
- 内容质量审计：258 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 258/258 可解析。
- 候选索引：`sha256:1b9c33cd...f5815`，7,217,974 B，5,339 行。

## 六、边界与研究债

- 27 条均只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 塑料、搪瓷的产量与企业、宋版书的具体书目、斗拱的测绘数据，来源均未提供，本批不补写。
- `wenzhi` 的 2016 候选跨 L1455-L6138 整段范围，设计学转义句的具体位置待核；本批已在该条验证状态中标注。
- Theme/Topic 均未 materialize；relation 未审查，正文只写导航性相关条目。
- 剩余 term doc2 80 组待后续批次；`xdup-0468` 鸡头壶天鸡壶并入本批 `tianji-hu.md`。
