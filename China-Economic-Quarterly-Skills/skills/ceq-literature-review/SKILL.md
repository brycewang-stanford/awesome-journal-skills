---
name: ceq-literature-review
description: Use when positioning a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript's contribution against the literature — benchmarking the precise method/result delta versus specific field papers (English + Chinese), not piling citations. Use after the topic is set and before/alongside identification.
---

# 文献与贡献定位（ceq-literature-review）

## 触发时机

- 综述只堆近年国内回归，没进 field 的方法/结论脉络
- 贡献写成"丰富了相关研究 / 填补国内空白"
- 说不清自己相对某篇具体文献做了什么新东西

## CEQ 的文献观：定位，不是清单

文献综述的唯一目的是**精确定位贡献**：你比 **具体某篇** 做得多/不同在哪。审稿人多有海外训练，会逐条核对你引的 field 文献是否到位、是否误读。

## 贡献陈述模板（对标具体文献）

> 不要写："本文丰富了关于 X 的研究。"
> 要写："相比 Author (Year, 期刊) 用 <方法> 得到 <结论>，本文用 <更干净的识别/新数据/新机制> 表明 <差异>，并解决了其 <未处理的内生性/异质性/外推问题>。"

贡献类型选一到两类讲清：
1. **识别更可信**（更干净的外生变异 / 现代 DID / 强工具）
2. **机制更明确**（区分竞争渠道 / 给出可证伪含义）
3. **新参数/新事实**（估计一个此前未识别的结构参数或因果量）
4. **方法范本**（识别策略或计量应用本身可被复用）

## 中英文献并重

- **必引 field 的方法/理论源头**（识别方法的原始文献、相关机制的经典理论），不能只引应用文章。
- 国内文献用来定位"本土证据缺口"，但不能替代国际对话。
- DID/IV/RDD 现代计量文献的引用见 `ceq-modern-did` 与 `ceq-inference`，方法用了就要引对应方法论文。

## 自检清单

- [ ] 引言里有一段"本文 vs 最接近的 1–3 篇"的精确差异
- [ ] 引用了所用识别方法的方法论原始文献（不是只引应用）
- [ ] 中英文献并重，国际对话不缺位
- [ ] 没有"丰富/填补/拓展"类空话贡献
- [ ] 引用的 field 结论无误读（关键文献复核过）

## 反模式

- 综述按时间流水账（A,2020；B,2021；C,2022）
- 只引应用文章，不引方法/理论源头
- 把"国内首次"当贡献
- 引一堆文献却说不清和哪篇最接近

## 输出格式

```
【最接近文献】1) ... 2) ... 3) ...
【本文差异】识别 / 机制 / 新参数 / 方法范本（选）
【贡献一句话】相比 X，本文 ...
【方法源头引用】齐 / 缺 <补>
【中英并重】是 / 否
【下一步】ceq-identification
```
