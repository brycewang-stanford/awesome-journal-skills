---
name: nbr-measurement
description: Use for measurement rigor in 《南开管理评论》 (Nankai Business Review) survey studies — reliability (Cronbach's α, composite reliability), validity (convergent via AVE, discriminant via Fornell-Larcker / HTMT), and common-method-bias diagnosis (Harman single-factor, marker variable, common latent factor). Use whenever a paper uses self-report scales, especially if measures were borrowed or single-source.
---

# 测量规范（nbr-measurement）

## 触发时机

- 用了量表（个体或企业层级自报）
- 量表照搬国外/他文，未做本土化与心理测量
- 单一来源、同一时点测自变量与因变量（CMV 高风险）

## 信度（Reliability）

- **Cronbach's α** ≥ 0.70（探索性 0.60 可商榷，需说明）
- **组合信度 CR** ≥ 0.70
- 报告每个构念的题项数、均值/标准差、来源出处

## 效度（Validity）

| 类型 | 指标 | 经验门槛 |
|------|------|----------|
| 收敛效度 | 标准化载荷显著且较高；**AVE** | 载荷 > 0.50（宜 > 0.70）；AVE > 0.50 |
| 区分效度 | Fornell-Larcker：√AVE > 构念间相关 | 或 **HTMT** < 0.85（严格 0.90） |
| 内容效度 | 量表来源、专家评议、预测试 | 翻译-回译，本土化适配 |
| 结构效度 | 验证性因子分析（CFA）拟合 | 见 nbr-survey-sem 拟合标准 |

## 共同方法偏差（CMV / CMB）

自报、单源、同时点测量必须**事前防范 + 事后检验**：
- **事前**：自变量/因变量分时点或分来源；匿名；反向题；不同量尺
- **事后（任选并报告）**：
  - **Harman 单因子**：未旋转首因子方差 < 50%（最弱证据，别只用它）
  - **标记变量（marker variable）**：引入理论无关变量做局部调整
  - **共同潜因子（CLF / ULMC）**：加方法因子，比较载荷变化
- 结论要写明"CMV 不构成实质威胁"的依据，而非一句"做了 Harman"

## 自检清单

- [ ] 每个构念报告 α 与 CR（≥ 0.70）
- [ ] 报告 AVE（> 0.50）证收敛效度
- [ ] 用 Fornell-Larcker 或 HTMT 证区分效度
- [ ] 量表注明来源、是否本土化、预测试
- [ ] 自报数据做了 CMV 事前设计 + 至少一种事后检验（勿只靠 Harman）
- [ ] 控制变量的测量同样交代清楚

## 反模式

- 只报 α，不报 CR/AVE
- 借用量表不验证、不本土化，直接套
- CMV 只做 Harman 单因子就宣称"无偏差"
- 区分效度只看相关系数，不与 √AVE 比较

## 输出格式

```
【信度】构念 α / CR 列表（最低值 <…>）
【收敛】AVE 列表（最低 <…> 是否 > 0.50）
【区分】Fornell-Larcker / HTMT：通过□ 风险□
【量表来源】本土化□ 预测试□
【CMV】事前设计：<…>｜事后：Harman <%> + <标记/CLF> ｜结论：<…>
【下一步】nbr-survey-sem
```
