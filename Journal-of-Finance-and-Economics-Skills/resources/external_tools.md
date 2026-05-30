# 实证研究外部工具与资源

本文档整理了向《财经研究》(Journal of Finance and Economics) 投稿实证研究论文时可能需要的外部工具、数据资源和辅助软件。《财经研究》是综合性财经类期刊，涵盖财政、产业、金融与公司财务、国际贸易、劳动、区域与发展、数字经济等方向，对**权威微观数据 + 现代因果识别**有明确要求。

> 提示：数据库覆盖年限、访问方式与授权政策会随时间变化，使用前请以各数据库官方说明为准。

## 一、数据资源

### 公司金融 / 公司财务类
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 国泰安（CSMAR） | 深圳希施玛数据科技有限公司 | 上市公司财务、治理、股价、债券 |
| Wind | 万得信息技术股份有限公司 | 金融市场、债券、基金、宏观高频 |
| 中国研究数据服务平台（CNRDS） | 北京博科恒辉科技有限公司 | 创新专利、ESG、媒体、文本 |
| 锐思（RESSET） | 北京色诺芬 | 财务、市场、基金 |
| CCER 经济金融数据库 | 北京大学 | 上市公司、宏观、行业 |

### 产业 / 贸易类
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 中国工业企业数据库 | 国家统计局 | 工业企业生产、出口、全要素生产率 |
| 中国海关进出口数据库 | 海关总署 | 贸易、进出口、企业出口产品 |
| 企业专利数据 | 国家知识产权局 / incoPat | 创新、专利质量 |
| 工商企业注册（天眼查 / 企查查） | 商业机构 | 企业成立、注销、股权穿透 |

### 财政 / 税收类
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 全国税收调查数据库 | 国家税务总局 | 税收、企业税负、减税政策 |
| 财政部 / 地方财政决算 | 财政部 | 财政收支、转移支付 |
| 地方政府债务 / 城投债 | Wind / CNRDS | 地方债、隐性债务 |

### 家庭 / 个体微观调查
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 中国家庭金融调查（CHFS） | 西南财经大学 | 家庭金融、消费、住房、财富 |
| 中国家庭追踪调查（CFPS） | 北京大学 | 收入、教育、就业、健康 |
| 中国健康与养老追踪调查（CHARLS） | 北京大学 | 健康、养老、劳动供给 |
| 中国综合社会调查（CGSS） | 中国人民大学 | 社会态度、主观福利 |

### 宏观 / 区域类
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 中国统计年鉴 / 城市统计年鉴 / 县域统计 | 国家统计局 | 宏观、区域、城市经济 |
| 中国分省份市场化指数 | 王小鲁等 | 制度环境、市场化程度异质性 |
| 世界银行 WDI | World Bank | 国际比较 |
| CEIC / IMF / OECD | 商业及国际机构 | 宏观高频、国际比较 |

## 二、统计软件

### Stata
- **推荐版本**：Stata 17/18 SE 及以上
- **常用包**：
  - `reghdfe`：高维固定效应回归（财经实证主力）
  - `did_multiplegt` / `csdid` / `eventdd`：交错 DID 与事件研究稳健估计
  - `xtreg` / `areg`：面板固定效应
  - `ivreg2` / `ivreghdfe`：两阶段最小二乘、弱工具检验
  - `rdrobust` / `rddensity`：断点回归与密度检验
  - `psmatch2` / `teffects`：倾向得分匹配
  - `synth` / `synth_runner`：合成控制
  - `boottest` / `reghdfe + cluster`：聚类标准误与 wild bootstrap
  - `winsor2`：缩尾处理
  - `estout` / `outreg2`：三线表导出

### Python
- **常用库**：
  - `pandas` / `numpy`：数据处理与数值计算
  - `linearmodels`：面板、IV、固定效应
  - `statsmodels`：计量模型
  - `econml` / `doubleml`：双重机器学习、因果森林
  - `scikit-learn`：ML 学习器（nuisance 估计 / PSM）
  - `matplotlib` / `seaborn`：可视化

### R
- **常用包**：
  - `fixest`：高维固定效应、事件研究（`feols` + `i()`）
  - `did`（Callaway-Sant'Anna）/ `didimputation`：交错 DID
  - `AER` / `ivreg`：工具变量
  - `rdrobust`：断点回归
  - `MatchIt`：倾向得分匹配
  - `DoubleML` / `grf`：双重机器学习、广义随机森林
  - `modelsummary` / `fixest::etable`：三线表

### MATLAB
- 适用于 DSGE、结构估计等理论模型

## 三、识别策略辅助工具

### 交错（staggered）DID
- `csdid`（Callaway-Sant'Anna）、`did_multiplegt`（de Chaisemartin-D'Haultfœuille）
- `eventdd` / `event_plot`：事件研究图
- `bacondecomp`：Goodman-Bacon 分解，诊断"坏比较"权重

### 工具变量
- `ivreg2` / `ivreghdfe`：弱工具 F 统计量、过度识别检验
- `weakivtest` / `rivtest`：弱工具稳健推断（Anderson-Rubin）

### 断点回归
- `rdrobust`：最优带宽、稳健置信区间（推荐）
- `rddensity`：操纵检验（McCrary 改进）

### 合成控制
- `synth` / `synth_runner`（Stata）、`Synth`（R）

### 双重机器学习
- `doubleml`（Python / R）、`econml`

## 四、数据处理与可视化

### 数据清洗
- Stata（面板清洗、缩尾）
- Python pandas（大规模工企 / 海关数据合并）
- R dplyr / data.table（高效整理）

### 图形制作
- **科研图表**：ggplot2、matplotlib、Stata `twoway`
- **流程图 / 机制图**：Draw.io、ProcessOn、Visio
- **导出要求**：≥ 300 dpi，黑白 + 1–2 主色，避免叠加过多曲线

### LaTeX 排版
- TeX Live / MacTeX、TeXstudio / VS Code + LaTeX Workshop、Overleaf

## 五、学术写作辅助

### 文献管理
| 工具 | 说明 |
|------|------|
| Zotero | 开源免费，插件丰富 |
| EndNote | 商业软件，期刊格式支持多 |
| NoteExpress | 国内中文文献管理常用 |

### 参考文献格式
《财经研究》中文文献与英文文献分别按规范排列，中文期刊用全名（《财经研究》不写缩写）。Zotero / EndNote 可设置对应样式，但务必以官网当年"投稿须知"格式为准、人工复核。

### 查重检测
- 知网查重（中文期刊认可）
- iThenticate / Turnitin（英文文本）

### 语言润色
- 中文学术润色：意得辑、AJE
- 英文摘要润色：American Journal Experts、Editage

## 六、投稿系统相关

### 系统要求
- 浏览器：Chrome / Firefox / Edge
- 文档格式：DOC / DOCX（Word）
- 文件大小：以系统提示为准

### 扩展资料格式
- 附录：Word 文档
- 数据：Excel / Stata `.dta` / CSV
- 代码：Stata `.do` / `.ado`、Python `.py`、R `.R`

## 七、其他工具

### 版本控制与协作
- Git + GitHub / Gitee（代码管理）
- Overleaf（LaTeX 协作）

### 笔记与知识管理
- Obsidian（Markdown 笔记）、Notion（知识管理）

## 八、常用网站

| 网站 | 用途 |
|------|------|
| https://cjyj.sufe.edu.cn/ | 《财经研究》期刊官网（投稿须知以此为准） |
| CNKI（知网） | 中文文献检索、查重 |
| Web of Science | 国际文献 |
| Google Scholar | 文献检索 |
| SSRN | 预印本 |
| RePEc / NBER | 经济学工作论文 |

## 九、注意事项

1. **数据合规**：使用数据库遵守授权协议，不要大批量爬取
2. **代码可复核**：实证代码详细注释，录用后期刊可能要求提供数据与代码
3. **版本管理**：保留完整的数据与代码版本，便于修订核对
4. **匿名处理**：投稿前确保正文、文件属性、数据说明中无作者可识别信息
5. **数据点名**：数据来源精确到数据库名称，不写"公开渠道"
