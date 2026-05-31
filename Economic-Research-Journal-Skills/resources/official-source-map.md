# 《经济研究》官方来源核查表（official source map）

> 期刊：《经济研究》（Economic Research Journal）
> 访问/核查日期：2026-05-30
>
> 重要说明：本次核查在受限网络环境下进行，**未能直连访问期刊官网/投稿系统进行实时核验**（curl 与抓取工具均被阻断）。
> 下表区分两类信息：
> - **A. 本仓库已落地、可在本地核对的事实**——来自本技能包内 `skills/er-submission/templates/` 与 `resources/external_tools.md`，技能正文据此撰写；
> - **B. 待核实（UNVERIFIED）**——版本/时点敏感或本次无法独立确认的信息，须以投稿当时官网为准。
>
> 本核查表不杜撰主编姓名、版面费金额、确切创刊年或字数硬上限；凡未确证者一律列入「待核实」。

## 一、官方/权威来源清单（建议联网逐条核实）

| 来源 | 网址（线索，须以官网为准） | 拟核实内容 | 本次状态 |
| --- | --- | --- | --- |
| 《经济研究》投审稿系统 | https://erj.ajcass.com（本仓库 `external_tools.md`、`templates/checklist.md` 记载；登录页 `https://erj.ajcass.com/Admin/user/login`） | 投稿须知、要素清单、附件要求、审稿与回避制度、是否收费、栏目 | 待核实（本次未能直连） |
| 期刊主页（README 徽章使用） | http://www.erj.cn/（README badge 链接） | 与 ajcass 系统的关系、是否为现行官网 | 待核实 |
| 中国社会科学院经济研究所 | cass.cn / 经济研究所官网（建议核实） | 主办单位身份 | 待核实 |
| 中国知网（CNKI）期刊导航 | navi.cnki.net（《经济研究》刊名页） | ISSN、CN、创刊年、出版周期、收录与栏目 | 待核实 |
| CSSCI 来源期刊目录（南京大学评价中心） | cssrac.nju.edu.cn（建议核实） | CSSCI 来源刊身份 | 待核实 |

## 二、A 类——本仓库已落地、可本地核对的《经济研究》专属事实

以下事实来自本技能包内文件，可在本地直接核对，技能正文（含模板/清单）据此撰写：

1. **投审稿系统网址**：`https://erj.ajcass.com`，登录页 `https://erj.ajcass.com/Admin/user/login`。
   - 来源：`resources/external_tools.md`「八、常用网站」；`skills/er-submission/templates/checklist.md`「投稿系统检查」。
2. **中文内容提要约 300 字；英文梗概约 4400 字符（含空格）**。
   - 来源：`skills/er-submission/templates/manuscript_template.md`、`templates/checklist.md`、`skills/er-abstract/SKILL.md`。
3. **必须标注 JEL Classification（JEL 分类号）**；中文关键词 3–8 个并附对应英文。
   - 来源：`templates/checklist.md`「摘要与关键词检查」、`templates/manuscript_template.md`。
4. **参考文献采用顺序编码制，不超过 50 条**；中文文献按姓氏拼音在前、外文在后；文中引用 (作者，年份，页码)。
   - 来源：`templates/manuscript_template.md`「参考文献」、`templates/checklist.md`「参考文献检查」。
5. **图表与公式上限**：正文表 ≤ 6 个、图 ≤ 4 个、图表合计 ≤ 8 个；数学表达式 ≤ 20 个。
   - 来源：`templates/manuscript_template.md`「图表格式 / 数学表达式格式」、`templates/checklist.md`。
6. **篇幅结构硬性下限**：引言与文献述评 ≥ 5000 字；结论与政策讨论 ≥ 1500 字。
   - 来源：`templates/manuscript_template.md`、`templates/checklist.md`「正文结构检查」。
7. **署名规范**：作者 ≤ 5 位；每位作者署名单位 ≤ 2 个、署名资助课题 ≤ 2 个；总资助课题数 ≤ 作者数 + 2；须标注通讯作者。
   - 来源：`templates/manuscript_template.md`「作者信息」、`templates/checklist.md`「作者信息检查」。
8. **匿名（双盲）投稿**：正文及文件属性中去除作者、单位、课题等可识别信息。
   - 来源：`templates/checklist.md`「投稿前格式检查」；各 SKILL.md 中的双盲要点。
9. **录用后须提交扩展资料**：附录（Word）、与统计软件匹配的数据文件/Excel、软件代码文件、（如有）权利人限制说明。
   - 来源：`templates/checklist.md`「扩展资料检查」。
10. **选题与评审口味**：理论贡献优先、紧扣中国现实问题、引言列 3–5 条边际贡献、准实验识别、机制分析近乎必备、政策含义偏「意义层」（区别于《管理世界》的「可操作层」）。
    - 来源：`skills/er-topic-selection`、`er-literature-review`、`er-identification`、`er-mechanism`、`er-policy-implication`、`er-workflow` 各 SKILL.md。

> 提示：上述 A 类事实虽可本地核对，但其权威来源仍是期刊官网；若官网与本仓库记载不一致，以官网为准，并据此更新模板与本表。

## 三、B 类——待核实清单（UNVERIFIED，须以投稿当时官网为准）

- [ ] 现行官网/投稿系统确切网址（erj.ajcass.com 与 erj.cn 的关系及哪一个为当前入口）。
- [ ] 主管/主办单位的准确表述；现任主编、编委会名单（本表未给出具体姓名，避免杜撰）。
- [ ] 是否收取审稿费 / 版面费及金额（本包未给出任何费用数字）。
- [ ] 创刊年、现行 ISSN 与 CN 刊号的精确值（本表未填写具体号码，避免误写）。
- [ ] 现行栏目设置与当期重点征稿方向 / 专栏。
- [ ] 双向匿名审稿与回避制度的官方表述（本包按「双盲」处理，细则待官网确认）。
- [ ] 上述 A 类各项数字（300 字 / 4400 字符 / ≤50 条文献 / ≤6 表 ≤4 图 / ≤20 式 / ≥5000 字等）的当期官方版本——投稿须知可能逐年微调。
- [ ] 可作对标的该刊 3–5 篇代表作（作者 + 简题 + 年份）——为避免误引，本次**未写入任何具体篇目**，待联网核实确属该刊后再补录。

> 复核方式：联网后优先访问投审稿系统 `https://erj.ajcass.com` 的「投稿须知 / 作者中心」，以 CNKI 刊名页核对 ISSN/CN/创刊年/栏目，并将上表「待核实」项逐条替换为带访问日期的确证信息。
