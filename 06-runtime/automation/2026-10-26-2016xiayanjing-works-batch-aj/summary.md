# 批次 AJ 交付摘要 — 2016 册 works

- work package：`06-runtime/automation/2026-10-26-2016xiayanjing-works-batch-aj/`
- 日期：2026-10-26
- 来源：夏燕靖《中国艺术设计史（升级版）》，上海人民美术出版社，2016（`doc_id: 2016-xiayanjing-zhongguo-yishu-shejishi-upgrade`）
- 状态：`applied`

## 一、范围

本批处理 2016 册 works 类 44 个候选（批前全部为 `needs_evidence`）。44 个候选的 `source_span` 并集合并相邻后为 28 段、共 582 行，逐行读过；另因大报恩寺琉璃塔跨段取证，补读 L4479。来源文件 `03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md` 全程只读，未作任何改动。

## 二、裁定汇总与状态变化

| 裁定 | 数量 |
|---|---|
| create | 42 |
| update | 1 |
| no_delta | 1 |
| rejected | 0 |
| 合并 | 0 |
| 合计 | 44 |

候选索引状态变化（43 个候选进入 applied，1 个进入 no_delta）：

| 状态 | 批前 | 批后 |
|---|---|---|
| applied | 1193 | 1236 |
| needs_evidence | 3253 | 3209 |
| no_delta | 81 | 82 |
| rejected | 812 | 812 |
| 合计 | 5339 | 5339 |

生命周期分类：批前 active 3253 / terminal 2086；批后 active 3209 / terminal 2130。索引重建幂等，重建脚本从 ledger 重放状态转移后与写入结果一致。

## 三、新建 42 条

全部位于 `04-knowledge/units/works/`。confidence 分布：medium 25、low 17；维度分布：B 36、C 6；sub_type 34 个取值（porcelain_vessel 6、animation 3、badge 2，其余各 1）。

| # | 文件（slug） | 标题 | sub_type | 维度 | confidence | 位置 |
|---|---|---|---|---|---|---|
| 1 | zhu-bishan-yincha | 朱碧山银槎（龙槎杯） | silver_vessel | B | medium | L3871-L3886 |
| 2 | quanzhou-qingjing-si | 泉州清净寺 | mosque | B | low | L3979-L3999 |
| 3 | liu-guandao-xiaoxia-tujuan | 刘贯道《消夏图卷》 | painting | B | medium | L4048-L4061 |
| 4 | yuan-huoqiang | 元代火铳 | firearm | B | medium | L3849-L3860 |
| 5 | guo-shoujing-jianyi | 郭守敬简仪 | astronomical_instrument | B | medium | L3928-L3951 |
| 6 | sajia-si | 萨迦寺 | monastery | B | medium | L3968-L3992 |
| 7 | sandian-jiaota-fangmianche | 三锭脚踏纺棉车 | spinning_wheel | B | low | L3764 |
| 8 | zhui-hanxin-tu-meiping | 追韩信图梅瓶 | porcelain_vessel | B | low | L3696-L3711 |
| 9 | mengtian-jiangjun-yuhuchun-ping | 蒙恬将军玉壶春瓶 | porcelain_vessel | B | low | L3696-L3714 |
| 10 | wugu-fengdeng-denglongwen-zhijin | 五谷丰登灯笼纹织锦 | brocade | B | low | L4160 |
| 11 | qinghua-wugu-fengdeng-tu-pan | 青花五谷丰登图盘 | porcelain_vessel | B | low | L4163 |
| 12 | dabaoensi-liuli-ta | 大报恩寺琉璃塔 | pagoda | B | medium | L4386-L4402；L4479 |
| 13 | beijing-zijincheng | 北京紫禁城 | palace_complex | B | medium | L4465-L4496 |
| 14 | shizhuzhai-jianpu | 《十竹斋笺谱》 | printed_book | C | medium | L4619-L4656 |
| 15 | yongzheng-fencai-sangnv-pan | 清雍正粉彩仕女采桑图盘 | porcelain_vessel | B | medium | L4427-L4452 |
| 16 | guangxu-caiyou-diaoci-fangping | 清光绪彩釉雕瓷四季花鸟纹方瓶 | porcelain_vessel | B | medium | L4427-L4452 |
| 17 | wangdafan-fugui-shoukao-ciban | 王大凡《富贵寿考瓷板》 | porcelain_plaque | B | low | L4767-L4776 |
| 18 | fanchuan-tujing-cipan | 帆船图景瓷盘 | porcelain_vessel | B | medium | L4427-L4452 |
| 19 | zisha-donglinggua | 紫砂“东陵瓜” | teapot | B | low | L4368-L4385 |
| 20 | jiulongbi | 九龙壁 | glazed_tile_wall | B | low | L4386-L4422 |
| 21 | yuehan-tielu-huizhang | 粤汉铁路徽章 | badge | C | low | L4717-L4730 |
| 22 | beiyang-jiqiju-biaozhi | 北洋机器局标志 | logo | C | low | L4717-L4730 |
| 23 | jiuxi-shibajian | 都锦生丝织风景《九溪十八涧》 | woven_picture | B | medium | L4851-L4868 |
| 24 | sassoon-house | 沙逊大厦 | commercial_building | B | medium | L5057-L5062 |
| 25 | prc-national-flag | 中华人民共和国国旗（五星红旗） | national_symbol | C | medium | L5128-L5146 |
| 26 | flying-pigeon-bicycle | 飞鸽牌自行车 | bicycle | B | medium | L5204-L5275 |
| 27 | jiefang-truck | 解放牌载重卡车 | truck | B | medium | L5319-L5343 |
| 28 | dongfeng-sedan | 东风牌小轿车 | automobile | B | medium | L5319-L5343 |
| 29 | great-wall-tapestry | 大型壁毯《长城》 | tapestry | B | medium | L5346-L5385 |
| 30 | mao-badge | 毛主席像章 | badge | C | medium | L5386-L5400 |
| 31 | minzu-wenhua-gong | 民族文化宫 | public_building | B | low | L5290-L5306 |
| 32 | xique-dengmei | 《喜鹊登梅》大挂屏 | lacquer_screen | B | low | L5175 |
| 33 | chengkun-tielu | 《成昆铁路》象牙雕刻 | ivory_carving | B | medium | L5375-L5377 |
| 34 | daiyuegui | 《戴月归》彩锦绣 | embroidery | B | low | L5420 |
| 35 | baidum | 《白度母》唐卡 | thangka | B | low | L5446 |
| 36 | jinxing-pen | 金星牌金笔 | pen | B | low | L5334 |
| 37 | da-nao-hua-shi | 《大闹画室》 | animation | B | medium | L5480-L5501 |
| 38 | da-nao-tian-gong | 《大闹天宫》 | animation | B | medium | L5480-L5501 |
| 39 | xiao-ke-dou-zhao-ma-ma | 《小蝌蚪找妈妈》 | animation | B | medium | L5480-L5501 |
| 40 | lenovo-et960 | 联想ET960智能手机 | mobile_phone | B | medium | L5452-L5468 |
| 41 | li-ning-banpo-basketball-shoe | 李宁半坡专业篮球鞋 | footwear | B | medium | L5452-L5468 |
| 42 | beijing-olympic-poster-2008 | 2008年北京奥运会海报 | poster | C | low | L5480-L5501 |

low 17 条的判定口径：仅图注一行、仅列名或仅一句描述，而无形制、尺寸、出土或流传信息。medium 条目的形制描述均取自正文文字；所有条目的图版均未视觉核验，已在验证状态内逐条注明。

## 四、更新 1 条

`04-knowledge/units/events/founding-ceremony-tiananmen-decoration-1949.md`：version 1→2。

- 既有内容基于同册 L5557，只记“天安门国庆工程指挥部把城楼装饰设计任务下达给华北军区政治部宣传部”这一层。
- 本批候选 span L5147-L5149 补出：部长张致祥把大红宫灯设计交给该部文工团舞美队；参与者含两位反战日本美工师；先后拿出装饰设计方案与宫灯张挂草图 20 余幅；周恩来选定 8 盏太阳宫灯并修改城楼布局、抹去金水桥栏杆扎满彩球的设计，并留下关于会场气氛的原话。
- 两处合并为同一条 event，不另立新条；`source_count` 按同册口径记 1。更新前指纹 `sha256:14ae5dba…` 取自 HEAD blob，更新后 `sha256:a1b3ff36…`，94 行 / 6638 字节。

## 五、no_delta 1 条

- 候选：`2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-11-39`“上海生态景观大道”。
- 既有 `events/2000-shanghai-eco-landscape-avenue.md` 已完整覆盖候选所抽事实，无新增可核事实。
- 按 `approved → no_delta` 记终态并保留 `target_ref`；既有文件未改写。

## 六、合并说明

本批无合并，`canonical-mapping.json` 的 `merged_candidates` 全部为空。以下近名对象经逐条对账后分立：

- 五谷丰登灯笼纹织锦（织物）与青花五谷丰登图盘（瓷器）：同题材、异媒材，不合并。
- 《大闹画室》《大闹天宫》《小蝌蚪找妈妈》：三部影片各自成条。
- 解放牌载重卡车与东风牌小轿车：同段叙述，不同车型，不合并。
- 北京紫禁城、萨迦寺、泉州清净寺、大报恩寺琉璃塔、九龙壁、沙逊大厦、民族文化宫：按 AI 批次先例作为“建筑作品”写入 works，不改用 places 字段组；与既有 places 城市／遗址条目并立，不据名称相近合并。

## 七、原文讹字、异写与内部张力

一律照录标疑、不改字，完整记录见各条目验证状态与证据范围：

- 紫禁城：图 9-35／9-36 图注与正文不指同一城；图 9-33／9-34 图注文字同行交错。
- 帆船图景瓷盘：图注作 3 鱼，正文作 4 鱼。
- 《十竹斋笺谱》：“短版／饱版”疑为“饾版”，该段六次用“短版”、一处用“饱版”。
- 沙逊大厦：“锥字体”疑指锥形。
- 大报恩寺琉璃塔：“欧州”“传教上”照录；“中国之大古董，永乐之大窑器”系清人称谓，非明人自评。
- 解放牌卡车：“还还参加”照录；Simca Vedetee 照录不改。
- 图 9-5-2 为瓷器图，却置于丝织品种段；图 11-36 与 1978 年展览段并置。
- 2008 年北京奥运会海报：正文段末以（图11-44）回指，但该段讲广告设计信息语意传达的一般过程，未描述海报本身。

## 八、验证

| 项目 | 结果 |
|---|---|
| ledger 行数 / 候选数 | 132 / 44（44×3 步转移） |
| 终态 | applied 43、no_delta 1、rejected 新增 0 |
| apply-plan | 43 行（create 42、update 1） |
| canonical-mapping | 44 条 |
| 指纹校验 | 43/43，错误 0；before 基线 head_blob 1 |
| 引文审计 | 92 处，逐字命中 92；首轮 6 处未命中已改写，另补入周恩来原话 1 处 |
| 内部 KU 链接 | 55 个，缺失 0 |
| YAML / 六节结构 | 43 个文件，错误 0 |
| 内容质量审计 | 1090 个知识元，发现 0 |
| 结构契约健康 | 122/130（traceability 7/15） |
| 知识结构质量 | 55/65（hierarchy_assignment 0） |
| 证据链质量 | 55/55 |
| 仓库审计 | 1090 单元；works 182、places 149、terms 192、institutions 144、procedures 121、persons 119、events 115、publications 68；broken_links 0；重名组 4、已消歧 8、缺失 0；evidence_ref 1090/1090 |
| 关系审计 | broken_target 0、invalid_relation_type 0、missing_inverse 0、weak_evidence 0、isolated 1090、relation_index_total 0、覆盖 0/67 |
| 规则漂移 | 0 |
| 空白/编码检查 | pass |
| Skill 注册表 | 18 个，18 leaf，0 router |
| 知识图谱 | 节点 1090、边 0 |
| pytest | 250 passed，16 subtests passed，0 失败 |
| 治理 backlog | system_p0/p1/p2 = 0/0/0；research_debt 5；candidate_opportunities 2 |
| 生成态闭合 | 18/18 通过；`--check-generated` 因未提交变更记 `blocked_pending_commit` |

## 九、遗留与研究债务

- 关系候选 dry run 报出 3 条 `s7_name_overlap` 机械信号。全库 `name_en` 重复仅 4 组，均为既有条目：`han feizi`、`xunzi`、`zhuangzi` 的 person/publication 配对，以及 `calendering` 对应 `procedures/chuai-ran.md` 与 `procedures/nian-ya.md`。本批 42 条新建未引入新的同名，3 条信号与本批无关，留作后续关系治理输入，不据此自动建关系。
- 全库仍为 `consensus: tentative`、`evidence_status: source_backed`；单源单元 511、low confidence 115、隔离单元 1090、`relation_index_total` 0。这些是既有的成熟度与关系债务，不是本批可解。
- 层级挂载仍为 0/1090，`hierarchy_assignment` 0 分；属既有层级工程缺口。
- `needs_evidence` 余 3209 个候选（claim 1363、unit 1846），是本阶段后续批次的主要工作面。
- 本批未执行 `git commit`／`push`；工作树相对 HEAD `74f6596` 的变更留待明确授权后处理。
