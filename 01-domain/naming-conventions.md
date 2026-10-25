# Naming Conventions v1.0

> 本文件定义仓库的目录、文件、Skill 与脚本命名规范。
> 所有新增与重构必须遵守。历史中文混名在后续迁移中逐步替换。

## 一、目录命名

```
数字前缀 + 英文主名（kebab-case）

根级:
  01-domain/        # 领域配置
  02-sources/       # 原始来源
  03-processing/    # 处理中间层
  04-knowledge/     # 知识库
  05-outputs/       # 输出产物
  06-runtime/       # 系统运行

Skill 阶段:
  00-coordination/
  01-intake/
  02-multisource/
  03-verification/
  04-relations/
  05-quality/
  06-growth/
  07-output/
  08-inspection/
  09-display/
```

**禁止**:
- 中文规则文件名
- 空格
- `phase` / `final` / `temp` / `old` / `new` 命名
- 阶段名和功能名混用

**历史语料例外**：`00基础书籍-PDF/`、`01基础书籍-章节切分/`、`02基础书籍-minerU解析/`、`03基础书籍-md文档/` 是安装前已存在的只读书籍语料，保留中文目录名与中文文件名，不在迁移时改名。新增的 workflow 文件、KU、Theme、Topic 仍须遵守本规范。

## 二、文件命名

统一 **kebab-case**。

```
correct: reading-ledger.md, claim-registry.yml, relation-governance.md
wrong:   Step6_Methodology_Report.md, old-settings.json, final-v2.md
```

## 三、Skill 命名

```
.agents/skills/<stage-id>-<stage-name>/<skill-name>/SKILL.md
.agents/skills/<stage-id>-<stage-name>/<skill-name>/references/<topic>.md

示例:
.agents/skills/00-coordination/system-upgrade/SKILL.md
.agents/skills/01-intake/ingest/SKILL.md
.agents/skills/01-intake/ingest/references/taxonomy.md
```

Skill 目录名使用 **英文 kebab-case**，不使用中文。触发词映射在 `AGENTS.md` 中维护。

## 四、Script 命名

| 前缀 | 含义 | 默认权限 |
|------|------|----------|
| `audit_*` | 只读审计/检查 | allow |
| `build_*` | 只读索引生成 | allow |
| `scan_*` | 只读扫描 | allow |
| `collect_*` | 证据收集 | confirm |
| `validate_*` | 只读校验 | allow |
| `apply_*` | 写回操作 | confirm/deny |
| `migrate_*` | 历史迁移（已完成） | deny |
| `repair_*` | 一次性修复（已完成） | deny |
| `backfill_*` | 一次性回填（已完成） | deny |
| `normalize_*` | 一次性规范化（已完成） | deny |

## 五、知识文件命名

```
Knowledge Unit: {slug}.md         # gao-feng.md / changxin-palace-lantern.md
Structure Node:  {name}.md        # dimension-a.md
Claim Registry:  claim-registry.yml
Relation Index:  relation-index.yml
```

**中文专名转写**：有通行英文名或权威英文译名时优先使用英文名；没有时使用无声调、小写、短横线分隔的汉语拼音，姓名按“姓-名”顺序。不得用拼音改写已有规范英文名（如用 `london.md`，不用 `lundun.md`）。

**禁止**:
- 在文件名中显式加 type 标签（如 `gao-feng-person.md`）
- 使用 `/` 连接独立概念
- 中文文件名

## 六、迁移规则

从中文混名迁移到英文时:
1. 先生成 `path-reference-map.md`
2. 逐目录移动（不一次全部迁移）
3. 全局 grep + replace 路径引用
4. 引用量最大的目录（`04-knowledge/`）放最后
5. 每步单独提交
