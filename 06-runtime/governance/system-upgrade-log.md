# 系统升级记录

## 工作流复刻初始化

- 原工作流按字节复刻，来源及哈希见 `COPYS/workflow-copy-manifest.json`。
- 新增空数据目录与复用说明，不复制源项目知识和历史验收结果。
- 未执行新领域语义适配，未初始化 Git，未启用或验证客户端 Hook。
- 复制与回归验证结果见交付文件夹的 `validation-report.json`。

## 中国设计史库安装（2026-10-24）

- 将工作流引擎安装到 `D:\中国设计史研究` 根目录，保留原有 `00–03` 书籍语料、`_scripts` 与 `COPYS` 不动。
- 领域配置从“信息可视化史与信息图表史”改为“中国设计史”：
  - Domain slug：`chinese-design-history`；
  - A–E 维度改为首批摄入的 `pilot` 分析轴；
  - 新增中国设计史的证据边界与语料映射规则。
- `02-sources/_catalog.md` 登记 24 册书，状态均为 `registered`，尚未摄入。
- `05-outputs` 重建为中国设计史的空图谱页面；不再保留源项目的书目、统计数字和封面资产。
- `.claude/skills/` 在 Windows 上由相对路径 stub 改为目录 junction，指向 `.agents/skills/`。
- `.claude/settings.json` 改用 `python`，Hook 匹配加入 `PowerShell`；`scripts/agent_guard.py` 改为按 UTF-8 读取 Hook 输入，并支持 PowerShell 工具名。
- `.gitignore` 增加现行 PDF / 章节切分 / MinerU 语料忽略规则，避免误提交约 5.5 GB 语料。
- 清理源项目领域残留：verify 的领域判断、taxonomy 命名示例、外部 API User-Agent 改为中国设计史语境。
- 中文专名命名规则改为：有通行英文名时用英文，否则用无声调、小写、短横线分隔的汉语拼音，姓名按“姓-名”顺序；不再禁止拼音。
- 建立初始派生状态：`current-health.json`、`candidate-index.jsonl`、`discovery-manifest.json`、`generated-projections-manifest.json`、输出画廊与浏览导航；输出登记将知识图谱和导航页标为 `rejected`（派生展示，不产生知识写回候选）。
- Git 远程抓取 refspec 收紧为仅 `main`：`+refs/heads/main:refs/remotes/origin/main`。
- 最终收口：`250 passed, 16 subtests passed`；规则漂移 0；18 个 Skill 通过注册校验；结构契约体检 115/130，其中 `traceability` 为 0/15，原因是尚未摄入任何 KU。
- 未提交、未推送；安装前已存在大量未暂存的目录重组变更，需分组审阅后再决定提交范围。
- 未声明知识成熟度或学术验收通过；当前为 0 KU 初始状态。
