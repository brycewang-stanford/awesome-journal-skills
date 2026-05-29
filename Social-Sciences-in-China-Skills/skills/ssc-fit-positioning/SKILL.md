---
name: ssc-fit-positioning
description: Use to judge whether a manuscript is on-target for 《中国社会科学》 (Social Sciences in China) before investing in revision — screening for 思想分量 over technical sophistication, big-question level, cross-disciplinary reach, and original theory — and to recommend a better venue when fit is low. The most common save: stopping a niche empirical paper from being mis-submitted.
---

# 匹配度判断（ssc-fit-positioning）

## 触发时机

- 还没动笔大改前，先问"这篇够不够格、对不对口"
- 稿子是漂亮的细分实证，但拿不准综合刊会不会要
- 学科叙事摇摆，不知道该不该冲

## 三道筛子（任一不过即高风险）

1. **问题层级**：问题立在国家发展 / 文明 / 制度 / 治理这一层级吗？还是某细分市场/行业的评估？
2. **原创理论**：本文提出了概念 / 命题 / 分析框架吗？还是在验证已有结论？
3. **思想 vs 技术**：贡献是"看清了某个思想问题"，还是"方法/数据更新"？

> 《中国社会科学》的隐性门槛：**思想分量 > 方法复杂度**。技术精致但问题琐碎，几乎必然不在射程内。

## 匹配度评级

| 评级 | 特征 | 处置 |
|------|------|------|
| 高 | 大问题 + 原创命题 + 跨学科纵深 | 进入 `ssc-topic-problematic` 精修 |
| 中 | 问题够大但命题偏验证 / 思想性不足 | 先补 `ssc-theory-contribution`，否则改投 |
| 低 | 细分评估 / 纯技术展示 / 单学科常规活 | 改投对口期刊（见下） |

## 改投路由（fit 低时）

- 干净因果 + 理论：`economic-research` / `china-economic-quarterly`
- 产业/政策实证 + 强稳健性：`china-industrial-economics`
- 金融机理：`journal-of-financial-research`
- 国际/开放经济：`journal-of-world-economy`
- 定量/定性社会学：`sociological-studies`
- 数理模型/算法：`journal-of-management-sciences-china`

## 自检清单

- [ ] 能一句话说清"原创理论命题"（不是"实证发现"）
- [ ] 问题层级在制度/文明/治理，而非细分行业
- [ ] 有跨学科或理论纵深，不是单学科标准技术活
- [ ] 方法被翻译成了思想发现

## 反模式

- 用"数据新 / 方法新"自证够格——这恰是综合刊最不看重的
- 把"政策评估"当成"重大现实问题"——前者多半 desk reject

## 输出格式

```
【匹配度】高 / 中 / 低（一句话理由）
【问题层级】文明/制度/治理 | 行业/细分（需上移）
【原创性】提出命题 / 验证已有（后者需重构）
【思想-技术比】思想主导 / 技术主导（后者高风险）
【建议】精修本刊 / 先补理论 / 改投 <期刊>
```
