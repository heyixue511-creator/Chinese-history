# 赵农《中国艺术设计史》2009 册机构候选批次（四）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009zhaonong-institutions-batch-s/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 处理赵农《中国艺术设计史》（2009）institution 候选 11 个（源行号 L8137—L8560，近代造纸、广告、货币与设计教育），逐条回读原文并作语义裁决。
- 11 个全部判 `create`，新建 institution KU；无 `update`、无 `rejected`、无 `no_delta`、无并入其他候选。
- 11 个候选终态：applied 11（create 11）。
- KU 总数由 781 增至 792；institution 类型由 100 增至 111。
- 候选索引投影后：applied 887、no_delta 56、rejected 808、needs_evidence 3,588；总数 5,339。
- `02-sources/` 未改动；`03基础书籍-md文档/` 只读；本会话未执行 commit／push。

**范围说明**：2009 赵农册共有 41 个 institution 候选，批次 P、Q、R、S（10＋10＋10＋11）至此全部处理完毕。六册 institution 候选剩 48 个：2010 田自秉 37 个、2011 李立新 11 个。

**台账行数说明**：本批 ledger 为 **33 行**。11 个 applied 候选各走完整三行，11 × 3 = 33；无 rejected 单行。

## 二、新建清单

| 文件 | 来源位置 | 主要增量 |
|---|---|---|
| institutions/lunzhang-zaozhi-ju.md | 2009 L8145 | 纶章造纸局：1891 年李鸿章创建，中国近代第一家引进国外造纸技术的工场。来源未给地点；既有 `procedures/xiandai-zaozhi-jishu.md` 作“上海（纶章造纸局）”，本批来源无对应文本，条目标“未详”并注明待核。未给创办方式、资本、设备、原料、产品、产量与沿革 |
| institutions/guangzhou-zaozhichang.md | 2009 L8145 | 广州造纸厂：民国时期能生产一定数量新闻纸；因依赖进口纸浆，抗战爆发后无法形成规模化生产。未给创设年份、厂址、设备、纸浆来源国、产量与战后结局 |
| institutions/yingmei-yancao-gongsi.md | 2009 L8168-L8182、L8186-L8188、L8214；夏燕靖 2009 L4069；夏燕靖 2016 L5011；高丰 L5377；李立新 L1320 | 英美烟草公司：招贴为 20 世纪早期上海等大城市最引人注目的广告，哈德门／老刀牌／红锡包占很大市场；邀请画家绘制月份牌并以赠送发布；现代意义包装伴随香烟销售出现；广告部规模最大，聘中国画家胡伯翔、倪耕野、梁鼎铭、丁悚、丁纳、杨芹生、杨秀英、唐九如等 10 余人，张光宇、张正宇参与；胡伯翔任设计骨干、张光宇从事广告设计 7 年、丁悚为设计骨干；南洋／英美／华成设驻厂设计师。并录“丁纳／丁讷”与张光宇身份表述差异 |
| institutions/zhongguo-renmin-yinhang.md | 2009 L8265 | 中国人民银行：1948 年 12 月首次发行人民币，已发行 5 套，以元、角、分为单位、十进位制，分铸币与纸币，按时更新，引进国际先进技术，精心设计并采取防伪措施。同段民国银圆“烂板”与地方银行滥发银券钱票只作背景，与机构沿革分开 |
| institutions/fuzhou-mawei-chuanzheng-xuetang-huishiyuan.md | 2009 L8361 | 福州马尾船政学堂绘事院：1867 年设立，与 1888 年江南船政局工艺学堂并列为“中国设计教育出现并快速发展”的起点。与既有福建船政局条不重复，该条记船政局与求实堂艺局而未记绘事院。未给创办人、学制、课程、招生、教员、学生数与停办时间 |
| institutions/jiangnan-chuanzhengju-gongyi-xuetang.md | 2009 L8361 | 江南船政局工艺学堂：1888 年开办，为设计教育起点之一。“江南船政局”一名来源仅此一见，未说明与江南制造总局的关系；条目不把二者等同，地点与上级机构标待核 |
| institutions/beiping-guoli-yizhuan.md | 2009 L8367 | 北平国立艺专：1949 年以前许多美术学校设“工艺”“实用美术”专业，仅与绘画、雕塑平衡；北平国立艺专图案系与杭州国立艺专图案系并列最具实力。同段蔡元培《美术的起源》学科分类与陈之佛 1929 年介绍包豪斯只作语境。未给创办年份、校址、课程、师资与学生数 |
| institutions/hangzhou-guoli-yizhuan.md | 2009 L8367、L8378；田自秉 L5723 | 杭州国立艺专：图案系最具实力，聚集一大批艺术设计专业教师；1950 年改名中央美术学院华东分院，实用美术系合并入中央美术学院实用美术系；1956 年成立中央工艺美术学院；其他地方院校相继设实用美术系／工艺系并改系科名。田自秉记解放前在该校求学、常去浙江省图书馆阅览《格古要论》《骨董琐记》并注意古代生活用品制作特点。并录校名两写与段首标题异常 |
| institutions/qinggongbu-qinggong-xueyuan.md | 2009 L8380 | 轻工业部属四所轻工学院（1 个候选并列四校，按院校群立目）：无锡、大连、北京、西北轻工学院与中央工艺美术学院同属轻工部管理，但从工业产品设计角度注重教学与市场调研，教学方向各有侧重，使中国艺术设计发展出现不同选择。不拆成四条，也不并入中央工艺美术学院 |
| institutions/dasheng-shachang.md | 2009 L8515；高丰 L5279 | 大生纱厂：1899 年张謇在南通创办，后办大生二厂、三厂、八厂。高丰在张謇小传中作实业成就，赵农在“官商一体”结构性批评中作反例，称其“用各种手段压制其他私人企业的发展”“无法推动中国社会生产力的进步”；两说并录为史学立场差异。未给资本、纱锭、产量与设备 |
| institutions/yiwensi-tushu-gongsi.md | 2009 L8184；高丰 L5348 | 伊文思图书公司：1926 年上海南京路出现销售打字机的广告。高丰作“霓虹灯传入我国”的最早实例（南京东路、橱窗、“皇家牌”打字机英文广告），赵农作“吊灯广告”并称随后出现大量霓虹灯广告；两说并录，不裁断是否同一物 |

- 11 个新建均 `source_count` 按实际来源数（英美烟草 5、大生 2、伊文思 2、杭州 2，其余 7 个单源）、`version: 1`、`evidence_status: source_backed`、`confidence: medium`、`consensus: tentative`。
- 维度：英美烟草、伊文思为 C 主导；大生、人民银行、四校群为 D 主导；纶章、广州造纸为 B 主导；绘事院、江南工艺学堂、北平艺专、杭州艺专为 D 主导（兼 B 或 C）。
- after 指纹（前 19 位）：lunzhang-zaozhi-ju `sha256:a45869bd0eac…`（4,411 bytes／84 行）；guangzhou-zaozhichang `a9c0db37b939…`（3,872／84）；yingmei-yancao-gongsi `12ae35658bd9…`（9,828／126）；zhongguo-renmin-yinhang `20ac134f688e…`（5,165／87）；fuzhou-mawei-chuanzheng-xuetang-huishiyuan `645b952efda0…`（5,330／87）；jiangnan-chuanzhengju-gongyi-xuetang `c68c2c3c21a0…`（5,154／85）；beiping-guoli-yizhuan `c708fc16e312…`（5,225／85）；hangzhou-guoli-yizhuan `9afae9a60f6c…`（7,072／98）；qinggongbu-qinggong-xueyuan `33666d7553ba…`（5,728／87）；dasheng-shachang `0b9accff25e7…`（5,447／95）；yiwensi-tushu-gongsi `aaf34144559d…`（5,401／94）。

## 三、update 清单

本批无 `update`。11 个候选与既有 institution KU 均无同名条目：大生纱厂、英美烟草公司、伊文思图书公司虽已在 `persons/zhang-jian.md`、`terms/yuefenpai.md`、`persons/zhang-guang-yu.md` 等 KU 中被提及，但没有同名 institution 条目，故按新建处理；杭州国立艺专、北平国立艺专、四所轻工学院亦无既有 institution 条目。

## 四、no_delta 判定

本批无 `no_delta`。

## 五、rejected 判定

本批无 `rejected`。

## 六、本批的判断

1. **同一机构不因“被提及”而降级**：大生纱厂已在张謇 KU 中详记，英美烟草公司已在月份牌、张光宇等 KU 中被提及，但条目类型不同；institution 层缺条目，仍按 create 立目，避免用人物或术语条目替代机构本体。
2. **评价冲突并录，不裁断**：大生纱厂的“实业先驱／官商一体”分歧、伊文思广告的“霓虹灯／吊灯广告”与“南京东路／南京路”差异、英美烟草“丁纳／丁讷”与张光宇“广告设计 7 年／驻厂设计师”的表述差异，均在正文并列并注明来源，不据一册改写另一册。
3. **单源信息不补外部知识**：纶章造纸局、广州造纸厂、人民银行、绘事院、江南工艺学堂、北平艺专、四校群均只有赵农一句或一段，条目不补创办人、课程、产量、设备等来源外细节；人民银行条目把同段民国货币背景与机构沿革分开。
4. **名称歧义保留待核**：纶章造纸局的“上海”只见于既有 procedure 条目，本批来源未给，标待核；“江南船政局”与江南制造总局的关系来源未说明，条目不把二者等同。
5. **子机构与上级机构分条**：福州马尾船政学堂绘事院与既有福建船政局条分属不同层级，后者不记绘事院，故新建而不 update；江南船政局工艺学堂同理不与江南制造总局合并。
6. **院校群按候选粒度立目**：无锡、大连、北京、西北轻工学院是 1 个候选并列四校，来源只给群体判断，按院校群立目，不拆成四条，也不并入中央工艺美术学院条。
7. **段落标题异常不据以合并**：赵农 L8378 以小标题“中央工艺美术学院”起头却先叙国立杭州艺术专科学校，来源无连接语；杭州艺专条目保留该异常，不把杭州艺专判为中央工艺美术学院的前身或分支。
8. **内容审计首轮 3 项已修正**：北平国立艺专、杭州国立艺专、四校群三个 title 初稿为“中文（中文别名）”，不符合双语 title 约定；已改为“中文（English）”，复检 0 findings。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：33 行；11 个候选；applied 11（各 3 行）；终态行均带 `target_ref`。
- `apply-plan.jsonl`：11 行；create 11、update 0；create 的 `before` 为 null；11/11 的 after 指纹、bytes、lines 与磁盘一致。
- `canonical-mapping.json`：11 条（全部 create）；`merged_candidates` 全为空。
- 候选索引：5,339 行；批前 `sha256:69d4e865…`（applied 876、needs_evidence 3,599、no_delta 56、rejected 808），批后 `sha256:8cefbf52…`（applied 887、needs_evidence 3,588、no_delta 56、rejected 808）；重建幂等。
- 内容质量审计：792 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 792/792 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，institutions 111、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；792 个 KU 均未建立正式 relation。
- 规则漂移审计：0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过；pytest 250 项、16 subtests 通过（failures 0、errors 0、skipped 0）。
- Sync closure：`--refresh-generated --full` 运行 18/18 通过；另以 `--refresh-generated --check-generated --full` 复核，第 1—16 步完成，第 17 步因工作树未提交、10 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。10 个文件为：`04-knowledge/quality/translation-index.yml`、`05-outputs/index/index.md`、`05-outputs/knowledge-graph-data.js`、`05-outputs/knowledge-graph-data.json`、`06-runtime/automation/index.md`、`06-runtime/governance/governance-backlog.md`、`06-runtime/state/candidate-index.jsonl`、`06-runtime/state/current-health.json`、`06-runtime/state/discovery-manifest.json`、`06-runtime/state/generated-projections-manifest.json`。

## 八、边界与研究债

- 11 个新建中 7 个仅有赵农 2009 一条来源，4 个为多源（英美烟草 5 册、大生 2 册、伊文思 2 册、杭州 2 册）；全部 `consensus: tentative`，验证层级未评定，图版未视觉核验。
- 具体缺项：纶章造纸局缺地点、创办方式、资本、设备、原料、产品与沿革；广州造纸厂缺创设年份、厂址、设备、纸浆来源、产量与战后结局；英美烟草公司缺成立年份、国籍与资本、注册地、厂址、品牌注册、广告投放量、广告部编制与月份牌印数；中国人民银行缺行址、隶属、发行准备制度、各套发行年份、版别、设计者与印制单位；绘事院与江南工艺学堂缺创办人、学制、课程、招生、教员、学生数与停办时间；北平国立艺专缺创办年份、校址、课程与师资；杭州国立艺专缺创办年份、校址、系科、教师名单与 1950 年后校名沿革；四校群缺各校成立年份、校址、专业与课程；大生纱厂缺资本、纱锭、产量、设备与二／三／八厂年份；伊文思图书公司缺公司性质、创办人、成立年份、地址、广告制作者与存续时间。
- 已并存未释的张力：纶章造纸局的“上海”地点；伊文思广告的“霓虹灯／吊灯广告”与“南京东路／南京路”；大生纱厂的“先驱／官商一体”评价；英美烟草的“丁纳／丁讷”与张光宇身份表述；杭州艺专的“杭州国立艺专／国立杭州艺术专科学校”与段首标题异常；“江南船政局”与江南制造总局的关系。
- 结构层仍为 0/4，层级完整挂载 0/792，正式 relation 0 条，Theme／Topic 均未实体化。
- 2009 赵农 41 个 institution 候选已全部处理（P 10、Q 10、R 10、S 11）；六册 institution 候选剩 48 个：2010 田自秉 37 个、2011 李立新 11 个。
- 下一批（批次 T）转 2010 田自秉 37 个 institution 候选，需先做候选清点与既有条目对账。
- 本批临时脚本（`_tmp_institutionss_emit.py`、`_tmp_institutionss_verify.py`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理；`_tmp_s_repo_audit.json`、`_tmp_s_repo_full.json`、`_tmp_s_closure19.txt` 同批待清理。
