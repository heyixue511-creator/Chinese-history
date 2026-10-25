# publication doc_count=2 第二批（xdup-0310—xdup-0332）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-publication-doc2-batch-b/`
状态：`applied`

## 一、本批做了什么

- 覆盖 publication 类型 doc_count=2 的后 23 个重复组，共 46 个候选。
- 23 组全部 `create`，新建 23 个 publication KU。
- 23 个 canonical `applied`，23 个同组重复成员 `rejected`。
- 候选索引投影后：applied 425、no_delta 14、rejected 725、needs_evidence 4175；active 4175、terminal 1164。
- publication doc2 累计关闭 46/46，**publication 类型 doc_count=2 全部收口**。

## 二、新建的 23 个 publication KU

| 组 | 条目 | sub_type | 维度 | 来源册次 |
|---|---|---|---|---|
| xdup-0310 | 盛世危言 | reform_treatise | D | 赵农 2009、李立新 2011 |
| xdup-0311 | 礼记 | classical_text | D | 田自秉 2010、夏燕靖 2016 |
| xdup-0312 | 禹贡 | geographical_text | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0313 | 竹书纪年 | history | A | 赵农 2009、夏燕靖 2016 |
| xdup-0314 | 管子 | classical_text | A | 赵农 2009、夏燕靖 2016 |
| xdup-0315 | 经世大典 | official_compendium | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0316 | 绣谱 | craft_treatise | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0317 | 考工记图 | illustrated_treatise | B | 赵农 2009、李立新 2011 |
| xdup-0318 | 良友 | pictorial | C | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0319 | 芥子园画传 | print_album | C | 高丰 2004、赵农 2009 |
| xdup-0320 | 荀子 | classical_text | A | 赵农 2009、夏燕靖 2016 |
| xdup-0321 | 萝轩变古笺谱 | print_album | C | 李立新 2011、夏燕靖 2016 |
| xdup-0322 | 蚕桑萃编 | agronomic_treatise | B | 高丰 2004、田自秉 2010 |
| xdup-0323 | 装潢志 | craft_treatise | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0324 | 装饰杂志 | periodical | D | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0325 | 论语 | classical_text | A | 赵农 2009、夏燕靖 2016 |
| xdup-0326 | 道德经 | classical_text | A | 赵农 2009、夏燕靖 2016 |
| xdup-0327 | 遵生八笺 | life_treatise | B | 田自秉 2010、夏燕靖 2016 |
| xdup-0328 | 闲情偶寄 | life_treatise | B | 高丰 2004、赵农 2009 |
| xdup-0329 | 韩非子 | classical_text | A | 赵农 2009、夏燕靖 2016 |
| xdup-0330 | 饮流斋说瓷 | ceramics_treatise | B | 夏燕靖 2009、夏燕靖 2016 |
| xdup-0331 | 鲁班经 | craft_manual | B | 赵农 2009、夏燕靖 2016 |
| xdup-0332 | 齐民要术 | agronomic_treatise | B | 赵农 2009、夏燕靖 2016 |

维度分布：A 6、B 11、C 3、D 3。

## 三、同名异书与跨类型同名

1. **《中国设计史》同类外**：本批无同名异书。
2. **跨类型同名 2 组**：新建《荀子》典籍条与 `persons/xunzi.md`、新建《韩非子》典籍条与 `persons/han-fei-zi.md` 同名。《荀子》两条同 basename，按 `mengzi`／`zhuangzi` 惯例为四条补 `disambiguation` 字段，均以“类型消歧：”开头；两个 person 条 version 1→2。
3. **过期表述修正**：`persons/han-fei-zi.md`「相关知识元」原记“《韩非子》应有独立的 publications/ 条目……publications/ 下现无该书条目，属研究债务”，本批建条后改为“已由 `publications/hanfeizi.md` 承接”，记入 manifest 的 `auxiliary_edits`。

## 四、并列保留的分歧

1. **《礼记》礼运篇引文 OCR 异文**：2016 作“未有宫窑，冬则居管窑，夏则居槽巢”，三处疑均为 OCR 讹字；KU 照录并标注，不擅改。
2. **《竹书纪年》盘庚至纣年数**：赵农作“二百七十三年”，2016 作“二百五十三年”；两说并列。
3. **《绣谱》章名**：田自秉作“程工”，2016 作“工程”；并列，以“程工”为正条并注异写。
4. **《考工记图》引文**：李立新作“高庫广狭有度”，疑“高庳”之讹；照录标注。
5. **《萝轩变古笺谱》版名**：李立新作“恒版拱花”，2016 作“饾版、拱花”；并列。
6. **《鲁班经》**：2016 作“年荣汇编”（疑“午荣”）、“雕新正式”（疑 OCR）；照录标注。
7. **《闲情偶寄》书名**：赵农同书另处作《闲情偶记》；以“闲情偶寄”为正条，别名保留异写。
8. **《荀子》篇名**：2016 作《玉制》，疑《王制》之讹；照录标注。
9. **《荀子》成书**：赵农只作“战国末年著作”，2016 据《史记·孟子荀卿列传》作“晚年总结百家争鸣而编”；并列。

## 五、本批的方法判断

- **文献入维度按“其内容主要服务的设计史问题”分配**：史学与造物思想类（《竹书纪年》《管子》《荀子》《论语》《道德经》《韩非子》）入 A；工艺、器物、技术类（《禹贡》《经世大典》《绣谱》《考工记图》《蚕桑萃编》《装潢志》《遵生八笺》《闲情偶寄》《饮流斋说瓷》《鲁班经》《齐民要术》）入 B；印刷与视觉传播类（《良友》《芥子园画传》《萝轩变古笺谱》）入 C；制度、服色等级与设计期刊类（《盛世危言》《礼记》《装饰杂志》）入 D。
- **注本不并入原典**：《考工记图》为戴震对《考工记》的注图之作，单独建条，不并入既有 `publications/kaogongji.md`；《管子》《荀子》《韩非子》等诸子条同理，与对应 person 条按 type 分流。
- **只写来源可证的文献信息**：多数条目只有一两句引用，未补卷次、版本、藏地；2016 的超大跨度位置（如《荀子》L1581-L6154、《韩非子》L529-L6158）在正文标注“具体位置待核”。

## 六、状态与验证

- `apply-plan.jsonl`：23 行 create，哈希 23/23 与磁盘一致。
- `candidate-decision-ledger.jsonl`：92 行（23×3 applied + 23 rejected）。
- 内容质量审计：432 个 KU，0 findings。
- 仓库审计：0 问题，证据引用 432/432 可解析，同名跨类型 3 组、消歧说明 6/6。
- 候选索引：`sha256:…` 与字节数见 `manifest.json`，5,339 行。
- 规则漂移 0；sync closure 19 步全部通过，250 tests + 16 subtests。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定。
- 赵农《道德经》L2424-L8560、《管子》L1966-L2423、《荀子》L2409-L2423、《韩非子》L2309-L2423 为多段拼接的超大跨度；2016《荀子》L1581-L6154、《韩非子》L529-L6158、《饮流斋说瓷》L3665-L6342、《绣谱》L4679-L6322、《装饰》L5657-L6042 同为超大跨度，正文已标注“具体位置待核”。
- 两册图版均未视觉核验；《良友》明星广告、《芥子园画传》卷目等只按正文转述。
- 出版年、版次、ISBN 多数缺失；未做来源外书目核对。
- 「相关知识元」仍为纯文本，未建立 relation；Theme/Topic 均未 materialize。
- publication doc2 已全关；后续转入 institution 26 组。
