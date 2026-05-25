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

下一步 TODO：为下列 100 本英文 + 100 本中文主流经管期刊各做一个 journal-specific pack。希望优先支持某本，请提 issue 或 PR 补充。

数据来源：[RePEc / IDEAS 经济学聚合排名](https://ideas.repec.org/top/top.journals.all.html)、[FT50](https://guides.lib.purdue.edu/ft50) + [UTD24](https://jsom.utdallas.edu/the-utd-top-100-business-school-research-rankings/list-of-journals) + [ABS AJG 2024](https://charteredabs.org/academic-journal-guide/academic-journal-guide-2024)、[CSSCI 2023–2024 来源期刊目录](https://rwskc.zust.edu.cn/__local/C/2D/AB/B2AE8C5DC9C1A75618611EE3F00_2F8A1CF6_3DC4D.pdf) + [FMS 高质量期刊 2025 版](https://www.fms-journal.net/news/2720)。

### 英文 —— 经管主流 100 本

#### 经济学 Economics (50)

1. American Economic Review (AER)
2. Quarterly Journal of Economics (QJE)
3. Journal of Political Economy (JPE)
4. Econometrica
5. Review of Economic Studies (REStud)
6. AER: Insights
7. AEJ: Applied Economics
8. AEJ: Macroeconomics
9. AEJ: Microeconomics
10. AEJ: Economic Policy
11. Journal of Economic Literature (JEL)
12. Journal of Economic Perspectives (JEP)
13. Review of Economics and Statistics (REStat)
14. Journal of Econometrics
15. Journal of Monetary Economics
16. Journal of Economic Growth
17. Journal of Labor Economics
18. Journal of the European Economic Association (JEEA)
19. The Economic Journal (EJ)
20. RAND Journal of Economics
21. Journal of International Economics
22. Journal of Public Economics
23. Journal of Development Economics (JDE)
24. Journal of Economic Theory (JET)
25. Journal of Money, Credit and Banking (JMCB)
26. Review of Economic Dynamics (RED)
27. European Economic Review (EER)
28. Journal of Human Resources (JHR)
29. International Economic Review (IER)
30. Experimental Economics
31. Journal of Applied Econometrics
32. Journal of Business & Economic Statistics (JBES)
33. Journal of Health Economics
34. Journal of Environmental Economics and Management (JEEM)
35. Journal of Urban Economics
36. Games and Economic Behavior (GEB)
37. Journal of Law and Economics
38. Journal of Law, Economics, and Organization (JLEO)
39. World Development
40. World Bank Economic Review
41. IMF Economic Review
42. Annual Review of Economics
43. Brookings Papers on Economic Activity (BPEA)
44. Economic Policy
45. Journal of Risk and Uncertainty (JRU)
46. Quantitative Economics
47. The Econometrics Journal
48. Econometric Theory
49. Journal of Economic Behavior & Organization (JEBO)
50. Journal of Economic Geography

#### 金融 Finance (13)

1. Journal of Finance (JF)
2. Journal of Financial Economics (JFE)
3. Review of Financial Studies (RFS)
4. Review of Finance
5. Journal of Financial and Quantitative Analysis (JFQA)
6. Journal of Financial Intermediation (JFI)
7. Journal of Financial Markets (JFM)
8. Journal of Banking & Finance (JBF)
9. Journal of Corporate Finance (JCF)
10. Journal of International Money and Finance (JIMF)
11. Mathematical Finance
12. Journal of Empirical Finance (JEF)
13. Financial Management

#### 管理 / 战略 / 组织 Management (15)

1. Academy of Management Journal (AMJ)
2. Academy of Management Review (AMR)
3. Academy of Management Annals (AMA)
4. Administrative Science Quarterly (ASQ)
5. Strategic Management Journal (SMJ)
6. Organization Science (OrgSci)
7. Journal of Management (JOM-mgmt)
8. Journal of Management Studies (JMS)
9. Organization Studies (OS)
10. Human Relations
11. Human Resource Management (HRM)
12. Journal of International Business Studies (JIBS)
13. Research Policy
14. Journal of Business Venturing (JBV)
15. Entrepreneurship Theory and Practice (ETP)

#### 营销 Marketing (6)

1. Journal of Marketing (JM)
2. Journal of Marketing Research (JMR)
3. Marketing Science
4. Journal of Consumer Research (JCR)
5. Journal of Consumer Psychology (JCP)
6. Journal of the Academy of Marketing Science (JAMS)

#### 会计 Accounting (6)

1. The Accounting Review (TAR)
2. Journal of Accounting Research (JAR)
3. Journal of Accounting and Economics (JAE)
4. Review of Accounting Studies (RAST)
5. Contemporary Accounting Research (CAR)
6. Accounting, Organizations and Society (AOS)

#### 运营管理与信息系统 OM & IS (10)

1. Management Science
2. Operations Research (OR)
3. Manufacturing and Service Operations Management (M&SOM)
4. Journal of Operations Management (JOM-ops)
5. Production and Operations Management (POM)
6. MIS Quarterly (MISQ)
7. Information Systems Research (ISR)
8. Journal of Management Information Systems (JMIS)
9. Journal of the Association for Information Systems (JAIS)
10. INFORMS Journal on Computing (IJOC)

### 中文 —— 经管主流 100 本

#### 经济学 (50)

1. 《经济研究》
2. 《经济学（季刊）》
3. 《中国工业经济》
4. 《世界经济》
5. 《金融研究》
6. 《中国农村经济》
7. 《数量经济技术经济研究》
8. 《经济学动态》
9. 《财经研究》
10. 《财贸经济》
11. 《国际金融研究》
12. 《国际经济评论》
13. 《国际贸易问题》
14. 《经济科学》
15. 《南开经济研究》
16. 《经济理论与经济管理》
17. 《经济评论》
18. 《财经科学》
19. 《财政研究》
20. 《财经问题研究》
21. 《中国农村观察》
22. 《农业经济问题》
23. 《中央财经大学学报》
24. 《上海财经大学学报》
25. 《上海经济研究》
26. 《世界经济研究》
27. 《世界经济文汇》
28. 《当代财经》
29. 《当代经济科学》
30. 《政治经济学评论》
31. 《改革》
32. 《产业经济研究》
33. 《宏观经济研究》
34. 《金融经济学研究》
35. 《现代金融研究》（原《金融论坛》）
36. 《金融评论》
37. 《金融监管研究》
38. 《农业技术经济》
39. 《农村经济》
40. 《南方经济》
41. 《经济问题》
42. 《经济问题探索》
43. 《经济社会体制比较》
44. 《经济纵横》
45. 《经济学家》
46. 《经济与管理研究》
47. 《中国经济问题》
48. 《中南财经政法大学学报》
49. 《劳动经济研究》
50. 《国际经贸探索》

#### 管理学 / 战略 / 公共管理 (30)

1. 《管理世界》
2. 《管理科学学报》
3. 《南开管理评论》
4. 《中国管理科学》
5. 《管理评论》
6. 《管理学报》
7. 《系统工程理论与实践》
8. 《公共管理学报》
9. 《中国软科学》
10. 《科学学研究》
11. 《科研管理》
12. 《管理科学》
13. 《管理工程学报》
14. 《公共管理评论》
15. 《公共管理与政策评论》
16. 《工程管理科技前沿》
17. 《科学管理研究》
18. 《科学决策》
19. 《科学学与科学技术管理》
20. 《中国行政管理》
21. 《治理研究》
22. 《中国科技论坛》
23. 《中国科学院院刊》
24. 《软科学》
25. 《经济管理》
26. 《经济体制改革》
27. 《外国经济与管理》
28. 《科技进步与对策》
29. 《研究与发展管理》
30. 《管理学刊》

#### 会计 / 审计 / 其他经管交叉 (20)

1. 《会计研究》
2. 《会计评论》
3. 《审计研究》
4. 《审计与经济研究》
5. 《会计与经济研究》
6. 《社会保障评论》
7. 《华东经济管理》
8. 《宏观质量研究》
9. 《电子政务》
10. 《组织与管理》
11. 《税务研究》
12. 《现代日本经济》
13. 《亚太经济》
14. 《证券市场导报》
15. 《商业经济与管理》
16. 《现代经济探讨》
17. 《山西财经大学学报》
18. 《现代财经（天津财经大学学报）》
19. 《江西财经大学学报》
20. 《广东财经大学学报》

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

更宽口径的 agent skill 合集（与本索引互补）：

- [Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) — 精选 23,000+ agent skills，覆盖 8 大社科学科的实证研究（由 CoPaper.AI / Stanford REAP 维护）。
- [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 通用的 research → write → review → revise → finalize 科研流水线 skill 包。

通用的科研写作 skill 包（与本索引定位不同）：

- [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)
- [nature-skills](https://github.com/Yuan1z0825/nature-skills)

---

## License

MIT
