---
name: cie-robustness
description: Use when building or auditing the robustness section of a 《中国工业经济》 (China Industrial Economics) manuscript — the journal's signature "arms race." Drives an exhaustive checklist: alternative measures, dropping competing policies, PSM-DID, changing windows/samples, placebo, winsorizing, and explicitly ruling out alternative explanations. Doing this thoroughly is the norm, not the exception.
---

# 稳健性"军备竞赛"（cie-robustness）

## 触发时机

- 稳健性只有 1—2 个检验，审稿人一问就塌
- 担心"换个度量结论就变"
- 审稿人反复要求"再补稳健性 / 排除其他解释"

## 为什么这是本刊招牌

《中国工业经济》以**实证工程化**著称——**稳健性做满是常态而非加分**。审稿人默认你已穷尽常规检验；缺一项就退修。把稳健性当作"主动堵住每一个可能的反驳"。

## 稳健性"军备竞赛"清单（按需做满）

### 一、变量与度量

- [ ] **替换核心解释变量度量**（口径/来源/构造方式）
- [ ] **替换被解释变量度量**（如 TFP：OP/LP/ACF 多法对照）
- [ ] 替换/增减控制变量集
- [ ] 关键连续变量 **1%/99% 缩尾（winsorize）** 或截尾对照

### 二、样本与窗口

- [ ] **剔除同期竞争性政策**样本（其他试点城市/行业）
- [ ] 改变**时间窗口**（缩短/延长事件窗）
- [ ] 剔除直辖市 / 特殊样本 / 极端行业
- [ ] 排除政策预期期（处理前 1 期样本剔除）

### 三、识别加固

- [ ] **PSM-DID**（先匹配再 DID，报告匹配后平衡性）
- [ ] 安慰剂（时点随机 + 对象随机，见 `cie-did-identification`）
- [ ] 异质性稳健估计与 TWFE 对照（交错处理，见 `cie-did-identification`）
- [ ] 工具变量 / Heckman（如存在选择或内生）
- [ ] 改变聚类层级 / Bootstrap 标准误 / 双向聚类

### 四、排除竞争性解释（本刊最看重）

- [ ] 逐条列出**替代解释**，用检验或证据排除
- [ ] 控制可能的混淆同期冲击（其他政策、宏观周期）
- [ ] "反向因果 / 遗漏变量"的针对性回应

## 组织原则

- 不要堆 20 个检验却无主次；按"度量—样本—识别—排除解释"四块组织
- 每个稳健性后**一句话**说明"结论是否稳定、系数量级是否接近"
- 大批量结果可放附录/在线附录，正文留关键几项

## 自检清单

- [ ] 四大块（度量 / 样本 / 识别 / 排除解释）都有覆盖
- [ ] **排除竞争性解释**是显性章节，不是一句带过
- [ ] PSM-DID + 安慰剂 + 替换度量 至少齐全
- [ ] 每个检验后有"是否稳定"的结论句
- [ ] 系数量级在各检验间基本一致（不只看星号）

## 反模式

- 稳健性 = "换个控制变量"一项就收
- 只报系数仍显著，不比量级是否漂移
- 不剔除同期竞争性政策（审稿人必问）
- 替代解释只口头否认，无检验
- 把所有检验塞正文，主次不分

## 输出格式

```
【度量】替换X □ 替换Y □ 缩尾 □
【样本/窗口】剔竞争政策 □ 改窗口 □ 剔特殊样本 □
【识别加固】PSM-DID □ 安慰剂 □ 异质稳健估计 □ IV/Heckman □
【排除解释】<已排除…> / 待补 <…>
【量级稳定性】稳定 / 漂移 <说明>
【下一步】cie-tables-figures
```
