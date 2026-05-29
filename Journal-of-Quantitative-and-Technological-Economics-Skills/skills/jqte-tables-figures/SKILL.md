---
name: jqte-tables-figures
description: Use when finalizing tables and figures for a 《数量经济技术经济研究》 (JQTE) manuscript — making sure measurement / forecast / decomposition results carry quantitative interpretation (magnitudes, units, shares, rankings, trends) rather than only significance stars, and that every table/figure states its source and method. Use after estimates and sensitivity are settled.
---

# 表格与图（jqte-tables-figures）

## 触发时机

- 表里只有系数和星号，缺量化解读
- 测度/分解结果没有单位、份额、排名或趋势的解读
- 图表来源/方法没标注，无法复现

## 本刊重点：量化解读，不止显著性

JQTE 是数量/技术经济刊，**读者要的是"量多大、占多少、排第几、怎么变"，而不仅是"显不显著"**。每张表/图都应支撑一个可量化的判断。

## 量化解读清单（按表型）

| 表/图类型 | 必给的量化信息 |
|-----------|----------------|
| 测度结果（TFP/效率/指数） | 数值水平 + 单位 + 时间趋势 + 横向排名/分组对比 |
| 分解（Malmquist/SDA） | 各分量的贡献份额（%）+ 主导因素识别 |
| 计量回归 | 经济意义量级（弹性/半弹性/标准差效应），不只星号 |
| 预测评估 | 各 horizon 的 RMSE/方向准确率 + 相对基准的改进幅度 |
| CGE 情景 | 关键变量相对基准的百分比变化 + 方向 |

## 规范要点

- 每张表/图标注**数据来源**与**测算方法/说明**（本刊看重可追溯）
- 单位、量纲、小数位统一；大数用合适量纲（亿元、%）
- 图优先用于呈现趋势/分布/敏感性区间，表用于精确数值
- 主回归表列数克制，把核心结果放主表，稳健性/异质性进附表
- 系数表注明标准误类型、显著性符号含义

## 自检清单

- [ ] 每张主表/图都对应一个可量化的判断
- [ ] 测度/分解结果给了水平、份额、趋势或排名，不止星号
- [ ] 预测表按 horizon 给误差并对比基准
- [ ] 所有表/图标注数据来源与方法
- [ ] 单位/量纲/小数位统一
- [ ] 主表列数克制，次要结果入附表

## 反模式

- 整页只有系数 + 三档星号，无经济量级解读
- 测度结果列一堆数字却不解读趋势/排名
- 表无来源、无方法注，无法复现
- 把所有稳健性都塞进主表，列数爆炸
- 图美观但无信息增量（如能用一句话说清却画三张图）

## 输出格式

```
【主表/图清单】[T1 …, F1 …]
【量化解读】到位 / 缺失 <处>
【来源方法注】齐 / 缺 <表号>
【单位量纲】统一 / 待修
【主表列数】<n>（克制 □）
【下一步】jqte-implications
```
