# 2026-10-26-2009zhaonong-units-batch-p 收口

## 一、范围与目标

- 来源：赵农《中国艺术设计史》（高等教育出版社，2009）Markdown 文本。
- 范围：第十章第五节「书籍与包装」L8103–L8245，含书籍装帧、纸张、印刷、广告招贴、包装、标志六小节。
- 目标：把本节 32 条 unit 候选逐条裁定为新建、更新或 no_delta，并完成类型化写回、索引重建与同步闭合。
- 本批不处理第六节货币与交通及以后内容；不启动 Book 7 及以后；未做 commit / push。

## 二、覆盖与复读

| 小节 | 行范围 | 候选 | 新建 | 更新 | 说明 |
|---|---:|---:|---:|---:|---|
| 1. 书籍装帧 | L8105–L8136 | 16 | 14 | 2 | 民国至改革开放后书籍封面、字体与出版机构；《良友画报》《装饰》为跨书更新 |
| 2. 纸张 | L8137–L8150 | 0 | 0 | 0 | 来源述纸史与机制纸，无独立可立目实体 |
| 3. 印刷 | L8151–L8165 | 0 | 0 | 0 | 来源述铅印、石印、胶印等技术史，已有印刷类 procedure 条目，不重复立目 |
| 4. 广告招贴 | L8166–L8209 | 5 | 5 | 0 | 阴丹士林色布广告与月份牌作者；《国际广告》《中国广告》 |
| 5. 包装 | L8210–L8221 | 3 | 3 | 0 | 邮票合并为一条；《中国包装》《包装年鉴》 |
| 6. 标志 | L8222–L8245 | 8 | 8 | 0 | 六件标志/品牌作品与交通标志、商品标志两术语 |
| 合计 | L8103–L8245 | 32 | 30 | 2 | 无 no_delta、无 rejected |

复读方式：逐段阅读正文、小标题、图注与图版位置；候选 `source_span` 为块级粗跨度，实际引用行逐条回查。图 10-37 至图 10-46 未做视觉核验，涉及图版的条目只据图注与正文著录。

## 三、32 条裁定总表

| # | 候选 | 实体 | 裁定 | 目标 | 证据 |
|---:|---|---|---|---|---|
| 1 | cand-12-05 | 《呐喊》 | create | publications/nahan.md | L8114 |
| 2 | cand-12-07 | 《彷徨》 | create | publications/panghuang.md | L8114 |
| 3 | cand-12-08 | 《坟》 | create | publications/fen.md | L8114 |
| 4 | cand-12-09 | 钱君陶 | create | persons/qian-juntao.md | L8114 |
| 5 | cand-12-13 | 《冯小青》 | create | publications/feng-xiaoqing.md | L8125 |
| 6 | cand-12-15 | 《万象》 | create | publications/wanxiang.md | L8125 |
| 7 | cand-12-16 | 《良友画报》 | update | publications/liangyou.md | L8125 |
| 8 | cand-12-17 | 《装饰》 | update | publications/zhuangshi-zazhi.md | L8127, L8131 |
| 9 | cand-12-18 | 《中国历代货币大系》 | create | publications/zhongguo-lidai-huobi-daxi.md | L8127 |
| 10 | cand-12-19 | 《毛泽东选集》 | create | publications/maozedong-xuanji.md | L8127 |
| 11 | cand-12-20 | 《中国历代绘画》 | create | publications/zhongguo-lidai-huihua.md | L8131 |
| 12 | cand-12-21 | 《陈寅恪文集》 | create | publications/chen-yinke-wenji.md | L8131 |
| 13 | cand-12-22 | 《老房子》 | create | publications/lao-fangzi.md | L8131 |
| 14 | cand-12-23 | 《老照片》 | create | publications/lao-zhaopian.md | L8131 |
| 15 | cand-12-24 | 《汉声》 | create | publications/hansheng.md | L8131 |
| 16 | cand-12-162 | 《读书》 | create | publications/dushu.md | L8131 |
| 17 | cand-12-40 | 阴丹士林色布 | create | terms/yindanshilin-sebu.md | L8172–L8175 |
| 18 | cand-12-44 | 金梅生 | create | persons/jin-meisheng.md | L8188 |
| 19 | cand-12-45 | 李慕白 | create | persons/li-mubai.md | L8188 |
| 20 | cand-12-46 | 《国际广告》 | create | publications/guoji-guanggao.md | L8194 |
| 21 | cand-12-47 | 《中国广告》 | create | publications/zhongguo-guanggao.md | L8194 |
| 22 | cand-12-50 | 《梅兰芳》等邮票 | create | terms/youpiao.md | L8212 |
| 23 | cand-12-52 | 《中国包装》 | create | publications/zhongguo-baozhuang.md | L8218 |
| 24 | cand-12-53 | 《包装年鉴》 | create | publications/baozhuang-nianjian.md | L8218 |
| 25 | cand-12-57 | 2008年北京奥运会标志 | create | works/aoyun-2008-biaozhi.md | L8236 |
| 26 | cand-12-58 | 中国银行标志 | create | works/zhongguo-yinhang-biaozhi.md | L8238 |
| 27 | cand-12-59 | 中国铁路标志 | create | works/zhongguo-tielu-biaozhi.md | L8238 |
| 28 | cand-12-60 | “永久”牌自行车 | create | works/yongjiu-zixingche.md | L8238 |
| 29 | cand-12-61 | 中国民航“凤凰”标志 | create | works/minhang-fenghuang-biaozhi.md | L8238 |
| 30 | cand-12-62 | 中国人民政治协商会议会徽 | create | works/zhengxie-huihui.md | L8227 |
| 31 | cand-12-167 | 交通标志 | create | terms/jiaotong-biaozhi.md | L8240 |
| 32 | cand-12-168 | 商品标志 | create | terms/shangpin-biaozhi.md | L8242 |

## 四、30 条新建分型

- 出版物 17：《呐喊》《彷徨》《坟》《冯小青》《万象》《中国历代货币大系》《毛泽东选集》《中国历代绘画》《陈寅恪文集》《老房子》《老照片》《汉声》《读书》《国际广告》《中国广告》《中国包装》《包装年鉴》。
- 人物 3：钱君陶、金梅生、李慕白。
- 术语 4：阴丹士林色布、邮票、交通标志、商品标志。
- 作品 6：2008年北京奥运会标志、中国银行标志、中国铁路标志、“永久”牌自行车、中国民航“凤凰”标志、中国人民政治协商会议会徽。

维度分布：primary C 29 条、primary B 1 条（阴丹士林色布）；secondary D 22 条、secondary E 2 条（《汉声》、2008年北京奥运会标志）。confidence：medium 9 条、low 21 条。

## 五、2 条更新

| 目标 | 类型 | 处理 | 版本变化 | 新增证据 |
|---|---|---|---|---:|
| publications/liangyou.md | 跨书新增来源 | 追加赵农 2009 来源块与一句影响力评语 | source_count 2→3，version 1→2 | L8125 |
| publications/zhuangshi-zazhi.md | 跨书新增来源 | 追加赵农 2009 来源块，补 1949 年后字体设计与改革开放后封面两条 | source_count 2→3，version 1→2 | L8127, L8131 |

两处更新均保留原夏燕靖两版来源，不删旧证据；日期续为 2026-10-26，review_due 续为 2027-04-26。

## 六、合并与不重复立条

- 四条邮票候选（《梅兰芳》《西厢记》《中国民居》《十二生肖》）合并为「邮票」一条，不按四套邮票分列；四套票名在条目中作为来源举例保留。
- 《良友画报》与既有 `publications/liangyou.md` 同指，《装饰》与既有 `publications/zhuangshi-zazhi.md` 同指，均按更新处理，不新建同名条目。
- 鲁迅、陈之佛、闻一多、张光宇、郑曼陀、杭穉英已有 KU，不重复立条。
- 国徽已有 `works/guohui-1950.md`，本批不新建；奥运标志、银行标志等与国徽分列。
- 阴丹士林色布与既有 `terms/yangbu.md`（洋布大类）分属染色布产品与机织布大类，不合并。
- 《毛泽东选集》与 `persons/mao-zedong.md` 分属出版物与人物；“永久”牌自行车与 `terms/sanzhuan-yixiang.md` 分属品牌作品与消费组合，均不合并。
- 纸张、印刷两小节候选为 0：来源所述为技术史与既有 procedure 条目覆盖范围，未产生新的可立目实体。

## 七、语义复读修正

1. **删除无来源引文**：金梅生、李慕白两条初稿引「已成为中国商业广告的最早表现形式之一」，回查赵农全书未找到该句，已删除引号，改为据 L8186–L8188 转述月份牌的广告发布方式与题材。该句不属本书证据。
2. **修正省略号引文**：《呐喊》初稿引「鲁迅……受中国传统古籍插图和金石碑帖的影响……」，含省略号，不是同一行连续文字；已改为完整连续引文「受中国传统古籍插图和金石碑帖的影响，在书籍的封面、标题、插图、版式上都有很好的意见」。
3. **《装饰》载体不确定**：L8127「张光宇的《装饰》等字体设计」未说明是杂志还是单行本；因与既有《装饰》杂志同名且同属张光宇，按同名归并，并在条目正文与匹配质量中明记不确定。
4. **阴丹士林色布 OCR 残缺**：L8172–L8175 广告文字为繁体竖排 OCR，字序与字形多有残缺，未逐字引用，只按可辨语义概述，confidence 取 low。
5. **政协徽仅图注**：L8227 只有图注一行，正文未解释图 10-45；条目只登记图注事实，未视觉核验，未据来源外材料补设计者、年代与象征含义。

## 八、验证与门禁

- `_zn_struct.py _zn_ch10p_all.txt`：problems 0（32 文件）。
- `_zn_audit.py _zn_ch10p_all.txt`：findings 0。
- `_zn_audit_strict.py _zn_ch10p_files.txt`：findings 0（30 新文件）。
- `_zn_checklines_ch10p.py`：30 条、50 处引文，problems 0；另手工复核更新条目 4 处引文，均命中 L8125 / L8127 / L8131。
- 工作包 `2026-10-26-2009zhaonong-units-batch-p`：ledger 96 行，apply-plan 32 行，create 30、update 2；候选索引写回 32 条，全部 `needs_evidence → applied`，`lifecycle_class: terminal`。
- 索引与闭合：`build_discovery_index.py` 5339 条，`build_translation_index.py` 1678 条；`run_sync_closure.py --refresh-generated --full` 通过，250 tests + 16 subtests。
- 状态：applied 2309、rejected 852、no_delta 192、needs_evidence 1986、terminal 3353；total_units 2070；health 102/130。
- 内容审计 12 项，均为既有问题（8 项空 frontmatter、1 项跨类型同名、3 项占位内容），无一项落在本批文件。

## 九、状态与下一跳

- 本批状态：closed（30 新建 + 2 更新已写回，索引与生成态已刷新）。
- 第十章剩余：第六节货币与交通 12 条、第七节艺术设计教育 9 条，合并为 batch Q（21 条）；随后「总结」9 条为 batch R。
- 之后转 2010 田自秉（404 条）与 2011 李立新（189 条 unit、1363 条 claim）。
- 未 commit、未 push；`03基础书籍-md文档/` 未改写；未创建分支或 worktree；Book 7 及以后未启动。
