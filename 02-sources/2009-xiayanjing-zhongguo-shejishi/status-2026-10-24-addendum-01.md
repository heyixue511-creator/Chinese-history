# 状态补编 01：claim_scope 修正说明

- 补编日期：2026-10-24
- 关联记录：`status-2026-10-24.md`

前件称“阅读器在完成前已把 9 条非法 `claim_scope` 改为合法枚举”，该表述超出可核实范围。

可核实事实是：

- 处理中一度见到 9 条候选把 `causal_argument` 或 `historiographical_claim` 填入 `claim_scope`。
- 最终落盘的 7 个 chunk result 与合并包中，`claim_scope` 全部为合法枚举，无非法值。
- 未记录具体由哪个环节、在何时完成改写；不得据此推断阅读器“自行修正”。

本补编不改变来源指纹、覆盖、候选数量、机械校验与审计结论。
