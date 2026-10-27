# 2009 赵农《中国艺术设计史》— 第二章 unit 批次（batch-b）

- 工作包：`2026-10-26-2009zhaonong-units-batch-b`
- 来源（只读）：`03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md`
- doc_id：`2009-zhaonong-zhongguo-yishu-shejishi`
- 日期：2026-10-26
- 候选范围：`_zn_ch2.txt` 指定的 35 条 unit 候选
- 结果：create 30、update 3（3 个文件）、no_delta 2

## 一、裁定汇总

| 候选 | 实体 | 动作 | 目标 |
|---|---|---|---|
| cand-02-25 | 夏历 | create | `terms/xia-li.md` |
| cand-02-29 | 盘庚 | create | `persons/pan-geng.md` |
| cand-02-32 | 井田制 | create | `terms/jingtian-zhi.md` |
| cand-02-37 | 青铜钱铲 | create | `terms/qingtong-qian-chan.md` |
| cand-02-88 | 青铜镢 | create | `terms/qingtong-jue.md` |
| cand-02-89 | 青铜镰 | create | `terms/qingtong-lian.md` |
| cand-02-90 | 青铜锄 | create | `terms/qingtong-chu.md` |
| cand-02-91 | 青铜犁铧 | create | `terms/qingtong-lihua.md` |
| cand-02-39 | 邑 | create | `terms/yi-settlement.md` |
| cand-02-45 | 中轴线 | create | `terms/central-axis.md` |
| cand-02-46 | 陶瓦 | create | `terms/tao-wa.md` |
| cand-02-48 | 灵台 | create | `works/lingtai.md` |
| cand-02-49 | 戈 | create | `terms/ge-dagger-axe.md` |
| cand-02-50 | 戟 | create | `terms/ji-halberd.md` |
| cand-02-51 | 钺 | create | `terms/yue-battle-axe.md` |
| cand-02-52 | 双虎食人青铜钺 | no_delta | `places/fuhao-tomb.md` |
| cand-02-53 | 青铜剑 | create | `terms/jian-sword.md` |
| cand-02-92 | 殳（西周） | create | `terms/shu-staff.md` |
| cand-02-54 | 车轮 | create | `terms/chelun.md` |
| cand-02-57 | 妇好 | create | `persons/fu-hao.md` |
| cand-03-05 | 青铜箸 | create | `terms/qingtong-zhu.md` |
| cand-03-09 | 商周酒器类型 | update | `terms/qingtong-jiuqi.md` |
| cand-03-14 | 玉琮 | update | `terms/yu-yue-cong-bi.md` |
| cand-03-16 | 郑州杜岭方鼎 | no_delta | `terms/ding.md` |
| cand-03-22 | 八音 | create | `terms/ba-yin.md` |
| cand-03-152 | 秦公镈 | create | `works/qin-gong-bo.md` |
| cand-03-26 | 王懿荣 | create | `persons/wang-yirong.md` |
| cand-03-27 | 甲骨文编 | create | `publications/jiaguwen-bian.md` |
| cand-03-28 | 金文编 | create | `publications/jinwen-bian.md` |
| cand-03-29 | 史墙盘 | create | `works/shi-qiang-pan.md` |
| cand-03-36 | 六书 | create | `terms/liu-shu.md` |
| cand-03-42 | 商代玉器分类 | create | `terms/shangdai-yuqi-fenlei.md` |
| cand-03-44 | 瑞玉六器 | create | `terms/rui-yu-liuqi.md` |
| cand-03-46 | 刻纹白陶 | update | `terms/shangdai-baitao.md` |
| cand-03-51 | 布币 | create | `terms/bu-bi.md` |

## 二、新建 30 条

### 分类构成

- term：22 条（夏历、井田制、青铜钱铲、青铜镢、青铜镰、青铜锄、青铜犁铧、邑、中轴线、陶瓦、戈、戟、钺、青铜剑、殳、车轮、青铜箸、八音、六书、商代玉器分类、瑞玉六器、布币）
- person：3 条（盘庚、妇好、王懿荣）
- work：3 条（灵台、秦公镈、史墙盘）
- publication：2 条（甲骨文编、金文编）

### 置信度

- medium：19 条
- low：11 条（盘庚、青铜镢、青铜镰、青铜锄、青铜犁铧、妇好、秦公镈、王懿荣、甲骨文编、金文编、史墙盘）

low 的原因：秦公镈、史墙盘仅图注；青铜四器多为单句；盘庚、妇好、王懿荣的材料依附于事件或墓葬；两部字书只引字数。

## 三、更新 3 条

| 目标 | 版本 | source_count | 新增内容 |
|---|---|---|---|
| `terms/qingtong-jiuqi.md` | 1→2 | 2→3 | 赵农 L1538 的饮酒／盛酒／盛水洗手三分、宴饮等级、分类差异与“钫”未分期 |
| `terms/yu-yue-cong-bi.md` | 1→2 | 1→1 | 同源扩写 L1692-L1700：玉琮形制、六器名录、西周礼制与五器／六器差异 |
| `terms/shangdai-baitao.md` | 1→2 | 1→2 | 赵农 L1714 商代晚期刻纹白陶、L1708 制陶种类；补 alias“刻纹白陶” |

`yu-yue-cong-bi.md` 的 source_count 保持 1：只扩同一赵农来源的行号，未新增来源；`qingtong-jiuqi.md` 与 `shangdai-baitao.md` 各新增赵农一册，故分别 2→3、1→2。

## 四、no_delta 2 条

- **cand-02-52 双虎食人青铜钺** → `places/fuhao-tomb.md`。既有条已记“所出双虎食人青铜钺重达9公斤，是已出土青铜钺中最重者”；候选的兵器与政权象征解释本批已写入 `terms/yue-battle-axe.md`。
- **cand-03-16 郑州杜岭方鼎** → `terms/ding.md`。既有条已引赵农 L1570 原句“如商早期的郑州杜岭方鼎，曾是商王的祭祀重器”，并补田自秉的两件杜岭方鼎形制。

两条目标与候选的 unit 类型不完全相同（work → place／term），但候选事实已被覆盖；另建单件短条只会重复。

## 五、原文错字与内部不一致

均照录并标疑，未径改：

- 钺 L1339：“钱是从石斧中发展起来”——“钱”当为“钺”。
- 殳 L1347：“反也是一种如杖状的兵器。”——句首“反”当为“殳”。
- 戈 L1319：“秘柄”“镈”，通行多作「柲柄」「鐏」。
- 戟 L1337：“河北蒿城”，通行多作「藁城」；同段末句“青铜戈作为仪仗”与前文“青铜戟”不一致，两存。
- 车轮 L1403：“轴的两端为轨”，通行多作「軎」。
- 八音 L1595：“属‘大乐司’”，通行《周礼》官名作「大司乐」。
- 青铜箸：L1534 作“用桿”“不用桿”，L2194 作“用桜”“不用桜”，第三章标题作“箸桜”；通行《礼记》多作「梜」。
- 王懿荣 L1621：“刘鄂”，通行多作「刘鹗」。
- 布币 L2270：“人们将镈形，铸成了象形的镈形”——“镈形”重复。
- 金文编 L1644：“15 000”“3 772”数字内含空格，照录其数值，不保留排版。

同书内部不一致：戈与钺的起源叙述方向不同（L1321 戈“发展为钺”，L1339 钺“从石斧发展”）；L1684 礼器只列五器、L1692 六器含玉琥；L1283 作“瓦钉和瓦环”、L1720 作“瓦钉或瓦环”；L1538“彝”同时列入盛酒与盛水洗手，“钫”未分期；玉琮句被“## 4. 陶器”标题隔断。以上均在对应条目标出。

## 六、图注与证据边界

- 秦公镈、史墙盘只有图注或一句正文，confidence 记 low，未据图补写器形、纹饰、铭文与收藏。
- 灵台有图 2-24，但图注未指向灵台；未核图。
- 玉琮既有条所引图 1-38、1-39、1-42 未视觉核验。
- 布币相邻图 3-43 为刀币，不是布币，不能据图补器形。
- 妇好、王懿荣、甲骨文编、金文编、青铜箸无对应图版，按纯文本处理。

## 七、引文审计与独立复核

- 33 个目标文件全库引文审计：修复后 0 MISS、0 NESTED、0 UNBALANCED。
  - 首轮 4 处 MISS：`ge-dagger-axe.md` 3 处、`qingtong-zhu.md` 1 处；系把通行字形与压缩表述误作逐字引文，已改用「」。
- 30 个新建文件“仅赵农语料”严格审计：修复后 0 MISS。
  - 首轮 5 处：`tao-wa.md` 2 处（“和／或”）、`ji-halberd.md` 1 处（“藁城”）、`ba-yin.md` 2 处（“大司乐”）；均为通行字形注，已改用「」。
- 结构校验：六节齐全、必填字段齐全、`## 相关知识元` 路径均存在、正文无 ASCII 双引号；仅 `qingtong-jiuqi.md` 的 created=2026-10-25 属既有文件，正常。
- 独立复核中另修正：
  - `rui-yu-liuqi.md` 删除 alias“六瑞”（六瑞与六器为《周礼》两套不同概念）。
  - `shangdai-baitao.md` 补 alias“刻纹白陶”，使候选可检索。
  - `shu-staff.md` 时限由“西周”改为“商周”，与牧野之战材料一致。
  - `bu-bi.md` 删除与布币无直接关系的 `places/yanshi-shangcheng.md` 链接。
  - `lingtai.md`、`qin-gong-bo.md` 的裸目录 `works/` 代码改为正文说明。
  - `qingtong-qian-chan.md` 一句语法修正。
- 两条 no_delta 目标已逐条核对原句与覆盖范围。

## 八、跨度说明

候选声明跨度并为 `L1053-L1307`、`L1310-L2279`，共覆盖 1,225 行；这是候选声明跨度的并集，不表示逐行产生候选。实际语义复读取各实体所在小节的有效段落，跨度内的其他候选材料未混入本条。

## 九、状态与下一跳

- 写入前候选索引：needs_evidence 2,776、applied 1,590、no_delta 160、rejected 813（5,339 行）。
- 本包重放后：needs_evidence 2,741、applied 1,623、no_delta 162、rejected 813（5,339 行）。
- 未 commit、未 push；未新建分支或 worktree；HEAD 仍为 `71b660a`。
- 下一跳：第二章已完成，继续第三章 60 条 unit 候选。
