# Administrative Science Quarterly (ASQ) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Administrative Science Quarterly (ASQ) 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-ASQ-7a2230)](https://journals.sagepub.com/home/asq)
[![Index](https://img.shields.io/badge/索引-SSCI%20%2F%20FT50-1f6feb)](https://journals.sagepub.com/home/asq)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Administrative Science Quarterly（ASQ，《行政科学季刊》）** 投稿的 Agent Skill 工具栈。ASQ 由 SAGE 出版、与康奈尔大学 Samuel Curtis Johnson 管理研究生院合作，是组织理论与组织社会学领域顶级的、以理论驱动的期刊。

本仓库刻意**不通用**——它不是泛化的"管理学写作助手"，而是围绕 ASQ 的标志性要求打造：对组织现象提出深刻、且常常**反直觉**的理论洞见，并以极高的写作工艺呈现。ASQ **同时**接受严谨的定量研究**和**扎实的定性／归纳研究（扎根理论、民族志、历史研究），本工具栈把两者都作为一等公民处理——因为在 ASQ，**方法服从理论问题**。

---

## 为什么要为 ASQ 单独做一套 Skills？

ASQ 的约束维度与 AMJ / SMJ / Organization Science **显著不同**：

| 维度        | ASQ 的要求                              | 隐含含义                                      |
|-----------|--------------------------------------|-------------------------------------------|
| 学科定位     | 组织理论 & 组织社会学                      | 纯微观认知或纯金融问题不适配                       |
| 看重什么     | 对组织现象的**反直觉**理论洞见               | 扎实但不令人意外的发现会被问"那又如何？"             |
| 贡献性质     | 必须是**理论**贡献，而非方法贡献             | 再精巧的方法也救不了单薄的想法                     |
| 方法立场     | 定性与定量**同为一等公民**                  | 方法要服从问题，不能反过来                        |
| 定性研究门槛 | 透明编码、理论抽样、数据—理论对照表           | "轶事式"引语、缺乏严谨性会被拒                     |
| 定量研究门槛 | 严谨设计、识别策略、稳健性                  | 横截面同源数据强行做因果推断会被惩罚                |
| 理论形态     | 过程理论常见；形态需与现象匹配               | 对过程问题套用"方差话语"是错配                     |
| 工艺与叙事   | 长文体；强叙事；上乘文笔                     | "实验报告体"写作表现不佳                         |
| 评审流程     | 发展性、多轮                             | 评审深入，通常 2 轮以上修订                       |
| 范围补充     | 也发表书评（book reviews）                 | 提交时选对稿件类型                              |

通用的"科研写作"或"管理学写作"Skill 包不会处理这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/asq-skills
/plugin install asq-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/asq-skills.git
cd asq-skills

mkdir -p ~/.claude/skills && cp -R skills/asq-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/asq-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 asq-workflow 告诉我这份 ASQ 目标稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
asq-topic-selection
        ▼
asq-theory-development
        ▼
asq-literature-positioning
        ▼
asq-methods
        ▼
asq-data-analysis
        ▼
asq-contribution-framing
        ▼
asq-tables-figures
        ▼
asq-writing-style      （polish）
        ▼
asq-submission
        ▼
asq-review-process
        ▼
asq-rebuttal
```

`asq-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## Skill 一览

| Skill                       | 用途                                                      |
|-----------------------------|---------------------------------------------------------|
| `asq-workflow`              | 路由器：判断当前阶段，推荐下一个 skill                         |
| `asq-topic-selection`       | "谜题/惊喜"适配检验 + 贡献声明模板                            |
| `asq-theory-development`    | 过程理论 vs 方差理论；生成性机制；边界条件                      |
| `asq-literature-positioning`| 加入特定的组织理论对话，而非泛泛综述一个领域                     |
| `asq-methods`               | 设计选择 + 定性**与**定量研究的严谨性门槛                      |
| `asq-data-analysis`         | 数据—理论链路（编码/证据表）或估计 + 稳健性                     |
| `asq-contribution-framing`  | 锤炼理论"那又如何"；明确贡献类型                              |
| `asq-tables-figures`        | 数据结构图、数据—理论对照表、过程模型、回归表                   |
| `asq-writing-style`         | 叙事弧线、过程话语、达到 ASQ 文笔工艺标准                      |
| `asq-submission`            | 投稿前 preflight + 稿件模板（适配、匿名、格式）                |
| `asq-review-process`        | 导航 ASQ 发展性、多轮评审流程                                |
| `asq-rebuttal`              | R&R 回复信结构（聚焦"深化贡献"）                              |

### 附属资源

- [`skills/asq-submission/templates/manuscript_template.md`](skills/asq-submission/templates/manuscript_template.md) —— 定性与定量两套稿件结构骨架
- [`skills/asq-submission/templates/checklist.md`](skills/asq-submission/templates/checklist.md) —— 投稿前 8 类自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 定性 CAQDAS + 定量软件、网络/历史研究工具、文献管理、ScholarOne 说明

---

## 与其他管理学期刊的差异

| 维度       | ASQ                       | AMJ                   | AMR        | SMJ                |
|----------|---------------------------|-----------------------|------------|--------------------|
| 核心交付   | 反直觉理论 + 工艺            | 实证贡献                | 纯理论       | 战略贡献             |
| 数据      | 定性**与**定量              | 以定量为主              | 无          | 以定量为主           |
| 理论形态   | 过程理论常见                | 方差/假设检验            | 概念性       | 方差/绩效            |
| 写作      | 长文体叙事；重工艺            | 结构化实证              | 论证驱动      | 结构化实证           |
| 评审      | 发展性、多轮                | 发展性                  | 发展性       | 发展性               |

如果稿件是没有数据的纯概念论文，AMR 风格的工具栈更合适；如果是没有理论惊喜的假设检验，请重新考虑 ASQ 是否是合适的归宿。

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的稿件
- 不模拟具体审稿人的偏好
- 不收录 ASQ 的录用率、影响因子或当前编委名单——这些易变信息请在期刊官网核实
- 不评判你的理论贡献是否真有原创性——这是研究者本人的判断

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [amj-skills](https://github.com/brycewang-stanford/amj-skills) —— Academy of Management Journal
- [smj-skills](https://github.com/brycewang-stanford/smj-skills) —— Strategic Management Journal

---

## License

MIT
