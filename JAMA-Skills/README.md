# JAMA Skills

<p align="center">
  <img src="assets/cover.svg" alt="JAMA journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JAMA-c0392b)](https://jamanetwork.com/journals/jama)
[![Index](https://img.shields.io/badge/index-MEDLINE%20%2F%20ICMJE-1f6feb)](https://jamanetwork.com/journals/jama)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for clinical manuscripts targeted at **JAMA (Journal of the American Medical Association)** — published by the American Medical Association and one of the "big-four" general medical journals alongside NEJM, The Lancet, and The BMJ.

This repository is opinionated. It is **not** a generic medical-writing toolbox. It is a **JAMA-specific** stack covering general-medical-importance scope checks, study design, EQUATOR reporting standards (CONSORT / STROBE / PRISMA / STARD), statistical rigor with effect sizes and 95% CIs, the JAMA structured abstract and Key Points box, trial registration and ICMJE ethics/disclosures, figures and tables, house style, the cover letter, submission preflight, and peer-review revision.

---

## Why a Separate JAMA Skill Stack?

JAMA imposes constraints that differ materially from specialty or basic-science journals:

| Constraint            | JAMA                                                          | Implication                                                  |
|-----------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| Scope                 | General medical importance for a broad clinician readership   | Narrow subspecialty or mechanistic-only papers are off-fit   |
| Core designs          | RCTs, observational studies, diagnostic studies, reviews      | Underpowered pilots / uncontrolled series rarely fit         |
| Reporting standard    | Matching EQUATOR guideline + flow diagram required            | Missing CONSORT/PRISMA diagram is a red flag                 |
| Trial registration    | Prospective registration before enrollment (ICMJE)            | Retrospective registration generally cannot be remedied      |
| Statistics            | Effect sizes with 95% CIs; ITT; multiplicity; **stat review** | P-values without estimates/CIs fail dedicated stat review    |
| Abstract              | JAMA structured headings (~350 words) + Key Points box        | A block-paragraph abstract is off-format                     |
| Ethics / disclosures  | IRB, consent, ICMJE authorship + COI, data sharing            | Missing statements stall or sink a submission                |
| Conclusions           | Bounded by the pre-specified primary outcome                  | "Spin" and causal language for associations are punished     |
| House style           | AMA Manual of Style; person-first language                    | Off-style notation/units signal an unprepared manuscript     |

Generic "scientific writing" packs do not address these constraints. Verify all current word/reference/figure limits, fees, and editor information on JAMA's official Instructions for Authors page.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jama-skills
/plugin install jama-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jama-skills.git
cd jama-skills

mkdir -p ~/.claude/skills && cp -R skills/jama-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jama-* ~/.codex/skills/
```

### First Prompt

```
Use jama-workflow to tell me which skill I should use next for my JAMA manuscript.
```

---

## Default Workflow

```text
jama-scope-fit
        ▼
jama-study-design
        ▼
jama-reporting-standards
        ▼
jama-statistics
        ▼
jama-figures-tables
        ▼
jama-structured-abstract
        ▼
jama-ethics-registration
        ▼
jama-writing-style          (polish)
        ▼
jama-cover-letter
        ▼
jama-submission
        ▼
jama-peer-review-revision
```

`jama-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                        | Purpose                                                              |
|------------------------------|----------------------------------------------------------------------|
| `jama-workflow`              | Router — decides which sub-skill to invoke next                      |
| `jama-scope-fit`             | General-medical-importance test + article-type match                |
| `jama-study-design`          | Design choice + internal-validity safeguards (ITT, bias, power)     |
| `jama-reporting-standards`   | EQUATOR checklist + flow diagram (CONSORT / STROBE / PRISMA / STARD) |
| `jama-statistics`            | Effect sizes + 95% CIs, multiplicity, ITT, dedicated stat review    |
| `jama-figures-tables`        | Flow diagram, baseline table, forest/KM plots, exhibit conventions  |
| `jama-structured-abstract`   | JAMA structured abstract + Key Points box (Question/Findings/Meaning)|
| `jama-ethics-registration`   | Registration, IRB/consent, ICMJE authorship/COI, data sharing       |
| `jama-writing-style`         | AMA style, spin removal, associational language, limitations        |
| `jama-cover-letter`          | Editor-facing pitch of general medical importance + declarations    |
| `jama-submission`            | Pre-submission preflight + checklist & manuscript templates         |
| `jama-peer-review-revision`  | Point-by-point response to reviewer + statistical-review comments   |

### Resources

- [`skills/jama-submission/templates/manuscript_template.md`](skills/jama-submission/templates/manuscript_template.md) — JAMA manuscript skeleton (structured abstract, Key Points, IMRaD, required statements)
- [`skills/jama-submission/templates/checklist.md`](skills/jama-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — EQUATOR guidelines, registries (ClinicalTrials.gov / PROSPERO), R / Stata / Python packages, and reference/figure tools

---

## Differences vs. Specialty-Journal Skills

| Dimension          | JAMA (general medicine)            | Specialty / basic-science journals     |
|--------------------|------------------------------------|----------------------------------------|
| Readership         | Broad clinicians across medicine   | Subspecialists / bench scientists      |
| Importance bar     | General medical importance         | Field-specific or mechanistic novelty  |
| Outcomes           | Patient-relevant endpoints         | Surrogate / mechanistic endpoints often ok |
| Reporting standard | EQUATOR + flow diagram enforced    | Varies by journal                      |
| Statistical review | Dedicated stat review              | Often standard peer review only        |

---

## What This Repository Does Not Do

- It does not write a submission-ready manuscript for you.
- It does not simulate a specific editor's preferences.
- It does not store JAMA's rejection rates, fees, or impact factor (verify on the journal site).
- It does not judge whether your clinical question is truly important — that is your call.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》 (Economic Research Journal)

---

## License

MIT
