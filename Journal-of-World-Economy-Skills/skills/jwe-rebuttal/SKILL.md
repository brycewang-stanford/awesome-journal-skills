---
name: jwe-rebuttal
description: Use when responding to 《世界经济》 (The Journal of World Economy) referee reports (R&R) — structuring a point-by-point response letter that addresses the journal's characteristic challenges (open-economy fit, shift-share / gravity inference, transmission channel, GVC measurement). Use after the manuscript has actually been revised.
---

# 外审回复（jwe-rebuttal）

## 触发时机

- 收到《世界经济》R&R / 外审意见，需要写回复信
- 多位审稿人意见冲突，不知如何取舍
- **前提：正文已据意见实修订**——回复信只对应已落地的修改

## 回复信结构

- 开头：感谢 + 一段总述（本轮主要修改与文稿改进概览）
- 按审稿人、逐条编号回应：**引用意见原文 → 修改说明 → 标注正文位置（页/表/段）**
- 每条明确"已修改 / 已补充 / 部分采纳并说明 / 不采纳并论证"
- 附修改对照（旧 → 新）便于审稿人核对

## 本刊高频意见与应对

| 审稿人常问 | 应对要点 |
|------------|----------|
| "国际 / 开放维度是否够" | 强化引言开放维度定位；必要时回 `jwe-fit-positioning` 重判，或补跨境机制证据 |
| "shift-share / Bartik 推断" | 补份额外生性论证、Rotemberg 权重、exposure-robust 标准误（GPSS / BHJ / AKM） |
| "外部冲击是否真外生" | 补制度 / 时序证据 + 安慰剂 + 预期效应检验 |
| "机制只是叙事" | 用分样本 / 中介 / 排除竞争渠道做实（`jwe-transmission-channel`） |
| "GVC 度量是否可靠" | 注明分解法（KWW）与 MRIO 来源年份，加替代分解稳健性 |
| "引力设定" | 改 PPML + 多边阻力固定效应，零贸易处理 |
| "只引国内文献" | 补国际贸易 / 金融经典与前沿对话（`jwe-literature-review`） |
| "政策含义太空 / 偏国内" | 重写到开放政策层并回指证据（`jwe-policy-implication`） |

## 写作礼仪

- 语气专业、就事论事；不与审稿人争意气
- 不采纳的意见要给**有理有据**的论证，不回避
- 审稿人意见冲突时，说明取舍依据并让编辑可裁断
- 新增分析若改变结论，诚实说明并更新摘要 / 政策含义

## 自检清单

- [ ] 每条意见都有独立回应，无遗漏
- [ ] 每条标注正文修改位置（页 / 表 / 段）
- [ ] 涉及 shift-share / 引力 / GVC 的方法质疑已用现代规范回应
- [ ] 不采纳项有论证，非回避
- [ ] 正文已实改，回复与正文一致

## 反模式

- 正文未改就先写"已修改"
- "感谢建议，我们会注意"式空回应
- 只回应好回的，回避识别 / 推断硬骨头
- 新结论与摘要 / 政策含义不同步更新

## 输出格式

```
【意见总数】X（审稿人 A: n / B: m）
【已逐条回应】是 / 否（缺 <编号>）
【方法类质疑】shift-share□ 引力□ GVC□ 外生性□
【正文位置标注】齐 / 缺
【不采纳项】[编号 → 论证]
【结论】可回复 / 待补 <清单>
```
