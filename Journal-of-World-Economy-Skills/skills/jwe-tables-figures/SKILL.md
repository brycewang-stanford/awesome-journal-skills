---
name: jwe-tables-figures
description: Use when finalizing the main tables and figures of a 《世界经济》 (The Journal of World Economy) manuscript — trimming over-wide regression tables, standardizing notes / clustering / significance, and presenting open-economy-specific objects (event-study plots, gravity tables, GVC decompositions). Use after results are settled.
---

# 表格与图（jwe-tables-figures）

## 触发时机

- 主表列数过多、信息过载，审稿人抓不到主结果
- 表注不规范（标准误层次、显著性、样本量缺失）
- 有事件研究 / 引力 / GVC 分解但展示方式不专业

## 主表原则

- **一张主表讲一个故事**：基准 + 关键稳健，控制 vs 不控制对比，4–6 列为宜，别堆到 10+ 列
- 每列报告：系数、标准误（注明聚类层次）、固定效应行、观测数、R²/拟合
- 显著性符号统一（*/**/***）并在表注定义；系数保留合理小数位
- 完整控制变量、次要稳健性放附录或备索

## 开放经济专属图表

| 对象 | 规范要点 |
|------|----------|
| **事件研究图** | 横轴相对处理期，含置信区间，处理前系数应近零（平行趋势） |
| **引力回归表** | 注明 PPML、固定效应结构（出口国×年、进口国×年、国家对）、零贸易处理 |
| **GVC 分解** | 注明分解法（KWW）、用哪张 MRIO 与年份、单位口径 |
| **shift-share** | 报告 exposure-robust 标准误，必要时附 Rotemberg 权重表 |
| **暴露度地图 / 分布** | 标注暴露度定义与数据来源 |

## 图的规范

- 《世界经济》为中文月刊（IWEP + 中国世界经济学会主办）：图表标题 / 注 用中文；变量定义清晰；可黑白打印仍可读（投稿前以官网最新版式要求为准）
- 不用花哨配色掩盖信息；坐标轴、单位、图例齐全
- 数据来源与样本期在图注标明

## 自检清单

- [ ] 主表 ≤ 6 列，主结果一眼可见
- [ ] 每表注明标准误聚类层次与显著性定义
- [ ] 固定效应、观测数、拟合优度齐全
- [ ] 事件研究图含 CI 且处理前近零
- [ ] 引力 / GVC / shift-share 表注明方法与口径
- [ ] 所有图表有数据来源与样本期

## 反模式

- 主表 10+ 列堆所有变量
- 表注不写聚类层次
- 事件研究图无置信区间
- 引力表不写是否 PPML

## 输出格式

```
【主表列数】X（建议 ≤6）
【表注规范】聚类□ 显著性□ FE□ N□
【专属图表】事件研究□ 引力□ GVC□ shift-share□
【数据来源标注】齐 / 缺
【下一步】jwe-policy-implication
```
