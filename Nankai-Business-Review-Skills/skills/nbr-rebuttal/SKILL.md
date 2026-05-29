---
name: nbr-rebuttal
description: Use to draft the revise-and-resubmit (R&R) response letter for 《南开管理评论》 (Nankai Business Review) — addressing reviewer concerns on theoretical contribution, mechanism logic, measurement (reliability/validity/CMV), analysis (mediation/moderation/HLM or experiment/qualitative rigor), and contextualization. Use only after the manuscript itself has been revised, not before.
---

# 外审回复（nbr-rebuttal）

## 触发时机

- 收到 R&R / 修改意见，需要逐条回复
- 多位审稿人意见冲突，需要协调

> 前置：**先改正文，后写回复**。回复信描述的是已落地的修改，不是承诺。

## 管理学审稿的高频意见与应对

| 审稿意见类型 | 应对要点 |
|--------------|----------|
| 理论贡献不清 / 只是验证 | 回 `nbr-theory-gap`：明确扩展/边界/整合，指名理论 |
| 假设缺机理 / 凭直觉 | 回 `nbr-hypothesis-development`：补机制链 |
| 量表信效度不足 | 回 `nbr-measurement`：补 α/CR/AVE、区分效度 |
| 共同方法偏差未排除 | 补标记变量 / CLF，勿只靠 Harman |
| 中介/调节方法不当 | 回 `nbr-survey-sem`：Bootstrap、简单斜率、moderated mediation 指数 |
| 嵌套数据未做多层 | 报告 ICC，改 HLM / 多层 SEM |
| 实验操纵/混淆质疑 | 补预测试、操纵检验、效应量 |
| 案例可信度/饱和不足 | 补三角验证、审计追踪、编码一致性、饱和依据 |
| 中国情境只是采样地 | 回 `nbr-china-context`：让情境进入模型与命题 |
| 讨论复述结果 | 回 `nbr-discussion-contribution`：回扣缺口、推进理论 |

## 回复信结构（逐条）

```
审稿人X-意见N（原文摘要）
→ 回应：接受 / 部分接受 / 商榷（给理由）
→ 修改：在第__页__段，已 <具体改动>
→ 证据：新表/新分析/新引文（如有）
```

## 写作原则

- **逐条、可定位**：每条意见对应页码段落，方便复审核对
- **接受要落地，商榷要有据**：不同意时用理论/方法依据礼貌说明，不空辩
- **协调冲突意见**：两位审稿要求相反时，说明取舍逻辑并知会编辑
- 语气专业、感谢，但不堆砌套话

## 自检清单

- [ ] 每条意见都有回应 + 定位 + 证据，无遗漏
- [ ] 正文确已按回复所述修改（先改后写）
- [ ] 商榷之处有理论/方法依据，非情绪化
- [ ] 冲突意见已协调并向编辑说明
- [ ] 新增分析（CMV/Bootstrap/HLM/操纵检验等）已并入正文与回复
- [ ] 回复信与修订稿编号、页码一致

## 反模式

- 笼统回"已按意见修改"，不给位置与证据
- 口头承诺却未真正改正文
- 对合理质疑硬辩或回避
- 两审冲突时各应付一句，自相矛盾

## 输出格式

```
【概述】共 X 条意见，接受 Y / 部分 Z / 商榷 W
【逐条】审稿X-N：回应 <…>｜改动 第_页_段 <…>｜证据 <…>
【新增分析】<CMV / Bootstrap / HLM / 操纵检验 …>
【冲突协调】<审稿A vs B 的取舍与说明>
【致编辑】<需编辑裁定的点>
```
