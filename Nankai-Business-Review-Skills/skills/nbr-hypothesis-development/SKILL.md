---
name: nbr-hypothesis-development
description: Use to develop hypotheses for 《南开管理评论》 (Nankai Business Review) so each is backed by an explicit theoretical mechanism, not intuition. Use when hypotheses read as "we expect a positive relationship", when mediation/moderation logic is asserted without a mechanism, or when the hypothesis set is not derived from the theory invoked in the introduction.
---

# 假设推演（nbr-hypothesis-development）

## 触发时机

- 假设写成"X 与 Y 正相关/负相关"，没讲为什么
- 中介/调节只是"加变量"，没有理论逻辑
- 假设与引言所用理论脱节，像事后补的

## 核心原则：每条假设 = 一条机理链

合格的假设推演必须显化**机制链**：
```
X 通过 <理论机制M> 影响 Y（H1）。
因为 <理论T 主张……>，所以在 <条件> 下，X→M→Y。
```
机制必须来自**理论**（如社会交换、资源基础观、自我决定、制度理论、计划行为、调节焦点等），不是"常识上应该"。

## 四类假设的机理要求

| 假设类型 | 必须讲清 |
|----------|----------|
| 主效应 H：X→Y | 一条可命名的理论机制，而非相关性观察 |
| 中介 H：X→M→Y | M 为何被 X 激发、M 为何驱动 Y，两段都要机理 |
| 调节 H：W 调节 X→Y | W 为何**改变机制强度/方向**，而非另一个主效应 |
| 被调节的中介 | 指明 W 调节的是 X→M 还是 M→Y 哪一段，并说清理由 |

## 自检清单

- [ ] 每条假设都能指出一个**有名字的理论机制**
- [ ] 中介两段（X→M、M→Y）各有机理，不是只论一段
- [ ] 调节讲的是"改变机制"，不是又一个独立主效应
- [ ] 被调节的中介明确作用于哪一段路径
- [ ] 假设方向与机理一致（别机理讲增强、假设写负向）
- [ ] 假设集与引言理论缺口同源，首尾闭环

## 反模式

- "已有研究多为正相关，故提出 H：正相关"（用相关代替机制）
- 调节变量与自变量其实是两个平行主效应，硬包装成交互
- 一口气提 8 条假设却共用一句笼统机理
- 机理用的理论和讨论部分回扣的理论不是同一个

## 输出格式

```
【H1 主效应】X→Y｜机制：<理论T 的 M> ｜方向：+/-
【H2 中介】X→M→Y｜X→M 机理：<…>｜M→Y 机理：<…>
【H3 调节】W × (X→Y)｜W 如何改变机制：<增强/削弱/反转>
【H4 被调节中介】W 作用于 <X→M / M→Y>｜理由：<…>
【一致性】方向与机理一致□ 与缺口同源□
【下一步】nbr-measurement
```
