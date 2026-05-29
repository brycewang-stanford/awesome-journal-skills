---
name: nbr-survey-sem
description: Use for survey-based structural equation modeling in 《南开管理评论》 (Nankai Business Review) — CFA/SEM fit indices, mediation and moderation, moderated mediation with bootstrap indirect effects and the index of moderated mediation, and multilevel models (HLM) for nested data. Use when testing construct-relationship hypotheses (mediation / moderation / moderated mediation) on questionnaire data.
---

# 问卷-SEM 分析（nbr-survey-sem）

## 触发时机

- 假设是中介 / 调节 / 被调节的中介
- 数据是问卷（个体或企业层级）
- 数据有嵌套结构（员工嵌套于团队/企业）

> 前置：测量须先过 `nbr-measurement`（信效度 + CMV）。模型拟合不能替代测量规范。

## 测量模型与拟合标准（经验门槛，非硬性）

先验证测量模型（CFA），再估结构模型：
- **χ²/df** < 3（宽松 < 5）；**CFI / TLI** > 0.90（宜 > 0.95）
- **RMSEA** < 0.08（宜 < 0.06）；**SRMR** < 0.08
- 用 CFA 区分多构念（如目标模型优于合并模型），佐证区分效度

## 中介 / 调节 / 被调节的中介

- **中介**：报告**Bootstrap**（如 5000 次）间接效应及偏差校正 95% CI，**CI 不含 0** 才成立；优先 Bootstrap 而非 Sobel
- **调节**：自变量与调节变量**中心化/标准化**后建交互项；报告交互项系数，并做**简单斜率（simple slope）**与图示
- **被调节的中介**：报告**moderated mediation 指数**（index of moderated mediation）及其 Bootstrap CI；并给不同调节水平下的**条件间接效应**

## 多层数据（HLM）

- 先看**ICC(1)/ICC(2)** 与 rwg 判断是否需要多层、能否聚合
- 跨层假设用**多层模型（HLM / 多层 SEM）**，区分组内/组间效应
- 跨层中介/调节按 1-1-1、2-1-1 等路径明确层级，必要时组均中心化

## 自检清单

- [ ] 先 CFA 后结构模型，拟合指标齐全（CFI/TLI/RMSEA/SRMR）
- [ ] 中介用 Bootstrap 间接效应 + CI，不只看系数显著
- [ ] 调节做了中心化、交互项、简单斜率与图
- [ ] 被调节的中介报告了 index of moderated mediation
- [ ] 嵌套数据先验证 ICC，再决定是否上 HLM
- [ ] 控制变量、共同方法因子等处理透明可复现

## 反模式

- 直接报结构模型，跳过测量模型拟合
- 中介只用逐步回归（Baron-Kenny）或 Sobel，不做 Bootstrap
- 调节不中心化、不画简单斜率，只贴一个交互项系数
- 嵌套数据当独立样本跑普通 SEM，无视 ICC

## 输出格式

```
【测量模型】χ²/df <…> CFI <…> TLI <…> RMSEA <…> SRMR <…>
【中介】间接效应 <…>，Boot 95% CI [ , ]｜成立□
【调节】交互项 β <…>，简单斜率：高/低 <…>
【被调节中介】index <…>，CI [ , ]｜条件间接效应：<…>
【多层】ICC1/ICC2 <…>｜模型：HLM / 多层SEM
【下一步】nbr-china-context / nbr-discussion-contribution
```
