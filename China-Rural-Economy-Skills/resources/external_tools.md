# 三农实证研究外部工具与资源

本文档整理了向《中国农村经济》投稿实证研究论文时可能需要的外部工具、数据资源和辅助软件，侧重农业、农村、农户（三农）研究场景。

## 一、数据资源

### 农户 / 个体微观调查（三农核心数据）
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 中国家庭追踪调查（CFPS） | 北京大学 | 农户收入、教育、迁移、家庭决策 |
| 中国家庭金融调查（CHFS） | 西南财经大学 | 农户金融、信贷、资产、消费 |
| 中国劳动力动态调查（CLDS） | 中山大学 | 农村劳动力、就业、流动 |
| 全国农村固定观察点 | 农业农村部 | 农户经营、收入、土地（长期追踪） |
| 中国健康与养老追踪调查（CHARLS） | 北京大学 | 农村老龄、健康、养老 |
| 中国营养与健康调查（CHNS） | 中国疾控中心等 | 农村健康、营养、收入 |
| 中国乡城人口流动调查（RUMiC） | 多机构 | 农民工、流动人口 |

### 村级 / 区域与宏观农业数据
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 中国农村统计年鉴 | 国家统计局 | 农业产出、农村发展宏观指标 |
| 中国县域统计年鉴 | 国家统计局 | 县域经济、城乡 |
| 农业农村部统计数据 | 农业农村部 | 粮食、播种面积、农产品价格 |
| 中国农业普查 | 国家统计局 | 农业经营主体、农地、农机 |
| 海关 / 农产品贸易数据 | 海关总署 | 农产品进出口、贸易 |

### 政策类数据
| 数据源 | 说明 | 获取方式 |
|--------|------|----------|
| 土地确权 / 流转政策 | 试点批次、实施时点 | 政策文件整理 |
| 脱贫县 / 贫困县名录 | 用于断点 / DID | 国务院扶贫办（历史）/ 乡村振兴局 |
| 农业补贴政策 | 粮食、农机、良种补贴 | 农业农村部 / 财政部文件 |
| 高标准农田 / 农村基建 | 项目分布与时序 | 政策文件、地方公报 |

## 二、统计软件

### Stata
- **推荐版本**：Stata 17/18 SE
- **常用包**：
  - `didregress` / `csdid` / `did_multiplegt`：交叠 / 连续处理 DID
  - `eventstudyinteract`：Sun-Abraham 事件研究
  - `bacondecomp`：Goodman-Bacon 分解
  - `xtreg`：面板固定效应（农户 / 村面板）
  - `ivreg2` / `ivreghdfe`：工具变量（处理农户自选择）
  - `psmatch2` / `teffects psmatch`：倾向得分匹配
  - `rdrobust` / `rddensity`：断点回归 + 密度检验
  - `medsem` / `causalmed`：中介 / 因果中介
  - `winsor2`：缩尾处理

### Python
- **常用库**：
  - `pandas` / `numpy`：数据处理与数值计算
  - `linearmodels`：面板与 IV 估计
  - `statsmodels`：计量模型
  - `scikit-learn`：机器学习（PSM / 倾向得分）
  - `matplotlib` / `seaborn`：可视化

### R
- **常用包**：
  - `dplyr` / `tidyr`：数据处理
  - `fixest`：高维固定效应 + 交互
  - `did`（Callaway-Sant'Anna）/ `didimputation`：现代 DID
  - `plm`：面板数据
  - `MatchIt`：倾向得分匹配
  - `rdrobust` / `rddensity`：断点回归
  - `mediation`：因果中介

## 三、识别策略辅助工具

### 现代交叠 DID（处理 staggered 偏误）
- `csdid` / `did`（Callaway-Sant'Anna）
- `eventstudyinteract`（Sun-Abraham）
- `did_multiplegt`（de Chaisemartin-D'Haultfœuille）
- `bacondecomp`（坏比较权重诊断）

### 工具变量与弱工具
- `ivreghdfe` / `ivreg2`
- `weakivtest`、Anderson-Rubin 检验（弱工具稳健 CI）

### 倾向得分匹配 / 双稳健
- `psmatch2`、`teffects`、`drdid`
- `rbounds`：Rosenbaum 敏感性分析（不可观测选择性）

### 断点回归
- `rdrobust`（最优带宽）
- `rddensity`（McCrary 密度检验，防农户操纵分组）

### 合成控制
- `synth` / `synth_runner`（Stata）、`Synth` / `tidysynth`（R）

## 四、数据处理与可视化

- **数据清洗**：Stata（面板）、Python pandas（大规模）、R dplyr
- **科研图表**：ggplot2、matplotlib、Origin
- **事件研究 / 森林图**：`coefplot`（Stata）、`ggplot2`（R）
- **空间 / 地理分布图**：QGIS、`sf` + `ggplot2`（注意村庄样本脱敏）
- **流程 / 机制路径图**：Draw.io、ProcessOn、Visio

## 五、学术写作辅助

### 文献管理
| 工具 | 说明 |
|------|------|
| Zotero | 开源免费，插件丰富 |
| EndNote | 商业软件，期刊格式支持多 |
| NoteExpress | 国内用户多，中文期刊格式友好 |

### 参考文献格式
《中国农村经济》采用本刊统一格式，Zotero / EndNote 可自定义样式；具体格式以官网投稿须知为准。

### 查重检测
- 知网查重（中文期刊认可）

## 六、投稿与协作

### 系统要求
- 浏览器：Chrome、Firefox、Edge
- 文档格式：DOC / DOCX
- 在线投稿系统 + 双向匿名评审（具体网址以官网为准）

### 扩展资料格式
- 附录：Word 文档
- 数据：Excel / Stata dta / CSV
- 代码：Stata .do/.ado、Python .py、R .R

### 版本控制与云存储
- Git + GitHub / Gitee（代码管理）
- 坚果云 / 百度网盘（数据备份与分享）

## 七、注意事项

1. **数据合规**：使用调查数据遵守使用协议，农户个人信息严格脱敏
2. **自选择处理**：农户入社 / 务工 / 流转等行为是自选择，识别时必须正面处理内生性
3. **时间逻辑**：跨轮次面板要保证机制变量在处理之后、结果之前测量，不用未来信息
4. **代码注释**：实证代码详细注释，便于审稿核查与录用后提交
5. **数据来源点名**：变量来源精确到调查 / 数据库，自行调研的交代抽样与样本量

## 八、常用网站

| 网站 | 用途 |
|------|------|
| 中国社会科学院农村发展研究所 | 主办单位 |
| 《中国农村经济》官网 / 投稿系统 | 投稿（网址以官网为准） |
| 《中国农村观察》 | 姊妹刊 |
| CNKI | 中文文献检索 |
| Web of Science / Google Scholar | 国际文献检索 |
| AgEcon Search | 农业经济学预印本与会议论文 |
