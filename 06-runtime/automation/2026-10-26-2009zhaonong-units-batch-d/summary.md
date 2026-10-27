# 2009 赵农《中国艺术设计史》— 第四章 unit 批次（batch-d）

- 工作包：`2026-10-26-2009zhaonong-units-batch-d`
- 来源（只读）：`03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md`
- doc_id：`2009-zhaonong-zhongguo-yishu-shejishi`
- 日期：2026-10-26
- 候选范围：第四章 L2479-L5385 内的 79 条 unit 候选（`cand-04-*` 与 `cand-05-*` 混编，章节归属以 `payload.source_span.chapter` 为准）
- 结果：create 64、update 6（6 个文件）、rejected 9、no_delta 0
- 语义验收：Agent 逐条复读全部 79 条候选，并独立复读 64 个新建条目与 6 个更新条目；未使用外部平台

## 一、裁定汇总

| 候选 | 实体 | 动作 | 目标 |
|---|---|---|---|
| cand-04-40 | 秦始皇 | create | `persons/qin-shi-huang.md` |
| cand-04-42 | 汉武帝 | create | `persons/han-wu-di.md` |
| cand-04-43 | 董仲舒 | create | `persons/dong-zhong-shu.md` |
| cand-04-45 | 司马迁 | create | `persons/si-ma-qian.md` |
| cand-04-47 | 班固 | create | `persons/ban-gu.md` |
| cand-04-49 | 许慎 | create | `persons/xu-shen.md` |
| cand-04-52 | 李斯 | create | `persons/li-si.md` |
| cand-04-53 | 蔡伦 | create | `persons/cai-lun.md` |
| cand-04-71 | 钟繇 | create | `persons/zhong-yao.md` |
| cand-04-141 | 程邈 | create | `persons/cheng-miao.md` |
| cand-04-75 | 王莽 | create | `persons/wang-mang.md` |
| cand-04-82 | 张骞 | create | `persons/zhang-qian.md` |
| cand-04-83 | 班超 | create | `persons/ban-chao.md` |
| cand-04-87 | 史禄 | create | `persons/shi-lu.md` |
| cand-04-143 | 萧何 | create | `persons/xiao-he.md` |
| cand-04-122 | 蒙恬 | create | `persons/meng-tian.md` |
| cand-04-127 | 霍去病 | create | `persons/huo-qu-bing.md` |
| cand-04-48 | 汉书 | create | `publications/han-shu.md` |
| cand-04-51 | 论衡 | create | `publications/lun-heng.md` |
| cand-04-119 | 《阿房宫赋》 | create | `publications/efang-palace-fu.md` |
| cand-05-18 | 《西京杂记》 | create | `publications/xijing-zaji.md` |
| cand-04-64 | 石鼓文 | create | `works/shi-gu-wen.md` |
| cand-04-65 | 商鞅方升 | create | `works/shang-yang-fang-sheng.md` |
| cand-04-67 | 睡虎地秦简 | create | `works/shuihudi-qin-bamboo-slips.md` |
| cand-04-69 | 居延汉简 | create | `works/juyan-han-slips.md` |
| cand-04-72 | 宣示表 | create | `works/xuan-shi-biao.md` |
| cand-04-77 | 秦驰道 | create | `works/qin-chi-dao.md` |
| cand-04-85 | 褒斜道 | create | `works/baoxie-road.md` |
| cand-04-86 | 灵渠 | create | `works/ling-qu.md` |
| cand-04-88 | 渭水三桥 | create | `works/weishui-three-bridges.md` |
| cand-04-89 | 灞桥 | create | `works/ba-bridge.md` |
| cand-04-103 | 风车 | create | `works/winnowing-machine.md` |
| cand-04-109 | 咸阳宫 | create | `works/xianyang-palace.md` |
| cand-04-110 | 未央宫 | create | `works/weiyang-palace.md` |
| cand-04-114 | 嵩山三阙 | create | `works/songshan-three-que.md` |
| cand-04-118 | 阿房宫 | create | `works/epang-palace.md` |
| cand-04-121 | 长城 | create | `works/qin-han-changcheng.md` |
| cand-04-126 | 马踏匈奴 | create | `works/horse-treading-xiongnu.md` |
| cand-05-30 | 马王堆帛地图 | create | `works/mawangdui-boditu.md` |
| cand-04-56 | 浑天说 | create | `terms/huntian-theory.md` |
| cand-04-57 | 四神 | create | `terms/si-shen.md` |
| cand-04-60 | 秦半两 | create | `terms/qin-ban-liang.md` |
| cand-04-61 | 汉五铢 | create | `terms/han-wu-zhu.md` |
| cand-04-66 | 隶书 | create | `terms/li-shu.md` |
| cand-04-68 | 章草 | create | `terms/zhang-cao.md` |
| cand-04-70 | 楷书 | create | `terms/kai-shu.md` |
| cand-04-74 | 金错刀 | create | `terms/jin-cuo-dao.md` |
| cand-04-142 | 马蹄金 | create | `terms/han-dai-jin-bi.md` |
| cand-04-78 | 车同轨 | create | `terms/che-tong-gui.md` |
| cand-04-84 | 栈道 | create | `terms/zhan-dao.md` |
| cand-04-97 | 环首刀 | create | `terms/huan-shou-dao.md` |
| cand-04-98 | 钩镶 | create | `terms/gou-xiang.md` |
| cand-04-99 | 汉代铠甲 | create | `terms/han-armor.md` |
| cand-04-100 | 耦犁 | create | `terms/ou-li.md` |
| cand-04-106 | 秦权 | create | `terms/qin-quan.md` |
| cand-04-107 | 秦量 | create | `terms/qin-liang.md` |
| cand-04-113 | 门阙 | create | `terms/men-que.md` |
| cand-04-123 | 烽燧 | create | `terms/feng-sui.md` |
| cand-05-02 | 覆斗形封土（方中） | create | `terms/fudou-xing-fengtu-fangzhong.md` |
| cand-05-09 | 汉代冠制 | create | `terms/handai-guanzhi.md` |
| cand-05-107 | 禅衣 | create | `terms/chanyi.md` |
| cand-05-108 | 履的种类 | create | `terms/lv-de-zhonglei.md` |
| cand-05-27 | 司南 | create | `terms/sinan.md` |
| cand-05-33 | 动物形灯与树形灯 | create | `terms/dongwuxing-dengju.md` |
| cand-04-80 | 汉代车制 | update | `terms/shuang-yuan-che.md` |
| cand-04-96 | 弩机 | update | `terms/nu-crossbow.md` |
| cand-04-105 | 石磨 | update | `terms/shi-mo.md` |
| cand-05-106 | 起绒锦 | update | `terms/rongquan-jin.md` |
| cand-04-115 | 武氏祠阙 | update | `places/wushi-ci.md` |
| cand-04-125 | 霍去病墓石刻 | update | `places/huoqubing-mu.md` |
| cand-04-155 | 麟趾金 | rejected | `terms/han-dai-jin-bi.md` |
| cand-04-156 | 金五铢 | rejected | `terms/han-dai-jin-bi.md` |
| cand-04-92 | 秦俑坑青铜剑 | rejected | `procedures/chromate-oxidation-treatment.md` |
| cand-04-144 | 卫青 | rejected | `persons/huo-qu-bing.md` |
| cand-05-10 | 秦始皇兵马俑 | rejected | `works/qin-bing-ma-yong.md` |
| cand-05-13 | 透光镜（魔光镜） | rejected | `terms/touguang-jing.md` |
| cand-05-17 | 卧褥香炉（被中香炉） | rejected | `persons/ding-huan.md` |
| cand-05-25 | 地动仪（候风地动仪） | rejected | `works/houfeng-dizhenyi.md` |
| cand-05-21 | 蔡侯纸 | rejected | `procedures/zaozhishu.md` |

## 二、新建 64 条

### 分类构成

- person：17 条（秦始皇、汉武帝、董仲舒、司马迁、班固、许慎、李斯、蔡伦、钟繇、程邈、王莽、张骞、班超、史禄、萧何、蒙恬、霍去病）
- works：18 条（石鼓文、商鞅方升、睡虎地秦简、居延汉简、宣示表、秦驰道、褒斜道、灵渠、渭水三桥、灞桥、风车、咸阳宫、未央宫、嵩山三阙、阿房宫、长城、马踏匈奴、马王堆帛地图）
- terms：25 条（浑天说、四神、秦半两、汉五铢、隶书、章草、楷书、金错刀、汉代金币、车同轨、栈道、环首刀、钩镶、汉代铠甲、耦犁、秦权、秦量、门阙、烽燧、覆斗形封土、汉代冠制、禅衣、履的种类、司南、动物形灯与树形灯）
- publication：4 条（《汉书》《论衡》《阿房宫赋》《西京杂记》）

### 置信度

- medium：44 条
- low：20 条（董仲舒、班固、钟繇、程邈、班超、石鼓文、睡虎地秦简、居延汉简、宣示表、嵩山三阙、禅衣、履的种类、动物形灯与树形灯等以一句或一段为主的条目）

### 字段约定

- 全部 `consensus: tentative`、`evidence_status: source_backed`、`source_count: 1`、`version: 1`、`created = updated = last_verified = 2026-10-26`、`review_due: 2027-04-26`。
- 六节齐全；正文 ASCII 双引号 0；逐字引文用“”，校正字形、拼接句与概括用「」。
- `works/songshan-three-que.md` 的 `sub_type` 统一为 `stone_architecture`，与既有 `works/gao-yi-que.md` 一致。

## 三、更新 6 条

| 候选 | 实体 | 文件 | 版本 | source_count | 要点 |
|---|---|---|---|---|---|
| cand-04-80 | 汉代车制 | `terms/shuang-yuan-che.md` | v1→v2 | 1→2 | 并入赵农 L2680-L2682 的金根车、轩车、轺车、辎车与东汉牛车；两册对双辕车起始时间的表述并存，不裁决 |
| cand-04-96 | 弩机 | `terms/nu-crossbow.md` | v1→v2 | 1→1 | 同书 L2769 秦汉弩机、秦俑坑铜弩机与汉代刻度；刻度不写作现代瞄准具 |
| cand-04-105 | 石磨 | `terms/shi-mo.md` | v1→v2 | 1→1 | 同书 L1986、L2809 汉代石磨与小麦；只两句，证据边界已收紧 |
| cand-05-106 | 起绒锦 | `terms/rongquan-jin.md` | v1→v2 | 1→2 | 并入赵农 L3042 起绒锦、素纱禅衣数据；两册“绒圈锦／起绒锦”未裁决是否同物 |
| cand-04-115 | 武氏祠阙 | `places/wushi-ci.md` | v1→v2 | 1→2 | 并入赵农 L2881 陵墓性门阙定位；两册对象分别为石祠画像与祠前门阙，不合表 |
| cand-04-125 | 霍去病墓石刻 | `places/huoqubing-mu.md` | v1→v2 | 1→2 | 并入赵农 L2971-L2986 陵墓环境、封土模拟祁连山与《马踏匈奴》；两册石刻清单（十类／约16件）并存 |

## 四、rejected 9 条

| 候选 | 实体 | 指向 | 理由 |
|---|---|---|---|
| cand-04-155 | 麟趾金 | `terms/han-dai-jin-bi.md` | 与 cand-04-142 马蹄金同一来源句，已合并为“汉代金币”一条，不再单独建 KU |
| cand-04-156 | 金五铢 | `terms/han-dai-jin-bi.md` | 同上，作为别名并入“汉代金币” |
| cand-04-92 | 秦俑坑青铜剑 | `procedures/chromate-oxidation-treatment.md` | 铬盐氧化处理已有既有条目，本候选为其器物例证，不另建 |
| cand-04-144 | 卫青 | `persons/huo-qu-bing.md` | 来源只在卫青、霍去病并称句中提及，无独立材料 |
| cand-05-10 | 秦始皇兵马俑 | `works/qin-bing-ma-yong.md` | 既有条目已存在，本候选材料并入该条 |
| cand-05-13 | 透光镜（魔光镜） | `terms/touguang-jing.md` | 既有条目已存在，不重复建 |
| cand-05-17 | 卧褥香炉（被中香炉） | `persons/ding-huan.md` | 既有丁缓条目已承载，不另建器物条 |
| cand-05-25 | 地动仪（候风地动仪） | `works/houfeng-dizhenyi.md` | 既有条目已存在 |
| cand-05-21 | 蔡侯纸 | `procedures/zaozhishu.md` | 既有造纸术条目已承载蔡侯纸，不重复建 |

## 五、原文错字与内部不一致

- **单位疑误**：L2829“一升相当于今200毫克”，同句一斤250克、一尺23厘米均合常规，“毫克”当为「毫升」，照录标疑（qin-quan、qin-liang、qin-shi-huang 均已标）。
- **形近之误**：L2831“平斗桶度量文章”通行《史记·李斯列传》作“平斗斛”，照录标疑（li-si）。
- **形近之误**：L2833“权者，铢、量、斤、钧、石也”，与同段“24铢等于一两”不合，“量”疑为「两」，照录标疑（han-shu）。
- **篇名差异**：来源两处作《汉书·武帝本纪》，通行作《武帝纪》，照录标疑（han-shu、han-wu-di）。
- **用字之误**：L3054“文官带进贤冠”疑为「戴」；L2926“以筑板夯土技术构建”疑为「板筑夯土」之倒；L3136“功莫大于焉”疑为「功莫大焉」；L2605“修定的”疑为「修订」、“未定的之意”疑衍一「的」。均照录标疑。
- **引文异文**：L2488“秦皇扫六合”（通行“秦王扫六合”）、L2490“为我独尊”（通行“唯我独尊”）、L2515“千古之绝唱”（通行鲁迅语“史家之绝唱”）、L3027“衣服旌旌节旗”（通行“衣服旄旌节旗”）、L2860“表峣阕与阊阖”（疑「阕」为「阙」）、L2895“周弛为阁道”（疑「周驰」）、L2852“极竞人间盛景”与 L2903“困困焉”“矗不知乎”等异文，均照录未改。
- **内部矛盾**：L2727 先称渭水三桥含东、西、中三座，又称汉代增修东西两桥，秦代是否已有东西两桥未明，weishui-three-bridges 不把三桥全部定为秦建。
- **表述存疑**：L2819“依样秦国时的度量衡标准”表述滞涩，疑有脱字，shang-yang-fang-sheng 未直引该句。
- **未采异文**：L2922“东入辽东（今朝鲜平壤附近）”括注地理位置可疑，qin-han-changcheng 照录来源原句但不据此另作地理判断。

## 六、图注与证据边界

- L2825-L2827“图 4-32 铁犁”图版与秦权无关，qin-quan 只记为本条行段内的无关图注，未视觉核验。
- L2897-L2901“图 4-37 汉彩绘车马纹铜镜”“图 4-38 汉画像石《牛耕图》”与阿房宫无直接关系，epang-palace 未据图补写。
- L2919-L2920“图 4-39 汉骑马俑”与长城段相邻，qin-han-changcheng 未据图补写。
- L3001-L3002“图 4-47 汉 九子奁漆具”插在封土段中，fudou-xing-fengtu-fangzhong 标为无关图注。
- L3134“图 4-57 铜车马”插在造纸段中，cai-lun 记其与上下文不连贯，是否为版面错置存疑。
- L3183 正文被“图 4-62 汉漆具”图注截断，mawangdui-boditu 按「」拼合并标出图注位置。
- L2978“图 4-45 汉 霍去病墓石刻马踏匈奴”仅作图注信息记录，huo-qu-bing 与 horse-treading-xiongnu 均未据图补写石刻尺寸、石质与形象细节。
- 所有新建与更新条目均声明图版未作视觉核验，不据图补形制、纹样与尺寸。

## 七、引文审计与独立复核

- 结构检查：`_zn_struct.py _zn_ch4_creates.txt` → `problems: 0`（六节、frontmatter 必需字段、正文 ASCII 双引号、反引号 KU 链接、日期与版本）。
- 六册合并语料引文回查：`_zn_audit.py @_zn_ch4_creates.txt` → `findings: 0`。
- 赵农册严格回查：`_zn_audit_strict.py @_zn_ch4_creates.txt` → `findings: 0`。
- 内部链接：64 个新建条目中的全部反引号 KU 路径均可解析，缺失 0。
- 独立复读：17 个 person、18 个 work、25 个 term、4 个 publication 均由 Agent 逐条复读；复读中修正 `songshan-three-que` 的 `sub_type`、补入 `meng-tian` 的 L2659 跨页续句、清理条目正文中的批次规格用语、补齐 `epang-palace` 的异文标注。
- 图版：全部未做视觉核验；依赖图版的形制、纹样与尺寸一律留空。

## 八、跨度说明

- 第四章候选来自两个切块器，编号混有 `cand-04-*` 与 `cand-05-*`；本包按 `payload.source_span.chapter` 归入第四章，不按编号前缀另立批次。
- 来源跨度 L2479-L5385 共 2907 行，覆盖第四章全部候选所在行段；同书多跨度更新在单条 `sources.citation` 内以逗号分隔行号，`source_count` 不增。
- 跨册更新（shuang-yuan-che、rongquan-jin、wushi-ci、huoqubing-mu）各新增一条来源，`source_count` 由 1 增至 2，`version` 加 1，`updated` 与 `review_due` 同步顺延。

## 九、状态与下一跳

- 候选状态变化：`needs_evidence` 2681 → 2602；`applied` 1679 → 1749；`rejected` 813 → 822；`no_delta` 166 不变；总数 5339 不变。
- 生成态：`scripts/build_discovery_index.py` 重建候选索引；`scripts/build_translation_index.py` 重建翻译索引（1161 条）；`scripts/run_sync_closure.py --refresh-generated --full` 全部通过（250 tests, 16 subtests）。
- `--check-generated`：因工作树尚未提交，`check generated snapshots` 按预期失败，记为 `blocked_pending_commit`；提交后重跑可闭合。
- 未提交、未推送：`commit`、`push` 等外部状态变更须由用户当次明确授权。
- 下一跳：赵农册第五章 unit 候选（88 条），随后第六章 91、第七章 126、第八章 63、第九章 156、第十章 113、总结 9 条。
