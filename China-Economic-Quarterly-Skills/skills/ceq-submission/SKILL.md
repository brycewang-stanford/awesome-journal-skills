---
name: ceq-submission
description: Use for the pre-submission preflight to 《经济学(季刊)》 (China Economic Quarterly, CEQ) — checking the online system (oaj.pku.edu.cn / ccj.pku.edu.cn), in-text author-date citation style (页内夹注, not footnotes), abstract limits (≤200字 中文 / ≤100词 英文), three keywords, three JEL codes, the 15,000-word length cap, reproducibility, and double-blind anonymity. Use right before submitting; verify every rule against the journal's current 投稿须知.
---

# 投稿前 preflight（ceq-submission）

## 触发时机

- 正文、识别、图表、英文摘要都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿/审稿系统：**https://www.oaj.pku.edu.cn/Journalx_jjx**（入口经 ccj.pku.edu.cn / oaj.pku.edu.cn）
- 主办：北京大学中国经济研究中心（CCER/NSD）；北京大学出版社出版
- 刊期：刊名为"季刊"，但**自 2021 年起全年六期**
- 引用体例：正文**作者—年份页内夹注**（如 "Black (1948: pp.66)"），**非脚注页下注**；脚注仅作内容性注释
- 篇幅：全文一般**不超过 15,000 字**
- 摘要：中文 **≤ 200 字**；英文 **≤ 100 词**；**三个**中英文关键词；**三个** JEL 号
- 评审：**双向匿名**

> 体例与字数以官网**最新《投稿须知》/《投稿体例》**为准。规则与刊期会变，投前务必复核，不要凭记忆。

## 体例 checklist

- [ ] 正文引用用**作者—年份夹注**，参考文献按作者姓名首字母排序
- [ ] **未**误用脚注当文献出处注（脚注仅内容性注释）
- [ ] 全文 ≤ 15,000 字；标题/表/图/等式/脚注分别连续编号
- [ ] 中文摘要 ≤ 200 字；英文摘要 ≤ 100 词（见 `ceq-abstract-english`）
- [ ] 三个中英文关键词；**三个 JEL 号选准**（JEL 决定分派主编）
- [ ] 结构齐：前言与文献回顾 / 理论或实证分析 / 结论与建议 / 附录 / 参考文献
- [ ] 图表自洽、有出处（见 `ceq-figures`）

## 可复现 hygiene

- [ ] 数据来源、样本筛选、变量构造可复述
- [ ] 估计量与软件包版本可交代（如 csdid / did_multiplegt）
- [ ] 主结果脚本/数据按要求备齐（应编辑/审稿要求）

## 双向匿名 hygiene

- [ ] 正文/致谢/脚注去除可识别作者身份信息
- [ ] 自引改第三人称或匿名占位
- [ ] 文件属性（作者名）已清除
- [ ] 基金项目等致谢信息按系统要求放置（不破坏匿名）

## 提交前内容复核（调用其它 skill）

- [ ] 识别假设显式且有支持（`ceq-identification`）
- [ ] 交错 DID 已过现代合规（`ceq-modern-did`）
- [ ] 推断细节经得起技术审稿（`ceq-inference`）
- [ ] 机制可证伪、能区分竞争渠道（`ceq-mechanism`）
- [ ] 主结果有自洽主图（`ceq-figures`）
- [ ] 英文摘要无套话、对标文献（`ceq-abstract-english`）

## 反模式

- 凭记忆套体例，不查最新《投稿须知》
- 用脚注/尾注替代作者—年份夹注
- JEL 号随便选，导致分派错主编
- 超 15,000 字硬投
- 忘清匿名信息就投双盲

## 输出格式

```
【体例】夹注□ 参考文献排序□ 编号连续□ 篇幅≤15000□
【摘要/关键词/JEL】中文≤200□ 英文≤100词□ 3关键词□ 3JEL□
【可复现】数据□ 估计量版本□ 脚本□
【匿名】已清理 / 待清理 <点>
【系统】oaj.pku.edu.cn/Journalx_jjx 入口已确认
【内容复核】识别□ DID□ 推断□ 机制□ 图□ 英文摘要□
【结论】可投 / 待修 <清单>
```
