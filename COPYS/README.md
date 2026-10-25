# 工作流系统完整复刻

已将当前项目的完整工作流导出为 **knowledge-distillation-workflow.zip**。先将压缩包解压到原仓库之外的独立目录，再阅读包内 `REUSE.md`。

采用 ZIP 隔离，是因为原仓库的 Skill 检查器会发现嵌套目录中的第二套 `SKILL.md`。压缩包不会成为当前项目的第二套活跃规则。

## 交付内容

- [完整工作流包](knowledge-distillation-workflow.zip)：约 2.92 MiB，235 个文件；保留原目录结构和隐藏配置目录。
- [复用说明](reuse-guide.md)：系统工作流、目录说明、领域适配、Python、Claude 链接、Hook 和 Git 门禁说明。
- [文件来源与哈希清单](workflow-copy-manifest.json)：187 个原文件与 47 个新增模板/辅助文件逐项区分；清单自身另计 1 个文件。
- [归档校验值](SHA256SUMS.txt)：ZIP 的 SHA-256。
- [验证报告](validation-report.md)、[机器可读报告](validation-report.json)：复制完整性、隔离测试及未验证项。
- `verify_copy.py`：不解压也可检查 ZIP 内每个文件的完整性。
- `build_workflow_copy.py`：从当前源仓库重新导出的可复现工具；默认拒绝覆盖已有 ZIP，明确传入 `--replace` 才更新本导出包。
- `validate_export.py`：在系统临时目录中解压并验证整个交付包。
- `run_portable_tests.py`：包内 `portable/run_tests.py` 的源文件；以包内版本作为使用入口。

## 复刻范围

完整保留 `AGENTS.md`、`CLAUDE.md`、`.agents/pipeline.md`、18 个 Skills、全部参考契约与 guards、Codex/Claude 适配、41 个 Python 执行脚本、39 个 Python 测试文件、领域配置、依赖声明、CI，以及图谱展示代码与本地静态依赖。

18 个 Skills：`system-upgrade`、`ingest`、`verify`、`audit-confidence`、`lint`、`reconcile`、`build-hierarchy`、`enrich`、`evolve-hierarchy`、`synthesize`、`compose`、`query`、`retrospect`、`encoding-check`、`inspector`、`read-full`、`system-review`、`knowledge-graph`。

本次保持源系统完整，没有采用此前对话中已撤回的功能取舍，也没有把当前讨论写成新规则。研究资料、知识单元、实际关系、旧工作包与历史验收状态未随系统迁移；只提供空的数据目录和明确标记的新项目模板。

## 验证结果

- 187 个原文件均与当前源文件匹配，复制差异为 0。
- 包内 234 个被清单覆盖的文件均通过哈希检查，ZIP CRC 正常。
- 18 个 Skills 的唯一性、脚本依赖、参考契约和注册表检查通过。
- 隔离测试：**250 项通过，16 个子测试通过**。5 个依赖原领域数据的用例使用临时合成 fixture，原执行脚本、测试和断言均未修改。
- 测试后重新核对包内文件，哈希仍一致。

这证明复制完整和测试行为可复现，不表示新领域已适配、客户端 Hook 已启用或新知识库已通过发布门禁。源领域配置、页面文案和环境命令需要按 `reuse-guide.md` 适配。

## 快速检查

在本目录运行：

```powershell
python -X utf8 -B verify_copy.py knowledge-distillation-workflow.zip
```

在解压后的新目录运行：

```powershell
python -m pip install PyYAML pytest
python -X utf8 -B portable/verify_copy.py .
python -X utf8 -B scripts/skill_registry.py
python -X utf8 -B portable/run_tests.py
```

只向当前项目新增了 `COPYS/`，未修改原工作流、知识或来源，未提交或推送。
