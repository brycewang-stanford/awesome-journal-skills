---
name: jmsc-workflow
description: Use when deciding which jmsc-* sub-skill to invoke next, or when sequencing a 《管理科学学报》 (Journal of Management Sciences in China) manuscript from decision-problem formulation through rebuttal. The key fork is 数理 (model/proof/algorithm) vs 经验实证 (regression/survey). Routes — does not replace — the specialized skills.
---

# 《管理科学学报》工作流（jmsc-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 jmsc-* skill**。

默认假设：目标是数理/定量管理科学顶刊《管理科学学报》（国家自然科学基金委员会管理科学部 + 天津大学主办，月刊）。衡量标准是**方法贡献与数理严谨性**——模型、证明、算法、数值实验，而非政策含义或经验叙事。基础事实见 `resources/journal-profile.md`。

## 关键分叉：数理 vs 经验实证

落笔前先判断稿件的**交付物形态**：

- **数理型**（本刊主线）：决策问题 → 模型 → 命题/定理（有证明）→ 算法（复杂度/收敛）→ 数值实验 → 管理洞见。
- **经验实证型**：因变量 + 回归识别 + 政策含义，或问卷-SEM——**多半不对口**，先过 `jmsc-fit-positioning`，再决定改投。

## 触发时机

- 用户问"这篇能不能投《管理科学学报》/ 下一步做什么"
- 有模型但命题没证明，或算法没复杂度分析
- 手头是回归结果 + 政策建议，不确定是否对口
- 收到外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定对不对口（像回归+政策 / 问卷-SEM） | `jmsc-fit-positioning` |
| 决策问题说不清楚、要素散乱 | `jmsc-problem-formulation` |
| 模型设定不完整（变量/约束/目标/假设缺项） | `jmsc-model-building` |
| 有结论但没命题/定理，或证明不全 | `jmsc-proofs` |
| 算法没复杂度 / 没收敛性论证 | `jmsc-algorithm` |
| 没数值实验，或实验单薄、没洞见 | `jmsc-numerical-experiments` |
| 用实验数据刻画行为偏差（行为运作） | `jmsc-behavioral-om` |
| 管理启示写成政策口号 | `jmsc-managerial-insights` |
| 记号混乱 / 假设不显式 / 正文被证明压垮 | `jmsc-notation-style` |
| 准备投稿，需要体例与系统 checklist | `jmsc-submission` |
| 收到外审意见，需要写回复 | `jmsc-rebuttal` |

## 默认顺序（数理主线）

1. `jmsc-fit-positioning` — 先判数理 vs 经验，别把回归稿硬投数理刊
2. `jmsc-problem-formulation` — 把决策问题形式化
3. `jmsc-model-building` — 变量/约束/目标/假设全部显式
4. `jmsc-proofs` — 命题/定理 + 证明，逻辑完整
5. `jmsc-algorithm` — 算法设计 + 复杂度/收敛性
6. `jmsc-numerical-experiments` — 仿真验证理论性质
7. `jmsc-managerial-insights` — 从模型导出决策规律
8. `jmsc-notation-style` — 记号统一、证明入附录
9. `jmsc-submission` — 投稿前 preflight
10. `jmsc-rebuttal` — 外审后

> 行为运作稿在第 2–3 步并入 `jmsc-behavioral-om`（实验设计 + 模型识别）。
> `jmsc-notation-style` 是后段统稿，别在命题未立住时去抠记号。

## 决策口诀

- "有模型没证明" → `jmsc-proofs`（命题立不住就别投）
- "算法只说跑得快" → `jmsc-algorithm`（要复杂度/收敛）
- "结论是回归系数 + 政策建议" → `jmsc-fit-positioning`（多半改投）
- "管理启示是'加强完善推进'" → `jmsc-managerial-insights`

## 与本仓库其它期刊包的差异

- 偏经验实证 / 案例 / 政策评估：转 **管理世界**（management-world）
- 偏组织行为理论建构 / 问卷-SEM：转 **南开管理评论**（nankai-business-review）
- 偏资产定价实证 / 金融市场经验：转 **金融研究**（journal-of-financial-research）
- 《管理科学学报》要的是**模型 + 证明 + 算法 + 数值洞见**，经验数据只是验证手段之一

## 反模式

- **不要**跳过 `jmsc-fit-positioning` 就动笔——它最常救稿（避免投错赛道）
- **不要**在命题没证明时去做数值实验和文风
- **不要**让 `jmsc-rebuttal` 在正文未修订前生成回复
