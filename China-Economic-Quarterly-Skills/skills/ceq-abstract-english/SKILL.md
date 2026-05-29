---
name: ceq-abstract-english
description: Use when writing or polishing the English abstract and contribution statement for a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript — producing a tight English abstract (≤ ~100 words per the journal's guideline) that reads to a field economist and benchmarks the contribution against specific papers. Use at the polish stage, after identification and results are final.
---

# 英文摘要与贡献陈述（ceq-abstract-english）

## 触发时机

- 英文摘要质量差 / 中式英语 / 超长
- 贡献写成"This paper enriches the literature on…"
- 定稿前，主结果与识别已确定

## 为什么重要

CEQ 很多读者**只读英文摘要 + 图**（见 `ceq-figures`）。英文摘要 = 你的门面。它必须让 field 经济学家在 100 词内看懂：**问什么、怎么识别、发现什么、相对谁是新的**。CEQ 规范：英文摘要不超过约 100 个单词，三个中英文关键词，三个 JEL 号（详见 `resources/journal-profile.md`）。

## 五句法（控制在 ~100 词）

1. **问题**：研究的因果问题（一句，去本土包装）。
2. **设计**：识别来源（"Using the staggered rollout of …, we …"）。
3. **发现**：量化主结果 + 单位（"… raises Y by X%"）。
4. **机制**：一句话渠道。
5. **贡献/含义**：相对最近文献的差异，或一句政策/理论含义。

## 好坏对照

| 黑名单（中式/空话） | 白名单（field 可读） |
|---------------------|----------------------|
| "This paper enriches the literature." | "We provide the first credibly identified estimate of …" |
| "We use a series of robust methods." | "Using a regression discontinuity at the eligibility cutoff …" |
| "The results have important policy implications." | "A 10% increase in X reduces Y by 4%, implying …" |
| "Our study fills a gap in domestic research." | "Unlike Author (Year), who rely on OLS, we exploit …" |

## 英文写作规范

- 主动语态、现在时陈述发现；避免冗长从句。
- 量化结果带单位与符号方向，别只说"significant"。
- 术语用 field 标准词（identification, parallel trends, instrument），不要直译中文。
- 不堆方法名词；识别策略一句带过即可。
- 中英文摘要表意一致，但英文不必逐句直译中文。

## 自检清单

- [ ] 英文摘要 ≤ ~100 词（按官网规范复核）
- [ ] 五要素齐：问题/设计/发现/机制/贡献
- [ ] 主结果量化、带单位与方向
- [ ] 贡献对标具体文献，无 "enrich/fill the gap" 套话
- [ ] field 同行不读正文即可懂贡献
- [ ] 三个关键词、三个 JEL 号已备（见 `ceq-submission`）

## 反模式

- 英文摘要是中文摘要的机器直译
- 通篇 "significant" 不给数字
- 罗列方法却不说识别从哪来
- 用大词收尾（"profound implications"）替代具体含义

## 输出格式

```
【英文摘要词数】X / ≤100
【五要素】问题□ 设计□ 发现(量化)□ 机制□ 贡献□
【套话命中】X 处：[...]
【贡献对标】具体文献 □ / 仍套话（需改）
【关键词/JEL】3 关键词 □ 3 JEL □
【下一步】ceq-submission
```
