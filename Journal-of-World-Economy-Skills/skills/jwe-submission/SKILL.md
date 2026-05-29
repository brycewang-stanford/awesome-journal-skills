---
name: jwe-submission
description: Use for the pre-submission preflight to 《世界经济》 (The Journal of World Economy) — checking footnote (页下注) conventions, reference list at the end, 内容提要 ≤ 300 chars + 3–5 keywords, bilingual title, blind-review anonymity, and the official online submission site (www.jweonline.cn). Use right before submitting; verify every rule against the journal's current 投稿须知.
---

# 投稿前 preflight（jwe-submission）

## 触发时机

- 正文、识别、渠道、文风都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿系统：**www.jweonline.cn**（编辑部唯一官方投稿网址；编辑部邮箱 jwe@cass.org.cn）
- 注释体例：**脚注（页下注）**置当页下；**参考文献置文末**，文中与文末一一对应，中文在前外文在后
- 内容提要 **不超过 300 字**；关键词 **3–5 个**；配中英文标题
- 投稿封面注明中英文标题、作者、单位、通讯方式；**正文不得出现作者姓名**（匿名外审）
- 主办：中国世界经济学会 + 中国社会科学院世界经济与政治研究所；月刊

> 体例与字数以官网**最新《投稿须知》**为准。该刊投稿系统曾迁移、网上有第三方代投站点——**只认 www.jweonline.cn**，不要凭记忆或第三方页面投稿。

## 体例 checklist

- [ ] 注释统一为**页下注（脚注）**；**参考文献置文末**且与文中一一对应
- [ ] 参考文献中文在前、外文在后，按拼音 / 字母排序；著录含刊名期号 / 出版年单位版次地点
- [ ] 引文准确可核查；直接引用标页码
- [ ] 中英文标题齐全；内容提要 ≤ 300 字、关键词 3–5
- [ ] 外国人名附原文或用原文；专业术语规范
- [ ] 图表规范、编号连续、有数据来源（PPML/GVC/shift-share 口径已注）
- [ ] 基金项目、作者信息按封面要求填写

## 匿名评审 hygiene

- [ ] 正文 / 注释 / 致谢中**去除可识别作者身份**的信息
- [ ] 自引改为第三人称或匿名占位
- [ ] 投稿封面与正文分离，正文不出现作者姓名
- [ ] 文件属性（作者名）已清除

## 提交前内容复核（调用其它 skill）

- [ ] 开放维度立得住（`jwe-fit-positioning`）
- [ ] 识别（含 shift-share 推断）站得住（`jwe-identification`）
- [ ] 传导渠道讲清（`jwe-transmission-channel`）
- [ ] 政策落在开放政策层（`jwe-policy-implication`）

## 反模式

- 凭记忆套体例，不查最新《投稿须知》
- 用尾注 / 纯文中夹注替代页下注，或参考文献不与文中对应
- 经第三方"代投"站点投稿，未认准 www.jweonline.cn
- 忘清匿名信息 / 正文留作者名就投

## 输出格式

```
【体例】页下注□ 文末参考文献□ 中英标题□ 著录规范□
【字数】内容提要 X 字（≤300）/ 关键词 X 个（3–5）
【匿名】已清理 / 待清理 <点>
【系统】www.jweonline.cn 官方入口已确认
【内容复核】定位□ 识别□ 渠道□ 政策□
【结论】可投 / 待修 <清单>
```
