---
name: cie-did-identification
description: Use when the identification strategy for a 《中国工业经济》 (China Industrial Economics) manuscript is multi-period / staggered DID or an event study. Mandates parallel-trends event-study plots, placebo tests, and modern heterogeneity-robust estimators (Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-D'Haultfœuille, Goodman-Bacon decomposition) whenever treatment timing varies.
---

# 识别策略：多期 DID / 事件研究（cie-did-identification）

## 触发时机

- 实证主体是 DID / 多期（交错）DID / event-study
- TWFE 用在交错处理上，但没回应异质性处理偏误
- 平行趋势只口头说"满足"，没画事件研究图
- 用连续型处理强度（continuous/dose DID）但识别假设没说清

## 本刊红线（缺一即高危退修）

1. **平行趋势必须画事件研究图**（动态效应 + 95% CI，处理前各期系数应不显著）
2. **安慰剂检验必做**（随机化处理时点/处理对象 500—1000 次，看真实估计是否落在分布尾部）
3. **交错处理必须用异质性稳健估计**——TWFE 在交错+异质性处理效应下有偏（负权重问题）

## 分支路径

### 分支 A：标准两期 / 单一时点 DID

- 平行趋势：事件研究图 + 处理前系数联合检验
- 安慰剂：随机分配处理组 ≥ 500 次
- 控制组合理性论证（为什么这些是有效对照）

### 分支 B：交错（staggered）DID —— 本刊高频

- **必须**做 Goodman-Bacon 分解，报告"坏比较（已处理作对照）"权重
- **必须**改用异质性稳健估计之一并作为主/稳健结果：
  - Callaway & Sant'Anna（2021）group-time ATT
  - Sun & Abraham（2021）交互加权事件研究
  - de Chaisemartin & D'Haultfœuille（2020）did_multiplegt
  - Borusyak et al. 插补估计 / Gardner two-stage
- 报告 TWFE 与稳健估计的对比，说明结论是否稳定

### 分支 C：事件研究（event-study）

- 基准期选择明确（通常 t=-1），不要遗漏共线性陷阱
- pre-trend 各期不显著；若显著需讨论预期效应/选择性
- 动态效应图标注处理时点垂直虚线（见 `cie-tables-figures`）

### 分支 D：连续/强度型 DID

- 处理强度的外生性论证
- "强度 × 时点"交互的平行趋势：不同强度组趋势一致
- 警惕强度与其他冲击共变

### 分支 E：识别加固（与 PSM-DID 衔接）

- 分配规则非随机 → PSM-DID（先匹配再 DID，转 `cie-robustness`）
- 排除同期竞争性政策（剔除其他试点样本/时间窗）

## 必查清单

- [ ] 事件研究图已画（动态系数 + 95% CI）
- [ ] 安慰剂检验已做（时点/对象随机化）
- [ ] 交错处理：Bacon 分解 + 异质性稳健估计齐全
- [ ] 标准误聚类层次合理（通常聚类到处理层级，如城市/行业）
- [ ] 回应"预期效应 / 提前响应"
- [ ] 剔除同期竞争性政策的干扰

## 反模式

- TWFE + 交错处理却不谈负权重/异质性偏误（本刊会直接退修）
- "平行趋势满足"一句带过，不画图
- 安慰剂只换一次处理组就称稳健
- 聚类到个体却忽视处理在群组层级（低估标准误）
- 连续 DID 不论证处理强度外生

## 输出格式

```
【识别策略】两期DID / 交错DID / event-study / 连续DID
【平行趋势】事件研究图 √ / 缺
【安慰剂】时点随机 □ 对象随机 □ / 缺
【交错处理】Bacon分解 □ CS/SA/dCDH 估计 □ / N.A.
【聚类层级】<…>
【缺失检验】<…>
【下一步】cie-mechanism
```
