# 处理摘要：中国设计艺术史论（李立新，2011）

- **doc_id**：`2011-lilixin-zhongguo-sheji-yishu-shilun`
- **处理 profile**：`compact-v4`
- **来源**：`03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md`
- **输入指纹**：`sha256:76a0d14b9bcc29b56170cb15c9a16cc62b8dc21d504970dfd805bc6168370f99`
- **状态**：`completed`（独立语义复读完成；结论 `accepted_with_findings`）

## 覆盖

- source blocks：149，已读/已合并/已排除：149，未读：0
- 无候选且无排除理由的块：0
- 复读范围：2495/2495 行（`full_asset`，单一全文资产）
- semantic units：221
- candidates：534（unit 339，claim 195）

## 候选分布

- 按状态：`{"needs_evidence": 533, "rejected": 1}`
- 按类型：`{"claim": 195, "unit": 339}`
- 按 unit_type：`{"event": 11, "institution": 19, "person": 60, "place": 38, "procedure": 12, "publication": 45, "term": 80, "work": 74}`

## 复读与修订

- 6 个分块独立复读：4 个 `accepted_with_findings`（chunk-01、02、05、06），2 个 `needs_revision`（chunk-03、04），共记录 96 项发现（2 blocking、41 major、53 minor）。
- 2 个 `needs_revision` 分块完成定向修复并复评：chunk-03 delta `accepted_with_findings`（4 项：1 major、3 minor），chunk-04 delta `accepted_with_findings`（2 项：2 minor）。初轮与 delta 合计 102 项（2 blocking、42 major、58 minor）。
- 去重专项：6 组同类型同名候选由 541 降至 535；去重复核 `accepted_with_findings`，记录 3 项发现（dd-01 major、dd-02/03 minor），均已修补。复核后又补并第 7 组“意匠化（设计）”与“意匠化设计”，由 535 降至 534。
- 指南车跨类型裁决：`2011-lilixin-zhongguo-sheji-yishu-shilun:cand-05-15`（work）与 `2011-lilixin-zhongguo-sheji-yishu-shilun:cand-03-61`（term）同指制车类型，合并到 `2011-lilixin-zhongguo-sheji-yishu-shilun:cand-03-61`；`2011-lilixin-zhongguo-sheji-yishu-shilun:cand-05-15` 保留为 `rejected` 并保留其块级 provenance，未删除。
- 补充复核：记录 6 项发现（sd-01/02 两项 blocking、sd-03 major、sd-04/05/06 minor）。sd-02 恢复 `b0093` 对 `2011-lilixin-zhongguo-sheji-yishu-shilun:cand-05-15` 的反向引用；sd-04/05 修正 `2011-lilixin-zhongguo-sheji-yishu-shilun:cand-01-72` 的“宋之前／中国古代造物／汉代以来”范围表述，并将 span 延至 L1169；sd-06 为 `2011-lilixin-zhongguo-sheji-yishu-shilun:cand-03-61` 补 L892、L897 证据；sd-01/03 的 manifest 哈希与 summary 计数在本轮收尾刷新。
- 修补后定向 delta 复评：`accepted`，0 项发现。
- 机械审计：block 覆盖、未知引用、span/evidence、引文与数字、重复 slug、unit_type 均为 0 异常；`check_reverse_refs.py` 返回 `ok=true`、`count=0`。

## 边界

- 本包只处理前六本书目中的第 5 本；其余书目不在本轮范围。
- 图版未逐张视觉核验；图注只按文字处理。
- OCR 异文按原文保留，未据外部版本校改；未做外部书目或实物核对。
- 全部候选保持 `needs_evidence` / `decision.status=pending`（1 个 `rejected` 为去重裁决记录）；未写入 `04-knowledge/`。
- 来源文件未改写；未 commit、未 push，未创建分支或 worktree。
