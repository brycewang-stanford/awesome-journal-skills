---
name: jqte-econometric-methods
description: Use when the empirical core of a 《数量经济技术经济研究》 (JQTE) manuscript is an econometric model — time series, cointegration, mixed-frequency, VAR/SVAR, state-space, or panel / macro-econometrics. Enforces correct model setup, stationarity / unit-root and cointegration diagnostics, and lag/specification justification. Use when the method itself is the contribution rather than a causal identification claim.
---

# 计量方法（jqte-econometric-methods）

## 触发时机

- 实证主体是时间序列 / VAR / 协整 / 混频 / 状态空间 / 宏观面板
- 模型设定、平稳性、滞后阶交代不清，或被质疑"伪回归"
- 方法本身是贡献（把某模型用到中国数据），而非干净因果

## 设定前必查：数据性质决定模型

| 数据性质 | 必做诊断 | 建模含义 |
|----------|----------|----------|
| 单一时间序列 | 单位根（ADF/PP/KPSS）、结构突变（Zivot-Andrews/Bai-Perron） | 非平稳需差分或协整建模 |
| 多变量时间序列 | 单位根 + 协整（Johansen / EG / ARDL 边界） | 协整存在用 VECM，否则差分 VAR |
| 混频数据 | 频率对齐方式 | MIDAS / 桥接模型 / 状态空间 |
| 宏观/动态面板 | 截面相关、面板单位根、面板协整 | 跨截面相关需 CCE/CSDL；动态面板用 GMM 并查工具有效性 |

## 各类模型的规范要点

### 时间序列 / VAR / SVAR

- 平稳性先于建模：单位根检验 + 必要的结构突变检验
- 滞后阶用信息准则（AIC/BIC/HQ）选并报告，不凭经验拍
- SVAR 的识别约束（递归/长期/符号约束）显式列出并论证
- 报告脉冲响应、方差分解，必要时给稳定性（伴随矩阵特征根 < 1）

### 协整 / VECM / ARDL

- 报告协整秩检验（迹/最大特征根）或 ARDL 边界检验
- 误差修正项符号与显著性、调整速度解读
- 长期与短期关系分开汇报

### 动态面板 / GMM

- 差分/系统 GMM 选择有依据；工具变量个数受控（避免工具过多）
- 报告 AR(1)/AR(2) 序列相关检验与 Hansen/Sargan 过度识别检验
- 内生变量、外生变量、工具集划分清楚

## 自检清单

- [ ] 先验平稳性/单位根，再建模（防伪回归）
- [ ] 滞后阶/协整秩用准则选并报告
- [ ] 识别约束（SVAR）或工具有效性（GMM）显式论证
- [ ] 报告了必要的诊断（残差自相关、稳定性、过度识别）
- [ ] 方法的适用条件与局限有交代

## 反模式

- 直接对非平稳序列跑 OLS/VAR，不验单位根（伪回归）
- 滞后阶凭经验定，不报准则
- 动态面板工具变量爆炸，Hansen 检验 p 值接近 1 仍不警觉
- 报一堆系数却不解读长期/短期关系或脉冲响应

## 输出格式

```
【模型】时间序列 / VAR-SVAR / 协整-VECM / 混频 / 动态面板
【平稳性】单位根 □ 结构突变 □ 协整 □
【设定】滞后阶 <准则> / 识别约束 <…> / 工具有效性 <…>
【诊断】自相关 □ 稳定性 □ 过度识别 □
【适用条件】<已交代 / 待补>
【下一步】jqte-forecasting / jqte-sensitivity
```
