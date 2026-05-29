---
name: cie-workflow
description: Use when deciding which cie-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《中国工业经济》 (China Industrial Economics). Routes — does not replace — the specialized skills, and cross-references sibling journal packages.
---

# 《中国工业经济》工作流（cie-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 cie-* skill**。

默认假设：目标是 CSSCI 产业经济实证顶刊《中国工业经济》（中国社会科学院工业经济研究所主办，月刊）。本刊的标志是**实证工程化**——办刊理念"理论顶天，实践立地"，要求识别干净、稳健性做满、机制+异质性齐备、政策含义可落地。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能冲《中国工业经济》/ 下一步做什么"
- 有政策冲击 + 数据，但识别、稳健性、机制拿不准
- 稿子被审稿人要求"再补一堆稳健性"
- 收到外审 / R&R 意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定够不够格、对不对口（理论太重？偏管理？） | `cie-fit-positioning` |
| 选题模糊 / 没有干净政策冲击或特征事实 | `cie-topic-selection` |
| 文献只堆近年回归、没述评不足 | `cie-literature-review` |
| 政策细节、试点名单、时点讲不准 | `cie-institutional-background` |
| 实证只有 OLS / TWFE，未回应交错处理偏误 | `cie-did-identification` |
| 有主结果没机制，或只会三步中介 | `cie-mechanism` |
| 异质性只切"东中西"一刀 | `cie-heterogeneity` |
| 稳健性单薄，一问就塌 | `cie-robustness` |
| 表格列数过多 / 只报显著性不报量级 | `cie-tables-figures` |
| 政策建议是"加强完善推进"四件套 | `cie-policy-implication` |
| 准备投稿，需要体例与系统 checklist | `cie-submission` |
| 收到外审意见，需要写回复 | `cie-rebuttal` |

## 默认顺序

1. `cie-fit-positioning` — 先判断匹配度，别把理论文/案例文硬投实证刊
2. `cie-topic-selection` — 政策准实验 / 企业行为 / 产业组织 / 数字经济
3. `cie-literature-review` — 述评不足，体现前沿性
4. `cie-institutional-background` — 政策细节、时点、试点名单讲准
5. `cie-did-identification` — 多期 DID / event-study（平行趋势+安慰剂+异质性稳健估计，强制）
6. `cie-mechanism` — 分渠道 / 调节，慎用三步中介
7. `cie-heterogeneity` — 多维切分 + 经济含义
8. `cie-robustness` — 本刊招牌：稳健性"军备竞赛"
9. `cie-tables-figures` — 主表后必有经济量级解读
10. `cie-policy-implication` — 可操作政策含义
11. `cie-submission` — 投稿前 preflight（页下注、实引、投稿系统、数据代码）
12. `cie-rebuttal` — 外审 / R&R 后

## 决策口诀

- "我有干净政策冲击 + 厚稳健性 + 落地政策" → 本刊正中
- "TWFE + 交错处理但不谈异质性偏误" → `cie-did-identification`
- "机制只有三步中介" → `cie-mechanism`（编委对其有保留，见江艇 2022）
- "审稿人又要我补稳健性" → `cie-robustness`
- "主表只报星号不报量级" → `cie-tables-figures`

## 与本仓库其它期刊包的差异（改投路由）

- **理论贡献厚于实证 / 偏纯因果机理** → 转 economic-research（《经济研究》）、china-economic-quarterly（《经济学（季刊）》）
- **偏管理理论 / 案例 / 问卷 / 实务** → 转 management-world（《管理世界》）
- **落点在金融机理 / 资产定价 / 银行信贷** → 转 journal-of-financial-research（《金融研究》）
- **落点在国际贸易 / 开放宏观 / 汇率** → 转 journal-of-world-economy（《世界经济》）
- 《中国工业经济》要的是**干净识别 + 做满的稳健性 + 落地的产业政策**

## 反模式

- **不要**跳过 `cie-fit-positioning` 就动笔——它最常救稿（避免投错门）
- **不要**在识别策略未立住时就去美化表格、抠摘要
- **不要**让 `cie-rebuttal` 在正文未修订前生成回复
