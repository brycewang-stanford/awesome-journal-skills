---
name: cie-institutional-background
description: Use when the policy / institutional background section of a 《中国工业经济》 (China Industrial Economics) manuscript needs accurate detail — exact document names, effective dates, pilot batches and city lists, and the assignment rule that justifies the quasi-experiment. Sloppy policy detail is a frequent desk-reject trigger here.
---

# 制度背景（cie-institutional-background）

## 触发时机

- 制度背景段只说"近年来国家高度重视…"，无文件、无时点
- DID 的处理组/时点说不清来源
- 试点是分批的，但稿子当成一次性冲击
- 审稿人质疑"政策是否外生 / 是否被预期"

## 为什么本刊特别看重这一段

本刊实证工程化，**识别的合法性几乎全押在制度细节上**。处理时点、处理对象、分配规则讲不准，后面所有 DID / event-study 都站不住。这也是高频拒稿/退修点。

## 必须讲准的要素

1. **政策文件**：准确的文件名称、发文机关、发文时间（不要只写"国家出台政策"）
2. **生效/执行时点**：政策何时落地——决定 DID 的处理时点；分批试点要逐批列时点
3. **处理对象**：哪些城市/行业/企业被覆盖；**分批试点必须给出批次与名单来源**
4. **分配规则**：为什么这些对象被选中——这是平行趋势/外生性论证的根基
5. **政策内容**：政策到底"做了什么"，对应理论机制的哪一环

## 把制度细节接到识别上

- 分配规则若与结果变量相关 → 平行趋势可能不成立 → 预告需要 PSM-DID / 控制趋势（转 `cie-robustness`）
- 分批试点 → 交错 DID → 必须用异质性稳健估计（转 `cie-did-identification`）
- 政策被预期 / 提前响应 → event-study 的 pre-trend 与"预期效应"讨论

## 自检清单

- [ ] 政策文件名、发文机关、时间**精确**（可核查）
- [ ] 处理时点明确；分批试点逐批列时点与名单来源
- [ ] 处理对象与分配规则讲清，并接到外生性论证
- [ ] 制度内容对应理论机制的具体环节
- [ ] 时点与数据期对齐（避免处理后样本不足）

## 反模式

- "近年来，随着…国家日益重视…"开篇却无任何文件/时点
- 把分批试点当一次性冲击，忽视交错处理
- 制度背景与识别脱节，读完不知处理组怎么来的
- 政策名称简写/记错（如把"重大项目"写成"重大"，文件年份记错）

## 输出格式

```
【政策】<文件名 + 发文机关 + 时间>（可核查 √ / 待核实）
【处理时点】<单一 / 分批：批次+时点>
【处理对象】<范围 + 名单来源>
【分配规则】<外生论证强 / 弱 → 需 PSM/趋势控制>
【接识别】交错 □ 预期效应 □ 平行趋势风险 □
【下一步】cie-did-identification
```
