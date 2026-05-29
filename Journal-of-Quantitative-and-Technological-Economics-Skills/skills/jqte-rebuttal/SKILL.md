---
name: jqte-rebuttal
description: Use when responding to peer-review / R&R comments on a 《数量经济技术经济研究》 (JQTE) manuscript — structuring a point-by-point response letter that addresses the journal's characteristic concerns (method transparency, measurement / parameter sensitivity, out-of-sample evaluation, CGE/IO reproducibility, data caliber) and reframing weak-causal pushback toward the paper's real measurement contribution. Use only after the manuscript itself is revised.
---

# 外审回复（jqte-rebuttal）

## 触发时机

- 收到 JQTE 外审 / R&R 意见，需要写回复信
- 意见集中在方法透明度、敏感性、样本外评估、可复现、数据口径
- 审稿人用"识别不干净"质疑，但本文贡献其实是测度/方法

## 回复信结构

1. **开头致谢 + 总览**：感谢，并用一段说明主要修改方向（对应哪些核心关切）。
2. **逐条回应**：每条意见 → 回应 → 正文修改位置（页/段/表号）。
3. **无法照办的项**：礼貌说明理由（数据限制、方法适用边界），给出替代方案，不硬顶也不空应付。

## 本刊高频意见与应对

| 审稿意见类型 | 应对要点 |
|--------------|----------|
| "方法构造不透明/无法复现" | 补充设定、参数来源、数据口径；必要时附复现说明或代码可得性 |
| "换个方法/参数结论会不会变" | 补敏感性矩阵（`jqte-sensitivity`），给取值区间与秩稳定性 |
| "预测只有样本内拟合" | 补样本外评估 + 基准对比 + DM 检验（`jqte-forecasting`） |
| "CGE 弹性/闭合无依据" | 逐项给弹性来源、说明闭合并做参数敏感性（`jqte-io-cge`） |
| "因果识别站不住" | 若贡献是测度/方法，**重定位**为测度贡献、淡化因果话术（`jqte-fit-positioning`）；若坚持因果，按现代规范补 |
| "数据口径存疑" | 说明来源、平减、基期，必要时换口径复核 |

## 应对"识别不干净"的特别提示

本刊不强求干净因果。**若审稿人按因果刊标准苛求识别，而本文真正贡献是测度/方法/预测**，应礼貌地把贡献重新框定为测度/方法应用，并指出相应的稳健性已通过敏感性而非安慰剂来保障——而不是硬补一个站不住的工具变量。

## 自检清单

- [ ] 逐条回应，无遗漏；每条标注正文修改位置
- [ ] 方法透明度/可复现的质疑已用具体补充回应
- [ ] 敏感性/样本外评估等"本刊关切"已正面补齐
- [ ] 被质疑因果时，正确区分"重定位测度贡献"还是"补识别"
- [ ] 无法照办项有理由 + 替代方案
- [ ] 语气专业、对事不对人

## 反模式

- 嘴上答应改、正文没改（审稿人会复核）
- 对"无法复现"的质疑空泛辩解，不给具体补充
- 被质疑识别就硬塞一个弱工具变量，而非重定位为测度贡献
- 逐条变成情绪化辩论

## 输出格式

```
【意见总数】N（已逐条 □）
【核心关切】方法透明 / 敏感性 / 样本外 / 可复现 / 数据口径 / 识别
【因果质疑处置】重定位测度贡献 / 按规范补识别
【正文是否已改】是 / 否（未改勿生成终稿回复）
【无法照办项】[条目 + 理由 + 替代]
【下一步】终稿复核 → jqte-submission
```
