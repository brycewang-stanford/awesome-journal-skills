---
name: ceq-modern-did
description: Use when a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript uses difference-in-differences with staggered adoption or heterogeneous treatment effects — to bring it into compliance with modern estimators (Callaway–Sant'Anna, de Chaisemartin–D'Haultfœuille, Sun–Abraham) instead of bare two-way fixed effects. Bare TWFE on staggered timing is a near-certain reject at CEQ.
---

# 现代 DID 合规（ceq-modern-did）

## 触发时机

- 处理时点**交错**（不同单位不同时间被处理），但只跑了 TWFE
- 处理效应可能随队列/时间**异质**
- 审稿人提"负权重 / 坏比较 / 前置效应"等批评

## 核心判断：你的 DID 是哪一类？

| 情形 | 是否有 TWFE 偏误 | 处理 |
|------|------------------|------|
| 单一时点、两组 | 通常无 | 标准 DID 即可，仍画事件研究图 |
| 交错处理 + 同质效应 | 轻 | 仍建议稳健估计量交叉验证 |
| 交错处理 + 异质效应 | **严重（负权重）** | **必须**用现代估计量 |
| 连续/强度处理 | 视情形 | 用 de Chaisemartin–D'Haultfœuille 等专用估计量 |

## 必做四步（交错处理）

1. **诊断**：Goodman-Bacon 分解，报告"坏比较"（already-treated 作对照）的权重；或 de Chaisemartin–D'Haultfœuille 负权重诊断。
2. **现代估计量**（至少一种，建议交叉验证两种）：
   - Callaway–Sant'Anna（`csdid` / `did`）：分组-时间 ATT 聚合
   - de Chaisemartin–D'Haultfœuille（`did_multiplegt(dyn)`）：适配连续/可逆处理
   - Sun–Abraham（`eventstudyinteract`）：交互加权事件研究
3. **事件研究图**：用上述估计量画动态效应（见 `ceq-figures`），而非 TWFE 的污染系数。
4. **对照报告**：TWFE 与现代估计量并列，说明差异来源。

## 易踩坑

- 用 TWFE 事件研究图当"平行趋势成立"——其前置系数本身被污染
- 把 not-yet-treated 与 already-treated 混作对照而不说明
- 连续处理直接套 Callaway–Sant'Anna（其默认针对二元吸收处理）
- 只报现代估计量的点估计，不报其聚合方式与对照组定义

## 自检清单

- [ ] 已诊断是否交错 + 是否异质（决定要不要现代估计量）
- [ ] 至少一种现代估计量；建议两种交叉验证
- [ ] 事件研究图来自现代估计量，前置系数近零
- [ ] 报告了对照组定义（never/not-yet-treated）与聚合权重
- [ ] TWFE 与现代估计量并列，差异有解释
- [ ] 连续/可逆处理用了适配的估计量

## 反模式

- 裸 TWFE 跑交错处理直接声称因果（CEQ 退稿高发）
- 不做负权重/坏比较诊断
- "我们也跑了 Callaway-Sant'Anna，结果稳健"但不展示、不解释

## 输出格式

```
【处理结构】单时点 / 交错 / 连续
【异质性风险】低 / 高（是否需现代估计量）
【诊断】Bacon 分解 / 负权重 已做 □
【现代估计量】CS □ dCDH □ SA □（用了哪些）
【事件研究图】来自现代估计量 □
【缺口】<待补>
【下一步】ceq-inference
```
