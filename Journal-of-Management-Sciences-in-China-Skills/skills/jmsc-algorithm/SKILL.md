---
name: jmsc-algorithm
description: Use when designing and analyzing a solution algorithm for a 《管理科学学报》 (Journal of Management Sciences in China) manuscript — giving exact / heuristic / decomposition methods with complexity analysis and, for iterative methods, convergence proofs. "It runs fast" is not analysis. Use after the model and properties are established.
---

# 算法设计与分析（jmsc-algorithm）

## 触发时机

- 模型有了，但求解方法只是"调用求解器/跑得快"
- 算法没有复杂度分析，或没有收敛性论证
- 启发式无近似比/界，无法说明解的质量
- 审稿质疑"算法贡献在哪、能否保证收敛"

## 核心：算法必须可分析，不止可运行

本刊看的是**算法贡献的可分析性**："跑得快"不算分析。要么给**复杂度**（精确/近似算法），要么给**收敛性**（迭代算法），要么给**界/近似比**（启发式），三者至少其一并配数值验证。

## 算法类型与必答问题

| 算法类型 | 必须回答 |
|----------|----------|
| 精确算法（DP/B&B/列生成） | 时间/空间复杂度；状态空间规模；是否多项式 |
| 分解算法（Benders/Lagrangian/ADMM） | 子问题可解性；收敛到何点（最优/KKT）；收敛速率 |
| 迭代算法（梯度/不动点/拍卖） | 收敛性证明；步长条件；线性/次线性速率 |
| 启发式/近似 | 近似比 ρ 或最坏情形界；与下界的 gap |
| 元启发式（GA/SA/PSO） | 参数设定依据；与精确解/界对比（不能只给"更好"） |

## 复杂度分析要点

- 用 O(·) 给出**关于输入规模的**时间与空间复杂度，并指明输入规模如何定义（n 个客户、T 期、|S| 状态…）。
- 区分**最坏 / 平均 / 实例相关**复杂度，别混用。
- 若是 NP-hard 问题，先给硬度结论，再说明为何用启发式/近似。

## 收敛性分析要点

- 陈述收敛**到什么**（全局最优 / 局部 / 稳定点 / 均衡）。
- 给出收敛**条件**（凸性、步长、Lipschitz、单调）。
- 有条件就给**速率**（线性、次线性 O(1/k)、二阶）。

## 自检清单

- [ ] 算法用伪代码给出，输入/输出/终止条件明确
- [ ] 复杂度以 O(·) 表达，输入规模定义清楚
- [ ] 迭代算法有收敛性证明（到什么点、什么条件、什么速率）
- [ ] 启发式有近似比或与界/最优的 gap，而非只比对手好
- [ ] NP-hard 已说明，启发式的使用有正当理由
- [ ] 算法性质用数值实验验证（见 jmsc-numerical-experiments）

## 反模式

- 只说"算法高效""收敛快"，无 O(·)、无证明
- 元启发式只报"比基准好 X%"，不给界、不与最优/下界比
- 把"调用 CPLEX/Gurobi 求解"当成算法贡献
- 收敛图当收敛证明用

## 输出格式

```
【算法类型】精确 / 分解 / 迭代 / 启发式 / 元启发式
【伪代码】有 / 无（输入/输出/终止条件齐？）
【复杂度】时间 O(…)，空间 O(…)，输入规模=<…>
【收敛性】到<点>，条件<…>，速率<…> / 不适用
【解质量】近似比 ρ=… / gap=… / 仅经验对比（弱）
【硬度】NP-hard? 是/否 → 启发式理由
【下一步】jmsc-numerical-experiments
```
