# procedure doc_count=2 批次（xdup-0277—xdup-0286）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-procedure-doc2-batch/`
状态：`applied`

## 一、本批做了什么

- 覆盖 procedure 类型 doc_count=2 的全部 10 个重复组，共 20 个候选。
- 9 组 `create`，新建 9 个 procedure KU。
- 1 组 `update`：xdup-0279「夹缬」并入既有 `terms/jiaxie.md`，version 1→2。
- 10 个 canonical `applied`，10 个同组重复成员 `rejected`。
- 候选索引投影后：applied 485、no_delta 15、rejected 786、needs_evidence 4053；active 4053、terminal 1286。
- procedure doc2 累计关闭 10/10，**procedure 类型 doc_count=2 全部收口**。

## 二、新建的 9 个 procedure KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0277 | 吹灰法 | metalworking_technique | B | 夏燕靖 2009、田自秉 2010 |
| xdup-0278 | 夹纻胎 | lacquerware_technique | B | 高丰 2004、夏燕靖 2009 |
| xdup-0280 | 捣练法 | textile_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0281 | 泥条盘筑法 | ceramic_technique | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0282 | 琉璃烧造 | ceramic_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0283 | 转轮排字法 | printing_technique | C | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0284 | 鎏金 | metalworking_technique | B | 赵农 2009、田自秉 2010 |
| xdup-0285 | 铁范铸造 | metalworking_technique | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0286 | 雕版印刷 | printing_technique | C | 赵农 2009、夏燕靖 2016 |

维度分布：B 7、C 2。

## 三、update：夹缬并入 `terms/jiaxie.md`

1. **判据**：该条已存在，`type: term`、`sub_type: textile_technique`，已覆盖镂空版夹持、防染与色浆两条工艺路线、北魏形态、唐宋制度与“李装花”行业化；本组两候选同指一实体，另建 `procedures/jiaxie.md` 会造成同实体双条并跨类型同名。
2. **增补**：高丰 2004 的《事物纪原》转引《二仪实录》“秦汉间已有之，陈梁间贵贱通服之”、盛唐流行于宫廷、唐代军服用途、日本正仓院藏唐代夹缬屏风；田自秉 2010 的隋开皇六年（586）吐鲁番已有夹缬、可染两三色、花纹对称均衡、披巾衣裙与家具装饰。
3. **源流处理**：2016 作“上溯东汉”，高丰引《二仪实录》作“秦汉间已有”，田自秉以隋开皇六年吐鲁番实物为最早实证——三说年代不同层，并列保留，不裁定。
4. **不改的部分**：title、type、sub_type、既有段落与 aliases 保持原样；`source_count` 2→4、`version` 1→2。
5. **before 指纹**：编辑前直接对磁盘文件计算，`sha256:1001a471…`，4,133 B，86 行。

## 四、并列保留的分歧

1. **夹缬源流**：东汉（2016）／秦汉间已有（高丰引《二仪实录》）／隋开皇六年吐鲁番（田自秉）。
2. **夹缬唐代用途**：军服（高丰）与家具装饰（田自秉）。
3. **夹纻胎材料**：纻麻（2009xy）与麻布或丝绸（高丰）。
4. **捣练法文献**：两册均作班婕妤《捣练赋》（原文如此，未改）。
5. **泥条盘筑时代**：新石器时代（田自秉）与新石器时代至春秋战国（2016）。
6. **铁范器类首字**：2009xy 作“鏤”、2016 作“镰”，并列。
7. **鎏金时代**：赵农作战国中期已应用，田自秉 F 字段作春秋战国。
8. **吹灰法分离原理**：两册均只述“铅入灰中、纯银留存窠上”，未给化学解释。

## 五、本批的方法判断

- **工序类条目按“步骤可复述”组织核心内容**：每条把来源的做法拆成原料—工序—参数—效果，缺项明标“未见于来源”，不用外部工艺知识补全。
- **既有 term 覆盖同一工艺时走 update**：夹缬在早期已作为染缬术语建条，procedure 只是同一实体的另一种归类，故不新建。
- **印刷、排字归 C，其余工艺归 B**：转轮排字法与雕版印刷承担文字复制与版面设计功能，与既有 C 维度条目一致；冶金、漆、陶、纺织工序归 B。
- **时代冲突不靠“更晚即更准”裁决**：夹缬源流三说、泥条盘筑两说均并列，保留各册表述。

## 六、状态与验证

- `apply-plan.jsonl`：10 行（9 create + 1 update），哈希 10/10 与磁盘一致；update 行含 `before` 指纹。
- `candidate-decision-ledger.jsonl`：40 行（10×3 canonical + 10 rejected）。
- 内容质量审计：489 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 489/489 可解析，同名跨类型 3 组、消歧说明 6/6。
- 候选索引：5,339 行，`sha256:…` 与字节数见 `manifest.json`。
- 规则漂移 0；sync closure 19 步全部通过，250 tests + 16 subtests。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 工序类条目普遍缺操作参数（炉温、配比、工时、器具尺寸）与实验考古核对。
- 两册图版均未视觉核验。
- 「相关知识元」仍为纯文本，未建立 relation；Theme/Topic 均未 materialize。
- procedure doc2 已全关；仅剩 event doc2（9 组）与 doc1 组（6 组）即可结束重复组收口，之后转入 ungrouped unit 与 claim。
