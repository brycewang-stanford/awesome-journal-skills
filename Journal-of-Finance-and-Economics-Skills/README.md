# Journal-of-Finance-and-Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="《财经研究》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Finance%20and%20Economics-c0392b)](https://cjyj.sufe.edu.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://cjyj.sufe.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《财经研究》 (Journal of Finance and Economics)** — a CSSCI-indexed comprehensive finance-and-economics journal hosted by **Shanghai University of Finance and Economics (上海财经大学)**.

This repository is opinionated. It is **not** a generic Chinese-economics writing toolbox. It is a **Journal-of-Finance-and-Economics-specific** stack covering topic selection with theoretical grounding, bilingual literature review, modern quasi-experimental identification, mechanism / heterogeneity analysis, CSSCI house style, policy implications, submission preflight, and double-blind R&R rebuttals.

> Accuracy note: word limits, fees, editorial board, and impact metrics change over time. This stack encodes the journal's **durable norms**; always verify current numbers against the official 投稿须知 (Author Guidelines) before you submit.

---

## Why a Separate Journal-of-Finance-and-Economics Skill Stack?

《财经研究》 imposes constraints that differ materially from AER / AEJ / top finance journals, and even from a pure-economics CSSCI journal:

| Constraint                | Journal of Finance and Economics                          | Implication                                                |
|---------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Discipline                | Comprehensive finance & economics (public finance, industrial, corporate finance, trade, labor, regional, digital) | Pure-management or pure-case papers are off-fit |
| Topic                     | Theoretical contribution **answering a China reality**     | "Policy evaluation only" reads as a working paper          |
| Contribution sentences    | 3–5 explicit "边际贡献" bullets in intro                    | Cannot be a single paragraph                               |
| Literature review         | Bilingual; **canonical theory citations required**         | Missing canonical theory refs is a desk-reject signal      |
| Identification            | Quasi-experimental + careful endogeneity discussion        | OLS + controls often desk-rejected                         |
| Mechanism                 | Near-mandatory                                             | Empirical papers without mechanism rarely accepted         |
| Heterogeneity             | Strongly preferred                                         | Often requested in R&R if missing                          |
| Policy implications       | Mandatory; framed as "significance" rather than "actions"  | Different from 《管理世界》 actionable-policy style         |
| Data                      | Authoritative micro data named explicitly (CSMAR / Wind / CNRDS / 工企 / 海关 / CFPS) | "Public sources" wording is a red flag |
| Abstract                  | Structured Chinese abstract + aligned English abstract     | "What we do + what we find" first, then significance       |

Generic "scientific writing" or "economics writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/journal-of-finance-and-economics-skills
/plugin install journal-of-finance-and-economics-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/journal-of-finance-and-economics-skills.git
cd journal-of-finance-and-economics-skills

mkdir -p ~/.claude/skills && cp -R skills/cfe-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cfe-* ~/.codex/skills/
```

### First Prompt

```
Use cfe-workflow to tell me which skill I should use next for my Journal-of-Finance-and-Economics manuscript.
```

---

## Default Workflow

```text
cfe-topic-selection
        ▼
cfe-literature-review
        ▼
cfe-identification
        ▼
cfe-mechanism
        ▼
cfe-heterogeneity
        ▼
cfe-tables-figures
        ▼
cfe-policy-implication
        ▼
cfe-abstract        (polish)
        ▼
cfe-style           (polish)
        ▼
cfe-submission
        ▼
cfe-rebuttal
```

`cfe-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                      | Purpose                                                        |
|---------------------------|----------------------------------------------------------------|
| `cfe-workflow`             | Router — decides which sub-skill to invoke next                |
| `cfe-topic-selection`      | Theoretical-grounding fit + China-reality + contribution sentences |
| `cfe-literature-review`    | Bilingual structure + canonical-theory checklist               |
| `cfe-identification`       | Quasi-experimental design (DID / IV / RDD / DML / PSM)         |
| `cfe-mechanism`            | Mechanism-analysis paths and writing template                  |
| `cfe-heterogeneity`        | Heterogeneity cuts: five-dimension priority                    |
| `cfe-tables-figures`       | Three-line tables, variable-definition table, figure aesthetics |
| `cfe-policy-implication`   | Significance-level policy framing (not action-level)           |
| `cfe-abstract`             | Structured Chinese abstract five-sentence pattern + blacklist phrases |
| `cfe-style`                | Language polish: empty-significance → concrete contribution     |
| `cfe-submission`           | Pre-submission checklist + manuscript template (format, word count, double-blind) |
| `cfe-rebuttal`             | Double-blind R&R response-letter structure                     |

### Resources

- [`skills/cfe-submission/templates/manuscript_template.md`](skills/cfe-submission/templates/manuscript_template.md) — Standard manuscript skeleton (abstract, variable table, references)
- [`skills/cfe-submission/templates/checklist.md`](skills/cfe-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — Chinese finance-and-economics data sources (CSMAR / Wind / CNRDS / 工企 / 海关 / CFPS) + Stata / Python / R packages

---

## Differences vs. Economic-Research Skills

| Dimension          | Journal of Finance and Economics             | Economic Research (经济研究)        |
|--------------------|----------------------------------------------|-------------------------------------|
| Discipline         | Comprehensive finance & economics            | Economics (macro / institutional)   |
| Topic preference   | Empirical, China-reality-driven with theory  | Theory-contribution-first           |
| Methods center     | Causal identification + micro data           | Identification + structural / theory|
| Policy framing     | Significance (institutional / qualitative)   | Significance (macro / qualitative)  |
| Host               | Shanghai Univ. of Finance and Economics      | CASS Institute of Economics         |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》
- [management-world-skills](https://github.com/brycewang-stanford/management-world-skills) — 《管理世界》

---

## License

MIT
