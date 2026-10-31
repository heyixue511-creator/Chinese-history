# h62 重复候选裁决：11 组同名／同义条目，0 合并、0 别名改写

- 批次：`06-runtime/automation/2026-10-31-reconcile-duplicate-candidates`
- profile：`reconcile-duplicate-candidates-v1`
- 日期：2026-10-31
- 层级版本：v1.51 → **v1.51**（不动结构，不升版）
- 工件：`candidate-ledger.jsonl`（11 条冲突记录）；无 `evidence.jsonl`、无 `apply-plan.jsonl`

## 一、目标与范围

前三批（h44–h61）每批都在 `unresolved` 里保留「重复候选待 reconcile」这一项。本批对全库 2570 个 KU 做一次可复现的同名扫描：按 `title` 与 `aliases` 建索引，凡同一字符串出现在两个文件上即为一组。命中 11 组，逐组读两侧正文后裁决。

**本批不合并任何 KU、不改任何别名、不迁移任何对象。** 依据是 reconcile 契约第 5 条：涉及 merge、alias、same_as 或对象迁移的写回，除术语同一性证据外还须取得明确授权；本批没有当次授权，故只形成裁决记录。

## 二、裁决结果

| 组 | 对象 | 共享名 | 类型 | 裁决 |
|---|---|---|---|---|
| rc-01 | 忍冬纹／唐草纹 | 卷草纹 | 定义 | `parallel_interpretations` |
| rc-02 | 琉璃／玻璃 | 玻璃器 | 对象同一性 | `parallel_interpretations` |
| rc-03 | 珐琅彩／搪瓷 | 洋瓷 | 类型边界 | `resolved` |
| rc-04 | 雕漆／元代漆器装饰技法 | 剔红 | 类型边界 | `resolved` |
| rc-05 | 御器厂／琉璃烧造 | 御窑 | 对象同一性 | `deferred` |
| rc-06 | 孙子（人物）／《孙子兵法》 | 孙子 | 同名 | `rejected` |
| rc-07 | 庄子（人物）／《庄子》 | 庄子 | 同名 | `rejected` |
| rc-08 | 管仲／《管子》 | 管子 | 同名 | `rejected` |
| rc-09 | 荀子（人物）／《荀子》 | 荀子 | 同名 | `rejected` |
| rc-10 | 韩非子／《韩非子》 | 韩非子 | 同名 | `rejected` |
| rc-11 | 河姆渡遗址／河姆渡文化 | 浙江余姚河姆渡 | 类型边界 | `rejected` |

分布：`rejected` 6、`resolved` 2、`parallel_interpretations` 2、`deferred` 1。

## 三、四组的判断依据

**rc-01 忍冬纹／唐草纹（并列）**：忍冬纹的对象是断代与母题都更窄的纹样（六朝流行，取忍冬花枝叶或莲叶演变，东晋北魏后与莲花纹一起进入铜器、金银器、砖瓦、石刻）；唐草纹是以「S」形波状曲线组织方式定义的通名，母题含忍冬、荷花、兰花、牡丹。忍冬是唐草母题之一，二者是包含关系不是同一对象；唐草纹条自身也写「两册对名称来源的表述不同，本条并列不裁断」。故保持两条并立。

**rc-02 琉璃／玻璃（并列）**：琉璃条已自陈两义并列——战国汉文献语境中的「琉璃」即原始玻璃（铅钡玻璃，仿玉代用品），另一义为建筑砖瓦用的铅釉陶。玻璃条收的是现代玻璃材料与现代制造业（石英砂、纯碱、长石、石灰石，吹塑模压，上海起厂、1949 年后多地建厂）。前者是古代器物史写法，后者是现代材料与工业写法。**登记的证据缺口**：琉璃条已引用李立新 2011 册（以「玻璃器」为名写古代玻璃的沉浮序列），但两条 KU 之间无互引关系，读者分查会读到两份互不引用的古代玻璃叙述。

**rc-03 珐琅彩／搪瓷（已裁决为不同对象）**：胎体不同——珐琅彩是瓷胎画珐琅（清宫造办处珐琅作，四册来源），搪瓷是金属胎涂敷珐琅浆（冲压坯胎、洒喷浸渍、热涨系数须与坯胎一致）。二者共享的「洋瓷」是同一俗称在两种历史语境下的指称，不是同一对象。

**rc-04 雕漆／元代漆器装饰技法（已裁决为不同对象）**：前者是跨断代的技法条（别名漆雕、剔红），后者是断代集合条（剔红、剔犀、螺钿三事，单册来源）。剔红同时挂两条别名，实为雕漆的一个品种、也是元代条所列三事之一。

## 四、不做的三件事

1. **不合并**。11 组中没有一组取得对象同一性证明——最接近的 rc-02 也只是「古代器物史」与「现代材料史」两种写法，不是同一描述的两次记录。
2. **不改别名**。5 组存在别名交叉（卷草纹、玻璃器、洋瓷、剔红、御窑）。按契约，别名改写须取得明确授权；本批一律 `apply_authorized: false`，并在 rationale 中写明应改的方向（rc-01 卷草纹应限定为唐草纹的通称；rc-04 剔红应归雕漆条；rc-05 御窑疑为误置）。
3. **不创建冲突知识类型**。11 条记录只存在于本包 `candidate-ledger.jsonl`，不是 `type: conflict`，也不是新的 KU 或 structure node。

## 五、验证

- 扫描可复现：按 `title` + `aliases` 建索引、按完全相等匹配，命中 11 组；未做模糊匹配，故本批不声称「全库无近似重复」，只声称「全库无字面同名重复」。
- 11 条记录采用标准 candidate envelope（`candidate_id`／`candidate_type: unit`／`origin_type: knowledge`／`origin_ref`／`payload`／`evidence_refs`／`state`／`decision`／`created_at`／`updated_at`／`lifecycle_class`），冲突字段全部放在 `payload` 内。**这一步是必需的，不是形式**：`06-runtime/automation/**/candidate-ledger.jsonl` 会被 `build_discovery_index.py` 当作发现来源扫描，本批首次以「冲突记录」格式落盘时即以 exit=1 拦下闭包（缺 candidate_id 等 12 项）。改写后 `build_discovery_index.py` 退出 0，候选索引由 5339 增至 5350。
- 状态映射：`rejected`→state rejected、`deferred`→state deferred、`resolved`／`parallel_interpretations`→state `no_delta`（裁决为保持并列、无写回）。deferred 的 rc-05 按系统规则落为 `lifecycle_class: active`，故 `governance-backlog.md` 新增 `OPP-CANDIDATES`（active discovery candidates 1）——这是**如实**的待办信号，不是本批遗留故障。
- 无写回 → 无 `apply-plan.jsonl`；`hierarchy_stress_test.py` 期望值不变（v1.51、107、884、868、1702）。
- 保护路径 `02-sources/` 零改动；分支 `main`、单一 worktree。
- **本包不 commit、不 push**——commit/push 需用户当次明确授权。

## 六、未决事项与下一跳

1. **别名治理需单独授权**：5 组别名交叉（rc-01、rc-02、rc-03、rc-04、rc-05）的正确归属已在 rationale 中写明，但改写属 merge/alias 门槛内，需用户明确授权后才能执行。
2. **rc-05 待补句证**：琉璃烧造条把「御窑」列为别名，需回到其两处来源逐句核对；本批未取得可定位原句，故 `deferred`。
3. **古代玻璃两条互引缺失**（rc-02）：琉璃条与玻璃条之间应建立 `related` 或互见说明，属 relation 写回，同样需要授权与 dry-run。
4. **下一跳**：图注待核 12 条与未核图版（5-32、8-57、8-58、10-48、图 4-32「铁犁」归属、图 8-14「清式紫檀大宝座」）→ A 维度遗留（A.1.2 命名逐条对照、1917 年许衍灼《中国工艺史沿革史》）→ 存量债务（未挂载 1702、隔离 1057、单源 1919、low 496、tentative 2570）。
