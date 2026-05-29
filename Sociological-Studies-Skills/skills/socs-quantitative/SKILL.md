---
name: socs-quantitative
description: Use for the quantitative path in 《社会学研究》 (Sociological Studies) — analyzing survey data (CGSS/CFPS/CLDS) with regression / Logit / multilevel / event-history (survival) / sequence analysis, and interpreting results as a sociological mechanism rather than entering an econometric identification arms race. Use when the draft only reports coefficients.
---

# 定量路径（socs-quantitative）

## 触发时机

- 数据是 CGSS / CFPS / CLDS / 人口普查等社会调查
- 已有回归结果，但只报系数与显著性，缺社会学解读
- 担心审稿人嫌"识别不干净"，想往因果军备竞赛上加码

## 立场：方法服务社会学问题

本刊不是因果识别竞赛场。**系数本身不是发现，社会过程才是。**识别要诚实、稳健，但目标是揭示机制与异质性的**社会学含义**，不是把工具变量堆到无懈可击。描述性事实若揭示重要社会结构，本刊比经济学刊更接纳。

## 方法工具箱（按问题选，不是越炫越好）

| 问题形态 | 常用方法 |
|----------|----------|
| 连续/类别结果的影响因素 | OLS / Logit / 多项 Logit / 有序 Logit |
| 嵌套结构（个体嵌入地区/学校/家庭） | 多层模型（HLM）、随机效应 |
| 事件发生与时机（初婚、离职、流动） | 事件史 / 生存分析（Cox、离散时间） |
| 生命历程的状态序列 | 序列分析、最优匹配 |
| 潜变量与测量结构 | 结构方程、潜类别 |
| 代际/流动结构 | 对数线性、流动表分析 |

## 数据与测量规范

- 交代抽样、权重、缺失处理（CGSS/CFPS/CLDS 的设计权重与追访结构）
- 关键变量的**社会学操作化**：为什么这样测，测的是哪个理论构念
- 报告样本量随模型变化、稳健性来源；区分横截面与面板含义

## 把定量做成社会学的关键

- **机制**：不止"X 显著"，而是"经由什么社会过程"——转 `socs-mechanism-social-process`
- **异质性**：按结构位置（阶层、城乡、性别、世代）切分，并给社会学解释
- **解读**：把效应量翻译成可理解的社会后果（多少机会差距、多大流动壁垒）

## 自检清单

- [ ] 方法由问题决定，不是为炫技选难模型
- [ ] 变量操作化有社会学理由，对应理论构念
- [ ] 抽样/权重/缺失处理交代清楚
- [ ] 系数已翻译成社会过程与社会后果，不止显著性
- [ ] 异质性按结构位置切分并有解释
- [ ] 不把"识别更干净"当作主要贡献

## 反模式

- 把显著性当结论，无机制无解读
- 识别军备竞赛，喧宾夺主盖过社会学问题
- 异质性只切"东中西"，无结构含义
- 罗列模型不报告稳健性与样本变化

## 输出格式

```
【数据】CGSS/CFPS/CLDS/普查（年份、样本、权重）
【方法】<回归/多层/事件史/序列…> 及理由
【关键构念操作化】<…>
【机制】社会过程 = <…>（→ socs-mechanism-social-process）
【异质性】按 <结构位置> + 社会学解释
【下一步】socs-mechanism-social-process
```
