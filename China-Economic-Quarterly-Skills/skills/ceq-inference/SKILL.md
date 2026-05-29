---
name: ceq-inference
description: Use when scrutinizing statistical inference for a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript — choosing and justifying the clustering level, handling weak instruments with robust inference, correcting for multiple hypothesis testing, and reporting standard errors that survive a technical reviewer. Default robust SEs are rarely enough at CEQ.
---

# 推断细节（ceq-inference）

## 触发时机

- 标准误用了默认稳健，但没说聚类层级理由
- 第一阶段 F 偏低 / 工具偏弱
- 跑了大量子样本/异质性，没做多重检验校正
- 审稿人会逐条挑推断的稿子

## CEQ 视角：推断是技术审稿的主战场

海外训练的审稿人会盯：**聚类层级、弱工具、多重检验、有限样本**。点估计漂亮但推断站不住，照样退。

## 1. 聚类层级（要给理由，不是默认）

- 聚类应与**处理/抽样的层级**一致：处理在省级，就省级聚类（即使样本在个体）。
- 簇数太少（< ~30–50）→ 用 wild cluster bootstrap（Cameron-Gelbach-Miller）。
- 面板同时考虑双向聚类（个体 + 时间）是否必要。
- [ ] 聚类层级与处理分配层级一致，且写明理由
- [ ] 少簇情形用 wild bootstrap

## 2. 弱工具（IV）

- 第一阶段 F 报告；多工具用 Kleibergen-Paap（非同方差稳健）而非简单 F。
- F 偏弱 → 用 **Anderson-Rubin** 等 weak-IV-robust 置信区间，别只靠 t 比。
- 报告 reduced form 与第一阶段，别只给 2SLS。
- [ ] F / KP 报告；弱则给 AR 区间
- [ ] reduced form 与第一阶段都展示

## 3. 多重假设检验

- 跑了多个结果变量 / 多个子组 → Romano-Wolf、List-Shaikh-Xu，或 BH/Bonferroni 校正。
- 异质性"找显著"要预警 p-hacking；最好预先登记或限制切分维度。
- [ ] 多结果/多子组已做 MHT 校正
- [ ] 异质性切分有理论依据，非数据挖掘

## 4. 标准误与有限样本

- DID 现代估计量用其配套（解析或 bootstrap）标准误，别套 TWFE 的。
- 小样本/少处理单位 → 随机化推断（permutation / placebo 分布）。
- [ ] 估计量与标准误匹配
- [ ] 必要时随机化推断

## 反模式

- "标准误聚类到个体层"但处理在省级——典型低估
- 只报 2SLS t 值，不管弱工具
- 报告 20 个异质性里挑出的 2 个显著，不做校正
- 现代 DID 估计量配 TWFE 标准误

## 输出格式

```
【聚类层级】... | 与处理层级一致 □ | 少簇 bootstrap □
【弱工具】F/KP=... | AR 区间 □ | reduced form □
【多重检验】结果数=.. 子组数=.. | 校正方法=..
【标准误-估计量匹配】是 / 否
【缺口】<待补>
【下一步】ceq-mechanism
```
