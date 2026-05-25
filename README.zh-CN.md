# Awesome Journal Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

按**期刊**组织的社科 Agent Skill 包索引——涵盖选题、识别策略、引言写作、表格规范、复制包准备、修改回复。

每个 pack 都是**针对单一期刊**的方法论沉淀：它编码了某一本期刊的编委偏好、格式规范、识别标准和审稿文化。通用的"科研写作"Skill 包做不到这一点。

---

## 为什么要"按期刊"做 Skills？

不同顶刊对手稿的约束**显著不同**：

- **AER** 退稿点常在识别策略（TWFE、弱 IV、naive RDD）
- **《管理世界》** 退稿点常在缺中国制度背景
- **《经济研究》** 退稿点常在缺经典理论文献

一套"经济学写作"Skill 不可能同时编码这些差异。本索引下的每个 pack 都是按期刊定制的。

---

## Skill Pack 一览

| 期刊                                | 仓库                                                                                          | 学科                       | 状态    |
|-----------------------------------|---------------------------------------------------------------------------------------------|---------------------------|---------|
| **American Economic Review** + AER:Insights + AEJ 系列 | [AER-skills](https://github.com/brycewang-stanford/AER-skills)                              | 经济学（Top-5）             | v1.0    |
| **《管理世界》**                       | [management-world-skills](https://github.com/brycewang-stanford/management-world-skills)    | 管理学 + 应用经济           | v0.1    |
| **《经济研究》**                       | [economic-research-skills](https://github.com/brycewang-stanford/economic-research-skills)  | 经济学（中国 CSSCI 顶级）    | v0.1    |

---

## 仓库结构

本仓库以 **git submodule** 方式收录每个 pack，分别指向其上游独立仓库。每天通过 GitHub Actions（[`.github/workflows/sync-submodules.yml`](.github/workflows/sync-submodules.yml)）自动把 submodule 指针 bump 到上游 `main` 最新提交，无需手工同步。

```text
awesome-journal-skills/
├── AER-skills/                 → submodule: brycewang-stanford/AER-skills
├── economic-research-skills/   → submodule: brycewang-stanford/economic-research-skills
├── management-world-skills/    → submodule: brycewang-stanford/management-world-skills
└── .github/workflows/sync-submodules.yml
```

带 submodule 克隆：

```bash
git clone --recurse-submodules https://github.com/brycewang-stanford/awesome-journal-skills.git
# 若已克隆：
git submodule update --init --recursive
```

随时手动拉取最新 pack 内容：

```bash
git submodule update --remote --merge
```

---

## 如何使用

### 方式 A —— Claude Code 插件（推荐）

按需安装：

```bash
# AER
/plugin marketplace add https://github.com/brycewang-stanford/AER-skills
/plugin install aer-skills

# 管理世界
/plugin marketplace add https://github.com/brycewang-stanford/management-world-skills
/plugin install management-world-skills

# 经济研究
/plugin marketplace add https://github.com/brycewang-stanford/economic-research-skills
/plugin install economic-research-skills

/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/AER-skills.git
git clone https://github.com/brycewang-stanford/management-world-skills.git
git clone https://github.com/brycewang-stanford/economic-research-skills.git

mkdir -p ~/.claude/skills
cp -R AER-skills/skills/aer-* ~/.claude/skills/
cp -R management-world-skills/skills/mw-* ~/.claude/skills/
cp -R economic-research-skills/skills/er-* ~/.claude/skills/
```

### 第一条 Prompt

```
用 aer-workflow（或 mw-workflow / er-workflow）告诉我这份目标[期刊]的稿子下一步该做什么。
```

---

## Pack 选择速查

| 你的稿子是…                                  | 用这个 pack                  |
|------------------------------------------|---------------------------|
| 因果识别为主的实证文章，目标 top-5 经济学           | `AER-skills`              |
| 中国情境实证 + 政策可操作                          | `management-world-skills` |
| 中国情境 + 理论贡献突出                            | `economic-research-skills`|

---

## 路线图

下一步 TODO：为下列 20 + 20 本主流经管期刊各做一个 journal-specific pack。希望优先支持某本，请提 issue。

### 英文 —— 经管主流 20 本

1. Quarterly Journal of Economics (QJE) — *经济学*
2. Journal of Political Economy (JPE) — *经济学*
3. Econometrica — *经济学*
4. Review of Economic Studies (REStud) — *经济学*
5. Review of Economics and Statistics (REStat) — *经济学*
6. Journal of Economic Perspectives (JEP) — *经济学*
7. Journal of Econometrics — *经济学*
8. AEJ: Applied Economics — *经济学*
9. AEJ: Macroeconomics — *经济学*
10. Journal of Development Economics (JDE) — *经济学*
11. Journal of Finance (JF) — *金融*
12. Journal of Financial Economics (JFE) — *金融*
13. Review of Financial Studies (RFS) — *金融*
14. Academy of Management Journal (AMJ) — *管理*
15. Academy of Management Review (AMR) — *管理*
16. Administrative Science Quarterly (ASQ) — *管理*
17. Strategic Management Journal (SMJ) — *战略*
18. Management Science — *运营 / 通用管理*
19. Journal of Marketing (JM) — *营销*
20. The Accounting Review (TAR) — *会计*

### 中文 —— 经管主流 20 本

1. 《经济学（季刊）》 — *经济学*
2. 《世界经济》 — *经济学*
3. 《中国工业经济》 — *经济学*
4. 《金融研究》 — *金融*
5. 《中国农村经济》 — *经济学*
6. 《数量经济技术经济研究》 — *计量*
7. 《财经研究》 — *经济学*
8. 《财贸经济》 — *经济学*
9. 《经济学动态》 — *经济学*
10. 《国际金融研究》 — *金融*
11. 《经济科学》 — *经济学*
12. 《南开经济研究》 — *经济学*
13. 《管理科学学报》 — *管理*
14. 《南开管理评论》 — *管理*
15. 《中国管理科学》 — *管理*
16. 《管理评论》 — *管理*
17. 《管理学报》 — *管理*
18. 《系统工程理论与实践》 — *管理*
19. 《科研管理》 — *管理*
20. 《会计研究》 — *会计*

---

## 贡献

每个 pack 都在自己的仓库里。要为某个 pack 贡献内容，请到对应仓库提 PR。要提议新增 pack，请在本仓库提 issue。

收录到本索引的质量门槛：

1. 必须按期刊定制（不是通用 pack）
2. 中英文双语 README（针对中国相关期刊）
3. 至少有一个 `*-workflow` 路由 skill
4. 含 plugin manifest（`.claude-plugin/plugin.json` + `marketplace.json`）
5. MIT 协议

---

## 相关项目

通用的科研写作 skill 包（与本索引定位不同）：

- [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)
- [nature-skills](https://github.com/Yuan1z0825/nature-skills)

---

## License

MIT
