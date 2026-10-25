# 中国设计史知识蒸馏库

以中国设计史为领域，复用 Knowledge Distillation v5.3.0 的工作流引擎：结构节点、知识元、断言与证据三层架构，来源只读、状态诚实、写回受控。

> 当前状态：**引擎已安装，知识库为空**（0 KU / 0 Theme / 0 Topic）。A–E 是首批摄入用的试运行分析轴，不是已经由证据检验的最终分类。
> 当前版本：v5.3.0（工作流引擎）；本库领域配置 v0.1.0（2026-10-24）。

---

## 一、先看哪里

| 入口 | 路径 |
|---|---|
| 权威总纲 | `AGENTS.md` |
| 工作流路由 | `.agents/pipeline.md` |
| 领域配置 | `01-domain/index.md` |
| 当前领域与边界 | `01-domain/domain-registry.md` |
| 试运行维度 A–E | `01-domain/dimension-registry.md` |
| 领域覆盖规则 | `01-domain/workflow-overrides.md` |
| 来源目录 | `02-sources/_catalog.md` |
| 摄入契约 | `.agents/skills/01-intake/ingest/SKILL.md` |
| KU 字段规范 | `.agents/skills/01-intake/ingest/references/knowledge-unit-field-contract.md` |
| 层级字段规范 | `.agents/skills/01-intake/ingest/references/hierarchy-field.md` |
| 当前机器状态 | `06-runtime/state/current-health.json`（首次审计后生成） |
| 系统升级日志 | `06-runtime/governance/system-upgrade-log.md` |

---

## 二、语料在哪里

原有书籍语料保持原位，工作流不搬动、不改写、不重命名：

| 目录 | 内容 | 角色 |
|---|---|---|
| `00基础书籍-PDF/` | 原始 PDF | provenance，只读 |
| `01基础书籍-章节切分/` | 章节切分 PDF 与 `_章节索引.txt` | provenance，只读 |
| `02基础书籍-minerU解析/` | MinerU 解析产物 | 辅助定位与 OCR 核对，只读 |
| `03基础书籍-md文档/` | 24 册全文 Markdown | **首选阅读文本** |
| `基础书籍清单.md` | 23 种 24 册书目清单 | 书目身份的起点 |

`02-sources/_catalog.md` 已登记 24 册书的 `doc_id` 与来源路径。真正摄入某本书时，才建立：

```text
02-sources/<doc-id>/          来源副本或来源登记
03-processing/<doc-id>/       compact-v4 五件套
```

不得为了目录整齐而复制 5.5 GB PDF，也不得把 MinerU 产物当作全文阅读的替代品。

---

## 三、三层架构

```text
Layer 3 - Structure Nodes
  domain / dimension / theme / topic
  目录: 04-knowledge/structure/

Layer 2a - Knowledge Units
  person / institution / place / work / publication
  term / procedure / event
  目录: 04-knowledge/units/

Layer 2b - Assertion & Evidence
  claim / source / citation / evidence
  目录: 04-knowledge/quality/
```

层级主轴：`domain -> dimension -> theme -> topic -> KU`。Theme 是 Level 3 问题群，Topic 是 Level 4 可研究问题，KU 通过多对多 `topic_memberships` 提供材料。Cluster 只是发现候选，不是结构节点。

---

## 四、第一次运行

要求 Python 3.10+。本机可用：

```powershell
python --version
python -m pip install -e ".[dev]"
```

先跑只读体检：

```powershell
python scripts\audit_repo.py --summary
python scripts\build_runtime_index.py
```

首次体检出现 0 KU、0 Theme、0 Topic 是正常的；它说明引擎能跑，不说明知识库已经建成。

### 摄入第一本书的推荐顺序

建议从体量适中、结构清晰的通史开始，例如高丰《中国设计史》（2004）或陈楠《中国汉字设计史》（2021）。不要一上来全库批处理。

```text
1. 在 02-sources/_catalog.md 确认 doc_id
2. 建立 02-sources/<doc-id>/ 与 03-processing/<doc-id>/
3. 按 ingest skill 完整阅读，写 source-map / semantic-units / candidate-ledger
4. python scripts\validate_processing_package.py 03-processing\<doc-id>
5. 逐候选裁决，只把有证据的候选写入 04-knowledge/
6. python scripts\audit_repo.py --summary
```

正式验证写回必须走：

```text
collect -> evidence JSONL -> dry-run -> python scripts\verify_apply_evidence.py --apply
```

禁止脚本自动提升 confidence、consensus 或 verification 状态。

---

## 五、目录结构

```text
AGENTS.md                 权威总纲
CLAUDE.md                 Claude Code 薄适配入口
.agents/                  workflow router、guards 与唯一 Skill 语义根
.claude/                  Claude Code Hook 与 Skill 发现适配
.codex/                   Codex 项目 Hook 配置（POSIX 写法，Windows 需适配）
.github/                  CI
01-domain/                中国设计史的类型、维度、边界与命名规则
02-sources/               只读来源与书目登记
03-processing/            摄入覆盖证明与候选中间产物
04-knowledge/             units、structure、quality、hierarchy
05-outputs/               查询、写作与展示输出
06-runtime/               派生状态、治理、work package 与评测
scripts/                  受控机械执行器
tests/                    自动化回归测试
00基础书籍-PDF/           原始 PDF（本地语料）
01基础书籍-章节切分/       章节 PDF（本地语料）
02基础书籍-minerU解析/     MinerU 产物（本地语料）
03基础书籍-md文档/         24 册全文 Markdown（本地语料）
COPYS/                    工作流交付副本，安装后可保留作对照
_scripts/                 安装前的语料构建脚本，未纳入工作流
```

---

## 六、Skill 与门禁

18 个 leaf skill 位于 `.agents/skills/`，这是唯一语义权威根。`.claude/skills/` 只是发现入口；本仓库在 Windows 上已建立目录 junction，指向 `.agents/skills/` 对应目录。

常用事件路由：

| 事件 | Skill |
|---|---|
| 新书摄入 | `ingest` |
| 补证与核实 | `enrich` / `verify` |
| 建层级 | `build-hierarchy` / `evolve-hierarchy` |
| 查重与冲突 | `reconcile` |
| 质量检查 | `lint` / `audit-confidence` |
| 查询与写作 | `query` / `compose` |
| 回溯与审查 | `retrospect` / `system-review` |
| 图谱展示 | `knowledge-graph` |

`scripts/agent_guard.py` 是硬门禁；`.claude/settings.json` 在 Windows 上使用 `python` 调用。若客户端未信任项目 Hook，配置文件存在不等于门禁已生效。

---

## 七、Git 注意事项

安装前工作树已存在大量未暂存的目录重组变更（旧 00-基础文献、01-文献md 目录的删除）。因此：

1. **不要**直接 `git add -A` 或 `git add .`，否则会把历史删除、新语料和本次安装混成一个提交。
2. 提交前先按路径分组审阅；本次安装只应包含 `.agents/`、`.claude/`、`.codex/`、`.github/`、`01-domain/`、`02-sources/`、`03-processing/`、`04-knowledge/`、`05-outputs/`、`06-runtime/`、`scripts/`、`tests/`、`AGENTS.md`、`CLAUDE.md`、`README.md`、`pyproject.toml`、`.gitattributes`、`.gitignore`。
3. 语料 PDF 已加入 `.gitignore`；`03基础书籍-md文档/` 是否纳入版本管理由你决定。
4. 提交与推送必须由你明确授权；工作流本身也禁止未经授权的 commit / push。

---

## 八、Windows 说明

- 命令示例使用 `python`；源项目文档里的 `python3` 在 Windows 上可能不存在。
- `.claude/skills/` 使用目录 junction；若复制到另一台机器，junction 可能失效，需要重建。
- `.codex/hooks.json` 仍保留 POSIX 写法；若使用 Codex，请改成 Windows 可执行的命令，或先不使用该 Hook。
- 工作流要求单主线 `main`，不创建功能分支或额外 worktree。安装阶段已在 `main` 工作树上完成，未提交。
