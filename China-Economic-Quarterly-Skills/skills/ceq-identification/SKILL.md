---
name: ceq-identification
description: Use when the identification strategy is the bottleneck for a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript — either a structural model with credible parameters, or a clean quasi-experiment (DID / IV / RDD / event-study). CEQ is the strictest Chinese econ journal here; identification assumptions must be made explicit and each defended. Stress-test the design before drafting exhibits.
---

# 识别策略（ceq-identification）

## 触发时机

- 实证主体仅 OLS + 控制变量，把相关性当因果
- 有处理/外生变异，但识别假设没写清、没逐条辩护
- 拿不准走结构估计还是准实验路线

## CEQ 的铁律：要么结构，要么准实验

CEQ 不接受"加一堆控制变量就声称因果"。两条合法路径：

- **结构估计**：微观基础清晰、识别假设显式、参数有经济含义、能做反事实。
- **准实验**：DID / IV / RDD / event-study，外生变异来源可信、识别假设可检验。

**识别假设必须显式写出，并逐条给经验支持**——这是 CEQ 与多数国内刊的最大差异。

## 设计优先级（强 → 弱）

1. 政策冲击 + DID（含交错/连续处理，须过 `ceq-modern-did`）
2. 断点回归（清晰政策门槛）
3. 工具变量（强工具 + 排他性论证）
4. 倾向得分匹配 + DID
5. 合成控制法
6. 双重机器学习 / 因果森林
7. OLS + 严密内生性讨论（仅在结构/理论实证文章中可接受）

## 分支自检

### DID（→ 详见 ceq-modern-did）
- [ ] 交错处理已用 Callaway–Sant'Anna / de Chaisemartin–D'Haultfœuille / Sun–Abraham
- [ ] 平行趋势：事件研究图必画（见 `ceq-figures`）
- [ ] 安慰剂（随机处理时点/对象）已做

### IV
- [ ] 第一阶段 F 报告，弱工具走 weak-IV-robust（见 `ceq-inference`）
- [ ] 排他性论证 ≥ 3 段（理论/制度/安慰剂）
- [ ] 报告了 reduced form；工具本身外生性有论证

### RDD
- [ ] McCrary / 密度操纵检验
- [ ] 最优带宽（CCT）+ ≥3 个带宽稳健性
- [ ] 协变量在断点处平滑

### 结构估计
- [ ] 识别假设逐条列出并辩护
- [ ] 参数有经济含义、估计稳定
- [ ] 提供反事实 / 福利分析

## 通用必查

- [ ] 识别假设**显式成文**，每条配经验支持
- [ ] 标准误聚类层级有理由（见 `ceq-inference`）
- [ ] 回应"被处理者预期/提前反应"问题
- [ ] 安慰剂/平行趋势/敏感性是**标配而非加分**

## 反模式

- "我们认为该政策外生"却无任何证据
- TWFE + 交错处理不讨论异质性偏误
- IV 用"外生事件 × 上一期内生变量"，说不清为何上一期不影响当期
- RDD 用截断带宽但不汇报带宽敏感性
- 把稳健性当摆设，不汇报不利结果

## 输出格式

```
【识别策略】结构 / DID / IV / RDD / DML / 仅相关（需补）
【识别假设是否显式】是 / 否 <补>
【已完成检验】[平行趋势, 安慰剂, 弱工具, 密度, ...]
【缺失检验】[...]
【下一步】ceq-modern-did（若 DID）/ ceq-inference / ceq-mechanism
```
