---
name: acr-robustness
description: Use when building the robustness section for a 《会计研究》 (Accounting Research) manuscript — replacing accounting measures with alternatives, adding governance / institutional controls, placebo tests, and endogeneity follow-ups — so the main result survives an accounting referee's scrutiny. Use after mechanism is settled.
---

# 稳健性与敏感性（acr-robustness）

## 触发时机

- 主结果只跑了一种度量、一套控制变量
- 没替换会计度量、没控治理/制度变量
- 内生性只在主表处理，未做后续敏感性
- 审稿人质疑"结果是否对度量/设定敏感"

## 本刊稳健性的四个支柱

1. **替换会计度量**：主度量换替代（如 DA 换真实盈余管理、C-Score 换 Basu、披露指数换文本指标），结论不变
2. **控制治理与制度变量**：加入股权集中、两职合一、机构持股、产权性质、地区市场化、行业×年度固定效应，排除遗漏变量
3. **安慰剂/伪检验**：随机处理时点、随机处理组、伪事件、错位样本
4. **内生性后续**：PSM 不同匹配、加入更多协变量、改变聚类、删除特殊年份/行业、Heckman 备择设定

## 会计特有的稳健性动作

| 关注 | 稳健性做法 |
|------|-----------|
| 应计度量口径 | 资产负债表法 vs 现金流量表法总应计互验 |
| 分年分行业估计噪声 | 改变行业分类（证监会门类 vs 二级）、最低观测数门槛 |
| 极端值 | 不同缩尾/截尾水平（1% vs 5%）、winsorize vs truncate |
| 样本构成 | 剔除金融业、ST、IPO 当年、亏损企业 |
| 准则识别窗口 | 改变事件窗口、剔除施行过渡年、安慰剂年份 |
| 真实 vs 应计操纵 | 同时控制两者，排除替代效应混淆 |

## 自检清单

- [ ] 主会计度量有 ≥1 个替代度量复现结论
- [ ] 控制了治理 + 制度（产权/市场化/固定效应）变量
- [ ] 至少一类安慰剂/伪检验
- [ ] 缩尾水平、样本筛选做了敏感性
- [ ] 内生性后续（PSM 设定/聚类/窗口）补齐
- [ ] 稳健性结果与主表方向一致，差异有解释

## 反模式

- 稳健性只是"换一个控制变量再跑一次"，无替代度量
- 不控产权性质/市场化等中国制度变量
- 安慰剂只做随机处理组，不做随机时点（或反之）
- 替代度量结果不一致却不讨论，只报支持的那个
- 把稳健性堆成附录但正文不交代关键结论

## 输出格式

```
【替代度量】<主→替代，结论是否一致>
【制度/治理控制】产权□ 市场化□ 固定效应□
【安慰剂】随机时点□ 随机处理组□ 伪事件□
【敏感性】缩尾□ 样本筛选□ 窗口□
【内生性后续】PSM设定□ 聚类□ Heckman备择□
【一致性】与主表方向一致 / 差异解释
【下一步】acr-tables-figures
```
