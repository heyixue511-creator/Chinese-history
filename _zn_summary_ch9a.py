# -*- coding: utf-8 -*-
"""Write the batch-i summary with a generated decision table."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
PKG = ROOT / "06-runtime/automation/2026-10-26-2009zhaonong-units-batch-i"
cfg = json.loads((ROOT / "_zn_decisions_ch9a.json").read_text(encoding="utf-8"))

rows = []
for i, d in enumerate(cfg["decisions"], 1):
    target = d["target"] or "—（不立条）"
    if d["target"]:
        target = "`" + d["target"].split("04-knowledge/units/")[1] + "`"
    rows.append(f"| {i} | {d['entity']} | {d['action']} | {target} | {d['analysis']} |")
table = "\n".join(rows)

body = """# 2026-10-26-2009zhaonong-units-batch-i 收口

## 一、范围与目标

- 来源：赵农《中国艺术设计史》（高等教育出版社，2009），`doc_id: 2009-zhaonong-zhongguo-yishu-shejishi`。
- 范围：第九章「专制的文化——明清时期的设计」第一至第二节 L6599–L6833，共 235 行；第一节绪论 L6601–L6652，第二节城市与建筑 L6653–L6833。
- 候选：34 条 unit 候选，全部完成检索、语义裁定、类型化写回与独立复读。
- 目标：把明清政治与工艺文献、火器造船与京张铁路、西学东渐传教士，以及都城、地方城市、寺观、皇家陵园、万里长城五目，转为可追踪的知识元。
- 边界：`03基础书籍-md文档/` 只读；不 commit、不 push；单主线 `main`；图版未视觉核验。

## 二、覆盖与复读

全节逐段阅读，候选按 `payload.source_span.section` 归节，分布与写回如下：

| 节 | 行段 | 候选 | 写回要点 |
|---|---|---|---|
| 第一节 绪论 | L6599–L6652 | 10 | 万里长城、郑和、农政全书、京张铁路、詹天佑、汤若望、南怀仁 7 条新建；紫禁城、工程做法 2 条跨册更新；江南私家园林仅一句总述判 rejected |
| 第二节 城市与建筑 | L6653–L6833 | 24 | 蒯祥、左祖右社、西苑、天坛、先农坛、太和殿、前朝后室、南京城墙、沈阳故宫、武当山道观、金顶铜殿、承德外八庙、明孝陵、明十三陵、长陵棱恩殿、定陵、清西陵、清东陵、山海关、居庸关、八达岭、嘉峪关 22 条新建；中轴线、西安 2 条同册更新 |

独立语义复读对象为全部 33 个写回文件（29 新建 + 4 更新），逐个 dump frontmatter 选键与「描述／核心内容／层级体系中的位置／相关知识元／验证状态」五节，逐条核对候选标题与目标文件标题、维度与 `01-domain/dimension-registry.md` 边界、引文与来源行、图注材料的边界、`hierarchy_scope_note` 与 body `scope_note` 是否同文。复读中未再发现需要改写的条目；此前审计发现的引文体例问题已在生成器源文件修正并重建，见第八节。

三重机械审计（写回与修正后重跑）：

| 审计 | 范围 | 结果 |
|---|---|---|
| `_zn_struct.py` | 33 个写回文件 | `problems: 0` |
| `_zn_audit.py` | 六册合并语料回查 | `findings: 0` |
| `_zn_audit_strict.py` | 仅赵农册、仅 29 个单源新建 | `findings: 0` |

## 三、34 条裁定总表

| # | 实体 | 裁定 | 目标 | 依据摘要 |
|---|---|---|---|---|
@@TABLE@@

## 四、29 条新建分型

按类型：works 16、persons 5、places 5、terms 2、publications 1。按维度：B 25、D 2、E 2；无 A 维度条目（本段不涉史学方法），无 C 维度主维条目。按置信度：medium 22、low 7。

- **works（16）**：万里长城、京张铁路、天坛、先农坛、太和殿、南京城墙、沈阳故宫、武当山道观、武当山金顶铜殿、承德外八庙、明孝陵、明十三陵、长陵棱恩殿、定陵、清西陵、清东陵。
- **persons（5）**：郑和、詹天佑、汤若望、南怀仁、蒯祥。
- **places（5）**：西苑、山海关、居庸关、八达岭长城、嘉峪关。
- **terms（2）**：左祖右社、前朝后室。
- **publications（1）**：《农政全书》。

D 维度 2 条为郑和、先农坛（后者以劝农礼制为主维，坛庙实体归 B）；E 维度 2 条为汤若望、南怀仁，均属清初西学东渐人物。

low 置信度 7 条均为单句或单段提及、缺本体信息的条目（郑和、《农政全书》、汤若望、南怀仁、蒯祥、前朝后室、八达岭长城），已在「匹配质量」逐条写明缺项：郑和只记下西洋的政治意图与宝船威势，无生卒、航行次数与路线；《农政全书》只记保留农具与生产器具资料，无卷数、版本与器目；汤若望、南怀仁只记其与清初历法、铸炮的关联，来源未给生卒与著作；蒯祥只记永乐年间规划营建紫禁城；前朝后室只有一句评价，未给定义与文献出处；八达岭长城只记其为居庸关前哨与游览段。

## 五、4 条更新

| 目标 | 变动 | 结果 |
|---|---|---|
| `works/beijing-zijincheng.md` | 新增赵农 L6687、L6689、L6691、L6693、L6701 source 条 | 跨册：source_count 1→2、version 1→2；补蒯祥规划营建、前三殿与后三宫、9999 间、72 万平方米、御花园与宁寿宫花园、角楼与筒子河、前朝后室 |
| `publications/gongcheng-zuofa.md` | 新增赵农 L6649 source 条 | 跨册：source_count 2→3、version 2→3；补书名异写《大清工部工程作法则例》与清代建筑法典的定位 |
| `terms/central-axis.md` | 赵农 citation 扩至 L1227、L1281、L6668 | 同册多跨度：source_count 1 不变、version 1→2；补明清北京中轴的外城—宫城—北城三段格局 |
| `places/xian.md` | 赵农 citation 扩至 L6745、L6749、L6751、L7811 | 同册多跨度：source_count 1 不变、version 1→2；补隋唐旧城基础、钟鼓楼与十字街、城墙 14 公里与 12 米、箭楼瓮城城门序列、明末关城梢门关厢 |

## 六、no_delta 条

本批无 `no_delta`。34 条候选均给出 create、update 或 rejected；同册已有的紫禁城、工程做法、中轴线、西安均因来源提供新增材料按 update 处理，未以“既有条目已覆盖”结案。

## 七、1 条 rejected

- **绪论一句总述不足立条（1）**：江南私家园林（cand-10-03）在 L6641 只有一句总述，未给园名、造园手法与实例；本章第五节 L7346–L7416 对江南园林有整段展开，并另有候选 cand-11-001，届时按该段立条。本批不另建条，避免同一概念两目；`target_ref` 记 null，材料保留在来源层。

## 八、语义复读修正与原文疑误

### 引文体例修正

首轮审计共报 4 条文件、5 处引文问题，修正写在生成器源文件 `_zn_ch9a_e1.py`，再 purge 重建，未直接改生成物：

- **跨图版行不得逐字引**：武当山金顶铜殿一条，原文“天柱”与“峰”之间跨图版行，改为叙述并注明本条不逐字引。
- **跨图版行不得整句引**：明孝陵一条，原文“宝顶下面为”在 L6794、“地宫”在 L6799，中间隔图版行，拆为“方城明楼是建在方形城门上的城楼。宝顶有圆墙环绕”两句，后半改叙述并注明跨图版行。
- **跨行不得整句引**：居庸关一条，原文“历史”在 L6823 行末、“上有”在 L6828 行首，只引“天下九塞，居庸其一”，并注明本条不整句引。
- **作者判断不得加引号**：西安一条的“文物古迹—明代城墙—地下文物”与“保留旧城老街”均为作者自撰短语，改为不加引号的叙述。

### 原文疑误与内部张力

- 来源 L6815 记明长城“西起嘉峪关，东达山海关，并延伸修筑‘辽东边墙’直至鸭绿江畔”，L6821 又称山海关“位于明长城的东端”。两说并存，万里长城与山海关两条各照所据行著录，不径改；长城东端的确切所指以来源两处表述并列保留。
- 前朝后室一条照录来源用词“前朝后室”，不代人改写为通行的“前朝后寝”，也不补《考工记》或礼制文献出处。
- 西安一条两项“最”（建都时间最长、建立朝代最多）为来源判断，条目照录并标注来源未给建都朝代清单与累计年数。
- 紫禁城一条 9999 间、72 万平方米、角楼“九梁十八柱七十二脊”等数字与俗称均照来源著录，未做实测核对。
- 汤若望、南怀仁在来源中仅随明清历法与铸炮段落提及，条目只登记来源所载，不据他册补生平与著作。
- 图版（第九章第一至第二节各图）未视觉核验；相关条目只录文字所载，不据图补写构图、尺寸与藏地。
- 候选 `source_span` 为块级粗跨度，`candidate_spans_union` 上界 8560 超出本批阅读范围；实际引用行均落在 L6599–L6833 内，章属与节属以 `payload.source_span.section` 与实际引用行为准。
- 候选 ID 前缀 `cand-10-*`、`cand-11-*` 是抽取批次号，不是章号；本章候选跨越两个批次，检索时必须带 `doc_id`。

## 九、状态与下一跳

- 工作包状态：`applied`；决策链 34 条全部落账（create 29、update 4、rejected 1），ledger 101 行、apply-plan 33 行。
- 候选索引：本章本批 34 条全部转 `terminal`；索引总行 5339，applied 2100、rejected 848、no_delta 191、needs_evidence 2200，terminal 3139。
- 生成态：`build_discovery_index.py` 重建后 applied 2100、no_delta 191、rejected 848、needs_evidence 2200，terminal 3139；`build_translation_index.py` 写入 1483 条；`run_sync_closure.py --refresh-generated --full` 通过（250 tests + 16 subtests，structural_health 102/130）。内容质量审查报 12 条，均为本批之外的既有条目（`liezi-tangwen`、`songshi-yufuzhi`、`zhao-nong`、`zhongguo-yishu-shejishi-zhaonong-2009`、`he-zun` 与一条跨类型同名），本批无新增发现。
- 未做：未 commit、未 push；`--check-generated` 在工作树未提交时预期为 `blocked_pending_commit`。
- 未做：本批范围内 7 条 claim 候选仍保持 `needs_evidence`，未进入 claim-registry；本批只处理 unit 候选。
- 下一跳：第九章余下 122 条 unit 候选——第三节商业与民居 30 条、第四节文具与书籍 27 条、第五节园林与瓷器 35 条、第六节服饰与交通 24 条、第七节设计文献 6 条；随后第十章 113 条、总结 9 条，再转 2010 田自秉（404 条）与 2011 李立新（189 条 unit、1,363 条 claim）。
"""

out = body.replace("@@TABLE@@", table)
(PKG / "summary.md").write_text(out, encoding="utf-8", newline="\n")
print("written", len(out.splitlines()), "lines")
