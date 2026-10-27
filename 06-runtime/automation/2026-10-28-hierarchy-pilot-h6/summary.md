# h6 批次摘要：T5 D 维度「近代城市、建筑制度与职业」的 D.3 物化

- 批次：`2026-10-28-hierarchy-pilot-h6`
- 日期：2026-10-28
- 层级版本：v0.6 → v0.7
- 结论：新增 1 个 Theme、2 个 Topic，主挂载 8 个 KU；16 个变更文件，16/16 哈希匹配。未 commit、未 push。

## 一、目标与范围

h5 已把 T5「建筑、城市与室内设计」的 B 维度部分 materialize 为 B.3。本批处理同一归并主题的 D 维度部分，建立 D.3「近代城市、建筑制度与职业」：

- D.3.1 近代城市与规划制度；
- D.3.2 建筑研究、建材流通与装饰业。

至此 T5 已按 B／D 两个主维度完成试点拆分：B.3 解释材料、结构、立面、内部空间与纪念性如何形成；D.3 解释城市制度、研究机构、建材流通与装饰业如何组织。E 维度「外来式建筑」术语仍待 E 类 Theme，T5 不因 B／D 已挂载而声称整体闭合。

## 二、结构物化

新增 Theme `04-knowledge/structure/themes/d3-jindai-chengshi-jianzhu-zhidu-zhiye.md`：

- `node_type: theme`
- `theme_code: D.3`
- `primary_domain: chinese-design-history`
- `primary_dimension: D`
- `secondary_dimensions: [B, E]`
- `status: pilot`

新增 Topic：

| Topic | 研究问题 | 支撑 KU |
|---|---|---|
| D.3.1 近代城市与规划制度 | 租界、特别市、首都计划与市中心区域规划如何把近代城市空间纳入制度安排，城市规划又怎样成为设计史的研究对象？ | 上海、南京、广州、上海市市中心区域规划 |
| D.3.2 建筑研究、建材流通与装饰业 | 中国营造学社与朱启钤如何组织建筑古籍整理和实地测绘，盖茨公司与亚平艺术装饰公司又如何把建材供应、室内装饰与商业美术连成设计市场？ | 中国营造学社、朱启钤、盖茨公司、亚平艺术装饰公司 |

两 Topic 按「城市制度—建筑研究／装饰业」分工，不重复计入同一 KU。

## 三、8 个 KU 的挂载与语义决定

8 个 KU 全部为单主挂载、`secondary_themes: []`、`primary: true`，写入 `updated: 2026-10-28`；`last_verified` 不改。

### D.3.1（4 个）

- **上海**（place，`geographical_context`）：以开埠、租界制度、1927 年上海特别市与《建国方略》浦东规划为锚点；租界行政、警察、监狱、驻军与租界—棚户区二元结构是本 Topic 的核心材料。1949 年后浦东开发只作边界说明；西方建筑输入仍归 E 次维度。
- **南京**（place，`geographical_context`）：以 1928 年「首都计划」与中山陵、总统府大门、中央博物院等规划期建筑为锚点。六朝建康、明初都城、南洋劝业会等前近代内容不并入本 Topic。
- **广州**（place，`geographical_context`）：以 17 世纪以来的通商口岸定位与 1901–1911 年织布工场为锚点，观察外来贸易、近代工场与城市空间的连接；汉代船模、明代船厂、外销瓷与广式家具属 B 维度，不并入本 Topic。
- **上海市市中心区域规划**（publication，`source_publication`）：以「为提倡国粹起见，市府新屋应用中国式建筑」一句为锚点，观察规划条文如何推动中国固有式建筑；只有一句转述，规划原件未核，confidence 维持 low。

### D.3.2（4 个）

- **中国营造学社**（institution，`key_institution`）：1925 年朱启钤发起「营造学会」，1930 年改名中国营造学社，整理出版《园冶》《梓人遗制》，在河北、山西、山东实地测绘，1946 年停止活动。梁思成《中国建筑史》已归 B.3.2，不重复挂载。
- **朱启钤**（person，`key_person`）：以营造学会／中国营造学社组织工作与 1927 年据日本钞本刊刻《髹饰录》为锚点；其建筑研究组织者身份是本 Topic 的主线，漆艺文献整理作并行材料。
- **盖茨公司**（institution，`key_institution`）：20 世纪初上海南京路的装饰材料供应商，代理石材、瓷砖、壁纸、夹板，并在《建筑月刊》广告中承诺免费样品、报价与对外国监理的技术支持；建材品类归 B、外资代理归 E 次维度。
- **亚平艺术装饰公司**（institution，`key_institution`）：业务横跨广告、商标盒样、橱窗、染织图案、油漆路牌、舞台布置、门面与室内装饰、家具设计、制版等，说明近代上海设计业务尚未按专业分化；其广告业务涉及 C 维度，但原 KU 未列 C 次维度，本批不新增。

字段处理：南京、朱启钤、亚平艺术装饰公司、上海市市中心区域规划原先没有 `secondary_dimensions`，本批显式写为 `[]`；上海、广州、中国营造学社、盖茨公司保留原有次维度，不因挂入 D.3 而改写主维度。所有 `secondary_themes` 为空，因为 B.3 与 D.3 的交叉关系已在 Theme 正文说明，但尚未建立可引用的正式次 Theme 挂载。

## 四、执行与验证

- `scripts/hierarchy_stress_test.py`：v0.7，8 Theme、18 Topic、106 membership、105 complete、2465 incomplete、`cross_dimension_topics: []`、`apply_permitted: false`。
- `scripts/audit_content_quality.py`：总发现 0。
- `scripts/audit_repo.py`：EXIT=0，断链 0，Frontmatter 0，类型值不匹配 0，同名消歧 10/10。
- `scripts/run_sync_closure.py --refresh-generated --full`：18/18，`250 passed, 16 subtests passed`。
- `apply-plan.jsonl`：16 行（3 个 structure_node_create、8 个 hierarchy_mount、5 个 structure_index_update），16/16 `after_sha256` 重新计算匹配。
- 结构健康 130/130；知识结构质量 55/65，`hierarchy_assignment` 仍为 0，这是 2465 个 KU 未挂载的覆盖度信号，不是本批新增结构错误。

## 五、指标变化

| 指标 | h5 后 v0.6 | h6 后 v0.7 | 变化 |
|---|---:|---:|---:|
| Theme | 7 | 8 | +1 |
| Topic | 16 | 18 | +2 |
| Topic membership | 98 | 106 | +8 |
| 完整挂载 KU | 97 | 105 | +8 |
| 未挂载 KU | 2473 | 2465 | −8 |
| Relation 总数 | 6193 | 6209 | +16 |
| `member_of` | 195 | 211 | +16 |
| 隔离单元 | 1473 | 1470 | −3 |
| 结构健康 | 130 | 130 | 0 |
| 知识结构质量 | 55/65 | 55/65 | 0 |
| 内容质量发现 | 0 | 0 | 0 |
| KU / claim / candidate / translation | 2570 / 1242 / 5339 / 2178 | 同左 | 0 |

`member_of` 增加 16 而不是 8：每个 KU 为 `role_in_theme` 生成 1 条 Theme 关系，为 `topic_memberships` 生成 1 条 Topic 关系。隔离单元只减少 3，表示另外 5 个 KU 原本已有其他显式关系；不能据此推断它们已被充分研究。

## 六、语义边界

- 本批只证明 105 个 KU 完成五级字段挂载，不证明 2570 个 KU 全量挂载，也不证明 D.3 已是稳定分类。
- D.3 是 `pilot` Theme，不表示 T5 已验收或结构闭合；E 维度「外来式建筑」术语仍未 materialize。
- 2465 个未挂载 KU 仍是研究债务；`structure_node_coverage` 仍为 2/4，因为 Domain 与 Dimension 尚未 materialize。
- 上海、南京、广州三个城市条目各自覆盖较长时段，本批只取近代段；古代都城、秦汉造船、外销瓷与广式家具不因城市名并入 D.3。
- 中国营造学社与朱启钤同据赵农一段，组织章程、经费、成员总数与测绘对象清单缺失；不把两人的材料写成完整制度史。
- 盖茨公司与亚平艺术装饰公司只证明存在材料代理与综合装饰业务，不证明行业规模、专业分化程度或客户结构。
- 建筑教育、建筑师执业制度、营造厂与建筑事务所尚无独立 KU；本批不能声称近代建筑职业已完整覆盖。
- 规划图纸、城市地图与建筑照片尚未视觉核验。

## 七、生成态与门禁

- `06-runtime/automation/index.md` 与 `06-runtime/state/generated-projections-manifest.json` 由完整闭包刷新；本批新增 3 个 runtime 文件（`apply-plan.jsonl`、`manifest.json`、`summary.md`），预计索引为 209 个批次目录、1105 个文件。
- h6 尚未 commit，发布门禁 `--refresh-generated --check-generated` 预期在 `[17/17] check generated snapshots` 以 `EXIT=1` 结束，状态为 `blocked_pending_commit`；这不是内容失败，而是未提交状态下的预期结果。
- 本批未 commit、未 push；外部状态变更等待用户当次明确授权。

## 八、未决事项与下一跳

1. **E 维度**：`wailaishi-jianzhu` 主维度为 E，暂不挂载；归并报告把 E 视为跨主题的维度标签，不单列 Theme，故 T5 只完成 B／D 两个主维度，不预设 E Theme。
2. **1949 年后建筑**：人民大会堂、北京十大建筑、国徽、1961 年文章不并入 D.3。
3. **T6/T7**：设计教育/职业/机构、传统工艺的近代命运尚未 materialize；本批发现的建筑教育、执业制度与营造厂缺口应进入 T6 候选。
4. **存量挂载**：2465 个 KU 仍缺五级字段；单源 1919、tentative 2570、低置信 496、隔离 1470 继续作为研究债。
5. **待复核**：三城条目的规划档案与地图、上海市市中心区域规划原件、中国营造学社章程与经费、盖茨公司与亚平艺术装饰公司的创办人与存续时间。
6. **既有欠账**：qian-juntao 重复、shenghuo-weekly 的 C.1.2 回填、h4 排除项复审，均未在本批处理。
