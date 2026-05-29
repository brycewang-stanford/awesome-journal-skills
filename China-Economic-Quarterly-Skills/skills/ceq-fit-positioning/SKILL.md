---
name: ceq-fit-positioning
description: Use to judge whether a manuscript is on-target for 《经济学(季刊)》 (China Economic Quarterly, CEQ) before investing in revision — CEQ is the strictest Chinese econ journal on identification and the most internationally legible. If the fit is weak, re-route to economic-research / china-industrial-economics / journal-of-financial-research / journal-of-world-economy.
---

# 匹配度判断（ceq-fit-positioning）

## 触发时机

- 拿不准稿子够不够格、对不对口 CEQ
- 在 CEQ 与《经济研究》之间犹豫
- 只有相关性结果，担心识别撑不起来

## CEQ 是什么、不是什么

CEQ 的隐性门槛：**一位海外训练的 field 审稿人，能在读引言+主图后立刻说出"贡献是什么、识别凭什么可信"**。它不是政策刊、不是行业刊、不是"中国故事包装"刊。

## 三维快速诊断

| 维度 | 对口 CEQ（高） | 不对口（改投/补强） |
|------|----------------|---------------------|
| 识别 | 结构模型 + 可信参数，或干净 DID/IV/RDD/event-study | 仅 OLS+控制、相关性当因果 |
| 贡献可对话 | field 同行看引言即懂，不靠本土语境包装 | 贡献="填补国内空白"/"丰富研究" |
| 问题层级 | 机制清楚、可建模、可推广 | 纯描述、纯政策评估、过度琐碎 |

三项均高 → 正中靶心；两项高一项低 → 先补那一项；只有一项高 → 多半应改投。

## 改投决策（re-route）

- 理论贡献厚、识别一般、偏中国制度叙事 → **《经济研究》(economic-research)**
- 产业政策评估、行业层面实证 → **《中国工业经济》(china-industrial-economics)**
- 金融市场、资产定价、银行/公司金融 → **《金融研究》(journal-of-financial-research)**
- 开放宏观、国际贸易、汇率 → **《世界经济》(journal-of-world-economy)**
- 纯相关性、无机制 → 任何刊都先补识别，否则别投

## 自检清单

- [ ] 识别策略是结构或干净准实验，不是 OLS+控制充因果
- [ ] field 审稿人读引言能复述贡献，无需懂本土背景
- [ ] 贡献能对标到 ≥1 篇具体国际/顶刊文献的差异
- [ ] 问题可建模或可推广，不是单一情境的政策评估
- [ ] 主结果可用一张图讲清（见 `ceq-figures`）

## 反模式

- 把"国内首次研究 X"当贡献——CEQ 不看新鲜度，看识别与可对话性
- 用"中国情境特殊"回避识别——审稿人会问"特殊在哪、怎么外生"
- 政策腔贡献（"为政府提供参考"）——CEQ 尤其反感

## 输出格式

```
【匹配度】高 / 中 / 低
【识别维度】结构 / 准实验(类型) / 仅相关（需补）
【可对话性】field 可懂 / 依赖本土包装（需改）
【问题层级】可建模可推广 / 政策评估（需上移）
【建议去向】CEQ / 经济研究 / 工业经济 / 金融研究 / 世界经济
【下一步】ceq-topic-selection 或 ceq-identification
```
