# 中国农村经济 Skills

<p align="center">
  <img src="assets/cover.svg" alt="《中国农村经济》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-中国农村经济-c0392b)](https://www.cssn.cn/)
[![Index](https://img.shields.io/badge/索引-CSSCI%20一区-1f6feb)](https://www.cssn.cn/)
[![Workflow](https://img.shields.io/badge/工作流-识别+机制+异质性-blue)](skills/cre-workflow)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《中国农村经济》** 投稿的 Agent Skill 工具栈。该刊由中国社会科学院农村发展研究所主办，是中国农业与农村经济领域的顶级期刊（CSSCI 一区），姊妹刊为《中国农村观察》。本工具栈覆盖**三农选题、文献综述、农户微观识别、机制分析、异质性、表格、乡村振兴政策含义、投稿规范、修改回复**等环节，配套 CFPS / CHFS / CLDS / 农村固定观察点等三农数据与 Stata / R / Python 模板。

本仓库刻意**不通用**——它是面向《中国农村经济》编委审稿口味的方法论沉淀，不是泛化的"中文经济学写作助手"。

---

## 为什么要为《中国农村经济》单独做一套 Skills？

《中国农村经济》的约束维度与综合性经济学期刊**显著不同**：

| 维度       | 《中国农村经济》要求             | 隐含含义                                          |
|----------|-----------------------|---------------------------------------------|
| 学科定位    | 农业与农村经济（三农）            | 脱离三农场景的"通用"实证不适合                       |
| 选题       | 理论贡献 + 中国农村政策现实，落到三农场景 | 第一段就要说明"为什么是农村问题、为什么现在做"      |
| 边际贡献    | 引言必须明确写出，3–5 条               | "本文有以下创新"段落必须精炼                        |
| 数据       | 微观农户 / 村级调查（CFPS、CHFS、CLDS、固定观察点） | 仅省级面板描述统计易被认为"工作论文"   |
| 识别策略    | 准实验 + 处理农户自选择内生性          | 纯描述统计 / OLS 易被退稿                        |
| 内生性     | 入社 / 务工 / 流转等自选择必须处理      | 忽视农村数据内生性是退稿信号                       |
| 机制       | 几乎必备，且落到农户微观层面            | 只有宏观叙事的实证文章命中率低                     |
| 异质性     | 强烈推荐，且贴合三农场景               | 只切"东中西"会被视为偷懒                          |
| 政策含义    | 意义层，但落到具体三农对象              | "加强完善推进"四件套套话会被挑刺                   |
| 字数       | 正文约 1.5–2.5 万字（含图表，以官网为准）   | 结构完整                                       |

通用的"科研写作"或"经济学写作"Skill 包不会处理这些约束。

> 准确性提示：确切字数、参考文献条数、图表数量、投稿网址、评审流程等会随年度调整。本工具栈描述的是持久规范，**具体数字请以《中国农村经济》官网"投稿须知"为准**。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/china-rural-economy-skills
/plugin install china-rural-economy-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/china-rural-economy-skills.git
cd china-rural-economy-skills

mkdir -p ~/.claude/skills && cp -R skills/cre-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/cre-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 cre-workflow 告诉我这份《中国农村经济》目标稿子下一步该做什么。
```

---

## 默认工作流

```text
cre-topic-selection
        ▼
cre-literature-review
        ▼
cre-identification
        ▼
cre-mechanism
        ▼
cre-heterogeneity
        ▼
cre-tables-figures
        ▼
cre-policy-implication
        ▼
cre-abstract      （polish）
        ▼
cre-style         （polish）
        ▼
cre-submission
        ▼
cre-rebuttal
```

`cre-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## Skill 一览

| Skill                     | 用途                                  |
|--------------------------|------------------------------------|
| `cre-workflow`            | 路由器：判断当前阶段，推荐下一个 skill     |
| `cre-topic-selection`     | 三农场景契合 + 理论贡献 + 边际贡献四句式  |
| `cre-literature-review`   | 中外并重 + 三农经典必引 + 对话式综述      |
| `cre-identification`      | 农户微观准实验设计（DID / IV / RDD / PSM）+ 自选择处理 |
| `cre-mechanism`           | 农户层面机制分析路径与写作模板            |
| `cre-heterogeneity`       | 贴合三农场景的异质性切分（超越"东中西"）  |
| `cre-tables-figures`      | 三线表、变量定义表、图形美学              |
| `cre-policy-implication`  | 政策含义（意义层但落到具体三农对象）       |
| `cre-abstract`            | 摘要五句法 + 黑名单短语清除               |
| `cre-style`               | 全文语言 polish：空话套话 / 四件套 → 具体 |
| `cre-submission`          | 投稿 checklist + 稿件模板（格式、双盲、查重）|
| `cre-rebuttal`            | 修改回复信结构（致谢 → 逐条 → 修订对照） |

### 附属资源

- [`skills/cre-submission/templates/manuscript_template.md`](skills/cre-submission/templates/manuscript_template.md) —— 稿件结构骨架（中英摘要、变量定义表、参考文献格式）
- [`skills/cre-submission/templates/checklist.md`](skills/cre-submission/templates/checklist.md) —— 投稿前 8 类自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 三农数据资源（CFPS / CHFS / CLDS / 农村固定观察点 / 农业农村部统计等）+ Stata / R / Python 包速查

---

## 与姊妹刊《中国农村观察》的差异

| 维度        | 《中国农村经济》          | 《中国农村观察》          |
|----------|-----------------------|----------------------|
| 侧重        | 因果识别实证             | 对质性 / 案例更包容        |
| 方法门槛    | 高（DID / IV / RDD / PSM-DID） | 较包容             |
| 政策观察    | 较少                    | 接受                  |
| 共同点      | 均要求三农场景，均由社科院农发所主办 | 同上            |

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的稿件
- 不模拟审稿人偏好
- 不收录《中国农村经济》历年拒稿率、影响因子等元数据
- 不评估你的"理论贡献"是否真有原创性——这是研究者本人的判断

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) —— 《经济研究》投稿工具栈

---

## License

MIT
