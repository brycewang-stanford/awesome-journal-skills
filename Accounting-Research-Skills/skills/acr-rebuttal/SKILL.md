---
name: acr-rebuttal
description: Use when responding to 《会计研究》 (Accounting Research) reviewer reports / an R&R — drafting a point-by-point response letter and 修改说明 that addresses accounting-measure construction, institutional/standard accuracy, identification, and information-mechanism concerns, while keeping the revision anonymous. Use only after the manuscript itself has been revised.
---

# 外审回复 / R&R（acr-rebuttal）

## 触发时机

- 收到《会计研究》外审意见或修改要求（双向匿名、三审制）
- 已对正文做了实质修订，需要写回复信与修改说明
- 多位审稿人意见冲突，需要协调回应

## 前提：先改正文，再写回复

回复信不替代修订。**先在正文落实修改**，回复信只解释"改了什么、在哪、为什么"。修改说明同样需匿名（不得泄露作者身份）。

## 会计稿外审高频意见类型与应对

| 意见类型 | 应对要点 |
|----------|----------|
| 度量不规范/不可复现 | 补充模型、估计粒度、样本与缩尾说明；加替代度量复现（`acr-measurement`） |
| 落点像公司金融 | 强化信息机制主线、改/加会计信息因变量（`acr-fit-positioning` / `acr-mechanism`） |
| 制度背景/准则有误 | 核实条款、文号、施行时点并更正，附官方出处（`acr-institutional-standards`） |
| 内生性/识别不足 | 补准则外生变更 DID、PSM、安慰剂、平行趋势（`acr-identification`） |
| 机制是定价而非信息 | 直接测信息中介变量，做理论一致的横截面切分（`acr-mechanism`） |
| 稳健性不够 | 替代度量、制度/治理控制、敏感性（`acr-robustness`） |
| 贡献只有"丰富文献" | 重写理论贡献 + 具体准则/监管启示（`acr-implications`） |

## 回复信结构

1. **总述**：感谢 + 概述主要修改（一段，点出最重要的 2–3 处实质改进）
2. **逐条回应**：每条复制审稿意见原文 → 回应 → 指明修改位置（页/段/表号）
3. **冲突意见**：如两位审稿人要求相反，说明取舍理由，必要时折中并双向交代
4. **未采纳的意见**：礼貌、给学理理由，不硬顶；能补检验则补

## 回应写法规范

- 逐条、对号入座，不遗漏；引用审稿人原文再回应
- 用证据回应（新表、新检验、新出处），不空许诺
- 指明修改在正文的确切位置（"见修订稿第 X 页第 Y 段 / 表 Z"）
- 语气专业、谦逊；对的就改，不对的讲道理
- 修改说明与正文保持匿名

## 自检清单

- [ ] 正文已实质修订，回复信与之一致
- [ ] 每条意见都有回应且指明修改位置
- [ ] 度量/制度/识别/机制类意见用证据回应
- [ ] 冲突意见有取舍说明
- [ ] 未采纳项给了学理理由
- [ ] 回复信/修改说明已匿名

## 反模式

- 回复信先于正文修订生成（空头承诺）
- "已修改"但正文没动，或位置指不出
- 对识别/度量质疑只辩解不补检验
- 硬顶审稿人或泄露作者身份

## 输出格式

```
【意见总数】X（审稿人 A: n / B: m / ...）
【逐条状态】已回应 X / X；均指明位置□
【实质修改】[度量补充, 制度更正, 新增识别检验, 机制中介, ...]
【冲突处理】<取舍说明>
【未采纳】<条目 + 学理理由>
【匿名】回复信/修改说明已清理□
【结论】可提交修订 / 待补 <清单>
```
