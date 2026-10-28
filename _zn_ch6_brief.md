# 第六章 KU 写作 brief（赵农 2009 册）

## 你只写指定的文件

- 只创建或更新分配表里列出的目标文件；不改动任何其他文件。
- 不新建目录，不删除文件，不 commit，不 push。
- 不使用网络，不引入来源之外的知识；一切内容必须来自指定行段。

## 来源

`03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md`（只读，UTF-8）。
第六章范围为 L4108-L4941。

先 Read 指定行段，逐句核对；不得只依据候选摘要写作。

## frontmatter 模板（新建）

```yaml
---
title: 中文名（English Name）
name_en: English Name
type: term
sub_type: garment_form
term_original: 中文名
term_zh: 中文名
academic_translation_status: provisional
translation_note: 采用通行译名 English Name；来源未提供英文名，不另拟意译。
tags:
  - 隋唐
  - 服饰
aliases: []
sources:
  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L4610."
    location: "L4610"
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
hierarchy_scope_note: 一句话说明本条为何落在该维度；Theme/Topic 尚未 materialize。
---
```

- `type` 只能是 person / institution / place / work / publication / term / procedure / event。
- person 加 `name_original`、`language_original: zh`、`name_zh`、`translation_status: provisional`、`translation_note`；按需 `birth_death: 未载`、`nationality`、`period`、`occupation`、`contribution_scope`。
- work 加 `title_original`、`title_original_language: zh`、`title_zh`、`translation_note`；按需 `creator`、`year`、`format`、`location`、`dimensions: 未记`、`collection: 未记`。
- publication 加 `title_original`、`title_original_language: zh`、`title_zh`、`translation_note`；按需 `author`、`publication_year`、`edition`。
- term 加 `term_original`、`term_zh`、`academic_translation_status: provisional`、`translation_note`；按需 `aliases`、`term_note`。
- 日期、版本、consensus、evidence_status 固定如上；`confidence` 按分配表。
- `primary_dimension` 只能是 A/B/C/D/E。需要时写 `secondary_dimensions`。
- tags 3–6 个，取自来源实际出现的历史时期、材质、用途、人物等。

## 正文固定六节

```markdown
## 描述

（3–6 句，概括对象、来源记述范围与未载事项。）

## 核心内容

- **要点名（Lxxxx）**: “逐字引文”。
- **要点名**: 概括性说明，不加引号。
- **原文未载**: ……

## 在层级体系中的位置

- primary_domain: chinese-design-history
- primary_dimension: B（造物、工艺与生产技术）
- primary_theme: 未建立；Theme 尚未 materialize
- topic_memberships: 无；Topic 尚未 materialize
- role_in_theme: 未定
- scope_note: 与 frontmatter 的 hierarchy_scope_note 同义复述。

## 相关知识元

`works/xxx.md` 记……；`terms/yyy.md` 记……。relation 未审查，不写入正式 `relations`。

## 验证状态

- 证据状态: source_backed（赵农 2009 册内复读）
- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7
- 验证平台: 未使用外部平台
- 匹配质量: 逐条说明命中了哪些行、给出什么、缺什么，并说明 confidence 依据。
- 验证日期: 2026-10-26
- 证据范围: 仅赵农 2009 册 Markdown 文本 Lxxx-Lxxx；未做来源外核对

## 参考文献

1. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009.
```

## 引文与用字硬规则

1. 逐字引文用 `“ ”`；**每个 `“` 必须有同行的 `”` 配对**，不得跨行。
2. 校正写法、拼接句、压缩改写、自拟概括用 `「 」`，不得用 `“ ”`。
3. 正文（frontmatter 之外）**禁止 ASCII 双引号 `"`**；嵌套引号用 `‘ ’`。
4. `“ ”` 内的文字必须能在赵农册原文中找到（去掉标点与空白后比对）；错一个字就会被审计脚本判 MISS。
5. 原文疑似错字：照录 `“原文如此”`，随后用 `「 」` 标出疑误写法，并写“照录标疑，不径改”。不得直接改字。
6. 跨页、跨图注断句：分别引两段，用 `「 」` 说明拼合；不得伪造成一句连续引文。
7. 来源没有的事实一律不写。人物生卒、尺寸、数量、出土地、收藏地缺失时写“未载”。

## 内容纪律

- 不写“规格”“confidence 依据”“按规格表”等批次内部用语。
- 不写“本候选”“candidate”“批次”等流水线词汇。
- 不做来源外考证、不比较其他书、不引用其他书。
- 图版未做视觉核验：涉及图的条目在正文明确“图版未核，不据图补写形制、纹样与尺寸”。
- `## 相关知识元` 只写分配表给的相关 KU 路径；路径必须真实存在，反引号内用 `type/slug.md`。
- 每条正文 60–120 行为宜，短条目可更短；不得为凑长度重复。

## 更新既有条目的额外规则

- 只在既有正文上追加，不删除、不改写原有来源的表述。
- `sources` 新增一条赵农 citation（放在末尾）；`source_count` 加 1；`version` 加 1；`updated`、`last_verified` 改为 2026-10-26；`review_due` 改为 2027-04-26。
- `confidence` 若因新材料而上调，需在验证状态说明；不得下调。
- `## 核心内容` 追加带（赵农 2009，Lxxxx）的条目；`## 验证状态` 的匹配质量与证据范围补入赵农行段；`## 参考文献` 追加赵农。
- 六节顺序与既有小节不得重排。

## 交付

写完后自查：
- 六节齐全，frontmatter 字段齐全；
- 正文无 ASCII 双引号；
- 所有 `“ ”` 引文可在指定行段中找到；
- 所有反引号 KU 链接存在；
- 不虚构任何事实。
