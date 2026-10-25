# 赵农《中国艺术设计史》2009 册工艺候选批次（四）执行总结

日期：2026-10-25
工作包：`06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-d/`
状态：`applied`；验证 `passed_with_generated_block`

## 一、本批做了什么

- 从赵农《中国艺术设计史》（2009）的未分组 unit 候选中，续取第 26—39 个 `procedure` 候选逐条回读原文并作语义裁决。
- 12 个判 `create`，新建 procedure KU；2 个判 `update`，补入既有 procedure KU；无 `no_delta`、无 `rejected`。
- KU 总数由 650 增至 662，procedure 类型由 53 增至 65。
- 候选索引投影后：applied 721、no_delta 43、rejected 801、needs_evidence 3,774；active 3,774、terminal 1,565。
- `02-sources/` 未改动；本会话未执行 commit／push。
- 赵农 2009 册的 `procedure` 候选至此清零。

## 二、新建清单

| 文件 | 时间／地域 | 主要增量 |
|---|---|---|
| procedures/gong-hua.md | 明代（明末）；中国 | 吴发祥、胡正言印笺谱时以刻版压印使花纹凸显，犹如钢印；来源称“化旧翻新，穷工极变”是明代书籍印刷不断进步的根本原因；未给刻版深度、压力、纸张湿度及与短版的先后关系 |
| procedures/ci-huazi.md | 清代中期；山东泰安 | 徐志定在泥活字上挂釉烧成瓷活字，为最早瓷活字样式，印《周易说略》；同段记李瑶“仿宋胶泥版印法”、翟金生 30 余年积 10 余万泥活字、陶质范母翻制阳文泥活字；泥活字只作脉络，不并入瓷活字工序 |
| procedures/shiyin-ben.md | 晚清；中国 | 石印自西方传入，提高书籍图版质量；石材制版、胶性药墨过写药纸、覆石揭纸，依油水分离印书；未给石版材质、药墨配方、压印机具与成本 |
| procedures/xian-zhuang.md | 明代中期；中国 | 封面封底裁成书样，天头、地脚、右边裁齐，丝线四孔装订；上下角厚纸包角防磨；封面贴书目标签；未给线材、孔距、打孔穿线次序与装帧演变关系 |
| procedures/ming-changcheng-qiangti-gouzhu.md | 明代；山海关至山西段 | 墙体以巨砖、石条外包，内以黄土、石灰、江米质黏合；外墙设垛口，沿线建烽火台；明长城全长 12,700 多里，设九边镇；未给砖石尺寸、灰浆配比、夯层与施工组织 |
| procedures/huo-pao-zhuzao.md | 明代至清代；中国；虎门 | 洪武“大碗口铳”铁炮见铜制到铁制之变；锻造以熟铁成瓦片、铁钉连接、锉磨内壁；铸造经铸型、铣模、合模、化料、浇注、起模、验膛、齐口、镟膛、钻火门、制铳车十一序；记佛朗机、红夷炮、神威大将军；虎门炮台炮长 2.3 米、口径 0.14 米，火药铁弹各 15 斤 |
| procedures/xiandai-zaozhi-jishu.md | 近代至 1949 年后；上海、广州 | 1891 年李鸿章创“纶章造纸局”，为中国近代第一家引进国外造纸技术的工场；民国广州造纸厂依赖进口纸浆，抗战爆发后未能规模化；1949 年后可产造纸机械与纸浆；现代以木材为原料，硫酸盐法、中性亚硫酸盐法连续蒸煮并高速造纸 |
| procedures/qianzi-yinshua.md | 19 世纪末传入；1980 年前广泛使用 | 铅字印刷随西方石版、铅字技术传入；凸版形式，活铅字排版组合，轮转机印刷；1980 年前杂志、报刊广泛采用；未给铅合金配比、字号字模与排版工序 |
| procedures/zhaoxiang-zhiban.md | 现代；中国 | 以胶片感光原理把细致图像制成印版，弥补铅字印刷简单、难印复杂插图的缺陷，达到图文并茂；未给网线、感光材料、制版流程与设备 |
| procedures/siwang-yinshua.md | 现代；中国 | 利用照相感光方法在丝网上制成漏版，进行细致印刷；来源仅此一句，未给丝网材料、感光胶、刮板、套色与干燥工序；`confidence` 记 `low` |
| procedures/tongban-yinshua.md | 现代；中国 | 铜版涂蜡、刻刀刻画、酸腐蚀加深线条、去蜡后油墨印刷；未给铜版厚度、刻刀、酸液配方、腐蚀时间与压印机具；本条为铜版蚀刻，与铜活字排印区分 |
| procedures/dianzi-zhaopai.md | 20 世纪末；中国 | 随计算机桌面印刷系统普及出现，解决设计印刷难题；电子排版、喷绘、复印机逐渐改变印刷制作观念与方法，推动版面设计发展；未给系统型号、字体格式、输出精度与时间节点 |

## 三、update 清单

| 文件 | 候选 | 变更 |
|---|---|---|
| procedures/huozi-yinshua.md | cand-09-67 | 来源位置由 L5041-L5060 扩为 L5041-L5060, L6539-L6541；date 增“元代王祯木活字”，location 增“安徽旌德”，participants 增王祯，tags 增元代、王祯、活木字、木活字、转轮排字；新增王祯活木字描述段、元代活木字与转轮检字等核心条目、证据边界；相关知识元增 `persons/wang-zhen.md`、`publications/wang-zhen-nongshu.md` |
| procedures/duanban-taoyin.md | cand-10-101 | `source_count` 1→2，增赵农 2009 L7195；aliases 增短版技术、短版；date_note 增“赵农系于明末”；新增明末短版描述段与分册标注的核心条目；相关知识元增 `publications/luoxuan-biangu-jianpu.md`、`procedures/gong-hua.md`；参考文献增赵农 |

- `huozi-yinshua.md`：before `sha256:e552711a…`／6,641 bytes／94 行；after `sha256:e58704e0…`／8,752 bytes／105 行。
- `duanban-taoyin.md`：before `sha256:030828f4…`／3,844 bytes／81 行；after `sha256:7d828876…`／6,247 bytes／103 行。
- 两条 before 指纹与历史 apply-plan 中创建时的 after 指纹逐项一致，再与重建的 pre-image 复核后写入。

## 四、no_delta 判定

本批无 `no_delta`。14 个候选逐一与既有 procedure KU 对账：

- `活木字印刷` 由既有 `huozi-yinshua.md` 承载。该条已记“后人刻制木字、铅字、铜字”，王祯活木字正是这条改进线索的展开；同一工序家族、同一来源册，判 update，不另立重复条目。
- `短版技术` 由既有 `duanban-taoyin.md` 承载。赵农所记明末短版与高丰所记明代创造、清代盛行的短版套印为同一技术，且“短版技术”“短版”已作别名收录，判 update。
- 其余 12 条在既有 procedure KU 中无对应实体，判 create。`gong-hua.md` 与短版套印同见于笺谱印制，但拱花为压印凸起、短版为分色套印，工序不同，分列互指；`ci-huazi.md` 与 `huozi-yinshua.md` 同属活字排印，但瓷活字多出挂釉烧成工序，分列互指；`xiandai-zaozhi-jishu.md` 与 `zaozhishu.md` 分属现代工业造纸与传统植物纤维造纸，分列互指；`ming-changcheng-qiangti-gouzhu.md` 与 `rammed-earth-board-construction.md` 的版筑墙体材料与构造不同，分列互指。

## 五、本批的判断

1. **两条 update 以同一实体为准，不以“材料不同即分列”机械处理**：王祯木活字与毕昇泥活字同属活字排印，既有条目已把元明木、铅、铜字写入改进线索，故补写而不复制条目；短版技术是短版套印的别名，故合于原条。分列只用于工序单位确实不同的对象，如拱花与短版、瓷活字与泥活字。
2. **瓷活字条以瓷为主、泥活字为脉络**：徐志定挂釉烧成瓷活字是本条主实体；同段李瑶、翟金生材料足以说明清代泥活字的延续与范母翻制路线，但不足以另立“清代泥活字”完整工序，故在同条记脉络并明确不并入瓷活字工序。
3. **现代印刷五条按制版原理分列**：石印（油水分离）、铅字（凸版活字）、照相制版（胶片感光）、丝网（感光漏版）、铜版（蚀刻）、电子照排（桌面系统）各自成条，不合并为“现代印刷”一条；各条互指，保留来源对“传统印刷面临淘汰”的判断。
4. **铜版印刷与铜活字严格区分**：来源此处讲的是涂蜡刻版、酸腐蚀的铜版蚀刻；正文与相关知识元均注明与铜活字排印不是同一工序，避免同名混淆。
5. **火炮铸造兼记锻造与铸造两路**：来源把锻造熟铁瓦片、铁钉连接、锉磨与铸造十一序并列；本条两存，不把十一序写成唯一工艺，也不把佛朗机、红夷炮、神威大将军混为同一炮型。
6. **原文疑字照录**：来源“龙门火炮”承上文虎门炮台，疑为“虎门”之讹；本条照录“龙门”，在核心条目注明疑误，不改原文。
7. **线装与明长城只写来源所记工序与构造**：线装未补打孔穿线次序，明长城未补灰浆配比与夯层；两者均把来源未载参数写入证据边界。
8. **现代造纸以产业节点与技术路线并记**：纶章造纸局、广州造纸厂、1949 年后造纸机械与纸浆，与木材原料、硫酸盐法、中性亚硫酸盐法、连续蒸煮、高速造纸同条；不把“1949 年后满足社会消费需求”改写为产量数据。

## 六、本批的方法判断

- 14 个候选逐条回读原文行段：拱花 L6819、瓷活字 L7553-L7564（并核 L7242 附近清代活字脉络）、石印本 L7202、线装 L7255-L7257、明长城 L7263、火炮 L8139-L8149、现代造纸 L8153-L8160、铅字 L8162、照相制版 L8164、丝网 L8162、铜版 L8164、电子照排 L8164；活木字 L6539-L6541、短版技术 L7195。核对材料、步骤、工具、引文与例证后再动笔。
- 候选 payload 的 `summary` 与 `proposed_fields` 为机器提取，span 常为章级；本批一律以原文行段为准，机器摘要只作索引，不作阅读替代。
- 12 个 create 均 `source_count: 1`、`consensus: tentative`；`confidence` 为 medium 11 条、low 1 条（丝网印刷）。2 个 update 的 `source_count` 分别为 1（同一赵农册合并两处位置）与 2（高丰、赵农两册）。
- KU 文件以 UTF-8 写入；写后做 YAML 解析、来源数与参考文献数一致性、六节结构与 BOM 检查，14/14 通过。
- 判定与写回分离：台账 42 行（14×3）、apply-plan 14 行（create 12、update 2）、mapping 14 条，与磁盘、索引三方核对，0 错误。

## 七、状态与验证

- `candidate-decision-ledger.jsonl`：42 行，14 个候选各 3 行；终态 applied 14。
- `apply-plan.jsonl`：14 行，create 12 行 `before` 为 null，update 2 行带 before 指纹；14/14 的 after 指纹与磁盘一致，2/2 的 before 与 pre-image 一致。
- `canonical-mapping.json`：14 条，候选并集与台账完全一致。
- 候选索引：5,339 行；批前 `sha256:ac232887…`（applied 707、no_delta 43、needs_evidence 3,788、rejected 801），批后 `sha256:813de48a…`（applied 721、no_delta 43、needs_evidence 3,774、rejected 801）；重建幂等。
- 内容质量审计：662 个 KU，0 findings。
- 仓库审计：结构门禁健康 122/130，知识结构完整性 55/65，证据链完整性 55/55，证据引用 662/662 可解析，断链 0，Frontmatter 缺失 0，类型覆盖 8/8，procedures 65、events 115；同名跨类型组 4，有消歧说明 8、无消歧说明 0。
- 关系审计：断链目标 0、非法关系类型 0、缺反向 0、弱证据 0、过连接 0；662 个 KU 均未建立正式 relation。
- 规则漂移审计：closure 刷新后 0 findings；Skill registry 18 个 leaf；空白检查通过。
- 系统升级链：18/18 通过，`behavioral_ready: true`；pytest 266 项通过（failures 0、errors 0、skipped 0）。
- Sync closure：运行 `--refresh-generated --full --check-generated`，第 17/19 步因工作树未提交、9 个生成态文件与 HEAD 不一致而阻断；这是该门禁的设计行为，授权提交后即可转绿。阻断前的 16 步与阻断后单独运行的系统链、pytest 均通过。

## 八、边界与研究债

- 全部条目只依据前六册 Markdown 文本；`consensus` 为 `tentative`，验证层级未评定，图版未视觉核验。
- 12 个新建均只有赵农 2009 单一来源；2 个 update 中短版套印得高丰、赵农两册互证，活字印刷仍为赵农单册（同册两处位置）。丝网印刷仅一句，`confidence` 为 low。
- 拱花未给刻版深度、压印压力、纸张湿度及与短版的先后关系；瓷活字未给挂釉厚度、烧成温度、瓷字强度与印数；石印未给石版材质、药墨配方与机具；线装未给线材、孔距与穿线次序；明长城未给砖石尺寸、灰浆配比、夯层与施工组织；火炮未给炮管壁厚、合金配比、铸模材料与射程；现代造纸未给蒸煮温度压力、药液配比、纸机车速、产量与污染治理；铅字未给合金配比、字号字模与排版工序；照相制版未给网线、感光材料与设备；丝网仅一句；铜版未给版厚、酸液与腐蚀时间；电子照排未给系统型号、字体格式、输出精度与时间节点。
- 结构层仍为 0/4，层级完整挂载 0/662，正式 relation 0 条，Theme／Topic 均未实体化。
- 六册剩余 `needs_evidence` unit 候选 2,411 个，其中 procedure 92 个（田自秉 47、李立新 10、夏燕靖 2016 35）；赵农 procedure 已清零。另有 claim 候选 1,363 个待进入 claim/evidence 流程。
- 下一批应转入田自秉《中国工艺美术史》的 47 个 `procedure` 候选。
- 本批临时脚本（`_tmp_zhaonong_proceduresd_emit.py`、`_tmp_zhaonong_proceduresd_verify.py`、`_tmp_update_zhaonong_proceduresd_manifest.py`、`_tmp_pre_d_huozi-yinshua.md`、`_tmp_pre_d_duanban-taoyin.md`、`_tmp_closure_d.log`、`_tmp_pytest_d.log`、`_tmp_pytest_d.xml` 等）留在 `06-runtime/` 根部，待全阶段收尾时统一清理。
