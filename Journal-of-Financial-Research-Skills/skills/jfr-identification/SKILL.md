---
name: jfr-identification
description: Use when the identification strategy is the bottleneck for a 《金融研究》 (Journal of Financial Research) manuscript — policy shocks (MPA / 资管新规 / LPR / 注册制), high-frequency monetary-policy surprises, DID, IV, RDD — stress-testing the design before drafting tables.
---

# 因果识别策略（jfr-identification）

## 触发时机

- 实证主体仅 OLS + 控制变量，谈"相关"不谈"因果"
- 宏观题靠时间序列相关讲故事，缺冲击识别
- DID 用 TWFE 但没回应异质性处理批评
- IV 第一阶段弱 / 排他性存疑

## 设计优先级（《金融研究》口味，强 → 弱）

1. **自然实验式政策冲击 + DID**（MPA 考核、资管新规、LPR 改革、注册制等监管/政策变动）
2. **高频识别**：货币政策意外（政策公告窗口的利率/价格高频反应）
3. **断点回归**（清晰的监管门槛：资本充足率、规模、评级阈值）
4. **工具变量**（强工具 + 排他性论证；金融题常用制度/地理/历史工具）
5. **倾向得分匹配 + DID**
6. 宏观时序方法：**VAR / 局部投影（local projection）/ 符号约束**，用于刻画传导
7. OLS + 严密内生性讨论（结构估计或理论实证中可接受）

## 分支路径

### 分支 A：政策冲击 DID

- 是否 staggered（分批生效）？→ 必须 Goodman-Bacon 分解 + Callaway-Sant'Anna 或 Sun-Abraham
- 平行趋势：事件研究图必画；处理前系数应不显著
- 安慰剂：随机分配处理组/处理时点 500–1000 次
- 把"政策外生于个体决策"用制度细节论证（见 jfr-institutional-background）

### 分支 B：高频货币政策意外

- 用政策公告窗口（如 MLF/OMO/LPR 公布）的高频价格变动构造意外
- 窗口选择与基准资产说明清楚；剔除同窗其它信息
- 与低频结果交叉印证（局部投影 IRF）

### 分支 C：宏观传导（VAR/LP）

- 识别假设明确（递归/符号约束/外部工具）
- 报告脉冲响应 + 置信带；稳健于滞后阶数与变量排序
- 区分"价格型"与"数量型"货币政策工具

### 分支 D：IV / RDD

- IV 第一阶段 F **≥ 10**（弱工具 → Anderson-Rubin 稳健 CI）；排他性给理论/制度/安慰剂三段；报告 reduced form
- RDD：McCrary 操纵检验 + 最优带宽（CCT）+ ≥ 3 个带宽稳健性 + 协变量平滑

## 必查清单

- [ ] 平行趋势 / 平滑性 / 弱工具 检验齐全
- [ ] 安慰剂（处理对象/时点随机）做了
- [ ] 标准误聚类层次合理（公司/银行/行业/地区 × 时间）
- [ ] 风险类指标稳健（VaR/CoVaR/SRISK 等口径一致）
- [ ] 回应"预期效应/抢跑"（政策前调整）

## 反模式

- TWFE + staggered 不谈异质性处理偏误
- 货币政策题用时序相关冒充因果，无冲击识别
- "我们认为该监管外生于公司决策"却无制度/数据证据
- IV 用"外生事件 × 上期内生变量"，排他性站不住
- 风险度量随意（VaR 与 CoVaR 混用口径）

## 输出格式

```
【识别策略】政策冲击DID / 高频意外 / VAR-LP / IV / RDD / 结构
【已完成检验】[平行趋势, 安慰剂, 弱工具, McCrary, ...]
【缺失检验】[...]
【聚类层次】...
【外生性论证】制度□ 数据□ 安慰剂□
【下一步】jfr-mechanism
```
