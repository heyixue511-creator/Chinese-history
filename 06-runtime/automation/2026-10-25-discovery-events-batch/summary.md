# 考古发现事件候选批次执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-discovery-events-batch/`
状态：`applied`

## 一、本批做了什么

- 从田自秉《中国工艺美术史（修订本）》的未分组 unit 候选中，取 7 个 `event` 候选（`cand-02-46/47/48/49`、`cand-05-54/55`、`cand-06-50`）逐条回读原文并作语义裁决。
- 6 个判 `create`，新建 event KU；1 个判 `no_delta`（舞蹈纹彩陶盆，已由既有 work KU 完整覆盖）；无 `update`、无 `rejected`。
- KU 总数由 505 增至 511，event 类型由 11 增至 17。
- 候选索引投影后：applied 548、no_delta 27、rejected 801、needs_evidence 3,963；active 3,963、terminal 1,376。
- `02-sources/` 未改动；本会话未执行 commit／push。

## 二、新建清单

| 文件 | 时间／地点 | 主要增量 |
|---|---|---|
| events/xianrendong-taoci-chutu.md | 1962 年，江西万年仙人洞 | 距今 8000 多年陶器；来源称“我国目前发现的最早的陶器资料”；同段并置裴李岗、磁山、大地湾、河姆渡、仰韶等新石器时代陶器序列 |
| events/donghulin-muzang.md | 1966 年，北京门头沟东胡林村 | 新石器时代早期墓葬；少女遗骸的小螺壳项链与牛肋骨骨镯；来源以“装饰的萌芽”与“审美的功利性高于艺术性”作解释 |
| events/xixiacun-canjian.md | 1926 年，山西夏县 | 半个蚕茧与养蚕起源；同段钱山漾家蚕丝织物（每平方英寸经纬各约 120 根）、柴达木毛布、龙山文化骨梭与麻线合股 |
| events/zenghouyi-mu-fajue.md | 1977 年，湖北随县 | 铜尊、铜盘失蜡法；失蜡法四项特点；1979 年淅川下寺铜禁铜盏为最早制件、把历史提早一百多年 |
| events/mashan-yihao-mu-sichupin.md | 1982 年 1 月，湖北江陵马山砖厂一号墓 | 绢罗纱锦组绦、二重经、几何纹凤鸟纹锦（双色、二方连续）、舞人动物纹锦（三色、舞蹈人首见）、辫绣为主的刺绣与龙凤虎纹绣衣 |
| events/mawangdui-yihao-mu-fajue.md | 1972 年，湖南长沙东郊 | 100 多件、46 段、58 件、“丝绸之库”；绢纱罗绮锦与平纹斜纹罗纹；经锦三色；绒圈锦双经轴、总经数约 8800～112000 根 |

## 三、no_delta 判定

`2010-tianzibing-zhongguo-gongyi-meishushi:cand-02-47`（舞蹈纹彩陶盆）→ `04-knowledge/units/works/wudaowen-caitao-pen.md`。

既有 KU 已记录 1973 年秋青海大通上孙家寨出土、高 14 厘米／口径 29 厘米／底径 10 厘米、五人一组三组共十五人的舞蹈纹与内壁四道平行带纹；候选 payload 无独立事件增量，再建 event 条会与 work 条重复，故判 `no_delta`。

## 四、本批的判断

1. **event 与 work 分工**：发现事件记“何时、何地、出土了什么、来源据此说明什么”，器物形制、尺寸、纹样细节归 work 条。曾侯乙墓事件不重复 `works/zenghouyi-zunpan.md` 的透雕与双层铜梗，只补 1977 年发掘年份与淅川下寺年代序列。
2. **已有 work 覆盖即 no_delta**：舞蹈纹彩陶盆的全部候选事实均已在 work 条内，不因“事件可另立条目”而强行建条。
3. **数量异文并列**：马王堆丝织品，田自秉记 46 段、58 件；高丰记 46 幅、50 余件。两说并列保留，不裁定。
4. **年份照录**：曾侯乙墓发掘年份照录田自秉“1977 年”，不据外部资料校正；`date_note` 已注明同段并列 1979 年淅川下寺墓。
5. **证据边界写明**：仙人洞、东胡林、西阴村三条来源仅一两句，条目内明确写出未记器形、尺寸、发掘机构、鉴定方法，不引来源外材料补全。
6. **维度判断**：6 条均为 `primary_dimension: B`（造物、工艺与生产技术），因候选核心是工艺起源、铸造法与丝织技术，而非制度或跨文化互动。

## 五、本批的方法判断

- 7 个候选对应的 9 处原文跨度逐条回读（L443、L484、L583、L829、L1814、L1962、L1972、L2466、L2470），核对时间、地点、数量与引文后再动笔。
- 建条前比对 6 个相关既有 KU（`wudaowen-caitao-pen`、`susha-chanyi`、`zenghouyi-zunpan`、`zenghouyi-bianzhong`、`lost-wax-casting`、`kesi`），确认增量边界。
- 模板沿用 `events/hufu-qishe.md` 的六节结构；`sub_type` 取 taxonomy 枚举 `discovery`。
- KU 文件统一以 `write_bytes(text.encode("utf-8"))` 写入，写后核验无 CRLF。
- 判定与写回分离：台账 21 行（7×3）、apply-plan 6 行、mapping 7 条，与磁盘、索引三方核对。

## 六、状态与验证

- `candidate-decision-ledger.jsonl`：21 行，7 个候选各 3 行；终态 applied 6、no_delta 1。
- `apply-plan.jsonl`：6 行，均为 create，`before` 为 null；6/6 的 after 指纹与磁盘一致。
- `canonical-mapping.json`：7 条（create 6、no_delta 1），候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:7ee85080…`（applied 542、no_delta 26、needs_evidence 3,970），批后 `sha256:bf61969f…`（applied 548、no_delta 27、needs_evidence 3,963）；重建幂等。
- 内容质量审计：511 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据引用 511/511 可解析，断链 0，Frontmatter 缺失 0，events 17。
- Sync closure：运行 `--refresh-generated --full --check-generated`，结果见 manifest 的 `verification` 字段；第 17 步若因工作树未提交而阻断，属该门禁设计行为，授权提交后即可转绿。

## 七、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 6 条新建 KU 均为 `source_count: 1`（田自秉），未标 high confidence。
- 西阴村、仙人洞、东胡林三条来源极简，事实密度低，后续若有第二来源应优先补证。
- 结构层仍为 0/4，层级挂载 0/511，正式 relation 0 条，Theme／Topic 均未实体化。
- 未分组 unit 候选仍有 2,600 个 active；claim 候选 1,363 个待进入 claim／evidence 流程。
- 本批临时脚本（`_tmp_discovery_emit.py`、`_tmp_discovery_verify.py`、`_tmp_events_inv.py`、`_tmp_events.tsv` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
