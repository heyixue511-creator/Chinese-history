# 2010 册 units 批次 T7（六朝）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-26-2010tianzibing-units-batch-t7/`
- 来源：田自秉《中国工艺美术史（修订本）》（2010），doc_id `2010-tianzibing-zhongguo-gongyi-meishushi`
- 候选范围：2010 册第七章六朝（L2713-L3015）的 unit 候选 23 条（cand-07-44 至 cand-08-22 之间的 needs_evidence 项，含 cand-08-100、cand-08-101）
- 裁定结果：新建 18 条、更新 0 条、no_delta 5 条、rejected 0 条
- 状态：applied（23 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 主复读区间：第七章六朝（L2713-L3015），含陶瓷、染织、金属工艺、漆器、其他工艺与结语。
- 截断点：L2712 为汉代末，L3015 为六朝末，L3016 起隋唐归 T8；本批不把隋唐候选提前纳入。
- 本批候选的 source span 并集经工作包计算为 60 行，见 `manifest.json.inputs.source.candidate_spans_union`。
- 插图 1-①、2、4、11、12、13、14 只读图注，未视觉核验。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-07-44 | 六朝工匠制度（百工、番役、纳资代役） | create | `terms/liuchao-gongjiang-zhidu.md` |
| cand-07-55 | 潘岳 | no_delta | `terms/piao-ci.md` |
| cand-07-50 | 杜毓 | no_delta | `places/ou-kiln.md` |
| cand-07-56 | 盘口壶 | create | `terms/pan-kou-hu.md` |
| cand-07-59 | 黄釉瓷扁壶 | create | `works/huangyou-ci-bianhu.md` |
| cand-07-60 | 魂瓶 | create | `terms/hunping.md` |
| cand-07-63 | 莲花纹 | create | `terms/lianhua-wen.md` |
| cand-07-66 | 邓县画象砖 | no_delta | `places/dengxian-xuezhuang-huaxiangzhuan-mu.md` |
| cand-07-67 | 竹林七贤和荣启期砖画 | create | `works/zhulin-qixian-rongqiqi-zhuanhua.md` |
| cand-08-04 | 橦华布 | create | `terms/tonghua-bu.md` |
| cand-08-05 | 苏氏（窦滔妻） | create | `persons/su-shi-qianqin.md` |
| cand-08-08 | 鸟兽纹绮（晋） | create | `works/niaoshou-wen-qi.md` |
| cand-08-09 | 敦煌莫高窟125～126窟北魏刺绣 | create | `works/dunhuang-125-126-ku-xiu.md` |
| cand-08-11 | 六朝铜镜 | create | `terms/liuchao-tongjing.md` |
| cand-08-14 | 戴逵 | create | `persons/dai-kui.md` |
| cand-08-15 | 南京瓦棺寺夹纻佛像 | create | `works/waguan-si-jiazhu-foxiang.md` |
| cand-08-16 | 斑漆 | create | `terms/ban-qi.md` |
| cand-08-17 | 绿沉漆 | create | `terms/lvchen-qi.md` |
| cand-08-18 | 北魏木板漆画 | create | `works/beiwei-muban-qihua.md` |
| cand-08-20 | 南京肖景墓前石柱 | create | `works/xiao-jing-mu-shizhu.md` |
| cand-08-100 | 伎乐人物龙纹石雕（六朝） | no_delta | `terms/tangcao-wen.md` |
| cand-08-101 | 玻璃碗（北燕） | no_delta | `terms/liuli.md` |
| cand-08-22 | 网纹玻璃杯 | create | `works/wangwen-boli-bei.md` |

## 4. 新建 18 条

**制度（1）**：六朝工匠制度。

**陶瓷（4）**：盘口壶、黄釉瓷扁壶、魂瓶、莲花纹（纹样，陶瓷为主要载体）。

**砖画与染织（5）**：竹林七贤和荣启期砖画、橦华布、鸟兽纹绮、敦煌莫高窟125～126窟北魏刺绣、六朝铜镜（金属工艺）。

**人物（2）**：苏氏（窦滔妻）、戴逵。

**漆器与石雕（5）**：瓦棺寺夹纻佛像、斑漆、绿沉漆、北魏木板漆画、肖景墓石柱。

**玻璃（1）**：网纹玻璃杯。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，日期 created/updated/last_verified 为 2026-10-26、review_due 为 2027-04-26，`academic_translation_status` / `translation_status` 均为 provisional。confidence：苏氏为 low（来源仅一句且无生平），其余为 medium。

## 5. 语义判断与内部张力

1. **工匠制度只到六朝一段**：`terms/gong-zu-tu.md` 记汉代工、卒、徒三分与工巧奴，本条记三国百工独立户籍、东晋番役、南朝纳资代役，两条各管一段，不互相覆盖，也不把“独立和自由”外推为完全脱离官府控制。
2. **盘口壶与天鸡壶分工**：天鸡壶条已记“在盘口壶基础上”加鸡头与把手，但不承担祖型形制；本条只记盘口壶的鼓腹、细颈、盘形口、肩系与平底，二者互指而不合并。
3. **黄釉瓷扁壶的“中外交流”是来源判断**：来源由舞乐浮雕人物与莲花舞推出中外文化艺术交流，未给乐舞来源地；条目照录判断，不补粟特、西域等外部结论。
4. **魂瓶三名并列**：魂亭、神亭、谷仓三名同出 L2817，来源未辨三者使用场合；条目并列，不把“谷仓”当作储存功能的证据。
5. **莲花纹反印度说保留论辩层次**：来源先说“有人认为莲花在六朝时期因佛教的发展而从印度传来”，再称“这说法是不确切的”；条目先录本土传统与早期实物，再录反驳，不把反驳写成已证结论。
6. **竹林七贤砖画与七贤群体条分工**：`terms/zhu-lin-qi-xian.md` 记群体思想与文学史评价，且明言未列全七人；本条记三处发现地、八人、神态、题材转变与 200 多块砖的规模，不重复群体评价。
7. **砖画“200多块”不换算画面单元**：来源只给拼合砖数，未给每砖画面分配、尺寸与三墓差异；条目照录总数，不推每砖一人的对应关系。
8. **橦华布的棉布判断归田自秉**：刘逵注只说“其花柔毳，可绩为布”，未用“棉”字；条目把“实际上这是一种棉布”标为来源判断，不据此判草棉或木棉。
9. **苏氏 slug 加时代限定**：`persons/su-shi.md` 已为宋代苏轼，同名异物。本条采用 `persons/su-shi-qianqin.md`，不修改苏轼条，也不把苏氏补名为苏蕙；回文锦不另立作品条。
10. **鸟兽纹绮的总述与本件分开**：L2922 的波状骨架、几何分割线是对六朝丝织的“主要的艺术特点”总述，不专属图注所指的晋代鸟兽纹绮；条目把总述单列，避免把时代特征写成单件特征。
11. **敦煌刺绣与《拾遗记》“针绝”分开**：L2929 为文献传闻，L2931 为有出土地点的北魏实物；条目只在前者作背景，不用文献证明实物，也不用实物反证文献。
12. **六朝铜镜与伍子胥画像镜分工**：`works/wu-zixu-huaxiang-jing.md` 已据 L2947、L2949 立条并记五名人物与历史本事；本条只记三类镜、绍兴浮雕与工匠纪年，不重复单器图像。
13. **戴逵与瓦棺寺佛像分工**：人物条记身份、专长与作品归属，作品条记五躯、三绝并称、夹纻作法与行像背景；`procedures/jiazhu-tai.md` 记工序，三者互指不重复。
14. **斑漆与犀皮先后照来源**：`terms/xipi.md` 称犀皮“实为六朝斑漆的发展”；本条只记斑漆本身，不替来源裁决二者年代先后，也不把无遗物的斑漆与有实物的犀皮等同。
15. **绿沉漆人名书名照录**：来源作“御史中丞刘桢”与《书经》，与常见史料用字不一致；条目照录并标存疑，不代改，也不据外部知识更正。
16. **肖景从来源字形**：候选标题作“萧景”，来源原文作“肖景”；条目从来源作肖景，不另立萧景别名，避免在无来源支持时统一字形。
17. **图注类候选记 no_delta**：插图13“伎乐人物龙纹石雕(六朝)”与插图14“玻璃碗(北燕)”均只有品名与朝代，无尺寸、出土地、技法与图像细节；前者所在段落已由 `terms/tangcao-wen.md` 承担卷草纹，后者的冯素弗墓五件组数据由本批 `works/wangwen-boli-bei.md` 承载，故不另立空条。
18. **网纹玻璃杯的外来说之辨**：来源以景县、定县、北票、南京四批出土反驳“古玻璃都来自西方”，并给铜器漆器瓷器大量生产与玻璃质地未过关两条原因；条目照录论证，不把“国内已制造”扩大为“全部自产”。

## 6. 生成态与门禁

- 结构审计：`_zn_struct.py` 对 18 个新建文件，0 问题（13 个 frontmatter 字段、六节正文、ASCII 引号、悬空反引号链接、日期与状态字段均通过）。
- 引文审计：`_zn_checklines_t7.py` 覆盖 18 个新建条目，142 处双引号逐字引文与田自秉 2010 册源文去标点比对，0 遗漏、0 越界、0 行号错配。
- 全库引文审计：`_zn_audit.py` 对 18 个文件报 0 条发现。
- 索引重建：`build_discovery_index.py` 后 total 5339 不变；applied 2480→2498、needs_evidence 1795→1772、rejected 852 不变、no_delta 212→217；terminal 3544→3567、active 1795→1772。`build_translation_index.py` 后 translation index 1846 条；知识元 2238 条（T6 后 2220，+18 新建）。
- 工作包：apply-plan 18 行（18 create）、candidate-decision-ledger 69 行（23×3）、canonical-mapping 23 条、manifest 1 份。工作包在 candidate-index 写回前构建，`counts_before` 与 `sha256_before` 为写回前真实值（needs_evidence 1795、applied 2480、rejected 852、no_delta 212，rows 5339）。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18 步全部通过（250 tests passed, 16 subtests passed）。
- `python scripts/run_sync_closure.py --refresh-generated --check-generated`：实测 [17/17] check generated snapshots FAILED exit=1，因本批与既有未提交知识元、生成态快照未提交，记 `blocked_pending_commit`，属设计行为。

## 7. 跨批修正

- `_zn_t7_e1.py` 的 `huangyou-ci-bianhu` 关联原写 `places/anyang.md`，该条不存在，删除该链接。
- `_zn_t7_e1.py` 的 `hunping` 关联原写 `terms/wulian-guan.md`，该条不存在，删除该链接，五联罐只在正文叙述。
- `lianhua-wen` 描述原把自撰压缩语“六朝因佛教从印度传来”加引号，全库引文审计判 MISS，去引号改为“莲花纹因佛教在六朝自印度传来的说法”。
- `liuchao-tongjing` 证据边界原引“早期草略、晚期精美”为压缩语，去引号改为“早晚工艺差异的描述”。
- `waguan-si-jiazhu-foxiang` 证据边界原引“轻便坚固”为压缩语，去引号改为“轻便坚固的比较”。
- `wangwen-boli-bei` 描述原引“我国古代玻璃器都来自西方”为压缩语，去引号改为“我国古代玻璃器都来自西方的看法”。
- 候选 `cand-08-100`（伎乐人物龙纹石雕）原计划 no_delta 指向 `terms/rendong-wen.md`；复核后改指 `terms/tangcao-wen.md`，因图注所在 L2992 段落主题为卷草纹而非忍冬纹。

## 8. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- 2010 册 unit 候选剩余 225 条（304−32−29−18）；claim 候选 278 条未启动。
- 六朝百工人数、番役年限、纳资数额与南北差异未载。
- 盘口壶的高度、口径、腹径、型式分期与窑口归属未载；黄釉瓷扁壶的尺寸、墓号、藏地与胎质未载。
- 魂瓶的高度、腹径、墓葬、窑口与纪年未载；莲花纹的单元尺寸、瓣数与配色未载。
- 竹林七贤砖画的尺寸、三墓墓主、画面分配与藏地未载；200 多块为来源计数。
- 橦华布的幅宽、产量、棉种与织法未载；苏氏的名字、生卒、籍贯与回文锦尺寸、字数、存佚未载。
- 鸟兽纹绮的尺寸、组织、经纬密度、墓号与藏地未载；敦煌刺绣的尺寸、片数、藏地与出土编号未载。
- 六朝铜镜的直径、重量、镜背布局、合金配比与藏地未载。
- 戴逵的生卒、籍贯、师承与其他作品未载；瓦棺寺五躯的尺寸、形制、胎层、漆色与存佚未载。
- 斑漆的胎体、器形、色料与工序未载（无遗物）；绿沉漆的色料成分、调色配方与实物未载。
- 北魏木板漆画的数量、尺寸、板厚、墓号、墓主与藏地未载；肖景墓石柱的高度、柱径、棱数、材质与保存状况未载。
- 网纹玻璃杯的壁厚、重量、成分分析与成型工艺未载；插图14 为北燕玻璃碗，非本杯。
- 图版插图 1、2、4、11、12、13、14 未视觉核验。
- Book 7 及以后不启动（用户范围限定）。
