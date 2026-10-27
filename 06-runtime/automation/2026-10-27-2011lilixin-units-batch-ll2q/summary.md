# 2011 册 units 批次 LL2q（著者、导师、意匠化与后记）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2011lilixin-units-batch-ll2q/`
- 来源：李立新《中国设计艺术史论》（2011），doc_id `2011-lilixin-zhongguo-sheji-yishu-shilun`
- 候选范围：李立新 2011 册余下 5 条单元候选（3 条首末提及的长跨度条目、2 条后记条目）
- 裁定结果：新建 5 条、更新 0 条、no_delta 0 条、rejected 0 条
- 状态：applied（5 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 候选跨度是首末提及的包围跨度：cand-01-01 李立新 L5-L2464、cand-01-57 张道一 L341-L2446、cand-01-72 意匠化设计 L368-L1169。中间未逐行复读，按各提及处语境裁定。
- 实际复读 7 段共 114 行：
  - L5-L60（56 行）：书名页、封面提要、CIP 数据、版权页与版次。
  - L341（1 行）：1994 年 6 月东南大学在张道一倡导和组建下设立我国第一个艺术学系。
  - L368-L390（23 行）：设计史分期、意匠化与写实性的对举、张道一的判断、院体画成因。
  - L857（1 行）：汉代以来意匠化设计到宋代画上句号。
  - L1159-L1169（11 行）：意匠化设计的界定、例证与元明清余波。
  - L1517（1 行）：《跛者不踊》的转引与李立新的引申。
  - L2444-L2464（21 行）：后记全段，含成书说明、求学经历、答辩与评审名单、致谢、署名 2003 年 6 月 28 日。
- 候选跨度并集按首末取 L5-L2464，共 2460 行；这是包围跨度，不等于连续复读。本批实际复读 114 行，其余未读。
- 未读但相关的范围：论文《造物之迹》原文（来源外）、张道一《跛者不踊》原文（来源外）、全书正文各章、图版与脚注。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-01-01 | 李立新 | 新建 | `persons/li-lixin.md` |
| cand-01-57 | 张道一 | 新建 | `persons/zhang-daoyi.md` |
| cand-01-72 | 意匠化设计 | 新建 | `terms/yijianghua-sheji.md` |
| cand-06-04 | 造物之迹——中国设计艺术史引论 | 新建 | `publications/zaowu-zhi-ji.md` |
| cand-06-08 | 中国设计艺术史 | 新建 | `publications/zhongguo-sheji-yishu-shi.md` |

## 4. 新建 5 条

- `persons/li-lixin.md`（李立新），medium，A 维度（次 D）。承载版权页与 CIP 著者身份、人民出版社 2011 年 10 月第 1 版、封面提要的研究取向、1998 年苏州大学艺术学院研究生毕业、1999 年 9 月考入东南大学师从张道一、2002 年 6 月 15 日答辩、本书由博士论文修改完成、后记署 2003 年 6 月 28 日。
- `persons/zhang-daoyi.md`（张道一），medium，A 维度（次 D）。承载著名学者身份、1994 年 6 月倡导和组建东南大学第一个艺术学系、李立新的博士导师、宋代之后意匠化局面消失的判断、《跛者不踊》对美术史单线叙述的批评、后记评价与合写《中国设计艺术史》的计划。
- `terms/yijianghua-sheji.md`（意匠化设计），medium，A 维度（次 C）。承载宋前意匠化与宋后写实性的风格对举、彩陶至金银器等例证、象征性与寓意性的装饰意匠界定、宋代句号、院体画扩张的成因、元明清余波与三种异写。
- `publications/zaowu-zhi-ji.md`（造物之迹——中国设计艺术史引论），medium，A 维度。承载博士论文题名、与本书的成书关系、2002 年 6 月 15 日答辩、同行评审与答辩委员会名单、指导教授；2002 只作答辩年，不当作出版年。
- `publications/zhongguo-sheji-yishu-shi.md`（中国设计艺术史），low，A 维度。承载后记所记由张道一带头、胡平与李立新参与合写的计划、选题“造物艺术史”、前期资料工作与博士论文的关系；原文未记出版信息，只是写作计划。

5 条新建均为 version 1、source_count 1，created/updated/last_verified 均为 2026-10-27，review_due 2027-04-27。

## 5. 判重与别名复核

| 候选 | 既有条目 | 判据 |
|---|---|---|
| cand-01-01 李立新 | `events/li-lixin-doctoral-defense-2002.md`、`events/dongnan-daxue-yishuxuexi-1994.md` | 两个 event 条承担事件，不承担著者身份、出版项与人物关系；按 person 新建，不重复事件内容 |
| cand-01-57 张道一 | `events/dongnan-daxue-yishuxuexi-1994.md`、`persons/gao-feng.md` 等的顺带提及 | 无 person 条；event 只记建系事件；按 person 新建 |
| cand-01-72 意匠化设计 | `terms/benyuan-tezheng.md`、`terms/bian-yu-tong.md`、`terms/sanzhong-zaowu-sheji.md` | 两个特质条是结论章的第 7、8 项，本条是风格分期概念；层次不同，按 term 新建 |
| cand-06-04 造物之迹 | 无 publication 条 | 与 `events/li-lixin-doctoral-defense-2002.md` 分工：event 记答辩，publication 记论文本身 |
| cand-06-08 中国设计艺术史 | 无 publication 条 | 与本书《中国设计艺术史论》书名不同，与赵农《中国艺术设计史》、夏燕靖《中国设计史》均不同，不合并 |

本批未出现“候选记 novel、实际已有别名条”的漏判：5 条均有明确的不合并理由或新建理由。

## 6. 语义判断与内部张力

- **著者与封面提要的归属**：封面提要称设计史更重一般造物而不仅是经典与宫廷设计，该提要同时出现在书名页与版权页前（L7、L19）。本条按封面提要记录，不写成作者自述。
- **事件与人物分工**：1994 年建系与 2002 年答辩已由两个 event 条承担；本批 person 条只记人物身份、关系与观点，避免同一事实在两类条目中重复叙述。
- **张道一批评的边界**：来源记张道一在《跛者不踊》中批评美术史习惯把传统穿成一条线、质疑承传关系是否客观；多元并进、共时多元与把这一视野移入设计史是李立新的引申。条目在正文与核心内容两处分别标明归属，不把引申写成张道一本人对设计史的方法主张。
- **意匠化的三种异写**：来源并用“意匠化设计”“意匠性设计”“意匠设计”，本条以“意匠化设计”立目，别名并列三种写法，不改写引文。
- **意匠化的定义边界**：来源没有单一定义句，只有分期对举、例证范围与“象征性或寓意性”的形容；本条据多处归纳，并在证据边界注明未设定义专节。
- **计划著作的置信度**：《中国设计艺术史》只见后记一句计划与一段前期工作说明，原文未记出版信息与成书状态；confidence 取 low，不据外部书目补写出版项，也不把书名与本书《中国设计艺术史论》混同。
- **博士论文的年份**：2002 年是答辩年，原文未记论文完成年与出版信息；`publication_year` 记“未载（2002年答辩）”，不把答辩年当作出版年。
- **李立新的身份边界**：来源只给版权页、CIP 与后记，能确认著者身份与 1998—2003 年的求学经历；生年、籍贯、职称、任职单位与其他著作均未载，条目不作外部补写。
- **后记中的出版社异文**：后记感谢“天津人民出版社的韩玉霞先生”（L2458），版权页与 CIP 记出版发行“人民出版社”（L49、L27），责任编辑同为韩玉霞（L45）。两处出版机构不同，来源内无从判定，本批未据此改动任何条目，留作研究债务。

## 7. 跨批维护

- 5 条 create 均为 version 1、created/updated/last_verified 2026-10-27、review_due 2027-04-27。
- 新条同 `persons/li-lixin.md`、`persons/zhang-daoyi.md`、`events/li-lixin-doctoral-defense-2002.md`、`events/dongnan-daxue-yishuxuexi-1994.md`、`terms/yijianghua-sheji.md`、`terms/benyuan-tezheng.md`、`terms/bian-yu-tong.md`、`terms/sanzhong-zaowu-sheji.md`、`events/song-dai-huayuan-sheli.md`、`publications/zaowu-zhi-ji.md`、`publications/zhongguo-sheji-yishu-shi.md` 建立相关知识元链接；未改动任何既有文件。
- 本批未发现既有条目的引文缺陷，未做额外的引号修正。
- 新增 publication 的 `author`、`publication_year`、`publisher` 三个字段，按既有 publication 条目的字段惯例填写；出版项未知时记“未载”，不置空。

## 8. 生成态与门禁

- `_zn_ll2q_check.py`：5 条新建的 35 处引文全部在所指单行内命中，problems 0。首轮曾把 L368 与 L370 的两处引文写在同一 `（L368）` 标签下，校验报 LINE，已改为 `（L368、L370）`。
- `_zn_struct.py`：5 个文件字段、六节、链接、日期、版本全部通过，problems 0。
- `_zn_audit.py`：5 个文件全库引文审计 findings 0。
- 内容质量审计：首轮新增 4 项 frontmatter 空字段，全在 `publications/zaowu-zhi-ji.md`（title、name_en、sub_type、tags）。原因是英文题名含“冒号加空格”，未加引号的 YAML 标量被解析成映射，连带后续字段错位；`_zn_struct.py` 未发现这一问题。已把英文题名由“Zaowu Zhi Ji: An Introduction to the History of Chinese Design Art”改为“Zaowu Zhi Ji (An Introduction to the History of Chinese Design Art)”并重建该条，内容质量发现归零。修复后 `content_quality_findings=20`，全部为本批之前的存量项，本批新条无内容质量发现。
- 候选索引：`needs_evidence` 1373 → 1368，`applied` 2862 → 2867，`no_delta` 233 不变，`rejected` 871 不变；总行数 5339 不变；active 1373 → 1368，terminal 3966 → 3971。
- 工作包：ledger 15 行、apply-plan 5 行、canonical-mapping 5 条；候选跨度并集 L5-L2464（2460 行），实际复读 114 行。
- 生成态：`build_discovery_index.py`、`build_translation_index.py`、`build_runtime_index.py` 已重建；`06-runtime/automation/index.md` 已收录本包。
- 完整闭包：`python scripts/run_sync_closure.py --refresh-generated --full` 18/18 通过，250 项测试与 16 项子测试通过，`structural_health=96`，`content_quality_findings=20`。
- 生成态发布门禁：在 `[17/19] check generated snapshots` 失败，原因是工作树内未提交批次累积的输入漂移；状态记 `blocked_pending_commit`。本批未获 commit 授权，不处理。

## 9. 未决事项

- 李立新 2011 册 unit 候选在本批后全部清零（0 条 `needs_evidence`）。
- 全库 unit 候选余 5 条开放，均属田自秉 2010 册：cand-01-10 曾中游父方壶 L82、cand-01-13 四鹿四龙四凤铜案 L92、cand-01-14 青铜尊和盘 L95、cand-01-16 蚱蜢纹金盏、镂空金匙 L101、cand-03-09 二里头铜爵 L78-L872。
- claim/evidence 流尚未启动：全库 claim 候选 1363 条，须走 collect → evidence JSONL → apply，写回入口 `scripts/verify_apply_evidence.py`。
- 本批识别的研究债务：张道一《跛者不踊》原文；论文《造物之迹》全文与出版项；后记所载“天津人民出版社”与版权页“人民出版社”的出版机构异文；李立新的生年、籍贯与任职单位；意匠化设计的定义专节与分界标准。
- 本批无 commit、无 push；索引与生成态改动留在工作树，等待用户明确授权。

## 10. 下一跳

- 下一批 LL2r：复读田自秉 2010 册 L78-L101 与 L872 一带，处理余下 5 条 unit 候选（四件图注器物与二里头铜爵）。
- 之后进入 claim/evidence 流：1363 条 claim 候选按 collect → evidence JSONL → apply 两阶段处理。
