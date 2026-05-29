---
name: jwe-identification
description: Use when the identification strategy is the bottleneck for a 《世界经济》 (The Journal of World Economy) manuscript — external shocks (tariffs, trade agreements, exchange-rate reforms, FDI negative-list) as quasi-experiments, plus shift-share / Bartik and gravity designs. Stress-tests exogeneity and inference, including the modern shift-share critiques.
---

# 开放经济识别策略（jwe-identification）

## 触发时机

- 实证主体仅 OLS + 控制变量，外生性靠"我们认为"
- 用 shift-share / Bartik 暴露度但不讨论 exposure 外生性与推断
- 引力模型用 OLS-log、零贸易直接丢
- 有外部冲击但没想清"为何对个体外生"

## 设计优先级（开放经济场景）

1. **外部 / 制度性冲击 + DID / event-study**：关税战、入世、自贸区、汇改、外资负面清单
2. **shift-share / Bartik 暴露度**（进口渗透、出口需求冲击）——需现代推断
3. **引力模型（PPML）** 估贸易政策（协定、关税）效应
4. **IV**（外部冲击作工具，论证排他性）
5. OLS + 严密外生性讨论（理论实证 / 结构估计中可接受）

## 分支路径

### 分支 A：外部冲击 DID / event-study
- 冲击是否真外生于个体（关税由贸易伙伴决定 / 政策非内生于被处理者）？
- staggered 处理 → 用 Goodman-Bacon 分解 + Callaway-Sant'Anna / Sun-Abraham，别裸用 TWFE
- 平行趋势：事件研究图必画；安慰剂（随机处理时点 / 对象）
- 预期效应：被处理者是否提前响应（前置项）

### 分支 B：shift-share / Bartik（重点）
- 暴露度 = 初期份额 × 共同冲击（如 ADH 的进口渗透）
- **现代推断批评必须回应**：
  - Goldsmith-Pinkham-Sorkin-Swift：识别力来自**份额**，须检验份额外生、报告 Rotemberg 权重
  - Borusyak-Hull-Jaravel：识别力来自**冲击**，须冲击层面随机性 + 相应推断
  - Adão-Kolesár-Morales：标准误须按暴露结构调整（常规聚类会过度拒绝）
- 至少报告：份额外生性论证、Rotemberg 权重 top 来源、shock-level 或 exposure-robust 标准误

### 分支 C：引力模型
- **用 PPML**（Santos Silva-Tenreyro）处理异方差与零贸易，别用 OLS-log
- 进出口国×年 + 国家对固定效应（multilateral resistance）
- 贸易政策变量（协定 / 关税）内生性：滞后 / IV / 事件研究

### 分支 D：IV（外部冲击为工具）
- 第一阶段 F ≥ 10；弱工具用 Anderson-Rubin / weak-IV-robust CI
- 排他性三段论：理论 + 制度 + 安慰剂
- 报告 reduced form

## 必查清单

- [ ] 外部冲击对个体的外生性有制度 / 理论证据，不只"我们认为"
- [ ] staggered DID 回应了异质性处理偏误
- [ ] shift-share 报告份额外生性 + Rotemberg 权重 + exposure-robust SE
- [ ] 引力用 PPML + 多边阻力固定效应
- [ ] 平行趋势 / 安慰剂 / 弱工具 检验齐全
- [ ] 标准误聚类层次与暴露 / 冲击结构匹配

## 反模式

- shift-share 当普通 IV 用，标准误常规聚类、不提 exposure-robust 推断
- 关税 / 协定当外生但不论证对方为何这样定
- 引力 OLS-log 丢零贸易
- TWFE + staggered 不讨论 Bacon 分解

## 输出格式

```
【识别策略】外部冲击DID / shift-share / 引力PPML / IV / 结构
【外生性论证】制度□ 理论□ 安慰剂□
【shift-share 推断】份额外生□ Rotemberg□ exposure-robust SE□
【已完成检验】[平行趋势, 安慰剂, 弱工具, ...]
【缺失检验】[...]
【下一步】jwe-transmission-channel
```
