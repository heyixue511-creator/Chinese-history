---
title: 中国设计史层级知识体系
version: 0.1
date: 2026-10-24
status: initial
evaluation_baseline: 0 KU
---

# 中国设计史层级知识体系 v0.1

## 当前状态

- Level 1 Domain：`chinese-design-history`（中国设计史），配置见 `../../../01-domain/domain-registry.md`。
- Level 2 Dimension：A–E 五个 `pilot` 分析轴，配置见 `../../../01-domain/dimension-registry.md`。
- Level 3 Theme：0 个，尚未 materialize。
- Level 4 Topic：0 个，尚未 materialize。
- Level 5 KU：0 个，尚未摄入。

## 结构原则

```text
domain -> dimension -> theme -> topic -> KU
```

- A–E 是首批摄入用的试运行维度，不是最终分期，也不是已经由知识元证明的分类。
- Theme 必须由稳定问题群形成，不能为了填满结构而创建空 Theme。
- Topic 是可研究、可回答的问题，不得由相似度或页面布局自动生成。
- KU 通过多对多 `topic_memberships` 支持 Topic；缺失挂载保持为研究债务。
- Cluster 只是发现候选，不写入本目录。

## 版本边界

v0.1 只表示“初始骨架已登记”，不表示结构闭合、层级验收通过或知识成熟。首批摄入后，按 `build-hierarchy` 建立 Theme/Topic，再由 `evolve-hierarchy` 复审 A–E 的边界与命名。
