---
name: ceq-figures
description: Use when building or auditing the exhibits of a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript — favoring figures over tables (event-study plots, bin-scatter, model-fit / counterfactual figures) so the main result is legible at a glance, since many readers consume the English abstract plus figures. Use after identification and mechanism are settled.
---

# 图表（图优于表）（ceq-figures）

## 触发时机

- 主结果全靠回归表，没有一张能独立讲清的图
- DID/IV/RDD 缺配套诊断图
- 定稿阶段需要把主图打磨到"审稿人扫一眼就懂"

## CEQ 的图表观：图是主角

很多读者只读**英文摘要 + 图**。主结果应能用一张图讲清；表是补充。每张主图须**自洽**：标题、坐标轴、单位、置信带、样本说明齐全，脱离正文也能读懂。

## 按设计选主图

| 设计 | 必备主图 |
|------|----------|
| DID / event-study | **事件研究图**：动态系数 + 95% CI，前置系数近零（用现代估计量，见 `ceq-modern-did`） |
| RDD | 断点图：bin-scatter + 局部多项式拟合，断点处跳跃可见 |
| IV | 第一阶段散点 / reduced-form 关系图 |
| 连续处理 / 剂量反应 | bin-scatter（分箱散点 + 拟合） |
| 结构估计 | **模型拟合图**（数据 vs 模型矩）+ 反事实图 |
| 异质性 / 机制 | 分组系数 forest plot |

## 制图规范

- 事件研究图：横轴相对处理期，0 期前后对称，标出参照期，画 95% CI 而非仅点。
- bin-scatter：分箱数说明，叠加原始拟合，避免视觉误导。
- 置信带优先于星号；颜色在黑白打印下可辨。
- 图注写清：估计量、样本、聚类层级、CI 含义。
- 数量级与单位标注；不要默认读者知道 y 轴是对数还是水平。

## 自检清单

- [ ] 主结果有一张能独立讲清的图
- [ ] DID 有事件研究图，前置系数近零且来自现代估计量
- [ ] RDD/IV/结构 各有对应诊断/拟合图
- [ ] 每张图自洽（标题/轴/单位/CI/样本说明齐全）
- [ ] 图脱离正文仍可读；黑白打印可辨
- [ ] 图与表不重复堆同一信息

## 反模式

- 只放回归表，让审稿人自己脑补动态效应
- 事件研究图用被污染的 TWFE 系数
- bin-scatter 不说明分箱数，制造虚假平滑
- 图注缺失，必须翻正文才懂坐标轴含义
- 用一堆装饰性图凑数，主结果反而没有图

## 输出格式

```
【主图】有 / 无（能否独立讲清主结果）
【事件研究图】有 □ 来自现代估计量 □ 前置近零 □
【设计配套图】RDD/IV/结构 拟合图：齐 / 缺 <补>
【自洽性】标题/轴/单位/CI/样本：齐 / 缺 <补>
【图表分工】图为主 □ 表不冗余 □
【下一步】ceq-abstract-english
```
