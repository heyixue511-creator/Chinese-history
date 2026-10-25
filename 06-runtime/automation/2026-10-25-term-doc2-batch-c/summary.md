# term doc_count=2 第三批（xdup-0390—xdup-0416）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-term-doc2-batch-c/`
状态：`applied`

## 一、本批做了什么

- 覆盖 27 个 term 类型 doc_count=2 重复组，共 54 个候选。
- 新建 26 个 term KU。
- 1 组判定 `no_delta`：`xdup-0409` 百工制度，并入既有 `terms/baigong.md`。
- 26 个 canonical `applied`，27 个同组重复候选 `rejected`，1 个 canonical `no_delta`。
- 候选索引投影后：applied 276、no_delta 11、rejected 575、needs_evidence 4477；active 4477、terminal 862。
- term doc2 累计关闭 83 组，仍开 53 组、106 个成员。

## 二、新建的 26 个 term KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0390 | 新石器时代（Neolithic Period） | archaeological_period | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0391 | 明光铠（Mingguang Armor） | armor_form | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0392 | 明器（Mingqi） | burial_good | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0393 | 景泰蓝（Cloisonné） | enamelware_type | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0394 | 月份牌（Yuefenpai） | advertising_form | C | 高丰 2004、赵农 2009 |
| xdup-0395 | 柴窑（Chai Kiln） | ceramic_kiln | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0396 | 案（An / Table） | furniture_form | B | 赵农 2009、夏燕靖 2016 |
| xdup-0397 | 梅瓶（Meiping） | vessel_form | B | 高丰 2004、赵农 2009 |
| xdup-0398 | 楼船（Tower Ship） | ship_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0399 | 歙砚（She Inkstone） | inkstone_type | B | 赵农 2009、田自秉 2010 |
| xdup-0400 | 沙船（Shachuan） | ship_type | B | 赵农 2009、夏燕靖 2016 |
| xdup-0401 | 清代家具三大名作（Three Great Qing Furniture Styles） | furniture_style | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0402 | 火花（Matchbox Label） | advertising_form | C | 赵农 2009、夏燕靖 2016 |
| xdup-0403 | 犀皮（Xipi） | lacquer_technique | B | 高丰 2004、田自秉 2010 |
| xdup-0404 | 独轮车（Wheelbarrow） | vehicle_type | B | 赵农 2009、夏燕靖 2016 |
| xdup-0405 | 玉壶春瓶（Yuhuchun Vase） | vessel_form | B | 赵农 2009、夏燕靖 2016 |
| xdup-0406 | 玻璃（Glass） | material_type | B | 赵农 2009、田自秉 2010 |
| xdup-0407 | 甲骨文（Oracle Bone Script） | script_form | C | 赵农 2009、夏燕靖 2016 |
| xdup-0408 | 白瓷（White Porcelain） | ceramic_type | B | 赵农 2009、夏燕靖 2016 |
| xdup-0410 | 相缬（Xiangxie） | textile_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0411 | 石榴裙（Pomegranate Skirt） | garment_form | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0412 | 租庸调（Zu-Yong-Diao） | tax_system | D | 田自秉 2010、夏燕靖 2016 |
| xdup-0413 | 窑变（Kiln Transmutation） | ceramic_decoration | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0414 | 端砚（Duan Inkstone） | inkstone_type | B | 赵农 2009、田自秉 2010 |
| xdup-0415 | 簠（Fu） | vessel_form | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0416 | 粤绣（Yue Embroidery） | embroidery_type | B | 夏燕靖 2009、田自秉 2010 |

维度分布：A 0、B 23、C 2、D 1、E 0。

## 三、`no_delta`：百工制度

`terms/baigong.md` 已有别名“百工制度”，并已引高丰 2004 L947、L949-L953（百工为直接服务于王室、由官长率领的手工业者，殷商至战国延续一千余年）与李立新 2011 L827（《礼记·曲礼》六工分职、春秋战国制度成熟）。本组两候选所指内容与既有 KU 完全重叠，无新增字段或段落，故判定 `no_delta`，两个候选均不再单独写回。

## 四、并列处理的语义分歧

1. **沙船创制时代**：2016 记 period 为唐，赵农记其为宋代海船制造中出现的平底船样式。
2. **犀皮创始期**：田自秉称宋代新创造，高丰以东吴朱然墓出土犀皮耳杯为最早实物，上限推至三国。
3. **玉壶春瓶时代**：赵农置于宋代典型瓷瓶，2016 称元代最有特色的瓶式；口部描述亦有“外斜／喇叭”之别。
4. **梅瓶肩部**：赵农作“圆肩”，高丰作“丰肩”；审美评价一为“秀丽媚妩”，一为“挺拔刚劲”。
5. **楼船层数**：2009 作三层至 5 层甚至 10 层，2016 作高 10 余丈、分数层。
6. **窑变成色机制**：田自秉作铜元素还原，2016 作“铜的气化物”并自带“原文如此”存疑标注。

以上均并列保留，未裁定。

## 五、状态与验证

- `apply-plan.jsonl`：26 行 create，哈希 26/26 与磁盘一致。
- `candidate-decision-ledger.jsonl`：108 行（26 条三段 applied 链 + 1 条三段 no_delta 链 + 27 条 rejected）。
- 内容质量审计：284 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 284/284 可解析。
- 候选索引：`sha256:a7b08640...d40b`，7,226,649 B，5,339 行。

## 六、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 柴窑的窑址与实物、端砚与歙砚的坑口分级、粤绣 1900 年出口值的原始海关数据，均未在来源外核对。
- 甲骨文的甲骨片数、著录与缀合情况，来源未提供；本批未补写。
- Theme/Topic 均未 materialize；relation 未审查。
- 剩余 term doc2 53 组（106 个成员）待第四、五批处理。
