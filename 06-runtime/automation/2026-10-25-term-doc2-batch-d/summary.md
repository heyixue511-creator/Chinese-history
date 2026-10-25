# term doc_count=2 第四批（xdup-0417—xdup-0443）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-term-doc2-batch-d/`
状态：`applied`

## 一、本批做了什么

- 覆盖 27 个 term 类型 doc_count=2 重复组，共 54 个候选。
- 27 组全部判定 `create`，新建 27 个 term KU。
- 27 个 canonical `applied`，27 个同组重复候选 `rejected`。
- 候选索引投影后：applied 303、no_delta 11、rejected 602、needs_evidence 4423；active 4423、terminal 916。
- term doc2 累计关闭 110 组，仍开 26 组、52 个成员。

## 二、新建的 27 个 term KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0417 | 紫口铁足（Purple Mouth, Iron Foot） | ceramic_decoration | B | 田自秉 2010、赵农 2009 |
| xdup-0418 | 紫砂陶（Zisha Pottery） | ceramic_type | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0419 | 红木（Hongmu / Rosewood） | material_type | B | 赵农 2009、夏燕靖 2016 |
| xdup-0420 | 细石器（Microlith） | tool_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0421 | 经锦（Warp-Faced Brocade） | textile_technique | B | 高丰 2004、田自秉 2010 |
| xdup-0422 | 绞缬（Tie-Resist Dyeing） | textile_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0423 | 绫（Ling / Twill Silk） | textile_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0424 | 绿色设计（Green Design） | design_concept | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0425 | 编钟（Bianzhong） | musical_instrument | B | 赵农 2009、田自秉 2010 |
| xdup-0426 | 缥瓷（Piao Porcelain） | ceramic_type | B | 田自秉 2010、李立新 2011 |
| xdup-0427 | 美金与恶金（Meijin and Ejin） | material_concept | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0428 | 羼和料（Temper） | ceramic_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0429 | 耒耜（Leisi） | agricultural_tool | B | 赵农 2009、夏燕靖 2016 |
| xdup-0430 | 联珠纹（Linked-Pearl Motif） | decorative_motif | C | 高丰 2004、田自秉 2010 |
| xdup-0431 | 胡服（Hu Dress） | garment_form | E | 赵农 2009、夏燕靖 2016 |
| xdup-0432 | 脱胎漆器（Bodiless Lacquerware） | lacquerware_type | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0433 | 艺术设计（Art Design） | design_discipline | D | 夏燕靖 2009、赵农 2009 |
| xdup-0434 | 花釉（Splashed Glaze） | ceramic_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0435 | 花钿（Huadian） | cosmetic_accessory | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0436 | 苏式彩画（Suzhou-Style Painting） | architectural_painting | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0437 | 苏泥勃青（Sumali Blue） | ceramic_material | B | 赵农 2009、田自秉 2010 |
| xdup-0438 | 蓝田人（Lantian Man） | hominin | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0439 | 藏礼于器（Ritual Embedded in Vessels） | ritual_concept | A | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0440 | 蛋壳黑陶（Eggshell Black Pottery） | ceramic_type | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0441 | 蜀锦（Shu Brocade） | textile_type | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0442 | 蝴蝶装（Butterfly Binding） | book_binding | C | 高丰 2004、赵农 2009 |
| xdup-0443 | 褐（He / Coarse Woolen Cloth） | textile_type | B | 夏燕靖 2009、夏燕靖 2016 |

维度分布：A 1、B 21、C 2、D 2、E 1。

## 三、并列处理的语义分歧

1. **蓝田人年代**：2016 记“距今约 80 万—60 万年”，另处作“100 万—65 万年”，同册前后不一致；2009 作“约 100 至 65 万年”。两版并列，未裁定。
2. **联珠纹来源**：高丰主张联珠圈与动物纹的组合最早见于公元 3 世纪波斯萨珊王朝丝织品、南北朝经丝绸之路传入；田自秉明确反对“从波斯传入”之说，举中国新石器彩陶、北魏石砚、隋锦、敦煌藻井等说明中国联珠纹历史悠久。两说相反，全文照录。
3. **苏泥勃青来源**：赵农作“来自波斯”，田自秉作“南洋输入”。两说并列。
4. **紫砂陶初烧期**：田自秉记明代始盛，2016 记宋始烧、明代闻名、清代为高峰。已并入同一 KU，未统一。
5. **红木的性质**：2016 把红木界定为“明清以来稀有硬木统称、非特定树种”；赵农则记“红木”是 20 世纪末期中国社会重新出现的传统家具时尚。二者分指材料名与当代消费现象，并列保留。
6. **艺术设计的时间范围**：赵农把它作为 1980 年以后逐步形成的现代学科概念（1998 年教育部专业目录以之替代“工艺美术”）；夏燕靖把它界定为“人类有意识的、用艺术创造力所体现的造物活动”，可上溯原始社会。两种用法并列。
7. **胡服与带钩**：赵农补带钩／“钩络带”较丝绳绑扎更便捷，属两册中仅见的附件创新叙述；2016 未及。
8. **缥瓷定义口径**：田自秉作“青白色瓷器，即青瓷”，李立新作“淡青色玻璃釉青瓷”。并列。

## 四、本批的方法判断

- **藏礼于器与列鼎制度分工**：前者是观念命题（礼制等级编码于器物），后者是数量规则（鼎簋组合的等级序列）。本批把藏礼于器置于 A 维度，列鼎制度沿用既有条目，避免两处重复叙述同一制度。
- **艺术设计与工艺美术的分工**：既有 `terms/gongyi-meishu.md` 讲传统学科与行业，本条讲 1998 年前后的替代关系与现代设计运动，二者不合并。
- **绿色设计与工艺美术、艺术设计同属 D 维度**：三者均涉及学科、教育与设计观念的制度化，而非具体工艺。
- **胡服置 E 维度**：本条的主线是跨文化服饰功能移植（赵武灵王胡服骑射），不是中原服饰形制的常态演变。

## 五、状态与验证

- `apply-plan.jsonl`：27 行 create，哈希 27/27 与磁盘一致。
- `candidate-decision-ledger.jsonl`：108 行（27 条三段 applied 链 + 27 条 rejected）。
- 内容质量审计：311 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 311/311 可解析。
- 候选索引：`sha256:a35d7454...cb913`，7,235,061 B，5,339 行。
- 规则漂移 0；sync closure 19 步全部通过，250 tests + 16 subtests。

## 六、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 蓝田人的地层与测年方法、联珠纹各实例的织物编号、苏泥勃青的钴料成分分析，来源均未提供，本批未补写。
- 羼和料条记录了 2016 的两处 OCR 讹字（“稻草木和碎陶木”“露和料”），按原文照录并标注，未改动来源。
- 耒耜条记录赵农 L573“从未耜发展起来”疑为 OCR，按上下文标注。
- 「相关知识元」中引用的部分 `terms/*.md` 在本批后仍未建立（如 `terms/an.md`、`terms/guan-ying-shou-gong-ye.md`），属既有条目遗留的悬空路径，留待 term 批次收尾统一处理。
- Theme/Topic 均未 materialize；relation 未审查。
- 剩余 term doc2 26 组（52 个成员）待第五批处理。
