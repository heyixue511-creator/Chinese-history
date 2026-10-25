# institution doc_count=2 批次（xdup-0176—xdup-0201）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-institution-doc2-batch-a/`
状态：`applied`

## 一、本批做了什么

- 覆盖 institution 类型 doc_count=2 的全部 26 个重复组，共 52 个候选。
- 25 组 `create`，新建 25 个 institution KU。
- 1 组 `update`：xdup-0190「少府」并入既有 `institutions/shaofujian.md`（少府监），version 1→2。
- 26 个 canonical `applied`，26 个同组重复成员 `rejected`。
- 候选索引投影后：applied 451、no_delta 14、rejected 751、needs_evidence 4123；active 4123、terminal 1216。
- institution doc2 累计关闭 26/26，**institution 类型 doc_count=2 全部收口**。

## 二、新建的 25 个 institution KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0176 | 三服官 | government_office | D | 赵农 2009、田自秉 2010 |
| xdup-0177 | 上海美术电影制片厂 | film_studio | C | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0178 | 两江师范学堂 | design_school | D | 赵农 2009、李立新 2011 |
| xdup-0179 | 中国工艺美术学会 | professional_society | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0180 | 中国工艺美术馆 | museum | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0181 | 中国美术馆 | museum | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0182 | 中天电机厂 | commercial_enterprise | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0183 | 中央工艺美术科学研究所 | research_institute | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0184 | 中央美术学院 | design_school | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0185 | 云锦研究工作组 | research_institute | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0186 | 亚平艺术装饰公司 | design_firm | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0187 | 内务府造办处 | government_office | D | 高丰 2004、夏燕靖 2016 |
| xdup-0188 | 南京市云锦研究所 | research_institute | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0189 | 商务印书馆 | publishing_house | C | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0191 | 尚美图案馆 | design_firm | D | 李立新 2011、夏燕靖 2016 |
| xdup-0192 | 故宫博物院 | museum | D | 田自秉 2010、李立新 2011 |
| xdup-0193 | 文思院 | government_office | D | 田自秉 2010、夏燕靖 2016 |
| xdup-0194 | 江南制造总局 | government_office | D | 夏燕靖 2009、赵农 2009 |
| xdup-0195 | 汲古阁 | publishing_house | C | 李立新 2011、夏燕靖 2016 |
| xdup-0196 | 申新纺织公司 | commercial_enterprise | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0197 | 第二轻工业部 | government_office | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0198 | 船宫 | craft_workshop | B | 赵农 2009、夏燕靖 2016 |
| xdup-0199 | 轮船招商局 | commercial_enterprise | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0200 | 金银作坊院 | government_office | D | 夏燕靖 2009、田自秉 2010 |
| xdup-0201 | 铸镜局 | government_office | D | 田自秉 2010、夏燕靖 2016 |

维度分布：B 3、C 3、D 19。

## 三、update：少府并入少府监

1. **判据**：`institutions/shaofujian.md` 已存在并覆盖唐代少府监的五署、工匠规模与宋代沿革；xdup-0190 两个候选分别记唐代少府（赵农）与汉代少府属官（李立新），属同一机构谱系，另建 `shaofu.md` 会造成同实体双条。
2. **处理**：以赵农 cand-07-123 为 canonical 执行 `update`，增补：李立新所记汉代属官（尚方、考工室、若庐、东织西织、东园匠）；赵农所记唐代别名尚方监、从三品、《新唐书·百官志》“掌百工技巧之政”与诸冶、铸钱、互市等监；工匠 19850 人；分工细致导致设计华丽富贵的评述。
3. **不改的部分**：title 保持“少府监（Court of the Imperial Workshops）”，新增 `aliases`「少府」「尚方监」；工匠数由两说扩为三说并列；`source_count` 5→7，`version` 1→2。
4. **before 指纹**：对最终文件执行逆向替换并正向回放校验一致后计算，`sha256:0b9d2345…`，6,951 B，116 行。

## 四、并列保留的分歧

1. **三服官设置地**：赵农作“襄邑、临淄一带”，田自秉作“齐郡临淄、陈留郡襄邑”。
2. **两江师范学堂**：赵农记 1905 年开设与设计有关的课程；李立新记 1902 年设三江师范学堂、1905 年更名、1906 年设图画手工科并称“首次在中国设立美术与设计学科”。
3. **云锦机构“最早／第一家”**：1954 年工作组称“新中国建立初期最早的工艺美术研究机构”，1957 年研究所称“新中国第一家工艺美术研究机构”，两册均未调和。
4. **文思院**：宋代隶属同段两作（工部所属／少府监所属），作数两作（42 作／40 多种作）。
5. **内务府造办处成立时间**：高丰只作“清代”，2016 作“康熙年间成立至 1924 年、先后设 60 多个专业作坊”。
6. **铸镜局时代**：田自秉作“南宋湖州、饶州”，2016 作“宋代”。
7. **船宫地域**：赵农作“吴越”，2016 作“南方楚、吴、越”。
8. **尚美图案馆业务**：李立新作“工业产品的图案设计”，2016 作“主要从事染织纹样设计”。

## 五、本批的方法判断

- **同名跨朝代机构合条不分拆**：文思院唐宋两代同名而职掌不同，合为一条按朝代分述；少府（汉）、少府监（唐）、宋沿设同理分层。判断依据是“是否为同一机构谱系”，而非“名称是否完全一致”。
- **既有 KU 覆盖时走 update 而非 create**：少府组是唯一用例。update 只增补缺口，不改 title、不重写既有段落，来源逐条追加。
- **机构维度按“其主要设计史功能”分配**：官营手工业与行政机构、博物馆、院校、企业多入 D；以工艺研究与品种恢复为主要内容的云锦机构、造船工场入 B；出版与动画机构入 C。
- **只写来源可证的机构信息**：多数条目未记创办人之外的资本、编制、沿革；2016 的超大跨度位置（如内务府造办处 L4341-L6330、江南制造总局 L7513-L8560）在正文标注“具体位置待核”。

## 六、状态与验证

- `apply-plan.jsonl`：26 行（25 create + 1 update），哈希 26/26 与磁盘一致；update 行含 `before` 指纹。
- `candidate-decision-ledger.jsonl`：104 行（26×3 applied + 26 rejected）。
- 内容质量审计：457 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 457/457 可解析，同名跨类型 3 组、消歧说明 6/6。
- 候选索引：`sha256:…` 与字节数见 `manifest.json`，5,339 行。
- 规则漂移 0；sync closure 19 步全部通过，250 tests + 16 subtests。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 机构类条目普遍只有一两句来源，缺创办年、隶属、编制、存续与遗址信息；未做来源外机构史核对。
- 两册图版均未视觉核验。
- 「相关知识元」仍为纯文本，未建立 relation；Theme/Topic 均未 materialize。
- institution doc2 已全关；后续转入 place（25 组）、procedure（10 组）、event（9 组）。
