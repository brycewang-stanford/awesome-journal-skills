# Cell Skills

<p align="center">
  <img src="assets/cover.png" alt="Cell (Cell Press) 封面卡" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-Cell%20(Cell%20Press)-006699)](https://www.cell.com/cell/home)
[![Scope](https://img.shields.io/badge/定位-分子与细胞生物学-1f6feb)](https://www.cell.com/cell/home)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Cell（Cell Press）** 投稿的 Agent Skill 工具栈——分子与细胞生物学旗舰刊。

本仓库刻意**不通用**。它不是泛化的"科研写作助手"，而是把 Cell 的编辑底线——**一个完整、有机制、由假设驱动的故事**，且需多条独立证据汇聚到同一机制——以及由此衍生的具体规范沉淀成一套方法论：单一叙事主线的 Article、标志性的 **Highlights / eTOC 短文 / 图文摘要（Graphical Abstract）** 三件套、≤150 词的非结构化 **Summary**、含**关键资源表（Key Resources Table）** 与 **Resource Availability** 的 **STAR Methods**、数据/代码存档（**Mendeley Data** 为 Elsevier 默认仓库）、Cell Press **著者-年份**引用体例、以及"以概念性进展开场"的投稿信。

---

## 为什么要为 Cell 单独做一套 Skills？

Cell 的约束维度与领域刊、乃至 Nature/Science 都**显著不同**：

| 维度        | Cell 要求                                                  | 隐含含义                                       |
|-----------|---------------------------------------------------------|--------------------------------------------|
| 编辑底线     | **完整、有机制的故事** + 多条证据汇聚                          | 单一观察/描述性稿件**多数不送审、直接拒稿**          |
| 文章结构     | Summary · 引言 · Results · Discussion · **STAR Methods**  | 自由文本的 Methods 段不合体例                     |
| 标志件      | **Highlights**、**eTOC 短文**、**图文摘要**                | 缺失或薄弱会在各编辑环节吃亏                       |
| Highlights | 3–4 条，每条 **≤ 85 字符**                                 | 写成整句或超长即不合规                            |
| Summary（摘要） | 单段、**≤ ~150 词**、点明机制、需量化                    | 长的/结构化摘要不合体例                          |
| 方法        | **STAR Methods** + 关键资源表 + Resource Availability     | 试剂须给出来源 + RRID/货号                       |
| 数据与代码   | 须存档并给登录号/DOI；**Mendeley Data** 默认；三段式声明        | 主数据"按需提供"不被接受                          |
| 参考文献     | **著者-年份**、**按字母排序**、全作者列出                     | 按出现顺序的编号制（Science）必须转换               |
| 过度声称     | 拒稿首要原因之一；审稿人要求故事"完整闭环"                      | 结论不得超出证据                                |

通用的"科研写作"Skill 包不会编码这些"按刊定制"的约束。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install cell-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Cell-Skills

mkdir -p ~/.claude/skills && cp -R skills/cell-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/cell-* ~/.codex/skills/
```

### 第一条提示词

```
用 cell-workflow 告诉我，针对 Cell 的稿子，下一步该用哪个 skill。
```

---

## 默认工作流

```text
cell-fit            （先过"完整机制故事"这一关）
        ▼
cell-framing        （锁定单一叙事主线：假设 → 机制 → 意义）
        ▼
cell-writing        （Article 结构；守住篇幅；用 STAR Methods 而非自由文本）
        ▼
cell-figures        （图件控制在预算内）
        ▼
cell-star-methods   （关键资源表 + Resource Availability + QSA）
        ▼
cell-data           （数据/代码存档 + 三段式可得性声明）
        ▼
cell-summary        （≤150 词 Summary——润色）
        ▼
cell-highlights     （Highlights + eTOC 短文 + 图文摘要——润色）
        ▼
cell-citation       （Cell Press 著者-年份体例——润色）
        ▼
cell-submission     （投稿信 + 投稿前自检）
        ▼
cell-rebuttal       （送审之后）
```

`cell-workflow` 是路由器——根据你所处阶段告诉你下一个该用哪个 skill。

---

## Skills 一览

| Skill                | 作用                                                          |
|----------------------|-------------------------------------------------------------|
| `cell-workflow`      | 路由器——决定下一步调用哪个子 skill                              |
| `cell-fit`           | 初筛过滤：完整机制故事判定；Cell Press 选刊路由                    |
| `cell-framing`       | 锁定单一叙事主线、陈述式标题                                     |
| `cell-highlights`    | Highlights（≤85 字符）、eTOC 短文（~50 词）、图文摘要              |
| `cell-summary`       | ≤150 词非结构化 Summary，点明机制、量化                          |
| `cell-writing`       | Article 结构；篇幅预算（~45,000 字符）；STAR Methods 位置          |
| `cell-figures`       | 栏宽尺寸（85/114/174 mm）、≥6–7pt 字号、展示原始数据、图像规范      |
| `cell-star-methods`  | 关键资源表 + Resource Availability（三小节）+ QSA                 |
| `cell-data`          | 存档（GEO/PDB/PRIDE/Mendeley Data）、登录号、三段式声明            |
| `cell-citation`      | Cell Press 著者-年份体例、按字母排序、全作者列出                    |
| `cell-submission`    | 完整投稿前自检清单 + 投稿信模板                                  |
| `cell-rebuttal`      | 决议分诊、实验优先级、逐条回复                                    |

### 资源

- [`skills/cell-submission/templates/checklist.md`](skills/cell-submission/templates/checklist.md) — 完整投稿前自检清单
- [`skills/cell-submission/templates/cover_letter_template.md`](skills/cell-submission/templates/cover_letter_template.md) — 以概念性进展开场的投稿信脚手架
- [`resources/external_tools.md`](resources/external_tools.md) — 数据存档仓库、STAR Methods/RRID 标准、图表/统计工具、Cell Press 作者页面

---

## 与 Nature / Science / Cell Press 姊妹刊的差异

| 维度      | Cell                          | Nature / Science                  | Molecular Cell / Cell Reports / CRM |
|---------|-------------------------------|-----------------------------------|-------------------------------------|
| 门槛      | 完整机制故事                    | 顶尖广泛意义                        | Cell Reports：较宽                    |
| 标志件     | Highlights + eTOC + 图文摘要    | 一句话总结（Science）/ 总结段（Nature） | 同为 Cell Press 三件套                |
| 摘要      | **Summary**，≤150 词、非结构化   | Science ≤125 词 + 一句话总结        | 类似的 Cell Press Summary            |
| 方法      | **STAR Methods** + 关键资源表    | Methods 段 / 补充材料               | 同样使用 STAR Methods                 |
| 参考文献   | **著者-年份、按字母排序**         | Science：**按出现顺序编号**          | Cell Press 著者-年份                  |
| 何时切换    | —                             | 想要最广读者时                       | Molecular Cell（分子机制）/ Cell Reports（不够广）/ CRM（转化） |

> 注意：Cell 用**著者-年份**引用——与 *Science* 的按出现顺序编号**正好相反**。Science 见姊妹包 [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills)；Nature 见 [nature-skills](https://github.com/Yuan1z0825/nature-skills)。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊定制 skill 包索引
- [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) · [PNAS-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/PNAS-Skills) · [NEJM-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/NEJM-Skills) · [Lancet-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Lancet-Skills)

---

## 免责声明

本包为独立、社区构建的 skill 包，**与 Cell Press / Elsevier / Cell 无任何隶属、背书或合作关系**。所有指标（字数、字符上限、图件上限、体例规则）均依据写作时公开的作者指南——**投稿前请务必以最新的 [Cell 作者指南](https://www.cell.com/cell/authors) 与 [STAR Methods 指南](https://www.cell.com/star-methods) 为准**。

---

## 许可证

MIT
