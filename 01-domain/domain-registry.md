# Domain Registry — 领域演化注册规则

Domain 是五级主干的 Level 1，总结一套能够独立提出问题、组织分析维度并持续吸收来源的研究领域。当前只 materialize “中国设计史”，但数量不是永久上限。

## 一、层级关系

```text
Domain -> Dimension -> Theme -> Topic -> KU
```

- Domain 定义总问题域和纳入/排除边界。
- 一个 Domain 必须能够稳定组织多个 Dimension。
- 跨 Domain 的 KU 或 Topic 使用关系与辅助归属表达，不复制知识元。

## 二、当前 Domain 边界

**纳入范围**

- 中国境内的设计实践、造物活动、工艺技术、视觉传达与设计观念；
- 设计教育、设计机构、设计出版、设计展览与设计政策；
- 与传统工艺、近现代商业美术、平面与文字设计、产品与器物设计相关的历史材料；
- 中国设计史自身的史学书写、分期方式、核心概念与研究方法。

**排除范围**

- 纯美术史、纯美学史、纯机械史的独立叙事：只有在能说明其与设计实践、设计观念或设计制度的明确关系时，才作为上下文或桥接证据纳入；
- 与设计无关的政治史、军事史、文学史事件；
- 无法回到具体来源的概括性判断。

**相邻领域处理**

中国近现代美术史、美学文库、机械史等材料属于相邻领域。它们可以作为历史上下文、制度背景或技术条件进入证据层，但必须在 claim 中写明桥接理由，不得直接当作“设计史事实”。

## 三、Domain Candidate 条件

只有同时满足以下条件，才可提出新 Domain：

1. 新知识无法在不稀释现有 Domain 边界的情况下自然归入；
2. 已形成独立核心研究问题，而不只是一个新 Theme 或 Dimension；
3. 能稳定组织至少 2 个 Dimension，每个 Dimension 已有 Theme、Topic 与 KU/claim/evidence 支撑；
4. 得到多个独立来源持续支持，并通过反例与边界测试；
5. 已说明与现有 Domain 的重叠、迁移、跨域关系和查询价值。

Cluster 密度、共享标签或来源数量只能召回 Domain Candidate，不能自动创建 Domain。

## 四、生命周期

```text
candidate -> needs_evidence -> ready_for_review -> approved
         -> pilot -> active | merged | split | deprecated
```

审批与结构迁移由 `evolve-hierarchy` 执行。历史 Domain 标识必须保留映射，KU 不因 Domain 调整而复制。

## 五、当前 Domain

| slug | 名称 | 状态 |
|---|---|---|
| `chinese-design-history` | 中国设计史 | active |

## 六、变更记录

- 2026-10-24：建立中国设计史 Domain；替代源项目的 `information-visualization-history-and-theory`。此时尚无 KU，状态为初始骨架，不是已由证据闭合的领域模型。
