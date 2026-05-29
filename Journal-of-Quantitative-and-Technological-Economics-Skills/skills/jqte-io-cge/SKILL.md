---
name: jqte-io-cge
description: Use when a 《数量经济技术经济研究》 (JQTE) manuscript is built on an input-output table, a CGE model, or a structural decomposition (SDA). Enforces explicit data sources, parameter calibration, closure rules, scenario design, and end-to-end reproducibility. The standard reject here is a black-box model run whose setup cannot be reconstructed.
---

# 投入产出 / CGE / 结构分解（jqte-io-cge）

## 触发时机

- 模型基于投入产出表、CGE 或 SDA/SPA 结构分解
- 用了 GTAP/GAMS/现成 CGE 模板但设定交代不清
- 审稿人质疑"参数从哪来、闭合怎么定、结果能否复现"

## 本刊铁律：数据 + 校准 + 闭合 + 情景，全链可复现

CGE/IO 最易被拒的是**黑箱**：跑出漂亮结果却无法重建模型。必须把数据来源、参数来源、闭合规则、情景设定写到能复现的程度。

## 投入产出（IO）

- IO 表来源与年份明确（国家/地区 IO 表、WIOD、OECD-ICIO 等）
- 部门合并/拆分规则、价格型 vs 实物型、竞争型 vs 非竞争型进口处理交代清楚
- 关联指标（影响力系数、感应度系数、Leontief/Ghosh 逆矩阵）定义给全
- 多区域 IO (MRIO) 说明区域间贸易数据来源与平衡方法

## 结构分解（SDA / SPA）

- 分解项（技术系数变化、最终需求结构、规模等）的定义与公式给全
- 多因素分解的**分解形式**说明（两极分解平均、加性 LMDI 等），避免路径依赖造成的非唯一性
- 报告分解残差或说明为何无残差

## CGE

- **数据**：基准社会核算矩阵 (SAM) 的来源、年份、平衡方法
- **参数校准**：弹性参数（替代弹性、Armington、Frisch 等）的来源——校准得到还是文献/计量估计，逐一列出
- **闭合规则**：宏观闭合（储蓄-投资、政府、外部）显式说明，闭合不同结论可能反转
- **情景设定**：基准情景 (BAU) 与政策情景的冲击变量、幅度、引入路径清楚
- **求解与检验**：求解软件/算法、是否通过基准复制 (benchmark replication) 校验

## 自检清单

- [ ] 数据来源（IO 表 / SAM）年份、口径、平衡方法明确
- [ ] 关键弹性参数逐一给出来源（校准 / 文献 / 估计）
- [ ] 闭合规则显式说明，并讨论其对结论的影响
- [ ] 情景冲击的变量、幅度、路径清楚
- [ ] SDA 分解形式说明，残差处理交代
- [ ] 模型通过基准复制校验，结果可复现

## 反模式

- 用现成 CGE 模板跑情景，却不交代弹性参数从哪来
- 闭合规则只字不提（换闭合可能结论反转）
- SDA 不说分解形式，结果随分解路径变化而不自知
- 情景冲击幅度无依据、来源不明
- 给结果却无法让人重建模型（黑箱）

## 输出格式

```
【模型】IO / MRIO / SDA-SPA / CGE
【数据】<IO表/SAM 来源 + 年份 + 平衡方法>
【参数校准】弹性来源 <校准/文献/估计>（逐项 □）
【闭合规则】<宏观闭合说明 + 对结论影响>
【情景】基准 vs 政策：冲击 <变量/幅度/路径>
【可复现】基准复制校验 □ 公式/分解形式齐 □
【下一步】jqte-sensitivity / jqte-tables-figures
```
