# 类型候选观察队列

> 本文件只记录尚未晋升为正式 Knowledge Unit 类型的观察项，不是 taxonomy 本体。

## 当前状态

- 正式基础类型：8/8（person / institution / place / work / publication / term / procedure / event），见 `01-domain/taxonomy-registry.md`。
- 候选项：0。
- 尚无摄入知识元，因此没有可据以提出的新类型候选。

## 记录规则

| 字段 | 要求 |
|---|---|
| 候选类型 | 暂定英文 slug 与中文名 |
| 触发证据 | 至少 3 个无法归入现有 8 类的 KU 候选，附 doc_id 与定位 |
| `sub_type` 测试 | 说明为何不能作为现有类型的子类型解决 |
| 关系影响 | 对 relation schema、索引页和图谱颜色的影响 |
| 状态 | `observing` / `promoted` / `merged` / `rejected` |

没有证据时保持 0 条；不得为了类型表好看而新增类型。
