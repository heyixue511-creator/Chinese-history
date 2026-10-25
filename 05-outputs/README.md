# 输出产物层说明

本目录只承载**知识库与内容产出物**。

允许放在这里的内容：

- `drafts/`：蒸馏报告与摄入快照
- `exports/`：面向知识使用的导出物
- `index/`：面向知识浏览与检索的内容导航
- `output-registry.yml`：没有 bundle-local metadata 的输出元数据登记表
- `index/output-gallery.md`：file-back 状态总览（由 `build_output_gallery.py` 生成）

## 知识图谱

- `knowledge-graph.html`：当前二维主入口，读取 `knowledge-graph-data.*`。
- `knowledge-graph-2d.html`：二维快照入口，读取独立的 `knowledge-graph-2d-data.*`。
- `knowledge-graph-data.json` / `.js`：由 `scripts/build_knowledge_graph_data.py` 从 KU、正式层级与权威 relation index 生成。
- `vendor/d3.v7.9.0.min.js`：本地 D3 运行时，页面不依赖网络。

当前图谱是**空图**（0 节点、0 关系），因为知识库尚未摄入第一批书籍。页面会明确显示空状态，不用示例节点填充。

知识图谱只呈现 KU-to-KU 关系；结构节点不伪装成知识元。缺失 Theme 或 Topic membership 的 KU 显示为待组织，不根据相似度或画面位置推断归属。

## 不应放在这里的内容

- 系统状态
- 治理待办
- Hook 日志
- 系统升级日志
- 系统审查报告
- 脚本运行记录

这些内容统一放入 `06-runtime/`。
