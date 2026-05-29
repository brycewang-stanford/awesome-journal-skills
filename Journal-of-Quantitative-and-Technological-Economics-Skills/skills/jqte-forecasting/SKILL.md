---
name: jqte-forecasting
description: Use when a 《数量经济技术经济研究》 (JQTE) manuscript makes a forecasting or prediction claim — macro forecasting, business-cycle / sentiment indices, mixed-frequency nowcasting, or model-based prediction. Enforces genuine out-of-sample evaluation (RMSE / MAE / directional accuracy / Diebold-Mariano), a proper benchmark, and a recursive / rolling design. The fastest desk-reject here is reporting in-sample fit only.
---

# 预测评估（jqte-forecasting）

## 触发时机

- 文章声称"能预测"某宏观/行业指标或景气
- 只报了样本内拟合（R²、拟合图），没有样本外检验
- 没有对比基准模型，无法说明"预测得更好"

## 本刊铁律：样本外评估 + 基准对比

**只报样本内拟合是高频拒因。** 预测的价值在样本外，必须有真正的 out-of-sample 设计和一个像样的基准。

## 必备四件套

1. **样本划分**：训练/验证/测试明确，或采用递归 (recursive) / 滚动 (rolling) 窗口，避免用全样本信息预测过去（信息泄漏）。
2. **基准模型**：至少与随机游走 (RW)、AR(p)、或一个简单基准比较——"比 naive 模型好"是底线。
3. **误差度量**：点预测报 RMSE / MAE / MAPE；方向性预测报方向准确率 (directional accuracy) / 混淆矩阵；必要时报区间预测覆盖率。
4. **统计显著性**：用 Diebold-Mariano（或 Clark-West，嵌套模型）检验预测差异是否显著，而非只看数字大小。

## 设计要点

- 预测期 (horizon) h 明确，多步预测报各 h 的误差，不只报 h=1
- 实时数据 vs 修订后数据：宏观预测应说明用的是哪种（real-time vs revised）
- 混频/nowcasting：信息集随时间更新的方式交代清楚
- 若做政策模拟/情景预测，区分"条件预测"与"无条件预测"

## 自检清单

- [ ] 有真正的样本外评估，不是样本内拟合
- [ ] 样本划分/滚动窗口无信息泄漏
- [ ] 至少一个基准模型（RW / AR）对比
- [ ] 报告 RMSE/MAE 或方向准确率，按 horizon 分列
- [ ] 用 Diebold-Mariano 等检验预测优势的显著性
- [ ] 数据修订/实时性问题有交代（宏观）

## 反模式

- 用全样本估计、再"预测"样本内的点，号称预测能力
- 只与自己的另一版模型比，不与 naive 基准比
- 报一个好看的 RMSE 却不做显著性检验
- 多步预测只报 h=1，回避长期表现
- 用修订后数据假装实时预测

## 输出格式

```
【预测对象 + horizon】<指标>，h = <…>
【样本划分】训练/测试 / 递归 / 滚动（无泄漏 □）
【基准】RW / AR / 其他 <…>
【误差度量】RMSE □ MAE □ 方向准确率 □
【显著性】Diebold-Mariano / Clark-West □
【实时性】real-time / revised
【下一步】jqte-sensitivity / jqte-tables-figures
```
