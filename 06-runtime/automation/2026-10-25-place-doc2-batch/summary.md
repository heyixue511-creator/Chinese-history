# place doc_count=2 批次（xdup-0252—xdup-0276）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-place-doc2-batch/`
状态：`applied`

## 一、本批做了什么

- 覆盖 place 类型 doc_count=2 的全部 25 个重复组，共 50 个候选。
- 23 组 `create`，新建 23 个 place KU。
- 1 组 `update`：xdup-0261「哥窑」并入既有 `terms/ge-yao.md`，version 1→2。
- 1 组 `no_delta`：xdup-0255「云岗石窟」并入同批新建的 `places/yungang-shiku.md`（异写）。
- 25 个 canonical 全部处置，25 个同组重复成员 `rejected`。
- 候选索引投影后：applied 475、no_delta 15、rejected 776、needs_evidence 4073；active 4073、terminal 1266。
- place doc2 累计关闭 25/25，**place 类型 doc_count=2 全部收口**。

## 二、新建的 23 个 place KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0252 | 三星堆 | archaeological_site | B | 赵农 2009、夏燕靖 2016 |
| xdup-0253 | 临淄 | city | D | 赵农 2009、夏燕靖 2016 |
| xdup-0254 | 云冈石窟 | archaeological_site | B | 赵农 2009、李立新 2011、田自秉 2010、夏燕靖 2016 |
| xdup-0256 | 仙人洞遗址 | archaeological_site | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0257 | 偃师商城 | archaeological_site | B | 赵农 2009、夏燕靖 2016 |
| xdup-0258 | 南京 | city | D | 赵农 2009、夏燕靖 2016 |
| xdup-0259 | 吉州窑 | kiln_site | B | 赵农 2009、田自秉 2010 |
| xdup-0260 | 周口店遗址 | archaeological_site | B | 田自秉 2010、李立新 2011 |
| xdup-0262 | 大兴城 | city | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0263 | 大地湾遗址 | archaeological_site | B | 赵农 2009、李立新 2011 |
| xdup-0264 | 妇好墓 | archaeological_site | B | 赵农 2009、夏燕靖 2016 |
| xdup-0265 | 宜兴 | kiln_site | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0266 | 山顶洞遗址 | archaeological_site | B | 赵农 2009、田自秉 2010 |
| xdup-0267 | 庙底沟遗址 | archaeological_site | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0268 | 建窑 | kiln_site | B | 赵农 2009、田自秉 2010 |
| xdup-0269 | 敦煌莫高窟 | archaeological_site | B | 李立新 2011、夏燕靖 2016 |
| xdup-0270 | 曾侯乙墓 | archaeological_site | B | 李立新 2011、夏燕靖 2016 |
| xdup-0271 | 满城汉墓 | archaeological_site | B | 田自秉 2010、李立新 2011 |
| xdup-0272 | 瓯窑 | kiln_site | B | 赵农 2009、田自秉 2010 |
| xdup-0273 | 耀州窑 | kiln_site | B | 赵农 2009、田自秉 2010 |
| xdup-0274 | 醴陵 | kiln_site | B | 赵农 2009、田自秉 2010 |
| xdup-0275 | 雍城 | city | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0276 | 马王堆汉墓 | archaeological_site | B | 高丰 2004、田自秉 2010 |

维度分布：B 19、D 4。类型分布：archaeological_site 14、kiln_site 5、city 4。

## 三、update 与 no_delta

1. **update：哥窑并入 `terms/ge-yao.md`**。
   - **判据**：该条已存在且把哥窑定为 term（`sub_type: ceramic_kiln`）；窑址至今未发现，不宜另立 place 条目，另建 `places/ge-yao.md` 会造成同实体双条并跨类型同名。
   - **增补**：2009xy 的章生一、章生二兄弟在两浙路处州、龙泉县各建一窑的传说（兄窑哥窑、弟窑亦称章窑或龙泉窑）、传世宫藏哥窑瓷实为南宋修内司官窑烧制的专家说、失透乳浊釉与灰青釉色、仿北宋官窑者黑胎；2009zn 的“在浙江龙泉、属龙泉窑系、胎质暗黑、利用胎釉收缩差成开片、南宋常为官窑产品”。
   - **不改的部分**：title、type、sub_type 与既有段落保持原样；`source_count` 2→4、`version` 1→2；窑址“未发现”（2009xy、2016、田自秉）与“浙江龙泉”（赵农）并列，不裁定。
   - **before 指纹**：编辑前直接对磁盘文件计算，`sha256:8b13f88c…`，3,696 B，85 行。
2. **no_delta：云岗石窟并入云冈石窟**。
   - **判据**：0254「云冈石窟」（赵农、李立新）与 0255「云岗石窟」（田自秉、2016）为同一处石窟的异写，按《梦梁录／梦粱录》先例合并。
   - **处理**：以 0254 赵农候选为 canonical 新建 `places/yungang-shiku.md`，`aliases` 收“云岗石窟”“大同云冈石窟”；0255 田自秉候选走 `approved -> no_delta`，另一成员 `rejected`。田自秉“六朝著名石窟、集体创造的艺术结晶”与 2016“北魏平城、早期造像模仿犍陀罗风格”已并入该条正文与来源。

## 四、并列保留的分歧

1. **建窑地点**：赵农作“福建建阳”，田自秉作“福建建瓯、水吉一带”。
2. **瓯窑时代**：赵农系于唐，田自秉系于六朝；赵农重“温润如玉、淡雅清脆”，田自秉重含铁量、胎色与“缥瓷”。
3. **宜兴时代**：田自秉以清代紫砂为主（另记明代紫砂已著名），2016 作“明清时期成为陶都”。
4. **马王堆衣物件数**：高丰作“50余件衣物”、46 幅；田自秉作“成件衣服 58 件”、匹端单幅丝织物 46 段。
5. **吉州窑时代**：赵农系于南宋；田自秉作宋代民窑，并记唐宋时为广州南海北上京都交通要道。
6. **云冈石窟规模**：仅赵农给“编号53个、佛像51000躯以上”，其余三册只列名，未互校。
7. **仙人洞地名**：2016 自注同章另处作“江西万县仙人洞”，本条从“江西万年”。
8. **妇好墓酒器**：2016 称“4件”，所列器名仅铜鸮尊、偶方彝、圈足觥三件，照录不改。

## 五、本批的方法判断

- **异写合并先于建条**：同一遗址的“云冈／云岗”只建一条，异写进 alias；避免因 OCR 或习惯写法产生双条。
- **既有 KU 同实体且类型更合时走 update**：哥窑的窑址未发现，作为 term 比作为 place 更准确，故 update 而非 create。
- **遗址/窑址一律入 B，都城入 D**：与既有 `places/` 16 条的分布一致（banpo、erlitou、yinxu、各窑址均 B；jingdezhen、yuan-dadu 为 D）。
- **只写来源可证的字段**：多数条目缺始建年、面积、堆积厚度等；`modern_name` 只填来源出现的地名，未据外部知识补“今某市”（雍城即作“陕西关中西部（汧山、雍水一带）”）。
- **来源行号优先取实际命中行**：对分期跨度大的候选（临淄、妇好墓、宜兴、马王堆、南京、满城）另行检索正文定位，不直接沿用 chunk 全域范围。

## 六、状态与验证

- `apply-plan.jsonl`：24 行（23 create + 1 update），哈希 24/24 与磁盘一致；update 行含 `before` 指纹。
- `candidate-decision-ledger.jsonl`：100 行（23×3 create + 1×3 update + 1×3 no_delta + 25 rejected）。
- 内容质量审计：480 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 480/480 可解析，同名跨类型 3 组、消歧说明 6/6。
- 候选索引：5,339 行，`sha256:…` 与字节数见 `manifest.json`。
- 规则漂移 0；sync closure 19 步全部通过，250 tests + 16 subtests。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 遗址类条目普遍缺地层、年代测定与出土器物清单；窑址类条目缺窑炉结构、装烧工艺与遗址范围。
- 两册图版均未视觉核验（耀州窑图7-48、图7-49 已在正文标注）。
- 「相关知识元」仍为纯文本，未建立 relation；Theme/Topic 均未 materialize。
- place doc2 已全关；后续转入 procedure（10 组）、event（9 组），再做 doc1 组 6 个与 ungrouped unit。
