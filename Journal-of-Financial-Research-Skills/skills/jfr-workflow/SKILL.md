---
name: jfr-workflow
description: Use when deciding which jfr-* sub-skill to invoke next, or when sequencing manuscript work from fit positioning through rebuttal for 《金融研究》 (Journal of Financial Research). Routes — does not replace — the specialized skills, and cross-refs sibling journal packs.
---

# 《金融研究》工作流（jfr-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 jfr-* skill**。

默认假设：目标是国内金融学第一刊《金融研究》（中国金融学会主办，中国人民银行金融研究所编辑出版，月刊）。衡量标准是**严谨识别 + 对中国金融体系/政策的现实意义**。该刊有两大支流：**宏观金融**（货币政策、银行、金融稳定、监管）与**微观公司金融**（公司金融、资本市场、治理）。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能冲《金融研究》/ 下一步做什么"
- 题目摇摆在宏观金融与微观公司金融之间，叙事不一致
- 有实证发现但讲不清金融渠道
- 收到 R&R 外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定对不对口、是宏观还是微观线 | `jfr-fit-positioning` |
| 选题模糊、金融贡献立不住 | `jfr-topic-selection` |
| 文献只堆近年实证、缺金融经典与机制文献 | `jfr-literature-review` |
| 制度背景写不准（监管口径/市场分层/所有制） | `jfr-institutional-background` |
| 实证只有 OLS、缺政策冲击或识别策略 | `jfr-identification` |
| 主结果有了但停在"促进/抑制"、无金融渠道 | `jfr-mechanism` |
| 没切异质性 / 切分维度太粗 | `jfr-heterogeneity` |
| 主表列数过多 / 注释与编号不合体例 | `jfr-tables-figures` |
| 政策含义空泛、没落到具体金融主体 | `jfr-policy-implication` |
| 准备投稿，需要体例与系统 checklist | `jfr-submission` |
| 收到 R&R，需要写回复 | `jfr-rebuttal` |

## 默认顺序

1. `jfr-fit-positioning` — 先定线别与匹配度，别把产业/会计题硬投金融刊
2. `jfr-topic-selection` — 把金融问题与贡献立住
3. `jfr-literature-review` — 进入金融脉络，中英文并重
4. `jfr-institutional-background` — 把中国金融制度细节讲准
5. `jfr-identification` — 政策冲击/高频识别/DID/IV
6. `jfr-mechanism` — 落到金融渠道
7. `jfr-heterogeneity` — 按所有制/银行类型/市场分层切分
8. `jfr-tables-figures` — 主表/主图终化
9. `jfr-policy-implication` — 面向货币当局/监管/机构
10. `jfr-submission` — 投稿前 preflight（注释、摘要/JEL、系统）
11. `jfr-rebuttal` — R&R 后

## 决策口诀

- "货币/银行/监管/系统性风险" → 宏观金融线（先 `jfr-fit-positioning`）
- "上市公司融资/投资/治理" → 微观公司金融线
- "DID 用了 TWFE 但没回应异质性处理批评" → `jfr-identification`
- "只能说'缓解了融资约束'" → `jfr-mechanism`
- "读起来像产业政策实证" → 见下方改投

## 与本仓库其它期刊包的差异

- 偏干净因果 + 理论：转 [economic-research](https://github.com/brycewang-stanford/awesome-journal-skills)
- 偏前沿计量 + 理论实证：转 [china-economic-quarterly](https://github.com/brycewang-stanford/awesome-journal-skills)
- 落点在产业升级而非金融机理：转 [china-industrial-economics](https://github.com/brycewang-stanford/awesome-journal-skills)
- 落点在公司治理的管理学理论 / 案例：转 [nankai-business-review](https://github.com/brycewang-stanford/awesome-journal-skills)
- 落点在会计信息、审计、盈余质量：转 [accounting-research](https://github.com/brycewang-stanford/awesome-journal-skills)
- 《金融研究》要的是**金融机理 + 可信识别 + 制度准确**，三者缺一不可

## 反模式

- **不要**跳过 `jfr-fit-positioning` 就动笔——线别错了全文都歪
- **不要**在识别策略未立住时去美化表格或抠摘要
- **不要**让 `jfr-rebuttal` 在正文未修订前生成回复
