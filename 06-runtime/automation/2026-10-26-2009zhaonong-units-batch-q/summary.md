# 2026-10-26-2009zhaonong-units-batch-q 收口

## 一、范围与目标

- 来源：赵农《中国艺术设计史》（高等教育出版社，2009）Markdown 文本。
- 范围：第十章第六节「货币与交通」L8246–L8356、第七节「艺术设计教育」L8357–L8443。
- 目标：把两节 21 条 unit 候选逐条裁定为新建、更新或 no_delta，并完成写回、索引重建与同步闭合。
- 本批不处理第八节结论、思考练习题与附录；不启动 Book 7 及以后；未做 commit / push。

## 二、覆盖与复读

| 小节 | 行范围 | 候选 | 新建 | no_delta | 说明 |
|---|---:|---:|---:|---:|---|
| 1. 钱币 | L8248–L8266 | 4 | 4 | 0 | 大清银币、袁大头、人民币、墨西哥鹰洋 |
| 2. 生活票证 | L8267–L8274 | 2 | 2 | 0 | 生活票证总类与粮票子类分列 |
| 3. 其他器具 | L8275–L8291 | 1 | 1 | 0 | 神舟五号载人飞船，正文泛称、图注点名 |
| 4. 交通工具 | L8292–L8356 | 5 | 4 | 1 | 人力车、慈禧太后专用车、上海磁悬浮列车、自行车；龙号机车 no_delta |
| 5. 设计教育发展 | L8359–L8409 | 1 | 1 | 0 | 蔡元培与《美术的起源》的学科分类 |
| 6. 艺术设计研究 | L8410–L8443 | 8 | 8 | 0 | 八种设计史论著述 |
| 合计 | L8246–L8443 | 21 | 20 | 1 | 无 update、无 rejected |

复读方式：逐段阅读正文、小标题与图注；候选 `source_span` 为块级粗跨度，实际引用行逐条回查。图 10-48 至图 10-64 未做视觉核验，涉及图版的条目只据图注与正文著录。

## 三、21 条裁定总表

| # | 候选 | 实体 | 裁定 | 目标 | 证据 |
|---:|---|---|---|---|---|
| 1 | cand-12-66 | 大清银币 | create | works/daqing-yinbi.md | L8250 |
| 2 | cand-12-67 | 袁大头 | create | works/yuandatou.md | L8254, L8256, L8261 |
| 3 | cand-12-69 | 人民币 | create | terms/renminbi.md | L8259, L8265 |
| 4 | cand-12-166 | 墨西哥鹰洋 | create | works/moxige-yingyang.md | L8250 |
| 5 | cand-12-72 | 生活票证 | create | terms/shenghuo-piaozheng.md | L8269, L8271, L8273 |
| 6 | cand-12-73 | 粮票 | create | terms/liangpiao.md | L8269 |
| 7 | cand-12-78 | 神舟五号载人飞船 | create | works/shenzhou-wuhao.md | L8290, L8303 |
| 8 | cand-12-79 | 人力车 | create | terms/renliche.md | L8307 |
| 9 | cand-12-80 | “龙”号机车 | no_delta | works/longhao-jiche.md | L8332 |
| 10 | cand-12-81 | 慈禧太后专用车 | create | works/cixi-zhuanyongche.md | L8334 |
| 11 | cand-12-82 | 上海磁悬浮列车 | create | works/shanghai-cifu.md | L8315, L8324, L8332 |
| 12 | cand-12-161 | 自行车 | create | terms/zixingche.md | L8309 |
| 13 | cand-12-90 | 蔡元培 | create | persons/cai-yuanpei.md | L8367 |
| 14 | cand-12-106 | 《世界现代设计史》 | create | publications/shijie-xiandai-shejishi.md | L8440 |
| 15 | cand-12-107 | 《世界现代平面设计史》 | create | publications/shijie-xiandai-pingmian-shejishi.md | L8440 |
| 16 | cand-12-108 | 《工业设计学概论》 | create | publications/gongye-shejixue-gailun.md | L8440 |
| 17 | cand-12-109 | 《白马设计学丛书》 | create | publications/baima-shejixue-congshu.md | L8440 |
| 18 | cand-12-110 | 《艺术设计学》 | create | publications/yishu-shejixue.md | L8440 |
| 19 | cand-12-111 | 《现代设计大系》 | create | publications/xiandai-sheji-daxi.md | L8440 |
| 20 | cand-12-112 | 《高等院校设计艺术专业系列教材》 | create | publications/gaodeng-yuanxiao-sheji-jiaocai.md | L8440 |
| 21 | cand-12-113 | 《设计概论》 | create | publications/sheji-gailun.md | L8440 |

## 四、20 条新建分型

- 作品 6：大清银币、袁大头、墨西哥鹰洋、神舟五号载人飞船、慈禧太后专用车、上海磁悬浮列车。
- 术语 5：人民币、生活票证、粮票、人力车、自行车。
- 人物 1：蔡元培。
- 出版物 8：《世界现代设计史》《世界现代平面设计史》《工业设计学概论》《白马设计学丛书》《艺术设计学》《现代设计大系》《高等院校设计艺术专业系列教材》《设计概论》。

维度分布：primary B 9 条、primary D 4 条、primary A 7 条；secondary D 13 条、secondary C 2 条、secondary E 3 条、secondary A 2 条。confidence：medium 7 条、low 13 条。

## 五、1 条 no_delta

「龙」号机车与既有 `works/longhao-jiche.md` 同指。既有条目已据赵农 L7583 记唐胥铁路与中国人自造机车；本批 L8332 只以「从 1881 年 ‘龙’ 号机车，到磁悬浮列车」作交通史对举，未提供新型式、功率、制造厂或制造年份，故保持原状，不重复写回。

## 六、合并与分层边界

- 生活票证与粮票：总类与子类分列，粮票不并入生活票证。
- 自行车与永久、飞鸽：自行车为车类术语，`works/yongjiu-zixingche.md`、`works/flying-pigeon-bicycle.md` 为具体品牌作品，三者不合并。
- 人民币与古代纸币：`terms/qing-baochao.md`、`terms/daming-tongxing-baochao.md` 等为古代纸币，与人民币分列。
- 大清银币与大清宝钞：一为银币、一为纸币，不因「大清」同名合并。
- 神舟五号与载人航天工程：来源正文未点名，只有图注；本条按候选与通行名立目，未另立工程条目。
- 设计研究八种著述各自独立：丛书、教材系列与单本著作不合并；《设计概论》与赵农《中国艺术设计史》为同一作者不同著作，不合并。

## 七、语义复读修正

1. **非来源名称不加引号**：神舟五号条目初稿把通行名「神舟五号」放进引号，回查赵农原文只有「神州五号」，已改为不加引号的说明文字，只对图注原文用引号。
2. **图注用字差异**：图 10-52 图注作「神州五号载人飞船发射」，通行名为神舟五号；条目照录图注原字并标明差异，不径改来源。
3. **正文与图注分层**：神舟五号在正文只对应「载人太空飞船的发射回收成功」的泛称，未点名；条目明确区分正文泛称与图注点名，confidence 取 low。
4. **作者自述影响**：《设计概论》一条的「广泛的社会影响」出自赵农本人著述的自述，条目照录并标注，不当作独立评价。
5. **图版均未视觉核验**：人民币图 10-48、神舟五号图 10-52、上海磁悬浮图 10-56 等只据图注著录，未据图扩写。

## 八、验证与门禁

- `_zn_struct.py _zn_ch10q_files.txt`：problems 0（20 文件）。
- `_zn_audit.py _zn_ch10q_files.txt`：findings 0。
- `_zn_audit_strict.py _zn_ch10q_files.txt`：findings 0。
- `_zn_checklines_ch10q.py`：20 条、53 处引文，problems 0。
- 工作包 `2026-10-26-2009zhaonong-units-batch-q`：ledger 63 行，apply-plan 20 行，create 20、no_delta 1。
- 候选索引写回 21 条：20 条 `needs_evidence → applied`，1 条 `needs_evidence → no_delta`，均 `lifecycle_class: terminal`。
- 索引与闭合：`build_discovery_index.py` 5339 条，`build_translation_index.py` 1698 条；`run_sync_closure.py --refresh-generated --full` 通过，250 tests + 16 subtests。
- 状态：applied 2329、rejected 852、no_delta 193、needs_evidence 1965、terminal 3374；total_units 2090；health 102/130。
- 内容审计 12 项，均为既有问题（8 项空 frontmatter、1 项跨类型同名、3 项占位内容），无一项落在本批文件。

## 九、状态与下一跳

- 本批状态：closed（20 新建 + 1 no_delta 已写回，索引与生成态已刷新）。
- 第十章剩余：思考练习题段 9 条 unit 候选（林则徐、水晶宫、魏源、冯桂芬、《校邠庐抗议》、陈独秀、胡适、康有为、中国风），作为 batch R 处理。
- 之后转 2010 田自秉（404 条）与 2011 李立新（189 条 unit、1363 条 claim）。
- 未 commit、未 push；`03基础书籍-md文档/` 未改写；未创建分支或 worktree；Book 7 及以后未启动。
