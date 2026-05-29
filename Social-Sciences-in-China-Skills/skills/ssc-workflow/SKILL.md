---
name: ssc-workflow
description: Use when deciding which ssc-* sub-skill to invoke next, or when sequencing manuscript work from problematic framing through rebuttal for 《中国社会科学》 (Social Sciences in China). Routes — does not replace — the specialized skills.
---

# 《中国社会科学》工作流（ssc-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 ssc-* skill**。

默认假设：目标是中国社科最高综合平台《中国社会科学》（中国社会科学院主办，月刊）。衡量标准是**思想分量与原创理论贡献**，而非方法复杂度。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能冲《中国社会科学》/ 下一步做什么"
- 手头有实证发现但讲不出"大问题/原创命题"
- 学科归属摇摆，不知往哪个学科叙事靠
- 收到外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定稿子够不够格、对不对口 | `ssc-fit-positioning` |
| 问题太小 / 立不住"重大问题" | `ssc-topic-problematic` |
| 有发现没"原创理论命题"、不知如何谈贡献 | `ssc-theory-contribution` |
| 文献只堆近年实证、没进理论脉络 | `ssc-literature-dialogue` |
| 论证跳跃 / 思辨不严谨 / 概念界定含糊 | `ssc-argumentation` |
| 经验材料（定量/定性/历史）与论题脱节 | `ssc-evidence` |
| 通篇政策汇报腔 / 口号化 / 炫技 | `ssc-style` |
| 摘要写成套话 / 不合 200–300 字规范 | `ssc-abstract-keywords` |
| 准备投稿，需要体例与系统 checklist | `ssc-submission` |
| 收到外审意见，需要写回复 | `ssc-rebuttal` |

## 默认顺序

1. `ssc-fit-positioning` — 先判断匹配度，别把细分实证硬投综合刊
2. `ssc-topic-problematic` — 把"重大问题/问题意识"立住
3. `ssc-theory-contribution` — 提炼原创理论命题与自主知识体系定位
4. `ssc-literature-dialogue` — 进入理论脉络对话
5. `ssc-argumentation` — 论证链与思辨规范
6. `ssc-evidence` — 经验证据服务论题（方法多元）
7. `ssc-style` — 学理文风，去口号化
8. `ssc-abstract-keywords` — 摘要 200–300 字 + 3–5 关键词
9. `ssc-submission` — 投稿前 preflight（页下注、投稿系统）
10. `ssc-rebuttal` — 外审后

## 决策口诀

- "我有发现但没命题" → `ssc-theory-contribution`（命题立不住就别投）
- "问题像是某行业的细分评估" → `ssc-topic-problematic`（上移到制度/文明层）
- "文献全是近五年回归" → `ssc-literature-dialogue`
- "读起来像政策文件" → `ssc-style`

## 与本仓库其它期刊包的差异

- 偏干净因果 + 理论：转 economic-research / china-economic-quarterly
- 偏产业政策实证：转 china-industrial-economics
- 偏定量/定性社会学：转 sociological-studies
- 《中国社会科学》要的是**跨学科的大问题 + 原创理论**，方法只是证据之一

## 反模式

- **不要**跳过 `ssc-fit-positioning` 就动笔——它最常救稿（避免投错门）
- **不要**在没有原创命题时去抠摘要和文风
- **不要**让 `ssc-rebuttal` 在正文未修订前生成回复
