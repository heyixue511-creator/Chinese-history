# 批次 AS — 2009 册 unit 候选 24 条

- **工作包**: `2026-10-26-2009xiayanjing-units-batch-as`
- **日期**: 2026-10-26
- **状态**: applied
- **来源**: 夏燕靖《中国设计史》（上海人民美术出版社，2009）
- **范围**: `2009-xiayanjing-zhongguo-shejishi` 剩余 unit 候选中的前 24 条，`cand-03-103` 至 `cand-05-86`
- **裁定**: 新建 11、更新 1、no_delta 12

## 一、覆盖与基线

- 候选索引基线：5,339 行；AS 前状态为 applied 1,467、no_delta 128、needs_evidence 2,932、rejected 812。
- 本批登记 24 条候选、24 个 source spans，跨度并集 **262 行**；scope 由各候选 span 的并集逐行覆盖，候选之间的空档不计为已读。来源文件只读，未改写、未删除。
- 候选 span 按候选登记顺序写入 `manifest.json`，同一段落在不同候选间允许重复；并集范围为 L1811-L1826、L1831-L1834、L1837-L1866、L1869-L1874、L1891-L1908、L2052-L2064、L2150-L2161、L2232-L2260、L2615-L2630、L2674-L2688、L2796-L2815、L2855-L2862、L2988-L2994、L3003-L3009、L3095-L3098、L3159-L3175、L3424-L3427、L3492-L3503、L3593-L3616。
- 判重检索覆盖 `04-knowledge/units/` 下既有 KU 的标题、正文与全文命中；候选 `payload.knowledge_match` 原记录为“知识库当前为 0 KU”的早期占位，AS 以当前 checkout 的实际语义复读为准，不沿用占位判断。

## 二、新建 11 条

| 候选 | 实体 | 源跨度 | 目标 | 主要新增内容 |
|---|---|---|---|---|
| cand-03-103 | 拍竿 | L1891-L1896 | `terms/pai-gan.md` | 南朝大战船巨型击船装置；数十尺巨木悬石，敌船迫近时发木击毁；同段船名与图 5-22 边界 |
| cand-03-106 | 谢灵运木屐 | L1897-L1908 | `works/xie-ling-yun-mu-ji.md` | 东晋谢灵运制木底鞋，前后活齿，用于登山；同段家具背景；图 5-23 实为床 |
| cand-03-88 | 帔子 | L1811-L1826 | `terms/pei-zi.md` | “披之肩背”的长巾；比披帛更艳丽、有绣纹；晋朝贵族兴，后世尊卑通用；北方男式衲裆女子也用 |
| cand-03-91 | 羊肠裙（百褶裙） | L1831-L1834 | `terms/yang-chang-qun.md` | 百褶裙为西北民族女服，汉末传入，魏晋贵族视为时髦；窄瘦皱褶卷曲；段前“铜镜”标题异常标疑 |
| cand-03-92 | 裥裙 | L1831-L1834 | `terms/jian-qun.md` | 南北朝时兴，多幅，两种以上颜色的纱罗或布帛条片拼成，长裾高腰，色彩华丽 |
| cand-03-94 | 天宫寺释迦立像 | L1837-L1840 | `works/tian-gong-si-shi-jia-li-xiang.md` | 《洛阳伽蓝记》所记洛阳天宫寺立像高 43 尺、用铜 10 万斤、黄金 600 斤；文献转引、无实物 |
| cand-03-95 | 花丝工艺 | L1841-L1857 | `terms/hua-si-gong-yi.md` | 西晋盛行金银细丝盘绕花形；洛阳金村、宜兴、南京栖霞山实物；三国东吴“大吉”花形金饰；“错采镂金” |
| cand-03-97 | 筒袖铠 | L1858-L1866 | `terms/tong-xiu-kai.md` | 晋代鱼鳞或龟背甲片连缀筒形甲身，护肩装筒袖；与衲裆铠、明光铠并列三种基本形制 |
| cand-04-108 | 《开宝藏》 | L2674-L2688 | `publications/kaibao-zang.md` | 北宋开宝四年（971）雕印佛藏；《佛说阿惟越政遮经》卷首扉画继承唐五代形式、雕刻更细致工丽 |
| cand-04-24 | 执壶 | L2052-L2064 | `terms/zhi-hu.md` | 唐代酒壶称执壶或注子；盘口短颈、鼓腹短嘴、曲柄短把；晚唐壶身增高、瓜棱、嘴柄渐长 |
| cand-05-86 | 元代瓷器壶、杯、匜、炉 | L3003-L3009 | `terms/yuan-dai-ciqi-qixing.md` | 四种器形并列的清单级条目；壶加流与把手，杯以高足杯为代表，匜为元代流行造型，炉腹大高耳矮足 |

## 三、更新 1 条

| 候选 | 实体 | 源跨度 | 目标 | 更新内容 |
|---|---|---|---|---|
| cand-05-84 | 紫砂器 | L3593-L3616 | `terms/zisha-tao.md` | 补宜兴窑汉代始烧红陶、灰陶、原始青瓷；紫砂宋始烧、明闻名、清高峰；明代壶杯瓶罐与供寿、时大彬、陈鸣远；清代杨怀仁等匠师、葛明祥兄弟宜均釉；紫泥、红泥、黄泥、白泥、黑泥、花泥；丁蜀市况与蜀山 10 多条龙窑 |

`zisha-tao.md` 由 3 源升为 4 源，`version: 2 → 3`，`source_count: 3 → 4`；参考文献补齐李立新。2009 把陈鸣远列入明代，李立新列为清代，两说并列不裁定；2009 作“供寿”，与“龚春”同指，字面差异照录。

## 四、no_delta 12 条

| 候选 | 实体 | 源跨度 | 既有承载 | 判定依据 |
|---|---|---|---|---|
| cand-03-99 | 卤簿 | L1869-L1874 | `terms/lubu.md` | 已载 35 类、80 种旗纹、西晋大驾卤簿；2009 同段无新增 |
| cand-04-100 | 瑶斑布 | L2615-L2630 | `terms/dian-la-man.md` | 已载南宋广西瑶族瑶斑布、成批生产与点蜡幔 |
| cand-04-41 | 蜡缬 | L2150-L2157 | `procedures/la-ran.md` | 四源条已覆盖定义、工序、裂纹与宋代瑶族用法 |
| cand-04-43 | 介质印花 | L2150-L2161 | `procedures/jiezhi-yinhua.md` | 已逐字覆盖 2009 L2156 与 2016 L2711 |
| cand-04-56 | 舞马衔杯纹皮囊式银壶 | L2232-L2260 | `works/liujin-wuma-xianbei-yinhu.md` | 三源条已载器形、纹样、工艺与何家村窖藏；2009 只作名品并列 |
| cand-05-07 | 辽代夹缬《南无释迦牟尼佛》 | L2796-L2815 | `works/namo-shakyamuni-fo.md` | 已载 2016 同段夹缬佛像、构图与三件同出 |
| cand-05-12 | 西夏茂花闪色绵 | L2855-L2862 | `events/xixia-mausoleum.md` | 已载茂花闪色绵与二股合捻加拈；`procedures/yin-jing.md` 另载田自秉“茂花闪色锦” |
| cand-05-25 | 影青瓷 | L2988-L2994 | `terms/yingqing.md` | 三源条已覆盖“玉出昆山”、假玉器、薄剔飞凤 |
| cand-05-36 | 药斑布 | L3095-L3098 | `procedures/lan-yinhua-bu.md` | 四版条已载元代药斑布灰药防染与“同于近代蓝印花布” |
| cand-05-43 | 元代朱碧山银槎 | L3159-L3175 | `works/zhu-bishan-yincha.md` | 已载尺寸、铭文、诗、印与四件传世 |
| cand-05-66 | 八达晕 | L3424-L3427 | `terms/badayun.md` | 已载 2016 同段定义、三名与明锦地位 |
| cand-05-73 | “衣冠禽兽” | L3492-L3503 | `terms/buzi.md` | 已载 2009 原句、语义翻转与“禽兽衣冠”语序；不另立成语条 |

## 五、语义判断

1. **同段异实体拆分**：羊肠裙与裥裙同出 L1831-L1834，但前者为窄瘦多褶的百褶裙，后者为多幅拼色、长裾高腰女裙，分别立目；帔子与披帛在来源中对举，前者更艳丽且有绣纹，不并入 `terms/pibo.md`。
2. **清单级 term**：元代瓷器壶、杯、匜、炉为同一源段的四种器形并列，不是单一原子实体；按清单级 term 立目，杯的细节交既有 `terms/gaozu-bei.md`，避免拆成四个微条。
3. **图版边界**：图 5-23 图注为《女史箴图》中的床，不是谢灵运木屐；图 5-18 为三国牛头鹿角金饰件，不能核对西晋花丝；图 6-8 为唐代凤首龙柄壶，不是典型执壶；图 5-19 图注仅作“魏晋南北朝 铠甲”。各条均标图版未视觉核验。
4. **span 边界**：`筒袖铠` 候选 span 为 L1858-L1866；L1873 的“盔铠制造可见工艺技术的精巧”不在 span 内，未写入该条。初稿描述中的同一判断已删除。
5. **文献转引**：天宫寺释迦立像仅见于《洛阳伽蓝记》转引，未给实物、图像或藏地；条目保留 low confidence 与证据边界。
6. **原文照录**：《开宝藏》条保留源文经名“阿惟越政遮经”，不径改为通行经名；`zisha-tao` 保留“供寿”与“龚春”的同指说明。
7. **人物时代张力**：2009 与李立新对陈鸣远所处时代的说法并列，不裁定；`zisha-tao` 的 2009 新材料与既有三源合并，不把单一来源的分期写成定论。

## 六、门禁结果

| 检查 | 结果 |
|---|---|
| `python scripts/build_discovery_index.py` | 通过；total 5,339，applied 1,479、no_delta 140、needs_evidence 2,908、rejected 812 |
| `python scripts/audit_content_quality.py` | 通过；1,313 个知识元，0 发现 |
| `python scripts/run_sync_closure.py --refresh-generated --full` | 通过；18/18 步，250 passed + 16 subtests；structural_health 122/130；relation broken target 0 |
| `python scripts/run_sync_closure.py --refresh-generated --check-generated` | **blocked_pending_commit**；17 步中前 16 步通过，第 17 步 `check generated snapshots` 以 exit 1 阻断，原因是工作树未提交，属设计行为 |
| 引文审计 | 12 个改动文件共 62 处引号短语，对所属引用来源去空白比对，0 未匹配；ASCII 双引号 0 处；自拟表述“材料即装饰”改用「」 |
| apply-plan 复核 | 12 行（11 create + 1 update）；after sha256、bytes、lines 全部与磁盘一致；update 的 before 与 HEAD blob 一致 |
| ledger 复核 | 72 行 = 24 候选 × 3 状态；终态 applied 12、no_delta 12；终态均带 target_ref |

**运行环境观察**：closure 启动时 `changed_paths_from_git()` 的 `subprocess.run(..., text=True)` 在 Windows GBK 默认解码下读取含中文路径的 Git 输出，打印 `UnicodeDecodeError` 线程异常；本轮 `--full` 仍执行全部 18 步并以 0 退出，`--check-generated` 仍按设计以 1 退出。该异常不影响本批结果，但可能使路由审计漏掉中文路径，建议后续将 `text=True` 改为显式 UTF-8 解码。另有一次 `--check-generated` 在 `build discovery index` 写 `candidate-index.jsonl` 时出现 Windows `OSError [Errno 22]`，单步重跑成功，最终阻断点仍为第 17 步。

## 七、状态与后续

- 本批未提交、未推送；`check-generated` 的阻断状态为 `blocked_pending_commit`，需用户当次授权后才能提交并复跑。
- 2009 册 unit 候选剩余 16 条：`cand-05-88` 元代寺庙壁画、`cand-05-90` 云锦纹样七类、`cand-05-92` 清代丝织品种、`cand-05-93` 明代女装与凤冠、`cand-05-94` 清代首饰与头饰、`cand-06-02` 金陵大报恩寺琉璃塔、`cand-06-04` 《工程作法》、`cand-06-12` 饾版、`cand-06-24` 剪辫易服、`cand-06-39` 五星红旗、`cand-06-43` 飞鸽自行车、`cand-06-80` 地方与民族工艺美术品种、`cand-07-17` 《工艺美术参考》、`cand-07-32` 田自秉《中国工艺美术史》、`cand-07-33` 王家树《中国工艺美术史》、`cand-07-34` 龙宗鑫《中国工艺美术史》。
- 其余五册 unit 候选与 1,363 条 claim 候选尚未启动；Book 7 及以后不启动。
