---
name: jwe-workflow
description: Use when deciding which jwe-* sub-skill to invoke next, or when sequencing manuscript work from open-economy positioning through rebuttal for 《世界经济》 (The Journal of World Economy). Routes — does not replace — the specialized skills, and cross-refers to economic-research / china-economic-quarterly / journal-of-financial-research / china-industrial-economics when the paper is really domestic.
---

# 《世界经济》工作流（jwe-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 jwe-* skill**。

默认假设：目标是国内国际经济学 / 开放宏观第一刊《世界经济》（中国社会科学院主管，中国世界经济学会与世界经济与政治研究所主办，月刊）。核心标识是**国际 / 开放维度 + 明确传导渠道**，而非"贴一句全球化"的国内政策评估。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能投《世界经济》/ 下一步做什么"
- 手头有发现但讲不清"国际 / 开放维度"或"传导渠道"
- 学科归属摇摆：到底投《世界经济》还是《金融研究》/《中国工业经济》
- 收到外审意见（R&R）需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定开放维度立不立得住、对不对口 | `jwe-fit-positioning` |
| 选题像国内问题，缺国际视角的因果问句 | `jwe-topic-international` |
| 文献只堆国内实证，没进国际贸易/金融脉络 | `jwe-literature-review` |
| 数据是一般省级面板，不像国际经济研究 | `jwe-data-sources` |
| 识别只有 OLS / shift-share 不讨论暴露外生性 | `jwe-identification` |
| 机制停在"促进了出口"，没说清渠道 | `jwe-transmission-channel` |
| 异质性只切东中西 / 维度太少 | `jwe-heterogeneity` |
| 主表列数过多 / 图表不规范 | `jwe-tables-figures` |
| 政策含义写成国内操作清单 | `jwe-policy-implication` |
| 准备投稿，需要体例与系统 checklist | `jwe-submission` |
| 收到 R&R，需要写回复 | `jwe-rebuttal` |

## 默认顺序

1. `jwe-fit-positioning` — 先判断开放维度，别把国内稿硬投本刊
2. `jwe-topic-international` — 把"国际视角的因果问句"立住
3. `jwe-literature-review` — 进入国际贸易/国际金融脉络对话
4. `jwe-data-sources` — 选对口数据（海关/跨国/GVC）
5. `jwe-identification` — 外部冲击 + shift-share/引力，含推断批评
6. `jwe-transmission-channel` — 讲清传导渠道
7. `jwe-heterogeneity` — 按暴露度/企业/国别/边际切分
8. `jwe-tables-figures` — 主表主图最终化
9. `jwe-policy-implication` — 落在开放政策层
10. `jwe-submission` — 投稿前 preflight（页下注、www.jweonline.cn）
11. `jwe-rebuttal` — 外审后

## 决策口诀

- "外部冲击/开放政策 + 传导渠道" → 本刊对口（`jwe-fit-positioning` 确认）
- "国际只是引言一句话" → `jwe-topic-international`（上移到开放维度）
- "文献全是国内回归" → `jwe-literature-review`
- "机制只说促进了出口" → `jwe-transmission-channel`
- "政策建议是加强完善推进" → `jwe-policy-implication`

## 与本仓库其它期刊包的差异（跨刊改投）

- 落点在**银行 / 货币政策 / 资本市场 / 公司金融** → 转 **journal-of-financial-research**（《金融研究》）
- 落点在**国内产业 / 企业行为 / 产业政策** → 转 **china-industrial-economics**（《中国工业经济》）
- **纯国内干净因果 + 一般均衡理论** → 转 **economic-research / china-economic-quarterly**（《经济研究》/《经济学季刊》）
- 《世界经济》要的是**开放经济中的因果 + 传导渠道 + 国际对话**，国内数据/政策只是工具

## 反模式

- **不要**跳过 `jwe-fit-positioning` 就动笔——它最常救稿（避免投错门）
- **不要**在开放维度没立住时就抠摘要、美化表格
- **不要**让 `jwe-rebuttal` 在正文未修订前生成回复
