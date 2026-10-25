# 既有 KU 重叠候选清算批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-overlap-candidates-batch/`
状态：`applied`

## 一、本批做了什么

- 在 2,660 个未分组 unit 候选中，按 title／alias 归一化匹配 504 个既有 KU，筛出 53 个指向同一实体的重叠候选。
- 53 个候选全部回读原文并比对既有 KU：41 个判 `update`，写回 39 个 KU；1 个判 `create`，新建 1 个 KU；11 个判 `no_delta`，对应 10 个既有 KU；无 `rejected`。
- KU 总数由 504 增至 505（新增 `events/hufu-qishe.md`）。
- 候选索引投影后：applied 542、no_delta 26、rejected 801、needs_evidence 3,970；active 3,970、terminal 1,369。
- 本会话未执行 commit／push；批次期间工作树由外部自动提交三次（见第六节）；`02-sources/` 未改动。

## 二、写回清单

### update：39 个文件 / 41 个候选

| 文件 | 主要增量 |
|---|---|
| terms/an-furniture.md | 汉代食案两型、柱状与蹄状足、尺度及广州沙河顶东汉铜圆案 |
| terms/jianghu.md | 明代匠籍、轮班与住坐、洪武二十六年 232089 名与 62 行业、班次序列；条目由元代扩为元明 |
| works/yuan-yinjingjia.md | 双凤戏牡丹／玉兔蟾蜍灵芝纹与“豪华小交椅”造型评价 |
| terms/tihuaji.md | 脚踏提综斜织机到提花机的发展关系与李约瑟“西方晚 4 个世纪”说 |
| terms/longyao.md | 浙江上虞等地东汉窑址、陶瓷共烧转专窑及高岭土原料 |
| terms/dougong.md | 斗栱所处的秦汉木构体系、四类屋顶、板门交棂窗与梁柱叠架 |
| places/yungang-shiku.md | 石窟寺印度源流、3 世纪传入与“中国形式”造像的形成 |
| terms/chai-yao.md | 吴越钱氏 14 万件贡瓷、秘色瓷上品、“片瓦值千金”与周世宗贡瓷推测 |
| terms/guan-yao.md | 鼎炉觚彝仿古器形、宫廷风格与开片的胎釉膨胀系数成因 |
| terms/kesi.md | 扩展 2009 版位置至 L4265；南宋苏州松江产地、贡品与乡村副业、父子相传及新中国镶色新作 |
| terms/qingtong-liqi.md | 礼的鬼神起源、祀与戎、苍璧黄琮与良渚玉礼器、饮食器与礼器交织 |
| works/san-jiao-lou.md | 木斗与铁耧脚连通的耧车结构、两辕两扶把、日种一顷及二牛三人耦犁 |
| publications/zhouyi.md | 文王演易、韦编三绝、《系辞传》四则制器原文与“道器在形内”的整体理解 |
| persons/mozi.md | 扩展赵农位置至 L2395；光学力学数学声学机械土木六类研究与《墨子·佚文》因材施工的材质观 |
| works/houfeng-dizhenyi.md | 阳嘉元年、篆文山龟鸟兽饰纹、一龙发机七首不动与合契若神、木质模型 |
| terms/dulunche.md | 新增李立新源并扩展赵农位置至 L2684；鸡公车／羊角车别称、汉代画像砖雏形与绳带绕颈、倒拉、木棒支撑；同组“鹿车”候选合并写入 |
| places/dunhuang-mogao-ku.md | 河西走廊位置、366／353 两说、砂砾岩与 492 窟 39 早期窟、中心塔柱与人字披、支提窟渊源 |
| terms/lifang-zhi.md | 扩展赵农位置至 L5388-L5425；北宋废里坊、废夜禁与夜市，及开封三重城、40 里、四水贯都、御道中轴 |
| works/kaifeng-xiangguosi-pagoda.md | 褐色琉璃瓦与锈铁色泽得名、螺旋蹬道联结塔壁与中心塔柱；与既有“28 种琉璃砖”说并列 |
| works/miaoying-si-baita.md | 赵农 53 米异文与宝瓶塔身、元大都喇嘛塔样式；高度两说并列不裁定 |
| institutions/fujian-chuanzhengju.md | 1865 年徐寿“黄鹄”轮与江南制造总局、福州／天津／广东军装／旅顺船坞序列及洋务企业年表 |
| procedures/lost-wax-casting.md | 扩展田自秉位置至 L915；“约商代以后、公元前五六世纪春秋已有实物”的上限说 |
| procedures/jiazhu-tai.md | 新增田自秉与 2016 两源；行像、戴逵瓦棺寺三绝与汉代夹纻硬胎；同组“夹纻胎”候选合并写入 |
| terms/qian-you-tao.md | 硅酸主体与钙钠铅媒熔剂、关中最早产地、西汉呈色与器形、南北软硬釉 |
| terms/rendong-wen.md | 扩展田自秉位置至 L2992；二方连续卷曲结构、响堂山浮雕及佛光、石碑边侧、敦煌藻井实例 |
| terms/jiaoxie.md | 阿斯塔那唐垂拱四年（688）绞缬裙及绛紫、茄紫菱形网格 |
| works/liujin-wuma-xianbei-yinhu.md | “屈膝衔杯赴节”唐诗、千秋节舞马表演与马身锦绣金银饰物 |
| terms/wuda-mingyao.md | 田自秉“显然有偏颇”之评与磁州窑、吉州窑民窑贡献 |
| terms/nanjing-yunjin.md | 得名两说与清代文献无载、妆花 6／9／18 色过管配色、明式风格与蒙藏衣帽用途 |
| terms/wenzhi.md | “绘事后素”、质先文后与不偏不倚的中正之境 |
| works/yuanmingyuan.md | 郎世宁等欧洲设计师、罗可可家具壁毯与谐奇趣铜版画 |
| terms/yuefenpai.md | 作者多未受正规西画训练、木刻与年画渊源、“简单甚至肤浅”及“空前绝后”之评 |
| terms/zisha-tao.md | 龚春、时大彬、制壶四大家、陈鸣远、杨彭年兄妹、邵大亨与“块团形式” |
| works/qin-shi-huang-ling.md | 新增 2016 源并扩展赵农位置至 L2674-L2676；1980 年两组铜车马、1555 块／12 年复原、3000 部件、1:2 与 1200 千克、工艺及戎车安车尺寸伞盖 |
| terms/yuexiu.md | 既有 2009 引得句中补“通过洋庄源源输向世界各地”的外销渠道；无新增源 |
| terms/zhongshanzhuang.md | 早期背面有缝与中腰带、胖裥、定型后后背无缝、平贴袋与袋盖弧形、垫肩收腰廓形 |
| institutions/zhongguo-meishuguan.md | 扩展 2016 位置至 L5290-L5317；1958 年 9 月国庆工程十项、彩画木雕装饰与图 11-25 十大建筑题名 |
| persons/hang-zhiying.md | 1920 年商务印书馆练习生名单、德日画家授课与吴待秋教中国画、广告画家群及早期商业招贴专家身份 |
| persons/guan-zhong.md | 扩展 2016 位置至 L1500-L1503；“字仲”与“春秋第一相”称谓；候选标题“管子”指人物，写回 person 而非 publication |

### create：1 个 KU

| 文件 | 内容 |
|---|---|
| events/hufu-qishe.md | 战国服饰改革事件：胡服形制（短衣、长裤、靴）、赵武灵王说辞、《史记·赵世家》三句引文、带钩“钩络带”、跨文化采纳与设计史意义；source_count 1（赵农 L2175-L2179） |

### no_delta：11 个候选 / 10 个既有 KU

庞薰琹（2 个候选，含异写“庞薰琍”）、水碓、龙门石窟、干栏式、彩漆动物座屏、司母戊鼎、汝窑、定窑、黄成、李诫。

## 三、本批的判断

1. **重叠即归并，不另建条**：53 个候选指向既有实体，全部以既有 KU 为目标。同实体的重复候选只保留 canonical：`dulunche` 合并 2009“独轮车”与 2011“鹿车”；`jiazhu-tai` 合并 2010“夹纻”与 2016“夹纻胎”；庞薰琹两候选合并为一条 `no_delta`。
2. **canonical 按信息量指定**：多候选目标取原文跨度更长、细节更完整者；同组其余候选的独有事实并入同一 KU，不重复建条。
3. **no_delta 的判定标准**：既有 KU 正文已完整覆盖候选摘要与原文事实，仅措辞不同，不因“可以改写”而写回。
4. **类型与维度判断**：胡服骑射作 `event`／`historical_event`，维度 E（现代性与跨文化互动），因其核心是服饰制度的跨文化采纳而非器物形制；管子候选 payload 为人物生卒、字与称谓，改映射 `persons/guan-zhong.md`，不写 `publications/guanzi.md`。
5. **两册冲突并列**：妙应寺白塔 53 米（赵农）与 50.9 米（2016）并列；开封铁塔褐色琉璃瓦与 28 种琉璃砖并列；莫高窟 366 年与 353 年两说并列；云锦得名两说并列。均不裁定。
6. **来源计数按实际新增**：31 个 update 新增 32 个来源块（`jiazhu-tai` 增田自秉与 2016 两源），`source_count` 相应递增；7 个仅扩展既有 source 位置；`yuexiu` 无新增源，仅改既有引句。

## 四、同条并列的说法

1. **妙应寺白塔高度**：2016 版作 53 米，既有条目作 50.9 米；两说同条并列，不取其一。
2. **开封铁塔外观**：一作褐色琉璃瓦、因锈铁色泽得名；一作 28 种琉璃砖。两种描述并列，未合成单一材质结论。
3. **莫高窟始建年**：366 年（前秦建元二年）与 353 年两说并列。
4. **南京云锦得名**：一说因“云纹”而得名，一说因“色泽灿烂如云霞”得名；清代文献无载一点照录。
5. **胡服形制**：原文以“短衣、长裤、靴子”概括，未记具体裁剪与材料；条目不作外部补全。

## 五、本批的方法判断

- **回读原文而非只据候选摘要**：40 段原文跨度逐条回读（`_tmp_overlap_spans.txt`，28,870 字符），核对数值、分期与引文后再写。
- **先比对既有正文再动笔**：导出 39 个目标 KU 的 304 条既有 bullets，逐条比对，只保留真正增量；已覆盖的草稿（如提花机王逸／马王堆、斗栱一斗二升、中山装九粒扣等）全部删除，避免同条重复。
- **精确 change-set**：所有替换以 `text.replace(old, new, 1)` 执行，未命中即中止；扩展源重写 `location` 与 citation 末段；新源按固定册序插入 `sources:` 与 `created:` 之间。
- **编码控制**：KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写回，写后核验 `CRLF files: 0`。
- **判定与写回分离**：候选台账记录 159 行状态迁移（53×3），apply-plan 记录 40 行精确指纹，二者与磁盘、索引三方核对。

## 六、状态与验证

- `apply-plan.jsonl`：40 行（update 39、create 1）；40/40 的 after 指纹与磁盘一致，39 个 update 的 before 均与当前文件不同，create 的 before 为 null。
- `candidate-decision-ledger.jsonl`：159 行，53 个候选各 3 行；终态 applied 42、no_delta 11。
- `canonical-mapping.json`：50 个实体（39 update、1 create、10 no_delta），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:d5229189…`（needs_evidence 4,023），批后 `sha256:7ee85080…`（needs_evidence 3,970）；重建幂等，字节与哈希不变。
- 内容质量审计：505 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，证据引用 505/505 可解析，断链 0，Frontmatter 缺 0。
- Sync closure：首次运行在第 17 步因工作树未提交被 `git diff --exit-code HEAD` 阻断；生成态快照提交后重跑 19/19 全部通过，250 项测试与 16 个子测试均通过。随后修正 manifest 与 summary 又产生未提交改动，末次运行再次停在第 17 步——这是该门禁的预期行为，授权提交后即可转绿。
- 批次期间工作树由外部自动提交三次并推送其中两次：21009c4（17:59:18）、99bf8ef（18:00:44，已推送）、8d79692（18:03:53，本地未推送）；作者均为 Yixue He。本会话未调用 `git commit` 或 `git push`。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 当前 505 个 KU：multi_source 496、single_source 9；`source_count=1` 的条目不再标 high confidence。
- 结构层仍为 0/4，层级挂载 0/505，正式 relation 0 条，Theme／Topic 均未实体化。
- 未分组 unit 候选仍有 2,607 个 active（unit 候选合计 3,976，terminal 1,369）；claim 候选 1,363 个待进入 claim／evidence 流程。
- 本批临时脚本与中间文件（`_tmp_overlap_*`、`_tmp_bullets.txt`、`_tmp_plan_list*`、`_tmp_row.txt`、`_tmp_source_check.py`、`_tmp_preview/`）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
