---
name: nbr-experiment
description: Use for experimental studies submitted to 《南开管理评论》 (Nankai Business Review) — design (between/within, scenario/vignette, lab/field), manipulation checks, randomization and confound control, effect sizes and power, and mediation/moderation via experimental-causal-chain or measurement-of-mediation designs. Use when a hypothesis is tested by manipulating an independent variable rather than measuring it.
---

# 实验法（nbr-experiment）

## 触发时机

- 自变量是**操纵**出来的（情境/启动/任务），不是测量
- 用情境实验（vignette/scenario）、实验室或现场实验做因果推断
- 想用实验补强问卷研究的内部效度（多研究设计）

## 设计要点

- 明确**被试间 / 被试内 / 混合**设计，给出各组样本量与分配
- 操纵材料**预测试（pilot）**：确认操纵有效、强度适中、无混淆
- **随机分配**到条件，报告分配方式；现场实验交代随机化层级

## 操纵检验与混淆控制

- **操纵检验（manipulation check）**：证明操纵确实改变了目标构念，且**未同时改变**其它构念
- **混淆排查**：需求特征、注意力检验（attention check）、可信度/真实感评分
- 报告**剔除标准**（未通过注意力/操纵检验者）及剔除前后稳健性

## 统计与效应量

- 报告**效应量**（Cohen's d / η²p / f），不只报 p 值
- 交代**功效分析（power）**或样本量依据
- 多重比较做校正；必要时报告贝叶斯因子或等效性检验
- **机制**：用**实验因果链**（操纵中介变量）或**测量中介 + Bootstrap**检验过程；调节用交互 + 简单斜率

## 自检清单

- [ ] 设计类型、各条件样本量、随机分配交代清楚
- [ ] 操纵做了预测试，正文有操纵检验且无混淆
- [ ] 有注意力检验与明确剔除标准（含稳健性）
- [ ] 报告效应量与功效/样本量依据，不只 p 值
- [ ] 机制用因果链或测量中介（Bootstrap），不止"显著差异"
- [ ] 讨论了生态效度 / 外部效度的局限

## 反模式

- 只报均值差异显著，不报效应量与功效
- 操纵无预测试、无操纵检验，自称"成功操纵"
- 事后随意剔除被试，不报标准与稳健性
- 把"组间差异显著"直接当成机制成立

## 输出格式

```
【设计】被试间/内/混合｜条件数 <…>｜各组 n <…>
【操纵】预测试□｜操纵检验：通过□ 无混淆□
【质控】注意力检验□｜剔除标准 <…>
【统计】效应量 <d/η²p>｜功效/样本量依据 <…>
【机制】因果链 / 测量中介(Boot CI) <…>
【下一步】nbr-china-context / nbr-discussion-contribution
```
