# 第十五批：剩余 person doc_count=2 组（M 批）裁决总结

## 一、本批做了什么

本批处理剩余 21 个 `doc_count=2` 的 person 同名组，共 42 个候选：

- 19 组新建 person KU；
- 2 组整组拒绝：xdup-0237 贾兰坡、xdup-0243 阎立本；
- 19 个同组非 canonical 候选以“同一 entity、语义已并入”rejected；
- 0 个 no_delta，0 个既有 KU 更新。

状态链：19 条 canonical 走 `needs_evidence -> ready_for_review -> approved -> applied`；19 条 merged member 与 4 条整组拒绝候选走 `needs_evidence -> rejected`。台账共 80 行，apply-plan 共 19 行 create。

至此 person 类型全部 48 个 `doc_count=2` 同名组关闭，person 维度内不再有 open 的 doc2 组。

## 二、十九个新建 KU

| group_id | 实体 | slug | 维度 | sub_type | 主要来源 |
|---|---|---|---|---|---|
| xdup-0223 | 李有行 | `li-youxing` | C | designer | 高丰 2004 L5465-L5483；夏燕靖 2016 L4783-L4813 |
| xdup-0224 | 李诚 | `li-cheng` | B | architect | 赵农 2009 L5464-L5493；夏燕靖 2016 L3407-L3426 |
| xdup-0225 | 李鸿章 | `li-hongzhang` | D | statesman | 赵农 2009 L8137-L8168；夏燕靖 2016 L4946-L4972 |
| xdup-0227 | 杭穉英 | `hang-zhiying` | C | designer | 高丰 2004 L5366-L5384；赵农 2009 L8170-L8209 |
| xdup-0228 | 梁思成 | `liang-sicheng` | B | architect | 赵农 2009 L7721-L7752；夏燕靖 2016 L5150-L5181、L5302 |
| xdup-0229 | 毕昇 | `bi-sheng` | C | craftsman | 赵农 2009 L4995-L5016；李立新 2011 L1841 |
| xdup-0231 | 沈括 | `shen-kuo` | B | scientist | 赵农 2009 L4999-L5030；田自秉 2010 L3374 |
| xdup-0235 | 苏轼 | `su-shi` | A | scholar | 赵农 2009 L4962-L4993；李立新 2011 L847-L878、L1109 |
| xdup-0236 | 蒲元 | `pu-yuan` | B | craftsman | 夏燕靖 2009 L1879-L1890；2016 L1888-L1919 |
| xdup-0238 | 郑曼陀 | `zheng-mantuo` | C | designer | 高丰 2004 L5366-L5384；赵农 2009 L8170-L8209 |
| xdup-0239 | 郑观应 | `zheng-guanying` | D | scholar | 赵农 2009 L8363、L8527-L8529；李立新 2011 L1291 |
| xdup-0240 | 都锦生 | `du-jinsheng` | B | industrialist | 夏燕靖 2009 L3927-L3947；2016 L4851-L4868 |
| xdup-0241 | 鉴真 | `jianzhen` | E | other | 赵农 2009 L4232-L4246；夏燕靖 2016 L2518-L2528 |
| xdup-0242 | 闻一多 | `wen-yiduo` | C | designer | 赵农 2009 L8105-L8136；夏燕靖 2016 L5034 |
| xdup-0244 | 阿尼哥 | `anige` | B | architect | 赵农 2009 L6190-L6221；夏燕靖 2016 L3958-L3972 |
| xdup-0246 | 陶元庆 | `tao-yuanqing` | C | designer | 赵农 2009 L8105-L8136；夏燕靖 2016 L5013-L5044 |
| xdup-0247 | 雷发达 | `lei-fada` | B | architect | 夏燕靖 2009 L3666-L3669；2016 L4483-L4496 |
| xdup-0248 | 雷圭元 | `lei-guiyuan` | D | designer | 高丰 2004 L5465-L5483；夏燕靖 2016 L4820、L5177、L5280、L5993 |
| xdup-0250 | 顾恺之 | `gu-kai-zhi` | B | artist | 赵农 2009 L3874；李立新 2011 L940-L953 |

## 三、两组整组拒绝

- **xdup-0237 贾兰坡**：现代考古学家。李立新 L410、夏燕靖 2016 L357-L364 只引其石器研究结论，作为中国设计起源讨论的学术依据；来源未记其参与设计、工艺或造物活动。不建 person KU，也不并入任何既有条目。
- **xdup-0243 阎立本**：唐代画家。田自秉 2010 L3429、夏燕靖 2016 L2715-L2891 只以《步辇图》《萧翼赚兰亭图》作唐代服饰、家具的图像史料；来源未记其参与设计或工艺活动。不建 person KU。

两组均不写 `target_ref`；`build_discovery_index.py` 允许 rejected 行缺省该字段。

## 四、canonical 与 rejected

- canonical 选择以“内容最完整、proposed_slug 与最终文件名最接近”为准：19 组分别落在夏燕靖 2016（10 组）、赵农 2009（4 组）、高丰 2004（2 组）、李立新 2011（2 组）、夏燕靖 2009（1 组）。
- 19 个非 canonical 候选均因同一 entity 合并而 rejected，`target_ref` 指向新建 KU。
- 异写 slug 统一：`hang-zhi-ying` 取 `hang-zhiying`；`li-cheng` 保留并置别名“李诫”；`anige` 保留通行藏文转写。
- 新建 KU 全部 `confidence=medium`、`consensus=tentative`、`evidence_status=source_backed`，未升级验证层级。

## 五、关键发现

1. **C 维度民国视觉传达谱系基本成形**：月份牌一线有周慕桥（未建）、郑曼陀、杭穉英；书籍装帧一线有鲁迅（未建）、陶元庆、闻一多、丰子恺、张光宇、陈之佛。两条谱系在赵农 2009 同一节并列。
2. **B 维度建筑谱系跨时代连续**：李诚（宋《营造法式》）—阿尼哥（元喇嘛塔）—雷发达（清样式雷）—吕彦直、梁思成（近代），形成官式建筑规范与技术传承的完整序列。
3. **D 维度洋务—实业谱系闭环**：曾国藩、李鸿章、左宗棠、张之洞、郑观应由人物到主张，均可回溯到赵农 2009 晚清章节；江南制造总局、轮船招商局等机构尚未单独成 KU，为下一层研究债。
4. **E 维度出现“工匠随行”型传播节点**：鉴真东渡携玉作人、雕檀、刻镂等工手 85 人，与利玛窦、郎世宁的“器物—知识”传入路径并列，构成两种跨文化传播模型。
5. **印刷设计谱系可上溯**：毕昇—王祯—毛晋三代并置，李立新把毕昇纳入“印刷设计家集群”，而非仅作技术发明者。
6. **来源内部张力持续保留**：蒲元独轮车的发明者与时代、阿尼哥白塔高度（53 米／50.9 米）、李诚成书年代（哲宗／熙宁）、李鸿章生卒（赵农给／2016 未给），均并列照录。
7. **图像史料人物与设计主体的边界明确**：阎立本、贾兰坡两组说明“被引作史料”不等于“设计史人物”，与 L 批夏燕靖 paratext 规则共同构成人物准入的两条否定边界。

## 六、状态与验证

| 项目 | 结果 |
|---|---|
| 新建 KU | 19 |
| 更新 KU | 0 |
| rejected 候选 | 23 |
| ledger 行 | 80 |
| apply-plan 行 | 19 |
| apply-plan 哈希核对 | 19/19 |
| KU 总数 | 206 |
| 候选索引 | 5,339 行；applied 197、no_delta 10、rejected 492、needs_evidence 4,640 |
| lifecycle | active 4,640、terminal 699 |
| 内容质量审查 | 206 KU，0 findings |
| 仓库审查 | 0 问题；evidence 206/206；persons 72 |
| pre-commit | 规则漂移 0 |
| sync closure | 19 steps；250 passed, 16 subtests |
| person doc2 同名组 | 48 组全部关闭，0 组 open |
| doc2 同名组总计 | 352，已关闭 50，剩余 302 |
| doc_count=1 open | 6 |
| doc_count≥3 open | 0 |
| open members | 617 |

## 七、边界与研究债

- 未 commit、未 push；只改工作树。
- 未新建分支或 worktree；只保留 `main`。
- `02-sources/` 与 `03基础书籍-md文档/` 只读。
- 未使用外部验证平台；未做图版、器物、手稿或档案核对。
- 19 条 KU 均为 `confidence=medium`、`consensus=tentative`、`evidence_status=source_backed`。
- `primary_theme` 与 `topic_memberships` 留空；Theme/Topic 尚未 materialize。
- 未写入正式 `relations`；同段并置只作非断言性叙述。
- 下一步：term（134 个 open doc2 组）→ work（52）→ publication（46）→ institution（26）→ place（25）→ procedure（10）→ event（9），再处理 doc1 组、ungrouped unit 与 claim。
- 本批只覆盖前六册；Book 7 及以后未启动。
