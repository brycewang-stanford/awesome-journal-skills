# Annals of Mathematics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Annals of Mathematics 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-Annals%20of%20Mathematics-c0392b)](https://annals.math.princeton.edu/)
[![Index](https://img.shields.io/badge/领域-纯数学-1f6feb)](https://annals.math.princeton.edu/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Annals of Mathematics**（《数学年刊》）投稿的"定理—证明"型论文 Agent Skill 工具栈。该刊由普林斯顿大学数学系与高等研究院（IAS）联合出版，是纯数学领域最负盛名的期刊之一。

本仓库刻意**不通用**——它不是泛化的"数学写作助手"，而是面向 Annals 编委与审稿口味的方法论沉淀。该刊的标准是：**重要性 + 原创性 + 完整、正确、可被严格核验的证明，且叙述清晰**。任何被掩盖的逻辑漏洞都是致命的，重要性门槛非常高。

> 本工具栈沉淀的是**长期稳定的规范与体例**，**不**断言易变的具体信息（现任编辑、费用、影响因子等）。投稿细节请务必以期刊官网为准：<https://annals.math.princeton.edu/>。

---

## 为什么要为 Annals of Mathematics 单独做一套 Skills？

Annals 的约束维度与实验科学期刊（PRL、JACS）以及一般的专业数学期刊**显著不同**：

| 维度        | Annals of Mathematics 的要求                  | 隐含含义                                  |
|-----------|------------------------------------------|---------------------------------------|
| 学科定位     | 整个纯数学领域；"定理—证明"型论文                  | 没有实验；通常很少或没有插图                 |
| 重要性门槛    | 具有长久意义的重大、深刻结果                       | "正确 + 新但增量"的结果不合适              |
| 严谨性      | 完整、正确、可被完全核验的证明                     | 任何一个逻辑漏洞都是致命的                   |
| "显然/易见"  | 是需要偿还的"债"，而非跳步的许可                    | 藏在缓和措辞后的漏洞会被抓出                 |
| 结果陈述     | 精确陈述主定理，置于靠前，并与既有工作定位             | 用一段话代替精确陈述会显得"未完成"           |
| 方法（证明策略） | 论证架构、关键引理、新颖技术所在                   | 没有路线图的整块证明很难被审阅               |
| 叙述（exposition） | 先陈述后证明；记号一致；分节清晰              | 须让相邻领域的专家也能读懂                   |
| 补充材料     | 没有科学期刊式的"补充材料"；要点留在正文              | 附录用于缓解篇幅，而非藏匿难点               |
| 篇幅        | 可以很长，但每一节都必须必要                       | 惩罚注水与冗余，但不惩罚深度                 |
| 审稿        | 专家逐步核验证明，常需一年以上                     | 须为缓慢、彻底、对抗式的阅读做准备            |
| 格式        | AMS-LaTeX；摘要 + MSC 分类；严谨引用文献           | 对所引定理的含糊转述是危险信号               |

通用的"科研写作"或"数学写作"Skill 包不会处理这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/annals-of-mathematics-skills
/plugin install annals-of-mathematics-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/annals-of-mathematics-skills.git
cd annals-of-mathematics-skills

mkdir -p ~/.claude/skills && cp -R skills/anmath-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/anmath-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 anmath-workflow 告诉我这份 Annals of Mathematics 目标稿子下一步该做什么。
```

---

## 默认工作流

```text
anmath-scope-fit
        ▼
anmath-results-framing
        ▼
anmath-methods
        ▼
anmath-figures
        ▼
anmath-supplementary
        ▼
anmath-writing-style       （polish）
        ▼
anmath-length-management   （polish）
        ▼
anmath-cover-letter
        ▼
anmath-submission
        ▼
anmath-referee-strategy
        ▼
anmath-revision
```

`anmath-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## Skill 一览

| Skill                      | 用途                                                       |
|----------------------------|----------------------------------------------------------|
| `anmath-workflow`          | 路由器：判断当前阶段，推荐下一个 skill                          |
| `anmath-scope-fit`         | 按 Annals 重要性门槛筛查结果的重要性与原创性                     |
| `anmath-results-framing`   | 精确陈述主定理 + 与既有工作定位                                |
| `anmath-methods`           | 证明策略：论证架构、关键引理、新颖技术、难点所在                   |
| `anmath-figures`           | 叙述与结构：分节、记号、先陈述后证明、交换图                       |
| `anmath-supplementary`     | 附录安放辅助结果 / 长计算；要点保留在正文                         |
| `anmath-writing-style`     | 严谨性与文风：消除漏洞、去掉"显然/易见"                          |
| `anmath-length-management` | 长可以，注水不行——每一节都必须必要                              |
| `anmath-cover-letter`      | 向编辑简洁说明重要性与契合度的投稿信                            |
| `anmath-submission`        | 投稿前 preflight（AMS-LaTeX、MSC、文献、arXiv）+ 模板          |
| `anmath-referee-strategy`  | 预判专家对证明的逐步核验；对论证做对抗式压力测试                   |
| `anmath-revision`          | 修补漏洞并撰写对审稿意见的逐条回复                              |

### 附属资源

- [`skills/anmath-submission/templates/manuscript_template.md`](skills/anmath-submission/templates/manuscript_template.md) —— AMS-LaTeX 稿件骨架（前置信息、定理环境、分节、参考文献）
- [`skills/anmath-submission/templates/checklist.md`](skills/anmath-submission/templates/checklist.md) —— 投稿前 8 类自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— TeX/AMS 宏包、MathSciNet / zbMATH / arXiv、证明助手（Lean / Coq / Isabelle）、绘图工具（`tikz-cd`）

---

## 与 PRL / JACS Skill 包的差异

| 维度        | Annals of Mathematics       | PRL / JACS（实验科学）           |
|-----------|-----------------------------|------------------------------|
| 核心对象     | 定理及其证明                   | 实验 / 计算结果                  |
| 插图        | 可选，常常没有                  | 核心；图承载主线                  |
| 方法部分     | 证明策略与架构                  | 材料、实验流程、仪器               |
| 补充材料     | 附录；要点在正文                | 大量补充信息                     |
| 致命缺陷     | 单个逻辑漏洞                   | 不可复现 / 夸大                  |
| 审稿周期     | 常需一年以上                   | 数周至数月                      |

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的证明
- 不替你判断结果是否**真的**原创或重要——这是研究者本人的判断
- 不收录该刊的录用率、费用、影响因子等元数据
- 不模拟某位具体编辑或审稿人的偏好

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) —— 《经济研究》投稿工具栈

---

## License

MIT
