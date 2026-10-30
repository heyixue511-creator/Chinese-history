# h55 层级试点：另立 Theme B.17「竹材与编织工艺」并建立 Topic B.17.1／B.17.2

- 批次：`06-runtime/automation/2026-10-30-hierarchy-pilot-h55`
- profile：`hierarchy-pilot-v1`
- 日期：2026-10-30
- 层级版本：v1.45 → **v1.46**
- apply-plan：19 行；changed_files 27

## 一、目标与范围

本批把「竹材工艺」从连续两批登记的债务变成结构节点。闭合对象是三处已落盘文本：

1. h54 summary 第九节下一跳：「竹编工艺方法（`procedures/zhubian-yishu-jiagong`，仍无 `primary_theme` 与 `topic_memberships`）」。
2. h54 manifest 的下一跳登记同一句。
3. B.14.7 主题文件边界与 hierarchy v1.43 段：「不收竹编工艺体系（`procedures/zhubian-yishu-jiagong` 仍未挂载）」。

不并入 B.14（家具）的理由：B.14.7 只取章水泉竹家具一条，竹家具的问题是「家具怎样以竹代木」，与编织、雕刻共用材料却不同问题；也不并入 B.5（陶器）或 B.9（金属）的器物装饰节，因为竹编与竹刻的条目从不出现在这两条线的技术叙述中。

## 二、结构物化

- **Theme B.17**「竹材与编织工艺：席、竹编、竹刻与藤器」：`theme_code=B.17`、`primary_dimension=B`、`secondary_dimensions=[C, D]`、`status=pilot`、`source_basis` 六册。正文五节齐备。
- **Topic B.17.1**「编织：苇席、绳索、竹编五法与地方品类」：`primary_dimension=B`、`parent_theme=B.17`、`secondary_themes=[D]`、`status=pilot`、`source_count=3`。研究问题：**编织线把方法写成五句定义、把材料写成八类、把产地写成八个地名，唯一带数字的是新石器遗物的尺寸与件数——编织在六册里是被写成「一套做法」，还是被写成「一些产地和品类」？**
- **Topic B.17.2**「刻竹：嘉定派、金陵派与嘉定三朱」：`primary_dimension=B`、`parent_theme=B.17`、`secondary_themes=[C]`、`status=pilot`、`source_count=1`。研究问题：**两个流派共用四句刀法形容（深刻透雕／用刀较浅、勾勒数刀／不事刀斧／刀不苟下），七条中只有一件器物且以图注 low confidence 立条——竹刻在六册里是以「流派」被写，还是以「刀法」被写？**

层级主轴仍为 `domain → dimension → theme → topic → KU`；B.17 是第 32 个 Theme、B.17.1 与 B.17.2 是第 100 与第 101 个 Topic。

## 三、12 条 membership：全部为主挂载

| KU | 类型 | role | 归属 |
|---|---|---|---|
| [编织](../../../04-knowledge/units/procedures/bianzhi.md) | procedure | `procedure` | B.17.1 主挂载 |
| [手工编织](../../../04-knowledge/units/terms/shougong-bianzhi.md) | term | `term_anchor` | B.17.1 主挂载 |
| [竹编艺术加工方法](../../../04-knowledge/units/procedures/zhubian-yishu-jiagong.md) | procedure | `procedure` | B.17.1 主挂载（原无 Theme，本批闭合的债务） |
| [龚玉璋](../../../04-knowledge/units/persons/gong-yuzhang.md) | person | `key_person` | B.17.1 主挂载 |
| [广东南海藤厂](../../../04-knowledge/units/institutions/guangdong-nanhai-tengchang.md) | institution | `key_institution` | B.17.1 主挂载 |
| [嘉定派](../../../04-knowledge/units/terms/jiading-school.md) | term | `term_anchor` | B.17.2 主挂载 |
| [金陵派](../../../04-knowledge/units/terms/jinling-school.md) | term | `term_anchor` | B.17.2 主挂载 |
| [朱鹤](../../../04-knowledge/units/persons/zhu-he.md) | person | `key_person` | B.17.2 主挂载 |
| [朱小松](../../../04-knowledge/units/persons/zhu-xiaosong.md) | person | `key_person` | B.17.2 主挂载 |
| [朱三松](../../../04-knowledge/units/persons/zhu-sansong.md) | person | `key_person` | B.17.2 主挂载 |
| [濮仲谦](../../../04-knowledge/units/persons/pu-zhongqian.md) | person | `key_person` | B.17.2 主挂载 |
| [嘉定朱小松竹刻香薰](../../../04-knowledge/units/works/jiading-zhu-xiaosong-bamboo-censer.md) | work | `representative_work` | B.17.2 主挂载 |

- 主挂载 12、次挂载 0。与 h54 的 3+4 结构相反：竹材条目在六册中没有一条已有其他 Theme 的主归属，故不存在次挂载。
- role：`procedure` 2、`term_anchor` 3、`key_person` 5、`key_institution` 1、`representative_work` 1；类型 procedure 2、term 3、person 5、institution 1、work 1。
- 来源（按 KU 计，跨册重复计入）：田自秉 2010 11、赵农 2009 2、夏燕靖 2016 1；`source_count` 3（按册计）。高丰 2004、夏燕靖 2009、李立新 2011 零覆盖。
- confidence：medium 10、low 2（广东南海藤厂、嘉定朱小松竹刻香薰）；consensus 全部 tentative。

## 四、边界处置

`excluded_by_boundary` 已写入 manifest，九条。其中四条需要点明：

1. **竹纸与竹简不入**：`terms/zhu-zhi` 归造纸线，简牍归 C.2；本 Theme 只取器物编织与雕刻，不取纤维加工与书写材料。
2. **名称带「竹」的书不入**：《竹谱》《竹书纪年》《十竹斋笺谱》《十竹斋画谱》归文献与印刷线；本库不按书名用字归并。
3. **以竹为纹样的器物与图像不入**：竹林七贤画像砖、竹林七贤和荣启期砖画、珐琅彩竹菊鹌鹑瓶、鎏金银竹节高柄铜薰炉分别归 B.5、B.6、B.9；纹样与器物形态不是竹材工艺。
4. **章水泉竹器不重挂**：已主挂 B.14.7，竹家具的问题属家具线；本版只在边界中记明，不迁移其主归属。

## 五、执行与验证

- 写回：`h55_mount.py` 输出 `mounted 12 bad []`；frontmatter 复核 12 条 `primary_theme: B.17`、各含 1 条 `topic_memberships`（`primary: true`）、`secondary_themes` 镜像原 `secondary_dimensions`（B.17.1 五条为 `[D]`、B.17.2 七条为 `[C]`），无残留 `尚未 materialize` 占位。
- 索引升版四处：`hierarchy/index.md` → v1.46（Theme 31→32、Topic 99→101、Level 5 828/1742/842、double-mount 清单维持 14 条、追加 v1.46 段）；`themes/README.md`（32、代码表补 B.17、新增 B.17 全段）；`topics/README.md`（101、B.17 下 2 个、新增 B.17.1 与 B.17.2 两段）；`dimension-candidates.md`（五十五批 828、B 未挂载 1027、全库 1742）。**旧版先归档**为 `hierarchy/archive/v1.45.md`（95917 字节），再编辑 index.md——此为 h54 归档次序失误后的改正。
- 实测：`hierarchy_stress_test.py` 报 themes 32、topics 101、membership 842、complete 828、incomplete 1742、`cross_dimension_topics` 为空、`apply_permitted: false`；`build_relation_index.py` 7668（explicit 5998、inferred 1670、3/67）；`audit_relation_consistency.py` broken 0、invalid 0、missing inverse 0、weak evidence 0、isolated 1084、over-connected 10；`write_current_health.py` structural 130/130、ksq 58/65（`hierarchy_assignment` 3/10）、content 0、`system_p0=0`。
- **生成态次序**：`run_sync_closure.py --refresh-generated --full` 的第 8 步早于第 9 步，relation 数变化后单跑一次会残留 `output_navigation_snapshot_stale`，必须连续跑两次；本批按此处理。
- `--check-generated` 为 17 步，第 17 步 `git diff --exit-code HEAD` 在未 commit 时必然 exit=1，属预期。

## 六、指标变化

| 指标 | v1.45 | v1.46 | 变化 |
|---|---|---|---|
| Theme | 31 | **32** | +1 |
| Topic | 99 | **101** | +2 |
| topic_memberships | 830 | **842** | +12 |
| complete assignments | 816 | **828** | +12 |
| incomplete assignments | 1754 | **1742** | −12 |
| double-mount KU | 14 | 14 | 0 |
| relation index | 7644 | **7668** | +24 |
| member_of / inferred | 1646 | **1670** | +24 |
| explicit | 5998 | 5998 | 0 |
| 隔离单元 | 1093 | **1084** | −9 |
| B 维度未挂载 | 1039 | **1027** | −12 |
| structural health | 130/130 | 130/130 | 0 |
| ksq | 58/65 | 58/65 | 0 |

**一处非整数推导，必须按实测记录：**

- 隔离单元减 9 而非 12：12 条中有 3 条原本已有显式关系、不属隔离，只有 9 条由隔离转为有边，取自 `audit_relation_consistency.py` 前后两次实测。

## 七、语义边界：并列不裁与不做的事

本批的判断是「并列照录」而非「择优裁定」：

1. **两条线并置是本库安排**：田自秉把竹编放在「编织工艺」节、竹刻放在「雕塑工艺」节，相隔数百行互不引用；B.17 把二者置于同一 Theme 并由「竹被劈成丝／被整段保留」切分两个 Topic，是结构判断，不是来源判断。
2. **两派刀法照录不裁**：嘉定「以深刻及透雕见长」与金陵「用刀较浅，刀法简洁」是方向相反的形容，六册不给深浅尺度、通透程度与刀法图示，也不作两派作品并置；本库只照录这两句，不据此判定哪一派更「工」。
3. **流派与人物并立不合并**：嘉定派条已含三朱与秦一爵、沈大生，人物条各只一到两句专长；本批按条目分立照录，是否应保留四条人物条记入未解决问题。
4. **藤编组织锚点不扩写**：「解放后建立了许多大型的藤编工艺厂，广东南海藤厂就是其中的一个」一句承担藤编的全部组织信息，「大型」无量化标准，本库不据一句补写产量、厂址与所有制。

不做的事：不从「五法」推工艺参数。五法各一句定义、刻竹五个形容，六册无篾丝宽度、编织密度、刀形、进刀角，因此「哪种做法更精」在本 Theme 内不可比较，本库不据名称补写参数。

## 八、生成态与门禁

- 次序：manifest 与 summary 先落盘，再跑闭包。
- 全量闭包连续两次后，`rule_drift.findings` 归 0、backlog 为「No active items」。
- `--check-generated` 17 步，第 17 步 exit=1 属预期（未 commit）。
- 保护路径 `02-sources/` 零改动；分支 `main`、单一 worktree；HEAD 仍为 `c249c6fe`。
- **本包不 commit、不 push**——commit/push 需用户当次明确授权。

## 九、未决事项与下一跳

本批 12 条 unresolved 已写入 `manifest.json`，要点归四类：

**证据结构类**
- 两条线从不并读：六册无一段把编与刻放在一起，也不说明同一竹材为何一边劈丝、一边整段保留。
- 刻竹线全部出自一册一段：B.17.2 七条均来自田自秉 2010 L4472-L4477（正文一段加插图 11 图注），六条互为子集，无第二册交叉。
- 只有一件器物：朱小松竹刻香薰以图注 `confidence: low` 立条，尺寸、形制、纹样、款识、藏地全缺，图版未核。

**量化类**
- 量化只落在遗物与用工：苇席 1 平方米、绳索 1.2 厘米与 2—3 毫米、钱山漾 200 多件、龚扇穿丝几百至 1 000 次以上；无篾丝宽度、经纬密度与工时定额；刻竹线零量化。

**结构自陈类**
- 「竹材」作为一个 Theme 是本库读法：来源按章节分置「编织工艺」与「雕塑工艺」，两条线的组织单位相反（做法／人），本版并置二者并自陈这一刀。
- 流派条与人物条内容互为子集，四条人物条是否必要待后续来源复核重估。

**跨批债务**
- B.14.7 边界「不收竹编工艺体系（`procedures/zhubian-yishu-jiagong` 仍未挂载）」未回改指向 B.17.1。
- h54 登记的 B.12.2／B.13.2／B.5.3「简单机械线尚未物化」与 B.12「归待建水利 Topic 或 B.3」仍未回改。

**下一跳优先级**：前近代服饰与甲胄等级 Theme → 跨批文本回改批次（B.14.7、B.12.2、B.13.2、B.5.3、B.12、B.9「货币归后续 Topic」、B.14.3 边界材料侧指向 B.14.7）→ 重复候选 reconcile 9 组与图注待核 12 条。
