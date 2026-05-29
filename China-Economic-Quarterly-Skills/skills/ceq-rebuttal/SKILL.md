---
name: ceq-rebuttal
description: Use when drafting the response letter for a revise-and-resubmit (R&R) at 《经济学(季刊)》 (China Economic Quarterly, CEQ) — where reviewers are typically field-trained and press hardest on identification, modern-DID compliance, and inference. Structures a point-by-point reply that concedes or rebuts with evidence. Use only after the manuscript itself has been revised.
---

# 外审回复信（ceq-rebuttal）

## 触发时机

- 收到 CEQ 的 R&R（修改重投）或外审意见
- 正文**已**按意见修订（未改正文前不要生成回复）

## CEQ 审稿人的火力点

CEQ 审稿人多有海外训练，最常打的位置（对照各专用 skill）：

- 识别假设是否真外生（`ceq-identification`）
- 交错 DID 是否过现代估计量（`ceq-modern-did`）
- 聚类/弱工具/多重检验（`ceq-inference`）
- 机制是中介回归还是可证伪证据（`ceq-mechanism`）
- 贡献是否对标具体文献，还是套话（`ceq-literature-review`）

## 回复信结构

1. **开头致谢 + 总览**：一段说明主要修改（识别强化、现代 DID、新增检验），让编辑快速抓到改动量。
2. **逐条回应**：每条意见用统一三段式（见下）。
3. **修改对照**：引用修订稿的页码/表号，必要时贴关键新结果。

## 单条回应三段式

```
> 审稿人意见原文（粘贴）
【回应】接受 / 部分接受 / 谨慎反驳（+一句立场）
【做了什么】具体修改：新增了什么检验 / 改了哪段 / 见修订稿第X页 表Y 图Z
【为什么这样改】方法/识别依据（必要时引文献）
```

## 应对策略

- **能补就补，别嘴硬**：要求加安慰剂/现代估计量/弱工具稳健——直接做，附新结果。
- **反驳要有据**：不同意时给方法论文献或数据证据，语气专业克制，不情绪化。
- **识别类意见最高优先**：先回识别与推断，再回写作类小意见。
- **两位审稿人冲突**时：说明你的取舍逻辑，请编辑裁断，不偏废任一方。
- **做不到的**：诚实说明数据/制度约束，给出退而求其次的稳健性，而非假装做了。

## 自检清单

- [ ] 每条意见都有独立回应，无遗漏
- [ ] 识别/DID/推断类意见已用新结果回应，不是口头保证
- [ ] 每条标注修订稿对应页码/表号
- [ ] 反驳处有文献或证据支撑，语气专业
- [ ] 审稿人间冲突已说明取舍
- [ ] 正文确已修订（回复与正文一致）

## 反模式

- 正文没改就写"已修改"
- 用"我们认为没有必要"打发识别类硬意见而不给理由
- 把"已在修订稿中处理"当万能挡箭牌，不指页码
- 情绪化反驳或忽视次要意见
- 声称做了某检验，正文却找不到

## 输出格式

```
【总览段】主要修改：识别 / 现代DID / 推断 / 机制 / 写作
【逐条回应】共 N 条 | 接受 X / 部分 Y / 反驳 Z
【硬意见(识别/推断)】是否已用新结果回应：是/否 <补>
【页码对照】齐 / 缺 <补>
【冲突意见处理】有 / 无
【结论】可重投 / 仍需补 <清单>
```
