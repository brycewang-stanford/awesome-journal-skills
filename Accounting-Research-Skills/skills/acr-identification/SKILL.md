---
name: acr-identification
description: Use when the empirical identification strategy is the bottleneck for a 《会计研究》 (Accounting Research) manuscript — exogenous standard / regulatory changes (event study, DID), PSM, Heckman, IV — and you need to stress-test the design before drafting tables. Prefers standard/regulatory shocks as the cleanest accounting identification source.
---

# 因果识别策略（acr-identification）

## 触发时机

- 实证主体仅有 OLS + 控制变量，未处理内生性
- 用了准则/监管变更但没把它做成干净的 DID/事件研究
- DID 用 TWFE 但未回应近年异质性处理批评
- 自选择明显（如自愿披露、聘请大所）却没 PSM/Heckman

## 设计优先级（本刊偏好，强 → 弱）

1. **准则/监管外生变更 + DID 或事件研究**（本刊黄金来源：统一推行、对企业近似外生）
2. **断点回归**（清晰的监管门槛，如某规模/比例阈值触发披露义务）
3. **PSM + DID**（处理自选择 + 时间趋势）
4. **Heckman 两阶段**（自选择，如是否自愿披露、是否聘大所）
5. **工具变量**（强工具 + 排他性论证，会计场景工具较难，慎用）
6. OLS + 严密内生性讨论（描述性/计量基准类文章可接受）

## 分支路径

### 分支 A：准则/监管变更 DID（首选）
- 处理时点对齐准则**实际施行日**（见 `acr-institutional-standards`），非发布日
- 处理组/对照组界定来自适用范围（强制 vs 未覆盖）
- 平行趋势：事件研究图必须画；分批施行优先用 Callaway-Sant'Anna / Sun-Abraham，回应异质性处理偏误
- 安慰剂：随机处理时点 / 随机处理组 500–1000 次
- 预期效应：是否存在抢先反应（提前调整会计政策）

### 分支 B：PSM / PSM+DID
- 报告匹配变量、匹配方法（近邻/卡尺/核）、匹配后平衡性检验
- 共同支撑域、匹配前后差异

### 分支 C：Heckman
- 第一阶段选择方程须有**排他性约束变量**（影响选择不直接影响结果）
- 报告逆米尔斯比率显著性与方向

### 分支 D：RDD / IV
- RDD：McCrary 操纵检验、最优带宽 + 带宽稳健性、协变量平滑
- IV：第一阶段 F ≥ 10，排他性需理论/制度/安慰剂三段论证

## 必查清单

- [ ] 处理时点对齐准则施行日，处理/对照组界定有制度依据
- [ ] 平行趋势 / 平滑性 / 选择方程排他变量 已做
- [ ] 安慰剂检验（随机时点 / 随机处理组）
- [ ] staggered DID 回应异质性处理偏误（CS / SA / Bacon 分解）
- [ ] 标准误聚类层次合理（公司 / 公司+年 / 处理层级）
- [ ] 自选择已用 PSM 或 Heckman 处理

## 反模式

- 用"我们认为该准则外生于公司决策"但无制度论证与安慰剂
- TWFE + 分批施行但不讨论异质性处理偏误
- 把发布日当施行日设事件窗口
- 会计场景硬找工具变量，排他性站不住
- Heckman 第一阶段无排他性约束，等同主回归加一项

## 输出格式

```
【识别策略】准则DID / 事件研究 / PSM / Heckman / RDD / IV
【处理时点】<施行日对齐？> 处理组/对照组依据
【已完成检验】[平行趋势, 安慰剂, 平衡性, 排他变量, ...]
【缺失检验】[...]
【聚类层次】...
【下一步】acr-mechanism
```
