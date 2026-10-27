# 2010 册 units 批次 T2（商代）摘要

## 1. 目标与范围

- 工作包：`06-runtime/automation/2026-10-26-2010tianzibing-units-batch-t2/`
- 来源：田自秉《中国工艺美术史（修订本）》（2010），doc_id `2010-tianzibing-zhongguo-gongyi-meishushi`
- 候选范围：2010 册商代章节 unit 候选 19 条（cand-03 16 条、cand-04 2 条、cand-10 1 条）
- 裁定结果：新建 16 条、更新 1 条、no_delta 2 条、rejected 0 条
- 状态：applied（19 条全部终态，均有 `target_ref`）

## 2. 来源与复读范围

- 复读区间：第二章商代的工艺美术（L854-L1275），含第一节概说、第二节青铜工艺（制作、造型、装饰、艺术特点）、第三节陶瓷工艺、第四节雕刻工艺、第五节其他工艺、第六节结语。
- 另因 `cand-10-46`（巧色）跨度延至宋代，补读 L3918-L3924（宋代其他工艺的玉雕巧色段），用于同实体更新，不扩为宋代章节的整章复读。
- 彩版 6、插图 4、8、10、14、15、19、20、21、22、23、24、25、26、27 均只读图注，未视觉核验。

## 3. 裁定结果

| 候选 | 实体 | 处置 | 目标 |
|---|---|---|---|
| cand-03-16 | 杜岭方鼎 | create | `works/du-ling-fang-ding.md` |
| cand-03-20 | 铜连座立人 | create | `works/tong-lianzuo-liren.md` |
| cand-03-23 | 将军盔 | create | `terms/jiang-jun-kui.md` |
| cand-03-26 | 商代青铜器八类 | create | `terms/shangdai-qingtongqi-balei.md` |
| cand-03-32 | 妇好三联甗 | create | `works/fuhao-sanlian-yan.md` |
| cand-03-36 | 夔纹 | create | `terms/kui-wen.md` |
| cand-03-37 | 回纹 | create | `terms/hui-wen.md` |
| cand-03-39 | 郭沫若 | create | `persons/guo-moruo.md` |
| cand-03-42 | 白陶 | create | `terms/bai-tao.md` |
| cand-03-45 | 青釉瓷尊 | create | `works/qingyou-ci-zun.md` |
| cand-03-49 | 妇好墓玉人 | create | `works/fuhao-mu-yuren.md` |
| cand-03-51 | 龙纹 | create | `terms/long-wen.md` |
| cand-03-52 | 凤纹 | create | `terms/feng-wen.md` |
| cand-03-53 | 灰陶 | create | `terms/hui-tao.md` |
| cand-04-03 | 象牙杯（妇好墓） | create | `works/xiangya-bei.md` |
| cand-04-76 | 花土 | create | `terms/hua-tu.md` |
| cand-10-46 | 巧色 | update | `procedures/yudiao-taocai-qiaose.md` |
| cand-03-07 | 二里头文化 | no_delta | `places/erlitou-site.md` |
| cand-03-33 | 五爵 | no_delta | `terms/qingtong-jiuqi.md` |

## 4. 新建 16 条

**作品（6）**：杜岭方鼎、铜连座立人、妇好三联甗、青釉瓷尊、妇好墓玉人、象牙杯。

**术语（9）**：将军盔、商代青铜器八类、夔纹、龙纹、凤纹、回纹、灰陶、白陶、花土。

**人物（1）**：郭沫若。

单源条目统一：`consensus: tentative`、`evidence_status: source_backed`、`version: 1`、`source_count: 1`，日期 created/updated/last_verified 为 2026-10-26、review_due 为 2027-04-26，`academic_translation_status` / `translation_status` 均为 provisional。confidence：medium 15 条、low 1 条（郭沫若）。

## 5. 更新 1 条

| 候选 | 既有条目 | 追加内容 | 计数变化 |
|---|---|---|---|
| cand-10-46 | `procedures/yudiao-taocai-qiaose.md` | 商代 L1231 已用巧色的判断；宋代 L3922 巧色定义与子母猫、甘黄玉葵花杯、玉雕人物三例；citation 追加两处 | source_count 1 不变（同册多跨段），version 1→2 |

同册多跨段按契约追加 citation，不新增 source block；原 L5288-L5290 的新中国材料保留，正文另起段落，未覆盖。

## 6. 语义判断与内部张力

1. **二里头文化记 no_delta**：`places/erlitou-site.md` 已据田自秉同段立条，别名收“洛达庙文化”，正文引 L864 的文化界定与夏文化存疑、L870 的早晚两期陶器序列，并记遗址群清单。另立 `terms/erlitou-culture.md` 会与遗址条重复，故并入不新建。
2. **五爵记 no_delta**：`terms/qingtong-jiuqi.md` 已以“五爵”为别名，正文与核心条均记五器合称，候选 payload 的定义只是这一合称。L970-L1001 的五器分述属该块其他内容，不在本候选定义内。
3. **巧色候选合并两处并跨章节**：cand-10-46 由 cand-03-50 合并而来，payload 明言巧色定义据 L3922、L5288，L1231 只见名称。既有条目原只据 L5288-L5290 记新中国玉雕，故按同实体更新，补商代与宋代两段；明代陆子冈“茶晶花插”巧色在 L4464，不在本候选跨度，留明代批次。
4. **郭沫若补第二处引述**：候选跨度为 L1118-L1460，来源在 L1460 另记郭沫若以鬼柳、榉柳木材花纹解释周代窃曲纹，并随即提出“仍是变形的动物纹样”的反驳。条目两说并录，附来源的反驳，confidence 仍取 low：来源未给生卒年、任职、著述与两说出处。
5. **花土一詞两义**：L1260 指大司空村殷墓麻布残痕上的黑色饕餮图案，L1262 指武官村大墓雕花木器涂朱红漆后在夯土中留下的印痕。来源未说明二者关系，条目两义并列，不合并为单一定义。
6. **杜岭方鼎是两件鼎的合称**：L899 明言“两件大型铜方鼎，考古界称之为‘杜岭方鼎’”，来源未分别命名，条目按合称著录，不并作一件，也不补两鼎差异。
7. **铜连座立人的年代归属**：来源作“约为商末周初”，本条照录，不按商代章节径定为商代；同段三星堆铜人头像（彩版 6）记入核心内容，图版未视觉核验。
8. **商代青铜器八类的性质**：八类是田自秉按生活用途的分类，不是考古类型学标准分类；条目照录并标来源性质，未改写为通行器类体系。
9. **灰陶占比与成形方法**：L1180 的“百分之九十以上”是来源表述，未给统计口径；陶模、陶车、盘条、手制四种成形方式照录，不补工艺参数。
10. **白陶的起源推测**：L1184 明言“有人推测”北方制陶工人模仿南方硬陶，条目照录推测归属，不当作定论；商代以后不复发现的表述亦照录。
11. **妇好墓玉人的服饰句被图版隔断**：L1226 末“腹前悬长”与 L1231 首“条形的‘蔽膝’”之间隔插图 24 与图注，条目分两处引，未拼成单行逐字引文。
12. **图版层与正文层分开**：彩版 6 与插图 4、19、20、21、27 等只著录图注，不据图补尺寸、藏地与出土层位；三联甗的 64 厘米、138.2 公斤与象牙杯的 30.5 厘米均出自正文。

## 7. 生成态与门禁

- 结构审计：`_zn_struct.py` 16 个新建文件与 1 个更新文件 0 问题；`_zn_audit.py` 0 findings；`_zn_audit_strict.py` 0 findings。
- 引文审计：16 个新建条目 68 处双引号逐字引文，逐条与田自秉 2010 册源文去标点比对，0 遗漏、0 行号错配；更新条目新增 4 处引文另核 L1231、L3922，均落在所标单行。跨行句“每个坩埚只能熔铜10多斤……才能成功”用「 」。
- 索引重建：total 5339 不变；applied 2370→2387、needs_evidence 1924→1905、rejected 852 不变、no_delta 193→195；terminal 3415→3434。知识元 2127→2143。
- 工作包：apply-plan 17 行（16 create、1 update）、candidate-decision-ledger 57 行（19×3）、canonical-mapping 19 条、manifest 1 份。
- `python scripts/run_sync_closure.py --refresh-generated --full`：18 步全部通过（250 tests passed, 16 subtests passed）；结构健康分与类型覆盖 8/8 不变；内容质量发现 12 条均为既有问题（liezi-tangwen、songshi-yufuzhi、armillary sphere、zhao-nong、zhongguo-yishu-shejishi-zhaonong-2009、he-zun），本批未新增。
- `python scripts/run_sync_closure.py --refresh-generated --check-generated`：[17/17] FAILED exit=1，因本批与既有未提交知识元、生成态快照未提交，记 `blocked_pending_commit`，属设计行为。

## 8. 跨批修正

- 本批无跨批语义修正。
- 郭沫若条目在写入后、建包前补入 L1460 的窃曲纹说与来源反驳，citation 由 L1118 改为 L1118, L1460；`_zn_t2_e1.py` 同步，避免重生成回退。
- 巧色条目版本由 1 升为 2，`updated` / `last_verified` 续为 2026-10-26，`review_due` 续为 2027-04-26。

## 9. 未决事项

- 工作区与生成态快照未提交、未推送（无用户当次授权）。
- 2010 册 unit 候选剩余 353 条（404−51），其中 work 143、term 142、person 59、publication 9；claim 候选 278 条未启动。
- 彩版 5 及以后 7 条作品候选留给商周至战国章节批次。
- 郭沫若条为 low confidence：只有两处学术意见转述，无生平与著述。
- 明代陆子冈“茶晶花插”巧色在 L4464，未纳入本批，留明代章节批次。
- 图版彩版 6 与各插图未视觉核验；器物尺寸、藏地与出土层位多未载。
- Book 7 及以后不启动（用户范围限定）。
