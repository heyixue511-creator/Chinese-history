# 领域配置总入口

本目录保存当前垂直领域的可替换配置。通用规则仍以 `AGENTS.md` 为权威；本目录只定义“中国设计史”这一实例领域的类型、维度、验证和输出偏好。

## 一、当前领域

- **领域名称**：中国设计史
- **核心研究对象**：中国设计实践、设计观念、设计教育、视觉传达与物质文化的历史
- **当前语料**：24 册（23 种）中国设计史、工艺美术史、现代设计史、文字与平面设计、商业美术及相邻领域专著
- **当前知识规模**：以 `06-runtime/state/current-health.json` 的实时扫描为准；首次安装时为 0 KU
- **当前 hierarchy**：v0.1（初始骨架，尚未由 KU 证据检验）
- **基础类型覆盖**：8/8（类型已注册，尚未有实例）
- **当前 Level 2 维度**：5 个试运行维度（A–E）

> 状态说明：A–E 是依据现有书目结构提出的**初始分析轴**，状态为 `pilot`。它们不是已经由知识元反复检验的稳定分类，也不构成对中国设计史学的最终分期或解释框架。首批摄入后必须按 `evolve-hierarchy` 复审。

## 二、配置文件

| 文件 | 职责 |
|---|---|
| `taxonomy-registry.md` | 知识元类型体系：基础类型、候选类型、晋升/合并/弃用规则 |
| `domain-registry.md` | Level 1 Domain：当前实例、候选 Domain 与演化边界 |
| `dimension-registry.md` | Level 2 维度体系：试运行维度、候选维度、拆分/合并/弃用规则 |
| `workflow-overrides.md` | 当前领域的对象、候选、层级演化与状态诚实覆盖规则 |
| `naming-conventions.md` | 目录、文件、Skill 与脚本命名规范 |

## 三、候选观察队列

| 文件 | 职责 |
|---|---|
| `04-knowledge/structure/taxonomy/type-candidates.md` | 类型候选观察队列 |
| `04-knowledge/structure/dimension-candidates.md` | 维度候选观察队列 |

## 四、当前执行约束

1. 不直接新增正式类型。新类型先进入候选观察队列。
2. 不直接新增正式 Level 2 维度。新维度先进入候选观察队列。
3. 能作为 `sub_type` 解决的问题，不晋升为新 `type`。
4. 能作为 Topic 或 Level 3 Theme 解决的问题，不晋升为新 Level 2 Dimension。
5. 类型或维度晋升必须通过 `evolve-hierarchy`、`system-review` 和状态诚实门槛；无人工工作流下由 Agent 写明 evidence、boundary test、hierarchy impact 与 unresolved items。
6. 若通用 Skill 与本领域配置出现可复现冲突，按 `AGENTS.md` 优先级解释并触发 `system-upgrade`，不得长期保留两套活跃规则。
7. 若确认某条领域经验需要升级为系统规则，应移交 `system-upgrade`，而不是只停留在对话中。
8. 中国设计史的核心断言必须能回到本地 `doc_id`、页码/行号或可核对的来源片段；相邻领域材料只能提供上下文，不能未经桥接就冒充设计史证据。

## 五、语料位置与工作流映射

现有书籍语料保持原位，不复制、不移动、不改名：

| 目录 | 内容 | 工作流角色 |
|---|---|---|
| `00基础书籍-PDF/` | 原始 PDF | provenance，只读 |
| `01基础书籍-章节切分/` | 按章节切分的 PDF 与索引 | provenance，只读 |
| `02基础书籍-minerU解析/` | MinerU 解析产物 | provenance / 辅助定位，只读 |
| `03基础书籍-md文档/` | 24 册全文 Markdown | **首选阅读文本**，登记为 `02-sources` 的来源文件 |

`02-sources/_catalog.md` 只登记 `doc_id`、书目信息与来源路径；真正摄入某本书时，再建立 `02-sources/<doc-id>/` 与 `03-processing/<doc-id>/`。不得为了“目录整齐”搬动或重写原始语料。

## 六、状态快照入口

本项目默认按 workflow-first 工作流执行。以下命令只用于生成辅助状态快照，不是领域配置、知识裁决或工作流完成标准：

```powershell
python scripts\audit_repo.py
```

该辅助工具会实时统计：

- 知识元数量和类型覆盖
- 必需字段与推荐字段缺失
- `MIGRATION_TODO` 来源队列
- `UNVERIFIED` 队列
- Markdown 链接和 `local_file` 可达性
- 类型候选信号与维度候选信号
- intake → processing 数据流完整性

语义阅读、类型判断、层级演化和关系裁决仍由 Agent / Skill Contract 处理。
