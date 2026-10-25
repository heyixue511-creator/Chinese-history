# event doc_count=2 批次（xdup-0167—xdup-0175）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-event-doc2-batch/`
状态：`applied`

## 一、本批做了什么

- 覆盖 event 类型 doc_count=2 的全部 9 个重复组，共 18 个候选。
- 9 组 `create`，新建 9 个 event KU。
- 9 个 canonical `applied`，9 个同组重复成员 `rejected`。
- 候选索引投影后：applied 494、no_delta 15、rejected 795、needs_evidence 4035；active 4035、terminal 1304。
- event doc2 累计关闭 9/9，**event 类型 doc_count=2 全部收口**；全部类型 doc_count≥2 的重复组至此清空，仅剩 6 个 doc_count=1 组（person 2、term 3、work 1）。

## 二、新建的 9 个 event KU

| 组 | 条目 | sub_type | 维度 | canonical 册次 |
|---|---|---|---|---|
| xdup-0167 | 上海市首次手工业技艺人员授衔大会 | professional_event | D | 夏燕靖 2009 |
| xdup-0168 | 1959年全国工艺美术展览会 | exhibition | D | 夏燕靖 2009 |
| xdup-0169 | 全国民间美术工艺品展览会 | exhibition | D | 夏燕靖 2016 |
| xdup-0170 | 南洋劝业会 | exhibition | D | 夏燕靖 2009 |
| xdup-0171 | 安史之乱 | historical_event | E | 夏燕靖 2016 |
| xdup-0172 | 巴拿马赛会 | exhibition | E | 夏燕靖 2009 |
| xdup-0173 | 洋务运动 | historical_event | E | 夏燕靖 2016 |
| xdup-0174 | 盘庚迁殷 | historical_event | E | 夏燕靖 2016 |
| xdup-0175 | 辛亥革命 | historical_event | E | 夏燕靖 2016 |

维度分布：D 4、E 5。类型分布：exhibition 4、historical_event 4、professional_event 1。

## 三、本批的判断

1. **事件按“名称＋时间＋地点＋参与者＋原因＋结果”六项建 frontmatter**，沿用既有 `events/opium-war.md` 的字段结构；来源未记的项填“未记”，不据外部知识补。
2. **展览类归 D、政治与分期事件归 E**：南洋劝业会、巴拿马赛会虽涉对外交流，但其设计史功能是产品评奖与实业制度，归 D；巴拿马赛会因跨文化展示性质较强，归 E。革命、战乱、迁都、自强运动归 E。
3. **同一事件只建一条**：`places/nanjing.md` 中的南洋劝业会会场、`places/yinxu.md` 中的殷都只作地点信息，不另建 event。
4. **同名展览加年份入题**：“1959年全国工艺美术展览会”以年份与 1953—1954 年民间美术工艺品展览会区分。

## 四、并列保留的分歧

1. **全国民间美术工艺品展览会**：巡展国别 2009 作苏联、捷克斯洛伐克、匈牙利、保加利亚四国；2016 作五国（加缅甸）、6—11 月，并称促成艺人座谈；日期 2009 只给月份、2016 给 12 月 7 日与 1 月 3 日。
2. **盘庚迁殷年代**：田自秉作公元前15世纪末；2016 作约前1250—前1050。2016 同段又作“计73年”，与253年、八代十二王相矛盾，未改字。
3. **洋务运动评价**：2016 重“开启近代工业、设计孕育土壤”的正面定位；赵农重“旧学为体、西学为用”“强国实为强政府、少关注民生”的批判。
4. **巴拿马赛会中国展品**：约1500吨仅 2009 所记，2016 未记；两册均未记举办城市与获奖。
5. **安史之乱**：两册均无具体年份、地点、人物与战事过程，只作分期背景。
6. **辛亥革命年份**：2016 作1911年，赵农只系于清末未给年份。

## 五、本批的方法判断

- **事件类条目以“来源怎么说”为准，不做史实补全**：六项 frontmatter 中“未记”即留白，避免把通史知识写成来源证据。
- **canonical 取信息量大者**：2016 在展览日期、迁殷年数、洋务举措上更全，取 6 组；2009 在获奖省份、展品吨位、人物数字上更全，取 3 组。
- **两册立场相反时并列**：洋务运动的正面定位与批判性判断分列，不合成“辩证评价”。

## 六、状态与验证

- `apply-plan.jsonl`：9 行 create，哈希 9/9 与磁盘一致。
- `candidate-decision-ledger.jsonl`：36 行（9×3 canonical + 9 rejected）。
- 内容质量审计：498 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 498/498 可解析，同名跨类型 3 组、消歧说明 6/6。
- 候选索引：5,339 行，`sha256:…` 与字节数见 `manifest.json`。
- 规则漂移 0；sync closure 19 步全部通过，250 tests + 16 subtests。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 事件类条目普遍缺起止年、地点与过程；多数只有一两句背景性叙述。
- 两册图版均未视觉核验。
- 「相关知识元」仍为纯文本，未建立 relation；Theme/Topic 均未 materialize。
- 下一批：doc_count=1 的 6 个组（person 2、term 3、work 1），完成后转入 ungrouped unit 与 claim。
