---
name: jfr-submission
description: Use for the pre-submission preflight to 《金融研究》 (Journal of Financial Research) — checking word count (~20k chars), ~200-char abstract, 3–5 keywords, three JEL codes, note conventions (①②③ with continuous numbering), the online submission system (jryj.org.cn), double-blind anonymity, and document hygiene. Verify every rule against the journal's current 来稿须知.
---

# 投稿前 preflight（jfr-submission）

## 触发时机

- 正文、识别、机制、文风都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿系统：**http://www.jryj.org.cn/** 在线办公系统"作者在线投稿"（HTTPS 证书可能告警，以官方入口为准）
- 篇幅：**论文以 2 万字左右为宜**（含图表、注释）
- 摘要 **二百字左右**；中文关键词 **3–5 个**；须给 **3 个 JEL 分类号**
- 注释：能随文括号说明的尽量随文；不随文者用 **①②③……** 标号、文后依次列出；标题/表/图/等式/脚注**分别连续编号**
- 标题编号：一级"一、二、三"，二级"（一）（二）（三）"，三级"1. 2. 3."，四级"(1)(2)(3)"
- 主管：中国人民银行；主办：中国金融学会；月刊

> 体例与字数以官网**最新《来稿须知》**为准。规则会变，投前务必复核，不要凭记忆。

## 体例 checklist

- [ ] 全文约 2 万字，篇幅与版面相称
- [ ] 中文摘要约 200 字、关键词 3–5 个、JEL 分类号 3 个
- [ ] 注释①②③规范、文后依次列出；能随文者已随文
- [ ] 标题/表/图/等式/脚注分别连续编号，层级编号合规
- [ ] 参考文献体例统一、可核查；直接引用标页码
- [ ] 图表规范、编号连续、单位口径一致、有出处
- [ ] 基金项目、作者信息按系统要求填写

## 双盲匿名 hygiene

- [ ] 上传全文**隐去全部作者信息**（正文/注释/致谢/基金号）
- [ ] 自引改为第三人称或匿名占位
- [ ] 文件属性（作者名）已清除

## 提交前内容复核（调用其它 skill）

- [ ] 线别一致、匹配度够（`jfr-fit-positioning`）
- [ ] 识别策略可信、检验齐全（`jfr-identification`）
- [ ] 机制落到金融渠道（`jfr-mechanism`）
- [ ] 制度背景准确（`jfr-institutional-background`）
- [ ] 政策含义对象明确、不空转（`jfr-policy-implication`）

## 反模式

- 凭记忆套体例，不查最新《来稿须知》
- 忘给 JEL 分类号 / 关键词超 5 个
- 注释编号与文后列示不一致、编号跳号
- 忘隐去作者信息就投双盲

## 输出格式

```
【字数】正文约 X 万字
【摘要/关键词/JEL】X 字 / X 个 / X 个
【体例】注释①②③□ 连续编号□ 标题层级□ 参考文献□
【匿名】已清理 / 待清理 <点>
【系统】jryj.org.cn 在线投稿入口已确认
【内容复核】线别□ 识别□ 机制□ 制度□ 政策□
【结论】可投 / 待修 <清单>
```
