---
name: jqte-literature-review
description: Use when building the literature review for a 《数量经济技术经济研究》 (JQTE) manuscript — organizing it around the method lineage (how a quantity has been measured / a series forecast / a structure decomposed) and the China-data application gap, rather than a chronological pile of recent empirical citations. Use after the topic and contribution type are set.
---

# 文献综述（jqte-literature-review）

## 触发时机

- 综述只按时间堆近年实证，看不出方法演进
- 引用一堆"X 影响 Y"，但没交代"前人怎么量/怎么预测/怎么分解"
- 讲不清本文方法相对前沿的位置与缺口

## 本刊综述的核心：方法脉络 + 应用缺口

JQTE 的综述不是验证某个理论命题的对话，而是**把"测度/预测/分解某对象"的方法谱系讲清**，并指出本文落在哪个缺口：

1. **测度/方法源流**：该量（TFP、效率、某指数、某结构）历史上用什么方法量？各方法的假设与局限？
2. **前沿进展**：近年方法的改进（如非参/半参效率前沿、混频、机器学习计量、动态 SDA）。
3. **中国数据应用缺口**：在中国数据/口径下，现有做法的不足（数据可得性、口径不一致、参数难校准），本文如何补。

## 引用结构建议

| 层 | 内容 |
|----|------|
| 方法源流 | 经典方法 + 提出者（如 Malmquist 指数、SFA、随机前沿、Leontief IO） |
| 方法前沿 | 近年方法学改进文献 |
| 中国应用 | 中文与中国数据相关的应用研究及其口径问题 |
| 本文定位 | 一句话：本文在方法/口径/数据上补哪个缺口 |

## 自检清单

- [ ] 综述按"方法源流 → 前沿 → 中国应用缺口"组织，不是按时间堆砌
- [ ] 关键方法引到原始提出者，不只引二手应用
- [ ] 明确指出现有测度/预测/分解在中国数据上的具体不足
- [ ] 本文方法定位与缺口对齐，能自然引出方法节
- [ ] 中英文献并重，方法学经典文献不缺位

## 反模式

- 把综述写成"近五年回归大全"，看不出方法演进
- 只引应用文献、不引方法原始文献
- 缺口写成空话（"研究尚不充分"），不落到具体方法/口径问题
- 综述与后文方法节脱节，引不出本文贡献

## 输出格式

```
【方法源流】<经典方法 + 提出者>
【前沿进展】<近年方法学改进>
【中国应用缺口】<具体的数据/口径/参数不足>
【本文定位】本文补 <…> 缺口
【缺位文献】[需补的方法学经典/前沿]
【下一步】jqte-measurement / jqte-econometric-methods / jqte-io-cge
```
