---
name: jqte-measurement
description: Use when the contribution of a 《数量经济技术经济研究》 (JQTE) manuscript is productivity / efficiency / index measurement — TFP, Malmquist, DEA, SFA, technical-progress decomposition, or index construction. Enforces transparent, reproducible construction plus sensitivity to method and parameter choices. This is the centerpiece skill for the journal's measurement track.
---

# 测度（jqte-measurement）

## 触发时机

- 贡献是 TFP / 效率 / 指数 / 技术进步分解
- 用了 DEA/SFA/Malmquist 但构造细节交代不清
- 审稿人或自己怀疑"换个方法/参数结论还成立吗"

## 本刊铁律：构造透明 + 可复现 + 敏感性

测度类论文的方法节是重头。**"量出一个数"不够，要让人能照着复现、并知道这个数对方法选择有多敏感。**

## 各方法的必交代项

### TFP（全要素生产率）

- 估计路径明确：增长核算（索洛余值）/ 参数法（OP、LP、ACF）/ 指数法，并说明为何选它
- 资本存量口径（永续盘存法的折旧率、基期、投资平减）显式给出
- 产出/投入的价格平减指数来源与基期统一
- 若做绿色/全要素能源效率，非期望产出的处理方式（方向距离函数等）讲清

### 效率前沿：DEA / SFA

- DEA：规模报酬假设（CRS/VRS）、导向（投入/产出）、是否超效率/窗口/Malmquist，投入产出变量选择有依据
- SFA：生产/成本函数形式（C-D / 超越对数）、无效率项分布假设（半正态/截断正态/指数）、是否含时变
- 投入产出变量的量纲、缺失值与异常值处理交代清楚

### Malmquist / 技术进步分解

- 分解为技术进步 (TC) × 技术效率变化 (EC)（必要时含规模效率）
- 几何平均基期选择、混合期距离函数构造说明
- 是否存在线性规划不可行解及其处理

### 指数构建

- 指标体系、权重来源（主观赋权/熵权/PCA/等权）说明，避免"拍脑袋"权重
- 标准化方法、量纲处理、缺失值补全可复现
- 给出权重/方法替代下的敏感性（接 `jqte-sensitivity`）

## 自检清单

- [ ] 方法选择有依据，不是"别人都这么用"
- [ ] 指标/参数构造透明，他人能照着复现
- [ ] 数据口径（资本存量、平减、基期）统一且交代清楚
- [ ] 做了方法/参数替代的敏感性（DEA 规模假设、SFA 分布、权重方案）
- [ ] 测度结果有量化解读，不止给一张表

## 反模式

- 用现成软件跑 DEA/SFA 却不交代规模假设、函数形式、分布假设
- 资本存量折旧率/基期凭默认值，不说明来源
- 指数权重随手定，无敏感性
- 只报一个测度结果，不验证对方法的稳健性

## 输出格式

```
【测度对象】TFP / 效率 / 指数 / 技术进步分解
【方法 + 依据】<方法> 因 <理由>
【关键参数/口径】<折旧率/基期/分布假设/权重方案…>
【可复现性】构造透明 □ 数据来源齐 □
【敏感性】已做 / 待做 <方法或参数替代>
【下一步】jqte-sensitivity / jqte-tables-figures
```
