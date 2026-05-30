# NEJM Skills

<p align="center">
  <img src="assets/cover.png" alt="The New England Journal of Medicine cover card" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-NEJM-b1141c)](https://www.nejm.org/)
[![Scope](https://img.shields.io/badge/scope-clinical%20medicine-1f6feb)](https://www.nejm.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **The New England Journal of Medicine** (NEJM) — the flagship clinical-medicine journal.

This pack is opinionated. It is **not** a generic "medical writing" toolbox. It is an **NEJM-specific** stack that encodes the journal's editorial bar — **practice-changing clinical impact backed by methodological rigor and generalizability** — and the concrete clinical conventions that follow: mandatory prospective trial registration plus a protocol and statistical analysis plan, EQUATOR reporting guidelines with the CONSORT flow diagram, the structured ≤250-word abstract with a registration number, terse IMRAD writing, clinical statistics (confidence intervals over P, intention-to-treat, absolute risk and NNT), clinical display items (Table 1, Kaplan–Meier, forest plots), clinical ethics (IRB, informed consent, ICMJE disclosures, data-sharing statement), and Vancouver/ICMJE references.

---

## Why a Separate NEJM Skill Stack?

NEJM imposes clinical constraints that differ materially from basic-science journals — and from its clinical siblings:

| Constraint                | NEJM                                                          | Implication                                                  |
|---------------------------|---------------------------------------------------------------|-------------------------------------------------------------|
| Editorial bar             | Practice-changing impact + rigor + generalizability           | Most papers are **desk-rejected without review** if narrow  |
| Trial registration        | **Prospective** registration (ClinicalTrials.gov/ICTRP) before enrollment | An unregistered trial is generally disqualified      |
| Protocol + SAP            | Submitted and published with trials; SAP pre-specified        | A post-hoc analysis plan is a credibility problem           |
| Reporting guidelines      | EQUATOR: **CONSORT** (+ flow diagram) / STROBE / PRISMA       | An RCT without a CONSORT flow diagram is not ready          |
| Abstract                  | **Structured ≤250 words**: Background/Methods/Results/Conclusions, with NCT number + funding | Unstructured abstracts are off-style       |
| Statistics                | **CIs over bare P**; ITT primary; absolute risk + NNT         | Relative-risk-only / P-only reporting is flagged            |
| Display items             | Table 1 (no baseline P values); Kaplan–Meier with numbers-at-risk; forest plots | Wrong conventions read as inexperience       |
| Ethics & integrity        | IRB + consent; **ICMJE disclosures + data-sharing statement** | Missing disclosures/data-sharing block submission           |
| References                | **Vancouver / ICMJE** numbered, six authors then et al.       | Author–date style must be converted                         |
| Over-claiming / causation | A top rejection reason; causal claims on observational data flagged | Conclusions must be calibrated to the design          |

Generic "medical writing" packs do not encode these venue and reporting constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install nejm-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/NEJM-Skills

mkdir -p ~/.claude/skills && cp -R skills/nejm-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/nejm-* ~/.codex/skills/
```

### First Prompt

```
Use nejm-workflow to tell me which skill I should use next for my clinical manuscript targeted at NEJM.
```

---

## Default Workflow

```text
nejm-fit             (clear the practice-changing bar first)
        ▼
nejm-study-design    (trial registration + protocol + SAP; design rigor)
        ▼
nejm-reporting       (CONSORT / STROBE / PRISMA + required flow diagram)
        ▼
nejm-writing         (Original Article vs Brief Report; terse IMRAD)
        ▼
nejm-statistics      (CIs, ITT, multiplicity, pre-specified subgroups, NNT)
        ▼
nejm-figures-tables  (Table 1, Kaplan–Meier, forest plots, CONSORT diagram)
        ▼
nejm-ethics          (IRB, consent, ICMJE disclosures, data-sharing statement)
        ▼
nejm-abstract        (structured ≤250-word abstract with NCT number — polish)
        ▼
nejm-citation        (Vancouver / ICMJE numbered style — polish)
        ▼
nejm-submission      (preflight + cover-letter template)
        ▼
nejm-rebuttal        (after review — incl. the statistical reviewer)
```

`nejm-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                 | Purpose                                                                       |
|-----------------------|-------------------------------------------------------------------------------|
| `nejm-workflow`       | Router — decides which sub-skill to invoke next                                |
| `nejm-fit`            | Desk-reject filter: practice-changing impact + rigor + generalizability; venue routing |
| `nejm-study-design`   | Prospective trial registration, protocol + SAP, randomization/blinding/ITT     |
| `nejm-reporting`      | EQUATOR guideline selection; CONSORT/STROBE/PRISMA checklist + flow diagram     |
| `nejm-abstract`       | Structured ≤250-word abstract (Background/Methods/Results/Conclusions) + NCT    |
| `nejm-writing`        | Original Article vs Brief Report; terse IMRAD; sober Discussion + limitations   |
| `nejm-statistics`     | CIs over P; ITT; multiplicity; pre-specified subgroups + interaction; NNT       |
| `nejm-figures-tables` | Table 1 (no baseline P); Kaplan–Meier with numbers-at-risk; forest plots; CONSORT |
| `nejm-ethics`         | IRB + consent; ICMJE disclosures + authorship; funding role; data-sharing       |
| `nejm-citation`       | Vancouver / ICMJE numbered style; six authors then et al.; NLM abbreviations    |
| `nejm-submission`     | Full clinical preflight checklist + templates                                   |
| `nejm-rebuttal`       | Decision triage; statistical-reviewer responses; point-by-point letter          |

### Resources

- [`skills/nejm-submission/templates/checklist.md`](skills/nejm-submission/templates/checklist.md) — full clinical preflight checklist
- [`skills/nejm-submission/templates/cover_letter_template.md`](skills/nejm-submission/templates/cover_letter_template.md) — clinical cover-letter scaffold
- [`resources/external_tools.md`](resources/external_tools.md) — registries, EQUATOR guidelines, ICMJE/ethics standards, data-sharing platforms, stats tooling, and key NEJM author pages

---

## Differences vs. Lancet / JAMA / BMJ

| Dimension          | NEJM                              | The Lancet                        | JAMA                               | BMJ                                |
|--------------------|-----------------------------------|-----------------------------------|------------------------------------|------------------------------------|
| Bar                | Practice-changing, definitive     | Practice-changing + global health | Practice-changing, large audience  | Rigorous + open-science ethos      |
| Tone               | Terse, plain, ~2700-word articles | Broader framing/advocacy          | Structured, key-points discipline  | Methods/registration emphasis      |
| Abstract           | Structured ≤250 w, 4 sections     | Own structured format             | Structured + Key Points            | Structured format                  |
| Review             | Single-blind; statistical reviewer| Single-blind                      | Statistical review common          | Open peer review (often public)    |
| Shared (ICMJE)     | Registration · CONSORT · disclosures · data-sharing — **all four enforce these** | | | |

The registration, reporting-guideline, statistics, and ethics work transfers across all four — but **format and tone do not**. For Lancet and Cell, see the sibling packs in [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills); JAMA and BMJ are venue-routing comparators, not bundled packs here.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) · [Lancet-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Lancet-Skills) · [PNAS-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/PNAS-Skills) · [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills)

---

## Disclaimer

This is an independent, community-built skill pack. It is **not** affiliated with, endorsed by, or produced by NEJM, the Massachusetts Medical Society, or any of its journals. All targets (word counts, reference limits, style rules, policy details) reflect publicly documented author guidelines and ICMJE recommendations at the time of writing — **always confirm against the current [NEJM Author Center](https://www.nejm.org/author-center) and [ICMJE Recommendations](http://www.icmje.org/recommendations/)** before submitting.

---

## License

MIT
