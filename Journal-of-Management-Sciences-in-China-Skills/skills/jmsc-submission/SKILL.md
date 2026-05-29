---
name: jmsc-submission
description: Use for the pre-submission preflight to 《管理科学学报》 (Journal of Management Sciences in China) — checking length (≤8000 chars; review ≤12000), abstract (≤300 chars), keywords (3–8), bilingual title/abstract, numbered-reference style 〔1〕 by order of appearance, formula numbering, theorem/symbol typesetting, and the online system (jmsc.tju.edu.cn). Verify every rule against the journal's current 投稿指南.
---

# 投稿前 preflight（jmsc-submission）

## 触发时机

- 模型、证明、算法、数值、文风都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿系统：**http://jmsc.tju.edu.cn**（作者注册后线上投稿；2012 年起全面线上）
- 篇幅：全文**以不超过 8000 字为宜**；综述可放宽到 **12000 字**（含图表）
- 摘要 **≤300 字**；关键词 **3—8 个**；需中英文标题/作者/单位/摘要/关键词
- 参考文献：限公开发表；**按文中出现先后排序**；正文引用**只写序号〔1〕〔2〕**
- 公式：**独立数学公式按先后统一编号**；符号/上下角标/外文字母印刷体规范
- 上传 Word 或 PDF；主办：国家自然科学基金委管理科学部 / 天津大学；月刊

> 体例、字数、模板以官网**最新《投稿指南/来稿须知》**为准。规则会变，投前务必复核，不要凭记忆。

## 体例 checklist

- [ ] 全文 ≤8000 字（综述 ≤12000），含图表
- [ ] 摘要 ≤300 字；关键词 3—8 个
- [ ] 中英文标题、作者、单位、摘要、关键词齐全且对齐
- [ ] 参考文献：公开发表、按出现先后排序、正文引用序号〔1〕〔2〕
- [ ] 参考文献书写格式参照本刊近期已发表论文
- [ ] 图表编号连续、有题、有出处

## 数理排版 checklist（本刊特有，最易被拒）

- [ ] **独立公式统一连续编号**，正文引用编号一致
- [ ] 定理/命题/引理/推论环境与编号统一（对接 jmsc-notation-style）
- [ ] **完整证明放附录**，正文留陈述 + 直觉，正文可读
- [ ] 记号一符一义、字体/上下标体例一致；建议附符号表
- [ ] 假设集中显式编号，正文按号引用
- [ ] 算法以伪代码呈现，复杂度/收敛性论证齐备

## 提交前内容复核（调用其它 skill）

- [ ] 对口数理赛道（`jmsc-fit-positioning`）
- [ ] 模型设定完整（`jmsc-model-building`）
- [ ] 命题有完整证明（`jmsc-proofs`）
- [ ] 算法有复杂度/收敛（`jmsc-algorithm`）
- [ ] 数值验证理论 + 给洞见（`jmsc-numerical-experiments`）
- [ ] 管理启示是决策规律、政策口号 = 0（`jmsc-managerial-insights`）

## 反模式

- 凭记忆套体例，不查最新《投稿指南》
- 正文引用写成作者-年份，而非序号〔1〕
- 公式漏编号或编号不连续
- 把完整证明堆在正文，正文读不下去
- 篇幅严重超 8000 字还不是综述

## 输出格式

```
【篇幅】X 字（≤8000？综述≤12000？）
【摘要/关键词】X 字（≤300）/ X 个（3—8）
【中英对齐】齐 / 缺 <项>
【参考文献】序号〔1〕□ 按出现排序□ 格式参照本刊□
【数理排版】公式编号□ 定理环境□ 证明入附录□ 记号统一□ 假设显式□
【内容复核】对口□ 模型□ 证明□ 算法□ 数值□ 启示□
【系统】jmsc.tju.edu.cn 已确认入口
【结论】可投 / 待修 <清单>
```
