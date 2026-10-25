# 知识图谱数据格式规范

> 本文件只定义格式。以下 JSON 中的节点、关系与统计均为**占位示例**，不是本库已录入的知识。

## JSON 结构

```json
{
  "nodes": [{
    "id": "example-institution",
    "title": "示例机构",
    "name_en": "Example Institution",
    "type": "institution",
    "type_zh": "机构",
    "color": "#8B5CF6",
    "tags": ["示例标签"],
    "confidence": "high|medium|low",
    "consensus": "confirmed|tentative|debated",
    "sub_type": "子类型",
    "source_count": 1,
    "evidence_status": "验证状态",
    "primary_domain": "chinese-design-history",
    "secondary_domains": [],
    "primary_dimension": "D",
    "primary_theme": "D.1",
    "secondary_themes": [],
    "role_in_theme": "key_institution",
    "topic_memberships": [{"topic": "topics/example-topic.md", "theme": "D.1", "role": "key_institution"}],
    "hierarchy_scope_note": "示例：说明该机构为何归入此 Theme。",
    "description": "示例描述，不是本库事实。",
    "path": "04-knowledge/units/institutions/example-institution.md"
  }],
  "links": [{
    "source": "example-institution",
    "target": "example-person",
    "relation_type": "权威 relation vocabulary 中的关系类型",
    "relation_source": "explicit|inferred_by_rule|migrated_from_related",
    "review_status": "关系审查状态",
    "confidence": "high|medium|low",
    "evidence_ref": {}
  }],
  "structure": {
    "domains": [{"id": "chinese-design-history", "code": "chinese-design-history", "title": "中国设计史"}],
    "dimensions": [{"id": "a-design-historiography", "code": "A", "title": "设计史观与史学方法"}],
    "themes": [{"id": "example-theme-slug", "code": "A.1", "title": "示例 Theme，尚未 materialize"}],
    "topics": [{"id": "example-topic", "code": "example-topic", "parent_theme": "A.1", "title": "示例 Topic，尚未 materialize"}]
  },
  "stats": {
    "total_nodes": 0,
    "total_links": 0,
    "relation_index_total": 0,
    "skipped_non_unit_relations": 0,
    "by_type": {"person": 0, "institution": 0, "place": 0, "work": 0, "publication": 0, "term": 0, "procedure": 0, "event": 0},
    "hierarchy": {
      "domain_assigned": 0,
      "dimension_assigned": 0,
      "theme_assigned": 0,
      "topic_assigned": 0
    },
    "structure_nodes": {"domains": 0, "dimensions": 0, "themes": 0, "topics": 0}
  }
}
```

`structure.*` 的计数来自已 materialize 的结构文件，不是配置层登记数。因此：

- `01-domain/` 中的中国设计史 Domain 与 A–E 试运行维度，在没有对应结构文件时，`structure_nodes` 仍为 0；
- 页面可以在配置层显示“1 个领域、5 个试运行维度”，但必须与已物化计数分开说明；
- 不得为了让页面好看而把配置登记冒充结构文件。

## 数据生成器

`scripts/build_knowledge_graph_data.py` — 从 `04-knowledge/units/` 提取全部知识元，读取 `04-knowledge/structure/` 的正式层级，以 `04-knowledge/quality/relation-index.yml` 为唯一关系来源，并只生成：

- `05-outputs/knowledge-graph-data.json`：机器可读 JSON。
- `05-outputs/knowledge-graph-data.js`：供 `file://` 直接打开 HTML 时读取的同内容脚本。

## 展示实现与依赖

- `05-outputs/vendor/d3.v7.9.0.min.js`：固定版本的本地 D3 运行时；页面不得依赖远程脚本或字体。
- `05-outputs/knowledge-graph.html`：当前 D3 二维主入口，读取 `knowledge-graph-data.*`。
- `05-outputs/knowledge-graph-2d.html`：冻结的 D3 二维快照入口，读取独立的 `knowledge-graph-2d-data.*`。
- `05-outputs/knowledge-graph-2d-manifest.json`：冻结二维快照的入口、数据、D3 依赖与 SHA-256 边界。

`knowledge-graph-2d-manifest.json` 是输出完整性清单，不是 runtime R2 provenance manifest。`hash_mode: sha256-lf-normalized-v1` 要求计算前把 CRLF 规范化为 LF，以保证 Windows 与 Linux 检出结果一致。

层级字段只呈现仓库中已正式写入的挂载。缺失 `primary_theme` 的知识元进入“待组织空间”；缺失 `topic_memberships` 时不得根据相似度或画面需要虚构 Topic。

`structure.*[].id` 是结构文件的稳定 slug，显示与布局匹配必须优先使用 `code`。例如 Theme 文件 `a1-example-theme.md` 的 `id` 为文件名 slug，而正式层级键是 `code: A.1`。
