# PNAS Skills

<p align="center">
  <img src="assets/cover.png" alt="PNAS 封面卡" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-PNAS-005a9c)](https://www.pnas.org/)
[![Scope](https://img.shields.io/badge/定位-综合性顶刊-1f6feb)](https://www.pnas.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **PNAS（美国国家科学院院刊，Proceedings of the National Academy of Sciences）** 投稿的 Agent Skill 工具栈——美国国家科学院（NAS）旗下覆盖面广的综合性刊物。

本仓库刻意**不通用**。它不是泛化的"科研写作助手"，而是把 PNAS 的编辑底线——**高质量 + 广泛意义，且比 Science/Nature 更易接受**——以及由此衍生的具体规范沉淀成方法论：独特的**投稿通道**（Direct 直投 vs 由 NAS 院士 Contributed 转交）、强制的 **≤120 词 Significance Statement（意义陈述）**、**生物/物理/社会科学三大类的 Classification 分类体系**、**约 250 词的自洽摘要**、**正文内保留 Materials and Methods**、PNAS 的**按出现顺序编号引用**、统计与可复现报告、以及强制的数据/代码可得性。

---

## 为什么要为 PNAS 单独做一套 Skills？

PNAS 的约束维度与领域刊、乃至 Science/Nature 都**显著不同**：

| 维度        | PNAS 要求                                                   | 隐含含义                                       |
|-----------|-----------------------------------------------------------|--------------------------------------------|
| 编辑底线     | 高质量 + 广泛意义；**比 Science/Nature 更易接受**              | 看重扎实而重要的科学，而非只追最炫的结果            |
| 投稿通道     | **Direct 直投**（编辑指派）vs **Contributed**（NAS 院士、约每年 2 篇、自行组织 ≥2 名审稿人） | 通道决定处理与审稿——要尽早确定           |
| 意义陈述     | 必备，**≤120 词**，写给非本领域读者                            | 缺失/薄弱、或只是摘要翻版会在初筛吃亏              |
| 摘要        | **约 250 词**，单段、自洽、需量化                              | **不要**套用 Science 的 ≤125 词摘要或一句话总结    |
| 分类        | 一个大类（**生物 / 物理 / 社会科学**）+ 小类 + 关键词            | 投稿时必填                                    |
| 方法位置     | **Materials and Methods 保留在正文**                         | 与 Science Report / Cell 不同，别把方法抽走        |
| 参考文献     | 编号制、按出现顺序、全作者列出                                  | 著者-年份体例必须转换                            |
| 数据与代码   | 数据可得性声明 + 存档并给登录号/DOI；"按需提供"不被接受           | 没有登录号 = 没准备好投稿                         |

通用的"科研写作"Skill 包不会编码这些"按刊定制"的约束。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install pnas-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/PNAS-Skills

mkdir -p ~/.claude/skills && cp -R skills/pnas-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/pnas-* ~/.codex/skills/
```

### 第一条提示词

```
用 pnas-workflow 告诉我，针对 PNAS 的稿子，下一步该用哪个 skill。
```

---

## 默认工作流

```text
pnas-fit            （先过"广泛意义"这一关；确认 PNAS 是合适投向）
        ▼
pnas-track          （Direct 直投 vs Contributed 转交——尽早定）
        ▼
pnas-writing        （结构、分类 + 关键词、方法留在正文）
        ▼
pnas-figures        （图件控制在预算内）
        ▼
pnas-statistics     （严谨性 + 可复现）
        ▼
pnas-data           （数据/代码可得性 + 存档）
        ▼
pnas-significance   （≤120 词意义陈述——高价值）
        ▼
pnas-abstract       （约 250 词自洽摘要——润色）
        ▼
pnas-citation       （PNAS 编号体例——润色）
        ▼
pnas-submission     （投稿前自检 + 投稿信）
        ▼
pnas-rebuttal       （送审之后）
```

`pnas-workflow` 是路由器——根据你所处阶段告诉你下一个该用哪个 skill。

---

## Skills 一览

| Skill               | 作用                                                          |
|---------------------|-------------------------------------------------------------|
| `pnas-workflow`     | 路由器——决定下一步调用哪个子 skill                              |
| `pnas-fit`          | 广泛意义判定；PNAS vs Science/Nature vs 领域刊选刊路由            |
| `pnas-track`        | **Direct 直投 vs Contributed（NAS 院士）** 投稿通道——PNAS 独有    |
| `pnas-significance` | 强制 **≤120 词 Significance Statement（写给广义读者）**           |
| `pnas-abstract`     | **约 250 词** 自洽摘要；与意义陈述区分                            |
| `pnas-writing`      | 结构、篇幅、**分类 + 关键词**、**方法留在正文**                    |
| `pnas-figures`      | 栏宽尺寸（9/11.4/18 cm）、字号、展示原始数据、色盲友好             |
| `pnas-statistics`   | 效应量 + 置信区间 + n + 检验；重复性；随机化；可复现                |
| `pnas-data`         | 数据可得性声明、仓库存档、登录号/DOI、代码                         |
| `pnas-citation`     | PNAS 编号体例、按出现顺序、全作者列出                             |
| `pnas-submission`   | 完整投稿前自检清单 + 投稿信模板                                  |
| `pnas-rebuttal`     | 决议分诊、实验优先级、逐条回复                                    |

### 资源

- [`skills/pnas-submission/templates/checklist.md`](skills/pnas-submission/templates/checklist.md) — 完整投稿前自检清单
- [`skills/pnas-submission/templates/cover_letter_template.md`](skills/pnas-submission/templates/cover_letter_template.md) — PNAS 投稿信脚手架（意义 + 通道 + 直投时推荐编辑/审稿人）
- [`resources/external_tools.md`](resources/external_tools.md) — 数据存档仓库、报告标准、图表/统计工具、PNAS 作者页面

---

## 与 Science / Nature 的差异

| 维度      | PNAS                                   | Science                | Nature              |
|---------|----------------------------------------|------------------------|---------------------|
| 门槛      | 高质量 + 广泛意义；**更易接受**            | 顶尖广泛意义              | 顶尖广泛意义           |
| 投稿通道   | **Direct vs Contributed（NAS 院士）**     | 单一通道                 | 单一通道              |
| 通俗件     | **Significance Statement ≤120 词**      | 一句话总结               | 总结段落              |
| 摘要      | **约 250 词**，自洽                       | ≤ ~125 词              | 总结段落约定           |
| 方法      | **正文内**（Materials and Methods）       | 补充材料（Report）        | Methods 段落约定       |
| 参考文献   | 编号、按出现顺序、全作者                    | 编号、按出现顺序           | 另一种编号体例          |

Science 见姊妹包 [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills)。Nature 见 [nature-skills](https://github.com/Yuan1z0825/nature-skills)。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 按刊定制 skill 包索引
- [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) · [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills) · [NEJM-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/NEJM-Skills) · [Lancet-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Lancet-Skills)

---

## 免责声明

本包为独立、社区构建的 skill 包，**与美国国家科学院（NAS）/ PNAS 无任何隶属、背书或合作关系**。所有指标（字数、图件上限、通道配额、体例规则）均依据写作时公开的作者指南——**投稿前请务必以最新的 [PNAS 作者须知](https://www.pnas.org/author-center/submitting-your-manuscript) 为准**。

---

## 许可证

MIT
