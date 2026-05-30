# 《美国管理学会会刊》(AMJ) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Academy of Management Journal 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AMJ-14635a)](https://aom.org/research/journals/journal)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20SSCI-1f6feb)](https://aom.org/research/journals/journal)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国管理学会会刊》(Academy of Management Journal, AMJ)** 投稿的 Agent 技能栈 —— AMJ 是由美国管理学会 (AOM) 出版的、最顶级的*实证*管理学期刊。

本仓库是有立场的。它**不是**通用的"管理学写作"工具箱，而是围绕 AMJ 的核心标准打造的 **AMJ 专用**技能栈：一项扎实的实证研究，**同时要做出清晰的理论贡献**。覆盖范围包括以理论为驱动的选题、先验的理论与假设构建、文献定位、严谨的研究设计与数据分析（多层线性模型/HLM、结构方程模型/SEM、面板数据、实验、多来源数据）、理论贡献的提炼、符合 AOM 体例的图表与文风、ScholarOne 投稿、发展型评审流程，以及多轮 R&R 答复。

> 仅描述持久规范。主编、版面费、确切字数/页数限制及各项政策会变化 —— 请务必以 AMJ 官方投稿页面与当前版本的 AOM Style Guide 为准。

---

## 为什么需要单独的 AMJ 技能栈？

相比纯理论期刊或经济学/金融学期刊，AMJ 的约束有本质差异：

| 约束维度       | 《美国管理学会会刊》(AMJ)                                  | 含义                                                       |
|----------------|------------------------------------------------------------|------------------------------------------------------------|
| 学科           | 实证管理学（组织行为、战略、人力资源、创业、组织理论）       | 纯经济学或纯方法论文章不契合                                |
| 核心标准       | 实证贡献**与**理论贡献兼备                                   | 结果再强、若无理论推进，只算技术报告                        |
| 理论           | 明确的机制；假设须**先验**推导                               | "找空白"(gap-spotting) 与事后假设(HARKing) 是拒稿信号        |
| 设计           | 档案、问卷、实验、多方法、田野 —— 但须**匹配**问题           | 方法必须能够检验假设                                        |
| 效度           | 测量效度、共同方法偏差(CMB)处理、档案数据的内生性            | 单一来源自评或内生性未处理会被惩罚                          |
| 分析           | SEM / HLM / 面板 / 实验，与设计匹配                          | 在嵌套数据上跑 OLS、用因果步骤法做中介都会被点名            |
| 贡献句         | 在引言与讨论中明确"我们学到了什么新理论"                     | 不能含糊带过                                                |
| 体例           | AOM 体例；完整的 引言–理论–方法–结果–讨论 结构              | 篇幅较长；具体限制请核实                                    |
| 流程           | ScholarOne；发展型、多轮 R&R 文化                           | 首轮直接录用几乎闻所未闻                                    |

通用的"科研写作"或"社科方法"技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/amj-skills
/plugin install amj-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/amj-skills.git
cd amj-skills

mkdir -p ~/.claude/skills && cp -R skills/amj-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/amj-* ~/.codex/skills/
```

### 第一条指令

```
用 amj-workflow 告诉我，我这篇 AMJ 稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
amj-topic-selection（选题）
        ▼
amj-theory-development（理论与假设）
        ▼
amj-literature-positioning（文献定位）
        ▼
amj-methods（研究设计）
        ▼
amj-data-analysis（数据分析与效度）
        ▼
amj-contribution-framing（理论贡献提炼）
        ▼
amj-tables-figures（图表）
        ▼
amj-writing-style（文风打磨）
        ▼
amj-submission（投稿前自检）
        ▼
amj-review-process（理解评审流程）
        ▼
amj-rebuttal（R&R 答复）
```

`amj-workflow` 是路由器 —— 它根据你当前所处的阶段告诉你下一步该用哪个 skill。

---

## 技能列表

| Skill                       | 用途                                                                  |
|-----------------------------|-----------------------------------------------------------------------|
| `amj-workflow`              | 路由器 —— 决定下一步调用哪个子技能                                     |
| `amj-topic-selection`       | 理论驱动的选题 + AMJ 契合度判断（对比 AMR/ASQ/SMJ）                    |
| `amj-theory-development`    | 先验的机制与假设；规范地做中介/调节                                    |
| `amj-literature-positioning`| 加入学术对话；用"问题化"取代"找空白"                                   |
| `amj-methods`               | 把设计（档案/问卷/实验/多方法）与研究问题匹配                          |
| `amj-data-analysis`         | 测量效度、CMB、SEM/HLM/面板估计、内生性、稳健性                        |
| `amj-contribution-framing`  | 明确的理论贡献陈述 + 讨论部分                                          |
| `amj-tables-figures`        | 相关/结果表、理论模型图、交互作用图，符合 AOM 体例                     |
| `amj-writing-style`         | 论点前置、主动语态、AOM/APA 体例                                       |
| `amj-submission`            | ScholarOne 投稿前自检 + 稿件模板（匿名化、格式、文件）                 |
| `amj-review-process`        | AMJ 评审/决定如何运作；如何读懂决定信                                  |
| `amj-rebuttal`              | 多轮 R&R 修改与逐条答复信                                              |

### 资源

- [`skills/amj-submission/templates/manuscript_template.md`](skills/amj-submission/templates/manuscript_template.md) —— 完整的 AMJ 稿件结构骨架
- [`skills/amj-submission/templates/checklist.md`](skills/amj-submission/templates/checklist.md) —— 8 类投稿前自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 管理学研究数据源（Compustat / BoardEx / Execucomp / Qualtrics / Prolific）与分析软件（Mplus / R lavaan / HLM / Stata / SPSS PROCESS）

---

## 与 AMR / ASQ / SMJ 的差异

| 维度       | AMJ                          | AMR                 | ASQ                          | SMJ                     |
|------------|------------------------------|---------------------|------------------------------|-------------------------|
| 数据       | **必须**（实证）             | 无（纯理论）        | 实证或理论皆可               | 必须（常为档案数据）    |
| 核心贡献   | 实证**加**理论               | 全新理论            | 大胆的框架、深度情境         | 战略/绩效理论           |
| 标志方法   | SEM / HLM / 面板 / 实验      | 概念论证            | 定性与定量                   | 面板档案、计量          |
| 最契合     | 用数据检验理论的文章         | 纯概念性文章        | 丰富、情境化、反直觉的研究   | 竞争优势类问题          |

如果你的文章没有原始数据、纯属概念性，应投 **AMR** 而非 AMJ。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford) —— 《经济研究》

---

## 许可证

MIT
