# 赵农 2009《中国艺术设计史》claim 批次 zn1b（第一章 26 条）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-27-2009zhaonong-claims-batch-zn1b/`
- 来源：赵农《中国艺术设计史》（2009，高等教育出版社），doc_id `2009-zhaonong-zhongguo-yishu-shejishi`
- 候选范围：第一章“文明的曙光——石器时期的设计”L358-L1037 的 26 条 claim 候选，覆盖绪论、上古传说、石器与玉器、陶器与彩陶、骨器与箭器、建筑与村落、纺织与饰品、结论八节。
- 背景：zn1a 完成后 registry 为 403 条，赵农册剩余 366 条 claim 候选。
- 裁定结果：新建 26 条 claim（`claim-0404` 至 `claim-0429`）；无同义合并、无并入既有 claim、无 rejected、无 no_delta；26 条全部 terminal。
- 册级进度：赵农册已处理 36 条，剩余 340 条 `needs_evidence`。

## 2. 来源与复读范围

- 来源文件 8800 行，UTF-8 无 BOM、LF；本批只读，不改写。
- 逐段复读 L358-L1037：第一节绪论（人类史与设计史、工具与武器、环境与定居）、第二节上古传说（女娲、伏羲、有巢氏、燧人氏、神农氏、黄帝、龙凤）、第三节石器与玉器（定居、农耕、石器类型、玉器与良渚）、第四节陶器与彩陶（制陶、器形、陶轮陶窑、彩陶与尖底瓶）、第五节骨器与箭器（骨针、骨耜、弓箭、渔钩、刀矛）、第六节建筑与村落（半地穴式、干栏式、水井、城堡）、第七节纺织与饰品（蚕桑、纺轮、编织、饰物、贝币、文字、乐器）、第八节结论。
- 26 条候选的语义行见各行 `key_lines`；包围跨度去重后 24 个，因为 `claim-0418`/`0419` 同处 L768-L792、`claim-0420`/`0421` 同处 L812-L829。
- 未读部分：章内插图与图注未逐张视觉核验；思考练习题 L1028-L1037 不建候选；第一节前的地球与文明起源段落只作上下文，不单独建条。

**来源张力提示**：

- L362 的“公元前 22 世纪以前”注明据《我国历代纪元表》，本批未把该断代写成独立 claim。
- L618 的“数十万年”与 L772 的石箭头“距今约 28945 年”是原文给出的年代，未给测年方法。
- L787 直接引用恩格斯《家庭、私有制和国家的起源》中译句，未给版本、页码与译者。
- L878 的“公元前 3000 年左右”的郑州西山城址与“50 多处”龙山城堡，未给遗址清单与统计口径。
- L915 的绢片“每厘米 48 根”来自原文，未给检测报告。

## 3. 裁定结果

| 处置 | 候选数 | claim 行 |
|---|---:|---:|
| 新建（主候选） | 26 | 26 |
| 并入新建 claim（同义重复） | 0 | 0 |
| 并入既有 claim | 0 | 0 |
| rejected | 0 | 0 |
| no_delta | 0 | 0 |
| 合计 | 26 | 26 |

- 类型：historiographic 7（`0404`、`0409`、`0411`、`0414`、`0422`、`0424`、`0426`）、interpretive 14（`0405`、`0406`、`0407`、`0408`、`0410`、`0412`、`0413`、`0418`、`0419`、`0420`、`0421`、`0423`、`0425`、`0429`）、factual 2（`0415`、`0416`）、evaluative 2（`0417`、`0428`）、synthetic 1（`0427`）。
- 类型映射：`cand-01-71`、`01-72` 的 `basic_fact` 按语义映射为 factual_claim；`cand-02-62` 的 `source_claim` 按语义映射为 interpretive_claim；其余按候选原值写入。
- 置信度 medium 26；跨度类型 line 1（`0411`）、bounded 25；全部 `consensus: tentative`、`review_status: source_backed`。
- 代表条目：`claim-0408` 良渚玉钺/琮/璧与权力财富；`claim-0410` 骨针与手指、脑智力、职业分工；`claim-0419` 恩格斯弓箭引文；`claim-0422` 城堡与技术职业专门化；`claim-0427` 第八节结论的地理环境与设计文化生成。

## 4. 语义判断与支持链接

- 判重：26 条逐条与既有 403 条 claim 对读，未发现同义断言，全部新建；无 `merged_candidate_ids`、无 `corroborating_spans`。
- 同段近邻：`cand-02-61`（弓箭设计思想）与 `cand-02-62`（恩格斯引文）同处 L768-L792，前者为设计学解释、后者为文献转引，分别建 `claim-0418`、`claim-0419`；`cand-02-63`（建筑三条件）与 `cand-02-64`（面南而居）同处 L812-L829，分别建 `claim-0420`、`claim-0421`。
- 30 条 `supported_by` 覆盖 25 个不同路径：
  - places 8 条链接 / 5 个路径：`liangzhu-gucheng`、`banpo-site`（0408、0420、0421、0428）、`hemudu-site`、`xishan-chengzhi`。
  - terms 20 条链接 / 19 个路径：`yishu-sheji`、`yuanshi-nongju`、`yue-battle-axe`、`yu-yue-cong-bi`、`yushi`、`ding`、`taoqi`（0409、0416、0417）、`shandingdong-ren-guzhen`、`yuanshi-fuzhuang`、`bagua`、`shougong-bianzhi`、`heitao`、`gongjian`（0418、0419）、`bandixue-shi-jianzhu`、`ganlan-shi-jianzhu`、`fanglun`、`beibi`、`banpo-kehua-fuhao`、`caihui-tao`。
  - persons 2 条链接 / 1 个路径：`leizu` 同时支撑 `claim-0423` 的蚕桑判断。
- `claim-0405`、`0407`、`0412`、`0413`、`0414`、`0415`、`0427` 为无直接 KU 可链的判断或年代陈述，`supported_by` 为空。
- 30 条链接经闭包投影为 60 条关系条目（1922→1982）；未新建或改动 KU，未手工改动 translation-index。
- `claim-0419` 为恩格斯引文，`statement_zh` 保留“赵农引……语”的转引结构，不把引文写成赵农本人的原创判断。

## 5. 跨批维护

- `claim-registry.yml`：751582→787633 bytes；hash `sha256:9f7e005b…`→`sha256:1ae1bd1e6b619c3a9626984364ed09b711a7297f79dc747c0425c6ab6433af48`；header total 403→429。
- 候选索引：applied 3395→3421；needs 839→813；rejected 871；no_delta 234；terminal 4526；active 813。
- 赵农册：claim 候选 366→340 条 needs；全部候选 applied 1078、needs 340、rejected 227、no_delta 51。
- 全库 claim 债务 813 条：赵农 340、田自秉 278、李立新 195。
- 包内工件：`manifest.json`、`claim-rows.jsonl`（26 行）、`claim-updates.jsonl`（0 行）、`apply-plan.jsonl`（26 行 create）、`candidate-decision-ledger.jsonl`（26 行）、`canonical-mapping.json`（26 条）、`summary.md`。
- 未 commit、未 push。

## 6. 生成态与门禁

- 写回前：`_zn_generic_preflight.py` 核对 registry 403、候选状态 3395/839/234/871、26 条候选均为 needs_evidence 且类型 claim、跨度落在 L358-L1037、关键词逐条命中、范围内候选与使用集合完全一致；结果 `claims 26`、`missing 0`、`extra 0`、`problem_count 0`。
- 写回：`_zn_generic_apply.py` 写入 26 行，registry 429 行、787633 bytes、30 条链接、25 个路径。
- 写回后：`_zn_generic_verify.py` 验证 429 行、26 条新 claim、类型计数、30/25 链接、候选状态 3421/813、lifecycle 4526/813、赵农册 needs 340、债务 813、包内 26/0/26/26/26 与 manifest 一致。
- 完整闭包：`python scripts/run_sync_closure.py --refresh-generated --full` 18/18 通过（250 项测试与 16 项子测试）。
- 发布门禁：`--check-generated` 仍在 check generated snapshots 失败（exit=1），相对 HEAD 的 11 个生成态文件差异与 zn1a 相同，属未提交批次累积；状态 `blocked_pending_commit`。

## 7. 未决事项与下一跳

- 26 条均为单来源，`supports` 为 0；evidence 层仍未建。
- 待补材料：石器/玉器断代与墓葬统计（0408、0414）、陶鼎年代序列（0409）、骨针使用痕迹（0410）、父系社会断代（0411）、弓箭实验与恩格斯版本页码（0418、0419）、建筑复原与房屋朝向统计（0420、0421）、城堡作坊定量（0422）、蚕桑考古（0423）、纺轮与织机实验（0424）、贝币计量（0425）、半坡符号释读（0426）、渔钩测量（0428）、饰物与彩陶纹样统计（0429）。
- 下一批：第二章“沉痛的狞厉——夏商西周时期的设计”L1038-L1764，41 条 claim 候选，拟编号 `zn2a`，claim 从 `claim-0430` 起。
- 其余：第三章 30、第四章 24、第五章 28、第六章 54、第七章 55、第八章 19、第九章 31、第十章 52、总结 4、后记 2；之后田自秉 278、李立新 195。
