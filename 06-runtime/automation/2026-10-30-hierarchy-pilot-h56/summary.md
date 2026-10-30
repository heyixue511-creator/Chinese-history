# h56 层级试点：另立 Theme B.18「前近代服饰与冠服等级」并建立 Topic B.18.1／B.18.2／B.18.3

- 批次：`06-runtime/automation/2026-10-30-hierarchy-pilot-h56`
- profile：`hierarchy-pilot-v1`
- 日期：2026-10-30
- 层级版本：v1.46 → **v1.47**
- apply-plan：31 行；changed_files 39

## 一、目标与范围

本批把「前近代服饰」从连续三批登记的债务变成结构节点。闭合对象是四处已落盘文本：

1. h53–h55 summary 与 manifest 反复登记的下一跳「前近代服饰与甲胄等级 Theme」。
2. B.9.6 边界：「甲胄与服饰等级的关系归服饰 Topic」。
3. B.9.6 正文：「秦代服饰、两裆衫等服装条目不在本 Topic 挂载」。
4. B.18 之外无处可归的事实：D.2 只管 1912 年前后的服制改革，E.5 只管改制动因与族群身份，B.2 只管 1840 年以后的织绣与服装工艺。

不并入 D.2 的理由：D.2 的两条 Topic 是「剪辫易服与服制改革」「中山装与国家礼服」，问题都是「服制如何被近代制度改写」；本批二十三条的问题全是「服物本身如何被写成等级或形制」，时代也全部在前近代。不并入 E.5 的理由：E.5 的边界明写只取「功能对礼仪的冲击」与「汉化中的改制」两类动因，胡服、孝文改制一类条目正是本批明确排除的对象。

## 二、结构物化

- **Theme B.18**「前近代服饰与冠服等级：冕服、深衣、袍衫、裙制与甲胄」：`theme_code=B.18`、`primary_dimension=B`、`secondary_dimensions=[C, D, E]`、`status=pilot`、`source_basis` 六册。正文五节齐备，核心问题一问加三个具体问题，边界九条、支撑结构四层、未解决问题十条。
- **Topic B.18.1**「冕服与冠服等级：冕服制度、冕冠与冕旒、祎衣、霞帔与燕居服」：`primary_dimension=B`、`parent_theme=B.18`、`secondary_themes=[D]`、`status=pilot`、`source_count=4`。研究问题：**等级在六册里是一套可数的符号，还是一套可穿的服物？**
- **Topic B.18.2**「上衣下裳与深衣形制：原始服装、深衣、袍服与汉代成衣」：`secondary_themes=[C, D]`、`source_count=6`（六册全覆盖）。研究问题：**从原始服装到深衣这条主线，在六册里是靠形制名连成的，还是靠实测数据连成的？**
- **Topic B.18.3**「袍衫袄襦与两裆：隋唐圆领袍、北朝短衣与元代辫线袄」：`secondary_themes=[D]`、`source_count=3`。研究问题：**短衣与袍衫在六册里是一条连续谱系，还是八个各自命名的名目？**

层级主轴仍为 `domain → dimension → theme → topic → KU`；B.18 是第 33 个 Theme，B.18.1／B.18.2／B.18.3 是第 102、103、104 个 Topic。

## 三、23 条 membership：全部为主挂载

| KU | 类型 | role | 归属 |
|---|---|---|---|
| [冕服制度](../../../04-knowledge/units/terms/mianfu-zhidu.md) | term | `term_anchor` | B.18.1 主挂载 |
| [冕冠与冕旒](../../../04-knowledge/units/terms/mian-guan-mian-liu.md) | term | `term_anchor` | B.18.1 主挂载 |
| [祎衣](../../../04-knowledge/units/terms/yiyi.md) | term | `term_anchor` | B.18.1 主挂载 |
| [晋武帝司马炎冕服](../../../04-knowledge/units/works/jin-wudi-simayan-mianfu.md) | work | `representative_work` | B.18.1 主挂载 |
| [霞帔](../../../04-knowledge/units/terms/xiapei.md) | term | `term_anchor` | B.18.1 主挂载 |
| [燕居服](../../../04-knowledge/units/terms/yanju-fu.md) | term | `term_anchor` | B.18.1 主挂载 |
| [原始服装](../../../04-knowledge/units/terms/yuanshi-fuzhuang.md) | term | `term_anchor` | B.18.2 主挂载 |
| [秦代服饰](../../../04-knowledge/units/terms/qin-dai-fu-shi.md) | term | `term_anchor` | B.18.2 主挂载 |
| [汉代袍服](../../../04-knowledge/units/terms/han-dai-pao-fu.md) | term | `term_anchor` | B.18.2 主挂载 |
| [深衣](../../../04-knowledge/units/terms/shenyi.md) | term | `term_anchor` | B.18.2 主挂载 |
| [禅衣](../../../04-knowledge/units/terms/chanyi.md) | term | `term_anchor` | B.18.2 主挂载 |
| [素纱禅衣](../../../04-knowledge/units/works/susha-chanyi.md) | work | `representative_work` | B.18.2 主挂载 |
| [马王堆贵夫人辛追服饰](../../../04-knowledge/units/works/xinzhui-fushi.md) | work | `representative_work` | B.18.2 主挂载 |
| [龙凤虎纹绣衣](../../../04-knowledge/units/works/longfenghuwen-xiuyi.md) | work | `representative_work` | B.18.2 主挂载 |
| [集宁路刺绣夹衫](../../../04-knowledge/units/works/jininglu-cixiu-jiashan.md) | work | `representative_work` | B.18.2 主挂载 |
| [圆领袍衫](../../../04-knowledge/units/terms/yuanling-paoshan.md) | term | `term_anchor` | B.18.3 主挂载 |
| [杂裾垂髾服](../../../04-knowledge/units/terms/zaju-chuishao-fu.md) | term | `term_anchor` | B.18.3 主挂载 |
| [比甲](../../../04-knowledge/units/terms/bijia.md) | term | `term_anchor` | B.18.3 主挂载 |
| [袄](../../../04-knowledge/units/terms/ao.md) | term | `term_anchor` | B.18.3 主挂载 |
| [辫线袄](../../../04-knowledge/units/terms/bianxian-ao.md) | term | `term_anchor` | B.18.3 主挂载 |
| [襦](../../../04-knowledge/units/terms/ru.md) | term | `term_anchor` | B.18.3 主挂载 |
| [衫与两裆衫](../../../04-knowledge/units/terms/shan-liang-dang-shan.md) | term | `term_anchor` | B.18.3 主挂载 |
| [衲裆](../../../04-knowledge/units/terms/na-dang.md) | term | `term_anchor` | B.18.3 主挂载 |

- 主挂载 23、次挂载 0。与 B.16（主 3 次 4）、B.17（主 12 次 0）相比，本批是第三批「纯主挂载」Theme：二十三条在库中全部没有其他 Theme 的主归属。
- role：`term_anchor` 18、`representative_work` 5；类型 term 18、work 5。
- 来源（按 KU 计，跨册重复计入）：赵农 2009 十、夏燕靖 2016 十、夏燕靖 2009 六、田自秉 2010 三、高丰 2004 二、李立新 2011 二；六册全覆盖，`source_count` 6（按册计）。单册来源 19 条、三册 3 条（霞帔、素纱禅衣、圆领袍衫）、五册 1 条（深衣）。
- confidence：medium 18、low 5（祎衣、晋武帝司马炎冕服、禅衣、比甲、袄）；consensus 全部 tentative。

## 四、边界处置

`excluded_by_boundary` 已写入 manifest，十二条。其中四条需要点明：

1. **近代服制不入**：剪辫易服、《剪辫通令》、《服制条例》、中山装、国家礼服归 D.2；B.18 的「前近代」不是修辞，是边界——B.18 与 D.2 的分界是 1912 年前后的服制改革，不是「是否谈制度」。
2. **改制动因不入**：胡服、胡服骑射、孝文改制、孝明帝服饰改革归 E.5。B.18.3 只在袄、衲裆、两裆衫三条中记录「北方游牧」「缘起于铠甲」一类的形制来源句，不展开族群身份问题。
3. **甲胄本体不入**：汉代铠甲、明光铠、筒袖铠、皮甲归 B.9.6 与待建鞋履甲胄 Topic；B.18.3 只用两裆衫「形制缘起于铠甲」一句作服饰与护具的唯一连接，不以一句代替甲胄结构。
4. **名称带「帽」字的不按名称归**：毗卢帽经读条目确认实为清代架子床顶沿的雕饰式样（赵农），属家具装饰，归 B.14；初选名单曾误列为首服，读后撤回。

**待建登记**：裙制 7 条（裙、襦裙、裥裙、石榴裙、羊肠裙、安乐公主羽裙、晕絰提花锦裙）、首服与妆饰 6 条（幅巾、幞头、顾姑冠、假髻、佛妆、帔子）、鞋履与甲胄 4 条（履的种类、云头锦鞋、花盆底鞋、皮甲）共 17 条，已摄入且全部无 `primary_theme`，本批按分批原则未挂载，登记在 Theme 边界与未解决问题中。

## 五、执行与验证

- 写回：`h56_mount.py` 输出 `mounted 23 bad []`；frontmatter 复核 23 条全部 `primary_theme: B.18`、各含 1 条 `topic_memberships`（`primary: true`）、`secondary_themes` 镜像原 `secondary_dimensions`（B.18.1 中三条为 `[D]`、三条无；B.18.2 中四条 `[D]`、三条 `[C]`、两条无；B.18.3 中三条 `[D]`、五条无）、`version` 各 +1（深衣与圆领袍衫由 2 升至 3）、`updated` 全部改为 2026-10-30、无残留 `尚未 materialize` 占位。
- 索引升版四处：`hierarchy/index.md` → v1.47（Theme 32→33、Topic 101→104、Level 5 851/1719/865、double-mount 清单维持 14 条、追加 v1.47 段）；`themes/README.md`（33、代码表补 B.18、新增 B.18 全段）；`topics/README.md`（104、B.18 下 3 个、新增三段）；`dimension-candidates.md`（五十六批 851、B 未挂载 1004、全库 1719）。**旧版先归档**为 `hierarchy/archive/v1.46.md`（100130 字节），再编辑 index.md。
- 实测：`hierarchy_stress_test.py` 报 themes 33、topics 104、membership 865、complete 851、incomplete 1719、`cross_dimension_topics` 为空、`apply_permitted: false`；`build_relation_index.py` 7714（explicit 5998、inferred 1716、3/67）；`audit_relation_consistency.py` broken 0、invalid 0、missing inverse 0、weak evidence 0、isolated 1071、over-connected 10；`write_current_health.py` structural 130/130、ksq 58/65（`hierarchy_assignment` 3/10）、content 0、`system_p0=0`。
- **一处按实测纠错必须记录**：第一次重建关系索引只增 40 条而非 46 条。原因是 B.18.1 的 Topic 文件名含「yu」（`...xiapei-yu-yanju.md`），而 6 条主挂载按 `...xiapei-yanju.md` 写入，`_materialized_structure_target` 因目标文件不存在而跳过 topic 边，只剩 theme 边。改正 6 条 KU 的 topic 路径后重建得 46，与推导一致。结构体化阶段「文件已建」不等于「路径已对」，本轮以实测差数发现，未靠推理设想。
- **生成态次序**：`run_sync_closure.py --refresh-generated --full` 的第 8 步早于第 9 步，relation 数变化后单跑一次会残留 `output_navigation_snapshot_stale`，必须连续跑两次；本批按此处理。
- `--check-generated` 为 17 步，第 17 步 `git diff --exit-code HEAD` 在未 commit 时必然 exit=1，属预期。

## 六、指标变化

| 指标 | v1.46 | v1.47 | 变化 |
|---|---|---|---|
| Theme | 32 | **33** | +1 |
| Topic | 101 | **104** | +3 |
| topic_memberships | 842 | **865** | +23 |
| complete assignments | 828 | **851** | +23 |
| incomplete assignments | 1742 | **1719** | −23 |
| double-mount KU | 14 | 14 | 0 |
| relation index | 7668 | **7714** | +46 |
| member_of / inferred | 1670 | **1716** | +46 |
| explicit | 5998 | 5998 | 0 |
| 隔离单元 | 1084 | **1071** | −13 |
| B 维度未挂载 | 1027 | **1004** | −23 |
| structural health | 130/130 | 130/130 | 0 |
| ksq | 58/65 | 58/65 | 0 |

**一处非整数推导，必须按实测记录：**

- 隔离单元减 13 而非 23：23 条中有 10 条原本已有显式关系、不属隔离，只有 13 条由隔离转为有边，取自 `audit_relation_consistency.py` 前后两次实测。

## 七、语义边界：并列不裁与不做的事

本批的判断是「并列照录」而非「择优裁定」：

1. **三个 Topic 的分法是本库安排，不是来源结论**：六册按自己的章节结构写服饰（晋式、宋式、便装、女服、短衣、冠服），从无一段把「等级」与「形制」并置讨论；B.18 按「这件衣物在六册里回答什么」切三刀，是结构判断。同一朝代（汉、宋、明）的条目因此分属不同 Topic。
2. **两裆衫与衲裆并列不裁**：赵农作「两裆衫，前后为两片布衣，在肩部用布带连缀」；夏燕靖 2009 作「衲裆用两片组成，前片挡胸、后片挡背，肩上以搭襻联结」。描述近同而名称不同，本库并列照录，不判定为同物异名。
3. **霞帔两说并列不合并**：时代（宋／明）与形态（深青缎地禽纹／彩带连缀金玉坠子）两个层面均不同源，两说并列，不取其一。
4. **深衣三处分歧只记录不校订**：起始时代三说、直裾归属两说、服用者等级两说，均属形制归类问题；《礼记》原本未核，不据转引文字校订任何一说。
5. **毗卢帽撤回**：初选按名称含「帽」列入首服候选，读条目后确认实为床饰，撤回并写入 Theme 边界——名称不是分类依据，这是本批的一处自我修正。

不做的事：不从形制名推版型。「续衽钩边」「曲裾绕襟」「横襕」「细褶缝衲」六册都只有文字而无裁片图、缝份与拼接线，本库不据四字或五字复原结构；也不把素纱禅衣的 128 厘米与 49 克回填到其他汉代衣物条目。

## 八、生成态与门禁

- 次序：manifest 与 summary 先落盘，再跑闭包。
- 全量闭包连续两次后，`rule_drift.findings` 归 0、backlog 为「No active items」。
- `--check-generated` 17 步，第 17 步 exit=1 属预期（未 commit）。
- 保护路径 `02-sources/` 零改动；分支 `main`、单一 worktree；HEAD 仍为 `c249c6fe`。
- **本包不 commit、不 push**——commit/push 需用户当次明确授权。

## 九、未决事项与下一跳

本批 12 条 unresolved 已写入 `manifest.json`，要点归四类：

**证据结构类**
- 等级与形制不共段：无一条同时给出等级规则与衣物尺寸；五种等级载体（制度、数、配伍、色、图像）各由一条承担且互不引用。
- 成衣实测只有一件：素纱禅衣，且袖长两册相差 10 厘米、测量方式均未注明。
- 服饰与护具只在一处相接：两裆衫「形制缘起于铠甲」一句，与皮甲条从未互引。

**名实类**
- 两裆衫／衲裆同物与否未裁；霞帔时代与形态两说未合；袄、襦、衫、袍四者的服用场合与裁法只在名目上分开。

**用量化类**
- 全 Theme 唯一带数字的成衣是素纱禅衣；其余二十二条零衣长、零袖宽、零用料、零工时。可数的只有旒数（12／9／8／6）、冕板尺寸（7 寸 × 1 尺 2 寸）、霞帔品级（一至七品）与丝织品出土规模（两说）。

**结构自陈类**
- 三个 Topic 的分法、B.18 的「前近代」边界与本批 23 条的选择范围，均为本库读法；裙制 7 条、首服 6 条、鞋履甲胄 4 条共 17 条待建。

**下一跳优先级**：跨批文本回改批次（B.14.7 → B.17.1、B.12.2／B.13.2／B.5.3 → B.16.1、B.12 → B.15、B.9「货币归后续 Topic」→ B.13、B.14.3 边界材料侧 → B.14.7、B.9.6 → B.18）→ 裙制 Topic（7 条，本 Theme 后续最大单批）→ 重复候选 reconcile 9 组与图注待核 12 条。
