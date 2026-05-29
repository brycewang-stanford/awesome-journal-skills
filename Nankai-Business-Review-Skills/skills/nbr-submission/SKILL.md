---
name: nbr-submission
description: Use for the pre-submission preflight to 《南开管理评论》 (Nankai Business Review) — checking abstract/keyword limits, manuscript length, bilingual title/abstract, reference style (GB/T 7714 plus the journal's 来稿规范说明), the online submission system at nbr.nankai.edu.cn, anonymity, and document hygiene. Use right before submitting; verify every rule against the journal's current 来稿规范说明.
---

# 投稿前 preflight（nbr-submission）

## 触发时机

- 正文、贡献、测量都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿系统 / 官网：**https://nbr.nankai.edu.cn/**（在线投稿经官网入口）
- 主管 / 主办：教育部主管；南开大学（商学院）主办
- 摘要 **100–300 字**（多数指引建议 300 字左右）；关键词 **3–8 个**
- 篇幅：以 **8–15 千字**为宜，一般不超过 **2 万字**
- 配**中英文**标题 / 摘要（英文约 300 词，可不与中文严格对应）/ 关键词
- 参考文献：正文内实引、文末对应；著录参照 **GB/T 7714** 及官网《来稿规范说明》
- 一稿一投，勿重复投稿

> 字数、篇幅、体例均**以官网公告栏最新《来稿规范说明》为准**。规则会变，投前务必复核，不要凭记忆。现行刊期（月刊/双月刊）以官网为准。

## 体例 checklist

- [ ] 中文标题（建议不超过 20 字）、作者与单位齐全
- [ ] 摘要 100–300 字、关键词 3–8 个
- [ ] 中英文标题 / 摘要 / 关键词齐备（英文质量过关）
- [ ] 结构顺序：标题→摘要→关键词→引言→正文→结论→参考文献→注释→英文部分→附录
- [ ] 参考文献文中实引、标号对应、GB/T 7714 + 官网规范
- [ ] 图表规范、编号连续、有出处
- [ ] 基金项目、作者简介按系统要求填写
- [ ] 篇幅 8–15 千字（不超 2 万字）

## 匿名评审 hygiene

- [ ] 正文/注释/致谢中**去除可识别作者身份**信息
- [ ] 自引改为第三人称或匿名占位
- [ ] 文件属性（作者名）已清除

## 提交前内容复核（调用其它 skill）

- [ ] 理论缺口与贡献立得住（`nbr-theory-gap`）
- [ ] 每条假设有机理（`nbr-hypothesis-development`）
- [ ] 信效度 + CMV 齐全（`nbr-measurement`）
- [ ] 分析规范：Bootstrap / 简单斜率 / HLM 或实验质控（`nbr-survey-sem` / `nbr-experiment` / `nbr-qualitative-case`）
- [ ] 情境进入理论（`nbr-china-context`）
- [ ] 讨论推进理论、非复述（`nbr-discussion-contribution`）

## 反模式

- 凭记忆套体例，不查官网最新《来稿规范说明》
- 摘要超 300 字 / 关键词超 8 个 / 篇幅超 2 万字
- 英文摘要机翻、质量差
- 忘清匿名信息就投盲审

## 输出格式

```
【体例】摘要 X 字 / 关键词 X 个｜中英对齐□ 参考文献 GB/T 7714□
【篇幅】X 千字（≤ 2 万）
【匿名】已清理 / 待清理 <点>
【系统】nbr.nankai.edu.cn 入口已确认
【内容复核】缺口□ 假设机理□ 信效度CMV□ 分析□ 情境□ 讨论□
【结论】可投 / 待修 <清单>
```
