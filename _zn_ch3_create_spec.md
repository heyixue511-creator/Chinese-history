# 任务规格：为赵农《中国艺术设计史》（2009）第三章新建知识元

## 语料（只读）

- 文件：`03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md`
- doc_id：`2009-zhaonong-zhongguo-yishu-shejishi`
- 只允许读，不得改写、移动、删除。

## 工作方式

1. 先读你负责的候选所在行（见任务清单），定位该实体自己的段落；行跨度常是整节，不代表整节都属该实体。
2. 读 1–2 个同类既有条目作格式范本（见下），照其字段与语气写。
3. 只写清单指定的目标文件；不得修改其他任何文件，不得运行 git、不得改候选索引。
4. 写完后自查：六节齐全、正文无 ASCII 双引号、`## 相关知识元` 中每个反引号路径都真实存在。

## Frontmatter 规范

### term

```yaml
---
title: 中文名（English Name）
name_en: English Name
type: term
sub_type: weapon
term_original: 中文名
term_zh: 中文名
academic_translation_status: provisional
translation_note: 采用……译名；来源未提供英文名。
tags:
  - 标签
aliases:
  - 别名
sources:
  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L1234."
    location: "L1234"
    evidence_ref:
      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi
      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md
      chapter_id: null
      chunk_id: null
created: 2026-10-26
updated: 2026-10-26
confidence: medium
consensus: tentative
source_count: 1
last_verified: 2026-10-26
review_due: 2027-04-26
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: B
hierarchy_scope_note: "……。Theme/Topic 尚未 materialize。"
---
```

### person

用 `name_original`、`language_original`、`name_zh`、`translation_status` 替代 term 的 `term_*` 字段组。范本：`04-knowledge/units/persons/fu-hao.md`。

### work

用 `title_original`、`title_original_language`、`title_zh`，并按需加 `medium`、`format`、`year`。范本：`04-knowledge/units/works/qin-gong-bo.md`。

### publication

用 `title_original`、`title_original_language`、`title_zh`。范本：`04-knowledge/units/publications/jiaguwen-bian.md`。

## 正文六节（顺序与标题固定）

```markdown
## 描述

## 核心内容

## 在层级体系中的位置

## 相关知识元

## 验证状态

## 参考文献
```

- `## 描述`：2–4 句，说清是什么、来源在本节怎么讲；不写来源没有的内容。
- `## 核心内容`：条目化，每条尽量带行号；可用 `**小标题**` 分组。
- `## 在层级体系中的位置`：固定六条 bullet：
  - `- primary_domain: chinese-design-history`
  - `- primary_dimension: B（造物、工艺与生产技术）`（如确有需要可改 C/A，但须在 scope_note 说明）
  - `- primary_theme: 未建立；Theme 尚未 materialize`
  - `- topic_memberships: 无；Topic 尚未 materialize`
  - `- role_in_theme: 未定`
  - `- scope_note: ……`
- `## 相关知识元`：一段话，反引号路径必须是已存在文件；结尾写 `relation 未审查，不写入正式 \`relations\`。`
- `## 验证状态`：固定 bullets：
  - `- 证据状态: source_backed（来源内复读）`
  - `- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7`
  - `- 验证平台: 未使用外部平台`
  - `- 匹配质量: ……（说明哪几行给了什么、缺什么、confidence 依据）`
  - `- 验证日期: 2026-10-26`
  - `- 证据范围: 仅赵农 2009 册 Markdown 文本 L……；未做来源外核对`
- `## 参考文献`：`1. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009.`

## 引文规则（最重要）

- 逐字原文用 `“ ”`。
- 以下情况一律用 `「 」`：通行字形／校正写法、压缩改写、自拟概括、被图版或标题隔断的拼接句。
- 嵌套内层用 `‘ ’` 或 `「 」`。
- 正文里禁止出现 ASCII 双引号 `"`；ASCII 双引号只允许出现在 YAML 的 citation/location 值里。
- 每个 `“ ”` 引文必须能在赵农原文中逐字找到（允许跨行拼接，但拼接处不能插入原文没有的字）。
- 原文错字、重复字、内部矛盾：照录并标「原文如此／疑为某字」，不得径改。

## confidence 判定

- `medium`：该实体有 2 条以上实质事实（形制、尺寸、工艺、用途、出土等）。
- `low`：只有一句、只有图注、或材料主要依附他事。
- 不写 `high`（单源）。

## 事实边界

- 不补来源之外的年代、尺寸、收藏、器形、纹饰。
- 图注只作“图某为某”的记录，不据图补器形；未核图要写明。
- 若来源只有图注，`匹配质量` 要说明“仅图注，无正文描述”。

## 交付报告（最后一条消息）

按目标逐条列出：

```
路径 | cid | confidence | 引用行号 | 一句话内容 | 发现的原文字形/错字/矛盾 | 使用的相关 KU 路径
```

并单列：无法确定或需要主代理裁决的问题。
