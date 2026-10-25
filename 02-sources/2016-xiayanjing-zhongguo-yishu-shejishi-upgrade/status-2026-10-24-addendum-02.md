# 处理状态补记 02：中国艺术设计史（升级版）（夏燕靖，2016）

- **记录日期**：2026-10-24
- **doc_id**：`2016-xiayanjing-zhongguo-yishu-shejishi-upgrade`
- **处理包**：`03-processing/2016-xiayanjing-zhongguo-yishu-shejishi-upgrade/`
- **处理 profile**：`compact-v4`
- **当前状态**：`completed`（重试复评后的补修已完成）

本文件是 `status-2026-10-24.md` 的第二次追加补记；原状态文件与 `status-2026-10-24-addendum-01.md` 均保持只读，不改写。

## 补记原因

最终聚焦复评的独立重试返回了 15 项发现（0 blocking、3 major、12 minor）和 13 项疑似漏立对象。与首轮 14 项发现相比，重试多出两项，首轮曾记录的 cand-02-151（簠）时代字段问题未再出现。逐项核对后确认：

- 13 项发现已在首轮修订中处理。
- 2 项为新发现，已补修：
  - `cand-07-102`（major）：L4133 末句在“云”字后中断，插入“知识链接：明清丝纺织业文献例举”与图9-3，L4144 接“贵和辽东地区”。原候选误判为来源截断。现已把 span 扩至 L4144、补入云贵与辽东，并修正 notes；相邻 `cand-07-101` 的同一误注一并修正。
  - `cand-07-100`（minor）：标题原把“浸铜法”等同于“水法冶金”，原文只说浸铜法是水法冶金技术的起源；且同书 L3851 作“已运用科学方法”、L3869 作“已运用化学方法”，两处异文未记。现标题改为“浸铜法（水法冶金之始）”，notes 记录异文，span 与 evidence 覆盖 L3851-L3870。
- 13 项疑似漏立对象经全账本核对均已有候选承载：鼎、簋、尊、壶、爵（cand-02-116 至 cand-02-120）、莲鹤方壶（cand-02-32）、九鼎八簋（cand-02-17）、商代象尊（cand-02-134）、人民大会堂（cand-09-71 / cand-09-116）、南京云锦（cand-07-79，另见 cand-06-25）、深衣（cand-02-53）、冕服（cand-02-57；本次补入 L997 的明确界定）、干栏式建筑（cand-01-70 / cand-01-71）、清代工艺文献三种（cand-08-49《陶说》、cand-08-50《绣谱》、cand-08-52《装潢志》）、《蜀锦谱》（cand-11-68）、《梓人遗制》（cand-11-69）、《遵生八笺》（cand-11-71）、镔铁局（cand-07-78）、《淮南子》（cand-04-30 / cand-11-52）、开封相国寺塔（cand-06-82）、定县开元寺瞭敌塔（cand-06-83）。`omission_count=0`。

## 复核结果

- 候选总数不变：1211（unit 957、claim 254）；全部仍为 `needs_evidence` / `decision.status=pending`。
- 机械审计：block 覆盖 754/754、未读 0、未知引用 0、span/evidence 错误 0、引文/数字抽查 0 异常、重复 slug 0、非法 unit_type 0。
- 仓库校验：`python scripts/validate_processing_package.py "03-processing/2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"` 返回 `valid: true`。
- `semantic_acceptance` 已更新重试复评记录，结论仍为 `accepted_with_findings`。

## 指纹

- 聚合输入指纹：`sha256:2e6be085828a3688f5568e8f4cf1a4e5788be8c849a215fa8c336cd2cb97e682`
- `semantic_acceptance.source_version` 未变，与聚合输入指纹一致。

## 边界

- 本补记不表示候选已写入 `04-knowledge/`。
- 未做图版逐张视觉核验；未做外部书目或实物核对；OCR 异文按原文保留。
- 未 commit、未 push；未创建分支或 worktree；来源文件未改写。
- 本补记不构成写入、提交或推送授权。
