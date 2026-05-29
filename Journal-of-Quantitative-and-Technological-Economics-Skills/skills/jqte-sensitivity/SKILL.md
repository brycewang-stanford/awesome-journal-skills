---
name: jqte-sensitivity
description: Use to design and report robustness for a 《数量经济技术经济研究》 (JQTE) manuscript where the contribution is measurement, a model, or a forecast — focusing on sensitivity to method choice, parameter / specification, data caliber, and sample window, rather than the placebo / parallel-trends battery of a causal paper. Use after the main estimates exist.
---

# 敏感性与稳健性（jqte-sensitivity）

## 触发时机

- 主测度/模型/预测结果有了，但只有一种设定
- 审稿人问"换个方法/参数/口径还成立吗"
- 误把因果刊的稳健性套路（安慰剂、平行趋势）当成本刊要的

## 本刊的稳健性 ≠ 因果刊的稳健性

因果论文比拼安慰剂、平行趋势、随机化检验；**JQTE 测度/方法/预测论文比拼的是对"方法-参数-口径-样本"选择的敏感性**——核心问题是"我这个数/这个预测，换合理的设定会不会翻"。

## 四类敏感性（按贡献类型取用）

| 维度 | 测度类 | 计量/预测类 | IO/CGE 类 |
|------|--------|-------------|-----------|
| 方法选择 | DEA 规模假设、SFA 分布、参数法 vs 指数法 | 模型族（VAR vs VECM vs ARDL） | 分解形式、闭合规则 |
| 参数/设定 | 折旧率、基期、权重方案 | 滞后阶、窗口、识别约束 | 弹性参数取值、冲击幅度 |
| 数据口径 | 平减指数、变量定义 | 实时 vs 修订、频率 | IO 表年份、部门聚合 |
| 样本范围 | 子样本/分组 | 子区间、剔除危机期 | 不同基准年 |

## 报告方式

- 给**敏感性区间或矩阵**：核心结论在合理设定集合下的取值范围，而非只展示"我选的那个"
- 若结论对某参数特别敏感，**明说**并讨论合理取值的依据，不掩盖
- 测度类：核心排序/趋势是否在方法替代下稳定（如效率排名的秩相关）
- 预测类：不同窗口/基准下的相对优势是否稳定
- CGE：对关键弹性做参数扫描 (sensitivity sweep) 或系统敏感性分析 (SSA)

## 自检清单

- [ ] 至少覆盖"方法 + 参数 + 口径"中两类敏感性
- [ ] 给出结论的取值区间/秩稳定性，而非单点
- [ ] 对最敏感的假设有显式讨论与依据
- [ ] 敏感性结论与主结论的关系说清（稳健 / 有条件稳健）
- [ ] 没有用因果刊的安慰剂套路充数

## 反模式

- 只展示自己选的那一组设定，回避替代设定
- 把"加几个控制变量"当全部稳健性（测度类这远不够）
- 结论对参数高度敏感却不提
- CGE 不对弹性做敏感性，单点结果当定论

## 输出格式

```
【贡献类型】测度 / 计量预测 / IO-CGE
【已做敏感性】方法 □ 参数 □ 口径 □ 样本 □
【结论稳健性】稳健 / 有条件稳健（条件 <…>）/ 不稳健
【最敏感假设】<…>，依据 <…>
【缺口】<待补的敏感性>
【下一步】jqte-tables-figures
```
