---
name: jqte-submission
description: Use for the pre-submission preflight to 《数量经济技术经济研究》 (JQTE) — checking footnote conventions (脚式编排, renumbered per page), title/keyword/abstract format, the ≥1000-character policy section, reproducibility of the method section, the online submission system (jqte.net), and anonymity. Use right before submitting; verify every numeric rule against the journal's current 投稿须知.
---

# 投稿前 preflight（jqte-submission）

## 触发时机

- 方法、结果、含义都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿系统 / 官网：**https://www.jqte.net/**（编辑部官方网站，远程投稿系统，作者登录 author/login.aspx）
- 注释体例：**文中所需注释以脚式编排，每页重新编号**（页下注/脚注，逐页起编）
- **政策建议不少于 1000 字（纯方法类论文除外）**
- 中文题目一般 ≤ 20 字（可加副标题）；英文题目 ≤ 10 个实词，不加副标题
- 题名下列作者、单位、摘要、关键词、中图分类号，并附英文摘要
- 请在投稿系统内上传全本稿件
- 主办：中国社会科学院数量经济与技术经济研究所；月刊

> 字数、关键词数量、查重阈值等部分数值来自第三方转载、官网未直接列明（见 profile「待核实」）。**以官网最新《投稿须知》与投稿系统提示为准，不要凭记忆。**

## 体例 checklist

- [ ] 注释统一为**脚式编排、每页重新编号**（页下注，逐页起编）
- [ ] 中文题目 ≤ 20 字；英文题目 ≤ 10 实词、无副标题、与中文一致
- [ ] 题名下信息齐全：作者、单位、摘要、关键词、中图分类号、英文摘要
- [ ] 摘要为完整短文，独立自含、不分段、不用图表公式
- [ ] 关键词数量、摘要字数按系统/官网最新要求核对（待核实数值勿凭记忆）
- [ ] 政策建议 ≥ 1000 字（纯方法类除外）
- [ ] 图表有数据来源与方法注、编号连续
- [ ] 已在投稿系统上传全本稿件

## 可复现性 hygiene（本刊尤重）

- [ ] 方法/指标/参数构造透明，他人能复现
- [ ] 数据来源、口径、年份、平减/校准交代齐全
- [ ] CGE/IO 的弹性来源、闭合规则、情景设定可重建

## 匿名评审 hygiene

- [ ] 正文/脚注/致谢/基金信息中去除可识别作者身份
- [ ] 自引改第三人称或匿名占位
- [ ] 文件属性（作者名）已清除

## 提交前内容复核（调用其它 skill）

- [ ] 贡献类型清楚、未硬凑因果（`jqte-fit-positioning`）
- [ ] 测度/模型/分解透明可复现（`jqte-measurement` / `jqte-io-cge`）
- [ ] 预测做了样本外评估（`jqte-forecasting`）
- [ ] 做了方法/参数敏感性（`jqte-sensitivity`）
- [ ] 表格有量化解读（`jqte-tables-figures`）

## 反模式

- 凭记忆套体例与字数，不查最新《投稿须知》
- 用尾注/文中夹注替代脚式编排逐页注
- 政策建议不足 1000 字（非纯方法类）
- 方法节黑箱、无法复现就投

## 输出格式

```
【体例】脚注逐页□ 题目字数□ 题名下信息□ 图表注□
【字数】政策建议 X 字（≥1000 □ / 纯方法豁免 □）；摘要/关键词按系统核对
【可复现】方法透明□ 数据口径□ CGE/IO 可重建□
【匿名】已清理 / 待清理 <点>
【系统】jqte.net 投稿入口已确认
【结论】可投 / 待修 <清单>
```
