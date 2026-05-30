# 《财经研究》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《财经研究》 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Finance%20and%20Economics-c0392b)](https://cjyj.sufe.edu.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://cjyj.sufe.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《财经研究》(Journal of Finance and Economics)** 投稿的 Agent 技能栈——由 **上海财经大学** 主办的 CSSCI 来源、综合性财经类高水平学术期刊。

本仓库是有立场的。它**不是**一个通用的中文经济学写作工具箱，而是一个**专门针对《财经研究》**的技能栈，覆盖：有理论贡献的选题、中英文献综述、现代准实验识别、机制 / 异质性分析、CSSCI 行文规范、政策含义、投稿前检查，以及双向匿名外审后的 R&R 回复。

> 准确性提示：字数限制、版面费、编委会构成、影响因子等会随时间变化。本技能栈编码的是期刊的**持久规范**；投稿前务必到官网"投稿须知"核对当前的具体数字。

---

## 为什么需要一套独立的《财经研究》技能栈？

《财经研究》的约束与 AER / AEJ / 顶级金融期刊有实质区别，甚至与纯经济学 CSSCI 期刊也不同：

| 约束维度   | 《财经研究》                                              | 含义                                       |
|-----------|----------------------------------------------------------|--------------------------------------------|
| 学科      | 综合性财经（财政、产业、金融与公司财务、贸易、劳动、区域、数字经济） | 纯管理或纯案例文章定位不符               |
| 选题      | 有理论贡献且**回应中国现实问题**                          | "只做政策评估"读起来像工作论文            |
| 边际贡献  | 引言中 3–5 条明确的"边际贡献"                             | 不能只写一段话                            |
| 文献综述  | 中外并重；**必引经典理论文献**                            | 缺经典理论文献是退稿信号                  |
| 识别策略  | 准实验 + 严密内生性讨论                                   | 仅 OLS + 控制变量常被退稿                 |
| 机制      | 接近必备                                                 | 无机制的实证文章很难被接收                |
| 异质性    | 强烈偏好                                                 | 缺失时常在 R&R 中被要求补做               |
| 政策含义  | 必备；偏"意义层"而非"操作层"                              | 区别于《管理世界》的可操作政策风格        |
| 数据      | 明确点名权威微观数据（国泰安 / Wind / CNRDS / 工企 / 海关 / CFPS） | 写"公开渠道"是危险信号 |
| 摘要      | 规范的中文摘要 + 对齐的英文摘要                          | 先"做了什么 + 发现什么"，再谈意义         |

通用的"科研写作"或"经济学写作"技能包无法处理这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/journal-of-finance-and-economics-skills
/plugin install journal-of-finance-and-economics-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/journal-of-finance-and-economics-skills.git
cd journal-of-finance-and-economics-skills

mkdir -p ~/.claude/skills && cp -R skills/cfe-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/cfe-* ~/.codex/skills/
```

### 第一句提示词

```
用 cfe-workflow 告诉我，我的《财经研究》稿件下一步该用哪个 skill。
```

---

## 默认工作流

```text
cfe-topic-selection
        ▼
cfe-literature-review
        ▼
cfe-identification
        ▼
cfe-mechanism
        ▼
cfe-heterogeneity
        ▼
cfe-tables-figures
        ▼
cfe-policy-implication
        ▼
cfe-abstract        (后段 polish)
        ▼
cfe-style           (后段 polish)
        ▼
cfe-submission
        ▼
cfe-rebuttal
```

`cfe-workflow` 是路由器——它根据你所处的阶段告诉你下一步该用哪个 skill。

---

## Skills 一览

| Skill                      | 用途                                                          |
|---------------------------|---------------------------------------------------------------|
| `cfe-workflow`             | 路由器——决定下一步调用哪个子 skill                            |
| `cfe-topic-selection`      | 理论贡献契合 + 中国现实 + 边际贡献句式                         |
| `cfe-literature-review`    | 中英文献三层结构 + 经典理论自检                                |
| `cfe-identification`       | 准实验识别设计（DID / IV / RDD / DML / PSM）                  |
| `cfe-mechanism`            | 机制分析路径与写作模板                                         |
| `cfe-heterogeneity`        | 异质性切分：五维度优先级                                       |
| `cfe-tables-figures`       | 三线表、变量定义表、图形美学                                   |
| `cfe-policy-implication`   | 意义层政策含义（而非操作层）                                   |
| `cfe-abstract`             | 中文摘要五句法 + 黑名单短语清除                                |
| `cfe-style`                | 语言润色：空洞意义 → 具体贡献                                  |
| `cfe-submission`           | 投稿前检查清单 + 稿件模板（格式、字数、双盲）                  |
| `cfe-rebuttal`             | 双向匿名 R&R 回复信结构                                        |

### 资源

- [`skills/cfe-submission/templates/manuscript_template.md`](skills/cfe-submission/templates/manuscript_template.md) —— 标准稿件结构骨架（中英摘要、变量定义表、参考文献）
- [`skills/cfe-submission/templates/checklist.md`](skills/cfe-submission/templates/checklist.md) —— 投稿前 8 类自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 中文财经实证数据资源（国泰安 / Wind / CNRDS / 工企 / 海关 / CFPS）与 Stata / Python / R 软件包速查

---

## 与《经济研究》Skills 的差异

| 维度       | 《财经研究》                                  | 《经济研究》                        |
|-----------|----------------------------------------------|-------------------------------------|
| 学科      | 综合性财经                                    | 经济学（宏观 / 制度）               |
| 选题偏好  | 实证、中国现实驱动且有理论贡献                | 理论贡献优先                        |
| 方法重心  | 因果识别 + 微观数据                          | 识别 + 结构估计 / 理论              |
| 政策措辞  | 意义层（制度 / 定性）                        | 意义层（宏观 / 定性）               |
| 主办单位  | 上海财经大学                                 | 中国社会科学院经济研究所            |

---

## 相关项目

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) —— 《经济研究》
- [management-world-skills](https://github.com/brycewang-stanford/management-world-skills) —— 《管理世界》

---

## 许可证

MIT
